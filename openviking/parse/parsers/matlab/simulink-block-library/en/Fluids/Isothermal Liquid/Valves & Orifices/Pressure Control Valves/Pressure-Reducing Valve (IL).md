---
type: simulink-block
title: 'Pressure-Reducing Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Pressure Control Valves'
documentation_page: 'pressurereducingvalveil'
documentation_source_path: 'ref/pressurereducingvalveil.html'
language: en
---

# Pressure-Reducing Valve (IL)

## Ports

### Input

### **Ps** — Set pressure signal, Pa physical signal

Pressure threshold for controlled valve operation, in Pa.

#### Dependencies

To enable this
port, set **Set pressure control** to
`Controlled`.
### Conserving

### **A** — Liquid port isothermal liquid

Entry or exit point to the valve.

### **B** — Liquid port isothermal liquid

Entry or exit point to the valve.

## Parameters

### Parameters

### **Set pressure control** — Valve operation method `Constant` (default) | `Controlled`

Valve operation method. When you set this parameter to
`Constant`, the valve closes linearly over
a fixed pressure regulation range or in accordance with the tabulated
pressure and opening area data that you provide. When you set this
parameter to `Controlled`, the valve closes
according to a variable set pressure signal at port
**Ps** over a fixed pressure regulation
range.

### **Opening parameterization** — Opening parameterization `Linear - Area vs. pressure` (default) | `Tabulated data - Area vs. pressure` | `Tabulated data - Volumetric flow rate vs. pressure`

Method of modeling the opening of the valve. When you select `Linear - Area
vs. pressure` or `Tabulated data - Area vs.
pressure`, the block relates the opening area to the
control pressure. When you select `Tabulated data -
Volumetric flow rate vs. pressure`, the block takes a
reference flow rate and pressure differential curve of the reducing
valve..

### **Set pressure (gauge)** — Gauge pressure beyond which valve operation triggers `0.1` `MPa` (default) | positive scalar

Gauge pressure beyond which valve operation triggers. When the
pressure at port **B** reaches this value, the valve
begins to shut. This parameter shifts the reference curve so the
reducing valve begins to close when the pressure at port
**B** equals the set pressure.

#### Dependencies

To enable this parameter, set **Set pressure
control** to
`Constant`.

### **Pressure regulation range** — Valve operational pressure range `1` `MPa` (default) | positive scalar

Operational pressure range of the valve. The pressure regulation range
begins at the **Set pressure (gauge)** and the end of
the range is the maximum valve operating pressure.

#### Dependencies

To enable this parameter, set **Opening parameterization** to
`Linear - Area vs. pressure`.

### **Maximum opening area** — Area of fully opened valve `1e-4` `m^2` (default) | positive scalar

Cross-sectional area of the valve in the fully open position.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure`.

### **Leakage area** — Valve gap area when in fully closed position `1e-10` `m^2` (default) | positive scalar

Sum of all gaps when the valve is in the fully closed position. Any area smaller than
this value saturates to the specified leakage area. This parameter
contributes to numerical stability by maintaining continuity in the
flow.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure`.

### **Pressure at port B (gauge) vector** — Vector of gauge pressure values for tabulated area parameterization `[0.2 : 0.2 : 1.2]` `MPa` (default) | 1-by-*n* vector

Vector of gauge pressure values for the tabulated parameterization of
the valve opening area. The vector elements must correspond one-to-one
with the elements in the **Opening area vector**
parameter. The elements must be positive and in ascending order. The
block uses linear interpolation between the data points.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Tabulated data -
Area vs. pressure`.

### **Opening area vector** — Valve opening areas for tabulated parameterization `[1e-05, 8e-06, 6e-06, 4e-06, 2e-06, 1e-10]` `m^2` (default) | 1-by-*n* vector

Vector of valve opening areas for the tabulated parameterization of the valve opening
area. The vector elements must correspond one-to-one with the elements
in the **Pressure at port B (gauge) vector** parameter.
The elements must be positive and in ascending order. The block uses
linear interpolation between the data points.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Tabulated data -
Area vs. pressure`.

### **Cross-sectional area at ports A and B** — Area at valve entry or exit `inf` `m^2` (default) | positive scalar

