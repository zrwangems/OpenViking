---
type: simulink-block
title: 'Propagation Delay'
family: discrete
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'propagationdelay'
---

# Propagation Delay

Model loop delay, latency, pulse delay

## 中文

对循环延迟、延迟、脉冲延迟建模

### 库

Simulink / Discrete

### 描述

Propagation Delay block 将信号的当前值延迟到未来，延迟量由延迟信号指定。Propagation Delay block 非常适合在离散系统中实现时间延迟。

在每个仿真步 *k*，模块对信号输入
*U**k* 和延迟输入
*D**k* 进行采样。模块输出值
变为延迟时间
*D**k* 从当前仿真时间
*T**k* 起经过之后的信号值。

*y*(*t*) =
*U**k* 当 *t* =
*T**k* +
*D**k*

在仿真开始时，模块输出值为 **Initial output** 模块参数值 *Y*0。延迟信号 *D*0 的第一个采样确定模块输出何时从 **Initial output** 值变为延迟后的输入信号值。

*y*(*t*) =
*Y*0 当 *t* < *T*0 +
*D*0

当仿真到达时间 *T*0 +
*D*0 时，模块输出由信号和延迟采样确定。

*y*(*t*) =
*U**k* 当
*T**k* +
*D**k* ≤ *t*
≤ *T**k*+1 +
*D**k*+1,

其中：

- *U**k* 是在 *t* =
  *T**k* 处取得的输入信号采样。
- *D**k* 是在 *t* =
  *T**k* 处取得的延迟信号采样。
- *T**k*+1 是取得下一个信号和延迟采样的仿真时间。
- *D**k*+1* 是在时间
  *T**k*+1 处取得的延迟采样。

### 端口

#### 输入

#### **u** — 要延迟的信号标量

Propagation Delay block 支持具有连续或离散采样时间的实数标量输入信号。输入信号数据类型可以是除 `int64` 和 `uint64` 之外的任何内置类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

#### **dt** — 延迟信号标量

延迟信号指定在仿真中每个时间步要应用的延迟量。您可以使用 Propagation Delay block 实现恒定延迟或可变延迟。

延迟信号值必须满足以下约束：

- 延迟信号必须包含大于 `128*eps` 的标量、实数、有限、正值，`128*eps` 是软件支持的最小时间分辨率。
- 延迟输入信号采样的输出时间必须单调递增。

  例如，假设在仿真时间 `0` 处延迟信号值为 `0.6`，下一个仿真步发生在时间 `0.5`。时间 `0.5` 处的延迟信号必须大于 `0.1`，以使输入信号采样 *U*0.5 的延迟输出时间大于输入信号采样 *U*0 的输出时间（`0.6`）。
- 当您选择 **Run at fixed time intervals** 时，延迟信号值必须大于您为 **Sample time** 参数指定的值。

**数据类型：** `double`

#### 输出

#### **y** — 延迟后的信号标量

输出信号与输入信号具有相同的数据类型。默认情况下，输出信号具有固定次小步长采样时间。当您选择 **Run at fixed time intervals** 时，输出信号具有您为 **Sample time** 参数指定的离散采样时间。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### 参数

#### **Initial output** — 输出信号的初始值 `0`（默认）| 标量

指定初始输出信号值
*Y*0。延迟信号
*D*0 的第一个采样确定模块输出何时
从 **Initial output** 值变为延迟后的输入信号
值。

*y*(*t*) =
*Y*0 当 *t* < *T*0 +
*D*0

#### 编程用法

|  |
| --- |
| **模块参数：** `InitialOutput` |
| **类型：** string | character vector |
| **值：** 数值标量 |
| **默认值：** `0` |

#### **Run at fixed time intervals** — 以固定速率执行模块的选项 `off`（默认）| `on`

此参数指定模块如何执行以及输出信号的采样时间。

- `off` — 模块在输入采样的延迟每经过一次时执行。输出信号具有固定次小采样时间。
- `on` — 模块以您使用 **Sample time** 参数指定的固定速率执行。输出信号具有您使用 **Sample time** 参数指定的采样时间。

当您选择 **Run at fixed time intervals** 时：

- 延迟信号值必须大于您为 **Sample time** 参数指定的值。
- 不是指定采样时间整数倍的延迟信号值将向下舍入到最接近的采样时间整数倍。例如，如果采样时间为 `0.1`，延迟信号值为 `0.68`，软件会将延迟舍入为 `0.6`。

#### 编程用法

|  |
| --- |
| **模块参数：** `RunAtFixedTimeIntervals` |
| **类型：** string | character vector |
| **值：** `'on'` | `'off'` |
| **默认值：** `'off'` |

#### **Sample time** — 输出采样时间 `0.1`（默认）| 标量

指定模块输出信号的采样时间。延迟信号值必须大于指定的采样时间。

当延迟信号值不是指定采样时间的整数倍时，软件会将延迟值向下舍入到最接近的、为采样时间整数倍的值。例如，如果采样时间为 `0.1`，延迟值为 `0.68`，软件会将延迟舍入为 `0.6`。

#### 依赖关系

要启用此参数，请选择 **Run at fixed time intervals**。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** string | character vector |
| **值：** 数值标量 |
| **默认值：** `0.1` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要从使用 Propagation Delay block 的模型生成代码，必须将 Propagation Delay block 配置为生成具有离散采样时间的输出。选择 **Run at fixed sample intervals**，并为 **Sample time** 参数指定离散速率。

