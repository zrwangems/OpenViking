---
type: simulink-block
title: 'Delay'
family: discrete
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'delay'
---

# Delay

Delay input signal by fixed or variable sample periods

## 中文

按固定或可变采样周期延迟输入信号

### 所属库

Simulink / Commonly Used Blocks Simulink / Discrete DSP System Toolbox / Signal Operations HDL Coder / Commonly Used Blocks HDL Coder / Discrete

### 描述

Delay 模块会在一段延迟之后再输出模块的输入。此模块根据**延迟长度**参数的值来确定延迟时间。此模块支持：

- 可变延迟长度
- 来自输入端口的初始条件的规范
- 状态存储
- 使用环形缓冲区而不是数组缓冲区来存储状态
- 用外部重置信号重置初始条件的状态
- 利用外部使能信号控制模块在每一时间步的执行

初始模块输出取决于几个因素，例如**初始条件**参数和仿真开始时间等。有关详细信息，请参阅初始模块输出。**外部重置**参数确定模块输出是否在触发时重置为初始条件。**显示使能端口**参数确定是否由外部使能信号控制每一时间步的模块执行。

#### 初始模块输出

在仿真的前几个时间步的输出取决于模块的采样时间、延迟长度和仿真开始时间。此模块支持指定或继承离散采样时间，以确定采样之间的时间间隔。有关详细信息，请参阅指定采样时间。

下表显示了 Delay 模块在采用以下设置时前几个时间步的输出。模块继承离散采样时间 `[Tsampling,Toffset]`，其中 `Tsampling` 是采样周期，`Toffset` 是初始时间偏移量。*`n`* 是**延迟长度**参数的值，`Tstart` 是模型的仿真开始时间。

| 仿真时间范围 | 模块输出 |
| --- | --- |
| `(Tstart)` 到 `(Tstart + Toffset)` | 零 |
| `(Tstart + Toffset)` 到 `(Tstart + Toffset + n * Tsampling)` | **初始条件**参数 |
| 在 `(Tstart + Toffset + n * Tsampling)` 之后 | 输入信号 |

#### 使用外部使能信号时的行为

选中**显示使能端口**复选框将启用 Enable 端口。如果启用了使能端口，则该模块将按以下顺序运行：

1. 检查是否满足使能条件。
2. 如果启用了重置端口，将检查重置条件。
3. 执行 Delay 模块功能。

该模块通过 Enable 端口执行以下操作：

- 当出现第一个模块使能信号时，模块输出是初始条件值 (`x0`)。
- 对于连续的使能信号，该模块取输入信号 u 的最后一个状态。
- 如果端口在仿真开始时未启用，则 Delay 模块输出 `0`。
- 在仿真期间，如果端口在启用后变为禁用，则该模块不执行并保持其最后值。

#### 可变大小支持

Delay 模块为可变大小信号提供下列支持：

- 数据输入端口 `u` 接受可变大小信号。其他输入端口不接受可变大小信号。
- 对于可变大小输入，输出端口与数据输入端口 `u` 具有相同的信号维度。

对可变大小信号应用的规则取决于 Delay 模块的输入处理模式。

| 输入处理模式 | 对可变大小信号的支持规则 |
| --- | --- |
| **元素作为通道(基于采样)** | - 信号维度仅在启用模块时的状态重置期间发生变化。 - 初始条件必须为标量。 |
| **列作为通道(基于帧)** | - 不支持 |

#### 总线支持

Delay 模块为总线信号提供下列支持：

- 数据输入 `u` 接受虚拟和非虚拟总线信号。除了输入端口 `x0`，其他输入端口不接受总线信号。
- 初始条件 `x0` 端口接受非虚拟总线信号。
- 对于总线输入，输出端口与数据输入端口 `u` 具有相同的总线类型。
- 总线使用：

  - 基于采样和基于帧的处理
  - 固定和可变延迟长度
  - 数组和环形缓冲区

要使用总线信号作为 Delay 模块的输入，请在对话框中或通过 `x0` 端口指定初始条件。对虚拟和非虚拟总线的支持取决于您指定的初始条件，以及**状态名称**参数是否为空。对于 `x0` 输入端口，仅支持非虚拟总线。

| 初始条件 | 状态名称 | |
| --- | --- | --- |
| 空 | 非空 |
| 零 | 支持虚拟和非虚拟总线 | 仅支持非虚拟总线 |
| 非零标量 | 支持虚拟和非虚拟总线 | 不支持总线 |
| 非标量 | 不支持总线 | 不支持总线 |
| 结构体 | 支持虚拟和非虚拟总线 | 仅支持非虚拟总线 |
| 非完全结构体 | 支持虚拟和非虚拟总线 | 仅支持非虚拟总线 |

