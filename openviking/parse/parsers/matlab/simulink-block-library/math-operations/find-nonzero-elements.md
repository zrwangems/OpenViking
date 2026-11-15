---
type: simulink-block
title: 'Find Nonzero Elements'
family: math-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'findnonzeroelements'
---

# Find Nonzero Elements

Find nonzero elements in array

## 中文

查找数组中的非零元素

### 所属库

Simulink / Math Operations

### 描述

Find Nonzero Elements 模块找到输入信号的所有非零元素，并返回这些元素的线性索引。如果输入是多维信号，则 Find Nonzero Elements 模块还可以返回非零输入元素的下标。在这两种情况下，您都可以显示具有非零输入值的输出端口。

Find Nonzero Elements 模块输出一个可变大小信号。任何可变大小信号的采样时间必须是离散的。如果模型尚未使用定步长求解器，则可能需要在“配置参数”对话框中选择定步长求解器。有关详细信息，请参阅比较求解器和选择求解器。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

输入信号，模块将从中查找所有非零元素。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
#### 输出

#### **Port\_1** — 非零元素的索引 可变大小信号

Find Nonzero Elements 模块将非零元素的索引输出为一个可变大小信号。您可以使用**输出数据类型**模块参数控制输出的数据类型。

##### 依赖关系

默认情况下，模块从第一个输出端口输出线性索引。当您将**索引输出格式**更改为**下标**时，该模块将以下标形式提供二维或更大信号的元素索引。在此模式下，必须指定**输入维数**，模块将为每个维度创建单独的输出端口。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **Port\_2** — 非零元素的值 可变大小信号

（可选）Find 模块可以将所有非零元素的值输出为一个可变大小信号。

##### 依赖关系

要启用此端口，请选择**显示非零输入值的输出端口**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 参数

#### 常设

#### **索引输出格式** — 非零元素索引的格式 **线性索引** (默认) | **下标**

选择非零输入值的索引的输出格式。

- 选择**线性索引**将以向量形式提供任何维度信号的元素索引。对于一维（向量）信号，索引对应于向量内非零值的位置。对于具有多个维度的信号，会沿第一个维度将下标转换为索引。您无需知道输入信号的信号维度。
- 选择**下标**将以下标形式提供二维或更大信号的元素索引。由于该模块显示每个维度的输出端口，因此该选项要求您指定**输入维数**。

##### 编程用法

|  |
| --- |
| **模块参数**：`IndexOutputFormat` |
| **类型：**字符向量 |
| **值**：`'Linear indices'` | `'Subscripts'` |
| **默认值：**`'Linear indices'` |

#### **输入维数** — 输入信号的维数 `1` (默认) | 标量

将输入信号的维数指定为 1 到 32 之间的正整数值。

##### 依赖关系

要启用此参数，请将**索引输出格式**设置为**下标**。

##### 编程用法

|  |
| --- |
| **模块参数**：`NumberOfInputDimensions` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'1'` |

#### **索引模式** — 指定从 0 或 1 开始的索引 **从 0 开始** (默认) | **从 1 开始**

将索引模式指定为**从 0 开始**或**从 1 开始**。

- 对于**从 0 开始**索引，索引 `0` 指定输入向量的第一个元素。索引 `1` 指定第二个元素，依此类推。
- 对于**从 1 开始**索引，索引 `1` 指定输入向量的第一个元素。索引 `2` 指定第二个元素，依此类推。

##### 编程用法

|  |
| --- |
| **模块参数**：`IndexMode` |
| **类型：**字符向量 |
| **值：**`'Zero-based'` | `'One-based'` |
| **默认值：**`'Zero-based'` |

#### **显示非零输入值的输出端口** — 为非零值启用输出端口 `off` (默认) | `on`

显示或隐藏非零输入值的输出端口。

- 清除此复选框 (`off`) 后，模块会隐藏非零输入值的输出端口。
- 选中此复选框 (`on`) 后，模块会显示非零输入值的输出端口。额外的输出端口提供非零输入元素的值。

##### 编程用法

|  |
| --- |
| **模块参数**：`ShowOutputPortForNonzeroInputValues` |
| **类型：**字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'off'` |

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

