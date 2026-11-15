---
type: simulink-block
title: 'Queue'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Buffers, Switches, and Counters'
documentation_page: 'queue'
documentation_source_path: 'ref/queue.html'
language: en
---

# Queue

## Ports

### Input

### **In** — Input to FIFO register scalar | vector | matrix

Specify the input to the FIFO register as a scalar, vector, or a
matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **Push** — Trigger signal to push queue scalar

Specify the trigger signal to push the queue as a real scalar.

Input to the **Push** port must have the same data
type as the input to the **Pop** and
**Rst** ports.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Pop** — Trigger signal to pop queue scalar

Specify the trigger signal to pop the queue as a real scalar.

Input to the **Pop** port must have the same data
type as the inputs to the **Push** and
**Rst** ports.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Rst** — Trigger signal to empty queue scalar

Specify the trigger signal to empty the queue as a real scalar.

Input to the **Rst** port must have the same data
type as the inputs to the **Push** and
**Pop** ports.

#### Dependencies

To enable this port, select **Show reset port (Rst) to
clear internal stack buffer**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Out** — Output of FIFO register scalar | vector | matrix

Output of the FIFO register, returned as a scalar, vector, or a
matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **Empty** — Indicates if queue is empty `1` | `0`

The block returns `1` at this port to indicate an
empty queue and `0` otherwise.

#### Dependencies

To enable this port, select **Show empty register
indicator port (Empty)**.

**Data Types:** `double` | `Boolean`

### **Full** — Indicates if queue is full `1` | `0`

The block returns `1` at this port to indicate a full
queue and `0` otherwise.

If you select `Dynamic reallocation` in the
**Push onto full register** parameter, the
**Full** port remains `0`.

#### Dependencies

To enable this port, select **Show full register indicator
port (Full)**.

**Data Types:** `double` | `Boolean`

### **Num** — Track number of elements in queue scalar

Track the number of elements in the queue at any given time.

If the data type at the **In** port is
`double`, the data type at the
**Num** port is `double`.
Otherwise, the data type at the **Num** port is
`uint32`.

#### Dependencies

To enable this port, select **Show number of register
entries port (Num)**.

**Data Types:** `double` | `uint32`

## Parameters

### **Register size** — Number of entries FIFO register can hold 8 (default) | positive integer

The number of entries that the FIFO register can hold, specified as a
positive integer.

### **Trigger type** — Type of trigger event for Push, Pop, and Rst ports `Rising edge` (default) | `Falling edge` | `Either edge` | `Non-zero sample`

The type of event that triggers the execution of the block. Select one of
these options:

| Trigger Type | Description |
| --- | --- |
| `Rising edge` | Triggers execution of the block when the trigger input does one of the following:  - Rises from a negative value to zero or a   positive value. - Rises from zero to a positive value but is not   a continuing rise. |
| `Falling edge` | Triggers execution of the block when the trigger input does one of the following:  - Falls from a positive value to zero or a   negative value. - Falls from zero to a negative value but is not   a continuing fall. |
| `Either edge` | Triggers execution of the block when the trigger input type is `Rising edge` or `Falling edge` (as described above). |
| `Non-zero sample` | Triggers execution of the block at each sample time that the trigger input is not zero. |

The rate of the trigger signal must be the same as the rate of the data
signal input.

### **Push onto full register** — Specify block behavior to push request when register is full `Dynamic reallocation` (default) | `Ignore` | `Warning` | `Error`

Specify the block behavior when it receives a trigger at the
**Push** port but the register is full. The available
options are:

- `Dynamic reallocation` — Dynamically
  resize the register to accept as many additional inputs as memory
  permits.

  To use this option, set the **System target
  file** parameter on the **Code
  Generation** pane of the Model Configuration Parameters
  dialog box to `grt_malloc.tlc – Generic Real-Time Target
  with dynamic memory allocation`.

  **Note**

  If your model contains any referenced models that use a
  Queue block with the **Push onto full
  register** parameter set to
  `Dynamic reallocation`, you
  cannot simulate your top-level model in the accelerator mode
  in Simulink®.
- `Ignore` — Ignore the trigger event and
  continue the simulation.
- `Warning` — Ignore the trigger event but
  display a warning message in the MATLAB® Command Window.
- `Error` — Display an error dialog box and
  terminate the simulation.

**Note**

The **Push onto full register** is a diagnostic
parameter. Like all diagnostic parameters in the Configuration
Parameters dialog box, this parameter is set to
`Ignore` in the code generated for this
block by the Simulink
Coder™ code generation software.

### **Pop empty register** — Specify block behavior to pop request when register is empty `Warning` (default) | `Ignore` | `Error`

Specify the block behavior when it receives a trigger at the
**Pop** port but the register is empty. The available
options are:

- `Ignore` — Ignore the trigger event and
  continue the simulation.
- `Warning` — Ignore the trigger event but
  display a warning message in the MATLAB Command Window.
- `Error` — Display an error dialog box and
  terminate the simulation.

**Note**

The **Pop empty register** is a diagnostic parameter.
Like all diagnostic parameters in the Configuration Parameters dialog
box, this parameter is set to `Ignore` in the
code generated for this block by the Simulink
Coder code generation software.

### **Show empty register indicator port (Empty)** — Enable Empty output port off (default) | on

Select to enable the **Empty** output port to indicate an
empty register.

### **Show full register indicator port (Full)** — Enable Full output port off (default) | on

Select to enable the **Full** output port to indicate a
full register.

### **Show number of register entries port (Num)** — Enable Num output port off (default) | on

Select to enable the **Num** output port to show the
number of register entries.

### **Show reset port (Rst) to clear internal stack buffer** — Enable Rst input port off (default) | on

Select to enable the **Rst** input port. The block
empties the queue when it receives a trigger at this port.

### **Clear output port on reset** — Set Out port to `0` when clearing queue off (default) | on

If you select **Clear output port on reset**, then a
trigger event at the **Rst** port empties the queue and
sets the value at the **Out** port to `0`.
This setting also applies when a disabled subsystem containing the
Queue block is re-enabled.

#### Dependencies

To enable this parameter, select the **Show reset port (Rst)
to clear internal stack buffer** parameter.

### **Allow direct feedthrough** — Allow input data to be readily available at Out port on (default) | off

Select to allow the input data to be available immediately at the
**Out** port of the block. Clear to delay the input
data by an extra frame.

When you select the **Allow direct feedthrough**
parameter and trigger two or more of the control input ports at the same
time step, the block executes the operations in the following order:

1. Reset
2. Push
3. Pop

When you clear the **Allow direct feedthrough** parameter
and trigger two or more of the control input ports at the same time step,
the block executes the operations in the following order:

1. Reset
2. Pop
3. Push

The rate of the trigger signal must be the same as the rate of the data
signal input.

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
- When you select `Dynamic reallocation`, you must
  set the **System target file** parameter on the
  **Code Generation** pane of the Configuration
  Parameters dialog box to `grt_malloc.tlc - Generic Real-Time
  Target with dynamic memory allocation`.

## Version History

**Introduced before R2006a**

## Description

Store inputs in FIFO register

The Queue block stores a sequence of input samples in a first-in
first-out (FIFO) register. Depending on the inputs at the ports, the block can push,
pop, or empty the queue.

When the block receives a trigger event at the **Push** port, it
pushes the input at the **In** port to the end of the queue. When the
block receives a trigger event at the **Pop** port, it pops the first
element off the queue and holds the **Out** port at that value. The
first input to be pushed onto the queue is always the first to be popped off.
