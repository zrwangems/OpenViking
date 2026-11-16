---
type: simulink-block
title: 'Neighborhood Processing Subsystem'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Code Generation from Simulink / Speed and Area Optimization / I/O Optimization'
documentation_page: 'neighborhoodprocessingsubsystem'
documentation_source_path: '../simulink/slref/neighborhoodprocessingsubsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Neighborhood Processing Subsystem



创建遵循邻域模式的算法

## 库

Simulink / Matrix Operations

## 描述

Neighborhood Processing Subsystem 模块是预配置为创建遵循邻域模式的子系统的起点的 Subsystem 模块。在每个仿真时间步，子系统迭代输入数组的每个元素。对于每个元素，子系统处理围绕该元素的邻域值。将该子系统用于图像处理。某些图像处理算法涉及分块处理图像，而不是一次处理整个图像。

### 配置子系统

Neighborhood Processing Subsystem 包含一个 Neighborhood 模块，该模块充当子系统的控制模块。指定 Neighborhood 模块的参数以配置子系统的行为。

**邻域大小** 参数控制邻域的维度。对于输入矩阵边缘附近的元素，邻域可能延伸到输入矩阵之外。**填充选项** 参数控制子系统如何处理来自输入矩阵外部的值。可以将子系统配置为使用常量填充这些值，或通过重用矩阵内部的值来填充。如果使用 `Constant` 填充选项，请使用 **填充常量** 参数设置常量值。

可以将 Neighborhood Processing Subsystem 模块配置为仅处理输入矩阵的某些元素。使用 **步幅** 参数将 Neighborhood Processing Subsystem 模块配置为在每次迭代时跳过一定数量的元素。使用 **处理偏移量** 和 **处理宽度** 参数分别定义图像中感兴趣区域 (ROI) 的左上边界和右下边界。Neighborhood Processing Subsystem 模块仅迭代该区域。

**输出大小** 参数控制输出矩阵的大小。`Same` 值将输出矩阵配置为与 ROI 大小相同。`Full` 值通过为 ROI 之外但其邻域包含至少一个来自 ROI 的元素的元素计算值，生成更大的输出矩阵。`Valid` 值通过仅为邻域不超出 ROI 的元素计算值，生成更小的输出矩阵。使用此设置时，**填充常量** 参数被禁用。

### 示例

考虑此模型。

一个包含值为 "ones(5,5)" 的 Constant 模块的模型，该模块传递给 Neighborhood Processing Subsystem，后者输出到 Display 模块。Display 模块不显示任何值。

在此示例中，Neighborhood Processing Subsystem 模块获取 5×5 矩阵，并使用 `Same` 输出大小选项输出相同维度的矩阵。该子系统包含以下模块。

一个包含一个输入端口和一个输出端口的 Neighborhood Processing Subsystem。输入端口连接到 Sum of Elements 模块，该模块输出到输出端口。

在 Neighborhood Processing Subsystem 模块内部，输入端口不会接收完整的 5×5 矩阵。相反，由于 **邻域大小** 参数值为 `[3 3]`，输入端口接收一个更小的 3×3 元素窗口。子系统迭代输入矩阵的元素，在每次迭代时将每个元素的邻域传递到输入端口。

该模型使用 `Constant` 填充选项，填充值为 `0`。对于延伸到输入矩阵之外的邻域，子系统将外部值视为 `0`。

Neighborhood Processing Subsystem 模块的输出端口接收一个标量，该标量表示窗口中心元素的派生值。在此情况下，**Sum over** 参数设置为 `All dimensions` 的 Sum of Elements 模块为每个窗口生成一个标量，表示该窗口中值的和。

运行模型以填充 Display 模块。

与之前相同的模型，Display 模块填充了一个 5×5 矩阵。内部 9 个元素的值为 9，角元素的值为 4，非角边缘元素的值为 6。

输出矩阵的每个值是对应元素及其在输入矩阵中的八个直接相邻元素的和。内部元素周围都是 `1`，因此值为 `9`。外部元素的值较低，因为所选填充方法对输入矩阵外部的元素使用值 `0`。

## 端口

### 输入

### **In** — 到子系统的信号输入 矩阵 | 向量

使用 Inport 模块从局部环境获取信号。

