---
type: simulink-block
title: 'Enabled Resettable Delay'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'enabledresettabledelay'
documentation_source_path: 'ref/enabledresettabledelay.html'
language: zh-CN
chinese_source: worker-translation
---

# Enabled Resettable Delay

## 端口
```yaml
ports:
- name: u
  summary: 数据输入信号 标量 | 向量
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | string | Boolean
    | fixed point | enumerated | bus
- name: d
  summary: 延迟长度 标量
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | fixed point
- name: Enable
  summary: 外部使能信号 标量
  direction: input
  data_types: Boolean
- name: External reset
  summary: 外部复位信号 标量
  direction: input
  data_types: Boolean
- name: x0
  summary: 初始条件 标量 | 向量
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point | bus
- name: Port_1
  summary: 输出信号 标量 | 向量
  direction: output
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | string | Boolean
    | fixed point | enumerated | bus
```

### 输入

### **u** — 数据输入信号 标量 | 向量

根据参数设置进行延迟的输入数据信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **d** — 延迟长度 标量

延迟长度，指定为从输入端口继承。当您将 **Delay length: Source** 参数选择为 `Input port` 时启用。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Enable** — 外部使能信号 标量

使能或禁用模块执行的使能信号。要创建此端口，请选择 **Show enable port** 参数。

**数据类型：** `Boolean`

### **External reset** — 外部复位信号 标量

将模块执行复位到初始条件的外部信号。要创建此端口，请选择 **External reset** 参数。

**数据类型：** `Boolean`

### **x0** — 初始条件 标量 | 向量

初始条件，指定为从输入端口继承。当您将 **Initial Condition: Source** 参数选择为 `Input port` 时启用。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

输出信号，即输入信号延迟由 **Delay length** 参数指定的时间长度。输出信号的初始值取决于若干条件。请参阅 Delay。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: Delay length
  summary: 延迟长度 Dialog（默认）| Input port
  group: 主要
  block_parameter: DelayLengthUpperLimit
  type: 字符向量
  values: 标量
  default: '''100'''
- name: Initial condition
  summary: 初始条件 Dialog（默认）| Input port
  group: 主要
  block_parameter: InitialCondition
  type: 字符向量
  values: 标量
  default: '''0.0'''
- name: 输入处理
  summary: 指定基于采样或基于帧的处理 Elements as channels (sample based)（默认）| Columns as channels (frame based)
  group: 主要
  block_parameter: InputProcessing
  type: 字符向量
  values: '''Columns as channels (frame based)'' | ''Elements as channels (sample based)'''
  default: '''Elements as channels (sample based)'''
- name: 使用循环缓冲区存储状态
  summary: 用于存储状态的循环缓冲区 off（默认）| on
  group: 主要
  block_parameter: UseCircularBuffer
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: 防止直接馈通
  summary: 防止直接馈通 off（默认）| on
  group: 主要
  block_parameter: PreventDirectFeedthrough
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: 在生成的代码中移除延迟长度检查
  summary: 移除延迟长度超出范围检查 off（默认）| on
  group: 主要
  block_parameter: RemoveDelayLengthCheckInGeneratedCode
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: 延迟长度的诊断
  summary: 延迟长度的诊断检查 None（默认）| Warning | Error
  group: 主要
  block_parameter: DiagnosticForDelayLength
  type: 字符向量
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''None'''
- name: 显示使能端口
  summary: 创建使能端口 on（默认）| off
  group: 主要
  block_parameter: ShowEnablePort
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''on'''
- name: 外部复位
  summary: 外部状态复位 None（默认）| Rising | Falling | Either | Level | Level hold
  group: 主要
  block_parameter: ExternalReset
  type: 字符向量
  values: '''None'' | ''Rising'' | ''Falling'' | ''Either'' | ''Level'' | ''Level hold'''
  default: '''None'''
- name: 采样时间（-1 表示继承）
  summary: 采样时间命中之间的离散间隔 -1（默认）| scalar
  group: 主要
  block_parameter: SampleTime
  type: 字符向量
  values: 实数标量
  default: '''-1'''
