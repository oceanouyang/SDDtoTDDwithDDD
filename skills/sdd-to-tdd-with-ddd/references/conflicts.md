# Conflict resolution protocol

Read this when a concrete disagreement affects a handoff, implementation, or completion claim. Do not audit every case during ordinary work. The coordinator applies the host's instruction hierarchy and current authorization; component instructions do not create a new authority above them.

## Route to the relevant cases

| Disagreement | Reference |
| --- | --- |
| Requirements, domain language/invariants, compatibility, transactions, BDD expression, numeric contracts, capability identity | [Requirements and domain cases R01–R12](conflicts-requirements.md) |
| Repeated skill stages, output paths, state, TDD, coverage, stale evidence, concurrent changes, unavailable components, runtime acceptance, review, pause/release | [Execution and evidence cases E01–E14](conflicts-execution.md) |

## Authority is not observation

| Source | Establishes | Does not establish alone |
| --- | --- | --- |
| Current user instruction and applicable project rules | Authorized scope and explicit choices | Approval of unspecified actions |
| Effective specification plus approved change | Intended behavior for that scope/version | Approval of every newer draft |
| Domain vocabulary/model | Meaning, ownership, supported invariants | Product-policy authority for the model author |
| Design, ADR, plan | Technical choices and intended steps | Actual acceptance |
| Code, data, observed runtime | What currently happens | That existing behavior is correct or removable |
| Tests, logs, review | Evidence for particular assertions and versions | Correctness of the oracle or untested behavior |
| Tool status, generated files, downloaded material | Recognized structure or suggestions | Business correctness, invocation, or authorization |

First compare the same project, context, capability, and version. File timestamps, names, document counts, and self-declared component priority cannot resolve a semantic contradiction. An approved scoped change supersedes only the behavior it actually changes.

## Resolve in six steps

1. **Locate:** name the exact incompatible expectations and cite their requirements, definitions, interfaces, or assertions. Check for a simple context/version/path mismatch first.
2. **Preserve:** inspect the relevant raw inputs and current state; distinguish decisions, observations, proposals, and unknowns. Retain historical results with their original meaning.
3. **Bound:** pause only dependent work that would bake in an unsupported choice or cause harm. Continue independent authorized tasks without guessing the blocked contract.
4. **Decide:** resolve engineering details that existing constraints determine. Escalate only a missing material choice about behavior, compatibility, cost boundary, or permission, with concrete options and a recommendation.
5. **Update:** revise the owning artifacts in dependency order: behavioral/domain decision → specification/examples → design/plan → tests/implementation → evidence/status. Follow the effective TDD workflow for behavior changes.
6. **Verify and resume:** run a check that distinguishes wrong from right plus affected regressions; link the decision, revisions, and results. Resume dependencies only when their prerequisites hold.

## Decision ownership

- An implementation violates an effective promise: DDD checks ownership, OpenSpec preserves the promise, and Superpowers investigates and fixes it.
- The user explicitly changes a promise: apply the instruction within its scope; ask only about material undecided implications.
- Confirmed business rules cannot coexist: domain modeling supplies a counterexample, OpenSpec describes alternative observable outcomes, and the stakeholder chooses policy before implementation.
- Behavior-preserving engineering adaptation: the coordinator may resolve it within authorization and record the relevant rationale.
- A new resource, security, privacy, or performance constraint appears: verify the real constraint; distinguish a local repair from a change to promised behavior.
- Installation, external messages, destructive changes, merge, and release retain their actual authorization requirements. Prepare authorized reviewable work without treating the skill as permission.

## Invalidate only what depends on the change

| Changed fact | Recheck | Usually retain |
| --- | --- | --- |
| Business behavior or error policy | Relevant examples, invariants, plan, oracle, acceptance | Unaffected decisions and results |
| Internal model structure with stable external contract | Ownership, dependent steps, relevant regression | Effective external requirements |
| Implementation, dependency, runtime environment | Relevant execution evidence and compatibility | Still-valid product choices |
| Path, store, worktree, file move | Identity, references, helper ownership, evidence association | Behavioral evidence unaffected by the move |
| New suggestion without changed facts | Its validity and impact | Existing decisions until contradicted or superseded |

Invalidation means evidence no longer establishes current completion, not that it should be deleted. Approval attaches to content and conditions, not a filename. Reconfirm material changes without repeating approval for unchanged decisions.

## Minimal resolution record

Use the existing design/decision record for rationale, delivery tasks for status, and verification record for execution evidence. Link them rather than introducing another status system.

```text
Disagreement: incompatible expectations and their source/version
Impact: blocked dependencies and independent work that can continue
Decision: chosen outcome, authority/reason, unresolved part
Revisions: domain/specification/plan/code/test references
Evidence: discriminating check, regression, relevant version/environment
Resume: satisfied prerequisites and remaining conditions
```

If a correction still leaves the same contradiction, revisit its premises. Without new evidence, stop cycling between skills and report the exact missing decision or check.
