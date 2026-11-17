---
type: simulink-block
title: 'Truth Table'
family: 'stateflow'
product_id: 'stateflow'
product_name: 'Stateflow'
documentation_release: R2025b
official_category: ''
documentation_page: 'truthtable'
documentation_source_path: 'ref/truthtable.html'
language: zh-CN
chinese_source: worker-translation
---

# Truth Table

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入端口 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus | string
- name: Port_1
  summary: 输出端口 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus | string
```

### 输入

### **Port\_1** — 输入端口 标量 | 向量 | 矩阵

当您使用 **Symbols** 窗格在 Stateflow® 真值表中创建输入数据时，Stateflow 会在 Truth Table 模块上创建对应的输入端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
### 输出

### **Port\_1** — 输出端口 标量 | 向量 | 矩阵

当您使用 **Symbols** 窗格在 Stateflow 真值表中创建输出数据时，Stateflow 会在 Truth Table 模块上创建对应的输出端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
## 参数
```yaml
parameters:
- name: Update method
  summary: 更新或唤醒 Stateflow 真值表的方法 Inherited（默认）| Discrete | Continuous
  group: ''
  block_parameter: ChartUpdate
  values: '"INHERITED"（默认）| "CONTINUOUS" | "DISCRETE"'
- name: Sample time
  summary: Stateflow 真值表在仿真期间唤醒的时间间隔 -1（默认）| 标量 | 向量
  group: ''
  block_parameter: SampleTime
  values: '"-1"（默认） | 字符串标量 | 字符向量'
- name: 整型溢出时饱和
  summary: 数据在整型溢出时是否饱和 on（默认） | off
  group: 高级
  block_parameter: SaturateOnIntegerOverflow
  values: true 或 1（默认） | false 或 0
- name: 支持可变大小数组
  summary: 真值表是否支持可变大小数据 on（默认） | off
  group: 高级
  block_parameter: SupportVariableSizing
  values: true 或 1（默认） | false 或 0
- name: 将长度为 1 的维度视为固定大小
  summary: 真值表是否将长度为 1 的维度的非标量数据视为固定大小 on（默认） | off
  group: 高级
  block_parameter: TreatDimensionOfLengthOneAsFixedSize
  values: true 或 1（默认） | false 或 0
- name: 过度指定
  summary: 真值表过度指定时的诊断级别 "Error"（默认） | "Warning" | "None"
  group: 高级
  block_parameter: OverSpecDiagnostic
  values: '"Error"（默认） | "Warning" | "None"'
- name: 将这些继承的 Simulink 信号类型视为 fi 对象
  summary: 要视为 fi 对象的继承 Simulink 信号 Fixed-point（默认） | Fixed-point & Integer
  group: 定点属性
  block_parameter: TreatAsFi
  values: '"Fixed-point"（默认） | "Fixed-point & Integer"'
- name: MATLAB Chart fimath
  summary: 默认 fimath 对象属性 Same as MATLAB（默认） | Specify Other
  group: 定点属性
  block_parameter: EmlDefaultFimath
  values: '"Same as MATLAB Default"（默认） | "Other:UserSpecified"'
```

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

**注意**

Truth Table 模块还具有 Subsystem (Simulink) 模块参数，您可以通过右键单击该模块并单击 **Block Parameters (Subsystem)** 来访问这些参数。但是，不建议更新这些模块参数。

### **Update method** — 更新或唤醒 Stateflow 真值表的方法 `Inherited`（默认）| `Discrete` | `Continuous`

更新或唤醒 Stateflow 真值表的方法，指定为 `Inherited`、`Discrete` 或 `Continuous`。

`Inherited`
:   来自 Simulink 模型的输入决定真值表在仿真期间何时唤醒（默认）。

    如果您为真值表定义输入事件，则 Stateflow 真值表由来自所连接 Simulink 模块的触发端口上的信号显式触发。您可以将此触发输入事件设置为响应 Simulink 信号而发生。Simulink 信号可以是 `Rising`、`Falling` 或 `Either`（上升沿和下降沿），也可以响应 `Function Call`。有关详细信息，请参阅 Activate a Stateflow Chart by Sending Input Events。

    如果您不定义输入事件，则 Stateflow 真值表隐式继承来自 Stateflow 模型的触发。这些隐式事件是向真值表提供输入的 Stateflow 信号的离散或连续采样时间。如果您定义数据输入，则真值表以最快数据输入的速率唤醒。如果您不为真值表定义任何数据输入，则真值表按其父级子系统的执行行为所定义的方式唤醒。

`Discrete`
:   Simulink 模型以固定时间间隔生成隐式事件，以您在 **Sample Time** 真值表参数中指定的速率唤醒 Stateflow 真值表。Simulink 模型中的其他模块可以具有不同的采样时间。

`Continuous`
:   Stateflow 真值表仅在主时间步期间更新其状态，尽管它会在主时间步和次时间步期间计算输出和局部连续变量。有关详细信息，请参阅 Continuous-Time Modeling in Stateflow。

#### 编程使用

要以编程方式设置模块参数值，请访问模块的 `Stateflow.TruthTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **Parameter:** | `ChartUpdate` |
| **值**：| `"INHERITED"`（默认）| `"CONTINUOUS"` | `"DISCRETE"` |

