---
type: simulink-block
title: 'Mean'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'mean'
documentation_source_path: 'ref/mean.html'
language: zh-CN
chinese_source: worker-translation
---

# Mean

## 端口

### 输入

### **I** — 数据输入 向量 | 矩阵 | *N* 维数组

该模块接受实值或复值多通道和多维输入。输入数据类型必须为双精度、单精度、整数或具有 2 的幂斜率且零偏置的定点。

在您选择 **Running mean** 参数并将 **Reset port** 参数设置为 `None` 以外的任何选项之前，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是

### **Rst** — 复位端口 标量

指定导致模块复位运行均值的复位事件。**Rst** 输入的采样时间必须是输入采样时间的正整数倍。

#### 依赖关系

要启用此端口，请选择 **Running mean** 参数并将 **Reset port** 参数设置为 `None` 以外的任何选项。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Port\_1** — 沿指定维度的均值 标量 | 向量 | 矩阵 | *N* 维数组

输出的数据类型与输入的数据类型一致。

当您未选择 **Running mean** 参数时，该模块计算输入每一行或每一列的均值，或沿输入指定维度的向量的均值。它还可以在每个单独的采样时间计算整个输入的均值。输出数组 `y` 中的每个元素是对应列、行或整个输入的均值。输出数组 `y` 取决于 **Find the mean value over** 参数的设置。考虑一个大小为 *M*×*N*×*P* 的三维输入信号。当您将 **Find the mean value over** 设置为：

- `Entire input` — 每个采样时间的输出是一个标量，包含 *M*×*N*×*P* 输入矩阵的均值。
- `Each row` — 每个采样时间的输出由一个 *M*×1×*P* 数组组成，其中每个元素包含输入第二维度上每个向量的均值。对于 *M*×*N* 矩阵输入，每个采样时间的输出是一个 *M*×1 列向量。
- `Each column` — 每个采样时间的输出由一个 1×*N*×*P* 数组组成，其中每个元素包含输入第一维度上每个向量的均值。对于 *M*×*N* 矩阵输入，每个采样时间的输出是一个 1×*N* 行向量。

  在此模式下，该模块将长度为 *M* 的无方向向量输入视为 *M*×1 列向量。
- `Specified dimension` — 每个采样时间的输出取决于 **Dimension** 参数的值。如果您将 **Dimension** 设置为 `1`，输出与选择 `Each column` 时相同。如果您将 **Dimension** 设置为 `2`，输出与选择 `Each row` 时相同。如果您将 **Dimension** 设置为 `3`，每个采样时间的输出是一个 *M*×*N* 矩阵，包含输入第三维度上每个向量的均值。

当您选择 **Running mean** 时，该模块在输入的时间序列中跟踪每个通道的均值。在此模式下，您还必须为 **Input processing** 参数指定一个值。

- `Elements as channels (sample based)` — 该模块将输入的每个元素视为单独的通道。对于大小为 *M*×*N*×*P* 的三维输入信号，该模块输出一个 *M*×*N*×*P* 数组。输出中的每个元素 *yijk* 包含自上次复位以来所有输入的对应元素 *uijk* 的均值。

  当复位事件发生时，当前帧中的运行均值 *yijk* 被复位为元素 *uijk*。
- `Columns as channels (frame based)` — 该模块将输入的每一列视为单独的通道。此选项不支持 N 维输入信号，其中 N > 2。对于大小为 *M*×*N* 的二维输入信号，该模块输出一个 *M*×*N* 矩阵。输出中的每个元素 *yij* 包含自上次复位以来所有输入中第 *j* 列值的均值，直至并包括当前输入的对应元素 *uij*。

  当复位事件发生时，每个通道的运行均值变为当前输入帧中所有样本（直至并包括当前输入样本）的均值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是

## 参数

### 主选项卡

### **Running mean** — 选择运行均值的选项 关闭（默认） | 打开

当您选择 **Running mean** 参数时，该模块在输入的时间序列中跟踪每个通道的均值。

### **Find the mean value over** — 模块计算均值所沿的维度 `Each column`（默认） | `Entire input` | `Each row` | `Specified dimension`

- `Each column` — 该模块输出每一列的均值。
- `Each row` — 该模块输出每一行的均值。
- `Entire input` — 该模块输出整个输入的均值。
- `Specified dimension` — 该模块输出沿 **Dimension** 参数中指定维度的均值。

#### 依赖关系

要启用此参数，请清除 **Running mean** 参数。

### **Dimension** — 自定义维度 `1`（默认） | 标量

指定计算均值所沿的输入信号维度（从 1 开始的值）。此参数的值必须大于 0 且小于输入信号的维度数。

#### 依赖关系

要启用此参数，请将 **Find the mean value over** 设置为 `Specified dimension`。

### **Input processing** — 在运行模式下处理输入的方法 `Columns as channels (frame based)`（默认） | `Elements as channels (sample based)`

- `Columns as channels (frame based)` — 该模块将输入的每一列视为单独的通道。此选项不支持 N 维输入信号，其中 N > 2。对于大小为 *M*×*N* 的二维输入信号，该模块输出一个 *M*×*N* 矩阵。输出中的每个元素 *yij* 包含自上次复位以来所有输入中第 *j* 列值的均值，直至并包括当前输入的对应元素 *uij*。

  当复位事件发生时，每个通道的运行均值变为当前输入帧中所有样本（直至并包括当前输入样本）的均值。
