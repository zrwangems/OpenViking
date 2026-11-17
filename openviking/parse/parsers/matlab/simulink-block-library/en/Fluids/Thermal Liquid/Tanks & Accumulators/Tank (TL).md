---
type: simulink-block
title: 'Tank (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Tanks & Accumulators'
documentation_page: 'tanktl'
documentation_source_path: 'ref/tanktl.html'
language: en
---

# Tank (TL)

## Ports
```yaml
ports:
- name: A
  summary: Liquid port thermal liquid
  direction: conserving
- name: B
  summary: Liquid port thermal liquid
  direction: conserving
- name: C
  summary: Liquid port thermal liquid
  direction: conserving
- name: D
  summary: Liquid port thermal liquid
  direction: conserving
- name: E
  summary: Liquid port thermal liquid
  direction: conserving
- name: F
  summary: Liquid port thermal liquid
  direction: conserving
- name: H
  summary: Fluid temperature thermal liquid
  direction: conserving
- name: P
  summary: Tank pressure, MPa physical signal
  direction: input
- name: V
  summary: Liquid volume, m^3 physical signal
  direction: output
- name: L
  summary: Liquid level, m physical signal
  direction: output
- name: T
  summary: Fluid temperature, K physical signal
  direction: output
```

### Conserving

### **A** — Liquid port thermal liquid

Tank inlet.

### **B** — Liquid port thermal liquid

Optional tank inlet.

#### Dependencies

To enable this port, set **Number of inlets** to
`2`, `3`,
`4`, `5`, or
`6`.

### **C** — Liquid port thermal liquid

Optional tank inlet.

#### Dependencies

To enable this port, set **Number of inlets** to
`3`, `4`,
`5`, or
`6`.

### **D** — Liquid port thermal liquid

Optional tank inlet.

#### Dependencies

To enable this port, set **Number of inlets** to
`4`, `5`, or
`6`.

### **E** — Liquid port thermal liquid

Optional tank inlet.

#### Dependencies

To enable this port, set **Number of inlets** to
`5`, or
`6`.

### **F** — Liquid port thermal liquid

Optional tank inlet.

#### Dependencies

To enable this port, set **Number of inlets** to
`6`.

### **H** — Fluid temperature thermal liquid

Fluid temperature inside the tank.
### Input

### **P** — Tank pressure, `MPa` physical signal

Tank pressure, specified as a physical signal input, in MPa.

#### Dependencies

To enable this port, set **Pressurization
specification** to `Variable
pressure`.
### Output

### **V** — Liquid volume, `m^3` physical signal

Liquid volume inside the tank in `m^3`, specified as
a physical signal.

### **L** — Liquid level, `m` physical signal

Liquid level inside the tank in `m`, specified as a
physical signal.

### **T** — Fluid temperature, `K` physical signal

Tank fluid temperature in `K`, specified as a
physical signal.
## Parameters
```yaml
parameters:
- name: Number of inlets
  summary: Number of inlet ports 1 (default) | 2 | 3 | 4 | 5 | 6
  group: ''
- name: Pressurization specification
  summary: Tank pressure specification method Atmospheric pressure (default) | Specified pressure | Variable pressure
  group: ''
- name: Tank pressurization
  summary: User-defined tank pressure 0.101325 MPa (default) | positive scalar
  group: ''
- name: Tank volume parameterization
  summary: Tank area characteristics Constant cross-section area (default) | Tabulated data - volume vs. level
  group: ''
- name: Tank cross-sectional area
  summary: Tank cross-sectional area 1 m^2 (default) | positive scalar
  group: ''
- name: Liquid level vector
  summary: Vector of tank fluid levels [0, 3, 5] m (default) | 1-by-*n* vector
  group: ''
- name: Liquid volume vector
  summary: Vector of tank fluid levels [0, 4, 6] m^3 (default) | 1-by-*n* vector
  group: ''
- name: Inlet height
  summary: Height of inlet port 0.1 m (default) | positive scalar
  group: ''
- name: Inlet cross-sectional area
  summary: Cross-sectional area of the port inlet 0.01 m^2 (default) | positive scalar
  group: ''
- name: Height vector for inlets A and B
  summary: Vector of port heights for multiple enabled ports [.1, .1] m (default) | 1-by-*n* vector
  group: ''
- name: Cross-sectional area vector for inlets A and B
  summary: Vector of inlet areas for two enabled ports [.01, .01] m^2 (default) | 1-by-*n* vector
  group: ''
- name: Liquid level below inlet height
  summary: Whether to be notified of low tank levels Error (default) | Warning | None
  group: ''
- name: Liquid volume above max capacity
  summary: Whether to be notified of high tank volume None (default) | Warning | Error
  group: ''
- name: Maximum tank capacity
  summary: Fill limit of the tank 10 m^3 (default) | positive scalar
  group: ''
- name: Gravitational acceleration
  summary: Acceleration of gravity constant 9.81 m/s^2 (default) | positive scalar
  group: ''
```

