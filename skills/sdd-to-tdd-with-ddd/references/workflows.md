# Development workflows

Use the relevant branch, the [handoff contract](handoffs.md), and the participation boundaries in [modes.md](modes.md). Return only the affected work to an earlier stage when new evidence changes a decision.

For every branch, apply [OpenSpec project readiness](handoffs.md#openspec-project-readiness) before OpenSpec-dependent work; a lightweight branch records its non-use instead of initializing unnecessarily.

## New project

1. Establish users, concrete tasks, platform, first deliverable, and success criteria. Preserve explicit constraints and technology choices.
2. Compare feasible approaches and satisfy applicable design-decision requirements. Label experiments and unconfirmed assumptions as such.
3. Model only the concepts, rules, and boundaries needed for the slice. Simple functions and types may be sufficient.
4. Create the authorized project/change entry point using the available OpenSpec schema. Capabilities describe maintainable system behavior, not merely task names.
5. Write observable requirements and named examples, then the relevant design and plan. Treat environment setup as a dependency of a real deliverable.
6. Implement a small useful vertical slice through TDD and applicable acceptance checks; then continue according to the authorized delivery scope or learning pace.

Exit: an increment has observable value and evidence, with remaining scope explicit; a directory tree is not a delivered product.

## Add or change an existing feature

1. Inspect the affected implementation, tests, effective specification, glossary, and active changes. Distinguish observed behavior, intended behavior, and the requested difference.
2. Reuse approved decisions and existing handoff/progress records. Fill only relevant documentation gaps rather than reverse-engineering the whole repository.
3. Revisit domain modeling when meanings, invariants, or ownership change; otherwise consume the existing model.
4. Use the current OpenSpec schema for additions, modifications, removals, and renames. A modification must preserve the full updated requirement and all retained scenarios where that schema requires them.
5. Plan interface/data compatibility, needed migration, and recovery. Integrate new acceptance and retained regressions into the responsible tasks.
6. Observe a meaningful failing test for changed/missing behavior, implement minimally, and verify the relevant new and preserved behavior.
7. Synchronize and archive only after the actual completion conditions hold.

Exit: the change satisfies the new contract and preserves promised existing behavior, with compatibility costs understood.

## Fix a defect

1. Use actual inputs, errors, logs, or a reproducing test to investigate the cause through the effective debugging workflow.
2. Determine whether implementation violates an established promise or the requested product policy itself is changing. Do not redefine a bug as correct behavior to obtain a green suite.
3. Reproduce the defect, observe failure for the right reason, apply the smallest fix, and run relevant regressions. Check rule ownership when the domain is involved.
4. Use the project's lightweight change mechanism for a restoration of existing behavior. Do not invent a capability merely to satisfy a document format.

Exit: the reproduced defect changes from failing to passing, the impact is bounded, and the contract/implementation relationship is clear.

## Behavior-preserving refactor, documentation, or configuration

Use a proportionate plan and checks. Refactors preserve public behavior through appropriate regression protection. Documentation and reversible configuration changes do not automatically need new business specifications or implementation-mirroring tests. Maintain the existing structure and contracts unless changing them is necessary and authorized.

## Exploration or prototype

Use a separate authorized fixture when it answers a real technical question. Identify synthetic assumptions, disposable outputs, and the actual acceptance question. A simulated stakeholder, author review, or mocked service does not prove real product approval, independent review, or production integration.

## Design-only, read-only, or paused

Design-only work produces a reviewable design without beginning product implementation. Read-only diagnosis observes the allowed sources without restarting services or generating unapproved load. A pause stops the affected work and monitoring; retain the current phase and next step and resume only after a subsequent explicit request.

Existing approval remains applicable to unchanged content. Prepare authorized evidence and concrete choices before asking for a material missing decision; do not create a new permission checkpoint after every artifact.
