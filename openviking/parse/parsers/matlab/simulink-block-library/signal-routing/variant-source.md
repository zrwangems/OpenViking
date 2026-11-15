---
type: simulink-block
title: 'Variant Source'
family: signal-routing
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'variantsource'
---

# Variant Source

Route among multiple inputs using variants

## 中文

使用变体在多个输入之间进行路由

### 库

Simulink / Signal Routing

### 描述

Variant Source 模块使您能够在单层中，在信号源处包含组件的多个实现。

例如，假设您想要仿真此模型，以通过使用不同的雨量传感器来控制汽车挡风玻璃雨刮器的速度。Variant Source 模块在不同的雨量传感器之间切换。控制逻辑使用此信息将结果输出到 Variant Sink 模块。然后，Variant Sink 模块在仿真期间切换为雨刮器电机模型，并在代码生成期间切换为发送到传感器的命令。这些变体模块基于您选择的变体模块中的变体控制模式类型在选项之间切换。有关详细信息，请参阅变体控制简介。

**注意**

在仿真期间，连接到 Variant Source 模块输入端的变体选择中，最多有一个处于活动状态。

使用 Variant Source 模块控制汽车挡风玻璃速度的多个实现

Variant Source 模块有一个或多个输入端口，并且只有一个输出端口。您可以将变化的选项连接到该模块的输入端口，以便在模型执行期间最多有一个选项处于活动状态。

Variant Source 模块与一个变体控制模式和一个变体激活时间相关联。变体控制模式确定如何指定变体控制。变体激活时间确定激活选项的时间，并决定在生成的代码中是仅包含活动选项，还是同时包含活动和非活动选项。在仿真期间，Simulink® 将活动选项直接连接到 Variant Source 模块的输出端口，并忽略非活动选项。

使用 Variant Source 模块允许您：

- 在整个模型中传播变体条件。
- 在模型的单层中可视化变体选择的所有可能实现，从而提高模型可读性。
- Simulink 消除整个模型中的非活动模块，从而提高运行时性能。如果所有变体选择都处于非活动状态，Simulink 会从模型中完全移除该变体区域。
- 变体源和接收器提供变体组件接口，您可以使用这些接口快速对变体选择进行建模。

模块图标上变体徽章的颜色和图标会根据 **变体激活时间**、**变体控制模式** 和 **允许零个活动变体控制** 参数的值而变化。有关详细信息，请参阅变体徽章。

### 端口

#### 输入

#### **Port\_1** — 与第一个变体控制关联的输入端口 标量 | 向量 | 矩阵

与第一个变体控制关联的输入端口。计算结果为 `true` 的变体控制确定哪个输入端口处于活动状态。

您可以通过将鼠标悬停在模块侧面，或将信号拖到模块边界附近，在 Variant Source 模块上自动插入输入端口。您可以通过按键盘上的 delete 键或使用鼠标单击来删除该端口。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

#### **Port\_N** — 与第 *N* 个变体控制关联的输入端口 标量 | 向量 | 矩阵

与第 *N* 个变体控制关联的输入端口。计算结果为 `true` 的变体控制确定哪个输入端口处于活动状态。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
#### 输出

#### **Port\_1** — 活动变体的输出 标量 | 向量 | 矩阵

来自活动变体的输出信号。

您可以通过将鼠标悬停在模块侧面，或将信号拖到模块边界附近，在 Variant Source 模块上自动插入输出端口。您可以通过按键盘上的 delete 键或使用鼠标单击来删除该端口。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### 参数

#### **变体控制模式** — 变体控制模式 `expression` (默认) | `label` | `sim codegen switching`

确定活动变体选择的变体控制可以是以下任意类型。

- `expression` — 软件基于变体条件的计算结果选择活动变体。当条件表达式的计算结果为 `true` 时，对应的变体选择变为活动状态。当条件表达式的计算结果为 `false` 时，对应的变体选择变为非活动状态。请参阅使用变体模块中的条件表达式在选项之间切换。
- `label` — 软件基于变体名称选择活动变体。变体控制是一个字符串，不需要您在任何工作区中创建任何变量。请参阅使用变体模块中的标签在选项之间切换。
- `sim codegen switching` — 在仿真和代码生成工作流之间自动切换变体，而无需创建任何工作区变量。当您仿真模型时，软件会自动选择 `sim` 分支作为活动选择。同样，当您执行 software-in-the-loop (SIL) 或 processor-In-Loop (PIL) 仿真、生成代码或使用外部模式时，软件会自动选择 `codegen` 分支。请参阅在不使用控制变量的情况下在变体模块中为仿真和代码生成工作流切换选项。

