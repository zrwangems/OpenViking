---
type: simulink-block
title: 'Bit Reduce'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'bitreduce'
documentation_source_path: 'ref/bitreduce.html'
language: zh-CN
chinese_source: worker-translation
---

# Bit Reduce

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

执行位缩减操作的输入信号。

- 最小位宽：2
- 最大位宽：128

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

经过位缩减后的输出信号。

**数据类型：** `ufix1`

## 参数

### **Reduction Mode** — 对输入执行的缩减操作 `AND`（默认）| `OR` | `XOR`

指定缩减操作：

- `AND`（默认）：对输入信号执行按位 AND 缩减。
- `OR`：对输入信号执行按位 OR 缩减。
- `XOR`：对输入信号执行按位 XOR 缩减。

#### 编程使用

|  |
| --- |
| **模块参数：** `mode` |
| **类型**：string scalar | character vector |
| **Value:** `"AND"` | `"OR"` | `"XOR"` |
| **默认值**：`'AND'` |

## 所属库

HDL Coder / Logic and Bit Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |

## 版本历史

**在 R2014a 中引入**

## 描述

对输入信号的所有位执行 AND、OR 或 XOR 位缩减，得到单个位

Bit Reduce 模块对输入信号的所有位执行选定的位缩减操作（AND、OR 或 XOR），得到单个位结果。
