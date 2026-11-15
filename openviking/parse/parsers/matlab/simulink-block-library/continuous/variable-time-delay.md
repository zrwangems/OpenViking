---
type: simulink-block
title: 'Variable Time Delay'
family: continuous
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Continuous'
documentation_page: 'variabletimedelay'
---

# Variable Time Delay

Delay input by variable amount of time

## 中文

按可变时间量延迟输入

### 所属库

Simulink / Continuous

### 描述

Variable Transport Delay 和 Variable Time Delay 模块在 Simulink® 模块库中显示为两个模块。但它们是同一个 Simulink 模块，只是**选择延迟类型**参数的设置不同。使用此参数可以指定模块的运行模式。

#### 可变时滞

在此模式中，模块具有数据输入、时滞输入和数据输出。（有关各种模块方向的端口顺序的描述，请参阅标识旋转或翻转模块上的端口位置。）当前时间步的输出等于上一个时间步的数据输入值。此时间步等于当前仿真时间减去由时滞输入指定的延迟时间。

y(t)=u(t−t0)=u(t−τ(t))

在仿真过程中，模块将时间和输入值对存储在内部缓冲区。仿真开始时，模块会输出**初始输出**参数的值，直到仿真时间超过时滞输入。然后，在每个仿真步，模块会在相当于当前仿真时间减去延迟时间的时间输出信号。

如果您需要两个存储输入时间之间的某个时间的输出，且求解器是连续求解器，模块将在各点之间进行线性插值。如果时滞小于步长，模块将根据上一个点外插输出点。例如，假定一个定步长仿真的步长为 `1`，当前时间为 `t = 5`。如果延迟为 `0.5`，则模块必须在 `t = 4.5` 时生成点，但最新存储的时间值为 `t = 4`。那么，模块将根据 t = `4` 时的输入外插 t = `4.5` 时的输入，并将外插值作为 `t = 5` 时的输出。

根据上一个时间步向前外插产生的结果没有根据当前时间步向后外插产生的结果准确。但是，模块无法使用当前输入计算其输出值，因为输入端口没有直接馈通。

如果模型指定了离散求解器，模块将不会在时间步之间插值。相反，它将返回所需值前面的那个最近存储值。

#### 可变传输延迟

在此模式中，当前时间步的模块输出等于之前的时间步（等于当前时间减去传输延迟）的数据（顶部或左侧）输入的值。

y(t)=u(t−td(t))

Simulink 软件通过解析下列方程来计算传输延迟 td(t)：

∫t−td(t)t1ti(τ)dτ=1

此方程涉及到一个瞬时时滞 ti(t)，由时滞（底部或右侧）输入指定。

假设您要使用此模块为管道内流速随时间改变的流体建模。在本例中，模块的时滞输入为

ti(t)=Lvi(t)

其中 `L` 代表管道长度，vi(t) 代表流体速度。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。

当您选中**处理零延迟**参数时，此端口有直接馈通。当您选择**线性化期间直接馈通输入**参数时，此端口在配平和线性化操作期间有直接馈通。

**数据类型:** `double`

#### **t0** — 时滞输入 标量 | 向量 | 矩阵

指定为标量、向量或矩阵的时滞输入。当模块处于**可变时滞**模式时，此值指定时滞。有关该计算的详细信息，请参阅可变时滞。

此端口具有直接馈通。

##### 依赖关系

要启用此端口，请将**选择延迟类型**设置为**可变时滞**。

**数据类型:** `double`

#### **ti** — 瞬时时滞输入 标量 | 向量 | 矩阵

指定为标量、向量或矩阵的瞬时时滞输入。当模块处于**可变传输延迟**模式时，此值用于计算传输延迟。有关该计算的详细信息，请参阅可变传输延迟。

此端口具有直接馈通。

##### 依赖关系

要启用此端口，请将**选择延迟类型**设置为**可变传输延迟**。

**数据类型:** `double`
#### 输出

#### **Port\_1** — 延迟的信号 标量 | 向量 | 矩阵

输出信号，指定为标量、向量或矩阵。

**数据类型:** `double`

### 参数

#### **选择延迟类型** — 延迟的类型 **可变时滞** | **可变传输延迟**

将延迟类型指定为**可变时滞**或**可变传输延迟**。

此参数的默认值取决于模块实现：对于 Variable Time Delay 模块，默认值为**可变时滞**，对于 Variable Transport Delay 模块，默认值为**可变传输延迟**。

##### 依赖关系

- 将此参数设置为**可变时滞**将启用**处理零延迟**参数。
- 将此参数设置为**可变传输延迟**将启用**绝对容差**和**状态名称**参数。

