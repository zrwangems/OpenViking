---
type: simulink-block
title: 'State Transition Table'
family: 'stateflow'
product_id: 'stateflow'
product_name: 'Stateflow'
documentation_release: R2025b
official_category: 'Chart Programming / Chart Programming Basics / Stateflow Charts'
documentation_page: 'statetransitiontable'
documentation_source_path: 'ref/statetransitiontable.html'
language: zh-CN
chinese_source: official
---

# State Transition Table

## 端口

### 输入

### **Port\_1** — 输入端口 标量 | 向量 | 矩阵

当您使用**符号**窗格在 Stateflow 状态转移表中创建输入数据时，Stateflow 会在 State Transition Table 模块上创建对应的输入端口。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
### 输出

### **Port\_1** — 输出端口 标量 | 向量 | 矩阵

当您使用**符号**窗格在 Stateflow 状态转移表中创建输出数据时，Stateflow 会在 State Transition Table 模块上创建对应的输出端口。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。从 Simulink® 工具条的**仿真**选项卡上的**准备**库中，选择**属性检查器**。

**注意**

State Transition Table 模块也有 Subsystem (Simulink) 模块参数，您可以通过右键点击模块并点击**模块参数(子系统)** 来访问这些参数。但是，不推荐更新这些模块参数。

### **更新方法** — 用于更新或唤醒 Stateflow 状态转移表的方法 **继承** (默认) | **离散** | **连续**

用于更新或唤醒 Stateflow 状态转移表的方法，指定为**继承**、**离散**或**连续**。

**继承**
:   来自 Simulink 模型的输入决定状态转移表在仿真过程中何时唤醒。

    如果为状态转移表定义输入事件，则连接到触发端口的 Simulink 模块发出的信号会触发状态转移表。Simulink 信号可以是**上升沿**、**下降沿**或**任一沿**（上升和下降），或者是响应**函数调用**。有关详细信息，请参阅通过发送输入事件激活 Stateflow 图。

    如果不定义输入事件，Stateflow 状态转移表将从 Simulink 模型隐式继承触发器。这些隐式事件是为状态转移表提供输入的 Simulink 信号的离散或连续采样时间。如果您定义了数据输入，状态转移表将以其中最快的数据输入的速率唤醒。如果没有为状态转移表定义任何数据输入，状态转移表将按照其父级子系统的执行行为所定义的方式唤醒。

**离散**
:   当 Simulink 模型以您在**采样时间**状态转移表属性中指定的固定时间间隔生成隐式事件时，Stateflow 状态转移表将唤醒。Simulink 模型中的其他模块可以具有不同的采样时间。

**连续**
:   Stateflow 状态转移表仅在主时间步内更新其状态，且在主时间步和子时间步内都会计算输出和局部连续变量。状态转移表可以记录过零，这样，只要状态发生变化，Simulink 模型就可以对 Stateflow 状态转移表进行采样。Stateflow 状态转移表计算局部连续变量的导数。有关详细信息，请参阅Continuous-Time Modeling in Stateflow。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `ChartUpdate` |
| **值:** | `"INHERITED"` (默认) | `"CONTINUOUS"` | `"DISCRETE"` |

### **采样时间** — 仿真期间状态转移表唤醒的时间间隔 `-1` (默认) | 标量 | 向量

默认时间间隔是 `-1`，这表示 Stateflow 状态转移表从 Simulink 继承采样时间。

指定仿真期间状态转移表唤醒的时间间隔。默认值表示状态转移表从 Simulink 继承采样时间。有关指定采样时间的详细信息，请参阅指定采样时间 (Simulink)。

不要在 Subsystem 模块参数中使用**采样时间**参数。请改用属性检查器。

#### 依赖关系

要启用此参数，请将**更新方法**设置为**离散**。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `"-1"` (默认) | string scalar | character vector |
| **数据类型:** | `string` | `char` |

### **创建监控输出** — 是否创建激活状态数据输出 `off` (默认) | `on`

是否为状态转移表创建激活状态数据输出端口。有关详细信息，请参阅Monitor State Activity Through Active State Data。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `HasOutputData` |
| **值:** | `false` or `0` (默认) | `true` or `1` |
| **数据类型:** | `logical` |

### **输出监控模式** — 激活状态输出的监控模式 `Child activity` (默认) | `Leaf state activity`

激活状态输出数据的监控模式。

#### 依赖关系

要启用此参数，请启用**创建监控输出**。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `OutputMonitoringMode` |
| **值:** | `"ChildActivity"` (默认) | `"LeafStateActivity"` |

### **数据名称** — 激活状态数据对象的名称 `State_Transition_TableMode` (默认) | 标量

状态转移表的激活状态数据对象的名称。

#### 依赖关系

