---
type: simulink-block
title: 'Variant Sink'
family: signal-routing
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'variantsink'
language: zh-CN
chinese_source: worker-translation
---

# Variant Sink



使用变体在多个输出之间路由

## 库

Simulink / Signal Routing

## 描述

Variant Sink 模块使你能够在单个层中，在信号的接收端（sink）包含组件的多个实现。

例如，假设你想通过使用不同的雨量传感器来仿真此模型以控制汽车雨刮器的速度。Variant Source 模块在不同的雨量传感器之间切换。控制逻辑使用此信息将结果输出到 Variant Sink 模块。然后 Variant Sink 在仿真期间的雨刮器电机模型和代码生成期间发送到传感器的命令之间切换。变体模块根据你在 Variant 模块中选择的变体控制模式类型在选项之间切换。有关详细信息，请参阅变体控制简介。

**注意**

在仿真期间，连接到 Variant Sink 模块输出端口的变体选项最多只有一个处于活动状态。

使用 Variant Sink 模块控制汽车挡风玻璃速度的多个实现

Variant Sink 模块只有一个输入端口和一个或多个输出端口。你可以将各种变体选项连接到该模块的输出端口，以便在模型执行期间最多只有一个选项处于活动状态。

Variant Sink 模块与一个变体控制模式和一个变体激活时间关联。变体控制模式确定如何指定变体控制。变体激活时间确定激活选项的时间，并决定在生成的代码中是仅包含活动选项，还是同时包含活动和非活动选项。在仿真期间，Simulink® 将活动选项直接连接到 Variant Sink 模块的输入端口，并忽略非活动选项。

使用 Variant Sink 模块允许你：

- 在整个模型中传播变体条件。
- 在模型的单个层中可视化变体选项的所有可能实现，这提高了模型可读性。
- Simulink 会消除整个模型中的非活动模块，从而提高运行时性能。如果所有变体选项都处于非活动状态，Simulink 会从模型中完全移除变体区域。
- Variant Source 和 Variant Sink 提供变体组件接口，你可以使用这些接口快速对变体选项建模。

模块图标上变体徽章的颜色和图标会根据模块上设置的 **变体激活时间**、**变体控制模式** 和 **允许零个活动变体控制** 参数的值而变化。有关详细信息，请参阅变体徽章。

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

要连接到活动输出端口的输入信号。

你可以通过将鼠标悬停在模块侧边或将信号拖到模块边界附近，在 Variant Sink 模块上自动插入输入端口。你可以通过按键盘上的 delete 键或鼠标点击来删除该端口。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `struct`

### 输出

### **Port\_1** — 来自第一个变体的输出 标量 | 向量 | 矩阵

来自第一个变体的输出信号。求值为 `true` 的变体控制决定哪个输出端口处于活动状态。

你可以通过将鼠标悬停在模块侧边或将信号拖到模块边界附近，在 Variant Sink 模块上自动插入输出端口。你可以通过按键盘上的 delete 键或鼠标点击来删除该端口。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_N** — 来自第 *N* 个变体的输出 标量 | 向量 | 矩阵

来自第 *N* 个变体的输出信号。求值为 `true` 的变体控制决定哪个输出端口处于活动状态。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **变体控制模式** — 变体控制模式 `expression` (default) | `label` | `sim codegen switching`

确定活动变体选项的变体控制可以是以下任意类型。

- `expression` — 软件基于变体条件的求值选择活动变体。当条件表达式求值为 `true` 时，对应的变体选项变为活动状态。当条件表达式求值为 `false` 时，对应的变体选项变为非活动状态。请参阅在 Variant 模块中使用条件表达式在选项之间切换。
- `label` — 软件基于变体的名称选择活动变体。变体控制是字符串，不需要你在任何工作区中创建任何变量。请参阅在 Variant 模块中使用标签在选项之间切换。
- `sim codegen switching` — 自动在仿真和代码生成工作流的变体之间切换，无需创建任何工作区变量。当你仿真模型时，软件自动选择 `sim` 分支作为活动选项。同样，当你执行软件在环（SIL）或处理器在环（PIL）仿真、生成代码或使用外部模式时，软件自动选择 `codegen` 分支。请参阅在不使用控制变量的情况下在 Variant 模块中为仿真和代码生成工作流切换选项。

有关变体控制模式的详细信息，请参阅变体控制简介。有关不同变体控制模式类型之间的比较，请参阅比较 Variant 模块中不同类型的变体控制模式。

