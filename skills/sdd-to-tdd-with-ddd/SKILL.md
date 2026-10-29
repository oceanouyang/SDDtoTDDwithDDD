---
name: sdd-to-tdd-with-ddd
description: Coordinate specification-driven development, domain modeling, BDD examples, and test-driven implementation with OpenSpec and Superpowers. Use when a project adopts this combined workflow or the user explicitly requests coordinated planning, implementation, or change management.
---

# SDDtoTDDwithDDD

Turn a user goal into shared domain meaning, an observable behavioral contract, an implementation plan, and verified delivery. Coordinate the available components; do not impersonate a missing skill or assume that reading a document invokes another component.

## Establish the current task

1. Read applicable project instructions, existing approved decisions, and the affected code, tests, specifications, and active change. Establish scope, current phase, intended behavior, and observable completion evidence. Resume valid work rather than restarting discovery.
2. Identify the available OpenSpec interface, Superpowers skills, and domain-modeling capability through the host's actual discovery/configuration mechanism. A downloaded repository is not an enabled skill. Explain missing capabilities and continue independent authorized work.
3. Read [handoffs.md](references/handoffs.md) to resolve artifact ownership and task identity. Use [modes.md](references/modes.md) to select explanation, guided learning, delivery, or read-only boundaries from the request and existing agreements.
4. Read the relevant branch of [workflows.md](references/workflows.md). For implementation, review, or completion, also read [verification.md](references/verification.md).
5. When artifacts, instructions, behavior, evidence, or status disagree, read [conflicts.md](references/conflicts.md) and only the applicable cases it routes to.

Keep explanation, design-only work, and read-only diagnosis within their requested scope. In guided learning, respect the agreed participant and stopping point. In delivery, small verified increments are an execution method, not a reason to ask for permission after every ordinary step.

## Responsibilities

| Participant | Owns | Does not establish alone |
| --- | --- | --- |
| User / designated stakeholder | Product intent, material business choices, required design decisions, actual user acceptance | Unstated approval of unrelated changes |
| OpenSpec / SDD | Behavioral specifications, change scope, artifact lifecycle | Implementation correctness |
| Domain modeling / DDD | Language, boundaries, invariants, rule ownership | Authority to change product policy |
| BDD practice | Shared concrete examples and their acceptance mapping | Coverage merely because a scenario exists in prose |
| Superpowers / TDD | Discovery, planning, implementation, debugging, review, test-first feedback | Validity of an incorrect test oracle |
| This coordinator | Activity routing, handoff identity, consistency, conflict resolution | Additional permissions or independent review |

DDD is proportional to actual domain complexity. A small function or module can have clear terminology and invariants without repositories, event buses, microservices, or elaborate layers.

## Handoff sequence

1. **Discover:** use the available brainstorming/discovery workflow for unresolved goals and scope. Consume an existing approved design directly; ask only about material remaining gaps.
2. **Model:** clarify ambiguous concepts, state transitions, invariants, and ownership with concrete examples. Use the project's existing glossary entry point.
3. **Specify:** maintain the change through the project's OpenSpec interface. Describe observable behavior and named success, rejection, and boundary examples. Keep implementation choices in design artifacts.
4. **Plan:** use the effective planning workflow with explicit specification inputs and output locations. Reuse the authoritative design; map delivery tasks to implementation steps and verification.
5. **Implement:** use the authorized execution method, defaulting to inline when none is specified. Follow the effective TDD workflow: observe a meaningful behavioral failure, implement the smallest change, then refactor with relevant regression protection.
6. **Verify:** check every promised behavior, domain invariant, required regression, review, and applicable runtime acceptance. Update delivery status only for demonstrated results; synchronize specifications and archive when their actual prerequisites hold.

New evidence can return the affected work to an earlier stage. Preserve valid decisions and historical evidence; invalidate only the dependent parts. See the [conflict protocol](references/conflicts.md).

## Shared invariants

- One change identity connects specifications, domain decisions, design, plan, and evidence.
- One authoritative glossary entry point may index definitions for multiple bounded contexts; it is not a demand for one universal model.
- One delivery tracker owns delivery status. Plans and execution ledgers explain steps and evidence, not a competing truth about acceptance.
- Each promised scenario maps to an actual automated assertion or an explicit, justified manual check with its observed status.
- Small fixes, documentation changes, and behavior-preserving refactors use proportionate workflows.
- Component defaults cannot expand current authorization for delegation, installation, external actions, destructive changes, or publication. Apply the host's instruction hierarchy.

## Report the result

Explain what changed, what observable behavior was verified, and what remains unverified. Distinguish structural checks, automated behavior, runtime observation, independent review, and stakeholder acceptance. Follow the project's change-record requirements.

Installing this skill does not prove automatic routing, tool access, upstream invocation, or successful delivery. Make claims from actual actions and evidence.
