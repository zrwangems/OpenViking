---
type: simulink-block
title: 'Ground'
family: sources
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'ground'
---

# Ground

Ground unconnected input port

## 中文

将未连接的输入端口接地

### 所属库

Simulink / Commonly Used Blocks Simulink / Sources HDL Coder / Sources

### 描述

Ground 模块连接到其输入端口不连接到其他模块的模块。如果您使用具有未连接的输入端口的模块运行仿真，软件会发出警告。使用 Ground 模块将那些未连接的模块接地可以防止出现这些警告。

#### 使用定点数据类型

使用定点数据类型时，可能会出现定点数据类型不能准确表示零的情况。在这些情况下，Ground 模块输出尽可能最接近零的非零值。这种行为仅适用于具有非零偏置的定点数据类型。以下表达式是不能表示零的定点数据类型的示例：

- `fixdt(0, 8, 1, 1)` - 使用斜率 1 和偏置 1 的无符号 8 位数据类型
- `fixdt(1, 8, 6, 3)` - 使用斜率 6 和偏置 3 的有符号 8 位数据类型

#### 使用枚举数据类型

使用枚举数据类型时，Ground 模块输出枚举的默认值。此行为是否适用取决于：

- 枚举是否可以表示零
- 枚举的默认值是否为零

如果枚举类型没有默认值，则 Ground 模块输出类型定义中的第一个枚举值。

### 端口

#### 输出

#### **Port\_1** — 接地信号 标量

Ground 模块输出具有零值的标量信号，其数据类型与所连接的端口相同。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
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
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复信号的代码生成。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Commonly Used Blocks Simulink / Sources HDL Coder / Sources

## Description

The Ground block connects to blocks whose input ports do not connect to other
blocks. If you run a simulation with blocks that have unconnected input ports, the
software issues warnings. Using a Ground block to ground those
unconnected blocks can prevent these warnings.

### Working with Fixed-Point Data Types

When working with fixed-point data types, there may be instances where the fixed-point data
type cannot represent zero exactly. In these cases, the Ground block
outputs a nonzero value that is the closest possible value to zero. This behavior
applies only to fixed-point data types with nonzero bias. These expressions are
examples of fixed-point data types that cannot represent zero:

- `fixdt(0, 8, 1, 1)` — an unsigned 8-bit type with
  slope of 1 and bias of 1
- `fixdt(1, 8, 6, 3)` — a signed 8-bit type with
  slope of 6 and bias of 3

### Working with Enumerated Data Types

When working with enumerated data types, the Ground block outputs the
default value of the enumeration. This behavior applies whether:

- The enumeration can represent zero
- The default value of the enumeration is zero

If the enumerated type does not have a default value, the Ground block
outputs the first enumeration value in the type definition.

## Ports

### Output

### **Port\_1** — Ground signal scalar

The Ground block outputs a scalar signal with zero value, and the same
data type as the port to which it connects.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
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
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
