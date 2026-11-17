---
type: simulink-block
title: 'CIC Compensation Decimator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'ciccompensationdecimator'
documentation_source_path: 'ref/ciccompensationdecimator.html'
language: zh-CN
chinese_source: worker-translation
---

# CIC Compensation Decimator

## 端口
```yaml
ports:
- name: Input
  summary: 数据输入 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | fixed point
- name: Output
  summary: 滤波并降采样后的信号 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | fixed point
```

### 输入

### **Input** — 数据输入 向量 | 矩阵

将数据输入指定为向量或矩阵。

该模块将 *P*×*Q* 的输入矩阵视为 *Q* 个独立通道，对每个通道沿第一维度进行抽取。

当您输入可变大小信号（帧长度在仿真期间变化）时，信号 *P* 的帧长度可以是任意的，即输入帧长度不必是抽取因子的整数倍。当您输入固定大小信号（帧长度在仿真期间不变）时，仅当您选中 **Allow arbitrary frame length for fixed-size input signals** 参数时，帧长度才可以为任意值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
### 输出

### **Output** — 滤波并降采样后的信号 向量 | 矩阵

滤波并降采样后的信号，以向量或矩阵形式返回。

输出信号维度取决于输入信号维度、补偿器的抽取因子，以及您是否选中 **Allow arbitrary frame length for fixed-size input signals** 参数。

当输出为定点时，它仅为有符号类型。

下表提供了当您输入固定大小输入信号和可变大小输入信号时输出信号维度的更多信息。

