---
type: simulink-block
title: 'Stack'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Management / Buffers'
documentation_page: 'stack'
documentation_source_path: 'ref/stack.html'
language: en
---

# Stack

## Ports
```yaml
ports:
- name: In
  summary: Input scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: Push
  summary: Trigger event to push input scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Pop
  summary: Trigger event to pop elements scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Rst
  summary: Empty stack contents scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Out
  summary: Output scalar | vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: Empty
  summary: Empty stack indicator port scalar
  direction: output
  data_types: Boolean
- name: Full
  summary: Full stack indicator port scalar
  direction: output
  data_types: Boolean
- name: Num
  summary: Number of stack entries port scalar
  direction: output
  data_types: double | uint32
```

### Input

### **In** — Input scalar | vector | matrix

Specify the input as a scalar, vector, or a matrix.

When the block receives a trigger event at the
**Push** port, the block pushes the input at the
**In** port onto the top of the stack.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

### **Push** — Trigger event to push input scalar

Specify a trigger event at this port to push the input at the **In**
port to the top of the stack. The last input that the block pushes to
the stack is always the first to be popped off.

Inputs to this port must have the same built-in data type as inputs to
the **Pop** and **Rst** input
ports

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Pop** — Trigger event to pop elements scalar

Specify a trigger event at this port to pop the top element off the stack and to hold
the **Out** port at that value. The last input that the
block pushes to the stack is always the first to be popped off.

Inputs to this port must have the same built-in data type as inputs to
the **Push** and **Rst** input
ports

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Rst** — Empty stack contents scalar

Specify a trigger event at this port to empty the stack contents. When
you select **Clear output port on reset**, then a
trigger event at the **Rst** port empties the stack and
sets the value at the **Out** port to zero. This
setting also applies when a disabled subsystem containing the
Stack block is reenabled. In this case, when you
select **Clear output port on reset**, the
**Out** port value is only reset to zero.

Inputs to this port must have the same built-in data type as inputs to
the **Push** and **Pop** input
ports.

#### Dependencies

To enable this port, select **Show reset port (Rst) to
clear internal stack buffer**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Out** — Output scalar | vector | matrix

Stack output, returned as a scalar, vector, or a matrix. When you specify a trigger
event at the **Pop** port, the block pops the top
element off the stack and holds the **Out** port at
that value. The last input that the block pushes to the stack is always
the first to be popped off.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

### **Empty** — Empty stack indicator port scalar

The **Empty** port outputs a high (1) when the stack
is empty and low (0) otherwise.

#### Dependencies

To enable this port, select **Show empty stack indicator
port (Empty)**.

**Data Types:** `Boolean`

### **Full** — Full stack indicator port scalar

The **Full** port outputs a high (1) when the stack is full and low (0)
otherwise. The **Full** port remains low when you
select `Dynamic reallocation` in the
**Push full stack** parameter.

#### Dependencies

To enable this port, select **Show full stack indicator
port (Full)**.

**Data Types:** `Boolean`

### **Num** — Number of stack entries port scalar

The **Num** port outputs the number of stack entries through this port.
This value indicates the number of entries currently on the stack. The
block outputs a double-precision floating-point value at this port when
the input at the **In** port is of the double-precision
floating-point data type. The block outputs a 32-bit unsigned integer
value at this port when the input at the **In** port is
not a double-precision floating-point value.

#### Dependencies

To enable this port, select **Show number of stack entries
port (Num)**.

**Data Types:** `double` | `uint32`
## Parameters
```yaml
parameters:
- name: Stack depth
  summary: Number of entries stack can hold 8 (default) | positive integer
  group: ''
- name: Trigger type
  summary: Trigger type Rising edge (default) | Falling edge | Either edge | Non-zero sample
  group: ''
- name: Push full stack
  summary: Push full stack Dynamic reallocation (default) | Ignore | Warning | Error
  group: ''
- name: Pop empty stack
  summary: Pop empty stack Warning (default) | Ignore | Error
  group: ''
- name: Show empty stack indicator port (Empty)
  summary: Enable empty stack indicator port off (default) | on
  group: ''
- name: Show full stack indicator port (Full)
  summary: Enable full stack indicator port off (default) | on
  group: ''
- name: Show number of stack entries port (Num)
  summary: Enable number of stack entries port off (default) | on
  group: ''
- name: Show reset port (Rst) to clear internal stack buffer
  summary: Enable reset port off (default) | on
  group: ''
- name: Clear output port on reset
  summary: Clear output port on reset off (default) | on
  group: ''
```

### **Stack depth** — Number of entries stack can hold `8` (default) | positive integer

Specify the number of entries that the LIFO register can hold as a
positive integer.

### **Trigger type** — Trigger type `Rising edge` (default) | `Falling edge` | `Either edge` | `Non-zero sample`

Specify the type of event that triggers the block execution. The rate of
the trigger signal must be the same as the rate of the data signal
input.

Specify the triggering event for the **Push**, **Pop**,
and **Rst** ports as one of these options:

- `Rising edge` — Triggers execution
  of the block when the trigger input does one of the
  following:

  - Rises from a negative value to a positive value or
    0
  - Rises from 0 to a positive value, where the rise is not a
    continuation of a rise from a negative value to 0 (see the
    figure)
- `Falling edge` — Triggers
  execution of the block when the trigger input does one of the
  following:

  - Falls from a positive value to a negative value or
    0
  - Falls from 0 to a negative value, where the fall is not a
    continuation of a fall from a positive value to 0 (see the
    figure)

- `Either edge` — Triggers execution
  of the block when the trigger input behaves as described in
  `Rising edge` or `Falling
  edge`.
- `Non-zero sample` — Triggers
  execution of the block at each sample time that the trigger input is
  not 0.

### **Push full stack** — Push full stack `Dynamic reallocation` (default) | `Ignore` | `Warning` | `Error`

Use this parameter to specify how the block responds to the trigger at the
**Push** port when the register is full.

- `Dynamic reallocation` –– Dynamically
  resize the register to accept as many additional inputs as
  memory permits. To find out how many elements are on the stack
  at a given time, enable the **Num** output port
  by selecting the **Show number of stack entries
  port** parameter.

  To select this option, you must set the **System
  target file** parameter on the **Code
  Generation** pane of the Model Configuration
  Parameters dialog box to `grt_malloc.tlc – Generic
  Real-Time Target with dynamic memory
  allocation`.

  **Note**

  If your model contains any referenced models that use a
  Stack block with the **Push full
  stack** parameter set to `Dynamic
  reallocation`, you cannot simulate your
  top-level model in Simulink® Accelerator mode.
- `Ignore` — Ignore the trigger
  event and continue the simulation.
- `Warning` — Ignore the trigger
  event but display a warning message in the MATLAB® command window.
- `Error` — Display an error
  dialog box and terminate the simulation.

**Note**

The **Push full stack** parameter is a diagnostic
parameter. Like all diagnostic parameters on the Configuration
Parameters dialog box, this parameter is set to
`Ignore` in the code generated for this
block by the Simulink
Coder™ code generation software.

### **Pop empty stack** — Pop empty stack `Warning` (default) | `Ignore` | `Error`

Use this parameter to specify how the block responds to the trigger at the
**Pop** port when the register is empty.

- `Warning` — Ignore the trigger
  event but display a warning message in the MATLAB command window.
- `Ignore` — Ignore the trigger
  event and continue the simulation.
- `Error` — Display an error
  dialog box and terminate the simulation.

**Note**

The **Pop empty stack** parameter is a diagnostic
parameter. Like all diagnostic parameters on the Configuration
Parameters dialog box, this parameter is set to
`Ignore` in the code generated for this
block by the Simulink
Coder code generation software.

### **Show empty stack indicator port (Empty)** — Enable empty stack indicator port `off` (default) | `on`

Enable the **Empty** output port, which is high
(`1`) when the stack is empty, and low
(`0`) otherwise.

### **Show full stack indicator port (Full)** — Enable full stack indicator port `off` (default) | `on`

Enable the **Full** output port, which is high
(`1`) when the stack is full, and low
(`0`) otherwise. The `Full` port
remains low when you select `Dynamic reallocation`
in the **Push full stack** parameter.

### **Show number of stack entries port (Num)** — Enable number of stack entries port `off` (default) | `on`

Enable the **Num** output port, which tracks the number
of entries currently on the stack. When inputs to the
**In** port are double-precision values, the outputs
from the **Num** port are also double-precision values.
Otherwise, the outputs from the **Num** port are 32-bit
unsigned integer values.

### **Show reset port (Rst) to clear internal stack buffer** — Enable reset port `off` (default) | `on`

Enable the **Rst** input port to empty the stack when the
block receives the trigger specified in the **Trigger
type** parameter.

### **Clear output port on reset** — Clear output port on reset `off` (default) | `on`

Reset the **Out** port to 0 (in addition to clearing the stack) when the
block receives a trigger at the **Rst** input port.
## Libraries

DSP System Toolbox / Signal Management / Buffers

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

The following limitations apply:

- Generated code relies on the `memcpy` or
  `memset` function (`string.h`) under certain
  conditions.
- When you select `Dynamic reallocation`, the **System target file** parameter on the **Code Generation** pane of the Configuration
  Parameters dialog box must be set to `grt_malloc.tlc - Generic
  Real-Time Target with dynamic memory allocation`.

## Version History

**Introduced before R2006a**

## Description

Store inputs into LIFO register

The Stack block stores a sequence of input samples in a last in, first out
(LIFO) register. You set the register capacity in the **Stack depth**
parameter. Inputs to the block can be scalars, vectors, or matrices.

The block pushes the input at the **In** port to the top of the stack when
it receives a trigger event at the **Push** port. When it receives a
trigger event at the **Pop** port, the block pops the top element off
the stack and holds the **Out** port at that value. The last input that
the block pushes on the stack is always the first to be popped off.

When you trigger two or more of the control input ports at the same time step, the
block executes the operations in this order:

1. Reset (Rst)
2. Push
3. Pop
