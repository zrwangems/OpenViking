---
type: simulink-block
title: 'Matched Filter'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: 'matchedfilter'
documentation_source_path: 'ref/matchedfilter.html'
language: en
---

# Matched Filter

## Ports
```yaml
ports:
- name: X
  summary: Input signal *M*-by-*N* complex valued matrix
  direction: input
  data_types: double
- name: Coeff
  summary: Matched filter coefficients *M*-length complex column vector
  direction: input
  data_types: double
- name: Y
  summary: Matched filter output *M*-by-*N* complex valued matrix
  direction: output
  data_types: double
- name: G
  summary: Matched-filter gain *N*-length real-valued
  direction: output
  data_types: double
```

### Input

### **X** — Input signal *M*-by-*N* complex valued matrix

Input signal, specified as an
*M*-by-*N* complex valued matrix.
Matched filtering is applied along the first dimension. The input
`X` and the output `Y` have
the same dimensions. The initial transient is removed from the filtered
result.

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

**Data Types:** `double`

### **Coeff** — Matched filter coefficients *M*-length complex column vector

Matched filter coefficients, specified as an
*M*-length complex column vector.

#### Dependencies

To enable this port, set the **Source of
coefficients** pull-down menu `Input
port`.

**Data Types:** `double`
### Output

### **Y** — Matched filter output *M*-by-*N* complex valued matrix

Matched filter output, returned as an
*M*-by-*N* complex valued matrix.
The dimensions of `Y` are the same as the dimensions
of `X`.

**Data Types:** `double`

### **G** — Matched-filter gain *N*-length real-valued

Matched-filter gain, returned as an *N* real-valued
matrix. Gain is computed for each column of `X`.
Units are in dB.

#### Dependencies

To enable this port, select the **Enable SNR gain
output** check box.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Source of coefficients
  summary: Source of matched filter coefficients Property (default) | Input port
  group: ''
- name: Coefficients
  summary: Matched filter coefficients [1;1] (default)
  group: ''
- name: Spectrum window
  summary: Window for spectrum weighting None (default) | Hamming | Chebyshev | Hann | Kaiser | Taylor
  group: ''
- name: Spectrum window range (Hz)
  summary: Spectrum window coverage region [0, 1e5] (default)
  group: ''
- name: Inherit sample rate
  summary: Inherit sample rate from upstream blocks on (default) | off
  group: ''
- name: Sample rate (Hz)
  summary: Sample rate of the output waveform 1e6 (default) | positive scalar
  group: ''
  block_parameter: SampleRate
  type: double
  values: positive scalar
  default: 1e6
- name: Sidelobe attenuation level
  summary: Window sidelobe attenuation level 30 (default)
  group: ''
- name: Kaiser shape parameter
  summary: Kaiser shape parameter 0.5 (default)
  group: ''
- name: Number of constant level sidelobes
  summary: Number of nearly constant sidelobes in Taylor window 4 (default)
  group: ''
- name: Enable SNR gain output
  summary: Enable SNR gain output off (default) | on
  group: ''
- name: Simulate using
  summary: Block simulation method Interpreted Execution (default) | Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution, Code Generation
  default: Interpreted Execution
