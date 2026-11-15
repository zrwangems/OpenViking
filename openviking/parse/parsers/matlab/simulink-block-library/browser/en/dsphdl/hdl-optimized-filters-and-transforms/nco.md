---
type: simulink-block
title: 'NCO'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized Filters and Transforms'
documentation_page: 'nco'
documentation_source_path: 'ref/nco.html'
language: en
---

# NCO

## Ports

### Input

### **inc** — Phase increment scalar integer

Phase increment, specified as a scalar integer. The block casts this
value to match the accumulator word length.

`double` and `single` data types are
supported for simulation but not for HDL code generation.

#### Dependencies

To enable this port, set the **Phase increment
source** parameter to `Input
port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixdt([],N,0)`

### **offset** — Phase offset scalar integer

Phase offset, specified as a scalar integer.

`double` and `single` data types are
supported for simulation but not for HDL code generation.

#### Dependencies

To enable this port, set the **Phase offset
source** parameter to `Input
port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixdt([],N,0)`

### **dither** — Dither integer | column vector of integers

Dither, specified as an integer or a column vector of integers. The
length of the vector must equal the **Samples per
frame** parameter value.

`double` and `single` data types are
supported for simulation but not for HDL code generation.

#### Dependencies

To enable this port, set the **Dither source**
parameter to `Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixdt([],N,0)`

### **valid** — Control signal that enables NCO operation scalar

Control signal that enables NCO operation, specified as a Boolean
scalar. When this signal is `1`, the block increments
the phase and captures any input values. When this signal is
`0`, the block holds the phase accumulator and
ignores any input values.

When the **Samples per frame** parameter is greater
than `1`, this value enables processing of
**Samples per frame** samples.

**Data Types:** `Boolean`

### **reset accum** — Resets the accumulator scalar

Control signal that resets the accumulator, specified as a Boolean
scalar. When this signal is `1`, the block resets the
accumulator to its initial value. This signal does not reset the output
samples in the pipeline.

#### Dependencies

To enable this port, select the **Enable accumulator reset
input port** parameter.

**Data Types:** `Boolean`
### Output

### **sin, cos, exp** — Generated waveform scalar | column vector

Generated waveform, returned as a scalar or as a column vector with
length equal to the **Samples per frame** parameter
value. The output can be a single port that returns
**sin** or **cos** values, a
single port that returns **exp** values representing
`cosine + j*sine`, or two ports that return
**sin** and **cos** values,
respectively.

When all input values are fixed-point type or all input ports are
disabled, the block determines the output type using the
**Output data type** parameter. When any input
value is floating-point type, the block ignores the **Output
data type** parameter. In this case, the block returns the
waveform as floating-point values. Floating-point data types are
supported for simulation but not for HDL code generation.

#### Dependencies

By default, this output port is a sine wave,
**sin**. The port label and format changes
based on the **Type of output signal**
parameter.

### **phase** — Current phase of NCO scalar | column vector

Current phase of NCO, returned as a scalar or as a column vector with
length equal to the **Samples per frame** parameter
value. The phase is the output of the quantized accumulator with offset
and increment applied. If quantization is disabled, this port returns
the output of the accumulator with offset and increment applied. The
values are of type `fixdt(1,N,0)`, where
`N` is the **Number of quantizer
accumulator bits** parameter value. If quantization is
disabled, then `N` is the **Accumulator Word
length** parameter value.

If any input value is floating-point type, the block returns the
**phase** as a floating-point value. Floating-point
data types are supported for simulation but not for HDL code
generation.

#### Dependencies

To enable this port, select the **Enable phase
port** parameter.

**Data Types:** `single` | `double` | `fixdt(1,N,0)`

### **valid** — Indicates validity of output data scalar

Control signal that indicates validity of output data, returned as a
Boolean scalar. When output **valid** is
`1`, the values on the **sin**,
**cos**, **exp**, and
**phase** ports are valid. When output
**valid** is `0`, the values on
the output ports are not valid.

When the **Samples per frame** parameter is greater
than `1`, this signal indicates the validity of all
elements in the output vector.

