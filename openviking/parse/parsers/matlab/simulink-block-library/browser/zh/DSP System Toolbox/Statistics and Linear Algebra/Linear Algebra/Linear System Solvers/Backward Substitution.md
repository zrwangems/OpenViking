---
type: simulink-block
title: 'Backward Substitution'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Linear Algebra / Linear System Solvers'
documentation_page: 'backwardsubstitution'
documentation_source_path: 'ref/backwardsubstitution.html'
language: zh-CN
chinese_source: worker-translation
---

# Backward Substitution

## 端口

### 输入

### **U** — 输入上三角矩阵 *M*×*M* 矩阵

通过此端口指定输入上三角 *M*×*M* 矩阵 *U*。输入 *U* 和 *B* 必须具有相同的行数。

如果输入为定点，则它必须是有符号整数或具有 2 的幂斜率且零偏置的有符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** Yes

### **B** — *B* 矩阵 *M*×*N* 矩阵 | *M*×1 向量

在 *U**X* = *B* 方程中将 *B* 矩阵指定为 *M*×*N* 矩阵或 *M*×1 向量。

当您指定 *M*×1 向量时，模块将端口 **B** 处的长度为 *M* 的向量输入视为 *M*×1 矩阵。输入 *U* 和 *B* 必须具有相同的行数。

如果输入为定点，则它必须是有符号整数或具有 2 的幂斜率且零偏置的有符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** Yes
### 输出

### **X** — 方程组解 *M*×*N* 矩阵 | *M*×1 矩阵

模块将输出返回为 *M*×*N* 矩阵或 *M*×1 向量。*X* 矩阵的大小与 *B* 矩阵的大小相同。

当输入为定点时，输出矩阵 *X* 仅为有符号定点。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** Yes

## 参数

### 主选项卡

### **Input U is unit-upper triangular** — 输入矩阵的对角元素值为 1 `off`（默认） | `on`

仅当 *U* 对角线上的所有元素的值均为 `1` 时，才选中此复选框。这样做时，模块通过跳过不必要的除法运算来优化其行为。

如果 *U* 对角线上的任何元素的值不为 `1`，则不要选中此复选框。当您清除 **Input U is unit-upper triangular** 复选框时，模块始终执行除法运算。

### **Diagonal of complex input U is real** — 复数输入的对角元素为实数 `off`（默认） | `on`

当复数输入 *U* 的对角元素为实数时，选中以优化仿真速度。

**注意**

当 U 是复数定点信号时，您必须选中 **Input U is unit-upper triangular** 或 **Diagonal of complex input U is real**。选中其中任一选项时，模块会忽略 *U* 对角线的任何虚部。

#### 依赖关系

仅当未选中 **Input U is unit-upper triangular** 时，此参数才可见。

### 数据类型选项卡

**注意**

浮点继承优先于在此窗格上定义的数据类型设置。当输入为浮点时，模块忽略这些设置，并且所有内部数据类型均为浮点。

### **Rounding mode** — 舍入操作的方法 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅 rounding mode。

### **Saturate on integer overflow** — 溢出操作的方法 off（默认） | on

当您选中此参数时，模块会饱和其定点运算的结果。当您清除此参数时，模块会环绕其定点运算的结果。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **Product output** — 乘积输出数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Same as first input` | `fixdt(1,16,0)`

**Product output** 指定 Backward Substitution 模块中乘积运算输出的数据类型。有关乘积输出数据类型的详细信息，请参阅 Fixed-Point Data Types 和 Multiplication Data Types。

- `Inherit: Inherit via internal rule` — 模块根据内部规则继承乘积输出数据类型。有关此规则的详细信息，请参阅 Inherit via Internal Rule。
- `Inherit: Same as first input` — 模块将乘积输出数据类型指定为与第一个输入数据类型相同。
- `fixdt(1,16,0)` — 模块指定带符号、二进制点缩放、定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Product output** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮。

有关数据类型助手的详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Accumulator** — 累加器数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Same as product output` | `Inherit: Same as first input` | `fixdt(1,16,0)`

**Accumulator** 指定 Backward Substitution 模块中累加运算输出的数据类型。有关如何在此模块中使用累加器数据类型的图示，请参阅 Fixed-Point Data Types。

- `Inherit: Inherit via internal rule` — 模块根据内部规则继承累加器数据类型。有关此规则的详细信息，请参阅 Inherit via Internal Rule。
- `Inherit: Same as product output` — 模块将累加器数据类型指定为与乘积输出数据类型相同。
- `Inherit: Same as first input` — 模块将累加器数据类型指定为与第一个输入数据类型相同。
- `fixdt(1,16,0)` — 模块指定带符号、二进制点缩放、定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Accumulator** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮。

有关数据类型助手的详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output** — 输出数据类型 `Inherit: Same as first input`（默认） | `fixdt(1,16,0)`

**Output** 指定 Backward Substitution 模块输出的数据类型。有关输出数据类型的详细信息，请参阅 Fixed-Point Data Types。

- `Inherit: Same as first input` — 模块将输出数据类型指定为与第一个输入数据类型相同。
- `fixdt(1,16,0)` — 模块指定带符号、二进制点缩放、定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Output** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮。

有关数据类型助手的详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output Minimum** — 模块可以输出的最小值 `[]`（默认） | scalar

指定模块可以输出的最小值。Simulink® 软件使用此最小值执行：

- 仿真范围检查。请参阅 Specify Signal Ranges (Simulink)。
- 定点数据类型的自动缩放。

### **Output Maximum** — 模块可以输出的最大值 `[]`（默认） | scalar

指定模块可以输出的最大值。Simulink 软件使用此最大值执行：

- 仿真范围检查。请参阅 Specify Signal Ranges (Simulink)。
- 定点数据类型的自动缩放。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

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

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数 (`string.h`)。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

当 U 为上三角矩阵时，求解 U X = B 中的 X

Backward Substitution 模块通过简单的变量回代求解线性系统 *U**X* = *B*，其中：

- *U* 是输入到 **U** 端口的上三角 *M*×*M* 矩阵。
- *B* 是输入到 **B** 端口的 *M*×*N* 矩阵。
- *X* 是 *M*×*N* 输出矩阵，并且是方程组的解。

模块不检查输入的秩。模块仅使用输入 *U* 的*上三角*中的元素，并忽略下三角元素。当您选中 **Input U is unit-upper triangular** 复选框时，模块假定 *U* 对角线上的元素为 1。当矩阵 *U* 是另一操作（例如 LDL 分解）的结果，该操作使用对角线元素表示 *D* 矩阵时，这很有用。
