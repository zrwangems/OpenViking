---
type: simulink-block
title: 'Identity Matrix'
family: matrix-operations
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'identitymatrix'
---

# Identity Matrix

Generate matrix with ones on main diagonal and ground values elsewhere

## 中文

生成主对角线为 1、其他位置为 0 的矩阵

### 库

Simulink / Matrix Operations

### 说明

Identity Matrix 模块输出一个单位矩阵，类似于 MATLAB® `eye` 函数。该模块生成一个方阵或矩形矩阵，主对角线为 1，其他位置为 0。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

用于确定输出矩阵维度的输入信号，指定为标量、向量或矩阵。当输入信号是 *M*×*N* 矩阵时，该模块生成一个 *M*×*N* 矩阵输出，其采样周期与输入相同。输入矩阵中的值将被忽略。

#### 依赖关系

要启用此端口，请选中 **从输入端口继承输出端口属性** 复选框。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### 输出

#### **Port\_1** — 单位矩阵 标量 | 向量 | 矩阵

单位矩阵，指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 参数

#### **从输入端口继承输出端口属性** — 用于输出端口从输入端口继承属性的选项 off（默认） | on

选中此复选框可使输出端口从输入端口继承其维度、采样周期和数据类型。否则，清除此复选框。

#### 编程使用

|  |
| --- |
| **模块参数：** `InheritOutputPortAttributes` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |

#### **输出维度** — 输出矩阵的大小 `5`（默认） | 标量 | 二元素向量

输出矩阵中的行数和列数。可以指定：

- 一个正整数标量 *M*，用于创建 *M*×*M* 方阵输出。
- 一个正整数向量 [*M* *N*]，用于创建 *M*×*N* 输出。

#### 依赖关系

要启用此参数，请清除 **从输入端口继承输出端口属性** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数：** `OutputDimensions` |
| **类型：** character vector |
| **值：** 标量 | 二元素向量 |
| **默认：** `'5'` |

#### **输出数据类型** — 输出数据类型 `double`（默认） | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `Inherit: Inherit via back propagation` | `<data type expression>`

指定此模块的输出数据类型。您可以选择以下选项之一：

- 用于继承数据类型的规则，例如 `Inherit: Inherit via back propagation`。选择此选项时，输出数据类型和定标将与下一个下游模块匹配。
- 内置数据类型，例如 `double`。
- 求值结果为有效数据类型的表达式，例如 `fixdt(1,16)`。

有关设置数据类型参数的帮助，请单击 **显示数据类型助手** 按钮以显示 **数据类型助手**。

有关详细信息，请参阅控制信号的数据类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | | `'fixdt(1,16,0)'` | `'<data type expression>'` |
| **默认**：`'double'` |

#### **模式** — 数据类型模式 `Inherit`（默认） | `Built in` | `Fixed point` | `Expression`

选择希望如何指定 **输出数据类型** 的数据类型属性。可以选择：

- `Inherit` — 指定用于继承数据类型的规则，例如 `Inherit: Same as input`。
- `Built in`— 指定内置数据类型，例如 `double`。
- `Fixed point` — 指定数据类型的定点属性。
- `Expression` — 指定求值结果为有效数据类型的表达式，例如 `fixdt(1,16)`。

有关详细信息，请参阅使用数据类型助手指定数据类型。

#### **符号性** — 定点数据的符号性 `Signed`（默认） | `Unsigned`

指定定点数据是有符号还是无符号。`Signed` 数据可以表示正值和负值，但 `Unsigned` 数据仅表示正值。有关详细信息，请参阅使用数据类型助手指定数据类型。

#### **定标** — 定点数据的定标方法 `Best precision`（默认） | `Binary point`

指定定点数据的定标方法，以避免溢出情况并最小化量化误差。有关详细信息，请参阅使用数据类型助手指定数据类型。

#### 依赖关系

要启用此参数，请将 **模式** 设置为 `Fixed point`

#### **字长** — 保存量化整数的字的位大小 `16`（默认） | 从 2 到 65,535 的整数

将保存量化整数的字的位大小指定为从 2 到 65,535 的正整数。有关详细信息，请参阅使用数据类型助手指定数据类型。

#### 依赖关系

要启用此参数，请将 **模式** 设置为 `Fixed point`。

