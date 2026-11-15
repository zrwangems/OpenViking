---
type: simulink-block
title: 'NNG Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Communication'
documentation_page: 'nngreceive'
documentation_source_path: 'supportpkg/raspberrypi_ref/nngreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# NNG Receive

## 端口

### 输出

### **Data** — 接收的数据 [Nx1] 数组

从发布者接收的数据，指定为 *N*×1 向量。*N* 是由 **数据长度 (N)** 参数指定的消息长度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Status** — 新消息指示符 `0` | `1`

如果订阅者自上一个采样时间以来收到新消息，**Status** 端口输出 `1`。否则，该端口输出 `0`。

**数据类型：** `Boolean`

## 参数

### **IPC 名称** — 进程间通信的名称 `pubsub` (默认) | string

输入进程间通信 (IPC) 的名称。此 IPC 名称会反映在 URL 中。

### **URL** — 用于发送和接收数据的服务地址 `ipc:///tmp/pubsub.ipc` (默认) | string

URL 是发布者用来识别合法订阅者以传递数据的服务地址。此 URL 由发布者用来接收在同一 URL 上发送的数据。IPC 名称会反映在 URL 中。

**注意**

不能编辑此参数。

### **数据类型** — 输入数据的类型 `uint8` (默认) | `int8` | `uint16` | `int16` | `uint32` | `int32` | `single` | `double`

选择订阅者在每个采样时间接收的输入数据的类型。

### **数据长度 (N)** — 输入数据的长度 `1` (默认) | 1 到 2^31 之间的整数

输入订阅者在每个采样时间接收的数据的最大长度。

### **打印诊断消息** — 将订阅者响应保存到日志文件 off (默认) | on

选择此选项可在订阅者每次接收到数据时，将来自订阅者的响应保存到日志文件。日志文件的名称为 Simulink® 模型名称后跟 `.log`。

### **采样时间** — 检查来自服务器数据的频率 `-1` (默认) | 任何正整数

输入订阅者检查来自发布者的新数据的频率。当您将采样时间指定为 `-1` 时，该模块会基于其在 Simulink 模型中的上下文继承其采样时间。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Communication

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2023a 中引入**

## 描述

使用发布/订阅协议通过 nanomsg next gen (NNG) 接收数据

使用 NNG Receive 模块从发布者接收指定统一资源定位符 (URL) 的数据。该模块对所有进程间通信使用发布/订阅协议。在发布/订阅协议中，每个想要发送数据的发布者都会在某个 URL 上发布数据，而每个想要接收数据的订阅者都会订阅同一个 URL。
