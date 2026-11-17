---
type: simulink-block
title: 'Tapped Delay Enabled Synchronous'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'tappeddelayenabledsynchronous'
documentation_source_path: 'ref/tappeddelayenabledsynchronous.html'
language: zh-CN
chinese_source: worker-translation
---

# Tapped Delay Enabled Synchronous

## 端口
```yaml
ports:
- name: u
  summary: 输入信号 标量
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: E
  summary: 使能信号 Scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: y
  summary: 输入信号的延迟版本 标量 | 向量
  direction: output
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### 输入

### **u** — 输入信号 标量

要延迟的输入信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** 是

### **E** — 使能信号 `Scalar`

该模块接受下列数据类型的使能信号。有关更多信息，请参阅 Data Types Supported by Simulink。

当使能信号为 false 时，状态和输出信号保持先前的值。当 `E` 输入不为零时，使能信号为 true；当 `E` 输入为零时，使能信号为 false。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### 输出

### **y** — 输入信号的延迟版本 标量 | 向量

延迟输入信号的所有版本。使用 **Order output vector starting with** 参数指定输出向量中延迟信号的顺序。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Initial condition
  summary: 初始输出 0.0（默认）| 标量
  group: ''
  block_parameter: vinit
  type: character vector
  values: scalar
  default: '''0.0'''
- name: Sample time
  summary: 采样之间的时间 -1（默认）| 标量 | 向量
  group: ''
  block_parameter: samptime
  type: character vector
  values: scalar | vector
  default: '''-1'''
- name: Number of delays
  summary: 离散时间算子数量 4（默认）| 正标量 | -1（用于继承）
  group: ''
  block_parameter: NumDelays
  type: character vector
  values: positive scalar | -1 (inherited)
  default: '''4'''
- name: Order output vector starting with
  summary: 输出顺序 Oldest（默认）| Newest
  group: ''
  block_parameter: DelayOrder
  type: character vector
  values: '''Oldest'' | ''Newest'''
  default: '''Oldest'''
- name: Include current input in output vector
  summary: 在输出向量中包含当前输入 off（默认）| on
  group: ''
  block_parameter: includeCurrent
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
```

### **Initial condition** — 初始输出 `0.0`（默认）| 标量

指定仿真的初始输出。**Initial condition** 参数在离线状态下使用舍入到最接近值和饱和，从 double 转换为输入数据类型。

#### 限制

该模块的初始条件不能为 `inf` 或 `NaN`。

#### 编程使用

|  |
| --- |
| **模块参数**：`vinit` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'0.0'` |

### **Sample time** — 采样之间的时间 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关更多信息，请参阅 Specify Sample Time。

#### 编程使用

|  |
| --- |
| **模块参数**：`samptime` |
| **类型**：character vector |
| **值**：scalar | vector |
| **默认值**：`'-1'` |

### **Number of delays** — 离散时间算子数量 `4`（默认）| 正标量 | `-1`（用于继承）

将离散时间算子数量指定为正标量，或指定为 `-1` 以继承。

值 `-1` 指示该模块通过反向传播继承延迟数量。每个延迟等效于 z-1 离散时间算子，该算子由 Unit Delay 模块表示。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumDelays` |
| **类型**：character vector |
| **值**：positive scalar | `-1` (inherited) |
| **默认值**：`'4'` |

### **Order output vector starting with** — 输出顺序 `Oldest`（默认）| `Newest`

指定是先输出最旧的延迟版本，还是先输出最新的延迟版本。

#### 编程使用

|  |
| --- |
| **模块参数**：`DelayOrder` |
| **类型**：character vector |
| **值**：`'Oldest' | 'Newest'` |
| **默认值**：`'Oldest'` |

### **Include current input in output vector** — 在输出向量中包含当前输入 `off`（默认）| `on`

选中此复选框以在输出向量中包含当前输入。

#### 编程使用

|  |
| --- |
| **模块参数**：`includeCurrent` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |
## 所属库

HDL Coder / Discrete

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |
| **ResetType** | 抑制复位逻辑生成。默认值为 `default`，即生成复位逻辑。另请参阅 ResetType。 |

**复数数据支持**

此模块支持复数信号的代码生成。

## 版本历史

**在 R2023a 中引入**

## 描述

当外部使能信号为真时，将标量信号延迟多个采样周期并输出所有延迟版本

Tapped Delay Enabled Synchronous 模块将输入延迟指定的采样周期数。当外部使能信号 **E** 为真时，该模块返回每个延迟的输出信号。

例如，当您将 **Number of delays** 指定为 `4`，并将 **Order output starting with** 指定为 `Oldest` 时，该模块返回四个信号，第一个延迟四个采样周期，第二个延迟三个，依此类推。使用此模块可以在时域中离散化信号或对信号进行重采样。

**输出向量顺序**

该模块接受一个标量输入，并生成一个包含每个增量延迟数据的输出向量。使用 **Order output vector starting with** 参数指定输出向量中延迟信号的顺序：

- `Oldest` 将输出向量从最旧的延迟版本开始排序，以最新的延迟版本结束。
- `Newest` 将输出向量从最新的延迟版本开始排序，以最旧的延迟版本结束。

使用 **Initial condition** 参数指定第一个采样周期的输出向量。仔细选择此参数可以减轻不需要的输出行为。

**同步状态控制**

该模块使用同步状态控制语义。当您在模型中使用此模块并通过 HDL Coder™ 生成 HDL 代码时，由于该模块的 `Synchronous` 行为，您的模型将生成更简洁的 HDL 代码并使用更少的硬件资源。
