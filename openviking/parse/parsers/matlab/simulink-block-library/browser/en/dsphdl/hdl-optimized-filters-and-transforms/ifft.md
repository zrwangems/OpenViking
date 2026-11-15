---
type: simulink-block
title: 'IFFT'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized Filters and Transforms'
documentation_page: 'ifft'
documentation_source_path: 'ref/ifft.html'
language: en
---

# IFFT

## Ports

### Input

### **data** — Input data scalar or column vector of real or complex values

Input data, specified as a scalar or column vector of real or complex values.
Vector input is supported with the `Streaming Radix 2^2`
architecture, and not supported with variable FFT size. The vector size must be a
power of 2, in the range from 1 to 64, and less than or equal to the FFT
length.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `fixed point` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `single` | `double`
**Complex Number Support:** Yes

### **valid** — Indicates valid input data scalar

Control signal that indicates if the input data is valid. When
**valid** is `1` (`true`), the
block captures the values from the input **data** port. When
**valid** is `0` (`false`), the
block ignores the values from the input **data** port.

When you set the **Architecture** parameter to `Burst
Radix 2`, or set the **FFT length source** parameter
to `Input port`, you must apply input data only when the
**ready** backpressure signal is `1`
(`true`). The block ignores the input **data** and
**valid** signals when **ready** is
`0` (`false`).

**Data Types:** `Boolean`

### **log2FFTLen** — Log2 of the FFT length scalar

*Since R2025a*

Provide the FFT size as
`log2(FFTLength)`. For
example, if the FFT length is 32, specify `5` at the port. For HDL
code generation, the FFT length must be a power of 2 between
22 and 216, so the port value
must be in the range 2 to 16. If the value is less than 2, the block uses an FFT
length of 4. If the value is greater than 16, the block uses an FFT length of
216.

To notify the block of the new FFT length, set **loadFFTLen** to
`1` (`true`) for at least one cycle with a new
value on **log2FFTLen**.

When you use variable FFT length, your input data must comply with the
**ready** backpressure signal. You can specify a new FFT length
while a frame is processing. The block sets **ready** to
`0` (`false`) while it finishes the current frame,
then sets **ready** to `1` (`true`)
to indicate it is ready for the next frame. The block uses the new FFT length for the
next input frame. If you set **loadFFTLen** to `1`
(`true`) when no frame is processing, the block sets
**ready** to `0` (`false`) for
four cycles while it updates internal logic.

#### Dependencies

To enable this port, set the **FFT length source** parameter to
`Input port`.

**Data Types:** `fixdt(0,M,0) where 1<M<6`

### **loadFFTLen** — Indicates valid FFT size scalar

*Since R2025a*

Control signal that indicates if the input FFT size is valid. When
**loadFFTLen** is `1` (`true`),
the block captures the value from the input **log2FFTLen** port. When
**loadFFTLen** is `0` (`false`),
the block ignores the value from the input **log2FFTLen**
port.

#### Dependencies

To enable this port, set the **FFT length source** parameter to
`Input port`.

**Data Types:** `Boolean`

### **reset** — Clears internal states scalar

Control signal that clears internal states. When **reset** is
`1` (`true`), the block stops the current
calculation and clears internal states. When the **reset** is
`0` (`false`) and the input
**valid** is `1` (`true`), the
block captures data for processing.

For more reset considerations, see the Reset Signal section on the
Hardware Control Signals page.

#### Dependencies

To enable this port, on the **Control Ports** tab, select the
**Enable reset input port** parameter.

**Data Types:** `Boolean`
### Output

### **data** — Frequency channel output data scalar or column vector of real or complex values

Output data, returned as a scalar or column vector of real or complex values.
When input is fixed-point data type and scaling is enabled, the output data type
is the same as the input data type. When the input is integer type and scaling is
enabled, the output is fixed-point type with the same word length as the input
integer. The output order is bit-reversed by default. If scaling is disabled, the
output word length increases to avoid overflow. For more
information, see the **Divide butterfly outputs by two**
parameter.

**Data Types:** `fixed point` | `double` | `single`
**Complex Number Support:** Yes

### **valid** — Indicates valid output data scalar

Control signal that indicates if the output data
is valid. When **valid** is
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
(`false`), the block ignores any input data in the next time
step.

For a waveform that shows this protocol, see the timing diagrams in the Control Signals
section.