**Data Types:** `Boolean`

## Parameters

### Main

**Note**

This block supports `double` and `single`
input for simulation but not for HDL code generation. When all input values are
fixed-point type or all input ports are disabled, the block determines the
output type using the **Output data type** parameter. When any
input value is floating-point type, the block ignores the **Output data
type** parameter. In this case, the block returns the waveform and
optional **phase** as floating-point values.

To use the Fixed-Point Designer™ data type override feature, you can obtain a
`double` output value by applying `double`
input data to one of the optional ports.

### **Phase increment source** — Source of phase increment `Input port` (default) | `Property`

You can set the phase increment with an input port or by entering a
value for the parameter. If you select
`Property`, the **Phase
increment** parameter appears for you to enter a value. If
you select `Input port`, the
**inc** port appears on the block.

### **Phase increment** — Phase increment for generated waveform `100` (default) | integer

Phase increment for the generated the waveform, specified as an
integer. The block casts this value to match the accumulator word
length.

#### Dependencies

To enable this parameter, set the **Phase increment
source** parameter to
`Property`.

### **Phase offset source** — Source of phase offset `Input port` (default) | `Property`

You can set the phase offset with an input port or by entering a value
for the parameter. If you select `Property`,
the **Phase offset** parameter appears for you to enter
a value. If you select `Input port`, the
**offset** port appears on the block.

### **Phase offset** — Phase offset for generated waveform `0` (default) | integer

Phase offset for the generated waveform, specified as an
integer.

#### Dependencies

To enable this parameter, set the **Phase offset
source** parameter to
`Property`.

### **Dither source** — Source of number of dither bits `Property` (default) | `Input port` | `None`

You can set the dither from an input port or from a parameter. If you
select `Property`, the **Number of
dither bits** parameter appears. If you select
`Input port`, a port appears on the block.
If you select `None`, the block does not add
dither.

### **Number of dither bits** — Bits used to express dither `4` (default) | positive integer

Number of dither bits, specified as a positive integer.

#### Dependencies

To enable this parameter, set the **Dither
source** parameter to
`Property`.

### **Samples per frame** — Vector size for frame-based input and output `1` (default) | positive integer

When you set this value to `1`, the block has scalar
input and output. When this value is greater than `1`,
the **dither** port expects a column vector of length
**Samples per frame** and the
**sin**, **cos**,
**exp**, and **phase** ports
return column vectors of length **Samples per
frame**.

### **Enable look up table compression method** — Compress the lookup table `off` (default) | `on`

By default, the block implements a noncompressed lookup table, and the
output of this block matches the output of the NCO block. When you enable
this option, the block implements a compressed lookup table. The
Sunderland compression method reduces the size of the lookup table,
losing less than one LSB of precision. The spurious free dynamic range
(SFDR) is empirically 1–3 dB lower than the noncompressed case. The
hardware savings of the compressed lookup table allow room to improve
performance by increasing the word length of the accumulator and the
number of quantize bits. For detail of the compression method, see Algorithms.

### **Enable accumulator reset input port** — Enable reset control signal `off` (default) | `on`

Select this parameter to enable the **reset accum**
port. When **reset accum** is `1`, the
block resets the accumulator to its initial value.

### **Type of output signal** — Format of output waveform `Sine` (default) | `Cosine` | `Complex exponential` | `Sine and cosine`

If you select `Sine` or
`Cosine`, the block shows the applicable
port, **sin** or **cos**. If you
select `Complex exponential`, the output is of
the form `cosine + j*sine` and the port is labeled
**exp**. If you select `Sine and
cosine`, the block shows two ports,
**sin** and **cos**.

When you set the **Type of output signal** parameter
to `Complex exponential` or `Sine
and cosine`, the block implements a 1/8 sine wave
lookup table for each of the sine and cosine parts of the waveform, and
uses control logic to select and invert the values to generate both sine
and cosine waveforms. This optimization means that dual output mode uses
similar hardware resources compared to single output mode.

### **Enable phase port** — Output current phase `off` (default) | `on`

