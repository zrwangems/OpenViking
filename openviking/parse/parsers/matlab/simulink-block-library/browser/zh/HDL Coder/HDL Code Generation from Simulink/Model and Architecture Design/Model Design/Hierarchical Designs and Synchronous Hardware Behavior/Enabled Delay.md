---
type: simulink-block
title: 'Enabled Delay'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Code Generation from Simulink / Model and Architecture Design / Model Design / Hierarchical Designs and Synchronous Hardware Behavior'
documentation_page: 'enableddelay'
documentation_source_path: 'ref/enableddelay.html'
language: zh-CN
chinese_source: worker-translation
---

# Enabled Delay

## 端口

### 输入

### **u** — 数据输入信号 标量 | 向量

根据参数设置延迟的输入数据信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **d** — 延迟长度 标量

指定为从输入端口继承的延迟长度。当您将 **延迟长度: 源** 参数选择为 `Input port` 时启用。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Enable** — 外部使能信号 标量

使能或禁用模块执行的使能信号。要创建此端口，请选择 **显示使能端口** 参数。

**数据类型：** `Boolean`

### **External reset** — 外部复位信号 标量

将模块执行复位到初始条件的外部信号。要创建此端口，请选择 **外部复位** 参数。

**数据类型：** `Boolean`

### **x0** — 初始条件 标量 | 向量

指定为从输入端口继承的初始条件。当您将 **初始条件: 源** 参数选择为 `Input port` 时启用。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

输出信号，即输入信号延迟参数 **延迟长度** 指定的时间长度后的信号。输出信号的初始值取决于多个条件。请参阅 Delay。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### 主要

### **延迟长度** — 延迟长度 `Dialog`（默认） | `Input port`

指定是直接在对话框上输入延迟长度（固定延迟），还是从输入端口继承延迟（可变延迟）。

- 如果将 **源** 设置为 `Dialog`，请在 **值** 下的编辑字段中输入延迟长度。
- 如果将 **源** 设置为 `Input port`，请验证上游信号为 `d` 输入端口提供延迟长度。您还可以通过指定 **上限** 参数来指定其最大值。

将标量延迟长度指定为实数非负整数。对话框（固定延迟）中超出范围或非整数的值会返回错误。来自输入端口（可变延迟）的超出范围的值会将其转换到范围内。来自输入端口（可变延迟）的非整数值会将其截断为整数。

#### 编程用法

|  |
| --- |
| **模块参数**：`DelayLengthSource` |
| **类型**：character vector |
| **值**：`'Dialog'` | `'Input port'` |
| **默认值**：`'Dialog'` |

|  |
| --- |
| **模块参数**：`DelayLength` |
| **类型**：character vector |
| **值**：标量 |
| **默认值**：`'2'` |

|  |
| --- |
| **模块参数**：`DelayLengthUpperLimit` |
| **类型**：character vector |
| **值**：标量 |
| **默认值**：`'100'` |

### **初始条件** — 初始条件 `Dialog`（默认） | `Input port`

指定是直接在对话框上输入初始条件，还是从输入端口继承初始条件。

- 如果将 **源** 设置为 `Dialog`，请在 **值** 下的编辑字段中输入初始条件。
- 如果将 **源** 设置为 `Input port`，请验证上游信号为 `x0` 输入端口提供初始条件。

Simulink 会在离线情况下使用四舍五入取整操作和饱和，将 **初始条件** 的数据类型转换为输入信号 `u` 的数据类型。

#### 编程用法

|  |
| --- |
| **模块参数**：`InitialConditionSource` |
| **类型**：character vector |
| **值**：`'Dialog'` | `'Input port'` |
| **默认值**：`'Dialog'` |

|  |
| --- |
| **模块参数**：`InitialCondition` |
| **类型**：character vector |
| **值**：标量 |
| **默认值**：`'0.0'` |

### **输入处理** — 指定基于采样或基于帧的处理 `Elements as channels (sample based)`（默认） | `Columns as channels (frame based)`

指定模块执行基于采样还是基于帧的处理：

- `Columns as channels (frame based)` — 将输入的每一列视为单独通道（基于帧的处理）。

  **注意**

  基于帧的处理需要 DSP System Toolbox™ 许可证。

  有关详细信息，请参阅基于采样和基于帧的概念 (DSP System Toolbox)。
- `Elements as channels (sample based)` — 将输入的每个元素视为单独通道（基于采样的处理）。

使用 **输入处理** 指定模块执行基于采样还是基于帧的处理。有关这两种处理模式的详细信息，请参阅基于采样和基于帧的概念 (DSP System Toolbox)。

#### 编程用法

