---
type: simulink-block
title: 'Pressure Relief Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid Library / Valves and Orifices / Pressure Control Valves'
documentation_page: 'pressurereliefvalvetl'
documentation_source_path: 'ref/pressurereliefvalvetl.html'
language: en
---

# Pressure Relief Valve (TL)

## Ports

### Input

### **Ps** — Set pressure signal, Pa physical signal

Set pressure differential for controlled valve operation, in Pa.

#### Dependencies

To enable this port, set **Set pressure control**
to `Controlled`.
### Conserving

### **A** — Liquid port thermal liquid

Thermal liquid conserving port associated with valve inlet A.

### **B** — Liquid port thermal liquid

Thermal liquid conserving port associated with valve inlet B.

## Parameters

### Parameters

### **Set pressure control** — Valve operation method `Constant` (default) | `Controlled`

Valve operation method. A `Constant` valve
opens linearly over a fixed pressure regulation range or in accordance
with tabulated pressure and opening area data that you provide. A
`Controlled` valve opens according to a
variable set pressure signal at port **Ps** over a
fixed pressure regulation range.

#### Dependencies

To enable this parameter, set **Set pressure
control** to
`Constant`.

### **Opening parameterization** — Method of modeling constant valve opening or closing `Linear - Area vs. pressure` (default) | `Tabulated data - Area vs. pressure` | `Tabulated data - Volumetric flow rate vs. pressure`

Method of modeling the valve opening or closing. You can parameterize
the valve opening linearly or by using a table of values that correlate
the area-to-pressure differential.

#### Dependencies

To enable this parameter, set **Set pressure
control** to
`Constant`.

### **Pressure control specification** — Method to evaluate pressure `Pressure at port A` (default) | `Pressure differential`

Specification method for the valve control pressure. When you set this
parameter to `Pressure at port A`, the block
uses only the pressure at port **A** to determine when
the flow exceeds the value of the **Set pressure
(gauge)** parameter. When you set this parameter
`Pressure differential`, the block uses the
value of the **Set pressure differential** parameter to
determine whether the pressure differential from port
**A** to port **B** exceeds the
range.

#### Dependencies

To enable this parameter, set **Set pressure
control** to `Constant` and
**Opening parameterization** to
`Linear - Area vs. pressure` or
`Tabulated data - Area vs.
pressure`.

### **Set pressure (gauge)** — Gauge pressure when opening mechanism triggers `0.1` `MPa` (default) | positive scalar

Pressure at which the opening mechanism triggers. The opening area
remains variable throughout the pressure regulation range of the
valve.

#### Dependencies

To enable this parameter, set **Set pressure
control** to `Constant` and
either:

- **Pressure control specification** to
  `Pressure at port A` and
  **Opening parameterization** to
  `Linear - Area vs.
  pressure`.
- **Opening parameterization** to
  `Tabulated data - Volumetric flow rate
  vs. pressure`.

### **Set pressure differential** — Minimum opening pressure differential `0` `MPa` (default) | nonnegative scalar

Minimum pressure differential between ports **A** and
**B** required to open the valve. A pressure
differential above this value causes the valve to gradually open until
it reaches the fully open state.

#### Dependencies

To enable this parameter, set **Set pressure
control** to `Constant`,
**Pressure control specification** to
`Pressure differential`, and
**Opening parameterization** to
`Linear - Area vs. pressure`.

### **Pressure regulation range** — Valve pressure range `0.15` `MPa` (default) | positive scalar

Valve operational range. The valve begins to open at the set pressure
value, and is fully open at
*pmax*, the end of the
pressure regulation range, where *pmax =
pset +
prange*.

#### Dependencies

To enable this parameter, set either:

- **Set pressure control** to
  `Controlled`.
- **Set pressure control** to
  `Constant` and
  **Opening parameterization** to
  `Linear - Area vs.
  pressure`.

### **Maximum opening area** — Opening area in fully open position `1e-4` `m^2` (default) | positive scalar

Opening area of the valve in the fully open position due to sealing
imperfections, when the valve is at the upper limit of the pressure
regulation range.

#### Dependencies

To enable this parameter, set either:

