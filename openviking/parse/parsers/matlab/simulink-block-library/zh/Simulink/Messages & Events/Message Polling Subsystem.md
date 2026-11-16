---
type: simulink-block
title: 'Message Triggered Subsystem, Message Polling Subsystem'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Messages & Events'
documentation_page: 'messagetriggeredsubsystem'
documentation_source_path: 'slref/messagetriggeredsubsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Message Triggered Subsystem

## 端口

### 输入

### **Trigger** — 控制信号和数据输入 标量 | 向量 | 矩阵

在 Subsystem 模块中放置一个 **触发类型** 设置为 `message` 的 Trigger 模块，会向该模块添加一个外部消息输入端口。

使用 Trigger 端口控制子系统的执行，并将数据传递到子系统。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 输出

### **Out** — 信号输出 标量 | 向量 | 矩阵

在 Subsystem 模块中放置一个 Outport 模块，会向该模块添加一个外部输出端口。Subsystem 模块上的端口标签与 Outport 模块的名称相匹配。

使用 Outport 模块将信号发送到局部环境。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条的 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

### 主要

### **显示端口标签** — 端口标签的显示选项 `FromPortIcon` (默认) | `FromPortBlockName` | `SignalName` | `none`

选择在 Subsystem 模块图标上显示端口标签的方式。

- `none` — 不显示端口标签。
- `FromPortIcon` — 如果对应的端口图标显示信号名称，则在 Subsystem 模块上显示该信号名称。否则，显示端口模块名称；如果模块名称是默认名称，则显示端口编号。
- `FromPortBlockName` — 在 Subsystem 模块上显示对应端口模块的名称。
- `SignalName` — 如果连接到端口的信号已命名，则在 Subsystem 模块上显示该信号的名称。否则，显示对应端口模块的名称。

有关 Subsystem 模块上的端口标签编辑，请参阅 编辑 Subsystem 模块上的端口标签。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ShowPortLabels` |
| **值：** | `'FromPortIcon'` (默认) | `'FromPortBlockName'` | `'SignalName'` | `'none'` |

### **读/写权限** — 对子系统内容的访问级别 `ReadWrite` (默认) | `ReadOnly` | `NoReadOrWrite`

控制用户对子系统内容的访问。

- `ReadWrite` — 允许打开和修改子系统内容。
- `ReadOnly` — 允许打开子系统，但不允许修改。如果子系统位于模块库中，您可以创建并打开指向该子系统的链接，也可以创建并修改该子系统的本地副本，但不能更改权限或修改原始库实例的内容。
- `NoReadOrWrite` — 禁止打开或修改子系统。如果子系统位于库中，您可以在模型中创建指向该子系统的链接，但不能打开、修改、更改权限或创建该子系统的本地副本。

如果尝试查看 **读/写权限** 参数设置为 `NoReadOrWrite` 的子系统内容，您将不会收到响应。例如，双击此类子系统时，软件不会打开该子系统，也不会显示任何消息。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Permissions` |
| **值：** | `'ReadWrite'` (默认) | `'ReadOnly'` | `'NoReadOrWrite'` |

### **错误回调函数名称** — 发生错误时要调用的函数名称 无默认值

输入当软件执行子系统期间发生错误时要调用的函数名称。

软件会向该函数传递两个参数：子系统的句柄以及一个指定错误类型的字符向量。如果未指定函数，则当执行子系统导致错误时，软件会显示一般错误消息。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ErrorFcn` |
| **值：** | `''` (默认) | 带引号的函数名称 |
| **数据类型：** | `char` | `string` |

### **允许层次化解析** — 工作区变量名称的解析 `All` (默认) | `ExplicitOnly` | `None`

选择是否解析此子系统引用的工作区变量的名称。

有关详细信息，请参阅 符号解析和符号解析过程。

- `All` — 解析此子系统使用的所有工作区变量名称，包括用于指定模块参数值和 Simulink 数据对象（例如 `Simulink.Signal` 对象）的名称。
- `ExplicitOnly` — 仅解析用于指定模块参数值、数据存储内存（不存在模块时）、信号和标记为“必须解析”的状态的工作区变量名称。
- `None` — 不解析任何工作区变量名称。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PermitHierarchicalResolution` |
| **值：** | `'All'` (默认) | `'ExplicitOnly'` | `'None'` |

