---
type: simulink-block
title: 'Standard Deviation'
family: 'statistics'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'standarddeviation'
documentation_source_path: 'ref/standarddeviation.html'
language: zh-CN
chinese_source: worker-translation
---

# Standard Deviation

## 端口

### 输入

### **In** — 数据输入 向量 | 矩阵 | *N*-D 数组

该模块接受实值或复值多通道和多维输入。

在选择 **Running standard deviation** 参数并将 **Reset port** 参数设置为 `None` 以外的任何选项之前，该端口未命名。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **Rst** — 重置端口 标量

指定使模块重置运行标准差的重置事件。**Rst** 输入的采样时间必须是输入采样时间的正整数倍。

#### 依赖关系

要启用此端口，请选择 **Running standard deviation** 参数并将 **Reset port** 参数设置为 `None` 以外的任何选项。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### 输出

### **Port\_1** — 沿指定维度的标准差 标量 | 向量 | 矩阵 | *N*-D 数组

输出数据类型与输入数据类型匹配。

当未选择 **Running standard deviation** 参数时，模块计算输入每一行或每一列的标准差，或沿输入指定维度的向量计算。它还可以在每个独立采样时间计算整个输入的标准差。输出数组 `y` 中的每个元素是对应列、行或整个输入的标准差。输出数组 `y` 取决于 **Find the standard deviation value over** 参数的设置。考虑一个大小为 *M*-by-*N*-by-*P* 的三维输入信号。当将 **Find the standard deviation value over** 设置为：

- `Entire input` — 每个采样时间处的输出是一个标量，包含 *M*-by-*N*-by-*P* 输入矩阵的标准差。
- `Each row` — 每个采样时间处的输出由 *M*-by-1-by-*P* 数组组成，其中每个元素包含输入第二维上每个向量的标准差。对于 *M*-by-*N* 矩阵输入，每个采样时间处的输出是 *M*-by-1 列向量。
- `Each column` — 每个采样时间处的输出由 1-by-*N*-by-*P* 数组组成，其中每个元素包含输入第一维上每个向量的标准差。对于 *M*-by-*N* 矩阵输入，每个采样时间处的输出是 1-by-*N* 行向量。

  在此模式下，模块将长度为 *M* 的未定向向量输入视为 *M*-by-1 列向量。
- `Specified dimension` — 每个采样时间处的输出取决于 **Dimension** 参数的值。如果将 **Dimension** 设置为 `1`，则输出与选择 `Each column` 时相同。如果将 **Dimension** 设置为 `2`，则输出与选择 `Each row` 时相同。如果将 **Dimension** 设置为 `3`，则每个采样时间处的输出是一个 *M*-by-*N* 矩阵，包含输入第三维上每个向量的标准差。

当选择 **Running standard deviation** 时，模块跟踪输入时间序列中每个通道的标准差。在此模式下，还必须为 **Input processing** 参数指定一个值。

- `Elements as channels (sample based)` — 模块将输入的每个元素视为单独通道。对于大小为 *M*-by-*N*-by-*P* 的三维输入信号，模块输出 *M*-by-*N*-by-*P* 数组。输出中的每个元素 *yijk* 包含自上次重置以来所有输入的对应元素 *uijk* 的标准差。

  当重置事件发生时，当前帧中的运行标准差 *yijk* 重置为元素 *uijk*。
- `Columns as channels (frame based)` — 模块将输入的每一列视为单独通道。此选项不支持超过二维的输入信号。对于大小为 *M*-by-*N* 的二维输入信号，模块输出 *M*-by-*N* 矩阵。输出中的每个元素 *yij* 包含自上次重置以来所有输入中第 *j* 列元素的标准差，直到并包括当前输入的对应元素 *uij*。

  当重置事件发生时，每个通道的运行标准差变为当前输入帧中所有样本的标准差，直到并包括当前输入样本。

**数据类型：** `single` | `double`

## 参数

### 主选项卡

### **Running standard deviation** — 用于选择运行标准差的选项 off (default) | on

当选择 **Running standard deviation** 参数时，模块跟踪输入时间序列中每个通道的标准差值。

### **Find the standard deviation value over** — 模块计算标准差所依据的维度 `Each column` (default) | `Entire input` | `Each row` | `Specified dimension`

- `Each column` — 模块输出每一列上的标准差。
- `Each row` — 模块输出每一行上的标准差。
- `Entire input` — 模块输出整个输入上的标准差。
- `Specified dimension` — 模块输出 **Dimension** 参数中指定维度上的标准差。

