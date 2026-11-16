---
type: simulink-block
title: 'Orifice (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Valves & Orifices'
documentation_page: 'orifice2p'
documentation_source_path: 'ref/orifice2p.html'
language: en
---

# Orifice (2P)

## Ports

### Conserving

### **A** — Fluid entry or exit two-phase fluid

Two-phase fluid conserving port associated with the fluid entry or
exit port.

### **B** — Fluid entry or exit two-phase fluid

Two-phase fluid conserving port associated with the fluid entry or
exit port.
### Input

### **S** — Control member position, m physical signal

Control member position that sets the orifice opening.

#### Dependencies

To enable this port, set **Orifice type** to
`Variable`.

## Parameters

### **Modeling option** — Modeling option for fluid phase `Liquid operating condition` (default) | `Vapor operating condition`

Modeling option for the fluid phase at the orifice. Set this parameter to
`Liquid operating condition` if the two-phase
fluid at the block location is in a liquid state. Set this parameter to
`Vapor operating condition` if the two-phase
fluid at the block location is in a vapor state.

### Parameters

### **Orifice type** — Constant or variable orifice `Variable` (default) | `Constant`

Type of orifice. When you set this parameter to `Variable`, the
orifice area varies according to the input signal received at port
**S**.

### **Orifice parameterization** — Variable or constant orifice parameterization `Linear - Area vs. control member position` (default) | `Orifice area` | `Nominal mass flow rate` | `Linear - Nominal mass flow rate vs. control member position` | `Tabulated data - Area vs. control member position` | `Cv flow coefficient` | `Kv flow coefficient`

Method the block uses to calculate the mass flow rate from the pressure difference
across the orifice or the pressure difference from the mass flow
rate.

When **Modeling option** is `Liquid
operating condition` and **Orifice
type** is `Variable`, the choices
for this parameter are:

- `Linear - Area vs. control member
  position`
- `Linear - Nominal mass flow rate vs. control
  member position`
- `Tabulated data - Area vs. control member
  position`

When **Modeling option** is `Liquid
operating condition` and **Orifice
type** is `Constant`, the choices
for this parameter are:

- `Orifice area`
- `Nominal mass flow rate`

When **Modeling option** is `Vapor operating
condition`, the choices for this parameter are:

- `Cv flow coefficient`
- `Kv flow coefficient`
- `Orifice area`

### **Nominal mass flow rate** — Rated mass flow rate `0.1` kg/s (default) | positive scalar

Typical, rated, or design mass flow rate through a constant
orifice.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition`,
**Orifice type** to
`Constant`, and **Orifice
parameterization** to `Nominal mass flow
rate`.

### **Nominal pressure drop** — Rated pressure drop `0.001` MPa (default) | positive scalar

Typical, rated, or design pressure drop through a constant
orifice.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition`,
**Orifice type** to
`Constant`, and **Orifice
parameterization** to `Nominal mass flow
rate`.

### **Nominal inlet condition specification** — Method of determining inlet fluid state `Temperature` (default) | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

Method of determining the inlet fluid state. The block determines the orifice nominal
inlet specific volume from the tabulated fluid properties data based on
the value of the **Nominal inlet pressure** parameter
and the setting of the **Nominal inlet condition
specification** parameter.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition` and either:

- **Orifice type** to
  `Constant` and
  **Orifice parameterization** to
  `Nominal mass flow
  rate`.
- **Orifice type** to
  `Variable` and
  **Orifice parameterization** to
  `Linear - Nominal mass flow rate vs.
  control member position`.

### **Nominal inlet pressure** — Inlet fluid pressure `0.101325` MPa (default) | positive scalar

Inlet pressure in nominal conditions. The block determines the inlet specific volume
from the tabulated fluid properties data based on the value of the
**Nominal inlet pressure** parameter and the
setting of the **Nominal inlet condition
specification** parameter.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition` and either:

- **Orifice type** to
  `Constant` and
  **Orifice parameterization** to
  `Nominal mass flow
  rate`.
