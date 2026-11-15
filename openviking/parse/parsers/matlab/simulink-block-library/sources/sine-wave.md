---
type: simulink-block
title: 'Sine Wave'
family: sources
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'sinewave'
---

# Sine Wave

Generate sine wave, using simulation time as time source

## 中文

使用仿真时间作为时间源以生成正弦波

### 所属库

Simulink / Sources

### 描述

Sine Wave 模块输出正弦曲线波形。此模块可在基于时间或基于采样的模式下运行。

**注意**

此模块相当于 Math Operations 模块库中的 Sine Wave Function 模块。如果您在模块对话框中为**时间**参数选择了**使用外部信号**，您将获得 Sine Wave Function 模块。

#### 基于时间的模式

该模块可计算输出波形。

y=amplitude×sin(frequency×time+phase)+bias.

在基于时间的模式下，**采样时间**参数的值确定模块是在连续模式还是离散模式下运行。

- `0`（默认值）将使得模块在连续模式下运行。
- `>0` 将使得模块在离散模式下运行。

有关详细信息，请参阅指定采样时间。

**连续模式下的模块行为**

在连续模式下运行时，由于随着时间变得非常大，导致精度损失，因此 Sine Wave 模块可能会变得不准确。

**离散模式下的模块行为**

如果**采样时间**参数的值大于零，将会导致模块好像在驱动一个采样时间设置为该值的 Zero-Order Hold 模块。

通过这种方式，您可以构建具有纯离散正弦波源的模型，而不是混合了连续/离散系统的模型。混合系统本质上更复杂，因此需要更长的仿真时间。

在离散模式下，此模块使用微分增量算法，而不是基于绝对时间的算法。因此，此模块对于要在无限长时间内运行的模块（如振动或疲劳测试）非常有用。

微分增量算法根据在上一采样时间计算出的值来计算正弦值。此方法使用下列三角恒等式：

sin(t+Δt)=sin(t)cos(Δt)+sin(Δt)cos(t)cos(t+Δt)=cos(t)cos(Δt)−sin(t)sin(Δt)

采用矩阵形式，这些恒等式表示为：

[sin(t+Δt)cos(t+Δt)]=[cos(Δt)sin(Δt)−sin(Δt)cos(Δt)][sin(t)cos(t)]

由于 Δ*t* 是常量，所以下列表达式是常量：

[cos(Δt)sin(Δt)−sin(Δt)cos(Δt)]

因此，问题就变为一种矩阵乘法，用 sin(t) 的值乘以一个常量矩阵以得出 sin(t+Δt)。

离散模式只能减少但不能消除舍入误差的累积。发生累积是因为模块在每个时间步的输出的计算都取决于上一个时间步的输出值。

**离散模式下的舍入误差的处理方法**

要处理 Sine Wave block 模块在基于时间的离散模式下运行时产生的舍入误差，请使用下列方法之一。

| 方法 | 理由 |
| --- | --- |
| 在 Sine Wave 模块的直接下游插入一个 Saturation 模块。 | 通过为 Sine Wave 模块输出设置饱和界限，可以避免由于舍入误差累积而出现的过冲。 |
| 将 Sine Wave 模块设置为使用 `sin()` 数学模块库函数来计算模块输出。  1. 在 Sine Wave 模块对话框中，将**时间**设置为**使用外部信号**，这样模块图标上将出现一个输入端口。 2. 使用 Digital Clock 模块将一个时钟信号连接到此输入端口上。 3. 将时钟信号的采样时间设置为 Sine Wave 模块的采样时间。 | `sin()` 数学模块库函数*单独*计算每个时间步的模块输出，从而可以避免舍入误差的累积。 |

#### 基于采样的模式

基于采样的模式使用以下公式计算 Sine Wave 模块的输出。

y=Asin(2π(k+o)/p)+b

- *A* 是正弦波的振幅。
- *p* 是每个正弦波周期内的时间采样数。
- *k* 为重复的整数值，范围从 0 到 *p*–1。
- *o* 是信号的偏移量（相位偏移）。
- *b* 是信号偏差。

在此模式下，Simulink® 将第一个时间步的 *k* 设置为等于 `0`，并使用该公式计算模块输出。在下一个时间步，Simulink 递增 *k*，然后重新计算模块输出。当 *k* 达到 *p* 时，Simulink 在计算模块输出之前将 *k* 重置为 `0`。此过程会一直继续，直到仿真结束。

