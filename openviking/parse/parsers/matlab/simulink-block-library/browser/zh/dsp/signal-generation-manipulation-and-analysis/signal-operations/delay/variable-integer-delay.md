---
type: simulink-block
title: 'Delay'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Discrete'
documentation_page: 'delay'
documentation_source_path: 'slref/delay.html'
language: zh-CN
chinese_source: worker-translation
---

# Delay

## 端口

### 输入

### **u** — 数据输入信号 标量 | 向量

输入数据信号根据参数设置进行延迟。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **d** — 延迟长度 标量

延迟长度指定为从输入端口继承。当您将 **Delay length: Source** 参数选择为 `Input port` 时启用。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Enable** — 外部使能信号 标量

使能信号，用于启用或禁用模块的执行。要创建此端口，请选择 **Show enable port** 参数。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **External reset** — 外部复位信号 标量

外部信号，用于将模块的执行复位到初始条件。要创建此端口，请选择 **External reset** 参数。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **x0** — 初始条件 标量 | 向量

初始条件指定为从输入端口继承。当您将 **Initial Condition: Source** 参数选择为 `Input port` 时启用。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

输出信号，即由参数 **Delay length** 指定的时间长度延迟后的输入信号。输出信号的初始值取决于若干条件。请参阅初始模块输出。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### 主

### **Delay length** — 延迟长度 `Dialog` (default) | `Input port`

指定是直接在对话框上输入延迟长度（固定延迟），还是从输入端口继承延迟（可变延迟）。

- 如果将 **Source** 设置为 `Dialog`，请在 **Value** 下的编辑字段中输入延迟长度。
- 如果将 **Source** 设置为 `Input port`，请确认上游信号为 `d` 输入端口提供延迟长度。您还可以通过指定参数 **Upper limit** 来指定其最大值。

将标量延迟长度指定为实数非负整数。最大延迟长度会变化。它由以下方程确定：*delay\_length* < *2147483647* / (*bytes\_per\_element* \* *number\_of\_elements*)，其中整数类型（`intmax`）可持有的最大值为 `2147483647`。例如，如果以下条件成立：

- *number\_of\_elements* = `1`
- *bytes\_per\_element* = `8`

则允许的最大延迟长度必须小于 `2147483647/(1 * 8)`，即 `268435455`。如果延迟长度为 `268435456` 或更大，模块将返回如下错误消息：

```
Error:In block  'untitled/Delay', total memory requested
for state is larger than the maximum supported number,
which is '2147483647' bytes for simulation.
To avoid this error, please decrease the value of 'DelayLength'.
```

对话框（固定延迟）中超出范围或非整数的值会返回错误。来自输入端口（可变延迟）的超出范围的值会将其强制转换到范围内。来自输入端口（可变延迟）的非整数值会将其截断为整数。

#### 程序化使用

|  |
| --- |
| **模块参数**: `DelayLengthSource` |
| **类型**: character vector |
| **值**: `'Dialog'` | `'Input port'` |
| **默认值**: `'Dialog'` |

|  |
| --- |
| **模块参数**: `DelayLength` |
| **类型**: character vector |
| **值**: scalar |
| **默认值**: `'2'` |

|  |
| --- |
| **模块参数**: `DelayLengthUpperLimit` |
| **类型**: character vector |
| **值**: scalar |
| **默认值**: `'100'` |

### **Initial condition** — 初始条件 `Dialog` (default) | `Input port`

指定是直接在对话框上输入初始条件，还是从输入端口继承初始条件。

- 如果将 **Source** 设置为 `Dialog`，请在 **Value** 下的编辑字段中输入初始条件。
- 如果将 **Source** 设置为 `Input port`，请确认上游信号为 `x0` 输入端口提供初始条件。

Simulink® 会在离线状态下使用四舍五入到最接近值和饱和操作，将 **Initial condition** 的数据类型转换为输入信号 `u` 的数据类型。

**注意**

当在 **State Attributes** 窗格上选中 **State name must resolve to Simulink signal object** 时，模块会将信号对象的初始值复制到 **Initial condition** 参数。但是，当 **Initial condition** 的源为 `Input port` 时，模块会忽略信号对象的初始值。

