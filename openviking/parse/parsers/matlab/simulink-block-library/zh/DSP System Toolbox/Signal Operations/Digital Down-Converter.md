---
type: simulink-block
title: 'Digital Down-Converter'
family: 'signal-operations'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'digitaldownconverter'
documentation_source_path: 'ref/digitaldownconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Down-Converter

## 端口

### 输入

### **Input 1** — 数据输入列向量 | 矩阵

将数据输入指定为列向量或矩阵。输入信号中的行数必须是您在 **Decimation factor** 参数中指定的抽取因子的倍数。

当输入数据类型为 `double` 或 `single` 精度时，输出数据类型与输入数据类型相同。当输入数据类型为有符号整数或定点类型时，输出数据类型由 **Data Types** 选项卡上的 **Output** 参数定义。

如果输入为定点，则它必须是有符号整数或具有 2 的幂斜率且零偏置的有符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
**复数支持：** Yes

### **Osc** — 振荡器信号列向量 | 矩阵

将模块用于对输入信号进行频率下变频的振荡器信号指定为列向量或矩阵。该信号必须是复数，且其长度必须等于输入的长度。

当振荡器输入为定点时，它必须仅为有符号。

#### 依赖项

要启用此端口，请将 **Type of oscillator** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
**复数支持：** Yes

### 输出

### **Output 1** — 下变频并下采样后的信号列向量 | 矩阵

模块将下变频并下采样后的信号输出为列向量或矩阵。输出的长度等于输入的长度除以您在 **Decimation factor** 参数中指定的值。

当输入的数据类型为 `double` 或 `single` 精度时，输出的数据类型与输入的数据类型相同。当输入数据类型为定点类型或有符号整数时，输出数据类型由 **Data Types** 选项卡上的 **Output** 参数定义。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
**复数支持：** Yes

## 参数

### 主选项卡

### **Decimation factor** — 抽取因子 `100` (默认) | 正整数 ≥ 2 | 正整数的向量

将抽取因子指定为 ≥ 2 的正整数，或指定为 1×2 或 1×3 的正整数向量。

当将此参数设置为标量值时，模块对三个抽取滤波级应用相同的抽取因子。

当将此参数设置为 1×2 向量时，模块将向量中的第一个值和第二个值分别应用于第一滤波级和第二滤波级，并绕过第三级。**Decimation factor** 的两个元素都必须大于 1。

当将此参数设置为 1×3 向量时，模块将向量中的值应用于对应的滤波级。**Decimation factor** 的第一个和第二个元素必须大于 1，第三个元素必须为 1 或 2。

### **Minimum order filter design** — 设计最小阶数滤波器 `on` (默认) | `off`

选中此复选框时，模块设计满足以下参数中所指定要求的最小可能阶数滤波器：

- **Passband ripple of cascade response
  (dB)**
- **Stopband attenuation of cascade response
  (dB)**
- **Two-sided bandwidth of input
  signal**
- **Source of stopband frequency**
- **Stopband frequency**

清除此复选框时，模块使用您在 **Number of sections of CIC decimator**、**Order of CIC compensation filter stage** 和 **Order of third filter stage** 中指定的阶数设计滤波器。滤波器设计满足您在 **Two-sided bandwidth of input signal**、**Source of stopband frequency** 和 **Stopband frequency** 中设置的通带和阻带频率规范。默认情况下，选中此复选框。

### **Number of sections of CIC decimator** — CIC 抽取器的节数 `3` (默认) | 正整数

将 CIC 抽取器中的节数指定为正整数。

#### 依赖项

要启用此参数，请清除 **Minimum order filter design** 参数。

### **Order of third filter stage** — 第三滤波器级的阶数 `10` (默认) | 偶正整数

将第三滤波器级的阶数指定为偶正整数。当将 **Decimation factor** 指定为 1×2 向量时，模块忽略此参数中的值，因为模块绕过第三滤波器级。

#### 依赖项

要启用此参数，请清除 **Minimum order filter design** 参数。

### **Source of stopband frequency** — 阻带频率的来源 `Auto` (默认) | `Property`

将阻带频率的来源指定为 `Auto` 或 `Property`。

当将此参数设置为 `Auto` 并设置：

- **Sample rate mode** 设置为
  `Specify on dialog` –– 模块将级联滤波器响应的截止频率置于大约
  *Fc* =
  *SampleRate*/(2*M*)
  Hz，其中 *M* 是在 **Decimation factor** 中指定的总抽取因子。
  *SampleRate* 是您在 **Input sample rate
  (Hz)** 参数中指定的输入采样率。模块按下式计算阻带频率：
  *Fstop* =
  *Fc* +
  (*TW*/2)。*TW* 是级联响应的过渡带宽，计算为
  2×(*Fc*–*Fp*)，
  其中通带频率
  *Fp* 等于
  *Bandwidth*/2。
