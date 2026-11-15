---
type: simulink-block
title: 'Counter Limited'
family: sources
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'counterlimited'
---

# Counter Limited

Count up and wrap to zero after specified upper limit

## 中文

进行累加计数，并在达到指定的上限后绕回到 0

### 所属库

Simulink / Sources HDL Coder / Sources

### 描述

Counter Limited 模块进行累加计数，直到达到指定的上限。然后，该计数器绕回到零并重新启动累加计数。该计数器始终初始化为零。

**注意**

仿真期间，此模块不会报告溢出绕回警告。要报告这些警告，请参阅 `Simulink.restoreDiagnostic` 参考页。但此模块会报告由于溢出绕回而导致的错误。

### 端口

#### 输出

#### **Port\_1** — 计数值 标量

计数值，以 8 位、16 位、32 位、64 位无符号整数形式或 ufix128 形式返回。该模块使用表示上限所需的最小位数。

**数据类型:** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### **上限** — 上限 `7` (默认) | 标量

将模块计数的上限指定为有限实数值标量。

##### 编程用法

|  |
| --- |
| **模块参数**：`uplimit` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'7'` |

#### **采样时间** — 采样之间的时间间隔 `-1` (默认) | 标量 | 向量

将采样之间的时间间隔指定为标量 (`sampling period`) 或二元素向量 (`sampling period, initial offset`)。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

##### 编程用法

|  |
| --- |
| **模块参数**：`tsamp` |
| **类型：**字符向量 |
| **值：**标量 | 向量 |
| **默认值：**`'-1'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `fixed point` | `integer` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

- 代码生成器不会在生成的代码中将构成非原子封装子系统模块的原始模块显式组合在一起。这种灵活性可以提高代码生成效率。在某些情况下，通过选择**视为原子单元**选项，可以通过将封装子系统模块配置为以原子单元执行来进行组合。
- 不建议用于生产代码。涉及到嵌入式系统中常见的资源限制以及对速度和内存的限制。生成的代码可以包含动态分配和释放内存、递归、额外的内存开销以及长短不等的执行时间。虽然代码在功能上有效并且在资源丰富的环境中通常可接受，但较小的嵌入式目标通常不能支持此类代码。通常情况下，模块会向适合生产代码的方向发展。因此，适合生产代码的模块仍然适用。

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

Simulink / Sources HDL Coder / Sources

## Description

The Counter Limited block counts up until the specified upper limit is reached. Then the counter wraps back to zero, and restarts counting up. The counter always initializes to zero.

**Note**

This block does not report wrap on overflow warnings during simulation. To report
these warnings, see the `Simulink.restoreDiagnostic`
reference page. The block does report errors due to wrap on overflow.

## Ports

### Output

### **Port\_1** — Count value scalar

Count value, returned as an unsigned integer of 8 bits, 16 bits, 32 bits, 64 bits, or
ufix128. The block uses the smallest number of bits required to
represent the upper limit.

**Data Types:** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Upper limit** — Upper limit `7` (default) | scalar

Specify the upper limit for the block to count to as a finite, real-valued scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `uplimit` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'7'` |

### **Sample time** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples as a scalar (`sampling
period`), or a two-element vector (`sampling period,
initial offset`). To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `tsamp` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'-1'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `fixed point` | `integer` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

- The code generator does not explicitly group primitive blocks that
  constitute a nonatomic masked subsystem block in the generated code. This
  flexibility allows for more efficient code generation. In certain cases, you
  can achieve grouping by configuring the masked subsystem block to execute as
  an atomic unit by selecting the **Treat as atomic
  unit** option.
- Not recommended for production code. Relates to resource limits and
  restrictions on speed and memory often found in embedded systems. Generated
  code can contain dynamic allocation and freeing of memory, recursion,
  additional memory overhead, and widely-varying execution times. While the
  code is functionally valid and generally acceptable in resource-rich
  environments, smaller embedded targets often cannot support such code.
  Usually, blocks evolve toward being suitable for production code. Thus,
  blocks suitable for production code remain suitable.

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
