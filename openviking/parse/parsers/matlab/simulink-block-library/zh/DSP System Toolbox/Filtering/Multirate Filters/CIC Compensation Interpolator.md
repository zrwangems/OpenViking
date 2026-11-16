---
type: simulink-block
title: 'CIC Compensation Interpolator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'ciccompensationinterpolator'
documentation_source_path: 'ref/ciccompensationinterpolator.html'
language: zh-CN
chinese_source: worker-translation
---

# CIC Compensation Interpolator

## 端口

### Input

### **Input** — 数据输入向量 | 矩阵

指定数据输入为向量或矩阵。

模块将 *P*×*Q* 输入矩阵视为 *Q* 个独立通道，并沿第一个维度对每个通道进行插值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`

### Output

### **Output** — 上采样并滤波后的信号向量 | 矩阵

上采样并滤波后的信号，以向量或矩阵形式返回。对于 *P*×*Q* 输入矩阵，输出为 *LP*×*Q* 矩阵，其中 *L* 为插值因子。

当输出为 fixed-point 时，它仅是有符号的。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`

## 参数

### 主选项卡

### **Rate change factor** — CIC 滤波器的速率变更因子 `2` (默认) | 正整数

将 CIC 滤波器的速率变更因子指定为正整数。模块使用 FIR 多相插值器作为补偿滤波器来补偿 CIC 滤波器。

### **Number of sections** — 被补偿的 CIC 滤波器中的节数 `2` (默认) | 正整数

将 CIC 滤波器中的节数指定为正整数。模块使用 FIR 多相插值器作为补偿滤波器来补偿 CIC 滤波器。

### **Differential delay** — CIC 滤波器的差分延迟 `1` (默认) | 正整数

将 CIC 滤波器的每个梳状节中使用的差分延迟值指定为正整数。模块使用 FIR 多相插值器作为补偿滤波器来补偿 CIC 滤波器。

### **Interpolation factor** — 补偿滤波器的插值因子 `2` (默认) | 正整数

将补偿滤波器的插值因子 *L* 指定为正整数。

### **Minimum order filter design** — 设计最小阶数或指定阶数的补偿滤波器 `on` (默认) | `off`

选中此复选框时，模块设计满足通带频率、阻带频率、通带波纹和阻带衰减规格的最小阶数滤波器。清除此复选框时，模块设计您在 **Filter order** 参数中指定的阶数滤波器。

### **Filter order** — 补偿滤波器的阶数 `12` (默认) | 正整数

将补偿滤波器的阶数指定为正整数。

#### 依赖关系

要启用此参数，请清除 **Minimum order filter design** 参数。

### **Passband edge frequency (Hz)** — 补偿滤波器的通带边缘频率 `100000` (默认) | 正标量

将补偿滤波器的通带边缘频率 *Fpass* 指定为以 Hz 为单位的正标量，或以归一化频率单位表示的正标量 *(自 R2024a 起)*。

如果您将 **Sample rate mode** 参数设置为：

- `Specify on dialog` 或 `Inherit from input port` —— 通带边缘频率的值以 Hz 为单位，并且必须在 *Fpass* < *Fstop* < (*Fs*/2) × *L* 范围内，其中 *Fstop* 是阻带边缘频率，*Fs* 是您通过 **Input sample rate (Hz)** 参数指定的输入采样率，*L* 是您通过 **Interpolation factor** 参数指定的插值因子。
- `Use normalized frequency (0 to 1)` —— 通带边缘频率的值以归一化频率单位表示，并且必须在 *Fpass* < *Fstop* < `1.0` 范围内。

*(自 R2024a 起)*

### **Stopband edge frequency (Hz)** — 补偿滤波器的阻带边缘频率 `400000` (默认) | 正标量

将补偿滤波器的阻带边缘频率 *Fstop* 指定为以 Hz 为单位的正标量，或以归一化频率单位表示的正标量 *(自 R2024a 起)*。

如果您将 **Sample rate mode** 参数设置为：

- `Specify on dialog` 或 `Inherit from input port` —— 阻带边缘频率的值以 Hz 为单位，并且必须在 *Fpass* < *Fstop* < (*Fs*/2) × *L* 范围内，其中 *Fpass* 是通带边缘频率，*Fs* 是您通过 **Input sample rate (Hz)** 参数指定的输入采样率，*L* 是您通过 **Interpolation factor** 参数指定的插值因子。
- `Use normalized frequency (0 to 1)` —— 阻带边缘频率的值以归一化频率单位表示，并且必须在 *Fpass* < *Fstop* < `1.0` 范围内。

*(自 R2024a 起)*

#### 依赖关系

