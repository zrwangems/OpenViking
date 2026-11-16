---
type: simulink-block
title: 'M-PSK TCM Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Trellis-Coded Modulation'
documentation_page: 'mpsktcmencoder'
documentation_source_path: 'ref/mpsktcmencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# M-PSK TCM Encoder

## 端口

R2025b 中未提供文档。

## 参数

**网格结构**
:   包含卷积编码器网格描述的 MATLAB 结构体。

**操作模式**
:   在 `Continuous` 模式（默认设置）下，模块会在每个帧结束时保留编码器状态，以供下一帧使用。

    在 `Truncated (reset every frame)` 模式下，模块独立处理每个帧。即编码器状态在每个帧开始时重置为全零状态。

    在 `Terminate trellis by appending bits` 模式下，模块独立处理每个帧。对于每个输入帧，使用额外比特在帧结束时将编码器状态设置为全零状态。输出长度由 y=n⋅(x+s)/k 给出，其中 *x* 是输入比特数，且 *s* 为约束长度减 1（或者，在存在多个约束长度的情况下，*s* =`sum(ConstraintLength(i)-1)`）。对于列向量输入信号，模块支持此模式。

    在 `Reset on nonzero input via port` 模式下，模块具有一个额外的输入端口，标签为 `Rst`。当 `Rst` 输入非零时，编码器重置为全零状态。

**M 元数**
:   信号星座图中的点数。

**输出数据类型**
:   模块的输出类型可指定为 `single` 或 `double`。默认情况下，模块将其设置为 `double`。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

对二进制数据进行卷积编码，并使用 PSK 方法进行调制

M-PSK TCM Encoder 模块通过对二进制输入信号进行卷积编码，并将结果映射到 PSK 信号星座图，实现网格编码调制 (TCM)。

**M 元数**参数是信号星座图中的点数，它也等于卷积编码器可能输出的符号数。（也就是说，对于码率为 k/n 的卷积码，log2(**M 元数**) 等于 n。）

### 输入信号和输出信号

如果网格结构所描述的卷积编码器表示码率为 *k*/*n* 的编码，则模块输入信号必须是长度为 *L*\**k* 的二进制列向量，其中 *L* 为某个正整数。

此模块接受二值输入信号。输出信号是长度为 *L* 的复数列向量。

### 指定编码器

要定义卷积编码器，请使用**网格结构**参数。此参数是一个 MATLAB® 结构体，其格式在“卷积码的网格描述”中介绍。您可以通过两种方式使用此参数字段：

- 如果要使用编码器的约束长度、生成多项式以及可能的反馈连接多项式来指定编码器，请在**网格结构**字段中使用 `poly2trellis` 命令。例如，要使用约束长度为 7、代码生成多项式为 171 和 133（八进制数）、反馈连接为 171（八进制）的编码器，请将**网格结构**参数设置为

  `poly2trellis(7,[171 133],171)`
- 如果 MATLAB 工作区中有一个包含网格结构的变量，则将其名称输入为**网格结构**参数。这种方式速度更快，因为与上一项目符号中的用法相比，它使 Simulink® 软件在每次仿真开始时花费更少的时间来更新框图。

编码器寄存器初始为全零状态。您可以配置编码器，使其在仿真过程中将寄存器重置为全零状态。为此，请将 `Operation mode` 设置为 **Reset on nonzero input via port**。此时，模块会打开第二个输入端口，标签为 `Rst`。`Rst` 端口处的信号是标量信号。当该信号非零时，编码器会在处理第一个输入端口的数据之前重置。

### 信号星座图

网格编码调制技术将星座图划分为称为陪集的子集，以使每个陪集中各点对之间的最小距离最大化。此模块根据您为 **M 元数**参数选择的值，在内部形成有效的划分。

下图显示了当 **M 元数**为 8 时模块使用的带标签的集合划分信号星座图。对于其他大小的星座图，请参阅 [1]。

### 编码增益

在存在 AWGN 的情况下，采用多相网格码可实现相对于未编码情况 3 至 6 decibels 的编码增益 [3]。
