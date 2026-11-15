---
type: simulink-block
title: 'Tank (G-TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid Library / Tanks and Accumulators'
documentation_page: 'tankgtl'
documentation_source_path: 'ref/tankgtl.html'
language: en
---

# Tank (G-TL)

## Ports

### Output

### **V** — Thermal liquid volume, `m^3` physical signal

Physical signal output port that reports the volume of thermal liquid
in the tank, in m3.

### **L** — Thermal liquid level, `m` physical signal

Physical signal output port that reports the height of the thermal
liquid volume relative to the bottom of the tank, in m.
### Conserving

### **A1** — Gas inlet gas

Gas conserving port associated with the opening through which gas
flows into or out of the tank.

### **B1** — Gas inlet gas

Gas conserving port associated with the opening through which gas
flows into or out of the tank.

### **A2** — Thermal liquid inlet thermal liquid

Thermal liquid conserving port associated with the opening through
which thermal liquid flows into or out of the tank.

### **B2** — Thermal liquid inlet thermal liquid

Thermal liquid conserving port associated with the opening through
which thermal liquid flows into or out of the tank.

#### Dependencies

To enable this port, set **Number of inlets** to
`2`, `3`,
`4`, `5`, or
`6`.

### **C2** — Thermal liquid inlet thermal liquid

Thermal liquid conserving port associated with the opening through
which thermal liquid flows into or out of the tank.

#### Dependencies

To enable this port, set **Number of inlets** to
`3`, `4`,
`5`, or
`6`.

### **D2** — Thermal liquid inlet thermal liquid

Thermal liquid conserving port associated with the opening through
which thermal liquid flows into or out of the tank.

#### Dependencies

To enable this port, set **Number of inlets** to
`4`, `5`, or
`6`.

### **E2** — Thermal liquid inlet thermal liquid

Thermal liquid conserving port associated with the opening through
which thermal liquid flows into or out of the tank.

#### Dependencies

To enable this port, set **Number of inlets** to
`5` or
`6`.

### **F2** — Thermal liquid inlet thermal liquid

Thermal liquid conserving port associated with the opening through
which thermal liquid flows into or out of the tank.

#### Dependencies

To enable this port, set **Number of inlets** to
`6`.

### **H1** — Gas temperature thermal

Thermal conserving port associated with the temperature inside the gas
volume.

### **H2** — Thermal liquid temperature thermal

Thermal conserving port associated with the temperature inside the
thermal liquid volume.

## Parameters

### **Number of inlets** — Number of thermal liquid ports `1` (default) | `2` | `3` | `4` | `5` | `6`

Number of thermal liquid ports for the block.

### **Total tank volume** — Combined gas and thermal liquid volume `10 m^3` (default) | positive scalar

Aggregate volume of the gas and thermal liquid portions of the
tank.

### **Tank volume parameterization** — Parameterization for thermal liquid volume `Constant cross-sectional area` (default) | `Tabulated data — volume vs. level`

Choice of parameterization for the thermal liquid volume. Select
`Constant cross-sectional area` to specify a
constant tank cross-sectional area. Select `Tabulated data
— volume vs. level` to compute the thermal liquid
volume by interpolation or extrapolation of tabulated data.

### **Tank cross-sectional area** — Area of constant tank cross-section `1` m^2 (default) | positive scalar

Area of the tank cross-section. The block assumes this value is constant
over the allowed range of fluid levels. The block uses this parameter to
compute the volume of thermal liquid inside the tank.

#### Dependencies

To enable this parameter, set **Tank volume
parameterization** to `Constant cross-sectional
area`.

### **Liquid level vector** — Thermal liquid levels at which to specify thermal liquid volume `[0, 3, 5]` m (default) | vector

Vector of thermal liquid levels at which to specify the thermal liquid
volume in the tank. The block uses this vector to construct a one-way lookup
table for the thermal liquid volume as a function of the thermal liquid
level.

#### Dependencies

To enable this parameter, set **Tank volume
parameterization** to `Tabulated data - volume
vs. level`.

### **Liquid volume vector** — Thermal liquid volume at specified thermal liquid levels `[0, 4, 6]` m^3 (default) | vector

Vector of thermal liquid volumes that correspond to the elements of the
**Liquid level vector** parameter. The block uses this
vector to construct a one-way lookup table for the thermal liquid volume as
a function of the thermal liquid level.

#### Dependencies

To enable this parameter, set **Tank volume
parameterization** to `Tabulated data - volume
vs. level`.

### **Cross-sectional area vector for inlets A1 and B1** — Flow areas of gas inlets `[.01, .01] m^2` (default) | vector

Two-element vector that specifies the flow areas of the gas inlets.

### **Inlet height at port A2** — Height of thermal liquid inlet `0.1 m` (default) | positive scalar

Height of the thermal liquid inlet.

#### Dependencies

To enable this parameter, set **Number of inlets** to
`1`.

### **Cross-sectional area at port A2** — Flow area of thermal liquid inlet `0.01 m^2` (default) | positive scalar

Flow area of the thermal liquid inlet.

#### Dependencies

To enable this parameter, set **Number of inlets** to
`1`.

