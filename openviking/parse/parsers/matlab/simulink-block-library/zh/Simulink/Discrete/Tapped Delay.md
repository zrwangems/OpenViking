---
type: simulink-block
title: 'Tapped Delay'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'tappeddelay'
documentation_source_path: 'slref/tappeddelay.html'
language: zh-CN
chinese_source: worker-translation
---

# Tapped Delay

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 输入信号的延迟版本 标量 | 向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### 输入

### **Port\_1** — 输入信号 标量

要延迟的输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** 是
### 输出

### **Port\_1** — 输入信号的延迟版本 标量 | 向量

延迟输入信号的所有版本。使用 **Order output vector starting with** 参数指定输出向量中延迟信号的顺序。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Initial condition
  summary: 初始输出 0.0（默认）| 标量
  group: ''
  block_parameter: vinit
  type: 字符向量
  values: 标量
  default: '''0.0'''
- name: Sample time
  summary: 采样之间的时间 -1（默认）| 标量 | 向量
  group: ''
  block_parameter: samptime
  type: 字符向量
  values: 标量 | 向量
  default: '''-1'''
- name: Number of delays
  summary: 离散时间算子数量 4（默认）| 正标量 | -1（用于继承）
  group: ''
  block_parameter: NumDelays
  type: 字符向量
  values: 正标量 | -1（继承）
  default: '''4'''
- name: Order output vector starting with
  summary: 输出顺序 Oldest（默认）| Newest
  group: ''
  block_parameter: DelayOrder
  type: 字符向量
  values: '''Oldest'' | ''Newest'''
  default: '''Oldest'''
- name: Include current input in output vector
  summary: 在输出向量中包含当前输入 off（默认）| on
  group: ''
  block_parameter: includeCurrent
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
```

### **Initial condition** — 初始输出 `0.0`（默认）| 标量

指定仿真的初始输出。**Initial condition** 参数在离线状态下使用舍入到最近值和饱和从 double 转换为输入数据类型。

#### 限制

此模块的初始条件不能为 `inf` 或 `NaN`。

#### 编程用法

|  |
| --- |
| **模块参数：** `vinit` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认值：** `'0.0'` |

### **Sample time** — 采样之间的时间 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 编程用法

|  |
| --- |
| **模块参数：** `samptime` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 |
| **默认值：** `'-1'` |

### **Number of delays** — 离散时间算子数量 `4`（默认）| 正标量 | `-1`（用于继承）

将离散时间算子数量指定为正标量，或指定为 `-1` 以继承。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumDelays` |
| **类型：** 字符向量 |
| **值：** 正标量 | `-1`（继承） |
| **默认值：** `'4'` |

### **Order output vector starting with** — 输出顺序 `Oldest`（默认）| `Newest`

指定是先输出最旧的延迟版本，还是先输出最新的延迟版本。

#### 编程用法

|  |
| --- |
| **模块参数：** `DelayOrder` |
| **类型：** 字符向量 |
| **值：** `'Oldest' | 'Newest'` |
| **默认值：** `'Oldest'` |

### **Include current input in output vector** — 在输出向量中包含当前输入 `off`（默认）| `on`

选中此复选框可在输出向量中包含当前输入。

#### 编程用法

|  |
| --- |
| **模块参数：** `includeCurrent` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |
## 所属库

Simulink / Discrete HDL Coder / Discrete

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ResetType** | 抑制复位逻辑生成。默认值为 `default`，即生成复位逻辑。另请参阅 ResetType (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

将标量信号延迟多个采样周期并输出所有延迟版本

Tapped Delay 模块将输入延迟指定的采样周期数，并为每个延迟提供一个输出信号。例如，当您为 **Number of delays** 指定 `4` 且 **Order output starting with** 为 `Oldest` 时，该模块提供四个输出——第一个延迟四个采样周期，第二个延迟三个，依此类推。使用此模块可以在时间上离散化信号或以不同速率对信号进行重采样。

该模块接受一个标量输入，并生成一个输出向量，其中包含每个增量延迟的数据。使用 **Order output vector starting with** 参数指定输出向量中延迟信号的顺序：

- `Oldest` 将输出向量从最旧的延迟版本开始排序，到最新的延迟版本结束。
- `Newest` 将输出向量从最新的延迟版本开始排序，到最旧的延迟版本结束。

使用 **Initial condition** 参数指定第一个采样周期的输出向量。仔细选择此参数可以减轻不需要的输出行为。

使用 **Sample time** 参数指定采样之间的时间。使用 **Number of delays** 参数指定延迟数量。值 `-1` 指示模块通过反向传播继承延迟数量。每个延迟等效于 z-1 离散时间算子，即 Unit Delay 模块所表示的算子。
