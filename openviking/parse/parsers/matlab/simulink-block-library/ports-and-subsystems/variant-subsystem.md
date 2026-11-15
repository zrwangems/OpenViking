---
type: simulink-block
title: 'Variant Subsystem'
family: ports-and-subsystems
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'variantsubsystem'
---

# Variant Subsystem

Template subsystem containing Subsystem blocks as variant choices

## 中文

包含 Subsystem 模块作为变体选项的模板子系统

### 所属库

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

### 描述

Variant Subsystem 模块允许您在一个单独层次结构中包含组件的多个实现。

例如，假设您要仿真一个表示具有三种可能发动机配置的车辆的模型：2-cylinder gas、4-cylinder gas 和 8-cylinder gas。您可以将每个发动机模型实现为 Variant Subsystem 模块内的单独子系统，然后根据您选择的 Types of Variant Control Modes in Variant Blocks 在子系统之间切换。有关详细信息，请参阅 Introduction to Variant Controls。

**注意**

在仿真期间，Variant Subsystem 模块只有一个实现处于活动状态。

Variant Subsystem 模块内的发动机多个模型

Variant Subsystem 模块是一个预先配置的模板，包含两个或多个模块以用作变体选项。这些选项表示系统的多个实现。在模型执行期间，只有一个子模块处于活动状态。活动子模块称为 *active variant*。

Variant Subsystem 模块内的每个变体选项都与 **Variant control mode** 和 **Variant activation time** 相关联。变体控制模式确定如何选择活动变体。变体激活时间确定激活选项的时间，并决定在生成的代码中是仅包含活动选项还是同时包含活动和非活动选项。

Variant Subsystem 模块可以包含 Subsystem 模块、Model 模块或 Subsystem Reference 模块的混合作为变体选项。仅以 Model 模块作为选项的 Variant Subsystem 模块称为 Variant Model 模块。有关详细信息，请参阅 Implement Variations in Separate Hierarchy Using Variant Subsystems。以 Model 或 Subsystem Reference 模块作为选项，且这些选项只能从外部文件添加或移除而不能在模块内添加或移除的 Variant Subsystem 模块称为 Variant Assembly Subsystem 模块。

除了变体选项之外，您可以在 Variant Subsystem 模块内包含 Inport、控制端口（Enable、Trigger、Reset 和 Function-Call Subsystem）、Outport 或 Connection Port (Simscape) 模块。Variant Subsystem 模块内的模块之间没有绘制的连接。在模型编译期间，软件会自动将活动变体连接到 Variant Subsystem 的 Inport 和 Outport 模块。表示变体选项的模块可以具有与父 Variant Subsystem 模块中的输入和输出端口数量不同的输入和输出端口。有关详细信息，请参阅 Map Input and Output Ports of Variant Choices in Variant Subsystem。

当您加载包含 Variant Subsystem 模块的模型，且该模块的变体选项存储在子系统文件中时，默认情况下，仅加载活动选项以优化模型的加载时间。但是，如果您使用 `find_system`、`get_param` 或 `set_param` 函数以编程方式初始化模型，则可能会加载非活动选项。

使用 Variant Subsystem 模块允许您：

- 混合使用 Subsystem、Model 和 Subsystem Reference 模块作为变体选项。
- 对不具有相似接口的组件建模。您可以在 Variant Subsystem 内为多个变体选项设置不同数量的 inport 和 outport。但是，必须满足 Map Input and Output Ports of Variant Choices in Variant Subsystem 中列出的条件。
- 建立层次化框图，其中 Variant Subsystem 模块位于一层，变体选项位于另一层。
- 将功能相关的模块保持在一起。
- 降低模型的复杂度。
- 在模型编译期间，软件会根据您选择的变体激活时间消除整个模型中的非活动模块。

模块图标上变体徽章的颜色和图标会根据模块上设置的 **Variant activation time**、**Variant control mode** 和 **Propagate conditions outside of variant subsystem** 参数的值而变化。有关详细信息，请参阅 Variant Badges。

#### Open the Block

您可以从 Simulink® 界面或以编程方式打开 Variant Subsystem 模块。根据您的需求，这些方法使您能够访问活动变体选项或 Variant Subsystem 模块的整个变体层。

**从 Simulink 界面打开**

在 Simulink 界面中使用以下任一操作打开 Variant Subsystem 模块。

| 键盘和鼠标操作 | 结果 |
| --- | --- |
| 双击 | 在新选项卡中打开模块内的活动变体选项  **注意**  如果变体选项是 Model 模块且其引用的模型未加载，则双击该模块会打开包含变体选项的变体层，而不是打开活动变体选项的底层。 |
| 按住 **Ctrl** 并双击 | 在新选项卡中打开模块，显示变体层 |
| 按住 **Shift** 并双击 | 在新窗口中打开模块，显示变体层 |
| 右键单击，选择 **Open** > **Open in New Tab** | 在当前窗口中打开模块，显示变体层 |
| 右键单击，选择 **Open** > **Open in New Window** | 在新窗口中打开模块，显示变体层 |
| 右键单击变体徽章，选择 **Open** >**(active variant)** | 在新选项卡中打开活动变体选项 |
| 右键单击变体徽章，选择 **Open** > **variant control (variant choice name)**，其中 *`variant control`* 是指由 *variant choice name* 指定的变体选项的变体控制 `expression`、`label` 或 `(sim)` 或 `(codegen)` | 在新选项卡中打开选定的变体选项 |

**以编程方式打开**

使用以下任一命令打开 Variant Subsystem 模块，其中 *`variantSubsystemBlockName`* 是模块的名称：

- `open_system("variantSubsystemBlockName")` 命令 — 打开 Variant Subsystem 模块并查看其变体层。
- `open_system("variantSubsystemBlockName","ActiveChoice")` — 打开 Variant Subsystem 模块内的活动变体选项。

有关使用 `open_system` 命令打开 Variant Subsystem 模块的其他选项（例如在新选项卡或窗口中打开）的信息，请参阅 `open_system`。

### 端口

#### Input

#### **In\_1** — 对应于 variant subsystem 中根级 Inport 模块的输入端口，接受与 Inport 模块相同的数据类型

Variant Subsystem 中包含的每个 Subsystem、Model 或 Subsystem Reference 模块表示一个变体选项。变体选项可以在其输入处包含 Inport、控制端口（Enable、Trigger、Reset 和 Function-Call Subsystem）或 Connection Port (Simscape) 模块。变体选项的输入端口数量可以与父 Variant Subsystem 模块中的输入端口数量不同。但是，必须满足 Map Input and Output Ports of Variant Choices in Variant Subsystem 中描述的条件。

#### Output

#### **Out\_1** — 对应于 variant subsystem 中包含的根级 Outport 模块的输出端口，接受与 Outport 模块相同的数据类型

Variant Subsystem 中包含的每个 Subsystem、Model 或 Subsystem Reference 模块表示一个变体选项。变体选项可以在其输出处包含 Outport 或 Connection Port (Simscape) 模块。变体选项的输出端口数量可以与父 Variant Subsystem 模块中的输出端口数量不同。但是，必须满足 Map Input and Output Ports of Variant Choices in Variant Subsystem 中描述的条件。

Variant Subsystem 模块的未连接输出端口（非活动输出端口）输出 ground 值。要输出 ground 以外的值，请选择 Outport 模块的 **Specify output when source is unconnected** 参数并指定一个值。

### 参数

要访问这些参数，请右键单击模块图标上的变体徽章，然后选择 **Block Parameters**。有关详细信息，请参阅 Variant Badges。

#### **Variant control mode** — 变体控制模式 `expression` (默认) | `label` | `sim codegen switching`

确定活动变体选项的变体控制可以是以下任一类型。

- `expression` — 软件根据变体条件的求值结果选择活动变体。当条件表达式求值为 `true` 时，对应的变体选项变为活动。当条件表达式求值为 `false` 时，对应的变体选项变为非活动。请参阅 Switch Between Choices Using Condition Expressions in Variant Blocks。
- `label` — 软件根据变体名称选择活动变体。变体控制是字符串，不需要您在任何工作区中创建任何变量。请参阅 Switch Between Choices Using Labels in Variant Blocks。
- `sim codegen switching` — 在不创建任何工作区变量的情况下，自动在仿真和代码生成工作流之间切换变体。当您仿真模型时，软件自动选择 `sim` 分支作为活动选项。类似地，当您执行 software-in-the-loop (SIL) 或 processor-In-Loop (PIL) 仿真、生成代码或使用 external mode 时，软件自动选择 `codegen` 分支。请参阅 Switch Between Choices for Simulation and Code Generation Workflows Without Using Control Variables in Variant Blocks。

有关变体控制模式的详细信息，请参阅 Introduction to Variant Controls。有关不同变体控制模式类型之间的比较，请参阅 Compare Different Types of Variant Control Modes in Variant Blocks。

#### Dependencies

不同变体激活时间的可用性取决于您指定的 **Variant control mode** 类型。**Variant activation time** 参数确定软件设置活动选项的时间。该参数还确定在生成的代码中包含哪些可变性。此表说明了每种变体控制模式支持的变体激活时间。

| **Variant activation time** | | | | |  |
| --- | --- | --- | --- | --- | --- |
| **Variant control mode** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` | `runtime` (仅 Variant Subsystem 模块) |
| `expression` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `label` | ✓ | x | x | x | x |
| `sim codegen switching` | ✓ | ✓ | x | x | x |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantControlMode` |
| **类型：** character vector |
| **值：** `'expression'` | `'label'` | `'sim codegen switching'` |
| **默认值：** `'expression'` |

