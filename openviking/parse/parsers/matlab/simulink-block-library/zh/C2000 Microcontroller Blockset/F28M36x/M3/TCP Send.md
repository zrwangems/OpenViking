---
type: simulink-block
title: 'TCP Send'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F28M36x / M3'
documentation_page: 'tcpsend'
documentation_source_path: '../rtw/freescalefrdmk64fboard/ref/tcpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# TCP Send

## 端口

### 输入

### **Port\_1** — 输入数据向量

该模块接受指定为 *N*×1 数组的数据。该模块通过 TCP/IP 网络将此数据发送到接收主机。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

## 参数

### **Connection mode** — 将模块设置为服务器或客户端 `Server`（默认）| `Client`

将模块设置为 TCP/IP 服务器或客户端。

当您将此参数设置为 `Server` 时，必须提供 **Local IP Port**。本地端口充当 TCP/IP 服务器的监听端口。

当您将此参数设置为 `Client` 时，必须提供要向其发送数据的 TCP/IP 服务器的 **Remote IP Address** 和 **Remote IP Port**。

### **Remote IP Address** — 数据发送到的服务器的远程 IP 地址 `192.168.1.2`（默认）| 任何有效的 IP 地址

指定数据发送到的服务器的远程 IP 地址。

#### 依赖关系

此参数仅在您将 **Connection mode** 参数设置为 `Client` 时显示。

### **Remote IP Port** — 数据发送到的服务器的远程 IP 端口 `25000`（默认）| [1 到 65,535]

指定数据发送到的服务器的端口号。

#### 依赖关系

此参数仅在您将 **Connection mode** 参数设置为 `Client` 时显示。

### **Local IP Port** — 发送主机的 IP 端口，数据从该端口发送 `25001`（默认）| [1 到 65,535]

指定发送数据的应用程序的端口号。此本地端口充当发送主机的监听端口。

## 所属库

Simulink Coder Support Package for NXP FRDM-K64F Board

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017b 中引入**

## 描述

通过 TCP/IP 网络向远程主机发送数据

TCP Send 模块通过有线网络向远程主机或另一块硬件板发送数据。您可以将模块的 **Connection mode** 设置为 `Server` 或 `Client`。当您将 **Connection mode** 设置为 `Client` 时，必须提供要向其发送数据的服务器的 **Remote IP Address** 和 **Remote IP Port**。当您将 **Connection mode** 设置为 `Server` 时，必须提供 **Local IP Port**。此 **Local IP Port** 充当 TCP/IP 服务器的监听端口。
