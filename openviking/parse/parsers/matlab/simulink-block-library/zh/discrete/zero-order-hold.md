---
type: simulink-block
title: 'Zero-Order Hold'
family: discrete
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'zeroorderhold'
language: zh-CN
chinese_source: official
---

# Zero-Order Hold

实现零阶保持采样周期

## 所属库

Simulink / Discrete HDL Coder / Discrete

## 描述

Zero-Order Hold 模块在您指定的采样周期内保持其输入不变。如果输入为向量，模块会按相同的采样周期保持向量中的所有元素。

可通过**采样时间**参数指定样本之间的时间间隔。设置为 `-1` 表示模块将继承**采样时间**。

**提示**

请勿使用 Zero-Order Hold 模块在以不同速率运行的模块之间创建快速到慢速转移。这种情况请改用 Rate Transition 模块。

### 总线支持

Zero-Order Hold 模块支持总线。输入可以是虚拟或非虚拟总线信号。没有特定于模块的限制条件。Zero-Order Hold 模块的非虚拟总线输入中的所有信号必须具有相同的采样时间，即使相关总线对象的元素指定了继承的采样时间也是如此。您可以使用 Rate Transition 模块更改总线中单个信号或所有信号的采样时间。有关详细信息，请参阅Modify Sample Times for Nonvirtual Buses和 Bus-Capable Blocks。

可使用总线数组作为 Zero-Order Hold 模块的输入信号。有关定义和使用总线数组的详细信息，请参阅使用总线数组组合非虚拟总线。

### 与类似模块的比较

Memory、Unit Delay 和 Zero-Order Hold 模块提供相似的功能，但各自具有不同的能力。此外，每个模块的用途也各不相同。

下表显示每个模块的推荐用途。

| 模块 | 模块的用途 | 引用示例 |
| --- | --- | --- |
| Unit Delay | 使用您指定的离散采样时间实现延迟。该模块接受并输出具有离散采样时间的信号。 | - 具有闭环控制的发动机定时模型（Compression 子系统） |
| Memory | 将信号延迟一个主积分时间步。在理想情况下，该模块接受连续（或在子时间步中固定）的信号并输出在子时间步中固定的信号。 | - Building a Clutch Lock-Up Model（Friction Mode Logic/Lockup FSM 子系统） - 使用 Memory 模块捕获弹球的速度 |
| Zero-Order Hold | 将具有连续采样时间的输入信号转换为具有离散采样时间的输出信号。 | - Developing the Apollo Lunar Module Digital Autopilot - 使用 MATLAB Function 模块的雷达跟踪 |

每个模块有以下功能。

| 功能 | 内存 | 单位延迟 | 零阶保持 |
| --- | --- | --- | --- |
| 指定初始条件 | 是 | 是 | 否，因为在时间 t = 0 的模块输出必须与输入值相匹配。 |
| 指定采样时间 | 否，因为该模块只能从驱动模块或用于整个模型的求解器继承采样时间。 | 是 | 是 |
| 支持基于帧的信号 | 否 | 是 | 是 |
| 支持状态记录 | 否 | 是 | 否 |

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

输入信号，模块会将其保持一个采样周期。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

输出信号，即保持了一个采样周期的输入。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **采样时间(-1 表示继承)** — 采样时间命中点之间的离散间隔 `-1` (默认) | `scalar`

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 指定采样时间。

不要指定连续采样时间（`0` 或 `[0,0]`）。此模块仅支持离散采样时间。当此参数为 `-1` 时，继承的采样时间必须是离散时间，不能是连续时间。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `-1` (默认) | positive scalar number |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("mdl/Zero-Order Hold","SampleTime","0.1")` specifies a discrete sample time of `0.1` for the Zero-Order Hold block named `Zero-Order Hold` in the model named `mdl`.

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

生成的代码在特定条件下依赖于 `memcpy` 或 `memset` 函数 (`strong.h`)。

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

**复数数据支持**

此模块支持复信号的代码生成。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史记录

**在 R2006a 之前推出**
