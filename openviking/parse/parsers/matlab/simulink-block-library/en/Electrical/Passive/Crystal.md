---
type: simulink-block
title: 'Crystal'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'crystal'
documentation_source_path: 'ref/crystal.html'
language: en
---

# Crystal

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

Electrical conserving port associated with the crystal positive
voltage.

### **-** — Negative terminal electrical

Electrical conserving port associated with the crystal negative
voltage.
## Parameters
```yaml
parameters:
- name: Parameterization
  summary: Block parameterization Series resonance data (default) | Parallel resonance data | Equivalent circuit parameters
  group: ''
- name: Series resonance, fs
  summary: Crystal series resonant frequency 32.764 kHz (default)
  group: ''
- name: Parallel resonance, fa
  summary: Crystal parallel resonant frequency 32.768 kHz (default)
  group: ''
- name: Motional inductance, L1
  summary: Motional inductance 6742 H (default)
  group: ''
- name: R1 parameterization
  summary: Series resistance parameterization Equivalent series resistance R1 (default) | Quality factor Q
  group: ''
- name: Quality factor, Q
  summary: Crystal quality factor 90000 (default)
  group: ''
- name: Equivalent series resistance, R1
  summary: Motional damping 15 kOhm (default)
  group: ''
- name: Motional capacitance, C1
  summary: Motional capacitance 0.0035 pF (default)
  group: ''
- name: Load capacitance, CL
  summary: Load capacitance 12.5 pF (default)
  group: ''
- name: Shunt capacitance, C0
  summary: Shunt capacitance 1.6 pF (default) | positive scalar
  group: ''
- name: Initial voltage
  summary: Initial output voltage 0 V (default)
  group: ''
```

### **Parameterization** — Block parameterization `Series resonance data` (default) | `Parallel resonance data` | `Equivalent circuit parameters`

Select one of the following methods for block parameterization:

- `Series resonance data` —
  Provide series resonant frequency and capacitance data for the
  crystal. This method is the default.
- `Parallel resonance data` —
  Provide parallel resonant frequency and capacitance data for the
  crystal.
- `Equivalent circuit parameters`
  — Provide electrical parameters for an equivalent circuit
  model of the crystal.

### **Series resonance, fs** — Crystal series resonant frequency `32.764` `kHz` (default)

Crystal series resonant frequency.

#### Dependencies

This parameter is visible only when you select `Series
resonance data` for the
**Parameterization** parameter.

### **Parallel resonance, fa** — Crystal parallel resonant frequency `32.768` `kHz` (default)

Crystal parallel resonant frequency that corresponds to operating with a
parallel load capacitance specified by the **Load capacitance,
CL** parameter.

#### Dependencies

This parameter is visible only when you select `Parallel
resonance data` for the
**Parameterization** parameter.

### **Motional inductance, L1** — Motional inductance `6742` `H` (default)

Inductance that represents the mechanical mass of the crystal.

#### Dependencies

This parameter is visible only when you select `Equivalent
circuit parameters` for the
**Parameterization** parameter.

### **R1 parameterization** — Series resistance parameterization `Equivalent series resistance R1` (default) | `Quality factor Q`

Select one of the following methods for series resistance parameterization:

- `Equivalent series resistance R1`
  — Provide the resistance value directly. This is the
  default method.
- `Quality factor Q` — Provide
  the quality factor that the block uses to calculate the
  resistance value.

#### Dependencies

This parameter is visible only when you select `Series
resonance data` or `Parallel resonance
data` for the **Parameterization**
parameter.

### **Quality factor, Q** — Crystal quality factor `90000` (default)

Crystal quality factor. This parameter is only visible when you make one
of the following selections:

- `Series resonance data` for the
  **Parameterization** parameter and
  `Quality factor Q` for the
  **R1 parameterization** parameter
- `Parallel resonance data` for the
  **Parameterization** parameter and
  `Quality factor Q` for the
  **R1 parameterization** parameter

#### Dependencies