#### 程序化使用

|  |
| --- |
| **模块参数**: `InitialConditionSource` |
| **类型**: character vector |
| **值**: `'Dialog'` | `'Input port'` |
| **默认值**: `'Dialog'` |

|  |
| --- |
| **模块参数**: `InitialCondition` |
| **类型**: character vector |
| **值**: scalar |
| **默认值**: `'0.0'` |

### **Input processing** — 指定基于采样或基于帧的处理 `Elements as channels (sample based)` (default) | `Columns as channels (frame based)`

指定模块执行基于采样还是基于帧的处理：

- `Columns as channels (frame based)` — 将输入的每一列视为单独的通道（基于帧的处理）。

  **注意**

  基于帧的处理需要 DSP System Toolbox™ 许可证。

  有关详细信息，请参阅基于采样和基于帧的概念（DSP System Toolbox）。
- `Elements as channels (sample based)` — 将输入的每个元素视为单独的通道（基于采样的处理）。

使用 **Input processing** 指定模块执行基于采样还是基于帧的处理。有关这两种处理模式的详细信息，请参阅基于采样和基于帧的概念（DSP System Toolbox）。

#### 程序化使用

|  |
| --- |
| **模块参数**: `InputProcessing` |
| **类型**: character vector |
| **值**: `'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **默认值**: `'Elements as channels (sample based)'` |

### **Use circular buffer for state** — 用于存储状态的循环缓冲区 `off` (default) | `on`

选择此项以在仿真和代码生成中使用循环缓冲区存储状态。否则，将使用数组缓冲区存储状态。

当延迟长度很大时，使用循环缓冲区可以提高执行速度。对于数组缓冲区，复制操作的数量会随着延迟长度增加而增加。对于循环缓冲区，复制操作的数量在延迟长度增加时保持不变。

如果以下条件之一成立，则始终使用数组缓冲区存储状态，因为循环缓冲区不会提高执行速度。

- 对于基于采样的信号，延迟长度为 1。
- 对于基于帧的信号，延迟长度不大于帧大小。

#### 程序化使用

|  |
| --- |
| **模块参数**: `UseCircularBuffer` |
| **类型**: character vector |
| **值**: `'off'` | `'on'` |
| **默认值**: `'off'` |

### **Prevent direct feedthrough** — 防止直接馈通 `off` (default) | `on`

选择此项以将延迟长度从零增加到 **Input processing** 模式的下限。

- 对于基于采样的信号，将最小延迟长度增加到 1。
- 对于基于帧的信号，将最小延迟长度增加到帧长度。

选中此复选框可防止从输入端口 `u` 到输出端口的直接馈通。但是，此复选框无法防止从初始条件端口 `x0` 到输出端口的直接馈通。

#### 依赖关系

要启用此参数，请将 **Delay length: Source** 设置为 `Input port`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `PreventDirectFeedthrough` |
| **类型**: character vector |
| **值**: `'off'` | `'on'` |
| **默认值**: `'off'` |

### **Remove delay length check in generated code** — 移除延迟长度超出范围检查 `off` (default) | `on`

选择此项以移除检查延迟长度是否超出范围的代码。

| 复选框 | 结果 | 何时使用 |
| --- | --- | --- |
| 已选中 | 生成的代码不包含用于检查延迟长度是否超出范围的条件语句。 | 为了代码效率 |
| 已清除 | 生成的代码包含用于检查延迟长度是否超出范围的条件语句。 | 用于安全关键型应用 |

#### 依赖关系

要启用此参数，请将 **Delay length: Source** 设置为 `Input port`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `RemoveDelayLengthCheckInGeneratedCode` |
| **类型**: character vector |
| **值**: `'off'` | `'on'` |
| **默认值**: `'off'` |

### **Diagnostic for delay length** — 对延迟长度进行诊断检查 `None` (default) | `Warning` | `Error`

指定当输入 `d` 小于下限或大于 **Delay length: Upper limit** 时，是生成警告还是错误。下限取决于 **Prevent direct feedthrough** 的设置。

- 如果清除该复选框，则下限为零。
- 如果选中该复选框，则对于基于采样的信号，下限为 1；对于基于帧的信号，下限为帧长度。

诊断选项包括：

- `None` — Simulink 软件不采取任何操作。
- `Warning` — Simulink 软件显示警告并继续仿真。
- `Error` — Simulink 软件终止仿真并显示错误。

#### 依赖关系

要启用此参数，请将 **Delay length: Source** 设置为 `Input port`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `DiagnosticForDelayLength` |
| **类型**: character vector |
| **值**: `'None'` | `'Warning'` | `'Error'` |
| **默认值**: `'None'` |

### **Show enable port** — 创建使能端口 `off` (default) | `on`

选择此项以使用使能端口控制此模块的执行。当此端口的输入为非零时，模块被视为已启用；当输入为 `0` 时，模块被视为已禁用。输入值在模块执行的同一时间步进行检查。

#### 程序化使用

|  |
| --- |
| **模块参数:** `ShowEnablePort` |
| **类型:** character vector |
| **值:** `'off' | 'on'` |
| **默认值:** `'off'` |

### **External reset** — 外部状态复位 `None` (default) | `Rising` | `Falling` | `Either` | `Level` | `Level hold`

指定用于将状态复位到初始条件的触发事件。

| 复位模式 | 行为 |
| --- | --- |
| `None` | 不复位 |
| `Rising` | 在上升沿复位 |
| `Falling` | 在下降沿复位 |
| `Either` | 在上升沿或下降沿复位 |
| `Level` | 在以下任一情况下复位：  - 当前时间步复位信号为非零时 - 当前时间步复位信号值从前一时间步的非零变为零时 |
| `Level hold` | 当前时间步复位信号为非零时复位 |

#### 程序化使用

|  |
| --- |
| **模块参数**: `ExternalReset` |
| **类型**: character vector |
| **值**: `'None'` | `'Rising'` | `'Falling'` | `'Either'` | `'Level'` | `'Level hold'` |
| **默认值**: `'None'` |

### **Sample time (-1 for inherited)** — 采样时间命中之间的离散间隔 `-1` (default) | `scalar`

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。此模块支持离散采样时间，但不支持连续采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数**: `SampleTime` |
| **类型**: character vector |
| **值**: real scalar |
| **默认值**: `'-1'` |

### 状态属性

### **State name** — 模块状态的唯一名称 `''` (default) | alphanumeric string

使用此参数为模块状态分配唯一名称。默认值为 `' '`。当此字段为空时，不分配名称。使用此参数时，请记住以下注意事项：

- 有效标识符以字母或下划线字符开头，后跟字母数字或下划线字符。
- 状态名称仅适用于所选模块。

当您点击 **Apply** 时，此参数会启用 **State name must resolve to Simulink signal object**。

有关详细信息，请参阅模型接口元素的 C 数据代码接口配置 (Simulink Coder)。

#### 程序化使用

|  |
| --- |
| **模块参数:** `StateName` |
| **类型:** character vector |
| **值:** unique name |
| **默认值:** `''` |

### **State name must resolve to Simulink signal object** — 要求状态名称解析为信号对象 `off` (default) | `on`

选中此复选框以要求状态名称解析为 Simulink 信号对象。

#### 依赖关系

要启用此参数，请为 **State name** 指定一个值。仅当您将模型配置参数 **Signal resolution** 设置为 `None` 以外的值时，才会显示此参数。

#### 程序化使用

|  |
| --- |
| **模块参数:** `StateMustResolveToSignalObject` |
| **类型:** character vector |
| **值:** `'off' | 'on'` |
| **默认值:** `'off'` |

## 所属库

Simulink / Commonly Used Blocks Simulink / Discrete DSP System Toolbox / Signal Operations HDL Coder / Commonly Used Blocks HDL Coder / Discrete

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

在某些条件下，生成的代码依赖 `memcpy` 或 `memset` 函数（`string.h`）。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的配置选项。

| 模块参数设置 | 描述 |
| --- | --- |
| 将 **External reset** 设置为 `Level`。 | 在 HDL 代码中生成复位端口。 |
| 选择 **Show enable port**。 | 在 HDL 代码中生成使能端口。 |
| 对于 **Initial condition**，将 **Source** 设置为 `Dialog` 并输入值。 | 指定模块的初始条件。 |
| 将 **Input processing** 设置为 `Columns as channels (frame based)` 或 `Elements as channels (sample based)`。 | 期望向量输入数据，其中向量的每个元素表示一个时间采样。 |

**使用 State Control 模块时的附加设置**

如果在 Simulink 模型的子系统内将 State Control 模块与 Delay 模块一起使用，请使用以下附加设置。

| 模块参数设置 | 描述 |
| --- | --- |
| 对于 State Control 模块的 `Synchronous` 模式，将 **External reset** 设置为 `Level hold`；对于 `Classic` 模式，设置为 `Level`。 | 在 HDL 代码中生成复位端口。 |
| 对于带有外部使能端口的 Delay 模块，将 **Delay length** 设置为零。 | 仅在 State Control 模块的 `Synchronous` 模式下被视为导线。 |
| 对于带有外部复位端口的 Delay 模块，将 **Delay length** 设置为零。 | 在 State Control 模块的 `Synchronous` 和 `Classic` 模式下被视为导线。 |

有关 State Control 模块的详细信息，请参阅 State Control (HDL Coder)。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **AllowDelayDistribution** | 允许在分布式流水线和延迟吸收优化期间分布或吸收延迟。默认值为 `inherit`。有关更多详细信息，请参阅 AllowDelayDistribution (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ResetType** | 抑制复位逻辑生成。默认值为 `default`，会生成复位逻辑。另请参阅 ResetType (HDL Coder)。 |
| **UseRAM** | 将延迟映射到 RAM 而不是寄存器。默认值为 `off`。另请参阅 UseRAM (HDL Coder)。 |

**可变整数延迟支持**

- 您可以为通过 `Input port` 设置 **Delay Length** 的 Delay 模块生成 HDL 代码。输入延迟长度可以是整数类型或浮点类型。
- 代码生成支持延迟模块 'd' 端口处的正整数值。通过输入端口设置的延迟长度必须介于 `0` 和 `Upper limit` 之间，该值在 Block Parameters 对话框中指定。
- 对于负延迟长度值，HDL Coder 会将这些负延迟长度转换为 `0`。
- 类似地，如果您指定的延迟长度大于上限，HDL Coder 会将延迟长度转换为 `Upper limit` 值。
- 上限范围由延迟长度输入数据类型的范围定义。例如，如果将延迟长度输入数据类型指定为 `uint8`，则上限不得超过 `255`。
- 您可以为可变整数 Delay 模块使用使能和复位端口。

**复数数据支持**

此模块支持复数信号的代码生成。

**使用结构体作为初始值**

您可以为使用结构体指定 Delay 模块初始条件的 Delay 模块生成 HDL 代码。当在模型中对 Delay 模块使用总线输入时，您可以使用结构体值设置延迟模块的初始条件，以初始化总线延迟。

要指定由结构体定义的初始条件：

1. 在模型工作区、MATLAB® 基础工作区、掩码工作区或 Simulink 数据字典中定义结构体。
2. 将初始条件值分配给此结构体。
3. 将 **Initial Condition** 参数设置为 `Dialog`，并在 **Value** 字段中输入该结构体。

您还可以在其他延迟模块中将结构体用作初始值，包括 Unit Delay 和 Tapped Delay 模块

**限制**

- 对于 **Initial condition**，将 **Source** 设置为 `Input port` 不支持 HDL 代码生成。
- HDL 代码生成在 Reset 和 Enable 端口仅支持 Boolean 数据类型。
- 对于通过 `Input port` 设置 **Delay Length** 的 Delay 模块，不支持用于 RAM 映射的 HDL 模块属性 **UseRAM**。
- 通过 `Input port` 设置 **Delay Length** 的 Delay 模块不支持用于 HDL 代码生成的总线和矩阵数据输入。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**早于 R2006a 引入**

## 描述

按固定或可变采样周期延迟输入信号

Delay 模块在延迟后输出模块的输入。该模块基于 **Delay length** 参数的值确定延迟时间。该模块支持：

- 可变延迟长度
- 从输入端口指定初始条件
- 状态存储
- 使用循环缓冲区而不是数组缓冲区进行状态存储
- 使用外部复位信号将状态复位到初始条件
- 使用外部使能信号在每个时间步控制模块的执行

初始模块输出取决于若干因素，例如 **Initial condition** 参数和仿真开始时间。有关详细信息，请参阅初始模块输出。**External reset** 参数确定触发时模块输出是否复位到初始条件。**Show enable port** 参数确定模块执行是否在每个时间步由外部使能信号控制。

### 初始模块输出

仿真前几个时间步的输出取决于模块采样时间、延迟长度和仿真开始时间。该模块支持指定或继承离散采样时间，以确定采样之间的时间间隔。有关详细信息，请参阅指定采样时间。

下表显示了使用这些设置时前几个时间步的 Delay 模块输出。模块继承离散采样时间 `[Tsampling,Toffset]`，其中 `Tsampling` 是采样周期，`Toffset` 是初始时间偏移。*`n`* 是 **Delay length** 参数的值，`Tstart` 是模型的仿真开始时间

| 仿真时间范围 | 模块输出 |
| --- | --- |
| `(Tstart)` 到 `(Tstart + Toffset)` | 零 |
| `(Tstart + Toffset)` 到 `(Tstart + Toffset + n * Tsampling)` | **Initial condition** 参数 |
| 在 `(Tstart + Toffset + n * Tsampling)` 之后 | 输入信号 |

### 外部使能信号行为

选中 **Show enable port** 复选框会启用 Enable 端口。如果使能端口已启用，模块按以下顺序操作

1. 检查是否满足使能条件。
2. 如果复位端口已启用，则检查复位条件。
3. 执行 Delay 模块功能。

模块使用 Enable 端口时具有以下操作：

- 在模块首次使能时，模块输出为初始条件值（`x0`）。
- 对于连续使能信号，模块采用输入信号 u 的最后状态。
- 如果仿真开始时端口未使能，则 Delay 模块输出 `0`。
- 在仿真期间，如果端口在已使能后变为禁用，则模块不执行并保持其最后一个值。

### 可变大小支持

Delay 模块为可变大小信号提供以下支持：

- 数据输入端口 `u` 接受可变大小信号。其他输入端口不接受可变大小信号。
- 对于可变大小输入，输出端口具有与数据输入端口 `u` 相同的信号维度。

适用于可变大小信号的规则取决于 Delay 模块的输入处理模式。

| 输入处理模式 | 可变大小信号支持规则 |
| --- | --- |
| `Elements as channels (sample based)` | - 信号维度仅在模块使能时的状态复位期间发生变化。 - 初始条件必须为标量。 |
| `Columns as channels (frame based)` | - 不支持 |

### 总线支持

Delay 模块为总线信号提供以下支持：

- 数据输入 `u` 接受虚拟和非虚拟总线信号。除输入端口 `x0` 外，其他输入端口不接受总线信号。
- 初始条件 `x0` 端口接受非虚拟总线信号。
- 对于总线输入，输出端口具有与数据输入端口 `u` 相同的总线类型。
- 总线可与以下项一起使用：

  - 基于采样和基于帧的处理
  - 固定和可变延迟长度
  - 数组和循环缓冲区

要将总线信号用作 Delay 模块的输入，请在对话框上或通过 `x0` 端口指定初始条件。对虚拟和非虚拟总线的支持取决于您指定的初始条件以及 **State name** 参数是否为空。对于 `x0` 输入端口，仅支持非虚拟总线。

| Initial Condition | State Name | |
| --- | --- | --- |
| 空 | 非空 |
| 零 | 支持虚拟和非虚拟总线 | 仅支持非虚拟总线 |
| 非零标量 | 支持虚拟和非虚拟总线 | 不支持总线 |
| 非标量 | 不支持总线 | 不支持总线 |
| 结构体 | 支持虚拟和非虚拟总线 | 仅支持非虚拟总线 |
| 部分结构体 | 支持虚拟和非虚拟总线 | 仅支持非虚拟总线 |

### 字符串支持

Delay 模块仅在以下情况下可以接受并输出 string 数据类型：

- 模块配置为 **Initial condition** 参数的默认值 (0)。
- **Delay length** 值为 1 或更小。
