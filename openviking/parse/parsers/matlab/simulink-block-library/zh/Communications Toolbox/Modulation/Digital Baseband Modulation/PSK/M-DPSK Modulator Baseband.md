---
type: simulink-block
title: 'M-DPSK Modulator Baseband'
family: 'modulation'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PSK'
documentation_page: 'mdpskmodulatorbaseband'
documentation_source_path: 'ref/mdpskmodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# M-DPSK Modulator Baseband

## 端口

R2025b 中未提供文档。

## 参数

R2025b 中未提供文档。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用 M 元差分相移键控方法进行调制

M-DPSK Modulator Baseband 模块使用 M 元差分相移键控方法进行调制。输出是调制信号的基带表示。**M-ary number** 参数 M 是可以紧跟在给定输出符号之后的可能输出符号的数量。

输入必须是离散时间信号。对于整数输入，模块可以接受 `int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`single` 和 `double` 数据类型。对于比特输入，模块可以接受 `int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single` 和 `double` 数据类型。

输入可以是比特或整数，它们通过二进制映射或格雷映射转换为符号。

此模块接受列向量输入信号。对于比特输入，输入宽度必须是每符号比特数的整数倍。

### 整数值信号和二进制值信号

如果将 **Input type** 参数设置为 `Integer`，则有效输入值是 0 到 M-1 之间的整数。在这种情况下，输入可以是标量或基于帧的列向量。如果第一个输入为 k1，则调制符号为

exp(jθ+j2πk1m)

其中，θ 表示 **Phase rotation** 参数。如果后续输入为 *k*，则调制符号为

exp(jθ+j2πkm)⋅(前一个调制符号)

当将 **Input type** 参数设置为 `Bit` 时，模块接受表示整数的二进制值输入。模块将二进制值信号按每组 *K* = log2(*M*) 个比特进行分组，其中 *K* 是每符号的比特数，*M* 是调制阶数。输入向量长度必须是 *K* 的整数倍。在此配置中，模块接受一组 *K* 个比特，并将该组比特映射为模块输出的一个符号。模块为每组 *K* 个比特输出一个调制符号。

输入可以是长度为 *K* 的整数倍的列向量。

在二进制输入模式下，**Constellation ordering** 参数指示模块如何将一组 *K* 个输入比特映射到相应的相位差。`Binary` 选项使用二进制编码的整数映射，而 `Gray` 选项使用相位差的格雷编码分配。例如，下表列出了三比特输入在 `Binary` 和 `Gray` 两种选项下的相位差分配。θ 是 **Phase rotation** 参数。相位差是前一个符号与当前符号之间的相位差。

| 当前输入 | 二进制编码的相位差 | 格雷编码的相位差 |
| --- | --- | --- |
| [0 0 0] | jθ | jθ |
| [0 0 1] | jθ + jπ/4 | jθ + jπ/4 |
| [0 1 0] | jθ + jπ2/4 | jθ + jπ3/4 |
| [0 1 1] | jθ + jπ3/4 | jθ + jπ2/4 |
| [1 0 0] | jθ + jπ4/4 | jθ + jπ7/4 |
| [1 0 1] | jθ + jπ5/4 | jθ + jπ6/4 |
| [1 1 0] | jθ + jπ6/4 | jθ + jπ4/4 |
| [1 1 1] | jθ + jπ7/4 | jθ + jπ5/4 |

有关 `Binary` 和 `Gray` 选项的更多详细信息，请参阅 M-PSK Modulator Baseband 模块的参考页。该模块的信号星座图对应于本模块的相位差排列。
