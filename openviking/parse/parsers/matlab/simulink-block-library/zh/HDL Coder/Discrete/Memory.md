---
type: simulink-block
title: 'Memory'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'memory'
documentation_source_path: '../simulink/slref/memory.html'
language: zh-CN
chinese_source: worker-translation
---

# Memory

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

输入信号，指定为标量、向量、矩阵或 N 维数组。输入可以是连续的或离散的，包含 Simulink® 支持的任何数据类型的实数值或复数值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 延迟一个主积分时间步的输入 标量 | 向量 | 矩阵 | N 维数组

输出是上一个时间步的输入。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### 主要

### **初始条件** — 初始条件 0（默认）| 标量 | 向量 | 矩阵 | N 维数组

指定初始积分步的输出。当不使用内置输入数据类型时，此值必须为 0。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialCondition` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 |
| **默认：** `'0'` |

### **继承采样时间** — 继承采样时间 `off`（默认）| `on`

选择以从驱动模块继承采样时间：

- 如果驱动模块具有离散采样时间，则该模块继承该采样时间。
- 如果驱动模块具有连续采样时间，则选中此复选框没有效果。采样时间取决于用于仿真模型的求解器类型。

清除此复选框时，模块采样时间取决于用于仿真模型的求解器类型：

- 如果求解器是变步长求解器，则模块采样时间是连续的但在次时间步中固定：`[0, 1]`。
- 如果求解器是固定步长求解器，则 `[0, 1]` 采样时间在采样时间传播后转换为求解器步长。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InheritSampleTime` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认：** `'off'` |

### **线性化期间输入的直接馈通** — 在线性化和配平期间输出输入 `off`（默认）| `on`

选择以在线性化和配平期间输出输入。此选择将模块模式设置为直接馈通。

选中此复选框可能导致在使用函数 `linmod`、`dlinmod` 或 `trim` 时模型中状态顺序发生变化。要提取此新的状态顺序，请使用以下命令。

首先使用以下命令编译模型，其中 `model` 是 Simulink 模型的名称。

```
    [sizes, x0, x_str] = model([],[],[],'lincompile');
```

接下来，使用此命令终止编译。

```
  model([],[],[],'term');
```

输出参数 `x_str` 是 Simulink 模型中状态的元胞数组，包含新的状态顺序。当将状态向量作为输入传递给 `linmod`、`dlinmod` 或 `trim` 函数时，状态向量必须使用此新的状态顺序。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LinearizeMemory` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认：** `'off'` |

### **使用离散采样时间线性化时视为单位延迟** — 对离散输入线性化为单位延迟 `off`（默认）| `on`

选择以在 Memory 模块由具有离散采样时间的信号驱动时，将 Memory 模块线性化为单位延迟。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LinearizeAsDelay` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认：** `'off'` |

### 状态属性

### **状态名称** — 模块状态的唯一名称 `''`（默认）| 字母数字字符串

使用此参数为模块状态分配唯一名称。默认值为 `' '`。当此字段为空时，不分配名称。使用此参数时，请记住以下注意事项：

- 有效标识符以字母或下划线字符开头，后跟字母数字或下划线字符。
- 状态名称仅适用于所选模块。

当您点击 **应用** 时，此参数会启用 **状态名称必须解析为 Simulink 信号对象**。

有关详细信息，请参阅 C Data Code Interface Configuration for Model Interface Elements (Simulink Coder)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StateName` |
| **类型：** 字符向量 |
| **值：** 唯一名称 |
| **默认：** `''` |

### **状态名称必须解析为 Simulink 信号对象** — 要求状态名称解析为信号对象 `off`（默认）| `on`

选中此复选框以要求状态名称解析为 Simulink 信号对象。

#### 依赖关系

要启用此参数，请为 **状态名称** 指定一个值。仅当您将模型配置参数 **信号解析** 设置为 `None` 以外的值时，此参数才会出现。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StateMustResolveToSignalObject` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认：** `'off'` |

## 所属库

Simulink / Discrete HDL Coder / Discrete

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `noa` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 此模块的直接馈通特性取决于模块参数值。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
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

