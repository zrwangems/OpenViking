---
type: simulink-block
title: 'Signal Generator'
family: sources
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'signalgenerator'
---

# Signal Generator

Generate various waveforms

## 中文

生成各种波形

### 所属库

Simulink / Sources

### 描述

#### 支持的运算

Signal Generator 模块可以产生四种不同波形：

- 正弦波
- 方波
- 锯齿波
- 随机

您可以使用 hertz 或 rad/sec 为单位表示信号参数。使用默认参数值，可以获得下列波形之一：

| 波形 | 波形输出 |
| --- | --- |
| 正弦波 |  |
| 方波 |  |
| 锯齿波 |  |
| 随机波 |  |

为**振幅**参数指定负值将产生 180 度相移。您可以通过多种方式生成除 180 度之外的相移波。例如，您可以将 Clock 模块信号连接到 MATLAB Function 模块，并为特定波形编写方程。

您可以在仿真过程中更改 Signal Generator 模块的输出设置，以快速确定系统对不同类型输入的响应。

**振幅**和**频率**参数确定输出信号的振幅和频率。在进行标量扩展后，这两个参数必须具有相同的维度。如果清除**将向量参数解释为一维向量**复选框，模块将输出与**振幅**和**频率**参数（标量扩展后）具有相同维度的信号。如果选中**将向量参数解释为一维向量**复选框，若**振幅**和**频率**参数是行或列向量，即单行或单列二维数组，模块将输出向量（一维）信号。否则，模块将输出与这两个参数具有相同维度的信号。

#### 求解器注意事项

如果您的模型使用定步长求解器，Simulink® 将对整个仿真使用相同的步长。在这种情况下，Signal Generator 模块输出将提供理想波形的均匀采样表示。

如果您的模型使用变步长求解器，Simulink 可能会在仿真过程中使用不同的步长。在这种情况下，Signal Generator 模块输出并不总是提供理想波形的均匀采样表示。为了确保模块输出是均匀采样的表示，请直接在 Signal Generator 模块的下游添加一个 Hit Crossing 模块。以下模型显示了具有和没有 Hit Crossing 模块时 Signal Generator 模块输出的区别。

| 使用变步长求解器的模型 | Signal Generator 模块输出 |
| --- | --- |
|  | Signal Generator with sawtooth wave and variable-step solver |
|  | Signal Generator with sawtooth wave and variable-step solver and Hit Cross |

### 端口

#### 输出

#### **Port\_1** — 生成的输出信号 标量 | 向量 | 矩阵

输出信号指定为下列波形之一。

- 正弦波
- 方波
- 锯齿波
- 随机

**数据类型:** `double`

### 参数

#### **波形** — 要生成的波形 **正弦** (默认) | **方波** | **锯齿波** | **随机**

指定波形。

##### 编程用法

|  |
| --- |
| **模块参数**：`WaveForm` |
| **类型**：字符向量 |
| **值**：`'sine'` | `'square'` | `'sawtooth'` | `'random'` |
| **默认值**：`'sine'` |

#### **时间(t)** — 时间变量的来源 **使用仿真时间** (默认) | **使用外部信号**

指定是使用仿真时间还是外部信号作为波形时间变量值的来源。如果指定外部源，模块将显示一个输入端口用来连接该外部源。

##### 编程用法

|  |
| --- |
| **模块参数**：`TimeSource` |
| **类型**：字符向量 |
| **值**：`'Use simulation time'` | `'Use external signal'` |
| **默认值**：`'Use simulation time'` |

#### **振幅** — 信号振幅 `1` (默认) | 标量 | 向量 | 矩阵

指定生成的波形的振幅。

##### 编程用法

|  |
| --- |
| **模块参数**：`Amplitude` |
| **类型**：字符向量 |
| **值**：实数标量 |
| **默认值**：`'1'` |

#### **频率** — 信号频率 `1` (默认) | 标量 | 向量 | 矩阵

指定生成的波形的频率。

##### 编程用法

|  |
| --- |
| **模块参数**：`Frequency` |
| **类型**：字符向量 |
| **值**：实数标量 |
| **默认值**：`'1'` |

#### **单位** — 信号单位 **rad/sec** (默认) | **Hertz**

指定信号单位是 **Hertz** 还是 **rad/sec**。

##### 编程用法

|  |
| --- |
| **模块参数**：`Units` |
| **类型**：字符向量 |
| **值**：`'rad/sec'` | `'Hertz'` |
| **默认值**：`'rad/sec'` |

#### **将向量参数解释为一维向量** — 将向量视为一维 `on` (默认) | `off`

如果**常量值**参数的计算结果为包含 `N` 个元素的行或列向量，选中此复选框将输出长度为 `N` 的向量。

- 如果**常量值**参数的计算结果为包含 `N` 个元素的行或列向量，则选中此复选框时，模块将输出长度为 `N` 的向量。例如，模块将输出 `1-by-N` 维或 `N-by-1` 维矩阵。
- 如果**常量值**参数的计算结果为包含 `N` 个元素的行或列向量，则清除此复选框时，模块不输出长度为 `N` 的向量。

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
| **数据类型** | `double` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不能在触发子系统层次结构中使用。

