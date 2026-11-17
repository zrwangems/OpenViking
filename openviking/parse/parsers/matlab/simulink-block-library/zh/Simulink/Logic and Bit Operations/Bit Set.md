---
type: simulink-block
title: 'Bit Set'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'bitset'
documentation_source_path: 'slref/bitset.html'
language: zh-CN
chinese_source: worker-translation
---

# Bit Set

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

具有存储整数指定比特位的输入信号。

**数据类型：** `single` | `double` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

将指定比特位设置为 1 的输出信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **Index of bit** — 比特位索引 0（默认）| 标量 | 向量

比特位的索引，其中比特位 0 为最低有效位。

#### 编程使用

|  |
| --- |
| **模块参数**：`iBit` |
| **类型**：character vector |
| **值**：positive integer |
| **默认值**：`'0'` |

## 所属库

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `fixed point` | `integer` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a 不建议对布尔信号使用位运算。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

将存储整数的指定比特位设置为 1

Bit Set 模块将存储整数的指定比特位设置为 1。
缩放被忽略。

您可以使用 **Index of bit** 参数指定要设置为 1 的比特位，其中比特位 0 为最低有效位。
