---
type: simulink-block
title: 'Backlash'
family: 'libsb2sl'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'DYN'
documentation_page: 'backlash'
documentation_source_path: 'slref/backlash.html'
language: en
---

# Backlash

## Ports

### Input

### **Port\_1** — Input signal scalar | vector

Input signal to the backlash algorithm. The value of this signal is
either in the deadband or engaging the output in a positive or negative
direction.

**Data Types:** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal after the backlash algorithm is applied to the input
signal. When the input is in the deadband, then the output remains
unchanged. If the input is engaged with the output, then the output
changes an equal amount as the input.

**Data Types:** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **Deadband width** — Specify the width of the deadband `1` (default) | scalar | vector

Specify the size of the deadband zone centered on the output value. When
the input signal is inside the deadband, then a change in input does not
cause a change in output. When the input signal is outside of the deadband,
then the output changes an equal amount as the input.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BacklashWidth` |
| **Type**: character vector |
| **Values**: real scalar or vector |
| **Default**: `'1'` |

### **Initial output** — Specify the initial output value 0 (default) | scalar | vector

Specify the initial center of the deadband zone. If the initial input
value is in the deadband zone, then the output value is equal to
**Initial output**. If the initial input value is
outside of the deadband zone, then the output value is **Initial
output** plus or minus half of the deadzone width.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InitialOutput` |
| **Type**: character vector |
| **Values**: real scalar or vector |
| **Default**: `'0'` |

### **Input processing** — Specify sample- or frame-based processing `Elements as channels (sample based)` (default) | `Columns as channels (frame based)`

Specify whether the block performs sample- or frame-based processing:

- `Columns as channels (frame based)` — Treat
  each column of the input as a separate channel (frame-based processing).

  **Note**

  Frame-based processing requires a DSP System Toolbox™ license.

  For more information, see Sample- and Frame-Based Concepts (DSP System Toolbox).
- `Elements as channels (sample based)` — Treat
  each element of the input as a separate channel (sample-based
  processing).

Use **Input processing** to specify whether the block performs
sample- or frame-based processing. For more information about these two processing
modes, see Sample- and Frame-Based Concepts (DSP System Toolbox).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InputProcessing` |
| **Type**: character vector |
| **Values**: `'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **Default**: `'Elements as channels (sample based)'` |

### **Enable zero-crossing detection** — Enable zero-crossing detection `on` (default) | `off`

Select to enable zero-crossing detection. For more information, see Zero-Crossing Detection.

This block supports zero-crossing detection only in simulations
that use a variable-step solver. When you use a fixed-step solver for simulation, the software
does not detect or locate zero crossings for this block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroCross` |
| **Type**: character vector | string |
| **Values**: `'off'` | `'on'` |
| **Default**: `'on'` |

## Libraries

Simulink / Discontinuities HDL Coder / Discontinuities

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on `memcpy` or `memset`
function (`string.h`) in certain conditions.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

The **Deadband width** and **Initial
output** parameters support only scalar values.

## Version History

**Introduced before R2006a**

## Description

Model behavior of system with play

The Backlash block implements a system in which a change in input causes an equal
change in output, except when the input changes direction. When the input changes
direction, the initial change in input has no effect on the output. The amount of
side-to-side play in the system is referred to as the *deadband*. The
deadband is centered about the output. This figure shows an initial state, with the
default deadband width of 1 and initial output of 0.

A system with play can be in one of three modes.

| Mode | Input | Output |
| --- | --- | --- |
| Disengaged | Inside deadband zone. | Remains constant. |
| Engaged-positive direction | Outside deadband zone and increasing. | Equals input *minus* half of deadband width. |
| Engaged-negative direction | Outside deadband zone and decreasing. | Equals input *plus* half of deadband width. |

The **Initial output** parameter value defines the
initial center of the deadband zone.

This table shows output values when initial conditions are: **Deadband
width** = `2` and **Initial output** =
`5`.

| Output Value | Condition |
| --- | --- |
| 5 | 4 <= input <= 6 |
| input + 1 | input < 4 |
| input - 1 | input > 6 |

For example, you can use the Backlash block to model the meshing of two gears. The
input and output are both shafts with a gear on one end, and the input shaft drives the
output shaft. Extra space between the gear teeth introduces *play*.
The width of this spacing is the **Deadband width**
parameter. If the system is disengaged initially, the **Initial
output** parameter defines the output.

These figures illustrate operation when the initial input is within the deadband and
the system begins in disengaged mode.

When the input increases and reaches the end of the deadband, it engages the output.
The output remains at its previous value.

After the input engages the output, the output changes by the same amount as the
input.

If the input reverses direction, it disengages from the output. The output remains
constant until the input reaches the end of the deadband and engages again.
