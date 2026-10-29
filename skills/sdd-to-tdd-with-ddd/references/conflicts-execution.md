# Execution and evidence conflicts

Apply the [shared protocol](conflicts.md), then use the relevant case. These are conditional responses, not mandatory checks for every change.

## E01 — Skills repeat discovery or recursively invoke each other

Keep one task identity and coordinator. Superpowers leads unresolved discovery, DDD resolves domain ambiguity, and OpenSpec records the contract. Consume valid handoff artifacts rather than restarting completed stages. Project mappings can adapt defaults, but incompatible explicit requirements must be disclosed rather than silently ignored. Resume with one next activity and satisfied stage exits; reading instructions does not establish every activity was executed.

## E02 — Components write different designs or plan paths

Resolve actual planning root, store, change, worktree, and accepted interfaces. Maintain one editable design and one detailed plan; use supported parameters or references for compatibility. Check a helper's full-path ownership before assuming same-named files collide. If a real mismatch exists, use an authorized project adaptation or explicit alternative execution method. Verify the receiving interface consumes the correct file and identity.

## E03 — Delivery tasks, plan, ledger, and CLI disagree about completion

Check what each status means and how steps map to deliverables. A file can be ready and a microstep complete while acceptance remains outstanding. Compare actual changes, assertions, and results; correct premature delivery checks without rewriting historical logs. Track pending conditions in the existing delivery mechanism. Resume completion only when current evidence supports each item.

## E04 — RED is environmental, a test starts green, or implementation came first

Fix the relevant environment problem before interpreting behavioral failure. A green test can be a useful regression; investigate whether its assertions distinguish wrong behavior. An isolated known-wrong sample can check detection without damaging the actual workspace. If implementation came first, disclose the missing test-first evidence. Any safe reconstruction must respect ownership and effective TDD instructions; never discard another person's work or invent RED history.

## E05 — The oracle is wrong or test convenience distorts the model

Check the test against independent confirmed rules and examples. Change an assertion only with a concrete reason, not merely because it fails. Test public behavior and invariants; mock justified external boundaries rather than only mock calls. Avoid production-only test backdoors with no domain purpose. Resume when an independent counterexample distinguishes the correct implementation and any interface change preserves compatibility.

## E06 — Green tests omit promised scenarios or lack real assertions

Compare OpenSpec's promised set, relevant domain boundaries, actual assertions, data rows, and execution results. Identify undiscovered, ungenerated, empty, skipped, pending, and undefined coverage. Add the missing verification through the existing mechanism, then exercise it; do not relabel an omission as manual success. Nine discovered green cases do not establish a tenth prose-only case passed.

## E07 — A changed requirement partially invalidates the plan and approval

Compute the relevant difference, domain implications, specification update, dependent steps, and changed oracle. Preserve independent valid work. Old approvals and successful logs retain historical meaning but cannot establish the new behavior. Reopen affected delivery/verification items and reconfirm only a material new decision. Resume from the updated actual plan and rerun affected checks.

## E08 — Concurrent changes merge textually but overwrite semantics

Compare their common baseline, full requirements, scenarios, and invariants. Establish specification synchronization order; the later modification must retain the first change's effective behavior. Serialize conflicting synchronization, preserve separate change identities, and distinguish code merge from archive. Protect unrelated workspace changes. Verify the combined contract and integrated code, not just a conflict-free Git merge.

## E09 — A dependency is missing, incompatible, or only downloaded

Identify the actual enabled capability, version, and interface. Continue independent authorized work; handle installation or project adaptation under existing authorization. Do not silently replace a specified component, patch managed upstream skills, or upgrade the entire environment. Report whether the result is static inspection, a consumable handoff, actual execution, or an unresolved block.

## E10 — Evidence is stale, cross-environment, or flaky

Associate results with relevant code, dependencies, configuration, inputs, and environment. Revalidate affected evidence after changes without discarding unrelated results. Preserve intermittent failures and diagnose time/randomness/network/shared-state causes. Retries can investigate; selecting one green run cannot establish reliability. A quarantined case leaves a gap, and results from different versions cannot be combined into a fictitious all-green version.

## E11 — Unit tests pass but runtime promises fail

Confirm the requirement is in scope and observe the actual promised UI, offline, scale, latency, privacy, or integration behavior. Distinguish a technical bottleneck from a domain restriction. Repair within the contract where possible; reduced precision, changed consistency, or a material new cost needs an established decision or stakeholder choice. Missing runtime tooling leaves explicit pending acceptance, not a substitute success claim.

## E12 — Partial delivery, migration, rollback, archive, and release are conflated

Record each lifecycle result separately. Split delivery only when authorized and independently valid, keeping remaining promises tracked. Preserve actual recovery state after failure. Roll back only identifiable owned changes within authorization; shared data and irreversible migrations need the appropriate recovery decision. For an uncertain external operation, inspect actual status before repeating side effects. Archive success does not establish code merge or release.

## E13 — Review conflicts with the contract or independent review is unavailable

Treat a finding as evidence to verify. Reproduce a defect against the effective contract; separate preference or new requirements from correctness. Use independent review only when available and authorized. Otherwise label author review honestly; if independence is a required exit and unavailable, delivery remains pending that exit. Do not impersonate a second reviewer or silently lower the standard.

## E14 — A component suggests execution beyond the current boundary

Apply the current design-only, read-only, pause, delegation, or publication limits to every component. A workflow's next step is not fresh authorization. Preserve task identity, phase, changes, evidence, and next step without continuing a paused task. On explicit resume, inspect current files, relevant status, prior external outcomes, and evidence freshness. An old summary or another task's request is not permission to resume.
