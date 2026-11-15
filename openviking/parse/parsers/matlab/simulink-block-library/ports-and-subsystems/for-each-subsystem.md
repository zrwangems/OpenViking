---
type: simulink-block
title: 'For Each Subsystem'
family: ports-and-subsystems
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'foreachsubsystem'
---

# For Each Subsystem

Apply algorithm to individual elements or subarrays of input signals or mask parameters

## 中文

将算法应用于输入信号或封装参数的单个元素或子数组

### 所属库

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

### 描述

For Each Subsystem 模块是一个预先配置的 Subsystem 模块，可以作为一个起点，用于创建在仿真时间步期间对输入信号或封装参数数组的每个元素或子数组都要重复执行的子系统。

For Each Subsystem block icon, displayed alongside contents of for-each subsystem, consisting of a For Each block, an Inport block, and an Outport block.

子系统中的模块组表示应用于原始信号或封装参数数组的单个元素（或子数组）的算法。在子系统内，具有状态的每个模块维护它所处理的每个元素或子数组的单独状态集。因此，此子系统的操作在行为上类似于复制原始输入信号或封装参数数组中每个元素的子系统的内容，然后使用其各自的子系统副本处理每个元素。随着该子系统中的模块集对元素（或子数组）的处理，该子系统串联结果以形成输出信号。

#### 配置子系统

For Each Subsystem 模块包含 For Each 模块，该模块充当子系统的控制模块。指定 For Each 模块的参数，以配置将子系统输入或封装参数分解为元素或子数组，并配置将各个结果串联为输出信号。模块参数**分区维度**和**分区宽度**分别指定对输入信号或封装参数数组进行切片的维度和每个切片的宽度。要对行向量进行分区，请将**分区维度**指定为 `2`。要对列向量进行分区，请将**分区维度**指定为 `1`。使用参数**分区偏移量**指定分区之间的间隙或重叠。指定**迭代次数**以将处理范围限制为部分数据。要了解有关模块参数的更多信息，请参阅 For Each。

**将输入信号分区到子系统**

要为 For Each 子系统中的每次迭代指定要对哪些输入信号分区，请使用 For Each 模块的对话框中的**输入分区**选项卡。在指定要分区的信号时，指定**分区维度**、**分区宽度**和**分区偏移量**参数。

**对子系统的封装参数进行分区**

您可以对 For Each Subsystem 模块的封装参数进行分区。对于在每次迭代中结构相同但参数值不同的系统，分区非常有用。在这种情况下，针对每个参数更改模型来对额外输入参数进行分区非常繁琐。请改为将封装参数添加到 For Each 子系统中。有关详细信息，请参阅创建简单封装。要选择封装参数进行分区，请使用 For Each 模块对话框中的**参数分区**选项卡。有关详细信息，请参阅下文的选择分区参数。

**串联输出**

通过在**输出串联**选项卡中指定**串联维度**来定义沿哪个维度串联结果。

模块为每个子数组生成的结果沿串联维度 1 堆叠。默认情况下，使用维度 1（*y* 轴），这意味着结果垂直堆叠。但是，如果指定的串联维度为 2，结果将沿水平方向（*x* 轴）串联。因此，如果该过程生成行向量，则串联的结果在第一种情况下是矩阵，在第二个种情况下是行向量。有关示例，请参阅在 For Each 模块中指定连接维度。

**选择分区参数**

当选择要分区的输入信号或子系统封装参数时，您必须为每次迭代指定如何将其分解为元素或子数组。为**分区维度**、**分区宽度**和**分区偏移量**参数设置整数值。

作为说明，以如下形式的输入信号矩阵 `A` 为例：

A 3-by-3 matrix A with all nine elements displayed, showing d1 as the vertical dimension and d2 as the horizontal dimension

标签 *d*1 和 *d*2 分别定义维度 1 和 2。如果为分区维度和分区宽度均保留默认设置 `1`，为分区偏移量保留默认设置 `0`，则 Simulink® 会垂直于分区维度 1 以等于分区宽度（一个元素）的宽度进行切片：

A 3-by-3 matrix A, with all nine elements showing, partitioned into rows

矩阵 A 分解为以下三个行向量：

A 3-by-3 matrix A, decomposed into three 3-element row vectors

如果改为将 `2` 指定为分区维度，则 Simulink 将垂直于维度 2 进行切片来形成以下三个列向量：

A 3-by-3 matrix A, decomposed into three 3-element column vectors

