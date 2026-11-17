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
```yaml
ports:
- name: Input
  summary: 输入向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: A
  summary: 模型系数向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: K
  summary: 反射系数向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: P
  summary: 输出预测误差功率向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point
```

### 输入

### **Input** — 输入向量 | 矩阵

将模块的输入 `r =``[r(1)
r(2) ...
r(n+1)]` 指定为向量或矩阵。如果输入是矩阵，模块将每一列视为独立通道，并分别求解。输入的每个通道包含自相关序列从滞后 *0* 到滞后 *n* 的值，这些值出现在矩阵 *R* 中。

如果输入为定点，则它必须是有符号整数，或者是斜率为 2 的幂且偏置为零的有符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是
### 输出

### **A** — 模型系数向量 | 矩阵

模型系数 *A*，以向量或矩阵形式返回。*A* 的维度与输入相同。

对于每个通道，端口 **A** 输出 `A =` `[1
a(2) a(3) ...
a(n+1)]`，即 Levinson-Durbin 方程的解。您还可以将每个输出通道的元素视为一个 *n* 阶自回归 (AR) 过程的系数。

#### 依存关系

要启用此端口，请将 **Output(s)** 设置为 `A and K` 或 `A`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是

### **K** — 反射系数向量 | 矩阵

反射系数 *K*，以向量或矩阵形式返回。*K* 的维度与输入相同，但少一个元素。

对于每个通道，端口 **K** 输出 `K =``[k(1)
k(2) ...
k(n)]`，其中包含 *n* 个反射系数。

选择 `K` 时，标量输入通道会导致错误。您可以使用反射系数来实现 AR 过程的格型表示。有关更多详细信息，请参阅“应用”。

#### 依存关系

要启用此端口，请将 **Output(s)** 设置为 `A and K` 或 `K`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是

### **P** — 输出预测误差功率向量

输出预测误差功率 *P*，以向量形式返回，该向量的长度等于输入通道数。向量中的每个元素均为相应通道的预测误差功率。

对于每个通道，*P* 表示一个 FIR 滤波器的输出功率，该滤波器的抽头为 *A*，其输入自相关由 *r* 描述，其中 *A* 表示预测误差滤波器，*r* 是模块的输入。在这种情况下，*A* 是白化滤波器。*P* 中每个输入通道对应一个元素。

#### 依赖关系

要启用此端口，请选中**输出预测误差功率 (P)**复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
## 参数
```yaml
parameters:
- name: 输出
  summary: 输出 K（默认） | A and K | A
  group: 主选项卡
- name: 输出预测误差功率 (P)
  summary: 输出预测误差功率 off (默认) | on
  group: 主选项卡
- name: 如果滞后 0 处的值为零，则 A=[1 zeros], K=[zeros], P=0
  summary: 如果滞后 0 处的值为零，则 A=[1 zeros], K=[zeros], P=0 on (默认) | off
  group: 主选项卡
- name: 舍入模式
  summary: 舍入模式 Floor (默认) | Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型选项卡
- name: 整数溢出时饱和
  summary: 整数溢出时饱和 off (默认) | on
  group: 数据类型选项卡
- name: Product output
  summary: '乘积输出 Inherit: Same as input (默认) | 数值类型'
  group: 数据类型选项卡
- name: Accumulator
  summary: '累加器 Inherit: Same as input (默认) | Inherit: Same as product output | 数值类型'
  group: 数据类型选项卡
- name: 多项式系数 (A)
  summary: 多项式系数数据类型 fixdt(1,16,0)（默认）| 数值类型
  group: 数据类型选项卡
- name: 反射系数 (K)
  summary: 反射系数数据类型 fixdt(1,16,0)（默认）| 数值类型
  group: 数据类型选项卡
- name: 预测误差功率 (P)
  summary: '预测误差功率数据类型 Inherit: Same as input（默认）| 数值类型'
  group: 数据类型选项卡
- name: 最小值
  summary: 多项式系数、反射系数或预测误差功率的最小值 []（默认值）| 标量
  group: 数据类型选项卡
- name: 最大值
  summary: 多项式系数、反射系数或预测误差功率的最大值 []（默认值）| 标量
  group: 数据类型选项卡
- name: 锁定数据类型设置以防止定点工具更改
  summary: 防止定点工具覆盖数据类型 off（默认值）| on
  group: 数据类型选项卡
```

### 主选项卡

### **输出** — 输出 `K`（默认） | `A and K` | `A`

指定要输出的 *R**a* = *b* 的解的表示形式：

- 多项式系数 (`A`) –– 对于每个通道，端口 **A** 输出
  `A =``[1 a(2) a(3) ... a(n+1)]`，
  即 Levinson-Durbin 方程的解。*A* 的维度与输入相同。您还可以将每个输出通道的元素视为一个 *n* 阶自回归 (AR) 过程的系数。
- 反射系数 (`K`) –– 对于每个通道，端口 **K** 输出
  `K =``[k(1) k(2) ... k(n)]`，
  其中包含 *n* 个反射系数，其维度与输入相同，但少一个元素。选择 `K` 时，标量输入通道会导致错误。您可以使用反射系数来实现本页后文所述 AR 过程的格型表示。
- 模型系数和反射系数 (`A and K`) –– 模块在相应端口输出这两种表示形式。选择 `A and K` 时，标量输入通道会导致错误。

当输入为标量或行向量时，必须将此参数设置为 `A`。

### **输出预测误差功率 (P)** — 输出预测误差功率 `off` (默认) | `on`

选择此参数可在端口 **P** 输出每个通道的预测误差功率。

