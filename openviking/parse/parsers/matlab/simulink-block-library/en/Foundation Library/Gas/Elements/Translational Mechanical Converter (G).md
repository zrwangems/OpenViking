---
type: simulink-block
title: 'Translational Mechanical Converter (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Elements'
documentation_page: 'translationalmechanicalconverterg'
documentation_source_path: 'ref/translationalmechanicalconverterg.html'
language: en
---

# Translational Mechanical Converter (G)

## Ports
```yaml
ports:
- name: p
  summary: Displacement of port R relative to port C, m physical signal
  direction: input
- name: A
  summary: Converter inlet gas
  direction: conserving
- name: H
  summary: Temperature inside converter thermal
  direction: conserving
- name: R
  summary: Rod mechanical translational
  direction: conserving
- name: C
  summary: Case mechanical translational
  direction: conserving
```

### Input

### **p** — Displacement of port R relative to port C, m physical signal

Input physical signal that passes the position information from a
Simscape™
Multibody™ joint. Connect this port to the position sensing port
**p** of the joint. For more information, see Connecting Simscape Networks to Simscape Multibody Joints.

#### Dependencies

To enable this port, set the **Interface
displacement** parameter to `Provide input
signal from Multibody joint`.
### Conserving

### **A** — Converter inlet gas

Gas conserving port associated with the converter inlet.

### **H** — Temperature inside converter thermal

Thermal conserving port associated with the temperature of the
gas inside the converter.

### **R** — Rod mechanical translational

Mechanical translational conserving port associated with the
moving interface.

### **C** — Case mechanical translational

Mechanical translational conserving port associated with the
converter casing.
## Parameters
```yaml
parameters:
- name: Mechanical orientation
  summary: Select the converter orientation Pressure at A causes positive displacement of R relative to C (default) | Pressure
    at A causes negative displacement of R relative to C
  group: ''
- name: Interface displacement
  summary: Select method to determine relative port positions Calculate from velocity of port R relative to port C (default)
    | Provide input signal from Multibody joint
  group: ''
- name: Initial interface displacement
  summary: Translational offset of port R relative to port C at the start of simulation 0 m (default)
  group: ''
- name: Interface cross-sectional area
  summary: The area on which the gas exerts pressure to generate the translational force 0.01 m^2 (default)
  group: ''
- name: Dead volume
  summary: Volume of gas when the interface displacement is 0 1e-5 m^3 (default)
  group: ''
- name: Cross-sectional area at port A
  summary: Area normal to flow path at the converter inlet 0.01 m^2 (default)
  group: ''
- name: Environment pressure specification
  summary: Select a specification method for the environment pressure Atmospheric pressure (default) | Specified pressure
  group: ''
- name: Environment pressure
  summary: Pressure outside the converter 0.101325 MPa (default)
  group: ''
```

### **Mechanical orientation** — Select the converter orientation `Pressure at A causes positive displacement of R relative to C` (default) | `Pressure at A causes negative displacement of R relative to C`

Select the relative orientation of the converter with respect
to the converter gas volume:

- `Pressure at A causes positive displacement of R
  relative to C` — Increase in the gas volume
  results in a positive displacement of port **R**
  relative to port **C**.
- `Pressure at A causes negative displacement of R
  relative to C` — Increase in the gas volume
  results in a negative displacement of port **R**
  relative to port **C**.

### **Interface displacement** — Select method to determine relative port positions `Calculate from velocity of port R relative to port C` (default) | `Provide input signal from Multibody joint`

Select method to determine displacement of port **R**
relative to port **C**:

- `Calculate from velocity of port R relative to port
  C` — Calculate displacement from relative
  port velocities, based on the block equations. This is the default
  method.
- `Provide input signal from Multibody
  joint` — Enable the input physical signal
  port **p** to pass the displacement information
  from a Multibody joint. Use this method only when you connect the
  converter to a Multibody joint by using a
  Translational Multibody Interface
  block. For more information, see How to Pass Position Information.

### **Initial interface displacement** — Translational offset of port R relative to port C at the start of simulation `0 m` (default)

Translational offset of port **R** relative to port
**C** at the start of simulation. A value of 0
corresponds to an initial gas volume equal to **Dead
volume**.

#### Dependencies

Enabled when the **Interface displacement** parameter
is set to `Calculate from velocity of port R relative to
port C`.

- If **Mechanical orientation** is
  `Pressure at A causes positive displacement of R
  relative to C`, the parameter value must be
  greater than or equal to 0.
- If **Mechanical orientation** is
  `Pressure at A causes negative displacement of R
  relative to C`, the parameter value must be
  less than or equal to 0.

### **Interface cross-sectional area** — The area on which the gas exerts pressure to generate the translational force `0.01 m^2` (default)

The area on which the gas exerts pressure to generate the translational
force.

### **Dead volume** — Volume of gas when the interface displacement is 0 `1e-5 m^3` (default)

Volume of gas when the interface displacement is 0.

### **Cross-sectional area at port A** — Area normal to flow path at the converter inlet `0.01 m^2` (default)

The cross-sectional area of the converter inlet, in the direction
normal to gas flow path.

### **Environment pressure specification** — Select a specification method for the environment pressure `Atmospheric pressure` (default) | `Specified pressure`

Select a specification method for the environment pressure:

- `Atmospheric pressure` — Use the
  atmospheric pressure, specified by the Gas Properties
  (G) block connected to the circuit.
- `Specified pressure` —
  Specify a value by using the **Environment pressure** parameter.

### **Environment pressure** — Pressure outside the converter `0.101325 MPa` (default)

Pressure outside the converter acting against the pressure of
the converter gas volume. A value of 0 indicates that the converter
expands into vacuum.