- **Set pressure control** to
  `Controlled`.
- **Set pressure control** to
  `Constant` and
  **Opening parameterization** to
  `Linear - Area vs.
  pressure`.

### **Leakage area** — Gap area when in fully shut position `1e-10` `m^2` (default) | positive scalar

Sum of all gaps when the valve is in the fully shut position. The
block saturates smaller numbers to this value. This parameter
contributes to numerical stability by maintaining continuity in the
flow.

#### Dependencies

To enable this parameter, set either:

- **Set pressure control** to
  `Controlled`.
- **Set pressure control** to
  `Constant` and
  **Opening parameterization** to
  `Linear - Area vs.
  pressure`.

### **Pressure differential vector** — Differential pressure values for tabular parameterization `[0.2 : 0.2 : 1.2]` MPa (default) | 1-by-*n* vector

Vector of pressure differential values for the tabular
parameterization of the valve opening area. The vector elements must
correspond one-to-one with the elements in the **Opening area
vector** parameter. The elements must be listed in
ascending order and must be greater than 0. The block employs linear
interpolation between table data points.

The first element of this parameter is the pressure setting of the
valve, at which the valve begins to open. The last element is the
maximum pressure, at which the valve is fully open. The difference
between the two is the pressure regulation range of the valve.

#### Dependencies

To enable this parameter, set **Set pressure
control** to `Constant` and
either:

- **Opening parameterization** to
  `Tabulated data - Volumetric flow rate
  vs. pressure`.
- **Opening parameterization** to
  `Tabulated data - Area vs.
  pressure` and **Pressure
  control specification** to
  `Pressure
  differential`.

### **Opening pressure (gauge) vector** — Differential pressure values for tabular area parameterization `[0.2 : 0.2 : 1.2]` MPa (default) | 1-by-*n* vector

Vector of pressure differential values for the tabular area
parameterization of the valve opening area. The vector elements must
correspond one-to-one with the elements in the **Opening area
vector** parameter. The elements are must be in ascending
order and must be greater than 0. The block employs linear interpolation
between table data points.

The first element of this parameter is the pressure setting of the
valve, at which the valve begins to open. The last element is the
maximum pressure, at which the valve is fully open. The difference
between the two is the pressure regulation range of the valve.

#### Dependencies

To enable this parameter, set **Set pressure
control** to `Constant`,
**Opening parameterization** to
`Tabulated data - Area vs. pressure`,
and **Pressure control specification** to
`Pressure at port A`.

### **Opening area vector** — Valve opening areas for tabular area parameterization `[1e-10, 2e-06, 4e-06, 6e-06, 8e-06, 1e-05]`m^2 (default) | 1-by-*n* vector

Vector of valve opening areas for the tabular area parameterization of
the valve opening area. The vector elements must correspond one-to-one
with the elements in the **Pressure differential
vector** parameter. The elements must be in ascending order
and must be greater than 0. The block employs linear interpolation
between table data points.

#### Dependencies

To enable this parameter, set **Set pressure
control** to `Constant` and
**Opening parameterization** to
`Tabulated data - Area vs.
pressure`.

### **Volumetric flow rate vector** — Vector of volumetric flow rate for tabulated data parameterization `[1e-09, 3.6e-05, 8.9e-05, .00015, .00023, .00031]`m^3/s (default) | 1-by-*n* vector

Vector of volumetric flow rate values for the tabular parameterization
of the valve opening. This vector must have the same number of elements
as the **Pressure drop vector** parameter. The vector
elements must be in ascending order.

#### Dependencies

To enable this parameter, set **Set pressure
control** to `Constant` and
**Opening parameterization** to
`Tabulated data - Volumetric flow rate vs.
pressure`.

### **Cross-sectional area at ports A and B** — Area at conserving ports `0.01` `m^2` (default) | positive scalar

Area at ports **A** and **B**, which
the block uses in the pressure-flow rate equation that determines the
mass flow rate through the valve.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor that the block uses to account for discharge losses
in theoretical flows.

#### Dependencies

To enable this parameter, set either:

- **Set pressure control** to
  `Controlled`.
