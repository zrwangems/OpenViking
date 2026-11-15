---
type: simulink-block
title: 'Transport Delay'
family: continuous
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Continuous'
documentation_page: 'transportdelay'
---

# Transport Delay

Delay input by given amount of time

## 中文

按给定的时间量延迟输入

### 所属库

Simulink / Continuous

### 描述

Transport Delay 模块可按指定的时间量延迟输入。可使用此模块实现时滞的仿真。此模块的输入应为连续信号。

在仿真开始时，模块输出**初始输出**参数，直到仿真时间超过**时滞**参数。然后，模块开始生成延迟的输入。在仿真期间，模块将输入点和仿真时间存储在缓冲区中。可通过**初始缓冲区大小**参数指定此大小。

如果您需要某个时间的输出，而存储的输入值没有对应的时间，模块会在点之间进行线性插值。当延迟小于步长时，模块会根据最后一个输出点外插，这可能会导致结果不准确。因为模块没有直接馈通，无法使用当前输入来计算输出值。例如，假定一个定步长仿真的步长为 1，当前时间为 t = 5。如果延迟为 0.5，模块必须在 t = 4.5 时生成点。因为最新存储的时间值是 t = 4，模块将执行正向外插。

Transport Delay 模块不会对离散信号进行插值。相反，模块会返回所需时间处的离散值。

此模块与 Unit Delay 模块不同，后者仅延迟和保持采样命中点的输出。

**提示**

请避免使用 `linmod` 线性化包含 Transport Delay 模块的模型。有关详细信息，请参阅 线性化模型。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

要延迟的输入信号，指定为标量、向量或矩阵。

当**时滞**参数值为 `0` 时，此端口具有直接馈通。由于**时滞**参数是运行时可调的，因此软件将 Transport Delay 模块视为此端口始终具有直接馈通。

**数据类型:** `double`
#### 输出

#### **Port\_1** — 延迟的信号 标量 | 向量 | 矩阵

输入信号，延迟指定的时间量。输出信号与输入信号具有相同的维度和数据类型。

**数据类型:** `double`

### 参数

#### **时滞** — 时滞 `1` (默认) | 标量 | 向量 | 矩阵

输入信号在传播到输出之前要延迟的仿真时间量，指定为非负标量、向量或矩阵。

##### 编程用法：

|  |
| --- |
| **模块参数**：`DelayTime` |
| **类型：**字符向量、字符串 |
| **值：**非负标量、向量或矩阵 |
| **默认值：**`'1'` |

#### **初始输出** — 初始输出值 `0` (默认) | 标量 | 向量 | 矩阵

指定模块在仿真时间首次超过输入的时滞量之前生成的输出，指定为标量、向量或矩阵。

##### 限制

此模块的初始输出不能为 `inf` 或 `NaN`。

在仿真运行时期间不能更改 `Run-to-run tunable parameter`。但是，在仿真开始之前更改此参数不会使得加速或快速加速重新生成代码。

##### 编程用法

