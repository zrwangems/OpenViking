---
type: simulink-block
title: 'Range Doppler Response'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: 'rangedopplerresponse'
documentation_source_path: '../radar/../phased/ref/rangedopplerresponse.html'
language: en
---

# Range Doppler Response

## Ports

### Input

### **X** — Input complex-valued *K*-by-*L* matrix | *K*-by-*N*-by-*L* array

Input data, specified as a complex-valued
*K*-by-*L* matrix or
*K*-by-*N*-by-*L*
array where

- *K* denotes the number of fast-time
  samples.
- *N* denotes the number of channels such
  as beams or sensors. When *N* is one, only
  a single data channel is present.
- *L* denotes the number of pulses for
  matched-filter processing and the number of sweeps for FFT
  processing.

**Data Types:** `single` | `double`

### **Coeff** — Matched filter coefficients column vector

Matched filter coefficients, specified as a column vector.

#### Dependencies

To enable this port, set the **Range processing
method** to `Matched filter`.

**Data Types:** `single` | `double`

### **XRef** — Reference signal vector

Reference signal, specified as a

#### Dependencies

To enable this port, set the **Range processing
method** to `FFT` and then select the
**Dechirp input signal** check box.

**Data Types:** `double`

### **PRF** — Pulse repetition frequency positive scalar

Pulse repetition frequency, specified as a positive scalar.
`prf` must be less than or equal to the sample
rate specified in the `SampleRate` property divided
by the length of the first dimension of the input signal,
`x`. You can specify this argument as single or
double precision.

#### Dependencies

To enable this port, set the **Source of pulse repetition
frequency** drop down menu to `Input
port`.

**Data Types:** `double`
### Output

### **Resp** — Range-Doppler response complex

Range-Doppler, returned as a complex-valued
*M*-by-*P* matrix or an
*M*-by-*N*-by-*P*
array.

### **Range** — Range samples vector

Range samples at which the range-Doppler response is evaluated. The
output is a column vector of length *M*.

**Data Types:** `double`

### **Dop** — Doppler or speed samples vector

Doppler samples or speed samples at which the range-Doppler response is evaluated.
returned as a column vector of length *P*. Whether
`Dop` contains Doppler or speed samples depends
on the **Doppler output** parameter.

**Data Types:** `double`

## Parameters

### **Measurement mode** — Measurement mode `Monostatic` (default) | `Bistatic`

Measurement mode, specified as `Monostatic` or `Bistatic`. When set to `Monostatic`, the range measurement is the monostatic range. When set to `Bistatic`, the range measurement is the bistatic range.

**Example:** `Bistatic`

**Data Types:** `char` | `string`

### **Range processing method** — Range processing method `Matched filter` (default) | `FFT`

Specify the method of range processing as `Matched
filter` or `FFT`

|  |  |
| --- | --- |
| `Matched filter` | Applies a matched filter to the incoming signal. This technique is commonly used for pulsed signals, where the matched filter is the time reverse of the transmitted signal. Choosing this option creates the `Coeff` input port. |
| `FFT` | Performs range processing by applying an FFT to the input signal. This approach is commonly used with FMCW and linear FM pulsed signals. |

### **Propagation speed (m/s)** — Signal propagation speed `physconst('LightSpeed')` (default) | positive scalar

Signal propagation speed, specified as a real-valued positive scalar. The default
value of the speed of light is the value returned by
`physconst('LightSpeed')`.

**Data Types:** `double`

### **Inherit sample rate** — Inherit sample rate from upstream blocks on (default) | off

Select this parameter to inherit the sample rate from upstream blocks. Otherwise,
specify the sample rate using the **Sample rate (Hz)**
parameter.

**Data Types:** `Boolean`

### **Sample rate (Hz)** — Sampling rate of signal `1e6` (default) | positive real-valued scalar

Specify the signal sampling rate as a positive scalar. Units are in Hz.

#### Dependencies

To enable this parameter, clear the **Inherit sample rate** check
box.

**Data Types:** `double`

### **Reference range (m)** — Reference range `0` (default)

Specify the reference range of the range grid as a nonnegative scalar.

- If you set the **Range processing method**
  parameter to `Matched filter`, the
  reference range is set to the start of the range grid.
- If you set the **Range processing method**
  property to `FFT`, the reference range
  depends on the **Set reference range at
  center** check box.

  - When you select the **Set reference range
    at center** check box, the reference
    range is set to the center of the range grid.
  - If you do not select the **Set reference
    range at center** check box, the
    reference range is set to the start of the range
    grid.

  Units are in meters.

### **Source of pulse repetition frequency** — Source of pulse repetition frequency `Auto` (default) | `Property` | `Input port`

Specify the source of pulse repetition frequency as

- `Auto` — automatically compute
  the pulse repetition frequency (PRF). The PRF is the sample rate
  of the signal divided by the number of rows in the input port
  signal, `X`.
- `Property`— specify the pulse
  repetition frequency using the `PRF`
  parameter.
- `Input port`— specify the PRF
  using the `PRF` input port.

Use the `Property` or
`Input port` option when the pulse repetition
frequency cannot be determined by the signal duration, as is the case with
range-gated data.

### **Pulse repetition frequency of the input signal (Hz)** — Pulse repetition frequency of the input signal `10e3` (default)

