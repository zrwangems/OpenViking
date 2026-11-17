---
type: simulink-block
title: 'Unit Delay'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'unitdelay'
documentation_source_path: 'slref/unitdelay.html'
language: zh-CN
chinese_source: worker-translation
---

# Unit Delay

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | string | Boolean
    | fixed point | enumerated | bus | image
- name: Port_1
  summary: 输出信号 标量 | 向量
  direction: output
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | string | Boolean
    | fixed point | enumerated | bus | image
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量

模块延迟一个采样周期的输入信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

延迟一个采样周期的输入信号作为输出信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
## 参数
```yaml
parameters:
- name: 初始条件
  summary: 第一个采样周期的输出 0（默认）| 标量 | 向量
  group: 主要
  block_parameter: InitialCondition
  type: 字符向量
  values: 标量 | 向量
  default: '''0'''
- name: 输入处理
  summary: 指定基于采样或基于帧的处理 Elements as channels (sample based)（默认）| Columns as channels (frame based)
  group: 主要
  block_parameter: InputProcessing
  type: 字符向量
  values: '''Columns as channels (frame based)'' | ''Elements as channels (sample based)'''
  default: '''Elements as channels (sample based)'''
- name: 采样时间（-1 表示继承）
  summary: 采样时间命中之间的离散间隔 -1（默认）| 1×2 向量
  group: 主要
  block_parameter: SampleTime
  type: 字符向量
  values: 实数标量 | 1×2 向量
  default: '''-1'''
- name: 状态名称
  summary: 模块状态的唯一名称 ''（默认）| 字母数字字符串
  group: 状态属性
  block_parameter: StateName
  type: 字符向量
  values: 唯一名称
  default: ''''''
- name: 状态名称必须解析为 Simulink 信号对象
  summary: 要求状态名称解析为信号对象的选项 off（默认）| on
  group: 状态属性
  block_parameter: StateMustResolveToSignalObject
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
```

### 主要

### **初始条件** — 第一个采样周期的输出 `0`（默认）| 标量 | 向量

指定第一个采样周期的仿真输出，在此期间 Unit Delay 模块的输出在其他情况下是未定义的。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialCondition` |
| **类型**：字符向量 |
| **值**：标量 | 向量 |
| **默认值**：`'0'` |

### **输入处理** — 指定基于采样或基于帧的处理 `Elements as channels (sample based)`（默认）| `Columns as channels (frame based)`

指定模块执行基于采样还是基于帧的处理：

- `Columns as channels (frame based)` — 将输入的每一列视为单独的通道（基于帧的处理）。

  **注意**

  基于帧的处理需要 DSP System Toolbox™ 许可证。

  有关详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。
- `Elements as channels (sample based)` — 将输入的每个元素视为单独的通道（基于采样的处理）。

使用 **输入处理** 指定模块执行基于采样还是基于帧的处理。有关这两种处理模式的详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。

#### 编程使用

|  |
| --- |
| **模块参数**：`InputProcessing` |
| **类型**：字符向量 |
| **值**：`'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **默认值**：`'Elements as channels (sample based)'` |

### **采样时间（-1 表示继承）** — 采样时间命中之间的离散间隔 `-1`（默认）| 1×2 向量

输入采样时间命中之间的离散间隔，或指定 `-1` 以继承采样时间。

另请参阅 Specify Sample Time。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：实数标量 | 1×2 向量 |
| **默认值**：`'-1'` |

### 状态属性

### **状态名称** — 模块状态的唯一名称 `''`（默认）| 字母数字字符串

使用此参数为模块状态分配唯一名称。默认值为 `' '`。当此字段为空时，不分配名称。使用此参数时，请记住以下注意事项：

- 有效标识符以字母或下划线字符开头，后跟字母数字或下划线字符。
- 状态名称仅适用于所选模块。

当您点击 **应用** 时，此参数会启用 **状态名称必须解析为 Simulink 信号对象**。

