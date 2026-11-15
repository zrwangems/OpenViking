---
type: simulink-block
title: 'TCP/IP Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Parrot Minidrones / Modeling'
documentation_page: 'tcpipsend'
documentation_source_path: 'supportpkg/parrot_ref/tcpipsend.html'
language: zh-CN
chinese_source: worker-translation
---

# TCP/IP Send

## 端口

### 输入

### **Port1** — 接受数据 [Nx1] 数组的输入端口

该模块接受指定为 *N*×1 数组的数据。该模块通过 TCP/IP 网络将此数据发送到接收主机。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

## 参数

#### 主选项卡

### **Connection mode** — 将模块设置为服务器或客户端 `Server` (default) | `Client`

将模块设置为 TCP/IP 服务器或客户端。

当您将该参数设置为 `Server` 时，必须提供 **Local IP port**。该本地端口用作 TCP/IP 服务器的监听端口。

当您将该参数设置为 `Client` 时，必须提供要将数据发送到的 TCP/IP 服务器的 **Remote IP port**。

### **Local IP port** — 用作服务器监听端口的本地端口 `25000` (default) | [1, 65535]

输入用作 TCP/IP 服务器监听端口的本地端口号。

#### 依赖关系

仅当您将 **Connection mode** 参数设置为 `Server` 时，此参数才显示。

### **Remote IP Address** — 要将数据发送到的服务器的远程 IP 地址 `192.168.3.2` (default)

数据发送到的服务器的远程 IP 地址。**Remote IP address** 设置为 192.168.3.2；请勿更改此 IP 地址。

#### 依赖关系

仅当您将 **Connection mode** 参数设置为 `Client` 时，此参数才显示。

### **Remote IP port** — 要将数据发送到的服务器的远程 IP 端口 `25000` (default) | [1, 65535]

指定要将数据发送到的服务器的端口号。

**注意**

请勿将端口 `24099` 和 `26061` 用于与 Parrot minidrone 进行 TCP/IP 通信，因为这些端口是保留的。

#### 依赖关系

仅当您将 **Connection mode** 参数设置为 `Client` 时，此参数才显示。

#### 高级选项卡

### **Manually specify local IP port** — 手动指定本地 IP 端口的编号 off (default) | logical

允许手动指定发送数据所使用的本地 IP 端口。仅当您将 **Connection mode** 设置为 `Client` 时，此参数才显示。

### **Local IP port** — 发送数据所使用的本地端口 25000 (default) | scalar

输入用于发送数据的客户端本地端口。仅当您将 **Connection mode** 设置为 `Client` 并选中复选框 **Manually specify local IP port** 时，此参数才显示。

## 所属库

Simulink Support Package for Parrot Minidrones

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

通过 TCP/IP 网络向远程主机发送数据

TCP/IP Send 模块通过 Bluetooth® 网络将数据发送到远程主机。您可以将该模块的 **Connection mode** 设置为 `Server` 或 `Client`。当您将 **Connection mode** 设置为 `Client` 时，必须提供要将数据发送到的服务器的 **Remote IP port**。当您将 **Connection mode** 设置为 `Server` 时，必须提供 **Local IP port**。此 **Local IP port** 充当 TCP/IP 服务器的监听端口。
