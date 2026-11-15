---
type: simulink-block
title: 'Logical Operator'
family: logic-and-bit-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'logicaloperator'
---

# Logical Operator

Perform specified logical operation on input

## 中文

对输入执行指定的逻辑运算

### 所属库

Simulink / Commonly Used Blocks Simulink / Logic and Bit Operations HDL Coder / Commonly Used Blocks HDL Coder / Logic and Bit Operations

### 描述

Logical Operator 模块对其输入执行指定的逻辑运算。输入值为非零值时为 true (`1`)，为零时则为 false (`0`)。

使用**运算符**参数列表选择连接输入的布尔运算。如果您选择**矩形**作为**图标形状**属性，所选运算符的名称将显示在模块图标上。如果您选择**不同**作为**图标形状**属性，则所选运算符的名称不会显示在模块图标上。下表显示了支持的运算：

| 运算 | 描述 |
| --- | --- |
| AND | 如果所有输入均为 TRUE，则为 TRUE |
| OR | 如果至少有一个输入为 TRUE，则为 TRUE |
| NAND | 如果至少有一个输入为 FALSE，则为 TRUE |
| NOR | 如果所有输入均不为 TRUE，则为 TRUE |
| XOR | 如果有奇数个输入为 TRUE，则为 TRUE |
| NXOR | 如果有偶数个输入为 TRUE，则为 TRUE |
| NOT | 如果输入为 FALSE，则为 TRUE |

如果选择**不同**作为**图标形状**，则模块的外观会指示其功能。Simulink® 软件将按照 IEEE® 逻辑函数的图形符号标准，显示所选运算符的独特形状。

要指定输入端口的数量，请使用**输入端口数目**参数。使用**输出数据类型**参数指定输出类型。如果为 TRUE，则输出值为 `1`，如果为 FALSE，则输出值为 `0`。

**注意**

输出数据类型应该准确表示零。满足此条件的数据类型包括有符号整数和无符号整数，以及所有浮点数据类型。

输出大小取决于输入向量大小和所选运算符：

- 如果模块有多个输入，则任何非标量输入都必须具有相同的维度。例如，如果有任何输入是 2×2 数组，则所有其他非标量输入也必须是 2×2 数组。

  标量输入将扩展为与非标量输入具有相同的维度。

  如果模块有多个输入，则输出与输入具有相同的维度（标量扩展后），并且每个输出元素都是将指定逻辑运算应用于相应输入元素的结果。例如，如果指定运算为 AND，输入为 2×2 数组，则输出为 2×2 数组，其左上角的元素是将 AND 应用于输入的左上角元素的结果，以此类推。
- 对于单个向量输入，模块会将运算（除 NOT 运算符外）应用于向量的所有元素。输出始终为标量。
- NOT 运算符仅接受一个输入，该输入可以是标量也可以是向量。如果输入为向量，则输出为相同大小的向量，其中包含输入向量元素的逻辑补码。

当配置为多输入 XOR 门时，此模块将按照 IEEE 逻辑元素标准的规定执行加法双模运算。

### 端口

#### 输入

#### **Port\_1** — 第一个输入信号 标量 | 向量 | 矩阵

第一个输入信号，指定为标量、向量或矩阵。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **Port\_2** — 第二个输入信号 标量 | 向量 | 矩阵

第二个输入信号，指定为标量、向量或矩阵。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **Port\_N** — 第 N 个输入信号 标量 | 向量 | 矩阵

第 N 个输入信号，指定为标量、向量或矩阵。

##### 依赖关系

要启用其他输入端口，请使用**输入端口数目**参数。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

输出信号，由 0 和 1 组成，具有与输入相同的维度。您可以使用**要求所有输入和输出具有相同的数据类型**和**输出数据类型**参数控制输出数据类型。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 参数

#### 常设

#### **运算符** — 逻辑运算符 **AND** (默认) | **OR** | **nand** | **NOR** | **XOR** | **NXOR** | **NOT**

选择要应用于模块输入的逻辑运算符。

- **AND** - 如果所有输入均为 TRUE，则为 TRUE
- **OR** - 如果至少有一个输入为 TRUE，则为 TRUE
- **nand** - 如果至少有一个输入为 FALSE，则为 TRUE
- **NOR** - 如果所有输入均不为 TRUE，则为 TRUE
- **XOR** - 如果有奇数个输入为 TRUE，则为 TRUE
- **NXOR** - 如果有偶数个输入为 TRUE，则为 TRUE
- **NOT** - 如果输入为 FALSE，则为 TRUE

##### 编程用法

