# Firescape implementation and algorithmic research backlog

**Program state:** Conditional GO
**Gate date:** 2026-08-08
**Current phase:** Build the smallest complete adversarial research loop
**Decision record:** [First end-to-end research loop](research/first-loop/GATE_REPORT.md)
**Architecture review:** [Approved with conditions](research/first-loop/ARCHITECTURE_REVIEW.md)

This is now an execution backlog, not an idea-validation list. The first research loop found that wildfire-evacuation simulation is active and partly commercialized, while the narrower open workflow for adversarial failure discovery, full-simulator verification, counterexample minimization, and held-out intervention attack remains a credible contribution.

The project is authorized to build and test that workflow. It is not authorized to make operational recommendations, expand statewide, or build a polished product until the scientific gates in this backlog pass.

## Program thesis

At an equal budget of expensive simulations, a plausibility-constrained quality-diversity adversary should discover more severe, reproducible, and causally distinct evacuation-plan failures than historical/analyst scenarios, random sampling, stratified extremes, Sobol sampling, and cross-entropy search. Interventions selected from those failures should then reduce held-out tail risk without worsening the worst-served group.

The project succeeds only if it completes this chain:

> plausible inputs → adversarial search → full simulation → verified and minimized failure → implementable intervention → independent held-out attack → robust harm reduction → identifiable planning decision

## Non-negotiable rules

1. **Benchmark before platform.** No statewide infrastructure, live routing, or polished dashboard before the first algorithm and intervention gates pass.
2. **Strongest baseline wins the comparison.** The candidate is compared with CEM and Sobol, not merely random search.
3. **Full simulators certify.** Surrogates may acquire candidates; they cannot certify failures or repairs.
4. **Plausibility is executable.** Every material variable carries units, source, transformation, range, and compatibility constraints.
5. **Uncertainty is an input, not a footnote.** Calibration yields an ensemble of acceptable worlds, not a single false-precision world.
6. **Safety is disaggregated.** Average clearance cannot hide queue overtake, loss of egress, emergency-access obstruction, or subgroup harm.
7. **Repairs face a new attacker.** The method that finds a repair cannot be the only method used to validate it.
8. **All budgets are equal and auditable.** Count invalid proposals, full-simulator calls, retries, wall time, and preprocessing.
9. **Negative results ship.** Saturation by simple baselines, model reversals, or data insufficiency are publishable outcomes.
10. **No operational claims.** Firescape is research and planning evidence until external validation and governance explicitly change that status.

## Status labels

| Status | Meaning |
|---|---|
| **Ready** | Contract and acceptance test are frozen; implementation can begin |
| **Blocked** | A named prerequisite prevents meaningful work |
| **In progress** | Work has begun; scientific thresholds may no longer change |
| **Implemented** | Code and unit/integration tests meet the item contract |
| **Supported** | Preregistered empirical test passed |
| **Rejected** | Preregistered empirical test failed |
| **Deferred** | Explicitly outside the current gate |

## Locked v0 architecture

```text
firescape/
├── pyproject.toml
├── docker-compose.yml
├── configs/
│   ├── golden/
│   └── paradise/
├── data/
│   ├── manifests/
│   ├── raw/                 # ignored; fetched from manifests
│   ├── interim/             # ignored; reproducible transforms
│   └── fixtures/            # small redistributable test data
├── src/firescape/
│   ├── schemas/             # source, world, scenario, plan, run, certificate
│   ├── provenance/          # hashes, licenses, transforms, evidence tiers
│   ├── worlds/              # golden and California world builders
│   ├── hazard/              # ELMFIRE adapter and hazard clock
│   ├── traffic/             # SUMO/libsumo adapter and golden engine
│   ├── behavior/            # explicit stochastic archetypes
│   ├── coupling/            # edge state and exposure exchange
│   ├── oracles/             # validity, safety, equity, operability
│   ├── search/              # baselines, CEM, QD, later surrogates
│   ├── certificates/        # replay, minimization, causal signatures
│   ├── interventions/       # typed plan changes and compiler
│   ├── evaluation/          # metrics, statistics, held-out attacks
│   ├── registry/            # failures, experiments, result cards
│   └── cli.py
├── tests/
│   ├── unit/
│   ├── contract/
│   ├── golden/
│   └── integration/
├── experiments/
│   ├── preregistrations/
│   └── manifests/
└── research/
    ├── first-loop/
    ├── evidence/
    └── reports/
```

The file tree is a target contract, not permission to scaffold everything at once. Each milestone creates only the modules required for its acceptance test.

## Core data contracts

These objects must be versioned before simulator integration.

### `SourceArtifact`

- stable source ID and retrieval URL;
- publisher, retrieved-at time, geographic/time coverage;
- content hash, license, redistribution rule;
- raw and normalized coordinate reference systems;
- exact transformation graph;
- evidence tier and known limitations.

