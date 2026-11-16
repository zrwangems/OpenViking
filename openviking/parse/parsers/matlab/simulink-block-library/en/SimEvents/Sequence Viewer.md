---
type: simulink-block
title: 'Sequence Viewer'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'sequenceviewer'
documentation_source_path: 'ref/sequenceviewer.html'
language: en
---

# Sequence Viewer

## Ports

Not documented in R2025b.

## Parameters

### **Time Precision for Variable Step** — Digits for time increment precision `3` (default) | scalar

Number of digits for time increment precision. When using a variable step
solver, change this parameter to adjust the time precision for the sequence
viewer. By default the block supports `3` digits of
precision.

Suppose the block displays two events that occur at times
`0.1215` and `0.1219`. Displaying
these two events precisely requires `4` digits of
precision. If the precision is `3`, then the block displays
two events at time `0.121`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `VariableStepTimePrecision` |
| **Type**: string scalar or character vector |
| **Values**: `"3"` | scalar |
| **Default**: `"3"` |

### **History** — Maximum number of previous events to display `5000` (default) | scalar

Total number of events before the last event to display.

For example, if **History** is `5` and
there are `10` events in your simulation, then the block
displays `6` events, including the last event and the five
events prior the last event. Earlier events are not displayed. The time
ruler is greyed to indicate the time between the beginning of the simulation
and the time of the first displayed event.

Each send, receive, drop, or function call event is counted as one event,
even if they occur at the same simulation time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `History` |
| **Type**: string scalar or character vector |
| **Values**: `"1000"` | scalar |
| **Default**: `"1000"` |

## Libraries

Simulink / Messages & Events Simulink Test SimEvents Stateflow

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block can be used for visualizing message transitions during simulation, but
is not included in the generated code.

## Version History

**Introduced in R2015b**

## Description

Display messages, events, states, transitions, and functions between blocks during simulation

The Sequence Viewer block displays messages, events, states,
transitions, and functions between certain blocks during simulation. The blocks that you
can display are called *lifeline blocks* and include:

- Subsystems
- Referenced models
- Blocks that contain messages, such as Stateflow® charts
- Blocks that call functions or generate events, such as Function
  Caller, Function-Call Generator, and MATLAB
  Function blocks
- Blocks that contain functions, such as Function-Call Subsystem
  and Simulink Function blocks

To see states, transitions, and events for lifeline blocks in a referenced model, you
must have a Sequence Viewer block in the referenced model. Without a
Sequence Viewer block in the referenced model, you can see only
messages and functions for lifeline blocks in the referenced model.

**Note**

The Sequence Viewer block does not display function calls generated
by MATLAB Function blocks and S-functions.
