---
type: simulink-block
title: 'Relational Operator'
family: logic-and-bit-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'relationaloperator'
---

# Relational Operator

Perform specified relational operation on inputs

## 中文

对输入执行指定的关系运算

### 所属库

Simulink / Commonly Used Blocks Simulink / Logic and Bit Operations HDL Coder / Commonly Used Blocks HDL Coder / HDL Floating Point Operations HDL Coder / Logic and Bit Operations

### 描述

Relational Operator 模块对输入执行指定的关系运算。为**关系运算符**参数选择的值确定模块是接受一个还是两个输入信号。

#### 双输入模式

默认情况下，Relational Operator 模块使用您指定的**关系运算符**参数比较两个输入。第一个输入对应于上面的输入端口，第二个输入对应于下面的输入端口。（有关各种模块方向的端口顺序的描述，请参阅标识旋转或翻转模块上的端口位置。）

您可以在双输入模式中指定以下运算之一：

| 运算 | 描述 |
| --- | --- |
| `==` | 如果第一个输入等于第二个输入，则为 TRUE |
| `~=` | 如果第一个输入不等于第二个输入，则为 TRUE |
| `<` | 如果第一个输入小于第二个输入，则为 TRUE |
| `<=` | 如果第一个输入小于或等于第二个输入，则为 TRUE |
| `>=` | 如果第一个输入大于或等于第二个输入，则为 TRUE |
| `>` | 如果第一个输入大于第二个输入，则为 TRUE |

您可以将输入指定为标量、数组或者标量与数组的组合。

| 对于... | 输出为... |
| --- | --- |
| 标量输入 | 标量 |
| 数组输入 | 具有相同维度的数组，其中每个元素是对输入数组逐元素比较的结果 |
| 混合标量和数组输入 | 数组，其中每个元素是将标量与对应的数组元素进行比较的结果 |

如果关系运算可以在硬件板上高效且准确地表示，则使用这种高效表示。否则，使用溢出饱和与指定的舍入模式将两个操作数都转换为一种公共类型。

您可以使用**输出数据类型**参数指定输出的数据类型。如果为 true，则输出为 `1`；如果为 false，则输出为 `0`。

**提示**

选择准确表示零的输出数据类型。满足此条件的数据类型包括有符号整数和无符号整数，以及所有浮点数据类型。

#### 单输入模式

当您为**关系运算符**选择下列运算之一时，模块将切换到单输入模式。

| 运算 | 描述 |
| --- | --- |
| `isInf` | 如果输入为 `Inf`，则为 TRUE |
| `isNaN` | 如果输入为 `NaN`，则为 TRUE |
| `isFinite` | 如果输入为有限值，则为 TRUE |

对于非浮点输入，模块将生成以下输出。

| 数据类型 | 运算 | 模块输出 |
| --- | --- | --- |
| - 定点 - 布尔 - 内置整数 | `isInf` | False |
| `isNaN` | False |
| `isFinite` | true |

#### 数据类型传播的规则

当您的模块有一个或多个输入端口未指定数据类型时，将按以下规则进行数据类型传播。

| 当模块位于... | 而且... | 模块使用... |
| --- | --- | --- |
| 双输入模式 | 两个输入端口均未指定数据类型 | `double` 作为两个输入的默认数据类型 |
| 一个输入端口未指定数据类型 | 指定了数据类型的输入端口的数据类型作为另一个端口的默认数据类型 |
| 单输入模式 | 输入端口未指定数据类型 | `double` 作为输入的默认数据类型 |

### 端口

#### 输入

#### **Port\_1** — 第一个输入信号 标量 | 向量 | 矩阵

第一个输入信号，指定为标量、向量或矩阵。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **Port\_2** — 第二个输入信号 标量 | 向量 | 矩阵

第二个输入信号，指定为标量、向量或矩阵。

##### 依赖关系

要启用此端口，请将**关系运算符**设置为 **==**、**~=**、**<**、**<=**、**>=** 或 **>**。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

输出信号，由 0 和 1 组成，具有与输入相同的维度。使用**输出数据类型**参数控制输出数据类型。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 参数

#### 常设

#### **关系运算符** — 关系运算符 **<=** (默认) | **~=** | **==** | **<** | **>=** | **>** | **isInf** | **isNaN** | **isFinite**

指定比较两个输入的运算，或确定一个输入的信号类型。

- **==** - 如果第一个输入等于第二个输入，则为 TRUE
- **~=** - 如果第一个输入不等于第二个输入，则为 TRUE
- **<** - 如果第一个输入小于第二个输入，则为 TRUE
- **<=** - 如果第一个输入小于或等于第二个输入，则为 TRUE
- **>=** - 如果第一个输入大于或等于第二个输入，则为 TRUE
- **>** - 如果第一个输入大于第二个输入，则为 TRUE
- **isInf** - 如果输入为 `Inf`，则为 TRUE
- **isNaN** - 如果输入为 `NaN`，则为 TRUE
- **isFinite** - 如果输入为有限值，则为 TRUE

**==** 和 **~=** 支持使用复数进行仿真和代码生成。

