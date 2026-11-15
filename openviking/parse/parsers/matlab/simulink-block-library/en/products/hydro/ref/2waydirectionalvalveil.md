---
type: simulink-block
title: '2-Way Directional Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Valves and Orifices / Directional Control Valves'
documentation_page: '2waydirectionalvalveil'
documentation_source_path: 'ref/2waydirectionalvalveil.html'
language: en
---

# 2-Way Directional Valve (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Isothermal liquid conserving port.

### **B** — Liquid port isothermal liquid

Isothermal liquid conserving port.
### Input

### **S** — Spool displacement, m physical signal

Physical signal associated with the spool displacement, in m. A positive value causes
the valve to open.

## Parameters

### Model Parameterization

### **Orifice parameterization** — Opening area relationship `Linear - area vs. spool travel` (default) | `Tabulated data - Area vs. spool travel` | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`

Method the block uses to calculate the valve flow area. To learn more,
see Orifice Parameterizations.

### **Spool position at maximum orifice area** — Spool offset at maximum area `5e-3` `m` (default) | positive scalar

Position of the spool travel member when the valve is fully open. The
default value represents a zero-lapped system. A positive, nonzero value
represents an underlapped, or partially closed, system. A negative,
nonzero value represents an overlapped system where the valve remains
open over a range of displacements.

### **Spool travel between closed and open orifice** — Maximum spool stroke `5e-3` `m` (default) | positive scalar

Spool offset at the maximum valve opened area.

#### Dependencies

To enable this parameter, set **Orifice
parametrization** to `Linear - area vs.
spool travel`.

### **Maximum orifice area** — Area of fully open valve `1e-4` `m^2` (default) | positive scalar

Maximum valve area experienced during simulation.

#### Dependencies

To enable this parameter, set **Orifice
parametrization** to `Linear - area vs.
spool travel`.

### **Leakage area** — Valve gap area when in fully closed position `1e-10` `m^2` (default) | positive scalar

Sum of all gaps when the valve is in the fully closed position. The block maintains any
area smaller than this value at the specified leakage area. This
parameter contributes to numerical stability by maintaining continuity
in the flow.

#### Dependencies

To enable this parameter, set **Orifice
parametrization** to `Linear - area vs.
spool travel`.

### **Spool travel vector** — Spool opening distance values `[0, .002, .004, .007, .017]` `m` (default) | vector

Vector of control member travel distances. A positive value opens the
valve. The values in this vector correspond one-to-one to values in the
**Orifice area vector** parameter. The values must
ascend from 0. The block interpolates the points linearly.

#### Dependencies

To enable this parameter, set **Orifice
parametrization** to `Tabulated data - Area
vs. spool travel`.

### **Orifice area vector** — Valve opening area values `[1e-09, 2.0352e-07, 4.0736e-05, .00011438, .00034356]` `m^2` (default) | vector

Vector of valve area values for the tabular parametrization of opening
area. The values in this vector correspond one-to-one with the elements
in the **Spool travel vector** parameter. The first
element of this vector is the leakage area, and the last element is the
maximum valve area. The block interpolates the points linearly.

#### Dependencies

To enable this parameter, set **Orifice
parametrization** to `Tabulated data - Area
vs. spool travel`.

### **Spool travel vector, ds** — Tabular spool opening distance values `[0, .002, .004, .007, .017]` `m` (default) | vector

Vector of control member travel distances. The spool travel vector
forms an independent axis with the **Pressure drop vector,
dp** parameter for the 3-D dependent **Volumetric
flow rate table, q(ds,dp)** parameter. A positive
displacement corresponds to valve opening. The values ascend from 0. The
block interpolates the points linearly.

#### Dependencies

To enable this parameter, set **Orifice
parametrization** to `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`.

### **Pressure drop vector, dp** — Tabular pressure drop values `[.3, .5, .7]` `MPa` (default) | vector

Vector of pressure drop values for the volumetric flow rate. The
pressure drop vector forms an independent axis with the **Spool
travel vector, ds** parameter for the 3-D dependent
**Volumetric flow rate table, q(ds,dp)** parameter.
The values must be positive and ascending. The block interpolates the
points linearly

