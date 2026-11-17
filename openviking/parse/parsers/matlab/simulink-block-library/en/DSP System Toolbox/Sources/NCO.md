---
type: simulink-block
title: 'NCO'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'nco'
documentation_source_path: 'ref/nco.html'
language: en
---

# NCO

## Ports
```yaml
ports:
- name: inc
  summary: Phase increment scalar | vector
  direction: input
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: offset
  summary: Phase offset scalar | vector | matrix
  direction: input
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: sin
  summary: Sine output scalar | vector | matrix
  direction: output
  data_types: single | double | fixed point
- name: cos
  summary: Cosine output scalar | vector | matrix
  direction: output
  data_types: single | double | fixed point
- name: exp
  summary: Complex exponential scalar | vector | matrix
  direction: output
  data_types: single | double | fixed point
- name: Qerr
  summary: Phase quantization error scalar | vector | matrix
  direction: output
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **inc** — Phase increment scalar | vector

Phase increment signal, specified as a real-valued scalar or vector.
The input must have an integer data type, or a fixed-point data type
with zero fraction length. The dimensions of the phase increment signal
depend on how you choose to specify the **Phase
offset** parameter:

- When you specify the **Phase offset** on the
  block dialog box, the **Phase increment** must
  be a scalar or a vector with the same length as the
  **Phase offset** value. The block applies
  each element of the vector to a different channel, and therefore
  the vector length defines the number of output channels.
- When you specify the **Phase offset** via the
  an input port, the **offset** port treats each
  column of the input as an independent channel. The
  **Phase increment** length must equal the
  number of columns in the input to the
  **offset** port.

#### Dependencies

To enable this port, set **Phase increment
source** to `Input
port`.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **offset** — Phase offset scalar | vector | matrix

Phase offset signal, specified as a real-valued scalar, vector, or a
full matrix. The input must have an integer data type, or a fixed-point
data type with zero fraction length. The block treats each column of the
input to the offset port as an independent channel. The number of
channels in the phase offset must match the number of channels in the
data input. For each
frame of the input, the block can apply different phase offsets to each
sample and channel.

#### Dependencies

To enable this port, set **Phase offset source**
to `Input port`.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **sin** — Sine output scalar | vector | matrix

Sinusoidal output signal specified as a scalar, vector, or matrix. You
can specify the data type of the signal using the
**Output** data type parameter.

#### Dependencies

To enable this port, set **Output signal** to
`Sine` or `Sine and
cosine`.

**Data Types:** `single` | `double` | `fixed point`

### **cos** — Cosine output scalar | vector | matrix

Cosinusoidal output signal specified as a scalar, vector, or matrix. You can specify the
data type of the signal using the **Output Data Type**
parameter.

#### Dependencies

To enable this port, set **Output signal** to
`Cosine` or `Sine and
cosine`.

**Data Types:** `single` | `double` | `fixed point`

### **exp** — Complex exponential scalar | vector | matrix

Complex exponential output, specified as a scalar, vector, or matrix. You can specify
the data type of the signal using the **Output Data
Type** parameter.

#### Dependencies

To enable this port, set **Output signal** to
`Complex exponential`.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes

### **Qerr** — Phase quantization error scalar | vector | matrix

Phase quantization error specified as a scalar, vector, or
matrix.

#### Dependencies

To enable this port, select the **Show phase quantization
error port** check box.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## Parameters
```yaml
parameters:
- name: Phase increment source
  summary: Source of phase increment value Specify via dialog | Input port
  group: Main
- name: Phase increment
  summary: Phase increment value 100 (default) | scalar | vector
  group: Main
- name: Phase offset source
  summary: Source of phase offset Specify via dialog (default) | Input port
  group: Main
- name: Phase offset
  summary: Phase offset value 0 (default) | scalar | vector
  group: Main
- name: Add internal dither
  summary: Add internal dithering on (default) | off
  group: Main
- name: Number of dither bits
  summary: Number of dither bits 4 (default) | positive integer
  group: Main
- name: Quantize phase
  summary: Enable quantization of accumulated phase on (default) | off
  group: Main
- name: Number of quantized accumulator bits
  summary: Number of quantized accumulator bits 12 (default) | integer scalar
  group: Main
- name: Show phase quantization error port
  summary: Output quantization error off (default) | on
  group: Main
- name: Output signal
  summary: Output signal Sine (default) | Cosine | Complex exponential | Sine and cosine
  group: Main
- name: Sample time
  summary: Output sample period 1 (default) | positive scalar
  group: Main
- name: Samples per frame
  summary: Samples per frame 1 (default) | positive integer
  group: Main
- name: Rounding mode
  summary: 'Rounding method Read-only: Floor (default)'
  group: Data Types
