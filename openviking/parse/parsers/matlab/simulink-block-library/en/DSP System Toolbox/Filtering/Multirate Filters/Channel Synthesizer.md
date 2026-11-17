---
type: simulink-block
title: 'Channel Synthesizer'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'channelsynthesizer'
documentation_source_path: 'ref/channelsynthesizer.html'
language: en
---

# Channel Synthesizer

## Ports
```yaml
ports:
- name: x
  summary: Input narrowband signals *Q*-by-*M* matrix | *L*-by-*M*-by-*N* array
  direction: input
  data_types: single | double
- name: coeffs
  summary: Prototype lowpass filter coefficients row vector
  direction: input
  data_types: single | double
- name: Port_1
  summary: Broadband signal *Q×M*-by-1 vector | *L×M*-by-*N* matrix
  direction: output
  data_types: single | double
```

### Input

### **x** — Input narrowband signals *Q*-by-*M* matrix | *L*-by-*M*-by-*N* array

Input narrowband signals, which the channel synthesizer merges to form
the broadband signal. Each narrowband signal forms a column in the input
signal. The number of columns in the input correspond to the number of
frequency bands of the filter bank. If the input is three-dimensional,
each matrix corresponds to a separate channel.

This port is unnamed until you set **Polyphase filter
specification** to `Coefficients`
and select the **Specify coefficients from input port**
parameter.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **coeffs** — Prototype lowpass filter coefficients row vector

Coefficients of the prototype lowpass filter. There must be at least
one coefficient per frequency band. If the length of the lowpass filter
is less than the number of frequency bands, the block zero-pads the
coefficients.

If you specify complex coefficients, the block designs a prototype
filter that is centered at a nonzero frequency, also known as a bandpass
filter. The modulated versions of the prototype bandpass filter appear
with respect to the prototype filter and are wrapped around the
frequency range [−*F*s
*F*s].

#### Dependencies

This port appears when you set **Polyphase filter
specification** to
`Coefficients` and select the
**Specify coefficients from input port**
parameter.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Broadband signal *Q×M*-by-1 vector | *L×M*-by-*N* matrix

Broadband signal the channel synthesizer forms from the multiple input
narrow subbands.

If the input is one of the following:

- *Q*-by-*M* matrix
  — The output is a *Q×M*-by-1
  vector. *M* is the number of frequency
  bands.
- *Q*-by-*M*-by-*N*
  matrix — The output is a
  *Q×M*-by-*N*
  matrix.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: InterpolationFactor
  summary: Interpolation factor Number of frequency bands (default) | positive integer
  group: ''
- name: Polyphase filter specification
  summary: Filter design parameters or coefficients Number of taps per band and stopband attenuation (default) | Coefficients
  group: ''
- name: Number of filter taps per frequency band
  summary: Number of filter coefficients per frequency band 12 (default) | positive integer
  group: ''
- name: Stopband attenuation (dB)
  summary: Stopband attenuation 80 (default) | positive real scalar
  group: ''
- name: Specify coefficients from input port
  summary: Flag to specify lowpass filter coefficients off (default) | on
  group: ''
- name: Prototype lowpass filter coefficients
  summary: Coefficients of prototype lowpass filter rcosdesign(0.25,6,8,'sqrt') (default) | row vector
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

If a parameter is listed as tunable, then you can change its value during
simulation.

### **InterpolationFactor** — Interpolation factor `Number of frequency bands` (default) | positive integer

*Since R2024a*

Specify the interpolation factor *L* as one of these:

- `Number of frequency bands` –– When
  you change the number of frequency bands, the interpolation
  factor changes automatically.
- Positive integer greater than or equal to the number of
  frequency bands *M*.

The number of frequency bands equals the number of channels in the input
signal. If the interpolation factor *L* equals the number
of frequency bands *M*, then the
*L*/*M* ratio equals 1, and the
synthesizer is known as the critically sampled channel synthesizer.

If *L* is greater than *M*, then the
*L*/*M* ratio must be an integer. For
more details, see Algorithm.

