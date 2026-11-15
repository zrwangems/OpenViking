---
type: simulink-block
title: 'Sqrt'
family: math-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'sqrt'
---

# Sqrt

Calculate square root, signed square root, or reciprocal of square root

## 中文

计算平方根、带符号的平方根或平方根的倒数

### 所属库

Simulink / Math Operations HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

### 描述

Sqrt 模块计算输入信号的平方根、有符号平方根或平方根的倒数。从**函数**下拉列表中选择以下函数之一。

| 函数 | 描述 | 数学表达式 | MATLAB® 等效函数 |
| --- | --- | --- | --- |
| `sqrt` | 输入信号的平方根 | `u0.5` | `sqrt` |
| `signedSqrt` | 输入信号绝对值的平方根乘以输入信号的符号 | `sign(u)*|u|0.5` | — |
| `rSqrt` | 输入信号的平方根的倒数 | `u-0.5` | — |

模块图标将发生变化以匹配函数。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

模块的输入信号，用于计算平方根、有符号平方根或平方根的倒数。`sqrt` 函数接受实数或复数输入，但复数定点信号除外。`signedSqrt` 和 `rSqrt` 不接受复数输入。输入信号必须为浮点数。

下表总结了 `sqrt`、`rSqrt` 和 `signedSqrt` 函数的浮点、整数和定点数据类型对复数类型和负值的支持。

| 函数 | 数据类型 | 复数 | | 负值 |
| --- | --- | --- | --- | --- |
| 输入 | 输出 |
| `sqrt` | 浮点 | 是 | 是 | 是 |
|  | 整数和定点 | 否 | 否 | 否 |
| `rSqrt` | 浮点 | 否 | 否 | 是 |
|  | 整数和定点 | 否 | 否 | 否 |
| `signedSqrt` | 浮点 | 否 | 是 | 是 |
|  | 整数和定点 | 否 | 否 | 否 |

如果输入为负数，请将除 `signedSqrt` 之外的所有函数的**输出信号**设置为复数。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

输出信号，是输入信号的平方根、有符号平方根或平方根的倒数。当输入信号的类型为整数或定点时，输出必须为浮点。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### 常设

#### **函数** — 模块执行的函数 **sqrt** | **signedSqrt** | **rSqrt**

指定模块计算的数学函数。模块图标将发生变化以匹配您选择的函数。

| 函数 | 模块图标 |
| --- | --- |
| `sqrt` | Sqrt block |
| `signedSqrt` | Signed Sqrt block |
| `rSqrt` | Reciprocal Sqrt block |

默认值取决于模块配置。

- **sqrt** 默认值 - Sqrt 和 Square Root 模块
- **signedSqrt** 默认值 - Signed Sqrt 和 Signed Square Root 模块
- **rSqrt** 默认值 - Reciprocal Sqrt 和 Reciprocal Square Root 模块

##### 编程用法

|  |
| --- |
| **模块参数**：`Operator` |
| **类型**：字符向量 |
| **值**：`'sqrt'` | `'signedSqrt'` | `'rSqrt'` |

#### **输出信号类型** — 输出信号类型 **自动** (默认) | **实数** | **复**

指定模块的输出信号类型。

| 函数 | 输入信号类型 | 输出信号类型 | | |
| --- | --- | --- | --- | --- |
| 自动 | 实数 | 复数 |
| `sqrt` | `real` | 对于非负输入为 `real`  对于负输入为 `NaN` | 对于非负输入为 `real`  对于负输入为 `NaN` | `complex` |
| `complex` | `complex` | `error` | `complex` |
| `signedSqrt` | `real` | `real` | `real` | `complex` |
| `complex` | `error` | `error` | `error` |
| `rSqrt` | `real` | `real` | `real` | `error` |
| `complex` | `error` | `error` | `error` |

##### 编程用法

|  |
| --- |
| **模块参数**：`OutputSignalType` |
| **类型**：字符向量 |
| **值**：`'auto'` | `'real'` | `'complex'` |
| **默认值**：`'auto'` |

#### **采样时间(-1 表示继承)** — 采样之间的时间间隔 `-1` (默认) | 标量 | 向量

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

##### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时才可见。要了解详细信息，请参阅不建议设置采样时间的模块。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `"-1"` (默认) | scalar or vector in quotes |

#### 算法

#### **方法** — 计算平方根倒数的方法 **完全** (默认) | **牛顿-拉夫逊**

指定用于计算平方根倒数的方法。

| 方法 | 支持的数据类型 | 何时使用此方法 |
| --- | --- | --- |
| **完全** | 浮点 | 您不需要逼近值时。  输入或输出必须为浮点类型。 |
| **牛顿-拉夫逊** | 浮点、定点和内置的整数类型 | 您需要快速的近似计算时。 |

**完全**方法提供了与 MATLAB 计算一致的结果。

##### 依赖关系

要启用此参数，请将**函数**设置为 **rSqrt**。

当**函数**设置为 **sqrt** 或 **signedSqrt** 时，此参数设置为**完全**。

