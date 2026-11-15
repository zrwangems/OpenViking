---
type: simulink-block
title: 'Variant Start'
family: signal-routing
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'variantstart'
language: zh-CN
chinese_source: worker-translation
---

# Variant Start

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

要连接到活动输出端口的输入信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `struct`
### 输出

### **Port\_1** — 输出分支 标量 | 向量 | 矩阵

输出分支，与对应 Variant End block 的输入端口一起构成有界区域的起点。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_N** — 来自第 *N* 个分支的输出 标量 | 向量 | 矩阵

来自第 *N* 个分支的输出信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **Variant Start End Tag** — 有界区域的唯一标识符 `A`（默认） | 有效的 MATLAB® 标识符

用于标识构成有界区域的正确 Variant Start 和 Variant End 对的唯一标识符，指定为有效的 MATLAB 标识符。有效的 MATLAB 标识符是由字母数字（A–Z、a–z、0–9）和下划线组成的字符向量，其中第一个字符是字母，且字符向量长度小于或等于 `namelengthmax`。

#### 编程用法

|  |
| --- |
| **模块参数：** `VariantStartEndTag` |
| **类型：** 字符向量 |
| **值：** `'A'` | 有效的 MATLAB 标识符 |
| **默认值：** `'A'` |

### **Variant control mode** — Variant 控制模式 `expression`（默认） | `label` | `sim codegen switching`

确定活动变体选择的变体控制可以是以下任一类型。

- `expression` — 软件基于对变体条件的求值选择活动变体。当条件表达式求值为 `true` 时，对应的变体选择变为活动。当条件表达式求值为 `false` 时，对应的变体选择变为非活动。请参阅 Switch Between Choices Using Condition Expressions in Variant Blocks。
- `label` — 软件基于变体名称选择活动变体。变体控制是字符串，不要求你在任何工作区中创建任何变量。请参阅 Switch Between Choices Using Labels in Variant Blocks。
- `sim codegen switching` — 自动在用于仿真和代码生成工作流的变体之间切换，而无需创建任何工作区变量。当你仿真模型时，软件自动选择 `sim` 分支作为活动选择。类似地，当你执行 software-in-the-loop (SIL) 或 processor-In-Loop (PIL) 仿真、生成代码或使用外部模式时，软件自动选择 `codegen` 分支。请参阅 Switch Between Choices for Simulation and Code Generation Workflows Without Using Control Variables in Variant Blocks。

有关变体控制模式的详细信息，请参阅 Introduction to Variant Controls。有关不同类型变体控制模式的比较，请参阅 Compare Different Types of Variant Control Modes in Variant Blocks。

#### 依赖关系

不同变体激活时间的可用性取决于你指定的 **Variant control mode** 类型。**Variant activation time** 参数确定软件设置活动选择的时间。该参数还确定生成的代码中包含哪些可变性。下表说明了每种变体控制模式支持的变体激活时间。

| **Variant activation time** | | | | |
| --- | --- | --- | --- | --- |
| **Variant control mode** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` |
| `expression` | ✓ | ✓ | ✓ | ✓ |
| `label` | ✓ | x | x | x |
| `sim codegen switching` | ✓ | ✓ | x | x |

#### 编程用法

|  |
| --- |
| **模块参数：** `VariantControlMode` |
| **类型：** 字符向量 |
| **值：** `'expression'` | `'label'` | `'sim codegen switching'` |
| **默认值：** `'expression'` |

### **Variant activation time** — 软件选择活动变体选择的时间 `update diagram`（默认） | `update diagram analyze all choices` | `code compile` | `startup` | `inherit from Simulink.VariantControl`

此参数确定仿真和代码生成工作流中包含哪些可变性。有关详细信息，请参阅 Activate Variant During Different Stages of Simulation and Code Generation Workflow。

- `update diagram` — 当你执行模型时，只有活动选择包含在仿真和代码生成工作流中。生成的代码仅包含活动选择。
- `update diagram analyze all choices` — 当你执行模型时，活动和非活动选择都会在整个模型中进行一致性分析。但是，只有活动选择包含在仿真和代码生成工作流中。生成的代码仅包含活动选择。
- `code compile` — 当你执行模型时，活动和非活动选择都会在整个模型中进行一致性分析，并且所有选择都包含在仿真和代码生成工作流中。生成的代码包含活动和非活动选择，它们被包含在预处理器条件 `#if` 和 `#elif` 中。但是，从生成的代码构建的可执行文件仅包含活动选择。
- `startup` — 当你执行模型时，活动和非活动选择都会在整个模型中进行一致性分析，并且所有选择都包含在仿真和代码生成工作流中。使用此选项，你可以使用快速重启提高迭代仿真的速度。有关详细信息，请参阅 Run Iterative Simulations Without Recompiling Model for Variant Systems Using Fast Restart。从模型生成的代码包含活动和非活动选择，它们被包含在常规 `if` 条件中。从生成的代码构建的可执行文件也包含活动和非活动选择。
- `inherit from Simulink.VariantControl` — 当你执行模型时，模块从其类型为 `Simulink.VariantControl` 的变体控制变量继承激活时间。如果一个变体模块有多个类型为 `Simulink.VariantControl` 的变体控制变量，则所有这些变量必须具有相同的激活时间。

