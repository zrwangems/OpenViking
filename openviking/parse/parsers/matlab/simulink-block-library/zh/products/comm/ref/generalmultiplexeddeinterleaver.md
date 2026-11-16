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

R2025b 中未提供相关文档。

## 参数

**交织器延迟 (samples)**
:   一个向量，列出对应交织器的每个移位寄存器可容纳的符号数量。该向量的长度等于移位寄存器的数量。

**初始条件**
:   仿真开始时填充到每个移位寄存器中的值。

## 所属库

R2025b 中未提供相关文档。

## 模块特性

R2025b 中未提供相关文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

General Multiplexed Deinterleaver 模块的实现基于移位寄存器。如果要禁止生成复位逻辑，请将实现参数 `ResetType` 设置为 `none`。

当 `ResetType` 设置为 `none` 时，不会将复位应用于移位寄存器。当寄存器未完全加载时，在初始阶段，Simulink® 与生成代码之间会在若干采样点出现不匹配。为避免测试平台出现虚假错误，请确定填满移位寄存器所需的样本数，并相应地设置 **忽略输出数据检查（样本数）** 选项。（如果您使用命令行界面，可以为此使用 `IgnoreDataChecking` 属性。）

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计中移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入生成代码中的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入生成代码中的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ResetType** | 禁止生成复位逻辑。默认值为 `default`，即生成复位逻辑。另请参阅 ResetType (HDL Coder)。 |

## 版本历史

**在 R2006a 之前推出**

## 描述

使用具有指定延迟的移位寄存器恢复符号的顺序

General Multiplexed Deinterleaver 模块可恢复使用 General Multiplexed Interleaver 模块交织后的序列的原始顺序。

在典型用法中，两个模块中的参数具有相同的值。因此，**交织器延迟**参数 *V* 指定的是对应*交织器*中各移位寄存器的延迟，所以解交织器移位寄存器的实际延迟为 `max(V)-V`。

该模块接受标量或列向量输入信号，该信号可以是实信号或复信号。输出信号与输入信号具有相同的采样时间。

该模块可以接受 `int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和 fixed-point 数据类型。输出的数据类型将与输入信号的数据类型相同。
