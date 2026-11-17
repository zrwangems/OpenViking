---
type: simulink-block
title: 'Pressure Compensator Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Pressure Control Valves'
documentation_page: 'pressurecompensatorvalveil'
documentation_source_path: 'ref/pressurecompensatorvalveil.html'
language: en
---

# Pressure Compensator Valve (IL)

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
  summary: Pressure reference isothermal liquid
  direction: conserving
- name: Y
  summary: Pressure reference isothermal liquid
  direction: conserving
- name: Ps
  summary: Controlled pressure differential, Pa physical signal
  direction: input
```

### Conserving

### **A** — Liquid port isothermal liquid

Isothermal liquid conserving port associated with the A side of the valve.

### **B** — Liquid port isothermal liquid

Isothermal liquid conserving port associated with the B side of the valve.

### **X** — Pressure reference isothermal liquid

Isothermal liquid conserving port associated with sensing the pressure
at point X, *Px*.

### **Y** — Pressure reference isothermal liquid

Isothermal liquid conserving port associated with sensing the pressure at point Y,
*P*y.
### Input

### **Ps** — Controlled pressure differential, Pa physical signal

Pressure differential for controlled valve operation, in Pa.

#### Dependencies

To enable this port, set **Set pressure control**
to `Controlled`.
## Parameters
```yaml
parameters:
- name: Valve specification
  summary: Valve bias Normally open (default) | Normally closed
  group: Parameters
- name: Set pressure control
  summary: Constant or controlled valve operation Constant (default) | Controlled
  group: Parameters
- name: Opening parameterization
  summary: Opening parameterization Linear (default) | Tabulated
  group: Parameters
- name: Set pressure differential
  summary: Range outside of which constant valve operation is triggered 0 MPa (default) | scalar
  group: Parameters
- name: Pressure regulation range
  summary: Valve operational pressure range 0.1 MPa (default) | scalar
  group: Parameters
- name: Maximum opening area
  summary: Area of fully open valve 1e-4 m^2 (default) | positive scalar
  group: Parameters
- name: Leakage area
  summary: Gap area when in fully closed position 1e-10 m^2 (default) | positive scalar
  group: Parameters
- name: Pressure differential vector
  summary: 'Differential pressure values for tabulated parameterization [0.2 : 0.2 : 1.2] MPa (default) | 1-by*n* vector'
  group: Parameters
- name: Opening area vector
  summary: Valve opening areas for tabulated parameterization [1e-05, 8e-06, 6e-06, 4e-06, 2e-06, 1e-10] m^2 (default) | 1-by*n*
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
- name: Pressure recovery
  summary: Option to include pressure recovery Off (default) | On
  group: Parameters
- name: Smoothing factor
  summary: Numerical smoothing factor 0.01 (default) | positive scalar in the range of [0,1]
  group: Parameters
- name: Opening dynamics
  summary: Option to simulate flow response to valve transitions off (default) | on
  group: Parameters
- name: Opening time constant
  summary: Valve opening time constant 0.1 s (default) | positive scalar
  group: Parameters
- name: Pressure Compensator Valve Area fault
  summary: Option to model valve area fault Add fault
  group: Faults
- name: Opening area when faulted
  summary: Faulted valve position Closed (default) | Open | Maintain last value
  group: Faults
