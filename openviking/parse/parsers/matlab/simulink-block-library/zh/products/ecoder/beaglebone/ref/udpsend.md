---
type: simulink-block
title: 'UDP Send'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / BeagleBone Black / Modeling'
documentation_page: 'udpsend'
documentation_source_path: 'beaglebone/ref/udpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Send

## 端口

### Input

### **Input** — 输入数据向量 vector

指定模块作为 UDP 数据包传输的输入数据向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
**复数支持：** Yes

## 参数

### **Remote IP address ('255.255.255.255' for broadcast)** — 要将 UDP 数据包发送到的 IP 地址 `'127.0.0.1'`（默认） | IP address | string

指定要将 UDP 数据包发送到的 IP 地址或主机名。如果指定主机名，请将其指定为 string。要广播 UDP 数据包，请指定 `'255.255.255.255'`。

### **Remote IP port** — 远程 IP 端口号 25000（默认） | 范围 [1, 65535] 内的 scalar

指定要将 UDP 数据包发送到的 IP 端口号。此参数在生成的代码中可调，但在仿真期间不可调。

在 Linux® 上，要将 IP 端口号设置为低于 1024，请以 root 权限运行 MATLAB®。例如，在 Linux 命令行中输入 `sudo matlab`。

### **Local IP port source** — 本地 IP 端口的来源 `Automatically determine`（默认） | `Specify via dialog`

指定模块使用的是系统分配的本地端口号，还是使用通过 **Local IP port** 参数指定的本地端口号。要让系统分配端口号，请选择 `Automatically determine`。如果接收地址期望来自特定端口号的 UDP 数据包，请选择 `Specify via dialog`，并使用 **Local IP port** 参数指定端口号。

### **Local IP port** — 本地 IP 端口号 -1（默认） | 范围 [1, 65535] 内的 scalar

指定模块从其发送 UDP 数据包的 IP 端口号。当接收地址期望来自特定端口号的消息时，使用此参数。

#### 参数依赖关系

- 要启用此参数，请将 **Local IP port source** 设置为
  `Specify via dialog`。

### **Send buffer size (bytes)** — 发送 UDP 数据包的缓冲区大小 8192（默认） | 范围 [1, 67108864] 内的 scalar

指定发送 UDP 数据包的缓冲区大小，以 bytes 为单位。使缓冲区足够大，以避免因缓冲区溢出而导致的数据丢失。

## 所属库

Embedded Coder Support Package for BeagleBone Black Hardware

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014b 中引入**

## 描述

发送 UDP 消息

UDP Send 模块将用户数据报协议 (UDP) 数据传输到远程主机。该模块将输入数据向量作为 UDP 数据包传输到远程 IP 网络端口。该模块向其发送 UDP 数据包的远程 IP 端口号在生成的代码中可调。
