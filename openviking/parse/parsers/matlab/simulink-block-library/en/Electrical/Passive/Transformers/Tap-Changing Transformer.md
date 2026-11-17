---
type: simulink-block
title: 'Tap-Changing Transformer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Transformers'
documentation_page: 'tapchangingtransformer'
documentation_source_path: 'ref/tapchangingtransformer.html'
language: en
---

# Tap-Changing Transformer

## Ports
```yaml
ports:
- name: 1+
  summary: Line 1 positive terminal electrical
  direction: conserving
- name: 1-
  summary: Line 1 negative terminal electrical
  direction: conserving
- name: 2+
  summary: Line 2 positive terminal electrical
  direction: conserving
- name: 2-
  summary: Line 2 negative terminal electrical
  direction: conserving
- name: c
  summary: Control input physical
  direction: conserving
```

### Conserving

### **1+** — Line 1 positive terminal electrical

Electrical conserving port associated with the positive terminal of
line 1.

### **1-** — Line 1 negative terminal electrical

Electrical conserving port associated with the negative terminal of
line 1.

### **2+** — Line 2 positive terminal electrical

Electrical conserving port associated with the positive terminal of
line 2.

### **2-** — Line 2 negative terminal electrical

Electrical conserving port associated with the negative terminal of
line 2.

### **c** — Control input physical

Input physical signal that specifies the input control value.
## Parameters
```yaml
parameters:
- name: Turns ratio (primary/secondary)
  summary: Turns ratio 1 (default) | positive number
  group: Nominal
- name: Primary leakage inductance
  summary: Line 1 leakage inductance 1e-6 H (default) | positive number
  group: Nominal
- name: Secondary leakage inductance
  summary: Line 2 leakage inductance 1e-6 H (default) | positive number
  group: Nominal
- name: Core-loss resistance
  summary: Mutual resistance 1e6 Ohm (default) | zero or positive number
  group: Nominal
- name: Magnetization inductance
  summary: Magnetization inductance 100e-6 H (default) | positive number
  group: Nominal
- name: Primary series resistance
  summary: Line 1 series resistance 0 Ohm (default) | zero or positive number
  group: Nominal
- name: Secondary series resistance
  summary: Line 2 series resistance 0 Ohm (default) | zero or positive number
  group: Nominal
- name: Primary leakage conductance
  summary: Line 1 leakage conductance 0 1/Ohm (default) | zero or positive number
  group: Nominal
- name: Secondary leakage conductance
  summary: Line 2 leakage conductance 0 1/Ohm (default) | zero or positive number
  group: Nominal
- name: Tap-changer location
  summary: Tap-changer winding Primary (default) | Secondary
  group: Tap
- name: Minimum tap index (nominal=0)
  summary: Minimum tap position -5 (default) | zero or negative integer
  group: Tap
- name: Maximum tap index (nominal=0)
  summary: Maximum tap position 5 (default) | zero or positive integer
  group: Tap
- name: Change per tap (%)
  summary: Tap change step 1 % (default) | positive number
  group: Tap
- name: Control threshold
  summary: Shift threshold 0.5 (default)
  group: Tap
```

### Nominal

### **Turns ratio (primary/secondary)** — Turns ratio `1` (default) | positive number

Turns ratio of the transformer in the nominal tap position. The turns
ratio is defined as the primary number of turns divided by the secondary
number of turns.

### **Primary leakage inductance** — Line 1 leakage inductance `1e-6` `H` (default) | positive number

Leakage inductance of the primary winding.

### **Secondary leakage inductance** — Line 2 leakage inductance `1e-6` `H` (default) | positive number

Leakage inductance of the secondary winding.

### **Core-loss resistance** — Mutual resistance `1e6` `Ohm` (default) | zero or positive number

Mutual resistance of the transformer.

### **Magnetization inductance** — Magnetization inductance `100e-6` `H` (default) | positive number

Magnetization inductance of the transformer.

### **Primary series resistance** — Line 1 series resistance `0` `Ohm` (default) | zero or positive number

Series resistance of the primary winding.

### **Secondary series resistance** — Line 2 series resistance `0` `Ohm` (default) | zero or positive number

Series resistance of the secondary winding.

### **Primary leakage conductance** — Line 1 leakage conductance `0` `1/Ohm` (default) | zero or positive number

Leakage conductance of the primary winding. Set this value to be
nonzero for achieving numerical convergence in some circuit
topologies.

### **Secondary leakage conductance** — Line 2 leakage conductance `0` `1/Ohm` (default) | zero or positive number

Leakage conductance of the secondary winding. Set this value to be
nonzero for achieving numerical convergence in some circuit
topologies.

### Tap

### **Tap-changer location** — Tap-changer winding `Primary` (default) | `Secondary`

Specify whether the tap-changer is on the primary or secondary winding.

### **Minimum tap index (nominal=0)** — Minimum tap position `-5` (default) | zero or negative integer

Minimum allowable position of the tap-changer.

### **Maximum tap index (nominal=0)** — Maximum tap position `5` (default) | zero or positive integer

Maximum allowable position of the tap-changer.

### **Change per tap (%)** — Tap change step `1` `%` (default) | positive number

Percent change in the number of turns per tap position step of the
tap-changer winding. Set this value such that the absolute percent
change at the minimum and maximum tap indices is less than
`100`
`%`.

### **Control threshold** — Shift threshold `0.5` (default)

Control value at which the tap changes position. To lower the tap
position, apply a control signal **c** smaller than the
negative of this value. To increase the tap position, apply a control
signal **c** greater than this value.
## Libraries

Simscape / Electrical / Passive / Transformers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Single-phase tap-changing transformer

The Tap-Changing Transformer block represents a single-phase
tap-changing transformer. You can vary the turns-ratio of the transformer during the
simulation using the control input.

Use this component to regulate or change the output voltage of a linear transformer during a
simulation. To model the effects of saturation, consider using the Nonlinear Transformer block.

### Operating Principle

Use the control input **c** to change the tap position of the transformer.

- Increase **c** above the **Control
  threshold**, *t*, to increase the tap
  position *p* by one.
- Decrease **c** below the negative of the
  **Control threshold** to decrease the tap position
  *p* by one.

This figure shows the tap-response to a control input.

In the diagram:

- *N0* is the nominal number of
  turns for the tap-changer winding.
- *δ* is the percent change in turns per tap position
  step. Specify this value using the **Change per tap
  (%)** parameter.
- *pmin* and
  *pmax* are the minimum
  and maximum allowable tap indices. Specify these values with the
  **Minimum tap index (nominal=0)** and
  **Maximum tap index (nominal=0)**
  parameters.

To select the tap-changer winding, use the **Tap-changer
location** parameter. The overall turns ratio, *n*,
depends on this location:

- `Primary`

  n=Np(N0,δ,p)Ns=n0(1+δp100)
- `Secondary`

  n=NpNs(N0,δ,p)=n0(1+δp100)−1

where *n0* is the nominal
turns ratio for the transformer.

### Equivalent Circuit

The equivalent circuit is shown in the diagram.

Here:

- *Rp* and
  *Rs* are the primary and
  secondary series resistances, respectively. Changes in the tap position
  affect these values.
- *Llp* and
  *Lls* are the primary
  and secondary leakage inductances, respectively. Changes in the tap
  position affect these values.
- *Rm* and *M*
  are the magnetization resistance and inductance, respectively. Changes
  in the tap position affect these values.
- *n* is the turns ratio of the transformer.
- *Gp* and
  *Gs* are the primary and
  secondary leakage conductances, respectively. Changes in the tap
  position do not affect these values.
