---
type: simulink-block
title: 'Assignment'
family: math-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'assignment'
---

# Assignment

Assign values to specified elements of signal

## 中文

为指定的信号元素赋值

### 所属库

Simulink / Math Operations HDL Coder / Math Operations

### 描述

Assignment 模块为指定的信号元素赋值。您可以通过在模块对话框中输入索引，或者通过将一个或多个外部索引源连接到模块，来指定要赋值的元素的索引。模块数据端口 `U` 处的信号指定要赋给 `Y` 的值。该模块将 `Y` 的指定元素替换为数据信号的元素。

基于您为**输出维度的数量**参数输入的值，将显示一个索引选项表。表中的每一行对应于**输出维度的数量**中的一个输出维度。对于每个维度，您可以定义要使用的信号元素。可将向量信号指定为一维信号，将矩阵信号指定为二维信号。要启用外部索引端口，请在表的对应行中将**索引选项**设置为**索引向量(端口)** 或**起始索引(端口)**。

例如，假设一个 5 维信号具有从 1 开始的索引模式。Assignment 模块对话框中的表将发生变化，使每个维度都有一个对应的行。如果您使用以下选项定义每个维度：

| 行 | 索引选项 | 索引 |
| --- | --- | --- |
| 1 | **全部赋值** |  |
| 2 | **索引向量(对话框)** | `[1 3 5]` |
| 3 | **起始索引(对话框)** | `4` |
| 4 | **起始索引(端口)** |  |
| 5 | **索引向量(端口)** |  |

所赋的值为 `Y(1:end,[1 3 5],4:3+size(U,3),Idx4:Idx4+size(U,4)-1,Idx5)=U`，其中 `Idx4` 和 `Idx5` 是维度 4 和 5 的输入端口。

在普通模式下使用 Assignment 模块时，Simulink® 将模块输出初始化为零，即使模型没有显式初始化它们也是如此。在加速模式下，Simulink 将模型转换成 S-Function。这涉及到代码生成。生成的代码可能不会隐式初始化模块输出。在这种情况下，您必须显式初始化模型输出。

您可以使用模块为向量、矩阵或多维信号赋值。

可使用总线数组作为 Assignment 模块的输入信号。

#### 条件子系统中的 Assignment 模块

如果在条件子系统模块中放置一个 Assignment 模块，在许多情况下会插入一个隐藏的信号缓冲区（相当于 Signal Conversion 模块），并且将来自 Assignment 模块的信号与部分写入合并会导致错误。

但是，如果选择条件子系统 Outport 模块的**确保输出端口为虚拟端口**参数，将对此类情况提供支持，并且可以使用 Assignment 模块部分写入数组。请参阅Ensure Output Port Is Virtual。

### 端口

#### 输入

#### **Y0** — 输出信号的初始值 标量 | 向量

输出信号的初始值。如果未对在输入数据端口 (**U**) 上指定的信号分配与初始值不同的值，则端口 **Y** 上的输出信号值与初始值匹配。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `Boolean` | `enumerated` | `bus`

#### **U** — 输入数据端口 标量 | 向量

赋给输出元素的值（当指定了该值时）。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `Boolean` | `enumerated` | `bus`

#### **IndxN** — 第 *N* 个索引信号 标量 | 向量

外部端口，用于指定对应输出元素的赋值的索引。

您可以指定自定义宽度的整数（例如，15 位整数或 23 位整数）作为索引信号值。配置整数的宽度时，必须将**模式**指定为**定点**，其中**字长**小于或等于 65,535，**斜率**等于 1，**偏置**等于 0。有关指定定点数据类型的详细信息，请参阅使用数据类型助手指定数据类型。

##### 依赖关系

要启用外部索引端口，请在**索引选项**表的对应行中将**索引选项**设置为**索引向量(端口)** 或**起始索引(端口)**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
#### 输出

#### **Y** — 具有已赋值的输出信号 标量 | 向量

