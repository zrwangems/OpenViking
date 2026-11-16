---
type: simulink-block
title: 'Cartridge Valve Insert (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Flow Control Valves'
documentation_page: 'cartridgevalveinsertil'
documentation_source_path: 'ref/cartridgevalveinsertil.html'
language: en
---

# Cartridge Valve Insert (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Liquid entry or exit port.

### **B** — Liquid port isothermal liquid

Liquid entry or exit port.

### **X** — Pressure port isothermal liquid

Pilot pressure port. There is no mass flow rate through port
**X**.

## Parameters

### **Valve seat specification** — Geometry of valve seat `Conical` (default) | `Custom`

Geometry of valve seat. This parameter is used for calculating the open
area between the poppet and seat.

### **Poppet diameter** — Diameter of the valve control member `0.01 m` (default) | positive scalar

Diameter of the valve control member.

#### Dependencies

To enable this parameter, set **Valve seat
specification** to
`Conical`.

### **Seat cone angle** — Angle of the seat opening `120 deg` (default) | positive scalar

Angle of the seat opening.

#### Dependencies

To enable this parameter, set **Valve seat
specification** to
`Conical`.

### **Orifice parameterization** — Method of calculating orifice area `Linear - area vs. control member position` (default) | `Tabulated data - Area vs. control member position` | `Tabulated data - Volumetric flow rate vs. control member position and pressure drop`

The valve opening is calculated in one of three ways, linearly or by
tabulated data:

- `Linear - area vs. control member
  position`: The orifice area is determined by a
  linear relationship to the poppet opening or closing
  distance.
- `Tabulated data - Area vs. control member
  position`: The opening area is interpolated
  from the **Poppet position vector** and the
  **Orifice area vector** based on the
  current poppet position.
- `Tabulated data - Volumetric flow rate vs. control
  member position and pressure drop`. The
  volumetric flow rate is directly interpolated from the provided
  **Poppet position vector, s**;
  **Pressure drop vector, dp**; and
  **Volumetric flow rate table, q(s,dp)**
  parameters, based on the current poppet position.

#### Dependencies

To enable this parameter, set **Valve seat
specification** to
`Custom`.

### **Poppet stroke** — Maximum poppet extension `5e-3 m` (default) | positive scalar

Maximum poppet extension.

#### Dependencies

To enable this parameter, set **Valve seat
specification** to `Custom` and
**Orifice parameterization** to `Linear
- area vs. control member position`.

### **Maximum orifice area** — Maximum orifice cross-sectional area `1e-4 m^2` (default) | positive scalar

Cross-sectional area of the orifice in its fully open position. This
parameter is used as an upper limit for area-pressure calculations during
the simulation.

#### Dependencies

To enable this parameter, set **Valve seat
specification** to `Custom` and
**Orifice parameterization** to `Linear
- area vs. control member position`.

### **Poppet position vector** — Vector of opening positions `[0, .002, .004, .007, .017] m` (default) | 1-by-*n* vector

Vector of orifice opening positions for the tabular parameterization of
the orifice opening area. The vector elements must correspond one-to-one
with the elements in the **Orifice area vector** parameter.
The elements are listed in ascending order and must be greater than
0.

#### Dependencies

To enable this parameter, set **Valve seat
specification** to `Custom` and
**Orifice parameterization** to
`Tabulated data - Area vs. control member
position`.

### **Orifice area vector** — Vector of opening areas `[1e-09, 2.0352e-07, 4.0736e-05, .00011438, .00034356] m^2` (default) | 1-by-*n* vector

Vector of valve opening areas for the tabular parameterization of the
valve opening area. The vector elements must correspond one-to-one with the
elements in the **Poppet position vector** parameter. The
elements are listed in ascending order and must be greater than 0.

#### Dependencies

To enable this parameter, set **Valve seat
specification** to `Custom` and
**Orifice parameterization** to
`Tabulated data - Area vs. control member
position`.

### **Poppet position vector, s** — Vector of control member positions `[0, .002, .004, .007, .017] m` (default) | 1-by-*n* vector

