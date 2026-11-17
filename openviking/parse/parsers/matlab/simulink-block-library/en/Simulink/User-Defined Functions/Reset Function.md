---
type: simulink-block
title: 'Reset Function'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'resetfunction'
documentation_source_path: 'slref/resetfunction.html'
language: en
---

# Reset Function

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters: []
```

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
control active variants in the Reset Function block, provided the
**Generate preprocessor conditionals** parameter is
`off`.

## Description

Execute subsystem on model reset event

The Reset Function block is a preconfigured Subsystem block that executes on a model reset event. By default, the
Reset Function block includes:

- An Event Listener block with
  the **Event type** set to `Reset`
  and the **Event name** set to
  `reset`
- A Constant block with the **Constant
  value** set to `0`
- A State Writer block with no
  **State owner block** set

Reset Function block contents

Customize the contents of the Reset Function block by, for example,
replacing the Constant block with source blocks that generate the state
value for the State Writer block and specifying a **State owner
block** for the State Writer block.

Conditionally executed subsystems with output ports are fully supported within
Reset Function blocks.

For a list of unsupported blocks and features, see Initialize, Reinitialize, Reset, and Terminate Function Limitations.

A model can potentially have multiple Reset Function blocks with each
block having a different **Event name**. Each of these reset events
appear in the generated code as a different function.

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
