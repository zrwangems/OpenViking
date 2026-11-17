---
type: simulink-block
title: 'Subsystem'
family: 'wireless-hdl'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: ''
documentation_page: 'subsystem'
documentation_source_path: '../simulink/slref/subsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Subsystem

## 端口

### 输入

### **In** — 子系统的信号输入 标量 | 向量 | 矩阵 | 数组 | 总线

在子系统中放置诸如 Inport 或 In Bus Element 模块会向 Subsystem 模块添加一个外部输入端口。

使用 Inport 或 In Bus Element 模块从局部环境获取信号。

有关详细信息，请参阅 Connect Subsystems。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
**复数支持：** 是

### **reinit** — 子系统重新初始化事件的控制信号 标量

重新初始化事件端口提供一个函数调用控制信号，该信号触发子系统重新初始化事件，从而重置子系统的状态。

子系统必须包含一个 Reinitialize Function 模块，与每个子系统重新初始化事件相对应。要指定端口名称，请使用 Reinitialize Function 模块中 Event Listener 模块的 **Event name** 参数。有关详细信息，请参阅 Reinitialize States of Blocks in Subsystem。

#### 依赖关系

要启用此端口，请选择 **Treat as atomic unit**，然后选择 **Show subsystem reinitialize ports**。
### 输出

### **Out** — 子系统的信号输出 标量 | 向量 | 矩阵 | 数组 | 总线

在子系统中放置诸如 Outport 或 Out Bus Element 模块会从 Subsystem 模块添加一个输出端口。

使用 Outport 或 Out Bus Element 模块向局部环境发送信号。

有关详细信息，请参阅 Connect Subsystems。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
**复数支持：** 是

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **Show port labels** — 端口标签的显示选项 `FromPortIcon`（默认）| `FromPortBlockName` | `SignalName` | `none`

选择如何在 Subsystem 模块图标上显示端口标签。

- `none` — 不显示端口标签。
- `FromPortIcon` — 如果对应的端口图标显示信号名称，则在 Subsystem 模块上显示该信号名称。否则，显示端口模块名称，或者如果模块名称为默认名称，则显示端口编号。
- `FromPortBlockName` — 在 Subsystem 模块上显示对应端口模块的名称。
- `SignalName` — 如果连接到该端口的信号已命名，则在 Subsystem 模块上显示该信号名称。否则，显示对应端口模块的名称。

有关 Subsystem 模块上的端口标签编辑，请参阅 Edit Port Labels on Subsystem Blocks。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ShowPortLabels` |
| **值：** | `'FromPortIcon'`（默认）| `'FromPortBlockName'` | `'SignalName'` | `'none'` |

### **Read/Write permissions** — 对子系统内容的访问级别 `ReadWrite`（默认）| `ReadOnly` | `NoReadOrWrite`

控制用户对子系统内容的访问。

- `ReadWrite` — 允许打开和修改子系统内容。
- `ReadOnly` — 允许打开但不允许修改子系统。如果子系统位于模块库中，您可以创建并打开指向该子系统的链接，可以创建和修改子系统的本地副本，但不能更改权限或修改原始库实例的内容。
- `NoReadOrWrite` — 禁止打开或修改子系统。如果子系统位于库中，您可以在模型中创建指向该子系统的链接，但不能打开、修改、更改权限或创建子系统的本地副本。

如果尝试查看 **Read/Write permissions** 参数设置为 `NoReadOrWrite` 的子系统内容，您将不会收到任何响应。例如，双击此类子系统时，软件不会打开该子系统，也不会显示任何消息。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Permissions` |
| **值：** | `'ReadWrite'`（默认）| `'ReadOnly'` | `'NoReadOrWrite'` |

### **Name of error callback function** — 发生错误时要调用的函数名称 无默认值

输入当软件执行子系统期间发生错误时要调用的函数名称。

