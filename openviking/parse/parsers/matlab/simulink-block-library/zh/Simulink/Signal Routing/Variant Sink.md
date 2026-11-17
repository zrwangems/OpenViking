---
type: simulink-block
title: 'Variant Sink'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'variantsink'
documentation_source_path: 'slref/variantsink.html'
language: zh-CN
chinese_source: worker-translation
---

# Variant Sink

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | struct
- name: Port_1
  summary: 第一个变体的输出 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus
- name: Port_N
  summary: 第 *N* 个变体的输出 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

要连接到活动输出端口的输入信号。

您可以通过将鼠标悬停在模块侧面或将信号拖到模块边界附近，在 Variant Sink 模块上自动插入输入端口。您可以通过按键盘上的删除键或用鼠标单击来删除端口。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `struct`
### 输出

### **Port\_1** — 第一个变体的输出 标量 | 向量 | 矩阵

第一个变体的输出信号。求值为 `true` 的变体控制决定了哪个输出端口处于活动状态。

您可以通过将鼠标悬停在模块侧面或将信号拖到模块边界附近，在 Variant Sink 模块上自动插入输出端口。您可以通过按键盘上的删除键或用鼠标单击来删除端口。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_N** — 第 *N* 个变体的输出 标量 | 向量 | 矩阵

第 *N* 个变体的输出信号。求值为 `true` 的变体控制决定了哪个输出端口处于活动状态。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
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
  summary: 软件选择活动变体选择的时间 update diagram（默认）| update diagram analyze all choices | code compile | startup | inherit from Simulink.VariantControl
  group: ''
  block_parameter: VariantActivationTime
  type: character vector
  values: '''update diagram'' | ''update diagram analyze all choices'' | ''code compile'' | ''startup'''
  default: '''update diagram'''
- name: Port and associated conditions
  summary: 变体选择、变体控制和条件的表格 空表格（默认）
  group: ''
- name: Port
  summary: 已连接输出端口的编号 无默认值
  group: ''
- name: Variant control label
  summary: label 模式下选择的名称 true 或 false（默认）| 字符串
  group: ''
  block_parameter: VariantControls
  values: 与变体选择关联的变体控制
- name: Variant control switch
  summary: 用于仿真和代码生成工作流的变体选择 (sim) | (codegen)
  group: ''
  block_parameter: VariantControls
  values: 与变体选择关联的变体控制
- name: Variant control expression
  summary: 决定活动选择的条件表达式 true 或 false（默认）| 布尔条件表达式 | 表示布尔条件表达式的 Simulink.VariantExpression 对象 | (default)
  group: ''
  block_parameter: VariantControls
  values: 与变体选择关联的变体控制
- name: Condition (read-only)
  summary: Simulink.VariantExpression 对象中的条件表达式 只读：N/A（默认）
  group: ''
- name: Label mode active choice
  summary: label 模式下活动选择的名称 true (Subsystem)（默认）| false (Subsystem1)
  group: ''
  block_parameter: LabelModeActiveChoice
  type: character vector
  values: 如果未指定标签模式活动选择，则该值为空。如果指定了标签模式活动选择，则该值为活动选择的变体控制标签。
  default: ''''''