要启用此参数，请选择 **Minimum order filter design** 参数。

### **Passband ripple (dB)** — 补偿滤波器的通带波纹 `0.1` (默认) | 正标量

将补偿滤波器的滤波器通带波纹指定为以 dB 为单位的正标量。

### **Stopband attenuation (dB)** — 补偿滤波器的阻带衰减 `60` (默认) | 正标量

将补偿滤波器的阻带衰减指定为以 dB 为单位的正标量。

### **Sample rate mode** — 指定输入采样率的模式 `Use normalized frequency (0 to 1)` (默认) | `Specify on dialog` | `Inherit from input port`

*自 R2024a 起*

使用以下选项之一指定输入采样率：

- `Use normalized frequency (0 to 1)` —— 使用归一化频率单位 (0 到 1) 指定通带边缘频率和阻带边缘频率。
- `Specify on dialog` —— 使用 **Input sample rate (Hz)** 参数在模块对话框中指定输入采样率。
- `Inherit from input port` —— 模块从输入信号继承采样率。

### **Input sample rate (Hz)** — 输入信号的采样率 `600000` (默认) | 正标量

将输入信号的采样率指定为以 Hz 为单位的正标量。

#### 依赖关系

要启用此参数，请将 **Sample rate mode** 参数设置为 `Specify on dialog`。*(自 R2024a 起)*

### **View Filter Response** — 查看滤波器响应按钮

点击此按钮可打开滤波器可视化工具 (FVTool)，并显示 CIC Compensation Interpolator 的幅值响应和相位响应。该响应基于您在模块参数对话框中指定的值。对这些参数所做的更改会更新 FVTool。

要在 FVTool 运行时更新幅值响应，请修改对话框参数，然后点击 **Apply**。

要同时查看幅值响应和相位响应，请点击工具栏上的 **Magnitude and Phase responses** 按钮。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (默认) | `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，该 C 代码便会用于后续仿真。此选项需要额外的启动时间，但可提供更快的后续仿真。

### 数据类型选项卡

### **Rounding mode** — 输出 fixed-point 运算的舍入模式 `Floor` (默认) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择 fixed-point 运算的舍入模式。默认值为 `Floor`。

### **Coefficients** — 系数的字长和小数长度 `fixdt(1,16)` (默认) | `fixdt(1,16,0)`

将系数的 fixed-point 数据类型指定为以下之一：

- `fixdt(1,16)` — 字长为 `16` 且采用二进制小数点定标的带符号 fixed-point 数据类型。模块会根据系数值自动确定小数长度，以使系数在不溢出的情况下占据最大可表示范围。
- `fixdt(1,16,0)` — 字长为 `16` 且小数长度为 `0` 的带符号 fixed-point 数据类型。您可以将小数长度更改为任何其他整数值。
- `<data type expression>` — 通过使用求值为数据类型对象的表达式来指定系数数据类型。例如，`numerictype`(`fixdt`(`[ ]`,`16`, `15`))。将该数据类型的符号模式指定为 `[ ]` 或 true。
- `Refresh Data Type` — 刷新为默认数据类型。

点击 **Show data type assistant** 按钮 以显示数据类型助手，它可帮助您设置系数数据类型。

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

## 版本历史

**在 R2015b 中引入**

### R2024a：**Simulate using** 参数的默认值更改

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，模块默认使用 MATLAB 解释器进行仿真。

### R2024a：支持归一化频率

当您将 **Sample rate mode** 参数设置为 `Use normalized frequency (0 to 1)` 时，可以使用归一化频率单位 (0 到 1) 指定通带边缘频率和阻带边缘频率。

## 描述

使用 FIR 插值器补偿 CIC 滤波器

CIC Compensation Interpolator 模块使用 FIR 多相插值器作为补偿滤波器。CIC 补偿插值器是多速率 FIR 滤波器，您将其与 CIC 插值器级联，以减轻 CIC 滤波器的缺点。

CIC 插值滤波器用于需要高插值的领域。这些滤波器在 ASIC 和 FPGA 中很流行，因为它们没有任何乘法器。CIC 滤波器有两个缺点：

- CIC 滤波器具有会导致通带区域下垂的幅值响应。该幅值响应为：

  abs(sin(Mω2)sin(ω2))n

  - *M* — 差分延迟
  - *n* — 级数
  - *ω* — 归一化角频率
- CIC 滤波器具有较宽的过渡区。

补偿插值器滤波器具有逆 sinc 通带响应，以校正 CIC 下垂，并且具有窄过渡宽度。

此模块将 `dsp.CICCompensationInterpolator` System object™ 的功能引入 Simulink® 环境。