Select this parameter to return the current NCO phase on the
**phase** port. The phase is the output of the
quantized accumulator, with offset and increment applied. If
quantization is disabled, this port returns the output of the
accumulator, with offset and increment applied.

### Data Types

### **Rounding Mode** — Rounding mode for fixed-point operations `Floor` (default)

Rounding
mode for fixed-point operations. **Rounding
Mode** is a read-only parameter with value
`Floor`.

### **Overflow mode** — Overflow mode for fixed-point operations `Wrap` (default)

Overflow
mode for fixed-point operations. **Overflow
mode** is a read-only parameter. Fixed-point numbers wrap
around on overflow.

### **Accumulator Data Type** — Accumulator data type `Binary point scaling` (default)

Accumulator data type description. This parameter is read-only, with
value `Binary point scaling`. The block defines
the fixed-point data type using the **Accumulator
Signed**, **Accumulator Word length**, and
**Accumulator Fraction length** parameters.

### **Accumulator Signed** — Signed or unsigned accumulator data format `Signed` (default)

This parameter is read-only. All output is signed format.

### **Accumulator Word length** — Accumulator word length `16` (default) | integer

Units are in bits. This value must include the sign bit.

If you clear the **Quantize phase** parameter, then
**Accumulator word length** determines the LUT
size. For HDL code generation, the LUT size must be between 2 and
217 entries. When you select
**Enable look up table compression method**, this
parameter must be an integer in the range [5,21]. When you clear
**Enable look up table compression method**, this
parameter must be an integer in the range [3,19]. For more information
on how this parameter affects the LUT size, see the Algorithms section.

When you select the **Quantize phase** parameter,
there is no limit to the **Accumulator word length**
parameter value.

### **Accumulator Fraction length** — Accumulator fraction length `0` (default) | integer

This parameter is read-only. The accumulator fraction length is zero
bits.

The accumulator operates on integers. If the phase increment is
`fixdt` type with a fractional part, the block
returns an error.

### **Quantize phase** — Quantize accumulated phase `off` (default) | `on`

When you select **Quantize phase**, the block
quantizes the result of the phase accumulator to a fixed bit-width. The
block uses this quantized value to select a waveform value from the
lookup table. Quantizing the output of the phase accumulator enables you
to reduce the lookup table size without lowering the frequency
resolution. Select the size of the lookup table by using the
**Number of quantizer accumulator bits** parameter.

When you clear **Quantize phase**, the block uses the
full accumulator value as the address of the lookup table.

### **Number of quantizer accumulator bits** — Number of quantizer accumulator bits `12` (default) | integer

Number of quantizer accumulator bits, specified as an integer scalar
less than the accumulator word length. For HDL code generation, this
parameter value must result in a LUT size between 2 and
217 entries. When you select
**Enable look up table compression method**, this
parameter must be an integer in the range [5,21]. When you clear
**Enable look up table compression method**, this
parameter must be an integer in the range [3,19]. For more information
on how this parameter affects the LUT size, see the Algorithms section.

#### Dependencies

To enable this parameter, select the **Quantize
phase** parameter.

### **Output Data Type** — Output data type `Binary point scaling` (default) | `double` | `single`

Specify the data type for the **sin**,
**cos**, and **exp** ports. This
parameter is ignored if any input is of floating-point type. In that
case, the output data type is floating-point.

If you select `Binary point scaling`, the
block defines the fixed-point data type using the **Output
Signed**, **Output Word length**, and
**Output Fraction length** parameters.

### **Output Signed** — Signed or unsigned output data format `Signed` (default)

This parameter is read-only. All output is signed format.

### **Output Word length** — Output word length `16` (default) | integer

Units are in bits. This value must include the sign bit.

### **Output Fraction length** — Output fraction length `14` (default) | integer

Units are in bits.

## Libraries

DSP HDL Toolbox / Signal Operations DSP HDL Toolbox / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink accelerator and rapid accelerator modes and for DPI component generation.

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

