---
type: simulink-block
title: 'Zero-Order Hold'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'zeroorderhold'
documentation_source_path: 'slref/zeroorderhold.html'
language: zh-CN
chinese_source: worker-translation
---

# Zero-Order Hold

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
- name: Port_1
  summary: 输出信号 标量 | 向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量

模块保持一个采样周期的输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

输出信号为输入保持一个采样周期后的信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: Sample time (-1 for inherited)
  summary: 采样时间命中之间的离散间隔 -1（默认）| scalar
  group: ''
  block_parameter: SampleTime
  values: -1 (default) | positive scalar number
```

### **Sample time (-1 for inherited)** — 采样时间命中之间的离散间隔 `-1`（默认）| `scalar`

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关更多信息，请参阅 Specify Sample Time。

不要指定连续采样时间（`0` 或 `[0,0]`）。此模块仅支持离散采样时间。当此参数为 `-1` 时，继承的采样时间必须是离散的，不能是连续的。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **值**：| `-1` (default) | positive scalar number |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/Zero-Order
Hold","SampleTime","0.1")` specifies a discrete sample
`0.1` 的时间用于零阶
Hold block named `Zero-Order Hold` in
名为 `mdl` 的模型。
## 所属库

Simulink / Discrete HDL Coder / Discrete

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`strong.h`）。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

实现零阶保持采样周期

Zero-Order Hold 模块在其指定的采样周期内保持其输入。如果输入是向量，则该模块在相同的采样周期内保持向量的所有元素。

您可以通过 **Sample time** 参数指定采样之间的时间。设置为 `-1` 表示该模块继承 **Sample time**。

**提示**

不要使用 Zero-Order Hold 模块在不同采样率下运行的模块之间创建快慢转换。请改用 Rate Transition 模块。

### 总线支持

Zero-Order Hold 模块是支持总线的模块。输入可以是虚拟或非虚拟总线信号。不存在特定于模块的限制。输入到 Zero-Order Hold 模块的非虚拟总线中的所有信号必须具有相同的采样时间，即使相关总线对象的元素指定了继承的采样时间。您可以使用 Rate Transition 模块来更改单个信号或总线中所有信号的采样时间。有关更多信息，请参阅 Modify Sample Times for Nonvirtual Buses and Bus-Capable Blocks。

您可以将总线数组用作 Zero-Order Hold 模块的输入信号。有关定义和使用总线数组的详细信息，请参阅 Group Nonvirtual Buses in Arrays of Buses。

### 与类似模块的比较

Memory、Unit Delay 和 Zero-Order Hold 模块提供类似的功能，但具有不同的能力。此外，每个模块的用途也不同。

下表显示了每个模块的建议用法。

| 模块 | 模块用途 | 参考示例 |
| --- | --- | --- |
| Unit Delay | 使用您指定的离散采样时间实现延迟。该模块接受并输出具有离散采样时间的信号。 | - Engine Timing Model with Closed Loop Control (Compression subsystem) |
| Memory | 通过一个主积分时间步实现延迟。理想情况下，该模块接受连续（或在次要时间步中固定）信号，并输出在次要时间步中固定的信号。 | - Building a Clutch Lock-Up Model (Friction Mode Logic/Lockup FSM subsystem) - Capture the Velocity of a Bouncing Ball with the Memory Block |
| Zero-Order Hold | 将具有连续采样时间的输入信号转换为具有离散采样时间的输出信号。 | - Developing the Apollo Lunar Module Digital Autopilot - Radar Tracking Using MATLAB Function Blocks |

每个模块具有以下能力。

| 能力 | Memory | Unit Delay | Zero-Order Hold |
| --- | --- | --- | --- |
| 初始条件指定 | 是 | 是 | 否，因为时间 t = 0 时的模块输出必须与输入值匹配。 |
| 采样时间指定 | 否，因为该模块只能从驱动模块或用于整个模型的求解器继承采样时间。 | 是 | 是 |
| 基于帧的信号支持 | 否 | 是 | 是 |
| 状态记录支持 | 否 | 是 | 否 |
