---
type: simulink-block
title: 'LDL Factorization'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Linear Algebra / Matrix Factorization'
documentation_page: 'ldlfactorization'
documentation_source_path: 'ref/ldlfactorization.html'
language: zh-CN
chinese_source: worker-translation
---

# LDL Factorization

## 端口

### 输入

### **Port\_1** — 输入信号矩阵

输入信号，指定为方阵。

算法要求输入为方阵且为 Hermitian 正定矩阵。当输入不是正定时，模块按 **非正定输入** 参数指定的方式作出反应。

如果输入为定点，则它必须是有符号整数或具有 2 的幂斜率且零偏置的有符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### 输出

### **Port\_1** — 输出信号矩阵

输出是一个复合矩阵，其中下三角元素 *lij* 来自 *L*，对角元素 *dij* 来自 *D*，上三角元素 *uij* 来自 *L\**，其中 *L* 是下三角方阵且其对角元素为单位元素，*D* 是对角矩阵，*L\** 是 *L* 的 Hermitian（复共轭）转置。

下面显示了 5×5 矩阵的输出格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

## 参数

### 主选项卡

### **非正定输入** — 非正定输入操作 `Warning`（默认） | `Ignore` | `Error`

指定当出现非正定矩阵输入时要执行的操作：

- `Ignore` — 继续计算且不发出警报。输出不是有效的分解。部分分解存在于输出的左上角。
- `Warning` — 在 MATLAB® 命令窗口中显示警告消息并继续仿真。输出不是有效的分解。部分分解存在于输出的左上角。
- `Error` — 显示错误对话框并终止仿真。

### 数据类型选项卡

### **舍入模式** — 舍入操作的方法 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式，为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅舍入模式。

### **整数溢出时饱和** — 溢出操作的方法 off（默认） | on

当您选择此参数时，模块会对其定点运算的结果进行饱和处理。当您清除此参数时，模块会对其定点运算的结果进行绕回处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **中间乘积** — 中间乘积数据类型 `Inherit: Same as input`（默认） | `fixdt(1,16,0)`

指定中间乘积数据类型。如定点数据类型中所示，乘法器的输出在输入的下一个元素乘入其中之前，会被转换为中间乘积数据类型。您可以将数据类型设置为：

- 继承数据类型的规则，例如 `Inherit: Same as input`
- 求值为有效数据类型的表达式，例如 `fixdt(1,16,0)`

或者，您可以使用 **数据类型助手** 设置 **中间乘积** 数据类型。要使用该助手，请点击 **显示数据类型助手** 按钮。

有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **乘积输出** — 乘积输出数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Same as input` | `fixdt([],16,0)`

**乘积输出** 指定 LDL Factorization 模块中乘积运算输出的数据类型。

- `Inherit: Inherit via internal rule` — 模块根据内部规则继承乘积输出数据类型。有关此规则的详细信息，请参阅通过内部规则继承。
- `Inherit: Same as input` — 模块将乘积输出数据类型指定为与输入数据类型相同。
- `fixdt([],16,0)` — 模块指定一个自动符号、二进制小数点、定标的定点数据类型，其字长为 16 位，小数长度为 0。

有关详细信息，请参阅乘法数据类型和定点数据类型。

或者，您可以使用 **数据类型助手** 设置 **乘积输出** 数据类型。要使用该助手，请点击 **显示数据类型助手** 按钮。

有关数据类型助手的详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **累加器** — 累加器数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt([],16,0)`

**累加器** 指定 LDL Factorization 模块中累加运算输出的数据类型。

- `Inherit: Inherit via internal rule` — 模块根据内部规则继承累加器数据类型。有关此规则的详细信息，请参阅通过内部规则继承。
- `Inherit: Same as input` — 模块将累加器数据类型指定为与输入数据类型相同。
- `Inherit: Same as product output` — 模块将累加器数据类型指定为与乘积输出数据类型相同。
- `fixdt([],16,0)` — 模块指定一个自动符号、二进制小数点、定标的定点数据类型，其字长为 16 位，小数长度为 0。

有关如何在此模块中使用累加器数据类型的说明，请参阅定点数据类型。

或者，您可以使用 **数据类型助手** 设置 **累加器** 数据类型。要使用该助手，请点击 **显示数据类型助手** 按钮。

有关数据类型助手的详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **输出** — 输出数据类型 `Inherit: Same as input`（默认） | `fixdt([],16,0)`

**输出** 指定 LDL Factorization 模块输出的数据类型。有关输出数据类型的详细信息，请参阅定点数据类型。

- `Inherit: Same as input` — 模块将输出数据类型指定为与输入数据类型相同。
- `fixdt([],16,0)` — 模块指定一个自动符号、二进制小数点、定标的定点数据类型，其字长为 16 位，小数长度为 0。

或者，您可以使用 **数据类型助手** 设置 **输出** 数据类型。要使用该助手，请点击 **显示数据类型助手** 按钮。

有关数据类型助手的详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **输出最小值** — 模块可以输出的最小值 `[]`（默认） | 标量

指定模块可以输出的最小值。Simulink 软件使用此最小值执行：

- 仿真范围检查。请参阅指定信号范围 (Simulink)。
- 定点数据类型的自动定标。

### **输出最大值** — 模块可以输出的最大值 `[]`（默认） | 标量

指定模块可以输出的最大值。Simulink 软件使用此最大值执行：

- 仿真范围检查。请参阅指定信号范围 (Simulink)。
- 定点数据类型的自动定标。

### **锁定数据类型设置以防止定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

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

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

将方阵 Hermitian 正定矩阵分解为下三角、上三角和对角分量

LDL Factorization 模块将方阵 Hermitian 正定输入矩阵 S 唯一分解为

S=LDL\*

其中 *L* 是下三角方阵且其对角元素为单位元素，*D* 是对角矩阵，*L\** 是 *L* 的 Hermitian（复共轭）转置。仅使用输入矩阵的对角线和下三角部分。对角元素的任何虚部都会被忽略。

LDL 分解所需的计算量是高斯消元（LU 分解）的一半，并且始终稳定。它比 Cholesky 分解更高效，因为它避免计算对角元素的平方根。
