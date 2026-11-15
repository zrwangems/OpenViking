---
type: simulink-block
title: 'Hit Scheduler'
family: messages-events
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Messages & Events'
documentation_page: 'hitscheduler'
---

# Hit Scheduler

Schedule major time steps for variable-step solver

## 中文

为变步长求解器调度主时间步

### 库

Simulink / Messages & Events

### 说明

使用 Hit Scheduler 模块在仿真期间为变步长求解器调度主时间步。借助 Hit Scheduler 模块，您可以根据仿真期间模型的行为实现动态求解器命中事件调度。

要调度主时间步，需为该模块提供两个输入：

- **En** — 使能输入控制模块何时调度时间步。当该输入为逻辑 `true` 时，模块会调度一个时间步。
- **Δt** — 时间间隔输入指定所调度时间步何时发生。Hit Scheduler 模块将待调度的时间命中（以 seconds 为单位）计算为当前仿真时间与时间间隔输入之和。

当仿真到达所调度的时间命中时，仿真会执行一个主时间步，并且模块输出会更新。您可以使用 **输出类型** 参数将该模块配置为生成信号输出或函数调用输出。

您可以使用 Hit Scheduler 模块调度多个未来时间步。该模块将未来时间步存储在队列中，您可以使用 **初始缓冲区大小** 和 **使用固定缓冲区大小** 参数配置该队列。

#### 向量信号输入和输出

当您将该模块配置为生成信号输出时，可以使用单个模块通过向量输入，基于模型中的多个信号来调度时间命中。**En** 输入向量中的每个元素指示模块应基于 **Δt** 向量中的同一元素何时调度时间命中。模块输出信号与输入信号具有相同的维度。当仿真执行所调度的步长时，输出向量中与调度该时间步的输入向量元素相对应的元素会从逻辑 `false` 变为逻辑 `true`。

### 端口

#### 输入

#### **En** — 用于调度时间步的使能信号 标量 | 向量

当使能输入值为逻辑 `true` 时，模块会调度一个仿真时间步。

当您将 **输出类型** 设置为 `Signal` 时，输入可以是标量或向量。当 **En** 输入为向量时，**Δt** 输入必须为具有相同维度的向量。

当您将 **输出类型** 设置为 `Function call` 时，输入必须为标量。

**数据类型：** `Boolean`

#### **Δt** — 当前仿真时间与要调度的时间步之间的间隔 标量 | 向量

模块将待调度的时间步（以 seconds 为单位）计算为当前仿真时间与时间间隔输入当前值之和。

当您将 **输出类型** 设置为 `Signal` 时，输入可以是标量或向量。当 **Δt** 输入为向量时，**En** 输入必须为具有相同维度的向量。

当您将 **输出类型** 设置为 `Function call` 时，输入必须为标量。

**数据类型：** `double`
#### 输出

#### **Port\_1** — 所调度时间步的指示 标量 | 向量

模块输出值指示仿真何时执行模块所调度的时间步。您可以使用 **输出类型** 参数将该模块配置为生成信号或函数调用事件。模块输出的值取决于输出类型和输入信号的维度。

- 当您将 **输出类型** 设置为 `Signal` 且输入信号为标量时，当仿真执行所调度的时间步时，模块输出变为逻辑 `true`。
- 当您将 **输出类型** 设置为 `Signal` 且输入信号为向量时，输出向量中与调度该时间步的输入向量元素相对应的元素会从逻辑 `false` 变为逻辑 `true`。
- 当您将 **输出类型** 设置为 `Function-Call` 时，输入必须为标量，并且当仿真执行所调度的时间步时，模块会生成函数调用事件。

由于 Hit Scheduler 模块显式调度会影响模块执行时间的求解器时间命中，因此对于两种输出类型，输出都具有可变采样时间。有关可变采样时间的详细信息，请参阅采样时间类型。

**数据类型：** `Boolean`

### 参数

#### **输出类型** — 模块输出的类型 `Signal`（默认） | `Function Call`

模块输出指示仿真何时执行模块所调度的时间步。您可以将该模块配置为生成 Boolean 信号或函数调用事件。

- `Signal` — 当仿真执行所调度的时间步时，模块输出变为逻辑 `true`。支持标量和向量输入及输出信号。
- `Function Call` — 当仿真执行所调度的时间步时，模块生成函数调用事件。仅支持标量输入信号。

#### 程序化使用

|  |
| --- |
| **模块参数：** `HitSchedulerOutputType` |
| **类型：** string | character vector |
| **值：** `'Signal'` | `'Function-Call'` |
| **默认值：** `'Signal'` |

#### **初始缓冲区大小** — 用于已调度时间步的缓冲区初始大小 `256`（默认） | integer

将存储已调度时间步的缓冲区大小指定为正的标量 integer 值。

