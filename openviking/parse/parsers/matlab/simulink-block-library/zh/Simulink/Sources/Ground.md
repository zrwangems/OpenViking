---
type: simulink-block
title: 'Ground'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'ground'
documentation_source_path: 'slref/ground.html'
language: zh-CN
chinese_source: official
---

# Ground

## 端口

### 输出

### **Port\_1** — 接地信号 标量

Ground 模块输出具有零值的标量信号，其数据类型与所连接的端口相同。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## 参数

R2025b 官方文档未提供。

## 所属库

Simulink / Commonly Used Blocks Simulink / Sources HDL Coder / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `否` |
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
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复信号的代码生成。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

将未连接的输入端口接地

Ground 模块连接到其输入端口不连接到其他模块的模块。如果您使用具有未连接的输入端口的模块运行仿真，软件会发出警告。使用 Ground 模块将那些未连接的模块接地可以防止出现这些警告。

### 使用定点数据类型

使用定点数据类型时，可能会出现定点数据类型不能准确表示零的情况。在这些情况下，Ground 模块输出尽可能最接近零的非零值。这种行为仅适用于具有非零偏置的定点数据类型。以下表达式是不能表示零的定点数据类型的示例：

- `fixdt(0, 8, 1, 1)` - 使用斜率 1 和偏置 1 的无符号 8 位数据类型
- `fixdt(1, 8, 6, 3)` - 使用斜率 6 和偏置 3 的有符号 8 位数据类型

### 使用枚举数据类型

使用枚举数据类型时，Ground 模块输出枚举的默认值。此行为是否适用取决于：

- 枚举是否可以表示零
- 枚举的默认值是否为零

如果枚举类型没有默认值，则 Ground 模块输出类型定义中的第一个枚举值。
