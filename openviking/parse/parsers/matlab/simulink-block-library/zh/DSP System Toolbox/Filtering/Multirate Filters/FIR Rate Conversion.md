---
type: simulink-block
title: 'FIR Rate Conversion'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'firrateconversion'
documentation_source_path: 'ref/firrateconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# FIR Rate Conversion

## 端口

### 输入

### **Port\_1(In1)** — 输入信号向量 | 矩阵

指定输入信号为大小为 *P*×*Q* 的向量或矩阵。输入列表示 *Q* 个独立通道。

当将 **Rate options** 设置为 `Enforce single-rate processing` 时，模块支持可变大小输入信号（仿真期间帧长度发生变化）。当模块接受可变大小输入信号时，这些信号可以具有任意帧长度，也就是说，输入帧长度不必是抽取因子的倍数。对于固定大小信号，帧长度在某些条件下可以是任意的。有关更多详细信息，请参阅基于帧的处理。

当模块输入为定点时，所有内部数据类型均为有符号定点。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** Yes

### 输出

### **Port\_1(Out1)** — 速率转换后的信号向量 | 矩阵

速率转换后的信号，以向量或矩阵形式返回。

当将 **Rate options** 参数设置为：

- `Enforce single-rate processing`
  –– 模块保持输入采样率，并通过将输出帧大小更改 *L*/*M* 倍来重新采样信号。

  对于大小为 *P*×*Q* 的输入，输出的上限大小为
  `ceil`(*LP*/*M*)×*Q*。
- `Allow multirate processing` ––
  模块对信号进行抽取，使输出信号采样率为输入采样率的 *L*/*M* 倍。

  输出帧大小与输入帧大小相同，
  *Fo* =
  (*L*/*M*)×*Fi*

  连接到输出的所有模块以
  *Fo* 运行，连接到输入的所有模块以
  *Fi* 运行。

  有关更多详细信息，请参阅基于帧的处理。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** Yes

## 参数

### **Coefficient source** — 操作模式 **Auto** (默认) | **Dialog parameters** | **Filter object**

FIR Rate Conversion 模块可以在三种不同模式下运行。在 **Coefficient source** 分组框中选择模式。

- **Dialog parameters** — 在模块对话框中输入有关滤波器的信息，例如 FIR 滤波器系数。
- **Filter object** — 使用 `dsp.FIRRateConverter` System object™ 指定滤波器。
- **Auto** (默认) — 模块确定滤波器系数。

FIR Rate Conversion 模块对话框中的设置会根据所选模式而变化。

### 主选项卡

### **Interpolation factor** — 插值因子 `3` (默认) | 正整数

将插值因子 *L* 指定为正整数。模块在对信号进行滤波之前按此值对信号进行上采样。

#### 依赖关系

要启用此参数，请将 **Coefficient source** 设置为 **Dialog parameters** 或 **Auto**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **FIR filter coefficients** — FIR 滤波器系数 `designMultirateFIR(3,2)` (默认) | 向量

按 *z* 的降幂指定 FIR 滤波器系数。默认情况下，模块使用 `designMultirateFIR(3,2)` 函数计算滤波器系数。

#### 依赖关系

要启用此参数，请将 **Coefficient source** 设置为 **Dialog parameters**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
**复数支持：** Yes

### **Decimation factor** — 抽取因子 `2` (默认) | 正整数

将抽取因子 *M* 指定为正整数。模块在对信号进行滤波后按此值对信号进行下采样。

#### 依赖关系

要启用此参数，请将 **Coefficient source** 设置为 **Dialog parameters** 或 **Auto**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Rate options** — 强制单速率处理或允许多速率处理 `Enforce single-rate processing` (默认) | `Allow multirate processing`

指定是强制单速率处理还是允许多速率处理。

