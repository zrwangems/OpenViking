---
type: simulink-block
title: 'Check Valve (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Valves & Orifices / Directional Control Valves'
documentation_page: 'checkvalve2p'
documentation_source_path: 'ref/checkvalve2p.html'
language: en
---

# Check Valve (2P)

## Ports
```yaml
ports:
- name: A
  summary: Fluid entry two-phase fluid
  direction: conserving
- name: B
  summary: Fluid exit two-phase fluid
  direction: conserving
```

### Conserving

### **A** — Fluid entry two-phase fluid

Two-phase fluid conserving port associated with the fluid entry
port.

### **B** — Fluid exit two-phase fluid

Two-phase fluid conserving port associated with the fluid exit
port.
## Parameters
```yaml
parameters:
- name: Modeling option
  summary: Modeling option for fluid phase Liquid operating condition (default) | Vapor operating condition
  group: ''
- name: Valve parameterization
  summary: Model for valve parameterization Linear - Area vs. pressure (default) | Linear - Nominal mass flow rate vs. pressure
    | Tabulated data - Area vs. pressure | Cv flow coefficient | Kv flow coefficient | Orifice area
  group: Parameters
- name: Opening pressure specification
  summary: Control pressure Pressure differential (default) | Gauge pressure at port A
  group: Parameters
- name: Cracking pressure (gauge)
  summary: Cracking pressure 0.1 MPa (default) | positive scalar
  group: Parameters
- name: Maximum opening pressure (gauge)
  summary: Pressure that fully opens the valve 0.2 MPa (default) | positive scalar
  group: Parameters
- name: Cracking pressure differential
  summary: Cracking pressure 0.01 MPa (default) | positive scalar
  group: Parameters
- name: Maximum opening pressure differential
  summary: Maximum valve operational pressure 0.1 MPa (default) | positive scalar
  group: Parameters
- name: Nominal mass flow rate at maximum valve opening
  summary: Rated mass flow rate 0.1 kg/s (default) | positive scalar
  group: Parameters
- name: Nominal pressure drop at maximum valve opening
  summary: Rated pressure drop 0.001 MPa (default) | positive scalar
  group: Parameters
- name: Nominal inlet condition specification
  summary: Method of determining inlet fluid state Temperature (default) | Vapor quality | Vapor void fraction | Specific
    enthalpy | Specific internal energy
  group: Parameters
- name: Nominal inlet pressure
  summary: Inlet fluid pressure 0.101325 MPa (default) | positive scalar
  group: Parameters
- name: Nominal inlet temperature
  summary: Fluid temperature 293.15 K (default) | positive scalar
  group: Parameters
- name: Nominal inlet vapor quality
  summary: Inlet vapor quality mass fraction 0 (default) | positive scalar in the range [0,1]
  group: Parameters
- name: Nominal inlet vapor void fraction
  summary: Inlet volume fraction 0 (default) | positive scalar in the range [0,1]
  group: Parameters
- name: Nominal inlet specific enthalpy
  summary: Inlet fluid specific enthalpy 400 kJ/kg (default) | positive scalar
  group: Parameters
- name: Nominal inlet specific internal energy
  summary: Inlet specific internal energy 400 kJ/kg (default) | positive scalar
  group: Parameters
- name: Maximum valve area
  summary: Maximum valve opening area 1e-4 m^2 (default) | positive scalar
  group: Parameters
- name: Opening pressure differential vector
  summary: 'Vector of pressure differentials [0.2 : 0.2 : 1.2] MPa (default) | 1-by-*n* vector'
  group: Parameters
- name: Opening pressure (gauge) vector
  summary: 'Vector of gauge pressures [0.2 : 0.2 : 1.2] MPa (default) | 1-by-*n* vector'
  group: Parameters
- name: Valve area vector
  summary: Vector of valve opening area values [1e-10, 2e-06, 4e-06, 6e-06, 8e-06, 1e-05] m^2 (default) | 1-by-*n* vector
  group: Parameters
- name: Discharge coefficient
  summary: Discharge coefficient 0.64 (default) | positive scalar
  group: Parameters
- name: Pressure recovery
  summary: Whether to account for pressure increase in area expansions off (default) | on
  group: Parameters
- name: Opening characteristic
  summary: Method to parameterize measure of flow capacity Linear (default) | Tabulated
  group: Parameters
- name: Maximum Cv flow coefficient
  summary: '*Cv* coefficient that corresponds to maximally open component 4 (default) | positive scalar'
  group: Parameters
- name: Cv flow coefficient vector
  summary: '*Cv* coefficients that correspond to values in member position vector [1e-06, .8, 1.6, 2.4, 3.2, 4] (default)
    | 1-by-*n* vector'
  group: Parameters
- name: Maximum Kv flow coefficient
  summary: '*Kv* coefficient that corresponds to maximally open component 3.6 (default) | positive scalar'
  group: Parameters
- name: Kv flow coefficient vector
  summary: '*Kv* coefficients that correspond to values in member position vector [1e-06, .72, 1.44, 2.16, 2.88, 3.6] (default)
    | 1-by-*n* vector'
  group: Parameters
- name: xT pressure differential ratio factor at choked flow
  summary: Ratio of pressure differentials 0.7 (default) | positive scalar
  group: Parameters
- name: Maximum orifice area
  summary: Maximum valve opening area 1e-4 m^2 (default) | positive scalar
  group: Parameters
- name: Orifice area vector
  summary: Vector of valve opening area values [1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2 (default) | 1-by-*n* vector
  group: Parameters
- name: Leakage flow fraction
  summary: Ratio of flow rates 1e-6 (default) | positive scalar
  group: Parameters
- name: Smoothing factor
  summary: Numerical smoothing factor 0.01 (default) | positive scalar in the range [0,1]
  group: Parameters
- name: Inlet phase change time constant
  summary: Lag for liquid specific volume 0.1 s (default) | positive scalar
  group: Parameters
- name: Laminar flow pressure ratio
  summary: Laminar-turbulent transition pressure ratio 0.999 (default) | positive scalar
  group: Parameters
- name: Cross-sectional area at ports A and B
  summary: Valve port areas 0.01 m^2 (default) | positive scalar
  group: Parameters
```

