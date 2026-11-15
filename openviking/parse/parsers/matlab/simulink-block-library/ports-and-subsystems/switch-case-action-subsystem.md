---
type: simulink-block
title: 'Switch Case Action Subsystem'
family: ports-and-subsystems
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'switchcaseactionsubsystem'
---

# Switch Case Action Subsystem

Subsystem whose execution is enabled by Switch Case block

## 中文

由 Switch Case 模块使能执行的子系统

### 所属库

Simulink / Ports & Subsystems

### 描述

Switch Case Action Subsystem 模块是经过预先配置的 Subsystem 模块，您可基于它创建由 Switch Case 模块控制执行的子系统。Switch Case 模块的输入端口选择使用 **case 条件**参数定义的 case。根据输入值和选择的 case，该模块发送动作信号，以执行 Switch Case Action Subsystem 模块。子系统的执行由放置在子系统内部的 Action Port 模块控制。

Simulink® 会忽略对 Switch Case Action Subsystem 模块设置的优先级。在这种情况下，请对启动子系统执行的 Switch Case 模块设置优先级。

Switch Case Action Subsystem 模块中的所有模块都必须以与 Switch Case 驱动模块相同的速率运行。可以通过将每个模块采样时间参数都设置为继承 (`-1`) 或与 Switch Case 模块相同的采样时间来实现此要求。

#### 合并来自 Switch Case 执行子系统模块的信号

示例模型 `ex_switch_case_block` 显示如何基于多个子系统输出信号创建一个信号。有关详细信息，请参阅选择子系统执行。

Model ex\_switch\_case\_block

Switch Case 模块从一组子系统中选择一个 If Action Subsystem 模块执行。无论 Switch Case 模块选择哪个子系统，您都可以用 Merge 模块创建一个结果信号。

### 端口

#### 输入

#### **In1** — 子系统的信号输入 标量 | 向量 | 矩阵

在子系统中放置一个 Inport 模块会向 Subsystem 模块添加一个外部输入端口。端口标签与 Inport 模块的名称相匹配。

使用 Inport 模块可以从局部环境中获取信号。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

#### **Action** — 控制子系统的信号输入 标量 | 向量 | 矩阵

子系统内的 Action Port 模块会向 Subsystem 模块添加一个外部输入端口并将该模块更改为 Switch Case Action Subsystem 模块。

**注意**

Action Port 模块在 Simulink 库浏览器中不可用。使用 Switch Case Action Subsystem 模块时，您只能从 Switch Case Action Subsystem 模块中访问 Action Port 模块。

从 Switch Case 模块到 Switch Case Action Subsystem 模块的点划线表示*动作*信号。动作信号是连接到 Switch Case Action Subsystem 模块的 **Action** 端口的控制信号。动作信号上的消息启动子系统的执行。

**数据类型:** `action`
#### 输出

#### **Out1** — 子系统的信号输出 标量 | 向量 | 矩阵

在子系统中放置一个 Outport 模块会从 Subsystem 模块添加一个输出端口。子系统模块上的端口标签是 Outport 模块的名称。

使用 Outport  模块可以向局部环境发送信号。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条中，在**仿真**选项卡的**准备**库中，选择**属性检查器**。

#### 常设

#### **显示端口标签** — 端口标签的显示选项 **FromPortIcon** (默认) | **FromPortBlockName** | **SignalName** | **无**

选择如何在 Subsystem 模块图标上显示端口标签。

- **无** - 不显示端口标签。
- **FromPortIcon** - 如果对应的端口图标显示了信号名称，则在 Subsystem 模块上显示信号名称。否则，如果模块名称是默认名称，则显示端口模块名称或端口号。
- **FromPortBlockName** - 在 Subsystem 模块上显示对应端口模块的名称。
- **SignalName** - 如果连接到端口的信号已命名，则会在 Subsystem 模块上显示信号的名称。否则，显示相应端口模块的名称。

有关 Subsystem 模块上的端口标签编辑，请参阅编辑子系统模块上的端口标签。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ShowPortLabels` |
| **值:** | `'FromPortIcon'` (默认) | `'FromPortBlockName'` | `'SignalName'` | `'none'` |

#### **读取/写入权限** — 子系统内容的访问级别 **ReadWrite** (默认) | **ReadOnly** | **NoReadOrWrite**

控制用户对子系统内容的访问。

- **ReadWrite** - 允许打开和修改子系统内容。
- **ReadOnly** - 允许打开但不允许修改子系统。如果子系统在模块库中，您可以创建和打开该子系统的链接，创建和修改子系统的本地副本，但不能更改权限或修改原始模块库实例的内容。
- **NoReadOrWrite** - 禁止打开或修改子系统。如果子系统在模块库中，您可以在模型中创建该子系统的链接，但不能打开、修改、更改权限或创建子系统的本地副本。

如果您尝试查看其**读取/写入权限**参数设置为 **NoReadOrWrite** 的子系统的内容，将不会收到响应。例如，当您双击此类子系统时，软件不会打开该子系统，并且不显示任何消息。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Permissions` |
| **值:** | `'ReadWrite'` (默认) | `'ReadOnly'` | `'NoReadOrWrite'` |

#### **错误回调函数的名称** — 发生错误时要调用的函数的名称 无默认值

输入软件执行子系统时，如果发生错误要调用的函数的名称。

该软件向函数传递两个参量：子系统的句柄以及指定错误类型的字符向量。如果未指定任何函数，当执行子系统导致错误时，软件将显示常规错误消息。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ErrorFcn` |
| **值:** | `''` (默认) | function name in quotes |
| **数据类型:** | `char` | `string` |

#### **允许层次解析** — 工作区变量名称解析 **全部** (默认) | **ExplicitOnly** | **无**

选择是否解析此子系统引用的工作区变量的名称。

有关详细信息，请参阅符号解析和符号解析过程。

- **全部** - 解析此子系统使用的所有工作区变量的名称，包括用来指定模块参数值和 Simulink 数据对象（例如，`Simulink.Signal` 对象）的工作区变量的名称。
- **ExplicitOnly** - 只解析用来指定模块参数值、数据存储内存（不存在模块）、信号以及标有“must resolve”状态的工作区变量的名称。
- **无** - 不解析任何工作区变量名称。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `PermitHierarchicalResolution` |
| **值:** | `'All'` (默认) | `'ExplicitOnly'` | `'None'` |

#### **显示子系统重新初始化端口** — 显示重新初始化事件端口的选项 `off` (默认) | `on`

选中此参数可显示重新初始化事件端口。清除此参数可删除这些端口。

##### 依赖关系

要启用此参数，请选择**视为原子单元**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ShowSubsystemReinitializePorts` |
| **值:** | `'off'` (默认) | `'on'` |