#### 依赖关系

不同变体激活时间的可用性取决于你指定的 **变体控制模式** 类型。**变体激活时间** 参数确定软件何时设置活动选项。该参数还确定生成的代码中要包含哪些可变性。此表说明了每种变体控制模式支持的变体激活时间。

| **变体激活时间** | | | | |
| --- | --- | --- | --- | --- |
| **变体控制模式** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` |
| `expression` | ✓ | ✓ | ✓ | ✓ |
| `label` | ✓ | x | x | x |
| `sim codegen switching` | ✓ | ✓ | x | x |

#### 程序化使用

|  |
| --- |
| **模块参数：** `VariantControlMode` |
| **类型：** character vector |
| **值：** `'expression'` | `'label'` | `'sim codegen switching'` |
| **默认：** `'expression'` |

### **变体激活时间** — 软件选择活动变体选项的时间 `update diagram` (default) | `update diagram analyze all choices` | `code compile` | `startup` | `inherit from Simulink.VariantControl`

此参数确定在仿真和代码生成工作流中要包含哪些可变性。有关详细信息，请参阅在仿真和代码生成工作流的不同阶段激活变体。

- `update diagram` — 当你执行模型时，仿真和代码生成工作流中仅包含活动选项。生成的代码仅包含活动选项。
- `update diagram analyze all choices` — 当你执行模型时，会分析活动和非活动选项在整个模型中的一致性。但是，仿真和代码生成工作流中仅包含活动选项。生成的代码仅包含活动选项。
- `code compile` — 当你执行模型时，会分析活动和非活动选项在整个模型中的一致性，并且所有选项都包含在仿真和代码生成工作流中。生成的代码包含活动和非活动选项，并将它们包含在预处理器条件 `#if` 和 `#elif` 中。但是，由生成的代码构建的可执行文件仅包含活动选项。
- `startup` — 当你执行模型时，会分析活动和非活动选项在整个模型中的一致性，并且所有选项都包含在仿真和代码生成工作流中。使用此选项，你可以使用快速重启提高迭代仿真的速度。有关详细信息，请参阅使用快速重启在不重新编译变体系统模型的情况下运行迭代仿真。从模型生成的代码包含活动和非活动选项，并将它们包含在常规 `if` 条件中。由生成的代码构建的可执行文件也包含活动和非活动选项。
- `inherit from Simulink.VariantControl` — 当你执行模型时，模块从其 `Simulink.VariantControl` 类型的变体控制变量继承激活时间。如果变体模块有多个 `Simulink.VariantControl` 类型的变体控制变量，那么所有这些变量必须具有相同的激活时间。

#### 依赖关系

不同变体激活时间的可用性取决于你指定的变体控制模式类型。**变体激活时间** 参数确定软件何时设置活动选项。该参数还确定生成的代码中要包含哪些可变性。此表说明了每种变体控制模式支持的变体激活时间。

| **变体激活时间** | | | | |
| --- | --- | --- | --- | --- |
| **变体控制模式** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` |
| `expression` | ✓ | ✓ | ✓ | ✓ |
| `label` | ✓ | x | x | x |
| `sim codegen switching` | ✓ | ✓ | x | x |

#### 程序化使用

|  |
| --- |
| **模块参数：** `VariantActivationTime` |
| **类型：** character vector |
| **值：** `'update diagram'` | `'update diagram analyze all choices'` | `'code compile'` | `'startup'` |
| **默认：** `'update diagram'` |

### **端口和关联条件** — 变体选项、变体控制和条件的表 空表（默认）

该表为连接到 Variant Sink 模块输出端口的每个变体选项包含一行。如果没有变体选项，则该表为空。

你可以使用 **端口和关联条件** 表左侧的按钮来修改表中的元素。

| 要... | 点击... |
| --- | --- |
| **添加新输出端口**：创建一个新输出端口作为变体选项，并在表中为新选项添加条目。 | 添加新输出端口按钮 |
| **删除选定端口**：从模块中删除选定的变体选项，并从表中删除其条目。 | 删除选定端口按钮 |
| **创建/编辑选定的变体对象**：在全局工作区中为选定的变体选项创建或编辑 `Simulink.VariantExpression` 对象，并使用 `Simulink.VariantExpression` 对象参数对话框指定变体条件。  **注意**  对于使用基础工作区的模型，此操作会在基础工作区中创建 `Simulink.VariantExpression` 对象，并且该对象仅对当前 MATLAB® 会话可用。要永久存储数据，请将对象保存到 MAT 文件或 MATLAB 脚本中。 | 创建或编辑选定的变体对象按钮 |

### **端口** — 已连接输出端口的编号 无默认值

连接到 Variant Sink 模块上游某个变体选项的输出端口编号。此值为只读。

点击添加新输出端口按钮以添加端口，或点击删除选定端口按钮以删除现有端口。

### **变体控制标签** — `label` 模式下选项的名称 `true` 或 `false` (default) | string

选项的名称，指定为 string。

#### 依赖关系

要启用此参数，请将 **变体控制模式** 设置为 `label`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VariantControls` |
| **值：** | 与变体选项关联的变体控制 |
| **数据类型：** | `char` |