对指定元素赋值后的输出信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `bus`

### 参数

#### **输出维度的数量** — 输出信号的维数 `1` (默认) | 整数

键入输出信号的维数。

##### 编程用法

|  |
| --- |
| **参数：**`NumberOfDimensions` |
| **类型：**字符向量 |
| **值：**整数 |
| **默认值：**`'1'` |

#### **索引模式** — 索引模式 **从 1 开始** (默认) | **从 0 开始**

选择索引模式。如果选择**从 1 开始**，则索引 1 指定输入向量的第一个元素。如果选择**从 0 开始**，则索引 0 指定输入向量的第一个元素。

##### 编程用法

|  |
| --- |
| **参数：**`IndexMode` |
| **类型：**字符向量 |
| **值：**`'Zero-based'` | `'One-based'` |
| **默认值：**`'One-based'` |

#### **索引选项** — 元素的索引方法 **索引向量(对话框)** (默认) | **全部赋值** | **索引向量(端口)** | **起始索引(对话框)** | **起始索引(端口)**

按维度定义信号元素的索引方式。从列表中，选择：

| 菜单项 | 操作 |
| --- | --- |
| **全部赋值** | 所有元素都被分配。 |
| **索引向量(对话框)** | 启用**索引**列。输入元素的索引。 |
| **索引向量(端口)** | 索引端口定义元素的索引。 |
| **起始索引(对话框)** | 启用**索引**列。输入要赋值的元素范围的起始索引。 |
| **起始索引(端口)** | 索引端口定义要赋值的元素范围的起始索引。 |

如果您为表中的任何维度选择**索引向量(端口)** 或**起始索引(端口)**，则可以为**初始化输出(Y)** 参数指定下列值之一：

- **使用输入端口 <Y0> 初始化**
- **指定表中每个维度的大小**

否则，`Y0` 始终初始化输出端口 `Y`。

**索引**和**输出大小**列显示为具有相关性。

##### 编程用法

|  |
| --- |
| **参数：**`IndexOptionArray` |
| **类型：**字符向量元胞数组 |
| **值：** `{'Assign all'}` | `{'Index vector (dialog)'}` | `{'Index vector (port)'}` | `{'Starting index (dialog)'}` | `{'Starting index (port)'}` |
| **默认值：**`{'Index vector (dialog)'}` |

对于字符向量而不是字符向量元胞数组，请使用 `IndexOptions`。

#### **索引** — 元素的索引 `1` (默认) | 整数

如果**索引选项**设置为**索引向量(对话框)**，则输入所需的每个元素的索引。

如果**索引选项**设置为**起始索引(对话框)**，则输入要选择的元素范围的起始索引。从起点开始的元素数量由此维度在 `U` 处的大小决定。

##### 编程用法

|  |
| --- |
| **参数：**`IndexParamArray` |
| **类型：**字符向量元胞数组 |
| **值：**整数 |
| **默认值：**`{'1'}` |

对于字符向量而不是字符向量元胞数组，请使用 `Indices`。

#### **输出大小** — 模块输出信号的宽度 `1` (默认) | 整数

输入模块输出信号的宽度。

##### 依赖关系

要启用此列，请将**初始化输出(Y)** 设置为**指定表中每个维度的大小**。

##### 编程用法

|  |
| --- |
| **参数：**`OutputSizeArray` |
| **类型：**字符向量元胞数组 |
| **值：**整数 |
| **默认值：**`{'1'}` |

对于字符向量而不是字符向量元胞数组，请使用 `OutputSizes`。

#### **初始化输出(Y)** — 如何初始化输出信号 **使用输入端口 <Y0> 初始化** (默认) | **指定表中每个维度的大小**

指定如何初始化输出信号。

- **使用输入端口 <Y0> 初始化** - 位于输入端口 `Y0` 的信号初始化输出。
- **指定表中每个维度的大小** - 要求您在**输出大小**参数中指定模块输出信号的宽度。如果输出具有未分配的元素，则这些元素的值未定义。

