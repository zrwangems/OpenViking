---
type: simulink-block
title: 'Variant Subsystem'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'variantsubsystem'
documentation_source_path: 'slref/variantsubsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Variant Subsystem

## 端口
```yaml
ports:
- name: In_1
  summary: 与变体子系统中根级 Inport 模块对应的输入端口，接受与 Inport 模块相同的数据类型
  direction: input
- name: Out_1
  summary: 与变体子系统中包含的根级 Outport 模块对应的输出端口，接受与 Outport 模块相同的数据类型
  direction: output
```

### 输入

### **In\_1** — 与变体子系统中根级 Inport 模块对应的输入端口，接受与 Inport 模块相同的数据类型

Variant Subsystem 中包含的每个 Subsystem、Model 或 Subsystem Reference 模块代表一个变体选择。变体选择可以在其输入端包含 Inport、控制端口（Enable、Trigger、Reset 和 Function-Call Subsystem）或 Connection Port（Simscape）模块。变体选择的输入端口数量可以与父 Variant Subsystem 模块的输入端口数量不同。但是，必须满足 Map Input and Output Ports of Variant Choices in Variant Subsystem 中描述的条件。
### 输出

### **Out\_1** — 与变体子系统中包含的根级 Outport 模块对应的输出端口，接受与 Outport 模块相同的数据类型

Variant Subsystem 中包含的每个 Subsystem、Model 或 Subsystem Reference 模块代表一个变体选择。变体选择可以在其输出端包含 Outport 或 Connection Port（Simscape）模块。变体选择的输出端口数量可以与父 Variant Subsystem 模块的输出端口数量不同。但是，必须满足 Map Input and Output Ports of Variant Choices in Variant Subsystem 中描述的条件。

Variant Subsystem 模块的未连接输出端口（非活动输出端口）输出接地值。要输出接地值以外的值，请选择 Outport 模块的 **Specify output when source is unconnected** 参数并指定一个值。
## 参数
```yaml
parameters:
- name: Variant control mode
  summary: 变体控制模式 expression（默认）| label | sim codegen switching
  group: ''
  block_parameter: VariantControlMode
  type: character vector
  values: '''expression'' | ''label'' | ''sim codegen switching'''
  default: '''expression'''
- name: Variant activation time
  summary: 软件选择活动变体选择的时间 update diagram（默认）| update diagram analyze all choices | code compile | startup | runtime | inherit
    from Simulink.VariantControl
  group: ''
  block_parameter: VariantActivationTime
  type: character vector
  values: '''update diagram'' | ''update diagram analyze all choices'' | ''code compile'' | ''startup''| ''runtime'''
  default: '''update diagram'''
- name: Variant control variable
  summary: 用于确定活动变体选择的变量 Simulink.VariantControl 对象 | 标量变量 | Simulink.Parameter 对象 | struct
  group: ''
  block_parameter: VariantControlVariable
  type: character vector
  values: Simulink.VariantControl 对象、标量变量、Simulink.Parameter 对象、struct
  default: ''''''
- name: Variant choices enumeration
  summary: 用于添加变体选择的枚举类，以模型或子系统文件名作为其成员
  group: ''
  block_parameter: VariantChoicesEnumeration
  type: character vector
  values: 使用 classdef 或 Simulink.defineIntEnumType 定义的枚举类
  default: ''''''
- name: Variant choices specifier
  summary: 用于添加变体选项的 MATLAB 表达式，可以是任何求值为一维元胞数组的 MATLAB 表达式，该数组包含模型或子系统文件名，或与模型或子系统文件名匹配的文件名模式，也可以是字符串数组
  group: ''
  block_parameter: VariantChoicesSpecifier
  type: character vector
  values: 任何求值为一维文件名或文件名模式元胞数组的 MATLAB 表达式。
  default: ''''''
- name: Variant choices
  summary: 变体选项、变体控制和条件表 空表（默认）
  group: ''
- name: Name (read-only)
  summary: 变体选项名称 只读：Subsystem 和 Subsystem1（默认）| Variant Subsystem 中包含的选项名称
  group: ''
- name: Variant control label
  summary: label 模式下的选项名称 true 或 false（默认）| 字符串
  group: ''
  block_parameter: VariantControl
  values: 与变体选项关联的变体控制
- name: Variant control switch
  summary: 用于仿真和代码生成工作流的变体选项 (sim) | (codegen)
  group: ''
  block_parameter: VariantControl
  values: 与变体选项关联的变体控制
- name: Variant control expression
  summary: 确定活动选项的条件表达式 true 或 false（默认）| 布尔条件表达式 | 表示布尔条件表达式的 Simulink.VariantExpression 对象 | (default)
  group: ''
  block_parameter: VariantControls
  values: 与变体选项关联的变体控制
- name: Condition (read-only)
  summary: Simulink.VariantExpression 对象中的条件表达式 只读：N/A（默认）
  group: ''
- name: Label mode active choice
  summary: label 模式下的活动选项名称 true (Subsystem)（默认）| false (Subsystem1)
  group: ''
  block_parameter: LabelModeActiveChoice
  type: character vector
  values: 如果未指定标签模式活动选项，则该值为空。如果指定了标签模式活动选项，则该值为活动选项的变体控制标签。
  default: ''''''
- name: Built-in empty choice
  summary: 如果没有活动变体选项则输出零 off（默认）| on
  group: ''
  block_parameter: EmptyChoice
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Built-in passthrough choice
  summary: 如果没有活动变体选项则将输入端口值赋给输出端口 off（默认）| on
  group: ''
  block_parameter: PassThrough
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Propagate conditions outside of variant subsystem
  summary: 选择是否必须将变体子系统外部的组件告知底层模块的活动和非活动状态的选项 off（默认）| on
  group: ''
  block_parameter: PropagateVariantConditions
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Allow flexible interface
  summary: 选择使变体子系统的接口灵活的选项 on（默认）| off
  group: ''
  block_parameter: AllowFlexibleInterface
  type: character vector
  values: '''off'' | ''on'''
  default: '''on'''
```

