---
type: simulink-block
title: 'For Each Subsystem'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'foreachsubsystem'
documentation_source_path: 'slref/foreachsubsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# For Each Subsystem

## 端口

### 输入

### **In** — Subsystem 模块的信号输入 标量 | 向量 | 矩阵

Subsystem 模块的信号输入，指定为标量、向量或矩阵。在 Subsystem 模块中放置 Inport 模块会为该模块添加一个外部输入端口。端口标签与 Inport 模块的名称匹配。

使用 Inport 模块从局部环境接收信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Out** — Subsystem 模块的信号输出 标量 | 向量 | 矩阵

Subsystem 模块的信号输出，以标量、向量或矩阵形式返回。在 Subsystem 模块中放置 Outport 模块会为该模块添加一个外部输出端口。端口标签与 Outport 模块的名称匹配。

使用 Outport 模块向局部环境发送信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **Show port labels** — 端口标签的显示选项 `FromPortIcon`（默认）| `FromPortBlockName` | `SignalName` | `none`

选择如何在 Subsystem 模块图标上显示端口标签。

- `none` — 不显示端口标签。
- `FromPortIcon` — 如果对应端口图标显示信号名称，则在 Subsystem 模块上显示该信号名称。否则，显示端口模块名称，或者如果模块名称为默认名称，则显示端口编号。
- `FromPortBlockName` — 在 Subsystem 模块上显示对应端口模块的名称。
- `SignalName` — 如果连接到端口的信号已命名，则在 Subsystem 模块上显示该信号名称。否则，显示对应端口模块的名称。

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
- `ReadOnly` — 允许打开子系统但不允许修改。如果子系统位于模块库中，您可以创建并打开指向该子系统的链接，也可以创建和修改该子系统的局部副本，但不能更改权限或修改原始库实例的内容。
- `NoReadOrWrite` — 禁止打开或修改子系统。如果子系统位于库中，您可以在模型中创建指向该子系统的链接，但不能打开、修改、更改权限或创建该子系统的局部副本。

如果尝试查看 **Read/Write permissions** 参数设置为 `NoReadOrWrite` 的子系统内容，您不会收到任何响应。例如，双击此类子系统时，软件不会打开该子系统，也不会显示任何消息。

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
- `ExplicitOnly` — 仅解析用于指定模块参数值、数据存储内存（不存在对应模块时）、信号以及标记为“must resolve”的状态的工作区变量名称。
- `None` — 不解析任何工作区变量名称。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PermitHierarchicalResolution` |
| **值：** | `'All'`（默认）| `'ExplicitOnly'` | `'None'` |

### **Minimize algebraic loop occurrences** — 消除人为代数环的选项 `off`（默认）| `on`

尝试消除包含原子子系统的任何人为代数环

- `off` — 不尝试消除包含原子子系统的任何人为代数环。
- `on` — 尝试消除包含原子子系统的任何人为代数环。

#### 依赖关系

要启用此参数，请选择 **Treat as atomic unit**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `MinAlgLoopOccurrences` |
| **值：** | `'off'`（默认）| `'on'` |

### 代码生成

代码生成选项卡上的参数需要 Simulink Coder 或 Embedded Coder® 许可证。

### **Function packaging** — 代码格式 `Auto` | `Inline` | `Nonreusable function` | `Reusable function`

选择要为原子（非虚拟）子系统生成的代码格式。

- `Auto` — 软件根据模型中存在的子系统类型和实例数量为您选择最佳格式。
- `Inline` — 软件无条件地内联该子系统。
- `Nonreusable function` — 如果 **Filename options** 设置为 `Auto`，软件会在模型文件中打包单独的函数。如果 **File name options** 设置为 `Use subsystem name`、`Use function name` 或 `User specified` 并使用不同的文件名，软件会在单独的文件中打包单独的函数。

  使用此设置的子系统生成的函数可能带有参数，具体取决于 Function interface 参数设置。您可以分别使用 Function name 和 File name (no extension) 参数来命名生成的函数和文件。这些函数不可重入。
- `Reusable function` — 软件生成带参数的函数，当模型包含子系统的多个实例时，允许重用子系统代码。

  此选项还会生成带参数的函数，允许在模型引用层次结构的生成代码中重用子系统代码，该层次结构在多个被引用模型中包含子系统的多个实例。在这种情况下，子系统必须位于库中。

有关详细信息，请参阅：

- 为单个子系统生成代码和可执行文件 (Simulink Coder)
- Generate Inlined Subsystem Code (Simulink Coder)
- 将子系统代码生成为单独的函数和文件 (Simulink Coder)
- 从跨模型共享的库子系统生成可重用代码 (Simulink Coder)

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Reusable function`。