### `World`

- versioned road graph and edge attributes;
- origins, safe destinations, refuge, institutions, zones;
- population/demand ensemble;
- traffic calibration ensemble;
- hazard-realization references;
- documented excluded mechanisms;
- validation observations and acceptable intervals.

### `Scenario`

- reference to immutable world and plan;
- epistemic parameter selection;
- aleatory seed and draws;
- warning, behavior, traffic, hazard, and failure events;
- joint-plausibility constraint results;
- proposal method and complete lineage.

### `Intervention`

- actor and operational decision;
- typed changes to warning, staging, routing, traffic control, refuge, assistance, or infrastructure;
- activation conditions, resources, delay, cost evidence, and legal/physical constraints;
- groups and geographic areas affected.

### `RunArtifact`

- immutable inputs and container/software digests;
- random seeds and simulator call accounting;
- event trace, person/vehicle conservation, exposure trace;
- safety/equity/operability metrics;
- validity decisions and error taxonomy.

### `FailureCertificate`

- stable failure ID and causal family;
- minimized scenario delta from a reference world;
- reproduction rate and confidence interval;
- necessary conditions and severity amplifiers;
- affected zones/groups, choke points, and time interval;
- cross-seed/model sensitivity;
- candidate decisions and disclosure status.

## Milestone 0 — Reproducible research kernel

**Exit gate:** A clean machine can validate schemas and reproduce one deterministic run from a manifest.

### FIRE-I001 — Python project and dependency lock

**Status:** Ready
**Build:** Python 3.11 package, lint/type/test commands, deterministic numeric settings, dependency lock, container definitions for external engines.
**Acceptance:** One documented command installs the orchestration layer; one command runs unit tests; CI repeats both on Linux. Version output is captured in every run.
**Do not add:** web frontend, cloud platform, user accounts, distributed scheduler.

### FIRE-I002 — Source and experiment provenance

**Status:** Ready
**Build:** `SourceArtifact`, transformation records, SHA-256 hashing, license/redistribution flags, experiment manifests, immutable run IDs.
**Acceptance:** Mutating any input, config, code version, or container digest changes the experiment/run identity. A run with an unregistered artifact is rejected.

### FIRE-I003 — Scenario, plan, run, and certificate schemas

**Status:** Ready
**Build:** Pydantic schemas with units, validation, JSON Schema export, upgrade/version policy, canonical serialization.
**Acceptance:** Round-trip fixtures; incompatible units and unknown fields fail loudly; schemas cover every variable used by the golden worlds.

### FIRE-I004 — Deterministic runner and artifact store

**Status:** Ready
**Build:** Local CLI, seed tree, subprocess/container adapter, structured logs, DuckDB catalog, Parquet/JSONL result storage, resumable idempotent runs.
**Acceptance:** Repeating a deterministic manifest produces byte-identical canonical metrics; interrupted batches resume without duplicate simulator calls.

### FIRE-I005 — License and contribution boundary

**Status:** Ready
**Build:** Select repository license, third-party notices, data-license registry, contribution instructions, safety disclaimer.
**Acceptance:** No public code/data release has an unknown reuse status; OSM-derived artifacts retain required attribution and share-alike handling.

## Milestone 1 — Golden failure laboratory

**Exit gate:** Exhaustive enumeration proves that the runner, oracle, search accounting, replay, and minimizer work on known systems.

### FIRE-A001 — Deterministic golden traffic engine

**Status:** Ready
**Build:** Small time-stepped network flow/queue engine with origins, destinations/refuge, edge capacity, storage, travel time, closures, exposure, and emergency priority.
**Purpose:** Unit-test Firescape logic without blaming SUMO. It is not a scientific traffic model.
**Acceptance:** Vehicle/person conservation, FIFO behavior where declared, analytic single-edge throughput, merge capacity, closure, and spillback tests.

### FIRE-A002 — Six exhaustively enumerable worlds

**Status:** Ready
**Build:**

1. queue overtaken by hazard;
2. merge gridlock caused by simultaneous release;
3. loss of every safe path after correlated closures;
4. compressed warning plus pre-departure delay;
5. emergency-access conflict;
6. average improvement with worst-group regression.

**Acceptance:** Each world declares the complete scenario space, exact failure boundary, expected minimal cause, and exhaustive reference result.

### FIRE-A003 — Validity and conservation oracles

**Status:** Ready
**Build:** Input plausibility, causal compatibility, graph reachability, conservation, temporal consistency, finite-number, and simulator-health checks.
**Acceptance:** All seeded invalid fixtures are rejected with stable reason codes; no known valid extreme fixture is excluded.

### FIRE-A004 — Safety, equity, and operability oracle

**Status:** Ready
**Build:** Lexicographic metric vector:

1. unsafe person-minutes;
2. persons without a viable path;
3. queue/vehicle overtake;
4. emergency-access blocked minutes;
5. zone clearance lateness;
6. worst-zone/worst-group outcomes;
7. total clearance and delay.

**Acceptance:** Every golden failure triggers its intended component; the worst-group fixture cannot be reported as an improvement; units and aggregation are documented.

### FIRE-A005 — Replay and hierarchical delta minimization

**Status:** Ready
**Build:** Cross-seed replay; reproduce threshold; group→variable→value delta debugging; necessary-condition and severity-amplifier labels.
**Acceptance:** Returns the known one-minimal cause for every golden world and is invariant to irrelevant parameter ordering.

## Milestone 2 — Paradise–Magalia evidence world

**Exit gate:** A versioned public evidence ensemble can reproduce selected qualitative Camp Fire mechanisms without pretending to reconstruct every person.

### FIRE-D001 — Camp Fire evidence ledger

**Status:** Ready
**Inputs:** NIST NETTRA report and supplements, official incident reports, public notification/order records, traffic observations, refuge/convoy/closure records.
**Build:** Machine-readable observation objects with interval, location, source excerpt locator, confidence, and whether they are calibration, validation, or contextual evidence.
**Acceptance:** Include at minimum fire/road interaction, notification timing, closure timing, extreme travel delay, simultaneous artery loss, abandonment, temporary refuge, traffic redirection, contraflow/convoy evidence. No observation is used for both calibration and validation without disclosure.

### FIRE-D002 — Public data manifest and fetchers

**Status:** Ready
**Inputs:** OSM, Census/TIGER, ACS, LODES, LANDFIRE, USGS 3DEP, HRRR, CAL FIRE perimeters, Caltrans counts/PeMS where applicable.
**Build:** Pin query boundaries, versions/dates, hashes, licenses, download commands, transformations, and cached-fixture policy.
**Acceptance:** A reviewer can rebuild the normalized source inventory; inaccessible or changed upstream data produces a legible failure, not silent substitution.

### FIRE-D003 — OSM-to-SUMO Paradise network

**Status:** Ready
**Build:** Import, clean, and document lanes, turns, junctions, restrictions, speeds, storage, signal/control, candidate refuges and destinations; retain source-to-edge mapping.
**Validation:** Compare arterial continuity and geometry with public road evidence; flag high-leverage unknown local attributes.
**Acceptance:** Network connectivity tests pass; every origin has a declared destination/refuge policy; suspect capacity attributes are ensemble variables rather than invented facts.

### FIRE-D004 — Synthetic population and demand ensemble

**Status:** Ready
**Build:** Aggregate origins and synthetic agents using Census/ACS/LODES, household vehicle availability, day/night location, occupancy, workers/visitors, and institutions. No named individual or device trace.
**Acceptance:** Aggregate margins match source tolerances; uncertainty is represented through multiple populations; generated agents carry no reidentifying fields.

### FIRE-D005 — Traffic calibration envelope

**Status:** Ready
**Build:** Priors/ranges for free-flow speed, capacity, saturation flow, background traffic, turn choice, incident reduction, and smoke reduction using public counts and published studies.
**Method:** Approximate Bayesian computation or multiobjective calibration over qualitative/interval targets; retain all acceptable parameter sets.
**Acceptance:** Publish posterior/accepted ranges, non-identifiable parameters, and which historical mechanisms each accepted world can or cannot reproduce.

### FIRE-D006 — Behavioral plausibility envelope

**Status:** Ready
**Build:** Explicit distributions for warning receipt, awareness/preparation/departure delay, early evacuation, household trip chaining, vehicle count/occupancy, route familiarity, compliance/rerouting, mobility support, and institutional loading.
**Constraints:** Correlations and mutually incompatible states are executable. LLM-generated behavior is forbidden as evidence.
**Acceptance:** Every marginal and dependency is sourced or labeled assumption; global sensitivity identifies whether unsupported behavior assumptions dominate outcomes.

### FIRE-D007 — Known-mechanism replay gate

**Status:** Blocked on FIRE-D003–D006 and hazard replay
**Test:** Hold out selected NIST observations and ask whether an acceptable ensemble reproduces qualitative patterns rather than an exact trajectory.
**Pass:** At least one accepted world reproduces each selected mechanism and no single parameter set is presented as truth.
**Fail/pivot:** If public evidence cannot constrain the world, restrict the scientific claim to golden/synthetic benchmarks or rank evidence needs instead of interventions.

## Milestone 3 — Hazard realization and coupling

**Exit gate:** Reproducible time-indexed hazard fields drive traffic-edge states and exposure, with no temporal leakage or hidden manual edits.

### FIRE-H001 — Canonical hazard-field contract

