---
type: simulink-block
title: 'Math Function'
family: 'libsb2sl'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'ALG / AlgExpression'
documentation_page: 'mathfunction'
documentation_source_path: '../simulink/slref/mathfunction.html'
language: zh-CN
chinese_source: worker-translation
---

# Math Function

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。支持的模式接受实数和复数输入，但 `reciprocal` 除外，它不接受复数定点输入。请参阅描述。

#### 依赖

此模块的数据类型支持取决于您选择的 **Function** 以及输入的大小。有关详细信息，请参阅数据类型支持。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_2** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。支持的模式接受实数和复数输入，但 `reciprocal` 除外，它不接受复数定点输入。

#### 依赖

要启用此端口，请将 **Function** 设置为 `hypot`、`rem` 或 `mod`。

此模块的数据类型支持取决于您选择的 **Function** 以及输入的大小。有关详细信息，请参阅数据类型支持。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 函数对一个或多个输入进行运算的结果 标量 | 向量 | 矩阵

输出信号，指定为标量、向量或矩阵。模块输出的维度取决于您选择的 **Function** 以及输入的大小。模块输出为实数或复数，取决于您为 **Output signal type** 选择的值。请参阅描述。

#### 使用 Newton-Raphson 方法的 `reciprocal`

使用 Newton-Raphson 方法的 `reciprocal` 输出数据类型取决于输入数据类型：

| 输入数据类型 | 输出数据类型 |
| --- | --- |
| single | single |
| double | double |
| 内置整数 | 内置整数 |
| 内置定点 | 内置定点 |
| `fi` (*value*, 0, *word\_length*, *fraction\_length*) | `fi` (*value*, 0, *word\_length*, *word\_length*–*fraction\_length*–1) |
| `fi` (*value*, 1, *word\_length*, *fraction\_length*) | `fi` (*value*, 1, *word\_length*, *word\_length*–*fraction\_length*–2) |

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### 主要

### **Function** — 数学函数 `exp`（默认）| `log` | `2^u` | `10^u` | `log10` | `magnitude^2` | `square` | `pow` | `conj` | `reciprocal` | `hypot` | `rem` | `mod` | `transpose` | `hermitian`

指定数学函数。有关此参数选项的详细信息，请参阅描述。

#### 依赖

将 **Function** 设置为 `pow` 会启用 **Signed power** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `Operator` |
| **类型：** 字符向量 |
| **值：** `'exp' | 'log' | '2^u' | '10^u' | 'log10' | 'magnitude^2' | 'square' | 'pow' | 'conj' | 'reciprocal' | 'hypot' | 'rem' | 'mod' | 'transpose' | 'hermitian'` |
| **默认值：** `'exp'` |

### **Algorithm method** — `reciprocal` 函数的算法方法 `Exact`（默认）| `Newton-Raphson`

`reciprocal` 函数的算法方法，指定为 `Exact` 或 `Newton-Raphson`。要使用 Newton-Raphson 近似方法计算倒数，请选择 `Newton-Raphson`。否则，请选择 `Exact`。

#### 依赖

将 **Function** 设置为 `reciprocal` 会启用此参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `AlgorithmType` |
| **类型：** 字符向量 |
| **值：** `'Exact' | 'Newton-Raphson'` |
| **默认值：** `'Exact'` |

### **Signed power** — 幂的符号性 on（默认）| off

计算幂时，指定为 on 或 off，考虑输入信号的符号。Math Function 仅在输出信号为实数时使用此参数。

- on — 计算输入绝对值的幂，再乘以输入的符号。
- off — 计算实际输入值的幂。如果第一个输入为负数，第二个输入不是整数，且输出信号为实数，则该函数返回 `NaN`。

#### 依赖

将 **Function** 设置为 `pow` 会启用此参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `SignedPower` |
| **类型：** 字符向量 |
| **值：** `'on' | 'off' |` |
| **默认值：** `'on'` |

