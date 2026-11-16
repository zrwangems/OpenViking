---
type: simulink-block
title: 'Check Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Valves and Orifices / Directional Control Valves'
documentation_page: 'checkvalveil'
documentation_source_path: 'ref/checkvalveil.html'
language: en
---

# Check Valve (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Entry point to the valve.

### **B** — Liquid port isothermal liquid

Exit point to the valve.

## Parameters

### Parameters

### **Opening parameterization** — Method of calculating valve opening `Linear - Area vs. pressure` (default) | `Tabulated data - Area vs. pressure` | `Tabulated data - Volumetric flow rate vs. pressure`

Method of calculating valve opening.

- `Linear - Area vs. pressure`: The
  valve opening area corresponds linearly to the valve
  pressure.
- `Tabulated data - Area vs.
  pressure`: The valve mass flow rate is
  determined from a table of area values with respect to
  pressure differential.
- `Tabulated data - Volumetric flow rate vs.
  pressure`: The valve mass flow rate is
  determined from a table of volumetric flow rate values with
  respect to pressure differential.

### **Opening pressure specification** — Pressure differential used for valve control `Pressure differential` (default) | `Pressure at port A`

Specifies the control pressure differential. The `Pressure
differential` option refers to the pressure difference
between ports **A** and **B**. The
`Pressure at port A` option refers to the
pressure difference between port **A** and atmospheric
pressure.

#### Dependencies

To enable this parameter, set **Opening parameterization** to
`Linear - Area vs. pressure`.

### **Cracking pressure differential** — Threshold pressure `0.01 MPa` (default) | positive scalar

Pressure beyond which the valve operation is triggered. This is the set pressure when
the control pressure is the pressure differential between ports
**A** and **B**.

#### Dependencies

To enable this parameter, set **Opening pressure specification** to
`Pressure differential` and
**Opening parameterization** to
`Linear - Area vs. pressure`.

### **Cracking pressure (gauge)** — Threshold pressure `0.1 MPa` (default) | positive scalar

Gauge pressure beyond which valve operation is triggered when the control pressure is
the pressure differential between port **A** and
atmospheric pressure.

#### Dependencies

To enable this parameter, set **Opening parameterization** to
`Linear - Area vs. pressure` and
**Opening pressure specification** to
`Pressure at port A`.

### **Maximum opening pressure differential** — Valve differential pressure maximum `0.1 MPa` (default) | positive scalar

Maximum valve differential pressure. This parameter provides an upper
limit to the pressure so that system pressures remain realistic.

#### Dependencies

To enable this parameter, set **Opening parameterization** to
`Linear - Area vs. pressure` and
**Opening pressure specification** to
`Pressure differential`.

### **Maximum opening pressure (gauge)** — Valve pressure maximum `0.2 MPa` (default) | positive scalar

Maximum valve gauge pressure. This parameter provides an upper limit
to the pressure so that system pressures remain realistic.

#### Dependencies

To enable this parameter, set **Opening parameterization** to
`Linear - Area vs. pressure` and
**Opening pressure specification** to
`Pressure at port A`.

### **Maximum opening area** — Area of fully opened valve `1e-4 m^2` (default) | positive scalar

Cross-sectional area of the valve in its fully open position.

#### Dependencies

To enable this parameter, set **Opening parameterization** to
`Linear - Area vs. pressure`.

### **Leakage area** — Valve gap area when in fully closed position `1e-12 m^2` (default) | positive scalar

Sum of all gaps when the valve is in its fully closed position. Any
area smaller than this value is saturated to the specified leakage area.
This contributes to numerical stability by maintaining continuity in the
flow.

#### Dependencies

To enable this parameter, set **Opening parameterization** to
`Linear - Area vs. pressure`.

### **Pressure differential vector** — Differential pressure values for tabular parameterization `[0.01 : 0.01 : 0.1] MPa` (default) | 1-by-*n* vector

