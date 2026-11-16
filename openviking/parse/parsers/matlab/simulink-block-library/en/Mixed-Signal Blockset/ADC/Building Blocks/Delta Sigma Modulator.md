---
type: simulink-block
title: 'Delta Sigma Modulator'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'ADC / Building Blocks'
documentation_page: 'deltasigmamodulator'
documentation_source_path: 'ref/deltasigmamodulator.html'
language: en
---

# Delta Sigma Modulator

## Ports

### Input

### **input** — Analog input signal scalar

Analog input signal, specified as a scalar.

**Data Types:** `double`

### **reset** — Reset delta-sigma modulator scalar

Reset signal for Delta Sigma Modulator block, specified as a
scalar.

**Data Types:** `double`

### **feedback** — Output from next stage scalar

Output from the next stage. Use this port to feed the output back into the block
when modeling a multistage DSM. If there is no feedback from the next stage, connect
this port to the ground.

Use this port to build cascaded DSM structures such as MASH and S-MASH.

**Data Types:** `double`
### Output

### **dsmOut** — Digital output signal scalar

Digital output signal, returned as a scalar.

**Data Types:** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **filterOut** — Output of loop filter scalar

The output of the loop filter inside the delta-sigma modulator, returned as a
scalar.

**Data Types:** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **quantOut** — Output of quantizer scalar

The output of the quantizer inside the delta-sigma modulator, returned as a
scalar. If you do not use this port, connect it to a terminator.

If you do not use the **feedback** port,
**quantOut** and **dsmOut** ports have the same
values.

Use this port to build cascaded DSM structures such as MASH and S-MASH.

**Data Types:** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **Delta Sigma Modulator architecture** — Architecture of delta-sigma modulator `CIFB` (default) | `CRFB` | `CIFF` | `CRFF`

Architecture of the delta-sigma modulator, specified as:

- `CIFB` — Cascade of feedback integrators
- `CRFB` — Cascade of feedback resonators
- `CIFF` — Cascade of feed-forward integrators
- `CRFF` — Cascade of feed-forward resonators

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `dsmArchitecture` |
| **Type:** character vector |
| **Values:** `CIFB` | `CRFB` | `CIFF` | `CRFF` |
| **Default:** `CIFB` |

### **Delta Sigma Modulator order** — Order of delta-sigma modulator `2nd order` (default) | `1st order` | `3rd order` | `4th order` | `5th order` | `6th order`

Order of the delta-sigma modulator. You can choose between orders one to six.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `dsmOrder` |
| **Type:** character vector |
| **Values:** `1st order` | `2nd order` | `3rd order` | `4th order` | `5th order` | `6th order` |
| **Default:** `2nd order` |

### Input Parameters

### **System bandwidth (Hz)** — Bandwidth of delta-sigma modulator system `1000` (default) | nonnegative real scalar

Bandwidth of the delta-sigma modulator system, specified as a nonnegative real
scalar.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `BandWidth` |
| **Type:** character vector |
| **Values:** nonnegative real scalar |
| **Default:** `1000` |

### **OSR** — Ratio of delta-sigma modulator sampling rate to Nyquist rate `64` (default) | nonnegative real scalar

Ratio of the delta-sigma modulator sampling rate to the Nyquist rate, specified as
a nonnegative real scalar. A high oversampling ratio results in a relaxed
anti-aliasing filter and reduced in-band quantization noise.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OSR` |
| **Type:** character vector |
| **Values:** nonnegative real scalar |
| **Default:** `64` |

### **Sampling frequency (Hz)** — Sampling frequency of delta-sigma modulator `128e3` (default) | positive real scalar

Sampling frequency of the delta-sigma modulator. This read-only parameter is
calculated from the **System bandwidth** and
**OSR** parameters.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SamplingFrequency` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `128e3` |

### **Quantizer levels** — Number of quantizer levels in delta-sigma modulator `2` (default) | positive real integer

Number of quantizer levels in the delta-sigma modulator, specified as a positive
real integer.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `NumberLevels` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `2` |

### **Quantizer output** — Range of quantizer output `[-1,1]` (default) | real-valued vector

Range of the quantizer output in the delta-sigma modulator architecture, returned
as a vector with real elements. This parameter is read-only.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `QuantizerOutput` |
| **Type:** character vector |
| **Values:** real valued vector |
| **Default:** `[-1;1]` |

