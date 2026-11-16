---
type: simulink-block
title: 'Tank (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Tanks & Accumulators'
documentation_page: 'tankil'
documentation_source_path: 'ref/tankil.html'
language: en
---

# Tank (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Tank inlet.

### **B** — Liquid port isothermal liquid

Optional tank inlet.

#### Dependencies

To enable this port, set **Number of inlets** to
`2`, `3`,
`4`, `5`, or
`6`.

### **C** — Liquid port isothermal liquid

Optional tank inlet.

#### Dependencies

To enable this port, set **Number of inlets** to
`3`, `4`,
`5`, or
`6`.

### **D** — Liquid port isothermal liquid

Optional tank inlet.

#### Dependencies

To enable this port, set **Number of inlets** to
`4`, `5`, or
`6`.

### **E** — Liquid port isothermal liquid

Optional tank inlet.

#### Dependencies

To enable this port, set **Number of inlets** to
`5` or
`6`.

### **F** — Liquid port isothermal liquid

Optional tank inlet.

#### Dependencies

To enable this port, set **Number of inlets** to
`6`.
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

## Parameters

### **Number of inlets** — Number of inlet ports `1` (default) | positive integer between 1 and 6

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

### **Tank pressurization** — User-defined tank pressure `0.101325 MPa` (default) | positive scalar

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

### **Tank cross-sectional area** — Tank cross-sectional area `1 m^2` (default) | positive scalar

Tank cross-sectional area.

#### Dependencies

To enable this parameter, set **Tank volume
parameterization** to `Constant cross-section
area`.

### **Liquid level vector** — Vector of tank fluid levels `[0, 3, 5] m` (default) | 1-by-*n* vector

Vector of tank fluid levels for the tabular parameterization of a
non-constant tank area. The values in this vector correspond one-to-one to
values in the **Volumetric flow rate vector** parameter.
Its elements are listed in ascending order. The elements must be positive
and the first element must be 0.

#### Dependencies

To enable this parameter, set **Tank volume
parameterization** to `Tabulated data - volume
vs. level`.

### **Liquid volume vector** — Vector of tank fluid volumes `[0, 4, 6] m^3` (default) | 1-by-*n* vector

Vector of tank fluid volumes for the tabular parameterization of a
non-constant tank area. The values in this vector correspond one-to-one to
values in the **Liquid level vector** parameter. Its
elements are listed in ascending order. The elements must be positive and
the first element must be 0.

#### Dependencies

To enable this parameter, set **Tank volume
parameterization** to `Tabulated data - volume
vs. level`.

### **Inlet height** — Height of inlet port `0.1 m` (default) | positive scalar

Height of inlet port. The value must be greater than or equal to 0.

#### Dependencies

To enable this parameter, set **Number of inlets** to
`1`.

### **Inlet cross-sectional area** — Cross-sectional area of the port inlet `0.01 m^2` (default) | positive scalar

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

### **Cross-sectional area vector for inlets A and B** — Vector of inlet areas for two enabled ports `[.01, .01] m^2` (default) | 1-by-*n* vector

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

### **Liquid level below inlet height** — Whether to be notified of low tank levels `Error` (default) | `None` | `Warning`

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

### **Maximum tank capacity** — Fill limit of the tank `10 m^3` (default) | positive scalar

Fill limit of the tank.

#### Dependencies

To enable this parameter, set **Liquid volume above max
capacity** to either:

- `Warning`
- `Error`

### **Gravitational acceleration** — Acceleration of gravity constant `9.81 m/s^2` (default) | positive scalar

Constant for the acceleration of gravity.

## Libraries

Simscape / Fluids / Isothermal Liquid / Tanks & Accumulators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

### R2023b: Specify variable pressure

You can now specify variable tank pressurization for the Tank
(IL) block. When you set **Pressurization
specification** to `Variable pressure`, the
block uses the values from the physical signal at port **P** in the
dynamic pressure equation.

### R2023b: Tank (IL) block calculates dynamic pressure directly