软件向该函数传递两个参数：子系统的句柄和一个指定错误类型的字符向量。如果未指定函数，则当执行子系统导致错误时，软件会显示一条通用错误消息。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ErrorFcn` |
| **值：** | `''`（默认）| 带引号的函数名称 |
| **数据类型：** | `char` | `string` |

### **Permit hierarchical resolution** — 工作区变量名称的解析方式 `All`（默认）| `ExplicitOnly` | `None`

选择是否解析此子系统引用的工作区变量名称。

有关详细信息，请参阅 Symbol Resolution 和 Symbol Resolution Process。

- `All` — 解析此子系统使用的所有工作区变量名称，包括用于指定模块参数值和 Simulink 数据对象（例如 `Simulink.Signal` 对象）的名称。
- `ExplicitOnly` — 仅解析用于指定模块参数值、数据存储内存（不存在对应模块时）、信号和标记为“must resolve”的状态的工作区变量名称。
- `None` — 不解析任何工作区变量名称。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PermitHierarchicalResolution` |
| **值：** | `'All'`（默认）| `'ExplicitOnly'` | `'None'` |

### **Treat as atomic unit** — 将子系统作为一个单元执行的选项 `off` | `on`

选择此参数会使软件在确定模块方法的执行顺序时将子系统视为一个单元。

- `off` — 在确定模块方法执行顺序时，将子系统中的所有模块视为与子系统处于模型层次结构中的同一级别。这可能导致子系统内模块方法的执行与子系统外模块方法的执行交错进行。
- `on` — 在确定模块方法的执行顺序时将子系统视为一个单元。例如，当需要计算子系统的输出时，软件会先调用子系统内所有模块的输出方法，然后再调用与 Subsystem 模块处于同一级别的其他模块的输出方法。

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `off`。Atomic Subsystem 模块的默认值为 `on`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TreatAsAtomicUnit` |
| **值：** | `'off'` | `'on'` |

### **Show subsystem reinitialize ports** — 显示重新初始化事件端口的选项 `off`（默认）| `on`

选择此参数以显示重新初始化事件端口。清除此参数以移除这些端口。

#### 依赖关系

要启用此参数，请选择 **Treat as atomic unit**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ShowSubsystemReinitializePorts` |
| **值：** | `'off'`（默认）| `'on'` |

### **Minimize algebraic loop occurrences** — 消除人为代数环的选项 `off`（默认）| `on`

尝试消除任何包含原子子系统的人为代数环

- `off` — 不尝试消除任何包含原子子系统的人为代数环。
- `on` — 尝试消除任何包含原子子系统的人为代数环。

#### 依赖关系

要启用此参数，请选择 **Treat as atomic unit**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `MinAlgLoopOccurrences` |
| **值：** | `'off'`（默认）| `'on'` |

### **Schedule as** — 调度类型 `Sample time`（默认）| `Periodic partition` | `Aperiodic partition`

指定如何调度子系统。

- `Sample time` — 指定此子系统中的所有模块必须以相同速率运行还是可以以不同速率运行。
- `Periodic partition` — 将子系统调度为周期性分区。指定分区名称和与分区运行速率对应的采样时间。
- `Aperiodic partition` — 将子系统调度为非周期性分区。指定分区名称。

#### 依赖关系

要启用此参数，请选择 **Treat as atomic unit**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ScheduleAs` |
| **值：** | `'Sample time'`（默认）| `'Periodic partition'` | `'Aperiodic partition'` |

### **Partition name** — 分区名称 无默认值

指定子系统的分区名称。

#### 依赖关系

要启用此参数，请选择 **Treat as atomic unit**，并将 **Schedule as** 设置为 `Periodic partition` 或 `Aperiodic partition`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PartitionName` |
| **值：** | `''`（默认）| 带引号的分区名称 |
| **数据类型：** | `char` | `string` |

### **Sample time** — 时间间隔 `-1`（默认）| `[Ts 0]`

指定此子系统中的所有模块必须以相同速率运行还是可以以不同速率运行。

- `-1` — 继承采样时间。
- `[Ts 0]` — 周期性采样时间。

如果子系统中的模块可以以不同速率运行，请将子系统采样时间指定为继承（`-1`）。

如果所有模块必须以相同速率运行，请将与此速率对应的采样时间指定为 **Sample time** 参数的值。

如果子系统中的任何模块指定了不同的采样时间（`-1` 或 `inf` 除外），软件在更新或仿真模型时会显示错误消息。例如，假设子系统中的所有模块必须以每秒 `5` 次的速率运行。为确保此速率，请将子系统的采样时间指定为 `0.2`。在此示例中，如果子系统中的任何模块指定的采样时间不是 `0.2`、`-1` 或 `inf`，软件在更新或仿真模型时会显示错误。

