---
type: simulink-block
title: 'RMS'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'rms'
documentation_source_path: 'ref/rms.html'
language: zh-CN
chinese_source: worker-translation
---

# RMS

## 端口

### 输入

### **In** — 数据输入 向量 | 矩阵 | *N* 维数组

该模块接受实值或复值多通道和多维输入。

在选择 **Running RMS** 参数并将 **Reset port** 参数设置为除 `None` 以外的任何选项之前，此端口未命名。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Rst** — 复位端口 标量

指定使模块复位 running RMS 的复位事件。**Rst** 输入的采样时间必须是输入采样时间的正整数倍。

#### 依赖关系

要启用此端口，请选择 **Running RMS** 参数，并将 **Reset port** 参数设置为除 `None` 以外的任何选项。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### 输出

### **Port\_1** — 沿指定维度的 RMS 值 标量 | 向量 | 矩阵 | *N* 维数组

输出的数据类型与输入的数据类型匹配。

当未选择 **Running RMS** 参数时，模块计算输入每一行或每一列的 RMS 值，或沿输入指定维度的向量计算 RMS 值。它还可以在每个单独采样时间计算整个输入的 RMS 值。输出数组 `y` 中的每个元素是对应列、行或整个输入的 RMS 值。输出数组 `y` 取决于 **Find the RMS value over** 参数的设置。考虑一个大小为 *M*×*N*×*P* 的三维输入信号。当将 **Find the RMS value over** 设置为：

- `Entire input` — 每个采样时间的输出是一个标量，其中包含 *M*×*N*×*P* 输入矩阵的 RMS 值。
- `Each row` — 每个采样时间的输出由 *M*×1×*P* 数组组成，其中每个元素包含沿输入第二维的每个向量的 RMS 值。对于 *M*×*N* 矩阵输入，每个采样时间的输出是 *M*×1 列向量。
- `Each column` — 每个采样时间的输出由 1×*N*×*P* 数组组成，其中每个元素包含沿输入第一维的每个向量的 RMS 值。对于 *M*×*N* 矩阵输入，每个采样时间的输出是 1×*N* 行向量。

  在此模式下，模块将长度为 *M* 的无向向量输入视为 *M*×1 列向量。
- `Specified dimension` — 每个采样时间的输出取决于 **Dimension** 参数的值。如果将 **Dimension** 设置为 `1`，输出与选择 `Each column` 时相同。如果将 **Dimension** 设置为 `2`，输出与选择 `Each row` 时相同。如果将 **Dimension** 设置为 `3`，每个采样时间的输出是 *M*×*N* 矩阵，其中包含沿输入第三维的每个向量的 RMS 值。

当选择 **Running RMS** 时，模块跟踪时间序列输入中每个通道的 RMS 值。在此模式下，还必须为 **Input processing** 参数指定值。

- `Elements as channels (sample based)` — 模块将输入的每个元素视为单独通道。对于大小为 *M*×*N*×*P* 的三维输入信号，模块输出 *M*×*N*×*P* 数组。输出的每个元素 *yijk* 包含自上次复位以来所有输入的对应元素 *uijk* 的 RMS 值。

  当复位事件发生时，当前帧中的 running RMS *yijk* 被复位为元素 *uijk*。
- `Columns as channels (frame based)` — 模块将输入的每一列视为单独通道。此选项不支持超过二维的输入信号。对于大小为 *M*×*N* 的二维输入信号，模块输出 *M*×*N* 矩阵。输出的每个元素 *yij* 包含自上次复位以来所有输入中第 *j* 列元素的 RMS 值，直到并包括当前输入的对应元素 *uij*。

  当复位事件发生时，每个通道的 running RMS 变为当前输入帧中所有样本的 RMS 值，直到并包括当前输入样本。

**数据类型：** `single` | `double`

## 参数

### 主选项卡

### **Running RMS** — 选择 running RMS 的选项 off (默认) | on

当选择 **Running RMS** 参数时，模块跟踪时间序列输入中每个通道的 RMS 值。

### **Find the RMS value over** — 模块计算 RMS 值所沿的维度 `Each column` (默认) | `Entire input` | `Each row` | `Specified dimension`

- `Each column` — 模块输出每一列的 RMS 值。
- `Each row` — 模块输出每一行的 RMS 值。
- `Entire input` — 模块输出整个输入的 RMS 值。
- `Specified dimension` — 模块输出 **Dimension** 参数中指定维度的 RMS 值。