输出上一个时间步的输入

Memory 模块保持其输入并将其延迟一个主积分时间步。当放置在迭代器子系统中时，它保持其输入并将其延迟一个迭代。此模块接受连续和离散信号。该模块接受一个输入并生成一个输出。每个信号可以是标量、向量、矩阵或 N 维数组。如果输入是非标量，则该模块将所有输入元素保持并延迟相同的时间步。

您使用 **初始条件** 参数指定第一个时间步的模块输出。仔细选择此参数可以最小化不需要的输出行为。但是，您无法指定采样时间。此模块的采样时间取决于所使用的求解器类型，或者您可以指定继承它。**继承采样时间** 参数决定采样时间是继承的还是基于求解器的。

**提示**

当以下两个条件同时为真时，避免使用 Memory 模块：

- 您的模型使用变步长求解器 `ode15s` 或 `ode113`。
- 模块的输入在仿真期间发生变化。

当 Memory 模块继承离散采样时间时，该模块类似于 Unit Delay 模块。但是，Memory 模块不支持状态记录。如果需要记录最终状态，请改用 Unit Delay 模块。

### 与相似模块的比较

Memory、Unit Delay 和 Zero-Order Hold 模块提供相似的功能，但具有不同的能力。此外，每个模块的用途也不同。

此表显示了每个模块的推荐用法。

| 模块 | 模块用途 | 参考示例 |
| --- | --- | --- |
| Unit Delay | 使用您指定的离散采样时间实现延迟。该模块接受并输出具有离散采样时间的信号。 | - Engine Timing Model with Closed Loop Control (Compression subsystem) |
| Memory | 通过一个主积分时间步实现延迟。理想情况下，该模块接受连续（或次时间步中固定）信号，并输出在次时间步中固定的信号。 | - Building a Clutch Lock-Up Model (Friction Mode Logic/Lockup FSM subsystem) - Capture the Velocity of a Bouncing Ball with the Memory Block |
| Zero-Order Hold | 将具有连续采样时间的输入信号转换为具有离散采样时间的输出信号。 | - Developing the Apollo Lunar Module Digital Autopilot - Radar Tracking Using MATLAB Function Blocks |

每个模块具有以下能力。

| 能力 | Memory | Unit Delay | Zero-Order Hold |
| --- | --- | --- | --- |
| 初始条件的指定 | 是 | 是 | 否，因为在时间 t = 0 时的模块输出必须与输入值匹配。 |
| 采样时间的指定 | 否，因为该模块只能从驱动模块或用于整个模型的求解器继承采样时间。 | 是 | 是 |
| 对基于帧的信号的支持 | 否 | 是 | 是 |
| 对状态记录的支持 | 否 | 是 | 否 |

### 总线支持

Memory 模块是支持总线的模块。输入可以是虚拟或非虚拟总线信号，但受以下限制：

- **初始条件** 必须为零、非零标量或有限数值结构体。
- 如果 **初始条件** 为零或结构体，并且您指定了 **状态名称**，则输入不能是虚拟总线。
- 如果 **初始条件** 为非零标量，则不能指定 **状态名称**。

有关指定初始条件结构体的信息，请参阅 Specify Initial Conditions for Bus Elements。

输入到 Memory 模块的非虚拟总线中的所有信号必须具有相同的采样时间，即使关联总线对象的元素指定了继承采样时间。您可以使用 Rate Transition 模块来更改单个信号或总线中所有信号的采样时间。有关更多信息，请参阅 Modify Sample Times for Nonvirtual Buses and Bus-Capable Blocks。

您可以使用总线数组作为 Memory 模块的输入信号。您可以使用以下内容指定 **初始条件** 参数：

- 值 `0`。在这种情况下，总线数组中的所有单个信号使用初始值 `0`。
- 结构体数组，为总线数组中的每个单个信号指定初始条件。
- 标量结构体，为总线类型定义的每个元素指定初始条件。使用此技术为数组中的每个总线指定相同的初始条件。

有关定义和使用总线数组的详细信息，请参阅 Group Nonvirtual Buses in Arrays of Buses。