#### 依赖关系

要启用此参数，请选择 **Treat as atomic unit**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SystemSampleTime` |
| **值：** | `'-1'`（默认）| `'[Ts 0]'` |

### **Treat as grouped when propagating variant conditions** — 传播变体条件时将子系统视为单元的选项 `on`（默认）| `off`

指定软件在从 Variant Source 模块传播变体条件或向 Variant Sink 模块传播变体条件时是否将子系统视为一个单元。

- `on` — 软件在从 Variant Source 模块传播变体条件或向 Variant Sink 模块传播变体条件时将子系统视为一个单元。例如，当软件计算子系统的变体条件时，软件会将该条件传播到子系统中的所有模块。
- `off` — 软件在确定变体条件时，将子系统中的所有模块视为与子系统本身处于模型层次结构中的同一级别。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TreatAsGroupedWhenPropagatingVariantConditions` |
| **值：** | `'on'`（默认）| `'off'` |

#### 依赖关系

要启用此参数，请清除 **Treat as atomic unit** 参数。

### 代码生成

Code Generation 选项卡上的参数需要 Simulink Coder™ 或 Embedded Coder® 许可证。

### **Function packaging** — 代码格式 `Auto` | `Inline` | `Nonreusable function` | `Reusable function`

选择要为原子（非虚拟）子系统生成的代码格式。

- `Auto` — 软件根据模型中存在的子系统类型和实例数量为您选择最佳格式。
- `Inline` — 软件无条件地内联子系统。
- `Nonreusable function` — 如果 **Filename options** 设置为 `Auto`，软件在模型文件中打包单独的函数。如果 **File name options** 设置为 `Use subsystem name`、`Use function name` 或使用不同文件名的 `User specified`，软件在单独的文件中打包单独的函数。

  使用此设置的子系统生成的函数可能带有参数，具体取决于 Function interface 参数设置。您可以分别使用 Function name 和 File name (no extension) 参数来命名生成的函数和文件。这些函数不可重入。
- `Reusable function` — 软件生成带参数的函数，当模型包含子系统的多个实例时允许重用子系统代码。

  此选项还生成带参数的函数，允许在包含跨引用模型中子系统多个实例的模型引用层次结构的生成代码中重用子系统代码。在这种情况下，子系统必须位于库中。

有关详细信息，请参阅：

- 为单个子系统生成代码和可执行文件 (Simulink Coder)
- Generate Inlined Subsystem Code (Simulink Coder)
- 将子系统代码生成为单独的函数和文件 (Simulink Coder)
- 从跨模型共享的库子系统生成可重用代码 (Simulink Coder)

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Reusable function`。

#### 提示

- 当您希望将子系统的多个实例表示为一个可重用函数时，可以将每个实例指定为 `Auto` 或 `Reusable function`。最好只使用其中一种，因为同时使用两者会创建两个可重用函数，每种指定各一个。这些选择的结果仅在无法重用时才有所不同。选择 `Auto` 不允许控制子系统代码的函数或文件名。
- `Reusable function` 和 `Auto` 选项都会尝试确定是否存在子系统的多个实例以及代码是否可以重用。每种选项行为的区别在于当无法重用时的表现：

  - `Auto` 生成内联代码，或者如果情况禁止内联，则为每个子系统实例生成单独的函数。
  - `Reusable function` 为模型中的每个子系统实例生成一个带参数的单独函数。
- 如果您在生成的代码处于源代码控制下时选择 `Reusable function`，请将 **File name options** 设置为 `Use subsystem name`、`Use function name` 或 `User specified`。否则，每当您修改模型时，代码文件的名称都会更改，从而妨碍对文件进行源代码控制。
- 如果您选择的选项不是 `Auto` 或 `Inline`，并且模型配置参数 **States** 已设置，代码生成器会生成单独的输出和更新方法。代码生成器不会考虑 **Combine output and update methods for code generation and simulation** 规范。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证才能进行代码生成。
- 要启用此参数，请选择 **Treat as atomic unit**。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWSystemCode` |
| **值：** | `'Auto'` | `'Inline'` | `'Nonreusable function'` | `'Reusable function'` |