- name: 状态名称
  summary: 模块状态的唯一名称 ''（默认）| 字母数字字符串
  group: 状态属性
  block_parameter: StateName
  type: 字符向量
  values: 唯一名称
  default: ''''''
- name: State name must resolve to Simulink signal object
  summary: 要求状态名称解析为信号对象的选项 off（默认）| on
  group: 状态属性
  block_parameter: StateMustResolveToSignalObject
  type: 字符向量
  values: '''off'' | ''on'''
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### 主要

### **Delay length** — 延迟长度 `Dialog`（默认）| `Input port`

指定是直接在对话框上输入延迟长度（固定延迟）还是从输入端口继承延迟（可变延迟）。

- 如果将 **Source** 设置为 `Dialog`，请在 **Value** 下的编辑字段中输入延迟长度。
- 如果将 **Source** 设置为 `Input port`，请验证上游信号为 `d` 输入端口提供延迟长度。您还可以通过指定 **Upper limit** 参数来指定其最大值。

将标量延迟长度指定为实数非负整数。对话框中超出范围或非整数的值（固定延迟）会返回错误。来自输入端口的超出范围的值（可变延迟）会将其转换到范围内。来自输入端口的非整数值（可变延迟）会将其截断为整数。

#### 编程用法

|  |
| --- |
| **模块参数**：`DelayLengthSource` |
| **类型**：字符向量 |
| **值**：`'Dialog'` | `'Input port'` |
| **默认值**：`'Dialog'` |

|  |
| --- |
| **模块参数**：`DelayLength` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'2'` |

|  |
| --- |
| **模块参数**：`DelayLengthUpperLimit` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'100'` |

### **Initial condition** — 初始条件 `Dialog`（默认）| `Input port`

指定是直接在对话框上输入初始条件还是从输入端口继承初始条件。

- 如果将 **Source** 设置为 `Dialog`，请在 **Value** 下的编辑字段中输入初始条件。
- 如果将 **Source** 设置为 `Input port`，请验证上游信号为 `x0` 输入端口提供初始条件。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialConditionSource` |
| **类型**：字符向量 |
| **值**：`'Dialog'` | `'Input port'` |
| **默认值**：`'Dialog'` |

|  |
| --- |
| **模块参数**：`InitialCondition` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0.0'` |

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

### **使用循环缓冲区存储状态** — 用于存储状态的循环缓冲区 `off`（默认）| `on`

选择此项以在仿真和代码生成中使用循环缓冲区存储状态。否则，使用数组缓冲区存储状态。

当延迟长度较大时，使用循环缓冲区可以提高执行速度。对于数组缓冲区，复制操作的数量随着延迟长度的增加而增加。对于循环缓冲区，复制操作的数量在延迟长度增加时保持不变。

如果以下条件之一为真，则始终使用数组缓冲区存储状态，因为循环缓冲区不会提高执行速度。

