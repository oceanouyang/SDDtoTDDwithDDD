# Compatibility and integration

## Supported contract

The skill is Markdown instructions with optional UI metadata. It requires a host that can read instructions, inspect project artifacts, and perform the authorized development work. It has no background runtime, package installer, dependency resolver, or automatic hook into another skill.

For the full OpenSpec/Superpowers/domain-modeling path:

1. Set up each chosen component using its own current supported procedure.
2. Identify actual names, versions, commands, and project paths rather than assuming examples are current APIs.
3. Give the coordinator the relevant installed instructions and resolved change identity.
4. Pass specification/domain inputs and explicit output locations to the implementation workflow.
5. Verify a real handoff before reporting integration as successful.

OpenSpec is a concrete tool; SDD is the practice it supports. Superpowers is an execution workflow; TDD can also be performed through another explicitly identified workflow. DDD and BDD are practices, not single mandatory packages.

If a requested component is unavailable, disclose the gap and any proposed equivalent. Continue independent work, but do not claim the missing component ran.

## Host differences

Use the host's supported skill folder and installation/management process. Install `skills/sdd-to-tdd-with-ddd/`, not the entire repository as a skill. Follow that host's discovery/reload requirements.

Some hosts accept `$sdd-to-tdd-with-ddd`; others require explicit instructions or a different invocation. The README's dollar-prefixed example applies only when the host supports it. `agents/openai.yaml` is optional UI metadata and does not provide tool access or install upstream workflows.

Language, local/global scope, delegation, approvals, scheduling, credentials, and publication come from the actual user/project/host. This repository does not prescribe a machine-specific manager or edit managed system/plugin files.

## Known adaptation points

| Difference | Resolution |
| --- | --- |
| Different glossary filenames | Resolve one authoritative entry point; keep context-qualified definitions |
| OpenSpec schema/path/store differences | Consume actual configuration and current command output |
| Upstream plan output differs from project location | Pass supported explicit paths or project-owned references |
| Same-named plans | Verify helper ownership/isolation before adding another mechanism |
| Delegated versus inline execution | Use the authorized effective workflow; report review limits |
| Artifact ready versus tested behavior | Apply actual evidence-based completion conditions |
| Gherkin versus another testing stack | Maintain semantic scenario-to-assertion coverage |

## Validation status

The included Python example is self-contained and reproducible. It is not an OpenSpec/Superpowers runtime adapter. Initial publication checks validate the package and example, not every host/version combination, automatic skill discovery, or model compliance. Future compatibility claims should name the exact host, component versions, inputs, outputs, and executed checks. See [validation.md](validation.md).
