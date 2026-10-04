# Renaissance Work Ledger

**Purpose:** A small working bookmark for continuing human/AI work.

This file is a navigation aid, not canon, architecture, a roadmap, a changelog,
or a replacement for Git history. Canonical authority remains in the
constitutional documents and recorded Decisions.

## Current Frontier

**Status:** Attention Choice contract ratified; implementation boundary is next.

### Last verified stopping point

The Learn 001A experiment and delayed-retention follow-up are complete:

- Initial execution recorded baseline, instruction, immediate performance, transfer, and reflection.
- Delayed retest used a new directory layout with no hints or re-teaching.
- All four path-resolution questions were answered correctly, providing bounded evidence of delayed retention and transfer.
- **Commit:** `e1926b106e8c07b80b9a9baf67fa2dd24fe5f24b9`
- No implementation of Learn was introduced.

### Cross-repository catch-up finding

A world-level review found that Praxis and Episteme completed their first explicit evidence handoff boundary on 2026-10-03.

- Praxis records the problem/intervention/test/result domain semantics.
- Praxis explicitly admits evidence through a human decision boundary.
- Episteme has a canonical Praxis handoff adapter that preserves the supplied Praxis evidence and admission objects, assigns an Episteme-owned identity, and preserves provenance without making Praxis a runtime dependency.
- Praxis commits: `7baa1db6`, `1aca6554`, `873c54e8`, `740ff5bf`, `e3bb5b8b`
- Episteme commits: `ce3d5464`, `a0c3a347`, `72cd2555`, `0ea499c1`, `8f88274f`

The Renaissance-facing relationship was checked against `ARCHITECTURE.md` and `CONSTELLATION_AUDIT.md`.

**Result:** this is documentation synchronization, not a missing Renaissance architecture boundary.

The smallest justified change was made in `CONSTELLATION_AUDIT.md`:

- Praxis is recorded as a supporting/satellite project.
- The concrete Praxis→Episteme handoff is recorded as an existing constellation relationship.
- No Renaissance runtime interface, dependency, or ownership was introduced.
- The audit now explicitly records that the existing Renaissance interoperability and authority rules are sufficient for this relationship.

**Commit:** `c3ff5d0b1fb32788b36094c853f8b55e00cc91bf`

### Human-facing interaction discovery

Recent role-play established that Renaissance should not require the human to classify a request into a capability or workflow before receiving useful help.

Examples tested:

- curiosity that could become a small self-run experiment (color and mood);
- a request for a way into an unfamiliar subject (systems);
- conceptual exploration with boundary-checking ("anti-magnets");
- observations and meaning-bearing thoughts ("the stars are beautiful", a poetic thought about God);
- causal curiosity about a person and history (Van Gogh).

The important finding is broader than question answering: a human-facing Renaissance must be able to recognize the kind of moment it is in and respond proportionately. Sometimes that means investigation, sometimes learning, sometimes conceptual exploration, and sometimes simply participating in a human moment without turning it into a task.

### Knowledge-growth hypothesis

The latest discussion points toward a stronger hypothesis:

> Renaissance may be most useful as a system for reasoning over, accumulating, connecting, testing, and expanding knowledge, with the human participating rather than manually driving every step.

A possible long-running cycle is:

`curiosity → exploration → reasoning → evidence/experiment → knowledge → memory → connections → new questions`

A further possibility is that the system can generate some of its own next questions and investigations rather than waiting for the human to supply every step.

This is **not yet an architecture decision** and does not justify a new repository or subsystem by itself.

The investigation that followed established that the missing pressure is **attention**, not another epistemic-memory object.

### Attention Choice investigation

The grounded investigation established:

- Episteme already preserves findings, hypotheses, predictions, experiments, results, evaluations, workflow lineage, acquisition lineage, and provenance.
- The missing seam is the transition:
  `represented pressure → choice of what to attend to → declared work`