#### 依赖关系

不同变体激活时间的可用性取决于你指定的变体控制模式类型。**Variant activation time** 参数确定软件设置活动选择的时间。该参数还确定生成的代码中包含哪些可变性。下表说明了每种变体控制模式支持的变体激活时间。

| **Variant activation time** | | | | |
| --- | --- | --- | --- | --- |
| **Variant control mode** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` |
| `expression` | ✓ | ✓ | ✓ | ✓ |
| `label` | ✓ | x | x | x |
| `sim codegen switching` | ✓ | ✓ | x | x |

#### 编程用法

|  |
| --- |
| **模块参数：** `VariantActivationTime` |
| **类型：** 字符向量 |
| **值：** `'update diagram'` | `'update diagram analyze all choices'` | `'code compile'` | `'startup'` |
| **默认值：** `'update diagram'` |

### **Port and associated conditions** — 变体选择、变体控制和条件的表 空表（默认）

该表为连接到 Variant Start block 输出端口的每个变体选择包含一行。如果没有变体选择，则该表为空。

你可以使用 **Port and associated conditions** 表左侧的按钮来修改表中的元素。

| 要... | 单击... |
| --- | --- |
| **Add a new output port**：创建一个新输出端口作为变体选择，并在表中为新选择添加条目。 | add a new output port 按钮 |
| **Delete selected port**：从模块中删除选定的变体选择，并从表中删除其条目。 | delete selected port 按钮 |
| **Create/Edit selected variant object**：在全局工作区中为选定的变体选择创建或编辑 `Simulink.VariantExpression` 对象，并使用 `Simulink.VariantExpression` 对象参数对话框指定变体条件。  **注意**  对于使用基础工作区的模型，此操作会在基础工作区中创建 `Simulink.VariantExpression` 对象，并且该对象仅对当前 MATLAB 会话可用。要永久存储数据，请将该对象保存到 MAT 文件或 MATLAB 脚本中。 | Create or Edit selected variant object 按钮 |

### **Port** — 连接的输出端口编号 只读：无默认值

此参数为只读。

连接到 Variant Start block 上游某个变体选择的输出端口编号。此值为只读。

单击 add a new output port 按钮添加端口，或单击 delete selected port 按钮删除现有端口。

### **Variant control label** — `label` 模式下选择的名称 `true` or `false`（默认） | string

选择的名称，指定为字符串。

#### 依赖关系

要启用此参数，请将 **Variant control mode** 设置为 `label`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VariantControl` |
| **值：** | 与变体选择关联的变体控制 |
| **数据类型：** | `char` |

**示例：** `set_param(gcb, 'VariantControl', 'V == 3')`，其中 `gcb` 是 Variant Start block 的变体选择。

**示例：** `get_param(gcb, 'VariantControl')`，其中 `gcb` 是 Variant Start block 的变体选择。

### **Variant control expression** — 确定活动选择的条件表达式 `true` or `false`（默认） | 布尔条件表达式 | 表示布尔条件表达式的 `Simulink.VariantExpression` 对象 | `(default)`

指定用于确定活动选择的条件表达式。当条件表达式求值为 `true` 时，软件激活对应的变体选择。当条件表达式求值为 `false` 时，软件停用对应的变体选择。

变体控制可以是：

- 用于快速原型的布尔条件表达式。例如 `A == 1`、`A ~= B`、`A && B == 1` 等。
- 一个包含条件表达式以实现条件复用的 `Simulink.VariantExpression` 对象。请参阅 Simulink.VariantExpression Objects for Variant Condition Reuse of Variant Blocks。
- 如果没有任何选择求值为 `true`，则为 Default Variant Choice。

