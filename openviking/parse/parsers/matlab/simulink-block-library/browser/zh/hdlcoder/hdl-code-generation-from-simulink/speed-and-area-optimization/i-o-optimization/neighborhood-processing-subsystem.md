---
type: simulink-block
title: 'Neighborhood Processing Subsystem'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Matrix Operations'
documentation_page: 'neighborhoodprocessingsubsystem'
documentation_source_path: 'slref/neighborhoodprocessingsubsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Neighborhood Processing Subsystem

## 端口

### 输入

### **In** — 子系统的信号输入 矩阵 | 向量

使用 Inport 模块从局部环境获取信号。

将 Inport 模块放置在 Neighborhood Processing Subsystem 模块中会向该子系统添加一个外部输入端口。端口标签与 Inport 模块的名称匹配。使用 Neighborhood control 模块配置要使用邻域模式处理哪些输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 输出

### **Out** — 子系统的信号输出 矩阵 | 向量

使用 Outport 模块向局部环境发送信号。

将 Outport 模块放置在 Neighborhood Processing Subsystem 模块中会从该子系统添加一个外部输出端口。端口标签与 Outport 模块的名称匹配。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### 主要

### **显示端口标签** — 端口标签的显示选项 `FromPortIcon`（默认） | `FromPortBlockName` | `SignalName` | `none`

选择如何在 Subsystem 模块图标上显示端口标签。

- `none` — 不显示端口标签。
- `FromPortIcon` — 如果对应端口图标显示信号名称，则在 Subsystem 模块上显示该信号名称。否则，显示端口模块名称；如果模块名称是默认名称，则显示端口号。
- `FromPortBlockName` — 在 Subsystem 模块上显示对应端口模块的名称。
- `SignalName` — 如果连接到端口的信号有名称，则在 Subsystem 模块上显示该信号名称。否则，显示对应端口模块的名称。

有关在 Subsystem 模块上编辑端口标签的信息，请参阅在 Subsystem 模块上编辑端口标签。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ShowPortLabels` |
| **值：** | `'FromPortIcon'`（默认） | `'FromPortBlockName'` | `'SignalName'` | `'none'` |

### **读/写权限** — 对子系统内容的访问级别 `ReadWrite`（默认） | `ReadOnly` | `NoReadOrWrite`

控制用户对子系统内容的访问。

- `ReadWrite` — 允许打开和修改子系统内容。
- `ReadOnly` — 允许打开但不能修改子系统。如果子系统位于模块库中，您可以创建并打开指向该子系统的链接，也可以创建和修改该子系统的本地副本，但不能更改权限或修改原始库实例的内容。
- `NoReadOrWrite` — 禁止打开或修改子系统。如果子系统位于库中，您可以在模型中创建指向该子系统的链接，但不能打开、修改、更改权限或创建该子系统的本地副本。

如果您尝试查看 **读/写权限** 参数设置为 `NoReadOrWrite` 的子系统内容，则不会收到任何响应。例如，当双击此类子系统时，软件不会打开该子系统，也不会显示任何消息。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Permissions` |
| **值：** | `'ReadWrite'`（默认） | `'ReadOnly'` | `'NoReadOrWrite'` |

### **错误回调函数名称** — 发生错误时要调用的函数名称 无默认值

输入当软件执行子系统期间发生错误时要调用的函数名称。

软件将两个参数传递给该函数：子系统的句柄以及指定错误类型的字符向量。如果未指定函数，则当执行子系统导致错误时，软件会显示一般错误消息。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ErrorFcn` |
| **值：** | `''`（默认） | 带引号的函数名称 |
| **数据类型：** | `char` | `string` |

### **允许分层解析** — 工作区变量名称的解析 `All`（默认） | `ExplicitOnly` | `None`

选择是否解析此子系统引用的工作区变量名称。

有关详细信息，请参阅符号解析和符号解析过程。

- `All` — 解析此子系统使用的所有工作区变量名称，包括用于指定模块参数值和 Simulink 数据对象（例如 `Simulink.Signal` 对象）的名称。
- `ExplicitOnly` — 仅解析用于指定模块参数值、数据存储内存（不存在对应模块时）、信号以及标记为“must resolve”的状态的工作区变量名称。
- `None` — 不解析任何工作区变量名称。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PermitHierarchicalResolution` |
| **值：** | `'All'`（默认） | `'ExplicitOnly'` | `'None'` |