Specify the pulse repetition frequency of the input signal as a positive
scalar. `PRF` must be less than or equal to the sample
rate divided by the number of rows of the input signal. When the signal
length is variable, use the maximum possible number of rows of the input
signal instead.

#### Dependencies

To enable this parameter, set the **Source of pulse repetition
frequency** parameter to
`Property`.

### **Source of FFT length in Doppler processing** — Source of FFT length in Doppler processing `Auto` (default) | `Property`

Specify how the block determines the length of the FFT used in Doppler
processing. Values of this parameter are

|  |  |
| --- | --- |
| `Auto` | The FFT length equals the number of rows of the input signal. |
| `Property` | The **FFT length in Doppler processing** parameter of this block specifies the FFT length. |

### **FFT length in Doppler processing** — FFT length in Doppler processing `1024`

Specify the length of the FFT used in Doppler processing as a positive
integer.

#### Dependencies

This parameter appears only when you set **Source of FFT
length in Doppler processing** to
`Property`.

### **Doppler processing window** — Doppler processing window `None` (default) | `Hamming` | `Chebyshev` | `Hann` | `Kaiser` | `Taylor`

Specify the window used for Doppler processing using one of

|  |
| --- |
| `None` |
| `Hamming` |
| `Chebyshev` |
| `Hann` |
| `Kaiser` |
| `Taylor` |

If you set this parameter to
`Taylor`, the generated Taylor window has four
nearly-constant sidelobes adjacent to the mainlobe.

### **Doppler sidelobe attenuation level** — Doppler sidelobe attenuation level `30` (default)

Specify the sidelobe attenuation level as a positive scalar, in
decibels.

#### Dependencies

This parameter appears only when **Doppler processing
window** is set to `Kaiser`,
`Chebyshev`, or
`Taylor`.

### **Doppler output** — Doppler output `Frequency` (default) | `Range rate` | `Speed`

Doppler domain output, returned in the **Dop** output port. Output types can be
`Frequency`, `Range
rate`, or `Speed`.

|  |  |
| --- | --- |
| `Frequency` | **Dop** is the Doppler shift. Units are in Hz. |
| `Range rate` | **Dop** is the corresponding radial range rate which is negative as the target approaches the radar. Units are in meters per second. |
| `Speed` | **Dop** is the radial speed which is positive as the target approaches the radar. Units are in meters per second. |

#### Dependencies

To set this parameter to `"Speed"`, set the
`Mode` parameter to
`"Monostatic"`.

### **Signal carrier frequency (Hz)** — Signal carrier frequency `3e8` (default) | positive scalar

Signal carrier frequency, specified as a positive scalar. Units are in Hz.

**Data Types:** `double`

### **FM sweep slope (Hz/s)** — FM sweep slope `1e9` (default)

Specify the slope of the linear FM sweeping, in hertz per second, as a
scalar.

#### Dependencies

This parameter appears only when you set **Range processing
method** to `FFT`.

### **Dechirp input signal** — Dechirp input signal off (default) | on

Select this check box to make the block perform the dechirp operation on
the input signal. Clear this check box to indicate that the input signal is
already dechirped and no dechirp operation is necessary.

#### Dependencies

This check box appears only when you set **Range processing
method** to `FFT`.

### **Source of FFT length in range processing** — Source of FFT length in range processing `Auto` (default) | `Property`

Specify how the block determines the FFT length in range processing.
Values of this parameter are

|  |  |
| --- | --- |
| `Auto` | The FFT length equals the number of rows of the input signal. |
| `Property` | The FFT length is specified by **FFT length in range processing**. |

#### Dependencies

This parameter appears only when you set **Range processing
method** to `FFT`.

### **FFT length in range processing** — FFT length in range processing `1024` (default)

Specify the FFT length in the range domain as a positive integer.

#### Dependencies

This parameter appears only when you set **Range processing
method** to `FFT` and
**Source of FFT length in range processing** to
`Property`.

### **Range processing window** — Range processing window `None` (default) | `Hamming` | `Chebyshev` | `Hann` | `Kaiser` | `Taylor`

Specify the window used for range processing using one of

|  |
| --- |
| `None` |
| `Hamming` |
| `Chebyshev` |
| `Hann` |
| `Kaiser` |
| `Taylor` |

If you set this parameter to
`Taylor`, the generated Taylor window has four
nearly-constant sidelobes adjacent to the mainlobe.

#### Dependencies

This parameter appears only when you set **Range processing
method** to `FFT`.

### **Set reference range at center** — Set reference range at center on (default) | off

Set reference range at the center of range grid, specified as
`on` or `off`. Selecting this check
box, enables you to set the reference range at the center of the range grid.
Otherwise, the reference range is set to the beginning of the range
grid.

### **Range sidelobe attenuation level** — Range sidelobe attenuation level `30` (default)

Specify the sidelobe attenuation level as a positive scalar, in
decibels.

#### Dependencies

This parameter appears only when you set **Range processing
method** to `FFT` and
**Range processing window** to
`Kaiser`,
`Chebyshev`, or
`Taylor`.

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

Range-Doppler response

The Range-Doppler Response block computes the range-Doppler map of an input signal. The output response is a matrix whose rows represent range gates and whose columns represent Doppler bins.