#### **Variant activation time** — 软件选择活动变体选项的时间 `update diagram` (默认) | `update diagram analyze all choices` | `code compile` | `startup` | `runtime` | `inherit from Simulink.VariantControl`

此参数确定在仿真和代码生成工作流中包含哪些可变性。有关详细信息，请参阅 Activate Variant During Different Stages of Simulation and Code Generation Workflow。

- `update diagram` — 当您执行模型时，仿真和代码生成工作流中仅包含活动选项。生成的代码仅包含活动选项。
- `update diagram analyze all choices` — 当您执行模型时，会针对整个模型的一致性分析活动和非活动选项。但是，仿真和代码生成工作流中仅包含活动选项。生成的代码仅包含活动选项。
- `code compile` — 当您执行模型时，会针对整个模型的一致性分析活动和非活动选项，并且仿真和代码生成工作流中包含所有选项。生成的代码包含活动和非活动选项，二者由预处理条件 `#if` 和 `#elif` 包围。但是，从生成的代码构建的可执行文件仅包含活动选项。
- `startup` — 当您执行模型时，会针对整个模型的一致性分析活动和非活动选项，并且仿真和代码生成工作流中包含所有选项。使用此选项，您可以使用 fast restart 提高迭代仿真的速度。有关详细信息，请参阅 Run Iterative Simulations Without Recompiling Model for Variant Systems Using Fast Restart。从模型生成的代码包含活动和非活动选项，二者由常规 `if` 条件包围。从生成的代码构建的可执行文件也包含活动和非活动选项。
- `runtime` — 当您执行模型时，可以使用 Parameter Writer 模块在仿真期间或生成代码执行期间切换活动变体。将 Parameter Writer 模块放在条件执行子系统内，或放在 Initialize Function 模块、Reinitialize Function 模块或 Reset Function 模块中。有关这些模块的详细信息，请参阅 Event Functions。您可以使用 Parameter Writer 模块写入模块参数、模型工作区变量和基础工作区变量。`runtime` 激活时间不支持多个变体控制变量。Parameter Writer 模块支持的所有建模模式对于运行时激活都有效。有关详细信息，请参阅 Common Uses of Parameter Writer Block。

  当您将 Variant Subsystem 模块的 **Variant activation time** 参数设置为 `runtime` 时，非活动变体选项的颜色不会淡化。在这种情况下，Simulink Editor 的 **Debug** 选项卡上 **Information Overlays** 菜单中 **Variant Fading** 选项的设置将被忽略。
- `inherit from Simulink.VariantControl` — 当您执行模型时，模块从其类型为 `Simulink.VariantControl` 的变体控制变量继承激活时间。如果变体模块具有多个类型为 `Simulink.VariantControl` 的变体控制变量，则所有这些变量必须具有相同的激活时间。

下表根据条件代码、变体切换、状态处理和 fast restart 支持比较不同的变体激活时间。

|  | `update diagram` or `update diagram analyze all choices` | `code compile` | `startup` | `runtime` |
| --- | --- | --- | --- | --- |
| **生成的条件代码** | 非活动条件代码不可用。 | 条件代码存在于预处理器宏内。编译生成的代码时，非活动选项代码会被消除。 | 条件代码作为 `if-elseif-else` 语句的一部分生成。在执行期间不能修改变体控制变量的值。 | 条件代码作为 `if-elseif-else` 语句的一部分生成。在执行期间可以修改变体控制变量的值。 |
| **仿真或代码执行期间的变体切换** | 不支持。 | 不支持。 | 在 startup 时支持（在仿真开始 *t* = 0 之前）。 | 支持。通过使用 Parameter Writer 模块更改变体控制变量来切换活动变体。 |
| **显式设置状态的 held 或 reset 选项** | 不支持。非活动模块的状态会被重置。 | 不支持。非活动模块的状态会被重置 | 在仿真期间不能更改状态。在生成的代码中，如果您尝试更改变体，状态将处于 held 状态。 | 默认情况下状态处于 held 状态。通过 State Writer 模块显式重置状态。使用 State Reader 模块读取带状态的模块，并使用 State Writer 模块将其传输到另一个选项。 |
| **可执行文件大小** | 较小。不会为非活动变体生成代码。 | 较小。非活动变体代码在编译期间被移除。 | 相对较大。活动和非活动变体代码都可用于 startup 切换。 | 相对较大。活动和非活动变体代码都可用于运行期切换。 |
| **Fast restart 支持** | 不支持。 | 不支持。 | 支持。 | 支持。 |

#### Dependencies

- 不同变体激活时间的可用性取决于您指定的变体控制模式类型。**Variant activation time** 参数确定软件何时设置活动选项。该参数还确定在生成的代码中包含哪些可变性。此表说明了每种变体控制模式支持的变体激活时间。

  | **Variant activation time** | | | | |  |
  | --- | --- | --- | --- | --- | --- |
  | **Variant control mode** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` | `runtime` |
  | `expression` | ✓ | ✓ | ✓ | ✓ | ✓ |
  | `label` | ✓ | x | x | x | x |
  | `sim codegen switching` | ✓ | ✓ | x | x | x |
- 要使用 `runtime` 激活时间启用 Variant Subsystem 模块活动变体选项的切换，您必须使用 Parameter Writer 模块。根据变体控制变量的位置设置 Parameter Writer 模块的 **Destination** 参数，并选择 **Validate parameter**：

  - `Block parameter` — 控制变量是子系统中的 mask 参数。
  - `Model workspace variable` — 控制变量位于模型工作区中。
  - `Base workspace variable` — 控制变量位于基础工作区或数据字典中。

  例如，您可以在子系统中创建 mask 参数 `V`，并在变体控制的变体条件表达式中使用它。Parameter Writer 模块会写入变体控制条件中 `V` 的值。

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantActivationTime` |
| **类型：** character vector |
| **值：** `'update diagram'` | `'update diagram analyze all choices'` | `'code compile'` | `'startup'`| `'runtime'` |
| **默认值：** `'update diagram'` |

#### **Variant control variable** — 用于确定活动变体选项的变量 `Simulink.VariantControl` 对象 | 标量变量 | `Simulink.Parameter` 对象 | `struct`

当您指定 Types of Variant Control Variables (Operands) in Variant Blocks 中列出的类型的变量时，软件会为 Variant Assembly Subsystem 模块的变体选项生成变体控制表达式。您在此处指定的 **Variant control variable** 位于左侧，**Variant enumeration choice** 的成员位于生成表达式的右侧。两侧通过 `==` 关联。

变体控制变量充当切换活动变体选项的开关。您为变体控制变量指定一个值并运行仿真。在仿真期间，软件对变体控制表达式求值以确定活动变体选项。当表达式求值为 `true` 时，对应的变体选项被设置为活动。要更改活动变体，请更改变体控制变量的值，使对应的变体控制表达式求值为 `true` 并变为活动。

#### Dependencies

此参数仅在 Variant Assembly Subsystem 模块中可用。要启用此参数，请将 **Variant control mode** 设置为 `expression`。

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantControlVariable` |
| **类型：** character vector |
| **值：** `Simulink.VariantControl` object, scalar variable, `Simulink.Parameter` object, `struct` |
| **默认值：** `''` |

#### **Variant choices enumeration** — 用于添加变体选项的枚举类，其成员为模型或子系统文件名

要将 Model 或 Subsystem Reference 模块作为变体选项添加到 Variant Assembly Subsystem 模块，请指定一个枚举类名称，其中包含相应的模型或子系统文件名作为其成员。然后，您可以使用 **Variant choices** 表中的 Refresh 按钮验证该枚举类。验证成功后，枚举类的成员将作为变体选项添加到 Variant Assembly Subsystem 模块。每个选项都有一个变体控制表达式，其左侧为 **Variant control variable**，右侧为您在此处指定的 **Variant choices enumeration** 的成员。表达式的两侧通过 `==` 关联。新添加的变体选项及其对应的控制表达式将显示在 **Variant choices** 表中。

要从 Variant Assembly Subsystem 模块中移除变体选项，请从您在此处指定的枚举类中移除相应成员。您不能从 Variant Assembly Subsystem 模块内部管理变体选项。

您指定的枚举类必须位于当前 MATLAB® 会话的搜索路径上。有关如何将文件或文件夹添加到搜索路径的信息，请参阅 `addpath`。

有关如何使用 **Variant choices enumeration** 参数添加选项的详细信息，请参阅 Add or Remove Variant Choices of Variant Assembly Subsystem Blocks Using External Files。

#### Dependencies

此参数仅在 Variant Assembly Subsystem 模块中可用。要启用此参数，请将 **Variant control mode** 设置为 `expression`。

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantChoicesEnumeration` |
| **类型：** character vector |
| **值：** 使用 `classdef` 或 `Simulink.defineIntEnumType` 定义的枚举类 |
| **默认值：** `''` |

#### **Variant choices specifier** — 用于添加变体选项的 MATLAB 表达式，该表达式求值为模型或子系统文件名的一维 cell 数组，或匹配模型或子系统文件名的文件名模式，或字符串数组

要将 Model 或 Subsystem Reference 模块作为变体选项添加到 Variant Assembly Subsystem 模块，请指定相应的模型或子系统文件名。文件名必须指定为在求值时返回字符向量一维 cell 数组的 MATLAB 表达式或字符串数组。然后，您可以使用 **Variant choices** 表中的 Refresh 按钮验证该表达式。验证成功后，与指定文件对应的模块将作为变体选项添加到 Variant Assembly Subsystem 模块。对于每个选项，会生成一个变体控制标签。变体控制标签的名称与选项名称相同。新添加的变体选项及其对应的控制标签将显示在 **Variant choices** 表中。

