---
type: simulink-block
title: 'FIR Decimation'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'firdecimation'
documentation_source_path: 'ref/firdecimation.html'
language: zh-CN
chinese_source: worker-translation
---

# FIR Decimation

## 端口

### 输入

### **In** — 数据输入 向量 | 矩阵

将数据输入指定为大小为 *P*×*Q* 的向量或矩阵。输入信号中的列表示 *Q* 个独立通道。

当您将 **Input processing** 设置为 `Columns as channels (frame based)` 并将 **Rate options** 设置为 `Enforce single-rate processing` 时，该模块支持可变大小输入信号（帧长度在仿真期间变化）。当该模块接受可变大小输入信号时，它们可以具有任意帧长度，也就是说，输入帧长度不必是抽取因子的整数倍。当您指定固定大小信号时，帧长度在某些条件下可以是任意的。有关更多详细信息，请参阅基于帧的处理和基于采样的处理。

在您将 **Coefficient source** 设置为 **Input port** 之前，此端口是未命名的。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是

### **Num** — 分子系数 向量

将 FIR 滤波器的分子系数指定为向量。

FIR 滤波器的传递函数 *H*(*z*) 由下式给出：

H(z)=b0+b1z−1+...+bNz−N，

您可以使用 DSP System Toolbox™ 滤波器设计函数（如 `designMultirateFIR`、`firnyquist`、`firgr` 或 `firceqrip`）之一生成 FIR 滤波器系数向量 **b** = [*b0*, *b1*, …, *bN*]。

为了充当有效的抗混叠滤波器，系数通常对应于归一化截止频率不大于 1/*M* 的低通滤波器，其中 *M* 是抽取因子。要设计此类滤波器，请使用 `designMultirateFIR` 函数。

通过 **Num** 获得的系数值是可调的，也就是说，它们可以在仿真期间更改，而它们的属性必须保持不变。

**Num** 输入的数据类型必须与 **In** 输入的数据类型匹配。

#### 依赖关系

当您将 **Coefficient source** 设置为 **Input port** 时，**Num** 输入端口出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是
### 输出

### **Out** — 抽取器输出 向量 | 矩阵

FIR Decimator 模块的输出，以向量或矩阵形式返回。

当您将 **Rate options** 设置为：

- `Enforce single-rate processing` —— 该模块保持输入采样率，并通过将输出帧大小减小 *M* 倍来对信号进行抽取。

  对于大小为 *P*×*Q* 的输入，输出的上限大小为 `ceil`(*P*/*M*)×*Q*。
- `Allow multirate processing` —— 该模块对信号进行抽取，使得输出采样率比输入采样率慢 *M* 倍。

  输出帧大小与输入帧大小相同。

有关更多详细信息，请参阅基于帧的处理和基于采样的处理。

在您将 **Coefficient source** 设置为 **Input port** 之前，此端口是未命名的。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是

## 参数

#### 系数来源

### **Coefficient source** — FIR 滤波器系数来源 **Auto**（默认）| **Dialog parameters** | **Input port** | **Filter object**

将 FIR 滤波器系数来源指定为以下之一：

- **Dialog parameters** —— 通过模块对话框中的 **FIR filter coefficients** 参数指定滤波器系数。
- **Input port** —— 通过 **Num** 输入端口指定滤波器系数。
- **Filter object** —— 使用 `dsp.FIRDecimator` System object™ 指定滤波器。
- **Auto** —— 当您选择 **Auto** 时，该模块使用您在 **Decimation factor** 中指定的抽取因子设计 FIR 抽取器。`designMultirateFIR` 函数设计滤波器并返回该模块使用的系数。

  有关滤波器设计的更多信息，请参阅 Orfanidis [2]。

#### 主选项卡

### **FIR filter coefficients** — 低通 FIR 滤波器系数 `designMultirateFIR(1,2)`（默认）| 向量

