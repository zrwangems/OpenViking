---
type: simulink-block
title: 'N-Sample Switch'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Management / Switches and Counters'
documentation_page: 'nsampleswitch'
documentation_source_path: 'ref/nsampleswitch.html'
language: en
---

# N-Sample Switch

## Ports

### Input

### **Input 1** — First input signal scalar | vector | matrix

Specify the first input signal as a scalar, vector, or a
matrix.

Both inputs must have the same dimension, except in the following two
cases:

- When one input is a scalar, the block expands the scalar input
  to match the size of the other input.
- When one input is an unoriented vector and the other input is
  a row or column vector with the same number of elements, the
  block reshapes the unoriented vector to match the dimension of
  the other input.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

### **Input 2** — Second input signal scalar | vector | matrix

Specify the second input signal as a scalar, vector, or a
matrix.

Both inputs must have the same dimension, except in the following two
cases:

- When one input is a scalar, the block expands the scalar input
  to match the size of the other input.
- When one input is an unoriented vector and the other input is
  a row or column vector with the same number of elements, the
  block reshapes the unoriented vector to match the dimension of
  the other input.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

### **Rst** — Reset signal scalar

Specify the reset signal as a scalar. At any time during the count, a
trigger event at the **Rst** port resets the counter to
zero. The reset sample time must be a positive integer multiple of the
input sample time.

For more information on the reset trigger type, see the description
for the **Trigger type** parameter.

#### Dependencies

To enable this port, select the **Reset input**
check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### Output

### **Output** — Output of the switch scalar | vector | matrix

Output of the switch, returned as a scalar, vector, or a matrix. The
block switches between two inputs after specified number of sample
periods *N*.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### **Switch count, N** — Switch count `8` (default) | nonnegative integer

Specify the number of sample periods, *N*, for which the
output is connected to the top input before switching to the bottom input as
a nonnegative integer.

**Tunable:** Yes

### **Reset input** — Reset input `off` (default) | `on`

Select this check box to enable the **Rst** input port.
The rate of the reset signal must be a positive integer that is a multiple
of the rate of the data signal input.

This block supports triggered subsystems when you select the
**Reset input** check box.

### **Trigger type** — Trigger type `Rising edge` (default) | `Falling edge` | `Either edge` | `Non-zero sample`

Reset the block's counter with the type of event at the
**Rst** port.

You specify the triggering event in the **Trigger
type** pop-up menu, and can be one of the following:

- `Rising edge` — Triggers a reset
  operation when the **Rst** input does one of the
  following:

  - Rises from a negative value to a positive value or
    zero
  - Rises from zero to a positive value, where the rise is not
    a continuation of a rise from a negative value to zero (see
    the following figure)
- `Falling edge` — Triggers a reset
  operation when the `Rst` input does one of the
  following:

  - Falls from a positive value to a negative value or
    zero
  - Falls from zero to a negative value, where the fall is not
    a continuation of a fall from a positive value to zero (see
    the following figure)
- `Either edge` — Triggers a reset
  operation when the `Rst` input is a
  `Rising edge` or `Falling
  edge` (as described above).
- `Non-zero sample` — Triggers a
  reset operation at each sample time that the `Rst`
  input is not zero.

**Tunable:** Yes

#### Dependencies

To enable this parameter, select the **Reset input**
check box.

### **Sample time** — Sample time `0.1` (default) | positive scalar

Specify the sample period *Ts* for
the block's counter as a positive scalar. The block switches inputs at
*t* =
*Ts*×(*N*+1).

You specify the sample period of the output in the **Sample
time** parameter, that is, the output sample period is not
inherited from the sample period of either input.

The block applies a zero-order hold at the input ports, so the value the
block reads from a given port between input sample times is the value of the
most recent input to that port.

## Libraries

DSP System Toolbox / Signal Management / Switches and Counters

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Switch between two inputs after specified number of sample periods

The N-Sample Switch block outputs the signal connected to the top input
port during the first *N* sample times after the simulation begins or
the block is reset, where you specify *N* in the **Switch
count** parameter. Beginning with output sample *N*+1, the
block outputs the signal connected to the bottom input until the next reset event or the
end of the simulation.