- **Orifice type** to
  `Variable` and
  **Orifice parameterization** to
  `Linear - Nominal mass flow rate vs.
  control member position`.

### **Nominal inlet temperature** — Fluid temperature `293.15` K (default) | positive scalar

Inlet fluid temperature in nominal operating conditions.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition` and either:

- **Orifice type** to
  `Constant`,
  **Orifice parameterization** to
  `Nominal mass flow rate`,
  and **Nominal inlet condition
  specification** to
  `Temperature`.
- **Orifice type** to
  `Variable`,
  **Orifice parameterization** to
  `Linear - Nominal mass flow rate vs.
  control member position`, and
  **Nominal inlet condition
  specification** to
  `Temperature`.

### **Nominal inlet vapor quality** — Inlet vapor quality mass fraction `0` (default) | positive scalar in the range [0,1]

Inlet mixture vapor quality by mass fraction in nominal operating
conditions. A value of `0` means that the inlet fluid
is subcooled liquid. A value of `1` means that the
inlet fluid is superheated vapor.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition` and either:

- **Orifice type** to
  `Constant`,
  **Orifice parameterization** to
  `Nominal mass flow rate`,
  and **Nominal inlet condition
  specification** to `Vapor
  quality`.
- **Orifice type** to
  `Variable`,
  **Orifice parameterization** to
  `Linear - Nominal mass flow rate vs.
  control member position`, and
  **Nominal inlet condition
  specification** to `Vapor
  quality`.

### **Nominal inlet vapor void fraction** — Inlet volume fraction `0` (default) | positive scalar in the range [0,1]

Inlet mixture volume fraction in nominal operating conditions. A value
of `0` means that the inlet fluid is subcooled liquid.
A value of `1` means that the inlet fluid is
superheated vapor.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition` and either:

- **Orifice type** to
  `Constant`,
  **Orifice parameterization** to
  `Nominal mass flow rate`,
  and **Nominal inlet condition
  specification** to `Vapor void
  fraction`.
- **Orifice type** to
  `Variable`,
  **Orifice parameterization** to
  `Linear - Nominal mass flow rate vs.
  control member position`, and
  **Nominal inlet condition
  specification** to `Vapor void
  fraction`.

### **Nominal inlet specific enthalpy** — Inlet fluid specific enthalpy `400` kJ/kg (default) | positive scalar

Inlet specific enthalpy in nominal operating conditions.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition` and either:

- **Orifice type** to
  `Constant`,
  **Orifice parameterization** to
  `Nominal mass flow rate`,
  and **Nominal inlet condition
  specification** to `Specific
  enthalpy`.
- **Orifice type** to
  `Variable`,
  **Orifice parameterization** to
  `Linear - Nominal mass flow rate vs.
  control member position`, and
  **Nominal inlet condition
  specification** to `Specific
  enthalpy`.

### **Nominal inlet specific internal energy** — Inlet specific internal energy `400` kJ/kg (default) | positive scalar

Inlet specific internal energy in nominal operating conditions.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition` and either:

- **Orifice type** to
  `Constant`,
  **Orifice parameterization** to
  `Nominal mass flow rate`,
  and **Nominal inlet condition
  specification** to `Specific
  internal energy`.
- **Orifice type** to
  `Variable`,
  **Orifice parameterization** to
  `Linear - Nominal mass flow rate vs.
  control member position`, and
  **Nominal inlet condition
  specification** to `Specific
  internal energy`.

### **Orifice area** — Area of orifice opening `1e-4` `m^2` (default) | positive scalar

Cross-sectional area of the orifice opening.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Constant` and **Orifice
parameterization** to `Orifice
area`.

### **Control member position at closed orifice** — Control member offset `0` m (default) | positive scalar

Control member offset, or the value at **S** when the
orifice is fully closed.

#### Dependencies

To enable this parameter, set either:

- **Modeling option** to
  `Liquid operating
  condition`, **Orifice
  type** to
  `Variable`, and
  **Orifice parameterization** to
  `Linear – Nominal mass flow rate vs.
  control member position` or
  `Linear – Area vs. control member
  position`.