当配置为基于采样运行时，这些模块不引用绝对时间。在基于时间的运行中，它们依赖于绝对时间。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**限制**

将 Signal Generator 模块连接到 DUT 端口以在模型中用作源模块，但确保它不放置在 DUT 子系统内。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Sources

## Description

### Supported Operations

The Signal Generator block can produce one of four different waveforms:

- sine
- square
- sawtooth
- random

You can express signal parameters in hertz or radians per second.
Using default parameter values, you get one of the following waveforms:

| Waveform | Scope Output |
| --- | --- |
| Sine wave |  |
| Square wave |  |
| Sawtooth wave |  |
| Random wave |  |

A negative **Amplitude** parameter value causes a 180-degree phase shift.
You can generate a phase-shifted wave at other than 180 degrees in many ways. For
example, you can connect a Clock block signal to a MATLAB Function block and write the
equation for the specific wave.

You can vary the output settings of the Signal Generator block while a
simulation is in progress to determine quickly the response of a system to different
types of inputs.

The **Amplitude** and **Frequency** parameters determine
the amplitude and frequency of the output signal. The parameters must be of the same
dimensions after scalar expansion. If you clear the **Interpret vector
parameters as 1-D** check box, the block outputs a signal of the same
dimensions as the **Amplitude** and **Frequency**
parameters (after scalar expansion). If you select the **Interpret vector
parameters as 1-D** check box, the block outputs a vector (1-D) signal
if the **Amplitude** and **Frequency** parameters
are row or column vectors, that is, single-row or column 2-D arrays. Otherwise, the
block outputs a signal of the same dimensions as the parameters.

### Solver Considerations

If your model uses a fixed-step solver, Simulink® uses the same step size for the entire simulation. In this case, the
Signal Generator block output provides a uniformly sampled representation of the
ideal waveform.

If your model uses a variable-step solver, Simulink might use different step sizes during the simulation. In this case,
the Signal Generator block output does not always provide a uniformly
sampled representation of the ideal waveform. To ensure that the block output is a
uniformly sampled representation, add a Hit Crossing block directly
downstream of the Signal Generator block. These models show the
difference in Signal Generator block output with and without the
Hit Crossing block.

| Model That Uses a Variable-Step Solver | Signal Generator Block Output |
| --- | --- |
|  | Signal Generator with sawtooth wave and variable-step solver |
|  | Signal Generator with sawtooth wave and variable-step solver and Hit Cross |

## Ports

### Output

### **Port\_1** — Generated output signal scalar | vector | matrix

Output signal specified as one of these waveforms.

- sine
- square
- sawtooth
- random

**Data Types:** `double`

## Parameters

### **Wave form** — Wave form to generate `sine` (default) | `square` | `sawtooth` | `random`

Specify the wave form.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `WaveForm` |
| **Type**: character vector |
| **Values**: `'sine'` | `'square'` | `'sawtooth'` | `'random'` |
| **Default**: `'sine'` |

### **Time (t)** — Source of time variable `Use simulation time` (default) | `Use external signal`

Specify whether to use simulation time or an external signal as the source of values for
the waveform time variable. If you specify an external source, the block
displays an input port for connecting the source.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TimeSource` |
| **Type**: character vector |
| **Values**: `'Use simulation time'` | `'Use external signal'` |
| **Default**: `'Use simulation time'` |

### **Amplitude** — Signal amplitude `1` (default) | scalar | vector | matrix

Specify the amplitude of the generated waveform.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Amplitude` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'1'` |

### **Frequency** — Signal frequency `1` (default) | scalar | vector | matrix

Specify the frequency of the generated waveform.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Frequency` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'1'` |

### **Units** — Signal units `rad/sec` (default) | `Hertz`

Specify the signal units as `Hertz` or
`rad/sec`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Units` |
| **Type**: character vector |
| **Values**: `'rad/sec'` | `'Hertz'` |
| **Default**: `'rad/sec'` |

### **Interpret vector parameters as 1-D** — Treat vectors as 1-D `on` (default) | `off`

Select this check box to output a vector of length `N` if the
**Constant value** parameter evaluates to an
`N`-element row or column vector.

- When you select this check box, the block outputs a vector of length
  `N` if the **Constant value** parameter
  evaluates to an `N`-element row or column vector. For example,
  the block outputs a matrix of dimension `1-by-N` or
  `N-by-1`.
- When you clear this check box, the block does not output a vector of length
  `N` if the **Constant value** parameter
  evaluates to an `N`-element row or column vector.

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
| **Data Types** | `double` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Cannot be used inside a triggered subsystem hierarchy.

These blocks do not reference absolute time when configured for sample-based operation. In
time-based operation, they depend on absolute time.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

**Restrictions**

Connect the Signal Generator block to the DUT ports to use it
as a source block in your model, but ensure it is not placed inside the DUT
subsystem.

## Version History

**Introduced before R2006a**