This parameter is visible only when you select:

- `Series resonance data` for the
  **Parameterization** parameter and
  `Quality factor Q` for the
  **R1 parameterization**
  parameter
- `Parallel resonance data` for the
  **Parameterization** parameter and
  `Quality factor Q` for the
  **R1 parameterization**
  parameter

### **Equivalent series resistance, R1** — Motional damping `15` `kOhm` (default)

Motional damping term. This parameter is only visible when you make one of
the following selections:

- `Series resonance data` for the
  **Parameterization** parameter and
  `Equivalent series resistance R1`
  for the **R1 parameterization**
  parameter
- `Parallel resonance data` for the
  **Parameterization** parameter and
  `Equivalent series resistance R1`
  for the **R1 parameterization**
  parameter
- `Equivalent circuit parameters` for
  the **Parameterization** parameter

#### Dependencies

This parameter is visible only when you select:

- `Series resonance data` for the
  **Parameterization** parameter and
  `Equivalent series resistance
  R1` for the **R1
  parameterization** parameter
- `Parallel resonance data` for the
  **Parameterization** parameter and
  `Equivalent series resistance
  R1` for the **R1
  parameterization** parameter
- `Equivalent circuit parameters`
  for the **Parameterization**
  parameter

### **Motional capacitance, C1** — Motional capacitance `0.0035` `pF` (default)

Capacitance that represents crystal mechanical stiffness under
load.

### **Load capacitance, CL** — Load capacitance `12.5` `pF` (default)

Load capacitance that corresponds to the **Parallel resonance,
fa** parameter value.

#### Dependencies

This parameter is visible only when you select `Parallel
resonance data` for the
**Parameterization** parameter.

### **Shunt capacitance, C0** — Shunt capacitance `1.6` `pF` (default) | positive scalar

Electrical capacitance between the two crystal electrical
connections.

### **Initial voltage** — Initial output voltage `0` `V` (default)

The output voltage at the start of the simulation when the output current
is zero.
## Libraries

Simscape / Electrical / Passive

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2009a**

## Description

Stable resonator

The Crystal block represents the electrical
characteristics of a crystal. The following figure shows the equivalent circuit model of
the Crystal block.

You specify the equivalent circuit parameters for this model when you set the
**Parameterization** parameter to `Equivalent circuit
parameters`.

- The capacitor *C0* corresponds to the capacitance you
  specify in the **Shunt capacitance, C0** parameter.
- The capacitor *C1* corresponds to the capacitance you
  specify in the **Motional capacitance, C1**
  parameter.
- The inductor *L1* corresponds to the inductance you
  specify in the **Motional inductance, L1**
  parameter.
- The resistor *R1* corresponds to the resistance you
  specify in the **Equivalent series resistance, R1**
  parameter.

Most datasheets specify crystal frequency rather than inductance, so the block
optionally accepts frequency data.

- When you set the **Parameterization** parameter to
  `Series resonance data`, the block uses the
  following relationship to calculate *L1* from the series
  resonant frequency:

  fs=12πL1C1

  Where *fs* is the
  **Series resonance, fs** parameter value.
- When you set the **Parameterization** parameter to
  `Parallel resonance data`, the block uses the
  following relationship to calculate *L1* from the parallel
  resonant frequency:

  fa=12πL1C1(C0+CL)/(C1+C0+CL)

  Where:

  - *fa* is the
    **Parallel resonance, fa** parameter
    value.
  - *CL* is the
    **Load capacitance, CL** parameter
    value.

Some datasheets specify quality factor rather than equivalent series resistance, so
the block optionally accepts quality factor data. When you set the **R1
parameterization** parameter to `Quality factor
Q`, the block uses the following relationship to calculate
*R1* from the quality factor:

Q=2πfL1R1

Where *Q* is the **Quality factor,
Q** parameter value.

**Note**

The **R1 parameterization** parameter is only visible when you
select `Series resonance data` or `Parallel
resonance data` for the **Parameterization**
parameter.