### **Modeling option** — Modeling option for fluid phase `Liquid operating condition` (default) | `Vapor operating condition`

Modeling option for the fluid phase at the valve. Set this parameter to
`Liquid operating condition` if the two-phase
fluid at the block location is in a liquid state. Set this parameter to
`Vapor operating condition` if the two-phase
fluid at the block location is in a vapor state.

### Parameters

### **Valve parameterization** — Model for valve parameterization `Linear - Area vs. pressure` (default) | `Linear - Nominal mass flow rate vs. pressure` | `Tabulated data - Area vs. pressure` | `Cv flow coefficient` | `Kv flow coefficient` | `Orifice area`

Method the block uses to calculate the mass flow rate from the pressure difference
across the valve or the pressure difference from the mass flow
rate.

When **Modeling option** is `Liquid
operating condition`, the choices for this parameter are:

- `Linear - Area vs.
  pressure`
- `Linear - Nominal mass flow rate vs.
  pressure`
- `Tabulated data - Area vs.
  pressure`

When **Modeling option** is `Vapor operating
condition`, the choices for this parameter are:

- `Cv flow coefficient`
- `Kv flow coefficient`
- `Orifice area`

### **Opening pressure specification** — Control pressure `Pressure differential` (default) | `Gauge pressure at port A`

Control pressure specification:

- When this parameter is `Pressure
  differential`, the valve opens when
  *pA ̶
  pB* exceeds the
  **Cracking pressure differential**.
- When this parameter is `Gauge pressure at port
  A`, the valve opens when
  *pA ̶
  patm* exceeds the
  **Cracking pressure (gauge)**.

### **Cracking pressure (gauge)** — Cracking pressure `0.1` MPa (default) | positive scalar

Valve pressure threshold. When the control pressure,
*pA ̶
patm*, exceeds the opening pressure,
the valve begins to open.

#### Dependencies

To enable this parameter, set **Opening pressure
specification** to `Gauge pressure at port
A` and either:

- **Modeling option** to
  `Liquid operating
  condition` and **Valve
  parameterization** to `Linear -
  Area vs. pressure` or
  `Linear - Nominal mass flow rate vs.
  pressure`.
- **Modeling option** to
  `Vapor operating condition`
  and **Opening characteristic** to
  `Linear`.

### **Maximum opening pressure (gauge)** — Pressure that fully opens the valve `0.2` MPa (default) | positive scalar

Valve operational pressure at which the valve is fully open. The valve
begins to open at the cracking pressure value, and is fully open at
*pmax*.

#### Dependencies

