---
type: simulink-block
title: 'LU Factorization'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Factorizations'
documentation_page: 'lufactorization'
documentation_source_path: 'ref/lufactorization.html'
language: zh-CN
chinese_source: worker-translation
---

# LU Factorization

## 端口

### 输入

### **A** — 输入矩阵 *M*×*M* 方阵

通过此端口将输入矩阵指定为
*M*×*M* 方阵。如果输入矩阵为定点类型，则它必须是有符号整数
或具有 2 的幂斜率且零偏置的有符号定点数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是
### 输出

### **LU** — 下三角和上三角因子 *M*×*M* 方阵

包含 *L* 的下三角元素和
*U* 的上三角元素的复合矩阵。该复合
矩阵提高了模块的效率。该矩阵输出的格式与 `lu` 函数的输出不同，`lu` 函数
将 *L* 和 *U* 作为单独的
矩阵返回。要将模块 **LU** 端口的输出转换为单独的 *L* 和 *U*
矩阵，请使用以下代码：

```
L = tril(LU,-1)+eye(size(LU)); U = triu(LU);
```

如果将这些方程产生的结果与 `lu` 函数的实际输出进行比较，您可能会看到
略有不同的值。这些差异是由舍入误差引起的，属于预期情况。
有关 LU 分解的更多信息，请参阅 `lu` 函数
页面。

该复合矩阵的大小、数据类型和复数性与
输入矩阵 *A* 相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是

### **P** — 置换向量 向量

置换向量，以长度为
*M* 的向量形式返回。该模块使用置换向量
*P* 对输入方阵
*A* 进行置换，并将置换后的矩阵分解为单位下
三角矩阵 *L* 和上三角矩阵
*U*。

考虑以下输入矩阵。

A=[1−234062−13]

当置换索引向量 *P* 等于 P=[213] 时，置换后的矩阵
*Ap* 变为：

Ap=[4061−232−13]

该模块将此矩阵分解为上三角和下三角
矩阵。有关此示例的更详细版本，请参阅 Factorize Matrix Using LU Factorization Block。

**数据类型：** `single` | `double` | `uint32`

### **S** — 输入矩阵的奇异性 逻辑标量

您可以通过启用可选输出端口
**S** 来确定输入矩阵
*A* 的奇异性。当 *A* 为奇异矩阵时，该
模块在端口 **S** 输出 `1`。
当 *A* 为非奇异矩阵时，该模块输出
`0`。

**数据类型：** `Boolean`

## 参数

### 主选项卡

### **Show singularity status** — 显示奇异性状态 `off`（默认）| `on`

选择此项以在端口
**S** 输出输入的奇异性，该端口输出布尔数据类型的值 1
或 0。输出为 1 表示当前输入为奇异矩阵，输出为 0 表示当前输入为非奇异矩阵。

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

有关更多详细信息，请参阅舍入
模式。

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

当您选择此参数时，模块将对其
定点运算的结果进行饱和处理。当您清除此参数时，模块将
对其定点运算的结果进行环绕处理。有关
`saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出
模式。

### **Product output** — 乘积输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `fixdt(1,16,0)`

**Product output** 指定 LU Factorization 模块中乘积
运算输出的数据类型。有关
乘积输出数据类型的更多信息，请参阅 Fixed-Point Data Types 和
Multiplication Data Types。

- `Inherit: Inherit via internal rule`
  — 模块根据内部规则继承乘积输出数据类型。有关此规则的更多信息，请参阅
  Inherit via Internal Rule。
- `Inherit: Same as input` —
  模块将乘积输出数据类型指定为与
  输入数据类型相同。
- `fixdt(1,16,0)` — 模块
  指定一个有符号、二进制点缩放、定点数据类型，
  字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Product output**
数据类型。要使用
助手，请单击 **Show data type assistant**
按钮 。

有关数据类型助手的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Accumulator** — 累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

**Accumulator** 指定 LU Factorization 模块中
累加运算输出的数据类型。有关
如何在此模块中使用累加器数据类型的更多信息，
请参阅 Fixed-Point Data Types
部分。

- `Inherit: Inherit via internal rule`
  — 模块根据内部规则继承累加器数据类型。有关此规则的更多信息，请参阅 Inherit via Internal Rule。
- `Inherit: Same as input` —
  模块将累加器数据类型指定为与
  输入数据类型相同。
- `Inherit: Same as product output`
  — 模块将累加器数据类型指定为与
  乘积输出数据类型相同。
- `fixdt(1,16,0)` — 模块
  指定一个有符号、二进制点缩放、定点数据类型，
  字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Accumulator** 数据
类型。要使用
助手，请单击 **Show data type assistant**
按钮 。

有关数据类型助手的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output** — 输出数据类型 `Inherit: Same as input`（默认）| `fixdt(1,16,0)`

**Output** 指定 LU
Factorization 模块输出的数据类型。有关输出数据
类型的更多信息，请参阅 Fixed-Point Data Types
部分。

- `Inherit: Same as input` — 模块
  将输出数据类型指定为与输入
  数据类型相同。
- `fixdt(1,16,0)` — 模块
  指定一个有符号、二进制点缩放、定点数据类型，
  字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Output** 数据类型。
要使用
助手，请单击 **Show data type assistant**
按钮。

有关数据类型助手的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output Minimum** — 模块可以输出的最小值 `[]`（默认）| 标量

指定模块可以输出的最小值。Simulink® 软件使用此最小值来执行：

- 仿真范围检查。请参阅 Specify Signal Ranges (Simulink)。
- 定点数据类型的自动缩放。

### **Output Maximum** — 模块可以输出的最大值 `[]`（默认）| 标量

指定模块可以输出的最大值。Simulink 软件使用此最大值来执行：

- 仿真范围检查。请参阅 Specify Signal Ranges (Simulink)。
- 定点数据类型的自动缩放。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数以防止定点工具覆盖您在模块对话框中指定的数据类型。

## 所属库

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Factorizations

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

生成的代码在某些条件下依赖于 `memcpy` 或
`memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

将方阵分解为下三角和上三角分量

LU Factorization 模块将方形输入
矩阵 *A* 的行置换版本分解为 *A*p =
*L*\**U*，其中 *L* 是
单位下三角矩阵，*U* 是上三角矩阵，
*A*p 包含按置换索引向量
*P* 指示进行置换的 *A* 的行。该模块使用枢轴矩阵
*A*p 而不是精确的输入矩阵
*A*，因为它提高了
分解的数值精度。
