---
type: simulink-block
title: 'Matrix Concatenate'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Math Operations'
documentation_page: 'matrixconcatenate'
documentation_source_path: 'slref/matrixconcatenate.html'
language: zh-CN
chinese_source: worker-translation
---

# Matrix Concatenate

## 端口

### 输入

### **Port\_1** — 用于拼接的第一个输入 标量 | 向量 | 矩阵 | 数组

用于拼接的第一个输入，指定为标量、向量、矩阵或数组。

- 输入必须具有相同的数据类型。
- 仅当您将 **模式** 设置为 `Multidimensional array` 时，才支持矩阵和数组输入。

当数据类型为 `Simulink.Bus` 对象时，输入必须是非虚拟总线。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **Port\_N** — 用于拼接的第 *N* 个输入 标量 | 向量 | 矩阵 | 数组

用于拼接的第 *N* 个输入，指定为标量、向量、矩阵或数组。

- 输入必须具有相同的数据类型。
- 仅当您将 **模式** 设置为 `Multidimensional array` 时，才支持矩阵和数组输入。

#### 依赖关系

要添加输入端口，请将 **输入端口数** 设置为大于或等于 2 的整数。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### 输出

### **Port\_1** — 输入信号的拼接 标量 | 向量 | 矩阵 | 数组

沿指定维度拼接输入信号。输出与输入具有相同的数据类型。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### **输入端口数** — 输入端口数 `2`（默认） | 正整数

将模块的输入数目指定为小于或等于 65536 的实值正整数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NumInputs` |
| **值：** | `'2'`（默认） | 带引号的正整数 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,'NumInputs','3')`

### **模式** — 拼接类型 `Vector` | `Multidimensional array`

选择模块是在向量拼接模式还是多维数组拼接模式下运行。Vector Concatenate 模块的默认 **模式** 为 `Vector`。Matrix Concatenate 模块的默认 **模式** 为 `Multidimensional array`。

- 当您选择 `Vector` 时，模块执行向量拼接。
- 当您选择 `Multidimensional array` 时，模块执行矩阵拼接。

| **模式** 设置 | 输入信号 | 输出信号 |
| --- | --- | --- |
| `Vector` | - 向量 - 行向量（1-by-*M* 矩阵） - 列向量（*M*-by-1 矩阵） - 向量与行向量或列向量的组合 | 当所有输入均为向量时，输出为向量。  如果任一输入为行向量或列向量，则输出分别为行向量或列向量。 |
| `Multidimensional array` | 任意维度的信号（标量、向量和矩阵） | 输出始终为数组。  对于较低维度的输入，末尾维度假定为 `1`。例如，如果输出为 4-D，输入为 `[2x3]`（2-D），则此模块将输入视为 `[2x3x1x1]`。  拼接在您使用 **拼接维度** 参数指定的维度上进行。 |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Mode` |
| **值：** | `'Vector'` | `'Multidimensional array'` |

**示例：** `set_param(gcb,'Mode','Vector')`

### **拼接维度** — 沿其拼接输入数组的输出维度 标量整数

指定沿其拼接输入数组的输出维度。

- `1` — 垂直拼接输入。垂直矩阵拼接将输入矩阵在输出矩阵中堆叠在一起。当您插入 Vector Concatenate 模块并将 **模式** 设置为 `Multidimensional array` 时，默认值为 `1`。
- `2` — 水平拼接输入。水平矩阵拼接将输入矩阵并排放置在输出矩阵中。当您插入 Matrix Concatenate 模块时，默认值为 `2`。
- `3` 或更大 — 对输入执行多维拼接。

输入矩阵必须具有兼容的大小才能进行拼接。垂直拼接要求输入矩阵具有相同的列数。水平拼接要求输入矩阵具有相同的行数。

#### 依赖关系

要启用此参数，请将 **模式** 设置为 `Multidimensional array`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ConcatenateDimension` |
| **值：** | 带引号的标量整数 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,'ConcatenateDimension','2')`

## 所属库

Simulink / Math Operations Simulink / Matrix Operations DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Operations HDL Coder / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `image` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，要在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**数据类型支持**

此模块支持以下用于 HDL 代码生成的数据类型：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 枚举 | 复信号 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | 标量  向量  矩阵（最高 2-D） | Yes | Half  Single  Double | No | Yes | Yes | Yes | Yes |

**优化**

此模块参与以下 HDL 优化，以优化速度和面积。

**面积优化**

| 优化 | 描述 |
| --- | --- |
| 资源共享 (HDL Coder) | *资源共享* 是一种面积优化，其中 HDL Coder 识别多个功能等效的资源，并将它们替换为单个资源。 |
| 流式处理 (HDL Coder) | *流式处理* 是一种面积优化，其中 HDL Coder 将向量数据路径转换为标量数据路径（或转换为若干较小规模的向量数据路径）。 |

**速度优化**

| 优化 | 描述 |
| --- | --- |
| 分布式流水线 (HDL Coder) | *分布式流水线*，或寄存器重定时，是一种速度优化，它移动设计中现有的延迟，以缩短关键路径，同时保持功能行为。 |
| 时钟频率流水线 (HDL Coder) | *时钟频率流水线* 是 HDL Coder 中的一种优化框架，允许其他速度和面积优化在时钟频率下引入延迟。 |
| 自适应流水线 (HDL Coder) | *自适应流水线* 优化会创建带寄存器的模式或模块组合，通过向设计中的模块插入流水线寄存器，可以提高可实现的时钟频率并减少 FPGA 板上的面积使用。 |
| 关键路径估计 (HDL Coder) | 要快速识别设计中最可能的关键路径，请使用 *关键路径估计*。关键路径估计可加速查找关键路径的迭代过程。要了解在关键路径估计中已表征的模块，请参阅已表征模块 (HDL Coder)。 |

**FOR-GENERATE 循环支持**

对于此模块，HDL Coder 使用 `FOR-GENERATE` 循环生成代码。有关更多信息，请参阅展开 For-Generate 循环 (HDL Coder)。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2009b 中引入**

## 描述

拼接相同数据类型的输入矩阵以进行迭代处理

Matrix Concatenate 模块拼接输入信号以创建非标量信号，您可以使用子系统（例如 for-each、while-iterator 或 for-iterator 子系统）对其进行迭代处理。

您可以使用多个 Matrix Concatenate 模块分阶段创建输出信号，但结果沿每个拼接维度是展平的，就像使用单个模块拼接信号一样。

输出信号中的信号沿拼接维度按照模块输入信号的相同顺序出现。有关各种模块方向的端口顺序说明，请参阅识别旋转或翻转模块上的端口位置。

您必须使用 Vector Concatenate 或 Matrix Concatenate 模块来定义总线数组。有关更多信息，请参阅在总线数组中组合非虚拟总线。
