---
type: simulink-block
title: 'If'
family: ports-and-subsystems
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'if'
---

# If

Select subsystem execution using logic similar to if-else statement

## 中文

使用类似于 if-else 语句的逻辑选择子系统执行

### 所属库

Simulink / Ports & Subsystems

### 描述

If 模块以及包含 Action Port 模块的 If Action Subsystem 模块实现 if-else 逻辑来控制子系统的执行。有关使用 If 模块的示例，请参阅选择子系统执行。

Model ex\_if\_block

### 端口

#### 输入

#### **Logical operands** — 用于计算逻辑表达式的值 标量 | 向量

输入 `u1,u2,...,un` 必须具有相同的数据类型。输入不能是任何用户定义的类型，例如枚举类型。

If 模块不直接支持定点数据类型。但是，可以使用 Compare To Constant 模块解决此限制。请参阅 选择子系统执行中对定点数据类型的支持。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
#### 输出

#### **Action** — 用于 If Action Subsystem 模块的动作信号 标量

来自 `if`、`else` 和 `elseif` 端口的输出是到 If Action Subsystem 模块的动作信号。

### 参数

#### **输入数目** — 指定输入端口个数 `1` (默认) | 整数

`1`
:   指定一个输入端口。

整数
:   指定输入端口个数。模块端口的标签为 `'u'` 字符后跟数字 `1,2,...,n`，其中 `n` 等于您指定的输入数目。

##### 编程用法

|  |
| --- |
| **模块参数**：`NumInputs` |
| **类型**：字符向量 |
| **值**：`'1'` | 用引号引起来的整数 |
| **默认值**：`'1'` |

#### **显示 else 条件** — 控制 else 端口的显示 `on` (默认) | `off`

当 **if** 端口和所有 **elseif** 端口表达式为 `false` 时，**else** 端口发送动作信号来执行所连接的 If Action Subsystem 模块。

on
:   显示 **else** 端口。

off
:   隐藏 **else** 端口。

##### 编程用法

|  |
| --- |
| **模块参数**：`ShowElse` |
| **类型：**字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'on'` |

#### **启用过零检测** — 控制过零检测 `on` (默认) | `off`

控制过零检测。

on
:   检测过零点。

off
:   不检测过零点。

##### 编程用法

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型：**字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'on'` |

#### **在生成的代码中提供 if-else 语句** — 在从 If 模块生成的代码中仅包含 if-else 语句的选项 `off` (默认) | `on`

*自 R2025a 起*

选择此参数可确保从 If  模块生成的代码中仅包含 if-else 语句。

on
:   在生成的代码中仅包含 if-else 语句。此选项可防止在生成的代码中包含 switch-case 语句。