要启用此参数，请启用**创建监控输出**。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `OutputPortName` |
| **值:** | `"State_Transition_TableMode"` (默认) | string scalar | character vector |
| **数据类型:** | `string` | `char` |

### **枚举名称** — 激活状态数据对象的枚举数据类型的名称 `State_Transition_TableModeType` (默认) | 标量

状态转移表的激活状态数据对象的名称。

#### 依赖关系

要启用此参数，请启用**创建监控输出**。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `EnumTypeName` |
| **值:** | `"State_Transition_TableModeType"` (默认) | string scalar | character vector |
| **数据类型:** | `string` | `char` |

### **手动定义枚举类型** — 是否手动定义枚举数据类型 `off` (默认) | `on`

是否手动定义激活状态数据输出的枚举数据类型。有关详细信息，请参阅Define State Activity Enumeration Type。

#### 依赖关系

要启用此参数，请启用**创建监控输出**。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `DoNotAutogenerateEnum` |
| **值:** | `false` or `0` (默认) | `true` or `1` |
| **数据类型:** | `logical` |

### 高级

### **初始化时执行(进入)图** — 是否初始化状态配置 `off` (默认) | `on`

是否在时间零处初始化状态转移表的状态配置，而不是在第一个输入事件处初始化。有关详细信息，请参阅初始化时的图执行。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `ExecuteAtInitialization` |
| **值:** | `false` or `0` (默认) | `true` or `1` |
| **数据类型:** | `logical` |

### **对整数溢出进行饱和处理** — 数据是否对整数溢出进行饱和处理 `on` (默认) | `off`

状态转移表中的数据是否对整数溢出进行饱和处理。当清除此参数时，状态转移表中的数据会在整数溢出时绕回。有关详细信息，请参阅Handle Integer and Enumeration Overflow for Chart Data。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `SaturateOnIntegerOverflow` |
| **值:** | `true` or `1` (默认) | `false` or `0` |
| **数据类型:** | `logical` |

### **每次图唤醒时初始化输出** — 是否初始化输出数据 `off` (默认) | `on`

是否在每次状态转移表唤醒时初始化输出数据。

当选中此参数时，状态转移表会在每次唤醒状态转移表时（而不仅仅是在时间 0 处）重置其输出值。每当函数调用、边沿触发器或时钟计时单元触发状态转移表时，状态转移表都会重置输出值。如果为输出数据对象设置初始值，则输出将重置为该值。否则，输出重置为零。选中此参数可以：

- 确保所有输出都在每个状态转移表执行中定义。
- 防止输出锁存，即防止用先前执行中计算的输出值。
- 为所有状态转移表输出提供有意义的初始值。

有关详细信息，请参阅初始值。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `InitializeOutput` |
| **值:** | `false` or `0` (默认) | `true` or `1` |
| **数据类型:** | `logical` |

### **支持可变大小数组** — 状态转移表是否支持可变大小数据 `on` (默认) | `off`

状态转移表是否支持可变大小数据。有关详细信息，请参阅Declare Variable-Size Data in Stateflow Charts。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `SupportVariableSizing` |
| **值:** | `true` or `1` (默认) | `false` or `0` |
| **数据类型:** | `logical` |

### **启用超时间步语义** — 是否启用超时间步语义 `off` (默认) | `on`

是否为状态转移表启用超时间步语义。选择此参数可使状态转移表在每个时间步中进行多次转移，直到达到稳态。当您执行以下操作时，此选项不可用。有关详细信息，请参阅Super Step Semantics。

#### 依赖关系

要启用此参数，请将**更新方法**设置为**离散**。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `EnableNonTerminalStates` |
| **值:** | `false` or `0` (默认) | `true` or `1` |
| **数据类型:** | `logical` |

### **一个超时间步中的最大迭代次数** — 最大转移次数 `1000` (默认) | 正整数

在一个超时间步中可以完成的最大转移次数。有关详细信息，请参阅Super Step Semantics。

#### 依赖关系