#### 字符串支持

仅在以下情况下，Delay 模块才接受和输出字符串数据类型：

- 模块配置为采用**初始条件**参数的默认值 (0)。
- **延迟长度**值等于或小于 1。

### 端口

#### 输入

#### **u** — 数据输入信号 标量 | 向量

根据参数设置延迟的输入数据信号。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`

#### **d** — 延迟长度 标量

指定为从输入端口继承的延迟长度。当您对**延迟长度:源**参数选择**输入端口**时启用。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `fixed point`

#### **Enable** — 外部使能信号 标量

使能信号，用于启用或禁用模块的执行。要创建此端口，请选择**显示使能端口**参数。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **External reset** — 外部重置信号 标量

将模块的执行重置为初始状态的外部信号。要创建此端口，请选择**外部重置**参数。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **x0** — 初始条件 标量 | 向量

指定为从输入端口继承的初始条件。当您对**初始条件:源**参数选择**输入端口**时启用。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量

输出信号，它是按参数**延迟长度**指定的时间长度延迟后的输入信号。输出信号的初始值取决于几个条件。请参阅初始模块输出。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 参数

#### 常设

#### **延迟长度** — 延迟长度 **对话框** (默认) | **输入端口**

指定是直接在对话框中输入延迟长度（固定延迟），还是从输入端口继承（可变延迟）。

- 如果将**源**设置为**对话框**，请在**值**下面的编辑框中输入延迟长度。
- 如果将**源**设置为**输入端口**，请验证上游信号为 `d` 输入端口提供了延迟长度。您还可以通过指定参数**上限**来指定其最大值。

将标量延迟长度指定为非负实数整数。如果对话框中的值（固定延迟）超出范围或者为非整数，将返回错误。如果来自输入端口的值（可变延迟）超出范围，将被转换为位于范围之内的值。如果来自输入端口的值（可变延迟）为非整数，将截断为整数。

##### 编程用法

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

#### **初始条件** — 初始条件 **对话框** (默认) | **输入端口**

指定是直接在对话框中输入初始条件，还是从输入端口继承初始条件。

- 如果将**源**设置为**对话框**，请在**值**下面的编辑框中输入初始条件。
- 如果将**源**设置为**输入端口**，请验证上游信号为 `x0` 输入端口提供了初始条件。

Simulink® 使用舍入到最邻近值运算和饱和处理，将**初始条件**的数据类型脱机转换为输入信号 `u` 的数据类型。

**注意**

如果选中了**状态属性**窗格上的**状态名称必须解析为 Simulink 信号对象**，模块会将信号对象的初始值复制到**初始条件**参数中。但是，如果**初始条件**的源是**输入端口**，模块将忽略信号对象的初始值。

##### 编程用法

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

#### **输入处理** — 指定基于采样或基于帧的处理 **元素作为通道(基于采样)** (默认) | **列作为通道(基于帧)**

指定模块是执行基于采样还是基于帧的处理：

- **列作为通道(基于帧)** - 将输入信号的每一列视为一个单独的通道（基于帧的处理）。

  **注意**

  基于帧的处理需要具有 DSP System Toolbox™ 许可证。

  有关详细信息，请参阅Sample- and Frame-Based Concepts (DSP System Toolbox)。
- **元素作为通道(基于采样)** - 将输入信号的每个元素视为一个单独的通道（基于采样的处理）。

可以使用**输入处理**指定模块是执行基于采样的处理还是基于帧的处理。有关这两种处理模式的详细信息，请参阅Sample- and Frame-Based Concepts (DSP System Toolbox)。

##### 编程用法

|  |
| --- |
| **模块参数**：`InputProcessing` |
| **类型**：字符向量 |
| **值**：`'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **默认值**：`'Elements as channels (sample based)'` |

#### **使用环形缓冲区保存状态** — 存储状态的环形缓冲区 `off` (默认) | `on`

选择在仿真和代码生成时使用环形缓冲区来存储状态。在其他情况下，则使用数组缓冲区来存储状态。

当延迟长度值很大时，使用环形缓冲区可以提高执行速度。对于数组缓冲区，复制操作的数量随着延迟长度的增加而增加。对于环形缓冲区，不管延迟长度如何增加，复制操作的数量保持不变。

如果符合下列任一条件，都应使用数组缓冲区来存储状态，因为环形缓冲区不会提高执行速度。