| 输入信号大小 | 输入信号维度 | 输出信号维度 |
| --- | --- | --- |
| 固定 | *P*×1 列向量，其中 *P* 是抽取因子 *M* 的整数倍 | (*P*/*M*)×1 |
| 固定 | *P*×1 列向量，其中 *P* 不是抽取因子 *M* 的整数倍 | 当您选中 **Allow arbitrary frame length for fixed-size input signals** 时，为 `ceil`(*P*/*M*)×1。如果您未选中 **Allow arbitrary frame length for fixed-size input signals**，模块将报错。 |
| 固定 | *P*×*Q* 矩阵，其中 *P* 是抽取因子 *M* 的整数倍 | (*P*/*M*)×*Q* |
| 固定 | *P*×*Q* 矩阵，其中 *P* 不是抽取因子 *M* 的整数倍 | 当您选中 **Allow arbitrary frame length for fixed-size input signals** 时，为 `ceil`(*P*/*M*)×*Q*。如果您未选中 **Allow arbitrary frame length for fixed-size input signals**，模块将报错。 |
| 可变 | *P*×*Q* | `ceil`(*P*/*M*)×*Q*  **Allow arbitrary frame length for fixed-size input signals** 参数会出现在模块对话框中，但对输入帧长度没有任何影响。即使您未选中 **Allow arbitrary frame length for fixed-size input signals** 参数，您也可以输入任意帧长度的可变大小信号。 |

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
## 参数
```yaml
parameters:
- name: Rate change factor
  summary: CIC 滤波器的速率变化因子 2（默认）| 正整数
  group: 主选项卡
- name: Number of sections
  summary: CIC 滤波器中的节数 2（默认）| 正整数
  group: 主选项卡
- name: Differential delay
  summary: CIC 滤波器的差分延迟 1（默认）| 正整数
  group: 主选项卡
- name: Decimation factor
  summary: 补偿滤波器的抽取因子 2（默认）| 正整数标量
  group: 主选项卡
- name: Minimum order filter design
  summary: 设计最小阶数或指定阶数的补偿滤波器 on（默认）| off
  group: 主选项卡
- name: Filter order
  summary: 补偿滤波器的阶数 12（默认）| 正整数
  group: 主选项卡
- name: Passband edge frequency (Hz)
  summary: 补偿滤波器的通带边缘频率 100000（默认）| 正标量
  group: 主选项卡
- name: Stopband edge frequency (Hz)
  summary: 补偿滤波器的阻带边缘频率 400000（默认）| 正标量
  group: 主选项卡
- name: Passband ripple (dB)
  summary: 补偿滤波器的通带波纹 0.1（默认）| 正实数标量
  group: 主选项卡
- name: Stopband attenuation (dB)
  summary: 补偿滤波器的阻带衰减 60（默认）| 正实数标量
  group: 主选项卡
- name: Sample rate mode
  summary: 指定输入采样率的模式 Use normalized frequency (0 to 1)（默认）| Specify on dialog | Inherit from input port
  group: 主选项卡
- name: Input sample rate (Hz)
  summary: 输入信号的采样率 1200000（默认）| 正实数标量
  group: 主选项卡
- name: Allow arbitrary frame length for fixed-size input signals
  summary: 允许固定大小输入信号具有任意帧长度 off（默认）| on
  group: 主选项卡
- name: View Filter Response
  summary: 查看滤波器响应 按钮（默认）
  group: 主选项卡
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: 主选项卡
- name: Rounding mode
  summary: 输出定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型选项卡
- name: Coefficients
  summary: 系数的字长和小数长度 fixdt(1,16)（默认）| fixdt(1,16,0)
  group: 数据类型选项卡
```

### 主选项卡

### **Rate change factor** — CIC 滤波器的速率变化因子 `2`（默认）| 正整数

将 CIC 滤波器的速率变化因子指定为正整数。该模块使用 FIR 多相抽取器作为补偿滤波器来补偿 CIC 滤波器。

### **Number of sections** — CIC 滤波器中的节数 `2`（默认）| 正整数

将 CIC 滤波器中抽取器和梳状节的数目指定为正整数。该模块使用 FIR 多相抽取器作为补偿滤波器来补偿 CIC 滤波器。

### **Differential delay** — CIC 滤波器的差分延迟 `1`（默认）| 正整数

将 CIC 滤波器每个梳状节中使用的延迟值指定为正整数。该模块使用 FIR 多相抽取器作为补偿滤波器来补偿 CIC 滤波器。

### **Decimation factor** — 补偿滤波器的抽取因子 `2`（默认）| 正整数标量

将补偿滤波器的抽取因子 *M* 指定为正整数。输入行数必须是抽取因子的整数倍。

### **Minimum order filter design** — 设计最小阶数或指定阶数的补偿滤波器 `on`（默认）| `off`

当您选中此复选框时，模块设计满足通带频率、阻带频率、通带波纹和阻带衰减规格的最小阶数滤波器。当您清除此复选框时，模块设计您在 **Filter order** 参数中指定的阶数滤波器。

默认情况下，此复选框处于选中状态。

### **Filter order** — 补偿滤波器的阶数 `12`（默认）| 正整数

将补偿滤波器的阶数指定为正整数。

#### 依赖关系

要启用此参数，请清除 **Minimum order filter design** 参数。

### **Passband edge frequency (Hz)** — 补偿滤波器的通带边缘频率 `100000`（默认）| 正标量

将补偿滤波器的通带边缘频率指定为正标量，单位为 Hz 或归一化频率单位 *(自 R2024a 起)*。

如果您将 **Sample rate mode** 参数设置为：

- `Specify on dialog` 或 `Inherit from input port` —— 通带边缘频率的值以 Hz 为单位，且必须在 *Fpass* < *Fstop* < *Fs*/2 范围内，其中 *Fstop* 是阻带边缘频率，*Fs* 是您通过 **Input sample rate (Hz)** 参数指定的输入采样率。
- `Use normalized frequency (0 to 1)` —— 通带边缘频率的值以归一化频率单位表示，且必须在 *Fpass* < *Fstop* < `1.0` 范围内。

*(自 R2024a 起)*

### **Stopband edge frequency (Hz)** — 补偿滤波器的阻带边缘频率 `400000`（默认）| 正标量

将补偿滤波器的阻带边缘频率指定为正标量，单位为 Hz 或归一化频率单位 *(自 R2024a 起)*。

如果您将 **Sample rate mode** 参数设置为：

- `Specify on dialog` 或 `Inherit from input port` —— 阻带边缘频率的值以 Hz 为单位，且必须在 *Fpass* < *Fstop* < *Fs*/2 范围内，其中 *Fpass* 是通带边缘频率，*Fs* 是您通过 **Input sample rate (Hz)** 参数指定的输入采样率。
- `Use normalized frequency (0 to 1)` —— 阻带边缘频率的值以归一化频率单位表示，且必须在 *Fpass* < *Fstop* < `1.0` 范围内。

*(自 R2024a 起)*

#### 依赖关系

要启用此参数，请选中 **Minimum order filter design** 参数。

### **Passband ripple (dB)** — 补偿滤波器的通带波纹 `0.1`（默认）| 正实数标量

将补偿滤波器的通带波纹指定为正实数标量，单位为 dB。

### **Stopband attenuation (dB)** — 补偿滤波器的阻带衰减 `60`（默认）| 正实数标量

将补偿滤波器的阻带衰减指定为正实数标量，单位为 dB。

### **Sample rate mode** — 指定输入采样率的模式 `Use normalized frequency (0 to 1)`（默认）| `Specify on dialog` | `Inherit from input port`

*自 R2024a 起*

使用以下选项之一指定输入采样率：

- `Use normalized frequency (0 to 1)` —— 以归一化频率单位（0 到 1）指定通带边缘频率和阻带边缘频率。
- `Specify on dialog` —— 在模块对话框中使用 **Input sample rate (Hz)** 参数指定输入采样率。
- `Inherit from input port` —— 模块从输入信号继承采样率。

### **Input sample rate (Hz)** — 输入信号的采样率 `1200000`（默认）| 正实数标量

将输入信号的采样率指定为正实数标量，单位为 Hz。

#### 依赖关系

要启用此参数，请将 **Sample rate mode** 参数设置为 `Specify on dialog`。*(自 R2024a 起)*

### **Allow arbitrary frame length for fixed-size input signals** — 允许固定大小输入信号具有任意帧长度 off（默认）| on

*自 R2023a 起*

指定固定大小输入信号（其大小在仿真期间不变）是否可以具有任意帧长度，其中帧长度不必是抽取因子的倍数。该模块仅对固定大小输入信号使用此参数设置，如果输入为可变大小，则忽略此参数。

当输入信号为可变大小信号时，该信号可以具有任意帧长度，即帧长度不必是抽取因子的倍数。

对于固定大小输入信号，如果您：

- 选中 **Allow arbitrary frame length for fixed-size input signals** 参数，则信号的帧长度不必是抽取因子的倍数。如果输入不是抽取因子的倍数，则输出通常为可变大小信号。因此，为了支持任意输入大小，该模块还必须支持可变大小操作，您可以通过选中 **Allow arbitrary frame length for fixed-size input signals** 参数来启用该操作。
- 清除 **Allow arbitrary frame length for fixed-size input signals** 参数，则输入帧长度必须是抽取因子的倍数。

### **View Filter Response** — 查看滤波器响应 按钮（默认）

点击此按钮可打开滤波器可视化工具 FVTool，并显示 CIC 补偿抽取器的幅值和相位响应。响应基于您在模块参数对话框中指定的值。对这些参数所做的更改会更新 FVTool。

要同时查看幅值响应和相位响应，请点击工具栏上的 **Magnitude and Phase responses** 按钮。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，C 代码就会在后续仿真中重复使用。此选项需要额外的启动时间，但可提供更快的后续仿真。

### 数据类型选项卡

### **Rounding mode** — 输出定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择定点运算的舍入模式。默认值为 `Floor`。

### **Coefficients** — 系数的字长和小数长度 `fixdt(1,16)`（默认）| `fixdt(1,16,0)`

将系数的定点数据类型指定为以下之一：

- `fixdt(1,16)`（默认）—— 字长为 `16` 的带符号定点数据类型，采用二进制小数点定标。该模块根据系数值自动确定小数长度，使系数在不溢出的情况下占据最大可表示范围。
- `fixdt(1,16,0)` —— 字长为 `16`、小数长度为 `0` 的带符号定点数据类型。您可以将小数长度更改为任何其他整数值。
- `<data type expression>` —— 通过使用求值为数据类型对象的表达式来指定系数数据类型。例如，`numerictype`(`fixdt`(`[ ]`,`16`,`15`))。将此数据类型的符号模式指定为 `[ ]` 或 true。
- `Refresh Data Type` —— 刷新为默认数据类型。

点击 **Show data type assistant** 按钮以显示数据类型助手，它可帮助您设置系数数据类型。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。
## 所属库

DSP System Toolbox / Filtering / Multirate Filters

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

### R2024a：**Simulate using** 参数默认值的变化

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，该模块默认使用 MATLAB 解释器进行仿真。

### R2024a：支持归一化频率

当您将 **Sample rate mode** 参数设置为 `Use normalized frequency (0 to 1)` 时，您可以以归一化频率单位（0 到 1）指定通带边缘和阻带边缘频率。

### R2023a：支持任意输入帧长度

当以下情况成立时，该模块支持具有任意帧长度的输入信号：

- 输入信号为固定大小信号（帧长度在仿真期间不变），并且您选中 **Allow arbitrary frame length for fixed-size input signals** 参数
- 输入信号为可变大小信号（帧长度在仿真期间变化）

当该模块支持具有任意帧长度的输入信号时，输入帧长度不必是抽取因子的倍数。

## 描述

使用 FIR 抽取器补偿 CIC 滤波器

CIC Compensation Decimator 模块使用 FIR 多相抽取器作为补偿滤波器。CIC 补偿抽取器是多速率 FIR 滤波器，您将其与 CIC 抽取器级联，以减轻 CIC 滤波器的缺点。

CIC 抽取滤波器用于需要高抽取率的领域。这些滤波器在 ASIC 和 FPGA 中很流行，因为它们没有任何乘法器。CIC 滤波器有两个缺点：

- CIC 滤波器的幅值响应会导致通带区域出现下垂。该幅值响应为：

  abs(sin(Mω2)sin(ω2))n

  - *M* —— 差分延迟
  - *n* —— 级数
  - *ω* —— 归一化角频率
- CIC 滤波器具有较宽的过渡区域。

补偿抽取器滤波器具有反向通带响应以校正 CIC 下垂，并且具有较窄的过渡宽度。

该模块将 `dsp.CICCompensationDecimator` System object™ 的功能引入 Simulink® 环境。