- **Modeling option** to
  `Vapor operating
  condition`, **Orifice
  type** to
  `Variable`, and
  **Opening characteristic** to
  `Linear`.

### **Control member travel between closed and open orifice** — Control member stroke `5e-3` m (default) | positive scalar

Distance the control member travels between a closed and open orifice.
When you set **Opening orientation** to
`Positive control member displacement opens
orifice`, the orifice is fully open at the sum of the
**Control member position at closed orifice** and
**Control member travel between closed and open
orifice** parameters. When you set **Opening
orientation** to `Negative control member
displacement opens orifice`, the orifice is fully open
at the difference between the **Control member position at
closed orifice** and **Control member travel
between closed and open orifice** parameters.

#### Dependencies

To enable this parameter, set either:

- **Modeling option** to
  `Liquid operating
  condition`, **Orifice
  type** to
  `Variable`, and
  **Orifice parameterization** to
  `Linear – Nominal mass flow rate vs.
  control member position` or
  `Linear – Area vs. control member
  position`.
- **Modeling option** to
  `Vapor operating
  condition`, **Orifice
  type** to
  `Variable`, and
  **Opening characteristic** to
  `Linear`.

### **Opening orientation** — Direction of displacement that opens the orifice `Positive control member displacement opens orifice` (default) | `Negative control member displacement opens orifice`

Direction of the member displacement that opens the variable orifice. A positive
orientation means that an increase in the signal at
**S** opens the orifice. A negative orientation
means that a decrease in the signal at **S** opens the
orifice.

#### Dependencies

To enable this parameter, set either:

- **Modeling option** to
  `Liquid operating
  condition`, **Orifice
  type** to
  `Variable`, and
  **Orifice parameterization** to
  `Linear – Nominal mass flow rate vs.
  control member position` or
  `Linear – Area vs. control member
  position`.
- **Modeling option** to
  `Vapor operating
  condition`, **Orifice
  type** to
  `Variable`, and
  **Opening characteristic** to
  `Linear`.

### **Nominal mass flow rate at maximum orifice opening** — Rated mass flow rate `0.1` kg/s (default) | positive scalar

Mass flow rate through a fully open orifice under typical, design, or
rated conditions.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition`,
**Orifice type** to
`Variable`, and **Orifice
parameterization** to `Linear – Nominal
mass flow rate vs. control member position`.

### **Nominal pressure drop at maximum orifice opening** — Rated pressure drop `0.001` MPa (default) | positive scalar

Pressure drop over a fully open orifice under typical, design, or
rated conditions.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition`,
**Orifice type** to
`Variable`, and **Orifice
parameterization** to `Linear – Nominal
mass flow rate vs. control member position`.

### **Maximum orifice area** — Maximum orifice opening area `1e-4 m^2` (default) | positive scalar

Orifice area when it is fully open.

#### Dependencies

To enable this parameter, set either:

- **Modeling option** to
  `Liquid operating
  condition`, **Orifice
  type** to
  `Variable`, and
  **Orifice parameterization** to
  `Linear – Area vs. control member
  position`.
- **Modeling option** to
  `Vapor operating
  condition`, **Orifice
  type** to
  `Variable`,
  **Orifice parameterization** to
  `Orifice area`, and
  **Opening characteristic** to
  `Linear`.

### **Control member position vector** — Vector of control member positions `[0, .002, .004, .007, .017] m` (default) | 1-by-*n* vector

Vector of control member positions for the tabulated orifice parameterizations. The
vector elements correspond one-to-one to the values in the
**Orifice area vector**, **Cv flow
coefficient vector**, or **Kv flow coefficient
vector** parameters.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable` and either

- **Modeling option** to
  `Liquid operating
  condition` and **Orifice
  parameterization** to
  `Tabulated data - Area vs. control
  member position`.
- **Modeling option** to
  `Vapor operating condition`
  and **Opening characteristic** to
  `Tabulated`.

### **Orifice area vector** — Vector of orifice opening area values `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of orifice area values for the tabulated parameterization of the orifice area.
The values in this vector correspond one-to-one with the elements in the
**Control member position vector** parameter.