#### 提示

- 当您希望将子系统的多个实例表示为一个可重用函数时，可以将每个实例指定为 `Auto` 或 `Reusable function`。最好只使用其中一种，因为同时使用两者会创建两个可重用函数，每种指定各一个。这些选择的结果仅在无法重用时才有所不同。选择 `Auto` 不允许控制子系统代码的函数名或文件名。
- `Reusable function` 和 `Auto` 选项都会尝试确定是否存在子系统的多个实例以及代码是否可以重用。两种选项行为之间的区别在于，当无法重用时：

  - `Auto` 会生成内联代码，或者如果情况不允许内联，则为每个子系统实例生成单独的函数。
  - `Reusable function` 会为模型中的每个子系统实例生成一个带参数的单独函数。
- 如果在生成的代码处于源代码控制之下时选择 `Reusable function`，请将 **File name options** 设置为 `Use subsystem name`、`Use function name` 或 `User specified`。否则，每当修改模型时，代码文件的名称都会更改，从而无法对文件进行源代码控制。
- 如果选择 `Auto` 或 `Inline` 以外的选项，并且模型配置参数 **States**，代码生成器会生成单独的输出和更新方法。代码生成器不会考虑 **Combine output and update methods for code generation and simulation** 规范。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证才能进行代码生成。
- 要启用此参数，请选择 **Treat as atomic unit**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWSystemCode` |
| **值：** | `'Auto'` | `'Inline'` | `'Nonreusable function'` | `'Reusable function'` |

### **Function name options** — 如何命名生成的函数 `Auto` | `Use subsystem name` | `User specified`

选择软件如何命名它为子系统生成的函数。

如果您拥有 Embedded Coder 许可证，可以使用配置参数 **Code Generation** > **Identifiers** 窗格上的选项控制函数名称。

- `Auto` — 使用默认命名约定 `model_subsystem()` 分配唯一的函数名称，其中 *`model`* 是模型名称，*`subsystem`* 是子系统名称，或者在代码重用时为相同子系统的名称。

  如果为 **Function packaging** 参数选择 `Reusable function`，并且模型引用层次结构包含可重用子系统的多个实例，则为了生成子系统的可重用代码，**Function name options** 必须设置为 `Auto`。
- `Use subsystem name` — 使用子系统名称作为函数名称。默认情况下，函数名称使用命名约定 `model_subsystem`。

  当子系统位于库模块中且子系统参数 Function packaging 设置为 `Reusable function` 时，如果设置 `Use subsystem name` 选项，代码生成器将使用库模块的名称作为子系统函数名称和文件名。
- `User specified` — 启用 **Function name** 字段。输入任何合法的 C 或 C++ 函数名称，该名称必须唯一。

有关详细信息，请参阅 Generate Subsystem Code as Separate Function and Files (Simulink Coder)。

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Use subsystem name`。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFcnNameOpts` |
| **值：** | `'Auto'` | `'Use subsystem name'` | `'User specified'` |

### **Function name** — 子系统代码的函数名称 无默认值

为子系统代码指定唯一的、合法的 C 或 C++ 函数名称。

如果您想为函数指定特定名称，而不是让 Simulink Coder 代码生成器分配自己的自动生成名称或使用子系统名称，请使用此参数。有关详细信息，请参阅 Generate Subsystem Code as Separate Function and Files (Simulink Coder)。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **Function name options** 设置为 `User specified`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFcnName` |
| **值：** | `''`（默认）| 带引号的函数名称 |
| **数据类型：** | `char` | `string` |

### **File name options** — 如何命名生成的文件 `Auto` | `Use subsystem name` | `Use function name` | `User specified`

选择软件如何命名它为子系统生成的函数的单独文件。