- name: Overflow mode
  summary: 'Overflow method Read-only: Wrap (default)'
  group: Data Types
- name: Accumulator Word Length
  summary: Accumulator word length 16 (default) | integer from 2 to 128
  group: Data Types
- name: Output Data Type
  summary: Output data type double (default) | single | Binary point scaling
  group: Data Types
- name: Output Word Length
  summary: Output word length 16 (default) | integer from 2 to 128
  group: Data Types
- name: Output Fraction Length
  summary: Output fraction length 14 (default) | integer
  group: Data Types
- name: Number of data points for lookup table
  summary: Number of points in lookup table no default
  group: NCO Characterization
- name: Quarter wave sine lookup table size
  summary: Size of quarter wave sine lookup table no default
  group: NCO Characterization
- name: Theoretical spurious free dynamic range
  summary: Spurious free dynamic range no default
  group: NCO Characterization
- name: Frequency resolution
  summary: Frequency resolution no default
  group: NCO Characterization
```

### Main

#### Phase adder parameters

### **Phase increment source** — Source of phase increment value `Specify via dialog` | `Input port`

Choose how you specify the phase increment. The phase increment can
come from an input port or from the dialog box parameter.

- If you select `Input port`, the
  **inc** input port appears on the block
  icon.
- If you select `Specify via dialog`,
  the **Phase increment** parameter
  appears.

#### Dependencies

When the block comes from the Signal Operations library, the
default value of the **Phase increment Source**
parameter is `Input port`.

When the block comes from the Sources library, the default value
of the **Phase increment Source** parameter is
`Specify via dialog`.

### **Phase increment** — Phase increment value `100` (default) | scalar | vector

Specify the phase increment as an integer-valued scalar or vector.
Only integer data types, including fixed-point data types with zero
fraction length, are allowed. The dimensions of the phase increment
depend on those of the phase offset:

- When you specify the phase offset on the block dialog box, the
  phase increment must be a scalar or a vector with the same
  length as the phase offset. The block applies each element of
  the vector to a different channel, and therefore the vector
  length defines the number of output channels.
- When you specify the phase offset via an input port, the
  offset port treats each column of the input as an independent
  channel. The phase increment length must equal the number of
  columns in the input to the offset port.

#### Dependencies

To enable this parameter, set **Phase increment
source** to `Specify via
dialog`.

### **Phase offset source** — Source of phase offset `Specify via dialog` (default) | `Input port`

Choose how you specify the phase offset. The phase offset can come
from an input port or from the dialog box.

- If you select `Input port`, the
  **offset** port appears on the block
  icon.
- If you select `Specify via dialog`,
  the **Phase offset** parameter appears.

### **Phase offset** — Phase offset value `0` (default) | scalar | vector

Specify the phase offset as an integer-valued scalar or vector. Only
integer data types, including fixed-point data types with zero fraction
length, are allowed. When you specify the phase offset using this dialog
box parameter, it must be a scalar or vector with the same length as the
phase increment. Scalars are expanded to a vector with the same length
as the phase increment. Each element of the phase offset vector is
applied to a different channel of the input, and therefore the vector
length defines the number of output channels.

#### Dependencies

To enable this parameter, set **Phase offset
source** to `Specify via
dialog`.

### **Add internal dither** — Add internal dithering `on` (default) | `off`

Select to add internal dithering to the NCO algorithm. Dithering is
added using the PN Sequence Generator (Communications Toolbox) from the
Communications Toolbox™ product.

### **Number of dither bits** — Number of dither bits `4` (default) | positive integer

Specify the number of dither bits as a positive integer.

#### Dependencies

To enable this port, select the **Add internal
dither** check box.

### **Quantize phase** — Enable quantization of accumulated phase `on` (default) | `off`

To enable quantization of the accumulated phase, select this check
box.

### **Number of quantized accumulator bits** — Number of quantized accumulator bits `12` (default) | integer scalar

Specify the number of quantized accumulator bits as a scalar integer
greater than one, and less than the accumulator word length. This value
determines the number of entries in the lookup table.

#### Dependencies

To enable this port, select the **Quantize
phase** check box.

### **Show phase quantization error port** — Output quantization error `off` (default) | `on`

Select to output the phase quantization error. When you select this
check box, the **Qerr** port appears on the block
icon.

#### Dependencies

To enable this parameter, select the **Quantize
phase** check box.

#### Output Parameters

### **Output signal** — Output signal `Sine` (default) | `Cosine` | `Complex exponential` | `Sine and cosine`

Choose whether the block outputs a `Sine`,
`Cosine`, `Complex
exponential`, or both `Sine and
cosine` signals. If you select `Sine and
cosine`, the two signals output on different
ports.

### **Sample time** — Output sample period `1` (default) | positive scalar

When the block is acting as a source, specify the sample time in
seconds as a positive scalar.

#### Dependencies

To enable this parameter, both **Phase increment
source** and **Phase offset source**
must be set to `Specify via dialog`. When
either the phase increment or phase offset come in via a block input
port, the sample time is inherited and this parameter is not
visible.

### **Samples per frame** — Samples per frame `1` (default) | positive integer

Specify the number of samples per frame as a positive integer. When
the value is greater than one, the phase increment and phase offset can
vary from channel to channel and from frame to frame, but they are
constant along each channel in a given frame.

When the phase offset input port exists, it has the same frame status
as any output port present. When the phase increment input port exists,
it does not support frames.

#### Dependencies

To enable this parameter set **Phase increment
source** and/or **Phase offset
source** to `Specify via
dialog`.

### Data Types

### **Rounding mode** — Rounding method Read-only: `Floor` (default)

This parameter is read-only.

When the input is fixed point, the NCO block always
uses the rounding
mode
`Floor`.

### **Overflow mode** — Overflow method Read-only: `Wrap` (default)

This parameter is read-only.

When the input is fixed point, the NCO block always
uses the overflow
mode
`Wrap`.

### **Accumulator Word Length** — Accumulator word length `16` (default) | integer from 2 to 128

Specify a **Word length** for the **Accumulator** as a
positive integer from 2 to 128. The **Data Type** is
always `Binary point scaling`, and the
**Fraction length** is always
`0`.

### **Output Data Type** — Output data type `double` (default) | `single` | `Binary point scaling`

Specify a **Data Type** for the block
**Output**.

- Choose `double` or
  `single` for a floating-point
  implementation.
- When you select `Binary point
  scaling`, you can enter the word length and the
  fraction length of the output, in bits.

**Note**

The lookup table for this block is constructed from
double-precision floating-point values. Thus, the maximum amount of
precision you can achieve in your output is 53 bits. Setting the
word length of the **Output** data type to values
greater than 53 bits does not improve the precision of your
output.

### **Output Word Length** — Output word length `16` (default) | integer from 2 to 128

Specify a **Word length** for the block **Output** as
a positive integer from 2 to 128.

#### Dependencies

To enable this parameter, set the **Data Type**
for the **Output** to `Binary point
scaling`.

### **Output Fraction Length** — Output fraction length `14` (default) | integer

Specify a **Fraction length** for the block **Output**
as a scalar integer.

#### Dependencies

To enable this parameter, set the **Data Type**
for the **Output** to `Binary point
scaling`.

### NCO Characterization

The **NCO Characterization** pane provides you with read-only
details on the NCO signal currently being implemented by the block:

### **Number of data points for lookup table** — Number of points in lookup table no default

The lookup table is implemented as a quarter-wave sine table. The
number of lookup table data points is defined by

2number of quantized accumulator bits−2+1

**Example:** 1025

### **Quarter wave sine lookup table size** — Size of quarter wave sine lookup table no default

The quarter wave sine lookup table size is defined by

(number of data points for lookup table)⋅(output word length)8 bytes

**Example:** 2050 bytes

### **Theoretical spurious free dynamic range** — Spurious free dynamic range no default

The spurious free dynamic range (SFDR) is calculated as follows for a
lookup table with 2P entries:

SFDR=(6P) dB           without ditherSFDR=(6P+12) dB    with dither

**Example:** 84 dBc

### **Frequency resolution** — Frequency resolution no default

The frequency resolution is the smallest possible incremental change
in frequency and is defined by:

Δf=1Ts⋅2NHz

**Example:** 15.2588 uHz

#### Dependencies

The frequency resolution only appears when you set **Phase
increment source** and **Phase offset
source** to `Specify via
dialog`.
## Libraries

DSP System Toolbox / Signal Operations DSP System Toolbox / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `fixed point` | `integer` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL support for the NCO block will be removed in a future release. Use the NCO (DSP HDL Toolbox) block instead. The
DSP HDL Toolbox™ block provides an HDL-optimized algorithm with hardware-friendly
control signals and simulates the latency of the HDL algorithm in Simulink®.

## Version History

**Introduced before R2006a**

## Description

Generate real or complex sinusoidal signals

The NCO block generates a multichannel real or complex sinusoidal
signal, with independent frequency and phase in each output channel. The amplitude of
the created signal is always `1`. The NCO block supports
real inputs only. All outputs are real except for the output signal in
`Complex exponential` mode. For more information on how the
block computes the output, see Algorithms.

To produce a multichannel output, specify a vector quantity for the **Phase
increment** and **Phase offset** parameters. Both
parameters must have the same length, which defines the number of output channels. Each
element of each vector is applied to a different output channel.
