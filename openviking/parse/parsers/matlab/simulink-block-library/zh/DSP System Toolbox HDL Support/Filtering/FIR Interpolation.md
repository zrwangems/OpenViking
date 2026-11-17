---
type: simulink-block
title: 'FIR Interpolation'
family: 'filtering'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'firinterpolation'
documentation_source_path: '../dsp/ref/firinterpolation.html'
language: zh-CN
chinese_source: worker-translation
---

# FIR Interpolation

## 端口

### 输入

### **In** — 数据输入向量 | 矩阵

将数据输入指定为向量或矩阵。

当将 **输入处理** 设置为
`Columns as channels (frame based)` 且将
**速率选项** 设置为 `Enforce
single-rate processing` 时，输入可以是变大小信号。也就是说，信号的帧大小（行数）和通道数（列数）可以在仿真期间更改。

在将 **系数来源** 设置为 **Input port** 之前，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是

### **Num** — 分子系数向量

将 FIR 滤波器的分子系数指定为向量。

FIR 滤波器的传递函数 *H*(*z*) 由下式给出：

H(z)=b0+b1z−1+...+bNz−N,

可以使用 DSP System Toolbox™ 滤波器设计函数之一（如 `designMultirateFIR`、
`firnyquist`、`firgr` 或 `firceqrip`）生成 FIR 滤波器系数向量 **b** =
[*b0*,
*b1*, …,
*bN*]。

为了充当有效的抗成像滤波器，系数通常对应于归一化截止频率不大于插值因子倒数的低通滤波器。要设计此类滤波器，请使用 `designMultirateFIR`
函数。

系数值可调。也就是说，其值可以在仿真期间更改，但其属性（如大小、数据类型和复/实性）不能更改。

**Num** 输入的数据类型必须与 **In** 输入的数据类型匹配。

#### 依赖关系

当将 **系数来源** 设置为 **Input
port** 时，会出现 **Num** 输入端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是
### 输出

### **Out** — 插值器输出向量 | 矩阵

FIR Interpolator 模块的输出，以向量或矩阵形式返回。

当 **速率选项** 设置为：

- `Enforce single-rate processing`
  — 选择此选项时，模块保持输入采样率，并通过将输出帧大小增大 *L* 倍来对信号进行插值。
- `Allow multirate processing` —
  选择此选项时，模块对信号进行插值，使输出采样率比输入采样率快 *L* 倍。

当输入是变大小信号时，输出也是变大小信号。

在将 **系数来源** 设置为 **Input port** 之前，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是

## 参数

#### 系数来源

### **系数来源** — FIR 滤波器系数来源 **Auto** (default) | **Dialog parameters** | **Input port** | **Filter object**

将 FIR 滤波器系数来源指定为以下之一：

- **Dialog parameters** –– 通过模块对话框中的 **FIR 滤波器系数** 参数指定滤波器系数。
- **Input port** –– 通过 **Num** 输入端口指定滤波器系数。
- **Filter object** –– 使用 `dsp.FIRInterpolator`
  System object™ 指定滤波器。
- **Auto** –– 当选择
  **Auto** 时，模块使用在
  **插值因子** 中指定的插值因子设计 FIR
  插值器。`designMultirateFIR`
  函数设计滤波器并返回模块使用的系数。

  有关滤波器设计的更多信息，请参阅 Orfanidis [2]。

#### 主选项卡

### **FIR 滤波器系数** — 低通 FIR 滤波器系数 `designMultirateFIR(3,1)` (default) | vector

指定 FIR 滤波器传递函数
*H*(*z*) 的分子系数。

H(z)=b0+b1z−1+...+bNz−N,

可以使用 DSP System Toolbox 滤波器设计函数之一（如 `designMultirateFIR`、`firnyquist`、`firgr` 或 `firceqrip`）生成 FIR 滤波器系数向量 **b** =
[*b0*,
*b1*, …,
*bN*]。