要从 Variant Assembly Subsystem 模块中移除变体选项，请修改此参数中指定的表达式。您不能从 Variant Assembly Subsystem 模块内部管理其变体选项。

您指定的 MATLAB 表达式必须包含以下任一项：

- 位于当前 MATLAB 会话搜索路径上的模型或子系统文件名。例如，如果您指定 `{'model1.slx', 'subsystemRef1.slx'}` 作为 specifier，则与 `model1.slx` 和 `subsystemRef1.slx` 文件对应的模块将作为 Variant Assembly Subsystem 模块的变体选项添加。
- 匹配 MATLAB 路径上模型或子系统文件名的文件名模式。模式中的路径可以是绝对路径，也可以是相对于包含 Variant Assembly Subsystem 模块的模型的父文件夹的路径。例如，如果您指定 `{'folder_1/*.slx', 'folder_2/*.slx'}` 作为 specifier，软件会将字符向量 `folder_1/*` 和 `folder2/*` 传递给 `dir` 函数。然后，该函数返回位于 `folder1` 和 `folder2` 文件夹内的模型和子系统文件。与返回文件对应的模块将作为 Variant Assembly Subsystem 模块的变体选项添加。

有关如何将文件或文件夹添加到搜索路径的信息，请参阅 `addpath`。

有关如何在 **Variant choices specifier** 参数中指定选项的详细信息，请参阅 Add or Remove Variant Choices of Variant Assembly Subsystem Blocks Using External Files。

#### Dependencies

此参数仅在 Variant Assembly Subsystem 模块中可用。要启用此参数，请将 **Variant control mode** 设置为 `label`。

#### Programmatic Use

|  |
| --- |
| **Parameter:** `VariantChoicesSpecifier` |
| **类型：** character vector |
| **值：** Any MATLAB expression that evaluates to a one-dimensional cell array of filenames or filename patterns. |
| **默认值：** `''` |

#### **Variant choices** — 变体选项、变体控制和条件的表 空表（默认）

该表为 variant subsystem 中包含的每个变体选项提供一行。如果没有变体选项，则该表为空。

您可以使用 **Variant choices** 表左侧的按钮修改表中的元素。

| 要... | 单击... |
| --- | --- |
| **Create and add a new subsystem choice**：创建一个新的 Subsystem 模块作为变体选项，并在表中为新选项添加条目。 | Create and add a new subsystem choice 按钮 |
| **Create and add a new model variant choice**：创建一个新的 Model 模块作为变体选项，并在表中为新选项添加条目。 | Create and add a new model variant choice 按钮 |
| **Delete selected variant choices**：永久删除变体选项。 | Delete selected variant choices 按钮 |
| **Create/Edit selected variant object**：在全局工作区中创建或编辑 `Simulink.VariantExpression` 对象，并使用 `Simulink.VariantExpression` 对象参数对话框指定变体条件。  **注意**  对于使用基础工作区的模型，此操作会在基础工作区中创建 `Simulink.VariantExpression` 对象，并且该对象仅在当前 MATLAB 会话中可用。要永久存储数据，请将对象保存到 MAT 文件或 MATLAB 脚本中。 | Create or Edit selected variant object 按钮 |
| **Open selected variant choice block**：为所选行打开 Subsystem 模块。 | Open selected variant choice block 按钮 |
| **Refresh dialog information from Variant Subsystem contents**：根据全局工作区中的变体选项和变体控制值更新 **Variant choices** 表。 | Refresh dialog information from Variant Subsystem contents 按钮 |

#### Dependencies

Variant Assembly Subsystem 模块仅允许您使用本节中的按钮打开选定的变体选项并刷新变体选项列表。要向 Variant Assembly Subsystem 模块添加新的变体选项，请参阅 Add or Remove Variant Choices of Variant Assembly Subsystem Blocks Using External Files。

#### **Name (read-only)** — Variant 选项名称 只读：`Subsystem` 和 `Subsystem1`（默认） | Variant Subsystem 中包含的选项名称

此参数为只读。

此参数显示选项的名称。每个选项都有一个变体控制，其形式为标签、表达式或开关。对于处于 `label` 模式的 Variant Assembly Subsystem，没有单独的变体控制可用。选项的名称用作变体控制以设置活动选项。

#### **Variant control label** — `label` 模式下选项的名称 `true` 或 `false`（默认） | string

选项的名称，指定为字符串。

#### Dependencies

要启用此参数，请将 **Variant control mode** 设置为 `label`。

#### Programmatic Use

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `VariantControl` |
| **Values:** | 与变体选项关联的变体控制 |
| **Data Types:** | `char` |

**示例：** `set_param(gcb, 'VariantControl', 'V == 3')`，其中 `gcb` 是 Variant Subsystem 模块的变体选项。

**示例：** `get_param(gcb, 'VariantControl')`，其中 `gcb` 是 Variant Subsystem 模块的变体选项。

#### **Variant control switch** — 用于仿真和代码生成工作流的变体选项 `(sim)` | `(codegen)`

指定 `(sim)` 以在仿真期间激活对应的变体选项。指定 `(codegen)` 以在执行代码生成工作流（例如 SIL、PIL、external mode 等）时激活对应的变体选项。

#### Dependencies

要启用此参数，请将 **Variant control mode** 设置为 `sim codegen switching`。

#### Programmatic Use

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `VariantControl` |
| **Values:** | 与变体选项关联的变体控制 |
| **Data Types:** | `char` |

**示例：** `set_param(gcb, 'VariantControl', '(sim)')`，其中 `gcb` 是 Variant Subsystem 模块的变体选项。

**示例：** `get_param(gcb, 'VariantControl')`，其中 `gcb` 是 Variant Subsystem 模块的变体选项。

#### **Variant control expression** — 确定活动选项的条件表达式 `true` 或 `false`（默认） | boolean 条件表达式 | 表示 boolean 条件表达式的 `Simulink.VariantExpression` 对象 | `(default)`

指定条件表达式以确定活动选项。当条件表达式求值为 `true` 时，软件激活对应的变体选项。当条件表达式求值为 `false` 时，软件停用对应的变体选项。

变体控制可以是：

- 用于快速原型设计的 boolean 条件表达式。例如 `A == 1`、`A ~= B`、`A && B == 1` 等。
- 包含条件表达式以复用条件的 `Simulink.VariantExpression` 对象。请参阅 Simulink.VariantExpression Objects for Variant Condition Reuse of Variant Blocks。
- 如果没有任何选项求值为 `true`，则为 Default Variant Choice。

这里，`A` 和 `B` 是称为 *variant control variables* 的操作数。`==`、`~=` 和 `&&` 是条件表达式中的运算符。条件表达式可以包含一个或多个此类变体控制变量和运算符。有关变体控制变量支持的类型和存储位置的信息，请参阅 Types of Variant Control Variables (Operands) in Variant Blocks 和 Storage Locations for Variant Control Variables (Operands) in Variant Blocks。有关运算符的信息，请参阅 Types of Operators in Variant Blocks for Different Activation Times。

有关详细信息，请参阅 Switch Between Choices Using Condition Expressions in Variant Blocks。

在 Variant Assembly Subsystem 模块中，此参数是自动生成的 boolean 表达式列表，左侧为 **Variant control variable**，右侧为 **Variant enumeration choice** 的成员。表达式的两侧通过 `==` 连接。此参数为只读。

#### Programmatic Use

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

Variant Subsystem 模块：

|  |  |
| --- | --- |
| **Parameter:** | `VariantControl` |
| **Values:** | 与变体选项关联的变体控制 |
| **Data Types:** | `char` |

**示例：** `set_param(gcb, 'VariantControl', 'V == 3')`，其中 `gcb` 是 Variant Subsystem 模块的变体选项。

**示例：** `get_param(gcb, 'VariantControl')`，其中 `gcb` 是 Variant Subsystem 模块的变体选项。

Variant Source 和 Variant Sink 模块：

|  |  |
| --- | --- |
| **Parameter:** | `VariantControls` |
| **Values:** | 与变体选项关联的变体控制 |
| **Data Types:** | `char` |

**示例：** `set_param(gcb, 'VariantControls', {'A == 1','A == 2'})`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

**示例：** `get_param(gcb, 'VariantControls')`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

#### **Condition (read-only)** — `Simulink.VariantExpression` 对象中的条件表达式 只读：`N/A`（默认）

此参数为只读。

此参数显示指定为 `Simulink.VariantExpression` 对象的条件表达式。要更改或编辑条件表达式，请使用在工作区中双击该对象时出现的 `Simulink.VariantExpression` 参数对话框。

**注意**

您在类型为 `Simulink.VariantExpression` 的条件表达式中指定的操作数必须在基础工作区或数据字典中定义。不支持指定在 mask 或模型工作区中定义的操作数。

#### **Label mode active choice** — `label` 模式下活动选项的名称 `true (Subsystem)`（默认） | `false (Subsystem1)`

此列表包含所有变体选项的标签。要设置活动选项，请从列表中选择一个标签。对应的选项将变为活动。或者，要在 label 模式下更改活动选项，您可以遵循 Set Active Choices Using Variant Control Labels 中描述的方法。

#### Dependencies

要启用此参数，请将 **Variant control mode** 设置为 `label`。

#### Programmatic Use

|  |
| --- |
| **Parameter:** `LabelModeActiveChoice` |
| **类型：** character vector |
| **值：** 如果未指定 label mode active choice，则该值为空。如果指定了 label mode active choice，则该值为活动选项的变体控制标签。 |
| **默认值：** `''` |