##### 编程用法

|  |
| --- |
| **模块参数**：`AlgorithmType` |
| **类型**：字符向量 |
| **值**：`'Exact'` | `'Newton-Raphson'` |
| **默认值**：`'Exact'` |

#### **迭代次数** — 牛顿-拉夫逊算法的迭代次数 `3` (默认) | 整数

指定执行牛顿-拉夫逊算法的迭代次数。在使用 `rSqrt` 函数且**方法**的值为**牛顿-拉夫逊**时，此参数有效。

如果您输入 `0`，则模块输出是牛顿-拉夫逊算法的初始估计值。

##### 编程用法

|  |
| --- |
| **模块参数**：`Iterations` |
| **类型**：字符向量 |
| **值**：整数 |
| **默认值**：`'3'` |

#### 数据类型

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

#### **中间结果数据类型** — 中间结果的数据类型 **继承: 从内部规则继承** (默认) | **继承: 从输入继承** | **继承: 从输出继承** | **double** | **single** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16,,0)** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>**

当您将**函数**设置为 **sqrt** 或 **rSqrt** 时，请指定中间结果的数据类型。

该类型可以继承、直接指定或表示为数据类型对象，如 `Simulink.NumericType` 对象。

为了避免溢出，中间数据类型必须大于或等于可以包含输出数据类型平方的数据类型。

为平方根函数 `sqrt` 显式设置中间数据类型时，请遵循以下规范：

| 输入和输出数据类型 | 中间数据类型 |
| --- | --- |
| 输入或输出为双精度。 | 使用双精度。 |
| 输入或输出是单精度，而且有任何非单精度数据类型*不*是双精度。 | 使用单精度或双精度。 |
| 输入和输出是定点。 | 使用定点。 |

为平方根倒数函数 `rSqrt` 显式设置中间数据类型时，请遵循以下规范：

| 输入和输出数据类型 | 中间数据类型 |
| --- | --- |
| 输入是双精度，输出不是单精度。 | 使用双精度。 |
| 输入不是单精度，输出是双精度。 | 使用双精度。 |
| 输入和输出是定点。 | 使用定点。 |

**小心**

在下列情况下，不要将**中间结果数据类型**设置为**继承:从输出继承**：

- 您选择了**牛顿-拉夫逊**方法来计算平方根的倒数。
- 输入数据类型为浮点。
- 输出数据类型为定点。

在这些情况下，选择**继承:从输出继承**会使性能受到影响并产生错误。

要避免此错误，请将浮点类型的输入信号转换成定点数据类型。例如，在 Sqrt 模块之前插入一个 Data Type Conversion 模块以执行转换。

##### 依赖关系

要启用此参数，请将**函数**设置为 **sqrt** 或 **rSqrt**。

##### 编程用法

|  |
| --- |
| **模块参数**：`IntermediateResultsDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via internal rule'` | `'Inherit: Inherit from input'` | `'Inherit: Inherit from output'` | `'double'` | `'single'`、`'int8'`、`'uint8'`、`int16`、`'uint16'`、`'int32'`、`'uint32'`、`'int64'`、`'uint64'`、`fixdt(1,16,0)`、`fixdt(1,16,2^0,0)`。`'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

#### **输出** — 输出数据类型 **继承: 与第一个输入相同** (默认) | **继承: 从内部规则继承** | **继承: 通过反向传播继承** | **double** | **single** | **half** | **int8** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>** | ...

指定输出数据类型。该类型可以继承、直接指定或表示为数据类型对象，如 `Simulink.NumericType` 对象。

##### 依赖关系

当输入是小于单精度的浮点数据类型时，**继承: 从内部规则继承**输出数据类型取决于 Inherit floating-point output type smaller than single precision 配置参数的设置。当对数据类型进行编码所需的位数小于对单精度数据类型编码所需的 32 位时，数据类型小于单精度。例如，`half` 和 `int16` 小于单精度。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | **fixdt(1,16,2^0,0)** | `fixdt(1,16,2^0,0)` | `'<data type expression>'` |
| **默认值**：`'Inherit: Same as first input'` |

#### **最小** — 范围检查的最小输出值 `[]` (默认) | 标量

将软件检查的输出范围的下限值指定为有限的双精度实数标量值。

如果您指定总线对象作为此模块的数据类型，请不要为模块上的总线数据设置最小值。软件会忽略此设置。但请为指定作为数据类型的总线对象的总线元素设置最小值。有关详细信息，请参阅 `Simulink.BusElement`。

软件使用最小值执行下列操作：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

##### 提示

**输出最小值**不会对实际输出信号进行饱和处理或截断。请改用 Saturation 模块。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'[]'` |

#### **最大** — 范围检查的最大输出值 `[]` (默认) | 标量

将软件检查的输出范围的上限值指定为有限的双精度实数标量值。

如果您指定总线对象作为此模块的数据类型，请不要为模块的总线数据设置最大值。软件会忽略此设置。但请为指定作为数据类型的总线对象的总线元素设置最大值。有关详细信息，请参阅 `Simulink.BusElement`。

