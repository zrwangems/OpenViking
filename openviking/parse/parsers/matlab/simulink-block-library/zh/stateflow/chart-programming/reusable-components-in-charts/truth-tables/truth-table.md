---
type: simulink-block
title: 'Truth Table'
family: 'stateflow'
product_id: 'stateflow'
product_name: 'Stateflow'
documentation_release: R2025b
official_category: 'Chart Programming / Chart Programming Basics / Stateflow Charts'
documentation_page: 'truthtable'
documentation_source_path: 'ref/truthtable.html'
language: zh-CN
chinese_source: official
---

# Truth Table

## 端口

### 输入

### **Port\_1** — 输入端口 标量 | 向量 | 矩阵

当您使用**符号**窗格在 Stateflow® 真值表中创建输入数据时，Stateflow 会在 Truth Table 模块上创建对应的输入端口。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
### 输出

### **Port\_1** — 输出端口 标量 | 向量 | 矩阵

当您使用**符号**窗格在 Stateflow 真值表中创建输出数据时，Stateflow 会在 Truth Table 模块上创建对应的输出端口。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。从 Simulink® 工具条的**仿真**选项卡上的**准备**库中，选择**属性检查器**。

**注意**

Truth Table 模块也有 Subsystem (Simulink) 模块参数，您可以通过右键点击模块并点击**模块参数(子系统)** 来访问这些参数。但是，不推荐更新这些模块参数。

### **更新方法** — 用于更新或唤醒 Stateflow 真值表的方法 **继承** (默认) | **离散** | **连续**

用于更新或唤醒 Stateflow 真值表的方法，指定为**继承**、**离散**或**连续**。

**继承**
:   来自 Simulink 模型的输入决定真值表在仿真过程中何时唤醒（默认值）。

    如果您为真值表定义输入事件，则Stateflow 真值表由其触发端口上的信号显式触发，该信号源自连接的 Simulink 模块。您可以将此触发输入事件设置为响应 Simulink 信号而发生。Simulink 信号可以是**上升沿**、**下降沿**或**任一沿**（上升和下降），或者是响应**函数调用**。有关详细信息，请参阅通过发送输入事件激活 Stateflow 图。

    如果不定义输入事件，Stateflow 真值表将从 Stateflow 模型隐式继承触发器。这些隐式事件是为真值表提供输入的 Stateflow 信号的离散或连续采样时间。如果您定义了数据输入，真值表将以其中最快的数据输入的速率唤醒。如果没有为真值表定义任何数据输入，真值表将按照其父级子系统的执行行为所定义的方式唤醒。

**离散**
:   Simulink 模型以固定时间间隔生成隐式事件，以您在**采样时间**真值表参数中指定的速率唤醒 Stateflow 真值表。Simulink 模型中的其他模块可以具有不同的采样时间。

**连续**
:   Stateflow 真值表仅在主时间步内更新其状态，尽管它在主时间步和子时间步内都会计算输出和局部连续变量。有关详细信息，请参阅Continuous-Time Modeling in Stateflow。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.TruthTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `ChartUpdate` |
| **值:** | `"INHERITED"` (默认) | `"CONTINUOUS"` | `"DISCRETE"` |

### **采样时间** — Stateflow 真值表在仿真期间唤醒的时间间隔 `-1` (默认) | 标量 | 向量

真值表在仿真期间唤醒的时间间隔，由标量或向量指定。默认时间间隔是 `-1`，这表明 Stateflow 真值表从 Simulink 继承采样时间。

不要在 Subsystem 模块参数中使用**采样时间**参数。请改用属性检查器。

#### 依赖关系

要启用此参数，请将**更新方法**设置为**离散**。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.TruthTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `"-1"` (默认) | string scalar | character vector |
| **数据类型:** | `string` | `char` |

### 高级

### **对整数溢出进行饱和处理** — 数据是否对整数溢出进行饱和处理 `on` (默认) | `off`

真值表中的数据是否对整数溢出进行饱和处理。当清除此参数时，真值表中的数据会在整数溢出时绕回。有关详细信息，请参阅Handle Integer and Enumeration Overflow for Chart Data。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.TruthTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `SaturateOnIntegerOverflow` |
| **值:** | `true` or `1` (默认) | `false` or `0` |
| **数据类型:** | `logical` |

### **支持可变大小数组** — 真值表是否支持可变大小数据 `on` (默认) | `off`

真值表是否支持可变大小数据。有关详细信息，请参阅Declare Variable-Size Data in Stateflow Charts。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.TruthTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `SupportVariableSizing` |
| **值:** | `true` or `1` (默认) | `false` or `0` |
| **数据类型:** | `logical` |

### **将长度为 1 的维度视为固定大小** — 真值表是否将维度长度为 1 的非标量数据视为固定大小 `on` (默认) | `off`

*自 R2023a 起*

真值表是否将维度长度为 1 的非标量数据视为固定大小。当选中此参数时，无论是否启用**可变大小**数据属性，真值表都会将有至少一个长度为 1 的维度的非标量数据视为固定大小。当清除此参数时，真值表会将启用**可变大小**属性的非标量数据视为可变大小。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.TruthTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `TreatDimensionOfLengthOneAsFixedSize` |
| **值:** | `true` or `1` (默认) | `false` or `0` |
| **数据类型:** | `logical` |

