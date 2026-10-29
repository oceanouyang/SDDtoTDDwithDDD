# Validation scope

## Reproduce local checks

Use Python 3.11 or newer; no third-party Python dependencies are required:

```sh
python scripts/validate.py
```

The validator checks:

- The explicit publication file set, portable skill identifier, frontmatter, UI invocation, and reference availability.
- Repository-local Markdown links; it does not claim to check remote link availability.
- Common accidental credential patterns, local absolute paths, and non-source/binary files in the publication set.
- The standard-library loan example's six behavior tests.

The disclosure scan is a useful bounded check, not proof that a secret can never appear. Publish only deliberately reviewed source files; never copy private conversation archives or an entire authoring workspace into this repository.

## Evidence levels

| Check | What it demonstrates | What it does not demonstrate |
| --- | --- | --- |
| Metadata and links | Required local artifacts exist and references resolve | Correct product decisions |
| Example tests | Six assertions about the supplied loan behavior pass | Every workflow instruction is obeyed |
| An observed example RED→GREEN | The recorded change fixed the demonstrated missing behavior | A fabricated full test-first history or independent review |
| A real component handoff | The named versions consume the supplied inputs | All other hosts/versions are compatible |
| Model evaluation | The tested prompts produced observed decisions | Universal or guaranteed compliance |

For the initial release, local package checks and the worked example are executable; independent model evaluation, automatic discovery, and full upstream component invocation are not established by these repository tests.

## Improving the workflow

Report an actual or synthetic, explicitly labeled failing case with the input, relevant artifacts, component/host versions, observed decision, and expected behavior. Resolve one demonstrated coordination issue at a time. Distinguish author walkthroughs from independent evaluations.

When available and authorized, behavioral evaluations should give an evaluator the skill and raw task artifacts without the intended answer. Use an isolated workspace and preserve failure evidence. No such independent evaluation is claimed by the initial release.