除了将**分区维度**设置为 `2` 之外，如果再将**分区宽度**设置为 `2` 并将**分区偏移量**设置为 `-1`，Simulink 会将矩阵处理为两个重叠的 3×2 分区。

A 3-by-3 matrix A, decomposed into two overlapping 3-by-2 matrices

有关示例，请参阅使用 For Each 模块对输入信号进行分区。

默认情况下，处理输入信号或封装参数的所有分区。要处理部分分区，请在**迭代次数**中输入要处理的分区的数量。在上面的矩阵示例中，如果**分区偏移量**设置为 `0`（默认值），并且**迭代次数**设置为 `2`，则仅处理输入矩阵 `A` 的前 2 行或前 2 列。

**注意**

在 Simulink 中，只有信号被视为一维。封装参数是行向量或列向量，具体取决于其方向。要对行向量进行分区，请将分区维度指定为 2（沿列进行）。要对列向量进行分区，请将分区维度指定为 1（沿行进行）。

#### 代码重用支持

对于某些模型，For Each Subsystem 模块可提高 Simulink Coder™ 生成代码的代码重用。假设有一个模型包含两个可重用的 Atomic Subsystem 模块，且对信号的每个元素应用相同的标量算法。如果这些子系统的输入信号维度不同，Simulink Coder 生成的代码中将包含两个不同的函数。您可以将这两个子系统替换为两个相同的 For Each Subsystem 模块，后两者配置为使用相同的算法处理其各自输入的每个元素。在这种情况下，Simulink Coder 生成的代码会包含一个根据输入信号的元素数进行参数化的函数。此函数被调用两次，即对模型中 For Each Subsystem 模块的每个唯一实例分别调用一次。对于其中每种情况，输入信号元素均具有不同的值。

#### 多核执行支持

在快速加速模式下仿真模型时，Simulink 使用多核执行来加快 For Each 子系统的仿真速度。Simulink 自动为每个符合条件的 For Each 子系统探查其在快速加速模式下运行的前两个时间步，以比较并行和串行执行时间。然后，如果在仿真运行的后续时间步中指定 For Each 子系统进行并行多核执行会加快执行速度，则 Simulink 会指定采用这种方式。对于嵌套的 For Each 子系统，多核执行仅适用于顶层子系统。多核执行不适用于包含连续状态或 Function Caller 模块的 For Each 子系统。

要禁止给定 For Each 子系统的多核执行，请将该子系统内 For Each 模块的 `MultithreadedSim` 参数设置为 `'off'`。

```
set_param(ForEachBlockName,'MultithreadedSim','off')
```

请注意，这是子系统中 For Each 模块的参数，而不是 For Each Subsystem 模块本身的参数。要禁止模型中所有 For Each 子系统的多核执行，请将模型的 `MultithreadedSim` 参数设置为 `'off'`。

```
set_param(ModelName,'MultithreadedSim','off')
```

要重新启用多核执行，请将相关的 `MultithreadedSim` 参数设置为其默认值 `'auto'`。

有关示例，请参阅Multithreaded Simulation Using For Each Subsystem。

**注意**

如果以快速加速模式仿真模型或从模型生成代码，并且对 For Each 子系统中的封装参数进行分区，则 For Each Subsystem 中引用分区参数的任何表达式都必须为可调表达式。请参阅Tunable Expression Limitations (Simulink Coder)。

#### S-Function 支持

For Each Subsystem 模块支持 C-MEX S-Function 和 2 级 MATLAB® S-Function，前提是 S-Function 使用以下方法之一支持多个执行实例：

- C-MEX S-Function 必须在 `mdlSetWorkWidths` 方法中声明 `ssSupportsMultipleExecInstances(S, true)`。
- 2 级 MATLAB S-Function 必须在 setup 方法中声明 `block.SupportsMultipleExecInstances = true`。

如果使用这些设定，则：

- 不要使用全局变量或持久变量或在 S-Function 的用户数据内缓存运行时数据，如 DWork 和模块 I/O。
- 在 For Each Subsystem 模块中，对于 S-Function 处理的每个元素，各调用一次 S-Function 执行方法（从 `mdlStart` 直到 `mdlTerminate`）。因此，您必须确保不要在重复调用 `mdlTerminate` 时释放相同的内存。例如，假设某个 C-MEX S-Function 为 `mdlSetWorkWidths` 内的运行时参数分配内存。仅当在 `mdlTerminate` 中时，该内存才需要释放一次。作为一种解决方案，请在首次调用 `mdlTerminate` 后将指针设置为空。