### **显示子系统重新初始化端口** — 显示重新初始化事件端口的选项 `off` (默认) | `on`

选中此参数以显示重新初始化事件端口。清除此参数以移除这些端口。

#### 依赖关系

要启用此参数，请选择 **视为原子单元**。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ShowSubsystemReinitializePorts` |
| **值：** | `'off'` (默认) | `'on'` |

### **最小化代数环出现次数** — 消除人为代数环的选项 `off` (默认) | `on`

尝试消除包含原子子系统的任何人为代数环

- `off` — 不尝试消除包含原子子系统的任何人为代数环。
- `on` — 尝试消除包含原子子系统的任何人为代数环。

#### 依赖关系

要启用此参数，请选择 **视为原子单元**。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `MinAlgLoopOccurrences` |
| **值：** | `'off'` (默认) | `'on'` |

### **采样时间** — 时间间隔 `-1` (默认) | `[Ts 0]`

指定此子系统中的所有模块必须以相同速率运行，还是可以以不同速率运行。

- `-1` — 继承采样时间。
- `[Ts 0]` — 周期采样时间。

如果子系统中的模块可以以不同速率运行，请将子系统采样时间指定为继承（`-1`）。

如果所有模块必须以相同速率运行，请将与此速率对应的采样时间指定为 **采样时间** 参数的值。

如果子系统中的任何模块指定了不同的采样时间（不是 `-1` 或 `inf`），则软件在更新或仿真模型时会显示错误消息。例如，假设子系统中的所有模块必须每秒运行 `5` 次。为确保此速率，请将子系统的采样时间指定为 `0.2`。在此示例中，如果子系统中的任何模块指定的采样时间不是 `0.2`、`-1` 或 `inf`，则软件在更新或仿真模型时会显示错误。

#### 依赖关系

要启用此参数，请选择 **视为原子单元**。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SystemSampleTime` |
| **值：** | `'-1'` (默认) | `'[Ts 0]'` |

### 代码生成

代码生成选项卡上的参数需要 Simulink Coder™ 或 Embedded Coder 许可证。

### **函数封装** — 代码格式 `Auto` | `Inline` | `Nonreusable function` | `Reusable function`

选择要为原子（非虚拟）子系统生成的代码格式。

- `Auto` — 软件根据模型中存在的子系统类型和实例数量为您选择最佳格式。
- `Inline` — 软件无条件地内联子系统。
- `Nonreusable function` — 如果 **文件名选项** 设置为 `Auto`，软件会将各个函数打包在模型文件中。如果 **文件名选项** 设置为 `Use subsystem name`、`Use function name` 或 `User specified` 并使用不同的文件名，则软件会将各个函数打包在单独的文件中。

  使用此设置的子系统生成的函数可能带有参数，具体取决于 **函数接口** 参数设置。
  您可以分别使用 **函数名称** 和 **文件名**（不带扩展名）参数来命名生成的函数和文件。
  这些函数不可重入。
- `Reusable function` — 软件生成带参数的函数，当模型包含子系统的多个实例时，允许重用子系统代码。

  此选项还会生成带参数的函数，当模型引用层次结构跨被引用模型包含子系统的多个实例时，允许在生成代码中重用子系统代码。在这种情况下，子系统必须位于库中。

有关详细信息，请参阅：