要访问这些参数，请右键单击模块图标上的变体徽章，然后选择 **Block Parameters**。有关详细信息，请参阅 Variant Badges。

### **Variant control mode** — 变体控制模式 `expression`（默认）| `label` | `sim codegen switching`

用于确定活动变体选择的变体控制可以是以下任意类型。

- `expression` — 软件根据变体条件的求值结果选择活动变体。当条件表达式求值为 `true` 时，相应的变体选择变为活动状态。当条件表达式求值为 `false` 时，相应的变体选择变为非活动状态。请参阅 Switch Between Choices Using Condition Expressions in Variant Blocks。
- `label` — 软件根据变体的名称选择活动变体。变体控制是一个字符串，不需要在任何工作区中创建任何变量。请参阅 Switch Between Choices Using Labels in Variant Blocks。
- `sim codegen switching` — 在仿真和代码生成工作流之间自动切换变体，无需创建任何工作区变量。当您仿真模型时，软件自动选择 `sim` 分支作为活动选择。同样，当您执行软件在环（SIL）或处理器在环（PIL）仿真、生成代码或使用外部模式时，软件自动选择 `codegen` 分支。请参阅 Switch Between Choices for Simulation and Code Generation Workflows Without Using Control Variables in Variant Blocks。

有关变体控制模式的详细信息，请参阅 Introduction to Variant Controls。有关不同类型变体控制模式之间的比较，请参阅 Compare Different Types of Variant Control Modes in Variant Blocks。

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
| **模块参数**：`VariantControlMode` |
| **类型**：character vector |
| **值**：`'expression'` | `'label'` | `'sim codegen switching'` |
| **默认值**：`'expression'` |

### **Variant activation time** — 软件选择活动变体选择的时间 `update diagram`（默认）| `update diagram analyze all choices` | `code compile` | `startup` | `runtime` | `inherit from Simulink.VariantControl`

此参数确定仿真和代码生成工作流中包含哪些可变性。有关详细信息，请参阅 Activate Variant During Different Stages of Simulation and Code Generation Workflow。

- `update diagram` — 当您执行模型时，只有活动选择包含在仿真和代码生成工作流中。生成的代码仅包含活动选择。
- `update diagram analyze all choices` — 当您执行模型时，活动和非活动选择都会在模型中进行一致性分析。但是，只有活动选择包含在仿真和代码生成工作流中。生成的代码仅包含活动选择。
- `code compile` — 当您执行模型时，活动和非活动选择都会在模型中进行一致性分析，并且所有选择都包含在仿真和代码生成工作流中。生成的代码包含活动和非活动选择，它们被包围在预处理器条件 `#if` 和 `#elif` 中。但是，从生成的代码构建的可执行文件仅包含活动选择。
- `startup` — 当您执行模型时，活动和非活动选择都会在模型中进行一致性分析，并且所有选择都包含在仿真和代码生成工作流中。使用此选项，您可以使用快速重启来提高迭代仿真的速度。有关详细信息，请参阅 Run Iterative Simulations Without Recompiling Model for Variant Systems Using Fast Restart。从模型生成的代码包含活动和非活动选择，它们被包围在常规 `if` 条件中。从生成的代码构建的可执行文件也包含活动和非活动选择。
- `runtime` — 当您执行模型时，活动变体可以在仿真或生成的代码执行期间通过使用 Parameter Writer 模块进行切换。将 Parameter Writer 模块放置在条件执行子系统内，或放置在 Initialize Function 模块、Reinitialize Function 模块或 Reset Function 模块中。有关这些模块的详细信息，请参阅 Event Functions。您可以使用 Parameter Writer 模块写入模块参数、模型工作区变量和基础工作区变量。`runtime` 激活时间不支持多个变体控制变量。Parameter Writer 模块支持的所有建模模式对运行时激活均有效。有关详细信息，请参阅 Common Uses of Parameter Writer Block。

  当您将 Variant Subsystem 模块的 **Variant activation time** 参数设置为 `runtime` 时，非活动变体选择的颜色不会淡化。在这种情况下，Simulink Editor 的 **Debug** 选项卡上 **Information Overlays** 菜单中 **Variant Fading** 选项的设置将被忽略。
- `inherit from Simulink.VariantControl` — 当您执行模型时，模块从其类型为 `Simulink.VariantControl` 的变体控制变量继承激活时间。如果变体模块有多个类型为 `Simulink.VariantControl` 的变体控制变量，则所有这些变量必须具有相同的激活时间。

下表根据条件代码、变体切换、状态处理和快速重启支持比较了不同的变体激活时间。

