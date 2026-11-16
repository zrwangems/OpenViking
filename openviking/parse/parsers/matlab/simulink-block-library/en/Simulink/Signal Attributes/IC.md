---
type: simulink-block
title: 'IC'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'ic'
documentation_source_path: 'slref/ic.html'
language: en
---

# IC

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

Input signal, specified as a scalar, vector, matrix, or N-D array. The
block sets the initial condition of this signal to the **Initial
value** you specify.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — Output signal scalar | vector | matrix | N-D array

Output signal provided as the **Initial value** you specify, followed
by the actual values of the input signal. See Behavior for Nonzero Sample Time Offset
for more information.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **Initial value** — Initial value `1` (default) | real, finite scalar, vector, matrix, or N-D array

Specify the initial value of the input signal as a finite, real-valued scalar, vector,
matrix, or N-D array. The value must be a scalar, or have the same
dimensions as the input signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Value` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix | N-D array |
| **Default:** `'1'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Dependencies

This parameter is visible only if you set it to a value other than
`-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar or vector in quotes |

## Libraries

Simulink / Signal Attributes

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code. Relates to resource limits and restrictions on speed
and memory often found in embedded systems. Generated code can contain dynamic
allocation and freeing of memory, recursion, additional memory overhead, and widely
varying execution times. While the code is functionally valid and generally
acceptable in resource-rich environments, smaller embedded targets often cannot
support such code. Usually, blocks evolve toward being suitable for production code.
Thus, blocks suitable for production code remain suitable.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2023b: IC Block Row-Major Support Update

The IC block now supports code generation for row-major array
layout.

## Description

Set initial value of signal

The IC block sets the initial condition of the signal at its input port, for
example, the value of the signal at the simulation start time
(`tstart`). To do so, the block outputs
the specified initial condition when you start the simulation, regardless of the actual
value of the input signal. Thereafter, the block outputs the actual value of the input
signal.

The IC block is useful for providing an initial guess for the algebraic state
variables in a loop. For more information, see Algebraic Loop Concepts.

### Behavior for Nonzero Sample Time Offset

If an IC block has a nonzero sample time offset
(`toffset`), the IC
block outputs its initial value at time `t`,

```
t = n * tperiod + toffset
```

where `n` is the smallest integer such that `t ≥
tstart`.

That is, the IC block outputs its initial value the first-time blocks with
sample time `[tperiod,
toffset]` execute, which can be after
`tstart`.
