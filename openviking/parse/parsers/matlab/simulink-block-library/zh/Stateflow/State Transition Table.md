---
type: simulink-block
title: 'State Transition Table'
family: 'stateflow'
product_id: 'stateflow'
product_name: 'Stateflow'
documentation_release: R2025b
official_category: ''
documentation_page: 'statetransitiontable'
documentation_source_path: 'ref/statetransitiontable.html'
language: zh-CN
chinese_source: worker-translation
---

# State Transition Table

## 端口

### 输入

### **Port\_1** — 输入端口 标量 | 向量 | 矩阵

当您使用 **Symbols** 窗格在 Stateflow 状态转移表中创建输入数据时，Stateflow 会在 State Transition Table 模块上创建对应的输入端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
### 输出

### **Port\_1** — 输出端口 标量 | 向量 | 矩阵

当您使用 **Symbols** 窗格在 Stateflow 状态转移表中创建输出数据时，Stateflow 会在 State Transition Table 模块上创建对应的输出端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

**注意**

State Transition Table 模块还具有 Subsystem (Simulink) 模块参数，您可以通过右键单击模块并单击 **Block Parameters (Subsystem)** 来访问这些参数。但是，不建议更新这些模块参数。

### **Update method** — 更新或唤醒 Stateflow 状态转移表的方法 `Inherited`（默认）| `Discrete` | `Continuous`

用于更新或唤醒 Stateflow 状态转移表的方法，指定为 `Inherited`、`Discrete` 或 `Continuous`。

`Inherited`
:   来自 Simulink 模型的输入决定状态转移表在仿真期间何时唤醒。

    如果您为状态转移表定义了输入事件，则来自连接到触发端口的 Simulink 模块的信号会触发状态转移表。Simulink 信号可以是 `Rising`、`Falling` 或 `Either`（上升沿和下降沿），或者响应 `Function Call`。有关详细信息，请参阅 Activate a Stateflow Chart by Sending Input Events。

    如果您未定义输入事件，Stateflow 状态转移表会隐式继承来自 Simulink 模型的触发。这些隐式事件是为状态转移表提供输入的 Simulink 信号的离散或连续采样时间。如果您定义了数据输入，状态转移表会以最快数据输入的速率唤醒。如果您未为状态转移表定义任何数据输入，则状态转移表按其父级子系统的执行行为所定义的方式唤醒。

`Discrete`
:   State Transition Table 在 Simulink 模型以您在 **Sample Time** 状态转移表属性中指定的固定时间间隔生成隐式事件时唤醒。Simulink 模型中的其他模块可以具有不同的采样时间。

`Continuous`
:   Stateflow 状态转移表仅在主时间步期间更新其状态，并在主时间步和次时间步期间计算输出和局部连续变量。状态转移表可以注册过零点，这允许 Simulink 模型在状态变化发生时对 Stateflow 状态转移表进行采样。Stateflow 状态转移表计算局部连续变量的导数。有关详细信息，请参阅 Continuous-Time Modeling in Stateflow。

#### 编程使用

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **Parameter:** | `ChartUpdate` |
| **值**：| `"INHERITED"`（默认）| `"CONTINUOUS"` | `"DISCRETE"` |

### **Sample time** — 状态转移表在仿真期间唤醒的时间间隔 `-1`（默认）| 标量 | 向量

默认时间间隔为 `-1`，表示 Stateflow 状态转移表从 Simulink 继承采样时间。

指定状态转移表在仿真期间唤醒的时间间隔。默认值表示状态转移表从 Simulink 继承采样时间。有关指定采样时间的详细信息，请参阅 Specify Sample Time (Simulink)。

不要使用 Subsystem 模块参数中的 **Sample Time** 参数。请改用 Property Inspector。

#### 依赖关系

要启用此参数，请将 **Update method** 设置为 `Discrete`。

#### 编程使用

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **值**：| `"-1"`（默认）| 字符串标量 | 字符向量 |
| **Data Types:** | `string` | `char` |

### **Create output for monitoring** — 是否创建活动状态数据输出 `off`（默认）| `on`

是否为状态转移表创建活动状态数据输出端口。有关详细信息，请参阅 Monitor State Activity Through Active State Data。

#### 编程使用

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **Parameter:** | `HasOutputData` |
| **值**：| `false` 或 `0`（默认）| `true` 或 `1` |
| **Data Types:** | `logical` |

### **Output monitoring mode** — 活动状态输出的监控模式 `Child activity`（默认）| `Leaf state activity`