|  |
| --- |
| **模块参数**：`Operator` |
| **类型：**字符向量 |
| **值：**`'AND' | 'OR' | 'NAND' | 'NOR' | 'XOR' | 'NXOR' | 'NOT'` |
| **默认值：**`'AND'` |

#### **输入端口数目** — 输入数目 `2` (默认) | 正整数

将模块输入的个数指定为正整数。

##### 编程用法

|  |
| --- |
| **模块参数**：`Inputs` |
| **类型：**字符向量 |
| **值：**正整数 |
| **默认值：**`'2'` |

##### 依赖关系

将**运算符**设置为 **NOT** 时，此参数不可用。

#### **图标形状** — 图标形状 **矩形** (默认) | **不同**

指定模块图标的形状。

- **矩形** - 生成显示所选运算符名称的矩形模块。
- **不同** - 按照 IEEE 标准针对所选运算符使用图形符号。

##### 编程用法

|  |
| --- |
| **模块参数**：`IconShape` |
| **类型：**字符向量 |
| **值**：`'rectangular' | 'distinctive'` |
| **默认值：**`'rectangular'` |

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

#### 数据类型

#### **要求所有输入和输出具有相同的数据类型** — 要求所有端口具有相同的数据类型 `off` (默认) | `on`

若要求所有模块输入和输出具有相同的数据类型，请选中此复选框。清除此复选框后，输入和输出可以具有不同数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`AllPortsSameDT` |
| **类型：**字符向量 |
| **值：**`'off' | 'on` |
| **默认值：**`'off'` |

#### **输出数据类型** — 输出数据类型 **boolean** (默认) | **继承: Logical（请参阅配置参数：优化）** | **继承:通过反向传播继承** | **fixdt(1,16)** | **<数据类型表达式>**

指定输出数据类型。各选项的意义如下：

- **boolean** - 模块输出的数据类型为 `boolean`。
- **继承: Logical（请参阅配置参数：优化)** - 模块使用**将逻辑信号实现为布尔数据**配置参数指定输出数据类型（请参阅将逻辑信号实现为布尔数据(而不是双精度数据)）。

  **注意**

  此选项支持在 `boolean` 选项可用之前创建的模型。对于新模型，请使用其他选项之一，首选 `boolean`。
- **继承:通过反向传播继承** - 模块继承数据类型。选择此选项时，输出数据类型和定标与下一个下游模块匹配。
- **fixdt(1,16)** - 模块输出具有指定的定点数据类型 `fixdt(1,16)`。

  **提示**

  **数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。
- **<data type expression>** - 模块输出具有您指定为数据类型表达式的数据类型，例如 `Simulink.NumericType`。

  **提示**

  要输入内置数据类型（`double`、`single`、`int8`、`uint8`、`int16`、`uint16`、`int32` 或 `uint32`），请将表达式用单引号引起来。例如，输入 `'double'` 而不是 `double`。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型：**字符向量 |
| **值**：`'Inherit: Logical (see Configuration Parameters: Optimization)'` | `'boolean'` | `'fixdt(1,16)'` | `'<data type expression>'` |
| **默认值：**`'boolean'` |

#### **模式** — 要指定的数据的类别 **内置** (默认) | **继承** | **定点** | **表达式**

选择要指定的数据类别。

- **内置** - 指定内置数据类型。选择**内置**将启用 **boolean**。
- **继承** - 指定数据类型的继承规则。选择 **inherit** 将启用**逻辑(请参阅 "配置参数":优化)**。
- **定点** - 指定定点数据类型。
- **表达式** - 指定计算结果为数据类型的表达式。

##### 依赖关系

要启用此参数，请点击**显示数据类型助手**按钮。

#### **数据类型覆盖** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

为此信号选择数据类型覆盖模式。

- 当您选择 **inherit** 时，Simulink 从信号的上下文（即：从 Simulink 中使用该信号的模块、`Simulink.Signal` 对象或 Stateflow® 图）中继承数据类型覆盖设置。
- 当您选择 **off** 时，Simulink 忽略信号上下文的数据类型覆盖设置，并使用为信号指定的定点数据类型。

有关详细信息，请参阅 Simulink 文档中的使用数据类型助手指定数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为**内置**或**定点**。

##### 提示

由于能够关闭单个数据类型的数据类型覆盖，您可以在应用数据类型覆盖时更好地控制模型中的数据类型。例如，您可以使用此选项确保数据类型满足下游模块的要求，而忽略数据类型覆盖设置。

#### **符号性** — 定点数据的符号性 **有符号** (默认) | **无符号**

指定您希望定点数据为有符号还是无符号数据。有符号数据可以表示正值和负值，无符号数据只表示正值。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为**定点**。

