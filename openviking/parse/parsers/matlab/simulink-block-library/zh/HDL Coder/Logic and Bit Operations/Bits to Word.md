---
type: simulink-block
title: 'Bits to Word'
family: 'logic-and-bit-operations'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'bitstoword'
documentation_source_path: 'ref/bitstoword.html'
language: zh-CN
chinese_source: worker-translation
---

# Bits to Word

## 端口

### 输入

### **In** — 输入信号 二值标量 | 二值向量

模块的输入信号，指定为二值标量或向量。可以指定包含最多 128 个元素的向量。

**示例：**
`[0 1 1 0 0 1 1 1]`

**数据类型：** `fixdt(0,1,0)`
### 输出

### **Out** — 输出信号 标量

*N* 位整数，其中 *N* 是输入向量的大小，以非负标量形式返回。例如，当指定 1×8 输入信号时，输出信号是数据类型为 `ufix8` 的无符号整数。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **输入位顺序** — 输入位顺序 `LSB first`（默认） | `MSB first`

输入位顺序，指定为 `'MSB first'` 或 `'LSB first'`。

- `'MSB first'` –– 输入信号的第一位是最高有效位 (MSB)。
- `'LSB first'` –– 输入信号的第一位是最低有效位 (LSB)。

#### 编程用法

|  |
| --- |
| **模块参数**：`bitOrder` |
| **类型**：character vector |
| **值**：`'LSB first'` | `'MSB first'` |
| **默认值**：`'LSB first'` |

### **位打包后，将生成的整数值视为** — 位打包后带符号整数值的标志 `Unsigned`（默认） | `Signed`

指定位打包后生成的整数值被视为有符号还是无符号。

#### 编程用法

|  |
| --- |
| **模块参数**：`signedOutputValues` |
| **类型**：character vector |
| **值**：`'Unsigned'` | `'Signed'` |
| **默认值**：`'Unsigned'` |

## 所属库

HDL Coder / Logic and Bit Operations

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了额外的配置选项，这些选项会影响 HDL 实现和综合逻辑。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，要在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |

**数据类型支持**

此模块支持以下数据类型用于 HDL 代码生成：

| 输入端口 | 维度 | Fixed-Point | Floating-Point | Built-in Integers | Bus | Boolean | Complex Signal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | 标量  向量 | `ufix1` | No | No | No | No | No |

**限制**

- 不支持矩阵输入。

## 版本历史

**在 R2023a 中引入**

## 描述

将位向量转换为整数

Bits to Word 模块将长度为 *N* 的输入位向量转换为 *N* 位整数。该模块的输出是一个字长为 *N* 的无符号整数。

该模块将输入向量的第一个元素视为输出的最低有效位 (LSB)，并将后续位按升序视为接下来的有效位。下图显示了位向量 `[1 0 1 1 0]` 到整数值 `13` 的转换。

位到整数转换