- 对于基于采样的信号，延迟长度为 1。
- 对于基于帧的信号，延迟长度不大于帧大小。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseCircularBuffer` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **防止直接馈通** — 防止直接馈通 `off`（默认）| `on`

选择此项以将延迟长度从零增加到 **输入处理** 模式的下限。

- 对于基于采样的信号，将最小延迟长度增加到 1。
- 对于基于帧的信号，将最小延迟长度增加到帧长度。

选中此复选框可防止从输入端口 `u` 到输出端口的直接馈通。但是，此复选框无法防止从初始条件端口 `x0` 到输出端口的直接馈通。

#### 依赖关系

要启用此参数，请将 **延迟长度：源** 设置为 `Input port`。

#### 编程使用

|  |
| --- |
| **模块参数**：`PreventDirectFeedthrough` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **在生成的代码中移除延迟长度检查** — 移除延迟长度超出范围检查 `off`（默认）| `on`

选择此项以移除检查延迟长度是否超出范围的代码。

| 复选框 | 结果 | 使用时机 |
| --- | --- | --- |
| 选中 | 生成的代码不包含用于检查延迟长度是否超出范围的条件语句。 | 用于提高代码效率 |
| 清除 | 生成的代码包含用于检查延迟长度是否超出范围的条件语句。 | 用于安全关键型应用 |

#### 依赖关系

要启用此参数，请将 **延迟长度：源** 设置为 `Input port`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`RemoveDelayLengthCheckInGeneratedCode` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **延迟长度的诊断** — 延迟长度的诊断检查 `None`（默认）| `Warning` | `Error`

指定当输入 `d` 小于下限或大于**延迟长度：上限**时是否生成警告或错误。下限取决于**防止直接馈通**的设置。

- 如果清除该复选框，下限为零。
- 如果选中该复选框，对于基于采样的信号，下限为 1；对于基于帧的信号，下限为帧长度。

诊断选项包括：

- `None` — Simulink 软件不采取任何操作。
- `Warning` — Simulink 软件显示警告并继续仿真。
- `Error` — Simulink 软件终止仿真并显示错误。

#### 依赖关系

要启用此参数，请将**延迟长度：来源**设置为 `Input port`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`DiagnosticForDelayLength` |
| **类型**：字符向量 |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'None'` |

### **显示使能端口** — 创建使能端口 `on`（默认）| `off`

选择此项以通过使能端口控制此模块的执行。当此端口的输入为非零时，模块被视为已使能；当输入为 `0` 时，模块被禁用。输入值在与模块执行相同的时间步进行检查。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowEnablePort` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'on'` |

### **外部复位** — 外部状态复位 `None`（默认）| `Rising` | `Falling` | `Either` | `Level` | `Level hold`

指定用于将状态复位到初始条件的触发事件。

| 复位模式 | 行为 |
| --- | --- |
| `None` | 不复位 |
| `Rising` | 在上升沿复位 |
| `Falling` | 在下降沿复位 |
| `Either` | 在上升沿或下降沿复位 |
| `Level` | 在以下任一情况下复位：  - 当复位信号在当前时间步为非零时 - 当复位信号值从上一时间步的非零变为当前时间步的零时 |
| `Level hold` | 当复位信号在当前时间步为非零时复位 |

#### 程序化使用

|  |
| --- |
| **模块参数**：`ExternalReset` |
| **类型**：字符向量 |
| **值**：`'None'` | `'Rising'` | `'Falling'` | `'Either'` | `'Level'` | `'Level hold'` |
| **默认值**：`'None'` |

### **采样时间（-1 表示继承）** — 采样时间命中之间的离散间隔 `-1`（默认）| `scalar`

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。此模块支持离散采样时间，但不支持连续采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：实数标量 |
| **默认值**：`'-1'` |

### 状态属性

### **状态名称** — 模块状态的唯一名称 `''`（默认）| 字母数字字符串

使用此参数为模块状态分配唯一名称。默认值为 `' '`。当此字段为空时，不分配名称。使用此参数时，请记住以下注意事项：

- 有效标识符以字母或下划线字符开头，后跟字母数字或下划线字符。
- 状态名称仅适用于所选模块。

当您点击**应用**时，此参数会启用**状态名称必须解析为 Simulink 信号对象**。

