---
type: simulink-block
title: 'Matrix Concatenate'
family: math-operations
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'matrixconcatenate'
language: zh-CN
chinese_source: official
---

# Matrix Concatenate

## 端口

### 输入

### **Port\_1** — 要串联的第一个输入 标量 | 向量 | 矩阵 | 数组

要串联的第一个输入，指定为标量、向量、矩阵或数组。

- 输入必须具有相同的数据类型。
- 仅当**模式**设置为**多维数组**时，才支持矩阵和数组输入。

当数据类型是 `Simulink.Bus` 对象时，输入必须为非虚拟总线。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **Port\_N** — 要串联的第 *N* 个输入 标量 | 向量 | 矩阵 | 数组

要串联的第 *N* 个输入，指定为标量、向量、矩阵或数组。

- 输入必须具有相同的数据类型。
- 仅当**模式**设置为**多维数组**时，才支持矩阵和数组输入。

#### 依赖关系

要添加输入端口，请将**输入数目**设置为大于或等于 2 的整数。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### 输出

### **Port\_1** — 输入信号的串联 标量 | 向量 | 矩阵 | 数组

输入信号沿指定维度的串联。输出的数据类型与输入相同。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条中，在**仿真**选项卡的**准备**库中，选择**属性检查器**。

### **输入数目** — 输入端口数目 `2` (默认) | 正整数

将模块的输入的个数指定为小于或等于 65536 的实数值正整数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `NumInputs` |
| **值:** | `'2'` (默认) | positive integer in quotes |
| **数据类型:** | `char` | `string` |

**示例:** `set_param(gcb,'NumInputs','3')`

### **模式** — 串联类型 **向量** | **多维数组**

选择模块是以向量模式还是多维数组串联模式运行。Vector Concatenate 模块的默认**模式**是**向量**。Matrix Concatenate 模块的默认**模式**是**多维数组**。

- 当您选择**向量**时，模块将执行向量串联。
- 当您选择**多维数组**时，模块会执行矩阵串联。

| **模式**设置 | 输入信号 | 输出信号 |
| --- | --- | --- |
| **向量** | - 向量 - 行向量（1×*M* 矩阵） - 列向量（*M*×1 矩阵） - 向量与行向量或列向量的组合 | 当所有输入都是向量时，输出是向量。  如果输入是行向量或列向量，则输出分别是行向量或列向量。 |
| **多维数组** | 任何维度的信号（标量、向量和矩阵） | 输出始终都是数组。  对于维度较低的输入，尾部维度假定为 `1`。例如，如果输出是 4 维，输入为 `[2x3]`（2 维），此模块会将输入视为 `[2x3x1x1]`。  串联在您使用**串联维度**参数指定的维度上进行。 |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Mode` |
| **值:** | `'Vector'` | `'Multidimensional array'` |

**示例:** `set_param(gcb,'Mode','Vector')`

### **串联维度** — 沿其串联输入数组的输出维度 整数标量

指定沿哪个输出维度串联输入数组。

- `1` - 垂直串联输入。垂直矩阵串联将输入矩阵上下堆叠在输出矩阵中。当您插入 Vector Concatenate 模块并将**模式**设置为**多维数组**时，默认值为 `1`。
- `2` - 水平串联输入。水平矩阵串联将输入矩阵并排放置在输出矩阵中。当插入 Matrix Concatenate 模块时，默认值为 `2`。
- `3` 或更多 - 对输入执行多维串联。

输入矩阵必须具有兼容的大小才能串联。垂直串联要求输入矩阵具有相同的列数。水平串联要求输入矩阵具有相同的行数。

#### 依赖关系

要启用此参数，请将**模式**设置为**多维数组**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ConcatenateDimension` |
| **值:** | scalar integer in quotes |
| **数据类型:** | `char` | `string` |

**示例:** `set_param(gcb,'ConcatenateDimension','2')`

## 所属库

Simulink / Math Operations Simulink / Matrix Operations DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Operations HDL Coder / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `image` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

**数据类型支持**

该模块支持使用以下数据类型进行 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 枚举 | 复信号 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | 标量  向量  矩阵（最高二维） | 是 | 半精度  单精度  双精度 | 否 | 是 | 是 | 是 | 是 |

**优化**

模块参与以下 HDL 优化，以优化速度和面积。

**面积优化**

| 优化 | 描述 |
| --- | --- |
| Resource Sharing (HDL Coder) | *资源复用*是一种面积优化，其中 HDL Coder 确定多个在功能上等效的资源，并用单个资源替换它们。 |
| Streaming (HDL Coder) | *流式处理*是一种面积优化，其中 HDL Coder 将向量数据路径变换为标量数据路径（或多个较小的向量数据路径）。 |

**速度优化**

| 优化 | 描述 |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *分布式流水线*或寄存器重定时是一种速度优化，它可以移动设计中的现有延迟，以在缩减关键路径的同时保留功能性行为。 |
| Clock-Rate Pipelining (HDL Coder) | *时钟频率流水线*是 HDL Coder 中的一个优化框架，它允许其他速度优化和面积优化在时钟频率下引入延迟。 |
| Adaptive Pipelining (HDL Coder) | *自适应流水线*优化创建带寄存器的模块模式或组合，通过在设计中的模块中插入流水线寄存器，可以提高可实现的时钟频率并减少 FPGA 板上的面积使用量。 |
| 关键路径估计 (HDL Coder) | 要快速确定设计中最可能的关键路径，请使用*关键路径估计*。关键路径估计加速寻找关键路径的迭代过程。要了解在关键路径估计中表征的模块，请参阅Characterized Blocks (HDL Coder)。 |

**FOR-GENERATE 循环支持**

对于此模块，HDL Coder 使用 `FOR-GENERATE` 循环生成代码。有关详细信息，请参阅Unroll For-Generate Loops (HDL Coder)

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2009b 中推出**

## 描述

串联相同数据类型的输入矩阵以进行迭代处理

Matrix Concatenate 模块会串联输入信号以创建一个非标量信号，您可以使用子系统（例如，For Each、While Iterator 或 For Iterator 子系统）对其进行迭代处理。

您可以使用多个 Matrix Concatenate 模块分多个阶段创建输出信号，但结果沿每个串联维度上都是平面结构，就像您只使用一个模块串联信号一样。

输出信号中信号的显示顺序与沿串联维度的模块的输入信号相同。有关各种模块方向的端口顺序的描述，请参阅标识旋转或翻转模块上的端口位置。

您必须使用 Vector Concatenate 或 Matrix Concatenate 模块来定义总线数组。有关详细信息，请参阅 使用总线数组组合非虚拟总线。