#### 代码生成

设置“代码生成”选项卡上的参数需要具有 Simulink Coder™ 或 Embedded Coder® 许可证。

#### **函数打包** — 代码格式 **自动** | **内联** | **不可重用函数** | **可重用函数**

选择要为原子（非虚拟）子系统生成的代码格式。

- **自动** - 软件将根据模型中存在的子系统的类型和实例数为您选择最佳格式。
- **内联** - 软件无条件内联子系统。
- **不可重用函数** - 如果将**文件名选项**设置为**自动**，则软件会将单独函数打包到模型文件中。如果使用不同的文件名将**文件名选项**设置为**使用子系统名称**、**使用函数名称**或**用户指定**，则软件将单独函数分别打包到独立的文件中。

  采用此设置的子系统生成的函数可能有参量，具体取决于 函数接口 参数设置。您可以使用参数 函数名称 和 文件名(无扩展名) 分别为生成的函数和文件命名。这些函数不可重入。
- **可重用函数** - 当模型中包含子系统的多个实例时，软件可以生成带参量的函数，该函数将允许重用子系统的代码。

  此选项还可生成带参量的函数，允许在为模型引用层次结构（其中引用的模型包含子系统的多个实例）生成的代码中重用子系统代码。在这种情况下，子系统必须是模块库中的子系统。

有关详细信息，请参阅：

- Generate Code and Executables for Individual Subsystems (Simulink Coder)
- Generate Inlined Subsystem Code (Simulink Coder)
- 将子系统代码生成为单独的函数和文件 (Simulink Coder)
- Generate Reusable Code from Library Subsystems Shared Across Models (Simulink Coder)

默认值取决于模块配置。例如，Subsystem 模块的默认值为**自动**。CodeReuseSubsystem 模块的默认值为**可重用函数**。

##### 提示

- 如果您希望子系统的多个实例表示为一个可重用函数，可以为每个子系统指定**自动**或**可重用函数**。最好是使用其中一个，因为使用两个将生成两个可重用函数，每个指定一个函数。仅当可以重用时，这些选项的结果才会有区别。选择**自动**则不允许控制子系统代码的函数或文件名。
- **可重用函数**和**自动**选项都尝试确定是否存在子系统的多个实例，以及是否可以重用代码。者两个选项的行为区别体现在不能重用时：

  - **自动**生成内联代码，或者在禁止内联的情况下为每个子系统实例生成一个单独的函数。
  - **可重用函数**为模型中的每个子系统实例生成一个单独的参量函数。
- 如果您在生成的代码处于源代码管理状态下时选择了**可重用函数**，请将**文件名选项**设置为**使用子系统名称**、**使用函数名称**或**用户指定**。否则，只要您修改模型，代码文件的名称就会改变，从而无法对文件进行源代码管理。
- 如果您选择除**自动**或**内联**以外的选项，并且使用模型配置参数**状态**，则代码生成器会生成单独的输出和更新方法。代码生成器不考虑**为代码生成和仿真合并输出和更新方法**设定。

##### 依赖关系

- 此参数需要 Simulink Coder 许可证才能生成代码。
- 要启用此参数，请选择**视为原子单元**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RTWSystemCode` |
| **值:** | `'Auto'` | `'Inline'` | `'Nonreusable function'` | `'Reusable function'` |

#### **函数名称选项** — 如何命名生成的函数 **自动** | **使用子系统名称** | **用户指定**

选择软件如何命名它为子系统生成的函数。

如果您拥有 Embedded Coder 许可证，则可以使用“配置参数”对话框的**代码生成** > **标识符**窗格上的选项来控制函数名称。

- **自动** - 使用默认的命名约定 `model_subsystem()` 指定唯一的函数名称，其中 *`model`* 是模型的名称，*`subsystem`* 是子系统的名称，或者，在重用代码时，也可以是相同子系统的名称。

  如果您为**函数打包**参数选择了**可重用函数**，而模型引用层次结构中存在可重用子系统的多个实例，则要为子系统生成可重用代码，必须将**函数名称选项**设置为**自动**。
- **使用子系统名称** - 使用子系统名称作为函数名称。默认情况下，函数名称使用命名约定 `model_subsystem`。

  当子系统在模块库模块中而子系统参数 函数打包 设置为**可重用函数**时，如果您设置**使用子系统名称**选项，代码生成器将使用模块库模块的名称作为子系统函数名和文件名。
- **用户指定** - 启用**函数名称**字段。输入任何合法的 C 或 C++ 函数名，此名称必须唯一。

有关详细信息，请参阅将子系统代码生成为单独的函数和文件 (Simulink Coder)。

默认值取决于模块配置。例如，Subsystem 模块的默认值为**自动**。CodeReuseSubsystem 模块的默认值为**使用子系统名称**。

##### 依赖关系

- 此参数要求具有 Simulink Coder 许可证。
- 要启用此参数，请将**函数打包**设置为**不可重用函数**或**可重用函数**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RTWFcnNameOpts` |
| **值:** | `'Auto'` | `'Use subsystem name'` | `'User specified'` |

#### **函数名称** — 子系统代码的函数名称 无默认值

为子系统代码指定唯一的有效 C 或 C++ 函数名称。

如果您想为函数指定特定的名称，而不是让 Simulink Coder 代码生成器分配其自己自动生成的名称或者使用子系统名称，请使用此参数。有关详细信息，请参阅将子系统代码生成为单独的函数和文件 (Simulink Coder)。

##### 依赖关系

