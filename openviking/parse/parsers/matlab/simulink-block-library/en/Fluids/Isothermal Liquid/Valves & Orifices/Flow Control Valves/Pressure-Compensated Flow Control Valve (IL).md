---
type: simulink-block
title: 'Pressure-Compensated Flow Control Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Flow Control Valves'
documentation_page: 'pressurecompensatedflowcontrolvalveil'
documentation_source_path: 'ref/pressurecompensatedflowcontrolvalveil.html'
language: en
---

# Pressure-Compensated Flow Control Valve (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Liquid entry or exit point to the valve.

### **B** — Liquid port isothermal liquid

Liquid entry or exit point to the valve.
### Input

### **S** — Physical signal, in m physical signal

Orifice opening in m, returned as a physical signal. A positive signal
opens the orifice.

## Parameters

### **Orifice parameterization** — Method of modeling orifice opening `Linear - area vs. control member position` (default) | `Tabulated data - Area vs. control member position` | `Tabulated data - Volumetric flow rate vs. control member position and pressure drop`

Method of modeling the opening of the orifice. The opening is either
parametrized linearly, which correlates the opening area to the control
member position; by user-supplied data that correlate the orifice opening
area to the control member position; or by an array of data that correlates
the valve flow rate to the control member position and valve pressure
drop.

### **Control member travel between closed and open valve** — Maximum control member stroke `5e-3 m` (default) | positive scalar

Control member stroke that fully opens the orifice.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Linear - area vs.
control member travel`.

### **Maximum orifice area** — Maximum orifice cross-sectional area `8e-5 m^2` (default) | positive scalar

Cross-sectional area of the orifice in its fully open position. This
parameter is used as an upper limit for area-pressure calculations during
the simulation.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Linear - area vs.
control member travel`.

### **Control member position at closed valve** — Control member offset `0 m` (default) | positive scalar

Control member offset when the orifice is fully open. A positive, nonzero
value indicates a partially closed orifice. A negative, nonzero value
indicates an overlapped orifice that remains open for an initial
displacement set by the physical signal at port
**S**.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Linear - area vs.
control member travel`.

### **Control member position vector** — Vector of control member travel distances `[0, .002, .007]` (default) | 1-by-*n* vector

Vector of orifice opening distances for the tabular parameterization of
the orifice opening area. The vector elements must correspond one-to-one
with the elements in the **Orifice area vector** parameter.
The elements are listed in ascending order and the first element must be 0.
Linear interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Tabulated data - Area
vs. control member position`.

### **Orifice area vector** — Vector of opening areas `[1e-09, 4e-09, 1e-05] m^2` (default) | 1-by-*n* vector

Vector of valve opening areas for the tabular parameterization of the
valve opening area. The vector elements must correspond one-to-one with the
elements in the **Control member position vector**
parameter. The elements are listed in ascending order and must be greater
than 0.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Tabulated data - Area
vs. control member position`.

### **Control member position vector, s** — Vector of control member displacements `[0, .002, .004, .007, .017] m` (default) | 1-by-*n* vector

Vector of control member positions for the tabular parameterization of the
volumetric flow rate. The control member position vector forms an
independent axis with the **Pressure drop vector, dp**
parameter for the 3-D dependent **Volumetric flow rate table,
q(s,dp)** parameter. A positive displacement corresponds to
valve opening. The values are listed in ascending order and the first
element must be 0. Linear interpolation is employed between table data
points.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Volumetric flow rate vs.
control member position and pressure drop`.

### **Pressure drop vector, dp** — Vector of pressure differential values `[.3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of valve opening areas for the tabular parameterization of the
valve opening area. The pressure drop vector forms an independent axis with
the **Control member position vector, s** parameter for the
3-D dependent **Volumetric flow rate table, q(s,dp)**
parameter. The values are listed in ascending order and must be greater than
0. Linear interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Volumetric flow rate vs.
control member position and pressure drop`.

### **Volumetric flow rate table, q(s,dp)** — Array of volumetric flow rate values `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13] .* 1e-3 m^3/s` (default) | *M*-by-*N* array

Array of volumetric flow rates based on independent values of pressure
drop and spool travel distance. *M* and
*N* are the sizes of the corresponding vectors:

- *M* is the number of elements in the
  **Pressure drop vector, dp**
  parameter.
- *N* is the number of elements in the
  **Control member position vector, s**
  parameter.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Volumetric flow rate vs.
control member position and pressure drop`.

### **Set orifice pressure differential** — Threshold for compensator valve operation `0.6 MPa` (default) | scalar

Magnitude of pressure differential that triggers valve opening or
closing.

### **Pressure compensator valve regulation range** — Pressure operational region of the pressure compensating valve `0.1 MPa` (default) | scalar

Operational pressure range of the valve. The pressure regulation range
lies between the **Set orifice pressure differential** and
the maximum valve operating pressure.

### **Pressure compensator valve maximum area** — Area of the fully opened pressure compensator valve `1.5 * 8e-5 m^2` (default) | positive scalar

Cross-sectional area of the valve in its fully open position. This
parameter is used as an upper limit for area-pressure calculations during
the simulation.

### **Leakage area** — Gap area when in fully closed position `1e-10 m^2` (default) | positive scalar

Sum of all gaps when the valve is in the fully closed position. Any area
smaller than this value is maintained at the specified leakage area. This
contributes to numerical stability by maintaining continuity in the
flow.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor that accounts for discharge losses in theoretical
flows.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the valve.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change to the flow response
when the valve is in near-open or near-closed positions. Set this value to a
nonzero value less than one to increase the stability of your simulation in
these regimes.

## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Flow Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Flow control with pressure regulation in an isothermal liquid system

The Pressure-Compensated Flow Control Valve (IL) block provides constant-pressure flow
control through an Orifice (IL) block via a Pressure Compensator Valve (IL) connected in
series. When the control pressure over the orifice,
*p*A –
*p*B, meets or exceeds the **Set
orifice pressure differential**, the reducing valve in the pressure
compensator component begins to close, which maintains the pressure in the orifice. For
systems with venting or redirection of fluid to another part of the system, see the
Pressure-Compensated 3-Way Flow Control Valve (IL) block.

The valve opening and closing is controlled by a physical signal received at port
**S**. A positive signal opens the valve.

**Flow Control Valve Schematic**

### Numerically-Smoothed Area and Pressure

When the orifice parameterization is linear, you can maintain numerical robustness
at the extremes of the orifice area and valve pressure range by tuning the
**Smoothing factor** parameter to a nonzero value less than
1. If the **Smoothing factor** parameter is nonzero, the block
applies a smoothing function to all calculated areas and pressures, but it primarily
influences the simulation at the extremes of these ranges.

If you enable smoothing, the block smoothly saturates the orifice area between the
**Leakage area** and **Maximum orifice
area** parameters and applies a smoothing function. The block smoothly
saturates the valve pressure between the **Set orifice pressure
differential** parameter and the sum of the **Set orifice
pressure differential**  and the **Pressure compensator valve
regulation range** parameters.

For more information, see Numerical Smoothing.

### Orifice Parameterization

Setting **Orifice parameterization** to:

- `Linear - area vs. control member position`
  assumes that the spool position and the orifice opening area are related
  linearly.
- `Tabulated data - Area vs. control member
  position` interpolates user-provided data between the
  orifice opening area and the control member position with a potentially
  nonlinear relationship.
- `Tabulated data - Volumetric flow rate vs. control member
  position and pressure drop` interpolates the orifice
  volumetric flow rate directly from user-provided data between the
  control member position, orifice pressure drop, and orifice volumetric
  flow rate.