### **过定** — 真值表过定时的诊断级别 `"Error"` (默认) | `"Warning"` | `"None"`

真值表过定时的诊断操作级别，指定为 `"Error"`、`"Warning"` 或 `"None"`。有关详细信息，请参阅Correct Overspecified and Underspecified Truth Tables。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.TruthTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `OverSpecDiagnostic` |
| **值:** | `"Error"` (默认) | `"Warning"` | `"None"` |

### 定点属性

### **将这些继承的 Simulink 信号类型视为 fi 对象** — 继承的 Simulink 信号被视为 `fi` 对象 `Fixed-point` (默认) | `Fixed-point & Integer`

继承的 Simulink 信号被视为 Fixed-Point Designer™ `fi` 对象，指定为以下值之一：

- `Fixed-point` - 真值表将所有定点输入视为 `fi` 对象。
- `Fixed-point & Integer` - 真值表将所有定点和整数输入视为 `fi` 对象。

此参数仅适用于使用 MATLAB 作为动作语言的真值表。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.TruthTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `TreatAsFi` |
| **值:** | `"Fixed-point"` (默认) | `"Fixed-point & Integer"` |

### **MATLAB 图 fimath** — 默认 `fimath` 对象属性 `Same as MATLAB` (默认) | `Specify Other`

真值表的默认 `fimath` 对象属性，指定为以下值之一：

- `Same as MATLAB` - 真值表使用与当前默认 `fimath` 对象相同的 `fimath` 对象属性。文本框灰显，并以只读形式显示当前全局 `fimath` 对象。
- `Specify other` - 在文本框中指定您自己的 `fimath` 对象。

有关详细信息，请参阅fimath Object Construction (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.TruthTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `EmlDefaultFimath` |
| **值:** | `"Same as MATLAB Default"` (默认) | `"Other:UserSpecified"` |

## 所属库

Stateflow

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**可调参数**

您可以在 Truth Table 模块中使用可调参数，用于 HDL 代码生成。有关详细信息，请参阅Generate DUT Ports for Tunable Parameters (HDL Coder)。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstMultiplierOptimization** | 正则有符号数 (CSD) 或因子化 CSD 优化。默认值为 **none**。另请参阅ConstMultiplierOptimization (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 要通过移动设计中的现有延迟来放置的输出端寄存器的数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分布或寄存器重定时。默认值为**继承**。另请参阅 DistributedPipelining (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ResetType** | 隐藏重置逻辑生成。默认值为**默认**，会生成重置逻辑。另请参阅 ResetType (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的功能等效的资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |

**优化**

模块参与以下这些 HDL 优化，以优化速度和面积。

**速度和面积优化**

| 优化 | 描述 |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *分布式流水线*或寄存器重定时是一种速度优化，它可以移动设计中的现有延迟，以在缩减关键路径的同时保留功能性行为。 |
| Resource Sharing (HDL Coder) | *资源复用*是一种面积优化，其中 HDL Coder 会识别多个在功能上等效的资源，并用单个资源替换它们。 |
| Understand Delay Balancing in HDL Coder (HDL Coder) | 当优化或模块实现选项在模型中的关键路径中引入延迟时，*延迟平衡*会检测在一条路径中引入的新延迟，然后在其他路径中插入匹配的延迟。 |
| Clock-Rate Pipelining (HDL Coder) | *时钟频率流水线*是 HDL Coder 中的一个优化框架，它允许其他速度优化和面积优化在时钟频率下引入延迟。 |
| Adaptive Pipelining (HDL Coder) | *自适应流水线*优化通过在设计中的模块中插入流水线寄存器来创建包含寄存器的构型或模块组合，从而提高可实现的时钟频率并减少 FPGA 板上的面积使用量。 |
| 关键路径估计 (HDL Coder) | 要快速确定设计中最可能的关键路径，请使用*关键路径估计*。关键路径估计加速了寻找关键路径的迭代过程。要了解在关键路径估计中表征的模块，请参阅Characterized Blocks (HDL Coder)。 |

**限制**

要了解有关限制的信息，请参阅Introduction to Stateflow HDL Code Generation (HDL Coder)。

应用优化时，模块有以下限制：

- 具有 **Trigger** 端口的模块不支持 HDL 优化。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

### R2023a: 指定如何处理维度长度为 1 的非标量数据

使用新参数**将长度为 1 的维度视为固定大小**，您可以指定当至少一个维度的长度为 1 时，真值表如何处理非标量数据。在 R2023a 之前，无论您是否启用**可变大小**数据属性，真值表都会将有至少一维长度为 1 的非标量数据视为固定大小。

## 描述

用条件、决策和动作来表示逻辑决策行为

Truth Table 模块以表格形式表示组合逻辑设计。您可以使用 Truth Table 模块基于一组条件为决策行为进行建模。有关详细信息，请参阅使用真值表对组合逻辑建模。

为了实现控制逻辑，Truth Table 模块使用 MATLAB® 作为动作语言。
