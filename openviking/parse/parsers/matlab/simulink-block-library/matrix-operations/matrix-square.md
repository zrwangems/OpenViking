---
type: simulink-block
title: 'Matrix Square'
family: matrix-operations
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'matrixsquare'
---

# Matrix Square

Compute square of input matrix

## 中文

计算输入矩阵的平方

### 库

Simulink / Matrix Operations

### 说明

Matrix Square 模块通过使用 Hermitian 转置进行左乘，计算 *M*×*N* 输入矩阵 *u* 的平方。等效的 MATLAB® 代码为：

    y = u' * u

该模块将长度为 *M* 的未定向向量输入视为 *M*×1 矩阵。当输入为 *M*×*N* 矩阵时，模块的输出为 *N*×*N* 矩阵。

#### 应用

Matrix Square 模块可用于多种应用：

- 一般矩阵平方 — Matrix Square 模块计算输出矩阵 *y*，而无需显式构造 *u'*。因此，它比其他计算矩阵平方的方法更高效。
- 平方和 — 当输入为列向量（*N*=1）时，模块的操作等效于乘加（MAC）过程，或内积。输出是输入的平方和，并且始终为实数标量。
- 相关矩阵 — 当输入为行向量（*M*=1）时，输出 *y* 是对称自相关矩阵，或外积。

### 端口

#### 输入

#### **Port\_1** — 输入矩阵 *M*×1 矩阵 | 1×*N* 矩阵 | *M*×*N* 矩阵

输入矩阵，指定为 *M*×1、1×*N* 或 *M*×*N* 矩阵。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `fixed point`

#### 输出

#### **Port\_1** — 输出矩阵 *M*×*M* 矩阵 | *N*×*N* 矩阵

输出矩阵，返回为 *N*×*N* 或 *M*×*M* 矩阵。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### **输出最小值** — 用于范围检查的最小输出值 `[]`（默认）| scalar

Simulink® 检查的用于范围检查的最小输出值。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges）
- 定点数据类型的自动定标

#### 程序化使用

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型**：character vector |
| **值**：`'[ ]'`| scalar |
| **默认**：`'[ ]'` |

#### **输出最大值** — 用于范围检查的最大输出值 `[]`（默认）| scalar

Simulink® 检查的用于范围检查的最大输出值。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges）
- 定点数据类型的自动定标

#### 程序化使用

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：character vector |
| **值**：`'[ ]'`| scalar |
| **默认**：`'[ ]'` |

#### **输出数据类型** — 输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Inherit via back propagation` | `Inherit: Same as input` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `fixdt(1,16,0)` | `<data type expression>`

指定此模块的输出数据类型。

您可以选择以下选项之一：

- 指定如何继承数据类型的规则，例如 `Inherit: Inherit via internal rule`。有关此规则的详细信息，请参阅 Inherit via Internal Rule (DSP System Toolbox)。
- 计算结果为有效数据类型的表达式，例如 `fixdt([],16,0)`

点击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Output data type** 参数。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 程序化使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Same as input'` | `'Inherit: Inherit via internal rule'`| `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | `'<data type expression>'` |
| **默认**：`'Inherit: Inherit via internal rule'` |

#### **锁定输出数据类型设置以防止定点工具更改** — 输出数据类型锁定 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块掩码上指定的 **Output data type**。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** character vector |
| **值：** `'off' | 'on'` |
| **默认：** `'off'` |

#### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择用于定点运算的舍入模式 (DSP System Toolbox)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** character vector |
| **值：** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认：** `'Floor'` |

#### **在整数溢出时饱和** — 发生整数溢出时的行为 `off`（默认）| `on`

选中此复选框可使溢出饱和到该数据类型能表示的最大值或最小值。如果清除此复选框，模块将回绕所有溢出。有关详细信息，请参阅 Precision and Range (DSP System Toolbox)。

选中此复选框时，饱和将应用于模块上的每个内部运算，而不仅仅是输出或结果。代码生成过程通常可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 程序化使用

|  |
| --- |
| **模块参数**：`SaturateOnIntegerOverflow` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认**：`'off'` |

