---
type: simulink-block
title: 'Pulse Generator'
family: sources
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'pulsegenerator'
---

# Pulse Generator

Generate square wave pulses at regular intervals

## 中文

按固定间隔生成方波脉冲

### 所属库

Simulink / Sources

### 描述

Pulse Generator 模块按固定间隔生成方波脉冲。此模块的波形参数**振幅**、**脉冲宽度**、**周期**和**相位延迟**确定了输出波形的形状。下图说明了每个参数对波形的影响。

Pulse Generator 模块可以生成任何实数数据类型的标量、向量或矩阵信号。要生成标量信号，请使用标量指定波形参数。要生成向量或矩阵信号，请分别使用向量或矩阵指定波形参数。波形参数的每个元素会影响输出信号的对应元素。例如，振幅向量参数的第一个元素确定输出脉冲向量的第一个元素的振幅。进行标量扩展后，所有波形参数必须具有相同的维度。输出的数据类型与**振幅**参数的数据类型相同。

可以在基于时间或基于采样的模式下生成模块输出，具体情况由**脉冲类型**参数确定。

#### 基于时间的模式

在基于时间的模式下，Simulink® 仅在输出实际发生变化时才计算模块输出。采用此方法，在仿真时间周期内为求取模块输出而进行的计算量较少。通过将**脉冲类型**参数设置为**基于时间**可以激活此模式。

此模块不支持产生常量输出信号的基于时间的配置。如果参数**脉冲宽度**和**周期**满足下列任一条件，Simulink 将返回错误：

Period​\*PulseWidth100=0Period​\*PulseWidth100=Period

根据脉冲波形特征，模块输出发生变化的时间间隔可能不同。由于这个原因，基于时间的 Pulse Generator 模块具有可变的采样时间。此类模块的采样时间颜色是褐色的（有关详细信息，请参阅查看采样时间信息）。

Simulink 不能使用定步长求解器来计算基于时间的脉冲发生器的输出。如果您为包含基于时间的脉冲发生器的模型指定定步长求解器，Simulink 将计算基于时间的脉冲发生器的固定采样时间。然后基于时间的脉冲发生器会以基于采样的模式进行仿真。

如果使用定步长求解器，而**脉冲类型**为`基于时间`，请选择步长，使周期、相位延迟和脉冲宽度（以秒为单位）等于求解器步长的整数倍。例如，假定周期为 `4` 秒，脉冲宽度为 `75%`（即 `3` 秒），相位延迟为 `1` 秒。在这种情况下，计算出的采样时间为 `1` 秒。因此，请选择定步长 `1` 或者能够将 `1` 整除的数字（例如 `0.25`）。要确保此设置，请在“配置参数”对话框的**求解器**窗格中选择 `auto`。

#### 基于采样的模式

在基于采样的模式下，模块按照您指定的固定时间间隔来计算其输出。通过将**脉冲类型**参数设置为**基于采样**可以激活此模式。

基于时间的模式和基于采样的模式之间有一个重要区别，前者的模块输出基于仿真时间，后者的模块输出只取决于仿真开始时间，与已用仿真时间无关。

在基于采样的模式下，此模块支持重置语义。例如，如果 Pulse Generator 模块在一个可重置子系统中，如果子系统触发了重置触发器，模块输出将重置为其初始条件。

### 端口

#### 输出

#### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

根据参数指定生成的方波脉冲信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### **脉冲类型** — 计算方法 **基于时间** (默认) | **基于采样**

计算方法，基于时间或基于采样生成此模块生成的方波类型。根据您选择的是基于时间还是基于采样，对话框中将出现某些参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`PulseType` |
| **类型**：字符向量 |
| **值**：`'Time based'` | `'Sample based'` |
| **默认值**：`'Time based'` |

#### **时间(t)** — 时间变量的来源 **使用仿真时间** (默认) | **使用外部信号**

指定是使用仿真时间还是外部信号作为输出脉冲时间变量值的来源。如果指定外部源，模块将显示一个输入端口用来连接该外部源。输出脉冲有所不同，如下所示：

- **使用仿真时间**：模块生成时间变量等于仿真时间的输出脉冲。
- **使用外部信号**：模块生成时间变量等于来自输入端口的值（可能不同于仿真时间）的输出脉冲。

##### 编程用法

|  |
| --- |
| **模块参数**：`TimeSource` |
| **类型**：字符向量 |
| **值**：`'Use simulation time'` | `'Use external signal'` |
| **默认值**：`'Use simulation time'` |

#### **振幅** — 信号振幅 `1` (默认) | `scalar`

