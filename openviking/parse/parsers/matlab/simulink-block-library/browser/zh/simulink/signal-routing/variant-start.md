---
type: simulink-block
title: 'Variant Start'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Signal Routing'
documentation_page: 'variantstart'
documentation_source_path: 'slref/variantstart.html'
language: zh-CN
chinese_source: worker-translation
---

# Variant Start

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

要连接到活动输出端口的输入信号。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `struct`

### 输出

### **Port\_1** — 输出分支 标量 | 向量 | 矩阵

与 Variant End 模块的对应输入端口一起构成有界区域起点的输出分支。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_N** — 来自第 *N* 个分支的输出 标量 | 向量 | 矩阵

来自第 *N* 个分支的输出信号。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **Variant Start End Tag** — 有界区域的唯一标识符 `A` (默认) | 有效的 MATLAB® 标识符

用于标识构成有界区域的正确 Variant Start 和 Variant End 对的唯一标识符，指定为有效的 MATLAB 标识符。有效的 MATLAB 标识符是由字母数字（A–Z、a–z、0–9）和下划线组成的字符向量，使得第一个字符是字母，并且字符向量的长度小于或等于 `namelengthmax`。

#### 程序化使用

|  |
| --- |
| **模块参数:** `VariantStartEndTag` |
| **类型:** character vector |
| **值:** `'A'` | 有效的 MATLAB 标识符 |
| **默认值:** `'A'` |

### **Variant control mode** — Variant control mode `expression` (默认) | `label` | `sim codegen switching`

确定活动变体选项的变体控制可以是以下任何类型。

- `expression` — 软件根据变体条件的评估选择活动变体。当条件表达式计算结果为 `true` 时，相应的变体选项变为活动状态。当条件表达式计算结果为 `false` 时，相应的变体选项变为非活动状态。请参阅 Switch Between Choices Using Condition Expressions in Variant Blocks。
- `label` — 软件根据变体的名称选择活动变体。变体控制是一个字符串，不需要您在任何工作区中创建任何变量。请参阅 Switch Between Choices Using Labels in Variant Blocks。
- `sim codegen switching` — 在仿真和代码生成工作流之间自动切换变体，而无需创建任何工作区变量。当您仿真模型时，软件自动选择 `sim` 分支作为活动选项。类似地，当您执行软件在环 (SIL) 或处理器在环 (PIL) 仿真、生成代码或使用外部模式时，软件自动选择 `codegen` 分支。请参阅 Switch Between Choices for Simulation and Code Generation Workflows Without Using Control Variables in Variant Blocks。

有关变体控制模式的详细信息，请参阅 Introduction to Variant Controls。有关不同类型的变体控制模式之间的比较，请参阅 Compare Different Types of Variant Control Modes in Variant Blocks。

#### 依赖关系

不同变体激活时间的可用性取决于您指定的 **Variant control mode** 的类型。**Variant activation time** 参数确定软件设置活动选项的时间。该参数还确定生成的代码中包含哪些可变性。下表说明了每种变体控制模式支持的变体激活时间。

| **Variant activation time** | | | | |
| --- | --- | --- | --- | --- |
| **Variant control mode** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` |
| `expression` | ✓ | ✓ | ✓ | ✓ |
| `label` | ✓ | x | x | x |
| `sim codegen switching` | ✓ | ✓ | x | x |

#### 程序化使用

|  |
| --- |
| **模块参数:** `VariantControlMode` |
| **类型:** character vector |
| **值:** `'expression'` | `'label'` | `'sim codegen switching'` |
| **默认值:** `'expression'` |

### **Variant activation time** — 软件选择活动变体选项的时间 `update diagram` (默认) | `update diagram analyze all choices` | `code compile` | `startup` | `inherit from Simulink.VariantControl`

此参数确定仿真和代码生成工作流中包含哪些可变性。有关详细信息，请参阅 Activate Variant During Different Stages of Simulation and Code Generation Workflow。

- `update diagram` — 当您执行模型时，只有活动选项包含在仿真和代码生成工作流中。生成的代码仅包含活动选项。
- `update diagram analyze all choices` — 当您执行模型时，会分析活动和非活动选项在整个模型中的一致性。但是，只有活动选项包含在仿真和代码生成工作流中。生成的代码仅包含活动选项。
- `code compile` — 当您执行模型时，会分析活动和非活动选项在整个模型中的一致性，并且所有选项都包含在仿真和代码生成工作流中。生成的代码包含括在预处理器条件 `#if` 和 `#elif` 中的活动和非活动选项。但是，从生成的代码构建的可执行文件仅包含活动选项。
- `startup` — 当您执行模型时，会分析活动和非活动选项在整个模型中的一致性，并且所有选项都包含在仿真和代码生成工作流中。使用此选项，您可以使用快速重启提高迭代仿真的速度。有关详细信息，请参阅 Run Iterative Simulations Without Recompiling Model for Variant Systems Using Fast Restart。从模型生成的代码包含括在常规 `if` 条件中的活动和非活动选项。从生成的代码构建的可执行文件也包含活动和非活动选项。
- `inherit from Simulink.VariantControl` — 当您执行模型时，模块从其类型为 `Simulink.VariantControl` 的变体控制变量继承激活时间。如果变体模块具有多个类型为 `Simulink.VariantControl` 的变体控制变量，则所有这些变量必须具有相同的激活时间。

