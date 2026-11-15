---
type: simulink-block
title: 'Pixel Processing Subsystem'
family: matrix-operations
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'pixelprocessingsubsystem'
language: zh-CN
chinese_source: worker-translation
---

# Pixel Processing Subsystem



创建将多通道图像数据转换为单通道的算法

## 库

Simulink / Matrix Operations

## 描述

Pixel Processing Subsystem 模块是一个 Neighborhood Processing Subsystem 模块，它接受三维输入矩阵。Pixel Processing Subsystem 模块通过处理输入矩阵元素周围的 1-by-1-by-*`n`* 邻域矩阵，将邻域模式应用于输入矩阵，其中 *`n`* 是输入矩阵第三维的大小。Pixel Processing Subsystem 模块的行为等效于将 **Neighborhood size** 参数设置为 `[1,1,n]` 且将 **Padding option** 参数设置为 `Valid` 的 Neighborhood Processing Subsystem 模块。

Pixel Processing Subsystem 模块生成一个二维输出矩阵，其第一维和第二维与输入矩阵相同。使用 Pixel Processing Subsystem 将多通道图像数据转换为单通道图像数据。在每个迭代步骤中，子系统处理一个 1-by-1-by*`n`* 邻域，该邻域表示输入图像中一个像素的通道值，并推导出一个单值以放置在输出矩阵的对应像素中。

Pixel Processing Subsystem 包含一个 Pixel Processing 模块，它充当该子系统的控制模块。

## 端口

### 输入

### **In** — 子系统矩阵的信号输入

使用 Inport 模块从局部环境获取信号。

在 Pixel Processing Subsystem 模块中放置 Inport 模块会向该子系统添加一个外部输入端口。端口标签与 Inport 模块的名称匹配。使用 Neighborhood control block 配置要使用邻域模式处理哪些输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 输出

### **Out** — 子系统矩阵的信号输出

使用 Outport 模块将信号发送到局部环境。

在 Pixel Processing Subsystem 模块中放置 Outport 模块会从该子系统添加一个外部输出端口。端口标签与 Outport 模块的名称匹配。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

若要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，从 **Prepare** 库中选择 **Property Inspector**。

### 主要

### **Show port labels** — 端口标签的显示选项 `FromPortIcon` (默认) | `FromPortBlockName` | `SignalName` | `none`

选择如何在 Subsystem 模块图标上显示端口标签。

- `none` — 不显示端口标签。
- `FromPortIcon` — 如果对应端口图标显示信号名称，则在 Subsystem 模块上显示该信号名称。否则，显示端口模块名称，或者如果模块名称为默认名称，则显示端口号。
- `FromPortBlockName` — 在 Subsystem 模块上显示对应端口模块的名称。
- `SignalName` — 如果连接到端口的信号已命名，则在 Subsystem 模块上显示该信号的名称。否则，显示对应端口模块的名称。

有关 Subsystem 模块上的端口标签编辑，请参阅 Edit Port Labels on Subsystem Blocks。

#### 程序化使用

若要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ShowPortLabels` |
| **值：** | `'FromPortIcon'` (默认) | `'FromPortBlockName'` | `'SignalName'` | `'none'` |

### **Read/Write permissions** — 对子系统内容的访问级别 `ReadWrite` (默认) | `ReadOnly` | `NoReadOrWrite`

控制用户对子系统内容的访问。

- `ReadWrite` — 允许打开和修改子系统内容。
- `ReadOnly` — 允许打开子系统，但不允许修改。如果子系统位于模块库中，您可以创建并打开指向该子系统的链接，也可以制作并修改该子系统的本地副本，但不能更改权限或修改原始库实例的内容。
- `NoReadOrWrite` — 禁止打开或修改子系统。如果子系统位于库中，您可以在模型中创建指向该子系统的链接，但不能打开、修改、更改权限或创建该子系统的本地副本。

如果尝试查看 **Read/Write permissions** 参数设置为 `NoReadOrWrite` 的子系统内容，您不会收到任何响应。例如，双击此类子系统时，软件不会打开该子系统，也不会显示任何消息。

#### 程序化使用

若要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Permissions` |
| **值：** | `'ReadWrite'` (默认) | `'ReadOnly'` | `'NoReadOrWrite'` |