#### Dependencies

To enable this parameter, set either

- **Modeling option** to
  `Liquid operating
  condition`, **Orifice
  type** to
  `Variable`, and
  **Orifice parameterization** to
  `Tabulated data - Area vs. control
  member position`.
- **Modeling option** to
  `Vapor operating
  condition`, **Orifice
  type** to
  `Variable`,
  **Orifice parameterization** to
  `Orifice area`, and
  **Opening characteristic** to
  `Tabulated`.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Ratio of actual flow rate to ideal flow rate. This parameter accounts for real-world
losses that are not captured in the orifice equation.

#### Dependencies

To enable this parameter, set either:

- **Orifice type** to
  `Constant` and
  **Orifice parameterization** to
  `Orifice area`.
- **Modeling option** to
  `Liquid operating
  condition`, **Orifice
  type** to
  `Variable` and
  **Orifice parameterization** to
  either `Linear - Area vs. control member
  position` or `Tabulated
  data - Area vs. control member
  position`.
- **Modeling option** to
  `Vapor operating
  condition`, **Orifice
  type** to
  `Variable` and
  **Orifice parameterization** to
  `Orifice area`.

### **Pressure recovery** — Whether to account for pressure increase in area expansions `off` (default) | `on`

Whether to account for the small rise in pressure after the pressure drop from the inlet
to the orifice hole. When the fluid jet exits the orifice hole, it
dissipates and expands to fill the port area, which causes this small
pressure rise. The block does not model this pressure increase when you
clear the **Pressure recovery** check box.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition` and either:

- **Orifice type** to
  `Variable` and
  **Orifice parameterization** to
  either `Linear - Area vs. control member
  position` or `Tabulated
  data - Area vs. control member
  position`.
- **Orifice type** to
  `Constant` and
  **Orifice parameterization** to
  `Orifice area`.

### **Opening characteristic** — Method to convert from control signal to measure of flow capacity `Linear` (default) | `Tabulated`

Method by which to convert the control signal specified at port
**S** to the chosen measure of flow
capacity.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Vapor operating condition` and
**Orifice type** to
`Variable`.

### **Cv flow coefficient** — Flow coefficient `4` (default) | positive scalar

Value of the constant *Cv*
flow coefficient. This parameter measures the ease with which the vapor
traverses the resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Vapor operating condition`,
**Orifice type** to
`Constant`, and **Orifice
parameterization** to `Cv flow
coefficient`.

### **Maximum Cv flow coefficient** — *Cv* coefficient that corresponds to maximally open component `4` (default) | positive scalar

Value of the *Cv* flow
coefficient when the orifice is fully open and the area available for
flow is at a maximum. This parameter measures the ease with which the
vapor traverses the resistive element when driven by a pressure
differential.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Vapor operating condition`,
**Orifice type** to
`Variable`, **Orifice
parameterization** to `Cv flow
coefficient`, and **Opening
characteristic** to
`Linear`.

### **Cv flow coefficient vector** — *Cv* coefficients that correspond to values in member position vector `[1e-06, .8, 1.6, 2.4, 3.2, 4]` (default) | 1-by-*n* vector

Vector of *Cv* flow
coefficients. Each coefficient corresponds to a value in the
**Control member position vector** parameter. This
parameter measures the ease with which the vapor traverses the resistive
element when driven by a pressure differential. The size of the vector
must be the same as the **Control member position
vector** parameter.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Vapor operating condition`,
**Orifice type** to
`Variable`, **Orifice
parameterization** to `Cv flow
coefficient`, and **Opening
characteristic** to
`Tabulated`.

### **Kv flow coefficient** — Flow coefficient `3.6` (default) | positive scalar

Value of the constant *Kv*
flow coefficient. This parameter measures the ease with which the vapor
traverses the resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Vapor operating condition`,
**Orifice type** to
`Constant`, and **Orifice
parameterization** to `Kv flow
coefficient`.