|  |
| --- |
| **模块参数：**`InitialOutput` |
| **类型：**字符向量、字符串 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'0'` |

#### **初始缓冲区大小** — 初始内存分配 `1024` (默认) | 正整数标量

为要存储的输入点数定义初始内存分配。

- 如果输入点数超出初始缓冲区大小，模块将分配更多内存。
- 仿真结束后，会通过消息显示需要的总缓冲区大小。

##### 提示

- 由于分配内存会降低仿真速度，因此如果仿真速度很重要，请谨慎选择此值。
- 对于长时滞，此模块可能会使用大量内存，特别是对于维度化输入。

##### 编程用法

|  |
| --- |
| **模块参数：**`BufferSize` |
| **类型：**字符向量、字符串 |
| **值：**正整数标量 |
| **默认值：**`'1024'` |

#### **使用固定缓冲区大小** — 使用固定大小的缓冲区 `off` (默认) | `on`

选中此复选框可使用固定大小缓冲区保存之前时间步的输入数据。

可使用**初始缓冲区大小**参数指定缓冲区大小。如果缓冲区已满，新数据将替换缓冲区中已有的数据。Simulink® 软件使用线性外插来估算不在缓冲区内的输出值。

**注意**

如果您拥有 Simulink Coder™ 许可证，即使没有选中此复选框，ERT 或 GRT 代码生成也使用固定大小缓冲区。

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

#### **线性化期间直接馈通输入** — 启用直接馈通 `off` (默认) | `on`

使得模块在线性化期间输出其输入并配平，此操作可将模块模式设置为直接馈通。

##### 提示

- 当使用 `linmod`、`dlinmod` 或 `trim` 函数时，选中此复选框可能会使模型中状态的排序发生变化。要提取此新的状态顺序，请执行以下操作：

  1. 使用下列命令编译模型，其中 `model` 是 Simulink 模型的名称。

     ```
         [sizes, x0, x_str] = model([],[],[],'lincompile');
     ```
  2. 使用下列命令终止编译。

     ```
       model([],[],[],'term');
     ```
- 输出参量 `x_str`（在 Simulink 模型中为状态的元胞数组）包含新的状态顺序。当您将状态向量作为输入传递给 `linmod`、`dlinmod` 或 `trim` 函数时，状态向量必须使用这种新的状态顺序。

##### 编程用法

|  |
| --- |
| **模块参数：**`TransDelayFeedthrough` |
| **类型：**字符向量、字符串 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### **帕德阶(用于线性化)** — 帕德逼近的阶 `0` (默认) | 标量 | 向量 | 矩阵

线性化例程的帕德逼近的阶，设置为非负整数的标量、向量或矩阵。

- 默认值为 `0`，将产生无动态状态的单位增益。
- 将阶设置为正整数 `n` 将在模型中添加 `n` 个状态，但会产生更准确的传输延迟线性模型。

##### 编程用法

|  |
| --- |
| **模块参数：**`PadeOrder` |
| **类型：**字符向量、字符串 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'0'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产级的代码。涉及到嵌入式系统中常见的资源限制以及对速度和内存的限制。生成的代码可以包含内存的动态分配和释放、递归、额外的内存开销以及长短不等的执行时间。虽然代码在功能上有效并且在资源丰富的环境中通常可接受，但较小的嵌入式目标通常不能支持此类代码。

通常，考虑使用 Simulink 模型离散化器将连续模块映射到支持生产代码生成的离散等效模块。要启动模型离散化器，请在 Simulink 编辑器中，在 **App** 选项卡上，在 **App** 下，在**控制系统**下，点击**模型离散化器**。一个例外是 Second-Order Integrator 模块，因为对于该模块，模型离散化器产生近似离散化。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Continuous

## Description

The Transport Delay block delays the input by a specified amount of time. You
can use this block to simulate a time delay. The input to this block should be a
continuous signal.

At the start of simulation, the block outputs the **Initial output**
parameter until the simulation time exceeds the **Time delay**
parameter. Then, the block begins generating the delayed input. During simulation, the
block stores input points and simulation times in a buffer. You specify this size with
the **Initial buffer size** parameter.

When you want output at a time that does not correspond to times of the stored input
values, the block interpolates linearly between points. When the delay is smaller than
the step size, the block extrapolates from the last output point, which can produce
inaccurate results. Because the block does not have direct feedthrough, it cannot use
the current input to calculate an output value. For example, consider a fixed-step
simulation with a step size of 1 and the current time at t = 5. If the delay is 0.5, the
block must generate a point at t = 4.5. Because the most recent stored time value is at
t = 4, the block performs forward extrapolation.

The Transport Delay block does not interpolate discrete signals. Instead, the
block returns the discrete value at the required time.

This block differs from the Unit Delay block, which delays and holds
the output on sample hits only.

**Tip**

Avoid using `linmod` to linearize a model that contains a Transport
Delay block. For more information, see Linearizing Models.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal to delay, specified as a scalar, vector, or
matrix.

This port has direct feedthrough when the **Time
delay** parameter value is `0`. Because
the **Time delay** parameter is run-time tunable, the
software treats the Transport Delay block as though this
port always has direct feedthrough.

**Data Types:** `double`
### Output

### **Port\_1** — Delayed signal scalar | vector | matrix

Input signal, delayed by specified amount of time. Output has the same
dimensions and data type as the input signal.

**Data Types:** `double`

## Parameters

### **Time delay** — Time delay `1` (default) | scalar | vector | matrix

Specify the amount of simulation time to delay the input signal before propagation to the
output as a nonnegative scalar, vector, or matrix.

#### Programmatic Use:

|  |
| --- |
| **Block Parameter:** `DelayTime` |
| **Type:** character vector, string |
| **Values:** nonnegative scalar, vector, or matrix |
| **Default:** `'1'` |

### **Initial output** — Initial output value `0` (default) | scalar | vector | matrix

Specify the output that the block generates until the simulation time first exceeds the
time delay input as a scalar, vector, or matrix.

#### Limitations

The initial output of this block cannot be `inf` or
`NaN`.

A `Run-to-run tunable parameter` cannot
be changed during a simulation run time. However, changing it before a
simulation begins does not cause Accelerator or Rapid Accelerator to
regenerate code.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialOutput` |
| **Type:** character vector, string |
| **Values:** scalar | vector | matrix |
| **Default:** `'0'` |

