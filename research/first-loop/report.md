# Firescape first-loop evidence appendix

This file is generated from the independently researched and schema-validated JSON records. Claims explicitly marked uncertain, and fields named in each record's `uncertain` array, are omitted.

## Contents

1. [First falsifiable Firescape experiment: an equal-budget benchmark of adversarial scenario search for wildfire-evacuation failure discovery, certificate minimization, and intervention attack-repair-retest on synthetic golden worlds plus one Paradise-Magalia-style case.](#first-falsifiable-firescape-experiment-an-equal-budget-benchmark-of-adversarial-scenario-search-for-wildfire-evacuation-failure-discovery-certificate-minimization-and-intervention-attack-repair-retest-on-synthetic-golden-worlds-plus-one-paradise-magalia-style-case) — Decision: CONDITIONAL GO
2. [Landscape attention and adoption for an open-source, adversarial wildfire-evacuation stress-testing layer ('Firescape') aimed at California planning and operations.](#landscape-attention-and-adoption-for-an-open-source-adversarial-wildfire-evacuation-stress-testing-layer-firescape-aimed-at-california-planning-and-operations)
3. [Public-data benchmark and simulator stack for a Paradise-Magalia wildfire evacuation experiment that couples open wildfire spread modeling, public road-network data, and open traffic simulation.](#public-data-benchmark-and-simulator-stack-for-a-paradise-magalia-wildfire-evacuation-experiment-that-couples-open-wildfire-spread-modeling-public-road-network-data-and-open-traffic-simulation)

## 1. First falsifiable Firescape experiment: an equal-budget benchmark of adversarial scenario search for wildfire-evacuation failure discovery, certificate minimization, and intervention attack-repair-retest on synthetic golden worlds plus one Paradise-Magalia-style case.

**Evidence record:** `algorithm_experiment_and_go_gate.json`

### Scope and pathway

#### Research Object

First falsifiable Firescape experiment: an equal-budget benchmark of adversarial scenario search for wildfire-evacuation failure discovery, certificate minimization, and intervention attack-repair-retest on synthetic golden worlds plus one Paradise-Magalia-style case.

#### Real World Harm And Scale

Wildland-urban interface evacuation failure is a life-safety problem, not a mere travel-time problem. NIST's Camp Fire investigation reports 85 civilian fatalities, more than 19,000 destroyed or damaged structures, and rapid entrapment of evacuees during the 2018 Paradise-Concow-Magalia event. NIST's life-safety report states that about 40,000 people attempted to evacuate, that routes which normally took about 25 minutes took hours or became impassable, and that many people lost every safe egress route. The wildfire-evacuation verification literature also cites about US$3 billion in evacuation costs in the United States. The harm is concentrated in fast-moving, low-notice, high-congestion events where queueing, delayed warning, smoke, road loss, and institutional demand interact.

#### Causal Path To Harm Reduction

A useful first-loop algorithm would improve harm only through a specific chain: better search finds severe but still plausible evacuation failures that ordinary scenario testing misses; replay and minimization convert those failures into small, understandable causal certificates; planners or researchers test a bounded intervention catalog against those certified failure families; held-out attacks identify whether a proposed repair lowers tail risk without harming the worst-served zone; the resulting artifact changes a concrete decision such as zone timing, route control, traffic post staffing, assisted-evacuation capacity, drill design, or evidence collection. If any step fails, the pathway to harm reduction fails. Firescape should therefore optimize for decision-changing evidence, not simulator spectacle.

#### Exact Bottleneck

The bottleneck is not 'simulate wildfire evacuation' but 'discover, under a fixed expensive-simulation budget, more severe and causally diverse plausible failures than strong non-adaptive baselines, then convert them into robust intervention evidence.' The computational subproblem is rare-event search over a coupled scenario envelope with hard joint constraints, mixed continuous/discrete variables, stochastic outputs, and expensive full simulation calls.

#### Decision Or Capability Changed

The first experiment should change one narrow capability decision: whether Firescape should exist as an adversarial evidence layer at all, versus collapsing into simpler baseline scenario testing, trigger-buffer planning, or single-model evacuation analysis. If positive, it also changes the immediate operational capability to produce failure certificates and ranked intervention cards for one bounded case study rather than generic statewide tooling.

### Attention and residual novelty

#### Closest Systems And Attempts

Closest overlaps split into four buckets. First, coupled open research platforms: WUI-NITY integrates wildfire spread, pedestrian, and traffic layers, and the 2023 verification paper shows explicit multi-layer verification tests; WiSE integrates fire dynamics, behavior, traffic, and a Bayesian network to estimate safe egress probability for Paradise. Second, commercial operational products: Ladris Evac advertises evacuation simulation and optimization for planning and active disasters; Genasys Protect advertises zone-based evacuation updates, facility updates, and traffic models. Third, trigger and timing systems: WUIVAC and later fire-traffic trigger papers compute evacuation trigger buffers from fire spread and traffic assumptions. Fourth, transport-only or corridor-optimization work: recent Lahaina modeling isolates lane-capacity and contraflow benefits. Exact overlap with Firescape is partial. These systems show that coupled evacuation modeling already exists, but none of the sourced systems demonstrate the full open loop of equal-budget adversarial search, plausibility rejection, failure replay, minimization, causal-family coverage accounting, intervention selection from discovered failures, and held-out retest as the primary product.

#### Residual Contribution

The credible residual contribution is narrow and methodological: an open benchmark plus execution loop for plausibility-constrained failure search, certificate extraction, and intervention retesting. Firescape should not claim novelty from coupling fire and traffic, from evacuation simulation itself, or from zone-management UX. It should claim novelty only if it produces a transparent protocol in which strong equal-budget baselines are frozen, invalid scenarios are rejected with reasons, discovered failures are replayed and minimized, causal families are counted, interventions are selected from those families, and held-out attacks plus cross-model checks determine whether the repair survives.

#### Why Little Attention

The residual path has likely received less attention for reasons that are partly opportunity and partly warning. Opportunity: it sits between wildfire science, traffic simulation, evacuation behavior, and safety validation, so ownership is fragmented; open benchmark work is less commercially legible than closed products; verification and negative results are under-produced public goods. Warning: the task is expensive, calibration data are scarce, liability is high, and model outputs can easily outrun their evidence base. These warning signs mean the first experiment should be benchmark-first and geography-narrow, not an early productization bet.

### Feasibility and evidence

#### Simulator And Tool Options

Primary fire-side options are ELMFIRE, ForeFire, and Cell2Fire. ELMFIRE is attractive because it is open source, explicitly supports historical reconstruction and validation workflows, and is oriented toward operational wildfire spread use. ForeFire is attractive as a modern open C++ wildfire engine with documentation and demo support. Cell2Fire is attractive for batch statistical runs and research experimentation but is less obviously the primary high-credibility replay engine for this first loop. Primary traffic-side options are SUMO/libsumo and MATSim. SUMO is attractive for scriptable microscopic, intermodal runs and large-network tooling; MATSim is attractive as an authoritative open multi-agent transport framework and as a secondary cross-model check. A practical first loop should also include a pure-Python synthetic benchmark simulator for deterministic golden worlds, plus Python orchestration for scenario schemas, constraints, search, replay, minimization, and accounting.

#### Repeated Unresolved Limitations

Repeated limitations across the sourced literature are consistent: wildfire-evacuation model verification is immature enough that a dedicated protocol only appeared in 2023; calibration and validation datasets are sparse; household behavior and departure timing remain highly variable; smoke, temporary refuge, and institutional demand are hard to encode cleanly; and many models remain scenario-analysis tools rather than decision-grade certified systems. The 2026 behavior paper reinforces that transportation mode can be predicted more reliably than evacuation timing, which is a direct warning against overconfident micro-behavior claims. Recent wildfire mapping safety work also highlights that standard ML thresholds can be unsafe because false negatives carry direct evacuation risk.

#### Excluded Populations Geographies And Failures

The first loop should explicitly exclude or only coarsely represent several important populations and conditions: vehicle-less households, people needing intensive mobility assistance, tourists and transient populations, medically fragile institutional residents, complex school pickup dynamics, non-English warning comprehension, and cross-county mutual-aid dynamics. Geography should initially be limited to one California case and synthetic networks; it should not claim transfer to Hawaii, the Pacific Northwest, or international WUI settings in loop one. Failure coverage should also exclude deep structure-to-structure ignition dynamics, live responder improvisation beyond simple traffic-control actions, detailed communications infrastructure outages, and real-time active-fire forecasting. These exclusions are acceptable for loop one only if they are plainly reported and tied to a narrow claim.

#### Why Now

Several changes since 2020 make the problem more tractable now than a decade ago. Open wildfire and traffic tooling is easier to access and document. The WUI verification protocol now exists. NIST's Camp Fire and ESCAPE publications provide unusually concrete life-safety failure mechanisms and planning metrics. Recent work continues to add behavior, smoke, and transport evidence, while compute and open-data access make large equal-budget experiments easier for a solo researcher. The key reason it is 'now' rather than 'later' is not model novelty; it is that the public benchmark ingredients are finally good enough to test the adversarial-search thesis without pretending to deploy a live operational system.

#### Hidden Dependencies And Penalties

Fatal dependencies remain and should be penalized upfront. If the fire-arrival model is too crude, the discovered failure families may be simulator artifacts. If departure-time and route-choice assumptions dominate the outcome, search may optimize weak sociology rather than robust bottlenecks. If the case-study plan geometry, zone release logic, or institutional demand are unavailable, the experiment degrades into generic traffic stress tests. If cross-model checks reverse the rankings, intervention claims should be vetoed. If the compute budget is so large that only the adaptive method can be tuned properly, the equal-budget claim fails. If no identifiable actor can use a resulting intervention card, translation value falls sharply even when the algorithmic result is positive.

### Experiment and decision

#### Falsifiable Hypothesis

Predeclare the following hypothesis: under the same budget of expensive full simulations, a transparent plausibility-constrained adaptive search built from cross-entropy updates plus quality-diversity archiving will outperform the strongest non-adaptive baseline by at least 25% on plausibility-adjusted severe-failure yield per 1,000 valid full simulations, and by at least 2 additional causal failure families on average, across the golden worlds and one Paradise-Magalia-style case. A second clause should be tested only if the first passes: at least one intervention chosen from adaptive-search certificates reduces held-out tail risk by at least 15% without worsening the worst-served zone by more than 2%.

#### Strongest Baselines

The baseline ladder should be stronger than ordinary random search. Include: exhaustive enumeration on tiny golden worlds; crude Monte Carlo under the base distribution; stratified or Latin-hypercube sampling; Sobol or quasi-random sampling; historical replay and small distortions of historical conditions; expert-authored edge-case scenarios; pure cross-entropy or adaptive importance sampling without diversity maintenance; and a 'single-objective worst clearance time' search that ignores causal diversity. For the intervention phase, include best intervention chosen from random scenarios, best intervention under average clearance time, and expert-picked intervention. All methods must spend the same counted budget of valid expensive simulations and must report invalid proposal rate separately.

#### Experiment Protocol

- **Scope:** Two-stage protocol. Stage A uses deterministic golden worlds with analytically known failures. Stage B uses one bounded Paradise-Magalia-style geographic case with frozen network, zone logic, scenario envelope, and intervention catalog.
- **Scenario Representation:** Typed schema spanning fire-arrival traces or parameters, warning delay and coverage, household departure-delay distributions, route-compliance parameters, background traffic, road-capacity loss, smoke regime, crash or stall events, institutional loading demand, and assisted-evacuation capacity. Every field must carry units, range, provenance, and whether it is directly searched or derived.
- **Plausibility Rules:** Use hard compatibility constraints first, soft likelihood weights second. Hard rejects cover impossible combinations such as contradictory route availability, implausible simultaneous institution states, impossible weather-fire pairings, or evacuation demand that violates frozen population accounting. Soft likelihood weights down-rank but do not forbid rare compound cases.
- **Safety And Equity Oracles:** - unsafe-road person-minutes before fire arrival
- loss of every safe path for any zone or protected cohort
- fire overtakes queue or trapped subqueue on an exposed segment
- missed zone-specific safe-egress deadline
- emergency-access obstruction on declared responder corridors
- worst-zone tail-risk and conditional-value-at-risk metrics
- assisted-evacuation overload or refuge-capacity failure
- **Adaptive Methods:** - Cross-entropy rare-event search over the base scenario distribution
- MAP-Elites-style quality-diversity archive over failure descriptors such as first failed corridor, affected zone, institution involvement, smoke regime, and failure mechanism
- Optional hybrid where cross-entropy proposes candidates and the archive preserves family diversity
- **Failure Descriptors For Qd:** - first corridor or junction that becomes unsafe
- zone or cohort first losing safe egress
- presence of institution or assisted-evacuation overload
- warning-timing regime
- smoke or visibility regime
- capacity-loss mechanism
- **Budgets:** - **Golden Worlds:** Enumerate completely where possible; otherwise cap each method at 5,000 valid full simulations per world.
- **Geographic Case:** Freeze 20,000 valid full simulations per method for discovery, 2,000 valid held-out simulations for evaluation, and a separate replay or minimization budget counted independently.
- **Seeds:** At least 5 random seeds per method.
- **Held Out And Cross Model Checks:** Freeze a held-out scenario pool before intervention testing. Train or discover on one simulator stack, then replay the top failure certificates and top interventions on a smaller secondary model stack or altered fire-arrival assumptions. A repair that only survives on the generating stack is not counted as supported.
- **Failure Replay And Minimization:** Require seeded replay above a fixed reproduction threshold before a failure enters the archive. Then run delta-debugging or variable ablation to find a smallest sufficient cause set and store the minimized certificate as the public artifact.
- **Intervention Phase:** Use a small frozen catalog: staged release timing, route split, traffic-control posts, emergency-only lane protection, warning-delay reduction, and assisted-capacity increase. Select interventions separately using adaptive and baseline discovery sets, then attack each chosen intervention on the unseen held-out pool.
- **Statistics And Outputs:** Primary metrics: plausibility-adjusted severe-failure yield, causal-family coverage, best-tail-risk found, invalid proposal rate, replay success rate, minimization size, held-out intervention tail-risk reduction, worst-zone effect, and compute per valid simulation. Publish full run tables, negative results, and rejected scenarios.

#### Success And Kill Thresholds

- **Go:** GO only if the adaptive method beats the best non-adaptive baseline by at least 25% on plausibility-adjusted severe-failure yield per 1,000 valid full simulations in at least 4 of 5 seeds, discovers at least 2 extra causal families on average, maintains invalid-scenario share below 15% after warmup, and yields at least one intervention that cuts held-out tail risk by 15% or more without worsening the worst-served zone by more than 2%. Cross-model replay must preserve the sign of the intervention effect.
- **Conditional Go:** CONDITIONAL GO if the adaptive method shows a smaller but repeatable advantage, for example 10-25% yield improvement or 1 additional causal family, but intervention robustness or cross-model stability is still incomplete. In that case, continue only as a benchmark-and-methodology project, not as a broad product build.
- **Kill Or No Go:** NO-GO if the best strong baseline matches the adaptive method within 10%, if most discovered failures are ruled implausible or fail replay, if minimization cannot produce understandable certificates, or if intervention rankings flip under modest model changes. Also stop if equal-budget accounting reveals that the gain comes mainly from hidden tuning or extra simulator calls.

#### Solo 30 60 Day Feasibility

A solo software researcher can plausibly execute a disciplined first loop in 30-60 days if the scope is frozen hard. Days 1-10: implement schema, constraint layer, golden worlds, oracle tests, and baseline accounting. Days 11-25: complete strong baselines and deterministic replay/minimization on golden worlds. Days 26-45: wire one geographic case and run equal-budget discovery. Days 46-60: run held-out intervention attacks, cross-model subset checks, and write the benchmark report. This is only feasible if the geographic case is simplified, the intervention catalog is tiny, and the secondary simulator check is replay-only on a subset. It is not feasible in 60 days to build a calibrated statewide platform or production operator interface.

#### Twelve Month Proof Target

A credible 12-month proof target is one open benchmark suite plus two case studies showing that the same benchmark protocol transfers across at least two different community topologies, with independent critique from one wildfire-evacuation researcher and one practitioner. The proof should include: published negative results, a stable certificate format, a baseline library, one supported intervention family that survives held-out attacks and cross-model checks, and a documented list of evidence gaps that materially change decisions. That would justify further investment; anything short of this should remain a bounded research artifact.

#### Actors And Translation Path

Nearest adopters are not consumers but expert intermediaries: county or city emergency managers, transportation planners, wildfire consultants, state OES and CAL FIRE analysts, and academic collaborators building evacuation drills or planning studies. The workflow insertion point is pre-season planning, exercise design, after-action learning, and evidence prioritization, not live incident command. The usable outputs are failure certificates, intervention cards, scenario-coverage reports, and 'highest decision value data to collect next' memos.

#### Strongest Rejection Argument

The strongest rejection case is that wildfire-evacuation decisions are already dominated by simpler bottleneck analyses, trigger buffers, institutional planning, and uncertain human behavior, so adversarial search mainly adds computational theater. If the severe failures it finds are mostly consequences of debatable departure-time assumptions or fire-arrival modeling noise, then the method may look novel while contributing little beyond what a strong planner or a trigger-buffer model already knows.

#### Evidence That Changes Decision

Evidence that would raise the ranking: a clean win over strong equal-budget baselines on golden worlds and the first real case; independent reproduction by another group; practitioner confirmation that minimized certificates are legible and decision-relevant; and cross-model agreement on intervention direction. Evidence that would lower or reverse the ranking: parity with stratified or cross-entropy baselines, high invalid-scenario rates, instability under replay, intervention reversals under alternate model stacks, or proof that a simpler trigger-plus-capacity workflow answers the same decisions with far less complexity.

#### Go No Go Assessment

- **Judgment:** CONDITIONAL GO
- **Rationale:** There is still a real residual contribution, but only for a narrow benchmark-first research program. Existing systems already cover coupled simulation, trigger timing, and operational zone management. The differentiated claim survives only if Firescape proves that open adversarial search plus certificate extraction plus intervention retest beats strong equal-budget baselines and produces more decision-ready evidence than ordinary scenario sets.
- **Scores 0 To 5:** - **Importance:** 5
- **Leverage:** 4
- **Neglectedness:** 3
- **Tractability:** 3
- **Accessibility:** 3
- **Marginal Contribution:** 4
- **Translation:** 3
- **Evidence Confidence:** 3
- **What This Means:** Proceed with FIRE-R002 through FIRE-R008 as a frozen research benchmark. Do not build statewide infrastructure, polished product UX, or broad hazard generalization before the first superiority test and held-out intervention test pass.

#### Sources

- title: NIST Investigation of the 2018 Camp Fire | url: https://www.nist.gov/programs-projects/wildland-urban-interface-wui-fire-data-collection-parcel-vulnerabilities/nist | date: updated 2026-07-21 | source type: official government project page | claim supported: Camp Fire scale, fatalities, destroyed structures, multi-year federal-state research program, and authoritative publication trail.
- title: Life Safety During the Camp Fire | url: https://www.nist.gov/programs-projects/wildland-urban-interface-wui-fire-data-collection-parcel-vulnerabilities/nist/life | date: accessed 2026-08-09 | source type: official government project page | claim supported: 40,000-person evacuation, gridlock, route failure, burnover events, and no-safe-egress mechanisms.
- title: WUI Fire Evacuation and Sheltering Considerations: Assessment, Planning, and Execution (ESCAPE) | url: https://www.nist.gov/programs-projects/wildland-urban-interface-wui-fire-data-collection-parcel-vulnerabilities/escape | date: accessed 2026-08-09 | source type: official government project page | claim supported: Need for planning metrics beyond simple evacuation, temporary refuge concepts, and modern low-notice wildfire constraints.
- title: The verification of wildland-urban interface fire evacuation models | url: https://doi.org/10.1007/s11069-023-05913-2 | date: 2023-03-28 | source type: peer-reviewed paper | claim supported: 24-test verification protocol, lack of prior standardized WUI verification, multi-layer credibility issues, and cost estimate reference.
- title: WUI-NITY 4: An Industry-Ready WUI Fire Evacuation Model | url: https://portal.research.lu.se/files/224899975/WUI-NITY4.pdf | date: 2024-10 | source type: technical report | claim supported: Active open wildfire-evacuation platform lineage and current maturity of coupled evacuation modeling.
- title: The simulation of wildland-urban interface fire evacuation: The WUI-NITY platform | url: https://doi.org/10.1016/J.SSCI.2020.105145 | date: 2021 | source type: peer-reviewed paper | claim supported: Existence of an open coupled platform and prior art that already combines wildfire and evacuation layers.
- title: Evac | url: https://www.ladris.com/products/evacuation | date: accessed 2026-08-09 | source type: official product page | claim supported: Commercial evacuation simulation and optimization capability for planning and active disasters.
- title: Genasys Protect | url: https://genasys.com/genasys-protect/ | date: accessed 2026-08-09 | source type: official product page | claim supported: Commercial zone-based evacuation updates, facility updates, and traffic-model positioning.
- title: ELMFIRE documentation | url: https://elmfire.io/ | date: accessed 2026-08-09 | source type: official documentation | claim supported: Open-source fire-spread model with reconstruction and validation workflows.
- title: ForeFire Documentation | url: https://forefire.readthedocs.io/en/latest/ | date: accessed 2026-08-09 | source type: official documentation | claim supported: Modern open wildfire simulation engine option for secondary or alternative fire modeling.
- title: Cell2Fire: A Cell Based Forest Fire Growth Model C++/Python | url: https://github.com/cell2fire/Cell2Fire | date: accessed 2026-08-09 | source type: official source repository | claim supported: Research-use open fire simulator with batch and statistical capabilities.
- title: SUMO Documentation | url: https://sumo.dlr.de/docs/index.html | date: accessed 2026-08-09 | source type: official documentation | claim supported: Open microscopic intermodal traffic simulator suitable for scripted evacuation experiments.
- title: MATSim Documentation | url: https://matsim.org/docs/ | date: accessed 2026-08-09 | source type: official documentation | claim supported: Authoritative open multi-agent transport framework suitable for secondary checks.
- title: Performance Measurement System (PeMS) Data Source | url: https://dot.ca.gov/programs/traffic-operations/mpr/pems-source | date: accessed 2026-08-09 | source type: official government data page | claim supported: California traffic detector coverage and historical archive availability.
- title: 3D Elevation Program | url: https://www.usgs.gov/3d-elevation-program | date: accessed 2026-08-09 | source type: official government data page | claim supported: Free topographic and lidar-derived elevation products for terrain modeling.
- title: NOAA High-Resolution Rapid Refresh (HRRR) Model | url: https://registry.opendata.aws/noaa-hrrr-pds/ | date: accessed 2026-08-09 | source type: official open-data registry page | claim supported: Open 3 km hourly weather archive and permissive public-data access.
- title: LEHD Data | url: https://lehd.ces.census.gov/data/ | date: accessed 2026-08-09 | source type: official government data page | claim supported: Public LODES and related employment-flow data for demand approximation.
- title: Scalable End-to-End Autonomous Vehicle Testing via Rare-event Simulation | url: https://arxiv.org/abs/1811.00145 | date: 2018-10-31 | source type: research paper | claim supported: Adaptive importance sampling can accelerate rare-event discovery over naive Monte Carlo under fixed simulation budgets.
- title: Adaptive Stress Testing for Autonomous Vehicles | url: https://arxiv.org/abs/1902.01909 | date: 2019-02-05 | source type: research paper | claim supported: AST frames failure discovery as a search problem and shows simulator-efficient discovery of more likely failures than weaker search.
- title: The Cross-Entropy Method for Estimation | url: https://web.stanford.edu/~glynn/papers/2013/KroeseRubinsteinG13.pdf | date: 2013 | source type: tutorial chapter | claim supported: Rare-event estimation and importance-sampling rationale for cross-entropy baselines and adaptive search.
- title: Quality Diversity Algorithms | url: https://members.loria.fr/jbmouret/qd.html | date: accessed 2026-08-09 | source type: research group overview | claim supported: MAP-Elites-style quality-diversity is straightforward and useful for preserving many high-performing, behaviorally diverse solutions.
- title: WUIVAC: a wildland-urban interface evacuation trigger model applied in strategic wildfire scenarios | url: https://doi.org/10.1007/s11069-006-9032-y | date: 2007 | source type: peer-reviewed paper | claim supported: Prior art on trigger buffers and strategic evacuation timing using fuels, weather, and topography.
- title: Setting Wildfire Evacuation Triggers by Coupling Fire and Traffic Simulation Models: A Spatiotemporal GIS Approach | url: https://doi.org/10.1007/s10694-018-0771-6 | date: 2018 | source type: peer-reviewed paper | claim supported: Prior art on coupled fire-traffic trigger timing and probabilistic trigger buffers.
- title: A Bayesian agent-based model and software for wildfire safe evacuation planning and management | url: https://doi.org/10.1177/1748006X241259215 | date: 2024-07-26 | source type: peer-reviewed paper | claim supported: WiSE as a recent integrated fire-behavior-traffic safe-egress framework and proof that integrated planning systems already exist.
- title: Characterizing and Predicting Wildfire Evacuation Behavior: A Dual-Stage ML Approach | url: https://arxiv.org/abs/2603.02223 | date: 2026-02-10 | source type: research paper | claim supported: Recent evidence that evacuation timing remains behaviorally difficult to predict, reinforcing uncertainty limits.
- title: Macroscopic Traffic Flow Network Modeling For Wildfire Evacuation: A Game-Theoretic Junction Optimization Approach with Application to Lahaina Fire | url: https://arxiv.org/abs/2603.29055 | date: 2026-03-30 | source type: research paper | claim supported: Recent active work on wildfire-evacuation optimization and the importance of lane-capacity bottlenecks and contraflow.
- title: Conformal Risk Control for Safety-Critical Wildfire Evacuation Mapping: A Comparative Study of Tabular, Spatial, and Graph-Based Models | url: https://arxiv.org/html/2603.22331v1 | date: 2026-03-20 | source type: research paper | claim supported: Recent evidence that safety-critical wildfire prediction needs explicit false-negative controls and that standard thresholds can be unsafe.


## 2. Landscape attention and adoption for an open-source, adversarial wildfire-evacuation stress-testing layer ('Firescape') aimed at California planning and operations.

**Evidence record:** `landscape_attention_and_adoption.json`

### Scope and pathway

#### Research Object

Landscape attention and adoption for an open-source, adversarial wildfire-evacuation stress-testing layer ('Firescape') aimed at California planning and operations.

#### Real World Harm And Scale

- Wildfire evacuation failure is directly life-critical. NIST's Camp Fire NETTRA case study reports that the 2018 Camp Fire quickly forced the evacuation of 40,000 people and resulted in 85 fatalities and more than 18,000 destroyed structures.
- The problem is not limited to one town. A June 4, 2026 University of California release reports that 17.7 million Americans live in communities below a critical six-exit threshold, and 2.5 million of them are also in high wildfire hazard areas.
- Operational communication failures can amplify the harm. Los Angeles County stated on January 10, 2025 that a correctly targeted alert was erroneously sent to nearly 10 million residents, showing that alerting, zoning, routing, and public trust are part of the same safety system.

#### Causal Path To Harm Reduction

- Firescape's plausible path is: stress-test an existing evacuation plan or zone design under coupled fire, traffic, human-behavior, and communications failures; identify the specific assumptions that break; then convert those findings into route, zoning, trigger, phasing, and refuge-area changes before the next fire or plan update.
- The measurable outputs are lower clearance times, fewer exposed or stranded households, lower dependence on improvised refuge, fewer shadow-evacuation spillovers, and better identification of neighborhoods where evacuation is infeasible without infrastructure or policy change.
- The translation mechanism is strongest when the tool is used before safety-element updates, CWPP revisions, CEQA wildfire analysis, evacuation-study grants, vendor procurement, and annual drills, rather than during live incident command.

#### Exact Bottleneck

- The bottleneck is not 'wildfire evacuation' in general. It is the lack of an open, auditable, scenario-search layer that can falsify evacuation assumptions under no-notice conditions, road failures, alert delays, tourist surges, and vulnerable-population constraints using mostly public California data.
- Current options split into three incomplete buckets: closed commercial systems with adoption but limited public auditability; research platforms that couple fire/traffic/behavior but are not county-ready; and narrow algorithm papers that optimize one slice of the stack without reproducing agency workflows.
- Because of that split, counties can buy software or cite studies, but still lack a transparent way to compare plan robustness across tools, assumptions, and worst-case envelopes.

#### Decision Or Capability Changed

- Primary decisions changed: which evacuation zones exist, when each zone is warned or ordered, whether staged evacuation or contraflow is justified, where temporary fire refuge areas should exist, and which road or vegetation projects matter most for life safety.
- Planning decisions changed: what a city or county writes into a safety element, local hazard mitigation plan, CWPP, evacuation study, or CEQA wildfire appendix.
- Procurement and oversight capability changed: whether an OEM, sheriff, fire district, county consultant, or board can independently test a vendor-backed plan instead of accepting a black-box output.

### Attention and residual novelty

#### Closest Systems And Attempts

- WUI-NITY/PREACT is the closest open integrated attempt. The 2020 NFPA report describes coupled fire, pedestrian, and traffic simulation plus dynamic vulnerability mapping; the public GitHub repo says the software is under active development, contains incomplete features and bugs, only the Windows dev branch works, and one macro traffic module is broken while SUMO is preferred.
- WiSE is the closest probabilistic planning platform. The 2024/2025 paper says it integrates fire dynamics, a human behavior model, and traffic simulation to estimate safe egress probability; the SFPE WUI Research Library says Pacific Gas & Electric sponsored the project and that it was validated against the 2018 Camp Fire.
- Genasys Protect/Zonehaven is the strongest evacuation-zoning and alerting incumbent. Genasys said in June 2021 that Zonehaven was trusted by more than 170 fire districts, 140 law enforcement agencies, 200 cities, and 3,300 evacuation zones covering 3.2 million people in Northern California and Southern Oregon.
- Ladris is the strongest California planning-and-response commercial adjacent. Public pages show work with Marin, Truckee, Tahoe Basin, and Nevada County, plus an OEZ standard for evacuation zones; its differentiation is operational packaging and customer deployment rather than open benchmarking.
- WUI-PEM is a methodology, not a full simulation stack. It offers a six-step phased zone evacuation method for planning, management, and training.
- WUISHOW is a collaborative visualization layer, not a standalone benchmarked simulator. The 2025 publication describes it as a digital collaborative decision-making tool for procedural visualization of wildfire evacuation simulations.
- PyroRL and AgentEvac are the closest open algorithmic adjacencies. PyroRL is a published RL environment for wildfire evacuation, but at gridworld abstraction; AgentEvac couples SUMO with LLM-driven agents, but public evidence suggests an early-stage research codebase rather than a field-validated county tool.
- Recent coupled or adjacent research includes Camp Fire ABM work, Kincade decision and traffic studies, Glass and Silverado traffic-data analyses, time-expanded network routing, RESCUE dynamic routing, route optimization on the 2023 McDougall Creek fire, and conformal-risk-control fire-mapping work. These are important ingredients, but not a turnkey California planning benchmark.

### Feasibility and evidence

#### Simulator And Tool Options

- Fire layer options: import precomputed outputs from FlamMap/FARSITE/WISE/Prometheus into an evacuation stack, as WUI-NITY supports, or use an open spread simulator such as ELMFIRE, Cell2Fire, ForeFire, or another raster-producing tool for scenario generation.
- Traffic layer options: SUMO/libsumo is the most practical open choice for first-loop routing and closure experiments. MATSim is an alternative for larger demand modeling but adds setup overhead.
- Behavior layer options: start with empirical distributions and simple decision models grounded in Camp Fire and Kincade work. Treat LLM-driven agents from AgentEvac or FLARE-like models as an exploratory branch, not the core benchmark.
- Planning and visualization options: WUI-NITY/PREACT can be studied or adapted; WUISHOW-like collaboration views can come later; GIS outputs can remain simple GeoJSON/FlatGeobuf plus static maps in the first loop.

#### Repeated Unresolved Limitations

- Published work repeatedly runs into the same problems: limited validation datasets, heavy dependence on assumed behavior, and weak comparability across studies.
- Open tools remain fragile. WUI-NITY's public repo explicitly mentions incomplete features and bugs; its macro traffic module is broken; and some models are not recommended because they are not fully verified and validated.
- Operational workflows remain fragmented. Ladris' OEZ page argues that jurisdictions still hand-copy zones between GIS and alerting systems, which is a real systems-integration failure rather than a pure modeling failure.
- Communications reliability remains unresolved. Los Angeles County's January 2025 statement shows that even when a targeted message is prepared correctly, downstream software and telecom failures can still break public trust.

#### Why Now

- Why now is stronger than it was a few years ago. NIST updated ESCAPE in April 2025, said 30 California communities had already incorporated the earlier guidance, and emphasized no-notice planning, decision zones, and predesignated refuge areas.
- The regulatory and planning context is sharper. OPR/LCI guidance ties SB 99, AB 747, and AB 1409 to safety-element obligations, and CEQA wildfire scrutiny has intensified after recent California litigation.
- The data and research base is also richer. Camp Fire, Kincade, Glass, Silverado, Nevada County, Tahoe, and Roxborough Park together provide more calibration and benchmark material than was available in 2020.
- Commercial adoption and public failures are visible enough to create demand for independent audit. Genasys and Ladris show that agencies buy evacuation technology; the January 2025 Los Angeles alert failure shows why transparent robustness testing matters.

### Experiment and decision

#### Falsifiable Hypothesis

- Hypothesis: in a Paradise-Magalia-style California WUI envelope, an open adversarial stress-testing layer built on public data and SUMO-class traffic simulation will find at least one decision-relevant failure mode that a standard as-planned baseline misses, and at least one feasible mitigation that improves a primary safety metric by 20% or more without materially worsening the worst-off zone.
- Failure condition: the open stress test does not reveal anything beyond simple staged-evacuation, vehicle-reduction, or route-priority heuristics, or the results are too sensitive to arbitrary fire and behavior assumptions to be trusted.

#### Actors And Translation Path

- Key actors are county OEM directors, sheriffs, CAL FIRE unit planners, fire districts, public works and traffic engineers, MPO or transportation consultants, safety-element and CEQA consultants, Fire Safe Councils, and state guidance bodies such as OPR/LCI and Cal OES.
- The insertion point is pre-incident planning: safety-element revisions, local hazard mitigation plans, CWPP updates, evacuation-study grants, after-action reviews, annual drills, and vendor procurement or renewal.
- The usable outputs are not academic metrics alone. They are failure maps, route-priority tables, zone-timing recommendations, TFRA gaps, alert-timing stress cases, and a short technical appendix that can survive policy or legal scrutiny.

#### Sources

- title: WUI-NITY: a platform for the simulation of wildland-urban interface fire evacuation | url: https://content.nfpa.org/-/media/Project/Storefront/Catalog/Files/Research/Research-Foundation/Reports/WUI/RFWUINITY.pdf | date: 2020-04 | source type: NFPA / Fire Protection Research Foundation report | claim supported: WUI-NITY couples fire, pedestrian, and traffic simulation; uses FARSITE, trigger buffers, and case studies; aimed at planning and situational awareness.
- title: bran-jnw/wuinity | url: https://github.com/bran-jnw/wuinity | date: accessed 2026-08-09 | source type: GitHub repository | claim supported: Public WUI-NITY/PREACT code exists, but repo warns of incomplete features, bugs, Windows-only development, and broken macro traffic support.
- title: A Bayesian agent-based model and software for wildfire safe evacuation planning and management | url: https://journals.sagepub.com/doi/10.1177/1748006X241259215 | date: 2024-07-26 first published online | source type: Peer-reviewed journal article | claim supported: WiSE integrates fire dynamics, human behavior, and traffic to estimate safe egress probability.
- title: WUI Research Library - Wildfire Egress Model and Simulation Platform entry | url: https://www.sfpe.org/foundation/wildland-urban-interface/wuiresearch | date: accessed 2026-08-09 | source type: SFPE Foundation research library | claim supported: PG&E sponsored WiSE; the platform integrates human decision, traffic, and wildfire models and was validated against the 2018 Camp Fire.
- title: WUI-PEM: Wildfire Phased Zone Evacuation Methodology | url: https://ojs.iscram.org/index.php/Proceedings/article/view/78 | date: 2024 | source type: Conference proceedings article | claim supported: WUI-PEM is a six-step methodology for staged zone evacuation planning, management, and training.
- title: WUISHOW: A digital collaborative wildfire evacuation platform | url: https://portal.research.lu.se/en/publications/wuishow-a-digital-collaborative-wildfire-evacuation-platform/ | date: 2025-09-01 | source type: Published meeting abstract / university publication page | claim supported: WUISHOW is a collaborative visualization and decision-support interface for simulation outputs, not a standalone benchmarked simulator.
- title: PyroRL: A Reinforcement Learning Environment for Wildfire Evacuation | url: https://joss.theoj.org/papers/10.21105/joss.06739 | date: 2024-09-18 | source type: JOSS software paper | claim supported: PyroRL is a published open RL environment for wildfire evacuation research.
- title: denoslab/AgentEvac | url: https://github.com/denoslab/AgentEvac | date: accessed 2026-08-09 | source type: GitHub repository | claim supported: AgentEvac is an open SUMO plus LLM wildfire evacuation simulator focused on PADM-style agent behavior.
- title: OEZ Standard | url: https://www.ladris.com/products/open-evacuation-zones | date: accessed 2026-08-09 | source type: Commercial product page | claim supported: Ladris offers a free open evacuation zone standard integrated with existing GIS and alerting tools and says it is in production across multiple states.
- title: Marin Wildfire Protection Authority selects Ladris AI for disaster readiness | url: https://www.ladris.com/news/marin-selects-ladris | date: 2024-03-06 | source type: Commercial press release | claim supported: Marin selected Ladris to enhance evacuation preparedness and evaluate options to reduce evacuation times.
- title: Tahoe Basin wildfire evacuation simulations spotlight infrastructure limitations and public safety dangers | url: https://www.ladris.com/news/tahoe-basin-wildfire-evacuation-simulations-spotlight-infrastructure-limitations-public-safety-dangers | date: 2024-08-28 | source type: Commercial press release | claim supported: Ladris and partners ran 400+ Tahoe-wide simulations and reported much longer evacuations than legacy planning assumptions.
- title: Town of Truckee customer story | url: https://www.ladris.com/stories/answering-the-question-how-much-time-do-we-have-to-evacuate | date: accessed 2026-08-09 | source type: Commercial customer story | claim supported: Truckee used Ladris during the Mosquito Fire threat and generated an evacuation plan within hours.
- title: Nevada County Evacuation Study | url: https://www.nevadacountyca.gov/3831/Nevada-County-Evacuation-Study | date: accessed 2026-08-09 | source type: County government page | claim supported: CAL FIRE grant funding supported a county evacuation study; Ladris performed wildfire and traffic modeling for scenario ranking.
- title: Genasys Inc. Acquires Emergency Evacuation SaaS Provider, Zonehaven | url: https://genasys.com/press-releases/genasys-inc-acquires-emergency-evacuation-saas-provider-zonehaven/ | date: 2021-06-09 | source type: Commercial press release | claim supported: Zonehaven had broad California adoption before acquisition and became part of the Genasys stack.
- title: Yuba County, California - Government | url: https://genasys.com/case-studies/yuba-county-california-case-study/ | date: accessed 2026-08-09 | source type: Commercial case study | claim supported: Yuba County uses Genasys Protect for evacuation management and repopulation; case study describes cross-agency use and reduced dispatch burden.
- title: Alert San Diego | url: https://www.alertsandiego.org/ | date: accessed 2026-08-09 | source type: County emergency portal | claim supported: San Diego County's public emergency portal links residents to Genasys Protect for live zones and road closures.
- title: Los Angeles County Moves to Immediately Address Emergency Alert Problems and Implement Solutions | url: https://lacounty.gov/2025/01/10/los-angeles-county-moves-to-immediately-address-emergency-alert-problems-and-implement-solutions/ | date: 2025-01-10 | source type: County government statement | claim supported: A correctly targeted alert was erroneously sent to nearly 10 million residents; Genasys and telecom issues were under review.
- title: Fire Hazard Planning Technical Advisory | url: https://www.lci.ca.gov/wp-content/uploads/20220817-Fire_Hazard_Planning_TA.pdf | date: 2022-08-17 | source type: California state planning guidance | claim supported: SB 99, AB 747, and AB 1409 create evacuation-planning obligations in California safety elements and related planning documents.
- title: Draft Evacuation Planning Technical Advisory Released for Public Comment | url: https://lci.ca.gov/newsroom/news/2023/10-05/ | date: 2023-10-05 | source type: California state planning announcement | claim supported: California continued to refine evacuation-planning guidance for local governments under SB 99, AB 747, and AB 1409.
- title: A Case Study of the Camp Fire - Notification, Evacuation, Traffic, and Temporary Refuge Areas (NETTRA) | url: https://www.nist.gov/publications/case-study-camp-fire-notification-evacuation-traffic-and-temporary-refuge-areas-nettra | date: 2023-07-18 | source type: NIST case study | claim supported: Camp Fire evacuation scale, fatalities, and the importance of traffic, notification, and temporary refuge areas.
- title: NIST Updates Critical Wildfire Evacuation and Sheltering Guidance | url: https://www.nist.gov/news-events/news/2025/04/nist-updates-critical-wildfire-evacuation-and-sheltering-guidance | date: 2025-04-24 | source type: NIST news release | claim supported: ESCAPE guidance was updated; 30 California communities had incorporated earlier guidance; no-notice planning and TFRAs were emphasized.
- title: National Wildfire Evacuation Planning Guidance, 1st Edition | url: https://www.usfa.fema.gov/downloads/pdf/publications/national-wildfire-evacuation-guidance-1st-edition.pdf?cacheKey=1783555200124 | date: 2026 | source type: USFA/FEMA guidance | claim supported: Federal guidance now provides a structured evacuation planning framework including zones, routing, notifications, and AFN/CTN populations.
- title: Six roads to safety: New study finds a critical threshold for wildfire survival | url: https://www.universityofcalifornia.edu/news/six-roads-safety-new-study-finds-critical-threshold-wildfire-survival | date: 2026-06-04 | source type: University news release | claim supported: National egress-threshold evidence quantifies how many people live in communities with structurally poor evacuation access.
- title: Testing Wildfire Evacuation Strategies and Coordination Plans for Wildland-Urban Interface Communities in California | url: https://ucits.org/projects/testing-wildfire-evacuation-strategies-and-coordination-plans-for-wildland-urban-interface-communities-in-california/ | date: 2021-08-01 to 2023-06-30 project window | source type: UC ITS project page | claim supported: California-focused public research on strategy testing exists, including policy-oriented scenario evaluation.
- title: Traffic dynamics during the 2019 Kincade wildfire evacuation | url: https://www.sciencedirect.com/science/article/pii/S136192092300007X | date: 2023 | source type: Peer-reviewed journal article | claim supported: Empirical traffic-flow data for a major California wildfire evacuation exist for model calibration and validation.
- title: The analysis of traffic data of wildfire evacuation: the case study of the 2020 Glass Fire | url: https://www.sciencedirect.com/science/article/pii/S0379711223001777 | date: 2023 | source type: Peer-reviewed journal article | claim supported: Glass Fire data show background traffic and observed traffic dynamics matter for validation.
- title: Traffic Performance Indicators for Evacuation: The Case Study of the 2020 Silverado Wildfire | url: https://link.springer.com/article/10.1007/s10694-025-01813-y | date: 2025 | source type: Peer-reviewed journal article | claim supported: Silverado wildfire analysis extends empirical traffic benchmarking and performance indicators.
- title: Social vulnerabilities and wildfire evacuations: A case study of the 2019 Kincade Fire | url: https://www.sciencedirect.com/science/article/pii/S0925753524001474 | date: 2024 | source type: Peer-reviewed journal article | claim supported: Social vulnerability affects evacuation behavior and should be represented in planning and benchmarking.
- title: Fast-moving dire wildfire evacuation simulation | url: https://ncst.ucdavis.edu/research-product/fast-moving-dire-wildfire-evacuation-simulation | date: 2022 | source type: Research product summary | claim supported: Camp Fire-inspired ABM work targets extreme no-notice wildfire evacuation scenarios and highlights behavior gaps.
- title: Conformal Risk Control for Safety-Critical Wildfire Evacuation Mapping | url: https://arxiv.org/abs/2603.22331 | date: 2026-03-20 | source type: arXiv preprint | claim supported: Recent work applies formal safety guarantees to wildfire threat mapping, showing a path for robust or adversarial evaluation.
- title: Evacuation Planning on Time-Expanded Networks with Integrated Wildfire Information | url: https://arxiv.org/abs/2410.14500 | date: 2024-10-18 | source type: arXiv preprint | claim supported: Recent open algorithmic work addresses wildfire-aware routing but not the full planning stack.


## 3. Public-data benchmark and simulator stack for a Paradise-Magalia wildfire evacuation experiment that couples open wildfire spread modeling, public road-network data, and open traffic simulation.

**Evidence record:** `public_data_simulators_and_validation.json`

### Scope and pathway

#### Research Object

Public-data benchmark and simulator stack for a Paradise-Magalia wildfire evacuation experiment that couples open wildfire spread modeling, public road-network data, and open traffic simulation.

#### Real World Harm And Scale

The target harm is civilian death, burnover exposure, failed evacuation, and delayed rescue during fast-moving wildland-urban interface fires. In the Camp Fire on November 8, 2018, the communities of Concow, Paradise, and Magalia were rapidly impacted; NIST reports 85 fatalities, more than 18,000 destroyed structures, more than 2,200 fire observations for the progression reconstruction, and more than 2,600 notification/evacuation/traffic/temporary-refuge-area observations for life-safety reconstruction. The NETTRA report states that about 40,000 people evacuated, 31 temporary refuge areas were used by more than 1,200 civilians, and 198 rescue or evacuation-assistance events involved at least 1,000 civilians. Later California cases show the traffic problem generalizes beyond Paradise: Sonoma County's 2019 Kincade Fire after-action report says more than 186,000 residents evacuated at peak; the 2020 Glass Fire traffic paper analyzes freeway disruption during evacuation; the 2025 Silverado paper reports nearly 100,000 people were ordered to evacuate. The practical scale is therefore not a niche single-town issue but a recurring California mass-evacuation problem in which route capacity, closure timing, and departure timing interact with fire progression.

#### Causal Path To Harm Reduction

A usable causal chain is: better public benchmark and calibrated open simulator stack -> more credible pre-season comparison of staged-zone releases, route controls, closure policies, and temporary-refuge-area placement -> improved county and fire-agency plans, drills, and trigger thresholds -> faster and less conflicted evacuations under comparable future fires -> lower trapped-vehicle minutes, fewer burnovers, fewer ad hoc rescues, and lower fatality risk. The technical intervention is not 'predict every household perfectly'; it is narrowing the decision space for planners by ruling out obviously bad release orders and by quantifying which uncertainties matter most before a real incident.

#### Exact Bottleneck

The bottleneck is assembling a reproducible end-to-end public loop that turns publicly available fire, hazard, road, zone, and demographic data into a coupled fire-traffic replay for Paradise-Magalia with an empirical validation ladder. Existing components are individually available, but the hard part is the seam: aligning fire-arrival-time evidence to a road graph, mapping evacuation zones to demand buckets, converting fire effects into link penalties and closures, and validating outputs against real wildfire traffic data instead of generic highway-capacity assumptions.

#### Decision Or Capability Changed

This research should decide whether one software researcher can build a credible open benchmark and baseline stack for Paradise-Magalia in 30 to 60 days, with enough empirical grounding to justify a larger translation effort. The changed capability would be an auditable replay-and-policy-comparison harness rather than a polished operational decision-support product.

### Attention and residual novelty

#### Closest Systems And Attempts

Closest fire simulators: ELMFIRE with the Berkeley Fire Lab Wildland-Urban Extension, ForeFire, Cell2Fire and its more actively maintained C2FK fork, and PyTorchFire. Closest evacuation couplers: WUI-NITY/PREACT, which explicitly couples wildfire, pedestrian, and traffic layers; SUMO/libsumo and MATSim, which provide the traffic side but not wildfire physics; and the 2020 Paradise/Mill Valley 'Simulation Pipeline for Traffic Evacuation in Urban Areas' paper, which used an interactive traffic simulation pipeline for California wildfire-risk cities. Closest empirical validation work: NIST's Camp Fire progression and NETTRA reconstructions, plus empirical traffic studies for the 2019 Kincade Fire, 2020 Glass Fire, and 2020 Silverado Fire. Exact overlap remains limited because no inspected source provided a public, versioned Paradise benchmark that already bundles open fire progression, open evacuation-zone demand, and a validated open traffic-coupling pipeline.

#### Funding Commercial And Government Activity

Government and quasi-public activity is substantial. NIST invested in a multi-report Camp Fire case study and released public supporting data. CAL FIRE FRAP and OSFM maintain statewide fire perimeter and hazard data. Butte County states that it received a California Department of Housing and Community Development grant in 2021 and hired a transportation consulting firm in 2022 to produce evacuation modeling scenarios and community evacuation maps. Caltrans maintains PeMS and funds evacuation-route research through DRISI and related reports. NFPA's Fire Protection Research Foundation has published WUI-NITY project material. Commercial/open operational signals exist but are narrower: ELMFIRE is used operationally in the Pyrecast project and was built by Chris Lautenberger/CloudFire with Berkeley Fire Lab extensions, but there is no evidence in the inspected material of a broad commercial market already solved by an open Paradise-grade benchmark.

#### Residual Contribution

The real residual contribution is not inventing another fire or traffic model. It is packaging a versioned Paradise-Magalia benchmark with public input data, public preprocessing steps, a documented coupling contract between fire and traffic layers, baseline policies, and a validation ladder tied to Camp Fire evidence and cross-checked against Kincade/Glass/Silverado traffic changes. That would fill a reproducibility and validation gap that current projects leave open.

#### Why Little Attention

Reasons for lower attention are mostly structural. Fire modelers, transport modelers, and emergency-management practitioners work on different data, tooling, and publication norms. County evacuation operations are highly local, and public release of detailed operational logs, household movement traces, and law-enforcement actions is uncommon. Liability pressure discourages strong claims, which is visible in WUI-NITY/PREACT disclaimers. The work also has a high preprocessing tax because fuels, weather, topography, roads, zones, and demand assumptions must be harmonized. These are partly opportunity signals because they favor integration-focused work, but they are also warnings because they imply the benchmark may stall on missing ground truth rather than on missing algorithms.

### Feasibility and evidence

#### Repeated Unresolved Limitations

Across the inspected literature and tooling, the same limitations recur: wildfire evacuation traffic models are calibration-poor; route capacity under fire and smoke is not the same as routine capacity; household departure timing is hard to observe; closure timing and law-enforcement control actions are often incomplete in public data; and coupled tools carry disclaimers against direct operational substitution. The Kincade, Glass, and Silverado papers all reinforce that emergency traffic changes the speed-flow-density relationship and that generic routine assumptions are not enough. Tool-side limitations repeat as well: WUI-specific couplers are broad but heavy, traffic frameworks need scenario-specific demand engineering, and fire models require expensive raster harmonization.

#### Excluded Populations Geographies And Failures

Current public work and the proposed first loop both under-cover non-drivers, institutional populations, medically fragile residents, households with trailers or large animals, evacuees without phone/power connectivity, tourists, and people who refuse or delay evacuation. Geographically, a Paradise-Magalia first loop will not immediately generalize to coastal canyon systems, dense freeway-dependent suburbs, or places with formal contra-flow plans. Operational failures likely to remain weakly modeled include ad hoc temporary refuge area creation, firefighter-directed reverse movements, communications outages, smoke-only visibility degradation without direct flame contact, and intersection-management improvisation by officers on the ground.

#### Why Now

Tractability is better now than it was even a few years ago. Since 2021, NIST has published detailed Camp Fire progression and life-safety reconstructions plus a public supporting dataset. Butte County now has post-Camp-Fire community evacuation maps and zone infrastructure shaped by 2021 to 2022 planning work. SUMO remains actively released and mature, with official 1.27.1 downloads visible on August 9, 2026. MATSim has a 2026.0 stable release. ELMFIRE has a modern public documentation site and versioned releases. PyTorchFire and FireDataForge indicate that wildfire data retrieval and rapid calibration are improving. The empirical traffic literature also advanced after Camp Fire, giving public Kincade, Glass, and Silverado findings that can bound evacuation traffic assumptions rather than relying entirely on hurricane-era or generic HCM relationships.

#### Hidden Dependencies And Penalties

The main hidden dependency is not raw code but missing operational truth. A benchmark can be built without private data, but credible policy claims depend heavily on zone definitions, departure timing assumptions, road-control actions, and special-population demand that are only partly public. There is also a licensing/redistribution penalty: OSM's ODbL is manageable but imposes share-alike obligations on adapted databases, and county evacuation-zone redistribution terms were not confirmed. A preprocessing penalty is substantial because fire, weather, road, and demographic layers arrive in different resolutions, coordinate systems, and update cadences. A translation penalty is also high: even a good benchmark may change academic understanding faster than county practice unless its outputs fit planning workflows.

### Experiment and decision

#### Falsifiable Hypothesis

Using only public data, a coupled ELMFIRE plus SUMO benchmark can reproduce the broad first-3-hour Camp Fire clearance and blockage chronology well enough to rank staged evacuation-zone policies more credibly than a traffic-only routine-capacity baseline. A concrete falsifiable version is: at least one staged-zone policy will reduce exposed vehicle-minutes by 15% or more relative to a simultaneous-release baseline while keeping total modeled clearance time within 10% of the best simultaneous-release case under the same demand assumptions.

#### Strongest Baselines

Baseline 1: traffic-only SUMO/libsumo with all-at-once zone release and routine-capacity assumptions. Baseline 2: traffic-only SUMO/libsumo with wildfire-adjusted speed/capacity curves taken from the Kincade, Glass, and Silverado literature but without dynamic fire closures. Baseline 3: ELMFIRE plus SUMO simultaneous-release coupling with no staged policy optimization. Baseline 4: a Cell2Fire plus SUMO variant for cheaper fire-side scenario sweeps. Baseline 5: if time permits, a WUI-NITY/PREACT-style conceptual comparison or a MATSim staged-evacuation replication on a reduced network to test whether the chosen stack is missing a material behavioral effect.

#### Experiment Protocol

Primary scenario: replay November 8, 2018 for Paradise and Magalia over the first 180 minutes after ignition. Inputs: NIST TN 2135 fire observations, NIST TN 2252 NETTRA observations, Butte County evacuation zones/maps, OSM road graph, Paradise/Magalia demographic aggregates, FRAP perimeters/FHSZ context, and public weather/fuel layers required by the chosen fire engine. Step 1 validates geometry and timestamps: all source layers aligned to one spatial reference and one minute-based simulation clock. Step 2 validates the traffic side alone using public wildfire traffic literature ranges: the implemented speed-flow-density relationships should be able to express Kincade-like, Glass-like, and Silverado-like reductions. Step 3 replays Camp Fire with dynamic closures and zone releases to check whether major observed route failures, standstills, and temporary refuge area pressures occur in roughly the right time order. Step 4 compares a small policy set: simultaneous evacuation, current-zone-order proxy, north-to-south staging, and risk-triggered staging. Use at least 20 stochastic seeds per policy for demand jitter and departure-time uncertainty. Publish artifacts as versioned configs, preprocessing scripts, derived network files, event logs, and evaluation notebooks.

#### Twelve Month Proof Target

If the first gate passes, a credible 12-month target is a public 'Firescape Paradise Benchmark v1' plus a methods paper or technical report showing: open preprocessing from public sources, validated fire-traffic coupling on Camp Fire, cross-case traffic sanity checks using Kincade/Glass/Silverado, and at least one planner-relevant finding about staged releases, route vulnerability, or temporary refuge dependence. A stronger translation target would add one or two additional California case-study geographies and a simple scenario explorer for emergency-planning workshops.

#### Actors And Translation Path

Potential adopters are county emergency managers, CAL FIRE unit planners, evacuation consultants, Fire Safe Councils, transportation researchers, and resilience nonprofits. The insertion point is pre-season planning and exercise design, not live incident command. Useful outputs are zone-release comparisons, bottleneck maps, road segments whose failure dominates clearance time, uncertainty intervals on clearance under different demand assumptions, and candidate temporary-refuge-area stress points.

#### Strongest Rejection Argument

The best rejection case is that the benchmark will be precise-looking but behaviorally underdetermined. If household departures, informal communications, officer control, and ad hoc refuge behavior drive outcomes more than solver choice does, then a public-data coupled model may mostly tell a tidy story about an untidy event and offer little trustworthy decision leverage. In that case, the work could become an integration exercise with weak practical translation.

#### Sources

- title: A Case Study of the Camp Fire - Notification, Evacuation, Traffic, and Temporary Refuge Areas (NETTRA) | url: https://www.nist.gov/publications/case-study-camp-fire-notification-evacuation-traffic-and-temporary-refuge-areas-nettra | date: 2023-08-08 | source type: official report landing page | claim supported: Camp Fire life-safety ground truth, more than 2,600 NETTRA observations, 31 temporary refuge areas, 198 rescue events.
- title: A Case Study of the Camp Fire - Fire Progression Timeline | url: https://www.nist.gov/publications/case-study-camp-fire-fire-progression-timeline | date: 2021-01-01 | source type: official report landing page | claim supported: Camp Fire progression reconstruction, high winds, long-range spotting, and Paradise/Magalia impact chronology.
- title: Data supporting the case study of the 2018 Camp Fire | url: https://catalog.data.gov/dataset/data-supporting-the-case-study-of-the-2018-camp-fire | date: 2024-03-04 | source type: government dataset catalog | claim supported: Public supporting dataset, more than 2,200 geolocated fire observations, public spreadsheet download.
- title: Fire Perimeters | CAL FIRE FRAP | url: https://www.fire.ca.gov/what-we-do/fire-resource-assessment-program/fire-perimeters | date: accessed 2026-08-09 | source type: official data program page | claim supported: Historical California fire perimeters are publicly distributed and released annually in April.
- title: Fire Hazard Severity Zones | OSFM | url: https://osfm.fire.ca.gov/what-we-do/community-wildfire-preparedness-and-mitigation/fire-hazard-severity-zones | date: accessed 2026-08-09 | source type: official hazard data page | claim supported: FHSZ is hazard rather than risk, with factors including fuels, terrain, flame length, embers, and weather.
- title: Fire Hazard Severity Zone Viewer - Dataset - California Open Data | url: https://data.ca.gov/dataset/fire-hazard-severity-zone-viewer1 | date: accessed 2026-08-09 | source type: state open-data catalog | claim supported: Current viewer references SRA data effective April 1, 2024 and LRA recommendations dated March 24, 2025.
- title: Community Evacuation Maps | Butte County, CA | url: https://www.buttecounty.net/795/Community-Evacuation-Maps | date: accessed 2026-08-09 | source type: county emergency-preparedness page | claim supported: Butte County received a 2021 grant and used 2022 traffic-flow modeling to produce community evacuation maps.
- title: Know Your Zone | Butte County, CA | url: https://www.buttecounty.net/1498/Know-Your-Zone | date: accessed 2026-08-09 | source type: county live map page | claim supported: Public evacuation zone map exists for Butte County and is part of current resident-facing planning.
- title: U.S. Census Bureau QuickFacts: Paradise town, California | url: https://www.census.gov/quickfacts/fact/table/paradisetowncalifornia/HCN010222 | date: accessed 2026-08-09 | source type: official demographic dataset page | claim supported: Paradise population and age structure for demand context.
- title: Performance Measurement System (PeMS) Data Source - Caltrans | url: https://dot.ca.gov/programs/traffic-operations/mpr/pems-source | date: accessed 2026-08-09 | source type: official traffic-data page | claim supported: PeMS is a public archived and real-time California freeway traffic source used for wildfire traffic studies.
- title: ELMFIRE documentation | url: https://elmfire.io/ | date: 2025.0212 docs accessed 2026-08-09 | source type: official software documentation | claim supported: ELMFIRE license, use cases, installation path, and real-world fuel/terrain tutorials.
- title: Software and Data - Berkeley Fire Research Lab | url: https://firelab.berkeley.edu/software/ | date: accessed 2026-08-09 | source type: lab software page | claim supported: ELMFIRE operational context and Berkeley Wildland-Urban Extension maintenance.
- title: Cell2Fire GitHub repository | url: https://github.com/cell2fire/Cell2Fire | date: accessed 2026-08-09 | source type: official code repository | claim supported: GPL-3.0 license, research-only disclaimer, parallel computation, and pointer to more actively maintained C2FK fork.
- title: ForeFire GitHub repository | url: https://github.com/forefireAPI/forefire | date: accessed 2026-08-09 | source type: official code repository | claim supported: GPL-3.0 license, MPI support, Python bindings, NetCDF handling, Docker and HTTP interfaces.
- title: PyTorchFire GitHub repository | url: https://github.com/xiazeyu/PyTorchFire | date: accessed 2026-08-09 | source type: official code repository | claim supported: pip-installable wildfire simulator with notebook examples and optional FireDataForge integration.
- title: PyTorchFire: A GPU-Accelerated Wildfire Simulator with Differentiable Cellular Automata | url: https://arxiv.org/abs/2502.18738 | date: 2025-02-26 | source type: academic preprint | claim supported: PyTorchFire speed, differentiable calibration, and role as a newer GPU-first wildfire engine.
- title: FireDataForge: A Unified Framework for Multi-Source Wildfire Data Retrieval and Integration | url: https://arxiv.org/abs/2606.21198 | date: 2026-06-19 | source type: academic preprint | claim supported: Automated harmonization of 11 wildfire-related data sources and reduction of preprocessing burden.
- title: PREACT/WUI-NITY GitHub repository | url: https://github.com/bran-jnw/wuinity | date: accessed 2026-08-09 | source type: official code repository | claim supported: GPL-3.0 licensing, wildfire-pedestrian-traffic coupling, PREACT core split, and Unity legacy.
- title: The simulation of wildland-urban interface fire evacuation: the WUI-NITY platform | url: https://nrc-publications.canada.ca/eng/view/object/?id=2a4d9ef8-0f7d-4d60-9586-aae5385a47dd | date: 2021-01-01 | source type: academic/government publication record | claim supported: WUI-NITY architecture based on wildfire, pedestrian, and traffic layers and its FARSITE/LWR basis.
- title: SUMO Documentation | url: https://sumo.dlr.de/docs/index.html | date: accessed 2026-08-09 | source type: official software documentation | claim supported: SUMO license, intermodal support, scenario-creation tools, and mature documentation.
- title: Eclipse SUMO home page | url: https://eclipse.dev/sumo/ | date: accessed 2026-08-09 | source type: official software home page | claim supported: Current visible official SUMO release 1.27.1, OSM import, TraCI APIs, and project maturity.
- title: MATSim home page | url: https://matsim.org/ | date: accessed 2026-08-09 | source type: official software home page | claim supported: MATSim scope as an open-source large-scale agent-based transport simulation framework.
- title: Install MATSim | url: https://matsim.org/install/ | date: accessed 2026-08-09 | source type: official install documentation | claim supported: Stable release 2026.0, Java/Maven setup burden, and suitability as a framework rather than turnkey tool.
- title: Simulation Pipeline for Traffic Evacuation in Urban Areas and Emergency Traffic Management Policy Improvements through Case Studies | url: https://arxiv.org/abs/2002.06198 | date: 2020-02-14 | source type: academic preprint | claim supported: Prior Paradise case-study pipeline and closest open traffic-focused attempt.
- title: Traffic dynamics during the 2019 Kincade wildfire evacuation | url: https://trid.trb.org/View/2107381 | date: 2023-03-01 | source type: abstract/index record | claim supported: 69,116 data points from 24 locations, roughly 3.5 km/h lower speeds, and need for wildfire-specific traffic models.
- title: The analysis of traffic data of wildfire evacuation: the case study of the 2020 Glass Fire | url: https://www.nwfirescience.org/sites/default/files/publications/1-s2.0-S0379711223001777-main.pdf | date: 2023-01-01 | source type: academic PDF | claim supported: Glass Fire speed and capacity reductions and relationship to Kincade findings.
- title: Traffic Performance Indicators for Evacuation: The Case Study of the 2020 Silverado Wildfire | url: https://link.springer.com/article/10.1007/s10694-025-01813-y | date: 2025-01-01 | source type: academic article page | claim supported: Silverado evacuation of nearly 100,000 people and larger freeway capacity reduction during evacuation.
- title: 2019 Kincade Fire After Action Report - Sonoma County | url: https://sonomacounty.gov/Main%20County%20Site/Administrative%20Support%20%26%20Fiscal%20Services/Emergency%20Management/Documents/Archive/Administration/Services/Training__3/Service%201/_Documents/Sonoma-County-2019-Kincade-Fire-AAR-FINAL-ADA.pdf | date: 2020-01-01 | source type: county after-action report | claim supported: Peak evacuation scale for the Kincade Fire.