- `Auto` — 根据子系统的配置以及模型中的实例数量，`Auto` 会产生不同的结果。

  - 如果代码生成器*不*为子系统生成单独的文件，则子系统代码在从子系统父系统生成的代码模块中生成。如果子系统父系统是模型本身，则子系统代码在 `model.c` 或 `model.cpp` 中生成。
  - 如果为 **Function packaging** 参数选择 `Reusable function`，并且生成的代码处于源代码控制之下，请考虑指定 `Auto` 以外的 **File name options** 值。这可以防止生成的文件名因无关的模型修改而更改，这对于使用源代码控制管理配置来说是个问题。
  - 如果为 **Function packaging** 参数选择 `Reusable function`，并且模型引用层次结构包含可重用子系统的多个实例，则为了生成子系统的可重用代码，**File name options** 必须设置为 `Auto`。
- `Use subsystem name` — 代码生成器生成单独的文件，使用子系统（或库模块）名称作为文件名。

  当 **File name options** 设置为 `Use subsystem name` 时，如果模型包含 Model 模块，或者正在为模型生成模型引用目标，则子系统文件名会被改编。在这些情况下，子系统的文件名由子系统名称加上模型名称前缀组成。
- `Use function name` — 代码生成器使用由 **Function name options** 指定的函数名称作为文件名。
- `User specified` — 此选项启用 **File name (no extension)** 文本输入字段。代码生成器使用您输入的名称作为文件名。输入任何文件名，但不要包含 `.c` 或 `.cpp`（或任何其他）扩展名。此文件名不必唯一。

  虽然子系统源文件名不必唯一，但必须避免使用会导致循环依赖的非唯一名称。例如，`sys_a.h` 包含 `sys_b.h`，`sys_b.h` 包含 `sys_c.h`，而 `sys_c.h` 包含 `sys_a.h`。

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Use function name`。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFileNameOpts` |
| **值：** | `'Auto'` | `'Use subsystem name'` | `'Use function name'` | `'User specified'` |

### **文件名（无扩展名）** — 生成文件的名称，无默认值

您指定的文件名不必唯一。但是，请避免使用会导致循环依赖的非唯一名称。例如，`sys_a.h` 包含 `sys_b.h`，`sys_b.h` 包含 `sys_c.h`，而 `sys_c.h` 包含 `sys_a.h`。

有关详细信息，请参阅 Generate Subsystem Code as Separate Function and Files (Simulink Coder)。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **文件名选项** 设置为 `User specified`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFileName` |
| **值：** | `''`（默认） | 带引号的文件名 |
| **数据类型：** | `char` | `string` |

### **函数接口** — 如何使用生成函数的参数 `void_void`（默认） | `Allow arguments (Optimized)` | `Allow arguments (Match graphical interface)`

选择如何使用生成函数的参数。

- `void_void` — 生成不带参数的函数，并将数据作为全局变量传递。例如：

  ```
  void subsystem_function(void)
  ```
- `Allow arguments (Optimized)` — 生成使用参数而不是将数据作为全局变量传递的函数。此规范可减少全局 RAM。此选项可能会减小代码大小并提高执行速度，并使代码生成器能够应用额外的优化。例如：

  ```
  void subsystem_function(real_T rtu_In1, real_T rtu_In2,
                          real_T *rty_Out1)
  ```

  在某些情况下，生成优化代码时，代码生成器可能不会生成带参数的函数。
- `Allow arguments (Match graphical interface)` — 生成使用与 Subsystem 图形模块接口匹配的参数的函数接口。生成的函数接口是可预测的，不会发生变化。可预测的接口对于调试和测试代码以及与外部应用程序集成非常有用。例如，如果模型有两个 Inport 模块和两个 Outport 模块，则生成的函数接口为：

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
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FunctionInterfaceSpec` |
| **值：** | `'void_void'`（默认） | `'Allow arguments (Optimized)'` | `'Allow arguments (Match graphical interface)'` |

### **具有独立数据的函数** — 控制子系统 `off`（默认） | `on` 的代码生成

生成子系统函数代码，其中原子子系统的内部数据与其父模型分离，并由子系统拥有。

