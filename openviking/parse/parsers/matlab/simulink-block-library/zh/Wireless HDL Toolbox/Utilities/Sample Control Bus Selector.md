---
type: simulink-block
title: 'Sample Control Bus Selector'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'samplecontrolbusselector'
documentation_source_path: 'ref/samplecontrolbusselector.html'
language: zh-CN
chinese_source: worker-translation
---

# Sample Control Bus Selector

## 端口

### 输入

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包含 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界以及样本的有效性。

- `start` — 指示输入帧的起始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`
### 输出

### **start** — 帧起始标量

帧起始，以 `Boolean` 标量形式返回。该信号在一个时间步内为 1（true），对应于帧的第一个有效样本。

**数据类型：** `Boolean`

### **end** — 帧结束标量

帧结束，以 `Boolean` 标量形式返回。该信号在一个时间步内为 1（true），对应于帧的最后一个有效样本。

**数据类型：** `Boolean`

### **valid** — 样本有效性标量

样本有效性，以 `Boolean` 标量形式返回。该信号在对应于有效样本的时间步上为 1（true）。

**数据类型：** `Boolean`

## 参数

R2025b 中未记录。

## 所属库

Wireless HDL Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

该模块支持针对 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

要了解有关将总线用于 HDL 代码生成的更多信息，请参阅 Buses (HDL Coder) 和 Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder)。

**HDL 架构**

该模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2017b 中引入**

## 描述

从与 Wireless HDL Toolbox 模块一起使用的控制信号总线中选择信号

Sample Control Bus Selector 模块从 `samplecontrol` 总线中选择信号。该总线用于为硬件通信系统中的流控制信号建模。请参阅 Sample Control Bus。

该模块是 Simulink® Bus Selector 模块的实现。有关更多信息，请参阅 Bus Selector。
