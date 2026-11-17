---
type: simulink-block
title: 'Induction Machine Scalar Control'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Induction Machine Control'
documentation_page: 'inductionmachinescalarcontrol'
documentation_source_path: 'ref/inductionmachinescalarcontrol.html'
language: en
---

# Induction Machine Scalar Control

## Ports
```yaml
ports:
- name: fRef
  summary: Frequency scalar
  direction: input
  data_types: single | double
- name: Vabc
  summary: Voltage vector
  direction: output
  data_types: single | double
```

### Input

### **fRef** — Frequency scalar

Reference electrical frequency.

**Example:** Example

**Data Types:** `single` | `double`
### Output

### **Vabc** — Voltage vector

Reference phase voltages.

**Example:** Example

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Rated electrical frequency (Hz)
  summary: Frequency 60 (default) | positive scalar
  group: ''
- name: Rated voltage (V)
  summary: Voltage 550 (default) | positive and greater than the value of the Minimum voltage (V) parameter
  group: ''
- name: Minimum voltage (V)
  summary: Voltage 10 (default) | zero or positive
  group: ''
- name: Sample time (-1 for inherited)
  summary: Block sample time -1 (default) | positive scalar
  group: ''
```

### **Rated electrical frequency (Hz)** — Frequency `60` (default) | positive scalar

Nominal frequency.

### **Rated voltage (V)** — Voltage `550` (default) | positive and greater than the value of the **Minimum voltage (V)** parameter

Nominal voltage.

### **Minimum voltage (V)** — Voltage `10` (default) | zero or positive

Lower bound for the voltage.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | positive scalar

Time, in s, between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

If this block is inside a triggered subsystem, inherit the
sample time by setting this parameter to `-1`. If this block is in a
continuous variable-step model, specify the sample time explicitly using a positive
scalar.
## Libraries

Simscape / Electrical / Control / Induction Machine Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Induction machine V/f control

The Induction Machine Scalar Control block implements an induction
machine scalar, that is V/f or V/Hz, control structure. The diagram shows the open-loop
V/f control structure that the block implements.

### Equations

The Induction Machine Scalar Control block computes the magnitude
of the stator voltage based on the reference frequency, fs\*, as:

Vs\*=(Vn−Vminfn−fmin)fs\*,

where:

- *Vn* is the rated
  voltage.
- *Vmin* is the minimum
  voltage.
- *fn* is the rated electrical
  frequency.
- *fmin* is the minimum
  frequency.

The voltage components in the stationary reference frame are:

Vα=Vs\*cos(2πfs\*t)

and

Vβ=Vs\*sin(2πfs\*t).

The block obtains *Vabc* from
*Vα* and
*Vβ* by using an inverse Clarke
transformation.
