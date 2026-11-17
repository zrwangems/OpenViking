---
type: simulink-block
title: 'Trigonometric Function'
family: 'libsb2sl'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'TRG'
documentation_page: 'trigonometricfunction'
documentation_source_path: 'slref/trigonometricfunction.html'
language: zh-CN
chinese_source: worker-translation
---

# Trigonometric Function

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入指定为标量、向量或矩阵。该模块接受以下数据类型的输入信号：

| 函数 | 输入数据类型 |
| --- | --- |
| - `sin` - `cos` - `sincos` - `cos + jsin` - `atan2` | - 浮点 - 定点（仅当 **Approximation method** 为 `CORDIC` 或 `Lookup` 时） |
| - `tan` - `asin` - `acos` - `atan` - `sinh` - `cosh` - `tanh` - `asinh` - `acosh` - `atanh` | - 浮点 |

CORDIC 近似的定点类型传播：

| 输入数据类型 | 函数 | 输出数据类型 |
| --- | --- | --- |
| 定点，有符号或无符号 | `sin`、`cos`、`sincos` 和 `cos + jsin` | `fixdt``(1, WL, WL - 2)`，其中 *`WL`* 是输入字长 此定点类型为 CORDIC 算法提供最佳精度。 |
| 定点，有符号 | `atan2` | `fixdt``(1, WL, WL – 3)` |
| 定点，无符号 | `atan2` | `fixdt``(1, WL, WL – 2)` |

查找近似的定点类型传播：

| 输入数据类型 | 函数 | 输出数据类型 |
| --- | --- | --- |
| 定点，有符号 | `sin`、`cos`、`sincos`、`cos + jsin`、`atan2` | `fixdt``(1, WL, FL)` |
| 定点，无符号 | `sin`、`cos`、`sincos`、`cos + jsin`、`atan2` | `fixdt``(1, WL - 1, FL)` |

#### 依赖关系

- 当您将 **Function** 设置为 `atan2` 时，该模块显示两个输入端口。第一个输入（**Port\_1**）是函数参数的 *y* 轴或虚部。第二个输入（**Port\_2**）是函数参数的 *x* 轴或实部。
- 当您将 **Approximation method** 设置为 `None`、`CORDIC` 或 `Lookup` 时，可以使用浮点输入信号。但是，模块输出数据类型取决于您选择这些近似方法选项中的哪一个。

  | 输入数据类型 | 近似方法 | 输出数据类型 |
  | --- | --- | --- |
  | 浮点 | `None` | 取决于您对 **Output signal type** 的选择。选项为 `auto`（与输入相同的数据类型）、`real` 或 `complex`。 |
  | 浮点 | `CORDIC` | 与输入相同。当您使用 CORDIC 近似方法计算模块输出时，**Output signal type** 不可用。 |
  | 浮点 | `Lookup` | 与输入相同。当您使用 Lookup 近似方法计算模块输出时，**Output signal type** 不可用。 |

对于 CORDIC 和 Lookup 近似：

- 对于 `sin`、`cos`、`sincos`、`cos + jsin` 和 `atan2` 函数，输入必须为实数。
- 对于 `sin`、`cos`、`sincos` 和 `atan2` 函数，输出为实数。
- 对于 `cos + jsin` 函数，输出为复数。

有关详细信息，请参阅限制。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_2** — `atan2` 的函数参数的 *x* 轴或实部 标量 | 向量 | 矩阵

输入 `atan2` 的函数参数的 *x* 轴或实部。当您将 **Function** 设置为 `atan2` 时，该模块显示两个输入端口。第一个输入（**Port\_1**）是函数参数的 *y* 轴或虚部。第二个输入（**Port\_2**）是函数参数的 *x* 轴或实部。（有关各种模块方向的端口顺序说明，请参阅识别旋转或翻转模块上的端口位置。）

仅当您将 **Approximation** 方法设置为 `CORDIC` 或 `Lookup` 时，才支持定点输入信号。

#### 依赖关系

要启用此端口，请将 **Function** 设置为 `atan2`。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输入的指定三角函数 标量 | 向量 | 矩阵

将一个或多个输入（以 rad 为单位）应用于指定三角函数的结果。每个函数支持：

- 标量运算
- 逐元素的向量和矩阵运算

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **sin** — 输入信号的正弦 标量 | 向量 | 矩阵

输入信号的正弦，以 rad 和 rev 为单位。

#### 依赖关系

要启用此端口，请将 **Function** 设置为 `sincos`。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **cos** — 输入信号的余弦 标量 | 向量 | 矩阵

输入信号的余弦，以 rad 和 rev 为单位。