### **Function name options** — 如何命名生成的函数 `Auto` | `Use subsystem name` | `User specified`

选择软件如何为其为子系统生成的函数命名。

如果您拥有 Embedded Coder 许可证，可以使用配置参数 **Code Generation** > **Identifiers** 窗格上的选项来控制函数名称。

- `Auto` — 使用默认命名约定 `model_subsystem()` 分配唯一的函数名称，其中 *`model`* 是模型的名称，*`subsystem`* 是子系统的名称，或者当代码被重用时，是相同子系统的名称。

  如果您为 **Function packaging** 参数选择 `Reusable function`，并且模型引用层次结构包含可重用子系统的多个实例，为了生成子系统的可重用代码，**Function name options** 必须设置为 `Auto`。
- `Use subsystem name` — 使用子系统名称作为函数名称。默认情况下，函数名称使用命名约定 `model_subsystem`。

  当子系统位于库模块中且子系统参数 Function packaging 设置为 `Reusable function` 时，如果您设置 `Use subsystem name` 选项，代码生成器将使用库模块的名称作为子系统函数名称和文件名。
- `User specified` — 启用 **Function name** 字段。输入任何合法的 C 或 C++ 函数名称，该名称必须唯一。

有关详细信息，请参阅 Generate Subsystem Code as Separate Function and Files (Simulink Coder)。

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Use subsystem name`。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFcnNameOpts` |
| **值：** | `'Auto'` | `'Use subsystem name'` | `'User specified'` |

### **Function name** — 子系统代码的函数名称 无默认值

为子系统代码指定一个唯一、合法的 C 或 C++ 函数名称。

如果您想为函数指定特定名称，而不是让 Simulink Coder 代码生成器分配其自动生成的名称或使用子系统名称，请使用此参数。有关详细信息，请参阅 Generate Subsystem Code as Separate Function and Files (Simulink Coder)。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **Function name options** 设置为 `User specified`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFcnName` |
| **值：** | `''`（默认）| 带引号的函数名称 |
| **数据类型：** | `char` | `string` |

### **File name options** — 如何命名生成的文件 `Auto` | `Use subsystem name` | `Use function name` | `User specified`

选择软件如何为其为子系统生成的函数命名单独的文件。

- `Auto` — 根据子系统的配置以及模型中实例的数量，`Auto` 会产生不同的结果。

  - 如果代码生成器*不*为子系统生成单独的文件，则子系统代码生成在从子系统父系统生成的代码模块中。如果子系统父系统是模型本身，则子系统代码生成在 `model.c` 或 `model.cpp` 中。
  - 如果您为 **Function packaging** 参数选择 `Reusable function` 并且生成的代码处于源代码控制下，请考虑指定 `Auto` 以外的 **File name options** 值。这可以防止生成的文件名因无关的模型修改而更改，这对于使用源代码控制来管理配置是有问题的。
  - 如果您为 **Function packaging** 参数选择 `Reusable function`，并且模型引用层次结构包含可重用子系统的多个实例，为了生成子系统的可重用代码，**File name options** 必须设置为 `Auto`。
- `Use subsystem name` — 代码生成器生成一个单独的文件，使用子系统（或库模块）名称作为文件名。

  当 **File name options** 设置为 `Use subsystem name` 时，如果模型包含 Model 模块，或者正在为模型生成模型引用目标，则子系统文件名会被改编。在这些情况下，子系统的文件名由子系统名称加上模型名称前缀组成。
- `Use function name` — 代码生成器使用由 **Function name options** 指定的函数名称作为文件名。
- `User specified` — 此选项启用 **File name (no extension)** 文本输入字段。代码生成器使用您输入的名称作为文件名。输入任何文件名，但不要包含 `.c` 或 `.cpp`（或任何其他）扩展名。此文件名不必唯一。

  虽然子系统源文件名不必唯一，但您必须避免使用导致循环依赖的非唯一名称。例如，`sys_a.h` 包含 `sys_b.h`，`sys_b.h` 包含 `sys_c.h`，而 `sys_c.h` 包含 `sys_a.h`。

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Use function name`。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFileNameOpts` |
| **值：** | `'Auto'` | `'Use subsystem name'` | `'Use function name'` | `'User specified'` |

### **File name (no extension)** — 生成文件的名称 无默认值

您指定的文件名不必唯一。但是，请避免使用导致循环依赖的非唯一名称。例如，`sys_a.h` 包含 `sys_b.h`，`sys_b.h` 包含 `sys_c.h`，而 `sys_c.h` 包含 `sys_a.h`。

有关详细信息，请参阅 Generate Subsystem Code as Separate Function and Files (Simulink Coder)。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **File name options** 设置为 `User specified`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFileName` |
| **值：** | `''`（默认）| 带引号的文件名 |
| **数据类型：** | `char` | `string` |

