---
type: simulink-block
title: 'Pressure-Reducing 3-Way Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Pressure Control Valves'
documentation_page: 'pressurereducing3wayvalveil'
documentation_source_path: 'ref/pressurereducing3wayvalveil.html'
language: en
---

# Pressure-Reducing 3-Way Valve (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Liquid exit port of the valve.

### **P** — Liquid port isothermal liquid

Liquid entry port to the valve.

### **T** — Liquid port isothermal liquid

Liquid relief port of the valve.
### Input

### **Ps** — Controlled pressure differential physical signal

Varying-signal set pressure for controlled valve operation.

#### Dependencies

To enable this port, set **Set pressure control**
to `Controlled`.

## Parameters

### Parameters

### **Set pressure control** — Valve operation method `Constant` (default) | `Controlled`

Valve operation method. A `Constant` valve opens or closes
linearly over a fixed pressure regulation range and pressure transition
or in accordance with tabulated pressure and opening area data that you
provide. A `Controlled` valve opens or closes
according to a variable set pressure signal at port
**Ps** over a fixed pressure regulation and
pressure transition range. The selected setting applies both to the
reducing and relief valve operation.

### **Opening parameterization** — Type of opening parameterization `Linear` (default) | `Tabulated`

Method of modeling the valve opening or closing. Valve opening is
either parametrized linearly, which correlates the opening area to the
provided pressure range, or by a table of values you provide that
correlate the valve opening area to pressure differential data.

#### Dependencies

To enable this port, set **Set pressure control**
to `Constant`.

### **Set pressure differential for reducing valve** — Set pressure for valve closing at port P `0.6` MPa (default) | scalar

Pressure differential between port **T** and port
**A**. When this set pressure differential is
surpassed, the valve at port **P** begins to close. The
closing is parametrized linearly or by lookup table as defined in the
**Opening parameterization**.

### **Pressure regulation range** — Valve operational pressure range `3e-2` MPa (default) | scalar

Operational pressure range of the reducing valve. The pressure
regulation range lies between the **Set pressure
differential** and the maximum valve operating pressure. At
the end of the **Pressure regulation range**, the
pressure-reducing valve is closed and the **Pressure transition
range** begins.

#### Dependencies

To enable this parameter, set

- **Set pressure control** to
  `Controlled`, or
- **Set pressure control** to
  `Constant` and
  **Opening parameterization** to
  `Linear`.

### **Pressure transition range** — Pressure range of valve with ports P and T closed `2e-2` MPa (default) | scalar

Pressure range of the 3-way valve. This parameter defines the pressure
range, which begins at the end of the **Pressure regulation
range**, over which both ports **P** and
**T**  are closed. Below this range, the reducing
valve at port **P** is open to flow, and above this
range, the relief valve at port **T** opens.

#### Dependencies

To enable this parameter, set either:

- **Set pressure control** to
  `Controlled`
- **Set pressure control** to
  `Constant` and
  **Opening parameterization** to
  `Linear`

### **Maximum opening area** — Maximum opening area of ports `1e-4` m^2 (default) | positive scalar

Cross-sectional area of the valve
(**P**-**A** or
**A**-**T**) in its fully-open
position.

#### Dependencies

To enable this parameter, set either:

- **Set pressure control** to
  `Controlled`
- **Set pressure control** to
  `Constant` and
  **Opening parameterization** to
  `Linear`

### **Leakage area** — Gap area when in fully closed position `1e-10` m^2 (default) | positive scalar

Sum of all gaps when the valve is in fully closed position. Any area
smaller than this value is saturated to the specified leakage area. This
contributes to numerical stability by maintaining continuity in the
flow.

#### Dependencies

To enable this parameter, set either:

- **Set pressure control** to
  `Controlled`
- **Set pressure control** to
  `Constant` and
  **Opening parameterization** to
  `Linear`

### **Pressure differential vector for reducing valve** — Differential pressure values for tabular parameterization of reducing valve `0.6 : 0.02 : 0.7` MPa (default) | 1-by-*n* vector

