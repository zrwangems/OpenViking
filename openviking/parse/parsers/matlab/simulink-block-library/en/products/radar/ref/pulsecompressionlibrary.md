---
type: simulink-block
title: 'Pulse Compression Library'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: 'Signal and Data Processing / Detection, Range, Angle, and Doppler Estimation'
documentation_page: 'pulsecompressionlibrary'
documentation_source_path: 'ref/pulsecompressionlibrary.html'
language: en
---

# Pulse Compression Library

## Ports

### Input

### **X** — Input signal complex-valued *K*-by-*L* matrix | complex-valued *K*-by-*N* matrix | complex-valued *K*-by-*N*-by-*L* array

Input signal, specified as a complex-valued
*K*-by-*L* matrix, complex-valued
*K*-by-*N* matrix, or a
complex-valued
*K*-by-*N*-by-*L*
array. *K* denotes the number of fast time samples,
*L* the number of pulses, and *N*
is the number of channels. Channels can be array elements or
beams.

**Data Types:** `double`
**Complex Number Support:** Yes

### **Idx** — Index of processing specification positive integer

Index of the processing specification in the pulse compression
library, specified as a positive integer.

**Data Types:** `double`
### Output

### **Y** — Output signal complex-valued *K*-by-*L* matrix | complex-valued *K*-by-*N* matrix | complex-valued *K*-by-*N*-by-*L* array

Output signal, returned as a complex-valued
*M*-by-*L* matrix, complex-valued
*M*-by-*N* matrix, or a
complex-valued
*M*-by-*N*-by-*L*
array. *M* denotes the number of fast time samples,
*L* the number of pulses, and *N*
is the number of channels. Channels can be array elements or beams. The
number of dimensions of `Y` matches the number of
dimensions of `X`.

When matched filtering is performed, *M* is equal to
the number of rows in `X`. When stretch processing is
performed and you specify a value for the
`RangeFFTLength` name-value pair,
*M* is set to the value of
`RangeFFTLength`. When you do not specify
`RangeFFTLength`, *M* is equal to
the number of rows in `X`.

**Data Types:** `double`
**Complex Number Support:** Yes

### **Range** — Sample range real-valued length-*M* vector

Sample ranges, returned as a real-valued length-*M*
vector where *M* is the number of rows of
`Y`. Elements of this vector denote the ranges
corresponding to the rows of `Y`.

**Data Types:** `double`

## Parameters

### **Signal propagation speed (m/s)** — Signal propagation speed `physconst('LightSpeed')` (default) | real-valued positive scalar

Signal propagation speed, specified as a real-valued positive scalar. The default value of the
speed of light is the value returned by `physconst('LightSpeed')`.
Units are in meters per second.

**Example:** `3e8`

**Data Types:** `double`

### **Specification of each waveform in the library** — Specification of pulse waveforms in the library `{{'Rectangular','PRF',1e4,'PulseWidth',50e-6},{'LinearFM','PRF',1e4,'PulseWidth',50e-6,'SweepBandwidth',1e5,'SweepDirection','Up','SweepInterval','Positive'}}` (default) | cell array

Pulse waveforms, specified as a cell array. Each cell of the array
contains the specification of one waveform. Each waveform specification is
also a cell array containing the parameters of the
waveform.

```
{{Waveform 1 Specification},{Waveform 2 Specification},{Waveform 3 Specification}, ...}
```

This
block supports four built-in waveforms and also lets you specify custom
waveforms. Each built-in waveform specifier consists of a waveform
identifier followed by several name-value pairs that set the properties of
the waveform.

**Built-in Waveforms**

|  |  |  |
| --- | --- | --- |
| Waveform type | Waveform identifier | Waveform name-value pair arguments |
| Linear FM | `'LinearFM'` | See Linear FM Waveform Arguments |
| Phase coded | `'PhaseCoded'` | See Phase-Coded Waveform Arguments |
| Rectangular | `'Rectangular'` | See Rectangular Waveform Arguments |
| Stepped FM | `'SteppedFM'` | See Stepped FM Waveform Arguments |

You can create a custom waveform with a user-defined function. The first
input argument of the function must be the sample rate. Use a function
handle instead of the waveform identifier in the first cell of a waveform
specification. The remaining cells contain all function input arguments
except the sample rate. Specify all input arguments in the order they are
passed into the function. The function must have at least one output
argument to return the samples of each pulse in a column vector. You can
only create custom waveforms when you set **Simulate
using** to `Interpreted
Execution`.

### **Pulse compression specifications** — Specify type of pulse compression `{{'MatchedFilter','SpectrumWindow','None'},{'StretchProcessor','RangeSpan',200,'ReferenceRange',5e3,'RangeWindow','None'}}` (default) | cell array

Waveform processing type and parameters, specified as a cell array of
processing specifications. Each processing specification is itself a cell
array containing the processing type and processing
arguments.

```
{{Processing 1 Specification},{Processing 2 Specification},{Processing 3 Specification}, ...}
```

Each
processing specification indicates which type of processing to apply to a
waveform and the arguments needed for
processing.

```
{processtype,Name,Value,...}
```

The
value of `processtype` is either
`'MatchedFilter'` or
`'StretchProcessor'`.

