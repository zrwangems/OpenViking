---
type: simulink-block
title: 'Zigzag-Delta-Wye Transformer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Transformers'
documentation_page: 'zigzagdeltawyetransformer'
documentation_source_path: 'ref/zigzagdeltawyetransformer.html'
language: en
---

# Zigzag-Delta-Wye Transformer

## Ports
```yaml
ports:
- name: ~1
  summary: Primary winding voltage electrical
  direction: conserving
- name: ~2
  summary: Delta secondary winding voltage electrical
  direction: conserving
- name: ~3
  summary: Wye secondary winding voltage electrical
  direction: conserving
- name: n3
  summary: Second secondary winding neutral point electrical
  direction: conserving
- name: ~1i
  summary: Zigzag winding interconnection port electrical
  direction: conserving
```

### Conserving

### **~1** — Primary winding voltage electrical

Expandable three-phase electrical conserving port associated with the
three-phase, [*a1*
*b1*
*c1*], voltage of the primary winding.

### **~2** — Delta secondary winding voltage electrical

Expandable three-phase electrical conserving port associated with the
three-phase, [*a2*
*b2*
*c2*], voltage of the first secondary winding.

#### Dependencies

To enable this port, set **Secondary connection**
to `Delta` or `Wye and
Delta`.

### **~3** — Wye secondary winding voltage electrical

Expandable three-phase electrical conserving port associated with the
three-phase, [*a3*
*b3*
*c3*], voltage of the second secondary winding.

#### Dependencies

To enable this port, set **Secondary connection**
to `Wye` or `Wye and
Delta`.

### **n3** — Second secondary winding neutral point electrical

Electrical conserving port associated with the wye secondary winding
neutral point.

### **~1i** — Zigzag winding interconnection port electrical

Electrical conserving port associated with the interconnection of the
zigzag winding.

#### Dependencies

To enable this port, set **Zigzag configuration** to
`Accessible winding
interconnects`.
## Parameters
```yaml
parameters:
- name: Modeling option
  summary: Whether to model composite or expanded three-phase ports Composite three-phase ports (default) | Expanded three-phase
    ports
  group: ''
- name: Rated apparent power
  summary: Apparent power at rated capacity 100e6 V*A (default) | positive scalar
  group: Main
- name: Rated electrical frequency
  summary: Connected network electrical frequency 60 Hz (default) | positive scalar
  group: Main
- name: Primary rated voltage
  summary: Root mean square line voltage applied to the primary winding 24e3 V (default) | positive scalar
  group: Main
- name: Zigzag configuration
  summary: Zigzag configuration type Internal floating neutral (default) | Accessible winding interconnects
  group: Main
- name: Secondary connection
  summary: Zigzag configuration type Delta (default) | Wye | Wye and Delta
  group: Main
- name: Delta connection type
  summary: Delta connection type Delta 1 o'clock (default) | Delta 11 o'clock
  group: Main
- name: Delta secondary rated voltage
  summary: Root mean square line voltage applied to the delta secondary winding 4160 V (default) | positive scalar
  group: Main
- name: Wye secondary rated voltage
  summary: Root mean square line voltage applied to the wye secondary winding 4160 V (default) | positive scalar
  group: Main
- name: Secondary phase shift
  summary: Phase offset for secondary winding -7.5 deg (default)
  group: Main
- name: Primary winding resistance (pu)
  summary: Primary winding power loss 0.01 (default) | positive scalar
  group: Impedances
- name: Delta secondary winding resistance (pu)
  summary: Delta secondary winding power loss 0.01 (default) | positive scalar
  group: Impedances
- name: Wye secondary winding resistance (pu)
  summary: Wye secondary winding power loss 0.01 (default) | positive scalar
  group: Impedances
- name: Leakage reactance
  summary: Leakage reactance modeling Exclude (default) | Include
  group: Impedances
- name: Primary leakage reactance (pu)
  summary: Primary winding magnetic flux loss 0.001 (default) | positive scalar
  group: Impedances
- name: Delta secondary leakage reactance (pu)
  summary: Delta secondary winding flux loss 0.001 (default) | positive scalar
  group: Impedances
- name: Wye secondary leakage reactance (pu)
  summary: Wye secondary winding flux loss 0.001 (default) | positive scalar
  group: Impedances
- name: Magnetizing resistance
  summary: Magnetizing resistance modeling Exclude (default) | Include
  group: Impedances
- name: Shunt magnetizing resistance (pu)
  summary: Transformer core losses 500 (default) | positive scalar
  group: Impedances
- name: Magnetizing reactance
  summary: Magnetizing reactance modeling Exclude (default) | Include
  group: Impedances
- name: Magnetic saturation representation
  summary: Representation of the magnetic saturation None (default) | Lookup table (phi versus i)
  group: Impedances
- name: Current vector (pu), i
  summary: Per unit vector of currents [0, .002, 1, 2] (default)
  group: Impedances
- name: Magnetic flux vector (pu), phi
  summary: Per unit vector of magnetic flux [0, 1.2, 1.5, 1.51] (default)
  group: Impedances
- name: Shunt magnetizing reactance (pu)
  summary: Transformer core magnetic effects 500 (default) | positive scalar
  group: Impedances
```

