# Firescape Research Backlog

This backlog defines the research program required to determine whether Firescape should exist.

It is not a generic software feature list. Each item should resolve an uncertainty, falsify a hypothesis, establish a baseline, or create evidence that changes the direction of the project.

## Backlog rules

1. **Research before platform.** Do not build statewide product infrastructure before the adversarial-search hypothesis survives a controlled experiment.
2. **Baselines before novelty claims.** Every learned or adaptive method must compete against random, stratified, historical, and expert-authored scenarios under the same full-simulation budget.
3. **Evidence before fidelity claims.** A detailed simulator with weak inputs is still weak evidence.
4. **Held-out attacks before intervention claims.** A repair is not robust because it fixes the scenario that produced it.
5. **Worst-group constraints before average gains.** An intervention that improves average clearance while harming the least-served population is rejected.
6. **Negative results are deliverables.** Failed hypotheses, simulator artifacts, and inaccessible-data findings should be published.
7. **No actor, no priority.** High-priority applied work must connect to an identifiable planning, exercise, infrastructure, or evidence decision.
8. **No statewide town ranking without comparable calibration.** Publish intervention opportunities and evidence states, not false-precision community league tables.

## Priority definitions

| Priority | Meaning |
|---|---|
| **P0** | Required to determine whether the central research thesis is valid. Blocks scaling. |
| **P1** | Required for credible transfer, intervention ranking, and California-wide usefulness. |
| **P2** | Valuable after the core method works and independent users appear. |
| **Deferred** | Explicitly excluded until a stated prerequisite changes. |

## Status definitions

| Status | Meaning |
|---|---|
| **Proposed** | Question and experiment are defined but not yet frozen. |
| **Ready** | Inputs, baselines, acceptance criteria, and budget are frozen. |
| **Running** | Experiment is executing; success criteria may no longer change. |
| **Supported** | Evidence passed the predeclared test. |
| **Rejected** | Evidence failed the predeclared test. |
| **Blocked** | A named dependency prevents a meaningful test. |

## Research-item template

Every new item should include:

- **Question**
- **Hypothesis**
- **Why it matters**
- **Experiment**
- **Strongest baselines**
- **Success criterion**
- **Kill or downgrade condition**
- **Dependencies**
- **Expected open artifact**
- **Decision or actor affected**

## P0 — Prove or reject the core thesis

### FIRE-R001 — Exact-competitor and baseline contract

**Status:** Proposed
**Question:** What do existing wildfire-evacuation systems already accomplish, and what precise residual claim remains for Firescape?

**Hypothesis:** Existing systems provide coupled simulation and scenario analysis, but no accessible system demonstrates the complete adversarial falsification, counterexample minimization, intervention retesting, and evidence-gated ranking loop.

**Why it matters:** Firescape should not spend years recreating WUI-NITY, Ladris, Genasys, or established academic models.

**Experiment:** Build a dated capability matrix covering WUI-NITY, Ladris Fire/Evac, Genasys Protect, WUI-Go, recent coupled agent-based frameworks, fire-trigger models, robust evacuation optimization, and California traffic studies. Reproduce accessible baselines where possible.

**Strongest baselines:** WUI-NITY 4; Ladris Fire + Evac; recent modular fire–traffic–behavior frameworks; scenario-based evacuation studies.

**Success criterion:** A technically specific residual contribution remains after exact comparison, with at least one plausible adopting research or planning actor.

**Kill or downgrade condition:** An existing accessible system already provides the full loop and can accept the intended open contribution directly. In that case, Firescape should become a module or upstream contribution rather than a standalone platform.

**Dependencies:** Literature and product access; practitioner interviews later.

**Expected open artifact:** `research/landscape/competitor-capability-matrix.md` with sources and dated corrections.

**Decision or actor affected:** Project scope; potential collaborators; funding narrative.

### FIRE-R002 — Define the safety oracle

**Status:** Proposed
**Question:** What computational event constitutes a plan failure?

**Hypothesis:** Queue overtake, unsafe-road person-minutes, loss of every safe path, emergency-access obstruction, and missed zone safety deadlines form a sufficient initial oracle set.

