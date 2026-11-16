---
type: simulink-block
title: 'Highpass Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filter Design and Analysis / Filter Design / Singlerate'
documentation_page: 'highpassfilter'
documentation_source_path: 'ref/highpassfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Highpass Filter

## 端口

### 输入

### **Port\_1** — 要滤波的输入信号 列向量 | 矩阵

输入信号，指定为实数值或复数值列向量或矩阵。如果输入信号是矩阵，则矩阵的每一列被视为独立通道。输入信号中的行数表示通道长度。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** Yes
### 输出

### **Port\_1** — 滤波后的信号 向量 | 矩阵

滤波后的信号，以向量或矩阵形式返回。输出具有与输入相同的大小和复数特性。如果输出具有定点数据类型，则它始终为有符号。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** Yes

## 参数

### 主要

### **滤波器类型** — FIR 或 IIR 滤波器 `FIR`（默认）| `IIR`

指定模块实现 FIR 高通滤波器还是 IIR 高通滤波器。

### **设计最小阶数滤波器** — 设计具有最小阶数的滤波器 `on`（默认）| `off`

选中此复选框时，模块设计具有最小阶数的滤波器。清除此复选框时，可以将 **滤波器阶数** 指定为正整数。

### **滤波器阶数** — 高通滤波器的阶数 `50`（默认）| 正整数

将高通滤波器的阶数指定为正整数。

#### 依赖关系

要启用此参数，请清除 **设计最小阶数滤波器** 复选框。

### **阻带边缘频率 (Hz)** — 阻带边缘频率 `8e3`（默认）| 实数正标量

将高通滤波器的阻带边缘频率指定为以 Hz 或归一化频率单位表示的实数正标量 *(自 R2023a 起)*。

如果将 **采样率模式** 参数设置为：

- `Specify on dialog` 或
  `Inherit from input port` ––
  阻带边缘频率的值以 Hz 为单位，并且必须小于通带边缘频率。
- `Use normalized frequency (0 to
  1)` –– 阻带边缘频率的值以归一化频率单位表示。该值必须是小于通带边缘频率的正标量。

*(自 R2023a 起)*

#### 依赖关系

要启用此参数，请选中 **设计最小阶数滤波器** 复选框。

### **通带边缘频率 (Hz)** — 通带边缘频率 `12e3`（默认）| 实数正标量

将高通滤波器的通带边缘频率指定为以 Hz 或归一化频率单位表示的实数正标量 *(自 R2023a 起)*。

如果将 **采样率模式** 参数设置为：

- `Specify on dialog` 或
  `Inherit from input port` ––
  通带边缘频率的值以 Hz 为单位，并且必须小于输入采样率值的一半。
- `Use normalized frequency (0 to
  1)` –– 通带边缘频率的值以归一化频率单位表示。该值必须是小于
  `1.0` 的正标量。

*(自 R2023a 起)*

### **最小阻带衰减 (dB)** — 最小阻带衰减 `80`（默认）| 实数正标量

将阻带中的最小衰减指定为以 dB 为单位的实数正标量。

### **最大通带纹波 (dB)** — 最大通带纹波 `0.1`（默认）| 实数正标量

将通带中滤波器响应的最大纹波指定为以 dB 为单位的实数正标量。

### **采样率模式** — 用于指定输入采样率的模式 `Use normalized frequency (0 to 1)`（默认）| `Specify on dialog` | `Inherit from input port`

*自 R2023a 起*

使用以下选项之一指定输入采样率：

- `Use normalized frequency (0 to
  1)` –– 以归一化频率单位 (0 到 1) 指定通带边缘和阻带边缘频率。
- `Specify on dialog` –– 在模块对话框中通过
  **输入采样率 (Hz)**
  参数指定输入采样率。
- `Inherit from input port` –– 模块从输入信号继承采样率。

### **输入采样率 (Hz)** — 输入采样率 `44100`（默认）| 标量

将输入采样率指定为以 Hz 为单位的标量。

#### 依赖关系

要启用此参数，
请将 **采样率模式** 参数设置为
`Specify on dialog`。*(自 R2023a 起)*

### **仿真方式** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

要运行的仿真类型：

- `Interpreted execution`
  （默认）

  使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，
  但仿真速度比 `Code
  generation` 慢。
- `Code generation`

  使用生成的 C 代码仿真模型。首次运行仿真时，
  Simulink® 会为该模块生成 C 代码。只要模型不
  发生变化，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但
  提供的仿真速度比
  `Interpreted execution` 快。

### **查看滤波器响应** — 打开滤波器可视化工具按钮

打开滤波器可视化工具 (`fvtool`) 并显示高通滤波器的幅值/相位响应。该响应基于模块对话框参数。对这些参数所做的更改会更新 FVTool。

要在 FVTool 运行时更新幅值响应，请修改对话框参数并点击 **应用**。

### 数据类型

### **舍入模式** — 舍入方法 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

输出定点运算的舍入方法。

### **系数** — 系数数据类型 `fixdt(1,16)`（默认）| `fixdt(1,16,0)` | `<data type expression>`

系数的定点数据类型，指定为以下之一：

- `fixdt(1,16)` — 字长 `16` 的有符号
  定点数据类型，采用二进制小数点缩放。模块根据系数值自动确定小数
  长度，使得系数在不溢出的情况下占用最大可表示范围。
- `fixdt(1,16,0)` — 字长 `16`
  且小数长度 `0` 的有符号定点数据类型。可以将
  小数长度更改为任何其他整数值。
- `<data type expression>`
  — 使用求值为数据类型对象的表达式指定数据类型，例如，数值类型
  (`fixdt`(`[
  ]`,`16`,
  `15`))。将此数据类型的符号模式指定为 `[ ]` 或
  `true`。
- `Refresh Data Type` — 刷新为
  默认数据类型。

单击 **显示数据类型助手**
按钮 以显示数据类型助手，
它可帮助您设置数据类型。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

## 所属库

DSP System Toolbox / Filtering / Filter Designs

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Highpass Filter 模块支持 ARM
Cortex 代码生成。要了解有关 ARM
Cortex 代码生成的详细信息，请参阅为 ARM Cortex-M 和 ARM Cortex-A 处理器生成代码。

Highpass Filter 模块还支持在以下条件下使用 Intel
AVX2 代码替换库进行 SIMD 代码生成：

- **滤波器类型** 设置为
  `FIR`。
- 输入信号的数据类型为 `single` 或
  `double`。

SIMD 技术显著提高生成代码的性能。
有关详细信息，请参阅 SIMD 代码生成。要从
此模块生成 SIMD 代码，请参阅使用 Intel AVX2 代码替换库从 Simulink 模块生成 SIMD 代码。

## 版本历史

**在 R2015b 中引入**

### R2023a: 支持归一化频率

当将 **采样率模式** 参数设置为
`Use normalized frequency (0 to 1)` 时，可以以归一化频率单位 (0 到
1) 指定通带和阻带边缘频率。

## 描述

设计 FIR 或 IIR 高通滤波器

Highpass Filter 模块使用给定的设计规格随时间独立地对输入信号的每个通道进行滤波。可以使用 **滤波器
类型** 参数控制模块实现 IIR 还是 FIR 高通滤波器。可以以 Hz 或归一化频率
单位指定通带和阻带边缘频率 *(自 R2023a 起)*。

此模块支持 ARM®
Cortex® 代码生成。在某些条件下，此模块还支持 SIMD
代码生成。有关详细信息，请参阅代码生成。
