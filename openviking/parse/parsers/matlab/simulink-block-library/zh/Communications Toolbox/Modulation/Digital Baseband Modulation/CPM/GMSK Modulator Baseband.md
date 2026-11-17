---
type: simulink-block
title: 'GMSK Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / CPM'
documentation_page: 'gmskmodulatorbaseband'
documentation_source_path: 'ref/gmskmodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# GMSK Modulator Baseband

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**输入类型**
:   指示输入由双极性值还是二进制值组成。

**BT product**
:   带宽与时间的乘积。

    该模块使用此参数以增加符号间干扰为代价来降低带宽。为此参数输入一个非负标量值。

**Pulse length (symbol intervals)**
:   频率脉冲形状的长度。

**Symbol prehistory**
:   一个标量或向量值，指定模块在仿真开始之前使用的数据符号，按时间倒序排列。

    - 标量值扩展为长度为 *L*P – 1 的向量。*L*P 表示脉冲长度，由 **Pulse length (symbol intervals)** 参数指定。
    - 对于向量，长度必须为 *L*P – 1。

**Phase offset (rad)**
:   输出波形的初始相位，以弧度为单位。

**Samples per symbol**
:   模块为输入中的每个整数或比特产生的输出样本数，必须为正整数。对于所有非二进制方案（由脉冲形状定义），此值必须大于 1。

    有关详细信息，请参阅 Signal Upsampling and Rate Changes。

**Rate options**
:   选择模块的速率处理选项。

    - `Enforce single-rate processing` — 选择此选项时，输入和输出信号具有相同的端口采样时间。该模块通过与输入相比在输出端进行大小变更来实现速率变化。输出宽度等于符号数与 **Samples per symbol** 参数值的乘积。
    - `Allow multirate processing` — 选择此选项时，输入和输出信号具有不同的端口采样时间。输出采样时间等于符号周期除以 **Samples per symbol** 参数值。

**输出数据类型**
:   模块的输出类型可以指定为 `single` 或 `double`。默认情况下，模块将此设置为 `double`。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用高斯最小频移键控方法进行调制

GMSK Modulator Baseband 模块使用高斯最小频移键控方法进行调制。输出是调制信号的基带表示。

**BT product** 参数表示带宽乘以时间。此参数为非负标量。它用于以增加符号间干扰为代价来降低带宽。**Pulse length** 参数以符号间隔为单位测量高斯脉冲形状的长度。有关脉冲形状的说明，请参阅下方参考文献中 Anderson、Aulin 和 Sundberg 的著作。频率脉冲形状由以下方程定义。

g(t)=12T{Q[2πBbt−T2ln(2)]−Q[2πBbt+T2ln(2)]}Q(t)=∫t∞12πe−τ2/2dτ

对于此模块，输入符号 1 会导致 π/2 弧度的相位偏移。

群延迟是滤波器响应开始与其峰值之间的样本数。该模块引入的群延迟为 **Pulse length**/2 \* **Samples per symbol**（以输出采样周期为参考）。对于 GMSK，**Pulse length** 表示以符号为单位的截断频率脉冲长度。接收端（解调器）的净延迟效应由 **Traceback depth** 参数决定，在大多数情况下该参数会大于群延迟。

### 整数值信号和二进制值信号

当将 **输入类型** 参数设置为 `Integer` 时，模块接受值 1 和 -1。

当将 **输入类型** 参数设置为 `Bit` 时，模块接受值 0 和 1。

此模块接受标量值或列向量输入信号。对于列向量输入信号，输出宽度等于符号数与 **Samples per symbol** 参数值的乘积。

### 单速率处理

在单速率处理模式下，输入和输出信号具有相同的端口采样时间。该模块通过与输入相比在输出端进行大小变更来隐式实现速率变化。在此模式下，模块的输入可以是多个符号。

- 当将 **输入类型** 设置为 `Integer` 时，输入可以是列向量，其长度为输入符号数。
- 当将 **输入类型** 设置为 `Bit` 时，输入宽度必须是 2 的整数倍。

输出宽度等于输入符号数与 **Samples per symbol** 参数值的乘积。

### 多速率处理

在多速率处理模式下，输入和输出信号具有不同的端口采样时间。在此模式下，模块的输入必须是一个符号。

- 当将 **输入类型** 设置为 `Integer` 时，输入必须是标量。
- 当将 **输入类型** 设置为 `Bit` 时，输入宽度必须等于每符号的比特数。

输出采样时间等于符号周期除以 **Samples per symbol** 参数值。