**示例：** `set_param(gcb, 'VariantControls', {'A == 1','A == 2'})`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

**示例：** `get_param(gcb, 'VariantControls')`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

### **变体控制开关** — 用于仿真和代码生成工作流的变体选项 `(sim)` | `(codegen)`

指定 `(sim)` 以在仿真期间激活对应的变体选项。指定 `(codegen)` 以在执行代码生成工作流（例如 SIL、PIL、外部模式等）时激活对应的变体选项。

#### 依赖关系

要启用此参数，请将 **变体控制模式** 设置为 `sim codegen switching`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VariantControls` |
| **值：** | 与变体选项关联的变体控制 |
| **数据类型：** | `char` |

**示例：** `set_param(gcb, 'VariantControls', {'(sim)','(codegen)'})`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

**示例：** `get_param(gcb, 'VariantControls')`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

### **变体控制表达式** — 确定活动选项的条件表达式 `true` 或 `false` (default) | boolean condition expression | 表示 boolean condition expression 的 `Simulink.VariantExpression` 对象 | `(default)`

指定条件表达式以确定活动选项。当条件表达式求值为 `true` 时，软件激活对应的变体选项。当条件表达式求值为 `false` 时，软件停用对应的变体选项。

变体控制可以是：

- 用于快速原型设计的布尔条件表达式。例如，`A == 1`、`A ~= B`、`A && B == 1` 等。
- 包含条件表达式以重用条件的 `Simulink.VariantExpression` 对象。请参阅用于 Variant 模块变体条件重用的 Simulink.VariantExpression 对象。
- 如果没有任何选项求值为 `true`，则为默认变体选项。

这里，`A` 和 `B` 是称为 *变体控制变量* 的操作数。`==`、`~=` 和 `&&` 是条件表达式中的运算符。条件表达式可以包含一个或多个这样的变体控制变量和运算符。有关变体控制变量支持的类型和存储位置的信息，请参阅 Variant 模块中变体控制变量（操作数）的类型和 Variant 模块中变体控制变量（操作数）的存储位置。有关运算符的信息，请参阅不同激活时间下 Variant 模块中的运算符类型。

有关详细信息，请参阅在 Variant 模块中使用条件表达式在选项之间切换。

在 Variant Assembly Subsystem 模块中，此参数是自动生成的布尔表达式列表，左侧为 **变体控制变量**，右侧为 **变体枚举选项** 的成员。表达式的两侧通过 `==` 连接。此参数为只读。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

Variant Subsystem 模块：

|  |  |
| --- | --- |
| **参数：** | `VariantControl` |
| **值：** | 与变体选项关联的变体控制 |
| **数据类型：** | `char` |

**示例：** `set_param(gcb, 'VariantControl', 'V == 3')`，其中 `gcb` 是 Variant Subsystem 模块的变体选项。

**示例：** `get_param(gcb, 'VariantControl')`，其中 `gcb` 是 Variant Subsystem 模块的变体选项。

Variant Source 和 Variant Sink 模块：

|  |  |
| --- | --- |
| **参数：** | `VariantControls` |
| **值：** | 与变体选项关联的变体控制 |
| **数据类型：** | `char` |

**示例：** `set_param(gcb, 'VariantControls', {'A == 1','A == 2'})`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

**示例：** `get_param(gcb, 'VariantControls')`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

### **条件（只读）** — `Simulink.VariantExpression` 对象中的条件表达式 只读：`N/A` (default)

此参数为只读。

此参数显示指定为 `Simulink.VariantExpression` 对象的条件表达式。要更改或编辑条件表达式，请使用在工作区中双击该对象时出现的 `Simulink.VariantExpression` 参数对话框。

**注意**

你在 `Simulink.VariantExpression` 类型的条件表达式中指定的操作数必须在基础工作区或数据字典中定义。不支持指定在掩码或模型工作区中定义的操作数。

### **Label 模式活动选项** — `label` 模式下活动选项的名称 `true (Subsystem)` (default) | `false (Subsystem1)`

此列表包含所有变体选项的标签。要设置活动选项，请从列表中选择一个标签。对应的选项变为活动状态。或者，要更改 label 模式下的活动选项，你可以遵循使用变体控制标签设置活动选项中描述的方法。

#### 依赖关系

要启用此参数，请将 **变体控制模式** 设置为 `label`。

#### 程序化使用

|  |
| --- |
| **参数：** `LabelModeActiveChoice` |
| **类型：** character vector |
| **值：** 如果未指定 label 模式活动选项，则值为空。如果指定了 label 模式活动选项，则该值为活动选项的变体控制标签。 |
| **默认：** `''` |

### **允许零个活动变体控制** — 在没有活动变体选项的情况下仿真模型 `off` (default) | `on`

- `off` — 当没有活动变体选项时，Simulink 生成错误。
- `on` — 当你选择此参数且没有活动变体选项时，Simulink 在没有连接到 Variant Sink 模块的任何活动变体选项的情况下仿真模型。Simulink 断开连接到 Variant Sink 模块输入和输出流的所有模块，从而从模型执行中完全移除变体区域。

考虑描述部分中的汽车雨刮器示例。假设你不希望将雨刮器速度传递到任一变体选项：wiper motor 和 D/A。当你使用 **允许零个活动变体控制** 设置为 `on` 来仿真模型，并且 `Variant Sink controlled by mode` 模块中没有活动变体选项时，Simulink 会断开 `Variant Sink controlled by mode` 模块及其所有连接的模块，这会从模型中完全移除变体区域。

此表显示了在 `code compile` 激活时间下，使用和不使用 **允许零个活动变体控制** 参数时生成的代码。在使用 **允许零个活动变体控制** 设置为 `off` 生成的代码中，只有变体选项 `wiper motor` 和 `D/A` 是有条件的，而 Gain 模块是无条件的。Gain 模块是无条件的，因此它会针对任一选项执行。此代码仅支持任一选项求值为 `true` 的场景。如果没有任何选项求值为 `true`，则两个选项都会从编译中移除。Gain 的输出保持未使用，这会导致错误。在使用 **允许零个活动变体控制** 设置为 `on` 生成的代码中，变体选项 `wiper motor`、`D/A` 以及连接的 Gain 模块都是有条件的。因此，如果没有任何选项求值为 `true`，Gain 模块也会被移除，从而使你能够从代码编译中完全移除变体区域。

| 未设置 **允许零个活动变体控制** 时生成的代码 | 设置 **允许零个活动变体控制** 时生成的代码 |
| --- | --- |
| ``` /* If none of the conditions Mode == 1 or Mode == 2  evaluate to true, the output of Gain remains unused which resuls in an error.*/  /* logic for Gain; */  # if Mode == 1   /* logic for wiper motor; */ # elif Mode == 2   /* logic for digital to analog conversion; */ # endif ``` | ``` # if Mode == 1   /* logic for wiper motor; */ # elif Mode == 2   /* logic digital to analog conversion; */ # endif  /* The logic for Gain is executed only if  either of the conditions evaluate to true.  Gain is removed from code compilation if none of the condition evaluates to true. */  # if (Mode == 1) ∥ (Mode == 2)   /* logic for Gain; */ # endif ``` |

#### 依赖关系

仅当你将 **变体控制模式** 设置为 `expression` 时，此参数才可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `AllowZeroVariantControls` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **在模块上显示变体条件** — 标注模块端口 `off` (default) | `on`

当你选择此选项时，Simulink 会在 Variant Sink 模块的每个端口上标注变体条件表达式。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowConditionOnBlock` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2016a 中引入**

### R2025a：在编辑时检测未定义的变体控制变量

Variant Source 和 Variant Sink 模块在模型编辑期间会通过为未定义的变体控制变量显示红色边框来发出错误。要查看错误描述，请将鼠标暂停在突出显示的模块上，然后单击错误符号以打开带有预定义修复的 notification 对话框。选择最合适的修复，然后单击 **Fix** 按钮。你可能需要提供其他信息来解决错误。如果成功，红色边框会消失。如果不成功，则会出现失败消息。
