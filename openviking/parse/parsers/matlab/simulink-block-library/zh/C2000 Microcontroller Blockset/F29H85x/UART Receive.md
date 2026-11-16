---
type: simulink-block
title: 'C29x UART Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F29H85x'
documentation_page: 'c29xuartreceiveblock'
documentation_source_path: 'ref/c29xuartreceiveblock.html'
language: zh-CN
chinese_source: worker-translation
---

# C29x UART Receive

## 端口

### 输出

### **Data** — UART 接收数据向量 | 标量

输出从 UART 端口读取的数据。

### **Status** — UART 接收状态 0 | 1 | 2 | 3 | 4 | 8

Status 端口输出以下值之一：

- 0 — 表示数据接收无错误
- 1 — 表示帧错误
- 2 — 表示奇偶校验错误
- 3 — 表示数据同步错误
- 4 — 表示数据接收中出现 break
- 8 — 表示溢出错误。

## 参数

### **UART 模块** — UART 模块 `A`（默认）| `B`

选择要从中接收数据的 UART 模块。

### **附加包报头** — 前缀报头 `S`（默认）

指定用作数据包前缀的附加包报头，以同步数据包。

### **附加包终止符** — 后缀终止符 `E`（默认）

指定用作数据包后缀的附加包终止符，以同步数据包。

### **数据类型** — 要接收的数据类型 `uint8`（默认）| `double` | `single` | `int8` | `int8` | `int16` | `int32` | `uint32` | `boolean`

选择输出数据类型。

### **数据长度** — 要接收的数据大小 `1`（默认）| 正整数

指定要接收的数据长度。

### **启用阻塞模式** — 为数据传输启用阻塞模式 `off`（默认）| on

启用此选项可确保在接收数据之前检查 FIFO 缓冲区的数据可用性。

### **采样时间** — 模块读取数据的时间间隔 `0.1`（默认）

指定接收数据的采样时间。要异步执行此模块，请将 Sample Time 设置为 -1。

## 所属库

C2000 Microcontroller Blockset / F29H85x

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2025a 中引入**

## 描述

从通用异步收发器 (UART) 端口接收数据

从通用异步接收器/发送器 (UART) 端口接收串行数据。

您可以使用附加包报头和终止符指定用于封装数据的 ASCII 字符。您可以使用该模块指定要接收的数据类型和数据长度。

DMA 中断将在后台用于从 Receive FIFO 到缓冲区的数据传送。当 FIFO 中接收到任何数据时，将触发 `UART_DMARx interrupt`。