### **Function interface** — 如何使用生成函数的参数 `void_void`（默认）| `Allow arguments (Optimized)` | `Allow arguments (Match graphical interface)`

选择如何使用生成函数的参数。

- `void_void` — 生成不带参数的函数，并将数据作为全局变量传递。例如：

  ```
  void subsystem_function(void)
  ```
- `Allow arguments (Optimized)` — 生成使用参数而不是将数据作为全局变量传递的函数。此规范减少了全局 RAM。此选项可能减小代码大小并提高执行速度，并使代码生成器能够应用额外的优化。例如：

  ```
  void subsystem_function(real_T rtu_In1, real_T rtu_In2,
                          real_T *rty_Out1)
  ```

  在某些情况下，当生成优化代码时，代码生成器可能不会生成带参数的函数。
- `Allow arguments (Match graphical interface)` — 生成使用与 Subsystem 图形模块接口匹配的参数的函数接口。生成的函数接口是可预测的且不会更改。可预测的接口对于调试和测试代码以及与外部应用程序集成非常有用。例如，如果模型有两个 Inport 模块和两个 Outport 模块，则生成的函数接口为：

  ```
  void subsystem_function(real_T rtu_In1, real_T rtu_In2,
                          real_T *rty_Out1, real_T *rty_Out2)
  ```

有关详细信息，请参阅：

- Reduce Global Variables in Nonreusable Subsystem Functions (Embedded Coder)
- 生成可预测的函数接口以匹配图形模块接口 (Embedded Coder)
- 为非虚拟子系统生成模块化函数代码 (Embedded Coder)

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FunctionInterfaceSpec` |
| **值：** | `'void_void'`（默认）| `'Allow arguments (Optimized)'` | `'Allow arguments (Match graphical interface)'` |

### **Function with separate data** — 控制子系统的代码生成 `off`（默认）| `on`

生成子系统函数代码，其中原子子系统的内部数据与其父模型分离，并由子系统拥有。

- `off` — 不生成子系统函数代码，其中原子子系统的内部数据与其父模型分离并由子系统拥有。
- `on` — 生成子系统函数代码，其中原子子系统的内部数据与其父模型分离并由子系统拥有。子系统数据结构独立于父模型数据结构声明。具有单独数据的子系统拥有自己的模块 I/O 和 `DWork` 数据结构。因此，为子系统生成的代码更易于跟踪和测试。数据分离还倾向于减少整个模型中全局数据结构的最大大小，因为它们被拆分为多个数据结构。

有关如何为原子子系统生成模块化函数代码的详细信息，请参阅 Generate Modular Function Code for Nonvirtual Subsystems (Embedded Coder)。

有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FunctionWithSeparateData` |
| **值：** | `'off'`（默认）| `'on'` |

### **Memory section for initialize/terminate functions** — 如何应用内存段 `Inherit from model`（默认）| `Default` | 模型内存段

选择软件如何将内存段应用于子系统初始化和终止函数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 可能的值取决于您为模型配置设置了什么内存段包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder) 和 Model Configuration Parameters: Code Generation (Simulink Coder)。
- 如果您尚未为模型配置包，`Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项对于覆盖给定子系统的模型内存段设置非常有用。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecFuncInitTerm` |
| **值：** | `'Inherit from model'`（默认）| `'Default'` | 带引号的模型内存段 |

### **Memory section for execution functions** — 如何应用内存段 `Inherit from model`（默认）| `Default` | 模型内存段

