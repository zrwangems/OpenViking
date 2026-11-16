---
type: simulink-block
title: 'Difference'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Array and Matrix Mathematics / Array Operations'
documentation_page: 'difference'
documentation_source_path: 'ref/difference.html'
language: zh-CN
chinese_source: worker-translation
---

# Difference

## 端口

### 输入

### **Port\_1** — 输入信号向量 | 矩阵 | *N* 维数组

输入信号，指定为向量、矩阵或 *N* 维数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** Yes
### 输出

### **Port\_1** — 输出信号向量 | 矩阵 | *N* 维数组

输入的相邻行、列或指定维度之间的差分，以向量、矩阵或 *N* 维数组形式返回。

输出与输入具有相同的数据类型和复数性，但计算差分的维度会减少一。其他维度的长度保持不变。

有关如何计算输出的更多详细信息，请参阅 Difference along 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** Yes

## 参数

### 主选项卡

### **Running difference** — 运行差分 `No`（默认）| `Yes`

指定该模块是否计算运行差分。

- `No` –– 该模块计算当前输入指定维度中相邻元素之间的差分。在此模式下，该模块可根据 Difference along 参数沿输入的列、行或指定维度计算差分。
- `Yes` –– 该模块沿输入的列计算运行差分。有关详细信息，请参阅 Running Operation。

### **Difference along** — 差分维度 `Columns`（默认）| `Rows` | `Specified dimension`

指定该模块沿输入的列、行或指定维度计算差分。

- `Columns` –– 该模块计算输入每一列中相邻元素之间的差分。等效 MATLAB® 代码为：

  ```
  y = diff(u)
  ```

  对于 *M*×*N* 输入，输出是一个 (*M* – 1)×*N* 矩阵，其第 *j* 列包含以下元素：

  yi,j=ui+1,j−ui,j     1≤i≤(M−1)
- `Rows` –– 该模块计算输入每一行中相邻元素之间的差分。等效 MATLAB 代码为：

  ```
  y = diff(u,[],2)
  ```

  输出是一个 *M*×(*N*-1) 矩阵，其第 *i* 行包含以下元素：

  yi,j=ui,j+1−ui,j     1≤j≤(N−1)
- `Specified dimension` –– 该模块的行为是前述按行差分的扩展。该模块沿你在 **Dimension** 参数中指定的维度计算相邻元素之间的差分。等效 MATLAB 代码为：

  ```
  y = diff(u,[],d)
  ```

  其中 *d* 是维度。

  输出是一个数组，其在指定维度上的长度比输入少一，而在其他维度上的长度保持不变。例如，考虑一个 *M*×*N*×*P*×*R* 输入数组，其元素为 *u(i,j,k,l)*，并假设 **Dimension** 参数的值为 `3`。该模块的输出是一个 *M*×*N*×(*P*–1)×*R* 数组，包含以下元素：

  yi,j,k,l=ui,j,k+1,l−ui,j,k,l     1≤k≤(P−1)

### **Dimension** — 基于一的维度 `1`（默认）| `2` | `3`

指定用于计算逐元素差分的基于一的维度。

#### 依赖关系

要启用此参数，请为 **Difference along** 参数选择 `Specified dimension`。

### 数据类型选项卡

### **Rounding mode** — 舍入操作的方法 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅 Rounding Modes。

### **Saturate on integer overflow** — 溢出操作方法 off（默认）| on

选中此参数时，该模块会对其定点运算的结果进行饱和处理。清除此参数时，该模块会对其定点运算的结果进行环绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅 overflow mode for fixed-point operations。

### **Accumulator** — 累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `fixdt([],16,0)`

**Accumulator** 指定 Difference 模块中累加运算输出的数据类型。

- `Inherit: Inherit via internal rule` — 该模块基于内部规则继承累加器数据类型。有关此规则的更多信息，请参阅 Inherit via Internal Rule。
- `Inherit: Same as input` — 该模块将累加器数据类型指定为与输入数据类型相同。
- `fixdt([],16,0)` — 该模块指定一个自动有符号、二进制点、定标、定点数据类型，字长为 16 位，小数长度为 0。

或者，你可以使用 **Data Type Assistant** 设置 **Accumulator** 数据类型。要使用助手，请点击 **Show data type assistant** 按钮。

有关数据类型助手的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

有关如何在此模块中使用累加器数据类型的说明，请参阅 Fixed-Point Data Types。

### **Output** — 输出数据类型 `Inherit: Same as accumulator`（默认）| `Inherit: Same as input` | `fixdt([],16,0)`

**Output** 指定 Difference 模块输出的数据类型。

- `Inherit: Same as input` — 该模块将输出数据类型指定为与输入数据类型相同。
- `Inherit: Same as accumulator` — 该模块将输出数据类型指定为与累加器数据类型相同。
- `fixdt([],16,0)` — 该模块指定一个自动有符号、二进制点、定标、定点数据类型，字长为 16 位，小数长度为 0。

或者，你可以使用 **Data Type Assistant** 设置 **Output** 数据类型。要使用助手，请点击 **Show data type assistant** 按钮。

有关更多信息，请参阅 Control Data Types of Signals (Simulink)。

有关输出数据类型的更多信息，请参阅 Fixed-Point Data Types。

### **Output Minimum** — 模块可以输出的最小值 `[]`（默认）| 标量

指定该模块可以输出的最小值。Simulink 使用此最小值执行：

- 仿真范围检查。请参阅 Specify Signal Ranges (Simulink)。
- 定点数据类型的自动定标。

### **Output Maximum** — 模块可以输出的最大值 `[]`（默认）| 标量

指定该模块可以输出的最大值。Simulink 使用此最大值执行：

- 仿真范围检查。请参阅 Specify Signal Ranges (Simulink)。
- 定点数据类型的自动定标。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖你在模块对话框中指定的数据类型。

**注意**

浮点继承优先于在此窗格上定义的数据类型设置。当输入为浮点型时，该模块会忽略这些设置，并且所有内部数据类型均为浮点型。

## 所属库

DSP System Toolbox / Math Functions / Math Operations

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

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

沿输入的指定维度计算逐元素差分

Difference 模块计算输入数组 *u* 的行、列或指定维度中相邻元素之间的差分。你可以配置该模块仅在当前输入内计算差分，或跨连续输入计算差分（运行差分）。
