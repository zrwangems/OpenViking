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
chinese_source: worker-translation
---

# Bit Slice

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

执行位切片的输入信号。输入信号的最大位宽为 128。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

经过位切片的输出信号。输出的字长按 `(MSB Position - LSB Position) + 1` 计算，其中 **MSB Position** 和 **LSB Position** 为模块参数。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **MSB Position** — 最高有效位位置 7（默认）

指定要提取字段的最高有效位（MSB）的位位置（从零开始）。

对于输入字长 `WS`，**MSB Position** 必须满足以下约束：

`WS > MSB Position >= LSB Position >= 0`

#### 编程使用

|  |
| --- |
| **模块参数：** `lidk` |
| **类型：** 字符串标量 | 字符向量 |
| **值：** 满足前述约束的正整数值 |
| **默认：** `'7'` |

### **LSB Position** — 最低有效位位置 0（默认）

指定要提取字段的最低有效位（LSB）的位位置（从零开始）。

对于输入字长 `WS`，**LSB Position** 必须满足以下约束：

`WS > MSB Position >= LSB Position >= 0`

#### 编程使用

|  |
| --- |
| **模块参数：** `ridk` |
| **类型：** 字符串标量 | 字符向量 |
| **值：** 满足前述约束的正整数值 |
| **默认：** `'0'` |

## 所属库

HDL Coder / Logic and Bit Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |

## 版本历史

**在 R2014a 中引入**

## 描述

从输入信号返回连续位字段

Bit Slice 模块从输入信号返回连续位字段。使用 **LSB Position** 和 **MSB Position** 参数中从零开始的索引指定位字段的下边界和上边界。对于输入字长 `WS`，**LSB Position** 和 **MSB Position** 必须满足以下约束：

`WS > MSB Position >= LSB Position >= 0`