- `Elements as channels (sample based)` — 该模块将输入的每个元素视为单独的通道。对于大小为 *M*×*N*×*P* 的三维输入信号，该模块输出一个 *M*×*N*×*P* 数组。输出中的每个元素 *yijk* 包含自上次复位以来所有输入的对应元素 *uijk* 的均值。

  当复位事件发生时，当前帧中的运行均值 *yijk* 被复位为元素 *uijk*。

  **可变大小输入**

  当您的输入为可变大小，并且您选择了 **Running mean** 参数时，则：

  - 如果您将 **Input processing** 参数设置为 `Elements as channels (sample based)`，状态将被复位。
  - 如果您将 **Input processing** 参数设置为 `Columns as channels (frame based)`，则：

    - 当输入大小差异在于通道数（列数）时，状态将被复位。
    - 当输入大小差异在于通道长度（行数）时，不会复位，运行操作照常执行。

#### 依赖关系

要启用此参数，请选择 **Running mean** 参数。

### **Reset port** — 复位事件 `None`（默认） | `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

当在可选的 **Rst** 端口检测到复位事件时，该模块复位运行均值。复位采样时间必须是输入采样时间的正整数倍。

当 **Input processing** 参数设置为 `Elements as channels (sample based)` 时发生复位事件，每个通道的运行均值被初始化为当前输入对应通道的值。类似地，当 **Input processing** 参数设置为 `Columns as channels (frame based)` 时，每个通道的运行均值变为当前输入帧中所有样本（直至并包括当前输入样本）的均值。

使用此参数指定复位事件。

- `None` — 禁用 **Rst** 端口。
- `Rising edge` — 当 **Rst** 输入执行以下操作之一时触发复位操作：

  - 从负值上升到正值或零。
  - 从零上升到正值，且该上升不是从负值上升到零的延续。
- `Falling edge` — 当 **Rst** 输入执行以下操作之一时触发复位操作：

  - 从正值下降到负值或零。
  - 从零下降到负值，且该下降不是从正值下降到零的延续。
- `Either edge` — 当 **Rst** 输入为 `Rising edge` 或 `Falling edge` 时触发复位操作。
- `Non-zero sample` — 当 **Rst** 输入不为零时，在每个采样时间触发复位操作。

**注意**

在 Simulink 多任务模式下运行仿真时，复位信号有一个采样延迟。因此，当模块检测到复位事件时，在模块应用复位之前，复位端口速率上存在一个采样延迟。有关延迟和 Simulink 任务模式的详细信息，请参阅 Excess Algorithmic Delay (Tasking Latency) 和 Time-Based Scheduling and Code Generation (Simulink Coder)。

#### 依赖关系

要启用此参数，请选择 **Running mean** 参数。

### 数据类型选项卡

**注意**

要使用这些参数，数据输入必须为定点。对于所有其他输入，**Data Types** 选项卡上的参数将被忽略。

### **Rounding mode** — 舍入操作的方法 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅舍入模式。

### **Saturate on integer overflow** — 溢出操作的方法 关闭（默认） | 打开

当您选择此参数时，该模块对其定点运算的结果进行饱和处理。当您清除此参数时，该模块对其定点运算的结果进行回绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **Accumulator** — 累加器数据类型 `Inherit: Same as input`（默认） | `fixdt([],16,0)`

**Accumulator** 指定 Mean 模块中累加运算输出的数据类型。有关描述此模块中累加器数据类型使用的图示，请参阅定点数据类型。您可以将此参数设置为：

- `Inherit: Same as input` — 该模块将累加器数据类型指定为与输入数据类型相同。
- `fixdt([],16,0)` — 该模块指定一个自动有符号、二进制点、缩放定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Accumulator** 数据类型。要使用该助手，请单击 **Show data type assistant** 按钮。

有关数据类型助手的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output** — 输出数据类型 `Inherit: Same as accumulator`（默认） | `fixdt([],16,0)`

**Output** 指定 Mean 模块输出的数据类型。有关描述此模块中输出数据类型使用的图示，请参阅定点数据类型。您可以将其设置为：

- `Inherit: Same as accumulator` — 该模块将输出数据类型指定为与累加器数据类型相同。
- `fixdt([],16,0)` — 该模块指定一个自动有符号、二进制点、缩放定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Output** 数据类型。要使用该助手，请单击 **Show data type assistant** 按钮。

有关数据类型助手的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output Minimum** — 模块可以输出的最小值 `[]`（默认） | 标量

指定模块可以输出的最小值。默认值为 `[]`（未指定）。Simulink 使用此值执行：

- 仿真范围检查。请参阅 Specify Signal Ranges (Simulink)。
- 定点数据类型的自动缩放。

### **Output Maximum** — 模块可以输出的最大值 `[]`（默认） | 标量

指定模块可以输出的最大值。默认值为 `[]`（未指定）。Simulink 使用此值执行：

- 仿真范围检查。请参阅 Specify Signal Ranges (Simulink)。
- 定点数据类型的自动缩放。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 关闭（默认） | 打开

选择此参数以防止定点工具覆盖您在模块上指定的数据类型。

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

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

查找输入或输入序列的均值

Mean 模块计算输入每一行或每一列的均值，或沿输入指定维度的向量的均值。它还可以计算整个输入的均值。您可以使用 **Find the mean value over** 参数指定维度。Mean 模块还可以在一段时间内跟踪输入序列中的均值。要跟踪输入序列中的均值，请选择 **Running mean** 参数。

**注意**

Mean 模块中的 **Running** 模式将在未来版本中移除。要在 Simulink® 中计算运行均值，请改用 Moving Average 模块。
