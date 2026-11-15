---
type: simulink-block
title: 'TCP Receive'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Network'
documentation_page: 'tcpreceiveblock'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/tcpreceiveblock.html'
language: zh-CN
chinese_source: worker-translation
---

# TCP Receive

## 端口

### 输出

### **Data** — 输出数据向量

在每个时间步，端口按照您在 **Data size (N)** 参数中指定的大小，将数据作为向量输出。有关详细信息，请参阅接收数据的输出。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Status** — 在给定时间步接收到的请求数据 标量

在每个时间步，当接收到的数据长度大于或等于 **Data size (N)** 参数中指定的长度时，端口输出 `0`。值 `0` 表示在给定时间步收到了请求的数据。否则，它输出一个非零值，表示未收到新数据。

有关详细信息，请参阅接收数据的输出。

#### 依赖关系

要启用此端口，请选择 **Output error status** 参数。

**数据类型：** `uint16`

## 参数

### **Connection mode** — 将模块设置为服务器或客户端 `Server`（默认）| `Client`

将模块设置为 TCP/IP 服务器或客户端。

当您将此参数设置为 `Server` 时，必须提供 **Local IP Port**。本地端口充当 TCP/IP 服务器上的监听端口。

当您将此参数设置为 `Client` 时，必须提供要从其接收数据的 TCP/IP 服务器上的 **Server IP Address** 和 **Server IP Port**。

### **Local IP Port** — 接收主机上从其接收数据的 IP 端口 `25000`（默认）| 1 到 65,535 的任意整数

此本地端口号充当 TCP/IP 服务器上的监听端口。将本地端口号与发送主机的远程端口号匹配。

### **Server IP Address** — 从其接收数据的服务器的远程 IP 地址 `192.168.1.2`（默认）| 任何有效 IP 地址

指定从其接收数据的发送服务器的 IP 地址。

#### 依赖关系

要启用此参数，请将 **Connection mode** 参数设置为 `Client`。

### **Server IP Port** — 服务器上从其接收数据的远程 IP 端口 `25000`（默认）| 1 到 65,535 的任意整数

指定从其接收数据的发送服务器上的端口号。

#### 依赖关系

要启用此参数，请将 **Connection mode** 参数设置为 `Client`。

### **Wait until data received** — 等待直到请求的数据可用 `off`（默认）| `on`

- 选中此参数时，读取操作以阻塞模式运行。在等待请求的数据可用时，读取操作被阻塞。如果数据可用，**Data** 端口输出数据。如果数据不可用，**Data** 端口等待数据。

  如果当计划开始下一次读取操作时，目标硬件仍在等待数据可用，则会发生任务超限。

  要修复超限：

  - 使用 **Sample time** 参数增大时间步长。
  - 使用 **Data size (N)** 参数减少请求的数据长度。
- 清除此参数时，读取操作以非阻塞模式运行。读取数据时，如果数据不可用，**Data** 端口包含上一时间步接收到的数据。**Status** 端口输出 `0`。在此模式下，模块不会等待请求的数据可用。

### **Data type** — 接收数据的数据类型 `uint8`（默认）| `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

指定模块从发送主机接收的数据的类型。每个元素的大小取决于其数据类型。

### **Data size (N)** — 接收数据中的数据字节数 `1`（默认）| 任何正整数

指定每个时间步要接收的数据字节数。

### **Output error status** — 在数据传输期间显示错误状态的选项 `off`（默认）| `on`

选择此参数以在数据传输期间显示错误状态。

当您选择 Output error status 参数时，模块会配置一个输出端口。模块上的该端口标记为 Status，表示模块在输出端口输出读取操作的状态。

### **Sample time** — 模块从发送主机读取数据的时间间隔 `-1`（默认）| 非负值

当您将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

## 描述

通过 TCP/IP 网络从远程主机接收数据

TCP Receive 模块通过网络从远程主机或其他目标硬件接收数据。当您将 **Connection mode** 设置为 `Server` 时，必须提供 **Local IP Port**。**Local IP Port** 充当 TCP/IP 服务器的监听端口。当您将 **Connection mode** 设置为 `Client` 时，必须提供要从中接收数据的服务器上的 **Server IP Address** 和 **Server IP Port**。在将包含 TCP Receive 模块的模型部署到目标之前，服务器必须已启动并运行。

该模块以阻塞模式或非阻塞模式接收数据。在阻塞模式下，模型在等待请求的数据可用时阻塞执行。在非阻塞模式下，模型连续运行。要将模块设置为阻塞模式，请选择 **Wait until data received** 选项。

**注意**

确保在 STM32CubeMX 项目中配置 Ethernet 选项。有关详细信息，请参阅 Configure Ethernet Options in STM32CubeMX for STM32 Processor Based Boards。

在阻塞模式下，模型在等待请求的数据可用时阻塞执行。

阻塞模式

在时间步 1，模块请求四个数据值，TCP/IP 接收缓冲区获得四个数据值。执行运行。

在时间步 2，模块再次请求数据，但 TCP/IP 接收缓冲区仅获得三个数据值。执行暂停，直到缓冲区收到第四个数据值或超时值耗尽。然后，执行恢复。

在时间步 3，模块请求数据，缓冲区收到五个数据值。模块返回前四个数据值，剩余数据值用于下一个接收周期。

在非阻塞模式下，模型连续运行。

非阻塞模式

在时间步 1，模块请求数据，缓冲区获得四个数据值。模块将 **Status** 端口值更改为 0，表示新的请求数据可用。此时，**Data** 端口包含新接收到的数据值。模块将 **Data** 端口值重置为 0。

在时间步 2，模块再次请求数据，但缓冲区仅获得三个值。由于数据大小指定为 4，模块无法返回 3 的值。因此，模块将 **Status** 端口值设置为 1，表示没有新数据。**Data** 端口上的所有值变为 0。此时缓冲区有三个数据值。但是，在此阶段，与阻塞模式不同，执行不会停止。

在时间步 3，缓冲区有五个数据值，模块按接收顺序返回前四个数据值，并将 **Status** 端口值更改为 0。剩余数据值用于下一个接收周期。

在每个时间步，**Data** 端口按照您在 **Data size (N)** 参数中指定的大小，将数据作为向量输出。**Status** 端口输出 0 或非零值，指示是否收到新数据。**Status** 端口上的 0 表示收到了有效数据。有关详细信息，请参阅接收数据的输出。

**注意**

在某些情况下，防病毒软件或防火墙可能会阻止 TCP 流量。如果是这样，请配置防病毒软件或防火墙，以允许特定 IP 端口号的流量。
