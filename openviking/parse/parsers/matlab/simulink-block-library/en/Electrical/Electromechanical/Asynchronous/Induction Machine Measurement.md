---
type: simulink-block
title: 'Induction Machine Measurement'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Asynchronous'
documentation_page: 'inductionmachinemeasurement'
documentation_source_path: 'ref/inductionmachinemeasurement.html'
language: en
---

# Induction Machine Measurement

## Ports
```yaml
ports:
- name: pu
  summary: Input port physical
  direction: input
- name: o
  summary: Per-unit measurement output physical
  direction: output
```

### Input

### **pu** — Input port physical

Physical signal vector associated with per-unit measurements from a
connected induction machine. The vector elements are:

- *pu\_torque*
- *pu\_velocity*
- *pu\_vds*
- *pu\_vqs*
- *pu\_v0s*
- *pu\_ids*
- *pu\_iqs*
- *pu\_i0s*
### Output

### **o** — Per-unit measurement output physical

Physical signal associated with the per-unit measurement
output.
## Parameters
```yaml
parameters:
- name: Output
  summary: Per-unit measurement Electrical torque (default) | Rotor velocity | Stator d-axis voltage | Stator q-axis voltage
    | Stator zero-sequence voltage | Stator d-axis current | Stator q-axis current | Stator zero-sequence current | Slip |
    Apparent power | Real power | Reactive power | Terminal voltage | Power factor angle | Power factor angle
  group: ''
```

### **Output** — Per-unit measurement `Electrical torque` (default) | `Rotor velocity` | `Stator d-axis voltage` | `Stator q-axis voltage` | `Stator zero-sequence voltage` | `Stator d-axis current` | `Stator q-axis current` | `Stator zero-sequence current` | `Slip` | `Apparent power` | `Real power` | `Reactive power` | `Terminal voltage` | `Power factor angle` | `Power factor angle`

Per-unit measurement from induction machine. Options are:

- `Electrical torque`
- `Rotor velocity`
- `Stator d-axis voltage`
- `Stator q-axis voltage`
- `Stator zero-sequence voltage`
- `Stator d-axis current`
- `Stator q-axis current`
- `Stator zero-sequence current`
- `Slip`
- `Apparent power`
- `Real power`
- `Reactive power`
- `Terminal voltage`
- `Power factor angle`
- `Power factor angle`
## Libraries

Simscape / Electrical / Electromechanical / Asynchronous

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Per-unit measurement from induction machine

The Induction Machine Measurement block outputs a
per-unit measurement associated with a connected Induction Machine
Squirrel Cage or Induction Machine Wound
Rotor block. The input of the Induction Machine
Measurement block connects to the `pu` output port
of the induction machine block.

You set the **Output** parameter to a per-unit measurement associated
with the induction machine. Based on the value you select, the Induction
Machine Measurement block:

- Directly outputs the value of an element in the input signal vector
- Calculates the per-unit measurement by using values of elements in the input
  signal vector in mathematical expressions

The Induction Machine Measurement block outputs a
per-unit measurement from the induction machine according to the output value
expressions in the table. For example, when you set **Output** to
*Stator d-axis voltage*, the block directly outputs the value of
the *pu\_vds* element in the input signal vector. However, when you set
**Output** to *Slip*, the block calculates the
slip value by subtracting the value of the *pu\_velocity* element from
1.

| Output Parameter Setting | Output Value Expression |
| --- | --- |
| Electrical torque | pu\_torque |
| Rotor velocity | pu\_velocity |
| Stator d-axis voltage | pu\_vds |
| Stator q-axis voltage | pu\_vqs |
| Stator zero-sequence voltage | pu\_v0s |
| Stator d-axis current | pu\_ids |
| Stator q-axis current | pu\_iqs |
| Stator zero-sequence current | pu\_i0s |
| Slip | 1-pu\_velocity |
| Apparent power | pu\_Pt2+pu\_Qt2 |
| Real power | pu\_Pt = (pu\_vds\*pu\_ids) + (pu\_vqs\*pu\_iqs) + 2(pu\_v0s\*pu\_i0s) |
| Reactive power | pu\_Qt = (pu\_vqs\*pu\_ids) – (pu\_vds\*pu\_iqs) |
| Terminal voltage | pu\_vds2+pu\_vqs2 |
| Terminal current | pu\_ids2+pu\_iqs2 |
| Power factor angle (rad) | power\_factor\_angle = atan2(pu\_Qt, pu\_Pt) |
| Power factor | cos(power\_factor\_angle) |