### **Output signal type** — 输出信号的复/实性 `auto`（默认）| `real` | `complex`

将 Math Function 模块的输出信号类型指定为 `auto`、`real` 或 `complex`。

| 函数 | 输入信号类型 | 输出信号类型 | | |
| --- | --- | --- | --- | --- |
| Auto | Real | Complex |
| `exp`、`log`、`2^u`、`10^u`、`log10`、`square`、`pow`、`reciprocal`、`conjugate`、`transpose`、`hermitian` | `real`  `complex` | `real`  `complex` | `real`  `error` | `complex`  `complex` |
| `magnitude squared` | `real`  `complex` | `real`  `real` | `real`  `real` | `complex`  `complex` |
| `hypot`、`rem`、`mod` | `real`  `complex` | `real`  `error` | `real`  `error` | `complex`  `error` |

#### 编程使用

|  |
| --- |
| **模块参数：** `OutputSignalType` |
| **类型：** 字符向量 |
| **值：** `'auto' | 'real' | 'complex'` |
| **默认值：** `'auto'` |

### **Number of iterations** — Newton-Raphson 迭代次数 3（默认）| 标量

Newton-Raphson 迭代次数，指定为标量。

#### 依赖

要启用此参数，请设置：

- **Function** 为 `reciprocal`。
- **Algorithm method** 为 `Newton-Raphson`。

#### 编程使用

|  |
| --- |
| **模块参数：** `Iterations` |
| **类型：** 字符向量 |
| **值：** `'3' | scalar` |
| **默认值：** `'3'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

#### 依赖

仅当您将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅不建议使用采样时间的模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认）| 带引号的标量或向量 |

### 信号属性

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的下限值。

软件使用最小值来执行：

- 某些模块的参数范围检查（请参阅为模块参数指定最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围并启用仿真范围检查）。
- 定点数据类型的自动定标。
- 优化您从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **Output maximum** — 用于范围检查的最大输出值 `[]`（默认）| 标量

软件检查的输出范围的上限值。

软件使用最大值来执行：

- 某些模块的参数范围检查（请参阅为模块参数指定最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围并启用仿真范围检查）。
- 定点数据类型的自动定标。
- 优化您从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **Output data type** — 指定输出数据类型 `Inherit: Same as first input`（默认）| `Inherit: Inherit via internal rule` | `Inherit: Inherit via back propagation` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定输出数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via back propagation`
- 内置数据类型的名称，例如 `single`
- 数据类型对象的名称，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型。

#### 依赖

- 要启用此参数，请将 **Function** 设置为 `magnitude^2`、`square` 或 `reciprocal`。
- 对于 `magnitude^2` 和 `square`，当输入是小于单精度的浮点数据类型时，`Inherit: Inherit via internal rule` 输出数据类型取决于 Inherit floating-point output type smaller than single precision 配置参数的设置。当编码数据类型所需的位数小于编码单精度数据类型所需的 32 位时，数据类型小于单精度。例如，`half` 和 `int16` 小于单精度。

#### 编程使用

|  |
| --- |
| **模块参数**： `OutDataTypeStr` |
| **类型**： 字符向量 |
| **值**： `'Inherit: Inherit via internal rule` | `'Inherit: Same as first input'` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**： `'Inherit: Same as first input'` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块上指定的 **Output** 数据类型。有关详细信息，请参阅使用锁定输出数据类型设置 (Fixed-Point Designer)。

#### 依赖

要启用此参数，请将 **Function** 设置为 `magnitude^2`、`square` 或 `reciprocal`。

#### 编程使用

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB 舍入函数的表达式。

#### 依赖

要启用此参数，请将 **Function** 设置为 `magnitude^2`、`square` 或 `reciprocal`。

#### 编程使用

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值：** `'Floor'` |

### **Saturate on integer overflow** — 选择整数溢出时的行为 `on`（默认）| 布尔值

