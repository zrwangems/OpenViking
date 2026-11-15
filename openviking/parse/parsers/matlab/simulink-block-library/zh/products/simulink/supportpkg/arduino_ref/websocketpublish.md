---
type: simulink-block
title: 'WebSocket Publish'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Wi-Fi'
documentation_page: 'websocketpublish'
documentation_source_path: 'supportpkg/arduino_ref/websocketpublish.html'
language: zh-CN
chinese_source: worker-translation
---

# WebSocket Publish

## 端口

### 输入

### **Signal** — 要发布的行向量输入数据

要发布到 WebSocket 服务器的信号数据，指定为行向量。

该模块提供一个选项，最多可添加 10 个 **Signal** 输入端口，用于获取信号数据，其中每个信号均为行向量。

**示例：** `[1.5,3]`

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **Server port** — WebSocket 服务器上的端口号 `9000` (默认) | 任意端口号

指定承载 JSON 数据的 WebSocket 服务器上的端口号。

### **Number of Inputs** — 输入信号连接总数 `1` (默认) | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10`

选择连接到该模块的输入信号连接总数，这些输入信号随后会转换为 JSON 格式。

## 所属库

Simulink Support Package for Arduino Hardware / WiFi

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

以 JSON 格式将数据发布到 WebSocket 服务器

WebSocket Publish 模块将来自 Arduino® 硬件的数据发布到由 IP 地址和端口标识的 WebSocket 服务器。发布的数据采用 JavaScript Object Notation (JSON) 格式，WebSocket 客户端可以解释该格式以可视化数据。

如果 WebSocket 服务器托管在 Arduino 硬件上，网络上的任何设备都可以连接到该服务器并访问数据。

### 支持的 Arduino 开发板

- Arduino MKR1000
- Arduino MKR WIFI 1010
- Arduino Nano 33 IoT
- Arduino compatible ESP32 – WROOM board
- Arduino compatible ESP32 – WROVER board

### WebSocket JSON 数据

下图以 JSON 格式显示信号。

Arduino WebSocket Publish 的 JSON 格式

如果 JSON 字符串大小超过 1024 字节，则发布的数据将替换为错误消息。

WebSocket Publish 的错误格式