#### **Built-in empty choice** — 如果没有活动变体选项则输出零 `off`（默认） | `on`

- `off` — 当没有活动变体选项时，Simulink 生成错误。
- `on` — 当您选择此选项时，Simulink 将一个不可修改的变体选项条目添加到 **Variant choices** 表中，并将其变体控制设置为 `(default)`。此条目不会在 Variant Subsystem 模块中显示为可见的变体选项。在仿真期间，如果没有活动变体选项，Simulink 会断开 Variant Subsystem 模块的变体选项，从而将变体区域从模型中完全移除。子系统的非活动 outport 输出零。要输出零以外的值，请选择 Outport 模块的 **Specify output when source is unconnected** 参数并指定您选择的值。

有关详细信息，请参阅 Manage Variant Components to Pass Specified Values from Inactive Variant Subsystems with No Active Choice (Simulink Coder)。

#### Dependencies

仅当 Variant Subsystem 中没有 `default` 变体选项，并且您将 **Variant control mode** 设置为 `expression` 时，此参数才可用。

#### Programmatic Use

|  |
| --- |
| **Parameter:** `EmptyChoice` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

#### **Built-in passthrough choice** — 如果没有活动变体选项，则将输入端口值分配给输出端口 `off`（默认） | `on`

- `off` — 当没有活动变体选项时，Simulink 生成错误。
- `on` — 当您选择此选项时，Simulink 将一个不可修改的变体选项条目添加到 **Variant choices** 表中，并将其变体控制设置为 `(default)`。此条目不会在 Variant Subsystem 模块中显示为可见的变体选项。在仿真期间，如果没有活动变体选项，Simulink 会绕过 Variant Subsystem 模块的变体选项。仅输入和输出端口保持活动，并且输入端口将值直接传递到输出端口。

  要在没有活动选项时将值从输入端口映射到输出端口，Variant Subsystem 模块必须具有：

  - 仅有数据端口，没有其他类型的输入和输出端口
  - 数据输入和数据输出端口的数量相等
  - 输入和输出端口与变体选项的端口完全匹配

有关详细信息，请参阅 Manage Variant Components to Pass Specified Values from Inactive Variant Subsystems with No Active Choice (Simulink Coder)。

#### Dependencies

仅当 Variant Subsystem 中没有 `default` 变体选项，并且您将 **Variant control mode** 设置为 `expression` 时，此参数才可用。

#### Programmatic Use

|  |
| --- |
| **Parameter:** `PassThrough` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

#### **Propagate conditions outside of variant subsystem** — 选择是否必须将底层模块的活动和非活动状态通知 variant subsystem 外部的组件的选项 `off`（默认） | `on`

当您选择 **Propagate conditions outside of variant subsystem** 参数时，软件会将底层模块的变体条件传播到 Variant Subsystem 容器模块，以便该子系统可以使其接口适应底层模块的状态。映射到活动选项上的端口的端口变为活动。未映射到非活动选项上的端口的端口变为非活动。选择此选项可确保 Variant Subsystem 外部的组件知道 Variant Subsystem 模块内模块的活动和非活动状态。有关详细信息，请参阅 Propagate Variant Conditions to Define Variant Regions Outside Variant Subsystems to Promote Consistency and Reduce Errors 和 Propagate Variant Conditions to Control Execution of Conditional Subsystems

如果 Variant Subsystem 模块内的所有变体选项具有相同的接口，则变体条件不会传播到 Variant Subsystem 模块外部。

#### Programmatic Use

|  |
| --- |
| **Parameter:** `PropagateVariantConditions` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

#### **Allow flexible interface** — 选择使 variant subsystem 接口灵活的选项 `on`（默认） | `off`

指定是否使 variant subsystem 的接口灵活。

- `on` — 使用其输入和输出端口数量与 Variant Subsystem 模块的输入和输出端口数量不同的变体选项进行仿真。
- `off` — 当您使用此选项进行仿真时，如果接口不一致，软件将生成带有修复操作的错误，以使变体选项的端口与 Variant Subsystem 模块匹配。

#### Programmatic Use

