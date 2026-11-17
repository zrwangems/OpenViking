---
type: simulink-block
title: 'Interprocess Data Channel'
family: 'test-bench-blocks'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Test Bench Blocks'
documentation_page: 'interprocessdatachannel'
documentation_source_path: 'ref/interprocessdatachannel.html'
language: zh-CN
chinese_source: worker-translation
---

# Interprocess Data Channel

## 端口

### 输入

### **datain** — 输入数据消息标量

此消息端口从连接的 Interprocess Data Write 模块接收输入数据作为消息。有关消息的详细信息，请参阅 Messages。

**数据类型：** `SoCData`
### 输出

### **dataout** — 输出数据消息标量

此消息端口将输出数据作为消息发送到连接的 Interprocess Data Read 模块。有关消息的详细信息，请参阅 Messages。

**数据类型：** `SoCData`

### **overwritten** — 输出覆盖通知信号标量

每当内部缓冲区队列发生覆盖时，此端口发送 true 信号输出。当连接的处理器模型在外部模式中执行时，连接的 Interprocess Data Write 模块在 Simulation Data Inspector 工具中生成 **overwritten** 信号。

#### 依赖关系

要启用此端口，请选择 **Show when buffer is overwritten** 参数。

**数据类型：** `Boolean`

### **used** — 输出使用中缓冲区数量标量

此端口输出模块内部缓冲区队列中当前正在使用的缓冲区数量。当连接的处理器模型在外部模式中执行时，连接的 Interprocess Data Write 模块在 Simulation Data Inspector 工具中生成 **used** 信号。

#### 依赖关系

要启用此端口，请选择 **Show number of used buffers** 参数。

**数据类型：** `Boolean`

### **event** — 任务事件信号标量

此端口发送任务事件信号，触发 Task Manager 模块执行关联的事件驱动任务。

**注意**

- 如果模型中有一个 Interprocess Data Channel 模块，则仅允许 `IPC0` 中断
- 如果模型中有两个 Interprocess Data Channel 模块，则仅允许 `IPC0` 和 `IPC1` 中断。

#### 依赖关系

要启用此端口，请选择 **Show event port** 参数。

**数据类型：** `rteEvent`

## 参数

#### 主要

### **Circular FIFO depth** — 存储缓冲区数量 `1`（默认） | positive integer

缓冲区是在共享消息 RAM 中创建的循环缓冲区。缓冲区数量是一次存储在共享消息 RAM 中的元素数量。这些不是 FIFO，而会在下一实例中被覆盖。

### **Propagation delay** — 数据通过通道的传播延迟 `1e-6`（默认） | non-negative number

指定数据通过此模块的传输传播延迟。要忽略传播延迟，请将此参数设置为 `0`。

### **Show event port** — 启用任务事件端口的选项 `off`（默认） | `on`

启用一个事件端口，该端口连接到 Task Manager 模块后，可以执行事件驱动任务。

#### 统计

### **Show number of used circular FIFO** — 启用循环 FIFO 计数端口的选项 `off`（默认） | `on`

启用一个输出端口，显示 Interprocess Data Channel 模块内部缓冲区队列中当前使用的循环 FIFO 数量。

### **Show when circular FIFO is overwritten** — 启用显示循环 FIFO 覆盖的端口 `off`（默认） | `on`

启用一个输出端口，当 Interprocess Data Channel 模块内部循环 FIFO 队列发生覆盖时发出信号。

## 所属库

SoC Blockset / Processor Interconnect C2000 Microcontroller Blockset / Test Bench Blocks Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Test Bench Blocks Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Test Bench Blocks

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2020b 中引入**

## 描述

对两个处理器之间的处理器间数据通道进行建模

Interprocess Data Channel 模块模拟多处理器或 OS 管理的 SoC 硬件板系列中可用的处理器间数据通道。该模块提供两个处理器之间异步数据传输的通道。此图显示处理器间数据连接的通用视图。

处理器间数据通道图。

**注意**

如果您使用多处理器建模方法，其中单个模型使用 Task manager 触发多个核，请使用 Interprocess Data Read 和 Interprocess Data Write 模块在核之间发送和接收数据。

对于多核处理器，使用 IPC Receive 和 IPC Transmit 模块接收或发送数据到任一核。将这些模块用于扁平模型方法，其中您为每个核使用单独的模型。

为帮助您为应用选择正确的解决方案，请参阅 Communication Between Cores Using IPC Blocks，了解 IPC Transmit/Receive 模块与 Interprocess Data Read/Write 模块之间的详细比较。