#### 依赖关系

要启用此端口，请将 **Function** 设置为 `sincos`。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### 算法

### **Function** — 三角函数 `sin`（默认） | `cos` | `tan` | `asin` | `acos` | `atan` | `atan2` | `sinh` | `cosh` | `tanh` | `asinh` | `acosh` | `atanh` | `sincos` | `cos + jsin`

指定三角函数。模块图标上的函数名称会更改以匹配您的选择。

有关何时将 **Function** 设置为 `sin`、`cos`、`sincos` 或 `cos + jsin` 并将 **Approximation method** 设置为 `CORDIC` 的详细信息，请参阅限制。

#### 编程用法

|  |
| --- |
| **模块参数：** `Operator` |
| **类型：** 字符向量 |
| **值：** `'sin' | 'cos' | 'tan' | 'asin' | 'acos' | 'atan' | 'atan2' | 'sinh' | 'cosh' | 'tanh' | 'asinh' | 'acosh' | 'atanh' | 'sincos' | 'cos + jsin'` |
| **默认值：** `'sin'` |

### **Approximation method** — CORDIC、Lookup 或无 `None`（默认） | `CORDIC` | `Lookup`

指定用于计算输出的近似类型。

| 近似方法 | 支持的数据类型 | 何时使用此方法 |
| --- | --- | --- |
| `None`（默认） | 浮点 | 您想要使用默认的泰勒级数算法。 |
| `CORDIC` | 浮点和定点 | 您想要快速、近似的迭代计算。 |
| `Lookup` | 浮点（double 和 single）以及 **Bias** 值为 `0` 且 **Slope** 值为 2 的幂的定点 | 您想要快速、近似的查找表实现。 |

有关何时将 **Function** 设置为 `sin`、`cos`、`sincos` 或 `cos + jsin` 并将 **Approximation method** 设置为 `CORDIC` 的详细信息，请参阅限制。

#### 依赖关系

- 要启用此参数，请将 **Function** 设置为 `sin`、`cos`、`sincos`、`cos + jsin` 或 `atan2`。
- 要使用定点输入信号，您必须将 **Approximation method** 设置为 `CORDIC` 或 `Lookup`。
- 要启用 **Table data type** 参数，请将此方法设置为 `Lookup`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ApproximationMethod` |
| **类型：** 字符向量 |
| **值：** `'None' | 'CORDIC' | 'Lookup'` |
| **默认值：** `'None'` |

### **Interpolation method** — 断点值之间的插值方法 `Linear point-slope`（默认） | `Flat`

当输入落在断点值之间时，该模块使用相邻断点对输出值进行插值。有关插值方法的详细信息，请参阅插值方法。

#### 编程用法

|  |
| --- |
| **模块参数：** `InterpMethod` |
| **类型：** 字符向量 |
| **值：** `'Linear point-slope' | 'Flat'` |
| **默认值：** `'Linear point-slope'` |

### **Number of iterations** — CORDIC 算法的迭代次数 `11`（默认） | 小于或等于定点输入字长的正整数

指定执行 CORDIC 算法的迭代次数。默认值为 11。

- 当模块输入使用浮点数据类型时，迭代次数可以是正整数。
- 当模块输入为定点数据类型时，迭代次数不能超过字长。

  例如，如果模块输入为 `fixdt(1,16,15)`，则字长为 16。在这种情况下，迭代次数不能超过 16。

#### 依赖关系

要启用此参数，您必须按如下方式设置 **Function** 和 **Approximation method** 参数：

- 将 **Function** 设置为 `sin`、`cos`、`sincos`、`cos + jsin` 或 `atan2`。
- 将 **Approximation method** 设置为 `CORDIC`。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumberOfIterations` |
| **类型：** 字符向量 |
| **值：** 小于或等于定点输入字长的正整数 |
| **默认值：** `'11'` |

### **Angle unit** — 角度单位 `radian`（默认） | `revolution`

将查找方法的角度单位指定为 `radian` 或 `revolution`。

#### 依赖关系

要启用此参数：

- 将 **Function** 设置为 `sin`、`cos`、`sincos`、`cos + jsin` 或 `atan2`。
- 将 **Approximation method** 设置为 `Lookup`。

#### 编程用法

|  |
| --- |
| **模块参数：** `AngleUnit` |
| **类型：** 字符向量 |
| **值：** `'radian' | 'revolution'` |
| **默认值：** `'radian'` |

### **Number of data points** — 查找表的数据点数 `16`（默认） | 标量

将查找表的数据点数指定为标量实数。

#### 依赖关系

要启用此参数：

