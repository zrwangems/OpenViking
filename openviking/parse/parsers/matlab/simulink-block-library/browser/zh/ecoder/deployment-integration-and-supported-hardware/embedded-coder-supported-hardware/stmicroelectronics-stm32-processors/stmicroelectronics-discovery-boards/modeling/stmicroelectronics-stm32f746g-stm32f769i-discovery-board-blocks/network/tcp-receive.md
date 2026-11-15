---
type: simulink-block
title: 'TCP Receive'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / Network'
documentation_page: 'tcpreceive'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/tcpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# TCP Receive

## 端口

### 输出

### **Data** — 输出数据向量

在每个时间步，该端口按您在 **Data size (N)** 参数中指定的大小输出数据向量。有关详细信息，请参阅接收数据的输出。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Status** — 在给定时间步接收到所请求数据的标量

在每个时间步，当接收到的数据长度大于或等于 **Data size (N)** 参数中指定的长度时，该端口输出 `0`。值 `0` 表示在给定时间步接收到所请求的数据。否则，它输出一个非零值，表示未接收到新数据。

有关详细信息，请参阅接收数据的输出。

**数据类型：** `uint16`

## 参数

### **Connection mode** — 将模块设置为服务器或客户端 `Server`（默认） | `Client`

将模块设置为 TCP/IP 服务器或客户端。

当您将此参数设置为 `Server` 时，必须提供 **Local IP Port**。本地端口充当 TCP/IP 服务器上的侦听端口。

当您将此参数设置为 `Client` 时，必须提供要从其接收数据的 TCP/IP 服务器上的 **Server IP Address** 和 **Server IP Port**。

### **Local IP Port** — 接收主机上用于接收数据的 IP 端口 `25001`（默认） | 1 到 65,535 之间的任意整数

此本地端口号充当 TCP/IP 服务器上的侦听端口。将本地端口号与发送主机的远程端口号匹配。

### **Server IP Address** — 从其接收数据的服务器的远程 IP 地址 `192.168.1.2`（默认） | 任何有效 IP 地址

指定从其接收数据的发送服务器的 IP 地址。

#### 依赖关系

仅当您将 **Connection mode** 参数设置为 `Client` 时，此参数才会出现。

### **Server IP Port** — 从其接收数据的服务器上的远程 IP 端口 `25000`（默认） | 1 到 65,535 之间的任意整数

指定从其接收数据的发送服务器上的端口号。

#### 依赖关系

仅当您将 **Connection mode** 设置为 `Client` 时，此参数才会出现。

### **Data type** — 接收数据的数据类型 `uint8`（默认） | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

指定模块从发送主机接收的数据类型。每个元素的大小取决于其数据类型。

### **Data size (N)** — 接收数据中的数据字节数 `1`（默认） | 任何正整数

指定每个时间步要接收的数据字节数。

### **Wait until data received** — 等待直到请求的数据可用 on（默认） | off

- 当您选中此参数时，读取操作以阻塞模式运行。读取操作在等待所请求的数据可用时被阻塞。如果数据可用，**Data** 端口输出数据。如果数据不可用，**Data** 端口等待数据。

  如果当下一次读取操作计划开始时，目标硬件仍在等待数据可用，则会发生任务超限。

  要修复超限：

  - 使用 **Sample time** 参数增大时间步。
  - 使用 **Data size (N)** 参数减少请求的数据长度。

- 当您清除此参数时，读取操作以非阻塞模式运行。读取数据时，如果数据不可用，**Data** 端口包含上一个时间步接收到的数据。**Status** 端口输出 `0`。在此模式下，模块不会等待所请求的数据可用。

### **Sample time** — 模块从发送主机读取数据的时间间隔 `-1`（默认） | 非负值

当您将此参数设置为 `-1` 时，Simulink® 根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2017a 中引入**

## 描述

通过 TCP/IP 网络从远程主机接收数据

TCP Receive 模块通过网络从远程主机或其他目标硬件接收数据。当您将 **Connection mode** 设置为 `Server` 时，必须提供 **Local IP Port**。**Local IP Port** 充当 TCP/IP 服务器的侦听端口。当您将 **Connection mode** 设置为 `Client` 时，必须提供要从其接收数据的服务器上的 **Server IP Address** 和 **Server IP Port**。在将包含 TCP Receive 模块的模型部署到目标之前，服务器必须已启动并正在运行。

该模块可在阻塞模式或非阻塞模式下接收数据。在阻塞模式下，模型在等待所请求的数据可用时阻塞执行。在非阻塞模式下，模型连续运行。要将模块设置为阻塞模式，请选中 **Wait until data received** 选项。

在阻塞模式下，模型在等待所请求的数据可用时阻塞执行。

阻塞模式

在时间步 1，模块请求四个数据值，TCP/IP 接收缓冲区获得四个数据值。执行运行。

在时间步 2，模块再次请求数据，但 TCP/IP 接收缓冲区仅获得三个数据值。执行暂停，直到缓冲区接收到第四个数据值或超时值过去。然后，执行恢复。

在时间步 3，模块请求数据，缓冲区接收到五个数据值。模块返回前四个数据值，剩余的数据值用于下一个接收周期。

在非阻塞模式下，模型连续运行。

非阻塞模式

在时间步 1，模块请求数据，缓冲区获得四个数据值。模块将 **Status** 端口值更改为 0，表示新的请求数据可用。此时，**Data** 端口包含新接收到的数据值。模块将 **Data** 端口值重置为 0。

在时间步 2，模块再次请求数据，但缓冲区仅获得三个值。由于数据大小指定为 4，模块无法返回值为 3。因此，模块将 **Status** 端口值设置为 1，表示没有新数据。**Data** 端口上的所有值变为 0。此时，缓冲区有三个数据值。然而，在此阶段，与阻塞模式不同，执行不会停止。

在时间步 3，缓冲区有五个数据值，模块按接收顺序返回前四个数据值，并将 **Status** 端口值更改为 0。剩余的数据值用于下一个接收周期。

在每个时间步，**Data** 端口按您在 **Data size (N)** 参数中指定的大小输出数据向量。**Status** 端口输出 `0` 或非零值，指示是否接收到新数据。**Status** 端口上的 `0` 表示接收到有效数据。有关详细信息，请参阅接收数据的输出。

**注意**

- 在某些情况下，防病毒软件或防火墙可能会阻止 TCP 流量。如果这样，请将防病毒软件或防火墙配置为允许特定 IP 端口号的流量。
- 当在模型中启用 DHCP 并包含 TCP/IP 或 UDP 模块时，代码会在无限循环中等待，直到为开发板分配 IP。因此，如果用户的模型中启用了 DHCP 并包含任何 UDP/TCP 模块，用户必须确保开发板已连接到路由器。
