---
type: simulink-block
title: 'Bandstop IIR Filter Design'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filter Design and Analysis / Filter Design / Filter Design Sources'
documentation_page: 'bandstopiirfilterdesign'
documentation_source_path: 'ref/bandstopiirfilterdesign.html'
language: en
---

# Bandstop IIR Filter Design

## Ports

### Input

### **N** — Filter order even positive integer

Specify the filter order as an even positive integer. You can change the filter
order you input through this port during simulation.

#### Dependencies

To enable this port, select the **Specify filter order from input
port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Fc1** — First 3-dB cutoff frequency nonnegative scalar ≤ **Fc2**

Specify the first 3-dB cutoff frequency **Fc1** of the filter in
normalized frequency units as a nonnegative scalar less than or equal to the second
3-dB cutoff frequency **Fc2**.

You can change the first 3-dB cut off frequency you input through this port during
simulation.

#### Dependencies

To enable this port, select the **Specify first 3-dB cutoff frequency
from input port** parameter.

**Data Types:** `single` | `double`

### **Fc2** — Second 3-dB cutoff frequency **Fc1** ≤ positive scalar ≤ `1`

Specify the second 3-dB cutoff frequency of the filter in normalized frequency
units as a positive scalar greater than or equal to **Fc1** and less
than or equal to `1`.

You can change the second 3-dB cut off frequency you input through this port
during simulation.

#### Dependencies

To enable this port, select the **Specify second 3-dB cutoff frequency
from input port** parameter.

**Data Types:** `single` | `double`

### **Ap** — Passband ripple in dB nonnegative scalar

Specify the passband ripple of the Chebyshev Type I filter as a nonnegative scalar
in dB. You can change the passband ripple you input through this port during
simulation.

#### Dependencies

To enable this port:

- Set the **Design method** parameter to
  `Chebyshev Type I`.
- Select the **Specify the passband ripple from input
  port** parameter.

**Data Types:** `single` | `double`

### **Ast** — Stopband attenuation in dB nonnegative scalar

Specify the stopband attenuation of the Chebyshev Type II filter as a nonnegative
scalar in dB. You can change the stopband attenuation you input through this port
during simulation.

#### Dependencies

To enable this port:

- Set the **Design method** parameter to
  `Chebyshev Type II`.
- Select the **Specify the stopband attenuation from input
  port** parameter.

**Data Types:** `single` | `double`
### Output

### **Num** — Numerator coefficients *P*-by-3 matrix | *P*-by-5 matrix

Numerator coefficients, returned as a *P*-by-3 matrix (SOS form)
or a *P*-by-5 matrix (FOS form), where *P* is the
maximum number of filter sections.

**SOS
form** *(since R2023b)*

When you set **Filter cascade sections form** to
`Second-order sections`, the block generates a
*P*-by-3 numerator coefficients matrix.

b=[b01b11b21b02b12b22⋮⋮⋮b0Pb1Pb2P]

This equation represents the SOS filter in the transfer function form.

H(z)=∏k=1PHk(z)=∏k=1Pb0k+b1kz−1+b2kz−2a0k+a1kz−1+a2kz−2,

where

- **b** is a matrix of numerator coefficients.
- **a** is a matrix of denominator coefficients that the
  block outputs at the **Den** output port.
- *k* is the row index.

*P* equals
`ceil`(*Nmax*/2) in the
SOS form, where *Nmax* is the value of the
**Filter maximum order (must be even)** parameter.

When the actual filter order *N* is less than the maximum filter
order *Nmax*, the last
`ceil`(*Nmax*/2) −
`ceil`(*N*/2) sections are trivial with
coefficients [*b*0,
*b*1,
*b*2] = [1, 0, 0].

**FOS form**

When you set **Filter cascade sections form** to
`Fourth-order sections`, the block generates a
*P*-by-5 numerator coefficients matrix.

