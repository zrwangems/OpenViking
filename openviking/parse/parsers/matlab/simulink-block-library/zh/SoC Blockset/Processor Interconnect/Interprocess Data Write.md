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

此端口接收要通过进程间数据通道发送到另一个处理器的数据向量。

**数据类型：** `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### 输出

### **msg** — 输出数据消息标量

此消息端口将输出数据作为消息发送到连接的 Interprocess Data Channel 模块。有关消息的详细信息，请参阅 Messages。

#### 依赖关系

仅当启用 **Enable simulation port** 参数时，此端口才会出现。

**数据类型：** `SoCData`

## 参数

### **Enable simulation port** — 为模块启用外设仿真端口 `on` (默认) | `off`

选择此参数以配置 **msg** 输出端口，从而启用外设仿真功能。

### **Channels number** — 选择通道编号 `0` (默认) | `1` | `2` | `...`

选择要发送数据的通道。

#### 依赖关系

仅当禁用 **Enable simulation port** 参数时，此参数才可见。

### **Circular FIFO depth** — 存储缓冲区数量 `1` (默认) | 正整数

缓冲区是在共享消息 RAM 中创建的循环缓冲区。缓冲区数量是共享消息 RAM 中一次存储的元素数量。它们不是 FIFO，但在下一次实例时将被覆盖。

确保指定的缓冲区数量在 Tx 和 Rx 两侧必须相同。

#### 依赖关系

仅当禁用 **Enable simulation port** 参数时，此参数才可见。

### **Participating cores** — 选择处理器的参与核心 `The options vary based on the hardware board you select`

根据你在 Configuration Parameters 窗口中选择的 **Hardware board**，选择参与核心。

#### 依赖关系

仅当禁用 **Enable simulation port** 参数时，此参数才可见。

**注意**

确保模型对应的 Interprocess Data Read 和 Interprocess Data Write 模块的 **Channel number**、**Number of buffers** 和 **Participating cores** 参数匹配。

## 所属库

SoC Blockset / Processor Interconnect C2000 Microcontroller Blockset / Target Communication Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Target Communication Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Target Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

使用处理器间数据写入将消息发送到另一个处理器

Interprocess Data Write 模块使用进程间数据通道异步地将消息发送到 SoC 中的另一个处理器。Interprocess Data Write 模块连接到 Interprocess Data Channel 模块，后者同样连接到包含在单独处理器参考模型中的 Interprocess Data Read 模块。在仿真中，来自当前处理器的数据会被异步发送，并在包含 Interprocess Data Read 模块和相关异步任务的处理中进行处理。此图显示了进程间数据通道的总体视图。

**注意**

- 确保指定的缓冲区数量在 Tx 和 Rx
  两侧必须相同。
- 如果你正在使用单模型通过 Task manager 触发
  多个核心的多处理器建模方法，请使用 Interprocess Data Read 和 Interprocess
  Data Write 模块在核心之间发送和接收数据。

进程间数据通道图。