### **Name of error callback function** — 发生错误时要调用的函数名称 无默认值

输入当软件执行子系统期间发生错误时要调用的函数名称。

软件向该函数传递两个参数：子系统的句柄，以及指定错误类型的字符向量。如果未指定函数，则当执行子系统导致错误时，软件会显示一般错误消息。

#### 程序化使用

若要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ErrorFcn` |
| **值：** | `''` (默认) | 带引号的函数名 |
| **数据类型：** | `char` | `string` |

### **Permit hierarchical resolution** — 工作区变量名称的解析 `All` (默认) | `ExplicitOnly` | `None`

选择是否解析此子系统引用的工作区变量名称。

有关详细信息，请参阅 Symbol Resolution 和 Symbol Resolution Process。

- `All` — 解析此子系统使用的所有工作区变量名称，包括用于指定模块参数值和 Simulink 数据对象（例如 `Simulink.Signal` 对象）的名称。
- `ExplicitOnly` — 仅解析用于指定模块参数值、数据存储内存（不存在模块的位置）、信号以及标记为“must resolve”的状态的工作区变量名称。
- `None` — 不解析任何工作区变量名称。

#### 程序化使用

若要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PermitHierarchicalResolution` |
| **值：** | `'All'` (默认) | `'ExplicitOnly'` | `'None'` |

### **Show subsystem reinitialize ports** — 显示重新初始化事件端口的选项 `off` (默认) | `on`

选中此参数可显示重新初始化事件端口。清除此参数可移除这些端口。

#### 依赖关系

要启用此参数，请选择 **Treat as atomic unit**。

#### 程序化使用

若要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ShowSubsystemReinitializePorts` |
| **值：** | `'off'` (默认) | `'on'` |

### 代码生成

Code Generation 选项卡上的参数需要 Simulink Coder™ 或 Embedded Coder® 许可证。

### **Function packaging** — 代码格式 `Auto` | `Inline` | `Nonreusable function` | `Reusable function`

选择要为原子（非虚拟）子系统生成的代码格式。

- `Auto` — 软件根据模型中存在的子系统实例的类型和数量为您选择最佳格式。
- `Inline` — 软件无条件地内联该子系统。
- `Nonreusable function` — 如果 **Filename options** 设置为 `Auto`，软件会将单独的函数打包在模型文件中。如果 **File name options** 设置为 `Use subsystem name`、`Use function name` 或 `User specified` 并使用不同的文件名，软件会将单独的函数打包在单独的文件中。

  使用此设置的子系统生成的函数可能带有参数，具体取决于 Function interface 参数设置。您可以分别使用 Function name 和 File name (no extension) 参数为生成的函数和文件命名。这些函数不可重入。

- `Reusable function` — 软件生成带参数的函数，当模型包含子系统的多个实例时，允许重用子系统代码。

  此选项还生成带参数的函数，允许在模型引用层次结构的生成代码中重用子系统代码，该层次结构跨被引用模型包含子系统的多个实例。在这种情况下，子系统必须位于库中。

有关详细信息，请参阅：

- Generate Code and Executables for Individual Subsystems (Simulink Coder)
- Generate Inlined Subsystem Code (Simulink Coder)
- Generate Subsystem Code as Separate Function and Files (Simulink Coder)
- Generate Reusable Code from Library Subsystems Shared Across Models (Simulink Coder)

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Reusable function`。

#### 提示

- 当您希望将子系统的多个实例表示为一个可重用函数时，可以将它们分别指定为 `Auto` 或 `Reusable function`。最好只使用其中一种，因为同时使用两者会创建两个可重用函数，每个指定对应一个。这些选择的结果仅在无法重用时才有所不同。选择 `Auto` 不允许控制子系统代码的函数或文件名。
- `Reusable function` 和 `Auto` 选项都会尝试确定是否存在子系统的多个实例以及代码是否可以重用。每个选项行为之间的区别在于，当无法重用时：

  - `Auto` 生成内联代码，或者如果情况禁止内联，则为每个子系统实例生成单独的函数。
  - `Reusable function` 为模型中的每个子系统实例生成一个带参数的单独函数。