### **显示子系统重新初始化端口** — 显示重新初始化事件端口的选项 `off`（默认） | `on`

选择此参数以显示重新初始化事件端口。清除此参数以移除这些端口。

#### 依赖关系

要启用此参数，请选择 **视为原子单元**。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ShowSubsystemReinitializePorts` |
| **值：** | `'off'`（默认） | `'on'` |

### 代码生成

代码生成选项卡上的参数需要 Simulink Coder™ 或 Embedded Coder® 许可证。

### **函数打包** — 代码格式 `Auto` | `Inline` | `Nonreusable function` | `Reusable function`

选择要为原子（非虚拟）子系统生成的代码格式。

- `Auto` — 软件根据模型中存在的子系统实例的类型和数量为您选择最佳格式。
- `Inline` — 软件无条件地内联该子系统。
- `Nonreusable function` — 如果 **文件名选项** 设置为 `Auto`，则软件在模型文件中打包单独的函数。如果 **文件名选项** 设置为 `Use subsystem name`、`Use function name` 或 `User specified` 并使用不同的文件名，则软件在单独的文件中打包单独的函数。

  使用此设置的子系统生成的函数可能包含参数，具体取决于函数接口参数设置。您可以分别使用函数名称和文件名（无扩展名）参数来命名生成的函数和文件。这些函数不可重入。
- `Reusable function` — 软件生成带参数的函数，当模型包含多个子系统实例时，允许重用子系统代码。

  此选项还会生成带参数的函数，允许在模型引用层级的生成代码中重用子系统代码，其中该层级跨被引用模型包含多个子系统实例。在这种情况下，子系统必须位于库中。

有关详细信息，请参阅：

- 为单个子系统生成代码和可执行文件 (Simulink Coder)
- 生成内联子系统代码 (Simulink Coder)
- 将子系统代码生成为单独的函数和文件 (Simulink Coder)
- 从跨模型共享的库子系统生成可重用代码 (Simulink Coder)

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Reusable function`。

#### 提示

- 当您希望将子系统的多个实例表示为一个可重用函数时，可以将其中每个实例指定为 `Auto` 或 `Reusable function`。最好只使用其中一种，因为同时使用两者会创建两个可重用函数，每个指定对应一个。这些选择的结果仅在无法重用时才不同。选择 `Auto` 不允许控制子系统代码的函数或文件名。
- `Reusable function` 和 `Auto` 选项都会尝试确定是否存在子系统的多个实例以及代码是否可以重用。每个选项行为之间的区别在于，当无法重用时：

  - `Auto` 会生成内联代码，或者如果情况禁止内联，则为每个子系统实例生成单独的函数。
  - `Reusable function` 会为模型中的每个子系统实例生成带参数的单独函数。
- 如果生成的代码处于源代码管理下，而您选择了 `Reusable function`，请将 **文件名选项** 设置为 `Use subsystem name`、`Use function name` 或 `User specified`。否则，每次修改模型时，代码文件的名称都会更改，从而妨碍对文件进行源代码管理。
- 如果您选择 `Auto` 或 `Inline` 以外的选项以及模型配置参数 **状态**，代码生成器会生成单独的输出和更新方法。代码生成器不会考虑 **为代码生成和仿真合并输出与更新方法** 规范。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证才能进行代码生成。
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

- `Auto` — 使用默认命名约定 `model_subsystem()` 分配唯一的函数名称，其中 *`model`* 是模型的名称，*`subsystem`* 是子系统的名称；当重用代码时，是相同子系统的名称。

  如果您为 **函数打包** 参数选择 `Reusable function`，并且模型引用层级包含可重用子系统的多个实例，则为了为该子系统生成可重用代码，**函数名称选项** 必须设置为 `Auto`。
- `Use subsystem name` — 使用子系统名称作为函数名称。默认情况下，函数名称使用命名约定 `model_subsystem`。

  当子系统位于库模块中，并且子系统参数函数打包设置为 `Reusable function` 时，如果您设置 `Use subsystem name` 选项，代码生成器会使用库模块的名称作为子系统函数名称和文件名。
- `User specified` — 启用 **函数名称** 字段。输入任何合法的 C 或 C++ 函数名称，该名称必须唯一。