#### **小数长度** — 定点数据类型的小数长度 `0`（默认） | 整数标量

将定点数据类型的小数长度指定为正整数或负整数标量。

#### 依赖关系

要启用此参数，请将 **模式** 设置为 `Fixed point`，并将 **定标** 设置为 `Binary point`。

#### **数据类型覆盖** — 数据类型覆盖模式 `Inherit`（默认） | `Off`

选择此信号的数据类型覆盖模式。可以选择：

- `Inherit` — 继承为模型指定的数据类型覆盖设置。
- `Off` — 忽略为模型指定的数据类型覆盖设置，并使用您指定的定点数据类型。

#### 依赖关系

要启用此参数，请将 **模式** 设置为 `Built in` 或 `Fixed point`。有关详细信息，请参阅使用数据类型助手指定数据类型。

#### **采样时间** — 输出采样周期 `1`（默认） | 标量

输出的离散采样周期，指定为实值标量。

#### 依赖关系

要启用此参数，请清除 **从输入端口继承输出端口属性** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** character vector |
| **值：** 标量或向量 |
| **默认：** `'1'` |

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

**在 R2021b 中引入**

#### R2022a：Identity Matrix 模块已添加到 Simulink Matrix Operations 库

Identity Matrix 模块已从 **DSP System Toolbox** > **Math Functions** > **Matrices and Linear**  > **Matrix Operations** 库中移除。要获得等效功能，请使用 **Simulink** > **Matrix Operations** 库中的 Identity Matrix 模块。所有现有模型继续工作。

## Libraries

Simulink / Matrix Operations

## Description

The Identity Matrix block outputs an identity matrix, similar to the
MATLAB®
`eye` function. The block generates a square or rectangular matrix with ones on
the main diagonal and zeros elsewhere.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal used to determine dimensions of the output matrix, specified as a
scalar, vector, or matrix. When the input signal is an
*M*-by-*N* matrix, the block generates an
*M*-by-*N* matrix output with the same sample
period as the input. The values in the input matrix are ignored.

#### Dependencies

To enable this port, select the **Inherit output port attributes from
input port** check box.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Identity matrix scalar | vector | matrix

Identity matrix, specified as a scalar, vector, or matrix.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### **Inherit output port attributes from input port** — Option for output port to inherit attributes from input port off (default) | on

Select this check box for the output port to inherit its dimensions, sample period,
and data type from the input port. Otherwise, clear this check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InheritOutputPortAttributes` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **Output dimensions** — Size of output matrix `5` (default) | scalar | two-element vector

The number of rows and columns in the output matrix. You can specify:

- A positive integer scalar *M* to create a square
  *M*-by-*M* output.
- A vector of positive integers, [*M*
  *N*], to create an *M*-by-*N*
  output.

#### Dependencies

To enable this parameter, clear the **Inherit output port attributes from
input port** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputDimensions` |
| **Type:** character vector |
| **Values:** scalar | two-element vector |
| **Default:** `'5'` |

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

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | | `'fixdt(1,16,0)'` | `'<data type expression>'` |
| **Default**: `'double'` |

### **Mode** — Data type mode `Inherit` (default) | `Built in` | `Fixed point` | `Expression`

Select how you would like to specify the data type properties of the
**Output data type**. You can choose:

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
`Signed` data can represent positive and negative values, but
`Unsigned` data represents positive values only. For more
information, see Specify Data Types Using Data Type Assistant.

### **Scaling** — Method for scaling fixed-point data `Best precision` (default) | `Binary point`

Specify the method for scaling your fixed-point data to avoid overflow conditions
and minimize quantization errors. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set **Mode** to `Fixed
point`

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

The discrete sample period of the output, specified as a real-valued scalar.

#### Dependencies

To enable this parameter, clear the **Inherit output port attributes from
input port** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** scalar or vector |
| **Default:** `'1'` |

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

**Introduced in R2021b**

### R2022a: Identity Matrix Block Added to Simulink Matrix Operations Library

The Identity Matrix block has been removed from the **DSP System Toolbox** > **Math Functions** > **Matrices and Linear**  > **Matrix Operations** library. For equivalent functionality, use the Identity Matrix
block in the **Simulink** > **Matrix Operations** library. All existing models continue to work.
