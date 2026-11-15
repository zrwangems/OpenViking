---
type: simulink-block
title: 'Complex to Real-Imag'
family: math-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'complextorealimag'
---

# Complex to Real-Imag

Output real and imaginary parts of complex input signal

## 中文

输出复输入信号的实部和虚部

### 所属库

Simulink / Math Operations HDL Coder / Math Operations

### 描述

Complex to Real-Imag 模块输出输入信号的实部和/或虚部，具体取决于**输出**参数的设置。实数输出与复数输入具有相同的数据类型。输入可以是复信号数组（向量或矩阵），这种情况下，输出信号也是具有相同维度的数组。实数数组包含对应的复数输入元素的实部。同样，虚数输出包含输入元素的虚部。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

该模块计算并输出实部和/或虚部的复输入信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

输出信号，即输入信号的实部和/或虚部。要选择输出哪个部分，请设置**输出**参数。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 参数

#### **输出** — 实部和/或虚部输出设定 **实部和虚部** (默认) | **实部** | **虚部**

指定输出是输入信号的实部、虚部还是同时包含实部和虚部。

##### 编程用法

|  |
| --- |
| **参数：**`Output` |
| **类型：**字符串 | 字符向量 |
| **值：**`'Real and imag'` | `'Real'` | `'Imag'` |
| **默认值：**`'Real and imag'` |

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
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
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

**复数数据支持**

此模块支持复信号的代码生成。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Math Operations HDL Coder / Math Operations

## Description

The Complex to Real-Imag block outputs the real and/or imaginary part
of the input signal, depending on the setting of the **Output**
parameter. The real outputs are of the same data type as the complex input. The input
can be an array (vector or matrix) of complex signals, in which case the output signals
are arrays of the same dimensions. The real array contains the real parts of the
corresponding complex input elements. The imaginary output similarly contains the
imaginary parts of the input elements.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Complex input signal that the block computes and outputs the real
and/or imaginary part.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output signal that is the real and/or imaginary part of the input
signal. To choose which part is output, set the
**Output** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### **Output** — Real and/or imaginary output specification `Real and imag` (default) | `Real` | `Imag`

Specify whether the output is the real, imaginary, or both real and
imaginary part of the input signal.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `Output` |
| **Type:** string | character vector |
| **Values:** `'Real and imag'` | `'Real'` | `'Imag'` |
| **Default:** `'Real and imag'` |

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
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
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

**Complex Data Support**

This block supports code generation for complex signals.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
