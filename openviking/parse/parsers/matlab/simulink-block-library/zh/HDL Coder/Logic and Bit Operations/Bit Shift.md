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
chinese_source: worker-translation
---

# Bit Shift

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

进行逻辑移位或算术移位的输入信号。

- 最小位宽：2
- 最大位宽：128

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

经过逻辑移位或算术移位的输出信号。输出信号具有与输入信号相同的数据类型和位宽。

- 最小位宽：2
- 最大位宽：65535

## 参数

### **Shift Mode** — 移位的类型和方向 `Shift Left Logical`（默认）| `Shift Right Logical` | `Shift Right Arithmetic`

指定移位的类型和方向。

#### 编程使用

|  |
| --- |
| **模块参数：** `mode` |
| **类型**：string scalar | character vector |
| **Value:** `"Shift Left Logical"` | `"Shift Right Logical"` | `"Shift Right Arithmetic"` |
| **默认值**：`'Shift Left Logical'` |

### **Shift Length** — 要移位的位数 `0`（默认）

指定要移位的位数。指定一个大于或等于零的值。

#### 编程使用

|  |
| --- |
| **模块参数：** `N` |
| **类型**：string scalar | character vector |
| **Value:** A value greater than or equal to zero |
| **默认值**：`'0'` |

## 所属库

HDL Coder / Logic and Bit Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供额外的配置选项，这些选项会影响 HDL 实现和综合逻辑。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |

## 版本历史

**在 R2014a 中引入**

### R2024b：最大位宽为 65535 位

输出信号的最大位宽为 65535 位。在 R2024b 之前，最大位宽为 128 位。

## 描述

输入信号的逻辑移位或算术移位

Bit Shift 模块对输入信号执行逻辑移位或算术移位。

此模块在仿真和 HDL 代码生成行为方面与 Shift Arithmetic 模块不同。Bit Shift 模块可以对有符号数执行逻辑移位，而无需执行 `reinterpretcast` 操作。此模块使用基于 MATLAB Function 模块的实现，操作速度可能较慢。

Shift Arithmetic 模块移位输入数字的位或二进制小数点。与 Bit Shift 模块相比，此模块具有额外的 HDL 代码生成模块选项。当您想要执行可变移位操作时，请使用 Shift Arithmetic 模块而不是 Bit Shift 模块。如果输入为有符号数，该模块会对此数执行符号扩展。Shift Arithmetic 模块需要使用额外的 Data Type Conversion 模块，并选择 `Stored Integer (SI)` 选项。