#### **Mode** — 要指定的数据类别 `Inherit`（默认）| `Built in` | `Fixed point` | `Expression`

选择您希望如何指定 **Output** 数据类型的属性。您可以选择：

- `Inherit` — 允许您指定用于继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- `Built in` — 允许您指定内置数据类型。
- `Fixed point` — 允许您指定数据类型的定点属性。
- `Expression` — 允许您指定计算结果为有效数据类型的表达式，例如 `fixdt([],16,0)`

#### 依赖关系

要启用此参数，请在 **Output data type** 参数处点击 **>>**。

#### **Signedness** — 指定有符号或无符号 `Signed`（默认）| `Unsigned`

指定 **Output** 数据类型的 **Signedness**。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

#### **Scaling** — 定点数据的定标方法 `Binary point`（默认）

指定 **Output** 数据类型的 **Scaling**。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

#### **数据类型覆盖** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

选择此信号的数据类型覆盖模式。

- `Inherit` — 继承为模型指定的数据类型覆盖设置。
- `Off` — 忽略为模型指定的数据类型覆盖设置，并使用您指定的定点数据类型

有关详细信息，请参阅 Simulink 文档中的 Specify Data Types Using Data Type Assistant。

#### 提示

能够为单个数据类型关闭数据类型覆盖，可在应用数据类型覆盖时更好地控制模型中的数据类型。例如，您可以使用此选项确保数据类型满足下游模块的要求，而无论数据类型覆盖设置如何。

#### 依赖关系

要启用此参数，请点击 **Show data type assistant** 按钮，并将 **Mode** 设置为 `Built in` 或 `Fixed point`。

#### **Word length** — 保存量化整数的字长位数 `16`（默认）| 0 到 32 的整数

指定保存量化整数的字长位数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

#### **Fraction length** — 为定点数据类型指定小数长度 `0`（默认）| 标量整数

将定点数据类型的小数长度指定为正整数或负整数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请设置：

- **Mode** 为 `Fixed point`
- **Scaling** 为 `Binary point`

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

#### 定点转换
使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史

**在 R2006a 之前推出**

#### R2021b：Matrix Square 模块已移至 Simulink Matrix Operations 库

Matrix Square 模块已从 **DSP System Toolbox** > **Math Functions** > **Matrices and Linear Algebra** > **Matrix Operations** 移至 **Simulink** > **Matrix Operations**。所有现有模型继续工作。

## Libraries

Simulink / Matrix Operations

## Description

The Matrix Square block computes the square of an
*M*-by-*N* input matrix, *u*, by
premultiplying with the Hermitian transpose. The equivalent MATLAB® code is:

```
y = u' * u
```

The block treats length-*M*
unoriented vector inputs as an
*M*-by-1 matrix. When the input
is an *M*-by-*N*
matrix, the output of the block is an
*N*-by-*N* matrix.

### Applications

The Matrix Square block can be used in a variety of applications:

- General matrix squares — The Matrix
  Square block computes the output matrix,
  *y*, without explicitly forming
  *u'*. It is therefore more efficient than other methods for computing the matrix square.
- Sum of squares — When the input is a column vector
  (*N*=1), the operation of the block is equivalent to a
  multiply-accumulate (MAC) process, or inner product. The output is the sum
  of the squares of the input, and is always a real scalar.
- Correlation matrix — When the input
  is a row vector (*M*=1), the
  output, *y*, is the symmetric autocorrelation matrix, or outer product.

## Ports

### Input

### **Port\_1** — Input matrix *M*-by-1 matrix | 1-by-*N* matrix | *M*-by-*N* matrix

Input matrix, specified as an *M*-by-1, 1-by-*N*, or
*M*-by-*N* matrix.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `fixed point`
### Output

### **Port\_1** — Output matrix *M*-by-*M* matrix | *N*-by-*N* matrix

Output matrix, returned as an *N*-by-*N* or
*M*-by-*M* matrix.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Output minimum** — Minimum output value for range checking `[]` (default) | scalar