- name: Allow zero active variant controls
  summary: 在没有活动变体选择的情况下仿真模型 off（默认）| on
  group: ''
  block_parameter: AllowZeroVariantControls
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Show variant condition on block
  summary: 在模块端口上标注 off（默认）| on
  group: ''
  block_parameter: ShowConditionOnBlock
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
```

### **Variant control mode** — 变体控制模式 `expression`（默认）| `label` | `sim codegen switching`

决定活动变体选择的变体控制可以是以下任意类型。

- `expression` — 软件根据变体条件的求值结果选择活动变体。当条件表达式求值为 `true` 时，对应的变体选择变为活动状态。当条件表达式求值为 `false` 时，对应的变体选择变为非活动状态。请参阅 Switch Between Choices Using Condition Expressions in Variant Blocks。
- `label` — 软件根据变体的名称选择活动变体。变体控制是一个字符串，不需要您在任何工作区中创建任何变量。请参阅 Switch Between Choices Using Labels in Variant Blocks。
- `sim codegen switching` — 在仿真和代码生成工作流之间自动切换变体，无需创建任何工作区变量。当您仿真模型时，软件自动选择 `sim` 分支作为活动选择。同样，当您执行软件在环（SIL）或处理器在环（PIL）仿真、生成代码或使用外部模式时，软件自动选择 `codegen` 分支。请参阅 Switch Between Choices for Simulation and Code Generation Workflows Without Using Control Variables in Variant Blocks。

有关变体控制模式的详细信息，请参阅 Introduction to Variant Controls。有关不同变体控制模式类型之间的比较，请参阅 Compare Different Types of Variant Control Modes in Variant Blocks。

#### 依赖关系

不同变体激活时间的可用性取决于您指定的 **Variant control mode** 类型。**Variant activation time** 参数决定软件设置活动选择的时间。该参数还决定生成的代码中包含哪些可变性。下表说明了每种变体控制模式支持的变体激活时间。

| **Variant activation time** | | | | |
| --- | --- | --- | --- | --- |
| **Variant control mode** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` |
| `expression` | ✓ | ✓ | ✓ | ✓ |
| `label` | ✓ | x | x | x |
| `sim codegen switching` | ✓ | ✓ | x | x |

#### 编程使用

|  |
| --- |
| **模块参数**：`VariantControlMode` |
| **类型**：character vector |
| **值**：`'expression'` | `'label'` | `'sim codegen switching'` |
| **默认值**：`'expression'` |

### **Variant activation time** — 软件选择活动变体选择的时间 `update diagram`（默认）| `update diagram analyze all choices` | `code compile` | `startup` | `inherit from Simulink.VariantControl`

此参数决定仿真和代码生成工作流中包含哪些可变性。有关详细信息，请参阅 Activate Variant During Different Stages of Simulation and Code Generation Workflow。

- `update diagram` — 当您执行模型时，只有活动选择包含在仿真和代码生成工作流中。生成的代码仅包含活动选择。
- `update diagram analyze all choices` — 当您执行模型时，活动和非活动选择都会在模型中进行一致性分析。但是，只有活动选择包含在仿真和代码生成工作流中。生成的代码仅包含活动选择。
- `code compile` — 当您执行模型时，活动和非活动选择都会在模型中进行一致性分析，并且所有选择都包含在仿真和代码生成工作流中。生成的代码包含活动和非活动选择，它们被包裹在预处理器条件 `#if` 和 `#elif` 中。但是，从生成的代码构建的可执行文件仅包含活动选择。
- `startup` — 当您执行模型时，活动和非活动选择都会在模型中进行一致性分析，并且所有选择都包含在仿真和代码生成工作流中。使用此选项，您可以使用快速重启来提高迭代仿真的速度。有关详细信息，请参阅 Run Iterative Simulations Without Recompiling Model for Variant Systems Using Fast Restart。从模型生成的代码包含活动和非活动选择，它们被包裹在常规 `if` 条件中。从生成的代码构建的可执行文件也包含活动和非活动选择。
- `inherit from Simulink.VariantControl` — 当您执行模型时，模块从其类型为 `Simulink.VariantControl` 的变体控制变量继承激活时间。如果变体模块有多个类型为 `Simulink.VariantControl` 的变体控制变量，则所有这些变量必须具有相同的激活时间。

#### 依赖关系

不同变体激活时间的可用性取决于您指定的变体控制模式的类型。**Variant activation time** 参数决定软件何时设置活动选择。该参数还决定生成的代码中包含哪些可变性。下表说明了每种变体控制模式支持的变体激活时间。

