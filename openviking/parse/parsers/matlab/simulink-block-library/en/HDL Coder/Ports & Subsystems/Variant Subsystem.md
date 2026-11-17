---
type: simulink-block
title: 'Variant Subsystem'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'variantsubsystem'
documentation_source_path: '../simulink/slref/variantsubsystem.html'
language: en
---

# Variant Subsystem

## Ports
```yaml
ports:
- name: In_1
  summary: Input port corresponding to root-level Inport blocks in variant subsystem same data types accepted by Inport blocks
  direction: input
- name: Out_1
  summary: Output port corresponding to root-level Outport blocks contained in variant subsystem same data types accepted
    by Outport blocks
  direction: output
```

### Input

### **In\_1** — Input port corresponding to root-level Inport blocks in variant subsystem same data types accepted by Inport blocks

Each Subsystem, Model, or Subsystem
Reference block contained within a Variant
Subsystem represents one variant choice. The variant choices can
contain Inport, control port (Enable, Trigger, Reset, and Function-Call Subsystem), or
Connection Port (Simscape) blocks at
its input. The variant choices can have input ports that differ in number
from the input ports in the parent Variant Subsystem block.
However, the conditions described in Map Input and Output Ports of Variant Choices in Variant Subsystem must be met.
### Output

### **Out\_1** — Output port corresponding to root-level Outport blocks contained in variant subsystem same data types accepted by Outport blocks

Each Subsystem, Model, or Subsystem
Reference block contained within a Variant
Subsystem represents one variant choice. The variant choices can
contain Outport or Connection Port (Simscape) blocks at
its output. The variant choices can have output ports that differ in number
from the output ports in the parent Variant Subsystem block.
However, the conditions described in Map Input and Output Ports of Variant Choices in Variant Subsystem must be met.

The unconnected output ports (inactive output ports) of a Variant
Subsystem block output a ground value. To output a value other
than ground, select the **Specify output when source is
unconnected** parameter of the Outport block and
specify a value.
## Parameters
```yaml
parameters:
- name: Variant control mode
  summary: Variant control mode expression (default) | label | sim codegen switching
  group: ''
  block_parameter: VariantControlMode
  type: character vector
  values: '''expression'' | ''label'' | ''sim codegen switching'''
  default: '''expression'''
- name: Variant activation time
  summary: Time when software chooses active variant choice update diagram (default) | update diagram analyze all choices
    | code compile | startup | runtime | inherit from Simulink.VariantControl
  group: ''
  block_parameter: VariantActivationTime
  type: character vector
  values: '''update diagram'' | ''update diagram analyze all choices'' | ''code compile'' | ''startup''| ''runtime'''
  default: '''update diagram'''
- name: Variant control variable
  summary: Variable to determine active variant choices Simulink.VariantControl object | scalar variable | Simulink.Parameter
    object | struct
  group: ''
  block_parameter: VariantControlVariable
  type: character vector
  values: Simulink.VariantControl object, scalar variable, Simulink.Parameter object, struct
  default: ''''''
- name: Variant choices enumeration
  summary: Enumeration class to add variant choices enumeration class with model or subsystem filenames as its members
  group: ''
  block_parameter: VariantChoicesEnumeration
  type: character vector
  values: enumeration class defined using classdef or Simulink.defineIntEnumType
  default: ''''''
- name: Variant choices specifier
  summary: MATLAB expression to add variant choices any MATLAB expression that evaluates to a one-dimensional cell array of
    model or subsystem filenames, or filename patterns that match the model or subsystem filenames or an array of strings
  group: ''
  block_parameter: VariantChoicesSpecifier
  type: character vector
  values: Any MATLAB expression that evaluates to a one-dimensional cell array of filenames or filename patterns.
  default: ''''''
- name: Variant choices
  summary: Table of variant choices, variant controls, and conditions empty table (default)
  group: ''
- name: Name (read-only)
  summary: 'Variant choice name Read-only: Subsystem and Subsystem1 (default) | name of choices contained in Variant Subsystem'
  group: ''
- name: Variant control label
  summary: Name of choice in label mode true or false (default) | string
  group: ''
  block_parameter: VariantControl
  values: variant control that is associated with the variant choice
- name: Variant control switch
  summary: Variant choices for simulation and code generation workflows (sim) | (codegen)
  group: ''
  block_parameter: VariantControl
  values: variant control that is associated with the variant choice
- name: Variant control expression
  summary: Condition expression that determines the active choice true or false (default) | boolean condition expression |
    a Simulink.VariantExpression object representing a boolean condition expression | (default)
  group: ''
  block_parameter: VariantControls
  values: variant controls that are associated with variant choices
- name: Condition (read-only)
  summary: 'Condition expression in Simulink.VariantExpression object Read-only: N/A (default)'
  group: ''
- name: Label mode active choice
  summary: Name of active choice in label mode true (Subsystem) (default) | false (Subsystem1)
  group: ''
  block_parameter: LabelModeActiveChoice
  type: character vector
  values: If no label mode active choice is specified, the value is empty. If a label mode active choice is specified, the
    value is the variant control label for the active choice.
  default: ''''''
- name: Built-in empty choice
  summary: Output zero if no variant choice is active off (default) | on
  group: ''
  block_parameter: EmptyChoice
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Built-in passthrough choice
  summary: Assign input port values to output ports if no variant choice is active off (default) | on
  group: ''
  block_parameter: PassThrough
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Propagate conditions outside of variant subsystem
  summary: Option to choose if components outside of the variant subsystem must be informed of the active and inactive state
    of underlying blocks off (default) | on
  group: ''
  block_parameter: PropagateVariantConditions
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Allow flexible interface
  summary: Option to choose to make interface of the variant subsystem flexible on (default) | off
  group: ''
  block_parameter: AllowFlexibleInterface
  type: character vector
  values: '''off'' | ''on'''
  default: '''on'''
```