软件使用最大值执行下列操作：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

##### 提示

**输出最大值**不会对实际输出信号进行饱和处理或截断。请改用 Saturation 模块。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'[]'` |

#### **整数舍入模式** — 定点运算的舍入模式 **向下** (默认) | **向上** | **收敛** | **最邻近值** | **舍入** | **最简** | **零**

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

##### 编程用法

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型：**字符向量 |
| **值：**`'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值：**`'Floor'` |

#### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选中此选项将锁定此模块的输出数据类型设置，从而防止通过定点工具和定点顾问进行更改。有关详细信息，请参阅Use Lock Output Data Type Setting (Fixed-Point Designer)。

##### 编程用法

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

#### **对整数溢出进行饱和处理** — 溢出操作的方法 `on` (默认) | `off`

指定对溢出是进行饱和处理还是绕回处理。

- `on` - 将溢出饱和处理为数据类型能够表示的最小值或最大值。
- `off` - 溢出将绕回到数据类型可以表示的合适值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选择此参数后，模块输出将在达到 127 时饱和。类似地，模块输出将在达到最小输出值 -128 时饱和。
- 清除此参数后，软件会将导致溢出的值解释为 `int8`，这可能产生意外结果。例如，以 `int8` 表示的模块结果 130（二进制 1000 0010）为 -126。

##### 提示

- 如果您的模型存在可能的溢出，而您希望在生成的代码中进行显式饱和保护，请考虑选中此参数。
- 如果您希望优化生成的代码的效率，请考虑清除此参数。清除此参数还可以帮助您避免过度地指定信号超出范围时模块的处理方式。有关详细信息，请参阅信号范围错误故障排除。
- 如果选中此参数，饱和将应用于模块中的每个内部操作，而不仅仅应用于输出或结果。
- 一般情况下，代码生成进程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SaturateOnIntegerOverflow` |
| **值:** | `'on'` (默认) | `'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

| 函数 | 架构 | 描述 |
| --- | --- | --- |
| **sqrt**  **signedSqrt**  **rSqrt** | **SqrtFunction**（默认值） | 使用流水线移位相加算法或基于乘法的算法计算平方根。**sqrtfunction** 架构支持定点类型和浮点类型的代码生成。当您使用浮点类型时，选择**使用浮点**配置参数。您可以指定 HDL 属性 **LatencyStrategy** 和 **CustomLatency**，以便在硬件平台上设计时从一系列频率值中进行选择。  将 HDL 模块属性 **UseMultiplier** 与 **LatencyStrategy** 和 **CustomLatency** 属性结合使用，以指定是使用流水线移位相加算法还是使用乘法算法来计算平方根。通过将 **UseMultiplier** 设置为 `off` 并将 **LatencyStrategy** 设置为 `inherit`，改进设计频率并减少资源使用。 |
| **sqrt** | **SqrtNewton** | 使用牛顿迭代法优化面积。 |
| **sqrt** | **SqrtNewtonSingleRate** | 使用单频率流水线牛顿法。要优化速度或需要单速率实现，请选择此选项。 |
| **rSqrt** | **RecipSqrtNewton** | 使用牛顿迭代法优化面积。  要指定此架构，请将**方法**设置为**牛顿-拉夫逊**。 |
| **rSqrt** | **RecipSqrtNewtonSingleRate** | 使用单频率流水线牛顿法。要优化速度或需要单速率实现，请选择此选项。  要指定此架构，请将**方法**设置为**牛顿-拉夫逊**。 |

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **迭代数** | **SqrtNewton** 或 **SqrtNewtonSingleRate** 实现的迭代次数。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |
| **UseMultiplier** | 为 **SqrtFunction** 实现选择算法。默认情况下，此属性设置为 `off`，并且此模块使用移位相加算法计算平方根。当该属性设置为 `on` 时，通过使用乘数计算平方根。  通过将 **UseMultiplier** 设置为 `off` 并将 **LatencyStrategy** 设置为 `inherit`，提高设计频率并减少资源使用。 |
| **LatencyStrategy** | 对于定点和浮点类型，指定是将设计中的模块映射到 `MAX`、`MIN`、`CUSTOM` 还是 `ZERO` 延迟。默认值为 **MAX**。浮点类型的模块设置会覆盖模型级设置。对于定点类型，模块级设置确定延迟策略。另请参阅LatencyStrategy (HDL Coder)。  通过将 **UseMultiplier** 设置为 `off` 并将 **LatencyStrategy** 设置为 `inherit`，提高设计频率并减少资源使用。  您可以通过将 **LatencyStrategy** 设置为 `Custom(PerIterations)` 来控制迭代算法的流水线阶段。有关详细信息，请参阅Sqrt (HDL Coder)。 |
| **CustomLatency** | 当 **LatencyStrategy** 设置为 `CUSTOM` 时，如果您使用定点类型，请使用此属性为定点类型指定介于 `ZERO` 和 `MAX` 之间的自定义延迟值。对于浮点类型，此值成为运算符的自定义延迟。另请参阅NFPCustomLatency (HDL Coder)。 |
| **IterationsPerPipeline** | 当 **LatencyStrategy** 设置为 `Custom(PerIterations)` 时，使用此设置指定每个流水线阶段的迭代次数。要启用此属性，请将 HDL 架构设置为 **SqrtFunction**。  有关详细信息，请参阅Sqrt (HDL Coder)。 |