To enable this parameter, set **Opening pressure
specification** to `Gauge pressure at port
A` and either:

- **Modeling option** to
  `Liquid operating
  condition` and **Valve
  parameterization** to `Linear -
  Area vs. pressure` or
  `Linear - Nominal mass flow rate vs.
  pressure`.
- **Modeling option** to
  `Vapor operating condition`
  and **Opening characteristic** to
  `Linear`.

### **Cracking pressure differential** — Cracking pressure `0.01` MPa (default) | positive scalar

Valve pressure threshold. When the control pressure,
*pA ̶
pB*, exceeds the opening pressure,
the valve begins to open.

#### Dependencies

To enable this parameter, set **Opening pressure
specification** to `Pressure
differential` and either:

- **Modeling option** to
  `Liquid operating
  condition` and **Valve
  parameterization** to `Linear -
  Area vs. pressure` or
  `Linear - Nominal mass flow rate vs.
  pressure`.
- **Modeling option** to
  `Vapor operating condition`
  and **Opening characteristic** to
  `Linear`.

### **Maximum opening pressure differential** — Maximum valve operational pressure `0.1` MPa (default) | positive scalar

Maximum valve operational pressure. The valve begins to open at the
cracking pressure value, and is fully open at
*pmax*.

#### Dependencies

To enable this parameter, set **Opening pressure
specification** to `Pressure
differential` and either:

- **Modeling option** to
  `Liquid operating
  condition` and **Valve
  parameterization** to `Linear -
  Area vs. pressure` or
  `Linear - Nominal mass flow rate vs.
  pressure`.
- **Modeling option** to
  `Vapor operating condition`
  and **Opening characteristic** to
  `Linear`.

### **Nominal mass flow rate at maximum valve opening** — Rated mass flow rate `0.1` kg/s (default) | positive scalar

Mass flow rate through a fully open valve under typical, design, or
rated conditions.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition` and
**Valve parameterization** to
`Linear - Nominal mass flow rate vs.
pressure`.

### **Nominal pressure drop at maximum valve opening** — Rated pressure drop `0.001` MPa (default) | positive scalar

Pressure drop over a fully open valve under typical, design, or rated
conditions.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition` and
**Valve parameterization** to
`Linear - Nominal mass flow rate vs.
pressure`.

### **Nominal inlet condition specification** — Method of determining inlet fluid state `Temperature` (default) | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

Method of determining the inlet fluid state. The block determines the orifice nominal
inlet specific volume from the tabulated fluid properties data based on
the value of the **Nominal inlet pressure** parameter
and the setting of the **Nominal inlet condition
specification** parameter.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition` and
**Valve parameterization** to
`Linear - Nominal mass flow rate vs.
pressure`.

### **Nominal inlet pressure** — Inlet fluid pressure `0.101325` MPa (default) | positive scalar

Inlet pressure in nominal conditions. The block determines the inlet specific volume
from the tabulated fluid properties data based on the value of the
**Nominal inlet pressure** parameter and the
setting of the **Nominal inlet condition
specification** parameter.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition` and
**Valve parameterization** to
`Linear - Nominal mass flow rate vs.
pressure`.

### **Nominal inlet temperature** — Fluid temperature `293.15` K (default) | positive scalar

Inlet fluid temperature in nominal operating conditions.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition`,
**Valve parameterization** to
`Linear - Nominal mass flow rate vs.
pressure`, and **Nominal inlet condition
specification** to
`Temperature`.

### **Nominal inlet vapor quality** — Inlet vapor quality mass fraction `0` (default) | positive scalar in the range [0,1]

Inlet mixture vapor quality by mass fraction in nominal operating
conditions. A value of `0` means that the inlet fluid
is subcooled liquid. A value of `1` means that the
inlet fluid is superheated vapor.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition`,
**Valve parameterization** to
`Linear - Nominal mass flow rate vs.
pressure`, and **Nominal inlet condition
specification** to `Vapor
quality`.

### **Nominal inlet vapor void fraction** — Inlet volume fraction `0` (default) | positive scalar in the range [0,1]

Inlet mixture volume fraction in nominal operating conditions. A value
of `0` means that the inlet fluid is subcooled liquid.
A value of `1` means that the inlet fluid is
superheated vapor.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition`,
**Valve parameterization** to
`Linear - Nominal mass flow rate vs.
pressure`, and **Nominal inlet condition
specification** to `Vapor void
fraction`.

### **Nominal inlet specific enthalpy** — Inlet fluid specific enthalpy `400` kJ/kg (default) | positive scalar

Inlet specific enthalpy in nominal operating conditions.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition`,
**Valve parameterization** to
`Linear - Nominal mass flow rate vs.
pressure`, and **Nominal inlet condition
specification** to `Specific
enthalpy`.

