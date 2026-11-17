---
type: simulink-block
title: 'General Multiplexed Interleaver'
family: 'communications-toolbox-hdl-support'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Interleaving'
documentation_page: 'generalmultiplexedinterleaver'
documentation_source_path: 'ref/generalmultiplexedinterleaver.html'
language: zh-CN
chinese_source: worker-translation
---

# General Multiplexed Interleaver

## 端口

R2025b 中未记录。

## 参数

**Interleaver delay (samples)**
:   一个列向量，列出每个移位寄存器可容纳的符号数。该向量的长度即为移位寄存器的数量。（在基于样本的模式下，它也可以是行向量。）

**Initial conditions**
:   仿真开始时填充每个移位寄存器的值。

    如果 **Initial conditions** 是标量，则其值填充所有移位寄存器。如果 **Initial conditions** 是列向量，则每个条目填充对应的移位寄存器。（在基于样本的模式下，**Initial conditions** 也可以是行向量。）如果某个给定的移位寄存器具有零延迟，则 **Initial conditions** 向量中对应条目的值无关紧要。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了额外的配置选项，这些选项会影响 HDL 实现和综合逻辑。

**HDL 架构**

General Multiplexed Interleaver 模块的实现基于移位寄存器。如果要抑制复位逻辑的生成，请将实现参数 `ResetType` 设置为 `'none'`。

当您将 `ResetType` 设置为 `'none'` 时，复位不会应用于移位寄存器。在初始阶段，当寄存器未完全加载时，Simulink® 与生成的代码之间会在若干采样点上出现不匹配。为避免测试平台出现虚假错误，请确定填满移位寄存器所需的采样数。然后，相应地设置 **Ignore output data checking (number of samples)** 选项。（如果您使用的是命令行接口，可以为此使用 `IgnoreDataChecking` 属性。）

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

使用具有指定延迟的一组移位寄存器对输入符号进行置换

General Multiplexed Interleaver 模块对输入信号中的符号进行置换。在内部，它使用一组移位寄存器，每个移位寄存器都有自己的延迟值。

该模块接受标量或列向量输入信号，信号可以是实数或复数。输入和输出信号具有相同的采样时间。

该模块可以接受数据类型 `int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和定点。输出信号的数据类型与输入信号相同。
