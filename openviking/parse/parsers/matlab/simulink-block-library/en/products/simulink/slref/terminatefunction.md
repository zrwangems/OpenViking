---
type: simulink-block
title: 'Terminate Function'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / User-Defined Functions'
documentation_page: 'terminatefunction'
documentation_source_path: 'slref/terminatefunction.html'
language: en
---

# Terminate Function

## Ports

Not documented in R2025b.

## Parameters

Not documented in R2025b.

## Libraries

Simulink / User-Defined Functions

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

You can define variant control variables in the mask and model workspaces to
control active variants in the Terminate Function block, provided
the **Generate preprocessor conditionals** parameter is
`off`.

## Description

Execute subsystem on model terminate event

The Terminate Function block is a preconfigured Subsystem block that executes on a model terminate event. By default, the
Terminate Function block includes:

- An Event Listener block with
  the **Event type** set to
  `Terminate`
- A Terminator block
- A State Reader block with no
  **State owner block** set

Terminate Function block contents

Customize the contents of the Terminate Function block by, for example,
specifying a **State owner block** for the State Reader
block and replacing the Terminator block with blocks to save the state
value from the State Reader block.

Conditionally executed subsystems with output ports are fully supported within
Terminate Function blocks.

For a list of unsupported blocks and features, see Initialize, Reinitialize, Reset, and Terminate Function Limitations.

The input and output ports of a component containing Initialize
Function and Terminate Function blocks must connect to input
and output port blocks.

The code generated from this block is part of the `model_terminate`
function that is called once at the end of model execution.

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
