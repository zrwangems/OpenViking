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
```yaml
ports:
- name: Data
  summary: UART 接收数据，向量 | 标量
  direction: output
- name: Status
  summary: UART 接收状态 0 | 1 | 2 | 3 | 4 | 8
  direction: output
```

### 输出

### **Data** — UART 接收数据，向量 | 标量

输出从 UART 端口读取的数据。

### **Status** — UART 接收状态 0 | 1 | 2 | 3 | 4 | 8

Status 端口输出以下值之一：

- 0 — 表示数据接收无错误
- 1 — 表示帧错误
- 2 — 表示奇偶校验错误
- 3 — 表示数据同步错误
- 4 — 表示数据接收中断
- 8 — 表示溢出错误。
## 参数
```yaml
parameters:
- name: UART 模块
  summary: UART 模块 A（默认） | B
  group: ''
- name: 附加数据包标头
  summary: 前缀标头 S（默认）
  group: ''
- name: 附加数据包终止符
  summary: 后缀终止符 E（默认）
  group: ''
- name: 数据类型
  summary: 要接收的数据类型 uint8（默认） | double | single | int8 | int8 | int16 | int32 | uint32 | boolean
  group: ''
- name: 数据长度
  summary: 要接收的数据大小 1（默认） | 正整数
  group: ''
- name: 启用阻塞模式
  summary: 为数据传输启用阻塞模式 off（默认） | on
  group: ''
- name: 采样时间
  summary: 模块读取数据的时间间隔 0.1（默认）
  group: ''
```

### **UART 模块** — UART 模块 `A`（默认） | `B`

选择要从中接收数据的 UART 模块。

### **附加数据包标头** — 前缀标头 `S`（默认）

指定附加数据包标头，用作数据包前的前缀，以同步数据包。

### **附加数据包终止符** — 后缀终止符 `E`（默认）

指定附加数据包终止符，用作数据包后的后缀，以同步数据包。

### **数据类型** — 要接收的数据类型 `uint8`（默认） | `double` | `single` | `int8` | `int8` | `int16` | `int32` | `uint32` | `boolean`

选择输出数据类型。

### **数据长度** — 要接收的数据大小 `1`（默认） | 正整数

指定要接收的数据长度。

### **启用阻塞模式** — 为数据传输启用阻塞模式 `off`（默认） | on

启用此选项可确保在接收数据之前检查 FIFO 缓冲区中是否有可用数据。

### **采样时间** — 模块读取数据的时间间隔 `0.1`（默认）

指定接收数据的采样时间。要异步执行此模块，请将采样时间设置为 -1。
## 所属库

C2000 Microcontroller Blockset / F29H85x

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2025a 中推出**

## 描述

从通用异步收发器 (UART) 端口接收数据

从通用异步收发器 (UART) 端口接收串行数据。

您可以为附加的包报头和终止符指定 ASCII 字符，以封装数据。您还可以指定希望通过该模块接收的数据类型和数据长度。

DMA 中断将在后台用于将数据从接收 FIFO 传输到缓冲区。当 FIFO 中接收到任何数据时，将触发 `UART_DMARx interrupt`。