To access these parameters, right-click the variant badge on the block icon and select
**Block Parameters**. For more information, see Variant Badges.

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

| **Variant activation time** | | | | |  |
| --- | --- | --- | --- | --- | --- |
| **Variant control mode** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` | `runtime` (Variant Subsystem block only) |
| `expression` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `label` | ✓ | x | x | x | x |
| `sim codegen switching` | ✓ | ✓ | x | x | x |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantControlMode` |
| **Type:** character vector |
| **Values:** `'expression'` | `'label'` | `'sim codegen switching'` |
| **Default:** `'expression'` |

### **Variant activation time** — Time when software chooses active variant choice `update diagram` (default) | `update diagram analyze all choices` | `code compile` | `startup` | `runtime` | `inherit from Simulink.VariantControl`

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
- `runtime` — When you execute the model, the active
  variant can switch during simulation or execution of the generated code by using
  the Parameter
  Writer block. Place a Parameter Writer block inside a
  conditionally executed subsystem or in an Initialize Function block, a
  Reinitialize Function block, or a Reset Function block. For more
  information on the blocks, see Event Functions.
  You can use the Parameter Writer block to write to block
  parameters, model workspace variables, and base workspace variables. Multiple
  variant control variables are not supported for
  `runtime` activation time. All modeling patterns
  supported by the Parameter Writer block are valid for run-time
  activation. For more information, see Common Uses of Parameter Writer Block.

  When you set the **Variant activation time** parameter of the
  Variant Subsystem block to
  `runtime`, the color of the inactive variant choices
  does not fade. In this case, the setting of the **Variant
  Fading** option in the **Information Overlays**
  menu on the **Debug** tab of the Simulink Editor is
  ignored.
- `inherit from Simulink.VariantControl` — When you
  execute the model, the block inherits the activation time from its variant
  control variables of type `Simulink.VariantControl`. If a variant block has multiple variant
  control variables of type `Simulink.VariantControl`, then all those
  variables must have the same activation time.

The table compares the different variant activation times based on conditional code,
variant switching, handling of states, and fast restart support.

|  | `update diagram` or `update diagram analyze all choices` | `code compile` | `startup` | `runtime` |
| --- | --- | --- | --- | --- |
| **Generated conditional code** | Inactive conditional code is not available. | Conditional code is present inside preprocessor macros. The inactive choice code is eliminated when generated code is compiled. | Conditional code is generated as part of an `if-elseif-else` statement. The variant control variable value cannot be modified during execution. | Conditional code is generated as part of an `if-elseif-else` statement. The variant control variable value can be modified during execution. |
| **Variant switching during simulation or code execution** | Not supported. | Not supported. | Supported at startup (before simulation start at *t* = 0). | Supported. The active variants are switched by changing the variant control variable using the Parameter Writer block. |
| **Explicit setting of held or reset option for states** | Not supported. States are reset for inactive blocks. | Not supported. States are reset for inactive blocks | States cannot be changed during simulation. In the generated code, if you attempt to change the variant, states are in held state. | States are held by default. Reset states explicitly through State Writer blocks. Read blocks with states by using the State Reader block and transfer to another choice by using the State Writer block. |
| **Executable size** | Smaller size. Code is not generated for the inactive variant. | Smaller size. The inactive variant code is removed during compilation. | Comparatively larger size. Both active and inactive variant code is available for startup switching. | Comparatively larger size. Both active and inactive variant code is available for run-time switching. |
| **Fast restart support** | Not supported. | Not supported. | Supported. | Supported. |