#### Dependencies

Enabled when the **Environment pressure specification** parameter
is set to `Specified pressure`.
## Libraries

Simscape / Foundation Library / Gas / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

## Description

Interface between gas and mechanical translational networks

The Translational Mechanical Converter (G) block models an
interface between a gas network and a mechanical translational network. The block
converts gas pressure into mechanical force and vice versa. It can be used as a building
block for linear actuators.

The converter contains a variable volume of gas. The pressure and temperature evolve based on
the compressibility and thermal capacity of this gas volume. The **Mechanical
orientation** parameter lets you specify whether an increase in the gas
volume results in a positive or negative displacement of port **R**
relative to port **C**.

Port **A** is the gas conserving port associated with the converter inlet.
Port **H** is the thermal conserving port associated with the
temperature of the gas inside the converter. Ports **R** and
**C** are the mechanical translational conserving ports associated
with the moving interface and converter casing, respectively.

### Mass Balance

Mass conservation equation is similar to that for the Constant Volume Chamber (G)
block, with an additional term related to the change in gas volume:

∂M∂p⋅dpIdt+∂M∂T⋅dTIdt+ρIdVdt=m˙A

where:

- ∂M∂p is
  the partial derivative of the mass of the gas volume with respect
  to pressure at constant temperature and volume.
- ∂M∂T is
  the partial derivative of the mass of the gas volume with respect
  to temperature at constant pressure and volume.
- *p*I is the pressure of the gas
  volume. Pressure at port **A** is assumed equal to this
  pressure, *p*A =
  *p*I.
- *T*I is the temperature of the gas
  volume. Temperature at port **H** is assumed equal to this
  temperature, *T*H =
  *T*I.
- *ρ*I is
  the density of the gas volume.
- *V* is the volume of gas.
- *t* is time.
- m˙A is the mass flow rate at port
  **A**. Flow rate associated with a port is positive
  when it flows into the block.

### Energy Balance

Energy conservation equation is also similar to that for the Constant Volume Chamber (G)
block. The additional term accounts for the change in gas volume, as well as the
pressure-volume work done by the gas on the moving interface:

∂U∂p⋅dpIdt+∂U∂T⋅dTIdt+ρIhIdVdt=ΦA+QH

where:

- ∂U∂p is
  the partial derivative of the internal energy of the gas volume with
  respect to pressure at constant temperature and volume.
- ∂U∂T is
  the partial derivative of the internal energy of the gas volume with
  respect to temperature at constant pressure and volume.
- ФA is the energy flow rate at port
  **A**.
- *Q*H is the heat flow rate at port
  **H**.
- *h*I is the
  specific enthalpy of the gas volume.

### Partial Derivatives for Perfect and Semiperfect Gas Models

The partial derivatives of the mass *M* and the internal energy
*U* of the gas volume, with respect to pressure and temperature at
constant volume, depend on the gas property model. For perfect and semiperfect gas models,
the equations are:

∂M∂p=VρIpI∂M∂T=−VρITI∂U∂p=V(hIZRTI−1)∂U∂T=VρI(cpI−hITI)

where:

- *ρ*I is
  the density of the gas volume.
- *V* is the volume of gas.
- *h*I is the
  specific enthalpy of the gas volume.
- *Z* is the compressibility factor.
- *R* is the specific gas constant.
- *c*pI is the
  specific heat at constant pressure of the gas volume.

### Partial Derivatives for Real Gas Model

For real gas model, the partial derivatives of the mass *M* and the internal
energy *U* of the gas volume, with respect to pressure and temperature at
constant volume, are:

∂M∂p=VρIβI∂M∂T=−VρIαI∂U∂p=V(ρIhIβI−TIαI)∂U∂T=VρI(cpI−hIαI)

where:

- *β* is the isothermal bulk
  modulus of the gas volume.
- *α* is the isobaric thermal
  expansion coefficient of the gas volume.

### Gas Volume

The gas volume depends on the displacement of the moving interface:

V=Vdead+Sintxintεint

where:

- *V*dead is
  the dead volume.
- *S*int is
  the interface cross-sectional area.
- *x*int is
  the interface displacement.
- *ε*int is the mechanical
  orientation coefficient. If **Mechanical orientation** is
  `Pressure at A causes positive displacement of R relative to
  C`, *ε*int =
  1. If **Mechanical orientation** is
  `Pressure at A causes negative displacement of R relative to
  C`, *ε*int =
  –1.

If you connect the converter to a Multibody joint, use the physical signal input
port **p** to specify the displacement of port
**R** relative to port **C**. Otherwise, the
block calculates the interface displacement from relative port velocities. The
interface displacement is zero when the gas volume is equal to the dead volume.
Then, depending on the **Mechanical orientation** parameter
value:

- If `Pressure at A causes positive displacement of R relative
  to C`, the interface displacement increases when the gas
  volume increases from dead volume.
- If `Pressure at A causes negative displacement of R relative
  to C`, the interface displacement decreases when the gas
  volume increases from dead volume.

### Force Balance

Force balance across the moving interface on the gas volume
is

Fint=(penv−pI)Sintεint

where:

- *F*int is the force from port
  **R** to port **C**.
- *p*env is
  the environment pressure.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables and Initial Conditions for Blocks with Finite Gas Volume.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.

### Assumptions and Limitations

- The converter casing is perfectly rigid.
- There is no flow resistance between port **A** and
  the converter interior.
- There is no thermal resistance between port **H** and
  the converter interior.
- The moving interface is perfectly sealed.
- The block does not model mechanical effects of the
  moving interface, such as hard stop, friction, and inertia.
