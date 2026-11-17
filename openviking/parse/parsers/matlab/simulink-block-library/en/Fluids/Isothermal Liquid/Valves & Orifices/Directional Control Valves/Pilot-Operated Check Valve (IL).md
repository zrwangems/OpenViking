---
type: simulink-block
title: 'Pilot-Operated Check Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: 'pilotoperatedcheckvalveil'
documentation_source_path: 'ref/pilotoperatedcheckvalveil.html'
language: en
---

# Pilot-Operated Check Valve (IL)

## Ports
```yaml
ports:
- name: A
  summary: Liquid port isothermal liquid
  direction: conserving
- name: B
  summary: Liquid port isothermal liquid
  direction: conserving
- name: X
  summary: Pressure port isothermal liquid
  direction: conserving
```

### Conserving

### **A** — Liquid port isothermal liquid

Isothermal liquid conserving port associated with the valve entry. When the control
pressure exceeds the cracking pressure, liquid can exit from this
port.

### **B** — Liquid port isothermal liquid

Isothermal liquid conserving port associated with the valve exit. When the control
pressure exceeds the cracking pressure, liquid can enter the valve from
this port.

### **X** — Pressure port isothermal liquid

Isothermal liquid conserving port associated with the pressure port that contributes to
the flow control through the valve. There is no mass flow through this
port.
## Parameters
```yaml
parameters:
- name: Pilot pressure direction
  summary: Whether pilot pressure assists with valve opening or valve closing Pilot-to-open (default) | Pilot-to-close
  group: ''
- name: Spool configuration
  summary: Valve geometry Rigidly connected pilot spool and poppet (default) | Disconnected pilot spool and poppet
  group: ''
- name: Opening pilot pressure specification
  summary: Reference pressure differential for valve control Pressure difference of port X relative to port A (default) |
    Gauge pressure at port X
  group: ''
- name: Opening parameterization
  summary: Method of calculating valve opening Linear - Area vs. pressure (default) | Tabulated data - Area vs. pressure |
    Tabulated data - Volumetric flow rate vs. pressure
  group: ''
- name: Cracking pressure differential
  summary: Pressure threshold 0.01 MPa (default) | positive scalar
  group: ''
- name: Maximum opening pressure differential
  summary: Maximum pressure differential in opened valve 0.02 MPa (default) | positive scalar
  group: ''
- name: Pilot ratio
  summary: Pilot port area ratio 1 (default) | positive scalar in the range of (0,1]
  group: ''
- name: Maximum opening area
  summary: Maximum valve area 1e-4 m^2 (default) | positive scalar
  group: ''
- name: Leakage area
  summary: Gap area when in fully closed position 1e-10 m^2 (default) | positive scalar
  group: ''
- name: Control pressure vector
  summary: 'Control pressure values for tabular parameterization [0.01 : 0.01 : 0.1] MPa (default) | 1-by-*n* vector'
  group: ''
- name: Opening area vector
  summary: Valve opening areas for tabular parameterization [1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05,
    .0001] m^2 (default) | 1-by-*n* vector
  group: ''
- name: Reference pressure differential vector
  summary: 'Pressure differential vector for tabular volumetric flow rate parameterization [0.01 : 0.01 : 0.1] MPa (default)
    | 1-by-*n* vector'
  group: ''
- name: Reference volumetric flow rate vector
  summary: Vector of volumetric flow rate for tabulated data parameterization [.000358, .045, .11, .191, .284, .39, .505,
    .63, .764, .905] .* 1e-3 m^3/s (default) | 1-by-*n* vector
  group: ''
- name: Cross-sectional area at ports A and B
  summary: Area at conserving ports inf m^2 (default) | positive scalar
  group: ''
- name: Discharge coefficient
  summary: Discharge coefficient 0.64 (default) | positive scalar
  group: ''
- name: Critical Reynolds number
  summary: Upper Reynolds number limit for laminar flow 150 (default) | positive scalar
  group: ''
- name: Smoothing factor
  summary: Numerical smoothing factor 0.01 (default) | positive scalar in the range [0,1]
  group: ''
- name: Pressure recovery
  summary: Whether to account for pressure increase in area expansions off (default) | on
  group: ''
- name: Opening dynamics
  summary: Whether to introduce flow lag due to valve opening off (default) | on
  group: ''
- name: Opening time constant
  summary: Valve opening time constant 0.1 s (default) | positive scalar
  group: ''
```

