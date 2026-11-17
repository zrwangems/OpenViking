---
type: simulink-block
title: 'Byte Reversal'
family: 'signal-management'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Signal Management'
documentation_page: 'bytereversal'
documentation_source_path: 'ref/bytereversal.html'
language: zh-CN
chinese_source: worker-translation
---

# Byte Reversal

## 端口

### 输入

### **Port\_1** — 要转换的数据 标量、向量、矩阵

模块更改其字节顺序的数据。该模块使用的输入端口数取决于你为 **Number of inputs** 参数指定的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 输出

### **Port\_1** — 转换后的数据 标量、向量、矩阵

具有修改后字节顺序的数据。该模块使用的输出端口数取决于你为 **Number of inputs** 参数指定的值。每个输入端口映射到匹配的输出端口。在输入端口 1 上接收的数据通过输出端口 1 发送，以此类推。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **Number of inputs** — 模块输入数 1 (default) | integer

指定模块输入数。该模块创建该数量的输入端口和输出端口。每个输入端口映射到匹配的输出端口。在输入 `Port_1` 上接收的数据通过输出 `Port_1` 发送，以此类推。

反转字节顺序不会更改数据类型。输入和输出保持匹配的数据类型。

## 所属库

Motor Control Blockset / Signal Management

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2024a 中引入**

## 描述

反转输入字中的字节顺序

Byte Reversal 模块更改你输入到该模块的数据中的字节顺序。当一个进程在使用不同字节序的目标计算机之间通信时，例如在采用小端序的 Intel® 处理器与采用大端序的其他处理器之间通信时，使用此模块。Texas Instruments® 处理器默认采用小端序。

要在具有不同字节序的处理器之间交换数据，请将 Byte Reversal 模块放在发送模块之前，并紧跟在接收模块之后。

此模型显示了三个输入的字节反转。每个路径的输入端口和输出端口匹配。