#### Dependencies

- The availability of different variant activation times depends on the type
  of the variant control mode that you specify. The **Variant
  activation time** parameter determines when the software sets
  the active choice. The parameter also determines which variability to
  include in the generated code. This table explains the variant activation
  time supported by each variant control mode.

  | **Variant activation time** | | | | |  |
  | --- | --- | --- | --- | --- | --- |
  | **Variant control mode** | `update diagram` | `update diagram analyze all choices` | `code compile` | `startup` | `runtime` |
  | `expression` | ✓ | ✓ | ✓ | ✓ | ✓ |
  | `label` | ✓ | x | x | x | x |
  | `sim codegen switching` | ✓ | ✓ | x | x | x |
- To enable switching of active variant choice of the Variant
  Subsystem block using the `runtime` activation
  time, you must use the Parameter Writer block. Set the
  **Destination** parameter of the Parameter
  Writer block based on the location of your variant control
  variable and select **Validate parameter** :

  - `Block parameter` — Control variable
    is a mask parameter in a subsystem.
  - `Model workspace variable` — Control
    variable is located in the model workspace.
  - `Base workspace variable` — Control
    variable is located in the base workspace or a data
    dictionary.

  For example, you can create a mask parameter
  `V` in a subsystem and use it in a variant condition
  expression for a variant control. The Parameter Writer block
  writes to the value of `V` in the variant control
  condition.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantActivationTime` |
| **Type:** character vector |
| **Values:** `'update diagram'` | `'update diagram analyze all choices'` | `'code compile'` | `'startup'`| `'runtime'` |
| **Default:** `'update diagram'` |

### **Variant control variable** — Variable to determine active variant choices `Simulink.VariantControl` object | scalar variable | `Simulink.Parameter` object | `struct`

When you specify a variable of type listed in Types of Variant Control Variables (Operands) in Variant Blocks, the
software generates variant control expressions for the variant choices of the
Variant Assembly Subsystem block. The **Variant
control variable** that you specify here is on the left side and
the members of the **Variant enumeration choice** are on the
right side of the generated expressions. Both the sides are related by
`==`.

The variant control variable acts as a switch to change the active variant
choice. You specify a value for a variant control variable and run the
simulation. During simulation, the software evaluates the variant control
expressions to determine the active variant choice. When an expression evaluates
to `true`, the corresponding variant choice is set active. To
change the active variant, change the value of the variant control variable such
that the corresponding variant control expression evaluates to
`true` turns active.

#### Dependencies

This parameter is available only in Variant Assembly
Subsystem block. To enable this parameter, set **Variant
control mode** to `expression`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantControlVariable` |
| **Type:** character vector |
| **Values:** `Simulink.VariantControl` object, scalar variable, `Simulink.Parameter` object, `struct` |
| **Default:** `''` |

### **Variant choices enumeration** — Enumeration class to add variant choices enumeration class with model or subsystem filenames as its members

To add Model or Subsystem Reference blocks as
variant choices to a Variant Assembly Subsystem block, specify an
enumeration class name that contains the corresponding model or subsystem
filenames as its members. You can then validate the enumeration class using the
Refresh button in the **Variant choices** table. On a
successful validation, the members of the enumeration class are added as variant
choices to the Variant Assembly Subsystem block. Each choice has
a variant control expression with **Variant control
variable** on its left side and the members of the
**Variant choices enumeration** that you specify here on
its right side. Both the sides of the expression are related by
`==`. The newly added variant choices and their
corresponding control expressions are displayed in the **Variant
choices** table.

To remove variant choices from a Variant Assembly Subsystem
block, remove the corresponding members from the enumeration class that you
specify here. You cannot manage the variant choices from inside the
Variant Assembly Subsystem block.

The enumeration class that you specify must be on the search path of your
current MATLAB® session. For information on how to add files or folders to the
search path, see `addpath`.

For more information on how to add choices using the **Variant choices
enumeration** parameter, see Add or Remove Variant Choices of Variant Assembly Subsystem Blocks Using External Files.

#### Dependencies

