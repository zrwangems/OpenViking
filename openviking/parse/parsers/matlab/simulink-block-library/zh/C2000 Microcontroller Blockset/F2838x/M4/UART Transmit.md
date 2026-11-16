---
type: simulink-block
title: 'F2838x-M4 UART Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F2838x / M4'
documentation_page: 'f2838xm4uarttransmit'
documentation_source_path: 'ref/f2838xm4uarttransmit.html'
language: zh-CN
chinese_source: official
---

# F2838x-M4 UART Transmit

## 端口

### 输入

### **Data** — UART 发送数据 向量 | 标量

该端口将数据发送到 UART 端口。

## 参数

### **附加包头** — 前缀头 `S` (默认)

指定要用作数据包前缀的附加包头，以同步数据包。

### **附加包终止符** — 后缀终止符 `E` (默认)

指定要用作数据包后缀的附加包终止符，以同步数据包。

### **启用阻塞模式** — 启用数据传输阻塞模式 `off` (默认) | on

启用此选项可确保在发送数据之前检查 FIFO 缓冲区中的数据可用性。

## 所属库

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / M3

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2020a 中推出**

## 描述

向通用异步收发器 (UART) 端口发送串行数据

通过通用异步收发器 (UART) 端口发送串行数据。您可以使用附加的包头和终止符来指定用于打包数据的 ASCII 字符。

内部将使用 DMA 来复制 FIFO 中的数据。