- 此参数要求具有 Simulink Coder 许可证。
- 要启用此参数，请将**函数名称选项**设置为**用户指定**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RTWFcnName` |
| **值:** | `''` (默认) | function name in quotes |
| **数据类型:** | `char` | `string` |

#### **文件名选项** — 如何命名生成的文件 **自动** | **使用子系统名称** | **使用函数名称** | **用户指定**

选择软件如何命名它为子系统生成的函数的单独文件。

- **自动** - 根据子系统的配置以及子系统在模型中的实例数，**自动**将生成不同的结果。

  - 如果代码生成器*不*为子系统生成单独的文件，将在从子系统的父级系统生成的代码模块内生成子系统代码。如果子系统的父级就是模型本身，将在 `model.c` 或 `model.cpp` 内生成子系统代码。
  - 如果您为**函数打包**参数选择了**可重用函数**，而您生成的代码处于源代码管理状态下，请不要将**文件名选项**值指定为**自动**。这样可以防止由于不相关的模型修改而更改生成的文件名，而在使用源代码管理来管理配置时，文件名的改变会产生问题。
  - 如果您为**函数打包**参数选择了**可重用函数**，而模型引用层次结构中存在可重用子系统的多个实例，则要为子系统生成可重用代码，必须将**文件名选项**设置为**自动**。
- **使用子系统名称** - 代码生成器将生成一个单独的文件，并使用子系统（或模块库模块）名称作为文件名。

  当**文件名选项**设置为**使用子系统名称**时，如果模型中包含 Model 模块，或者正在为模型生成模型引用目标，则子系统文件名将被破坏。在这些情况下，子系统的文件名由子系统名称加上模型名称前缀构成。
- **使用函数名称** - 代码生成器使用**函数名称选项**指定的函数名称作为文件名。
- **用户指定** - 此选项将启用**文件名(无扩展名)** 文本输入字段。代码生成器将使用您输入的名称作为文件名。可以输入任何文件名，但不要带 `.c` 或 `.cpp`（或任何其他）扩展名。此文件名不必是唯一的。

  虽然子系统源文件名不需要唯一，但必须避免使用不唯一名称，否则会导致循环依赖关系。例如，`sys_a.h` 包括 `sys_b.h`，`sys_b.h` 包括 `sys_c.h`，而 `sys_c.h` 包括 `sys_a.h`。

默认值取决于模块配置。例如，Subsystem 模块的默认值为**自动**。CodeReuseSubsystem 模块的默认值为**使用函数名称**。

##### 依赖关系

- 此参数要求具有 Simulink Coder 许可证。
- 要启用此参数，请将**函数打包**设置为**不可重用函数**或**可重用函数**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RTWFileNameOpts` |
| **值:** | `'Auto'` | `'Use subsystem name'` | `'Use function name'` | `'User specified'` |

#### **文件名(无扩展名)** — 所生成文件的名称 无默认值

您指定的文件名不必是唯一的。但是，避免使用非唯一名称，否则会导致循环依赖关系。例如，`sys_a.h` 包括 `sys_b.h`，`sys_b.h` 包括 `sys_c.h`，而 `sys_c.h` 包括 `sys_a.h`。

有关详细信息，请参阅将子系统代码生成为单独的函数和文件 (Simulink Coder)。

##### 依赖关系

- 此参数要求具有 Simulink Coder 许可证。
- 要启用此参数，请将**文件名选项**设置为**用户指定**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RTWFileName` |
| **值:** | `''` (默认) | filename in quotes |
| **数据类型:** | `char` | `string` |

#### **函数接口** — 如何将参量与生成的函数结合使用 **void\_void** (默认) | **允许参量(优化)** | **允许参量(匹配图形接口)**

选择如何在生成的函数中使用参量。

- **void\_void** - 生成不带参量的函数，并将数据作为全局变量进行传递。例如：

  ```
  void subsystem_function(void)
  ```
- **允许参量(优化)** - 生成带参量的函数，而不是将数据作为全局变量进行传递。此规范可以减少全局 RAM。此选项可以减小代码大小、提高执行速度，并支持代码生成器应用更多的优化。例如：

  ```
  void subsystem_function(real_T rtu_In1, real_T rtu_In2,
                          real_T *rty_Out1)
  ```

  在某些情况下，当生成优化代码时，代码生成器可能不会生成具有参量的函数。
- **允许参量(匹配图形接口）** - 生成一个函数接口，该接口与 Subsystem 图形模块接口匹配的参量。生成的函数接口是可预知的，并且不会更改。可预知的接口对于调试和测试代码以及与外部应用程序集成非常有用。例如，如果模型有两个 Inport 模块和两个 Outport 模块，则生成的函数接口是：

  ```
  void subsystem_function(real_T rtu_In1, real_T rtu_In2,
                          real_T *rty_Out1, real_T *rty_Out2)
  ```

有关详细信息，请参阅：

- 减少不可重用的子系统函数中的全局变量 (Embedded Coder)
- Generate Predictable Function Interface to Match Graphical Block Interface (Embedded Coder)
- 为非虚拟子系统生成模块化函数代码 (Embedded Coder)

##### 依赖关系

- 此参数需要 Embedded Coder 许可证和一个基于 ERT 的系统目标文件。
- 要启用此参数，请将**函数打包**设置为**不可重用函数**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `FunctionInterfaceSpec` |
| **值:** | `'void_void'` (默认) | `'Allow arguments (Optimized)'` | `'Allow arguments (Match graphical interface)'` |

#### **具有独立数据的函数** — 控制子系统的代码生成 `off` (默认) | `on`

生成其中原子子系统的内部数据与其父级模型分离且归子系统所有的子系统函数代码。

- `off` - 不生成其中原子子系统的内部数据与其父级模型分离且归子系统所有的子系统函数代码。
- `on` - 生成其中原子子系统的内部数据与其父级模型分离且归子系统所有的子系统函数代码。子系统数据结构的声明独立于父模型数据结构。带单独数据的子系统具有其自己的模块 I/O 和 `DWork` 数据结构。因此，为子系统生成的代码更容易跟踪和检验。数据分离还可以减小整个模型的全局数据结构的最大大小，因为它们被拆分成多个数据结构。

有关如何为原子子系统生成模块化函数代码的详细信息，请参阅为非虚拟子系统生成模块化函数代码 (Embedded Coder)。

有关如何对原子子系统应用内存段的详细信息，请参阅Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

##### 依赖关系

- 此参数需要 Embedded Coder 许可证和一个基于 ERT 的系统目标文件。
- 要启用此参数，请将**函数打包**设置为**不可重用函数**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `FunctionWithSeparateData` |
| **值:** | `'off'` (默认) | `'on'` |

#### **用于初始化/终止函数的内存段** — 如何应用内存段 **从模型继承** (默认) | **默认** | 模型内存段

选择软件如何将内存段应用于子系统初始化和终止函数。

- **从模型继承** - 将根模型内存段应用于子系统函数代码。
- **默认** - 不将内存段应用于子系统的系统代码，覆盖任何模型级的设置。
- 将模型的某个内存段应用于子系统。

##### 提示

- 可能的值根据您为模型配置设置的内存段数据包（如果有）而不同。请参阅Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)和模型配置参数：代码生成 (Simulink Coder)。
- 如果您没有为模型配置数据包，将只显示**从模型继承**。否则，列表中将包括**默认**以及模型包中的所有内存段。
- 这些选项对于为给定子系统覆盖模型内存段设置很有用。有关如何对原子子系统应用内存段的详细信息，请参阅Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

##### 依赖关系

- 此参数需要 Embedded Coder 许可证和一个基于 ERT 的系统目标文件。
- 要启用此参数，请将**函数打包**设置为**不可重用函数**或**可重用函数**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RTWMemSecFuncInitTerm` |
| **值:** | `'Inherit from model'` (默认) | `'Default'` | model memory section in quotes |

