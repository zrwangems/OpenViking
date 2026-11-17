---
type: simulink-block
title: 'F28M35x/F28M36x UART Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F28M35x / M3'
documentation_page: 'f28m35xf28m36xuarttransmit'
documentation_source_path: 'ref/f28m35xf28m36xuarttransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# F28M35x/F28M36x UART Transmit

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

DMA 将在内部用于将数据复制到 FIFO 中。
## 参数
```yaml
parameters:
- name: UART Port
  summary: 选择用于数据传输的 UART 端口 UART0（默认）| UART1 | UART2 | UART3 | UART4
  group: ''
- name: Additional package header
  summary: 前缀头 S（默认）
  group: ''
- name: Additional package terminator
  summary: 后缀终止符 E（默认）
  group: ''
- name: Enable blocking mode
  summary: 启用数据传输的阻塞模式 off（默认）| on
  group: ''
```

### **UART Port** — 选择用于数据传输的 UART 端口 `UART0`（默认）| `UART1` | `UART2` | `UART3` | `UART4`

从 UART0 到 UART4 中选择一个端口号用于数据传输。

UART Port 选择允许访问处理器上存在的不同 UART 模块。

### **Additional package header** — 前缀头 `S`（默认）

指定用作数据包前缀的附加包头部，以同步数据包。

### **Additional package terminator** — 后缀终止符 `E`（默认）

指定用作数据包后缀的附加包终止符，以同步数据包。

### **Enable blocking mode** — 启用数据传输的阻塞模式 `off`（默认）| on

启用此选项可确保在发送数据之前检查 FIFO 缓冲区是否有可用数据。
## 所属库

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / M3

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

将串行数据发送到通用异步收发器（UART）端口

通过通用异步收发器（UART）端口发送串行数据。您可以使用附加包头部和终止符指定 ASCII 字符来封装数据。
