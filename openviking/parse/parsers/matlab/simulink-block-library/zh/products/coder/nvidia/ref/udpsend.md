---
type: simulink-block
title: 'UDP Send'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Network'
documentation_page: 'udpsend'
documentation_source_path: 'nvidia/ref/udpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Send

## 端口

### 输入

### **Port\_1** — 输入数据端口向量

该端口接受一个数组，并将其作为 UDP 数据包通过 IP 网络端口发送到接收 UDP 主机。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **远程 IP 地址（广播时为 '255.255.255.255'）** — 接收 UDP 主机的 IP 地址 `'255.255.255.255'`（默认） | `any valid IP address`

指定模块要将 UDP 数据包发送到的 IP 地址或主机名。要将数据包广播到所有接收主机，请指定 `'255.255.255.255'`。

### **远程 IP 端口** — 接收主机上数据发送到的 IP 端口 `25000`（默认） | [1,65535] 范围内的正整数

指定接收主机上要向其发送数据包的应用的端口号。使远程端口号与接收主机的本地端口号匹配。

## 所属库

NVIDIA Jetson and NVIDIA DRIVE / Network

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

将 UDP 数据包发送到 UDP 主机

UDP Send 模块将 UDP 数据包发送到 UDP 主机。使用该模块进行无状态且无连接的数据传输。

接收主机的 IP 地址和端口号在 **远程 IP 地址（广播时为 255.255.255.255）** 和 **远程 IP 端口** 参数中指定。

该模块接受数据类型为 `int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`single` 或 `double` 的输入。

**注意**

您的防病毒软件或防火墙可能会阻止 UDP 流量。请配置该软件以允许来自特定 IP 端口号的流量。
