---
type: simulink-block
title: 'Expand Scalar'
family: matrix-operations
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'expandscalar'
---

# Expand Scalar

Create matrix from scalar using scalar expansion

## 中文

使用标量扩展从标量创建矩阵

### 库

Simulink / Matrix Operations

### 描述

Expand Scalar 模块输出一个标量扩展矩阵，其中矩阵中的每个元素都具有相同的值。

### 端口

#### 输出

#### **Port\_1** — 标量扩展矩阵 标量 | 向量 | 矩阵

标量扩展矩阵，以标量、向量或矩阵形式返回。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `bus` | `Boolean` | `fixed point`

### 参数

要交互式编辑模块参数，请使用 Property Inspector。从 Simulink® Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

#### **Element value** — 矩阵元素值 `1`（默认）| 标量

将扩展矩阵的矩阵元素值指定为标量。元素值可以是 `struct`。

**可调：** Yes

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ElementValue` |
| **值：** | 1（默认）| 标量 |
| **数据类型：** | `char` |

#### **Output dimensions** — 输出矩阵的维度 `5`（默认）| 标量 | 二元素向量

将输出矩阵的维度指定为标量或向量。

- 正整数标量创建无方向向量。
- 二维向量创建有方向向量。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutputDimensions` |
| **值：** | `'5'`（默认）| 标量 | 二元素向量 |
| **数据类型：** | `char` |

#### **Output data type** — 输出数据类型 `double`（默认）| `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `Inherit: Inherit via back propagation` | `<data type expression>`

指定此模块的输出数据类型。您可以选择以下选项之一：

- 继承数据类型的规则，例如 `Inherit: Inherit via back propagation`。选择此选项时，输出数据类型和缩放与下一个下游模块匹配。
- 内置数据类型，如 `double`。
- 计算结果为有效数据类型的表达式，例如 `fixdt(1,16)`。

有关设置数据类型参数的帮助，请单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**。

有关详细信息，请参阅 Control Data Types of Signals。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'double'`（默认）| `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `Inherit: Inherit via back propagation` | `<data type expression>` |
| **数据类型：** | `char` |

#### **Mode** — 数据类型模式 `Inherit`（默认）| `Built in` | `Fixed point` | `Expression`

选择希望如何指定 **Output data type** 的数据类型属性。

- `Inherit` — 指定用于继承数据类型的规则，例如 `Inherit: Same as input`。
- `Built in`— 指定内置数据类型，例如 `double`。
- `Fixed point` — 指定数据类型的定点属性。
- `Expression` — 指定计算结果为有效数据类型的表达式，例如 `fixdt(1,16)`。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### **Signedness** — 定点数据的符号性 `Signed`（默认）| `Unsigned`

指定定点数据是有符号还是无符号。`Signed` 数据可以表示正值和负值。`Unsigned` 数据仅表示正值。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### **Scaling** — 定点数据的缩放方法 `Best precision`（默认）| `Binary point`

指定定点数据的缩放方法，以避免溢出情况并最小化量化误差。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

#### **Word length** — 保存量化整数的字长位大小 `16`（默认）| 从 2 到 65,535 的整数

将保存量化整数的字长位大小指定为从 2 到 65,535 的正整数。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

#### **Fraction length** — 定点数据类型的小数长度 `0`（默认）| 整数标量

将定点数据类型的小数长度指定为正整数或负整数标量。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`，并将 **Scaling** 设置为 `Binary point`。

#### **Data type override** — 数据类型覆盖模式 `Inherit`（默认）| `Off`

选择此信号的数据类型覆盖模式。您可以选择：

- `Inherit` — 继承为模型指定的数据类型覆盖设置。
- `Off` — 忽略为模型指定的数据类型覆盖设置，并使用您指定的定点数据类型。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Built in` 或 `Fixed point`。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### **Sample time** — 输出采样周期 `1`（默认）| 标量

将输出的离散采样周期指定为实值标量。

#### 依赖关系

要启用此参数，请清除 **Inherit output port attributes from input port** 复选框。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `'1'`（默认）| 标量 |
| **数据类型：** | `char` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 版本历史

**在 R2024a 中引入**

#### R2024b：Expand Scalar 模块支持 `struct` 扩展

Expand Scalar 模块现在支持使用 Simulink 总线数据类型的 MATLAB® `struct` 扩展。

