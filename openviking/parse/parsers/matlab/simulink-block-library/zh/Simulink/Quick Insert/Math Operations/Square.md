---
type: simulink-block
title: 'Matrix Square'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2023b
official_category: 'Quick Insert / Math Operations'
documentation_page: 'matrixsquare'
documentation_source_path: 'slref/matrixsquare.html'
language: zh-CN
chinese_source: worker-translation
---

# Matrix Square

## 端口

### 输入

### **Port\_1** — 输入矩阵 *M*×1 矩阵 | 1×*N* 矩阵 | *M*×*N* 矩阵

输入矩阵，指定为 *M*×1、1×*N* 或 *M*×*N* 矩阵。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出矩阵 *M*×*M* 矩阵 | *N*×*N* 矩阵

输出矩阵，返回为 *N*×*N* 或 *M*×*M* 矩阵。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认）| 标量

用于 Simulink® 检查的范围检查的最小输出值。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges）
- 定点数据类型的自动缩放

#### 编程使用

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型**：字符向量 |
| **值**：`'[ ]'`| 标量 |
| **默认值**：`'[ ]'` |

### **Output maximum** — 用于范围检查的最大输出值 `[]`（默认）| 标量

用于 Simulink 检查的范围检查的最大输出值。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges）
- 定点数据类型的自动缩放

#### 编程使用

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：字符向量 |
| **值**：`'[ ]'`| 标量 |
| **默认值**：`'[ ]'` |

### **Output data type** — 输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Inherit via back propagation` | `Inherit: Same as input` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `fixdt(1,16,0)` | `<data type expression>`

指定此模块的输出数据类型。

您可以选择以下选项之一：

- 指定如何继承数据类型的规则，例如
  `Inherit: Inherit via internal rule`。
  有关此规则的详细信息，请参阅 Inherit via Internal Rule (DSP System Toolbox)。
- 求值为有效数据类型的表达式，例如
  `fixdt([],16,0)`

点击 **Show data type assistant** 按钮
以显示 **Data Type
Assistant**，它可帮助您设置 **Output data
type** 参数。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Same as input'` | `'Inherit: Inherit via internal rule'`| `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Lock output data type setting against changes by the fixed-point tools** — 输出数据类型锁定 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块封装上指定的
**Output data type**。有关
详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：字符向量 |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择定点运算的舍入
模式 (DSP System Toolbox)。

#### 编程使用

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：字符向量 |
| **值**：`'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值**：`'Floor'` |

### **Saturate on integer overflow** — 整数溢出时的行为 `off`（默认）| `on`

选中此复选框可使溢出饱和到数据类型能够表示的最大值或最小
值。如果清除此复选框，模块将环绕所有溢出。有关详细信息，请参阅 Precision and
Range (DSP System Toolbox)。

当您选中此复选框时，饱和适用于模块上的每个内部
运算，而不仅仅是输出或结果。代码生成
过程通常可以检测到不可能发生溢出的情况。在这种情况下，
代码生成器不会生成饱和代码。

#### 编程使用

|  |
| --- |
| **模块参数**：`SaturateOnIntegerOverflow` |
| **类型**：字符向量 |
| **Value**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Mode** — 要指定的数据类别 `Inherit`（默认）| `Built in` | `Fixed point` | `Expression`

选择您希望如何指定 **Output** 数据类型的数据类型属性。您可以选择：

- `Inherit` — 允许您指定继承数据类型的
  规则，例如，
  `Inherit: Inherit via internal
  rule`
- `Built in`— 允许您指定
  内置数据类型。
- `Fixed point` — 允许您
  指定数据类型的定点属性。
- `Expression` — 允许您
  指定求值为有效数据类型的表达式，例
  如，`fixdt([],16,0)`

#### 依赖关系

要启用此参数，请点击 **Output data type** 参数处的 **>>**。

### **Signedness** — 指定有符号或无符号 `Signed`（默认）| `Unsigned`

指定 **Output** 数据类型的 **Signedness**。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为
`Fixed point`。

### **Scaling** — 定点数据的缩放方法 `Binary point`（默认）

指定 **Output** 数据类型的 **Scaling**。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为
`Fixed point`。

### **Data type override** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

选择此信号的数据类型覆盖模式。

- `Inherit` — 继承为模型指定的数据类型
  覆盖设置。
- `Off` — 忽略为模型指定的数据类型
  覆盖设置，并使用您指定的定点
  数据类型

有关详细信息，请参阅 Simulink
文档中的 Specify Data Types Using Data Type Assistant。

#### 提示

为单个数据类型关闭数据类型覆盖的能力
在您应用数据类型覆盖时，可对模型中的数据类型提供更强的控制。例如，您可以使用此选项确保
数据类型满足下游模块的要求，而无论数据类型覆盖设置如何。

#### 依赖关系

要启用此参数，请点击 **Show data type
assistant** 按钮，并将 **Mode** 设置为
`Built in` 或 `Fixed
point`。

### **Word length** — 保存量化整数的字长位数 `16`（默认）| 0 到 32 的整数

指定保存量化整数的字长位数。有关
详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为
`Fixed point`。

### **Fraction length** — 指定定点数据类型的小数长度 `0`（默认）| 标量整数

将定点数据类型的小数长度指定为正整数或
负整数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将：

- **Mode** 设置为 `Fixed
  point`
- **Scaling** 设置为 `Binary
  point`

## 所属库

Simulink / Matrix Operations

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2021b: Matrix Square Block Moved to Simulink Matrix Operations Library

The Matrix Square block has been moved from the **DSP System Toolbox** > **Math Functions** > **Matrices and Linear Algebra** > **Matrix Operations** to the **Simulink** > **Matrix Operations**。所有现有模型继续正常工作。

## 描述

Compute square of input matrix

Matrix Square 模块通过左乘 Hermitian 转置来计算
*M*×*N* 输入矩阵 *u* 的平方。等效的 MATLAB® 代码为：

```
y = u' * u
```

该模块将长度为 *M*
的无向向量输入视为
*M*×1 矩阵。当输入
为 *M*×*N*
矩阵时，模块的输出为
*N*×*N* 矩阵。

### 应用

Matrix Square 模块可用于多种应用：

- 一般矩阵平方 — Matrix
  Square 模块计算输出矩阵
  *y*，而不显式构造
  *u'*。因此，它比其他计算矩阵平方的方法更高效。
- 平方和 — 当输入为列向量
  （*N*=1）时，模块的运算等效于
  乘累加 (MAC) 过程，或内积。输出为输入的
  平方和，并且始终为实数标量。
- 相关矩阵 — 当输入
  为行向量（*M*=1）时，
  输出 *y* 为对称自相关矩阵，或外积。