- 对于基于采样的信号，延迟长度为 1。
- 对于基于帧的信号，延迟长度不大于帧大小。

##### 编程用法

|  |
| --- |
| **模块参数**：`UseCircularBuffer` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

#### **防止直接馈通** — 防止直接馈通 `off` (默认) | `on`

对于**输入处理**模式，选择此项可将延迟长度从零增加到下限值。

- 对于基于采样的信号，将最小延迟长度增加到 1。
- 对于基于帧的信号，将最小延迟长度增加到帧的长度。

选中此复选框可防止从输入端口 `u` 到输出端口的直接馈通。但是，此复选框无法阻止从初始条件端口 `x0` 到输出端口的直接馈通。

##### 依赖关系

要启用此参数，请将**延迟长度:源**设置为**输入端口**时，此复选框可用。

##### 编程用法

|  |
| --- |
| **模块参数**：`PreventDirectFeedthrough` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

#### **在生成代码中去除延迟长度检查** — 删除延迟长度超出范围检查 `off` (默认) | `on`

选择此选项可删除用来检查超出范围的延迟长度的代码。

| 复选框 | 结果 | 何时使用 |
| --- | --- | --- |
| 选中 | 生成的代码中未包含用来检查超出范围的延迟长度的条件语句。 | 提高代码效率 |
| 清除 | 生成的代码中包含检查超范围延迟长度的条件语句。 | 适用于安全性至关重要的应用领域 |

##### 依赖关系

要启用此参数，请将**延迟长度:源**设置为**输入端口**时，此复选框可用。

##### 编程用法

|  |
| --- |
| **模块参数**：`RemoveDelayLengthCheckInGeneratedCode` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

#### **延迟长度的诊断** — 延迟长度的诊断检查 **无** (默认) | **警告** | **错误**

指定当输入 `d` 小于下限或大于**延迟长度:上限**时是否生成警告或错误。下限取决于**防止直接馈通**的设置。

- 如果清除此复选框，则下限为零。
- 如果选中此复选框，对于基于采样的信号，下限为 1；对于基于帧的信号，下限为帧的长度。

诊断选项包括：

- `None` - Simulink 软件不执行任何操作。
- `Warning` - Simulink 软件显示警告并继续进行仿真。
- `Error` - Simulink 软件终止仿真并显示错误。

##### 依赖关系

要启用此参数，请将**延迟长度:源**设置为**输入端口**时，此复选框可用。

##### 编程用法

