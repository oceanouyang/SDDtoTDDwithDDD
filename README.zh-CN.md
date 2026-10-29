# SDDtoTDDwithDDD

[English README](README.md)

一个把 **SDD（规格驱动开发）→ TDD（测试驱动开发）** 与 **DDD（领域驱动设计）** 串联起来的通用 Agent Skill，同时用 BDD 的具体行为例子连接需求与验收。

它协调 OpenSpec、Superpowers 和领域建模流程之间的职责、产物及工作顺序，不是捆绑安装包，也不会凭空获得外部工具或自动调用其他 Skill。

## 分工与顺序

- **OpenSpec / SDD**：维护行为约定、本次变更范围及交付生命周期。
- **DDD / domain-modeling**：澄清术语、边界、规则归属与不变量，按项目复杂度建模。
- **BDD**：把需求落实为成功、失败和边界例子；Gherkin 与 Cucumber 都是可选工具。
- **Superpowers / TDD**：计划、实现、调试、评审及验证，用真实行为失败驱动实现。
- **协调 Skill**：传递正确资料、处理矛盾、让完成状态对应实际证据。

通常按“目标 → 领域含义 → 规格与例子 → 设计和计划 → 测试失败 → 最小实现 → 测试通过 → 回归和验收”推进。已有设计直接复用，小修复走轻量分支。

## 使用

通过你的 Agent 宿主支持的方式安装 `skills/sdd-to-tdd-with-ddd/` 目录，再按各自官方方式配置所需组件。支持 `$skill-name` 的宿主可使用：

```text
使用 $sdd-to-tdd-with-ddd 完成本次功能。
先读取现有规则、设计、规格与实现，确认本次范围，再按可验证增量实施。
```

仓库及展示名称为 **SDDtoTDDwithDDD**，内部 Skill 标识为 **sdd-to-tdd-with-ddd**。没有自动发现能力时，可以明确让 Agent 读取 [SKILL.md](skills/sdd-to-tdd-with-ddd/SKILL.md)。

通用版提供讲解、陪练、持续交付和只读调研等分支；具体语言、节奏、授权及技术栈由当前用户与项目决定，不绑定个人偏好、特定电脑或全局管理工具。

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
