---
type: simulink-block
title: 'Stretch Processor'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: 'stretchprocessor'
documentation_source_path: 'ref/stretchprocessor.html'
language: zh-CN
chinese_source: worker-translation
---

# Stretch Processor

## 端口

### 输入

### **X** — 输入信号，*M*×*P* 复值矩阵

输入信号，指定为 *M*×*P* 复值数组。*M* 是采样点数，*P* 是脉冲数。

输入矩阵第一个维度的大小可以变化，以仿真信号长度的变化。例如，对于脉冲重复频率可变的脉冲波形，可能会发生这种大小变化。

**数据类型：** `double`
**复数支持：** 是

### **PRF** — 脉冲重复频率，正标量

当前脉冲的脉冲重复频率，指定为正标量。

#### 依赖关系

要启用此端口，请将 **PRF 指定方式** 参数设置为 `Input port`。

**数据类型：** `double`

### 输出

### **Y** — 拉伸处理后的信号，*M*×*P* 复值矩阵

拉伸处理后的信号，以 *M*×*P* 复值数组的形式返回。*M* 是采样点数，*P* 是脉冲数。

**数据类型：** `double`
**复数支持：** 是

## 参数

### **脉冲宽度 (s)** — 脉冲的持续时间 `50e-6` (默认) | 正标量

每个脉冲的持续时间，指定为正标量。将 **脉冲宽度 (s)** 与 **脉冲重复频率** 的乘积设置为小于或等于 1。此限制可确保脉冲宽度小于脉冲重复间隔。单位为 seconds。

**示例：** `300e-6`

### **PRF 指定方式** — PRF 值的来源 `Property` (默认) | `Auto` | `Input port`

拉伸处理器的 PRF 值来源，指定为 `Property`、`Auto` 或 `Input port`。当设置为 `Property` 时，由 **脉冲重复频率 (Hz)** 参数设置 PRF。当设置为 `Input port` 时，通过 `PRF` 输入端口传入 PRF。当设置为 `Auto` 时，根据输入信号的行数计算 PRF。

.

### **脉冲重复频率 (Hz)** — 脉冲重复频率 `1e4` (默认) | 正标量

脉冲重复频率（PRF），指定为正标量。单位为 Hertz。将此参数设置为与仿真中使用的任何 `Waveform` 库模块所设置的值相同。

#### 依赖关系

要启用此参数，请将 **PRF 指定方式** 参数设置为 `Property`。

### **FM 扫频斜率 (Hz/s)** — 线性 FM 扫频的斜率 `2e9` (默认) | 标量

线性 FM 扫频的斜率，以标量形式指定。单位为 Hertz per second。

**示例：** `1e3`

### **FM 扫频区间** — FM 扫频方向 `Positive` (默认) | `Symmetric`

FM 扫频区间，指定为 `Positive` 或 `Symmetric`。如果将此参数值设置为 `Positive`，波形会在 *0* 和 *B* 之间的频带内扫频，其中 *B* 是频率带宽。如果将此参数值设置为 `Symmetric`，波形会在 *–B/2* 和 *B/2* 之间的区间内扫频。

### **信号传播速度 (m/s)** — 信号传播速度 `physconst('LightSpeed')` (默认) | 实值正标量

信号传播速度，指定为实值正标量。光速的默认值是 `physconst('LightSpeed')` 返回的值。单位为 meters per second。

**示例：** `3e8`

**数据类型：** `double`

### **参考距离 (m)** — 感兴趣距离的中心 `5000` (默认) | 正标量

感兴趣距离的中心，指定为正标量。参考距离必须位于一个脉冲的无模糊距离范围内。单位为 meters。

**示例：** `10e3`

### **参考距离跨度 (m)** — 感兴趣距离的跨度 `500` (默认) | 正标量

感兴趣距离的跨度，指定为正标量。该距离范围以 **参考距离 (m)** 参数指定的距离为中心。单位为 meters。

**示例：** `1e3`

### **仿真方式** — 模块仿真方法 `Interpreted Execution` (默认) | `Code Generation`

模块仿真方式，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要编译时间，但通常运行速度更快。

在开发和调优模型时，解释执行很有用。该模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。对结果满意后，可以使用 `Code Generation` 运行该模块。与解释执行相比，长时间仿真使用生成的代码运行速度更快。您可以重复运行而无需重新编译，但如果更改任何模块参数，模块会在执行前自动重新编译。

下表显示了 **仿真方式** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，通过 **仿真方式** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 该模块使用 MATLAB 解释器执行。 | 该模块使用 MATLAB 解释器执行。 | 基于模型创建独立可执行文件。 |
| `Code Generation` | 该模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅选择仿真模式 (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`、`Code Generation` |
| **默认值：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Detection

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2014b 中引入**

## 描述

用于线性 FM 波形的拉伸处理器

Stretch Processor 模块对线性 FM 波形进行拉伸处理。拉伸处理也称为去斜处理，对于线性 FM 波形，它是匹配滤波的一种替代方法。
