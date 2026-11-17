---
type: simulink-block
title: 'GMSK Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / CPM'
documentation_page: 'gmskdemodulatorbaseband'
documentation_source_path: 'ref/gmskdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# GMSK Demodulator Baseband

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**输出类型**
:   确定输出由双极性值还是二进制值组成。

**BT product**
:   带宽与时间的乘积。

**Pulse length (symbol intervals)**
:   频率脉冲形状的长度。

**Symbol prehistory**
:   一个标量或向量值，按时间倒序指定模块在仿真开始之前使用的数据符号。

    - 标量值会扩展为长度为 *L*P – 1 的向量。*L*P 表示脉冲长度，由 **Pulse length (symbol intervals)** 参数指定。
    - 对于向量，长度必须为 *L*P – 1。

**Phase offset (rad)**
:   调制波形的初始相位。

**Samples per symbol**
:   表示每个调制符号的输入样本数，必须为正整数。有关详细信息，请参阅 *Communications Toolbox™ User's Guide* 中的 Signal Upsampling and Rate Changes。

**Rate options**
:   选择模块的速率处理方法。

    - `Enforce single-rate processing` — 选择此选项时，输入和输出信号具有相同的端口采样时间。模块通过使输出相对于输入发生大小变化来实现速率变化。当 **输出类型** 参数设置为 `Integer` 时，输出宽度为符号数（通过将输入长度除以 **Samples per symbol** 参数值得到）。
    - `Allow multirate processing` — 选择此选项时，输入和输出信号具有不同的端口采样时间。输出周期与符号周期相同，并等于输入周期与 **Samples per symbol** 参数值的乘积。

    有关详细信息，请参阅本页描述部分中的 Single-Rate Processing 和 Multirate Processing。

**Traceback depth**
:   GMSK Demodulator Baseband 模块用于构造每条回溯路径的网格分支数。

**输出数据类型**
:   输出数据类型可以为 `boolean`、`int8`、`int16`、`int32` 或 `double`。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

解调 GMSK 调制数据

GMSK Demodulator Baseband 模块使用 Viterbi 算法解调使用高斯最小频移键控方法调制的信号。此模块的输入是调制信号的基带表示。

### 整数值信号和二进制值信号

此模块接受数据类型为 `single` 或 `double` 的标量值或列向量输入信号。如果将 **输出类型** 参数设置为 `Integer`，则模块生成值 1 和 -1。如果将 **输出类型** 参数设置为 `Bit`，则模块生成值 0 和 1。

### 单速率处理

在单速率处理模式下，输入和输出信号具有相同的端口采样时间。模块通过使输出相对于输入发生大小变化来隐式实现速率变化。输入宽度必须是 **Samples per symbol** 参数值的整数倍，并且输入可以是列向量。

- 当将 **输出类型** 设置为 `Bit` 时，输出宽度是输入符号数的两倍。
- 当将 **输出类型** 设置为 `Integer` 时，输出宽度是输入符号数。

对于列向量输入信号，输入宽度等于符号数与 **Samples per symbol** 参数值的乘积。

### 多速率处理

在多速率处理模式下，输入和输出信号具有不同的端口采样时间。输入必须为标量。输出符号时间是输入采样时间与 **Samples per symbol** 参数值的乘积。

- 当将 **输出类型** 设置为 `Bit` 时，输出宽度等于每符号的位数。
- 当将 **输出类型** 设置为 `Integer` 时，输出为标量。

### 回溯深度和输出延迟

在内部，此模块创建调制方案的网格描述并使用 Viterbi 算法。此模块中的 **Traceback depth** 参数 D 是用于构造每条回溯路径的网格分支数。D 影响输出延迟，即输出中第一个有意义的解调值之前的零符号数。

- 当将 **Rate options** 参数设置为 `Allow multirate processing`，并且模型使用变步长求解器或 **Tasking Mode** 参数设置为 `SingleTasking` 的定步长求解器时，延迟由 D+1 个零符号组成。
- 当将 **Rate options** 参数设置为 `Enforce single-rate processing` 时，延迟由 D 个零符号组成。

最佳 **Traceback depth** 参数值取决于最小平方欧几里得距离计算。或者，可以使用*五倍约束长度*规则选择取决于状态数的典型值，该规则对应于 5log2(*numStates*。状态数由以下方程确定：

numStates={p⋅2(L−1), for even m2p⋅2(L−1), for odd m}

其中：

- *h* = *m*/*p* 是适当有理形式的调制指数

  - *m* = 调制指数的分子
  - *p* = 调制指数的分母
- *L* 是 Pulse length
