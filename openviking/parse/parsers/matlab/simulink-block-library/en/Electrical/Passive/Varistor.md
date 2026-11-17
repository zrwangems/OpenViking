---
type: simulink-block
title: 'Varistor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'varistor'
documentation_source_path: 'ref/varistor.html'
language: en
---

# Varistor

## Ports
```yaml
ports:
- name: +
  summary: Positive terminal electrical
  direction: conserving
- name: '-'
  summary: Negative terminal electrical
  direction: conserving
```

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the varistor positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the varistor negative
terminal.
## Parameters
```yaml
parameters:
- name: Parameterization
  summary: Varistor operation mode Linear (default) | Power-law
  group: ''
- name: Clamping voltage
  summary: Threshold voltage 260 (default) | positive number
  group: ''
- name: Off resistance
  summary: Low-voltage resistance 3e8 (default) | positive number
  group: ''
- name: On resistance
  summary: High-voltage resistance 1 (default) | positive number
  group: ''
- name: Leakage to normal voltage transition
  summary: First threshold voltage 130 (default) | positive number
  group: ''
- name: Normal to upturn voltage transition
  summary: Second threshold voltage 300 (default) | positive number
  group: ''
- name: Leakage-mode resistance
  summary: Low-voltage resistance 3e8 (default) | positive number
  group: ''
- name: Normal-mode power-law exponent
  summary: Mid-voltage resistance 45 (default) | positive number
  group: ''
- name: Upturn-mode resistance
  summary: High-voltage resistance 0.07 (default) | positive number
  group: ''
- name: Terminal resistance
  summary: Terminal resistance 100e-6 (default) | non-negative number
  group: ''
- name: Capacitance
  summary: Parallel capacitance 4.4 (default) | non-negative number
  group: ''
```

### **Parameterization** — Varistor operation mode `Linear` (default) | `Power-law`

Choose how the varistor resistance changes with increasing voltages:

- `Linear` — Two regions. The
  low-voltage region has high resistance and the high-voltage
  region has low resistance.
- `Power-law` — Three regions. The
  leakage region has high resistance. The normal region has
  exponentially decreasing resistance. The upturn region has low
  resistance.

### **Clamping voltage** — Threshold voltage `260` (default) | positive number

Transition point voltage,
*vclamp*, between the off- and
on-states of the linear varistor.

#### Dependencies

Enabled when the **Parameterization** parameter is
set to `Linear`.

### **Off resistance** — Low-voltage resistance `3e8` (default) | positive number

Low-voltage resistance, *Roff*, of
the varistor in the off-state.

#### Dependencies

Enabled when the **Parameterization** parameter is
set to `Linear`.

### **On resistance** — High-voltage resistance `1` (default) | positive number

High-voltage resistance, *Ron*, of
the varistor in the on-state.

#### Dependencies

Enabled when the **Parameterization** parameter is
set to `Linear`.

### **Leakage to normal voltage transition** — First threshold voltage `130` (default) | positive number

Transition point voltage, *vLN*,
between the leakage and normal regions of the power-law varistor.

#### Dependencies

Enabled when the **Parameterization** parameter is
set to `Power-law`.

### **Normal to upturn voltage transition** — Second threshold voltage `300` (default) | positive number

Transition point voltage, *vNU*,
between the normal and upturn regions of the power-law varistor.

#### Dependencies

Enabled when the **Parameterization** parameter is
set to `Power-law`.

### **Leakage-mode resistance** — Low-voltage resistance `3e8` (default) | positive number

Low-voltage resistance, *RL*, of
the varistor in the leakage region.

#### Dependencies

Enabled when the **Parameterization** parameter is
set to `Power-law`.

### **Normal-mode power-law exponent** — Mid-voltage resistance `45` (default) | positive number

Exponent that determines rate of current increase with voltage increase of
the varistor in the normal region.

#### Dependencies

Enabled when the **Parameterization** parameter is
set to `Power-law`.

### **Upturn-mode resistance** — High-voltage resistance `0.07` (default) | positive number

High-voltage resistance, *RU*, of
the varistor in the upturn region.

#### Dependencies

Enabled when the **Parameterization** parameter is
set to `Power-law`.

### **Terminal resistance** — Terminal resistance `100e-6` (default) | non-negative number

