---
type: simulink-block
title: 'Detect Rise Positive'
family: logic-and-bit-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'detectrisepositive'
---

# Detect Rise Positive

Detect rising edge when signal value increases to strictly positive value, and its previous value was nonpositive

## 中文

上升沿检测，当信号值从上一个严格意义上的负值变为非负值时

### 所属库

Simulink / Logic and Bit Operations

### 描述

Detect Rise Positive 模块通过确定输入是严格正值且上一个值是非正值来检测上升沿。

- 当输入信号大于零且上一个值小于或等于零时，输出为 true（等于 `1`）。
- 当输入信号为负或为零时，或者当输入信号为正、上一个值也为正时，输出为 false（等于 `0`）。

此模块仅支持离散采样时间。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

输出信号，用于检测输入是严格正值且上一个值是非正值时的上升沿。输出可以是标量、向量或矩阵。

- 当输入信号大于零且上一个值小于或等于零时，输出为 true（等于 `1`）。
- 当输入信号为负或为零时，或者当输入信号为正、上一个值也为正时，输出为 false（等于 `0`）。

**数据类型:** `uint8` | `Boolean`

### 参数

#### **初始条件** — 布尔表达式 `U/z > 0` 的初始条件 `0` (默认) | 标量 | 向量 | 矩阵

设置布尔表达式 `U/z > 0` 的初始条件。

##### 编程用法

|  |
| --- |
| **模块参数**：`vinit` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'0'` |

#### **输入处理** — 指定基于采样或基于帧的处理 **元素作为通道(基于采样)** (默认) | **列作为通道(基于帧)**

指定模块是执行基于采样还是基于帧的处理：

- **列作为通道(基于帧)** - 将输入信号的每一列视为一个单独的通道（基于帧的处理）。

  **注意**

  基于帧的处理需要具有 DSP System Toolbox™ 许可证。

  有关详细信息，请参阅Sample- and Frame-Based Concepts (DSP System Toolbox)。
- **元素作为通道(基于采样)** - 将输入信号的每个元素视为一个单独的通道（基于采样的处理）。

可以使用**输入处理**指定模块是执行基于采样的处理还是基于帧的处理。有关这两种处理模式的详细信息，请参阅Sample- and Frame-Based Concepts (DSP System Toolbox)。

##### 编程用法

|  |
| --- |
| **模块参数**：`InputProcessing` |
| **类型**：字符向量 |
| **值**：`'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **默认值**：`'Elements as channels (sample based)'` |

#### **输出数据类型** — 输出数据类型 `boolean` (默认) | `uint8`

将输出数据类型指定为 `boolean` 或 `uint8`。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'boolean' | 'uint8'` |
| **默认值：**`'boolean'` |

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

生成的代码在特定条件下依赖于 `memcpy` 或 `memset` 函数 (`string.h`)。

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

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Logic and Bit Operations

## Description

The Detect Rise Positive block detects a rising edge by determining if
the input is strictly positive, and its previous value was nonpositive.

- The output is true (equal to `1`) when the input signal is
  greater than zero, and the previous value was less than or equal to zero.
- The output is false (equal to `0`) when the input is negative
  or zero, or if the input is positive, the previous value was also
  positive.

This block supports only discrete sample times.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal, specified as a scalar, vector, or matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output signal that detects a rising edge whenever the input is
strictly positive, and its previous value was nonpositive. The output
can be a scalar, vector, or matrix.

- The output is true (equal to `1`) when
  the input signal is greater than zero, and the previous
  value was less than or equal to zero.
- The output is false (equal to `0`) when
  the input is negative or zero, or if the input is positive,
  the previous value was also positive.

**Data Types:** `uint8` | `Boolean`

## Parameters

### **Initial condition** — Initial condition of Boolean expression `U/z > 0` `0` (default) | scalar | vector | matrix

Set the initial condition of the Boolean expression `U/z >
0`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `vinit` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'0'` |

### **Input processing** — Specify sample- or frame-based processing `Elements as channels (sample based)` (default) | `Columns as channels (frame based)`

Specify whether the block performs sample- or frame-based processing:

- `Columns as channels (frame based)` — Treat
  each column of the input as a separate channel (frame-based processing).

  **Note**

  Frame-based processing requires a DSP System Toolbox™ license.

  For more information, see Sample- and Frame-Based Concepts (DSP System Toolbox).
- `Elements as channels (sample based)` — Treat
  each element of the input as a separate channel (sample-based
  processing).

Use **Input processing** to specify whether the block performs
sample- or frame-based processing. For more information about these two processing
modes, see Sample- and Frame-Based Concepts (DSP System Toolbox).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InputProcessing` |
| **Type**: character vector |
| **Values**: `'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **Default**: `'Elements as channels (sample based)'` |

### **Output data type** — Output data type `boolean` (default) | `uint8`

Specify the output data type as `boolean` or
`uint8`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'boolean' | 'uint8'` |
| **Default:** `'boolean'` |

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

Generated code relies on `memcpy` or
`memset` functions (`string.h`) under
certain conditions.

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

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
