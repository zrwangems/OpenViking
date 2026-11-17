---
type: simulink-block
title: 'Byte Reversal'
family: 'slrealtime'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'bytereversal'
documentation_source_path: 'ref/bytereversal.html'
language: zh-CN
chinese_source: official
---

# Byte Reversal

## 端口

### 输入

### **Port\_1** — 要转换的数据 标量、向量、矩阵

需要通过模块更改字节顺序的数据。模块使用的输入端口数取决于您为**输入数目**参数指定的值。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 转换的数据 标量、向量、矩阵

修改了字节顺序的数据。模块使用的输出端口数取决于您为**输入数目**参数指定的值。每个输入端口映射到匹配的输出端口。输入端口 1 接收到的数据通过输出端口 1 发送，依此类推。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **输入数目** — 模块输入的数目 1 (默认) | 整数

指定模块输入的数目。该模块创建该数目的输入端口和输出端口。每个输入端口映射到匹配的输出端口。输入 `Port_1` 接收到的数据通过输出  `Port_1` 发送，依此类推。

反转字节顺序不会改变数据类型。输入和输出保留匹配的数据类型。

## 所属库

Embedded Coder / Embedded Targets / Host Communication

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2011a 中推出**

## 描述

反转输入字中的字节顺序

Byte Reversal 模块更改输入到该模块的数据中字节的顺序。当进程在使用不同端序的目标计算机之间进行通信时，例如在采用小端的 Intel® 处理器和其他大端处理器之间进行通信时，请使用此模块。默认情况下，Texas Instruments® 处理器是小端处理器。

要在具有不同端序的处理器之间交换数据，请在紧挨发送模块之前和紧挨接收模块后放置一个 Byte Reversal 模块。

此模型显示三个输入的字节反转。每条路径的输入端口和输出端口都匹配。