在 Neighborhood Processing Subsystem 模块中放置 Inport 模块会向子系统添加一个外部输入端口。端口标签与 Inport 模块的名称匹配。使用 Neighborhood 控制模块配置要使用邻域模式处理哪些输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 输出

### **Out** — 来自子系统的信号输出 矩阵 | 向量

使用 Outport 模块将信号发送到局部环境。

在 Neighborhood Processing Subsystem 模块中放置 Outport 模块会从子系统添加一个外部输出端口。端口标签与 Outport 模块的名称匹配。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### Main

### **显示端口标签** — 端口标签的显示选项 `FromPortIcon` (默认) | `FromPortBlockName` | `SignalName` | `none`

选择如何在 Subsystem 模块图标上显示端口标签。

- `none` — 不显示端口标签。
- `FromPortIcon` — 如果对应的端口图标显示信号名称，则在 Subsystem 模块上显示该信号名称。否则，显示端口模块名称；如果模块名称是默认名称，则显示端口号。
- `FromPortBlockName` — 在 Subsystem 模块上显示对应端口模块的名称。
- `SignalName` — 如果连接到端口的信号已命名，则在 Subsystem 模块上显示该信号名称。否则，显示对应端口模块的名称。

有关 Subsystem 模块上的端口标签编辑，请参阅 Edit Port Labels on Subsystem Blocks。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ShowPortLabels` |
| **值：** | `'FromPortIcon'` (默认) | `'FromPortBlockName'` | `'SignalName'` | `'none'` |

### **读/写权限** — 对子系统内容的访问级别 `ReadWrite` (默认) | `ReadOnly` | `NoReadOrWrite`

控制用户对子系统内容的访问。

- `ReadWrite` — 允许打开和修改子系统内容。
- `ReadOnly` — 允许打开但不允许修改子系统。如果子系统位于模块库中，可以创建并打开指向该子系统的链接，并可以创建和修改子系统的本地副本，但不能更改权限或修改原始库实例的内容。
- `NoReadOrWrite` — 禁止打开或修改子系统。如果子系统位于库中，可以在模型中创建指向该子系统的链接，但不能打开、修改、更改权限或创建子系统的本地副本。

如果尝试查看 **读/写权限** 参数设置为 `NoReadOrWrite` 的子系统的内容，不会收到响应。例如，双击此类子系统时，软件不会打开该子系统，也不会显示任何消息。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Permissions` |
| **值：** | `'ReadWrite'` (默认) | `'ReadOnly'` | `'NoReadOrWrite'` |

### **错误回调函数名称** — 发生错误时要调用的函数名称 无默认值

输入在软件执行子系统期间发生错误时要调用的函数名称。

软件向该函数传递两个参数：子系统的句柄以及指定错误类型的字符向量。如果未指定函数，则当执行子系统导致错误时，软件显示一般错误消息。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ErrorFcn` |
| **值：** | `''` (默认) | 带引号的函数名称 |
| **数据类型：** | `char` | `string` |

### **允许层次化解析** — 工作区变量名称的解析 `All` (默认) | `ExplicitOnly` | `None`

选择是否解析此子系统引用的工作区变量名称。

有关详细信息，请参阅 Symbol Resolution and Symbol Resolution Process。

- `All` — 解析此子系统使用的所有工作区变量名称，包括用于指定模块参数值和 Simulink 数据对象（例如 `Simulink.Signal` 对象）的名称。
- `ExplicitOnly` — 仅解析用于指定模块参数值、数据存储内存（不存在对应模块时）、信号以及标记为“必须解析”的状态的工作区变量名称。
- `None` — 不解析任何工作区变量名称。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PermitHierarchicalResolution` |
| **值：** | `'All'` (默认) | `'ExplicitOnly'` | `'None'` |

### **显示子系统重新初始化端口** — 显示重新初始化事件端口的选项 `off` (默认) | `on`

选择此参数以显示重新初始化事件端口。清除此参数以移除这些端口。

#### 依赖关系