指定信号振幅。

##### 编程用法

|  |
| --- |
| **模块参数**：`Amplitude` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'1'` |

#### **周期(秒)** — 脉冲周期 `10` (默认) | `scalar`

如果脉冲类型为基于时间，则以秒为单位指定脉冲周期。如果脉冲类型为基于采样，则以采样时间的数量指定脉冲周期。

##### 编程用法

|  |
| --- |
| **模块参数**：`Period` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'10'` |

#### **脉冲宽度** — 占空比 `5` (默认) | `scalar in the range [0,100]`

占空比，如果脉冲类型是基于时间，则指定为脉冲周期内有信号时的占比；如果基于采样，则是指定为有信号的采样次数。

##### 编程用法

|  |
| --- |
| **模块参数**：`PulseWidth` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'5'` |

#### **相位延迟(秒)** — 脉冲前延迟量 `0` (默认) | `scalar`

脉冲前延迟量，如果脉冲类型为基于时间，则以秒为单位指定生成脉冲之前的延迟时间；如果基于采样，则指定为生成脉冲之前的采样次数。

##### 编程用法

|  |
| --- |
| **模块参数**：`PhaseDelay` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

#### **采样时间** — 采样时间的长度 `0` (默认) | `scalar` | 向量

此模块的采样时间的长度（以秒为单位）。仅当模块的脉冲类型为基于采样时，才会显示此参数。请参阅 指定采样时间。

##### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'1'` |

#### **将向量参数解释为一维向量** — 将向量视为一维 `on` (默认) | `off`

如果**振幅**、**周期**、**脉冲宽度**或**相位延迟**参数的计算结果为包含 `N` 个元素的行向量或列向量，则选中此复选框将输出长度为 `N` 的向量。

- 如果任一值参数的计算结果为包含 `N` 个元素的行或列向量，则选中此复选框时，模块将输出长度为 `N` 的向量。例如，模块将输出 `1-by-N` 维或 `N-by-1` 维矩阵。
- 如果任一值参数的计算结果为包含 `N` 个元素的行或列向量，则清除此复选框时，模块不输出长度为 `N` 的向量。

有关如何使用此参数的详细信息，请参阅确定源模块的输出维度。

##### 编程用法

|  |
| --- |
| **模块参数**：`VectorParams1D` |
| **类型：**字符向量 |
| **值：**`'on' | 'off'` |
| **默认值：**`'on'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不能在触发子系统层次结构中使用。

当配置为基于采样运行时，这些模块不引用绝对时间。在基于时间的运行中，它们依赖于绝对时间。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

当**脉冲类型**参数设置为**基于采样**且**时间(t)** 参数设置为**使用仿真时间**时，此模块支持 HDL 代码生成。

**限制**

将 Pulse Generator 模块连接到 DUT 端口以在模型中用作源模块，但确保它不放置在 DUT 子系统内。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Sources

## Description

The Pulse Generator block generates square wave pulses at regular intervals.
The block waveform parameters, **Amplitude**, **Pulse
Width**, **Period**, and **Phase delay**,
determine the shape of the output waveform. The following diagram shows how each
parameter affects the waveform.

The Pulse Generator block can emit scalar, vector, or
matrix signals of any real data type. To emit a scalar signal, use scalars to specify
the waveform parameters. To emit a vector or matrix signal, use vectors or matrices,
respectively, to specify the waveform parameters. Each element of the waveform
parameters affects the corresponding element of the output signal. For example, the
first element of a vector amplitude parameter determines the amplitude of the first
element of a vector output pulse. All the waveform parameters must have the same
dimensions after scalar expansion. The data type of the output is the same as the data
type of the **Amplitude** parameter.

The block output can be generated in time-based or sample-based modes, determined by the
**Pulse type** parameter.

### Time-Based Mode

In time-based mode, Simulink® computes the block output only at times when the output actually
changes. This approach results in fewer computations for the block output over the
simulation time period. Activate this mode by setting the **Pulse
type** parameter to `Time based`.

The block does not support a time-based configuration that results in a constant
output signal. Simulink returns an error if the parameters **Pulse Width**
and **Period** satisfy either of these conditions:

Period​\*PulseWidth100=0Period​\*PulseWidth100=Period

Depending on the pulse waveform characteristics, the intervals between changes in
the block output can vary. For this reason, a time-based Pulse Generator block has a
variable sample time. The sample time color of such blocks is brown (see View Sample Time Information
for more information).

Simulink cannot use a fixed-step solver to compute the output of a time-based
pulse generator. If you specify a fixed-step solver for models that contain
time-based pulse generators, Simulink computes a fixed sample time for the time-based pulse generators. Then
the time-based pulse generators simulate as sample based.

If you use a fixed-step solver and the **Pulse type** is `Time based`, choose the step size such that the
period, phase delay, and pulse width (in seconds) are integer multiples of the
solver step size. For example, suppose that the period is `4`
seconds, the pulse width is `75%` (that is, `3`
s), and the phase delay is `1` s. In this case, the computed sample
time is `1` s. Therefore, choose a fixed-step size of
`1` or a number that divides `1` exactly (for
example, `0.25`). To ensure this setting, select
`auto` on the **Solver** pane of the
Configuration Parameters dialog box.

### Sample-Based Mode

In sample-based mode, the block computes its outputs at fixed intervals that you
specify. Activate this mode by setting the **Pulse type** parameter
to `Sample based`.

An important difference between the time-based and sample-based modes is that in time-based
mode, the block output is based on simulation time, and in sample-based mode, the
block output depends only on the simulation start, regardless of elapsed simulation
time.

This block supports reset semantics in sample-based mode. For example, if a Pulse
Generator block is in a resettable subsystem that hits a reset trigger,
the block output resets to its initial condition.

## Ports

### Output

### **Port\_1** — Output signal scalar | vector | matrix

Generated square wave pulse signal specified by the parameters.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Pulse type** — Computational technique `Time based` (default) | `Sample based`

Computational technique to generate the type of square wave that this
block generates, either time- or sample-based. Some parameters in the dialog
box appear depending on whether you select time-based or
sample-based.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PulseType` |
| **Type**: character vector |
| **Values**: `'Time based'` | `'Sample based'` |
| **Default**: `'Time based'` |

