---
type: simulink-block
title: 'Counter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Buffers, Switches, and Counters'
documentation_page: 'counter'
documentation_source_path: 'ref/counter.html'
language: en
---

# Counter

## Ports

### Input

### **Inc/Dec** — Input signal to trigger count event scalar | vector

Input signal used to determine when the block increments or decrements
the counter, specified as a real-valued scalar or vector. If the input
to the **Inc** or **Dec** port is a
vector, the block treats the vector as a frame. Each time a triggering
event occurs at the **Inc** or **Dec**
input port, the block increments or decrements the counter,
respectively. You control the type of triggering event using the
**Count event** parameter.

#### Dependencies

The block enables the **Inc** (increment) port
when you set the **Count direction**
parameter to `Up`.

The block enables the **Dec** (decrement) port
when you set the **Count direction**
parameter to `Down`.

The block disables the
**Inc**/**Dec** input port
when you set the **Count event**
parameter to `Free running`. In free
running mode, the block counts at a constant time interval.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Rst** — Reset signal scalar

Input signal used to determine when the block resets the counter,
specified as a real-valued scalar. The **Rst** port
must have the same port sample time as the **Inc** or
**Dec** input port. Each time a triggering event
occurs at the **Rst** port, the block resets the
counter to its initial value. For more information about triggering
events, see Count event.

#### Dependencies

To enable this port, select the **Reset input**
check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Max** — Maximum counter size scalar

Specify the maximum counter size as any unsigned integer that the
**Count data type** can represent. The counter
values range from `0` to the value you specify as an
input to the **Max** port.

#### Dependencies

To enable this port, set the **Counter size**
parameter to `Specify via input
port`.

**Data Types:** `uint8` | `uint16` | `uint32`
### Output

### **Cnt** — Current value of counter scalar | vector

Current value of the counter, specified as a scalar or vector. When
you set the **Count event** parameter to
`Free running`, the
**Cnt** output is a *M*-by-1
vector containing the count value at each of *M* consecutive sample times, where *M* is the value you specify for the
**Samples per output frame**
parameter.

#### Dependencies

To enable this port, set the **Output** parameter
to `Count` or `Count and
Hit`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Hit** — Hit status scalar | vector

Hit status of the integer values you specified in the **Hit
values** parameter. When a value you specify occurs in the
count, the block outputs a `1` at the
**Hit** port.

**Note**

The block might output Boolean values from the
**Hit** output port depending on the setting of
the **Hit data type** parameter.

#### Dependencies

To enable this port, set the **Output** parameter
to `Hit` or `Count and
Hit`.

**Data Types:** `Boolean` | `Logical`

## Parameters

### **Count direction** — Count up or down `Up` (default) | `Down`

Specify whether to count `Up` or
`Down`. The port label on the block icon
changes to **Inc** (increment) or **Dec**
(decrement) based on the value of this parameter.

- When you set the **Count direction** parameter to
  `Up` and the counter reaches the upper
  limit of the counter range, the block restarts the counter at zero
  the next time a trigger event occurs at the **Inc**
  port.
- When you set the **Count direction** parameter to
  `Down` and the counter reaches zero,
  the block restarts the counter at the upper limit of the counter
  range the next time a trigger event occurs at the
  **Dec** port.

This parameter is tunable (Simulink) in Simulink® normal mode.

**Tunable:** Yes

### **Count event** — Type of trigger event `Rising edge` (default) | `Falling edge` | `Either edge` | `Non-zero sample` | `Free running`

Specify the type of event that triggers the block to increment, decrement,
or reset the counter when received at the
**Inc**/**Dec** or
**Rst** ports. You can select:

- `Rising edge` — Triggers a count
  or reset operation when the input to the
  **Inc**/**Dec** or
  **Rst** port behaves in one of the following
  ways:

  - Rises from a negative value to a positive value or
    zero.
  - Rises from zero to a positive value, where the rise is not
    a continuation of a rise from a negative value to zero (see
    the following figure).

- `Falling edge` — Triggers a count
  or reset operation when the input to the
  **Inc**/**Dec** or
  **Rst** port behaves in one of the following
  ways:

  - Falls from a positive value to a negative value or
    zero.
  - Falls from zero to a negative value, where the fall is not
    a continuation of a fall from a positive value to zero (see
    the following figure).
- `Either edge` — Triggers a count
  or reset operation when the input to the
  **Inc**/**Dec** or
  **Rst** port is a `Rising
  edge` or `Falling
  edge`.
- `Non-zero sample` — Triggers a
  count or reset operation at each sample time when the input to the
  **Inc**/**Dec** or
  **Rst** port is not zero.
- `Free running` — Disables the
  **Inc**/**Dec** port and
  enables the **Samples per output frame** and
  **Sample time** block parameters. The block
  increments or decrements the counter at a constant interval,
  *Ts*, which you
  specify using the **Sample time** parameter. For
  more information, see Free-Running Operation. In this mode, the block resets
  the counter whenever it receives a non-zero sample at the
  **Rst** port.

#### Dependencies

When you set this parameter to `Free
running`, the block disables the
**Inc**/**Dec** port and counts at
the constant interval specified by the **Sample time**
parameter.