| 原生浮点 | |
| --- | --- |
| **HandleDenormals** | 指定是否希望 HDL Coder 在设计中插入额外的逻辑来处理非正规数字。非正规数是大小非常小、必须使用包含前导零的尾数才能表示的浮点数。默认值为 **inherit**。另请参阅HandleDenormals (HDL Coder)。 |

**数据类型支持**

该模块支持使用以下数据类型进行 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 复信号 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | 标量  向量  矩阵（最高二维） | 是 | 单精度  双精度 | 是 | 是 | 否 | 否 |

**延迟详细信息**

此模块具有多周期实现，这会在生成的代码中引入额外的延迟。要查看增加的延迟，请查看生成的模型或验证模型。请参阅Generated Model and Validation Model (HDL Coder)。

**浮点延迟**

| 架构 | 浮点类型 | 延迟策略 | 延迟（周期数） | 自定义延迟支持 |
| --- | --- | --- | --- | --- |
| **SqrtFunction** | 单精度 | 最小值 | 16 | 是 |
| 最大值 | 28 |
| 双精度 | 最小值 | 33 |
| 最大值 | 58 |

**定点延迟**

| 架构 | 最大延迟（周期数） | 描述 | 延迟策略支持 | 自定义延迟支持 |
| --- | --- | --- | --- | --- |
| **SqrtFunction** | 要计算定点数据类型的延迟，请参阅 Sqrt (HDL Coder) 中的*算法*。 | 最大延迟由输出字长以及定点数据的输入和输出小数长度确定。 | 是 | 是 |
| **SqrtNewton** | **迭代数** + 3 | **迭代数** HDL 模块属性的默认值为 3。  **迭代数**的推荐值为 2 到 10。如果**迭代数**超出推荐范围，HDL Coder 会生成一条消息。 | 否 | 否 |
| **SqrtNewtonSingleRate** | (**迭代数**\* 4) + 6 |
| **RecipSqrtNewton** | **迭代次数** + 2 | **迭代次数**模块参数的默认值为 3。  **迭代次数**的推荐值是从 2 到 10。如果**迭代次数**超出推荐范围，HDL Coder 将生成一条消息。 |
| **RecipSqrtNewtonSingleRate** | (**迭代次数**\* 4) + 5 |

**模块参数配置**

以下模块参数配置与 HDL 代码生成不兼容。

| 模块参数 | 限制和注意事项 |
| --- | --- |
| **输出信号类型** | 不支持参数值**复数**。 |
| **方法** | 当您将**函数**参数设置为 **rSqrt** 时，请对浮点数据类型使用**完全**，对定点数据类型使用**牛顿-拉夫逊**。 |
| **中间结果数据类型** | 不支持**继承:通过内部规则继承**以外的参数值 |
| **输出** | 选择与输入相同的输出端口数据类型。 |
| **整数舍入模式** | 定点类型不支持参数值**收敛**、**舍入**。 |

**优化**

您可以使用以下 HDL Coder 优化来优化速度、面积和 I/O。

**面积优化**

| 优化 | 描述 |
| --- | --- |
| Resource Sharing (HDL Coder) | *资源复用*是一种面积优化，其中 HDL Coder 确定多个在功能上等效的资源，并用单个资源替换它们。 |
| Streaming (HDL Coder) | *流式处理*是一种面积优化，其中 HDL Coder 将向量数据路径变换为标量数据路径（或多个较小的向量数据路径）。 |

**速度优化**

| 优化 | 描述 |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *分布式流水线*或寄存器重定时是一种速度优化，它可以移动设计中的现有延迟，以在缩减关键路径的同时保留功能性行为。  对于 Sqrt 模块，HDL Coder 在模块周围（而不是在模块内）分布流水线寄存器。 |
| Clock-Rate Pipelining (HDL Coder) | *时钟频率流水线*是 HDL Coder 中的一个优化框架，它允许其他速度优化和面积优化在时钟频率下引入延迟。 |
| 关键路径估计 (HDL Coder) | 要快速确定设计中最可能的关键路径，请使用*关键路径估计*。关键路径估计加速寻找关键路径的迭代过程。要了解在关键路径估计中表征的模块，请参阅Characterized Blocks (HDL Coder)。 |

**I/O 优化**

| 优化 | 描述 |
| --- | --- |
| 帧到采样的转换 (HDL Coder) | 要优化您的设计所需的 I/O，请使用帧到采样的转换。这种优化将基于帧的向量或矩阵输入转换为更小的采样或像素，以便 HDL 代码生成到基于流的目标硬件，并减小处理大输入和输出信号所需的 FPGA I/O。 |

