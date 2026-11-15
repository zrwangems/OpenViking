---
type: simulink-block
title: 'Parametric Equalizer Design'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Audio Processing Algorithm Design / Filter Design'
documentation_page: 'parametricequalizerdesign'
documentation_source_path: 'ref/parametricequalizerdesign.html'
language: en
---

# Parametric Equalizer Design

## Ports

### Input

### **N** — Filter order positive even integer

Use this port to specify the value of the **Filter
order** parameter.

#### Dependencies

To enable this port, select the **Specify filter order from input
port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **G** — Gain (dB) real scalar

Use this port to specify the value of the **Gain (dB)**
parameter.

#### Dependencies

To enable this port, select the **Specify gain from input
port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Fc** — Normalized center frequency scalar in range [0,1]

Use this port to specify the value of the **Normalized center
frequency** parameter.

#### Dependencies

To enable this port, select the **Specify normalized center frequency
from input port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **BW** — Normalized bandwidth scalar in range [0,1]

Use this port to specify the value of the **Normalized
bandwidth** parameter.

#### Dependencies

To enable this port, select the **Specify normalized bandwidth from
input port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### Output

### **Num** — Numerator filter coefficients matrix

Numerator filter coefficients, returned as a matrix.

- For SOS filters, the block returns the coefficients as an
  *N*-by-3 matrix.
- For FOS filters, the block returns the coefficients as an
  *N*-by-5 matrix.

*N* is the number of filter sections and depends on the
**Maximum filter
order** parameter. If **Filter
order** is less than the **Maximum filter order**, then
the block sets the unused sections to pass-through sections.

#### Dependencies

- The data type of the output depends on the **Output data
  type** parameter.
- The output dimensions depend on the **Maximum filter
  order** and **Filter cascade
  sections form** parameters.

**Data Types:** `single` | `double`

### **Den** — Denominator filter coefficients matrix

Denominator filter coefficients, returned as a matrix.

- For SOS filters, the block returns the coefficients as an
  *N*-by-3 matrix.
- For FOS filters, the block returns the coefficients as an
  *N*-by-5 matrix.

*N* is the number of filter sections and depends on the
**Maximum filter
order** parameter. If **Filter
order** is less than **Maximum filter order**, then the
block sets the unused sections to pass-through sections.

#### Dependencies

- The data type of the output depends on the **Output data
  type** parameter.
- The output dimensions depend on **Maximum filter
  order** and **Filter cascade
  sections form** parameters.

**Data Types:** `single` | `double`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Smooth tuned filter parameters** — Smooth filter parameters when tuning `off` (default) | `on`

Select this parameter to gradually change a filter parameter to the new value when
tuning it. If you clear this parameter, the tuned parameter immediately switches to the
new value. Specify the level of smoothing with the **Smoothing
factor** parameter.

### **Smoothing factor** — Smoothing factor for tuned parameters `0.6` (default) | scalar in range [0,1)

Smoothing factor for tuned parameters, specified as a scalar in the range [0,1). As
the smoothing factor approaches 1, a tuned parameter changes more gradually to the new
value. A smoothing factor of 0 is equivalent to no smoothing.

For more information about smoothing, see Smoothing.

**Tunable:** Yes

#### Dependencies

To enable this parameter, select the **Smooth tuned filter
parameters** parameter.

### **Maximum filter order** — Maximum filter order `2` (default) | positive even integer

Maximum filter order of the designed coefficients, specified as a positive even
integer. The **Filter
order** parameter cannot exceed this value.

### **Specify filter order from input port** — Use additional input port to specify filter order `off` (default) | `on`

When you select this parameter, an additional input port, **N**, is added
to the block.

### **Filter order** — Filter order `2` (default) | positive even integer

Filter order of designed coefficients, specified as a positive even integer.

**Tunable:** Yes

#### Dependencies

- To enable this parameter, clear the **Specify filter order from input
  port** parameter.
- The value of this parameter cannot exceed **Maximum filter
  order**.

### **Specify gain from input port** — Use additional input port to specify gain `off` (default) | `on`

When you select this parameter, an additional input port, **G**, is added
to the block. Use this port to specify the gain of the filter.

### **Gain (dB)** — Gain (dB) `0` (default) | real scalar

Gain of the filter in dB, specified as a real scalar.

**Tunable:** Yes

#### Dependencies

To enable this parameter, clear the **Specify gain from input
port** parameter.

### **Specify normalized center frequency from input port** — Use additional input port to specify normalized center frequency `off` (default) | `on`

When you select this parameter, an additional input port, **Fc**, is added
to the block.

### **Normalized center frequency** — Normalized center frequency `0.2` (default) | scalar in range [0,1]

Normalized center frequency of the filter, specified as a scalar in the range [0,1]
where 1 corresponds to the Nyquist frequency.

**Tunable:** Yes

#### Dependencies

To enable this parameter, clear the **Specify normalized center frequency
from input port** parameter.

### **Specify normalized bandwidth from input port** — Use additional input port to specify normalized bandwidth `off` (default) | `on`

When you select this parameter, an additional input port, **BW**, is added
to the block.

### **Normalized bandwidth** — Normalized bandwidth `0.1` (default) | scalar in range [0,1]

Normalized bandwidth of the filter, specified as a scalar in the range [0,1] where 1
corresponds to the Nyquist frequency.

Normalized bandwidth is measured at gain/2 dB. If gain is set to `-Inf` (notch filter),
normalized bandwidth is measured at the 3 dB attenuation point: 10×log10(0.5).

To convert octave bandwidth to normalized bandwidth, calculate the associated
*Q*-factor as

Q=2(octave bandwidth)2(octave bandwidth)−1 .

Then convert to bandwidth

bandwidth=centerFreqQ .

#### Dependencies

To enable this parameter, clear the **Specify normalized bandwidth from
input port** parameter.

**Tunable:** Yes

### **Filter cascade sections form** — Form of cascaded filter sections `Second-order sections` (default) | `Fourth-order sections`

Form of cascaded filter sections, specified as `Second-order
sections` for SOS filters or `Fourth-order
sections` for FOS filters.

### **Output data type** — Data type of output coefficients `double` (default) | `single`

Data type of output coefficients, specified as `double` or
`single`.

### **Sample time** — Sample time of block `-1` (default) | positive scalar

Sample time of the block, in seconds, specified as `-1` or a
positive scalar. Setting this parameter to `-1` means Simulink determines the sample time automatically for you. You can set this
parameter to enable the design block to run at a slower rate than the filtering
block.

### **Simulate using** — Specify type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` –– Simulate model using the
  MATLAB® interpreter. This option shortens startup time but has a slower
  simulation speed than `Code generation`. In this mode,
  you can debug the source code of the block.
- `Code generation` –– Simulate model using generated C
  code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for subsequent
  simulations, as long as the model does not change. This option requires additional
  startup time, but the speed of the subsequent simulations is comparable to
  `Interpreted execution`.

## Libraries

Audio Toolbox / Filters

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

Design tunable parametric equalizer coefficients

The Parametric Equalizer Design block designs a parametric equalizer with
the specified filter order, gain, center frequency, and bandwidth. The block outputs filter
coefficients of cascaded second-order section (SOS) or fourth-order section (FOS) filters,
which you can use with the Second-Order Section
Filter or Fourth-Order Section
Filter blocks to filter audio signals. You can tune the filter parameters during
simulation.
