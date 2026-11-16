---
type: simulink-block
title: 'Data Type Conversion'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Signal Attributes'
documentation_page: 'datatypeconversion'
documentation_source_path: 'slref/datatypeconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Data Type Conversion

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

输入信号，指定为标量、向量、矩阵或 N 维数组。输入可以是任何实数或复数值信号。如果输入为实数，则输出为实数。如果输入为复数，则输出为复数。该模块将输入信号转换为指定的**输出数据类型**。

当转换定点数据类型时，使用**输入和输出相等**参数来确定转换是基于信号的 `Real World Value (RWV)` 还是 `Stored Integer (SI)` 值进行。有关详细信息，请参阅 Convert Fixed-Point Signals。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵 | N 维数组

输出信号，转换为指定的数据类型，且维数与输入信号相同。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

## 参数

### **输出最小值** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的下限值。

软件使用最小值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges 和 Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 对从模型生成的代码进行优化。此优化可能会移除算法代码，并影响某些仿真模式（如 SIL 或 external mode）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**输出最小值**不会对实际输出信号进行饱和或裁剪。请改用 Saturation 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **输出最大值** — 用于范围检查的最大输出值 `[]`（默认）| 标量

软件检查的输出范围的上限值。

软件使用最大值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges 和 Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 对从模型生成的代码进行优化。此优化可能会移除算法代码，并影响某些仿真模式（如 SIL 或 external mode）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**输出最大值**不会对实际输出信号进行饱和或裁剪。请改用 Saturation 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **输出数据类型** — 输出数据类型 `Inherit: Inherit via back propagation`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

选择输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutDataTypeStr` |
| **类型：** character vector |
| **值：** `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'Enum: <class name>'` | `'<data type expression>'` |
| **默认：** `'Inherit: Inherit via back propagation'` |

### **锁定输出数据类型设置以防止被定点工具更改** — 用于防止定点工具覆盖输出数据类型的选项 `off`（默认）| `on`

选择此参数可防止定点工具覆盖你在模块上指定的**输出**数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **值：** | `'off'`（默认）| `'on'` |

### **输入和输出相等** — 用于转换定点数据类型的约束 `Real World Value (RWV)`（默认）| `Stored Integer (SI)`

指定在定点数据表示的上下文中，输入和输出的哪种值必须相等。

- `Real World Value (RWV)` — 指定使输入的 `Real World Value (RWV)` 等于输出的 `Real World Value (RWV)` 的目标。
- `Stored Integer (SI)` — 指定使输入的 `Stored Integer (SI)` 值等于输出的 `Stored Integer (SI)` 值的目标。

#### 编程用法

|  |
| --- |
| **模块参数：** `ConvertRealWorld` |
| **类型：** character vector |
| **值：** `'Real World Value (RWV)' | 'Stored Integer (SI)'` |
| **默认：** `'Real World Value (RWV)'` |

### **整数舍入模式** — 指定定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

请选择以下舍入模式之一。

`Ceiling`
:   将正数和负数都向正无穷方向舍入。等效于 MATLAB® 的 `ceil` 函数。

`Convergent`
:   将数字舍入到最接近的可表示值。如果出现结值，则舍入到最接近的偶数整数。等效于 Fixed-Point Designer™ 的 `convergent` 函数。

`Floor`
:   将正数和负数都向负无穷方向舍入。等效于 MATLAB 的 `floor` 函数。

`Nearest`
:   将数字舍入到最接近的可表示值。如果出现结值，则向正无穷方向舍入。等效于 Fixed-Point Designer 的 `nearest` 函数。

`Round`
:   将数字舍入到最接近的可表示值。如果出现结值，则将正数向正无穷方向舍入，将负数向负无穷方向舍入。等效于 Fixed-Point Designer 的 `round` 函数。

`Simplest`
:   自动在向 floor 舍入和向零舍入之间选择，以生成尽可能高效的舍入代码。

`Zero`
:   将数字向零方向舍入。等效于 MATLAB 的 `fix` 函数。

#### 编程用法

|  |
| --- |
| **模块参数**： `RndMeth` |
| **类型**： character vector |
| **值**： `'Ceiling'` | `'Convergent'` | `'Floor'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |
| **默认**： `'Floor'` |