- `'MatchedFilter'` – The name-value pair
  arguments are

  - `'Coefficients'`,`coeff`
    – specifies the matched filter coefficients,
    `coeff`, as a column vector.
    When not specified, the coefficients are calculated
    from the `WaveformSpecification`
    property. For the Stepped FM waveform containing
    multiple pulses, `coeff`
    corresponds to each pulse until the pulse index,
    `idx` changes.
  - `'SpectrumWindow'`,`sw`
    – specifies the spectrum weighting window,
    `sw`, applied to the waveform.
    Window values are one of `'None'`,
    `'Hamming'`,
    `'Chebyshev'`,
    `'Hann'`,
    `'Kaiser'`, and
    `'Taylor'`. The default value is
    `'None'`.
  - `'SidelobeAttenuation'`,`slb`
    – specifies the sidelobe attenuation window,
    `slb`, of the Chebyshev or
    Taylor window as a positive scalar. The default
    value is 30. This parameter applies when you set
    `'SpectrumWindow'` to
    `'Chebyshev'` or
    `'Taylor'`.
  - `'Beta'`,`beta`
    – specifies the parameter,
    `beta`, that determines the
    Kaiser window sidelobe attenuation as a nonnegative
    scalar. The default value is 0.5. This parameter
    applies when you set
    `'SpectrumWindow'` to
    `'Kaiser'`.
  - `'Nbar'`,`nbar`
    – specifies the number of nearly constant level
    sidelobes, `nbar`, adjacent to
    the main lobe in a Taylor window as a positive
    integer. The default value is 4. This parameter
    applies when you set
    `'SpectrumWindow'` to
    `'Taylor'`.
  - `'SpectrumRange'`,`sr`
    – specifies the spectrum region,
    `sr`, on which the spectrum
    window is applied as a 1-by-2 vector having the form
    `[StartFrequency EndFrequency]`.
    The default value is [0 1.0e5]. This parameter
    applies when you set the
    `'SpectrumWindow'` to any value
    other than 'None'. Units are in Hz.

    Both `StartFrequency` and
    `EndFrequency` are measured in
    the baseband region [-*Fs*/2
    *Fs*/2]. *Fs* is
    the sample rate specified by the
    `SampleRate` property.
    `StartFrequency` cannot be larger
    than `EndFrequency`.
- `'StretchProcessor'` – The name-value pair
  arguments are

  - `'ReferenceRange'`,`refrng`
    – specifies the center of ranges of interest,
    `refrng`, as a positive scalar.
    The `refrng` must be within the
    unambiguous range of one pulse. The default value is
    5000. Units are in meters.
  - `'RangeSpan'`,`rngspan`
    – specifies the span of the ranges of interest.
    `rngspan`, as a positive scalar.
    The range span is centered at the range value specified
    in the `'ReferenceRange'` parameter.
    The default value is 500. Units are in meters.
  - `'RangeFFTLength'`,`len`
    – specifies the FFT length in the range domain,
    `len`, as a positive integer. If
    not specified, the default value is same as the input
    data length.
  - `'RangeWindow'`,`rw`
    specifies the window used for range processing,
    `rw`, as one of
    `'None'`,
    `'Hamming'`,
    `'Chebyshev'`,
    `'Hann'`,
    `'Kaiser'`, and
    `'Taylor'`. The default value is
    `'None'`.

**Data Types:** `cell`

### **Inherit sample rate** — Inherit sample rate from upstream blocks on (default) | off

Select this parameter to inherit the sample rate from upstream
blocks. Otherwise, specify the sample rate using the **Sample
rate (Hz)** parameter.

**Data Types:** `Boolean`

### **Sample rate (Hz)** — Sampling rate of signal `1e6` (default) | positive real-valued scalar

Specify the signal sampling rate as a positive scalar. Units
are in Hz.

#### Dependencies

To enable this parameter, clear the **Inherit sample rate** check box.

**Data Types:** `double`

### **Simulate using** — Block simulation method `Interpreted Execution` (default) | `Code Generation`

Block simulation, specified as `Interpreted Execution` or `Code
Generation`. If you want your block to use the MATLAB® interpreter,
choose `Interpreted Execution`. If you want
your block to run as compiled code, choose `Code Generation`.
Compiled code requires time to compile but usually runs faster.

Interpreted execution is useful when you are developing and tuning a model. The block runs the
underlying System object™ in MATLAB. You can change and execute your model quickly. When you are satisfied
with your results, you can then run the block using `Code
Generation`. Long simulations run faster with generated code than in
interpreted execution. You can run repeated executions without recompiling, but if you
change any block parameters, then the block automatically recompiles before
execution.

This table shows how the **Simulate using** parameter affects the overall
simulation behavior.

When the Simulink® model is in `Accelerator` mode, the block mode specified
using **Simulate using** overrides the simulation mode.

**Acceleration Modes**

|  |  |  |  |
| --- | --- | --- | --- |
| Block Simulation | Simulation Behavior | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | The block executes using the MATLAB interpreter. | The block executes using the MATLAB interpreter. | Creates a standalone executable from the model. |
| `Code Generation` | The block is compiled. | All blocks in the model are compiled. |

For more information, see Choosing a Simulation Mode (Simulink).

## Libraries

Radar Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Library of pulse compression specifications

The Pulse Compression Library block performs range processing using
pulse compression. Pulse compression techniques include matched filtering and stretch
processing. The block lets you create a library of different pulse compression
specifications. The output is the filter response consisting of a matrix or a
three-dimensional array with rows representing range gates.
