---
type: simulink-block
title: 'Tapped Delay Resettable Synchronous'
family: 'discrete'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'tappeddelayresettablesynchronous'
documentation_source_path: 'ref/tappeddelayresettablesynchronous.html'
language: zh-CN
chinese_source: worker-translation
---

# Tapped Delay Resettable Synchronous

## 端口

### 输入

### **u** — 输入信号 标量

要延迟的输入信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** 是

### **R** — 复位信号 `Scalar`

该模块接受下列数据类型的 Reset 信号。有关详细信息，请参阅 Data Types Supported by Simulink。

当 Reset 信号为 true 时，状态和输出信号采用 **初始条件** 参数的值。当 R 不为零时，Reset 信号为 true；当 R 为零时，Reset 信号为 false。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### 输出

### **y** — 输入信号的延迟版本 标量 | 向量

延迟输入信号的所有版本。使用 **输出向量排序起始于** 参数指定输出向量中延迟信号的顺序。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### **初始条件** — 初始输出 `0.0`（默认）| 标量

指定仿真的初始输出。**初始条件** 参数会在离线状态下使用舍入到最接近值和饱和从 double 转换为输入数据类型。

#### 限制

此模块的初始条件不能为 `inf` 或 `NaN`。

#### 编程用法

|  |
| --- |
| **模块参数：** `vinit` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认值：** `'0.0'` |

### **采样时间** — 采样之间的时间 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 编程用法

|  |
| --- |
| **模块参数：** `samptime` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 |
| **默认值：** `'-1'` |

### **延迟数** — 离散时间算子数 `4`（默认）| 正标量 | `-1`（用于继承）

将离散时间算子数指定为正标量，或指定为 `-1` 表示继承。

值 `-1` 指示模块通过反向传播继承延迟数。每个延迟相当于 z-1 离散时间算子，该算子由 Unit Delay 模块表示。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumDelays` |
| **类型：** 字符向量 |
| **值：** 正标量 | `-1`（继承） |
| **默认值：** `'4'` |

### **输出向量排序起始于** — 输出顺序 `Oldest`（默认）| `Newest`

指定先输出最旧的延迟版本，还是先输出最新的延迟版本。

#### 编程用法

|  |
| --- |
| **模块参数：** `DelayOrder` |
| **类型：** 字符向量 |
| **值：** `'Oldest' | 'Newest'` |
| **默认值：** `'Oldest'` |

### **在输出向量中包含当前输入** — 在输出向量中包含当前输入 `off`（默认）| `on`

选中此复选框可在输出向量中包含当前输入。

#### 编程用法

|  |
| --- |
| **模块参数：** `includeCurrent` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

## 所属库

HDL Coder / Discrete

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline。 |
| **ResetType** | 抑制复位逻辑生成。默认值为 `default`，这会生成复位逻辑。另请参阅 ResetType。 |

**复数数据支持**

此模块支持复数信号的代码生成。

## 版本历史

**在 R2023a 中引入**

## 描述

当外部 Reset 信号为 false 时，将标量信号延迟多个采样周期并输出所有延迟版本

Tapped Delay Enabled Synchronous 模块将输入延迟指定的采样周期数。当外部 Reset 信号 **R** 为 false 时，该模块为每个延迟返回一个输出信号。

例如，当您将 **延迟数** 指定为 `4`，并将 **输出向量排序起始于** 指定为 `Oldest` 时，该模块返回四个信号：第一个延迟四个采样周期，第二个延迟三个采样周期，依此类推。使用此模块可在时域中离散化信号或对信号进行重采样。

**输出向量顺序**

该模块接受一个标量输入，并生成一个输出向量，其中包含每个增量延迟的数据。使用 **输出向量排序起始于** 参数指定输出向量中延迟信号的顺序：

- `Oldest` 使输出向量从最旧的延迟版本开始，到最新的延迟版本结束。
- `Newest` 使输出向量从最新的延迟版本开始，到最旧的延迟版本结束。

使用 **初始条件** 参数指定第一个采样周期的输出向量。谨慎选择此参数可以减轻不需要的输出行为。

**同步状态控制**

该模块使用同步状态控制语义。当您在模型中使用此模块，并使用 HDL Coder™ 生成 HDL 代码时，由于模块的 `Synchronous` 行为，您的模型会生成更简洁的 HDL 代码并使用更少的硬件资源。
