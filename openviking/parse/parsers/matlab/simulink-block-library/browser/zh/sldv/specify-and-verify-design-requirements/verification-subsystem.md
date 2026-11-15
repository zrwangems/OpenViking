---
type: simulink-block
title: 'Verification Subsystem'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2025b
official_category: 'Specify and Verify Design Requirements'
documentation_page: 'verificationsubsystem'
documentation_source_path: 'ref/verificationsubsystem.html'
language: zh-CN
chinese_source: official
---

# Verification Subsystem

## 端口

R2025b 官方文档未提供。

## 参数

R2025b 官方文档未提供。

## 所属库

Simulink Design Verifier / Verification Utilities

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和合成逻辑的附加配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| **无 HDL** | 不要为该模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制不相关逻辑的移除。默认值为 `off`，这意味着未连接的逻辑不会保留在 HDL 代码中。有关更多详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

## 版本历史

**在 R2007b 中推出**

## 描述

指定证明或测试目标而不影响仿真结果或生成的代码

这个模块是一个 Subsystem 模块，它经过预先配置，可作为创建子系统的起点，该子系统指定与 Simulink® Design Verifier™ 软件一起使用的证明或测试目标。

Simulink Coder™ 软件在代码生成过程中忽略 Verification Subsystem 模块，就好像子系统不存在一样。Verification Subsystem 模块允许您将 Simulink Design Verifier 组件添加到模型中，而不会影响其生成的代码。

**注意**

如果 Verification Subsystem 模块包含依赖于绝对时间的模块，并且您选择基于 ERT 的目标 (Simulink Coder)进行代码生成，请将软件环境设置为绝对时间。打开“配置参数”对话框。在**软件环境**下的 **代码生成** > **接口**窗格中，选择**绝对时间**。不要选择**连续时间**。有关此设置的更多信息，请参阅 支持：绝对时间 (Embedded Coder)。

在收集模型覆盖率时，Simulink Coverage™ 软件仅记录 Verification Subsystem 模块中 Simulink Design Verifier 模块的覆盖率；它不会记录验证子系统中任何其他模块的覆盖率。

要在您的模型中创建验证子系统：

1. 将 Simulink Design Verifier 库中的 Verification Subsystem 模块复制到您的模型中。
2. 双击打开 Verification Subsystem 模块。
3. 在验证子系统窗口中，添加指定证明或测试目标的模块。使用 Inport 模块来表示来自子系统外部的输入。

Simulink Design Verifier 库中的 Verification Subsystem 模块已预先配置为与 Simulink Design Verifier 软件一起使用。Verification Subsystem 模块必须：

- 不包含 Outport 模块。
- 启用其**视为原子单元**参数。
- 将其**封装类型**参数指定为 `VerificationSubsystem`。

如果您更改 Verification Subsystem 模块以致前面的条件不满足，则 Simulink Design Verifier 软件会显示警告。
