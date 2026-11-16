---
type: simulink-block
title: 'Translational Mechanical Converter (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Elements'
documentation_page: 'translationalmechanicalconverteril'
documentation_source_path: 'ref/translationalmechanicalconverteril.html'
language: en
---

# Translational Mechanical Converter (IL)

## Ports

### Input

### **p** — Displacement of port R relative to port C, m physical signal

Input physical signal that passes the position information from a Simscape™
Multibody™ joint. Connect this port to the position sensing port
**p** of the joint. For more information, see Connecting Simscape Networks to Simscape Multibody Joints.

#### Dependencies

To enable this port, set the **Interface displacement**
parameter to `Provide input signal from Multibody
joint`.
### Conserving

### **A** — Converter inlet isothermal liquid

Isothermal liquid conserving port associated with the converter inlet.

### **R** — Rod mechanical translational

Mechanical translational conserving port associated with the moving
interface.

### **C** — Case mechanical translational

Mechanical translational conserving port associated with the converter
casing.

## Parameters

### **Mechanical orientation** — Select the converter orientation `Pressure at A causes positive displacement of R relative to C` (default) | `Pressure at A causes negative displacement of R relative to C`

Select the alignment of moving interface with respect to fluid pressure:

- `Pressure at A causes positive displacement of R relative to
  C` — Increase in the fluid pressure results in a positive
  displacement of port **R** relative to port
  **C**.
- `Pressure at A causes negative displacement of R relative to
  C` — Increase in the fluid pressure results in a negative
  displacement of port **R** relative to port
  **C**.

### **Interface displacement** — Select method to determine relative port positions `Calculate from velocity of port R relative to port C` (default) | `Provide input signal from Multibody joint`

Select method to determine displacement of port **R** relative to
port **C**:

- `Calculate from velocity of port R relative to port C`
  — Calculate displacement from relative port velocities, based on the mass
  balance equations. This is the default method.
- `Provide input signal from Multibody joint` —
  Enable the input physical signal port **p** to pass the
  displacement information from a Multibody joint. Use this method only when you
  connect the converter to a Multibody joint by using a Translational
  Multibody Interface block. For more information, see How to Pass Position Information.

### **Initial interface displacement** — Translational offset of port R relative to port C at the start of simulation `0 m` (default) | scalar

Translational offset of port **R** relative to port
**C** at the start of simulation. A value of 0 corresponds to an
initial liquid volume equal to **Dead volume**.

#### Dependencies

Enabled when the **Interface displacement** parameter is set to
`Calculate from velocity of port R relative to port
C`.

- If **Mechanical orientation** is `Pressure at A
  causes positive displacement of R relative to C`, the parameter
  value must be greater than or equal to 0.
- If **Mechanical orientation** is `Pressure at A
  causes negative displacement of R relative to C`, the parameter
  value must be less than or equal to 0.

### **Interface cross-sectional area** — The area on which the liquid exerts pressure to generate the translational force `0.01 m^2` (default) | positive scalar

The area on which the liquid exerts pressure to generate the translational force.

### **Dead volume** — Volume of liquid when the interface displacement is 0 `1e-5 m^3` (default) | positive scalar

Volume of liquid when the interface displacement is 0.

### **Environment pressure specification** — Select a specification method for the environment pressure `Atmospheric pressure` (default) | `Specified pressure`

Select a specification method for the pressure outside the converter:

- `Atmospheric pressure` — Use the atmospheric
  pressure, specified by the Isothermal Liquid Properties
  (IL) block connected to the circuit.
- `Specified pressure` — Specify a value by using
  the **Environment pressure** parameter.

### **Environment pressure** — Pressure outside the converter `0.101325 MPa` (default) | positive scalar

Pressure outside the converter acting against the pressure of the converter liquid
volume. A value of 0 indicates that the converter expands into vacuum.

#### Dependencies

Enabled when the **Environment pressure specification** parameter
is set to `Specified pressure`.