- Renaissance has no existing request/intent/selection contract that owns this seam.
- A universal importance score or global ranking mechanism is neither present nor justified.
- The smallest useful semantic unit is an **Attention Choice**: a declared decision to give an identified matter attention.
- The choice belongs above Episteme's scientific execution machinery.
- Episteme remains responsible for the investigation it receives and its scientific provenance.

The proposed contract was created at:

`PROPOSALS/ATTENTION_CHOICE_CONTRACT.md`

It remains explicitly **Proposed — not canon**.

### Attention Choice record validation

The proposed referential record was tested against seven knowledge-growth cases.

The record shape is:

```
AttentionChoice
  id
  pressure_ref
  target_ref
  supporting_refs[]
  selection_basis
  alternative_refs[]
  mode
  authorization_ref?
  outcome_ref?
```

The tests established:

- human curiosity can supply pressure directly;
- an Episteme gap can motivate a suggestion without making Episteme the agenda setter;
- multiple candidates can be handled without universal ranking;
- unrelated novelty does not justify investigation;
- rejection remains a valid outcome;
- investigation results remain separate from the original choice;
- a choice does not become permission merely because execution follows.

The authorization test exposed and resolved one real provenance seam: when execution requires separate authorization, the choice must preserve a reference to that established authorization without becoming an authority object itself.

Validation records:

- `experiments/ATTENTION_CHOICE_MVT.md`
- `experiments/ATTENTION_CHOICE_RECORD_MVT.md`
- `experiments/ATTENTION_CHOICE_AUTHORIZATION_MVT.md`

Latest validation commit:

**`3b040d21150e24ca864034983b26bdd6c72409d2`**

### Decision boundary — resolved

Decision 0009 ratified the Attention Choice contract as a Renaissance architectural boundary.

- Decision: `DECISIONS/0009-establish-attention-choice-boundary.md`
- The proposal is accepted as the contract source; implementation details remain unresolved.
- `ARCHITECTURE.md` is synchronized.
- The contract does not authorize a storage format, runtime organ, universal ranking engine, autonomous agenda subsystem, or Episteme redesign.
- Authorization remains distinct from attention choice.

### Implementation-boundary investigation

The first implementation inspection is complete across Renaissance, Episteme, and the existing Organs runtime substrate.

**Finding:** there is no existing Renaissance-side Attention Choice persistence or request/selection object to reuse directly.

- Renaissance currently defines capability contracts and architecture, but has no runtime persistence layer for this semantic object.
- Episteme has mature durable SQLite persistence, workflow definitions/executions, provenance, and lineage, but its grounded `Record` model is explicitly epistemic and its record kinds are source/observation/measurement/dataset/experiment/result. Attention Choice does not belong there without distorting Episteme's responsibility.
- Episteme workflow execution preserves what ran and how; it should not be made responsible for the prior Renaissance choice that selected the work.
- Organs Communications already provides a durable SQLite event history with topic, event type, publisher, payload, independent consumer cursors, replay/debug inspection, and no requirement that the publisher's semantic object become an Organs-owned epistemic artifact.
- Organs Memory also has durable ledgers and structured state, but its model is specifically memory/facts/scars/promises/relations and is not an appropriate owner for Attention Choice semantics.

Therefore the smallest currently justified implementation boundary appears to be **an Attention Choice event carried through the existing Communications persistence mechanism**, while Renaissance retains ownership of the semantic contract. This is an integration hypothesis, not yet an implementation decision.

### Communications transport boundary test

The existing Communications core was checked directly.

**Result: PASS as a transport/persistence mechanism; no Communications code change is justified.**

Its event contract already provides exactly the structural envelope required by the Attention Choice record:

- durable SQLite event row;
- timestamp;
- topic;
- event type;
- publisher;
- arbitrary JSON payload;
- topic-indexed inspection;
- independent consumer cursors;
- replay/reset for inspection and recovery.

The Attention Choice minimum record can therefore live unchanged inside the payload. Its semantic fields remain Renaissance-owned; Communications does not need to understand or interpret them.

The important boundary is:

`Renaissance Attention Choice record → Communications event envelope → consumer`