|  |
| --- |
| **Parameter:** `AllowFlexibleInterface` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'on'` |

### 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `yesa` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a 实际数据类型或能力支持取决于模块实现。 | |

### 扩展功能

#### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

实际数据类型或能力支持取决于模块实现。

#### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。实际数据类型或能力支持取决于模块实现。

**HDL 架构**

| 架构 | 说明 |
| --- | --- |
| `Module`（默认） | 为子系统及子系统内的模块生成代码。HDL Coder 为所有变体选项生成代码。 |
| `BlackBox` | 生成黑盒接口。也就是说，生成的 HDL 代码仅包含子系统的输入/输出端口定义。这样，您就可以使用模型中的子系统为现有手写 HDL 代码生成接口。  为子系统生成的黑盒接口类似于为 Model 模块生成的接口，但不生成时钟信号。 |
| `No HDL` | 从生成的代码中移除子系统。您可以在仿真中使用该子系统，但在 HDL 代码中将其视为“no-op”。 |

**黑盒接口自定义**

对于 `BlackBox` 架构，您可以自定义端口名称并设置外部组件接口的属性。请参阅 Customize Black Box or HDL Cosimulation Interface (HDL Coder)。

**HDL 模块属性**

| General | |
| --- | --- |
| **AdaptivePipelining** | 基于综合工具、目标频率和乘法器字长自动插入流水线。默认值为 `inherit`。另请参阅 AdaptivePipelining (HDL Coder)。 |
| **BalanceDelays** | 检测沿一条路径引入的新延迟，并在其他路径上插入匹配的延迟。默认值为 `inherit`。另请参阅 BalanceDelays (HDL Coder)。 |
| **ClockRatePipelining** | 以更快的时钟速率而不是较慢的数据速率插入流水线寄存器。默认值为 `inherit`。另请参阅 ClockRatePipelining (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分布或寄存器重定时。默认值为 `inherit`。另请参阅 DistributedPipelining (HDL Coder)。 |
| **DSPStyle** | 用于乘法器映射的综合属性。默认值为 `none`。另请参阅 DSPStyle (HDL Coder)。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中移除子系统层次结构。默认值为 `inherit`。另请参阅 FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的功能等效资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |
| **StreamingFactor** | 经时间复用转换为串行标量数据路径的并行数据路径（或向量）数量。默认值为 0，表示实现完全并行的数据路径。另请参阅 Streaming (HDL Coder)。 |

**目标规范**

此模块不能作为 DUT，因此 **Target Specification** 选项卡中的模块属性设置将被忽略。

**限制**

- Variant Subsystem 不能作为 design-under-test (DUT)。
- **Variant activation time** 参数必须设置为 `update diagram`、`update diagram analyze all choices` 或 `startup`。
- 对于 Variant Subsystem 的 Outport 模块，**Specify output when source is unconnected** 参数必须禁用。

#### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

实际数据类型或能力支持取决于模块实现。

### 版本历史

**在 R2010b 中引入**

#### R2025a：通过抑制非活动变体选项和注释模块的回调来减少开销和不相关诊断消息

对于具有 `update diagram` 激活时间的 Variant Subsystem 模块中的非活动变体选项以及注释模块，回调 `LoadFcn`、`ContinueFcn`、`InitFcn`、`ModelCloseFcn`、`PauseFcn`、`PostSaveFcn`、`PreSaveFcn`、`StartFcn` 和 `StopFcn` 不会执行。此抑制可减少计算开销，并防止不影响当前模型迭代的模块产生不必要的诊断消息。但是，对于注释的或非活动的 Model 模块或 Subsystem Reference 模块内的模型或子系统文件中的模块，不会抑制这些回调。此外，mask 初始化和 mask 参数回调不会被抑制。有关适用回调的列表，请参阅 Author Mask Initialization and Callbacks 和 Mask Parameters。

#### R2025a：在没有变体选项时输出零的参数已从 **Allow zero active variant controls** 重命名

**Allow zero active variant controls** 参数现在已重命名为 **Built-in empty choice**。此新参数保留了以前的功能：移除变体组件，并在没有活动变体选项时输出零。

#### R2025a：在没有变体选项时将输入值分配给输出端口

使用 **Built-in passthrough choice** 参数绕过变体区域，并在没有活动变体选项时将输入值分配给输出端口。

#### R2024b：`runtime` 激活时间：在仿真或代码生成期间更改活动选项

从 R2024b 开始，在 Variant Subsystem 模块中使用 `runtime` 变体激活时间，通过 Parameter Writer 模块在仿真或代码生成期间更改活动变体。您可以对所有场景建模，其中 Parameter Writer 模块可以写入全局工作区、mask 工作区或模型工作区中的变体控制变量。

#### R2024a：自动端口同步

Simulink 提供选项来添加缺失端口并删除 Variant Subsystem 和 Variant Assembly Subsystem 模块中未使用的端口，以匹配底层变体选项的端口。在仿真期间，如果 Simulink 遇到 Variant Subsystem 或 Variant Assembly Subsystem 模块与其变体选项之间的端口不匹配，则生成的错误消息会提供添加缺失端口和删除未使用端口的选项来解决该问题。

#### R2024a：使用自适应速率模型模块作为选项

您可以在 Variant Subsystem 模块中使用自适应速率模型模块作为变体选项。当您将自适应速率模型添加为变体选项时，variant subsystem 中的 inport 会与相应速率模型的端口名称匹配。

#### R2024a：访问活动变体选项的 mask

您可以直接访问 Variant Subsystem 活动变体选项的 mask，而无需导航到 Variant Subsystem 模块内部。

- 如果 Variant Subsystem 模块未设置 mask，则双击该模块会打开其活动选项的 mask。单击 **Look under mask** 徽章，或从 Variant Subsystem 模块的上下文菜单中选择相应选项，将直接带您进入活动选项内部。
- 如果 Variant Subsystem 模块设置了 mask，且活动选项也具有 mask，则双击该模块会打开 Variant Subsystem mask。
- 如果 Variant Subsystem 模块未设置 mask，且其活动选项设置了 mask，则双击 **Look under mask** 徽章会将您带到变体层。在设置了 mask 的 Variant Subsystem 模块中，如果活动选项未设置 mask，您会看到类似行为。

当您单击链接的 Variant Subsystem 模块的 **Look under mask** 徽章，且其活动选项是链接且设置 mask 的 Model Reference 模块时，Model Reference 会在单独的编辑器中打开。此外，您必须对活动选项模块的 mask 参数执行 `set_param` 操作，而不是对 Variant Subsystem 模块执行。

活动选项 mask 的提升仅限于其直接父级。不支持嵌套 Variant Subsystem mask 提升。

#### R2024a：将变体选项指定为字符串数组

您可以在 Variant Assembly Subsystem 模块中将 **Variant choices specifier** 指定为字符串数组。

#### R2023b：提升活动选项的内容预览

Simulink 会自动提升 Variant Subsystem 模块活动选项的内容预览。当活动选项是未加载的 Model Reference，且活动选项是 Stateflow chart 时，Variant Subsystem 会显示为内容预览。

#### R2023b：直接导航到活动选项

您可以通过双击 Variant Subsystem 模块直接导航到活动变体内部。当您从上下文菜单中选择 **Open in New Tab** 或 **Open in New Window** 时，活动选项会在新选项卡或新窗口中打开。您还可以使用 `open_system` 函数访问变体层和活动选项。

```
open_system(vssBlock)
open_system(vssBlock,'ActiveChoice','window')
```

当活动选项具有 `OpenFcn` 回调时，双击 Variant Subsystem 模块不会执行该回调。此外，如果活动选项是未加载的引用模型，双击 Variant Subsystem 不会导航到活动选项内部。

#### R2021a：自动提升活动变体的 mask 图标

Simulink 会自动在父 Variant Subsystem 上显示活动变体模块的 mask 图标。在 R2021a 之前，您必须在 Variant Subsystem 的 mask 上提供图标绘制命令，以显示底层活动变体模块的 mask 图标。

## Libraries

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

## Description

The Variant Subsystem block enables you to include multiple
implementations of a component in a separate hierarchy.

For example, suppose you want to simulate a model that represents a vehicle with three
possible engine configurations: 2-cylinder gas, 4-cylinder gas, and 8-cylinder gas. You
could implement each engine model as a separate subsystem inside the Variant
Subsystem block and then switch between the subsystems based on the Types of Variant Control Modes in Variant Blocks you select. For
more information, see Introduction to Variant Controls.

**Note**

Only one implementation of a Variant Subsystem block is active
during simulation.

Multiple models of an engine inside a Variant Subsystem block

The Variant Subsystem block is a template preconfigured to contain two
or more blocks to use as variant choices. These choices represent multiple
implementations of a system. Only one child block is active during model execution. The
active child block is referred to as the *active variant*.

Each variant choice inside the Variant Subsystem block is associated
with a **Variant
control mode** and a **Variant
activation time**. The variant control mode determines how to select the
active variant. The variant activation time determines a time to activate the choices
and to decide whether to include only the active choice or both active and inactive
choices in the generated code.

A Variant Subsystem block can contain a mixture of Subsystem blocks, Model blocks, or Subsystem
Reference blocks as variant choices. A Variant Subsystem
block with only Model blocks as choices is called a Variant
Model block. For more information, see Implement Variations in Separate Hierarchy Using Variant Subsystems. A Variant Subsystem block with Model or
Subsystem Reference blocks as choices that can be added or removed
only from external files and not within the block is called a Variant Assembly
Subsystem block.

Apart from the variant choices, you can include Inport, control port (Enable, Trigger, Reset, and Function-Call Subsystem), Outport, or Connection Port (Simscape) blocks inside a
Variant Subsystem block. There are no drawn connections between the
blocks that are inside the Variant Subsystem blocks. The software
automatically wires the active variant to the Inport and
Outport blocks of the Variant Subsystem during model
compilation. The blocks representing variant choices can have input and output ports
that differ in number from the input and output ports in the parent Variant
Subsystem block. For more information, see Map Input and Output Ports of Variant Choices in Variant Subsystem.

When you load a model with a Variant Subsystem block that has variant
choices stored in subsystem files, by default, only the active choice is loaded to
optimize the loading time for models. However, if you initialize a model
programmatically using the `find_system`,
`get_param`, or `set_param` function, inactive
choices might get loaded.

Using Variant Subsystem block allows you to:

- Mix Subsystem, Model, and Subsystem
  Reference blocks as variant choices.
- Model components that do not have similar interface. You can have
  different numbers of inports and outports for multiple variant choices
  inside a Variant Subsystem. However, the conditions listed in
  Map Input and Output Ports of Variant Choices in Variant Subsystem must be met.
- Establish a hierarchical block diagram, where the Variant
  Subsystem block is on one layer and the variant choices are on
  another layer.
- Keeps functionally related blocks together.
- Reduce the complexity of your model.
- During model compilation, the software eliminates inactive blocks
  throughout the model, depending on the variant activation time you
  select.

The color and icon of the variant badge on the block icon changes depending on the
values of the **Variant activation time**, **Variant control
mode**, and **Propagate conditions outside of variant
subsystem** parameters set on the block. For more information, see Variant Badges.

### Open the Block

You can open the Variant Subsystem block from the Simulink® interface or programmatically. These methods enable you to access the
active variant choice or the entire variant layer of the Variant
Subsystem block, depending on your requirements.

**Open from Simulink Interface**

Use any of these actions in the Simulink interface to open the Variant Subsystem
block.

| Keyboard and mouse action | Result |
| --- | --- |
| Double-click | Opens the active variant choice inside the block in a new tab  **Note**  If the variant choice is a Model block and the model it references is not loaded, then double-clicking the block opens the variant layer containing the variant choices instead of opening the underlying layer of the active variant choice. |
| Hold **Ctrl** and double-click | Opens the block in a new tab, shows the variant layer |
| Hold **Shift** and double-click | Opens the block in a new window, shows the variant layer |
| Right-click, select **Open** > **Open in New Tab** | Opens the block in the current window, shows the variant layer |
| Right-click, select **Open** > **Open in New Window** | Opens the block in a new window, shows the variant layer |
| Right-click the variant badge, select **Open** >**(active variant)** | Opens the active variant choice in a new tab |
| Right-click the variant badge, select **Open** > **variant control (variant choice name)**, where *`variant control`* is the variant control `expression`, `label`, or `(sim)` or `(codegen)` for the variant choice specified by the *variant choice name.* | Opens the selected variant choice in a new tab |

**Open Programmatically**

Use either of these commands to open the Variant Subsystem
block, where *`variantSubsystemBlockName`* is the name of
the block:

- `open_system("variantSubsystemBlockName")`
  command — Open the Variant Subsystem block and view its
  variant layers.
- `open_system("variantSubsystemBlockName","ActiveChoice")`
  — Open the active variant choice within the Variant
  Subsystem block.

For information on additional options to open the Variant
Subsystem block using the `open_system` command,
such as opening in a new tab or window, see `open_system`.

## Ports

### Input

### **In\_1** — Input port corresponding to root-level Inport blocks in variant subsystem same data types accepted by Inport blocks

Each Subsystem, Model, or Subsystem
Reference block contained within a Variant
Subsystem represents one variant choice. The variant choices can
contain Inport, control port (Enable, Trigger, Reset, and Function-Call Subsystem), or
Connection Port (Simscape) blocks at
its input. The variant choices can have input ports that differ in number
from the input ports in the parent Variant Subsystem block.
However, the conditions described in Map Input and Output Ports of Variant Choices in Variant Subsystem must be met.
### Output

### **Out\_1** — Output port corresponding to root-level Outport blocks contained in variant subsystem same data types accepted by Outport blocks

Each Subsystem, Model, or Subsystem
Reference block contained within a Variant
Subsystem represents one variant choice. The variant choices can
contain Outport or Connection Port (Simscape) blocks at
its output. The variant choices can have output ports that differ in number
from the output ports in the parent Variant Subsystem block.
However, the conditions described in Map Input and Output Ports of Variant Choices in Variant Subsystem must be met.

The unconnected output ports (inactive output ports) of a Variant
Subsystem block output a ground value. To output a value other
than ground, select the **Specify output when source is
unconnected** parameter of the Outport block and
specify a value.

## Parameters

To access these parameters, right-click the variant badge on the block icon and select
**Block Parameters**. For more information, see Variant Badges.

### **Variant control mode** — Variant control mode `expression` (default) | `label` | `sim codegen switching`

The variant control that determines the active variant choice can be any of these
types.

- `expression` — The software chooses the active variant based
  on the evaluation of the variant conditions. When a condition expression evaluates to
  `true`, the corresponding variant choice becomes active. When a
  condition expression evaluates to `false`, the corresponding variant
  choice becomes inactive. See Switch Between Choices Using Condition Expressions in Variant Blocks.
- `label` — The software chooses the active variant based on
  the name of the variant. The variant control is a string and does not require you to
  create any variable in any workspaces. See Switch Between Choices Using Labels in Variant Blocks.
- `sim codegen switching` — Automatically switch between the
  variants for simulation and code generation workflows without creating any workspace
  variable. When you simulate a model, the software automatically chooses the
  `sim` branch as the active choice. Similarly, when you do a
  software-in-the-loop (SIL) or processor-In-Loop (PIL) simulation, generate code, or use
  external mode, the software automatically chooses the `codegen` branch.
  See Switch Between Choices for Simulation and Code Generation Workflows Without Using Control Variables in Variant Blocks.

For more information on variant control modes, see Introduction to Variant Controls. For a comparison between different types of variant control modes, see Compare Different Types of Variant Control Modes in Variant Blocks.

#### Dependencies

The availability of different variant activation times depends on the type of the
**Variant control mode** that you specify. The
**Variant activation time** parameter determines the time when
the software sets the active choice. The parameter also determines which variability
to include in the generated code. This table explains the variant activation time
supported by each variant control mode.

| **Variant activation time** | | | | |  |
| --- | --- | --- | --- | --- | --- |
| **Variant control mode** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` | `runtime` (Variant Subsystem block only) |
| `expression` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `label` | ✓ | x | x | x | x |
| `sim codegen switching` | ✓ | ✓ | x | x | x |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantControlMode` |
| **Type:** character vector |
| **Values:** `'expression'` | `'label'` | `'sim codegen switching'` |
| **Default:** `'expression'` |

### **Variant activation time** — Time when software chooses active variant choice `update diagram` (default) | `update diagram analyze all choices` | `code compile` | `startup` | `runtime` | `inherit from Simulink.VariantControl`

This parameter determines which variability to include in the simulation and code
generation workflows. For more information, see Activate Variant During Different Stages of Simulation and Code Generation Workflow.

- `update diagram` — When you execute the model, only
  the active choice is included in the simulation and the code generation
  workflow. Generated code contains only the active choice.
- `update diagram analyze all choices` — When you
  execute the model, both active and inactive choices are analyzed for consistency
  across the model. However, only the active choice is included in the simulation
  and the code generation workflow. Generated code contains only the active
  choice.
- `code compile` — When you execute the model, both
  active and inactive choices are analyzed for consistency across the model, and
  all choices are included in the simulation and the code generation workflow.
  Generated code contains both the active and inactive choices enclosed in the
  preprocessor conditionals `#if` and `#elif`.
  However, the executable built from the generated code contains only active
  choice.
