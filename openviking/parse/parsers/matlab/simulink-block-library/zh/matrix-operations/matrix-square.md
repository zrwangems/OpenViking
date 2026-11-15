---
type: simulink-block
title: 'Matrix Square'
family: matrix-operations
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'matrixsquare'
language: zh-CN
chinese_source: worker-translation
---

# Matrix Square



计算输入矩阵的平方

## 库

Simulink / Matrix Operations

## 说明

Matrix Square 模块通过使用 Hermitian 转置进行左乘，计算 *M*×*N* 输入矩阵 *u* 的平方。等效的 MATLAB® 代码为：

    y = u' * u

该模块将长度为 *M* 的未定向向量输入视为 *M*×1 矩阵。当输入为 *M*×*N* 矩阵时，模块的输出为 *N*×*N* 矩阵。

### 应用

Matrix Square 模块可用于多种应用：

- 一般矩阵平方 — Matrix Square 模块计算输出矩阵 *y*，而无需显式构造 *u'*。因此，它比其他计算矩阵平方的方法更高效。
- 平方和 — 当输入为列向量（*N*=1）时，模块的操作等效于乘加（MAC）过程，或内积。输出是输入的平方和，并且始终为实数标量。
- 相关矩阵 — 当输入为行向量（*M*=1）时，输出 *y* 是对称自相关矩阵，或外积。

## 端口

### 输入

### **Port\_1** — 输入矩阵 *M*×1 矩阵 | 1×*N* 矩阵 | *M*×*N* 矩阵

输入矩阵，指定为 *M*×1、1×*N* 或 *M*×*N* 矩阵。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `fixed point`

### 输出

### **Port\_1** — 输出矩阵 *M*×*M* 矩阵 | *N*×*N* 矩阵

输出矩阵，返回为 *N*×*N* 或 *M*×*M* 矩阵。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **输出最小值** — 用于范围检查的最小输出值 `[]`（默认）| scalar

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

### **输出最大值** — 用于范围检查的最大输出值 `[]`（默认）| scalar

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

### **输出数据类型** — 输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Inherit via back propagation` | `Inherit: Same as input` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `fixdt(1,16,0)` | `<data type expression>`

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

### **锁定输出数据类型设置以防止定点工具更改** — 输出数据类型锁定 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块掩码上指定的 **Output data type**。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** character vector |
| **值：** `'off' | 'on'` |
| **默认：** `'off'` |

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择用于定点运算的舍入模式 (DSP System Toolbox)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** character vector |
| **值：** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认：** `'Floor'` |

### **在整数溢出时饱和** — 发生整数溢出时的行为 `off`（默认）| `on`

选中此复选框可使溢出饱和到该数据类型能表示的最大值或最小值。如果清除此复选框，模块将回绕所有溢出。有关详细信息，请参阅 Precision and Range (DSP System Toolbox)。

选中此复选框时，饱和将应用于模块上的每个内部运算，而不仅仅是输出或结果。代码生成过程通常可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 程序化使用

|  |
| --- |
| **模块参数**：`SaturateOnIntegerOverflow` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认**：`'off'` |

### **Mode** — 要指定的数据类别 `Inherit`（默认）| `Built in` | `Fixed point` | `Expression`

选择您希望如何指定 **Output** 数据类型的属性。您可以选择：

- `Inherit` — 允许您指定用于继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- `Built in` — 允许您指定内置数据类型。
- `Fixed point` — 允许您指定数据类型的定点属性。
- `Expression` — 允许您指定计算结果为有效数据类型的表达式，例如 `fixdt([],16,0)`

#### 依赖关系

要启用此参数，请在 **Output data type** 参数处点击 **>>**。

### **Signedness** — 指定有符号或无符号 `Signed`（默认）| `Unsigned`

指定 **Output** 数据类型的 **Signedness**。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Scaling** — 定点数据的定标方法 `Binary point`（默认）

指定 **Output** 数据类型的 **Scaling**。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **数据类型覆盖** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

选择此信号的数据类型覆盖模式。

- `Inherit` — 继承为模型指定的数据类型覆盖设置。
- `Off` — 忽略为模型指定的数据类型覆盖设置，并使用您指定的定点数据类型

有关详细信息，请参阅 Simulink 文档中的 Specify Data Types Using Data Type Assistant。

#### 提示

能够为单个数据类型关闭数据类型覆盖，可在应用数据类型覆盖时更好地控制模型中的数据类型。例如，您可以使用此选项确保数据类型满足下游模块的要求，而无论数据类型覆盖设置如何。

#### 依赖关系

要启用此参数，请点击 **Show data type assistant** 按钮，并将 **Mode** 设置为 `Built in` 或 `Fixed point`。

### **Word length** — 保存量化整数的字长位数 `16`（默认）| 0 到 32 的整数

指定保存量化整数的字长位数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Fraction length** — 为定点数据类型指定小数长度 `0`（默认）| 标量整数

将定点数据类型的小数长度指定为正整数或负整数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请设置：

- **Mode** 为 `Fixed point`
- **Scaling** 为 `Binary point`

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换
使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

### R2021b：Matrix Square 模块已移至 Simulink Matrix Operations 库

Matrix Square 模块已从 **DSP System Toolbox** > **Math Functions** > **Matrices and Linear Algebra** > **Matrix Operations** 移至 **Simulink** > **Matrix Operations**。所有现有模型继续工作。
