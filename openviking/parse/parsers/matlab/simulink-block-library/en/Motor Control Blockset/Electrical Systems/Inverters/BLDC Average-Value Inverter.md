---
type: simulink-block
title: 'BLDC Average-Value Inverter'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Electrical Systems / Inverters'
documentation_page: 'bldcaveragevalueinverter'
documentation_source_path: 'ref/bldcaveragevalueinverter.html'
language: en
---

# BLDC Average-Value Inverter

## Ports
```yaml
ports:
- name: Dsw
  summary: Duty cycles corresponding to six inverter switches 1-by-6 array
  direction: input
  data_types: single | double | fixed point
- name: Vdc
  summary: Inverter DC voltage scalar
  direction: input
  data_types: single | double | fixed point | uint8 | uint16 | uint32
- name: Vabc
  summary: Three-phase voltage output 1-by-3 array
  direction: output
  data_types: single | double | fixed point
```

### Input

### **Dsw** — Duty cycles corresponding to six inverter switches `1`-by-`6` array

Six duty cycles in the range [0, 1] for generating the three-phase voltages that
run the motor.

**Data Types:** `single` | `double` | `fixed point`

### **Vdc** — Inverter DC voltage scalar

DC bus voltage input to the inverter.

**Data Types:** `single` | `double` | `fixed point` | `uint8` | `uint16` | `uint32`
### Output

### **Vabc** — Three-phase voltage output `1`-by-`3` array

Three-phase trapezoidal voltage (Volts) corresponding to the input duty cycles
that runs the motor.

**Data Types:** `single` | `double` | `fixed point`
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Motor Control Blockset / Electrical Systems / Inverters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2023a**

## Description

Compute three-phase trapezoidal AC voltage from inverter DC voltage

The BLDC Average-Value Inverter block models an average-value and full-wave
inverter. It computes the three-phase trapezoidal voltage output from the inverter DC voltage
by using the six duty cycles corresponding to six inverter switches.

### Equations

These equations describe how the block computes the three-phase AC voltage.

Va=Vdc×(Da−Da')

Vb=Vdc×(Db−Db')

Vc=Vdc×(Dc−Dc')

where:

- *Da*,
  *Db*,
  *Dc*,
  *Da'*,
  *Db'*, and
  *Dc'* are the duty cycles (ranging between 0
  and 1) corresponding to the six switches of the inverter (shown in the figure).
- Va, Vb, and Vc are the output three-phase trapezoidal voltages (volts).
- *Vdc* is the DC bus voltage of the inverter
  (volts).
