---
type: simulink-block
title: 'Difference'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Math Operations'
documentation_page: 'difference'
documentation_source_path: 'ref/difference.html'
language: zh-CN
chinese_source: worker-translation
---

# Difference

## 端口

### 输入

### **Port\_1** — 输入信号 向量 | 矩阵 | *N* 维数组

输入信号，指定为向量、矩阵或 *N* 维数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是
### 输出

### **Port\_1** — 输出信号 向量 | 矩阵 | *N* 维数组

输入的相邻行、列或指定维度之间的差值，以向量、矩阵或 *N* 维数组形式返回。

输出的数据类型和复数性与输入相同，但计算差值的维度长度减一。其他维度的长度保持不变。

有关输出计算方式的更多详细信息，请参阅沿参数方向的差分。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是

## 参数

### 主选项卡

### **运行差分** — 运行差分 `No`（默认）| `Yes`

指定模块是否计算运行差分。

- `No` —— 模块计算当前输入指定维度中相邻元素之间的差值。在此模式下，模块可以根据沿参数方向的差分计算输入沿列、行或指定维度的差值。
- `Yes` —— 模块计算输入沿列的运行差分。有关更多信息，请参阅运行操作。

### **沿参数方向的差分** — 差分维度 `Columns`（默认）| `Rows` | `Specified dimension`

指定模块计算输入沿列、行或指定维度的差值。

- `Columns` —— 模块计算输入每一列中相邻元素之间的差值。等效的 MATLAB® 代码为：

  ```
  y = diff(u)
  ```

  对于 *M*×*N* 输入，输出为 (*M* – 1)×*N* 矩阵，其第 *j* 列包含以下元素：

  yi,j=ui+1,j−ui,j     1≤i≤(M−1)
- `Rows` —— 模块计算输入每一行中相邻元素之间的差值。等效的 MATLAB 代码为：

  ```
  y = diff(u,[],2)
  ```

  输出为 *M*×(*N*–1) 矩阵，其第 *i* 行包含以下元素：

  yi,j=ui,j+1−ui,j     1≤j≤(N−1)
- `Specified dimension` —— 模块的行为是前述按行差分的扩展。模块计算沿**维度**参数中指定维度的相邻元素之间的差值。等效的 MATLAB 代码为：

  ```
  y = diff(u,[],d)
  ```

  其中 *d* 是维度。

  输出是一个数组，其在指定维度上的长度比输入少一，其他维度上的长度保持不变。例如，考虑一个 *M*×*N*×*P*×*R* 输入数组，其元素为 *u(i,j,k,l)*，并假设**维度**参数的值为 `3`。模块的输出为 *M*×*N*×(*P*–1)×*R* 数组，包含以下元素：

  yi,j,k,l=ui,j,k+1,l−ui,j,k,l     1≤k≤(P−1)

### **维度** — 基于一的维度 `1`（默认）| `2` | `3`

指定用于计算逐元素差值的基于一的维度。

#### 依赖关系

要启用此参数，请为**沿参数方向的差分**参数选择 `Specified dimension`。

### 数据类型选项卡

### **舍入模式** — 舍入运算的方法 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅舍入模式。

### **整数溢出时饱和** — 溢出操作的方法 off（默认）| on

选中此参数时，模块对其定点运算的结果进行饱和处理。清除此参数时，模块对其定点运算的结果进行回绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **累加器** — 累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `fixdt([],16,0)`

**累加器**指定 Difference 模块中累加运算输出的数据类型。

- `Inherit: Inherit via internal rule` —— 模块根据内部规则继承累加器数据类型。有关此规则的更多信息，请参阅通过内部规则继承。
- `Inherit: Same as input` —— 模块将累加器数据类型指定为与输入数据类型相同。
- `fixdt([],16,0)` —— 模块指定一个自动有符号、二进制点、定标定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用**数据类型助手**设置**累加器**数据类型。要使用助手，请点击**显示数据类型助手**按钮。

有关数据类型助手的更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

有关如何在此模块中使用累加器数据类型的说明，请参阅定点数据类型。

### **输出** — 输出数据类型 `Inherit: Same as accumulator`（默认）| `Inherit: Same as input` | `fixdt([],16,0)`

**输出**指定 Difference 模块输出的数据类型。

- `Inherit: Same as input` —— 模块将输出数据类型指定为与输入数据类型相同。
- `Inherit: Same as accumulator` —— 模块将输出数据类型指定为与累加器数据类型相同。
- `fixdt([],16,0)` —— 模块指定一个自动有符号、二进制点、定标定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用**数据类型助手**设置**输出**数据类型。要使用助手，请点击**显示数据类型助手**按钮。

有关更多信息，请参阅控制信号的数据类型 (Simulink)。

有关输出数据类型的更多信息，请参阅定点数据类型。

### **输出最小值** — 模块可以输出的最小值 `[]`（默认）| 标量

指定模块可以输出的最小值。Simulink 使用此最小值执行：

- 仿真范围检查。请参阅指定信号范围 (Simulink)。
- 定点数据类型的自动定标。

### **输出最大值** — 模块可以输出的最大值 `[]`（默认）| 标量

指定模块可以输出的最大值。Simulink 使用此最大值执行：

- 仿真范围检查。请参阅指定信号范围 (Simulink)。
- 定点数据类型的自动定标。

### **锁定数据类型设置以防止定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。

**注意**

浮点继承优先于此窗格上定义的数据类型设置。当输入为浮点时，模块忽略这些设置，所有内部数据类型均为浮点。

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

计算输入沿指定维度的逐元素差值

Difference 模块计算输入数组 *u* 的相邻行、列或指定维度中相邻元素之间的差值。您可以将模块配置为仅计算当前输入内的差值，或跨连续输入计算差值（运行差分）。