**HDL 算法**

HDL Coder 通过使用牛顿-拉夫逊迭代法在 **ReciprocalRsqrtBasedNewton** 和 **ReciprocalRsqrtBasedNewtonSingleRate** 架构中实现倒数平方根运算，方程如下：

xi+1=xi−f(xi)f'(xi)=xi(1.5−0.5axi2)

f(x)=1x2−1

**限制**

基于牛顿-拉夫逊的实现与在原生浮点模式下的 HDL 代码生成不兼容。要在原生浮点模式下生成 HDL 代码，请在 HDL 模块属性中选择 **SqrtFunction** 架构。

**HDL 建模规范**

Use SqrtFunction Architecture for Square Root Block (HDL Coder)

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2010a 中推出**

## Libraries

Simulink / Math Operations HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

## Description

The Sqrt block calculates the square root, signed square root, or
reciprocal of square root on the input signal. Select one of the following functions
from the **Function** parameter list.

| Function | Description | Mathematical Expression | MATLAB® Equivalent |
| --- | --- | --- | --- |
| `sqrt` | Square root of the input | `u0.5` | `sqrt` |
| `signedSqrt` | Square root of the absolute value of the input, multiplied by the sign of the input | `sign(u)*|u|0.5` | — |
| `rSqrt` | Reciprocal of the square root of the input | `u-0.5` | — |

The block icon changes to match the function.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal to the block to calculate the square root, signed square root, or
reciprocal of square root. The `sqrt` function accepts
real or complex inputs, except for complex fixed-point signals.
`signedSqrt` and `rSqrt` do not
accept complex inputs. The input signal must be a floating point
number.

This table summarizes the support for complex types and negative
values for floating point, integer, and fixed-point data types for
`sqrt`, `rSqrt`, and
`signedSqrt` functions.

| Function | Data Type | Complex | | Negative Values |
| --- | --- | --- | --- | --- |
| Input | Output |
| `sqrt` | Floating point | Yes | Yes | Yes |
|  | Integer and fixed-point | No | No | No |
| `rSqrt` | Floating point | No | No | Yes |
|  | Integer and fixed-point | No | No | No |
| `signedSqrt` | Floating point | No | Yes | Yes |
|  | Integer and fixed-point | No | No | No |

If the input is negative, set the **Output signal** to complex for all
functions except `signedSqrt`.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output signal that is the square root, signed square root, or
reciprocal of square root of the input signal. When the input is an
integer or fixed-point type, the output must be floating point.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### Main

### **Function** — Function the block performs `sqrt` | `signedSqrt` | `rSqrt`

Specify the mathematical function that the block calculates. The block
icon changes to match the function you select.

| Function | Block Icon |
| --- | --- |
| `sqrt` | Sqrt block |
| `signedSqrt` | Signed Sqrt block |
| `rSqrt` | Reciprocal Sqrt block |

The default value depends on the block configuration.

- `sqrt` default — Sqrt
  and Square Root blocks
- `signedSqrt` default — Signed
  Sqrt and Signed Square Root
  blocks
- `rSqrt` default — Reciprocal
  Sqrt and Reciprocal Square Root
  blocks

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Operator` |
| **Type**: character vector |
| **Values**: `'sqrt'` | `'signedSqrt'` | `'rSqrt'` |

### **Output signal type** — Output signal type `auto` (default) | `real` | `complex`

Specify the output signal type of the block.

| Function | Input Signal Type | Output Signal Type | | |
| --- | --- | --- | --- | --- |
| Auto | Real | Complex |
| `sqrt` | `real` | `real` for nonnegative inputs  `NaN` for negative inputs | `real` for nonnegative inputs  `NaN` for negative inputs | `complex` |
| `complex` | `complex` | `error` | `complex` |
| `signedSqrt` | `real` | `real` | `real` | `complex` |
| `complex` | `error` | `error` | `error` |
| `rSqrt` | `real` | `real` | `real` | `error` |
| `complex` | `error` | `error` | `error` |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputSignalType` |
| **Type**: character vector |
| **Values**: `'auto'` | `'real'` | `'complex'` |
| **Default**: `'auto'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Dependencies

This parameter is visible only if you set it to a value other than
`-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar or vector in quotes |

### Algorithm

### **Method** — Method to compute reciprocal of square root `Exact` (default) | `Newton-Raphson`

Specify the method for computing the reciprocal of a square root.

| Method | Data Types Supported | When to Use This Method |
| --- | --- | --- |
| `Exact` | Floating point | You do not want an approximation.  The input or output must be floating point. |
| `Newton-Raphson` | Floating-point, fixed-point, and built-in integer types | You want a fast, approximate calculation. |

The `Exact` method provides results that are
consistent with MATLAB computations.

#### Dependencies

To enable this parameter, set **Function** to
`rSqrt`.