|  |
| --- |
| **模块参数**：`DiagnosticForDelayLength` |
| **类型**：字符向量 |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'None'` |

#### **显示使能端口** — 创建使能端口 `off` (默认) | `on`

此选项使用使能端口来控制此模块的执行。当此端口的输入非零时，模块被视为启用；当输入为 `0` 时，模块被视为禁用。输入的值在执行模块的同一时间步进行检查。

##### 编程用法

|  |
| --- |
| **模块参数**：`ShowEnablePort` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **外部重置** — 外部状态重置 **无** (默认) | **上升沿** | **下降沿** | **任一沿** | **电平** | **电平保持**

指定用于将状态重置为初始条件的触发事件。

| 重置模式 | 行为 |
| --- | --- |
| **无** | 不重置。 |
| **上升沿** | 基于上升沿重置。 |
| **下降沿** | 基于下降沿重置。 |
| **任一沿** | 基于上升或下降沿重置。 |
| **电平** | 在下列任一情况下重置：  - 当重置信号在当前时间步为非零值时 - 当重置信号值从上一时间步的非零更改为当前时间步的零时 |
| **电平保持** | 当重置信号在当前时间步为非零值时重置 |

##### 编程用法

|  |
| --- |
| **模块参数**：`ExternalReset` |
| **类型**：字符向量 |
| **值**：`'None'` | `'Rising'` | `'Falling'` | `'Either'` | `'Level'` | `'Level hold'` |
| **默认值**：`'None'` |

#### **采样时间(-1 表示继承)** — 采样时间命中点之间的离散间隔 `-1` (默认) | `scalar`

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。此模块支持离散采样时间，但不支持连续采样时间。

##### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：实数标量 |
| **默认值**：`'-1'` |

#### 状态属性

#### **状态名称** — 模块状态的唯一名称 `''` (默认) | 字母数字字符串

使用此参数为模块状态指定唯一名称。默认值为 `' '`。如果此字段为空，则表示未指定任何名称。使用此参数时，请记住以下注意事项：

- 有效的标识符以字母或下划线字符开始，后跟字母数字或下划线字符。
- 状态名称仅适用于所选模块。

当您点击**应用**时，此参数将启用**状态名称必须解析为 Simulink 信号对象**。

有关详细信息，请参阅模型接口元素的 C 数据代码接口配置 (Simulink Coder)。

##### 编程用法

|  |
| --- |
| **模块参数**：`StateName` |
| **类型：**字符向量 |
| **值：**唯一名称 |
| **默认值：**`''` |

#### **状态名称必须解析为 Simulink 信号对象** — 要求将状态名称解析为信号对象 `off` (默认) | `on`

选中此复选框会要求将状态名称解析为 Simulink 信号对象。

##### 依赖关系

要启用此参数，请为**状态名称**指定值。仅当将模型配置参数**信号解析**设置为除**无**以外的值时，才会显示此参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`StateMustResolveToSignalObject` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

### 模块特性

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

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

生成的代码在特定条件下依赖于 `memcpy` 或 `memset` 函数 (`string.h`)。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的配置选项。

| 模块参数设置 | 描述 |
| --- | --- |
| 将**外部重置**设置为**电平**。 | 在 HDL 代码中生成重置端口。 |
| 选择**显示使能端口**。 | 在 HDL 代码中生成使能端口。 |
| 对于**初始条件**，将**源**设置为**对话框**，并输入值。 | 指定模块的初始条件。 |
| 将**输入处理**设置为**列作为通道(基于帧)** 或**元素作为通道(基于采样)**。 | 需要向量输入数据，其中向量的每个元素表示一个时间点上的采样。 |

**使用 State Control 模块时的附加设置**

如果您要在一个 Simulink 模型子系统中结合使用 State Control 模块和 Delay 模块，请使用以下附加设置。

| 模块参数设置 | 描述 |
| --- | --- |
| 将**同步**模式下的**外部重置**设置为**电平保持**，并设置 State Control 模块的**典型**模式的**电平**。 | 在 HDL 代码中生成重置端口。 |
| 对于具有外部使能端口的 Delay 模块，将**延迟长度**设置为零。 | 仅在 State Control 模块的**同步**模式下视为一条线。 |
| 对于具有外部重置端口的 Delay 模块，将**延迟长度**设置为零。 | 在 State Control 模块的**同步**和**典型**模式下视为一条线。 |

有关 State Control 模块的详细信息，请参阅State Control (HDL Coder)。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **AllowDelayDistribution** | 允许在分布式流水线和延迟吸收优化期间分布或吸收延迟。默认值为 **inherit**。有关详细信息，请参阅AllowDelayDistribution (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |
| **ResetType** | 隐藏重置逻辑生成。默认值为**默认**，它生成重置逻辑。另请参阅ResetType (HDL Coder)。 |
| **UseRAM** | 将延迟映射到 RAM 而不是寄存器。默认值为 **off**。另请参阅UseRAM (HDL Coder)。 |

**可变整数延迟支持**

- 您可以为通过**输入端口**设置**延迟长度**的 Delay 模块生成 HDL 代码。输入延迟长度可以是整数类型或浮点类型。
- 代码生成在 Delay 模块的 'd' 端口支持正整数值。通过输入端口设置的延迟长度必须在 `0` 和 `Upper limit` 之间，在“模块参数”对话框中指定。
- 对于负延迟长度值，HDL Coder 将这些负延迟长度转换为 `0`。
- 同样，如果您指定的延迟长度大于上限，HDL Coder 会将延迟长度转换为 `Upper limit` 值。
- 上限范围由延迟长度输入数据类型的范围定义。例如，如果将延迟长度输入数据类型指定为 `uint8`，则上限不能超过 `255`。
- 对于 Variable Integer Delay 模块，您可以使用使能端口和重置端口。

**复数数据支持**

此模块支持复信号的代码生成。

**使用结构体作为初始值**

您可以为 Delay 模块生成 HDL 代码，以使用结构体来指定 Delay 模块的初始条件。当对模型中的 Delay 模块使用总线输入时，您可以用结构体值设置 Delay 模块的初始条件以初始化总线延迟。

要指定由结构体定义的初始条件，请执行以下操作：

1. 在模型工作区、MATLAB® 基础工作区、封装工作区或 Simulink 数据字典中定义一个结构体。
2. 将初始条件值赋给此结构体。
3. 将**初始条件**参数设置为**对话框**，并在**值**字段中输入结构体。

您还可以在其他 Delay 模块中使用结构体作为初始值，包括 Unit Delay 和 Tapped Delay 模块

**限制**

- 对于**初始条件**，HDL 代码生成不支持将**源**设置为**输入端口**。
- HDL 代码生成仅在重置端口和使能端口上支持布尔数据类型。
- 通过**输入端口**设置**延迟长度**的 Delay 模块不支持 RAM 映射的 HDL 模块属性 **UseRAM**。
- 通过**输入端口**设置**延迟长度**的 Delay 模块不支持 HDL 代码生成的总线和矩阵数据输入。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Commonly Used Blocks Simulink / Discrete DSP System Toolbox / Signal Operations HDL Coder / Commonly Used Blocks HDL Coder / Discrete

## Description

The Delay block outputs the input of the block after a delay. The block
determines the delay time based on the value of the **Delay length**
parameter. The block supports:

- Variable delay length
- Specification of the initial condition from an input port
- State storage
- Using a circular buffer instead of an array buffer for state storage
- Resetting the state to the initial condition with an external reset
  signal
- Controlling execution of the block at every time step with an external enable
  signal

The initial block output depends on several factors such as the **Initial
condition** parameter and the simulation start time. For more information,
see Initial Block Output. The **External reset** parameter
determines if the block output resets to the initial condition on triggering. The
**Show enable port** parameter determines if the block execution is
controlled in every time step by an external enable signal.

### Initial Block Output

The output in the first few time steps of the simulation depends on the block
sample time, the delay length, and the simulation start time. The block supports
specifying or inheriting discrete sample times to determine the time interval
between samples. For more information, see Specify Sample Time.

The table shows the Delay block output for the first few time steps with these
settings. The block inherits a discrete sample time as
`[Tsampling,Toffset]`,
where `Tsampling` is the sampling period
and `Toffset` is the initial time
offset. *`n`* is the value of the **Delay
length** parameter and
`Tstart` is the simulation start
time for the model

| Simulation Time Range | Block Output |
| --- | --- |
| `(Tstart)` to `(Tstart + Toffset)` | Zero |
| `(Tstart + Toffset)` to `(Tstart + Toffset + n * Tsampling)` | **Initial condition** parameter |
| After `(Tstart + Toffset + n * Tsampling)` | Input signal |

### Behavior with External Enable Signal

Selecting the **Show enable port** check box enables the Enable
port. If the enable port is enabled, the block operates in this order

1. Checks if the enable condition is satisfied.
2. If the reset port is enabled, checks the reset condition.
3. Performs the Delay block functionality.

The block has this operation with the Enable port:

- At the first block enable, the block output is the initial condition value
  (`x0`).
- For consecutive enable signals, the block takes the last state of the
  input signal u.
- If the port is not enabled at the start of simulation, the
  Delay block outputs `0`.
- During simulation, if the port becomes disabled after having been enabled,
  the block does not execute and holds its last value.

### Variable-Size Support

The Delay block provides the following support for variable-size
signals:

- The data input port `u` accepts variable-size signals.
  The other input ports do not accept variable-size signals.
- The output port has the same signal dimensions as the data input port
  `u` for variable-size inputs.

The rules that apply to variable-size signals depend on the input processing mode
of the Delay block.

| Input Processing Mode | Rules for Variable-Size Signal Support |
| --- | --- |
| `Elements as channels (sample based)` | - The signal dimensions change only during state reset   when the block is enabled. - The initial condition must be scalar. |
| `Columns as channels (frame based)` | - No support |

### Bus Support

The Delay block provides the following support for bus
signals:

- The data input `u` accepts virtual and nonvirtual bus
  signals. Other than input port `x0`, the other input ports
  do not accept bus signals.
- The initial condition `x0` port accepts nonvirtual bus
  signals.
- The output port has the same bus type as the data input port
  `u` for bus inputs.
- Buses work with:

  - Sample-based and frame-based processing
  - Fixed and variable delay length
  - Array and circular buffers

To use a bus signal as the input to a Delay block, specify the
initial condition on the dialog box or through the `x0` port.
Support for virtual and nonvirtual buses depends on the initial condition that you
specify and whether the **State name** parameter is empty or not.
For the `x0` input port, only nonvirtual buses are
supported.

| Initial Condition | State Name | |
| --- | --- | --- |
| Empty | Not Empty |
| Zero | Virtual and nonvirtual bus support | Nonvirtual bus support only |
| Nonzero scalar | Virtual and nonvirtual bus support | No bus support |
| Nonscalar | No bus support | No bus support |
| Structure | Virtual and nonvirtual bus support | Nonvirtual bus support only |
| Partial structure | Virtual and nonvirtual bus support | Nonvirtual bus support only |

### String Support

The Delay block can accept and output string data type only
if:

- The block is configured for the default value of the **Initial
  condition** parameter (0).
- The **Delay length** value is 1 or less.

## Ports

### Input

### **u** — Data input signal scalar | vector

Input data signal delayed according to parameters settings.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **d** — Delay length scalar

Delay length specified as inherited from an input port. Enabled when
you select the **Delay length: Source** parameter as
`Input port`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Enable** — External enable signal scalar

Enable signal that enables or disables execution of the block. To
create this port, select the **Show enable port**
parameter.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **External reset** — External reset signal scalar

External signal that resets execution of the block to the initial
condition. To create this port, select the **External
reset** parameter.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **x0** — Initial condition scalar | vector

Initial condition specified as inherited from an input port. Enabled
when you select the **Initial Condition: Source**
parameter as `Input port`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal that is the input signal delayed by the length of time
specified by the parameter **Delay length**. The
initial value of the output signal depends on several conditions. See
Initial Block Output.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### Main

### **Delay length** — Delay length `Dialog` (default) | `Input port`

Specify whether to enter the delay length directly on the dialog box
(fixed delay) or to inherit the delay from an input port (variable
delay).

- If you set **Source** to
  `Dialog`, enter the delay length in
  the edit field under **Value**.
- If you set **Source** to `Input
  port`, verify that an upstream signal supplies
  a delay length for the `d` input port. You can
  also specify its maximum value by specifying the parameter
  **Upper limit**.

Specify the scalar delay length as a real, nonnegative integer. The
maximum delay length varies. It is determined by the equation:
*delay\_length* < *2147483647* /
(*bytes\_per\_element* \*
*number\_of\_elements*), where the maximum value that
can be held by an integer type (`intmax`) is
`2147483647`. For example, if the following is
true:

- *number\_of\_elements* =
  `1`
- *bytes\_per\_element* =
  `8`

Then the maximum allowed delay length must be less than
`2147483647/(1 * 8)`, which is
`268435455`. If the delay length is
`268435456` or greater, the block returns an error
message like this:

```
Error:In block  'untitled/Delay', total memory requested
for state is larger than the maximum supported number,
which is '2147483647' bytes for simulation.
To avoid this error, please decrease the value of 'DelayLength'.
```

An out-of-range or noninteger value in the dialog box (fixed delay)
returns an error. An out-of-range value from an input port (variable
delay) casts it into the range. A noninteger value from an input port
(variable delay) truncates it to the integer.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DelayLengthSource` |
| **Type**: character vector |
| **Values**: `'Dialog'` | `'Input port'` |
| **Default**: `'Dialog'` |

