---
type: simulink-block
title: 'Variant Subsystem'
family: ports-and-subsystems
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'variantsubsystem'
language: zh-CN
chinese_source: worker-translation
---

# Variant Subsystem

## 端口

### Input

### **In\_1** — 对应于 variant subsystem 中根级 Inport 模块的输入端口，接受与 Inport 模块相同的数据类型

Variant Subsystem 中包含的每个 Subsystem、Model 或 Subsystem Reference 模块表示一个变体选项。变体选项可以在其输入处包含 Inport、控制端口（Enable、Trigger、Reset 和 Function-Call Subsystem）或 Connection Port (Simscape) 模块。变体选项的输入端口数量可以与父 Variant Subsystem 模块中的输入端口数量不同。但是，必须满足 Map Input and Output Ports of Variant Choices in Variant Subsystem 中描述的条件。

### Output

### **Out\_1** — 对应于 variant subsystem 中包含的根级 Outport 模块的输出端口，接受与 Outport 模块相同的数据类型

Variant Subsystem 中包含的每个 Subsystem、Model 或 Subsystem Reference 模块表示一个变体选项。变体选项可以在其输出处包含 Outport 或 Connection Port (Simscape) 模块。变体选项的输出端口数量可以与父 Variant Subsystem 模块中的输出端口数量不同。但是，必须满足 Map Input and Output Ports of Variant Choices in Variant Subsystem 中描述的条件。

Variant Subsystem 模块的未连接输出端口（非活动输出端口）输出 ground 值。要输出 ground 以外的值，请选择 Outport 模块的 **Specify output when source is unconnected** 参数并指定一个值。

## 参数

要访问这些参数，请右键单击模块图标上的变体徽章，然后选择 **Block Parameters**。有关详细信息，请参阅 Variant Badges。

### **Variant control mode** — 变体控制模式 `expression` (默认) | `label` | `sim codegen switching`

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

### **Variant activation time** — 软件选择活动变体选项的时间 `update diagram` (默认) | `update diagram analyze all choices` | `code compile` | `startup` | `runtime` | `inherit from Simulink.VariantControl`

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

### **Variant control variable** — 用于确定活动变体选项的变量 `Simulink.VariantControl` 对象 | 标量变量 | `Simulink.Parameter` 对象 | `struct`

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

### **Variant choices enumeration** — 用于添加变体选项的枚举类，其成员为模型或子系统文件名

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

### **Variant choices specifier** — 用于添加变体选项的 MATLAB 表达式，该表达式求值为模型或子系统文件名的一维 cell 数组，或匹配模型或子系统文件名的文件名模式，或字符串数组

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

### **Variant choices** — 变体选项、变体控制和条件的表 空表（默认）

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

### **Name (read-only)** — Variant 选项名称 只读：`Subsystem` 和 `Subsystem1`（默认） | Variant Subsystem 中包含的选项名称

此参数为只读。

此参数显示选项的名称。每个选项都有一个变体控制，其形式为标签、表达式或开关。对于处于 `label` 模式的 Variant Assembly Subsystem，没有单独的变体控制可用。选项的名称用作变体控制以设置活动选项。

### **Variant control label** — `label` 模式下选项的名称 `true` 或 `false`（默认） | string

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

### **Variant control switch** — 用于仿真和代码生成工作流的变体选项 `(sim)` | `(codegen)`

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

### **Variant control expression** — 确定活动选项的条件表达式 `true` 或 `false`（默认） | boolean 条件表达式 | 表示 boolean 条件表达式的 `Simulink.VariantExpression` 对象 | `(default)`

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

### **Condition (read-only)** — `Simulink.VariantExpression` 对象中的条件表达式 只读：`N/A`（默认）

此参数为只读。

此参数显示指定为 `Simulink.VariantExpression` 对象的条件表达式。要更改或编辑条件表达式，请使用在工作区中双击该对象时出现的 `Simulink.VariantExpression` 参数对话框。

**注意**

您在类型为 `Simulink.VariantExpression` 的条件表达式中指定的操作数必须在基础工作区或数据字典中定义。不支持指定在 mask 或模型工作区中定义的操作数。

### **Label mode active choice** — `label` 模式下活动选项的名称 `true (Subsystem)`（默认） | `false (Subsystem1)`

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

### **Built-in empty choice** — 如果没有活动变体选项则输出零 `off`（默认） | `on`

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

### **Built-in passthrough choice** — 如果没有活动变体选项，则将输入端口值分配给输出端口 `off`（默认） | `on`

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

### **Propagate conditions outside of variant subsystem** — 选择是否必须将底层模块的活动和非活动状态通知 variant subsystem 外部的组件的选项 `off`（默认） | `on`

当您选择 **Propagate conditions outside of variant subsystem** 参数时，软件会将底层模块的变体条件传播到 Variant Subsystem 容器模块，以便该子系统可以使其接口适应底层模块的状态。映射到活动选项上的端口的端口变为活动。未映射到非活动选项上的端口的端口变为非活动。选择此选项可确保 Variant Subsystem 外部的组件知道 Variant Subsystem 模块内模块的活动和非活动状态。有关详细信息，请参阅 Propagate Variant Conditions to Define Variant Regions Outside Variant Subsystems to Promote Consistency and Reduce Errors 和 Propagate Variant Conditions to Control Execution of Conditional Subsystems

如果 Variant Subsystem 模块内的所有变体选项具有相同的接口，则变体条件不会传播到 Variant Subsystem 模块外部。

#### Programmatic Use

