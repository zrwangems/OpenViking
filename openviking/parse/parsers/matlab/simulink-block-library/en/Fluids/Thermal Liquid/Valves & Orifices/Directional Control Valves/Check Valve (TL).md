---
type: simulink-block
title: 'Check Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: 'checkvalvetl'
documentation_source_path: 'ref/checkvalvetl.html'
language: en
---

# Check Valve (TL)

## Ports
```yaml
ports:
- name: A
  summary: Valve inlet thermal liquid
  direction: conserving
- name: B
  summary: Valve outlet thermal liquid
  direction: conserving
```

### Conserving

### **A** — Valve inlet thermal liquid

Thermal liquid conserving port associated with the valve inlet.

### **B** — Valve outlet thermal liquid

Thermal liquid conserving port associated with the valve
outlet.
## Parameters
```yaml
parameters:
- name: Opening parameterization
  summary: Method of calculating valve opening Linear - Area vs. pressure (default) | Tabulated data - Area vs. pressure |
    Tabulated data - Volumetric flow rate vs. pressure
  group: Parameters
- name: Opening pressure specification
  summary: Pressure differential to use for valve control Pressure differential (default) | Pressure at port A
  group: Parameters
- name: Cracking pressure differential
  summary: Threshold pressure 0.01 MPa (default) | positive scalar
  group: Parameters
- name: Cracking pressure (gauge)
  summary: Threshold pressure 0.1 MPa (default) | positive scalar
  group: Parameters
- name: Maximum opening pressure differential
  summary: Valve differential pressure maximum 0.02 MPa (default) | positive scalar
  group: Parameters
- name: Maximum opening pressure (gauge)
  summary: Valve pressure maximum 0.2 MPa (default) | positive scalar
  group: Parameters
- name: Maximum opening area
  summary: Area of fully opened valve 1e-4 m^2 (default) | positive scalar
  group: Parameters
- name: Leakage area
  summary: Valve gap area when in fully closed position 1e-10 m^2 (default) | positive scalar
  group: Parameters
- name: Pressure differential vector
  summary: 'Differential pressure values for tabular parameterization [0.01 : 0.01 : 0.1] MPa (default) | 1-by-*n* vector'
  group: Parameters
- name: Opening area vector
  summary: Valve opening areas for tabular parameterization [1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05,
    .0001] m^2 (default) | 1-by-*n* vector
  group: Parameters
- name: Cross-sectional area at ports A and B
  summary: Area at valve entry or exit 0.01 m^2 (default) | positive scalar
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
- name: Volumetric flow rate vector
  summary: Vector of volumetric flow rate for tabulated data parameterization [.000358, .045, .11, .191, .284, .39, .505,
    .63, .764, .905] .* 1e-3 m^3/s (default) | 1-by-*n* vector
  group: Parameters
- name: Check Valve Area fault
  summary: Option to model valve area fault Add fault
  group: Faults
- name: Opening area when faulted
  summary: Faulted valve area Closed (default) | Open | Maintain at last value
  group: Faults
```

### Parameters

### **Opening parameterization** — Method of calculating valve opening `Linear - Area vs. pressure` (default) | `Tabulated data - Area vs. pressure` | `Tabulated data - Volumetric flow rate vs. pressure`

Method of calculating valve opening.

- `Linear - Area vs. pressure`: The
  valve opening area corresponds linearly to the valve
  pressure.
- `Tabulated data - Area vs.
  pressure`: The block determines the valve
  mass flow rate from a table of area values with respect to
  pressure differential.
- `Tabulated data - Volumetric flow rate vs.
  pressure`: The block determines the valve
  mass flow rate from a table of volumetric flow rate values
  with respect to pressure differential.

### **Opening pressure specification** — Pressure differential to use for valve control `Pressure differential` (default) | `Pressure at port A`