**Why it matters:** Adversarial search is meaningless if it optimizes a convenient but causally irrelevant score.

**Experiment:** Specify outcome definitions on small analytically understandable networks. Review them against documented wildfire evacuation failures and NIST evacuation concepts.

**Strongest baselines:** Clearance time alone; total travel time; required-safe-egress-time versus available-safe-egress-time comparisons.

**Success criterion:** The oracle detects known dangerous toy cases, distinguishes congestion from unsafe congestion, and does not hide a failed zone behind good aggregate performance.

**Kill or downgrade condition:** No public-data-compatible proxy can connect simulation outcomes to meaningful safety conditions. Firescape would then be limited to traffic performance research.

**Dependencies:** FIRE-R001; documented event mechanisms.

**Expected open artifact:** Versioned oracle specification, golden cases, and executable tests.

**Decision or actor affected:** Every later research result.

### FIRE-R003 — Plausibility-envelope specification

**Status:** Proposed
**Question:** How can the adversary search bad-to-worst combinations without inventing nonsense?

**Hypothesis:** Provenance-bearing marginal ranges plus explicit causal compatibility constraints can exclude obvious impossibilities while preserving rare compound failures.

**Why it matters:** An unconstrained adversary will maximize simulator artifacts and impossible combinations.

**Experiment:** Define scenario schemas for fire, warning, behavior, traffic, and institutions. Construct adversarial examples that are individually valid but jointly impossible, and test rejection logic.

**Strongest baselines:** Independent uniform ranges; expert-authored scenario sets; fully joint probabilistic models where available.

**Success criterion:** All intentionally incompatible test cases are rejected with legible reasons, while all predeclared plausible rare cases remain searchable.

**Kill or downgrade condition:** Joint plausibility requires proprietary incident data or expert judgment unavailable to the project. Restrict the initial envelope and state the limitation.

**Dependencies:** FIRE-R001; FIRE-R002.

**Expected open artifact:** Scenario schema, provenance format, constraint library, and coverage-report template.

**Decision or actor affected:** Researchers and reviewers assessing whether a failure is credible.

### FIRE-R004 — Golden failure worlds

**Status:** Proposed
**Question:** Can Firescape reliably find and explain failures whose causes are already known?

**Hypothesis:** A small suite of synthetic networks can exercise queue overtake, merge gridlock, harmful staging, road isolation, emergency-access conflict, warning compression, and worst-group regression.

**Why it matters:** Real geography is too complex to diagnose search and certification bugs initially.

**Experiment:** Create deterministic toy systems with known failure boundaries and necessary causal variables.

**Strongest baselines:** Exhaustive enumeration on the small scenario spaces.

**Success criterion:** Firescape rediscovers every seeded failure, identifies the correct necessary variables, and preserves vehicle or flow conservation.

**Kill or downgrade condition:** The architecture cannot reproduce known failures deterministically. Do not connect a real community until fixed.

**Dependencies:** FIRE-R002; FIRE-R003.

**Expected open artifact:** Synthetic benchmark package with analytical expectations and regression tests.

**Decision or actor affected:** Firescape maintainers and external algorithm contributors.

### FIRE-R005 — Equal-budget scenario-selection baselines

**Status:** Proposed
**Question:** What performance must adversarial search beat?

**Hypothesis:** Uniform Monte Carlo is weak, but stratified, quasi-random, historical, expert-authored, cross-entropy, and importance-sampling baselines will be competitive.

**Why it matters:** Comparing only against random sampling would inflate novelty and usefulness.

**Experiment:** Freeze simulation budgets and implement each baseline against the golden worlds and first geographical case.

**Strongest baselines:** Exhaustive enumeration where possible; expert cases; cross-entropy and adaptive importance sampling.

**Success criterion:** Every baseline emits the same accounting: proposals, invalid cases, simulator calls, failures, severity, diversity, and compute.

**Kill or downgrade condition:** A simple baseline saturates failure discovery at trivial cost. Focus on certification, intervention evaluation, or a harder scenario domain instead.

