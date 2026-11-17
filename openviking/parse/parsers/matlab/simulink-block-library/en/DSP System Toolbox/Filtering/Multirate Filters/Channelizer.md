---
type: simulink-block
title: 'Channelizer'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'channelizer'
documentation_source_path: 'ref/channelizer.html'
language: en
---

# Channelizer

## Ports
```yaml
ports:
- name: x
  summary: Broadband signal *L*-by-1 column vector | *L*-by-*N* matrix
  direction: input
  data_types: single | double
- name: coeffs
  summary: Prototype lowpass filter coefficients row vector
  direction: input
  data_types: single | double
- name: Output(s)
  summary: Multiple narrowband signals vector | matrix | 3-D array
  direction: output
  data_types: single | double
```

### Input

### **x** — Broadband signal *L*-by-1 column vector | *L*-by-*N* matrix

Specify the input broadband signal that the channelizer splits into
multiple narrow bands.

- When you input a variable-size signal (frame length changes
  during simulation), the frame length of the signal can be
  arbitrary, that is, the input frame length does not have to be a
  multiple of the decimation factor.
- When you input a fixed-size signal (frame length does not
  change during simulation), the frame length can be arbitrary
  only when you select the **Allow arbitrary frame length
  for fixed-size input signals** parameter.

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

### **Output(s)** — Multiple narrowband signals vector | matrix | 3-D array

Multiple narrow subbands of the input broadband signal, returned as a
vector, matrix, or 3-D array. The number of
output ports and the dimension of each port depends on the
dimensions of the input signal and whether you select the
**Bands as separate output ports (Max. of 16
bands)** parameter. *(since R2024a)*

When you select the
**Bands as separate output ports (Max. of 16
bands)** parameter, the block outputs each narrowband
signal at a separate port. The number of output ports is in the range [1
`min`(**Number of frequency
bands**, 16)]. When you clear the **Bands as
separate output ports (Max. of 16 bands)** parameter, the
block outputs each narrowband signal as a separate column in the output
array and outputs the array at a single output port. *(since R2024a)*

This table provides more information on the dimensions of the output
signal when you input a fixed-size input signal (frame size does not
change during simulation).

| Input Signal | Conditions | Output Signal |
| --- | --- | --- |
| *L*-by-1 column vector, where *L* is a multiple of *M* and *M* is the number of frequency bands.  You can specify *M* using the **Number of frequency bands** parameter. | Clear the **Bands as separate output ports (Max. of 16 bands)** parameter | (*L*/*M*)-by-*M* |
| Select the **Bands as separate output ports (Max. of 16 bands)** parameter | The block outputs *M* narrowband signals of size (*L*/*M*)-by-1 at each of the *M* output ports.  If *M* > 16, the size of the narrowband signal at the last output port is (*L*/*M*)-by-(*M*−15). |
| *L*-by-1 column vector, where *L* is not a multiple of *M*  Select the **Allow arbitrary frame length for fixed-size input signals** parameter. If you do not select **Allow arbitrary frame length for fixed-size input signals**, the block errors. | Clear the **Bands as separate output ports (Max. of 16 bands)** parameter | `ceil`(*L*/*M*)-by-*M* |
| Select the **Bands as separate output ports (Max. of 16 bands)** parameter | The block outputs *M* narrowband signals of size `ceil`(*L*/*M*)-by-1 at each of the *M* output ports.  If *M* > 16, the size of the narrowband signal at the last output port is `ceil`(*L*/*M*)-by-(*M*−15). |
| *L*-by-*N* matrix, where *L* is a multiple of *M* | Clear the **Bands as separate output ports (Max. of 16 bands)** parameter | (*L*/*M*)-by-*M*-by-*N* |
| Select the **Bands as separate output ports (Max. of 16 bands)** parameter | The block outputs *M* narrowband signals of size (*L*/*M*)-by-*N* at each of the *M* output ports.  If *M* > 16, the size of the narrowband signal at the last output port is (*L*/*M*)-by-(*M*−15)-by-*N*. |
| *L*-by-*N* matrix, where *L* is not a multiple of *M*  Select the **Allow arbitrary frame length for fixed-size input signals** parameter. If you do not select **Allow arbitrary frame length for fixed-size input signals**, the block errors. | Clear the **Bands as separate output ports (Max. of 16 bands)** parameter | `ceil`(*L*/*M*)-by-*M*-by-*N* |
| Select the **Bands as separate output ports (Max. of 16 bands)** parameter | The block outputs *M* narrowband signals of size `ceil`(*L*/*M*)-by-*N* at each of the *M* output ports.  If *M* > 16, the size of the narrowband signal at the last output port is `ceil`(*L*/*M*)-by-(*M*−15)-by-*N*. |