##### 编程用法

|  |
| --- |
| **模块参数：**`VariableDelayType` |
| **类型：**字符向量、字符串 |
| **值**：`'Variable transport delay'` | `'Variable time delay'` |

#### **最大延迟** — 时滞输入的最大值 `10` (默认) | 标量 | 向量

设置时滞输入的最大值。此值定义此模块允许的最大时滞输入。模块会截减超过此值的任何延迟量。此值不能为负数。如果时滞变为负数，模块会将其截减为零并发出警告消息。

##### 编程用法

|  |
| --- |
| **模块参数：**`MaximumDelay` |
| **类型：**字符向量、字符串 |
| **值**：标量 | 向量 |
| **默认值：**`'10'` |

#### **初始输出** — 初始输出 `0` (默认) | 标量 | 向量

指定模块在仿真时间首次超过输入的时滞量之前生成的输出。

##### 依赖关系

- 此模块的初始输出不能为 `inf` 或 `NaN`。
- 不能在仿真运行时更改`运行到运行可调参数`。但是，在仿真开始之前更改此参数不会使得加速或快速加速重新生成代码。

##### 编程用法

|  |
| --- |
| **模块参数：**`InitialOutput` |
| **类型：**字符向量、字符串 |
| **值：**标量 | 向量 |
| **默认值：**`'0'` |

#### **初始缓冲区大小** — 初始内存分配 `1024` (默认) | 标量

为要存储的输入点数定义初始内存分配。输入点定义了输入信号在当前仿真时间之前的历史记录。

- 如果输入点数超出初始缓冲区大小，模块将分配更多内存。
- 仿真结束后，如果缓冲区空间不足而必须分配更多内存，则会显示一条消息。

##### 提示

- 由于分配内存会降低仿真速度，因此如果仿真速度很重要，请谨慎选择此值。
- 对于长时滞，此模块可能会占用大量内存，特别是对于维度化输入。

##### 编程用法

|  |
| --- |
| **模块参数：**`MaximumPoints` |
| **类型：**字符向量、字符串 |
| **值：**标量 | 向量 |
| **默认值：**`'1024'` |

#### **使用固定缓冲区大小** — 使用固定大小的缓冲区 `off` (默认) | `on`

选中此复选框将使用固定大小缓冲区保存来自之前时间步的输入数据。清除此复选框后，模块不使用固定大小缓冲区。

可通过**初始缓冲区大小**参数指定缓冲区大小。如果缓冲区已满，新数据将替换缓冲区中已有的数据。Simulink 软件使用线性外插来估算不在缓冲区内的输出值。

**注意**

即使您不选中此复选框，ERT 或 GRT 代码生成也使用固定大小缓冲区。

##### 提示

- 如果输入数据为线性，选中此复选框可节省内存。
- 如果输入数据非线性，请勿选中此复选框。否则，生成的结果可能不准确。

##### 编程用法

|  |
| --- |
| **模块参数：**`FixedBuffer` |
| **类型：**字符向量、字符串 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### **处理零延迟** — 用于允许零延迟的选项 `off` (默认) | `on`

指定模块是否允许延迟值为 `0`。

- `off` - 该模块不允许零延迟。输入信号端口没有直接馈通。
- `on` - 该模块允许零延迟。输入信号端口具有直接馈通。

##### 依赖关系

要启用此参数，请将**选择延迟类型**参数设置为**可变时滞**。

##### 编程用法

|  |
| --- |
| **模块参数：**`ZeroDelay` |
| **类型：**字符串 | 字符向量 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### **线性化期间直接馈通输入** — 用于在线性化和配平操作期间使用零延迟的选项 `off` (默认) | `on`

指定在配平或线性化操作期间是否对模块使用零延迟值。

##### 提示

当您使用函数 `linmod`、`dlinmod` 或 `trim` 时，选择此参数可能会导致模型中状态的顺序发生变化。要提取此新的状态顺序，请执行以下操作：

1. 使用此命令编译模型，其中 `model` 是模型的名称。

   ```
       [sizes,x0,x_str] = model([],[],[],'lincompile');
   ```
2. 使用下列命令终止编译。

   ```
     model([],[],[],'term');
   ```

   输出参量 `x_str`（在 Simulink 模型中为状态的元胞数组）包含新的状态顺序。当您将状态向量作为输入传递给 `linmod`、`dlinmod` 或 `trim` 函数时，状态向量必须使用这种新的状态顺序。

##### 编程用法

|  |
| --- |
| **模块参数：**`TransDelayFeedthrough` |
| **类型：**字符串 | 字符向量 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### **帕德阶(用于线性化)** — 帕德逼近的阶 `0` (默认) | 标量