**Status:** Ready
**Build:** Raster/mesh contract for arrival time, intensity/exposure class, smoke/visibility proxy, validity mask, time zone, resolution, uncertainty label, and provenance.
**Acceptance:** Synthetic advancing-front and spot-fire fixtures interpolate correctly; out-of-domain roads are rejected or explicitly assigned no-data behavior.

### FIRE-H002 — ELMFIRE container and adapter

**Status:** Ready
**Build:** Pinned ELMFIRE image, input compiler, resource/time limits, logs, output normalizer, stable run ID, minimal validation cases.
**Acceptance:** Reproduce one documented ELMFIRE validation case within declared tolerance; run the same input twice reproducibly; store complete provenance.

### FIRE-H003 — Paradise fire-realization library

**Status:** Blocked on data manifest and ELMFIRE adapter
**Build:** Bounded ensemble over ignition, weather, fuel moisture, spotting parameters, and model error; condition/reject against historical progression intervals for reconstruction members.
**Acceptance:** Every realization is labelled historical-consistent, plausible counterfactual, or stress-only; no stress-only member is described as probable.

### FIRE-H004 — Hazard-clock adapter

**Status:** Ready after FIRE-H001
**Build:** Map hazard fields to time-indexed SUMO edge events: speed/capacity reduction, closure, reopening, exposure accumulation, and visibility.
**Acceptance:** Golden raster/network tests prove event timing, interpolation, precedence, and unit conversion. No future hazard state leaks into agent routing unless the plan explicitly supplies a forecast.

### FIRE-H005 — Coupling-sufficiency test

**Status:** Blocked on first end-to-end runs
**Question:** Is one-way replay adequate for the intervention class?
**Test:** Vary edge-event mappings and compare at least one alternate fire/exposure interpretation.
**Upgrade triggers:** vehicle/structure fire feedback, suppression interaction, smoke models, or mapping choices reverse failure or intervention ranks.

## Milestone 4 — Full traffic, warning, and behavior simulation

**Exit gate:** SUMO/libsumo executes reproducible scenarios, passes contracts against golden cases, and produces complete agent/exposure accounting.

### FIRE-T001 — SUMO/libsumo container and adapter

**Status:** Ready
**Build:** Pinned SUMO image; programmatic step/run API; network, route, person, vehicle, closure, reroute, and metric exchange; structured error taxonomy.
**Acceptance:** Official small-network smoke test plus Firescape merge/closure contract tests; complete version/seeds captured.

### FIRE-T002 — Traffic demand and destination compiler

**Status:** Blocked on world/population schemas
**Build:** Convert synthetic population and scenario into departure, vehicle, route/destination, background, inbound responder, bus/paratransit, and pedestrian demand.
**Acceptance:** Conservation from source population to safe/refuge/unfinished states; deterministic compilation for a fixed seed.

### FIRE-T003 — Warning and behavior state machine

**Status:** Ready after behavioral envelope
**Build:** Warning unavailable→received→interpreted→preparing→departing→rerouting/refuge states with explicit dwell distributions and plan signals.
**Acceptance:** State transition/property tests; no impossible double departure; receipt, preparation, and mobility support remain separable.

### FIRE-T004 — Coupled event scheduler

**Status:** Blocked on hazard and traffic adapters
**Build:** Deterministic ordering for warning, departure, routing, incident, hazard, traffic control, refuge, and measurement events.
**Acceptance:** Tie-breaking contract, time-zone handling, no future-information leakage, consistent replay after resume.

### FIRE-T005 — Full-run trace and oracle integration

**Status:** Blocked on FIRE-T001–T004
**Build:** Stream edge/person/vehicle/hazard state into oracle accumulators; avoid retaining unnecessary fine-grained personal traces.
**Acceptance:** Reconcile starting population with all terminal states; reproduce golden-network results within an explicitly explained simulator tolerance.

### FIRE-T006 — Runtime and fidelity profile

**Status:** Blocked on first full world
**Measure:** Wall time, memory, event volume, stochastic variance, scenario compile time, and failure rate across world sizes.
**Decision:** Freeze the full-simulator-call budget and decide whether parallel local workers, traffic aggregation, or a surrogate is justified.

## Milestone 5 — Equal-budget baseline suite

**Exit gate:** All baselines share one proposal API, plausibility filter, call budget, seed protocol, and metric report.

### FIRE-S001 — Search-space registry

**Status:** Ready
**Build:** Typed dimensions, transforms, conditional variables, correlations, immutable bounds, evidence tier, mutation distance, and descriptor extraction.
**Acceptance:** Sample/serialize/deserialize property tests; a frozen registry hash appears in every comparison.

### FIRE-S002 — Historical and analyst scenario baseline

**Status:** Blocked on evidence ledger
**Build:** Reconstructed Camp Fire family plus documented edge/extreme cases.
**Acceptance:** Scenarios are traceable, not tuned after candidate results, and count against the same evaluation budget when simulated.

