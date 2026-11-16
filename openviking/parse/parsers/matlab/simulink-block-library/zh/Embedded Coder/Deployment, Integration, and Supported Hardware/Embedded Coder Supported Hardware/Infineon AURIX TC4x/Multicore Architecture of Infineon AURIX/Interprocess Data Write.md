---
type: simulink-block
title: 'Interprocess Data Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / Interprocess Data Communication'
documentation_page: 'interprocessdatawrite'
documentation_source_path: 'ref/interprocessdatawrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Interprocess Data Write

## 端口

### 输入

### **data** — 数据输入向量

此端口接收要通过处理器间数据通道发送到另一个处理器的数据向量。

**数据类型：** `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### 输出

### **msg** — 输出数据消息标量

此消息端口将输出数据作为消息发送到连接的 Interprocess Data Channel 模块。有关消息的详细信息，请参阅 Messages。

#### 依赖关系

此端口仅在启用 **Enable simulation port** 参数时出现。

**数据类型：** `SoCData`

## 参数

### **Enable simulation port** — 为模块启用外设仿真端口 `on` (默认) | `off`

选择此参数可将 **msg** 输出端口配置为启用外设仿真功能。

### **Channels number** — 选择通道编号 `0` (默认) | `1` | `2` | `...`

选择要发送数据的通道。

#### 依赖关系

仅当禁用 **Enable simulation port** 参数时，此参数才可见。

### **Circular FIFO depth** — 存储缓冲区数量 `1` (默认) | 正整数

缓冲区是在共享消息 RAM 中创建的循环缓冲区。缓冲区数量是一次存储在共享消息 RAM 中的元素数量。这些不是 FIFO，但在下一次实例时将被覆盖。

确保指定的缓冲区数量在 Tx 和 Rx 侧必须相同。

#### 依赖关系

仅当禁用 **Enable simulation port** 参数时，此参数才可见。

### **Participating cores** — 选择处理器的参与核心 `选项因所选的硬件板而异`

根据你在 Configuration Parameters 窗口中选择的 **Hardware board**，选择参与核心。

#### 依赖关系

仅当禁用 **Enable simulation port** 参数时，此参数才可见。

**注意**

确保模型中对应的 Interprocess Data Read 和 Interprocess Data Write 模块的 **Channel number**、**Number of buffers** 和 **Participating cores** 参数匹配。

## 所属库

SoC Blockset / Processor Interconnect C2000 Microcontroller Blockset / Target Communication Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Target Communication Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Target Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

使用处理器间数据写入向另一个处理器发送消息

Interprocess Data Write 模块使用处理器间数据通道异步地向 SoC 中的另一个处理器发送消息。Interprocess Data Write 模块连接到 Interprocess Data Channel 模块，后者类似地连接到包含在单独处理器参考模型中的 Interprocess Data Read 模块。在仿真中，来自当前处理器的数据被异步发送到包含 Interprocess Data Read 模块和相关异步任务的处理器中并进行处理。此图展示了处理器间数据通道的概括视图。

**注意**

- 确保指定的缓冲区数量在 Tx 和 Rx 侧必须相同。
- 如果你使用多处理器建模方法，其中单个模型使用 Task manager 触发多个核心，请使用 Interprocess Data Read 和 Interprocess Data Write 模块在核心之间发送和接收数据。

处理器间数据通道图。

要为 SoC 模型生成并执行 C 代码，此模块需要 Embedded Coder® Support Package for Infineon® AURIX™ TC4x Microcontrollers 或 Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers。
