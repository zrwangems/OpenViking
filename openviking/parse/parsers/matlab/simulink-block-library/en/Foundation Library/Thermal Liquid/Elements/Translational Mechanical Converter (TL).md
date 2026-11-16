---
type: simulink-block
title: 'Translational Mechanical Converter (TL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal Liquid / Elements'
documentation_page: 'translationalmechanicalconvertertl'
documentation_source_path: 'ref/translationalmechanicalconvertertl.html'
language: en
---

# Translational Mechanical Converter (TL)

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

### **A** — Converter inlet thermal liquid

Thermal liquid conserving port associated with the converter inlet.

### **H** — Temperature inside converter thermal

Thermal conserving port associated with the temperature of the liquid inside the
converter.

### **R** — Rod mechanical translational

Mechanical translational conserving port associated with the moving
interface.

### **C** — Case mechanical translational

Mechanical translational conserving port associated with the converter
casing.

## Parameters

### Main

### **Mechanical orientation** — Select the converter orientation `Pressure at A causes positive displacement of R relative to C` (default) | `Pressure at A causes negative displacement of R relative to C`

Select the alignment of moving interface with respect to the converter liquid
volume:

- `Pressure at A causes positive displacement of R relative to
  C` — Increase in the liquid volume results in a positive
  displacement of port **R** relative to port
  **C**.
- `Pressure at A causes negative displacement of R relative to
  C` — Increase in the liquid volume results in a negative
  displacement of port **R** relative to port
  **C**.

### **Interface displacement** — Select method to determine relative port positions `Calculate from velocity of port R relative to port C` (default) | `Provide input signal from Multibody joint`

Select method to determine displacement of port **R** relative to
port **C**:

- `Calculate from velocity of port R relative to port
  C` — Calculate displacement from relative port velocities,
  based on the mass balance equations. This is the default method.
- `Provide input signal from Multibody joint` —
  Enable the input physical signal port **p** to pass the
  displacement information from a Multibody joint. Use this method only when you
  connect the converter to a Multibody joint by using a Translational
  Multibody Interface block. For more information, see How to Pass Position Information.

### **Initial interface displacement** — Translational offset of port R relative to port C at the start of simulation `0 m` (default)

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

### **Interface cross-sectional area** — The area on which the liquid exerts pressure to generate the translational force `0.01 m^2` (default)

The area on which the liquid exerts pressure to generate the translational force.

### **Dead volume** — Volume of liquid when the interface displacement is 0 `1e-5 m^3` (default)

Volume of liquid when the interface displacement is 0.

### **Environment pressure specification** — Select a specification method for the environment pressure `Atmospheric pressure` (default) | `Specified pressure`

Select a specification method for the pressure outside the converter:

- `Atmospheric pressure` — Use the atmospheric
  pressure, specified by the Thermal Liquid Settings
  (TL) or Thermal Liquid Properties
  (TL) block connected to the circuit.
- `Specified pressure` — Specify a value by
  using the **Environment pressure** parameter.

### **Environment pressure** — Pressure outside the converter `0.101325 MPa` (default)

Pressure outside the converter acting against the pressure of the converter liquid
volume. A value of 0 indicates that the converter expands into vacuum.

#### Dependencies

Enabled when the **Environment pressure specification**
parameter is set to `Specified pressure`.

### Effects and Initial Conditions

### **Enable dynamic compressibility** — Select whether to model fluid dynamic compressibility `On` (default) | `Off`

Select whether to account for the dynamic compressibility of the liquid. Dynamic
compressibility gives the liquid density a dependence on pressure and temperature,
impacting the transient response of the system at small time scales.

### **Initial liquid pressure** — Liquid pressure at time zero `0.101325 MPa` (default)

Liquid pressure in the converter at the start of simulation.

#### Dependencies

To enable this parameter, select the **Enable dynamic
compressibility** check box.

### **Initial liquid temperature** — Liquid temperature at time zero `293.15 K` (default)