Small, constant resistance in series with the varistor. Set this value to
zero to remove the resistance from the equivalent circuit.

### **Capacitance** — Parallel capacitance `4.4` (default) | non-negative number

Capacitor in parallel with the varistor. Set this value to zero to remove
the capacitor from the equivalent circuit.
## Libraries

Simscape / Electrical / Passive

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Voltage-dependent resistor

The Varistor block represents a voltage-dependent resistor (VDR). This
component is also commonly known as a metal-oxide varistor (MOV). The block exhibits
high resistance at low voltages and low resistance at high voltages.

You can protect parts of an electrical circuit from high-voltage surges by placing
this block in parallel with them. When a surge occurs, the resistance of the varistor
drops significantly, causing the current to be shunted through the varistor rather than
through the circuit.

Use the **Parameterization** parameter to choose between two
different behaviors for this block. The `Linear` option focuses
on the on- and off-states of the varistor and uses a linear relationship between current
and voltage in both regions. The `Power-law` option uses an
exponential relationship between current and voltage in the initial on-state. This
option also adds a third, linear region at higher voltages.

### Linear Parameterization

This parameterization option separates the voltage-current relationship into two
linear regions:

- Off-region — resistance is high and current increases slowly with
  increasing voltage.
- On-region — resistance is low and current increases rapidly with
  increasing voltage.

This figure shows the voltage-current relationship across the on- and off-regions.

Use linear parameterization in one of these scenarios:

- You are modeling voltage surges close to the threshold voltage
- You expect your varistor to behave linearly in all regions

The voltage-current relationship for the linear varistor is:

ivaristor={vvaristorRoff|vvaristor|<vclampvvaristorRon+c1sgn(vvaristor)|vvaristor|≥vclamp.

where:

- *vvaristor* and
  *ivaristor* are the
  varistor voltage and current, respectively.
- *vclamp* is the threshold
  voltage that separates the two regions of operation. Set this value
  using the **Clamping voltage** parameter.
- *Ron* and
  *Roff* are the
  resistances in the on- and off-regions. Set these values using the
  **On resistance** and **Off
  resistance**, respectively.
- *c1* is a constant used to
  enforce current continuity between the two regions:

  c1=vclamp(1Roff−1Ron).

### Power-Law Parameterization

This parameterization option separates the voltage-current relationship into three regions:

- Leakage region — Resistance is high and current increases slowly with
  increasing voltage.
- Normal region — Resistance decreases exponentially with increasing
  voltage.
- Upturn region — Resistance is low and current increases rapidly with
  increasing voltage.

This figure shows the three regions of operation in log-log-scale.

Use power-law parameterization in one of these scenarios:

- You are modeling voltage surges across a large range of
  voltages
- You expect your varistor to behave exponentially in the first
  on-region

The voltage-current relationship for the power-law varistor is:

ivaristor={vvaristorRL|vvaristor|<vLNk(vvaristor)α+c1vLN≤|vvaristor|≤vNUvvaristorRU+c2|vvaristor|>vNU

where:

- *vvaristor* and
  *ivaristor* are the
  varistor voltage and current, respectively.
- *α* is the power-law exponent which determines the
  rate of current increase with voltage increase in the normal region. Set
  this value using the **Normal-mode power-law exponent**
  parameter.
- *vLN* and the
  *vNU* are the threshold
  voltages corresponding to the leakage-normal and normal-upturn
  transition points. Set these values using the **Leakage to
  normal voltage transition** and **Normal to upturn
  voltage transition** parameters, respectively.
- *RL* and
  *RU* are the resistances
  in the leakage- and upturn-regions. Set these values using the
  **Leakage-mode resistance** and
  **Upturn-mode resistance** parameters,
  respectively.
- *k*, *c1*,
  and *c2* are constants used to
  enforce current continuity between the regions:

  k=1αRUvNUα−1,

  c1=vLNRL−vLNααRUvNUα−1,

  and

  c2=1αRUvNUα−1(vNUα−vLNα)−vNURU+vLNRL.

### Equivalent Circuit

In addition to the varistor equations, you can also specify a constant terminal
resistance *Rt* and device capacitance
*C*. This figure shows the equivalent circuit for the varistor
in either parameterization mode.
