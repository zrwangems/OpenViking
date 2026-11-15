---
type: simulink-block
title: 'Continuous Time Delta Sigma Modulator'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Data Converters'
documentation_page: 'continuoustimedeltasigmamodulator'
documentation_source_path: 'ref/continuoustimedeltasigmamodulator.html'
language: en
---

# Continuous Time Delta Sigma Modulator

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

### **Delta Sigma Modulator architecture** — Architecture of delta-sigma modulator `CIFB` (default) | `CIFF`

Architecture of the delta-sigma modulator, specified as:

- `CIFB` — Cascade of feedback integrators
- `CIFF` — Cascade of feed-forward integrators

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `dsmArchitecture` |
| **Type:** character vector |
| **Values:** `CIFB` | `CIFF` |
| **Default:** `CIFB` |

### **Delta Sigma Modulator order** — Order of delta-sigma modulator `2nd order` (default) | `1st order` | `3rd order` | `4th order`

Order of the delta-sigma modulator. You can choose between orders one to
four.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `dsmOrder` |
| **Type:** character vector |
| **Values:** `1st order` | `2nd order` | `3rd order` | `4th order` |
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

### **Use custom coefficient values** — Option to use custom values for coefficients 'a', 'g', 'b', and 'c' off (default) | on

Use custom values for coefficients 'a', 'g', 'b', and 'c'.

### **Coefficient 'a'** — Feedback/feed-forward coefficients from/to the quantizer `[0.5714 0.1601]` (default) | real-valued vector

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
| **Default:** `[0.5714 0.1601]` |

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

### **Coefficient 'b'** — Feed-in coefficients from the modulator input to each integrator `[1.000 0.5714 0.1601]` (default) | real-valued vector

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
| **Default:** `[1.000 0.5714 0.1601]` |

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

You need a Control System Toolbox™ license to use the parameters in the **Advanced**
tab.

## Libraries

Mixed-Signal Blockset / ADC / Building Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

ADC based on continuous-time delta-sigma modulator

The Continuous Time Delta Sigma Modulator block models an ADC based on
continuous-time delta-sigma modulator using two different sets of architectures.

- Cascade of integrators with feedback (CIFB)
- Cascade of integrators with feed-forward (CIFF)

You can model a continuous-time DSM of orders from one to four. You can also use the block
to design cascaded structures such as multistage noise shaping (MASH) and sturdy MASH
(S-MASH).
