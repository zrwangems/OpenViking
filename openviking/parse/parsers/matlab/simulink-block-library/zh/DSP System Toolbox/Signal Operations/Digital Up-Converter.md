---
type: simulink-block
title: 'Digital Up-Converter'
family: 'signal-operations'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'digitalupconverter'
documentation_source_path: 'ref/digitalupconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Up-Converter

## 端口

### 输入

### **Input 1** — 输入信号列向量

将输入信号指定为实数或复数值的列向量。

当输入数据类型为 `double` 或 `single` 精度时，输出数据类型与输入数据类型相同。当输入数据类型为有符号整数或定点时，输出数据类型由 **Data Types** 选项卡上的 **Output** 参数定义。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
**复数支持：** Yes
### 输出

### **Output 1** — 上变频和上采样后的信号列向量

该模块将上变频和上采样后的信号输出为实数值列向量。输出长度等于输入长度乘以 **Interpolation factor** 参数中指定的值。

当输入数据类型为 `double` 或 `single` 精度时，输出数据类型与输入数据类型相同。当输入数据类型为有符号整数或定点时，输出数据类型由 **Data Types** 选项卡上的 **Output** 参数定义。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`

## 参数

### 主选项卡

### **Interpolation factor** — 插值因子 `100`（默认） | 正整数 > 1 | 正整数向量

将插值因子指定为大于 `1` 的正整数，或指定为 1×2 或 1×3 的正整数向量。

当您将此参数设置为标量值时，该模块对三个插值滤波级应用相同的插值因子。

当您将此参数设置为 1×2 向量时，该模块将向量中的第二个和第三个值分别应用于第二个和第三个滤波级，并绕过第一个滤波级。**Interpolation factor** 的两个元素都必须大于 `1`。

当您将此参数设置为 1×3 向量时，该模块将向量中的值应用于对应的滤波级。**Interpolation factor** 的第二个和第三个元素必须大于 `1`，第一个元素必须为 `1` 或 `2`。

### **Minimum order filter design** — 设计最小阶数滤波器 `on`（默认） | `off`

选中此复选框时，该模块设计的滤波器具有满足以下参数中所指定要求的最小可能阶数：

- **Passband ripple of cascade response (dB)**
- **Stopband attenuation of cascade response (dB)**
- **Two sided bandwidth of input signal**
- **Source of stopband frequency**
- **Stopband frequency**

当您清除此复选框时，该模块使用您在 **Order of first filter stage**、**Order of CIC compensation filter stage** 和 **Number of sections of CIC interpolator** 中指定的阶数来设计滤波器。这些滤波器设计满足您在 **Two sided bandwidth of input signal**、**Source of stopband frequency** 和 **Stopband frequency** 中设置的通带和阻带频率规范。默认情况下，此复选框处于选中状态。

### **Order of first filter stage** — 第一滤波级的阶数 `10`（默认） | 正偶数整数

将第一滤波级的阶数指定为偶数正整数。当您将 **Interpolation factor** 指定为 1×2 向量时，该模块忽略此参数中的值，因为该模块绕过第一滤波级。

#### 依赖关系

要启用此参数，请清除 **Minimum order filter design** 参数。

### **Number of sections of CIC interpolator** — CIC 插值器的段数 `3`（默认） | 正整数

将 CIC 插值器中的段数指定为正整数。

#### 依赖关系

当您清除 **Minimum order filter design** 参数时，此参数出现。

### **Source of stopband frequency** — 阻带频率来源 `Auto`（默认） | `Property`

将阻带频率来源指定为 `Auto` 或 `Property`。

当您将此参数设置为 `Auto` 并设置：

- **Sample rate mode** 为 `Specify on dialog` 或 `Inherit from input port` –– 该模块将级联滤波器响应的截止频率置于大约 *Fc* = *SampleRate*/2 Hz，并将阻带频率计算为 *Fstop* = *Fc* + *TW*/2。*SampleRate* 计算为 `1`/*Ts*，其中 *Ts* 是输入信号的采样时间。*TW* 是级联响应的过渡带宽，计算为 2×(*Fc*–*Fp*)，通带频率 *Fp* 等于 *Bandwidth*/2。
- **Sample rate mode** 为 `Use normalized frequency (0 to 1)` –– 该模块将级联滤波器响应的截止频率置于大约 *Fc* = 1/*L*，其中 *L* 是 **Interpolation factor** 中指定的总插值因子，并将阻带频率计算为 *Fstop* = *Fc* + *TW*/2。*TW* 是级联响应的过渡带宽，计算为 2×(*Fc*–*Fp*)，通带频率 *Fp* 等于 *Bandwidth*/2。

当您将此参数设置为 `Property` 时，请在 **Stopband frequency** 参数中指定阻带频率。

### **Type of oscillator** — 振荡器类型 `Sine wave`（默认） | `NCO`

将振荡器类型指定为以下之一：

- `Sine wave`（默认）—— 该模块使用从正弦三角函数样本获得的复指数信号，对插值滤波器级联的输出执行频率上变频。
- `NCO` —— 该模块使用由数控振荡器 (NCO) 获得的复指数执行频率上变频。

### **Center frequency of output signal** — 输出信号中心频率 `0.9333`（默认） | 正标量

将输出信号的中心频率指定为以 Hz 或归一化频率单位表示的正标量 *（自 R2024b 起）*。

如果您将 **Sample rate mode** 参数设置为：

- `Specify on dialog` 或 `Inherit from input port` –– 中心频率的值以 Hz 为单位，并且必须小于或等于 *SampleRate* 乘以总插值因子之积的一半。*SampleRate* 计算为 `1`/ *Ts*，其中 *Ts* 是输入信号的采样时间。该模块对输入信号进行上变频，使输出频谱以您在 **Center frequency of output signal** 中指定的频率为中心。
- `Use normalized frequency (0 to 1)` –– 中心频率的值以归一化频率单位表示。该值必须为小于或等于 `1.0` 的正标量。

*（自 R2024b 起）*

### **Order of CIC compensation filter stage** — CIC 补偿滤波器级的阶数 `12`（默认） | 正整数

将 CIC 补偿滤波器级的阶数指定为正整数。

#### 依赖关系

要启用此参数，请清除 **Minimum order filter design** 参数。

### **Two sided bandwidth of input signal** — 输入信号的双边带宽 `0.0133`（默认） | 正标量

将输入信号的双边带宽指定为以 Hz 或归一化频率单位表示的正标量 *（自 R2024b 起）*。该模块将滤波器级联的通带频率设置为您在此参数中指定值的一半。

### **Stopband frequency** — 阻带频率 `0.01`（默认） | 正标量

将阻带频率指定为以 Hz 或归一化频率单位表示的正标量 *（自 R2024b 起）*。

#### 依赖关系

要启用此参数，请将 **Source of stopband frequency** 设置为 `Property`。

### **Passband ripple of cascade response (dB)** — 级联响应通带波纹 (dB) `0.1`（默认） | 正标量

将级联响应的通带波纹以 dB 为单位指定为双精度正标量。当您选中 **Minimum order filter design** 参数时，该模块设计滤波器，使级联响应满足您在 **Passband ripple of cascade response (dB)** 中指定的通带波纹。

#### 依赖关系

要启用此参数，请选中 **Minimum order filter design** 参数。

### **Stopband attenuation of cascade response (dB)** — 级联响应阻带衰减 (dB) `60`（默认） | 正标量

将级联响应的阻带衰减以 dB 为单位指定为双精度正标量。当您选中 **Minimum order filter design** 参数时，该模块设计滤波器，使级联响应满足您在此参数中指定的阻带衰减。

#### 依赖关系

要启用此参数，请选中 **Minimum order filter design** 参数。

### **Number of NCO accumulator bits** — NCO 累加器位数 `16`（默认） | 正整数

将 NCO 累加器位数指定为范围 [`1 128`] 内的整数标量。

#### 依赖关系

要启用此参数，请将 **Type of oscillator** 设置为 `NCO`。

### **Number of NCO quantized accumulator bits** — NCO 量化累加器位数 `12`（默认） | 正整数

将 NCO 量化累加器位数指定为范围 [`1 128`] 内的整数标量。此值必须小于您在 **Number of NCO accumulator bits** 中指定的值。

#### 依赖关系

要启用此参数，请将 **Type of oscillator** 设置为 `NCO`。

### **Dither control for NCO** — NCO 的抖动控制 `on`（默认） | `off`

当您选中此参数时，该模块根据您在 **Number of NCO dither bits** 中指定的抖动位数，对 NCO 信号应用抖动。

#### 依赖关系

要启用此参数，请将 **Type of oscillator** 设置为 `NCO`。

### **Number of NCO dither bits** — NCO 抖动位数 `4`（默认） | 正整数

将 NCO 抖动位数指定为小于 **Number of NCO accumulator bits** 中累加器位数的整数标量。

#### 依赖关系

要启用此参数，请将 **Type of oscillator** 设置为 `NCO`，并选中 **Dither control for NCO** 参数。

### **Sample rate mode** — 指定输入采样率的模式 `Use normalized frequency (0 to 1)`（默认） | `Specify on dialog` | `Inherit from input port`

*自 R2024b 起*

使用以下选项之一指定输入采样率：

- `Use normalized frequency (0 to 1)` –– 以归一化频率单位 (0 to 1) 指定中心频率、双边带宽和阻带频率。
- `Specify on dialog` –– 使用 **Input sample rate (Hz)** 参数在模块对话框中指定输入采样率。
- `Inherit from input port` –– 该模块从输入信号继承采样率。该模块将采样率计算为 `N`/*Ts*，其中 *N* 是输入信号的帧大小，*Ts* 是输入信号的采样时间。

### **Input sample rate (Hz)** — 输入信号的采样率 `300e3`（默认） | 正标量

将输入信号的采样率以 Hz 为单位指定为正标量。此参数的值乘以总插值因子必须大于或等于 **Center frequency of output signal** 中值的两倍。

#### 依赖关系

要启用此参数，请将 **Sample rate mode** 参数设置为 `Specify on dialog`。*（自 R2024b 起）*

### **View Filter Response** — 查看滤波器响应按钮

单击此按钮以打开滤波器可视化工具 (FVTool)，并显示 Digital Up-Converter 中每个级以及级联级的幅度和相位响应。该响应基于您在模块参数对话框中指定的值。对这些参数所做的更改会更新 FVTool。

要在 FVTool 运行时更新幅度响应，请在对话框中修改参数，然后单击 **Apply**。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` –– 使用生成的 C 代码仿真模型。第一次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码会复用于后续仿真。此选项需要额外的启动时间，但可提供更快的后续仿真。

