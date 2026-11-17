---
type: simulink-block
title: 'General Multiplexed Interleaver'
family: 'interleaving'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Interleaving / Convolutional'
documentation_page: 'generalmultiplexedinterleaver'
documentation_source_path: '../comm/ref/generalmultiplexedinterleaver.html'
language: zh-CN
chinese_source: worker-translation
---

# General Multiplexed Interleaver

## 端口

R2025b 中未提供相关文档。

## 参数

**交织器延迟 (samples)**
:   一个列向量，列出每个移位寄存器可容纳的符号数。该向量的长度等于移位寄存器的数量。（在基于采样的模式下，它也可以是行向量。）

**初始条件**
:   仿真开始时填入每个移位寄存器的值。

    如果 **初始条件** 是标量，则其值将填入所有移位寄存器。如果 **初始条件** 是列向量，则每个元素将填入对应的移位寄存器。（在基于采样的模式下，**初始条件** 也可以是行向量。）如果某个移位寄存器的延迟为零，则 **初始条件** 向量中对应元素的值无关紧要。

## 所属库

R2025b 中未提供相关文档。

## 模块特性

R2025b 中未提供相关文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的其他配置选项。

**HDL 架构**

General Multiplexed Interleaver 模块采用基于移位寄存器的实现。如果要抑制复位逻辑的生成，请将实现参数 `ResetType` 设置为 `'none'`。

当 `ResetType` 设置为 `'none'` 时，不会对移位寄存器应用复位。在初始阶段，寄存器尚未完全加载，Simulink® 与生成的代码之间会在若干采样内出现不匹配。为避免测试平台出现虚假错误，请确定填满移位寄存器所需的采样数。然后，相应地设置 **忽略输出数据检查（采样数）** 选项。（如果您使用的是命令行界面，可以使用 `IgnoreDataChecking` 属性来实现此目的。）

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟而放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入到生成的代码中的输入流水线级数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入到生成的代码中的输出流水线级数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ResetType** | 抑制复位逻辑的生成。默认值为 `default`，此时会生成复位逻辑。另请参阅 ResetType (HDL Coder)。 |

## 版本历史

**在 R2006a 之前推出**

## 描述

使用一组具有指定延迟的移位寄存器对输入符号进行置换

General Multiplexed Interleaver 模块对输入信号中的符号进行置换。在内部，它使用一组移位寄存器，每个移位寄存器都有自己的延迟值。

此模块接受标量或列向量输入信号，该信号可以是实信号或复信号。输入和输出信号具有相同的采样时间。

此模块可接受 `int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和 fixed-point 数据类型。输出信号的数据类型与输入信号相同。