- 为单个子系统生成代码和可执行文件（Simulink Coder）
- 生成内联子系统代码（Simulink Coder）
- 将子系统代码生成为单独的函数和文件（Simulink Coder）
- 从跨模型共享的库子系统生成可重用代码（Simulink Coder）

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Reusable function`。

#### 提示

- 当希望将子系统的多个实例表示为一个可重用函数时，可以将其中每个实例指定为 `Auto` 或 `Reusable function`。最好只使用其中一种，因为同时使用两者会创建两个可重用函数，每个指定对应一个。这些选择的结果仅在无法重用时才有所不同。选择 `Auto` 不允许控制子系统代码的函数或文件名。
- `Reusable function` 和 `Auto` 选项都会尝试确定是否存在子系统的多个实例以及代码是否可以重用。每个选项行为的区别在于无法重用时：

  - `Auto` 会生成内联代码；或者如果情况禁止内联，则为每个子系统实例生成单独的函数。
  - `Reusable function` 会为模型中的每个子系统实例生成一个带参数的单独函数。
- 如果在生成代码受源代码管理控制时选择 `Reusable function`，请将 **文件名选项** 设置为 `Use subsystem name`、`Use function name` 或 `User specified`。否则，每当修改模型时，代码文件的名称都会更改，从而妨碍对文件进行源代码管理。
- 如果选择 `Auto` 或 `Inline` 以外的选项，并且模型配置参数 **状态**，则代码生成器会生成单独的输出和更新方法。代码生成器不会考虑 **为代码生成和仿真合并输出和更新方法** 规范。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证才能生成代码。
- 要启用此参数，请选择 **视为原子单元**。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWSystemCode` |
| **值：** | `'Auto'` | `'Inline'` | `'Nonreusable function'` | `'Reusable function'` |

### **函数名称选项** — 如何命名生成的函数 `Auto` | `Use subsystem name` | `User specified`

选择软件为子系统生成的函数的命名方式。

如果您拥有 Embedded Coder 许可证，可以使用配置参数 **代码生成** > **标识符** 窗格上的选项控制函数名称。

- `Auto` — 使用默认命名约定分配唯一的函数名称，即 `model_subsystem()`，其中 *`model`* 是模型名称，*`subsystem`* 是子系统名称；当代码被重用时，则是相同子系统的名称。

  如果为 **函数封装** 参数选择 `Reusable function`，并且模型引用层次结构包含可重用子系统的多个实例，则为了生成子系统的可重用代码，**函数名称选项** 必须设置为 `Auto`。
- `Use subsystem name` — 使用子系统名称作为函数名称。默认情况下，函数名称使用命名约定 `model_subsystem`。

  当子系统位于库模块中，且子系统参数 **函数封装** 设置为 `Reusable function` 时，如果设置 `Use subsystem name` 选项，代码生成器会将库模块的名称用于子系统函数名称和文件名。
- `User specified` — 启用 **函数名称** 字段。输入任何合法的 C 或 C++ 函数名称，该名称必须唯一。

有关详细信息，请参阅 将子系统代码生成为单独的函数和文件（Simulink Coder）。

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Use subsystem name`。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **函数封装** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFcnNameOpts` |
| **值：** | `'Auto'` | `'Use subsystem name'` | `'User specified'` |

### **函数名称** — 子系统代码的函数名称 无默认值

为子系统代码指定一个唯一且合法的 C 或 C++ 函数名称。