### **Time (t)** — Source of time variable `Use simulation time` (default) | `Use external signal`

Specifies whether to use simulation time or an external signal as the
source of values for the output pulse's time variable. If you specify an
external source, the block displays an input port for connecting the source.
The output pulse differs as follows:

- `Use simulation time`: The block
  generates an output pulse where the time variable equals the
  simulation time.
- `Use external signal`: The block
  generates an output pulse where the time variable equals the value
  from the input port, which can differ from the simulation
  time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TimeSource` |
| **Type**: character vector |
| **Values**: `'Use simulation time'` | `'Use external signal'` |
| **Default**: `'Use simulation time'` |

### **Amplitude** — Signal amplitude `1` (default) | `scalar`

Specify the amplitude of the signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Amplitude` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'1'` |

### **Period (secs)** — Pulse period `10` (default) | `scalar`

Pulse period specified in seconds if the pulse type is time-based. If the pulse type is
sample-based, then the period is specified as the number of sample
times.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Period` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'10'` |

### **Pulse width** — Duty cycle `5` (default) | `scalar in the range [0,100]`

Duty cycle specified as the percentage of the pulse period that the signal is on if
time-based or as number of sample times if sample-based.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PulseWidth` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'5'` |

### **Phase delay (secs)** — Delay before pulse `0` (default) | `scalar`

Delay before the pulse is generated, specified in seconds, if the pulse type is
time-based or as number of sample times if the pulse type is
sample-based.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PhaseDelay` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'0'` |

### **Sample time** — Length of sample time `0` (default) | `scalar` | vector

Length of the sample time for this block in seconds. This parameter appears only if the
block's pulse type is sample-based. See Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'1'` |

### **Interpret vector parameters as 1-D** — Treat vectors as 1-D `on` (default) | `off`

Select this check box to output a vector of length `N` if
the **Amplitude**, **Period**,
**Pulse width**, or **Phase delay**
parameter evaluates to an `N`-element row or column
vector.

- When you select this check box, the block outputs a vector of
  length `N` if any of the value parameters evaluate
  to an `N`-element row or column vector. For
  example, the block outputs a matrix of dimension
  `1-by-N` or `N-by-1`.
- When you clear this check box, the block does not output a vector
  of length `N` if any of the value parameters
  evaluate to an `N`-element row or column
  vector.

For more information on how this parameter is used, see Determine the Output Dimensions of Source Blocks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VectorParams1D` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Cannot be used inside a triggered subsystem hierarchy.

These blocks do not reference absolute time when configured for sample-based operation. In
time-based operation, they depend on absolute time.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL code generation is supported for this block with the **Pulse
type** parameter set to `Sample based` and the
**Time (t)** parameter set to `Use simulation
time`.

**Restrictions**

Connect the Pulse Generator block to the DUT ports to use it as
a source block in your model, but ensure it is not placed inside the DUT
subsystem.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
