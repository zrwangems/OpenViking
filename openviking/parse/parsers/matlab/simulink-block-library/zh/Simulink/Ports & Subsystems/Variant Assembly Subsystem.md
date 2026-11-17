---
type: simulink-block
title: 'Variant Assembly Subsystem'
family: 'ports-subsystems'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'variantsubsystem'
documentation_source_path: 'slref/variantsubsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Variant Assembly Subsystem

## 端口

### 输入

### **In\_1** — 输入端口，对应于 Variant Subsystem 中根级 Inport 模块，接受与 Inport 模块相同的数据类型

Variant Subsystem 中包含的每个 Subsystem、Model 或 Subsystem Reference 模块都表示一个变体选择。变体选择可以在其输入处包含 Inport、控制端口（Enable、Trigger、Reset 和 Function-Call Subsystem）或 Connection Port (Simscape) 模块。变体选择可以具有与父级 Variant Subsystem 模块中的输入端口数量不同的输入端口。但是，必须满足 Map Input and Output Ports of Variant Choices in Variant Subsystem 中所述的条件。

### 输出

### **Out\_1** — 输出端口，对应于 Variant Subsystem 中包含的根级 Outport 模块，接受与 Outport 模块相同的数据类型

Variant Subsystem 中包含的每个 Subsystem、Model 或 Subsystem Reference 模块都表示一个变体选择。变体选择可以在其输出处包含 Outport 或 Connection Port (Simscape) 模块。变体选择可以具有与父级 Variant Subsystem 模块中的输出端口数量不同的输出端口。但是，必须满足 Map Input and Output Ports of Variant Choices in Variant Subsystem 中所述的条件。

Variant Subsystem 模块的未连接输出端口（非活动输出端口）输出接地值。要输出除接地值以外的值，请选择 Outport 模块的 **Specify output when source is unconnected** 参数并指定一个值。

## 参数

要访问这些参数，请右键单击模块图标上的变体徽章，然后选择 **Block Parameters**。有关更多信息，请参阅 Variant Badges。

### **Variant control mode** — 变体控制模式 `expression`（默认）| `label` | `sim codegen switching`

确定活动变体选择的变体控制可以是以下任一类型。

- `expression` — 软件基于变体条件的求值选择活动变体。当条件表达式求值为 `true` 时，对应的变体选择变为活动。当条件表达式求值为 `false` 时，对应的变体选择变为非活动。请参阅 Switch Between Choices Using Condition Expressions in Variant Blocks。
- `label` — 软件基于变体名称选择活动变体。变体控制是一个字符串，不要求您在任何工作区中创建任何变量。请参阅 Switch Between Choices Using Labels in Variant Blocks。
- `sim codegen switching` — 在无需创建任何工作区变量的情况下，自动在用于仿真和代码生成工作流的变体之间切换。当您仿真模型时，软件自动选择 `sim` 分支作为活动选择。类似地，当您执行软件在环 (SIL) 或处理器在环 (PIL) 仿真、生成代码或使用外部模式时，软件自动选择 `codegen` 分支。请参阅 Switch Between Choices for Simulation and Code Generation Workflows Without Using Control Variables in Variant Blocks。

有关变体控制模式的更多信息，请参阅 Introduction to Variant Controls。有关不同类型的变体控制模式之间的比较，请参阅 Compare Different Types of Variant Control Modes in Variant Blocks。

#### 依赖关系

不同变体激活时间的可用性取决于您指定的 **Variant control mode** 类型。**Variant activation time** 参数确定软件设置活动选择的时间。该参数还确定生成的代码中包含哪些可变性。下表说明了每种变体控制模式支持的变体激活时间。

