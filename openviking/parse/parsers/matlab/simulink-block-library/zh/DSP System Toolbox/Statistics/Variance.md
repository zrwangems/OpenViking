---
type: simulink-block
title: 'Variance'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'variance'
documentation_source_path: 'ref/variance.html'
language: zh-CN
chinese_source: worker-translation
---

# Variance

## 端口

### 输入

### **In** — 数据输入向量 | 矩阵 | *N* 维数组

该模块接受实值或复值多通道和多维输入。

在您选择 **Running variance** 参数并将 **Reset port** 参数设置为除 `None` 之外的任何选项之前，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是

### **Rst** — 复位端口标量

指定导致模块重置运行方差的事件。
**Rst** 输入的采样时间必须是输入采样时间的正整数倍。

#### 依赖关系

要启用此端口，请选择 **Running variance** 参数，并将 **Reset port** 参数设置为除 `None` 之外的任何选项。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### 输出

### **Port\_1** — 沿指定维度的方差 标量 | 向量 | 矩阵 | *N* 维数组

当您未选择 **Running variance** 参数时，模块计算输入的每一行或每一列的方差，或沿输入的指定维度的向量计算方差。它还可以在每个单独采样时间计算整个输入的方差。输出数组 `y` 中的每个元素是对应列、行或整个输入的方差。输出数组 `y` 取决于 **Find the variance value over** 参数的设置。

考虑大小为 *M*×*N*×*P* 的三维输入信号。当您将 **Find the variance value over** 设置为：

- `Entire input` — 每个采样时间的输出是一个标量，其中包含 *M*×*N*×*P* 输入矩阵的方差。
- `Each row` — 每个采样时间的输出由 *M*×1×*P* 数组组成，其中每个元素包含输入第二维度上每个向量的方差。对于 *M*×*N* 矩阵输入，每个采样时间的输出是 *M*×1 列向量。
- `Each column` — 每个采样时间的输出由 1×*N*×*P* 数组组成，其中每个元素包含输入第一维度上每个向量的方差。对于 *M*×*N* 矩阵输入，每个采样时间的输出是 1×*N* 行向量。

  在此模式下，模块将长度为 *M* 的无向向量输入视为 *M*×1 列向量。
- `Specified dimension` — 每个采样时间的输出取决于 **Dimension** 参数的值。如果将 **Dimension** 设置为 `1`，则输出与选择 `Each column` 时相同。如果将 **Dimension** 设置为 `2`，则输出与选择 `Each row` 时相同。如果将 **Dimension** 设置为 `3`，则每个采样时间的输出是一个 *M*×*N* 矩阵，其中包含输入第三维度上每个向量的方差。

当您选择 **Running variance** 时，模块在输入时间序列中跟踪每个通道的方差。在此模式下，您还必须为 **Input processing** 参数指定值。当您将 **Input processing** 设置为：

- `Elements as channels (sample based)` — 模块将输入的每个元素视为单独通道。对于大小为 *M*×*N*×*P* 的三维输入信号，模块输出一个 *M*×*N*×*P* 数组。输出中的每个元素 *yijk* 包含自上次重置以来所有输入的对应元素 *uijk* 的方差。

  当发生重置事件时，当前帧中的运行方差 *yijk* 被重置为元素 *uijk*。
- `Columns as channels (frame based)` — 模块将输入的每一列视为单独通道。此选项不支持超过二维的输入信号。对于大小为 *M*×*N* 的二维输入信号，模块输出一个 *M*×*N* 矩阵。输出中的每个元素 *yij* 包含自上次重置以来所有输入第 *j* 列中元素的方差，直至且包括当前输入的对应元素 *uij*。

  当发生重置事件时，每个通道的运行方差变为当前输入帧中所有样本（直至且包括当前输入样本）的方差。

输出的数据类型与输入的数据类型匹配。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### 主选项卡

### **Running variance** — 用于选择运行方差的选项 off（默认）| on

当您选择 **Running variance** 参数时，模块在输入时间序列中跟踪每个通道的方差值。

