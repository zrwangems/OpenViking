---
type: simulink-block
title: 'Data Type Conversion'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Commonly Used Blocks'
documentation_page: 'datatypeconversion'
documentation_source_path: '../simulink/slref/datatypeconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Data Type Conversion

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

输入信号，指定为标量、向量、矩阵或 N 维数组。输入可以是任何实值或复值信号。如果输入为实数，则输出为实数。如果输入为复数，则输出为复数。该模块将输入信号转换为您指定的 **Output data type**。

当您转换定点数据类型时，使用 **Input and output to have equal** 参数来确定转换是基于信号的 `Real World Value (RWV)` 还是 `Stored Integer (SI)` 值进行。有关详细信息，请参阅 Convert Fixed-Point Signals。

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵 | N 维数组

输出信号，转换为您指定的数据类型，其维度与输入信号相同。

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

## 参数

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的下限值。

软件使用最小值来执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）以用于某些模块。
- 仿真范围检查（请参阅 Specify Signal Ranges 和 Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

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

软件使用最大值来执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）以用于某些模块。
- 仿真范围检查（请参阅 Specify Signal Ranges 和 Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **值**：| `'[]'`（默认）| 带引号的标量 |

### **Output data type** — 输出数据类型 `Inherit: Inherit via back propagation`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

选择输出的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'Enum: <class name>'` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via back propagation'` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖 Output data type 的选项 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块上指定的 **Output** 数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `LockScale` |
| **值**：| `'off'`（默认）| `'on'` |

### **Input and output to have equal** — 转换定点数据类型的约束 `Real World Value (RWV)`（默认）| `Stored Integer (SI)`

在定点数据表示的上下文中，指定输入和输出中必须相等的类型。

- `Real World Value (RWV)` — 指定使输入的 `Real World Value (RWV)` 等于输出的 `Real World Value (RWV)` 的目标。
- `Stored Integer (SI)` — 指定使输入的 `Stored Integer (SI)` 值等于输出的 `Stored Integer (SI)` 值的目标。

#### 编程使用

|  |
| --- |
| **模块参数**：`ConvertRealWorld` |
| **类型**：字符向量 |
| **值**：`'Real World Value (RWV)' | 'Stored Integer (SI)'` |
| **默认值**：`'Real World Value (RWV)'` |

### **Integer rounding mode** — 指定定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择以下舍入模式之一。

`Ceiling`
:   将正数和负数都向正无穷方向舍入。等效于 MATLAB® 的 `ceil` 函数。

`Convergent`
:   将数字舍入到最接近的可表示值。如果出现平局，则舍入到最接近的偶数整数。等效于 Fixed-Point Designer™ 的 `convergent` 函数。

`Floor`
:   将正数和负数都向负无穷方向舍入。等效于 MATLAB 的 `floor` 函数。

`Nearest`
:   将数字舍入到最接近的可表示值。如果出现平局，则向正无穷方向舍入。等效于 Fixed-Point Designer 的 `nearest` 函数。

`Round`
:   将数字舍入到最接近的可表示值。如果出现平局，则将正数向正无穷方向舍入，将负数向负无穷方向舍入。等效于 Fixed-Point Designer 的 `round` 函数。

`Simplest`
:   自动在向 floor 舍入和向零舍入之间进行选择，以生成尽可能高效的舍入代码。

`Zero`
:   将数字向零方向舍入。等效于 MATLAB 的 `fix` 函数。

#### 编程使用

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：字符向量 |
| **值**：`'Ceiling'` | `'Convergent'` | `'Floor'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |
| **默认值**：`'Floor'` |

#### 另请参阅

有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出时是饱和还是回绕。

- `on` — 溢出饱和到数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到数据类型可以表示的相应值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出饱和于 127。类似地，模块输出饱和于最小输出值 -128。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 -126。

#### 提示

- 当您的模型可能存在溢出并且您希望在生成的代码中显式提供饱和保护时，请考虑选择此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors。
- 当您选择此参数时，饱和适用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **值**：| `'off'`（默认）| `'on'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **值**：| `"-1"`（默认）| 带引号的标量或向量 |

### **Mode** — 选择数据类型模式 `Inherit`（默认）| `Built in` | `Fixed Point`

选择要指定的数据类别。

- `Inherit` — 数据类型的继承规则。选择 `Inherit` 会启用右侧的第二个菜单/文本框，您可以在其中选择继承模式。
- `Built in` — 内置数据类型。选择 `Built in` 会启用右侧的第二个菜单/文本框，您可以在其中选择内置数据类型。
- `Fixed point` — 定点数据类型。选择 `Fixed point` 会启用附加参数，您可以使用这些参数指定定点数据类型。
- `Expression` — 求值为数据类型的表达式。选择 `Expression` 会启用右侧的第二个菜单/文本框，您可以在其中输入表达式。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请点击 **Show data type assistant** 按钮。

### **Data type override** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

选择此信号的数据类型覆盖模式。

- 当您选择 `Inherit` 时，Simulink 从其上下文中继承数据类型覆盖设置，即从使用该信号的模块、`Simulink.Signal` 对象或 Simulink 中的 Stateflow® 图继承。
- 当您选择 `Off` 时，Simulink 忽略其上下文的数据类型覆盖设置，并使用为信号指定的定点数据类型。

