---
type: simulink-block
title: 'TCP Send'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Network'
documentation_page: 'tcpsendblock'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/tcpsendblock.html'
language: zh-CN
chinese_source: worker-translation
---

# TCP Send

## 端口

### 输入

### **data** — 输入数据向量

该模块接受指定为 *N*×1 数组的数据。该模块通过 TCP/IP 网络将此数据发送到接收主机。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### 输出

### **Status** — 在给定时步传输的请求数据（标量）

在每个时步，当传输的数据长度大于或等于 **Data size (N)** 参数中指定的长度时，该端口输出 `0`。值 `0` 表示在给定时步接收到了所传输的数据。否则，它输出非零值，表示未传输新数据。

#### 依赖项

要启用此端口，请选择 **Output error status** 参数。

**数据类型：** `uint16`

## 参数

### **Connection mode** — 将模块设置为服务器或客户端 `Server`（默认） | `Client`

将该模块设置为 TCP/IP 服务器或客户端。

将此参数设置为 `Server` 时，必须提供 **Local IP Port**。本地端口充当 TCP/IP 服务器上的侦听端口。

将此参数设置为 `Client` 时，必须提供要向其发送数据的 TCP/IP 服务器上的 **Server IP Address** 和 **Server IP Port**。

### **Server IP Address** — 数据要发送到的服务器的远程 IP 地址 `192.168.1.2`（默认） | 任何有效的 IP 地址

指定数据要发送到的接收服务器的远程 IP 地址。

#### 依赖项

要启用此参数，请将 **Connection mode** 参数设置为 `Client`。

### **Server IP Port** — 数据要发送到的服务器上的远程 IP 端口 `25000`（默认） | 从 1 到 65,535 的任何整数

指定数据要发送到的接收服务器上的端口号。

#### 依赖项

要启用此参数，请将 **Connection mode** 参数设置为 `Client`。

### **Local IP Port** — 发送主机上用于发送数据的 IP 端口 `25000`（默认） | 从 1 到 65,535 的任何整数

指定用于发送数据的应用程序的端口号。此本地端口充当 TCP/IP 服务器的侦听端口。

### **Wait until previous packet transmitted** — 等待上一时步接收到的数据发送完成 `off`（默认） | `on`

- 选择此参数时，发送操作以阻塞模式运行。如果上一时步接收到的数据的发送操作已完成，则该模块接受来自输入端口的数据。如果发送操作正在进行，则该模块会等待数据发送完成，然后接受来自输入端口的数据。

  如果当下一发送操作计划开始时，目标硬件仍在等待所请求的数据发送完成，则会发生任务溢出。要修复溢出：

  - 增加输入数据的采样时间。
  - 减少输入端口处的数据长度。
- 清除此参数时，发送操作以非阻塞模式运行。如果上一时步接收到的数据的发送操作仍在进行，则给定时步输入端口处的数据将被丢弃。

### **Output error status** — 在数据传输期间显示错误状态的选项 `off`（默认） | `on`

选择此选项可在数据传输期间显示错误状态。

当选择 Output error status 参数时，该模块会配置一个输出端口。模块上的该端口标记为 Status，表示该模块在输出端口输出读取操作的状态。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2022b 中引入**

## 描述

通过 TCP/IP 网络向远程主机发送数据

TCP Send 模块通过 TCP/IP 网络将数据发送到远程主机或另一个硬件板。可以将该模块的 **Connection mode** 设置为 `Server` 或 `Client`。当将 **Connection mode** 设置为 `Client` 时，必须提供要向其发送数据的服务器上的 **Server IP Address** 和 **Server IP Port**。当将 **Connection mode** 设置为 `Server` 时，必须提供 **Local IP Port**。此 **Local IP Port** 用作 TCP/IP 服务器上的侦听端口。在将包含 TCP Send 模块的模型部署到目标之前，服务器必须已启动并运行。

该模块以阻塞模式或非阻塞模式发送数据。在阻塞模式下，模型在等待数据完全发送期间会阻塞执行。在非阻塞模式下，模型连续运行。要将该模块设置为阻塞模式，请选择 **Wait until data received** 选项。

**注意**

确保在 STM32CubeMX 工程中配置以太网选项。有关详细信息，请参阅 Configure Ethernet Options in STM32CubeMX for STM32 Processor Based Boards。