### **Height vector for inlets A2 and B2** — Vector of port heights for ports `[.1, .1]` m (default) | 1-by-*n* vector

Vector of port heights for multiple enabled ports. The parameter name and
vector length depend on the value of the **Number of
inlets** parameter. Each element of the vector corresponds to
an inlet port, starting with port **A2**. The default
height for each inlet is `.1 m`. Each element of this
vector must be greater than or equal to 0.

For example, if **Number of inlets** is
`4`, the name of this parameter is
**Height vector for inlets A2, B2, C2, and D2** and the
default value is `0.1 * ones(1, 4)` m.

#### Dependencies

To enable this parameter, set **Number of inlets** to
`2`, `3`,
`4`, `5`, or
`6`.

### **Cross-sectional area vector for inlets A2 and B2** — Vector of inlet areas for ports `[.01, .01] m^2` (default) | 1-by-*n* vector

Vector of cross-sectional areas for multiple enabled ports. The parameter
name and vector length depend on the value of the **Number of
inlets** parameter. Each element of the vector corresponds to
an inlet port, starting with port **A2**. The default
height for each inlet is `.01 m`. Each element of this
vector must be greater than 0.

For example, if **Number of inlets** is
`4`, the name of this parameter is
**Cross-sectional area vector for inlets A2, B2, C2, and
D2** and the default value is `0.01 * ones(1,
4)` m2.

#### Dependencies

To enable this parameter, set **Number of inlets** to
`2`, `3`,
`4`, `5`, or
`6`.

### **Liquid volume above max capacity** — Whether to be notified of high tank volume `None` (default) | `Warning` | `Error`

Whether to be notified if the tank fluid volume rises above the value of
the **Total tank volume** parameter during simulation. Set
this parameter to `Warning` to receive a warning
when this occurs during simulation. Set the parameter to
`Error` for the simulation to stop when this
occurs.

### **Maximum tank liquid capacity** — Fill limit of tank `10 m^3` (default) | positive scalar

Fill limit of the tank.

#### Dependencies

To enable this parameter, set **Liquid volume above max
capacity** to either `Warning` or
`Error`.

### **Gravitational acceleration** — Gravitational acceleration constant `9.81` m/s^2 (default) | positive scalar

Value of the gravitational acceleration at the elevation of the tank. The
block assumes this value is constant over the height of the tank.

## Libraries

Simscape / Fluids / Thermal Liquid / Tanks & Accumulators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

### R2023b: Model up to six thermal liquid ports

Previously, the Tank (G-TL) block could only model
up to three thermal liquid ports. You can now use the **Number of
inlets** parameter to model up to six thermal liquid ports.

## Description

Pressurized tank with variable gas and thermal liquid volumes

The Tank (G-TL) block models the accumulation of mass and energy in a
chamber with separate gas and thermal liquid volumes. The total fluid volume is fixed,
but the individual gas and thermal liquid volumes can vary. Two gas ports allow for gas
flow and a variable number of thermal liquid ports, ranging from one to six, allow for
thermal liquid flow. The thermal liquid ports can be at different elevations.

Diagram depicting tank with thermal liquid to height y and containing ports A2, B2, and C2. The top of the tank contains gas and ports A1 and B1.

The tank is pressurized, but the pressurization is not fixed. It changes during
simulation with the pressure in the gas volume. The pressure rises when the pressure of
the gas volume rises and falls when the pressure of the gas volume falls. The thermal
liquid volume is assumed to be at equilibrium with the gas volume and its pressure is
therefore the same as that of the gas.

The fluid volumes can exchange energy with other fluid components and with the
environment but not with each other. The fluid volumes behave as if they were isolated
from each other by an insulated membrane. Energy exchanges with other components occur
through gas or thermal liquid ports, while exchanges with the environment occur,
strictly in the form of heat, through thermal ports.

Use this block to model components such as drain tanks, in which water condensed from
a compressed gas system is trapped at the bottom by gravity and expelled through a drain
outlet. Note, however, that neither gas nor thermal liquid domains capture the effects
of phase change—and therefore that this block cannot capture the effects of
condensation.

### Thermal Liquid Ports

You can specify the number of thermal liquid ports using the **Number of
inlets** parameter:

| Number of inlets | Exposed thermal liquid ports |
| --- | --- |
| `1` | Port **A2** |
| `2` | Ports **A2** and **B2** |
| `3` | Ports **A2**, **B2**, and **C2** |
| `4` | Ports **A2**, **B2**, **C2**, and **D2** |
| `5` | Ports **A2**, **B2**, **C2**, **D2**, and **E2** |
| `6` | Ports **A2**, **B2**, **C2**, **D2**, **E2**, and **F2** |

### Fluid Volumes

The total volume of the tank is equal to the sum of the gas and thermal liquid
volumes that it contains,

VT=VL+VG,

where *V* is the volume and
*T*, *L*, and *G* stand for
total, liquid, and gas. Because the total volume is fixed, the time rate of change
of the gas volume must be the reverse of that measured for the thermal liquid volume,

V˙G=−V˙L.

The time rate of change of the thermal liquid volume is
calculated by differentiating the expression

