---
type: simulink-block
title: 'Rectangular QAM TCM Encoder'
family: 'modulation'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / TCM'
documentation_page: 'rectangularqamtcmencoder'
documentation_source_path: 'ref/rectangularqamtcmencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Rectangular QAM TCM Encoder

## 端口

R2025b 中未提供文档。

## 参数

**Trellis structure**
:   包含卷积编码器网格描述的 MATLAB 结构体。

**Operation mode**
:   在 `Continuous` 模式（默认设置）下，模块在每帧结束时保留编码器状态，以供下一帧使用。

    在 `Truncated (reset every frame)` 模式下，模块独立处理每一帧。即，编码器状态在每帧开始时重置为全零状态。

    在 `Terminate trellis by appending bits` 模式下，模块独立处理每一帧。对于每个输入帧，使用额外比特在帧结束时将编码器状态设置为全零状态。输出长度由 y=n⋅(x+s)/k 给出，其中 *x* 是输入比特数，s=constraint length−1（或者，在存在多个约束长度的情况下，*s* =`sum(ConstraintLength(i)-1)`）。
    该模块对列向量输入信号支持此模式。

    在 `Reset on nonzero input via port` 模式下，模块具有一个额外的输入端口，标记为 `Rst`。当 `Rst` 输入非零时，编码器重置为全零状态。

**M-ary number**
:   信号星座图中的点数。

**Output data type**
:   模块的输出类型可指定为 `single` 或 `double`。默认情况下，模块将其设置为 `double`。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

对二进制数据进行卷积编码，并使用 QAM 方法进行调制

Rectangular QAM TCM Encoder 模块通过对二进制输入信号进行卷积编码，并将结果映射到 QAM 信号星座图，实现网格编码调制 (TCM)。

**M-ary number** 参数是信号星座图中的点数，也等于卷积编码器可能输出的符号数。（也就是说，对于码率为 k/n 的卷积码，log2(**M-ary number**) 等于 n。）

### 输入信号和输出信号

如果网格结构所描述的卷积编码器表示码率为 *k*/*n* 的编码，则 Rectangular QAM TCM Encoder 模块的输入必须是二进制列向量，其长度为 *L*\**k*，其中 *L* 为某个正整数。

Rectangular QAM TCM Encoder 模块的输出是长度为 *L* 的复数列向量。

### 指定编码器

要定义卷积编码器，请使用 **Trellis structure** 参数。此参数是一个 MATLAB 结构体，其格式在“卷积码的网格描述”中介绍。您可以通过两种方式使用此参数字段：

- 如果要使用编码器的约束长度、生成多项式以及可能存在的反馈连接多项式来指定编码器，请在 **Trellis structure** 字段中使用 `poly2trellis` 命令。例如，要使用约束长度为 7、码生成多项式为 171 和 133（八进制数）、反馈连接为 171（八进制）的编码器，请将 **Trellis structure** 参数设置为

  `poly2trellis(7,[171 133],171)`
- 如果 MATLAB 工作区中有一个包含网格结构的变量，请将其名称输入为 **Trellis structure** 参数。这种方式更快，因为与上一项目符号中的用法相比，它可使 Simulink 在每次仿真开始时花费更少的时间来更新框图。

编码器寄存器初始处于全零状态。您可以将编码器配置为在仿真过程中将其寄存器重置为全零状态。为此，请将 `Operation mode` 设置为 **Reset on nonzero input via port**。随后，模块会打开第二个输入端口，标记为 `Rst`。`Rst` 端口上的信号是标量信号。当该信号非零时，编码器会在处理第一个输入端口上的数据之前重置。

### 信号星座图

网格编码调制技术将星座图划分为称为陪集的子集，以使每个陪集中点对之间的最小距离最大化。该模块根据您为 **M-ary number** 参数选择的值，在内部形成有效的划分。

下图显示当 **M-ary number** 为 `16`、`32` 和 `64` 时，模块使用的带标签的集合划分信号星座图。对于其他大小的星座图，请参阅 Biglieri, E., D. Divsalar, P. J. McLane and M. K. Simon，*Introduction to Trellis-Coded Modulation with Applications*，New York，Macmillan，1991。

### 编码增益

在存在 AWGN 的情况下，采用多相网格码可实现相对于未编码情况 3 至 6 decibels 的编码增益。有关详细信息，请参阅 Biglieri, E., D. Divsalar, P. J. McLane and M. K. Simon，*Introduction to Trellis-Coded Modulation with Applications*，New York，Macmillan，1991。