**Dependencies:** FIRE-R003; FIRE-R004.

**Expected open artifact:** Baseline library and frozen benchmark protocol.

**Decision or actor affected:** Scientific novelty assessment.

### FIRE-R006 — First adversarial-search superiority test

**Status:** Proposed
**Question:** Can an adaptive search discover more severe and causally diverse failures per expensive simulation than strong baselines?

**Hypothesis:** A transparent cross-entropy or quality-diversity search will outperform random and stratified sampling on narrow failure regions while retaining multiple failure families.

**Why it matters:** This is the central computational claim.

**Experiment:** Pre-register a fixed budget, seeds, scenario envelope, objectives, diversity descriptors, and superiority threshold. Run the adaptive method and all FIRE-R005 baselines.

**Strongest baselines:** Best-performing FIRE-R005 method, not merely uniform random.

**Success criterion:** A predeclared improvement in plausibility-adjusted severe failures and causal-family coverage per full simulation, repeated across seeds.

**Kill or downgrade condition:** No meaningful improvement, improvement disappears after compute accounting, or discoveries are mostly invalid. Stop building the adversarial platform until the cause is understood.

**Dependencies:** FIRE-R002 through FIRE-R005.

**Expected open artifact:** Reproducible benchmark report including negative and failed runs.

**Decision or actor affected:** Go/no-go for the project.

### FIRE-R007 — Failure reproduction and minimization

**Status:** Proposed
**Question:** Can a severe simulated outcome be converted into a stable, understandable causal certificate?

**Hypothesis:** Seeded replay, robustness checks, and delta-debugging can separate necessary causal variables from severity amplifiers.

**Why it matters:** Planners cannot use a million-dimensional scenario vector or a one-off stochastic failure.

**Experiment:** Apply reproduction thresholds and variable-removal tests to known golden failures and FIRE-R006 discoveries.

**Strongest baselines:** Raw worst scenario; feature importance from a surrogate; analyst-authored explanation.

**Success criterion:** Certificates reproduce above the frozen threshold, remove irrelevant perturbations, and preserve necessary causes.

**Kill or downgrade condition:** Failures are too unstable to reproduce or minimization returns misleading causes. Publish them only as exploratory anomalies.

**Dependencies:** FIRE-R004; FIRE-R006.

**Expected open artifact:** Failure-certificate schema, minimizer, and certificate registry fixtures.

**Decision or actor affected:** Planners, reviewers, and intervention designers.

### FIRE-R008 — Intervention attack–repair–retest proof

**Status:** Proposed
**Question:** Does adversarial discovery lead to better repairs than baseline scenario testing?

**Hypothesis:** Interventions selected against verified failure families will reduce held-out safety tail risk more than interventions selected from baseline scenarios alone.

**Why it matters:** Finding catastrophes without improving a decision is not sufficient.

**Experiment:** Freeze a small intervention catalog—zone timing, release spacing, route split, traffic control, warning delay, and assisted capacity. Select interventions using separate discovery sets, then attack them using unseen scenarios and an independent search.

**Strongest baselines:** Best intervention under random scenarios; best average-clearance intervention; expert-selected intervention.

**Success criterion:** At least one intervention materially reduces held-out tail risk without worsening the worst-served group and without excessive operational complexity.

**Kill or downgrade condition:** Repairs only solve their generating examples, reverse under modest parameter changes, or require unavailable controls. Limit Firescape to failure discovery and evidence prioritization.

**Dependencies:** FIRE-R002; FIRE-R006; FIRE-R007.

**Expected open artifact:** Intervention cards, held-out attack report, and residual-failure set.

**Decision or actor affected:** Emergency managers and transportation planners.

### FIRE-R009 — Evidence-gated intervention ranking

**Status:** Proposed
**Question:** Can Firescape rank interventions without laundering uncertainty into false precision?

**Hypothesis:** Separate dimensions plus multiplicative evidence and feasibility gates will produce more defensible priorities than additive scores or modeled harm reduction alone.