为了充当有效的抗成像滤波器，系数通常对应于归一化截止频率不大于插值因子倒数的低通滤波器。要设计此类滤波器，
请使用 `designMultirateFIR`
函数。

该模块在内部将所有滤波器状态初始化为零。

#### 依赖关系

仅当将 **系数来源** 设置为 **Dialog parameters** 时，此参数才会出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
**复数支持：** 是

### **插值因子** — 插值因子 `3` (default) | positive scalar

指定整数因子 *L*。模块按此因子增大输入序列的采样率。

#### 依赖关系

仅当将 **系数来源** 设置为 **Dialog parameters**、
**Input port** 或
**Auto** 时，此参数才会出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **滤波器对象** — 滤波器对象 `dsp.FIRInterpolator`

指定希望模块实现的多速率滤波器对象的名称。必须将滤波器指定为 `dsp.FIRInterpolator`
System object。

可以直接在模块对话框中定义 System object。或者，可以在 MATLAB® 工作区变量中定义该对象，并在模块对话框中指定该变量。

有关创建 System object 的信息，请参阅 Define Basic System Objects。

#### 依赖关系

仅当将 **系数来源** 设置为 **Filter object** 时，此参数才会出现。

### **输入处理** — 处理输入信号的方法 `Columns as channels (frame based)` (default) | `Elements as channels (sample based)`

指定模块应如何处理输入。可以将此参数设置为以下选项之一：

- `Columns as channels (frame based)`
  — 选择此选项时，模块将输入的每一列视为单独通道。
- `Elements as channels (sample based)`
  — 选择此选项时，模块将输入的每个元素视为单独通道。

### **速率选项** — 模块对输入进行插值的方法 `Enforce single-rate processing` (default) | `Allow multirate processing`

指定模块应对输入进行插值的方法。可以选择以下选项之一：

- `Enforce single-rate processing`
  — 选择此选项时，模块保持输入采样率，并通过将输出帧大小增大 *L* 倍来对信号进行插值。要选择此选项，必须将 **输入处理** 参数设置为 `Columns as channels (frame based)`。
- `Allow multirate processing` —
  选择此选项时，模块对信号进行插值，使输出采样率比输入采样率快 *L* 倍。

### **输出缓冲区初始条件** — 初始条件 `0` (default) | scalar | matrix

当将 **速率选项** 参数设置为
`Allow multirate processing` 并在 Simulink®
`MultiTasking` 模式下运行模型时，模块会表现出延迟。多速率、多任务操作的延迟量取决于如何设置
**输入处理** 参数。

| 输入处理 | 延迟 |
| --- | --- |
| `Elements as channels (sample based)` | *L* samples |
| `Columns as channels (frame based)` | *L* frames (*Ki* samples per frame) |

当模块表现出延迟时，默认初始条件为零。
或者，可以使用 **输出缓冲区初始条件** 参数指定初始条件矩阵（其中为每个通道包含一个值）或指定模块应用于所有通道的标量初始条件。模块将
**输出缓冲区初始条件** 除以
**插值因子**，并输出缩放后的初始条件，直到第一个滤波后的输入样本可用。

输出缓冲区初始条件以输出数据类型和定标存储。

有关 FIR Interpolation 模块中延迟的更多信息，请参阅 Latency。

#### 依赖关系

仅当通过将 **速率选项** 设置为
`Allow multirate processing` 来配置模块执行多速率处理时，此参数才会出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
**复数支持：** 是

### **查看滤波器响应** — 查看滤波器响应按钮

单击此按钮可打开 Filter Visualization Tool (`fvtool`) 并显示模块对话框中定义的滤波器的响应。

#### 数据类型选项卡

### **舍入模式** — 舍入模式 `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择定点运算的舍入模式。默认值为
`Floor`。滤波器系数不遵循此参数，并始终舍入为
`Nearest`。

**注意**

