---
type: simulink-block
title: 'Unit Delay'
family: discrete
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'unitdelay'
---

# Unit Delay

Delay signal one sample period

## 中文

将信号延迟一个采样周期

### 所属库

Simulink / Discrete HDL Coder / Discrete

### 描述

Unit Delay 模块将其输入保持并延迟一个采样周期。当放置于迭代子系统中时，该模块将其输入保持并延迟一个迭代。此模块相当于 z-1 离散时间运算符。此模块接受一个输入并生成一个输出。每个信号可以是标量，也可以是向量。如果输入为向量，模块会按相同的采样周期保持和延迟向量中的所有元素。

可通过**初始条件**参数指定第一个采样周期的模块输出。仔细选择此参数可以最大程度地减少不需要的输出行为。可通过**采样时间**参数指定样本之间的时间间隔。设置为 `-1` 表示模块将继承**采样时间**。

**注意**

如果您使用 Unit Delay 模块在以不同采样率运行的模块之间进行速率转移，此模块将报告错误。请改用 Rate Transition 模块。

#### 与类似模块的比较

Memory、Unit Delay 和 Zero-Order Hold 模块提供相似的功能，但各自具有不同的能力。此外，每个模块的用途也各不相同。

下表显示每个模块的推荐用途。

| 模块 | 模块的用途 | 引用示例 |
| --- | --- | --- |
| Unit Delay | 使用您指定的离散采样时间实现延迟。该模块接受并输出具有离散采样时间的信号。 | - 具有闭环控制的发动机定时模型（Compression 子系统） |
| Memory | 将信号延迟一个主积分时间步。在理想情况下，该模块接受连续（或在子时间步中固定）的信号并输出在子时间步中固定的信号。 | - Building a Clutch Lock-Up Model（Friction Mode Logic/Lockup FSM 子系统） - 使用 Memory 模块捕获弹球的速度 |
| Zero-Order Hold | 将具有连续采样时间的输入信号转换为具有离散采样时间的输出信号。 | - Developing the Apollo Lunar Module Digital Autopilot - 使用 MATLAB Function 模块的雷达跟踪 |

每个模块有以下功能。

| 功能 | 内存 | 单位延迟 | 零阶保持 |
| --- | --- | --- | --- |
| 指定初始条件 | 是 | 是 | 否，因为在时间 t = 0 的模块输出必须与输入值相匹配。 |
| 指定采样时间 | 否，因为该模块只能从驱动模块或用于整个模型的求解器继承采样时间。 | 是 | 是 |
| 支持基于帧的信号 | 否 | 是 | 是 |
| 支持状态记录 | 否 | 是 | 否 |

#### 字符串支持

仅当 Unit Delay 模块配置为**初始条件**参数采用默认值 (0) 时，该模块才接受和输出字符串数据类型。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量

输入信号，它被模块延迟了一个采样周期。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量

输出信号，即延迟了一个采样周期的输入信号。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### 参数

#### 常设

#### **初始条件** — 第一个采样周期输出 `0` (默认) | 标量 | 向量

指定第一个采样周期的仿真输出，否则，此周期内 Unit Delay 模块的输出为未定义。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialCondition` |
| **类型**：字符向量 |
| **值**：标量 | 向量 |
| **默认值**：`'0'` |

#### **输入处理** — 指定基于采样或基于帧的处理 **元素作为通道(基于采样)** (默认) | **列作为通道(基于帧)**

指定模块是执行基于采样还是基于帧的处理：

- **列作为通道(基于帧)** - 将输入信号的每一列视为一个单独的通道（基于帧的处理）。

  **注意**

  基于帧的处理需要具有 DSP System Toolbox™ 许可证。

  有关详细信息，请参阅Sample- and Frame-Based Concepts (DSP System Toolbox)。
- **元素作为通道(基于采样)** - 将输入信号的每个元素视为一个单独的通道（基于采样的处理）。

可以使用**输入处理**指定模块是执行基于采样的处理还是基于帧的处理。有关这两种处理模式的详细信息，请参阅Sample- and Frame-Based Concepts (DSP System Toolbox)。

##### 编程用法

|  |
| --- |
| **模块参数**：`InputProcessing` |
| **类型**：字符向量 |
| **值**：`'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **默认值**：`'Elements as channels (sample based)'` |

