---
type: simulink-block
title: 'Interprocess Data Read'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Target Communication'
documentation_page: 'interprocessdataread'
documentation_source_path: 'ref/interprocessdataread.html'
language: zh-CN
chinese_source: worker-translation
---

# Interprocess Data Read

## 端口

### 输入

### **msg** — 来自进程间数据通道的标量数据消息

此消息端口从连接的 Interprocess Data
Channel 模块接收数据消息。当 Task Manager 模块触发包含此模块的任务时，消息会进行处理。有关消息的详细信息，请参阅 Messages。

#### 依赖关系

仅当启用 **Enable simulation port**
参数时，此端口才会出现。

**数据类型：** `SoCData`
### 输出

### **data** — 从另一个处理器读取的数据帧向量

此端口发出通过 Interprocess data Channel 模块从另一个处理器读取的数据帧。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `bus`

### **status** — 进程间数据读取状态 0 | 1 | 2 | 4 | 6

状态端口输出以下值之一：

- `0—`无错误
- `1—`数据不可用
- `2—`数据类型不匹配
- `4—`数据长度不匹配
- `6—`数据类型和数据长度不匹配

#### 依赖关系

禁用 **Enable simulation
port** 参数时，此端口会出现。

## 参数

### **Enable simulation port** — 为模块启用外设仿真端口 `on` (default) | `off`

选择此参数以配置 **msg** 输出端口，
以启用外设仿真功能。

### **Data type** — 进程间数据通道的数据类型 `double` (default) | `single` | `int8` | `int16` | `int32` | `int64` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `uint64` | `Boolean` | `bus`

输入进程间数据通道所使用的数据类型。

你可以通过单击 >> 按钮或 << 按钮来选择性地显示或隐藏 **Data Type
Assistant** 选项。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

### **Circular FIFO depth** — 存储缓冲区数量 `1` (default) | 正整数

缓冲区是在共享消息 RAM 中创建的循环缓冲区。缓冲区数量是一次存储在共享消息 RAM 中的元素数量。它们不是 FIFO，但将在下一次实例时被覆盖。

确保在 Tx 和 Rx 两侧指定的缓冲区数量必须相同。

#### 依赖关系

仅当禁用 **Enable simulation
port** 参数时，此参数可见。

### **Circular FIFO element size** — 从进程间数据通道读取的数据向量大小 `1` (default) | 正整数

输入从进程间数据通道读取的数据向量的循环 FIFO 元素大小。

### **Channel number** — 选择通道编号 `0` (default) | `1` | `2` | `...`

选择要将数据发送到的通道。

#### 依赖关系

仅当禁用 **Enable simulation
port** 参数时，此参数可见。

### **Acknowledge interrupts** — 选择以确认中断 `off` (default) | `on`

选择此参数以在接收核心确认 IPC 中断，从而接收更多数据。

#### 依赖关系

仅当禁用 **Enable simulation
port** 参数时，此参数可见。

### **Participating cores** — 选择处理器的参与核心 `The options vary based on the hardware board you select`

根据你在配置参数窗口中选择的 **Hardware board**，选择参与核心。

#### 依赖关系

仅当禁用 **Enable simulation
port** 参数时，此参数可见。

**注意**

确保模型对应的 Interprocess Data Read 和 Interprocess Data Write 模块的 **Channel number**、**Number of
buffers** 和 **Participating cores** 参数匹配。

### **Sample time** — 采样时间 `-1` (default) | 正标量

输入要应用于定时器驱动任务子系统的模块采样时间。

## 所属库

SoC Blockset / Processor Interconnect C2000 Microcontroller Blockset / Target Communication Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Target Communication Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Target Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

使用进程间通信通道从另一个处理器接收消息

Interprocess data Read 模块使用进程间数据通道异步接收来自 SoC 中另一个处理器的消息。Interprocess Data Read 模块连接到 Interprocess Data Channel 模块，后者类似地连接到包含在单独处理器参考模型中的 Interprocess Data Write 模块。在仿真中，来自另一个处理器的数据由包含 Interprocess Data Read 模块及相关异步任务的处理器异步接收和处理。此图显示了处理器间数据通道连接的总体视图。

**注意**

- 确保在 Tx 和 Rx 两侧指定的缓冲区数量必须相同。
- 如果你使用多处理器建模方法，即使用 Task manager 通过单个模型触发多个核心，请使用 Interprocess Data Read 和 Interprocess Data Write 模块在内核之间发送和接收数据。

  对于多核处理器，使用 IPC Receive 和 IPC Transmit 模块向任一内核接收或发送数据。对于平面模型方法（你为每个内核使用单独模型），请使用这些模块。

  为帮助你的应用选择合适的解决方案，请参阅 Communication Between Cores Using IPC Blocks，了解 IPC Transmit/Receive 模块与 Interprocess Data Read/Write 模块之间的详细比较

进程间数据通道图。