要启用此参数，请选择 **视为原子单元**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ShowSubsystemReinitializePorts` |
| **值：** | `'off'` (默认) | `'on'` |

### 代码生成

**Code Generation** 选项卡上的参数需要 Simulink Coder™ 或 Embedded Coder® 许可证。

### **函数打包** — 代码格式 `Auto` | `Inline` | `Nonreusable function` | `Reusable function`

选择要为原子（非虚拟）子系统生成的代码格式。

- `Auto` — 软件根据模型中存在的子系统的类型和实例数量为您选择最佳格式。
- `Inline` — 软件无条件地内联该子系统。
- `Nonreusable function` — 如果 **文件名选项** 设置为 `Auto`，软件在模型文件中打包单独的函数。如果 **文件名选项** 设置为 `Use subsystem name`、`Use function name` 或使用不同文件名的 `User specified`，软件在单独的文件中打包单独的函数。

  使用此设置的子系统生成的函数可能带有参数，具体取决于 Function interface 参数设置。可以分别使用 Function name 和 File name (no extension) 参数命名生成的函数和文件。这些函数不可重入。
- `Reusable function` — 软件生成带参数的函数，当模型包含子系统的多个实例时，允许重用子系统代码。

  此选项还会生成带参数的函数，允许在包含跨引用模型中子系统多个实例的模型引用层次的生成代码中重用子系统代码。在这种情况下，子系统必须位于库中。

有关详细信息，请参阅：

- Generate Code and Executables for Individual Subsystems (Simulink Coder)
- Generate Inlined Subsystem Code (Simulink Coder)
- Generate Subsystem Code as Separate Function and Files (Simulink Coder)
- Generate Reusable Code from Library Subsystems Shared Across Models (Simulink Coder)

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Reusable function`。

#### 提示

- 当希望将子系统的多个实例表示为一个可重用函数时，可以将每个实例指定为 `Auto` 或 `Reusable function`。最好只使用其中一种，因为同时使用两者会创建两个可重用函数，每种指定各一个。这些选择的结果仅在无法重用时才不同。选择 `Auto` 不允许控制子系统代码的函数或文件名。
- `Reusable function` 和 `Auto` 选项都会尝试确定是否存在子系统的多个实例以及代码是否可以重用。每个选项行为的区别在于，当无法重用时：

  - `Auto` 会产生内联代码，或者如果情况禁止内联，则为每个子系统实例生成单独的函数。
  - `Reusable function` 会为模型中的每个子系统实例生成带参数的单独函数。
- 如果在生成的代码处于源代码控制下时选择 `Reusable function`，请将 **文件名选项** 设置为 `Use subsystem name`、`Use function name` 或 `User specified`。否则，代码文件的名称会在修改模型时更改，从而妨碍对文件进行源代码控制。
- 如果选择的选项不是 `Auto` 或 `Inline`，并且模型配置参数 **States**，代码生成器会生成单独的输出和更新方法。代码生成器不会考虑 **Combine output and update methods for code generation and simulation** 规范。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证才能进行代码生成。
- 要启用此参数，请选择 **视为原子单元**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWSystemCode` |
| **值：** | `'Auto'` | `'Inline'` | `'Nonreusable function'` | `'Reusable function'` |

### **函数名称选项** — 如何命名生成的函数 `Auto` | `Use subsystem name` | `User specified`

选择软件如何为子系统生成的函数命名。

如果拥有 Embedded Coder 许可证，可以使用 Configuration Parameter **Code Generation** > **Identifiers** 窗格上的选项控制函数名称。

- `Auto` — 使用默认命名约定分配唯一函数名称 `model_subsystem()`，其中 *`model`* 是模型名称，*`subsystem`* 是子系统名称；当代码被重用时，则是相同子系统的名称。

  如果为 **函数打包** 参数选择 `Reusable function`，并且模型引用层次包含可重用子系统的多个实例，则为了为该子系统生成可重用代码，**函数名称选项** 必须设置为 `Auto`。
- `Use subsystem name` — 使用子系统名称作为函数名称。默认情况下，函数名称使用命名约定 `model_subsystem`。

  当子系统位于库模块中，并且子系统参数 Function packaging 设置为 `Reusable function` 时，如果设置 `Use subsystem name` 选项，代码生成器会将库模块的名称用于子系统函数名称和文件名。
- `User specified` — 启用 **函数名称** 字段。输入任何合法的 C 或 C++ 函数名称，该名称必须唯一。

有关详细信息，请参阅 Generate Subsystem Code as Separate Function and Files (Simulink Coder)。

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Use subsystem name`。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFcnNameOpts` |
| **值：** | `'Auto'` | `'Use subsystem name'` | `'User specified'` |

### **函数名称** — 子系统代码的函数名称 无默认值

为子系统代码指定唯一、合法的 C 或 C++ 函数名称。

如果希望为函数指定特定名称，而不是让 Simulink Coder 代码生成器分配其自己的自动生成名称或使用子系统名称，请使用此参数。有关详细信息，请参阅 Generate Subsystem Code as Separate Function and Files (Simulink Coder)。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **函数名称选项** 设置为 `User specified`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFcnName` |
| **值：** | `''` (默认) | 带引号的函数名称 |
| **数据类型：** | `char` | `string` |

