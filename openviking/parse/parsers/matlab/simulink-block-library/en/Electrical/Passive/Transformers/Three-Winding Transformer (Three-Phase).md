---
type: simulink-block
title: 'Three-Winding Transformer (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Transformers'
documentation_page: 'threewindingtransformerthreephase'
documentation_source_path: 'ref/threewindingtransformerthreephase.html'
language: en
---

# Three-Winding Transformer (Three-Phase)

## Ports
```yaml
ports:
- name: ~1
  summary: Primary winding voltage electrical
  direction: conserving
- name: n1
  summary: Primary winding neutral point electrical
  direction: conserving
- name: ~2
  summary: First secondary winding voltage electrical
  direction: conserving
- name: n2
  summary: First secondary winding neutral point electrical
  direction: conserving
- name: ~3
  summary: Second secondary winding voltage electrical
  direction: conserving
- name: n3
  summary: Second secondary winding neutral point electrical
  direction: conserving
```

### Conserving

### **~1** — Primary winding voltage electrical

Expandable three-phase electrical conserving port associated with the
three-phase, [*a1*
*b1*
*c1*], voltage of winding 1.

### **n1** — Primary winding neutral point electrical

Electrical conserving port associated with the primary winding neutral
point.

#### Dependencies

This port is only visible when the **Main**
parameter **Winding 1 connection type** is set to
`Wye with neutral port`.

### **~2** — First secondary winding voltage electrical

Expandable three-phase electrical conserving port associated with the
three-phase, [*a2*
*b2*
*c2*], voltage of the first secondary winding.

### **n2** — First secondary winding neutral point electrical

Electrical conserving port associated with the first secondary winding
neutral point.

#### Dependencies

This port is only visible when the **Main**
parameter **Winding 2 connection type** is set to
`Wye with neutral port`.

### **~3** — Second secondary winding voltage electrical

Expandable three-phase electrical conserving port associated with the
three-phase, [*a3*
*b3*
*c3*], voltage of the second secondary winding.

### **n3** — Second secondary winding neutral point electrical

Electrical conserving port associated with the second secondary
winding neutral point.

#### Dependencies

This port is only visible when the **Main**
parameter **Winding 3 connection type** is set to
`Wye with neutral port`.
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
- name: Primary winding connection type
  summary: Primary winding configuration Wye with floating neutral (default) | Wye with neutral port | Wye with grounded neutral
    | Delta 1 o'clock | Delta 11 o'clock
  group: Main
- name: Primary rated voltage
  summary: RMS line voltage applied to the primary winding 4160 V (default) | positive scalar
  group: Main
- name: First secondary connection type
  summary: First secondary winding configuration Wye with floating neutral (default) | Wye with neutral port | Wye with grounded
    neutral | Delta 1 o'clock | Delta 11 o'clock
  group: Main
- name: First secondary rated voltage
  summary: RMS line voltage applied to the first secondary winding 24e3 V (default) | positive scalar
  group: Main
- name: Second secondary connection type
  summary: Second secondary winding configuration Wye with floating neutral (default) | Wye with neutral port | Wye with grounded
    neutral | Delta 1 o'clock | Delta 11 o'clock
  group: Main
- name: Second secondary rated voltage
  summary: RMS line voltage applied to the second secondary winding 24e3 (default) | positive scalar
  group: Main
- name: Core type
  summary: Number of limbs Three-phase three-limb (default) | Three-phase five-limb
  group: Main
- name: Primary winding resistance (pu)
  summary: Primary winding power loss 0.01 (default) | positive scalar
  group: Impedances
- name: First secondary winding resistance (pu)
  summary: First secondary winding power loss 0.01 (default) | positive scalar
  group: Impedances
- name: Second secondary winding resistance (pu)
  summary: Second secondary winding power loss 0.01 (default) | positive scalar
  group: Impedances
- name: Leakage reactance
  summary: Leakage reactance modeling Exclude (default) | Include
  group: Impedances
- name: Primary leakage reactance (pu)
  summary: Primary winding magnetic flux loss 0.001 (default) | positive scalar
  group: Impedances
- name: First secondary leakage reactance (pu)
  summary: First secondary winding magnetic flux loss 0.001 (default) | positive scalar
  group: Impedances