#### **输出数据类型** — 输出数据类型 `Inherit: Inherit via internal rule` (默认) | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `<data type expression>`

指定输出数据类型。

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit via internal rule'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'<data type expression>'` |
| **默认值：**`'Inherit: Inherit via internal rule'` |

#### **模式** — 选择数据类型模式 `Inherit` (默认) | `Built in` | `Fixed Point`

选择要指定的数据类别。

- **继承** - 数据类型的继承规则。选择 `Inherit` 将在右侧启用另一个菜单/文本框，您可以在其中选择继承模式。
- **内置** - 内置数据类型。选择 `Built in` 将在右侧启用另一个菜单/文本框，您可以在其中选择内置数据类型。
- **定点** - 定点数据类型。选择**定点**将启用可用于指定定点数据类型的其他参数。
- **表达式** - 计算结果为数据类型的表达式。选择 `Expression` 将在右侧启用另一个菜单/文本框，您可以在其中输入表达式。

有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 依赖关系

要启用此参数，请点击**显示数据类型助手**按钮。

#### **数据类型覆盖** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

为此信号选择数据类型覆盖模式。

- 当您选择 **inherit** 时，Simulink 从信号的上下文（即：从 Simulink® 中使用该信号的模块、`Simulink.Signal` 对象或 Stateflow® 图）中继承数据类型覆盖设置。
- 当您选择 **off** 时，Simulink 忽略信号上下文的数据类型覆盖设置，并使用为信号指定的定点数据类型。

有关详细信息，请参阅 Simulink 文档中的使用数据类型助手指定数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为**内置**或**定点**。

##### 提示

由于能够关闭单个数据类型的数据类型覆盖，您可以在应用数据类型覆盖时更好地控制模型中的数据类型。例如，您可以使用此选项确保数据类型满足下游模块的要求，而忽略数据类型覆盖设置。

#### **符号性** — 指定有符号或无符号 `Signed` (默认) | `Unsigned`

指定定点数据是有符号还是无符号。有符号数据可以表示正值和负值，无符号数据只表示正值。

- **有符号**，将定点数据指定为有符号数据。
- **无符号**，将定点数据指定为无符号数据。

有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为 `Fixed point`。

#### **字长** — 存储量化整数的字的位大小 `16` (默认) | 从 0 到 32 的整数

指定存储量化整数的字的位大小。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为**定点**。

#### **定标** — 定点数据的定标方法 `Integer` (默认)

指定定点数据的定标方法，以避免发生溢出情况并最大限度地减少量化误差。选择**整数**会指定定点数据的二进制小数点位置，并将小数长度设置为 `0`。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为 `Fixed point`。

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2010a 中推出**

## Libraries

Simulink / Math Operations

## Description

The Find Nonzero Elements block locates all nonzero elements of the input
signal and returns the linear indices of those elements. If the input is a
multidimensional signal, the Find Nonzero Elements block can also return
the subscripts of the nonzero input elements. In both cases, you can show an output port
with the nonzero input values.

The Find Nonzero Elements block outputs a variable-size signal. The sample
time for any variable-size signal must be discrete. If your model does not already use a
fixed-step solver, you may need to select a fixed-step solver in the Configuration
Parameters dialog. For more information, see Compare Solvers
and Choose a Solver.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

Input signal from which the block finds all nonzero elements.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Indices of nonzero elements variable-size signal

The Find Nonzero Elements block outputs the indices of nonzero elements
as a variable-size signal. You control the data type of the output using
the **Output data type** block parameter.

#### Dependencies

By default, the block outputs linear indices from the first output port. When you
change the **Index output format** to
`Subscripts`, the block instead
provides the element indices of a two-dimension or larger signal in
a subscript form. In this mode, you must specify the
**Number of input dimensions**, and the block
creates a separate output port for each dimension.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_2** — Values of nonzero elements variable-size signal

The Find block can optionally output the values of all nonzero
elements as a variable-size signal.

#### Dependencies

To enable this port, select **Show output port for nonzero
input values**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main

