---
type: simulink-block
title: 'F2838x-M4 UART Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / Arm Cortex - M3/M4'
documentation_page: 'f2838xm4uartreceive'
documentation_source_path: 'ref/f2838xm4uartreceive.html'
language: zh-CN
chinese_source: official
---

# F2838x-M4 UART Receive

## 端口

### 输出

### **Data** — UART 接收数据 向量 | 标量

输出从 UART 端口读取的数据。

### **Status** — UART 接收状态 0 | 1 | 2 | 3 | 4 | 8

状态端口输出以下值之一：

- 0 - 表示数据接收无误
- 1 - 表示帧误差
- 2 - 表示奇偶校验错误
- 3 - 表示数据同步错误
- 4 - 表示数据接收中断
- 8 - 表示超限错误。

## 参数

### **附加包头** — 前缀头 `S` (默认)

指定要用作数据包前缀的附加包头，以同步数据包。

### **附加包终止符** — 后缀终止符 `E` (默认)

指定要用作数据包后缀的附加包终止符，以同步数据包。

### **数据类型** — 要接收的数据类型 `uint8` (默认) | `double` | `single` | `int8` | `int8` | `int16` | `int32` | `uint32` | `boolean`

选择输出数据类型。

### **数据长度** — 要接收的数据大小 `1` (默认) | 正整数

指定要接收的数据长度。

### **启用阻塞模式** — 启用数据传输阻塞模式 `off` (默认) | on

启用此选项可确保在接收数据之前检查 FIFO 缓冲区中的数据可用性。

### **采样时间** — 模块读取数据的时间间隔 `0.1` (默认)

指定接收数据的采样时间。要异步执行此模块，请将采样时间设置为 -1。

## 所属库

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / M3

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2020a 中推出**

## 描述

从通用异步收发器 (UART) 端口接收数据

从通用异步收发器 (UART) 端口接收串行数据。

您可以使用附加的包头和终止符来指定用于打包数据的 ASCII 字符。您可以使用该模块指定要接收的数据类型和数据长度。

DMA 中断将在后台用于将数据从接收 FIFO 传输到缓冲区。当 FIFO 中接收到任何数据时，`UART_DMARx interrupt` 将被触发。