- **Set pressure control** to
  `Constant` and
  **Opening parameterization** to
  `Linear - Area vs.
  pressure` or `Tabulated
  data - Area vs. pressure`.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the valve.

#### Dependencies

To enable this parameter, set either:

- **Set pressure control** to
  `Controlled`.
- **Set pressure control** to
  `Constant` and
  **Opening parameterization** to
  `Linear - Area vs.
  pressure` or `Tabulated
  data - Area vs. pressure`.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change
to the flow response when the valve is in near-open or near-closed
positions. Set this value to a nonzero value less than one to increase
the stability of your simulation in these regimes.

A smoothing factor of 0 corresponds to a linear function that is
discontinuous at the set and maximum-area pressures. A smoothing factor
of 1 corresponds to a nonlinear function that changes continuously
throughout the entire function domain.

A smoothing factor between 0 and 1 corresponds to a continuous
function with smooth nonlinear transitions at the set and maximum-area
pressures.

#### Dependencies

To enable this parameter, set either:

- **Set pressure control** to
  `Controlled`.
- **Set pressure control** to
  `Constant` and
  **Opening parameterization** to
  `Linear - Area vs.
  pressure`.

### **Pressure recovery** — Whether to account for pressure increase in area expansions `off` (default) | `on`

Whether to account for pressure increase when fluid flows from a
region of smaller cross-sectional area to a region of larger
cross-sectional area. To capture the increase in pressure, select this
parameter.

#### Dependencies

To enable this parameter, set either:

- **Set pressure control** to
  `Controlled`.
- **Set pressure control** to
  `Constant` and
  **Opening parameterization** to
  `Linear - Area vs.
  pressure` or `Tabulated
  data - Area vs. pressure`.

### **Opening dynamics** — Whether to account for flow response to valve opening `off` (default) | `on`

Whether to account for transient effects to the fluid system due to
the valve opening. Selecting this parameter approximates the opening
conditions by introducing a first-order lag in the flow response.

### **Opening time constant** — Valve opening time constant `0.1` s (default) | positive scalar

Time constant by which to compute the lag in the opening
dynamics.

#### Dependencies

To enable this parameter, select **Opening
dynamics**.

### Faults

### **Pressure Relief Valve Area fault** — Option to model opening area fault `Add fault`

Option to model a valve area fault in the block. To add a fault, click
the **Add fault** hyperlink. When a fault occurs, the
valve area normally set by the opening parameterization is set based on
the value specified in the **Opening area when
faulted** parameter.

### **Opening area when faulted** — Faulted valve characteristics `Closed` (default) | `Open` | `Maintain last value`

Faulted valve type. You can choose for the valve to seize when the
valve is opened, closed, or at the area when the fault triggers.

#### Dependencies

To enable this parameter, click the **Add
fault** hyperlink.

## Libraries

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Pressure Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

### R2024b: Model faults with the Simscape faults interface

The Pressure Relief Valve (TL) block now supports the Simscape faults interface. To learn more,
see Introduction to Simscape Faults.

### R2024b: Model a controlled pressure relief valve

Set **Set pressure control** to
`Controlled` to control the block set pressure with the
signal at port **Ps**.

### R2023a: New Parameterization Options

Use the **Opening parameterization** parameter to choose the
block parameterization `Linear - Area vs. pressure`,
`Tabulated data - Area vs. pressure`, or
`Tabulated data - Volumetric flow rate vs.
pressure`.

## Description

Pressure relief valve in a thermal liquid network

The Pressure Relief Valve (TL) block represents a valve
that relieves excess pressure in a thermal liquid network. The valve remains closed when
the pressure is less than a specified value. When this pressure is met or surpassed, the
valve opens. This set pressure is either a threshold pressure differential over the
valve, between ports **A** and **B**, or between port
**A** and atmospheric pressure. A control pressure above the set
pressure causes the valve to gradually open, which allows the fluid network to relieve
excess pressure.

### Pressure Control

The normalized pressure, p^, controls the valve opening area when **Opening
parameterization** is `Linear - Area vs.
pressure`. The normalized pressure is

p^=pcontrol-psetpmax-pset,

where:

- *pcontrol* is the control
  pressure, which depends on the value of the **Pressure control
  specification** parameter.

  When you set **Pressure control specification** to
  `Pressure differential`, the control pressure
  is *pA ̶ pB*.

  When you set **Pressure control specification** to
  `Pressure at port A`, the control pressure is
  the difference between the pressure at port **A** and
  atmospheric pressure.
- *pset* is the set pressure, which
  depends on the value of the **Pressure control
  specification** parameter.

  When you set **Pressure control specification** to
  `Pressure differential`,
  *pset* is the value of the
  **Set pressure differential** parameter.

  When you set **Set pressure specification** to
  `Pressure at port A`,
  *pset* is the value of the
  **Set pressure (gauge)** parameter.
- *pmax* is the maximum pressure,
  *pmax = pset +
  prange*, where
  *prange* is the value of the
  **Pressure regulation range** parameter.

### Opening Parameterization

The mass flow rate depends on the value of the **Opening
parameterization** parameter.

**Area vs. Pressure Parameterizations**

When you set **Set pressure control** to
`Constant` and **Opening
parameterization** to `Linear - Area vs.
pressure` or `Tabulated data - Area vs.
pressure`, the mass flow rate is

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

where:

- *Cd* is the value of the
  **Discharge coefficient** parameter.
- *Avalve* is the
  instantaneous valve open area.
- *Aport* is the value of
  the **Cross-sectional area at ports A and B**
  parameter.
- ρ¯ is the average fluid density.
- *Δp* is the valve pressure difference
  *pA* –
  *pB*.

The critical pressure difference,
*Δpcrit*, is the pressure
differential associated with the **Critical Reynolds number**,
*Recrit*, the flow regime
transition point between laminar and turbulent flow:

Δpcrit=π8Avalveρ¯(μRecritCd)2,

where *μ* is the dynamic viscosity of the thermal
liquid.

The pressure loss, *PRloss*, describes
the reduction of pressure in the valve due to a decrease in area. The block
calculates *PRloss* as

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport.

The pressure recovery describes the positive pressure change in the valve due
to an increase in area. When you clear the **Pressure
recovery** check box, the block sets
*PRloss* to 1.

When you set **Opening parameterization** to
`Linear - Area vs. pressure`, the block calculates
the opening area as

Avalve=p^(Amax−Aleak)+Aleak,

where *Aleak* is the
value of the **Leakage Area** parameter and
*Amax* is the value of the
**Maximum opening area** parameter.

This figure shows how the block controls the opening area using the linear
parameterization.

Pressure differential between ports X and Y with respect to opening area for a normally closed valve using the linear parameterization

When the valve is in a near-open or
near-closed position in the linear parameterization, you can maintain numerical
robustness in your simulation by adjusting the **Smoothing
factor** parameter. If the **Smoothing factor**
parameter is nonzero, the block smoothly saturates the control pressure between
*pset* and
*pmax*. For more information,
see Numerical Smoothing.

When you set **Opening parameterization** to
`Tabulated data - Area vs. pressure`, the block
calculates the opening area as

Avalve=tablelookup(pcontrol,TLU,ref,ATLU,pcontrol,interpolation=linear,extrapolation=nearest),

where:

- *pcontrol,TLU,ref*
  = *pTLU* +
  *poffset*.
- *pTLU* is the
  **Pressure differential vector** or
  **Opening pressure (gauge) vector** parameter,
  depending on the value of the **Pressure control
  specification** parameter.
- *poffset* is an internal
  pressure offset that causes the valve to start closing when
  *pcontrol,TLU,ref* =
  *pset*.
- *ATLU* is the
  **Opening area vector** parameter.

This figure shows how the block controls the opening area when
**Opening parameterization** is `Tabulated data
- Area vs. pressure`.

Pressure differential between ports X and Y with respect to opening area for a normally closed valve using the tabulated parameterization

**Volumetric Flow Rate vs. Pressure Parameterization**

When you set **Set pressure control** to
`Constant` and **Opening
parameterization** to `Tabulated data - Volumetric flow
rate vs. pressure`, the valve opens according to the
user-provided tabulated data of volumetric flow rate and pressure differential
between ports **A** and **B**.