Vector of pressure differential values for the tabular
parameterization of opening area. The vector elements correspond
one-to-one to the values in the **Opening area vector reducing
valve** parameter. Pressure differential vector values are
listed in ascending order and must have the same number of elements as
the **Opening area vector reducing valve** parameter.
Linear interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set **Set pressure control** to
`Constant` and **Opening
parameterization** to
`Tabulated`.

### **Opening area vector reducing valve** — Vector of valve opening areas for tabular parameterization of reducing valve `[1e-05, 8e-06, 6e-06, 4e-06, 2e-06, 1e-10]`m^2 (default) | 1-by-*n* vector

Vector of opening area values for the tabular parameterization of
opening area. The vector elements must correspond one-to-one to the
values in the **Pressure differential vector for reducing
valve** parameter. Areas are listed in descending order.
Linear interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set **Set pressure control** to
`Constant` and **Opening
parameterization** to
`Tabulated`.

### **Pressure differential vector for relief valve** — Differential pressure values for tabular parameterization of relief valve `0.68 : 0.02 : 0.78` MPa (default) | 1-by-*n* vector

Vector of pressure differential values for the tabular
parameterization of opening area. The vector elements correspond
one-to-one to the values in the **Opening area vector relief
valve** parameter. Pressure differential vector values are
listed in ascending order and must have the same number of elements as
the **Opening area vector relief valve** parameter.
Linear interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set **Set pressure control** to
`Constant` and **Opening
parameterization** to
`Tabulated`.

### **Opening area vector for relief valve** — Valve opening areas for tabular parameterization of relief valve `[1e-10, 2e-06, 4e-06, 6e-06, 8e-06, 1e-05]`m^2 (default) | 1-by-*n* vector

Vector of opening area values for the tabular parameterization of
opening area. The vector elements must correspond one-to-one to the
values in the **Pressure differential vector for relief
valve** parameter. Areas are listed in ascending order.
Linear interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set **Set pressure control** to
`Constant` and **Opening
parameterization** to
`Tabulated`.

### **Cross-sectional area at ports A, P & T.** — Orifice area at conserving ports `inf` m^2 (default) | positive scalar

Cross-sectional area at the entry and exit ports
**A**, **P**, and
**T**. This area is used in the pressure-flow rate
equation that determines the mass flow rate through the orifice.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor accounting for discharge losses in theoretical
flows. The default discharge coefficient for a valve in Simscape™
Fluids™ is 0.64.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the valve.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range of [0,1]

Continuous smoothing factor that introduces a layer of gradual change
to the flow response when the valve is in near-open or near-closed
positions. Set this value to a nonzero value less than one to increase
the stability of your simulation in these regimes.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to
`Linear`.

### **Pressure recovery** — Whether to account for pressure increase in area expansions `off` (default) | `on`

Accounts for pressure increase when fluid flows from a region of smaller cross-sectional
area to a region of larger cross-sectional area. This increase in
pressure is not captured when you clear the **Pressure
recovery** check box.

### **Opening dynamics** — Whether to introduce flow lag due to orifice opening `off` (default) | `on`

Accounts for transient effects to the fluid system due to the valve opening. Selecting
**Opening dynamics** approximates the opening
conditions by introducing a first-order lag in the flow response. The
**Opening time constant** also impacts the modeled
opening dynamics.

### **Reducing valve initial opening area** — Open area at port P at the start of the simulation `1e-4` m^2 (default) | positive scalar

Initial cross-sectional area at port **P** at the
time of dynamic opening. This value is used to calculate the
instantaneous opening area for the dynamic opening between
**P** and **A** at the following
time step.

#### Dependencies

To enable this parameter, select **Opening dynamics**.

### **Relief valve initial opening area** — Open area at port T at the start of the simulation `1e-10` m^2 (default) | positive scalar

