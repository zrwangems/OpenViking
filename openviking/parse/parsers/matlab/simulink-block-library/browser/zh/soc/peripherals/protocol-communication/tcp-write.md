---
type: simulink-block
title: 'TCP Write'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Protocol Communication'
documentation_page: 'tcpwrite'
documentation_source_path: 'ref/tcpwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# TCP Write

## 端口

### 输入

### **data** — 输入数据数值向量

输入数据，指定为数值向量。该模块通过 TCP/IP 网络将此数据发送到远程主机。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **msg** — 发送到远程主机的 TCP/IP 数据包流，标量

此消息端口将 TCP/IP 数据包作为消息发送到连接的 IO Data Sink 模块。有关消息的详细信息，请参阅“消息”。

**注意**

此输出仅在仿真期间使用，在代码生成和外部模式仿真中不起作用。

**数据类型：** `SoCData`

## 参数

### **Network role** — 将模块设置为服务器或客户端 `Client`（默认）| `Server`

要将此模块配置为 TCP/IP 客户端或服务器，请将此参数分别设置为 `Client` 或 `Server`。

当您将此参数设置为 `Client` 时，必须提供要向其发送 TCP/IP 数据包的 TCP/IP 服务器的远程 IP 地址和远程 IP 端口号。请使用 **Remote address** 和 **Remote port** 参数指定此信息。

当您将此参数设置为 `Server` 时，必须提供本地 IP 端口号，该端口号用作硬件中运行的 TCP/IP 服务器的监听端口。请使用 **Local port** 参数指定此信息。

### **Remote address** — 将 TCP/IP 数据包发送到的远程服务器的 IP 地址 `127.0.0.1`（默认）| 点分四段表达式

指定要向其发送 TCP/IP 数据包的远程服务器的 IP 地址。

#### 依赖关系

要启用此参数，请将 **Network role** 参数设置为 `Client`。

### **Remote port** — 将 TCP/IP 数据包发送到的远程服务器的 IP 端口 `25000`（默认）| 1 到 65,535 的整数

指定要向其发送 TCP/IP 数据包的远程服务器的端口号。

#### 依赖关系

要启用此参数，请将 **Network role** 参数设置为 `Client`。

### **Local port** — 发送主机上从其发送 TCP/IP 数据包的 IP 端口 `-1`（默认）| 1 到 65535 的整数

当 **Network role** 参数设置为 `Client` 时，指定要从中发送 TCP/IP 数据包的应用程序的 IP 端口号。默认值 `-1` 会将此 IP 端口号设置为随机可用端口号，并使用该端口发送数据包。

当 **Network role** 参数设置为 `Server` 时，此本地端口用作硬件中运行的 TCP/IP 服务器的监听端口。在这种情况下，请为此参数指定 1 到 65,535 之间的值。

### **Byte order** — 字节序 `LittleEndian`（默认）| `BigEndian`

TCP/IP 数据包的字节序，指定为以下值之一：

- `LittleEndian` — 将 TCP/IP 数据包的字节序设置为小端。
- `BigEndian` — 将 TCP/IP 数据包的字节序设置为大端。

## 所属库

SoC Blockset / Processor I/O

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要为您的设计自动生成 C 代码并在 SoC 设备上执行，请使用 SoC Builder 工具。要为您的 SoC 模型生成并执行 C 代码，需要 Embedded Coder® 功能。有关为 SoC 设计生成代码的详细信息，请参阅使用 SoC Builder 生成 SoC 设计。

Embedded Coder 为此模块生成事件驱动代码。此图显示了生成代码实现的通用表示。

**注意**

在任务实例执行期间，生成代码的时序测量值可能与仿真中任务的时序不同。您可以配置模型以在任务信号中使用数据缓存，从而使仿真与生成代码之间更加一致。有关详细信息，请参阅任务子系统信号的值和缓存。

## 版本历史

**在 R2019a 中引入**

## 描述

通过 TCP/IP 网络向远程主机发送 TCP/IP 数据包

TCP Write 模块通过 TCP/IP（传输控制协议/互联网协议）网络向远程主机发送 TCP/IP 数据包。
