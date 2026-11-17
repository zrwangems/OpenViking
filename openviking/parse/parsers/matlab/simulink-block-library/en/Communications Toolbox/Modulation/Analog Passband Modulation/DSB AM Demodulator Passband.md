---
type: simulink-block
title: 'DSB AM Demodulator Passband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Analog Passband Modulation'
documentation_page: 'dsbamdemodulatorpassband'
documentation_source_path: 'ref/dsbamdemodulatorpassband.html'
language: en
---

# DSB AM Demodulator Passband

## Ports
```yaml
ports:
- name: In
  summary: Input signal scalar
  direction: input
  data_types: double
- name: Out
  summary: Demodulated output signal scalar
  direction: output
  data_types: double
```

### Input

### **In** — Input signal scalar

Input signal, specified as a scalar. The input is a passband representation of the
modulated signal.

This port is unnamed on the block.

**Data Types:** `double`
### Output

### **Out** — Demodulated output signal scalar

Demodulated output signal, returned as a scalar.

This port is unnamed on the block.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Input signal offset
  summary: Input signal offset factor 1 (default) | scalar
  group: ''
- name: Carrier frequency (Hz)
  summary: Carrier frequency in Hz 300 (default) | positive scalar
  group: ''
- name: Initial phase (rad)
  summary: Initial phase offset in radians 0 (default) | scalar
  group: ''
- name: Lowpass filter design method
  summary: Design method for lowpass filter Butterworth (default) | Chebyshev type I | Chebyshev type II | Elliptic
  group: ''
- name: Filter order
  summary: Order of lowpass filter 4 (default) | positive scalar
  group: ''
- name: Cutoff frequency
  summary: Cutoff frequency in Hz 300 (default) | positive scalar
  group: ''
- name: Passband ripple (dB)
  summary: Peak-to-peak passband ripple in dB 0.1 (default) | positive scalar
  group: ''
- name: Stopband ripple (dB)
  summary: Peak-to-peak stopband ripple in dB 0.1 (default) | positive scalar
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Input signal offset** — Input signal offset factor `1` (default) | scalar

Input signal offset factor, *k*, specified as a scalar. This value
should be greater than or equal to the absolute value of the minimum of the input
signal. Set this parameter to the input signal offset value in the corresponding DSB AM
Modulator Passband block.

### **Carrier frequency (Hz)** — Carrier frequency in Hz `300` (default) | positive scalar

Carrier frequency in Hz, specified as a positive scalar. Match the carrier
frequency, *f*c, to the corresponding DSB AM
Modulator Passband block.

Typically, an appropriate carrier frequency is a much higher
than the highest frequency of the input signal. By the Nyquist sampling theorem, 1 / *T*s > (2 ×
*f*c), where *T*s represents the sample time
of the input signal. For more information, see Baseband vs. Passband Simulation.

### **Initial phase (rad)** — Initial phase offset in radians `0` (default) | scalar

Initial phase offset of the carrier in radians, specified as a scalar.

### **Lowpass filter design method** — Design method for lowpass filter `Butterworth` (default) | `Chebyshev type I` | `Chebyshev type II` | `Elliptic`

Design method for the lowpass filter, specified as
`Butterworth`
`Chebyshev type I`, `Chebyshev type
II`, or `Elliptic`.

### **Filter order** — Order of lowpass filter `4` (default) | positive scalar

Order of the lowpass filter, specified as a positive scalar in the range [1, 500].
This parameter value defines the order of the filter specified by the **Lowpass filter design
method** parameter.

### **Cutoff frequency** — Cutoff frequency in Hz `300` (default) | positive scalar

Cutoff frequency in Hz, specified as a positive scalar. This parameter value defines
the cutoff frequency of the filter specified by the **Lowpass filter design
method** parameter.

### **Passband ripple (dB)** — Peak-to-peak passband ripple in dB `0.1` (default) | positive scalar

Peak-to-peak passband ripple in dB, specified as a positive scalar.

#### Dependencies

To enable this parameter, set **Lowpass filter design
method** to `Chebyshev type I` or
`Elliptic`.

### **Stopband ripple (dB)** — Peak-to-peak stopband ripple in dB `0.1` (default) | positive scalar

Peak-to-peak stopband ripple in dB, specified as a positive scalar.

#### Dependencies

To enable this parameter, set **Lowpass filter design
method** or `Chebyshev type II` or
`Elliptic`.
## Libraries

Communications Toolbox / Modulation / Analog Passband Modulation

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

## Description

Demodulate DSB-AM-modulated data

The DSB AM Demodulator Passband block demodulates a signal that was modulated using
double-sideband amplitude modulation. The block uses the envelope detection method. The input
is a passband representation of the modulated signal. Both the input and output signals are
real scalar signals.
