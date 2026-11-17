---
type: simulink-block
title: 'Unit Delay Enabled Synchronous'
family: 'discrete'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'unitdelayenabledsynchronous'
documentation_source_path: 'ref/unitdelayenabledsynchronous.html'
language: zh-CN
chinese_source: worker-translation
---

# Unit Delay Enabled Synchronous

## 端口

### 输入

### **u** — 输入信号 `Scalar` | `Vector` | `Matrix` | `Array` | `Bus`

Unit Delay Enabled Synchronous 模块接受
以下所列数据类型的输入信号。有关详细信息，请参阅
Simulink 支持的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **E** — 使能信号 `Scalar`

Unit Delay Enabled Synchronous 模块接受
以下所列数据类型的使能信号。有关详细信息，请参阅
Simulink 支持的数据类型。

当使能信号为 false 时，状态和输出信号保持
上一个值。当 `E`
输入不为零时，使能信号为 true；当 `E` 输入为
零时，使能信号为 false。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### 输出

### **y** — 输出信号 `Scalar` | `Vector` | `Matrix` | `Array` | `Bus`

输出数据类型与输入匹配。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **初始条件** — 仿真的初始输出 0.0 (默认) | `Scalar` | `Vector` | `Matrix` | `Array` | `Bus`

**初始条件** 可以接受标量输入，也可以
使用与输入信号相同的数据类型。不能使用
`NaN` 或 `Inf` 作为
**初始条件** 运行仿真。

#### 编程用法

|  |
| --- |
| **模块参数：** `InitialCondition` |
| **类型：** character vector |
| **值：** `'0'` | `'[n]'` | `'[m n]'` |
| **默认：** `'0'` |

### **采样时间** — 采样之间的时间间隔 -1 (默认) | `Scalar` | `Vector`

**采样时间** 必须是指定周期的实数 double 标量，或指定
周期和偏移量的长度为二的实数 double 向量。周期和偏移量必须为有限且非负，
并且偏移量小于周期。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** character vector |
| **值：** `'-1'` | `'[n]'` | `'[m n]'` |
| **默认：** `'-1'` |

## 所属库

HDL Coder / Discrete

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder 提供影响 HDL 实现和综合逻辑的其他配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **InputPipeline** | 要插入到生成代码中的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 要插入到生成代码中的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline。 |
| **ResetType** | 禁止生成复位逻辑。默认值为 `default`，它会生成复位逻辑。另请参阅 ResetType。 |

**复数数据支持**

此模块支持针对复数信号的代码生成。

**限制**

HDL 代码生成在使能端口仅支持 boolean 数据类型。

## 版本历史

**在 R2017b 中引入**

## 描述

当外部使能信号为 true 时，将输入信号延迟一个采样周期

当外部使能信号为 true 时，Unit Delay Enabled Synchronous 模块将输入信号 u 延迟一个采样周期。当使能信号为 false 时，状态和输出信号保持上一个值。当 E 不为零时，使能信号为 true；当 E 为零时，使能信号为 false。

Unit Delay Enabled Synchronous 模块实现由一个
Synchronous Subsystem 组成，其中包含一个 **延迟长度** 为 1 的 Enabled Delay
模块，以及一个处于 `Synchronous` 模式的 State Control
模块。在模型中使用此模块并且安装了 HDL Coder™ 时，由于 State Control 模块的 `Synchronous` 行为，模型会生成更简洁的 HDL 代码并使用更少的硬件资源。