**Why it matters:** A spectacular simulated benefit is not useful when the road capacity is unknown or nobody can implement the intervention.

**Experiment:** Construct intervention cases containing fatal evidence, equity, actor, and feasibility weaknesses. Compare geometric, additive, benefit–cost-only, and expert rankings under sensitivity analysis.

**Strongest baselines:** Additive multi-criteria score; modeled benefit–cost; expert ordering.

**Success criterion:** Fatal weaknesses cannot be averaged away, close scores remain ties, and rank sensitivity is visible.

**Kill or downgrade condition:** Reasonable weights or evidence assumptions produce arbitrary rank reversals. Publish dimensions and tiers without a headline rank.

**Dependencies:** FIRE-R008; practitioner review eventually.

**Expected open artifact:** Ranking specification, test cases, and score-sensitivity report.

**Decision or actor affected:** Agencies prioritizing studies or interventions.

### FIRE-R010 — Paradise–Magalia end-to-end proof

**Status:** Proposed
**Question:** Does the complete method work in a geographically grounded, historically informed California case?

**Hypothesis:** Public terrain, fuel, road, weather, population, and Camp Fire evidence are sufficient to test the computational hypothesis without claiming an exact historical reconstruction.

**Why it matters:** Golden worlds establish correctness but not real-world relevance.

**Experiment:** Build a versioned Paradise–Magalia experiment, conduct partial historical replay, freeze the scenario envelope and budgets, run FIRE-R005 through FIRE-R009, and solicit independent technical and practitioner critique.

**Strongest baselines:** Published Camp Fire traffic and agent-based studies; simultaneous and staged plans; strongest scenario-selection baseline.

**Success criterion:** The pipeline reproduces known qualitative mechanisms, finds additional plausible failures, and produces at least one held-out-robust intervention or high-value evidence recommendation.

**Kill or downgrade condition:** Public data cannot support even bounded safety claims, or results depend mainly on unvalidated local road and behavior assumptions. Publish the data-access failure and reassess geography.

**Dependencies:** FIRE-R001 through FIRE-R009.

**Expected open artifact:** Complete experiment manifest, benchmark results, certificates, intervention cards, and validation report.

**Decision or actor affected:** Project go/no-go; potential Butte County and California reviewers.

## P1 — Establish transfer and decision value

### FIRE-R101 — California-addressable world construction

**Question:** Can a submitted California location be converted into a transparent full-pipeline experiment without silent assumptions?

**Hypothesis:** Public statewide datasets can automate most physical-world construction while emitting a useful missing-evidence ledger.

**Experiment:** Test the constructor on mountain, canyon, suburban WUI, coastal hillside, tourist, and multi-community corridor archetypes.

**Success criterion:** Every source, transformation, license, assumption, and missing local input appears in a deterministic manifest.

**Kill condition:** Local manual work dominates construction or automated defaults control outcomes. Narrow statewide-addressable claims.

**Artifact:** California ingestion package and coverage-state registry.

### FIRE-R102 — Behavioral uncertainty and plan reversal

**Question:** Which warning, departure, destination, and compliance assumptions change the preferred intervention?

**Hypothesis:** A small subset of behavioral uncertainties controls most plan reversals.

**Experiment:** Global sensitivity analysis using published survey ranges and correlated household archetypes.

**Success criterion:** Identify stable simplifications and decision-critical unknowns separately.

**Kill condition:** Nearly every plausible behavior model changes the intervention. Return insufficient evidence and prioritize local behavioral studies.

**Artifact:** Behavior sensitivity atlas and value-of-information recommendations.

### FIRE-R103 — Cross-model disagreement

**Question:** Do important failures and interventions survive alternate fire, traffic, and behavior models?

**Hypothesis:** Causal failure families transfer more reliably than precise exposure counts or clearance times.

**Experiment:** Re-run high-value certificates through at least one alternate model per controlling layer.

**Success criterion:** The causal mechanism persists within predeclared tolerances.

**Kill condition:** High-value rankings systematically reverse. Downgrade them and study model selection as the controlling problem.

