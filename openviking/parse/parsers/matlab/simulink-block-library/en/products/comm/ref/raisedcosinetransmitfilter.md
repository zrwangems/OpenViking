---
type: simulink-block
title: 'Raised Cosine Transmit Filter'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Filtering'
documentation_page: 'raisedcosinetransmitfilter'
documentation_source_path: 'ref/raisedcosinetransmitfilter.html'
language: en
---

# Raised Cosine Transmit Filter

## Ports

### Input

### **In** — Input signal scalar | column vector | matrix

Input signal, specified as a scalar, column vector, or
*K*i-by-*N*
matrix. *K*i is the number of
input samples per signal channel, and *N* is the number
of signal channels.

**Data Types:** `double` | `single` | `fixed point`
### Output

### **Out** — Output signal scalar | column vector | matrix

Output signal, returned as a scalar, column vector, or matrix. The block filters each
channel over time and generates a
*K*o-by-*N*
output matrix. The output signal is the same data type as the input signal.

- *K*o =
  *K*i ×
  *L*.
- *N* is the number of signal
  channels.
- *K*i is the number
  of input samples per signal channel.
- *L* is the value you specify in the
  **Output samples per symbol** parameter.

**Data Types:** `double` | `single` | `fixed point`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

#### Main

### **Filter shape** — Filter shape `Square root` (default) | `Normal`

Filter shape, specified as `Square root` or
`Normal`. For more information, see Filter Characteristics.

### **Rolloff factor** — Roll-off factor `0.2` (default) | scalar

Roll-off factor of the filter, specified as a scalar in the range [`0`,
`1`].

### **Filter span in symbols** — Filter span in symbols `10` (default) | even positive integer

Filter span in symbols, specified as an even positive integer. The block
truncates the infinite impulse response length of the ideal raised cosine
filter to an FIR with a length equal to the value of this parameter.

### **Output samples per symbol** — Number of output samples per symbol `8` (default) | integer greater than `1`

Number of output samples per symbol, specified as an integer value greater
than `1`. The number of taps for the raised cosine filter
equals the value of this parameter multiplied by the value of the **Filter
span in symbols** parameter.

### **Linear amplitude filter gain** — Linear filter gain `1` (default) | positive scalar

Linear filter gain, specified as a positive scalar. The block scales the normalized
filter coefficients by the linear filter gain value that you specify.

### **Input processing** — Input processing control `Columns as channels (frame based)` (default) | `Elements as channels (sample based)`

Input processing control, specified as one of these options:

- `Columns as channels (frame based)` — The block
  treats each column of the input as a separate channel.
- `Elements as channels (sample based)` — The block
  treats each element of the input as a separate channel.

### **Rate options** — Block processing rate `Enforce single-rate processing` (default) | `Allow multirate processing`

Block processing rate for input signal upsampling and filtering, specified as one of
these options:

- `Enforce single-rate processing` — When you
  select this option, the block maintains the input sample rate and processes
  the signal by increasing the output frame size by a factor of
  *N*.
- `Allow multirate processing` — When you select
  this option, the block processes the signal such that the output sample rate
  is *N* times faster than the input sample rate.

#### Dependencies

To use `Enforce single-rate processing`, you must set
**Input processing** to `Columns as channels
(frame based)`.

### **Export filter coefficients to workspace** — Export filter coefficients `off` (default) | `on`

Select this parameter to save the filter coefficients as the MATLAB® workspace variable that you specify in the **Coefficient variable name** parameter.

### **Coefficient variable name** — Name of coefficient variable `rcTxFilt` (default)

Name of the coefficient variable to create in the MATLAB workspace.

#### Dependencies

This parameter appears when you select **Export
filter coefficients to workspace**.

### **View Filter Response** — Open Filter Visualization Tool button

To analyze the raised cosine filter response, click the **View
Filter Response** button. MATLAB opens a filter visualization window. When you change the block
mask parameter settings, click the button again to open a new instance of
the window and see the new filter characteristics. Previous filter
visualization windows remain open and reflect your previous mask settings.
Instances of the filter visualization window remain open after you close the
model.

#### Data Types

### **Rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Select the rounding mode for fixed-point operations. The block uses
rounding mode when the result of a fixed-point calculation does not map
exactly to a number representable by the data type. The filter coefficients
do not obey this parameter; they always round to
`Nearest`. For more information, see Rounding Modes
or Rounding Mode: Simplest (Fixed-Point Designer).

### **Saturate on integer overflow** — Overflow mode for fixed-point operations `off` (default) | `on`