### **Maximum Kv flow coefficient** — *Kv* coefficient that corresponds to maximally open component `3.6` (default) | positive scalar

Value of the *Kv* flow
coefficient when the orifice is fully open and the area available for
flow is at a maximum. This parameter measures the ease with which the
vapor traverses the resistive element when driven by a pressure
differential.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Vapor operating condition`,
**Orifice type** to
`Variable`, **Orifice
parameterization** to `Kv flow
coefficient`, and **Opening
characteristic** to
`Linear`.

### **Kv flow coefficient vector** — *Kv* coefficients that correspond to values in member position vector `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` (default) | 1-by-*n* vector

Vector of *Kv* flow
coefficients. Each coefficient corresponds to a value in the
**Control member position vector** parameter. This
parameter measures the ease with which the vapor traverses the resistive
element when driven by a pressure differential. The size of the vector
must be the same as the **Control member position
vector** parameter.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Vapor operating condition`,
**Orifice type** to
`Variable`, **Orifice
parameterization** to `Kv flow
coefficient`, and **Opening
characteristic** to
`Tabulated`.

### **xT pressure differential ratio factor at choked flow** — Ratio of pressure differentials `0.7` (default) | positive scalar

Ratio between the inlet pressure,
*pin*, and the outlet
pressure, *pout*, defined as (pin−pout)/pin where choking first occurs.

#### Dependencies

To enable this parameter, **Modeling option** to `Vapor
operating condition` and **Orifice
parameterization** to `Cv flow
coefficient` or `Kv flow
coefficient`.

### **Leakage flow fraction** — Ratio of flow rates `1e-6` (default) | positive scalar

Ratio of the flow rate of the orifice when it is closed to when it is
open.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable` and any combination of other
parameters, except when:

- **Modeling option** is
  `Liquid operating
  condition` and **Orifice
  parameterization** is
  `Tabulated data - Area vs. control
  member position`.
- **Modeling option** is
  `Vapor operating condition`
  and **Opening characteristic** is
  `Tabulated`.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change
to the flow response when the orifice is in near-open or near-closed
positions. Set this parameter to a nonzero value less than one to
increase the stability of your simulation in these regions.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable` and any combination of other
parameters, except when:

- **Modeling option** is
  `Liquid operating
  condition` and **Orifice
  parameterization** is
  `Tabulated data - Area vs. control
  member position`.
- **Modeling option** is
  `Vapor operating condition`
  and **Opening characteristic** is
  `Tabulated`.

### **Inlet phase change time constant** — Lag for liquid specific volume `0.1` s (default) | positive scalar

