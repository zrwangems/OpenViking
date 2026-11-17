---
type: simulink-block
title: 'Sum'
family: 'hdlcoder'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Commonly Used Blocks'
documentation_page: 'sum'
documentation_source_path: '../simulink/slref/sum.html'
language: zh-CN
chinese_source: worker-translation
---

# Sum

## 端口

### 输入

除非选中 **Require all inputs to have the same data type**，否则输入可以具有不同的数据类型。

### **Port\_1** — 第一个输入操作数信号 标量 | 向量 | 矩阵

加法或减法运算的输入信号。如果只有一个输入信号，则对所有维度或指定维度上的元素执行加法或减法。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_n** — 第 *n* 个输入操作数信号 标量 | 向量 | 矩阵

运算的第 *n* 个输入信号。输入的数量与 **List of signs** 参数中符号的数量一致。模块按列出的顺序对输入执行运算。您也可以使用等于输入端口数量的数值作为 **List of signs** 参数。模块将创建输入端口并对所有输入执行加法。例如，如果将 **List of signs** 参数赋值为 `5`，模块将创建 `5` 个输入端口并将它们相加产生输出。

所有非标量输入必须具有相同的维度。标量输入将扩展为与其他输入具有相同的维度。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

由加法和/或减法运算产生的输出信号。输出信号与输入信号具有相同的维度。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### 主要

### **Icon shape** — 模块图标形状 `rectangular` | `round`

将模块的图标形状指定为矩形或圆形。

默认值取决于模块配置。

- `round` 默认值 — Sum 模块
- `rectangular` 默认值 — Add、Subtract 和 Sum of Element 模块

对于矩形模块，第一个输入端口是顶部端口。对于圆形 Sum 模块，第一个输入端口是最接近 12 点钟位置并沿逆时针方向绕模块的端口。类似地，其他输入端口按逆时针顺序围绕模块排列。

#### 编程使用

|  |
| --- |
| **模块参数**：`IconShape` |
| **类型**：character vector |
| **值**：`'rectangular'` | `'round'` |

### **List of signs** — 对输入执行的运算 `+` | `-` | `|` | integer

输入对输入执行的加法和减法运算。每个运算创建一个输入端口。间隔符（`|`）在模块图标上的输入端口之间创建额外空间。加法是默认运算。如果只想对输入求和，请输入输入端口数量。运算按列出的顺序执行。

默认值取决于模块配置。

- `|++` 默认值 — Sum 模块
- `++` 默认值 — Add 模块
- `+-` 默认值 — Subtract 模块
- `+` 默认值 — Sum of Element 模块

当只输入一个符号时，模块将启用 **Apply over** 参数。对于向量输入，`+` 或 `-` 对所有维度或指定维度上的元素进行加法或减法。

#### 提示

您可以通过在 **List of signs** 参数中的符号之间插入间隔符（`|`）来调整模块上输入端口的位置。例如，“`++|--`”在第二个和第三个输入端口之间创建额外空间。

#### 编程使用

|  |
| --- |
| **模块参数**：`Inputs` |
| **类型**：character vector |
| **值**：`'+'` | `'-'` | `|` | integer |

### **Apply over** — 如何沿指定维度应用函数 `All dimensions`（默认）| `Specified dimension`

指定如何沿指定维度应用函数。

- `All dimensions` — 对所有维度的所有输入值应用函数。

  例如，在此模型中，**List of signs** 设置为 `+`，**Apply over** 设置为 `All dimensions`。模块返回所有维度的所有输入值之和。

  2D 矩阵，Constant 模块值为 [1 2 3 4 5 6] 作为 Sum 模块的输入，配置为所有维度

  当您选择配置参数 **Use algorithms optimized for row-major array layout** 时，软件启用行主序算法进行仿真。要生成行主序代码，请将配置参数 **Array layout (Simulink Coder)** 设置为 `Row-major`，并选择 **Use algorithms optimized for row-major array layout**。列主序和行主序算法仅在求和顺序上有所不同。在某些情况下，由于对同一数据集的不同运算顺序，您可能会在列主序和行主序算法的输出中遇到轻微的数值差异。
- `Specified dimensions` — 对指定维度的所有输入值应用函数。

#### 依赖关系

要启用此参数，请在 **List of signs** 参数中仅输入一个符号。

#### 编程使用

|  |
| --- |
| **模块参数**：`CollapseMode` |
| **类型**：character vector |
| **值**：`'All dimensions'` | `'Specified dimension'` |
| **默认值**：`'All dimensions'` |

### **Dimension** — 应用求和的维度 `1`（默认）| 正整数

将应用求和的维度指定为正整数。

模块遵循与 MATLAB® `sum` 函数相同的求和规则。有关详细信息，请参阅算法。

例如，在此模型中，**List of signs** 设置为 `+`，**Apply over** 设置为 `Specified dimension`，**Dimension** 设置为 `2`。模块返回每一行的输入值之和。

2D 矩阵，Constant 模块值为 [1 2 3;4 5 6] 作为 Sum 模块的输入，配置为维度 2