### **Number of inlets** — Number of inlet ports `1` (default) | `2` | `3` | `4` | `5` | `6`

Number of inlet ports. Setting this parameter to
`2` or more exposes additional input
ports.

### **Pressurization specification** — Tank pressure specification method `Atmospheric pressure` (default) | `Specified pressure` | `Variable pressure`

Method to specify the tank pressure. To define a non-atmospheric constant
pressure, set this parameter to `Specified
pressure` and specify the value with the **Tank
pressurization** parameter. To specify a variable tank
pressure, set this parameter to `Variable pressure`
and supply the tank pressure as a physical signal at port
**P**.

### **Tank pressurization** — User-defined tank pressure `0.101325` MPa (default) | positive scalar

User-defined tank pressure.

#### Dependencies

To enable this parameter, set **Pressurization
specification** to `Specified
pressure`.

### **Tank volume parameterization** — Tank area characteristics `Constant cross-section area` (default) | `Tabulated data - volume vs. level`

Specifies tank area characteristics. This parameter is used to determine
the fluid level in the tank. If you would like to model a tank with a
variable cross-sectional area, you can provide data for tank volume and
fluid level with the `Tabulated data - volume vs.
level` option.

### **Tank cross-sectional area** — Tank cross-sectional area `1` m^2 (default) | positive scalar

Tank cross-sectional area.

#### Dependencies

To enable this parameter, set **Tank volume
parameterization** to `Constant cross-section
area`.

### **Liquid level vector** — Vector of tank fluid levels `[0, 3, 5]` m (default) | 1-by-*n* vector

Vector of tank fluid levels for the tabular parameterization of a
non-constant tank area. The values in this vector correspond one-to-one to
values in the **Volumetric flow rate vector** parameter.
Its elements are listed in ascending order. The elements must be positive
and the first element must be 0.

#### Dependencies

To enable this parameter, set **Tank volume
parameterization** to `Tabulated data - volume
vs. level`.

### **Liquid volume vector** — Vector of tank fluid levels `[0, 4, 6]` m^3 (default) | 1-by-*n* vector

Vector of tank fluid levels for the tabular parameterization of a
non-constant tank area. The values in this vector correspond one-to-one to
values in the **Volumetric flow rate vector** parameter.
Its elements are listed in ascending order. The elements must be positive
and the first element must be 0.

#### Dependencies

To enable this parameter, set **Tank volume
parameterization** to `Tabulated data - volume
vs. level`.

### **Inlet height** — Height of inlet port `0.1` m (default) | positive scalar

Height of inlet port. The value must be greater than or equal to 0.

#### Dependencies

To enable this parameter, set **Number of inlets** to
`1`.

### **Inlet cross-sectional area** — Cross-sectional area of the port inlet `0.01` m^2 (default) | positive scalar

Cross-sectional area of the port inlet. This value must be greater than
0.

### **Height vector for inlets A and B** — Vector of port heights for multiple enabled ports `[.1, .1]` m (default) | 1-by-*n* vector

Vector of port heights for multiple enabled ports. If you have two or more
ports enabled, the **Inlet height** parameter becomes a
vector of values that correspond to the height of each inlet port, starting
with port **A**. The parameter name and vector length
depend on the value of the **Number of inlets** parameter.
The default height for each inlet is `.1 m`. Each element
of this vector must be greater than or equal to 0.

#### Dependencies

To enable this parameter, set **Number of inlets** to
`2`, `3`,
`4`, `5`, or
`6`.

### **Cross-sectional area vector for inlets A and B** — Vector of inlet areas for two enabled ports `[.01, .01]` m^2 (default) | 1-by-*n* vector

Vector of cross-sectional areas for multiple enabled ports. If you have
two or more ports enabled, the **Inlet cross-sectional
area** parameter becomes a vector of values that correspond to
the cross-sectional area of each inlet, starting with port
**A**. The parameter name will include all enabled
ports. Each element of this vector must be greater than 0.

#### Dependencies

