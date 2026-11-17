---
type: simulink-block
title: 'Two-Channel Analysis Subband Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'twochannelanalysissubbandfilter'
documentation_source_path: 'ref/twochannelanalysissubbandfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Two-Channel Analysis Subband Filter

## 端口
```yaml
ports:
- name: Input 1
  summary: 数据输入 列向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: Hi band
  summary: 高频子带 列向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: Lo band
  summary: 低频子带 列向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point
```

### 输入

### **Input 1** — 数据输入 列向量 | 矩阵

将数据输入指定为列向量或大小为 *M*×*N* 的矩阵。输入信号中的列表示 *N* 个独立通道。

当您将 **Input processing** 设置为 `Columns as channels (frame based)` 并将 **Rate options** 设置为 `Enforce single-rate processing` 时，该模块支持可变大小输入信号（帧长度在仿真期间变化）。当您指定可变大小输入信号时，它们可以具有任意帧长度，即输入帧长度不必为偶数。当您指定固定大小信号时，帧长度在某些条件下可以是任意的。有关更多详细信息，请参阅基于帧的处理和基于采样的处理。

如果输入是定点数，则它必须是有符号整数或具有 2 的幂斜率且零偏置的有符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### 输出

### **Hi band** — 高频子带 列向量 | 矩阵

该模块将高频子带输出为列向量或矩阵。

当您将 **Rate options** 设置为：

- `Enforce single-rate processing`
  —— 该模块保持输入采样率，并通过将输出帧大小减小 2 倍来对信号进行抽取。

  对于大小为 *M*×*N* 的输入，输出的上限大小为 `ceil`(*M*/2)×*N*。
- `Allow multirate processing` ——
  该模块对信号进行抽取，使得输出采样率为输入采样率的一半。

  输出帧大小与输入帧大小相同。

有关更多详细信息，请参阅基于帧的处理和基于采样的处理。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **Lo band** — 低频子带 列向量 | 矩阵

该模块将低频子带输出为列向量或矩阵。

当您将 **Rate options** 设置为：

- `Enforce single-rate processing`
  —— 该模块保持输入采样率，并通过将输出帧大小减小 2 倍来对信号进行抽取。

  对于大小为 *M*×*N* 的输入，输出的上限大小为 `ceil`(*M*/2)×*N*。
- `Allow multirate processing` ——
  该模块对信号进行抽取，使得输出采样率为输入采样率的一半。

  输出帧大小与输入帧大小相同。

有关更多详细信息，请参阅基于帧的处理和基于采样的处理。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
## 参数
```yaml
parameters:
- name: Lowpass FIR filter coefficients
  summary: 低通 FIR 滤波器系数 [0.0352 -0.0854 -0.1350 0.4599 0.8069 0.3327]（默认）| 行向量
  group: 主选项卡
- name: Highpass FIR filter coefficients
  summary: 高通 FIR 滤波器系数 [-0.3327 0.8069 -0.4599 -0.1350 0.0854 0.0352]（默认）| 行向量
  group: 主选项卡
- name: Input processing
  summary: 输入处理 Columns as channels (frame based)（默认）| Elements as channels (sample based)
  group: 主选项卡
- name: Rate options
  summary: 速率选项 Enforce single-rate processing（默认）| Allow multirate processing
  group: 主选项卡
- name: Allow arbitrary frame length for fixed-size input signals
  summary: 允许固定大小输入信号的任意帧长度 off（默认）| on
  group: 主选项卡
- name: Rounding mode
  summary: 定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型选项卡
- name: Saturate on integer overflow
  summary: 整数溢出时饱和 off（默认）| on
  group: 数据类型选项卡
- name: Coefficients
  summary: '系数的数据类型 Inherit: Same word length as input（默认）| fixdt(1,16) | fixdt(1,16,0)'
  group: 数据类型选项卡
- name: Coefficients Minimum
  summary: 滤波器系数的最小值 []（默认）| 标量
  group: 数据类型选项卡
- name: Coefficients Maximum
  summary: 滤波器系数的最大值 []（默认）| 标量
  group: 数据类型选项卡
- name: Product output
  summary: '乘积输出数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | fixdt(1,16,0)'
  group: 数据类型选项卡
- name: Accumulator
  summary: '累加器数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | Inherit: Same as product output | fixdt(1,16,0)'
  group: 数据类型选项卡
- name: Output
  summary: '输出数据类型 Inherit: Same as accumulator（默认）| Inherit: Same as input | Inherit: Same as product output | fixdt(1,16,0)'
  group: 数据类型选项卡
- name: Output Minimum
  summary: 输出最小值 []（默认）| 标量
  group: 数据类型选项卡
- name: Output Maximum
  summary: 输出最大值 []（默认）| 标量
  group: 数据类型选项卡
- name: Lock data type settings against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: 数据类型选项卡
```

