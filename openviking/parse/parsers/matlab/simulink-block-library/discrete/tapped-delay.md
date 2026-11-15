---
type: simulink-block
title: 'Tapped Delay'
family: discrete
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'tappeddelay'
---

# Tapped Delay

Delay scalar signal multiple sample periods and output all delayed versions

## 中文

将标量信号延迟多个采样周期并输出所有延迟版本

### 所属库

Simulink / Discrete HDL Coder / Discrete

### 描述

Tapped Delay 模块将输入延迟指定数量的采样周期，并为每个延迟提供一个输出信号。例如，当您为**延迟数**指定 `4` 且**输出向量排序**为**最早**时，该模块提供四个输出 - 第一个输出延迟四个采样周期，第二个输出延迟三个采样周期，依此类推。使用此模块可以适时离散化信号，或以不同的速率对信号进行重采样。

该模块接受一个标量输入，并生成包含每个增量延迟的数据的输出向量。使用**输出向量排序**参数指定输出向量中的延迟信号顺序：

- **最早**输出向量以最早的延迟版本开始，以最新的延迟版本结束的顺序。
- **最近**输出向量以最新的延迟版本开始，以最早的延迟版本结束的顺序。

通过**初始条件**参数指定第一个采样周期的输出向量。谨慎选择此参数可以减少不需要的输出行为。

通过**采样时间**参数指定采样之间的时间间隔。通过**延迟数**参数指定延迟数量。值 `-1` 指示模块通过反向传播来继承延迟数量。每个延迟相当于 Unit Delay 模块表示的 z-1 离散时间运算符。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量

要延迟的输入信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持:** 是
#### 输出

#### **Port\_1** — 输入信号的延迟版本 标量 | 向量

延迟的输入信号的所有版本。使用**输出向量排序**参数指定输出向量中延迟信号的顺序。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 参数

#### **初始条件** — 初始输出 `0.0` (默认) | 标量

指定仿真的初始输出。**初始条件**参数通过舍入到最邻近整数及饱和处理从双精度脱机转换为输入数据类型。

##### 限制

此模块的初始条件不能为 `inf` 或 `NaN`。

##### 编程用法

|  |
| --- |
| **模块参数**：`vinit` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'0.0'` |

#### **采样时间** — 采样之间的时间间隔 `-1` (默认) | 标量 | 向量

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

##### 编程用法

|  |
| --- |
| **模块参数**：`samptime` |
| **类型：**字符向量 |
| **值：**标量 | 向量 |
| **默认值：**`'-1'` |

#### **延迟数** — 离散时间运算符的数量 `4` (默认) | 正标量 | `-1`（表示继承）

将离散时间运算符的数量指定为正标量，或指定 `-1` 表示继承。

##### 编程用法

|  |
| --- |
| **模块参数**：`NumDelays` |
| **类型：**字符向量 |
| **值：**正标量 | `-1`（继承） |
| **默认值：**`'4'` |

#### **输出向量排序** — 输出的顺序 **最早** (默认) | **最近**

指定先输出最早的延迟版本还是最新的延迟版本。

##### 编程用法

|  |
| --- |
| **模块参数**：`DelayOrder` |
| **类型：**字符向量 |
| **值**：`'Oldest' | 'Newest'` |
| **默认值：**`'Oldest'` |

#### **将当前输入包含在输出向量中** — 将当前输入包含在输出向量中 `off` (默认) | `on`

选中此复选框可将当前输入包括在输出向量中。

##### 编程用法

|  |
| --- |
| **模块参数**：`includeCurrent` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

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

The Tapped Delay block delays an input by the specified number of sample
periods and provides an output signal for each delay. For example, when you specify
`4` for **Number of delays** and **Order
output starting with** is `Oldest`, the block
provides four outputs — the first delayed by four sample periods, the second delayed by
three, and so on. Use this block to discretize a signal in time or resample a signal at
a different rate.

The block accepts one scalar input and generates an output vector that contains data for
each incremental delay. Specify the order of the delayed signals in the output vector
with the **Order output vector starting with** parameter:

- `Oldest` orders the output vector starting with the oldest delay version and ending with the newest delay version.
- `Newest` orders the output vector starting with the newest delay version and ending with the oldest delay version.

Specify the output vector for the first sampling period with the **Initial
condition** parameter. Careful selection of this parameter can mitigate
unwanted output behavior.

Specify the time between samples with the **Sample time** parameter.
Specify the number of delays with the **Number of delays** parameter. A
value of `-1` instructs the block to inherit the number of delays by
backpropagation. Each delay is equivalent to the z-1
discrete-time operator, which the Unit Delay block represents.

## Ports

### Input

### **Port\_1** — Input signal scalar

Input signal to delay.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Delayed versions of input signal scalar | vector

All versions of the delayed input signal. Use the **Order
output vector starting with** parameter to specify the
order of delayed signals in the output vector.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### **Initial condition** — Initial output `0.0` (default) | scalar

Specify the initial output of the simulation. The **Initial
condition** parameter is converted from a double to the input
data type offline using round-to-nearest and saturation.

#### Limitations

The initial condition of this block cannot be `inf`
or `NaN`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `vinit` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0.0'` |

### **Sample time** — Time between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set
this parameter to `-1`. For more information, see Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `samptime` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'-1'` |

### **Number of delays** — Number of discrete-time operators `4` (default) | positive scalar | `-1` (for inherited)

Specify the number of discrete-time operators as a positive scalar, or
`-1` for inherited.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumDelays` |
| **Type:** character vector |
| **Values:** positive scalar | `-1` (inherited) |
| **Default:** `'4'` |

### **Order output vector starting with** — Order of output `Oldest` (default) | `Newest`

Specify whether to output the oldest delay version first, or the newest
delay version first.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DelayOrder` |
| **Type:** character vector |
| **Values:** `'Oldest' | 'Newest'` |
| **Default:** `'Oldest'` |

### **Include current input in output vector** — Include current input in output vector `off` (default) | `on`

Select this check box to include the current input in the output
vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `includeCurrent` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

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
