#!/usr/bin/env python3
"""Compile validated first-loop JSON evidence into a complete Markdown appendix."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parent
FIELDS_PATH = ROOT / "fields.yaml"
RESULTS_DIR = ROOT / "results"
OUTPUT_PATH = ROOT / "report.md"

CATEGORY_MAPPING = {
    "Basic Info": ["basic_info", "Basic Info"],
    "Technical Features": ["technical_features", "technical_characteristics", "Technical Features"],
    "Performance Metrics": ["performance_metrics", "performance", "Performance Metrics"],
    "Milestone Significance": ["milestone_significance", "milestones", "Milestone Significance"],
    "Business Info": ["business_info", "commercial_info", "Business Info"],
    "Competition & Ecosystem": ["competition_ecosystem", "competition", "Competition & Ecosystem"],
    "History": ["history", "History"],
    "Market Positioning": ["market_positioning", "market", "Market Positioning"],
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def contains_uncertain(value: Any) -> bool:
    if isinstance(value, str):
        return "[uncertain]" in value.lower()
    if isinstance(value, list):
        return any(contains_uncertain(item) for item in value)
    if isinstance(value, dict):
        return any(contains_uncertain(item) for item in value.values())
    return False


def find_field(data: dict[str, Any], field: str, category: str) -> Any:
    if field in data:
        return data[field]
    category_keys = [category, slug(category).replace("-", "_")]
    category_keys.extend(CATEGORY_MAPPING.get(category, []))
    for key in category_keys:
        value = data.get(key)
        if isinstance(value, dict) and field in value:
            return value[field]
    stack: list[Any] = list(data.values())
    while stack:
        value = stack.pop()
        if isinstance(value, dict):
            if field in value:
                return value[field]
            stack.extend(value.values())
        elif isinstance(value, list):
            stack.extend(value)
    return None


def format_value(value: Any, depth: int = 0) -> str:
    if isinstance(value, dict):
        lines = []
        for key, item in value.items():
            label = key.replace("_", " ").title()
            rendered = format_value(item, depth + 1)
            if "\n" in rendered or len(rendered) > 140:
                lines.append(f"- **{label}:** {rendered}")
            else:
                lines.append(f"- **{label}:** {rendered}")
        return "\n".join(lines)
    if isinstance(value, list):
        if not value:
            return ""
        if all(isinstance(item, dict) for item in value):
            rendered = []
            for item in value:
                pieces = [f"{key.replace('_', ' ')}: {format_value(val, depth + 1)}" for key, val in item.items()]
                rendered.append("- " + " | ".join(pieces))
            return "\n".join(rendered)
        if len(value) <= 4 and all(len(str(item)) <= 100 for item in value):
            return ", ".join(str(item) for item in value)
        return "\n".join(f"- {format_value(item, depth + 1)}" for item in value)
    if isinstance(value, bool):
        return "Yes" if value else "No"
    return str(value)


def item_name(data: dict[str, Any], source: Path) -> str:
    value = find_field(data, "research_object", "Scope and pathway")
    return str(value or source.stem.replace("_", " ").title())


def judgment(data: dict[str, Any]) -> str | None:
    value = find_field(data, "go_no_go_assessment", "Experiment and decision")
    if contains_uncertain(value):
        return None
    if isinstance(value, dict):
        return str(value.get("judgment", "Recorded in detail"))
    return str(value) if value else None


def main() -> None:
    schema = yaml.safe_load(FIELDS_PATH.read_text())
    categories = schema["field_categories"]
    records = []
    for source in sorted(RESULTS_DIR.glob("*.json")):
        data = json.loads(source.read_text())
        records.append((source, data, item_name(data, source)))

    lines = [
        "# Firescape first-loop evidence appendix",
        "",
        "This file is generated from the independently researched and schema-validated JSON records. "
        "Claims explicitly marked uncertain, and fields named in each record's `uncertain` array, are omitted.",
        "",
        "## Contents",
        "",
    ]
    for index, (_, data, name) in enumerate(records, 1):
        summary = judgment(data)
        suffix = f" — Decision: {summary}" if summary else ""
        lines.append(f"{index}. [{name}](#{slug(name)}){suffix}")

    defined_fields = {field["name"] for category in categories for field in category["fields"]}
    internal_fields = {"_source_file", "uncertain"}

    for index, (source, data, name) in enumerate(records, 1):
        uncertain = set(data.get("uncertain", [])) if isinstance(data.get("uncertain"), list) else set()
        lines.extend(["", f"## {index}. {name}", "", f"**Evidence record:** `{source.name}`", ""])
        for category in categories:
            rendered_fields = []
            for field in category["fields"]:
                field_name = field["name"]
                if field_name in internal_fields or field_name in uncertain:
                    continue
                value = find_field(data, field_name, category["category"])
                if value is None or value == "" or contains_uncertain(value):
                    continue
                rendered_fields.append((field_name, value))
            if not rendered_fields:
                continue
            lines.extend([f"### {category['category']}", ""])
            for field_name, value in rendered_fields:
                lines.extend([f"#### {field_name.replace('_', ' ').title()}", "", format_value(value), ""])

        extra = []
        for key, value in data.items():
            if key in defined_fields or key in internal_fields or key in uncertain:
                continue
            if value is None or value == "" or contains_uncertain(value):
                continue
            extra.append((key, value))
        if extra:
            lines.extend(["### Other Info", ""])
            for key, value in extra:
                lines.extend([f"#### {key.replace('_', ' ').title()}", "", format_value(value), ""])

    OUTPUT_PATH.write_text("\n".join(lines).rstrip() + "\n")
    print(f"Wrote {OUTPUT_PATH} from {len(records)} evidence records")


if __name__ == "__main__":
    main()