### 主选项卡

### **Lowpass FIR filter coefficients** — 低通 FIR 滤波器系数 `[0.0352 -0.0854 -0.1350 0.4599 0.8069 0.3327]`（默认）| 行向量

指定低通 FIR 滤波器系数的向量，按 *z* 的降幂排列。低通滤波器应为半带滤波器，其通过的频带被 **Highpass FIR filter coefficients** 参数指定的滤波器所阻止。此参数的默认值指定了基于三阶 Daubechies 小波的滤波器。当您使用 Two-Channel Synthesis Subband Filter 模块重建此模块的输入时，您需要设计完美重建滤波器以用于合成子带滤波器。有关更多信息，请参阅指定 FIR 滤波器。

### **Highpass FIR filter coefficients** — 高通 FIR 滤波器系数 `[-0.3327 0.8069 -0.4599 -0.1350 0.0854 0.0352]`（默认）| 行向量

指定高通 FIR 滤波器系数的向量，按 *z* 的降幂排列。高通滤波器应为半带滤波器，其通过的频带被 **Lowpass FIR filter coefficients** 参数指定的滤波器所阻止。此参数的默认值指定了基于三阶 Daubechies 小波的滤波器。当您使用 Two-Channel Synthesis Subband Filter 模块重建此模块的输入时，您需要设计完美重建滤波器以用于合成子带滤波器。有关更多信息，请参阅指定 FIR 滤波器。

### **Input processing** — 输入处理 `Columns as channels (frame based)`（默认）| `Elements as channels (sample based)`

指定该模块应如何处理输入。您可以将此参数设置为以下选项之一：

- `Columns as channels (frame based)`
  （默认）—— 当您选择此选项时，该模块将输入的每一列视为单独的通道。
- `Elements as channels (sample based)`
  —— 当您选择此选项时，该模块将输入的每个元素视为单独的通道。

有关更多信息，请参阅基于帧的处理和基于采样的处理。

### **Rate options** — 速率选项 `Enforce single-rate processing`（默认）| `Allow multirate processing`

指定该模块的速率处理规则。您可以将此参数设置为以下选项之一：

- `Enforce single-rate processing`
  —— 当您选择此选项时，该模块将输入的每一列视为独立通道，并随时间分解每个通道。输出的采样率与输入相同，但输出帧大小是输入帧大小的一半。要选择此选项，您必须将 **Input processing** 参数设置为 `Columns as channels (frame based)`。
- `Allow multirate processing` ——
  当您选择此选项时，该模块的输入和输出大小相同，但输出的采样率是输入的一半。

此参数的某些设置会导致该模块具有非零延迟。有关更多信息，请参阅延迟。

### **Allow arbitrary frame length for fixed-size input signals** — 允许固定大小输入信号的任意帧长度 `off`（默认）| `on`

*自 R2023a 起*

指定固定大小输入信号（其大小在仿真期间不变）是否可以具有任意帧长度，其中帧长度不必为偶数。该模块仅对固定大小输入信号使用此参数，如果输入具有可变大小，则忽略此参数。

当输入信号是可变大小信号时，该信号可以具有任意帧长度，即帧长度不必为偶数。

对于固定大小输入信号，如果您：

- 选中 **Allow arbitrary frame length for fixed-size input signals** 参数，则信号的帧长度不必为偶数。输出为可变大小信号。
- 清除 **Allow arbitrary frame length for fixed-size input signals** 参数，则输入帧长度必须为偶数。

#### 依赖关系

要启用此参数，请将 **Input processing** 设置为 `Columns as channels (frame based)`，并将 **Rate options** 设置为 `Enforce single-rate processing`。

### 数据类型选项卡

### **Rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择定点运算的舍入模式。滤波器系数不遵循此参数；它们始终舍入为 `Nearest`。

**注意**

当以下所有条件均存在时，**Rounding mode** 和 **Saturate on integer overflow** 设置对数值结果没有影响：

- **Product output** 为 `Inherit: Inherit via internal rule`
- **Accumulator** 为 `Inherit: Inherit via internal rule`
- **Output** 为 `Inherit: Same as accumulator`