Liquid temperature in the converter at the start of simulation.

### **Nominal liquid pressure** — Liquid pressure at nominal operating conditions `0.101325 MPa` (default)

Thermal liquid pressure at nominal operating conditions. The block uses this value
to calculate the nominal density to use in the mass and energy conservation equation
when dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** check box.

### **Nominal liquid temperature** — Liquid temperature at nominal operating conditions `293.15 K` (default)

Thermal liquid temperature at nominal operating conditions. The block uses this
value to calculate the nominal density to use in the mass and energy conservation
equation when dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** check box.

## Libraries

Simscape / Foundation Library / Thermal Liquid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Interface between thermal liquid and mechanical translational networks

The Translational Mechanical Converter (TL) block models an
interface between a thermal liquid network and a mechanical rotational network. The block
converts thermal liquid pressure into mechanical force and vice versa. It can be used as a
building block for linear actuators.

The converter contains a variable volume of liquid. The temperature evolves based on the
thermal capacity of this volume. If the **Enable dynamic compressibility**
check box is selected, then the pressure also evolves based on the dynamic compressibility of
the liquid volume. The **Mechanical orientation** parameter lets you specify
whether an increase in pressure moves port **R** away from or towards port
**C**.

Port **A** is the thermal liquid conserving port associated with the
converter inlet. Port **H** is the thermal conserving port associated with
the temperature of the liquid inside the converter. Ports **R** and
**C** are the mechanical translational conserving ports associated with the
moving interface and converter casing, respectively.

### Mass Balance

The mass conservation equation in the mechanical converter volume is

m˙A=ε ρS v+{0,if fluid dynamic compressibility is offVρ(1βdpdt+αdTdt),if fluid dynamic compressibility is on

where:

- m˙A is the liquid mass flow rate into the converter through port A.
- *ε* is the mechanical orientation of the converter
  (`1` if increase in fluid pressure causes positive displacement of R
  relative to C, `-1` if increase in fluid pressure causes negative
  displacement of R relative to C).
- *ρ* is the liquid mass density.
- *S* is the cross-sectional area of the converter interface.
- *v* is the translational velocity of the converter
  interface.
- *V* is the liquid volume inside the converter.
- *β* is the liquid bulk modulus inside the converter.
- *α* is the coefficient of thermal expansion of the liquid.
- *p* is the liquid pressure inside the converter.
- *T* is the liquid temperature inside the converter.

If you connect the converter to a Multibody joint, use the physical signal input port
**p** to specify the displacement of port **R** relative
to port **C**. Otherwise, the block calculates the interface displacement
from relative port velocities, according to the block equations. The interface displacement
is zero when the liquid volume is equal to the dead volume. Then, depending on the
**Mechanical orientation** parameter value:

- If `Pressure at A causes positive displacement of R relative to
  C`, the interface displacement increases when the liquid volume increases
  from dead volume.
- If `Pressure at A causes negative displacement of R relative to
  C`, the interface displacement decreases when the liquid volume increases
  from dead volume.

### Momentum Balance

The momentum conservation equation in the mechanical converter volume is

F=−ε(p−pAtm)S

where:

- *F* is the force the liquid exerts on the converter
  interface.
- *p*Atm is the atmospheric pressure.

### Energy Balance

The energy conservation equation in the mechanical converter volume is

d(ρuV)dt=ϕA+QH−pSεv,

where:

- *u* is the liquid internal energy.
- *ϕ*A is the total energy flow rate into
  the mechanical converter volume through port A.
- *Q*H is the heat flow rate into the
  mechanical converter volume.

### Assumptions and Limitations

- Converter walls are not compliant. They cannot deform regardless of internal
  pressure and temperature.
- The converter contains no mechanical hard stops. To include hard stops, use the
  Translational Hard Stop
  block.
- The flow resistance between the inlet and the interior of the converter is
  negligible.
- The thermal resistance between the thermal port and the interior of the converter is
  negligible.
- The kinetic energy of the fluid in the converter is negligible.
