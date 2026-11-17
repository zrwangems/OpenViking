---
type: simulink-block
title: 'FM Demodulator Passband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Analog Passband Modulation'
documentation_page: 'fmdemodulatorpassband'
documentation_source_path: 'ref/fmdemodulatorpassband.html'
language: en
---

# FM Demodulator Passband

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
- name: Carrier frequency (Hz)
  summary: Carrier frequency in Hz 300 (default) | positive scalar
  group: ''
- name: Initial phase (rad)
  summary: Initial phase offset in radians 0 (default) | scalar
  group: ''
- name: Frequency deviation (Hz)
  summary: Frequency deviation of carrier frequency in Hz 50 (default) | scalar
  group: ''
- name: Hilbert transform filter order (must be even)
  summary: Hilbert transform filter order 100 (default) | positive scalar
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Carrier frequency (Hz)** — Carrier frequency in Hz `300` (default) | positive scalar

Carrier frequency in Hz, specified as a positive scalar.

Due to the implementation of the Hilbert transform by means of a filter, for best
results, choose a carrier frequency, *f*c, that
exceeds the sample rate of the input signal by at least 10%.

Typically, an appropriate carrier frequency is a much higher
than the highest frequency of the input signal. By the Nyquist sampling theorem, 1 / *T*s > (2 ×
*f*c), where *T*s represents the sample time
of the input signal. For more information, see Baseband vs. Passband Simulation.

### **Initial phase (rad)** — Initial phase offset in radians `0` (default) | scalar

Initial phase offset of the carrier in radians, specified as a scalar.

### **Frequency deviation (Hz)** — Frequency deviation of carrier frequency in Hz `50` (default) | scalar

Frequency deviation of the carrier frequency in Hz, specified as a scalar. Also know as
the *variation* in the frequency.

### **Hilbert transform filter order (must be even)** — Hilbert transform filter order `100` (default) | positive scalar

Hilbert transform filter order, specified as an even, positive scalar with a value
greater than `2`. This parameter value defines the length of the FIR filter
used to compute the Hilbert transform.
## Libraries

Communications Toolbox / Modulation / Analog Baseband Modulation

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Demodulate FM-modulated data

The FM Demodulator Passband block demodulates a signal that was modulated using frequency
modulation. Both the input and output signals are real scalar signals.
