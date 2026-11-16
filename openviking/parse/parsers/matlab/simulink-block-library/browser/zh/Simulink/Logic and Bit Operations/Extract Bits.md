---
type: simulink-block
title: 'Extract Bits'
family: logic-and-bit-operations
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'extractbits'
language: zh-CN
chinese_source: official
---

# Extract Bits

输出从输入信号选择的连续位

## 所属库

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## 描述

Extract Bits 模块允许您从输入信号的存储整数值中输出选择的连续位。使用**提取位**参数定义选择输出位的方法。

- 选择 `Upper half` 输出一半的输入位，其中包含最高有效位。如果输入信号中有奇数数量的位，则按以下方程计算输出位数

  ```
  number of output bits = ceil(number of input bits/2)
  ```
- 选择 `Lower half` 输出一半的输入位，其中包含最低有效位。如果输入信号中有奇数数量的位，则按以下方程计算输出位数

  ```
  number of output bits = ceil(number of input bits/2)
  ```
- 选择 `Range starting with most significant bit` 以输出一定数量的输入信号最高有效位。在**位数**参数中指定要输出的最高有效位数。
- 选择 `Range ending with least significant bit` 以输出一定数量的输入信号最低有效位。在**位数**参数中指定要输出的最低有效位数。
- 选择 `Range of bits` 以在**位索引**参数中指定要输出的输入信号的一系列连续位。您需要以 `[start end]` 格式指明范围，而输入位的索引将从 0（最低有效位）开始连续标记。

仿真期间，此模块不会报告溢出绕回警告。要报告这些警告，请参阅 `Simulink.restoreDiagnostic` 参考页。但此模块会报告由于溢出绕回而导致的错误。

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

输入信号，指定为标量、向量、矩阵或 N 维数组。浮点输入通过模块时保持不变。`boolean` 输入被视为 `uint8` 信号。

**注意**

对有符号整数执行位运算非常困难。要解决这个难题，您可以将输入的数据类型转换为无符号整数类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 提取位 标量 | 向量 | 矩阵 | N 维数组

提取的连续选择的位，指定为标量、向量、矩阵或 N 维数组。浮点输入通过模块时保持不变。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **提取位** — 提取位的方法 **上半部** (默认) | **下半部** | **以最高有效位开始的范围** | **以最低有效位结束的范围** | **位范围**

选择用于从输入信号中提取位的方法。

假定有一个输入信号以二进制格式表示为 `110111001`：

- 如果您为**提取位**参数选择 `Upper half`，则输出为二进制 `11011`。
- 如果您为**提取位**参数选择 `Lower half`，则输出为二进制 `11001`。
- 如果您为**提取位**参数选择 `Range starting with most significant bit`，并为**位数**参数指定 `3`，则输出为二进制 `110`。
- 如果您为**提取位**参数选择 `Range ending with least significant bit`，并为**位数**参数指定 `8`，则输出为二进制 `10111001`。
- 如果您为**提取位**参数选择 `Range of bits`，并为**位索引**参数指定 `[4 7]`，则输出为二进制 `1011`。

#### 编程用法

|  |
| --- |
| **模块参数**：`bitsToExtract` |
| **类型：**字符向量 |
| **值：**`'Upper half' | 'Lower half' | 'Range starting with most significant bit' | 'Range ending with least significant bit' | 'Range of bits'` |
| **默认值：**`'Upper half'` |

### **位数** — 要输出的位数 `8` (默认) | 正整数标量

将输入信号输出的位数指定为正整数标量。

#### 依赖关系

要启用此参数，请将**提取位**设置为 `Range starting with most significant bit` 或 `Range ending with least significant bit`。

#### 编程用法

|  |
| --- |
| **模块参数**：`numBits` |
| **类型：**字符向量 |
| **值：**正整数标量 |
| **默认值：**`'8'` |

### **位索引** — 要输出的位数的连续范围 [0 7] (默认) | 二元素向量 | 正整数标量

将要输出的输入信号位的二元素向量指定为正整数标量。以 `[start end]` 格式指定范围。

#### 依赖关系

要启用此参数，请将**提取位**设置为 `Range of bits`。

#### 编程用法

|  |
| --- |
| **模块参数**：`bitIdxRange` |
| **类型：**字符向量 |
| **值：**二元素向量 | 正整数标量 |
| **默认值：**`'[0 7]'` |

### **输出定标模式** — 输出定标模式 **保留定点定标** (默认) | **将位域视为整数**

选择要对输出位选项使用的定标模式：

- 如果您选择 `Preserve fixed-point scaling`，则在数据类型转换过程中，将使用输入的定点定标来确定输出缩放。
- 如果您选择 `Treat bit field as an integer`，将忽略输入的定点定标，只使用存储的整数来计算输出数据类型。

#### 编程用法

|  |
| --- |
| **模块参数**：`outScalingMode` |
| **类型：**字符向量 |
| **值：**`'Preserve fixed-point scaling' | 'Treat bit field as an integer'` |
| **默认值：**`'Preserve fixed-point scaling'` |

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史记录

**在 R2006a 之前推出**
