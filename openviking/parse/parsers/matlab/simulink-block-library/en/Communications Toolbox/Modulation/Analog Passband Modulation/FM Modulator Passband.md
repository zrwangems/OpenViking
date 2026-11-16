---
type: simulink-block
title: 'FM Modulator Passband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Analog Passband Modulation'
documentation_page: 'fmmodulatorpassband'
documentation_source_path: 'ref/fmmodulatorpassband.html'
language: en
---

# FM Modulator Passband

## Ports

### Input

### **In** — Input signal scalar

Input signal, specified as a scalar.

This port is unnamed on the block.

**Data Types:** `double`
### Output

### **Out** — Output signal scalar

Output signal, returned as a scalar. The output is a passband representation of the
modulated signal.

This port is unnamed on the block.

**Data Types:** `double`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Carrier frequency (Hz)** — Carrier frequency in Hz `300` (default) | positive scalar

Carrier frequency in Hz, specified as a positive scalar. Match the carrier frequency,
*f*c, to the corresponding FM
Demodulator Passband block.

Typically, an appropriate carrier frequency is a much higher
than the highest frequency of the input signal. By the Nyquist sampling theorem, 1 / *T*s > (2 ×
*f*c), where *T*s represents the sample time
of the input signal. For more information, see Baseband vs. Passband Simulation.

### **Initial phase (rad)** — Initial phase offset in radians `0` (default) | scalar

Initial phase offset of the carrier in radians, specified as a scalar.

### **Frequency deviation (Hz)** — Frequency deviation of carrier frequency in Hz `50` (default) | scalar

Frequency deviation of the carrier frequency in Hz, specified as a scalar. Also known as
the *variation* in the frequency.

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

Modulate using frequency modulation

The FM Modulator Passband block modulates a signal using frequency modulation. The
output is a passband representation of the modulated signal. The frequency of the output signal
varies with the amplitude of the input signal. Both the input and output signals are real scalar
signals.