The pressure differential to use for the valve control. Select the
`Pressure differential` option to measure
the pressure difference between ports **A** and
**B**. Select the `Pressure at port
A` option to measure the pressure difference between
port **A** and atmospheric pressure.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure`.

### **Cracking pressure differential** — Threshold pressure `0.01 MPa` (default) | positive scalar

Pressure beyond which the valve operation triggers. This value is the
set pressure when the control pressure is the pressure differential
between ports **A** and **B**.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure` and **Opening pressure
specification** to `Pressure
differential`.

### **Cracking pressure (gauge)** — Threshold pressure `0.1 MPa` (default) | positive scalar

Gauge pressure beyond which valve operation triggers when the control
pressure is the pressure differential between port
**A** and atmospheric pressure.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure` and **Opening pressure
specification** to `Pressure at port
A`.

### **Maximum opening pressure differential** — Valve differential pressure maximum `0.02 MPa` (default) | positive scalar

Maximum valve differential pressure. This parameter provides an upper
limit to the pressure so that system pressures remain realistic.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure` and **Opening pressure
specification** to `Pressure
differential`.

### **Maximum opening pressure (gauge)** — Valve pressure maximum `0.2 MPa` (default) | positive scalar

Maximum valve gauge pressure. This parameter provides an upper limit
to the pressure so that system pressures remain realistic.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure` and **Opening pressure
specification** to `Pressure at port
A`.

### **Maximum opening area** — Area of fully opened valve `1e-4 m^2` (default) | positive scalar

Cross-sectional area of the valve in its fully open position.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure`.

### **Leakage area** — Valve gap area when in fully closed position `1e-10 m^2` (default) | positive scalar

Sum of all gaps when the valve is in its fully closed position. Any
area smaller than this value saturates to the specified leakage area.
This value contributes to numerical stability by maintaining continuity
in the flow.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure`.

### **Pressure differential vector** — Differential pressure values for tabular parameterization `[0.01 : 0.01 : 0.1] MPa` (default) | 1-by-*n* vector

Vector of pressure differential values for the tabular
parameterization of the valve opening area. The vector elements must
correspond one-to-one with the elements in the **Opening area
vector** parameter. The elements are in ascending order and
must be greater than 0. The block employs linear interpolation between
the table data points.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Tabulated data -
Volumetric flow rate vs. pressure` or
`Tabulated data - Area vs.
pressure`.

### **Opening area vector** — Valve opening areas for tabular parameterization `[1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of valve opening areas for the tabular parameterization of the
valve opening area. The vector elements must correspond one-to-one with
the elements in the **Pressure differential vector**
parameter. The elements are in ascending order and must be greater than
0. The block employs linear interpolation between the table data
points.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Tabulated data -
Area vs. pressure`.

### **Cross-sectional area at ports A and B** — Area at valve entry or exit `0.01 m^2` (default) | positive scalar

Cross-sectional area at the entry and exit ports
**A** and **B**. The block uses
these areas in the pressure-flow rate equation that determines the mass
flow rate through the valve.

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

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure`.

### **Pressure recovery** — Whether to account for pressure increase in area expansions `off` (default) | `on`

Whether to account for pressure increase when fluid flows from a
region of smaller cross-sectional area to a region of larger
cross-sectional area.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure`.

### **Opening dynamics** — Whether to account for flow response to valve opening `off` (default) | `on`

Whether to account for transient effects to the fluid system due to
opening the valve. Selecting **Opening dynamics**
approximates the opening conditions by introducing a first-order lag in
the flow response. The **Opening time constant** also
impacts the modeled opening dynamics.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure`.

### **Opening time constant** — Valve opening time constant `0.1 s` (default) | positive scalar

