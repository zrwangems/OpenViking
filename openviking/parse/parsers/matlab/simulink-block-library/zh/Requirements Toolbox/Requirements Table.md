---
type: simulink-block
title: 'Requirements Table'
family: 'slrequirements'
product_id: 'slrequirements'
product_name: 'Requirements Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'requirementstable'
documentation_source_path: 'ref/requirementstable.html'
language: zh-CN
chinese_source: worker-translation
---

# Requirements Table

## 端口

### 输入

### **Port\_1** — 输入数据 标量 | 向量 | 矩阵

输入数据，指定为实数值标量、向量或矩阵。您定义的每个输入数据都有一个对应的输入端口。

#### 依赖关系

要创建输入端口，请打开该模块并在 **Symbols** 窗格中创建输入数据。请参阅 Define Data in Requirements Table Blocks。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出数据 标量 | 向量 | 矩阵

输出数据，指定为实数值标量、向量或矩阵。您定义的每个输出数据都有一个对应的输出端口。

#### 依赖关系

要创建输出端口，请打开该模块并在 **Symbols** 窗格中创建输出数据。请参阅 Define Data in Requirements Table Blocks。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus`

## 参数

要以交互方式编辑模块参数：

- 使用 Property Inspector。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。
- 使用 Table Properties 窗口。打开该模块。然后，在 **Simulation** 选项卡的 **Prepare** 部分中，点击 **Table Properties**。

**注意**

Requirements Table 模块还具有 Subsystem (Simulink) 模块参数，您可以通过右键点击该模块并点击 **Block Parameters (Subsystem)** 来访问这些参数。但是，不建议更新这些模块参数。

### **Update method** — 用于激活模块的方法 `Inherited`（默认） | `Discrete`

将激活 Requirements Table 模块的方法指定为以下值之一：

- `Inherited` — 来自 Simulink 模型的输入激活 Requirements Table 模块。

  如果您定义了输入数据，Requirements Table 模块以最快输入数据的速率进行采样。如果您未定义输入数据，Requirements Table 模块以父子系统执行行为所定义的速率进行采样。
- `Discrete` — 使用您在 Requirements Table 模块的 **Sample time** 参数中指定的速率对 Requirements Table 模块进行采样。Requirements Table 模块以与指定速率对应的固定时间间隔生成隐式事件。模型中的其他模块可以具有不同的采样时间。

### **Sample time** — 模块在仿真期间激活的时间间隔 `-1`（默认） | 标量 | 向量

指定 Requirements Table 模块在仿真期间激活的时间间隔。默认值表示该模块从 Simulink 继承采样时间。此属性使用与 Simulink 中相同的格式。有关指定采样时间的详细信息，请参阅 Specify Sample Time (Simulink)。

不要使用 Subsystem 模块参数中的 **Sample Time** 参数。而应使用 Table Properties 窗口。

#### 依赖关系

要启用此参数，请将模块参数 **Update method** 设置为 `Discrete`。

### **Saturate on interger overflow** — 数据是否在整数溢出时饱和 `on`（默认） | `off`

将 Requirements Table 模块中的数据在整数溢出时是否饱和指定为以下值之一：

- `on` — 该模块通过将整数设置为字长所允许的最大正值或负值来使其饱和。此设置与 MATLAB® 行为一致。
- `off` — 该模块对该值进行回绕。

有关详细信息，请参阅 Saturation and Wrapping (Fixed-Point Designer)。

### **支持可变大小数组** — 模块是否支持可变大小数据 `on`（默认）| `off`

指定 Requirements Table 模块是否支持在仿真期间维度发生变化的输入和输出数据。当此参数为 `on` 时，您可以通过在输出数据上启用 **Variable size** 属性来定义可变大小输出。有关详细信息，请参阅 Variable size。

### **在前置条件中启用输出** — 模块是否在前置条件中支持输出数据 `off`（默认）| `on`

指定模块是否可以在前置条件中使用 **Scope** 设置为 `Output` 的数据。如果禁用此参数，模块会在使用输出数据的前置条件中高亮显示该单元格并显示警报图标，除非该数据是 `getPrevious` 的输入参数。但是，如果 `getPrevious` 尝试在数据未定义的时间步返回该数据的值，`getPrevious` 将返回未定义行为。

#### 提示

- 当您在前置条件中使用输出数据时，可能会在仿真期间的需求中遇到先读后写问题。要解决这些问题，请按顺序指定您的需求。有关详细信息，请参阅 Detect Read-Before-Write Issues 和 Leverage Evaluation Order of Formal Requirements。

### 定点属性

### **Requirements Table fimath** — 默认 `fimath` 对象属性 `Same as MATLAB`（默认）| `Specify Other`

将 Requirements Table 模块的默认 `fimath` 对象属性指定为以下值之一：

- `Same as MATLAB` — 模块使用与当前默认 `fimath` 对象相同的 `fimath` 对象属性。文本框将变暗并显示当前的全局 `fimath` 对象。
- `Specify other` — 通过以下两种方式之一在文本框中指定您自己的 `fimath` 对象：

  - 在文本框中构造 `fimath` 对象。
  - 在 MATLAB 或模型工作区中构造 `fimath` 对象，然后将其变量名输入到文本框中。如果您使用此选项并计划与他人共享您的模型，请在模型工作区中定义该变量。
- 有关 `fimath` 对象的详细信息，请参阅 fimath Object Construction (Fixed-Point Designer)。

#### 提示

- Requirements Table 模块的 `fimath` 对象对该模块的内容而言，其行为类似于 `globalfimath` (Fixed-Point Designer)。模块将此参数中的 `fimath` 对象属性与模块的定点输入信号和整数输入信号相关联，您可以选择将这些信号视为 `fi` 对象。在 Requirements Table 模块中构造 `fi` 对象会引入额外的注意事项。

  - 如果在构造 `fi` 对象时没有 `fimath` 对象与其关联，则 `fi` 构造函数将使用默认 `fimath` 对象设置，而不考虑 **Requirements Table fimath** 中的属性。如果您在 `fi` 对象构造后对其执行操作，则该对象将采用 **Requirements Table fimath** 中的属性。
  - 如果您在 `fi` 构造函数中指定了 `fimath` 对象，则 `fi` 构造函数在量化值时会遵循该 `fimath` 对象。未在 `fi` 构造函数中指定的 `fimath` 设置将使用 **Requirements Table fimath** 中指定的属性。

## 所属库

Requirements Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

### GPU 代码生成 使用 GPU Coder™ 为 NVIDIA® GPU 生成 CUDA® 代码。

实际数据类型或功能支持取决于模块实现。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 为 HDL 实现和综合逻辑提供额外的配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstMultiplierOptimization** | 规范符号数字 (CSD) 或因式分解 CSD 优化。默认值为 `none`。另请参阅 ConstMultiplierOptimization (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分配或寄存器重定时。默认值为 `inherit`。另请参阅 DistributedPipelining (HDL Coder)。 |
| **GuardIndexVariables** | 指定是否将数组索引从条件语句中提升出来。当您启用某些优化（如 RAM 映射、循环流式处理、共享等）时，表达式会被移出数组索引。会为该表达式创建一个临时变量，这可能会导致仿真期间出现索引越界错误。默认值为 `off`。请参阅 GuardIndexVariables (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **InstantiateFunctions** | 为每个函数生成一个 VHDL® `entity` 或 Verilog® `module`。默认值为 `off`。另请参阅 InstantiateFunctions (HDL Coder)。 |
| **LoopOptimization** | 展开、流式处理或不优化循环。默认值为 `none`。另请参阅 LoopOptimization (HDL Coder)。 |
| **MapPersistentVarsToRAM** | 将持久数组映射到 RAM。默认值为 `off`。另请参阅 MapPersistentVarsToRAM (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ResetType** | 抑制复位逻辑生成。默认值为 `default`，即生成复位逻辑。另请参阅 ResetType (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的功能等效资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |

**优化**

此模块参与以下 HDL 优化，以优化速度和面积。

**速度和面积优化**

| 优化 | 描述 |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *分布式流水线*，或称寄存器重定时，是一种速度优化，它移动设计中已有的延迟以减少关键路径，同时保持功能行为。 |
| Resource Sharing (HDL Coder) | *资源共享*是一种面积优化，HDL Coder 在其中识别多个功能等价的资源，并将它们替换为单个资源。 |
| Understand Delay Balancing in HDL Coder (HDL Coder) | 当优化或模块实现选项在模型的关键路径上引入延迟时，*延迟平衡*会检测到在一条路径上引入的新延迟，然后在其他路径上插入匹配的延迟。 |
| Clock-Rate Pipelining (HDL Coder) | *时钟速率流水线*是 HDL Coder 中的一种优化框架，它允许其他速度和面积优化在时钟速率下引入延迟。 |
| Adaptive Pipelining (HDL Coder) | *自适应流水线*优化通过向设计中的模块插入流水线寄存器，创建带有寄存器的模式或模块组合，从而提高可实现的时钟频率并减少 FPGA 板上的面积使用。 |
| Critical Path Estimation (HDL Coder) | 要快速识别设计中可能性最大的关键路径，请使用*关键路径估计*。关键路径估计加速了查找关键路径的迭代过程。要了解在关键路径估计中被表征的模块，请参阅 Characterized Blocks (HDL Coder)。 |

**限制**

当您应用优化时，该模块具有以下限制：

- 具有 **Trigger** 端口的模块不支持 HDL 优化。

### Fixed-Point Conversion 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型或能力支持取决于模块实现。

## 版本历史

**在 R2022a 中引入**

### R2022b：Requirements Table 模块的字符串支持

您现在可以在 Requirements Table 模块中创建和操作字符串数据。字符串数据类型与 MATLAB 和 Simulink 中的字符串兼容。

## 描述

使用输入条件对形式化需求进行建模

Requirements Table 模块对形式化需求进行建模。该模块首先评估 **Precondition** 列中的条件。如果条件满足，该模块会检查其他仿真数据是否满足 **Postcondition** 列中的条件，或执行 **Action** 列中的动作。有关详细信息，请参阅 Use a Requirements Table Block to Create Formal Requirements。

您可以通过在 **Assumptions** 选项卡中定义假设，根据模型的物理限制来约束需求。请参阅 Add Assumptions to Requirements。

只有在您拥有 Requirements Toolbox™ 时，才能配置此模块。
