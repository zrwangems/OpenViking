---
type: simulink-block
title: 'Pressure-Compensated 3-Way Flow Control Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Valves and Orifices / Flow Control Valves'
documentation_page: 'pressurecompensated3wayflowcontrolvalveil'
documentation_source_path: 'ref/pressurecompensated3wayflowcontrolvalveil.html'
language: en
---

# Pressure-Compensated 3-Way Flow Control Valve (IL)

## Ports

### Conserving

### **A** — Valve liquid port isothermal liquid

Liquid entry or exit port to the three-way valve.

### **B** — Orifice liquid port isothermal liquid

Liquid entry or exit port to the orifice.

### **R** — Reducing valve liquid port isothermal liquid

Liquid exit port from the reducing valve.
### Input

### **S** — Physical signal, in m physical signal

Orifice opening in m, set as a physical signal.

## Parameters

### **Orifice parameterization** — Method of modeling orifice opening `Linear - area vs. control member position` (default) | `Tabulated data - Area vs. control member position` | `Tabulated data - Volumetric flow rate vs. control member position and pressure drop`

Method of modeling the opening of the orifice. The opening is either
parametrized linearly, which correlates the opening area to the control
member position; by user-supplied data that correlate the orifice opening
area to the control member position; or by an array of data that correlates
the valve flow rate to the control member position and valve pressure
drop.

### **Control member position at closed orifice** — Control member offset `0 m` (default) | scalar

Control member offset when the orifice is fully open. A positive, nonzero
value indicates a partially closed orifice. A negative, nonzero value
indicates an overlapped orifice that remains open for an initial
displacement set by the physical signal at port
**S**.

### **Control member travel between closed and opened orifice** — Maximum control member stroke `5e-3 m` (default) | positive scalar

Control member stroke that fully opens the orifice.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Linear - area vs.
control member position`.

### **Maximum orifice area** — Maximum orifice cross-sectional area `8e-5 m^2` (default) | positive scalar

Cross-sectional area of the orifice in its fully open position. This
parameter is used as an upper limit for area-pressure calculations during
the simulation.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Linear - area vs.
control member position`.

### **Control member position vector** — Vector of opening position `[0, .002, .007] m` (default) | 1-by-*n* vector

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

### **Control member position vector, s** — Vector of control member positions `[0, .002, .004, .007, .017] m` (default) | 1-by-*n* vector

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

### **Set orifice pressure differential** — Threshold for compensator valve operation `0.6 MPa` (default) | positive scalar

Magnitude of pressure differential that triggers valve opening or
closing.

### **Pressure compensator valve regulation range** — Area of the fully opened pressure compensator valve `1e-4 m^2` (default) | positive scalar

Cross-sectional area of the valve in its fully open position. This
parameter is used as an upper limit for area-pressure calculations during
the simulation.

### **Pressure compensator valve maximum area** — Pressure operational region of the pressure compensating valve `0.1 MPa` (default) | scalar

Operational pressure range of the valve. The pressure regulation range
lies between the **Set orifice pressure differential** and
the maximum valve operating pressure.

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

3-way flow control in an isothermal liquid system

The Pressure-Compensated 3-Way Flow Control Valve (IL) block
models constant-pressure flow control. When the control pressure,
*p*A –
*p*B, meets or exceeds the **Set
orifice pressure differential**, the relief component of the underlying
compensator valve opens to maintain the pressure in the block.

The flow control valve opening and closing is controlled by a physical signal received at
port **S**, which determines the area of the underlying orifice block.
A positive signal opens the valve. Port **R** vents liquid to another
part of your network.

For pressure-compensated flow control without venting, see the Pressure-Compensated Flow Control Valve (IL) block.

### Orifice Parameterization

You can choose the valve model with the **Orifice parameterization** setting:

- `Linear - area vs. control member position`
  is an analytical formulation that assumes the valve opening area and the
  valve control member are related linearly.
- `Tabulated data - Area vs. control member
  position` is a user-supplied data sheet that relates
  orifice opening area and the control member position. The block queries
  between data points with linear interpolation and uses nearest
  extrapolation for points beyond the table boundaries.
- `Tabulated data - Volumetric flow rate vs. control member
  position and pressure drop` is a user-supplied data
  sheet that relates the control member position, orifice pressure drop,
  and orifice volumetric flow rate. The block queries between data points
  with linear interpolation and uses a nearest extrapolation for points
  beyond the table boundaries.

### Numerically-Smoothed Area and Pressure

When the orifice parameterization is linear, you can maintain numerical robustness at the
extremes of the orifice area and valve pressure range by tuning the
**Smoothing factor** parameter to a nonzero value less than
1. If the **Smoothing factor** parameter is nonzero, the block
applies a smoothing function to all calculated areas and pressures, but it primarily
influences the simulation at the extremes of these ranges.

If you enable smoothing, the block smoothly saturates the orifice area between the
**Leakage area** and **Maximum orifice
area** parameters. The block smoothly saturates the valve pressure
between the **Set orifice pressure differential** parameter and
the sum of the **Set orifice pressure differential**  and the
**Pressure compensator valve regulation range**
parameters.

For more information, see Numerical Smoothing.

### Block Schematic

The Pressure-Compensated 3-Way Flow Control Valve (IL) is constructed from the
Pressure Compensator Valve (IL) and Orifice (IL) blocks.

**Three-Way Flow Control Valve Schematic**