#### **用于执行函数的内存段** — 如何应用内存段 **从模型继承** (默认) | **默认** | 模型内存段

选择 Embedded Coder 如何将内存段应用于子系统执行函数。

- **从模型继承** - 将根模型内存段应用于子系统函数代码。
- **默认** - 不将内存段应用于子系统的系统代码，覆盖任何模型级的设置。
- 将模型的某个内存段应用于子系统。

##### 提示

- 可能的值根据您为模型配置设置的内存段数据包（如果有）而不同。请参阅Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)和模型配置参数：代码生成 (Simulink Coder)。
- 如果您没有为模型配置数据包，将只显示**从模型继承**。否则，列表中将包括**默认**以及模型包中的所有内存段。
- 这些选项对于为给定子系统覆盖模型内存段设置很有用。有关如何对原子子系统应用内存段的详细信息，请参阅Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

##### 依赖关系

- 此参数需要 Embedded Coder 许可证和一个基于 ERT 的系统目标文件。
- 要启用此参数，请将**函数打包**设置为**不可重用函数**或**可重用函数**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RTWMemSecFuncExecute` |
| **值:** | `'Inherit from model'` (默认) | `'Default'` | model memory section in quotes |

#### **用于常量的内存段** — 如何应用内存段 **从模型继承** (默认) | **默认** | 模型内存段

选择软件如何将内存段应用于子系统常量。

- **从模型继承** - 将根模型内存段应用于子系统数据。
- **默认** - 不要将内存段应用于子系统数据，将覆盖任何模型级的设置。
- 将模型的某个内存段应用于子系统。

##### 提示

- 您指定的内存段将应用于生成的代码中对应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅Standard Data Structures (Simulink Coder)。
- 可能的值根据您为模型配置设置的内存段数据包（如果有）而不同。请参阅Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果您没有为模型配置数据包，将只显示**从模型继承**。否则，列表中将包括**默认**以及模型包中的所有内存段。
- 这些选项对于为给定子系统覆盖模型内存段设置很有用。有关如何对原子子系统应用内存段的详细信息，请参阅Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

##### 依赖关系

- 此参数需要 Embedded Coder 许可证和一个基于 ERT 的系统目标文件。
- 要启用此参数，请将**函数打包**设置为**不可重用函数**，然后选择**具有独立数据的函数**参数。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RTWMemSecDataConstants` |
| **值:** | `'Inherit from model'` (默认) | `'Default'` | model memory section in quotes |

#### **用于内部数据的内存段** — 如何应用内存段 **从模型继承** (默认) | **默认** | 模型内存段

选择软件如何将内存段应用于子系统内部数据。

- **从模型继承** - 将根模型内存段应用于子系统数据。
- **默认** - 不要将内存段应用于子系统数据，将覆盖任何模型级的设置。
- 将模型的某个内存段应用于子系统。

##### 提示

- 您指定的内存段将应用于生成的代码中对应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅Standard Data Structures (Simulink Coder)。
- 可能的值根据您为模型配置设置的内存段数据包（如果有）而不同。请参阅Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果您没有为模型配置数据包，将只显示**从模型继承**。否则，列表中将包括**默认**以及模型包中的所有内存段。
- 这些选项对于为给定子系统覆盖模型内存段设置很有用。有关如何对原子子系统应用内存段的详细信息，请参阅Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

##### 依赖关系

- 此参数需要 Embedded Coder 许可证和一个基于 ERT 的系统目标文件。
- 要启用此参数，请将**函数打包**设置为**不可重用函数**，然后选择**具有独立数据的函数**参数。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RTWMemSecDataInternal` |
| **值:** | `'Inherit from model'` (默认) | `'Default'` | model memory section in quotes |

#### **用于参数的内存段** — 如何应用内存段 **从模型继承** (默认) | **默认** | 模型内存段

选择软件如何将内存段应用于子系统参数。

- **从模型继承** - 将根模型内存段应用于子系统函数代码。
- **默认** - 不将内存段应用于子系统的系统代码，覆盖任何模型级的设置。
- 将模型的某个内存段应用于子系统。

##### 提示

- 您指定的内存段将应用于生成的代码中对应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅Standard Data Structures (Simulink Coder)。
- 可能的值根据您为模型配置设置的内存段数据包（如果有）而不同。请参阅Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果您没有为模型配置数据包，将只显示**从模型继承**。否则，列表中将包括**默认**以及模型包中的所有内存段。
- 这些选项对于为给定子系统覆盖模型内存段设置很有用。有关如何对原子子系统应用内存段的详细信息，请参阅Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

##### 依赖关系

- 此参数需要 Embedded Coder 许可证和一个基于 ERT 的系统目标文件。
- 要启用此参数，请将**函数打包**设置为**不可重用函数**，然后选择**具有独立数据的函数**参数。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RTWMemSecDataParameters` |
| **值:** | `'Inherit from model'` (默认) | `'Default'` | model memory section in quotes |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `否` |
| **多维信号** | `是a` |
| **可变大小信号** | `是a` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 实际支持的数据类型或功能取决于模块实施。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