Initial cross-sectional area at port **T** of opening
at the time of dynamic opening. This value is used to calculate the
instantaneous opening area for the dynamic opening between
**A** and **T** at the following
time step.

#### Dependencies

To enable this parameter, select **Opening dynamics**.

### **Opening time constant** — Valve opening time constant `0.1` s (default) | positive scalar

Constant that captures the time required for the fluid to reach
steady-state when opening or closing the valve from one position to
another. This parameter impacts the modeled opening dynamics.

#### Dependencies

To enable this parameter, select **Opening dynamics**.

### Faults

### **Pressure-Reducing 3-Way Valve Area fault** — Option to model valve area fault `Add fault`

Option to model a valve area fault in the block. To add a fault, click the **Add
fault** hyperlink. When a fault occurs, the valve area
normally set by the opening parameterization is set based on the value
specified in the **Opening area when faulted**
parameter.

### **Valve areas when faulted** — Faulted valve characteristics `Reducing valve closed and relief valve open` (default) | `Reducing valve open and relief valve closed` | `Maintain last value`

Faulted valve type. You can choose for the valve to seize when the
valves are opened, closed, or at the area when faulting is
triggered.

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

The Pressure-Reducing 3-Way Valve (IL) block now supports the Simscape faults interface. To learn more, see Introduction to Simscape Faults.

## Description

Combined pressure-relief and pressure-reducing valve in an isothermal liquid system

The Pressure-Reducing 3-Way Valve (IL) is a combination of a pressure-relief and
pressure-reducing valve. It maintains pressure at the valve outlet, port
**A**, by restricting the inflow area at port
**P** and venting the flow at port **T**.

### Valve Functionality

The block controls the valve operation by comparing the pressure difference between port
**A** and port **T** to a set of pressure
threshold ranges. When the pressure difference between **A** and
**T**, *Pcontrol*,
exceeds *Pset,reducing*, port
**P** begins to close. When
*Pcontrol* is between
*Pset,reducing*+*Preg*
and *Pset,reducing*+
*Preg*+*Ptransition*,
the block is in a transition range and both valves at ports **P**
and **T** are closed. When
*Pcontrol* exceeds the pressure
transition range, *Pset,relief*, where Pset,relief=Pset,reducing+Preg+Ptransition, port **T** begins to open.

To simulate pressure relief or pressure reduction with respect to another system
element, see Pressure
Compensator Valve (IL). To simulate pressure reduction between
the valve outlet and atmosphere, see the Pressure-Reducing
Valve (IL). To simulate pressure relief with respect to a valve
or between the valve outlet and atmospheric pressure, see Pressure Relief
Valve (IL).

### Pressure Control

When *Pcontrol*,
*PA* –
*PT*, exceeds the threshold
pressure, *Pset,reducing*, the valve at port
**P** begins to close. When the pressure exceeds the transition
range, or when *Pcontrol* >
*Pset,relief*, the valve at port
**T** begins to open. Both valve closing and opening are
parameterized in two ways:

- When **Set pressure control** is
  `Controlled`, the block uses the pressure
  signal at port **Ps** to control the valve. In this
  setting, *Preg* is the value of
  the **Pressure regulation range** parameter, and
  *Ptransition* is the
  value of the **Pressure transition range** parameter.
  The pressure-reducing valve begins to close when
  *Pcontrol* is greater
  than *Pset,reducing*, which is
  the value of the signal at port **Ps**. The relief
  valve response is triggered, meaning port **T** starts
  to open, when *Pcontrol* is
  greater than *Pset,relief* and
  below *Pmax,relief*.
  *Pmax,relief* is the sum
  of the value of the **Pressure regulation range**
  parameter and
  *Pset,relief*.