如果指定的维度大于输入的维度，将出现错误消息。

#### 依赖关系

要启用此参数，请将 **Apply over** 设置为 `Specified dimension`。

#### 编程使用

|  |
| --- |
| **模块参数**：`CollapseDim` |
| **类型**：character vector |
| **Value**: integer |
| **默认值**：`'1'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

#### 依赖关系

仅当您将其设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅不建议使用采样时间的模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **值**：| `"-1"`（默认）| 带引号的标量或向量 |

### 信号属性

**Data Type Assistant** 帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型。

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的下限值。

软件使用最小值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `OutMin` |
| **值**：| `'[]'`（默认）| 带引号的标量 |

### **Output maximum** — 用于范围检查的最大输出值 `[]`（默认）| 标量

软件检查的输出范围的上限值。

软件使用最大值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **值**：| `'[]'`（默认）| 带引号的标量 |

### **Output data type** — 指定输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Keep MSB` | `Inherit: Keep LSB` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `Inherit: Same as accumulator` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

选择输出的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType` 对象）。

当您选择继承选项时，模块的行为如下：

- `Inherit: Inherit via internal rule` — 软件选择一种数据类型以平衡数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。

  **注意**

  累加器内部规则倾向于更高的数值精度，可能以生成代码效率较低为代价。要使输出获得相同的精度，请将输出数据类型设置为 `Inherit: Inherit same as accumulator`。

  **注意**

  当输入是小于单精度的浮点数据类型时，`Inherit: Inherit via internal rule` 输出数据类型取决于 Inherit floating-point output type smaller than single precision 配置参数的设置。当编码数据类型所需的位数小于编码单精度数据类型所需的 32 位时，数据类型小于单精度。例如，`half` 和 `int16` 小于单精度。
- `Inherit: Keep MSB` – 软件选择一种保持运算完整范围的数据类型，然后将输出的精度降低到适合嵌入式目标硬件的大小。

  **提示**

  要获得更高效的生成代码，请将 **Accumulator data type** 设置为 `Inherit: Inherit via internal rule`，并清除 **Saturate on integer overflow**。

  此规则从不产生溢出。
- `Inherit: Keep LSB`– 软件选择一种保持运算精度的数据类型，但如果完整类型不适合嵌入式目标硬件，则减小范围。

  **提示**

  要获得更高效的生成代码，请将 **Accumulator data type** 设置为 `Inherit: Inherit via internal rule`，并清除 **Saturate on integer overflow**。

  此规则可能产生溢出。

  如果更改嵌入式目标设置，这些内部规则选择的数据类型可能会改变。软件并不总是能够同时优化代码效率和数值精度。如果这些规则不满足您对数值精度或性能的特定需求，请使用以下选项之一：

  - 显式指定输出数据类型。
  - 使用 `Inherit: Same as first input` 的简单选择。
  - 显式指定默认数据类型（如 `fixdt(1,32,16)`），然后使用 Fixed-Point Tool 为您的模型建议数据类型。有关详细信息，请参阅 `fxptdlg` (Fixed-Point Designer)。
  - 要指定自己的继承规则，请使用 `Inherit: Inherit via back propagation`，然后使用 Data Type Propagation 模块。有关如何使用此模块的示例可在 Signal Attributes 库的 Data Type Propagation Examples 模块中找到。
- `Inherit: Inherit via back propagation` — 使用驱动模块的数据类型。
- `Inherit: Same as first input` — 使用第一个输入信号的数据类型。
- `Inherit: Inherit same as accumulator`— 使用累加器的数据类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule` | `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Same as accumulator'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'`|`'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Accumulator data type** — 累加器的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as first input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

选择累加器的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，Simulink® 选择一种数据类型以平衡数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。

#### 编程使用

|  |
| --- |
| **模块参数**：`AccumDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'`, `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Require all inputs to have the same data type** — 要求所有输入具有相同的数据类型 `off`（默认）| `on`

指定输入信号是否必须全部具有相同的数据类型。如果启用此参数，则当输入信号类型不同时，仿真期间将出现错误。

#### 编程使用