### **Enable dynamic range scaling** — Enable dynamic range scaling of coefficients off (default) | on

Enable dynamic range scaling of coefficients. This prevents premature saturation
of internal states.

#### Dependencies

When this parameter is enabled, **Use custom coefficient
values** option is deselected.

### **Use custom coefficient values** — Option to use custom values for coefficients 'a', 'g', 'b', and 'c' off (default) | on

Use custom values for coefficients 'a', 'g', 'b', and 'c'.

#### Dependencies

When this parameter is enabled, **Enable dynamic range
scaling** option is deselected.

### **Coefficient 'a'** — Feedback/feed-forward coefficients from/to the quantizer `[0.1601 0.6515]` (default) | real-valued vector

Feedback coefficients from the quantizer or feed-forward coefficients to the
quantizer, specified as a vector with real elements.

#### Dependencies

To enable this parameter, select the **Use custom coefficient
values** parameter.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `a` |
| **Type:** character vector |
| **Values:** real valued vector |
| **Default:** `[0.1601 0.6515]` |

### **Coefficient 'g'** — Resonator coefficients `[0.0000]` (default) | real-valued vector

Resonator coefficients, specified as a vector with real elements.

#### Dependencies

To enable this parameter, select the **Use custom coefficient
values** parameter.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `g` |
| **Type:** character vector |
| **Values:** real valued vector |
| **Default:** `[0.0000]` |

### **Coefficient 'b'** — Feed-in coefficients from the modulator input to each integrator `[0.1601 0.6515 1.0000]` (default) | real-valued vector

Feed-in coefficients from the modulator input to each integrator, specified as a
vector with real elements.

#### Dependencies

To enable this parameter, select the **Use custom coefficient
values** parameter.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `b` |
| **Type:** character vector |
| **Values:** real valued vector |
| **Default:** `[0.1601 0.6515 1.0000]` |

### **Coefficient 'c'** — Integrator inter-stage coefficients `[1.0000 1.0000]` (default) | real-valued vector

Integrator inter-stage coefficients, specified as a vector with real
elements.

#### Dependencies

To enable this parameter, select the **Use custom coefficient
values** parameter.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `c` |
| **Type:** character vector |
| **Values:** real valued vector |
| **Default:** `[1.0000 1.0000]` |

### Impairment

### **Integrator opamp gain** — Open loop gain of op-amp `Inf` (default) | positive real scalar

Open loop gain of the internal op-amp, specified as a positive real scalar. This
parameter is used in the analysis of the noise transfer function (NTF). Ideal NTF
assumes that the op-amp gain is infinite.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OLgain` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `Inf` |

### **Enable Noise Impairment** — Enable noise calculations in delta-sigma modulator ADC off (default) | on

Enable noise calculations in the delta-sigma modulator ADC.

### **Thermal noise value** — Thermal noise density `200e-6` (default) | real scalar

Thermal noise density, specified in units of Vrms or
dB/Hz.

When you specify the thermal noise in units of Vrms, the
value of this parameter must be a nonnegative real scalar.

#### Dependencies

To enable this parameter, select the **Enable Noise
Impairment** parameter.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `thermalNoiseValue` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `0.125` |

### **Reference resistance (ohm)** — Reference resistance for power calculation `50` (default) | positive real scalar

Reference noise to use for power calculations, specified as a positive real scalar
in ohms.

#### Dependencies

To enable this parameter, select the **Enable Noise
Impairment** parameter.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `refResistance` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `50` |

### **1/f corner frequency (Hz)** — Corner frequency for flicker noise `1000` (default) | positive real scalar

Corner frequency for flicker (1/f) noise, specified as a positive real scalar in
Hz. At this frequency, the 1/f noise approximately equals the thermal noise.

#### Dependencies

To enable this parameter, select the **Enable Noise
Impairment** parameter.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `fcorner` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `1000` |

### Advanced

### **NTF zeros opitimization flag** — Method to optimize zeros in NTF `2` (default) | `0` | `1`

Method that the block uses to optimize the zeros in the NTF:

- `0` — Not optimized
- `1` — Optimized
- `2` — Optimized with at least one zero at the center
  of the band

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ntfOptim` |
| **Type:** character vector |
| **Values:** `0` | `1` | `2` |
| **Default:** `2` |