Vector of control member positions for the tabular parameterization of the
volumetric flow rate. The spool travel vector forms an independent axis with
the **Pressure drop vector, dp** parameter for the 3-D
dependent **Volumetric flow rate table, q(s,dp)**
parameter. A positive displacement corresponds to valve opening. The values
are listed in ascending order and the first element must be 0. Linear
interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set **Valve seat
specification** to `Custom` and
**Orifice parameterization** to
`Volumetric flow rate vs. control member position and
pressure drop`.

### **Pressure drop vector, dp** — Vector of pressure differential values `[.3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure drop values for tabular parameterization of volumetric flow rate. The
pressure drop vector forms an independent axis with the **Poppet
position vector, s** parameter for the 3-D dependent
**Volumetric flow rate table, q(s,dp)** parameter. The
values are listed in ascending order and must be greater than 0. Linear
interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set **Valve seat
specification** to `Custom` and
**Orifice parameterization** to
`Volumetric flow rate vs. control member position and
pressure drop`.

### **Volumetric flow rate table, q(s,dp)** — Array of volumetric flow rate values `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13] .* 1e-3 m^3/s` (default) | *M*-by-*N* array

Matrix of volumetric flow rates based on independent values of pressure
drop and spool travel distance. *M* and
*N* are the sizes of the corresponding vectors:

- *M* is the number of elements in the
  **Poppet position vector, s**
  parameter.
- *N* is the number of elements in the
  **Pressure drop vector, dp**
  parameter.

#### Dependencies

To enable this parameter, set **Valve seat
specification** to `Custom` and
**Orifice parameterization** to
`Volumetric flow rate vs. control member position and
pressure drop`.

### **Port A poppet area** — Cross-sectional area of port A `1e-4 m^2` (default) | positive scalar

Cross-sectional area of port **A**.

### **Port A poppet to port X pilot area ratio** — Ratio of inlet to pilot port area `0.5` (default) | positive scalar

Ratio of the inlet port, **A**, to the pilot pressure
port, **X**. This value is used to calculate the force at
port **X**. The ratio must be less than or equal to
1.

### **Spring preload force** — Spring force in neutral poppet position `25 N` (default) | positive scalar

Spring force on the poppet when the poppet is in the neutral position.
This parameter is a threshold value which, when added to the pilot pressure
at port **X**, counterbalances the valve opening due to the
pressures at ports **A** and **B**.

### **Spring stiffness** — Stiffness constant `15e3 N/m` (default) | positive scalar

Spring stiffness constant.

### **Leakage area** — Gap area when in fully closed position `1e-10 m^2` (default) | positive scalar

Sum of all gaps when the valve is in the fully closed position. Any area
smaller than this value is saturated to the specified leakage area. This
contributes to numerical stability by maintaining continuity in the
flow.

#### Dependencies

To enable this parameter, set either:

- **Valve seat specification** to
  `Conical`.
- **Valve seat specification** to
  `Custom` and **Orifice
  parameterization** to `Linear -
  Area vs. control member position`.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor that accounts for discharge losses in theoretical
flows.

#### Dependencies

To enable this parameter, set either:

- **Valve seat specification** to
  `Conical`.
- **Valve seat specification** to
  `Custom` and **Orifice
  parameterization** to `Linear -
  Area vs. control member position` or
  `Tabulated data - Area vs. control member
  position`.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the valve.

#### Dependencies

To enable this parameter, set either:

- **Valve seat specification** to
  `Conical`.
- **Valve seat specification** to
  `Custom` and **Orifice
  parameterization** to `Linear -
  Area vs. control member position` or
  `Tabulated data - Area vs. control member
  position`.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change to the flow response
when the valve is in near-open or near-closed positions. Set this value to a
nonzero value less than one to increase the stability of your simulation in
these regimes.

#### Dependencies

To enable this parameter, set either:

- **Valve seat specification** to `Conical`.
- **Valve seat specification** to `Custom` and **Orifice parameterization** to `Linear - Area vs. control member position`.

### **Valve opening time constant** — Valve time constant `0.1 s` (default) | positive scalar