| **Variant activation time** | | | | |
| --- | --- | --- | --- | --- |
| **Variant control mode** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` |
| `expression` | ✓ | ✓ | ✓ | ✓ |
| `label` | ✓ | x | x | x |
| `sim codegen switching` | ✓ | ✓ | x | x |

#### 编程使用

|  |
| --- |
| **模块参数**：`VariantActivationTime` |
| **类型**：character vector |
| **值**：`'update diagram'` | `'update diagram analyze all choices'` | `'code compile'` | `'startup'` |
| **默认值**：`'update diagram'` |

### **Port and associated conditions** — 变体选择、变体控制和条件的表格 空表格（默认）

该表格为连接到 Variant Sink 模块输出端口的每个变体选择包含一行。如果没有变体选择，则表格为空。

您可以使用 **Port and associated conditions** 表格左侧的按钮来修改表格中的元素。

| 要... | 请单击... |
| --- | --- |
| **添加新的输出端口**：创建一个新的输出端口作为变体选择，并在表格中为新选择添加条目。 | 添加新的输出端口按钮 |
| **删除选定的端口**：从模块中删除选定的变体选择，并从表格中删除其条目。 | 删除选定的端口按钮 |
| **创建/编辑选定的变体对象**：在全局工作区中为选定的变体选择创建或编辑 `Simulink.VariantExpression` 对象，并使用 `Simulink.VariantExpression` 对象参数对话框指定变体条件。  **注意**  对于使用基础工作区的模型，此操作会在基础工作区中创建 `Simulink.VariantExpression` 对象，该对象仅在当前 MATLAB® 会话中可用。要永久存储数据，请将对象保存到 MAT 文件或 MATLAB 脚本中。 | 创建/编辑选定的变体对象按钮 |

### **Port** — 已连接输出端口的编号 无默认值

连接到 Variant Sink 模块上游的一个变体选择的输出端口的编号。此值为只读。

单击添加新的输出端口按钮以添加端口，或单击删除选定的端口按钮以删除现有端口。

### **Variant control label** — `label` 模式下选择的名称 `true` 或 `false`（默认）| 字符串

选择的名称，指定为字符串。

#### 依赖关系

要启用此参数，请将 **Variant control mode** 设置为 `label`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `VariantControls` |
| **值**：| 与变体选择关联的变体控制 |
| **Data Types:** | `char` |

**示例：** `set_param(gcb, 'VariantControls', {'A == 1','A ==
2'})`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

**示例：** `get_param(gcb, 'VariantControls')`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

### **Variant control switch** — 用于仿真和代码生成工作流的变体选择 `(sim)` | `(codegen)`

指定 `(sim)` 以在仿真期间激活对应的变体选择。指定 `(codegen)` 以在执行代码生成工作流（如 SIL、PIL、外部模式等）时激活对应的变体选择。

#### 依赖关系

要启用此参数，请将 **Variant control mode** 设置为 `sim codegen switching`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `VariantControls` |
| **值**：| 与变体选择关联的变体控制 |
| **Data Types:** | `char` |

**示例：** `set_param(gcb, 'VariantControls',
{'(sim)','(codegen)'})`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

**示例：** `get_param(gcb, 'VariantControls')`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

### **Variant control expression** — 决定活动选择的条件表达式 `true` 或 `false`（默认）| 布尔条件表达式 | 表示布尔条件表达式的 `Simulink.VariantExpression` 对象 | `(default)`

指定条件表达式以确定活动选择。当条件表达式求值为 `true` 时，软件激活对应的变体选择。当条件表达式求值为 `false` 时，软件停用对应的变体选择。

变体控制可以是：

- 用于快速原型开发的布尔条件表达式。例如，`A == 1`、`A ~= B`、`A
  && B == 1` 等。
- 包含条件表达式以复用条件的 `Simulink.VariantExpression` 对象。请参阅 Simulink.VariantExpression Objects for Variant Condition Reuse of Variant Blocks。
- 默认变体选择（如果没有任何选择求值为 `true`）。

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
| **值**：| 与变体选择关联的变体控制 |
| **Data Types:** | `char` |

**示例：** `set_param(gcb, 'VariantControl', 'V == 3')`，其中 `gcb` 是 Variant Subsystem 模块的变体选择。

**示例：** `get_param(gcb, 'VariantControl')`，其中 `gcb` 是 Variant Subsystem 模块的变体选择。

Variant Source 和 Variant Sink 模块：

|  |  |
| --- | --- |
| **Parameter:** | `VariantControls` |
| **值**：| 与变体选择关联的变体控制 |
| **Data Types:** | `char` |

**示例：** `set_param(gcb, 'VariantControls', {'A == 1','A ==
2'})`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

**示例：** `get_param(gcb, 'VariantControls')`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

### **Condition (read-only)** — `Simulink.VariantExpression` 对象中的条件表达式 只读：`N/A`（默认）

此参数为只读。

此参数显示指定为 `Simulink.VariantExpression` 对象的条件表达式。要更改或编辑条件表达式，请使用在工作区中双击该对象时出现的 `Simulink.VariantExpression` 参数对话框。

**注意**

您在类型为 `Simulink.VariantExpression` 的条件表达式中指定的操作数必须在基础工作区或数据字典中定义。不支持指定在掩码或模型工作区中定义的操作数。

### **Label mode active choice** — `label` 模式下活动选择的名称 `true (Subsystem)`（默认）| `false (Subsystem1)`

此列表包含所有变体选择的标签。要设置活动选择，请从列表中选择一个标签。对应的选择变为活动状态。或者，要更改标签模式下的活动选择，您可以按照 Set Active Choices Using Variant Control Labels 中描述的方法进行操作。

#### 依赖关系

要启用此参数，请将 **Variant control mode** 设置为 `label`。

#### 编程使用

|  |
| --- |
| **Parameter:** `LabelModeActiveChoice` |
| **类型**：character vector |
| **Value:** 如果未指定标签模式活动选择，则该值为空。如果指定了标签模式活动选择，则该值为活动选择的变体控制标签。 |
| **默认值**：`''` |

### **Allow zero active variant controls** — 在没有活动变体选择的情况下仿真模型 `off`（默认）| `on`

- `off` — 当没有活动变体选择时，Simulink 生成错误。
- `on` — 当您选择此参数并且没有活动变体选择时，Simulink 在没有连接到 Variant Sink 模块的任何活动变体选择的情况下仿真模型。Simulink 断开连接到 Variant Sink 模块输入和输出流的所有模块，从而将变体区域从模型执行中完全移除。

考虑描述部分中的汽车挡风玻璃雨刮器示例。假设您不想将雨刮器速度传递给任一变体选择，即雨刮电机和 D/A。当您在 **Allow zero active variant controls** 设置为 `on` 的情况下仿真模型，并且 `Variant Sink controlled by mode` 模块中没有活动变体选择时，Simulink 断开 `Variant Sink controlled by mode` 模块及其所有连接的模块，从而将变体区域从模型中完全移除。

此表显示了在 `code compile` 激活时间下，使用和不使用 **Allow zero active variant controls** 参数时生成的代码。在 **Allow zero active variant controls** 设置为 `off` 时生成的代码中，只有变体选择 `wiper motor` 和 `D/A` 是条件性的，而 Gain 模块是无条件的。Gain 模块是无条件的，因此它会针对任一选择执行。此代码仅支持任一选择求值为 `true` 的场景。如果没有任何选择求值为 `true`，则两个选择都会从编译中移除。Gain 的输出保持未使用，这会导致错误。在 **Allow zero active variant controls** 设置为 `on` 时生成的代码中，变体选择 `wiper motor`、`D/A` 以及连接的 Gain 模块都是条件性的。因此，如果没有任何选择求值为 `true`，Gain 模块也会被移除，从而使您能够将变体区域从代码编译中完全移除。

| 不使用 **Allow zero active variant controls** 生成的代码 | 使用 **Allow zero active variant controls** 生成的代码 |
| --- | --- |
| ``` /* If none of the conditions Mode == 1 or Mode == 2  evaluate to true, the output of Gain remains unused which resuls in an error.*/  /* logic for Gain; */  # if Mode == 1   /* logic for wiper motor; */ # elif Mode == 2   /* logic for digital to analog conversion; */ # endif ``` | ``` # if Mode == 1   /* logic for wiper motor; */ # elif Mode == 2   /* logic digital to analog conversion; */ # endif  /* The logic for Gain is executed only if  either of the conditions evaluate to true.  Gain is removed from code compilation if none of the condition evaluates to true. */  # if (Mode == 1) ∥ (Mode == 2)   /* logic for Gain; */ # endif ``` |

#### 依赖关系

此参数仅在您将 **Variant control mode** 设置为 `expression` 时可用。

#### 编程使用

|  |
| --- |
| **模块参数**：`AllowZeroVariantControls` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Show variant condition on block** — 在模块端口上标注 `off`（默认）| `on`

当您选择此选项时，Simulink 会在 Variant Sink 模块的每个端口上标注变体条件表达式。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowConditionOnBlock` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |
## 所属库

Simulink / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### Fixed-Point Conversion 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2016a 中引入**

### R2025a: Detect undefined variant control variables during edit-time

Variant Source 和 Variant Sink 模块在模型编辑期间通过为未定义的变体控制变量显示红色边框来发出错误。要查看错误的描述，请将鼠标悬停在突出显示的模块上，然后单击错误符号以打开带有预定义修复的通知对话框。选择最合适的修复，然后单击 **Fix** 按钮。您可能需要提供其他信息来解决错误。如果成功，红色边框会消失。如果失败，则会出现失败消息。

## 描述

使用变体在多个输出之间路由

Variant Sink 模块使您能够在单层中包含信号目标（汇）处组件的多个实现。

例如，假设您想要仿真此模型，以通过使用不同的雨量传感器来控制汽车挡风玻璃雨刮器的速度。Variant Source 模块在不同的雨量传感器之间切换。控制逻辑使用此信息将结果输出到 Variant Sink 模块。然后，Variant Sink 在仿真期间在雨刮电机模型和代码生成期间发送到传感器的命令之间切换。变体模块根据您选择的变体模块中的变体控制模式类型在选项之间切换。有关详细信息，请参阅 Introduction to Variant Controls。

**注意**

在仿真期间，连接到 Variant Sink 模块输出端口的至多一个变体选择处于活动状态。

使用 Variant Sink 模块控制汽车挡风玻璃速度的多个实现

Variant Sink 模块只有一个输入端口和一个或多个输出端口。您可以将变化的选项连接到模块的输出端口，以便在模型执行期间至多一个选项处于活动状态。

Variant Sink 模块与 Variant control mode 和 Variant activation time 相关联。变体控制模式确定如何指定变体控制。变体激活时间确定激活选项的时间，并决定在生成的代码中是仅包含活动选项还是同时包含活动和非活动选项。在仿真期间，Simulink® 将活动选项直接连接到 Variant Sink 模块的输入端口，并忽略非活动选项。

使用 Variant Sink 模块允许您：

- 在整个模型中传播变体条件。
- 在模型的单层中可视化变体选项的所有可能实现，从而提高模型可读性。
- Simulink 消除整个模型中的非活动模块，从而提高运行时性能。如果所有变体选项都处于非活动状态，Simulink 会从您的模型中完全移除变体区域。
- 变体源和汇提供变体组件接口，您可以使用这些接口快速建模变体选项。

模块图标上变体徽章的颜色和图标会根据模块上设置的 **Variant activation time**、**Variant control mode** 和 **Allow zero active variant controls** 参数的值而变化。有关详细信息，请参阅 Variant Badges。