在计算给定时间步的模块输出时，基于采样的方法不依赖于上一个时间步的输出。因此，这种模式可以避免舍入误差的累积。基于采样的模式还支持在提供语义的子系统中重置语义。例如，如果 Sine Wave 模块在一个可重置子系统中，子系统收到一个重置触发事件，重复的整数 `k` 将重置，模块输出将重置为其初始条件。

### 端口

#### 输出

#### **Port\_1** — 正弦波输出信号 标量 | 向量

基于模块参数值创建的正弦波输出信号。

**数据类型:** `double`

### 参数

#### **正弦类型** — 正弦波的类型 **基于时间** (默认) | **基于采样**

指定此模块生成的正弦波的类型。根据您选择的是基于时间还是基于采样，对话框中将出现某些参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`SineType` |
| **类型**：字符向量 |
| **值**：`'Time based'` | `'Sample based'` |
| **默认值**：`'Time based'` |

#### **时间(t)** — 时间变量的来源 **使用仿真时间** (默认) | **使用外部信号**

指定是使用仿真时间还是外部源作为时间变量值的来源。如果指定外部时间源，模块将为该时间源创建一个输入端口。选择外部时间源时，该模块与 Sine Wave Function 模块相同。

##### 编程用法

|  |
| --- |
| **模块参数**：`TimeSource` |
| **类型**：字符向量 |
| **值**：`'Use simulation time'` | `'Use external signal'` |
| **默认值**：`'Use simulation time'` |

#### **振幅** — 正弦波的振幅 `1` (默认) | 标量 | 向量

指定正弦波输出信号的振幅。

##### 编程用法

|  |
| --- |
| **模块参数**：`Amplitude` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'1'` |

#### **偏置** — 添加到正弦波的常量 `0` (默认) | 标量 | 向量

指定为了生成输出在正弦中添加的常量值。

##### 编程用法

|  |
| --- |
| **模块参数**：`Bias` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

#### **频率(弧度/秒)** — 正弦波的频率 `1` (默认) | 标量 | 向量

指定频率，以 rad/sec 为单位。

##### 依赖关系

要启用此参数，请将**正弦类型**设置为**基于时间**。

##### 编程用法

|  |
| --- |
| **模块参数**：`Frequency` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'1'` |

#### **相位(弧度)** — 正弦波的相移 `0` (默认) | 标量 | 向量

指定正弦波的相移。

如果将**时间(t)** 设置为**使用仿真时间**，则不能将此参数配置为在生成的代码中显示为可调全局变量。例如，如果将**默认参数行为**设置为**可调**或将某个存储类应用于 `Simulink.Parameter` 对象，则**相位**参数不会在生成的代码中显示为可调全局变量。

要生成代码以便在执行期间可以调整相位，请将**时间(t)** 设置为**使用外部信号**。您可以提供您自己的时间输入信号，或使用 Digital Clock 模块生成时间信号。有关示例，请参阅Tune Phase Parameter of Sine Wave Block During Code Execution (Simulink Coder)。

##### 依赖关系

要启用此参数，请将**正弦类型**设置为**基于时间**。

##### 编程用法

|  |
| --- |
| **模块参数**：`Phase` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

#### **每周期采样数** — 每周期采样数 `0` (默认) | `integer scalar` | `integer vector`

指定每个周期的采样数。

##### 依赖关系

要启用此参数，请将**正弦类型**设置为**基于采样**。

##### 编程用法