### **Nominal inlet specific internal energy** — Inlet specific internal energy `400` kJ/kg (default) | positive scalar

Inlet specific internal energy in nominal operating conditions.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition`,
**Valve parameterization** to
`Linear - Nominal mass flow rate vs.
pressure`, and **Nominal inlet condition
specification** to `Specific internal
energy`.

### **Maximum valve area** — Maximum valve opening area `1e-4 m^2` (default) | positive scalar

Maximum valve area when it is fully open.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition` and
**Valve parameterization** to
`Linear – Area vs. pressure`.

### **Opening pressure differential vector** — Vector of pressure differentials `[0.2 : 0.2 : 1.2] MPa` (default) | 1-by-*n* vector

Vector of pressure differential values for the tabulated
parameterization of valve area. The values in this vector correspond
one-to-one with the elements in the **Valve area
vector**, **Orifice area vector**,
**Cv flow coefficient vector**, or **Kv
flow coefficient vector** parameters.

#### Dependencies

To enable this parameter, set **Opening pressure
specification** to `Pressure
differential` and either:

- **Modeling option** to
  `Liquid operating
  condition` and **Valve
  parameterization** to
  `Tabulated data - Area vs.
  pressure`
- **Modeling option** to
  `Vapor operating condition`
  and **Opening characteristic** to
  `Tabulated`.

### **Opening pressure (gauge) vector** — Vector of gauge pressures `[0.2 : 0.2 : 1.2] MPa` (default) | 1-by-*n* vector

Vector of gauge pressure values for the tabulated parameterization of
valve area. The values in this vector correspond one-to-one with the
elements in the **Valve area vector**,
**Orifice area vector**, **Cv flow
coefficient vector**, or **Kv flow coefficient
vector** parameters.

#### Dependencies

To enable this parameter, set **Opening pressure
specification** to `Gauge pressure at port
A` and either:

- **Modeling option** to
  `Liquid operating
  condition` and **Valve
  parameterization** to
  `Tabulated data - Area vs.
  pressure`
- **Modeling option** to
  `Vapor operating condition`
  and **Opening characteristic** to
  `Tabulated`.

### **Valve area vector** — Vector of valve opening area values `[1e-10, 2e-06, 4e-06, 6e-06, 8e-06, 1e-05] m^2` (default) | 1-by-*n* vector

Vector of orifice area values for the tabulated parameterization of the valve area. The
values in this vector correspond one-to-one with the elements in the
**Opening pressure differential vector** or the
**Opening pressure (gauge) vector** parameters.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition` and
**Valve parameterization** to
`Tabulated data - Area vs.
pressure`.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Ratio of actual flow rate to ideal flow rate. This parameter accounts
for real-world losses that are not captured in the orifice
equation.

#### Dependencies

To enable this parameter, set either:

- **Modeling option** to
  `Liquid operating
  condition` and **Valve
  parameterization** to `Linear -
  Area vs. pressure` or
  `Tabulated data - Area vs.
  pressure`.
- **Modeling option** to
  `Vapor operating condition`
  and **Valve parameterization** to
  `Orifice area`.

### **Pressure recovery** — Whether to account for pressure increase in area expansions `off` (default) | `on`

Whether to account for the small rise in pressure after the pressure drop from the inlet
to the orifice hole. When the fluid jet exits the orifice hole, it
dissipates and expands to fill the port area, which causes this small
pressure rise. The block does not model this pressure increase when you
clear the **Pressure recovery** check box.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition` and
**Valve parameterization** to
`Linear - Area vs. pressure` or
`Tabulated data - Area vs.
pressure`.

### **Opening characteristic** — Method to parameterize measure of flow capacity `Linear` (default) | `Tabulated`

Method by which to parameterize the vapor valve for the chosen measure
of flow capacity.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Vapor operating condition`.

### **Maximum Cv flow coefficient** — *Cv* coefficient that corresponds to maximally open component `4` (default) | positive scalar

Value of the *Cv* flow
coefficient when the restriction area available for flow is at a
maximum. This parameter measures the ease with which the vapor traverses
the resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Vapor operating condition`,
**Valve parameterization** to `Cv
flow coefficient`, and **Opening
characteristic** to
`Linear`.

