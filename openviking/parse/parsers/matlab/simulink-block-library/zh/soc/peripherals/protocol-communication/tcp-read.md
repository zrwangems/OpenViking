---
type: simulink-block
title: 'TCP Read'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Protocol Communication'
documentation_page: 'tcpread'
documentation_source_path: 'ref/tcpread.html'
language: zh-CN
chinese_source: worker-translation
---

# TCP Read

## 端口

### 输入

### **msg** — 从远程主机接收的 TCP/IP 数据包流 标量

此消息端口从连接的 IO Data Source 模块接收 TCP/IP 数据包（作为消息）。当 Task Manager 模块触发包含 TCP Read 模块的任务时，会处理这些消息。有关消息的详细信息，请参阅 Messages。

**注意**

此输入仅在仿真期间使用，在代码生成和外部模式仿真中不起作用。

**数据类型：** `SoCData`
### 输出

### **data** — 从远程主机接收的 TCP/IP 数据包 数值向量

输出从远程主机接收的 TCP/IP 数据包，以数值向量形式返回。此输出的大小和数据类型与输入消息的大小和数据类型相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **length** — 输出 TCP/IP 数据包的长度 非负标量

在输出 **data** 端口上返回的输出 TCP/IP 数据包的长度。

**数据类型：** `uint32`

## 参数

### **网络角色** — 将模块设置为客户端或服务器 `Client` (默认) | `Server`

要将此模块配置为 TCP/IP 客户端或服务器，请将此参数分别设置为 `Client` 或 `Server`。

当将此参数设置为 `Client` 时，必须提供要从中接收 TCP/IP 数据包的 TCP/IP 服务器的远程 IP 地址和远程 IP 端口号。请使用 **远程地址** 和 **远程端口** 参数指定此信息。

当将此参数设置为 `Server` 时，必须提供本地 IP 端口号，它充当硬件中运行的 TCP/IP 服务器的侦听端口。请使用 **本地端口** 参数指定此信息。当将此参数设置为 `Server` 时，一次只能连接一个客户端。

### **远程地址** — 从中接收 TCP/IP 数据包的远程服务器的 IP 地址 `127.0.0.1` (默认) | 点分四段表达式

指定要从中接收 TCP/IP 数据包的远程服务器的 IP 地址。

#### 依赖项

要启用此参数，请将 **网络角色** 参数设置为 `Client`。

### **远程端口** — 从中接收 TCP/IP 数据包的远程服务器上的 IP 端口 `25000` (默认) | 1 到 65535 的整数

指定要从中接收 TCP/IP 数据包的远程服务器的端口号。

#### 依赖项

要启用此参数，请将 **网络角色** 参数设置为 `Client`。

### **本地端口** — 接收数据的主机的 IP 端口 `-1` (默认) | 1 到 65,535 的整数

当 **网络角色** 设置为 `Client` 时，指定要接收 TCP/IP 数据包的应用程序的端口号。当将 **网络角色** 参数设置为 `Client` 时，默认值 `-1` 会将任意可用的随机端口分配为本地端口。

当 **网络角色** 设置为 `Server` 时，此本地端口充当 TCP/IP 服务器上的侦听端口。当将 **网络角色** 参数设置为 `Server` 时，请指定 1 到 65535 之间的值。请将此本地端口号指定为要从中接收 TCP/IP 数据包的发送主机中的远程端口号。

### **数据类型** — 接收的 TCP/IP 数据包的数据类型 `uint8` (默认) | `single` | `double` | `int8` | `int16` | `int32` | `uint16` | `uint32`

选择输入数据的数据类型。将此数据类型与从远程主机发送的 TCP/IP 数据包的数据类型匹配。

### **最大数据长度（元素）** — 输出 TCP/IP 数据包的最大长度 `1` (默认) | 正标量

指定输出 **data** 端口在每个时间步可以生成的最大数据元素数。

### **启用基于事件的执行** — 启用基于事件的任务执行 off (默认) | on

要生成事件驱动代码，请选中此参数。要生成定时器驱动代码，请清除此参数。

选中 **启用基于事件的执行** 时，只要套接字缓冲区中接收到任何 TCP/IP 数据包，该模块就会从套接字缓冲区读取 TCP/IP 数据包，而不考虑采样时间。清除 **启用基于事件的执行** 时，该模块会在每个采样时间从套接字缓冲区读取可用的 TCP/IP 数据包。要设置该模块可从套接字缓冲区读取的 TCP/IP 数据包大小，请在 **接收缓冲区大小** 参数中指定大小。

### **采样时间** — 采样时间 `-1` (默认) | 非负标量

指定调度器运行此模块的频率。如果此值为 `-1` (默认)，则调度器会为该模块分配采样时间。

## 所属库

SoC Blockset / Processor I/O

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要自动为您的设计生成 C 代码并在 SoC 设备上执行，请使用 SoC Builder 工具。要为 SoC 模型生成并执行 C 代码，需要 Embedded Coder® 功能。有关为 SoC 设计生成代码的详细信息，请参阅 Use SoC Builder to Generate SoC Design。

Embedded Coder 基于 **启用基于事件的执行** 参数选择为此模块生成事件驱动或定时器驱动代码。此图显示了所生成代码实现的通用表示。

**注意**

在任务实例执行期间，来自生成代码的时序测量值可能与仿真中任务的时序不同。您可以配置模型以在任务信号中使用数据缓存，从而提高仿真与生成代码之间的一致性。有关详细信息，请参阅 Value and Caching of Task Subsystem Signals。

## 版本历史

**在 R2019a 中引入**

## 描述

通过 TCP/IP 网络从远程主机接收 TCP/IP 数据包

TCP Read 模块通过 TCP/IP（传输控制协议/网际协议）网络从远程主机接收 TCP/IP 数据包流。