- **Sample rate mode** 设置为
  `Inherit from input port` ––
  模块将级联滤波器响应的截止频率置于大约
  *Fc* =
  *SampleRate*/(2*M*)
  Hz，其中 *M* 是在 **Decimation factor** 中指定的总抽取因子。
  *SampleRate* 计算为
  `1`/ *Ts*，其中
  *Ts* 是输入信号的采样时间。模块按下式计算阻带频率：
  *Fstop* =
  *Fc* +
  (*TW*/2)。*TW* 是级联响应的过渡带宽，计算为
  2×(*Fc*–*Fp*)，
  其中通带频率
  *Fp* 等于
  *Bandwidth*/2。
- **Sample rate mode** 设置为 `Use
  normalized frequency (0 to 1)` –– 模块
  将级联滤波器响应的截止频率置于大约
  *Fc* =
  1/*M* ，其中 *M* 是
  您在 **Decimation factor** 中指定的总抽取因子。模块
  按下式计算阻带频率：
  *Fstop* =
  *Fc* +
  (*TW*/2)。*TW* 是
  级联响应的过渡带宽，计算为
  2×(*Fc*–*Fp*)，
  并且通带频率
  *Fp* 等于
  *Bandwidth*/2。

当将此参数设置为 `Property` 时，在 **Stopband frequency** 中指定阻带频率。

### **Type of oscillator** — 振荡器类型 `Sine wave` (默认) | `NCO` | `Input port` | `None`

将振荡器类型指定为以下之一：

- `Sine wave` — 模块使用由正弦三角函数采样获得的复指数对输入信号执行频率下变频。
- `NCO` — 模块使用由数控振荡器 (NCO) 获得的复指数对输入信号执行频率下变频。
- `Input port` — 模块使用您通过 **Osc** 输入端口提供的复信号对输入信号执行频率下变频。
- `None` — 模块不需要混频器级，并作为三级级联抽取器工作。

### **Center frequency of output signal** — 输出信号的中心频率 `0.9333` (默认) | 正标量

将输出信号的中心频率指定为以 Hz 或归一化频率单位表示的正标量 *（自 R2024b 起）*。

如果将 **Sample rate mode** 参数设置为：

- `Specify on dialog` 或
  `Inherit from input port` ––
  中心频率的值以 Hz 为单位，并且必须小于输入信号采样率的一半。模块将输入信号从您在 **Center frequency
  of output signal** 中指定的通带中心频率下变频到 `0`
  Hz。
- `Use normalized frequency (0 to
  1)` –– 中心频率的值以归一化频率单位表示。该值必须是小于或等于 `1.0` 的正标量。

*（自 R2024b 起）*

#### 依赖项

要启用此参数，请将 **Type of
oscillator** 设置为 `Sine wave` 或
`NCO`。

### **Order of CIC compensation filter stage** — CIC 补偿滤波器级的阶数 `12` (默认) | 正整数

将 CIC 补偿滤波器级的阶数指定为正整数。

#### 依赖项

要启用此参数，请清除 **Minimum order filter design** 参数。

### **Two-sided bandwidth of input signal** — 输入信号的双侧带宽 `0.0133` (默认) | 正标量