- `startup` — When you execute the model, both active
  and inactive choices are analyzed for consistency across the model, and all
  choices are included in the simulation and the code generation workflow. With
  this option, you can improve the speed of iterative simulations using fast
  restart. For more information, see Run Iterative Simulations Without Recompiling Model for Variant Systems Using Fast Restart. Code
  generated from the model contains both the active and inactive choices that are
  enclosed in regular `if` conditions. The executable built from
  the generated code also contains both active and inactive choices.
- `runtime` — When you execute the model, the active
  variant can switch during simulation or execution of the generated code by using
  the Parameter
  Writer block. Place a Parameter Writer block inside a
  conditionally executed subsystem or in an Initialize Function block, a
  Reinitialize Function block, or a Reset Function block. For more
  information on the blocks, see Event Functions.
  You can use the Parameter Writer block to write to block
  parameters, model workspace variables, and base workspace variables. Multiple
  variant control variables are not supported for
  `runtime` activation time. All modeling patterns
  supported by the Parameter Writer block are valid for run-time
  activation. For more information, see Common Uses of Parameter Writer Block.

  When you set the **Variant activation time** parameter of the
  Variant Subsystem block to
  `runtime`, the color of the inactive variant choices
  does not fade. In this case, the setting of the **Variant
  Fading** option in the **Information Overlays**
  menu on the **Debug** tab of the Simulink Editor is
  ignored.
- `inherit from Simulink.VariantControl` — When you
  execute the model, the block inherits the activation time from its variant
  control variables of type `Simulink.VariantControl`. If a variant block has multiple variant
  control variables of type `Simulink.VariantControl`, then all those
  variables must have the same activation time.

The table compares the different variant activation times based on conditional code,
variant switching, handling of states, and fast restart support.

|  | `update diagram` or `update diagram analyze all choices` | `code compile` | `startup` | `runtime` |
| --- | --- | --- | --- | --- |
| **Generated conditional code** | Inactive conditional code is not available. | Conditional code is present inside preprocessor macros. The inactive choice code is eliminated when generated code is compiled. | Conditional code is generated as part of an `if-elseif-else` statement. The variant control variable value cannot be modified during execution. | Conditional code is generated as part of an `if-elseif-else` statement. The variant control variable value can be modified during execution. |
| **Variant switching during simulation or code execution** | Not supported. | Not supported. | Supported at startup (before simulation start at *t* = 0). | Supported. The active variants are switched by changing the variant control variable using the Parameter Writer block. |
| **Explicit setting of held or reset option for states** | Not supported. States are reset for inactive blocks. | Not supported. States are reset for inactive blocks | States cannot be changed during simulation. In the generated code, if you attempt to change the variant, states are in held state. | States are held by default. Reset states explicitly through State Writer blocks. Read blocks with states by using the State Reader block and transfer to another choice by using the State Writer block. |
| **Executable size** | Smaller size. Code is not generated for the inactive variant. | Smaller size. The inactive variant code is removed during compilation. | Comparatively larger size. Both active and inactive variant code is available for startup switching. | Comparatively larger size. Both active and inactive variant code is available for run-time switching. |
| **Fast restart support** | Not supported. | Not supported. | Supported. | Supported. |

#### Dependencies

- The availability of different variant activation times depends on the type
  of the variant control mode that you specify. The **Variant
  activation time** parameter determines when the software sets
  the active choice. The parameter also determines which variability to
  include in the generated code. This table explains the variant activation
  time supported by each variant control mode.

  | **Variant activation time** | | | | |  |
  | --- | --- | --- | --- | --- | --- |
  | **Variant control mode** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` | `runtime` |
  | `expression` | ✓ | ✓ | ✓ | ✓ | ✓ |
  | `label` | ✓ | x | x | x | x |
  | `sim codegen switching` | ✓ | ✓ | x | x | x |
- To enable switching of active variant choice of the Variant
  Subsystem block using the `runtime` activation
  time, you must use the Parameter Writer block. Set the
  **Destination** parameter of the Parameter
  Writer block based on the location of your variant control
  variable and select **Validate parameter** :

  - `Block parameter` — Control variable
    is a mask parameter in a subsystem.
  - `Model workspace variable` — Control
    variable is located in the model workspace.
  - `Base workspace variable` — Control
    variable is located in the base workspace or a data
    dictionary.

  For example, you can create a mask parameter
  `V` in a subsystem and use it in a variant condition
  expression for a variant control. The Parameter Writer block
  writes to the value of `V` in the variant control
  condition.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantActivationTime` |
| **Type:** character vector |
| **Values:** `'update diagram'` | `'update diagram analyze all choices'` | `'code compile'` | `'startup'`| `'runtime'` |
| **Default:** `'update diagram'` |

### **Variant control variable** — Variable to determine active variant choices `Simulink.VariantControl` object | scalar variable | `Simulink.Parameter` object | `struct`

When you specify a variable of type listed in Types of Variant Control Variables (Operands) in Variant Blocks, the
software generates variant control expressions for the variant choices of the
Variant Assembly Subsystem block. The **Variant
control variable** that you specify here is on the left side and
the members of the **Variant enumeration choice** are on the
right side of the generated expressions. Both the sides are related by
`==`.

The variant control variable acts as a switch to change the active variant
choice. You specify a value for a variant control variable and run the
simulation. During simulation, the software evaluates the variant control
expressions to determine the active variant choice. When an expression evaluates
to `true`, the corresponding variant choice is set active. To
change the active variant, change the value of the variant control variable such
that the corresponding variant control expression evaluates to
`true` turns active.

#### Dependencies

This parameter is available only in Variant Assembly
Subsystem block. To enable this parameter, set **Variant
control mode** to `expression`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantControlVariable` |
| **Type:** character vector |
| **Values:** `Simulink.VariantControl` object, scalar variable, `Simulink.Parameter` object, `struct` |
| **Default:** `''` |

### **Variant choices enumeration** — Enumeration class to add variant choices enumeration class with model or subsystem filenames as its members

To add Model or Subsystem Reference blocks as
variant choices to a Variant Assembly Subsystem block, specify an
enumeration class name that contains the corresponding model or subsystem
filenames as its members. You can then validate the enumeration class using the
Refresh button in the **Variant choices** table. On a
successful validation, the members of the enumeration class are added as variant
choices to the Variant Assembly Subsystem block. Each choice has
a variant control expression with **Variant control
variable** on its left side and the members of the
**Variant choices enumeration** that you specify here on
its right side. Both the sides of the expression are related by
`==`. The newly added variant choices and their
corresponding control expressions are displayed in the **Variant
choices** table.

To remove variant choices from a Variant Assembly Subsystem
block, remove the corresponding members from the enumeration class that you
specify here. You cannot manage the variant choices from inside the
Variant Assembly Subsystem block.

The enumeration class that you specify must be on the search path of your
current MATLAB® session. For information on how to add files or folders to the
search path, see `addpath`.

For more information on how to add choices using the **Variant choices
enumeration** parameter, see Add or Remove Variant Choices of Variant Assembly Subsystem Blocks Using External Files.

#### Dependencies

This parameter is available only in Variant Assembly
Subsystem block. To enable this parameter, set **Variant
control mode** to `expression`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantChoicesEnumeration` |
| **Type:** character vector |
| **Values:** enumeration class defined using `classdef` or `Simulink.defineIntEnumType` |
| **Default:** `''` |