| 操作 | 理由 | 溢出 | 示例 |
| --- | --- | --- | --- |
| 选中 **Saturate on integer overflow** 复选框。 | 您的模型可能发生溢出，并且您希望在生成的代码中提供显式的饱和保护。 | 溢出饱和到数据类型可以表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中该复选框后，模块输出饱和于 127。类似地，模块输出饱和于最小输出值 -128。 |
| 不选中 **Saturate on integer overflow** 复选框。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅排查信号范围错误。 | 溢出回绕到数据类型可表示的相应值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框后，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 -126。 |

当您选中此复选框时，饱和应用于模块上的每个内部运算，而不仅仅是输出或结果。代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 依赖

要启用此参数，请将 **Function** 设置为 `magnitude^2`、`square`、`conj`、`reciprocal` 或 `hermitian`。

#### 编程使用

|  |
| --- |
| **模块参数**： `SaturateOnIntegerOverflow` |
| **类型**： 字符向量 |
| **值**： `'off'` | `'on'` |
| **默认值**： `'on'` |

## 所属库

Simulink / Math Operations HDL Coder / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

| 函数 | 架构 | 描述 |
| --- | --- | --- |
| `conj` | `ComplexConjugate` | 计算复共轭。 |
| `hermitian` | `Hermitian` | 计算埃尔米特转置。 |
| `transpose` | `Transpose` | 计算数组转置。请参阅 Simulink 文档中的 Math Function。 |
| `mod`  `rem` | `ShiftAdd` | 通过使用非恢复除法算法对内置整数类型输入执行取模或求余运算，该算法执行多次移位和加法操作来计算 `mod` 和 `rem` 运算。`ShiftAdd` 是一种流水线实现，它可能会在生成的代码中引入额外的延迟。使用此架构，您还可以通过设置 **LatencyStrategy** 参数来设置延迟策略。 |

**倒数架构**

当您将 **Algorithm method** 设置为 `Exact` 时，您可以在该模块的 HDL Block 属性中选择此选项。

| 架构 | 参数 | 额外延迟周期 | 描述 |
| --- | --- | --- | --- |
| `ShiftAdd(default)` | 无 | 有符号输入：(输入字长 + 4)  无符号输入：(输入字长 + 4)  有关模块的浮点延迟，请参阅浮点运算符的延迟值 (HDL Coder)。 | 通过使用非恢复除法算法对定点或浮点输入执行倒数运算，该算法执行多次移位和加法操作来计算倒数。与 Newton-Raphson 近似方法相比，此架构提供了更高的精度。当您使用定点数据类型时，必须满足以下条件才能生成 HDL 代码： - 输入字长 (`WL`) 必须小于或等于 63。 - `[WL input + Abs(FL Sum)]` 必须小于或等于 63。其中，`FL Sum` 由下式给出：`FL sum = FL input + FL output` |

您可以在 `ShiftAdd` 架构中对 Math Function Reciprocal 模块应用共享优化。有关详细信息，请参阅资源分享 (HDL Coder)。

此模块具有多周期实现，会在生成的代码中引入额外延迟。要查看增加的延迟，请查看生成的模型或验证模型。请参阅生成的模型和验证模型 (HDL Coder)。

HDL 代码生成还支持 `reciprocal` 函数的 Newton-Raphson 算法方法。选择 **Algorithm method** 为 `Newton-Raphson`，以在 Math Function 模块中对 `reciprocal` 函数使用这些架构。