为线性化例程设置帕德逼近的阶。

- 默认值为 `0`，将产生无动态状态的单位增益。
- 将阶设置为正整数 `n` 将在模型中添加 `n` 个状态，但会产生更准确的传输延迟线性模型。

##### 编程用法

|  |
| --- |
| **模块参数：**`PadeOrder` |
| **类型：**字符向量、字符串 |
| **值：**标量 |
| **默认值：**`'0'` |

#### **绝对容差** — 用于计算模块状态的绝对容差 `auto` (默认) | 正实数标量或向量

指定用于计算模块状态的绝对容差。

##### 依赖关系

要启用此参数，请将**选择延迟类型**设置为**可变传输延迟**。

##### 编程用法

|  |
| --- |
| **模块参数：**`AbsoluteTolerance` |
| **类型：**字符向量、字符串 |
| **值：**`'auto'` | `'-1'` | 任何正实数标量或向量 |
| **默认值：**`'auto'` |

#### **状态名称(例如，'position')** — 每个状态的唯一名称 `' '` (默认) | 字符向量、字符串

为每个状态分配唯一名称。如果此字段为空，则不会分配任何名称。

##### 提示

- 要为单个状态分配名称，请输入名称并用引号引起来，例如 `'velocity'`。
- 要为多个状态分配名称，请输入以逗号分隔的列表并用花括号括起来，例如 `{'a', 'b', 'c'}`。每个名称都必须是唯一的。
- 状态名称只会应用于所选模块。
- 状态数量必须能够被状态名称的数量均分。
- 指定的名称数量可以少于状态数量，但不能多于状态数量。

  例如，可以在具有四个状态的系统中指定两个名称。第一个名称应用于前两个状态，第二个名称应用于后两个状态。
- 要在 MATLAB® 工作区中分配带变量的状态名称，请输入不带引号的变量。变量可以是字符向量、字符串、元胞数组或结构体。

##### 依赖关系

要启用此参数，请将**选择延迟类型**设置为**可变传输延迟**。

##### 编程用法

|  |
| --- |
| **模块参数：**`ContinuousStateAttributes` |
| **类型：**字符向量、字符串 |
| **值：**`' '` | 用户定义字符向量、用户定义的字符串 |
| **默认值：**`' '` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `否a, b` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 此模块的端口具有不同的直接馈通特性。  b 此模块的直接馈通特性取决于模块参数值。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产级的代码。涉及到嵌入式系统中常见的资源限制以及对速度和内存的限制。生成的代码可以包含内存的动态分配和释放、递归、额外的内存开销以及长短不等的执行时间。虽然代码在功能上有效并且在资源丰富的环境中通常可接受，但较小的嵌入式目标通常不能支持此类代码。

通常，考虑使用 Simulink 模型离散化器将连续模块映射到支持生产代码生成的离散等效模块。要启动模型离散化器，请在 Simulink 编辑器中，在 **App** 选项卡上，在 **App** 下，在**控制系统**下，点击**模型离散化器**。一个例外是 Second-Order Integrator 模块，因为对于该模块，模型离散化器产生近似离散化。

### 版本历史记录

**在 R2007a 中推出**

## Libraries

Simulink / Continuous

## Description

The Variable Transport Delay and
Variable Time Delay blocks appear as two blocks in the Simulink® block library. However, they are the same Simulink block with different settings for the **Select delay
type** parameter. Use this parameter to specify the mode in which the block
operates.

### Variable Time Delay

In this mode, the block has a data input, a time delay input, and a data output. (See Identify Port Location on Rotated or Flipped Block for a description of the port order for various block orientations.) The output at the current time step equals the value of its data input at a previous time step. This time step is the current simulation time minus a delay time specified by the time delay input.

y(t)=u(t−t0)=u(t−τ(t))

During the simulation, the block stores time and input value pairs in an internal buffer. At the start of simulation, the block outputs the value of the **Initial output** parameter until the simulation time exceeds the time delay input. Then, at each simulation step, the block outputs the signal at the time that corresponds to the current simulation time minus the delay time.

If you want the output at a time between input storing times and the solver is a continuous
solver, the block interpolates linearly between points. If the time delay is smaller than
the step size, the block extrapolates an output point from a previous point. For example,
consider a fixed-step simulation with a step size of `1` and the current
time at `t = 5`. If the delay is `0.5`, the block must
generate a point at `t = 4.5`, but the most recent stored time value is at
`t = 4`. Thus, the block extrapolates the input at
`4.5` from the input at `4` and uses the extrapolated
value as its output at `t = 5`.

