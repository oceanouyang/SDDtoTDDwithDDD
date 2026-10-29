# Implementation and completion evidence

Read this for implementation, review, integration, or completion. Use [conflicts.md](conflicts.md) if a test, specification, implementation, or status disagrees with another source.

## TDD evidence

Follow the effective TDD instructions for the task. New or changed behavior needs a concrete test that fails for the intended behavioral reason, minimal implementation that passes it, and relevant regression protection during refactoring.

- Derive expected outcomes from confirmed rules, independent examples, hand calculation, or appropriate properties. Do not compute the oracle with the implementation under test.
- Import errors, missing dependencies, misspelled commands, and unavailable tools do not establish a behavioral RED.
- A new test that immediately passes may protect existing behavior. Check its discriminating power; do not break production code merely to manufacture a failure history.
- Test observable outcomes, state, invariants, and real boundaries. Use mocks for justified external seams, not as the sole behavior being verified.
- If code was written first, report that honestly. Apply the effective workflow within ownership/safety constraints; do not delete another person's work or invent test-first evidence.
- Preserve and explain pre-existing failures and their relevance. Do not silently expand into unrelated fixes or hide a failing baseline.

## BDD and scenario coverage

BDD includes collaborative example discovery, a shared contract, and acceptance feedback. Gherkin and Cucumber are optional. Reuse a suitable existing test stack.

Map each promised requirement/scenario to assertions and actual results. One scenario can map to several tests, several scenarios to one parameterized test, or an outline to multiple data rows. Use stable identities and verify semantic coverage; equal names or counts alone are insufficient.

| Evidence | Supported statement |
| --- | --- |
| Actual automated assertions pass on the relevant version | Those behaviors passed that execution |
| Manual/runtime steps were performed and observed | The documented observed path passed |
| Only prose or generated test files exist | Specification/tests were written; execution remains unverified |
| Skipped, pending, undefined, missing assertions, or undiscovered cases | A validation gap remains |

Compare the promised set with the executed set, rather than trusting only cases discovered by the runner. Retain existing scenarios that should survive the change. Generated scenarios remain derived outputs; revise their authoritative source.

## Delivery exit

Check the applicable items together:

1. **Coverage:** promised behavior and boundaries have corresponding verification; gaps remain explicit.
2. **Domain consistency:** language, ownership, state transitions, and invariants match the effective contract.
3. **Execution:** relevant checks ran after the change, on identified code and environment, with unexplained failures resolved or correctly scoped.
4. **Regression:** preserved interfaces/data and behaviors have appropriate evidence.
5. **Review:** required available review is complete; author review and independent review are reported separately.
6. **Runtime acceptance:** actual UI, offline, performance, integration, or other promised conditions have the evidence they require.
7. **Status:** only supported delivery items are complete; plan and ledger results do not override missing acceptance.

Structural validation or an artifact marked ready is not proof of implementation correctness. A mechanical project gate can improve enforcement when authorized, but an instruction document is not such a gate.

Separate archive, code merge, data migration, release, and stakeholder acceptance. Identify any operation that synchronizes specifications as a side effect before executing it.

## Component and version compatibility

Discover actual interfaces and relevant versions through the host/project. Use help, configuration, and current effective instructions; do not treat a stale integration recipe as a universal API.

Adapt project-owned paths or configuration within authorization. Preserve managed upstream/system/plugin instructions. A glossary might be named CONTEXT.md or GLOSSARY.md; resolve the existing authoritative entry point instead of creating both.

Some execution helpers already distinguish same-named plans using full-path ownership. Verify the mechanism before adding snapshots or an extra tracking layer. Some releases support inline TDD and review even if an older bridge description assumes delegation.

Observe only the checks that the change needs. Installing, discovering, loading, executing, and successfully integrating a component are different facts. Report an unavailable component or blocked validation explicitly, including any proposed substitute and its limits.

## Calibrated completion

Use statements such as “specification and automated behavior checks passed; offline browser acceptance remains unverified” or “inline implementation was exercised; independent review and automatic skill routing were not verified.” State actual capabilities used, not names that merely appeared in a catalog.
