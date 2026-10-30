# First use, missing components, and setup recovery

Read this branch for a fresh host, a necessary missing component, an installed-but-undiscovered component, or an uncertain setup result. Inspect before installing; require only what the current task needs. This is guidance for an agent with available tools, not a bundled installer or a guarantee of tool access.

## 1. Preserve the task and inspect the actual environment

Keep the original goal, project/change identity, approved artifacts, participation mode, authorization scope, and next unfinished step in the existing handoff or a short checkpoint. Installing dependencies does not restart discovery or approve implementation.

Inspect the host (including app versus CLI), platform, effective instructions, configured skill manager/discovery, relevant executable versions, project setup, and prior setup results. Use actual tool/configuration evidence, not remembered paths. Classify each required capability as usable, missing, installed but undiscovered, incompatible, or not yet verified.

| Capability | Minimum relevant evidence | Installation consequence |
| --- | --- | --- |
| OpenSpec | The selected interface resolves the intended project/store/change and supports the required operation | Find its current official host/platform setup only if needed |
| Superpowers | The host discovers the selected skills/plugin and the agent can load the relevant effective instructions | Distinguish a downloaded repository from a discovered integration |
| Domain modeling | Existing project terminology/invariants plus an available modeling workflow when needed | DDD does not require one particular skill package |
| Behavioral examples | Existing tests or an explicit manual acceptance path for the promised scenarios | BDD does not require Cucumber or a new framework |

Reuse healthy installations and current project conventions. A read-only explanation can proceed with disclosed gaps. Install only when setup belongs to the authorized task; otherwise report the gap and continue independent work.

## 2. Find and present the official sources

When a required component is missing or incompatible, search GitHub and verify the current official project identity against these starting points:

| Component | Official repository | Installation source to read |
| --- | --- | --- |
| OpenSpec | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | Current README and the official installation/supported-tools documentation it links |
| Superpowers | [obra/superpowers](https://github.com/obra/superpowers) | Current README installation section for the actual host, including Codex App versus Codex CLI |

Show these official addresses to the user with the missing capabilities and the applicable installation source. If ownership or location changes, verify the move through the original official source. Stars can help discovery; popularity alone does not establish official ownership, suitability, or compatibility.

Read the current linked instructions before proposing commands. Do not copy another host's procedure, assume an old installation-file URL still exists, or prescribe a package manager/runtime when the selected official route does not require it. Record the inspected version/ref or date and the actual host variant in the setup handoff.

If lookup or browsing is unavailable, distinguish the known starting addresses from currently verified instructions. Offer the official links and a bounded user-operated fallback; keep source/compatibility verification pending rather than executing a guessed command or substituting an unverified mirror.

## 3. Match the setup plan to existing authorization

Before mutation, give a compact setup summary: required missing capabilities, official sources, proposed installation/initialization scope, existing authorization covering the actions, and the check that would demonstrate readiness.

Use existing valid authorization without asking again. If a necessary action exceeds it, ask only about that action or group of related actions. Project-local dependency setup, host/plugin installation, global settings, project initialization, upgrades, and restarts are distinct effects. A request to use the coordinator is not blanket permission for all of them.

Use the user's actual host/manager procedure. Preserve existing same-named installations and unrelated configuration; compare before replacement. Follow effective host rules for managed installations. The public guide does not impose a particular manager. For a beginner, state what changes and where, then give one concrete next action when user participation is needed.

## 4. Install or repair through the supported route

When the required scope is authorized and tools are available, carry out the applicable official procedure for the selected component, host, and platform. Install only missing prerequisites. Capture the actual result and affected scope; a proposed command is not an executed installation.

If a command fails or its result is unknown, inspect existing artifacts, discovery/configuration, and output before retrying. Reuse a completed safe step; avoid duplicate initialization or overwriting unrelated work. A source/version change or a wider installation scope needs a revised plan and its applicable authorization.

If the agent cannot perform a UI, permission, authentication, or host reload step, explain the exact user action and expected observation. Resume verification when the result is available. Keep the original task/checkpoint intact while setup is blocked.

## 5. Verify readiness in separate observable layers

| Layer | Evidence | Limit |
| --- | --- | --- |
| Installation | Successful official operation plus the expected installed artifact/interface/version | Files present do not prove host discovery |
| Discovery and loading | The actual host exposes the component and the relevant effective instructions can be read | A displayed name does not prove execution |
| Interface readiness | A non-destructive supported query resolves the intended project/context and accepts the required input format | A generic version/help result does not prove the project integration |
| Task handoff | Within the task's authorization, the selected component consumes the real specification/domain/plan inputs and produces its expected output | A separate demo does not prove the shared chain |

Follow the current host's discovery/reload guidance when needed and preserve unrelated running work. Report each verified layer and any pending user action. Installation success can be reported while a new-session discovery check remains pending; do not call the whole workflow integrated until its actual handoff is observed.

## 6. Return to the original task

Summarize what is now usable, what remains missing/pending, and the next original task step. Restore the same change, approved design/plan, domain entry point, participation mode, and stopping boundary. Continue the authorized development work from that point, or stop at the agreed learning/design/read-only boundary.

For a first-time user, keep this handover short: what is ready, what needs their decision/action, and what happens next. Reuse the existing progress record rather than creating a second tracker. A setup repair does not erase prior failures or complete unrelated delivery tasks.