#### Dependencies

To enable this port, set the **Architecture** parameter to
`Burst Radix 2`, or with
**Architecture** set to `Streaming Radix
2^2`, set the **FFT length source** parameter to
`Input port`.

**Data Types:** `Boolean`

### **start** — Indicates first valid cycle of output frame scalar

Control signal that indicates the first valid cycle of the output frame. When
**start** is `1` (`true`), the
block returns the first valid sample of the frame on the output
**data** port.

#### Dependencies

To enable this port, on the **Control Ports** tab, select the
**Enable start output port** parameter.

**Data Types:** `Boolean`

### **end** — Indicates last valid cycle of output frame scalar

Control signal that indicates the last valid cycle of the output frame. When
**end** is `1` (`true`), the
block returns the last valid sample of the frame on the output
**data** port.

#### Dependencies

To enable this port, on the **Control Ports** tab, select the
**Enable end output port** parameter.

**Data Types:** `Boolean`

## Parameters

### Main

### **Architecture** — Hardware implementation `Streaming Radix 2^2` (default) | `Burst Radix 2`

Specify the hardware implementation for the IFFT.

- `Streaming Radix 2^2` — Low-latency
  architecture. This architecture supports GSPS throughput when using vector input.
  Since R2025a, this architecture supports variable FFT length. When you use
  variable FFT length, your input data must comply with the
  **ready** backpressure signal.
- `Burst Radix 2` — Minimum resource
  architecture. This architecture does not support vector input. When you use this
  architecture, your input data must comply with the **ready**
  backpressure signal. This architecture supports only fixed FFT lengths.

For more details about these architectures, see Algorithms.

### **FFT length source** — Source of FFT length `Property` (default) | `Input port`

*Since R2025a*

You can enter a constant FFT length as a parameter or provide time-varying FFT
length by using an input port. When you select `Input port`,
the **log2FFTLen**, **loadFFTLen**, and
**ready** ports appear on the block.

#### Dependencies

This parameter is only available when you set **Architecture**
to `Streaming Radix 2^2`.

When you select `Input port`, the **Output in
bit-reversed order** and **Input in bit-reversed order**
parameters are disabled. The block uses natural input order and bit-reversed output
order.

### **FFT length** — Number of data points used for one FFT calculation `1024` (default)

Specify the number of data points used for one IFFT calculation. For HDL code
generation, the FFT length must be a power of 2 between 22
and 216.

#### Dependencies

This parameter is available when you set **Architecture** to
`Burst Radix 2` or you set the **FFT length
source** parameter to `Property`.

### **Maximum FFT length** — Highest FFT length expected from the input port `1024` (default)

*Since R2025a*

Specify the maximum number of data points used for one FFT calculation. This
parameter can help limit the hardware resources needed for a variable-size FFT design.
For HDL code generation, the FFT length must be a power of 2 between
23 to 216.

If you provide an input frame after reset without setting the FFT length from the
port, the block uses the **Maximum FFT length** parameter
value.

#### Dependencies

This parameter is available when you set the **FFT length
source** parameter to `Input port`.

### **Complex multiplication** — Hardware implementation of complex multipliers `Use 4 multipliers and 2 adders` (default) | `Use 3 multipliers and 5 adders`

Specify the hardware implementation for complex multipliers. Each multiplication
is implemented either with `Use 4 multipliers and 2 adders`
or with `Use 3 multipliers and 5 adders`. Depending on your
synthesis tool and target device, one option may be faster or smaller.

### **Output in bit-reversed order** — Order of output data on (default) | off

When you select this check box, the output elements are bit-reversed relative to
the input order. To return output elements in linear order, clear this check
box.

The IFFT algorithm calculates output in the reverse order to the input. If you
specify the output to be in the same order as the input, the algorithm performs an
extra reversal operation. For more information, see Linear and Bit-Reversed Output Order.

#### Dependencies

When you set the **FFT length source** parameter to
`Input port`, the **Output in bit-reversed
order** and **Input in bit-reversed order** parameters
are disabled. The block uses natural input order and bit-reversed output order.

### **Input in bit-reversed order** — Expected order of input data off (default) | on

When you select this check box, the block expects input data in bit-reversed
order. By default, the check box is cleared and the input is expected in linear
order.

