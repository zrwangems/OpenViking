---
type: simulink-block
title: 'CPFSK Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / CPM'
documentation_page: 'cpfskmodulatorbaseband'
documentation_source_path: 'ref/cpfskmodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# CPFSK Modulator Baseband

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**M-ary number**
:   字母表的大小。

**输入类型**
:   指示输入由整数还是比特组组成。

**Symbol set ordering**
:   确定模块如何将每组输入比特映射到对应的整数。此字段仅在 **输入类型** 设置为 `Bit` 时有效。

**Modulation index**
:   指定调制指数 {hi}。默认值为 `0.5`。此属性的值必须为实数、非负标量或列向量。

    此模块支持多 h **Modulation index**。有关详细信息，请参阅 CPM Modulator Baseband。

**Phase offset (rad)**
:   输出波形的初始相位，以弧度为单位。

**Samples per symbol**
:   模块为输入中的每个整数或二进制字产生的输出采样数，必须为正整数。对于所有非二进制方案（如脉冲形状所定义），此值必须大于 1。

    有关详细信息，请参阅 Signal Upsampling and Rate Changes。

**Rate options**
:   选择模块的速率处理选项。

    - `Enforce single-rate processing` —
      选择此选项时，输入和输出信号具有相同的端口采样时间。模块通过使输出相对于输入发生大小变化来实现速率变化。输出宽度等于符号数与 **Samples per symbol** 参数值的乘积。
    - `Allow multirate processing` —
      选择此选项时，输入和输出信号具有不同的端口采样时间。输出采样时间等于符号周期除以 **Samples per symbol** 参数值。

**输出数据类型**
:   选择输出信号的数据类型。输出数据类型可以为 `single` 或 `double`。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用连续相位频移键控方法进行调制

CPFSK Modulator Baseband 模块使用连续相位频移键控方法对信号进行调制。输出是已调制信号的基带表示。**M-ary number** 参数 *M* 表示输入字母表的大小。*M* 必须具有 2*K* 的形式，其中 *K* 为某个正整数。

此模块支持多 h **Modulation index**。有关详细信息，请参阅 CPM Modulator Baseband。

### 整数值信号和二值信号

当将 **输入类型** 参数设置为 `Integer` 时，模块接受 -(M-1) 到 M-1 之间的奇数整数。

当将 **输入类型** 参数设置为 `Bit` 时，模块接受 *K* 个比特的分组。每个分组称为一个二进制*字*。输入向量长度必须是 *K* 的整数倍。

在二进制输入模式下，模块使用取决于将 **Symbol set ordering** 参数设置为 `Binary` 还是 `Gray` 的映射方案，将每个二进制字映射到 0 到 M-1 之间的整数。然后，模块将整数 *k* 映射到中间值 2k-(M-1)，并按照整数输入模式进行操作。有关详细信息，请参阅 Integer-Valued and Binary-Valued Symbols。

此模块接受标量值或列向量输入信号。如果将 **输入类型** 设置为 `Bit`，则输入信号也可以是长度为 *K* 的向量。

### 单速率处理

在单速率处理模式下，输入和输出信号具有相同的端口采样时间。模块通过使输出相对于输入发生大小变化来隐式实现速率变化。在此模式下，模块的输入可以是多个符号。

- 当将 **输入类型** 设置为 `Integer` 时，输入可以是列向量，其长度为输入符号数。
- 当将 **输入类型** 设置为 `Bit` 时，输入必须是列向量，其宽度为 *K*（每符号比特数）的整数倍。

输出宽度等于输入符号数与 **Samples per symbol** 参数值的乘积。

### 多速率处理

在多速率处理模式下，输入和输出信号具有不同的端口采样时间。在此模式下，模块的输入必须为一个符号。

- 当将 **输入类型** 设置为 `Integer` 时，输入必须为标量。
- 当将 **输入类型** 设置为 `Bit` 时，输入宽度必须等于每符号比特数。

输出采样时间等于符号周期除以 **Samples per symbol** 参数值。