|  |
| --- |
| **模块参数**：`InputSameDT` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此项可锁定此模块的数据类型设置，防止被 Fixed-Point Tool 和 Fixed-Point Advisor 更改。有关详细信息，请参阅锁定输出数据类型设置 (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LockScale` |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式（Fixed-Point Designer）。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入方式，请在掩码字段中输入使用 MATLAB 舍入函数的表达式。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RndMeth` |
| **值**：| `'Floor'`（默认）| `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出时是饱和还是回绕。

- `on` — 溢出饱和到数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到数据类型可以表示的适当值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出饱和于 127。类似地，模块输出饱和于最小输出值 -128。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 -126。

#### 提示

- 当您的模型可能存在溢出并且您希望在生成的代码中显式添加饱和保护时，请考虑选中此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅信号范围错误疑难解答。
- 选中此参数时，饱和适用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **值**：| `'off'`（默认）| `'on'` |

## 所属库

Simulink / Commonly Used Blocks Simulink / Math Operations HDL Coder / Commonly Used Blocks HDL Coder / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**Sum、Add 和 Subtract 模块的 HDL 架构**

默认的 `Linear` 架构为 N 个输入生成 N 个运算（加法器）的链。

**Sum of Elements 模块的 HDL 架构**

对于 Sum of Elements 模块，HDL Coder 支持具有单个多元素向量输入的 Sum of Elements 模块的 `Tree` 架构。

此模块具有多周期实现，会在生成的代码中引入额外延迟。要查看增加的延迟，请查看生成的模型或验证模型。请参阅生成的模型和验证模型（HDL Coder）。

| Architecture | Additional cycles of latency | Description |
| --- | --- | --- |
| `Linear` | 0 | 生成加法器的线性链以计算和的乘积。对于具有不同位宽的多个输入，`Linear` 架构通过在多级中实现加法器并在级之间使用流水线来优化资源利用率。每一级的输出根据该级输入的位宽计算。 |
| `Tree` | 0 | 生成加法器的树结构以计算和的乘积。 |

**HDL 模块属性**

**注意**

要使用 HDL Block Properties 对话框的 **Native Floating Point** 选项卡中的 **LatencyStrategy** 设置，请将 HDL Architecture 指定为 `Linear` 或 `Tree`。

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline（HDL Coder）。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline（HDL Coder）。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline（HDL Coder）。 |

**注意**

Sum of Elements 模块不支持在 Native Floating Point 模式下使用 double 数据类型进行 HDL 代码生成。

| Native Floating Point | |
| --- | --- |
| **LatencyStrategy** | 指定是否将设计中的模块映射为浮点运算符的 `inherit`、`Max`、`Min`、`Zero` 或 `Custom`。默认值为 `inherit`。另请参阅 LatencyStrategy（HDL Coder）。 |
| **NFPCustomLatency** | 要指定值，请将 **LatencyStrategy** 设置为 `Custom`。HDL Coder 添加等于您为 **NFPCustomLatency** 设置指定的值的延迟。另请参阅 NFPCustomLatency（HDL Coder）。 |

**复数数据支持**

默认的 `Linear` 实现支持复数数据。

`Tree` 实现支持复数数据，**List of signs** 模块参数使用 `+`。在原生浮点支持下，`Tree` 实现支持复数数据，**List of signs** 同时使用 `+` 和 `-`。

**限制和注意事项**

要为具有混合标量和向量输入的多输入 Sum 模块生成 HDL 代码，您必须在 Sum 模块的前两个输入之一处指定向量输入。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2024a：使用 **Apply over** 参数指定如何应用函数，该参数由 **Sum over** 重命名而来

当您为 **List of signs** 仅输入一个符号时，模块会启用 **Apply over** 参数。对于向量输入，`+` 或 `-` 在所有维度上或在指定维度上对元素进行加法或减法运算。

为了更好地反映支持的行为，**Sum over** 参数现在称为 **Apply over**。

## 描述

对输入进行加法或减法运算

Sum 模块对其输入执行加法或减法运算。Add、Subtract、Sum of Elements 和 Sum 模块是同一模块的替代配置。此模块可以对标量、向量或矩阵输入进行加法或减法运算。它还可以折叠信号的元素并执行求和。

您使用 **List of signs** 参数指定模块的运算，使用加号（`+`）、减号（`-`）和间隔符（`|`）。

- `+` 和 `-` 字符的数量等于输入的数量。例如，`+-+` 需要三个输入。模块从第一个（顶部）输入中减去第二个（中间）输入，然后加上第三个（底部）输入。
- 间隔符在模块图标上的端口之间创建额外空间。
- 如果仅执行加法，您可以使用等于输入数量的数值。
- 如果只有一个输入端口，一个 `+` 或 `-` 在所有维度上或在指定维度上对元素进行加法或减法运算。

Sum 模块首先将输入数据类型转换为其累加器数据类型，然后执行指定的运算。模块使用指定的舍入和溢出模式将结果转换为其输出数据类型。

### 模块输出的计算

Sum 模块的输出计算取决于模块输入的数量和输入端口的符号。

| 加法模块输入端口数量 | 输入端口符号 | 模块输出计算公式 | 输出公式变量 |
| --- | --- | --- | --- |
| 一个输入端口 | 输入端口符号为 + | y = e[0] + e[1] + e[2] ... + e[m] | `e[i]` 是输入 u 的第 *i* 个元素 |
| 输入端口符号为 – | y = 0.0 – e[0] – e[1] – e[2] ... – e[m] |
| 两个或更多输入端口 | 所有输入端口符号为 – | y = 0.0 – u[0] – u[1] – u[2] ... – u[n] | `u[i]` 是第 *i* 个输入端口的输入 |
| 第 *k* 个输入端口是第一个符号为 + 的端口 | y = u[k] – u[0] – u[1] – u[2] – u[k–1] (+/–) u[k+1] ... (+/–) u[n] |