When **Function** is set to
`sqrt` or
`signedSqrt`, this parameter is set to
`Exact`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AlgorithmType` |
| **Type**: character vector |
| **Values**: `'Exact'` | `'Newton-Raphson'` |
| **Default**: `'Exact'` |

### **Number of iterations** — Number of iterations used for Newton Raphson algorithm `3` (default) | integer

Specify the number of iterations to perform the Newton-Raphson
algorithm. This parameter is valid with the `rSqrt`
function and the `Newton-Raphson` value for
**Method**.

If you enter `0`, the block output is the initial
guess of the Newton-Raphson algorithm.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Iterations` |
| **Type**: character vector |
| **Values**: integer |
| **Default**: `'3'` |

### Data Types

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

### **Intermediate results data type** — Data type of intermediate results `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit from input` | `Inherit: Inherit from output` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for intermediate results when you set
**Function** to `sqrt` or
`rSqrt`.

The type can be inherited, specified directly, or expressed as a data
type object such as a `Simulink.NumericType`
object.

To avoid overflow, the intermediate data type must be larger than or
equal to a data type that can contain the square of the output data
type.

Follow these guidelines on setting an intermediate data type
explicitly for the square root function, `sqrt`:

| Input and Output Data Types | Intermediate Data Type |
| --- | --- |
| Input or output is double. | Use double. |
| Input or output is single, and any non-single data type is *not* double. | Use single or double. |
| Input and output are fixed point. | Use fixed point. |

Follow these guidelines on setting an intermediate data type
explicitly for the reciprocal square root function,
`rSqrt`:

| Input and Output Data Types | Intermediate Data Type |
| --- | --- |
| Input is double and output is not single. | Use double. |
| Input is not single and output is double. | Use double. |
| Input and output are fixed point. | Use fixed point. |

**Caution**

Do not set **Intermediate results data type** to
`Inherit: Inherit from output`
when:

- You select `Newton-Raphson` to
  compute the reciprocal of a square root.
- The input data type is floating point.
- The output data type is fixed point.

Under these conditions, selecting `Inherit: Inherit
from output` yields suboptimal performance and
produces an error.

To avoid this error, convert the input signal from a
floating-point to fixed-point data type. For example, insert a
Data Type Conversion
block in front of the Sqrt block to perform the
conversion.

#### Dependencies

To enable this parameter, set **Function** to
`sqrt` or
`rSqrt`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IntermediateResultsDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule'` | `'Inherit: Inherit from input'` | `'Inherit: Inherit from output'` | `'double'` | `'single'`, `'int8'`, `'uint8'`, `int16`, `'uint16'`, `'int32'`, `'uint32'`, `'int64'`, `'uint64'`, `fixdt(1,16,0)`, `fixdt(1,16,2^0,0)`. `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Output** — Output data type `Inherit: Same as first input` (default) | `Inherit: Inherit via internal rule` | `Inherit: Inherit via back propagation` | `double` | `single` | `half` | `int8` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,2^0,0)` | `<data type expression>` | ...

Specify the output data type. The type can be inherited, specified
directly, or expressed as a data type object such as a
`Simulink.NumericType` object.

#### Dependencies

When input is a floating-point data type smaller than single
precision, the `Inherit: Inherit via internal
rule` output data type depends on the setting of
the Inherit floating-point output type smaller than single precision configuration parameter. Data types are smaller than single
precision when the number of bits needed to encode the data type is
less than the 32 bits needed to encode the single-precision data
type. For example, `half` and
`int16` are smaller than single
precision.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `fixdt(1,16,2^0,0)` | `'<data type expression>'` |
| **Default**: `'Inherit: Same as first input'` |

### **Minimum** — Minimum output value for range checking `[]` (default) | scalar

Specify the lower value of the output range that the software checks
as a finite, real, double, scalar value.

If you specify a bus object as the data type for this block, do not
set the minimum value for bus data on the block. The software ignores
this setting. Instead, set the minimum values for bus elements of the
bus object specified as the data type. For more information, see `Simulink.BusElement`.

The software uses the minimum to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters) for some
  blocks.
- Simulation range checking (see Specify Signal Ranges and Enable Simulation Range Checking).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model.
  This optimization can remove algorithmic code and affect the
  results of some simulation modes such as SIL or external
  mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output minimum** does not saturate or clip the
actual output signal. Use the Saturation block
instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMin` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'[]'` |

### **Maximum** — Maximum output value for range checking `[]` (default) | scalar

Specify the upper value of the output range that the software checks
as a finite, real, double, scalar value.

If you specify a bus object as the data type for this block, do not
set the maximum value for bus data on the block. The software ignores
this setting. Instead, set the maximum values for bus elements of the
bus object specified as the data type. For more information, see `Simulink.BusElement`.

The software uses the maximum value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters) for some
  blocks.
- Simulation range checking (see Specify Signal Ranges and Enable Simulation Range Checking).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model.
  This optimization can remove algorithmic code and affect the
  results of some simulation modes such as SIL or external
  mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output maximum** does not saturate or clip the
