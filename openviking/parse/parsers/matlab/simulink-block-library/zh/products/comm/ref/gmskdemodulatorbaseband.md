---
type: simulink-block
title: 'GMSK Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Continuous Phase Modulation'
documentation_page: 'gmskdemodulatorbaseband'
documentation_source_path: 'ref/gmskdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# GMSK Demodulator Baseband

## 端口

R2025b 中未提供文档。

## 参数

**输出类型**
:   确定输出由双极性值还是二进制值组成。

**BT 乘积**
:   带宽与时间的乘积。

**脉冲长度 (symbol intervals)**
:   频率脉冲波形的长度。

**符号预历史**
:   一个标量或向量值，用于指定模块在仿真开始之前使用的数据符号，按逆时间顺序排列。

    - 标量值将扩展为长度为 *L*P – 1 的向量。*L*P
      表示脉冲长度，由 **脉冲长度 (symbol intervals)**
      参数指定。
    - 对于向量，其长度必须为 *L*P – 1。

**相位偏移 (rad)**
:   调制波形的初始相位。

**每符号采样数**
:   表示每个调制符号的输入采样数，必须为正整数。有关更多信息，请参阅
    *Communications Toolbox™ 用户指南*中的“信号上采样和速率变化”。

**速率选项**
:   选择模块的速率处理方法。

    - `Enforce single-rate processing` —
      选择此选项时，输入和输出信号具有相同的端口采样时间。模块通过使输出大小相对于输入大小发生变化来实现速率变化。输出宽度为符号数（当 **输出类型** 参数设置为 `Integer` 时，符号数由输入长度除以 **每符号采样数** 参数值得到）。
    - `Allow multirate processing` —
      选择此选项时，输入和输出信号具有不同的端口采样时间。输出周期与符号周期相同，等于输入周期与 **每符号采样数** 参数值的乘积。

    有关更多信息，请参阅本页“描述”部分中的“单速率处理”和“多速率处理”。

**回溯深度**
:   GMSK Demodulator Baseband 模块用于构建每条回溯路径的网格图分支数。

**输出数据类型**
:   输出数据类型可以为 `boolean`、
    `int8`、`int16`、
    `int32` 或 `double`。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

对 GMSK 调制数据进行解调

GMSK Demodulator Baseband 模块使用 Viterbi 算法，对采用高斯最小频移键控方法调制的信号进行解调。此模块的输入是调制信号的基带表示形式。

### 整数值信号和二进制值信号

此模块接受数据类型为 `single` 或 `double` 的标量值或列向量输入信号。如果将
**输出类型** 参数设置为
`Integer`，则模块生成值 1 和 -1。如果将
**输出类型** 参数设置为
`Bit`，则模块生成值 0 和 1。

### 单速率处理

在单速率处理模式下，输入和输出信号具有相同的端口采样时间。模块通过使输出大小相对于输入大小发生变化来隐式实现速率变化。输入宽度必须是 **每符号采样数** 参数值的整数倍，并且输入可以是列向量。

- 当将 **输出类型** 设置为
  `Bit` 时，输出宽度为输入符号数的两倍。
- 当将 **输出类型** 设置为
  `Integer` 时，输出宽度为输入符号数。

对于列向量输入信号，输入宽度等于符号数与 **每符号采样数** 参数值的乘积。

### 多速率处理

在多速率处理模式下，输入和输出信号具有不同的端口采样时间。输入必须为标量。输出符号时间等于输入采样时间与 **每符号采样数** 参数值的乘积。

- 当将 **输出类型** 设置为
  `Bit` 时，输出宽度等于每个符号的比特数。
- 当将 **输出类型** 设置为
  `Integer` 时，输出为标量。

### 回溯深度和输出延迟

在内部，此模块创建调制方案的网格描述，并使用 Viterbi 算法。此模块中的 **回溯深度** 参数 D 是用于构建每条回溯路径的网格图分支数。D 会影响输出延迟，输出延迟是输出中第一个有效解调值之前的零符号数。

- 当将 **速率选项** 参数设置为
  `Allow multirate processing`，并且模型使用变步长求解器，或使用 **任务模式** 参数设置为
  `SingleTasking` 的定步长求解器时，延迟由 D+1 个零符号组成。
- 当将 **速率选项** 参数设置为
  `Enforce single-rate processing` 时，延迟由 D 个零符号组成。

最佳 **回溯深度** 参数值取决于最小平方欧氏距离的计算。或者，可以根据状态数，使用
*五倍约束长度*规则来选择一个典型值，该规则对应于 5log2(*numStates*)。状态数由以下方程确定：

numStates={p⋅2(L−1), 当 m 为偶数时；2p⋅2(L−1), 当 m 为奇数时}

其中：

- *h* = *m*/*p* 是以既约有理数形式表示的调制指数

  - *m* = 调制指数的分子
  - *p* = 调制指数的分母
- *L* 为脉冲长度
