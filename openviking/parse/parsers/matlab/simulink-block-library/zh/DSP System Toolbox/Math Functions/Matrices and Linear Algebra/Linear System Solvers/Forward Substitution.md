---
type: simulink-block
title: 'Forward Substitution'
family: 'math-functions'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Linear System Solvers'
documentation_page: 'forwardsubstitution'
documentation_source_path: 'ref/forwardsubstitution.html'
language: zh-CN
chinese_source: worker-translation
---

# Forward Substitution

## 端口

### 输入

### **L** — 输入下三角矩阵 *M*-by-*M* 矩阵

通过此端口指定输入下三角 *M*-by-*M* 矩阵 *L*。输入 *L* 和 *B* 的行数必须相同。

当输入 *L* 为定点时，它仅为有符号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** Yes

### **B** — *B* 矩阵 *M*-by-*N* 矩阵 | *M*-by-1 向量

在 *L**X* = *B* 方程中，将 *B* 矩阵指定为 *M*-by-*N* 矩阵或 *M*-by-1 向量。

当您指定 *M*-by-1 向量时，模块将端口 **B** 处的长度 *M* 向量输入视为 *M*-by-1 矩阵。输入 *L* 和 *B* 的行数必须相同。

当输入 *B* 为定点时，它仅为有符号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** Yes

### 输出

### **X** — 方程组解 *M*-by-*N* 矩阵 | *M*-by-1 矩阵

模块将输出返回为 *M*-by-*N* 矩阵或 *M*-by-1 矩阵。*X* 矩阵的大小与 *B* 矩阵的大小相同。

当输入为定点时，输出矩阵 *X* 仅为有符号定点。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** Yes

## 参数

### 主选项卡

### **输入 L 为单位下三角** — 输入矩阵的对角线元素的值为 1 `off` (default) | `on`

仅当 *L* 对角线上的所有元素的值均为 `1` 时，才选中此复选框。这样做时，模块会通过跳过不必要的除法运算来优化其行为。

如果 *L* 对角线上的任何元素的值不为 `1`，则不要选中此复选框。当您清除 **输入 L 为单位下三角** 复选框时，模块始终执行除法运算。

### **复数输入 L 的对角线为实数** — 复数输入的对角线元素为实数 `off` (default) | `on`

当复数输入 *L* 的对角线元素为实数时，选中此项可优化仿真速度。

**注意**

当 *L* 为复数定点信号时，您必须选择 **输入 L 为单位下三角** 或 **复数输入 L 的对角线为实数**。在这些情况下，模块会忽略 *L* 对角线的任何虚部。

#### 依赖关系

仅当未选中 **输入 L 为单位上三角** 时，此参数才可见。

### 数据类型选项卡

**注意**

浮点继承优先于此窗格上定义的数据类型设置。当输入为浮点时，模块会忽略这些设置，并且所有内部数据类型均为浮点。

### **舍入模式** — 舍入运算的方法 `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅舍入模式。

### **对整数溢出进行饱和处理** — 溢出操作的方法 off (default) | on

选中此参数时，模块会对其定点运算的结果进行饱和处理。清除此参数时，模块会对其定点运算的结果进行环绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **乘积输出** — 乘积输出数据类型 `Inherit: Inherit via internal rule` (default) | `Inherit: Same as first input` | `fixdt(1,16,0)`

**乘积输出** 指定 Backward Substitution 模块中乘积运算输出的数据类型。有关乘积输出数据类型的详细信息，请参阅 Fixed-Point Data Types 和 Multiplication Data Types。

- `Inherit: Inherit via internal rule`
  — 模块基于内部规则继承乘积输出数据类型。有关此规则的详细信息，请参阅 Inherit via Internal Rule。
- `Inherit: Same as first input`
  — 模块将乘积输出数据类型指定为与第一个输入数据类型相同。
- `fixdt(1,16,0)` — 模块指定一个有符号、二进制点定标、定点数据类型，其字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **乘积输出** 数据类型。要使用助手，请点击 **Show data type assistant** 按钮 。

有关数据类型助手的详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **累加器** — 累加器数据类型 `Inherit: Inherit via internal rule` (default) | `Inherit: Same as product output` | `Inherit: Same as first input` | `fixdt(1,16,0)`

**累加器** 指定 Backward Substitution 模块中累加运算输出的数据类型。有关如何在此模块中使用累加器数据类型的说明，请参阅 Fixed-Point Data Types 部分。

- `Inherit: Inherit via internal rule`
  — 模块基于内部规则继承累加器数据类型。有关此规则的详细信息，请参阅 Inherit via Internal Rule。
- `Inherit: Same as product output`
  — 模块将累加器数据类型指定为与乘积输出数据类型相同。
- `Inherit: Same as first input`
  — 模块将累加器数据类型指定为与第一个输入数据类型相同。
- `fixdt(1,16,0)` — 模块指定一个有符号、二进制点定标、定点数据类型，其字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **累加器** 数据类型。要使用助手，请点击 **Show data type assistant** 按钮 。

有关数据类型助手的详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **输出** — 输出数据类型 `Inherit: Same as first input` (default) | `fixdt(1,16,0)`

**输出** 指定 Backward Substitution 模块输出的数据类型。有关输出数据类型的详细信息，请参阅 Fixed-Point Data Types 部分。

- `Inherit: Same as first input`
  — 模块将输出数据类型指定为与第一个输入数据类型相同。
- `fixdt(1,16,0)` — 模块指定一个有符号、二进制点定标、定点数据类型，其字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **输出** 数据类型。要使用助手，请点击 **Show data type assistant** 按钮。

有关数据类型助手的详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **输出最小值** — 模块可以输出的最小值 `[]` (default) | scalar

指定模块可以输出的最小值。Simulink® 软件使用此最小值执行：

- 仿真范围检查。请参阅 Specify Signal Ranges (Simulink)。
- 定点数据类型的自动定标。

### **输出最大值** — 模块可以输出的最大值 `[]` (default) | scalar

指定模块可以输出的最大值。Simulink 软件使用此最大值执行：

- 仿真范围检查。请参阅 Specify Signal Ranges (Simulink)。
- 定点数据类型的自动定标。

### **锁定数据类型设置以防止定点工具更改** — 防止定点工具覆盖数据类型 `off` (default) | `on`

选中此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。

## 所属库

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Linear System Solvers

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

当 *L* 为下三角矩阵时，求解 *L**X* = *B* 中的 *X*

Forward Substitution 模块通过变量的简单前向代入求解线性系统 *L**X* = *B*，其中：

- *L* 是 **L** 端口的输入下三角 *M*-by-*M* 矩阵。
- *B* 是 **B** 端口的输入 *M*-by-*N* 矩阵。
- *X* 是 *M*-by-*N* 输出矩阵，并且是方程组的解。

模块不检查输入的秩。模块仅使用输入 *L* 的*下三角*中的元素，并忽略上三角元素。当您选中 **输入 L 为单位下三角** 时，模块假定 *L* 对角线上的元素为 1。当矩阵 *L* 是另一个运算（例如使用对角线元素表示 *D* 矩阵的 LDL 分解）的结果时，这很有用。