有关详细信息，请参阅 Simulink 文档中的 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Built in` 或 `Fixed point`。

#### 提示

为单个数据类型关闭数据类型覆盖的能力，使您可以在应用数据类型覆盖时对模型中的数据类型进行更好的控制。例如，您可以使用此选项来确保数据类型满足下游模块的要求，而不管数据类型覆盖设置如何。

### **Signedness** — 指定有符号或无符号 `Signed`（默认）| `Unsigned`

指定定点数据是有符号还是无符号。有符号数据可以表示正值和负值，但无符号数据仅表示正值。

- `Signed`，将定点数据指定为有符号。
- `Unsigned`，将定点数据指定为无符号。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Scaling** — 定点数据定标的方法 `Best precision`（默认）| `Binary point` | `Slope and bias`

指定定点数据的定标方法，以避免溢出条件并最小化量化误差。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Word length** — 保存量化整数的字长位数 `16`（默认）| 0 到 32 的整数

指定保存量化整数的字长位数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Fraction length** — 指定定点数据类型的小数长度 `0`（默认）| 标量整数

将定点数据类型的小数长度指定为正整数或负整数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为 `Binary point`。

### **Slope** — 指定定点数据类型的斜率 `2^0`（默认）| 正实值标量

指定定点数据类型的斜率。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为 `Slope and bias`。

### **Bias** — 指定定点数据类型的偏置 `0`（默认）| 实值标量

将定点数据类型的偏置指定为任意实数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为 `Slope and bias`。

## 所属库

Simulink / Commonly Used Blocks Simulink / Signal Attributes HDL Coder / Commonly Used Blocks HDL Coder / HDL Floating Point Operations HDL Coder / Signal Attributes

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了额外的配置选项，这些选项会影响 HDL 实现和综合逻辑。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**注意**

使用 HDL Code Advisor，您可以将使用 `Stored Integer (SI)` 模式并在浮点与定点数据类型之间转换的 Data Type Conversion 模块替换为 Float Typecast 模块。

| 原生浮点 | |
| --- | --- |
| **LatencyStrategy** | 指定是将设计中的模块映射为 `inherit`、`Max`、`Min`、`Zero` 还是 `Custom` 以用于浮点运算符。默认值为 `inherit`。另请参阅 LatencyStrategy (HDL Coder)。 |
| **NFPCustomLatency** | 要指定值，请将 **LatencyStrategy** 设置为 `Custom`。HDL Coder 会添加与您为 **NFPCustomLatency** 设置指定的值相等的延迟。另请参阅 NFPCustomLatency (HDL Coder)。 |

**枚举数据支持**

此模块支持枚举信号的代码生成。使用此模块可将枚举类型的信号转换为任意整数类型，或将任意整数类型的信号转换为枚举类型。

**复数数据支持**

此模块支持复数信号的代码生成。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

将输入信号转换为指定的数据类型

Data Type Conversion 模块将任何 Simulink® 数据类型的输入信号转换为您指定的数据类型。

**注意**

要通过指定模块参数来控制输出数据类型，或从下游模块继承数据类型，请使用 Data Type Conversion 模块。要从模型中的不同信号继承数据类型，请使用 Data Type Conversion Inherited 模块。

### 转换定点信号

当您在定点数据类型之间转换时，**Input and output to have equal** 参数控制模块行为。当出现以下情况时，此参数不会更改模块的行为：

- 输入和输出不具有定点数据类型。
- 输入或输出具有带平凡缩放的定点数据类型。

有关定点数的更多信息，请参阅 Fixed-Point Numbers in Simulink (Fixed-Point Designer)。

要通过尝试保留输入信号的现实世界值来将信号从一种数据类型转换为另一种数据类型，请选择 `Real World Value (RWV)`，这是默认设置。该模块会考虑输入和输出的缩放所施加的限制，并尝试生成具有相等现实世界值的输出。

要通过执行存储整数值的缩放重新解释来更改输入信号的现实世界值，请选择 `Stored Integer (SI)`。在指定数据类型的限制内，该模块在转换期间尝试保留信号的存储整数值。最佳实践是使用相同的字长和有符号性来指定输入和输出数据类型。这样做可确保模块仅更改信号的缩放。为输入和输出指定不同的有符号性或字长可能会产生意外结果，例如范围丢失或意外的符号扩展。有关示例，请参阅 Convert Data Types in Simulink Models。

如果您选择 `Stored Integer (SI)`，该模块不会对浮点输入信号执行较低级别的位重新解释。例如，如果输入为 `single` 且值为 `5`，则将该输入存储在内存中的位由以下命令以十六进制给出。

```
num2hex(single(5))
```

```
40a00000
```

但是，Data Type Conversion 模块不会将存储整数值视为 `40a00000`，而是将其视为现实世界值 `5`。转换后，输出的存储整数值为 `5`。

### 转换枚举信号

使用 Data Type Conversion 模块按如下方式转换枚举信号：

1. 将枚举类型的信号转换为任意数值类型的信号。

   输入到 Data Type Conversion 模块的所有枚举值的底层整数必须在数值类型的范围内。否则，仿真期间会发生错误。
2. 将任意整数类型的信号转换为枚举类型的信号。

   输入到 Data Type Conversion 模块的值必须与某个枚举值的底层值匹配。否则，仿真期间会发生错误。

   您可以启用 **Saturate on integer overflow** 参数，以便当输入到模块的值与某个枚举值的底层值不匹配时，Simulink 使用枚举类型的默认值。请参阅 Type Casting for Enumerations (Simulink Coder)。

在以下情况下不能使用 Data Type Conversion 模块：

- 将非整数数值信号转换为枚举信号。
- 将复数信号转换为枚举信号，无论复数信号的实部和虚部是什么数据类型。

有关使用枚举类型的信息，请参阅 Simulink Enumerations。