#### **采样时间(-1 表示继承)** — 采样时间命中点之间的离散间隔 `-1` (默认) | 1×2 向量

输入采样时间命中点之间的离散间隔，或者指定 `-1` 以继承采样时间。

另请参阅指定采样时间。

##### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：实数标量 | 1×2 向量 |
| **默认值**：`'-1'` |

#### 状态属性

#### **状态名称** — 模块状态的唯一名称 `''` (默认) | 字母数字字符串

使用此参数为模块状态指定唯一名称。默认值为 `' '`。如果此字段为空，则表示未指定任何名称。使用此参数时，请记住以下注意事项：

- 有效的标识符以字母或下划线字符开始，后跟字母数字或下划线字符。
- 状态名称仅适用于所选模块。

当您点击**应用**时，此参数将启用**状态名称必须解析为 Simulink 信号对象**。

有关详细信息，请参阅模型接口元素的 C 数据代码接口配置 (Simulink Coder)。

##### 编程用法

|  |
| --- |
| **模块参数**：`StateName` |
| **类型：**字符向量 |
| **值：**唯一名称 |
| **默认值：**`''` |

#### **状态名称必须解析为 Simulink 信号对象** — 要求状态名称解析为信号对象的选项 `off` (默认) | `on`

指定是否需要将状态名称解析为信号对象。如果选中此选项，则在指定的状态名称与信号对象的名称不匹配时，软件会在运行时生成错误。

选择此参数将禁用**代码生成存储类**参数。

##### 依赖关系

当您为**状态名称**参数指定值并将**信号解析**模型配置参数设置为**无**以外的值时启用。

##### 编程用法

|  |
| --- |
| **模块参数**：`StateMustResolveToSignalObject` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `image` | `integer` | `single` | `string` |
| **直接馈通** | `否a` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 此模块的直接馈通特性取决于模块参数值。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

