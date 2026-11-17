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
chinese_source: worker-translation
---

# F2838x-M4 UART Transmit

## 端口
```yaml
ports:
- name: Data
  summary: UART 发送数据向量 | 标量
  direction: input
```

### 输入

### **Data** — UART 发送数据向量 | 标量

该端口将数据发送到 UART 端口。
## 参数
```yaml
parameters:
- name: Additional package header
  summary: 前缀头 S（默认）
  group: ''
- name: Additional package terminator
  summary: 后缀终止符 E（默认）
  group: ''
- name: Enable blocking mode
  summary: 启用数据发送的阻塞模式 off（默认）| on
  group: ''
```

### **Additional package header** — 前缀头 `S`（默认）

指定用作数据包前缀的附加包头部，以同步数据包。

### **Additional package terminator** — 后缀终止符 `E`（默认）

指定用作数据包后缀的附加包终止符，以同步数据包。

### **Enable blocking mode** — 启用数据发送的阻塞模式 `off`（默认）| on

启用此选项可确保在发送数据之前检查 FIFO 缓冲区是否有可用数据。
## 所属库

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / M3

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020a 中引入**

## 描述

向通用异步收发器（UART）端口发送串行数据

通过通用异步收发器（UART）端口发送串行数据。
您可以指定 ASCII 字符，通过附加包头部和终止符来封装数据。

内部将使用 DMA 将数据复制到 FIFO 中。
