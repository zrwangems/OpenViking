---
type: simulink-block
title: 'Requirements Table'
family: 'slrequirements'
product_id: 'slrequirements'
product_name: 'Requirements Toolbox'
documentation_release: R2025b
official_category: 'Author and Validate Requirements / Model and Validate Requirements'
documentation_page: 'requirementstable'
documentation_source_path: 'ref/requirementstable.html'
language: zh-CN
chinese_source: official
---

# Requirements Table

## 端口

### 输入

### **Port\_1** — 输入数据 标量 | 向量 | 矩阵

输入数据，指定为实数值标量、向量或矩阵。您定义的每个输入数据都有对应的输入端口。

#### 依赖关系

要创建输入端口，需打开此模块并在**符号**窗格中创建输入数据。请参阅在 Requirements Table 模块中定义数据。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出数据 标量 | 向量 | 矩阵

输出数据，指定为实数值标量、向量或矩阵。您定义的每个输出数据都有对应的输出端口。

#### 依赖关系

要创建输出端口，请打开此模块并在**符号**窗格中创建输出数据。请参阅在 Requirements Table 模块中定义数据。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus`

## 参数

要以交互方式编辑模块参数，请执行以下操作：

- 使用属性检查器。在 Simulink 工具条中，在**仿真**选项卡的**准备**库中，选择**属性检查器**。
- 使用“表属性”窗口。打开此模块。然后，在**仿真**选项卡的**准备**部分中，点击**表属性**。

**注意**

Requirements Table 模块也有 Subsystem (Simulink) 模块参数，您可以通过右键点击此模块并点击**模块参数(子系统)** 来访问这些参数。不过，不推荐更新这些模块参数。

### **更新方法** — 用于激活模块的方法 **继承** (默认) | **离散**

将用于激活 Requirements Table 模块的方法指定为以下值之一：

- **继承** - 来自 Simulink 模型的输入用于激活 Requirements Table 模块。

  如果您定义了输入数据，Requirements Table 模块将以最快的数据输入速率进行采样。如果您未定义输入数据，Requirements Table 模块将以父级子系统的执行行为定义的速率进行采样。
- **离散** - 使用您在 Requirements Table 模块的**采样时间**参数中指定的速率对 Requirements Table 模块进行采样。Requirements Table 模块将以与指定速率相对应的固定时间间隔生成隐式事件。模型中的其他模块可以有不同的采样时间。

### **采样时间** — 模块在仿真期间激活的时间间隔 `-1` (默认) | 标量 | 向量

指定 Requirements Table 在仿真期间激活的时间间隔。默认值表示此模块从 Simulink 继承采样时间。此属性使用您在 Simulink 中使用的相同格式。有关指定采样时间的详细信息，请参阅指定采样时间 (Simulink)。

请勿在 Subsystem 模块参数中使用**采样时间**参数，而应使用“表属性”窗口。

#### 依赖关系

要启用此参数，请将模块参数**更新方法**设置为**离散**。

### **对整数溢出进行饱和处理** — 数据在整数溢出时是否饱和 `on` (默认) | `off`

指定 Requirements Table 模块中的数据在整数溢出时是否饱和，值包括：

- `on` - 模块通过将整数设置为字长所允许的最大正值或负值来对其进行饱和处理。此设置与 MATLAB® 行为一致。
- `off` - 模块对值进行绕回处理。

有关详细信息，请参阅饱和与绕回 (Fixed-Point Designer)。

### **支持可变大小数组** — 模块是否支持可变大小数据 `on` (默认) | `off`

指定 Requirements Table 模块是否支持在仿真期间维度会发生变化的输入和输出数据。当此参数为 `on` 时，您可以通过为输出数据启用**可变大小**属性来定义可变大小输出。有关详细信息，请参阅可变大小。

### **在预条件中启用输出** — 模块是否支持在预条件中使用输出数据 `off` (默认) | `on`

指定模块是否可以在预条件中使用**作用域**设置为**输出**的数据。如果禁用此参数，当在预条件中使用输出数据时（除非这些数据是 `getPrevious` 的输入参量），模块将突出显示这些预条件所在的单元格并显示警报图标 。但如果 `getPrevious` 尝试返回未定义数据的时间步的数据值，`getPrevious` 将返回未定义的行为。

#### 提示

- 在预条件中使用输出数据时，仿真期间在您的需求中可能会遇到写前读问题。为解决这些问题，请按顺序指定您的需求。有关详细信息，请参阅检测先读后写问题和利用形式需求的评估顺序。

### 定点属性

### **需求表 fimath** — 默认 `fimath` 对象属性 `Same as MATLAB` (默认) | `Specify Other`

将 Requirements Table 模块的默认 `fimath` 对象属性指定为以下值之一：

- `Same as MATLAB` - 此模块使用与当前默认 `fimath` 对象相同的 `fimath` 对象属性。文本框呈灰色显示，并显示当前全局 `fimath` 对象。
- `Specify other` - 通过以下两种方式之一在文本框中指定您自己的 `fimath` 对象：

  - 在文本框内构造 `fimath` 对象。
  - 在 MATLAB 或模型工作区中构造 `fimath` 对象，然后在文本框中输入其变量名称。如果您使用此选项并计划与他人共享您的模型，请在模型工作区中定义变量。
- 有关 `fimath` 对象的详细信息，请参阅fimath Object Construction (Fixed-Point Designer)。

#### 提示

- 对于模块的内容而言，Requirements Table 模块的 `fimath` 对象的作用相当于 `globalfimath` (Fixed-Point Designer) 函数。此模块将此参数中的 `fimath` 对象属性与您选择视为 `fi` 对象的此模块的定点和整数输入信号相关联。在 Requirements Table 模块中构造 `fi` 对象会引入以下需要额外考虑的事项。

  - 如果在构造 `fi` 对象时没有 `fimath` 对象与之相关联，则 `fi` 构造函数将使用默认的 `fimath` 对象设置，而不管**需求表 fimath** 中的属性如何。如果您在构造该 `fi` 对象之后对其执行操作，则该对象将采用**需求表 fimath** 中的属性。
  - 如果您在 `fi` 构造函数中指定 `fimath` 对象，则 `fi` 构造函数在对值进行量化时将遵循该 `fimath` 对象。`fi` 构造函数中未指定的 `fimath` 设置将使用**需求表 fimath** 中指定的属性。

## 所属库

Requirements Toolbox

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

### GPU 代码生成 使用 GPU Coder™ 为 NVIDIA® GPU 生成 CUDA® 代码。

实际数据类型或功能支持取决于模块实现。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 为 HDL 实现和综合逻辑提供额外的配置选项。

**HDL 架构**

此模块有一个默认的 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstMultiplierOptimization** | 正则有符号数 (CSD) 或因式分解 CSD 优化。默认值为 **none**。另请参阅ConstMultiplierOptimization (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过移动设计中的现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分布，或寄存器重定时。默认值为 **inherit**。另请参阅DistributedPipelining (HDL Coder)。 |
| **GuardIndexVariables** | 指定是否将数组索引从条件语句中提升出来。启用某些优化（如 RAM 映射、循环流式处理、共享等）时，表达式会从数组索引中移出。此时，会为该表达式创建一个临时变量，这可能会在仿真期间导致索引越界错误。默认值为 **off**。请参阅GuardIndexVariables (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线阶段数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **InstantiateFunctions** | 为每个函数生成 VHDL® `entity` 或 Verilog® `module`。默认值为 **off**。另请参阅InstantiateFunctions (HDL Coder)。 |
| **LoopOptimization** | 展开循环、对循环进行流式处理，或者不进行循环优化。默认值为 **none**。另请参阅LoopOptimization (HDL Coder)。 |
| **MapPersistentVarsToRAM** | 将持久数组映射到 RAM。默认值为 **off**。另请参阅MapPersistentVarsToRAM (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线阶段数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |
| **ResetType** | 抑制复位逻辑生成。默认值为 **default**，即生成复位逻辑。另请参阅ResetType (HDL Coder)。 |
| **SharingFactor** | 映射到单个共享资源的功能等效资源的数量。默认值为 0。另请参阅Resource Sharing (HDL Coder)。 |

**优化**

此模块参与以下 HDL 优化，以优化速度和面积。

**速度和面积优化**

| 优化 | 描述 |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *分布式流水线*（或寄存器重定时）是一种速度优化技术，它通过移动设计中的现有延迟来减少关键路径，同时保持功能行为不变。 |
| Resource Sharing (HDL Coder) | *资源复用*是一种面积优化技术，在这种技术中，HDL Coder 会识别出多个功能等效的资源，然后用单个资源来替代它们。 |
| Understand Delay Balancing in HDL Coder (HDL Coder) | 当优化或模块实现选项在模型的关键路径上引入延迟时，*延迟平衡*会检测到一条路径上引入了新的延迟，然后在其他路径上插入匹配的延迟。 |
| Clock-Rate Pipelining (HDL Coder) | *时钟频率流水线*是 HDL Coder 中的一个优化框架，它允许其他速度和面积优化以时钟速率引入延迟。 |
| Adaptive Pipelining (HDL Coder) | *自适应流水线*优化会创建带有寄存器的模块模式或组合，通过将流水线寄存器插入设计中的模块，可以提高可实现的时钟频率，并减少 FPGA 板上的面积使用。 |
| 关键路径估计 (HDL Coder) | 为了快速识别设计中最可能的关键路径，请使用*关键路径估计*。关键路径估计可以加快寻找关键路径的迭代过程。要了解在关键路径估计中表征的模块，请参阅Characterized Blocks (HDL Coder)。 |

**限制**

应用优化时，此模块具有以下限制：

- 具有 **Trigger** 端口的模块不支持 HDL 优化。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型或功能支持取决于模块实现。

## 版本历史

**在 R2022a 中推出**

### R2022b: Requirements Table 模块支持字符串

现在，您可以在 Requirements Table 模块中创建和操作字符串数据。字符串数据类型与 MATLAB 和 Simulink 中的字符串兼容。

## 描述

使用输入条件对形式化需求进行建模

Requirements Table 模块对形式化需求进行建模。此模块首先评估**预条件**列中的条件。如果这些条件得到满足，此模块会检查其他仿真数据是否满足**预条件**列中的条件，或者执行**操作**列中的操作。有关详细信息，请参阅使用 Requirements Table 模块创建正式需求。

您可以通过在**假设**选项卡中定义假设，来基于您的模型的物理限制为需求设定约束。请参阅将假设添加到需求中。

仅当您拥有 Requirements Toolbox™ 时才可以配置此模块。