off
:   当此参数为 off 时，从 If 模块生成的代码可能包含 switch-case 语句（这些语句执行与 If 模块相同的操作）。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |
| --- |
| **模块参数**：`EnsureIfElseCode` |
| **类型：**字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'off'` |

#### **if** — 逻辑表达式 `u1 > 0` (默认) | 逻辑表达式

连接到 **if** 端口的 If Action Subsystem 模块在关联的 `if` 表达式的计算结果为 `true` 时执行。

`u1 > 0`
:   指定当输入 `u1` 大于 `0` 时在输出端口上发送动作信号。

逻辑表达式
:   **注意**

    从 R2025a 开始，要编辑默认 **if** 表达式 (`u1 > 0`)，请使用**表达式**表。对于包含多个输入和运算符的复杂表达式，请选择 **if** 表达式并在**表达式编辑器**框中编辑。

    对于 R2025a 之前的版本，此参数在模块对话框中显示为 **If 表达式**。您可以使用此参数指定逻辑表达式。

    不过，对于所有 Simulink® 版本，此表达式在 If 模块上与 **if** 输出端口相邻显示。

    该表达式只能包含运算符 `<, <=, ==, ~=, >, >=, &, |, ~, ()`  和 `unary-minus`。不允许使用 `+, -, *, /` 和 `^` 等运算符。该表达式不能包含数据类型表达式（例如 `int8(6)`），并且不能引用任何数据类型不是 `double` 或 `single` 的工作区变量。

##### 编程用法

|  |
| --- |
| **模块参数**：`IfExpression` |
| **类型**：字符向量 |
| **值**：`'u1 > 0'` | 用引号引起来的逻辑表达式 |
| **默认值**：`'u1 > 0'` |

#### **elseif** — 逻辑表达式 空 (默认) | 逻辑表达式列表

连接到 **elseif** 端口的 If Action Subsystem 模块在关联的 `elseif` 表达式计算结果为 `true` 且所有其他 `if` 和 `elseif` 表达式为 false 时执行。

空
:   未指定逻辑表达式。

逻辑表达式列表
:   **注意**

    从 R2025a 开始，要添加和编辑 **elseif** 表达式，请使用**表达式**表。使用表左侧的操作按钮添加、删除和移动表达式。该表允许您分别编写每个 **elseif** 表达式，而不是在以逗号分隔的列表中编写，并可根据建模需求组织表达式。对于包含多个输入和运算符的复杂表达式，请选择包含该 **elseif** 表达式的行并在**表达式编辑器**框中编辑它。

    对于 R2025a 之前的版本，此参数在模块对话框中显示为 **Else 表达式**。在这些版本中，指定以逗号分隔的逻辑表达式列表。

    不过，对于所有 Simulink 版本，当您选中**显示 else 条件**复选框时，表达式出现在 If 模块上的 **if** 端口下方及 **else** 端口上方。

    表达式只能包含运算符 `<, <=, ==, ~=, >, >=, &, |, ~, ()` 和 `unary-minus`。不允许使用 `+, -, *, /` 和 `^` 等运算符。表达式不能包含数据类型表达式（例如 `int8(6)`），并且不能引用任何数据类型不是 `double` 或 `single` 的工作区变量。

##### 编程用法

|  |
| --- |
| **模块参数**：`ElseIfExpressions` |
| **类型**：字符向量 |
| **值**：`''` | 用引号引起来的以逗号分隔的逻辑表达式列表 |
| **默认值**：`''` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `是` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

### 版本历史记录

**在 R2006a 之前推出**

#### R2025a: 模块对话框和代码生成的增强功能

- 更新后的模块对话框允许您在表中指定逻辑表达式。您不再需要以逗号分隔的列表形式指定 elseif 表达式。此更改使整体逻辑流更易于可视化和解析。该表还包含新的操作按钮，允许您添加、删除和上下移动 if-else 表达式。这些按钮帮助您根据建模需求组织表达式。此外，新表达式编辑器框允许您编辑复杂表达式。
- 生成的代码包含 if-else 表达式。此更改可防止包含 switch-case 语句并增强生成代码的可读性。

## Libraries

Simulink / Ports & Subsystems

## Description

The If block, along with If Action Subsystem blocks that contain
an Action Port block, implements if-else
logic to control subsystem execution. For an example that uses the If
block, see Select Subsystem Execution.

Model ex\_if\_block

## Ports

### Input

### **Logical operands** — Values for evaluating logical expressions scalar | vector

Inputs `u1,u2,...,un` must have the same data type. The inputs
cannot be of any user-defined type, such as an enumerated type.

The If block does not directly support fixed-point data types.
However, you can use the Compare To Constant block to work around this
limitation. See Support for Fixed-Point Data Type in Select Subsystem Execution.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Action** — Action signal for an If Action Subsystem block scalar

Outputs from the `if`, `else`, and
`elseif` ports are action signals to If Action
Subsystem blocks.

## Parameters

### **Number of inputs** — Specify number of input ports `1` (default) | integer

`1`
:   Specify one input port.

integer
:   Specify the number of input ports. Block ports are labeled
    with a `'u'` character followed by a number,
    `1,2,...,n`, where `n`
    equals the number of inputs that you specify.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumInputs` |
| **Type**: character vector |
| **Values**: `'1'` | integer in quotes |
| **Default**: `'1'` |

### **Show else condition** — Control display of else port `on` (default) | `off`

When the **if** port and all **elseif**
port expressions are `false`, the **else**
port sends an action signal to execute the attached If Action
Subsystem block.

on
:   Display **else** port.