使用这些数据类型设置时，该模块实际上以全精度模式运行。

### **Saturate on integer overflow** — 整数溢出时饱和 `off`（默认）| `on`

当您选中此参数时，该模块对其定点运算的结果进行饱和处理。当您清除此参数时，该模块对其定点运算的结果进行回绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

**注意**

当满足以下所有条件时，**Rounding mode** 和 **Saturate on integer overflow** 参数对数值结果没有影响：

- **Product output** 数据类型为 `Inherit: Inherit via internal rule`。
- **Accumulator** 数据类型为 `Inherit: Inherit via internal rule`。

使用这些数据类型设置时，该模块以全精度模式运行。

### **Coefficients** — 系数的数据类型 `Inherit: Same word length as input`（默认）| `fixdt(1,16)` | `fixdt(1,16,0)`

指定系数数据类型。有关说明此模块中系数数据类型使用的图示，请参阅定点数据类型和乘法数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Same word length as input`
- 求值为有效数据类型的表达式，例如 `fixdt(1,16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Coefficients** 参数。

有关更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Coefficients Minimum** — 滤波器系数的最小值 `[]`（默认）| 标量

指定滤波器系数的最小值。默认值为 `[]`（未指定）。Simulink® 软件使用此值执行定点数据类型的自动定标。

### **Coefficients Maximum** — 滤波器系数的最大值 `[]`（默认）| 标量

指定滤波器系数的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行定点数据类型的自动定标。

### **Product output** — 乘积输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `fixdt(1,16,0)`

指定乘积输出数据类型。有关说明此模块中乘积输出数据类型使用的图示，请参阅定点数据类型和乘法数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`。有关此规则的更多信息，请参阅通过内部规则继承。

  **注意**

  实际乘积输出字长可能等于或大于计算出的理想乘积输出字长，具体取决于“配置参数”对话框的 **Hardware Implementation** 窗格上的设置。
- 求值为有效数据类型的表达式，例如 `fixdt(1,16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Product output** 参数。

有关更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Accumulator** — 累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

指定累加器数据类型。有关说明此模块中累加器数据类型使用的图示，请参阅定点数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`。有关此规则的更多信息，请参阅通过内部规则继承。
- 求值为有效数据类型的表达式，例如 `fixdt(1,16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Accumulator** 参数。

有关更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Output** — 输出数据类型 `Inherit: Same as accumulator`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

指定输出数据类型。有关说明此模块中输出数据类型使用的图示，请参阅定点数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Same as accumulator`
- 求值为有效数据类型的表达式，例如 `fixdt(1,16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Output** 参数。

有关更多信息，请参阅控制信号的数据类型 (Simulink)。

### **Output Minimum** — 输出最小值 `[]`（默认）| 标量

指定该模块应输出的最小值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅指定信号范围 (Simulink)）
- 定点数据类型的自动定标

### **Output Maximum** — 输出最大值 `[]`（默认）| 标量

指定该模块应输出的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅指定信号范围 (Simulink)）
- 定点数据类型的自动定标

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。
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

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2023a：支持任意输入帧长度

当以下情况时，该模块支持具有任意帧长度的输入信号：

- 输入信号是固定大小信号（帧长度在仿真期间不变），且该模块允许多速率处理。
- 输入信号是固定大小信号，该模块强制执行单速率处理，且您选中 **Allow arbitrary frame length for fixed-size input signals** 参数。
- 输入信号是可变大小信号（帧长度在仿真期间变化）。

当该模块支持具有任意帧长度的输入信号时，输入帧长度不必为偶数。

有关更多详细信息，请参阅基于帧的处理和基于采样的处理。

## 描述

将信号分解为高频和低频子带

Two-Channel Analysis Subband Filter 模块将输入分解为高频和低频子带，每个子带的带宽和采样率均为输入的一半。

该模块使用一对高通和低通 FIR 滤波器对输入进行滤波，然后将结果下采样 2 倍，如下图所示。

该模块使用多相滤波器结构将 FIR 滤波和下采样步骤一起实现，这比前面图中所示的先滤波后抽取算法更高效。每个子带是相应多相滤波器的第一个相位。您可以通过连接多个此模块的副本或使用 Dyadic Analysis Filter Bank 模块来实现多级二进分析滤波器组。有关更多信息，请参阅创建多级二进分析滤波器组。

您必须为低通和高通 FIR 滤波器提供滤波器系数向量。每个滤波器应为半带滤波器，其通过的频带被另一个滤波器所阻止。
