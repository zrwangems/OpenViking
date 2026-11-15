---
type: simulink-block
title: 'UDP Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Network'
documentation_page: 'udpreceive'
documentation_source_path: 'supportpkg/raspberrypi_ref/udpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Receive

## 端口

### 输出

### **Data** — 从发送 UDP 主机接收的 UDP 数据包向量

在每个采样时间，模块将接收到的数据包内容输出为数据向量，其大小由 **Data size
(elements)** 参数指定。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Size** — 接收到的 UDP 消息中的数据字节数，标量

在每个采样时间，模块输出接收消息中的数据字节数。

**数据类型：** `uint8`

## 参数

### **Local IP port** — 接收 UDP 的 IP 端口号 `25000`（默认） | 范围 [`1`,`65535`] 中的正整数

指定要接收 UDP 消息的应用程序的端口号。将本地端口号与发送主机的远程端口号匹配。

### **Data type** — UDP 数据包中元素的数据类型 `uint8`（默认） | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

选择模块从发送主机接收数据字节时采用的数据类型。

### **Data size (elements)** — 每个 UDP 数据包中的数据元素数 `255`（默认） | 标量

指定要在每个 UDP 数据包中接收的元素数。

### **Sample time (seconds)** — 模块接收数据的时间间隔 `0.01`（默认） | 标量

指定调度器调用 UDP Receive 模块的频率，以 seconds 为单位。输入大于零的值。在实时操作中，将此参数设置为较小的值可降低 UDP 消息丢失的可能性。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Network

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

通过 IP 网络接收 UDP 数据包

UDP Receive 模块从 UDP 主机接收 UDP 数据包。使用该模块进行无状态和无连接的数据交换。

**注意**

您的防病毒软件或防火墙可能会阻止 UDP 流量。请配置该软件以允许来自特定 IP 端口号的流量。