#### 依赖关系

要启用此参数，请清除 **Running standard deviation** 参数。

### **Dimension** — 自定义维度 `1` (default) | 标量

指定计算标准差所依据的输入信号维度（从 1 开始的值）。此参数的值必须大于 0 且小于输入信号中的维度数。

#### 依赖关系

要启用此参数，请将 **Find the standard deviation value over** 设置为 `Specified dimension`。

### **Input processing** — 在运行模式下处理输入的方法 `Columns as channels (frame based)` (default) | `Elements as channels (sample based)`

- `Columns as channels (frame based)` — 模块将输入的每一列视为单独通道。此选项不支持超过二维的输入信号。对于大小为 *M*-by-*N* 的二维输入信号，模块输出 *M*-by-*N* 矩阵。输出中的每个元素 *yij* 包含自上次重置以来所有输入中第 *j* 列元素的标准差，直到并包括当前输入的对应元素 *uij*。

  当重置事件发生时，每个通道的运行标准差变为当前输入帧中所有样本的标准差，直到并包括当前输入样本。
- `Elements as channels (sample based)` — 模块将输入的每个元素视为单独通道。对于大小为 *M*-by-*N*-by-*P* 的三维输入信号，模块输出 *M*-by-*N*-by-*P* 数组。输出中的每个元素 *yijk* 包含自上次重置以来所有输入的对应元素 *uijk* 的标准差。

  当重置事件发生时，当前帧中的运行标准差 *yijk* 重置为元素 *uijk*。

  **可变大小输入**

  当输入为可变大小时，并且选择 **Running standard deviation** 参数，则：

  - 如果将 **Input processing** 参数设置为 `Elements as channels (sample based)`，则状态会重置。
  - 如果将 **Input processing** 参数设置为 `Columns as channels (frame based)`，则：

    - 当输入大小差异在于通道数（列数）时，状态会重置。
    - 当输入大小差异在于通道长度（行数）时，不会发生重置，并且照常执行运行操作。

#### 依赖关系

要启用此参数，请选择 **Running standard deviation** 参数。

### **Reset port** — 重置事件 `None` (default) | `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

当在可选 **Rst** 端口检测到重置事件时，模块会重置运行标准差。重置采样时间必须是输入采样时间的正整数倍。

当 **Input processing** 参数设置为 `Elements as channels (sample based)` 时发生重置事件，每个通道的运行标准差会初始化为当前输入对应通道中的值。类似地，当 **Input processing** 参数设置为 `Columns as channels (frame based)` 时，每个通道的运行标准差变为当前输入帧中所有样本的标准差，直到并包括当前输入样本。

使用此参数指定重置事件。

- `None` — 禁用 **Rst** 端口。
- `Rising edge` — 当 **Rst** 输入执行以下操作之一时触发重置操作：

  - 从负值上升到正值或零。
  - 从零上升到正值，其中该上升不是从负值上升到零的延续。
- `Falling edge` — 当 **Rst** 输入执行以下操作之一时触发重置操作：

  - 从正值下降到负值或零。
  - 从零下降到负值，其中该下降不是从正值下降到零的延续。
- `Either edge` — 当 **Rst** 输入为 `Rising edge` 或 `Falling edge` 时触发重置操作。
- `Non-zero sample` — 当 **Rst** 输入不为零时，在每个采样时间触发重置操作。

**注意**

在 Simulink 多任务模式下运行仿真时，重置信号具有一个采样的延迟。因此，当模块检测到重置事件时，在模块应用重置之前，会在重置端口速率下存在一个采样延迟。有关延迟和 Simulink 任务模式的详细信息，请参阅 Excess Algorithmic Delay (Tasking Latency) 和 Time-Based Scheduling and Code Generation (Simulink Coder)。

#### 依赖关系

要启用此参数，请选择 **Running standard deviation** 参数。

## 所属库

DSP System Toolbox / Statistics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

输入或输入序列的标准差

Standard Deviation 模块计算输入每一行或每一列的标准差，或沿输入指定维度的向量计算。它还可以计算整个输入的标准差。您可以使用 **Find the standard deviation value over** 参数指定维度。Standard Deviation 模块还可以跟踪一段时间内输入序列的标准差。要跟踪输入序列的标准差，请选择 **Running standard deviation** 参数。

**注意**

Standard Deviation 模块中的 **Running** 模式将在未来版本中移除。要在 Simulink® 中计算运行标准差，请改用 Moving Standard Deviation 模块。
