---
type: simulink-block
title: 'Memory'
family: discrete
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'memory'
---

# Memory

Output input from previous time step

## 中文

输出上一个时间步的输入

### 所属库

Simulink / Discrete HDL Coder / Discrete

### 描述

Memory 模块将其输入保持并延迟一个主积分时间步。当放置于迭代子系统中时，该模块将其输入保持并延迟一个迭代。此模块接受连续和离散信号。此模块接受一个输入并生成一个输出。每个信号可以是标量、向量、矩阵或 N 维数组。如果输入为非标量，该模块会将输入的所有元素保持并延迟相同的时间步。

使用**初始条件**参数指定第一个时间步的模块输出。仔细选择此参数可以最大程度地减少不需要的输出行为。但是，您不能指定采样时间。此模块的采样时间取决于所用求解器的类型，您也可以指定继承采样时间。**继承采样时间**参数确定采样时间是继承的还是基于求解器。

**提示**

当以下两个条件均为真时，避免使用 Memory 模块：

- 型使用变步长求解器 `ode15s` 或 `ode113`。
- 模块的输入在仿真期间发生变化。

当 Memory 模块继承离散采样时间时，该模块类似于 Unit Delay 模块。但是，Memory 模块不支持状态记录。如果需要记录最终状态，请改用 Unit Delay 模块。

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

#### 总线支持

Memory 模块支持总线。输入可以是满足下列限制条件的虚拟或非虚拟总线信号：

- **初始条件**必须为零、非零标量或有限数值结构体。
- 如果**初始条件**为零或结构体，而您指定了**状态名称**，则输入不能是虚拟总线。
- 如果**初始条件**为非零标量，则不能指定**状态名称**。

有关指定初始条件结构体的信息，请参阅Specify Initial Conditions for Bus Elements。

Memory 模块的非虚拟总线输入中的所有信号都必须具有相同的采样时间，即使关联总线对象的元素指定继承采样时间也是如此。您可以使用 Rate Transition 模块更改总线中单个信号或所有信号的采样时间。有关详细信息，请参阅Modify Sample Times for Nonvirtual Buses和支持总线的模块。

可使用总线数组作为 Memory 模块的输入信号。可为**初始条件**参数指定：

- 值 `0`。在这种情况下，总线数组中的所有单个信号都使用初始值 `0`。
- 结构体数组，为总线数组中的每个信号指定初始条件。
- 标量结构体，为总线类型定义的每个元素指定初始条件。使用此方法可为数组中的每条总线指定相同的初始条件。

有关定义和使用总线数组的详细信息，请参阅使用总线数组组合非虚拟总线。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

输入信号，指定为标量、向量、矩阵或 N 维数组。输入可以是连续的或离散的，包含 Simulink® 支持的任何数据类型的实数或复数值。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
#### 输出

#### **Port\_1** — 延迟了一个主积分时间步的输入 标量 | 向量 | 矩阵 | N 维数组

输出是来自上一时间步的输入。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 参数

#### 常设

#### **初始条件** — 初始条件 0 (默认) | 标量 | 向量 | 矩阵 | N 维数组

指定初始积分步长的输出。当不使用内置输入数据类型时，此值必须为 0。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialCondition` |
| **类型：**字符向量 |
| **值：**标量 | 向量 |
| **默认值：**`'0'` |

#### **继承采样时间** — 继承采样时间 `off` (默认) | `on`

选中此选项可从驱动模块继承采样时间：

- 如果驱动模块具有离散采样时间，模块将继承该采样时间。
- 如果驱动模块具有连续采样时间，则选中此复选框没有任何作用。采样时间取决于用于模型仿真的求解器的类型。

如果清除此复选框，模块采样时间将取决于用于模型仿真的求解器的类型：

- 如果求解器为变步长求解器，则模块采样时间是连续的，但在子时间步中是固定的：`[0, 1]`。
- 如果求解器是定步长求解器，则 `[0, 1]` 采样时间将转换为采样时间传播后的求解器步长。

##### 编程用法

|  |
| --- |
| **模块参数**：`InheritSampleTime` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **线性化期间直接馈通输入** — 在线性化和配平期间直接将输入作为输出 `off` (默认) | `on`

选中此选项可在线性化和配平期间直接将输入作为输出。此选择可将模块模式设置为直接馈通。

当使用函数 `linmod`、`dlinmod` 或 `trim` 时，选中此复选框可能会使模型中状态的排序发生变化。要提取这一新的状态排序方式，请使用阶以下命令。

首先使用以下命令编译模型，其中 `model` 是 Simulink 模型的名称。

```
    [sizes, x0, x_str] = model([],[],[],'lincompile');
```

接下来，使用以下命令终止编译。

```
  model([],[],[],'term');
```

输出参量 `x_str` 是 Simulink 模型中状态的元胞数组，其中包含新的状态排序方式。将状态向量作为输入传递到 `linmod`、`dlinmod` 或 `trim` 函数时，状态向量必须使用这一新的状态排序方式。

##### 编程用法

|  |
| --- |
| **模块参数**：`LinearizeMemory` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **针对离散采样时间信号进行线性化时视为单位延迟** — 对于离散输入，线性化为单位延迟 `off` (默认) | `on`

当 Memory 模块由具有离散采样时间的信号驱动时，选择此选项可将 Memory 模块线性化为单位延迟。

##### 编程用法

|  |
| --- |
| **模块参数**：`LinearizeAsDelay` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

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

#### **状态名称必须解析为 Simulink 信号对象** — 要求将状态名称解析为信号对象 `off` (默认) | `on`

选中此复选框会要求将状态名称解析为 Simulink 信号对象。

##### 依赖关系

要启用此参数，请为**状态名称**指定值。仅当将模型配置参数**信号解析**设置为除**无**以外的值时，才会显示此参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`StateMustResolveToSignalObject` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否a` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 此模块的直接馈通特性取决于模块参数值。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
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