### **文件名选项** — 如何命名生成的文件 `Auto` | `Use subsystem name` | `Use function name` | `User specified`

选择软件如何为子系统生成的函数命名单独文件。

- `Auto` — 根据子系统的配置以及模型中的实例数量，`Auto` 会产生不同结果。

  - 如果代码生成器*不*为子系统生成单独文件，则子系统代码在从子系统父系统生成的代码模块中生成。如果子系统父系统是模型本身，则子系统代码在 `model.c` 或 `model.cpp` 中生成。
  - 如果为 **函数打包** 参数选择 `Reusable function`，并且生成的代码处于源代码控制下，请考虑指定 `Auto` 以外的 **文件名选项** 值。这可以防止生成的文件名由于无关的模型修改而更改，否则会妨碍使用源代码控制管理配置。
  - 如果为 **函数打包** 参数选择 `Reusable function`，并且模型引用层次包含可重用子系统的多个实例，则为了为该子系统生成可重用代码，**文件名选项** 必须设置为 `Auto`。
- `Use subsystem name` — 代码生成器生成单独文件，使用子系统（或库模块）名称作为文件名。

  当 **文件名选项** 设置为 `Use subsystem name` 时，如果模型包含 Model 模块，或者正在为模型生成模型引用目标，则子系统文件名会被改编。在这些情况下，子系统的文件名由子系统名称加上模型名称前缀组成。
- `Use function name` — 代码生成器使用 **函数名称选项** 指定的函数名称作为文件名。
- `User specified` — 此选项启用 **文件名（无扩展名）** 文本输入字段。代码生成器使用输入的名称作为文件名。输入任何文件名，但不要包含 `.c` 或 `.cpp`（或任何其他）扩展名。此文件名不需要唯一。

  虽然子系统源文件名不需要唯一，但必须避免使用导致循环依赖的非唯一名称。例如，`sys_a.h` 包含 `sys_b.h`，`sys_b.h` 包含 `sys_c.h`，而 `sys_c.h` 包含 `sys_a.h`。

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Use function name`。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFileNameOpts` |
| **值：** | `'Auto'` | `'Use subsystem name'` | `'Use function name'` | `'User specified'` |

### **文件名（无扩展名）** — 生成文件的名称 无默认值

指定的文件名不必唯一。但是，避免使用导致循环依赖的非唯一名称。例如，`sys_a.h` 包含 `sys_b.h`，`sys_b.h` 包含 `sys_c.h`，而 `sys_c.h` 包含 `sys_a.h`。

有关详细信息，请参阅 Generate Subsystem Code as Separate Function and Files (Simulink Coder)。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **文件名选项** 设置为 `User specified`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFileName` |
| **值：** | `''` (默认) | 带引号的文件名 |
| **数据类型：** | `char` | `string` |

### **函数接口** — 如何将参数与生成的函数一起使用 `void_void` (默认) | `Allow arguments (Optimized)` | `Allow arguments (Match graphical interface)`

选择如何将参数与生成的函数一起使用。

- `void_void` — 生成不带参数的函数，并将数据作为全局变量传递。例如：

    void subsystem_function(void)

- `Allow arguments (Optimized)` — 生成使用参数而不是将数据作为全局变量传递的函数。此规范可减少全局 RAM。此选项可能减小代码大小并提高执行速度，并使代码生成器能够应用额外优化。例如：

    void subsystem_function(real_T rtu_In1, real_T rtu_In2,
                            real_T *rty_Out1)

  在某些情况下，生成优化代码时，代码生成器可能不会生成带参数的函数。
- `Allow arguments (Match graphical interface)` — 生成使用与 Subsystem 图形模块接口匹配的参数的函数接口。生成的函数接口是可预测的，并且不会更改。可预测的接口对于调试和测试代码以及与外部应用程序集成可能很有用。例如，如果模型有两个 Inport 模块和两个 Outport 模块，则生成的函数接口为：

    void subsystem_function(real_T rtu_In1, real_T rtu_In2,
                            real_T *rty_Out1, real_T *rty_Out2)

有关详细信息，请参阅：

- Reduce Global Variables in Nonreusable Subsystem Functions (Embedded Coder)
- Generate Predictable Function Interface to Match Graphical Block Interface (Embedded Coder)
- Generate Modular Function Code for Nonvirtual Subsystems (Embedded Coder)

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FunctionInterfaceSpec` |
| **值：** | `'void_void'` (默认) | `'Allow arguments (Optimized)'` | `'Allow arguments (Match graphical interface)'` |