- name: Second secondary leakage reactance (pu)
  summary: Second secondary winding magnetic flux loss 0.001 (default) | positive scalar
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
- name: Zero sequence reactance (pu)
  summary: Zero sequence reactance 0.5 (default) | positive scalar
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

Apparent power flowing through the transformer when operating at rated capacity. The
value must be greater than `0`.

### **Rated electrical frequency** — Connected network electrical frequency `60` `Hz` (default) | positive scalar

Rated or nominal frequency of the AC network to which the transformer is connected. The
value must be greater than `0`.

### **Primary winding connection type** — Primary winding configuration `Wye with floating neutral` (default) | `Wye with neutral port` | `Wye with grounded neutral` | `Delta 1 o'clock` | `Delta 11 o'clock`

Primary winding type.

### **Primary rated voltage** — RMS line voltage applied to the primary winding `4160` `V` (default) | positive scalar

RMS line voltage applied to the primary winding under normal operating conditions. The
value must be greater than `0`.

### **First secondary connection type** — First secondary winding configuration `Wye with floating neutral` (default) | `Wye with neutral port` | `Wye with grounded neutral` | `Delta 1 o'clock` | `Delta 11 o'clock`

First secondary winding type.

### **First secondary rated voltage** — RMS line voltage applied to the first secondary winding `24e3` `V` (default) | positive scalar

RMS line voltage applied to the first secondary winding under normal operating
conditions. The value must be greater than `0`.

### **Second secondary connection type** — Second secondary winding configuration `Wye with floating neutral` (default) | `Wye with neutral port` | `Wye with grounded neutral` | `Delta 1 o'clock` | `Delta 11 o'clock`

Second secondary winding type.

### **Second secondary rated voltage** — RMS line voltage applied to the second secondary winding `24e3` (default) | positive scalar

RMS line voltage applied to the second secondary winding under normal operating
conditions. The value must be greater than `0`.

### **Core type** — Number of limbs `Three-phase three-limb` (default) | `Three-phase five-limb`

Number of limbs that comprise the magnetic circuit.

#### Dependencies

**Zero sequence reactance (pu)**, an **Impedances**
parameter, is only visible when this parameter is set to
`Three-phase three-limb`.

### Impedances

### **Primary winding resistance (pu)** — Primary winding power loss `0.01` (default) | positive scalar

Per-unit power loss in the primary winding. The value must be greater than
`0`.

### **First secondary winding resistance (pu)** — First secondary winding power loss `0.01` (default) | positive scalar

Per-unit power loss in the first secondary winding. The value must be
greater than `0`.

### **Second secondary winding resistance (pu)** — Second secondary winding power loss `0.01` (default) | positive scalar

Per-unit power loss in the second secondary winding. The value must be
greater than `0`.

### **Leakage reactance** — Leakage reactance modeling `Exclude` (default) | `Include`

Whether to model magnetic flux losses.

### **Primary leakage reactance (pu)** — Primary winding magnetic flux loss `0.001` (default) | positive scalar

Per-unit magnetic flux loss in the primary winding. The value must be greater than
`0`.

#### Dependencies

To enable this parameter, set **Leakage
reactance** to
`Include`.

### **First secondary leakage reactance (pu)** — First secondary winding magnetic flux loss `0.001` (default) | positive scalar

Per-unit magnetic flux loss in the first secondary winding. The value must be greater
than `0`.

#### Dependencies

To enable this parameter, set **Leakage
reactance** to
`Include`.

### **Second secondary leakage reactance (pu)** — Second secondary winding magnetic flux loss `0.001` (default) | positive scalar

Per-unit magnetic flux loss in the second secondary winding. The value must be greater
than `0`.

#### Dependencies

To enable this parameter, set **Leakage
reactance** to
`Include`.

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

Choose if and how you want to represent the magnetic
saturation.

#### Dependencies

To enable this parameter, set **Magnetizing
reactance** to
`Include`.

### **Current vector (pu), i** — Per unit vector of currents `[0, .002, 1, 2]` (default)

Per unit vector of currents. The first value must be
`0`. This parameter must be strictly
ascending.

#### Dependencies

To enable this parameter, set **Magnetizing
reactance** to `Include` and
**Magnetic saturation representation** to
`Lookup table (phi versus i)`.

### **Magnetic flux vector (pu), phi** — Per unit vector of magnetic flux `[0, 1.2, 1.5, 1.51]` (default)

