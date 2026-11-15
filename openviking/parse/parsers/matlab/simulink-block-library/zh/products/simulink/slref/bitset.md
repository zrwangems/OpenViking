---
type: simulink-block
title: 'Bit Set'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Logic and Bit Operations'
documentation_page: 'bitset'
documentation_source_path: 'slref/bitset.html'
language: zh-CN
chinese_source: official
---

# Bit Set

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

具有存储整数的指定位的输入信号。

**数据类型:** `single` | `double` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

指定位设置为 1 的输出信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **位的索引** — 位的索引 0 (默认) | 标量 | 向量

位的索引，其中位 0 是最低有效位。

#### 编程用法

|  |
| --- |
| **模块参数**：`iBit` |
| **类型**：字符向量 |
| **值**：正整数 |
| **默认值**：`'0'` |

## 所属库

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `fixed point` | `integer` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 建议不要对布尔信号进行位运算。 | |

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

## 版本历史

**在 R2006a 之前推出**

## 描述

将存储整数的指定位设置为 1

Bit Set 模块将存储整数的指定位设置为 1。忽略定标。

您可以使用**位的索引**参数指定要设置为 1 的位，其中位 0 是最低有效位。