### **Enable dynamic compressibility** — Select whether to model fluid dynamic compressibility `On` (default) | `Off`

Select whether to account for the dynamic compressibility of the liquid. Dynamic
compressibility gives the liquid density a dependence on pressure and temperature,
impacting the transient response of the system at small time scales.

### **Initial liquid pressure** — Liquid pressure at time zero `0.101325 MPa` (default) | positive scalar

Liquid pressure in the converter at the start of simulation.

#### Dependencies

To enable this parameter, select the **Enable dynamic
compressibility** check box.

### **Nominal liquid pressure** — Liquid pressure at nominal operating conditions `0.101325 MPa` (default)

Thermal liquid pressure at nominal operating conditions. The block uses this value
to calculate the nominal density to use in the mass conservation equation when dynamic
compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** check box.

## Libraries

Simscape / Foundation Library / Isothermal Liquid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Interface between isothermal liquid and mechanical translational networks

The Translational Mechanical Converter (IL) block models an
interface between an isothermal liquid network and a mechanical translational network. The
block converts isothermal liquid pressure into mechanical force and vice versa. It can be used
as a building block for linear actuators.

The converter contains a variable volume of liquid. If the **Enable dynamic
compressibility** check box is selected, then the pressure evolves based on the
dynamic compressibility of the liquid volume. The **Mechanical orientation**
parameter lets you specify whether an increase in pressure moves port **R**
away from or towards port **C**.

Port **A** is the isothermal liquid conserving port associated with the
converter inlet. Ports **R** and **C** are the mechanical
translational conserving ports associated with the moving interface and converter casing,
respectively.

### Mass Balance

The mass conservation equations in the mechanical converter volume are

m˙A={ε ρIS v,if fluid dynamic compressibility is offε ρIS v+1βIdpIdtρIV,if fluid dynamic compressibility is onv=dxdtv=vR−vCV=Vdead+εSx

where:

- m˙A is the mass flow rate into the converter through port
  **A**.
- *ε* is the mechanical orientation of the converter
  (`1` if increase in fluid pressure causes positive displacement of R
  relative to C, `-1` if increase in fluid pressure causes negative
  displacement of R relative to C).
- *ρ*I is the fluid density inside the
  converter.
- *β*I is the fluid bulk modulus inside the
  converter.
- *S* is the cross-sectional area of the converter interface.
- *v* is the translational velocity of the converter
  interface.
- *v*R and
  *v*C are the translational velocities of ports
  **R** and **C**, respectively.
- *x* is the displacement of the converter interface.
- *V* is the liquid volume inside the converter.
- *V*dead is the dead volume, that is, volume
  of liquid when the interface displacement is 0.
- *p*I is the pressure inside the
  converter.

If you connect the converter to a Multibody joint, use the physical signal input port
**p** to specify the displacement of port **R** relative
to port **C**. Otherwise, the block calculates the interface displacement
from relative port velocities, according to the equations above. The interface displacement
is zero when the liquid volume is equal to the dead volume. Then, depending on the
**Mechanical orientation** parameter value:

- If `Pressure at A causes positive displacement of R relative to
  C`, the interface displacement increases when the liquid volume increases
  from dead volume.
- If `Pressure at A causes negative displacement of R relative to
  C`, the interface displacement decreases when the liquid volume increases
  from dead volume.

Equations used to compute the fluid mixture density and bulk modulus depend on the
selected isothermal liquid model. For detailed information, see Isothermal Liquid Modeling Options.

### Momentum Balance

The momentum conservation equation in the mechanical converter volume is

F=ε(penv−p)S,

where:

- *F* is the force the liquid exerts on the converter
  interface.
- *p*env is the environment pressure outside
  the converter.

### Assumptions and Limitations

- Converter walls are perfectly rigid.
- The converter contains no mechanical hard stops. To include hard stops, use the
  Translational Hard Stop
  block.
- The flow resistance between the inlet and the interior of the converter is
  negligible.
- The kinetic energy of the fluid in the converter is negligible.