To enable this parameter, set **Number of inlets** to
`2`, `3`,
`4`, `5`, or
`6`.

### **Liquid level below inlet height** — Whether to be notified of low tank levels `Error` (default) | `Warning` | `None`

Whether to be notified if the tank fluid level falls below the port inlet
height during simulation. Set this parameter to
`Warning` if you would like to receive a
warning when this occurs during simulation. Set the parameter to
`Error` if you would like the simulation to
stop when this occurs.

### **Liquid volume above max capacity** — Whether to be notified of high tank volume `None` (default) | `Warning` | `Error`

Whether to be notified if the tank fluid volume rises above the tank
maximum capacity during simulation. Set this parameter to
`Warning` if you would like to receive a
warning when this occurs during simulation. Set the parameter to
`Error` if you would like the simulation to
stop when this occurs.

### **Maximum tank capacity** — Fill limit of the tank `10` m^3 (default) | positive scalar

Fill limit of the tank.

#### Dependencies

To enable this parameter, set **Liquid volume above max
capacity** to either:

- `Warning`
- `Error`

### **Gravitational acceleration** — Acceleration of gravity constant `9.81` m/s^2 (default) | positive scalar

Constant for the acceleration of gravity.
## Libraries

Simscape / Fluids / Thermal Liquid / Tanks & Accumulators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

### R2023b: Specify variable pressure

You can now specify variable tank pressurization for the Tank
(TL) block. When you set **Pressurization
specification** to `Variable pressure`, the
block uses the values from the physical signal at port **P** in the
dynamic pressure equation.

## Description

Thermal liquid container with variable fluid volume

The Tank (TL) block models a thermal liquid container
with a variable fluid volume. The absolute pressure of the tank fluid volume is assumed
constant and equal to the value specified in the block dialog box. In the special case
that the tank pressurization is equal to atmospheric pressure, the block represents a
vented tank.

The tank can exchange energy with its surroundings, allowing the internal temperature
and pressure to evolve over time. Connect port **H** to additional
thermal blocks to model heat transfer with the environment or conduction through the
tank walls.

**Tank Schematic**

The tank can have up to six input ports, **A** through
**F**. The pressure at the tank inlets is the sum of the constant
tank pressurization specified in the block dialog box and the hydrostatic pressure due
to the inlet height. The temperature at port **H** is the temperature
of the tank fluid volume.

### Tank Volume

The tank fluid volume is computed from the total fluid mass at each time step:

V=Mρ,

where:

- *V* is the tank fluid volume.
- *M* is the tank fluid mass.
- *ρ* is the tank fluid density.

### Mass Balance

The mass conservation equation in the tank fluid volume is

M˙=m˙A+m˙B+m˙C+m˙D+m˙E+m˙F,

where:

- M˙ is the change in fluid mass.
- m˙η denotes the mass flow rates into the tank fluid volume
  through port **η**.

### Momentum Balance

The momentum conservation equation in the tank fluid volume for port
**η** with η=A,B,C,D,E,F is

pη+pdyn=pRef+ρg(y−yη),

where:

- *pη* is the fluid pressure at
  inlet **η**.
- *pRef* is the constant tank
  pressurization.
- *pdyn* is the dynamic pressure:

  pdyn={0,m˙η≥0m˙η22ρηSIA2,m˙η<0

  When the flow direction is into tank, the incoming jet dissipates into
  the large fluid volume, loses momentum, and causes
  *pdyn* to be
  `0`. When the fluid flows out of the tank, the
  fluid in the volume accelerates into the port and causes
  *pdyn* to be greater
  than `0`.
- *ρη* is the liquid density at
  port **η**.
- *SIA* is the tank inlet
  area.
- *g* is the gravitational constant.
- *y* is the tank level, or height, relative to the
  tank bottom.
- *yη* is the tank inlet
  elevation relative to the tank bottom.

### Energy Balance

The energy conservation equation in the tank fluid volume is

M(Cp−hα)T˙=ϕA+ϕB+ϕC+ϕD+ϕE+ϕF−(m˙A+m˙B+m˙C+m˙D+m˙E+m˙F+MαT˙)h+Q,

where:

- *Cp* is the fluid thermal
  capacity.
- *α* is the fluid isobaric bulk modulus.
- *T* is the fluid temperature.
- *Φη* denotes the energy flow
  rates into the tank through port **η**.
- *h* is the fluid enthalpy.
- *Q* is the thermal energy flow rate into the tank
  through port **H**.
