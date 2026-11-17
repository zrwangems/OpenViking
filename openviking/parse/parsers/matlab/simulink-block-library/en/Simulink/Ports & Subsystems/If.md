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
language: en
---

# If

## Ports
```yaml
ports:
- name: Logical operands
  summary: Values for evaluating logical expressions scalar | vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Action
  summary: Action signal for an If Action Subsystem block scalar
  direction: output
```

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
```yaml
parameters:
- name: Number of inputs
  summary: Specify number of input ports 1 (default) | integer
  group: ''
  block_parameter: NumInputs
  type: character vector
  values: '''1'' | integer in quotes'
  default: '''1'''
- name: Show else condition
  summary: Control display of else port on (default) | off
  group: ''
  block_parameter: ShowElse
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Enable zero-crossing detection
  summary: Control zero-crossing detection on (default) | off
  group: ''
  block_parameter: ZeroCross
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Provide if-else statements in generated code
  summary: Option to include only if-else statements in code generated from If block off (default) | on
  group: ''
  block_parameter: EnsureIfElseCode
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: if
  summary: Logical expression u1 > 0 (default) | logical expression
  group: ''
  block_parameter: IfExpression
  type: character vector
  values: '''u1 > 0'' | logical expression in quotes'
  default: '''u1 > 0'''
- name: elseif
  summary: Logical expression empty (default) | list of logical expressions
  group: ''
  block_parameter: ElseIfExpressions
  type: character vector
  values: ''''' | list of logical expressions separated by commas placed in quotes'
  default: ''''''
```

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
## Libraries

Simulink / Ports & Subsystems

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

## Description

Select subsystem execution using logic similar to if-else statement

The If block, along with If Action Subsystem blocks that contain
an Action Port block, implements if-else
logic to control subsystem execution. For an example that uses the If
block, see Select Subsystem Execution.

Model ex\_if\_block