Extrapolating forward from the previous time step can produce a less accurate result than extrapolating back from the current time step. However, the block cannot use the current input to calculate its output value because the input port does not have direct feedthrough.

If the model specifies a discrete solver, the block does not interpolate between time steps. Instead, it returns the nearest stored value that precedes the required value.

### Variable Transport Delay

In this mode, the block output at the current time step is equal to the value of its data
(top, or left) input at an earlier time step equal to the current time minus a
transport delay.

y(t)=u(t−td(t))

Simulink software finds the transport delay, td(t), by solving the following equation:

∫t−td(t)t1ti(τ)dτ=1

This equation involves an instantaneous time delay, ti(t), given by the time delay (bottom, or right) input.

Suppose that you want to use this block to model the fluid flow through a pipe where the fluid
speed varies with time. In this case, the time delay input to the block is

ti(t)=Lvi(t)

where `L` is the length of the pipe and vi(t) is the speed of the fluid.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal specified as a scalar, vector, or matrix.

This port has direct feedthrough when you select the **Handle zero
delay** parameter. This port has direct feedthrough during
trimming and linearization operations when you select the **Direct
feedthrough of input during linearization** parameter.

**Data Types:** `double`

### **t0** — Time delay input scalar | vector | matrix

Time delay input specified as a scalar, vector, or matrix. When the block is in `Variable time delay` mode, this value specifies the time delay. For more information about that calculation, see Variable Time Delay.

This port has direct feedthrough.

#### Dependencies

To enable this port, set **Select delay type** to `Variable time delay`.

**Data Types:** `double`

### **ti** — Instantaneous time delay input scalar | vector | matrix

Instantaneous time delay input specified as a scalar, vector, or matrix. When the block is in
`Variable transport delay` mode, this value is
used to calculate the transport delay. For more information about that
calculation, see Variable Transport Delay.

This port has direct feedthrough.

#### Dependencies

To enable this port, set **Select delay type** to `Variable transport delay`.

**Data Types:** `double`
### Output

### **Port\_1** — Delayed signal scalar | vector | matrix

Output signal specified as a scalar, vector, or matrix.

**Data Types:** `double`

## Parameters

### **Select delay type** — Type of delay `Variable time delay` | `Variable transport delay`

Specify the type of delay as `Variable time delay` or `Variable transport delay`.

The default value of this parameter depends on the block implementation:
`Variable time delay` for the Variable Time
Delay block, and `Variable transport delay` for
the Variable Transport Delay block.

#### Dependencies

- Setting this parameter to `Variable time
  delay` enables the **Handle zero
  delay** parameter.
- Setting this parameter to `Variable transport
  delay` enables the **Absolute
  tolerance** and **State Name**
  parameters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariableDelayType` |
| **Type:** character vector, string |
| **Values:** `'Variable transport delay'` | `'Variable time delay'` |

### **Maximum delay** — Maximum value of time delay input `10` (default) | scalar | vector

Set the maximum value of the time delay input. This value defines the largest time delay input that this block allows. The block clips any delay that exceeds this value. This value cannot be negative. If the time delay becomes negative, the block clips it to zero and issues a warning message.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MaximumDelay` |
| **Type:** character vector, string |
| **Value:** scalar | vector |
| **Default:** `'10'` |

### **Initial output** — Initial output `0` (default) | scalar | vector

Specify the output that the block generates until the simulation time first exceeds the time delay input.

#### Dependencies

- The initial output of this block cannot be `inf` or `NaN`.
- A `Run-to-run tunable parameter` cannot be changed during simulation run time. However, changing it before a simulation begins does not cause Accelerator or Rapid Accelerator to regenerate code.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialOutput` |
| **Type:** character vector, string |
| **Values:** scalar | vector |
| **Default:** `'0'` |

### **Initial buffer size** — Initial memory allocation `1024` (default) | scalar

Define the initial memory allocation for the number of input points to store. The input points define the history of the input signal up to the current simulation time.

- If the number of input points exceeds the initial buffer size, the block allocates additional memory.
- After simulation ends, a message displays if the buffer is not sufficient
  and more memory must be allocated.

#### Tips

- Because allocating memory slows down simulation, choose this value carefully if simulation speed is an issue.
- For long time delays, this block might use a large amount of memory, particularly for dimensionalized input.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MaximumPoints` |
| **Type:** character vector, string |
| **Values:** scalar | vector |
| **Default:** `'1024'` |

### **Use fixed buffer size** — Use fixed-size buffer `off` (default) | `on`

Selecting this check box uses a fixed-size buffer to save input data from previous time steps. When you clear this check box, the block does not use a fixed-size buffer.