This preserves the distinction between **transport/storage** and **semantic ownership**. It also avoids duplicating persistence in Renaissance or turning Organs into an Attention subsystem.

One limitation remains: Communications provides durable event transport, not a domain-level Attention Choice registry or query contract. That is acceptable for the current decision because no consumer/query requirement has yet been demonstrated. A domain-specific registry should only be added if a concrete use case requires lookup, lifecycle management, or validation beyond event replay/inspection.

**Implementation conclusion:** the existing Communications mechanism is sufficient for the first durable representation. No new persistence subsystem and no Communications semantic extension are currently justified.

The next grounded step is to define the smallest Renaissance-facing event contract needed to publish an Attention Choice, then test it end-to-end without inventing a registry or autonomous consumer.\n\n### Publisher boundary inspection\n\nTargeted inspection found no existing Renaissance-side HTTP client, Communications integration wrapper, or Attention publisher. Organs' established cross-organ convention is registry discovery followed by direct HTTP calls; Communications exposes a generic publish endpoint accepting `event_type`, `payload`, and `publisher` under a caller-selected topic.\n\n**Finding:** there is currently no justified existing Renaissance publisher to reuse. Creating a generic Communications client merely for Attention Choice would be premature infrastructure. The smallest next artifact is therefore the Renaissance-facing event contract itself, not runtime code.

Do **not** turn Communications into an Attention organ, move Attention Choice semantics into Organs, or modify Episteme merely to gain storage.

## Last Known Organs Boundary

Organs has a real Communications BUS carrying Memory events, but current
Renaissance requirements do not establish a consumer for those topics.

Archaeology confirmed that this is an available integration seam, not a missing
component or current architectural defect. No subscriber, organ, protocol, or
Decision is required at this time.

If a concrete capability later requires one of these events, establish the
responsible contract at that time before implementing the consumer.

## Ledger Rule

Keep this document small.

Move the pointer rather than turning this into a diary. The useful question is:

> **Where were we, and what was the next grounded place to look?**

Git is the long-term record. The ledger is the bookmark. Conversation is the
scratchpad.


### Attention Choice event contract

The smallest Renaissance-facing integration contract is now defined in `PROPOSALS/ATTENTION_CHOICE_EVENT_CONTRACT.md`.

It fixes the transport vocabulary for the first implementation boundary:

- topic: `renaissance.attention`
- event type: `attention_choice`
- publisher: `renaissance`
- payload: the accepted Attention Choice record, unchanged

The contract explicitly keeps Communications as transport/persistence infrastructure. It does not create an Attention registry, agenda, queue, ranking engine, new database, Episteme record type, or permission mechanism.

The next step is the smallest implementation/test of a Renaissance-side publisher using the existing Organs discovery convention.

### Publisher implementation boundary check

The proposed first publisher was checked against the current Renaissance repository.

**Finding:** Renaissance currently has no established runtime/package/test surface for a Communications publisher. There is no existing Renaissance HTTP client, service entrypoint, Python package, or test harness to extend.

Therefore implementing a publisher now would require inventing a runtime location and lifecycle that the architecture has deliberately left unresolved. That would be more architecture than the current evidence justifies.

The event contract is complete enough to guide a future publisher, but the correct next step is **not** to manufacture a runtime. A real Renaissance runtime/use case must establish the hosting boundary first. The existing Organs discovery convention remains the intended integration mechanism once that boundary exists.

**Result:** implementation deferred for lack of an existing justified runtime boundary. No code was added.

### Human-facing runtime boundary investigation

The Organs I/O Interface was inspected as the existing human-facing runtime front door. It accepts natural-language requests, maps them through a fixed intent catalog, routes recognized actions through Critic, and sends consequential actions through Executive approval. This establishes that Renaissance does not need to invent a second front door merely to host human-facing interaction.

**Boundary finding:** the I/O Interface is operational routing infrastructure, not a Renaissance capability interpreter. Its current catalog describes concrete Organs operations (memory, introspection, reflection, orchestration, sandbox), and it deliberately refuses to infer arbitrary new actions. Therefore it should not silently become the owner of Renaissance semantics.

