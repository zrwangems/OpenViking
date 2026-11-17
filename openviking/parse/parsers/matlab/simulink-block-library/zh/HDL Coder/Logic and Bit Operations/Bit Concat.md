---
type: simulink-block
title: 'Bit Concat'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'bitconcat'
documentation_source_path: 'ref/bitconcat.html'
language: zh-CN
chinese_source: worker-translation
---

# Bit Concat

## 端口
```yaml
ports:
- name: H
  summary: 最高位输入字 标量 | 向量
  direction: input
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: L
  summary: 最低位输入字 标量 | 向量
  direction: input
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Output
  summary: 拼接后的字 标量 | 向量
  direction: output
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **H** — 最高位输入字 标量 | 向量

模块要拼接的最高位输入字，它将成为拼接后输出信号中最左侧的值。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **L** — 最低位输入字 标量 | 向量

模块要拼接的最低位输入字，它将成为拼接后输出信号中最右侧的值。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Output** — 拼接后的字 标量 | 向量

输出是按输入字从低到高顺序拼接后的字。拼接后的输出字最大大小为 65535 位。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: Number of Inputs
  summary: 输入信号的数量 2（默认）| 小于或等于 128 的正整数值
  group: ''
  block_parameter: numInputs
  type: string scalar | character vector
  values: A positive integer value less than or equal to 128
  default: '''2'''
```

### **Number of Inputs** — 输入信号的数量 2（默认）| 小于或等于 128 的正整数值

输入一个整数，指定输入信号的数量。更改 **Number of Inputs** 时，模块输入端口数量会更新。

- 默认：2
- 最小值：1
- 最大值：128

**注意**

请确保 **Number of Inputs** 等于连接到模块的信号数量。如果模块有未连接的输入，代码生成期间会发生错误。

#### 编程使用

|  |
| --- |
| **模块参数：** `numInputs` |
| **类型**：string scalar | character vector |
| **Value:** A positive integer value less than or equal to 128 |
| **默认值**：`'2'` |
## 所属库

HDL Coder / Logic and Bit Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |

## 版本历史

**在 R2014a 中引入**

### R2024b：最大输出字大小为 65535 位

拼接后的输出字最大大小为 65535 位。在 R2024b 之前，最大字大小为 128 位。

## 描述

将最多 128 个输入字拼接为单个输出

Bit Concat 模块将最多 128 个输入字拼接为单个输出。标记为 `L` 的输入端口指定最低位输入字。标记为 `H` 的输入端口指定最高位输入字。对于标量输入，应将两个或更多输入信号连接到模块。对于向量输入，至少应将一个输入连接到模块。该模块使用 `bitconcat` 函数，使得输出中字从右到左的顺序遵循输入信号从低到高的顺序。要了解该模块如何工作，请参阅 Algorithms。
