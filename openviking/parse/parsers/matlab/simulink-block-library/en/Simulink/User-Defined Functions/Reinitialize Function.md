---
type: simulink-block
title: 'Reinitialize Function'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / User-Defined Functions'
documentation_page: 'reinitializefunction'
documentation_source_path: 'slref/reinitializefunction.html'
language: en
---

# Reinitialize Function

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

**Introduced in R2022a**

### R2025a: Variant control variables in mask and model workspaces supported

You can define variant control variables in the mask and model workspaces to control
active variants in Reinitialize
Function block, provided the **Generate preprocessor
conditionals** parameter is `off`.

## Description

Execute subsystem on model or subsystem reinitialize event

The Reinitialize Function block is a preconfigured Subsystem block that executes on a model or subsystem reinitialize event. By
default, the Reinitialize Function block includes:

- An Event Listener block with the
  **Event type** set to `Reinitialize` and the
  **Event name** set to `reinit`
- A Constant block with the **Constant value** set to
  `0`
- A State Writer block with no **State
  owner block** set

Reinitialize Function block iconEvent listener block and Constant block connected to State Writer block.

Customize the Reinitialize Function block by, for example, replacing the
Constant block with source blocks that generate the state value for the
State Writer block and specifying a **State owner block**
for the State Writer block.

To generate a model reinitialize event, send a function-call signal to a reinitialize port
of a Model block that references a model that contains a Reinitialize
Function block. To generate a subsystem reinitialize event, send a function-call
signal to a reinitialize port of a Subsystem block that contains a
Reinitialize Function block. The reinitialize event has these effects:

1. The state of each block in the model or subsystem reverts back to its initial
   condition, including blocks within subsystems or referenced models inside the model or
   subsystem receiving the reinitialize event.
2. The contents of the Reinitialize Function block corresponding to the
   reinitialize port are executed.
3. If any subsystems or referenced models inside the model or subsystem receiving the
   reinitialize event contain a Reinitialize Function block, and the
   **Event name** of that block matches the **Event
   name** of the Reinitialize Function block corresponding to the
   reinitialize port, then the contents of those Reinitialize Function
   blocks are executed.

To execute a model referenced by a Model block on a reinitialize event, you
must place a Reinitialize Function block at the root level of the referenced
model. Based on your modeling requirements, you might need to customize the
Reinitialize Function block inside the referenced model.

If a Simulink® based state in a Stateflow® chart contains a Reinitialize Function block, to generate a
subsystem reinitialize event for the state, use a transition event with this
syntax:

```
{StateName.ReinitializeEventName()}
```

Conditionally executed subsystems with output ports are fully supported within
Reinitialize Function blocks.

A model or subsystem can have multiple Reinitialize Function blocks with
each block having a different **Event name**. Each of these reinitialize
events appears in the generated code as a different function. Set the **Event
name** in the block dialog box of the Event Listener block. The
**Event Name** appears on the Reinitialize Function block
icon, and as the port label for the reinitialize port corresponding to the reinitialize
event.

You can select an Initialize Function, Reinitialize
Function, Reset Function, or Terminate Function block or
a corresponding state owner block to highlight blocks related to it. To show a related block
in an open diagram or new tab, pause on the ellipsis that appears after selection. Then,
select **Related Blocks**
Related Blocks button from the action bar. When multiple blocks correspond to the
selected block, a list of related blocks opens. You can filter the list of related blocks by
entering a search term in the text box. After you select a related block from the list, window
focus goes to the open diagram or new tab that shows the related block.