b=[b01b11b21b31b41b02b12b22b32b42⋮⋮⋮⋱⋮b0Pb1Pb2Pb3Pb4P]

This equation represents the FOS filter in the transfer function form.

H(z)=∏k=1PHk(z)=∏k=1Pb0k+b1kz−1+b2kz−2+b3kz−3+b4kz−4a0k+a1kz−1+a2kz−2+a3kz−3+a4kz−4

*P* equals
`ceil`(*Nmax*/4) in the
FOS form.

When the actual filter order *N* is less than the maximum filter
order *Nmax*, the last
`ceil`(*Nmax*/4) −
`ceil`(*N*/4) sections are trivial with
coefficients [*b*0,
*b*1,
*b*2,
*b*3,
*b*4] = [1, 0, 0, 0, 0].

The data type of this port depends on the value of the **Output data
type** parameter.

**Data Types:** `single` | `double`

### **Den** — Denominator coefficients *P*-by-5 matrix

Denominator coefficients, returned as a *P*-by-3 matrix (SOS
form) or a *P*-by-5 matrix (FOS form), where *P* is
the maximum number of filter sections.

**SOS
form** *(since R2023b)*

When you set **Filter cascade sections form** to
`Second-order sections`, the block generates a
*P*-by-3 denominator coefficients matrix.

a=[a01a11a21a02a12a22⋮⋮⋮a0Pa1Pa2P]

This equation represents the SOS filter in the transfer function form.

H(z)=∏k=1PHk(z)=∏k=1Pb0k+b1kz−1+b2kz−2a0k+a1kz−1+a2kz−2,

where

- **a** is a matrix of denominator coefficients and the
  leading denominator coefficient *a*0 is
  always 1.
- **b** is a matrix of numerator coefficients that the block
  outputs at the **Num** port.
- *k* is the row index.

*P* equals
`ceil`(*Nmax*/2) in the
SOS form, where *Nmax* is the value of the
**Filter maximum order (must be even)** parameter.

When the actual filter order *N* is less than the maximum filter
order *Nmax*, the last
`ceil`(*Nmax*/2) −
`ceil`(*N*/2) sections are trivial with
coefficients [*a*0,
*a*1,
*a*2] = [1, 0, 0].

**FOS form**

When you set **Filter cascade sections form** to
`Fourth-order sections`, the block generates a
*P*-by-5 denominator coefficients matrix.

a=[a01a11a21a31a41a02a12a22a32a42⋮⋮⋮⋱⋮a0Pa1Pa2Pa3Pa4P]

This equation represents the FOS filter in the transfer function form.

H(z)=∏k=1PHk(z)=∏k=1Pb0k+b1kz−1+b2kz−2+b3kz−3+b4kz−4a0k+a1kz−1+a2kz−2+a3kz−3+a4kz−4

*P* equals
`ceil`(*Nmax*/4) in the
FOS form.

The leading denominator coefficient *a*0
is always 1.

When the actual filter order *N* is less than the maximum filter
order *Nmax*, the last
`ceil`(*Nmax*/4) −
`ceil`(*N*/4) sections are trivial with
coefficients [*a*0,
*a*1,
*a*2,
*a*3,
*a*4] = [1, 0, 0, 0, 0].

The data type of this port depends on the value of the **Output data
type** parameter.

**Data Types:** `single` | `double`

### **g** — Scale values for each second-order section vector

*Since R2023b*

Scale values for each second-order section, returned as a vector with
*P* + 1 elements, where *P* is the maximum number
of filter sections and equals
`ceil`(*Nmax*/2), where
*Nmax* is the value of the
**Filter maximum order (must be even)** parameter.

**Tunable:** Yes

#### Dependencies

To enable this port:

- Set **Filter cascade sections form** to
  `Second-order sections`.
- Select the **Design has scale values** parameter.

**Data Types:** `single` | `double`

## Parameters

### **Smooth tuned filter parameters** — Smooth tuned filter parameters `off` (default) | `on`