|  |
| --- |
| **模块参数**：`InputProcessing` |
| **类型**：character vector |
| **值**：`'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **默认值**：`'Elements as channels (sample based)'` |

### **使用循环缓冲区存储状态** — 用于存储状态的循环缓冲区 `off`（默认） | `on`

选择以在仿真和代码生成中使用循环缓冲区存储状态。否则，使用数组缓冲区存储状态。

当延迟长度较大时，使用循环缓冲区可以提高执行速度。对于数组缓冲区，复制操作的数量会随着延迟长度的增加而增加。对于循环缓冲区，随着延迟长度的增加，复制操作的数量保持不变。

如果以下条件之一成立，则始终使用数组缓冲区存储状态，因为循环缓冲区不会提高执行速度。

- 对于基于采样的信号，延迟长度为 1。
- 对于基于帧的信号，延迟长度不大于帧大小。

#### 编程用法

|  |
| --- |
| **模块参数**：`UseCircularBuffer` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **防止直接馈通** — 防止直接馈通 `off`（默认） | `on`

选择以将延迟长度从零增加到 **输入处理** 模式的下限。

- 对于基于采样的信号，将最小延迟长度增加到 1。
- 对于基于帧的信号，将最小延迟长度增加到帧长度。

选中此复选框可防止从输入端口 `u` 到输出端口的直接馈通。但是，此复选框无法防止从初始条件端口 `x0` 到输出端口的直接馈通。

#### 依赖关系

要启用此参数，请将 **延迟长度: 源** 设置为 `Input port`。

#### 编程用法

|  |
| --- |
| **模块参数**：`PreventDirectFeedthrough` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **在生成代码中移除延迟长度检查** — 移除延迟长度超出范围检查 `off`（默认） | `on`

选择以移除检查延迟长度是否超出范围的代码。

| 复选框 | 结果 | 使用时机 |
| --- | --- | --- |
| 选中 | 生成的代码不包含用于检查延迟长度是否超出范围的条件语句。 | 为了提高代码效率 |
| 清除 | 生成的代码包含用于检查延迟长度是否超出范围的条件语句。 | 用于安全关键型应用 |

#### 依赖关系

要启用此参数，请将 **延迟长度: 源** 设置为 `Input port`。

#### 编程用法

|  |
| --- |
| **模块参数**：`RemoveDelayLengthCheckInGeneratedCode` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **延迟长度诊断** — 延迟长度的诊断检查 `None`（默认） | `Warning` | `Error`

指定当输入 `d` 小于下限或大于 **延迟长度: 上限** 时是产生警告还是错误。下限取决于 **防止直接馈通** 的设置。

- 如果清除该复选框，则下限为零。
- 如果选中该复选框，则对于基于采样的信号，下限为 1；对于基于帧的信号，下限为帧长度。

诊断选项包括：

- `None` — Simulink 软件不采取任何操作。
- `Warning` — Simulink 软件显示警告并继续仿真。
- `Error` — Simulink 软件终止仿真并显示错误。

#### 依赖关系

要启用此参数，请将 **延迟长度: 源** 设置为 `Input port`。

#### 编程用法

|  |
| --- |
| **模块参数**：`DiagnosticForDelayLength` |
| **类型**：character vector |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'None'` |

### **显示使能端口** — 创建使能端口 `on`（默认） | `off`

