---
type: simulink-block
title: 'Sine Wave Generator (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'sinewavegeneratorthreephase'
documentation_source_path: 'ref/sinewavegeneratorthreephase.html'
language: en
---

# Sine Wave Generator (Three-Phase)

## Ports
```yaml
ports:
- name: mag
  summary: Magnitude of generated three-phase sine wave scalar
  direction: input
- name: ang
  summary: Phase shift of the generated three-phase sine wave, deg scalar
  direction: input
- name: freq
  summary: Frequency of generated three-phase sine wave, Hz scalar
  direction: input
- name: abc
  summary: Three-phase sine wave vector
  direction: output
- name: wt
  summary: Angle of sine wave of all three phases, rad vector
  direction: output
```

### Input

### **mag** — Magnitude of generated three-phase sine wave scalar

Magnitude of the generated three-phase sine wave, specified as a
scalar.

### **ang** — Phase shift of the generated three-phase sine wave, deg scalar

Phase shift for phase *a* of the generated
three-phase sine wave, specified as a scalar in degrees.

### **freq** — Frequency of generated three-phase sine wave, Hz scalar

Frequency of the generated three-phase sine wave, specified as a
scalar in Hz.
### Output

### **abc** — Three-phase sine wave vector

Three-phase sine wave, returned as a Simulink signal vector.

### **wt** — Angle of sine wave of all three phases, rad vector

Angle of all three phases of the sine wave, returned as a Simulink
signal vector in rad.
## Parameters
```yaml
parameters:
- name: Sample time (-1 for inherited)
  summary: Block sample time -1 (default) | 0 | positive scalar
  group: ''
```

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | `0` | positive scalar

Time between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

For inherited discrete-time operation, set this parameter to `-1`.
For discrete-time operation, set this parameter to a positive integer. For
continuous-time operation, set this parameter to `0`.

If this block is in a masked subsystem or a variant subsystem that supports switching
between continuous operation and discrete operation, promote this parameter to ensure
correct switching between the continuous and discrete implementations of the block. For
more information, see Promote Block Parameters on a Mask.
## Libraries

Simscape / Electrical / Control / General Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Discrete-time or continuous-time three-phase sine wave generator

The Sine Wave Generator (Three-Phase) block generates a
balanced three-phase sine wave from magnitude, phase shift, and frequency inputs.
