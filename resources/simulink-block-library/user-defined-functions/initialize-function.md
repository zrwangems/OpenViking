---
type: simulink-block
title: 'Initialize Function'
family: user-defined-functions
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'initializefunction'
---

# Initialize Function

Execute subsystem on model initialize event

## Libraries

Simulink / User-Defined Functions

## Description

The Initialize Function block is a preconfigured Subsystem block that executes on a model initialize event. By default, the
Initialize Function block includes:

- An Event Listener block with
  the **Event type** set to
  `Initialize`
- A Constant block with the **Constant
  value** set to `0`
- A State Writer block with no
  **State owner block** set

initialize function block contents

Use this block when you need to initialize a task based on an event. For example,
Initialize Function block inside a Simulink model referenced by a
Model  block is triggered when the Model block
receives a function-call control signal at its **initialize** port. For more
information about the modeling patterns using Initialize Function block,
see Common Uses of the Initialize Function Block. This block
allows you to schedule and control the initialization of a task in a model.

Customize the contents of the Initialize Function block by, for
example, replacing the Constant block with source blocks that generate
the state value for the State Writer block and specifying a
**State owner block** for the State Writer
block.

Conditionally executed subsystems with output ports are fully supported within
Initialize Function blocks. For a list of unsupported blocks and
features, see Initialize, Reinitialize, Reset, and Terminate Function Limitations.

The input and output ports of a component containing Initialize
Function and Terminate Function blocks must connect to
Inport and Outport blocks, respectively.

The code generated from this block is part of the `model_initialize`
function that is called once at the beginning of model execution.

You can select an Initialize Function, Reinitialize
Function, Reset Function, or Terminate
Function block or a corresponding state owner block to highlight blocks
related to it. To show a related block in an open diagram or new tab, pause on the
ellipsis that appears after selection. Then, select **Related
Blocks**
 from the action bar. When multiple blocks correspond
to the selected block, a list of related blocks opens. You can filter the list of
related blocks by entering a search term in the text box. After you select a related
block from the list, window focus goes to the open diagram or new tab that shows the
related block.

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual code generation support depends on block implementation.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type support depends on block implementation.

## Version History

### R2025a: Variant control variables in mask and model workspaces supported

You can define variant control variables in the mask or model workspaces to
control active variants in the Initialize Function block, provided
the **Generate preprocessor conditionals** parameter is
`off`.
