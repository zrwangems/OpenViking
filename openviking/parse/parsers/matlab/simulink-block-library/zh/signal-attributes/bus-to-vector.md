---
type: simulink-block
title: 'Bus to Vector'
family: signal-attributes
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'bustovector'
language: zh-CN
chinese_source: official
---

# Bus to Vector

将虚拟总线转换为向量

## 所属库

Simulink / Signal Attributes HDL Coder / Signal Attributes

## 描述

Bus to Vector 模块将虚拟总线转换为向量。Bus to Vector 模块仅用于将隐式的总线到向量转换替换为显式转换。

不接受总线的模块可能隐式将总线转换为向量。当总线被视为向量时，总线元素变得不可访问。要识别和更正用作向量的总线，请使用模型顾问检查检查被视为向量的总线信号或函数 `Simulink.BlockDiagram.addBusToVector`。

## 端口

### 输入

### **Port\_1** — 要转换为向量的总线 标量 | 向量 | 总线

输入总线必须由具有相同的数据类型、信号类型和采样模式的标量或一维、行或列向量组成。如果输入是非总线信号，则该模块不进行转换。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
**复数支持:** 是
### 输出

### **Port\_1** — 输出向量 向量

输出向量的维数取决于输入总线元素的维数。如果输入总线包含行向量或列向量，此模块将分别输出一个行向量或一个列向量。否则，输出是一维向量。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
**复数支持:** 是

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

要了解有关使用总线进行 HDL 代码生成的更多信息，请参阅Buses (HDL Coder) 和Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder)。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型或功能支持取决于模块实现。

## 版本历史记录

**在 R2007a 中推出**
