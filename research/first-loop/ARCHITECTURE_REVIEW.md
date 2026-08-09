# Firescape v0 architecture review

## Verdict

**Approve with conditions.**

The design is appropriate for a design-before-build research instrument if implementation preserves a narrow dependency direction and treats every simulator as a replaceable adapter. Reopen the architecture if one-way hazard replay changes intervention rankings, if the golden and SUMO paths acquire different scientific meanings, or if runtime/artifact volume makes the preregistered comparison infeasible on one workstation.

## Evidence reviewed

### Inspected

- [Firescape system description](../../README.md)
- [First end-to-end research decision](GATE_REPORT.md)
- [Implementation and algorithmic research backlog](../../RESEARCH_BACKLOG.md)
- three independent schema-validated evidence records under `results/`
- the current documentation-only repository and proposed local runtime

### Missing or weak

- measured ELMFIRE/SUMO runtime on the target machine;
- a tested OSM-to-SUMO Paradise network;
- exact redistribution constraints for every dataset;
- a committed practitioner or planning decision;
- behavioral and local-road evidence adequate for operational claims;
- an alternate coupled model for cross-model validation.

This is approval to build the research kernel, not evidence that the stack will pass its scientific gates.

## Quality-attribute scenarios

| Attribute | Stimulus and environment | Required response | Measure/evidence |
|---|---|---|---|
| Reproducibility | A clean machine receives a manifest | Rebuild inputs and rerun without manual GIS edits | Same canonical IDs; deterministic golden output; documented stochastic tolerance |
| Modifiability | A simulator or behavior model is replaced | Search, oracle, certificate, and evaluation code stay unchanged | Adapter contracts pass; domain schemas contain no engine types |
| Scientific validity | Search proposes a severe but impossible case | Reject before certification and count it | Stable reason code and reported invalid rate |
| Performance | Thousands of local runs are requested | Reuse fire fields, cache immutable results, resume | Frozen budget fits the experiment; no duplicate run IDs |
| Consistency | A run is interrupted or repeated | Preserve lineage and never partially promote a certificate | Atomic artifact commit and idempotent catalog entry |
| Explainability | A high-dimensional failure is found | Return a minimal cause independent of optimizer internals | Cross-seed replay and hierarchical minimization pass |
| Safety | A certificate reveals sensitive dependencies | Classify before release | Public, coarsened, or restricted state is recorded |
| Cost | A surrogate/distributed layer is proposed | Demonstrate a measured bottleneck first | Runtime profile and learning curve justify it |

## Top risks

| Severity | Risk | Evidence | Recommendation |
|---|---|---|---|
| Critical | Results optimize uncertain behavior or local capacity | Public evidence lacks complete trajectories and road-level truth | Preserve acceptable-world ensembles; block operational ranking when assumptions dominate |
| Critical | Search exploits a SUMO/coupling bug | Adversarial methods seek discontinuities | Require invariants, full replay, minimization, alternate mappings, and artifact labels |
| High | Golden and SUMO paths define failure differently | Engines necessarily differ in fidelity | Share schemas and oracles; contract-test classifications, not numerical identity |
| High | One-way fire replay is inadequate | Feedback may matter for some interventions | Restrict v0 interventions and reopen coupling on rank reversal |
| High | Engine types contaminate research logic | This would make cross-model checks expensive | Enforce ports/adapters and forbidden-import tests |
| High | Microscopic traces overwhelm local storage | Thousands of full runs can be large | Stream oracle aggregates, retain sampled traces, profile before scale |
| High | Platform work precedes a research result | UI/statewide work does not answer the first hypothesis | Treat scientific gates as funding gates |
| Medium | Public certificates expose operational weaknesses | Choke points and alert failures may be sensitive | Classify at certificate creation, not publication |

## Tradeoffs