要启用此参数，请启用**启用超时间步语义**。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `NonTerminalMaxCounts` |
| **值:** | `1000` (默认) | positive integer |
| **数据类型:** | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` |

### **在过多迭代后** — 超时间步超出最大转移次数时的动作 `Proceed` (默认) | `Throw Error`

如果超时间步超出在一个超时间步中的最大转移次数，Stateflow 要执行的动作。有关详细信息，请参阅Super Step Semantics。

#### 依赖关系

要启用此参数，请启用**启用超时间步语义**。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `NonTerminalUnstableBehavior` |
| **值:** | `"Proceed"` (默认) | `"Throw Error"` |

### **将长度为 1 的维度视为固定大小** — 状态转移表是否将维度长度为 1 的非标量数据视为固定大小 `on` (默认) | `off`

*自 R2023a 起*

状态转移表是否将维度长度为 1 的非标量数据视为固定大小。当选中此参数时，无论是否启用**可变大小**数据属性，状态转移表都会将有至少一个长度为 1 的维度的非标量数据视为固定大小。当清除此参数时，状态转移表会将启用**可变大小**属性的非标量数据视为可变大小。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `TreatDimensionOfLengthOneAsFixedSize` |
| **值:** | `true` or `1` (默认) | `false` or `0` |
| **数据类型:** | `logical` |

### **动作语言** — 动作语言 `MATLAB` (默认) | `C`

对状态转移表进行编程时所用的动作语言，指定为 `MATLAB` 或 `C`。有关详细信息，请参阅使用 MATLAB 和 C 作为动作语言语法时的差异。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `ActionLanguage` |
| **值:** | `"MATLAB"` (默认) | `"C"` |

### **状态机类型** — 状态机语义 `Classic` (默认) | `Mealy` | `Moore`

由状态转移表实现的状态机语义，指定为 `Classic`、`Mealy` 或 `Moore`。有关详细信息，请参阅米利和摩尔状态机概述。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `StateMachineType` |
| **值:** | `"Classic"` (默认) | `"Mealy"` | `"Moore"` |

### 定点属性

### **将这些继承的 Simulink 信号类型视为 fi 对象** — 继承的 Simulink 信号被视为 `fi` 对象 `Fixed-point` (默认) | `Fixed-point & Integer`

继承的 Simulink 信号被视为 Fixed-Point Designer™ `fi` 对象，指定为以下值之一：

- `Fixed-point` - 状态转移表将所有定点输入视为 `fi` 对象。
- `Fixed-point & Integer` - 状态转移表将所有定点和整数输入视为 `fi` 对象。

此参数仅适用于使用 MATLAB 作为动作语言的状态转移表。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用圆点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `TreatAsFi` |
| **值:** | `"Fixed-point"` (默认) | `"Fixed-point & Integer"` |

### **MATLAB 函数 fimath** — 默认 `fimath` 属性 `Same as MATLAB` (默认) | `Specify Other`

状态转移表的默认 `fimath` 对象属性，指定为以下值之一：

- `Same as MATLAB` - 状态转移表使用与当前默认 `fimath` 对象相同的 `fimath` 对象属性。文本框灰显，并以只读形式显示当前全局 `fimath` 对象。
- `Specify other` - 在文本框中指定您自己的 `fimath` 对象。

有关详细信息，请参阅fimath Object Construction (Fixed-Point Designer)。

#### 依赖关系

要启用此参数，请将**动作语言**设置为 **MATLAB**。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用圆点表示法更改对象属性。

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

您可以在 State Transition Table 模块中使用可调参数，用于 HDL 代码生成。有关详细信息，请参阅Generate DUT Ports for Tunable Parameters (HDL Coder)。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**激活状态输出**

要在 HDL 代码中生成显示激活状态的输出端口，请在图的属性窗口中选择**创建监控输出**。输出是枚举数据类型。请参阅通过合并激活状态输出来简化 Stateflow 图。

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

- 将**状态机类型**属性设置为**摩尔**的 State Transition Table 模块不支持 HDL 优化。
- 具有 **Trigger** 端口的模块不支持 HDL 优化。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2012b 中推出**

### R2023b: 转换为图

要将状态转移表转换为 Stateflow 图，请使用对象函数 `convertToChart`。

### R2023a: 添加并行状态

要将一个状态转移表状态的分解设置为并行，请选择该状态。在**建模**选项卡中，选择**设置状态分解** > **并行(AND)**。

### R2023a: 指定如何处理维度长度为 1 的非标量数据

使用新属性 **将长度为 1 的维度视为固定大小**，您可以指定当至少一个维度的长度为 1 时，状态转移表如何处理非标量数据。在 R2023a 之前，无论您是否启用**可变大小**数据属性，状态转移表都会将有至少一个长度为 1 的维度的非标量数据视为固定大小。

### R2022b: 导出状态转移表的内容

通过调用对象函数 `exportAsStruct`，将状态转移表的内容导出为结构体数组。

### R2022b: 新键盘快捷方式

将转移列追加到状态转移表的键盘快捷方式现在是 **Ctrl+K**。在以前的版本中，键盘快捷方式是 **Ctrl+M**。

## 描述

以表格形式表示模态逻辑

State Transition Table 模块以表格形式表示有限状态机。除了在 Stateflow® 图中绘制状态和转移这种方式，您还可以使用状态转移表，以简洁、紧凑的格式对状态机进行建模，而且只需对图对象进行极少的维护。有关详细信息，请参阅使用状态转移表对有限状态机建模。

为了实现控制逻辑，State Transition Table 模块可以使用 MATLAB® 或 C 语言作为动作语言。有关详细信息，请参阅使用 MATLAB 和 C 作为动作语言语法时的差异。
