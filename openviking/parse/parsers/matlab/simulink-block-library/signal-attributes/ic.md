---
type: simulink-block
title: 'IC'
family: signal-attributes
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'ic'
---

# IC

Set initial value of signal

## 中文

设置信号的初始值

### 所属库

Simulink / Signal Attributes

### 描述

IC 模块设置其输入端口的信号的初始条件，例如，仿真开始时 (`tstart`) 信号的值。为此，该模块在仿真开始时输出指定的初始条件，而不管输入信号的实际值为何。此后，该模块输出输入信号的实际值。

IC 模块用于为环路中的代数状态变量提供初始估计值。有关详细信息，请参阅代数环概念。

#### 非零采样时间偏移量的行为

如果 IC 模块具有非零采样时间偏移量 (`toffset`)，IC 模块将在时间 `t` 输出其初始值，

```
t = n * tperiod + toffset
```

其中 `n` 是满足 `t ≥ tstart` 的最小整数。

即，IC 模块在模块以采样时间 `[tperiod, toffset]` 第一次执行时（可以在 `tstart` 之后）输出其初始值。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

输入信号，指定为标量、向量、矩阵或 N 维数组。模块将此信号的初始条件设置为您指定的**初始值**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量 | 矩阵 | N 维数组

输出信号以您指定的**初始值**开始，后跟输入信号的实际值。有关详细信息，请参阅非零采样时间偏移量的行为。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 参数

#### **初始值** — 初始值 `1` (默认) | 实数、有限标量、向量、矩阵或 N 维数组

将输入信号的初始值指定为有限实数值标量、向量、矩阵或 N 维数组。该值必须是标量，或者与输入信号具有相同的维度。

##### 编程用法

|  |
| --- |
| **模块参数**：`Value` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 | N 维数组 |
| **默认值：**`'1'` |

#### **采样时间(-1 表示继承)** — 采样之间的时间间隔 `-1` (默认) | 标量 | 向量

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

##### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时才可见。要了解详细信息，请参阅不建议设置采样时间的模块。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `"-1"` (默认) | scalar or vector in quotes |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产代码。涉及到嵌入式系统中常见的资源限制以及对速度和内存的限制。生成的代码可以包含内存的动态分配和释放、递归、额外的内存开销以及长短不等的执行时间。虽然代码在功能上有效并且在资源丰富的环境中通常可接受，但较小的嵌入式目标通常不能支持此类代码。通常情况下，模块会向适合生产代码的方向发展。因此，适合生产代码的模块仍然适用。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

#### R2023b: IC 模块行优先支持更新

IC 模块现在支持行优先数组布局的代码生成。

## Libraries

Simulink / Signal Attributes

## Description

The IC block sets the initial condition of the signal at its input port, for
example, the value of the signal at the simulation start time
(`tstart`). To do so, the block outputs
the specified initial condition when you start the simulation, regardless of the actual
value of the input signal. Thereafter, the block outputs the actual value of the input
signal.

The IC block is useful for providing an initial guess for the algebraic state
variables in a loop. For more information, see Algebraic Loop Concepts.

### Behavior for Nonzero Sample Time Offset

If an IC block has a nonzero sample time offset
(`toffset`), the IC
block outputs its initial value at time `t`,

```
t = n * tperiod + toffset
```

where `n` is the smallest integer such that `t ≥
tstart`.

That is, the IC block outputs its initial value the first-time blocks with
sample time `[tperiod,
toffset]` execute, which can be after
`tstart`.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

Input signal, specified as a scalar, vector, matrix, or N-D array. The
block sets the initial condition of this signal to the **Initial
value** you specify.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — Output signal scalar | vector | matrix | N-D array

Output signal provided as the **Initial value** you specify, followed
by the actual values of the input signal. See Behavior for Nonzero Sample Time Offset
for more information.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **Initial value** — Initial value `1` (default) | real, finite scalar, vector, matrix, or N-D array

Specify the initial value of the input signal as a finite, real-valued scalar, vector,
matrix, or N-D array. The value must be a scalar, or have the same
dimensions as the input signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Value` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix | N-D array |
| **Default:** `'1'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Dependencies

This parameter is visible only if you set it to a value other than
`-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar or vector in quotes |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code. Relates to resource limits and restrictions on speed
and memory often found in embedded systems. Generated code can contain dynamic
allocation and freeing of memory, recursion, additional memory overhead, and widely
varying execution times. While the code is functionally valid and generally
acceptable in resource-rich environments, smaller embedded targets often cannot
support such code. Usually, blocks evolve toward being suitable for production code.
Thus, blocks suitable for production code remain suitable.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2023b: IC Block Row-Major Support Update

The IC block now supports code generation for row-major array
layout.