### **Initial buffer size** — Initial memory allocation `1024` (default) | positive integer scalar

Define the initial memory allocation for the number of input points to
store.

- If the number of input points exceeds the initial buffer size, the
  block allocates additional memory.
- After simulation ends, a message shows the total buffer size
  needed.

#### Tips

- Because allocating memory slows down simulation, choose this
  value carefully if simulation speed is an issue.
- For long time delays, this block can use a large amount of
  memory, particularly for dimensionalized input.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BufferSize` |
| **Type:** character vector, string |
| **Value:** positive integer scalar |
| **Default:** `'1024'` |

### **Use fixed buffer size** — Use fixed-size buffer `off` (default) | `on`

Select this check box to use a fixed-size buffer to save input data from
previous time steps.

The **Initial buffer size** parameter specifies the size
of the buffer. If the buffer is full, new data replaces data already in the
buffer. Simulink® software uses linear extrapolation to estimate output values
that are not in the buffer.

**Note**

If you have a Simulink
Coder™ license, ERT or GRT code generation uses a fixed-size
buffer even if you do not select this check box.

#### Tips

- If the input data is linear, selecting this check box can save
  memory.
- If the input data is nonlinear, do not select this check box.
  Doing so can yield inaccurate results.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FixedBuffer` |
| **Type:** character vector, string |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Direct feedthrough of input during linearization** — Enable direct feedthrough `off` (default) | `on`

Cause the block to output its input during linearization and trim, which
sets the block mode to direct feedthrough.

#### Tips

- Selecting this check box can cause a change in the ordering of
  states in the model when you use the functions `linmod`,
  `dlinmod`, or
  `trim`. To
  extract this new state ordering:

  1. Compile the model using the following command, where
     `model` is the name of the
     Simulink model.

     ```
         [sizes, x0, x_str] = model([],[],[],'lincompile');
     ```
  2. Terminate the compilation with the following
     command.

     ```
       model([],[],[],'term');
     ```
- The output argument `x_str`, which is a cell
  array of the states in the Simulink model, contains the new state ordering. When you
  pass a vector of states as input to the
  `linmod`, `dlinmod`, or
  `trim` functions, the state vector must use
  this new state ordering.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TransDelayFeedthrough` |
| **Type:** character vector, string |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Pade order (for linearization)** — Order of Pade approximation `0` (default) | scalar | vector | matrix

Set the order of the Pade approximation for linearization routines as a
scalar, vector, or matrix of nonnegative integers.

- The default value is `0`, which results in a
  unity gain with no dynamic states.
- Setting the order to a positive integer `n` adds
  `n` states to your model, but results in a more
  accurate linear model of the transport delay.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PadeOrder` |
| **Type:** character vector, string |
| **Values:** scalar | vector | matrix |
| **Default:** `'0'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production-quality code. Relates to resource limits and
restrictions on speed and memory often found in embedded systems. The code generated
can contain dynamic allocation and freeing of memory, recursion, additional memory
overhead, and widely-varying execution times. While the code is functionally valid
and generally acceptable in resource-rich environments, smaller embedded targets
often cannot support such code.

In general, consider using the Simulink Model Discretizer to map continuous blocks into
discrete equivalents that support production code generation. To start the Model
Discretizer, in the Simulink Editor, on the **Apps** tab, under
**Apps**, under **Control Systems**, click
**Model Discretizer**. One exception is the Second-Order
Integrator block because, for this block, the Model Discretizer produces
an approximate discretization.

## Version History

**Introduced before R2006a**
