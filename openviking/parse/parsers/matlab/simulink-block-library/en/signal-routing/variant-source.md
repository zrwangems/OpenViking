---
type: simulink-block
title: 'Variant Source'
family: signal-routing
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'variantsource'
language: en
---

# Variant Source

Route among multiple inputs using variants

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