#### 依赖关系

要启用此参数，请清除 **Running RMS** 参数。

### **Dimension** — 自定义维度 `1` (默认) | 标量

指定计算 RMS 值所沿的输入信号维度（基于一的值）。此参数的值必须大于 0 且小于输入信号中的维度数。

#### 依赖关系

要启用此参数，请将 **Find the RMS value over** 设置为 `Specified dimension`。

### **Input processing** — 在 running 模式下处理输入的方法 `Columns as channels (frame based)` (默认) | `Elements as channels (sample based)`

- `Columns as channels (frame based)` — 模块将输入的每一列视为单独通道。此选项不支持超过二维的输入信号。对于大小为 *M*×*N* 的二维输入信号，模块输出 *M*×*N* 矩阵。输出的每个元素 *yij* 包含自上次复位以来所有输入中第 *j* 列元素的 RMS 值，直到并包括当前输入的对应元素 *uij*。

  当复位事件发生时，每个通道的 running RMS 变为当前输入帧中所有样本的 RMS 值，直到并包括当前输入样本。
- `Elements as channels (sample based)` — 模块将输入的每个元素视为单独通道。对于大小为 *M*×*N*×*P* 的三维输入信号，模块输出 *M*×*N*×*P* 数组。输出的每个元素 *yijk* 包含自上次复位以来所有输入的对应元素 *uijk* 的 RMS 值。

  当复位事件发生时，当前帧中的 running RMS *yijk* 被复位为元素 *uijk*。

  **可变大小输入**

  当输入为可变大小，并且选择 **Running RMS** 参数时：

  - 如果将 **Input processing** 参数设置为 `Elements as channels (sample based)`，状态会复位。
  - 如果将 **Input processing** 参数设置为 `Columns as channels (frame based)`，则：

    - 当输入大小差异在通道数（列数）上时，状态会复位。
    - 当输入大小差异在通道长度（行数）上时，不会复位，并且照常执行 running 运算。

#### 依赖关系

要启用此参数，请选择 **Running RMS** 参数。

### **Reset port** — 复位事件 `None` (默认) | `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

当在可选的 **Rst** 端口检测到复位事件时，模块会复位 running RMS。复位采样时间必须是输入采样时间的正整数倍。

当 **Input processing** 参数设置为 `Elements as channels (sample based)` 时发生复位事件，每个通道的 running RMS 会初始化为当前输入对应通道中的值。类似地，当 **Input processing** 参数设置为 `Columns as channels (frame based)` 时，每个通道的 running RMS 变为当前输入帧中所有样本的 RMS 值，直到并包括当前输入样本。

使用此参数指定复位事件。

- `None` — 禁用 **Rst** 端口。
- `Rising edge` — 当 **Rst** 输入执行以下操作之一时触发复位操作：

  - 从负值上升到正值或零。
  - 从零上升到正值，其中该上升不是从负值上升到零的延续。
- `Falling edge` — 当 **Rst** 输入执行以下操作之一时触发复位操作：

  - 从正值下降到负值或零。
  - 从零下降到负值，其中该下降不是从正值下降到零的延续。
- `Either edge` — 当 **Rst** 输入为 `Rising edge` 或 `Falling edge` 时触发复位操作。
- `Non-zero sample` — 当 **Rst** 输入不为零时，在每个采样时间触发复位操作。

**注意**

在 Simulink 多任务模式下运行仿真时，复位信号有一个采样延迟。因此，当模块检测到复位事件时，在模块应用复位之前，在复位端口速率下会有一个采样延迟。有关延迟和 Simulink 任务模式的详细信息，请参阅 Excess Algorithmic Delay (Tasking Latency) 和 Time-Based Scheduling and Code Generation (Simulink Coder)。

#### 依赖关系

要启用此参数，请选择 **Running RMS** 参数。

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

输入或输入序列的均方根值

RMS 模块计算输入每一行或每一列的均方根 (RMS) 值，或沿输入指定维度的向量计算 RMS 值。它还可以计算整个输入的 RMS 值。可以使用 **Find the RMS value over** 参数指定维度。RMS 模块还可以在某个时间段内跟踪一系列输入中的 RMS 值。要跟踪一系列输入中的 RMS 值，请选择 **Running RMS** 参数。

**注意**

RMS 模块中的 **Running** 模式将在未来版本中移除。要在 Simulink® 中计算 running RMS，请改用 Moving RMS 模块。