#### **字长** — 存储量化整数的字的位大小 `16` (默认) | 从 0 到 32 的整数

指定存储量化整数的字的位大小。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为**定点**。

#### **定标** — 定标的方法 **整数** (默认)

指定定点数据的定标方法，以避免发生溢出情况并最大限度地减少量化误差。指定**整数**等效于指定二进制小数点位置并将小数长度设置为 `0`。

##### 依赖关系

要启用此参数，请点击**显示数据类型助手**按钮并将**模式**设置为**定点**。

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Commonly Used Blocks Simulink / Logic and Bit Operations HDL Coder / Commonly Used Blocks HDL Coder / Logic and Bit Operations

## Description

The Logical Operator block performs the specified logical operation on its
inputs. An input value is true (`1`) if it is nonzero and false
(`0`) if it is zero.

You select the Boolean operation connecting the inputs with the
**Operator** parameter list. If you select
`rectangular` as the **Icon shape**
property, the name of the selected operator displays on the block icon. If you select
`distinctive` as the **Icon shape**
property, the name of the selected operator does not display on the block icon. This
table shows supported operations:

| Operation | Description |
| --- | --- |
| AND | TRUE if all inputs are TRUE |
| OR | TRUE if at least one input is TRUE |
| NAND | TRUE if at least one input is FALSE |
| NOR | TRUE when no inputs are TRUE |
| XOR | TRUE if an odd number of inputs are TRUE |
| NXOR | TRUE if an even number of inputs are TRUE |
| NOT | TRUE if the input is FALSE |

If you select `distinctive` as the **Icon shape**,
the block appearance indicates its function. Simulink® software displays a distinctive shape for the selected operator,
conforming to the IEEE® Standard Graphic Symbols for Logic Functions.

To specify the number of input ports, use the **Number of input ports**
parameter. The output type is specified using the **Output data type**
parameter. An output value is `1` if TRUE and `0` if
FALSE.

**Note**

The output data type should represent zero exactly. Data types that satisfy this condition include signed and unsigned integers, and any floating-point data type.

The size of the output depends on input vector size and the selected operator:

- If the block has more than one input, any nonscalar inputs must have the same dimensions. For example, if any input is a 2-by-2 array, all other nonscalar inputs must also be 2-by-2 arrays.

  Scalar inputs are expanded to have the same dimensions as the nonscalar inputs.

  If the block has more than one input, the output has the same dimensions as the inputs
  (after scalar expansion) and each output element is the result of applying the
  specified logical operation to the corresponding input elements. For example, if
  the specified operation is AND and the inputs are 2-by-2 arrays, the output is a
  2-by-2 array whose top left element is the result of applying AND to the top
  left elements of the inputs, and so on.
- For a single vector input, the block applies the operation (except the NOT operator) to all elements of the vector. The output is always a scalar.
- The NOT operator accepts only one input, which can be a scalar or a vector. If the input is a vector, the output is a vector of the same size containing the logical complements of the input vector elements.

When configured as a multi-input XOR gate, this block performs an addition modulo two
operation as mandated by the IEEE Standard for Logic Elements.

## Ports

### Input

### **Port\_1** — First input signal scalar | vector | matrix

First input signal, specified as a scalar, vector, or matrix.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_2** — Second input signal scalar | vector | matrix

Second input signal, specified as a scalar, vector, or matrix.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_N** — Nth input signal scalar | vector | matrix

Nth input signal, specified as a scalar, vector, or matrix.

#### Dependencies

To enable additional input ports, use the **Number of
input ports** parameter.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output signal, consisting of zeros and ones, with the same dimensions
as the input. You control the output data type with the
**Require all inputs and output to have the same data
type** and **Output data type**
parameters.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main

### **Operator** — Logical operator `AND` (default) | `OR` | `NAND` | `NOR` | `XOR` | `NXOR` | `NOT`

Select the logical operator to apply to block inputs.

- `AND` — TRUE if all inputs are
  TRUE
- `OR` — TRUE if at least one input is
  TRUE
- `NAND` — TRUE if at least one input
  is FALSE
- `NOR` — TRUE when no inputs are
  TRUE
- `XOR` — TRUE if an odd number of
  inputs are TRUE
- `NXOR` — TRUE if an even number of
  inputs are TRUE
- `NOT` — TRUE if the input is
  FALSE

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Operator` |
| **Type:** character vector |
| **Values:** `'AND' | 'OR' | 'NAND' | 'NOR' | 'XOR' | 'NXOR' | 'NOT'` |
| **Default:** `'AND'` |

### **Number of input ports** — Number of inputs `2` (default) | positive integer

Specify the number of block inputs as a positive integer.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Inputs` |
| **Type:** character vector |
| **Values:** positive integer |
| **Default:** `'2'` |

