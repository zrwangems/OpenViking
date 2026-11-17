---
type: simulink-block
title: 'LDL Factorization'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Factorizations'
documentation_page: 'ldlfactorization'
documentation_source_path: 'ref/ldlfactorization.html'
language: zh-CN
chinese_source: worker-translation
---

# LDL Factorization

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: Port_1
  summary: 输出信号矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point
```

### 输入

### **Port\_1** — 输入信号矩阵

输入信号，指定为方阵。

该算法要求输入为方阵且为 Hermitian 正定矩阵。当输入不是正定矩阵时，该模块将按照 **Non-positive definite input** 参数指定的方式作出响应。

如果输入为定点类型，则它必须是有符号整数或具有 2 的幂斜率且零偏置的有符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### 输出

### **Port\_1** — 输出信号矩阵

输出是一个复合矩阵，其下三角元素为来自 *L* 的 *lij*，对角元素为来自 *D* 的 *dij*，上三角元素为来自 *L\** 的 *uij*，其中 *L* 是下三角方阵且对角元素为单位值，*D* 是对角矩阵，*L\** 是 *L* 的 Hermitian（复共轭）转置。

下面显示了 5×5 矩阵的输出格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
## 参数
```yaml
parameters:
- name: Non-positive definite input
  summary: 非正定输入操作 Warning（默认）| Ignore | Error
  group: 主选项卡
- name: Rounding mode
  summary: 舍入操作的方法 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型选项卡
- name: Saturate on integer overflow
  summary: 溢出操作的方法 off（默认）| on
  group: 数据类型选项卡
- name: Intermediate product
  summary: '中间乘积数据类型 Inherit: Same as input（默认）| fixdt(1,16,0)'
  group: 数据类型选项卡
- name: Product output
  summary: '乘积输出数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | fixdt([],16,0)'
  group: 数据类型选项卡
- name: Accumulator
  summary: '累加器数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | Inherit: Same as product output | fixdt([],16,0)'
  group: 数据类型选项卡
- name: Output
  summary: '输出数据类型 Inherit: Same as input（默认）| fixdt([],16,0)'
  group: 数据类型选项卡
- name: Output Minimum
  summary: 模块可以输出的最小值 []（默认）| 标量
  group: 数据类型选项卡
- name: Output Maximum
  summary: 模块可以输出的最大值 []（默认）| 标量
  group: 数据类型选项卡
- name: Lock data type settings against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: 数据类型选项卡
```

### 主选项卡

### **Non-positive definite input** — 非正定输入操作 `Warning`（默认）| `Ignore` | `Error`

指定当出现非正定矩阵输入时要执行的操作：

- `Ignore` — 继续计算并且不发出警报。输出不是有效的分解。输出左上角存在部分分解。
- `Warning` — 在 MATLAB® 命令窗口中显示警告消息并继续仿真。输出不是有效的分解。输出左上角存在部分分解。
- `Error` — 显示错误对话框并终止仿真。

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

有关更多详细信息，请参阅舍入模式。

### **Saturate on integer overflow** — 溢出操作的方法 off（默认）| on

选中此参数时，该模块会对其定点运算的结果进行饱和处理。清除此参数时，该模块会对其定点运算的结果进行回绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **Intermediate product** — 中间乘积数据类型 `Inherit: Same as input`（默认）| `fixdt(1,16,0)`

指定中间乘积数据类型。如定点数据类型中所示，乘法器的输出在输入的下一个元素与其相乘之前会被转换为中间乘积数据类型。您可以将数据类型设置为：

- 继承数据类型的规则，例如 `Inherit: Same as input`
- 求值为有效数据类型的表达式，例如 `fixdt(1,16,0)`

或者，您可以使用 **Data Type Assistant** 设置 **Intermediate product** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Product output** — 乘积输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `fixdt([],16,0)`

**Product output** 指定 LDL Factorization 模块中乘积运算输出的数据类型。

- `Inherit: Inherit via internal rule` — 该模块基于内部规则继承乘积输出数据类型。有关此规则的更多信息，请参阅 Inherit via Internal Rule。
- `Inherit: Same as input` — 该模块将乘积输出数据类型指定为与输入数据类型相同。
- `fixdt([],16,0)` — 该模块指定自动有符号、二进制点缩放、字长为 16 位且小数长度为 0 的定点数据类型。

有关更多信息，请参阅 Multiplication Data Types 和 Fixed-Point Data Types。

或者，您可以使用 **Data Type Assistant** 设置 **Product output** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮。

有关数据类型助手的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Accumulator** — 累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt([],16,0)`

**Accumulator** 指定 LDL Factorization 模块中累加运算输出的数据类型。

- `Inherit: Inherit via internal rule` — 该模块基于内部规则继承累加器数据类型。有关此规则的更多信息，请参阅 Inherit via Internal Rule。
- `Inherit: Same as input` — 该模块将累加器数据类型指定为与输入数据类型相同。
- `Inherit: Same as product output` — 该模块将累加器数据类型指定为与乘积输出数据类型相同。
- `fixdt([],16,0)` — 该模块指定自动有符号、二进制点缩放、字长为 16 位且小数长度为 0 的定点数据类型。

有关如何在此模块中使用累加器数据类型的说明，请参阅 Fixed-Point Data Types。

或者，您可以使用 **Data Type Assistant** 设置 **Accumulator** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮。

有关数据类型助手的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output** — 输出数据类型 `Inherit: Same as input`（默认）| `fixdt([],16,0)`

**Output** 指定 LDL Factorization 模块输出的数据类型。有关输出数据类型的更多信息，请参阅 Fixed-Point Data Types。

- `Inherit: Same as input` — 该模块将输出数据类型指定为与输入数据类型相同。
- `fixdt([],16,0)` — 该模块指定自动有符号、二进制点缩放、字长为 16 位且小数长度为 0 的定点数据类型。

或者，您可以使用 **Data Type Assistant** 设置 **Output** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮。

有关数据类型助手的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output Minimum** — 模块可以输出的最小值 `[]`（默认）| 标量

指定模块可以输出的最小值。Simulink 软件使用此最小值来执行：

- 仿真范围检查。请参阅 Specify Signal Ranges (Simulink)。
- 定点数据类型的自动缩放。

### **Output Maximum** — 模块可以输出的最大值 `[]`（默认）| 标量

指定模块可以输出的最大值。Simulink 软件使用此最大值来执行：

- 仿真范围检查。请参阅 Specify Signal Ranges (Simulink)。
- 定点数据类型的自动缩放。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

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

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

将方阵 Hermitian 正定矩阵分解为下三角、上三角和对角分量

LDL Factorization 模块将方阵 Hermitian 正定输入矩阵 S 唯一分解为

S=LDL\*

其中 *L* 是具有单位对角元素的下三角方阵，*D* 是对角矩阵，*L\** 是 *L* 的 Hermitian（复共轭）转置。仅使用输入矩阵的对角线和下三角部分。对角元素的任何虚部都会被忽略。

LDL 分解所需的计算量是高斯消元（LU 分解）的一半，并且始终稳定。它比 Cholesky 分解更高效，因为它避免了计算对角元素的平方根。