## Libraries

Simulink / Matrix Operations

## Description

The Expand Scalar block outputs a scalar-expanded matrix where each element
in the matrix has the same value.

## Ports

### Output

### **Port\_1** — Scalar-expanded matrix scalar | vector | matrix

Scalar-expanded matrix, returned as a scalar, vector, or matrix.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `bus` | `Boolean` | `fixed point`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Element value** — Matrix element value `1` (default) | scalar

Specify the matrix element value as a scalar for the expanded matrix. Element value
can be a `struct`.

**Tunable:** Yes

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ElementValue` |
| **Values:** | 1 (default) | scalar |
| **Data Types:** | `char` |

### **Output dimensions** — Dimension of output matrix `5` (default) | scalar | two-element vector

Specify the dimension of output matrix as a scalar or vector.

- A positive integer scalar creates an unoriented vector.
- A 2-D vector creates an oriented vector.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutputDimensions` |
| **Values:** | `'5'` (default) | scalar | two-element vector |
| **Data Types:** | `char` |

### **Output data type** — Output data type `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `Inherit: Inherit via back propagation` | `<data type expression>`

Specify the output data type for this block. You can select one of these
options:

- A rule that inherits a data type, for example, `Inherit: Inherit via
  back propagation`. When you select this option, the output data type
  and scaling matches that of the next downstream block.
- A built-in data type, such as `double`.
- An expression that evaluates to a valid data type, for example,
  `fixdt(1,16)`.

For help setting data type parameters, display the **Data Type
Assistant** by clicking the **Show data type assistant**
button .

See Control Data Types of Signals for more
information.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `'double'` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `Inherit: Inherit via back propagation` | `<data type expression>` |
| **Data Types:** | `char` |

### **Mode** — Data type mode `Inherit` (default) | `Built in` | `Fixed point` | `Expression`

Select how you would like to specify the data type properties of the
**Output data type**.

- `Inherit` — Specify a rule for inheriting a
  data type, for example, `Inherit: Same as input`.
- `Built in`— Specify a built-in data type, for
  example, `double`.
- `Fixed point` — Specify the fixed-point
  attributes of the data type.
- `Expression` — Specify an expression that
  evaluates to a valid data type, for example,
  `fixdt(1,16)`.

For more information, see Specify Data Types Using Data Type Assistant.

### **Signedness** — Signedness of fixed-point data `Signed` (default) | `Unsigned`

Specify whether the fixed-point data is signed or unsigned.
`Signed` data can represent positive and negative values.
`Unsigned` data represents positive values only. For more
information, see Specify Data Types Using Data Type Assistant.

### **Scaling** — Method for scaling fixed-point data `Best precision` (default) | `Binary point`

Specify the method for scaling fixed-point data to avoid overflow conditions and
minimize quantization errors. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set **Mode** to `Fixed
point`.

### **Word length** — Bit size of word that holds quantized integer `16` (default) | integer from 2 to 65,535

Specify the bit size of the word that holds the quantized integer as a positive
integer from 2 to 65,535. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set **Mode** to `Fixed
point`.

### **Fraction length** — Fraction length for fixed-point data type `0` (default) | integer scalar

Specify the fraction length of the fixed-point data type as a positive or negative
integer scalar.

#### Dependencies

To enable this parameter, set **Mode** to `Fixed
point` and **Scaling** to `Binary
point`.

### **Data type override** — Data type override mode `Inherit` (default) | `Off`

Select the data type override mode for this signal. You can select:

- `Inherit` — Inherits the data type override setting
  specified for the model.
- `Off` — Ignores the data type override setting
  specified for the model and uses the fixed-point data type you specify.

#### Dependencies

To enable this parameter, set **Mode** to `Built
in` or `Fixed point`. For more information,
see Specify Data Types Using Data Type Assistant.

### **Sample time** — Output sample period `1` (default) | scalar

Specify the discrete sample period of the output as a real-valued scalar.

#### Dependencies

To enable this parameter, clear the **Inherit output port attributes from
input port** check box.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `'1'` (default) | scalar |
| **Data Types:** | `char` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

### R2024b: Expand Scalar block supports `struct` expansion

The Expand Scalar block now supports MATLAB®
`struct` expansion with a Simulink bus data type.