actual output signal. Use the Saturation block
instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMax` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'[]'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations.
For more information, see Rounding Modes (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **Default:** `'Floor'` |

### **Lock output data type setting against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select to lock the output data type setting of this block against changes
by the Fixed-Point Tool and the Fixed-Point Advisor. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LockScale` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Saturate on integer overflow** — Method of overflow action `on` (default) | `off`

Specify whether overflows saturate or wrap.

- `on` — Overflows saturate to either the minimum or maximum
  value that the data type can represent.
- `off` — Overflows wrap to the appropriate value that the data
  type can represent.

For example, the maximum value that the signed 8-bit integer `int8`
can represent is 127. Any block operation result greater than this maximum value causes
overflow of the 8-bit integer.

- With this parameter selected, the block output saturates at 127.
  Similarly, the block output saturates at a minimum output value of
  -128.
- With this parameter cleared, the software interprets the overflow-causing
  value as `int8`, which can produce an unintended result.
  For example, a block result of 130 (binary 1000 0010) expressed as
  `int8` is -126.

#### Tips

- Consider selecting this parameter when your model has a possible overflow
  and you want explicit saturation protection in the generated code.
- Consider clearing this parameter when you want to optimize efficiency of
  your generated code. Clearing this parameter also helps you to avoid
  overspecifying how a block handles out-of-range signals. For more
  information, see Troubleshoot Signal Range Errors.
- When you select this parameter, saturation applies to every internal
  operation on the block, not just the output or result.
