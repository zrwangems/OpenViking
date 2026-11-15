---
type: simulink-block
title: 'Zero-Order Hold'
family: discrete
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'zeroorderhold'
language: en
---

# Zero-Order Hold

## Ports

### Input

### **Port\_1** — Input signal scalar | vector

Input signal that the block holds by one sample period.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal that is the input held by one sample period.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **Sample time (-1 for inherited)** — Discrete interval between sample time hits `-1` (default) | `scalar`

Specify the time interval between samples. To inherit the sample time, set this parameter
to `-1`. See Specify Sample Time for
more information.

Do not specify a continuous sample time (`0` or
`[0,0]`). This block supports only discrete sample times.
When this parameter is `-1`, the inherited sample time must
be discrete and not continuous.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `-1` (default) | positive scalar number |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/Zero-Order
Hold","SampleTime","0.1")` specifies a discrete sample
time of `0.1` for the Zero-Order
Hold block named `Zero-Order Hold` in
the model named `mdl`.

## Libraries

Simulink / Discrete HDL Coder / Discrete

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on `memcpy` or `memset`
functions (`strong.h`) under certain conditions.

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

**Complex Data Support**

This block supports code generation for complex signals.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Implement zero-order hold sample period

The Zero-Order Hold block holds its input for the sample period you
specify. If the input is a vector, the block holds all elements of the vector for the
same sample period.

You specify the time between samples with the **Sample time**
parameter. A setting of `-1` means the block inherits the
**Sample time**.

**Tip**

Do not use the Zero-Order Hold block to create a fast-to-slow transition between
blocks operating at different sample rates. Instead, use the Rate Transition block.

### Bus Support

The Zero-Order Hold block is a bus-capable block. The input can be a virtual or
nonvirtual bus signal. No block-specific restrictions exist. All signals in a
nonvirtual bus input to a Zero-Order Hold block must have the same sample time, even
if the elements of the associated bus object specify inherited sample times. You can
use a Rate Transition block to change the
sample time of an individual signal, or of all signals in a bus. See Modify Sample Times for Nonvirtual Buses and
Bus-Capable Blocks for more
information.

You can use an array of buses as an input signal to a Zero-Order Hold block. For
details about defining and using an array of buses, see Group Nonvirtual Buses in Arrays of Buses.

### Comparison with Similar Blocks

The Memory, Unit Delay, and Zero-Order Hold
blocks provide similar functionality but have different capabilities. Also, the purpose of
each block is different.

This table shows recommended usage for each block.

| Block | Purpose of the Block | Reference Examples |
| --- | --- | --- |
| Unit Delay | Implement a delay using a discrete sample time that you specify. The block accepts and outputs signals with a discrete sample time. | - Engine Timing Model with Closed Loop Control (Compression subsystem) |
| Memory | Implement a delay by one major integration time step. Ideally, the block accepts continuous (or fixed in minor time step) signals and outputs a signal that is fixed in minor time step. | - Building a Clutch Lock-Up Model (Friction Mode Logic/Lockup FSM subsystem) - Capture the Velocity of a Bouncing Ball with the Memory Block |
| Zero-Order Hold | Convert an input signal with a continuous sample time to an output signal with a discrete sample time. | - Developing the Apollo Lunar Module Digital Autopilot - Radar Tracking Using MATLAB Function Blocks |

Each block has the following capabilities.

| Capability | Memory | Unit Delay | Zero-Order Hold |
| --- | --- | --- | --- |
| Specification of initial condition | Yes | Yes | No, because the block output at time t = 0 must match the input value. |
| Specification of sample time | No, because the block can only inherit sample time from the driving block or the solver used for the entire model. | Yes | Yes |
| Support for frame-based signals | No | Yes | Yes |
| Support for state logging | No | Yes | No |