有关变体控制模式的详细信息，请参阅变体控制简介。有关不同类型变体控制模式之间的比较，请参阅比较变体模块中不同类型的变体控制模式。

#### 依赖关系

不同变体激活时间的可用性取决于您指定的 **变体控制模式** 类型。**变体激活时间** 参数确定软件设置活动选择的时间。该参数还确定在生成的代码中包含哪些可变性。下表说明了每种变体控制模式支持的变体激活时间。

| **变体激活时间** | | | | |
| --- | --- | --- | --- | --- |
| **变体控制模式** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` |
| `expression` | ✓ | ✓ | ✓ | ✓ |
| `label` | ✓ | x | x | x |
| `sim codegen switching` | ✓ | ✓ | x | x |

#### 编程用法

|  |
| --- |
| **模块参数:** `VariantControlMode` |
| **类型:** character vector |
| **值:** `'expression'` | `'label'` | `'sim codegen switching'` |
| **默认值:** `'expression'` |

#### **变体激活时间** — 软件选择活动变体选择的时间 `update diagram` (默认) | `update diagram analyze all choices` | `code compile` | `startup` | `inherit from Simulink.VariantControl`

此参数确定在仿真和代码生成工作流中包含哪些可变性。有关详细信息，请参阅在仿真和代码生成工作流的不同阶段激活变体。

- `update diagram` — 当您执行模型时，仿真和代码生成工作流中仅包含活动选择。生成的代码仅包含活动选择。
- `update diagram analyze all choices` — 当您执行模型时，会分析活动和非活动选择在整个模型中的一致性。但是，仿真和代码生成工作流中仅包含活动选择。生成的代码仅包含活动选择。
- `code compile` — 当您执行模型时，会分析活动和非活动选择在整个模型中的一致性，并且所有选择都包含在仿真和代码生成工作流中。生成的代码同时包含活动和非活动选择，并封闭在预处理器条件 `#if` 和 `#elif` 中。但是，从生成的代码构建的可执行文件仅包含活动选择。
- `startup` — 当您执行模型时，会分析活动和非活动选择在整个模型中的一致性，并且所有选择都包含在仿真和代码生成工作流中。使用此选项，您可以使用快速重启来提高迭代仿真的速度。有关详细信息，请参阅使用快速重启为变体系统运行迭代仿真而无需重新编译模型。从模型生成的代码同时包含活动和非活动选择，并封闭在常规 `if` 条件中。从生成的代码构建的可执行文件也同时包含活动和非活动选择。
- `inherit from Simulink.VariantControl` — 当您执行模型时，模块从其类型为 `Simulink.VariantControl` 的变体控制变量继承激活时间。如果变体模块有多个类型为 `Simulink.VariantControl` 的变体控制变量，则所有这些变量必须具有相同的激活时间。

#### 依赖关系

不同变体激活时间的可用性取决于您指定的变体控制模式类型。**变体激活时间** 参数确定软件设置活动选择的时间。该参数还确定在生成的代码中包含哪些可变性。下表说明了每种变体控制模式支持的变体激活时间。

