---
type: simulink-block
title: 'Maximum'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'maximum'
documentation_source_path: '../dsp/ref/maximum.html'
language: zh-CN
chinese_source: worker-translation
---

# Maximum

## 端口

### 输入

### **In** — 数据输入 向量 | 矩阵 | *N*-D 数组

模块接受实值或复值多通道和多维输入。输入可以是 floating-point、fixed-point 或 Boolean。实 fixed-point 输入可以是 signed 或 unsigned。复 fixed-point 输入必须为 signed。

在将 **Mode** 参数设置为 `Running` 且将 **Reset port** 参数设置为 `None` 以外的任何选项之前，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** Yes

### **Rst** — Reset port 标量

指定导致模块重置 running maximum 的重置事件。**Rst** 输入的采样时间必须是输入采样时间的正整数倍。

#### 依赖关系

要启用此端口，请将 **Mode** 参数设置为 `Running`，并将 **Reset port** 参数设置为 `None` 以外的任何选项。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `Boolean`

### 输出

### **Val** — 沿指定维度的最大值 标量 | 向量 | 矩阵 | *N*-D 数组

最大值的数据类型与输入的数据类型一致。

当 **Mode** 参数设置为 `Value and Index` 或 `Value` 时，以下适用：

- 计算最大值的维度大小为 1。所有其他维度的大小与输入数组匹配。例如，当输入为 *M*-by-*N*-by-*P* 数组，维度设置为 `1` 时，模块输出 1-by-*N*-by-*P* 数组。当维度设置为 `3` 时，模块输出二维 *M*-by-*N* 矩阵。
- 当输入为 *M*-by-*N* 矩阵，维度设置为 `1` 时，模块输出 1-by-*N* 矩阵。

如果指定模块在整个输入上计算最大值，则模块输出标量。

当 **Mode** 参数设置为 `Running` 时，模块在 *M*-by-*N* 输入的时间序列中跟踪每个通道的最大值。在此模式下，还必须将 **Input processing** 参数指定为以下之一：

- `Elements as channels (sample based)` — 模块将输入的每个元素视为单独通道。对于大小为 *M*-by-*N*-by-*P* 的三维输入信号，模块输出 *M*-by-*N*-by-*P* 数组。输出的每个 *yijk* 元素包含自上次重置以来所有输入中元素 *uijk* 观测到的最大值。

  当重置事件发生时，当前帧中的 running maximum *yijk* 重置为元素 *uijk*。
- `Columns as channels (frame based)` — 模块将输入的每一列视为单独通道。此选项不支持 N > 2 的 N 维输入信号。对于大小为 *M*-by-*N* 的二维输入信号，模块输出 *M*-by-*N* 矩阵。输出的每个元素 *yij* 包含自上次重置以来所有输入的第 *j* 列中观测到的最大值，直至并包括当前输入的 *uij* 元素。

  当重置事件发生时，每个通道的 running maximum 变为当前输入帧中直至并包括当前输入样本的所有样本的最大值。

每当在可选 **Rst** 端口检测到重置事件时，模块会重置 running maximum。重置采样时间必须是输入采样时间的正整数倍。

#### 依赖关系

要启用此端口，请将 **Mode** 参数设置为 `Value and Index` 或 `Value`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** Yes

### **Idx** — 沿指定维度的最大值的索引 标量 | 向量 | 矩阵 | *N*-D 数组

当输入为 `double` 时，索引值也为 `double`。否则，索引值为 `uint32`。

#### 依赖关系

要启用此端口，请将 **Mode** 参数设置为 `Value and Index` 或 `Index`。

**数据类型：** `double` | `uint32`

## 参数

### 主选项卡

### **Mode** — 模块运行的模式 `Value and Index`（默认） | `Value` | `Index` | `Running`

当 **Mode** 参数设置为：