| 架构 | 额外延迟周期 | 描述 |
| --- | --- | --- |
| `ReciprocalNewton` (default) | `Iterations` + 1 | 使用迭代牛顿法的多速率实现。选择此选项可优化设计的面积。`Iterations` 的默认值为 3。`Iterations` 的建议值为 2 到 10。如果 `Iterations` 值超出建议范围，HDL Coder 会显示一条消息。 |
| `ReciprocalNewtonSingleRate` | (`Iterations` \* 2) + 1 | 使用单速率流水线牛顿法。选择此选项可优化设计的速度，或者如果您需要单速率实现。`Iterations` 的默认值为 3。`Iterations` 的建议值为 2 到 10。如果 `Iterations` 值超出建议范围，HDL Coder 会显示一条消息。 |
| ReciprocalRsqrtBasedNewtonSingleRate | 有符号输入：(`Iterations` \* 4) + 8  无符号输入：(`Iterations` \* 4) + 6 | 使用单速率流水线牛顿法。选择此选项可优化速度，或者如果您需要单速率实现。`Iterations` 的默认值为 3。`Iterations` 的建议值为 2 到 10。如果 `Iterations` 超出建议范围，代码生成器会生成一条消息。 |

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **LatencyStrategy** | 要启用此属性，请将 HDL 架构设置为 `ShiftAdd`。指定是否将设计中的模块映射为定点类型的 `MAX`、`Min`、`CUSTOM` 或 `ZERO` 延迟。默认值为 `MAX`。另请参阅 LatencyStrategy (HDL Coder)。 |
| **CustomLatency** | 要启用此属性，请将 HDL 架构设置为 `ShiftAdd`。当 **LatencyStrategy** 设置为 `CUSTOM` 时，使用此属性为定点类型指定介于 `ZERO` 和 `MAX` 之间的自定义延迟值。另请参阅 LatencyStrategy (HDL Coder)。 |

| 原生浮点 | |
| --- | --- |
| **CheckResetToZero** | 将此属性用于 Math Function 模块的 `mod` 和 `rem` 函数。如果您有数字 `a` 和 `b`，使得商 `a/b` 接近整数，此设置将 `a` 视为 `b` 的整数倍，并且 `rem(a,b)` = 0。此结果在数值上是准确的，并且与仿真结果匹配。计算此结果会使用额外资源，并增加目标 FPGA 器件上的面积占用。有关更多信息，请参阅 CheckResetToZero (HDL Coder)。 |
| **HandleDenormals** | 指定您是否希望 HDL Coder 插入附加逻辑来处理设计中的非规格化数。非规格化数是幅值小于最小浮点数的数，该最小浮点数可以在尾数中没有前导零的情况下表示。默认值为 `inherit`。另请参阅 HandleDenormals (HDL Coder)。 |
| **LatencyStrategy** | 指定是否将设计中的模块映射为浮点运算符的 `inherit`、`Max`、`Min`、`Zero` 或 `Custom`。默认值为 `inherit`。另请参阅 LatencyStrategy (HDL Coder)。 |
| **NFPCustomLatency** | 要指定值，请将 **LatencyStrategy** 设置为 `Custom`。HDL Coder 会添加等于您为 **NFPCustomLatency** 设置指定的值的延迟。另请参阅 NFPCustomLatency (HDL Coder)。 |
| **MaxIterations** | 将此属性用于 Math Function 模块的 `mod` 和 `rem` 函数。如果您有数字 `a` 和 `b`，它们是非常大的整数，您可以增加 **MaxIterations** 以匹配仿真结果。计算此结果会使用额外资源，并增加目标 FPGA 器件上的面积占用。有关更多信息，请参阅 MaxIterations (HDL Coder)。 |
| **IterationsPerPipeline** | 将此属性用于 Math Function 模块的 `reciprocal` 函数。要启用此属性，请将 **Algorithm method** 参数设置为 `Exact`。当您将 **LatencyStrategy** 设置为 `Custom(PerIterations)` 时，使用此设置来指定每个流水线级的迭代次数。有关更多信息，请参阅 Reciprocal (HDL Coder)。 |

**原生浮点中支持的数据类型和函数**

Math Function 模块支持标量、向量或矩阵数据类型。此模块通过原生浮点支持这些函数。

