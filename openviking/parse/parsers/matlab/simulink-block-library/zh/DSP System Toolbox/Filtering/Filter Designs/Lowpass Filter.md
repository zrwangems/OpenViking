---
type: simulink-block
title: 'Lowpass Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Designs'
documentation_page: 'lowpassfilter'
documentation_source_path: 'ref/lowpassfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Lowpass Filter

## 端口
```yaml
ports:
- name: Port_1
  summary: 待滤波的输入信号 列向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: 滤波后的信号 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **Port\_1** — 待滤波的输入信号 列向量 | 矩阵

输入信号，指定为实值或复值列向量或矩阵。如果输入信号是矩阵，则矩阵的每一列被视为独立通道。输入信号中的行数表示通道长度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是
### 输出

### **Port\_1** — 滤波后的信号 向量 | 矩阵

滤波后的信号，以向量或矩阵形式返回。输出具有与输入相同的大小、数据类型和复数特性。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Filter type
  summary: FIR 或 IIR 滤波器 FIR（默认）| IIR
  group: 主
- name: Design minimum order filter
  summary: 设计最小阶数滤波器 on（默认）| off
  group: 主
- name: Filter order
  summary: 低通滤波器的阶数 50（默认）| 正整数
  group: 主
- name: Passband edge frequency (Hz)
  summary: 通带边缘频率 8e3（默认）| 实正标量
  group: 主
- name: Stopband edge frequency (Hz)
  summary: 阻带边缘频率 12e3（默认）| 实正标量
  group: 主
- name: Maximum passband ripple (dB)
  summary: 最大通带波纹 0.1（默认）| 实正标量
  group: 主
- name: Minimum stopband attenuation (dB)
  summary: 最小阻带衰减 80（默认）| 实正标量
  group: 主
- name: Sample rate mode
  summary: 指定输入采样率的模式 Use normalized frequency (0 to 1)（默认）| Specify on dialog | Inherit from input port
  group: 主
- name: Input sample rate (Hz)
  summary: 输入采样率 44100（默认）| 标量
  group: 主
- name: View Filter Response
  summary: 打开滤波器可视化工具 button
  group: 主
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: 主
- name: Rounding mode
  summary: 舍入方法 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型
- name: Coefficients
  summary: 系数数据类型 fixdt(1,16)（默认）| fixdt(1,16,0) | <data type expression>
  group: 数据类型
```

### 主

### **Filter type** — FIR 或 IIR 滤波器 `FIR`（默认）| `IIR`

指定该模块实现的是 FIR 低通滤波器还是 IIR 低通滤波器。

### **Design minimum order filter** — 设计最小阶数滤波器 `on`（默认）| `off`

选中此复选框时，模块将设计具有最小阶数以及指定的通带、阻带频率、通带波纹和阻带衰减的滤波器。

清除此复选框时，您可以将 **Filter order** 指定为正整数。

### **Filter order** — 低通滤波器的阶数 `50`（默认）| 正整数

将低通滤波器的滤波器阶数指定为正整数。

#### 依赖关系

要启用此参数，请清除 **Design minimum order filter** 复选框。

### **Passband edge frequency (Hz)** — 通带边缘频率 `8e3`（默认）| 实正标量

将低通滤波器的通带边缘频率指定为以 Hz 为单位的实正标量，或以归一化频率单位表示的实正标量 *(自 R2023a 起)*。

如果将 **Sample rate mode** 参数设置为：

- `Specify on dialog` 或
  `Inherit from input port` ——
  通带边缘频率的值以 Hz 为单位，且必须小于输入采样率值的一半。
- `Use normalized frequency (0 to
  1)` —— 通带边缘频率的值以归一化频率单位表示。该值必须是小于
  `1.0` 的正标量。

*(自 R2023a 起)*

### **Stopband edge frequency (Hz)** — 阻带边缘频率 `12e3`（默认）| 实正标量

将低通滤波器的阻带边缘频率指定为以 Hz 为单位的实正标量，或以归一化频率单位表示的实正标量 *(自 R2023a 起)*。

如果将 **Sample rate mode** 参数设置为：

- `Specify on dialog` 或
  `Inherit from input port` ——
  阻带边缘频率的值以 Hz 为单位，且必须小于输入采样率值的一半。
- `Use normalized frequency (0 to
  1)` —— 阻带边缘频率的值以归一化频率单位表示。该值必须是小于
  `1.0` 的正标量。

*(自 R2023a 起)*