#### Dependencies

To enable this parameter, set **Orifice
parametrization** to `Tabulated data
-Volumetric flow rate vs. spool travel and pressure
drop`.

### **Volumetric flow rate table, q(ds,dp)** — Volumetric flow rate for given spool travel and pressure drop `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13]` `m^3/s` (default) | matrix

*M*-by-*N* matrix of volumetric flow
rates based on independent values of pressure drop and spool travel
distance. *M* and *N* are the sizes of
the correlated vectors:

- *M* is the number of elements in the
  **Spool travel vector, ds**
  parameter.
- *N* is the number of elements in the
  **Pressure drop vector, dp**
  parameter.

#### Dependencies

To enable this parameter, set **Orifice
parametrization** to `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Discharge loss for a hydraulic structure. The default discharge
coefficient for an valve in Simscape™
Fluids™ is 0.64.

#### Dependencies

To enable this parameter, set **Orifice
parametrization** to either:

- `Tabulated data - Area vs. spool
  travel`
- `Linear - area vs. spool
  travel`

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the valve.

#### Dependencies

To enable this parameter, set **Orifice
parametrization** to either:

- `Tabulated data - Area vs. spool
  travel`
- `Linear - area vs. spool
  travel`

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change
based to the flow response when the valve is in near-open and
near-closed positions. To increase the stability of your simulation in
these regimes, set this parameter to a nonzero value less than
one.

#### Dependencies

To enable this parameter, set **Orifice
parametrization** to `Linear - area vs.
spool travel`.

### **Pressure recovery** — Whether to account for pressure increase in area expansions `on` (default) | `off`

Whether to account for pressure increase when the fluid flows from a
region of smaller cross-sectional area to a region of larger
cross-sectional area.

### **Cross-sectional area at ports A and B** — Valve area at conserving ports `inf` `m^2` (default) | positive scalar

Cross-sectional area at ports **A** and **B**. The
block uses this area in the pressure-flow rate equation to determine the
volumetric flow rate through the valve.

#### Dependencies

To enable this parameter, set **Orifice
parametrization** to either:

- `Tabulated data - Area vs. spool
  travel`
- `Linear - area vs. spool
  travel`

### Faults

### **2-Way Directional Valve Area fault** — Option to model spool position fault `Add fault`

Option to model a spool position fault in the block. To add a fault, click the
**Add fault** hyperlink. When a fault occurs, the
valve area normally set by the opening parameterization is set based on
the value specified in the **Spool position when
faulted** parameter.

### **Spool position when faulted** — Faulted valve characteristics `Positive` (default) | `Negative` | `Maintain last value`

Faulted valve spool position. You can choose for the valve to seize
when the spool is in the positive position, negative position, or at the
position when the fault triggers.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink.

## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Directional Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

### R2024a: Model faults with the Simscape faults interface

The 2-Way Directional Valve (IL) block now supports the Simscape faults interface. To learn more, see Introduction to Simscape Faults.

## Description

2-way flow control valve in an isothermal liquid systems

The 2-Way Directional Valve (IL) block represents a two-way
valve, such as a shut-off valve. Use this block to simulate a flow-reducing control
element that responds to pressures in another part of the system.

The block uses a variable orifice to control the flow between ports **A**
and **B**. The physical signal at port **S** triggers
the spool motion to open or shut the valve. For more details about how the block
calculates flow rate through a variable orifice, see Orifice (IL).

### Orifice Parameterizations

You can parameterize the valve opening linearly or by using tabulated data.

**Linear**

When you set **Orifice parameterization** to
`Linear - Area vs. spool travel`, the opening area
is a linear function of the spool travel distance.

Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak,

where

- *Aorifice* is the opening
  area.
- *ΔS* is the spool travel distance input at port
  **S**. ΔS=S−Smax+ΔSmax.
- *ΔSmax* is the value of
  the **Spool travel between closed and open
  orifice** parameter.
- *ALeak* is the value of
  the **Leakage area** parameter.
- *Amax* is the value of the
  **Maximum orifice area** parameter.

Note the linear scaling from
*ALeak* to
*Amax* in the figure.

When the valve is in a near-open or near-closed position in the
linear parameterization, you can maintain numerical robustness in your simulation by adjusting
the **Smoothing factor** parameter. If the **Smoothing
factor** parameter is nonzero, the block smoothly saturates the opening area
between *Aleak* and
*Amax*. For more information, see Numerical Smoothing.

**Tabulated**

When you set **Orifice parameterization** to
`Tabulated data - Area vs. spool travel`, the block
uses the **Spool travel vector** and **Orifice area
vector** parameters to define the relationship between
*Aorifice* and
*ΔS* by interpolation.
*Aleak* and
*Amax* are the first and last
parameters of the **Orifice area vector** parameter, respectively.

When you set **Orifice parameterization** to
`Tabulated data - Volumetric flow rate vs. spool travel and
pressure drop`, the block uses the **Volumetric flow
rate table, q(ds,dp)**, **Pressure drop vector,
dp**, and **Spool travel vector, ds** parameters
to define the volumetric flow rate,
*q(**ΔS**,**p**)*.

### Visualize Orifice Openings

To visualize the spool offsets and displacement, right-click the block and select **Fluids** > **Plot Valve Characteristics**. The plot shows the valve open area or volumetric flow rate as a
function of spool position.

To update the data after changing the block parameters, click **Reload
Data** in the figure window.

This figure shows the valve configuration with:

- **Spool position at maximum orifice area** set to
  `2e-3` m.
- **Spool travel between closed and open orifice** set
  to `6e-3` m.

All other parameters are at the default values.

Plot of area versus spool position for each orifice.

### Faults

To model a fault, in the **Faults** section,
click the **Add fault** hyperlink next to the fault that you want to model. Use
the fault parameters to specify the fault properties. For more information about fault modeling,
see Introduction to Simscape Faults.

You can choose the type of fault by using the **Spool position when
faulted** parameter:

- `Negative` — The block freezes the valve at
  its smallest value. The table shows which value the block uses depending
  on the setting of the **Orifice parameterization**
  parameter.

  | **Orifice parameterization** Parameter Setting | Freeze Position Value |
  | --- | --- |
  | `Linear - Area vs. spool travel` | **Leakage area** parameter |
  | `Tabulated data - Area vs. spool travel` | First element of the **Orifice area vector** parameter |
  | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` | First row of the **Volumetric flow rate table, q(ds,dp)** parameter |