Constant that captures the time required for the fluid to reach
steady-state conditions when opening or closing the valve from one position
to another. This parameter impacts the modeled opening dynamics.

## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Flow Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Cartridge flow-control valve in an isothermal liquid network

The Cartridge Valve Insert (IL) block models a cartridge
flow-control valve in an isothermal liquid network. The valve seat can be specified as
conical or as a custom opening parameterized by analytical or tabular formulations. The
valve opens when the combined pressures at ports **A** and
**B** exceed the **Spring preload force** and
pressure at port **X**.

You can specify the block seat geometry as either conical or a custom. This seat setting
determines the sub-components that make up the block. In both configurations, the
**Port A poppet to port X pilot area ratio** parameter sets the
force ratio in the underlying Cartridge Valve Actuator
block.

Use the Cartridge Valve Insert (IL) block when you would like
flow control set by a pilot pressure line. Use the Pressure-Compensated 3-Way Flow Control Valve (IL) or Pressure-Compensated Flow Control Valve (IL) block for flow
control due to a pressure differential or the Poppet Valve (IL) block for valve
opening controlled by an external physical signal.

### Conical Valve Seat

The conical cartridge valve insert is a composite of two Isothermal Liquid library blocks:

- Poppet Valve (IL)
- Cartridge Valve Actuator (IL)

**Conical Cartridge Valve Insert Schematic**

### Custom Valve Seat

The custom cartridge valve insert is a composite of two Isothermal Liquid library blocks:

- Orifice (IL)
- Cartridge Valve Actuator (IL)

**Custom Cartridge Valve Insert Schematic**

In the custom configuration, you can parameterize the valve
opening analytically or with a data set.

**Analytical Parameterization**

By setting **Orifice parameterization** to
`Linear - area vs. control member position`, the
valve opening area is linearly proportional to the poppet position. Once the
pressure at port **A** or **B** exceeds the
**Spring preload force**, the valve opens until the
**Maximum orifice area** is reached. When the valve is
fully closed, a small **Leakage area** remains open to flow so
that numerical continuity is maintained in the network.

**Tabulated Parameterization**

By setting **Orifice parameterization** to `Tabulated data -
Area vs. control member position`, you can supply the opening
profile based on opening area and poppet position. The block queries between
data points with linear interpolation and uses nearest extrapolation for points
beyond the table boundaries.

By setting **Orifice parameterization** to `Tabulated data -
Volumetric flow rate vs. control member position and pressure
drop`, you can supply the volumetric flow rate through the
valve as a parameterized table of poppet position and valve pressure drop. The
block queries between data points with linear interpolation and uses linear
extrapolation for points beyond the table boundaries. The volumetric flow rate
is converted to a mass flow rate by multiplying by the fluid density.

### Opening Dynamics

If opening dynamics are modeled, a lag is introduced to the flow response to the
modeled control pressure. *p*control becomes
the dynamic control pressure, *p*dyn;
otherwise, *p*control is the steady-state
pressure. The instantaneous change in dynamic control pressure is calculated based
on the **Opening time constant**, *τ*:

p˙dyn=pcontrol−pdynτ.

By default, **Opening dynamics** is set to
`Off`.

### Numerically-Smoothed Force and Opening

When the actuator is close to full extension or full retraction, and
**Orifice parameterization** is set to `Linear -
area vs. control member position`, you can maintain numerical
robustness in your simulation by adjusting the block **Smoothing
factor**. A smoothing function is applied to the actuator force and
orifice opening or area, but primarily influences the simulation at the extremes of
these ranges.

The normalized force that opens the valve is

F^=FA+FB−FPreload−FPilotkxstroke.

where:

- *FA* is the force at port
  **A**.
- *FB* is the force at port
  **B**.
- *FPreload* is the
  **Spring preload force**.
- *FPilot* is the force at port
  **X**.

When **Valve seat specification** is set to
`Conical`, the block smoothly saturates the orifice
opening distance between `0` and the maximum orifice opening
distance. When **Valve seat specification** is set to
`Custom`, the block smoothly saturates the valve
opening area between the **Leakage area** parameter and the
**Maximum orifice area** parameter.

For more information, see Numerical Smoothing.