- 将 **Function** 设置为 `sin`、`cos`、`sincos`、`cos + jsin` 或 `atan2`。
- 将 **Approximation method** 设置为 `Lookup`。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumberOfDataPoints` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认值：** `'16'` |

### **Output signal type** — 输出信号的复/实性 `auto`（默认） | `real` | `complex`

将 Trigonometric Function 模块的输出信号类型指定为 `auto`、`real` 或 `complex`。

| 函数 | 输入信号类型 | 输出信号类型 | | |
| --- | --- | --- | --- | --- |
| Auto | Real | Complex |
| **Function** 参数的任意选择 | real | real | real | complex |
| complex | complex | error | complex |

#### 依赖关系

将 **Approximation method** 设置为 `CORDIC` 会禁用此参数。

**注意**

当 **Function** 为 `atan2` 时，仿真或代码生成不支持复数输入信号。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputSignalType` |
| **类型：** 字符向量 |
| **值：** `'auto' | 'real' | 'complex'` |
| **默认值：** `'auto'` |

### **Remove protection against out-of-range input** — 移除对超出范围输入的保护 off（默认） | on

对于 `acos` 和 `asin`，选中此复选框可移除对超出范围输入的保护，从而减少冗余。

- 当您清除此复选框时，保护处于启用状态。该模块在执行任何操作之前将超出范围的输入饱和为 `1` 或 `-1`。生成的代码包含用于检查超出范围输入的代码。
- 当您选中此复选框时，保护被移除。该模块对输入值执行所有操作而不做任何更改。生成的代码不包含用于检查超出范围输入的代码。

如果输入已在范围内，启用此复选框可以消除冗余。

#### 依赖关系

将 **Function** 设置为 `acos` 和 `asin` 会启用此参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `RemoveProtectionAgainstOutOfRangeInput` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认） | 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

#### 依赖关系

仅当您将其设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅不建议使用采样时间的模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认） | 带引号的标量或向量 |

### 数据类型

### **Table data type** — 表的数据类型 `Inherit: Inherit via input`（默认） | `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

查找表的数据类型，指定为：

- `Inherit: Inherit via input`
- `double`
- `single`
- `fixdt(1,16,0)`
- `<data type expression>`

有关设置数据类型的详细信息，请参阅控制信号的数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `TableDataTypeStr` |
| **类型：** 字符串标量或字符向量 |
| **值：** `Inherit: Inherit via input` | `single` | `double` | `fixdt(1,16,0)` | 数据类型表达式 |
| **默认值：** `Inherit: Inherit via input` |

### **Mode** — 要指定的数据类别 `Inherit`（默认） | `Built in` | `Fixed point` | `Expression`

选择您希望如何指定 **Output** 数据类型的数据类型属性。您可以选择：

- `Inherit` — 允许您指定继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- `Built in`— 允许您指定内置数据类型。
- `Fixed point` — 允许您指定数据类型的定点属性。
- `Expression` — 允许您指定一个求值为有效数据类型的表达式，例如 `fixdt([],16,0)`

#### 依赖关系

要启用此参数，请单击 **Output data type** 参数处的 **>>**。

### **Signedness** — 指定有符号或无符号 `Signed`（默认） | `Unsigned`

指定 **Output** 数据类型的 **Signedness**。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Scaling** — 定点数据的定标方法 `Binary point`（默认）

指定 **Output** 数据类型的 **Scaling**。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Data type override** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

选择此信号的数据类型覆盖模式。

- `Inherit` — 继承为模型指定的数据类型覆盖设置。
- `Off` — 忽略为模型指定的数据类型覆盖设置，并使用您指定的定点数据类型

有关详细信息，请参阅 Simulink® 文档中的使用数据类型助手指定数据类型。

#### 提示

为单个数据类型关闭数据类型覆盖的能力，使您可以在应用数据类型覆盖时更好地控制模型中的数据类型。例如，您可以使用此选项确保数据类型满足下游模块的要求，而不管数据类型覆盖设置如何。

#### 依赖关系

要启用此参数，请单击 **Show data type assistant** 按钮，并将 **Mode** 设置为 `Built in` 或 `Fixed point`。

### **Word length** — 保存量化整数的字的位大小 `16`（默认） | 从 0 到 32 的整数

指定保存量化整数的字的位大小。有关详细信息，请参阅指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Fraction length** — 指定定点数据类型的小数长度 `0`（默认） | 标量整数

将定点数据类型的小数长度指定为正整数或负整数。有关详细信息，请参阅指定定点数据类型。

#### 依赖关系

要启用此参数，请设置：

- **Mode** 为 `Fixed point`
- **Scaling** 为 `Binary point`

## 所属库

