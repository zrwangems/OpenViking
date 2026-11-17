---
type: simulink-block
title: 'Pressure Relief Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Pressure Control Valves'
documentation_page: 'pressurereliefvalveil'
documentation_source_path: 'ref/pressurereliefvalveil.html'
language: en
---

# Pressure Relief Valve (IL)

## Ports
```yaml
ports:
- name: A
  summary: Liquid port isothermal liquid
  direction: conserving
- name: B
  summary: Liquid port isothermal liquid
  direction: conserving
- name: Ps
  summary: Set pressure signal physical signal
  direction: input
```

### Conserving

### **A** — Liquid port isothermal liquid

Entry or exit point to the valve.

### **B** — Liquid port isothermal liquid

Entry or exit point to the valve.
### Input

### **Ps** — Set pressure signal physical signal

Varying-signal set pressure for controlled valve operation.

#### Dependencies

To enable this
port, set **Set pressure control** to
`Controlled`.
## Parameters
```yaml
parameters:
- name: Set pressure control
  summary: Valve operation method Constant (default) | Controlled
  group: Parameters
- name: Opening parameterization
  summary: Method of modeling constant valve opening or closing Linear - Area vs. pressure (default) | Tabulated data - Area
    vs. pressure | Tabulated data - Volumetric flow rate vs. pressure
  group: Parameters
- name: Opening pressure specification
  summary: Pressure differential used for valve control Pressure differential (default) | Pressure at port A
  group: Parameters
- name: Set pressure (gauge)
  summary: Threshold pressure 0.1 MPa (default) | positive scalar
  group: Parameters
- name: Set pressure differential
  summary: Threshold pressure 0 MPa (default) | positive scalar
  group: Parameters
- name: Pressure regulation range
  summary: Valve operational pressure range 0.1 MPa (default) | positive scalar
  group: Parameters
- name: Maximum opening area
  summary: Area of fully opened valve 1e-4 m^2 (default) | positive scalar
  group: Parameters
- name: Leakage area
  summary: Valve gap area when in fully closed position 1e-10 m^2 (default) | positive scalar
  group: Parameters
- name: Opening pressure (gauge) vector
  summary: 'Differential pressure values for tabular parameterization [0.2 : 0.2 : 1.2] MPa (default) | 1-by-*n* vector'
  group: Parameters
- name: Pressure differential vector
  summary: 'Differential pressure values for tabular parameterization [0.2 : 0.2 : 1.2] MPa (default) | 1-by-*n* vector'
  group: Parameters
- name: Volumetric flow rate vector
  summary: Vector of volumetric flow rate for tabulated data parameterization [1e-09, 3.6e-05, 8.9e-05, .00015, .00023, .00031]
    (default) | 1-by-*n* vector
  group: Parameters
- name: Opening area vector
  summary: Valve opening areas for tabular parameterization [1e-10, 2e-06, 4e-06, 6e-06, 8e-06, 1e-05]m^2 (default) | 1-by-*n*
    vector
  group: Parameters
- name: Cross-sectional area at ports A and B
  summary: Area at valve entry or exit inf m^2 (default) | positive scalar
  group: Parameters
- name: Discharge coefficient
  summary: Discharge coefficient 0.64 (default) | positive scalar
  group: Parameters
- name: Critical Reynolds number
  summary: Upper Reynolds number limit for laminar flow 150 (default) | positive scalar
  group: Parameters
- name: Smoothing factor
  summary: Numerical smoothing factor 0.01 (default) | positive scalar
  group: Parameters
- name: Pressure recovery
  summary: Whether to account for pressure increase in area expansions off (default) | on
  group: Parameters
- name: Opening dynamics
  summary: Whether to account for flow response to valve opening off (default) | on
  group: Parameters
- name: Opening time constant
  summary: Valve opening time constant 0.1 s (default) | positive scalar
  group: Parameters
- name: Pressure Relief Valve Area fault
  summary: Option to model opening area fault Add fault
  group: Faults
- name: Opening area when faulted
  summary: Faulted valve characteristics Closed (default) | Open | Maintain last value
  group: Faults
```

### Parameters

### **Set pressure control** — Valve operation method `Constant` (default) | `Controlled`

