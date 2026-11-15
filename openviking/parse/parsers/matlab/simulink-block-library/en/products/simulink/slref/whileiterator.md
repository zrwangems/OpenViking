---
type: simulink-block
title: 'While Iterator'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Modeling / Design Model Behavior / Iterator Subsystems'
documentation_page: 'whileiterator'
documentation_source_path: 'slref/whileiterator.html'
language: en
---

# While Iterator

## Ports

### Input

### **cond** — Logical condition signal scalar

Signal with the result from evaluating a logical condition. Because
the subsystem is not externally triggered during a time step, evaluating
a condition as true (`1`) or false
(`0`) must reside within the subsystem.

The data type and values of the signal can be:

- Logical (Boolean) — true (`1`) or
  false (`0`).
- Numerical — true (any positive or negative number)
  or false (`0`).

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **IC** — Initial logical condition scalar

Signal with the initial logical condition. At the beginning of each
time step:

- If `IC` is false (`0`),
  the subsystem does not execute during the time step.
- If `IC` is true (value not equal to
  `0`), the subsystem starts executing
  and continues to repeat execution as long as the
  `cond` signal is true.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### Output Arguments

### **Iteration number** — Signal with the number of iterations scalar

Signal with the number of While Iterator Subsystem
block executions during each time step.

**Data Types:** `double` | `int8` | `int16` | `int32`

## Parameters

### **Maximum number of iterations** — Specify maximum number of iterations `-1` (default) | integer

Specify maximum number of iterations allowed during a time step.

`-1`
:   Any number of iterations as long as the
    `cond` signal is true (value not equal to
    `0`). If you specify `-1`
    and the `cond` signal never becomes false
    (`0`), the simulation runs in an infinite
    loop. In this case, the only way to stop the simulation is to
    terminate MATLAB®.

integer
:   Maximum number of iterations during a time step.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MaxIters` |
| **Type**: character vector |
| **Values**: `'5'` | `'-1'` | integer in quotes |
| **Default**: `'5'` |

### **While loop type** — Select type of block `while` (default) | `do-while`

Select type of block.

`while`
:   The While Iterator block has two inputs, a
    `cond` (logical condition) input and an
    `IC` (initial logical condition) input. The
    source of the `IC` signal must be external to
    the While Iterator Subsystem block.

    At the beginning of each time step:

    - If the `IC` input is true (value
      not equal to `0`), the blocks in
      the subsystem repeat execution while the
      `cond` input is true. This
      process continues during a time step as long as the
      `cond` input is true and the
      number of iterations is less than or equal to the
      **Maximum number of
      iterations**.
    - If the `IC` input is false, the
      While Iterator block does not
      execute the contents of the subsystem.

`do-while`
:   The While Iterator block has one input, the
    `cond` (while condition) input.

    At each time step, the blocks in the subsystem repeat
    execution while the `cond` input is true (value
    not equal to `0`). This process continues as
    long as the `cond` input is true and the number
    of iterations is less than or equal to the **Maximum
    number of iterations**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `WhileBlockType` |
| **Type**: character vector |
| **Values**: `'while'` | `'do-while'` |
| **Default**: `'while'` |

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

### **Show iteration number port** — Control display of output port `off` | `on`

Control display of output port for signal with number of block executions.
The value of the signal from this port starts at
`1`and is incremented by
`1` for each succeeding iteration.

off
:   Remove output port.

on
:   Display output port for signal with iteration number.

#### Dependencies

Selecting this parameter enables the **Output data
type** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ShowIterationPort` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Output data type** — Select output data type for current iteration number `int32` (default) | `uint32` | `int16` | `uint16` | `int8` | `uint8` | `double`

Select output data type for iteration number signal. The value of this
signal is the number of iterations during a time step and the total number
of iterations at the end of a time step. The maximum allowable value for the
signal is determined by the **Output data type** parameter.
For example, if you set **Output data type** as
`int8`, the maximum allowable value for the
signal is 27-1. However, if you set
**Output data type** as
`uint32` or `double`,
the maximum allowable value for the signal is restricted to the maximum
positive value for signed 32-bit integer (`int32`). For
more information about range of values for different integer classes, see
Integers.

`int32`
:   Signed 32-bit integer.

`uint32`
:   Unsigned 32-bit integer.

`int16`
:   Signed 16-bit integer.

`uint16`
:   unsigned 16-bit integer.

`int8`
:   Signed 8-bit integer.

`uint8`
:   Unsigned 8-bit integer.

`double`
:   Double-precision floating point.

#### Dependencies

Select the **Show iteration number port** check box
to enable this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputDataType` |
| **Type**: character vector |
| **Value**: `'int32'` | `'unt32'` | `'int16'` | `'uint16'`|`'int8'` | `'uint8'` | `'double'` |
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

Control block for while-iterator subsystem

The While Iterator block, when placed in a Subsystem
block, repeatedly executes the contents of the subsystem during the current time step
while the value of the input condition is true or `1`. Use this block
to implement the block diagram equivalent of a `while` loop in a
programming language.

The While Iterator Subsystem block is
preconfigured with a While Iterator block. Placing a While
Iterator block in a Subsystem block makes it an atomic
subsystem.