活动状态输出数据的监控模式。

#### 依赖关系

要启用此参数，请启用 **Create output for monitoring**。

#### 编程使用

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **Parameter:** | `OutputMonitoringMode` |
| **值**：| `"ChildActivity"`（默认）| `"LeafStateActivity"` |

### **Data name** — 活动状态数据对象的名称 `State_Transition_TableMode`（默认）| 标量

状态转移表的活动状态数据对象的名称。

#### 依赖关系

要启用此参数，请启用 **Create output for monitoring**。

#### 编程使用

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **Parameter:** | `OutputPortName` |
| **值**：| `"State_Transition_TableMode"`（默认）| 字符串标量 | 字符向量 |
| **Data Types:** | `string` | `char` |

### **Enum name** — 活动状态数据对象的枚举数据类型名称 `State_Transition_TableModeType`（默认）| 标量

状态转移表的活动状态数据对象的名称。

#### 依赖关系

要启用此参数，请启用 **Create output for monitoring**。

#### 编程使用

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **Parameter:** | `EnumTypeName` |
| **值**：| `"State_Transition_TableModeType"`（默认）| 字符串标量 | 字符向量 |
| **Data Types:** | `string` | `char` |

### **Define enumerated type manually** — 是否手动定义枚举数据类型 `off`（默认）| `on`

是否手动为活动状态数据输出定义枚举数据类型。有关详细信息，请参阅 Define State Activity Enumeration Type。

#### 依赖关系

要启用此参数，请启用 **Create output for monitoring**。

#### 程序化使用

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `DoNotAutogenerateEnum` |
| **值：** | `false` 或 `0`（默认） | `true` 或 `1` |
| **数据类型：** | `logical` |

### 高级

### **在初始化时执行（进入）图表** — 是否初始化状态配置 `off`（默认） | `on`

是否在零时刻而不是在第一个输入事件时初始化状态转移表的状态配置。有关详细信息，请参阅 Execution of a Chart at Initialization。

#### 程序化使用

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `ExecuteAtInitialization` |
| **值：** | `false` 或 `0`（默认） | `true` 或 `1` |
| **数据类型：** | `logical` |

### **整数溢出时饱和** — 数据在整数溢出时是否饱和 `on`（默认） | `off`

状态转移表中的数据在整数溢出时是否饱和。当您清除此参数时，状态转移表中的数据在整数溢出时回绕。有关详细信息，请参阅 Handle Integer and Enumeration Overflow for Chart Data。

#### 程序化使用

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `true` 或 `1`（默认） | `false` 或 `0` |
| **数据类型：** | `logical` |

### **每次图表唤醒时初始化输出** — 是否初始化输出数据 `off`（默认） | `on`

是否在每次状态转移表唤醒时初始化输出数据。

当您选择此参数时，状态转移表会在每次状态转移表唤醒时重置其输出值，而不仅仅是在时刻 0。每当函数调用、边沿触发或时钟节拍触发状态转移表时，状态转移表都会重置输出值。如果您为输出数据对象设置了初始值，则输出将重置为该值。否则，输出将重置为零。选择此参数以：

- 确保在每次状态转移表执行时所有输出都已定义。
- 防止输出锁存，即防止先前执行中计算的输出值。
- 为所有状态转移表输出提供有意义的初始值。

有关详细信息，请参阅 Initial value。

#### 程序化使用

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `InitializeOutput` |
| **值：** | `false` 或 `0`（默认） | `true` 或 `1` |
| **数据类型：** | `logical` |

### **支持可变大小数组** — 状态转移表是否支持可变大小数据 `on`（默认） | `off`

状态转移表是否支持可变大小数据。有关详细信息，请参阅 Declare Variable-Size Data in Stateflow Charts。

#### 程序化使用

要以编程方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `SupportVariableSizing` |
| **值：** | `true` 或 `1`（默认） | `false` 或 `0` |
| **数据类型：** | `logical` |

### **Enable super step semantics** — 是否启用超级步语义 `off`（默认）| `on`

是否为状态转移表启用超级步语义。
选择此参数可使状态转移表在每个时间步中执行多次转移，直到达到稳定状态。
当您……时，此选项不可用。有关详细信息，请参阅 Super Step Semantics。

#### 依赖关系

要启用此参数，请将 **Update method** 设置为 `Discrete`。

#### 程序化使用