The Tank (IL) block no longer uses the **Inlet
pressure loss coefficient** or **Pressure loss coefficient
vector** parameters to calculate pressure loss. The block now
calculates the dynamic pressure directly. If your model previously used values
greater than 1 for the **Inlet pressure loss coefficient** or
**Pressure loss coefficient vector** parameters, connect a
Local Resistance (IL) block to the tank inlet or
outlet to maintain the model behavior. Set the loss coefficient for the
Local Resistance (IL) block to the value of the
previous tank loss coefficient minus 1. If your model previously used values less
than 1 for the **Inlet pressure loss coefficient** or
**Pressure loss coefficient vector** parameters, the
Tank (IL) block cannot recreate this
behavior.

The block does not model inlet losses. Do not connect these blocks directly to a
Tank (IL) block:

- Tank (IL) blocks
- Constant Volume Chamber (IL) blocks
- Spring-Loaded Accumulator (IL) blocks
- Gas-Charged Accumulator (IL) blocks

There must always be flow resistance, which can be modeled by blocks such as pipes,
orifices, and local resistances, between two fluid volumes.

## Description

Tank in an isothermal liquid system

The Tank (IL) block models a container with up to six input ports,
**A** through **F**, within an isothermal liquid
system. The tank outputs fluid volume at port **V** and fluid level at
port **L** as physical signals. The block models the hydrostatic
pressure difference between the liquid surface and the inlet height level. The tank can
be pressurized to a constant, user-specified value or to atmospheric pressure.

### Fluid Volume

The volume of fluid in the tank is determined from the total mass flow into the
tank:

V=Mρ,

where:

- *M* is the total mass in the tank supplied by all
  ports.
- *ρ* is the fluid density.

Due to the constant pressure in the tank, the liquid volume inside
the tank changes based on mass flow rate. Note that the converse is true for pipes,
where pressure is a function of fixed fluid volumes.

If the tank fluid volume exceeds the specified capacity of the tank, you can
choose to be notified. Set the **Liquid volume above max capacity**
parameter to `Warning` if you would like to receive a
warning when this occurs during simulation. Set the parameter to
`Error` if you would like the simulation to stop when
this occurs.

### Fluid Level

If **Tank volume parameterization** is set to
`Constant cross-section area`, the fluid level in the
tank is determined from the fluid volume *V*, due to the constant
cross-sectional area of the tank. Otherwise, the fluid level can be specified as
tabulated data in the `Tabulated data - volume vs. level`
option.

When the level in the tank falls below the inlet height, the assumption that fluid
entirely fills the volume of the connecting blocks may not be valid. Connections to
a Pipe (IL) block, which is based on this assumption, may in this case return
unphysical results. If you expect to model tank fluid levels below tank inlet
height(s), connect the Tank (IL) block to your system with a Partially Filled Pipe
(IL) block instead.

Like the **Liquid volume above max capacity** parameter, you can
be notified if the tank fluid level falls below the height of the inlet port(s)
during your simulation by changing the **Liquid level below inlet
height** parameter setting.

### Mass Flow Rate

If you set **Number of inlets** to a number greater than
`1`, the equations below apply to each port. The dynamic
pressure for an inlet port, *i*, is

pi,dyn={12ρivi2,if m˙i<00,if m˙i≥0

where:

- *ρi* is the fluid
  density.
- *vi* is the flow
  velocity.
- m˙i is the mass flow rate into the tank fluid volume
  through the port.

The total pressure is

ptotal=P+pdyn+Δpelev,port,

where:

- *P* is the value of the **Tank
  pressurization** parameter if the **Pressurization
  specification** parameter is `Specified
  pressure`. Otherwise, *P* is the
  atmospheric pressure.
- *Δpelev,port* is the
  hydrostatic pressure difference at the specified port **Inlet
  height**: Δpelev,port=ρgL, where *L* is either the difference
  in height between the fluid level and the inlet height or zero,
  whichever is larger.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or
Property Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