实际代码生成支持取决于模块实现。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| **模块**（默认值） | 为子系统和子系统内的模块生成代码。 |
| **BlackBox** | 生成黑盒接口。生成的 HDL 代码仅包括子系统的输入/输出端口定义。因此，您可以在模型中使用子系统来生成与手动编写的现有 HDL 代码的接口。  子系统的黑盒接口生成类似于没有时钟信号的 Model 模块接口生成。 |
| **无 HDL** | 从生成的代码中删除子系统。您可以在仿真中使用子系统，但在 HDL 代码中将其视为“无操作”。 |

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **AdaptivePipelining** | 基于综合工具、目标频率和乘法器字长的自动流水线插入。默认值为 **inherit**。另请参阅AdaptivePipelining (HDL Coder)。 |
| **BalanceDelays** | 检测沿一条路径引入的新延迟，并在其他路径上插入匹配的延迟。默认值为 **inherit**。另请参阅BalanceDelays (HDL Coder)。 |
| **ClockRatePipelining** | 以较快的时钟频率而不是较慢的数据速率插入流水线寄存器。默认值为 **inherit**。另请参阅ClockRatePipelining (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分配或寄存器重定时。默认值为 **inherit**。另请参阅DistributedPipelining (HDL Coder)。 |
| **DSPStyle** | 乘法器映射的综合属性。默认值为**无**。另请参阅DSPStyle (HDL Coder)。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中删除子系统层次结构。默认值为 **inherit**。另请参阅FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的功能等效的资源的数量。默认值为 0。另请参阅Resource Sharing (HDL Coder)。 |
| **StreamingFactor** | 并行数据路径或向量的数量，这些路径或向量通过时间多路复用的方式变换为串行标量数据路径。默认值为 0，表示实现完全并行的数据路径。另请参阅Streaming (HDL Coder)。 |

**目标设定**

此模块不能为 DUT，因此**目标设定**选项卡中的模块属性设置将被忽略。

**限制**

如果子系统的输出是总线，则输出端口的**初始条件**必须为 0。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型支持取决于模块实现。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Ports & Subsystems

## Description

The Switch Case Action Subsystem block is a Subsystem block preconfigured as a starting point for creating a subsystem whose
execution is controlled by a Switch Case block. The input port to a
Switch Case block selects a case defined using the **Case
conditions** parameter. Depending on input value and case selected, an action
signal is sent to execute a Switch Case Action Subsystem block. Execution of
the subsystem is controlled by an Action Port block placed inside the
subsystem.

Simulink® ignores a priority set on an Switch Case Action Subsystem
block. Instead, set the priority on the Switch Case block that initiates
execution of the subsystem.

All blocks in a Switch Case Action Subsystem block must run at the same
rate as the driving Switch Case block. You can achieve this requirement by
setting each block sample time parameter to be either inherited (`-1`) or the
same value as the Switch Case block sample time.

### Merge Signals from Switch Case Action Subsystem Blocks

The example model `ex_switch_case_block` shows how to create one signal
from multiple subsystem output signals. For more information, see Select Subsystem Execution.

Model ex\_switch\_case\_block

The Switch Case block selects the execution of one If Action
Subsystem block from a set of subsystems. Regardless of which subsystem the
Switch Case block selects, you can create one resulting signal with a
Merge block.

## Ports

### Input

### **In1** — Signal input to a subsystem scalar | vector | matrix

Placing an Inport block in a subsystem adds an external input port
to the Subsystem block. The port label matches the name of the
Inport block.

Use Inport blocks to get signals from the local environment.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Action** — Control signal input to a subsystem scalar | vector | matrix

The Action Port block inside
a subsystem adds an external input port to the Subsystem
block and changes the block to a Switch Case Action
Subsystem block.

**Note**

The Action Port block is not available in the
Simulink Library Browser. When using the Switch Case
Action Subsystem block, you can access the Action
Port block only from within the Switch Case
Action Subsystem block.

Dot-dash lines from a Switch Case block to a Switch Case Action
Subsystem block represent *action*
signals. An action signal is a control signal connected to the
**Action** port of a Switch Case Action
Subsystem block. A message on the action signal initiates
execution of the subsystem.

**Data Types:** `action`
### Output

### **Out1** — Signal output from a subsystem scalar | vector | matrix

Placing an Outport block in a subsystem adds an output
port from the Subsystem block. The port label on the subsystem block is
the name of the Outport block.

Use Outport blocks to send signals to the local
environment.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Show port labels** — Display options for port labels `FromPortIcon` (default) | `FromPortBlockName` | `SignalName` | `none`

Select how to display port labels on the Subsystem block icon.

- `none` — Do not display port labels.
- `FromPortIcon` — If the corresponding port icon displays a signal name, display the signal name on the Subsystem block. Otherwise, display the port block name or the port number if the block name is a default name.
- `FromPortBlockName` — Display the name of the corresponding port block on the Subsystem block.
- `SignalName` — If the signal connected to the port is named, display the name of the signal on the Subsystem block. Otherwise, display the name of the corresponding port block.

For port label editing on Subsystem blocks, see Edit Port Labels on Subsystem Blocks.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ShowPortLabels` |
| **Values:** | `'FromPortIcon'` (default) | `'FromPortBlockName'` | `'SignalName'` | `'none'` |

### **Read/Write permissions** — Levels of access to contents of subsystem `ReadWrite` (default) | `ReadOnly` | `NoReadOrWrite`

Control user access to the contents of the subsystem.

- `ReadWrite` — Enable opening and modification of subsystem contents.
- `ReadOnly` — Enable opening but not modification of the subsystem. If the subsystem resides in a block library, you can create and open links to the subsystem and can make and modify local copies of the subsystem but cannot change the permissions or modify the contents of the original library instance.
- `NoReadOrWrite` — Disable opening or modification of subsystem. If the subsystem resides in a library, you can create links to the subsystem in a model but cannot open, modify, change permissions, or create local copies of the subsystem.

You do not receive a response if you attempt to view the contents of a subsystem whose **Read/Write permissions** parameter is set to `NoReadOrWrite`. For example, when double-clicking such a subsystem, the software does not open the subsystem and does not display any messages.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Permissions` |
| **Values:** | `'ReadWrite'` (default) | `'ReadOnly'` | `'NoReadOrWrite'` |

### **Name of error callback function** — Name of function to be called if error occurs no default

Enter the name of a function to be called if an error occurs while the software executes the
subsystem.

The software passes two arguments to the function: the handle of the subsystem and a
character vector that specifies the error type. If no function is specified, the software
displays a generic error message if executing the subsystem causes an error.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ErrorFcn` |
| **Values:** | `''` (default) | function name in quotes |
| **Data Types:** | `char` | `string` |

### **Permit hierarchical resolution** — Resolution for workspace variable names `All` (default) | `ExplicitOnly` | `None`

Select whether to resolve names of workspace variables referenced by this subsystem.

For more information, see Symbol Resolution and Symbol Resolution Process.

- `All` — Resolve all names of workspace variables used by this subsystem, including those used to specify block parameter values and Simulink data objects (for example, `Simulink.Signal` objects).
- `ExplicitOnly` — Resolve only names of workspace variables used to specify block parameter values, data store memory (where no block exists), signals, and states marked as “must resolve”.
- `None` — Do not resolve any workspace variable names.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PermitHierarchicalResolution` |
| **Values:** | `'All'` (default) | `'ExplicitOnly'` | `'None'` |

### **Show subsystem reinitialize ports** — Option to display reinitialize event ports `off` (default) | `on`

Select this parameter to display the reinitialize event ports. Clear this parameter to remove the ports.

#### Dependencies

To enable this parameter, select **Treat as atomic unit**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ShowSubsystemReinitializePorts` |
| **Values:** | `'off'` (default) | `'on'` |

### Code Generation

Parameters on the Code Generation tab require a Simulink
Coder™ or Embedded Coder® license.

### **Function packaging** — Code format `Auto` | `Inline` | `Nonreusable function` | `Reusable function`

Select the code format to be generated for an atomic (nonvirtual) subsystem.

- `Auto` — The software chooses the optimal format for you
  based on the type and number of instances of the subsystem that exist in the
  model.
- `Inline` — The software inlines the subsystem
  unconditionally.
- `Nonreusable function` — If **Filename
  options** is set to `Auto`, the software packages
  separate functions in the model file. If **File name options** is
  set to `Use subsystem name`, `Use function
  name`, or `User specified` using different
  filenames, the software packages separate functions in separate files.

  Subsystems with this setting generate functions that might have arguments depending on
  the Function interface parameter setting.
  You can name the generated function and file using parameters Function name and File name (no extension), respectively.
  These functions are not reentrant.
- `Reusable function` — The software generates a function
  with arguments that allows reuse of subsystem code when a model includes multiple
  instances of the subsystem.

  This option also generates a function with arguments that allows subsystem code to
  be reused in the generated code of a model reference hierarchy that includes multiple
  instances of a subsystem across referenced models. In this case, the subsystem must be
  in a library.

For more information, see:

- Generate Code and Executables for Individual Subsystems (Simulink Coder)
- Generate Inlined Subsystem Code (Simulink Coder)
- Generate Subsystem Code as Separate Function and Files (Simulink Coder)
- Generate Reusable Code from Library Subsystems Shared Across Models (Simulink Coder)

The default value depends on the block configuration. For example, the default
value for the Subsystem block is `Auto`.
The default value for the CodeReuseSubsystem block is
`Reusable function`.

#### Tips

- When you want multiple instances of a subsystem to be represented as one
  reusable function, you can designate each one of them as
  `Auto` or as `Reusable
  function`. Using one or the other is best, as using both creates two
  reusable functions, one for each designation. The outcomes of these choices differ
  only when reuse is not possible. Selecting `Auto` does not
  allow control of the function or filename for the subsystem code.
- The `Reusable function` and `Auto`
  options both try to determine if multiple instances of a subsystem exist and if the
  code can be reused. The difference between the behavior of each option is that when
  reuse is not possible:

  - `Auto` yields inlined code, or if circumstances
    prohibit inlining, separate functions for each subsystem instance.
  - `Reusable function` yields a separate function
    with arguments for each subsystem instance in the model.
- If you select `Reusable function` while your generated
  code is under source control, set **File name options** to
  `Use subsystem name`, `Use function
  name`, or `User specified`. Otherwise, the
  names of your code files change whenever you modify your model, which prevents
  source control on your files.
- If you select an option other than `Auto` or
  `Inline` and the model configuration parameter
  **States**, the code generator produces separate output and
  update methods. The code generator does not take into account the
  **Combine output and update methods for code generation and
  simulation** specification.

#### Dependencies

- This parameter requires a Simulink
  Coder license for code generation.
- To enable this parameter, select **Treat as atomic
  unit**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RTWSystemCode` |
| **Values:** | `'Auto'` | `'Inline'` | `'Nonreusable function'` | `'Reusable function'` |

### **Function name options** — How to name generated function `Auto` | `Use subsystem name` | `User specified`

Select how the software names the function it generates for the subsystem.

If you have an Embedded Coder license, you can control function names with options on the Configuration
Parameter **Code Generation** > **Identifiers** pane.

- `Auto` — Assign a unique function name using the default
  naming convention,
  `model_subsystem()`,
  where *`model`* is the name of the model and
  *`subsystem`* is the name of the subsystem, or that of an
  identical one when code is being reused.

  If you select `Reusable function` for the
  **Function packaging** parameter and a model reference hierarchy
  contains multiple instances of the reusable subsystem, in order to generate reusable
  code for the subsystem, **Function name options** must be set to
  `Auto`.
- `Use subsystem name` — Use the subsystem name as the
  function name. By default, the function name uses the naming convention
  `model_subsystem`.

  When a subsystem is in a library block and the subsystem parameter Function packaging is set to
  `Reusable function`, if you set the
  `Use subsystem name` option, the code
  generator uses the name of the library block for the subsystem function
  name and filename.
- `User specified` — Enable the **Function
  name** field. Enter any legal C or C++ function name, which must be
  unique.

For more information, see Generate Subsystem Code as Separate Function and Files (Simulink Coder).

The default value depends on the block configuration. For example, the default
value for the Subsystem block is `Auto`.
The default value for the CodeReuseSubsystem block is
`Use subsystem name`.

#### Dependencies

- This parameter requires a Simulink
  Coder license.
- To enable this parameter, set **Function packaging** to
  `Nonreusable function` or `Reusable
  function`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RTWFcnNameOpts` |
| **Values:** | `'Auto'` | `'Use subsystem name'` | `'User specified'` |

### **Function name** — Name of function for subsystem code no default

Specify a unique, valid C or C++ function name for subsystem code.

Use this parameter if you want to give the function a specific name instead of
allowing the Simulink
Coder code generator to assign its own autogenerated name or use the subsystem
name. For more information, see Generate Subsystem Code as Separate Function and Files (Simulink Coder).

#### Dependencies

- This parameter requires a Simulink
  Coder license.
- To enable this parameter, set **Function name options** to
  `User specified`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RTWFcnName` |
| **Values:** | `''` (default) | function name in quotes |
| **Data Types:** | `char` | `string` |

### **File name options** — How to name generated file `Auto` | `Use subsystem name` | `Use function name` | `User specified`

Select how the software names the separate file for the function it generates for the
subsystem.

- `Auto` — Depending on the configuration of the subsystem
  and how many instances are in the model, `Auto` yields
  different results.

  - If the code generator does *not* generate a separate file
    for the subsystem, the subsystem code is generated within the code module
    generated from the subsystem parent system. If the subsystem parent is the model
    itself, the subsystem code is generated within
    `model.c` or
    `model.cpp`.
  - If you select `Reusable function` for the
    **Function packaging** parameter and your generated code is
    under source control, consider specifying a **File name
    options** value other than `Auto`. This
    prevents the generated filename from changing due to unrelated model
    modifications, which is problematic for using source control to manage
    configurations.
  - If you select `Reusable function` for the
    **Function packaging** parameter and a model reference
    hierarchy contains multiple instances of the reusable subsystem, in order to
    generate reusable code for the subsystem, **File name
    options** must be set to `Auto`.
- `Use subsystem name` — The code generator generates a
  separate file, using the subsystem (or library block) name as the filename.

  When **File name options** is set to `Use subsystem
  name`, the subsystem filename is mangled if the model contains
  Model blocks, or if a model reference target is being generated for
  the model. In these situations, the filename for the subsystem consists of the
  subsystem name prefixed by the model name.
- `Use function name` — The code generator uses the
  function name specified by **Function name options** as the
  filename.
- `User specified` — This option enables the
  **File name (no extension)** text entry field. The code generator
  uses the name you enter as the filename. Enter any filename, but do not include the
  `.c` or `.cpp` (or any other) extension. This
  filename need not be unique.

  While a subsystem source filename need not be unique, you must avoid giving nonunique
  names that result in cyclic dependencies. For example, `sys_a.h`
  includes `sys_b.h`, `sys_b.h` includes
  `sys_c.h`, and `sys_c.h` includes
  `sys_a.h`.

The default value depends on the block configuration. For example, the default
value for the Subsystem block is `Auto`.
The default value for the CodeReuseSubsystem block is
`Use function name`.

#### Dependencies

- This parameter requires a Simulink
  Coder license.
- To enable this parameter, set **Function packaging** to
  `Nonreusable function` or `Reusable
  function`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RTWFileNameOpts` |
| **Values:** | `'Auto'` | `'Use subsystem name'` | `'Use function name'` | `'User specified'` |

### **File name (no extension)** — Name of generated file no default

The filename that you specify does not have to be unique. However, avoid giving
non-unique names that result in cyclic dependencies. For example,
`sys_a.h` includes `sys_b.h`,
`sys_b.h` includes `sys_c.h`, and
`sys_c.h` includes `sys_a.h`.

For more information, see Generate Subsystem Code as Separate Function and Files (Simulink Coder).

#### Dependencies

- This parameter requires a Simulink
  Coder license.
- To enable this parameter, set **File name options** to
  `User specified`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RTWFileName` |
| **Values:** | `''` (default) | filename in quotes |
| **Data Types:** | `char` | `string` |

### **Function interface** — How to use arguments with generated function `void_void` (default) | `Allow arguments (Optimized)` | `Allow arguments (Match graphical interface)`

Select how to use arguments with the generated function.

- `void_void` — Generate a function without arguments and
  pass data as global variables. For example:

  ```
  void subsystem_function(void)
  ```
- `Allow arguments (Optimized)` — Generate a function that
  uses arguments instead of passing data as global variables. This specification reduces
  global RAM. This option might reduce code size and improve execution speed and enable
  the code generator to apply additional optimizations. For
  example:

  ```
  void subsystem_function(real_T rtu_In1, real_T rtu_In2,
                          real_T *rty_Out1)
  ```

  In some cases, when generating optimized code, the code generator might not
  generate a function that has arguments.
- `Allow arguments (Match graphical interface)` — Generate
  a function interface that uses arguments that match the Subsystem
  graphical block interface. The generated function interface is predictable and does
  not change. A predictable interface can be useful for debugging and testing your code
  and integrating with external applications. For example, if a model has two
  Inport blocks and two Outport blocks, then the
  generated function interface
  is:

  ```
  void subsystem_function(real_T rtu_In1, real_T rtu_In2,
                          real_T *rty_Out1, real_T *rty_Out2)
  ```

For more information, see:

- Reduce Global Variables in Nonreusable Subsystem Functions (Embedded Coder)
- Generate Predictable Function Interface to Match Graphical Block Interface (Embedded Coder)
- Generate Modular Function Code for Nonvirtual Subsystems (Embedded Coder)

#### Dependencies

- This parameter requires an Embedded Coder license and an ERT-based system target file.
- To enable this parameter, set **Function packaging** to
  `Nonreusable function`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `FunctionInterfaceSpec` |
| **Values:** | `'void_void'` (default) | `'Allow arguments (Optimized)'` | `'Allow arguments (Match graphical interface)'` |

### **Function with separate data** — Control code generation for subsystem `off` (default) | `on`

Generate subsystem function code in which the internal data for an atomic subsystem is
separated from its parent model and is owned by the subsystem.

- `off` — Do not generate subsystem function code in which the
  internal data for an atomic subsystem is separated from its parent model and is owned
  by the subsystem.
- `on` — Generate subsystem function code in which the internal
  data for an atomic subsystem is separated from its parent model and is owned by the
  subsystem. The subsystem data structure is declared independently from the parent
  model data structures. A subsystem with separate data has its own block I/O and
  `DWork` data structure. As a result, the generated code for the
  subsystem is easier to trace and test. The data separation also tends to reduce the
  maximum size of global data structures throughout the model, because they are split
  into multiple data structures.

For details on how to generate modular function code for an atomic subsystem, see
Generate Modular Function Code for Nonvirtual Subsystems (Embedded Coder).

For details on how to apply memory sections to atomic subsystems, see Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder).