有关详细信息，请参阅模型接口元素的 C 数据代码接口配置。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StateName` |
| **类型：** 字符向量 |
| **值：** 唯一名称 |
| **默认值：** `''` |

### **State name must resolve to Simulink signal object** — 要求状态名称解析为信号对象的选项 `off`（默认）| `on`

指定是否要求状态名称解析为信号对象。如果选中，当您指定的状态名称与信号对象的名称不匹配时，软件将在运行时生成错误。

选中此参数会禁用 **Code generation storage class** 参数。

#### 依赖关系

当您为 **State name** 参数指定值，并将 **Signal resolution** 模型配置参数设置为 `None` 以外的值时启用。

#### 程序化使用

|  |
| --- |
| **模块参数**：`StateMustResolveToSignalObject` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认**：`'off'` |
## 所属库

HDL Coder / Discrete Simulink / Discrete

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成
使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的配置选项。

| 模块参数设置 | 描述 |
| --- | --- |
| 将 **External reset** 设置为 `Level`。 | 在 HDL 代码中生成复位端口。 |
| 选择 **Show enable port**。 | 在 HDL 代码中生成使能端口。 |
| 对于 **Initial condition**，将 **Source** 设置为 `Dialog` 并输入值。 | 为模块指定初始条件。 |
| 将 **Input processing** 设置为 `Columns as channels (frame based)` 或 `Elements as channels (sample based)`。 | 期望向量输入数据，其中向量的每个元素表示一个时间样本。 |

**使用 State Control 模块时的附加设置**

如果在 Simulink 模型的子系统内将 State Control 模块与 Delay 模块一起使用，请使用以下附加设置。

| 模块参数设置 | 描述 |
| --- | --- |
| 对于 State Control 模块的 `Synchronous` 模式，将 **External reset** 设置为 `Level hold`；对于 `Classic` 模式，设置为 `Level`。 | 在 HDL 代码中生成复位端口。 |
| 对于带外部使能端口的 Delay 模块，将 **Delay length** 设置为零。 | 仅在 State Control 模块的 `Synchronous` 模式下被视为导线。 |
| 对于带外部复位端口的 Delay 模块，将 **Delay length** 设置为零。 | 在 State Control 模块的 `Synchronous` 和 `Classic` 模式下被视为导线。 |

有关 State Control 模块的更多信息，请参阅 State Control。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **AllowDelayDistribution** | 允许在分布式流水线和延迟吸收优化期间分配或吸收延迟。默认值为 `inherit`。有关更多详细信息，请参阅 AllowDelayDistribution。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |
| **ResetType** | 抑制复位逻辑生成。默认值为 `default`，即生成复位逻辑。另请参阅 ResetType。 |
| **UseRAM** | 将延迟映射到 RAM 而不是寄存器。默认值为 `off`。另请参阅 UseRAM。 |

**可变整数延迟支持**

- 可以为通过 `Input port` 设置 **Delay Length** 的 Delay 模块生成 HDL 代码。输入延迟长度可以是整数类型或浮点类型。
- 代码生成支持延迟模块 'd' 端口处的正整数值。通过输入端口设置的延迟长度必须介于 `0` 和模块参数对话框中指定的 `Upper limit` 之间。
- 对于负延迟长度值，HDL Coder 将这些负延迟长度转换为 `0`。
- 类似地，如果指定的延迟长度大于上限，HDL Coder 会将延迟长度转换为 `Upper limit` 值。
- 上限范围由延迟长度输入数据类型的范围定义。例如，如果将延迟长度输入数据类型指定为 `uint8`，则上限不得超过 `255`。
- 可以为可变整数 Delay 模块使用使能和复位端口。

**复数数据支持**

此模块支持复数信号的代码生成。

**限制**

- 对于 **Initial condition**，将 **Source** 设置为
  `Input port` 不支持 HDL 代码生成。
- HDL 代码生成在 Reset 和 Enable 端口仅支持 Boolean 数据类型。
- 对于通过 `Input port` 设置 **Delay Length** 的 Delay 模块，不支持用于 RAM 映射的 HDL Block Property **UseRAM**。
- 通过 `Input port` 设置 **Delay Length** 的 Delay 模块不支持用于 HDL 代码生成的 bus 和 matrix 数据输入。

## 版本历史

**在 R2024b 中引入**

## 描述

当外部 Enable 信号为 true 且外部 Reset 信号为 false 时，将输入信号延迟固定或可变采样周期

当 Enable 信号为 true 且 Reset 信号为 false 时，Enabled Resettable Delay 模块将输入信号延迟若干时间步。当 Reset 信号为 true 时，状态和输出信号采用 Initial condition 参数的值。该模块支持：

- 可变延迟长度
- 状态存储
- 使用循环缓冲区而非数组缓冲区进行状态存储
- 通过外部复位信号将状态重置为初始条件
- 通过外部使能信号控制模块在每个时间步的执行
