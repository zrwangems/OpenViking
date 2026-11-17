---
type: simulink-block
title: 'Convolutional Deinterleaver'
family: 'interleaving'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Interleaving / Convolutional'
documentation_page: 'convolutionaldeinterleaver'
documentation_source_path: 'ref/convolutionaldeinterleaver.html'
language: zh-CN
chinese_source: worker-translation
---

# Convolutional Deinterleaver

## 端口

R2025b 中未提供相关文档。

## 参数

**移位寄存器行数**
:   模块内部使用的移位寄存器数量。

**寄存器长度步长**
:   各相邻移位寄存器之间的符号容量差，其中最后一个寄存器容纳零个符号。

**初始条件**
:   指示仿真开始时填充每个移位寄存器的值（最后一个移位寄存器除外，该寄存器的延迟为零）。

    - 当为**初始条件**选择标量值时，该值将填充所有移位寄存器（最后一个除外）
    - 当选择长度等于**移位寄存器行数**参数的列向量时，每个元素将填充对应的移位寄存器。

    **初始条件**参数的第一个元素的值并不重要，因为最后一个移位寄存器的延迟为零。

## 所属库

R2025b 中未提供相关文档。

## 模块特性

R2025b 中未提供相关文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

可以使用基于移位寄存器的实现或基于 RAM 的实现，为 Convolutional Deinterleaver 模块生成 HDL 代码。

Convolutional Deinterleaver 模块的默认实现基于移位寄存器。要禁止生成复位逻辑，请将实现参数 `ResetType` 设置为 `'none'`。当将 `ResetType` 设置为 `'none'` 时，复位不会应用于移位寄存器。

当寄存器尚未完全填满时，在初始阶段的若干采样点内，Simulink® 与生成的代码之间会出现不匹配。为避免测试平台出现虚假错误，请确定填满移位寄存器所需的采样点数，并相应地设置**忽略输出数据检查（采样点数）**选项。（如果您使用命令行界面，可以为此使用 `IgnoreDataChecking` 属性。）

为 Convolutional Deinterleaver 模块选择 `RAM` 实现时，HDL Coder 将使用 RAM 资源，而不是移位寄存器。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中的现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入生成代码中的输入流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入生成代码中的输出流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ResetType** | 禁止生成复位逻辑。默认值为 `default`，该值会生成复位逻辑。另请参阅 ResetType (HDL Coder)。 |

**限制**

选择 `RAM` 实现时：

- 输入或输出信号均不支持 Double 或 single 数据类型。
- 必须将模块的**初始条件**设置为零。
- 至少需要两行交织。

## 版本历史

**在 R2006a 之前推出**

## 描述

恢复使用移位寄存器置换的符号顺序

Convolutional Deinterleaver 模块可恢复使用 Convolutional Interleaver 模块交织的信号。该模块内部使用一组移位寄存器。两个模块中的参数必须具有相同的值。有关延迟的信息，请参阅“卷积交织与解交织的延迟”。

此模块接受标量或列向量输入信号，该信号可以是实信号或复信号。输出信号具有与输入信号相同的采样时间。

此模块接受以下数据类型：`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和 fixed-point。
