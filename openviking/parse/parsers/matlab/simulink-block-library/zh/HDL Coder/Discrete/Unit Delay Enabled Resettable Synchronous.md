---
type: simulink-block
title: 'Unit Delay Enabled Resettable Synchronous'
family: 'discrete'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'unitdelayenabledresettablesynchronous'
documentation_source_path: 'ref/unitdelayenabledresettablesynchronous.html'
language: zh-CN
chinese_source: worker-translation
---

# Unit Delay Enabled Resettable Synchronous

## 端口

### 输入

### **u** — 输入信号 `Scalar` | `Vector` | `Matrix` | `Array` | `Bus`

Unit Delay Enabled Resettable Synchronous 模块接受下列数据类型的输入信号。有关更多信息，请参阅 Simulink 支持的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **E** — Enable 信号 `Scalar`

Unit Delay Enabled Synchronous 模块接受下列数据类型的 Enable 信号。有关更多信息，请参阅 Simulink 支持的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **R** — Reset 信号 `Scalar`

Unit Delay Resettable Synchronous 模块接受下列数据类型的 Reset 信号。有关更多信息，请参阅 Simulink 支持的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### 输出

### **y** — 输出信号 `Scalar` | `Vector` | `Matrix` | `Array` | `Bus`

输出数据类型与输入匹配。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **初始条件** — 仿真的初始输出 0.0（默认） | `Scalar` | `Vector` | `Matrix` | `Array` | `Bus`

**初始条件** 可以接受标量输入，或使用与输入信号相同的数据类型。不能使用 `NaN` 或 `Inf` 作为 **初始条件** 运行仿真。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialCondition` |
| **类型：** 字符向量 |
| **值：** `'0'` | `'[n]'` | `'[m n]'` |
| **默认值：** `'0'` |

### **采样时间** — 采样之间的时间间隔 -1（默认） | `Scalar` | `Vector`

**采样时间** 必须是指定周期的实 double 标量，或指定周期和偏移量的长度为 2 的实 double 向量。周期和偏移量必须为有限且非负，且偏移量小于周期。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** 字符向量 |
| **值：** `'-1'` | `'[n]'` | `'[m n]'` |
| **默认值：** `'-1'` |

## 所属库

HDL Coder / Discrete

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **InputPipeline** | 要在生成代码中插入的输入流水线阶段数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线阶段数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |
| **ResetType** | 抑制复位逻辑生成。默认值为 `default`，它会生成复位逻辑。另请参阅 ResetType。 |

**复数数据支持**

此模块支持复数信号的代码生成。

**限制**

HDL 代码生成在 Reset 和 Enable 端口仅支持 boolean 数据类型。

## 版本历史

**在 R2017b 中引入**

## 描述

当外部 Enable 信号为 true 且外部 Reset 信号为 false 时，将输入信号延迟一个采样周期

Unit Delay Enabled Resettable Synchronous 模块结合了 Unit Delay Enabled Synchronous 模块和 Unit Delay Resettable Synchronous 模块的功能。

当外部 Enable 信号为 true 且外部 Reset 信号为 false 时，Unit Delay Enabled Resettable Synchronous 模块将输入信号 u 延迟一个采样周期。当 Enable 信号为 false 时，状态和输出信号保持先前的值。当 Reset 信号为 true 时，状态和输出信号在一个采样周期后取 **初始条件** 参数的值。当 E 和 R 非零时，Enable 和 Reset 信号为 true；当 E 和 R 等于零时，为 false。

Unit Delay Enabled Synchronous 模块的实现由一个 Synchronous Subsystem 组成，该子系统包含一个 **延迟长度** 为 1 的 Enabled Delay 模块，以及一个处于 `Synchronous` 模式的 State Control 模块。当你在模型中使用此模块并安装了 HDL Coder™ 时，由于 State Control 模块的 `Synchronous` 行为，你的模型会生成更简洁的 HDL 代码并使用更少的硬件资源。