Cross-sectional area at the entry and exit ports **A** and
**B**. The block uses these areas in the
pressure-flow rate equation that determines the mass flow rate through
the valve.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure` or `Tabulated data - Area vs.
pressure`.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor that accounts for discharge losses in theoretical flows.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure` or `Tabulated data - Area vs.
pressure`.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the valve.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure` or `Tabulated data - Area vs.
pressure`.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change
to the flow response when the valve is in near-open or near-closed
positions. Set this value to a nonzero value less than one to increase
the stability of your simulation in these regimes.

#### Dependencies

To enable this parameter, set **Opening parameterization** to
`Linear - Area vs. pressure`.

### **Pressure recovery** — Option to include pressure increase during area expansions `off` (default) | `on`

Whether to capture the increase in pressure when fluid flows from a region of smaller
cross-sectional area to a region of larger cross-sectional area.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure` or `Tabulated data - Area vs.
pressure`.

### **Opening dynamics** — Option to include flow response to valve opening `off` (default) | `on`

Whether to approximate the transient effects to the fluid system due to valve opening.
Selecting **Opening dynamics** approximates opening
conditions by introducing a first-order lag in the flow response.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure` or `Tabulated data - Area vs.
pressure`.

### **Opening time constant** — Valve opening time constant `0.1` `s` (default) | positive scalar

Time constant by which to compute the lag in the opening dynamics.

#### Dependencies

To enable this parameter, select **Opening dynamics** and set
**Opening parameterization** to
`Linear - Area vs. pressure` or
`Tabulated data - Area vs.
pressure`.

### **Reference pressure at port A (gauge)** — Reference pressure at port A `1.5` `MPa` (default) | positive scalar

Constant pressure at port **A** that forms the basis of the reference
curve. This value typically corresponds to the maximum operating
pressure of the valve. The pressure at port **A** can
be any value during simulation.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Tabulated data -
Volumetric flow rate vs. pressure`.

### **Reference pressure at port B (gauge) vector** — Reference pressure at port B `[1.2, 1, .8, .6, .4, .2]` `MPa` (default) | 1-by-*n* vector

Vector of monotonically decreasing pressure values at port **B** in the
reference curve as the valve opening area changes. The first element is
the reference maximum pressure, which is the pressure where the valve
fully shuts. The last element is the reference set pressure.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Tabulated data -
Volumetric flow rate vs. pressure`.

### **Reference volumetric flow rate vector** — Reference volumetric flow rate `[1e-09, 1.8e-05, 6.6e-05, .00013, .0002, .00028]` `m^3/s` (default) | 1-by-*n* vector

Vector of monotonically increasing reference flow rates through the valve. The block
uses this curve to generate a flow coefficient for the changing valve
area.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Tabulated data -
Volumetric flow rate vs. pressure`.

### Check Valve

### **Enable check valve** — Check valve option `off` (default) | `on`

Whether the block simulates an internal check valve.

### **Cracking pressure differential** — Set pressure for check valve operation `0.1` `MPa` (default) | positive scalar

Pressure differential that lifts the check valve.

#### Dependencies

To enable this parameter, set **Enable check
valve** to `On` and
**Valve parameterization** to
`Linear - Area vs. pressure`.

### **Maximum opening pressure differential** — Maximum pressure in valve `0.2` `MPa` (default) | positive scalar

Pressure differential when the check valve fully shuts.

#### Dependencies

To enable this parameter, set **Enable check
valve** to `On` and
**Valve parameterization** to
`Linear - Area vs. pressure`.

### **Maximum opening area** — Maximum open area `1e-4` `m^2` (default) | positive scalar

Maximum open area of the check valve in the load line. Internally, the check valve is in
parallel with the reducing stage.

#### Dependencies

To enable this parameter, set **Enable check
valve** to `On` and
**Valve parameterization** to
`Linear - Area vs. pressure`.

### **Pressure differential vector** — Pressure differential for check valve operation `[0.01 : 0.01 : 1]` `MPa` (default) | 1-by-*n* vector

Vector of pressure differentials for the check valve stage. The block computes the check
valve pressure differential as pressure at port **B**
with respect to pressure at port **A**.

#### Dependencies

To enable this parameter, set **Enable check
valve** to `On` and
**Valve parameterization** to
`Tabulated data - Area vs. pressure` or
`Tabulated data - Volumetric flow rate vs.
pressure`.

### **Opening area vector** — Check stage opening areas `[1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001]` `m^2` (default) | 1-by-*n* vector

Vector of opening areas for the check valve stage. The vector elements
must correspond one-to-one with the elements in the **Pressure
differential vector** parameter.

#### Dependencies

