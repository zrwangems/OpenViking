---
type: simulink-block
title: 'Synchronous Machine Measurement'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Synchronous'
documentation_page: 'synchronousmachinemeasurement'
documentation_source_path: 'ref/synchronousmachinemeasurement.html'
language: en
---

# Synchronous Machine Measurement

## Ports

### Input

### **pu** — Per-unit measurements from a connected synchronous machine physical

Physical signal vector port associated with per-unit measurements from
a connected synchronous machine. The vector elements are:

- `pu_fd_Efd`
- `pu_fd_Ifd`
- `pu_torque`
- `pu_velocity`
- `pu_ed`
- `pu_eq`
- `pu_e0`
- `pu_id`
- `pu_iq`
- `pu_i0`
### Output

### **o** — Per-unit measurement output port physical

Physical signal output port associated with the per-unit
measurement.

## Parameters

### **Output** — Per-unit measurement from synchronous machine `Field voltage (field circuit base, Efd)` (default) | `Field current (field circuit base, Ifd)` | `Electrical torque` | `Rotor velocity` | `Stator d-axis voltage` | `Stator q-axis voltage` | `Stator zero-sequence voltage` | `Stator d-axis current` | `Stator q-axis current` | `Stator zero-sequence current` | `Apparent power` | `Real power` | `Reactive power` | `Terminal voltage` | `Terminal current` | `Power factor angle` | `Power factor` | `Load angle` | `Rotor electrical angle`

Per-unit measurement from synchronous machine. The default value is
`Field voltage (field circuit base,
Efd)`.

## Libraries

Simscape / Electrical / Electromechanical / Synchronous

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Per-unit measurement from synchronous machine

The Synchronous Machine Measurement block outputs a
per-unit measurement associated with a connected Synchronous Machine
Round Rotor or Synchronous Machine Salient
Pole block. The input of the Synchronous Machine
Measurement block connects to the `pu` output port
of the synchronous machine block.

You set the **Output** parameter to a per-unit measurement associated
with the synchronous machine. Based on the value you select, the
Synchronous Machine Measurement block:

- Directly outputs the value of an element in the input signal vector
- Calculates the per-unit measurement by using values of elements in the input
  signal vector in mathematical expressions

The Synchronous Machine Measurement block outputs a
per-unit measurement from the synchronous machine according to the output value
expressions in the table. For example, when you set **Output** to
`Stator d-axis voltage`, the block directly outputs the value of
the `pu_ed` element in the input signal vector. However, when you set
**Output** to `Reactive power`, the block
calculates the value from the `pu_ed`, `pu_eq`,
`pu_id`, and `pu_iq` elements.

| Output Parameter Setting | Output Value Expression |
| --- | --- |
| Field voltage (field circuit base, Efd) | `pu_fd_Efd` |
| Field current (field circuit base, Ifd) | `pu_fd_Ifd` |
| Electrical torque | `pu_torque` |
| Rotor velocity | `pu_velocity` |
| Stator d-axis voltage | `pu_ed` |
| Stator q-axis voltage | `pu_eq` |
| Stator zero-sequence voltage | `pu_e0` |
| Stator d-axis current | `pu_id` |
| Stator q-axis current | `pu_iq` |
| Stator zero-sequence current | `pu_i0` |
| Apparent power | pu\_Pt2+pu\_Qt2 |
| Real power | `pu_Pt = (pu_ed*pu_id) + (pu_eq*pu_iq) + 2(pu_e0*pu_i0)` |
| Reactive power | `pu_Qt = (pu_eq*pu_id) – (pu_ed*pu_iq)` |
| Terminal voltage | (pu\_ed2+​pu\_eq2) |
| Terminal current | (pu\_id2+pu\_iq2) |
| Power factor angle (rad) | `power_factor_angle = atan2(pu_Qt, pu_Pt)` |
| Power factor | `cos(power_factor_angle)` |
| Load angle (rad) | `load_angle(rad) = atan2(pu_ed, pu_eq)` |
| Rotor electrical angle | `y = pi+2*atan(tan((u-pi)/2))` |