当以下所有条件都成立时，**舍入模式** 和 **整数溢出时饱和** 设置对数值结果没有影响：

- **乘积输出** 为
  `Inherit: Inherit via internal
  rule`
- **累加器** 为 `Inherit:
  Inherit via internal rule`
- **输出** 为 `Inherit: Same
  as accumulator`

使用这些数据类型设置时，模块实际上以全精度模式运行。

### **整数溢出时饱和** — 整数溢出时饱和 `off` (default) | `on`

选择此参数时，模块会对其定点运算的结果进行饱和处理。清除此参数时，模块会对其定点运算的结果进行环绕处理。有关
`saturate` 和 `wrap` 的详细信息，请参阅 overflow
mode for fixed-point operations。

**注意**

当满足以下所有条件时，**舍入模式** 和 **整数溢出时饱和** 参数对数值结果没有影响：

- **乘积输出** 数据类型为
  `Inherit: Inherit via internal
  rule`。
- **累加器** 数据类型为
  `Inherit: Inherit via internal
  rule`。

使用这些数据类型设置时，模块以全精度模式运行。

### **系数数据类型** — 系数数据类型 `Inherit: Same word length as input` (default) | `fixdt(1,16)` | `fixdt(1,16,0)`

指定系数数据类型。有关此模块中系数数据类型的使用图示，请参阅 Fixed-Point Data Types 和 Multiplication Data Types。

可以将此参数设置为以下之一：

- `Inherit: Same word length as
  input`
- `fixdt(1,16,0)` 或
  `fixdt(1,16)` –– 指定数据类型对象。

单击 **Show data type assistant** 按钮
双大于符号以显示 **Data Type
Assistant**，它有助于设置
**Coefficients** 参数。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 依赖关系

仅当将 **系数来源** 设置为 `Dialog parameters`、
`Filter object` 或
`Auto` 时，此参数才会出现。

当 **系数来源** 设置为
`Filter object` 时，
**Coefficients** 参数会自动设置为
`Same word length as input`。

### **系数最小值** — 滤波器系数的最小值 `[]` (default) | scalar

指定滤波器系数的最小值。默认值为
`[]`（未指定）。Simulink 软件使用此值执行定点数据类型的自动定标。

#### 依赖关系

仅当将 **系数来源** 设置为 `Dialog parameters` 或
`Auto` 时，此参数才会出现。

### **系数最大值** — 滤波器系数的最大值 `[]` (default) | scalar

指定滤波器系数的最大值。默认值为
`[]`（未指定）。Simulink 软件使用此值执行定点数据类型的自动定标。

#### 依赖关系

仅当将 **系数来源** 设置为 `Dialog parameters` 或
`Auto` 时，此参数才会出现。

### **乘积输出数据类型** — 乘积输出数据类型 `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `fixdt(1,16,0)`

指定乘积输出数据类型。有关此模块中乘积输出数据类型的使用图示，请参阅 Fixed-Point Data Types 和 Multiplication Data Types。

可以将此参数设置为以下之一：

- `Inherit: Inherit via internal
  rule`

  有关此规则的更多信息，请参阅 Inherit via Internal Rule。
- `Inherit: Same as input`
- `fixdt(1,16,0)` –– 指定数据类型对象。

单击 **Show data type assistant** 按钮
双大于符号以显示 **Data Type
Assistant**，它有助于设置 **Product
output** 参数。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 依赖关系

当 **系数来源** 设置为
`Filter object` 时，**Product
output** 参数会自动设置为 `Full
precision`。

### **累加器数据类型** — 累加器数据类型 `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

指定累加器数据类型。有关此模块中累加器数据类型的使用图示，请参阅 Fixed-Point Data Types。

可以将此参数设置为以下之一：

- `Inherit: Inherit via internal rule`.

  有关此规则的更多信息，请参阅 Inherit via Internal Rule。
- `Inherit: Same as input`
- `Inherit: Same as product output`
- `fixdt(1,16,0)` –– 指定数据类型对象。