Per unit vector of magnetic flux. The first value must be
`0`. This parameter must be strictly
ascending.

#### Dependencies

To enable this parameter, set **Magnetizing
reactance** to `Include` and
**Magnetic saturation representation** to
`Lookup table (phi versus i)`.

### **Shunt magnetizing reactance (pu)** — Transformer core magnetic effects `500` (default) | positive scalar

Per-unit magnetic effects of the transformer core when operating in its linear region.
The value must be greater than `0`.

#### Dependencies

To enable this parameter, set **Magnetizing
reactance** to `Include` and
**Magnetic saturation representation** to
`None`.

### **Zero sequence reactance (pu)** — Zero sequence reactance `0.5` (default) | positive scalar

Per-unit zero sequence reactance. The value must be greater than or equal to the primary
winding magnetic flux loss.

#### Dependencies

To enable this parameter, set **Core type**, a
**Main** parameter, to `Three-phase
three-limb`.
## Libraries

Simscape / Electrical / Passive / Transformers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

## Description

Three-phase linear nonideal wye- and delta-configurable three-winding transformer with saturation capability

The Three-Winding Transformer (Three-Phase) block represents
a linear nonideal three-phase three-winding transformer that transfers electrical energy
between two or more circuits through electromagnetic induction. The block includes
linear winding leakage and linear core magnetization effects. You can parameterize the
block impedance using per-unit values. The primary, first secondary , and second
secondary winding types, delta-wye phase angle, and core types are configurable.

The configuration options for the primary and secondary winding types are:

- Wye with floating neutral — Star or T configuration with Floating
  Neutral (Three-Phase)
- Wye with neutral port — Star or T configuration with Neutral Port
  (Three-Phase)
- Wye with grounded neutral — Star or T configuration with Grounded
  Neutral (Three-Phase)
- Delta 1 o'clock — Mesh configuration with a lagging 30 degree phase shift relative to
  the voltage of a connected wye configuration
- Delta 11 o'clock — Mesh configuration with leading 30 degree phase shift relative to
  the voltage of a connected wye configuration

Options for the core type are:

- Three-phase five-limb
- Three-phase three-limb

Although a three-limbs core is typically less expensive, a five-limb core
offers these advantages:

- Lower impedance for the zero-sequence component of current, that is
  between the line and neutral, in the case of an unbalanced load
- Greater heat dissipation

### Equations

**Three-Limb Core**

This block is implemented in the magnetic domain using basic magnetic
reluctances, windings, and eddy currents blocks.

It is important to determine the relation between the electrical domain
parameters from the block mask and the magnetic domain parameters used in the model:

- *n1* is the number of the
  primary winding turns.
- *n2* is the number of the
  first secondary winding turns.
- *n3* is the number of the
  second secondary winding turns.
- *Lm* is the shunt
  magnetizing inductance.
- *L0* is the zero-sequence
  inductance.
- *Lp* is the primary
  winding leakage inductance.
- *Ls1* is the first
  secondary winding leakage inductance.
- *Ls2* is the second
  secondary winding leakage inductance.
- *Rm* is the shunt
  magnetizing resistance.
- *R* is the magnetizing reluctance between
  phases.

  R=n12Lm
- *R0* is the zero sequence
  reluctance.

  R0=13n12L0−Lp
- *Rl1* is the primary
  winding leakage reluctance.

  Rl1=n12Lp
- *Rl2* is the first winding
  secondary leakage reluctance.

  Rl2=n22Ls1
- *Rl3* is the second
  winding secondary leakage reluctance.

  Rl3=n32Ls2
- *Leddy* is the conductance
  of eddy current loop

  Leddy=n12Rm

For three-winding transformers (three-phase), the coupling
between different windings in each phase is identical.

**Five-Limb Core**

In the case of a five-limb transformer, the extra magnetic flux paths provided
by the extra limbs can be represented by zero sequence reluctances, which are
originally designed for magnetic paths through the air in the three-limb
transformer.

In a five-limb model, the magnetic reluctances from the phases to the extra
limbs are supposed to be equal to the magnetic reluctances between phases.

R=R0

Therefore we deduce:

R=R0=n12Lm

### Display Options

You can display the transformer per-unit base values in the MATLAB® command window using the block context menu. To display the values,
right-click the block and select **Electrical** > **Display Base Values**.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. You can
specify nominal values using different sources, including the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
