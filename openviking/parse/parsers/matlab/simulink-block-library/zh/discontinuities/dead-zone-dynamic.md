---
type: simulink-block
title: 'Dead Zone Dynamic'
family: discontinuities
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'deadzonedynamic'
language: zh-CN
chinese_source: official
---

# Dead Zone Dynamic

提供零输出的动态区域

## 所属库

Simulink / Discontinuities HDL Coder / Discontinuities

## 描述

Dead Zone Dynamic 模块根据指定上限和下限的动态输入信号生成零输出区域。模块输出取决于输入 **u** 以及输入信号 **up** 和 **lo** 的值。

| 输入 | 输出 |
| --- | --- |
| `u >= lo` 和 `u <= up` | 零 |
| `u > up` | `u` – `up` |
| `u < lo` | `u` – `lo` |

Dead Zone Dynamic 模块是封装子系统，没有任何参数。

## 端口

### 输入

### **u** — 输入信号 标量 | 向量

死区算法的输入信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **lo** — 死区下限 标量 | 向量

提供零输出区域下界的动态值。当输入小于 **lo** 时，输出值将向下偏移 **lo** 的值。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **up** — 死区上限 标量

提供零输出区域上界的动态值。当输入大于 **up** 时，输出值将向下偏移 **up** 的值。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **y** — 输出信号 标量 | 向量

对输入信号应用动态死区算法后的输出信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史记录

**在 R2006a 之前推出**