This parameter is available only in Variant Assembly
Subsystem block. To enable this parameter, set **Variant
control mode** to `expression`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantChoicesEnumeration` |
| **Type:** character vector |
| **Values:** enumeration class defined using `classdef` or `Simulink.defineIntEnumType` |
| **Default:** `''` |

### **Variant choices specifier** — MATLAB expression to add variant choices any MATLAB expression that evaluates to a one-dimensional cell array of model or subsystem filenames, or filename patterns that match the model or subsystem filenames or an array of strings

To add Model or Subsystem Reference blocks as
variant choices to a Variant Assembly Subsystem block, specify
the corresponding model or subsystem filenames. The filenames must be specified
as a MATLAB expression that returns a one-dimensional cell array of character
vectors when evaluated or an array of strings. You can then validate the
expression using the Refresh button in the **Variant choices**
table. On a successful validation, the blocks that correspond to the specified
files are added as variant choices to the Variant Assembly
Subsystem block. For each choice, a variant control label is
generated. The name of the variant control label is same as the name of the
choice. The newly added variant choices and their corresponding control labels
are displayed in the **Variant choices** table.

To remove variant choices from a Variant Assembly Subsystem
block, modify the expression specified in this parameter. You cannot manage the
variant choices of a Variant Assembly Subsystem block from inside
the block.

The MATLAB expression that you specify must contain either of these:

- Model or subsystem filenames that are on the search path of your
  current MATLAB session. For example, if you specify
  `{'model1.slx', 'subsystemRef1.slx'}` as a
  specifier, the blocks that correspond to the
  `model1.slx` and
  `subsystemRef1.slx` files are added as variant
  choices of the Variant Assembly Subsystem
  block.
- File name patterns that match the model or subsystem filenames on
  the MATLAB path. The paths in the pattern can be absolute or
  relative to the parent folder of the model that contains the
  Variant Assembly Subsystem block. For example, if
  you specify `{'folder_1/*.slx', 'folder_2/*.slx'}`
  as a specifier, the software passes the character vectors
  `folder_1/*` and `folder2/*`
  to the `dir` function. The
  function then returns the model and the subsystem files that are
  located inside the `folder1` and
  `folder2` folders. The blocks that correspond
  to the returned files are added as variant choices of the
  Variant Assembly Subsystem block.

For information on how to add files or folders to the search
path, see `addpath`.

For more information on how to specify choices in the **Variant choices
specifier** parameter, see Add or Remove Variant Choices of Variant Assembly Subsystem Blocks Using External Files.

#### Dependencies

This parameter is available only in Variant Assembly
Subsystem block. To enable this parameter, set **Variant
control mode** to `label`.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `VariantChoicesSpecifier` |
| **Type:** character vector |
| **Value:** Any MATLAB expression that evaluates to a one-dimensional cell array of filenames or filename patterns. |
| **Default:** `''` |

### **Variant choices** — Table of variant choices, variant controls, and conditions empty table (default)

The table has a row for each variant choice contained in the variant
subsystem. If there are no variant choices, the table is empty.

You can use buttons to the left of the **Variant choices**
table to modify the elements in the table.

| To... | Click... |
| --- | --- |
| **Create and add a new subsystem choice**: Create a new Subsystem block as a variant choice and add an entry for the new choice in the table. | the Create and add a new subsystem choice button |
| **Create and add a new model variant choice**: Create a new Model block as a variant choice and add an entry for the new choice in the table. | the Create and add a new model variant choice button |
| **Delete selected variant choices**: Delete variant choices permanently. | the Delete selected variant choices button |
| **Create/Edit selected variant object**: Create or edit a `Simulink.VariantExpression` object in the global workspace and specify the variant condition using the `Simulink.VariantExpression` object parameter dialog box.  **Note**  For a model that uses the base workspace, this operation creates the `Simulink.VariantExpression` object in the base workspace and the object is available only for the current MATLAB session. To permanently store the data, save the object in a MAT file or MATLAB script. | the Create or Edit selected variant object button |
| **Open selected variant choice block**: Open the Subsystem block for the selected row. | the Open selected variant choice block button |
| **Refresh dialog information from Variant Subsystem contents**: Update the **Variant choices** table according to the variant choices and values of the variant control in the global workspace. | the Refresh dialog information from Variant Subsystem contents button |

#### Dependencies

The Variant Assembly Subsystem block allows you to only
open the selected variant choice and refresh the list of variant choices
using the buttons in this section. To add new variant choices to the
Variant Assembly Subsystem block, see Add or Remove Variant Choices of Variant Assembly Subsystem Blocks Using External Files.

### **Name (read-only)** — Variant choice name Read-only: `Subsystem` and `Subsystem1` (default) | name of choices contained in Variant Subsystem

This parameter is read-only.

This parameter displays the
name of the choices. Each choice has a variant control in the form of labels,
expressions, or switches. For Variant Assembly Subsystem in the
`label` mode, no separate variant control is
available. The name of the choice is used as a variant control to set the active
choice.

### **Variant control label** — Name of choice in `label` mode `true` or `false` (default) | string

A name for a choice, specified as a string.

#### Dependencies

To enable this parameter, set **Variant control mode** to
`label`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `VariantControl` |
| **Values:** | variant control that is associated with the variant choice |
| **Data Types:** | `char` |

**Example:** `set_param(gcb, 'VariantControl', 'V == 3')`,
where `gcb` is the variant choice of the Variant
Subsystem block.

**Example:** `get_param(gcb, 'VariantControl')`, where
`gcb` is the variant choice of the Variant
Subsystem block.

### **Variant control switch** — Variant choices for simulation and code generation workflows `(sim)` | `(codegen)`

Specify `(sim)` to activate the corresponding variant choice
during simulation. Specify `(codegen)` to activate the
corresponding variant choice while performing code generation workflows such as
SIL, PIL, external mode, and so on.

#### Dependencies

To enable this parameter, set **Variant control mode** to
`sim codegen switching`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `VariantControl` |
| **Values:** | variant control that is associated with the variant choice |
| **Data Types:** | `char` |

**Example:** `set_param(gcb, 'VariantControl', '(sim)')`,
where `gcb` is the variant choice of the Variant
Subsystem block.

**Example:** `get_param(gcb, 'VariantControl')`, where
`gcb` is the variant choice of the Variant
Subsystem block.

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

### **Built-in empty choice** — Output zero if no variant choice is active `off` (default) | `on`

- `off` — Simulink generates an error when there is no active variant
  choice.
- `on` — When you select this option, Simulink adds a nonmodifiable variant choice entry to the
  **Variant choices** table with its variant control
  set to `(default)`. This entry does not appear as a
  visible variant choice in the Variant Subsystem block.
  During simulation, if there is no active variant choice, Simulink disconnects the variant choices of the Variant
  Subsystem block, thus removing the variant regions
  completely from the model. The inactive outports of the subsystem output
  zero. To output a value other than zero, select the **Specify
  output when source is unconnected** parameter of the
  Outport block and specify a value of your
  choice.

For more information, see Manage Variant Components to Pass Specified Values from Inactive Variant Subsystems with No Active Choice (Simulink Coder).

#### Dependencies

This parameter is available only if there are no
`default` variant choices in the Variant
Subsystem and if you set **Variant control
mode** to `expression`.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `EmptyChoice` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Built-in passthrough choice** — Assign input port values to output ports if no variant choice is active `off` (default) | `on`

- `off` — Simulink generates an error when there is no active variant
  choice.
- `on` — When you select this option, Simulink adds a nonmodifiable variant choice entry to the
  **Variant choices** table with its variant control
  set to `(default)`. This entry does not appear as a
  visible variant choice in the Variant Subsystem block.
  During simulation, if there is no active variant choice, Simulink bypasses the variant choices of the Variant
  Subsystem block. Only the input and output ports remain
  active, and the input port pass values directly to the output
  ports.

  For values to be mapped from input ports to output ports when no
  choice is active, the Variant Subsystem block must
  have:

  - Only data ports, with no other types of input and output
    ports
  - An equal number of data input and output ports
  - Input and output ports that exactly match the ports of variant
    choices

For more information, see Manage Variant Components to Pass Specified Values from Inactive Variant Subsystems with No Active Choice (Simulink Coder).

#### Dependencies

This parameter is available only if there are no
`default` variant choices in the Variant
Subsystem and if you set **Variant control
mode** to `expression`.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `PassThrough` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Propagate conditions outside of variant subsystem** — Option to choose if components outside of the variant subsystem must be informed of the active and inactive state of underlying blocks `off` (default) | `on`

When you select the **Propagate conditions outside of variant
subsystem** parameter, the software propagates the variant
condition of the underlying blocks to the Variant Subsystem
container block so the subsystem can adapt its interface to the state of the
underlying blocks. Ports that are mapped to the ports on the active choice
becomes active. Ports that are not mapped to the ports on the inactive choice
becomes inactive. Selecting this option ensures that the components outside of
the Variant Subsystem are aware of the active and inactive state
of blocks within the Variant Subsystem block. For more
information, see Propagate Variant Conditions to Define Variant Regions Outside Variant Subsystems to Promote Consistency and Reduce Errors and Propagate Variant Conditions to Control Execution of Conditional Subsystems

Variant conditions do not propagate outside a Variant Subsystem
block if all variant choices within the block have the same interface.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `PropagateVariantConditions` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Allow flexible interface** — Option to choose to make interface of the variant subsystem flexible `on` (default) | `off`

Specify whether to make the interface of a variant subsystem flexible.

- `on` — Simulate with variant choices that have
  input and output ports that differ in number from the input and
  output ports of the Variant Subsystem block.
- `off` — When you simulate with this option, if
  there is inconsistency in the interface, the software will generate
  errors with fix-it actions to match the ports of the variant choices
  to the Variant Subsystem block.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `AllowFlexibleInterface` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'on'` |
## Libraries

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `yesa` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual data type or capability support depends on block implementation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic. Actual data type or capability support depends
on block implementation.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `Module` (default) | Generate code for the subsystem and the blocks within the subsystem. HDL Coder generates code for all the variant choices. |
| `BlackBox` | Generate a black-box interface. That is, the generated HDL code includes only the input/output port definitions for the subsystem. In this way, you can use a subsystem in your model to generate an interface to existing manually written HDL code.  The black-box interface generated for subsystems is similar to the interface generated for Model blocks, but without generation of clock signals. |
| `No HDL` | Remove the subsystem from the generated code. You can use the subsystem in simulation but treat it as a “no-op” in the HDL code. |

**Black Box Interface Customization**

For the `BlackBox` architecture, you
can customize port names and set attributes of the external component
interface. See Customize Black Box or HDL Cosimulation Interface (HDL Coder).

**HDL Block Properties**

| General | |
| --- | --- |
| **AdaptivePipelining** | Automatic pipeline insertion based on the synthesis tool, target frequency, and multiplier word-lengths. The default is `inherit`. See also AdaptivePipelining (HDL Coder). |
| **BalanceDelays** | Detects introduction of new delays along one path and inserts matching delays on the other paths. The default is `inherit`. See also BalanceDelays (HDL Coder). |
| **ClockRatePipelining** | Insert pipeline registers at a faster clock rate instead of the slower data rate. The default is `inherit`. See also ClockRatePipelining (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **DistributedPipelining** | Pipeline register distribution, or register retiming. The default is `inherit`. See also DistributedPipelining (HDL Coder). |
| **DSPStyle** | Synthesis attributes for multiplier mapping. The default is `none`. See also DSPStyle (HDL Coder). |
| **FlattenHierarchy** | Remove subsystem hierarchy from generated HDL code. The default is `inherit`. See also FlattenHierarchy (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |
| **StreamingFactor** | Number of parallel data paths, or vectors, that are time multiplexed to transform into serial, scalar data paths. The default is 0, which implements fully parallel data paths. See also Streaming (HDL Coder). |

**Target Specification**

This block cannot be the DUT, so the block property settings in the **Target
Specification** tab are ignored.

**Restrictions**

- The Variant Subsystem cannot be a design-under-test
  (DUT).
- **Variant activation time** parameter must be set to
  `update diagram`, `update
  diagram analyze all choices`, or
  `startup`.
- For the Outport block of the Variant Subsystem,
  **Specify output when source is unconnected**
  parameter must be disabled.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type or capability support depends on block implementation.

## Version History

**Introduced in R2010b**

### R2025a: Reduce overhead and irrelevant diagnostic messages by suppressing callbacks for inactive variant choices and commented blocks

The callbacks `LoadFcn`, `ContinueFcn`,
`InitFcn`, `ModelCloseFcn`,
`PauseFcn`, `PostSaveFcn`,
`PreSaveFcn`, `StartFcn`, and
`StopFcn` do not execute for inactive variant choices in Variant Subsystem blocks with the
`update diagram` activation time and for commented
blocks. This suppression reduces computational overhead and prevents unnecessary
diagnostic messages from the blocks that do not affect the current model iteration.
However, these callbacks are not suppressed for blocks within models or subsystem
files inside a commented or an inactive Model block or Subsystem Reference block. Also, the mask initialization and mask
parameter callbacks are not suppressed. For the list of applicable callbacks, see
Author Mask Initialization and Callbacks and Mask Parameters.

### R2025a: Parameter to output zero when no variant choices exist renamed from **Allow zero active variant controls**

The **Allow zero active variant controls** parameter is now
renamed to **Built-in empty choice**. This new parameter maintains
the previous functionality to remove the variant components and output zero when no
variant choice is active.

### R2025a: Assign input values to output ports when no variant choices exist

Use the **Built-in passthrough choice** parameter to bypass
variant region and assign input values to the output ports when no variant choice is
active.

### R2024b: `runtime` activation time : Change the active choice during simulation or code generation

Starting in R2024b, use the `runtime` variant activation time in
a Variant Subsystem block to change the active variant during
simulation or code generation by using the Parameter Writer block.
You can model all scenarios where the Parameter Writer block can
write to the variant control variable in the global workspace, mask workspace, or
model workspace.

### R2024a: Automated port synchronization

Simulink provides options to add missing ports and delete unused ports in
Variant Subsystem and Variant Assembly Subsystem
blocks to match the ports of the underlying variant choices. During simulation, if
Simulink encounters a port mismatch between a Variant Subsystem
or Variant Assembly Subsystem block and its variant choices, the
resulting error message provides the option of adding missing ports and deleting
unused ports to resolve the issue.

### R2024a: Use adapted rate-based model blocks as choices

You can use adapted rate-based model blocks as variant choices in a Variant
Subsystem block. When you add adapted rate-based models as variant
choices, the inports in the variant subsystem are matched to the port names of the
respective rate-based models.

### R2024a: Access the mask of the active variant choice

You can access the mask of the active variant choice of the Variant
Subsystem directly without having to navigate inside the Variant
Subsystem block.

- If the Variant Subsystem block is unmasked,
  double-clicking on the block opens the mask of its active choice.
  Clicking on the **Look under mask** badge or selecting
  the corresponding option from the context menu of the Variant
  Subsystem block takes you directly inside the active
  choice.
- If the Variant Subsystem block is masked and the active
  choice also has a mask, then double-clicking on the block opens the
  Variant Subsystem mask.
- If the Variant Subsystem block is unmasked and its
  active choice is masked, then double-clicking on the **Look
  under mask** badge takes you to the variant layer. You can
  see similar behavior in a masked Variant Subsystem block
  with an unmasked active choice.

When you click on the **Look under mask** badge of a linked
Variant Subsystem block with its active choice as a linked and
masked Model Reference block, the Model Reference
opens in a separate editor. Additionally, you must perform
`set_param` operations on the mask parameters of the active
choice block on the active choice, and not on the Variant Subsystem
block.

Promotion of the mask of the active choice is limited to its immediate parent.
Nested Variant Subsystem mask promotion is not supported.

### R2024a: Specify variant choices as an array of strings

You can specify **Variant choices specifier** as an
array of strings in Variant Assembly Subsystem block.

### R2023b: Promote content preview of active choice

Simulink promotes the content preview of the active choice of the
Variant Subsystem block automatically. When the active choice is
a Model Reference that is not loaded, and when the active choice is a
Stateflow chart, the Variant Subsystem is shown as the content
preview.

### R2023b: Navigate directly into active choice

You can navigate directly inside the active variant by double clicking on the
Variant Subsystem block. When you select **Open in New
Tab** or **Open in New Window** from the context menu,
the active choice is opened in a new tab or a new window. You can also use the
`open_system` function to access the variant layer and the
active choice.

```
open_system(vssBlock)
open_system(vssBlock,'ActiveChoice','window')
```

When the active choice
has an `OpenFcn` callback, double-clicking on the Variant
Subsystem block does not execute that callback. Additionally,
double-clicking on the Variant Subsystem does not navigate into the
active choice if the active choice is a referenced model that is not loaded.

### R2021a: Promote mask icon of active variant automatically

Simulink automatically displays the mask icon of the active variant block on
the parent Variant Subsystem. Prior to R2021a, you had to provide
icon drawing commands on the mask of the Variant Subsystem to display
the mask icon of the underlying active variant block.

## Description

Template subsystem containing Subsystem blocks as variant choices

The Variant Subsystem block enables you to include multiple
implementations of a component in a separate hierarchy.

For example, suppose you want to simulate a model that represents a vehicle with three
possible engine configurations: 2-cylinder gas, 4-cylinder gas, and 8-cylinder gas. You
could implement each engine model as a separate subsystem inside the Variant
Subsystem block and then switch between the subsystems based on the Types of Variant Control Modes in Variant Blocks you select. For
more information, see Introduction to Variant Controls.

**Note**

Only one implementation of a Variant Subsystem block is active
during simulation.

Multiple models of an engine inside a Variant Subsystem block

The Variant Subsystem block is a template preconfigured to contain two
or more blocks to use as variant choices. These choices represent multiple
implementations of a system. Only one child block is active during model execution. The
active child block is referred to as the *active variant*.

Each variant choice inside the Variant Subsystem block is associated
with a **Variant
control mode** and a **Variant
activation time**. The variant control mode determines how to select the
active variant. The variant activation time determines a time to activate the choices
and to decide whether to include only the active choice or both active and inactive
choices in the generated code.

A Variant Subsystem block can contain a mixture of Subsystem blocks, Model blocks, or Subsystem
Reference blocks as variant choices. A Variant Subsystem
block with only Model blocks as choices is called a Variant
Model block. For more information, see Implement Variations in Separate Hierarchy Using Variant Subsystems. A Variant Subsystem block with Model or
Subsystem Reference blocks as choices that can be added or removed
only from external files and not within the block is called a Variant Assembly
Subsystem block.

Apart from the variant choices, you can include Inport, control port (Enable, Trigger, Reset, and Function-Call Subsystem), Outport, or Connection Port (Simscape) blocks inside a
Variant Subsystem block. There are no drawn connections between the
blocks that are inside the Variant Subsystem blocks. The software
automatically wires the active variant to the Inport and
Outport blocks of the Variant Subsystem during model
compilation. The blocks representing variant choices can have input and output ports
that differ in number from the input and output ports in the parent Variant
Subsystem block. For more information, see Map Input and Output Ports of Variant Choices in Variant Subsystem.

When you load a model with a Variant Subsystem block that has variant
choices stored in subsystem files, by default, only the active choice is loaded to
optimize the loading time for models. However, if you initialize a model
programmatically using the `find_system`,
`get_param`, or `set_param` function, inactive
choices might get loaded.

Using Variant Subsystem block allows you to:

- Mix Subsystem, Model, and Subsystem
  Reference blocks as variant choices.
- Model components that do not have similar interface. You can have
  different numbers of inports and outports for multiple variant choices
  inside a Variant Subsystem. However, the conditions listed in
  Map Input and Output Ports of Variant Choices in Variant Subsystem must be met.
- Establish a hierarchical block diagram, where the Variant
  Subsystem block is on one layer and the variant choices are on
  another layer.
- Keeps functionally related blocks together.
- Reduce the complexity of your model.
- During model compilation, the software eliminates inactive blocks
  throughout the model, depending on the variant activation time you
  select.

The color and icon of the variant badge on the block icon changes depending on the
values of the **Variant activation time**, **Variant control
mode**, and **Propagate conditions outside of variant
subsystem** parameters set on the block. For more information, see Variant Badges.

### Open the Block

You can open the Variant Subsystem block from the Simulink® interface or programmatically. These methods enable you to access the
active variant choice or the entire variant layer of the Variant
Subsystem block, depending on your requirements.

**Open from Simulink Interface**

Use any of these actions in the Simulink interface to open the Variant Subsystem
block.

| Keyboard and mouse action | Result |
| --- | --- |
| Double-click | Opens the active variant choice inside the block in a new tab  **Note**  If the variant choice is a Model block and the model it references is not loaded, then double-clicking the block opens the variant layer containing the variant choices instead of opening the underlying layer of the active variant choice. |
| Hold **Ctrl** and double-click | Opens the block in a new tab, shows the variant layer |
| Hold **Shift** and double-click | Opens the block in a new window, shows the variant layer |
| Right-click, select **Open** > **Open in New Tab** | Opens the block in the current window, shows the variant layer |
| Right-click, select **Open** > **Open in New Window** | Opens the block in a new window, shows the variant layer |
| Right-click the variant badge, select **Open** >**(active variant)** | Opens the active variant choice in a new tab |
| Right-click the variant badge, select **Open** > **variant control (variant choice name)**, where *`variant control`* is the variant control `expression`, `label`, or `(sim)` or `(codegen)` for the variant choice specified by the *variant choice name.* | Opens the selected variant choice in a new tab |

**Open Programmatically**

Use either of these commands to open the Variant Subsystem
block, where *`variantSubsystemBlockName`* is the name of
the block:

- `open_system("variantSubsystemBlockName")`
  command — Open the Variant Subsystem block and view its
  variant layers.
- `open_system("variantSubsystemBlockName","ActiveChoice")`
  — Open the active variant choice within the Variant
  Subsystem block.

For information on additional options to open the Variant
Subsystem block using the `open_system` command,
such as opening in a new tab or window, see `open_system`.