- `off` — 不生成子系统函数代码，其中原子子系统的内部数据与其父模型分离，并由子系统拥有。
- `on` — 生成子系统函数代码，其中原子子系统的内部数据与其父模型分离，并由子系统拥有。子系统数据结构独立于父模型数据结构声明。具有独立数据的子系统拥有自己的模块 I/O 和 `DWork` 数据结构。因此，为子系统生成的代码更易于跟踪和测试。数据分离还倾向于减小整个模型中全局数据结构的最大大小，因为它们被拆分为多个数据结构。

有关如何为原子子系统生成模块化函数代码的详细信息，请参阅 Generate Modular Function Code for Nonvirtual Subsystems (Embedded Coder)。

有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FunctionWithSeparateData` |
| **值：** | `'off'`（默认） | `'on'` |

### **初始化/终止函数的内存段** — 如何应用内存段 `Inherit from model`（默认） | `Default` | 模型内存段

选择软件如何将内存段应用于子系统初始化和终止函数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 可能的值因您为模型配置设置的任何内存段包而异。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder) 和 Model Configuration Parameters: Code Generation (Simulink Coder)。
- 如果您尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecFuncInitTerm` |
| **值：** | `'Inherit from model'`（默认） | `'Default'` | 带引号的模型内存段 |

### **执行函数的内存段** — 如何应用内存段 `Inherit from model`（默认） | `Default` | 模型内存段

选择 Embedded Coder 如何将内存段应用于子系统执行函数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 可能的值因您为模型配置设置的任何内存段包而异。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder) 和 Model Configuration Parameters: Code Generation (Simulink Coder)。
- 如果您尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecFuncExecute` |
| **值：** | `'Inherit from model'`（默认） | `'Default'` | 带引号的模型内存段 |

### **常量的内存段** — 如何应用内存段 `Inherit from model`（默认） | `Default` | 模型内存段

选择软件如何将内存段应用于子系统常量。

- `Inherit from model` — 将根模型内存段应用于子系统数据。
- `Default` — 不将内存段应用于子系统数据，覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 您指定的内存段应用于生成代码中相应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值因您为模型配置设置的任何内存段包而异。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果您尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function` 并选择 **具有独立数据的函数** 参数。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataConstants` |
| **值：** | `'Inherit from model'`（默认） | `'Default'` | 带引号的模型内存段 |

### **内部数据的内存段** — 如何应用内存段 `Inherit from model`（默认） | `Default` | 模型内存段

选择软件如何将内存段应用于子系统内部数据。

- `Inherit from model` — 将根模型内存段应用于子系统数据。
- `Default` — 不将内存段应用于子系统数据，覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 您指定的内存段应用于生成代码中相应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值因您为模型配置设置的任何内存段包而异。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果您尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function` 并选择 **具有独立数据的函数** 参数。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataInternal` |
| **值：** | `'Inherit from model'`（默认） | `'Default'` | 带引号的模型内存段 |

### **参数的内存段** — 如何应用内存段 `Inherit from model`（默认） | `Default` | 模型内存段

选择软件如何将内存段应用于子系统参数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 您指定的内存段应用于生成代码中相应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值因您为模型配置设置的任何内存段包而异。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果您尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function` 并选择 **具有独立数据的函数** 参数。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataParameters` |
| **值：** | `'Inherit from model'`（默认） | `'Default'` | 带引号的模型内存段 |

## 所属库

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` |
| **直接馈通** | `no` |
| **多维信号** | `yesa` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 实际数据类型或功能支持取决于模块实现。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际代码生成支持取决于模块实现。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

当为 For Each Subsystem 生成 HDL 代码时，代码生成器尝试使用 `for-generate` 循环来遍历输入和输出信号的元素。for-generate 循环提高了可读性并减少了代码行数，否则对于大型向量信号可能会产生数百行代码。该子系统支持向量和 3D 矩阵输入信号。参见 Generate HDL Code for Blocks Inside For Each Subsystem (HDL Coder)。

您可以为 HDL 代码生成使用非零分区偏移量。代码生成器支持标量、向量或矩阵作为掩码参数值。您可以为 For Each Subsystem 模块内的掩码参数的元素、1D 和 2D 分区生成 HDL 代码。在 For Each Subsystem 模块内部，将掩码参数用作 Constant 模块中的 **Constant value** 参数或 Gain 模块中的 **Gain** 参数。

