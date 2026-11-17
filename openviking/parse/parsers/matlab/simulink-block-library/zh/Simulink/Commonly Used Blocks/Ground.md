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
chinese_source: worker-translation
---

# Ground

## 端口

### 输出

### **Port\_1** — 接地信号 标量

Ground 模块输出一个值为零的标量信号，其数据类型与它所连接的端口相同。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## 参数

R2025b 中未记录。

## 所属库

Simulink / Commonly Used Blocks Simulink / Sources HDL Coder / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

接地未连接的输入端口

Ground 模块连接到输入端口未与其他模块连接的模块。如果运行仿真时存在输入端口未连接的模块，软件会发出警告。使用 Ground 模块对接那些未连接的模块可以防止这些警告。

### 使用定点数据类型

在使用定点数据类型时，可能存在定点数据类型无法精确表示零的情况。在这些情况下，Ground 模块输出一个非零值，该值是最接近零的可能值。此行为仅适用于具有非零偏置的定点数据类型。以下表达式是无法表示零的定点数据类型示例：

- `fixdt(0, 8, 1, 1)` — 斜率为 1、偏置为 1 的无符号 8 位类型
- `fixdt(1, 8, 6, 3)` — 斜率为 6、偏置为 3 的有符号 8 位类型

### 使用枚举数据类型

在使用枚举数据类型时，Ground 模块输出该枚举的默认值。此行为适用于以下两种情况：

- 该枚举可以表示零
- 该枚举的默认值为零

如果枚举类型没有默认值，Ground 模块输出类型定义中的第一个枚举值。