|  |
| --- |
| **Block Parameter**: `DelayLength` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'2'` |

|  |
| --- |
| **Block Parameter**: `DelayLengthUpperLimit` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'100'` |

### **Initial condition** — Initial condition `Dialog` (default) | `Input port`

Specify whether to enter the initial condition directly on the dialog
box or to inherit the initial condition from an input port.

- If you set **Source** to
  `Dialog`, enter the initial
  condition in the edit field under
  **Value**.
- If you set **Source** to `Input
  port`, verify that an upstream signal supplies
  an initial condition for the `x0` input
  port.

Simulink® converts offline the data type of **Initial
condition** to the data type of the input signal
`u` using a round-to-nearest operation and
saturation.

**Note**

When **State name must resolve to Simulink signal
object** is selected on the **State
Attributes** pane, the block copies the initial value
of the signal object to the **Initial condition**
parameter. However, when the source for **Initial
condition** is `Input port`,
the block ignores the initial value of the signal object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InitialConditionSource` |
| **Type**: character vector |
| **Values**: `'Dialog'` | `'Input port'` |
| **Default**: `'Dialog'` |

|  |
| --- |
| **Block Parameter**: `InitialCondition` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'0.0'` |

### **Input processing** — Specify sample- or frame-based processing `Elements as channels (sample based)` (default) | `Columns as channels (frame based)`

