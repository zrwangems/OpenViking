---
type: simulink-block
title: 'Terminator'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'terminator'
documentation_source_path: '../simulink/slref/terminator.html'
language: zh-CN
chinese_source: official
---

# Terminator

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组 | 总线

使用此端口来处理仿真过程中并不连接到其他端口的输出端口的信号。该端口接受所有数据类型的实信号或复信号。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## 参数

R2025b 官方文档未提供。

## 所属库

Simulink / Commonly Used Blocks Simulink / Sinks HDL Coder / Sinks

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

| 架构 | 描述 |
| --- | --- |
| **无 HDL** | 不为此模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制是否删除未连接的逻辑。默认值为 `off`，这意味着未连接的逻辑不会保留在 HDL 代码中。有关详细信息，请参阅PreserveUpstreamLogic (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

终止未连接的输出端口

使用 Terminator 模块终止输出端口未连接其他模块的模块。如果您运行的仿真中有一些模块的输出端口未连接任何模块，Simulink® 将发出警告消息。使用 Terminator 模块终止这些模块，可以防止出现此类警告消息。
