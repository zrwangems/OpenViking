---
type: simulink-block
title: 'Convolutional Interleaver'
family: 'interleaving'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Interleaving / Convolutional'
documentation_page: 'convolutionalinterleaver'
documentation_source_path: '../comm/ref/convolutionalinterleaver.html'
language: zh-CN
chinese_source: worker-translation
---

# Convolutional Interleaver

## 端口

R2025b 中未提供文档。

## 参数

**移位寄存器的行数**
:   模块内部使用的移位寄存器数量。

**寄存器长度步长**
:   每个后续移位寄存器比前一个寄存器多容纳的符号数量，其中第一个寄存器容纳零个符号。

**初始条件**
:   仿真开始时填充每个移位寄存器的值。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的其他配置选项。

**HDL 架构**

您可以使用基于移位寄存器的实现或基于 RAM 的实现，为 Convolutional Interleaver 模块生成 HDL 代码。

Convolutional Interleaver 模块的默认实现基于移位寄存器。要抑制复位逻辑的生成，请将实现参数 `ResetType` 设置为 `'none'`。将 `ResetType` 设置为 `'none'` 后，不会对移位寄存器应用复位。

当寄存器尚未完全填满时，在初始阶段的若干采样点内，Simulink® 与生成的代码之间会出现不匹配。为避免测试平台误报错误，请确定填满移位寄存器所需的采样点数量，并相应地设置 **忽略输出数据检查（采样点数）** 选项。（如果您使用命令行界面，可以为此使用 `IgnoreDataChecking` 属性。）

为 Convolutional Interleaver 模块选择 `RAM` 实现时，HDL Coder 会使用 RAM 资源，而不是移位寄存器。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中的现有延迟而放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入生成的代码中的输入流水线级数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入生成的代码中的输出流水线级数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ResetType** | 抑制复位逻辑的生成。默认值为 `default`，即生成复位逻辑。另请参阅 ResetType (HDL Coder)。 |

**限制**

选择 `RAM` 实现时：

- 输入或输出信号均不支持 double 或 single 数据类型。
- 必须将模块的 **初始条件** 设置为零。
- 至少需要两行交织。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用一组移位寄存器对输入符号进行置换

Convolutional Interleaver 模块对输入信号中的符号进行置换。它在内部使用一组移位寄存器。有关延迟的信息，请参阅“卷积交织和解交织的延迟”。

**初始条件** 参数指定在仿真开始时填充每个移位寄存器的值（第一个移位寄存器除外，其延迟为零）。如果 **初始条件** 是标量，则其值将填充除第一个移位寄存器之外的所有移位寄存器；如果 **初始条件** 是列向量，且其长度等于 **移位寄存器的行数** 参数值，则每个元素填充对应的移位寄存器。**初始条件** 参数的第一个元素的值并不重要，因为第一个移位寄存器的延迟为零。

此模块接受标量或列向量输入信号，该信号可以是实数或复数。输出信号与输入信号具有相同的采样时间。

该模块可接受 `int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和 fixed-point 数据类型。此输出信号的数据类型将与输入信号的数据类型相同。
