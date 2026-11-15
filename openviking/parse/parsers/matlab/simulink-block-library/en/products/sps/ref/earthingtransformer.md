---
type: simulink-block
title: 'Earthing Transformer'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / Transformers'
documentation_page: 'earthingtransformer'
documentation_source_path: 'ref/earthingtransformer.html'
language: en
---

# Earthing Transformer

## Ports

### Conserving

### **~** — Three-phase voltage electrical

Expandable three-phase
electrical conserving port associated with three-phase
voltage.

### **n** — Neutral electrical

Electrical three-phase
electrical conserving port associated with the neutral
point.

## Parameters

### **Modeling option** — Whether to model composite or expanded three-phase ports `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical conserving ports
with a single block port. You can use composite three-phase ports to build models that
correspond to single-line diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a three-phase system
using three separate electrical conserving ports.

### **Rated apparent power** — Rated apparent power `100e6` `V*A` (default) | positive scalar

Rated apparent power in SI units. The value must be greater than
`0`.

### **Rated voltage** — Rated voltage `24e3` `V` (default) | positive scalar

Rated voltage in SI units. The value must be greater than 0.

### **Rated electrical frequency** — Rated electrical frequency `60` `Hz` (default) | positive scalar

Rated electrical frequency in SI units. The value must be greater than
`0`.

### **Units** — Parameterization unit system `Per unit` (default) | `SI`

System of units for impedance parameterization.

#### Dependencies

The visibility of other parameters depends on the value of this
parameter.

### **Zero-sequence resistance (pu)** — Zero-sequence resistance `0.01` (default) | positive scalar

Per-unit zero-sequence resistance. The value must be greater than
`0`.

#### Dependencies

This parameter is only visible when the **Units**
parameter is set to `Per unit`.

### **Zero-sequence reactance (pu)** — Zero-sequence reactance `0.3` (default) | positive scalar

Per-unit zero-sequence reactance. The value must be greater than
`0`.

#### Dependencies

This parameter is only visible when the **Units**
parameter is set to `Per unit`.

### **Shunt magnetizing resistance (pu)** — Shunt magnetizing resistance `500` (default) | positive scalar

Per-unit shunt magnetizing resistance. The value must be greater than
`0`.

#### Dependencies

This parameter is only visible when the **Units**
parameter is set to `Per unit`.

### **Shunt magnetizing reactance (pu)** — Shunt magnetizing reactance `500` (default) | positive scalar

Per-unit shunt magnetizing reactance. The value must be greater than
`0`.

#### Dependencies

This parameter is only visible when the **Units**
parameter is set to `Per unit`.

### **Zero-sequence resistance** — Zero-sequence resistance `0.0576` `Ohm` (default) | positive scalar

Zero-sequence resistance in SI units. The value must be greater than
`0`.

#### Dependencies

This parameter is only visible when the **Units**
parameter is set to `SI`.

### **Zero-sequence inductance** — Zero-sequence inductance `1.728` `H` (default) | positive scalar

Zero-sequence inductance in SI units. The value must be greater than
`0`.

#### Dependencies

This parameter is only visible when the **Units**
parameter is set to `SI`.

### **Shunt magnetizing resistance** — Shunt magnetizing resistance `2880` `Ohm` (default) | positive scalar

Shunt magnetizing resistance in SI units. The value must be greater than
`0`.

#### Dependencies

This parameter is only visible when the **Units**
parameter is set to `SI`.

### **Shunt magnetizing inductance** — Shunt magnetizing inductance `2880` `H` (default) | positive scalar

Shunt magnetizing inductance in SI units. The value must be greater than
`0`.

#### Dependencies

This parameter is only visible when the **Units**
parameter is set to `SI`.

## Libraries

Simscape / Electrical / Passive / Transformers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

## Description

Three-phase earthing transformer in zigzag configuration

The Earthing Transformer block models a three-phase
zigzag-connection earthing or grounding transformer. The block allows you to provide an
artificial neutral in an ungrounded three-phase power system. The artificial neutral
creates a low-impedance path for the zero-sequence current and high-impedance path for
the positive-sequence current. To accommodate a phase-to-neutral load, the return path
allows a delta-connected supply.

For more information on using a three-phase zigzag-connection earthing or grounding
transformer, see Engineering Applications

### Equations

This block is implemented in both electrical and magnetic domains, representing
the physics of phase windings and magnetic core. The equivalent circuit for the
block includes windings, reluctances, and eddy currents.

For a zigzag configuration in magnetic circuit, the *a*-.
*b*-, and *c*-phases represent each leg of the
magnetic core.

You can obtain the relationship between the electrical and the magnetic properties
by applying several mathematical steps based on the magnetic flux conservation rule
and on the Hopkinson's law.

For earthing transformers, the couplings between the phases and all the windings
are identical. In the equations below:

- *n* is the number of turns of the winding.
- *R* is the magnetizing reluctance between
  phases.
- *RL* is the leakage
  reluctance.
- *Leddy* is the magnetic
  inductance due to eddy current losses between phases.

Then the relationship between the inductance matrix in electrical domain and the
reluctance matrix in the magnetic domain can be written as:

L​=[L11L12L13L21L22L23L31L32L33]=[n2(2Rl+6R)−3n2R−3n2R−3n2Rn2(2Rl+6R)−3n2R−3n2R−3n2Rn2(2Rl+6R)]

The diagonal elements represent the sum of a leakage and magnetizing inductance
for each phase, such that:

Ll=2n2Rl

Therefore:

RL=2n2Ll

R=9n2Lm

Leddy=9n2Rm
