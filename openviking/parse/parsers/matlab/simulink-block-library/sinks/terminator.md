---
type: simulink-block
title: 'Terminator'
family: sinks
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'terminator'
---

# Terminator

Terminate unconnected output port

## 中文

终止未连接的输出端口

### 所属库

Simulink / Commonly Used Blocks Simulink / Sinks HDL Coder / Sinks

### 描述

使用 Terminator 模块终止输出端口未连接其他模块的模块。如果您运行的仿真中有一些模块的输出端口未连接任何模块，Simulink® 将发出警告消息。使用 Terminator 模块终止这些模块，可以防止出现此类警告消息。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组 | 总线

使用此端口来处理仿真过程中并不连接到其他端口的输出端口的信号。该端口接受所有数据类型的实信号或复信号。

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

| 架构 | 描述 |
| --- | --- |
| **无 HDL** | 不为此模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制是否删除未连接的逻辑。默认值为 `off`，这意味着未连接的逻辑不会保留在 HDL 代码中。有关详细信息，请参阅PreserveUpstreamLogic (HDL Coder)。 |

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Commonly Used Blocks Simulink / Sinks HDL Coder / Sinks

## Description

Use the Terminator block to cap blocks whose output ports do not connect to other
blocks. If you run a simulation with blocks having unconnected output ports, Simulink® issues warning messages. Using Terminator blocks to cap those blocks helps
prevent warning messages.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | n-D array | bus

Use this port to direct signals from output ports that are otherwise
unconnected during a simulation. The port accepts real or complex
signals of all data types.

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

| Architecture | Description |
| --- | --- |
| `No HDL` | Do not generate HDL code for this block. |

**HDL Block Properties**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | Control the removal of unconnected logic. The default is `off`, which means unconnected logic is not preserved in HDL code. For more details, see PreserveUpstreamLogic (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