要以程序化方式设置模块参数值，请访问模块的
`Stateflow.StateTransitionTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `EnableNonTerminalStates` |
| **值：** | `false` 或 `0`（默认）| `true` 或 `1` |
| **数据类型：** | `logical` |

### **Max iterations in a superstep** — 最大转移次数 `1000`（默认）| 正整数

在一个超级步中可以完成的最大转移次数。有关详细信息，请参阅 Super Step Semantics。

#### 依赖关系

要启用此参数，请启用 **Enable super step semantics**。

#### 程序化使用

要以程序化方式设置模块参数值，请访问模块的
`Stateflow.StateTransitionTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `NonTerminalMaxCounts` |
| **值：** | `1000`（默认）| 正整数 |
| **数据类型：** | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` |

### **After too many iterations** — 超级步超过最大转移次数时的操作 `Proceed`（默认）| `Throw Error`

当一个超级步中的转移次数超过最大转移次数时，Stateflow 要执行的操作。有关详细信息，请参阅 Super Step Semantics。

#### 依赖关系

要启用此参数，请启用 **Enable super step semantics**。

#### 程序化使用

要以程序化方式设置模块参数值，请访问模块的
`Stateflow.StateTransitionTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `NonTerminalUnstableBehavior` |
| **值：** | `"Proceed"`（默认）| `"Throw Error"` |

### **Treat dimensions of length 1 as fixed size** — 状态转移表是否将长度为 1 的维度上的非标量数据视为固定大小 `on`（默认）| `off`

*自 R2023a 起*

状态转移表是否将长度为 1 的维度上的非标量数据视为固定大小。当您选择此参数时，
状态转移表将至少有一个长度为 1 的维度的非标量数据视为固定大小，
无论您是否启用 **Variable size** 数据属性。当您清除此参数时，
状态转移表将启用了 **Variable size** 属性的非标量数据视为可变大小。

#### 程序化使用

要以程序化方式设置模块参数值，请访问模块的
`Stateflow.StateTransitionTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `TreatDimensionOfLengthOneAsFixedSize` |
| **值：** | `true` 或 `1`（默认）| `false` 或 `0` |
| **数据类型：** | `logical` |

### **Action language** — 动作语言 `MATLAB`（默认）| `C`

用于编写状态转移表的动作语言，指定为 `MATLAB` 或 `C`。有关详细
信息，请参阅 Differences Between MATLAB and C as Action Language Syntax。

#### 程序化使用

要以程序化方式设置模块参数值，请访问模块的
`Stateflow.StateTransitionTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `ActionLanguage` |
| **值：** | `"MATLAB"`（默认）| `"C"` |

### **状态机类型** — 状态机语义 `Classic`（默认）| `Mealy` | `Moore`

状态转移表所实现的状态机语义，指定为 `Classic`、`Mealy` 或 `Moore`。有关详细信息，请参阅 Overview of Mealy and Moore Machines。

#### 程序化使用

要以程序化方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `StateMachineType` |
| **值：** | `"Classic"`（默认）| `"Mealy"` | `"Moore"` |

### 定点属性

### **将这些继承的 Simulink 信号类型视为 fi 对象** — 要视为 `fi` 对象的继承 Simulink 信号 `Fixed-point`（默认）| `Fixed-point & Integer`

要视为 Fixed-Point Designer™ `fi` 对象的继承 Simulink 信号，指定为以下值之一：

- `Fixed-point` — 状态转移表将所有定点输入视为 `fi` 对象。
- `Fixed-point & Integer` — 状态转移表将所有定点和整数输入视为 `fi` 对象。

此参数仅适用于使用 MATLAB 作为动作语言的状态转移表。

#### 程序化使用

要以程序化方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `TreatAsFi` |
| **值：** | `"Fixed-point"`（默认）| `"Fixed-point & Integer"` |

### **MATLAB Function fimath** — 默认 `fimath` 属性 `Same as MATLAB`（默认）| `Specify Other`

状态转移表的默认 `fimath` 对象属性，指定为以下值之一：

- `Same as MATLAB` — 状态转移表使用与当前默认 `fimath` 对象相同的 `fimath` 对象属性。文本框将变暗，并以只读形式显示当前全局 `fimath` 对象。
- `Specify other` — 在文本框中指定您自己的 `fimath` 对象。

有关详细信息，请参阅 fimath Object Construction (Fixed-Point Designer)。

#### 依赖关系

要启用此参数，请将 **Action language** 设置为 `MATLAB`。

#### 程序化使用

