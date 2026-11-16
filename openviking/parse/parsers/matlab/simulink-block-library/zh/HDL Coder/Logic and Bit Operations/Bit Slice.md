---
type: simulink-block
title: 'Bit Slice'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'bitslice'
documentation_source_path: 'ref/bitslice.html'
language: zh-CN
chinese_source: official
---

# Bit Slice

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

对其执行位切片的输入信号。输入信号的最大位宽为 128。

**数据类型:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

经过位切片的输出信号。输出的字长计算为 `(MSB Position - LSB Position) + 1`，其中 **MSB 位置**和 **LSB 位置**是模块参数。

**数据类型:** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **MSB 位置** — 最高有效位的位置 7 (默认)

指定要提取的字段的最高有效位 (MSB) 的位置（从 0 开始）。

对于输入字长 `WS`，**MSB 位置**必须满足以下约束：

`WS > MSB Position >= LSB Position >= 0`

#### 编程用法

|  |
| --- |
| **模块参数：**`lidk` |
| **类型：**字符串标量 | 字符向量 |
| **值：**满足前述约束的正整数值 |
| **默认值：**`'7'` |

### **LSB 位置** — 最低有效位的位置 0 (默认)

指定要提取的字段的最低有效位 (LSB) 的位置（从 0 开始）。

对于输入字长 `WS`，**LSB 位置**必须满足以下约束：

`WS > MSB Position >= LSB Position >= 0`

#### 编程用法

|  |
| --- |
| **模块参数：**`ridk` |
| **类型：**字符串标量 | 字符向量 |
| **值：**满足前述约束的正整数值 |
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

## 描述

从输入信号返回连续位字段

Bit Slice 模块从输入信号返回连续位字段。使用 **LSB 位置**和 **MSB 位置**参数中的从 0 开始的索引来指定位字段的下边界和上边界。对于输入字长 `WS`，**LSB 位置**和 **MSB 位置**必须满足以下约束：

`WS > MSB Position >= LSB Position >= 0`