将低通 FIR 滤波器系数指定为按 *z* 的降幂排列的向量。默认情况下，`designMultirateFIR(1,2)` 计算滤波器系数。

FIR 滤波器的传递函数 *H*(*z*) 由下式给出：

H(z)=b0+b1z−1+...+bNz−N，

您可以使用 DSP System Toolbox 滤波器设计函数（如 `designMultirateFIR`、`firnyquist`、`firgr` 或 `firceqrip`）之一生成 FIR 滤波器系数向量 **b** = [*b0*, *b1*, …, *bN*]。

为了充当有效的抗混叠滤波器，系数通常对应于归一化截止频率不大于 1/*M* 的低通滤波器，其中 *M* 是抽取因子。要设计此类滤波器，请使用 `designMultirateFIR` 函数。

该模块在内部将所有滤波器状态初始化为零。

#### 依赖关系

此参数仅在您将 **Coefficient source** 设置为 **Dialog parameters** 时出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
**复数支持：** 是

### **Decimation factor** — 抽取因子 `2`（默认）| 正标量

指定整数因子 *M*。该模块将输入序列的采样率降低此因子。

#### 依赖关系

此参数仅在您将 **Coefficient source** 设置为 **Dialog parameters**、**Input port** 或 **Auto** 时出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Filter structure** — FIR 滤波器结构 `Direct form`（默认）| `Direct form transposed`

将 FIR 滤波器结构指定为 `Direct form` 或 `Direct form transposed`。

#### 依赖关系

此参数仅在您将 **Coefficient source** 设置为 **Dialog parameters**、**Input port** 或 **Auto** 时出现。

### **Filter object** — 滤波器对象 `dsp.FIRDecimator`

指定您希望该模块实现的多速率滤波器对象的名称。您必须将该滤波器指定为 `dsp.FIRDecimator` System object。

您可以直接在模块对话框中定义 System object。或者，您可以在 MATLAB® 工作区变量中定义该对象，并在模块对话框中指定该变量。

有关创建 System object 的信息，请参阅 Define Basic System Objects。

#### 依赖关系

此参数仅在您将 **Coefficient source** 设置为 **Filter object** 时出现。

### **Input processing** — 处理输入信号的方法 `Columns as channels (frame based)`（默认）| `Elements as channels (sample based)`

指定该模块应如何处理输入。您可以将此参数设置为以下选项之一：

- `Columns as channels (frame based)` —— 当您选择此选项时，该模块将输入的每一列视为一个单独的通道。
- `Elements as channels (sample based)` —— 当您选择此选项时，该模块将输入的每个元素视为一个单独的通道。

### **Rate options** — 模块对输入进行抽取的方法 `Enforce single-rate processing`（默认）| `Allow multirate processing`

指定该模块应对输入进行抽取的方法。您可以选择以下选项之一：

- `Enforce single-rate processing` —— 当您选择此选项时，该模块保持输入采样率，并通过将输出帧大小减小 *M* 倍来对信号进行抽取。要选择此选项，您必须将 **Input processing** 参数设置为 `Columns as channels (frame based)`。

  当您将 **Rate options** 参数设置为 `Enforce single-rate processing` 时，您可以在触发子系统内使用 FIR Decimation 模块。
- `Allow multirate processing` —— 当您选择此选项时，该模块对信号进行抽取，使得输出采样率比输入采样率慢 *M* 倍。

### **Allow arbitrary frame length for fixed-size input signals** — 允许固定大小输入信号的任意帧长度 off（默认）| on

指定固定大小输入信号（其大小在仿真期间不变）是否可以具有任意帧长度，其中帧长度不必是抽取因子的整数倍。该模块仅对固定大小输入信号使用此参数设置，如果输入具有可变大小，则忽略此参数。

当输入信号是可变大小信号时，该信号可以具有任意帧长度，也就是说，帧长度不必是抽取因子的整数倍。

对于固定大小输入信号，如果您：

- 选择 **Allow arbitrary frame length for fixed-size input signals** 参数，则信号的帧长度不必是抽取因子的整数倍。如果输入不是抽取因子的整数倍，则输出通常是可变大小信号。因此，为了支持任意输入大小，该模块还必须支持可变大小操作，您可以通过选择 **Allow arbitrary frame length for fixed-size input signals** 参数来启用该操作。
- 清除 **Allow arbitrary frame length for fixed-size input signals** 参数，则输入帧长度必须是抽取因子的整数倍。

#### 依赖关系

要启用此参数，请将 **Input processing** 设置为 `Columns as channels (frame based)`，并将 **Rate options** 设置为 `Enforce single-rate processing`。

### **Output buffer initial conditions** — 初始条件 `0`（默认）| 标量 | 矩阵

当您将 FIR Decimation 模块设置为基于帧的处理模式时，该模块可能表现出一帧延迟。在一帧延迟的情况下，此参数指定在第一个滤波输入样本可用之前该模块的输出。将此参数指定为要应用于所有信号通道的标量值，或指定为包含每个通道一个值的矩阵。

当输入帧大小大于 1，并且您将 FIR Decimation 模块的 **Input processing** 和 **Rate options** 参数设置如下时，可能会出现一帧延迟的情况：

- **Input processing** 设置为 `Columns as channels (frame based)`
- **Rate options** 设置为 `Allow multirate processing`

有关 FIR Decimation 模块中延迟的更多信息，请参阅延迟。

#### 依赖关系

此参数仅在您通过将 **Rate options** 设置为 `Allow multirate processing` 来配置该模块执行多速率处理时出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
**复数支持：** 是

### **View Filter Response** — 查看滤波器响应 按钮

单击此按钮可打开滤波器可视化工具（`fvtool`），并显示模块对话框中定义的滤波器的滤波器响应。

#### 数据类型选项卡

### **Rounding mode** — 舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择定点运算的舍入模式。默认值为 `Floor`。滤波器系数不遵循此参数，始终舍入为 `Nearest`。

**注意**

当以下所有条件都存在时，**Rounding mode** 和 **Saturate on integer overflow** 设置对数值结果没有影响：

- **Product output** 为 `Inherit: Inherit via internal rule`
- **Accumulator** 为 `Inherit: Inherit via internal rule`
- **Output** 为 `Inherit: Same as accumulator`

在这些数据类型设置下，该模块实际上以全精度模式运行。

### **Saturate on integer overflow** — 整数溢出时饱和 `off`（默认）| `on`

当您选择此参数时，该模块对其定点运算的结果进行饱和处理。当您清除此参数时，该模块对其定点运算的结果进行环绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

**注意**

当满足以下所有条件时，**Rounding mode** 和 **Saturate on integer overflow** 参数对数值结果没有影响：

- **Product output** 数据类型为 `Inherit: Inherit via internal rule`。
- **Accumulator** 数据类型为 `Inherit: Inherit via internal rule`。

在这些数据类型设置下，该模块以全精度模式运行。

### **Coefficients Data Type** — 系数数据类型 `Inherit: Same word length as input`（默认）| `fixdt(1,16)` | `fixdt(1,16,0)`

指定系数数据类型。有关说明此模块中系数数据类型使用的图示，请参阅定点数据类型和乘法数据类型。

您可以将此参数设置为以下之一：

- `Inherit: Same word length as input`
- `fixdt(1,16,0)` 或 `fixdt(1,16)` —— 指定一个数据类型对象。

单击 **Show data type assistant** 按钮 Double greater than symbols 以显示 **Data Type Assistant**，它可帮助您设置 **Coefficients** 参数。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 依赖关系

此参数仅在您将 **Coefficient source** 设置为 `Dialog parameters`、`Filter object` 或 `Auto` 时出现。

当 **Coefficient source** 设置为 `Filter object` 时，**Coefficients** 参数自动设置为 `Same word length as input`。

### **Coefficients Minimum** — 滤波器系数的最小值 `[]`（默认）| 标量

指定滤波器系数的最小值。默认值为 `[]`（未指定）。Simulink® 软件使用此值对定点数据类型执行自动定标。

#### 依赖关系

此参数仅在您将 **Coefficient source** 设置为 `Dialog parameters` 或 `Auto` 时出现。

### **Coefficients Maximum** — 滤波器系数的最大值 `[]`（默认）| 标量

指定滤波器系数的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值对定点数据类型执行自动定标。

#### 依赖关系

此参数仅在您将 **Coefficient source** 设置为 `Dialog parameters` 或 `Auto` 时出现。

### **Product output Data Type** — 乘积输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `fixdt(1,16,0)`

指定乘积输出数据类型。有关说明此模块中乘积输出数据类型使用的图示，请参阅定点数据类型和乘法数据类型。

您可以将此参数设置为以下之一：

- `Inherit: Inherit via internal rule`

  有关此规则的更多信息，请参阅 Inherit via Internal Rule。
- `Inherit: Same as input`
- `fixdt(1,16,0)` —— 指定一个数据类型对象。

单击 **Show data type assistant** 按钮 Double greater than symbols 以显示 **Data Type Assistant**，它可帮助您设置 **Product output** 参数。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 依赖关系

当 **Coefficient source** 设置为 `Filter object` 时，**Product output** 参数自动设置为 `Full precision`。

### **Accumulator Data Type** — 累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

指定累加器数据类型。有关此模块中累加器数据类型使用的图示，请参阅定点数据类型。

您可以将此参数设置为以下值之一：

- `Inherit: Inherit via internal rule`。

  有关此规则的详细信息，请参阅通过内部规则继承。
- `Inherit: Same as input`
- `Inherit: Same as product output`
- `fixdt(1,16,0)` –– 指定数据类型对象。

点击 **Show data type assistant** 按钮
Double greater than symbols 以显示 **Data Type
Assistant**，它可帮助您设置
**Accumulator** 参数。

有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 依赖关系

当 **Coefficient source** 设置为
`Filter object` 时，
**Accumulator** 参数自动设置为
`Full precision`。

### **Output Data Type** — 输出数据类型 `Inherit: Same as accumulator`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

指定输出数据类型。有关此模块中输出数据类型使用的图示，请参阅定点数据类型。

您可以将其设置为以下值之一：

- `Inherit: Same as accumulator`
- `Inherit: Same as input`
- `Inherit: Same as product output`
- `fixdt(1,16,0)` –– 指定数据类型对象。

点击 **Show data type assistant** 按钮
Double greater than symbols 以显示 **Data Type
Assistant**，它可帮助您设置
**Output** 参数。

有关详细信息，请参阅控制信号的数据类型 (Simulink)。

#### 依赖关系

当 **Coefficient source** 设置为
`Filter object` 时，
**Output** 参数自动设置为
`Same as accumulator`。

### **Output Minimum** — 模块输出的最小值 `[]`（默认）| 标量

指定模块应输出的最小值。默认值为
`[]`（未指定）。Simulink 软件使用此值来执行：

- 仿真范围检查（请参阅指定信号范围 (Simulink)）
- 定点数据类型的自动定标

#### 依赖关系

此参数仅在将 **Coefficient
source** 设置为 `Dialog parameters`、
`Input port` 或
`Auto` 时显示。

### **Output Maximum** — 模块输出的最大值 `[]`（默认）| 标量

指定模块应输出的最大值。默认值为
`[]`（未指定）。Simulink 软件使用此值来执行：

- 仿真范围检查（请参阅指定信号范围 (Simulink)）
- 定点数据类型的自动定标

#### 依赖关系

此参数仅在将 **Coefficient
source** 设置为 `Dialog parameters`、
`Input port` 或
`Auto` 时显示。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。

## 所属库

DSP System Toolbox / Filtering / Multirate Filters DSP System Toolbox HDL Support / Filtering

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

生成的代码在某些条件下依赖于 `memcpy` 或
`memset` 函数（`string.h`）。

**使用 Intel® AVX2 代码替换库生成 SIMD 代码**

**注意**

需要 Embedded Coder® 许可证

FIR Decimation 模块在以下条件下支持使用 Intel AVX2 代码替换库生成 SIMD 代码：

- **Filter structure** 设置为 `Direct
  form`。
- **Input processing** 设置为 `Columns
  as channels (frame based)`。
- **Rate options** 设置为 `Enforce
  single-rate processing`。
- 清除 **Allow arbitrary frame length for fixed-size input
  signals** 参数。
- 输入信号为实值且滤波器系数为实数。
- 输入信号为复值且滤波器系数为实数或复数。
- 输入信号的数据类型为 `single` 或
  `double`。

要使用此工作流从此模块生成 SIMD 代码，请参阅使用 Intel AVX2 代码替换库从 Simulink 模块生成 SIMD 代码。

**通过利用目标硬件指令集扩展生成 SIMD 代码** *(自 R2023a 起)*

**注意**

需要 Simulink
Coder™ 或 Embedded Coder 许可证

在以下条件下，您可以通过使用模型配置参数
**Leverage target hardware instruction set extensions**，为所有 Intel 平台、ARM®
Cortex®-A 处理器和 Apple 芯片处理器上的 FIR Decimation 模块生成 SIMD 代码：

- 您将 FIR Decimation 模块的 **Filter structure** 设置为 `Direct
  form`
- 您将 **Input processing** 设置为 `Columns
  as channels (frame based)`
- 输入信号为实值且滤波器系数为实数
- 输入信号为复值且滤波器系数为实数或复数。
- 输入信号的数据类型为 `single`
  （ARM
  Cortex-A 处理器）
- 输入信号的数据类型为 `single` 或
  `double`（Intel 平台）

此外，请适当配置您的模型。在 Simulink 模型窗口的
**Modeling** 选项卡中，点击 **Model Settings**，然后在 **Code Generation** 下配置
这些参数。

- 在 **Optimization** 窗格中：

  - 在
    **Leverage target hardware instruction set
    extensions** 参数中提供特定的指令集。
  - 选择 **Optimize reductions**
    参数。
  - 在 **Optimization levels** 下，将
    **Level** 设置为
    `Maximum`，将
    **Priority** 设置为 `Maximize
    execution speed`。
- 在 **Interface** 窗格中，在 **Software
  environment** 下，清除 **non-finite
  numbers**。

要使用此工作流从此模块生成 SIMD 代码，请参阅使用目标硬件指令集扩展从 Simulink 模块生成 SIMD 代码（适用于 Intel 平台）、使用目标硬件指令集扩展从 Simulink 模块生成 SIMD 代码（适用于 Apple 芯片）以及使用目标硬件指令集扩展从 Simulink 模块生成 SIMD 代码（适用于 ARM Cortex-A 处理器）。

对于受支持模块上的计算密集型操作，SIMD 内建函数可以显著提高 Intel 平台上生成代码的性能。有关更多详细信息，请参阅使用 SIMD 优化归约操作的代码 (Simulink Coder)。

有关 DSP System Toolbox 中 SIMD 代码生成的更多信息，请参阅 SIMD 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**注意**

对于具有硬件友好控制信号和 Simulink 中 HDL 延迟仿真的 FIR 抽取滤波器，或者对于具有复数系数的复数数据，请使用 FIR Decimator (DSP HDL Toolbox) 模块代替此模块。

**HDL 架构**

该模块具有 `HDLDataPath` 作为默认
架构。此架构提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 模块属性**

| HDL 模块属性 | 描述 |
| --- | --- |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **FlattenFilter** | 从生成的 HDL 代码中移除 Filter 子系统的层次结构。默认值为 `auto`。请参阅 FlattenHierarchy (HDL Coder)。 |
| **DSPStyle** | 乘法器映射的综合属性。默认值为 `none`。另请参阅 DSPStyle (HDL Coder)。 |
| **SharingFactor** | 映射到单个共享资源的功能等效资源数。默认值为 0。另请参阅资源共享 (HDL Coder)。 |
| **StreamingFactor** | 被时间复用以转换为串行标量数据路径的并行数据路径或向量数。默认值为 0，表示实现完全并行的数据路径。另请参阅流式处理 (HDL Coder)。 |
| **ConstMultiplierOptimization** | 规范符号数字 (CSD) 或因式分解 CSD 优化。默认值为 `none`。另请参阅 ConstMultiplierOptimization (HDL Coder)。 |
| **MultiplerArchitecture** | 将乘法器架构选择为 `linear` 或 `shiftadd`。默认值为 `linear`。有关更多信息，请参阅 Product, Matrix Multiply (Simulink) 中的 HDL 代码生成部分。 |
| **MultiplierInputPipeline** | 指定在滤波器乘法器输入端添加的流水线级数。另请参阅 MultiplierInputPipeline (HDL Coder)。 |
| **MultiplierOutputPipeline** | 指定在滤波器乘法器输出端添加的流水线级数。另请参阅 MultiplierOutputPipeline (HDL Coder)。 |
| **AdderChainArchitecture** | 选择加法器架构以生成线性链或树形结构的加法器来计算元素之和。默认值为 `tree`。有关更多信息，请参阅 Sum (Simulink) 中的 HDL 代码生成部分。 |
| **AdderOutputPipeline** | 在生成代码中为加法运算插入的输出流水线级数。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**数据类型支持**

该模块支持以下数据类型用于 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 枚举 | 复数信号 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | 标量  向量  矩阵 | 是 | Half  Single  Double | 是 | 是 | 是 | 是 | 是 |

**优化**

该模块参与以下 HDL 优化以优化速度和
面积。

**面积优化**

| 优化 | 描述 |
| --- | --- |
| 资源共享 (HDL Coder) | *资源共享*是一种面积优化，HDL Coder 在其中识别多个功能等效资源并将其替换为单个资源。 |
| 流式处理 (HDL Coder) | *流式处理*是一种面积优化，HDL Coder 在其中将向量数据路径转换为标量数据路径（或转换为多个较小尺寸的向量数据路径）。 |

**速度优化**

| 优化 | 描述 |
| --- | --- |
| 分布式流水线 (HDL Coder) | *分布式流水线*，或寄存器重定时，是一种速度优化，它移动设计中的现有延迟以减少关键路径，同时保持功能行为。 |
| 时钟速率流水线 (HDL Coder) | *时钟速率流水线*是 HDL Coder 中的一种优化框架，允许其他速度和面积优化在时钟速率下引入延迟。 |
| 自适应流水线 (HDL Coder) | *自适应流水线*优化创建带有寄存器的模块模式或组合，通过向设计中的模块插入流水线寄存器，可以提高可实现的时钟频率并减少 FPGA 板上的面积使用。 |
| 关键路径估计 (HDL Coder) | 要快速识别设计中可能的关键路径，请使用*关键路径估计*。关键路径估计加速了查找关键路径的迭代过程。要了解在关键路径估计中被表征的模块，请参阅已表征模块 (HDL Coder)。 |

**限制和注意事项**

该模块具有以下限制：

- 您必须将 **Initial conditions** 设置为零。不支持非零初始状态的 HDL 代码
  生成。
- 当您选择 **Dialog parameters** 时，以下
  定点选项不支持 HDL 代码生成：

  - `Slope and Bias scaling`
- 不支持可编程系数。
- 基于帧的输入滤波器不支持：

  - 可复位和使能子系统
  - 具有复数系数的复数输入信号。您可以使用
    复数输入信号和实数系数，或复数
    系数和实数输入信号。
  - 共享和流式处理优化

要为基于帧的输入配置 FIR Decimation 模块，
请使用以下模块设置：

|  |  |
| --- | --- |
| **基于帧的输入** | HDL Coder 支持对 FIR Decimation 模块使用向量输入，其中向量的每个元素代表一个时间采样。您可以使用最多 512 个采样的输入向量。基于帧的实现支持定点输入和输出数据类型，并使用全精度内部数据类型。输出是缩减大小的列向量，对应于您的抽取因子。您可以使用实数系数和实数输入信号、实数系数和复数输入信号，或复数系数和实数输入信号。  1. 将列向量信号连接到 FIR    Decimation 模块输入端口。 2. 将 **Input processing** 指定为    `Columns as channels (frame    based)`。 3. 将 **Rate options** 设置为    `Enforce single-rate    processing`。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2024b：为 Apple 芯片处理器生成 SIMD 代码

在 R2024b 中，如果您拥有 Embedded Coder，您可以通过使用模型配置参数
**Leverage target hardware instruction set extensions**，为 Apple 芯片处理器的 FIR Decimation
模块生成 SIMD 代码。有关
更多信息，请参阅使用目标硬件指令集扩展从 Simulink 模块生成 SIMD 代码（适用于 Apple 芯片）。

### R2024a：为 ARM Cortex-A 处理器生成 SIMD 代码

在 R2024a 中，如果您拥有 Embedded Coder，您可以通过使用模型配置参数
**Leverage target hardware instruction set extensions**，为 ARM
Cortex-A 处理器的 FIR Decimation
模块生成 SIMD 代码。

### R2023b：为复数信号生成 SIMD 代码

在 R2023b 中，如果您拥有 Embedded Coder，当输入信号为复值时，您可以通过使用模型配置
参数 **Leverage target hardware instruction set
extensions** 为 FIR Decimation
模块生成 SIMD 代码。

### R2023a：在所有 Intel 平台上为 FIR Decimation 模块生成 SIMD 代码

在 R2023a 中，如果您拥有 Embedded Coder，您可以通过使用模型配置参数
**Leverage target hardware instruction set extensions**，在所有 Intel 平台上为 FIR Decimation
模块生成 SIMD 代码。
以前，您必须使用代码替换库来生成 SIMD 代码。有关
更多详细信息，请参阅代码生成。

### R2022b：支持任意输入帧长度

从 R2022b 开始，此模块在以下情况下支持具有任意帧长度的输入信号：

- 输入信号为固定大小信号（帧长度在仿真期间不变）且模块允许多速率处理
- 输入信号为固定大小信号，模块强制执行单速率处理，并且您选择 **Allow arbitrary frame length
  for fixed-size input signals** 参数
- 输入信号为可变大小信号（帧长度在仿真期间变化）

当此模块支持任意帧长度输入信号时，输入帧
长度不必是抽取因子的倍数。

有关更多详细信息，请参阅基于帧的处理和基于采样的处理。

## 描述

执行多相 FIR 抽取

FIR 抽取模块使用整数下采样因子 *M* 沿第一维度执行高效的多相抽取。

从概念上讲，FIR 抽取器（如示意图所示）由一个抗混叠 FIR 滤波器后接一个下采样器组成。要设计 FIR 抗混叠滤波器，请使用 `designMultirateFIR` 函数。

FIR 滤波器使用直接型 FIR 滤波器对输入中每个通道的数据进行滤波。
随后的下采样器通过对滤波后数据的每个通道取每第 *M* 个样本并丢弃其后的 *M* – 1 个样本来进行下采样。*M* 是您指定的抽取因子值。所得的离散时间信号的采样率为原始采样率的 1/*M*。

FIR 抽取器包含一个抗混叠 FIR 滤波器，后接一个下采样器。

请注意，实际模块算法实现的是直接型 FIR 多相结构，这是图中所示组合系统的高效等价形式。更多详细信息，请参阅算法。

在特定条件下，此模块还支持 SIMD 代码生成。详细信息，请参阅代码生成。