**限制**

- 不能将 For Each Subsystem 模块用作 DUT。
- 不能为 HDL 代码生成设置 For Each 模块的 `SpecifiedNumIters` 参数。当 `SpecifiedNumIters` 的值不等于默认值 `-1` 时，HDL 代码生成会返回错误。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `Module`（默认） | 为子系统及子系统内的模块生成代码。 |
| `BlackBox` | 生成黑盒接口。生成的 HDL 代码仅包含子系统的输入/输出端口定义。因此，您可以在模型中使用子系统来生成与现有手写 HDL 代码的接口。子系统的黑盒接口生成类似于 Model 模块接口生成，但不包含时钟信号。 |
| `No HDL` | 从生成的代码中移除子系统。您可以在仿真中使用该子系统，但在 HDL 代码中将其视为“空操作”。 |

**黑盒接口自定义**

对于 `BlackBox` 架构，您可以自定义端口名称并设置外部组件接口的属性。参见 Customize Black Box or HDL Cosimulation Interface (HDL Coder)。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **AdaptivePipelining** | 基于综合工具、目标频率和乘法器字长的自动流水线插入。默认值为 `inherit`。另请参见 AdaptivePipelining (HDL Coder)。 |
| **BalanceDelays** | 检测沿一条路径引入的新延迟，并在其他路径上插入匹配的延迟。默认值为 `inherit`。另请参见 BalanceDelays (HDL Coder)。 |
| **ClockRatePipelining** | 以更快的时钟速率而非较慢的数据速率插入流水线寄存器。默认值为 `inherit`。另请参见 ClockRatePipelining (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参见 ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分配，或寄存器重定时。默认值为 `inherit`。另请参见 DistributedPipelining (HDL Coder)。 |
| **DSPStyle** | 用于乘法器映射的综合属性。默认值为 `none`。另请参见 DSPStyle (HDL Coder)。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中移除子系统层级。默认值为 `inherit`。另请参见 FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参见 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参见 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 映射到单个共享资源的功能等效资源数量。默认值为 0。另请参见 Resource Sharing (HDL Coder)。 |
| **StreamingFactor** | 被时间复用以转换为串行标量数据路径的并行数据路径或向量数量。默认值为 0，即实现完全并行的数据路径。另请参见 Streaming (HDL Coder)。 |

**目标规范**

此模块不能作为 DUT，因此 **Target Specification** 选项卡中的模块属性设置将被忽略。

**复数数据支持**

该模块不支持用于 HDL 代码生成的复数数据信号。要输入复数信号，请将复数信号转换为信号数组，然后输入到该模块。要了解更多信息，请参见 Generate HDL Code for Blocks Inside For Each Subsystem (HDL Coder)。

**使用代数环生成 HDL 代码**

要为包含 For Each Subsystem 模块的模型生成 HDL 代码：

- 在“配置参数”对话框中，点击 **Diagnostics**，将 **Algebraic loop** 参数设置为 `none` 或 `warning`。
- 打开 For Each Subsystem 模块的模块掩码，并选中 **Minimize algebraic loop occurrences** 参数。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型支持取决于模块实现。

## 版本历史

**在 R2010a 中引入**

### R2024b：为迭代器子系统中的迭代编号输出添加信号断点和端口值标签

您现在可以通过为以下信号添加信号断点来在迭代器子系统的特定迭代上暂停仿真：

- While Iterator Subsystem 模块内 While Iterator 模块的迭代编号输出端口
- For Iterator Subsystem 模块内 For Iterator 模块的迭代器值输出端口
- For Each Subsystem 模块内 For Each 模块的分区索引输出端口

在以前的版本中，您可以在这些位置添加断点，但断点不会暂停仿真，并且在框图中显示为无效。

这些位置的端口值标签现在显示迭代编号。在以前的版本中，这些位置的端口值标签显示 `inaccessible`。

有关示例，请参见 Debug Simulation of Iterator Subsystem。

## 描述

将算法应用于输入信号或掩码参数的单个元素或子数组

For Each Subsystem 模块是一个 Subsystem 模块，预配置为创建子系统的起点，该子系统在仿真时间步内对输入信号或掩码参数数组的每个元素或子数组重复执行。

For Each Subsystem 模块图标，与 for-each 子系统内容一起显示，包含一个 For Each 模块、一个 Inport 模块和一个 Outport 模块。

子系统内的模块集合表示应用于原始信号或掩码参数数组的单个元素或子数组的算法。在子系统内部，每个具有状态的模块为其处理的每个元素或子数组维护单独的状态集。因此，该子系统的操作在行为上类似于为原始输入信号或掩码参数数组中的每个元素复制子系统内容，然后使用各自的子系统副本处理每个元素。当子系统中的模块集合处理元素或子数组时，子系统将结果拼接以形成输出信号。

### 配置子系统

For Each Subsystem 模块包含一个 For Each 模块，作为子系统的控制模块。指定 For Each 模块的参数以配置子系统输入或掩码参数分解为元素或子数组的方式，以及将各个结果拼接为输出信号的方式。模块参数 **Partition Dimension** 和 **Partition Width** 分别指定切分输入信号或掩码参数数组的维度以及每个切片的宽度。要分区行向量，将 **Partition Dimension** 指定为 `2`。要分区列向量，将 **Partition Dimension** 指定为 `1`。使用参数 **Partition Offset** 指定分区之间的间隙或重叠。指定 **Number of iterations** 以将处理限制为数据的子集。要了解有关模块参数的更多信息，请参见 For Each。

**分区子系统的输入信号**

要指定在 for-each 子系统中每次迭代要分区哪些输入信号，请使用 For Each 模块对话框中的 **Input Partition** 选项卡。指定要分区的信号时，请指定 **Partition Dimension**、**Partition Width** 和 **Partition Offset** 参数。

**分区子系统的掩码参数**

您可以分区 For Each Subsystem 模块的掩码参数。分区对于每次迭代具有相同结构但参数值不同的系统非常有用。在这种情况下，将模型更改为每次迭代分区额外的输入信号会很繁琐。相反，可以向 for-each 子系统添加掩码参数。有关更多信息，请参见 Create a Simple Mask。要选择要分区的掩码参数，请使用 For Each 模块对话框的 **Parameter Partition** 选项卡。有关更多信息，请参见下面的选择分区参数。

**拼接输出**

通过在 **Output Concatenation** 选项卡中指定 **Concatenation Dimension** 来定义拼接结果的维度。

模块为每个子数组生成的结果沿拼接维度堆叠。默认情况下，使用维度 1（*y* 轴），意味着结果垂直堆叠。但是，如果指定拼接维度为 2，则结果沿水平方向（*x* 轴）拼接。因此，如果过程生成行向量，则在第一种情况下拼接结果是矩阵，在第二种情况下是行向量。有关示例，请参见 Specifying the Concatenation Dimension in the For Each Block。

**选择分区参数**

选择要分区的输入信号或子系统掩码参数时，必须指定如何将其分解为每次迭代的元素或子数组。为 **Partition Dimension**、**Partition Width** 和 **Partition Offset** 参数设置整数值。

举例来说，考虑以下形式的输入信号矩阵 `A`：

一个 3×3 矩阵 A，显示所有九个元素，d1 为垂直维度，d2 为水平维度

标签 *d*1 和 *d*2 分别定义维度 1 和 2。如果分区维度和分区宽度都保留默认设置 `1`，分区偏移量为 `0`，则 Simulink® 以等于分区宽度的宽度垂直于分区维度 1 进行切片，即一个元素：

一个 3×3 矩阵 A，显示所有九个元素，按行分区

矩阵 A 分解为以下三个行向量：

一个 3×3 矩阵 A，分解为三个 3 元素行向量

如果改为指定 `2` 作为分区维度，Simulink 垂直于维度 2 进行切片，形成三个列向量：

一个 3×3 矩阵 A，分解为三个 3 元素列向量

除了将 **Partition Dimension** 设置为 `2` 之外，如果将 **Partition Width** 设置为 `2`，将 **Partition Offset** 设置为 `-1`，Simulink 使用两个重叠的 3×2 分区进行处理。

一个 3×3 矩阵 A，分解为两个重叠的 3×2 矩阵

有关示例，请参见 Partitioning an Input Signal with the For Each Block。

默认情况下，输入信号或掩码参数的所有分区都会被处理。要处理分区的子集，请输入要处理的分区数量作为 **Number of iterations**。在上述矩阵示例中，如果 **Partition Offset** 设置为 `0`（默认值），**Number of iterations** 设置为 `2`，则只处理输入矩阵 `A` 的前 2 行或列。

**注意**

在 Simulink 中只有信号被视为一维的。掩码参数根据其方向为行向量或列向量。要分区行向量，将分区维度指定为 2，沿列方向。要分区列向量，将分区维度指定为 1，沿行方向。

### 代码重用支持

对于某些模型，For Each Subsystem 模块改善了 Simulink Coder™ 生成代码中的代码重用。考虑一个包含两个可重用 Atomic Subsystem 模块的模型，它们对信号的每个元素应用相同的标量算法。如果这些子系统的输入信号维度不同，Simulink Coder 生成的代码包含两个不同的函数。您可以将这两个子系统替换为两个相同的 For Each Subsystem 模块，配置为使用相同的算法处理各自输入的每个元素。在这种情况下，Simulink Coder 生成的代码由单个函数组成，该函数由输入信号元素数量参数化。此函数被调用两次，分别对应模型中 For Each Subsystem 模块的每个唯一实例。对于每种情况，输入信号元素具有不同的值。

### 多核执行支持

当您在快速加速器模式下仿真模型时，Simulink 使用多核执行来加速 for-each 子系统的仿真。Simulink 自动在快速加速器模式下运行的前两个时间步对每个符合条件的 for-each 子系统进行性能分析，以比较并行和串行执行时间。然后，如果在仿真运行的后续时间步中这样做可以加快执行时间，Simulink 会指定该 for-each 子系统进行并行多核执行。对于嵌套的 for-each 子系统，多核执行仅适用于顶层子系统。多核执行不适用于包含连续状态或 Function Caller 模块的 for-each 子系统。

要抑制给定 for-each 子系统的多核执行，将子系统内 For Each 模块的 `MultithreadedSim` 参数设置为 `'off'`。

```
set_param(ForEachBlockName,'MultithreadedSim','off')
```

请注意，这是子系统内 For Each 模块的参数，而不是 For Each Subsystem 模块本身的参数。要抑制模型中所有 for-each 子系统的多核执行，将模型的 `MultithreadedSim` 参数设置为 `'off'`。

```
set_param(ModelName,'MultithreadedSim','off')
```

要重新启用多核执行，将相关的 `MultithreadedSim` 参数设置为其默认值 `'auto'`。

有关示例，请参见 Multithreaded Simulation Using For Each Subsystem。

**注意**

如果您在快速加速器模式下仿真模型或从模型生成代码，并且在 for-each 子系统中分区掩码参数，则 for-each 子系统内引用分区参数的任何表达式必须是可调表达式。参见 Tunable Expression Limitations (Simulink Coder)。

### S-Function 支持

For Each Subsystem 模块同时支持 C-MEX S-function 和 Level-2 MATLAB® S-function，前提是该 S-function 使用以下技术之一支持多个执行实例：

- C-MEX S-function 必须在 `mdlSetWorkWidths` 方法中声明 `ssSupportsMultipleExecInstances(S, true)`。
- Level-2 MATLAB S-function 必须在 setup 方法中声明 `block.SupportsMultipleExecInstances = true`。

如果使用这些规范：

- 不要使用全局变量或持久变量，也不要在 S-function 的用户数据中缓存运行时数据，例如 DWork 和 Block I/O。
- 在 For Each Subsystem 模块中，从 `mdlStart` 到 `mdlTerminate` 的每个 S-function 执行方法都会针对该 S-function 处理的每个元素调用一次。因此，必须确保在重复调用 `mdlTerminate` 时不会释放同一块内存。例如，考虑一个 C-MEX S-function，它在 `mdlSetWorkWidths` 中为运行时参数分配内存。该内存只需在 `mdlTerminate` 中释放一次。作为解决方案，在第一次调用 `mdlTerminate` 后将指针设置为空。
