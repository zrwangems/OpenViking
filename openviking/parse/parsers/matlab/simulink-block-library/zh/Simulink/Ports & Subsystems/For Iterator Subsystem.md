---
type: simulink-block
title: 'For Iterator Subsystem'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'foriteratorsubsystem'
documentation_source_path: 'slref/foriteratorsubsystem.html'
language: zh-CN
chinese_source: official
---

# For Iterator Subsystem

## 端口

### 输入

### **In** — 子系统模块的信号输入 标量 | 向量 | 矩阵

在子系统中放置一个 Inport 模块会向 Subsystem 模块添加一个外部输入端口。端口标签与 Inport 模块的名称相匹配。

使用 Inport 模块可以从局部环境中获取信号。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### 输出

### **Out** — 子系统的信号输出 标量 | 向量 | 矩阵

在子系统中放置一个 Outport 模块会从 Subsystem 模块添加一个输出端口。Subsystem 模块上的端口标签是 Outport 模块的名称。

使用 Outport 模块可以向局部环境发送信号。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条中，在**仿真**选项卡的**准备**库中，选择**属性检查器**。

### 常设

### **显示端口标签** — 端口标签的显示选项 **FromPortIcon** (默认) | **FromPortBlockName** | **SignalName** | **无**

选择如何在 Subsystem 模块图标上显示端口标签。

- **无** - 不显示端口标签。
- **FromPortIcon** - 如果对应的端口图标显示了信号名称，则在 Subsystem 模块上显示信号名称。否则，如果模块名称是默认名称，则显示端口模块名称或端口号。
- **FromPortBlockName** - 在 Subsystem 模块上显示对应端口模块的名称。
- **SignalName** - 如果连接到端口的信号已命名，则会在 Subsystem 模块上显示信号的名称。否则，显示相应端口模块的名称。

有关 Subsystem 模块上的端口标签编辑，请参阅编辑子系统模块上的端口标签。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ShowPortLabels` |
| **值:** | `'FromPortIcon'` (默认) | `'FromPortBlockName'` | `'SignalName'` | `'none'` |

### **读取/写入权限** — 子系统内容的访问级别 **ReadWrite** (默认) | **ReadOnly** | **NoReadOrWrite**

控制用户对子系统内容的访问。

- **ReadWrite** - 允许打开和修改子系统内容。
- **ReadOnly** - 允许打开但不允许修改子系统。如果子系统在模块库中，您可以创建和打开该子系统的链接，创建和修改子系统的本地副本，但不能更改权限或修改原始模块库实例的内容。
- **NoReadOrWrite** - 禁止打开或修改子系统。如果子系统在模块库中，您可以在模型中创建该子系统的链接，但不能打开、修改、更改权限或创建子系统的本地副本。

如果您尝试查看其**读取/写入权限**参数设置为 **NoReadOrWrite** 的子系统的内容，将不会收到响应。例如，当您双击此类子系统时，软件不会打开该子系统，并且不显示任何消息。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Permissions` |
| **值:** | `'ReadWrite'` (默认) | `'ReadOnly'` | `'NoReadOrWrite'` |

### **错误回调函数的名称** — 发生错误时要调用的函数的名称 无默认值

输入软件执行子系统时，如果发生错误要调用的函数的名称。

该软件向函数传递两个参量：子系统的句柄以及指定错误类型的字符向量。如果未指定任何函数，当执行子系统导致错误时，软件将显示常规错误消息。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ErrorFcn` |
| **值:** | `''` (默认) | function name in quotes |
| **数据类型:** | `char` | `string` |

### **允许层次解析** — 工作区变量名称解析 **全部** (默认) | **ExplicitOnly** | **无**

选择是否解析此子系统引用的工作区变量的名称。

有关详细信息，请参阅符号解析和符号解析过程。

- **全部** - 解析此子系统使用的所有工作区变量的名称，包括用来指定模块参数值和 Simulink 数据对象（例如，`Simulink.Signal` 对象）的工作区变量的名称。
- **ExplicitOnly** - 只解析用来指定模块参数值、数据存储内存（不存在模块）、信号以及标有“must resolve”状态的工作区变量的名称。
- **无** - 不解析任何工作区变量名称。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `PermitHierarchicalResolution` |
| **值:** | `'All'` (默认) | `'ExplicitOnly'` | `'None'` |

### **显示子系统重新初始化端口** — 显示重新初始化事件端口的选项 `off` (默认) | `on`

选中此参数可显示重新初始化事件端口。清除此参数可删除这些端口。

#### 依赖关系

要启用此参数，请选择**视为原子单元**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ShowSubsystemReinitializePorts` |
| **值:** | `'off'` (默认) | `'on'` |

### 代码生成