### **Pilot pressure direction** — Whether pilot pressure assists with valve opening or valve closing `Pilot-to-open` (default) | `Pilot-to-close`

Whether the pilot pressure assists with valve opening or closing. If you
set the parameter to `Pilot-to-open`, the pilot
pressure assists the valve opening. If you set the parameter to
`Pilot-to-close`, the pilot pressure assists
the valve closing.

### **Spool configuration** — Valve geometry `Rigidly connected pilot spool and poppet` (default) | `Disconnected pilot spool and poppet`

Valve geometry. Use `Rigidly connected pilot spool and poppet`
to model a valve with an opening mechanism connected to the valve poppet, or
`Disconnected pilot spool and poppet` to model
an opening mechanism that is aligned with, but moves freely away from, the
valve poppet. This parameter determines the pilot pressure
calculation.

#### Dependencies

To enable this parameter, set **Pilot pressure
direction** to
`Pilot-to-open`.

### **Opening pilot pressure specification** — Reference pressure differential for valve control `Pressure difference of port X relative to port A` (default) | `Gauge pressure at port X`

Reference pilot pressure differential to use for the valve control. The block adds the
pilot pressure differential to the pressure differential between ports
**A** and **B** and compared against
the valve threshold **Cracking pressure
differential**.

#### Dependencies

To enable this parameter, set **Pilot pressure
direction** to
`Pilot-to-open`.

### **Opening parameterization** — Method of calculating valve opening `Linear - Area vs. pressure` (default) | `Tabulated data - Area vs. pressure` | `Tabulated data - Volumetric flow rate vs. pressure`

Method of calculating valve opening:

- `Linear - Area vs. pressure` — The
  valve opening area corresponds linearly to the valve
  pressure.
- `Tabulated data - Area vs. pressure`
  — The block determines the valve mass flow rate from a table of
  area values with respect to the pressure differential.
- `Tabulated data - Volumetric flow rate vs.
  pressure` — The block determines the valve mass
  flow rate from a table of volumetric flow rate values with
  respect to the pressure differential.

### **Cracking pressure differential** — Pressure threshold `0.01 MPa` (default) | positive scalar

Set pressure for the valve operation.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure`.

### **Maximum opening pressure differential** — Maximum pressure differential in opened valve `0.02 MPa` (default) | positive scalar

Maximum pressure differential in an opened valve. This value provides an
upper limit to simulation pressures so that results remain physical.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure`.

### **Pilot ratio** — Pilot port area ratio `1` (default) | positive scalar in the range of (0,1]

Ratio of port area **X** to port area
**A**.

### **Maximum opening area** — Maximum valve area `1e-4 m^2` (default) | positive scalar

Maximum valve area. The block uses this value to determine the normalized valve pressure
and the valve opening area during operation.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure`.

### **Leakage area** — Gap area when in fully closed position `1e-10 m^2` (default) | positive scalar

Sum of all gaps when the valve is in the fully closed position. Any area smaller than
this value saturates to the specified leakage area. This parameter
contributes to numerical stability by maintaining continuity in the
flow.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure`.

### **Control pressure vector** — Control pressure values for tabular parameterization `[0.01 : 0.01 : 0.1] MPa` (default) | 1-by-*n* vector

Vector of pressure differential values for the tabular parameterization of
the valve opening area. The first element of this vector is the cracking
pressure differential.