#### Dependencies

This parameter is not available when you set the
**Operator** to
`NOT`.

### **Icon shape** — Icon shape `rectangular` (default) | `distinctive`

Specify the shape of the block icon.

- `rectangular` — Results in a
  rectangular block that displays the name of the selected
  operator.
- `distinctive` — Use the graphic
  symbol for the selected operator as specified by the IEEE standard.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IconShape` |
| **Type:** character vector |
| **Values:** `'rectangular' | 'distinctive'` |
| **Default:** `'rectangular'` |

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

### Data Type

### **Require all inputs and output to have the same data type** — Require all ports to have same data type `off` (default) | `on`

To require that all block inputs and the output have the same data
type, select this check box. When you clear this check box, the inputs
and output can have different data types.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AllPortsSameDT` |
| **Type:** character vector |
| **Values:** `'off' | 'on` |
| **Default:** `'off'` |

### **Output data type** — Output data type `boolean` (default) | `Inherit: Logical (see Configuration Parameters: Optimization)` | `Inherit: Inherit via back propagation` | `fixdt(1,16)` | `<data type expression>`

Specify the output data type. When you select:

- `boolean` — The block output has data type
  `boolean`.
- `Inherit: Logical (see Configuration Parameters:
  Optimization)` — The block uses the **Implement logic
  signals as Boolean data** configuration parameter to specify the
  output data type (see Implement logic signals as Boolean data (vs. double)).

  **Note**

  This option supports models created before the `boolean`
  option was available. Use one of the other options, preferably
  `boolean`, for new models.
- `Inherit: Inherit via back propagation` — The block
  inherits a data type. When you select this option, the output data type and
  scaling matches that of the next downstream block.
- `fixdt(1,16)` — The block output has the specified
  fixed-point data type `fixdt(1,16)`.

  **Tip**

  The **Data Type Assistant** helps you set data
  attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.
- `<data type expression>` — The block output has
  the data type you specify as a data type expression, for example,
  `Simulink.NumericType`.

  **Tip**

  To enter a built-in data type (`double`,
  `single`, `int8`,
  `uint8`, `int16`,
  `uint16`, `int32`, or
  `uint32`), enclose the expression in single quotes. For
  example, enter `'double'` instead of
  `double`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Logical (see Configuration Parameters: Optimization)'` | `'boolean'` | `'fixdt(1,16)'` | `'<data type expression>'` |
| **Default:** `'boolean'` |

### **Mode** — Category of data to specify `Built in` (default) | `Inherit` | `Fixed point` | `Expression`

Select the category of data to specify.

- `Built in` — Specifies built-in data types. Selecting
  `Built in` enables
  `boolean`.
- `Inherit` — Specifies inheritance rules for data
  types. Selecting `Inherit` enables `Logical
  (see Configuration Parameters: Optimization)`.
- `Fixed point` — Specifies fixed-point data
  types.
- `Expression` — Specifies expressions that evaluate to
  data types.

#### Dependencies

To enable this parameter, click the **Show data type
assistant** button.

### **Data type override** — Specify data type override mode for this signal `Inherit` | `Off`

Select the data type override mode for this signal.

- When you select `Inherit`, Simulink inherits the data
  type override setting from its context, that is, from the block,
  `Simulink.Signal` object or Stateflow® chart in Simulink that is using the signal.
- When you select `Off`, Simulink ignores the data type
  override setting of its context and uses the fixed-point data type specified for
  the signal.

For more information, see Specify Data Types Using Data Type Assistant in the
Simulink documentation.

#### Dependencies

To enable this parameter, set **Mode** to `Built
in` or `Fixed point`.

#### Tips

The ability to turn off data type override for an individual data type provides
greater control over the data types in your model when you apply data type override.
For example, you can use this option to ensure that data types meet the requirements
of downstream blocks regardless of the data type override setting.

### **Signedness** — Signedness of fixed-point data `Signed` (default) | `Unsigned`

Specify whether you want the fixed-point data as signed or unsigned.
Signed data can represent positive and negative values, but unsigned
data represents positive values only. For more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Word length** — Bit size of the word that holds the quantized integer `16` (default) | integer from 0 to 32

Specify the bit size of the word that holds the quantized integer. For
more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Scaling** — Method of scaling `Integer` (default)

Specify the method for scaling your fixed-point data to avoid overflow conditions and
minimize quantization errors. Specifying `Integer` has the same
result as specifying a binary point location and setting the fraction length to
`0`.

#### Dependencies

To enable this parameter, click the **Show data type
assistant** button and set **Mode** to
`Fixed point`.

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