### **Cv flow coefficient vector** — *Cv* coefficients that correspond to values in member position vector `[1e-06, .8, 1.6, 2.4, 3.2, 4]` (default) | 1-by-*n* vector

Vector of *Cv* flow
coefficients. Each coefficient corresponds to a value in the
**Opening pressure differential vector** or the
**Opening pressure (gauge) vector** parameters.
This parameter measures the ease with which the vapor traverses the
resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Vapor operating condition`,
**Valve parameterization** to `Cv
flow coefficient`, and **Opening
characteristic** to
`Tabulated`.

### **Maximum Kv flow coefficient** — *Kv* coefficient that corresponds to maximally open component `3.6` (default) | positive scalar

Value of the *Kv* flow
coefficient when the restriction area available for flow is at a
maximum. This parameter measures the ease with which the vapor traverses
the resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Vapor operating condition`,
**Valve parameterization** to `Kv
flow coefficient`, and **Opening
characteristic** to
`Linear`.

### **Kv flow coefficient vector** — *Kv* coefficients that correspond to values in member position vector `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` (default) | 1-by-*n* vector

Vector of *Kv* flow
coefficients. Each coefficient corresponds to a value in the
**Opening pressure differential vector** or the
**Opening pressure (gauge) vector** parameters.
This parameter measures the ease with which the vapor traverses the
resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Vapor operating condition`,
**Valve parameterization** to `Kv
flow coefficient`, and **Opening
characteristic** to
`Tabulated`.

### **xT pressure differential ratio factor at choked flow** — Ratio of pressure differentials `0.7` (default) | positive scalar

Ratio between the inlet pressure,
*pin*, and the outlet
pressure, *pout*, defined as (pin−pout)/pin where choking first occurs.

#### Dependencies

To enable this parameter, **Modeling option** to
`Vapor operating condition` and
**Valve parameterization** to `Cv
flow coefficient` or `Kv flow
coefficient`.

### **Maximum orifice area** — Maximum valve opening area `1e-4 m^2` (default) | positive scalar

Maximum valve area when the valve is fully open.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Vapor operating condition`,
**Valve parameterization** to
`Orifice area`, and **Opening
characteristic** to
`Linear`.

### **Orifice area vector** — Vector of valve opening area values `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of orifice area values for the tabulated parameterization of the vapor valve
area. The values in this vector correspond one-to-one with the elements
in the **Opening pressure differential vector** or the
**Opening pressure (gauge) vector**
parameters.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Vapor operating condition`,
**Valve parameterization** to
`Orifice area`, and **Opening
characteristic** to
`Tabulated`.

### **Leakage flow fraction** — Ratio of flow rates `1e-6` (default) | positive scalar

Ratio of the flow rate of the valve when it is closed to when it is
open.

#### Dependencies

To enable this parameter, set either:

- **Modeling option** to
  `Liquid operating
  condition` and **Valve
  parameterization** to `Linear -
  Nominal mass flow rate vs. pressure` or
  `Linear - Area vs.
  pressure`.
- **Modeling option** to
  `Vapor operating condition`
  and **Opening characteristic** to
  `Linear`.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change
to the flow response when the valve is in near-open or near-closed
positions. Set this parameter to a nonzero value less than one to
increase the stability of your simulation in these regions.

#### Dependencies

To enable this parameter, set either:

- **Modeling option** to
  `Liquid operating
  condition` and **Valve
  parameterization** to `Linear -
  Nominal mass flow rate vs. pressure` or
  `Linear - Area vs.
  pressure`.
- **Modeling option** to
  `Vapor operating condition`
  and **Opening characteristic** to
  `Linear`.

### **Inlet phase change time constant** — Lag for liquid specific volume `0.1` s (default) | positive scalar

Time lag for liquid-vapor mixtures in computing the fluid specific
volume.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition`.

### **Laminar flow pressure ratio** — Laminar-turbulent transition pressure ratio `0.999` (default) | positive scalar

Ratio of the valve outlet pressure to valve inlet pressure at which
the fluid transitions between the laminar and turbulent regimes. The
pressure loss corresponds to the mass flow rate linearly in laminar
flows and quadratically in turbulent flows.

### **Cross-sectional area at ports A and B** — Valve port areas `0.01` m^2 (default) | positive scalar