Valve operation method. A `Constant` valve
opens linearly over a fixed pressure regulation range or in accordance
with tabulated pressure and opening area data that you provide. A
`Controlled` valve opens according to a
variable set pressure signal at port **Ps** over a
fixed pressure regulation range.

### **Opening parameterization** — Method of modeling constant valve opening or closing `Linear - Area vs. pressure` (default) | `Tabulated data - Area vs. pressure` | `Tabulated data - Volumetric flow rate vs. pressure`

Method of modeling valve opening or closing. The valve opening is
either parametrized linearly or by a table of values that correlate area
to pressure differential.

### **Opening pressure specification** — Pressure differential used for valve control `Pressure differential` (default) | `Pressure at port A`

Pressure differential used for the valve control. Selecting
`Pressure differential` sets the pressure
difference between port **A** and port
**B** as the trigger for pressure control.
Selecting `Pressure at port A` sets the gauge
pressure at port **A**, or the difference between the
pressure at port **A** and atmospheric pressure, as the
trigger for pressure control.

### **Set pressure (gauge)** — Threshold pressure `0.1` MPa (default) | positive scalar

Gauge pressure beyond which valve operation is triggered when the
**Pressure control specification** is with respect
to port **A**.

#### Dependencies

To enable this parameter, set **Set pressure
control** to `Constant` and
**Pressure control specification** to
`Pressure at port A`.

### **Set pressure differential** — Threshold pressure `0` MPa (default) | positive scalar

Pressure beyond which valve operation is triggered. This is the set
pressure when the **Pressure control specification** is
with respect to the pressure differential between ports
**A** and **B**.

#### Dependencies

To enable this parameter, set **Set pressure
control** to `Constant` and
**Pressure control specification** to
`Pressure differential`.

### **Pressure regulation range** — Valve operational pressure range `0.1 MPa` (default) | positive scalar

Valve operational range. The valve begins to open at the set pressure
value, and is fully open at
*pmax*, the end of the
pressure regulation range, where *pmax =
pset +
prange*.

#### Dependencies

To enable this parameter, set

- **Set pressure control** to
  `Controlled`
- **Set pressure control** to
  `Constant` and
  **Opening parameterization** to
  `Linear - Area vs.
  pressure`

### **Maximum opening area** — Area of fully opened valve `1e-4` m^2 (default) | positive scalar

Cross-sectional area of the valve in its fully open position.

#### Dependencies

To enable this parameter, set either:

- **Set pressure control** to
  `Controlled`
- **Set pressure control** to
  `Constant` and
  **Opening parameterization** to
  `Linear - Area vs.
  pressure`

### **Leakage area** — Valve gap area when in fully closed position `1e-10` m^2 (default) | positive scalar

Sum of all gaps when the valve is in fully closed position. Any area
smaller than this value is maintained at the specified leakage area.
This contributes to numerical stability by maintaining continuity in the
flow.

#### Dependencies

To enable this parameter, set either:

- **Set pressure control** to
  `Controlled`.
- **Set pressure control** to
  `Constant` and
  **Opening parameterization** to
  `Linear - Area vs.
  pressure`

### **Opening pressure (gauge) vector** — Differential pressure values for tabular parameterization `[0.2 : 0.2 : 1.2]` MPa (default) | 1-by-*n* vector

Vector of pressure differential values for the tabular
parameterization of the valve opening area. The vector elements must
correspond one-to-one with the elements in the **Opening area
vector** parameter. The elements are listed in ascending
order and must be greater than 0. Linear interpolation is employed
between table data points.

The first element of this parameter is the pressure setting of the
valve, at which the valve begins to open. The last element is the
maximum pressure, at which the valve is fully open. The difference
between the two is the pressure regulation range of the valve.

#### Dependencies

To enable this parameter, set **Set pressure control** to
`Constant`, **Opening
parameterization** to `Tabulated data -
Area vs. pressure`, and **Opening pressure
specification** to `Pressure
differential`.

### **Pressure differential vector** — Differential pressure values for tabular parameterization `[0.2 : 0.2 : 1.2]` MPa (default) | 1-by-*n* vector

Vector of pressure differential values for the tabular
parameterization of the valve opening area. The vector elements must
correspond one-to-one with the elements in the **Opening area
vector** parameter. The elements are listed in ascending
order and must be greater than 0. Linear interpolation is employed
between table data points.

