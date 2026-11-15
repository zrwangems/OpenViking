---
type: simulink-block
title: 'Unit Delay'
family: discrete
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'unitdelay'
language: zh-CN
chinese_source: official
---

# Unit Delay

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

输入信号，它被模块延迟了一个采样周期。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

输出信号，即延迟了一个采样周期的输入信号。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## 参数

### 常设

### **初始条件** — 第一个采样周期输出 `0` (默认) | 标量 | 向量

指定第一个采样周期的仿真输出，否则，此周期内 Unit Delay 模块的输出为未定义。

#### 编程用法

|  |
| --- |
| **模块参数**：`InitialCondition` |
| **类型**：字符向量 |
| **值**：标量 | 向量 |
| **默认值**：`'0'` |

### **输入处理** — 指定基于采样或基于帧的处理 **元素作为通道(基于采样)** (默认) | **列作为通道(基于帧)**

指定模块是执行基于采样还是基于帧的处理：

- **列作为通道(基于帧)** - 将输入信号的每一列视为一个单独的通道（基于帧的处理）。

  **注意**

  基于帧的处理需要具有 DSP System Toolbox™ 许可证。

  有关详细信息，请参阅Sample- and Frame-Based Concepts (DSP System Toolbox)。
- **元素作为通道(基于采样)** - 将输入信号的每个元素视为一个单独的通道（基于采样的处理）。

可以使用**输入处理**指定模块是执行基于采样的处理还是基于帧的处理。有关这两种处理模式的详细信息，请参阅Sample- and Frame-Based Concepts (DSP System Toolbox)。

#### 编程用法

|  |
| --- |
| **模块参数**：`InputProcessing` |
| **类型**：字符向量 |
| **值**：`'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **默认值**：`'Elements as channels (sample based)'` |

### **采样时间(-1 表示继承)** — 采样时间命中点之间的离散间隔 `-1` (默认) | 1×2 向量

输入采样时间命中点之间的离散间隔，或者指定 `-1` 以继承采样时间。

另请参阅指定采样时间。

#### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：实数标量 | 1×2 向量 |
| **默认值**：`'-1'` |

### 状态属性

### **状态名称** — 模块状态的唯一名称 `''` (默认) | 字母数字字符串

使用此参数为模块状态指定唯一名称。默认值为 `' '`。如果此字段为空，则表示未指定任何名称。使用此参数时，请记住以下注意事项：

- 有效的标识符以字母或下划线字符开始，后跟字母数字或下划线字符。
- 状态名称仅适用于所选模块。

当您点击**应用**时，此参数将启用**状态名称必须解析为 Simulink 信号对象**。

有关详细信息，请参阅模型接口元素的 C 数据代码接口配置 (Simulink Coder)。

#### 编程用法

|  |
| --- |
| **模块参数**：`StateName` |
| **类型：**字符向量 |
| **值：**唯一名称 |
| **默认值：**`''` |

### **状态名称必须解析为 Simulink 信号对象** — 要求状态名称解析为信号对象的选项 `off` (默认) | `on`

指定是否需要将状态名称解析为信号对象。如果选中此选项，则在指定的状态名称与信号对象的名称不匹配时，软件会在运行时生成错误。

选择此参数将禁用**代码生成存储类**参数。

#### 依赖关系

当您为**状态名称**参数指定值并将**信号解析**模型配置参数设置为**无**以外的值时启用。

#### 编程用法

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
| **直接馈通** | `否a` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 此模块的直接馈通特性取决于模块参数值。 | |

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
| **AllowDelayDistribution** | 允许在分布式流水线和延迟吸收优化期间分布或吸收延迟。默认值为 **inherit**。有关详细信息，请参阅AllowDelayDistribution (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |
| **ResetType** | 隐藏重置逻辑生成。默认值为**默认**，它生成重置逻辑。另请参阅ResetType (HDL Coder)。 |

**复数数据支持**

此模块支持复信号的代码生成。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

将信号延迟一个采样周期

Unit Delay 模块将其输入保持并延迟一个采样周期。当放置于迭代子系统中时，该模块将其输入保持并延迟一个迭代。此模块相当于 z-1 离散时间运算符。此模块接受一个输入并生成一个输出。每个信号可以是标量，也可以是向量。如果输入为向量，模块会按相同的采样周期保持和延迟向量中的所有元素。

可通过**初始条件**参数指定第一个采样周期的模块输出。仔细选择此参数可以最大程度地减少不需要的输出行为。可通过**采样时间**参数指定样本之间的时间间隔。设置为 `-1` 表示模块将继承**采样时间**。

**注意**

如果您使用 Unit Delay 模块在以不同采样率运行的模块之间进行速率转移，此模块将报告错误。请改用 Rate Transition 模块。

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

### 字符串支持

仅当 Unit Delay 模块配置为**初始条件**参数采用默认值 (0) 时，该模块才接受和输出字符串数据类型。