- When **Set Pressure control** is
  `Constant`, the valve closing at port
  **P** is continuously regulated by either a linear
  or tabular parameterization. Similarly, relief valve opening at port
  **T** is parameterized linearly or by table lookup.
  An example of linear parameterization of the reduction valve (solid
  line) and relief valve (dotted line) is shown below.

  If you set **Opening parameterization** to
  `Linear`,
  *Pset,reducing* is the
  value of the **Set pressure differential for reducing
  valve** parameter,
  *Preg* is the value of the
  **Pressure regulation range** parameter, and
  *Ptransition* is the
  value of the **Pressure transition range** parameter.
  *Pmax,relief* is the sum
  of the value of the **Pressure regulation range**
  parameter and
  *Pset,relief*.

  If you set **Opening parameterization** to
  `Tabulated`,
  *Pset,reducing* and
  *Pmax,reducing* are the
  first and last parameters of the **Pressure differential vector
  for reducing valve**, respectively, and
  *Pset,relief* and
  *Pmax,relief* are the
  first and last parameters of the **Pressure differential vector
  for relief valve**, respectively. An example of tabular
  parameterization of both the reducing and relieving valves are shown
  below.

### Mass Flow Rate Equation

Momentum is conserved through the valve:

m˙A+m˙reducing+m˙relief=0.

The mass flow rate through the valves is calculated as:

m˙reducing=CdAPA2ρ¯PRloss,reducing(1−(APAAport)2)Δpreducing[Δpreducing2+Δpcrit,reducing2]1/4,

m˙relief=CdAAT2ρ¯PRloss,relief(1−(AATAport)2)Δprelief[Δprelief2+Δpcrit,relief2]1/4,

where:

- *Cd* is the value of the
  **Discharge coefficient** parameter.
- *A* is the instantaneous valve open area between
  ports **A** and **P** or
  **A** and **T**, as indicated by
  the subscript.
- *A*port is the value of the
  **Cross-sectional area at ports A, P & T**
  parameter.
- ρ¯ is the average fluid density.
- *Δp* is the valve pressure difference,
  *pA* –
  *pB*.

The critical pressure difference,
*Δpcrit*, is the pressure
differential associated with the **Critical Reynolds number**,
*Recrit*, the flow regime transition
point between laminar and turbulent flow, which corresponds to either the
pressure-reducing or pressure relief component of the valve,

Δpcrit=πρ¯8A(νRecritCd)2,

where *A* is either
*APA* or
*AAT*, corresponding to the reducing
or relief component of the valve, respectively.

*Pressure loss* describes the reduction of pressure in the valve due to
a decrease in area. *PRloss* is

PRloss=1−(AAport)2(1−Cd2)−CdAAport1−(AAport)2(1−Cd2)+CdAAport.

*Pressure recovery* describes the positive pressure change in the valve
due to an increase in area. If you do not want to capture this increase in pressure,
clear the **Pressure recovery** checkbox. In this case,
*PRloss* is 1.

When **Set Pressure control** is `Constant`, the
block calculates the opening area *A* by using the opening
parameterization of the reducing valve (**P** to
**A**) or relief valve (**A** to
**T**) and the valve opening dynamics.

### Opening and Closing Parameterization

When you set **Opening parameterization** to
`Linear`, the valve area for the reducing valve is

Avalve=p^reducing(Aleak−Amax)+Amax,

and for the relief valve is

Avalve=p^relief(Amax−Aleak)+Aleak.

The normalized pressure, p^, is

p^=pcontrol−psetpmax−pset,

where the set and maximum pressures are the respective reducing
or relief valve settings.

When the valve is in a near-open or near-closed position
in the linear parameterization, you can maintain numerical robustness in your
simulation by adjusting the **Smoothing factor** parameter. If
the **Smoothing factor** parameter is nonzero, the block smoothly
saturates the control pressure between
*pset* and
*pmax*. For more information, see
Numerical Smoothing.

When you set **Opening parameterization** to
`Tabulated`,
*A*leak,PA and
*A*max,PA are the first and last
elements of the **Opening area vector reducing valve** parameter,
respectively, and *A*leak,AT and
*A*max,AT are the first and last
elements of the **Opening area vector for relief valve** parameter,
respectively. The block calculates the opening area as

