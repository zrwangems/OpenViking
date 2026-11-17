---
type: simulink-block
title: 'Sqrt'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'sqrt'
documentation_source_path: 'slref/sqrt.html'
language: zh-CN
chinese_source: worker-translation
---

# Sqrt

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入到模块的信号，用于计算平方根、带符号平方根或平方根的倒数。`sqrt` 函数接受实数或复数输入，但复数定点信号除外。`signedSqrt` 和 `rSqrt` 不接受复数输入。输入信号必须是浮点数。

此表总结了 `sqrt`、`rSqrt` 和 `signedSqrt` 函数对浮点、整数和定点数据类型的复数类型和负值的支持情况。

| 函数 | 数据类型 | 复数 | | 负值 |
| --- | --- | --- | --- | --- |
| 输入 | 输出 |
| `sqrt` | 浮点 | 是 | 是 | 是 |
|  | 整数和定点 | 否 | 否 | 否 |
| `rSqrt` | 浮点 | 否 | 否 | 是 |
|  | 整数和定点 | 否 | 否 | 否 |
| `signedSqrt` | 浮点 | 否 | 是 | 是 |
|  | 整数和定点 | 否 | 否 | 否 |

如果输入为负，对于除 `signedSqrt` 以外的所有函数，将 **Output signal** 设置为复数。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

输出信号，为输入信号的平方根、带符号平方根或平方根的倒数。当输入为整数或定点类型时，输出必须为浮点。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### 主要

### **Function** — 模块执行的函数 `sqrt` | `signedSqrt` | `rSqrt`

指定模块计算的数学函数。模块图标会更改以匹配您选择的函数。

| 函数 | 模块图标 |
| --- | --- |
| `sqrt` | Sqrt block |
| `signedSqrt` | Signed Sqrt block |
| `rSqrt` | Reciprocal Sqrt block |

默认值取决于模块配置。

- `sqrt` 默认值 — Sqrt 和 Square Root 模块
- `signedSqrt` 默认值 — Signed Sqrt 和 Signed Square Root 模块
- `rSqrt` 默认值 — Reciprocal Sqrt 和 Reciprocal Square Root 模块

#### 编程使用

|  |
| --- |
| **模块参数**：`Operator` |
| **类型**：character vector |
| **值**：`'sqrt'` | `'signedSqrt'` | `'rSqrt'` |

### **Output signal type** — 输出信号类型 `auto` (默认) | `real` | `complex`

指定模块的输出信号类型。

| 函数 | 输入信号类型 | 输出信号类型 | | |
| --- | --- | --- | --- | --- |
| Auto | Real | Complex |
| `sqrt` | `real` | `real`（非负输入）  `NaN`（负输入） | `real`（非负输入）  `NaN`（负输入） | `complex` |
| `complex` | `complex` | `error` | `complex` |
| `signedSqrt` | `real` | `real` | `real` | `complex` |
| `complex` | `error` | `error` | `error` |
| `rSqrt` | `real` | `real` | `real` | `error` |
| `complex` | `error` | `error` | `error` |

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputSignalType` |
| **类型**：character vector |
| **值**：`'auto'` | `'real'` | `'complex'` |
| **默认值**：`'auto'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1` (默认) | 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **值**：| `"-1"` (默认) | 带引号的标量或向量 |

### 算法

### **Method** — 计算平方根倒数的方法 `Exact` (默认) | `Newton-Raphson`

指定计算平方根倒数的方法。

| 方法 | 支持的数据类型 | 何时使用此方法 |
| --- | --- | --- |
| `Exact` | 浮点 | 您不需要近似值。  输入或输出必须为浮点。 |
| `Newton-Raphson` | 浮点、定点和内置整数类型 | 您需要快速、近似的计算。 |

`Exact` 方法提供与 MATLAB 计算一致的结果。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `rSqrt`。

当 **Function** 设置为 `sqrt` 或 `signedSqrt` 时，此参数设置为 `Exact`。

#### 编程使用

|  |
| --- |
| **模块参数**：`AlgorithmType` |
| **类型**：character vector |
| **值**：`'Exact'` | `'Newton-Raphson'` |
| **默认值**：`'Exact'` |

### **Number of iterations** — 用于 Newton Raphson 算法的迭代次数 `3` (默认) | 整数

指定执行 Newton-Raphson 算法的迭代次数。此参数在 `rSqrt` 函数和 **Method** 的 `Newton-Raphson` 值下有效。

如果输入 `0`，模块输出为 Newton-Raphson 算法的初始猜测值。

#### 编程使用

|  |
| --- |
| **模块参数**：`Iterations` |
| **类型**：character vector |
| **值**：integer |
| **默认值**：`'3'` |

### 数据类型

**Data Type Assistant** 帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

### **Intermediate results data type** — 中间结果的数据类型 `Inherit: Inherit via internal rule` (默认) | `Inherit: Inherit from input` | `Inherit: Inherit from output` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

当您将 **Function** 设置为 `sqrt` 或 `rSqrt` 时，指定中间结果的数据类型。

该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType` 对象。

