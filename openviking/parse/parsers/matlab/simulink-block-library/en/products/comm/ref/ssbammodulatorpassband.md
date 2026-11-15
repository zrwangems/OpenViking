---
type: simulink-block
title: 'SSB AM Modulator Passband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Analog Passband Modulation'
documentation_page: 'ssbammodulatorpassband'
documentation_source_path: 'ref/ssbammodulatorpassband.html'
language: en
---

# SSB AM Modulator Passband

## Ports

### Input

### **In** — Input signal scalar

Input signal, specified as a scalar.

This port is unnamed on the block.

**Data Types:** `double`
### Output

### **Out** — Output signal scalar

Output signal, returned as a scalar. The output is a passband
representation of the modulated signal.

This port is unnamed on the block.

**Data Types:** `double`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Carrier frequency (Hz)** — Carrier frequency in Hz `300` (default) | positive scalar

Carrier frequency in Hz, specified as a positive scalar.

Due to the implementation of the Hilbert transform by means of a filter,
for best results, choose a carrier frequency,
*f*c, that exceeds the sample
rate of the input signal by at least 10%. For more information, see Hilbert Transform Filter.

Typically, an appropriate carrier frequency is a much higher
than the highest frequency of the input signal. By the Nyquist sampling theorem, 1 / *T*s > (2 ×
*f*c), where *T*s represents the sample time
of the input signal. For more information, see Baseband vs. Passband Simulation.

### **Initial phase (rad)** — Initial phase offset in radians `0` (default) | scalar

Initial phase offset of the modulated signal in radians, specified as a
scalar.

### **Sideband to modulate** — Sideband to modulate `Upper` (default) | `Lower`

Sideband to modulate, specified as `Upper` or
`Lower`.

### **Hilbert Transform filter order (must be even)** — Hilbert transform filter order `100` (default) | positive scalar

Hilbert transform filter order, specified as an even, positive scalar with
a value greater than `2`. This parameter value defines the
length of the FIR filter used to compute the Hilbert transform.

## Libraries

Communications Toolbox / Modulation / Analog Passband Modulation

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Modulate using single-sideband amplitude modulation

The SSB AM Modulator Passband block modulates a signal using single-sideband
amplitude modulation with a Hilbert transform filter. Both the input and output signals
are real scalar signals.
