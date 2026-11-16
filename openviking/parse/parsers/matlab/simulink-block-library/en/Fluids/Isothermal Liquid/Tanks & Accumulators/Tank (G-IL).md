---
type: simulink-block
title: 'Tank (G-IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Tanks & Accumulators'
documentation_page: 'tankgil'
documentation_source_path: 'ref/tankgil.html'
language: en
---

# Tank (G-IL)

## Ports

### Output

### **V** — Isothermal liquid volume, `m^3` physical signal

Physical signal output port that reports the volume of isothermal
liquid in the tank, in m3.

### **L** — Isothermal liquid level, `m` physical signal

Physical signal output port that reports the height of the isothermal
liquid volume relative to the bottom of the tank, in m.
### Conserving

### **A1** — Gas inlet gas

Gas conserving port associated with the opening through which gas
flows into or out of the tank.

### **B1** — Gas inlet gas

Gas conserving port associated with the opening through which gas
flows into or out of the tank.

### **A2** — Isothermal liquid inlet isothermal liquid

Isothermal liquid conserving port associated with the opening through
which isothermal liquid flows into or out of the tank.

### **B2** — Isothermal liquid inlet isothermal liquid

Isothermal liquid conserving port associated with the opening through
which isothermal liquid flows into or out of the tank.

#### Dependencies

To enable this port, set **Number of inlets** to
`2`, `3`,
`4`, `5`, or
`6`.

### **C2** — Isothermal liquid inlet isothermal liquid

Isothermal liquid conserving port associated with the opening through
which isothermal liquid flows into or out of the tank.

#### Dependencies

To enable this port, set **Number of inlets** to
`3`, `4`,
`5`, or
`6`.

### **D2** — Isothermal liquid inlet isothermal liquid

Isothermal liquid conserving port associated with the opening through
which isothermal liquid flows into or out of the tank.

#### Dependencies

To enable this port, set **Number of inlets** to
`4`, `5`, or
`6`.

### **E2** — Isothermal liquid inlet isothermal liquid

Isothermal liquid conserving port associated with the opening through
which isothermal liquid flows into or out of the tank.

#### Dependencies

To enable this port, set **Number of inlets** to
`5` or
`6`.

### **F2** — Isothermal liquid inlet isothermal liquid

Isothermal liquid conserving port associated with the opening through
which isothermal liquid flows into or out of the tank.

#### Dependencies

To enable this port, set **Number of inlets** to
`6`.

### **H1** — Heat transfer thermal

Thermal conserving port associated with heat transfer at the tank wall
for the gas volume.

## Parameters

### **Number of inlets** — Number of isothermal liquid ports `1` (default) | `2` | `3` | `4` | `5` | `6`

Number of isothermal liquid ports for the block.

### **Total tank volume** — Combined gas and isothermal liquid volume `10 m^3` (default) | positive scalar

Aggregate volume of the gas and isothermal liquid portions of the
tank.

### **Tank volume parameterization** — Parameterization for isothermal liquid volume `Constant cross-sectional area` (default) | `Tabulated data — volume vs. level`

Choice of parameterization for the isothermal liquid volume. Select
`Constant cross-sectional area` to specify a
constant tank cross-sectional area. Select `Tabulated data
— volume vs. level` to compute the isothermal liquid
volume by interpolation or extrapolation of tabulated data.

### **Tank cross-sectional area** — Area of constant tank cross-section `1` m^2 (default) | positive scalar

Area of the tank cross-section. The block assumes this value is constant
over the allowed range of fluid levels. The block uses this parameter to
compute the volume of isothermal liquid inside the tank.

#### Dependencies

To enable this parameter, set **Tank volume
parameterization** to `Constant cross-sectional
area`.

### **Liquid level vector** — Isothermal liquid levels at which to specify isothermal liquid volume `[0, 3, 5]` m (default) | vector

Vector of isothermal liquid levels at which to specify the isothermal
liquid volume in the tank. The block uses this vector to construct a one-way
lookup table for the isothermal liquid volume as a function of the
isothermal liquid level.

#### Dependencies

To enable this parameter, set **Tank volume
parameterization** to `Tabulated data - volume
vs. level`.

### **Liquid volume vector** — Isothermal liquid volume at specified isothermal liquid levels `[0, 4, 6]` m^3 (default) | vector

Vector of isothermal liquid volumes that correspond to the elements of the
**Liquid level vector** parameter. The block uses this
vector to construct a one-way lookup table for the isothermal liquid volume
as a function of the isothermal liquid level.

#### Dependencies

To enable this parameter, set **Tank volume
parameterization** to `Tabulated data - volume
vs. level`.

### **Cross-sectional area vector for inlets A1 and B1** — Flow areas of gas inlets `[.01, .01] m^2` (default) | vector

Two-element vector that specifies the flow areas of the gas inlets.

### **Inlet height at port A2** — Height of isothermal liquid inlet `0.1 m` (default) | positive scalar

Height of the isothermal liquid inlet.

#### Dependencies

To enable this parameter, set **Number of inlets** to
`1`.

### **Cross-sectional area at port A2** — Flow area of isothermal liquid inlet `0.01 m^2` (default) | positive scalar

Flow area of the isothermal liquid inlet.

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

Simscape / Fluids / Isothermal Liquid / Tanks & Accumulators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Pressurized tank with variable gas and isothermal liquid volumes