- 如果生成代码处于源代码管理下时选择 `Reusable function`，请将 **File name options** 设置为 `Use subsystem name`、`Use function name` 或 `User specified`。否则，每次修改模型时，代码文件的名称都会更改，这会妨碍对文件进行源代码管理。
- 如果选择 `Auto` 或 `Inline` 之外的选项，并且模型配置参数 **States**，代码生成器会生成单独的输出和更新方法。代码生成器不会考虑 **Combine output and update methods for code generation and simulation** 规范。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证才能进行代码生成。
- 要启用此参数，请选择 **Treat as atomic unit**。

#### 程序化使用

若要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWSystemCode` |
| **值：** | `'Auto'` | `'Inline'` | `'Nonreusable function'` | `'Reusable function'` |

### **Function name options** — 如何命名生成的函数 `Auto` | `Use subsystem name` | `User specified`

选择软件如何为子系统生成的函数命名。

如果您拥有 Embedded Coder 许可证，则可以使用 Configuration Parameter **Code Generation** > **Identifiers** 窗格上的选项控制函数名称。

- `Auto` — 使用默认命名约定 `model_subsystem()` 分配唯一函数名称，其中 *`model`* 是模型名称，*`subsystem`* 是子系统名称，或者在代码正在重用时为相同子系统的名称。

  如果为 **Function packaging** 参数选择 `Reusable function`，并且模型引用层次结构包含可重用子系统的多个实例，则为了为该子系统生成可重用代码，**Function name options** 必须设置为 `Auto`。
- `Use subsystem name` — 使用子系统名称作为函数名称。默认情况下，函数名称使用命名约定 `model_subsystem`。

  当子系统位于库模块中，并且子系统参数 Function packaging 设置为 `Reusable function` 时，如果设置 `Use subsystem name` 选项，代码生成器会使用库模块的名称作为子系统函数名称和文件名。
- `User specified` — 启用 **Function name** 字段。输入任何合法的 C 或 C++ 函数名称，该名称必须唯一。

有关详细信息，请参阅 Generate Subsystem Code as Separate Function and Files (Simulink Coder)。

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Use subsystem name`。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 程序化使用

若要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFcnNameOpts` |
| **值：** | `'Auto'` | `'Use subsystem name'` | `'User specified'` |

### **Function name** — 子系统代码的函数名称 无默认值

为子系统代码指定一个唯一、合法的 C 或 C++ 函数名称。

如果您希望为该函数指定特定名称，而不是让 Simulink Coder 代码生成器分配其自己的自动生成名称或使用子系统名称，请使用此参数。有关详细信息，请参阅 Generate Subsystem Code as Separate Function and Files (Simulink Coder)。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **Function name options** 设置为 `User specified`。

#### 程序化使用

若要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFcnName` |
| **值：** | `''` (默认) | 带引号的函数名 |
| **数据类型：** | `char` | `string` |

### **File name options** — 如何命名生成的文件 `Auto` | `Use subsystem name` | `Use function name` | `User specified`

选择软件如何为子系统生成的函数命名单独的文件。

- `Auto` — 根据子系统的配置以及模型中的实例数量，`Auto` 会产生不同的结果。

  - 如果代码生成器 *不* 为子系统生成单独的文件，则子系统代码会在从子系统父系统生成的代码模块中生成。如果子系统父系统是模型本身，则子系统代码在 `model.c` 或 `model.cpp` 中生成。
  - 如果为 **Function packaging** 参数选择 `Reusable function`，并且生成代码处于源代码管理下，请考虑指定 `Auto` 以外的 **File name options** 值。这可以防止生成的 filename 因不相关的模型修改而更改，而这对使用源代码管理来管理配置是有问题的。
  - 如果为 **Function packaging** 参数选择 `Reusable function`，并且模型引用层次结构包含可重用子系统的多个实例，则为了为该子系统生成可重用代码，**File name options** 必须设置为 `Auto`。