|  |
| --- |
| **Parameter:** `PropagateVariantConditions` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Allow flexible interface** — 选择使 variant subsystem 接口灵活的选项 `on`（默认） | `off`

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

## 所属库

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

## 模块特性

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

## 扩展功能

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

实际数据类型或能力支持取决于模块实现。

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

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

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

实际数据类型或能力支持取决于模块实现。

## 版本历史

**在 R2010b 中引入**

### R2025a：通过抑制非活动变体选项和注释模块的回调来减少开销和不相关诊断消息

对于具有 `update diagram` 激活时间的 Variant Subsystem 模块中的非活动变体选项以及注释模块，回调 `LoadFcn`、`ContinueFcn`、`InitFcn`、`ModelCloseFcn`、`PauseFcn`、`PostSaveFcn`、`PreSaveFcn`、`StartFcn` 和 `StopFcn` 不会执行。此抑制可减少计算开销，并防止不影响当前模型迭代的模块产生不必要的诊断消息。但是，对于注释的或非活动的 Model 模块或 Subsystem Reference 模块内的模型或子系统文件中的模块，不会抑制这些回调。此外，mask 初始化和 mask 参数回调不会被抑制。有关适用回调的列表，请参阅 Author Mask Initialization and Callbacks 和 Mask Parameters。

### R2025a：在没有变体选项时输出零的参数已从 **Allow zero active variant controls** 重命名

**Allow zero active variant controls** 参数现在已重命名为 **Built-in empty choice**。此新参数保留了以前的功能：移除变体组件，并在没有活动变体选项时输出零。

### R2025a：在没有变体选项时将输入值分配给输出端口

使用 **Built-in passthrough choice** 参数绕过变体区域，并在没有活动变体选项时将输入值分配给输出端口。

### R2024b：`runtime` 激活时间：在仿真或代码生成期间更改活动选项

从 R2024b 开始，在 Variant Subsystem 模块中使用 `runtime` 变体激活时间，通过 Parameter Writer 模块在仿真或代码生成期间更改活动变体。您可以对所有场景建模，其中 Parameter Writer 模块可以写入全局工作区、mask 工作区或模型工作区中的变体控制变量。

### R2024a：自动端口同步

Simulink 提供选项来添加缺失端口并删除 Variant Subsystem 和 Variant Assembly Subsystem 模块中未使用的端口，以匹配底层变体选项的端口。在仿真期间，如果 Simulink 遇到 Variant Subsystem 或 Variant Assembly Subsystem 模块与其变体选项之间的端口不匹配，则生成的错误消息会提供添加缺失端口和删除未使用端口的选项来解决该问题。

### R2024a：使用自适应速率模型模块作为选项

您可以在 Variant Subsystem 模块中使用自适应速率模型模块作为变体选项。当您将自适应速率模型添加为变体选项时，variant subsystem 中的 inport 会与相应速率模型的端口名称匹配。

### R2024a：访问活动变体选项的 mask

您可以直接访问 Variant Subsystem 活动变体选项的 mask，而无需导航到 Variant Subsystem 模块内部。

- 如果 Variant Subsystem 模块未设置 mask，则双击该模块会打开其活动选项的 mask。单击 **Look under mask** 徽章，或从 Variant Subsystem 模块的上下文菜单中选择相应选项，将直接带您进入活动选项内部。
- 如果 Variant Subsystem 模块设置了 mask，且活动选项也具有 mask，则双击该模块会打开 Variant Subsystem mask。
- 如果 Variant Subsystem 模块未设置 mask，且其活动选项设置了 mask，则双击 **Look under mask** 徽章会将您带到变体层。在设置了 mask 的 Variant Subsystem 模块中，如果活动选项未设置 mask，您会看到类似行为。

当您单击链接的 Variant Subsystem 模块的 **Look under mask** 徽章，且其活动选项是链接且设置 mask 的 Model Reference 模块时，Model Reference 会在单独的编辑器中打开。此外，您必须对活动选项模块的 mask 参数执行 `set_param` 操作，而不是对 Variant Subsystem 模块执行。

活动选项 mask 的提升仅限于其直接父级。不支持嵌套 Variant Subsystem mask 提升。

### R2024a：将变体选项指定为字符串数组

您可以在 Variant Assembly Subsystem 模块中将 **Variant choices specifier** 指定为字符串数组。

### R2023b：提升活动选项的内容预览

Simulink 会自动提升 Variant Subsystem 模块活动选项的内容预览。当活动选项是未加载的 Model Reference，且活动选项是 Stateflow chart 时，Variant Subsystem 会显示为内容预览。

### R2023b：直接导航到活动选项

您可以通过双击 Variant Subsystem 模块直接导航到活动变体内部。当您从上下文菜单中选择 **Open in New Tab** 或 **Open in New Window** 时，活动选项会在新选项卡或新窗口中打开。您还可以使用 `open_system` 函数访问变体层和活动选项。

```
open_system(vssBlock)
open_system(vssBlock,'ActiveChoice','window')
```

当活动选项具有 `OpenFcn` 回调时，双击 Variant Subsystem 模块不会执行该回调。此外，如果活动选项是未加载的引用模型，双击 Variant Subsystem 不会导航到活动选项内部。

### R2021a：自动提升活动变体的 mask 图标

Simulink 会自动在父 Variant Subsystem 上显示活动变体模块的 mask 图标。在 R2021a 之前，您必须在 Variant Subsystem 的 mask 上提供图标绘制命令，以显示底层活动变体模块的 mask 图标。

## 描述

包含 Subsystem 模块作为变体选项的模板子系统

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

### Open the Block

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