|  | `update diagram` 或 `update diagram analyze all choices` | `code compile` | `startup` | `runtime` |
| --- | --- | --- | --- | --- |
| **生成的条件代码** | 非活动条件代码不可用。 | 条件代码存在于预处理器宏内。非活动选择代码在生成的代码编译时被消除。 | 条件代码作为 `if-elseif-else` 语句的一部分生成。变体控制变量的值在执行期间不能修改。 | 条件代码作为 `if-elseif-else` 语句的一部分生成。变体控制变量的值在执行期间可以修改。 |
| **仿真或代码执行期间的变体切换** | 不支持。 | 不支持。 | 在启动时支持（仿真开始前 *t* = 0）。 | 支持。通过使用 Parameter Writer 模块更改变体控制变量来切换活动变体。 |
| **显式设置状态的保持或重置选项** | 不支持。非活动模块的状态被重置。 | 不支持。非活动模块的状态被重置。 | 状态在仿真期间不能更改。在生成的代码中，如果您尝试更改变体，状态处于保持状态。 | 状态默认保持。通过 State Writer 模块显式重置状态。使用 State Reader 模块读取带状态的模块，并使用 State Writer 模块传输到另一个选择。 |
| **可执行文件大小** | 较小的尺寸。不会为非活动变体生成代码。 | 较小的尺寸。非活动变体代码在编译期间被移除。 | 相对较大的尺寸。活动和非活动变体代码都可用于启动时切换。 | 相对较大的尺寸。活动和非活动变体代码都可用于运行时切换。 |
| **快速重启支持** | 不支持。 | 不支持。 | 支持。 | 支持。 |

#### 依赖关系