This table provides more information on the dimensions of the output
signal when you input a variable-size input signal (where signal frame
size changes during simulation).

| Input Signal | Conditions | Output Signal |
| --- | --- | --- |
| *L*-by-1 column vector, where *L* is a multiple of *M* | Clear the **Bands as separate output ports (Max. of 16 bands)** parameter | (*L*/*M*)-by-*M* |
| Select the **Bands as separate output ports (Max. of 16 bands)** parameter | The block outputs *M* narrowband signals of size (*L*/*M*)-by-1 at each of the *M* output ports.  If *M* > 16, the size of the narrowband signal at the last output port is (*L*/*M*)-by-(*M*−15). |
| *L*-by-1 column vector, where *L* is not a multiple of *M*  The block ignores the **Allow arbitrary frame length for fixed-size input signals** parameter. | Clear the **Bands as separate output ports (Max. of 16 bands)** parameter | `ceil`(*L*/*M*)-by-*M* |
| Select the **Bands as separate output ports (Max. of 16 bands)** parameter | The block outputs *M* narrowband signals of size `ceil`(*L*/*M*)-by-1 at each of the *M* output ports.  If *M* > 16, the size of the narrowband signal at the last output port is `ceil`(*L*/*M*)-by-(*M*−15). |
| *L*-by-*N* matrix, where *L* is a multiple of *M* | Clear the **Bands as separate output ports (Max. of 16 bands)** parameter | (*L*/*M*)-by-*M*-by-*N* |
| Select the **Bands as separate output ports (Max. of 16 bands)** parameter | The block outputs *M* narrowband signals of size (*L*/*M*)-by-*N* at each of the *M* ports.  If *M* > 16, the size of the narrowband signal at the last output port is (*L*/*M*)-by-(*M*−15)-by-*N*. |
| *L*-by-*N* matrix, where *L* is not a multiple of *M*  The block ignores the **Allow arbitrary frame length for fixed-size input signals** parameter. | Clear the **Bands as separate output ports (Max. of 16 bands)** parameter | `ceil`(*L*/*M*)-by-*M*-by-*N* |
| Select the **Bands as separate output ports (Max. of 16 bands)** parameter | The block outputs *M* narrowband signals of size `ceil`(*L*/*M*)-by-*N* at each of the *M* output ports.  If *M* > 16, the size of the narrowband signal at the last output port is `ceil`(*L*/*M*)-by-(*M*−15)-by-*N*. |

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Number of frequency bands
  summary: Number of frequency bands 8 (default) | positive integer greater than 1
  group: ''
- name: DecimationFactor
  summary: Decimation factor Number of frequency bands (default) | positive integer
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
- name: Allow arbitrary frame length for fixed-size input signals
  summary: Allow arbitrary frame length for fixed-size input signals off (default) | on
  group: ''
- name: Bands as separate output ports (Max. of 16 bands)
  summary: Output frequency bands on separate output ports off (default) | on
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

If a parameter is listed as tunable, then you can change its value during
simulation.

### **Number of frequency bands** — Number of frequency bands `8` (default) | positive integer greater than 1

Specify the number of frequency bands *M* into which the
block separates the input broadband signal. This parameter indicates the FFT
length and the decimation factor used by the algorithm.

### **DecimationFactor** — Decimation factor `Number of frequency bands` (default) | positive integer

Specify the decimation factor *D* to one of these:

- `Number of
  frequency bands` –– When you change the value
  of the **Number of frequency bands** parameter,
  the decimation factor changes automatically. *(since R2024a)*
- Positive integer less than or equal to the number of frequency
  bands *M*.

