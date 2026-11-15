---
type: simulink-block
title: 'Histogram'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Measurements and Statistics / Measurements'
documentation_page: 'histogram'
documentation_source_path: 'ref/histogram.html'
language: zh-CN
chinese_source: worker-translation
---

# Histogram

## 端口

### 输入

### **In** — 数据输入 向量 | 矩阵 | *N* 维数组

该模块接受实值或复值的多通道和多维输入。输入数据类型必须为 double precision、single precision、integer 或 fixed point，斜率为 2 的幂且偏置为零。

在选择 **Running histogram** 参数并将 **Reset port** 参数设置为除 `None` 之外的任何选项之前，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`
**复数支持：** 是

### **Rst** — 重置端口 标量

指定使模块重置运行直方图的重置事件。重置信号和输入数据信号必须具有相同的速率。

#### 依赖项

要启用此端口，请选择 **Running histogram** 参数，并将 **Reset port** 参数设置为除 `None` 之外的任何选项。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### 输出

### **Port\_1** — 直方图输出 向量 | 矩阵 | *N* 维数组

将直方图数据输出为向量、矩阵或数组。输出主要取决于 **Running histogram** 和 **Find the histogram over** 参数的设置。

例如，考虑大小为 *M*×*N* 的二维输入信号。

当您清除 **Running histogram** 参数时，该模块计算输入每一列中或沿整个输入的频率分布。当您将 **Find the histogram over** 设置为：

- `Each column` — 该模块计算输入每一列的直方图。输出是一个 *n*×*N* 矩阵，其中 *n* 是 **Number of bins**。输出矩阵的第 *j* 列包含 *M*×*N* 输入矩阵第 *j* 列中数据的直方图。
- `Entire input` — 该模块计算整个输入向量、矩阵或 *N* 维数组的直方图。输出是一个 *n*×1 向量，其中 *n* 是 **Number of bins**。

当您选择 **Running histogram** 参数时，该模块计算所有输入在一段时间内的频率分布。在这种情况下，当您将 **Find the histogram over** 设置为：

- `Each column` — 该模块计算输入每一列的运行直方图。输出是一个 *n*×*N* 矩阵，其中 *n* 是 **Number of bins**。输出矩阵的第 *j* 列包含 *M*×*N* 矩阵输入第 *j* 列中数据的运行直方图。
- `Entire input` — 该模块计算整个输入向量、矩阵或 *N* 维数组的运行直方图。输出是一个 *n*×1 向量，其中 *n* 是 **Number of bins**。

当输入的数据类型不是 `single` 或 `double` 时，输出数据类型为 `uint32`。`uint32` 可表示的最大数为 `232-1`。如果任何输入的范围超过此值，该模块会将值回绕为 `0`。

**数据类型：** `single` | `double` | `uint32`

## 参数

### 主选项卡

### **Lower limit of histogram** — 最低值 bin 的下边界 标量

将最低值 bin 的下边界指定为实数标量。此参数不接受 `NaN` 或 `Inf`。如果输入的值小于 **Lower limit of histogram**，该模块会将此元素放入最低值 bin 中。

### **Upper limit of histogram** — 最高值 bin 的上边界 标量

将最高值 bin 的上边界指定为实数标量。此参数不接受 `NaN` 或 `Inf`。如果输入的值大于 **Upper limit of histogram**，该模块会将此元素放入最高值 bin 中。

### **Number of bins** — 直方图 bin 数 正整数

将直方图 bin 数指定为正整数。

### **Find the histogram over** — 计算每一列或整个输入的直方图 `Each column` (默认) | `Entire input`

指定直方图是针对每一列还是整个输入进行计算。此参数的选项受 **Running histogram** 参数设置的影响。

当您清除 **Running histogram** 参数，并将 **Find the histogram over** 参数设置为：

- `Each column` — 该模块计算每一列的直方图。
- `Entire input` — 该模块输出整个输入的直方图。

当您选择 **Running histogram** 参数，并将 **Find the histogram over** 参数设置为：

- `Each column` — 该模块计算每一列的运行直方图。
- `Entire input` — 该模块输出整个输入的运行直方图。

### **Normalized** — 归一化输出 off (默认) | on

当您选择此参数时，模块输出 *y* 会归一化。在数学上，`sum(y) = 1`。此参数不适用于定点输入信号。

### **Running histogram** — 随时间跟踪频率分布 off (默认) | on

当您选择此参数时，该模块会在一段时间内跟踪输入的频率分布。

### **Reset port** — 重置事件 `Non-zero sample` (默认) | `None` | `Rising edge` | `Falling edge` | `Either edge`

每当在可选的 **Rst** 端口检测到重置事件时，该模块会重置运行直方图并清空所有 bin。重置采样时间必须等于输入采样时间。

使用此参数指定重置事件：

- `Non-zero sample` — 当 **Rst** 输入不为零时，在每个采样时间触发重置操作。
- `None` — 禁用 **Rst** 端口。
- `Rising edge` — 当 **Rst** 输入执行以下操作之一时触发重置操作：

  - 从负值上升到正值或零。
  - 从零上升到正值，其中该上升不是从负值上升到零的延续。
- `Falling edge` — 当 **Rst** 输入执行以下操作之一时触发重置操作：

  - 从正值下降到负值或零。
  - 从零下降到负值，其中该下降不是从正值下降到零的延续。
- `Either edge` — 当 **Rst** 输入为 `Rising edge` 或 `Falling edge` 时触发重置操作。

**注意**

在 Simulink 多任务模式下运行仿真时，重置信号具有一个采样延迟。当该模块检测到重置事件时，在模块应用重置之前，会在重置端口速率下有一个采样的延迟。有关延迟和 Simulink 任务模式的详细信息，请参阅 Excess Algorithmic Delay (Tasking Latency) 和 Time-Based Scheduling and Code Generation (Simulink Coder)。

#### 依赖项

要启用此参数，请选择 **Running histogram** 参数。

### 数据类型选项卡

**注意**

要使用这些参数，数据输入必须为复数且为定点。对于所有其他输入，**Data Types** 选项卡上的参数将被忽略。

### **Rounding mode** — 舍入操作的方法 `Floor` (默认) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关更多详细信息，请参阅 rounding mode。

### **Saturate on integer overflow** — 溢出操作的方法 off (默认) | on

当您选择此参数时，该模块会对其定点运算结果进行饱和。当您清除此参数时，该模块会对其定点运算结果进行回绕。有关 `saturate` 和 `wrap` 的详细信息，请参阅 overflow mode for fixed-point operations。

### **Product output** — 乘积输出数据类型 `Inherit: Same as input` (默认) | `fixdt([],16,0)`

复数输入的实部和虚部的平方存储在 **Product output** 数据类型中。

您可以将此参数设置为：

- `Inherit: Same as input` — 乘积输出数据类型与输入数据类型相同。
- `fixdt([],16,0)` — 乘积输出数据类型是自动有符号、二进制点、定标的 fixed-point 数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **数据类型助手** 设置 **Product output** 数据类型。要使用该助手，请点击 **显示数据类型助手** 按钮。

有关数据类型助手的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Accumulator** — 累加器数据类型 `Inherit: Same as input` (默认) | `Inherit: Same as product output` | `fixdt([],16,0)`

复数输入的实部和虚部的平方和的结果存储在 **Accumulator** 数据类型中。

您可以将此参数设置为：

- `Inherit: Same as input` — 累加器数据类型与输入数据类型相同。
- `Inherit: Same as product output` — 累加器数据类型与乘积输出数据类型相同。
- `fixdt([],16,0)` — 累加器数据类型是自动有符号、二进制点、定标的 fixed-point 数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **数据类型助手** 设置 **Accumulator** 数据类型。要使用该助手，请点击 **显示数据类型助手** 按钮。

有关数据类型助手的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 off (默认) | on

选择此参数以防止定点工具覆盖您在模块上指定的数据类型。

## 所属库

DSP System Toolbox / Statistics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `bus` | `double` | `fixed point` | `integer` | `single` |
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

输入或输入序列的直方图

Histogram 模块计算输入元素沿每一列或沿整个输入的频率分布。您可以使用 **Find the histogram over** 参数指定维度。该模块根据输入元素的值将其分配到由 **Number of bins** 参数指定数量的离散 bin 中。有关更多详细信息，请参阅 Algorithms。

当输入数据为实数时，bin 边界会转换为 double 数据类型。当输入数据为复数时，double-precision 输入的 bin 边界会转换为 double，integer 输入的 bin 边界会转换为 double 并求平方。有关示例，请参阅 Compute the Histogram of Real and Complex Data。

要在一段时间内跟踪输入的频率分布，请选择 **Running histogram** 参数。

当输入为复数时，该模块按幅值对元素排序。
