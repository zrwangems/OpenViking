---
type: simulink-block
title: 'UDP Send'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F2838x / M4'
documentation_page: 'udpsend'
documentation_source_path: '../simulink/supportpkg/parrot_ref/udpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Send

## 端口

### 输入

### **Port1** — 向另一个 UDP 主机发送 UDP 消息向量

该端口接受一个数组，并通过 IP
网络端口将其作为 UDP 消息发送到接收主机。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

## 参数

### **Remote IP address** — 接收 UDP 主机的 IP 地址 `192.168.3.2`（默认）

指定模块将 UDP 消息发送到的 IP 地址或主机名。**Remote IP address** 设置为 192.168.3.2；
请勿更改此 IP 地址。

### **Remote IP Port** — 接收 UDP 主机上的 IP 端口 `25000`（默认）| [1, 65535]

指定接收主机上要将消息发送到的应用程序的端口号。将远程端口号与接收主机的本地端口号匹配。

**注意**

不要将端口 `24099` 和 `26061`
用于与 Parrot minidrone 的 UDP 通信，因为这些端口是保留的。

### **Local IP Port** — 发送 UDP 主机上的 IP 端口 `2048`（默认）| [1, 65535]

如果为 **Local IP port source** 选择 `Specify via dialog` 选项，则此参数会显示。指定要从中发送消息的应用程序的端口号。

## 所属库

Simulink Support Package for Parrot Minidrones

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

向 UDP 主机发送 UDP 消息

UDP Send 模块通过 IP
网络端口将输入向量作为 UDP 消息发送到 UDP 主机。

在 **Remote IP address** 和 **Remote IP Port**
参数中指定接收主机的 IP 地址和端口号。