- 不同变体激活时间的可用性取决于您指定的变体控制模式的类型。**Variant activation time** 参数确定软件何时设置活动选择。该参数还确定生成的代码中包含哪些可变性。下表说明了每种变体控制模式支持的变体激活时间。

  | **Variant activation time** | | | | |  |
  | --- | --- | --- | --- | --- | --- |
  | **Variant control mode** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` | `runtime` |
  | `expression` | ✓ | ✓ | ✓ | ✓ | ✓ |
  | `label` | ✓ | x | x | x | x |
  | `sim codegen switching` | ✓ | ✓ | x | x | x |
- 要使用 `runtime` 激活时间启用 Variant Subsystem 模块活动变体选择的切换，您必须使用 Parameter Writer 模块。根据变体控制变量的位置设置 Parameter Writer 模块的 **Destination** 参数，并选择 **Validate parameter**：

  - `Block parameter` — 控制变量是子系统中的掩码参数。
  - `Model workspace variable` — 控制变量位于模型工作区中。
  - `Base workspace variable` — 控制变量位于基础工作区或数据字典中。

  例如，您可以在子系统中创建掩码参数 `V`，并将其用于变体控制的变体条件表达式中。Parameter Writer 模块写入变体控制条件中 `V` 的值。

#### 编程用法

|  |
| --- |
| **模块参数**：`VariantActivationTime` |
| **类型**：character vector |
| **值**：`'update diagram'` | `'update diagram analyze all choices'` | `'code compile'` | `'startup'`| `'runtime'` |
| **默认值**：`'update diagram'` |

### **Variant control variable** — 用于确定活动变体选择的变量 `Simulink.VariantControl` 对象 | 标量变量 | `Simulink.Parameter` 对象 | `struct`

当您指定 Types of Variant Control Variables (Operands) in Variant Blocks 中列出的类型的变量时，软件会为 Variant Assembly Subsystem 模块的变体选择生成变体控制表达式。您在此处指定的 **Variant control variable** 位于左侧，**Variant enumeration choice** 的成员位于生成表达式的右侧。两侧通过 `==` 关联。

变体控制变量充当切换活动变体选择的开关。您为变体控制变量指定一个值并运行仿真。在仿真期间，软件对变体控制表达式求值以确定活动变体选择。当表达式求值为 `true` 时，相应的变体选择被设为活动状态。要更改活动变体，请更改变体控制变量的值，使相应的变体控制表达式求值为 `true` 并变为活动状态。

#### 依赖关系

此参数仅在 Variant Assembly Subsystem 模块中可用。要启用此参数，请将 **Variant control mode** 设置为 `expression`。

#### 编程用法

|  |
| --- |
| **模块参数**：`VariantControlVariable` |
| **类型**：character vector |
| **值**：`Simulink.VariantControl` 对象、标量变量、`Simulink.Parameter` 对象、`struct` |
| **默认值**：`''` |

### **Variant choices enumeration** — 用于添加变体选择的枚举类，以模型或子系统文件名作为其成员

要将 Model 或 Subsystem Reference 模块作为变体选择添加到 Variant Assembly Subsystem 模块，请指定一个枚举类名称，该名称包含相应的模型或子系统文件名作为其成员。然后，您可以使用 **Variant choices** 表中的 Refresh 按钮验证枚举类。验证成功后，枚举类的成员将作为变体选择添加到 Variant Assembly Subsystem 模块。每个选择都有一个变体控制表达式，其左侧为 **Variant control variable**，右侧为您在此处指定的 **Variant choices enumeration** 的成员。表达式的两侧通过 `==` 关联。新添加的变体选择及其相应的控制表达式显示在 **Variant choices** 表中。

要从 Variant Assembly Subsystem 模块中移除变体选择，请从您在此处指定的枚举类中移除相应的成员。您无法从 Variant Assembly Subsystem 模块内部管理变体选择。

您指定的枚举类必须位于当前 MATLAB® 会话的搜索路径上。有关如何将文件或文件夹添加到搜索路径的信息，请参阅 `addpath`。

有关如何使用 **Variant choices enumeration** 参数添加选择的详细信息，请参阅 Add or Remove Variant Choices of Variant Assembly Subsystem Blocks Using External Files。

#### 依赖关系

此参数仅在 Variant Assembly Subsystem 模块中可用。要启用此参数，请将 **Variant control mode** 设置为 `expression`。

#### 编程用法

|  |
| --- |
| **模块参数**：`VariantChoicesEnumeration` |
| **类型**：character vector |
| **值**：使用 `classdef` 或 `Simulink.defineIntEnumType` 定义的枚举类 |
| **默认值**：`''` |

### **Variant choices specifier** — 用于添加变体选项的 MATLAB 表达式，可以是任何求值为一维元胞数组的 MATLAB 表达式，该数组包含模型或子系统文件名，或与模型或子系统文件名匹配的文件名模式，也可以是字符串数组

要将 Model 或 Subsystem Reference 模块作为变体选项添加到 Variant Assembly Subsystem 模块，请指定对应的模型或子系统文件名。文件名必须指定为 MATLAB 表达式，该表达式在求值时返回一维字符向量元胞数组或字符串数组。然后，您可以使用 **Variant choices** 表中的 Refresh 按钮验证该表达式。验证成功后，与指定文件对应的模块将作为变体选项添加到 Variant Assembly Subsystem 模块。对于每个选项，都会生成一个变体控制标签。变体控制标签的名称与选项的名称相同。新添加的变体选项及其对应的控制标签将显示在 **Variant choices** 表中。

要从 Variant Assembly Subsystem 模块中移除变体选项，请修改此参数中指定的表达式。您无法从模块内部管理 Variant Assembly Subsystem 模块的变体选项。

您指定的 MATLAB 表达式必须包含以下任一内容：

- 位于当前 MATLAB 会话搜索路径上的模型或子系统文件名。例如，如果您指定 `{'model1.slx', 'subsystemRef1.slx'}` 作为说明符，则与 `model1.slx` 和 `subsystemRef1.slx` 文件对应的模块将作为 Variant Assembly Subsystem 模块的变体选项添加。
- 与 MATLAB 路径上的模型或子系统文件名匹配的文件名模式。模式中的路径可以是绝对路径，也可以是相对于包含 Variant Assembly Subsystem 模块的模型的父文件夹的相对路径。例如，如果您指定 `{'folder_1/*.slx', 'folder_2/*.slx'}` 作为说明符，软件会将字符向量 `folder_1/*` 和 `folder2/*` 传递给 `dir` 函数。该函数随后返回位于 `folder1` 和 `folder2` 文件夹内的模型和子系统文件。与返回文件对应的模块将作为 Variant Assembly Subsystem 模块的变体选项添加。

有关如何将文件或文件夹添加到搜索路径的信息，请参阅 `addpath`。

有关如何在 **Variant choices specifier** 参数中指定选项的详细信息，请参阅 Add or Remove Variant Choices of Variant Assembly Subsystem Blocks Using External Files。

#### 依赖关系

此参数仅在 Variant Assembly Subsystem 模块中可用。要启用此参数，请将 **Variant control mode** 设置为 `label`。

#### 编程使用

|  |
| --- |
| **Parameter:** `VariantChoicesSpecifier` |
| **类型**：character vector |
| **Value:** 任何求值为一维文件名或文件名模式元胞数组的 MATLAB 表达式。 |
| **默认值**：`''` |

### **Variant choices** — 变体选项、变体控制和条件表 空表（默认）

该表为变体子系统中包含的每个变体选项对应一行。如果没有变体选项，则该表为空。

您可以使用 **Variant choices** 表左侧的按钮来修改表中的元素。

| 要执行的操作... | 点击... |
| --- | --- |
| **创建并添加新的子系统选项**：创建一个新的 Subsystem 模块作为变体选项，并在表中为新选项添加条目。 | Create and add a new subsystem choice 按钮 |
| **创建并添加新的模型变体选项**：创建一个新的 Model 模块作为变体选项，并在表中为新选项添加条目。 | Create and add a new model variant choice 按钮 |
| **删除选定的变体选项**：永久删除变体选项。 | Delete selected variant choices 按钮 |
| **创建/编辑选定的变体对象**：在全局工作区中创建或编辑 `Simulink.VariantExpression` 对象，并使用 `Simulink.VariantExpression` 对象参数对话框指定变体条件。  **注意**  对于使用基础工作区的模型，此操作会在基础工作区中创建 `Simulink.VariantExpression` 对象，该对象仅在当前 MATLAB 会话中可用。要永久存储数据，请将对象保存到 MAT 文件或 MATLAB 脚本中。 | Create or Edit selected variant object 按钮 |
| **打开选定的变体选项模块**：打开所选行对应的 Subsystem 模块。 | Open selected variant choice block 按钮 |
| **从 Variant Subsystem 内容刷新对话框信息**：根据全局工作区中的变体选项和变体控制值更新 **Variant choices** 表。 | Refresh dialog information from Variant Subsystem contents 按钮 |

#### 依赖关系

Variant Assembly Subsystem 模块仅允许您使用本节中的按钮打开选定的变体选项并刷新变体选项列表。要向 Variant Assembly Subsystem 模块添加新的变体选项，请参阅 Add or Remove Variant Choices of Variant Assembly Subsystem Blocks Using External Files。

### **Name (read-only)** — 变体选项名称 只读：`Subsystem` 和 `Subsystem1`（默认）| Variant Subsystem 中包含的选项名称

此参数为只读。

此参数显示选项的名称。每个选项都有一个变体控制，形式为标签、表达式或开关。对于处于 `label` 模式的 Variant Assembly Subsystem，没有单独的变体控制可用。选项的名称用作变体控制来设置活动选项。

### **Variant control label** — `label` 模式下的选项名称 `true` 或 `false`（默认）| 字符串

选项的名称，指定为字符串。

#### 依赖关系

要启用此参数，请将 **Variant control mode** 设置为 `label`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `VariantControl` |
| **值**：| 与变体选项关联的变体控制 |
| **Data Types:** | `char` |

**Example:** `set_param(gcb, 'VariantControl', 'V == 3')`，其中 `gcb` 是 Variant Subsystem 模块的变体选项。

**Example:** `get_param(gcb, 'VariantControl')`，其中 `gcb` 是 Variant Subsystem 模块的变体选项。

### **Variant control switch** — 用于仿真和代码生成工作流的变体选项 `(sim)` | `(codegen)`

指定 `(sim)` 以在仿真期间激活对应的变体选项。指定 `(codegen)` 以在执行代码生成工作流（如 SIL、PIL、外部模式等）时激活对应的变体选项。

#### 依赖关系

要启用此参数，请将 **Variant control mode** 设置为 `sim codegen switching`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `VariantControl` |
| **值**：| 与变体选项关联的变体控制 |
| **Data Types:** | `char` |

**Example:** `set_param(gcb, 'VariantControl', '(sim)')`，其中 `gcb` 是 Variant Subsystem 模块的变体选项。

**Example:** `get_param(gcb, 'VariantControl')`，其中 `gcb` 是 Variant Subsystem 模块的变体选项。

### **Variant control expression** — 确定活动选项的条件表达式 `true` 或 `false`（默认）| 布尔条件表达式 | 表示布尔条件表达式的 `Simulink.VariantExpression` 对象 | `(default)`

指定条件表达式以确定活动选项。当条件表达式求值为 `true` 时，软件激活对应的变体选项。当条件表达式求值为 `false` 时，软件停用对应的变体选项。

变体控制可以是：

- 用于快速原型开发的布尔条件表达式。例如，`A == 1`、`A ~= B`、`A && B == 1` 等。
- 包含条件表达式以复用条件的 `Simulink.VariantExpression` 对象。请参阅 Simulink.VariantExpression Objects for Variant Condition Reuse of Variant Blocks。
- 如果所有选项都未求值为 `true`，则为默认变体选项。

此处，`A` 和 `B` 是称为*变体控制变量*的操作数。`==`、`~=` 和 `&&` 是条件表达式中的运算符。条件表达式可以包含一个或多个此类变体控制变量和运算符。有关变体控制变量的支持类型和存储位置的信息，请参阅 Types of Variant Control Variables (Operands) in Variant Blocks 和 Storage Locations for Variant Control Variables (Operands) in Variant Blocks。有关运算符的信息，请参阅 Types of Operators in Variant Blocks for Different Activation Times。

有关详细信息，请参阅 Switch Between Choices Using Condition Expressions in Variant Blocks。

在 Variant Assembly Subsystem 模块中，此参数是自动生成的布尔表达式列表，**Variant control variable** 位于表达式的左侧，**Variant enumeration choice** 的成员位于表达式的右侧。表达式的两侧通过 `==` 连接。此参数为只读。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

Variant Subsystem 模块：

|  |  |
| --- | --- |
| **Parameter:** | `VariantControl` |
| **值**：| 与变体选项关联的变体控制 |
| **Data Types:** | `char` |

**Example:** `set_param(gcb, 'VariantControl', 'V == 3')`，其中 `gcb` 是 Variant Subsystem 模块的变体选项。

**Example:** `get_param(gcb, 'VariantControl')`，其中 `gcb` 是 Variant Subsystem 模块的变体选项。

Variant Source 和 Variant Sink 模块：

|  |  |
| --- | --- |
| **Parameter:** | `VariantControls` |
| **值**：| 与变体选项关联的变体控制 |
| **Data Types:** | `char` |

**Example:** `set_param(gcb, 'VariantControls', {'A == 1','A == 2'})`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

**Example:** `get_param(gcb, 'VariantControls')`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

### **Condition (read-only)** — `Simulink.VariantExpression` 对象中的条件表达式 只读：`N/A`（默认）

此参数为只读。

此参数显示指定为 `Simulink.VariantExpression` 对象的条件表达式。要更改或编辑条件表达式，请使用在工作区中双击该对象时出现的 `Simulink.VariantExpression` 参数对话框。

**注意**

您在 `Simulink.VariantExpression` 类型的条件表达式中指定的操作数必须在基础工作区或数据字典中定义。不支持指定在掩码或模型工作区中定义的操作数。

### **Label mode active choice** — `label` 模式下的活动选项名称 `true (Subsystem)`（默认）| `false (Subsystem1)`

此列表包含所有变体选项的标签。要设置活动选项，请从列表中选择一个标签。对应的选项将变为活动状态。或者，要更改标签模式下的活动选项，您可以按照 Set Active Choices Using Variant Control Labels 中描述的方法操作。

#### 依赖关系

要启用此参数，请将 **Variant control mode** 设置为 `label`。

#### 编程使用

|  |
| --- |
| **Parameter:** `LabelModeActiveChoice` |
| **类型**：character vector |
| **Value:** 如果未指定标签模式活动选项，则该值为空。如果指定了标签模式活动选项，则该值为活动选项的变体控制标签。 |
| **默认值**：`''` |

### **Built-in empty choice** — 如果没有活动变体选项则输出零 `off`（默认）| `on`

- `off` — 当没有活动变体选项时，Simulink 生成错误。
- `on` — 当您选择此选项时，Simulink 会向 **Variant choices** 表添加一个不可修改的变体选项条目，其变体控制设置为 `(default)`。此条目不会在 Variant Subsystem 模块中显示为可见的变体选项。在仿真期间，如果没有活动变体选项，Simulink 会断开 Variant Subsystem 模块的变体选项，从而将变体区域从模型中完全移除。子系统的非活动输出端口输出零。要输出零以外的值，请选择 Outport 模块的 **Specify output when source is unconnected** 参数并指定您选择的值。

有关详细信息，请参阅 Manage Variant Components to Pass Specified Values from Inactive Variant Subsystems with No Active Choice (Simulink Coder)。

#### 依赖关系

此参数仅在 Variant Subsystem 中没有 `default` 变体选项且您将 **Variant control mode** 设置为 `expression` 时可用。

#### 编程使用

|  |
| --- |
| **Parameter:** `EmptyChoice` |
| **类型**：character vector |
| **Value:** `'off'` | `'on'` |
| **默认值**：`'off'` |

### **Built-in passthrough choice** — 如果没有活动变体选项则将输入端口值赋给输出端口 `off`（默认）| `on`

- `off` — 当没有活动变体选项时，Simulink 生成错误。
- `on` — 当您选择此选项时，Simulink 会向 **Variant choices** 表添加一个不可修改的变体选项条目，其变体控制设置为 `(default)`。此条目不会在 Variant Subsystem 模块中显示为可见的变体选项。在仿真期间，如果没有活动变体选项，Simulink 会绕过 Variant Subsystem 模块的变体选项。只有输入和输出端口保持活动状态，输入端口将值直接传递给输出端口。

  要在没有活动选项时将值从输入端口映射到输出端口，Variant Subsystem 模块必须具有：

  - 仅数据端口，没有其他类型的输入和输出端口
  - 相同数量的数据输入和输出端口
  - 与变体选项的端口完全匹配的输入和输出端口

有关详细信息，请参阅 Manage Variant Components to Pass Specified Values from Inactive Variant Subsystems with No Active Choice (Simulink Coder)。

#### 依赖关系

此参数仅在 Variant Subsystem 中没有 `default` 变体选项且您将 **Variant control mode** 设置为 `expression` 时可用。

#### 编程使用

|  |
| --- |
| **Parameter:** `PassThrough` |
| **类型**：character vector |
| **Value:** `'off'` | `'on'` |
| **默认值**：`'off'` |

### **Propagate conditions outside of variant subsystem** — 选择是否必须将变体子系统外部的组件告知底层模块的活动和非活动状态的选项 `off`（默认）| `on`

当您选择 **Propagate conditions outside of variant subsystem** 参数时，软件会将底层模块的变体条件传播到 Variant Subsystem 容器模块，以便子系统可以根据底层模块的状态调整其接口。映射到活动选择端口上的端口变为活动状态。未映射到非活动选择端口上的端口变为非活动状态。选择此选项可确保 Variant Subsystem 外部的组件了解 Variant Subsystem 模块内模块的活动和非活动状态。有关详细信息，请参阅 Propagate Variant Conditions to Define Variant Regions Outside Variant Subsystems to Promote Consistency and Reduce Errors 和 Propagate Variant Conditions to Control Execution of Conditional Subsystems

如果 Variant Subsystem 模块内的所有变体选择具有相同的接口，则变体条件不会传播到 Variant Subsystem 模块外部。

#### 编程使用

|  |
| --- |
| **Parameter:** `PropagateVariantConditions` |
| **类型**：character vector |
| **Value:** `'off'` | `'on'` |
| **默认值**：`'off'` |

### **Allow flexible interface** — 选择使变体子系统的接口灵活的选项 `on`（默认）| `off`

指定是否使变体子系统的接口灵活。

- `on` — 使用变体选择进行仿真，这些变体选择的输入和输出端口数量与 Variant Subsystem 模块的输入和输出端口数量不同。
- `off` — 使用此选项进行仿真时，如果接口存在不一致，软件将生成带有修复操作的错误，以将变体选择的端口与 Variant Subsystem 模块匹配。

#### 编程使用

|  |
| --- |
| **Parameter:** `AllowFlexibleInterface` |
| **类型**：character vector |
| **Value:** `'off'` | `'on'` |
| **默认值**：`'on'` |
## 所属库

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `yesa` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a 实际数据类型或功能支持取决于模块实现。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。实际数据类型或功能支持取决于模块实现。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `Module`（默认） | 为子系统及子系统内的模块生成代码。HDL Coder 为所有变体选择生成代码。 |
| `BlackBox` | 生成黑盒接口。也就是说，生成的 HDL 代码仅包含子系统的输入/输出端口定义。通过这种方式，您可以在模型中使用子系统来生成与现有手写 HDL 代码的接口。为子系统生成的黑盒接口类似于为 Model 模块生成的接口，但不生成时钟信号。 |
| `No HDL` | 从生成的代码中移除子系统。您可以在仿真中使用该子系统，但在 HDL 代码中将其视为“空操作”。 |

**黑盒接口自定义**

对于 `BlackBox` 架构，您可以自定义端口名称并设置外部组件接口的属性。请参阅 Customize Black Box or HDL Cosimulation Interface (HDL Coder)。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **AdaptivePipelining** | 基于综合工具、目标频率和乘法器字长的自动流水线插入。默认值为 `inherit`。另请参阅 AdaptivePipelining (HDL Coder)。 |
| **BalanceDelays** | 检测沿一条路径引入的新延迟，并在其他路径上插入匹配的延迟。默认值为 `inherit`。另请参阅 BalanceDelays (HDL Coder)。 |
| **ClockRatePipelining** | 以更快的时钟速率而非较慢的数据速率插入流水线寄存器。默认值为 `inherit`。另请参阅 ClockRatePipelining (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分配，或寄存器重定时。默认值为 `inherit`。另请参阅 DistributedPipelining (HDL Coder)。 |
| **DSPStyle** | 用于乘法器映射的综合属性。默认值为 `none`。另请参阅 DSPStyle (HDL Coder)。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中移除子系统层级。默认值为 `inherit`。另请参阅 FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 映射到单个共享资源的功能等效资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |
| **StreamingFactor** | 被时间复用以转换为串行标量数据路径的并行数据路径或向量数量。默认值为 0，即实现完全并行的数据路径。另请参阅 Streaming (HDL Coder)。 |

**目标规范**

此模块不能作为 DUT，因此 **Target Specification** 选项卡中的模块属性设置将被忽略。

**限制**

- Variant Subsystem 不能是待测设计（DUT）。
- **Variant activation time** 参数必须设置为 `update diagram`、`update diagram analyze all choices` 或 `startup`。
- 对于 Variant Subsystem 的 Outport 模块，**Specify output when source is unconnected** 参数必须禁用。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型或功能支持取决于模块实现。

## 版本历史

**在 R2010b 中引入**

### R2025a: 通过抑制非活动变体选择和注释模块的回调来减少开销和不相关的诊断消息

回调 `LoadFcn`、`ContinueFcn`、`InitFcn`、`ModelCloseFcn`、`PauseFcn`、`PostSaveFcn`、`PreSaveFcn`、`StartFcn` 和 `StopFcn` 不会对激活时间为 `update diagram` 的 Variant Subsystem 模块中的非活动变体选择以及注释模块执行。此抑制减少了计算开销，并防止来自不影响当前模型迭代的模块的不必要诊断消息。但是，对于注释或非活动 Model 模块或 Subsystem Reference 模块内的模型或子系统文件中的模块，这些回调不会被抑制。此外，掩码初始化和掩码参数回调不会被抑制。有关适用回调的列表，请参阅 Author Mask Initialization and Callbacks 和 Mask Parameters。

### R2025a: 当不存在变体选择时输出零的参数从 **Allow zero active variant controls** 重命名

**Allow zero active variant controls** 参数现已重命名为 **Built-in empty choice**。此新参数保持之前的功能，即在没有变体选择处于活动状态时移除变体组件并输出零。

### R2025a: 当不存在变体选择时将输入值分配给输出端口

使用 **Built-in passthrough choice** 参数绕过变体区域，并在没有变体选择处于活动状态时将输入值分配给输出端口。

### R2024b: `runtime` 激活时间：在仿真或代码生成期间更改活动选择

从 R2024b 开始，在 Variant Subsystem 模块中使用 `runtime` 变体激活时间，通过 Parameter Writer 模块在仿真或代码生成期间更改活动变体。您可以对所有 Parameter Writer 模块可以写入全局工作区、掩码工作区或模型工作区中的变体控制变量的场景进行建模。

### R2024a: 自动端口同步

Simulink 提供选项来添加缺失端口和删除 Variant Subsystem 和 Variant Assembly Subsystem 模块中未使用的端口，以匹配底层变体选择的端口。在仿真期间，如果 Simulink 遇到 Variant Subsystem 或 Variant Assembly Subsystem 模块与其变体选择之间的端口不匹配，生成的错误消息会提供添加缺失端口和删除未使用端口以解决该问题的选项。

### R2024a: 使用自适应速率模型模块作为选择

您可以在 Variant Subsystem 模块中使用自适应速率模型模块作为变体选择。当您添加自适应速率模型作为变体选择时，变体子系统中的输入端口会与相应速率模型的端口名称匹配。

### R2024a: 访问活动变体选择的掩码

您可以直接访问 Variant Subsystem 活动变体选择的掩码，而无需导航到 Variant Subsystem 模块内部。

- 如果 Variant Subsystem 模块未设置掩码，双击该模块将打开其活动选择的掩码。单击 **Look under mask** 徽章或从 Variant Subsystem 模块的上下文菜单中选择相应选项，将直接进入活动选择内部。
- 如果 Variant Subsystem 模块已设置掩码且活动选择也有掩码，则双击该模块将打开 Variant Subsystem 掩码。
- 如果 Variant Subsystem 模块未设置掩码且其活动选择已设置掩码，则双击 **Look under mask** 徽章将带您进入变体层。在已设置掩码的 Variant Subsystem 模块中，如果其活动选择未设置掩码，您可以看到类似的行为。

当您单击链接的 Variant Subsystem 模块的 **Look under mask** 徽章，且其活动选择是链接且已设置掩码的 Model Reference 模块时，Model Reference 将在单独的编辑器中打开。此外，您必须对活动选择上的活动选择模块的掩码参数执行 `set_param` 操作，而不是对 Variant Subsystem 模块执行。

活动选择掩码的提升仅限于其直接父级。不支持嵌套 Variant Subsystem 掩码提升。

### R2024a: 将变体选择指定为字符串数组

您可以在 Variant Assembly Subsystem 模块中将 **Variant choices specifier** 指定为字符串数组。

### R2023b: 提升活动选择的内容预览

Simulink 自动提升 Variant Subsystem 模块活动选择的内容预览。当活动选择是未加载的 Model Reference 时，以及当活动选择是 Stateflow 图表时，Variant Subsystem 将显示为内容预览。

### R2023b: 直接导航到活动选择

您可以通过双击 Variant Subsystem 模块直接导航到活动变体内部。当您从上下文菜单中选择 **Open in New Tab** 或 **Open in New Window** 时，活动选择将在新选项卡或新窗口中打开。您还可以使用 `open_system` 函数访问变体层和活动选择。

```
open_system(vssBlock)
open_system(vssBlock,'ActiveChoice','window')
```

当活动选择具有 `OpenFcn` 回调时，双击 Variant Subsystem 模块不会执行该回调。此外，如果活动选择是未加载的引用模型，双击 Variant Subsystem 不会导航到活动选择内部。

### R2021a: 自动提升活动变体的掩码图标

Simulink 自动在父 Variant Subsystem 上显示活动变体模块的掩码图标。在 R2021a 之前，您必须在 Variant Subsystem 的掩码上提供图标绘制命令，以显示底层活动变体模块的掩码图标。

## 描述

包含子系统模块作为变体选项的模板子系统

Variant Subsystem 模块使您能够将组件的多个实现包含在单独的分层结构中。

例如，假设您要仿真一个表示具有三种可能发动机配置的车辆的模型：2 缸汽油、4 缸汽油和 8 缸汽油。您可以将每个发动机模型实现为 Variant Subsystem 模块内的单独子系统，然后根据您选择的变体模块中变体控制模式的类型在子系统之间切换。有关详细信息，请参阅变体控制简介。

**注意**

在仿真期间，Variant Subsystem 模块只有一个实现处于活动状态。

Variant Subsystem 模块内的多个发动机模型

Variant Subsystem 模块是一个预配置的模板，包含两个或多个模块用作变体选项。这些选项表示系统的多个实现。在模型执行期间只有一个子模块处于活动状态。活动的子模块称为*活动变体*。

Variant Subsystem 模块内的每个变体选项都与一个**变体控制模式**和一个**变体激活时间**相关联。变体控制模式决定如何选择活动变体。变体激活时间决定激活选项的时间，以及决定在生成的代码中是仅包含活动选项还是同时包含活动和未活动选项。

Variant Subsystem 模块可以包含子系统模块、模型模块或子系统引用模块的混合作为变体选项。仅以模型模块作为选项的 Variant Subsystem 模块称为 Variant Model 模块。有关详细信息，请参阅使用变体子系统在单独的分层结构中实现变体。以模型或子系统引用模块作为选项且只能从外部文件添加或移除而不能在模块内添加或移除的 Variant Subsystem 模块称为 Variant Assembly Subsystem 模块。

除了变体选项之外，您还可以在 Variant Subsystem 模块内包含 Inport、控制端口（Enable、Trigger、Reset 和 Function-Call Subsystem）、Outport 或 Connection Port（Simscape）模块。Variant Subsystem 模块内部的模块之间没有绘制的连接。软件在模型编译期间自动将活动变体连接到 Variant Subsystem 的 Inport 和 Outport 模块。表示变体选项的模块可以具有与父 Variant Subsystem 模块中的输入和输出端口数量不同的输入和输出端口。有关详细信息，请参阅映射 Variant Subsystem 中变体选项的输入和输出端口。

当您加载带有 Variant Subsystem 模块的模型，且该模块的变体选项存储在子系统文件中时，默认情况下仅加载活动选项以优化模型的加载时间。但是，如果您使用 `find_system`、`get_param` 或 `set_param` 函数以编程方式初始化模型，则可能会加载未活动的选项。

使用 Variant Subsystem 模块允许您：

- 将子系统、模型和子系统引用模块混合作为变体选项。
- 对不具有相似接口的组件进行建模。您可以在 Variant Subsystem 内为多个变体选项设置不同数量的输入端口和输出端口。但是，必须满足映射 Variant Subsystem 中变体选项的输入和输出端口中列出的条件。
- 建立分层框图，其中 Variant Subsystem 模块位于一层，变体选项位于另一层。
- 将功能相关的模块保持在一起。
- 降低模型的复杂度。
- 在模型编译期间，软件根据您选择的变体激活时间消除整个模型中的未活动模块。

模块图标上变体徽章的颜色和图标会根据模块上设置的**变体激活时间**、**变体控制模式**和**将条件传播到变体子系统外部**参数的值而变化。有关详细信息，请参阅变体徽章。

### 打开模块

您可以从 Simulink® 界面或以编程方式打开 Variant Subsystem 模块。这些方法使您能够根据您的需求访问活动变体选项或 Variant Subsystem 模块的整个变体层。

**从 Simulink 界面打开**

使用 Simulink 界面中的以下任一操作来打开 Variant Subsystem 模块。

| 键盘和鼠标操作 | 结果 |
| --- | --- |
| 双击 | 在新选项卡中打开模块内的活动变体选项  **注意**  如果变体选项是模型模块且其引用的模型未加载，则双击该模块会打开包含变体选项的变体层，而不是打开活动变体选项的底层 |
| 按住 **Ctrl** 并双击 | 在新选项卡中打开模块，显示变体层 |
| 按住 **Shift** 并双击 | 在新窗口中打开模块，显示变体层 |
| 右键单击，选择 **Open** > **Open in New Tab** | 在当前窗口中打开模块，显示变体层 |
| 右键单击，选择 **Open** > **Open in New Window** | 在新窗口中打开模块，显示变体层 |
| 右键单击变体徽章，选择 **Open** >**（活动变体）** | 在新选项卡中打开活动变体选项 |
| 右键单击变体徽章，选择 **Open** > **variant control (variant choice name)**，其中 *`variant control`* 是由 *variant choice name* 指定的变体选项的变体控制 `expression`、`label` 或 `(sim)` 或 `(codegen)` | 在新选项卡中打开所选的变体选项 |

**以编程方式打开**

使用以下任一命令打开 Variant Subsystem 模块，其中 *`variantSubsystemBlockName`* 是模块的名称：

- `open_system("variantSubsystemBlockName")` 命令 — 打开 Variant Subsystem 模块并查看其变体层。
- `open_system("variantSubsystemBlockName","ActiveChoice")` — 打开 Variant Subsystem 模块内的活动变体选项。

有关使用 `open_system` 命令打开 Variant Subsystem 模块的其他选项（例如在新选项卡或窗口中打开）的信息，请参阅 `open_system`。