有关详细信息，请参阅 C Data Code Interface Configuration for Model Interface Elements (Simulink Coder)。

#### 编程使用

|  |
| --- |
| **模块参数：** `StateName` |
| **类型：** 字符向量 |
| **值：** 唯一名称 |
| **默认值：** `''` |

### **状态名称必须解析为 Simulink 信号对象** — 要求状态名称解析为信号对象的选项 `off`（默认）| `on`

指定是否要求状态名称解析为信号对象。如果选中，当您指定的状态名称与信号对象的名称不匹配时，软件将在运行时生成错误。

选中此参数会禁用 **代码生成存储类** 参数。

#### 依赖关系

当您为 **状态名称** 参数指定值，并将 **信号解析** 模型配置参数设置为 `None` 以外的值时启用。

#### 编程使用

|  |
| --- |
| **模块参数**：`StateMustResolveToSignalObject` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |
## 所属库

Simulink / Discrete HDL Coder / Discrete

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `image` | `integer` | `single` | `string` |
| **直接馈通** | `noa` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 此模块的直接馈通特性取决于模块参数值。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`strong.h`）。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **AllowDelayDistribution** | 允许在分布式流水线和延迟吸收优化期间分配或吸收延迟。默认值为 `inherit`。有关更多详细信息，请参阅 AllowDelayDistribution (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ResetType** | 抑制复位逻辑生成。默认值为 `default`，即生成复位逻辑。另请参阅 ResetType (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

将信号延迟一个采样周期

Unit Delay 模块保持其输入并将其延迟一个采样周期。当放置在迭代器子系统中时，它保持其输入并将其延迟一个迭代。此模块等效于 z-1 离散时间算子。该模块接受一个输入并生成一个输出。每个信号可以是标量或向量。如果输入是向量，则该模块保持并向量的所有元素延迟相同的采样周期。

您可以使用 **初始条件** 参数指定第一个采样周期的模块输出。仔细选择此参数可以最大限度地减少不需要的输出行为。您可以使用 **采样时间** 参数指定采样之间的时间。设置为 `-1` 表示模块继承 **采样时间**。

**注意**

如果您使用 Unit Delay 模块在不同采样率下运行的模块之间创建转换，则会出错。请改用 Rate Transition 模块。

### 与相似模块的比较

Memory、Unit Delay 和 Zero-Order Hold 模块提供相似的功能，但具有不同的能力。此外，每个模块的用途也不同。

此表显示了每个模块的建议用法。

| 模块 | 模块用途 | 参考示例 |
| --- | --- | --- |
| Unit Delay | 使用您指定的离散采样时间实现延迟。该模块接受并输出具有离散采样时间的信号。 | - Engine Timing Model with Closed Loop Control（Compression 子系统） |
| Memory | 通过一个主积分时间步长实现延迟。理想情况下，该模块接受连续（或在次要时间步长中固定）信号，并输出在次要时间步长中固定的信号。 | - Building a Clutch Lock-Up Model（Friction Mode Logic/Lockup FSM 子系统） - Capture the Velocity of a Bouncing Ball with the Memory Block |
| Zero-Order Hold | 将具有连续采样时间的输入信号转换为具有离散采样时间的输出信号。 | - Developing the Apollo Lunar Module Digital Autopilot - Radar Tracking Using MATLAB Function Blocks |

每个模块具有以下能力。

| 能力 | Memory | Unit Delay | Zero-Order Hold |
| --- | --- | --- | --- |
| 初始条件指定 | 是 | 是 | 否，因为在时间 t = 0 时的模块输出必须与输入值匹配。 |
| 采样时间指定 | 否，因为该模块只能从驱动模块或用于整个模型的求解器继承采样时间。 | 是 | 是 |
| 基于帧的信号支持 | 否 | 是 | 是 |
| 状态记录支持 | 否 | 是 | 否 |

### 字符串支持

Unit Delay 模块仅在模块配置为 **初始条件** 参数的默认值（0）时才能接受和输出字符串数据类型。
