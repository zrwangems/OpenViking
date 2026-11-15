---
type: simulink-block
title: 'Event-Count Comparator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Buffers, Switches, and Counters'
documentation_page: 'eventcountcomparator'
documentation_source_path: 'ref/eventcountcomparator.html'
language: en
---

# Event-Count Comparator

## Ports

### Input

### **Data** — Data input scalar

Specify the data input as a discrete-time scalar.

The Event-Count Comparator block accepts real and complex floating-point
and fixed-point inputs. However, because the block has a discrete state,
it does not support constant or continuous sample times. Therefore, you
must connect at least one of the input ports or the output port of the
Event-Count Comparator block to a block whose
**Sample time** parameter is discrete. The
Event-Count Comparator block inherits this
noninfinite discrete sample time.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`
**Complex Number Support:** Yes

### **Int** — Interval enable signal scalar

Specify the interval enable signal as a scalar. A nonzero input at this port enables the
block to begin counting and resets the output.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`
### Output

### **Out** — Detect required number of nonzero inputs `true` or `1` | `false` or `0`

The block returns a logical `1` if the number of
nonzero inputs over time equals or exceeds the value you specify in the
**Event threshold** parameter.

**Data Types:** `Boolean`

## Parameters

### **Event threshold** — Event threshold `10` (default) | nonnegative integer

Specify the event threshold as a nonnegative integer. The block compares the number of
nonzero inputs to this value. If the number of nonzero inputs over time
equals or exceeds the value you specify in this parameter, the block returns
a logical `1`.

**Tunable:** Yes

## Libraries

DSP System Toolbox / Signal Management / Switches and Counters

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

## Version History

**Introduced before R2006a**

## Description

Detect threshold crossing of accumulated nonzero inputs

The Event-Count Comparator block detects the number of nonzero inputs at the
**Data** port during the period that the block is enabled by a high
signal (of value `1`) at the **Int** port. Both inputs
must be scalars.

When the number of accumulated nonzero inputs first equals the value in the **Event
threshold** parameter, the block waits one additional sample interval, and
then sets the **Out** port to `1`. The block holds the
**Out** port at `1` until the signal at the
**Int** port transitions from a low value (`0`) to
a high value (`1`).