- `Enforce single-rate processing`
  –– 输出帧大小 *Po* 是输入帧大小 *Pi* 的 *L*/*M* 倍，其中 *L* 是插值因子，*M* 是抽取因子。

  *Po* =
  (*L*/*M*)×*Pi*

  Simulink® 中的输出信号速率等于输入信号速率。

  *Fo* =
  *Fi*
- `Allow multirate processing` ––
  输出帧大小等于输入帧大小。

  *Po* =
  *Pi*

  Simulink 中的输出信号速率是输入信号速率的 *L*/*M* 倍。

  *Fo* =
  (*L*/*M*)×*Fi*

  连接到输出的所有模块以 *Fo* 运行，连接到输入的所有模块以 *Fi* 运行。

### **Filter object** — 滤波器对象 `FRC` (默认) | `dsp.FIRRateConverter` System object

指定希望模块实现的多速率滤波器对象。指定的滤波器对象必须是 `dsp.FIRRateConverter` System object。

可以在模块封装中或 MATLAB® 工作区变量中定义 System object。

有关创建 System object 的信息，请参阅定义基本 System Object。

#### 依赖关系

当 **Coefficient source** 设置为 **Filter object** 时，将显示此参数。

### **Allow arbitrary frame length for fixed-size input signals** — 允许固定大小输入信号的任意帧长度 off (默认) | on

指定固定大小输入信号（其大小在仿真期间不变）是否可以具有任意帧长度，其中帧长度不必是抽取因子的倍数。模块仅对固定大小输入信号使用此参数设置，如果输入为可变大小，则忽略此参数。

当输入信号为可变大小信号时，该信号可以具有任意帧长度，也就是说，帧长度不必是抽取因子的倍数。

对于固定大小输入信号，如果您：

- 选择 **Allow arbitrary frame length for fixed-size input signals** 参数，则信号的帧长度不必是抽取因子的倍数。如果输入不是抽取因子的倍数，则输出通常是可变大小信号。因此，为支持任意输入大小，模块还必须支持可变大小运算，您可以通过选择 **Allow arbitrary frame length for fixed-size input signals** 参数来启用该支持。
- 清除 **Allow arbitrary frame length for fixed-size input signals** 参数，则输入帧长度必须是抽取因子的倍数。

#### 依赖关系

要启用此参数，请将 **Rate options** 设置为 `Enforce single-rate processing`。

### **View Filter Response** — 可视化滤波器响应按钮

选择此参数以打开滤波器可视化工具 `fvtool`，并显示 FIR 滤波器的幅值响应。该响应基于模块对话框中选择的参数。对这些参数所做的更改会更新 `fvtool`。

要在 `fvtool` 运行时更新幅值响应，请修改模块参数并单击 **应用**。

要同时查看幅值响应和相位响应，请单击工具栏上的 **幅值和相位响应** 按钮。

### 数据类型选项卡

当 **Coefficient source** 设置为 **Filter object** 时，在 **主选项卡** 上指定的滤波器对象的定点设置会显示在 **数据类型选项卡** 上。不能直接在模块对话框中更改这些设置。要更改定点设置，必须编辑滤波器对象。

有关 System object 的详细信息，请参阅什么是 System Object？

当 **Coefficient source** 设置为 **Auto** 时，模块会自动选择滤波器系数。有关模块使用的滤波器设计算法的更多信息，请参阅指定 FIR 滤波器系数。

### **Rounding mode** — 舍入方法 `Floor` (默认) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅舍入模式。

滤波器系数不遵循此参数，始终舍入为 `Nearest`。

**注意**

当满足以下所有条件时，**Rounding mode** 和 **Saturate on integer overflow** 参数对数值结果没有影响：

- **Product output** 数据类型为 `Inherit: Inherit via internal rule`。
- **Accumulator** 数据类型为 `Inherit: Inherit via internal rule`。
- **Output** 数据类型为 `Inherit: Same as accumulator`。

使用这些数据类型设置时，模块以全精度模式运行。

#### 依赖关系

