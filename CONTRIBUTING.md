# Contributing

Use a concrete coordination problem rather than adding a universal rule for every hypothetical risk.

1. Describe the task, relevant artifacts, component/host versions, observed failure, and expected outcome. Label synthetic examples.
2. Keep common routing in `SKILL.md` and conditional detail in the appropriate reference. Preserve one source of truth for each rule.
3. Keep the skill host-neutral. Do not add private conversations, machine paths, credentials, personal preferences, or unrequested permissions.
4. Run `python scripts/validate.py` and `git diff --check`.
5. If changing the publication file set, update `PUBLIC_FILES` in the validator. Record AI-generated changes in `AI_CHANGELOG.md` with the actual scope and verification.

A passing example or author walkthrough is not an independent model evaluation. Describe what you actually checked, and keep upstream installation instructions linked rather than copied into this project.
