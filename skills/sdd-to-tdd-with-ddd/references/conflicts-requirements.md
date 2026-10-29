# Requirements and domain conflicts

Apply the [shared protocol](conflicts.md), then use only relevant cases. The coordinator is the currently authorized executor, not a new team or approval committee.

## R01 — A current request differs from an approved design

Distinguish an explicit instruction from a question or proposal. Apply an explicit scoped replacement without asking the same question again. DDD identifies semantic consequences; OpenSpec updates the affected contract; Superpowers revises dependent steps. Retain unchanged decisions. Resume when material implications and any required new design decision are resolved.

## R02 — A broad vision exceeds the current deliverable

Convert the vision into concrete tasks and useful increments. DDD identifies rules that must remain together; OpenSpec separates included behavior from later candidates; Superpowers plans feasible delivery. Use established priorities, but obtain a material scope tradeoff when promises cannot coexist. A backlog candidate is neither implicitly authorized work nor a delivered feature.

## R03 — Specification, implementation, and tests disagree

Compare effective versions and actual business sources, not document votes. If the promise is one renewal while code and tests allow two, fix the implementation and wrong assertion when the promise is authoritative. If a confirmed newer decision exists, update the stale contract first. Without a reliable decision, describe the disagreement and block only dependent behavior. Evaluate compatibility separately if customers rely on the defect.

## R04 — A new requirement contradicts an invariant

DDD supplies the smallest concrete counterexample and verifies that the invariant has a business basis. OpenSpec describes alternatives such as rejection, queuing, or a different resource model; Superpowers evaluates feasibility. A stakeholder chooses irreconcilable policy. Resume when the decision explains both the success and rejection/compensation states. Technical inconvenience is not automatically an immutable domain law.

## R05 — A term has different meanings across contexts

A catalog's “book” can mean a work while lending's “book” means a physical copy. DDD qualifies context, identity, units, and state in the existing glossary entry point. OpenSpec specifies boundary meaning; implementation translates at the boundary. Verify the mapping rather than forcing a universal model or renaming unrelated code. Different contexts are legitimate; ambiguous interchange within one context needs correction.

## R06 — Glossary locations or versions differ

Resolve the effective project entry point and installed instructions before adopting a new filename. Compare actual content when multiple definitions exist: link or consolidate uncontroversial material within authorization; resolve semantic disagreements separately. Resume when consumers reach the authoritative definitions. A newer upstream example does not authorize a project migration or a managed-skill edit.

## R07 — DDD structure is disproportionate to the problem

Identify actual concepts and consistency requirements before introducing repositories, microservices, events, or layers. Superpowers compares a sufficient simple implementation with more complex alternatives; OpenSpec stays focused on observable behavior. Prefer a small function/type/model when it protects the required rules. Removing ceremony does not remove domain analysis, and minimizing code does not excuse missing invariants.

## R08 — A new model breaks legacy interfaces or data

DDD separates internal representation from public contract and identifies deterministic versus ambiguous conversions. OpenSpec describes compatibility, rejection/degradation, and migration behavior; Superpowers plans adapters, migration, recovery, and representative tests. Preserve old promises where possible. Irreversible deletion, downtime, or client breakage does not become authorized merely because the new model is cleaner. Report unexecuted migration as unexecuted.

## R09 — Context boundaries conflict with transactional consistency

Determine which invariants require atomicity and which tolerate delay. OpenSpec describes visible intermediate states, failures, and duplicate requests. Superpowers evaluates shared transactions, boundary changes, idempotency, or compensation as appropriate. Replacing immediate consistency with eventual consistency is a behavioral decision. Verify relevant failure/reordering/duplicate paths; a compensation diagram alone is not implementation evidence.

## R10 — BDD examples and the automation format differ

Keep the behavioral contract in OpenSpec and its language consistent with the domain. Execute it through the existing suitable stack; Gherkin/Cucumber are options, not prerequisites. If selected, supply real steps and assertions. Generated files remain derived from their source. Resume when every promise maps to a discriminating check or an explicit justified manual item; similar names and counts do not prove coverage.

## R11 — Units, precision, defaults, or error semantics are implicit

Clarify types, units, valid values, modes, and undefined results. For example, an angle's interpretation changes a trigonometric result. OpenSpec makes the observable convention explicit; TDD uses independent examples or appropriate properties. Resolve visible defaults from existing decisions or ask for a missing material choice. Tolerance must follow correctness needs rather than being widened until the current output passes.

## R12 — Capability rename, split, or removal loses behavior

Check stable requirement identity and the actual schema's addition/modification/removal/rename semantics. A full modified requirement must retain scenarios that remain promised. DDD establishes whether meaning changed; Superpowers updates references and compatibility regression. Verify the final contract contains no accidental loss, duplication, or revived behavior. Concurrent changes to the capability also require [execution case E08](conflicts-execution.md).