off
:   Hide **else** port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ShowElse` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Enable zero-crossing detection** — Control zero-crossing detection `on` (default) | `off`

Control zero-crossing detection.

on
:   Detect zero crossings.

off
:   Do not detect zero crossings.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ZeroCross` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Provide if-else statements in generated code** — Option to include only if-else statements in code generated from If block `off` (default) | `on`

*Since R2025a*

Select this parameter to ensure only if-else statements are included in
the code generated from an If  block.

on
:   Only if-else statements are included in the generated
    code. This option prevents inclusion of switch-case
    statements in the generated code.

off
:   When this parameter is off, the code generated from an
    If block might contain switch-case
    statements, which perform the same operations as the
    If block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |
| --- |
| **Block Parameter:** `EnsureIfElseCode` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **if** — Logical expression `u1 > 0` (default) | logical expression

The If Action Subsystem block attached to the
**if** port executes when the associated `if`
expression evaluates to `true`.

`u1 > 0`
:   Specify sending an action signal on the output port when the
    input `u1` is greater than
    `0`.

logical expression
:   **Note**

    Starting in R2025a, to edit the default
    **if** expression (`u1 >
    0`), use the **Expressions**
    table. For a complex expression with multiple inputs and
    operators, select the **if**
    expression and edit it in the **Expression
    editor** box.

    For versions prior to R2025a, this parameter appears as
    **If expressions** in the block dialog box.
    You can specify logical expressions using this parameter.

    However, across all Simulink® versions, this expression appears on the
    If block adjacent to the
    **if** output port.

    The expression can include only the operators `<,
    <=, ==, ~=, >, >=, &, |, ~, ()` , and
    `unary-minus`. Operators such as
    `+, -, *, /`, and `^` are
    not allowed. The expression must not contain data type
    expressions, for example, `int8(6)`, and must
    not reference workspace variables whose data type is anything
    other than `double` or
    `single`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IfExpression` |
| **Type**: character vector |
| **Values**: `'u1 > 0'` | logical expression in quotes |
| **Default**: `'u1 > 0'` |

### **elseif** — Logical expression empty (default) | list of logical expressions

The If Action Subsystem block attached to an
**elseif** port executes when the associated
`elseif` expression evaluates to
`true` and all other `if` and
`elseif` expressions are false.

empty
:   Logical expressions not specified.

list of logical expressions
:   **Note**

    Starting in R2025a, to add and edit
    **elseif** expressions, use the
    **Expressions** table. Use the action
    buttons on the left of the table to add, delete, and move
    the expressions. The table allows you to write each
    **elseif** expression separately
    instead of in a comma-separated list and organize the
    expressions per your modeling requirements. For a complex
    expression with multiple inputs and operators, select the
    row containing that **elseif**
    expression and edit it in the **Expression
    editor** box.

    For versions prior to R2025a, this parameter appears as
    **Else expressions** in the block dialog
    box. In those versions, specify a list of logical expressions
    separated by commas.

    However, across all Simulink versions, the expressions appear on the
    If block below the **if**
    port and above the **else** port when you
    select the **Show else condition** check
    box.

    Expressions can include only the operators `<,
    <=, ==, ~=, >, >=, &, |, ~, ()`, and
    `unary-minus`. Operators such as
    `+, -, *, /`, and `^` are
    not allowed. The expressions must not contain data type
    expressions, for example, `int8(6)`, and must
    not reference workspace variables whose data type is anything
    other than `double` or
    `single`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ElseIfExpressions` |
| **Type**: character vector |
| **Values**: `''` | list of logical expressions separated by commas placed in quotes |
| **Default**: `''` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

## Version History

**Introduced before R2006a**

### R2025a: Enhancements to block dialog box and code generation

- The updated block dialog box allows you to specify the logical
  expressions in a table. You no longer need to specify the elseif
  expressions in a comma-separated list. This change makes the overall
  logic flow easier to visualize and parse. The table also contains new
  action buttons that allow you to add, delete, and move if-else
  expressions up and down. These buttons help you to organize the
  expressions per your modeling requirements. Additionally, the new
  expression editor box allows you to edit complex expressions.
- Generated code contains if-else expressions. This change prevents
  inclusion of switch-case statements and enhances readability of the
  generated code.