有关详细信息，请参阅将子系统代码生成为单独的函数和文件 (Simulink Coder)。

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Use subsystem name`。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFcnNameOpts` |
| **值：** | `'Auto'` | `'Use subsystem name'` | `'User specified'` |

### **函数名称** — 子系统代码的函数名称 无默认值

为子系统代码指定唯一、有效的 C 或 C++ 函数名称。

如果您希望为函数指定特定名称，而不是允许 Simulink Coder 代码生成器分配其自己的自动生成名称或使用子系统名称，请使用此参数。有关详细信息，请参阅将子系统代码生成为单独的函数和文件 (Simulink Coder)。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **函数名称选项** 设置为 `User specified`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFcnName` |
| **值：** | `''`（默认） | 带引号的函数名称 |
| **数据类型：** | `char` | `string` |

### **文件名选项** — 如何命名生成的文件 `Auto` | `Use subsystem name` | `Use function name` | `User specified`

选择软件为子系统生成的函数命名单独文件的方式。

- `Auto` — 根据子系统的配置以及模型中的实例数量，`Auto` 会产生不同的结果。

  - 如果代码生成器*不*为子系统生成单独的文件，则子系统代码会在从子系统父系统生成的代码模块中生成。如果子系统的父系统是模型本身，则子系统代码会在 `model.c` 或 `model.cpp` 中生成。
  - 如果您为 **函数打包** 参数选择 `Reusable function`，并且生成的代码处于源代码管理下，请考虑指定一个不是 `Auto` 的 **文件名选项** 值。这可以防止生成的文件名因不相关的模型修改而更改，而使用源代码管理来管理配置时这会造成问题。
  - 如果您为 **函数打包** 参数选择 `Reusable function`，并且模型引用层级包含可重用子系统的多个实例，则为了为该子系统生成可重用代码，**文件名选项** 必须设置为 `Auto`。
- `Use subsystem name` — 代码生成器生成单独的文件，使用子系统（或库模块）名称作为文件名。

  当 **文件名选项** 设置为 `Use subsystem name` 时，如果模型包含 Model 模块，或者正在为该模型生成模型引用目标，则子系统文件名会进行名称改编。在这些情况下，子系统文件名由模型名称作为前缀加上子系统名称组成。
- `Use function name` — 代码生成器使用由 **函数名称选项** 指定的函数名称作为文件名。
- `User specified` — 此选项启用 **文件名（无扩展名）** 文本输入字段。代码生成器使用您输入的名称作为文件名。输入任何文件名，但不要包含 `.c` 或 `.cpp`（或任何其他）扩展名。此文件名不必唯一。

  虽然子系统源文件名不必唯一，但必须避免使用会导致循环依赖的非唯一名称。例如，`sys_a.h` 包含 `sys_b.h`，`sys_b.h` 包含 `sys_c.h`，而 `sys_c.h` 包含 `sys_a.h`。

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Use function name`。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFileNameOpts` |
| **值：** | `'Auto'` | `'Use subsystem name'` | `'Use function name'` | `'User specified'` |

### **文件名（无扩展名）** — 生成文件的名称，无默认值

您指定的文件名不必唯一。但是，请避免使用会导致循环依赖的非唯一名称。例如，`sys_a.h` 包含 `sys_b.h`，`sys_b.h` 包含 `sys_c.h`，而 `sys_c.h` 包含 `sys_a.h`。

有关详细信息，请参阅将子系统代码生成为单独的函数和文件 (Simulink Coder)。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **文件名选项** 设置为 `User specified`。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFileName` |
| **值：** | `''`（默认） | 引号中的文件名 |
| **数据类型：** | `char` | `string` |

### **函数接口** — 如何将参数与生成的函数一起使用 `void_void`（默认） | `Allow arguments (Optimized)` | `Allow arguments (Match graphical interface)`

选择如何将参数与生成的函数一起使用。

- `void_void` — 生成不带参数的函数，并将数据作为全局变量传递。例如：

  ```
  void subsystem_function(void)
  ```
- `Allow arguments (Optimized)` — 生成使用参数而不是将数据作为全局变量传递的函数。此规范减少全局 RAM。此选项可能减小代码大小并提高执行速度，并使代码生成器能够应用其他优化。例如：

  ```
  void subsystem_function(real_T rtu_In1, real_T rtu_In2,
                          real_T *rty_Out1)
  ```

  在某些情况下，生成优化代码时，代码生成器可能不会生成带参数的函数。