为避免溢出，中间数据类型必须大于或等于能够包含输出数据类型平方的数据类型。

对于平方根函数 `sqrt`，显式设置中间数据类型时请遵循以下准则：

| 输入和输出数据类型 | 中间数据类型 |
| --- | --- |
| 输入或输出为 double。 | 使用 double。 |
| 输入或输出为 single，且任何非 single 数据类型*不是* double。 | 使用 single 或 double。 |
| 输入和输出为定点。 | 使用定点。 |

对于平方根倒数函数 `rSqrt`，显式设置中间数据类型时请遵循以下准则：

| 输入和输出数据类型 | 中间数据类型 |
| --- | --- |
| 输入为 double 且输出不是 single。 | 使用 double。 |
| 输入不是 single 且输出为 double。 | 使用 double。 |
| 输入和输出为定点。 | 使用定点。 |

**Caution**

在以下情况下，不要将 **Intermediate results data type** 设置为 `Inherit: Inherit from output`：

- 您选择 `Newton-Raphson` 来计算平方根的倒数。
- 输入数据类型为浮点。
- 输出数据类型为定点。

在这些条件下，选择 `Inherit: Inherit from output` 会产生次优性能并产生错误。

为避免此错误，请将输入信号从浮点数据类型转换为定点数据类型。例如，在 Sqrt 模块前面插入一个 Data Type Conversion 模块来执行转换。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `sqrt` 或 `rSqrt`。

#### 编程使用

|  |
| --- |
| **模块参数**：`IntermediateResultsDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule'` | `'Inherit: Inherit from input'` | `'Inherit: Inherit from output'` | `'double'` | `'single'`, `'int8'`, `'uint8'`, `int16`, `'uint16'`, `'int32'`, `'uint32'`, `'int64'`, `'uint64'`, `fixdt(1,16,0)`, `fixdt(1,16,2^0,0)`. `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Output** — 输出数据类型 `Inherit: Same as first input` (默认) | `Inherit: Inherit via internal rule` | `Inherit: Inherit via back propagation` | `double` | `single` | `half` | `int8` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,2^0,0)` | `<data type expression>` | ...

指定输出数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType` 对象。

#### 依赖关系

当输入为小于单精度的浮点数据类型时，`Inherit: Inherit via internal rule` 输出数据类型取决于 Inherit floating-point output type smaller than single precision 配置参数的设置。当编码数据类型所需的位数小于编码单精度数据类型所需的 32 位时，数据类型小于单精度。例如，`half` 和 `int16` 小于单精度。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `fixdt(1,16,2^0,0)` | `'<data type expression>'` |
| **默认值**：`'Inherit: Same as first input'` |

### **Minimum** — 用于范围检查的最小输出值 `[]` (默认) | 标量

指定软件检查的输出范围的下限值，为有限、实数、double、标量值。

如果指定总线对象作为此模块的数据类型，请不要在模块上设置总线数据的最小值。软件会忽略此设置。而应设置指定为数据类型的总线对象的总线元素的最小值。有关详细信息，请参阅 `Simulink.BusElement`。

软件使用最小值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）用于某些模块。
- 仿真范围检查（请参阅 Specify Signal Ranges 和 Enable Simulation Range Checking）。
- 定点数据类型的自动缩放。
- 优化您从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[]'` |

