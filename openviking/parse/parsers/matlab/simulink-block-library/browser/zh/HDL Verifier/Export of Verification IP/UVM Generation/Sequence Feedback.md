---
type: simulink-block
title: 'Sequence Feedback'
family: 'hdlverifier'
product_id: 'hdlverifier'
product_name: 'HDL Verifier'
documentation_release: R2025b
official_category: 'Export of Verification IP / UVM Generation'
documentation_page: 'sequencefeedback'
documentation_source_path: 'ref/sequencefeedback.html'
language: zh-CN
chinese_source: worker-translation
---

# Sequence Feedback

## 端口

### 输入

### **Port\_1** — 来自 scoreboard 子系统的标量反馈信号

Sequence Feedback 模块直接从 scoreboard 子系统接收输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 发往 sequence 子系统的标量反馈信号

Sequence Feedback 模块直接将信号输出到 sequence 子系统。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

R2025b 中未记录。

## 所属库

HDL Verifier / For Use with DPI-C SystemVerilog

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

## 描述

在 UVM 测试平台模型中连接 scoreboard 与 sequence

Sequence Feedback 模块在 UVM 测试平台模型中将来自 scoreboard 的反馈信号提升到 sequence。该模块实现了一个 Unit Delay (Simulink) 模块，并将 **Initial condition** 参数设置为 `0`。