Minimum output value for range checking that Simulink® checks. Simulink software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMin` |
| **Type**: character vector |
| **Values**: `'[ ]'`| scalar |
| **Default**: `'[ ]'` |

### **Output maximum** — Maximum output value for range checking `[]` (default) | scalar

Maximum output value for range checking that Simulink checks. Simulink software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMax` |
| **Type**: character vector |
| **Values**: `'[ ]'`| scalar |
| **Default**: `'[ ]'` |

### **Output data type** — Output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit via back propagation` | `Inherit: Same as input` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `fixdt(1,16,0)` | `<data type expression>`

Specify the output data type for this block.

You can select one of these options:

- A rule that specifies how to inherit a data type, such as
  `Inherit: Inherit via internal rule`.
  For more information on this rule, see Inherit via Internal Rule (DSP System Toolbox).
- An expression that evaluates to a valid data type, for example,
  `fixdt([],16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the **Output data
type** parameter. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Same as input'` | `'Inherit: Inherit via internal rule'`| `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Lock output data type setting against changes by the fixed-point tools** — Output data type locking `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the
**Output data type** you specify on the block mask. For
more information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Select the rounding
mode (DSP System Toolbox) for fixed-point operations.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **Default:** `'Floor'` |

### **Saturate on integer overflow** — Behavior when integer overflow occurs `off` (default) | `on`

Select this check box to have overflows saturate to the maximum or minimum
value that the data type can represent. If you clear this check box, the
block wraps all overflows. See Precision and
Range (DSP System Toolbox) for more information.

When you select this check box, saturation applies to every internal
operation on the block, not just the output or result. The code generation
process can generally detect when overflow is not possible. In this case,
the code generator does not produce saturation code.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SaturateOnIntegerOverflow` |
| **Type**: character vector |
| **Value**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Mode** — Category of data to specify `Inherit` (default) | `Built in` | `Fixed point` | `Expression`

Select how you would like to specify the data type properties of the
**Output** data type. You can choose:

- `Inherit` — Lets you specify a
  rule for inheriting a data type, for example,
  `Inherit: Inherit via internal
  rule`
- `Built in`— Lets you specify a
  built-in data type.
- `Fixed point` — Lets you
  specify the fixed-point attributes of the data type.
- `Expression` — Lets you
  specify an expression that evaluates to a valid data type, for
  example, `fixdt([],16,0)`

#### Dependencies

To enable this parameter, click **>>** at the
**Output data type** parameter.

### **Signedness** — Specify signed or unsigned `Signed` (default) | `Unsigned`

Specify the **Signedness** for the
**Output** data type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Scaling** — Method for scaling fixed-point data `Binary point` (default)

Specify the **Scaling** for the
**Output** data type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Data type override** — Specify data type override mode for this signal `Inherit` | `Off`

Select the data type override mode for this signal.

- `Inherit` — Inherits the data type
  override setting specified for the model.
- `Off` — Ignores the data type
  override setting specified for the model and uses the fixed-point
  data type you specify

For more information, see Specify Data Types Using Data Type Assistant
in the Simulink
documentation.

#### Tips

The ability to turn off data type override for an individual data type
provides greater control over the data types in your model when you
apply data type override. For example, you can use this option to ensure
that data types meet the requirements of downstream blocks regardless of
the data type override setting.

#### Dependencies

To enable this parameter, click the **Show data type
assistant** button, and set **Mode** to
`Built in` or `Fixed
point`.

### **Word length** — Bit size of the word that holds the quantized integer `16` (default) | integer from 0 to 32

Specify the bit size of the word that holds the quantized integer. For
more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Fraction length** — Specify fraction length for fixed-point data type `0` (default) | scalar integer

Specify fraction length for fixed-point data type as a positive or
negative integer. For more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set:

- **Mode** to `Fixed
  point`
- **Scaling** to `Binary
  point`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2021b: Matrix Square Block Moved to Simulink Matrix Operations Library

The Matrix Square block has been moved from the **DSP System Toolbox** > **Math Functions** > **Matrices and Linear Algebra** > **Matrix Operations** to the **Simulink** > **Matrix Operations**. All existing models continue to work.
