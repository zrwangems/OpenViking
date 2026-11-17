---
type: simulink-block
title: 'SM PSS7C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smpss7c'
documentation_source_path: 'ref/smpss7c.html'
language: en
---

# SM PSS7C

## Ports
```yaml
ports:
- name: V_SI1
  summary: Speed, frequency, or power scalar
  direction: input
  data_types: single | double
- name: V_SI2
  summary: Electrical power scalar
  direction: input
  data_types: single | double
- name: V_ST
  summary: Stabilization speed, frequency, or power scalar
  direction: output
  data_types: single | double
```

### Input

### **V\_SI1** — Speed, frequency, or power scalar

Per-unit speed, frequency of the terminal bus voltage, compensated frequency, or
electrical power, specified as a scalar.

**Data Types:** `single` | `double`

### **V\_SI2** — Electrical power scalar

Per-unit electrical power, specified as a scalar.

**Data Types:** `single` | `double`
### Output

### **V\_ST** — Stabilization speed, frequency, or power scalar

Automatic voltage regulator input stabilization signal, as limited by
*VST\_min* and
*VST\_max*, returned as a
scalar.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Power system stabilizer main gain, K_S1 (pu)
  summary: Power system stabilizer forward path gain 50 (default) | scalar
  group: ''
- name: Power system stabilizer gain, K_S2 (pu)
  summary: Power system stabilizer transducer gain 0.7052 (default) | scalar
  group: ''
- name: Power system stabilizer gain, K_S3 (pu)
  summary: Power system stabilizer gain 1 (default) | scalar
  group: ''
- name: PSS transducer time constant, T_6 (s)
  summary: Transducer time constant 6 0 (default) | scalar
  group: ''
- name: PSS transducer time constant, T_7 (s)
  summary: Transducer time constant 7 10 (default) | scalar
  group: ''
- name: PSS washout time constant, T_w1 (s)
  summary: Washout time constant 1 10 (default) | scalar
  group: ''
- name: PSS washout time constant, T_w2 (s)
  summary: Washout time constant 2 10 (default) | scalar
  group: ''
- name: PSS washout time constant, T_w3 (s)
  summary: Washout time constant 3 10 (default) | scalar
  group: ''
- name: PSS washout time constant, T_w4 (s)
  summary: Washout time constant 4 0 (default) | scalar
  group: ''
- name: PSS transducer time constant, T_8 (s)
  summary: Transducer time constant 8 0.5 (default) | scalar
  group: ''
- name: PSS washout time constant, T_9 (s)
  summary: Washout time constant 9 0.1 (default) | scalar
  group: ''
- name: Denominator exponent for ramp-track filter, M
  summary: Exponent of denominator of the ramp-track filter 5 (default) | scalar
  group: ''
- name: Overall exponent for ramp-track filter, N
  summary: Overall exponent of ramp-track filter 1 (default) | scalar
  group: ''
- name: PSS canonical gain 0, K_0 (pu)
  summary: Power system stabilizer canonical gain 0 0.399 (default) | scalar
  group: ''
- name: PSS canonical gain 1, K_1 (pu)
  summary: Power system stabilizer canonical gain 1 1.8462 (default) | scalar
  group: ''
- name: PSS canonical gain 2, K_2 (pu)
  summary: Power system stabilizer canonical gain 2 0.4231 (default) | scalar
  group: ''
- name: PSS canonical gain 3, K_3 (pu)
  summary: Power system stabilizer canonical gain 3 0.2104 (default) | scalar
  group: ''
- name: PSS canonical gain 4, K_4 (pu)
  summary: Power system stabilizer canonical gain 4 0 (default) | scalar
  group: ''
- name: PSS third block gain, K_i3 (pu)
  summary: Power system stabilizer third block gain 1 (default) | scalar
  group: ''
- name: PSS fourth block gain, K_i4 (pu)
  summary: Power system stabilizer fourth block gain 0 (default) | scalar
  group: ''
- name: PSS time constant (first block), T_i1 (s)
  summary: Power system stabilizer time constant for the first block 0.03 (default) | scalar
  group: ''
- name: PSS time constant (second block), T_i2 (s)
  summary: Power system stabilizer time constant for the second block 0.0293 (default) | scalar
  group: ''
- name: PSS time constant (third block), T_i3 (s)
  summary: Power system stabilizer time constant for the third block 0.2804 (default) | scalar
  group: ''
- name: PSS time constant (fourth block), T_i4 (s)
  summary: Power system stabilizer time constant for the fourth block 1 (default) | scalar
  group: ''
- name: Maximum PSS output, V_STmax (pu)
  summary: Maximum stabilization 0.05 (default) | scalar
  group: ''