- `Use subsystem name` — 代码生成器生成单独的文件，使用子系统（或库模块）名称作为 filename。

  当 **File name options** 设置为 `Use subsystem name` 时，如果模型包含 Model 模块，或者正在为模型生成模型引用目标，则会修改子系统 filename。在这些情况下，子系统的 filename 由前缀为模型名称的子系统名称组成。
- `Use function name` — 代码生成器使用由 **Function name options** 指定的函数名称作为 filename。
- `User specified` — 此选项启用 **File name (no extension)** 文本输入字段。代码生成器使用您输入的名称作为 filename。输入任何 filename，但不要包含 `.c` 或 `.cpp`（或任何其他）扩展名。此 filename 不必唯一。

  虽然子系统源 filename 不必唯一，但必须避免给出会导致循环依赖的非唯一名称。例如，`sys_a.h` 包含 `sys_b.h`，`sys_b.h` 包含 `sys_c.h`，而 `sys_c.h` 包含 `sys_a.h`。

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Use function name`。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 程序化使用

若要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFileNameOpts` |
| **值：** | `'Auto'` | `'Use subsystem name'` | `'Use function name'` | `'User specified'` |

### **File name (no extension)** — 生成文件的名称 无默认值

您指定的 filename 不必唯一。但是，避免给出会导致循环依赖的非唯一名称。例如，`sys_a.h` 包含 `sys_b.h`，`sys_b.h` 包含 `sys_c.h`，而 `sys_c.h` 包含 `sys_a.h`。

有关详细信息，请参阅 Generate Subsystem Code as Separate Function and Files (Simulink Coder)。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **File name options** 设置为 `User specified`。

#### 程序化使用

若要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFileName` |
| **值：** | `''` (默认) | 带引号的 filename |
| **数据类型：** | `char` | `string` |

### **Function interface** — 如何对生成的函数使用参数 `void_void` (默认) | `Allow arguments (Optimized)` | `Allow arguments (Match graphical interface)`

选择如何对生成的函数使用参数。

- `void_void` — 生成不带参数的函数，并将数据作为全局变量传递。例如：

        void subsystem_function(void)

- `Allow arguments (Optimized)` — 生成使用参数而不是将数据作为全局变量传递的函数。此规范可减少全局 RAM。此选项可能会减小代码大小并提高执行速度，并使代码生成器能够应用其他优化。例如：

        void subsystem_function(real_T rtu_In1, real_T rtu_In2,
                                real_T *rty_Out1)

  在某些情况下，生成优化代码时，代码生成器可能不会生成带参数的函数。
- `Allow arguments (Match graphical interface)` — 生成使用与 Subsystem 图形模块接口匹配的参数的函数接口。生成的函数接口是可预测的，并且不会更改。可预测的接口可用于调试和测试代码以及与外部应用程序集成。例如，如果模型有两个 Inport 模块和两个 Outport 模块，则生成的函数接口为：

        void subsystem_function(real_T rtu_In1, real_T rtu_In2,
                                real_T *rty_Out1, real_T *rty_Out2)

有关详细信息，请参阅：

- Reduce Global Variables in Nonreusable Subsystem Functions (Embedded Coder)
- Generate Predictable Function Interface to Match Graphical Block Interface (Embedded Coder)
- Generate Modular Function Code for Nonvirtual Subsystems (Embedded Coder)

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function`。

#### 程序化使用

