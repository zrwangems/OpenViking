---
type: simulink-block
title: 'Transmission Line (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / Lines'
documentation_page: 'transmissionlinethreephase'
documentation_source_path: 'ref/transmissionlinethreephase.html'
language: en
---

# Transmission Line (Three-Phase)

## Ports

### Conserving

### **~1** — Three-phase port electrical

Expandable three-phase
port.

### **~2** — Three-phase port electrical

Expandable three-phase
port.

### **g1** — Ground connection at end ~1 electrical

Electrical conserving port corresponding to ground connection at
`~1` end of the transmission line.

### **g2** — Ground connection at end ~2 electrical

Electrical conserving port corresponding to ground connection at
`~2` end of the transmission line.

### **g1'** — Ground connection at fault position 1 electrical

Electrical conserving port corresponding to ground connection at fault
position 1.

#### Dependencies

To enable this port, set **Accessible ground connections
at section interface** to
`Yes`

### **g2'** — Ground connection at fault position 2 electrical

Electrical conserving port corresponding to ground connection at fault
position 2.

#### Dependencies

To enable this port, set **Accessible ground connections
at section interface** to
`Yes`

## Parameters

### **Modeling option** — Whether to model composite or expanded three-phase ports `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical conserving ports
with a single block port. You can use composite three-phase ports to build models that
correspond to single-line diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a three-phase system
using three separate electrical conserving ports.

### Main

### **Line length** — Length of the transmission line `1` `km` (default)

Length of the transmission line.

### **Frequency used for rlcg specification** — Frequency used for rlcg specification `60` `Hz` (default) | positive scalar

Frequency used for the R, L, C, G specification, where:

- **R** is line resistance per unit
  length.
- **L** is the line inductance per unit
  length.
- **C** is the line capacitance per unit
  length.
- **G** is the line conductance per unit
  length.

### **Resistance** — Resistance of the transmission line `0.02` `Ohm/km` (default)

Resistance of the transmission line per phase per-unit length.

### **Inductance** — Self-inductance of the transmission line `0.5` `mH/km` (default)

Self-inductance of the transmission line per phase per-unit
length.

### **Mutual inductance** — Line-line mutual inductance `0.1` `mH/km` (default)

Line-line mutual inductance per-unit length. Set this to
`0` to remove mutual inductance.

### **Line-line capacitance** — Line-line capacitance `0.3` `μF/km` (default)

Line-line capacitance length, in per-unit.

### **Line-ground capacitance** — Line-ground capacitance `0.1` `μF/km` (default)

Line-ground capacitance length, in per-unit.

### **Mutual resistance** — Line-line mutual resistance `0` `Ohm/km` (default)

Line-line mutual resistance per unit length. The default value is
`0``Ohm/km` (no line-line
mutual resistance).

### **Model two line sections** — Line-line mutual resistance `No` (default) | `Yes`

Option to model the transmission line as two sections. You must enable
this parameter to add a non-intrusive fault in the
Transmission Line (Three-Phase)
block.

### **Number of segments** — Number of segments `1` (default)

Number of segments in the pi-line model.

#### Dependencies

To enable this parameter, set **Model two line
sections** to `No`.

### **Position of section interface** — Position of section interface `0.5` `Km` (default)

Position of the interface in the pi-line model. If you add a
non-intrusive fault, this parameter represents the position of the fault
in the pi-line model.

#### Dependencies

To enable this parameter, set **Model two line
sections** to `Yes`.

### **Number of segments in first section** — Number of segments in first section `1` (default)

Number of segments in the first section of the pi-line model. If you
add a non-intrusive fault, this parameter represents the number of
segments before the fault occurs.

#### Dependencies

To enable this parameter, set **Model two line
sections** to `Yes`.

### **Number of segments in second section** — Number of segments in second section `1` (default)

Number of segments in the second section of the pi-line model. If you
add a non-intrusive fault, this parameter represents the number of
segments after the fault occurs.

