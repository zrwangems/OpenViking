---
type: simulink-block
title: 'M-DPSK Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PSK'
documentation_page: 'mdpskdemodulatorbaseband'
documentation_source_path: 'ref/mdpskdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# M-DPSK Demodulator Baseband

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

对 DPSK 调制数据进行解调

M-DPSK Demodulator Baseband 模块对采用 M 元差分相移键控方法调制的信号进行解调。输入是已调制信号的基带表示。该模块的输入和输出均为离散时间信号。该模块接受标量值或列向量输入信号。有关每个模块端口支持的数据类型的信息，请参阅本页中的“支持的数据类型”表。

**M-ary number** 参数 M 是可能紧跟在给定输出符号之后的输出符号的数量。该模块将当前符号与前一个符号进行比较。由于没有前一个符号，该模块的第一个输出为初始值零（如果 **Output type** 参数设置为 `Bit`，则为一组零）。

### 整数值信号和二进制值信号

如果将 **Output type** 参数设置为 `Integer`，则模块将相位差

θ + 2πk/M

解调为 *k*，其中 θ 表示 **Phase rotation** 参数，*k* 表示介于 `0` 和 *M*-1 之间的整数。

当 **Output type** 参数设置为 `Bit` 时，模块输出表示整数的二进制值信号。模块使用一组 *K* = log2(*M*) 个比特来表示每个整数，其中 *K* 表示每个符号的比特数。输出向量的长度必须是 *K* 的整数倍。

在二进制输出模式下，符号可以采用二进制解映射或 Gray 解映射。**Constellation ordering** 参数指示模块如何将整数映射到相应的一组 *K* 个输出比特。有关详细信息，请参阅 M-DPSK Modulator Baseband 和 M-PSK Modulator Baseband 模块的参考页。
