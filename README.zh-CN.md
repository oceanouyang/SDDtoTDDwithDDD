# SDDtoTDDwithDDD

[English README](README.md)

一个把 **SDD（规格驱动开发）→ TDD（测试驱动开发）** 与 **DDD（领域驱动设计）** 串联起来的通用 Agent Skill，同时用 BDD 的具体行为例子连接需求与验收。

它协调 OpenSpec、Superpowers 和领域建模流程之间的职责、产物及工作顺序，不捆绑上游组件或自动调用运行时。具备工具和已有授权的 Agent 可以按首次引导分支检查环境、查找官方来源、代装必要缺项、验证后恢复原任务；Skill 本身不赋予安装权限。

## 分工与顺序

- **OpenSpec / SDD**：维护行为约定、本次变更范围及交付生命周期。
- **DDD / domain-modeling**：澄清术语、边界、规则归属与不变量，按项目复杂度建模。
- **BDD**：把需求落实为成功、失败和边界例子；Gherkin 与 Cucumber 都是可选工具。
- **Superpowers / TDD**：计划、实现、调试、评审及验证，用真实行为失败驱动实现。
- **协调 Skill**：传递正确资料、处理矛盾、让完成状态对应实际证据。

通常按“目标 → 领域含义 → 规格与例子 → 设计和计划 → 测试失败 → 最小实现 → 测试通过 → 回归和验收”推进。已有设计直接复用，小修复走轻量分支。

## 使用

从 [GitHub Releases](https://github.com/oceanouyang/SDDtoTDDwithDDD/releases) 下载带版本号的可移植 Skill ZIP（历史版本由标签保留），或获取源码中的 `skills/sdd-to-tdd-with-ddd/` 目录，通过你的 Agent 宿主支持的方式安装，再按各自官方方式配置所需组件。可移植 ZIP 包含 Skill 目录及许可／来源说明，不包含整个仓库。支持 `$skill-name` 的宿主可使用：

```text
使用 $sdd-to-tdd-with-ddd 完成本次功能。
先读取现有规则、设计、规格与实现，确认本次范围，再按可验证增量实施。
```

仓库及展示名称为 **SDDtoTDDwithDDD**，内部 Skill 标识为 **sdd-to-tdd-with-ddd**。没有自动发现能力时，可以明确让 Agent 读取 [SKILL.md](skills/sdd-to-tdd-with-ddd/SKILL.md)。

通用版提供讲解、陪练、持续交付和只读调研等分支；具体语言、节奏、授权及技术栈由当前用户与项目决定，不绑定个人偏好、特定电脑或全局管理工具。

## 第一次使用与可选个性化

- [环境与安装引导](skills/sdd-to-tdd-with-ddd/references/bootstrap.md)：先核对当前宿主和任务需要的能力；缺失时查找并列出 OpenSpec、Superpowers 的官方 GitHub 地址，读取当前宿主适用的安装文档；按已有授权代装，超出授权时只询问缺失部分。分别验证安装、发现／加载、接口和真实交接，再从原来的 change／步骤继续。需要用户操作时，明确说明“已就绪什么、还差什么、下一步做什么”。
- [可选个人版优化](skills/sdd-to-tdd-with-ddd/references/personalization.md)：仅由用户主动提出。先检测本次个性化所需的 Skill；必要 Skill 缺失时，提供核实过的官方 GitHub 地址，询问是否代装，并在获得授权后安装、验证可用性。随后询问希望囊括的项目或对话范围，申请相应的只读访问权限，再读取选定材料。按“可见文本筛选 → 相关原话与上下文精读 → 现有授权资料交叉核对 → 按项目、领域和参与方式提炼条件规则”生成独立个人候选，并借助已就绪的 `skill-creator` 等编写工具及官方规范校验。安装权限与历史访问权限分开；全账户访问以宿主实际能力为准，覆盖缺口如实记录，私人取证与公开包分开。

安装成功、宿主已发现、实际调用及完整交接是不同证据；文字引导和结构校验不能代替真实环境验证。

## 内容与验证

- [交接与产物职责](skills/sdd-to-tdd-with-ddd/references/handoffs.md)
- [26 类冲突的协调协议](skills/sdd-to-tdd-with-ddd/references/conflicts.md)
- [开发场景与工作方式](skills/sdd-to-tdd-with-ddd/references/modes.md)
- [借阅续期示例](examples/loan-renewal/README.md)
- [兼容性与限制](docs/compatibility.md)

使用 Python 3.11 及以上版本运行仓库检查：

```sh
python scripts/validate.py
```

这些检查验证文件、引用及示例行为；尚不证明模型稳定遵循全部指令，也不证明任意版本的组件都能自动衔接。验证范围见 [docs/validation.md](docs/validation.md)。

本项目采用 [MIT 许可证](LICENSE)，独立于上游项目，未捆绑其实现。欢迎通过具体、可复现的交接失败案例改进指引。
