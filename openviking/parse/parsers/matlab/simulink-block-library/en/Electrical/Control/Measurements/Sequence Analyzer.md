---
type: simulink-block
title: 'Sequence Analyzer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Measurements'
documentation_page: 'sequenceanalyzer'
documentation_source_path: 'ref/sequenceanalyzer.html'
language: en
---

# Sequence Analyzer

## Ports
```yaml
ports:
- name: u
  summary: Periodic input signal vector
  direction: input
- name: mag
  summary: Magnitude scalar | vector
  direction: output
- name: angle
  summary: Phase shift scalar | vector
  direction: output
```

### Input

### **u** — Periodic input signal vector

Periodic input signal, specified as a vector of three elements.
### Output

### **mag** — Magnitude scalar | vector

Magnitude of the positive, negative, or zero sequence. Depending on the harmonic
numbers, this output is a scalar or a vector.

### **angle** — Phase shift scalar | vector

Phase shift, in degrees, of the positive, negative, or zero sequence. Depending on the
harmonic numbers, this output is a scalar or a vector.
## Parameters
```yaml
parameters:
- name: Base frequency (Hz)
  summary: Base frequency 60 (default)
  group: ''
- name: Harmonic numbers
  summary: Harmonic numbers [1 2] (default) | scalar or vector
  group: ''
- name: Sequence
  summary: Sequence selection Positive (default) | Negative | Zero
  group: ''
- name: Sample Time (s)
  summary: Block sample time 0 (default)
  group: ''
```

### **Base frequency (Hz)** — Base frequency `60` (default)

Base frequency of the input signal in Hz.

### **Harmonic numbers** — Harmonic numbers `[1 2]` (default) | scalar or vector

Scalar or vector of the harmonic numbers. `1` stands for
base frequency and `2` is the second harmonic.

### **Sequence** — Sequence selection `Positive` (default) | `Negative` | `Zero`

Select whether the magnitude and phase of the sequence is positive,
negative or zero.

### **Sample Time (s)** — Block sample time `0` (default)

Time between consecutive block executions. During execution, the block
produces outputs and, if appropriate, updates its internal state. For more
information, see What Is Sample Time? and
Specify Sample Time.

For inherited discrete-time operation, specify `-1`. For
discrete-time operation, specify a positive integer. For continuous-time
operation, specify `0`.

If this block is in a masked subsystem, or other variant subsystem that
allows you to switch between continuous operation and discrete operation,
promote the sample time parameter. Promoting the sample time parameter
ensures correct switching between the continuous and discrete
implementations of the block. For more information, see Promote Block Parameters on a Mask.
## Libraries

Simscape / Electrical / Control / Measurements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Calculate the magnitude and phase of the positive, negative, or zero sequence of a three-phase signal

The Sequence Analyzer block takes a three-phase signal (usually voltage) as the input and
outputs the magnitude and phase of the positive, negative, or zero sequence.

The input signals are first converted to phasor representation based on the base frequency
and harmonic specified in the block mask. The block then transforms the phasor into a
sequence of components..

You can represent the zero, positive, and negative sequence components with
*V0*,
*V1*,
*V2* in phasor representation;
*Va*,
*Vb*,
*Vc* are the voltage of three phases. The
sequence components are computed as:

[V0V1V2]=13[1111aa21a2a2][VaVbVc]

where a=ej23π.