### FIRE-S003 — Random, stratified, Latin-hypercube, and Sobol baselines

**Status:** Ready after registry
**Build:** Reproducible low-discrepancy/stratified generators that respect conditional variables and joint constraints.
**Acceptance:** Golden-space coverage and distribution tests; rejected proposals are counted.

### FIRE-S004 — Cross-entropy method baseline

**Status:** Ready after registry
**Build:** Mixed continuous/categorical CEM, elite update, smoothing, constraint handling, restarts, and multi-objective acquisition scalar used only for search.
**Acceptance:** Finds every narrow golden failure within a frozen tolerance and emits complete proposal/update lineage.

### FIRE-S005 — Equal-budget experiment harness

**Status:** Ready after baselines
**Build:** Method×budget×seed matrix, paired seed sets, resumable execution, preregistration hash, bootstrap estimates, anytime curves.
**Metrics:**

- verified severe failures per 100 full simulations;
- unique causal failure families;
- maximum and 95th-percentile severity;
- time/calls to first verified failure;
- area under verified-family coverage curve;
- invalid proposal rate;
- wall time and full-simulator calls.

**Acceptance:** Synthetic no-difference test has calibrated false-positive behavior; a deliberately superior fixture is detected.

## Milestone 6 — Quality-diversity adversary

**Exit gate:** Candidate algorithm faces the frozen equal-budget gate. This is the first major project go/no-go.

### FIRE-Q001 — Failure descriptor study

**Status:** Ready after golden certificates
**Candidate descriptors:** first failed zone, dominant cut/choke point, warning-capacity interaction, demand/closure/route contribution, worst group, refuge dependence, emergency-access class.
**Test:** Descriptors must split known causal mechanisms, remain stable across stochastic replay, and not use unavailable post hoc labels during proposal.
**Reject:** Raw high-dimensional scenario distance or coordinates that create visually diverse but causally duplicate bins.

### FIRE-Q002 — MAP-Elites reference implementation

**Status:** Blocked on registry/descriptors
**Build:** Mixed-variable mutation, constraint-aware repair, bounded archive, deterministic selection, severity/validity quality score, complete lineage.
**Acceptance:** Recovers all reachable golden-world failure families and does not retain invalid candidates as elites.

### FIRE-Q003 — CEM or CMA-ME emitters

**Status:** Blocked on QD reference
**Build:** Emitters for random exploration, local improvement, and tail-region CEM; adaptive allocation is allowed only with auditable rules.
**Acceptance:** Ablation reports the value of each emitter; standalone CEM remains an untouched baseline.

### FIRE-Q004 — Uncertainty-aware archive

**Status:** Blocked on replay estimates
**Build:** Store confidence bounds, reproduction probability, invalidity, model disagreement, and full-simulator count; promotion requires evidence, not one lucky run.
**Acceptance:** Noisy golden tests do not let single-seed anomalies dominate the archive.

### FIRE-Q005 — Preregistered superiority experiment

**Status:** Blocked on complete Paradise benchmark
**Freeze before run:** space, worlds, fire library, call budget, seeds, methods, descriptors, severity threshold, family-clustering protocol, invalidity threshold, and analysis code hash.
**Primary pass:** Across 10 seeds, the candidate achieves either ≥25% improvement in area under the verified severe-family coverage curve or ≥2 additional verified causal families at the same budget, on ≥8/10 seeds, with ≤5% invalid proposals.
**Fail:** Stop algorithm expansion if the strongest baseline saturates discovery, compute accounting erases gains, or QD mainly finds simulator artifacts.

### FIRE-Q006 — Surrogate acquisition study

**Status:** Deferred until a versioned corpus exists
**Entry condition:** At least 10,000 diverse full runs or learning-curve evidence that less is sufficient.
**Candidates:** Gaussian process, calibrated gradient-boosted trees, graph neural network for traffic state, differentiable fire surrogate as an alternate model.
**Test:** Full-simulator failure-family coverage per wall-clock hour and per full call; calibration/out-of-distribution detection required.
**Rule:** No learned model certifies a result.

### FIRE-Q007 — Sequential adaptive stress testing

**Status:** Deferred
**Entry condition:** Evidence that within-event sequential adversarial decisions, rather than initial scenario selection, are the limiting search problem.
**Candidates:** MCTS/AST over warning, failures, or time-evolving perturbations.
**Reject:** DRL-first implementation without a demonstrable sequential advantage and strong nonlearned baseline.

## Milestone 7 — Failure certification and causal registry

**Exit gate:** A planner-facing certificate is reproducible, minimal, uncertainty-aware, and independent of optimizer internals.

### FIRE-C001 — Replay policy and statistical certificate

