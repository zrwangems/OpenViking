---
type: simulink-block
title: 'DSBSC AM Modulator Passband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Analog Passband Modulation'
documentation_page: 'dsbscammodulatorpassband'
documentation_source_path: 'ref/dsbscammodulatorpassband.html'
language: en
---

# DSBSC AM Modulator Passband

## Ports
```yaml
ports:
- name: In
  summary: Input signal scalar
  direction: input
  data_types: double
- name: Out
  summary: Output signal scalar
  direction: output
  data_types: double
```

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
```yaml
parameters:
- name: Carrier frequency (Hz)
  summary: Carrier frequency in Hz 300 (default) | positive scalar
  group: ''
- name: Initial phase (rad)
  summary: Initial phase offset in radians 0 (default) | scalar
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Carrier frequency (Hz)** — Carrier frequency in Hz `300` (default) | positive scalar

Carrier frequency in Hz, specified as a positive scalar.

Typically, an appropriate carrier frequency is a much higher
than the highest frequency of the input signal. By the Nyquist sampling theorem, 1 / *T*s > (2 ×
*f*c), where *T*s represents the sample time
of the input signal. For more information, see Baseband vs. Passband Simulation.

### **Initial phase (rad)** — Initial phase offset in radians `0` (default) | scalar

Initial phase offset of the carrier in radians, specified as a scalar.
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

Modulate using double-sideband suppressed-carrier amplitude modulation

The DSBSC AM Modulator Passband block modulates a signal using double-sideband
suppressed-carrier amplitude modulation. Both the input and output signals are real scalar
signals.