### **Sample time** — Stateflow 真值表在仿真期间唤醒的时间间隔 `-1`（默认）| 标量 | 向量

真值表在仿真期间唤醒的时间间隔，指定为标量或向量。默认时间间隔为 `-1`，表示 Stateflow 真值表从 Simulink 继承采样时间。

不要使用 Subsystem 模块参数中的 **Sample Time** 参数。而应使用属性检查器。

#### 依赖关系

要启用此参数，请将 **更新方法** 设置为
`Discrete`。

#### 程序化使用

要以编程方式设置模块参数值，请访问模块的 `Stateflow.TruthTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认） | 字符串标量 | 字符向量 |
| **数据类型：** | `string` | `char` |

### 高级

### **整型溢出时饱和** — 数据在整型溢出时是否饱和 `on`（默认） | `off`

真值表中的数据在整型溢出时是否饱和。当您清除此参数时，真值表中的数据在整型溢出时回绕。
有关详细信息，请参阅 Handle Integer and Enumeration Overflow for Chart Data。

#### 程序化使用

要以编程方式设置模块参数值，请访问模块的
`Stateflow.TruthTableChart` 对象，并使用点表示法
更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `true` 或 `1`（默认） | `false` 或 `0` |
| **数据类型：** | `logical` |

### **支持可变大小数组** — 真值表是否支持可变大小数据 `on`（默认） | `off`

真值表是否支持可变大小数据。有关更多
信息，请参阅 Declare Variable-Size Data in Stateflow Charts。

#### 程序化使用

要以编程方式设置模块参数值，请访问模块的
`Stateflow.TruthTableChart` 对象，并使用点表示法
更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `SupportVariableSizing` |
| **值：** | `true` 或 `1`（默认） | `false` 或 `0` |
| **数据类型：** | `logical` |

### **将长度为 1 的维度视为固定大小** — 真值表是否将长度为 1 的维度的非标量数据视为固定大小 `on`（默认） | `off`

*自 R2023a 起*

真值表是否将长度为 1 的维度的非标量数据视为固定大小。当您选中此参数时，真值表将至少有一个长度为 1 的维度的非标量数据视为固定大小，无论您是否启用 **可变大小** 数据属性。当您清除此参数时，真值表将启用了 **可变大小** 属性的非标量数据视为可变大小。

#### 程序化使用

要以编程方式设置模块参数值，请访问模块的
`Stateflow.TruthTableChart` 对象，并使用点表示法
更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `TreatDimensionOfLengthOneAsFixedSize` |
| **值：** | `true` 或 `1`（默认） | `false` 或 `0` |
| **数据类型：** | `logical` |

### **过度指定** — 真值表过度指定时的诊断级别 `"Error"`（默认） | `"Warning"` | `"None"`

真值表过度指定时的诊断操作级别，指定为 `"Error"`、`"Warning"`
或 `"None"`。有关更多信息，请参阅 Correct Overspecified and Underspecified Truth Tables。

#### 程序化使用

要以编程方式设置模块参数值，请访问模块的
`Stateflow.TruthTableChart` 对象，并使用点表示法
更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `OverSpecDiagnostic` |
| **值：** | `"Error"`（默认） | `"Warning"` | `"None"` |

### 定点属性

### **将这些继承的 Simulink 信号类型视为 fi 对象** — 要视为 `fi` 对象的继承 Simulink 信号 `Fixed-point`（默认） | `Fixed-point & Integer`

要视为 Fixed-Point Designer™
`fi` 对象的继承 Simulink 信号，指定为以下值之一：

- `Fixed-point` — 真值表将所有定点输入视为 `fi`
  对象。
- `Fixed-point & Integer` — 真值表将所有定点和整型输入视为
  `fi` 对象。

此参数仅适用于使用
MATLAB 作为动作语言的真值表。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.TruthTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `TreatAsFi` |
| **值：** | `"Fixed-point"`（默认） | `"Fixed-point & Integer"` |

### **MATLAB Chart fimath** — 默认 `fimath` 对象属性 `Same as MATLAB`（默认） | `Specify Other`

真值表的默认 `fimath` 对象属性，指定为以下值之一：

- `Same as MATLAB` — 真值表使用与当前默认 `fimath` 对象相同的 `fimath` 对象属性。文本框变暗，并以只读形式显示当前全局 `fimath` 对象。
- `Specify other` — 在文本框中指定您自己的 `fimath` 对象。

有关详细信息，请参阅 fimath Object Construction (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请访问模块的 `Stateflow.TruthTableChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `EmlDefaultFimath` |
| **值：** | `"Same as MATLAB Default"`（默认） | `"Other:UserSpecified"` |
## 所属库