##### 编程用法

|  |
| --- |
| **模块参数**：`Operator` |
| **类型：**字符向量 |
| **值：**`'==' | '~=' | '<' | '<=' | '>=' | '>' | 'isInf' | 'isNaN' | 'isFinite'` |
| **默认值：**`'<='` |

#### **启用过零检测** — 启用过零检测 `on` (默认) | `off`

选择此项以启用过零检测。有关详细信息，请参阅过零检测。

##### 编程用法

|  |
| --- |
| **参数：**`ZeroCross` |
| **类型：**字符向量、字符串 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'on'` |

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

#### **要求所有输入具有相同的数据类型** — 要求所有输入都有相同的数据类型 `off` (默认) | `on`

若要求所有模块输入具有相同的数据类型，请选中此复选框。清除此复选框后，输入可以具有不同数据类型。

##### 依赖关系

将**关系运算符**设置为 **isInf**、**isNaN** 或 **isFinite** 时，此复选框不可用，因为在这些模式下，模块只有一个输入端口。

##### 编程用法

|  |
| --- |
| **模块参数**：`InputSameDT` |
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

#### **整数舍入模式** — 定点运算的舍入模式 **最简** (默认) | **收敛** | **向下** | **最邻近值** | **舍入** | **向上** | **零**

指定定点运算的舍入模式。您可以选择：

**向上**
:   朝正无穷方向舍入正数和负数。等同于 MATLAB® `ceil` 函数。

**收敛**
:   将数值舍入到最邻近的可表示值。如果出现结值，则舍入到最邻近的偶数整数。等同于 Fixed-Point Designer™ `convergent` 函数。

**向下**
:   朝负无穷方向舍入正数和负数。等同于 MATLAB `floor` 函数。

**最邻近值**
:   将数值舍入到最邻近的可表示值。如果出现结值，则朝正无穷方向舍入。等同于 Fixed-Point Designer `nearest` 函数。

**舍入**
:   将数值舍入到最邻近的可表示值。如果出现结值，则将正数朝正无穷方向舍入，将负数朝负无穷方向舍入。等同于 Fixed-Point Designer `round` 函数。

**最简**
:   在向负无穷大方向舍入和向零舍入之间选择，以生成尽可能有效的舍入代码。

**零**
:   将数值向零舍入。等同于 MATLAB `fix` 函数。

有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

##### 编程用法

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型：**字符向量 |
| **值：**`'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值：**`'Simplest'` |

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

- 当您选择 **inherit** 时，Simulink 从信号的上下文（即：从 Simulink® 中使用该信号的模块、`Simulink.Signal` 对象或 Stateflow® 图）中继承数据类型覆盖设置。
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
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `是` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

| 原生浮点 | |
| --- | --- |
| **LatencyStrategy** | 指定对于浮点运算符是否将设计中的模块映射到 `inherit`、`Max`、`Min`、`Zero` 或 `Custom`。默认值为 **inherit**。另请参阅LatencyStrategy (HDL Coder)。 |
| **NFPCustomLatency** | 要指定值，请将 **LatencyStrategy** 设置为 `Custom`。HDL Coder 会增加延迟，其值等于您为 **NFPCustomLatency** 设置指定的值。另请参阅NFPCustomLatency (HDL Coder)。 |

**复数数据支持**

仿真和代码生成支持 `~=` 和 `==` 运算符。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Commonly Used Blocks Simulink / Logic and Bit Operations HDL Coder / Commonly Used Blocks HDL Coder / HDL Floating Point Operations HDL Coder / Logic and Bit Operations

## Description

The Relational Operator block performs the specified relational operation on
the input. The value you choose for the **Relational operator**
parameter determines whether the block accepts one or two input signals.

### Two-Input Mode

By default, the Relational Operator block compares two inputs using the
**Relational operator** parameter that you specify. The first
input corresponds to the top input port and the second input to the bottom input
port. (See Identify Port Location on Rotated or Flipped Block
for a description of the port order for various block orientations.)

You can specify one of the following operations in two-input mode:

| Operation | Description |
| --- | --- |
| `==` | True if the first input is equal to the second input |
| `~=` | True if the first input is not equal to the second input |
| `<` | True if the first input is less than the second input |
| `<=` | True if the first input is less than or equal to the second input |
| `>=` | True if the first input is greater than or equal to the second input |
| `>` | True if the first input is greater than the second input |

You can specify inputs as scalars, arrays, or a combination of a scalar and an array.

| For... | The output is... |
| --- | --- |
| Scalar inputs | A scalar |
| Array inputs | An array of the same dimensions, where each element is the result of an element-by-element comparison of the input arrays |
| Mixed scalar and array inputs | An array, where each element is the result of a comparison between the scalar and the corresponding array element |

If the relational operation can be efficiently and accurately represented on the
hardware board, this efficient representation is used. Otherwise, both operands are
cast to a common type using overflow saturation and the specified rounding
mode.

You can specify the output data type using the **Output data type**
parameter. The output equals `1` for true and `0`
for false.