Propagation Delay block 动态分配内存以存储输入信号和延迟信号采样。代码生成的目标必须支持动态内存分配。

### 版本历史

**在 R2022b 中引入**

## Libraries

Simulink / Discrete

## Description

The Propagation Delay block delays the current value for a signal into the
future by an amount specified by a delay signal. The Propagation Delay block is
well suited for implementing time delay in a discrete system.

On each simulation step *k*, the block samples the signal input
*U**k* and the delay input
*D**k*. The block output value
becomes the signal value after the delay time
*D**k* has elapsed from the
current simulation time
*T**k*.

*y*(*t*) =
*U**k* when *t* =
*T**k* +
*D**k*

At the start of the simulation, the block output value is the **Initial
output** block parameter value *Y*0. The
first sample of the delay signal *D*0 determines when
the block output changes from the **Initial output** value to the delayed
input signal values.

*y*(*t*) =
*Y*0 when *t* < *T*0 +
*D*0

When the simulation reaches the time *T*0 +
*D*0, the block output is determined by the signal and delay samples.

*y*(*t*) =
*U**k* when
*T**k* +
*D**k* ≤ *t*
≤ *T**k*+1 +
*D**k*+1,

where:

- *U**k* is the sample of the
  input signal taken at *t* =
  *T**k*.
- *D**k* is the sample of the
  delay signal taken at *t* =
  *T**k*.
- *T**k*+1 is the simulation
  time at which the next signal and delay samples were taken.
- *D**k*+1 is the delay
  sample taken at time
  *T**k*+1.

## Ports

### Input

### **u** — Signal to delay scalar

The Propagation Delay block supports real, scalar input signals
with continuous or discrete sample time. The input signal data type can be any
built-in type besides `int64` and `uint64`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **dt** — Delay signal scalar

The delay signal specifies the amount of delay to apply at each time step in the
simulation. You can use the Propagation Delay block to implement a
constant or variable delay.

The delay signal values must satisfy these constraints:

- The delay signal must contain scalar, real, finite, positive values larger
  than `128*eps`, which is the smallest time resolution the
  software supports.
- The output times for delayed input signal samples must increase
  monotonically.

  For example, suppose the delay signal value is `0.6` at
  simulation time `0` and the next simulation step occurs at time
  `0.5`. The delay signal at time `0.5` must
  be greater than `0.1` so that the delayed output time for the
  input signal sample *U*0.5 is greater
  than the output time for input signal sample
  *U*0 (`0.6`).
- When you select **Run at fixed time intervals**, the delay
  signal values must be greater than the value you specify for the
  **Sample time** parameter.

**Data Types:** `double`
### Output

### **y** — Delayed signal scalar

The output signal has the same data type as the input signal. By default, the
output signal has fixed-in-minor-step sample time. When you select **Run at
fixed time intervals**, the output signal has the discrete sample time you
specify for the **Sample time** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **Initial output** — Initial value for output signal `0` (default) | scalar

Specify the initial output signal value
*Y*0. The first sample of the delay signal
*D*0 determines when the block output changes
from the **Initial output** value to the delayed input signal
values.

*y*(*t*) =
*Y*0 when *t* < *T*0 +
*D*0

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialOutput` |
| **Type:** string | character vector |
| **Values:** numeric scalar |
| **Default:** `0` |

### **Run at fixed time intervals** — Option to execute block at fixed rate `off` (default) | `on`

This parameter specifies how the block executes and the sample time for the output signal.

- `off` — Block executes each time the delay for an input
  sample elapses. Output signal has fixed-in-minor sample time.
- `on` — Block executes at a fixed rate that you specify using
  the **Sample time** parameter. Output signal has the sample time
  you specify using the **Sample time** parameter.

When you select **Run at fixed time intervals**:

- The delay signal values must be greater than the value you specify for the
  **Sample time** parameter.
- Delay signal values that are not integer multiples of the specified sample
  time are rounded down to the nearest integer multiple of the sample time. For
  example, if the sample time is `0.1` and the delay signal value
  is `0.68`, the software rounds the delay to
  `0.6`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RunAtFixedTimeIntervals` |
| **Type:** string | character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **Sample time** — Output sample time `0.1` (default) | scalar

Specify the sample time for the block output signal. The delay signal values must be
greater than the specified sample time.

When the delay signal value is not an integer multiple of the specified sample time,
the software rounds the delay value down to the closest value that is an integer
multiple of the sample time. For example, if the sample time is `0.1`
and the delay value is `0.68`, the software rounds the delay to
`0.6`.

#### Dependencies

To enable this parameter, select **Run at fixed time
intervals**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** string | character vector |
| **Values:** numeric scalar |
| **Default:** `0.1` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

To generate code from a model that uses the Propagation Delay block, you
must configure the Propagation Delay block to produce an output with discrete
sample time. Select **Run at fixed sample intervals** and specify a
discrete rate for the **Sample time** parameter.

The Propagation Delay block dynamically allocates memory to store input
signal and delay signal samples. The target for code generation must support dynamic memory
allocation.

## Version History

**Introduced in R2022b**