#### 另请参阅

有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

### **整数溢出时饱和** — 溢出操作的方法 `off`（默认）| `on`

指定溢出是饱和还是环绕。

- `on` — 溢出饱和为该数据类型可表示的最小值或最大值。
- `off` — 溢出环绕为该数据类型可表示的相应值。

例如，有符号 8 位整数 `int8` 可表示的最大值是 127。任何大于此最大值的模块运算结果都会导致该 8 位整数溢出。

- 选中此参数时，模块输出在 127 处饱和。类似地，模块输出在最小输出值 -128 处饱和。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时是 -126。

#### 提示

- 当模型可能发生溢出，并且你希望在生成代码中具有显式饱和保护时，请考虑选中此参数。
- 当你希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors。
- 选中此参数时，饱和会应用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认）| `'on'` |

### **采样时间（-1 表示继承）** — 采样之间的时间间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当将此参数设置为 `-1` 以外的值时，此参数才可见。要了解详细信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认）| 带引号的标量或向量 |

### **模式** — 选择数据类型模式 `Inherit`（默认）| `Built in` | `Fixed Point`

选择要指定的数据类别。

- `Inherit` — 数据类型的继承规则。选择 `Inherit` 会启用右侧的第二个菜单/文本框，你可以在其中选择继承模式。
- `Built in` — 内置数据类型。选择 `Built in` 会启用右侧的第二个菜单/文本框，你可以在其中选择内置数据类型。
- `Fixed point` — 定点数据类型。选择 `Fixed point` 会启用其他参数，你可以使用这些参数指定定点数据类型。
- `Expression` — 求值为数据类型的表达式。选择 `Expression` 会启用右侧的第二个菜单/文本框，你可以在其中输入表达式。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请点击 **显示数据类型助手** 按钮。

### **数据类型覆盖** — 指定此信号的数据类型覆盖模式 `Inherit` | `Off`

选择此信号的数据类型覆盖模式。

- 选择 `Inherit` 时，Simulink 从其上下文继承数据类型覆盖设置，即从正在使用该信号的 Simulink 中的模块、`Simulink.Signal` 对象或 Stateflow® 图继承。
- 选择 `Off` 时，Simulink 忽略其上下文的数据类型覆盖设置，并使用为该信号指定的定点数据类型。

有关详细信息，请参阅 Simulink 文档中的 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将**模式**设置为 `Built in` 或 `Fixed point`。

#### 提示

针对单个数据类型关闭数据类型覆盖的功能，可在应用数据类型覆盖时更好地控制模型中的数据类型。例如，你可以使用此选项确保数据类型满足下游模块的要求，而不受数据类型覆盖设置的影响。

### **符号性** — 指定有符号或无符号 `Signed`（默认）| `Unsigned`

指定定点数据是有符号还是无符号。有符号数据可以表示正值和负值，但无符号数据仅表示正值。

- `Signed`，将定点数据指定为有符号。
- `Unsigned`，将定点数据指定为无符号。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将**模式**设置为 `Fixed point`。

### **定标** — 对定点数据进行定标的方法 `Best precision`（默认）| `Binary point` | `Slope and bias`

指定对定点数据进行定标的方法，以避免溢出情况并最小化量化误差。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将**模式**设置为 `Fixed point`。

### **字长** — 保存量化整数的字的 bit 大小 `16`（默认）| 0 到 32 的整数

指定保存量化整数的字的 bit 大小。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将**模式**设置为 `Fixed point`。

### **小数长度** — 指定定点数据类型的小数长度 `0`（默认）| 标量整数

将定点数据类型的小数长度指定为正整数或负整数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将**定标**设置为 `Binary point`。

### **斜率** — 指定定点数据类型的斜率 `2^0`（默认）| 正的实数值标量

指定定点数据类型的斜率。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将**定标**设置为 `Slope and bias`。

### **偏置** — 指定定点数据类型的偏置 `0`（默认）| 实数值标量

将定点数据类型的偏置指定为任意实数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将**定标**设置为 `Slope and bias`。

## 所属库