The Memory block holds and delays its input by one major integration
time step. When placed in an iterator subsystem, it holds and delays its input by one
iteration. This block accepts continuous and discrete signals. The block accepts one
input and generates one output. Each signal can be a scalar, vector, matrix, or N-D
array. If the input is non-scalar, the block holds and delays all elements of the input
by the same time
step.

You specify the block output for the first time step using the **Initial
condition** parameter. Careful selection of this parameter can minimize
unwanted output behavior. However, you cannot specify the sample time. This block’s
sample time depends on the type of solver used, or you can specify to inherit it. The
**Inherit sample time** parameter determines whether sample time is
inherited or based on the solver.

**Tip**

Avoid using the Memory block when both these conditions are true:

- Your model uses the variable-step solver `ode15s` or
  `ode113`.
- The input to the block changes during simulation.

When the Memory block inherits a discrete sample time, the block is analogous to the
Unit Delay block. However, the Memory
block does not support state logging. If logging the final state is necessary, use a
Unit Delay block instead.

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

### Bus Support

The Memory block is a bus-capable block. The input can be a virtual
or nonvirtual bus signal subject to the following restrictions:

- **Initial condition** must be zero, a nonzero scalar, or
  a finite numeric structure.
- If **Initial condition** is zero or a structure, and you
  specify a **State name**, the input cannot be a virtual
  bus.
- If **Initial condition** is a nonzero scalar, you cannot
  specify a **State name**.

For information about specifying an initial condition structure, see Specify Initial Conditions for Bus Elements.

All signals in a nonvirtual bus input to a Memory block must have
the same sample time, even if the elements of the associated bus object specify
inherited sample times. You can use a Rate Transition block to change the
sample time of an individual signal, or of all signals in a bus. See Modify Sample Times for Nonvirtual Buses and
Bus-Capable
Blocks for more information.

You can use an array of buses as an input signal to a Memory block.
You can specify the **Initial condition** parameter with:

- The value `0`. In this case, all the individual
  signals in the array of buses use the initial value
  `0`.
- An array of structures that specifies an initial condition for each of
  the individual signals in the array of buses.
- A scalar structure that specifies an initial condition for each of the
  elements that the bus type defines. Use this technique to specify the
  same initial conditions for each of the buses in the array.

For details about defining and using an array of buses, see Group Nonvirtual Buses in Arrays of Buses.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

Input signal, specified as a scalar, vector, matrix, or N-D array. The input can be
continuous or discrete, containing real, or complex values of any data
type Simulink® supports.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — Input delayed by one major integration time step scalar | vector | matrix | N-D array

Output is the input from the previous time step.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### Main

### **Initial condition** — Initial condition 0 (default) | scalar | vector | matrix | N-D array

Specify the output at the initial integration step. This value must be 0 when you do not
use a built-in input data type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialCondition` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'0'` |

### **Inherit sample time** — Inherit sample time `off` (default) | `on`

Select to inherit the sample time from the driving block:

- If the driving block has a discrete sample time, the block
  inherits the sample time.
- If the driving block has a continuous sample time,
  selecting this check box has no effect. The sample time
  depends on the type of solver used for simulating the
  model.

When this check box is cleared, the block sample time
depends on the type of solver used for simulating the model:

- If the solver is a variable-step solver, the block sample time
  is continuous but fixed in minor time step: `[0,
  1]`.
- If the solver is a fixed-step solver, the `[0,
  1]` sample time converts to the solver step size
  after sample-time propagation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InheritSampleTime` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Direct feedthrough of input during linearization** — Output the input during linearization and trim `off` (default) | `on`

Select to output the input during linearization and trim. This
selection sets the block mode to direct feedthrough.

Selecting this check box can cause a change in the ordering of states
in the model when using the functions `linmod`, `dlinmod`, or `trim`. To extract this
new state ordering, use the following commands.

First compile the model using the following command, where
`model` is the name of the Simulink model.

```
    [sizes, x0, x_str] = model([],[],[],'lincompile');
```

Next, terminate the compilation with this command.

```
  model([],[],[],'term');
```

The output argument, `x_str`, which is a cell array
of the states in the Simulink model, contains the new state ordering. When passing a
vector of states as input to the `linmod`,
`dlinmod`, or `trim` functions,
the state vector must use this new state ordering.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LinearizeMemory` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Treat as a unit delay when linearizing with discrete sample time** — Linearize to unit delay for discrete inputs `off` (default) | `on`

Select to linearize the Memory block to a unit delay
when the Memory block is driven by a signal with a
discrete sample time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LinearizeAsDelay` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

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

### **State name must resolve to Simulink signal object** — Require state name resolve to a signal object `off` (default) | `on`

Select this check box to require that the state name resolves to a Simulink signal object.

#### Dependencies

To enable this parameter, specify a value for **State name**. This parameter appears only if you set the model configuration parameter **Signal resolution** to a value other than `None`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateMustResolveToSignalObject` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `noa` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Direct feedthrough characteristics for this block depend on block parameter values. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **ResetType** | Suppress reset logic generation. The default is `default`, which generates reset logic. See also ResetType (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
