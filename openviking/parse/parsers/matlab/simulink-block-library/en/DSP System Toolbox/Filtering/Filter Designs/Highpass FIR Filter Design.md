---
type: simulink-block
title: 'Highpass FIR Filter Design'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Designs'
documentation_page: 'highpassfirfilterdesign'
documentation_source_path: 'ref/highpassfirfilterdesign.html'
language: en
---

# Highpass FIR Filter Design

## Ports

### Input

### **N** — Filter order even positive integer

Specify the filter order as an even positive integer less than or equal to
*Nmax*, where
*Nmax* is the value you specify
in the **Filter maximum order (must be even)** parameter. You
can change the filter order you input through this port during
simulation.

#### Dependency

To enable this port, select the **Specify filter order from input
port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Fcut** — Filter cutoff frequency positive scalar ≤ 1

Specify the cutoff frequency of the filter in the normalized frequency units
as a positive scalar less than or equal to 1. You can change the cutoff
frequency you input through this port during simulation.

#### Dependency

To enable this port, select the **Specify cutoff frequency from
input port** parameter.

**Data Types:** `single` | `double`

### **r** — Sidelobe attenuation in dB positive scalar

Specify the sidelobe attenuation of the Chebyshev type filter as a positive
scalar in dB. You can change the sidelobe attenuation you input through this
port during simulation.

#### Dependency

To enable this port:

- Set the **Window function** parameter to
  `Chebyshev`.
- Select the **Specify sidelobe attenuation from input
  port** parameter.

**Data Types:** `single` | `double`

### **beta** — Kaiser window parameter nonnegative scalar

Specify the Kaiser window parameter as a nonnegative scalar. You can change
the Kaiser window parameter you input through this port during
simulation.

#### Dependency

To enable this port:

- Set the **Window function** parameter to
  `Kaiser`.
- Select the **Specify kaiser window parameter from input
  port** parameter.

**Data Types:** `single` | `double`
### Output

### **Num** — Numerator coefficients row vector

Numerator coefficients, returned as a row vector of length
*Nmax* + 1, where *Nmax* is the maximum filter order that you specify using the
**Filter maximum order (must be even)** parameter.

This equation represents the vector of numerator coefficients
**b**.

b=[b0,b1,b2,...,bNmax]

This equation represents the FIR filter in the transfer function form.

H(z)=b0+b1z−1+b2z−2+...+bNmaxz−Nmax

When the actual filter order *N* is less than the maximum
filter order *Nmax*, the last *Nmax* −
*N* elements in the numerator coefficients vector are
trivial with a value of 0.

The data type of this port depends on the value of the **Output data
type** parameter.

**Data Types:** `single` | `double`

## Parameters

### **Smooth tuned filter parameters** — Smooth tuned filter parameters `off` (default) | `on`

*Since R2024a*

When you select this check box, the block updates the tunable filter parameters
such as the filter order, cutoff frequency, sidelobe attenuation, and Kaiser
window parameter gradually by repeatedly designing the filter with intermediate
values of the parameter until the parameter reaches the desired value. This
process is called parameter smoothing. For more information, see Parameter Smoothing.

When you clear this check box, the block redesigns the filter with the new
parameter value immediately.

### **Smoothing factor** — Smoothing factor 0.6 (default) | nonnegative scalar less than 1

*Since R2024a*

Specify the smoothing factor *α* as a nonnegative scalar less
than 1. When *α* = 0, no smoothing occurs. As
*α* approaches 1, the number of smoothing operations, and
consequently, the number of filter redesigns increase.

**Tunable:** Yes

#### Dependencies

To enable this parameter, select the **Smooth tuned filter
parameters** parameter.

### **Specify filter order from input port** — Flag to specify filter order from input port `off` (default) | `on`

Select this parameter to specify the filter order from the input port
**N**. When you clear this parameter, you can specify the
filter order in the block dialog box using the **Filter order (must be
even)** parameter.

### **Filter order (must be even)** — Filter order `100` (default) | even positive integer

Specify the filter order as an even positive integer that is less than or equal
to the value of the **Filter maximum order (must be even)**
parameter.

**Tunable:** Yes

#### Dependency

To enable this parameter, clear the **Specify filter order from
input port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Filter maximum order (must be even)** — Maximum order of filter `100` (default) | even positive integer