The block calculates the mass flow rate as

m˙=ρ¯V˙,

where:

- V˙ is the volumetric flow rate.
- ρ¯ is the average fluid density.

The block calculates the relationship between the mass flow and pressure
using

m˙=Kρ¯Δp,

where

K=V˙|Δp|.

**Controlled Pressure Regulation**

When you set **Set pressure control** to
`Controlled`, the control pressure is the pressure
differential between ports **A** and **B** and
there is no option to use a gauge pressure. The normalized pressure is

p^=pcontrol-pspmax-ps,

where:

- *ps* is the value of the
  signal at port **Ps**.
- *pmax = ps +
  prange*, where
  *prange* is the
  value of the **Pressure regulation range**
  parameter.
- *pcontrol* is the pressure
  differential between ports **A** and
  **B**, *pA ̶
  pB*.

### Opening Dynamics

When you set **Opening dynamics** to
`On`, the block introduces a control pressure lag and
replaces *pcontrol* with the dynamic control
pressure, *pdyn*. The block calculates the
dynamic control pressure based on the **Opening time constant**
parameter, *τ*

p˙dyn=pcontrol−pdynτ.

By default, the block clears the **Opening
dynamics** check box.

### Energy Balance

The energy conservation equation in the valve is

ϕA+ϕB=0,

where:

- *ϕ*A is the energy flow rate
  into the valve through port **A**.
- *ϕ*B is the energy flow rate
  into the valve through port **B**.

### Faults

To model a fault, in the **Faults** section,
click the **Add fault** hyperlink next to the fault that you want to model. Use
the fault parameters to specify the fault properties. For more information about fault modeling,
see Introduction to Simscape Faults.

The **Opening area when faulted** parameter has three fault options:

- `Closed` — The valve freezes at its smallest value:

  - When you set **Set pressure control** to
    `Constant` and
    **Opening parameterization** to
    `Linear - Area vs. pressure`,
    the valve area freezes at the **Leakage
    area** parameter.
  - When you set **Set pressure control** to
    `Constant` and
    **Opening parameterization** to
    `Tabulated data - Area vs.
    pressure`, the valve area freezes at the
    first element of the **Opening area
    vector** parameter.
  - When you set **Set pressure control** to
    `Controlled` the valve area
    freezes at the **Leakage area**
    parameter.
- `Open` — The valve freezes at its largest value:

  - When you set **Set pressure control** to
    `Constant` and
    **Opening parameterization** to
    `Linear - Area vs. pressure`,
    the valve area freezes at the **Maximum opening
    area** parameter.
  - When you set **Set pressure control** to
    `Constant` and
    **Orifice parameterization** to
    `Tabulated data - Area vs.
    pressure`, the valve area freezes at the
    last element of the **Opening area vector**
    parameter.
  - When you set **Set pressure control** to
    `Controlled` the valve area
    freezes at the **Maximum opening area**
    parameter.
- `Maintain last value` — The valve area
  freezes at the valve open area when the trigger occurred.

Due to numerical smoothing at the extremes of the valve area, the
minimum area the block uses is larger than the **Leakage area**
parameter, and the maximum is smaller than the **Maximum orifice
area** parameter, in proportion to the **Smoothing
factor** parameter value.

After the fault triggers, the valve remains at the faulted area for the rest of
the simulation.

When you set **Opening parameterization** to
`Tabulated data - Volumetric flow rate vs. pressure`,
the fault options are defined by the volumetric flow rate through the valve:

- `Closed` — The valve stops at the mass flow
  rate associated with the first elements of the **Volumetric flow
  rate vector** parameter and the **Pressure drop
  vector** parameter:

  m˙=KLeakρ¯Δp.
- `Open` — The valve stops at the mass flow
  rate associated with the last elements of the **Volumetric flow
  rate vector** parameter and the **Pressure drop
  vector** parameter:

  m˙=KMaxρ¯Δp
- `Maintain at last value` — The valve stops at
  the mass flow rate and pressure differential when the trigger occurs:

  m˙=KLastρ¯Δp,

where

KLast=|m˙|ρ¯|Δp|.

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
