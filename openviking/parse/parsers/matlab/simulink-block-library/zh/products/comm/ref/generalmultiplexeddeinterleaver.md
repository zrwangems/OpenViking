---
type: simulink-block
title: 'General Multiplexed Deinterleaver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Interleaving / Convolutional'
documentation_page: 'generalmultiplexeddeinterleaver'
documentation_source_path: 'ref/generalmultiplexeddeinterleaver.html'
language: zh-CN
chinese_source: worker-translation
---

# General Multiplexed Deinterleaver

## 端口

未在 R2025b 中记录。

## 参数

未在 R2025b 中记录。

## 所属库

未在 R2025b 中记录。

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了额外的配置选项，这些选项会影响 HDL 实现和综合逻辑。

**HDL 架构**

General Multiplexed Deinterleaver 模块的实现基于移位寄存器。如果要抑制复位逻辑的生成，请将实现参数 `ResetType` 设置为 `none`。

当您将 `ResetType` 设置为 `none` 时，复位不会应用于移位寄存器。当寄存器未完全加载时，在初始阶段的一些样本中，Simulink® 与生成的代码之间会出现不匹配。为避免虚假的测试平台错误，请确定填满移位寄存器所需的样本数。相应地设置 **Ignore output data checking (number of samples)** 选项。（如果您使用命令行界面，可以为此使用 `IgnoreDataChecking` 属性。）

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ResetType** | 抑制复位逻辑生成。默认值为 `default`，它会生成复位逻辑。另请参阅 ResetType (HDL Coder)。 |

## 版本历史

**R2006a 之前引入**

## 描述

使用指定延迟的移位寄存器恢复符号的顺序