Simulink / Commonly Used Blocks Simulink / Signal Attributes HDL Coder / Commonly Used Blocks HDL Coder / HDL Floating Point Operations HDL Coder / Signal Attributes

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**注意**

使用 HDL Code Advisor，你可以将使用 `Stored Integer (SI)` 模式并在浮点数据类型和定点数据类型之间转换的 Data Type Conversion 模块替换为 Float Typecast 模块。

| 本机浮点 | |
| --- | --- |
| **LatencyStrategy** | 指定是否将设计中的模块映射到浮点运算符的 `inherit`、`Max`、`Min`、`Zero` 或 `Custom`。默认值为 `inherit`。另请参阅 LatencyStrategy (HDL Coder)。 |
| **NFPCustomLatency** | 要指定值，请将 **LatencyStrategy** 设置为 `Custom`。HDL Coder 会添加与为 **NFPCustomLatency** 设置指定的值相等的延迟。另请参阅 NFPCustomLatency (HDL Coder)。 |

**枚举数据支持**

此模块支持枚举信号的代码生成。使用此模块可将枚举类型的信号转换为任何整数类型，或将任何整数类型的信号转换为枚举类型。

**复数数据支持**

此模块支持复数信号的代码生成。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**R2006a 之前推出**

## 描述

将输入信号转换为指定的数据类型

Data Type Conversion 模块将任何 Simulink® 数据类型的输入信号转换为你指定的数据类型。

**注意**

要通过指定模块参数来控制输出数据类型，或从下游模块继承数据类型，请使用 Data Type Conversion 模块。要从模型中的其他信号继承数据类型，请使用 Data Type Conversion Inherited 模块。

### 转换定点信号

当在定点数据类型之间转换时，**输入和输出相等**参数控制模块行为。在以下情况下，此参数不会更改模块的行为：

- 输入和输出不具有定点数据类型。
- 输入或输出具有平凡定标的定点数据类型。

有关定点数的详细信息，请参阅 Fixed-Point Numbers in Simulink (Fixed-Point Designer)。

要通过尝试保留输入信号的实际值来将信号从一种数据类型转换为另一种数据类型，请选择 `Real World Value (RWV)`，这是默认设置。该模块会考虑输入和输出的定标所施加的限制，并尝试生成具有相等实际值的输出。

要通过执行存储整数值的定标重新解释来更改输入信号的实际值，请选择 `Stored Integer (SI)`。在指定数据类型的限制内，该模块会尝试在转换期间保留信号的存储整数值。最佳做法是使用相同的字长和符号性指定输入和输出数据类型。这样做可确保该模块仅更改信号的定标。为输入和输出指定不同的符号性或字长可能会产生意外结果，例如范围丢失或意外符号扩展。有关示例，请参阅 Convert Data Types in Simulink Models。

如果选择 `Stored Integer (SI)`，该模块不会对浮点输入信号执行较低级别的位重新解释。例如，如果输入为 `single` 且值为 `5`，则内存中存储输入的位由以下命令以十六进制给出。

    num2hex(single(5))

    40a00000

但是，Data Type Conversion 模块不会将存储整数值视为 `40a00000`，而是将其视为实际值 `5`。转换后，输出的存储整数值为 `5`。

### 转换枚举信号

使用 Data Type Conversion 模块按如下方式转换枚举信号：

1. 将枚举类型的信号转换为任何数值类型的信号。

   输入到 Data Type Conversion 模块的所有枚举值的底层整数必须在数值类型的范围内。否则，仿真期间会发生错误。
2. 将任何整数类型的信号转换为枚举类型的信号。

   输入到 Data Type Conversion 模块的值必须与某个枚举值的底层值匹配。否则，仿真期间会发生错误。

   你可以启用 **整数溢出时饱和** 参数，以便当输入到模块的值与某个枚举值的底层值不匹配时，Simulink 使用枚举类型的默认值。请参阅 Type Casting for Enumerations (Simulink Coder)。

在以下情况下，你不能使用 Data Type Conversion 模块：

- 将非整数数值信号转换为枚举信号。
- 将复数信号转换为枚举信号，无论该复数信号的实部和虚部是什么数据类型。

有关使用枚举类型的信息，请参阅 Simulink Enumerations。