##### 依赖关系

要启用此参数，请为一个或多个维度将**索引选项**设置为**索引向量(端口)** 或**起始索引(端口)**。

##### 编程用法

|  |
| --- |
| **参数：**`OutputInitialize` |
| **类型：**字符向量 |
| **值**：`'Initialize using input port <Y0>'` | `'Specify size for each dimension in table'` |
| **默认值：**`'Initialize using input port <Y0>'` |

#### **未分配任何输出元素时的动作** — 产生警告或错误的选项 **警告** (默认) | **错误** | **无**

指定当您还有未分配的输出元素时是否生成警告或错误。选项包括：

- **警告** - Simulink 显示警告并继续进行仿真。
- **错误** - Simulink 终止仿真并显示错误。
- **无** - Simulink 不执行任何操作。

##### 依赖关系

要启用此参数，请为一个或多个维度将**索引选项**设置为**索引向量(端口)** 或**起始索引(端口)**。然后，将**初始化输出(Y)** 设置为**指定表中每个维度的大小**。

##### 编程用法

|  |
| --- |
| **参数：**`DiagnosticForDimensions` |
| **类型：**字符向量 |
| **值：**`'Error'` | `'Warning'` | `'None'` |
| **默认值：**`'Warning'` |

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

#### **在加速仿真中检查超范围索引** — 在加速和快速加速仿真模式下检查超范围索引值的选项 `off` (默认) | `on`

选中此复选框可让 Simulink 在加速或快速加速模式下进行仿真时检查是否有任何索引值超出输入信号的相关维度的有效索引范围。如果索引超出范围，Simulink 将停止仿真并显示错误消息。

**注意**

如果不选中此复选框，超出范围的索引值可能导致在加速或快速加速模式下仿真期间出现未定义的行为。

无论是否选中此复选框，在普通模式仿真期间 Simulink 都会执行此检查。

##### 编程用法

