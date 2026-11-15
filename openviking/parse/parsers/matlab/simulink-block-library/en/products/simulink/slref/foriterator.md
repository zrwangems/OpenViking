---
type: simulink-block
title: 'For Iterator'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Modeling / Design Model Behavior / Iterator Subsystems'
documentation_page: 'foriterator'
documentation_source_path: 'slref/foriterator.html'
language: en
---

# For Iterator

## Ports

### Input

### **Number of Iterations** — External value for iterator variable scalar | vector, size 1 | matrix, size 1x1

- The input port accepts data of mixed numeric types.
- If the input port value is non-integer, it is first truncated
  to an integer.
- Internally, the input value is cast to an integer of the type
  specified for the iteration variable output port.
- If no output port is specified, the input port value is cast
  to type `int32`.
- If the input port value exceeds the maximum value of the
  output port type, the overflow saturates.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Iterator value** — Value of iterator variable during time step scalar | vector, size 1 | matrix, size 1-by-1

Selecting the **Show iteration variable** parameter
check box adds an output port to this block.

**Data Types:** `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **States when starting** — Select block states between time steps `held` (default) | `reset`

Select how to handle block states between time steps.

`held`
:   Hold block states between time steps. Block state values
    persist across time steps.

`reset`
:   Reset block states to their initial values at the beginning of
    each time step and before the first iteration loop.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ResetStates` |
| **Type**: character vector |
| **Values**: `'held'` | `'reset'` |
| **Default**: `'held'` |

### **Iteration limit source** — Select source for number of iterations `internal` (default) | `external`

Select source for number of iterations.

`internal`
:   Value of the **Iteration limit**
    parameter determines the number of iterations.

`external`
:   Value of the signal at the **N** port
    determines the number of iterations. The signal source must
    reside outside the For Iterator Subsystem
    block.

#### Dependencies

Selecting `internal` displays and enables the
**Iteration limit** parameter. Selecting
`external` adds an input port labeled
**N**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IterationSource` |
| **Type**: character vector |
| **Values**: `'internal'` | `'external'` |
| **Default**: `'internal'` |

### **Iteration limit** — Specify number of iterations `5` (default) | integer

Specify the number of iterations. This parameter supports storage classes.
You can define the named constant in the base workspace of the Model
Explorer as a `Simulink.Parameter` object
of the built-in storage class `Define (custom)`
type.

`5`
:   Iterate blocks in the For Iterator Subsystem
    block `5` times.

integer
:   Specify an integer or a named constant variable.

#### Dependencies

To enable this parameter, select `internal`
from the **Iteration limit source** drop-down
list.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IterationLimit` |
| **Type**: character vector |
| **Values**: `'5'` | integer in quotes |
| **Default**: `'5'` |

### **Set Next i (iteration variable) externally** — Control display of input port `off` (default) | `on`

Control display of an input port.

off
:   Remove input port.

on
:   Add input port labeled **Next\_i** for
    connecting to an external iteration variable source. The value
    of the input at the current iteration is used as the value of
    the iteration variable at the next iteration.

#### Dependencies

To enable this parameter, select the **Show iteration
variable** parameter which also displays an output port
labeled **1:N**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ExternalIncrement` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Show iteration variable** — Control display of output port `on` (default) | `off`

Control the display of an output port with the current iterator value for
a loop.

on
:   Add output port labeled **1:N** to the
    For Iterator block.

off
:   Remove output port.

#### Dependencies

Selecting this parameter enables the **Set next i (iteration
variable) externally** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ShowIterationPort` |
| **Type**: character vector |
| **Value**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Index mode** — Select initial iteration number `One-based` (default) | `Zero-based`

Select an initial iteration number of `0` or
`1`.

`One-based`
:   Iteration number starts at one.

`Zero-based`
:   Iteration number starts at zero.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IndexMode` |
| **Type**: character vector |
| **Values**: `'One-based'` | `'Zero-based'` |
| **Default**: `'One-based'` |

### **Iteration variable data type** — Select data type `int32` (default) | `uint32` | `int16` | `uint16` | `int8` | `uint8` | `double`

Set the data type for the iteration value output from the iteration number
port. The maximum allowable value for the iteration variable is determined
by the **Index mode** and **Iteration variable data
type** parameters. For example, if you set **Index
mode** as `One-based` and
**Iteration variable data type** as
`int8`, the maximum allowable value for the
iteration variable is 27-1. However, if you set
**Iteration variable data type** as
`uint32` or `double`,
the maximum allowable value for the iteration variable is restricted to the
maximum positive value for signed 32-bit integer (`int32`).
For more information about range of values for different integer classes,
see Integers.

`int32`
:   Set data type to `int32`.

`uint32`
:   Set data type to `uint32`.

`int16`
:   Set data type to `int16`.

`uint16`
:   Set data type to `uint16`.

`int8`
:   Set data type to `int8`.

`uint8`
:   Set data type to `uint8`.

`double`
:   Set data type to `double`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IterationVariableDataType` |
| **Type**: character vector |
| **Value**: `'int32'` | `'uint32'` | `'int16'` | `'uint16'` | `'int8'` | `'uint8'` | `'double'` |
| **Default**: `'int32'` |

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

### R2024b: Add signal breakpoints and port value labels to iteration number outputs in iterator subsystems

You can now pause a simulation on a particular iteration of an iterator subsystem by adding
signal breakpoints to signals produced by:

- Iteration number output ports of While Iterator blocks inside While Iterator Subsystem blocks
- Iterator value output ports of For Iterator blocks inside For Iterator Subsystem blocks
- Partition index output ports of For Each blocks inside For Each Subsystem blocks

In previous releases, you could add a breakpoint in these locations, but the breakpoints
did not pause the simulation and appeared as invalid in the block diagram.

Port value labels at the same locations now display the iteration number. In previous releases, port value labels at these locations showed `inaccessible`.

For an example, see Debug Simulation of Iterator Subsystem.

## Description

Control block for for-iterator subsystem

The For Iterator block, when placed in a Subsystem
block, repeats the execution of a subsystem during the current time step until an
iteration variable exceeds the specified iteration limit. You can use this block to
implement the block diagram equivalent of a `for` loop in a programming
language.

The output of a For Iterator Subsystem block cannot be
a function-call signal. Simulink® displays an error message when the model updates.
