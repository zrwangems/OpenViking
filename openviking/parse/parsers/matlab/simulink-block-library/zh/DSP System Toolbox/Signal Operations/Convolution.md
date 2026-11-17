---
type: simulink-block
title: 'Convolution'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'convolution'
documentation_source_path: 'ref/convolution.html'
language: zh-CN
chinese_source: worker-translation
---

# Convolution

## 端口

### 输入

### **Port\_1** — 第一个输入信号 标量 | 向量 | 矩阵 | *N* 维数组

第一个输入 *u*，指定为标量、向量、矩阵或 *N* 维数组。当两个输入均为实数时，输出为实数。当一个或两个输入为复数时，输出为复数。两个输入的所有输入端口维度（除第一个维度外）必须具有相同的值。

输入 *u* 和 *v* 在超出其有效范围进行索引时为零。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是

### **Port\_2** — 第二个输入信号 标量 | 向量 | 矩阵 | *N* 维数组

第二个输入 *v*，指定为标量、向量、矩阵或 *N* 维数组。当两个输入均为实数时，输出为实数。当一个或两个输入为复数时，输出为复数。两个输入的所有输入端口维度（除第一个维度外）必须具有相同的值。

输入 *u* 和 *v* 在超出其有效范围进行索引时为零。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵 | *N* 维数组

卷积后的信号，根据输入信号返回为标量、向量、矩阵或 *N* 维数组。当两个输入均为实数时，输出为实数。当一个或两个输入为复数时，输出为复数。输入 *u* 和 *v* 在超出其有效范围进行索引时为零。有关卷积信号如何根据输入变化的更多详细信息，请参阅详细信息。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是

## 参数

### 主选项卡

### **Computation domain** — 计算域 `Time`（默认）| `Frequency` | `Fastest`

设置模块计算卷积所在的域：

- `Time` — 模块在时域中计算，可最大限度地减少内存使用。
- `Frequency` — 模块在频域中计算，根据输入长度，可能比在时域中计算需要更少的计算量。
- `Fastest` — 模块在使计算次数最少的域中计算。

定点信号仅在时域中受支持。输入定点信号时，请确保将 **Computation domain** 参数设置为 `Time`。

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

**注意**

当满足以下所有条件时，**Rounding mode** 和 **Saturate on integer overflow** 参数对数值结果没有影响：

- **Product output** 数据类型为 `Inherit: Inherit via internal rule`。
- **Accumulator** 数据类型为 `Inherit: Inherit via internal rule`。
- **Output** 数据类型为 `Inherit: Same as accumulator`。

使用这些数据类型设置时，模块以全精度模式运行。

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

选中此参数时，模块对其定点运算的结果进行饱和处理。清除此参数时，模块对其定点运算的结果进行环绕处理。有关*饱和*和*环绕*的详细信息，请参阅定点运算的溢出处理。

**注意**

当满足以下所有条件时，**Rounding mode** 和 **Saturate on integer overflow** 参数对数值结果没有影响：

- **Product output** 数据类型为 `Inherit: Inherit via internal rule`。
- **Accumulator** 数据类型为 `Inherit: Inherit via internal rule`。
- **Output** 数据类型为 `Inherit: Same as accumulator`。

使用这些数据类型设置时，模块以全精度模式运行。

### **Product output** — 乘积输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as first input` | `fixdt([],16,0)`

**Product output** 指定 Convolution 模块中乘积运算输出的数据类型。

- `Inherit: Inherit via internal rule` — 模块根据内部规则继承乘积输出数据类型。有关此规则的更多信息，请参阅通过内部规则继承。
- `Inherit: Same as first input` — 模块将乘积输出数据类型指定为与第一个输入数据类型相同。
- `fixdt([],16,0)` — 模块指定一个自动有符号、二进制点、定标、定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用**数据类型助手**设置 **Product output** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮。

有关数据类型助手的更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

有关乘积输出数据类型的更多信息，请参阅乘法数据类型和定点数据类型。

### **Accumulator** — 累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as first input` | `Inherit: Same as product output` | `fixdt([],16,0)`

**Accumulator** 指定 Convolution 模块中累加运算输出的数据类型。

- `Inherit: Inherit via internal rule` — 模块根据内部规则继承累加器数据类型。有关此规则的更多信息，请参阅通过内部规则继承。
- `Inherit: Same as first input` — 模块将累加器数据类型指定为与第一个输入数据类型相同。
- `Inherit: Same as product output` — 模块将累加器数据类型指定为与乘积输出数据类型相同。
- `fixdt([],16,0)` — 模块指定一个自动有符号、二进制点、定标、定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用**数据类型助手**设置 **Accumulator** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮。

有关数据类型助手的更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

有关如何在此模块中使用累加器数据类型的图示表示，请参阅定点数据类型。

### **Output** — 输出数据类型 `Inherit: Same as accumulator`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt([],16,0)`

**Output** 指定 Convolution 模块输出的数据类型。

- `Inherit: Same as accumulator` — 模块将输出数据类型指定为与累加器数据类型相同。
- `Inherit: Same as first input` — 模块将输出数据类型指定为与第一个输入数据类型相同。
- `Inherit: Same as product output` — 模块将输出数据类型指定为与乘积输出数据类型相同。
- `fixdt([],16,0)` — 模块指定一个自动有符号、二进制点、定标、定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用**数据类型助手**设置 **Output** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮。

有关更多信息，请参阅控制信号的数据类型 (Simulink)。

有关输出数据类型的更多信息，请参阅定点数据类型。

### **Output Minimum** — 模块可以输出的最小值 `[]`（默认）| 标量

指定模块可以输出的最小值。Simulink 使用此最小值执行：

- 仿真范围检查。请参阅指定信号范围 (Simulink)。
- 定点数据类型的自动定标。

### **Output Maximum** — 模块可以输出的最大值 `[]`（默认）| 标量

指定模块可以输出的最大值。Simulink 使用此最大值执行：

- 仿真范围检查。请参阅指定信号范围 (Simulink)。
- 定点数据类型的自动定标。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。

## 所属库

DSP System Toolbox / Signal Operations

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

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

两个输入的卷积

Convolution 模块将 *N* 维输入数组 *u* 的第一个维度与 *N* 维输入数组 *v* 的第一个维度进行卷积。该模块还可以将列向量与 *N* 维输入数组的第一个维度进行卷积。

卷积的一般方程为：

y(k)=∑nu(n−k)v(k)

两个 DSP System Toolbox™ 模块可用于对两个输入信号进行卷积：

- Convolution
- Discrete FIR Filter (Simulink)

Convolution 模块假定 *u* 和 *v* 的所有元素在每个 Simulink® 时间步均可用，并在每一步计算整个卷积。

Discrete FIR Filter 模块可用于在以下情况下对信号进行卷积：*v* 的所有元素在每个时间步均可用，但 *u* 是在仿真生命周期内到达的序列。使用 Discrete FIR Filter 模块时，卷积仅计算一次。

要确定哪个模块最适合您的需求，请参阅选择合适的卷积模块。