The first element of this parameter is the pressure setting of the
valve, at which the valve begins to open. The last element is the
maximum pressure, at which the valve is fully open. The difference
between the two is the pressure regulation range of the valve.

#### Dependencies

To enable this parameter, set **Set pressure
control** to `Constant`, and set

- **Opening parameterization** to
  `Tabulated data - Volumetric flow rate
  vs. pressure`, or
- **Opening parameterization** to
  `Tabulated data - Area vs.
  pressure` and **Opening
  pressure specification** to
  `Pressure
  differential`.

### **Volumetric flow rate vector** — Vector of volumetric flow rate for tabulated data parameterization `[1e-09, 3.6e-05, 8.9e-05, .00015, .00023, .00031]` (default) | 1-by-*n* vector

Vector of volumetric flow rate values for the tabular parameterization
of valve opening. This vector must have the same number of elements as
the **Pressure drop vector** parameter. The vector
elements must be listed in ascending order.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Tabulated data -
Volumetric flow rate vs. pressure`.

### **Opening area vector** — Valve opening areas for tabular parameterization `[1e-10, 2e-06, 4e-06, 6e-06, 8e-06, 1e-05]`m^2 (default) | 1-by-*n* vector

Vector of valve opening areas for the tabular parameterization of the
valve opening area. The vector elements must correspond one-to-one with
the elements in the **Pressure differential vector**
parameter. The elements are listed in ascending order and must be
greater than 0. Linear interpolation is employed between table data
points.

#### Dependencies

To enable this parameter, set **Set pressure control** to
`Constant` and **Opening
parameterization** to `Tabulated data -
Area vs. pressure`.

### **Cross-sectional area at ports A and B** — Area at valve entry or exit `inf` m^2 (default) | positive scalar

Cross-sectional area at the entry and exit ports
**A** and **B**. These areas are
used in the pressure-flow rate equation determining mass flow rate
through the valve.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor accounting for discharge losses in theoretical
flows. The default discharge coefficient for a valve in Simscape™
Fluids™ is 0.64.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the valve.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar

Continuous smoothing factor that introduces a layer of gradual change
to the flow response when the valve is in near-open or near-closed
positions. Set this value to a nonzero value less than one to increase
the stability of your simulation in these regimes.

#### Dependencies

To enable this parameter, set **Opening parameterization** to
`Linear - Area vs. pressure`.

### **Pressure recovery** — Whether to account for pressure increase in area expansions `off` (default) | `on`

Accounts for pressure increase when fluid flows from a region of smaller cross-sectional
area to a region of larger cross-sectional area. This increase in
pressure is not captured when you clear the **Pressure
recovery** check box.

### **Opening dynamics** — Whether to account for flow response to valve opening `off` (default) | `on`

Whether to account for transient effects to the fluid system due to valve opening.
Selecting **Opening dynamics** approximates the opening
conditions by introducing a first-order lag in the flow response. The
**Opening time constant** also impacts the modeled
opening dynamics.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure` or `Tabulated data - Area vs.
pressure`.

### **Opening time constant** — Valve opening time constant `0.1` s (default) | positive scalar

Constant that captures the time required for the fluid to reach
steady-state when opening or closing the valve from one position to
another. This parameter impacts the modeled opening dynamics.

#### Dependencies

To enable this parameter, set **Opening parameterization** to
`Linear - Area vs. pressure` or
`Tabulated data - Area vs. pressure`
and select **Opening dynamics**.

### Faults

### **Pressure Relief Valve Area fault** — Option to model opening area fault `Add fault`

Option to model a valve area fault in the block. To add a fault, click the **Add
fault** hyperlink. When a fault occurs, the valve area
normally set by the opening parameterization is set based on the value
specified in the **Opening area when faulted**
parameter.

### **Opening area when faulted** — Faulted valve characteristics `Closed` (default) | `Open` | `Maintain last value`

Faulted valve type. You can choose for the valve to seize when the
valve is opened, closed, or at the area when the fault triggers.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink.
## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Pressure Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

### R2024a: Model faults with the Simscape faults interface

The Pressure Relief Valve (IL) block now supports the Simscape faults interface. To learn more, see Introduction to Simscape Faults.

### R2022b: Access pre-parameterized block options