Time lag for liquid-vapor mixtures in computing the fluid specific
volume.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition`.

### **Laminar flow pressure ratio** — Laminar-turbulent transition pressure ratio `0.999` (default) | positive scalar

Ratio of the orifice outlet pressure to orifice inlet pressure at
which the fluid transitions between the laminar and turbulent regimes.
The pressure loss corresponds to the mass flow rate linearly in laminar
flows and quadratically in turbulent flows.

### **Cross-sectional area at ports A and B** — Valve port areas `0.01` m^2 (default) | positive scalar

Area of the orifice ports **A** and
**B**.

## Libraries

Simscape / Fluids / Two-Phase Fluid / Valves & Orifices

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

### R2024a: Model vapor or liquid valves

You can now use the **Modeling option** parameter to specify an
orifice when the two-phase fluid is in a vapor or liquid state. Both modeling
options also include new orifice parameterizations.

When **Modeling option** is `Liquid operating
condition`, you can now set **Orifice
parameterization** to:

- `Linear - Area vs. control member
  position`
- `Tabulated data - Area vs. control member
  position`
- `Orifice area`

When **Modeling option** is `Vapor operating
condition`, you can now set **Orifice
parameterization** to:

- `Cv flow coefficient`
- `Kv flow coefficient`
- `Orifice area`

To preserve the constant orifice behavior from previous releases, set **Modeling
option** to `Liquid operating condition` and
**Orifice parameterization** to `Nominal mass flow
rate`. To preserve the variable orifice behavior from previous
releases, set **Modeling option** to `Liquid operating
condition` and **Orifice parameterization** to
`Linear – Nominal mass flow rate vs. control member
position`.

## Description

Constant- or variable-area orifice in a two-phase fluid network

The Orifice (2P) block models pressure loss due to a constant or variable area orifice in a
two-phase fluid network. The **Modeling option** parameter controls the
parameterization options for a valve designed for modeling either vapor or liquid, but
does not impact the fluid properties. The block calculates fluid properties inside the
valve from inlet conditions. There is no heat exchange between the fluid and the
environment, and therefore phase change inside the orifice only occurs due to a pressure
drop or a propagated phase change from another part of the model.

The orifice can be constant or variable. When **Orifice type** is
`Variable`, the physical signal at port
**S** sets the position of the control member, which opens and
closes the orifice.

### Liquid Orifice

When **Modeling option** is `Liquid operating
condition`, the block parameterizations depend on the value of the
**Orifice type** parameter. The block calculates the pressure
loss and pressure recovery in the same way for all liquid parameterization
options.

The block accounts for pressure loss by using the ratio of the pressure loss across the
whole orifice to the pressure drop immediately across the orifice plate. This ratio,
*PRloss*, is

PRloss=1−(AorificeAport)2(1−Cd2)−CdAorificeAport1−(AorificeAport)2(1−Cd2)+CdAorificeAport,

where:

- *Cd* is the value of the
  **Discharge coefficient** parameter.
- *Aorifice* is the
  instantaneous orifice open area.
- *Aport* is the value of the
  **Cross-sectional area at ports A and B**
  parameter.

The pressure recovery is the positive pressure change in the valve due to an increase in
area after the orifice hole. If you do not want to capture this increase in
pressure, clear the **Pressure recovery** check box. In this case,
*PRloss* is 1, which reduces the
model complexity. Clear this setting if the orifice hole is quite small relative to
the port area or if the next downstream component is close to the block and any jet
does not have room to dissipate.

The critical pressure difference, *Δpcrit*, is the
pressure differential where the flow transitions between laminar and turbulent
flow,

Δpcrit=(pA+pB)2(1−Blam),

where:

- *pA* and
  *pB* are the pressure at
  port **A** and **B**, respectively.
- *Blam* is the value of the
  **Laminar flow pressure ratio** parameter.

**Nominal Mass Flow Rate Parameterization**

When you set **Orifice type** to `Constant` and
**Orifice Parameterization** to `Nominal mass
flow rate`, the mass flow rate through the orifice is

m˙=m˙nom[vnom2Δpnom]2vinΔp(Δp2+Δpcrit2)0.25,

where:

- m˙nom is the value of the **Nominal mass flow
  rate** parameter.
- *Δpnom* is the value of
  the **Nominal pressure drop rate**
  parameter.
- *vnom* is the nominal
  inlet specific volume. The block determines this value from the
  tabulated fluid properties data based on the value of the
  **Nominal inlet condition specification**
  parameter.
- *vin* is the inlet
  specific volume.

**Liquid Orifice Area Parameterization**

When you set **Orifice type** to `Constant` and
**Orifice Parameterization** to `Orifice
area`, the block calculates the mass flow rate as

m˙=CdAorifice2vinPRloss(1−(AorificeAport)2)Δp≈CdAorifice22vinPRloss(1−(AorificeAport)2)Δp[Δp2+Δpcrit]1/4,

where *Δp* is the pressure drop over the
orifice, *pA ̶
pB*.

**Linear - Nominal Mass Flow Rate vs. Control Member Position
Parameterization**

When you set **Orifice type** to `Variable` and
**Orifice Parameterization** to `Nominal mass
flow rate vs. control member position`, the mass flow rate
through the variable-area orifice is

m˙=λm˙nom[vnom2Δpnom]2vinΔp(Δp2+Δpcrit2)0.25,

where *λ* is the orifice opening fraction,
which is a fraction of the total orifice open area.

The block determines the orifice opening for all variable orifice
parameterizations as

λ=ε(1−fleak)(S−Smin)ΔS+fleak,

where:

- *ε* is `1` when
  **Opening orientation** is
  `Positive control member displacement opens
  orifice` and `-1` when
  **Opening orientation** is
  `Negative control member displacement opens
  orifice`.
- *fleak* is the value of
  the **Leakage flow fraction** parameter.
- *S* is th value of the signal at port
  **S**.
- *Smin* is the value of the
  **Control member position at closed orifice**
  parameter.
- *ΔS* is the value of the **Control member
  travel between closed and open orifice** parameter.

**Linear - Area vs. Control Member Position Parameterization**

When you set **Orifice type** to
`Variable` and **Orifice
Parameterization** to `Linear - Area vs. control member
position`, the orifice area is

Aorifice=λAmax,

where *Amax* is the
value of the **Maximum orifice area** parameter.

The mass flow rate is

m˙=CdAorifice2vinPRloss(1−(AorificeAport)2)Δp[Δp2+Δpcrit2]1/4.

When the orifice is in a near-open or near-closed
position, you can maintain numerical robustness in your simulation by adjusting
the **Smoothing factor** parameter. If the
**Smoothing factor** parameter is nonzero, the block
smoothly saturates the opening area between
*Aleak* and
*Amax*, where
*Aleak =
fleakAmax*. For
more information, see Numerical Smoothing.

**Tabulated Data - Area vs. Control Member Position Parameterization**

When you set **Orifice type** to `Variable` and
**Orifice Parameterization** to `Tabulated data
- Area vs. control member position`, the block interpolates the
orifice area, *Aorifice*, from the
**Orifice area vector** and **Control member
position vector** parameters. The signal at port
**S** specifies the control member position. The block uses
linear interpolation to query between the data points and nearest extrapolation
for points beyond the table boundaries.

The block uses the same equation as the `Linear - Area vs. control member
position` setting to calculate the volumetric flow
rate.

**Fluid Specific Volume Dynamics**

For all parameterizations, the block calculates the fluid specific volume during
simulation based on the liquid state.

If the fluid at the orifice inlet is a liquid-vapor mixture, the block
calculates the specific volume as

vin=(1−xdyn)vliq+xdynvvap,

where:

- *xdyn* is the inlet vapor
  quality. The block applies a first-order lag to the inlet vapor
  quality of the mixture.
- *vliq* is the liquid
  specific volume of the fluid.
- *vvap* is the vapor
  specific volume of the fluid.

If the inlet fluid is liquid or vapor,
*vin* is the respective liquid
or vapor specific volume.

If the inlet vapor quality is a liquid-vapor mixture, the block applies a first-order time lag,

dxdyndt=xin−xdynτ,

where:

- *xdyn* is the dynamic
  vapor quality.
- *xin* is the current inlet
  vapor quality.
- *τ* is the value of the **Inlet phase
  change time constant** parameter.

If the inlet fluid is a subcooled liquid,
*xin = 0*. If the inlet fluid is
a superheated vapor, *xin = 1*.

### Vapor Orifice

When **Modeling option** is `Vapor operating
condition`, the block behavior depends on the **Orifice
type**, **Orifice parameterization**, and
**Opening characteristic** parameters.

**Variable Vapor Orifice**

When you set **Orifice type** to `Variable` and
**Opening characteristic** to
`Linear`, the block uses the input at port
**S** to calculate the orifice opening,

λ=ε(1−fleak)(S−Smin)ΔS+fleak,

where *S* is the value of the signal at port
**S**, and *Smin*
and *ΔS* are the values of the **Control member
position at closed orifice** and **Control member travel
between closed and open orifice** parameters, respectively.

When you set **Orifice type** to
`Variable` and **Opening
characteristic** to `Tabulated`, the block
interpolates the orifice characteristics from the **Control member
position vector** parameter and the input at port **S**.

For a variable orifice, the flow rate in the orifice depends on the
**Opening characteristic** parameter:

- `Linear` — The measure of flow capacity is
  proportional to the control signal at port **S**. As the control signal increases, the measure of flow
  capacity scales from the specified minimum to the specified
  maximum.

  When you set **Orifice parameterization** to
  `Cv flow coefficient` or `Kv
  flow coefficient`, the block treats the parameter
  **xT pressure differential ratio factor at choked
  flow** as a constant independent of the control signal.
- `Tabulated` — The block calculates the
  measure of flow capacity as a function of the control signal at port
  **S**. This function uses a
  one-dimensional lookup table.

  When you set **Orifice parameterization** to
  `Cv flow coefficient` or `Kv
  flow coefficient`, the block treats the parameter
  **xT pressure differential ratio factor at choked
  flow** as a function of the control signal.

**Cv Flow Coefficient Parameterization**

When you set **Orifice parametrization** to `Cv
flow coefficient`, the mass flow rate is

m˙=CvN6Y(pin−pout)vin,

where:

- *Cv* is the flow
  coefficient.
- *N6* is a constant equal
  to 27.3 when mass flow rate is in kg/hr, pressure is in bar, and
  density is in kg/m3.
- *Y* is the expansion factor.
- *pin* is the inlet
  pressure.
- *pout* is the outlet
  pressure.
- *vin* is the inlet
  specific volume.

The expansion factor is

Y=1−pin−pout3pinFγxT,

where:

- *Fγ* is the ratio of the
  isentropic exponent to 1.4.
- *xT* is the value of the
   **xT pressure differential ratio factor at choked
  flow** parameter.

The block smoothly transitions to a linearized form of the equation when the
pressure ratio, pout/pin, rises above the value of the **Laminar flow pressure
ratio** parameter,
*Blam*,

m˙=CvN6Ylam1pavg(1−Blam)vavg(pin−pout),

where:

Ylam=1−1−Blam3FγxT.

When the pressure ratio, pout/pin, falls below 1−FγxT, the orifice becomes choked and the block uses the equation

m˙=23CvN6FγxTpinvin.

**Kv Flow Coefficient Parameterization**

When you set **Orifice parametrization** to `Kv flow
coefficient`, the block uses the same equations as the
`Cv flow coefficient` parametrization, but replaces
*Cv* with
*Kv* using the relation Kv=0.865Cv.

**Vapor Orifice Area Parameterization**

When you set **Orifice parametrization** to
`Orifice area`, the mass flow rate is

m˙=CdAorifice2γγ−1pin1vin(poutpin)2γ[1−(poutpin)γ−1γ1−(AorificeAport)2(poutpin)2γ],

where:

- *Cd* is the value of
  the **Discharge coefficient** parameter.
- *γ* is the isentropic exponent.

The block smoothly transitions to a linearized form of the equation when
the pressure ratio, pout/pin, rises above the value of the **Laminar flow
pressure ratio** parameter,
*Blam*,

m˙=CdAorifice2γγ−1pavg2−γγ1vavgBlam2γ[1− Blamγ−1γ1−(AorificeAport)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

When the pressure ratio, pout/pin, falls below(2γ+1)γγ−1 , the orifice becomes choked and the block uses the
equation

m˙=CdAorifice2γγ+1pin1vin1(γ+12)2γ−1−(AorificeAport)2.

### Mass Balance

Mass is conserved in the orifice,

m˙A+m˙B=0,

where:

- m˙A is the mass flow rate at port
  **A**.
- m˙B is the mass flow rate at port
  **B**.

### Energy Balance

Energy is conserved in the orifice,

ΦA+ΦB=0,

where:

- *ΦA* is the energy flow at
  port **A**.
- *ΦB* is the energy flow at
  port **B**.

### Assumptions and Limitations

- There is no heat exchange between the valve and the
  environment.
- When **Modeling option** is `Liquid
  operating condition`, the results may not be accurate
  outside of the subcooled liquid region. When **Modeling
  option** is `Vapor operating
  condition`, the results may not be accurate outside of
  the superheated vapor region. To model an orifice in a liquid-vapor
  mixture, set **Modeling option** to `Liquid
  operating condition`.
