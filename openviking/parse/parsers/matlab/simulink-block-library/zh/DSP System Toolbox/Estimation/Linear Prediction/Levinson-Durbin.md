---
type: simulink-block
title: 'Levinson-Durbin'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Linear Prediction'
documentation_page: 'levinsondurbin'
documentation_source_path: 'ref/levinsondurbin.html'
language: zh-CN
chinese_source: worker-translation
---

# Levinson-Durbin

## 端口

### 输入

### **Input** — 输入向量 | 矩阵

指定模块的输入，`r =``[r(1)
r(2) ...
r(n+1)]` 为向量或矩阵。如果输入是矩阵，模块将每一列视为独立通道并分别求解。输入的每个通道包含自相关序列的滞后 *0* 到 *n*，它们出现在矩阵 *R* 中。

如果输入是定点，它必须是有符号整数或具有 power-of-two slope 和 zero bias 的有符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是

### 输出

### **A** — 模型系数向量 | 矩阵

模型系数 *A*，以向量或矩阵形式返回。*A* 与输入具有相同的维度。

对于每个通道，端口 **A** 输出 `A =` `[1
a(2) a(3) ...
a(n+1)]`，即 Levinson-Durbin 方程的解。您还可以将每个输出通道的元素视为 *n* 阶自回归 (AR) 过程的系数。

#### 依赖关系

要启用此端口，请将 **Output(s)** 设置为 `A and K` 或 `A`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是

### **K** — 反射系数向量 | 矩阵

反射系数 *K*，以向量或矩阵形式返回。*K* 与输入具有相同的维度，但少一个元素。

对于每个通道，端口 **K** 输出 `K =``[k(1)
k(2) ...
k(n)]`，其中包含 *n* 个反射系数。

当您选择 `K` 时，标量输入通道会导致错误。您可以使用反射系数来实现 AR 过程的格型表示。有关更多详细信息，请参阅 Applications。

#### 依赖关系

要启用此端口，请将 **Output(s)** 设置为 `A and K` 或 `K`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是

### **P** — 输出预测误差功率向量

输出预测误差功率 *P*，以长度等于输入通道数的向量形式返回。向量中的每个元素是每个通道的预测误差功率。

对于每个通道，*P* 表示一个 FIR 滤波器输出的功率，该滤波器抽头为 *A*，输入自相关由 *r* 描述，其中 *A* 表示预测误差滤波器，*r* 是模块的输入。在这种情况下，*A* 是白化滤波器。*P* 每个输入通道有一个元素。

#### 依赖关系

要启用此端口，请选中 **Output prediction error
power (P)** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

## 参数

### 主选项卡

### **Output(s)** — Output(s) `K`（默认） | `A and K` | `A`

指定要输出的 *R**a* = *b* 的解表示：

- 多项式系数 (`A`) –– 对于每个通道，端口 **A** 输出 `A =``[1 a(2)
  a(3) ...
  a(n+1)]`，即 Levinson-Durbin 方程的解。*A* 与输入具有相同的维度。您还可以将每个输出通道的元素视为 *n* 阶自回归 (AR) 过程的系数。
- 反射系数 (`K`) –– 对于每个通道，端口 **K** 输出 `K =``[k(1)
  k(2) ...
  k(n)]`，其中包含 *n* 个反射系数，并且与输入具有相同的维度，但少一个元素。当您选择 `K` 时，标量输入通道会导致错误。您可以使用反射系数来实现本页后面描述的 AR 过程的格型表示。
- 模型系数和反射系数两者 (`A and K`) –– 模块在各自端口输出两种表示。当您选择 `A and K` 时，标量输入通道会导致错误。

当输入是标量或行向量时，您必须将此参数设置为 `A`。

### **Output prediction error power (P)** — Output prediction error power `off`（默认） | `on`

选中此参数以在端口 **P** 输出每个通道的预测误差功率。

### **If the value of lag 0 is zero, A=[1 zeros], K=[zeros], P=0** — If the value of lag 0 is zero, A=[1 zeros], K=[zeros], P=0 `on`（默认） | `off`

当您选中此复选框且输入的第一个元素 `r(1)` 为零时，模块会相应地输出以下向量：

- `A = [1 zeros(1,n)]`
- `K = [zeros(1,n)]`
- `P = 0`