|  |
| --- |
| **模块参数**：`Samples` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'10'` |

#### **偏移量(采样数)** — 偏移量（采样时间数） `0` (默认) | `integer scalar` | `integer vector`

以采样次数为单位指定偏移量（离散相位偏移）。

##### 依赖关系

要启用此参数，请将**正弦类型**设置为**基于采样**。

##### 编程用法

|  |
| --- |
| **模块参数**：`Offset` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

#### **采样时间** — 采样周期 `0` (默认) | 标量 | 向量

以秒为单位指定采样周期。默认值为 `0`。如果正弦类型是基于采样，则采样时间必须大于 0。请参阅 指定采样时间。

##### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

#### **将向量参数解释为一维向量** — 单行或单列矩阵的输出维度 `off` (默认) | `on`

指定当其他参数是单行和单列矩阵时输出维度为一维向量信号。如果不选中此框，模块将输出与数值参数具有相同维数的信号。请参阅确定源模块的输出维度。当利用外部信号指定时间时，此参数不可用。在这种情况下，如果数值参数是列或行矩阵值，输出则为 1 维向量。

##### 编程用法

|  |
| --- |
| **模块参数**：`VectorParams1D` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

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

位于触发子系统层次结构中时取决于绝对时间。当配置为基于采样运行时，这些模块不引用绝对时间。在基于时间的运行中，它们依赖于绝对时间。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

此模块的 HDL 代码生成支持：

- 基于采样的正弦波。
- **使用仿真时间**作为时间变量值的来源。
- 参数**振幅**、**偏置**、**每周期性采样数**、**偏移量(采样数)** 和**采样时间**的标量值。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

默认情况下，以下 HDL 模块属性可用。

| 通用 | |
| --- | --- |
| **MapToRAM** | 将查找表映射到 RAM。默认值为 **inherit**。请参阅MapToRAM (HDL Coder)。 |

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Sources

## Description

The Sine Wave block outputs a sinusoidal waveform. The block can operate in time-based
or sample-based mode.

**Note**

This block is the same as the Sine Wave Function block that
appears in the Math Operations library. If you select `Use external
signal` for the **Time** parameter in the block
dialog box, you get the Sine Wave Function block.

### Time-Based Mode

The block calculates the output waveform.

y=amplitude×sin(frequency×time+phase)+bias.

In time-based mode, the value of the **Sample time** parameter determines
whether the block operates in continuous mode or discrete mode.

- `0` (the default) causes the block to operate in
  continuous mode.
- `>0` causes the block to operate in discrete
  mode.

For more information, see Specify Sample Time.

**Block Behavior in Continuous Mode**

When operating in continuous mode, the Sine Wave block can become
inaccurate due to loss of precision as time becomes very large.

**Block Behavior in Discrete Mode**

A **Sample time** parameter value greater than zero causes the block to
behave as if it were driving a Zero-Order Hold block whose sample
time is set to that value.

This way, you can build models with sine wave sources that are purely discrete, rather
than models that are hybrid continuous/discrete systems. Hybrid systems are
inherently more complex and as a result take more time to simulate.

In discrete mode, this block uses a differential incremental algorithm instead
of one based on absolute time. As a result, the block can be useful in models
intended to run for an indefinite length of time, such as in vibration or
fatigue testing.

The differential incremental algorithm computes the sine based on the value
computed at the previous sample time. This method uses the following
trigonometric identities:

sin(t+Δt)=sin(t)cos(Δt)+sin(Δt)cos(t)cos(t+Δt)=cos(t)cos(Δt)−sin(t)sin(Δt)

In matrix form, these identities are:

[sin(t+Δt)cos(t+Δt)]=[cos(Δt)sin(Δt)−sin(Δt)cos(Δt)][sin(t)cos(t)]

Because Δ*t* is constant, the following expression is a constant:

[cos(Δt)sin(Δt)−sin(Δt)cos(Δt)]

Therefore, the problem becomes one of a matrix multiplication of the value of sin(t) by a constant matrix to obtain sin(t+Δt).

Discrete mode reduces but does not eliminate the accumulation of round-off errors. This
accumulation can happen because computation of the block output at each time
step depends on the value of the output at the previous time step.

**Methods to Handle Round-Off Errors in Discrete Mode**

To handle round-off errors when the Sine Wave block operates in time-based
discrete mode, use one of these methods.

| Method | Rationale |
| --- | --- |
| Insert a Saturation block directly downstream of the Sine Wave block. | By setting saturation limits on the Sine Wave block output, you can remove overshoot due to accumulation of round-off errors. |
| Set up the Sine Wave block to use the `sin()` math library function to calculate block output.  1. On the Sine Wave block dialog box, set    **Time** to `Use    external signal` so that an input    port appears on the block icon. 2. Connect a clock signal to this input port using a    Digital    Clock block. 3. Set the sample time of the clock signal to the    sample time of the Sine Wave block. | The `sin()` math library function computes block output at each time step *independently* of output values from other time steps, preventing the accumulation of round-off errors. |

### Sample-Based Mode

Sample-based mode uses this formula to compute the output of the Sine Wave
block.

y=Asin(2π(k+o)/p)+b

- *A* is the amplitude of the sine wave.
- *p* is the number of time samples per sine wave
  period.
- *k* is a repeating integer value that ranges from 0 to
  *p*–1.
- *o* is the offset (phase shift) of the signal.
- *b* is the signal bias.

In this mode, Simulink® sets *k* equal to `0` at the first
time step and computes the block output, using the formula. At the next time step,
Simulink increments *k* and recomputes the output of the
block. When *k* reaches *p*, Simulink resets *k* to `0` before computing
the block output. This process continues until the end of the simulation.

The sample-based method of computing block output at a given time step does not depend on
the output of the previous time steps. Therefore, this mode avoids the accumulation
of round-off errors. Sample-based mode supports reset semantics in subsystems that
offer it. For example, if a Sine Wave block is in a resettable
subsystem that receives a reset trigger, the repeating integer `k`
resets and the block output resets to its initial condition.

## Ports

### Output

### **Port\_1** — Sine wave output signal scalar | vector

Output sine wave signal created based on the block parameter
values.

**Data Types:** `double`

## Parameters

### **Sine type** — Type of sine wave `Time based` (default) | `Sample based`

Specify the type of sine wave that this block generates. Some parameters in the dialog
box appear depending on whether you select time-based or
sample-based.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SineType` |
| **Type**: character vector |
| **Values**: `'Time based'` | `'Sample based'` |
| **Default**: `'Time based'` |