Vector of pressure differential values for the tabular
parameterization of the valve opening area. The vector elements must
correspond one-to-one with the elements in the **Opening area
vector** parameter. The elements are listed in ascending
order and must be greater than 0. Linear interpolation is employed
between table data points.

#### Dependencies

To enable this parameter, set:

- **Set pressure control** to
  `Constant`.
- **Opening parameterization** to
  `Linear - Area vs.
  pressure` or `Tabulated
  data - Area vs. pressure`.
- **Opening pressure specification** to
  `Pressure
  differential`.

### **Opening area vector** — Valve opening areas for tabular parameterization `[1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of valve opening areas for the tabular parameterization of the
valve opening area. The vector elements must correspond one-to-one with
the elements in the **Pressure differential vector**
parameter. The elements are listed in ascending order and must be
greater than 0. Linear interpolation is employed between table data
points.

#### Dependencies

To enable this parameter, set **Set pressure
control** to `Constant` and
**Opening parameterization** to
`Tabulated data - Area vs.
pressure`.

### **Cross-sectional area at ports A and B** — Area at valve entry or exit `inf m^2` (default) | positive scalar

Cross-sectional area at the entry and exit ports
**A** and **B**. These areas are
used in the pressure-flow rate equation that determines the mass flow
rate through the valve.

#### Dependencies

To enable this parameter, set **Opening parameterization** to
`Linear - Area vs. pressure` or
`Tabulated data - Area vs.
pressure`.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor that accounts for discharge losses in theoretical
flows.

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

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar

Continuous smoothing factor that introduces a layer of gradual change
to the flow response when the valve is in near-open or near-closed
positions. Set this value to a nonzero value less than one to increase
the stability of your simulation in these regimes.

#### Dependencies

To enable this parameter, set **Opening parameterization** to
`Linear - Area vs. pressure`.

### **Pressure recovery** — Whether to account for pressure increase in area expansions `off` (default) | `on`

Whether to account for pressure increase when fluid flows from a
region of smaller cross-sectional area to a region of larger
cross-sectional area.

#### Dependencies

To enable this parameter, set **Opening parameterization** to
`Linear - Area vs. pressure`.

### **Opening dynamics** — Whether to account for flow response to valve opening `off` (default) | `on`

Whether to account for transient effects to the fluid system due to opening the valve.
Selecting **Opening dynamics** approximates the opening
conditions by introducing a first-order lag in the flow response. The
**Opening time constant** also impacts the modeled
opening dynamics.

#### Dependencies

To enable this parameter, set **Opening parameterization** to
`Linear - Area vs. pressure`.

### **Opening time constant** — Valve opening time constant `0.1 s` (default) | positive scalar

Constant that captures the time required for the fluid to reach
steady-state when opening or closing the valve from one position to
another. This parameter impacts the modeled opening dynamics.

#### Dependencies

To enable this parameter, set **Opening parameterization** to
`Linear - Area vs. pressure` and select
**Opening dynamics**.

### **Volumetric flow rate vector** — Vector of volumetric flow rate for tabulated data parameterization `[.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3 m^3/s` (default) | 1-by-*n* vector

Vector of volumetric flow rate values for the tabular parameterization
of valve opening. This vector must have the same number of elements as
the **Pressure drop vector** parameter. The vector
elements must be listed in ascending order.

#### Dependencies

To enable this parameter, set **Opening parameterization** to
`Tabulated data - Volumetric flow rate vs.
pressure`.

### Faults

### **Check Valve Area fault** — Option to model valve area fault `Add fault`

Option to model a valve area fault in the block. To add a fault, click the **Add
fault** hyperlink. When a fault occurs, the valve area
normally set by the opening parameterization is set based on the value
specified in the **Opening area when faulted**
parameter.

### **Opening area when faulted** — Faulted valve characteristics `Closed` (default) | `Open` | `Maintain at last value`

Faulted valve area. You can choose for the valve to seize at the fully
closed or fully open position, or at the conditions when faulting is
triggered. This parameter sets the area when **Opening
parameterization** is `Linear - Area vs.
pressure` and the mass flow rate when **Opening
parameterization** is `Tabulated
data`.

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

