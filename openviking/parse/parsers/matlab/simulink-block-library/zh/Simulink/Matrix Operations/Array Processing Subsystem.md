---
type: simulink-block
title: 'Array Processing Subsystem'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'arrayprocessingsubsystem'
documentation_source_path: 'slref/arrayprocessingsubsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Array Processing Subsystem

## 端口

### 输入

### **In** — 子系统的矩阵信号输入

使用 Inport 模块从局部环境获取信号。

在 Array Processing Subsystem 模块中放置 Inport 模块会为子系统添加一个外部输入端口。端口标签与 Inport 模块的名称一致。使用 Neighborhood 控制模块配置使用邻域模式处理哪些输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Out** — 子系统的矩阵信号输出

使用 Outport 模块将信号发送到局部环境。

在 Array Processing Subsystem 模块中放置 Outport 模块会为子系统添加一个外部输出端口。端口标签与 Outport 模块的名称一致。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### 主要

### **Show port labels** — 端口标签的显示选项 `FromPortIcon`（默认）| `FromPortBlockName` | `SignalName` | `none`

选择如何在 Subsystem 模块图标上显示端口标签。

- `none` — 不显示端口标签。
- `FromPortIcon` — 如果对应端口图标显示信号名称，则在 Subsystem 模块上显示该信号名称。否则，显示端口模块名称；如果模块名称为默认名称，则显示端口编号。
- `FromPortBlockName` — 在 Subsystem 模块上显示对应端口模块的名称。
- `SignalName` — 如果连接到端口的信号已命名，则在 Subsystem 模块上显示该信号名称。否则，显示对应端口模块的名称。

有关 Subsystem 模块上的端口标签编辑，请参阅 Edit Port Labels on Subsystem Blocks。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ShowPortLabels` |
| **值**：| `'FromPortIcon'`（默认）| `'FromPortBlockName'` | `'SignalName'` | `'none'` |

### **Read/Write permissions** — 对子系统内容的访问级别 `ReadWrite`（默认）| `ReadOnly` | `NoReadOrWrite`

控制用户对子系统内容的访问。

- `ReadWrite` — 允许打开和修改子系统内容。
- `ReadOnly` — 允许打开子系统但不允许修改。如果子系统位于模块库中，您可以创建并打开指向该子系统的链接，也可以制作和修改该子系统的本地副本，但不能更改权限或修改原始库实例的内容。
- `NoReadOrWrite` — 禁止打开或修改子系统。如果子系统位于库中，您可以在模型中创建指向该子系统的链接，但不能打开、修改、更改权限或创建该子系统的本地副本。

如果尝试查看 **Read/Write permissions** 参数设置为 `NoReadOrWrite` 的子系统的内容，您不会收到任何响应。例如，双击此类子系统时，软件不会打开该子系统，也不会显示任何消息。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `Permissions` |
| **值**：| `'ReadWrite'`（默认）| `'ReadOnly'` | `'NoReadOrWrite'` |

### **Name of error callback function** — 发生错误时要调用的函数名称 无默认值

输入当软件执行子系统期间发生错误时要调用的函数名称。

软件向该函数传递两个参数：子系统的句柄和一个指定错误类型的字符向量。如果未指定函数，则当执行子系统导致错误时，软件会显示一条通用错误消息。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ErrorFcn` |
| **值**：| `''`（默认）| 带引号的函数名称 |
| **Data Types:** | `char` | `string` |

### **Permit hierarchical resolution** — 工作区变量名称的解析方式 `All`（默认）| `ExplicitOnly` | `None`

选择是否解析此子系统引用的工作区变量名称。

有关详细信息，请参阅 Symbol Resolution 和 Symbol Resolution Process。

- `All` — 解析此子系统使用的所有工作区变量名称，包括用于指定模块参数值和 Simulink 数据对象（例如 `Simulink.Signal` 对象）的名称。
- `ExplicitOnly` — 仅解析用于指定模块参数值、数据存储内存（不存在对应模块时）、信号和标记为“must resolve”的状态的工作区变量名称。
- `None` — 不解析任何工作区变量名称。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PermitHierarchicalResolution` |
| **值**：| `'All'`（默认）| `'ExplicitOnly'` | `'None'` |

### **Show subsystem reinitialize ports** — 显示重新初始化事件端口的选项 `off`（默认）| `on`

选择此参数以显示重新初始化事件端口。清除此参数以移除这些端口。

#### 依赖关系

要启用此参数，请选择 **Treat as atomic unit**。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ShowSubsystemReinitializePorts` |
| **值**：| `'off'`（默认）| `'on'` |