#### Dependencies

To enable this parameter, set **Model two line
sections** to `Yes`.

### **Accessible ground connections at section interface** — Option to access ground connections at fault position `No` (default) | `Yes`

Option to access the ground connections at the fault position. If you
set this parameter to `No`, the block
internally connects the ground connections at the fault position to the
electrical reference.

#### Dependencies

To enable this parameter set **Model two line
sections** to `Yes`.

### Parasitics

### **Parasitic series resistance** — Parasitic series resistance `1e-6` `Ohm` (default)

Resistance value, divided by the number of segments, that is added in
series with every capacitor in the model.

### **Parasitic parallel conductance** — Parasitic parallel conductance `1e-6` `1/Ohm` (default)

Conductance value, divided by the number of segments, that is added in
parallel with every series resistor and inductor in the model.

### Faults

To modify the faults, create a fault and, in the block dialog
box, click **Open fault properties**. To open the faults, in the Property
Inspector, click the **Fault behavior** link.

### **Section interface fault** — Option to add fault to section interface `Add fault`

Option to add a fault to the section interface of the pi-line
model.

To add a fault, click the **Add fault**
hyperlink.

#### Dependencies

To enable this parameter, set **Model two line
sections** to `Yes`.

### **Fault type** — Type of fault `Single-phase to ground (a-g)` (default) | `Single-phase to ground (b-g)` | `Single-phase to ground (c-g)` | `Two-phase (a-b)` | `Two-phase (b-c)` | `Two-phase (c-a)` | `Two-phase to ground (a-b-g)` | `Two-phase to ground (b-c-g)` | `Two-phase to ground (c-a-g)` | `Three-phase (a-b-c)` | `Three-phase to ground (a-b-c-g)`

Type of fault to model. The visibility of related parameters depends
on the fault model. Options are:

- `Single-phase to ground (a-g)`
- `Single-phase to ground (b-g)`
- `Single-phase to ground (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground (a-b-g)`
- `Two-phase to ground (b-c-g)`
- `Two-phase to ground (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground
  (a-b-c-g)`

#### Dependencies

To enable this parameter, add a fault to the Transmission Line (Three-Phase) block by
clicking the **Add fault** hyperlink next to the
**Section interface fault** parameter.

### **Faulted phase-neutral resistance** — Faulted phase-neutral resistance `1e-3` `Ohm` (default)

Resistance between the phase connection and the neutral point when the
fault is active.

#### Dependencies

To enable this parameter, add a fault to the
Transmission Line (Three-Phase)
block by clicking the **Add fault** hyperlink next
to the **Section interface fault** parameter and
set the **Fault type** parameter to:

- `Single-phase to ground
  (a-g)`
- `Single-phase to ground
  (b-g)`
- `Single-phase to ground
  (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground
  (a-b-g)`
- `Two-phase to ground
  (b-c-g)`
- `Two-phase to ground
  (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground
  (a-b-c-g)`

### **Faulted neutral-ground resistance** — Faulted neutral-ground resistance `1e-3` `Ohm` (default)

Resistance between the neutral point and the electrical reference when
fault is active.

#### Dependencies

To enable this parameter, add a fault to the
Transmission Line (Three-Phase)
block by clicking the **Add fault** hyperlink next
to the **Section interface fault** parameter and
set the **Fault type** parameter to:

- `Single-phase to ground
  (a-g)`
- `Single-phase to ground
  (b-g)`
- `Single-phase to ground
  (c-g)`
- `Two-phase to ground
  (a-b-g)`
- `Two-phase to ground
  (b-c-g)`
- `Two-phase to ground
  (c-a-g)`
- `Three-phase to ground
  (a-b-c-g)`

### **Unfaulted phase-neutral conductance** — Unfaulted phase-neutral conductance `1e-6` `1/Ohm` (default)

Conductance between the phase connection and the neutral point when
the fault is not active.

#### Dependencies

