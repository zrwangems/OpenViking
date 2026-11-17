---
type: simulink-block
title: 'Interprocess Data Write'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Processor Interconnect'
documentation_page: 'interprocessdatawrite'
documentation_source_path: 'ref/interprocessdatawrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Interprocess Data Write

## 端口

### 输入

### **data** — 数据输入向量

此端口接收一个数据向量，以通过进程间数据通道将其发送到另一个处理器。

**数据类型：** `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### 输出

### **msg** — 输出数据消息标量

此消息端口将输出数据作为消息发送到所连接的 Interprocess Data Channel 模块。有关消息的详细信息，请参阅“消息”。

#### 依赖关系

仅当启用 **Enable simulation port** 参数时，才会显示此端口。

**数据类型：** `SoCData`

## 参数

### **Enable simulation port** — 为模块启用外设仿真端口 `on`（默认） | `off`

选择此参数可配置 **msg** 输出端口，以启用外设仿真功能。

### **Channels number** — 选择通道编号 `0`（默认） | `1` | `2` | `...`

选择要发送数据的通道。

#### 依赖关系

仅当禁用 **Enable simulation port** 参数时，此参数才可见。

### **Circular FIFO depth** — 存储缓冲区的数量 `1`（默认） | 正整数

缓冲区是在共享消息 RAM 中创建的循环缓冲区。缓冲区数量即为共享消息 RAM 中一次存储的元素数量。这些缓冲区不是 FIFO，其中的数据会在下一轮时被覆盖。

确保 Tx 和 Rx 端指定的缓冲区数量相同。

#### 依赖关系

仅当禁用 **Enable simulation port** 参数时，此参数才可见。

### **Participating cores** — 选择处理器中参与的内核 `选项根据您选择的硬件板而有所不同`

根据您在“配置参数”窗口中选择的 **Hardware board**，选择参与的内核。

#### 依存关系

仅当禁用 **Enable simulation port** 参数时，此参数才可见。

**注意**

确保模型中对应的 Interprocess Data Read 和 Interprocess Data Write 模块的
**Channel number**、**Number of buffers** 和 **Participating cores** 参数相匹配。

## 所属库

SoC Blockset / Processor Interconnect C2000 Microcontroller Blockset / Target Communication Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Target Communication Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Target Communication

## 模块特性

R2025b 中未提供相关文档。

## 扩展功能

R2025b 中未提供相关文档。

## 版本历史

**在 R2020b 中推出**

## 描述

通过处理器间数据写入向另一处理器发送消息

Interprocess Data Write 模块通过进程间数据通道，将消息异步发送到 SoC 中的另一个处理器。Interprocess Data Write 模块连接到一个
Interprocess Data Channel 模块，该模块同样连接到包含在独立处理器引用模型中的 Interprocess Data Read 模块。在仿真中，来自当前处理器的数据以异步方式发送，并在包含 Interprocess Data Read 模块及其关联异步任务的处理器中进行处理。此图显示进程间数据通道的通用视图。

**注意**

- 确保 Tx 和 Rx 端指定的缓冲区数量相同。
- 如果使用多处理器建模方法，通过 Task manager 让单个模型触发多个核，请使用 Interprocess Data Read 和 Interprocess Data Write 模块在各核之间发送和接收数据。

进程间数据通道示意图。