To enable this parameter, set **Enable check
valve** to `On` and
**Valve parameterization** to
`Tabulated data - Area vs.
pressure`.

### **Volumetric flow rate vector** — Check stage volumetric flow rates `[.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3` `m^3/s` (default) | 1-by-*n* vector

Vector of volumetric flow rates for the check valve stage. The
elements of this vector must correspond to the elements in the
**Pressure differential vector** parameter.

#### Dependencies

To enable this parameter, set **Enable check
valve** to `On` and
**Valve parameterization** to
`Tabulated data - Volumetric flow rate vs.
pressure`.

### Faults

### **Pressure-Reducing Valve Area fault** — Option to model reducing valve fault `Add fault`

Option to enable the fault parameters for the reducing valve. To add a fault, click the
**Add fault** hyperlink. When faulting occurs, the
block sets the opening area to the position specified by the
**Reducing valve opening when faulted** parameter.

### **Reducing valve opening when faulted** — Reducing valve fault position `Closed` (default) | `Open` | `Maintain last value`

Faulted reducing valve position. You can choose for the valve to fault while open, shut,
or in place.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Pressure-Reducing Valve Area fault**
parameter.

### **Check Valve Area fault** — Option to model check valve fault `Add fault`

Option to enable the fault parameters for the check valve. To add a fault, click the
**Add fault** hyperlink. When a fault occurs, the
block sets the opening area to the position specified by the
**Check valve opening when faulted** parameter.

#### Dependencies

To enable this parameter, select **Enable check
valve**.

### **Check valve opening when faulted** — Faulted valve characteristics `Closed` (default) | `Open` | `Maintain last value`

Faulted check valve position. You can choose for the valve to fault while open, shut, or
in place.

#### Dependencies

To enable this parameter, select **Enable check valve** and click
**Add fault** hyperlink for the
**Check Valve Area fault** parameter.

## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Pressure Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

### R2024a: Model faults with the Simscape faults interface

The Pressure-Reducing Valve (IL) block now supports the Simscape™ faults interface. To learn more, see Introduction to Simscape Faults.

### R2022b: Parameterize by volumetric flow rate vs. pressure

You can set **Opening parameterization** to
`Tabulated data - Volumetric flow rate vs.
pressure`.

### R2022b: Access pre-parameterized block options

The block supports pre-parameterization options. Suppliers include Hawe Hydraulik,
Rexroth Bosch Group, and Sun Hydraulics.

## Description

Pressure-reducing valve in an isothermal liquid network

The Pressure-Reducing Valve (IL) block represents a
pressure-reducing valve in an isothermal liquid network. The valve remains open when the
pressure at port **B** is less than a specified pressure. When the
pressure at port **B** meets or surpasses this pressure, the valve
closes. The block operates based on the differential between the set pressure and the
pressure at port **B**. The block contains a check valve portion that
functions identically to the Check Valve
(IL) block during flow reversals. For pressure control based on
another location in the fluid network, see the Pressure Compensator
Valve (IL) block.

### Set Pressure Control

The block regulates pressure between the set pressure and maximum pressure. When you set
**Set pressure control** to:

- `Controlled` — You can connect a pressure
  signal to port **Ps**. The block regulates pressure
  when the pressure at port **B** is greater than the
  reference set pressure, *Pset*,
  and below *Pmax*. The pressure
  at port **B** acts as the control pressure,
  *Pcontrol*, for this
  valve.

  *Pmax* is the sum of
  *Pset* and the pressure
  regulation range.
- `Constant` — The **Set pressure
  (gauge)** parameter defines a constant set pressure.

How the block determines the pressure regulation range depends on the
**Opening parameterization** parameter:

- `Linear - Area vs. pressure` — The
  **Pressure regulation range** parameter defines the
  pressure regulation range.
- `Tabulated data - Area vs. Pressure` — The
  pressure regulation range is the difference between the last and first
  elements of the **Pressure at port B (gauge) vector**
  parameter.
- `Tabulated data - Volumetric flow rate vs.
  pressure` — The pressure regulation range is the
  difference between the first and last elements of the
  **Reference pressure at port B (gauge) vector**
  parameter.

### Area vs. Pressure Parameterizations

When you set **Opening parameterization** to `Linear - Area
vs. pressure`, the block calculates the valve area as

Avalve=p^(Aleak−Amax)+Amax,

where the normalized pressure,p^, is

p^=pcontrol−psetpmax−pset.

