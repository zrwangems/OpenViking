---
type: simulink-block
title: 'Ideal Rectangular Pulse Filter'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Filters'
documentation_page: 'idealrectangularpulsefilter'
documentation_source_path: 'ref/idealrectangularpulsefilter.html'
language: en
---

# Ideal Rectangular Pulse Filter

## Ports
```yaml
ports:
- name: In
  summary: Input signal scalar | column vector | matrix
  direction: input
  data_types: double | single | fixed point
- name: Out
  summary: Output signal column vector | matrix
  direction: output
  data_types: double | single | fixed point
```

### Input

### **In** — Input signal scalar | column vector | matrix

Input signal, specified as a scalar, column vector, or
*K*i-by-*N*
matrix. *K*i is the number of
input samples per signal channel, and *N* is the number
of signal channels.

**Data Types:** `double` | `single` | `fixed point`
### Output

### **Out** — Output signal column vector | matrix

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
  **Pulse length (number of samples)**
  parameter.

**Data Types:** `double` | `single` | `fixed point`
## Parameters
```yaml
parameters:
- name: Pulse length (number of samples)
  summary: Pulse length 8 (default) | positive integer
  group: ''
- name: Pulse delay (number of samples)
  summary: Pulse delay 0 (default) | nonnegative integer
  group: ''
- name: Input processing
  summary: Input processing control Columns as channels (frame based) (default) | Elements as channels (sample based)
  group: ''
- name: Rate options
  summary: Block processing rate Enforce single-rate processing (default) | Allow multirate processing
  group: ''
- name: Normalize output signal
  summary: Option to normalize output signal off (default) | on
  group: ''
- name: Normalization method
  summary: Normalization method Sum of samples (default) | Energy per pulse
  group: ''
- name: Linear amplitude gain
  summary: Linear gain 1 (default) | positive scalar
  group: ''
- name: Rounding mode
  summary: Rounding mode for fixed-point operations Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest |
    Zero
  group: ''
- name: Saturate on integer overflow
  summary: Overflow mode for fixed-point operations off (default) | on
  group: ''
- name: Coefficients
  summary: 'Coefficient data type Inherit: Same word length as input (default) | fixdt(1,16) | fixdt(1,16,0)'
  group: ''
- name: Product output
  summary: 'Product output data type Inherit: Inherit via internal rule (default) | Inherit: Same as input | fixdt(1,16,0)'
  group: ''
- name: Accumulator
  summary: 'Accumulator data type Inherit via internal rule (default) | Inherit: Same as input | Inherit: Same as product
    output | fixdt(1,16,0)'
  group: ''
- name: Output
  summary: 'Output data type Inherit: Same as accumulator (default) | Inherit: Same as input | Inherit: Same as product output
    | fixdt(1,16,0)'
  group: ''
- name: Lock data type settings against changes by the fixed-point tools
  summary: Prevent fixed-point tools from overriding data types off (default) | on
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

#### Main

### **Pulse length (number of samples)** — Pulse length `8` (default) | positive integer

Pulse length in samples, specified as a positive integer. The block replicates each input
sample *L* times, where *L* is the pulse
length that you specify in samples.

### **Pulse delay (number of samples)** — Pulse delay `0` (default) | nonnegative integer

Pulse delay in samples, specified as a nonnegative integer. If this parameter is nonzero,
then the block outputs that number of zeros at the beginning of the
simulation, before starting to replicate any of the input values.

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

### **Normalize output signal** — Option to normalize output signal `off` (default) | `on`

Select this parameter to scale the set of replicated values before
applying the linear amplitude gain.

### **Normalization method** — Normalization method `Sum of samples` (default) | `Energy per pulse`

Normalization method, specified as `Sum of samples` or
`Energy per pulse`. This parameter assigns the
quantity that the block considers when scaling the set of replicated values.
For more information, see Normalization Methods.

#### Dependencies

This parameter appears when you select **Normalize output signal**.

### **Linear amplitude gain** — Linear gain `1` (default) | positive scalar

Linear gain, specified as a positive scalar. The block scales the output signal by the
linear gain value that you specify. For more information, see Normalization Methods.

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

Specify the word length and the fraction length of the filter coefficients (numerator and
denominator).

When you select `Inherit: Same word length as input`, the word
length of the filter coefficients match that of the input to the block. In
this mode, the fraction length of the coefficients is automatically set to
the binary-point-only scaling that provides you with the best precision
possible given the value and word length of the coefficients.

For more information and illustrations depicting the use of the
coefficient data types in this block, see the filter structure diagrams for
the Discrete FIR Filter (Simulink)
block.

The filter coefficients do not obey the **Rounding
mode** and the **Saturate
on integer overflow** parameters; they are always saturated
and rounded to `Nearest`.

For information about specifying data types, see Data Type Assistant.

### **Product output** — Product output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `fixdt(1,16,0)`

Specify the product output word and fraction lengths.

- When you select `Inherit: Inherit via internal
  rule`, the block inherits the data type based
  on an internal rule. For more information on this rule, see
  Inherit via Internal Rule.
- When you select `Inherit: Same as
  input`, these characteristics match those of
  the input to the block.

For more information and illustrations depicting the use of the product
output data type in this block, see the filter structure diagrams for the
Discrete FIR Filter (Simulink) and Multiplication Data Types.

For information about specifying data types, see Data Type Assistant.

### **Accumulator** — Accumulator data type `Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

Specify the accumulator word and fraction lengths.

- When you select `Inherit via internal
  rule`, the block inherits the data type based
  on an internal rule. For more information on this rule, see
  Inherit via Internal Rule.
- When you select `Inherit: Same as
  input`, these characteristics match those of
  the input to the block.
- When you select `Inherit: Same as product
  output`, these characteristics match those of
  the product output.

For more information and illustrations depicting the use of the
accumulator output data type in this block, see the filter structure
diagrams for the Discrete FIR Filter (Simulink) and Multiplication Data Types.

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

Communications Toolbox / Comm Filters

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

## Version History

**Introduced before R2006a**

## Description

Shape input signal using ideal rectangular pulses

The Ideal Rectangular Pulse Filter block upsamples and shapes the input signal using rectangular
pulses. After replicating input samples, the block can also normalize the output signal
and apply a linear amplitude gain.