If the decimation factor *D* equals the number of
frequency bands *M*, then the
*M*/*D* ratio equals 1, and the
channelizer is known as the maximally decimated channelizer.

If the *M*/*D* ratio is greater than
`1`, the output sample rate is different from the
channel spacing, and the channelizer is known as the non-maximally decimated
channelizer. If the ratio is an integer, the channelizer is known as the
integer-oversampled channelizer. If the ratio is not an integer, say 4/3,
the channelizer is known as the rationally oversampled channelizer. For more
details, see Algorithm.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

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
**Number of frequency bands** × **Number
of filter taps per frequency band**. For a given stopband
attenuation, increasing the number of taps per band narrows the transition
width of the filter. As a result, there is more usable bandwidth for each
frequency band, at the expense of increased computation.

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

When you select this parameter, the lowpass filter coefficients are input
through the **coeffs** port. When you clear this parameter,
the coefficients are specified on the block dialog through the
**Prototype lowpass filter coefficients**
parameter.

#### Dependencies

To enable this parameter, set **Polyphase filter
specification** to
`Coefficients`.

### **Prototype lowpass filter coefficients** — Coefficients of prototype lowpass filter `rcosdesign(0.25,6,8,'sqrt')` (default) | row vector

Coefficients of the prototype lowpass filter. The default value is the
coefficients vector that `rcosdesign(0.25,6,8,'sqrt')`
returns. There must be at least one coefficient per frequency band. If the
length of the lowpass filter is less than the number of frequency bands, the
block zero-pads the coefficients.

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

### **Allow arbitrary frame length for fixed-size input signals** — Allow arbitrary frame length for fixed-size input signals off (default) | on

Specify whether fixed-size input signals (whose size does not change
during simulation) can have an arbitrary frame length, where the frame
length does not have to be a multiple of the decimation factor. The block
uses this parameter setting only for fixed-size input signals and ignores
this parameter if the input has a variable-size.

When the input signal is a variable-size signal, the signal can have
arbitrary frame length, that is, the frame length does not have to be a
multiple of the decimation factor.

For fixed-size input signals, if you:

- Select the **Allow arbitrary frame length for
  fixed-size input signals** parameter, the frame
  length of the signal does not have to be a multiple of the
  decimation factor. If the input is not a multiple of the
  decimation factor, then the output is generally a variable-size
  signal. Therefore, to support arbitrary input size, the block
  must also support variable-size operations, which you can enable
  by selecting the **Allow arbitrary frame length for
  fixed-size input signals** parameter.
- Clear the **Allow arbitrary frame length for
  fixed-size input signals** parameter, the input
  frame length must be a multiple of the decimation factor.

### **Bands as separate output ports (Max. of 16 bands)** — Output frequency bands on separate output ports off (default) | on

*Since R2024a*

When you select this parameter, the block provides a separate output port
for each frequency band. The number of output ports equals
`min`(**Number of frequency bands**,
16). The block labels each output port as
**Band*`x`***, where
*x* can be a value in the range [1
`min`(**Number of frequency bands**,
16)].

For more information on the signal size on each output port, see the
**Output(s)** port description.

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

### R2024a: Output each narrowband signal at separate output port

When you select the **Bands as separate output ports (Max. of 16
bands)** parameter, the block outputs each narrowband signal at a
separate port. The block can output a maximum of 16 narrowband signals separately.
When you clear this parameter, the block concatenates all the narrowband signals to
form a single output array.

### R2024a: Specify decimation factor to equal the number of frequency bands

You can now set the **Decimation factor** parameter to
`Number of frequency bands`. When you change the value
of the **Number of frequency bands** parameter, the decimation
factor changes automatically.

Existing Simulink models using the Channelizer block continue to run in
R2024a.

### R2022b: Support for arbitrary input frame length

Channelizer block supports input signals with arbitrary frame lengths when the:

- Input signal is a fixed-size signal (frame length does not change
  during simulation) and you select the **Allow arbitrary frame
  length for fixed-size input signals** parameter
- Input signal is a variable-size signal (frame length changes during
  simulation)

The frame length is arbitrary when it is not a multiple of the decimation
factor.

## Description

Polyphase FFT analysis filter bank

The Channelizer block separates a broadband input signal into multiple
narrow subbands using an FFT-based analysis filter bank. The filter bank uses a
prototype lowpass filter and is implemented using a polyphase structure. You can specify
the filter coefficients directly or through design parameters. When you specify the
design parameters, the filter is designed using the `designMultirateFIR` function.

This block accepts variable-size inputs, so you can change the size of each input
channel during simulation. However, the number of channels cannot change.