如果希望为函数指定特定名称，而不是让 Simulink Coder 代码生成器分配其自动生成的名称或使用子系统名称，请使用此参数。有关详细信息，请参阅 将子系统代码生成为单独的函数和文件（Simulink Coder）。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **函数名称选项** 设置为 `User specified`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFcnName` |
| **值：** | `''` (默认) | 带引号的函数名称 |
| **数据类型：** | `char` | `string` |

### **File name options** — 如何命名生成的文件 `Auto` | `Use subsystem name` | `Use function name` | `User specified`

选择软件如何为它为该子系统生成的函数命名单独的文件。

- `Auto` — 根据子系统的配置以及模型中的实例数量，`Auto` 会产生不同的结果。

  - 如果代码生成器 *不* 为该子系统生成单独文件，则子系统代码在从子系统父系统生成的代码模块中生成。如果子系统的父系统是模型本身，则子系统代码在 `model.c` 或 `model.cpp` 中生成。
  - 如果你为 **Function packaging** 参数选择 `Reusable function`，并且生成的代码受源代码管理，考虑指定 `Auto` 以外的 **File name options** 值。这可防止生成的文件名因无关的模型修改而变化，而这种情况对于使用源代码管理来管理配置是有问题的。
  - 如果你为 **Function packaging** 参数选择 `Reusable function`，并且模型引用层次结构包含可重用子系统的多个实例，为了为该子系统生成可重用代码，**File name options** 必须设置为 `Auto`。

- `Use subsystem name` — 代码生成器生成单独文件，使用子系统（或库模块）名称作为文件名。

  当 **File name options** 设置为 `Use subsystem name` 时，如果模型包含 Model 模块，或者正在为该模型生成模型引用目标，则子系统文件名会被改写。在这些情况下，子系统文件名由模型名作为前缀加上子系统名组成。

- `Use function name` — 代码生成器使用由 **Function name options** 指定的函数名作为文件名。

- `User specified` — 此选项启用 **File name (no extension)** 文本输入字段。代码生成器使用你输入的名称作为文件名。输入任意文件名，但不要包含 `.c` 或 `.cpp`（或任何其他）扩展名。此文件名不必唯一。

  虽然子系统源文件名不必唯一，但必须避免使用导致循环依赖的非唯一名称。例如，`sys_a.h` 包含 `sys_b.h`，`sys_b.h` 包含 `sys_c.h`，而 `sys_c.h` 包含 `sys_a.h`。

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Use function name`。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，将 **Function packaging** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFileNameOpts` |
| **值：** | `'Auto'` | `'Use subsystem name'` | `'Use function name'` | `'User specified'` |

### **File name (no extension)** — 生成文件的名称 无默认值

你指定的文件名不必唯一。但请避免使用导致循环依赖的非唯一名称。例如，`sys_a.h` 包含 `sys_b.h`，`sys_b.h` 包含 `sys_c.h`，而 `sys_c.h` 包含 `sys_a.h`。

有关详细信息，请参阅 Generate Subsystem Code as Separate Function and Files (Simulink Coder)。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，将 **File name options** 设置为 `User specified`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFileName` |
| **值：** | `''` (default) | 带引号的文件名 |
| **数据类型：** | `char` | `string` |

### **Function interface** — 如何将参数与生成函数一起使用 `void_void` (default) | `Allow arguments (Optimized)` | `Allow arguments (Match graphical interface)`

选择如何将参数与生成的函数一起使用。

- `void_void` — 生成不带参数的函数，并将数据作为全局变量传递。例如：

  ```
  void subsystem_function(void)
  ```

- `Allow arguments (Optimized)` — 生成使用参数而不是将数据作为全局变量传递的函数。此规范减少全局 RAM。此选项可能减小代码大小并提高执行速度，并使代码生成器能够应用额外的优化。例如：

  ```
  void subsystem_function(real_T rtu_In1, real_T rtu_In2,
                          real_T *rty_Out1)
  ```

  在某些情况下，当生成优化代码时，代码生成器可能不会生成带参数的函数。

- `Allow arguments (Match graphical interface)` — 生成使用与 Subsystem 图形模块接口匹配的参数的函数接口。生成的函数接口是可预测的并且不会改变。可预测的接口对于调试和测试代码以及与外部应用程序集成很有用。例如，如果模型有两个 Inport 模块和两个 Outport 模块，则生成的函数接口为：

  ```
  void subsystem_function(real_T rtu_In1, real_T rtu_In2,
                          real_T *rty_Out1, real_T *rty_Out2)
  ```

有关详细信息，请参阅：

- Reduce Global Variables in Nonreusable Subsystem Functions (Embedded Coder)
- Generate Predictable Function Interface to Match Graphical Block Interface (Embedded Coder)
- Generate Modular Function Code for Nonvirtual Subsystems (Embedded Coder)

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，将 **Function packaging** 设置为 `Nonreusable function`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FunctionInterfaceSpec` |
| **值：** | `'void_void'` (default) | `'Allow arguments (Optimized)'` | `'Allow arguments (Match graphical interface)'` |

### **Function with separate data** — 控制子系统的代码生成 `off` (default) | `on`

生成子系统函数代码，其中原子子系统的内部数据与其父模型分离，并由该子系统拥有。

- `off` — 不生成这样的子系统函数代码：其中原子子系统的内部数据与其父模型分离，并由该子系统拥有。
- `on` — 生成子系统函数代码，其中原子子系统的内部数据与其父模型分离，并由该子系统拥有。子系统数据结构独立于父模型数据结构声明。具有分离数据的子系统拥有自己的模块 I/O 和 `DWork` 数据结构。因此，该子系统生成的代码更易于跟踪和测试。数据分离还倾向于减小整个模型中全局数据结构的最大大小，因为它们被拆分为多个数据结构。

有关如何为原子子系统生成模块化函数代码的详细信息，请参阅 Generate Modular Function Code for Nonvirtual Subsystems (Embedded Coder)。

有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，将 **Function packaging** 设置为 `Nonreusable function`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FunctionWithSeparateData` |
| **值：** | `'off'` (default) | `'on'` |

