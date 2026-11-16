---
type: simulink-block
title: 'TCP/IP Send'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / STM32F7'
documentation_page: 'tcpsend'
documentation_source_path: 'nucleo/ref/tcpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# TCP/IP Send

## 端口

### 输入

### **Port\_1** — 输入数据向量

该模块接受指定为 *N*×1 数组的数据。该模块通过 TCP/IP 网络将此数据发送到接收主机。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`
### 输出

### **Status** — 在给定时步传输的请求数据（标量）

在每个时间步，当传输的数据长度大于或等于 **Data size (N)** 参数中指定的长度时，该端口输出 `0`。值 `0` 表示传输的数据在给定的时间步被接收。否则，它输出一个非零值，表示没有传输新数据。

**数据类型：** `uint16`

## 参数

### **Connection mode** — 将模块设置为服务器或客户端 `Server` (默认) | `Client`

将模块设置为 TCP/IP 服务器或客户端。

当您将此参数设置为 `Server` 时，必须提供 **Local IP Port**。本地端口充当 TCP/IP 服务器上的侦听端口。

当您将此参数设置为 `Client` 时，必须提供要向其发送数据的 TCP/IP 服务器上的 **Server IP Address** 和 **Server IP Port**。

### **Server IP Address** — 数据要发送到的服务器的远程 IP 地址 `192.168.1.2` (默认) | 任何有效 IP 地址

指定数据要发送到的接收服务器的远程 IP 地址。

#### 依赖项

仅当您将 **Connection mode** 参数设置为 `Client` 时，此参数才会出现。

### **Server IP Port** — 数据要发送到的服务器上的远程 IP 端口 `25000` (默认) | 1 到 65,535 之间的任何整数

指定数据要发送到的接收服务器上的端口号。

#### 依赖项

仅当您将 **Connection mode** 参数设置为 `Client` 时，此参数才会出现。

### **Local IP Port** — 发送主机上用于发送数据的 IP 端口 `25000` (默认) | 1 到 65,535 之间的任何整数

指定发送数据的应用程序的端口号。此本地端口充当 TCP/IP 服务器的侦听端口。

### **Wait until previous packet transmitted** — 等待上一时间步接收的数据发送完成 `off` (默认) | `on`

- 当您选择此参数时，发送操作以阻塞模式运行。如果上一时间步接收的数据的发送操作已完成，则模块接受来自输入端口的数据。如果发送操作正在进行，则模块等待数据发送完成，然后接受来自输入端口的数据。

  如果下一次发送操作计划开始时，目标硬件仍在等待请求的数据发送完成，则会发生任务超限。要修复超限：

  - 增加输入数据的采样时间。
  - 减小输入端口处数据的长度。
- 当您清除此参数时，发送操作以非阻塞模式运行。如果上一时间步接收的数据的发送操作仍在进行，则给定时间步输入端口的数据将被丢弃。

### **Output error status** — 在数据传输期间显示错误状态的选项 `off` (默认) | `on`

选择此选项可在数据传输期间显示错误状态。

当您选择 Output error status 参数时，模块会配置一个输出端口。模块上的该端口标记为 Status，表示模块在输出端口输出读取操作的状态。

## 所属库

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32F7 Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32H7

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

通过 TCP/IP 网络将数据发送到远程主机

TCP Send 模块通过 TCP/IP 网络将数据发送到远程主机或另一块硬件板。您可以将模块的 **Connection mode** 设置为 `Server` 或 `Client`。当您将 **Connection mode** 设置为 `Client` 时，必须提供要将数据发送到的服务器上的 **Server IP Address** 和 **Server IP Port**。当您将 **Connection mode** 设置为 `Server` 时，必须提供 **Local IP Port**。此 **Local IP Port** 充当 TCP/IP 服务器上的侦听端口。在将包含 TCP Send 模块的模型部署到目标之前，服务器必须已启动并正在运行。

该模块以阻塞模式或非阻塞模式发送数据。在阻塞模式下，模型在等待数据完全发送完成时阻塞执行。在非阻塞模式下，模型连续运行。要将模块设置为阻塞模式，请选择 **Wait until data received** 选项。