选择 Embedded Coder 如何将内存段应用于子系统执行函数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 可能的值取决于您为模型配置设置了什么内存段包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder) 和 Model Configuration Parameters: Code Generation (Simulink Coder)。
- 如果您尚未为模型配置包，`Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项对于覆盖给定子系统的模型内存段设置非常有用。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为
  `Nonreusable function` 或 `Reusable
  function`。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecFuncExecute` |
| **值：** | `'Inherit from model'`（默认） | `'Default'` | 带引号的模型内存段 |

### **常量内存段** — 如何应用内存段 `Inherit from model`（默认） | `Default` | 模型内存段

选择软件如何将内存段应用于子系统常量。

- `Inherit from model` — 将根模型内存段应用于子系统数据。
- `Default` — 不将内存段应用于子系统数据，覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 您指定的内存段应用于生成代码中对应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值因您为模型配置设置的内存段包（如果有）而异。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果您尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包含 `Default` 以及模型包中包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 并选择 **Function with separate data** 参数。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataConstants` |
| **值：** | `'Inherit from model'`（默认） | `'Default'` | 带引号的模型内存段 |

### **内部数据内存段** — 如何应用内存段 `Inherit from model`（默认） | `Default` | 模型内存段

选择软件如何将内存段应用于子系统内部数据。

- `Inherit from model` — 将根模型内存段应用于子系统数据。
- `Default` — 不将内存段应用于子系统数据，覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 您指定的内存段应用于生成代码中对应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值因您为模型配置设置的内存段包（如果有）而异。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果您尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包含 `Default` 以及模型包中包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 并选择 **Function with separate data** 参数。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataInternal` |
| **值：** | `'Inherit from model'`（默认） | `'Default'` | 带引号的模型内存段 |

### **参数内存段** — 如何应用内存段 `Inherit from model`（默认） | `Default` | 模型内存段

选择软件如何将内存段应用于子系统参数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 您指定的内存段应用于生成代码中对应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值因您为模型配置设置的内存段包（如果有）而异。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果您尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包含 `Default` 以及模型包中包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 并选择 **Function with separate data** 参数。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataParameters` |
| **值：** | `'Inherit from model'`（默认） | `'Default'` | 带引号的模型内存段 |

### 子系统引用

### **子系统文件名** — 被引用子系统的文件名 无默认值

指定要引用的子系统文件。有关子系统引用的信息，请参阅 Create and Use Referenced Subsystems in Models。

#### 依赖关系

要访问此参数，请在 **Subsystem Reference** 部分中点击 **Convert**。

有关如何将子系统转换为被引用子系统的详细信息，请参阅 Convert Subsystem to a Referenced Subsystem。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ReferencedSubsystem` |
| **值：** | `''`（默认） | 带引号的子系统文件名 |
| **数据类型：** | `char` | `string` |

## 所属库

Simulink / Commonly Used Blocks Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `imagea` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `no` |
| **多维信号** | `yesa` |
| **可变大小信号** | `yesa` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 实际数据类型或功能支持取决于模块实现。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际代码生成支持取决于模块实现。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `Module`（默认） | 为子系统及子系统内的模块生成代码。 |
| `BlackBox` | 生成黑盒接口。生成的 HDL 代码仅包含子系统的输入/输出端口定义。因此，您可以在模型中使用子系统来生成与现有手写 HDL 代码的接口。子系统的黑盒接口生成类似于 Model 模块接口生成，但不包含时钟信号。 |
| `No HDL` | 从生成的代码中移除子系统。您可以在仿真中使用该子系统，但在 HDL 代码中将其视为“空操作”。 |

**黑盒接口自定义**