### **Memory section for initialize/terminate functions** — 如何应用内存段 `Inherit from model` (default) | `Default` | 模型内存段

选择软件如何将内存段应用于子系统初始化和终止函数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，覆盖任何模型级规范。
- 将某个模型内存段应用于该子系统。

#### 提示

- 可能的值取决于你为模型配置设置的内存段包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder) 和 Model Configuration Parameters: Code Generation (Simulink Coder)。
- 如果你尚未为模型配置包，`Inherit from model` 是唯一可用的值。否则，列表包含 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，将 **Function packaging** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecFuncInitTerm` |
| **值：** | `'Inherit from model'` (default) | `'Default'` | 带引号的模型内存段 |

### **Memory section for execution functions** — 如何应用内存段 `Inherit from model` (default) | `Default` | 模型内存段

选择 Embedded Coder 如何将内存段应用于子系统执行函数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，覆盖任何模型级规范。
- 将某个模型内存段应用于该子系统。

#### 提示

- 可能的值取决于你为模型配置设置的内存段包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder) 和 Model Configuration Parameters: Code Generation (Simulink Coder)。
- 如果你尚未为模型配置包，`Inherit from model` 是唯一可用的值。否则，列表包含 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，将 **Function packaging** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecFuncExecute` |
| **值：** | `'Inherit from model'` (default) | `'Default'` | 带引号的模型内存段 |

### **Memory section for constants** — 如何应用内存段 `Inherit from model` (default) | `Default` | 模型内存段

选择软件如何将内存段应用于子系统常量。

- `Inherit from model` — 将根模型内存段应用于子系统数据。
- `Default` — 不将内存段应用于子系统数据，覆盖任何模型级规范。
- 将某个模型内存段应用于该子系统。

#### 提示

- 你指定的内存段应用于生成代码中对应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值取决于你为模型配置设置的内存段包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果你尚未为模型配置包，`Inherit from model` 是唯一可用的值。否则，列表包含 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，将 **Function packaging** 设置为 `Nonreusable function`，并选择 **Function with separate data** 参数。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataConstants` |
| **值：** | `'Inherit from model'` (default) | `'Default'` | 带引号的模型内存段 |

### **Memory section for internal data** — 如何应用内存段 `Inherit from model` (default) | `Default` | 模型内存段

选择软件如何将内存段应用于子系统内部数据。

- `Inherit from model` — 将根模型内存段应用于子系统数据。
- `Default` — 不将内存段应用于子系统数据，覆盖任何模型级规范。
- 将某个模型内存段应用于该子系统。

#### 提示

- 你指定的内存段应用于生成代码中对应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值取决于你为模型配置设置的内存段包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果你尚未为模型配置包，`Inherit from model` 是唯一可用的值。否则，列表包含 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，将 **Function packaging** 设置为 `Nonreusable function`，并选择 **Function with separate data** 参数。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataInternal` |
| **值：** | `'Inherit from model'` (default) | `'Default'` | 带引号的模型内存段 |

### **Memory section for parameters** — 如何应用内存段 `Inherit from model` (default) | `Default` | 模型内存段

选择软件如何将内存段应用于子系统参数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，覆盖任何模型级规范。
- 将某个模型内存段应用于该子系统。

#### 提示