The Tank (G-IL) block models the accumulation of mass and energy in a
chamber with separate gas and isothermal liquid volumes. The total fluid volume is
fixed, but the individual gas and isothermal liquid volumes can to vary. Two gas ports
allow for gas flow and a variable number of isothermal liquid ports, ranging from one to
six, allow for isothermal liquid flow. The isothermal liquid ports can be at different
elevations.

Diagram depicting tank with isothermal liquid to height y and containing ports A2, B2, and C2. The top of the tank contains gas and ports A1 and B1.

The tank is pressurized, but the pressurization is not fixed. It changes during
simulation corresponding to the pressure in the gas volume. The pressure rises when the
pressure of the gas volume rises and falls when the pressure of the gas volume falls.
The block assumes that the isothermal liquid volume is at equilibrium with the gas
volume and its pressure is the same as that of the gas. The two fluid volumes go not
exchange energy with each other, but energy exchanges with other components can occur
through the gas ports.

### Isothermal Liquid Ports

You can specify the number of isothermal liquid ports using the **Number
of inlets** parameter:

| Number of inlets | Exposed isothermal liquid ports |
| --- | --- |
| `1` | Port **A2** |
| `2` | Ports **A2** and **B2** |
| `3` | Ports **A2**, **B2**, and **C2** |
| `4` | Ports **A2**, **B2**, **C2**, and **D2** |
| `5` | Ports **A2**, **B2**, **C2**, **D2**, and **E2** |
| `6` | Ports **A2**, **B2**, **C2**, **D2**, **E2**, and **F2** |

### Fluid Volumes

The total volume of the tank is the sum of the gas and isothermal liquid volumes
that it contains,

VT=VL+VG,

where *V* is the volume and
*T*, *L*, and *G* stand for
total, liquid, and gas. Because the total volume is fixed, the time rate of change
of the gas volume must be the reverse of the time rate of change for the isothermal
liquid volume,

V˙G=−V˙L.

The block calculates the time rate of change of the isothermal
liquid volume by differentiating the expression

ML=ρLVL,

where *M* is mass and *ρ* is
density. The differentiation gives the mass flow rate into the isothermal liquid volume,

M˙L=VLρ˙L+V˙LρL.

The rate of change of the isothermal liquid volume and, by extension, of the gas
volume is

V˙G=−V˙L≈VLp˙LρLdρLdp|−M˙LρL,

where *p* is the pressure.

### Mass Balance

The rate of mass accumulation in each fluid volume is equal to the net mass flow
rate into that fluid volume. In the isothermal liquid volume

M˙L=∑i=A2,B2,...F2m˙i,

where *ML* is the rate of
mass accumulation in the isothermal liquid volume and m˙i are the individual mass flow rates into that volume through the
isothermal liquid ports **A2**, **B2**,
**C2**, **D2**, **E2**, or
**F2**.

In the gas volume

M˙G=∑i=A1, B1m˙i,

*MG* is the rate of mass accumulation in the
gas volume and m˙i are the individual mass flow rates into that volume through the
gas ports **A1** and **B1**. The rate of mass
accumulation for the gas volume contains contributions from pressure, temperature,
and volume change,

M˙G=dMdp|Gp˙G+dMdT|GT˙G+V˙GρG,

where *T* is the temperature and the pressure
and temperature derivatives depend on the type of gas specified in the
Gas Properties (G) block.
The equations section of the Translational Mechanical Converter
(G) page defines the derivatives. The mass balance equation for
the gas volume is

p˙GdMdp|G+T˙GdMdT|G+p˙GρGρLVLdρLdp|=∑i=A1, B1m˙i+ρGρL∑i=A2, B2,...F2m˙i,

### Energy Balance

The rate of energy accumulation in the gas volume is

p˙GdUdp|G+T˙GdUdT|G+p˙GρGρLhGVLdρLdp|=QH1+∑i=A1, B1ϕi+ρGρLhG∑i=A2, B2,...F2m˙i

where:

- *U* is the total energy of the fluid volume.
- *h* is the fluid enthalpy.
- *Q* is the heat flow rate through the thermal
  port.
- *ϕi* are the energy flow rates
  through the fluid inlets.

The pressure and temperature derivatives depend on the type of gas
specified in the Gas Properties (G) block.
See the equations section of the Translational Mechanical Converter
(G) page for the definitions.

### Momentum Balance

The block ignores flow resistance due to friction or other causes in both fluid
volumes. The block also ignores the effect of elevation on inlet pressure, but only
on the gas side. The gas inlet pressures are equal to each other and to the internal
pressure of the gas volume:

pA1=pB1=pG.

The isothermal liquid inlet pressures are each a function of inlet depth. The
internal pressure of the isothermal liquid volume is equal to the gas volume, *pL* =
*pG*. The block includes dynamic pressures,
*p*i*,dyn*, at
the inlets by using the equation

pi+pi,dyn=pG+ρL(y−yi)g,

where *y* is the elevation of the isothermal
liquid surface, *y*i is the elevation of the
isothermal liquid inlet, and *g* is the gravitational constant. The
term *y* -
*yi* gives the depth of the isothermal liquid inlet with respect to the
gas-isothermal liquid boundary. The dynamic pressure at each isothermal liquid inlet
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
