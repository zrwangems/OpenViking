---
type: simulink-block
title: 'Stretch Processor'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: 'Signal and Data Processing / Detection, Range, Angle, and Doppler Estimation'
documentation_page: 'stretchprocessor'
documentation_source_path: '../phased/ref/stretchprocessor.html'
language: zh-CN
chinese_source: worker-translation
---

# Stretch Processor

## 端口

### 输入

### **X** — 输入信号 *M*×*P* 复值矩阵

输入信号，指定为 *M*×*P* 复值数组。*M* 是样本数，*P* 是脉冲数。

输入矩阵第一维的大小可以变化，以仿真变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形中，可能会发生大小变化。

**数据类型：** `double`
**复数支持：** Yes

### **PRF** — 脉冲重复频率正标量

当前脉冲的脉冲重复频率，指定为正标量。

#### 依赖关系

要启用此端口，请将 **Specify PRF as** 参数设置为 `Input port`。

**数据类型：** `double`
### 输出

### **Y** — 拉伸处理后的信号 *M*×*P* 复值矩阵

拉伸处理后的信号，返回为 *M*×*P* 复值数组。*M* 是样本数，*P* 是脉冲数。

**数据类型：** `double`
**复数支持：** Yes

## 参数

### **Pulse width (s)** — 脉冲的持续时间 `50e-6`（默认）| 正标量

每个脉冲的持续时间，指定为正标量。将 **Pulse width (s)** 与 **Pulse repetition frequency** 的乘积设置为小于或等于一。此限制确保脉冲宽度小于脉冲重复间隔。单位为秒。

**示例：** `300e-6`

### **Specify PRF as** — PRF 值的来源 `Property`（默认）| `Auto` | `Input port`

拉伸处理器的 PRF 值来源，指定为 `Property`、`Auto` 或 `Input port`。当设置为 `Property` 时，**Pulse repetition frequency (Hz)** 参数设置 PRF。当设置为 `Input port` 时，使用 `PRF` 输入端口传入 PRF。当设置为 `Auto` 时，PRF 根据输入信号的行数计算。

.

### **Pulse repetition frequency (Hz)** — 脉冲重复频率 `1e4`（默认）| 正标量

脉冲重复频率，PRF，指定为正标量。单位为赫兹。将此参数设置为仿真中使用的任何 `Waveform` 库模块中设置的相同值。

#### 依赖关系

要启用此参数，请将 **Specify PRF as** 参数设置为 `Property`。

### **FM sweep slope (Hz/s)** — 线性 FM 扫频的斜率 `2e9`（默认）| 标量

线性 FM 扫频的斜率（以标量表示），指定为标量。单位为赫兹每秒。

**示例：** `1e3`

### **FM sweep interval** — FM 扫频的方向 `Positive`（默认）| `Symmetric`

FM 扫频间隔，指定为 `Positive` 或 `Symmetric`。如果将此参数值设置为 `Positive`，则波形在 *0* 与 *B* 之间的频率带宽内扫频，其中 *B* 是频率带宽。如果将此参数值设置为 `Symmetric`，则波形在 *–B/2* 与 *B/2* 之间的区间内扫频。

### **Signal propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 实值正标量

信号传播速度，指定为实值正标量。光速的默认值是由 `physconst('LightSpeed')` 返回的值。单位为米每秒。

**示例：** `3e8`

**数据类型：** `double`

### **Reference range (m)** — 感兴趣距离范围的中心 `5000`（默认）| 正标量

感兴趣距离范围的中心，指定为正标量。参考距离必须在一个脉冲的非模糊距离内。单位为米。

**示例：** `10e3`

### **Reference span (m)** — 感兴趣距离范围的跨度 `500`（默认）| 正标量

感兴趣距离范围的跨度，指定为正标量。距离范围的跨度以 **Reference range (m)** 参数指定的距离为中心。单位为米。

**示例：** `1e3`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要编译时间，但通常运行更快。

当您开发和调整模型时，解释执行很有用。模块在 MATLAB 中运行底层的 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行得更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块会在执行前自动重新编译。

此表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都会被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Detection

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2014b 中引入**

## 描述

用于线性 FM 波形的拉伸处理器

Stretch Processor 模块对线性 FM 波形应用拉伸处理。拉伸处理也称为去斜（dechirping），是线性 FM 波形匹配滤波的一种替代方案。