若要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FunctionInterfaceSpec` |
| **值：** | `'void_void'` (默认) | `'Allow arguments (Optimized)'` | `'Allow arguments (Match graphical interface)'` |

### **Function with separate data** — 控制子系统的代码生成 `off` (默认) | `on`

生成子系统函数代码，其中原子子系统的内部数据与其父模型分离，并由该子系统拥有。

- `off` — 不生成这样的子系统函数代码：其中原子子系统的内部数据与其父模型分离并由该子系统拥有。
- `on` — 生成子系统函数代码，其中原子子系统的内部数据与其父模型分离，并由该子系统拥有。子系统数据结构与父模型数据结构独立声明。具有单独数据的子系统拥有自己的模块 I/O 和 `DWork` 数据结构。因此，子系统的生成代码更易于跟踪和测试。数据分离还倾向于减小整个模型中全局数据结构的最大大小，因为它们被拆分为多个数据结构。

有关如何为原子子系统生成模块化函数代码的详细信息，请参阅 Generate Modular Function Code for Nonvirtual Subsystems (Embedded Coder)。

有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function`。

#### 程序化使用

若要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FunctionWithSeparateData` |
| **值：** | `'off'` (默认) | `'on'` |

### **Memory section for initialize/terminate functions** — 如何应用内存段 `Inherit from model` (默认) | `Default` | model memory section

选择软件如何将内存段应用于子系统初始化和终止函数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，从而覆盖任何模型级规范。
- 将模型内存段之一应用于该子系统。

#### 提示

- 可能的值取决于您为模型配置设置的内存段包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder) 和 Model Configuration Parameters: Code Generation (Simulink Coder)。
- 如果尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 以及模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 程序化使用

若要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecFuncInitTerm` |
| **值：** | `'Inherit from model'` (默认) | `'Default'` | 带引号的 model memory section |

### **Memory section for execution functions** — 如何应用内存段 `Inherit from model` (默认) | `Default` | model memory section

选择 Embedded Coder 如何将内存段应用于子系统执行函数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，从而覆盖任何模型级规范。
- 将模型内存段之一应用于该子系统。

#### 提示

- 可能的值取决于您为模型配置设置的内存段包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder) 和 Model Configuration Parameters: Code Generation (Simulink Coder)。
- 如果尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 以及模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 程序化使用

若要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecFuncExecute` |
| **值：** | `'Inherit from model'` (默认) | `'Default'` | 带引号的 model memory section |

### **Memory section for constants** — 如何应用内存段 `Inherit from model` (默认) | `Default` | model memory section

选择软件如何将内存段应用于子系统常量。

- `Inherit from model` — 将根模型内存段应用于子系统数据。
- `Default` — 不将内存段应用于子系统数据，从而覆盖任何模型级规范。
- 将模型内存段之一应用于该子系统。

#### 提示

- 您指定的内存段应用于生成代码中对应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值取决于您为模型配置设置的内存段包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 以及模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function`，并选择 **Function with separate data** 参数。

#### 程序化使用

若要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataConstants` |
| **值：** | `'Inherit from model'` (默认) | `'Default'` | 带引号的 model memory section |

### **Memory section for internal data** — 如何应用内存段 `Inherit from model` (默认) | `Default` | model memory section

选择软件如何将内存段应用于子系统内部数据。

- `Inherit from model` — 将根模型内存段应用于子系统数据。
- `Default` — 不将内存段应用于子系统数据，从而覆盖任何模型级规范。
- 将模型内存段之一应用于该子系统。

#### 提示

- 您指定的内存段应用于生成代码中对应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值取决于您为模型配置设置的内存段包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 以及模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function`，并选择 **Function with separate data** 参数。

#### 程序化使用

若要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataInternal` |
| **值：** | `'Inherit from model'` (默认) | `'Default'` | 带引号的 model memory section |

### **Memory section for parameters** — 如何应用内存段 `Inherit from model` (默认) | `Default` | model memory section

选择软件如何将内存段应用于子系统参数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，从而覆盖任何模型级规范。
- 将模型内存段之一应用于该子系统。

#### 提示

- 您指定的内存段应用于生成代码中对应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值取决于您为模型配置设置的内存段包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 以及模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function`，并选择 **Function with separate data** 参数。

#### 程序化使用

若要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataParameters` |
| **值：** | `'Inherit from model'` (默认) | `'Default'` | 带引号的 model memory section |

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2025a：MATLAB Function 模块支持

您可以在 Pixel Processing Subsystem 模块内使用 MATLAB Function 模块。
