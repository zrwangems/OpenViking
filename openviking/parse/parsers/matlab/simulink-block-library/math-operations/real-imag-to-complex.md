---
type: simulink-block
title: 'Real-Imag to Complex'
family: math-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'realimagtocomplex'
---

# Real-Imag to Complex

Convert real and/or imaginary inputs to complex signal

## 中文

将实和/或虚输入转换为复信号

### 所属库

Simulink / Math Operations HDL Coder / Math Operations

### 描述

Real-Imag to Complex 模块将实和/或虚输入转换为具有复数值的输出信号。

这两个输入可以都是具有相同维度的数组（向量或矩阵）；也可以是一个输入为数组，另一个输入为标量。如果模块具有数组输入，则输出是具有相同维度的复数数组。实数输入的元素映射到对应的复数输出元素的实部。同样，虚数输入映射到复数输出信号的虚部。如果一个输入是标量，它将映射到所有复数输出信号的对应分量（实部或虚部）。

### 端口

#### 输入

#### **Re** — 复数输出的实部 标量 | 向量 | 矩阵

要转换为复数值输出信号的实数值，指定为标量、向量或矩阵。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`

#### **Im** — 复数输出的虚部 标量 | 向量 | 矩阵

要转换为复数值输出信号的虚数值，指定为标量、向量或矩阵。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`

#### **Port\_1** — 复数输出的实部或虚部 标量 | 向量 | 矩阵

要转换为复数输出信号的实数或虚数值，指定为有限标量、向量或矩阵。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`
#### 输出

#### **Port\_1** — 复信号 标量 | 向量 | 矩阵

复信号，由实数和虚数值构成。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### **输入** — 实数输入，虚数输入，或两者同时存在 **实部** (默认) | **虚部** | **实部和虚部**

指定输入的类型：实数输入、虚数输入或者两者同时存在。

##### 编程用法

|  |
| --- |
| **模块参数**：`Input` |
| **类型：**字符向量 |
| **值：**`'Real and imag' | 'Real' | 'Imag'` |
| **默认值：**`'Real and imag'` |

#### **虚部** — 复数输出的虚部 `0` (默认) | 有限标量、向量或矩阵

指定将输入转换为复数值输出信号时使用的虚数值。

##### 依赖关系

要启用此参数，请将**输入**设置为**实部**。

##### 编程用法

|  |
| --- |
| **模块参数**：`ConstantPart` |
| **类型：**字符向量 |
| **值：**虚数值 |
| **默认值：**`'0'` |

#### **实部** — 复数输出的实部 `0` (默认) | 有限标量、向量或矩阵

指定将输入转换为复数值输出信号时使用的常量实数值。

##### 依赖关系

要启用此参数，请将**输入**设置为**虚部**。

##### 编程用法

|  |
| --- |
| **模块参数**：`ConstantPart` |
| **类型：**字符向量 |
| **值：**有限实数值标量、向量或矩阵 |
| **默认值：**`'0'` |

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
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
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

The Real-Imag to Complex block converts real and/or imaginary inputs to a
complex-valued output signal.

The inputs can both be arrays (vectors or matrices) of equal dimensions, or one input can be an array and the other a scalar. If the block has an array input, the output is a complex array of the same dimensions. The elements of the real input map to the real parts of the corresponding complex output elements. The imaginary input similarly maps to the imaginary parts of the complex output signals. If one input is a scalar, it maps to the corresponding component (real or imaginary) of all the complex output signals.

## Ports

### Input

### **Re** — Real part of complex output scalar | vector | matrix

Real value to be converted to complex-valued output signal, specified
as a scalar, vector, or matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`

### **Im** — Imaginary part of complex output scalar | vector | matrix

Imaginary value to be converted to complex-valued output signal,
specified as a scalar, vector, or matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`

### **Port\_1** — Real or imaginary part of complex output scalar | vector | matrix

Real or imaginary value to convert to complex output signal, specified
as a finite scalar, vector, or matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`
### Output

### **Port\_1** — Complex signal scalar | vector | matrix

Complex signal, formed from real and imaginary values.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Input** — Real, imaginary, or both `Real` (default) | `Imag` | `Real and imag`

Specify the type of input: a real input, an imaginary input, or both.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Input` |
| **Type:** character vector |
| **Values:** `'Real and imag' | 'Real' | 'Imag'` |
| **Default:** `'Real and imag'` |

### **Imag part** — Imaginary part of complex output `0` (default) | finite scalar, vector, or matrix

Specify the imaginary value to use when converting the input to a
complex-valued output signal.

#### Dependencies

To enable this parameter, set **Input** to
`Real`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ConstantPart` |
| **Type:** character vector |
| **Values:** imaginary value |
| **Default:** `'0'` |

### **Real part** — Real part of complex output `0` (default) | finite scalar, vector, or matrix

Specify the constant real value to use when converting the input to a
complex-valued output signal.

#### Dependencies

To enable this parameter, set **Input** to
`Imag`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ConstantPart` |
| **Type:** character vector |
| **Values:** finite, real-valued scalar, vector, or matrix |
| **Default:** `'0'` |

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
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
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