### R2025a: Generate a digital data sheet

Generate a digital data sheet that includes performance data and pressure drop vs.
volumetric flow rate curves by using the **Generate datasheet**
hyperlink in the **Description** tab of the block dialog box. The
hyperlink opens a script that imports the parameters from the Check Valve (IL) block that
you select in the model. You can use the characteristic curves to evaluate the
cracking pressure and leakage flow.

### R2024a: Model faults with the Simscape faults interface

The Check Valve (IL) block now supports the Simscape™ faults interface. To learn more, see Introduction to Simscape Faults.

## Description

Check valve in an isothermal liquid system

The Check Valve (IL) block represents a check valve
with free flow from port **A** to port **B** and
restricted flow from port **B** to port **A**. When
the pressure at port **A** or the pressure differential meets or
exceeds the set pressure threshold, the valve begins to open.

### Opening Parameterization

When **Opening parameterization** is set to `Linear -
Area vs. pressure`, the valve open area is linearly related to the
opening pressure differential.

**Opening Pressure**

There are two options for valve control:

- When **Opening pressure differential**  is set to
  `Pressure differential`, the control
  pressure is the pressure differential between ports
  **A** and **B**. The valve
  begins to open when
  *P*control meets or
  exceeds the **Cracking pressure
  differential**.
- When **Opening pressure differential**  is set to
  `Pressure at port A`, the control
  pressure is the pressure difference between port
  **A** and atmospheric pressure. When
  *P*control meets or
  exceeds the **Cracking pressure (gauge)**, the
  valve begins to open.

**Opening Area and Pressure**

The linear parameterization of the valve area is

Avalve=p^(Amax−Aleak)+Aleak,

where the normalized pressure, p^, is

p^=pcontrol−pcrackingpmax−pcracking.

When the valve is in a near-open or
near-closed position in the linear parameterization, you can maintain numerical
robustness in your simulation by adjusting the **Smoothing
factor** parameter. If the **Smoothing factor**
parameter is nonzero, the block smoothly saturates the control pressure between
*pcracking* and
*pmax*. For more information,
see Numerical Smoothing.

When you set **Opening parameterization** to
`Tabulated data - Volumetric flow rate vs.
pressure`, *Avalve* is
the linearly interpolated value of the **Opening area vector**
parameter versus **Pressure differential vector** parameter
curve for a simulated pressure differential.

**Mass Flow Rate Equation**

Mass is conserved through the valve:

m˙A+m˙B=0.

The mass flow rate through the valve is calculated as:

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

where:

- *C*d is the
  **Discharge coefficient**.
- *A*valve is the
  instantaneous valve open area.
- *A*port is the
  **Cross-sectional area at ports A and
  B**.
- ρ¯ is the average fluid density.
- *Δp* is the valve pressure difference
  *p*A –
  *p*B.

The critical pressure difference,
*Δp*crit, is the pressure
differential associated with the **Critical Reynolds number**,
*Re*crit, the flow regime transition
point between laminar and turbulent flow:

Δpcrit=πρ¯8Avalve(νRecritCd)2.

*Pressure loss* describes the reduction of pressure in the
valve due to a decrease in area.
*PR*loss is calculated as:

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport.

*Pressure recovery* describes the positive pressure change in the valve
due to an increase in area. If you do not want to capture this increase in
pressure, clear the **Pressure recovery** check box. In this
case, *PR*loss is 1.

### Tabulated Volumetric Flow Rate Parameterization

When **Opening parameterization** is set to
`Tabulated data - Volumetric flow rate vs. pressure`,
the valve opens according to the user-provided tabulated data of volumetric flow
rate and pressure differential between ports **A** and
**B**.

The mass flow rate is

m˙=ρ¯KΔp(Δp2+Δpcrit2)1/4,

where:

