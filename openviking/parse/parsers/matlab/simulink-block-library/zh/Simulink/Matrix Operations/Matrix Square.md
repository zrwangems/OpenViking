---
type: simulink-block
title: 'Matrix Square'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Matrix Operations'
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

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `fixed point`
### 输出

### **Port\_1** — 输出矩阵 *M*×*M* 矩阵 | *N*×*N* 矩阵

输出矩阵，返回为 *N*×*N* 或 *M*×*M* 矩阵。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **输出最小值** — 用于范围检查的最小输出值 `[]`（默认） | 标量

用于范围检查的最小输出值，Simulink® 会检查该值。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges）
- 定点数据类型的自动定标

#### 编程用法

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型**：字符向量 |
| **值**：`'[ ]'`| 标量 |
| **默认值**：`'[ ]'` |

### **输出最大值** — 用于范围检查的最大输出值 `[]`（默认） | 标量

用于范围检查的最大输出值，Simulink 会检查该值。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges）
- 定点数据类型的自动定标

#### 编程用法

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：字符向量 |
| **值**：`'[ ]'`| 标量 |
| **默认值**：`'[ ]'` |

### **输出数据类型** — 输出数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Inherit via back propagation` | `Inherit: Same as input` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `fixdt(1,16,0)` | `<data type expression>`

指定此模块的输出数据类型。

可以选择以下选项之一：

- 用于指定如何继承数据类型的规则，例如 `Inherit: Inherit via internal rule`。
  有关此规则的详细信息，请参阅 Inherit via Internal Rule (DSP System Toolbox)。
- 计算结果为有效数据类型的表达式，例如 `fixdt([],16,0)`

点击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置 **输出数据类型** 参数。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Same as input'` | `'Inherit: Inherit via internal rule'`| `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **锁定输出数据类型设置以防止被定点工具更改** — 输出数据类型锁定 `off`（默认） | `on`

选择此参数可防止定点工具覆盖您在模块掩码上指定的 **输出数据类型**。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择用于定点运算的舍入模式（DSP System Toolbox）。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值：** `'Floor'` |

### **整数溢出时饱和** — 发生整数溢出时的行为 `off`（默认） | `on`

选中此复选框可使溢出饱和到该数据类型能够表示的最大值或最小值。如果清除此复选框，模块将环绕所有溢出。有关详细信息，请参阅 Precision and Range (DSP System Toolbox)。

选中此复选框时，饱和适用于模块上的每个内部运算，而不仅仅是输出或结果。代码生成过程通常可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

|  |
| --- |
| **模块参数**：`SaturateOnIntegerOverflow` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **模式** — 要指定的数据类别 `Inherit`（默认） | `Built in` | `Fixed point` | `Expression`

选择希望如何指定 **输出** 数据类型的数据类型属性。可以选择：

- `Inherit` — 允许您指定用于继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- `Built in`— 允许您指定内置数据类型。
- `Fixed point` — 允许您指定数据类型的定点属性。
- `Expression` — 允许您指定计算结果为有效数据类型的表达式，例如 `fixdt([],16,0)`

#### 依赖关系

要启用此参数，请在 **输出数据类型** 参数处点击 **>>**。

### **有符号性** — 指定有符号或无符号 `Signed`（默认） | `Unsigned`

指定 **输出** 数据类型的 **有符号性**。

#### 依赖关系

要启用此参数，请将 **模式** 设置为 `Fixed point`。

### **定标** — 定点数据的定标方法 `Binary point`（默认）

指定 **输出** 数据类型的 **定标**。

#### 依赖关系

要启用此参数，请将 **模式** 设置为 `Fixed point`。

### **数据类型覆盖** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

选择此信号的数据类型覆盖模式。

- `Inherit` — 继承为模型指定的数据类型覆盖设置。
- `Off` — 忽略为模型指定的数据类型覆盖设置，并使用您指定的定点数据类型

有关详细信息，请参阅 Simulink 文档中的 Specify Data Types Using Data Type Assistant。

#### 提示

为单个数据类型关闭数据类型覆盖的能力，使您在应用数据类型覆盖时能更好地控制模型中的数据类型。例如，可以使用此选项确保数据类型满足下游模块的要求，而不受数据类型覆盖设置的影响。

#### 依赖关系

要启用此参数，请点击 **显示数据类型助手** 按钮，并将 **模式** 设置为 `Built in` 或 `Fixed point`。

### **字长** — 保存量化整数的字位数 `16`（默认） | 0 到 32 的整数

指定保存量化整数的字位数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **模式** 设置为 `Fixed point`。

### **小数长度** — 指定定点数据类型的小数长度 `0`（默认） | 标量整数

将定点数据类型的小数长度指定为正整数或负整数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请设置：

- 将 **模式** 设置为 `Fixed point`
- 将 **定标** 设置为 `Binary point`

## 所属库

Simulink / Matrix Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2021b：Matrix Square 模块已移至 Simulink Matrix Operations 库

Matrix Square 模块已从 **DSP System Toolbox** > **Math Functions** > **Matrices and Linear Algebra** > **Matrix Operations** 移至 **Simulink** > **Matrix Operations**。所有现有模型继续工作。

## 描述

计算输入矩阵的平方

Matrix Square 模块通过用 Hermitian 转置进行预乘，计算 *M*×*N* 输入矩阵 *u* 的平方。等效的 MATLAB® 代码为：

```
y = u' * u
```

该模块将长度为 *M* 的未定向向量输入视为 *M*×1 矩阵。当输入为 *M*×*N* 矩阵时，模块的输出为 *N*×*N* 矩阵。

### 应用

Matrix Square 模块可用于多种应用：

- 一般矩阵平方 — Matrix Square 模块计算输出矩阵 *y*，而不显式构造 *u'*。因此，它比其他计算矩阵平方的方法更高效。
- 平方和 — 当输入为列向量（*N*=1）时，模块的操作等效于乘法累加（MAC）过程或内积。输出是输入的平方和，并且始终为实数标量。
- 相关矩阵 — 当输入为行向量（*M*=1）时，输出 *y* 是对称自相关矩阵或外积。