#### Dependencies

- This parameter requires an Embedded Coder license and an ERT-based system target file.
- To enable this parameter, set **Function packaging** to
  `Nonreusable function`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `FunctionWithSeparateData` |
| **Values:** | `'off'` (default) | `'on'` |

### **Memory section for initialize/terminate functions** — How to apply memory sections `Inherit from model` (default) | `Default` | model memory section

Select how the software applies memory sections to the subsystem initialization and
termination functions.

- `Inherit from model` — Apply the root model memory
  sections to the subsystem function code.
- `Default` — Do not apply memory sections to the subsystem
  system code, overriding any model-level specification.
- Apply one of the model memory sections to the subsystem.

#### Tips

- The possible values vary depending on what, if any, package of memory sections
  you have set for the model configuration. See Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder) and Model Configuration Parameters: Code Generation (Simulink Coder).
- If you have not configured the model with a package, `Inherit from
  model` is the only available value. Otherwise, the list includes
  `Default` and all memory sections the model package
  contains.
- These options can be useful for overriding the model memory section settings for
  the given subsystem. For details on how to apply memory sections to atomic
  subsystems, see Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder).

#### Dependencies

- This parameter requires an Embedded Coder license and an ERT-based system target file.
- To enable this parameter, set **Function packaging** to
  `Nonreusable function` or `Reusable
  function`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RTWMemSecFuncInitTerm` |
| **Values:** | `'Inherit from model'` (default) | `'Default'` | model memory section in quotes |

### **Memory section for execution functions** — How to apply memory sections `Inherit from model` (default) | `Default` | model memory section

Select how Embedded Coder applies memory sections to the subsystem execution functions.

- `Inherit from model` — Apply the root model memory
  sections to the subsystem function code.
- `Default` — Do not apply memory sections to the subsystem
  system code, overriding any model-level specification.
- Apply one of the model memory sections to the subsystem.

#### Tips

- The possible values vary depending on what, if any, package of memory sections
  you have set for the model configuration. See Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder) and Model Configuration Parameters: Code Generation (Simulink Coder).
- If you have not configured the model with a package, `Inherit from
  model` is the only available value. Otherwise, the list includes
  `Default` and all memory sections the model package
  contains.
- These options can be useful for overriding the model memory section settings for
  the given subsystem. For details on how to apply memory sections to atomic
  subsystems, see Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder).

#### Dependencies

- This parameter requires an Embedded Coder license and an ERT-based system target file.
- To enable this parameter, set **Function packaging** to
  `Nonreusable function` or `Reusable
  function`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RTWMemSecFuncExecute` |