The next architectural seam is the translation boundary between a human-facing request and a Renaissance capability request:

`human expression → Renaissance interpretation/capability boundary → appropriate instrument or Organs operation`

The investigation should determine whether an existing Renaissance contract already owns this translation, and if not, what smallest contract is justified. No new runtime component or I/O catalog entry is justified by this finding alone.

**Result:** Organs provides the front door; Renaissance still lacks an explicit capability-request boundary. The next step is contract inspection, not implementation.


### Capability Request boundary proposal

A minimal Renaissance-owned Capability Request contract was proposed and validated against seven human-facing cases.

The proposed record preserves the original expression while representing capability, intent, target/context, constraints, interaction mode, authorization provenance when applicable, and outcome reference. It keeps Capability Request distinct from Attention Choice, authorization, Episteme epistemic artifacts, execution, and universal ranking.

Validation covered ordinary learning, scientific curiosity, explicit investigation, creation, human expression that should not be converted into a task, ambiguity requiring clarification, and consequential operational requests. All cases passed the boundary checks.

Artifacts:
- `PROPOSALS/CAPABILITY_REQUEST_CONTRACT.md`
- `experiments/CAPABILITY_REQUEST_MVT.md`

**Result:** the semantic seam is sufficiently small to test further. It remains proposed, not canon. No runtime or persistence implementation was introduced.

**Next:** test the proposed contract against the real Organs I/O boundary and existing Renaissance/Episteme/Praxis interaction patterns before deciding whether any durable request record or adapter is actually needed.


### Capability Request real-boundary validation

The proposed Capability Request contract was tested against the actual Organs I/O Interface and the established Praxis/Episteme boundaries.

**Result: PASS with one integration finding.**

- Organs I/O correctly remains deterministic operational routing with Critic/Executive safety gates.
- Ordinary conversation need not become a Capability Request.
- Renaissance learning/investigation requests fit the proposed semantic boundary without becoming authorization or evidence.
- Praxis retains its domain semantics.
- Episteme retains scientific execution and provenance.
- Unrecognized Renaissance requests fail closed rather than being guessed into API calls.

The important finding is that the Capability Request boundary belongs above or alongside the existing Organs operational catalog, not inside it.

There is still no justified Renaissance runtime/adapter surface for this contract. No runtime, I/O catalog expansion, persistence layer, or new front door should be invented yet.

Experiment: `experiments/CAPABILITY_REQUEST_REAL_BOUNDARY_MVT.md`

**Next grounded question:** what existing Renaissance-facing interaction surface, if any, can host Capability Request interpretation without creating a second front door? If none exists, establish that absence before implementation.


### Capability boundary cleanup

Targeted inspection of the current human-facing capability model found one stale architectural reference to retired Akasha implementation material under Explore.

Because Akasha is retired historical archaeology, it should not remain presented as current Renaissance implementation evidence or as a source for future rebirth.

The Explore section was reduced to the established current truth: no current Renaissance Explore implementation is established; future implementation must be justified and tested against the Explore contract rather than inherited from retired archaeology.

**Result:** current public capability documentation now respects the retired-project boundary.


### Renaissance-facing interaction surface investigation

The remaining Capability Request question was resolved by inspecting the actual interaction surfaces.

**Finding: no existing Renaissance-facing semantic host currently exists.**

Organs does provide a real human-facing surface:

- `tui/organs_tui.py` has an **Input** tab.
- The Input tab sends human text to Organs' `/io/handle` front door, or `/io/interpret` for dry-run.
- Organs' I/O Interface deliberately performs deterministic matching against a fixed operational catalog.
- Unknown requests fail closed rather than being interpreted into arbitrary API calls.

That surface is therefore a valid **operational front door**, but it is not a Renaissance Capability Request interpreter and should not be turned into one merely for convenience.

Renaissance itself currently has no runtime/service/package surface capable of hosting Capability Request interpretation. The repository remains architectural/documentary rather than an executable front door.