| **Variant activation time** | | | | |  |
| --- | --- | --- | --- | --- | --- |
| **Variant control mode** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` | `runtime`（仅 Variant Subsystem 模块） |
| `expression` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `label` | ✓ | x | x | x | x |
| `sim codegen switching` | ✓ | ✓ | x | x | x |

#### 编程用法

|  |
| --- |
| **模块参数：** `VariantControlMode` |
| **类型：** character vector |
| **值：** `'expression'` | `'label'` | `'sim codegen switching'` |
| **默认：** `'expression'` |

### **Variant activation time** — 软件选择活动变体选择的时间 `update diagram`（默认）| `update diagram analyze all choices` | `code compile` | `startup` | `runtime` | `inherit from Simulink.VariantControl`

此参数确定在仿真和代码生成工作流中包含哪些可变性。有关更多信息，请参阅 Activate Variant During Different Stages of Simulation and Code Generation Workflow。

- `update diagram` — 当您执行模型时，仿真和代码生成工作流中仅包含活动选择。生成的代码仅包含活动选择。
- `update diagram analyze all choices` — 当您执行模型时，会分析活动和非活动选择在整个模型中的一致性。但是，仿真和代码生成工作流中仅包含活动选择。生成的代码仅包含活动选择。
- `code compile` — 当您执行模型时，会分析活动和非活动选择在整个模型中的一致性，并且所有选择都包含在仿真和代码生成工作流中。生成的代码包含活动和非活动选择，二者由预处理器条件 `#if` 和 `#elif` 包围。但是，从生成的代码构建的可执行文件仅包含活动选择。
- `startup` — 当您执行模型时，会分析活动和非活动选择在整个模型中的一致性，并且所有选择都包含在仿真和代码生成工作流中。使用此选项，您可以使用快速重启提高迭代仿真的速度。有关更多信息，请参阅 Run Iterative Simulations Without Recompiling Model for Variant Systems Using Fast Restart。从模型生成的代码包含活动和非活动选择，二者由常规 `if` 条件包围。从生成的代码构建的可执行文件也包含活动和非活动选择。
- `runtime` — 当您执行模型时，活动变体可以在仿真期间或生成的代码执行期间通过使用 Parameter Writer 模块进行切换。将 Parameter Writer 模块放在条件执行子系统内，或放在 Initialize Function 模块、Reinitialize Function 模块或 Reset Function 模块中。有关这些模块的更多信息，请参阅 Event Functions。您可以使用 Parameter Writer 模块写入模块参数、模型工作区变量和基础工作区变量。`runtime` 激活时间不支持多个变体控制变量。Parameter Writer 模块支持的所有建模模式对运行时激活都有效。有关更多信息，请参阅 Common Uses of Parameter Writer Block。

  当您将 Variant Subsystem 模块的 **Variant activation time** 参数设置为 `runtime` 时，非活动变体选择的颜色不会淡化。在这种情况下，Simulink Editor 的 **Debug** 选项卡上的 **Information Overlays** 菜单中的 **Variant Fading** 选项的设置将被忽略。
- `inherit from Simulink.VariantControl` — 当您执行模型时，模块从其类型为 `Simulink.VariantControl` 的变体控制变量继承激活时间。如果变体模块具有多个类型为 `Simulink.VariantControl` 的变体控制变量，则所有这些变量必须具有相同的激活时间。

下表基于条件代码、变体切换、状态处理和快速重启支持来比较不同的变体激活时间。

|  | `update diagram` 或 `update diagram analyze all choices` | `code compile` | `startup` | `runtime` |
| --- | --- | --- | --- | --- |
| **生成的条件代码** | 非活动条件代码不可用。 | 条件代码存在于预处理器宏内。编译生成的代码时，非活动选择的代码会被消除。 | 条件代码作为 `if-elseif-else` 语句的一部分生成。变体控制变量值在执行期间不能修改。 | 条件代码作为 `if-elseif-else` 语句的一部分生成。变体控制变量值在执行期间可以修改。 |
| **仿真或代码执行期间的变体切换** | 不支持。 | 不支持。 | 在启动时支持（在仿真开始前 *t* = 0）。 | 支持。通过使用 Parameter Writer 模块更改变体控制变量来切换活动变体。 |
| **显式设置状态的保持或重置选项** | 不支持。非活动模块的状态会重置。 | 不支持。非活动模块的状态会重置 | 仿真期间不能更改状态。在生成的代码中，如果您尝试更改变体，状态处于保持状态。 | 默认情况下状态保持。通过 State Writer 模块显式重置状态。使用 State Reader 模块读取带状态的模块，并使用 State Writer 模块将其转移到另一个选择。 |
| **可执行文件大小** | 较小。不会为非活动变体生成代码。 | 较小。编译期间会移除非活动变体代码。 | 相对较大。活动和非活动变体代码都可用于启动时切换。 | 相对较大。活动和非活动变体代码都可用于运行时切换。 |
| **快速重启支持** | 不支持。 | 不支持。 | 支持。 | 支持。 |

#### 依赖关系

