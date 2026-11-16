---
type: simulink-block
title: 'TCP/IP Send'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Communication'
documentation_page: 'tcpipsend'
documentation_source_path: 'beagleboneblue/ref/tcpipsend.html'
language: zh-CN
chinese_source: worker-translation
---

# TCP/IP Send

## 端口

### 输入

### **Port1** — 接受数据 [Nx1] 数组的输入端口

该模块接受 [Nx1] 数组形式的数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

#### 主选项卡

### **连接模式** — 将模块设置为客户端或服务器的选项 `Client`（默认） | `Server`

选择此选项可将模块设置为 TCP/IP 客户端或 TCP/IP 服务器。

### **本地 IP 端口** — 用作服务器监听端口的本地端口 25000（默认） | 标量

输入用作 TCP/IP 服务器监听端口的本地端口号。仅当您将 **连接模式** 设置为 `Server` 时，此参数才会显示。

### **远程 IP 地址** — 要将数据发送到的服务器的远程地址 127.0.0.1（默认） | 标量

输入要将数据发送到的远程服务器地址。仅当您将 **连接模式** 设置为 `Client` 时，此参数才会显示。

### **远程 IP 端口** — 要将数据发送到的服务器的远程端口 25000（默认） | 标量

输入远程服务器端口。仅当您将 **连接模式** 设置为 `Client` 时，此参数才会显示。

#### 高级选项卡

### **手动指定本地 IP 端口** — 手动指定本地 IP 端口的编号 off（默认） | on

允许手动指定从中发送数据的本地 IP 端口。仅当您将 **连接模式** 设置为 `Client` 时，此参数才会显示。

### **本地 IP 端口** — 用于发送数据的本地端口 25000（默认） | 标量

输入客户端用于发送数据的本地端口。仅当您将 **连接模式** 设置为 `Client` 并选中 **手动指定本地 IP 端口** 复选框时，此参数才会显示。

### **等待上一个数据包传输完成** — 用于设置模块等待数据发送的选项 off（默认） | on

选择此选项可指定模块等待当前数据发送完成。选中此复选框会启用“阻塞模式”。

### **超时时间（seconds）** — 等待数据发送的时间 0.1（默认） | 标量

指定模块在每个仿真时间步中等待数据发送的时间。如果您未选择 **等待上一个数据包传输完成** 参数，则此字段不可用。如果您希望模块无限期等待，直到发送数据，请在此参数中输入 `inf` 值。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Communication Simulink Support Package for Android Devices / Communication Simulink Support Package for LEGO MINDSTORMS EV3 Hardware Simulink Support Package for Raspberry Pi Hardware / Network

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

通过 TCP/IP 网络将数据发送到另一远程主机

通过网络将数据发送到远程主机/另一硬件板。您可以将模块的连接模式设置为服务器或客户端。当您将连接模式设置为 TCP/IP 客户端时，必须提供要将数据发送到的 TCP/IP 服务器的远程地址和远程 IP 端口。当您将模块设置为 TCP/IP 服务器时，必须提供 TCP/IP 服务器的本地 IP 端口。此 IP 端口用作 TCP/IP 服务器的监听端口。