Specify whether the block performs sample- or frame-based processing:

- `Columns as channels (frame based)` — Treat
  each column of the input as a separate channel (frame-based processing).

  **Note**

  Frame-based processing requires a DSP System Toolbox™ license.

  For more information, see Sample- and Frame-Based Concepts (DSP System Toolbox).
- `Elements as channels (sample based)` — Treat
  each element of the input as a separate channel (sample-based
  processing).

Use **Input processing** to specify whether the block performs
sample- or frame-based processing. For more information about these two processing
modes, see Sample- and Frame-Based Concepts (DSP System Toolbox).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InputProcessing` |
| **Type**: character vector |
| **Values**: `'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **Default**: `'Elements as channels (sample based)'` |

### **Use circular buffer for state** — Circular buffer for storing state `off` (default) | `on`

Select to use a circular buffer for storing the state in simulation
and code generation. Otherwise, an array buffer stores the state.

Using a circular buffer can improve execution speed when the delay
length is large. For an array buffer, the number of copy operations
increases as the delay length goes up. For a circular buffer, the number
of copy operations is constant for increasing delay length.

If one of the following conditions is true, an array buffer always
stores the state because a circular buffer does not improve execution
speed.

- For sample-based signals, the delay length is 1.
- For frame-based signals, the delay length is no larger than
  the frame size.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `UseCircularBuffer` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Prevent direct feedthrough** — Prevent direct feedthrough `off` (default) | `on`