### **Variant choices specifier** — MATLAB expression to add variant choices any MATLAB expression that evaluates to a one-dimensional cell array of model or subsystem filenames, or filename patterns that match the model or subsystem filenames or an array of strings

To add Model or Subsystem Reference blocks as
variant choices to a Variant Assembly Subsystem block, specify
the corresponding model or subsystem filenames. The filenames must be specified
as a MATLAB expression that returns a one-dimensional cell array of character
vectors when evaluated or an array of strings. You can then validate the
expression using the Refresh button in the **Variant choices**
table. On a successful validation, the blocks that correspond to the specified
files are added as variant choices to the Variant Assembly
Subsystem block. For each choice, a variant control label is
generated. The name of the variant control label is same as the name of the
choice. The newly added variant choices and their corresponding control labels
are displayed in the **Variant choices** table.

To remove variant choices from a Variant Assembly Subsystem
block, modify the expression specified in this parameter. You cannot manage the
variant choices of a Variant Assembly Subsystem block from inside
the block.

The MATLAB expression that you specify must contain either of these:

- Model or subsystem filenames that are on the search path of your
  current MATLAB session. For example, if you specify
  `{'model1.slx', 'subsystemRef1.slx'}` as a
  specifier, the blocks that correspond to the
  `model1.slx` and
  `subsystemRef1.slx` files are added as variant
  choices of the Variant Assembly Subsystem
  block.
- File name patterns that match the model or subsystem filenames on
  the MATLAB path. The paths in the pattern can be absolute or
  relative to the parent folder of the model that contains the
  Variant Assembly Subsystem block. For example, if
  you specify `{'folder_1/*.slx', 'folder_2/*.slx'}`
  as a specifier, the software passes the character vectors
  `folder_1/*` and `folder2/*`
  to the `dir` function. The
  function then returns the model and the subsystem files that are
  located inside the `folder1` and
  `folder2` folders. The blocks that correspond
  to the returned files are added as variant choices of the
  Variant Assembly Subsystem block.

For information on how to add files or folders to the search
path, see `addpath`.

For more information on how to specify choices in the **Variant choices
specifier** parameter, see Add or Remove Variant Choices of Variant Assembly Subsystem Blocks Using External Files.

#### Dependencies

This parameter is available only in Variant Assembly
Subsystem block. To enable this parameter, set **Variant
control mode** to `label`.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `VariantChoicesSpecifier` |
| **Type:** character vector |
| **Value:** Any MATLAB expression that evaluates to a one-dimensional cell array of filenames or filename patterns. |
| **Default:** `''` |

### **Variant choices** — Table of variant choices, variant controls, and conditions empty table (default)

The table has a row for each variant choice contained in the variant
subsystem. If there are no variant choices, the table is empty.

You can use buttons to the left of the **Variant choices**
table to modify the elements in the table.

| To... | Click... |
| --- | --- |
| **Create and add a new subsystem choice**: Create a new Subsystem block as a variant choice and add an entry for the new choice in the table. | the Create and add a new subsystem choice button |
| **Create and add a new model variant choice**: Create a new Model block as a variant choice and add an entry for the new choice in the table. | the Create and add a new model variant choice button |
| **Delete selected variant choices**: Delete variant choices permanently. | the Delete selected variant choices button |
| **Create/Edit selected variant object**: Create or edit a `Simulink.VariantExpression` object in the global workspace and specify the variant condition using the `Simulink.VariantExpression` object parameter dialog box.  **Note**  For a model that uses the base workspace, this operation creates the `Simulink.VariantExpression` object in the base workspace and the object is available only for the current MATLAB session. To permanently store the data, save the object in a MAT file or MATLAB script. | the Create or Edit selected variant object button |
| **Open selected variant choice block**: Open the Subsystem block for the selected row. | the Open selected variant choice block button |
| **Refresh dialog information from Variant Subsystem contents**: Update the **Variant choices** table according to the variant choices and values of the variant control in the global workspace. | the Refresh dialog information from Variant Subsystem contents button |

#### Dependencies

The Variant Assembly Subsystem block allows you to only
open the selected variant choice and refresh the list of variant choices
using the buttons in this section. To add new variant choices to the
Variant Assembly Subsystem block, see Add or Remove Variant Choices of Variant Assembly Subsystem Blocks Using External Files.

### **Name (read-only)** — Variant choice name Read-only: `Subsystem` and `Subsystem1` (default) | name of choices contained in Variant Subsystem

This parameter is read-only.

This parameter displays the
name of the choices. Each choice has a variant control in the form of labels,
expressions, or switches. For Variant Assembly Subsystem in the
`label` mode, no separate variant control is
available. The name of the choice is used as a variant control to set the active
choice.

### **Variant control label** — Name of choice in `label` mode `true` or `false` (default) | string

A name for a choice, specified as a string.

#### Dependencies

To enable this parameter, set **Variant control mode** to
`label`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `VariantControl` |
| **Values:** | variant control that is associated with the variant choice |
| **Data Types:** | `char` |

**Example:** `set_param(gcb, 'VariantControl', 'V == 3')`,
where `gcb` is the variant choice of the Variant
Subsystem block.

**Example:** `get_param(gcb, 'VariantControl')`, where
`gcb` is the variant choice of the Variant
Subsystem block.

### **Variant control switch** — Variant choices for simulation and code generation workflows `(sim)` | `(codegen)`

Specify `(sim)` to activate the corresponding variant choice
during simulation. Specify `(codegen)` to activate the
corresponding variant choice while performing code generation workflows such as
SIL, PIL, external mode, and so on.

#### Dependencies

To enable this parameter, set **Variant control mode** to
`sim codegen switching`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `VariantControl` |
| **Values:** | variant control that is associated with the variant choice |
| **Data Types:** | `char` |

**Example:** `set_param(gcb, 'VariantControl', '(sim)')`,
where `gcb` is the variant choice of the Variant
Subsystem block.

**Example:** `get_param(gcb, 'VariantControl')`, where
`gcb` is the variant choice of the Variant
Subsystem block.

### **Variant control expression** — Condition expression that determines the active choice `true` or `false` (default) | boolean condition expression | a `Simulink.VariantExpression` object representing a boolean condition expression | `(default)`

Specify the condition expression to determine the active choice. When a condition
expression evaluates to `true`, the software activates the
corresponding variant choice. When a condition expression evaluates to
`false`, the software deactivates the corresponding variant
choice.

The variant controls can be:

- Boolean condition expression for rapid prototyping. For example,
  `A == 1`, `A ~= B`, `A
  && B == 1`, and so on.
- A `Simulink.VariantExpression` object that contains a
  condition expression for condition reuse. See Simulink.VariantExpression Objects for Variant Condition Reuse of Variant Blocks.
- Default Variant Choice if none of the choices evaluates to
  `true`.

Here, `A` and `B` are operands called
as *variant control variables*. `==`,
`~=`, and `&&` are operators in the
condition expression. The condition expression can contain one or more such variant
control variables and operators. For information on supported types and storage location
of variant control variables, see Types of Variant Control Variables (Operands) in Variant Blocks and Storage Locations for Variant Control Variables (Operands) in Variant Blocks. For information
on operators, see Types of Operators in Variant Blocks for Different Activation Times.

For more information, see Switch Between Choices Using Condition Expressions in Variant Blocks.

In Variant Assembly Subsystem block, this parameter is a list of
auto-generated boolean expressions with **Variant control variable** on
the left-hand side and the members of the **Variant enumeration
choice** are on the right-hand side of the expressions. Both the sides of
the expressions are connected with `==`. This parameter is
read-only.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

Variant Subsystem block:

|  |  |
| --- | --- |
| **Parameter:** | `VariantControl` |
| **Values:** | variant control that is associated with the variant choice |
| **Data Types:** | `char` |

**Example:** `set_param(gcb, 'VariantControl', 'V == 3')`, where
`gcb` is the variant choice of the Variant
Subsystem block.

**Example:** `get_param(gcb, 'VariantControl')`, where
`gcb` is the variant choice of the Variant
Subsystem block.

Variant Source and Variant Sink blocks:

|  |  |
| --- | --- |
| **Parameter:** | `VariantControls` |
| **Values:** | variant controls that are associated with variant choices |
| **Data Types:** | `char` |

**Example:** `set_param(gcb, 'VariantControls', {'A == 1','A ==
2'})`, where `gcb` is the Variant
Sink or Variant Source block.

**Example:** `get_param(gcb, 'VariantControls')`, where
`gcb` is the Variant Sink or Variant
Source block.

### **Condition (read-only)** — Condition expression in `Simulink.VariantExpression` object Read-only: `N/A` (default)

This parameter is read-only.

This parameter displays the condition expression specified as
`Simulink.VariantExpression` object. To change or edit the condition
expression, use the `Simulink.VariantExpression` parameter dialog box
that appears when you double-click the object in the workspace.

**Note**

The operands that you specify in a condition expression of type
`Simulink.VariantExpression` must be defined in the base
workspace or a data dictionary. Specifying operands that are defined in the mask
or model workspace is not supported.

### **Label mode active choice** — Name of active choice in `label` mode `true (Subsystem)` (default) | `false (Subsystem1)`

This list contains the labels of all the variant choices. To set an active choice, select a
label from the list. The corresponding choice becomes active. Alternatively, to change
the active choice in label mode, you can follow the approaches described in Set Active Choices Using Variant Control Labels.

#### Dependencies

