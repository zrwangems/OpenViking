---
type: simulink-block
title: 'SRM Commutation'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'srmcommutation'
documentation_source_path: 'ref/srmcommutation.html'
language: en
---

# SRM Commutation

## Ports
```yaml
ports:
- name: θe
  summary: Electrical motor position scalar
  direction: input
  data_types: single | double | fixed point
- name: θeOn
  summary: Turn on electrical motor position scalar
  direction: input
  data_types: single | double | fixed point
- name: θeOff
  summary: Turn off electrical motor position scalar
  direction: input
  data_types: single | double | fixed point
- name: Ctrl
  summary: Control signal vector
  direction: output
  data_types: Boolean
```

### Input

### **θe** — Electrical motor position scalar

Electrical position of the motor measured with respect to phase
*a*, the first phase of the motor. Specify position between
`0-2π` radians or `0-360` degrees or
`0-1` per-unit.

**Data Types:** `single` | `double` | `fixed point`

### **θeOn** — Turn on electrical motor position scalar

Motor electrical position for phase *a* (phase used by
`θe` input) at which the switching
sequence turns from `0` to `1` and energizes the
corresponding phase. Specify position between
`0`-`2π` radians or
`0`-`360` degrees or
`0`-`1` per-unit.

**Data Types:** `single` | `double` | `fixed point`

### **θeOff** — Turn off electrical motor position scalar

Motor electrical position for phase *a* (phase used by
`θe` input) at which the switching
sequence turns from `1` to `0` and de-energizes the
corresponding phase. The value should lie between `0-2π` radians or
`0-360` degrees or `0-1` per-unit.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **Ctrl** — Control signal vector

Combination of switching sequences that you can use to switch each phase to on and
off to drive the motor.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Number of motor phases
  summary: Number of phases in SRM 3 (default) | 4 | 5 | 6
  group: ''
- name: Input position units
  summary: Unit of position inputs Radians (default) | Per unit | Degrees
  group: ''
```

### **Number of motor phases** — Number of phases in SRM `3` (default) | `4` | `5` | `6`

The number of phases in the stator windings of the SRM.

### **Input position units** — Unit of position inputs `Radians` (default) | `Per unit` | `Degrees`

Units for the `θe`,
`θeOn`, and
`θeOff` inputs.
## Libraries

Motor Control Blockset / Controls / Control Reference

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2022b**

## Description

Generate switching sequences for n -phase switched reluctance motor (SRM)

The SRM Commutation block implements a commutation system that generates
switching sequences to energize the stator windings of an *n*-phase
SRM.

The block supports either a three-, four-, five-, or six-phase SRM.

For more details about the algorithm used by the block, see Algorithm.