To enable this parameter, add a fault to the
Transmission Line (Three-Phase)
block by clicking the **Add fault** hyperlink next
to the **Section interface fault** parameter and
set the **Fault type** parameter to:

- `Single-phase to ground
  (a-g)`
- `Single-phase to ground
  (b-g)`
- `Single-phase to ground
  (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground
  (a-b-g)`
- `Two-phase to ground
  (b-c-g)`
- `Two-phase to ground
  (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground
  (a-b-c-g)`

## Libraries

Simscape / Electrical / Passive / Lines

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Three-phase transmission line using lumped-parameter pi-section line model

The Transmission Line (Three-Phase) block models a
three-phase transmission line using the lumped-parameter pi-line model. This model takes
into account phase resistance, phase self-inductance, line-line mutual inductance and
resistance, line-line capacitance, and line-ground capacitance.

To simplify the block-defining equations, Clarke’s transformation is used. The
resulting equations are:

V1′−V2′=[R+2RmR−RmR−Rm]I1′+[L+2ML−ML−M]dI1′dt

I1′+I2′=[CgCg+3ClCg+3Cl]dV2′dt

I1′=T′I1

I2′=T′I2

V1′=T′V1

V2′=T′V2

T=13[1201−12321−12−32]

where:

- *R* is the line resistance for the segment.
- *Rm* is the mutual resistance for
  the segment.
- *L* is the line inductance for the segment.
- *M* is the value of the **Mutual
  inductance** parameter.
- *Cg* is the line-ground
  capacitance for the segment.
- *Cl* is the line-line capacitance
  for the segment.
- *T* is the Clarke’s transformation matrix.
- *I1* is the three-phase current flowing into the
  `~1` port.
- *I2* is the three-phase current flowing into the
  `~2` port.
- *V1* is the three-phase voltage at the
  `~1` port.
- *V2* is the three-phase voltage at the
  `~2` port.

The positive and zero-sequence parameters are defined by the diagonal terms in the
transformed equations:

R0=R+2Rm

R1=R−Rm

L0=L+2M

L1=L−M

C0=Cg

C1=Cg+3Cl

Rearranging these equations gives the physical line quantities in terms of positive
and zero-sequence parameters:

R=2R1+R03

Rm=R0−R13

L=2L1+L03

M=L0−L13

Cl=C1−C03

Cg=C0

The figure shows the equivalent electrical circuit for a single-segment pi-line model
using Clarke’s transformation.

To increase fidelity, you can use the **Number of segments**
parameter to repeat the pi-section N times, resulting in an N-segment transmission line
model. More segments significantly slows down your simulation.

To improve numerical performance, you can add parasitic resistance and conductance
components. Choosing large values for these components improves simulation speed but
decreases simulation accuracy.

### Propagation Speeds

The Transmission Line (Three-Phase) calculates the
positive-sequence propagation speeds by using these equations:

- Z1=R1+jωL1 is the series impedance, in
  `Ω/Km`.
- Y1=jωC1 is the shunt admittance, in
  `s/Km`.
- γ1=Z1Y1 is the propagation constant.
- ν1=ωImag(γ1) is the propagation speed, in `Km/s`,
  where ω=2πf.

For zero-sequence propagation speed, the equations are the same but
*R1*,
*L1*,
*C1*,
*Z1*,
*Y1*,
*γ1*, and
*ν1* are
*R0*,
*L0*,
*C0*,
*Z0*,
*Y0*,
*γ0*, and
*ν0*.

### Faults

To model a fault in the Transmission Line (Three-Phase) block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The Transmission Line (Three-Phase) block allows
you to model these types of faults at specific position along the transmission line:

- Single-phase-to-ground fault (a-g, b-g, or c-g)
- Two-phase fault (a-b, b-c, or c-a)
- Two-phase-to-ground fault (a-b-g, b-c-g, or c-a-g)
- Three-phase fault (a-b-c)
- Three-phase-to-ground fault (a-b-c-g)