- `Allow arguments (Match graphical interface)` — 生成一个函数接口，该接口使用与 Subsystem 图形模块接口匹配的参数。生成的函数接口是可预测的，并且不会改变。可预测的接口可用于调试和测试代码以及与外部应用程序集成。例如，如果模型有两个 Inport 模块和两个 Outport 模块，则生成的函数接口为：

  ```
  void subsystem_function(real_T rtu_In1, real_T rtu_In2,
                          real_T *rty_Out1, real_T *rty_Out2)
  ```

有关详细信息，请参阅：

- 减少不可重用子系统函数中的全局变量 (Embedded Coder)
- 生成可预测的函数接口以匹配图形模块接口 (Embedded Coder)
- 为非虚拟子系统生成模块化函数代码 (Embedded Coder)

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function`。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FunctionInterfaceSpec` |
| **值：** | `'void_void'`（默认） | `'Allow arguments (Optimized)'` | `'Allow arguments (Match graphical interface)'` |

### **具有单独数据的函数** — 控制子系统的代码生成 `off`（默认） | `on`

生成子系统函数代码，其中原子子系统的内部数据与其父模型分离，并由该子系统拥有。

- `off` — 不生成子系统函数代码，其中原子子系统的内部数据与其父模型分离并由该子系统拥有。
- `on` — 生成子系统函数代码，其中原子子系统的内部数据与其父模型分离并由该子系统拥有。子系统数据结构独立于父模型数据结构声明。具有单独数据的子系统拥有自己的模块 I/O 和 `DWork` 数据结构。因此，该子系统生成的代码更易于跟踪和测试。数据分离还倾向于减小整个模型中全局数据结构的最大大小，因为它们被拆分为多个数据结构。

有关如何为原子子系统生成模块化函数代码的详细信息，请参阅为非虚拟子系统生成模块化函数代码 (Embedded Coder)。