Stateflow

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**可调参数**

您可以在用于 HDL 代码生成的 Truth Table 模块中使用可调参数。有关详细信息，请参阅 Generate DUT Ports for Tunable Parameters (HDL Coder)。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstMultiplierOptimization** | 规范符号数字 (CSD) 或因式分解 CSD 优化。默认值为 `none`。另请参阅 ConstMultiplierOptimization (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分布，或寄存器重定时。默认值为 `inherit`。另请参阅 DistributedPipelining (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ResetType** | 抑制复位逻辑生成。默认值为 `default`，即生成复位逻辑。另请参阅 ResetType (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的等效功能资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |

**优化**

此模块参与以下 HDL 优化，以优化速度和面积。

**速度和面积优化**

| 优化 | 描述 |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *分布式流水线*，或寄存器重定时，是一种速度优化，它移动设计中的现有延迟以减少关键路径，同时保持功能行为。 |
| Resource Sharing (HDL Coder) | *资源共享*是一种面积优化，HDL Coder 在其中识别多个功能等效的资源，并将其替换为单个资源。 |
| Understand Delay Balancing in HDL Coder (HDL Coder) | 当优化或模块实现选项在模型的关键路径上引入延迟时，*延迟平衡*会检测到在一条路径上引入的新延迟，然后在其他路径上插入匹配的延迟。 |
| Clock-Rate Pipelining (HDL Coder) | *时钟速率流水线*是 HDL Coder 中的一种优化框架，允许其他速度和面积优化在时钟速率下引入延迟。 |
| Adaptive Pipelining (HDL Coder) | *自适应流水线*优化创建带有寄存器的模块模式或组合，通过向设计中的模块插入流水线寄存器，可以提高可实现的时钟频率并减少 FPGA 板上的面积使用。 |
| Critical Path Estimation (HDL Coder) | 要快速识别设计中可能的关键路径，请使用*关键路径估计*。关键路径估计加快了查找关键路径的迭代过程。要了解在关键路径估计中表征的模块，请参阅 Characterized Blocks (HDL Coder)。 |

**限制**

要了解相关限制，请参阅 Introduction to Stateflow HDL Code Generation (HDL Coder)。

当您应用优化时，此模块具有以下限制：

- 对于具有 **Trigger** 端口的模块，不支持 HDL 优化。

### 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### Fixed-Point Conversion 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2023a: 指定如何处理长度为 1 的非标量数据

使用新参数 **Treat dimensions of length 1 as fixed size**，您可以指定当至少一个维度的长度为 1 时，真值表如何处理非标量数据。在 R2023a 之前，无论是否启用 **Variable size** 数据属性，真值表都会将至少一个维度长度为 1 的非标量数据视为固定大小。

## 描述

使用条件、决策和动作表示逻辑决策行为

Truth Table 模块以表格格式表示组合逻辑设计。您可以使用真值表模块基于一组条件来建模决策行为。有关详细信息，请参阅 Use Truth Tables to Model Combinatorial Logic。

为实现控制逻辑，Truth Table 模块使用 MATLAB® 作为动作语言。