*Since R2024a*

When you select this check box, the block updates the tunable filter parameters such
as the filter order, cutoff frequencies, passband ripple, and stopband attenuation
gradually by repeatedly designing the filter with intermediate values of the parameter
until the parameter reaches the desired value. This process is called parameter
smoothing. For more information, see Parameter Smoothing.

When you clear this check box, the block redesigns the filter with the new parameter
value immediately.

### **Smoothing factor** — Smoothing factor 0.6 (default) | nonnegative scalar less than 1

*Since R2024a*

Specify the smoothing factor *α* as a nonnegative scalar less than
1. When *α* = 0, no smoothing occurs. As *α*
approaches 1, the number of smoothing operations, and consequently, the number of filter
redesigns increase.

**Tunable:** Yes

#### Dependencies

To enable this parameter, select the **Smooth tuned filter
parameters** parameter.

### **Design method** — Filter design method `Butterworth` (default) | `Chebyshev Type I` | `Chebyshev Type II`

Specify the filter design method as one of these:

- `Butterworth`
- `Chebyshev Type I`
- `Chebyshev Type II`

### **Specify filter order from input port** — Flag to specify filter order from input port `off` (default) | `on`

Select this parameter to specify the filter order from the input port
**N**. When you clear this parameter, you can specify the filter
order in the block dialog box using the **Filter order (must be even)**
parameter.

### **Filter order (must be even)** — Filter order `6` (default) | even positive integer

Specify the filter order as an even positive integer less than or equal to the value
of the **Filter maximum order (must be even)** parameter.

**Tunable:** Yes

#### Dependencies

To enable this parameter, clear the **Specify filter order from input
port** parameter.

### **Filter maximum order (must be even)** — Maximum order of filter `10` (default) | even positive integer

Specify the maximum order of the filter as an even positive integer. The value you
specify in the **Filter order (must be even)** parameter must be less
than or equal to the value you specify in the **Filter maximum order (must be
even)** parameter.

### **Design has scale values** — Specify if filter has scale values for each section `off` (default) | `on`

*Since R2023b*

Specify if the filter has scale values for each section. When you select this
parameter, the block outputs the scale values through the **g** output
port.

#### Dependencies

To enable this parameter, set **Filter cascade sections form** to
`Second-order sections`.

### **Specify first 3-dB cutoff frequency from input port** — Flag to specify first 3-dB cutoff frequency from input port `off` (default) | `on`

Select this parameter to specify the first 3-dB filter cutoff frequency from the
input port **Fc1**. When you clear this parameter, you can specify the
first 3-dB cutoff frequency in the block dialog box using the **First 3-dB
cutoff frequency** parameter.

### **First 3-dB cutoff frequency** — First 3-dB cutoff frequency `0.25` (default) | positive scalar

Specify the first 3-dB cutoff frequency of the filter in normalized frequency units
as a positive scalar less than or equal to the second 3-dB cutoff frequency.

**Tunable:** Yes

#### Dependencies

To enable this parameter, clear the **Specify first 3-dB cutoff frequency
from input port** parameter.

### **Specify second 3-dB cutoff frequency from input port** — Flag to specify second 3-dB cutoff frequency from input port `off` (default) | `on`

Select this parameter to specify the second 3-dB filter cutoff frequency from the
input port **Fc2**. When you clear this parameter, you can specify the
second 3-dB cut-off frequency in the block dialog box using the **Second 3-dB
cutoff frequency** parameter.

### **Second 3-dB cutoff frequency** — Second 3-dB cutoff frequency `0.75` (default) | positive scalar

Specify the second 3-dB cutoff frequency of the filter in normalized frequency units
as a positive scalar greater than or equal to the first 3-dB cutoff frequency and less
than or equal to `1`.

**Tunable:** Yes

#### Dependencies

To enable this parameter, clear the **Specify second 3-dB cutoff frequency
from input port** parameter.

