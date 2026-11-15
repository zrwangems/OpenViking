---
type: simulink-block
title: 'TCP Send'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / Network'
documentation_page: 'tcpsend'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/tcpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# TCP Send

## 端口

### 输入

### **Port\_1** — 输入数据向量

该模块接受指定为 *N*×1 数组的数据。模块通过 TCP/IP 网络将此数据发送到接收主机。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

## 参数

### **Connection mode** — 将模块设置为服务器或客户端 `Server`（默认） | `Client`

将模块设置为 TCP/IP 服务器或客户端。

当您将此参数设置为 `Server` 时，必须提供 **Local IP Port**。本地端口充当 TCP/IP 服务器上的侦听端口。

当您将此参数设置为 `Client` 时，必须提供要将数据发送到的 TCP/IP 服务器上的 **Server IP Address** 和 **Server IP Port**。

### **Server IP Address** — 数据发送到的服务器的远程 IP 地址 `192.168.1.2`（默认） | 任何有效 IP 地址

指定数据发送到的接收服务器的远程 IP 地址。

#### 依赖关系

此参数仅在将 **Connection mode** 参数设置为 `Client` 时显示。

### **Server IP Port** — 数据发送到的服务器上的远程 IP 端口 `25000`（默认） | 1 到 65,535 之间的任何整数

指定数据发送到的接收服务器上的端口号。

#### 依赖关系

此参数仅在将 **Connection mode** 参数设置为 `Client` 时显示。

### **Local IP Port** — 发送主机上用于发送数据的 IP 端口 `25000`（默认） | 1 到 65,535 之间的任何整数

指定应用程序从中发送数据的端口号。此本地端口充当 TCP/IP 服务器的侦听端口。

### **Wait until previous packet transmitted** — 等待直到上一个时间步接收的数据已发送 `on`（默认） | `off`

- 当您选择此参数时，发送操作以阻塞模式运行。如果上一个时间步接收的数据的发送操作已完成，则模块接受来自输入端口的数据。如果发送操作正在进行，则模块等待数据发送完成，然后接受来自输入端口的数据。

  如果当计划开始下一次发送操作时，目标硬件仍在等待所请求的数据被发送，则发生任务超限。要修复超限：

  - 增加输入数据的采样时间。
  - 减少输入端口处的数据长度。
- 当您清除此参数时，发送操作以非阻塞模式运行。如果上一个时间步接收的数据的发送操作仍在进行，则给定时间步输入端口处的数据将被丢弃。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2017a 中引入**

## 描述

通过 TCP/IP 网络将数据发送到远程主机

TCP Send 模块通过 TCP/IP 网络将数据发送到远程主机或另一硬件板。您可以将模块的 **Connection mode** 设置为 `Server` 或 `Client`。当您将 **Connection mode** 设置为 `Client` 时，必须提供要将数据发送到的服务器上的 **Server IP Address** 和 **Server IP Port**。当您将 **Connection mode** 设置为 `Server` 时，必须提供 **Local IP Port**。此 **Local IP Port** 充当 TCP/IP 服务器上的侦听端口。在将包含 TCP Send 模块的模型部署到目标之前，服务器必须已启动并运行。

该模块以阻塞模式或非阻塞模式发送数据。在阻塞模式下，模型在等待数据完全发送时阻塞执行。在非阻塞模式下，模型连续运行。要将模块设置为阻塞模式，请选择 **Wait until data received** 选项。

**注意**

当模型中启用 DHCP 并包含 TCP/IP 或 UDP 模块时，代码将无限循环等待，直到为板分配 IP。因此，如果用户的模型中包含任何启用了 DHCP 的 UDP/TCP 模块，则用户必须确保板已连接到路由器。