- `Value` — 模块计算输入每行或每列中的最大值，或沿输入指定维度的向量中的最大值。它还可以在每个采样时间计算整个输入的最大值，并输出数组 *y*。输出中的每个元素是对应列、行、向量或整个输入中的最大值。输出 *y* 取决于 **Find the maximum value over** 参数的设置。考虑大小为 *M*-by-*N*-by-*P* 的三维输入信号。将 **Find the maximum value over** 设置为：

  - `Each row` — 每个采样时间的输出 *y* 由 *M*-by-1-by-*P* 数组组成，其中每个元素包含输入第二个维度上每个向量的最大值。对于 *M*-by-*N* 矩阵输入，每个采样时间的输出是 *M*-by-1 列向量。
  - `Each column` — 每个采样时间的输出 *y* 由 1-by-*N*-by-*P* 数组组成，其中每个元素包含输入第一个维度上每个向量的最大值。对于 *M*-by-*N* 矩阵输入，每个采样时间的输出是 1-by-*N* 行向量。

    在此模式下，模块将长度为 *M* 的无方向向量输入视为 *M*-by-1 列向量。
  - `Entire input` — 每个采样时间的输出 *y* 是一个标量，包含 *M*-by-*N*-by-*P* 输入矩阵中的最大值。
  - `Specified dimension` — 每个采样时间的输出 *y* 取决于 **Dimension**。如果 **Dimension** 设置为 `1`，输出与选择 `Each column` 时相同。如果 **Dimension** 设置为 `2`，输出与选择 `Each row` 时相同。如果 **Dimension** 设置为 `3`，每个采样时间的输出是 *M*-by-*N* 矩阵，包含输入第三个维度上每个向量的最大值。

  **复输入**

  对于复输入，模块选择输入每行或每列中、沿输入指定维度的向量中或整个输入中具有最大幅值平方的值，如下图所示。对于复数值 u=a+bi，幅值平方为 a2+b2。
- `Index` — 模块计算输入每行或每列中的最大值，沿输入指定维度的向量中的最大值，或整个输入的最大值，并输出索引数组 *I*。*I* 中的每个元素是一个整数，索引对应列、行、向量或整个输入中的最大值。输出 *I* 取决于 **Find the maximum value over** 参数的设置。考虑大小为 *M*-by-*N*-by-*P* 的三维输入信号：

  - `Each row` — 每个采样时间的输出 *I* 由 *M*-by-1-by-*P* 数组组成，其中每个元素包含输入第二个维度上每个向量的最大值的索引。对于 *M*-by-*N* 矩阵输入，每个采样时间的输出是 *M*-by-1 列向量。
  - `Each column` — 每个采样时间的输出 *I* 由 1-by-*N*-by-*P* 数组组成，其中每个元素包含输入第一个维度上每个向量的最大值的索引。对于 *M*-by-*N* 矩阵输入，每个采样时间的输出是 1-by-*N* 行向量。

    在此模式下，模块将长度为 *M* 的无方向向量输入视为 *M*-by-1 列向量。
  - `Entire input` — 每个采样时间的输出 *I* 是 1-by-3 向量，包含 *M*-by-*N*-by-*P* 输入矩阵中最大值的位置。对于 *M*-by-*N* 矩阵输入，输出是 1-by-2 向量。
  - `Specified dimension` — 每个采样时间的输出 *I* 取决于 **Dimension**。如果 **Dimension** 设置为 1，输出与选择 `Each column` 时相同。如果 **Dimension** 设置为 2，输出与选择 `Each row` 时相同。如果 **Dimension** 设置为 3，每个采样时间的输出是 *M*-by-*N* 矩阵，包含输入第三个维度上每个向量的最大值的索引。

  当最大值出现多次时，计算出的索引对应第一次出现。例如，当输入为列向量 `[3 2 1 2 3]'` 时，当选择 `Each column` 时，计算出的基于 1 的最大值索引为 `1`，而不是 `5`。
- `Value and Index` — 模块输出输入每行或每列中的最大值，沿输入指定维度的向量中的最大值，或整个输入的最大值，以及对应的索引数组 *I*。
- `Running` — 模块在 *M*-by-*N* 输入的时间序列中跟踪每个通道的最大值。在此模式下，还必须将 **Input processing** 参数指定为以下之一：

  - `Elements as channels (sample based)` — 模块将输入的每个元素视为单独通道。对于大小为 *M*-by-*N*-by-*P* 的三维输入信号，模块输出 *M*-by-*N*-by-*P* 数组。输出的每个 *yijk* 元素包含自上次重置以来所有输入中元素 *uijk* 观测到的最大值。

    当重置事件发生时，当前帧中的 running maximum *yijk* 重置为元素 *uijk*。
  - `Columns as channels (frame based)` — 模块将输入的每一列视为单独通道。此选项不支持 N > 2 的 N 维输入信号。对于大小为 *M*-by-*N* 的二维输入信号，模块输出 *M*-by-*N* 矩阵。输出的每个元素 *yij* 包含自上次重置以来所有输入的第 *j* 列中观测到的最大值，直至并包括当前输入的 *uij* 元素。

    当重置事件发生时，每个通道的 running maximum 变为当前输入帧中直至并包括当前输入样本的所有样本的最大值。

  每当在可选 **Rst** 端口检测到重置事件时，模块会重置 running maximum。重置采样时间必须是输入采样时间的正整数倍。

  **可变大小输入的 Running 模式**

  当输入是可变大小信号，并且将 **Mode** 设置为 `Running` 时：

  - 如果将 **Input processing** 参数设置为 `Elements as channels (sample based)`，状态会重置。
  - 如果将 **Input processing** 参数设置为 `Columns as channels (frame based)`，则：

    - 当输入大小差异在于通道数（列数）时，状态会重置。
    - 当输入大小差异在于通道长度（行数）时，不会重置，running 操作照常执行。

