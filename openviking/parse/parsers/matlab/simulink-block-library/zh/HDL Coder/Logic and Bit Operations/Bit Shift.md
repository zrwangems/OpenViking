---
type: simulink-block
title: 'Bit Shift'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'bitshift'
documentation_source_path: 'ref/bitshift.html'
language: zh-CN
chinese_source: official
---

# Bit Shift

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

对其执行逻辑或算术移位的输入信号。

- 最小位宽：2
- 最大位宽：128

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

经过逻辑或算术移位的输出信号。输出信号具有与输入信号相同的数据类型和位宽。

- 最小位宽：2
- 最大位宽：65535

## 参数

### **移位模式** — 移位的类型和方向 **逻辑左移位** (默认) | **逻辑右移位** | **算术右移位**

指定移位的类型和方向。

#### 编程用法

|  |
| --- |
| **模块参数：**`mode` |
| **类型：**字符串标量 | 字符向量 |
| **值：**`"Shift Left Logical"` | `"Shift Right Logical"` | `"Shift Right Arithmetic"` |
| **默认值：** `'Shift Left Logical'` |

### **移位长度** — 要移位的位数 `0` (默认)

指定要移位的位数。指定大于或等于零的值。

#### 编程用法

|  |
| --- |
| **模块参数：**`N` |
| **类型：**字符串标量 | 字符向量 |
| **值：**大于或等于零的值 |
| **默认值：** `'0'` |

## 所属库

HDL Coder / Logic and Bit Operations

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认的 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中的现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线阶段数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线阶段数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline。 |

## 版本历史

**在 R2014a 中推出**

### R2024b: 最大位宽为 65535 位

输出信号的最大位宽为 65535 位。在 R2024b 之前，最大位宽为 128 位。

## 描述

输入信号的逻辑或算术移位

Bit Shift 模块对输入信号执行逻辑或算术移位。

此模块在仿真和 HDL 代码生成行为方面与 Shift Arithmetic 模块不同。Bit Shift 模块可以执行有符号数的逻辑移位，而不必执行 `reinterpretcast` 运算。此模块使用基于 MATLAB Function 模块的实现，并且运算速度可能较慢。

Shift Arithmetic 模块移动输入数字的位或二进制小数点。与 Bit Shift 模块相比，此模块具有用于 HDL 代码生成的额外模块选项。当您要执行变量移位运算时，请使用 Shift Arithmetic 模块而不是 Bit Shift 模块。如果您以有符号数作为输入，该模块会执行该数的符号扩展。Shift Arithmetic 模块要求使用额外的已选择**存储的整数(SI)** 选项的 Data Type Conversion 模块。