The vector elements must correspond one-to-one with the elements in the **Opening
area vector** parameter. The elements are in ascending order
and must be greater than 0. The block employs linear interpolation between
the table data points.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Tabulated data - Area
vs. pressure`.

### **Opening area vector** — Valve opening areas for tabular parameterization `[1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of valve opening areas for the tabular area parameterization of the
valve opening area. The first element of this vector is the leakage area
when the valve is fully closed and the last element is the maximum valve
area.

The vector elements must correspond one-to-one with the elements in the **Control
pressure vector** parameter. The elements are in ascending
order and must be greater than 0. The block employs linear interpolation
between the table data points.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Tabulated data - Area
vs. pressure`.

### **Reference pressure differential vector** — Pressure differential vector for tabular volumetric flow rate parameterization `[0.01 : 0.01 : 0.1] MPa` (default) | 1-by-*n* vector

Vector of pressure differential values for the tabular volumetric flow rate
parameterization. These values are the free flow data when the pilot
pressure is `0`. The vector elements must correspond
one-to-one with the elements in the **Reference volumetric flow rate
vector** parameter. The elements are in ascending order and
must be greater than 0. The block employs linear interpolation between the
table data points.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Tabulated data -
Volumetric flow rate vs. pressure`.

### **Reference volumetric flow rate vector** — Vector of volumetric flow rate for tabulated data parameterization `[.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3 m^3/s` (default) | 1-by-*n* vector

Vector of volumetric flow rate values for the tabular parameterization. These values are
the free flow data when the pilot pressure is `0`. This
vector must have the same number of elements as the **Reference
pressure differential vector** parameter. The vector elements
must be in ascending order.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Tabulated data -
Volumetric flow rate vs. pressure`.

### **Cross-sectional area at ports A and B** — Area at conserving ports `inf m^2` (default) | positive scalar

Areas at the entry and exit ports **A** and **B**,
which the block uses in the pressure-flow rate equation that determines the
mass flow rate through the valve.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure` or `Tabulated data - Area vs.
pressure`.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor that accounts for discharge losses in theoretical flows.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the orifice.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change to the flow response
when the valve is in near-open or near-closed positions. Set this value to a
nonzero value less than one to increase the stability of your simulation in
these regimes.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure`.

### **Pressure recovery** — Whether to account for pressure increase in area expansions `off` (default) | `on`

Whether to account for pressure increase when fluid flows from a region of
smaller cross-sectional area to a region of larger cross-sectional
area.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to `Linear - Area vs.
pressure` or `Tabulated data - Area vs.
pressure`.

### **Opening dynamics** — Whether to introduce flow lag due to valve opening `off` (default) | `on`

Whether to account for transient effects to the fluid system due to opening the valve.
Selecting **Opening dynamics** approximates the opening
conditions by introducing a first-order lag in the pressure response.

### **Opening time constant** — Valve opening time constant `0.1 s` (default) | positive scalar

Constant that captures the time required for the fluid to reach
steady-state conditions when opening or closing the valve from one position
to another. This parameter impacts the modeled opening dynamics.

#### Dependencies

To enable this parameter, select **Opening dynamics**.
## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Directional Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

### R2025a: Parameterize block by using tabulated data

Parameterize the block with tabulated data for area and pressure or for volumetric flow
rate and pressure. Set **Opening parameterization** to
`Linear - Area vs. pressure` to preserve the previous
block functionality

### R2025a: Model pilot-to-close check valve

Set the **Pilot pressure direction** parameter to
`Pilot-to-close` to model a valve where the pilot
pressure assists the valve closing. Set **Pilot pressure
direction** to `Pilot-to-open` to preserve the
previous block functionality.

## Description

Check valve with pilot pressure control in an isothermal liquid system

The Pilot-Operated Check Valve (IL) block models a flow-control valve that allows
variable-direction flow based on the pilot-line pressure. The free flow direction is
from port **A** to port **B** and the valve opens when
the control pressure rises above the cracking pressure. When the control pressure
exceeds the value of the **Cracking pressure differential** parameter
or the value of the first element of the **Control pressure vector** or
**Reference pressure differential vector** parameters, the poppet
moves to allow flow in either direction. There is no mass flow at port
**X** or between port **X** and ports
**A** and **B**.

Schematic of Pilot-operated check valve

When the **Pilot pressure direction** parameter is
`Pilot-to-open`, the control pressure,
*pcontrol* is

pcontrol=ppilotkp+(pA−pB),

where:

- *ppilot* is the control pilot
  pressure differential.

  - When the **Opening pilot pressure specification**
    parameter is `Pressure difference of port X relative to
    port A`,
    *ppilot* is the pressure
    differential between port **X** and port
    **A**.
  - When **Opening pilot pressure specification** is
    `Gauge pressure at port X`,
    *ppilot* is the
    pressure difference between port **X** and
    atmospheric pressure.
- *kp* is the value of the
  **Pilot ratio** parameter, which is the ratio of the
  area at port **X** to the area at port
  **A**, kp=AXAA.
- *pA* –
  *pB* is the pressure
  differential over the valve.

When the **Pilot pressure direction** parameter is
`Pilot-to-close`, the control pressure is

pcontrol=−ppilotkp+(pA−pB),

where *ppilot =
pX - pB*.

### Spool Configuration

When the **Pilot pressure direction** parameter is
`Pilot-to-open`, you can configure the spool and poppet
as either rigidly connected or disconnected. When the **Spool
configuration** parameter is `Disconnected pilot spool and
poppet`, the relative pressure at port **X** must
be positive. If the measured pilot pressure is negative, the control pressure is
based only on the pressure differential between ports **A** and
**B**. When the **Spool configuration**
parameter is `Rigidly connected pilot spool and poppet`,
the pilot pressure is the measured pressure differential according to the opening
specification.

When the **Pilot pressure direction** parameter is
`Pilot-to-close`, the pilot spool and poppet are
disconnected. The relative pressure at port **X** must be positive.
If the measured pilot pressure is negative, the control pressure is based only on
the pressure differential between ports **A** and
**B**.

### Area vs. Pressure Opening Parameterizations

When **Opening parameterization** is `Linear - Area vs.
pressure` or `Tabulated data - Area vs.
pressure`, the mass flow rate through the valve is

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

where:

- *Cd* is the value of the
  **Discharge coefficient** parameter.
- *Avalve* is the instantaneous
  valve open area.
- *Aport* is the value of the
  **Cross-sectional area at ports A and B**
  parameter.
- ρ¯ is the average fluid density.
- *Δp* is the valve pressure difference,
  *p*A –
  *p*B.

The critical pressure difference,
*Δp*crit, is the pressure differential
associated with the **Critical Reynolds number**,
*Re*crit, the flow regime transition
point between laminar and turbulent flow,

Δpcrit=πρ¯8Avalve(νRecritCd)2.

The pressure loss is the pressure reduction in the valve due to a decrease in
area. *PR*loss is

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport.

The pressure recovery is the positive pressure change in the valve due to an increase in
area. If you do not want to capture this increase in pressure, clear the
**Pressure recovery** check box. In this case,
*PR*loss is 1.

**Linear Area vs. Pressure**

When **Opening parameterization** is `Linear -
Area vs. pressure`, the valve area is

Avalve=p^(Amax−Aleak)+Aleak,

where the normalized pressure, p^, is

p^=pcontrol−pcrackingpmax−pcracking.

When the valve is in a near-open or
near-closed position, you can maintain numerical robustness in your simulation
by adjusting the **Smoothing factor** parameter. If the
**Smoothing factor** parameter is nonzero, the block
smoothly saturates the control pressure between
*pmax* and
*pcracking*. For more
information, see Numerical Smoothing.

**Tabulated Area vs. Pressure**

When **Opening parameterization** is `Tabulated
data - Area vs. pressure`, the block interpolates the area of
the valve as

Avalve=tablelookup(pcontrol,TLU,Avalve,TLU,pcontrol,interpolation=linear,extrapolation=nearest),

where:

- *pcontrol,TLU* is the
  **Control pressure vector** parameter
- *Avalve,TLU* is the
  **Opening area vector** parameter.

The area of the valve saturates between the first and last element of the
**Opening area vector** parameter. The first element of the
**Control pressure vector** parameter corresponds to the
cracking pressure differential.

### Volumetric Flow Rate vs. Pressure Parameterization

When **Opening parameterization** is `Tabulated data
- Volumetric flow rate vs. pressure`, the mass flow rate is

m˙=ρ¯KΔp(Δp2+Δpcrit2)1/4,

and

K=tablelookup(Δpref,TLU,V˙ref,TLUΔpref,TLU,pcontrol,interpolation=linear,extrapolation=nearest),

where:

- *Δpref,TLU* is the
  **Reference pressure differential vector**
  parameter.
- V˙ref,TLU is the
  **Reference volumetric flow rate vector**
  parameter.

The value of *K* saturates between the values V˙ref,TLU(1)Δpref,TLU(1) and V˙ref,TLU(end)Δpref,TLU(end), which means that the first elements of the **Reference
pressure differential vector** and **Reference volumetric flow
rate vector** parameters correspond to the leakage mass flow rate and
the last elements correspond to the maximum mass flow rate.

### Opening Dynamics

If you select **Opening dynamics**, the block introduces a lag to the flow
response to the modeled control pressure.
*p*control becomes the dynamic control
pressure, *p*dyn. The instantaneous change
in dynamic control pressure depends on the **Opening time
constant** parameter, *τ*,

p˙dyn=pcontrol−pdynτ.

By default, the **Opening dynamics** check box
is cleared.

### Mass Conservation

Mass is conserved through the valve,

m˙A+m˙B=0.