Simulink / Math Operations HDL Coder / Math Operations HDL Coder / HDL Floating Point Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed pointa` | `half` | `integera` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 此模块支持 'Approximation method' 为 CORDIC 时的定点和基本整数数据类型。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

并非所有编译器都支持 `asinh`、`acosh` 和 `atanh` 函数。如果使用的编译器不支持这些函数，则会出现警告，并且生成的代码无法链接。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

要从使用定点数据的模块生成 HDL 代码，请将 **Architecture** 设置为 `Cordic` 或 `LUT`。下表显示了模块在这些设置下支持的函数：

| 模块参数 | HDL 模块属性 | 支持的函数 |
| --- | --- | --- |
| 将 **Approximation method** 设置为 `CORDIC`，**Number of data Points** 设置为任意标量实数。 | 将 **Architecture** 设置为 `Cordic`。 | - `sin` - `cos` - `sincos` - `cos+jsin` - `atan2` |
| 将 **Approximation method** 设置为 `Lookup`，**Interpolation method** 设置为 `Flat`，**Angle Unit** 设置为 `revolution`，**Number of data Points** 设置为任意标量实数。 | 将 **Architecture** 设置为 `LUT`。 | - `sin` - `cos` - `sincos` - `cos+jsin` |

要为使用浮点数据的模块的所有函数生成 HDL 代码，请将 **Approximation method** 模块参数设置为 `none`，并将 **Output signal type** 参数设置为 `auto` 或 `real` 或 `complex`。此外，将 HDL 模块属性中的 **Architecture** 参数设置为 `Trigonometric`。

此模块具有多周期实现，会在生成的代码中引入额外延迟。要查看增加的延迟，请查看生成的模型或验证模型。请参阅 Generated Model and Validation Model (HDL Coder)。

延迟计算取决于字长和 **LatencyStrategy** 设置。要查看定点数据类型的延迟计算，请参阅：

- Sin (HDL Coder)
- Cos (HDL Coder)
- Cos+jSin (HDL Coder)
- SinCos (HDL Coder)
- Atan2 (HDL Coder)

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **LatencyStrategy** | 要为定点类型启用此属性，请将 **Function** 设置为 `sin`、`cos`、`sincos`、`cos+jsin` 或 `atan2`，并将 **Approximation method** 设置为 `CORDIC`。指定是将设计中的模块映射为定点类型和浮点类型的 `MAX`、`Min`、`CUSTOM` 还是 `ZERO` 延迟。默认值为 `MAX`。另请参阅 LatencyStrategy (HDL Coder)。 |
| **CustomLatency** | 要为定点类型启用此属性，请将 **Function** 设置为 `sin`、`cos`、`sincos`、`cos+jsin` 或 `atan2`，并将 **Approximation method** 设置为 `CORDIC`。当 **LatencyStrategy** 设置为 `CUSTOM` 时，使用此属性为定点类型指定介于 `ZERO` 和 `MAX` 之间的自定义延迟值。另请参阅 LatencyStrategy (HDL Coder)。 |
| **IterationsPerPipeline** | 要为定点类型启用此属性，请将 **Function** 设置为 `sin`、`cos`、`sincos`、`cos+jsin` 或 `atan2`，并将 **Approximation method** 设置为 `CORDIC`。当将 **LatencyStrategy** 设置为 `Custom(PerIterations)` 时，使用此设置指定每个流水线级的迭代次数。有关更多信息，请参阅 Atan2 (HDL Coder)。 |

| 本机浮点 | |
| --- | --- |
| **InputRangeReduction** | 将此属性用于 `sin`、`cos`、`sincos`、`cos+jsin` 和 `atan2` 函数。如果输入范围无界，请启用此属性，以便 HDL Coder 插入额外逻辑将输入范围缩减到 `[-pi, pi]`。另请参阅 InputRangeReduction (HDL Coder)。 |
| **HandleDenormals** | 指定是否希望 HDL Coder 插入额外逻辑来处理设计中的非规格化数。非规格化数是幅值小于尾数中没有前导零时可表示的最小浮点数的数。默认值为 `inherit`。另请参阅 HandleDenormals (HDL Coder)。 |
| **LatencyStrategy** | 指定是将设计中的模块映射为浮点运算符的 `inherit`、`Max`、`Min` 还是 `Zero`。默认值为 `inherit`。另请参阅 LatencyStrategy (HDL Coder)。 |
| **MultiplyStrategy** | 将此属性用于 `sin`、`cos`、`sincos`、`cos+jsin` 和 `atan2` 函数。默认值为 `inherit`。指定要使用 `FullMultiplier` 还是 `PartMultiplierPartAddShift`。另请参阅 MantissaMultiplyStrategy (HDL Coder)。 |

**ULP 注意事项**

Trigonometric Function 模块在浮点运算中具有非零的最低有效位 (ULP) 误差。有关更多信息，请参阅 ULP Considerations of Native Floating-Point Operators (HDL Coder)。

**限制**

- 对于 `sin` 和 `cos` 函数，模块仅支持用于 CORDIC 逼近的有符号定点数据类型。
- 对于具有 CORDIC 模式的函数，例如 `sin`、`cos`、`sincos`、`atan2` 和 `cos+jsin`，HDL 代码生成不支持大于 `127` 位的定点数据类型。
- HDL 代码生成不支持三角函数中的双精度数据类型，`sin` 和 `cos` 函数除外。
- HDL 代码生成在以下情况下不支持查找逼近方法：

  - **Interpolation method** 参数设置为 `Linear point-slope`，且 **Angle Unit** 参数设置为 `radian` 或 `revolution`。
  - **Interpolation method** 参数为 `Flat`，且 **Angle Unit** 参数为 `radian`。
- 当 Trigonometric Function 模块位于反馈环路内且设置了以下内容时，HDL Coder 会显示错误：

  - **Architecture** 设置为 `Cordic`
  - **UsePipelinedKernel** 设置为 `On`

  出现该错误是因为模块位于反馈环路中，代码生成器无法插入额外延迟。要避免此错误，请在模块相邻位置添加一个长度等于 **Number of iterations** 加 3 的延迟。然后代码生成器会吸收此延迟以满足 Trigonometric Function 模块的额外延迟。

  例如，此 Trigonometric Function 模块的 **Number of iterations** 设置为 `30`。在模块相邻位置添加长度为 `33` 的 Delay 模块即可满足额外延迟。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

当将 **Function** 设置为 `sin`、`cos`、`sincos`、`cos + jsin` 或 `atan2`，并将 **Approximation method** 设置为 `CORDIC` 时，此模块支持定点和基整数数据类型。

## 版本历史

**在 R2006a 之前引入**

## 描述

对输入执行指定的三角函数

Trigonometric Function 模块执行常见三角函数并以 rad 或 rev 输出结果。

### 支持的函数

可以从 **Function** 参数列表中选择以下函数之一。

| 函数 | 描述 | 数学表达式 | MATLAB® 等效函数 |
| --- | --- | --- | --- |
| `sin` | 输入的正弦 | `sin(u)` | `sin` |
| `cos` | 输入的余弦 | `cos(u)` | `cos` |
| `tan` | 输入的正切 | `tan(u)` | `tan` |
| `asin` | 输入的反正弦 | `asin(u)` | `asin` |
| `acos` | 输入的反余弦 | `acos(u)` | `acos` |
| `atan` | 输入的反正切 | `atan(u)` | `atan` |
| `atan2` | 输入的四象限反正切 | `atan2(u)` | `atan2` |
| `sinh` | 输入的双曲正弦 | `sinh(u)` | `sinh` |
| `cosh` | 输入的双曲余弦 | `cosh(u)` | `cosh` |
| `tanh` | 输入的双曲正切 | `tanh(u)` | `tanh` |
| `asinh` | 输入的反双曲正弦 | `asinh(u)` | `asinh` |
| `acosh` | 输入的反双曲余弦 | `acosh(u)` | `acosh` |
| `atanh` | 输入的反双曲正切 | `atanh(u)` | `atanh` |
| `sincos` | 输入的正弦；输入的余弦 | — | — |
| `cos + jsin` | 输入的复指数 | — | — |

### CORDIC 逼近方法

CORDIC 是 COordinate Rotation DIgital Computer（坐标旋转数字计算机）的缩写。基于 Givens 旋转的 CORDIC 算法是可用的硬件效率最高的算法之一，因为它只需要迭代移位加法运算。有关更多信息，请参阅更多信息。模块输入有进一步要求。

有关将 **Function** 设置为 `sin`、`cos`、`sincos` 或 `cos + jsin` 并将 **Approximation method** 设置为 `CORDIC` 时的更多信息，请参阅 Port\_1。

下表总结了无效输入的情况。

| 模块使用 | 无效输入的影响 |
| --- | --- |
| 仿真模式 | 出现错误。 |
| 生成的代码 | 出现未定义行为。避免依赖生成代码的未定义行为。 |

### 查找逼近方法

有关将 **Function** 设置为 `sin`、`cos`、`sincos` 或 `cos + jsin` 并将 **Approximation method** 设置为 `Lookup` 时的更多信息，请参阅 Port\_1。
