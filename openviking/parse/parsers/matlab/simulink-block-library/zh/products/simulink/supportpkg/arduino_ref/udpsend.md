---
type: simulink-block
title: 'UDP Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Internet'
documentation_page: 'udpsend'
documentation_source_path: 'supportpkg/arduino_ref/udpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Send

## 端口

### 输入

### **Port\_1** — 输入数据向量 numeric vector

指定模块作为 UDP 数据包传输的输入数据向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32`

## 参数

### **远程 IP 地址** — 远程主机的 IP 地址 `192.168.0.5`（默认） | 有效 IP 地址 | string

指定要向其发送 UDP 数据包的 IP 地址或主机名。如果指定主机名，则将其指定为 string。要广播 UDP 数据包，请指定 `255.255.255.255`。

### **远程端口** — 远程端口的 IP 端口号 `55001`（默认） | [1, 65535] 范围内的整数

指定要向其发送 UDP 数据包的 IP 端口号。

### **本地端口** — 本地端口的 IP 端口号 `55002`（默认） | [1, 65535] 范围内的整数

指定模块从其发送 UDP 数据包的 IP 端口号。当接收地址期望来自特定端口号的消息时，使用此参数。

## 所属库

Simulink Support Package for Arduino Hardware / Ethernet Shield

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2013b 中引入**

## 描述

通过 UDP 网络将数据发送到远程主机

使用 UDP Send 模块将用户数据报协议 (UDP) 数据发送到远程主机。当传输速度比传输可靠性或消息顺序具有更高优先级时，使用此模块。在没有硬件的仿真期间，此模块不执行任何操作。
