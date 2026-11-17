---
type: simulink-block
title: 'Two-Channel Synthesis Subband Filter'
family: 'filtering'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'twochannelsynthesissubbandfilter'
documentation_source_path: 'ref/twochannelsynthesissubbandfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Two-Channel Synthesis Subband Filter

## 端口

### 输入

### **Hi band** — 高频子带向量 | 矩阵

将高频子带指定为向量或矩阵。高频子带和低频子带必须具有相同的大小和数据类型。

当输入为定点时，它必须仅为有符号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** Yes

### **Lo band** — 低频子带向量 | 矩阵

将低频子带指定为向量或矩阵。高频子带和低频子带必须具有相同的大小和数据类型。

如果输入为定点，则它必须是有符号整数或具有 2 的幂斜率且零偏置的有符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** Yes

### 输出

### **Output 1** — 合成输出向量 | 矩阵

该模块以向量或矩阵形式返回合成输出。输出中的行数是输入信号行数之和。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** Yes

## 参数

### 主选项卡

### **Lowpass FIR filter coefficients** — 低通 FIR 滤波器系数 `[0.3327 0.8069 0.4599 -0.1350 -0.0854 0.0352]`（默认）

低通 FIR 滤波器系数的向量，按 *z* 的降幂排列。低通滤波器应为半带滤波器，其通带是 **Highpass FIR filter coefficients** 参数所指定滤波器的阻带。要使用此模块重建 Two-Channel Analysis Subband Filter 模块的输出，必须设计此模块中的滤波器，以完美重建分析滤波器的输出。有关详细信息，请参阅指定 FIR 滤波器。

### **Highpass FIR filter coefficients** — 高通 FIR 滤波器系数 `[0.0352 0.0854 -0.1350 -0.4599 0.8069 -0.3327]`（默认）

高通 FIR 滤波器系数的向量，按 *z* 的降幂排列。高通滤波器应为半带滤波器，其通带是 **Lowpass FIR filter coefficients** 参数所指定滤波器的阻带。要使用此模块重建 Two-Channel Analysis Subband Filter 模块的输出，必须设计此模块中的滤波器，以完美重建分析滤波器的输出。有关详细信息，请参阅指定 FIR 滤波器。

### **Input processing** — 输入处理 `Columns as channels (frame based)`（默认）| `Elements as channels (sample based)`

指定该模块应如何处理输入。可将此参数设置为以下选项之一：

- `Columns as channels (frame based)`（默认）— 选择此选项时，模块将输入的每一列视为单独通道。
- `Elements as channels (sample based)` — 选择此选项时，模块将输入的每个元素视为单独通道。

有关详细信息，请参阅基于帧的处理和基于采样的处理。

### **Rate options** — 速率选项 `Enforce single-rate processing`（默认）| `Allow multirate processing`

指定该模块的速率处理规则。可将此参数设置为以下选项之一：

- `Enforce single-rate processing` — 选择此选项时，模块将输入的每一列视为独立通道，并随时间重建每个通道。输出与输入具有相同的采样率，但输出帧大小是输入帧大小的两倍。要选择此选项，必须将 **Input processing** 参数设置为 `Columns as channels (frame based)`。
- `Allow multirate processing` — 选择此选项时，模块的输入和输出大小相同，但输出的采样率是输入的两倍。

此参数的某些设置会导致模块具有非零延迟。有关详细信息，请参阅延迟。

### 数据类型选项卡

### **Rounding mode** — 舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择定点运算的舍入模式。滤波器系数不遵循此参数；它们始终舍入到 `Nearest`。

**注意**

当以下所有条件成立时，**Rounding mode** 和 **Saturate on integer overflow** 设置对数值结果没有影响：

- **Product output** 为 `Inherit: Inherit via internal rule`
- **Accumulator** 为 `Inherit: Inherit via internal rule`
- **Output** 为 `Inherit: Same as accumulator`

在这些数据类型设置下，模块实际上以全精度模式运行。

### **Saturate on integer overflow** — 整数溢出时饱和 `off`（默认）| `on`

选中此参数时，模块对其定点运算的结果进行饱和处理。清除此参数时，模块对其定点运算的结果进行环绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