#### 依赖关系

不同变体激活时间的可用性取决于您指定的变体控制模式的类型。**Variant activation time** 参数确定软件设置活动选项的时间。该参数还确定生成的代码中包含哪些可变性。下表说明了每种变体控制模式支持的变体激活时间。

| **Variant activation time** | | | | |
| --- | --- | --- | --- | --- |
| **Variant control mode** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` |
| `expression` | ✓ | ✓ | ✓ | ✓ |
| `label` | ✓ | x | x | x |
| `sim codegen switching` | ✓ | ✓ | x | x |

#### 程序化使用

|  |
| --- |
| **模块参数:** `VariantActivationTime` |
| **类型:** character vector |
| **值:** `'update diagram'` | `'update diagram analyze all choices'` | `'code compile'` | `'startup'` |
| **默认值:** `'update diagram'` |

### **Port and associated conditions** — 变体选项、变体控制和条件的表 空表 (默认)

该表为连接到 Variant Start 模块输出端口的每个变体选项包含一行。如果没有变体选项，则该表为空。

您可以使用 **Port and associated conditions** 表左侧的按钮来修改表中的元素。

| 要... | 单击... |
| --- | --- |
| **添加新输出端口**: 创建一个新输出端口作为变体选项，并在表中为新选项添加条目。 | 添加新输出端口按钮 |
| **删除选定端口**: 从模块中删除选定的变体选项，并从表中删除其条目。 | 删除选定端口按钮 |
| **创建/编辑选定的变体对象**: 在全局工作区中为选定的变体选项创建或编辑 `Simulink.VariantExpression` 对象，并使用 `Simulink.VariantExpression` 对象参数对话框指定变体条件。  **注意**  对于使用基础工作区的模型，此操作会在基础工作区中创建 `Simulink.VariantExpression` 对象，该对象仅对当前 MATLAB 会话可用。要永久存储数据，请将对象保存在 MAT 文件或 MATLAB 脚本中。 | 创建或编辑选定的变体对象按钮 |

### **Port** — 已连接输出端口的数量 只读: 无默认值

此参数为只读。

连接到 Variant Start 模块上游的一个变体选项的输出端口编号。此值为只读。

单击添加新输出端口按钮以添加端口，或单击删除选定端口按钮以删除现有端口。

### **Variant control label** — `label` 模式下的选项名称 `true` 或 `false` (默认) | 字符串

选项的名称，指定为字符串。

#### 依赖关系

要启用此参数，请将 **Variant control mode** 设置为 `label`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `VariantControl` |
| **值:** | 与变体选项关联的变体控制 |
| **数据类型:** | `char` |

**示例:** `set_param(gcb, 'VariantControl', 'V == 3')`，其中 `gcb` 是 Variant Start 模块的变体选项。

**示例:** `get_param(gcb, 'VariantControl')`，其中 `gcb` 是 Variant Start 模块的变体选项。

### **Variant control expression** — 确定活动选项的条件表达式 `true` 或 `false` (默认) | 布尔条件表达式 | 表示布尔条件表达式的 `Simulink.VariantExpression` 对象 | `(默认)`

指定条件表达式以确定活动选项。当条件表达式计算结果为 `true` 时，软件激活相应的变体选项。当条件表达式计算结果为 `false` 时，软件停用相应的变体选项。

变体控制可以是：

- 用于快速原型的布尔条件表达式。例如，`A == 1`、`A ~= B`、`A && B == 1` 等。
- 包含用于条件重用的条件表达式的 `Simulink.VariantExpression` 对象。请参阅 Simulink.VariantExpression Objects for Variant Condition Reuse of Variant Blocks。
- 如果没有任何选项计算结果为 `true`，则为默认变体选项。

这里，`A` 和 `B` 是称为 *变体控制变量* 的操作数。`==`、`~=` 和 `&&` 是条件表达式中的运算符。条件表达式可以包含一个或多个此类变体控制变量和运算符。有关变体控制变量支持的类型和存储位置的信息，请参阅 Types of Variant Control Variables (Operands) in Variant Blocks 和 Storage Locations for Variant Control Variables (Operands) in Variant Blocks。有关运算符的信息，请参阅 Types of Operators in Variant Blocks for Different Activation Times。

有关详细信息，请参阅 Switch Between Choices Using Condition Expressions in Variant Blocks。

在 Variant Assembly Subsystem 模块中，此参数是自动生成的布尔表达式的列表，左侧是 **Variant control variable**，右侧是 **Variant enumeration choice** 的成员。表达式的两侧用 `==` 连接。此参数为只读。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

Variant Subsystem 模块：

|  |  |
| --- | --- |
| **参数:** | `VariantControl` |
| **值:** | 与变体选项关联的变体控制 |
| **数据类型:** | `char` |

**示例:** `set_param(gcb, 'VariantControl', 'V == 3')`，其中 `gcb` 是 Variant Subsystem 模块的变体选项。

**示例:** `get_param(gcb, 'VariantControl')`，其中 `gcb` 是 Variant Subsystem 模块的变体选项。

Variant Source 和 Variant Sink 模块：

|  |  |
| --- | --- |
| **参数:** | `VariantControls` |
| **值:** | 与变体选项关联的变体控制 |
| **数据类型:** | `char` |

**示例:** `set_param(gcb, 'VariantControls', {'A == 1','A == 2'})`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

**示例:** `get_param(gcb, 'VariantControls')`，其中 `gcb` 是 Variant Sink 或 Variant Source 模块。

### **Condition (read-only)** — `Simulink.VariantExpression` 对象中的条件表达式 只读: `N/A` (默认)

此参数为只读。

此参数显示指定为 `Simulink.VariantExpression` 对象的条件表达式。要更改或编辑条件表达式，请使用双击工作区中的对象时出现的 `Simulink.VariantExpression` 参数对话框。

**注意**

您在类型为 `Simulink.VariantExpression` 的条件表达式中指定的操作数必须在基础工作区或数据字典中定义。不支持指定在掩码或模型工作区中定义的操作数。

### **Label mode active choice** — `label` 模式下的活动选项名称 `true (Subsystem)` (默认) | `false (Subsystem1)`

此列表包含所有变体选项的标签。要设置活动选项，请从列表中选择一个标签。相应的选项将变为活动状态。或者，要更改标签模式下的活动选项，您可以按照 Set Active Choices Using Variant Control Labels 中描述的方法操作。

#### 依赖关系

要启用此参数，请将 **Variant control mode** 设置为 `label`。

#### 程序化使用

|  |
| --- |
| **参数:** `LabelModeActiveChoice` |
| **类型:** character vector |
| **值:** 如果未指定标签模式活动选项，则值为空。如果指定了标签模式活动选项，则该值为活动选项的变体控制标签。 |
| **默认值:** `''` |

### **Show variant condition on block** — 注释模块端口 `off` (默认) | `on`

当您选择此选项时，Simulink® 会在 Variant Start 模块的每个端口上注释变体条件表达式。

#### 程序化使用

|  |
| --- |
| **模块参数:** `ShowConditionOnBlock` |
| **类型:** character vector |
| **值:** `'off'` | `'on'` |
| **默认值:** `'off'` |

## 所属库

Simulink / Signal Routing

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

**R2024a 中引入**

## 描述

定义有界区域的起点

Variant Start block 定义有界区域的起点，允许您限制变体条件传播而不引入层级。使用 Variant End 定义有界区域的终点。对于每个 Variant Start block，都有一个对应的 Variant End block。当您在 Variant Start block 上指定变体条件时，对应的 Variant End block 会在编译时基于唯一的 **Variant Start End Tag** 继承这些条件和其它参数。

在给定层级中，如果满足以下条件，则 Variant Start block 的输出端口与对应 Variant End block 的输入端口之间的区域被定义为有界区域：

- 您可以创建一个子系统，该子系统包装选择内的所有模块而不与其它选择相交。因此，选择有清晰的分界。
- 您可以创建一个仅有一个输入端口（连接到 Variant Start block 的输出端口）且仅有一个输出端口（连接到目标的输出端口）的子系统。选择不会分支到该区域之外。
