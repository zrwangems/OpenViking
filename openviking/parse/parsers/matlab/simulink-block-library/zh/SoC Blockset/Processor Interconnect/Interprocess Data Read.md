---
type: simulink-block
title: 'Interprocess Data Read'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Processor Interconnect'
documentation_page: 'interprocessdataread'
documentation_source_path: 'ref/interprocessdataread.html'
language: zh-CN
chinese_source: worker-translation
---

# Interprocess Data Read

## 端口

### 输入

### **msg** — 来自进程间数据通道的数据消息 标量

此消息端口接收来自所连接的 Interprocess Data Channel 模块的数据消息。当 Task Manager 模块触发包含此模块的任务时，这些消息会被处理。有关消息的详细信息，请参阅 Messages。

#### 依赖关系

此端口仅在 **Enable simulation port** 参数启用时出现。

**数据类型：** `SoCData`
### 输出

### **data** — 从另一个处理器读取的数据帧 向量

此端口输出通过 Interprocess data Channel 模块从另一个处理器读取的数据帧。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `bus`

### **status** — 进程间数据读取状态 0 | 1 | 2 | 4 | 6

状态端口输出以下值之一：

- `0—`无错误
- `1—`数据不可用
- `2—`数据类型不匹配
- `4—`数据长度不匹配
- `6—`数据类型和数据长度不匹配

#### 依赖关系

此端口在您禁用 **Enable simulation port** 参数时出现。

## 参数

### **Enable simulation port** — 启用外设仿真端口以进行阻塞 `on`（默认）| `off`

选择此参数以配置 **msg** 输出端口，从而启用外设仿真功能。

### **Data type** — 进程间数据通道的数据类型 `double`（默认）| `single` | `int8` | `int16` | `int32` | `int64` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `uint64` | `Boolean` | `bus`

输入进程间数据通道所使用的数据类型。

您可以通过点击 >> 按钮或 << 按钮来选择性地显示或隐藏 **Data Type Assistant** 选项。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

### **Circular FIFO depth** — 存储缓冲区数量 `1`（默认）| 正整数

缓冲区是在共享消息 RAM 中创建的循环缓冲区。缓冲区数量是共享消息 RAM 中一次存储的元素数量。这些不是 FIFO，但会在下一次实例时被覆盖。

确保在 Tx 和 Rx 两侧指定的缓冲区数量必须相同。

#### 依赖关系

此参数仅在您禁用 **Enable simulation port** 参数时可见。

### **Circular FIFO element size** — 从进程间数据通道读取的数据向量大小 `1`（默认）| 正整数

输入从进程间数据通道读取的数据向量的循环 FIFO 元素大小。

### **Channel number** — 选择通道号 `0`（默认）| `1` | `2` | `...`

选择您要发送数据的通道。

#### 依赖关系

此参数仅在您禁用 **Enable simulation port** 参数时可见。

### **Participating cores** — 选择处理器的参与核心 `选项因您选择的硬件板而异`

根据您在 Configuration Parameters 窗口中选择的 **Hardware board** 选择参与核心。

#### 依赖关系

此参数仅在您禁用 **Enable simulation port** 参数时可见。

**注意**

确保模型中对应的 Interprocess Data Read 和 Interprocess Data Write 模块的 **Channel number**、**Number of buffers** 和 **Participating cores** 参数相匹配。

### **Sample time** — 采样时间 `-1`（默认）| 正标量

输入模块的采样时间，以应用于定时器驱动的任务子系统。

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

Interprocess data Read 模块使用进程间数据通道从 SoC 中的另一个处理器异步接收消息。Interprocess Data Read 模块连接到一个 Interprocess Data Channel 模块，该模块同样连接到一个包含在独立处理器参考模型中的 Interprocess Data Write 模块。在仿真中，来自另一个处理器的数据在包含 Interprocess Data Read 模块及相关异步任务的处理器中被异步接收和处理。此图展示了处理器间数据通道连接的通用视图。

**注意**

- 确保在 Tx 和 Rx 两侧指定的缓冲区数量必须相同。
- 如果您使用多处理器建模方法，通过 Task manager 使用单个模型触发多个核心，请使用 Interprocess Data Read 和 Interprocess Data Write 模块在内核之间发送和接收数据。

进程间数据通道图。