选择以使用使能端口控制此模块的执行。当此端口的输入为非零时，模块被视为已启用；当输入为 `0` 时，模块被视为已禁用。输入值在模块执行的同一时间步进行检查。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowEnablePort` |
| **类型：** character vector |
| **值：** `'off' | 'on'` |
| **默认值：** `'on'` |

### **外部复位** — 外部状态复位 `None`（默认） | `Rising` | `Falling` | `Either` | `Level` | `Level hold`

指定用于将状态复位到初始条件的触发事件。

| 复位模式 | 行为 |
| --- | --- |
| `None` | 不复位 |
| `Rising` | 在上升沿复位 |
| `Falling` | 在下降沿复位 |
| `Either` | 在上升沿或下降沿复位 |
| `Level` | 在以下任一情况下复位： - 当前时间步的复位信号为非零时 - 当复位信号值从上一时间步的非零变为当前时间步的零时 |
| `Level hold` | 当前时间步的复位信号为非零时复位 |

#### 编程用法

|  |
| --- |
| **模块参数**：`ExternalReset` |
| **类型**：character vector |
| **值**：`'None'` | `'Rising'` | `'Falling'` | `'Either'` | `'Level'` | `'Level hold'` |
| **默认值**：`'None'` |

### **采样时间（-1 表示继承）** — 采样时间命中之间的离散间隔 `-1`（默认） | `scalar`

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。此模块支持离散采样时间，但不支持连续采样时间。

#### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：character vector |
| **值**：real scalar |
| **默认值**：`'-1'` |

### 状态属性

### **状态名称** — 模块状态的唯一名称 `''`（默认） | 字母数字字符串

使用此参数为模块状态分配唯一名称。默认值为 `' '`。当此字段为空时，不分配名称。使用此参数时，请记住以下注意事项：

- 有效标识符以字母或下划线字符开头，后跟字母数字或下划线字符。
- 状态名称仅适用于所选模块。

当您点击 **应用** 时，此参数会启用 **状态名称必须解析为 Simulink 信号对象**。

有关详细信息，请参阅 C Data Code Interface Configuration for Model Interface Elements。

#### 编程用法

|  |
| --- |
| **模块参数：** `StateName` |
| **类型：** character vector |
| **值：** 唯一名称 |
| **默认值：** `''` |

### **状态名称必须解析为 Simulink 信号对象** — 要求状态名称解析为信号对象的选项 `off`（默认） | `on`

指定是否要求状态名称解析为信号对象。如果选中，则当您指定的状态名称与信号对象的名称不匹配时，软件会在运行时生成错误。

选择此参数会禁用 **代码生成存储类** 参数。

#### 依赖关系

当您为 **状态名称** 参数指定值，并将 **信号解析** 模型配置参数设置为 `None` 以外的值时启用。

#### 编程用法

|  |
| --- |
| **模块参数**：`StateMustResolveToSignalObject` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

## 所属库

HDL Coder / Discrete Simulink / Discrete

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的配置选项。

| 模块参数设置 | 描述 |
| --- | --- |
| 将 **External reset** 设置为 `Level`。 | 在 HDL 代码中生成 reset 端口。 |
| 选择 **Show enable port**。 | 在 HDL 代码中生成 enable 端口。 |
| 对于 **Initial condition**，将 **Source** 设置为 `Dialog` 并输入值。 | 为模块指定初始条件。 |
| 将 **Input processing** 设置为 `Columns as channels (frame based)` 或 `Elements as channels (sample based)`。 | 期望向量输入数据，其中向量的每个元素表示一个时间采样。 |

**使用 State Control 模块时的附加设置**

如果在 Simulink 模型中的子系统内将 State Control 模块与 Delay 模块一起使用，请使用以下附加设置。

| 模块参数设置 | 描述 |
| --- | --- |
| 对于 State Control 模块的 `Synchronous` 模式，将 **External reset** 设置为 `Level hold`；对于 `Classic` 模式，将其设置为 `Level`。 | 在 HDL 代码中生成 reset 端口。 |
| 对于具有外部 enable 端口的 Delay 模块，将 **Delay length** 设置为零。 | 仅在 State Control 模块的 `Synchronous` 模式下被视为 wire。 |
| 对于具有外部 reset 端口的 Delay 模块，将 **Delay length** 设置为零。 | 在 State Control 模块的 `Synchronous` 和 `Classic` 模式下被视为 wire。 |

有关 State Control 模块的更多信息，请参阅 State Control。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **AllowDelayDistribution** | 允许在分布式流水线和延迟吸收优化期间分布或吸收延迟。默认值为 `inherit`。有关更多详细信息，请参阅 AllowDelayDistribution。 |
| **InputPipeline** | 要插入到生成代码中的输入流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 要插入到生成代码中的输出流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |
| **ResetType** | 抑制 reset 逻辑生成。默认值为 `default`，这会生成 reset 逻辑。另请参阅 ResetType。 |
| **UseRAM** | 将延迟映射到 RAM 而不是寄存器。默认值为 `off`。另请参阅 UseRAM。 |

**可变整数延迟支持**

- 可以为通过 `Input port` 设置 **Delay
  Length** 的 Delay 模块生成 HDL 代码。输入
  延迟长度可以是整数类型或浮点类型。
- 代码生成支持 Delay
  模块的 'd' 端口处的正整数值。通过输入端口设置的延迟长度必须介于
  `0` 和 `Upper limit` 之间，这些值在 Block
  Parameters 对话框中指定。
- 对于负延迟长度值，HDL Coder 将这些负延迟长度转换为 `0`。
- 类似地，如果指定的延迟长度大于上限，HDL Coder 会将延迟长度转换为 `Upper limit` 值。
- 上限范围由延迟长度输入数据类型的范围定义。例如，
  如果将延迟长度输入数据类型指定为 `uint8`，则
  上限不得超过 `255`。
- 可以为可变整数 Delay 模块使用 enable 和 reset 端口。

**复数数据支持**

此模块支持针对复数信号的代码生成。

**限制**

- 对于 **Initial condition**，将 **Source** 设置为
  `Input port` 的情况不支持 HDL 代码
  生成。
- HDL 代码生成在 Reset 和 Enable
  端口仅支持 Boolean 数据类型。
- 对于通过
  `Input port` 设置 **Delay Length** 的 Delay 模块，不支持
  用于 RAM 映射的 HDL 模块属性 **UseRAM**。
- 通过
  `Input port` 设置 **Delay Length** 的 Delay 模块不支持用于 HDL 代码生成的
  bus 和矩阵数据输入。

## 版本历史

**在 R2024b 中引入**

## 描述

当外部使能信号为 true 时，按固定或可变采样周期延迟输入信号

Enabled Delay 模块根据使能信号的状态输出输入信号的延迟版本。在仿真开始时或使能信号转换为 true 时，模块输出初始条件值 x0。如果使能信号在连续时间步中为 true，模块继续输出按指定延迟长度延迟的输入信号。如果使能信号在仿真开始时为 false，模块输出零。如果使能信号在变为 true 后变为 false，模块保持最后一个输出值，直到使能信号再次变为 true。此模块支持：

- 可变延迟长度
- 状态存储
- 使用循环缓冲区而不是数组缓冲区进行状态存储
- 使用外部 reset 信号将状态重置为初始条件
- 使用外部 enable
  信号控制模块在每个时间步的执行