### **Find the variance value over** — 计算方差所沿的维度 `Each column`（默认）| `Entire input` | `Each row` | `Specified dimension`

- `Each column` — 模块输出每一列的方差。
- `Each row` — 模块输出每一行的方差。
- `Entire input` — 模块输出整个输入的方差。
- `Specified dimension` — 模块输出 **Dimension** 参数中指定维度的方差。

#### 依赖关系

要启用此参数，请清除 **Running variance** 参数。

### **Dimension** — 自定义维度 `1`（默认）| 标量

指定计算方差所沿的输入信号维度（基于一的值）。此参数的值必须大于 0 且小于或等于输入信号的维数。

#### 依赖关系

要启用此参数，请将 **Find the variance value over** 设置为 `Specified dimension`。

### **Input processing** — 在运行模式下处理输入的方法 `Columns as channels (frame based)`（默认）| `Elements as channels (sample based)`

- `Columns as channels (frame based)` — 模块将输入的每一列视为单独通道。此选项不支持超过二维的输入信号。对于大小为 *M*×*N* 的二维输入信号，模块输出一个 *M*×*N* 矩阵。输出中的每个元素 *yij* 包含自上次重置以来所有输入第 *j* 列中元素的方差，直至且包括当前输入的对应元素 *uij*。

  当发生重置事件时，每个通道的运行方差变为当前输入帧中所有样本（直至且包括当前输入样本）的方差。
- `Elements as channels (sample based)` — 模块将输入的每个元素视为单独通道。对于大小为 *M*×*N*×*P* 的三维输入信号，模块输出一个 *M*×*N*×*P* 数组。输出中的每个元素 *yijk* 包含自上次重置以来所有输入的对应元素 *uijk* 的方差。

  当发生重置事件时，当前帧中的运行方差 *yijk* 被重置为元素 *uijk*。

  **可变大小输入**

  当您的输入为可变大小，并且您选择 **Running variance** 参数时，则：

  - 如果将 **Input processing** 参数设置为 `Elements as channels (sample based)`，则状态会被重置。
  - 如果将 **Input processing** 参数设置为 `Columns as channels (frame based)`，则：

    - 当输入大小差异在于通道数（列数）时，状态会被重置。
    - 当输入大小差异在于通道长度（行数）时，状态不会重置，并且按通常方式执行运行操作。

#### 依赖关系

要启用此参数，请选择 **Running variance** 参数。

### **Reset port** — 重置事件 `None`（默认）| `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

当在可选 **Rst** 端口检测到重置事件时，模块会重置运行方差。重置采样时间必须是输入采样时间的正整数倍。

当 **Input processing** 参数设置为 `Elements as channels (sample based)` 时发生重置事件，每个通道的运行方差会初始化为当前输入对应通道中的值。类似地，当 **Input processing** 参数设置为 `Columns as channels (frame based)` 时，每个通道的运行方差变为当前输入帧中所有样本（直至且包括当前输入样本）的方差。

使用此参数指定重置事件。

- `None` — 禁用 **Rst** 端口。
- `Rising edge` — 当 **Rst** 输入执行以下操作之一时触发重置操作：

  - 从负值上升为正值或零。
  - 从零上升为正值，其中该上升不是从负值上升为零的延续。
- `Falling edge` — 当 **Rst** 输入执行以下操作之一时触发重置操作：

  - 从正值下降为负值或零。
  - 从零下降为负值，其中该下降不是从正值下降为零的延续。
- `Either edge` — 当 **Rst** 输入是 `Rising edge` 或 `Falling edge` 时触发重置操作。
- `Non-zero sample` — 当 **Rst** 输入不为零时，在每个采样时间触发重置操作。

**注意**

在 Simulink 多任务模式下运行仿真时，重置信号有一个采样周期的延迟。因此，当模块检测到重置事件时，在模块应用重置之前，在重置端口速率下会有一个采样周期的延迟。有关延迟和 Simulink 任务模式的详细信息，请参阅 Excess Algorithmic Delay (Tasking Latency) 和 Time-Based Scheduling and Code Generation (Simulink Coder)。

#### 依赖关系