### **Index base** — 最大值索引的基数 `One`（默认） | `Zero`

指定最大值索引是使用基于 1 的编号还是基于 0 的编号报告。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Index` 或 `Value and Index`。

### **Find the maximum value over** — 模块计算最大值的维度 `Each column`（默认） | `Each row` | `Entire input` | `Specified dimension`

- `Each column` — 模块输出每一列上的最大值。
- `Each row` — 模块输出每一行上的最大值。
- `Entire input` — 模块输出整个输入上的最大值。
- `Specified dimension` — 模块输出在 **Dimension** 参数中指定的维度上的最大值。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Value and Index`、`Value` 或 `Index`。

### **Dimension** — 自定义维度 `1`（默认） | 标量

指定模块计算最大值的输入信号的维度（基于 1 的值）。此参数的值必须大于 0 且小于输入信号中的维度数。

#### 依赖关系

要启用此参数，请将 **Find the maximum value over** 设置为 `Specified dimension`。

### **Input processing** — 在 running 模式下处理输入的方法 `Columns as channels (frame based)`（默认） | `Elements as channels (sample based)`

- `Columns as channels (frame based)` — 模块将输入的每一列视为单独通道。此选项不支持 N > 2 的 N 维输入信号。对于大小为 *M*-by-*N* 的二维输入信号，模块输出 *M*-by-*N* 矩阵。输出的每个元素 *yij* 包含自上次重置以来所有输入的第 *j* 列中观测到的最大值，直至并包括当前输入的 *uij* 元素。

  当重置事件发生时，每个通道的 running maximum 变为当前输入帧中直至并包括当前输入样本的所有样本的最大值。
- `Elements as channels (sample based)` — 模块将输入的每个元素视为单独通道。对于大小为 *M*-by-*N*-by-*P* 的三维输入信号，模块输出 *M*-by-*N*-by-*P* 数组。输出的每个 *yijk* 元素包含自上次重置以来所有输入中元素 *uijk* 观测到的最大值。

  当重置事件发生时，当前帧中的 running maximum *yijk* 重置为元素 *uijk*。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Running`。

### **Reset port** — 重置事件 `None`（默认） | `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

每当在可选 **Rst** 端口检测到重置事件时，模块会重置 running maximum。重置采样时间必须是正整数，并且是输入采样时间的倍数。

- `None` — 禁用 **Rst** 端口。
- `Rising edge` — 当 **Rst** 输入执行以下操作之一时触发重置操作：

  - 从负值上升到正值或零。
  - 从零上升到正值，其中该上升不是从负值到零的上升的延续。
- `Falling edge` — 当 **Rst** 输入执行以下操作之一时触发重置操作：

  - 从正值下降到负值或零。
  - 从零下降到负值，其中该下降不是从正值到零的下降的延续。
