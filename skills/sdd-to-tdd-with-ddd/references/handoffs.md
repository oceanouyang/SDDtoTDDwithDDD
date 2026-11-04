# Artifact ownership and handoff contracts

Read this when starting or resuming coordination. Select a development branch in [workflows.md](workflows.md), participation boundaries in [modes.md](modes.md), and conflict handling in [conflicts.md](conflicts.md).

## Resolve task identity

Establish the repository/workspace root, change identifier, intended scope, effective requirements and decisions, current phase, execution method, participant, stopping point, and verification entry points. Use existing project records; a small task needs only a short note and links.

Resolve OpenSpec's actual change path, schema, planning root, and store, where supported, from the current interface and project configuration. Inspect version/help only as needed. A shell command, chat command, skill name, and generated instruction are different interfaces.

## OpenSpec project readiness

Apply this check to both new and existing projects before entering the OpenSpec specification/change workflow. Keep the result in the existing handoff: selected project/planning root and store, initialization state, supporting query/output, and next step.

1. Confirm the intended project root and participation mode. Inspect existing OpenSpec configuration and any explicit linked store; an installed CLI or loaded coordinator does not establish project initialization. A missing local `openspec/` directory does not establish missing setup when an independent store owns the planning artifacts.
2. When the task requires the full workflow, check that the selected CLI/interface is usable and use its current help, configuration, and supported read-only query to resolve that project or store. Record the result as ready, uninitialized, unavailable, or unresolved. Distinguish an empty initialized project from an unresolved root or an absent change; do not require a change before initialization can be verified.
3. If the project is confirmed uninitialized, read the current official initialization instructions and `init --help`, then initialize at the authorized location for the actual host. Reuse matching authorization. Before execution, inspect generated-file cleanup or home/global effects and obtain only any missing scope. Preserve existing source, specifications, custom instructions, and unrelated changes. For missing components or uncertain setup, follow [bootstrap.md](bootstrap.md); diagnose an unresolved context before retrying initialization.
4. Verify initialization from the actual result: check the generated configuration/artifact locations and run a supported query against the same intended project/store. Exit zero or files present alone is insufficient. An empty changes/specs collection can be a valid initialized state. Only then create or resume the authorized change and carry its resolved identity into specifications, plan, implementation, verification, and archive.
5. If initialization or readiness is blocked, report the precise gap, continue only independent authorized work, and keep the full OpenSpec workflow pending. In a lightweight branch that does not need OpenSpec, state that the OpenSpec specification workflow was not used for this task. Explanation, read-only diagnosis, design-only work, and guided learning retain their original write/participant/stopping boundaries.

## Ownership by artifact

| Artifact | Question answered | Update trigger |
| --- | --- | --- |
| Proposal / change scope | Why change, what is included, and who is affected? | New change or material scope revision |
| Main specification | What does the delivered system promise? | Verified specification synchronization |
| Change specification | What does this change add, modify, or remove? | Confirmed behavioral change |
| Glossary entry point | What does a term mean in its bounded context? | Meaning is established or changes |
| Domain notes | Who owns a rule and which states must remain consistent? | Relevant model or invariant changes |
| Design / ADR | How will it work, and why choose this approach? | Material technical decision or new constraint |
| Delivery tasks | Which deliverables have sufficient completion evidence? | Demonstrated delivery or newly invalidated evidence |
| Implementation plan | Which interfaces, files, dependencies, and test steps implement the contract? | Before execution or a relevant implementation revision |
| Execution log | What actually happened and how can work resume? | Actual execution and its results |
| Verification record | Which promises were checked, on what version, and with what gaps? | Acceptance or relevant revalidation |

A glossary is not a backlog or technology-selection diary. Main specifications are not proof that every existing code path is intentional. Duplicate designs and task ledgers do not make disagreements disappear.

## Minimum handoff

Give the receiving activity links to the information it actually needs:

1. **Identity and scope:** project/change, goal, included/excluded behavior, phase.
2. **Authority:** effective requirements/scenarios, domain definitions, decisions, approved design.
3. **Inputs and outputs:** interfaces, files/data versions, expected outputs and locations.
4. **Evidence:** relevant tests/checks, expected results, required runtime or manual acceptance.
5. **Constraints:** compatibility, permissions, known failures, and blocking unresolved decisions.

When something changes or work resumes, identify the relevant source version using a commit, hash, or precise content difference. State which prior approval or evidence still applies. Do not copy entire source documents into the handoff.

## Map activities to effective capabilities

| Activity | Typical component | Next handoff |
| --- | --- | --- |
| Unresolved intent or design | Superpowers brainstorming/discovery | Established goal, scope, decisions, remaining gaps |
| Ambiguous domain or changed rules | Available domain-modeling workflow | Context-qualified language, invariants, ownership |
| Create/update a change | Project's OpenSpec skill or CLI | Resolved change identity and effective contract |
| Plan implementation | Superpowers writing-plans or effective equivalent | Specification-linked steps, interfaces, checks |
| Execute inline | Effective inline execution workflow | Actual code, tests, decisions, execution evidence |
| Execute through authorized delegates | Effective delegated execution workflow | Explicit bounded ownership and review evidence |
| Implement a behavior | Effective TDD workflow | Meaningful RED, GREEN, and regression evidence |
| Investigate a failure | Effective systematic debugging workflow | Reproduced cause, minimal fix, verification |
| Review or complete | Effective review and verification workflows | Findings, fresh results, limitations |

Exact names and available mechanisms depend on the host and installed version. Read the actual selected instructions before claiming to follow them. This table is not a checklist requiring every component on every task.

## Stage exits

- **Discovery → modeling:** examples and intended outcomes are clear enough to disambiguate relevant concepts; important unresolved choices have an identified owner.
- **Modeling → specification:** language and rule ownership explain the examples; cross-context terms and interfaces are explicit.
- **Specification → design/plan:** steps reference effective behavior and independent expected outcomes. Existing design is reused; the output location is explicit.
- **Plan → implementation:** the implementer has the actual plan, exact boundary, dependencies, scenarios, and checks. Multiple TDD microsteps can implement one delivery task.
- **Implementation → verification:** provide actual differences, assertion/scenario mapping, results, decisions, and gaps. Components tested separately still need their promised integration checked.
- **Verification → synchronization/archive:** actual completion conditions hold. Archive, code merge, migration, and release remain separate operations with their own authorization and evidence.

After moving files or archiving a change, resolve current references rather than executing an old path from memory. Resume only unfinished authorized work. Use the [conflict protocol](conflicts.md) when any exit conditions disagree.