### **Time (t)** — Source of time variable `Use simulation time` (default) | `Use external signal`

Specify whether to use simulation time as the source of values for the
time variable, or an external source. If you specify an external time
source, the block creates an input port for the time source. When you select
an external time source, the block is the same as the Sine Wave
Function block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TimeSource` |
| **Type**: character vector |
| **Values**: `'Use simulation time'` | `'Use external signal'` |
| **Default**: `'Use simulation time'` |

### **Amplitude** — Amplitude of the sine wave `1` (default) | scalar | vector

Specify the amplitude of the output sine wave signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Amplitude` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'1'` |

### **Bias** — Constant added to sine wave `0` (default) | scalar | vector

Specify the constant value added to the sine to produce the output.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Bias` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'0'` |

### **Frequency (rad/sec)** — Frequency of sine wave `1` (default) | scalar | vector

Specify the frequency, in rad/sec.

#### Dependencies

To enable this parameter, set **Sine type** to
`Time based`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Frequency` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'1'` |

### **Phase (rad)** — Phase shift of sine wave `0` (default) | scalar | vector

Specify the phase shift of the sine wave.

You cannot configure this parameter to appear in the generated code as a
tunable global variable if you set **Time (t)** to
`Use simulation time`. For example, if you set
**Default parameter behavior** to
`Tunable` or apply a storage class to a
`Simulink.Parameter` object, the
**Phase** parameter does not appear in the generated
code as a tunable global variable.

To generate code so that you can tune the phase during execution, set
**Time (t)** to `Use external
signal`. You can provide your own time input signal or use
a Digital Clock block to generate the time signal. For an
example, see Tune Phase Parameter of Sine Wave Block During Code Execution (Simulink Coder).

#### Dependencies

To enable this parameter, set **Sine type** to
`Time based`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Phase` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'0'` |

### **Samples per period** — Samples per period `0` (default) | `integer scalar` | `integer vector`

Specify the number of samples per period.

#### Dependencies

To enable this parameter, set **Sine type** to
`Sample based`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Samples` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'10'` |

### **Number of offset samples** — Offset in number of sample times `0` (default) | `integer scalar` | `integer vector`

Specify the offset (discrete phase shift) in number of sample times.

#### Dependencies

To enable this parameter, set **Sine type** to
`Sample based`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Offset` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'0'` |

### **Sample time** — Sample period `0` (default) | scalar | vector

Specify the sample period in seconds. The default is `0`. If the sine
type is sample-based, the sample time must be greater than 0. See Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Value**: scalar |
| **Default**: `'0'` |

### **Interpret vector parameters as 1-D** — Output dimensions for one-row or one-column matrices `off` (default) | `on`

Specify the output dimensions to be a 1-D vector signal when other parameters are one-row
and one-column matrices. If you do not select this box, the block outputs a
signal of the same dimensionality as the numeric parameters. See Determine the Output Dimensions of Source Blocks. This
parameter is not available when an external signal specifies time. In this
case, if numeric parameters are column or row matrix values, the output is a
1-D vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `VectorParams1D` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'on'` |

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

Depends on absolute time when placed inside a triggered subsystem hierarchy. These blocks
do not reference absolute time when configured for sample-based operation. In
time-based operation, they depend on absolute time.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL code generation from this block supports:

- Sample-based sine waves.
- `Use simulation time` as the source of values
  for the time variable.
- Scalar values for parameters **Amplitude**,
  **Bias**, **Samples per period**,
  **Number of offset samples**, and **Sample
  time**.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

By default, the following HDL block property is available.

| General | |
| --- | --- |
| **MapToRAM** | Map lookup tables to RAM. The default is `inherit`. See MapToRAM (HDL Coder). |

## Version History

**Introduced before R2006a**
