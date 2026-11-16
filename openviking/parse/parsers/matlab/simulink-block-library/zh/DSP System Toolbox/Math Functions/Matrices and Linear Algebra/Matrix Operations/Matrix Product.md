---
type: simulink-block
title: 'Matrix Product'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Operations'
documentation_page: 'matrixproduct'
documentation_source_path: 'ref/matrixproduct.html'
language: zh-CN
chinese_source: worker-translation
---

# Matrix Product

## 端口

### Input

### **Input** — 输入向量 | 矩阵

将输入指定为大小为 *M*×*N* 的向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** Yes
### Output

### **Output** — 矩阵乘积输出向量 | 矩阵

Matrix Product 模块的输出，返回为向量或矩阵。有关模块如何计算输出的详细信息，请参阅 **Multiply over** 参数的描述。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** Yes

## 参数

### 主选项卡

### **Multiply over** — 相乘所沿的维度 `Columns`（默认） | `Rows` | `Entire input`

指定相乘所沿的维度为以下之一：

- `Columns` –– 该模块沿每一列向下将各元素相乘，并输出生成的
  1×*N* 矩阵。该模块将长度为 *M* 的无方向向量输入视为
  *M*×1 矩阵。

  [u11u12u13u21u22u23u31u32u33]⇓[y1y2y3]=[(∏i=13ui1)(∏i=13ui2)(∏i=13ui3)]
- `Rows` –– 该模块沿每一行横向将各元素相乘，并输出生成的
  *M*×1 矩阵。该模块将长度为 *N* 的无方向向量输入视为
  1×*N* 矩阵。

  [u11u12u13u21u22u23u31u32u33]⇒[y1y2y3]=[(∏j=13u1j)(∏j=13u2j)(∏j=13u3j)]
- `Entire input` –– 该模块将输入的所有元素相乘在一起，并输出生成的标量。

  [u11u12u13u21u22u23u31u32u33]⇒y=(∏i=13∏j=13uij)

### 数据类型选项卡

**注意**

浮点继承优先于在此窗格上定义的数据类型设置。当输入为浮点时，该模块忽略这些设置，并且所有内部数据类型均为浮点。

### **Rounding mode** — 舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅舍入模式。

### **Saturate on integer overflow** — 整数溢出时饱和 `off`（默认） | `on`

选中此参数时，该模块会对其定点运算的结果进行饱和处理。清除此参数时，该模块会对其定点运算的结果进行回绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **Intermediate product** — 中间乘积数据类型 `Inherit: Same as input`（默认） | `fixdt([],16,0)`

指定中间乘积数据类型。如定点数据类型中所示，该模块在将输入的下一个元素乘入之前，会将乘法器的输出转换为中间乘积数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Same as input`
- 求值为有效数据类型的表达式，例如 `fixdt([],16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Product output** 参数。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Product output** — 乘积输出数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Same as input` | `fixdt([],16,0)`

指定乘积输出数据类型。有关描述此模块中乘积输出数据类型用法的图示，请参阅定点数据类型和乘法数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`。有关此规则的更多信息，请参阅 Inherit via Internal Rule。
- 继承数据类型的规则，例如 `Inherit: Same as input`。
- 求值为有效数据类型的表达式，例如 `fixdt([],16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Product output** 参数。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Accumulator** — 累加器数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt([],16,0)`

指定累加器数据类型。有关描述此模块中累加器数据类型用法的图示，请参阅定点数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`。有关此规则的更多信息，请参阅 Inherit via Internal Rule。
- 继承数据类型的规则，例如 `Inherit: Same as input`。
- 继承数据类型的规则，例如 `Inherit: Same as product output`。
- 求值为有效数据类型的表达式，例如 `fixdt([],16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Accumulator** 参数。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output** — 输出数据类型 `Inherit: Same as product output`（默认） | `Inherit: Same as input` | `fixdt([],16,0)`

指定输出数据类型。有关描述此模块中输出数据类型用法的图示，请参阅定点数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Same as product output`
- 继承数据类型的规则，例如 `Inherit: Same as input`。
- 求值为有效数据类型的表达式，例如 `fixdt([],16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Output** 参数。

有关更多信息，请参阅 Control Data Types of Signals (Simulink)。

### **Output Minimum** — 输出最小值 `[]`（默认） | scalar

指定该模块应输出的最小值。默认值为 `[]`（未指定）。Simulink® 使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

### **Output Maximum** — 输出最大值 `[]`（默认） | scalar

指定该模块应输出的最大值。默认值为 `[]`（未指定）。Simulink 使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

选择此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。

## 所属库

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

在某些条件下，生成的代码依赖 `memcpy` 或 `memset` 函数（`string.h`）。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

沿行、列或整个输入乘以矩阵元素

Matrix Product 模块沿 *M*×*N* 输入矩阵的行、列或所有元素将元素相乘。