When the valve is in a near-open or near-closed position
in the linear parameterization, you can maintain numerical robustness in your
simulation by adjusting the **Smoothing factor** parameter. If
the **Smoothing factor** parameter is nonzero, the block smoothly
saturates the control pressure between
*pset* and
*pmax*. For more information, see
Numerical Smoothing.

The figure demonstrates the opening characteristics of the valve when using the linear area
parameterization. The opening area,
*Avalve*, drops linearly with the outlet
pressure, *pB,gauge*. The opening area
ranges from *Aleak* to
*AMax*, and the pressure operating
range starts at *pset* and goes to
*pmax*.

Plot of the opening area with respect to pressure for the linear area parameterization

When you set **Opening parameterization** to `Tabulated data -
Area vs. Pressure`, the block calculates the opening area as

Avalve=tablelookup(pcontrol,TLU,ATLU,pcontrol,interpolation=linear,extrapolation=nearest),

where:

- *pcontrol* =
  *pB,gauge* is the
  control pressure.
- *pcontrol,TLU* =
  *pB,TLU* +
  *poffset*.
- *pB,TLU* is the
  **Pressure at port B (gauge) vector**
  parameter.
- *poffset* is an internal
  pressure offset that causes the valve to start closing when
  *pB,Gauge* =
  *pset*, where
  *poffset* =
  *pset* -
  *pB,TLU(1)*.
- *ATLU* is the
  **Opening area vector** parameter.

*Amax* and
*Aleak* are the first and last
parameters of the **Opening area vector** parameter, respectively.
The figure demonstrates the opening characteristics of the valve when using the
tabulated area parameterization.

Plot of the opening area with respect to pressure for the tabulated area parameterization

**Conservation of Mass**

When you set **Opening parameterization** to
`Linear - Area vs. pressure` or
`Tabulated data - Area vs. Pressure`, the block
conserves mass such that:

m˙A+m˙B=0.

The block calculates the mass flow rate as

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

where:

- *Cd* is the
  **Discharge coefficient** parameter.
- *Avalve* is the
  instantaneous valve open area.
- *Aport* is the
  **Cross-sectional area at ports A and B**
  parameter.
- ρ¯ is the average fluid density.
- *Δp* is the valve pressure difference
  *pA* –
  *pB*.

The critical pressure difference,
*Δpcrit*, is the pressure
differential associated with the **Critical Reynolds number**
parameter, *Recrit*, the flow regime
transition point between laminar and turbulent flow:

Δpcrit=πρ¯8Avalve(νRecritCd)2.

*Pressure loss* describes the reduction of pressure in the
valve due to a decrease in area. The block calculates
*PRloss* as:

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport.

*Pressure recovery* describes the positive pressure change in the valve
due to an increase in area. If you do not want to capture this increase in
pressure, clear the **Pressure recovery** check box. In this
case, *PRloss* is 1.

The block determines the opening area,
*Avalve*, using the valve opening
dynamics.

**Opening Dynamics**

For either area parameterization, you can choose to simulate the opening dynamics of the
valve response. If you select **Opening dynamics**, the block
adds a lag to the flow response when the valve opens, and
*Avalve* becomes the dynamic
opening area, *Adyn*. Otherwise,
*Avalve* is the steady-state
opening area. The block calculates the instantaneous change in the dynamic
opening area based on the **Opening time constant** parameter,
*τ*:

p˙dyn=pcontrol−pdynτ.

By default, the block ignores opening dynamics.

The block calculates the steady-state dynamics based on the control pressure,
*pcontrol*, and using the same
parameterization as the valve opening.

### Volumetric Flow Rate vs. Pressure Parameterization

The volumetric flow rate parameterization equations refer to these quantities:

- *⩒TLU,ref* is the
  **Reference volumetric flow rate vector**
  parameter.
- *PA,gauge,ref* and
  *PB,gauge,ref* are the
  **Reference pressure at port A (gauge) vector** and
  **Reference pressure at port B (gauge) vector**
  parameters, respectively.
- *pset,gauge* is either the
  **Set pressure (gauge)** parameter or the signal at
  port **Ps**.
- *K* is the flow coefficient through the reducing
  stage, which the block calculates during the simulation.
- ρ¯ is the average fluid density in the reducing
  valve.
- *Δp* is the pressure drop across the valve for fluid
  flow.
- *Δpcrit* is the critical
  pressure drop for fluid flow.
