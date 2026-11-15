---
type: simulink-block
title: 'XCP CAN FD Transport Layer'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / XCP'
documentation_page: 'xcpcanfdtransportlayer'
documentation_source_path: 'io_ref/xcpcanfdtransportlayer.html'
language: zh-CN
chinese_source: official
---

# XCP CAN FD Transport Layer

## 端口

### 输入

### **CAN FD Msg** — 正在处理 CAN FD 消息结构体 向量

该模块输入为 Simulink `CAN_FD_MESSAGE_BUS` 信号。有关 Simulink 总线对象的更多信息，请参阅 合成接口。

### **N** — 消息数量 整数

向量中的消息数量。
### 输出

### **CAN FD Msg** — CAN FD 消息输出 `CAN_FD_MESSAGE_BUS`

该模块的输出为 Simulink `CAN_FD_MESSAGE_BUS` 信号。有关 Simulink 总线对象的更多信息，请参阅 合成接口。

### **N** — 消息数量 整数

向量中的消息数量。

## 参数

R2025b 官方文档未提供。

## 所属库

Simulink Real-Time / XCP / CAN FD

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2022b 中推出**

## 描述

生成并消费由 CAN FD 硬件传输的 XCP 消息

XCP CAN FD Transport Layer 模块通过使用 Simulink® Real-Time™ CAN FD 库模块，处理模型发送或接收的 CAN FD 消息。

将该模块的输入端连接至接收 CAN FD 消息的模块。将该模块的输出端连接至通过 CAN FD 传输 XCP 消息的模块。设置传输模块，确保仅在 XCP 消息可用时发送 CAN FD 消息。否则，当 XCP 消息不可用时，该模块会发送 `0` 字节数据，导致行为未定义。