**Status:** Ready after full simulation
**Build:** Predeclared seed sets, reproduction probability, Wilson/bootstrap intervals, severity confidence, failed-run handling.
**Acceptance:** Threshold behavior is tested; optimizer seeds are separated from certificate seeds.

### FIRE-C002 — Full-simulator certificate minimizer

**Status:** Ready after replay
**Build:** Hierarchical group/variable/value removal with caching, monotonicity checks, and nonmonotone fallback.
**Acceptance:** Matches golden minimal causes; reports alternative minimal certificates where causes are non-unique.

### FIRE-C003 — Causal signature and family clustering

**Status:** Blocked on certificate corpus
**Build:** Rule-based causal signature first; cluster only over certified mechanism features; human-readable medoids and merge/split audit.
**Acceptance:** Golden families are recovered; stability is measured across bootstrap samples and reasonable feature definitions.

### FIRE-C004 — Cross-model and artifact check

**Status:** Blocked on alternate model/mapping
**Build:** Replay certificate under alternate capacity, behavior, hazard mapping, and where feasible alternate fire/traffic abstraction.
**Labels:** robust, model-sensitive, unsupported, or artifact-suspect.
**Acceptance:** Model-sensitive results cannot appear in top recommendations without an evidence action.

### FIRE-C005 — Failure registry and disclosure policy

**Status:** Ready after first certificates
**Build:** Versioned registry, supersession, reproduction command, public/coarsened/coordinated-disclosure levels.
**Acceptance:** Every public failure links inputs→run→oracle→minimization→sensitivity; sensitive choke-point detail is reviewed before publication.

## Milestone 8 — Intervention attack–repair–retest

**Exit gate:** At least one implementable intervention survives an independent held-out attack and worst-group constraints.

### FIRE-V001 — Typed intervention compiler

**Status:** Ready after plan schema
**v0 catalog:** staged warning/order, warning timing, route/destination allocation, intersection control, contraflow activation, emergency-only capacity, temporary refuge, bus/paratransit allocation, one road-capacity change.
**Acceptance:** Each intervention names actor, activation delay, resources, constraints, affected groups, and exact simulator mutations. Invalid combinations are rejected.

### FIRE-V002 — Intervention selection baselines

**Status:** Blocked on failure families
**Build:** no change, analyst-authored repair, optimize mean clearance, optimize discovered scenarios only, robust tail/equity selection.
**Acceptance:** Comparison shows whether the adversarial evidence adds value beyond conventional objective optimization.

### FIRE-V003 — Held-out attacker protocol

**Status:** Ready after search suite
**Build:** Independent fire/behavior/traffic draws; attacker different from repair discovery method; no reuse of certificate seeds; immutable hidden manifest hash.
**Acceptance:** Leakage tests; only after analysis does the hidden manifest become public.

### FIRE-V004 — Tail-risk and equity evaluation

**Status:** Blocked on intervention runs
**Primary pass:** One feasible intervention reduces held-out CVaR of unsafe person-minutes ≥30%, worsens the worst-served group no more than 5%, and retains direction across at least two reasonable behavior/fire variants.
**Secondary:** Family elimination, persons without safe path, emergency access, clearance, cost/operability.
**Fail:** Do not claim harm reduction if gains exist only on attacked training scenarios or one model.

### FIRE-V005 — Decision and evidence cards

**Status:** Blocked on supported intervention
**Build:** Actor, action, failure family, modeled benefit interval, residual failures, cost/authority assumptions, evidence tier, most decision-sensitive unknown, and next validation action.
**Acceptance:** A practitioner can state what decision the card could change and what it cannot establish.

## Milestone 9 — Transfer, adoption, and release

**Exit gate:** The contribution survives a second geography/model and an external actor sees a legitimate use.

### FIRE-X001 — Second-geography selection

**Status:** Deferred until Q005
**Selection criteria:** different topology and fire history; sufficient public evidence; no method tuning before selection. Candidate families include Berkeley/Marin studies or a documented 2025 Southern California event.
**Acceptance:** Selection rationale and hidden validation targets are frozen before transfer work.

### FIRE-X002 — Cross-geography replication

**Status:** Deferred
**Pass:** Candidate search and certificate protocol retain a meaningful advantage without Paradise-specific descriptor or threshold redesign.
**Fail:** Reframe as a case-specific method or revise the scientific claim.

### FIRE-X003 — Practitioner evidence review

**Status:** Ready once a certificate/card exists
**Actors:** county/city emergency management, transportation/public works, fire/law enforcement, Cal OES/Caltrans researchers, WUI evacuation academics.
**Test:** Can the artifact change a plan, exercise, traffic-control study, refuge policy, data collection, or grant priority? What would make it inadmissible?
**Acceptance:** One named decision path and documented criticism; endorsement is not required.

### FIRE-X004 — Open benchmark v1