- *Cd* is the discharge
  coefficient, which the block sets internally for the volumetric flow
  rate parameterization.
- *Recrit* is the critical
  Reynolds number, which the block sets internally.
- *ν* is the kinematic viscosity, which is constant for
  the isothermal liquid network.

When you set **Opening parameterization** to
`Tabulated data - Volumetric flow rate vs. pressure`,
the block calculates the smoothed mass flow rate of the reducing valve such that

m˙valve=ρ¯KΔp(Δp2+Δp2)14Δp=pA−pBΔpcrit=π2ρ¯8CdK(Recritν)2

where the block computes *K* using a
`tablelookup` function such that

K=tablelookup(Δpcontrol,TLU,Ref,KTLU,Ref,Δpcontrol,interpolation=linear,extrapolation=nearest)KTLU,Ref=V˙TLU,RefΔpTLU,Ref

The block calculates the control pressure as

Δpcontrol=pB−pdrain,

where the block sets the drain pressure, *pdrain*, to 1 atm. The block calculates the reference control pressure
vector as

Δpcontrol,TLU,Ref=pB,gauge,ref+poffset,

where *poffset* is an
internally computed pressure offset that causes the valve to start shutting when *pB,gauge,ref* =
*pset,gauge*. Thus, *poffset* =
*pset,gauge* -
*pB,gauge,ref*. The figure shows how the block controls pressure using the
tabulated volumetric flow rate parameterization.

Plot of the opening area with respect to pressure for the tabulated volume parameterization

### Faults

To model a fault, in the **Faults** section,
click the **Add fault** hyperlink next to the fault that you want to model. Use
the fault parameters to specify the fault properties. For more information about fault modeling,
see Introduction to Simscape Faults.

Three fault options are available for the reducing valve and check valve. For the
**Reducing valve opening when faulted** and **Check
valve opening when faulted** parameters, you can choose:

- `Closed` — The valve shuts to its smallest
  opening value, depending on the **Opening
  parameterization** parameter. When you set
  **Opening parameterization** to:

  - `Linear - Area vs. pressure` —
    The valve area reduces to the value of the **Leakage
    area** parameter.
  - `Tabulated data - Area vs.
    pressure` — The valve area reduces to the
    value of the last element in the **Opening area
    vector** parameter.
  - `Tabulated data - Volumetric flow rate vs.
    pressure` — The flow coefficient reduces to
    the value of the last element of the derived flow
    coefficient lookup table,
    *KTLU,Ref*.
- `Open` — The valve opens to its largest
  opening value, depending on the **Opening
  parameterization** parameter. When you set
  **Opening parameterization** to:

  - `Linear - Area vs. pressure` —
    The valve area opens to the value of the **Maximum
    opening area**.
  - `Tabulated data - Area vs.
    pressure` — The valve area opens to the
    value of the first element in the **Opening area
    vector**.
  - `Tabulated data - Volumetric flow rate vs.
    pressure` — The flow coefficient reduces to
    the value of the first element of the derived flow
    coefficient lookup table,
    *KTLU,Ref*.
- `Maintain last value` — The valve area
  remains at the valve opening area when the trigger occurred.

For the linear parameterization, numerical smoothing at the extremes
of the valve area causes the minimum area applied to be larger than the
**Leakage area** parameter, and the maximum is smaller than
the **Maximum orifice area** parameter.

After the fault triggers, the valve remains at the faulted area for the rest of the
simulation.

### Predefined Parameterization

You can populate the block with pre-parameterized manufacturing data, which allows you to
model a specific supplier component.

To load a predefined parameterization:

1. In the block dialog box, next to **Selected part**, click the
   "<click to select>" hyperlink next to **Selected part** in
   the block dialog box settings.
2. The Block Parameterization Manager window opens. Select a part from the menu
   and click **Apply all**. You can narrow the choices using the
   **Manufacturer** drop down menu.
3. You can close the **Block Parameterization Manager** menu.
   The block now has the parameterization that you specified.
4. You can compare current parameter settings with a specific supplier component
   in the Block Parameterization Manager window by selecting a part and viewing the
   data in the **Compare selected part with block**
   section.

**Note**

Predefined block parameterizations use available data sources to supply parameter
values. The block substitutes engineering judgment and simplifying assumptions for
missing data. As a result, expect some deviation between simulated and actual physical
behavior. To ensure accuracy, validate the simulated behavior against experimental data
and refine your component models as necessary.

To learn more, see List of Pre-Parameterized Components.