This resolves the prior open question:

> **No existing Renaissance-facing interaction surface is currently available.**

The absence is now established rather than guessed. The next step, if warranted, is to determine the smallest contract for a Renaissance semantic interaction surface without creating a second operational front door or moving Renaissance semantics into Organs.

No implementation was created from this finding.


### Investigation result — Renaissance semantic interaction boundary

The concrete front-door inspection establishes four candidate placements. Organs I/O directly owning Renaissance capability semantics would violate its established operational-routing boundary. The Organs TUI is presentation/consumer infrastructure and must not become a second semantic front door. Creating a new Renaissance operational front door would duplicate existing topology without a demonstrated runtime need.

The smallest justified shape is therefore a **Renaissance-owned semantic boundary behind the existing human-facing front door**. It receives a human expression only when Renaissance capability work is actually present, produces a Capability Request under the accepted contract, and hands the request to the appropriate capability or instrument. Ordinary conversation remains possible without manufacturing a request.

Conceptually:

`human expression → existing front door → Renaissance semantic boundary → Capability Request → capability/instrument`

For investigation:

`Capability Request → Attention Choice → authorization when required → Episteme`

**Result: PASS conceptually; implementation location unresolved.** No new runtime, API, persistence layer, Organs capability, or second front door is justified yet. The next concrete evidence needed is a real Renaissance capability invocation need that establishes where this semantic boundary must live.


### Investigation result — first real Capability Request workflow evidence

Learn Experiment 001A (Linux paths) has an actual conversational execution record dated 2026-09-30. It provides the first concrete Renaissance capability workflow against which the Capability Request boundary can be tested.

The workflow can be represented as a Capability Request for `learn` without creating an Attention Choice, authorization, new front door, or epistemic artifact. The execution record remains the record of the learning interaction and its evidence; the Capability Request remains the semantic interpretation of the originating human expression.

**Result: PASS.** The Capability Request contract is now grounded by a real Renaissance capability workflow rather than conceptual tests alone.

The remaining implementation question is narrower: where should the Renaissance-owned semantic boundary live when this kind of capability interaction becomes operational beyond conversational execution?


### Implementation-boundary finding — Learn already has a real vertical slice

The repository already contains `experiments/learn_model.py` and `experiments/test_learn_model.py`, with CI configured to execute the Learn vertical tests. The model implements the minimum learning-process boundary: goal, capability target, baseline, activity, performance, feedback, adaptation, transfer, and bounded capability evidence. It explicitly refuses capability evidence without transfer and preserves unresolved outcomes.

This changes the Capability Request implementation question: there is now a concrete Renaissance-owned capability implementation surface to exercise without inventing a runtime or new repository. The semantic request boundary can be tested against this existing vertical slice first.

The smallest next step is therefore **not** a new service or adapter. It is a machine-checkable boundary test showing that a real Capability Request can hand off to the existing Learn vertical slice while keeping request interpretation, learning execution, and capability evidence distinct.


### Boundary test added — Capability Request → Learn vertical

Added `experiments/test_capability_request_learn_boundary.py`. The test exercises a concrete Capability Request handoff into the existing Learn vertical slice and asserts three distinct layers: request interpretation, learning execution, and bounded capability evidence. It also asserts that the request does not manufacture authorization, truth, permission, or evidence fields.

The existing Learn CI workflow now runs this boundary test alongside the Learn vertical tests on push and pull request paths.

The repository's workflow-run lookup did not report a run for the resulting commits, so CI execution is **not claimed as verified here**. The code-level boundary is present; runtime verification remains the next check if Actions reports a run.


### CI verification — Capability Request → Learn boundary

GitHub Actions executed the updated Learn workflow on commit `be699a4924aa271faf245869ed3b6af72973bff3`. The `learn-vertical` job completed successfully, including the new `test_capability_request_learn_boundary.py` test.

**Result: PASS in CI.** The Capability Request boundary is now both represented in code and verified by the repository's existing automated Learn workflow.


