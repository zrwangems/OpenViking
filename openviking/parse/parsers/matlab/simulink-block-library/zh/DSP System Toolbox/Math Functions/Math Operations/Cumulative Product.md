---
type: simulink-block
title: 'Cumulative Product'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Math Operations'
documentation_page: 'cumulativeproduct'
documentation_source_path: 'ref/cumulativeproduct.html'
language: zh-CN
chinese_source: worker-translation
---

# Cumulative Product

## 端口

### 输入

### **In** — 输入信号 向量 | 矩阵

将输入信号指定为向量或矩阵。

在将 **Reset port** 参数设置为 `None` 以外的任何值之前，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是

### **Rst** — 复位端口 标量

可选的复位端口 **Rst** 接受标量值，可以是任何内置 Simulink® 数值数据类型，包括 `boolean`。
**Rst** 端口输入的速率必须与输入数据信号的速率相同或更慢。**Rst** 端口输入的采样时间必须是输入采样时间的正整数倍。

有关此端口的详细信息，请参阅 Resetting Running Product。

#### 依赖关系

在将 **Reset port** 参数设置为 `None` 以外的任何值之前，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Out** — 累积乘积 向量 | 矩阵

信号的累积乘积，以向量或矩阵形式返回。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是

## 参数

### 主选项卡

### **Multiply input along** — 沿哪个维度计算输入的乘积 `Channels (running product)`（默认）| `Columns` | `Rows`

指定沿哪个维度计算累积乘积。您可以将此参数设置为以下选项之一：

- `Channels (running product)`
- `Columns`
- `Rows`

有关详细信息，请参阅以下部分：

- Computing Running Product Along Channels of Input
- Multiplying Along Columns
- Multiplying Along Rows

### **Input processing** — 输入处理 `Columns as channels (frame based)`（默认）| `Elements as channels (sample based)`

指定在沿输入通道计算运行乘积时模块应如何处理输入。您可以将此参数设置为以下选项之一：

- `Columns as channels (frame based)`
  — 模块将输入的每一列视为单独的通道。
- `Elements as channels (sample based)`
  — 模块将输入的每个元素视为单独的通道。

有关详细信息，请参阅 Computing Running Product Along Channels of Input。

#### 依赖关系

要启用此参数，请将 **Multiply input along** 参数设置为 `Channels (running product)`。

### **Reset port** — 复位类型 `None`（默认）| `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

指定导致模块沿通道复位乘积的复位事件。您可以将此参数设置为以下选项之一：

- `None`
- `Rising edge`
- `Falling edge`
- `Either edge`
- `Non-zero sample`

有关这些选项的详细信息，请参阅 Resetting Running Product。

#### 依赖关系

要启用此参数，请将 **Multiply input along** 参数设置为 `Channels (running product)`。

### 数据类型选项卡

**注意**

浮点继承优先于此窗格上定义的数据类型设置。当输入为浮点时，模块忽略这些设置，所有内部数据类型均为浮点。

### **Rounding mode** — 舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅 rounding mode。

### **Saturate on integer overflow** — 整数溢出时饱和 `off`（默认）| `on`

选中此参数时，模块对其定点运算的结果进行饱和处理。清除此参数时，模块对其定点运算的结果进行回绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅 overflow mode for fixed-point operations。

### **Intermediate product** — 中间乘积 `Inherit: Same as input`（默认）| `fixdt([],16,0)`

指定中间乘积数据类型。如 Fixed-Point Data Types 所示，乘法器的输出在下一个输入元素乘入之前被转换为中间乘积数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Same as input`
- 求值为有效数据类型的表达式，例如 `fixdt([],16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Product output** 参数。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Product output** — 乘积输出 `Inherit: Same as input`（默认）| `fixdt([],16,0)`

指定乘积输出数据类型。有关描述此模块中乘积输出数据类型使用的图示，请参阅 Fixed-Point Data Types 和 Multiplication Data Types。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Same as input`
- 求值为有效数据类型的表达式，例如 `fixdt([],16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Product output** 参数。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Accumulator** — 累加器 `Inherit: Same as input`（默认）| `Inherit: Same as product output` | `fixdt([],16,0)`

指定累加器数据类型。有关描述此模块中累加器数据类型使用的图示，请参阅 Fixed-Point Data Types。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Same as input`
- 继承数据类型的规则，例如 `Inherit: Same as product output`
- 求值为有效数据类型的表达式，例如 `fixdt([],16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Accumulator** 参数。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output** — 输出 `Inherit: Same as input`（默认）| `Inherit: Same as product output` | `fixdt([],16,0)`

指定输出数据类型。有关描述此模块中输出数据类型使用的图示，请参阅 Fixed-Point Data Types。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Same as input`
- 继承数据类型的规则，例如 `Inherit: Same as product output`
- 求值为有效数据类型的表达式，例如 `fixdt([],16,0)`

如果两个输入均为无符号，则所有数据类型（包括输出数据类型）均为无符号。如果其中一个输入为有符号，则内部数据类型和输出数据类型均为有符号。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Output** 参数。

有关更多信息，请参阅 Control Data Types of Signals (Simulink)。

### **Output Minimum** — 最小值 `[]`（默认）

指定模块必须输出的最小值。默认值为 `[]`（未指定）。Simulink 使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

### **Output Maximum** — 最大值 `[]`（默认）

指定模块必须输出的最大值。默认值为 `[]`（未指定）。Simulink 使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。

## 所属库

DSP System Toolbox / Math Functions / Math Operations

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

**在 R2006a 之前推出**

## 描述

通道、列或行元素的累积乘积

Cumulative Product 模块沿输入的指定维度或跨时间（运行乘积）计算累积乘积。
