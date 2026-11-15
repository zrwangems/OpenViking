---
type: simulink-block
title: 'Websocket Publish'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Network'
documentation_page: 'websocketpublish'
documentation_source_path: 'supportpkg/raspberrypi_ref/websocketpublish.html'
language: zh-CN
chinese_source: worker-translation
---

# Websocket Publish

## 端口

### 输入

### **Signal** — 要发布的输入数据 行向量

要发布到 WebSocket 服务器的信号数据，指定为行向量。

该模块提供选项，最多可添加 10 个 **Signal** 输入端口，您可使用这些端口获取信号数据，每个信号均为行向量。

**示例：** `[1.5,3]`

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **Block label** — 用于标识已发布 JSON 数据的唯一标签 `webPub 1`（默认值）

为该模块指定一个唯一标签，以标识已发布的 JSON 数据（该数据由输入信号数据生成）。标签最多可包含 128 个字符。

### **Server IP address** — WebSocket 服务器的 IP 地址 `127.0.0.1`（默认值） | 任意 IP 地址

托管 JSON 数据的 WebSocket 服务器的 IP 地址。

### **Server Port** — WebSocket 服务器上的端口号 `9000`（默认值） | 任意端口号

指定托管 JSON 数据的 WebSocket 服务器上的端口号。

**注意**

如果 **Server IP address** 和 **Server Port** 参数唯一，则可在 Simulink 模型中使用多个 Websocket Publish 模块。

### **Number of inputs** — 输入信号连接总数 `1`（默认值） | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10`

选择该模块的输入信号连接总数，随后会将其转换为 JSON 格式。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Network

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

## 描述

以 JSON 格式将数据发布到 WebSocket 服务器

WebSocket Publish 模块将来自 Raspberry Pi® 的数据发布到由 IP 地址和端口标识的 WebSocket 服务器。发布的数据采用 JavaScript Object Notation (JSON) 格式，WebSocket 客户端可以解释该格式以可视化数据。

如果 WebSocket 服务器托管在网络 IP 地址上，则网络上的任何设备都可以连接到该服务器并访问数据。

### WebSocket JSON 数据

下图显示了具有唯一模块标签的 JSON 格式信号。

WebSocket JSON 数据