### **带独立数据的函数** — 控制子系统的代码生成 `off` (默认) | `on`

生成子系统函数代码，其中原子子系统的内部数据与其父模型分离，并由子系统拥有。

- `off` — 不生成其中原子子系统的内部数据与其父模型分离并由子系统拥有的子系统函数代码。
- `on` — 生成其中原子子系统的内部数据与其父模型分离并由子系统拥有的子系统函数代码。子系统数据结构独立于父模型数据结构声明。具有独立数据的子系统有其自己的模块 I/O 和 `DWork` 数据结构。因此，子系统的生成代码更易于跟踪和测试。数据分离还倾向于减小整个模型中全局数据结构的最大大小，因为它们被拆分为多个数据结构。

有关如何为原子子系统生成模块化函数代码的详细信息，请参阅 Generate Modular Function Code for Nonvirtual Subsystems (Embedded Coder)。

有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FunctionWithSeparateData` |
| **值：** | `'off'` (默认) | `'on'` |

### **初始化/终止函数的内存段** — 如何应用内存段 `Inherit from model` (默认) | `Default` | model memory section

选择软件如何将内存段应用于子系统初始化和终止函数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，覆盖任何模型级规范。
- 将某个模型内存段应用于子系统。

#### 提示

- 可能的值取决于为模型配置设置的 memory sections 包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder) 和 Model Configuration Parameters: Code Generation (Simulink Coder)。
- 如果尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 以及模型包包含的所有内存段。
- 这些选项对于覆盖给定子系统的模型内存段设置可能很有用。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecFuncInitTerm` |
| **值：** | `'Inherit from model'` (默认) | `'Default'` | 带引号的模型内存段 |

### **执行函数的内存段** — 如何应用内存段 `Inherit from model` (默认) | `Default` | model memory section

选择 Embedded Coder 如何将内存段应用于子系统执行函数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，覆盖任何模型级规范。
- 将某个模型内存段应用于子系统。

#### 提示