Area of the ports **A** and
**B**.
## Libraries

Simscape / Fluids / Two-Phase Fluid / Valves & Orifices / Directional Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

### R2024a: Model vapor or liquid valves

You can now use the **Modeling option** parameter to specify an
valve when the two-phase fluid is in a vapor or liquid state. Both modeling options
also include new valve parameterizations.

When **Modeling option** is `Liquid operating
condition`, you can now set **Valve
parameterization** to:

- `Linear - Area vs. pressure`
- `Tabulated data - Area vs. pressure`

When **Modeling option** is `Vapor operating
condition`, you can now set **Valve
parameterization** to:

- `Cv flow coefficient`
- `Kv flow coefficient`
- `Orifice area`

To preserve the block behavior from previous releases, set **Modeling
option** to `Liquid operating condition` and
**Valve parameterization** to `Linear - Nominal
mass flow rate vs. pressure`.

## Description

Check valve in a two-phase fluid network

The Check Valve (2P) block models a directional control check valve in a two-phase
fluid network. The valve maintains the fluid pressure by opening above a specified
pressure and allowing flow from port **A** to port
**B**, but not in the reverse direction. The pressure differential
that opens the valve is specified in the **Opening pressure
specification** parameter. This value can be either the pressure difference
between ports **A** and **B** or the gauge pressure at
port **A**.

The **Modeling option** parameter controls the parameterization options for
a valve designed for modeling either vapor or liquid, but does not impact the fluid
properties. The block calculates fluid properties inside the valve from inlet
conditions. There is no heat exchange between the fluid and the environment, and
therefore phase change inside the orifice only occurs due to a pressure drop or a
propagated phase change from another part of the model.

### Directional Control

The valve opens when the pressure in the valve,
*pcontrol*, exceeds the cracking
pressure, *pcrack*. The valve is fully open
when the control pressure reaches the valve maximum pressure,
*pmax*. For linear
parameterizations, block calculates the opening fraction of the valve,
*λ*, as

λ=(1−fleak)(pcontrol−pcrack)(pmax−pcrack)+fleak,

where:

- *fleak* is the value of the
  **Leakage flow fraction** parameter.
- *pcontrol* is the control
  pressure, which depends on the value of the **Opening pressure
  specification** parameter.

  When you set **Opening pressure specification** to
  `Pressure differential`, the control
  pressure is *pA ̶
  pB*.

  When you set **Opening pressure specification** to
  `Gauge pressure at port A`, the control
  pressure is the difference between the pressure at port
  **A** and atmospheric pressure.

The cracking pressure and maximum pressure are specified as either a
differential value or a gauge value, depending on the setting of the
**Opening pressure specification**. If the control pressure
exceeds the maximum pressure, the valve opening fraction is 1.

### Liquid Valve

When **Modeling option** is `Liquid operating
condition`, the block parameterizations depend on the value of the
**Valve parameterization** parameter. The block calculates the
pressure loss and pressure recovery in the same way for all liquid parameterization
options.

The critical pressure difference,
*Δpcrit*, is the pressure differential where
the flow transitions between laminar and turbulent flow. For all liquid
parameterizations, *Δpcrit* is

Δpcrit=(pA+pB)2(1−Blam),

where:

- *pA* and
  *pB* are the pressure at
  port **A** and **B**, respectively.
- *Blam* is the value of the
  **Laminar flow pressure ratio** parameter.

The block accounts for pressure loss by using the ratio of the pressure loss across the
whole valve to the pressure drop immediately across the valve restriction area. This
ratio, *PRloss*, is

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport,

where:

- *Aport* is the value of the
  **Cross-sectional area at ports A and B**
  parameter.
- *Cd* is the value of the
  **Discharge coefficient** parameter.
- *Avalve* is the valve
  area.

The pressure recovery is the positive pressure change in the valve due to an
increase in area after the orifice hole. If you do not want to capture this increase
in pressure, clear the **Pressure recovery** check box. In this
case, *PRloss* is 1, which reduces the model
complexity. Clear this setting if the orifice hole is quite small relative to the
port area or if the next downstream component is close to the block and any jet does
not have room to dissipate.

**Linear - Nominal Mass Flow Rate vs. Pressure Parameterization**

When you set **Valve Parameterization** to `Nominal Mass Flow
Rate vs. pressure`, the mass flow rate through the valve is

m˙=λm˙nom[vnom2Δpnom]2vinΔp(Δp2+Δpcrit2)0.25,

