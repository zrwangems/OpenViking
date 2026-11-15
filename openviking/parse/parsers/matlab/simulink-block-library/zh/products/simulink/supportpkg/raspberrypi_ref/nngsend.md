---
type: simulink-block
title: 'NNG Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Communication'
documentation_page: 'nngsend'
documentation_source_path: 'supportpkg/raspberrypi_ref/nngsend.html'
language: zh-CN
chinese_source: worker-translation
---

# NNG Send

## 端口

### 输入

### **Port\_1** — 输入数据向量

该模块接受要发布到服务器的输入数据，指定为向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### 输出

### **Status** — 来自发布者的状态码，标量

该模块输出发布者响应发布请求而发出的状态码。如果发布者接受要发布的消息，该端口输出 `0`。任何非零输出表示发布者已拒绝该消息。

**数据类型：** `int8`

## 参数

### **IPC name** — 进程间通信的名称 `pubsub`（默认） | string

输入进程间通信 (IPC) 的名称。此 IPC 名称会反映在 URL 中。

### **URL** — 用于发送和接收数据的服务地址 `ipc:///tmp/pubsub.ipc`（默认） | string

URL 是发布者用来识别合法订阅者以传递数据的服务地址。发布者使用此 URL 接收在同一 URL 上发送的数据。IPC 名称会反映在 URL 中。

**注意**

无法编辑此参数。

### **Print diagnostic messages** — 将发布者响应保存到日志文件 off（默认） | on

选择此选项可在每次将数据发送给订阅者时，将发布者的响应保存到日志文件。日志文件的名称是 Simulink® 模型名称后跟 `.log`。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Communication

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2023a 中引入**

## 描述

使用发布/订阅协议通过 nanomsg next gen (NNG) 发送数据

使用 NNG Send 模块将数据广播到所有订阅同一统一资源定位符 (URL) 的应用程序。该模块对所有进程间通信使用发布/订阅协议。在发布/订阅协议中，每个想要发送数据的发布者都将数据发布到某个 URL 上，而每个想要接收数据的订阅者都订阅同一 URL。