The IFFT algorithm calculates output in the reverse order to the input. If you
specify the output to be in the same order as the input, the algorithm performs an
extra reversal operation. For more information, see Linear and Bit-Reversed Output Order.

#### Dependencies

When you set the **FFT length source** parameter to
`Input port`, the **Output in bit-reversed
order** and **Input in bit-reversed order** parameters
are disabled. The block uses natural input order and bit-reversed output order.

### **Divide butterfly outputs by two** — FFT scaling on (default) | off

When you select this parameter, the IFFT implements an overall
1/*FFTLength* scale factor by dividing the output of each butterfly
multiplication by two. This adjustment keeps the output of the IFFT in the same
amplitude range as its input. If you disable scaling, the block avoids overflow by
increasing the word length by 1 bit after each butterfly multiplication. The bit
growth is the same for both architectures.

### Data Types

### **Rounding Method** — Rounding mode for internal fixed-point calculations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

Rounding mode used for internal fixed-point calculations. When the input is any
integer or fixed-point data type, this block uses fixed-point arithmetic for internal
calculations. This option does not apply when the input data is
`single` or `double` type. Rounding applies to
twiddle-factor multiplication and scaling operations. For more information about
rounding modes, see Rounding Modes.

### Control Ports

### **Enable reset input port** — Optional reset signal off (default) | on

Enable the input **reset** port on the block.

### **Enable start output port** — Optional control signal indicating start of data off (default) | on

Enable the output **start** port on the block. This output signal
indicates the first sample of a frame of output data.

### **Enable end output port** — Optional control signal indicating end of data off (default) | on

Enable the output **end** port on the block. This output signal
indicates the last sample of a frame of output data.

## Libraries

DSP HDL Toolbox / Transforms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink accelerator and rapid accelerator modes and for DPI component generation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

- You cannot generate HDL code for this block inside an Enabled Subsystem (Simulink).

## Version History

**Introduced in R2014a**

### R2025a: Variable FFT length

You can now specify time-varying FFT length by using an input port. This feature is
supported only when you set **Architecture** to `Streaming
Radix 2^2` and you use scalar input data.

Set **FFT length source** parameter to `Input
port`, and then specify the FFT length at the **log2FFTLen**
port as `log2(FFTLength)`. For
example, if the FFT length is 32, specify `5` at the port. Set the
**loadFFTLen** port to `1` (`true`) for
at least one cycle to capture the value from the input **log2FFTLen**
port.

When you use variable FFT length, you must send input data only when the
**ready** backpressure signal is `1`
(`true`). The block sets the **ready** signal to
`0` (`false`) if a new FFT length is supplied while
processing a frame of data. The block sets the **ready** signal to
`1` (`true`) when it has completed a frame of output
data and has updated the FFT length for the next input frame.

To limit the hardware resources used in the variable-sized FFT implementation, set the
**Maximum FFT length** parameter to your expected maximum input size.

### R2022a: Moved to DSP HDL Toolbox from DSP System Toolbox

Before R2022a, this block was named IFFT HDL Optimized and was included
in the DSP System Toolbox™
**DSP System Toolbox HDL Support** library.

### R2022a: FFT length of 4

You can now set the FFT length to 4 (22). In previous
releases the FFT length had to be a power of 2 from 8 (23) to
216.

## Description

Compute inverse fast Fourier transform (IFFT)

The IFFT block provides two architectures that implement the algorithm for
FPGA and ASIC applications. You can select an architecture that optimizes for either
throughput or area.

- `Streaming Radix 2^2` — Use this architecture for
  high-throughput applications. This architecture supports scalar or vector input data. You
  can achieve gigasamples-per-second (GSPS) throughput, also called super sample rates,
  using vector input. Since 2025a, this architecture also supports specifying the FFT size
  by using an input port, when you use scalar input data.
- `Burst Radix 2` — Use this architecture for a minimum
  resource implementation, especially with large fast-Fourier-transform (FFT) sizes. Your
  system must be able to tolerate bursty data and higher latency. This architecture supports
  only scalar input data.

The block accepts real or complex data, provides hardware-friendly control signals, and
optional output frame control signals.

**Note**

You can also generate HDL code for this hardware-optimized algorithm, without creating a
Simulink® model, by using the DSP HDL IP Designer app. The app
provides the same interface and configuration options as the Simulink block.