| 数学函数 | 支持的浮点数据类型 | | | 定点数据类型支持 | 复数数据支持 |
| --- | --- | --- | --- | --- | --- |
| Half | Single | Double |
| `exp` | 否 | 是 | 否 | 否 | 否 |
| `log` | 否 | 是 | 是 | 否 | 否 |
| `2^u` | 否 | 是 | 否 | 否 | 否 |
| `10^u` | 否 | 是 | 否 | 否 | 否 |
| `log10` | 否 | 是 | 否 | 否 | 否 |
| `magnitude^2` | 否 | 是 | 是 | 是 | 是 |
| `square` | 否 | 是 | 否 | 是 | 是 |
| `pow` | 否 | 是 | 否 | 否 | 否 |
| `conj` | 否 | 是 | 否 | 是 | 是 |
| `reciprocal` | 是 | 是 | 是 | 是 | 否 |
| `hypot` | 否 | 是 | 否 | 否 | 否 |
| `rem` | 否 | 是 | 否 | 否 | 否 |
| `mod` | 否 | 是 | 否 | 否 | 否 |
| `transpose` | 是 | 是 | 是 | 是 | 是 |
| `hermitian` | 否 | 是 | 否 | 是 | 是 |

**限制**

当您使用 `reciprocal` 实现时：

- 输入必须是标量，并且必须具有整数或定点（有符号或无符号）数据类型。
- 输出必须是标量，并且具有整数或定点（有符号或无符号）数据类型。
- 必须选中模块上的 **Saturate on integer overflow** 选项。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

Math Function 模块仅在特定配置中支持定点转换。有关更多信息，请参阅模块支持表。

## 版本历史

**在 R2006a 之前引入**

### R2023a: `Math Function` 模块支持 2^u

Math Function 模块现在支持 `2^u` 函数。MATLAB 等效项为 `2.^u`（请参阅 `power`）。

## 描述

执行数学函数

Math Function 模块执行许多常见的数学函数。

您可以从 Math Function 模块的 **Function** 参数列表中选择以下函数之一。

| 函数 | 描述 | 数学表达式 | MATLAB® 等效项 |
| --- | --- | --- | --- |
| `exp` | 指数 | `eu` | `exp` |
| `log` | 自然对数 | `ln u` | `log` |
| `2^u` | 以 2 为底的幂 | `2u` | `2.^u`（请参阅 `power`） |
| `10^u` | 以 10 为底的幂 | `10u` | `10.^u`（请参阅 `power`） |
| `log10` | 常用（以 10 为底）对数 | `log u` | `log10` |
| `magnitude^2` | 复模 | `|u|2` | `real(u).^2 + imag(u).^2`（请参阅 `real`、`imag` 和 `power`） |
| `square` | 2 次幂 | `u2` | `u.^2`（请参阅 `power`） |
| `pow` | 幂 | - 选中 **Signed power** 且 **Output signal type** 设置为 `real` 时，表达式为 `sign(u)*|u|v`。 - 清除 **Signed power** 或 **Output signal type** 设置为 `complex` 时，表达式为 `uv`。 - 当 **Output signal type** 设置为 `auto` 时，表达式取决于软件编译的复数类型。 | `power` |
| `conj` | 复共轭 | `ū` | `conj` |
| `reciprocal` 使用 Exact 方法 | 倒数 | `1/u` | `1./u`（请参阅 `rdivide`） |
| `reciprocal` 使用 Newton-Raphson 方法 | 倒数 | 请参阅 Newton-Raphson 倒数算法方法 | 无 |
| `hypot` | 平方和的平方根 | `(u2+v2)0.5` | `hypot` |
| `rem` | 除法后的余数 | — | `rem` |
| `mod` | 除法后的模数 | — | `mod` |
| `transpose` | 转置 | `uT` | `u.'`（请参阅数组与矩阵运算） |
| `hermitian` | 复共轭转置 | `uH` | `u'`（请参阅数组与矩阵运算） |

**提示**

要执行平方根计算，请使用 Sqrt 模块。

模块输出是对输入或输入执行函数运算的结果。这些函数支持以下类型的运算。

