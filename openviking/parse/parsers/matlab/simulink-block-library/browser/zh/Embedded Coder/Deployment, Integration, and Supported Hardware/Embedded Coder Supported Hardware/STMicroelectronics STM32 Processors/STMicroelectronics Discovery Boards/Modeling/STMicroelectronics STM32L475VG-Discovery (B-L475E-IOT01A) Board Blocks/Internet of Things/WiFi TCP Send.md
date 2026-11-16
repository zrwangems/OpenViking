---
type: simulink-block
title: 'WiFi TCP Send'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32L475VG-Discovery (B-L475E-IOT01A) Board Blocks / Internet of Things'
documentation_page: 'wifitcpsend'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/wifitcpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# WiFi TCP Send

## 端口

### Input

### **Input** — 输入数据向量

该模块接受数据作为 *N*-by-1 数组。该模块通过 TCP/IP 网络将此数据发送到接收主机。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **连接模式** — 将模块设置为服务器或客户端 `Server` (默认) | `Client`

将模块设置为 TCP/IP 服务器或客户端。

当您将此参数设置为 `Server` 时，必须指定 **本地 IP 端口**。本地端口充当 TCP/IP 服务器上的侦听端口。

当您将此参数设置为 `Client` 时，必须指定 **远程 IP 地址** 以及要将数据发送到的 TCP/IP 服务器上的 **远程 IP 端口**。在部署包含客户端 WiFi TCP/IP Send 模块的模型之前，请确保服务器已启动并正在运行。

### **本地 IP 端口** — 发送主机上发送数据所用的 IP 端口 `25000` (默认) | `positive integer in the range [1 to 65,535]`

指定发送数据的应用程序的端口号。此本地端口充当 TCP/IP 服务器上的侦听端口。

#### 依赖项

要启用此参数，请将 **连接模式** 参数设置为 `Server`。

### **远程 IP 地址** — 数据发送到的服务器的远程 IP 地址 `192.168.1.2` (默认) | `any valid IP address`

指定数据发送到的服务器的远程 IP 地址。

#### 依赖项

要启用此参数，请将 **连接模式** 参数设置为 `Client`。

### **远程 IP 端口** — 数据发送到的服务器上的远程 IP 端口 `25000` (默认) | `positive integer in the range [1 to 65,535]`

指定接收服务器上数据发送到的端口号。

#### 依赖项

要启用此参数，请将 **连接模式** 参数设置为 `Client`。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A)

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

向互联网网络上的另一个 TCP/IP 主机发送 TCP/IP 数据包

WiFi TCP Send 模块通过无线网络将数据发送到远程主机或其他硬件板。

**注意**

您的防病毒软件或防火墙可能会阻止 TCP 流量。请配置软件以允许来自特定 IP 端口号的流量。
