---
type: simulink-block
title: 'Word to Bits'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Code Generation from Simulink / Model and Architecture Design / Model Design / Basic HDL Algorithms / Logic and Bit Operations'
documentation_page: 'wordtobits'
documentation_source_path: 'ref/wordtobits.html'
language: zh-CN
chinese_source: worker-translation
---

# Word to Bits

## 端口

### 输入

### **In** — 输入信号标量

输入信号，指定为标量。字长必须小于或等于 **Maximum Word Length** 参数。

**示例：** `72`

**示例：** `5.5`

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Out** — 输出信号二值标量 | 二值向量

输出信号，返回为二值标量或向量。在 **Maximum Word Length** 参数中设置此向量的长度。该模块将输出向量的第一个元素视为 LSB，并将后续位按升序视为下一个有效位。

**数据类型：** `ufix1`

## 参数

### **Maximum Word Length** — 最大输出字长 `64`（默认）| [1, 65535] 范围内的整数

最大输出字长，指定为 [1, 65535] 范围内的整数。参数值必须大于或等于输入信号字长。

#### 程序化使用

|  |
| --- |
| **模块参数：** `maxWordLength` |
| **类型：** character vector |
| **值：** [1, 65535] 范围内的整数 |
| **默认：** `'64'` |

### **Output bit order** — 输出位顺序 `LSB first`（默认）| `MSB first`

定义输出信号的第一位是最高有效位（MSB）还是最低有效位（LSB）。

#### 程序化使用

|  |
| --- |
| **模块参数**：`bitOrder` |
| **类型**：character vector |
| **值**：`'LSB first'` | `'MSB first'` |
| **默认**：`'LSB first'` |

## 所属库

HDL Coder / Logic and Bit Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |

**数据类型支持**

此模块支持以下用于 HDL 代码生成的数据类型：

| 输入端口 | 维度 | Fixed-Point | Floating-Point | Built-in Integers | Bus | Boolean | Complex Signal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | 标量 | Yes | No | Yes | No | No | No |

**限制**

- 不支持矩阵输入。

## 版本历史

**在 R2023a 中引入**

### R2024b：最大字长为 65535 bits

**Maximum Word Length** 模块参数支持最大字长为 65535 bits。在 R2024b 之前，最大字长为 128 bits。

## 描述

将实数转换为位向量

Word to Bits 模块将字长为 *N* 的实数转换为位向量。该模块的输出是一个向量，其长度在 **Maximum Word Length** 参数中指定。

该模块将输出向量的第一个元素视为最低有效位（LSB），并将后续位按升序视为下一个有效位。

此图显示当指定最大字长为 8 时，将无符号整数 72 转换为其二进制表示。也可以将有符号整数值转换为其对应的二进制向量。

Word to Bits 转换

此图显示将非整数值 5.5 转换为其二进制表示。输出是 5.5 的存储整数值的二进制表示。要确定定点实数的存储整数值，请使用 `storedInteger` 函数。

将实数转换为位向量