|  |
| --- |
| **参数：**`RuntimeRangeChecks` |
| **类型：**字符向量 |
| **值**：`'Off'` | `'On'` |
| **默认值**：`'Off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
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

**复数数据支持**

此模块支持复信号的代码生成。

**限制**

- 代码生成不支持可变大小信号。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

#### R2023a: 索引信号支持自定义宽度的整数

从 R2023a 开始，您可以自定义用于指定 Assignment 模块的索引信号值的整数宽度。

## Libraries

Simulink / Math Operations HDL Coder / Math Operations

## Description

The Assignment block assigns values to specified elements of the
signal. You specify the indices of the elements to be assigned values either by entering
the indices in the block dialog box or by connecting an external indices source or
sources to the block. The signal at the block data port, `U`, specifies
values to be assigned to `Y`. The block replaces the specified elements
of `Y` with elements from the data signal.

Based on the value you enter for the **Number of output dimensions**
parameter, a table of index options is displayed. Each row of the table corresponds to
one of the output dimensions in **Number of output dimensions**. For
each dimension, you can define the elements of the signal to work with. Specify a vector
signal as a 1-D signal and a matrix signal as a 2-D signal. To enable an external index
port, in the corresponding row of the table, set **Index Option** to
`Index vector (port)` or `Starting index
(port)`.

For example, assume a 5-D signal with a one-based index mode. The table in the
Assignment block dialog changes to include one row for each
dimension. If you define each dimension with the following entries:

| Row | Index Option | Index |
| --- | --- | --- |
| 1 | `Assign all` |  |
| 2 | `Index vector (dialog)` | `[1 3 5]` |
| 3 | `Starting index (dialog)` | `4` |
| 4 | `Starting index (port)` |  |
| 5 | `Index vector (port)` |  |

The assigned values are `Y(1:end,[1 3
5],4:3+size(U,3),Idx4:Idx4+size(U,4)-1,Idx5)=U`, where
`Idx4` and `Idx5` are the input ports for
dimensions 4 and 5.

When using the Assignment block in normal mode, Simulink® initializes block outputs to zero even if the model does not explicitly
initialize them. In accelerator mode, Simulink converts the model into an S-Function. This involves code generation. The
code generated may not do implicit initialization of block outputs. In such cases, you
must explicitly initialize the model outputs.

You can use the block to assign values to vector, matrix, or multidimensional
signals.

You can use an array of buses as an input signal to an Assignment
block.

### Assignment Block in Conditional Subsystem

If you place an Assignment block in a conditional subsystem block,
a hidden signal buffer (which is equivalent to a Signal Conversion block) is
inserted in many cases, and merging of signals from Assignment blocks
with partial writes can cause an error.

However, if you select the **Ensure outport is virtual**
parameter for the conditional subsystem Outport block, such cases are
supported and partial writes to arrays using Assignment blocks are
possible. See Ensure Output Port Is Virtual.

## Ports

### Input

### **Y0** — Initial value of output signal scalar | vector

The initial value of the output signal. If the signal specified at the
input data port (**U**) is not assigned a different value than
the initial value, then the output signal value at port **Y**
matches the initial value.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `Boolean` | `enumerated` | `bus`

### **U** — Input data port scalar | vector

Value assigned to the output element when specified.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `Boolean` | `enumerated` | `bus`

### **IndxN** — *N*th index signal scalar | vector

External port specifying an index for the assignment of the
corresponding output element.

You can specify integer of custom width (for example, a 15-bit integer
or 23-bit integer) as an index signal value. When you configure the
width of the integer, you must specify the **Mode** as
`Fixed point`, with **Word
length** less than or equal to 65,535,
**Slope** equal to 1, and **Bias**
equal to 0. For more information on specifying a fixed-point data type,
see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable an external index port, in the corresponding row of the
**Index Option** table, set **Index
Option** to `Index vector
(port)` or `Starting index
(port)`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Y** — Output signal with assigned values scalar | vector

The output signal with assigned values for the specified
elements.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `bus`

## Parameters

### **Number of output dimensions** — Number of dimensions of the output signal `1` (default) | integer

Enter the number of dimensions of the output signal.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `NumberOfDimensions` |
| **Type:** character vector |
| **Values:** integer |
| **Default:** `'1'` |

### **Index mode** — Index mode `One-based` (default) | `Zero-based`

Select the indexing mode. If `One-based` is
selected, an index of 1 specifies the first element of the input vector. If
`Zero-based` is selected, an index of 0
specifies the first element of the input vector.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `IndexMode` |
| **Type:** character vector |
| **Values:** `'Zero-based'` | `'One-based'` |
| **Default:** `'One-based'` |

### **Index Option** — Index method for elements `Index vector (dialog)` (default) | `Assign all` | `Index vector (port)` | `Starting index (dialog)` | `Starting index (port)`

Define, by dimension, how the elements of the signal are to be indexed.
From the list, select:

| Menu Item | Action |
| --- | --- |
| `Assign all` | All elements are assigned. |
| `Index vector (dialog)` | Enables the **Index** column. Enter the indices of elements. |
| `Index vector (port)` | The index port defines the indices of elements. |
| `Starting index (dialog)` | Enables the **Index** column. Enter the starting index of the range of elements to be assigned values. |
| `Starting index (port)` | The index port defines the starting index of the range of elements to be assigned values. |

If you choose `Index vector (port)` or
`Starting index (port)` for any dimension in
the table, you can specify one of these values for the **Initialize
output (Y)** parameter:

- `Initialize using input port
  <Y0>`
- `Specify size for each dimension in
  table`

Otherwise, `Y0` always initializes output port
`Y`.

The **Index** and **Output Size**
columns are displayed as relevant.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `IndexOptionArray` |
| **Type:** cell array of character vectors |
| **Values:** `{'Assign all'}` | `{'Index vector (dialog)'}` | `{'Index vector (port)'}` | `{'Starting index (dialog)'}` | `{'Starting index (port)'}` |
| **Default:** `{'Index vector (dialog)'}` |

For a character vector instead of a cell array of character vectors,
use `IndexOptions`.

### **Index** — Index of elements `1` (default) | integer

If the **Index Option** is `Index vector
(dialog)`, enter the index of each element you are
interested in.

If the **Index Option** is `Starting index
(dialog)`, enter the starting index of the range of
elements to be selected. The number of elements from the starting point is
determined by the size of this dimension at `U`.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `IndexParamArray` |
| **Type:** cell array of character vectors |
| **Values:** integers |
| **Default:** `{'1'}` |

For a character vector instead of a cell array of character vectors,
use `Indices`.

### **Output Size** — Width of block output signal `1` (default) | integer

Enter the width of the block output signal.

#### Dependencies

To enable this column, set **Initialize output
(Y)** to `Specify size for each dimension in
table`.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `OutputSizeArray` |
| **Type:** cell array of character vectors |
| **Values:** integers |
| **Default:** `{'1'}` |

For a character vector instead of a cell array of character vectors,
use `OutputSizes`.

### **Initialize output (Y)** — How to initialize output signal `Initialize using input port <Y0>` (default) | `Specify size for each dimension in the table`

Specify how to initialize the output signal.

- `Initialize using input port
  <Y0>` – Signal at the input port
  `Y0` initializes the output.
- `Specify size for each dimension in
  table` – Requires you to specify the width of
  the block output signal in the **Output Size**
  parameter. If the output has unassigned elements, the value of
  those elements is undefined.

#### Dependencies

To enable this parameter, set **Index Option** to
`Index vector (port)` or
`Starting index (port)` for one or more
dimensions.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `OutputInitialize` |
| **Type:** character vector |
| **Values:** `'Initialize using input port <Y0>'` | `'Specify size for each dimension in table'` |
| **Default:** `'Initialize using input port <Y0>'` |

### **Action if any output element is not assigned** — Option to produce warning or error `Warning` (default) | `Error` | `None`

Specify whether to produce a warning or error if you have not assigned all
output elements. Options include:

- `Warning` — Simulink displays a warning and continues the
  simulation.
- `Error` — Simulink terminates the simulation and displays an
  error.
- `None` — Simulink takes no action.

#### Dependencies

To enable this parameter, set **Index Option** to
`Index vector (port)` or
`Starting index (port)` for one or more
dimensions. Then, set **Initialize output (Y)** to
`Specify size for each dimension in
table`.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `DiagnosticForDimensions` |
| **Type:** character vector |
| **Values:** `'Error'` | `'Warning'` | `'None'` |
| **Default:** `'Warning'` |

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

### **Check for out-of-range index in accelerated simulation** — Option to check for out-of-range index values in accelerator and rapid accelerator simulation modes `off` (default) | `on`

Select this check box to have Simulink check during simulation in accelerator or rapid accelerator
mode whether any index values are outside the range of valid indices for the
relevant dimension of the input signal. If an index is out of range,
Simulink stops the simulation and displays an error message.

**Note**

If you do not select this check box, out-of-range index values
could lead to undefined behavior during accelerator or rapid
accelerator mode simulation.

Simulink performs this check during normal mode simulation regardless
of whether you select this check box.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `RuntimeRangeChecks` |
| **Type:** character vector |
| **Values:** `'Off'` | `'On'` |
| **Default:** `'Off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
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

**Complex Data Support**

This block supports code generation for complex signals.

**Restrictions**

- Variable-size signals are not supported for code generation.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2023a: Index signal supports integer of custom width

Starting in R2023a, you can customize the width of the integer that you use to
specify the index signal value for the Assignment block.