#### 依赖关系

要启用此参数，请选中 **Design minimum order filter** 复选框。

### **Maximum passband ripple (dB)** — 最大通带波纹 `0.1`（默认）| 实正标量

将通带中滤波器响应的最大波纹指定为以 dB 为单位的实正标量。

### **Minimum stopband attenuation (dB)** — 最小阻带衰减 `80`（默认）| 实正标量

将阻带中的最小衰减指定为以 dB 为单位的实正标量。

### **Sample rate mode** — 指定输入采样率的模式 `Use normalized frequency (0 to 1)`（默认）| `Specify on dialog` | `Inherit from input port`

*自 R2023a 起*

使用以下选项之一指定输入采样率：

- `Use normalized frequency (0 to
  1)` —— 以归一化频率单位（0 到 1）指定通带边缘频率和阻带边缘频率。
- `Specify on dialog` —— 在模块对话框中通过 **Input sample rate (Hz)** 参数指定输入采样率。
- `Inherit from input port` —— 模块从输入信号继承采样率。

### **Input sample rate (Hz)** — 输入采样率 `44100`（默认）| 标量

将输入采样率指定为以 Hz 为单位的标量。

#### 依赖关系

要启用此参数，请将 **Sample rate mode** 参数设置为 `Specify on dialog`。*(自 R2023a 起)*

### **View Filter Response** — 打开滤波器可视化工具 `button`

打开滤波器可视化工具（`fvtool`）并显示 Lowpass Filter 的幅值和相位响应。该响应基于模块对话框参数。对这些参数所做的更改会更新 FVTool。

要在 FVTool 运行时更新幅值响应，请修改对话框参数并点击 **Apply**。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

要运行的仿真类型：

- `Interpreted execution`（默认）

  使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。
- `Code generation`

  使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码就会在后续仿真中重用。此选项需要额外的启动时间，但提供比 `Interpreted execution` 更快的仿真速度。

### 数据类型

### **Rounding mode** — 舍入方法 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

输出定点运算的舍入方法。

### **Coefficients** — 系数数据类型 `fixdt(1,16)`（默认）| `fixdt(1,16,0)` | `<data type expression>`

系数的定点数据类型，指定为以下之一：

- `fixdt(1,16)` —— 字长为 `16` 的有符号定点数据类型，采用二进制小数点定标。模块根据系数值自动确定小数长度，使系数在不溢出的情况下占据最大可表示范围。
- `fixdt(1,16,0)` —— 字长为 `16`、小数长度为 `0` 的有符号定点数据类型。您可以将小数长度更改为任何其他整数值。
- `<data type expression>` —— 使用求值为数据类型对象的表达式指定数据类型，例如数值类型（`fixdt`(`[ ]`,`16`,`15`)）。将此数据类型的符号模式指定为 `[ ]` 或 `true`。
- `Refresh Data Type` —— 刷新为默认数据类型。

点击 **Show data type assistant** 按钮以显示数据类型助手，它可帮助您设置数据类型。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。
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

Lowpass Filter 模块支持 ARM Cortex 代码生成。要了解有关 ARM Cortex 代码生成的更多信息，请参阅 Code Generation for ARM Cortex-M and ARM Cortex-A Processors。

Lowpass Filter 模块还支持在以下条件下使用 Intel AVX2 代码替换库进行 SIMD 代码生成：

- **Filter type** 设置为 `FIR`。
- 输入信号的数据类型为 `single` 或 `double`。

SIMD 技术显著提高了生成代码的性能。有关详细信息，请参阅 SIMD Code Generation。要从该模块生成 SIMD 代码，请参阅 Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks。

## 版本历史

**在 R2015b 中引入**

### R2023a：支持归一化频率

当您将 **Sample rate mode** 参数设置为 `Use normalized frequency (0 to 1)` 时，可以以归一化频率单位（0 到 1）指定通带和阻带边缘频率。

## 描述

设计 FIR 或 IIR 低通滤波器

Lowpass Filter 模块使用模块参数指定的滤波器设计，随时间独立地对输入信号的每个通道进行滤波。您可以使用 **Filter type** 参数控制该模块实现的是 IIR 还是 FIR 低通滤波器。您可以以 Hz 或归一化频率单位指定通带和阻带边缘频率 *(自 R2023a 起)*。

该模块支持 ARM® Cortex® 代码生成。在某些条件下，该模块还支持 SIMD 代码生成。有关详细信息，请参阅 Code Generation。