设置“代码生成”选项卡上的参数需要具有 Simulink Coder™ 或 Embedded Coder® 许可证。

### **函数打包** — 代码格式 **自动** | **内联** | **不可重用函数** | **可重用函数**

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

#### 提示

- 如果您希望子系统的多个实例表示为一个可重用函数，可以为每个子系统指定**自动**或**可重用函数**。最好是使用其中一个，因为使用两个将生成两个可重用函数，每个指定一个函数。仅当可以重用时，这些选项的结果才会有区别。选择**自动**则不允许控制子系统代码的函数或文件名。
- **可重用函数**和**自动**选项都尝试确定是否存在子系统的多个实例，以及是否可以重用代码。者两个选项的行为区别体现在不能重用时：

  - **自动**生成内联代码，或者在禁止内联的情况下为每个子系统实例生成一个单独的函数。
  - **可重用函数**为模型中的每个子系统实例生成一个单独的参量函数。
- 如果您在生成的代码处于源代码管理状态下时选择了**可重用函数**，请将**文件名选项**设置为**使用子系统名称**、**使用函数名称**或**用户指定**。否则，只要您修改模型，代码文件的名称就会改变，从而无法对文件进行源代码管理。
- 如果您选择除**自动**或**内联**以外的选项，并且使用模型配置参数**状态**，则代码生成器会生成单独的输出和更新方法。代码生成器不考虑**为代码生成和仿真合并输出和更新方法**设定。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证才能生成代码。
- 要启用此参数，请选择**视为原子单元**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RTWSystemCode` |
| **值:** | `'Auto'` | `'Inline'` | `'Nonreusable function'` | `'Reusable function'` |

### **函数名称选项** — 如何命名生成的函数 **自动** | **使用子系统名称** | **用户指定**

选择软件如何命名它为子系统生成的函数。

如果您拥有 Embedded Coder 许可证，则可以使用“配置参数”对话框的**代码生成** > **标识符**窗格上的选项来控制函数名称。

- **自动** - 使用默认的命名约定 `model_subsystem()` 指定唯一的函数名称，其中 *`model`* 是模型的名称，*`subsystem`* 是子系统的名称，或者，在重用代码时，也可以是相同子系统的名称。

  如果您为**函数打包**参数选择了**可重用函数**，而模型引用层次结构中存在可重用子系统的多个实例，则要为子系统生成可重用代码，必须将**函数名称选项**设置为**自动**。
- **使用子系统名称** - 使用子系统名称作为函数名称。默认情况下，函数名称使用命名约定 `model_subsystem`。

  当子系统在模块库模块中而子系统参数 函数打包 设置为**可重用函数**时，如果您设置**使用子系统名称**选项，代码生成器将使用模块库模块的名称作为子系统函数名和文件名。
- **用户指定** - 启用**函数名称**字段。输入任何合法的 C 或 C++ 函数名，此名称必须唯一。

有关详细信息，请参阅将子系统代码生成为单独的函数和文件 (Simulink Coder)。

默认值取决于模块配置。例如，Subsystem 模块的默认值为**自动**。CodeReuseSubsystem 模块的默认值为**使用子系统名称**。

#### 依赖关系

- 此参数要求具有 Simulink Coder 许可证。
- 要启用此参数，请将**函数打包**设置为**不可重用函数**或**可重用函数**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RTWFcnNameOpts` |
| **值:** | `'Auto'` | `'Use subsystem name'` | `'User specified'` |

### **函数名称** — 子系统代码的函数名称 无默认值

为子系统代码指定唯一的有效 C 或 C++ 函数名称。

如果您想为函数指定特定的名称，而不是让 Simulink Coder 代码生成器分配其自己自动生成的名称或者使用子系统名称，请使用此参数。有关详细信息，请参阅将子系统代码生成为单独的函数和文件 (Simulink Coder)。

#### 依赖关系

- 此参数要求具有 Simulink Coder 许可证。
- 要启用此参数，请将**函数名称选项**设置为**用户指定**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RTWFcnName` |
| **值:** | `''` (默认) | function name in quotes |
| **数据类型:** | `char` | `string` |

### **文件名选项** — 如何命名生成的文件 **自动** | **使用子系统名称** | **使用函数名称** | **用户指定**

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

#### 依赖关系

- 此参数要求具有 Simulink Coder 许可证。
- 要启用此参数，请将**函数打包**设置为**不可重用函数**或**可重用函数**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RTWFileNameOpts` |
| **值:** | `'Auto'` | `'Use subsystem name'` | `'Use function name'` | `'User specified'` |

### **文件名(无扩展名)** — 所生成文件的名称 无默认值

您指定的文件名不必是唯一的。但是，避免使用非唯一名称，否则会导致循环依赖关系。例如，`sys_a.h` 包括 `sys_b.h`，`sys_b.h` 包括 `sys_c.h`，而 `sys_c.h` 包括 `sys_a.h`。