```

### Parameters

### **Valve specification** — Valve bias `Normally open` (default) | `Normally closed`

Normal operating condition of the pressure compensator valve. For a reducing valve,
choose `Normally open` valve. For a relief
valve, choose `Normally closed`.

### **Set pressure control** — Constant or controlled valve operation `Constant` (default) | `Controlled`

Valve operation method. When you set this parameter to:

- `Controlled` and connect a
  pressure signal to port **Ps**, the block
  keeps the pressure regulation range constant. The valve
  regulates pressure when
  *Pcontrol*
  is greater than the value of the signal at port
  **Ps** and less than
  *Pmax*.
- `Constant`, the **Set
  pressure differential** parameter defines a
  constant set pressure.

### **Opening parameterization** — Opening parameterization `Linear` (default) | `Tabulated`

Method to parameterize the opening action of the valve.

### **Set pressure differential** — Range outside of which constant valve operation is triggered `0` `MPa` (default) | scalar

Magnitude of the pressure differential that triggers pressure compensation.

#### Dependencies

To enable this parameter, set **Set pressure control** to
`Constant`.

### **Pressure regulation range** — Valve operational pressure range `0.1` `MPa` (default) | scalar

Operational pressure range of the valve. The pressure regulation range defines the
difference between the **Set pressure differential**
parameter and the maximum valve operating pressure.

#### Dependencies

To enable this parameter, set **Opening parameterization** to
`Linear`.

### **Maximum opening area** — Area of fully open valve `1e-4` `m^2` (default) | positive scalar

Cross-sectional area of the valve in the fully open position.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to
`Linear`.

### **Leakage area** — Gap area when in fully closed position `1e-10` `m^2` (default) | positive scalar

Sum of all gaps when the valve is in the fully closed position. Any area smaller than
this value saturates to the specified leakage area. This value
contributes to numerical stability by maintaining continuity in the
flow.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to
`Linear`.

### **Pressure differential vector** — Differential pressure values for tabulated parameterization `[0.2 : 0.2 : 1.2]` `MPa` (default) | 1-by*n* vector

Vector of pressure differential values for the tabulated parameterization of the opening
area. The vector elements must correspond one-to-one to the values in
the **Opening area vector** parameter. The pressures
must be in ascending order.

#### Dependencies

To enable this parameter, set **Opening parameterization** to
`Tabulated`.

### **Opening area vector** — Valve opening areas for tabulated parameterization `[1e-05, 8e-06, 6e-06, 4e-06, 2e-06, 1e-10]` `m^2` (default) | 1-by*n* vector

Vector of opening area values for the tabulated parameterization of
the opening area. The vector elements must correspond one-to-one to the
values in the **Pressure differential vector**
parameter. For normally open valves, list elements in descending order.
For normally closed valves, list elements in ascending order.

The opening area vector must have the same number of elements as the
**Pressure differential vector**. The block uses
linear interpolation between table data points.

#### Dependencies

To enable this parameter, set **Opening parameterization** to
`Tabulated`.

### **Cross-sectional area at ports A and B** — Area at valve entry or exit `inf` `m^2` (default) | positive scalar

Cross-sectional area at the entry and exit ports **A** and
**B**. The block uses this area in the
pressure-flow rate equation that determines mass flow rate through the
valve.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor that accounts for discharge losses in theoretical flows.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the valve.

### **Pressure recovery** — Option to include pressure recovery `Off` (default) | `On`

Whether to account for pressure increase when fluid flows from a
region of a smaller cross-sectional area to a region of larger
cross-sectional area.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range of [0,1]

Continuous smoothing factor that introduces a layer of gradual change
to the flow response when the valve is in near-open or near-closed
positions. Set this value to a nonzero value less than one to increase
the stability of your simulation in these regimes.

#### Dependencies

To enable this parameter, set **Opening
parameterization** to
`Linear`.

### **Opening dynamics** — Option to simulate flow response to valve transitions `off` (default) | `on`

Whether to account for transient effects to the fluid system due to the valve opening.
When you select **Opening dynamics**, the block
approximates the opening conditions by introducing a first-order lag in
the flow response.

### **Opening time constant** — Valve opening time constant `0.1` `s` (default) | positive scalar

Time constant by which to compute the lag in the opening
dynamics.

#### Dependencies

To enable this parameter, select **Opening dynamics**.

### Faults

### **Pressure Compensator Valve Area fault** — Option to model valve area fault `Add fault`

Option to model a valve area fault in the block. To add a fault, click the **Add
fault** hyperlink. After a fault, the block sets the valve
area based on the value specified in the **Opening area when
faulted** parameter.

### **Opening area when faulted** — Faulted valve position `Closed` (default) | `Open` | `Maintain last value`

Faulted opening area. You can choose for the valve to seize when the valve is opened,
closed, or at the area after a fault.

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

The Pressure Compensator Valve (IL) block now supports the Simscape faults interface. To learn more,
see Introduction to Simscape Faults.

## Description

Pressure compensator valve in an isothermal liquid network

The Pressure Compensator Valve (IL) block represents a
pressure compensator in an isothermal liquid network, such as a pressure relief valve or
pressure-reducing valve. Use this valve to maintain the pressure at the valve based on
signals from another part of the system.

The pressure differential between ports **X** and **Y** is
the control pressure, *Pcontrol*. When this
value meets or exceeds the set pressure, the valve area opens or closes depending on the
**Valve specification** parameter. The pressure regulation range
begins at the set pressure, *Pset*. You can
choose between constant and controlled set pressure regulation. A physical signal at
port **Ps** provides a varying set pressure.

### Pressure Control

The block regulates pressure when
*Pcontrol* exceeds
*Pset*. The block continues to
regulate the pressure up to *Pmax*, the sum
of *Pset* and the pressure regulation range.
The block supports two modes of regulation:

- When you set **Set pressure control** to
  `Controlled` and connect a pressure signal
  to port **Ps**, the block keeps the pressure regulation
  range constant. The valve regulates pressure when
  *Pcontrol* is greater
  than the value of the signal at port **Ps** and less
  than *Pmax*.
- When you set **Set pressure control** to
  `Constant`, the **Set pressure
  differential** parameter defines a constant set
  pressure.

### Conservation of Mass

The block conserves mass such that

m˙A+m˙B=0.

The block calculates the mass flow rate through the valve as

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

where:

- *Cd* is the
  **Discharge coefficient** parameter.
- *Avalve* is the instantaneous
  valve open area.
- *Aport* is the
  **Cross-sectional area at ports A and B**
  parameter.
- ρ¯ is the average fluid density.
- *Δp* is the valve pressure difference
  *pA* –
  *pB*.

The critical pressure difference,
*Δpcrit*, is the pressure
differential specified by the **Critical Reynolds number**
parameter, *Recrit*. This parameter
represents the flow regime transition point between laminar and turbulent flow. The
block finds the critical pressure difference as

Δpcrit=πρ¯8Avalve(νRecritCd)2.

The pressure loss, *PRloss*, describes the
reduction of pressure in the valve due to a decrease in area. The block calculates
the pressure loss as:

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport.

The pressure recovery describes the positive pressure change in the valve due to
an increase in area. When you set **Pressure recovery** to
`Off`, the block sets
*PRloss* to 1.

The block calculates *Avalve* using the opening
parameterization and the valve opening dynamics.

### Valve Opening Parameterization

When you set **Opening parameterization** to
`Linear`, the valve area for normally open valves is

Avalve=p^(Aleak−Amax)+Amax.

This figure demonstrates how the block controls the opening area
for a normally open valve using the linear parameterization.

Pressure differential between ports X and Y with respect to opening area for a normally open valve using the linear parameterization

For normally closed valves, the block uses

Avalve=p^(Amax−Aleak)+Aleak.

This figure demonstrates how the block controls the opening area
for a normally closed valve using the linear parameterization.

Pressure differential between ports X and Y with respect to opening area for a normally closed valve using the linear parameterization

The normalized pressure, p^, is

p^=pcontrol−psetpmax−pset.

When the valve is in a near-open or near-closed
position in the linear parameterization, you can maintain numerical robustness in
your simulation by adjusting the **Smoothing factor** parameter.
If the **Smoothing factor** parameter is nonzero, the block
smoothly saturates the control pressure between
*pset* and
*pmax*. For more information, see
Numerical Smoothing.

When you set **Opening parameterization** to
`Tabulated`,
*Aleak* and
*Amax* are the first and last
parameters of the **Opening area vector** parameter, respectively.
The block calculates the opening area as

Avalve=tablelookup(pcontrol,TLU,ref,ATLU,pcontrol,interpolation=linear,extrapolation=nearest),

where:

- *pcontrol* is the control
  pressure, the pressure differential between ports **X**
  and **Y**.
- *pcontrol,TLU,ref*
  = *pTLU* +
  *poffset*.
- *pTLU* is the
  **Pressure differential vector** parameter.
- *poffset* is an internal
  pressure offset that causes the valve to start closing when
  *pcontrol,TLU,ref* =
  *pset*.
- *ATLU* is the
  **Opening area vector** parameter.

This figure demonstrates how the block controls the opening area for
a normally open valve using the tabulated parameterization.

Pressure differential between ports X and Y with respect to opening area for a normally open valve using the tabulated parameterization

This figure demonstrates how the block controls the opening area for a normally
closed valve using the tabulated parameterization.

Pressure differential between ports X and Y with respect to opening area for a normally closed valve using the tabulated parameterization

### Opening Dynamics

When you set **Opening dynamics** to `On`, the
block introduces a control pressure lag and replaces
*pcontrol* with the dynamic control
pressure, *pdyn*. The block calculates the
dynamic control pressure based on the **Opening time constant**
parameter, *τ*

p˙dyn=pcontrol−pdynτ.

By default, the block does not model **Opening
dynamics**. For the linear parameterization, a nonzero value for the
**Smoothing factor** parameter provides additional numerical
stability when the orifice is in near-closed or near-open position.

The block calculates the steady-state dynamics according to the **Opening
parameterization** parameter, and are based on the control pressure,
*pcontrol*.

### Faults

To model a fault, in the **Faults** section,
click the **Add fault** hyperlink next to the fault that you want to model. Use
the fault parameters to specify the fault properties. For more information about fault modeling,
see Introduction to Simscape Faults.

You can set the **Opening area when faulted** parameter to:

- `Closed` — The valve area stops at its
  smallest value, depending on the **Opening
  parameterization** parameter setting:

  - `Linear` — The valve area stops
    at the value of the **Leakage area**
    parameter.
  - `Tabulated` — The valve area
    stops at the smallest element of the **Opening area
    vector** parameter.
- `Open` — The valve stops at its largest
  value, depending on the **Opening parameterization**
  parameter setting:

  - `Linear` — The valve area stops
    at the value of the **Maximum opening
    area** parameter.
  - `Tabulated` — The valve area stops
    at the largest element of the **Opening area
    vector** parameter.
- `Maintain last value` — The valve area stops
  at the valve open area when the trigger occurred.

Due to numerical smoothing at the extremes of the valve area, the
minimum area the block uses is larger than the leakage area, and the maximum is
smaller than the value of the **Maximum orifice area** parameter.
This effect is in proportion to the amount of smoothing you apply.

After the fault triggers, the valve remains at the faulted area for the rest of the
simulation.
