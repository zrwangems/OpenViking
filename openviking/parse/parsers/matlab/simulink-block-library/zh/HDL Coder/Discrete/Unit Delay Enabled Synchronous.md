---
type: simulink-block
title: 'Unit Delay Enabled Synchronous'
family: 'hdlcoder'
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
```yaml
ports:
- name: u
  summary: 输入信号 Scalar | Vector | Matrix | Array | Bus
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point | enumerated | bus
- name: E
  summary: 使能信号 Scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: y
  summary: 输出信号 Scalar | Vector | Matrix | Array | Bus
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point | enumerated | bus
```

### 输入

### **u** — 输入信号 `Scalar` | `Vector` | `Matrix` | `Array` | `Bus`

Unit Delay Enabled Synchronous 模块接受下列数据类型的输入信号。有关详细信息，请参阅 Simulink 支持的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **E** — 使能信号 `Scalar`

Unit Delay Enabled Synchronous 模块接受下列数据类型的使能信号。有关详细信息，请参阅 Simulink 支持的数据类型。

当使能信号为 false 时，状态和输出信号保持先前的值。当 `E` 输入不为零时，使能信号为 true；当 `E` 输入为零时，使能信号为 false。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### 输出

### **y** — 输出信号 `Scalar` | `Vector` | `Matrix` | `Array` | `Bus`

输出数据类型与输入匹配。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: Initial condition
  summary: 仿真的初始输出 0.0（默认）| Scalar | Vector | Matrix | Array | Bus
  group: ''
  block_parameter: InitialCondition
  type: 字符向量
  values: '''0'' | ''[n]'' | ''[m n]'''
- name: Sample time
  summary: 采样之间的时间间隔 -1（默认）| Scalar | Vector
  group: ''
  block_parameter: SampleTime
  type: 字符向量
  values: '''-1'' | ''[n]'' | ''[m n]'''
```

### **Initial condition** — 仿真的初始输出 0.0（默认）| `Scalar` | `Vector` | `Matrix` | `Array` | `Bus`

**Initial condition** 可以采用标量输入，或使用与输入信号相同的数据类型。不能使用 `NaN` 或 `Inf` 作为 **Initial condition** 来运行仿真。

#### 编程使用

|  |
| --- |
| **模块参数：** `InitialCondition` |
| **类型：** 字符向量 |
| **值：** `'0'` | `'[n]'` | `'[m n]'` |
| **默认：** `'0'` |

### **Sample time** — 采样之间的时间间隔 -1（默认）| `Scalar` | `Vector`

**Sample time** 必须是指定周期的实数双精度标量，或指定周期和偏移量的长度为二的实数双精度向量。周期和偏移量必须为有限且非负，且偏移量小于周期。

#### 编程使用

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** 字符向量 |
| **值：** `'-1'` | `'[n]'` | `'[m n]'` |
| **默认：** `'-1'` |
## 所属库

HDL Coder / Discrete

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |
| **ResetType** | 抑制复位逻辑生成。默认值为 `default`，即生成复位逻辑。另请参阅 ResetType。 |

**复数数据支持**

此模块支持复数信号的代码生成。

**限制**

HDL 代码生成在 Enable 端口仅支持 boolean 数据类型。

## 版本历史

**在 R2017b 中引入**

## 描述

当外部使能信号为真时，将输入信号延迟一个采样周期

当外部使能信号为真时，单位延迟使能同步模块将输入信号 u 延迟一个采样周期。当使能信号为假时，状态和输出信号保持先前的值。当 E 不为零时，使能信号为真；当 E 为零时，使能信号为假。

单位延迟使能同步模块的实现由一个同步子系统组成，该子系统包含一个**延迟长度**为一的使能延迟模块和一个处于 `Synchronous` 模式的状态控制模块。当您在模型中使用此模块并安装了 HDL Coder™ 时，由于状态控制模块的 `Synchronous` 行为，您的模型将生成更简洁的 HDL 代码并使用更少的硬件资源。