**Status:** Deferred until transfer gate
**Ship:** schemas, golden worlds, reproducible public cases, baseline library, QD method, manifests, metrics, certificates, negative results, data licenses, and compute/cost report.
**Acceptance:** Independent clean-machine reproduction of at least one full experiment.

### FIRE-X005 — Statewide-addressable feasibility study

**Status:** Deferred until all preceding gates pass
**Question:** Which California locations can be constructed at what evidence tier and marginal cost?
**Rule:** Do not publish cross-community safety rankings from incomparable calibration.

## Cross-cutting algorithmic research queue

These studies are scheduled by evidence, not fashion.

| ID | Question | Earliest entry | Decision |
|---|---|---|---|
| ALG-01 | Which causal descriptors yield stable, nonduplicate failure families? | Golden certificates | Locks QD archive axes |
| ALG-02 | Does CEM-QD beat standalone CEM at the same full-call budget? | Baseline suite | Core novelty gate |
| ALG-03 | Does uncertainty-aware elite promotion prevent lucky-run artifacts? | Noisy golden worlds | Locks certificate sampling policy |
| ALG-04 | Which hierarchical minimizer handles nonmonotone causes with least full-sim cost? | First failures | Locks certificate algorithm |
| ALG-05 | Can active learning reduce full calls while preserving calibrated tail discovery? | ≥10k runs or learning-curve proof | Allows surrogate acquisition |
| ALG-06 | Do graph surrogates transfer across unseen road topology? | Two geographies | Determines value of GNN research |
| ALG-07 | Does differentiable fire simulation help scenario acquisition without biasing certification? | Alternate-model stage | Determines PyTorchFire/ForeFire track |
| ALG-08 | Is robust intervention selection better modeled as distributionally robust optimization, CVaR search, or constrained QD? | Certificate corpus | Locks repair selector |
| ALG-09 | Can value-of-information analysis rank measurements when repairs are assumption-sensitive? | Model reversal/data dominance | Opens evidence-priority pivot |
| ALG-10 | Does sequential AST add failure families unavailable to initial-condition search? | Sequential limitation demonstrated | Opens MCTS/AST track |

## Data and validation research queue

| ID | Unknown | Initial treatment | Escalation evidence |
|---|---|---|---|
| DAT-01 | Local road/intersection capacity | Wide calibrated ensemble | Targeted counts or agency geometry/control data |
| DAT-02 | Incident departure and route behavior | Published distribution/archetypes | Survey, drill, connected-vehicle, or deidentified trace agreement |
| DAT-03 | Visitors and background demand | LODES/season/time ensemble | Tourism/mobile aggregate evidence with lawful access |
| DAT-04 | Warning receipt and interpretation | Channel/delay ensemble | Alert delivery logs and survey evidence |
| DAT-05 | Access/functional-needs movement | Explicit bounded archetypes | Co-designed agency/community evidence |
| DAT-06 | Institutions and assisted evacuation | Parametric loading/fleet models | Facility plans, drill timing, fleet availability |
| DAT-07 | Fire arrival at road scale | ELMFIRE ensemble and NIST intervals | Sensor/video/reconstruction or alternate-model agreement |
| DAT-08 | Smoke/visibility speed effects | Sensitivity range | Empirical traffic-under-smoke data |
| DAT-09 | Temporary refuge capacity/use | Historical evidence and scenario bounds | Site-level operational review |
| DAT-10 | Emergency inbound traffic | Parametric priority/demand | Agency AVL/after-action evidence |

## Experiment preregistration template

Every comparative result must freeze:

- research question and one primary endpoint;
- world, plan, source, and simulator digests;
- search space and plausibility constraints;
- calibration and held-out evidence split;
- algorithms, hyperparameter budget, compute/call budget;
- seed generation and number of replicates;
- failure threshold and family protocol;
- invalid-run/proposal handling;
- statistical analysis and uncertainty intervals;
- success, kill, and pivot thresholds;
- excluded mechanisms and external-validity boundary;
- exact code/config hash before results are inspected.

## Risk register and automatic penalties

| Risk | Current severity | Required control | Automatic consequence |
|---|---:|---|---|
| Behavioral ground truth is weak | Critical | Ensemble, sensitivity, evidence tiers, no LLM truth | Downgrade intervention confidence; pivot to evidence value if rank-dominant |
| Local-road capacity is weak | Critical | Capacity ensemble and targeted validation | No local operational recommendation |
| Fire/traffic sim-to-reality gap | High | Known-mechanism replay and cross-model checks | Model-sensitive label; no certification claim |
| Broad field is already crowded | High | Residual claim and exact-system updates | Contribute upstream if equivalent open loop is found |
| Paradise overfitting | High | Hidden second geography | No transfer or statewide claim |
| Search exploits simulator bugs | Critical | Validity oracle, replay, minimization, alternate model | Reject artifact-suspect family |
| Unclear adopter | High | Practitioner evidence review | No scaling or product spend |
| Compute becomes frontier-scale | Medium | Profile, precomputed hazard fields, equal call accounting | Simplify world or stop; no opaque cloud spend |
| Detailed vulnerabilities create misuse risk | Medium | Disclosure classification and coarsening | Withhold/coarsen sensitive artifact |
| Open data licensing blocks redistribution | Medium | Manifest/license registry | Release fetch/transform code, not prohibited data |