The **Initial buffer size** parameter specifies the buffer size. If the buffer is full, new data replaces data already in the buffer. Simulink software uses linear extrapolation to estimate output values that are not in the buffer.

**Note**

ERT or GRT code generation uses a fixed-size buffer even if you do not select this check box.

#### Tips

- If the input data is linear, selecting this check box can save memory.
- If the input data is nonlinear, do not select this check box. Doing so might yield inaccurate results.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FixedBuffer` |
| **Type:** character vector, string |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Handle zero delay** — Option to allow zero delay `off` (default) | `on`

Specify whether the block allows a delay value of `0`.

- `off` — The block does not allow zero delay. The
  input signal port does not have direct feedthrough.
- `on` — The block allows zero delay. The input signal
  port has direct feedthrough.

#### Dependencies

To enable this parameter, set the **Select delay type**
parameter to `Variable time delay`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ZeroDelay` |
| **Type:** string | character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Direct feedthrough of input during linearization** — Option to use zero delay during linearization and trimming operations `off` (default) | `on`

Specify whether to use a delay value of zero for the block during trimming or
linearization operations.

#### Tips

Selecting this parameter can cause a change in the order of states in the
model when you use the functions `linmod`, `dlinmod`, or `trim`. To extract this new
state ordering:

1. Compile the model using this command, where
   `model` is the name of the model.

   ```
       [sizes,x0,x_str] = model([],[],[],'lincompile');
   ```
2. Terminate the compilation with the following command.

   ```
     model([],[],[],'term');
   ```

   The output argument `x_str`, which is a cell
   array of the states in the Simulink model, contains the new state ordering. When you pass
   a vector of states as input to the `linmod`,
   `dlinmod`, or `trim`
   functions, the state vector must use this new state ordering.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TransDelayFeedthrough` |
| **Type:** string | character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Pade order (for linearization)** — Order of Pade approximation `0` (default) | scalar

Set the order of the Pade approximation for linearization routines.

- The default value is `0`, which results in a unity gain with no dynamic states.
- Setting the order to a positive integer `n` adds `n` states to your model, but results in a more accurate linear model of the transport delay.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PadeOrder` |
| **Type:** character vector, string |
| **Values:** scalar |
| **Default:** `'0'` |

### **Absolute tolerance** — Absolute tolerance for computing block state `auto` (default) | positive, real, scalar or vector

Specify the absolute tolerance for computing the block state.

#### Dependencies

To enable this parameter, set **Select delay type** to `Variable transport delay`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AbsoluteTolerance` |
| **Type:** character vector, string |
| **Values:** `'auto'` | `'-1'` | any positive real scalar or vector |
| **Default:** `'auto'` |

### **State Name (e.g., 'position')** — Unique name for each state `' '` (default) | character vector, string

Assign a unique name to each state. If this field is blank, no name assignment occurs.

#### Tips

- To assign a name to a single state, enter the name between quotes, for example, `'velocity'`.
- To assign names to multiple states, enter a comma-delimited list surrounded by braces, for example, `{'a', 'b', 'c'}`. Each name must be unique.
- The state names apply only to the selected block.
- The number of states must divide evenly among the number of state names.
- You can specify fewer names than states, but you cannot specify more names than states.

  For example, you can specify two names in a system with four states. The first name applies to the first two states and the second name to the last two states.
- To assign state names with a variable in the MATLAB® workspace, enter the variable without quotes. A variable
  can be a character vector, string, cell array, or structure.

#### Dependencies

To enable this parameter, set **Select delay type** to `Variable transport delay`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ContinuousStateAttributes` |
| **Type:** character vector, string |
| **Values:** `' '` | user-defined character vector, user-defined string |
| **Default:** `' '` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `noa, b` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Ports of this block have different direct feedthrough characteristics.  b Direct feedthrough characteristics for this block depend on block parameter values. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production-quality code. Relates to resource limits and restrictions on speed and memory often found in embedded systems. The code generated can contain dynamic allocation and freeing of memory, recursion, additional memory overhead, and widely-varying execution times. While the code is functionally valid and generally acceptable in resource-rich environments, smaller embedded targets often cannot support such code.

In general, consider using the Simulink Model Discretizer to map continuous blocks into
discrete equivalents that support production code generation. To start the Model
Discretizer, in the Simulink Editor, on the **Apps** tab, under
**Apps**, under **Control Systems**, click
**Model Discretizer**. One exception is the Second-Order
Integrator block because, for this block, the Model Discretizer produces an
approximate discretization.

## Version History

**Introduced in R2007a**