| 函数 | 标量运算 | 逐元素向量和矩阵运算 | 向量和矩阵运算 |
| --- | --- | --- | --- |
| `exp` | 是 | 是 | 不适用 |
| `log` | 是 | 是 | 不适用 |
| `2^u` | 是 | 是 | 不适用 |
| `10^u` | 是 | 是 | 不适用 |
| `log10` | 是 | 是 | 不适用 |
| `magnitude^2` | 是 | 是 | 不适用 |
| `square` | 是 | 是 | 不适用 |
| `pow` | 是 | 是 | 不适用 |
| `conj` | 是 | 是 | 不适用 |
| `reciprocal` 使用 Exact 方法 | 是 | 是 | 不适用 |
| `reciprocal` 使用 Newton-Raphson 方法 | 是 | 是 | 不适用 |
| `hypot` | 是，对两个输入 | 是，对两个输入（两个相同大小的向量或两个相同大小的矩阵、一个标量和一个向量，或一个标量和一个矩阵） | — |
| `rem` | 是，对两个输入 | 是，对两个输入（两个相同大小的向量或两个相同大小的矩阵、一个标量和一个向量，或一个标量和一个矩阵） | 不适用 |
| `mod` | 是，对两个输入 | 是，对两个输入（两个相同大小的向量或两个相同大小的矩阵、一个标量和一个向量，或一个标量和一个矩阵） | 不适用 |
| `transpose` | 是 | — | 是 |
| `hermitian` | 是 | — | 是 |

函数名称和相应数量的输入端口会显示在模块上。

**提示**

当您需要向量或矩阵输出时，请使用 Math Function 模块。

### Newton-Raphson 倒数算法方法

具有 Newton-Raphson 算法方法的 `reciprocal` 函数使用 Newton-Raphson 近似方法计算倒数。该函数使用递归近似来找到实值函数根的更好近似值。

实数 a 的倒数定义为函数的一个零点：

f(x)=1x−a.

Simulink® 在范围 0<x0<2a 内选择初始估计值，因为这是该函数的收敛域。

要连续计算函数的根，请指定 **Number of iterations** 参数。该过程重复如下：

xi+1=xi−f(xi)f'(xi)=xi+(xi−axi2)=xi.(2−axi)

f'(x) 是函数 f(x) 的导数。

### 数据类型支持

此表列出了模块的每个函数可以支持的输入数据类型。

| 函数 | Single | Double | Half\* | Boolean | 内置整数 | 定点 |
| --- | --- | --- | --- | --- | --- | --- |
| `exp` | 是 | 是 | 是 | — | — | — |
| `log` | 是 | 是 | 是 | — | — | — |
| `2^u` | 是 | 是 | 是 | — | — | — |
| `10^u` | 是 | 是 | 是 | — | — | — |
| `log10` | 是 | 是 | 是 | — | — | — |
| `magnitude^2` | 是 | 是 | 是 | — | 是 | 是 |
| `square` | 是 | 是 | 是 | — | 是 | 是 |
| `pow` | 是 | 是 | 是 | — | — | — |
| `conj` | 是 | 是 | 是 | — | 是 | 是 |
| `reciprocal` 使用 Exact 方法 | 是 | 是 | 是 | — | 是 | 是 |
| `reciprocal` 使用 Newton-Raphson 方法（有关更多信息，请参阅输出） | 是 | 是 | — | — | 是 | 是 |
| `hypot` | 是 | 是 | 是 | — | — | — |
| `rem` | 是 | 是 | 是 | — | 是 | — |
| `mod` | 是 | 是 | 是 | — | 是 | — |
| `transpose` | 是 | 是 | 是 | 是 | 是 | 是 |
| `hermitian` | 是 | 是 | 是 | — | 是 | 是 |

有关半精度算术运算的更多信息，请参阅 Simulink 中的半精度数据类型 (Fixed-Point Designer)。
