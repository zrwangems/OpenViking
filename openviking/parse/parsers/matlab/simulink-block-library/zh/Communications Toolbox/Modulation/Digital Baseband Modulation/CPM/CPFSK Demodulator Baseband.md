---
type: simulink-block
title: 'CPFSK Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / CPM'
documentation_page: 'cpfskdemodulatorbaseband'
documentation_source_path: 'ref/cpfskdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# CPFSK Demodulator Baseband

## 端口

R2025b 中未提供文档。

## 参数

**M 元数**
:   字母表的大小。

**输出类型**
:   确定输出由整数还是比特组组成。

**符号集排序**
:   确定模块如何将每个整数映射到一组输出比特。仅当 **输出类型** 设置为
    `Bit` 时，此字段才可用。

**调制指数**
:   指定调制指数 {hi}。默认值为
    `0.5`。此属性的值必须为非负实数标量或列向量。

    此模块支持多 h **调制指数**。有关详细信息，请参阅
    CPM Modulator Baseband。

**相位偏移 (rad)**
:   调制波形的初始相位。

**每符号采样数**
:   表示每个调制符号的输入采样数，该值必须为正整数。有关详细信息，请参阅
    *Communications Toolbox™ 用户指南*中的“信号上采样和速率变化”。

**速率选项**
:   选择模块的速率处理方法。

    - `Enforce single-rate processing` —
      选择此选项时，输入和输出信号具有相同的端口采样时间。与输入相比，模块通过更改输出的大小来实现速率变化。输出宽度为符号数（当 **输出类型** 参数设置为 `Integer` 时，符号数由输入长度除以 **每符号采样数** 参数值得到）。
    - `Allow multirate processing` —
      选择此选项时，输入和输出信号具有不同的端口采样时间。输出周期与符号周期相同，等于输入周期与 **每符号采样数** 参数值的乘积。

    有关详细信息，请参阅本页“描述”部分中的“单速率处理”和“多速率处理”。

**回溯深度**
:   CPFSK Demodulator Baseband 模块用于构建每条回溯路径的网格分支数。

**输出数据类型**
:   输出数据类型可以为 `boolean`、
    `int8`、`int16`、
    `int32` 或 `double`。

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

对 CPFSK 调制数据进行解调

CPFSK Demodulator Baseband 模块对使用连续相位频移键控方法调制的信号进行解调。此模块的输入是调制信号的基带表示。**M 元数** 参数 *M* 是输入字母表的大小。对于某个正整数 *K*，*M* 必须具有 2*K* 的形式。

此模块支持多 h **调制指数**。有关详细信息，请参阅 CPM Modulator Baseband。

### 整数值信号和二进制值信号

当将 **输出类型** 参数设置为
`Integer` 时，模块生成介于 -(M-1) 和 M-1 之间的奇整数。

当将 **输出类型** 参数设置为
`Bit` 时，模块生成由 *K* 个比特组成的分组。每个分组称为一个二进制*字*。

在二进制输出模式下，模块首先像在整数输出模式下一样，将每个输入符号映射到一个中间值。然后，模块将奇整数 k 映射为非负整数 (k+M-1)/2。最后，模块将每个非负整数映射为一个二进制字，所使用的映射取决于 **符号集排序** 参数是设置为 `Binary` 还是 `Gray`。

此模块接受数据类型为 `single` 或 `double` 的标量值或列向量输入信号。

### 单速率处理

在单速率处理模式下，输入和输出信号具有相同的端口采样时间。与输入相比，模块通过更改输出的大小来隐式实现速率变化。输入宽度必须是 **每符号采样数** 参数值的整数倍，并且输入可以是列向量。

- 当将 **输出类型** 设置为
  `Bit` 时，输出宽度为输入符号数量的 *K* 倍。
- 当将 **输出类型** 设置为
  `Integer` 时，输出宽度为输入符号的数量。

### 多速率处理

在多速率处理模式下，输入和输出信号具有不同的端口采样时间。输入必须为标量。输出符号时间为输入采样时间与 **每符号采样数** 参数值的乘积。

- 当将 **输出类型** 设置为
  `Bit` 时，输出宽度等于每符号的比特数。
- 当将 **输出类型** 设置为
  `Integer` 时，输出为标量。

### 回溯深度和输出延迟

在内部，此模块创建调制方案的网格描述，并使用 Viterbi 算法。此模块中的 **回溯深度** 参数 *D* 是算法用于构建每条回溯路径的网格分支数。*D* 会影响输出延迟，输出延迟是输出中首个有效解调值之前的零符号数。

- 当将 **速率选项** 参数设置为
  `Allow multirate processing`，并且模型使用可变步长求解器，或使用 **任务模式** 参数设置为
  `SingleTasking` 的定步长求解器时，延迟由 D+1 个零符号组成。
- 当将 **速率选项** 参数设置为
  `Enforce single-rate processing` 时，延迟由 D 个零符号组成。

最佳 **回溯深度** 参数值取决于最小平方欧氏距离的计算。或者，可以使用“五倍约束长度”规则，根据状态数选择一个典型值，该规则对应于 5·log2(*numStates*)。

有关状态数的定义，请参阅 CPM Demodulator Baseband 帮助页。
