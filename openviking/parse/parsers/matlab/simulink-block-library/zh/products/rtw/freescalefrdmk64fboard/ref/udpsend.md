---
type: simulink-block
title: 'UDP Send'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-K64F Board / Modeling'
documentation_page: 'udpsend'
documentation_source_path: 'freescalefrdmk64fboard/ref/udpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Send

## 端口

### 输入

### **Port\_1** — 向另一个 UDP 主机发送 UDP 消息向量

该端口接受一个数组，并将其作为 UDP 消息通过 IP 网络端口发送到接收主机。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

## 参数

### **远程 IP 地址（广播时为 255.255.255.255）** — 接收 UDP 主机的 IP 地址 `192.168.1.2`（默认）

指定模块将 UDP 消息发送到的 IP 地址或主机名。要将消息广播到所有接收主机，请指定 `255.255.255.255`。

### **远程 IP 端口** — 接收 UDP 主机上的 IP 端口 `25000`（默认） | `1` 到 `65535` 之间的任意整数

指定接收主机上要将消息发送到的应用程序的端口号。将远程端口号与接收主机的本地端口号匹配。

### **本地 IP 端口（-1 表示自动分配端口）** — 发送 UDP 主机上的 IP 端口 `-1`（默认）

指定要从其发送消息的应用程序的端口号。

默认值 `-1` 会将本地端口号设置为随机可用端口号，并使用该端口发送消息。如果接收主机期望来自特定端口号的 UDP 消息，请指定该端口号。

## 所属库

Simulink Coder Support Package for NXP FRDM-K64F Board

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2017a 中引入**

## 描述

向 UDP 主机发送 UDP 消息

UDP Send 模块通过 IP 网络端口将输入向量作为 UDP 消息发送到 UDP 主机。

该模块从 **本地 IP 端口（-1 表示自动分配端口）** 参数中指定的端口号发送消息。

在 **远程 IP 地址（广播时为 255.255.255.255）** 和 **远程 IP 端口** 参数中指定接收主机的 IP 地址和端口号。

该模块以非阻塞模式发送 UDP 消息。