### **Modeling option** — Whether to model composite or expanded three-phase ports `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical conserving ports
with a single block port. You can use composite three-phase ports to build models that
correspond to single-line diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a three-phase system
using three separate electrical conserving ports.

### Main

### **Rated apparent power** — Apparent power at rated capacity `100e6` `V*A` (default) | positive scalar

Apparent power flowing through the transformer when operating at rated
capacity, in V\*A.

### **Rated electrical frequency** — Connected network electrical frequency `60` `Hz` (default) | positive scalar

Rated or nominal frequency of the AC network to which the transformer
is connected, in Hz. The value must be greater than
`0`.

### **Primary rated voltage** — Root mean square line voltage applied to the primary winding `24e3` `V` (default) | positive scalar

RMS line voltage applied to the primary winding under normal operating
conditions, in V. The value must be greater than
`0`.

### **Zigzag configuration** — Zigzag configuration type `Internal floating neutral` (default) | `Accessible winding interconnects`

Configuration of zigzag winding.

### **Secondary connection** — Zigzag configuration type `Delta` (default) | `Wye` | `Wye and Delta`

Configuration of the secondary connection.

### **Delta connection type** — Delta connection type `Delta 1 o'clock` (default) | `Delta 11 o'clock`

Type of delta connection.

#### Dependencies

To enable this parameter, set **Secondary
connection** to `Delta` or
`Wye and Delta`.

### **Delta secondary rated voltage** — Root mean square line voltage applied to the delta secondary winding `4160` `V` (default) | positive scalar

RMS line voltage applied to the delta secondary winding under normal
operating conditions, in V. The value must be greater than
`0`.

#### Dependencies

To enable this parameter, set **Secondary
connection** to `Delta` or
`Wye and Delta`.

### **Wye secondary rated voltage** — Root mean square line voltage applied to the wye secondary winding `4160` `V` (default) | positive scalar

RMS line voltage applied to the wye secondary winding under normal
operating conditions, in V. The value must be greater than
`0`.

#### Dependencies

To enable this parameter, set **Secondary
connection** to `Wye` or
`Wye and Delta`.

### **Secondary phase shift** — Phase offset for secondary winding `-7.5` `deg` (default)

Phase offset between the zigzag and the secondary windings.

### Impedances

### **Primary winding resistance (pu)** — Primary winding power loss `0.01` (default) | positive scalar

Per-unit power loss in the primary winding. The value must be greater
than `0`.

### **Delta secondary winding resistance (pu)** — Delta secondary winding power loss `0.01` (default) | positive scalar

Per-unit power loss in the delta secondary winding. The value must be
greater than `0`.

#### Dependencies

To enable this parameter, set **Secondary
connection** to `Delta` or
`Wye and Delta`.

### **Wye secondary winding resistance (pu)** — Wye secondary winding power loss `0.01` (default) | positive scalar

Per-unit power loss in the wye secondary winding. The value must be
greater than `0`.

#### Dependencies

To enable this parameter, set **Secondary
connection** to `Wye` or
`Wye and Delta`.

### **Leakage reactance** — Leakage reactance modeling `Exclude` (default) | `Include`

Whether to model magnetic flux losses.

### **Primary leakage reactance (pu)** — Primary winding magnetic flux loss `0.001` (default) | positive scalar

Per-unit magnetic flux loss in the primary winding. The value must be
greater than `0`.

#### Dependencies

To enable this parameter, set **Leakage
reactance** to
`Include`.

### **Delta secondary leakage reactance (pu)** — Delta secondary winding flux loss `0.001` (default) | positive scalar

