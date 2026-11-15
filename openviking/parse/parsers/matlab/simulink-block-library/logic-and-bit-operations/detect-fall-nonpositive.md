---
type: simulink-block
title: 'Detect Fall Nonpositive'
family: logic-and-bit-operations
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'detectfallnonpositive'
---

# Detect Fall Nonpositive

Detect falling edge when signal value decreases to nonpositive value, and its previous value was strictly positive

## 中文

当信号值下降到非正值，且其先前值严格为正时，检测下降沿

### 库

Simulink / 逻辑和位运算

### 描述

Detect Fall Nonpositive 模块判断输入是否小于或等于零，且其先前值大于零。

- 当输入信号小于或等于零，且其先前值大于零时，输出为 true（等于 `1`）。
- 当输入信号大于零，或者如果其为非正值且其先前值也为非正值时，输出为 false（等于 `0`）。

此模块仅支持离散采样时间。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

检测下降沿的输出信号，指定为标量、向量或矩阵。

- 当输入信号小于或等于零，且其先前值大于零时，输出为 true（等于 `1`）。
- 当输入信号大于零，或者如果其为非正值且其先前值也为非正值时，输出为 false（等于 `0`）。

**数据类型：** `uint8` | `Boolean`

### 参数

#### **初始条件** — 布尔表达式 `U/z <= 0` 的初始条件 0（默认） | 标量 | 向量 | 矩阵

设置布尔表达式 `U/z <= 0` 的初始条件。

#### 程序化使用

|  |
| --- |
| **模块参数：** `vinit` |
| **类型：** character vector |
| **值：** 标量 | 向量 | 矩阵 |
| **默认：** `'0'` |

#### **输入处理** — 指定基于采样或基于帧的处理 `Elements as channels (sample based)`（默认） | `Columns as channels (frame based)`

指定该模块执行基于采样还是基于帧的处理：

- `Columns as channels (frame based)` — 将输入的每一列视为单独通道（基于帧的处理）。

  **注意**

  基于帧的处理需要 DSP System Toolbox™ 许可证。

  有关详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。
- `Elements as channels (sample based)` — 将输入的每个元素视为单独通道（基于采样的处理）。

使用 **输入处理** 指定该模块执行基于采样还是基于帧的处理。有关这两种处理模式的详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。

#### 程序化使用

|  |
| --- |
| **模块参数**： `InputProcessing` |
| **类型**： character vector |
| **值**： `'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **默认**： `'Elements as channels (sample based)'` |

#### **输出数据类型** — 输出数据类型 `boolean`（默认） | `uint8`

将输出数据类型指定为 `boolean` 或 `uint8`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutDataTypeStr` |
| **类型：** character vector |
| **值：** `'boolean' | 'uint8'` |
| **默认：** `'boolean'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供额外配置选项，这些选项会影响 HDL 实现和综合逻辑。

**HDL 架构**

此模块有一种默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计中移动现有延迟，放置在输出处的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入生成代码中的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入生成代码中的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史

**在 R2006a 之前引入**

## Libraries

Simulink / Logic and Bit Operations

## Description

The Detect Fall Nonpositive block determines if the input is less than
or equal to zero, and its previous value was greater than zero.

- The output is true (equal to `1`) when the input signal is
  less than or equal to zero, and its previous value was greater than zero.
- The output is false (equal to `0`) when the input signal is
  greater than zero, or if it is nonpositive, its previous value was also
  nonpositive.

This block supports only discrete sample times.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal, specified as a scalar, vector, or matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output signal that detects a falling edge, specified as a scalar,
vector, or matrix.

- The output is true (equal to `1`) when
  the input signal is less than or equal to zero, and its
  previous value was greater than zero.
- The output is false (equal to `0`) when
  the input signal is greater than zero, or if it is
  nonpositive, its previous value was also nonpositive.

**Data Types:** `uint8` | `Boolean`

## Parameters

### **Initial condition** — Initial condition of Boolean expression `U/z <= 0` 0 (default) | scalar | vector | matrix

Set the initial condition of the Boolean expression `U/z <=
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
