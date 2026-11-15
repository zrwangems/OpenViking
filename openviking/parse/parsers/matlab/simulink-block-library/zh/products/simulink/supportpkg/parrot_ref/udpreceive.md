---
type: simulink-block
title: 'UDP Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Parrot Minidrones / Modeling'
documentation_page: 'udpreceive'
documentation_source_path: 'supportpkg/parrot_ref/udpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Receive

## 端口

### 输出

### **Data** — 从发送 UDP 主机接收的 UDP 消息输出 [Nx1] 数组

在每个采样时间，该端口将所接收消息的数据字节输出为大小由 **Data size (N)** 参数指定的数据向量。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Size** — 所接收 UDP 消息中的数据字节数 标量

在每个采样时间，该端口输出所接收消息中的数据字节数。

**数据类型：** `uint16`

## 参数

### **Local IP port** — 接收 UDP 主机上的 IP 端口 `25000`（默认） | `[1, 65535]`

指定要接收消息的应用程序的端口号。将本地端口号与发送主机的远程端口号匹配。

**注意**

不要将端口 `24099` 和 `26061` 用于与 Parrot minidrone 的 UDP 通信，因为这些端口是保留的。

### **Data type** — UDP 消息中数据字节的数据类型 `uint8`（默认） | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

选择要从发送主机接收的字节的数据类型。

### **Data size (N)** — 每条 UDP 消息中的数据字节数 `4`（默认）

指定要在每条消息中接收的数据字节数。

### **Sample time** — 从发送 UDP 主机读取消息的间隔 `0.005`（默认） | 任何为 0.005 (5 ms) 倍数的非负值 | -1

输入接收数据的时间间隔。

当将此参数设置为 `-1` 时，Simulink® 根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Support Package for Parrot Minidrones

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018a 中引入**

## 描述

从 UDP 主机接收 UDP 消息

UDP Receive 模块从 UDP 主机接收 UDP 消息。

模块输出 **Data** 将 UDP 数据包数据作为指定数据类型的一维向量发出。模块输出 **Size** 发出 UDP 缓冲区中数据的大小。每次采样时，模块将 UDP 消息的字节输出为大小由 **Data size (N)** 参数指定的数据向量。

模块输出 `Data` 的数据类型取决于 **Data type** 参数。模块输出 `Size` 的数据类型为 `uint16`。`Size` 表示总字节数。例如，如果 `Data Type` 为 double，且元素数量（使用 `Data size (N)` 参数指定）为 5，则 `Size` 的值为 40，即 8\*5 字节。

该模块在 **Local IP port** 参数指定的端口号上接收消息。将 **Local IP port** 参数指定的端口号与发送主机的远程端口号匹配。

Parrot® minidrone 是一种小端设备。UDP Receive 模块期望所接收 UDP 数据的字节顺序为小端。

**注意**

如果您在使用 UDP 与计算机通信时遇到问题，防病毒或防火墙软件可能正在阻止 UDP 流量。如果是这样，请配置该软件以允许特定 IP 端口号的流量。