**注意**

当满足以下所有条件时，**Rounding mode** 和 **Saturate on integer overflow** 参数对数值结果没有影响：

- **Product output** 数据类型为 `Inherit: Inherit via internal rule`。
- **Accumulator** 数据类型为 `Inherit: Inherit via internal rule`。

在这些数据类型设置下，模块以全精度模式运行。

### **Coefficients** — 系数的数据类型 `Inherit: Same word length as input`（默认）| `fixdt(1,16)` | `fixdt(1,16,0)`

指定系数的数据类型。有关此模块中系数数据类型用法的图示，请参阅定点数据类型和乘法数据类型。可将它设置为：

- 继承数据类型的规则，例如 `Inherit: Same word length as input`
- 可求值为有效数据类型的表达式，例如 `fixdt(1,16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Coefficients** 参数。

有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Coefficients Minimum** — 滤波器系数的最小值 `[]`（默认）| scalar

指定滤波器系数的最小值。默认值为 `[]`（未指定）。Simulink® 软件使用此值对定点数据类型执行自动定标。

### **Coefficients Maximum** — 滤波器系数的最大值 `[]`（默认）| scalar

指定滤波器系数的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值对定点数据类型执行自动定标。

### **Product output** — 乘积输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `fixdt(1,16,0)`

指定乘积输出的数据类型。有关此模块中乘积输出数据类型用法的图示，请参阅定点数据类型和乘法数据类型。可将它设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`。有关此规则的详细信息，请参阅通过内部规则继承。

  **注意**

  实际乘积输出字长可能等于或大于计算出的理想乘积输出字长，具体取决于“配置参数”对话框的 **Hardware Implementation** 窗格上的设置。
- 可求值为有效数据类型的表达式，例如 `fixdt(1,16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Product output** 参数。

有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Accumulator** — 累加器的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

指定累加器的数据类型。有关此模块中累加器数据类型用法的图示，请参阅定点数据类型。可将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`。有关此规则的详细信息，请参阅通过内部规则继承。
- 可求值为有效数据类型的表达式，例如 `fixdt(1,16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Accumulator** 参数。

有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Output** — 输出的数据类型 `Inherit: Same as accumulator`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

指定输出的数据类型。有关此模块中输出数据类型用法的图示，请参阅定点数据类型。可将它设置为：

- 继承数据类型的规则，例如 `Inherit: Same as accumulator`
- 可求值为有效数据类型的表达式，例如 `fixdt(1,16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Output** 参数。

有关详细信息，请参阅控制信号的数据类型 (Simulink)。

### **Output Minimum** — 输出最小值 `[]`（默认）| scalar

指定模块应输出的最小值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅指定信号范围 (Simulink)）
- 定点数据类型的自动定标

### **Output Maximum** — 输出最大值 `[]`（默认）| scalar

指定模块应输出的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅指定信号范围 (Simulink)）
- 定点数据类型的自动定标

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。

## 所属库

DSP System Toolbox / Filtering / Multirate Filters

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

在某些条件下，生成的代码依赖 `memcpy` 或 `memset` 函数（`string.h`）。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

从高频和低频子带重建信号

Two-Channel Synthesis Subband Filter 模块从其高频和低频子带重建信号，每个子带具有原始信号一半的带宽和一半的采样率。使用此模块可重建由 Two-Channel Analysis Subband Filter 模块分解的信号。

该模块将高频和低频子带按 2 进行上采样，然后用一对高通和低通 FIR 滤波器对结果进行滤波，如下图所示。

该模块使用多相滤波器结构一起实现 FIR 滤波和下采样步骤，这比上一图中所示的先内插后滤波算法更高效。您可以通过连接多个此模块的副本或使用 Dyadic Synthesis Filter Bank 模块来实现多级二进合成滤波器组。有关详细信息，请参阅创建多级二进合成滤波器组。

您必须为低通和高通 FIR 滤波器提供滤波器系数向量。每个滤波器应为半带滤波器，其通带是另一个滤波器的阻带。您可以使用此模块重建 Two-Channel Analysis Subband Filter 模块的输出。为此，必须设计此模块中的滤波器，使其完美重建分析滤波器的输出。