- 指定的内存段应用于生成代码中对应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值取决于你为模型配置设置的内存段包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 以及模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖项

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function`，并选择 **具有单独数据的函数** 参数。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataParameters` |
| **值：** | `'Inherit from model'` (default) | `'Default'` | 引号中的模型内存段 |

### 子系统引用

### **子系统文件名** — 引用的子系统文件名，无默认值

指定要引用的子系统文件。有关子系统引用的信息，请参阅 Create and Use Referenced Subsystems in Models。

#### 依赖项

要访问此参数，请在 **子系统引用** 部分中，点击 **转换**。

有关如何将子系统转换为引用的子系统的详细信息，请参阅 Convert Subsystem to a Referenced Subsystem。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ReferencedSubsystem` |
| **值：** | `''` (default) | 引号中的子系统文件名 |
| **数据类型：** | `char` | `string` |

## 所属库

Simulink / Messages & Events

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `no` |
| **多维信号** | `yesa` |
| **可变大小信号** | `yesa` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 实际数据类型或能力支持取决于模块实现。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际代码生成支持取决于模块实现。仅当将控制端口连接到根级 Inport 模块并将 message-triggered subsystem 放在 export-function 模型中时，才支持计划模式的代码生成。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型支持取决于模块实现。

## 版本历史

**在 R2022a 中引入**

## 描述

执行由消息输入控制的子系统

此模块是一个 Subsystem 模块，已预配置为创建基于消息输入执行的子系统的起点。根据执行时机，该模块具有不同的名称。

- Message Triggered Subsystem 模块只要控制端口有可用消息就会执行，与模块采样时间无关。
- Message Polling Subsystem 模块定期检查消息，并在控制端口有可用消息时执行。

在子系统内部，Trigger 模块显示一个输出端口，该端口输出携带消息负载的数据信号。

### Message Triggered Subsystem

Message Triggered Subsystem 模块支持基于事件的消息触发。只要控制端口有可用消息，该模块就会执行，与采样时间无关。该模块包含一个 Trigger 模块，其 **触发类型** 设置为 `message`，**触发时间** 设置为 `on message available`。

该模块以两种模式运行：计划模式和立即模式。

- 在 *计划模式* 下，可以在调度编辑器中调度子系统的执行顺序，以对异步行为建模。你可以将子系统执行推迟到特定的 Simulink® 任务之后，同时保持在同一时间步。触发端口前的 Queue 模块可以在消息进入子系统之前缓冲消息。当消息到达 Queue 模块时，它会引发一个事件，该事件根据调度触发子系统从 Queue 模块拉取消息。如果消息源和触发端口之间没有 Queue 模块，Simulink 会将触发端口视为具有容量为 1 的内部覆盖型队列，类似于 Receive 模块。触发端口可以连接到根级 Inport 模块，以便对软件组件建模。Message-trigger subsystem 可以放在 export-function 模型中，例如 function-call 子系统。

  要使用计划模式，请在 Trigger 模块中选中 **将调度作为非周期分区** 复选框。
- 在 *立即模式* 下，只要控制端口有可用消息，子系统就会执行，这会将消息推送到子系统，而无需队列缓冲消息。

  要使用立即模式，请清除 Trigger 模块中的 **将调度作为非周期分区** 复选框。

### Message Polling Subsystem

Message Polling Subsystem 模块根据控制端口是否有可用消息，在每个时间步有条件地执行。该模块包含一个 Trigger 模块，其 **触发类型** 设置为 `message`，**触发时间** 设置为 `on sample time hit`。

该模块在每个时间步尝试从控制端口前的队列中拉取消息。如果消息源和控制端口之间没有 Queue 模块，Simulink 会将控制端口视为具有容量为 1 的内部覆盖型队列，类似于 Receive 模块。如果队列不为空，则会拉取一条消息，子系统以消息负载作为输入执行。每个时间步只拉取一条消息。每个时间步只拉取一条消息。如果当前时间步队列中有多条消息，则在下个时间步拉取下一条消息。如果队列为空，则子系统在该时间步不执行。你可以在 Message Polling Subsystem 模块的模块对话框中设置采样时间。请参阅 Sample time。