有关详细信息，请参阅将子系统代码生成为单独的函数和文件 (Simulink Coder)。

#### 依赖关系

- 此参数要求具有 Simulink Coder 许可证。
- 要启用此参数，请将**文件名选项**设置为**用户指定**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RTWFileName` |
| **值:** | `''` (默认) | filename in quotes |
| **数据类型:** | `char` | `string` |

### **函数接口** — 如何将参量与生成的函数结合使用 **void\_void** (默认) | **允许参量(优化)** | **允许参量(匹配图形接口)**

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

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和一个基于 ERT 的系统目标文件。
- 要启用此参数，请将**函数打包**设置为**不可重用函数**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `FunctionInterfaceSpec` |
| **值:** | `'void_void'` (默认) | `'Allow arguments (Optimized)'` | `'Allow arguments (Match graphical interface)'` |

### **具有独立数据的函数** — 控制子系统的代码生成 `off` (默认) | `on`

生成其中原子子系统的内部数据与其父级模型分离且归子系统所有的子系统函数代码。

- `off` - 不生成其中原子子系统的内部数据与其父级模型分离且归子系统所有的子系统函数代码。
- `on` - 生成其中原子子系统的内部数据与其父级模型分离且归子系统所有的子系统函数代码。子系统数据结构的声明独立于父模型数据结构。带单独数据的子系统具有其自己的模块 I/O 和 `DWork` 数据结构。因此，为子系统生成的代码更容易跟踪和检验。数据分离还可以减小整个模型的全局数据结构的最大大小，因为它们被拆分成多个数据结构。

有关如何为原子子系统生成模块化函数代码的详细信息，请参阅为非虚拟子系统生成模块化函数代码 (Embedded Coder)。

有关如何对原子子系统应用内存段的详细信息，请参阅Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和一个基于 ERT 的系统目标文件。
- 要启用此参数，请将**函数打包**设置为**不可重用函数**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `FunctionWithSeparateData` |
| **值:** | `'off'` (默认) | `'on'` |

### **用于初始化/终止函数的内存段** — 如何应用内存段 **从模型继承** (默认) | **默认** | 模型内存段

选择软件如何将内存段应用于子系统初始化和终止函数。

- **从模型继承** - 将根模型内存段应用于子系统函数代码。
- **默认** - 不将内存段应用于子系统的系统代码，覆盖任何模型级的设置。
- 将模型的某个内存段应用于子系统。

#### 提示

- 可能的值根据您为模型配置设置的内存段数据包（如果有）而不同。请参阅Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)和模型配置参数：代码生成 (Simulink Coder)。
- 如果您没有为模型配置数据包，将只显示**从模型继承**。否则，列表中将包括**默认**以及模型包中的所有内存段。
- 这些选项对于为给定子系统覆盖模型内存段设置很有用。有关如何对原子子系统应用内存段的详细信息，请参阅Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和一个基于 ERT 的系统目标文件。
- 要启用此参数，请将**函数打包**设置为**不可重用函数**或**可重用函数**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RTWMemSecFuncInitTerm` |
| **值:** | `'Inherit from model'` (默认) | `'Default'` | model memory section in quotes |

### **用于执行函数的内存段** — 如何应用内存段 **从模型继承** (默认) | **默认** | 模型内存段

选择 Embedded Coder 如何将内存段应用于子系统执行函数。

- **从模型继承** - 将根模型内存段应用于子系统函数代码。
- **默认** - 不将内存段应用于子系统的系统代码，覆盖任何模型级的设置。
- 将模型的某个内存段应用于子系统。

#### 提示

- 可能的值根据您为模型配置设置的内存段数据包（如果有）而不同。请参阅Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)和模型配置参数：代码生成 (Simulink Coder)。
- 如果您没有为模型配置数据包，将只显示**从模型继承**。否则，列表中将包括**默认**以及模型包中的所有内存段。
- 这些选项对于为给定子系统覆盖模型内存段设置很有用。有关如何对原子子系统应用内存段的详细信息，请参阅Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和一个基于 ERT 的系统目标文件。
- 要启用此参数，请将**函数打包**设置为**不可重用函数**或**可重用函数**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RTWMemSecFuncExecute` |
| **值:** | `'Inherit from model'` (默认) | `'Default'` | model memory section in quotes |

### **用于常量的内存段** — 如何应用内存段 **从模型继承** (默认) | **默认** | 模型内存段

选择软件如何将内存段应用于子系统常量。

- **从模型继承** - 将根模型内存段应用于子系统数据。
- **默认** - 不要将内存段应用于子系统数据，将覆盖任何模型级的设置。
- 将模型的某个内存段应用于子系统。

#### 提示

- 您指定的内存段将应用于生成的代码中对应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅Standard Data Structures (Simulink Coder)。
- 可能的值根据您为模型配置设置的内存段数据包（如果有）而不同。请参阅Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果您没有为模型配置数据包，将只显示**从模型继承**。否则，列表中将包括**默认**以及模型包中的所有内存段。
- 这些选项对于为给定子系统覆盖模型内存段设置很有用。有关如何对原子子系统应用内存段的详细信息，请参阅Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和一个基于 ERT 的系统目标文件。
- 要启用此参数，请将**函数打包**设置为**不可重用函数**，然后选择**具有独立数据的函数**参数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RTWMemSecDataConstants` |
| **值:** | `'Inherit from model'` (默认) | `'Default'` | model memory section in quotes |

