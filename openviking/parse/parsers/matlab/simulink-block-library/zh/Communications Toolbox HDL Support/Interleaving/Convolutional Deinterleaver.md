---
type: simulink-block
title: 'Convolutional Deinterleaver'
family: 'communications-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Interleaving'
documentation_page: 'convolutionaldeinterleaver'
documentation_source_path: '../comm/ref/convolutionaldeinterleaver.html'
language: zh-CN
chinese_source: worker-translation
---

# Convolutional Deinterleaver

## 端口

R2025b 中未记录。

## 参数

**Rows of shift registers**
:   模块内部使用的移位寄存器数量。

**Register length step**
:   每个连续移位寄存器符号容量的差值，其中最后一个寄存器保存零个符号。

**Initial conditions**
:   指示仿真开始时填充每个移位寄存器的值（最后一个移位寄存器除外，其延迟为零）。

    - 当为 **Initial conditions** 选择标量值时，该值填充所有移位寄存器（最后一个除外）
    - 当选择长度等于 **Rows of shift registers** 参数的列向量时，每个条目填充对应的移位寄存器。

    **Initial conditions** 参数第一个元素的值不重要，因为最后一个移位寄存器的延迟为零。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

您可以使用基于移位寄存器的实现或基于 RAM 的实现为 Convolutional Deinterleaver 模块生成 HDL 代码。

Convolutional Deinterleaver 模块的默认实现是基于移位寄存器的。要抑制复位逻辑的生成，请将实现参数 `ResetType` 设置为 `'none'`。当您将 `ResetType` 设置为 `'none'` 时，复位不会应用于移位寄存器。

当寄存器未完全加载时，在初始阶段的某些采样数内，Simulink® 与生成的代码之间会出现不匹配。为避免虚假的测试平台错误，请确定填充移位寄存器所需的采样数。相应地设置 **Ignore output data checking (number of samples)** 选项。（如果您使用的是命令行接口，可以为此目的使用 `IgnoreDataChecking` 属性。）

当您为 Convolutional Deinterleaver 模块选择 `RAM` 实现时，HDL Coder 使用 RAM 资源而不是移位寄存器。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ResetType** | 抑制复位逻辑的生成。默认值为 `default`，即生成复位逻辑。另请参阅 ResetType (HDL Coder)。 |

**限制**

当您选择 `RAM` 实现时：

- 输入和输出信号均不支持双精度或单精度数据类型。
- 必须将模块的 **Initial conditions** 设置为零。
- 至少需要两行交织。

## 版本历史

**在 R2006a 之前引入**

## 描述

恢复使用移位寄存器置换的符号的顺序

Convolutional Deinterleaver 模块恢复使用 Convolutional Interleaver 模块交织的信号。在内部，此模块使用一组移位寄存器。两个模块中的参数必须具有相同的值。有关延迟的信息，请参阅 Delays of Convolutional Interleaving and Deinterleaving。

此模块接受标量或列向量输入信号，可以是实数或复数。输出信号具有与输入信号相同的采样时间。

此模块接受以下数据类型：`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single`、`double` 和定点。
