---
type: simulink-block
title: 'TCP/IP Receive'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Communication'
documentation_page: 'tcpipreceive'
documentation_source_path: 'beagleboneblue/ref/tcpipreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# TCP/IP Receive

## 端口

### 输出

### **Data** — 用于发出所接收数据的输出端口 [Nx1] 数组

该模块以 [Nx1] 数组形式输出数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Status** — 用于发出所接收数据状态的输出端口 1 | 0

此端口显示数据接收状态。状态值 1 表示成功接收数据。

**数据类型：** `int8`

## 参数

#### 主选项卡

### **Connection mode** — 用于将模块设置为服务器或客户端的选项 `Server`（默认）| `Client`

选择该选项以将模块连接为 TCP/IP 服务器或 TCP/IP 客户端。

### **Local IP port** — 充当服务器侦听端口的本地端口 25000（默认）| 标量

输入本地端口号，该端口号充当 TCP/IP 服务器的侦听端口。仅当将 **Connection mode** 设置为 `Server` 时，此参数才会显示。

### **Remote IP address** — 要从中接收数据的服务器的远程地址 127.0.0.1（默认）| 标量

输入要从中接收数据的远程服务器地址。仅当将 **Connection mode** 设置为 `Client` 时，此参数才会显示。

### **Remote IP port** — 要从中接收数据的服务器的远程端口 25000（默认）| 标量

输入远程服务器端口。仅当将 **Connection mode** 设置为 `Client` 时，此参数才会显示。

### **Data type** — 要接收的数据类型 uint8（默认）| double | single | int8 | uint16 | int16 | uint32 | int32 | boolean

选择要从远程主机接收的数据类型。

### **Data size(N)** — 要接收的数据大小 1（默认）| 标量

输入要从远程主机接收的数据大小。

### **Sample time** — 接收数据的时间频率 0.1（默认）| 标量

输入接收数据的时间频率。

#### 高级选项卡

### **Manually specify local IP port** — 手动指定本地 IP 端口号 off（默认）| on

允许手动指定接收数据所用的本地 IP 端口。仅当将 **Connection mode** 设置为 `Client` 时，此参数才会显示。

### **Local IP port** — 接收数据所用的本地端口 25000（默认）| 标量

输入用于接收数据的客户端本地端口。仅当将 **Connection mode** 设置为 `Client` 并选中 **Manually specify local IP port** 复选框时，此参数才会显示。

### **Wait until data received** — 用于设置模块等待接收数据的选项 off（默认）| on

选择此选项以指定模块是否等待接收数据。选中此复选框会启用阻塞模式。

### **Timeout in seconds** — 等待直到接收到数据的时间 0.1（默认）| 标量

指定模块在每个仿真时间步内等待接收数据的时间。如果未选择 **Wait until data received** 参数，则此字段不可用。如果希望模块无限期等待，直到接收到数据，请在此参数中输入 ‘inf’ 值。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Communication Simulink Support Package for Android Devices / Communication Simulink Support Package for LEGO MINDSTORMS EV3 Hardware Simulink Support Package for Raspberry Pi Hardware / Network

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

未在 R2025b 中记录。

## 描述

通过 TCP/IP 网络从远程主机接收数据

从远程主机/另一目标硬件通过网络接收数据。当将连接模式设置为服务器时，必须提供本地端口。本地端口充当 TCP/IP 服务器的侦听端口。当将模块设置为客户端时，必须提供 TCP/IP 服务器的远程地址和远程端口以接收数据。该模块以阻塞模式或非阻塞模式接受数据。在每个时间步，**Data** 端口输出包含所请求的数据。**Status** 端口包含 0 或 1，用于指示指定时间步的新数据是否已接收。Status 端口值 1 表示来自 **Data** 端口的数据有效。

在阻塞模式下，模型在等待所请求的数据可用时会阻塞执行。

阻塞模式

在时间步 1，模块请求四个数据值，TCP/IP 接收缓冲区获得四个数据值。执行继续运行。

在时间步 2，模块再次请求数据，但 TCP/IP 接收缓冲区只获得三个数据值。执行暂停，直到缓冲区接收到第四个数据值或超时值流逝。然后，执行恢复。

在时间步 3，模块请求数据，缓冲区接收到五个数据值。模块返回前四个数据值，剩余的数据值用于下一个接收周期。

在非阻塞模式下，模型连续运行。

非阻塞模式

在时间步 1，模块请求数据，缓冲区获得四个数据值。模块将 **Status** 端口值更改为 0，指示所请求的新数据可用。此时，**Data** 端口包含新接收的数据值。模块将 **Data** 端口值重置为 0。

在时间步 2，模块再次请求数据，但缓冲区只获得三个值。模块无法返回 3 个值，因为数据大小指定为 4。因此，模块将 **Status** 端口值设置为 1，指示没有新数据。**Data** 端口上的所有值变为 0。此时，缓冲区有三个数据值。但是，在此阶段，与阻塞模式不同，执行不会停止。

在时间步 3，缓冲区有五个数据值，模块按接收顺序返回前四个数据值，并将 **Status** 端口值更改为 0。剩余的数据值用于下一个接收周期。