Select to increase the delay length from zero to the lower limit for
the **Input processing** mode.

- For sample-based signals, increase the minimum delay length to
  1.
- For frame-based signals, increase the minimum delay length to
  the frame length.

Selecting this check box prevents direct feedthrough from the input
port, `u`, to the output port. However, this check box
cannot prevent direct feedthrough from the initial condition port,
`x0`, to the output port.

#### Dependency

To enable this parameter, set **Delay length:
Source** to `Input
port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PreventDirectFeedthrough` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Remove delay length check in generated code** — Remove delay length out-of-range check `off` (default) | `on`

Select to remove code that checks for out-of-range delay
length.

| Check Box | Result | When to Use |
| --- | --- | --- |
| Selected | Generated code does not include conditional statements to check for out-of-range delay length. | For code efficiency |
| Cleared | Generated code includes conditional statements to check for out-of-range delay length. | For safety-critical applications |

#### Dependency

To enable this parameter, set **Delay length:
Source** to `Input
port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `RemoveDelayLengthCheckInGeneratedCode` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Diagnostic for delay length** — Diagnostic checks for delay length `None` (default) | `Warning` | `Error`

Specify whether to produce a warning or error when the input
`d` is less than the lower limit or greater than
the **Delay length: Upper limit**. The lower limit
depends on the setting for **Prevent direct
feedthrough**.

- If the check box is cleared, the lower limit is zero.
- If the check box is selected, the lower limit is 1 for
  sample-based signals and frame length for frame-based
  signals.

Options for the diagnostic include:

- `None` — Simulink software takes no action.
- `Warning` — Simulink software displays a warning and continues the
  simulation.
- `Error` — Simulink software terminates the simulation and displays an
  error.

#### Dependency

To enable this parameter, set **Delay length:
Source** to `Input
port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DiagnosticForDelayLength` |
| **Type**: character vector |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'None'` |

### **Show enable port** — Create enable port `off` (default) | `on`

Select to control execution of this block with an enable port. The block is considered
enabled when the input to this port is nonzero, and is disabled when the input is
`0`. The value of the input is checked at the same time step as the
block execution.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowEnablePort` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **External reset** — External state reset `None` (default) | `Rising` | `Falling` | `Either` | `Level` | `Level hold`

Specify the trigger event to use to reset the states to the initial conditions.

| Reset Mode | Behavior |
| --- | --- |
| `None` | No reset |
| `Rising` | Reset on a rising edge |
| `Falling` | Reset on a falling edge |
| `Either` | Reset on either a rising or falling edge |
| `Level` | Reset in either of these cases:  - When the reset signal is nonzero at the current time   step - When the reset signal value changes from nonzero at the   previous time step to zero at the current time step |
| `Level hold` | Reset when the reset signal is nonzero at the current time step |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ExternalReset` |
| **Type**: character vector |
| **Values**: `'None'` | `'Rising'` | `'Falling'` | `'Either'` | `'Level'` | `'Level hold'` |
| **Default**: `'None'` |

### **Sample time (-1 for inherited)** — Discrete interval between sample time hits `-1` (default) | `scalar`

Specify the time interval between samples. To inherit the sample time,
set this parameter to `-1`. This block supports
discrete sample time, but not continuous sample time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Value**: real scalar |
| **Default**: `'-1'` |

### State Attributes

### **State name** — Unique name for block state `''` (default) | alphanumeric string

Use this parameter to assign a unique name to the block state. The default is `' '`. When this field is blank, no name is assigned. When using this parameter, remember these considerations:

- A valid identifier starts with an alphabetic or underscore character, followed by alphanumeric or underscore characters.
- The state name applies only to the selected block.

This parameter enables **State name must resolve to Simulink signal object** when you click **Apply**.

For more information, see C Data Code Interface Configuration for Model Interface Elements (Simulink Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateName` |
| **Type:** character vector |
| **Values:** unique name |
| **Default:** `''` |

### **State name must resolve to Simulink signal object** — Require state name resolve to a signal object `off` (default) | `on`

Select this check box to require that the state name resolves to a Simulink signal object.

#### Dependencies

To enable this parameter, specify a value for **State name**. This parameter appears only if you set the model configuration parameter **Signal resolution** to a value other than `None`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateMustResolveToSignalObject` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `image` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `noa` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Direct feedthrough characteristics for this block depend on block parameter values. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on `memcpy` or
`memset` functions (`string.h`) under
certain conditions.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides configuration options that affect HDL implementation and
synthesized logic.

| Block Parameter Setting | Description |
| --- | --- |
| Set **External reset** to `Level`. | Generates a reset port in the HDL code. |
| Select **Show enable port**. | Generates an enable port in the HDL code. |
| For **Initial condition**, set **Source** to `Dialog` and enter the value. | Specifies an initial condition for the block. |
| Set **Input processing** to `Columns as channels (frame based)` or `Elements as channels (sample based)`. | Expects vector input data, where each element of the vector represents a sample in time. |

**Additional Settings When Using State Control Block**

If you use a State Control block with the Delay
block inside a subsystem in your Simulink model, use these additional settings.

| Block Parameter Setting | Description |
| --- | --- |
| Set **External reset** to `Level hold` for `Synchronous` mode and `Level` for `Classic` mode of the State Control block. | Generates a reset port in the HDL code. |
| Set **Delay length** to zero for a Delay block with an external enable port. | Treated as a wire in only `Synchronous` mode of the State Control block. |
| Set **Delay length** to zero for a Delay block with an external reset port. | Treated as a wire in `Synchronous` and `Classic` modes of the State Control block. |

For more information about the State Control block, see State Control (HDL Coder).

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **AllowDelayDistribution** | Allow delay to be distributed or absorbed during the distributed pipelining and delay absorption optimizations. The default is `inherit`. For more details, see AllowDelayDistribution (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **ResetType** | Suppress reset logic generation. The default is `default`, which generates reset logic. See also ResetType (HDL Coder). |
| **UseRAM** | Map delays to RAM instead of registers. The default is `off`. See also UseRAM (HDL Coder). |

**Variable Integer Delay Support**

- You can generate HDL code for the Delay block that has
  **Delay Length** set through the
  `Input port`. Input delay length can be
  integer types or floating-point types.
- The code generation supports positive integer values at the 'd' port
  of the delay block. The delay length set through the input port must be
  between `0` and `Upper limit`,
  specified in the Block Parameters dialog box.
- For negative delay length values, HDL Coder translates these negative delay length to
  `0`.
- Similarly, if you specify delay length greater than the upper limit,
  HDL Coder translates the delay length to the `Upper
  limit` value.
- Upper limit range is defined by the range of the delay length input
  data type. For example, if you specify delay length input data type as
  `uint8`, then the upper limit must not exceed
  `255`.
- You can use enable and reset ports for the variable integer Delay
  block.

**Complex Data Support**

This block supports code generation for complex signals.

**Use Structures as Initial Values**

You can generate HDL code for Delay blocks that use structures to specify the
initial conditions for the Delay block. When you use bus input for a Delay block
in your model, you can set initial condition for the delay block with a
structure value to initialize the bus delay.

To specify initial conditions defined by structures:

1. Define a structure in the model workspace, MATLAB® base workspace, mask workspace, or Simulink data dictionary.
2. Assign the initial condition value to this structure.
3. Set the **Initial Condition** parameter to
   `Dialog` and input the structure in the
   **Value** field.

You also use structures as the initial values in other delay blocks, including the Unit Delay and Tapped Delay blocks

**Restrictions**

- For **Initial condition**,
  **Source** set to `Input
  port` is not supported for HDL code
  generation.
- HDL code generation supports only the Boolean data type at the
  Reset and Enable ports.
- HDL Block Property **UseRAM** for RAM mapping is
  not supported for Delay block that has **Delay
  Length** set through the `Input
  port`.
- The Delay block that has **Delay Length**
  set through the `Input port` does not
  support bus and matrix data input for HDL code generation.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