### **Specify the passband ripple from input port** — Flag to specify passband ripple from input port `off` (default) | `on`

Select this parameter to specify passband ripple from the input port
**Ap**. When you clear this parameter, you can specify the passband
ripple in the block dialog box using the **Passband ripple (dB)**
parameter.

#### Dependencies

To enable this parameter, set the **Design method** parameter to
`Chebyshev Type I`.

### **Passband ripple (dB)** — Passband ripple in dB `1` (default) | positive scalar

Specify the passband ripple of the Chebyshev Type I filter as a positive scalar in
dB.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set the **Design method** parameter to
  `Chebyshev Type I`.
- Clear the **Specify the passband ripple from input port**
  parameter.

### **Specify the stopband attenuation from input port** — Flag to specify stopband attenuation from input port `off` (default) | `on`

Select this parameter to specify stopband attenuation from the input port
**Ast**. When you clear this parameter, you can specify the stopband
attenuation in the block dialog box using the **Stopband attenuation
(dB)** parameter.

#### Dependencies

To enable this parameter, set the **Design method** parameter to
`Chebyshev Type II`.

### **Stopband attenuation (dB)** — Stopband attenuation in dB `60` (default) | positive scalar

Specify the stopband attenuation of the Chebyshev Type II filter as a positive
scalar in dB.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set the **Design method** parameter to
  `Chebyshev Type II`.
- Clear the **Specify the stopband attenuation from input
  port** parameter.

### **Sample time** — Sample time in seconds `-1` (default) | positive scalar | `Inf`

Specify the sample time as `-1` (inherited), `Inf`
(constant sample time), or a positive scalar. This parameter determines when the block
produces the output and updates its internal state during simulation. For more details,
see What Is Sample Time? (Simulink).

### **Filter cascade sections form** — Form of filter cascade sections `Fourth-order sections` (default) | `Second-order sections`

*Since R2023b*

Specify the form of the filter cascade sections as one of these:

- `Fourth-order sections` –– The block generates a
  *P*-by-5 matrix of filter coefficients.
- `Second-order sections` –– The block generates a
  *P*-by-3 matrix of filter coefficients.

### **Output data type** — Data type of filter coefficients `double` (default) | `single`

Specify the data type of the filter coefficients that the block outputs through the
**Num** and **Den** ports. You can set the data type
to `double` or `single`.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB® interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.

## Libraries

DSP System Toolbox / Filtering / Filter Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

When you generate code from this block, you can tune the filter design specifications in
the generated code.

## Version History

**Introduced in R2023a**

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

### R2024a: Tunable Bandstop IIR Filter block renamed

The Tunable Bandstop IIR Filter has been renamed as Bandstop IIR
Filter Design block.

### R2024a: Support for smoothing tunable filter parameters

When tunable filter parameters such as the filter order, cutoff frequencies, passband
ripple, and stopband attenuation change during simulation, the block can smooth these
parameters until the parameters reach the desired value. For more information, see Parameter Smoothing.

### R2023b: Tunable Bandstop IIR Filter block generates coefficients in second-order section form

Starting in R2023b, the Tunable Bandstop IIR Filter block generates
filter coefficients in the SOS or FOS form. You can specify the form using the new
**Filter cascade sections form** parameter.

When you set **Filter cascade sections form** to `Second-order
sections` and select **Design has scale values**, the block
outputs scale values through the **g** port.

## Description

Design bandstop IIR filter with tunable filter specifications

Use the Bandstop IIR Filter Design block to design a bandstop IIR filter
using the Butterworth, Chebyshev Type I and Chebyshev Type II design methods. You can tune the
filter design specifications such as the filter order, 3-dB cutoff frequencies, passband
ripple, and stopband attenuation during simulation. When the values of these parameters
change, the block redesigns the filter and outputs the numerator and denominator coefficients
in the second-order section (SOS) form *(since R2023b)* or the
fourth-order section (FOS) form.
