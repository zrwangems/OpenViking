---
type: simulink-block
title: 'J1939 CAN Transport Layer'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'J1939'
documentation_page: 'j1939cantransportlayer'
documentation_source_path: 'io_ref/j1939cantransportlayer.html'
language: zh-CN
chinese_source: official
---

# J1939 CAN Transport Layer

## 端口

### 输入

### **CAN Msg** — CAN 消息结构体正在被消费 向量

正在被消费的 CAN 消息结构体向量。

### **N** — 消息数量 整数

向量中的消息数量。
### 输出

### **CAN Msg** — 正在生成 CAN 消息结构体 向量

正在生成 CAN 消息结构体的向量。

### **N** — 消息数量 整数

向量中的消息数量。

## 参数

R2025b 官方文档未提供。

## 所属库

Simulink Real-Time / J1939

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2020b 中推出**

## 描述

生成并处理通过 CAN 硬件传输的 J1939 消息

J1939 CAN Transport Layer 模块通过使用 Simulink® Real-Time™ CAN 库模块处理模型发送或接收的 CAN 消息。

将该模块的输入端连接到接收 CAN 消息的模块。将该模块的输出端连接至通过 CAN 总线传输 J1939 消息的模块。设置发送模块，使其仅在 J1939 消息可用时发送 CAN 消息。否则，当 J1939 消息不可用时，该模块会发送 `0` 字节数据，导致行为未定义。