对于 `BlackBox` 架构，您可以自定义端口名称并设置外部组件接口的属性。请参阅 Customize Black Box or HDL Cosimulation Interface (HDL Coder)。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **AdaptivePipelining** | 基于综合工具、目标频率和乘法器字长自动插入流水线。默认值为 `inherit`。另请参阅 AdaptivePipelining (HDL Coder)。 |
| **ClockRatePipelining** | 以更快的时钟速率而非较慢的数据速率插入流水线寄存器。默认值为 `inherit`。另请参阅 ClockRatePipelining (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分布，或寄存器重定时。默认值为 `inherit`。另请参阅 DistributedPipelining (HDL Coder)。 |
| **DSPStyle** | 用于乘法器映射的综合属性。默认值为 `none`。另请参阅 DSPStyle (HDL Coder)。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中移除子系统层级。默认值为 `inherit`。另请参阅 FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 映射到单个共享资源的功能等效资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |
| **StreamingFactor** | 被时分复用以转换为串行、标量数据路径的并行数据路径（或向量）数量。默认值为 0，表示实现完全并行的数据路径。另请参阅 Streaming (HDL Coder)。 |

如果此模块不是 DUT，则**目标规范**选项卡中的模块属性设置将被忽略。在 HDL Workflow Advisor 中，如果您使用 **IP Core Generation** 工作流，这些目标规范模块属性值将随模型一起保存。如果您使用 `hdlset_param` 指定这些目标规范模块属性值，则当您打开 HDL Workflow Advisor 时，这些字段将填充相应的值。

| 目标规范 | |
| --- | --- |
| **AdditionalTargetInterfaces** | 附加目标接口，指定为字符向量。要将此模块属性保存在模型上，请在 **IP Core Generation** 工作流的 **Set Target Interface** 任务中，针对要添加更多接口的 DUT 端口，选择 **Add more...**。然后您可以在 Add New Target Interfaces 对话框中添加更多接口。指定接口类型、附加接口数量以及每个附加接口的唯一名称。值：`''`（默认）| 字符向量元胞数组 示例：`'{{'AXI4-Stream','InterfaceID','AXI4-Stream1'}}'` |
| **ProcessorFPGASynchronization** | 处理器/FPGA 同步模式，指定为字符向量。要将此模块属性保存在模型上，请在 **IP Core Generation** 工作流的 **Set Target Interface** 任务中指定 **Processor/FPGA Synchronization**。值：`Free running`（默认）| `Coprocessing - blocking` 示例：`'Free running'` |
| **TestPointMapping** | 要将此模块属性保存在模型上，请在 **IP Core Generation** 工作流的 **Set Target Interface** 任务中指定测试点端口到目标平台接口的映射。值：`''`（默认）| 字符向量元胞数组 示例：`'{{'TestPoint','AXI4-Lite','x"108"'}}'` |
| **TunableParameterMapping** | 要将此模块属性保存在模型上，请在 **IP Core Generation** 工作流的 **Set Target Interface** 任务中指定可调参数端口到目标平台接口的映射。值：`''`（默认）| 字符向量元胞数组 示例：`'{{'myParam','AXI4-Lite','x"108"'}}'` |
| **AXI4RegisterReadback** | 要将此模块属性保存在模型上，请在 **IP Core Generation** 工作流的 **Generate RTL Code and IP Core** 任务中指定是否要在 AXI4 从属写寄存器上启用回读。要了解更多信息，请参阅 Model Design for AXI4 Slave Interface Generation (HDL Coder)。值：`'off'`（默认）| `'on'` |
| **AXI4SlaveIDWidth** | 要将此模块属性保存在模型上，请在 **IP Core Generation** 工作流的 **Generate RTL Code and IP Core** 任务中使用 **AXI4 Slave ID Width** 设置，指定您希望将 DUT IP 核连接到的 AXI 管理器接口数量。要了解更多信息，请参阅 Define Multiple AXI Master Interfaces in Reference Designs to Access DUT AXI4 Slave Interface (HDL Coder)。值：`'off'`（默认）| `'on'` |
| **RegisterInterfaceReadPipeline** | 要将此模块属性保存在模型上，请在 **IP Core Generation** 工作流的 **Generate RTL Code and IP Core** 任务中使用 **Register interface read pipeline** 设置，指定要在读地址解码器路径中插入的流水线级数。要了解更多信息，请参阅 Model Design for AXI4 Slave Interface Generation (HDL Coder)。值：`0`（默认）| 字符向量 |
| **GenerateDefaultAXI4Slave** | 要将此模块属性保存在模型上，请在 **IP Core Generation** 工作流的 **Generate RTL Code and IP Core** 任务中指定是否要禁用默认 AXI4 从属接口的生成。值：`'on'`（默认）| `'off'` |
| **IPCoreAdditionalFiles** | 设计中黑盒的 Verilog®、SystemVerilog 或 VHDL® 文件。指定每个文件的完整路径，并用分号 (;) 分隔文件名。您可以在 HDL Workflow Advisor 的 **Additional source files** 字段中设置此属性。值：`''`（默认）| 字符向量 示例：`'C:\myprojfiles\led_blinking_file1.vhd;C:\myprojfiles\led_blinking_file2.vhd;'` |
| **IPCoreName** | IP 核名称，指定为字符向量。您可以在 HDL Workflow Advisor 的 **IP core name** 字段中设置此属性。如果此属性设置为默认值，HDL Workflow Advisor 将根据 DUT 的名称构造 IP 核名称。值：`''`（默认）| 字符向量 示例：`'my_model_name'` |
| **IPCoreVersion** | IP 核版本号，指定为字符向量。您可以在 HDL Workflow Advisor 的 **IP core version** 字段中设置此属性。如果此属性设置为默认值，HDL Workflow Advisor 将设置 IP 核版本。值：`''`（默认）| 字符向量 示例：`'1.3'` |
| **IPDataCaptureBufferSize** | FPGA Data Capture 缓冲区大小，指定为字符向量。使用 FPGA Data Capture 在 FPGA 上运行时观察设计中的信号。缓冲区大小使用 128\*2^n 的值，其中 n 为整数。默认情况下，缓冲区大小为 128（n=0）。n 的最大值为 13，这意味着缓冲区大小的最大值为 1048576（=128\*2^13）。值：`''`（默认）| 字符向量 示例：`'1.3'` |

**使用代数环生成 HDL 代码**

要为包含 Subsystem 模块的模型生成 HDL 代码：

- 在 Configuration Parameters 对话框中，点击 **Diagnostics**，并将 **Algebraic loop** 参数设置为 `none` 或 `warning`。
- 打开 Subsystem 模块的模块封装，并选择 **Treat as atomic unit** 和 **Minimize algebraic loop occurrences** 参数。

**限制**

如果您的 DUT 是封装子系统，则只有在它位于模型的顶层时才能生成代码。

有关更多信息，请参阅：

- External Component Interfaces (HDL Coder)
- 为子系统生成黑盒接口 (HDL Coder)

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

子系统必须是原子的才能支持 PLC 代码生成。

**PLC 模块属性**

|  |  |
| --- | --- |
| **UseExternalDefinition** | 在生成的代码中抑制模块定义。默认值为 `Off`。另请参阅 UseExternalDefinition (Simulink PLC Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型支持取决于模块实现。

## 版本历史

**在 R2007a 中引入**

## 描述

将模块分组以创建模型层级

Subsystem 模块包含模型或系统中模块的子集。Subsystem 模块可以表示虚拟子系统或非虚拟子系统。

- *虚拟子系统*有助于在视觉上组织模块图。当您在虚拟子系统中对模块进行分组或展开虚拟子系统时，由于模块路径的变化，可能会影响模块的执行顺序。虚拟子系统既不按条件执行也不按原子方式执行。虚拟子系统没有校验和。
- *非虚拟子系统*，也称为*原子子系统*，有助于在功能上组织模块图。当您在非虚拟子系统中对模块进行分组或展开非虚拟子系统时，您会改变模型行为。当父模型执行时，每个非虚拟子系统作为单个模块（或原子单元）执行。非虚拟子系统中的模块连续执行。

有关非虚拟子系统类型的信息，请参阅 Explore Types of Subsystems。

要确定子系统是虚拟的还是非虚拟的，请使用以下任一策略：

- 检查模块的边框。表示虚拟子系统的模块具有细边框。表示非虚拟子系统的模块具有粗边框。

  虚拟和非虚拟子系统模块
- 使用 `get_param` 函数查询布尔模块参数 `IsSubsystemVirtual`。

Subsystem 模块上的端口对应于子系统内部的模块。有关更多信息，请参阅 Connect Subsystems。

Subsystem 模块支持通过子系统 Inport 和 Outport 模块进行信号标签传播。有关更多信息，请参阅 Signal Label Propagation。