要启用此参数，请选择 **Running variance** 参数。

### 数据类型选项卡

**注意**

要使用这些参数，数据输入必须是定点。对于所有其他输入，**Data Types** 选项卡上的参数将被忽略。

### **Rounding mode** — 舍入操作的方法 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关更多详细信息，请参阅 rounding mode。

### **Saturate on integer overflow** — 溢出操作的方法 off（默认）| on

当您选择此参数时，模块会对其定点运算的结果执行饱和。当您清除此参数时，模块会对其定点运算的结果执行回绕。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **Input-squared product output** — 输入平方项的数据类型 `Same as input`（默认）| `Binary point scaling`

输入元素的平方存储在 **Input-squared product output** 数据类型中。如果输入为复数，则输入的实部和虚部的平方存储在此数据类型中。有关更多详细信息，请参阅 Fixed-Point Data Types。

您可以将此参数设置为：

- `Inherit: Same as input` — 数据类型与输入数据类型相同。
- `Binary point scaling` — **Input-squared product output** 数据类型使用二进制小数点缩放。如果选择此选项，模块会显示用于指定 **Word length** 和 **Fraction length** 的字段。**Signedness** 从输入继承。

### **Input-sum-squared product** — 输入和平方项的数据类型 `Same as input-squared product`（默认）| `Binary point scaling`

输入元素之和的平方存储在 **Input-sum-squared product** 数据类型中。如果输入为复数，则实部之和的平方以及虚部之和的平方存储在此数据类型中。有关更多详细信息，请参阅 Fixed-Point Data Types。

您可以将此参数设置为：

- `Same as input-squared product` — 数据类型与输入平方乘积数据类型相同。
- `Binary point scaling` — **Input-sum-squared product** 数据类型使用二进制小数点缩放。如果选择此选项，模块会显示用于指定 **Word length** 和 **Fraction length** 的字段。**Signedness** 从输入继承。

### **Accumulator** — 累加器数据类型 `Same as input-squared product`（默认）| `Same as input` | `Binary point scaling`

**Accumulator** 指定 Variance 模块中累加运算输出的数据类型。有关描述此模块中累加器数据类型用法的图示，请参阅 Fixed-Point Data Types。

您可以将此参数设置为：

- `Same as input-squared product` — 累加器数据类型与输入平方乘积数据类型相同。
- `Same as input` — 累加器数据类型与输入数据类型相同。
- `Binary point scaling` — **Accumulator** 数据类型使用二进制小数点缩放。如果选择此选项，模块会显示用于指定 **Word length** 和 **Fraction length** 的字段。**Signedness** 从输入继承。

### **Output** — 输出数据类型 `Same as input-squared product`（默认）| `Same as accumulator` | `Same as input` | `Binary point scaling`

**Output** 指定 Variance 模块输出的数据类型。有关此模块中输出数据类型用法的信息，请参阅 Fixed-Point Data Types。您可以将其设置为：

- `Same as input-squared product` — 输出数据类型与输入平方乘积数据类型相同。
- `Same as accumulator` — 输出数据类型与累加器数据类型相同。
- `Same as input` — 输出数据类型与输入数据类型相同。
- `Binary point scaling` — **Output** 数据类型使用二进制小数点缩放。如果选择此选项，模块会显示用于指定 **Word length** 和 **Fraction length** 的字段。**Signedness** 从输入继承。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 off（默认）| on

选择此参数可防止定点工具覆盖您在模块上指定的数据类型。

## 所属库

DSP System Toolbox / Statistics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

输入或输入序列的方差

Variance 模块计算输入的每一行或每一列的无偏方差，或沿输入的指定维度的向量计算无偏方差。它还可以计算整个输入的方差。您可以使用 **Find the variance value over** 参数指定维度。Variance 模块还可以在一段时间内跟踪输入序列中的方差。要跟踪输入序列中的方差，请选择 **Running variance** 参数。

**注意**

Variance 模块中的 **Running** 模式将在未来版本中移除。要在 Simulink® 中计算运行方差，请改用 Moving Variance 模块。