### 代码生成

代码生成选项卡上的参数需要 Simulink Coder™ 或 Embedded Coder® 许可证。

### **Function packaging** — 代码格式 `Auto` | `Inline` | `Nonreusable function` | `Reusable function`

选择要为原子（非虚拟）子系统生成的代码格式。

- `Auto` — 软件根据模型中存在的子系统类型和实例数量为您选择最佳格式。
- `Inline` — 软件无条件地内联该子系统。
- `Nonreusable function` — 如果 **Filename options** 设置为 `Auto`，软件将各个函数打包在模型文件中。如果 **File name options** 设置为 `Use subsystem name`、`Use function name` 或 `User specified` 并使用不同的文件名，软件将各个函数打包在单独的文件中。

  使用此设置的子系统生成的函数可能带有参数，具体取决于 Function interface 参数设置。您可以分别使用 Function name 和 File name (no extension) 参数来命名生成的函数和文件。这些函数不可重入。
- `Reusable function` — 软件生成带参数的函数，当模型包含子系统的多个实例时允许复用子系统代码。

  此选项还会生成带参数的函数，允许在模型引用层次结构的生成代码中复用子系统代码，该层次结构在多个被引用模型中包含子系统的多个实例。在这种情况下，子系统必须位于库中。

有关详细信息，请参阅：

- 为单个子系统生成代码和可执行文件 (Simulink Coder)
- Generate Inlined Subsystem Code (Simulink Coder)
- 将子系统代码生成为单独的函数和文件 (Simulink Coder)
- 从跨模型共享的库子系统生成可重用代码 (Simulink Coder)

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Reusable function`。

#### 提示

- 当您希望将子系统的多个实例表示为一个可复用函数时，可以将每个实例指定为 `Auto` 或 `Reusable function`。最好只使用其中一种，因为同时使用两者会创建两个可复用函数，每种指定各一个。这些选择的结果仅在无法复用时才有所不同。选择 `Auto` 不允许控制子系统代码的函数名或文件名。
- `Reusable function` 和 `Auto` 选项都会尝试确定是否存在子系统的多个实例以及代码是否可以复用。两种选项行为之间的区别在于当无法复用时的表现：

  - `Auto` 生成内联代码，或者如果情况不允许内联，则为每个子系统实例生成单独的函数。
  - `Reusable function` 为模型中的每个子系统实例生成一个带参数的单独函数。
- 如果在生成的代码处于源代码控制下时选择 `Reusable function`，请将 **File name options** 设置为 `Use subsystem name`、`Use function name` 或 `User specified`。否则，每当修改模型时，代码文件的名称都会更改，从而无法对文件进行源代码控制。
- 如果选择 `Auto` 或 `Inline` 以外的选项，并且模型配置参数 **States** 设置为相应值，代码生成器会生成单独的输出和更新方法。代码生成器不会考虑 **Combine output and update methods for code generation and simulation** 规范。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证才能进行代码生成。
- 要启用此参数，请选择 **Treat as atomic unit**。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RTWSystemCode` |
| **值**：| `'Auto'` | `'Inline'` | `'Nonreusable function'` | `'Reusable function'` |

### **Function name options** — 如何命名生成的函数 `Auto` | `Use subsystem name` | `User specified`

选择软件如何命名其为子系统生成的函数。

如果您拥有 Embedded Coder 许可证，可以使用配置参数 **Code Generation** > **Identifiers** 窗格上的选项来控制函数名称。

- `Auto` — 使用默认命名约定分配唯一的函数名称 `model_subsystem()`，其中 *`model`* 是模型名称，*`subsystem`* 是子系统名称，或者在代码复用时为相同子系统的名称。

  如果为 **Function packaging** 参数选择 `Reusable function`，并且模型引用层次结构包含可复用子系统的多个实例，则为了生成该子系统的可复用代码，**Function name options** 必须设置为 `Auto`。
- `Use subsystem name` — 使用子系统名称作为函数名称。默认情况下，函数名称使用命名约定 `model_subsystem`。

  当子系统位于库模块中且子系统参数 Function packaging 设置为 `Reusable function` 时，如果设置 `Use subsystem name` 选项，代码生成器将使用库模块的名称作为子系统函数名称和文件名。
- `User specified` — 启用 **Function name** 字段。输入任何合法的 C 或 C++ 函数名称，该名称必须唯一。