### **Maximum** — 用于范围检查的最大输出值 `[]` (默认) | 标量

指定软件检查的输出范围的上限值，为有限、实数、double、标量值。

如果指定总线对象作为此模块的数据类型，请不要在模块上设置总线数据的最大值。软件会忽略此设置。而应设置指定为数据类型的总线对象的总线元素的最大值。有关详细信息，请参阅 `Simulink.BusElement`。

软件使用最大值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）用于某些模块。
- 仿真范围检查（请参阅 Specify Signal Ranges 和 Enable Simulation Range Checking）。
- 定点数据类型的自动缩放。
- 优化您从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[]'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor` (默认) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：character vector |
| **值**：`'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值**：`'Floor'` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择以锁定此模块的输出数据类型设置，防止被 Fixed-Point Tool 和 Fixed-Point Advisor 更改。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Saturate on integer overflow** — 溢出操作的方法 `on` (默认) | `off`

指定溢出是饱和还是环绕。

- `on` — 溢出饱和到数据类型可以表示的最小值或最大值。
- `off` — 溢出环绕到数据类型可以表示的适当值。

例如，有符号 8 位整数 `int8` 可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出在 127 处饱和。类似地，模块输出在最小输出值 -128 处饱和。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 -126。

#### 提示

- 当您的模型可能存在溢出并且您希望在生成的代码中显式提供饱和保护时，请考虑选中此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors。
- 选中此参数时，饱和应用于模块上的每个内部操作，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **值**：| `'on'` (默认) | `'off'` |

## 所属库

Simulink / Math Operations HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

| 函数 | 架构 | 描述 |
| --- | --- | --- |
| `sqrt`  `signedSqrt`  `rSqrt` | `SqrtFunction`（默认） | 使用流水线移位加法算法或基于乘法的算法计算平方根。`sqrtfunction` 架构支持定点类型和浮点类型的代码生成。使用浮点类型时，选择 **Use Floating Point** 配置参数。您可以指定 **LatencyStrategy** 和 **CustomLatency** HDL 属性，以便在硬件平台上定位设计时从一系列频率值中进行选择。 将 **UseMultiplier** HDL 模块属性与 **LatencyStrategy** 和 **CustomLatency** 属性结合使用，以指定是使用流水线移位加法还是乘法算法来计算平方根。通过将 **UseMultiplier** 设置为 `off` 并将 **LatencyStrategy** 设置为 `inherit`，可提高设计频率并减少资源利用率。 |
| `sqrt` | `SqrtNewton` | 使用迭代牛顿法优化面积。 |
| `sqrt` | `SqrtNewtonSingleRate` | 使用单速率流水线牛顿法。选择此选项可优化速度，或者如果您需要单速率实现。 |
| `rSqrt` | `RecipSqrtNewton` | 使用迭代牛顿法优化面积。 要指定此架构，请将 **Method** 设置为 `Newton-Raphson`。 |
| `rSqrt` | `RecipSqrtNewtonSingleRate` | 使用单速率流水线牛顿法。选择此选项可优化速度，或者如果您需要单速率实现。 要指定此架构，请将 **Method** 设置为 `Newton-Raphson`。 |

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **Iterations** | `SqrtNewton` 或 `SqrtNewtonSingleRate` 实现的迭代次数。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **UseMultiplier** | 选择 `SqrtFunction` 实现的算法。默认情况下，此属性设置为 `off`，模块使用移位加法算法计算平方根。当该属性设置为 `on` 时，使用乘法器计算平方根。 通过将 **UseMultiplier** 设置为 `off` 并将 **LatencyStrategy** 设置为 `inherit`，可提高设计频率并减少资源利用率。 |
| **LatencyStrategy** | 指定是否将设计中的模块映射为定点类型和浮点类型的 `MAX`、`MIN`、`CUSTOM` 或 `ZERO` 延迟。默认值为 `MAX`。浮点类型的模块设置会覆盖模型级设置。对于定点类型，模块级设置决定延迟策略。另请参阅 LatencyStrategy (HDL Coder)。 通过将 **UseMultiplier** 设置为 `off` 并将 **LatencyStrategy** 设置为 `inherit`，可提高设计频率并减少资源利用率。 您可以通过将 **LatencyStrategy** 设置为 `Custom(PerIterations)` 来控制迭代算法的流水线级数。有关更多信息，请参阅 Sqrt (HDL Coder)。 |
| **CustomLatency** | 当 **LatencyStrategy** 设置为 `CUSTOM` 且使用定点类型时，使用此属性为定点类型指定介于 `ZERO` 和 `MAX` 之间的自定义延迟值。对于浮点类型，此值成为运算符的自定义延迟。另请参阅 NFPCustomLatency (HDL Coder)。 |
| **IterationsPerPipeline** | 当您将 **LatencyStrategy** 设置为 `Custom(PerIterations)` 时，使用此设置指定每个流水线级的迭代次数。要启用此属性，请将 HDL 架构设置为 `SqrtFunction`。 有关更多信息，请参阅 Sqrt (HDL Coder)。 |

| 原生浮点 | |
| --- | --- |
| **HandleDenormals** | 指定是否希望 HDL Coder 插入附加逻辑来处理设计中的非规格化数。非规格化数是幅值小于最小浮点数的数，该最小浮点数可以在尾数中没有前导零的情况下表示。默认值为 `inherit`。另请参阅 HandleDenormals (HDL Coder)。 |

**数据类型支持**

该模块支持以下数据类型进行 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 复信号 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | 标量  向量  矩阵（最多二维） | 是 | Single  Double | 是 | 是 | 否 | 否 |

**延迟详细信息**

该模块具有多周期实现，会在生成代码中引入附加延迟。要查看增加的延迟，请查看生成的模型或验证模型。请参阅 Generated Model and Validation Model (HDL Coder)。

**浮点延迟**

| 架构 | 浮点类型 | 延迟策略 | 延迟（周期） | 自定义延迟支持 |
| --- | --- | --- | --- | --- |
| `SqrtFunction` | Single | Min | 16 | 是 |
| Max | 28 |
| Double | Min | 33 |
| Max | 58 |

**定点延迟**

| 架构 | 最大延迟（周期） | 描述 | 延迟策略支持 | 自定义延迟支持 |
| --- | --- | --- | --- | --- |
| `SqrtFunction` | 要计算定点数据类型的延迟，请参阅 Sqrt (HDL Coder) 中的 *Algorithm*。 | 最大延迟由定点数据的输出字长以及输入和输出小数长度决定。 | 是 | 是 |
| `SqrtNewton` | **Iterations** + 3 | **Iterations** HDL 模块属性的默认值为 3。 **Iterations** 的建议值为 2 到 10。如果 **Iterations** 超出建议范围，HDL Coder 会生成一条消息。 | 否 | 否 |
| `SqrtNewtonSingleRate` | (**Iterations**\* 4) + 6 |
| `RecipSqrtNewton` | **Number of iterations** + 2 | **Number of iterations** 模块参数的默认值为 3。 **Number of iterations** 的建议值为 2 到 10。如果 **Number of iterations** 超出建议范围，HDL Coder 会生成一条消息。 |
| `RecipSqrtNewtonSingleRate` | (**Number of iterations**\* 4) + 5 |

**模块参数配置**

这些模块参数配置与 HDL 代码生成不兼容。

| 模块参数 | 限制和注意事项 |
| --- | --- |
| **Output Signal Type** | 不支持参数值 `Complex`。 |
| **Method** | 当您将 **Function** 参数设置为 `rSqrt` 时，对浮点数据类型使用 `Exact`，对定点数据类型使用 `Newton Raphson`。 |
| **Intermediate results data type** | 不支持 `Inherit: Inherit via internal rule` 以外的参数值 |
| **Output** | 选择与输入相同的输出端口数据类型。 |
| **Integer rounding mode** | 对于定点类型，不支持参数值 `Convergent`、`Round`。 |

**优化**

您可以使用这些 HDL Coder 优化来优化速度、面积和 I/O。

**面积优化**

| 优化 | 描述 |
| --- | --- |
| Resource Sharing (HDL Coder) | *资源共享*是一种面积优化，HDL Coder 在其中识别多个功能等效的资源并将其替换为单个资源。 |
| Streaming (HDL Coder) | *流式处理*是一种面积优化，HDL Coder 在其中将向量数据路径转换为标量数据路径（或转换为若干较小尺寸的向量数据路径）。 |

**速度优化**

| 优化 | 描述 |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *分布式流水线*或寄存器重定时是一种速度优化，它在保持功能行为的同时移动设计中的现有延迟以减少关键路径。 对于 Sqrt 模块，HDL Coder 将流水线寄存器分布在模块周围而不是模块内部。 |
| Clock-Rate Pipelining (HDL Coder) | *时钟速率流水线*是 HDL Coder 中的一种优化框架，允许其他速度和面积优化在时钟速率下引入延迟。 |
| Critical Path Estimation (HDL Coder) | 要快速识别设计中可能的关键路径，请使用*关键路径估计*。关键路径估计可加速查找关键路径的迭代过程。要了解在关键路径估计中表征的模块，请参阅 Characterized Blocks (HDL Coder)。 |

**I/O 优化**

| 优化 | 描述 |
| --- | --- |
| Frame to Sample Conversion (HDL Coder) | 要优化设计所需的 I/O，请使用帧到样本转换。此优化将基于帧的向量或矩阵输入转换为较小尺寸的样本或像素，以便 HDL 代码生成能够面向基于流的硬件，并减少处理大型输入和输出信号所需的 FPGA I/O。 |

**HDL 算法**

HDL Coder 在 `ReciprocalRsqrtBasedNewton` 和 `ReciprocalRsqrtBasedNewtonSingleRate` 架构中使用牛顿-拉夫逊迭代法实现倒数平方根运算，其公式为：

xi+1=xi−f(xi)f'(xi)=xi(1.5−0.5axi2)

f(x)=1x2−1

**限制**

基于牛顿-拉夫逊的实现与原生浮点模式下的 HDL 代码生成不兼容。要在原生浮点模式下生成 HDL 代码，请在 HDL 模块属性中选择 `SqrtFunction` 架构。

**HDL 建模指南**

为 Square Root 模块使用 SqrtFunction 架构（HDL Coder）

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2010a 中引入**

## 描述

计算平方根、带符号平方根或平方根的倒数

Sqrt 模块计算输入信号的平方根、带符号平方根或平方根的倒数。从 **Function** 参数列表中选择以下函数之一。

| 函数 | 描述 | 数学表达式 | MATLAB® 等效项 |
| --- | --- | --- | --- |
| `sqrt` | 输入的平方根 | `u0.5` | `sqrt` |
| `signedSqrt` | 输入的绝对值的平方根乘以输入的符号 | `sign(u)*|u|0.5` | — |
| `rSqrt` | 输入的平方根的倒数 | `u-0.5` | — |

模块图标会更改以匹配该函数。
