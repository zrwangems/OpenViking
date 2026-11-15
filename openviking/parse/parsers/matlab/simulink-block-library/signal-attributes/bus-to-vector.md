---
type: simulink-block
title: 'Bus to Vector'
family: signal-attributes
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'bustovector'
---

# Bus to Vector

Convert virtual bus to vector

## 中文

将虚拟总线转换为向量

### 所属库

Simulink / Signal Attributes HDL Coder / Signal Attributes

### 描述

Bus to Vector 模块将虚拟总线转换为向量。Bus to Vector 模块仅用于将隐式的总线到向量转换替换为显式转换。

不接受总线的模块可能隐式将总线转换为向量。当总线被视为向量时，总线元素变得不可访问。要识别和更正用作向量的总线，请使用模型顾问检查检查被视为向量的总线信号或函数 `Simulink.BlockDiagram.addBusToVector`。

### 端口

#### 输入

#### **Port\_1** — 要转换为向量的总线 标量 | 向量 | 总线

输入总线必须由具有相同的数据类型、信号类型和采样模式的标量或一维、行或列向量组成。如果输入是非总线信号，则该模块不进行转换。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
**复数支持:** 是
#### 输出

#### **Port\_1** — 输出向量 向量

输出向量的维数取决于输入总线元素的维数。如果输入总线包含行向量或列向量，此模块将分别输出一个行向量或一个列向量。否则，输出是一维向量。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
**复数支持:** 是

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

要了解有关使用总线进行 HDL 代码生成的更多信息，请参阅Buses (HDL Coder) 和Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder)。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型或功能支持取决于模块实现。

### 版本历史记录

**在 R2007a 中推出**

## Libraries

Simulink / Signal Attributes HDL Coder / Signal Attributes

## Description

The Bus to Vector block converts a virtual bus to a vector. Use the
Bus to Vector block only to replace an implicit bus-to-vector conversion with
an explicit conversion.

Blocks that do not accept buses may implicitly convert buses to vectors. When a bus is
treated as a vector, bus elements become inaccessible. To identify and correct buses
used as vectors, use the Model Advisor check Check bus signals treated as
vectors or the function `Simulink.BlockDiagram.addBusToVector`.

## Ports

### Input

### **Port\_1** — Bus to convert to vector scalar | vector | bus

An input bus must consist of scalars or 1-D, row, or column vectors that have the
same data type, signal type, and sampling mode. If the input is a nonbus signal, the
block does no conversion.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Output vector vector

The dimensions of the output vector depend on the dimensions of the input bus elements.
If the input bus contains row or column vectors, the block output is a row or column
vector, respectively. Otherwise, the output is a 1-D vector.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
**Complex Number Support:** Yes

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual data type or capability support depends on block implementation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

To learn more about using buses for HDL code generation, see Buses (HDL Coder) and Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder).

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type or capability support depends on block implementation.

## Version History

**Introduced in R2007a**