| **变体激活时间** | | | | |
| --- | --- | --- | --- | --- |
| **变体控制模式** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` |
| `expression` | ✓ | ✓ | ✓ | ✓ |
| `label` | ✓ | x | x | x |
| `sim codegen switching` | ✓ | ✓ | x | x |

#### 编程用法

|  |
| --- |
| **模块参数:** `VariantActivationTime` |
| **类型:** character vector |
| **值:** `'update diagram'` | `'update diagram analyze all choices'` | `'code compile'` | `'startup'` |
| **默认值:** `'update diagram'` |

#### **端口及相关条件** — 变体选择、变体控制和条件的表 空表 (默认)

该表为连接到 Variant Source 模块输入端的每个变体选择包含一行。如果没有变体选择，则该表为空。

您可以使用 **端口及相关条件** 表左侧的按钮来修改表中的元素。

| 要... | 点击... |
| --- | --- |
| **添加新输入端口**：创建一个新输入端口作为变体选择，并在表中为该新选择添加一个条目。 | 添加新输入端口按钮 |
| **删除所选端口**：从模块中删除所选变体选择，并从表中删除其条目。 | 删除所选端口按钮 |
| **创建/编辑所选变体对象**：在全局工作区中为所选变体选择创建或编辑 `Simulink.VariantExpression` 对象，并使用 `Simulink.VariantExpression` 对象参数对话框指定变体条件。  **注意**  对于使用基础工作区的模型，此操作会在基础工作区中创建 `Simulink.VariantExpression` 对象，并且该对象仅对当前 MATLAB 会话可用。要永久存储数据，请将该对象保存到 MAT 文件或 MATLAB 脚本中。 | 创建或编辑所选变体对象按钮 |

#### **端口** — 已连接输入端口的编号 无默认值

连接到 Variant Source 模块上游的一个变体选择的输入端口编号。此值为只读。

单击添加新输入端口按钮以添加端口，或单击删除所选端口按钮以删除现有端口。

#### **变体控制标签** — `label` 模式下选择的名称 `true` 或 `false` (默认) | string

选择的名称，指定为 string。

#### 依赖关系

要启用此参数，请将 **变体控制模式** 设置为 `label`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `VariantControls` |
| **值:** | 与变体选择关联的变体控制 |
| **数据类型:** | `char` |

**示例:** `set_param(gcb, 'VariantControls', {'A == 1','A == 2'})`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

**示例:** `get_param(gcb, 'VariantControls')`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

#### **变体控制开关** — 用于仿真和代码生成工作流的变体选择 `(sim)` | `(codegen)`

指定 `(sim)` 以在仿真期间激活对应的变体选择。指定 `(codegen)` 以在执行代码生成工作流（例如 SIL、PIL、外部模式等）时激活对应的变体选择。

#### 依赖关系

要启用此参数，请将 **变体控制模式** 设置为 `sim codegen switching`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `VariantControls` |
| **值:** | 与变体选择关联的变体控制 |
| **数据类型:** | `char` |

**示例:** `set_param(gcb, 'VariantControls', {'(sim)','(codegen)'})`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

**示例:** `get_param(gcb, 'VariantControls')`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

#### **变体控制表达式** — 确定活动选择的条件表达式 `true` 或 `false` (默认) | 布尔条件表达式 | 表示布尔条件表达式的 `Simulink.VariantExpression` 对象 | `(default)`

指定用于确定活动选择的条件表达式。当条件表达式的计算结果为 `true` 时，软件激活对应的变体选择。当条件表达式的计算结果为 `false` 时，软件停用对应的变体选择。

变体控制可以是：

- 用于快速原型的布尔条件表达式。例如 `A == 1`、`A ~= B`、`A && B == 1` 等。
- 包含条件表达式以复用条件的 `Simulink.VariantExpression` 对象。请参阅 Simulink.VariantExpression 对象以复用变体模块的变体条件。
- 如果没有任何选择的计算结果为 `true`，则为默认变体选择。

这里，`A` 和 `B` 是称为*变体控制变量*的操作数。`==`、`~=` 和 `&&` 是条件表达式中的运算符。条件表达式可以包含一个或多个此类变体控制变量和运算符。有关变体控制变量支持的类型和存储位置的信息，请参阅变体模块中变体控制变量（操作数）的类型和变体模块中变体控制变量（操作数）的存储位置。有关运算符的信息，请参阅不同激活时间下变体模块中的运算符类型。

有关详细信息，请参阅使用变体模块中的条件表达式在选项之间切换。

在 Variant Assembly Subsystem 模块中，此参数是自动生成的布尔表达式列表，其中 **变体控制变量** 位于表达式的左侧，**变体枚举选择** 的成员位于表达式的右侧。表达式的两侧通过 `==` 连接。此参数为只读。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

Variant Subsystem 模块：

|  |  |
| --- | --- |
| **参数:** | `VariantControl` |
| **值:** | 与变体选择关联的变体控制 |
| **数据类型:** | `char` |

**示例:** `set_param(gcb, 'VariantControl', 'V == 3')`，其中 `gcb` 是 Variant Subsystem 模块的变体选择。

**示例:** `get_param(gcb, 'VariantControl')`，其中 `gcb` 是 Variant Subsystem 模块的变体选择。

Variant Source 和 Variant Sink 模块：

|  |  |
| --- | --- |
| **参数:** | `VariantControls` |
| **值:** | 与变体选择关联的变体控制 |
| **数据类型:** | `char` |

**示例:** `set_param(gcb, 'VariantControls', {'A == 1','A == 2'})`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

**示例:** `get_param(gcb, 'VariantControls')`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

#### **条件（只读）** — `Simulink.VariantExpression` 对象中的条件表达式 只读: `N/A` (默认)

此参数为只读。

此参数显示指定为 `Simulink.VariantExpression` 对象的条件表达式。要更改或编辑条件表达式，请使用双击工作区中的对象时出现的 `Simulink.VariantExpression` 参数对话框。

**注意**

您在类型为 `Simulink.VariantExpression` 的条件表达式中指定的操作数必须在基础工作区或数据字典中定义。不支持指定在封装或模型工作区中定义的操作数。

#### **标签模式活动选择** — `label` 模式下活动选择的名称 `true (Subsystem)` (默认) | `false (Subsystem1)`

此列表包含所有变体选择的标签。要设置活动选择，请从列表中选择一个标签。对应的选择将变为活动状态。或者，要更改标签模式下的活动选择，您可以遵循使用变体控制标签设置活动选择中所述的方法。

#### 依赖关系

要启用此参数，请将 **变体控制模式** 设置为 `label`。

#### 编程用法

|  |
| --- |
| **参数:** `LabelModeActiveChoice` |
| **类型:** character vector |
| **值:** 如果未指定标签模式活动选择，则该值为空。如果指定了标签模式活动选择，则该值为活动选择的变体控制标签。 |
| **默认值:** `''` |

#### **允许零个活动变体控制** — 在没有活动变体选择的情况下仿真模型 `off` (默认) | `on`

- `off` — 当没有活动变体选择时，Simulink 生成错误。
- `on` — 当您选择此参数并且没有活动变体选择时，Simulink 会在没有任何活动变体选择连接到 Variant Source 模块的情况下仿真模型。Simulink 断开与 Variant Source 模块输入和输出流连接的所有模块，从而从模型执行中完全移除变体区域。

  在生成的代码中，与 Variant Source 模块输入和输出流连接的所有模块都变为条件性的。

考虑“描述”部分中的汽车挡风玻璃雨刮器示例。假设您只想仿真手动挡风玻璃汽车雨刮器，并且不需要模型中的任何雨量传感器设置。当您将 **允许零个活动变体控制** 设置为 `on`，并且 `Rain Sensor Variant Source` 模块中没有活动变体选择时，Simulink 会断开 `Rain Sensor Variant Source` 模块及其所有连接的模块，从而从模型中完全移除变体区域。

下表显示了对于 `code compile` 激活时间，使用和不使用 **允许零个活动变体控制** 参数时生成的代码。在将 **允许零个活动变体控制** 设置为 `off` 时生成的代码中，仅变体选择 `Rain Sensor Model 1` 和 `Rain Sensor Model 2` 是条件性的。F1 模块是无条件的，因此它会对任一选择执行。此代码仅支持任一选择计算结果为 `true` 的场景。如果没有任何选择计算结果为 `true`，则这两个选择都会从编译中移除。F1 模块接收到无效输入，这会导致错误。在将 **允许零个活动变体控制** 设置为 `on` 时生成的代码中，变体选择 `Rain Sensor Model 1`、`Rain Sensor Model 2` 以及连接的 `F1` 模块都是条件性的。因此，如果没有任何选择的计算结果为 `true`，则 `F1` 模块也会被移除，从而使您能够从代码编译中完全移除变体区域。

| 未启用 **允许零个活动变体控制** 时生成的代码 | 启用 **允许零个活动变体控制** 时生成的代码 |
| --- | --- |
| ``` # if R == 1   /* logic for Rain Sensor Model 1; */ # elif R == 2   /* logic for Rain Sensor Model 2; */ # endif  /* If none of the conditions R == 1 or R == 2 evaluate to true,  the filter F1 receives an invalid input which resuls in an error.*/  /* logic for filter F1; */ ``` | ``` # if R == 1   /* logic for Rain Sensor Model 1; */ # elif R == 2   /* logic for Rain Sensor Model 2; */ # endif  /* The logic for filter F1 is executed only if  either of the conditions evaluate to true.  F1 is removed from code compilation if none of the condition evaluates to true. */  # if (R == 1) ∥ (R == 2)   /* logic for filter F1; */  # endif ``` |