### Public-reference hygiene sweep

A targeted search found stale retired/private project references in two Renaissance capability contracts: Explore referenced historical Akasha work, and Episteme named Behemoth, Leviathan, and Namagiri. These references conflicted with the current world rule that retired/private projects are not current Renaissance architecture or public navigation material.

Removed both references without changing the capability semantics. A follow-up repository search found no remaining occurrences of `Akasha`, `Behemoth`, `Leviathan`, or `Namagiri` in Renaissance.


### Investigation result — Capability Request composes with real Episteme workflow

The second real capability boundary was tested against Episteme's existing Phase 12 finite discovery workflow. A Renaissance `understand / investigate` Capability Request can precede the established Attention Choice boundary, after which Episteme receives a declared workflow and retains ownership of scientific execution, provenance, results, and knowledge-state change.

**Result: PASS.** The Learn boundary was not a special case. The semantic separation remains intact across two distinct capabilities:

`Capability Request ≠ Attention Choice ≠ Episteme workflow ≠ Episteme result/evidence`

This remains a real-boundary validation rather than a live cross-repository runtime invocation. No adapter, API, persistence layer, or new runtime is justified yet.

The remaining question is now whether there is a genuine user-facing runtime need that requires making this already-proven composition executable across repository boundaries.


### Boundary maturity check — no runtime need demonstrated

After validating the Capability Request boundary against both the existing Learn vertical and an existing Episteme investigation workflow, there is still no concrete user-facing runtime invocation that requires cross-repository execution. Existing Organs front-door routing remains operationally sufficient; Renaissance semantic interpretation can remain a contract until a real invocation demands executable composition.

**Result: stop at the boundary.** Further runtime construction would currently be architecture manufactured ahead of need.


### Human Doorway MVT — semantic boundary validated

The Human Doorway MVT was executed against the existing Renaissance contracts and real Learn, Episteme, Praxis, and Organs boundaries.

Seven cases passed:

- ordinary conversation remains conversation;
- clear learning requests can enter Learn without manufacturing Attention Choice or authorization;
- investigative questions compose through Capability Request → Attention Choice → authorization when required → Episteme;
- problem-solving requests preserve Praxis domain ownership;
- ambiguity produces clarification rather than invented capability/action;
- operational requests remain on the Organs I/O path;
- unsupported requests fail closed rather than manufacturing architecture.

**Result: PASS at the semantic boundary.**

The test does not justify an executable doorway, new runtime, universal classifier, second front door, autonomous agenda, ranking system, or persistence layer.

Artifact: `experiments/HUMAN_DOORWAY_MVT_RESULT.md`

The semantic problem is now substantially solved. The remaining question is practical:

> **What actual human interaction is valuable enough to justify making this doorway executable?**



### Human Doorway runtime boundary — Decision 0010

The Human Doorway semantic boundary and runtime placement were validated against the actual Renaissance and Organs surfaces.

Decision 0010 establishes the executable boundary:

`human → Organs I/O → Renaissance semantic runtime → conversation / clarification / Capability Request`

Organs remains the human-facing transport/front door and operational authority. Renaissance owns semantic interpretation of non-operational human expressions. The Renaissance runtime may use the existing Organs registry/discovery and service convention without transferring semantic ownership to Organs.

Communications was inspected and remains transport infrastructure, not semantic owner.

**Result:** Human Doorway runtime boundary ratified by Human Gate. The next implementation must be the smallest Renaissance service/adapter surface that can pass the existing Human Doorway harness against the real Organs transport. No autonomous agenda, ranking engine, new persistence, second front door, or automatic cross-repository execution is authorized by this decision.

Artifacts:
- `DECISIONS/0010-establish-human-doorway-runtime-boundary.md`
- `experiments/HUMAN_DOORWAY_RUNTIME_PLACEMENT_MVT.md`
- `PROPOSALS/HUMAN_DOORWAY_RUNTIME_BOUNDARY.md`



### Human Doorway runtime — first executable slice

