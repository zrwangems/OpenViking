---
type: simulink-block
title: 'Simplified Synchronous Machine Measurement'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Synchronous'
documentation_page: 'simplifiedsynchronousmachinemeasurement'
documentation_source_path: 'ref/simplifiedsynchronousmachinemeasurement.html'
language: en
---

# Simplified Synchronous Machine Measurement

## Ports

### Input

### **pu** — Per-unit measurements from a connected synchronous machine vector of physical signal

Physical signal associated with the per-unit measurements from a connected Simplified
Synchronous Machine, specified as:

- `pu_EMFa`
- `pu_EMFb`
- `pu_EMFc`
- `pu_torque`
- `pu_velocity`
- `pu_vd`
- `pu_vq`
- `pu_v0`
- `pu_id`
- `pu_iq`
- `pu_i0`
### Output

### **o** — Per-unit measurement output port physical signal

Physical signal output port associated with the per-unit measurement, returned as a
physical signal.

## Parameters

### **Output** — Per-unit measurement from synchronous machine `EMF phase A` (default) | `EMF phase B` | `EMF phase C` | `Electrical torque` | `Rotor velocity` | `Stator d-axis voltage` | `Stator q-axis voltage` | `Stator zero-sequence voltage` | `Stator d-axis current` | `Stator q-axis current` | `Stator zero-sequence current` | `Apparent power` | `Real power` | `Reactive power` | `Terminal voltage` | `Terminal current` | `Power factor angle` | `Power factor` | `Load angle` | `Rotor electrical angle`

Per-unit measurement from simplified synchronous machine. The default
value is `EMF phase A`.

## Libraries

Simscape / Electrical / Electromechanical / Synchronous

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Per-unit measurement from simplified synchronous machine

The Simplified Synchronous Machine Measurement block outputs
a per-unit measurement associated with a connected Simplified Synchronous
Machine block. The input of the Simplified
Synchronous Machine Measurement block connects to the
`pu` output port of the Simplified Synchronous Machine
block.

You set the **Output** parameter to a per-unit measurement associated
with the simplified synchronous machine. Based on the value you select, the
Simplified Synchronous Machine Measurement
block:

- Directly outputs the value of an element in the input signal vector
- Calculates the per-unit measurement by using values of elements in the input
  signal vector in mathematical expressions.

The Simplified Synchronous Machine Measurement block
outputs a per-unit measurement from the simplified synchronous machine according to the
output value expressions in the table. For example, when you set
**Output** to `Stator d-axis voltage`, the block
directly outputs the value of the `pu_ed` element in the input signal
vector. However, when you set **Output** to `Reactive
power`, the block calculates the value from the `pu_ed`,
`pu_eq`, `pu_id`, and `pu_iq`
elements.

| Output Parameter Setting | Output Value Expression |
| --- | --- |
| `EMF phase A` | `pu_EMFa` |
| `EMF phase B` | `pu_EMFb` |
| `EMF phase C` | `pu_EMFc` |
| `Electrical torque` | `pu_torque` |
| `Rotor velocity` | `pu_velocity` |
| `Stator d-axis voltage` | `pu_vd` |
| `Stator q-axis voltage` | `pu_vq` |
| `Stator zero-sequence voltage` | `pu_v0` |
| `Stator d-axis current` | `pu_id` |
| `Stator q-axis current` | `pu_iq` |
| `Stator zero-sequence current` | `pu_i0` |
| `Apparent power` | pu\_Pt2+pu\_Qt2 |
| `Real power` | `pu_Pt = (pu_vd*pu_id) + (pu_vq*pu_iq) + 2(pu_v0*pu_i0)` |
| `Reactive power` | `pu_Qt = (pu_vq*pu_id) – (pu_vd*pu_iq)` |
| `Terminal voltage` | (pu\_vd2+​pu\_vq2) |
| `Terminal current` | (pu\_id2+pu\_iq2) |
| `Power factor angle` | `power_factor_angle = atan2(pu_Qt, pu_Pt)` |
| `Power factor` | `cos(power_factor_angle)` |
| `Load angle` | `load_angle(rad) = atan2(pu_vd, pu_vq)` |
| `Rotor electrical angle` | θe(t)=Nθr(t) |