默认情况下，缓冲区大小是动态的，因此如果缓冲区在仿真期间填满，软件可以增大其大小。当您选择 **使用固定缓冲区大小** 时，**初始缓冲区大小** 参数值指定缓冲区的固定大小。如果缓冲区在仿真期间溢出，Hit Scheduler 模块会按先进先出方式覆盖已调度的时间命中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialBufferSize` |
| **类型：** string | character vector |
| **值：** 正数、整数、数值标量 |
| **默认值：** `'256'` |

#### **使用固定缓冲区大小** — 使用固定大小缓冲区的选项 `off`（默认） | `on`

当您选择此选项时，模块使用固定缓冲区大小，并且 **初始缓冲区大小** 参数指定缓冲区的大小。如果缓冲区在仿真期间溢出，Hit Scheduler 模块会按先进先出方式覆盖已调度的时间命中。默认情况下，缓冲区大小是动态的，因此软件可以在仿真期间根据需要调整大小。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FixedBuffer` |
| **类型：** string | character vector |
| **值：** `'on'` | `'off'` |
| **默认值：** `'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **零交叉检测** | `no` |

### 版本历史

**在 R2022b 中引入**

## Libraries

Simulink / Messages & Events

## Description

Use the Hit Scheduler block to schedule major time steps for a
variable-step solver during simulation. With the Hit Scheduler block, you can
implement dynamic solver hit event scheduling based on the behavior of your model during
simulation.

To schedule a major time step, you provide the block two inputs:

- **En** — The enable input controls when the block schedules a time
  step. The block schedules a time step when the input is logical
  `true`.
- **Δt** — The time interval input specifies when the scheduled time
  step occurs. The Hit Scheduler block calculates the time hit to schedule,
  in seconds, as the sum of the current simulation time and the time interval
  input.

When the simulation reaches the scheduled time hit, the simulation takes a major time step
and the block output updates. You can configure the block to produce either a signal output or
a function-call output using the **Output type** parameter.

You can use the Hit Scheduler block to schedule multiple future time steps.
The block stores the future time steps in a queue you can configure using the
**Initial buffer size** and **Use fixed buffer size**
parameters.

### Vector Signal Inputs and Outputs

When you configure the block to produce a signal output, you can use a single block to
schedule time hits based on multiple signals in the model by using vector inputs. Each
element in the **En** input vector indicates when the block should schedule
a time hit based on the same element in the **Δt** vector. The block output
signal has the same dimensions as the input signals. When the simulation takes a scheduled
step, the element in the output vector that corresponds to the input vector element that
scheduled the time step changes from logical `false` to logical
`true`.

## Ports

### Input

### **En** — Enable signal for scheduling time step scalar | vector

When the enable input value is logical `true`, the block
schedules a simulation time step.

When you set **Output type** to
`Signal`, the input can be a scalar or a vector. When the
**En** input is a vector, the **Δt** input must be
a vector with the same dimensions.

When you set **Output type** to `Function
call`, the input must be a scalar.

**Data Types:** `Boolean`

### **Δt** — Interval between current simulation time and time step to schedule scalar | vector

The block calculates the time step to schedule, in seconds, as the sum of the
current simulation time and the current value of the time interval input.

When you set **Output type** to
`Signal`, the input can be a scalar or a vector. When the
**Δt** input is a vector, the **En** input must be
a vector with the same dimensions.

When you set **Output type** to `Function
call`, the input must be a scalar.

**Data Types:** `double`
### Output

### **Port\_1** — Indication of scheduled time step scalar | vector

The block output value indicates when the simulation takes a time step the block
scheduled. You can configure the block to produce a signal or a function-call event
using the **Output type** parameter. The value of the block output
depends on the type of output and the dimensions of the input signal.

- When you set **Output type** to
  `Signal` and the input signal is a scalar, the block
  output becomes logical `true` when the simulation takes a
  scheduled time step.
- When you set **Output type** to
  `Signal` and the input signal is a vector, the
  element in the output vector that corresponds to the input vector element that
  scheduled the time step changes from logical `false` to logical
  `true`.
- When you set **Output type** to
  `Function-Call`, the input must be scalar, and the
  block generates a function-call event when the simulation takes a scheduled time
  step.

Because the Hit Scheduler block explicitly schedules solver time
hits that affect when the block executes, the output has variable sample time for both
output types. For more information about variable sample time, see Types of Sample Time.

**Data Types:** `Boolean`

## Parameters

### **Output type** — Type of block output `Signal` (default) | `Function Call`

The block output indicates when the simulation takes a time step that the block
scheduled. You can configure the block to produce a Boolean signal or a function-call
event.

- `Signal` — Block output becomes logical
  `true` when the simulation takes a scheduled time step. Scalar
  and vector input and output signals are supported.
- `Function Call` — Block generates a function-call event
  when the simulation takes a scheduled time step. Only scalar input signals are
  supported.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `HitSchedulerOutputType` |
| **Type:** string | character vector |
| **Values:** `'Signal'` | `'Function-Call'` |
| **Default:** `'Signal'` |

### **Initial buffer size** — Initial size of buffer for scheduled time steps `256` (default) | integer

Specify the size of the buffer that stores scheduled time steps as a positive,
scalar integer value.

By default, the buffer size is dynamic so that the software can increase the size if
the buffer fills during simulation. When you select **Use fixed buffer
size**, the **Initial buffer size** parameter value
specifies the fixed size for the buffer. If the buffer overflows during simulation, the
Hit Scheduler block overwrites scheduled time hits on a first-in,
first-out basis.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialBufferSize` |
| **Type:** string | character vector |
| **Values:** positive, whole, numeric scalar |
| **Default:** `'256'` |

### **Use fixed buffer size** — Option to use fixed-size buffer `off` (default) | `on`

When you select this option, the block uses a fixed buffer size, and the
**Initial buffer size** parameter specifies the size of the buffer.
If the buffer overflows during simulation, the Hit Scheduler block
overwrites scheduled time hits on a first-in, first-out basis. By default, the buffer
size is dynamic so that the software can adjust the size during simulation as
needed.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FixedBuffer` |
| **Type:** string | character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Version History

**Introduced in R2022b**