**Artifact:** Cross-model verification matrix.

### FIRE-R104 — Vehicle-less and supported evacuation

**Question:** Which combinations of transit, paratransit, pickup points, and departure timing protect populations without vehicles or independent mobility?

**Hypothesis:** Explicit supported-evacuation capacity changes intervention rankings that vehicle-only simulations would produce.

**Experiment:** Add vehicle-less households, mobility needs, loading time, fleet limits, and assistance coordination to selected cases.

**Success criterion:** Produce interventions that improve worst-group safety under held-out attacks.

**Kill condition:** Required local data are inaccessible and assumed ranges dominate results. Rank the missing evidence instead.

**Artifact:** Open supported-evacuation benchmark.

### FIRE-R105 — Institutional demand waves

**Question:** When do schools, hospitals, care facilities, and major employers create or suffer catastrophic congestion?

**Hypothesis:** Institution-specific timing can create failure families invisible in residential demand models.

**Experiment:** Vary dismissal, pickup, loading, staffing, and route interaction in communities with relevant facilities.

**Success criterion:** Identify actionable procedural changes or establish that road capacity remains binding.

**Artifact:** Institutional scenario and intervention library.

### FIRE-R106 — Shared regional corridors

**Question:** How often do community-level plans fail after neighboring demand enters the same downstream network?

**Hypothesis:** Independent community analysis systematically overestimates safety for shared-corridor systems.

**Experiment:** Couple two or more community systems with independently timed orders and regional background traffic.

**Success criterion:** Quantify when regional coordination changes the preferred plan or infrastructure intervention.

**Artifact:** Multi-community corridor benchmark.

### FIRE-R107 — Value-of-information ranking

**Question:** Can Firescape identify the measurement most likely to change an intervention decision?

**Hypothesis:** Expected value of information can distinguish decision-critical traffic counts, drills, surveys, and local plan facts from generally interesting data.

**Experiment:** Compare intervention rankings before and after simulated resolution of uncertain inputs, then validate prospectively where feasible.

**Success criterion:** Recommended evidence collection changes confidence or action more often than generic data collection.

**Kill condition:** Results are too model-dependent to prioritize measurements reliably.

**Artifact:** Evidence-priority cards and evaluation report.

### FIRE-R108 — Surrogate-assisted simulation allocation

**Question:** Can learned models reduce expensive simulator calls without certifying false failures?

**Hypothesis:** An uncertainty-aware graph or temporal surrogate can improve failure discovery per full simulation while every public finding remains fully verified.

**Experiment:** Compare tree, Gaussian-process, graph, and temporal surrogates as acquisition functions on held-out communities.

**Success criterion:** Better discovery efficiency, calibrated uncertainty, and no increase in published false certificates.

**Kill condition:** Gains disappear after training cost or fail under geography shift. Retain nonlearned search.

**Artifact:** Surrogate benchmark and model cards.

### FIRE-R109 — Transfer across community archetypes

**Question:** Which failure families and interventions transfer across geography?

**Hypothesis:** Road topology, fire-approach structure, population distribution, and institutional dependence define useful transfer archetypes.

**Experiment:** Hold out complete communities and test whether archetype-informed search or interventions improve results.

**Success criterion:** Transfer beats geography-agnostic baselines without suppressing local failure discovery.

**Kill condition:** Local differences dominate. Keep the registry as case-specific evidence rather than a transfer engine.

**Artifact:** Community-archetype and held-out transfer benchmark.

### FIRE-R110 — Planner comprehension and actionability

**Question:** Can intended users understand and use failure certificates and intervention cards?

**Hypothesis:** Minimized causal explanations outperform raw simulation dashboards for identifying a next planning action.

**Experiment:** Structured review with emergency managers, transportation planners, and facility operators comparing raw scenarios, standard dashboards, and Firescape cards.

**Success criterion:** Reviewers accurately identify the causal bottleneck, assumptions, residual risk, and next action.

**Kill condition:** Cards are misunderstood or encourage overconfidence. Redesign outputs before public release.

**Artifact:** Comprehension protocol and anonymized findings.