ML=ρLVL,

where *M* is mass and *ρ* is
density. The differentiation gives the mass flow rate into the thermal liquid volume,

M˙L=VLρ˙L+V˙LρL,

The time rate of change of the thermal liquid density is

ρ˙L=ρLβLp˙L−αLρLT˙L,

where:

- *β* is the thermal bulk modulus.
- *ɑ* is the isobaric thermal expansion
  coefficient.
- *p* is the fluid pressure.
- *T* is the fluid temperature.

Rearranging terms gives the rate of change of the thermal liquid
volume and, by extension, of the gas volume

V˙G=−V˙L≈VL(p˙LβL−αLT˙L)−M˙LρL.

### Mass Balance

The rate of mass accumulation in each fluid volume is equal to the net mass flow
rate into that fluid volume. In the thermal liquid volume

M˙L=∑i=A2,B2,...F2m˙i,

*M*L is the rate of mass
accumulation in the thermal liquid volume and m˙i are the individual mass flow rates into that volume through the
thermal liquid ports **A2**, **B2**,
**C2**, **D2**, **E2**, or
**F2**. The rate of mass accumulation contains contributions
from pressure, temperature, and volume change,

M˙L=VL(ρLβLp˙G−αLρLT˙L)+V˙LρL,

where the pressure of the thermal liquid volume is by definition
equal to the pressure of the gas volume and the equation is therefore written in
terms of the gas pressure. In the gas volume

M˙G=∑i=A1, B1m˙i,

where *MG* is the rate of
mass accumulation in the gas volume and m˙i are the individual mass flow rates into that volume through the
gas ports **A1** and **B1**. As with the thermal
liquid volume, the rate of mass accumulation contains contributions from pressure,
temperature, and volume change

M˙G=dMdp|Gp˙G+dMdT|GT˙G+V˙GρG,

where the pressure and temperature derivatives depend on the type
of gas specified in the Gas Properties (G) block.
The equations section of the Translational Mechanical Converter
(G) page defines the derivatives. Replacing
*VG* with the expression previously
obtained for this variable and combining the two expressions for
*MG*

dMdp|Gp˙G+dMdT|GT˙G+[VL(p˙GβL−αLT˙L)−M˙LρL]ρG=∑i=A1, B1m˙i.

Rearranging terms gives the final expression for the mass balance
in the gas volume

p˙G(dMdp|G+ρGVLβL)+(T˙GdMdT|G−T˙LρGVLαL)=∑i=A1, B1m˙i+ρGρL∑i=A2, B2,...F2m˙i,

where M˙L has been replaced with the summation of the mass flow rates into
the thermal liquid volume.

### Energy Balance

The rate of energy accumulation in each fluid volume is the sum of the energy flow
rates through the fluid inlets, the heat flow rate through the corresponding thermal
port, and the energy flow rate due to volume changes. For the gas volume

p˙G(dUdp|G+ρGhGVLβL)+(T˙GdUdT|G−T˙LρGhGVLαL)=QH1+∑i=A1, B1ϕi+ρGρLhG∑i=A2, B2,...F2m˙i,

where:

- *U* is the total energy of the fluid volume.
- *h* is the fluid enthalpy.
- *Q* is the heat flow rate through the thermal
  port.
- *ϕi* are the energy flow rates
  through the fluid inlets.

As before, the pressure and temperature derivatives depend on the
type of gas specified in the Gas Properties (G) block.
See the equations section of the Translational Mechanical Converter
(G) page for the definitions. For the thermal liquid volume

p˙LdUdp|L+T˙LdUdT|L=QH2+∑i=A2, B2,...F2ϕi+∑i=A2, B2,...F2m˙g(y(i)−y)−hL∑i=A2, B2,...F2m˙i,

where the pressure derivative is

dUdp|L=−TLαLVL,

and the temperature derivative is

dUdT|L=cp,LρLVL,

where *c*p is the
isobaric specific heat of the thermal liquid inside the tank.

### Momentum Balance

Flow resistance due to friction or other causes is ignored in both fluid volumes.
The block also ignores the effect of elevation on inlet pressure, but only on the
gas side. The gas inlet pressures are therefore equal to each other and to the
internal pressure of the gas volume

pA1=pB1=pG.

The thermal liquid inlet pressures are each a function of inlet depth. The
internal pressure of the thermal liquid volume is equal to the gas volume, *pL* =
*pG*. The block includes dynamic pressures,
*p*i*,dyn*, at
the inlets by using the equation

pi+pi,dyn=pG+ρL(y−yi)g,

where *y* is the elevation of the thermal liquid
surface, *y*i is the elevation of the
thermal liquid inlet, and *g* is the gravitational constant. The
term *y* -
*yi* gives the depth of the thermal liquid inlet with respect to the
gas-thermal liquid boundary. The dynamic pressure at each thermal liquid inlet
depends on the direction of flow at that inlet

pi,dyn={12ρivi2,if m˙i<00,if m˙i≥0

where *vi* is the flow
velocity.

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

- Fluid momentum is lost at the tank inlet due to the sudden expansion into
  the tank volume.