The block supports pre-parameterization options. Suppliers include Daikin,
Kawasaki Heavy Industries, Parker, and Yuken.

## Description

Pressure-relief valve in an isothermal liquid network

The Pressure Relief Valve (IL) block represents a pressure
relief valve in an isothermal liquid network. The valve remains closed when the pressure
is less than a specified value. When this pressure is met or surpassed, the valve opens.
This set pressure is either a threshold pressure differential over the valve, between
ports **A** and **B**, or between port
**A** and atmospheric pressure. For pressure control based on
another element in the fluid system, see the Pressure Compensator
Valve (IL) block.

### Pressure Control

For linear preparameterizations, the normalized pressure, p^, which controls the valve opening area, depends on the value of
the **Set pressure control** parameter.

When you set **Set pressure control** to
`Constant` and **Opening
parameterization** to `Linear - Area vs.
pressure`, the normalized pressure is

p^=pcontrol-psetpmax-pset,

where:

- *pcontrol* is the control
  pressure. When you set **Opening pressure specification**
  to `Pressure differential`, the control pressure is
  *pA ̶
  pB*. When you set **Opening
  pressure specification** to `Pressure at port
  A`, the control pressure is the difference between the
  pressure at port **A** and atmospheric pressure.
- *pset* is the set pressure. When
  **Opening pressure specification** is
  `Pressure differential`,
  *pset* is the value of the
  **Set pressure differential** parameter. When
  **Opening pressure specification** is
  `Pressure at port A`,
  *pset* is the value of the
  **Set pressure (gauge)** parameter.
- *pmax* is the maximum of pressure
  regulation range, *pmax =
  pset +
  prange*, where
  *prange* is the value of the
  **Pressure regulation range** parameter.

When you set **Set pressure control** to
`Controlled`, the normalized pressure is

p^=pcontrol-pspmax-ps,

where:

- *ps* is the value of the
  signal at port **Ps**.
- *pmax = ps +
  prange*, where
  *prange* is the value of
  the **Pressure regulation range** parameter.
- *pcontrol* is the pressure
  differential between ports **A** and
  **B**, *pA ̶
  pB*.

### Opening Parameterization

The mass flow rate depends on the values of the **Set pressure
control** and **Opening parameterization**
parameters.

**Area vs. Pressure Parameterizations**

When you set **Set pressure control** to
`Controlled`, or to
`Constant` and **Opening
parameterization** to `Linear - Area vs.
pressure` or `Tabulated data - Area vs.
pressure`, the mass flow rate is

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

where:

- *Cd* is the value of the
  **Discharge coefficient**.
- *Avalve* is the
  instantaneous valve open area.
- *Aport* is the value of
  the **Cross-sectional area at ports A and
  B**.
- ρ¯ is the average fluid density.
- *Δp* is the valve pressure difference
  *pA* –
  *pB*.

The critical pressure difference,
*Δpcrit*, is the pressure
differential associated with the **Critical Reynolds number**,
*Recrit*, the flow regime
transition point between laminar and turbulent flow:

Δpcrit=πρ¯8Avalve(νRecritCd)2.

*Pressure loss* describes the reduction of pressure in the
valve due to a decrease in area.
*PR*loss is calculated as:

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport.

*Pressure recovery* is the positive pressure change in the valve due to
an increase in area. If you do not want to capture this increase in pressure,
clear the **Pressure recovery** check box. In this case,
*PR*loss is 1.

When you set **Set pressure control** to
`Controlled`, or to
`Constant` and **Opening
parameterization** to `Linear - Area vs.
pressure`, the opening area is

Avalve=p^(Amax−Aleak)+Aleak,

where:

- *Aleak* is the value of
  the **Leakage area** parameter.
- *Amax* is the value of the
  **Maximum opening area** parameter.

When the valve is in a near-open or
near-closed position in the linear parameterization, you can maintain numerical
robustness in your simulation by adjusting the **Smoothing
factor** parameter. If the **Smoothing factor**
parameter is nonzero, the block smoothly saturates the control pressure between
*pset* and
*pmax*. For more information,
see Numerical Smoothing.

When you set **Set pressure control** to
`Constant` and **Opening
parameterization** to `Tabulated data - Area vs.
pressure`, the block interpolates
*Avalve* from the
**Opening area vector** parameter with respect to the
**Pressure differential vector** or **Opening
pressure (gauge) vector** parameter, depending on the value of the
**Pressure control specification** parameter. The block
also uses the smoothed, normalized pressure when the smoothing factor is nonzero
with linear interpolation and nearest extrapolation.

