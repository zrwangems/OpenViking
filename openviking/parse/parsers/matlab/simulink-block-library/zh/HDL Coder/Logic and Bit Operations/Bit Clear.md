---
type: simulink-block
title: 'Bit Clear'
family: 'logic-and-bit-operations'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'bitclear'
documentation_source_path: '../simulink/slref/bitclear.html'
language: zh-CN
chinese_source: worker-translation
---

# Bit Clear

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

输入信号是存储整数的指定位。

**数据类型：** `single` | `double` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

输出由设置为零的指定二进制位组成。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **位索引** — 位索引 0（默认）| 标量 | 向量

位索引，其中第 0 位是最低有效位。

#### 编程用法

|  |
| --- |
| **模块参数**：`iBit` |
| **类型**：character vector |
| **取值**：标量 | 向量 |
| **默认值**：`'0'` |

## 所属库

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `fixed point` | `integer` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 不建议将位运算用于 Boolean 信号。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

将存储整数的指定二进制位设置为零

Bit Clear 模块将存储整数的指定二进制位（由其索引给出）设置为零。缩放将被忽略。

您可以使用 **位索引** 参数指定要设置为零的位，其中第 0 位是最低有效位。
