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

通过此端口将输入矩阵指定为 *M*×*M* 方阵。如果输入矩阵为定点，则它必须是有符号整数，或具有 2 的幂斜率与零偏置的有符号定点。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** Yes
### 输出

### **LU** — 下三角和上三角因子 *M*×*M* 方阵

包含 *L* 的下三角元素和 *U* 的上三角元素的复合矩阵。该复合矩阵提高了模块的效率。该矩阵输出与 `lu` 函数的输出格式不同，`lu` 函数将 *L* 和 *U* 作为单独矩阵返回。要将模块 **LU** 端口的输出转换为单独的 *L* 和 *U* 矩阵，请使用以下代码：

```
L = tril(LU,-1)+eye(size(LU)); U = triu(LU);
```

如果将这些方程生成的结果与 `lu` 函数的实际输出进行比较，可能会看到略有不同的值。这些差异是由舍入误差引起的，属于预期现象。有关 LU 分解的详细信息，请参阅 `lu` 函数页面。

该复合矩阵的大小、数据类型和复数性与输入矩阵 *A* 相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** Yes

### **P** — 置换向量

置换向量，返回为长度为 *M* 的向量。模块使用置换向量 *P* 对输入方阵 *A* 进行置换，并将置换后的矩阵分解为单位下三角 *L* 和上三角矩阵 *U*。

考虑以下输入矩阵。

A=[1−234062−13]

其中置换索引向量 *P* 等于 P=[213]，置换后的矩阵 *Ap* 变为：

Ap=[4061−232−13]

模块将该矩阵分解为上三角矩阵和下三角矩阵。有关此示例的更详细版本，请参阅 Factorize Matrix Using LU Factorization Block。

**数据类型：** `single` | `double` | `uint32`

### **S** — 输入矩阵的奇异性 逻辑标量

可以通过启用可选输出端口 **S** 来确定输入矩阵 *A* 的奇异性。当 *A* 奇异时，模块在端口 **S** 输出 `1`。当 *A* 非奇异时，模块输出 `0`。

**数据类型：** `Boolean`

## 参数

### 主选项卡

### **显示奇异性状态** — 显示奇异性状态 `off` (默认) | `on`

选择此项可在端口 **S** 输出输入的奇异性，该端口输出 Boolean 数据类型的值 1 或 0。输出 1 表示当前输入奇异，输出 0 表示当前输入非奇异。

### 数据类型选项卡

### **舍入模式** — 舍入操作的方法 `Floor` (默认) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅舍入模式。

### **整数溢出时饱和** — 溢出操作的方法 `off` (默认) | `on`

当选择此参数时，模块会对其定点运算的结果进行饱和处理。当清除此参数时，模块会对其定点运算的结果进行回绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **乘积输出** — 乘积输出数据类型 `Inherit: Inherit via internal rule` (默认) | `Inherit: Same as input` | `fixdt(1,16,0)`

**乘积输出** 指定 LU Factorization 模块中乘积运算输出的数据类型。有关乘积输出数据类型的更多信息，请参阅 Fixed-Point Data Types 和 Multiplication Data Types。

- `Inherit: Inherit via internal rule`
  — 模块基于内部规则继承乘积输出数据类型。有关此规则的更多信息，请参阅 Inherit via Internal Rule。
- `Inherit: Same as input` — 模块将乘积输出数据类型指定为与输入数据类型相同。
- `fixdt(1,16,0)` — 模块指定一个有符号、二进制点、定标、定点数据类型，字长为 16 位，小数长度为 0。

或者，可以使用 **数据类型助手** 设置 **乘积输出** 数据类型。要使用该助手，请单击 **显示数据类型助手** 按钮 。

有关数据类型助手的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **累加器** — 累加器数据类型 `Inherit: Inherit via internal rule` (默认) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

**累加器** 指定 LU Factorization 模块中累加运算输出的数据类型。有关如何在此模块中使用累加器数据类型的更多信息，请参阅 Fixed-Point Data Types 一节。

- `Inherit: Inherit via internal rule`
  — 模块基于内部规则继承累加器数据类型。有关此规则的更多信息，请参阅 Inherit via Internal Rule。
- `Inherit: Same as input` — 模块将累加器数据类型指定为与输入数据类型相同。
- `Inherit: Same as product output`
  — 模块将累加器数据类型指定为与乘积输出数据类型相同。
- `fixdt(1,16,0)` — 模块指定一个有符号、二进制点定标、定点数据类型，字长为 16 位，小数长度为 0。

或者，可以使用 **数据类型助手** 设置 **累加器** 数据类型。要使用该助手，请单击 **显示数据类型助手** 按钮 。

有关数据类型助手的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **输出** — 输出数据类型 `Inherit: Same as input` (默认) | `fixdt(1,16,0)`

**输出** 指定 LU Factorization 模块输出的数据类型。有关输出数据类型的更多信息，请参阅 Fixed-Point Data Types 一节。

- `Inherit: Same as input` — 模块将输出数据类型指定为与输入数据类型相同。
- `fixdt(1,16,0)` — 模块指定一个有符号、二进制点定标、定点数据类型，字长为 16 位，小数长度为 0。

或者，可以使用 **数据类型助手** 设置 **输出** 数据类型。要使用该助手，请单击 **显示数据类型助手** 按钮。

有关数据类型助手的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **输出最小值** — 模块可输出的最小值 `[]` (默认) | scalar

指定模块可输出的最小值。Simulink® 软件使用此最小值来执行：

- 仿真范围检查。请参阅 Specify Signal Ranges (Simulink)。
- 定点数据类型的自动定标。

### **输出最大值** — 模块可输出的最大值 `[]` (默认) | scalar

指定模块可输出的最大值。Simulink 软件使用此最大值来执行：

- 仿真范围检查。请参阅 Specify Signal Ranges (Simulink)。
- 定点数据类型的自动定标。

### **锁定数据类型设置以防止定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。

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

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

将方阵分解为下三角和上三角分量

LU Factorization 模块将方阵输入矩阵 *A* 的行置换版本分解为 *A*p = *L*\**U*，其中 *L* 是单位下三角矩阵，*U* 是上三角矩阵，且 *A*p 包含按置换索引向量 *P* 指示进行置换后的 *A* 的行。模块使用主元矩阵 *A*p 而不是精确的输入矩阵 *A*，因为它提高了分解的数值精度。