### Data Types 选项卡

### **Stage output** — 级输出 `Inherit: Same as input`（默认） | `fixdt([],16,0)`

指定第一个、第二个和第三个滤波级中输出的数据类型。您可以将此参数设置为：

- `Inherit: Same as input`（默认）—— 该模块从输入信号继承 **Stage output** 数据类型。
- `fixdt([],16,0)` —— 该模块使用带二进制小数点定标的定点数据类型。将此数据类型的符号模式指定为 `[]` 或 `true`。
- 计算结果为数据类型的表达式，例如 `numerictype([],16,15)`。将此数据类型的符号模式指定为 `[]` 或 `true`。

该模块根据您在此参数中设置的值，对每个滤波级输出处的数据进行类型转换。对于 CIC 级，转换在信号已按归一化因子缩放之后进行。

有关设置 stage output 参数的帮助，您可以单击 **Show data type assistant** 按钮以显示数据类型助手。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output** — 输出 `Inherit: Same as input`（默认） | `fixdt([],16,0)`

指定模块输出的数据类型。您可以将此参数设置为：

- `Inherit: Same as input`（默认）—— 该模块从输入继承输出数据类型。
- `fixdt([],16,0)` —— 该模块使用带二进制小数点定标的定点数据类型。将此数据类型的符号模式指定为 `[]` 或 `true`。
- 计算结果为数据类型的表达式，例如 `numerictype([],16,15)`。将此数据类型的符号模式指定为 `[]` 或 `true`。

有关设置 **Output** 参数的帮助，您可以单击 **Show data type assistant** 按钮以显示数据类型助手。。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Minimum** — 最小值 `[]`（默认） | 标量

指定模块输出的最小值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

### **Maximum** — 最大值 `[]`（默认） | 标量

指定模块输出的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

选择此参数以防止定点工具覆盖您在模块对话框中指定的数据类型。

## 所属库

DSP System Toolbox / Signal Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2015a 中引入**

### R2024b：支持归一化频率

当您将 **Sample rate mode** 参数设置为 `Use normalized frequency (0 to 1)` 时，可以以归一化频率单位 (0 to 1) 指定输入信号的双边带宽、输出信号的中心频率和阻带频率。

### R2024a：**Simulate using** 参数默认值变更

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，该模块默认使用 MATLAB 解释器进行仿真。

## 描述

将数字信号从基带上变频并转换到中频 (IF) 频段

Digital Up-Converter (DUC) 模块将复数字基带信号转换为实通带信号。

DUC 模块使用三个插值滤波器的级联对输入信号进行上采样。该模块通过将上采样信号乘以指定的输出信号中心频率，对其进行频率上变频。该模块根据您在模块对话框中设置的滤波器参数设计插值滤波器。
