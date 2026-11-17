---
type: simulink-block
title: 'Sample Control Bus Creator'
family: 'utilities'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'samplecontrolbuscreator'
documentation_source_path: 'ref/samplecontrolbuscreator.html'
language: zh-CN
chinese_source: worker-translation
---

# Sample Control Bus Creator

## 端口

### 输入

### **start** — 帧起始标量

帧起始，指定为 `Boolean` 标量。此信号在一个时间步内为 1 (true)，对应于该帧的第一个有效采样。

**数据类型：** `Boolean`

### **end** — 帧结束标量

帧结束，指定为 `Boolean` 标量。此信号在一个时间步内为 1 (true)，对应于该帧的最后一个有效采样。

**数据类型：** `Boolean`

### **valid** — 采样有效性标量

采样有效性，指定为 `Boolean` 标量。此信号在对应于有效采样的时间步上为 1 (true)。

**数据类型：** `Boolean`
### 输出

### **ctrl** — 伴随采样流的控制信号 `samplecontrol` 总线

伴随采样流的控制信号，返回为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，这些信号指示帧的边界以及采样的有效性。

- `start` — 指示输出帧的起始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

## 参数

未在 R2025b 中记录。

## 所属库

Wireless HDL Toolbox / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink 加速模式和快速加速模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 生成用于 FPGA 和 ASIC 设计的 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

要了解有关将总线用于 HDL 代码生成的更多信息，请参阅 Buses (HDL Coder) 和 Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder)。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计中移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2017b 中引入**

## 描述

创建用于 Wireless HDL Toolbox 模块的控制信号总线

Sample Control Bus Creator 模块创建一个 `samplecontrol` 总线，用于为硬件通信系统中的流式控制信号建模。请参阅 Sample Control Bus。

该模块是 Simulink® Bus Creator 模块的一种实现。有关更多信息，请参阅 Bus Creator。