- `Positive` — The valve freezes at its largest
  value. The table shows which value the block uses depending on the
  setting of the **Orifice parameterization**
  parameter.

  | **Orifice parameterization** Parameter Setting | Freeze Position Value |
  | --- | --- |
  | `Linear - Area vs. spool travel` | **Maximum opening area** parameter |
  | `Tabulated data - Area vs. spool travel` | Last element of the **Orifice area vector** parameter |
  | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` | Last row of the **Volumetric flow rate table, q(ds,dp)** parameter |
- `Maintain last value` — The valve freezes at
  its last value. The table shows which value the block uses depending on
  the setting of the **Orifice parameterization**
  parameter.

  | **Orifice parameterization** Parameter Setting | Freeze Position Value |
  | --- | --- |
  | `Linear - Area vs. spool travel` | The valve open area when the trigger occurred |
  | `Tabulated data - Area vs. spool travel` | The valve open area when the trigger occurred |
  | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` | Current position |

  When you set **Orifice
  parameterization** to `Tabulated data -
  Volumetric flow rate vs. spool travel and pressure
  drop`, the volumetric flow rate continues to change
  according to pressure changes in the valve after the valve
  freezes.

Due to numerical smoothing at the extremes of the valve area, in the
linear parameterization, the minimum area that he block uses is larger than the
**Leakage area**, and the maximum is smaller than the
**Maximum orifice area**, in proportion to the
**Smoothing factor** value. For more information, see Numerical Smoothing.