**Tip**

Select an output data type that represents zero exactly. Data types that satisfy this condition include signed and unsigned integers and any floating-point data type.

### One-Input Mode

When you select one of the following operations
for **Relational operator**, the block switches to one-input mode.

| Operation | Description |
| --- | --- |
| `isInf` | True if the input is `Inf` |
| `isNaN` | True if the input is `NaN` |
| `isFinite` | True if the input is finite |

For an input that is not floating point, the block produces the following output.

| Data Type | Operation | Block Output |
| --- | --- | --- |
| - Fixed point - Boolean - Built-in integer | `isInf` | False |
| `isNaN` | False |
| `isFinite` | True |

### Rules for Data Type Propagation

The following rules apply for data type propagation when your block has one or more input ports with unspecified data types.

| When the block is in... | And... | The block uses... |
| --- | --- | --- |
| Two-input mode | Both input ports have unspecified data types | `double` as the default data type for both inputs |
| One input port has an unspecified data type | The data type from the specified input port as the default data type of the other port |
| One-input mode | The input port has an unspecified data type | `double` as the default data type for the input |

## Ports

### Input

### **Port\_1** — First input signal scalar | vector | matrix

First input signal, specified as a scalar, vector, or matrix.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_2** — Second input signal scalar | vector | matrix

Second input signal, specified as a scalar, vector, or matrix.

#### Dependencies

To enable this port, set the **Relational operator** to
`==`, `~=`,
`<`,
`<=`,
`>=`, or
`>`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output signal, consisting of zeros and ones, with the same dimensions
as the input. You control the output data type with the **Output
data type** parameter.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main

### **Relational operator** — Relational operator `<=` (default) | `~=` | `==` | `<` | `>=` | `>` | `isInf` | `isNaN` | `isFinite`

Specify the operation for comparing two inputs or determining the
signal type of one input.

- `==` — True if the first input is
  equal to the second input
- `~=` — True if the first input is not
  equal to the second input
- `<` — True if the first input is
  less than the second input
- `<=` — True if the first input is
  less than or equal to the second input
- `>=` — True if the first input is
  greater than or equal to the second input
- `>` — True if the first input is
  greater than the second input
- `isInf` — True if the input is
  `Inf`
- `isNaN` — True if the input is
  `NaN`
- `isFinite` — True if the input is
  finite

`==` and `~=`
support complex numbers for simulation and code generation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Operator` |
| **Type:** character vector |
| **Values:** `'==' | '~=' | '<' | '<=' | '>=' | '>' | 'isInf' | 'isNaN' | 'isFinite'` |
| **Default:** `'<='` |

### **Enable zero-crossing detection** — Enable zero-crossing detection `on` (default) | `off`

Select to enable zero-crossing detection. For more information, see Zero-Crossing Detection.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `ZeroCross` |
| **Type:** character vector, string |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

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

### **Require all inputs to have the same data type** — Require all inputs to have same data type `off` (default) | `on`

To require that all block inputs have the same data type, select this
check box. When you clear this check box, the inputs can have different
data types.

#### Dependencies

This check box is not available when you set **Relational operator**
to `isInf`,
`isNaN`, or
`isFinite` because, in those modes, the
block only has one input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputSameDT` |
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

### **Integer rounding mode** — Rounding mode for fixed-point operations `Simplest` (default) | `Convergent` | `Floor` | `Nearest` | `Round` | `Ceiling` | `Zero`

Specify the rounding mode for fixed-point operations. You can
select:

`Ceiling`
:   Rounds positive and negative numbers toward positive
    infinity. Equivalent to the MATLAB®
    `ceil` function.

`Convergent`
:   Rounds number to the nearest representable value. If a tie
    occurs, rounds to the nearest even integer. Equivalent to
    the Fixed-Point Designer™
    `convergent` function.

`Floor`
:   Rounds positive and negative numbers toward negative
    infinity. Equivalent to the MATLAB
    `floor` function.

`Nearest`
:   Rounds number to the nearest representable value. If a tie
    occurs, rounds toward positive infinity. Equivalent to the
    Fixed-Point Designer
    `nearest` function.

`Round`
:   Rounds number to the nearest representable value. If a tie
    occurs, rounds positive numbers toward positive infinity and
    rounds negative numbers toward negative infinity. Equivalent
    to the Fixed-Point Designer
    `round` function.

`Simplest`
:   Chooses between rounding toward floor and rounding toward
    zero to generate rounding code that is as efficient as
    possible.

`Zero`
:   Rounds number toward zero. Equivalent to the MATLAB
    `fix` function.

For more information, see Rounding Modes (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **Default:** `'Simplest'` |

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
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

| Native Floating Point | |
| --- | --- |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, `Zero`, or `Custom` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |
| **NFPCustomLatency** | To specify a value, set **LatencyStrategy** to `Custom`. HDL Coder adds latency equal to the value that you specify for the **NFPCustomLatency** setting. See also NFPCustomLatency (HDL Coder). |

**Complex Data Support**

The `~=` and `==` operators are supported for simulation
and code generation.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
