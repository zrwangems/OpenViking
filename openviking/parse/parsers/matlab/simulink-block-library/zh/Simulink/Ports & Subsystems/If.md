---
type: simulink-block
title: 'If'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'if'
documentation_source_path: 'slref/if.html'
language: zh-CN
chinese_source: worker-translation
---

# If

## 端口

### 输入

### **逻辑操作数** — 用于计算逻辑表达式的值 标量 | 向量

输入 `u1,u2,...,un` 必须具有相同的数据类型。输入不能是任何用户定义类型，例如枚举类型。

If 模块不直接支持定点数据类型。但是，您可以使用 Compare To Constant 模块来规避此限制。请参阅 Select Subsystem Execution 中的定点数据类型支持。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **动作** — If Action Subsystem 模块的动作信号 标量

来自 `if`、`else` 和 `elseif` 端口的输出是发送到 If Action Subsystem 模块的动作信号。

## 参数

### **输入数量** — 指定输入端口数量 `1`（默认）| 整数

`1`
:   指定一个输入端口。

整数
:   指定输入端口数量。模块端口以字符 `'u'` 后跟数字标记，即 `1,2,...,n`，其中 `n` 等于您指定的输入数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumInputs` |
| **类型**：character vector |
| **值**：`'1'` | integer in quotes |
| **默认值**：`'1'` |

### **显示 else 条件** — 控制 else 端口的显示 `on`（默认）| `off`

当 **if** 端口和所有 **elseif** 端口表达式均为 `false` 时，**else** 端口发送动作信号以执行所连接的 If Action Subsystem 模块。

on
:   显示 **else** 端口。

off
:   隐藏 **else** 端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowElse` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **启用过零检测** — 控制过零检测 `on`（默认）| `off`

控制过零检测。

on
:   检测过零点。

off
:   不检测过零点。

#### 编程使用

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **在生成代码中提供 if-else 语句** — 在 If 模块生成的代码中仅包含 if-else 语句的选项 `off`（默认）| `on`

*自 R2025a 起*

选择此参数以确保 If 模块生成的代码中仅包含 if-else 语句。

on
:   生成的代码中仅包含 if-else 语句。此选项可防止生成的代码中包含 switch-case 语句。

off
:   当此参数为 off 时，If 模块生成的代码可能包含 switch-case 语句，这些语句执行与 If 模块相同的操作。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |
| --- |
| **模块参数**：`EnsureIfElseCode` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **if** — 逻辑表达式 `u1 > 0`（默认）| 逻辑表达式

连接到 **if** 端口的 If Action Subsystem 模块在关联的 `if` 表达式求值为 `true` 时执行。

`u1 > 0`
:   指定当输入 `u1` 大于 `0` 时在输出端口发送动作信号。

逻辑表达式
:   **注意**

    从 R2025a 开始，要编辑默认的 **if** 表达式（`u1 > 0`），请使用 **Expressions** 表。对于包含多个输入和运算符的复杂表达式，请选择 **if** 表达式并在 **Expression editor** 框中编辑。

    对于 R2025a 之前的版本，此参数在模块对话框中显示为 **If expressions**。您可以使用此参数指定逻辑表达式。

    但是，在所有 Simulink® 版本中，此表达式都显示在 If 模块上 **if** 输出端口旁边。

    表达式只能包含运算符 `<, <=, ==, ~=, >, >=, &, |, ~, ()` 和 `unary-minus`。不允许使用 `+, -, *, /` 和 `^` 等运算符。表达式不得包含数据类型表达式，例如 `int8(6)`，并且不得引用数据类型不是 `double` 或 `single` 的工作区变量。

#### 编程使用

|  |
| --- |
| **模块参数**：`IfExpression` |
| **类型**：character vector |
| **值**：`'u1 > 0'` | logical expression in quotes |
| **默认值**：`'u1 > 0'` |

### **elseif** — 逻辑表达式 空（默认）| 逻辑表达式列表

连接到 **elseif** 端口的 If Action Subsystem 模块在关联的 `elseif` 表达式求值为 `true` 且所有其他 `if` 和 `elseif` 表达式均为 false 时执行。

空
:   未指定逻辑表达式。

逻辑表达式列表
:   **注意**

    从 R2025a 开始，要添加和编辑 **elseif** 表达式，请使用 **Expressions** 表。使用表左侧的操作按钮来添加、删除和移动表达式。该表允许您分别编写每个 **elseif** 表达式，而不是在逗号分隔列表中编写，并根据您的建模需求组织表达式。对于包含多个输入和运算符的复杂表达式，请选择包含该 **elseif** 表达式的行，并在 **Expression editor** 框中编辑。

    对于 R2025a 之前的版本，此参数在模块对话框中显示为 **Else expressions**。在这些版本中，请指定以逗号分隔的逻辑表达式列表。

    但是，在所有 Simulink 版本中，当您选中 **Show else condition** 复选框时，这些表达式显示在 If 模块上 **if** 端口下方和 **else** 端口上方。

    表达式只能包含运算符 `<, <=, ==, ~=, >, >=, &, |, ~, ()` 和 `unary-minus`。不允许使用 `+, -, *, /` 和 `^` 等运算符。表达式不得包含数据类型表达式，例如 `int8(6)`，并且不得引用数据类型不是 `double` 或 `single` 的工作区变量。

#### 编程使用

|  |
| --- |
| **模块参数**：`ElseIfExpressions` |
| **类型**：character vector |
| **值**：`''` | list of logical expressions separated by commas placed in quotes |
| **默认值**：`''` |

## 所属库

Simulink / Ports & Subsystems

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2006a 之前推出**

### R2025a：模块对话框和代码生成的增强

- 更新后的模块对话框允许您在表中指定逻辑表达式。您不再需要在逗号分隔列表中指定 elseif 表达式。此更改使整体逻辑流程更易于可视化和解析。该表还包含新的操作按钮，允许您添加、删除和上下移动 if-else 表达式。这些按钮可帮助您根据建模需求组织表达式。此外，新的表达式编辑器框允许您编辑复杂表达式。
- 生成的代码包含 if-else 表达式。此更改可防止包含 switch-case 语句并增强生成代码的可读性。

## 描述

使用类似于 if-else 语句的逻辑选择子系统执行

If 模块与包含 Action Port 模块的 If Action Subsystem 模块一起，实现 if-else 逻辑以控制子系统执行。有关使用 If 模块的示例，请参阅 Select Subsystem Execution。

模型 ex\_if\_block