将输入信号的双侧带宽指定为以 Hz 或归一化频率单位表示的正标量 *（自 R2024b 起）*。模块将滤波器级联的通带频率设置为此参数中指定值的一半。将此参数的值设置为小于 **Input sample rate
(Hz)**/**Decimation factor**。当将 **Sample rate mode** 设置为 **Inherit from
input port** 时，请将此值设置为小于
((`1`/*Ts*)/**Decimation
factor**)，其中 *Ts* 是输入信号的采样时间。如果将 **Sample rate mode** 设置为
`Use normalized frequency (0 to 1)`，请将此值设置为小于 1/**Decimation factor**。

### **Stopband frequency** — 阻带频率 `0.01` (默认) | 正标量

将阻带频率指定为以 Hz 或归一化频率单位表示的正标量 *（自 R2024b 起）*。

#### 依赖项

要启用此参数，请将 **Source of stopband
frequency** 设置为
`Property`。

### **Passband ripple of cascade response (dB)** — 级联响应的通带波纹 `0.1` (默认) | 正标量

将级联响应的通带波纹指定为以 dB 表示的双精度正标量。当您选择 **Minimum
order filter design** 时，模块设计滤波器，使级联响应满足您在 **Passband ripple of cascade response
(dB)** 中指定的通带波纹。

#### 依赖项

要启用此参数，请选择 **Minimum order
filter design** 参数。

### **Stopband attenuation of cascade response (dB)** — 级联响应的阻带衰减 `60` (默认) | 正标量

将级联响应的阻带衰减指定为以 dB 表示的双精度正标量。当您选择 **Minimum
order filter design** 参数时，模块设计滤波器，使级联响应满足您在此参数中指定的阻带衰减。

#### 依赖项

要启用此参数，请选择 **Minimum order
filter design** 参数。

### **Number of NCO accumulator bits** — NCO 累加器位数 `16` (默认) | 正整数

将 NCO 累加器位数指定为范围 [`1 128`] 中的整数标量。

#### 依赖项

要启用此参数，请将 **Type of
oscillator** 设置为 `NCO`。

### **Number of NCO quantized accumulator bits** — NCO 量化累加器位数 `12` (默认) | 范围 `[1 128]` 中的正整数

将 NCO 量化累加器位数指定为范围 `[1 128]` 中的整数标量。此值必须小于您在 **Number of NCO accumulator
bits** 中指定的值。

#### 依赖项

要启用此参数，请将 **Type of
oscillator** 设置为 `NCO`。

### **Dither control for NCO** — NCO 的抖动控制 `on` (默认) | `off`

选中此复选框时，模块根据您在 **Number of NCO dither bits** 中指定的抖动位数对 NCO 信号应用抖动。默认情况下，选中此复选框。

#### 依赖项

要启用此参数，请将 **Type of
oscillator** 设置为 `NCO`。

### **Number of NCO dither bits** — NCO 抖动位数 `4` (默认) | 正整数

将 NCO 抖动位数指定为小于 **Number of NCO
accumulator bits** 中累加器位数的整数标量。

#### 依赖项

要启用此参数，请将 **Type of
oscillator** 设置为 `NCO` 并选择 **Dither control for NCO** 参数。

### **Sample rate mode** — 指定输入采样率的模式 `Use normalized frequency (0 to 1)` (默认) | `Specify on dialog` | `Inherit from input port`

*自 R2024b 起*

使用以下选项之一指定输入采样率：

- `Use normalized frequency (0 to
  1)` –– 以归一化频率单位 (0 到 1) 指定中心频率、双侧带宽和阻带频率。
- `Specify on dialog` –– 在模块对话框中使用 **Input sample rate (Hz)** 参数指定输入采样率。
- `Inherit from input port` –– 模块从输入信号继承采样率。模块将采样率计算为 `N`/*Ts*，其中 *N* 是输入信号的帧大小，*Ts* 是输入信号的采样时间。

### **Input sample rate (Hz)** — 输入信号的采样率 `30e6` (默认) | 正标量

将输入信号的采样率指定为以 Hz 表示的正标量，该标量大于或等于 **Center frequency of output
signal** 中值的两倍。

#### 依赖项

要启用此参数，请将 **Sample rate mode** 参数设置为
`Specify on dialog`。*（自 R2024b 起）*

### **View Filter Response** — View Filter Response 按钮

点击此按钮以打开 Filter Visualization Tool (FVTool)，并显示 Digital Down-Converter 中每一级的幅值和相位响应以及各级的级联响应。该响应基于您在模块参数对话框中指定的值。对这些参数所做的更改会更新 FVTool。

要在 FVTool 运行时更新幅值响应，请修改对话框中的参数，然后点击 **Apply**。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (默认) | `Code generation`

指定要运行的仿真类型。可以将此参数设置为：

- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但可提供更快的后续仿真。

### Data Types 选项卡

### **Stage input** — 级输入 `Inherit: Same as input` (默认) | `fixdt([],16,0)`

指定第一、第二和第三滤波级中输入的数据类型。可以将此参数设置为以下之一：

- `Inherit: Same as input`
  (默认) — 模块从输入信号继承 **Stage
  input** 数据类型。
- `fixdt([],16,0)` — 模块使用带二进制小数点定标的定点数据类型。将此数据类型的符号模式指定为 `[]` 或 `true`。
- 计算结果为数据类型的表达式，例如 `numerictype([],16,15)`。将此数据类型的符号模式指定为 `[]` 或 `true`。

有关设置 stage input 参数的帮助，您可以点击 **Show data type assistant** 按钮以显示数据类型助手。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output** — 输出 `Inherit: Same as input` (默认) | `fixdt([],16,0)`

指定模块输出的数据类型。可以将此参数设置为：

- `Inherit: Same as input`
  (默认) — 模块从输入继承输出数据类型。
- `fixdt([],16,0)` — 模块使用带二进制小数点定标的定点数据类型。将此数据类型的符号模式指定为 `[]` 或 `true`。
- 计算结果为数据类型的表达式，例如 `numerictype([],16,15)`。将此数据类型的符号模式指定为 `[]` 或 `true`。

有关设置 **Output** 参数的帮助，您可以点击 **Show data type assistant** 按钮以显示数据类型助手。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Minimum** — 最小值 `[]` (默认) | 标量

指定模块输出的最小值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

### **Maximum** — 最大值 `[]` (默认) | 标量

模块输出的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。

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

当将 **Sample rate mode** 参数设置为
`Use normalized frequency (0 to 1)` 时，可以以归一化频率单位 (0 到 1) 指定输入信号的双侧带宽、输出信号的中心频率以及阻带频率。

### R2024a：**Simulate using** 参数的默认值变更

**Simulate using** 参数的默认值现在为
`Interpreted execution`。进行此更改后，模块默认使用 MATLAB 解释器进行仿真。

## 描述

将数字信号从中频 (IF) 频带转换到基带并对其进行抽取

Digital Down-Converter (DDC) 模块将中心位于中频 (IF) 的数字化实信号转换为中心位于零频率的基带复信号。DDC 模块使用三级抽取滤波器的级联对频率下变频后的信号进行下采样。此模块根据您在模块对话框中设置的滤波器参数设计抽取滤波器。
