---
type: simulink-block
title: 'General Multiplexed Deinterleaver'
family: 'communications-toolbox-hdl-support'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Interleaving'
documentation_page: 'generalmultiplexeddeinterleaver'
documentation_source_path: 'ref/generalmultiplexeddeinterleaver.html'
language: zh-CN
chinese_source: worker-translation
---

# General Multiplexed Deinterleaver

## 端口

R2025b 中未记录。

## 参数

**Interleaver delay (samples)**
:   一个向量，列出对应交织器的每个移位寄存器中可容纳的符号数量。该向量的长度即为移位寄存器的数量。

**Initial conditions**
:   仿真开始时填充每个移位寄存器的值。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

General Multiplexed Deinterleaver 模块的实现基于移位寄存器。如果要抑制复位逻辑的生成，请将实现参数 `ResetType` 设置为 `none`。

当将 `ResetType` 设置为 `none` 时，复位不会应用于移位寄存器。当寄存器未完全加载时，在初始阶段的若干采样内，Simulink® 与生成的代码之间会出现不匹配。为避免虚假的测试平台错误，请确定填满移位寄存器所需的采样数。相应地设置 **Ignore output data checking (number of samples)** 选项。（如果使用命令行接口，可以为此使用 `IgnoreDataChecking` 属性。）

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ResetType** | 抑制复位逻辑的生成。默认值为 `default`，即生成复位逻辑。另请参阅 ResetType (HDL Coder)。 |

## 版本历史

**在 R2006a 之前推出**

## 描述

使用指定延迟的移位寄存器恢复符号的顺序

General Multiplexed Deinterleaver 模块恢复使用 General Multiplexed Interleaver 模块交织的序列的原始顺序。

在典型用法中，两个模块中的参数具有相同的值。因此，**Interleaver delay** 参数 *V* 指定对应*交织器*中每个移位寄存器的延迟，使得解交织器的移位寄存器的延迟实际上为 `max(V)-V`。

该模块接受标量或列向量输入信号，可以是实数或复数。输出信号与输入信号具有相同的采样时间。

该模块可以接受数据类型 `int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和定点。输出的数据类型将与输入信号的数据类型相同。