where:

- *Δp* is the pressure drop over the valve,
  *pA ̶
  pB*.
- m˙nom is the value of the **Nominal mass flow
  rate at maximum valve opening** parameter.
- *Δpnom* is the value of
  the **Nominal pressure drop rate at maximum valve
  opening** parameter.
- *vnom* is the nominal
  inlet specific volume. The block determines this value from the
  tabulated fluid properties data based on the **Nominal inlet
  specific enthalpy** and **Nominal inlet
  pressure** parameters.
- *vin* is the inlet
  specific volume.

**Linear - Area vs. Pressure Parameterization**

When you set **Valve parameterization** to
`Linear - Area vs. Pressure Parameterization`, the
valve area is

Avalve=λAmax,

where *Amax* is the
value of the **Maximum valve area** parameter.

The mass flow rate is

m˙=CdAvalve2vinPRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4.

When the valve is in a near-open or near-closed position,
you can maintain numerical robustness in your simulation by adjusting the
**Smoothing factor** parameter. If the
**Smoothing factor** parameter is nonzero, the block
smoothly saturates the opening area between
*Aleak* and
*Amax*, where
*Aleak =
fleakAmax*. For
more information, see Numerical Smoothing.

**Tabulated Data - Area vs. Pressure Parameterization**

When you set **Valve Parameterization** to
`Tabulated data - Area vs. pressure`, the block
interpolates the valve area from the **Valve area vector** and
**Opening pressure differential vector** or
**Opening pressure (gauge) vector** parameters.

The block uses the same equation as the `Linear - Area vs.
pressure` setting to calculate the volumetric flow
rate.

**Fluid Specific Volume Dynamics**

For all parameterizations, the block calculates the fluid specific volume
during simulation based on the liquid state.

If the fluid at the valve inlet is a liquid-vapor mixture, the block
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

If the inlet fluid is a subcooled liquid, *xin =
0*. If the inlet fluid is a superheated vapor,
*xin = 1*.

### Vapor Valve

When **Modeling option** is `Vapor operating
condition`, the block behavior depends on the **Valve
parameterization** and **Opening characteristic**
parameters.

The flow rate in the valve depends on the **Opening
characteristic** parameter:

- `Linear` — The block scales the measure of flow
  capacity by *λ* to account for the valve opening
  area.
- `Tabulated` — The block interpolates the measure
  of flow capacity from either the **Cv flow coefficient
  vector**, **Kv flow coefficient vector**, or
  **Orifice area vector** parameters. This function uses
  a one-dimensional lookup table.

**Cv Flow Coefficient Parameterization**

When you set **Valve parametrization** to `Cv flow
coefficient`, the mass flow rate is

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

When the pressure ratio, pout/pin, falls below 1−FγxT, the valve becomes choked and the block uses the equation

m˙=23CvN6FγxTpinvin.

**Kv Flow Coefficient Parameterization**

When you set **Valve parametrization** to `Kv flow
coefficient`, the block uses the same equations as the
`Cv flow coefficient` parametrization, but replaces
*Cv* with
*Kv* using the relation Kv=0.865Cv.

**Valve Area Parameterization**

When you set **Valve parametrization** to `Orifice
area`, the mass flow rate is

m˙=CdAvalve2γγ−1pin1vin(poutpin)2γ[1−(poutpin)γ−1γ1−(AvalveAport)2(poutpin)2γ],

where:

- *γ* is the isentropic exponent.

The block smoothly transitions to a linearized form of the equation when
the pressure ratio, pout/pin, rises above the value of the **Laminar flow
pressure ratio** parameter,
*Blam*,

m˙=CdAvalve2γγ−1pavg2−γγ1vavgBlam2γ[1− Blamγ−1γ1−(AvalveAport)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

When the pressure ratio, pout/pin, falls below(2γ+1)γγ−1 , the valve becomes choked and the block uses the
equation

m˙=CdAvalve2γγ+1pin1vin1(γ+12)2γ−1−(AvalveAport)2.

### Mass Balance

Mass is conserved in the valve,

m˙A+m˙B=0,

where:

- m˙A is the mass flow rate at port
  **A**.
- m˙B is the mass flow rate at port
  **B**.

### Energy Balance

Energy is conserved in the valve,

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
  the superheated vapor region. To model a valve in a liquid-vapor
  mixture, set **Modeling option** to `Liquid
  operating condition`.
