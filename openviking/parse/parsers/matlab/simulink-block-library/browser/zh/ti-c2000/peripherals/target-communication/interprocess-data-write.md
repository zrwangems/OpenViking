---
type: simulink-block
title: 'Interprocess Data Write'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / C28x'
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

选择此参数以配置 **msg** 输出端口，从而启用外设仿真能力。

### **Channels number** — 选择通道号 `0` (默认) | `1` | `2` | `...`

选择要发送数据的通道。

#### 依赖关系

仅当禁用 **Enable simulation port** 参数时，此参数才可见。

### **Circular FIFO depth** — 存储缓冲区数量 `1` (默认) | 正整数

缓冲区是在共享消息 RAM 中创建的循环缓冲区。缓冲区数量是在共享消息 RAM 中一次存储的元素数量。它们不是 FIFO，但会在下一实例中被覆盖。

确保在 Tx 和 Rx 两侧指定的缓冲区数量必须相同。

#### 依赖关系

仅当禁用 **Enable simulation port** 参数时，此参数才可见。

### **Trigger interrupt on receiving core** — 选择以触发中断 `off` (默认) | `on`

选择此参数以在接收核上触发 IPC 中断。

#### 依赖关系

仅当禁用 **Enable simulation port** 参数时，此参数才可见。

### **Participating cores** — 选择处理器的参与核 `选项根据您选择的 Hardware board 而变化`

根据您在 Configuration Parameters 窗口中选择的 **Hardware board** 选择参与核。

#### 依赖关系

仅当禁用 **Enable simulation port** 参数时，此参数才可见。

**注意**

确保模型中对应的 Interprocess Data Read 和 Interprocess Data Write 模块的 **Channel number**、**Number of buffers** 和 **Participating cores** 参数匹配。

## 所属库

SoC Blockset / Processor Interconnect C2000 Microcontroller Blockset / Target Communication Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Target Communication Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Target Communication

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2020b 中引入**

## 描述

使用处理器间数据写入将消息发送到另一个处理器

Interprocess Data Write 模块使用进程间数据通道异步地将消息发送到 SoC 中的另一个处理器。Interprocess Data Write 模块连接到 Interprocess Data Channel 模块，后者类似地连接到包含在单独处理器参考模型中的 Interprocess Data Read 模块。在仿真中，来自当前处理器的数据被异步发送，并在包含 Interprocess Data Read 模块及相关异步任务的处理器中处理。此图显示了进程间数据通道的通用视图。

**注意**

- 确保在 Tx 和 Rx 两侧指定的缓冲区数量必须相同。
- 如果您使用多处理器建模方法，并通过 Task manager 使用单个模型触发多个核，请使用 Interprocess Data Read 和 Interprocess Data Write 模块在核之间发送和接收数据。

  对于多核处理器，使用 IPC Receive 和 IPC Transmit 模块接收或发送数据到任一核。当您为每个核使用单独模型（扁平模型方法）时，请使用这些模块。

  为帮助您为应用选择合适的解决方案，请参阅 Communication Between Cores Using IPC Blocks，以了解 IPC Transmit/Receive 模块与 Interprocess Data Read/Write 模块之间的详细比较

进程间数据通道示意图。