### **Index output format** — Format for indices of nonzero elements `Linear indices` (default) | `Subscripts`

Select the output format for the indices of the nonzero input
values.

- Selecting `Linear indices` provides
  the element indices of any dimension signal in a vector form.
  For one dimension (vector) signals, indices correspond to the
  position of nonzero values within the vector. For signals with
  more than one dimension, the conversion of subscripts to indices
  is along the first dimension. You do not need to know the signal
  dimension of the input signal.
- Selecting `Subscripts` provides the
  element indices of a two-dimension or larger signal in a
  subscript form. Because the block shows an output port for each
  dimension, this option requires you to specify the
  **Number of input dimensions**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IndexOutputFormat` |
| **Type:** character vector |
| **Values:** `'Linear indices'` | `'Subscripts'` |
| **Default:** `'Linear indices'` |

### **Number of input dimensions** — Number of dimensions for the input signal `1` (default) | scalar

Specify the number of dimensions for the input signal as a positive integer value from 1
to 32.

#### Dependencies

To enable this parameter, set **Index output
format** to
`Subscripts`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumberOfInputDimensions` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'1'` |

### **Index mode** — Specify zero- or one-based indexing `Zero-based` (default) | `One-based`

Specify the indexing mode as `Zero-based` or
`One-based`.

- For `Zero-based` indexing, an index
  of `0` specifies the first element of the input
  vector. An index of `1` specifies the second
  element, and so on.
- For `One-based` indexing, an index of
  `1` specifies the first element of the
  input vector. An index of `2`, specifies the
  second element, and so on.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IndexMode` |
| **Type:** character vector |
| **Values:** `'Zero-based'` | `'One-based'` |
| **Default:** `'Zero-based'` |

### **Show output port for nonzero input values** — Enable output port for nonzero values `off` (default) | `on`

Show or hide the output port for nonzero input values.

- When you clear this check box (`off`), the
  block hides the output port for nonzero input values.
- When you select this check box (`on`), the
  block displays the output port for nonzero input values. The
  additional output port provides values of the nonzero input
  elements.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowOutputPortForNonzeroInputValues` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

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

### Data Types

### **Output data type** — Output data type `Inherit: Inherit via internal rule` (default) | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `<data type expression>`

Specify the output data type.

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Mode** — Select data type mode `Inherit` (default) | `Built in` | `Fixed Point`

Select the category of data to specify.

- `Inherit` — Inheritance rules for data types.
  Selecting `Inherit` enables a second menu/text box to the right
  where you can select the inheritance mode.
- `Built in` — Built-in data types. Selecting
  `Built in` enables a second menu/text box to the right
  where you can select a built-in data type.
- `Fixed point` — Fixed-point data types. Selecting
  `Fixed point` enables additional parameters that
  you can use to specify a fixed-point data type.
- `Expression` — Expressions that evaluate to data
  types. Selecting `Expression` enables a second menu/text box to
  the right, where you can enter the expression.

For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, click the **Show data type
assistant** button.

### **Data type override** — Specify data type override mode for this signal `Inherit` | `Off`

Select the data type override mode for this signal.

- When you select `Inherit`, Simulink inherits the data
  type override setting from its context, that is, from the block,
  `Simulink.Signal` object or Stateflow® chart in Simulink® that is using the signal.
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

### **Signedness** — Specify signed or unsigned `Signed` (default) | `Unsigned`

Specify whether the fixed-point data is signed or unsigned. Signed data can represent
positive and negative values, but unsigned data represents positive values only.

- `Signed`, specifies the fixed-point data as
  signed.
- `Unsigned`, specifies the fixed-point data as
  unsigned.

For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set the **Mode** to `Fixed
point`.

### **Word length** — Bit size of the word that holds the quantized integer `16` (default) | integer from 0 to 32

Specify the bit size of the word that holds the quantized integer. For
more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Scaling** — Method for scaling your fixed-point data `Integer` (default)

Specify the method for scaling your fixed-point data to avoid overflow conditions and
minimize quantization errors. Selecting
`Integer` specifies a binary point location
for fixed-point data and sets the fraction length to
`0`. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2010a**
