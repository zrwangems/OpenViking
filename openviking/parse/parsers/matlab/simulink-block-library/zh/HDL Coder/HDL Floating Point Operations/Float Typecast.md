---
type: simulink-block
title: 'Float Typecast'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Floating Point Operations'
documentation_page: 'floattypecast'
documentation_source_path: 'ref/floattypecast.html'
language: zh-CN
chinese_source: official
---

# Float Typecast

## 端口

### 输入

### **Port\_1(u)** — 输入信号 `scalar` | `vector`

向模块提供输入的端口。

**数据类型:** `singledouble` | `uint32` | `fixed point`
### 输出

### **Port\_1(y)** — 输出信号 `scalar` | `vector`

从模块获取计算输出的端口。

**数据类型:** `single` | `double` | `uint32` | `fixed point`

## 参数

R2025b 官方文档未提供。

## 所属库

HDL Coder / HDL Floating Point Operations

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

该模块在 `Native Floating Point` 模式下支持 HDL 代码生成。要使用此模式，请将 `single` 或 `uint32` 数据类型指定为模块的输入。借助 HDL 代码顾问，您可以替换使用**存储的整数(SI)** 模式并在浮点和定点数据类型之间转换的 Data Type Conversion 模块。

该模块支持复信号的代码生成。

## 版本历史

**在 R2017b 中推出**

## 描述

将浮点类型转换为无符号整数，或者反之

该模块将输入的基础位强制转换为对应的定点或浮点表示。模块的输入和输出包含相同的位数。

| 输入数据类型 | 输出数据类型 |
| --- | --- |
| `half` | `uint16` |
| `single` | `uint32` |
| `double` | `uint64` |
| `uint32` | `single` |
| `uint64` | `double` |
| `uint16` | `half` |

下图显示模块封装、行为和输出数据类型如何根据您指定的输入数据类型而动态变化。

Shows how the output data types vary in response to changes in the input data type.
