---
type: simulink-block
title: 'Tapped Delay Enabled Synchronous'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'tappeddelayenabledsynchronous'
documentation_source_path: 'ref/tappeddelayenabledsynchronous.html'
language: en
---

# Tapped Delay Enabled Synchronous

## Ports

### Input

### **u** — Input signal scalar

Input signal to delay.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

### **E** — Enable signal `Scalar`

The block accepts the Enable signal of the data types listed below. For more
information, see Data Types Supported by Simulink.

When the Enable signal is false, the state and output signal hold the previous
value. The Enable signal is true when `E` input is not zero and false
when `E` input is zero.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### Output

### **y** — Delayed versions of input signal scalar | vector

All versions of the delayed input signal. Use the
**Order output vector starting with** parameter to specify the
order of delayed signals in the output vector.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### **Initial condition** — Initial output `0.0` (default) | scalar

Specify the initial output of the simulation. The **Initial
condition** parameter is converted from a double to the input data type
offline using round-to-nearest and saturation.

#### Limitations

The initial condition of this block cannot be `inf` or
`NaN`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `vinit` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0.0'` |

### **Sample time** — Time between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

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

A value of `-1` instructs the block to inherit the number of delays
by backpropagation. Each delay is equivalent to the z-1
discrete-time operator, which the Unit Delay block represents.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumDelays` |
| **Type:** character vector |
| **Values:** positive scalar | `-1` (inherited) |
| **Default:** `'4'` |

### **Order output vector starting with** — Order of output `Oldest` (default) | `Newest`

Specify whether to output the oldest delay version first, or the newest delay
version first.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DelayOrder` |
| **Type:** character vector |
| **Values:** `'Oldest' | 'Newest'` |
| **Default:** `'Oldest'` |

### **Include current input in output vector** — Include current input in output vector `off` (default) | `on`

Select this check box to include the current input in the output vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `includeCurrent` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

## Libraries

HDL Coder / Discrete

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder provides additional configuration options that
affect HDL implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline. |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline. |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline. |
| **ResetType** | Suppress reset logic generation. The default is `default`, which generates reset logic. See also ResetType. |

**Complex Data Support**

This block supports code generation for complex signals.

## Version History

**Introduced in R2023a**

## Description

Delay scalar signal multiple sample periods and output all delayed versions when external Enable signal is true

The Tapped Delay Enabled Synchronous block delays an input by the specified
number of sample periods. The block returns output signal for each delay when the external
Enable signal **E** is true.

For example, when you specify **Number of delays** as
`4` and **Order output starting with** as
`Oldest`, the block returns four signals, the first delayed by four
sample periods, the second delayed by three, and so on. Use this block to discretize a signal
in time domain or resample a signal.

**Output Vector Order**

The block accepts one scalar input and generates an output vector that contains data for
each incremental delay. Specify the order of the delayed signals in the output vector with the
**Order output vector starting with** parameter:

- `Oldest` orders the output vector starting with the oldest
  delay version and ending with the newest delay version.
- `Newest` orders the output vector starting with the newest
  delay version and ending with the oldest delay version.

Specify the output vector for the first sampling period with the **Initial
condition** parameter. Careful selection of this parameter can mitigate unwanted
output behavior.

**Synchronous State Control**

The block uses synchronous state control semantics. When you use this block in your model
and generate HDL code by using HDL Coder™, your model generates cleaner HDL code and uses fewer hardware resources due to
the `Synchronous` behavior of the block.