### **Modulator passband** — Type of modulator passband `Lowpass` (default) | `Bandpass`

Type of passband of the delta-sigma modulator.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `passbandType` |
| **Type:** character vector |
| **Values:** `Lowpass` | `Bandpass` |
| **Default:** `Lowpass` |

### **Center frequency** — Center frequency of modulator `0` (default) | scalar in the range [0 0.5]

Center frequency of the modulator, specified as a scalar in the range [0 0.5]. For
a lowpass filter, the center frequency is zero.

#### Dependencies

To enable this parameter, set the **Modulator passband**
parameter to `Bandpass`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `centerFrequency` |
| **Type:** character vector |
| **Values:** scalar in the range [0 0.5] |
| **Default:** `0` |

### **Use custom value of H\_inf** — Option to use custom value of H\_inf off (default) | on

Select this parameter to use custom values for H\_inf. By default, this option is
cleared.

### **Maximum out-of-band H\_inf** — Maximum out-of-band gain of NTF `1.4` (default) | positive real scalar

Maximum out-of-band gain of the NTF.

Lee’s rule states that *H\_inf* < 2 yields a stable modulator
with a binary quantizer. Reducing *H\_inf* increases the likelihood of
success, but reduces the magnitude of the attenuation provided by the NTF and the
theoretical resolution of the modulator.

#### Dependencies

To enable this parameter, select the **Use custom value of
H\_inf** parameter.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Hinf` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `1.4` |

**Note**

You need license to Control System Toolbox™ to use the parameters in the **Advanced** tab.

### Analysis

### **Noise transfer function (NTF)** — Plot NTF on (default) | off

Select to plot the noise transfer function (NTF) when you generate analyzed
plots.

### **NTF pole-zero plot** — Visualize pole and zero locations of NTF off (default) | on

Select to visualize the locations of the poles and zeros of the NTF when you
generate analyzed plots.

### **Signal transfer function (STF)** — Plot STF (default) |

Select to plot the signal transfer function (STF) when you generate analyzed
plots.

### **Predict SNR** — Predict SNR for binary modulators off (default) | on

Select to predict the signal-to-noise ratio (SNR) for binary modulators.

If the **Quantizer levels** is set to any other value than
`2`, this option is disabled.

### **Append plots** — Append plots to current figure off (default) | on

Select to append new analysis plots to current figure.

### **Generate analysis plots** — Plot selected analysis functions button

Plot the selected analysis functions: NTF, STF, NTF pole zero plot, and predicted
SNR.

### **Export analysis data to workspace** — Export analyzed data to base workspace off (default) | on

Select to export the analyzed data to base workspace as a structure. The structure
contains the NTF, STF, maximum SNR, and maximum stable amplitude (MSA).

To export the data, click the **Generate analysis plots**
button.

**Note**

You need a Control System Toolbox license to use the parameters in the **Analysis**
tab.

**Note**

The analysis results only include the effects of finite op-amp gain defined in the
**Integrator opamp gain** parameter. The block ignores the effects of
thermal noise while estimating the results in the **Analysis**
tab.

## Libraries

Mixed-Signal Blockset / ADC / Building Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

### R2024a: Plot NTF and STF

Plot noise transfer function (NTF), signal transfer function (STF), and predicted SNR
for binary modulators.

### R2023b: Generate Coefficients based on Over-Sampling Ratio and Bandwidth

Use dynamic range-scaling specifications to generate the delta-sigma modulator
coefficients *a*, *g*,
*b*, and *c* for use in
transistor-level designs.

## Description

ADC based on delta-sigma modulator

The Delta Sigma Modulator block models an ADC based on delta-sigma
modulator using four different sets of architectures.

- Cascade of resonators with feedback (CRFB)
- Cascade of integrators with feedback (CIFB)
- Cascade of resonators with feed-forward (CRFF)
- Cascade of integrators with feed-forward (CIFF)

You can model an DSM of orders from one to six. You can also use the block to design
cascaded structures such as multistage noise shaping (MASH) and sturdy MASH (S-MASH). You can
also model circuit based noise. You can plot the noise transfer function (NTF), signal
transfer function (STF), and predict the signal-to-noise ratio (SNR).