| Option | Upside | Downside | Assumption | Reversibility | Verification |
|---|---|---|---|---|---|
| Precomputed ELMFIRE fields + SUMO replay **(chosen)** | Many traffic/behavior runs per fire; solo-scale | No traffic-to-fire feedback; mapping may bias exposure | Fire is exogenous for v0 interventions | High | Mapping sensitivity and cross-model replay |
| Tight fire/traffic coupling | Rich interaction | Large integration/runtime burden before the core test | Feedback materially affects v0 decisions | Medium | Spike only after a coupling trigger |
| SUMO microscopic traffic **(chosen)** | Mature, open, lane/queue detail | Costly network prep and calibration | Detail improves relevant oracles | Medium | Golden contracts, incident mechanisms, runtime profile |
| Custom/mesoscopic geographic traffic | Fast sweeps | Rebuilds a mature engine and risks weak queues | Coarse dynamics preserve ranking | High | Replay subset in SUMO |
| Explicit stochastic behavior **(chosen)** | Auditable, sourceable, sensitivity-friendly | Incomplete and less visually rich | Evidence ranges beat imitation | High | Sensitivity and held-out mechanism checks |
| LLM or learned agents | Flexible behavior | No defensible incident truth; variable and costly | Output corresponds to people | High | Deferred absent empirical calibration |
| CEM + MAP-Elites/QD **(chosen)** | Transparent and diversity-aware | Descriptors can manufacture novelty | Causal descriptors are stable | High | Exhaustive worlds and descriptor ablation |
| Deep RL/AST first | Handles sequential adversaries | Training instability and hidden compute | Sequential decisions are the bottleneck | High | Enter only after a sequential limitation is measured |

## Architecture boundaries

```text
schemas + provenance
        ↓
worlds + plans + scenario constraints
        ↓
simulator ports ← engine adapters (golden, SUMO, ELMFIRE)
        ↓
oracles + immutable run artifacts
        ↓
search + replay + certificates
        ↓
interventions + held-out evaluation + registry
```

Rules:

- domain schemas do not import SUMO, ELMFIRE, GeoPandas, or optimizer types;
- search proposes `Scenario` objects and receives summaries through one evaluator port;
- simulators never decide scientific validity or promote certificates;
- oracles never depend on the proposal method;
- interventions compile to typed plan deltas before simulation;
- the registry accepts only immutable run artifacts and certified results;
- notebooks and visualizations are consumers, never the canonical computation path.

## Architecture drift

There is no implementation to exhibit drift yet. The first drift check becomes active when scaffolding begins: imports, schemas, simulator ports, and the evaluator call path must match the dependency direction above.

## Automation candidates

- forbidden-import tests for dependency direction;
- JSON Schema compatibility and canonical-serialization snapshots;
- property tests for units, constraints, conservation, and seeds;
- adapter contracts shared by golden and SUMO traffic paths;
- lineage tests proving that input/container changes alter run identity;
- budget guards counting rejected proposals and every simulator call;
- leakage tests separating calibration, optimizer, certificate, and held-out seeds;
- registry guards against surrogate-only or model-sensitive “supported” results;
- Markdown/local-link and research-schema validation in CI.

## ADR delta

### Context

The project must test an adversarial scenario-selection hypothesis on one workstation while retaining credible fire and microscopic traffic models. A tightly coupled statewide system would delay that experiment and multiply unvalidated assumptions.

### Decision

Use a simulator-agnostic Python kernel, precomputed versioned ELMFIRE hazard fields, SUMO/libsumo full traffic verification, a deterministic golden engine, explicit stochastic behavior, and CEM versus QD. Certify only through full-simulator replay and minimization.

### Alternatives

- one monolithic coupled simulator;
- WUI-NITY as a required runtime;
- a custom geographic traffic engine;
- MATSim as the initial engine;
- learned behavior and deep RL from the start;
- a surrogate-first statewide platform.

### Consequences

- Many traffic/behavior searches can reuse a smaller fire library.
- Cross-model verification is a planned task rather than an afterthought.
- Feedback-sensitive interventions remain out of scope.
- The contribution can survive replacement of an engine.
- Data preparation remains the likely schedule bottleneck.

### Accepted risks

- one-way replay may prove insufficient;
- public evidence may constrain only broad qualitative mechanisms;
- second-geography and practitioner review occur after the method gate;
- storage may need redesign after profiling.

### Revisit triggers

Reopen the decision if:

- edge-event mapping changes an intervention's sign or rank;
- more than 20% of proposed v0 interventions need fire/traffic feedback;
- a full Paradise run exceeds the preregistered runtime assumption by more than 3×;
- traces require more than 1 TB for the first comparative experiment;
- an oracle develops engine-specific semantics;
- CEM or Sobol saturates failure-family discovery;
- an equivalent open end-to-end system is found;
- an adopter requires live integration rather than preplanning evidence.

## Open questions

- Which NIST observations will be held out rather than used for calibration?
- Which public/local evidence can constrain Paradise intersection capacity?
- What is the smallest fire library that preserves rank uncertainty?
- Which failure descriptors remain stable across acceptable behavior worlds?
- Which actor and scheduled decision will evaluate the first intervention card?
