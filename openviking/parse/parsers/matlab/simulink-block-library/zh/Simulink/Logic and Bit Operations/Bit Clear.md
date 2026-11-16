---
type: simulink-block
title: 'Bit Clear'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Logic and Bit Operations'
documentation_page: 'bitclear'
documentation_source_path: 'slref/bitclear.html'
language: zh-CN
chinese_source: worker-translation
---

# Bit Clear



将存储整数的指定位置零

## 库

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## 描述

Bit Clear 模块将存储整数的指定位（由其索引给出）设置为零。缩放将被忽略。

您可以使用 **Index of bit** 参数指定要设置为零的位，其中位 0 是最低有效位。

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

输入信号是存储整数的指定位。

**数据类型：** `single` | `double` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

输出由设置为零的指定位组成。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **Index of bit** — 位索引 0（默认）| 标量 | 向量

位索引，其中位 0 是最低有效位。

#### 编程使用

|  |
| --- |
| **模块参数**: `iBit` |
| **类型**: character vector |
| **值**: 标量 | 向量 |
| **默认**: `'0'` |

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `fixed point` | `integer` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 建议不要将位操作与 Boolean 信号一起使用。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**
