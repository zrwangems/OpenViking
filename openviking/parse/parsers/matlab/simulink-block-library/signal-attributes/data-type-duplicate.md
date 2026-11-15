---
type: simulink-block
title: 'Data Type Duplicate'
family: signal-attributes
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'datatypeduplicate'
---

# Data Type Duplicate

Force all inputs to same data type

## 中文

强制所有输入为相同数据类型

### 所属库

Simulink / Signal Attributes HDL Coder / Signal Attributes

### 描述

Data Type Duplicate 模块强制所有输入具有相同的数据类型。输入信号的其他属性，例如维度、复杂度和采样时间，都是独立的。

您可以使用 Data Type Duplicate 模块来检查模块之间数据类型的一致性。如果所有信号不具有相同的数据类型，则该模块返回错误消息。

Data Type Duplicate 模块的典型用法是，一个到该模块的信号控制所有其他模块的数据类型。其他模块设置为通过反向传播继承其数据类型。

该模块在用户创建的库中也很有用。这些库模块可以放置在任何模型中，并且所有库模块的数据类型都是根据模型中的用途进行配置的。要创建具有比复制更复杂的数据类型规则的库模块，请使用 Data Type Propagation 模块。

### 端口

#### 输入

#### **Port\_1** — 第一个输入信号 标量 | 向量 | 矩阵 | N 维数组

第一个输入信号，指定为标量、向量、矩阵或 ND 数组。如果所有信号不具有相同的数据类型，则该模块返回错误消息。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `string` | `Boolean` | `fixed point` | `enumerated`

#### **Port\_N** — 第 N 个输入信号 标量 | 向量 | 矩阵 | N 维数组

第 N 个输入信号，指定为标量、向量、矩阵或 ND 数组。如果所有信号不具有相同的数据类型，则该模块返回错误消息。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `string` | `Boolean` | `fixed point` | `enumerated`

### 参数

#### **输入端口数目** — 模块输入的数目 `2` (默认) | 实值正整数

将此模块的输入数指定为实值正整数。

##### 编程用法

|  |
| --- |
| **模块参数**：`NumInputPorts` |
| **类型：**字符向量 |
| **值:** 实值正整数 |
| **默认值：**`'2'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

该模块可用于强制输入在生成代码的子系统中具有相同的数据类型，但不包含在硬件实现中。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Signal Attributes HDL Coder / Signal Attributes

## Description

The Data Type Duplicate block forces all inputs to have the same data type.
Other attributes of input signals, such as dimension, complexity, and sample time, are
independent.

You can use the Data Type Duplicate block to check for consistency of data
types among blocks. If all signals do not have the same data type, the block returns an
error message.

The Data Type Duplicate block is typically used such that one signal to the
block controls the data type for all other blocks. The other blocks are set to inherit
their data types via backpropagation.

The block can also be useful in a user created library. These library blocks can be placed
in any model, and the data type for all library blocks are configured according to the
usage in the model. To create a library block with more complex data type rules than
duplication, use the Data Type Propagation block.

## Ports

### Input

### **Port\_1** — First input signal scalar | vector | matrix | N-D array

First input signal, specified as a scalar, vector, matrix, or N-D array. If all signals
do not have the same data type, the block returns an error
message.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `string` | `Boolean` | `fixed point` | `enumerated`

### **Port\_N** — Nth input signal scalar | vector | matrix | N-D array

Nth input signal, specified as a scalar, vector, matrix, or N-D array. If all signals do
not have the same data type, the block returns an error message.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `string` | `Boolean` | `fixed point` | `enumerated`

## Parameters

### **Number of input ports** — Number of block inputs `2` (default) | real-valued positive integer

Specify the number of inputs to this block as a real-valued positive
integer.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumInputPorts` |
| **Type:** character vector |
| **Values:** real-valued positive integer |
| **Default:** `'2'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block can be used to force inputs to have same data
type in subsystems that generate code, but is not included in the hardware
implementation.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
