---
type: simulink-block
title: 'TCP/IP Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'tcpipsend'
documentation_source_path: 'supportpkg/android_ref/tcpipsend.html'
language: zh-CN
chinese_source: worker-translation
---

# TCP/IP Send

## 端口

### 输入

### **Port1** — 用于接受 [Nx1] 数组数据的输入端口

该模块接受 [Nx1] 数组形式的数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

#### 主选项卡

### **Connection mode** — 用于将模块设置为客户端或服务器的选项 `Client`（默认） | `Server`

选择此选项可将模块设置为 TCP/IP 客户端或 TCP/IP 服务器。

### **Local IP port** — 用作服务器监听端口的本地端口 25000（默认） | scalar

输入本地端口号，该端口号用作 TCP/IP 服务器的监听端口。仅当将 **Connection mode** 设置为 `Server` 时，此参数才会显示。

### **Remote IP address** — 要将数据发送到的服务器的远程地址 127.0.0.1（默认） | scalar

输入要将数据发送到的远程服务器地址。仅当将 **Connection mode** 设置为 `Client` 时，此参数才会显示。

### **Remote IP port** — 要将数据发送到的服务器的远程端口 25000（默认） | scalar

输入远程服务器端口。仅当将 **Connection mode** 设置为 `Client` 时，此参数才会显示。

#### 高级选项卡

### **Manually specify local IP port** — 手动指定本地 IP 端口号 off（默认） | on

允许手动指定发送数据所用的本地 IP 端口。仅当将 **Connection mode** 设置为 `Client` 时，此参数才会显示。

### **Local IP port** — 发送数据所用的本地端口 25000（默认） | scalar

输入客户端发送数据所用的本地端口。仅当将 **Connection mode** 设置为 `Client` 并选中 **Manually specify local IP port** 复选框时，此参数才会显示。

### **Wait until previous packet transmitted** — 用于设置模块等待数据发送完成的选项 off（默认） | on

选择此选项可指定模块等待当前数据发送完成。选中此复选框将启用“阻塞模式”。

### **Timeout in seconds** — 等待数据发送完成的时间 0.1（默认） | scalar

指定模块在每个仿真时间步中等待数据发送完成的时间。如果未选择 **Wait until previous packet transmitted** 参数，则此字段不可用。如果希望模块无限期等待直到发送数据，请在此参数中输入 `inf` 值。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Communication Simulink Support Package for Android Devices / Communication Simulink Support Package for LEGO MINDSTORMS EV3 Hardware Simulink Support Package for Raspberry Pi Hardware / Network

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

## 描述

通过 TCP/IP 网络将数据发送到另一个远程主机

通过网络将数据发送到远程主机/另一个硬件板。您可以将模块的连接模式设置为服务器或客户端。当将连接模式设置为 TCP/IP 客户端时，必须提供要将数据发送到的 TCP/IP 服务器的远程地址和远程 IP 端口。当将模块设置为 TCP/IP 服务器时，必须提供 TCP/IP 服务器的本地 IP 端口。此 IP 端口用作 TCP/IP 服务器的监听端口。