### **Counter size** — Range of integer values to count through `8 bits` (default) | `16 bits` | `32 bits` | `User defined` | `Specify via input port`

Specify the range of integer values the block counts through. When the
block counts through the entire counter range, the next time a trigger event
occurs at the **Inc**/**Dec** port, the
block resets the counter as follows:

- When you set the **Count direction** parameter to
  `Up` and the counter reaches the upper
  limit of the counter range, the block restarts the counter at
  zero.
- When you set the **Count direction** parameter to
  `Down` and the counter reaches zero,
  the block restarts the counter at the upper limit of the counter
  range.

You can set the **Counter size** parameter to one of the
following options:

- `8 bits` — Specifies a counter
  with a range of `0` to
  `255`.
- `16 bits` — Specifies a counter
  with a range of `0` to
  `65535`.
- `32 bits` — Specifies a counter
  with a range of `0` to `2`32–`1`.
- `User defined` — Enables the
  **Maximum count** parameter, which allows you
  to specify the upper-count limit as any arbitrary unsigned integer
  that the **Count data type** can represent. The
  counter values range from `0` to the value of the
  **Maximum count** parameter.
- `Specify via input port` — Enables
  the **Max** input port, which allows you to specify
  the upper-count limit as any arbitrary unsigned integer that the
  **Count data type** can represent. The counter
  values range from `0` to the value you specify as
  an input to the **Max** port.

### **Maximum count** — Maximum value of counter `255` (default) | positive integer

Specify the maximum value of the counter as any unsigned integer
representable by the data type you specify for the **Counter data
type** parameter. Tunable (Simulink) in Simulink normal mode.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Counter size** to
`User defined`.

### **Initial count** — Initial value of counter `0` (default) | integer ≥ 0

Specify the initial value of the counter as any unsigned integer in the
range defined by the **Counter size** parameter. The block
uses the initial value of the counter at the start of simulation and resets
the counter back to that initial value each time a trigger event occurs at
the **Rst** port.

**Tunable:** Yes

### **Output** — Output count value, hit value, or both `Count` (default) | `Hit` | `Count and Hit`

Select the output ports to enable. You can choose to enable the
`Count`, `Hit`, or
`Count and Hit` ports.

### **Hit values** — Count values to flag `32` (default) | scalar | vector

Specify an integer or vector of integers whose occurrence in the count
should be flagged by a `1` at the (optional)
**Hit** output port. This parameter appears only when
you set the **Output** parameter to `Hit`
or `Count and Hit`.

**Tunable:** Yes

### **Reset input** — Enable Rst input port `on` (default) | `off`

Select this check box to enable the **Rst** input port.
When you enable the **Rst** port, the block resets the
counter to its initial value each time a trigger event occurs at the
**Rst** port. To specify the type of event that
triggers a reset of the counter, set the **Count event**
parameter. When you clear the **Reset input** check box,
you cannot reset the counter during simulation.

### **Samples per output frame** — Number of samples in each output vector `1` (default) | positive integer

Specify the number of samples, *M*, in each output vector
as a positive integer.

#### Dependencies

To enable this parameter, set the **Count
event** to `Free running`.

### **Sample time** — Sample time in `Free Running` mode `1` (default) | `-1` | scalar ≥ 0

Specify the constant interval,
*T*s, at which the block
increments or decrements the counter when in free-running mode. You can
specify a scalar that is greater than or equal to zero, or specify a value
of `-1` to inherit the sample time.

For example, to have the block increment the counter every
`5` seconds, set the **Count
direction** parameter to `Up`, the
**Count event** parameter to `Free
running`, and specify a value of `5` for
the **Sample time** parameter. In free running mode, the
sample time of the output ports is always
*M**T*s.

#### Dependencies

To enable this parameter, set the **Count
event** to `Free
running`.

### **Count data type** — Data type of Cnt port `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

Specify the data type of the output at the **Cnt**
port.

#### Dependencies

To enable this parameter, set the **Output**
parameter to `Count` or `Count and
Hit`.

### **Hit data type** — Data type of Hit port `Logical` (default) | `Boolean`

Specify the data type of the output at the **Hit**
port.

#### Dependencies

To enable this parameter, set the **Output**
parameter to `Hit` or set it to
`Count and Hit` with the **Count
data type** parameter set to
`Double`.

## Libraries

DSP System Toolbox / Signal Management / Switches and Counters

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Count up or down through specified range of numbers

The Counter block counts up or down through a specified range of
numbers. The block enables the **Inc** (increment) port when you set
the **Count direction** parameter to `Up`.
When you set the **Count direction** parameter to
`Down`, the block enables the **Dec**
(decrement) port. If you set the **Count event** parameter to
`Free running`, the block disables the
**Inc** or **Dec** port and counts at a constant
time interval. For all other settings of the **Count event** parameter,
the block increments or decrements the counter each time a trigger event occurs at the
**Inc** or **Dec** input port. When a trigger
event occurs at the optional **Rst** port, the block resets the counter
to its initial state.

The Counter block accepts single-channel inputs. For more information
about scalar input operation, vector input operation, and free-running operation, see
Algorithms.