要启用此参数，请将 **Coefficient source** 设置为 **Dialog parameters** 或 **Auto**。

### **Saturate on integer overflow** — 溢出处理方法 off (默认) | on

选择此参数可对定点运算的结果进行饱和处理。清除此参数可对定点运算的结果进行回绕处理。有关 *饱和* 和 *回绕* 的详细信息，请参阅定点运算的溢出处理。

**注意**

当满足以下所有条件时，**Rounding mode** 和 **Saturate on integer overflow** 参数对数值结果没有影响：

- **Product output** 数据类型为 `Inherit: Inherit via internal rule`。
- **Accumulator** 数据类型为 `Inherit: Inherit via internal rule`。

使用这些数据类型设置时，模块以全精度模式运行。

#### 依赖关系

仅当 **Coefficient source** 设置为 **Dialog parameters** 或 **Auto** 时，此参数才可编辑。

### **Coefficients** — 系数的数据类型 `Inherit: Same word length as input` (默认) | `fixdt(1,16)` | `fixdt(1,16,0)`

**Coefficients** 指定滤波器系数的数据类型。

- `Inherit: Same word length as input`
  –– 模块从定点输入继承系数的字长。小数长度根据系数值确定，以获得最佳可能精度。
- `fixdt(1,16)` –– 系数的数据类型为有符号、二进制小数点定标定点数据类型，字长为 16 位。
- `fixdt(1,16,0)` –– 系数的数据类型为有符号、二进制小数点定标定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **数据类型助手** 设置 **Coefficients** 数据类型。要使用助手，请单击 **显示数据类型助手** 按钮。

有关数据类型助手的更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

有关此模块如何使用滤波器系数数据类型的图示，请参阅定点数据类型。

#### 依赖关系

仅当 **Coefficient source** 设置为 **Dialog parameters** 或 **Auto** 时，此参数才可编辑。

### **Coefficients Minimum** — 滤波器系数的最小值 `[]` (默认) | 标量

指定滤波器系数的最小值。Simulink 使用此最小值执行定点数据类型的自动定标。

### **Coefficients Maximum** — 滤波器系数的最大值 `[]` (默认) | 标量

指定滤波器系数的最大值。Simulink 使用此最大值执行定点数据类型的自动定标。

### **Product output** — 乘积输出的数据类型 `Inherit: Inherit via internal rule` (默认) | `Inherit: Same as input` | `fixdt(1,16,0)`

**Product output** 指定 FIR Rate Conversion 模块中乘积运算输出的数据类型。

- `Inherit: Inherit via internal rule`
  — 模块基于内部规则继承乘积输出数据类型。有关此规则的更多信息，请参阅通过内部规则继承。
- `Inherit: Same as input` — 模块将乘积输出数据类型指定为与输入数据类型相同。
- `fixdt(1,16,0)` — 模块指定有符号、二进制小数点定标定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **数据类型助手** 设置 **Product output** 数据类型。要使用助手，请单击 **显示数据类型助手** 按钮。

有关数据类型助手的更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

有关此模块如何使用乘积输出数据类型的图示，请参阅定点数据类型。

#### 依赖关系

仅当 **Coefficient source** 设置为 **Dialog parameters** 或 **Auto** 时，此参数才可编辑。

### **Accumulator** — 累加器的数据类型 `Inherit: Inherit via internal rule` (默认) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

**Accumulator** 指定 FIR Rate Conversion 模块中累加运算输出的数据类型。有关此模块如何使用累加器数据类型的图示，请参阅定点数据类型。

- `Inherit: Inherit via internal rule`
  — 模块基于内部规则继承累加器数据类型。有关此规则的更多信息，请参阅通过内部规则继承。
- `Inherit: Same as input` — 模块将累加器数据类型指定为与输入数据类型相同。
- `Inherit: Same as product output`
  — 模块将累加器数据类型指定为与乘积输出数据类型相同。