### **用于内部数据的内存段** — 如何应用内存段 **从模型继承** (默认) | **默认** | 模型内存段

选择软件如何将内存段应用于子系统内部数据。

- **从模型继承** - 将根模型内存段应用于子系统数据。
- **默认** - 不要将内存段应用于子系统数据，将覆盖任何模型级的设置。
- 将模型的某个内存段应用于子系统。

#### 提示

- 您指定的内存段将应用于生成的代码中对应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅Standard Data Structures (Simulink Coder)。
- 可能的值根据您为模型配置设置的内存段数据包（如果有）而不同。请参阅Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果您没有为模型配置数据包，将只显示**从模型继承**。否则，列表中将包括**默认**以及模型包中的所有内存段。
- 这些选项对于为给定子系统覆盖模型内存段设置很有用。有关如何对原子子系统应用内存段的详细信息，请参阅Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和一个基于 ERT 的系统目标文件。
- 要启用此参数，请将**函数打包**设置为**不可重用函数**，然后选择**具有独立数据的函数**参数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RTWMemSecDataInternal` |
| **值:** | `'Inherit from model'` (默认) | `'Default'` | model memory section in quotes |

### **用于参数的内存段** — 如何应用内存段 **从模型继承** (默认) | **默认** | 模型内存段

选择软件如何将内存段应用于子系统参数。

- **从模型继承** - 将根模型内存段应用于子系统函数代码。
- **默认** - 不将内存段应用于子系统的系统代码，覆盖任何模型级的设置。
- 将模型的某个内存段应用于子系统。

#### 提示

- 您指定的内存段将应用于生成的代码中对应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅Standard Data Structures (Simulink Coder)。
- 可能的值根据您为模型配置设置的内存段数据包（如果有）而不同。请参阅Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果您没有为模型配置数据包，将只显示**从模型继承**。否则，列表中将包括**默认**以及模型包中的所有内存段。
- 这些选项对于为给定子系统覆盖模型内存段设置很有用。有关如何对原子子系统应用内存段的详细信息，请参阅Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和一个基于 ERT 的系统目标文件。
- 要启用此参数，请将**函数打包**设置为**不可重用函数**，然后选择**具有独立数据的函数**参数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RTWMemSecDataParameters` |
| **值:** | `'Inherit from model'` (默认) | `'Default'` | model memory section in quotes |

## 所属库

Simulink / Ports & Subsystems

## 模块特性

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

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

实际代码生成支持取决于模块实现。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型支持取决于模块实现。

## 版本历史

**在 R2006a 之前推出**

### R2024b: 将信号断点和端口值标签添加到迭代子系统中的迭代序号输出

现在，您可以在迭代子系统的特定迭代上暂停仿真，方法是将信号断点添加到由以下各项产生的信号中：

- While Iterator Subsystem 模块内 While Iterator 模块的迭代序号输出端口
- For Iterator Subsystem 模块内 For Iterator 模块的迭代器值输出端口
- For Each Subsystem 模块内 For Each 模块的分区索引输出端口

在以前的版本中，您可以在这些位置添加断点，但断点不会暂停仿真，并且在模块图中显示为无效。

相同位置的端口值标签现在显示迭代序号。在以前的版本中，这些位置的端口值标签显示 `inaccessible`。

有关示例，请参阅Debug Simulation of Iterator Subsystem。

## 描述

在仿真时间步内重复执行指定迭代次数的子系统

For Iterator Subsystem 模块是一个预先配置的 Subsystem 模块，可以作为一个起点，用于创建在仿真时间步期间重复执行指定的迭代次数的子系统。迭代次数由子系统内部的 For Iterator 模块控制。有关示例，请参阅 `ex_for_iterator_block`。

**注意**

要在模型的仿真停止时间之前中断循环并手动终止仿真，请按 **Ctrl + C**。

当使用简化的初始化模式时，如果您在 For Iterator Subsystem 模块中放置需要经过一段时间才能得到结果的模块（例如 Discrete-Time Integrator 模块），Simulink® 会显示错误。
