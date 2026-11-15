---
type: simulink-block
title: 'UDP Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Network'
documentation_page: 'udpsend'
documentation_source_path: 'supportpkg/raspberrypi_ref/udpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Send

## 端口

### 输入

### **Port\_1** — 输入数据向量

该模块接受数组，并通过 IP 网络端口将其作为 UDP 数据包发送到接收 UDP 主机。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **远程 IP 地址（用于广播的 '255.255.255.255'）** — `'255.255.255.255'`（默认） | 任何有效 IP 地址

指定该模块将 UDP 数据包发送到的 IP 地址或主机名。要将数据包广播到所有接收主机，请指定
`'255.255.255.255'`。

### **远程 IP 端口** — 接收主机上数据发送到的 IP 端口 `25000`（默认） | 范围为 [`1`,`65535`] 的正整数

指定接收主机上您要将数据包发送到的应用程序的端口号。将远程端口号与接收主机的本地端口号匹配。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Network

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

通过 IP 网络发送 UDP 数据包

UDP Send 模块将 UDP 数据包发送到 UDP 主机。使用该模块进行无状态和无连接的数据传输。

**注意**

您的防病毒软件或防火墙可能会阻止 UDP 流量。请配置软件以允许来自特定 IP 端口号的流量。
