---
type: simulink-block
title: 'LTE Gold Sequence Generator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized System Design / Utilities'
documentation_page: 'ltegoldsequencegenerator'
documentation_source_path: 'ref/ltegoldsequencegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# LTE Gold Sequence Generator

## 端口

### 输入

### **load** — 加载初始移位寄存器值 标量

当此控制信号设置为 `true` (1) 时，模块将 **init** 端口上的值加载到移位寄存器中。可以使用此信号在任何时间点重新启动序列。

**数据类型：** `Boolean`

### **init** — 初始移位寄存器值 标量 | 向量

初始移位寄存器值，指定为表示 31 个二进制值的 `ufix31` 数字。要并行生成多个 Gold 序列输出，请指定初始值向量以表示多个信道。

**数据类型：** `ufix31`

### **enable** — 启用序列生成 标量

当此控制信号设置为 `true` (1) 时，它会启用 Gold 序列生成。

**数据类型：** `Boolean`
### 输出

### **data** — 生成的 Gold 序列 标量 | 向量

生成的 Gold 序列，返回为 `Boolean` 标量或向量，具体取决于 **init** 输入的大小。如果 **init** 是向量，则 **data** 是相同大小的向量，表示独立信道上的序列。

**数据类型：** `Boolean`

### **valid** — 指示有效输出数据 标量

指示 **data** 输出端口何时有效的控制信号。

**数据类型：** `Boolean`

## 参数

未在 R2025b 中记录。

## 所属库

Wireless HDL Toolbox / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计中移动现有延迟在输出处放置的寄存器数。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2018a 中引入**

## 描述

生成 Gold 序列

LTE Gold Sequence Generator 模块返回使用 LTE 标准 TS 36.212 [1] 指定的多项式和移位长度生成的 Gold 序列。Gold 码是具有高自相关性和低互相关性的伪随机序列。由于这些特性，Gold 码广泛用于通信系统。例如，它们用于区分工作在同一频率上的不同移动小区。LTE 系统将 Gold 序列生成器用于参考符号以及数据加扰/解扰，例如在 MIB 和 SIB 编码和解码中。

此模块通过并行实现移位寄存器初始化来提供最小延迟。

使用 **load** 控制信号指示 **init** 值何时有效。使用 **enable** 控制信号请求下一个 Gold 序列值。**valid** 信号指示输出样本何时可用。第一个输出样本在 **enable** 置为有效后三个周期准备好。**data** 和 **valid** 输出遵循 **enable** 输入的模式。