Specify the maximum order of the filter as an even positive integer. The value
you specify in the **Filter order (must be even)** parameter must
be less than or equal to the value you specify in the **Filter maximum
order (must be even)** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Specify cutoff frequency from input port** — Flag to specify cutoff frequency from input port `off` (default) | `on`

Select this parameter to specify the filter cutoff frequency from the input
port **Fcut**. When you clear this parameter, you can specify the
cutoff frequency in the block dialog box using the **Cutoff
frequency** parameter.

### **Cutoff frequency** — Cutoff frequency `0.5` (default) | positive scalar ≤ 1

Specify the cutoff frequency of the filter in the normalized frequency units as
a positive scalar less than or equal to `1`.

**Tunable:** Yes

#### Dependency

To enable this parameter, clear the **Specify cutoff frequency from
input port** parameter.

**Data Types:** `single` | `double`

### **Window function** — Window function `Hann` (default) | `Hamming` | `Blackman` | `Blackman-Harris` | `Chebyshev` | `Kaiser`

Specify the window function to use to design the filter:

- `Hann`
- `Hamming`
- `Blackman`
- `Blackman-Harris`
- `Chebyshev`
- `Kaiser`

### **Specify sidelobe attenuation from input port** — Flag to specify sidelobe attenuation from input port `off` (default) | `on`

Select this parameter to specify the sidelobe attenuation from the input port
**r**. When you clear this parameter, you can specify the
sidelobe attenuation in the block dialog box using the **Sidelobe
attenuation (dB)** parameter.

#### Dependency

To enable this parameter, set the **Window function**
parameter to `Chebyshev`.

### **Sidelobe attenuation (dB)** — Sidelobe attenuation in dB `60` (default) | positive scalar

Specify the sidelobe attenuation of the Chebyshev type FIR filter as a positive
scalar in dB.

**Tunable:** Yes

#### Dependency

To enable this parameter:

- Set the **Window function** parameter to
  `Chebyshev`.
- Clear the **Specify sidelobe attenuation from input
  port** parameter.

**Data Types:** `single` | `double`

### **Specify kaiser window parameter from input port** — Flag to specify Kaiser window parameter from input port `off` (default) | `on`

Select this parameter to specify the Kaiser window parameter from the input
port **beta**. When you clear this parameter, you can specify the
Kaiser window parameter in the block dialog box using **Kaiser window
parameter**.

#### Dependency

To enable this parameter, set the **Window function**
parameter to `Kaiser`.

### **Kaiser window parameter** — Kaiser window parameter `0.5` (default) | nonnegative scalar

Specify the Kaiser window parameter as a nonnegative scalar.

**Tunable:** Yes

#### Dependency

To enable this parameter:

- Set the **Window function** parameter to
  `Kaiser`.
- Clear the **Specify kaiser window parameter from input
  port** parameter.

**Data Types:** `single` | `double`

### **Sample time (−1 for inherited)** — Sample time in seconds `-1` (default) | positive scalar | `Inf`

Specify the sample time as `-1` (inherited),
`Inf` (constant sample time), or a positive scalar. This
parameter determines when the block produces the output and updates its internal
state during simulation. For more details, see What Is Sample Time? (Simulink).

**Data Types:** `single` | `double`

### **Output data type** — Data type of filter coefficients `double` (default) | `single`

Specify the data type of the filter coefficients that the block outputs through
the **Num** port. You can set the data type to
`double` or `single`.

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

When you generate code from this block, you can tune the filter design specifications
in the generated code.

## Version History

**Introduced in R2023b**

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

### R2024a: Tunable Highpass FIR Filter block renamed

The Tunable Highpass FIR Filter has been renamed as Highpass
FIR Filter Design block.

### R2024a: Support for smoothing tunable filter parameters

When tunable filter parameters such as the filter order, cutoff frequency, sidelobe
attenuation, and Kaiser window parameter change during simulation, the block can smooth
these parameters until the parameters reach the desired value. For more information, see
Parameter Smoothing.

## Description

Design highpass FIR filter with tunable filter specifications

Use the Highpass FIR Filter Design block to design a highpass FIR filter
using the Hann, Hamming, Blackman, Blackman-Harris, Chebyshev, and Kaiser windowing
methods. You can tune the filter order, filter cutoff frequency, and the sidelobe
attenuation during simulation. When the values of these parameters change, the block
redesigns the filter and outputs the numerator coefficients in vector form.