单击 **Show data type assistant** 按钮
双大于符号以显示 **Data Type
Assistant**，它有助于设置
**Accumulator** 参数。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 依赖关系

当 **系数来源** 设置为
`Filter object` 时，
**Accumulator** 参数会自动设置为
`Full precision`。

### **输出数据类型** — 输出数据类型 `Inherit: Same as accumulator` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

指定输出数据类型。有关此模块中输出数据类型的使用图示，请参阅 Fixed-Point Data Types。

可以将其设置为以下之一：

- `Inherit: Same as accumulator`
- `Inherit: Same as input`
- `Inherit: Same as product output`
- `fixdt(1,16,0)` –– 指定数据类型对象。

单击 **Show data type assistant** 按钮
双大于符号以显示 **Data Type
Assistant**，它有助于设置
**Output** 参数。

有关详细信息，请参阅 Control Data Types of Signals (Simulink)。

#### 依赖关系

当 **系数来源** 设置为
`Filter object` 时，
**Output** 参数会自动设置为
`Same as accumulator`。

### **输出最小值** — 模块输出的最小值 `[]` (default) | scalar

指定模块应输出的最小值。默认值为
`[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

#### 依赖关系

仅当将 **系数来源** 设置为 `Dialog parameters`、
`Input port` 或
`Auto` 时，此参数才会出现。

### **输出最大值** — 模块输出的最大值 `[]` (default) | scalar

指定模块应输出的最大值。默认值为
`[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

#### 依赖关系

仅当将 **系数来源** 设置为 `Dialog parameters`、
`Input port` 或
`Auto` 时，此参数才会出现。

### **锁定数据类型设置以防定点工具更改** — 防止定点工具覆盖数据类型 `off` (default) | `on`

选择此参数可防止定点工具覆盖你在模块对话框中指定的数据类型。

## 所属库

DSP System Toolbox / Filtering / Multirate Filters DSP System Toolbox HDL Support / Filtering

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

生成的代码在某些条件下依赖于 `memcpy` 或
`memset` 函数（`string.h`）。

**使用 Intel® AVX2 代码替换库生成 SIMD 代码**

**注意**

需要 Embedded Coder® 许可证

在以下条件下，FIR Interpolation 模块支持使用 Intel AVX2 代码替换库生成 SIMD 代码：

- **输入处理** 设置为 `Columns
  as channels (frame based)`。
- **速率选项** 设置为 `Enforce
  single-rate processing`。
- 输入信号为实值，且滤波器系数为实数。
- 输入信号为复值，且滤波器系数为实数或复数。
- 输入信号的数据类型为 `single` 或
  `double`。

要使用此工作流从此模块生成 SIMD 代码，请参阅 Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks。

**通过利用目标硬件指令集扩展生成 SIMD 代码** *(自 R2023a 起)*

**注意**

需要 Simulink
Coder™ 或 Embedded Coder 许可证

在以下条件下，可以使用模型配置参数
**Leverage target hardware instruction set extensions** 为所有
Intel 平台、ARM®
Cortex®-A 处理器和 Apple 芯片处理器上的 FIR Interpolation 模块生成 SIMD 代码：

- 将 **输入处理** 设置为 `Columns
  as channels (frame based)`
- 输入信号为实值，且滤波器系数为实数
- 输入信号为复值，且滤波器系数为实数或复数。
- 输入信号的数据类型为 `single`
  （ARM
  Cortex-A 处理器）
- 输入信号的数据类型为 `single` 或
  `double`（Intel 平台）

此外，请适当配置模型。在 Simulink 模型窗口的
**Modeling** 选项卡中，单击 **Model Settings**，然后在 **Code Generation** 下配置这些参数。

- 在 **Optimization** 窗格中：

  - 在
    **Leverage target hardware instruction set
    extensions** 参数中提供特定的指令集。
  - 选择 **Optimize reductions**
    参数。
  - 在 **Optimization levels** 下，将
    **Level** 设置为
    `Maximum`，并将
    **Priority** 设置为 `Maximize
    execution speed`。
- 在 **Interface** 窗格中的 **Software
  environment** 下，清除 **non-finite
  numbers**。

要使用此工作流从此模块生成 SIMD 代码，请参阅 Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for Intel Platforms、Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for Apple silicon 和 Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for ARM Cortex-A Processors。

对于受支持模块上的计算密集型运算，SIMD 内建函数可以显著提高 Intel 平台上生成的代码的性能。有关更多详细信息，请参阅 Optimize Code for Reduction Operations by Using SIMD (Simulink Coder)。

有关 DSP System Toolbox 中 SIMD 代码生成的更多信息，请参阅 SIMD Code Generation。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**注意**

对于具有硬件友好控制信号并支持向量输入和输出数据的 HDL 优化滤波器架构，请使用 FIR
Interpolator (DSP HDL Toolbox) 模块。DSP HDL Toolbox™ 模块在 Simulink 中仿真 HDL 算法的延迟。

**HDL 架构**

该模块具有 `HDLDataPath` 作为默认架构。此架构提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 模块属性**

| HDL 模块属性 | 描述 |
| --- | --- |
| **InputPipeline** | 要插入生成代码中的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入生成代码中的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过移动设计中的现有延迟来放置在输出处的寄存器数。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **FlattenFilter** | 从生成的 HDL 代码中删除 Filter 子系统的层次结构。默认值为 `auto`。请参阅 FlattenHierarchy (HDL Coder)。 |
| **DSPStyle** | 用于乘法器映射的综合属性。默认值为 `none`。另请参阅 DSPStyle (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的等效功能资源数。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |
| **StreamingFactor** | 被时间复用以转换为串行、标量数据路径的并行数据路径或向量数。默认值为 0，表示实现完全并行的数据路径。另请参阅 Streaming (HDL Coder)。 |
| **ConstMultiplierOptimization** | 规范有符号数字 (CSD) 或因式分解 CSD 优化。默认值为 `none`。另请参阅 ConstMultiplierOptimization (HDL Coder)。 |
| **MultiplerArchitecture** | 将乘法器架构选择为 `linear` 或 `shiftadd`。默认值为 `linear`。有关更多信息，请参阅 Product, Matrix Multiply (Simulink) 中的 HDL Code Generation 部分。 |
| **MultiplierInputPipeline** | 指定要在滤波器乘法器输入处添加的流水线级数。另请参阅 MultiplierInputPipeline (HDL Coder)。 |
| **MultiplierOutputPipeline** | 指定要在滤波器乘法器输出处添加的流水线级数。另请参阅 MultiplierOutputPipeline (HDL Coder)。 |
| **AdderOutputPipeline** | 要为加法运算插入生成代码中的输出流水线级数。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**数据类型支持**

该模块支持以下数据类型进行 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 枚举 | 复数信号 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | Scalar  Vector  Matrix | Yes | Half  Single  Double | Yes | Yes | Yes | Yes | Yes |

**模块参数配置**

这些模块参数配置与 HDL 代码生成不兼容。

| 模块参数 | 限制 |
| --- | --- |
| **速率选项** | 不支持参数值 `Enforce single-rate processing`。 |
| **输入处理** | 不支持参数值 `Columns as channels (frame based)`。 |
| **系数来源** | 不支持参数值 `Input port`。 |

**优化**

该模块参与以下 HDL 优化，以优化速度和面积。

**面积优化**

| 优化 | 描述 |
| --- | --- |
| Resource Sharing (HDL Coder) | *Resource sharing* 是一种面积优化，其中 HDL Coder 识别多个功能等效资源并将其替换为单个资源。 |
| Streaming (HDL Coder) | *Streaming* 是一种面积优化，其中 HDL Coder 将向量数据路径转换为标量数据路径（或转换为若干较小大小的向量数据路径）。 |

**速度优化**

| 优化 | 描述 |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *Distributed pipelining*，或寄存器重定时，是一种速度优化，它移动设计中的现有延迟以减少关键路径，同时保持功能行为。 |
| Clock-Rate Pipelining (HDL Coder) | *Clock-rate pipelining* 是 HDL Coder 中的一种优化框架，允许其他速度和面积优化在时钟速率下引入延迟。 |
| Adaptive Pipelining (HDL Coder) | *Adaptive pipelining* 优化创建带有寄存器的模块模式或组合，通过向设计中的模块插入流水线寄存器，可以提高可实现的时钟频率并减少 FPGA 板上的面积使用。 |
| Critical Path Estimation (HDL Coder) | 要快速识别设计中可能的关键路径，请使用 *Critical Path Estimation*。关键路径估计可加速查找关键路径的迭代过程。要了解在关键路径估计中表征的模块，请参阅 Characterized Blocks (HDL Coder)。 |

**限制和注意事项**

- 必须将 **初始条件** 设置为零。HDL 代码生成不支持非零初始状态。
- HDL 代码生成不支持帧输入和输出。
- 选择 **Dialog parameters** 时，以下定点选项不支持 HDL 代码生成：

  - **Coefficients**：`Slope and Bias
    scaling`

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2024b: 为 Apple 芯片处理器生成 SIMD 代码

在 R2024b 中，如果拥有 Embedded Coder，可以使用模型配置参数
**Leverage target hardware instruction set extensions** 为 Apple 芯片处理器上的 FIR Interpolation
模块生成 SIMD 代码。有关更多信息，请参阅 Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for Apple silicon。

### R2024a: 为 ARM Cortex-A 处理器生成 SIMD 代码

在 R2024a 中，如果拥有 Embedded Coder，可以使用模型配置参数
**Leverage target hardware instruction set extensions** 为 ARM
Cortex-A 处理器上的 FIR Interpolation 模块生成 SIMD 代码。

### R2023b: 为复数信号生成 SIMD 代码

在 R2023b 中，如果拥有 Embedded Coder，可以使用模型配置参数
**Leverage target hardware instruction set extensions** 在输入信号为复值时，为 FIR Interpolation 模块生成 SIMD 代码。

### R2023a: 在所有 Intel 平台上为 FIR Interpolation 模块生成 SIMD 代码

在 R2023a 中，如果拥有 Embedded Coder 许可证，可以使用模型配置参数
**Leverage target hardware instruction set extensions** 在所有 Intel 平台上为 FIR
Interpolation 模块生成 SIMD 代码。以前，必须使用代码替换库来生成 SIMD 代码。有关更多详细信息，请参阅 Code Generation。

## 描述

执行多相 FIR 插值

FIR Interpolation 模块沿第一个维度使用整数上采样因子 *L* 执行高效多相插值。

从概念上讲，FIR 插值器（如示意图所示）由一个上采样器后接一个 FIR 抗成像滤波器组成，该滤波器通常是理想带限插值滤波器的近似。要设计 FIR 抗成像滤波器，请使用
`designMultirateFIR` 函数。上采样器通过在样本之间插入 *L*–1
个零，将输入的每个通道上采样到更高采样率。随后的 FIR 滤波器对已上采样数据的每个通道进行滤波。得到的离散时间信号的采样率是原始采样率的 *L*
倍。

FIR 插值器包含一个上采样器，后接一个抗成像 FIR 滤波器。

但是，实际模块算法实现直接型 FIR 多相结构，这是图中所示组合系统的高效等效形式。有关更多详细信息，请参阅 Algorithms。

当将 **速率选项** 参数设置为 `Enforce single-rate processing` 时，可以在触发子系统内使用 FIR Interpolation 模块。

在特定条件下，此模块还支持 SIMD 代码生成。有关更多详细信息，请参阅 Code Generation。