Per-unit magnetic flux loss in the delta secondary winding. The value
must be greater than `0`.

#### Dependencies

To enable this parameter, set **Leakage reactance** to
`Include` and **Secondary
connection** to either `Delta`
or `Wye and Delta`.

### **Wye secondary leakage reactance (pu)** — Wye secondary winding flux loss `0.001` (default) | positive scalar

Per-unit magnetic flux loss in the wye secondary winding. The value
must be greater than `0`.

#### Dependencies

To enable this parameter, set **Leakage reactance** to
`Include` and **Secondary
connection** to either `Wye`
or `Wye and Delta`.

### **Magnetizing resistance** — Magnetizing resistance modeling `Exclude` (default) | `Include`

Whether to model the transformer core losses.

### **Shunt magnetizing resistance (pu)** — Transformer core losses `500` (default) | positive scalar

Per-unit losses in the transformer core. The value must be greater
than `0`.

#### Dependencies

To enable this parameter, set **Magnetizing
resistance** to
`Include`.

### **Magnetizing reactance** — Magnetizing reactance modeling `Exclude` (default) | `Include`

Whether to model magnetic effects of the transformer core.

### **Magnetic saturation representation** — Representation of the magnetic saturation `None` (default) | `Lookup table (phi versus i)`

Whether to represent magnetic saturation.

#### Dependencies

To enable this parameter, set **Magnetizing
reactance** to
`Include`.

### **Current vector (pu), i** — Per unit vector of currents `[0, .002, 1, 2]` (default)

Per unit vector of currents. The first value must be
`0`. This parameter must be strictly
ascending.

#### Dependencies

To enable this parameter, set **Magnetizing reactance** to
`Include` and **Magnetic
saturation representation** to `Lookup
table (phi versus i)`.

### **Magnetic flux vector (pu), phi** — Per unit vector of magnetic flux `[0, 1.2, 1.5, 1.51]` (default)

Per unit vector of magnetic flux. The first value must be
`0`. This parameter must be strictly
ascending.

#### Dependencies

To enable this parameter, set **Magnetizing reactance** to
`Include` and **Magnetic
saturation representation** to `Lookup
table (phi versus i)`.

### **Shunt magnetizing reactance (pu)** — Transformer core magnetic effects `500` (default) | positive scalar

Per-unit magnetic effects of the transformer core when operating in
its linear region. The value must be greater than
`0`.

#### Dependencies

To enable this parameter, set **Magnetizing reactance** to
`Include` and **Magnetic
saturation representation** to
`None`.
## Libraries

Simscape / Electrical / Passive / Transformers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Linear, non-ideal zigzag-delta-wye transformer with three-limb core with saturation capability

The Zigzag-Delta-Wye Transformer block models a linear,
nonideal transformer with a three-limb core that has primary zigzag windings and
secondary delta, wye, or delta and wye windings. You can specify the phase offset
between the zigzag and wye windings using the **Wye secondary phase
shift** parameter and parameterize the block impedance using per-unit
values. The block includes effects for linear winding leakage and linear core
magnetization.

The configuration options for the delta winding types are:

- Delta 1 o'clock — Mesh configuration with a lagging 30-degree phase shift
  relative to the voltage of a connected wye configuration
- Delta 11 o'clock — Mesh configuration with leading 30-degree phase shift
  relative to the voltage of a connected wye configuration

These equivalent circuit diagrams show the zigzag-delta-wye transformer in the delta 1
o'clock and delta 11 o'clock configurations, respectively.

In these diagrams:

- *Rw1* is the primary winding
  resistance.
- *Ll1* is the primary leakage
  reactance.
- *Rw2* is the delta secondary
  winding resistance.
- *Ll2* is the delta secondary
  leakage reactance.
- *Rw3* is the wye secondary winding
  resistance.
- *Ll3* is the wye secondary leakage
  reactance.
- *Rm* is the shunt magnetizing
  resistance.
- *Lm* is the shunt magnetizing
  reactance.

### Variables

Use the **Variables** settings to specify the priority and
initial target values for the block variables before simulation. For more
information, see Set Priority and Initial Target for Block Variables.

To enable the **Wye secondary currents** variable, set
**Secondary connection** to `Wye` or
`Wye and Delta`.

To enable the **Delta secondary currents** variable, set
**Secondary connection** to `Delta` or
`Wye and Delta`.