**Volumetric Flow Rate vs. Pressure Parameterization**

When you set **Set pressure control** to
`Constant` and **Opening
parameterization** to `Tabulated data - Volumetric flow
rate vs. pressure`, the valve opens according to the
user-provided tabulated data of volumetric flow rate and pressure differential
between ports **A** and **B**.

The mass flow rate is

m˙=ρ¯KΔp(Δp2+Δpcrit2)1/4,

where:

- ρ¯ is the average fluid density.
- Δp=pA−pB.
- Δpcrit=π2ρ¯8CdK(Recritv)2, where *Cd* is
  the discharge coefficient,
  *Recrit* is the critical
  Reynolds number, and *ν* is the kinematic viscosity. In
  this parameterization, *Cd* and
  *Recrit* are fixed at
  `0.64` and `150`,
  respectively.

When the block operates in the limits of the tabulated data,

K=tablelookup(ΔpTLU,KTLU,Δp,interpolation=linear,extrapolation=nearest),

where:

- *ΔpTLU* is the
  **Pressure drop vector** parameter.
- KTLU=V˙TLUΔpTLU, where *V˙TLU* is the
  **Volumetric flow rate vector**
  parameter.

When the simulation pressure falls below the first element of the
**Pressure drop vector** parameter,
*K*`=`*KLeak*,

KLeak=V˙TLU(1)|ΔpTLU(1)|,

where *V˙TLU(1)* is the first
element of the **Volumetric flow rate vector**
parameter.

When the simulation pressure rises above the last element of the
**Pressure drop vector** parameter,
*K*`=`*KMax*,

KMax=V˙TLU(end)|ΔpTLU(end)|,

where *V˙TLU(end)* is the last
element of the **Volumetric flow rate vector**
parameter.

### Conservation of Mass

The block conserves mass through the valve such that

m˙A+m˙B=0.

where m˙ is the mass flow rate into the valve through the port indicated by
the **A** or **B**
subscript.

### Opening Dynamics

When you set **Opening dynamics** to `On`, the
block introduces a control pressure lag and replaces
*pcontrol* with the dynamic control
pressure, *pdyn*. The block calculates the
dynamic control pressure based on the **Opening time constant**
parameter, *τ*

p˙dyn=pcontrol−pdynτ.

By default, the block clears the **Opening
dynamics** check box.

Steady-state dynamics are set by the same parameterization as valve opening, and
are based on the control pressure,
*p*control. A nonzero
**Smoothing factor** can provide additional numerical stability
when the orifice is in near-closed or near-open position.

### Faults

To model a fault, in the **Faults** section,
click the **Add fault** hyperlink next to the fault that you want to model. Use
the fault parameters to specify the fault properties. For more information about fault modeling,
see Introduction to Simscape Faults.

The **Opening area when faulted** parameter has three fault options:

- `Closed` — The valve freezes at its smallest
  value, depending on the **Opening parameterization** parameter:

  - When you set **Opening parameterization**
    to `Linear - Area vs. pressure`,
    the valve area freezes at the **Leakage
    area** parameter.
  - When you set **Opening
    parameterization** to `Tabulated
    data - Area vs. pressure`, the valve area
    freezes at the first element of the **Opening area
    vector** parameter.
- `Open` — The valve freezes at its largest
  value, depending on the **Opening parameterization** parameter:

  - When you set **Opening parameterization**
    to `Linear - Area vs. pressure`,
    the valve area freezes at the **Maximum opening
    area** parameter.
  - When you set **Orifice
    parameterization** to `Tabulated
    data - Area vs. pressure`, the valve area
    freezes at the last element of the **Opening area
    vector** parameter.
- `Maintain last value` — The valve area
  freezes at the valve open area when the trigger occurred.

Due to numerical smoothing at the extremes of the valve area, the
minimum area the block uses is larger than the **Leakage area**
parameter, and the maximum is smaller than the **Maximum orifice
area** parameter, in proportion to the **Smoothing
factor** parameter value.

After the fault triggers, the valve remains at the faulted area for the rest of the
simulation.

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