- name: Minimum PSS output, V_STmin (pu)
  summary: Minimum stabilization -0.05 (default) | scalar
  group: ''
- name: 'Input signal #1 maximum limit, V_S1max (pu)'
  summary: Maximum limit for the first input 2 (default) | scalar
  group: ''
- name: 'Input signal #1 minimum limit, V_S1min (pu)'
  summary: Minimum limit for the first input -2 (default) | scalar
  group: ''
- name: 'Input signal #2 maximum limit, V_S2max (pu)'
  summary: Maximum limit for the second input 2 (default) | scalar
  group: ''
- name: 'Input signal #2 minimum limit, V_S2min (pu)'
  summary: Minimum limit for the second input -2 (default) | scalar
  group: ''
- name: Generator MW threshold for PSS activation, P_PSSon (pu)
  summary: Generator threshold for power system stabilizer activation 0 (default) | scalar
  group: ''
- name: Generator MW threshold for PSS de-activation, P_PSSoff (pu)
  summary: Generator threshold for power system stabilizer deactivation 0 (default) | scalar
  group: ''
- name: Sample time (-1 for inherited)
  summary: Block sample time -1 (default) | 0 | positive scalar
  group: ''
```

### **Power system stabilizer main gain, K\_S1 (pu)** — Power system stabilizer forward path gain 50 (default) | scalar

Power system stabilizer forward path gain.

### **Power system stabilizer gain, K\_S2 (pu)** — Power system stabilizer transducer gain 0.7052 (default) | scalar

Power system stabilizer transducer gain.

### **Power system stabilizer gain, K\_S3 (pu)** — Power system stabilizer gain 1 (default) | scalar

Power system stabilizer gain.

### **PSS transducer time constant, T\_6 (s)** — Transducer time constant 6 `0` (default) | scalar

Transducer time constant 6, associated with the block labeled Low-Pass Filter in the
diagram.

### **PSS transducer time constant, T\_7 (s)** — Transducer time constant 7 `10` (default) | scalar

Transducer time constant 7, associated with the block labeled Low-Pass Filter1 in the
diagram.

### **PSS washout time constant, T\_w1 (s)** — Washout time constant 1 `10` (default) | scalar

Washout time constant 1, associated with the block labeled Washout1 in the
diagram.

### **PSS washout time constant, T\_w2 (s)** — Washout time constant 2 `10` (default) | scalar

Washout time constant 2, associated with the block labeled Washout2 in the
diagram.

### **PSS washout time constant, T\_w3 (s)** — Washout time constant 3 `10` (default) | scalar

Washout time constant 3, associated with the block labeled Washout3 in the
diagram.

### **PSS washout time constant, T\_w4 (s)** — Washout time constant 4 `0` (default) | scalar

Washout time constant 4, associated with the block labeled Washout4 in the
diagram.

### **PSS transducer time constant, T\_8 (s)** — Transducer time constant 8 `0.5` (default) | scalar

Transducer time constant 8.

### **PSS washout time constant, T\_9 (s)** — Washout time constant 9 `0.1` (default) | scalar

Washout time constant 9.

### **Denominator exponent for ramp-track filter, M** — Exponent of denominator of the ramp-track filter `5` (default) | scalar

Denominator exponent for the ramp-track filter.

### **Overall exponent for ramp-track filter, N** — Overall exponent of ramp-track filter `1` (default) | scalar

Overall exponent for the ramp-track filter.

### **PSS canonical gain 0, K\_0 (pu)** — Power system stabilizer canonical gain 0 0.399 (default) | scalar

Power system stabilizer canonical gain 0 for the Multi-band
subsystem.

### **PSS canonical gain 1, K\_1 (pu)** — Power system stabilizer canonical gain 1 1.8462 (default) | scalar

Power system stabilizer canonical gain 1 for the Multi-band
subsystem.

### **PSS canonical gain 2, K\_2 (pu)** — Power system stabilizer canonical gain 2 0.4231 (default) | scalar

Power system stabilizer canonical gain 2 for the Multi-band
subsystem.

### **PSS canonical gain 3, K\_3 (pu)** — Power system stabilizer canonical gain 3 0.2104 (default) | scalar

Power system stabilizer canonical gain 3 for the Multi-band
subsystem.

### **PSS canonical gain 4, K\_4 (pu)** — Power system stabilizer canonical gain 4 0 (default) | scalar

Power system stabilizer canonical gain 4 for the Multi-band
subsystem.

### **PSS third block gain, K\_i3 (pu)** — Power system stabilizer third block gain 1 (default) | scalar

Power system stabilizer third block gain for the Multi-band
subsystem.

### **PSS fourth block gain, K\_i4 (pu)** — Power system stabilizer fourth block gain 0 (default) | scalar

Power system stabilizer fourth block gain for the Multi-band
subsystem.

### **PSS time constant (first block), T\_i1 (s)** — Power system stabilizer time constant for the first block 0.03 (default) | scalar

Power system stabilizer time constant for the first block inside the
Multi-band subsystem.

### **PSS time constant (second block), T\_i2 (s)** — Power system stabilizer time constant for the second block 0.0293 (default) | scalar

Power system stabilizer time constant for the second block inside the
Multi-band subsystem.

### **PSS time constant (third block), T\_i3 (s)** — Power system stabilizer time constant for the third block 0.2804 (default) | scalar

Power system stabilizer time constant for the third block inside the
Multi-band subsystem.

### **PSS time constant (fourth block), T\_i4 (s)** — Power system stabilizer time constant for the fourth block 1 (default) | scalar

Power system stabilizer time constant for the fourth block inside the
Multi-band subsystem.

### **Maximum PSS output, V\_STmax (pu)** — Maximum stabilization `0.05` (default) | scalar

Maximum power system stabilizer output to the automatic voltage regulator (AVR).

### **Minimum PSS output, V\_STmin (pu)** — Minimum stabilization `-0.05` (default) | scalar

Minimum power system stabilizer output to the automatic voltage regulator (AVR).

### **Input signal #1 maximum limit, V\_S1max (pu)** — Maximum limit for the first input `2` (default) | scalar

Maximum signal value for the first stabilizer input.

### **Input signal #1 minimum limit, V\_S1min (pu)** — Minimum limit for the first input `-2` (default) | scalar

Minimum signal value for the first stabilizer input.

### **Input signal #2 maximum limit, V\_S2max (pu)** — Maximum limit for the second input `2` (default) | scalar

Maximum signal value for the second stabilizer input.

### **Input signal #2 minimum limit, V\_S2min (pu)** — Minimum limit for the second input `-2` (default) | scalar

Minimum signal value for the second stabilizer input.

### **Generator MW threshold for PSS activation, P\_PSSon (pu)** — Generator threshold for power system stabilizer activation `0` (default) | scalar

Generator threshold for power system stabilizer activation.

### **Generator MW threshold for PSS de-activation, P\_PSSoff (pu)** — Generator threshold for power system stabilizer deactivation `0` (default) | scalar

Generator threshold for power system stabilizer deactivation.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | 0 | positive scalar

Time between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

For inherited discrete-time operation, set the sample time to `-1`.
For discrete-time operation, set the sample time to a positive scalar. For
continuous-time operation, set the sample time to `0`.
## Libraries

Simscape / Electrical / Control / SM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Discrete-time or continuous-time single input PSS7C power system stabilizer

The SM PSS7C block implements a double-input PSS7C power system stabilizer
(PSS) that maintains rotor angle stability in a synchronous machine (SM) in conformance
with IEEE 421.5-2016[1].
Typically, you use a PSS to enhance the damping of power system oscillations through
excitation control.

You can represent two different types of dual-input power system stabilizers with this same model:

- A stabilizer that uses electrical power and speed (or frequency) signals
  to calculate the integral of the accelerating power. This make the
  calculated stabilizer signal insensitive to mechanical changes.
- A stabilizer that uses a combination of electrical power and either speed
  or frequency. To achieve the desired stabilizing signal shaping, the system
  uses the speed directly, without phase-lead compensation, and adds a signal
  that is proportional to the electrical power.

You can switch between continuous and discrete implementations of the block by using the
**Sample time (-1 for inherited)** parameter. To configure the
integrator for continuous time, set the **Sample time (-1 for
inherited)** property to `0`. To configure the integrator
for discrete time, set the **Sample time (-1 for inherited)** property
to a positive, nonzero value, or to `-1` to inherit the sample time
from an upstream block.

This diagram illustrates the overall structure of the PSS7C power system
stabilizer:

In the diagram:

- *V\_SI1* and *V\_SI2* are the two power
  system stabilizer inputs. Commonly used inputs are speed, frequency, or
  power.
- Two Washout (Discrete or Continuous) blocks
  are represented for each stabilizer input, with time constants
  *TW1* to
  *TW4*, along with a
  transducer, represented by a Low-Pass Filter (Discrete or Continuous), with
  time constants *T6* and
  *T7*.
- To allow a ramp-tracking filter characteristic, the Ramp Tracking Filter
  subsystem models a network of lead-lag and low-pass filter blocks in
  series.
- To provide phase compensation, the Multi-band subsystem implements a
  canonical state equation, with time constants
  *Ti1* to
  *Ti4* and gains
  *K0* to
  *K4*.
- The PSS output logic subsystem allows the representation of the PSS output
  logic associated with the generator active power output.
  *PPSSon* and
  *PPSSoff* are the threshold
  values used to define a hysteresis.