当您清除此复选框时，对于 `r`(1) 元素为零的每个通道，模块会输出一个 `NaN` 向量。通常，*r*(1) = `0` 的输入是无效的，因为它不能构造正定矩阵 *R*。然而，模块在仿真开始时经常会接收零值输入。此复选框允许您在此期间避免传播 `NaN`。

### 数据类型选项卡

**注意**

浮点继承优先于在此窗格上定义的数据类型设置。当输入为浮点时，模块会忽略这些设置，所有内部数据类型均为浮点。

### **Rounding mode** — Rounding mode `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅舍入模式。

### **Saturate on integer overflow** — Saturate on integer overflow `off`（默认） | `on`

当您选中此参数时，模块会对其定点运算的结果进行饱和处理。当您清除此参数时，模块会对其定点运算的结果进行回绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **Product output** — Product output `Inherit: Same as input`（默认） | numeric type

指定 product output 数据类型为 `Inherit: Same as input` 或 numeric type。请参阅 Fixed-Point Data Types 和 Multiplication Data Types，了解此模块中 product output 数据类型的用法说明。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Same as input`
- 求值为有效数据类型的表达式，例如 `fixdt(1,16,0)`

点击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置 **Product output** 参数。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Accumulator** — Accumulator `Inherit: Same as input`（默认） | `Inherit: Same as product output` | numeric type

指定 accumulator 数据类型为 `Inherit: Same as input`、`Inherit: Same as product output` 或 numeric type。请参阅 Fixed-Point Data Types，了解此模块中 accumulator 数据类型的用法说明。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Same as input`
- 继承数据类型的规则，例如 `Inherit: Same as product output`
- 求值为有效数据类型的表达式，例如 `fixdt(1,16,0)`

点击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置 **Accumulator** 参数。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Polynomial coefficients (A)** — Polynomial coefficients data type `fixdt(1,16,0)`（默认） | numeric type

指定多项式系数 (*A*) 数据类型为 numeric type。请参阅 Fixed-Point Data Types，了解此模块中 A 数据类型的用法说明。您可以将其设置为求值为有效数据类型的表达式，例如 `fixdt(1,16,10)`。

点击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置 **A** 参数。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Reflection coefficients (K)** — Reflection coefficients data type `fixdt(1,16,0)`（默认） | numeric type

指定反射系数 (*K*) 数据类型为 numeric type。请参阅 Fixed-Point Data Types，了解此模块中 K 数据类型的用法说明。您可以将其设置为求值为有效数据类型的表达式，例如 `fixdt(1,16,10)`。

点击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置 **K** 参数。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Prediction error power (P)** — Prediction error power data type `Inherit: Same as input`（默认） | numeric type

指定预测误差功率 (*P*) 数据类型为 `Inherit: Same as input` 或 numeric type。请参阅 Fixed-Point Data Types，了解此模块中 P 数据类型的用法说明。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Same as input`
- 求值为有效数据类型的表达式，例如 `fixdt(1,16,0)`

点击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置 **P** 参数。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Minimum** — Minimum values of polynomial coefficients, reflection coefficients, or prediction error power `[]`（默认） | scalar

指定多项式系数、反射系数或预测误差功率应具有的最小值。默认值为 `[]`（未指定）。Simulink® 使用此值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）
- 定点数据类型的自动定标

### **Maximum** — Maximum values of polynomial coefficients, reflection coefficients, or prediction error power `[]`（默认） | scalar

指定多项式系数、反射系数或预测误差功率应具有的最大值。默认值为 `[]`（未指定）。Simulink 使用此值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）
- 定点数据类型的自动定标

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off`（默认） | `on`

选中此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。

## 所属库

DSP System Toolbox / Estimation / Linear Prediction / Linear System Solvers DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Linear System Solvers

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

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 Levinson-Durbin 递推求解线性方程组

Levinson-Durbin 模块求解 *n* 阶线性方程组

*Ra* = *b*

在以下情况下：

- *R* 是 Hermitian、正定、Toeplitz 矩阵。
- *b* 与 *R* 的第一列相同，但偏移一个元素且符号相反。

[r(1)r\*(2)⋯r\*(n)r(2)r(1)⋯r\*(n−1)⋮⋮⋱⋮r(n)r(n−1)⋯r(1)] [a(2)a(3)⋮a(n+1)]=[−r(2)−r(3)⋮−r(n+1)]
