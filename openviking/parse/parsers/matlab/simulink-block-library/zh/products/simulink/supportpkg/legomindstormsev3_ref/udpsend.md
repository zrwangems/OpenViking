---
type: simulink-block
title: 'UDP Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Communication Protocol Blocks'
documentation_page: 'udpsend'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/udpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Send

## 端口

### 输入

### **Port\_1** — 用于接收数据的输入端口

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **远程 IP 地址（用于广播的 ‘255.255.255.255’）** — 远程主机的远程 IP 地址 127.0.0.1（默认）| 标量

输入远程设备上 IP 节点的地址或主机名。

要将 UDP 消息广播到所有设备，请使用默认参数值 `'255.255.255.255'`。请谨慎使用此方法，以避免产生不必要的广播流量。通常，IP 路由器会配置为丢弃发送到 `'255.255.255.255'` 的广播 UDP 数据包。

### **远程 IP 端口** — 远程主机的远程 IP 端口号 25000（默认）| 标量

远程设备上 IP 端口的编号，范围可以为 1 到 65535。此值默认为 `25000`。

### **本地 IP 端口源** — 模块从中发送数据的本地 IP 端口源 Automatically determine（默认）| Specify

选择此选项以确定模块从中发送数据的本地端口源。

### **本地端口** — 模块从中发送数据的本地端口 2048（默认）| 标量

输入模块将数据发送到远程主机时所使用的本地端口。

## 所属库

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware Simulink Coder Support Package for BeagleBone Blue Hardware / Communication Simulink Support Package for Android Devices / Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

将 UDP 数据包发送到 Internet 网络上的另一个 UDP 主机

将 UDP 数据包发送到由远程 IP 地址和远程 IP 端口参数标识的网络地址。

**注意**

如果您在使用 UDP 与计算机通信时遇到问题，请检查是否有防病毒或防火墙软件可能阻止 UDP 流量。如果是这样，请尝试重新配置该软件，以允许特定 IP 端口号的 UDP 流量。