这里，`A` 和 `B` 是称为 *变体控制变量* 的操作数。`==`、`~=` 和 `&&` 是条件表达式中的运算符。条件表达式可以包含一个或多个此类变体控制变量和运算符。有关变体控制变量支持的类型和存储位置的信息，请参阅 Types of Variant Control Variables (Operands) in Variant Blocks 和 Storage Locations for Variant Control Variables (Operands) in Variant Blocks。有关运算符的信息，请参阅 Types of Operators in Variant Blocks for Different Activation Times。

有关详细信息，请参阅 Switch Between Choices Using Condition Expressions in Variant Blocks。

在 Variant Assembly Subsystem block 中，此参数是自动生成的布尔表达式列表，其中左侧为 **Variant control variable**，右侧为 **Variant enumeration choice** 的成员。表达式的两侧用 `==` 连接。此参数为只读。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

Variant Subsystem block：

|  |  |
| --- | --- |
| **参数：** | `VariantControl` |
| **值：** | 与变体选择关联的变体控制 |
| **数据类型：** | `char` |

**示例：** `set_param(gcb, 'VariantControl', 'V == 3')`，其中 `gcb` 是 Variant Subsystem block 的变体选择。

**示例：** `get_param(gcb, 'VariantControl')`，其中 `gcb` 是 Variant Subsystem block 的变体选择。

Variant Source 和 Variant Sink block：

|  |  |
| --- | --- |
| **参数：** | `VariantControls` |
| **值：** | 与变体选择关联的变体控制 |
| **数据类型：** | `char` |

**示例：** `set_param(gcb, 'VariantControls', {'A == 1','A == 2'})`，其中 `gcb` 是 Variant Sink 或 Variant Source block。

**示例：** `get_param(gcb, 'VariantControls')`，其中 `gcb` 是 Variant Sink 或 Variant Source block。

### **Condition (read-only)** — `Simulink.VariantExpression` 对象中的条件表达式 只读：`N/A`（默认）

此参数为只读。

此参数显示指定为 `Simulink.VariantExpression` 对象的条件表达式。要更改或编辑条件表达式，请使用在工作区中双击该对象时出现的 `Simulink.VariantExpression` 参数对话框。

**注意**

在类型为 `Simulink.VariantExpression` 的条件表达式中指定的操作数必须定义在基础工作区或数据字典中。不支持指定在 mask 或模型工作区中定义的操作数。

### **Label mode active choice** — `label` 模式下活动选择的名称 `true (Subsystem)`（默认） | `false (Subsystem1)`

此列表包含所有变体选择的标签。要设置活动选择，请从列表中选择一个标签。对应的选择变为活动。或者，要更改 `label` 模式下的活动选择，你可以遵循 Set Active Choices Using Variant Control Labels 中所述的方法。

#### 依赖关系

要启用此参数，请将 **Variant control mode** 设置为 `label`。

#### 编程用法

|  |
| --- |
| **参数：** `LabelModeActiveChoice` |
| **类型：** 字符向量 |
| **值：** 如果未指定 label 模式活动选择，则该值为空。如果指定了 label 模式活动选择，则该值为活动选择的变体控制标签。 |
| **默认值：** `''` |

### **Show variant condition on block** — 标注模块端口 `off`（默认） | `on`

当你选择此选项时，Simulink® 会在 Variant Start block 的每个端口上标注变体条件表达式。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowConditionOnBlock` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

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

**在 R2024a 中引入**

## 描述

定义有界区域的起点

Variant Start block 定义有界区域的起点，允许你在不引入层级的情况下限制变体条件传播。使用 Variant End 定义有界区域的终点。对于每个 Variant Start block，都有一个对应的 Variant End block。当你在 Variant Start block 上指定变体条件时，对应的 Variant End block 在编译时基于唯一的 **Variant Start End Tag** 继承这些条件和其他参数。

在给定的层级中，如果满足以下条件，则 Variant Start block 的输出端口与对应 Variant End block 的输入端口之间的区域被定义为有界区域：

- 你可以创建一个子系统，该子系统包装该选择内的所有模块，而不与其他选择相交。因此，选择有清晰的界限。
- 你可以创建一个仅有一个输入端口（连接到 Variant Start block 的输出端口）和仅有一个输出端口（连接到目的地的输出端口）的子系统。选择不会分支到该区域之外。