| **Values:** | `'Inherit from model'` (default) | `'Default'` | model memory section in quotes |

### **Memory section for constants** — How to apply memory sections `Inherit from model` (default) | `Default` | model memory section

Select how the software applies memory sections to the subsystem constants.

- `Inherit from model` — Apply the root model memory
  sections to the subsystem data.
- `Default` — Do not apply memory sections to the subsystem
  data, overriding any model-level specification.
- Apply one of the model memory sections to the subsystem.

#### Tips

- The memory section that you specify applies to the corresponding global data
  structures in the generated code. For basic information about the global data
  structures generated for atomic subsystems, see Standard Data Structures (Simulink Coder).
- The possible values vary depending on what, if any, package of memory sections
  you have set for the model configuration. See Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder).
- If you have not configured the model with a package, `Inherit from
  model` is the only available value. Otherwise, the list includes
  `Default` and all memory sections the model package
  contains.
- These options can be useful for overriding the model memory section settings for
  the given subsystem. For details on how to apply memory sections to atomic
  subsystems, see Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder).

#### Dependencies

- This parameter requires an Embedded Coder license and an ERT-based system target file.
- To enable this parameter, set **Function packaging** to
  `Nonreusable function` and select the
  **Function with separate data** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RTWMemSecDataConstants` |
| **Values:** | `'Inherit from model'` (default) | `'Default'` | model memory section in quotes |

### **Memory section for internal data** — How to apply memory sections `Inherit from model` (default) | `Default` | model memory section

Select how the software applies memory sections to the subsystem internal data.

- `Inherit from model` — Apply the root model memory
  sections to the subsystem data.
- `Default` — Do not apply memory sections to the subsystem
  data, overriding any model-level specification.
- Apply one of the model memory sections to the subsystem.

#### Tips

- The memory section that you specify applies to the corresponding global data
  structures in the generated code. For basic information about the global data
  structures generated for atomic subsystems, see Standard Data Structures (Simulink Coder).
- The possible values vary depending on what, if any, package of memory sections
  you have set for the model configuration. See Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder).
- If you have not configured the model with a package, `Inherit from
  model` is the only available value. Otherwise, the list includes
  `Default` and all memory sections the model package
  contains.
- These options can be useful for overriding the model memory section settings for
  the given subsystem. For details on how to apply memory sections to atomic
  subsystems, see Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder).

#### Dependencies

- This parameter requires an Embedded Coder license and an ERT-based system target file.
- To enable this parameter, set **Function packaging** to
  `Nonreusable function` and select the
  **Function with separate data** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RTWMemSecDataInternal` |