- `fixdt(1,16,0)` — 模块指定有符号、二进制小数点定标定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **数据类型助手** 设置 **Accumulator** 数据类型。要使用助手，请单击 **显示数据类型助手** 按钮。

有关数据类型助手的更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 依赖关系

仅当 **Coefficient source** 设置为 **Dialog parameters** 或 **Auto** 时，此参数才可编辑。

### **Output** — 输出数据类型 `Inherit: Same as accumulator` (默认) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

**Output** 指定 FIR Rate Conversion 模块输出的数据类型。

- `Inherit: Same as input` — 模块将输出数据类型指定为与输入数据类型相同。
- `Inherit: Same as product output`
  — 模块将输出数据类型指定为与乘积输出数据类型相同。
- `Inherit: Same as accumulator`
  — 模块将输出数据类型指定为与累加器数据类型相同。
- `fixdt(1,16,0)` — 模块指定有符号、二进制小数点定标定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **数据类型助手** 设置 **Output** 数据类型。要使用助手，请单击 **显示数据类型助手** 按钮。

有关数据类型助手的更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

有关此模块如何使用输出数据类型的图示，请参阅定点数据类型。

#### 依赖关系

仅当 **Coefficient source** 设置为 **Dialog parameters** 或 **Auto** 时，此参数才可编辑。

### **Output Minimum** — 模块可输出的最小值 `[]` (默认) | 标量

指定模块可输出的最小值。Simulink 使用此最小值执行：

- 仿真范围检查。有关更多信息，请参阅指定信号范围 (Simulink)。
- 定点数据类型的自动定标。

### **Output Maximum** — 模块可输出的最大值 `[]` (默认) | 标量

指定模块可输出的最大值。Simulink 使用此最大值执行：

- 仿真范围检查。有关更多信息，请参阅指定信号范围 (Simulink)。
- 定点数据类型的自动定标。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。

#### 依赖关系

仅当 **Coefficient source** 设置为 **Dialog parameters** 或 **Auto** 时，此参数才显示。

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

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数 (`string.h`)。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2022b: 支持任意输入帧长度

从 R2022b 开始，当满足以下条件时，此模块支持具有任意帧长度的输入信号：

- 输入信号是固定大小信号（仿真期间帧长度不变），并且模块允许多速率处理
- 输入信号是固定大小信号，模块强制单速率处理，并且您选择 **Allow arbitrary frame length for fixed-size input signals** 参数
- 输入信号是可变大小信号（仿真期间帧长度发生变化）

当此模块支持任意帧长度输入信号时，输入帧长度不必是抽取因子的倍数。

有关更多详细信息，请参阅基于帧的处理。

## 描述

执行多相 FIR 采样率转换

FIR Rate Conversion 模块沿第一维度使用有理因子 *L*/*M* 执行高效的多相采样率转换。该模块将输入的每一列视为单独通道，并随时间独立地对每个通道中的数据进行重新采样。

从概念上讲，速率转换器组合了一个 FIR 内插器，后接一个 FIR 抽取器。以下示意图包含一个上采样器、一个组合的抗镜像和抗混叠 FIR 滤波器以及一个下采样器。要设计一个用作组合抗镜像和抗混叠 FIR 滤波器的 FIR 滤波器，请使用 `designMultirateFIR` 函数。

速率转换器执行以下操作：

1. 通过在输入样本之间插入 *L*−`1` 个零，将输入上采样到更高速率。
2. 使上采样数据通过 FIR 滤波器。
3. 通过在每个模块保留的样本之后丢弃 *M*-`1` 个连续样本，将滤波后的数据下采样到更低速率。

FIR 速率转换器包含一个上采样器，后接一个抗镜像、抗混叠 FIR 滤波器，再接一个下采样器。

请注意，实际模块算法实现的是多相结构，它是图中所示组合系统的高效等效形式。有关更多详细信息，请参阅算法。
