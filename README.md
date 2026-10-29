# SDDtoTDDwithDDD

**A portable agent skill connecting specifications, domain models, and test-driven delivery.**

[中文说明](README.zh-CN.md) · [Skill](skills/sdd-to-tdd-with-ddd/SKILL.md) · [Worked example](examples/loan-renewal/README.md) · [Validation](docs/validation.md)

SDDtoTDDwithDDD coordinates **Specification-Driven Development (SDD)**, **Test-Driven Development (TDD)**, **Domain-Driven Design (DDD)**, and **Behavior-Driven Development (BDD)**. It provides a practical handoff protocol for OpenSpec, Superpowers, and domain-modeling workflows.

It is an instruction-based coordination layer. It does not install dependencies, modify upstream skills, or provide a runtime that automatically invokes other skills.

## What it coordinates

| Concern | Responsibility | Useful artifact |
| --- | --- | --- |
| SDD / OpenSpec | Define the behavior being changed and manage its lifecycle | Proposal, requirements, scenarios, design, delivery tasks |
| DDD / domain modeling | Clarify language, boundaries, ownership, and invariants | Existing glossary, model notes, relevant decisions |
| BDD | Discover concrete examples with stakeholders and connect them to acceptance evidence | Named success, failure, and boundary scenarios |
| TDD / Superpowers | Plan, implement, debug, review, and verify behavior | Implementation plan, failing/passing tests, code, execution evidence |
| This skill | Connect those activities and resolve conflicting inputs | Scoped handoffs, traceability, evidence-based completion |

The normal flow is:

```text
Goal → domain meaning → specification and examples → design and plan
     → behavioral RED → minimal implementation → GREEN → refactor
     → acceptance and regression evidence → synchronize and archive
```

This is an incremental loop. Small fixes do not require a complete new modeling exercise, and an approved design should not trigger a second requirements interview.

## Install and use

1. Obtain this repository and locate `skills/sdd-to-tdd-with-ddd/`.
2. Install **that folder** using your agent host's supported skill installer, skill directory, or managed configuration. Preserve any existing same-named installation until you have compared it.
3. Enable OpenSpec, Superpowers, and your chosen domain-modeling capability through their own supported setup procedures when you want the full integration. See [compatibility](docs/compatibility.md).
4. Ask your agent to use the skill. In hosts supporting dollar-prefixed invocation:

```text
Use $sdd-to-tdd-with-ddd to implement this feature in the existing repository.
Reuse approved decisions, identify the relevant specification and domain rules,
then implement and verify the smallest useful increments.
```

If the host cannot discover installed skills, explicitly ask it to read `skills/sdd-to-tdd-with-ddd/SKILL.md`. That provides instructions; it does not prove automatic discovery or component invocation works.

The repository/display name is **SDDtoTDDwithDDD**. The portable skill identifier is **sdd-to-tdd-with-ddd**. `agents/openai.yaml` supplies optional UI metadata; hosts that do not support it can use the Markdown instructions.

## Common starting points

- **New project:** establish one deliverable slice, clarify only the relevant domain, and write observable acceptance examples before implementation.
- **Existing feature:** inspect the affected code, specifications, tests, and active changes; preserve existing contracts and resume from the actual unfinished point.
- **Bug fix:** reproduce the violation of an established promise. Change the promise only when that is the actual requested product change.
- **Guided learning:** explain the overall flow, then advance one agreed step and wait for the learner's contribution.
- **Continuous delivery:** continue through authorized, verifiable increments without asking for permission after every routine step.

Learning pace, autonomy, language, hosting, deployment, and approval rules come from the current user and project. This public edition does not impose one person's preferences or a particular local environment.

## Conflict handling

The [conflict protocol](skills/sdd-to-tdd-with-ddd/references/conflicts.md) covers **26 cases**, including contradictory requirements, incompatible invariants, legacy contracts, stale plans, incomplete green test suites, concurrent specification changes, missing components, and conflicting completion states.

Its central rule is to separate **decisions about intended behavior** from **evidence about observed behavior**. No component always wins simply because it is OpenSpec, a test suite, a domain model, or an implementation.

Only the affected work becomes blocked. Preserve valid decisions and evidence, resolve the actual disagreement, update dependent artifacts, and rerun the relevant checks.

## Try the example and repository checks

Python 3.11 or newer is sufficient for the included standard-library example and validator:

```sh
python scripts/validate.py
```

The [loan-renewal example](examples/loan-renewal/README.md) includes a specification, domain vocabulary, scenario-to-test mapping, implementation, and six executable tests. It demonstrates the artifact handoff without requiring OpenSpec or a BDD runner to be installed.

Repository validation checks packaging, local links, portable skill metadata, common accidental disclosures, and the example tests. These checks do **not** establish that a model will consistently follow the skill. Current validation limits are explicit in [docs/validation.md](docs/validation.md).

## Upstream projects and license

OpenSpec, Superpowers, and domain-modeling remain independent projects with their own installation procedures, licenses, and release schedules. No upstream implementation is bundled. This is an independent integration guide, not an official distribution or endorsement. See [ATTRIBUTION.md](ATTRIBUTION.md).

The original coordination instructions, documentation, and example in this repository are released under the [MIT License](LICENSE).