- 不同变体激活时间的可用性取决于您指定的变体控制模式类型。**Variant activation time** 参数确定软件何时设置活动选择。该参数还确定生成的代码中包含哪些可变性。下表说明了每种变体控制模式支持的变体激活时间。

  | **Variant activation time** | | | | |  |
  | --- | --- | --- | --- | --- | --- |
  | **Variant control mode** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` | `runtime` |
  | `expression` | ✓ | ✓ | ✓ | ✓ | ✓ |
  | `label` | ✓ | x | x | x | x |
  | `sim codegen switching` | ✓ | ✓ | x | x | x |
- 要使用 `runtime` 激活时间启用 Variant Subsystem 模块活动变体选择的切换，必须使用 Parameter Writer 模块。根据变体控制变量的位置设置 Parameter Writer 模块的 **Destination** 参数，并选择 **Validate parameter** :

  - `Block parameter` — 控制变量是子系统中的掩码参数。
  - `Model workspace variable` — 控制变量位于模型工作区中。
  - `Base workspace variable` — 控制变量位于基础工作区或数据字典中。

  例如，您可以在子系统中创建掩码参数 `V`，并在变体控制的变体条件表达式中使用它。Parameter Writer 模块写入变体控制条件中 `V` 的值。

#### 编程用法

|  |
| --- |
| **模块参数：** `VariantActivationTime` |
| **类型：** character vector |
| **值：** `'update diagram'` | `'update diagram analyze all choices'` | `'code compile'` | `'startup'`| `'runtime'` |
| **默认：** `'update diagram'` |

### **Variant control variable** — 确定活动变体选择的变量 `Simulink.VariantControl` object | scalar variable | `Simulink.Parameter` object | `struct`

当您指定 Types of Variant Control Variables (Operands) in Variant Blocks 中列出的类型的变量时，软件会为 Variant Assembly Subsystem 模块的变体选择生成变体控制表达式。您在此指定的 **Variant control variable** 位于生成的表达式的左侧，**Variant enumeration choice** 的成员位于右侧。两侧通过 `==` 关联。

变体控制变量充当开关，用于更改活动变体选择。您为变体控制变量指定一个值并运行仿真。在仿真期间，软件对变体控制表达式求值，以确定活动变体选择。当表达式求值为 `true` 时，对应的变体选择被设置为活动。要更改活动变体，请更改变体控制变量的值，使对应的变体控制表达式求值为 `true` 的选择变为活动。

#### 依赖关系

此参数仅在 Variant Assembly Subsystem 模块中可用。要启用此参数，请将 **Variant control mode** 设置为 `expression`。

#### 编程用法

|  |
| --- |
| **模块参数：** `VariantControlVariable` |
| **类型：** character vector |
| **值：** `Simulink.VariantControl` object, scalar variable, `Simulink.Parameter` object, `struct` |
| **默认：** `''` |

### **Variant choices enumeration** — 枚举类，用于添加变体选择枚举类，其成员为模型或子系统文件名

要将 Model 或 Subsystem Reference 模块作为变体选择添加到 Variant Assembly Subsystem 模块，请指定一个枚举类名称，该枚举类包含对应的模型或子系统文件名作为其成员。然后，您可以使用 **Variant choices** 表中的 Refresh 按钮验证该枚举类。验证成功后，该枚举类的成员将作为变体选择添加到 Variant Assembly Subsystem 模块。每个选择都有一个变体控制表达式，其左侧为 **Variant control variable**，右侧为您在此指定的 **Variant choices enumeration** 的成员。表达式的两侧通过 `==` 关联。新添加的变体选择及其对应的控制表达式将显示在 **Variant choices** 表中。

要从 Variant Assembly Subsystem 模块中移除变体选择，请从您在此指定的枚举类中移除对应成员。您无法从 Variant Assembly Subsystem 模块内部管理变体选择。

您指定的枚举类必须位于当前 MATLAB® 会话的搜索路径中。有关如何将文件或文件夹添加到搜索路径的信息，请参阅 `addpath`。

有关如何使用 **Variant choices enumeration** 参数添加选择的更多信息，请参阅 Add or Remove Variant Choices of Variant Assembly Subsystem Blocks Using External Files。

#### 依赖关系

此参数仅在 Variant Assembly Subsystem 模块中可用。要启用此参数，请将 **Variant control mode** 设置为 `expression`。

#### 编程用法

|  |
| --- |
| **模块参数：** `VariantChoicesEnumeration` |
| **类型：** character vector |
| **值：** 使用 `classdef` 或 `Simulink.defineIntEnumType` 定义的枚举类 |
| **默认：** `''` |

### **变体选择指定符** — 用于添加变体选择的 MATLAB 表达式，任何计算结果为模型或子系统文件名的一维元胞数组的 MATLAB 表达式，或与模型或子系统文件名匹配的文件名模式，或字符串数组

要将 Model 或 Subsystem Reference 模块作为变体选择添加到 Variant Assembly Subsystem 模块，请指定对应的模型或子系统文件名。这些文件名必须指定为一个 MATLAB 表达式，该表达式在求值时返回一维字符向量元胞数组，或指定为字符串数组。然后，可以使用 **变体选择**表中的 Refresh 按钮验证该表达式。验证成功后，与指定文件对应的模块将作为变体选择添加到 Variant Assembly Subsystem 模块。对于每个选择，会生成一个变体控制标签。变体控制标签的名称与选择名称相同。新添加的变体选择及其对应的控制标签将显示在 **变体选择**表中。

要从 Variant Assembly Subsystem 模块中删除变体选择，请修改此参数中指定的表达式。无法从 Variant Assembly Subsystem 模块内部管理该模块的变体选择。

指定的 MATLAB 表达式必须包含以下任一项：

- 位于当前 MATLAB 会话搜索路径上的模型或子系统文件名。例如，如果将 `{'model1.slx', 'subsystemRef1.slx'}` 指定为指定符，则与 `model1.slx` 和 `subsystemRef1.slx` 文件对应的模块将作为 Variant Assembly Subsystem 模块的变体选择添加。
- 与 MATLAB 路径上的模型或子系统文件名匹配的文件名模式。模式中的路径可以是绝对路径，也可以是相对于包含 Variant Assembly Subsystem 模块的模型的父文件夹的路径。例如，如果将 `{'folder_1/*.slx', 'folder_2/*.slx'}` 指定为指定符，软件会将字符向量 `folder_1/*` 和 `folder2/*` 传递给 `dir` 函数。然后该函数返回位于 `folder1` 和 `folder2` 文件夹内的模型和子系统文件。与返回文件对应的模块将作为 Variant Assembly Subsystem 模块的变体选择添加。

有关如何将文件或文件夹添加到搜索路径的信息，请参阅 `addpath`。

有关如何在 **变体选择指定符** 参数中指定选择的详细信息，请参阅使用外部文件添加或删除 Variant Assembly Subsystem 模块的变体选择。

#### 依赖关系

此参数仅在 Variant Assembly Subsystem 模块中可用。要启用此参数，请将 **变体控制模式** 设置为 `label`。

#### 编程用法

|  |
| --- |
| **参数：** `VariantChoicesSpecifier` |
| **类型：** character vector |
| **值：** 任何计算结果为文件名或文件名模式的一维元胞数组的 MATLAB 表达式。 |
| **默认：** `''` |

### **变体选择** — 变体选择、变体控制和条件的表格，空表（默认）

该表格为变体子系统中包含的每个变体选择提供一行。如果没有变体选择，则该表格为空。

可以使用 **变体选择**表左侧的按钮修改表中的元素。

| 要... | 单击... |
| --- | --- |
| **创建并添加新的子系统选择**：创建一个新的 Subsystem 模块作为变体选择，并在表中为新选择添加一个条目。 | Create and add a new subsystem choice 按钮 |
| **创建并添加新的模型变体选择**：创建一个新的 Model 模块作为变体选择，并在表中为新选择添加一个条目。 | Create and add a new model variant choice 按钮 |
| **删除选定的变体选择**：永久删除变体选择。 | Delete selected variant choices 按钮 |
| **创建/编辑选定的变体对象**：在全局工作区中创建或编辑 `Simulink.VariantExpression` 对象，并使用 `Simulink.VariantExpression` 对象参数对话框指定变体条件。  **注意**  对于使用基础工作区的模型，此操作会在基础工作区中创建 `Simulink.VariantExpression` 对象，并且该对象仅对当前 MATLAB 会话可用。要永久存储数据，请将该对象保存到 MAT 文件或 MATLAB 脚本中。 | Create or Edit selected variant object 按钮 |
| **打开选定的变体选择模块**：为选定行打开 Subsystem 模块。 | Open selected variant choice block 按钮 |
| **从 Variant Subsystem 内容刷新对话框信息**：根据全局工作区中变体控制的值和变体选择更新 **变体选择**表。 | Refresh dialog information from Variant Subsystem contents 按钮 |

#### 依赖关系

Variant Assembly Subsystem 模块仅允许您使用此部分中的按钮打开选定的变体选择并刷新变体选择列表。要将新的变体选择添加到 Variant Assembly Subsystem 模块，请参阅使用外部文件添加或删除 Variant Assembly Subsystem 模块的变体选择。

### **名称（只读）** — 变体选择名称，只读：`Subsystem` 和 `Subsystem1`（默认）| Variant Subsystem 中包含的选择名称

此参数为只读。

此参数显示选择的名称。每个选择都有一个变体控制，形式为标签、表达式或开关。对于处于 `label` 模式的 Variant Assembly Subsystem，没有单独的变体控制可用。选择名称用作变体控制以设置活动选择。

### **变体控制标签** — `label` 模式中的选择名称，`true` 或 `false`（默认）| string

为选择指定的名称，指定为 string。

#### 依赖关系

要启用此参数，请将 **变体控制模式** 设置为 `label`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VariantControl` |
| **值：** | 与变体选择关联的变体控制 |
| **数据类型：** | `char` |

**示例：** `set_param(gcb, 'VariantControl', 'V == 3')`，其中 `gcb` 是 Variant Subsystem 模块的变体选择。

**示例：** `get_param(gcb, 'VariantControl')`，其中 `gcb` 是 Variant Subsystem 模块的变体选择。

### **变体控制开关** — 用于仿真和代码生成工作流的变体选择 `(sim)` | `(codegen)`

指定 `(sim)` 以在仿真期间激活对应的变体选择。指定 `(codegen)` 以在执行代码生成工作流（如 SIL、PIL、外部模式等）期间激活对应的变体选择。

#### 依赖关系

要启用此参数，请将 **变体控制模式** 设置为 `sim codegen switching`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VariantControl` |
| **值：** | 与变体选择关联的变体控制 |
| **数据类型：** | `char` |

**示例：** `set_param(gcb, 'VariantControl', '(sim)')`，其中 `gcb` 是 Variant Subsystem 模块的变体选择。

**示例：** `get_param(gcb, 'VariantControl')`，其中 `gcb` 是 Variant Subsystem 模块的变体选择。

### **变体控制表达式** — 确定活动选择的条件表达式 `true` 或 `false`（默认）| 布尔条件表达式 | 表示布尔条件表达式的 `Simulink.VariantExpression` 对象 | `(default)`

指定条件表达式以确定活动选择。当条件表达式求值为 `true` 时，软件激活对应的变体选择。当条件表达式求值为 `false` 时，软件停用对应的变体选择。

变体控制可以是：

- 用于快速原型化的布尔条件表达式。例如 `A == 1`、`A ~= B`、`A && B == 1` 等。
- 包含条件表达式以实现条件重用的 `Simulink.VariantExpression` 对象。请参阅 Simulink.VariantExpression 对象以实现 Variant Blocks 的变体条件重用。
- 如果没有任何选择求值为 `true`，则为默认变体选择。

这里，`A` 和 `B` 是称为 *变体控制变量* 的操作数。`==`、`~=` 和 `&&` 是条件表达式中的运算符。条件表达式可以包含一个或多个此类变体控制变量和运算符。有关变体控制变量支持的类型和存储位置的信息，请参阅 Variant Blocks 中变体控制变量（操作数）的类型和 Variant Blocks 中变体控制变量（操作数）的存储位置。有关运算符的信息，请参阅不同激活时间的 Variant Blocks 中的运算符类型。

有关详细信息，请参阅使用条件表达式在 Variant Blocks 中的选择之间切换。

在 Variant Assembly Subsystem 模块中，此参数是自动生成的布尔表达式列表，**变体控制变量** 位于表达式左侧，**变体枚举选择** 的成员位于表达式右侧。表达式的两侧通过 `==` 连接。此参数为只读。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

Variant Subsystem 模块：

|  |  |
| --- | --- |
| **参数：** | `VariantControl` |
| **值：** | 与变体选择关联的变体控制 |
| **数据类型：** | `char` |

**示例：** `set_param(gcb, 'VariantControl', 'V == 3')`，其中 `gcb` 是 Variant Subsystem 模块的变体选择。

**示例：** `get_param(gcb, 'VariantControl')`，其中 `gcb` 是 Variant Subsystem 模块的变体选择。

Variant Source 和 Variant Sink 模块：

|  |  |
| --- | --- |
| **参数：** | `VariantControls` |
| **值：** | 与变体选择关联的变体控制 |
| **数据类型：** | `char` |

**示例：** `set_param(gcb, 'VariantControls', {'A == 1','A == 2'})`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

**示例：** `get_param(gcb, 'VariantControls')`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

### **条件（只读）** — `Simulink.VariantExpression` 对象中的条件表达式，只读：`N/A`（默认）

此参数为只读。

此参数显示指定为 `Simulink.VariantExpression` 对象的条件表达式。要更改或编辑条件表达式，请使用在工作区中双击该对象时出现的 `Simulink.VariantExpression` 参数对话框。

**注意**

在类型为 `Simulink.VariantExpression` 的条件表达式中指定的操作数必须定义在基础工作区或数据字典中。不支持指定在掩码或模型工作区中定义的操作数。

### **标签模式活动选择** — `label` 模式中的活动选择名称，`true (Subsystem)`（默认）| `false (Subsystem1)`

此列表包含所有变体选择的标签。要设置活动选择，请从列表中选择一个标签。对应选择将变为活动状态。或者，要更改标签模式中的活动选择，可以按照使用变体控制标签设置活动选择中所述的方法操作。

#### 依赖关系

要启用此参数，请将 **变体控制模式** 设置为 `label`。

#### 编程用法

|  |
| --- |
| **参数：** `LabelModeActiveChoice` |
| **类型：** character vector |
| **值：** 如果未指定标签模式活动选择，则该值为空。如果指定了标签模式活动选择，则该值为活动选择的变体控制标签。 |
| **默认：** `''` |

### **内置空选择** — 如果没有活动的变体选择，则输出零 `off`（默认）| `on`

- `off` — 当没有活动的变体选择时，Simulink 生成错误。
- `on` — 当选择此选项时，Simulink 会向 **变体选择**表添加一个不可修改的变体选择条目，其变体控制设置为 `(default)`。此条目不会在 Variant Subsystem 模块中显示为可见的变体选择。在仿真期间，如果没有活动的变体选择，Simulink 会断开 Variant Subsystem 模块的变体选择，从而从模型中完全移除变体区域。该子系统的非活动输出端口输出零。要输出零以外的值，请选择 Outport 模块的 **当源未连接时指定输出** 参数，并指定您选择的值。

有关详细信息，请参阅管理变体组件以从没有活动选择的非活动变体子系统传递指定值 (Simulink Coder)。

#### 依赖关系

仅当 Variant Subsystem 中没有 `default` 变体选择，并且将 **变体控制模式** 设置为 `expression` 时，此参数才可用。

#### 编程用法

|  |
| --- |
| **参数：** `EmptyChoice` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **内置直通选择** — 如果没有活动的变体选择，则将输入端口值分配给输出端口 `off`（默认）| `on`

- `off` — 当没有活动的变体选择时，Simulink 生成错误。
- `on` — 当选择此选项时，Simulink 会向 **变体选择**表添加一个不可修改的变体选择条目，其变体控制设置为 `(default)`。此条目不会在 Variant Subsystem 模块中显示为可见的变体选择。在仿真期间，如果没有活动的变体选择，Simulink 会绕过 Variant Subsystem 模块的变体选择。只有输入和输出端口保持活动，输入端口将值直接传递到输出端口。

  当没有选择处于活动状态时，要将值从输入端口映射到输出端口，Variant Subsystem 模块必须具有：

  - 仅数据端口，没有其他类型的输入和输出端口
  - 相同数量的数据输入和输出端口
  - 与变体选择的端口完全匹配的输入和输出端口

有关详细信息，请参阅管理变体组件以从没有活动选择的非活动变体子系统传递指定值 (Simulink Coder)。

#### 依赖关系

仅当 Variant Subsystem 中没有 `default` 变体选择，并且将 **变体控制模式** 设置为 `expression` 时，此参数才可用。

#### 编程用法

|  |
| --- |
| **参数：** `PassThrough` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **在 Variant Subsystem 外部传播条件** — 用于选择是否必须将底层模块的活动和非活动状态告知 Variant Subsystem 外部的组件 `off`（默认）| `on`

当你选择 **在 Variant Subsystem 外部传播条件** 参数时，软件会将底层模块的变体条件传播到 Variant Subsystem 容器模块，以便子系统可以调整其接口以适应底层模块的状态。映射到活动选择端口的端口变为活动状态。未映射到非活动选择端口的端口变为非活动状态。选择此选项可确保 Variant Subsystem 外部的组件了解 Variant Subsystem 模块内模块的活动和非活动状态。有关详细信息，请参阅将变体条件传播到 Variant Subsystems 外部以定义变体区域，从而提升一致性并减少错误和传播变体条件以控制条件子系统的执行

如果模块内所有变体选择具有相同接口，变体条件不会传播到 Variant Subsystem 模块外部。

#### 编程使用

|  |
| --- |
| **参数：** `PropagateVariantConditions` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **允许灵活接口** — 用于选择使变体子系统的接口灵活 `on`（默认）| `off`

指定是否使变体子系统的接口灵活。

- `on` — 使用其输入和输出端口数量与 Variant Subsystem 模块的输入和输出端口不同的变体选择进行仿真。
- `off` — 使用此选项进行仿真时，如果接口不一致，软件将生成错误，并提供修复操作，使变体选择的端口与 Variant Subsystem 模块匹配。

#### 编程使用

|  |
| --- |
| **参数：** `AllowFlexibleInterface` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'on'` |

## 所属库

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `no` |
| **多维信号** | `yesa` |
| **可变大小信号** | `yesa` |
| **零交叉检测** | `no` |
|  |  |
| --- | --- |
| a 实际数据类型或功能支持取决于模块实现。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。实际数据类型或功能支持取决于模块实现。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `Module`（默认） | 为子系统及子系统内的模块生成代码。HDL Coder 为所有变体选择生成代码。 |
| `BlackBox` | 生成黑盒接口。也就是说，生成的 HDL 代码仅包含子系统的输入/输出端口定义。这样，你可以在模型中使用子系统来生成到现有手动编写的 HDL 代码的接口。为子系统生成的黑盒接口与为 Model 模块生成的接口类似，但不生成时钟信号。 |
| `No HDL` | 从生成的代码中移除子系统。你可以在仿真中使用该子系统，但在 HDL 代码中将其视为“空操作”。 |

**黑盒接口自定义**

对于 `BlackBox` 架构，你可以自定义端口名称并设置外部组件接口的属性。请参阅自定义黑盒或 HDL Cosimulation 接口 (HDL Coder)。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **AdaptivePipelining** | 根据综合工具、目标频率和乘法器字长自动插入流水线。默认值为 `inherit`。另请参阅 AdaptivePipelining (HDL Coder)。 |
| **BalanceDelays** | 检测沿一条路径引入的新延迟，并在其他路径上插入匹配延迟。默认值为 `inherit`。另请参阅 BalanceDelays (HDL Coder)。 |
| **ClockRatePipelining** | 以更快的时钟速率而不是较慢的数据速率插入流水线寄存器。默认值为 `inherit`。另请参阅 ClockRatePipelining (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分布，或寄存器重定时。默认值为 `inherit`。另请参阅 DistributedPipelining (HDL Coder)。 |
| **DSPStyle** | 用于乘法器映射的综合属性。默认值为 `none`。另请参阅 DSPStyle (HDL Coder)。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中移除子系统层次结构。默认值为 `inherit`。另请参阅 FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的等效功能资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |
| **StreamingFactor** | 并行数据路径（或向量）的数量，这些路径经过时间复用转换为串行标量数据路径。默认值为 0，表示实现完全并行的数据路径。另请参阅 Streaming (HDL Coder)。 |

**目标规范**

此模块不能是 DUT，因此 **目标规范** 选项卡中的模块属性设置会被忽略。

**限制**

- Variant Subsystem 不能是受测设计 (DUT)。
- **变体激活时间** 参数必须设置为 `update diagram`、`update diagram analyze all choices` 或 `startup`。
- 对于 Variant Subsystem 的 Outport 模块，必须禁用 **指定源未连接时的输出** 参数。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型或功能支持取决于模块实现。

## 版本历史

**在 R2010b 中引入**

### R2025a：通过抑制非活动变体选择和已注释模块的回调，减少开销和不相关诊断消息

回调 `LoadFcn`、`ContinueFcn`、`InitFcn`、`ModelCloseFcn`、`PauseFcn`、`PostSaveFcn`、`PreSaveFcn`、`StartFcn` 和 `StopFcn` 不会针对具有 `update diagram` 激活时间的 Variant Subsystem 模块中的非活动变体选择以及已注释模块执行。这种抑制可减少计算开销，并防止不影响当前模型迭代的模块产生不必要的诊断消息。但是，对于已注释或非活动的 Model 模块或 Subsystem Reference 模块内部的模型或子系统文件中的模块，这些回调不会被抑制。此外，封装初始化和封装参数回调不会被抑制。有关适用回调的列表，请参阅 Author Mask Initialization and Callbacks 和 Mask Parameters。

### R2025a：当不存在变体选择时输出零的参数从 **允许零活动变体控制** 重命名

**允许零活动变体控制** 参数现已重命名为 **内置空选择**。这个新参数保留了以前的功能：在没有变体选择处于活动状态时移除变体组件并输出零。

### R2025a：当不存在变体选择时将输入值分配给输出端口

使用 **内置直通选择** 参数绕过变体区域，并在没有变体选择处于活动状态时将输入值分配给输出端口。

### R2024b：`runtime` 激活时间：在仿真或代码生成期间更改活动选择

从 R2024b 开始，在 Variant Subsystem 模块中使用 `runtime` 变体激活时间，可以通过 Parameter Writer 模块在仿真或代码生成期间更改活动变体。你可以对 Parameter Writer 模块可写入全局工作区、封装工作区或模型工作区中的变体控制变量的所有场景进行建模。

### R2024a：自动端口同步

Simulink 提供选项，用于在 Variant Subsystem 和 Variant Assembly Subsystem 模块中添加缺失端口并删除未使用端口，以匹配底层变体选择的端口。在仿真期间，如果 Simulink 遇到 Variant Subsystem 或 Variant Assembly Subsystem 模块与其变体选择之间的端口不匹配，生成的错误消息会提供添加缺失端口和删除未使用端口的选项来解决该问题。

### R2024a：使用自适应速率模型模块作为选择

你可以将自适应速率模型模块用作 Variant Subsystem 模块中的变体选择。当你添加自适应速率模型作为变体选择时，变体子系统中的输入端口会与相应速率模型的端口名称匹配。

### R2024a：访问活动变体选择的封装

你可以直接访问 Variant Subsystem 的活动变体选择的封装，而无需导航到 Variant Subsystem 模块内部。

- 如果 Variant Subsystem 模块未封装，双击该模块会打开其活动选择的封装。单击 **查看封装内部** 徽标或从 Variant Subsystem 模块的上下文菜单中选择相应选项，会直接将你带到活动选择内部。
- 如果 Variant Subsystem 模块已封装，并且活动选择也有封装，则双击该模块会打开 Variant Subsystem 封装。
- 如果 Variant Subsystem 模块未封装，并且其活动选择已封装，则双击 **查看封装内部** 徽标会带你到变体层。在活动选择未封装的已封装 Variant Subsystem 模块中，你会看到类似行为。

当你单击链接的 Variant Subsystem 模块的 **查看封装内部** 徽标，且其活动选择是链接且已封装的 Model Reference 模块时，Model Reference 会在单独的编辑器中打开。此外，你必须对活动选择上的活动选择模块的封装参数执行 `set_param` 操作，而不是对 Variant Subsystem 模块执行。

活动选择封装的提升仅限于其直接父级。不支持嵌套 Variant Subsystem 封装提升。

### R2024a：将变体选择指定为字符串数组

你可以在 Variant Assembly Subsystem 模块中将 **变体选择指定符** 指定为字符串数组。

### R2023b：提升活动选择的内容预览

Simulink 会自动提升 Variant Subsystem 模块活动选择的内容预览。当活动选择是未加载的 Model Reference，且当活动选择是 Stateflow 图时，Variant Subsystem 会显示为内容预览。

### R2023b：直接导航到活动选择

你可以通过双击 Variant Subsystem 模块直接导航到活动变体内部。当你从上下文菜单中选择 **在新选项卡中打开** 或 **在新窗口中打开** 时，活动选择会在新选项卡或新窗口中打开。你也可以使用 `open_system` 函数访问变体层和活动选择。

```
open_system(vssBlock)
open_system(vssBlock,'ActiveChoice','window')
```

当活动选择具有 `OpenFcn` 回调时，双击 Variant Subsystem 模块不会执行该回调。此外，如果活动选择是未加载的引用模型，双击 Variant Subsystem 不会导航到活动选择。

### R2021a：自动提升活动变体的封装图标

Simulink 会自动在父级 Variant Subsystem 上显示活动变体模块的封装图标。在 R2021a 之前，你必须在 Variant Subsystem 的封装上提供图标绘制命令，才能显示底层活动变体模块的封装图标。

## 描述

包含 Subsystem 模块作为变体选择的模板子系统

Variant Subsystem 模块使您能够将组件的多个实现包含在单独的层次结构中。

例如，假设您要仿真一个表示具有三种可能发动机配置的车辆的模型：2 缸汽油、4 缸汽油和 8 缸汽油。您可以将每个发动机模型实现为 Variant Subsystem 模块内的单独子系统，然后根据您选择的 Variant Blocks 中的变体控制模式类型在子系统之间切换。有关详细信息，请参阅变体控制简介。

**注意**

在仿真期间，Variant Subsystem 模块只有一个实现处于活动状态。

Variant Subsystem 模块内发动机的多个模型

Variant Subsystem 模块是一个模板，预配置为包含两个或多个模块以用作变体选择。这些选择表示系统的多个实现。在模型执行期间，只有一个子模块处于活动状态。活动子模块称为 *活动变体*。

Variant Subsystem 模块内的每个变体选择都与 **Variant control mode** 和 **Variant activation time** 关联。变体控制模式确定如何选择活动变体。变体激活时间确定激活选择的时间，并决定在生成的代码中是仅包含活动选择，还是同时包含活动选择和非活动选择。

Variant Subsystem 模块可以包含 Subsystem 模块、Model 模块或 Subsystem Reference 模块的混合作为变体选择。仅包含 Model 模块作为选择的 Variant Subsystem 模块称为 Variant Model 模块。有关详细信息，请参阅使用 Variant Subsystems 在单独层次结构中实现变体。包含 Model 或 Subsystem Reference 模块作为选择，且这些选择只能从外部文件添加或移除而不能在模块内添加或移除的 Variant Subsystem 模块称为 Variant Assembly Subsystem 模块。

除了变体选择之外，您还可以在 Variant Subsystem 模块内包含 Inport、控制端口（Enable、Trigger、Reset 和 Function-Call Subsystem）、Outport 或 Connection Port (Simscape) 模块。Variant Subsystem 模块内部的模块之间没有绘制的连接。在模型编译期间，软件会自动将活动变体连接到 Variant Subsystem 的 Inport 和 Outport 模块。表示变体选择的模块可以具有与父 Variant Subsystem 模块中的输入和输出端口数量不同的输入和输出端口。有关详细信息，请参阅映射 Variant Subsystem 中变体选择的输入和输出端口。

当您加载包含 Variant Subsystem 模块且其变体选择存储在子系统文件中的模型时，默认情况下，仅加载活动选择以优化模型的加载时间。但是，如果您使用 `find_system`、`get_param` 或 `set_param` 函数以编程方式初始化模型，则可能会加载非活动选择。

使用 Variant Subsystem 模块允许您：

- 将 Subsystem、Model 和 Subsystem Reference 模块混合作为变体选择。
- 对不具有相似接口的组件建模。您可以为 Variant Subsystem 内的多个变体选择设置不同数量的输入端口和输出端口。但是，必须满足映射 Variant Subsystem 中变体选择的输入和输出端口中列出的条件。
- 建立分层模块图，其中 Variant Subsystem 模块位于一层，变体选择位于另一层。
- 将功能相关的模块保持在一起。
- 降低模型的复杂度。
- 在模型编译期间，软件会根据您选择的变体激活时间消除整个模型中的非活动模块。

模块图标上变体徽章的颜色和图标取决于在该模块上设置的 **Variant activation time**、**Variant control mode** 和 **Propagate conditions outside of variant subsystem** 参数的值。有关详细信息，请参阅变体徽章。

### 打开模块

您可以从 Simulink® 界面或以编程方式打开 Variant Subsystem 模块。根据您的需求，这些方法使您能够访问 Variant Subsystem 模块的活动变体选择或整个变体层。

**从 Simulink 界面打开**

使用 Simulink 界面中的以下任一操作打开 Variant Subsystem 模块。

| 键盘和鼠标操作 | 结果 |
| --- | --- |
| 双击 | 在新选项卡中打开模块内的活动变体选择  **注意**  如果变体选择是 Model 模块且其引用的模型未加载，则双击该模块会打开包含变体选择的变体层，而不是打开活动变体选择的底层。 |
| 按住 **Ctrl** 并双击 | 在新选项卡中打开模块，显示变体层 |
| 按住 **Shift** 并双击 | 在新窗口中打开模块，显示变体层 |
| 右键单击，选择 **打开** > **在新选项卡中打开** | 在当前窗口中打开模块，显示变体层 |
| 右键单击，选择 **打开** > **在新窗口中打开** | 在新窗口中打开模块，显示变体层 |
| 右键单击变体徽章，选择 **打开** > **(活动变体)** | 在新选项卡中打开活动变体选择 |
| 右键单击变体徽章，选择 **打开** > **variant control (variant choice name)**，其中 *`variant control`* 是用于由 *`variant choice name`* 指定的变体选择的变体控制 `expression`、`label` 或 `(sim)` 或 `(codegen)`。 | 在新选项卡中打开所选的变体选择 |

**以编程方式打开**

使用以下任一命令打开 Variant Subsystem 模块，其中 *`variantSubsystemBlockName`* 是模块名称：

- `open_system("variantSubsystemBlockName")`
  命令 — 打开 Variant Subsystem 模块并查看其变体层。
- `open_system("variantSubsystemBlockName","ActiveChoice")`
  — 打开 Variant Subsystem 模块内的活动变体选择。

有关使用 `open_system` 命令打开 Variant Subsystem 模块的其他选项（例如在新选项卡或窗口中打开）的信息，请参阅 `open_system`。