#### 依赖关系

仅当您将 **变体控制模式** 设置为 `expression` 时，此参数才可用。

#### 编程用法

|  |
| --- |
| **模块参数:** `AllowZeroVariantControls` |
| **类型:** character vector |
| **值:** `'off'` | `'on'` |
| **默认值:** `'off'` |

#### **输出函数调用** — 接收并输出函数调用信号 `off` (默认) | `on`

当您选择此参数时，Simulink 使 Variant Source 模块能够在其输入端口接收函数调用信号，并在其输出端口有条件地合并这些信号。有关详细信息，请参阅从 Variant Source 输出端口到函数调用子系统的变体信号。

#### 编程用法

|  |
| --- |
| **模块参数:** `OutputFunctionCall` |
| **类型:** character vector |
| **值:** `'off'` | `'on'` |
| **默认值:** `'off'` |

#### **在模块上显示变体条件** — 标注模块端口 `off` (默认) | `on`

当您选择此选项时，Simulink 会在 Variant Source 模块的每个端口上标注变体条件表达式。

#### 编程用法

|  |
| --- |
| **模块参数:** `ShowConditionOnBlock` |
| **类型:** character vector |
| **值:** `'off'` | `'on'` |
| **默认值:** `'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史

**在 R2016a 中引入**

#### R2025a: 在编辑时检测未定义的变体控制变量

Variant Source 和 Variant Sink 模块在模型编辑期间对未定义的变体控制变量显示红色边框，从而发出错误。要查看错误描述，请将鼠标暂停在突出显示的模块上，然后单击错误符号以打开带有预定义修复的 notification dialog box。选择最合适的修复，然后单击 **Fix** 按钮。您可能需要提供其他信息来解决错误。如果成功，红色边框会消失。如果未成功，则会出现失败消息。

## Libraries

Simulink / Signal Routing

## Description

The Variant Source block enables you to include multiple
implementations of a component on the source of a signal in a single layer.

For example, suppose you want to simulate this model to control the speed of the car
windshield wiper by using different rain sensors. The Variant Source
block switches between different rain sensors. The control logic uses this information
to output the result to the Variant Sink block. The Variant
Sink block then switches between the wiper motor model during simulation and
the command to the sensor during code generation. The variant blocks switch between
choices based on the Types of Variant Control Modes in Variant Blocks you select. For
more information, see Introduction to Variant Controls.

**Note**

At most, one variant choice connected to input port of the Variant
Source block is active during simulation.

Multiple implementations to control speed of car windshield using a Variant Source block

The Variant Source block has one or more input ports and only one
output port. You can connect the varying choices to the input port of the block so that,
at most, one choice is active during model execution.

The Variant Source block is associated with a Variant control mode and a
Variant activation time. The
variant control mode determines how to specify the variant control. The variant
activation time determines a time to activate the choices and to decide whether to
include only the active choice or both active and inactive choices in the generated
code. During simulation, Simulink® connects the active choice directly to the output port of the
Variant Source block and ignores the inactive choices.

Using a Variant Source block allows you to:

- Propagate variant conditions throughout the model.
- Visualize all possible implementations of variant choices in a single
  layer of your model, which improves model readability.
- Simulink eliminates inactive blocks throughout the model, which
  improves runtime performance. If all the variant choices are inactive,
  Simulink removes the variant region completely from your model.
- Variant sources and sinks provide variant component interfaces that you
  can use to quickly model variant choices.

The color and icon of the variant badge on the block icon changes depending on the values of
the **Variant activation time**, **Variant control
mode**, and **Allow zero active variant controls**
parameters. For more information, see Variant Badges.

## Ports

### Input

### **Port\_1** — Input port associated with first variant control scalar | vector | matrix

Input port associated with the first variant control. The variant control that evaluates
to `true`, determines which input port is
active.

You can auto insert inport on the Variant Source block
by hovering the mouse over the block side or by dragging the signal near
the block boundary. You can delete the port by either clicking delete on
the keyboard or with a mouse click.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **Port\_N** — Input port associated with *N*th variant control scalar | vector | matrix

Input port associated with the *N*th variant control.
The variant control that evaluates to `true` determines
which input port is active.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### Output

### **Port\_1** — Output of active variant scalar | vector | matrix

Output signal from the active variant.

You can auto insert outport on the Variant Source block
by hovering the mouse over the block side or by dragging the signal near
the block boundary. You can delete the port by either clicking delete on
the keyboard or with a mouse click.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## Parameters

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

| **Variant activation time** | | | | |
| --- | --- | --- | --- | --- |
| **Variant control mode** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` |
| `expression` | ✓ | ✓ | ✓ | ✓ |
| `label` | ✓ | x | x | x |
| `sim codegen switching` | ✓ | ✓ | x | x |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantControlMode` |
| **Type:** character vector |
| **Values:** `'expression'` | `'label'` | `'sim codegen switching'` |
| **Default:** `'expression'` |

### **Variant activation time** — Time when software chooses active variant choice `update diagram` (default) | `update diagram analyze all choices` | `code compile` | `startup` | `inherit from Simulink.VariantControl`

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
- `inherit from Simulink.VariantControl` — When you
  execute the model, the block inherits the activation time from its variant
  control variables of type `Simulink.VariantControl`. If a variant block has multiple variant
  control variables of type `Simulink.VariantControl`, then all those
  variables must have the same activation time.

#### Dependencies

The availability of different variant activation times depends on the type of the
variant control mode that you specify. The **Variant activation
time** parameter determines when the software sets the active choice.
The parameter also determines which variability to include in the generated code.
This table explains the variant activation time supported by each variant control
mode.

| **Variant activation time** | | | | |
| --- | --- | --- | --- | --- |
| **Variant control mode** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` |
| `expression` | ✓ | ✓ | ✓ | ✓ |
| `label` | ✓ | x | x | x |
| `sim codegen switching` | ✓ | ✓ | x | x |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantActivationTime` |
| **Type:** character vector |
| **Values:** `'update diagram'` | `'update diagram analyze all choices'` | `'code compile'` | `'startup'` |
| **Default:** `'update diagram'` |

### **Port and associated conditions** — Table of variant choices, variant controls, and conditions empty table (default)

The table has a row for each variant choice connected to the input port of
the Variant Source block. If there are no variant choices,
the table is empty.

You can use buttons to the left of the **Port and associated
conditions** table to modify the elements in the table.

| To... | Click... |
| --- | --- |
| **Add a new input port**: Create a new input port as a variant choice and add an entry for the new choice in the table. | the add a new input port button |
| **Delete selected port**: Delete the selected variant choice from the block and its entry from the table. | the delete selected port button |
| **Create/Edit selected variant object**: Create or edit a `Simulink.VariantExpression` object for the selected variant choice in the global workspace and specify the variant condition using the `Simulink.VariantExpression` object parameter dialog box.  **Note**  For a model that uses the base workspace, this operation creates the `Simulink.VariantExpression` object in the base workspace, and the object is available only for the current MATLAB session. To permanently store the data, save the object in a MAT file or MATLAB script. | the Create or Edit selected variant object button |

### **Port** — Number of connected input port no default

Number of the input port that is connected to one variant choice upstream
of the Variant Source block. This value is read-only.

Click the add a new input port button to add a port or the delete selected port button to delete an existing one.

### **Variant control label** — Name of choice in `label` mode `true` or `false` (default) | string

A name for a choice, specified as a string.

#### Dependencies

To enable this parameter, set **Variant control
mode** to `label`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `VariantControls` |
| **Values:** | variant controls that are associated with variant choices |
| **Data Types:** | `char` |

**Example:** `set_param(gcb, 'VariantControls', {'A == 1','A ==
2'})`, where `gcb` is the
Variant Sink or Variant Source
block.

**Example:** `get_param(gcb, 'VariantControls')`,
where `gcb` is the Variant Sink or
Variant Source block.

### **Variant control switch** — Variant choices for simulation and code generation workflows `(sim)` | `(codegen)`

Specify `(sim)` to activate the corresponding variant
choice during simulation. Specify `(codegen)` to activate
the corresponding variant choice while performing code generation workflows
such as SIL, PIL, external mode, and so on.

#### Dependencies

To enable this parameter, set **Variant control
mode** to `sim codegen
switching`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `VariantControls` |
| **Values:** | variant controls that are associated with variant choices |
| **Data Types:** | `char` |

**Example:** `set_param(gcb, 'VariantControls',
{'(sim)','(codegen)'})`, where `gcb`
is the Variant Sink or Variant Source
block.

**Example:** `get_param(gcb, 'VariantControls')`,
where `gcb` is the Variant Sink or
Variant Source block.

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

### **Allow zero active variant controls** — Simulate model without active variant choice `off` (default) | `on`

- `off` — Simulink generates an error when there is no active variant
  choice.
- `on` — When you select this parameter and if
  there is no active variant choice, Simulink simulates the model without any active variant choice
  connected to the Variant Source block. Simulink disconnects all the blocks connected to the input and
  output stream of Variant Source block, thus removing
  the variant regions completely from the model execution.

  In the generated code, all the blocks that are connected to the
  input and output stream of the Variant Source block
  becomes conditional.

Consider the car windshield wiper example in the Description section. Suppose you want to
simulate only a manual windshield car wiper and you do not need any of the
rain sensor settings in the model. When you set **Allow zero active
variant controls** to `on` and if there is no
active variant choice in the `Rain Sensor Variant Source`
block, Simulink disconnects the `Rain Sensor Variant Source`
block and all its connected blocks, which removes the variant region
completely from the model.

This table shows the code that you generate with and without the **Allow zero
active variant controls** parameter for the `code
compile` activation time. In the code that you generate
with **Allow zero active variant controls** set to
`off`, only the variant choices `Rain Sensor
Model 1` and the `Rain Sensor Model 2` are
conditional. The F1 block is unconditional, and so it
executes for either of the choices. This code support only scenarios where
either of the choices evaluate to `true`. If none of the
choices evaluate to `true`, both the choices are removed
from compilation. The F1 block receives an invalid input and
this results in an error. In the code that you generate with **Allow
zero active variant controls** set to `on`,
the variant choices `Rain Sensor Model 1`, `Rain
Sensor Model 2`, and the connected `F1` blocks
are conditional. So, if none of the choices evaluate to
`true`, the `F1` block is also removed
thus enabling you to completely remove the variant region from code
compilation.

| Generated code without **Allow zero active variant controls** | Generated code with **Allow zero active variant controls** |
| --- | --- |
| ``` # if R == 1   /* logic for Rain Sensor Model 1; */ # elif R == 2   /* logic for Rain Sensor Model 2; */ # endif  /* If none of the conditions R == 1 or R == 2 evaluate to true,  the filter F1 receives an invalid input which resuls in an error.*/  /* logic for filter F1; */ ``` | ``` # if R == 1   /* logic for Rain Sensor Model 1; */ # elif R == 2   /* logic for Rain Sensor Model 2; */ # endif  /* The logic for filter F1 is executed only if  either of the conditions evaluate to true.  F1 is removed from code compilation if none of the condition evaluates to true. */  # if (R == 1) ∥ (R == 2)   /* logic for filter F1; */  # endif ``` |

#### Dependencies

This parameter is available only if you set **Variant control
mode** to `expression`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AllowZeroVariantControls` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Output function call** — Receive and output function-call signals `off` (default) | `on`

When you select this parameter, Simulink enables the Variant Source block to receive
function-call signals at its input ports and conditionally merge the signals
at its output port. For more information, see Variant Signals from Variant Source Outport to Function-Call Subsystem.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputFunctionCall` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Show variant condition on block** — Annotate block ports `off` (default) | `on`

When you select this option, Simulink annotates the variant condition expression on each port of the
Variant Source block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowConditionOnBlock` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2016a**

### R2025a: Detect undefined variant control variables during edit-time

The Variant Source and Variant Sink blocks issue errors
by displaying a red border for undefined variant control variables during
model editing. To see a description of the error, pause on the highlighted
block, and then click the error symbol to open the notification dialog box
with predefined fixes. Select the most appropriate fix, and click the
**Fix** button. You may need to provide
additional information to resolve the error. If successful, the red border
disappears. If not, a failure message appears.
