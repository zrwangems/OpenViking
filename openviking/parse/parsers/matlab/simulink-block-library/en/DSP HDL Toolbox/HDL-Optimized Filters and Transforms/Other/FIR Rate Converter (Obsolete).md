---
type: simulink-block
title: 'FIR Rate Converter (Obsolete)'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized Filters and Transforms / Other'
documentation_page: 'firrateconverterobsolete'
documentation_source_path: 'ref/firrateconverterobsolete.html'
language: en
---

# FIR Rate Converter (Obsolete)

## Ports

### Input

### **data** — Input data sample scalar | row vector

Input data sample, specified as a scalar, or as a row vector in which each element
represents an independent channel. The block accepts real or complex data.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **valid** — Indicates valid input data scalar

Control signal that indicates if the input data is valid. When
**valid** is `1` (`true`), the
block captures the values from the input **data** port. When
**valid** is `0` (`false`), the
block ignores the values from the input **data** port.

You can apply a valid data sample every `ceiling(L/M)` time
steps.

**Data Types:** `Boolean`

### **request** — Request control signal scalar

When the **request** port is `1`, and an output
data sample is available, on the next cycle the block returns that output data sample
on the output **data** port and sets the output
**valid** signal to `1`. When no new data is
available, the block sets the output **valid** signal to
`0`. When the **request** port is
`0`, the block holds available data until the
**request** port is set to `1`.

You can connect the **request** input port to the
**ready** output port of a downstream block.

**Data Types:** `Boolean`
### Output

### **data** — Output data sample scalar | row vector

Output data sample, returned as a scalar or a row vector in which each element
represents an independent channel.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **valid** — Indicates valid output data scalar

Control signal that indicates if the data from the output
**data** port is valid. When **valid** is
`1` (`true`), the block returns valid data from
the output **data** port. When **valid** is
`0` (`false`), the values from the output
**data** port are not valid.

**Data Types:** `Boolean`

### **ready** — Indicates block is ready for new input data scalar

Control signal that indicates that the block is ready for new input data sample on
the next cycle. When **ready** is `1`
(`true`), you can specify the **data**
and **valid**  inputs for the next time step. When
**ready** is `0`
(`false`), the block ignores any input data in the next time step.

You can connect the **ready** output port to the
**request** input port of an upstream block.

#### Dependencies

To enable this port, select the **Enable ready output port**
check box.

**Data Types:** `Boolean`

## Parameters

### Main

### **Interpolation factor** — Interpolation factor `3` (default) | positive integer

Specify a factor by which the block interpolates the input data sample.

### **Decimation factor** — Decimation factor `2` (default) | positive integer

Specify a factor by which the block decimates the input data sample.

### **FIR filter coefficients** — FIR filter coefficients `firpm(70, [0 0.28 0.32 1],[1 1 0 0])` (default) | row vector

Specify a row vector of coefficients in descending powers of
*z-1*.

**Note**

You can generate filter coefficients using Signal Processing Toolbox™ filter design functions (such as `fir1`). Design a
lowpass filter with normalized cutoff frequency no greater than
`min(1/L,1/M)`. The block initializes internal filter states to
zero.

### Data Types

### **Rounding mode** — Rounding mode for fixed-point operation `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

Select a rounding mode for fixed-point operations. For more information, see Rounding mode.

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

Specify whether overflows saturate or wrap.

- `off` — Overflows wrap to the appropriate value that data
  type can represent. For example, because 130 does not fit in a signed 8-bit
  integer, it wraps to -126.
- `on` — Overflows saturate to either the minimum or maximum
  value that data type can represent. For example, an overflow associated with a
  signed 8-bit integer can saturate to -128 or 127.

### **Coefficients** — FIR filter coefficients data type `fixdt(1,16,16)` (default)

FIR filter coefficients data type, specified as a
`fixdt(s,wl,fl)` object with `signedness`,
`word length`, and `fractional length`
properties.

### **Output** — Data type of output data sample `Inherit: Same word length as input` (default) | `Inherit via internal rule` | `fixdt(s,wl,fl)`

Specify the data type for the output data samples.

### Control Ports

### **Enable ready output port** — Option to enable ready control signal `off` (default) | `on`

Select this parameter to enable the **ready** port.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink® accelerator and rapid accelerator modes and for DPI component generation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

## Version History

**Introduced in R2015b**

### R2022a: Moved to DSP HDL Toolbox from DSP System Toolbox

Before R2022a, this block was named FIR Rate Conversion HDL Optimized and
was included in the DSP System Toolbox™
**DSP System Toolbox HDL Support** library.

### R2022a: Remove request port in future release

The **request** port on the FIR Rate Converter block is
no longer supported. Existing instances of the FIR Rate Converter block that
use the **request** port are forwarded to this block, which has a
nonoptional request port. This block will be removed in a future release.

Instead, use the FIR Rate Converter block without the
**request** port, and control the input data rate by using a FIFO outside
the block. See Control Data Rate Using Ready Signal.

### R2022a: One cycle latency between request and validOut

This block has a register on the **request** input port. This register
means there is one cycle latency between setting **request** to
`1` (`true`) and the block returning data on the
**dataOut** and **validOut** ports.

## Description

Upsample, filter, and downsample input signal (with request port)

The FIR Rate Converter block upsamples, filters, and downsamples input
signals. It is optimized for HDL code generation and operates on one sample of each channel at
a time. The block implements a polyphase architecture to avoid unnecessary arithmetic
operations and high intermediate sample rates.

High level rate converter architecture

The block upsamples the input signal by an integer factor of *L*, applies
it to a FIR filter, and downsamples the input signal by an integer factor of
*M*.

You can use the input and output control ports for pacing the flow of samples. In the
default configuration, the block uses input and output **valid** control
signals. The block has a **request** port to control the output rate. For
input flow control, you can enable a **ready** output signal.

Architecture diagram that shows the valid, ready, and request control signals

The **ready** output port indicates that the block can accept a new input
data sample on the next time step. When *L* ≥ *M*, you can
use the **ready** signal to achieve continuous output data samples. If you
apply a new input sample after each time the block returns **ready** signal
as `1`, the block returns a data output sample with the output
**valid** signal set to `1` on every time step.

When you disable the **ready** port, you can apply a valid data sample
only every `ceil(L/M)` time steps. For example, if:

- *L*/*M* = 4/5, then you can apply a new input
  sample on every time step.
- *L*/*M* = 3/2, then you can apply a new input
  sample on every other time step.

The block returns the next output sample one cycle after the **request**
signal is `1` and a valid output sample is available. When no new data is
available, block sets the output **valid** signal to
`0`.

You can connect the **request** input port to the
**ready** output port of a downstream block.