有关详细信息，请参阅 Generate Subsystem Code as Separate Function and Files (Simulink Coder)。

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Use subsystem name`。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RTWFcnNameOpts` |
| **值**：| `'Auto'` | `'Use subsystem name'` | `'User specified'` |

### **Function name** — 子系统代码的函数名称 无默认值

为子系统代码指定一个唯一、合法的 C 或 C++ 函数名称。

如果您想为函数指定特定名称，而不是让 Simulink Coder 代码生成器分配其自动生成的名称或使用子系统名称，请使用此参数。有关详细信息，请参阅 Generate Subsystem Code as Separate Function and Files (Simulink Coder)。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **Function name options** 设置为 `User specified`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RTWFcnName` |
| **值**：| `''`（默认）| 带引号的函数名称 |
| **Data Types:** | `char` | `string` |

### **File name options** — 如何命名生成的文件 `Auto` | `Use subsystem name` | `Use function name` | `User specified`

选择软件如何命名其为子系统生成的函数的单独文件。

- `Auto` — 根据子系统的配置以及模型中的实例数量，`Auto` 会产生不同的结果。

  - 如果代码生成器*不*为子系统生成单独的文件，则子系统代码生成在从子系统父系统生成的代码模块中。如果子系统父系统是模型本身，则子系统代码生成在 `model.c` 或 `model.cpp` 中。
  - 如果为 **Function packaging** 参数选择 `Reusable function` 且生成的代码处于源代码控制下，请考虑指定 `Auto` 以外的 **File name options** 值。这可以防止生成的文件名因无关的模型修改而更改，否则会对使用源代码控制管理配置造成问题。
  - 如果为 **Function packaging** 参数选择 `Reusable function`，并且模型引用层次结构包含可复用子系统的多个实例，则为了生成该子系统的可复用代码，**File name options** 必须设置为 `Auto`。
- `Use subsystem name` — 代码生成器生成单独的文件，使用子系统（或库模块）名称作为文件名。

  当 **File name options** 设置为 `Use subsystem name` 时，如果模型包含 Model 模块，或者正在为模型生成模型引用目标，则子系统文件名会被改编。在这些情况下，子系统的文件名由子系统名称加上模型名称前缀组成。
- `Use function name` — 代码生成器使用由 **Function name options** 指定的函数名称作为文件名。
- `User specified` — 此选项启用 **File name (no extension)** 文本输入字段。代码生成器使用您输入的名称作为文件名。输入任何文件名，但不要包含 `.c` 或 `.cpp`（或任何其他）扩展名。此文件名不必唯一。

  虽然子系统源文件名不必唯一，但必须避免使用会导致循环依赖的非唯一名称。例如，`sys_a.h` 包含 `sys_b.h`，`sys_b.h` 包含 `sys_c.h`，而 `sys_c.h` 包含 `sys_a.h`。

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Use function name`。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RTWFileNameOpts` |
| **值**：| `'Auto'` | `'Use subsystem name'` | `'Use function name'` | `'User specified'` |

### **File name (no extension)** — 生成文件的名称，无默认值

你指定的文件名不必唯一。但是，请避免使用会导致循环依赖的非唯一名称。例如，`sys_a.h` 包含 `sys_b.h`，`sys_b.h` 包含 `sys_c.h`，而 `sys_c.h` 包含 `sys_a.h`。

有关详细信息，请参阅 Generate Subsystem Code as Separate Function and Files (Simulink Coder)。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **File name options** 设置为 `User specified`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RTWFileName` |
| **值**：| `''` (default) | filename in quotes |
| **Data Types:** | `char` | `string` |

### **Function interface** — 如何使用生成函数的参数 `void_void` (default) | `Allow arguments (Optimized)` | `Allow arguments (Match graphical interface)`

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
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `FunctionInterfaceSpec` |
| **值**：| `'void_void'` (default) | `'Allow arguments (Optimized)'` | `'Allow arguments (Match graphical interface)'` |

### **Function with separate data** — 控制子系统代码生成 `off` (default) | `on`

生成子系统函数代码，其中原子子系统的内部数据与其父模型分离，并由子系统拥有。

- `off` — 不生成子系统函数代码，其中原子子系统的内部数据与其父模型分离，并由子系统拥有。
- `on` — 生成子系统函数代码，其中原子子系统的内部数据与其父模型分离，并由子系统拥有。子系统数据结构独立于父模型数据结构声明。具有分离数据的子系统拥有自己的模块 I/O 和 `DWork` 数据结构。因此，子系统的生成代码更易于跟踪和测试。数据分离还倾向于减小整个模型中全局数据结构的最大大小，因为它们被拆分为多个数据结构。

