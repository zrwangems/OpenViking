---
type: simulink-block
title: 'Cumulative Sum'
family: 'math-functions'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Math Operations'
documentation_page: 'cumulativesum'
documentation_source_path: 'ref/cumulativesum.html'
language: zh-CN
chinese_source: worker-translation
---

# Cumulative Sum

## 端口

### 输入

### **In** — 输入信号向量 | 矩阵

输入，指定为包含实数或复数值的向量或矩阵输入。

在您为 `Reset port` 参数选择非 `None` 值之前，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** Yes

### **Rst** — 复位端口标量

可选复位端口 **Rst** 接受标量值，这些值可以是任何内置 Simulink® 数据类型，包括 `boolean`。**Rst** 端口输入的速率必须与输入数据信号的速率相同或更慢。**Rst** 端口输入的采样时间必须是输入采样时间的正整数倍。

在您为 `Reset port` 参数选择非 `None` 值之前，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`
### 输出

### **Out** — 累积和向量 | 矩阵

输入的累积和，指定为向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### 主要

### **Sum input along** — 求和沿其进行的维度 `Channels (running sum)` (default) | `Columns` | `Rows`

指定计算累积和所沿的维度。您可以选择沿 `Channels (running sum)`、`Columns` 或 `Rows` 求和。有关更多信息，请参阅以下部分：

- Computing the Running Sum Along Channels of the Input
- Summing Along Columns
- Summing Along Rows

### **Input processing** — 处理输入的方法 `Columns as channels (frame based)` (default) | `Elements as channels (sample based)`

指定当沿输入的通道计算运行和时，模块如何处理输入。您可以将此参数设置为以下选项之一：

- `Columns as channels (frame based)`
  — 模块将输入的每一列视为单独通道。
- `Elements as channels (sample based)`
  — 模块将输入的每个元素视为单独通道。

#### 依赖关系

此参数仅在将 `Sum input along` 参数设置为 `Channels (running sum)` 时可用。

### **Reset port** — 复位类型 `None` (default) | `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

确定导致模块沿通道重置求和的复位事件。`Rst` 端口输入的速率必须与输入数据信号的速率相同或更慢。**Rst** 端口输入的采样时间必须是输入采样时间的正整数倍。有关更多信息，请参阅重置运行和。

#### 依赖关系

此参数仅在将 `Sum input along` 参数设置为 `Channels (running sum)` 时可用。

### 数据类型

**注意**

浮点继承优先于在此窗格上定义的数据类型设置。当输入为浮点时，模块会忽略这些设置。所有内部数据类型均为浮点。

### **Rounding mode** — 舍入模式 `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅舍入模式。

### **Saturate on integer overflow** — 定点运算饱和 `off` (default) | `on`

选择此参数后，模块会对其定点运算的结果进行饱和处理。清除此参数后，模块会对其定点运算的结果进行回绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **Accumulator** — 累加器的数据类型 `Inherit: Same as first input` (default) | `fixdt([],16,0)`

**Accumulator** 指定 Cumulative Sum 模块中累加运算输出的数据类型。有关如何在此模块中使用累加器数据类型的说明，请参阅定点数据类型。

- `Inherit: Same as input` — 模块将累加器数据类型指定为与输入数据类型相同。
- `fixdt([],16,0)` — 模块指定一个自动有符号、二进制点、定标、定点数据类型，其字长为 16 位，小数长度为 0。

或者，您可以使用 **数据类型助手** 设置 **Accumulator** 数据类型。单击 **显示数据类型助手** 按钮。

有关更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Output** — 输出的数据类型 `Inherit: Same as accumulator` (default) | `Inherit: Same as input` | `fixdt([],16,0)`

**Output** 指定 Cumulative Sum 模块输出的数据类型。有关输出数据类型的更多信息，请参阅定点数据类型。

- `Inherit: Same as input` — 模块将输出数据类型指定为与输入数据类型相同。
- `Inherit: Same as accumulator`
  — 模块将输出数据类型指定为与累加器数据类型相同。
- `fixdt([],16,0)` — 模块指定一个自动有符号、二进制点、定标、定点数据类型，其字长为 16 位，小数长度为 0。

或者，您可以使用 **数据类型助手** 设置 **Output** 数据类型。单击 **显示数据类型助手** 按钮。

有关数据类型助手的更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Output Minimum** — 模块可以输出的最小值 `[]` (default) | scalar

指定模块可以输出的最小值。Simulink 软件使用此最小值执行：

- 仿真范围检查。请参阅指定信号范围 (Simulink)。
- 定点数据类型的自动定标。

### **Output Maximum** — 模块可以输出的最大值 `[]` (default) | scalar

指定模块可以输出的最大值。Simulink 软件使用此最大值执行：

- 仿真范围检查。请参阅指定信号范围 (Simulink)。
- 定点数据类型的自动定标。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off` (default) | `on`

选择此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。

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

生成的代码在某些条件下依赖 `memcpy` 或
`memset` 函数（`string.h`）。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

通道、列或行元素的累积和

Cumulative Sum 模块计算输入指定维度上或跨时间的累积和（运行和）。