- `Either edge` — 当 **Rst** 输入为 `Rising edge` 或 `Falling edge` 时触发重置操作。
- `Non-zero sample` — 在 **Rst** 输入不为零的每个采样时间触发重置操作。

  **注意**

  在 Simulink `MultiTasking` 模式下运行仿真时，重置信号有一个采样延迟。因此，当模块检测到重置事件时，在模块应用重置之前，会以重置端口速率存在一个采样延迟。有关延迟和 Simulink 任务模式的详细信息，请参阅 Excess Algorithmic Delay (Tasking Latency) 和 Time-Based Scheduling and Code Generation (Simulink Coder)。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Running`。

### 数据类型选项卡

**注意**

要使用这些参数，数据输入必须是复数和 fixed-point。此类输入的实部和虚部的平方和会在进行比较之前形成，如主选项卡中 'Mode' 参数下所述。实部和虚部的平方结果放入 product output 数据类型。平方和的结果放入 accumulator 数据类型。对于其他类型的输入，这些参数将被忽略。

### **Rounding mode** — 舍入操作的方法 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将 fixed-point 操作的舍入模式指定为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅 rounding mode。

### **Saturate on integer overflow** — 溢出操作的方法 off（默认） | on

选择此参数时，模块对 fixed-point 操作的结果进行饱和。清除此参数时，模块对 fixed-point 操作的结果进行回绕。有关 `saturate` 和 `wrap` 的详细信息，请参阅 overflow mode for fixed-point operations。

### **Product output** — Product output 数据类型 `Inherit: Same as input`（默认） | `fixdt([],16,0)`

**Product output** 指定 Maximum 模块中乘积运算输出的数据类型。有关 product output 数据类型的更多信息，请参阅 Multiplication Data Types。

- `Inherit: Same as input` — 模块将 product output 数据类型指定为与输入数据类型相同。
- `fixdt([],16,0)` — 模块指定自动有符号、二进制点、缩放、fixed-point 数据类型，字长为 16 bits，小数长度为 0。

或者，可以使用 **Data Type Assistant** 设置 **Product output** 数据类型。要使用该助手，请单击 **Show data type assistant** 按钮。

有关 data type assistant 的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Accumulator** — Accumulator 数据类型 `Inherit: Same as product output`（默认） | `Inherit: Same as input` | `fixdt([],16,0)`

**Accumulator** 指定 Maximum 模块中累加运算输出的数据类型。

- `Inherit: Same as product output` — 模块将 accumulator 数据类型指定为与 product output 数据类型相同。
- `Inherit: Same as input` — 模块将 accumulator 数据类型指定为与输入数据类型相同。
- `fixdt([],16,0)` — 模块指定自动有符号、二进制点、缩放、fixed-point 数据类型，字长为 16 bits，小数长度为 0。

或者，可以使用 **Data Type Assistant** 设置 **Accumulator** 数据类型。要使用该助手，请单击 **Show data type assistant** 按钮。

有关 data type assistant 的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Lock data type settings against changes by the fixed-point tools** — 防止 fixed-point 工具覆盖数据类型 off（默认） | on

选择此参数以防止 fixed-point 工具覆盖您在模块对话框中指定的数据类型。

## 所属库

DSP System Toolbox / Statistics DSP System Toolbox HDL Support / Statistics

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

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**限制**

对于 HDL 代码生成，**In** 端口必须是向量。在这种情况下，输出 **Val** 和 **Idx** 端口为标量。

**HDL 架构**

此模块具有多周期实现，会在生成的代码中引入额外延迟。要查看增加的延迟，请查看生成的模型或验证模型。请参阅 Generated Model and Validation Model (HDL Coder)。

| 架构 | 额外延迟周期 | 描述 |
| --- | --- | --- |
| `default`  `Tree` | 0 | 生成比较器的树结构。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出处放置的寄存器数。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **InstantiateStages** | 为每个级联级生成 VHDL® `entity` 或 Verilog® `module`。默认值为 `off`。另请参阅 InstantiateStages (HDL Coder)。 |
| **SerialPartition** | 将 Cascade-serial 实现的分区指定为每个分区长度的向量。默认设置使用最少级数。另请参阅 SerialPartition (HDL Coder)。 |

## 版本历史

**在 R2006a 之前引入**

## 描述

输入或输入序列的最大值

Maximum 模块标识输入每行或每列中最大元素的值和位置，或沿输入指定维度的向量中最大元素的值和位置。它还可以计算整个输入的最大值。Maximum 模块还可以在一段时间内跟踪输入序列中的最大值。**Mode** 参数指定模块的运行模式，可设置为以下之一：

- `Value` — 模块输出指定维度中的最大值。
- `Index` — 模块输出指定维度中最大值的索引数组。
- `Value and Index` — 模块输出指定维度中的最大值和对应索引数组。
- `Running` — 模块在一段时间内跟踪输入序列中的最大值。

可以使用 **Find the maximum value over** 参数指定维度。

**注意**

Maximum 模块中的 **Running** 模式将在未来版本中移除。要在 Simulink® 中计算 running maximum，请改用 Moving Maximum 模块。