生成的代码在特定条件下依赖于 `memcpy` 或 `memset` 函数 (`strong.h`)。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **AllowDelayDistribution** | 允许在分布式流水线和延迟吸收优化期间分布或吸收延迟。默认值为 **inherit**。有关详细信息，请参阅AllowDelayDistribution (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |
| **ResetType** | 隐藏重置逻辑生成。默认值为**默认**，它生成重置逻辑。另请参阅ResetType (HDL Coder)。 |

**复数数据支持**

此模块支持复信号的代码生成。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Discrete HDL Coder / Discrete

## Description

The Unit Delay block holds and delays its input by one sample period. When
placed in an iterator subsystem, it holds and delays its input by one iteration. This
block is equivalent to the z-1 discrete-time operator. The
block accepts one input and generates one output. Each signal can be scalar or vector.
If the input is a vector, the block holds and delays all elements of the vector by the
same sample period.

You specify the block output for the first sampling period with the **Initial
conditions** parameter. Careful selection of this parameter can minimize
unwanted output behavior. You specify the time between samples with the **Sample
time** parameter. A setting of `-1` means the block
inherits the **Sample time**.

**Note**

The Unit Delay block errors out if you use it to create a
transition between blocks operating at different sample rates. Use the Rate Transition block
instead.

### Comparison with Similar Blocks

The Memory, Unit Delay, and Zero-Order Hold
blocks provide similar functionality but have different capabilities. Also, the purpose of
each block is different.

This table shows recommended usage for each block.

| Block | Purpose of the Block | Reference Examples |
| --- | --- | --- |
| Unit Delay | Implement a delay using a discrete sample time that you specify. The block accepts and outputs signals with a discrete sample time. | - Engine Timing Model with Closed Loop Control (Compression subsystem) |
| Memory | Implement a delay by one major integration time step. Ideally, the block accepts continuous (or fixed in minor time step) signals and outputs a signal that is fixed in minor time step. | - Building a Clutch Lock-Up Model (Friction Mode Logic/Lockup FSM subsystem) - Capture the Velocity of a Bouncing Ball with the Memory Block |
| Zero-Order Hold | Convert an input signal with a continuous sample time to an output signal with a discrete sample time. | - Developing the Apollo Lunar Module Digital Autopilot - Radar Tracking Using MATLAB Function Blocks |

Each block has the following capabilities.

| Capability | Memory | Unit Delay | Zero-Order Hold |
| --- | --- | --- | --- |
| Specification of initial condition | Yes | Yes | No, because the block output at time t = 0 must match the input value. |
| Specification of sample time | No, because the block can only inherit sample time from the driving block or the solver used for the entire model. | Yes | Yes |
| Support for frame-based signals | No | Yes | Yes |
| Support for state logging | No | Yes | No |

### String Support

The Unit Delay block can accept and output string data type only if
the block is configured for the default value of the **Initial
condition** parameter (0).

## Ports

### Input

### **Port\_1** — Input signal scalar | vector

Input signal that the block delays by one sample period.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal that is the input delayed by one sample period.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## Parameters

### Main

### **Initial condition** — First sample period output `0` (default) | scalar | vector

Specify the output of the simulation for the first sampling period,
during which the output of the Unit Delay block is
otherwise undefined.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InitialCondition` |
| **Type**: character vector |
| **Value**: scalar | vector |
| **Default**: `'0'` |

### **Input processing** — Specify sample- or frame-based processing `Elements as channels (sample based)` (default) | `Columns as channels (frame based)`

Specify whether the block performs sample- or frame-based processing:

- `Columns as channels (frame based)` — Treat
  each column of the input as a separate channel (frame-based processing).

  **Note**

  Frame-based processing requires a DSP System Toolbox™ license.

  For more information, see Sample- and Frame-Based Concepts (DSP System Toolbox).
- `Elements as channels (sample based)` — Treat
  each element of the input as a separate channel (sample-based
  processing).

Use **Input processing** to specify whether the block performs
sample- or frame-based processing. For more information about these two processing
modes, see Sample- and Frame-Based Concepts (DSP System Toolbox).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InputProcessing` |
| **Type**: character vector |
| **Values**: `'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **Default**: `'Elements as channels (sample based)'` |

### **Sample time (-1 for inherited)** — Discrete interval between sample time hits `-1` (default) | 1-by-2 vector

Enter the discrete interval between sample time hits or specify
`-1` to inherit the sample time.

See also Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Value**: real scalar | 1-by-2 vector |
| **Default**: `'-1'` |

### State Attributes

### **State name** — Unique name for block state `''` (default) | alphanumeric string

Use this parameter to assign a unique name to the block state. The default is `' '`. When this field is blank, no name is assigned. When using this parameter, remember these considerations:

- A valid identifier starts with an alphabetic or underscore character, followed by alphanumeric or underscore characters.
- The state name applies only to the selected block.

This parameter enables **State name must resolve to Simulink signal object** when you click **Apply**.

For more information, see C Data Code Interface Configuration for Model Interface Elements (Simulink Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateName` |
| **Type:** character vector |
| **Values:** unique name |
| **Default:** `''` |

### **State name must resolve to Simulink signal object** — Option to require that state names resolve to signal object `off` (default) | `on`

Specify whether state names are required to resolve to signal objects. If selected,
the software generates an error at run time if you specify a state name that does not
match the name of a signal object.

Selecting this parameter disables the **Code generation storage
class** parameter.

#### Dependencies

Enabled when you specify a value for the **State name** parameter
and set the **Signal resolution** model configuration parameter to
a value other than `None`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `StateMustResolveToSignalObject` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `image` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `noa` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Direct feedthrough characteristics for this block depend on block parameter values. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on `memcpy` or `memset`
functions (`strong.h`) under certain conditions.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **AllowDelayDistribution** | Allow delay to be distributed or absorbed during the distributed pipelining and delay absorption optimizations. The default is `inherit`. For more details, see AllowDelayDistribution (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **ResetType** | Suppress reset logic generation. The default is `default`, which generates reset logic. See also ResetType (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