Decision 0010 is now exercised by a real Renaissance service surface at `runtime/human_doorway/`.

The service exposes:

- `GET /health`
- `GET /info`
- `POST /renaissance/doorway`

The first implementation is deliberately conservative and deterministic. It accepts preserved human expression and returns only:

`conversation | clarify | capability_request | operational | unsupported`

with capability/mode when a Renaissance Capability Request is warranted.

It does not authorize, execute, create evidence, create Attention Choice, persist a request, or route work across repositories.

The service participates in the existing Organs registry convention by registering as `renaissance` when a Registry is available. Registry failure is non-fatal and does not cause the service to invent authority.

Executable tests cover the existing Human Doorway corpus, exact expression preservation, HTTP transport, and fail-closed ambiguity.

CI was extended to run the runtime tests. The first workflow result is not yet available for verification at the time of this ledger update.

**Next:** verify the new CI run. If green, exercise the doorway against the real Organs transport rather than expanding the service.


### Human Doorway — real Organs transport integration verified

The Renaissance doorway was exercised through the actual Organs I/O HTTP interface with the Registry and both services running in the integration workflow.

Verified cases:
- Registry discovery found the Renaissance service.
- Direct Renaissance doorway request succeeded.
- Organs I/O forwarded non-operational human expression to Renaissance with the expression preserved.
- Existing operational catalog routing retained precedence and remained Organs-owned.
- Ambiguous expression returned clarification through the real transport with `action_taken: false`.
- No semantic handoff authorized or executed an operation.

The Organs integration workflow completed successfully on commit `8284c471ee7bd33c7912cddfd2e25321c0763b6d`; all transport job steps passed. The Organs test workflow on the same commit also completed successfully.

**Result: PASS — the Decision 0010 boundary is now demonstrated across the real service boundary, not merely at the contract or local harness level.**

**Next:** inspect the adapter and runtime for contract drift and failure semantics, then run a compact interaction-boundary regression set. Do not broaden the classifier or add autonomy.

### Human Doorway transport hardening

The real Organs transport boundary was hardened after exercising failure cases at the Renaissance handoff.

Verified on Organs commit `1cfee77d9e1253095e6a6c92fc1c877023aecb24`:

- Renaissance discovery and direct doorway transport still pass.
- Malformed Renaissance responses fail closed without breaking the Organs front door.
- An unavailable Renaissance endpoint fails back without execution.
- The Organs test workflow and Human Doorway integration workflow both completed successfully.

The earlier failure on `eb131635e39242b045b320cb3844297116497be4` was a real integration-run failure at the Registry discovery assertion; it is preserved by Git history rather than being treated as current state.

**Current result: PASS — transport, ambiguity, and handoff failure semantics are covered without expanding Renaissance authority or adding autonomy.**

**Next:** inspect the broader world boundary for the next concrete seam. Do not add more Human Doorway machinery unless a demonstrated interaction requires it.

### Attention Choice — live transport verified

The Attention Choice publisher was exercised against the real Organs runtime rather than mocks.

Verified path:

Renaissance Attention Choice → Registry → Communications → real bus → readback

The live test confirmed that Registry discovery resolves Communications, the publisher sends the accepted Attention Choice payload unchanged, Communications persists the event, and the event can be read back from the real bus with the expected topic, event type, publisher, and payload.

The first live workflow attempt exposed a harness-only dependency omission (uvicorn was not installed). That run is preserved in GitHub history. The dependency was added without changing the architecture, and the corrected workflow completed successfully.

Verified commit: 848ae11df98b2649fc3ca19d3c32a173321dee46
GitHub Actions run: 37235855551 (run 101) — PASS

Result: PASS — the first durable Attention Choice transport boundary is now demonstrated end-to-end. Communications remains transport/persistence infrastructure; Renaissance retains Attention Choice semantic ownership. No registry, autonomous consumer, ranking system, or new persistence layer was introduced.

Next: return to the broader world boundary. Do not add more Attention Choice machinery unless a concrete consumer or lifecycle requirement appears.