## Frozen go, pivot, and stop gates

### Gate G1 — Research kernel

Pass when golden worlds, oracles, replay, and minimization reproduce exhaustive truth. Failure blocks real geography.

### Gate G2 — Public Paradise world

Pass when an ensemble of plausible worlds reproduces selected held-out qualitative Camp Fire mechanisms. If public evidence cannot constrain the world, continue only as a synthetic algorithm benchmark or evidence-priority project.

### Gate G3 — Search superiority

Pass only under FIRE-Q005. If CEM/Sobol saturates the space or QD gains vanish under accounting, stop the adversarial-algorithm expansion and publish the result.

### Gate G4 — Actionable certificate

Pass when multiple independently replayable failures minimize into stable, legible causal certificates. If failures remain high-dimensional or model-specific, do not call them decision evidence.

### Gate G5 — Robust intervention

Pass only under FIRE-V004. If no repair survives an independent attacker and alternate assumptions, do not claim that the research reduces harm.

### Gate G6 — Transfer and actor

Pass when the protocol transfers to a second geography and an identifiable actor confirms a legitimate decision use. Only then evaluate statewide-addressable infrastructure or a product interface.

## First 60 days: dependency-ordered execution

### Days 1–10

- FIRE-I001–I004: project, schemas, provenance, runner;
- FIRE-A001–A004: golden engine, worlds, validity and safety oracles;
- begin FIRE-D001 and FIRE-D002 evidence manifests.

**Checkpoint:** exhaustive truth is machine-readable and the runner is deterministic.

### Days 11–20

- FIRE-A005 replay/minimization;
- FIRE-H001 hazard contract;
- FIRE-T001 SUMO adapter;
- FIRE-D003 network and FIRE-D004 population.

**Checkpoint:** a synthetic world executes through both traffic engines and returns the same failure classification.

### Days 21–30

- FIRE-D005/D006 calibration and behavior envelopes;
- FIRE-H002/H003 ELMFIRE adapter and small fire library;
- FIRE-H004 and FIRE-T002–T005 full coupling.

**Checkpoint:** first traceable Paradise run, including conservation and exposure metrics.

### Days 31–40

- FIRE-D007 known-mechanism replay;
- FIRE-T006 runtime profile and budget freeze;
- FIRE-S001–S004 baseline implementations.

**Checkpoint:** G2 decision and signed preregistration draft.

### Days 41–50

- FIRE-S005 experiment harness;
- FIRE-Q001–Q004 QD implementation and ablations;
- run golden benchmark, freeze Paradise preregistration.

**Checkpoint:** no method-specific integration path; every proposal flows through the same validity/full-sim/certificate boundary.

### Days 51–60

- FIRE-Q005 superiority run;
- FIRE-C001–C003 certification and family registry;
- FIRE-V001–V004 three interventions and independent held-out attack;
- publish G3–G5 decision, including negative results.

**Scope rule:** If Paradise data construction consumes the schedule, use a traceable published fire-arrival field for the first method gate and continue ELMFIRE reconstruction separately. Do not relax the equal-budget or full-SUMO requirements.

## Twelve-month sequence

1. Months 1–2: complete G1–G5 or publish why they failed.
2. Months 3–4: harden manifests, certificate format, cross-model checks, and value-of-information pivot.
3. Months 5–6: freeze and construct a genuinely different second geography.
4. Months 7–8: run transfer experiment and descriptor/search ablations.
5. Months 9–10: external research and practitioner review; integrate criticism without moving original thresholds.
6. Months 11–12: benchmark v1, replication package, scientific paper/report, and explicit scale/no-scale decision.

The 12-month proof target is two cases, one reusable protocol, one supported repair family, and one real decision path—not a statewide consumer application.

## Immediate next work item

Start **FIRE-I001 through FIRE-A004** as one vertical research-kernel slice:

1. freeze project/tool versions;
2. define schemas and canonical run IDs;
3. implement the deterministic queue engine;
4. create the six golden worlds;
5. implement validity and lexicographic safety oracles;
6. exhaustively enumerate and store truth fixtures.

Do not begin ELMFIRE integration, UI, deep learning, or statewide ingestion until this slice proves that Firescape can state exactly what a failure is and find known failures without ambiguity.