### **Polyphase filter specification** — Filter design parameters or coefficients `Number of taps per band and stopband attenuation` (default) | `Coefficients`

- `Number of taps per band and stopband
  attenuation` — Specify the filter design
  parameters through the **Number of filter taps per
  frequency band** and **Stopband attenuation
  (dB)** parameters. When you specify the design
  parameters, the filter is designed using the `designMultirateFIR`
  function.
- `Coefficients` — Specify the
  filter coefficients directly using the **Prototype
  lowpass filter coefficients** parameter or input
  them through the **coeffs** port.

### **Number of filter taps per frequency band** — Number of filter coefficients per frequency band `12` (default) | positive integer

Number of filter coefficients that each polyphase branch uses. The number
of polyphase branches matches the number of frequency bands. The total
number of filter coefficients for the prototype lowpass filter is given by
the product of the number of frequency bands and the number of filter taps
per frequency band. The number of frequency bands equals the number of
columns in the input. For a given stopband attenuation, increasing the
number of taps per band narrows the transition width of the filter. As a
result, there is more usable bandwidth for each frequency band, at the
expense of increased computation.

#### Dependencies

To enable this parameter, set **Polyphase filter
specification** to `Number of taps per band and
stopband attenuation`.

### **Stopband attenuation (dB)** — Stopband attenuation `80` (default) | positive real scalar

Stopband attenuation of the lowpass filter, in dB. This value controls the
maximum amount of aliasing from one frequency band to the next. As the
stopband attenuation increases, the passband ripple decreases.

#### Dependencies

To enable this parameter, set **Polyphase filter
specification** to `Number of taps per band and
stopband attenuation`.

### **Specify coefficients from input port** — Flag to specify lowpass filter coefficients off (default) | on

When you select this check box, the lowpass filter coefficients are input
through the **coeffs** port. When you clear this check box,
the coefficients are specified on the block dialog through the
**Prototype lowpass filter coefficients**
parameter.

#### Dependencies

To enable this parameter, set **Polyspace filter
specification** to
`Coefficients`.

### **Prototype lowpass filter coefficients** — Coefficients of prototype lowpass filter `rcosdesign(0.25,6,8,'sqrt')` (default) | row vector

This parameter specifies the coefficients of the prototype lowpass filter.
The default value is the coefficients vector that
`rcosdesign(0.25,6,8,'sqrt')` returns. There must be at
least one coefficient per frequency band. If the length of the lowpass
filter is less than the number of frequency bands, the block zero-pads the
coefficients.

If you specify complex coefficients, the block designs a prototype filter
that is centered at a nonzero frequency, also known as a bandpass filter.
The modulated versions of the prototype bandpass filter appear with respect
to the prototype filter and are wrapped around the frequency range
[−*F*s
*F*s].

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Polyphase filter
specification** to `Coefficients`
and clear the **Specify coefficients from input port**
parameter.

**Complex Number Support:** Yes

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

DSP System Toolbox / Filtering / Multirate Filters

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `No` |
| **Variable-Size Signals** | `Yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

### R2024a: Support for integer oversampling

Use the new **Interpolation factor** parameter to specify an
interpolation factor *L* that is greater than or equal to the
number of frequency bands *M*. If *L* >
*M*, then the ratio *L*/*M*
must be an integer and the synthesizer is known as an oversampled channel
synthesizer.

## Description

Polyphase FFT synthesis filter bank

The Channel Synthesizer block merges multiple narrowband signals into a
broadband signal by using an FFT-based synthesis filter bank. The filter bank uses a
prototype lowpass filter and is implemented using a polyphase structure. You can specify
the filter coefficients directly or through design parameters. When you specify the
design parameters, the filter is designed using the `designMultirateFIR` function.

This block also accepts variable-size inputs. That is, during the simulation, you can
change the size of each input channel. The number of channels cannot change.