- When you set **Dither source** to
  `Property`, the block adds random dither
  every cycle. If you generate a validation model with these settings, a
  warning is displayed. Random generation of the internal dither can cause
  mismatches between the models. You can increase the error margin for the
  validation comparison to account for the difference. You can also
  disable dither or set **Dither source** to
  `Input port` to avoid this issue.
- You cannot use the NCO block inside a Resettable Synchronous
  Subsystem (HDL Coder).

## Version History

**Introduced in R2013a**

### R2022a: Moved to DSP HDL Toolbox from DSP System Toolbox

Before R2022a, this block was named NCO HDL Optimized and was
included in the DSP System Toolbox™
**DSP System Toolbox HDL Support** library.

### R2022a: Resource optimization for dual output mode

When you set the **Type of output signal** parameter
to `Complex exponential` or `Sine and
cosine`, this block implements a 1/8 sine wave lookup table for
each of the sine and cosine parts of the waveform, and uses control logic to select
and invert the values to generate both sine and cosine waveforms. This optimization
means that dual output mode uses hardware resources similar to single output mode.
In previous releases, the block implemented one lookup table for each output
waveform.

### R2020a: Valid input port required

In previous releases, the input **validIn** port was optional. It
is now required and renamed **valid**. If you are using no other
input ports, the block uses the **valid** signal as an enable
signal.

### R2020a: Phase quantization for floating-point input

The output waveform returned from floating-point input values has changed. The
output waveform now matches the waveform returned from the same input values
specified in fixed-point types.

Before R2020a, when using floating-point input types, the block did not quantize
the phase internally. The block expected floating-point phase increment and phase
offset inputs specified in radians. Now, the block quantizes the phase internally,
and you must specify the input phase increment and offset in terms of the quantized
size, for both floating-point and fixed-point input types.

For example, before R2020a, for a floating-point HDL NCO to generate output
samples with a desired output frequency of
*F*0 and sample frequency of
*F*s, you had to specify the phase
increment as
2π(*F*0/*F*s)
and phase offset as π/2.

Starting in R2020a, you must specify the phase increment and phase offset in terms
of the quantized size, *N*. These input values are the same as the
input values you use with fixed-point types. Specify the phase increment as
(*F*0×2*N*)/*F*s
and the phase offset as (π/2)×2*N*/2π,
or 2*N*/4.

### R2020a: LUTRegisterResetType option removed

In previous releases, you could choose from two options for the
**LUTRegisterResetType** parameter on the **HDL Block
Properties** dialog box. The two options were
`default` and `none`. Starting
in R2020a, the block ignores the parameter setting and uses
`none` for this parameter value. This option does not
connect a reset signal to the LUT registers. This configuration enables the
synthesis tool to determine whether to implement the lookup tables with LUTs or
BRAM.

### R2020a: High-throughput interface

You can generate frame-based waveforms from the block. The block returns a vector
where each element represents a sample in time. Set the **Samples per
frame** parameter to the desired output vector size.

## Description

Generate real or complex sinusoidal signals

The NCO block generates real or complex sinusoidal signals, while
providing hardware-friendly control signals.

A numerically-controlled oscillator (NCO) accumulates a phase increment and uses the
quantized output of the accumulator as the index to a lookup table that contains the
sine wave values. The wrap around of the fixed-point accumulator and quantizer data
types provide periodicity of the sine wave, and quantization reduces the necessary size
of the table for a given frequency resolution.

High level architecture of an NCO

For an example of how to generate a sine wave using the NCO block, see
Generate Sine Wave.
For more information on configuration and implementation, refer to the Algorithms section.

The block also provides these features:

- Optional frame-based output.
- A lookup table compression option to reduce the lookup table size. This
  compression results in less than one LSB loss in precision. See Lookup Table Compression for
  more information.
- An optional input port for external dither.
- An optional reset port that resets the phase accumulator to its initial
  value.
- An optional output port for the current NCO phase.

**Note**

You can also generate HDL code for this hardware-optimized algorithm, without creating a
Simulink® model, by using the DSP HDL IP Designer app. The app
provides the same interface and configuration options as the Simulink block.