### 端口

#### 输入

#### **In** — 子系统模块的信号输入 标量 | 向量 | 矩阵

Subsystem 模块的信号输入，指定为标量、向量或矩阵。在 Subsystem 模块中放置一个 Inport 模块会为该模块添加一个外部输入端口。端口标签与 Inport 模块的名称相匹配。

使用 Inport 模块可以从局部环境中接收信号。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
#### 输出

#### **Out** — 子系统模块的信号输出 标量 | 向量 | 矩阵

从 Subsystem 模块输出的信号，以标量、向量或矩阵形式返回。在 Subsystem 模块中放置一个 Outport 模块会为该模块添加一个外部输出端口。端口标签与 Outport 模块的名称相匹配。

使用 Outport 模块可以向局部环境发送信号。

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

#### **尽量减少出现代数环** — 消除人为代数环的选项 `off` (默认) | `on`

尝试消除任何包含原子子系统的人为代数环

- `off` - 不尝试消除任何包含原子子系统的人为代数环。
- `on` - 尝试消除任何包含原子子系统的人为代数环。

##### 依赖关系

要启用此参数，请选择**视为原子单元**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `MinAlgLoopOccurrences` |
| **值:** | `'off'` (默认) | `'on'` |

#### 代码生成

设置“代码生成”选项卡上的参数需要具有 Simulink Coder 或 Embedded Coder® 许可证。

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
| **数据类型** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` |
| **直接馈通** | `否` |
| **多维信号** | `是a` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 实际支持的数据类型或功能取决于模块实施。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

实际代码生成支持取决于模块实现。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

当您为 For Each Subsystem 生成 HDL 代码时，代码生成器尝试使用 `for-generate` 循环，该循环遍历输入和输出信号的元素。for-generate 循环可提高可读性，减少代码行数。如果不采用该循环，则对于大型向量信号，可能会产生数百行代码。子系统支持向量和三维矩阵输入信号。请参阅Generate HDL Code for Blocks Inside For Each Subsystem (HDL Coder)。

您可以使用非零分区偏移量来进行 HDL 代码生成。代码生成器支持标量、向量或矩阵作为封装参数值。您可以为 For Each Subsystem 模块内的元素、一维和二维封装参数分区生成 HDL 代码。在 For Each Subsystem 模块中，将封装参数用作 Constant 模块中的**常量值**参数或 Gain 模块中的**增益**参数。

**限制**

- 您不能将 For Each Subsystem 模块用作 DUT。
- 您不能为 HDL 代码生成设置 For Each 模块的 `SpecifiedNumIters` 参数。当 `SpecifiedNumIters` 的值不等于默认值 `-1` 时，HDL 代码生成将返回错误。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| **模块**（默认值） | 为子系统和子系统内的模块生成代码。 |
| **BlackBox** | 生成黑盒接口。生成的 HDL 代码仅包括子系统的输入/输出端口定义。因此，您可以在模型中使用子系统来生成与手动编写的现有 HDL 代码的接口。  子系统的黑盒接口生成类似于没有时钟信号的 Model 模块接口生成。 |
| **无 HDL** | 从生成的代码中删除子系统。您可以在仿真中使用子系统，但在 HDL 代码中将其视为“无操作”。 |

**黑盒接口自定义**

对于 **BlackBox** 架构，您可以自定义端口名称并设置外部组件接口的属性。请参阅Customize Black Box or HDL Cosimulation Interface (HDL Coder)。

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

**复数数据支持**

该模块不支持使用复数数据信号进行 HDL 代码生成。要输入复信号，请将复信号转换为信号数组，然后输入到模块。要了解详细信息，请参阅Generate HDL Code for Blocks Inside For Each Subsystem (HDL Coder)。

**生成具有代数环的模块的 HDL 代码**

要为包含 For Each Subsystem 模块的模型生成 HDL 代码，请执行以下操作：

- 在“配置参数”对话框中，点击**诊断**，并将**代数环**参数设置为**无**或**警告**。
- 打开 For Each Subsytem 模块的模块封装，并选择**尽量减少出现代数环**参数。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型支持取决于模块实现。

### 版本历史记录

**在 R2010a 中推出**

#### R2024b: 将信号断点和端口值标签添加到迭代子系统中的迭代序号输出

现在，您可以在迭代子系统的特定迭代上暂停仿真，方法是将信号断点添加到由以下各项产生的信号中：

- While Iterator Subsystem 模块内 While Iterator 模块的迭代序号输出端口
- For Iterator Subsystem 模块内 For Iterator 模块的迭代器值输出端口
- For Each Subsystem 模块内 For Each 模块的分区索引输出端口

在以前的版本中，您可以在这些位置添加断点，但断点不会暂停仿真，并且在模块图中显示为无效。

相同位置的端口值标签现在显示迭代序号。在以前的版本中，这些位置的端口值标签显示 `inaccessible`。

有关示例，请参阅Debug Simulation of Iterator Subsystem。

## Libraries

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

## Description

The For Each Subsystem block is a Subsystem block preconfigured as a starting point for creating a subsystem
that repeats execution during a simulation time step on each element or subarray of an
input signal or mask parameter array.

For Each Subsystem block icon, displayed alongside contents of for-each subsystem, consisting of a For Each block, an Inport block, and an Outport block.

The set of blocks within the subsystem represents the algorithm applied to a single
element or subarray of the original signal or mask parameter array. Inside the
subsystem, each block that has states maintains separate sets of states for each element
or subarray that it processes. Consequently, the operation of this subsystem is similar
in behavior to copying the contents of the subsystem for each element in the original
input signal or mask parameter array and then processing each element using its
respective copy of the subsystem. As the set of blocks in the subsystem processes the
elements or subarrays, the subsystem concatenates the results to form output
signals.

### Configure the Subsystem

The For Each Subsystem block contains a For Each block that acts as a control
block for the subsystem. Specify the parameters of the For Each block
to configure the decomposition of the subsystem inputs or mask parameters into
elements or subarrays and to configure the concatenation of the individual results
into output signals. The block parameters **Partition Dimension**
and **Partition Width** specify the dimension through which to
slice the input signal or mask parameter array and the width of each slice,
respectively. To partition a row vector, specify the **Partition
Dimension** as `2`. To partition a column vector,
specify the **Partition Dimension** as `1`. Use
the parameter **Partition Offset** to specify a gap or an overlap
between partitions. Specify a **Number of iterations** to limit
processing to a subset of the data. To learn more about the block parameters, see
For Each.

**Partition Input Signals to the Subsystem**

To specify which input signals to partition for each iteration in a for-each
subsystem, use the **Input Partition** tab in the dialog box of the
For Each block. When specifying a signal to be partitioned, specify the
**Partition Dimension**, **Partition Width**, and
**Partition Offset** parameters.

**Partition Mask Parameters of the Subsystem**

You can partition the mask parameters of a For Each Subsystem
block. Partitioning is useful for systems that have identical structures in each iteration
but different parameter values. In this case, changing the model to partition extra input
signals for each parameter is cumbersome. Instead, add a mask parameter to a for-each
subsystem. For more information, see Create a Simple Mask. To select the mask parameter for partitioning, use the
**Parameter Partition** tab of the For Each block dialog
box. For more information, see Select Partition Parameters, below.

**Concatenate Output**

Define the dimension along which to concatenate the results by specifying the
**Concatenation Dimension** in the **Output
Concatenation** tab.

The results generated by the block for each subarray are stacked along the
concatenation dimension. By default, dimension 1 (*y*-axis) is
used, meaning that the results are stacked vertically. However, if you specify a
concatenation dimension of 2, the results concatenate along the horizontal
direction (*x*-axis). Thus, if the process generates row
vectors, then the concatenated result is a matrix in the first case and a row
vector in the second case. For an example, see Specifying the Concatenation Dimension in the For Each Block.

**Select Partition Parameters**

When selecting an input signal or subsystem mask parameter for partitioning,
you must specify how to decompose it into elements or subarrays for each
iteration. Set integer values for the **Partition Dimension**,
**Partition Width**, and **Partition
Offset** parameters.

As an illustration, consider an input signal matrix `A` of
the form:

A 3-by-3 matrix A with all nine elements displayed, showing d1 as the vertical dimension and d2 as the horizontal dimension

The labels *d*1 and
*d*2 define dimensions 1 and 2,
respectively. If you retain the default setting of `1` for both
the partition dimension and the partition width and `0` for the
partition offset, then Simulink® slices perpendicular to partition dimension 1 at a width equal to
the partition width, that is one element:

A 3-by-3 matrix A, with all nine elements showing, partitioned into rows

Matrix A decomposes into these three row vectors:

A 3-by-3 matrix A, decomposed into three 3-element row vectors

If you specify `2` as the partition dimension instead,
Simulink slices perpendicular to dimension 2 to form three column
vectors:

A 3-by-3 matrix A, decomposed into three 3-element column vectors

In addition to setting the **Partition Dimension** to
`2`, if you set the **Partition Width** to
`2` and the **Partition Offset** to
`-1`, Simulink uses two overlapping 3-by-2 partitions for processing.

A 3-by-3 matrix A, decomposed into two overlapping 3-by-2 matrices

For an example, see Partitioning an Input Signal with the For Each Block.

By default, all partitions of the input signal or mask parameter are
processed. To process a subset of the partitions, enter the number of partitions
to process as the **Number of iterations**. In the matrix
examples above, if **Partition Offset** is set to
`0` (the default) and **Number of
iterations** is set to `2`, only the first 2 rows
or columns of the input matrix `A` are processed.

**Note**

Only signals are considered one-dimensional in Simulink. Mask parameters
are row or column vectors, according to their orientation. To partition a
row vector, specify the partition dimension as 2, along the columns. To
partition a column vector, specify the partition dimension as 1, along the
rows.

### Code Reuse Support

For certain models, the For Each Subsystem block improves code
reuse in Simulink
Coder™ generated code. Consider a model containing two reusable Atomic
Subsystem blocks with the same scalar algorithm applied to each element
of the signal. If the input signal dimensions of these subsystems are different,
Simulink
Coder generated code includes two distinct functions. You can replace these
two subsystems with two identical For Each Subsystem blocks that are
configured to process each element of their respective inputs using the same
algorithm. In this case, Simulink
Coder generated code consists of a single function parameterized by the
number of input signal elements. This function is invoked twice, once for each
unique instance of the For Each Subsystem block in the model. For
each of these cases, the input signal elements have different values.

### Multicore Execution Support

When you simulate your model in rapid accelerator mode, Simulink uses multicore execution for faster simulation of for-each subsystems.
Simulink automatically profiles each eligible for-each subsystem the first two time
steps it runs in rapid accelerator mode to compare parallel and serial execution times.
Simulink then designates the for-each subsystem for parallel, multicore execution in
subsequent time steps of the simulation run if doing so would speed up execution time. For
nested for-each subsystems, multicore execution applies only to the top-level subsystem.
Multicore execution does not apply to for-each subsystems containing continuous states or
Function Caller blocks.

To suppress multicore execution for a given for-each subsystem, set the
`MultithreadedSim` parameter of the For Each block within
the subsystem to
`'off'`.

```
set_param(ForEachBlockName,'MultithreadedSim','off')
```

Note that this is a parameter of the For Each block within the
subsystem, not the For Each Subsystem block itself. To suppress multicore
execution for all for-each subsystems in a model, set the
`MultithreadedSim` parameter of the model to
`'off'`.

```
set_param(ModelName,'MultithreadedSim','off')
```

To re-enable multicore execution, set the relevant
`MultithreadedSim` parameter to its default value of
`'auto'`.

For an example, see Multithreaded Simulation Using For Each Subsystem.

**Note**

If you simulate your model in rapid accelerator mode or generate code from your model,
and you partition mask parameters in a for-each subsystem, then any expression inside the
for-each subsystem that references a partitioned parameter must be a tunable expression.
See Tunable Expression Limitations (Simulink Coder).

### S-Function Support

The For Each Subsystem block supports both C-MEX S-functions and
Level-2 MATLAB® S-functions, provided that the S-function supports multiple execution
instances using one of these techniques:

- A C-MEX S-function must declare
  `ssSupportsMultipleExecInstances(S, true)` in the
  `mdlSetWorkWidths` method.
- A Level-2 MATLAB S-function must declare
  `block.SupportsMultipleExecInstances = true` in the
  setup method.

If you use these specifications:

- Do not cache run-time data such as DWork and Block I/O using global or
  persistent variables or within the user data of the S-function.
- In a For Each Subsystem block, every S-function execution
  method from `mdlStart` up to
  `mdlTerminate` is called once for each element
  processed by the S-function. Consequently, you must make sure not to free
  the same memory on repeated calls to `mdlTerminate`. For
  example, consider a C-MEX S-function that allocates memory for a run-time
  parameter within `mdlSetWorkWidths`. The memory only needs
  to be freed once in `mdlTerminate`. As a solution, set the
  pointer to be empty after the first call to
  `mdlTerminate`.

## Ports

### Input

### **In** — Signal input to Subsystem block scalar | vector | matrix

Signal input to a Subsystem block, specified as a
scalar, vector, or matrix. Placing an Inport block in a
Subsystem block adds an external input port to the
block. The port label matches the name of the Inport
block.

Use Inport blocks to receive signals from the local
environment.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Out** — Signal output from Subsystem block scalar | vector | matrix

Signal output from a Subsystem block, returned as a
scalar, vector, or matrix. Placing an Outport block in a
Subsystem block adds an external output port to the
block. The port label matches the name of the Outport
block.

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

### **Minimize algebraic loop occurrences** — Option to eliminate artificial algebraic loops `off` (default) | `on`

Try to eliminate any artificial algebraic loops that include the atomic subsystem

- `off` — Do not try to eliminate any artificial algebraic loops that include the atomic subsystem.
- `on` — Try to eliminate any artificial algebraic loops that include the atomic subsystem.

#### Dependencies

To enable this parameter, select **Treat as atomic unit**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `MinAlgLoopOccurrences` |
| **Values:** | `'off'` (default) | `'on'` |

### Code Generation

Parameters on the Code Generation tab require a Simulink
Coder or Embedded Coder® license.

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
| **Data Types** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `no` |
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

When you generate HDL code for the For Each Subsystem, the code
generator attempts to use a `for-generate` loop that iterates
through elements of the input and output signals. The for-generate loop improves
readability and reduces the number of lines of code, which could otherwise be
hundreds of lines of code for large vector signals. The subsystem supports vector
and 3D matrix input signals. See Generate HDL Code for Blocks Inside For Each Subsystem (HDL Coder).

You can use a nonzero partition offset for HDL code generation. The code generator
supports a scalar, vector, or matrix as mask parameter values. You can generate HDL
code for element, 1D, and 2D partitions of mask parameters inside a For Each
Subsystem block. Inside the For Each Subsystem block, use
the mask parameter as the **Constant value** parameter in Constant blocks or as the
**Gain** parameter in Gain blocks.

**Limitations**

- You cannot use the For Each Subsystem block as the
  DUT.
- You cannot set the `SpecifiedNumIters` parameter of
  the For Each block for HDL
  code generation. HDL code generation returns an error when the value of
  `SpecifiedNumIters` is not equal to the default
  value of `-1`.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `Module` (default) | Generate code for the subsystem and the blocks within the subsystem. |
| `BlackBox` | Generate a black box interface. The generated HDL code includes only the input/output port definitions for the subsystem. Therefore, you can use a subsystem in your model to generate an interface to existing, manually written HDL code.  The black-box interface generation for subsystems is similar to the Model block interface generation without the clock signals. |
| `No HDL` | Remove the subsystem from the generated code. You can use the subsystem in simulation, however, treat it as a “no-op” in the HDL code. |

**Black Box Interface Customization**

For the `BlackBox` architecture, you
can customize port names and set attributes of the external component
interface. See Customize Black Box or HDL Cosimulation Interface (HDL Coder).

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

**Complex Data Support**

The block does not support complex data signals for HDL code generation. To
input complex signals, convert the complex signal to an array of signals, and
then input to the block. To learn more, see Generate HDL Code for Blocks Inside For Each Subsystem (HDL Coder).

**Generate HDL Code with Algebraic Loops**

To generate HDL code for models that contain For Each Subsystem
blocks:

- In the Configuration Parameters dialog box, click
  **Diagnostics**, and set the
  **Algebraic loop** parameter to
  `none` or
  `warning`.
- Open the block mask for the For Each Subsystem block
  and select the **Minimize algebraic loop
  occurrences** parameter.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type support depends on block implementation.

## Version History

**Introduced in R2010a**

### R2024b: Add signal breakpoints and port value labels to iteration number outputs in iterator subsystems

You can now pause a simulation on a particular iteration of an iterator subsystem by adding
signal breakpoints to signals produced by:

- Iteration number output ports of While Iterator blocks inside While Iterator Subsystem blocks
- Iterator value output ports of For Iterator blocks inside For Iterator Subsystem blocks
- Partition index output ports of For Each blocks inside For Each Subsystem blocks

In previous releases, you could add a breakpoint in these locations, but the breakpoints
did not pause the simulation and appeared as invalid in the block diagram.

Port value labels at the same locations now display the iteration number. In previous releases, port value labels at these locations showed `inaccessible`.

For an example, see Debug Simulation of Iterator Subsystem.
