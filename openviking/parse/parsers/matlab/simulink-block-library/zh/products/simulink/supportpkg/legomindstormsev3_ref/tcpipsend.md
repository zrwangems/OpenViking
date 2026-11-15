---
type: simulink-block
title: 'TCP/IP Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Communication Protocol Blocks'
documentation_page: 'tcpipsend'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/tcpipsend.html'
language: zh-CN
chinese_source: official
---

# TCP/IP Send

## 端口

### 输入

### **Port1** — 接受数据的输入端口 [N×1] 数组

该模块接受 [N×1] 数组形式的数据。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

#### “常设”选项卡

### **连接模式** — 将模块设置为客户端或服务器的选项 **客户端** (默认) | **服务器**

选择此选项可将模块设置为 TCP/IP 客户端或 TCP/IP 服务器。

### **本地 IP 端口** — 充当服务器侦听端口的本地端口 25000 (默认) | 标量

输入充当 TCP/IP 服务器侦听端口的本地端口号。仅当您将**连接模式**设置为**服务器**时，此参数才会出现。

### **远程 IP 地址** — 向其发送数据的服务器的远程地址 127.0.0.1 (默认) | 标量

输入要将数据发送到的远程服务器地址。仅当您将**连接模式**设置为**客户端**时，此参数才会显示。

### **远程 IP 端口** — 向其发送数据的服务器的远程端口 25000 (默认) | 标量

输入远程服务器端口。仅当您将**连接模式**设置为**客户端**时，此参数才会显示。

#### “高级”选项卡

### **手动指定本地 IP 端口** — 手动指定本地 IP 端口号 off (默认) | on

允许手动指定发送数据的本地 IP 端口。仅当您将**连接模式**设置为**客户端**时，此参数才会显示。

### **本地 IP 端口** — 发送数据的本地端口 25000 (默认) | 标量

输入客户端发送数据的本地端口。仅当您将**连接模式**设置为**客户端**并选中复选框**手动指定本地 IP 端口**时，此参数才会显示。

### **等待上一个数据包传输完毕** — 为等待数据发送的模块设置的选项 off (默认) | on

选择此选项可指定模块等待当前数据发送。选中此复选框将启用“阻塞模式”。

### **超时(秒)** — 等待数据发送的时间 0.1 (默认) | 标量

指定在每个仿真时间步期间模块等待发送数据的时间。如果您未选择**等待上一个数据包传输完毕**参数，则此字段不可用。如果希望模块无限期等待，直到发送数据，请在此参数中输入 `inf` 值。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Communication Simulink Support Package for Android Devices / Communication Simulink Support Package for LEGO MINDSTORMS EV3 Hardware Simulink Support Package for Raspberry Pi Hardware / Network

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

R2025b 官方文档未提供。

## 描述

通过 TCP/IP 网络将数据发送到另一个远程主机

通过网络向远程主机/另一个硬件板发送数据。您可以将模块的连接模式设置为服务器或客户端。将连接模式设置为 TCP/IP 客户端时，您必须提供要向其发送数据的 TCP/IP 服务器的远程地址和远程 IP 端口。将模块设置为 TCP/IP 服务器时，您必须提供 TCP/IP 服务器的本地 IP 端口。此 IP 端口充当 TCP/IP 服务器的侦听端口。