要以程序化方式设置模块参数值，请访问模块的 `Stateflow.StateTransitionTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `EmlDefaultFimath` |
| **值：** | `"Same as MATLAB Default"`（默认）| `"Other:UserSpecified"` |

## 所属库

Stateflow

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供额外的配置选项，这些选项会影响 HDL 实现和综合逻辑。

**可调参数**

您可以在用于 HDL 代码生成的状态转移表中使用可调参数。有关详细信息，请参阅 Generate DUT Ports for Tunable Parameters (HDL Coder)。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**活动状态输出**

要在 HDL 代码中生成显示活动状态的输出端口，请在图表的属性窗口中选择 **Create output for monitoring**。该输出为枚举数据类型。请参阅 Simplify Stateflow Charts by Incorporating Active State Output。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstMultiplierOptimization** | 规范符号数字（CSD）或因式分解 CSD 优化。默认值为 `none`。另请参阅 ConstMultiplierOptimization (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分布，或寄存器重定时。默认值为 `inherit`。另请参阅 DistributedPipelining (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ResetType** | 抑制复位逻辑生成。默认值为 `default`，即生成复位逻辑。另请参阅 ResetType (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的函数等价资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |

**优化**

该模块参与以下 HDL 优化，以优化速度和面积。

**速度和面积优化**

| 优化 | 描述 |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *分布式流水线*，或寄存器重定时，是一种速度优化，它移动设计中的现有延迟，以缩短关键路径，同时保持功能行为。 |
| Resource Sharing (HDL Coder) | *资源共享*是一种面积优化，其中 HDL Coder 识别多个函数等价资源，并将其替换为单个资源。 |
| Understand Delay Balancing in HDL Coder (HDL Coder) | 当优化或模块实现选项在模型中的关键路径上引入延迟时，*延迟平衡*会检测到一条路径上新延迟的引入，然后在其他路径上插入匹配的延迟。 |
| Clock-Rate Pipelining (HDL Coder) | *时钟速率流水线*是 HDL Coder 中的一种优化框架，允许其他速度和面积优化在时钟速率下引入延迟。 |
| Adaptive Pipelining (HDL Coder) | *自适应流水线*优化会创建带有寄存器的模式或模块组合，通过向设计中的模块插入流水线寄存器，可以提高可实现的时钟频率并减少 FPGA 板上的面积使用。 |
| Critical Path Estimation (HDL Coder) | 要快速识别设计中可能最关键路径，请使用*关键路径估计*。关键路径估计可加速查找关键路径的迭代过程。要了解在关键路径估计中表征的模块，请参阅 Characterized Blocks (HDL Coder)。 |

**限制**

要了解限制，请参阅 Introduction to Stateflow HDL Code Generation (HDL Coder)。

应用优化后，该模块具有以下限制：

- **State Machine Type** 属性设置为 `Moore` 的 State Transition Table 模块不支持 HDL 优化。
- 具有 **Trigger** 端口的模块不支持 HDL 优化。

### PLC Code Generation 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### Fixed-Point Conversion 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2012b 中引入**

### R2023b：转换为 chart

要将状态转移表转换为 Stateflow chart，请使用对象函数 `convertToChart`。

### R2023a：添加并行状态

要将状态转移表状态的分解设置为并行，请选择该状态。在 **Modeling** 选项卡中，选择 **Set State Decomposition** > **Parallel (AND)**。

### R2023a：指定如何处理维度长度为 1 的非标量数据

通过新属性 **Treat dimensions of length 1 as fixed size**，您可以指定当至少一个维度的长度为 1 时，状态转移表如何处理非标量数据。在 R2023a 之前，无论是否启用 **Variable size** 数据属性，状态转移表都会将至少一个维度长度为 1 的非标量数据视为固定大小。

### R2022b：导出状态转移表的内容

通过调用对象函数 `exportAsStruct`，将状态转移表的内容导出为结构体数组。

### R2022b：新的键盘快捷键

向状态转移表追加转移列的键盘快捷键现在是 **Ctrl+K**。在之前的版本中，该快捷键是 **Ctrl+M**。

## 描述

以表格格式表示模态逻辑

State Transition Table 模块以表格格式表示有限状态机。您可以使用状态转移表以简洁、紧凑的格式对状态机建模，而无需在 Stateflow® chart 中绘制状态和转移，并且只需对图形对象进行最少的维护。有关详细信息，请参阅 Model Finite State Machines Using State Transition Tables。

为实现控制逻辑，State Transition Table 模块可以使用 MATLAB® 或 C 作为动作语言。有关详细信息，请参阅 Differences Between MATLAB and C as Action Language Syntax。