有关如何将内存段应用于原子子系统的详细信息，请参阅覆盖子系统函数和数据的默认内存放置 (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function`。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FunctionWithSeparateData` |
| **值：** | `'off'`（默认） | `'on'` |

### **初始化/终止函数的内存段** — 如何应用内存段 `Inherit from model`（默认） | `Default` | 模型内存段

选择软件如何将内存段应用于子系统初始化和终止函数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，并覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 可能的值取决于您为模型配置设置的内存段包（如果有）。请参阅通过插入 Pragmas 控制数据和函数在内存中的放置 (Embedded Coder) 和模型配置参数：代码生成 (Simulink Coder)。
- 如果尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅覆盖子系统函数和数据的默认内存放置 (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecFuncInitTerm` |
| **值：** | `'Inherit from model'`（默认） | `'Default'` | 引号中的模型内存段 |

### **执行函数的内存段** — 如何应用内存段 `Inherit from model`（默认） | `Default` | 模型内存段

选择 Embedded Coder 如何将内存段应用于子系统执行函数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，并覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 可能的值取决于您为模型配置设置的内存段包（如果有）。请参阅通过插入 Pragmas 控制数据和函数在内存中的放置 (Embedded Coder) 和模型配置参数：代码生成 (Simulink Coder)。
- 如果尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅覆盖子系统函数和数据的默认内存放置 (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecFuncExecute` |
| **值：** | `'Inherit from model'`（默认） | `'Default'` | 引号中的模型内存段 |

### **常量的内存段** — 如何应用内存段 `Inherit from model`（默认） | `Default` | 模型内存段

选择软件如何将内存段应用于子系统常量。

- `Inherit from model` — 将根模型内存段应用于子系统数据。
- `Default` — 不将内存段应用于子系统数据，并覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 您指定的内存段应用于生成代码中相应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅标准数据结构 (Simulink Coder)。
- 可能的值取决于您为模型配置设置的内存段包（如果有）。请参阅通过插入 Pragmas 控制数据和函数在内存中的放置 (Embedded Coder)。
- 如果尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅覆盖子系统函数和数据的默认内存放置 (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function`，并选择 **具有单独数据的函数** 参数。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataConstants` |
| **值：** | `'Inherit from model'`（默认） | `'Default'` | 引号中的模型内存段 |

### **内部数据的内存段** — 如何应用内存段 `Inherit from model`（默认） | `Default` | 模型内存段

选择软件如何将内存段应用于子系统内部数据。

- `Inherit from model` — 将根模型内存段应用于子系统数据。
- `Default` — 不将内存段应用于子系统数据，并覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 您指定的内存段应用于生成代码中相应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅标准数据结构 (Simulink Coder)。
- 可能的值取决于您为模型配置设置的内存段包（如果有）。请参阅通过插入 Pragmas 控制数据和函数在内存中的放置 (Embedded Coder)。
- 如果尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅覆盖子系统函数和数据的默认内存放置 (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function`，并选择 **具有单独数据的函数** 参数。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataInternal` |
| **值：** | `'Inherit from model'`（默认） | `'Default'` | 引号中的模型内存段 |

### **参数的内存段** — 如何应用内存段 `Inherit from model`（默认） | `Default` | 模型内存段

选择软件如何将内存段应用于子系统参数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，并覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 您指定的内存段应用于生成代码中相应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅标准数据结构 (Simulink Coder)。
- 可能的值取决于您为模型配置设置的内存段包（如果有）。请参阅通过插入 Pragmas 控制数据和函数在内存中的放置 (Embedded Coder)。
- 如果尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅覆盖子系统函数和数据的默认内存放置 (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **函数打包** 设置为 `Nonreusable function`，并选择 **具有单独数据的函数** 参数。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataParameters` |
| **值：** | `'Inherit from model'`（默认） | `'Default'` | 引号中的模型内存段 |

## 所属库

Simulink / Matrix Operations

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

如果拥有 Embedded Coder 许可证，您可以生成 Halide 代码。有关详细信息，请参阅使用 Halide 代码加速生成的代码执行 (Embedded Coder)。

### HDL Code Generation
使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供额外配置选项，这些选项会影响 HDL 实现和综合逻辑。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `Module`（默认） | 为子系统及该子系统内的模块生成代码。 |
| `BlackBox` | 生成黑盒接口。生成的 HDL 代码仅包含该子系统的输入/输出端口定义。因此，你可以在模型中使用子系统，为现有手动编写的 HDL 代码生成接口。针对子系统的黑盒接口生成类似于 Model block 接口生成，但不包含时钟信号。 |
| `No HDL` | 从生成代码中移除该子系统。你可以在仿真中使用该子系统，但在 HDL 代码中将其视为“no-op”。 |

**黑盒接口自定义**

对于 `BlackBox` 架构，你可以自定义端口名称并设置外部组件接口的属性。参见 Customize Black Box or HDL Cosimulation Interface (HDL Coder)。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **AdaptivePipelining** | 基于综合工具、目标频率和乘法器字长自动插入流水线。默认值为 `inherit`。另请参阅 AdaptivePipelining (HDL Coder)。 |
| **ClockRatePipelining** | 以更快的时钟速率而不是较慢的数据速率插入流水线寄存器。默认值为 `inherit`。另请参阅 ClockRatePipelining (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参见 ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分布，或寄存器重定时。默认值为 `inherit`。另请参阅 DistributedPipelining (HDL Coder)。 |
| **DSPStyle** | 用于乘法器映射的综合属性。默认值为 `none`。另请参阅 DSPStyle (HDL Coder)。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中移除子系统层级。默认值为 `inherit`。另请参阅 FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参见 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参见 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的功能等效资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |
| **StreamingFactor** | 要通过时分复用以转换为串行、scalar 数据路径的并行数据路径或向量数量。默认值为 0，表示实现完全并行的数据路径。另请参阅 Streaming (HDL Coder)。 |

如果此模块不是 DUT，则忽略 **Target Specification** 选项卡中的模块属性设置。在 HDL Workflow Advisor 中，如果你使用 **IP Core Generation** 工作流，这些目标规范模块属性值会随模型保存。如果你使用 `hdlset_param` 指定这些目标规范模块属性值，则打开 HDL Workflow Advisor 时，这些字段会填充为相应值。

| Target Specification | |
| --- | --- |
| **AdditionalTargetInterfaces** | 额外目标接口，指定为 character vector。 要将此模块属性保存到模型上，请在 **IP Core Generation** 工作流的 **Set Target Interface** 任务中，对于要向其添加更多接口的 DUT 端口，选择 **Add more...**。然后你可以在 Add New Target Interfaces 对话框中添加更多接口。指定接口类型、额外接口数量以及每个额外接口的唯一名称。 值：`''`（默认） \| cell array of character vectors 示例：`'{{'AXI4-Stream','InterfaceID','AXI4-Stream1'}}'` |
| **ProcessorFPGASynchronization** | 处理器/FPGA 同步模式，指定为 character vector。 要将此模块属性保存到模型上，请在 **IP Core Generation** 工作流的 **Set Target Interface** 任务中指定 **Processor/FPGA Synchronization**。 值：`Free running`（默认） \| `Coprocessing - blocking` 示例：`'Free running'` |
| **TestPointMapping** | 要将此模块属性保存到模型上，请在 **IP Core Generation** 工作流的 **Set Target Interface** 任务中指定测试点端口到目标平台接口的映射。 值：`''`（默认） \| cell array of character vectors 示例：`'{{'TestPoint','AXI4-Lite','x"108"'}}'` |
| **TunableParameterMapping** | 要将此模块属性保存到模型上，请在 **IP Core Generation** 工作流的 **Set Target Interface** 任务中指定可调参数端口到目标平台接口的映射。 值：`''`（默认） \| cell array of character vectors 示例：`'{{'myParam','AXI4-Lite','x"108"'}}'` |
| **AXI4RegisterReadback** | 要将此模块属性保存到模型上，请在 **IP Core Generation** 工作流的 **Generate RTL Code and IP Core** 任务中指定是否要在 AXI4 从属写寄存器上启用回读。要了解更多信息，请参见 Model Design for AXI4 Slave Interface Generation (HDL Coder)。 值：`'off'`（默认） \| `'on'` |
| **AXI4SlaveIDWidth** | 要将此模块属性保存到模型上，请使用 **IP Core Generation** 工作流的 **Generate RTL Code and IP Core** 任务中的 **AXI4 Slave ID Width** 设置，指定你希望将 DUT IP core 连接到的 AXI manager 接口数量。要了解更多信息，请参见 Define Multiple AXI Master Interfaces in Reference Designs to Access DUT AXI4 Slave Interface (HDL Coder)。 值：`'off'`（默认） \| `'on'` |
| **RegisterInterfaceReadPipeline** | 要将此模块属性保存到模型上，请使用 **IP Core Generation** 工作流的 **Generate RTL Code and IP Core** 任务中的 **Register interface read pipeline** 设置，指定要插入到读地址解码器路径中的流水线级数。要了解更多信息，请参见 Model Design for AXI4 Slave Interface Generation (HDL Coder)。 值：`0`（默认） \| character vector |
| **GenerateDefaultAXI4Slave** | 要将此模块属性保存到模型上，请在 **IP Core Generation** 工作流的 **Generate RTL Code and IP Core** 任务中指定是否要禁用默认 AXI4 从属接口的生成。 值：`'on'`（默认） \| `'off'` |
| **IPCoreAdditionalFiles** | 用于设计中黑盒的 Verilog®、SystemVerilog 或 VHDL® 文件。指定每个文件的完整路径，并用分号 (;) 分隔文件名。 你可以在 HDL Workflow Advisor 的 **Additional source files** 字段中设置此属性。 值：`''`（默认） \| character vector 示例：`'C:\myprojfiles\led_blinking_file1.vhd;C:\myprojfiles\led_blinking_file2.vhd;'` |
| **IPCoreName** | IP core 名称，指定为 character vector。 你可以在 HDL Workflow Advisor 的 **IP core name** 字段中设置此属性。如果此属性设置为默认值，HDL Workflow Advisor 会根据 DUT 的名称构造 IP core 名称。 值：`''`（默认） \| character vector 示例：`'my_model_name'` |
| **IPCoreVersion** | IP core 版本号，指定为 character vector。 你可以在 HDL Workflow Advisor 的 **IP core version** 字段中设置此属性。如果此属性设置为默认值，HDL Workflow Advisor 会设置 IP core 版本。 值：`''`（默认） \| character vector 示例：`'1.3'` |
| **IPDataCaptureBufferSize** | FPGA Data Capture 缓冲区大小，指定为 character vector。使用 FPGA Data Capture 在 FPGA 上运行时观察设计中的信号。 缓冲区大小使用 128\*2^n 的值，其中 n 是整数。默认情况下，缓冲区大小为 128 (n=0)。n 的最大值为 13，这意味着缓冲区大小的最大值为 1048576 (=128\*2^13)。 值：`''`（默认） \| character vector 示例：`'1.3'` |

**限制**

如果你的 DUT 是掩码子系统，则仅当它位于模型的顶层时才能生成代码。

有关更多信息，请参见：

- External Component Interfaces (HDL Coder)
- Generate Black Box Interface for Subsystem (HDL Coder)

## 版本历史

**在 R2022b 中引入**

### R2025a: MATLAB Function block 支持

你可以在 Neighborhood Processing Subsystem block 内使用 MATLAB Function blocks。

### R2025a: 不支持具有状态的模块

Neighborhood Processing Subsystem block 不能包含具有状态的模块。

## 描述

创建遵循邻域模式的算法

Neighborhood Processing Subsystem block 是一个预配置的 Subsystem block，作为创建遵循邻域模式的子系统的起点。在每个仿真时间步，该子系统遍历输入数组的每个元素。对于每个元素，该子系统处理该元素周围的值邻域。使用该子系统进行图像处理。某些图像处理算法涉及分段处理图像，而不是一次处理整个图像。

### 配置 Subsystem

Neighborhood Processing Subsystem 包含一个 Neighborhood block，它充当该子系统的控制模块。指定 Neighborhood block 的参数以配置该子系统的行为。

**Neighborhood size** 参数控制邻域的维度。对于输入矩阵边缘附近的元素，邻域可能扩展到输入矩阵之外。**Padding option** 参数控制该子系统如何处理来自输入矩阵外部的值。你可以配置该子系统用常量填充这些值，或通过重用矩阵内部的值来填充这些值。如果使用 `Constant` 填充选项，请使用 **Padding constant** 参数设置常量值。

你可以配置 Neighborhood Processing Subsystem block 仅处理输入矩阵的某些元素。使用 **Stride** 参数配置 Neighborhood Processing Subsystem block 在每次迭代时跳过一定数量的元素。使用 **Processing offset** 和 **Processing width** 参数分别定义图像内感兴趣区域 (ROI) 的左上边界和右下边界。Neighborhood Processing Subsystem block 仅迭代该区域。

**Output size** 参数控制输出矩阵的大小。`Same` 值将输出矩阵配置为与 ROI 大小相同。`Full` 值通过为 ROI 外部但其邻域至少包含一个来自 ROI 的元素的元素计算值，生成更大的输出矩阵。`Valid` 值通过仅为邻域不扩展到 ROI 之外的元素计算值，生成更小的输出矩阵。使用此设置时，**Padding constant** 参数被禁用。

### 示例

考虑此模型。

一个包含 Constant block 的模型，其值为 "ones(5,5)"，该值通过 Neighborhood Processing Subsystem 传递，并输出到 Display block。Display block 不显示任何值。

在此示例中，Neighborhood Processing Subsystem block 接收一个 5-by-5 矩阵，并通过使用 `Same` 输出大小选项输出一个相同维度的矩阵。该子系统包含以下模块。

一个带有一个输入端口和一个输出端口的 Neighborhood Processing Subsystem。该输入端口连接到 Sum of Elements block，该 block 输出到输出端口。

在 Neighborhood Processing Subsystem block 内部，输入端口不会接收完整的 5-by-5 矩阵。相反，由于 **Neighborhood size** 参数值为 `[3 3]`，输入端口接收一个更小的 3-by-3 元素窗口。该子系统遍历输入矩阵的元素，并在每次迭代时将每个元素的邻域传递到输入端口。

该模型使用 `Constant` 填充选项，填充值为 `0`。对于扩展到输入矩阵之外的邻域，该子系统将外部值视为 `0`。

Neighborhood Processing Subsystem block 的输出端口接收一个 scalar，它表示窗口中心元素的派生值。在此情况下，一个 Sum of Elements block 将 **Sum over** 参数设置为 `All dimensions`，会为每个窗口生成一个 scalar，表示该窗口中值的和。

运行模型以填充 Display block。

与之前相同的模型，其中 Display block 填充了一个 5-by-5 矩阵。内部的 9 个元素的值为 9，角元素的值为 4，非角边缘元素的值为 6。

输出矩阵的每个值都是输入矩阵中对应元素及其八个直接相邻元素之和。内部元素周围的值均为 `1`，因此其值为 `9`。外部元素的值较低，因为所选填充方法对输入矩阵之外的元素使用值 `0`。