```

### **Source of coefficients** — Source of matched filter coefficients `Property` (default) | `Input port`

Specify whether the matched filter coefficients come from
**Coefficients** or from an input port.

|  |  |
| --- | --- |
| `Property` | Matched filter coefficients are specified by **Coefficients**. |
| `Input port` | Matched filter coefficients are specified via the input port `Coeff`. |

### **Coefficients** — Matched filter coefficients `[1;1]` (default)

Specify the matched filter coefficients as a column vector. This parameter
appears when you set **Source of coefficients** to
`Property`.

### **Spectrum window** — Window for spectrum weighting `None` (default) | `Hamming` | `Chebyshev` | `Hann` | `Kaiser` | `Taylor`

Specify the window used for spectrum weighting using one of

|  |
| --- |
| `None` |
| `Hamming` |
| `Chebyshev` |
| `Hann` |
| `Kaiser` |
| `Taylor` |

Spectrum weighting is often used with linear FM waveforms to
reduce sidelobe levels in the time domain. The block computes the window
length internally to match the FFT length.

### **Spectrum window range (Hz)** — Spectrum window coverage region `[0, 1e5]` (default)

Specify the spectrum region, in hertz, on which the spectrum window is
applied as a 1-by-2 vector in the form of
`[StartFrequency,EndFrequency]`.

Note that both `StartFrequency` and
`EndFrequency` are measured in baseband. That is, they
are within `[-Fs/2,Fs/2]`, where `Fs` is
the sample rate specified in any of the waveform library blocks. The
parameter `StartFrequency` must be less than
`EndFrequency`.

#### Dependencies

This parameter appears when you set the **Spectrum
window** parameter to any value other than
`None`.

### **Inherit sample rate** — Inherit sample rate from upstream blocks on (default) | off

Select this parameter to inherit the sample rate from upstream blocks. Otherwise,
specify the sample rate using the **Sample rate (Hz)**
parameter.

**Data Types:** `Boolean`

### **Sample rate (Hz)** — Sample rate of the output waveform `1e6` (default) | positive scalar

Sample rate of the output waveform, specified as a positive scalar. The ratio of
**Sample rate (Hz)** to each element in the **Pulse
repetition frequency (Hz)** vector must be an integer. This restriction is
equivalent to requiring that the pulse repetition interval is an integral multiple of
the sample interval.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`SampleRate` |
| **Type:**double |
| **Values:**positive scalar |
| **Default:**`1e6` |

### **Sidelobe attenuation level** — Window sidelobe attenuation level `30` (default)

Specify the sidelobe attenuation level, in dB, of a Chebyshev or Taylor
window as a positive scalar.

#### Dependencies

This parameter appears when you set **Spectrum
window** to `Chebyshev` or
`Taylor`.

### **Kaiser shape parameter** — Kaiser shape parameter `0.5` (default)

Specify the parameter that affects the Kaiser window sidelobe attenuation as a
nonnegative scalar. Refer to the function `kaiser` for more
details.

#### Dependencies

This parameter appears when you set the **Spectrum
window** parameter to
`Kaiser`.

### **Number of constant level sidelobes** — Number of nearly constant sidelobes in Taylor window `4` (default)

Specify the number of nearly-constant-level sidelobes adjacent to the
mainlobe in a Taylor window as a positive integer.

#### Dependencies

This parameter appears when you set the **Spectrum
window** parameter to
`Taylor`.

### **Enable SNR gain output** — Enable SNR gain output off (default) | on

Select this check this box to obtain the matched filter SNR gain via the
output port `G`. The output port appears only when this box
is selected.

### **Simulate using** — Block simulation method `Interpreted Execution` (default) | `Code Generation`

Block simulation, specified as `Interpreted Execution` or
`Code Generation`. If you want your block to use the
MATLAB® interpreter, choose `Interpreted Execution`. If
you want your block to run as compiled code, choose `Code
Generation`. Compiled code requires time to compile but usually runs
faster.

Interpreted execution is useful when you are developing and tuning a model. The block
runs the underlying System object™ in MATLAB. You can change and execute your model quickly. When you are satisfied
with your results, you can then run the block using `Code
Generation`. Long simulations run faster with generated code than in
interpreted execution. You can run repeated executions without recompiling, but if you
change any block parameters, then the block automatically recompiles before
execution.

This table shows how the **Simulate using** parameter affects the
overall simulation behavior.

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

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimulateUsing` |
| **Type:** enum |
| **Values:** `Interpreted Execution`, `Code Generation` |
| **Default:** `Interpreted Execution` |
## Libraries

Phased Array System Toolbox / Detection

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Matched filter

The Matched Filter block implements matched filtering of an input signal. Matched filtering is an FIR filtering operation with the coefficients equal to the time reversed samples of the transmitted signal. The filter can improve SNR before detection.