To enable this parameter, set **Variant control mode** to
`label`.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `LabelModeActiveChoice` |
| **Type:** character vector |
| **Value:** If no label mode active choice is specified, the value is empty. If a label mode active choice is specified, the value is the variant control label for the active choice. |
| **Default:** `''` |

### **Built-in empty choice** — Output zero if no variant choice is active `off` (default) | `on`

- `off` — Simulink generates an error when there is no active variant
  choice.
- `on` — When you select this option, Simulink adds a nonmodifiable variant choice entry to the
  **Variant choices** table with its variant control
  set to `(default)`. This entry does not appear as a
  visible variant choice in the Variant Subsystem block.
  During simulation, if there is no active variant choice, Simulink disconnects the variant choices of the Variant
  Subsystem block, thus removing the variant regions
  completely from the model. The inactive outports of the subsystem output
  zero. To output a value other than zero, select the **Specify
  output when source is unconnected** parameter of the
  Outport block and specify a value of your
  choice.

For more information, see Manage Variant Components to Pass Specified Values from Inactive Variant Subsystems with No Active Choice (Simulink Coder).

#### Dependencies

This parameter is available only if there are no
`default` variant choices in the Variant
Subsystem and if you set **Variant control
mode** to `expression`.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `EmptyChoice` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Built-in passthrough choice** — Assign input port values to output ports if no variant choice is active `off` (default) | `on`

- `off` — Simulink generates an error when there is no active variant
  choice.
- `on` — When you select this option, Simulink adds a nonmodifiable variant choice entry to the
  **Variant choices** table with its variant control
  set to `(default)`. This entry does not appear as a
  visible variant choice in the Variant Subsystem block.
  During simulation, if there is no active variant choice, Simulink bypasses the variant choices of the Variant
  Subsystem block. Only the input and output ports remain
  active, and the input port pass values directly to the output
  ports.

  For values to be mapped from input ports to output ports when no
  choice is active, the Variant Subsystem block must
  have:

  - Only data ports, with no other types of input and output
    ports
  - An equal number of data input and output ports
  - Input and output ports that exactly match the ports of variant
    choices

For more information, see Manage Variant Components to Pass Specified Values from Inactive Variant Subsystems with No Active Choice (Simulink Coder).

#### Dependencies

This parameter is available only if there are no
`default` variant choices in the Variant
Subsystem and if you set **Variant control
mode** to `expression`.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `PassThrough` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Propagate conditions outside of variant subsystem** — Option to choose if components outside of the variant subsystem must be informed of the active and inactive state of underlying blocks `off` (default) | `on`

When you select the **Propagate conditions outside of variant
subsystem** parameter, the software propagates the variant
condition of the underlying blocks to the Variant Subsystem
container block so the subsystem can adapt its interface to the state of the
underlying blocks. Ports that are mapped to the ports on the active choice
becomes active. Ports that are not mapped to the ports on the inactive choice
becomes inactive. Selecting this option ensures that the components outside of
the Variant Subsystem are aware of the active and inactive state
of blocks within the Variant Subsystem block. For more
information, see Propagate Variant Conditions to Define Variant Regions Outside Variant Subsystems to Promote Consistency and Reduce Errors and Propagate Variant Conditions to Control Execution of Conditional Subsystems

Variant conditions do not propagate outside a Variant Subsystem
block if all variant choices within the block have the same interface.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `PropagateVariantConditions` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Allow flexible interface** — Option to choose to make interface of the variant subsystem flexible `on` (default) | `off`

Specify whether to make the interface of a variant subsystem flexible.

- `on` — Simulate with variant choices that have
  input and output ports that differ in number from the input and
  output ports of the Variant Subsystem block.
- `off` — When you simulate with this option, if
  there is inconsistency in the interface, the software will generate
  errors with fix-it actions to match the ports of the variant choices
  to the Variant Subsystem block.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `AllowFlexibleInterface` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'on'` |

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

Actual data type or capability support depends on block implementation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic. Actual data type or capability support depends
on block implementation.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `Module` (default) | Generate code for the subsystem and the blocks within the subsystem. HDL Coder generates code for all the variant choices. |
| `BlackBox` | Generate a black-box interface. That is, the generated HDL code includes only the input/output port definitions for the subsystem. In this way, you can use a subsystem in your model to generate an interface to existing manually written HDL code.  The black-box interface generated for subsystems is similar to the interface generated for Model blocks, but without generation of clock signals. |
| `No HDL` | Remove the subsystem from the generated code. You can use the subsystem in simulation but treat it as a “no-op” in the HDL code. |

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

**Restrictions**

- The Variant Subsystem cannot be a design-under-test
  (DUT).
- **Variant activation time** parameter must be set to
  `update diagram`, `update
  diagram analyze all choices`, or
  `startup`.
- For the Outport block of the Variant Subsystem,
  **Specify output when source is unconnected**
  parameter must be disabled.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type or capability support depends on block implementation.

## Version History

**Introduced in R2010b**

### R2025a: Reduce overhead and irrelevant diagnostic messages by suppressing callbacks for inactive variant choices and commented blocks

The callbacks `LoadFcn`, `ContinueFcn`,
`InitFcn`, `ModelCloseFcn`,
`PauseFcn`, `PostSaveFcn`,
`PreSaveFcn`, `StartFcn`, and
`StopFcn` do not execute for inactive variant choices in Variant Subsystem blocks with the
`update diagram` activation time and for commented
blocks. This suppression reduces computational overhead and prevents unnecessary
diagnostic messages from the blocks that do not affect the current model iteration.
However, these callbacks are not suppressed for blocks within models or subsystem
files inside a commented or an inactive Model block or Subsystem Reference block. Also, the mask initialization and mask
parameter callbacks are not suppressed. For the list of applicable callbacks, see
Author Mask Initialization and Callbacks and Mask Parameters.

### R2025a: Parameter to output zero when no variant choices exist renamed from **Allow zero active variant controls**

The **Allow zero active variant controls** parameter is now
renamed to **Built-in empty choice**. This new parameter maintains
the previous functionality to remove the variant components and output zero when no
variant choice is active.

### R2025a: Assign input values to output ports when no variant choices exist

Use the **Built-in passthrough choice** parameter to bypass
variant region and assign input values to the output ports when no variant choice is
active.

### R2024b: `runtime` activation time : Change the active choice during simulation or code generation

Starting in R2024b, use the `runtime` variant activation time in
a Variant Subsystem block to change the active variant during
simulation or code generation by using the Parameter Writer block.
You can model all scenarios where the Parameter Writer block can
write to the variant control variable in the global workspace, mask workspace, or
model workspace.

### R2024a: Automated port synchronization

Simulink provides options to add missing ports and delete unused ports in
Variant Subsystem and Variant Assembly Subsystem
blocks to match the ports of the underlying variant choices. During simulation, if
Simulink encounters a port mismatch between a Variant Subsystem
or Variant Assembly Subsystem block and its variant choices, the
resulting error message provides the option of adding missing ports and deleting
unused ports to resolve the issue.

### R2024a: Use adapted rate-based model blocks as choices

You can use adapted rate-based model blocks as variant choices in a Variant
Subsystem block. When you add adapted rate-based models as variant
choices, the inports in the variant subsystem are matched to the port names of the
respective rate-based models.

### R2024a: Access the mask of the active variant choice

You can access the mask of the active variant choice of the Variant
Subsystem directly without having to navigate inside the Variant
Subsystem block.

- If the Variant Subsystem block is unmasked,
  double-clicking on the block opens the mask of its active choice.
  Clicking on the **Look under mask** badge or selecting
  the corresponding option from the context menu of the Variant
  Subsystem block takes you directly inside the active
  choice.
- If the Variant Subsystem block is masked and the active
  choice also has a mask, then double-clicking on the block opens the
  Variant Subsystem mask.
- If the Variant Subsystem block is unmasked and its
  active choice is masked, then double-clicking on the **Look
  under mask** badge takes you to the variant layer. You can
  see similar behavior in a masked Variant Subsystem block
  with an unmasked active choice.

When you click on the **Look under mask** badge of a linked
Variant Subsystem block with its active choice as a linked and
masked Model Reference block, the Model Reference
opens in a separate editor. Additionally, you must perform
`set_param` operations on the mask parameters of the active
choice block on the active choice, and not on the Variant Subsystem
block.

Promotion of the mask of the active choice is limited to its immediate parent.
Nested Variant Subsystem mask promotion is not supported.

### R2024a: Specify variant choices as an array of strings

You can specify **Variant choices specifier** as an
array of strings in Variant Assembly Subsystem block.

### R2023b: Promote content preview of active choice

Simulink promotes the content preview of the active choice of the
Variant Subsystem block automatically. When the active choice is
a Model Reference that is not loaded, and when the active choice is a
Stateflow chart, the Variant Subsystem is shown as the content
preview.

### R2023b: Navigate directly into active choice

You can navigate directly inside the active variant by double clicking on the
Variant Subsystem block. When you select **Open in New
Tab** or **Open in New Window** from the context menu,
the active choice is opened in a new tab or a new window. You can also use the
`open_system` function to access the variant layer and the
active choice.

```
open_system(vssBlock)
open_system(vssBlock,'ActiveChoice','window')
```

When the active choice
has an `OpenFcn` callback, double-clicking on the Variant
Subsystem block does not execute that callback. Additionally,
double-clicking on the Variant Subsystem does not navigate into the
active choice if the active choice is a referenced model that is not loaded.

### R2021a: Promote mask icon of active variant automatically

Simulink automatically displays the mask icon of the active variant block on
the parent Variant Subsystem. Prior to R2021a, you had to provide
icon drawing commands on the mask of the Variant Subsystem to display
the mask icon of the underlying active variant block.
