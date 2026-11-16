---
type: simulink-block
title: 'Wrap To Zero'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Discontinuities'
documentation_page: 'wraptozero'
documentation_source_path: 'slref/wraptozero.html'
language: zh-CN
chinese_source: official
---

# Wrap To Zero

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

输入信号，指定为标量或向量。等于或大于 `Threshold` 值的信号值设置为零。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

设置为输入信号值或零的输出信号。输出的数据类型与输入的数据类型相同。

**提示**

如果输入数据类型不能表示零，将发生参数溢出。要检测此溢出，请转到“配置参数”对话框的**诊断 > 数据有效性**窗格，并将**参数 > 检测上溢**设置为**警告**或**错误**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

要编辑 Wrap to Zero 模块的参数，请双击模块图标。

### **阈值** — 使模块输出零的阈值 `255` (默认) | 标量

使模块将输出值设置为零的阈值。

#### 编程用法

|  |
| --- |
| **模块参数**：`Threshold` |
| **类型**：字符向量 |
| **值**：`scalar` |
| **默认值**：`'255'` |

## 所属库

Simulink / Discontinuities HDL Coder / Discontinuities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
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

**限制**

输入信号和**阈值**参数必须大小相等。例如，如果输入是二维向量，**阈值**也必须是二维向量。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

如果输入大于阈值，将输出设置为零

当输入大于**阈值**值时，Wrap To Zero 模块将输出设置为零。当输入小于或等于**阈值**时，输出等于输入。
