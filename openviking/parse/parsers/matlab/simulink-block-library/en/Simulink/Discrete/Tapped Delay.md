---
type: simulink-block
title: 'Tapped Delay'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'tappeddelay'
documentation_source_path: 'slref/tappeddelay.html'
language: en
---

# Tapped Delay

## Ports

### Input

### **Port\_1** — Input signal scalar

Input signal to delay.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Delayed versions of input signal scalar | vector

All versions of the delayed input signal. Use the **Order
output vector starting with** parameter to specify the
order of delayed signals in the output vector.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### **Initial condition** — Initial output `0.0` (default) | scalar

Specify the initial output of the simulation. The **Initial
condition** parameter is converted from a double to the input
data type offline using round-to-nearest and saturation.

#### Limitations

The initial condition of this block cannot be `inf`
or `NaN`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `vinit` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0.0'` |

### **Sample time** — Time between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set
this parameter to `-1`. For more information, see Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `samptime` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'-1'` |

### **Number of delays** — Number of discrete-time operators `4` (default) | positive scalar | `-1` (for inherited)

Specify the number of discrete-time operators as a positive scalar, or
`-1` for inherited.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumDelays` |
| **Type:** character vector |
| **Values:** positive scalar | `-1` (inherited) |
| **Default:** `'4'` |

### **Order output vector starting with** — Order of output `Oldest` (default) | `Newest`

Specify whether to output the oldest delay version first, or the newest
delay version first.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DelayOrder` |
| **Type:** character vector |
| **Values:** `'Oldest' | 'Newest'` |
| **Default:** `'Oldest'` |

### **Include current input in output vector** — Include current input in output vector `off` (default) | `on`

Select this check box to include the current input in the output
vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `includeCurrent` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

## Libraries

Simulink / Discrete HDL Coder / Discrete

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
| **ResetType** | Suppress reset logic generation. The default is `default`, which generates reset logic. See also ResetType (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Delay scalar signal multiple sample periods and output all delayed versions

The Tapped Delay block delays an input by the specified number of sample
periods and provides an output signal for each delay. For example, when you specify
`4` for **Number of delays** and **Order
output starting with** is `Oldest`, the block
provides four outputs — the first delayed by four sample periods, the second delayed by
three, and so on. Use this block to discretize a signal in time or resample a signal at
a different rate.

The block accepts one scalar input and generates an output vector that contains data for
each incremental delay. Specify the order of the delayed signals in the output vector
with the **Order output vector starting with** parameter:

- `Oldest` orders the output vector starting with the oldest delay version and ending with the newest delay version.
- `Newest` orders the output vector starting with the newest delay version and ending with the oldest delay version.

Specify the output vector for the first sampling period with the **Initial
condition** parameter. Careful selection of this parameter can mitigate
unwanted output behavior.

Specify the time between samples with the **Sample time** parameter.
Specify the number of delays with the **Number of delays** parameter. A
value of `-1` instructs the block to inherit the number of delays by
backpropagation. Each delay is equivalent to the z-1
discrete-time operator, which the Unit Delay block represents.
