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
chinese_source: worker-translation
---

# Byte Reversal

## 端口

### 输入

### **Port\_1** — 要转换的数据 标量、向量、矩阵

模块更改其字节顺序的数据。模块使用的输入端口数量取决于为 **Number of inputs** 参数指定的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 转换后的数据 标量、向量、矩阵

字节顺序已修改的数据。模块使用的输出端口数量取决于为 **Number of inputs** 参数指定的值。每个输入端口映射到匹配的输出端口。在输入端口 1 上接收的数据通过输出端口 1 发送，依此类推。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **Number of inputs** — 模块输入的数量 1（默认）| 整数

指定模块输入的数量。模块将创建该数量的输入端口和输出端口。每个输入端口映射到匹配的输出端口。在输入 `Port_1` 上接收的数据通过输出 `Port_1` 发送，依此类推。

反转字节顺序不会更改数据类型。输入和输出保持匹配的数据类型。

## 所属库

Embedded Coder / Embedded Targets / Host Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2011a 中引入**

## 描述

反转输入字中字节的顺序

Byte Reversal 模块更改输入到该模块的数据中字节的顺序。当进程在使用不同字节序的目标计算机之间通信时（例如在使用小端序的 Intel® 处理器与使用大端序的其他处理器之间）使用此模块。Texas Instruments® 处理器默认采用小端序。

要在具有不同字节序的处理器之间交换数据，请将 Byte Reversal 模块放在发送模块之前以及接收模块之后。

此模型展示了三个输入的字节反转。每条路径的输入端口和输出端口相匹配。