- 可能的值取决于为模型配置设置的 memory sections 包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder) 和 Model Configuration Parameters: Code Generation (Simulink Coder)。
- 如果尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 以及模型包包含的所有内存段。
- 这些选项对于覆盖给定子系统的模型内存段设置可能很有用。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecFuncExecute` |
| **值：** | `'Inherit from model'` (默认) | `'Default'` | 带引号的模型内存段 |

### **常量的内存段** — 如何应用内存段 `Inherit from model` (默认) | `Default` | model memory section

选择软件如何将内存段应用于子系统常量。

- `Inherit from model` — 将根模型内存段应用于子系统数据。
- `Default` — 不将内存段应用于子系统数据，覆盖任何模型级规范。
- 将某个模型内存段应用于子系统。

#### 提示

- 指定的内存段应用于生成代码中对应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值取决于为模型配置设置的 memory sections 包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 以及模型包包含的所有内存段。
- 这些选项对于覆盖给定子系统的模型内存段设置可能很有用。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function`，并选择 **带独立数据的函数** 参数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataConstants` |
| **值：** | `'Inherit from model'` (默认) | `'Default'` | 带引号的模型内存段 |

### **内部数据的内存段** — 如何应用内存段 `Inherit from model` (默认) | `Default` | model memory section

选择软件如何将内存段应用于子系统内部数据。

- `Inherit from model` — 将根模型内存段应用于子系统数据。
- `Default` — 不将内存段应用于子系统数据，覆盖任何模型级规范。
- 将某个模型内存段应用于子系统。

#### 提示

- 指定的内存段应用于生成代码中对应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值取决于为模型配置设置的 memory sections 包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 以及模型包包含的所有内存段。
- 这些选项对于覆盖给定子系统的模型内存段设置可能很有用。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function`，并选择 **带独立数据的函数** 参数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataInternal` |
| **值：** | `'Inherit from model'` (默认) | `'Default'` | 带引号的模型内存段 |

### **参数的内存段** — 如何应用内存段 `Inherit from model` (默认) | `Default` | model memory section

选择软件如何将内存段应用于子系统参数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，覆盖任何模型级规范。
- 将某个模型内存段应用于子系统。

#### 提示

- 指定的内存段应用于生成代码中对应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值取决于为模型配置设置的 memory sections 包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 以及模型包包含的所有内存段。
- 这些选项对于覆盖给定子系统的模型内存段设置可能很有用。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function`，并选择 **带独立数据的函数** 参数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataParameters` |
| **值：** | `'Inherit from model'` (默认) | `'Default'` | 带引号的模型内存段 |

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

如果有 Embedded Coder 许可证，可以生成 Halide 代码。有关详细信息，请参阅 Speed Up Generated Code Execution with Halide Code (Embedded Coder)。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `Module` (默认) | 为子系统以及子系统内的模块生成代码。 |
| `BlackBox` | 生成黑盒接口。生成的 HDL 代码仅包含子系统的输入/输出端口定义。因此，可以在模型中使用子系统来生成与现有手写 HDL 代码的接口。子系统的黑盒接口生成类似于 Model 模块接口生成，但不包含时钟信号。 |
| `No HDL` | 从生成的代码中移除子系统。可以在仿真中使用该子系统，但在 HDL 代码中将其视为“no-op”。 |

**黑盒接口自定义**

对于 `BlackBox` 架构，可以自定义端口名称并设置外部组件接口的属性。请参阅 Customize Black Box or HDL Cosimulation Interface (HDL Coder)。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **AdaptivePipelining** | 基于综合工具、目标频率和乘法器字长的自动流水线插入。默认值为 `inherit`。另请参阅 AdaptivePipelining (HDL Coder)。 |
| **ClockRatePipelining** | 以更快的时钟速率而不是较慢的数据速率插入流水线寄存器。默认值为 `inherit`。另请参阅 ClockRatePipelining (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出处放置的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分布或寄存器重定时。默认值为 `inherit`。另请参阅 DistributedPipelining (HDL Coder)。 |
| **DSPStyle** | 用于乘法器映射的综合属性。默认值为 `none`。另请参阅 DSPStyle (HDL Coder)。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中移除子系统层次。默认值为 `inherit`。另请参阅 FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的函数等效资源数。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |
| **StreamingFactor** | 时分复用为串行标量数据路径的并行数据路径（或向量）数。默认值为 0，表示实现完全并行的数据路径。另请参阅 Streaming (HDL Coder)。 |

如果此模块不是 DUT，则 **Target Specification** 选项卡中的模块属性设置将被忽略。在 HDL Workflow Advisor 中，如果使用 **IP Core Generation** 工作流，这些目标规范模块属性值会随模型保存。如果使用 `hdlset_param` 指定这些目标规范模块属性值，则打开 HDL Workflow Advisor 时，这些字段会填充为对应的值。

| 目标规范 | |
| --- | --- |
| **AdditionalTargetInterfaces** | 额外目标接口，指定为字符向量。要在模型上保存此模块属性，请在 **IP Core Generation** 工作流的 **Set Target Interface** 任务中，对于要添加更多接口的 DUT 端口，选择 **Add more...**。然后可以在 Add New Target Interfaces 对话框中添加更多接口。指定接口类型、额外接口数量以及每个额外接口的唯一名称。值：`''` (默认) | 字符向量元胞数组 示例：`'{{'AXI4-Stream','InterfaceID','AXI4-Stream1'}}'` |
| **ProcessorFPGASynchronization** | 处理器/FPGA 同步模式，指定为字符向量。要在模型上保存此模块属性，请在 **IP Core Generation** 工作流的 **Set Target Interface** 任务中指定 **Processor/FPGA Synchronization**。值：`Free running` (默认) | `Coprocessing - blocking` 示例：`'Free running'` |
| **TestPointMapping** | 要在模型上保存此模块属性，请在 **IP Core Generation** 工作流的 **Set Target Interface** 任务中指定测试点端口到目标平台接口的映射。值：`''` (默认) | 字符向量元胞数组 示例：`'{{'TestPoint','AXI4-Lite','x"108"'}}'` |
| **TunableParameterMapping** | 要在模型上保存此模块属性，请在 **IP Core Generation** 工作流的 **Set Target Interface** 任务中指定可调参数端口到目标平台接口的映射。值：`''` (默认) | 字符向量元胞数组 示例：`'{{'myParam','AXI4-Lite','x"108"'}}'` |
| **AXI4RegisterReadback** | 要在模型上保存此模块属性，请在 **IP Core Generation** 工作流的 **Generate RTL Code and IP Core** 任务中指定是否要在 AXI4 从属写寄存器上启用回读。要了解更多信息，请参阅 Model Design for AXI4 Slave Interface Generation (HDL Coder)。值：`'off'` (默认) | `'on'` |
| **AXI4SlaveIDWidth** | 要在模型上保存此模块属性，请在 **IP Core Generation** 工作流的 **Generate RTL Code and IP Core** 任务中使用 **AXI4 Slave ID Width** 设置，指定要将 DUT IP 核连接到的 AXI 管理器接口数量。要了解更多信息，请参阅 Define Multiple AXI Master Interfaces in Reference Designs to Access DUT AXI4 Slave Interface (HDL Coder)。值：`'off'` (默认) | `'on'` |
| **RegisterInterfaceReadPipeline** | 要在模型上保存此模块属性，请在 **IP Core Generation** 工作流的 **Generate RTL Code and IP Core** 任务中使用 **Register interface read pipeline** 设置，指定要插入读地址解码器路径的流水线级数。要了解更多信息，请参阅 Model Design for AXI4 Slave Interface Generation (HDL Coder)。值：`0` (默认) | 字符向量 |
| **GenerateDefaultAXI4Slave** | 要在模型上保存此模块属性，请在 **IP Core Generation** 工作流的 **Generate RTL Code and IP Core** 任务中指定是否要禁用默认 AXI4 从属接口的生成。值：`'on'` (默认) | `'off'` |
| **IPCoreAdditionalFiles** | 设计中黑盒的 Verilog®、SystemVerilog 或 VHDL® 文件。指定每个文件的完整路径，并用分号 (;) 分隔文件名。可以在 HDL Workflow Advisor 的 **Additional source files** 字段中设置此属性。值：`''` (默认) | 字符向量 示例：`'C:\myprojfiles\led_blinking_file1.vhd;C:\myprojfiles\led_blinking_file2.vhd;'` |
| **IPCoreName** | IP 核名称，指定为字符向量。可以在 HDL Workflow Advisor 的 **IP core name** 字段中设置此属性。如果此属性设置为默认值，HDL Workflow Advisor 会根据 DUT 的名称构造 IP 核名称。值：`''` (默认) | 字符向量 示例：`'my_model_name'` |
| **IPCoreVersion** | IP 核版本号，指定为字符向量。可以在 HDL Workflow Advisor 的 **IP core version** 字段中设置此属性。如果此属性设置为默认值，HDL Workflow Advisor 会设置 IP 核版本。值：`''` (默认) | 字符向量 示例：`'1.3'` |
| **IPDataCaptureBufferSize** | FPGA Data Capture 缓冲区大小，指定为字符向量。使用 FPGA Data Capture 在 FPGA 上运行时观察设计中的信号。缓冲区大小使用 128\*2^n 的值，其中 n 是整数。默认情况下，缓冲区大小为 128 (n=0)。n 的最大值为 13，这意味着缓冲区大小的最大值为 1048576 (=128\*2^13)。值：`''` (默认) | 字符向量 示例：`'1.3'` |

**限制**

如果 DUT 是掩码子系统，则仅当其位于模型顶层时才能生成代码。

有关详细信息，请参阅：

- External Component Interfaces (HDL Coder)
- Generate Black Box Interface for Subsystem (HDL Coder)

## 版本历史

**在 R2022b 中引入**

### R2025a：MATLAB Function 模块支持

可以在 Neighborhood Processing Subsystem 模块内使用 MATLAB Function 模块。

### R2025a：不支持具有状态的模块

Neighborhood Processing Subsystem 模块不能包含具有状态的模块。
