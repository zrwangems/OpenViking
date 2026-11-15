---
type: simulink-block
title: 'UDP Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'udpsend'
documentation_source_path: 'supportpkg/android_ref/udpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Send

## 端口

### 输入

### **Port\_1** — 输入数据信号，数值向量

输入数据信号，指定为数值向量。该模块将此数据作为 UDP 数据发送到远程 IP 端口处的远程 IP 地址。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32`

## 参数

### **Remote IP address ('255.255.255.255' for broadcast)** — 远程主机的 IP 地址 `'255.255.255.255'`（默认）| 有效 IP 地址

指定要将 UDP 数据发送到的远程主机的 IP 地址。要广播 UDP 消息，请使用默认值 `'255.255.255.255'`。请谨慎使用默认 IP 地址，以避免在网络上产生不必要的广播流量。通常，IP 路由器会配置为丢弃发送到此默认 IP 地址的广播 UDP 数据包。

### **Remote IP port** — 远程主机的 IP 端口号 `25000`（默认）| 1 到 65,535 的整数

指定要将 UDP 数据发送到的远程主机的 IP 端口号。IP 端口号必须是 1 到 65,535 的整数。

## 所属库

Simulink Support Package for Android Devices / Communication

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014a 中引入**

## 描述

通过 UDP 网络向远程主机发送数据

使用 UDP Send 模块将用户数据报协议 (UDP) 数据发送到远程主机。

**注意**

如果在主机和 Android® 设备之间使用 UDP 通信时遇到问题，防病毒或防火墙软件可能会阻止 UDP 流量。在这种情况下，请重新配置该软件，以启用特定 IP 端口号的 UDP 流量。
