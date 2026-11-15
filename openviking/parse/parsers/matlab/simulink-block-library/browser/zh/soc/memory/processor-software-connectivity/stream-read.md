---
type: simulink-block
title: 'Stream Read'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory / Processor Software Connectivity'
documentation_page: 'streamread'
documentation_source_path: 'ref/streamread.html'
language: zh-CN
chinese_source: worker-translation
---

# Stream Read

## 端口

### 输出

### **data** — 来自共享内存向量的数据帧

此端口发出从 Memory Channel 模块中定义的共享内存区域读取的数据帧。

**数据类型：** `uint16` | `uint32` | `uint64` | `fixdt(0,128,0)`

### **valid** — 有效帧数据标量

一个标志，指示从内存通道读取的数据帧是否有效。

**数据类型：** `Boolean`

### **done** — 读取完成通知消息标量

此消息端口以消息形式向连接的 Memory Channel 或 IO Data Source 模块发送读取已完成的通知。有关消息的详细信息，请参阅消息。

**数据类型：** `Boolean`

### 输入

### **msg** — 来自内存的数据消息标量

此消息端口从连接的 Memory Channel 或 IO Data Source 模块接收数据消息。当 Task Manager 模块触发包含 Stream Read 模块的任务时，会处理这些消息。有关消息的详细信息，请参阅消息。

**数据类型：** `SoCData`

## 参数

#### 主要

### **设备名称** — IP 核设备名称 `ip:s2mm0`（默认）| 以冒号分隔的 IP 核名称和通道列表

以冒号分隔列表的形式输入 FPGA 上 IP 核的名称和通道。

### **输出数据类型** — IP 核的数据类型 `uint32`（默认）| `uint16` | `uint64` | `fixdt(0,128,0)`

输入内存通道使用的数据类型。

### **每帧样本数** — 从 IP 核读取的数据向量大小 `1024`（默认）| 正标量整数

输入从内存通道读取的数据向量的大小。

### **缓冲区数量** — 数据缓冲区数量 `16`（默认）| 正整数

输入物理内存中数据帧缓冲区的数量。此数量应与 Memory Channel 模块或 IO Data Source 模块中的 **缓冲区数量** 参数匹配。

### **启用基于事件的执行** — 启用事件驱动的任务执行 `on`（默认）| `off`

要在事件驱动的任务子系统中使用此模块，请选中此参数。要在定时器驱动的任务子系统中使用此模块，请清除此参数。

选中 **启用基于事件的执行** 时，每当共享内存区域中有完整缓冲区可用时，此模块都会从 Memory Channel 读取。清除 **启用基于事件的执行** 时，此模块会在每个采样时间读取共享内存区域中的数据。

### **采样时间** — 以 seconds 为单位的采样时间 `-1`（默认）| 正标量

当清除 **启用基于事件的执行** 时，输入定时器驱动的任务子系统使用的采样时间。

## 所属库

SoC Blockset / Processor I/O

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要为您的设计自动生成 C 代码并在 SoC 设备上执行，请使用 SoC Builder 工具。要为您的 SoC 模型生成并执行 C 代码，需要 Embedded Coder® 功能。有关为 SoC 设计生成代码的更多信息，请参阅使用 SoC Builder 生成 SoC 设计。

SoC Builder 工具使用采用 AXI4-stream 通信协议的 FPGA 和处理器 IP 实现 Stream Read、Stream Write、Memory Channel 和 Task Manager 模块。AXI4-stream 协议使用直接内存访问 (DMA) 将数据向量读取到外部内存上的共享区域。此协议支持通过外部内存在 FPGA 和嵌入式处理器之间进行高速数据流传输。此图显示了生成的代码实现的通用表示。

## 版本历史

**在 R2019a 中引入**

## 描述

将数据从共享内存流式传输到处理器算法

Stream Read 模块将数据从内存通道中的共享内存流式传输到您的处理器算法。在仿真中，定时器驱动或事件驱动的任务子系统包含 Stream Read 模块。来自 Memory Channel 模块的数据信号连接到 Stream Read 模块。在写入共享内存之后，Memory Channel 会向 Task Manager 模块通知写入事件。然后，Task Manager 模块会触发包含 Stream Read 模块及相关算法的事件驱动子系统。

在开发或分析 SoC 应用的软件端时，Stream Read 模块可以连接到 IO Data Source 模块。在此配置中，IO Data Source 模块提供先前记录的数据或人工数据，从而能够更有针对性地仿真应用的软件和处理器端，而无需显式对硬件和内存交互进行建模。
