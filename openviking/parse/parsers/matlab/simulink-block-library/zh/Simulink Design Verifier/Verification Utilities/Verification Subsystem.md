---
type: simulink-block
title: 'Verification Subsystem'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2025b
official_category: 'Verification Utilities'
documentation_page: 'verificationsubsystem'
documentation_source_path: 'ref/verificationsubsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Verification Subsystem

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simulink Design Verifier / Verification Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了额外的配置选项，这些选项会影响 HDL 实现和综合逻辑。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `No HDL` | 不为该模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制未连接逻辑的移除。默认值为 `off`，这意味着未连接的逻辑不会保留在 HDL 代码中。有关更多详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

## 版本历史

**在 R2007b 中引入**

## 描述

在不影响仿真结果或生成代码的情况下指定证明或测试目标

该模块是一个子系统模块，已预配置为用作创建子系统的起点，该子系统用于指定供 Simulink® Design Verifier™ 软件使用的证明或测试目标。

Simulink Coder™ 软件在代码生成期间忽略 Verification Subsystem 模块，其行为如同这些子系统不存在一样。Verification Subsystem 模块允许您向模型添加 Simulink Design Verifier 组件，而不影响其生成的代码。

**注意**

如果 Verification Subsystem 模块包含依赖于绝对时间的模块，并且您为代码生成选择了基于 ERT 的目标（Simulink Coder），请将软件环境设置为绝对时间。打开“配置参数”对话框。在 **代码生成** > **接口** 窗格中的 **软件环境** 下，选择 **absolute time**。不要选择 **continuous time**。有关此设置的更多信息，请参阅 Support: absolute time (Embedded Coder)。

在收集模型覆盖率时，Simulink Coverage™ 软件仅记录 Verification Subsystem 模块中 Simulink Design Verifier 模块的覆盖率；它不记录 Verification Subsystem 中任何其他模块的覆盖率。

要在模型中创建 Verification Subsystem：

1. 将 Verification Subsystem 模块从 Simulink Design Verifier 库复制到您的模型中。
2. 通过双击打开 Verification Subsystem 模块。
3. 在 Verification Subsystem 窗口中，添加指定证明或测试目标的模块。使用 Inport 模块表示来自子系统外部的输入。

Simulink Design Verifier 库中的 Verification Subsystem 模块已预配置为与 Simulink Design Verifier 软件配合使用。Verification Subsystem 模块必须：

- 不包含任何 Outport 模块。
- 启用其 **Treat as Atomic Unit** 参数。
- 将其 **Mask type** 参数指定为 `VerificationSubsystem`。

如果您更改 Verification Subsystem 模块以致不满足上述条件，Simulink Design Verifier 软件将显示警告。