Select the overflow mode for fixed-point operations. The filter
coefficients do not obey this parameter; they are always saturated.

### **Coefficients** — Coefficient data type `Inherit: Same word length as input` (default) | `fixdt(1,16)` | `fixdt(1,16,0)`

Specify the word length and the fraction length of the filter coefficients
(numerator and denominator).

This block is a subsystem that contains a FIR Interpolation block. For
diagrams showing the use of the coefficient data types in this block, see
the filter structure diagrams for the Discrete FIR Filter (Simulink)
block.

When you select `Inherit: Same word length as input`, the word
length of the filter coefficients match that of the input to the block. In
this mode, the fraction length of the coefficients is automatically set to
the binary-point only scaling that provides you with the best precision
possible given the value and word length of the coefficients.

The filter coefficients do not obey the **Rounding
mode** and the **Saturate
on integer overflow** parameters; they are always saturated
and rounded to `Nearest`.

For information about specifying data types, see Data Type Assistant.

### **Product output** — Product output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `fixdt(1,16,0)`

Specify the product output word and fraction lengths. For diagrams showing
the use of the product output data type in this block, see the filter
structure diagrams for the Discrete FIR Filter (Simulink) block and
Multiplication Data Types.

- When you select `Inherit via internal
  rule`, the block inherits the data type based
  on an internal rule. For more information on this rule, see
  Inherit via Internal Rule.
- When you select `Inherit: Same as
  input`, these characteristics match those of
  the input to the block.

For information about specifying data types, see Data Type Assistant.

### **Accumulator** — Accumulator data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

Specify the accumulator word and fraction lengths. For diagrams showing
the use of the accumulator data type in this block, see the filter structure
diagrams for the Discrete FIR Filter (Simulink) block and
Multiplication Data Types.

- When you select `Inherit: Inherit via internal
  rule`, the block inherits the data type based
  on an internal rule. For more information on this rule, see
  Inherit via Internal Rule.
- When you select `Inherit: Same as
  input`, these characteristics match those of
  the input to the block.
- When you select `Inherit: Same as product
  output`, these characteristics match those of
  the product output.

For information about specifying data types, see Data Type Assistant.

### **Output** — Output data type `Inherit: Same as accumulator` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

Specify the output word and fraction lengths.

- When you select `Inherit: Same as
  input`, these characteristics match those of
  the input to the block.
- When you select `Inherit: Same as
  accumulator`, these characteristics match those
  of the accumulator.
- When you select `Inherit: Same as product
  output`, these characteristics match those of
  the product output.

For information about specifying data types, see Data Type Assistant.

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the
data types that you specify in the block dialog box. For more information,
see the Fixed-Point Tool (Fixed-Point Designer).

## Libraries

Communications Toolbox / Comm Filters Communications Toolbox HDL Support / Comm Filters

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed pointa` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
|  |  |
| --- | --- |
| a Fixed-point outputs must be signed. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on `memcpy` or
`memset` functions (`string.h`) under certain
conditions.

This block supports SIMD code generation using Intel® AVX2 technology under these conditions:

- **Input processing** is set to `Columns
  as channels (frame based)`.
- **Rate options** is set to `Enforce
  single-rate processing`.
- Input signal is real-valued with real filter coefficients.
- Input signal is complex-valued with real or complex filter
  coefficients.
- Input signal has a data type of `single` or
  `double`.

The SIMD technology significantly improves the performance of the
generated code. For details, see Generate SIMD Code from Simulink Blocks for Intel Platforms (Embedded Coder).

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

This block is a subsystem that contains an FIR Interpolation block. You can
set **HDL Properties** on the subsystem, or you can look under the
mask and set **HDL Properties** on the filter block. See the "HDL
Code Generation" section of the Subsystem, Atomic Subsystem, CodeReuse
Subsystem (Simulink) and FIR Interpolation block reference pages
for a list of properties.

To save setting changes under the mask, you must break the library link. To break the
library link, select the Raised Cosine Transmit Filter block and run
this
command.

```
set_param(gcb,'LinkStatus','inactive')
```

## Version History

**Introduced before R2006a**

## Description

Apply pulse shaping by interpolating signal using raised cosine FIR filter

The Raised Cosine Transmit Filter block applies pulse shaping by interpolating an input signal
using a raised cosine finite impulse response (FIR) filter. The FIR filter has
(**Filter span in
symbols** × **Output samples per
symbol** + 1) tap coefficients. The block icon shows the impulse response
of the filter. For more information, see Algorithms.