## P2 — Grow an open observatory

### FIRE-R201 — Distributed experiment registry

Define immutable experiment identifiers, provenance, reproduction environments, review states, supersession, and artifact storage for contributions from multiple organizations.

### FIRE-R202 — Benchmark governance

Create hidden test cases, independent adversaries, anti-overfitting rules, result review, and rules for adding newly discovered failures.

### FIRE-R203 — Responsible vulnerability disclosure

Determine what community details can be public, coarsened, embargoed, or shared only with authorized agencies. Test the policy against realistic choke-point and communication findings.

### FIRE-R204 — Distributed and donated compute

Evaluate whether content-addressed jobs and deterministic containers can expand California coverage without compromising reproducibility or sensitive inputs.

### FIRE-R205 — Prospective tabletop and drill validation

Translate verified failure families into exercise injects and compare modeled causal mechanisms with observed coordination, timing, and traffic behavior.

### FIRE-R206 — Global jurisdiction adapters

Test whether the core schemas, adversary, oracles, and certificates transfer outside California once a local data and authority adapter is supplied.

### FIRE-R207 — Other rapid-onset hazards

Only after wildfire validation, investigate whether the falsification and intervention framework transfers to tsunami, flood, volcanic, or industrial evacuation without erasing hazard-specific mechanisms.

## Deferred or rejected directions

### Live turn-by-turn routing

**Deferred until:** offline recommendations have prospective evidence, reliable live data exist, governance is defined, and human-factors risks are addressed.

### Custom wildfire-physics engine

**Rejected for v0 because:** it duplicates mature work and does not test the core adversarial hypothesis.

### Custom microscopic traffic engine

**Rejected for v0 because:** SUMO and other established simulators provide adapters sufficient for the initial research question.

### Named-household digital twins

**Rejected because:** they create privacy risk and false precision without being necessary for the core hypothesis.

### LLM-driven evacuee agents

**Deferred until:** explicit probabilistic behavior models have been exhausted and an LLM approach demonstrates external behavioral validity.

### Exact fatality prediction

**Rejected because:** available ground truth and causal modeling do not justify point estimates, and such outputs could mislead decisions.

### Precomputed full-fidelity simulation of every California location

**Rejected for initial scope because:** statewide local calibration and exhaustive computation are not available. Firescape is statewide-addressable and full-pipeline-on-demand instead.

### Direct ranking of California towns

**Deferred until:** scenario domains, calibration, evidence quality, and uncertainty are comparable. Intervention and evidence rankings come first.

### General all-hazard platform

**Deferred until:** the wildfire-specific core hypothesis is supported and the hazard-specific mechanisms are understood.

## Near-term execution order

The initial sequence is deliberately strict:

1. FIRE-R001 — exact competitors and residual claim.
2. FIRE-R002 — safety oracle.
3. FIRE-R003 — plausibility envelope.
4. FIRE-R004 — golden failure worlds.
5. FIRE-R005 — strong baselines.
6. FIRE-R006 — adversarial superiority test.
7. FIRE-R007 — failure certificates.
8. FIRE-R008 — intervention attack–repair–retest.
9. FIRE-R009 — evidence-gated ranking.
10. FIRE-R010 — Paradise–Magalia end-to-end proof.

Do not start P1 statewide scaling simply because the software pipeline exists. P1 begins only after FIRE-R006 through FIRE-R009 produce a credible positive result or a clearly revised hypothesis.

## Project-level go/no-go gate

Firescape earns continued investment only if the first end-to-end research cycle demonstrates that:

1. adversarial search finds more severe and causally diverse failures per full simulation than the strongest equal-budget baseline;
2. those failures are plausible, reproducible, and minimizable;
3. their causal explanations are understandable to an external reviewer;
4. at least one resulting intervention survives held-out attacks and does not worsen the worst-served population;
5. the output connects to an identifiable planning, exercise, infrastructure, or evidence decision.

If these conditions fail, publish the negative result and stop, narrow, or redirect the project rather than building a larger platform around an unsupported premise.
