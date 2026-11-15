---
type: simulink-block
title: 'Stream Write'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory / Processor Software Connectivity'
documentation_page: 'streamwrite'
documentation_source_path: 'ref/streamwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Stream Write

## 端口

### 输入

### **data** — 来自软件算法的数据帧向量

此端口接收来自软件算法的数据帧。然后，该模块将数据作为消息流式传输到 Memory Channel 模块中定义的共享内存区域。

**数据类型：** `uint16` | `uint32` | `uint64` | `fixdt(0,128,0)`

### **done** — 内存中可用缓冲区的通知 `scalar`

此消息端口接收来自连接的 Memory Channel 或 IO Data Sink 模块的通知。该通知指示读事务已完成，并且内存中有缓冲区可用于写入。

**数据类型：** `Boolean`

### 输出

### **msg** — 到内存的数据消息标量

当内存中有可用缓冲区空间时，此消息端口向连接的 Memory Channel 或 IO Data Sink 模块发出数据消息。有关消息的详细信息，请参阅 Messages。

**数据类型：** `SoCData`

### **status** — 已完成写事务的状态 `scalar`

在对内存发生写事务后，此端口向处理器发送 true 状态（`1`）。使用此状态可对丢弃帧进行计数。

**数据类型：** `Boolean`

## 参数

### **Device name** — IP 核设备名称 `ip:MM2S` (default) | 以冒号分隔的 IP 核名称和通道列表

设备名称参数由 SoC Builder 工具生成。将 FPGA 上 IP 核的名称和通道输入为以冒号分隔的列表。

### **Number of buffers** — 数据缓冲区数量 `3` (default) | 正整数

输入物理内存中的数据帧缓冲区数量。此数值必须与 Memory Channel 或 IO Data Sink 模块中的 **Number of buffers** 参数匹配。

### **Enable event-based execution** — 启用事件驱动任务执行的选项 `on` (default) | `off`

- 选择此参数可在事件驱动任务子系统使用此模块。在这种情况下，每当共享内存区域中有空缓冲区可用时，该模块都会写入 Memory Channel 模块。
- 清除此参数可在定时器驱动任务子系统使用此模块。在这种情况下，该模块在每个采样时间将数据写入共享内存区域。

## 所属库

SoC Blockset / Processor I/O

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要为您的设计自动生成 C 代码，并在 SoC 设备上执行，请使用 SoC Builder 工具。要为您的 SoC 模型生成并执行 C 代码，需要 Embedded Coder® 功能。有关为 SoC 设计生成代码的详细信息，请参阅 Use SoC Builder to Generate SoC Design。

SoC Builder 工具使用采用 AXI4-stream 通信协议的 FPGA 和处理器 IP 来实现 Stream Write、Stream Read、Memory Channel 和 Task Manager 模块。AXI4-stream 协议使用直接内存访问（DMA）将数据向量读取到外部内存上的共享区域。此协议支持通过外部内存在 FPGA 与嵌入式处理器之间高速流式传输数据。

## 版本历史

**在 R2020b 中引入**

## 描述

将数据从处理器算法流式传输到共享内存

Stream Write 模块将来自处理器算法的数据流式传输到 Memory Channel 模块中的共享内存。Stream Write 模块有一个内部计数器，用于跟踪共享内存中空缓冲区的数量。成功从内存读取后，内存会向 Stream Write 模块发送 done 信号。然后，该模块递增计数器，断言内存中有缓冲区可用。如果至少有一个缓冲区可用于写入，则写事务成功。Stream Write 模块向软件发送 `True` 状态。您可以使用此状态信号执行诸如对丢弃帧进行计数或发出重写请求等操作。

在仿真中，定时器驱动或事件驱动任务子系统包含 Stream Write 模块。来自软件算法的数据信号连接到 Stream Write 模块。写事务作为消息发出到 Memory channel 模块。在从共享内存执行读操作后，Memory Channel 模块通过 `done` 信号将读事件通知给 Stream Write 模块。