### **如果滞后 0 处的值为零，则 A=[1 zeros], K=[zeros], P=0** — 如果滞后 0 处的值为零，则 A=[1 zeros], K=[zeros], P=0 `on` (默认) | `off`

当选中此复选框且输入的第一个元素 `r(1)` 为零时，模块会根据情况输出以下向量：

- `A = [1 zeros(1,n)]`
- `K = [zeros(1,n)]`
- `P = 0`

当清除此复选框时，对于 `r`(1) 元素为零的每个通道，模块都会输出一个由 `NaN` 值组成的向量。通常，*r*(1) = `0` 的输入是无效的，因为它不能构造正定矩阵 *R*。但是，模块通常会在仿真开始时接收到零值输入。该复选框允许您避免在此期间传播 `NaN`。

### 数据类型选项卡

**注意**

浮点继承优先于此窗格中定义的数据类型设置。当输入为浮点时，模块会忽略这些设置，并且所有内部数据类型均为浮点。

### **舍入模式** — 舍入模式 `Floor` (默认) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为以下各项之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关详细信息，请参阅舍入模式。

### **整数溢出时饱和** — 整数溢出时饱和 `off` (默认) | `on`

当选中此参数时，模块会对其定点运算结果进行饱和处理。当清除此参数时，模块会对其定点运算结果进行绕回处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **Product output** — 乘积输出 `Inherit: Same as input` (默认) | 数值类型

将乘积输出数据类型指定为 `Inherit: Same as input` 或数值类型。有关此模块中乘积输出数据类型使用方式的图示，请参阅定点数据类型和乘法数据类型。可以将其设置为：

- 继承数据类型的规则，例如，
  `Inherit: Same as input`
- 计算结果为有效数据类型的表达式，例如，
  `fixdt(1,16,0)`

点击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可以帮助您设置 **Product output** 参数。

有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Accumulator** — 累加器 `Inherit: Same as input` (默认) | `Inherit: Same as product output` | 数值类型

将累加器数据类型指定为 `Inherit: Same as input`、`Inherit: Same as product output` 或数值类型。有关此模块中累加器数据类型使用方式的图示，请参阅定点数据类型。可以将其设置为：

- 继承数据类型的规则，例如，
  `Inherit: Same as input`
- 继承数据类型的规则，例如，
  `Inherit: Same as product output`
- 计算结果为有效数据类型的表达式，例如，
  `fixdt(1,16,0)`

点击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可以帮助您设置 **Accumulator** 参数。

有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **多项式系数 (A)** — 多项式系数数据类型 `fixdt(1,16,0)`（默认）| 数值类型

将多项式系数（*A*）数据类型指定为数值类型。有关此模块中 A 数据类型用法的图示，请参阅“定点数据类型”。可以将其设置为可计算为有效数据类型的表达式，例如 `fixdt(1,16,10)`。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置 **A** 参数。

有关详细信息，请参阅“使用数据类型助手指定数据类型 (Simulink)”。

### **反射系数 (K)** — 反射系数数据类型 `fixdt(1,16,0)`（默认）| 数值类型

将反射系数（*K*）数据类型指定为数值类型。有关此模块中 K 数据类型用法的图示，请参阅“定点数据类型”。可以将其设置为可计算为有效数据类型的表达式，例如 `fixdt(1,16,10)`。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置 **K** 参数。

有关详细信息，请参阅“使用数据类型助手指定数据类型 (Simulink)”。

### **预测误差功率 (P)** — 预测误差功率数据类型 `Inherit: Same as input`（默认）| 数值类型

将预测误差功率（*P*）数据类型指定为 `Inherit: Same as input` 或数值类型。有关此模块中 P 数据类型用法的图示，请参阅“定点数据类型”。可以将其设置为：

- 继承数据类型的规则，例如，
  `Inherit: Same as input`
- 可计算为有效数据类型的表达式，例如，
  `fixdt(1,16,0)`

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置 **P** 参数。

有关详细信息，请参阅“使用数据类型助手指定数据类型 (Simulink)”。

### **最小值** — 多项式系数、反射系数或预测误差功率的最小值 `[]`（默认值）| 标量

指定多项式系数、反射系数或预测误差功率应具有的最小值。默认值为 `[]`（未指定）。Simulink® 使用此值执行：

- 参数范围检查（请参阅为模块参数指定最小值和最大值（Simulink））
- 定点数据类型的自动定标

### **最大值** — 多项式系数、反射系数或预测误差功率的最大值 `[]`（默认值）| 标量

指定多项式系数、反射系数或预测误差功率应具有的最大值。默认值为 `[]`（未指定）。Simulink 使用此值执行：

- 参数范围检查（请参阅为模块参数指定最小值和最大值（Simulink））
- 定点数据类型的自动定标

### **锁定数据类型设置以防止定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认值）| `on`

选择此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。
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

在某些条件下，生成的代码依赖于 `memcpy` 或
`memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用 Levinson-Durbin 递归求解线性方程组

Levinson-Durbin 模块求解 *n* 阶
线性方程组

*Ra* = *b*

适用于以下情况：

- *R* 是埃尔米特、正定的托普利茨
  矩阵。
- *b* 与 *R* 的第一列相同，但平移了一个元素
  并取相反符号。

[r(1)r\*(2)⋯r\*(n)r(2)r(1)⋯r\*(n−1)⋮⋮⋱⋮r(n)r(n−1)⋯r(1)] [a(2)a(3)⋮a(n+1)]=[−r(2)−r(3)⋮−r(n+1)]