- In general, the code generation process can detect when overflow is not
  possible. In this case, the code generator does not produce saturation
  code.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **Values:** | `'on'` (default) | `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architectures**

| Function | Architecture | Description |
| --- | --- | --- |
| `sqrt`  `signedSqrt`  `rSqrt` | `SqrtFunction` (default) | Compute the square root by using a pipelined shift-addition algorithm or multiplication-based algorithm. The `sqrtfunction` architecture supports code generation for fixed-point types and floating-point types. When you use floating-point types, select **Use Floating Point** configuration parameter. You can specify the **LatencyStrategy** and **CustomLatency** HDL properties to choose from a range of frequency values when targeting your design on the hardware platform.  Use the **UseMultiplier** HDL block property in combination with the **LatencyStrategy** and **CustomLatency** properties to specify whether to compute the square root by using a pipelined shift and add or multiplication algorithm. Improve design frequency and reduce resource utilization by setting the **UseMultiplier** to `off` and **LatencyStrategy** to `inherit`. |
| `sqrt` | `SqrtNewton` | Use the iterative Newton method to optimize area. |
| `sqrt` | `SqrtNewtonSingleRate` | Use the single rate pipelined Newton method. Select this option to optimize speed, or if you want a single rate implementation. |
| `rSqrt` | `RecipSqrtNewton` | Use the iterative Newton method to optimize area.  To specify this architecture, set **Method** to `Newton-Raphson`. |
| `rSqrt` | `RecipSqrtNewtonSingleRate` | Use the single rate pipelined Newton method. Select this option to optimize speed, or if you want a single rate implementation.  To specify this architecture, set **Method** to `Newton-Raphson`. |

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **Iterations** | Number of iterations for `SqrtNewton` or `SqrtNewtonSingleRate` implementation. |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **UseMultiplier** | Select algorithm for `SqrtFunction` implementation. By default, this property is set to `off`, and the block computes square root by using the shift-add algorithm. When the property is set to `on`, the square root is computed by using multipliers.  Increase design frequency and reduce resource utilization by setting the **UseMultiplier** to `off` and **LatencyStrategy** to `inherit`. |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `MAX`, `MIN`, `CUSTOM`, or `ZERO` latency for fixed-point and floating-point types. The default is `MAX`. The block settings for floating-point types overrides the model-level settings. For fixed-point types, the block-level setting determines the latency strategy. See also LatencyStrategy (HDL Coder).  Increase design frequency and reduce resource utilization by setting the **UseMultiplier** to `off` and **LatencyStrategy** to `inherit`.  You can control the pipeline stages for the iterative algorithm by setting the **LatencyStrategy** to `Custom(PerIterations)`. For more information, see Sqrt (HDL Coder). |
| **CustomLatency** | When **LatencyStrategy** is set to `CUSTOM` and if you use fixed-point types, use this property to specify a custom latency value between `ZERO` and `MAX` for fixed-point types. For floating-point types, this value becomes the custom latency of the operator. See also NFPCustomLatency (HDL Coder). |
| **IterationsPerPipeline** | When you set **LatencyStrategy** to `Custom(PerIterations)`, use this setting to specify the number of iterations per pipeline stages. To enable this property, set HDL architecture to `SqrtFunction`.  For more information, see Sqrt (HDL Coder). |

| Native Floating Point | |
| --- | --- |
| **HandleDenormals** | Specify whether you want HDL Coder to insert additional logic to handle denormal numbers in your design. Denormal numbers are numbers that have magnitudes less than the smallest floating-point number that can be represented without leading zeros in the mantissa. The default is `inherit`. See also HandleDenormals (HDL Coder). |

**Data Type Support**

The block supports these data types for HDL code generation:

| Input Port | Dimension | Fixed-Point | Floating-Point | Built-in Integers | Bus | Boolean | Complex Signal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | Scalar  Vector  Matrix (up to 2-D) | Yes | Single  Double | Yes | Yes | No | No |

**Latency Details**

This block has multi-cycle implementations that introduce additional
latency in the generated code. To see the added latency, view the
generated model or validation model. See Generated Model and Validation Model (HDL Coder).

**Floating-Point Latency**

| Architecture | Floating-Point Type | Latency Strategy | Latency (in cycles) | Custom Latency Support |
| --- | --- | --- | --- | --- |
| `SqrtFunction` | Single | Min | 16 | Yes |
| Max | 28 |
| Double | Min | 33 |
| Max | 58 |

**Fixed-Point Latency**

| Architecture | Maximum Latency (in cycles) | Description | Latency Strategy Support | Custom Latency Support |
| --- | --- | --- | --- | --- |
| `SqrtFunction` | To calculate the latency for fixed-point data types, see *Algorithm* in Sqrt (HDL Coder). | The maximum latency is determined by the output word length, and input and output fraction lengths, for fixed-point data. | Yes | Yes |
| `SqrtNewton` | **Iterations** + 3 | The default value for **Iterations** HDL block property is 3.  The recommended value for **Iterations** is from 2 through 10. If **Iterations** is outside the recommended range, HDL Coder generates a message. | No | No |
| `SqrtNewtonSingleRate` | (**Iterations**\* 4) + 6 |
| `RecipSqrtNewton` | **Number of iterations** + 2 | The default value for **Number of iterations** block parameter is 3.  The recommended value for **Number of iterations** is from 2 through 10. If **Number of iterations** is outside the recommended range, HDL Coder generates a message. |
| `RecipSqrtNewtonSingleRate` | (**Number of iterations**\* 4) + 5 |

**Block Parameter Configuration**

These block parameter configurations are incompatible with HDL code
generation.

| Block Parameter | Limitations and Considerations |
| --- | --- |
| **Output Signal Type** | Parameter value `Complex` is not supported. |
| **Method** | When you set **Function** parameter to `rSqrt`, use `Exact` for floating-point data types and `Newton Raphson` for fixed-point data types. |
| **Intermediate results data type** | Parameter value other than `Inherit: Inherit via internal rule` is not supported |
| **Output** | Choose an output port data type that is same as the input. |
| **Integer rounding mode** | Parameter value `Convergent`, `Round` is not supported for fixed-point types. |

**Optimizations**

You can use these HDL Coder optimizations to optimize the speed, area, and
I/Os.

**Area Optimization**

| Optimization | Description |
| --- | --- |
| Resource Sharing (HDL Coder) | *Resource sharing* is an area optimization in which HDL Coder identifies multiple functionally equivalent resources and replaces them with a single resource. |
| Streaming (HDL Coder) | *Streaming* is an area optimization in which HDL Coder transforms a vector data path to a scalar data path (or to several smaller-sized vector data paths). |

**Speed Optimization**

| Optimization | Description |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *Distributed pipelining*, or register retiming, is a speed optimization that moves existing delays in a design to reduce the critical path while preserving functional behavior.  For the Sqrt block, HDL Coder distributes pipeline registers around the blocks instead of within them. |
| Clock-Rate Pipelining (HDL Coder) | *Clock-rate pipelining* is an optimization framework in HDL Coder that allows other speed and area optimizations to introduce latency at the clock rate. |
| Critical Path Estimation (HDL Coder) | To quickly identify the most likely critical path in your design, use *Critical Path Estimation*. Critical path estimation speeds up the iterative process of finding the critical path. To know blocks that are characterized in critical path estimation, see Characterized Blocks (HDL Coder). |

**I/O Optimization**

| Optimization | Description |
| --- | --- |
| Frame to Sample Conversion (HDL Coder) | To optimize the I/O needed for your design, use frame-to-sample conversion. This optimization converts frame-based vector or matrix inputs to smaller-sized samples or pixels for HDL code generation to target stream-based hardware and reduce the FPGA I/O needed to handle large input and output signals. |

**HDL Algorithm**

HDL Coder implements reciprocal square-root operation in
`ReciprocalRsqrtBasedNewton` and
`ReciprocalRsqrtBasedNewtonSingleRate` architecture
by using Newton-Raphson iterative method, which is given by the equation:

xi+1=xi−f(xi)f'(xi)=xi(1.5−0.5axi2)

f(x)=1x2−1

**Restrictions**

Newton-Raphson-based implementation is incompatible with HDL code generation
in native floating-point mode. To generate HDL code in native floating-point
mode, select the `SqrtFunction` architecture in the HDL
Block properties.

**HDL Modeling Guideline**

Use SqrtFunction Architecture for Square Root Block (HDL Coder)

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2010a**
