---
type: simulink-block
title: 'Autocorrelation'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'autocorrelation'
documentation_source_path: 'ref/autocorrelation.html'
language: zh-CN
chinese_source: worker-translation
---

# Autocorrelation

## 端口

### 输入

### **Port\_1** — 数据输入向量 | 矩阵 | *N* 维数组

数据输入。该模块接受实值或复值多通道和多维输入。当您将 **计算域** 设置为 `Time` 时，输入可以是定点信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** Yes

### 输出

### **Port\_1** — 自相关输出向量 | 矩阵 | *N* 维数组

数据输入的自相关输出。

- 当输入为 *M*×*N* 矩阵 *u* 时，输出 *y* 为 (*l*+1)×*N* 矩阵。*l* 是自相关的最大正滞后。
- 当输入为 *N* 维数组时，模块输出 *N* 维数组。第一维的大小为 *l*+1，所有其他维的大小与输入数组匹配。例如，当输入为 *M*×*N*×*P* 数组时，模块输出 (*l*+1)×*N*×*P* 数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** Yes

## 参数

### 主选项卡

### **计算所有非负滞后** — 在所有非负滞后上计算自相关 on（默认）| off

当您选择此参数时，Autocorrelation 模块计算范围 [0, `length(input)` – 1] 内所有非负滞后的自相关。当您清除此参数时，模块使用范围 [0, *l*] 内的滞后计算自相关，其中 *l* 是您在 **最大非负滞后（小于输入长度）** 中指定的值。

### **最大非负滞后（小于输入长度）** — 最大正滞后 `1`（默认）| 大于等于 0 且小于输入长度的整数

用于自相关的最大正滞后，指定为大于等于 0 且小于输入长度的整数。

#### 依赖关系

要启用此参数，请清除 **计算所有非负滞后** 参数。

### **缩放** — 输出的缩放 `None`（默认）| `Biased` | `Unbiased` | `Unity at zero-lag`

应用于输出的缩放。

- `None` — 生成未经归一化的原始自相关 *yi,j*。
- `Biased` — 生成自相关的有偏估计。

  yi,jbiased=yi,jM
- `Unbiased` — 生成自相关的无偏估计。

  yi,junbiased=yi,jM−i
- `Unity at zero-lag` — 对每个通道的自相关估计进行归一化，使零滞后和（每列的第一个元素）恒为 1。

  y0,j=1

### **计算域** — 模块计算自相关的域 `Time`（默认）| `Frequency`

- `Time` — 在时域中计算卷积，可最大限度减少内存使用。
- `Frequency` — 在频域中计算自相关。有关详细信息，请参阅算法。

要对定点信号进行自相关，请将此参数设置为 `Time`。

### 数据类型选项卡

**注意**

定点信号仅支持时域。要使用这些参数，请在 **主** 选项卡上将 **计算域** 设置为 `Time`。

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

**注意**

当满足以下所有条件时，**舍入模式** 和 **整数溢出时饱和** 参数对数值结果没有影响：

- **乘积输出** 数据类型为 `Inherit: Inherit via internal rule`。
- **累加器** 数据类型为 `Inherit: Inherit via internal rule`。
- **输出** 数据类型为 `Inherit: Same as accumulator`。

使用这些数据类型设置时，模块以全精度模式运行。

### **整数溢出时饱和** — 溢出操作的方法 off（默认）| on

当您选择此参数时，模块对其定点运算的结果进行饱和。当您清除此参数时，模块对其定点运算的结果进行环绕。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

**注意**

当满足以下所有条件时，**舍入模式** 和 **整数溢出时饱和** 参数对数值结果没有影响：

- **乘积输出** 数据类型为 `Inherit: Inherit via internal rule`。
- **累加器** 数据类型为 `Inherit: Inherit via internal rule`。

使用这些数据类型设置时，模块以全精度模式运行。

### **乘积输出** — 乘积输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `fixdt([],16,0)`

**乘积输出** 指定 Autocorrelation 模块中乘积运算输出的数据类型。有关乘积输出数据类型的详细信息，请参阅乘法数据类型和定点数据类型。

- `Inherit: Inherit via internal rule` — 模块基于内部规则继承乘积输出数据类型。有关此规则的详细信息，请参阅通过内部规则继承。
- `Inherit: Same as input` — 模块将乘积输出数据类型指定为与输入数据类型相同。
- `fixdt([],16,0)` — 模块指定一个自动有符号、二进制点、定标的定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **数据类型助手** 设置 **乘积输出** 数据类型。要使用该助手，请点击 **显示数据类型助手** 按钮。

有关数据类型助手的详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **累加器** — 累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt([],16,0)`

**累加器** 指定 Autocorrelation 模块中累加运算输出的数据类型。有关在此模块中如何使用累加器数据类型的说明，请参阅定点数据类型。

- `Inherit: Inherit via internal rule` — 模块基于内部规则继承累加器数据类型。有关此规则的详细信息，请参阅通过内部规则继承。
- `Inherit: Same as input` — 模块将累加器数据类型指定为与输入数据类型相同。
- `Inherit: Same as product output` — 模块将累加器数据类型指定为与乘积输出数据类型相同。
- `fixdt([],16,0)` — 模块指定一个自动有符号、二进制点、定标的定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **数据类型助手** 设置 **累加器** 数据类型。要使用该助手，请点击 **显示数据类型助手** 按钮。

有关数据类型助手的详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **输出** — 输出数据类型 `Inherit: Same as accumulator`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt([],16,0)`

**输出** 指定 Autocorrelation 模块输出的数据类型。有关输出数据类型的详细信息，请参阅定点数据类型。

- `Inherit: Same as input` — 模块将输出数据类型指定为与输入数据类型相同。
- `Inherit: Same as product output` — 模块将输出数据类型指定为与乘积输出数据类型相同。
- `Inherit: Same as accumulator` — 模块将输出数据类型指定为与累加器数据类型相同。
- `fixdt([],16,0)` — 模块指定一个自动有符号、二进制点、定标的定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **数据类型助手** 设置 **输出** 数据类型。要使用该助手，请点击 **显示数据类型助手** 按钮。

有关数据类型助手的详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **输出最小值** — 模块可以输出的最小值 `[]`（默认）| 标量

指定模块可以输出的最小值。Simulink® 软件使用此最小值执行：

- 仿真范围检查。请参阅指定信号范围 (Simulink)。
- 定点数据类型的自动定标。

### **输出最大值** — 模块可以输出的最大值 `[]`（默认）| 标量

指定模块可以输出的最大值。Simulink® 软件使用此最大值执行：

- 仿真范围检查。请参阅指定信号范围 (Simulink)。
- 定点数据类型的自动定标。

### **锁定数据类型设置，防止定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。

## 所属库

DSP System Toolbox / Statistics

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

N 维数组的 Autocorrelation

Autocorrelation 模块沿 *N* 维输入数组的第一维计算自相关。计算可在时域或频域中完成。您可以通过 **计算域** 参数指定域。在时域中，输入信号与其时间反转复共轭进行卷积。在频域中，模块通过对输入信号进行傅里叶变换、将傅里叶变换与其共轭相乘，并计算乘积的傅里叶逆变换来计算自相关。在此域中，根据输入长度，模块可能需要更少的计算。有关这两种计算方法的详细信息，请参阅算法。

您可以使用 **计算所有非负滞后** 和 **最大非负滞后（小于输入长度）** 参数指定自相关的最大滞后。

当您将 **计算域** 设置为 `Time` 时，该模块接受定点信号。