- ρ¯ is the average fluid density.
- Δp=pA−pB.
- Δpcrit=π2ρ¯8CdK(Recritv)2, where *Cd* is the
  discharge coefficient, *Recrit* is
  the critical Reynolds number, and *ν* is the kinematic
  viscosity. In this parameterization,
  *Cd* and
  *Recrit* are fixed at
  `0.64` and `150`, respectively.

When the block operates in the limits of the tabulated data,

K=tablelookup(ΔpTLU,KTLU,Δp,interpolation=linear,extrapolation=nearest),

where:

- *ΔpTLU* is the
  **Pressure drop vector** parameter.
- KTLU=V˙TLUΔpTLU, where *V˙TLU* is the
  **Volumetric flow rate vector** parameter.

When the simulation pressure falls below the first element of the **Pressure drop
vector** parameter,
*K*`=`*KLeak* ,

KLeak=V˙TLU(1)|ΔpTLU(1)|,

where *V˙TLU(1)* is the first element
of the **Volumetric flow rate vector** parameter.

When the simulation pressure rises above the last element of the **Pressure drop
vector** parameter,
*K*`=`*KMax*,

KMax=V˙TLU(end)|ΔpTLU(end)|,

where *V˙TLU(end)* is the last
element of the **Volumetric flow rate vector** parameter.

### Opening Dynamics

The linear parameterization supports valve opening and closing dynamics. If
opening dynamics are modeled, a lag is introduced to the flow response to the
modeled control pressure. *p*control becomes
the dynamic control pressure, *p*dyn;
otherwise, *p*control is the steady-state
pressure. The instantaneous change in dynamic control pressure is calculated based
on the **Opening time constant**, *τ*:

p˙dyn=pcontrol−pdynτ.

By default, the block clears the **Opening
dynamics** check box.

### Faults

To model a fault, in the **Faults** section,
click the **Add fault** hyperlink next to the fault that you want to model. Use
the fault parameters to specify the fault properties. For more information about fault modeling,
see Introduction to Simscape Faults.

The **Opening area when faulted** parameter has three options:

- `Closed`
- `Open`
- `Maintain at last value`

After the fault triggers, the valve remains at the faulted area for
the rest of the simulation.

**Faulting in the Linear Parameterization**

In the linear parameterization, the fault options are defined by the valve area:

- `Closed` — The valve area freezes
  at the **Leakage area**.
- `Open` — The valve area freezes at
  the **Maximum opening area**.
- `Maintain at last value` — The
  valve freezes at the open area when the trigger occurs.

**Faulting in the Tabulated Data Parameterization**

In the tabulated parameterization, the fault options are defined by the mass
flow rate through the valve:

- `Closed` — The valve freezes at the mass flow rate
  associated with the first elements of the **Volumetric flow
  rate vector** and the **Pressure drop
  vector**

  m˙=KLeakρ¯Δp.
- `Open` — The valve freezes at the mass flow rate
  associated with the last elements of the **Volumetric flow
  rate vector** and the **Pressure drop
  vector**

  m˙=KMaxρ¯Δp
- `Maintain at last value` — The valve freezes at the
  mass flow rate and pressure differential when the trigger occurs

  m˙=KLastρ¯Δp,

where

KLast=|m˙|ρ¯|Δp|.

### Generate Digital Data Sheet

*Since R2025a*

Generate a digital data sheet that includes performance data and pressure drop vs.
volumetric flow rate curves for the Check Valve
(IL) block by using the **Generate
datasheet** hyperlink in the **Description** tab of
the block dialog box. The datasheet script imports the parameters from the
Check Valve (IL) block that you select in the
model. You can use the characteristic curves to help evaluate the cracking pressure
and the leakage flow for the selected Check Valve
(IL) block. To open the live script:

1. Double-click the block to open the Block Parameters dialog box.
2. Open the **Description** tab.
3. Click the **Generate datasheet** hyperlink.
4. Click a Check Valve (IL) block in the
   model.
5. To generate the data sheet, in the live script, click the
   **Generate datasheet** button.

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