Constant that captures the time required for the fluid to reach
steady-state when opening or closing the valve from one position to
another. This parameter impacts the modeled opening dynamics.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure` and select **Opening
dynamics**.

### **Volumetric flow rate vector** — Vector of volumetric flow rate for tabulated data parameterization `[.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3 m^3/s` (default) | 1-by-*n* vector

Vector of volumetric flow rate values for the tabular parameterization
of valve opening. This vector must have the same number of elements as
the **Pressure drop vector** parameter. The vector
elements must be in ascending order.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Tabulated data -
Volumetric flow rate vs. pressure`.

### Faults

### **Check Valve Area fault** — Option to model valve area fault `Add fault`

Option to model a valve area fault in the block. To add a fault, click
the **Add fault** hyperlink. When a fault occurs, the
block uses the value specified in the **Opening area when
faulted** parameter for the valve area.

### **Opening area when faulted** — Faulted valve area `Closed` (default) | `Open` | `Maintain at last value`

Area that the block uses when the block faults. You can choose for the
valve to seize at the fully closed or fully open position, or at the
conditions when faulting is triggered. This parameter sets the area when
**Opening parameterization** is `Linear
- Area vs. pressure` and the mass flow rate when
**Opening parameterization** is
`Tabulated data`.

#### Dependencies

To enable this parameter, enable faults for the block by clicking
the **Add fault** hyperlink.
## Libraries

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Directional Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

### R2024b: Parameterize block using tabulated data

Set **Opening parameterization** to either `Tabulated
data - Area vs. pressure` or `Tabulated data -
Volumetric flow rate vs. pressure` to use tabulated data to
parameterize the block.

To maintain the same behavior as previous releases, set **Opening
parameterization** to `Linear - Area vs.
pressure`.

### R2024b: Model faults with the Simscape faults interface

The Check Valve (TL) block now supports the Simscape faults interface. To learn more,
see Introduction to Simscape Faults.

## Description

Check valve in a thermal liquid network

The Check Valve (TL) block models a check valve in the
thermal liquid domain. A check valve is a proportional valve that shuts when the
pressure difference between its ports drops below a threshold called the
*cracking pressure*. Check valves are common in backflow
prevention devices, such as those used in public water supply networks, where
contaminated water downstream of a water main must not be allowed to return upstream.
The block does not assume a specific valve shutoff mechanism such as a ball, disc, or
diaphragm. The allowed direction of flow is always from port **A** to
port **B**.

The valve cracks open when the pressure drop across the valve rises above the
specified cracking pressure. When the pressure drop reaches the maximum value specified
in the block, the valve is fully open and its opening area no longer increases with
pressure. The flow rate through the valve is never truly zero because a small leakage
area remains when the pressure falls below the cracking pressure.

### Area vs. Pressure Parameterizations

You can parameterize the block using linear or tabulated area and pressure
data.

**Linear Area vs Pressure Parameterization**

When **Opening parameterization** is `Linear -
Area vs. pressure`, the valve open area is linearly related to
the opening pressure differential. There are two options for valve control:

- When **Opening pressure differential**  is
  `Pressure differential`, the control
  pressure is the pressure differential between ports
  **A** and **B**. The valve
  begins to open when
  *P*control meets or
  exceeds the value of the **Cracking pressure
  differential** parameter.
- When **Opening pressure differential**  is
  `Pressure at port A`, the control
  pressure is the pressure difference between port
  **A** and atmospheric pressure. When
  *P*control meets or
  exceeds the value of the **Cracking pressure
  (gauge)** parameter, the valve begins to open.

The linear parameterization of the valve area is

Avalve=p^(Amax−Aleak)+Aleak,

where the normalized pressure, p^, is

p^=pcontrol−pcrackingpmax−pcracking.

When the valve is in a near-open or
near-closed position, you can maintain numerical robustness in your simulation
by adjusting the **Smoothing factor** parameter. If the
**Smoothing factor** parameter is nonzero, the block
smoothly saturates the control pressure between
*pcracking* and
*pmax*. For more information,
see Numerical Smoothing.

**Tabulated Data Area vs Pressure Parameterization**

When you set **Opening parameterization** to
`Tabulated data - Volumetric flow rate vs.
pressure`, the block linearly interpolates
*Avalve* from the curve of the
**Opening area vector** parameter versus the
**Pressure differential vector** parameter for a simulated
pressure differential.

For the tabulated data and linear area vs pressure parameterizations, the mass
flow rate through the valve is

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
differential associated with the **Critical Reynolds number**
parameter, *Recrit*, the flow regime
transition point between laminar and turbulent flow:

Δpcrit=πρ¯8Avalve(νRecritCd)2.

The pressure loss is the reduction of pressure in the valve due to a decrease
in area. *PRloss* is

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport.

The pressure recovery is the positive pressure change in the valve due to an
increase in area. If you do not want to capture this increase in pressure, clear
the **Pressure recovery** check box. In this case,
*PRloss* is 1.

### Tabulated Volumetric Flow Rate Parameterization

When **Opening parameterization** is `Tabulated data
- Volumetric flow rate vs. pressure`, the valve opens according to
the user-provided tabulated data of volumetric flow rate and pressure differential
between ports **A** and **B**.

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

When the simulation pressure falls below the first element of the
**Pressure drop vector** parameter,
*K*`=`*KLeak* ,

KLeak=V˙TLU(1)|ΔpTLU(1)|,

where *V˙TLU(1)* is the first element
of the **Volumetric flow rate vector** parameter.

When the simulation pressure rises above the last element of the
**Pressure drop vector** parameter,
*K*`=`*KMax*,

KMax=V˙TLU(end)|ΔpTLU(end)|,

where *V˙TLU(end)* is the last
element of the **Volumetric flow rate vector** parameter.

### Mass Balance

Mass is conserved through the valve

m˙A+m˙B=0,

where m˙ is the mass flow rate at port **A** or
**B**.

### Energy Balance

The valve is an adiabatic component. No heat exchange can occur between the fluid
and the wall of the valve. No work is done on or by the fluid as it traverses the
valve. With these assumptions, energy can enter and exit the valve only by
advection, through ports **A** and **B**. By the
principle of conservation of energy, the sum of the energy flows through the ports
must always equal zero,

ϕA+ϕB=0,

where *ϕ* is the energy flow rate into the valve through ports
**A** or **B**.

### Opening Dynamics

When **Opening parameterization** is `Linear- Area
vs. Pressure`, the block can model opening and closing dynamics. If
you model opening dynamics, the block introduces a lag to the flow response to the
control pressure and *pcontrol* becomes the
dynamic control pressure, *pdyn*.
Otherwise, *pcontrol* is the steady-state
pressure. The block calculates the instantaneous change in dynamic control pressure
based on the **Opening time constant** parameter,
*τ*:

p˙dyn=pcontrol−pdynτ.

By default, the **Opening dynamics** check box
is cleared.

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

When **Opening parameterization** is `Linear -
Area vs. pressure`, the valve area defines the fault options:

- `Closed` — The valve area freezes
  at the value of the **Leakage area**
  parameter.
- `Open` — The valve area freezes at
  the value of the **Maximum opening area**
  parameter.
- `Maintain at last value` — The
  valve freezes at the open area when the trigger occurs.

**Faulting in the Tabulated Data Parameterization**

When **Opening parameterization** is `Tabulated
data - Area vs. pressure` or `Tabulated data -
Volumetric flow rate vs. pressure`, the mass flow rate through
the valve defines the fault options:

- `Closed` — The valve freezes at
  the mass flow rate associated with the first elements of the
  **Volumetric flow rate vector** parameter and
  the **Pressure drop vector** parameters

  m˙=KLeakρ¯Δp.
- `Open` — The valve freezes at the
  mass flow rate associated with the last elements of the
  **Volumetric flow rate vector** and the
  **Pressure drop vector** parameters

  m˙=KMaxρ¯Δp
- `Maintain at last value` — The
  valve freezes at the mass flow rate and pressure differential when
  the trigger occurs,

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