Avalve=tablelookup(pcontrol,TLU,ref,ATLU,pcontrol,interpolation=linear,extrapolation=nearest).

For the reducing valve, the block calculates the opening area by using the table lookup
method, where:

- *pcontrol* is the control
  pressure, which is the pressure differential between ports
  **A** and **T**.
- *pcontrol,TLU,ref*
  = *pTLU* +
  *poffset*.
- *pTLU* is the
  **Pressure differential vector for reducing valve**
  parameter
- *poffset* is an internal
  pressure offset that causes the valve to start closing when
  *pcontrol,TLU,ref* =
  *pset,reducing*.
- *ATLU* is the
  **Opening area vector reducing valve**
  parameter.

For the relief valve, the block calculates the opening area by using the table lookup
method, where:

- *pcontrol* is the pressure
  differential between ports **A** and
  **T**.
- *pcontrol,TLU,ref*
  = *pTLU* +
  *poffset*.
- *pTLU* is the
  **Pressure differential vector for relief valve**
  parameter.
- *poffset* is an internal
  pressure offset that causes the valve to start opening when
  *pcontrol,TLU,ref* =
  *pset,releif*.
- *ATLU* is the
  **Opening area vector for relief valve** parameter.

### Opening Dynamics

If **Opening dynamics** are modeled, a lag is introduced to the flow
response to valve opening. *A*valve becomes
the dynamic opening or closing area, *A*dyn;
otherwise, *A*valve is the steady-state
opening area. This area is specific to the reducing and relief components of the
valve, *A*PA or
*A*AT, respectively. The instantaneous
change in dynamic opening area is calculated based on the **Opening time
constant**, *τ*:

p˙dyn=pcontrol−pdynτ.

By default, **Opening dynamics** are not
modeled.

### Faults

To model a fault, in the **Faults** section,
click the **Add fault** hyperlink next to the fault that you want to model. Use
the fault parameters to specify the fault properties. For more information about fault modeling,
see Introduction to Simscape Faults.

The **Valve areas when faulted** parameter has three fault options:

- `Reducing valve closed and relief valve open`
  — The reducing valve freezes at its smallest value and the relief
  valve freezes at its largest value, depending on the **Opening
  parameterization**:

  - When **Opening parameterization** is set
    to `Linear`, the reducing valve
    area freezes at the value of the **Leakage
    area** parameter and the relief valve area
    freezes at the value of the **Maximum opening
    area** parameter.
  - When **Opening parameterization** is set
    to `Tabulated`, the reducing valve
    area freezes at the value of the first element of the
    **Opening area vector** parameter and
    the relief valve area freezes at the value of the last
    element of the **Opening area vector**
    parameter.
- `Reducing valve open and relief valve closed`
  — The reducing valve freezes at its largest value and the relief
  valve freezes at its smallest value, depending on the **Opening
  parameterization**:

  - When **Opening parameterization** is set
    to `Linear`, the reducing valve
    area freezes at the value of the **Maximum opening
    area** parameter and the relief valve freezes
    at the value of the **Leakage area**
    parameter.
  - When **Orifice parameterization** is set
    to `Tabulated`, the reducing valve
    area freezes at the value of the last element of the
    **Opening area vector** parameter and
    the relief valve area freezes at the value of the first
    element of the **Opening area vector**
    parameter.
- `Maintain last value` — The reducing
  and relief valve areas freeze at the open area when the trigger
  occurred.

Due to numerical smoothing at the extremes of the valve area, the
minimum area the block uses is larger than the value of the **Leakage
area** parameter, and the maximum is smaller than the value of the
**Maximum orifice area** parameter, in proportion to the
**Smoothing factor** value.

After the fault triggers, the valves remain at the faulted area for the rest of the
simulation.

### Assumptions and Limitations

Friction between the valve and fluid, the hydraulic force of the fluid on the
valve components, and the effect of fluid inertia are neglected.