| **Values:** | `'Inherit from model'` (default) | `'Default'` | model memory section in quotes |

### **Memory section for parameters** — How to apply memory sections `Inherit from model` (default) | `Default` | model memory section

Select how the software applies memory sections to the subsystem parameters.

- `Inherit from model` — Apply the root model memory
  sections to the subsystem function code.
- `Default` — Do not apply memory sections to
  the subsystem system code, overriding any model-level
  specification.
- Apply one of the model memory sections to the subsystem.

#### Tips

- The memory section that you specify applies to the corresponding global data
  structure in the generated code. For basic information about the global data
  structures generated for atomic subsystems, see Standard Data Structures (Simulink Coder).
- The possible values vary depending on what, if any, package of memory sections
  you have set for the model configuration. See Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder).
- If you have not configured the model with a package, `Inherit from
  model` is the only available value. Otherwise, the list includes
  `Default` and all memory sections the model package
  contains.
- These options can be useful for overriding the model memory section settings for
  the given subsystem. For details on how to apply memory sections to atomic
  subsystems, see Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder).

#### Dependencies

- This parameter requires an Embedded Coder license and an ERT-based system target file.
- To enable this parameter, set **Function packaging** to
  `Nonreusable function` and select the
  **Function with separate data** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RTWMemSecDataParameters` |
| **Values:** | `'Inherit from model'` (default) | `'Default'` | model memory section in quotes |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `yesa` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual code generation support depends on block implementation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `Module` (default) | Generate code for the subsystem and the blocks within the subsystem. |
| `BlackBox` | Generate a black box interface. The generated HDL code includes only the input/output port definitions for the subsystem. Therefore, you can use a subsystem in your model to generate an interface to existing, manually written HDL code.  The black-box interface generation for subsystems is similar to the Model block interface generation without the clock signals. |
| `No HDL` | Remove the subsystem from the generated code. You can use the subsystem in simulation, however, treat it as a “no-op” in the HDL code. |

**HDL Block Properties**

| General | |
| --- | --- |
| **AdaptivePipelining** | Automatic pipeline insertion based on the synthesis tool, target frequency, and multiplier word-lengths. The default is `inherit`. See also AdaptivePipelining (HDL Coder). |
| **BalanceDelays** | Detects introduction of new delays along one path and inserts matching delays on the other paths. The default is `inherit`. See also BalanceDelays (HDL Coder). |
| **ClockRatePipelining** | Insert pipeline registers at a faster clock rate instead of the slower data rate. The default is `inherit`. See also ClockRatePipelining (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **DistributedPipelining** | Pipeline register distribution, or register retiming. The default is `inherit`. See also DistributedPipelining (HDL Coder). |
| **DSPStyle** | Synthesis attributes for multiplier mapping. The default is `none`. See also DSPStyle (HDL Coder). |
| **FlattenHierarchy** | Remove subsystem hierarchy from generated HDL code. The default is `inherit`. See also FlattenHierarchy (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |
| **StreamingFactor** | Number of parallel data paths, or vectors, that are time multiplexed to transform into serial, scalar data paths. The default is 0, which implements fully parallel data paths. See also Streaming (HDL Coder). |

**Target Specification**

This block cannot be the DUT, so the block property settings in the **Target
Specification** tab are ignored.

**Restrictions**

If the output of the subsystem is a bus then **Initial
condition** of the outport must be 0.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type support depends on block implementation.

## Version History

**Introduced before R2006a**