有关如何为原子子系统生成模块化函数代码的详细信息，请参阅 Generate Modular Function Code for Nonvirtual Subsystems (Embedded Coder)。

有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `FunctionWithSeparateData` |
| **值**：| `'off'` (default) | `'on'` |

### **Memory section for initialize/terminate functions** — 如何应用内存段 `Inherit from model` (default) | `Default` | model memory section

选择软件如何将内存段应用于子系统初始化和终止函数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 可能的值因你为模型配置设置的任何内存段包而异。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder) 和 Model Configuration Parameters: Code Generation (Simulink Coder)。
- 如果你尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RTWMemSecFuncInitTerm` |
| **值**：| `'Inherit from model'` (default) | `'Default'` | model memory section in quotes |

### **Memory section for execution functions** — 如何应用内存段 `Inherit from model` (default) | `Default` | model memory section

选择 Embedded Coder 如何将内存段应用于子系统执行函数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 可能的值因你为模型配置设置的任何内存段包而异。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder) 和 Model Configuration Parameters: Code Generation (Simulink Coder)。
- 如果你尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RTWMemSecFuncExecute` |
| **值**：| `'Inherit from model'` (default) | `'Default'` | model memory section in quotes |

### **Memory section for constants** — 如何应用内存段 `Inherit from model` (default) | `Default` | model memory section

选择软件如何将内存段应用于子系统常量。

- `Inherit from model` — 将根模型内存段应用于子系统数据。
- `Default` — 不将内存段应用于子系统数据，覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 你指定的内存段应用于生成代码中相应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值因你为模型配置设置的任何内存段包而异。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果你尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 并选择 **Function with separate data** 参数。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RTWMemSecDataConstants` |
| **值**：| `'Inherit from model'` (default) | `'Default'` | model memory section in quotes |

### **Memory section for internal data** — 如何应用内存段 `Inherit from model` (default) | `Default` | model memory section

选择软件如何将内存段应用于子系统内部数据。

- `Inherit from model` — 将根模型内存段应用于子系统数据。
- `Default` — 不将内存段应用于子系统数据，覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 你指定的内存段应用于生成代码中相应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值因你为模型配置设置的任何内存段包而异。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果你尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 并选择 **Function with separate data** 参数。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RTWMemSecDataInternal` |
| **值**：| `'Inherit from model'` (default) | `'Default'` | model memory section in quotes |

### **Memory section for parameters** — 如何应用内存段 `Inherit from model` (default) | `Default` | model memory section

选择软件如何将内存段应用于子系统参数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 你指定的内存段应用于生成代码中相应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值因你为模型配置设置的任何内存段包而异。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果你尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 并选择 **Function with separate data** 参数。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RTWMemSecDataParameters` |
| **值**：| `'Inherit from model'` (default) | `'Default'` | model memory section in quotes |

## 所属库

Simulink / Matrix Operations

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**Limitations**

- 如果 Array Processing Subsystem 模块位于模型的顶层，则该模块不支持 HDL 代码生成。
- 如果模型未选择 **Enable frame to sample conversion (HDL Coder)** 模型配置参数，则 Array Processing Subsystem 模块不支持 HDL 代码生成。

## 版本历史

**在 R2024a 中引入**

### R2025a: MATLAB Function block support

你可以在 Array Processing Subsystem 模块内使用 MATLAB Function 模块。

### R2024b: HDL code generation support

如果你拥有 HDL Coder™ 许可证，则可以为 Array Processing Subsystem 模块生成 HDL 代码。

## 描述

将算法应用于矩阵的每个元素

Array Processing Subsystem 模块是一个 Neighborhood Processing Subsystem 模块，它使用标量邻域将算法应用于输入矩阵的每个元素。在每个迭代步骤中，子系统内部的输入端口从输入矩阵接收一个元素。子系统内部的输出端口接收一个标量值，子系统将该值用作输出矩阵中对应元素的值。输出矩阵表示将子系统内部的算法应用于输入矩阵的每个元素的结果，类似于 `arrayfun` 函数和 For Each Subsystem 模块。

Array Processing Subsystem 模块针对大型输入矩阵（如图像数据）进行了优化。使用 Array Processing Subsystem 模块执行高性能的逐元素操作，如图像处理任务。

Array Processing Subsystem 模块包含一个 Array Processing 模块，该模块充当子系统的控制模块。
