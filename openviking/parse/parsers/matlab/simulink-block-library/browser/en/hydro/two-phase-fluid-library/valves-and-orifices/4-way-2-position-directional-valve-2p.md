---
type: simulink-block
title: '4-Way 2-Position Directional Valve (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid Library / Valves and Orifices'
documentation_page: '4way2positiondirectionalvalve2p'
documentation_source_path: 'ref/4way2positiondirectionalvalve2p.html'
language: en
---

# 4-Way 2-Position Directional Valve (2P)

## Ports

### Conserving

### **A** — Entry or exit port two-phase fluid

Two-phase fluid conserving port associated with the entry or exit port
to the valve.

### **B** — Entry or exit port two-phase fluid

Two-phase fluid conserving port associated with the entry or exit port
to the valve.

### **P** — Entry or exit port two-phase fluid

Two-phase fluid conserving port associated with the entry or exit port
to the valve.

### **T** — Entry or exit port two-phase fluid

Two-phase fluid conserving port associated with the entry or exit port
to the valve.
### Input

### **S** — Spool displacement, m physical signal

Physical signal associated with the spool displacement, in m.

## Parameters

### **Modeling option** — Modeling option for fluid phase `Liquid operating condition` (default) | `Vapor operating condition`

Modeling option for the fluid phase at the valve. Set this parameter to
`Liquid operating condition` if the two-phase
fluid at the block location is in a liquid state. Set this parameter to
`Vapor operating condition` if the two-phase
fluid at the block location is in a vapor state.

### Valve Configuration

### **Positive spool position open connections** — Flow paths open when spool is in positive position `P-A, B-T` (default) | `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-T, B-T`

Flow paths open when the spool is in a positive position. This
parameter sets the valve configuration and defines the direction of
spool movement according to the signal received at port
**S**.

### **Negative spool position open connections** — Flow paths open when spool moves in negative direction `P-B, A-T` (default) | `P-A, B-T` | `P-A, P-B` | `P-A` | `P-B` | `P-A, P-B, A-T, B-T`

Flow paths open when the spool moves in the negative direction. This
parameter sets the valve configuration and defines the direction of
spool movement according to the signal received at port
**S**.

### Model Parameterization

### **Area characteristics** — Flow equations for orifices `Identical for all flow paths` (default) | `Different for each flow path`

Whether to apply uniform or individual flow equations for the valve
orifice area. When you set this parameter to `Identical for
all flow paths`, the block uses the same orifice and
spool geometries, flow rates, pressure, and area vectors for all valve
orifices. When you set this parameter to `Different for each
flow path`, you can specify these parameters
individually for each orifice. For both settings, orifices
**A**, **B**,
**P**, and **T** have the same
cross-sectional areas, discharge coefficients, and Reynolds numbers when
you set **Orifice parameterization** to
`Linear - Area vs. spool travel` or
`Tabulated data - Area vs. spool travel`.

### **Orifice parameterization** — Variable or constant orifice parameterization `Linear - Area vs. spool travel` (default) | `Linear - Nominal mass flow rate vs. spool travel` | `Tabulated data - Area vs. spool travel` | `Cv flow coefficient` | `Kv flow coefficient` | `Orifice area`

Method the block uses to calculate the mass flow rate from the
pressure difference across the orifice or the pressure difference from
the mass flow rate.

When **Modeling option** is `Liquid
operating condition`, the choices for this parameter are:

- `Linear - Area vs. spool
  travel`
- `Linear - Nominal mass flow rate vs. spool
  travel`
- `Tabulated data - Area vs. spool
  travel`

When **Modeling option** is `Vapor
operating condition`, the choices for this parameter are:

- `Cv flow coefficient`
- `Kv flow coefficient`
- `Orifice area`

### **Spool travel between closed and open orifice** — Maximum spool stroke `0.005 m` (default) | positive scalar

Maximum distance of spool travel.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and either:

- **Modeling option** to
  `Liquid operating
  condition` and **Orifice
  parameterization** to `Linear -
  Area vs. spool travel`.
- **Modeling option** to
  `Vapor operating condition`
  and **Opening characteristic** to
  `Linear`.

### **Maximum orifice area** — Maximum orifice opening area `1e-4 m^2` (default) | positive scalar

Largest open area of each orifice during the operation of the
valve.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and either:

- **Modeling option** to
  `Liquid operating
  condition` and **Orifice
  parameterization** to `Linear -
  Area vs. spool travel`.
- **Modeling option** to
  `Vapor operating
  condition`, **Orifice
  parameterization** to `Orifice
  area`, and **Opening
  characteristic** to
  `Linear`.

### **Nominal mass flow rate at maximum orifice opening** — Rated mass flow rate `0.1` kg/s (default) | positive scalar

Typical, rated, or design mass flow rate at the orifice maximum
opening position.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition`,
**Area characteristics** to
`Identical for all flow paths`, and
**Orifice parameterization** to
`Linear - Nominal mass flow rate vs. spool
travel`.

### **Nominal pressure drop at maximum orifice opening** — Rated pressure drop `0.001` MPa (default) | positive scalar

Typical, rated, or design pressure drop at the orifice maximum opening
position.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition`,
**Area characteristics** to
`Identical for all flow paths`, and
**Orifice parameterization** to
`Linear - Nominal mass flow rate vs. spool
travel`.

### **Nominal inlet condition specification** — Method of determining inlet fluid state `Temperature` (default) | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

Method of determining the inlet fluid state. The block determines the
orifice nominal inlet specific volume from the tabulated fluid
properties data based on the value of the **Nominal inlet
pressure** and **Nominal inlet condition
specification** parameters.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition`,
**Area characteristics** to
`Identical for all flow paths`, and
**Orifice parameterization** to
`Linear - Nominal mass flow rate vs. spool
travel`.

### **Nominal inlet pressure** — Inlet fluid pressure `0.101325` MPa (default) | positive scalar

Inlet pressure in nominal conditions. The block determines the inlet
specific volume from the tabulated fluid properties data based on the
value of the **Nominal inlet pressure** and
**Nominal inlet condition specification**
parameters.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition`,
**Area characteristics** to
`Identical for all flow paths`, and
**Orifice parameterization** to
`Linear - Nominal mass flow rate vs. spool
travel`.

### **Nominal inlet temperature** — Fluid temperature `293.15` K (default) | positive scalar

Inlet fluid temperature in nominal operating conditions.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition`,
**Area characteristics** to
`Identical for all flow paths`,
**Orifice parameterization** to
`Linear - Nominal mass flow rate vs. spool
travel`, and **Nominal inlet condition
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
**Area characteristics** to
`Identical for all flow paths`,
**Orifice parameterization** to
`Linear - Nominal mass flow rate vs. spool
travel`, and **Nominal inlet condition
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
**Area characteristics** to
`Identical for all flow paths`,
**Orifice parameterization** to
`Linear - Nominal mass flow rate vs. spool
travel`, and **Nominal inlet condition
specification** to `Vapor void
fraction`.

### **Nominal inlet specific enthalpy** — Inlet fluid specific enthalpy `400` kJ/kg (default) | positive scalar

Inlet specific enthalpy in nominal operating conditions.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition`,
**Area characteristics** to
`Identical for all flow paths`,
**Orifice parameterization** to
`Linear - Nominal mass flow rate vs. spool
travel`, and **Nominal inlet condition
specification** to `Specific
enthalpy`.

### **Nominal inlet specific internal energy** — Inlet specific internal energy `400` kJ/kg (default) | positive scalar

Inlet specific internal energy in nominal operating conditions.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition`,
**Area characteristics** to
`Identical for all flow paths`,
**Orifice parameterization** to
`Linear - Nominal mass flow rate vs. spool
travel`, and **Nominal inlet condition
specification** to `Specific internal
energy`.

### **Opening characteristic** — Method to convert control signal to measure of flow capacity `Linear` (default) | `Tabulated`

Method by which to convert the control signal specified at port
**S** to the chosen measure of flow
capacity.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Vapor operating condition`.

### **Spool travel vector** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances when parameterizing the orifice according to the
tabulated valve area data. The vector elements must correspond
one-to-one with the elements in the **Orifice area
vector** parameter. List the values in ascending order. The
first element must be 0. The block uses linear interpolation between
table data points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and either:

- **Modeling option** to
  `Liquid operating
  condition` and **Orifice
  parameterization** to
  `Tabulated data - Area vs. spool
  travel`.
- **Modeling option** to
  `Vapor operating condition`
  and **Opening characteristic** to
  `Tabulated`.

### **Orifice area vector** — Vector of valve opening areas `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of opening areas when parameterizing the orifice according to the tabulated valve
area data. The vector elements must correspond one-to-one with the
elements in the **Spool travel vector** parameter. List
the values in ascending order. The elements must be greater than
0.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and either:

- **Modeling option** to
  `Liquid operating
  condition` and **Orifice
  parameterization** to
  `Tabulated data - Area vs. spool
  travel`.
- **Modeling option** to
  `Vapor operating
  condition`, **Orifice
  parameterization** to `Orifice
  area`, and **Opening
  characteristic** to
  `Tabulated`.

### **Maximum Cv flow coefficient** — *Cv* coefficient that corresponds to maximally open component `4` (default) | positive scalar

Value of the *Cv* flow
coefficient when the orifice is fully open and the area available for
flow is at a maximum. This parameter measures the ease with which the
vapor traverses the resistive element when driven by a pressure
differential.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Vapor operating condition`,
**Area characteristics** to
`Identical for all flow paths`,
**Orifice parameterization** to `Cv
flow coefficient`, and **Opening
characteristic** to
`Linear`.

### **Cv flow coefficient vector** — *Cv* coefficients for values in member position vector `[1e-06, .8, 1.6, 2.4, 3.2, 4]` (default) | 1-by-*n* vector

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
**Area characteristics** to
`Identical for all flow paths`,
**Orifice parameterization** to `Cv
flow coefficient`, and **Opening
characteristic** to
`Tabulated`.

### **Maximum Kv flow coefficient** — *Kv* coefficient that corresponds to maximally open component `3.6` (default) | positive scalar

Value of the *Kv* flow
coefficient when the orifice is fully open and the area available for
flow is at a maximum. This parameter measures the ease with which the
vapor traverses the resistive element when driven by a pressure
differential.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Vapor operating condition`,
**Area characteristics** to
`Identical for all flow paths`,
**Orifice parameterization** to `Kv
flow coefficient`, and **Opening
characteristic** to
`Linear`.

### **Kv flow coefficient vector** — *Kv* coefficients for values in member position vector `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` (default) | 1-by-*n* vector

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
**Area characteristics** to
`Identical for all flow paths`,
**Orifice parameterization** to `Kv
flow coefficient`, and **Opening
characteristic** to
`Tabulated`.

### **xT pressure differential ratio factor at choked flow** — Ratio of pressure differentials `0.7` (default) | positive scalar

Ratio between the inlet pressure,
*pin*, and the outlet
pressure, *pout*, defined as (pin−pout)/pin where choking first occurs.

#### Dependencies

To enable this parameter, **Modeling option** to
`Vapor operating condition`,
**Area characteristics** to
`Identical for all flow paths`, and
**Orifice parameterization** to `Cv
flow coefficient` or `Kv flow
coefficient`.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor that accounts for discharge losses in theoretical
flows.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Vapor operating condition` and
**Orifice parameterization** to
`Orifice area` or set
**Modeling option** to `Liquid
operating condition` and **Orifice
parameterization** to either:

- `Linear - Area vs. spool
  travel`
- `Tabulated data - Area vs. spool
  travel`

### **Leakage flow fraction** — Ratio of flow rates `1e-6` (default) | positive scalar

Ratio of the flow rate of the orifice when it is closed to when it is
open.

#### Dependencies

To enable this parameter, set either:

- **Modeling option** to
  `Liquid operating
  condition` and **Orifice
  parameterization** to `Linear -
  Area vs. spool travel`.
- **Modeling option** to
  `Vapor operating condition`
  and **Opening characteristic** to
  `Linear`.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range of [0,1]

Continuous smoothing factor that introduces a layer of gradual change based on the flow
response when the valve is in the near-open and near-closed positions.
To increase the stability of your simulation in these regimes, set this
parameter to a nonzero value less than one.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition` and
**Orifice parametrization** to
`Linear - area vs. spool travel` or set
**Modeling option** to `Vapor
operating condition` and **Opening
characteristic** to
`Linear`.

### **Pressure recovery** — Whether to account for pressure increase in area expansions `off` (default) | `on`

Whether to account for pressure increase when fluid flows from a
region of smaller cross-sectional area to a region of larger
cross-sectional area.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition` and
**Orifice parameterization** to either:

- `Linear - area vs. spool
  travel`
- `Tabulated data - Area vs. spool
  travel`

### **Laminar flow pressure ratio** — Laminar-turbulent transition pressure ratio `0.999` (default) | positive scalar

Ratio of the orifice outlet pressure to orifice inlet pressure at
which the fluid transitions between the laminar and turbulent regimes.
The pressure loss corresponds to the mass flow rate linearly in laminar
flows and quadratically in turbulent flows.

### **Inlet phase change time constant** — Time lag for mixture specific volume `0.1` `s` (default) | positive scalar

Time lag for liquid-vapor mixtures when computing the fluid specific
volume. This parameter does not influence the specific volume when the
inlet fluid is a fully supercooled liquid or fully superheated
vapor.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Liquid operating condition`.

### **Cross-sectional area at ports P, T, A and B** — Area at conserving ports `0.01 m^2` (default) | positive scalar

Maximum cross-sectional areas at the entry and exit ports
**P**, **T**,
**A**, and **B**, which the block
uses in the pressure-flow rate equation that determines the mass flow
rate through the valve.

### P-A Orifice

### **Spool position at maximum P-A orifice area** — Spool offset for fully open P-A orifice `5e-3 m` (default) | positive scalar

Spool offset from the neutral position for a fully open P-A
orifice.

#### Dependencies

To enable this parameter, set one of these parameters.

Set **Positive spool position open connections** to:

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

or set **Negative spool position open
connections** to:

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**Note:**

This parameter is enabled only when the P-A orifice
settings do not appear in both the **Positive spool position open connections** and
**Negative spool position open
connections** parameters.

### **P-A spool travel between closed and open orifice** — Maximum spool stroke `0.005 m` (default) | positive scalar

Maximum distance of spool travel. This value provides an upper limit
to calculations so that simulations do not return unphysical
values.

#### Dependencies

To enable this parameter, set one of the following
parameters:

**Positive spool position open connections** to:

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**Negative spool position open
connections** to:

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

And either:

- **Modeling option** to
  `Liquid operating condition`,
  **Area characteristics** to
  `Different for each flow path`,
  and **Orifice parameterization** to
  `Linear - Area vs. spool
  travel` or `Linear - Nominal
  mass flow rate vs. spool travel`.
- **Modeling option** to `Vapor
  operating condition`, **Area
  characteristics** to `Different for
  each flow path`, and **Opening
  characteristic** to
  `Linear`.

### **P-A nominal mass flow rate at maximum orifice opening** — Rated mass flow rate `0.1` `kg/s` (default) | positive scalar

Typical, rated, or design mass flow rate through a maximally open P-A
orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A nominal pressure drop at maximum orifice opening** — Rated pressure drop `0.001` `MPa` (default) | positive scalar

Typical, rated, or design pressure drop through a maximally open P-A
orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A nominal inlet condition specification** — Method of determining inlet fluid state `Temperature` (default) | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

Method of determining the inlet fluid state for P-A orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. At least one of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A nominal inlet pressure** — Inlet fluid pressure `0.101325` `MPa` (default) | positive scalar

Inlet pressure for the P-A orifice at nominal conditions.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. At least one of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A nominal inlet temperature** — Fluid temperature `293.15` `K` (default) | positive scalar

Inlet fluid temperature for the P-A orifice in nominal operating conditions.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** to
   `Temperature`
5. At least one of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A nominal inlet vapor quality** — Inlet vapor quality mass fraction `0` (default) | positive scalar in the range [0,1]

Inlet mixture vapor quality by mass fraction for the P-A orifice in nominal operating
conditions. A value of `0` means that the inlet fluid
is subcooled liquid. A value of `1` means that the
inlet fluid is superheated vapor.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** to `Vapor
   quality`
5. At least one of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A nominal inlet vapor void fraction** — Inlet vapor void fraction `0` (default) | positive scalar in the range [0,1]

Inlet mixture vapor void fraction for the P-A orifice in nominal operating conditions.
A value of `0` means that the inlet fluid is subcooled
liquid. A value of `1` means that the inlet fluid is
superheated vapor.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** to `Vapor void
   fraction`
5. At least one of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A nominal inlet specific enthalpy** — Inlet fluid specific enthalpy `400` `kJ/kg` (default) | positive scalar

Inlet specific enthalpy for the P-A orifice in nominal operating conditions.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** to `Specific
   enthalpy`
5. At least one of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A nominal inlet specific internal energy** — Inlet specific internal energy `400` `kJ/kg` (default) | positive scalar

Inlet specific internal energy for the P-A orifice in nominal operating
conditions.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** to `Specific
   internal energy`
5. At least one of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A constant orifice nominal mass flow rate** — Nominal mass flow rate `0.1` `kg/s` (default) | positive scalar

Typical, rated, or design mass flow rate through a constant P-A
orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. One of the following settings in each
   parameter:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

**Note:**

This parameter is enabled only when the P-A orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **P-A constant orifice nominal pressure drop** — Nominal pressure drop `0.001` `MPa` (default) | positive scalar

Typical, rated, or design pressure drop through a constant P-A
orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. One of the following settings in each
   parameter:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

**Note:**

This parameter is enabled only when the P-A orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **P-A constant orifice Cv flow coefficient** — Flow coefficient `4` (default) | positive scalar

Value of the constant *Cv* flow coefficient for
the P-A orifice. This parameter measures the ease with which the vapor
traverses the resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Cv flow
   coefficient`
4. One of the following settings in each
   parameter:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

**Note:**

This parameter is enabled only when the P-A orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **P-A orifice maximum Cv flow coefficient** — *Cv* coefficient that corresponds to maximally open component `4` (default) | positive scalar

Value of the *Cv* flow
coefficient when the P-A orifice is fully open and the area available
for flow is at a maximum. This parameter measures the ease with which
the vapor traverses the resistive element when driven by a pressure
differential.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Cv flow
   coefficient`
4. **Opening characteristic** to
   `Linear`
5. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A orifice Cv flow coefficient vector** — *Cv* coefficients for values in member position vector `[1e-06, .8, 1.6, 2.4, 3.2, 4]` (default) | 1-by-*n* vector

Vector of *Cv* flow
coefficients. Each coefficient corresponds to a value in the
**P-A orifice spool travel vector** parameter. This
parameter measures the ease with which the vapor traverses the resistive
element when driven by a pressure differential. The size of the vector
must be the same as the **P-A orifice spool travel
vector** parameter.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Cv flow
   coefficient`
4. **Opening characteristic** to
   `Tabulated`
5. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A constant orifice Kv flow coefficient** — Flow coefficient `3.6` (default) | positive scalar

Value of the constant *Kv* flow coefficient for
the P-A orifice. This parameter measures the ease with which the vapor
traverses the resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Kv flow
   coefficient`
4. One of the following settings in each
   parameter:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

**Note:**

This parameter is enabled only when the P-A orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **P-A orifice maximum Kv flow coefficient** — *Kv* coefficient that corresponds to maximally open component `3.6` (default) | positive scalar

Value of the *Kv* flow
coefficient when the P-A orifice is fully open and the area available
for flow is at a maximum. This parameter measures the ease with which
the vapor traverses the resistive element when driven by a pressure
differential.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Kv flow
   coefficient`
4. **Opening characteristic** to
   `Linear`
5. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A orifice Kv flow coefficient vector** — *Kv* coefficients for values in member position vector `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` (default) | 1-by-*n* vector

Vector of *Kv* flow
coefficients. Each coefficient corresponds to a value in the
**P-A orifice spool travel vector** parameter. This
parameter measures the ease with which the vapor traverses the resistive
element when driven by a pressure differential. The size of the vector
must be the same as the **P-A orifice spool travel
vector** parameter.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Kv flow
   coefficient`
4. **Opening characteristic** to
   `Tabulated`
5. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A orifice spool travel vector** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances for the tabular parameterization of
the valve area. List the values in ascending order. The first element
must be 0. The block uses linear interpolation between table data
points.

#### Dependencies

To enable this parameter, set one of the following
parameters:

**Positive spool position open connections** to:

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**Negative spool position open
connections** to:

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

And either:

- **Modeling option** to
  `Liquid operating condition`,
  **Area characteristics** to
  `Different for each flow path`,
  and **Orifice parameterization** to
  `Tabulated data - Area vs. spool
  travel`.
- **Modeling option** to `Vapor
  operating condition`, **Area
  characteristics** to `Different for
  each flow path`, and **Opening
  characteristic** to
  `Tabulated`.

### **P-A maximum orifice area** — Maximum orifice opening area `1e-4 m^2` (default) | positive scalar

Largest open area of the P-A orifice during the operation of the
valve.

#### Dependencies

To enable this parameter, set one of the following parameters:

**Positive spool position open connections** to:

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**Negative spool position open
connections** to:

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

Also set **Area characteristics** to
`Different for each flow path` and
either:

- **Modeling option** to
  `Liquid operating condition`
  and **Orifice parameterization** to
  `Linear - Area vs. spool
  travel`.
- **Modeling option** to `Vapor
  operating condition`, **Orifice
  parameterization** to `Orifice
  area`, and **Opening
  characteristic** to
  `Linear`.

### **P-A orifice area vector** — Vector of valve opening areas `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of opening areas for the tabular parameterization of the valve area. The vector
elements must correspond one-to-one with the elements in the
**P-A orifice spool travel vector** parameter. The
elements must be greater than 0 and listed in ascending order.

#### Dependencies

To enable this parameter, set one of the following parameters:

**Positive spool position open connections** to:

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**Negative spool position open
connections** to:

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

Also set **Area characteristics** to
`Different for each flow path` and
either:

- **Modeling option** to
  `Liquid operating condition`
  and **Orifice parameterization** to
  `Tabulated data - Area vs. spool
  travel`.
- **Modeling option** to `Vapor
  operating condition`, **Orifice
  parameterization** to `Orifice
  area`, and **Opening
  characteristic** to
  `Tabulated`.

### **P-A constant orifice area** — Cross-sectional area for constant orifice `1e-4 m^2` (default) | positive scalar

Orifice area when the positive and negative spool positions include
the same orifice.

#### Dependencies

To enable this parameter, set one of the following settings in
each parameter:

**Positive spool position open connections** to:

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**Negative spool position open
connections** to:

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

And either:

- **Modeling option** to
  `Liquid operating condition`,
  **Area characteristics** to
  `Different for each flow path`,
  and **Orifice parameterization** to
  `Tabulated data - Area vs. spool
  travel` or `Linear - Area vs.
  spool travel`.
- **Modeling option** to `Vapor
  operating condition`, **Area
  characteristics** to `Different for
  each flow path`, and **Opening
  characteristic** to
  `Tabulated`.

**Note:**

This parameter is enabled only when the P-A orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **P-A orifice xT pressure differential ratio factor at choked flow** — Ratio of pressure differentials `0.7` (default) | positive scalar

Ratio between the inlet pressure, *pin*, and the
outlet pressure, *pout*, defined
as (pin−pout)/pin where choking first occurs for the P-A orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Kv flow coefficient` or
   `Cv flow
   coefficient`
4. At least one of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### P-B Orifice

### **Spool position at maximum P-B orifice area** — Spool offset for fully open P-B orifice `5e-3 m` (default) | positive scalar

Spool offset from the neutral position for a fully open P-B
orifice.

#### Dependencies

To enable this parameter, set one of these parameters:

**Positive spool position open connections** to:

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

or set **Negative spool position open
connections** to:

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**Note:**

This parameter is enabled only when the P-B orifice settings
do not appear in both the **Positive spool
position open connections** and **Negative spool position open
connections** parameters.

### **P-B spool travel between closed and open orifice** — Maximum spool stroke `0.005 m` (default) | positive scalar

Maximum distance of spool travel. This value provides an upper limit
to calculations so that simulations do not return unphysical
values.

#### Dependencies

To enable this parameter, set one of the following
parameters:

**Positive spool position open connections** to:

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**Negative spool position open
connections** to:

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

And either:

- **Modeling option** to
  `Liquid operating condition`,
  **Area characteristics** to
  `Different for each flow path`,
  and **Orifice parameterization** to
  `Linear - Area vs. spool
  travel` or `Linear - Nominal
  mass flow rate vs. spool travel`.
- **Modeling option** to `Vapor
  operating condition`, **Area
  characteristics** to `Different for
  each flow path`, and **Opening
  characteristic** to
  `Linear`.

### **P-B nominal mass flow rate at maximum orifice opening** — Rated mass flow rate `0.1` `kg/s` (default) | positive scalar

Typical, rated, or design mass flow rate through a maximally open P-B
orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B nominal pressure drop at maximum orifice opening** — Rated pressure drop `0.001` `MPa` (default) | positive scalar

Typical, rated, or design pressure drop through a maximally open P-B
orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B nominal inlet condition specification** — Method of determining inlet fluid state `Temperature` (default) | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

Method of determining the inlet fluid state for P-B orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. At least one of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B nominal inlet pressure** — Inlet fluid pressure `0.101325` `MPa` (default) | positive scalar

Inlet pressure for the P-B orifice at nominal conditions.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. At least one of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B nominal inlet temperature** — Fluid temperature `293.15` `K` (default) | positive scalar

Inlet fluid temperature for the P-B orifice in nominal operating conditions.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** to
   `Temperature`
5. At least one of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B nominal inlet vapor quality** — Inlet vapor quality mass fraction `0` (default) | positive scalar in the range [0,1]

Inlet mixture vapor quality by mass fraction for the P-B orifice in nominal operating
conditions. A value of `0` means that the inlet fluid
is subcooled liquid. A value of `1` means that the
inlet fluid is superheated vapor.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** to `Vapor
   quality`
5. At least one of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B nominal inlet vapor void fraction** — Inlet vapor void fraction `0` (default) | positive scalar in the range [0,1]

Inlet mixture vapor void fraction for the P-B orifice in nominal operating conditions. A
value of `0` means that the inlet fluid is subcooled
liquid. A value of `1` means that the inlet fluid is
superheated vapor.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** to `Vapor void
   fraction`
5. At least one of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B nominal inlet specific enthalpy** — Inlet fluid specific enthalpy `400` `kJ/kg` (default) | positive scalar

Inlet specific enthalpy for the P-B orifice in nominal operating conditions.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** to `Specific
   enthalpy`
5. At least one of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B nominal inlet specific internal energy** — Inlet specific internal energy `400` `kJ/kg` (default) | positive scalar

Inlet specific internal energy for the P-B orifice in nominal operating
conditions.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** to `Specific
   internal energy`
5. At least one of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B constant orifice nominal mass flow rate** — Nominal mass flow rate `0.1` `kg/s` (default) | positive scalar

Typical, rated, or design mass flow rate through a constant P-B
orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. One of the following settings in each
   parameter:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

**Note:**

This parameter is enabled only when the P-B orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **P-B constant orifice nominal pressure drop** — Nominal pressure drop `0.001` `MPa` (default) | positive scalar

Typical, rated, or design pressure drop through a constant P-B
orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. One of the following settings in each
   parameter:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

**Note:**

This parameter is enabled only when the P-B orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **P-B constant orifice Cv flow coefficient** — Flow coefficient `4` (default) | positive scalar

Value of the constant *Cv* flow coefficient for
the P-B orifice. This parameter measures the ease with which the vapor
traverses the resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Cv flow
   coefficient`
4. One of the following settings in each
   parameter:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

**Note:**

This parameter is enabled only when the P-B orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **P-B orifice maximum Cv flow coefficient** — *Cv* coefficient that corresponds to maximally open component `4` (default) | positive scalar

Value of the *Cv* flow
coefficient when the P-B orifice is fully open and the area available
for flow is at a maximum. This parameter measures the ease with which
the vapor traverses the resistive element when driven by a pressure
differential.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Cv flow
   coefficient`
4. **Opening characteristic** to
   `Linear`
5. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B orifice Cv flow coefficient vector** — *Cv* coefficients for values in member position vector `[1e-06, .8, 1.6, 2.4, 3.2, 4]` (default) | 1-by-*n* vector

Vector of *Cv* flow
coefficients. Each coefficient corresponds to a value in the
**P-B orifice spool travel vector** parameter. This
parameter measures the ease with which the vapor traverses the resistive
element when driven by a pressure differential. The size of the vector
must be the same as the **P-B orifice spool travel
vector** parameter.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Cv flow
   coefficient`
4. **Opening characteristic** to
   `Tabulated`
5. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B constant orifice Kv flow coefficient** — Flow coefficient `3.6` (default) | positive scalar

Value of the constant *Kv* flow coefficient for
the P-B orifice. This parameter measures the ease with which the vapor
traverses the resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Kv flow
   coefficient`
4. One of the following settings in each
   parameter:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

**Note:**

This parameter is enabled only when the P-B orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **P-B orifice maximum Kv flow coefficient** — *Kv* coefficient that corresponds to maximally open component `3.6` (default) | positive scalar

Value of the *Kv* flow
coefficient when the P-B orifice is fully open and the area available
for flow is at a maximum. This parameter measures the ease with which
the vapor traverses the resistive element when driven by a pressure
differential.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Kv flow
   coefficient`
4. **Opening characteristic** to
   `Linear`
5. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B orifice Kv flow coefficient vector** — *Kv* coefficients for values in member position vector `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` (default) | 1-by-*n* vector

Vector of *Kv* flow
coefficients. Each coefficient corresponds to a value in the
**P-B orifice spool travel vector** parameter. This
parameter measures the ease with which the vapor traverses the resistive
element when driven by a pressure differential. The size of the vector
must be the same as the **P-B orifice spool travel
vector** parameter.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Kv flow
   coefficient`
4. **Opening characteristic** to
   `Tabulated`
5. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B orifice spool travel vector** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances for the tabular parameterization of
the valve area. List the values in ascending order. The first element
must be 0. The block uses linear interpolation between table data
points.

#### Dependencies

To enable this parameter, set one of the following
parameters:

**Positive spool position open connections** to:

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**Negative spool position open
connections** to:

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

And either:

- **Modeling option** to
  `Liquid operating condition`,
  **Area characteristics** to
  `Different for each flow path`,
  and **Orifice parameterization** to
  `Tabulated data - Area vs. spool
  travel`.
- **Modeling option** to `Vapor
  operating condition`, **Area
  characteristics** to `Different for
  each flow path`, and **Opening
  characteristic** to
  `Tabulated`.

### **P-B maximum orifice area** — Maximum orifice opening area `1e-4 m^2` (default) | positive scalar

Largest open area of the P-B orifice during the operation of the
valve.

#### Dependencies

To enable this parameter, set one of the following parameters:

**Positive spool position open connections** to:

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**Negative spool position open
connections** to:

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

Also set **Area characteristics** to
`Different for each flow path` and
either:

- **Modeling option** to
  `Liquid operating condition`
  and **Orifice parameterization** to
  `Linear - Area vs. spool
  travel`.
- **Modeling option** to `Vapor
  operating condition`, **Orifice
  parameterization** to `Orifice
  area`, and **Opening
  characteristic** to
  `Linear`.

### **P-B orifice area vector** — Vector of valve opening areas `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of opening areas for the tabular parameterization of the valve area. The vector
elements must correspond one-to-one with the elements in the
**P-B orifice spool travel vector** parameter. The
elements must be greater than 0 and listed in ascending order.

#### Dependencies

To enable this parameter, set one of the following parameters:

**Positive spool position open connections** to:

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**Negative spool position open
connections** to:

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

Also set **Area characteristics** to
`Different for each flow path` and
either:

- **Modeling option** to
  `Liquid operating condition`
  and **Orifice parameterization** to
  `Tabulated data - Area vs. spool
  travel`.
- **Modeling option** to `Vapor
  operating condition`, **Orifice
  parameterization** to `Orifice
  area`, and **Opening
  characteristic** to
  `Tabulated`.

### **P-B constant orifice area** — Cross-sectional area for constant orifice `1e-4 m^2` (default) | positive scalar

Orifice area when the positive and negative spool positions include
the same orifice.

#### Dependencies

To enable this parameter, set one of the following settings in
each parameter:

**Positive spool position open connections** to:

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**Negative spool position open
connections** to:

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

And either:

- **Modeling option** to
  `Liquid operating condition`,
  **Area characteristics** to
  `Different for each flow path`,
  and **Orifice parameterization** to
  `Tabulated data - Area vs. spool
  travel` or `Linear - Area vs.
  spool travel`.
- **Modeling option** to `Vapor
  operating condition`, **Area
  characteristics** to `Different for
  each flow path`, and **Opening
  characteristic** to
  `Tabulated`.

**Note:**

This parameter is enabled only when the P-B orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **P-B orifice xT pressure differential ratio factor at choked flow** — Ratio of pressure differentials `0.7` (default) | positive scalar

Ratio between the inlet pressure, *pin*, and the
outlet pressure, *pout*, defined
as (pin−pout)/pin where choking first occurs for the P-B orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Kv flow coefficient` or
   `Cv flow
   coefficient`
4. At least one of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### A-T Orifice

### **Spool position at maximum A-T orifice area** — Spool offset for fully open A-T orifice `5e-3 m` (default) | positive scalar

Spool offset from the neutral position for a fully open A-T
orifice.

#### Dependencies

To enable this parameter, set one of these parameters.

- **Positive spool position open
  connections** to `P-B,
  A-T` or `P-A, P-B, A-T,
  B-T`.
- **Negative spool position open
  connections** to `P-B,
  A-T` or `P-A, P-B, A-T,
  B-T`.

**Note:**

This parameter is enabled only when the A-T orifice
settings do not appear in both the **Positive spool position open connections** and
**Negative spool position open
connections** parameters.

### **A-T spool travel between closed and open orifice** — Maximum spool stroke `0.005 m` (default) | positive scalar

Maximum distance of spool travel. This value provides an upper limit
to calculations so that simulations do not return unphysical
values.

#### Dependencies

To enable this parameter, set one of the following
parameters:

- **Positive spool position open
  connections** to `P-B,
  A-T` or `P-A, P-B, A-T,
  B-T`.
- **Negative spool position open
  connections** to `P-B,
  A-T` or `P-A, P-B, A-T,
  B-T`.

And either:

- **Modeling option** to
  `Liquid operating condition`,
  **Area characteristics** to
  `Different for each flow path`,
  and **Orifice parameterization** to
  `Linear - Area vs. spool
  travel` or `Linear - Nominal
  mass flow rate vs. spool travel`.
- **Modeling option** to `Vapor
  operating condition`, **Area
  characteristics** to `Different for
  each flow path`, and **Opening
  characteristic** to
  `Linear`.

### **A-T nominal mass flow rate at maximum orifice opening** — Rated mass flow rate `0.1` `kg/s` (default) | positive scalar

Typical, rated, or design mass flow rate through a maximally open A-T
orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. One of the following parameters:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

### **A-T nominal pressure drop at maximum orifice opening** — Rated pressure drop `0.001` `MPa` (default) | positive scalar

Typical, rated, or design pressure drop through a maximally open A-T
orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. One of the following parameters:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

### **A-T nominal inlet condition specification** — Method of determining inlet fluid state `Temperature` (default) | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

Method of determining the inlet fluid state for A-T orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. At least one of the following parameters:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

### **A-T nominal inlet pressure** — Inlet fluid pressure `0.101325` `MPa` (default) | positive scalar

Inlet pressure for the A-T orifice at nominal conditions.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. At least one of the following parameters:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

### **A-T nominal inlet temperature** — Fluid temperature `293.15` `K` (default) | positive scalar

Inlet fluid temperature for the A-T orifice in nominal operating conditions.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** to
   `Temperature`
5. At least one of the following parameters:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

### **A-T nominal inlet vapor quality** — Inlet vapor quality mass fraction `0` (default) | positive scalar in the range [0,1]

Inlet mixture vapor quality by mass fraction for the A-T orifice in nominal operating
conditions. A value of `0` means that the inlet fluid
is subcooled liquid. A value of `1` means that the
inlet fluid is superheated vapor.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** to `Vapor
   quality`
5. At least one of the following parameters:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

### **A-T nominal inlet vapor void fraction** — Inlet vapor void fraction `0` (default) | positive scalar in the range [0,1]

Inlet mixture vapor void fraction for the A-T orifice in nominal operating conditions. A
value of `0` means that the inlet fluid is subcooled
liquid. A value of `1` means that the inlet fluid is
superheated vapor.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** to `Vapor void
   fraction`
5. At least one of the following parameters:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

### **A-T nominal inlet specific enthalpy** — Inlet fluid specific enthalpy `400` `kJ/kg` (default) | positive scalar

Inlet specific enthalpy for the A-T orifice in nominal operating conditions.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** to `Specific
   enthalpy`
5. At least one of the following parameters:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

### **A-T nominal inlet specific internal energy** — Inlet specific internal energy `400` `kJ/kg` (default) | positive scalar

Inlet specific internal energy for the A-T orifice in nominal operating
conditions.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** to `Specific
   internal energy`
5. At least one of the following parameters:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

### **A-T constant orifice nominal mass flow rate** — Nominal mass flow rate `0.1` `kg/s` (default) | positive scalar

Typical, rated, or design mass flow rate through a constant A-T
orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. One of the following settings in each
   parameter:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

**Note:**

This parameter is enabled only when the A-T orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **A-T constant orifice nominal pressure drop** — Nominal pressure drop `0.001` `MPa` (default) | positive scalar

Typical, rated, or design pressure drop through a constant A-T
orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. One of the following settings in each
   parameter:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

**Note:**

This parameter is enabled only when the A-T orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **A-T constant orifice Cv flow coefficient** — Flow coefficient `4` (default) | positive scalar

Value of the constant *Cv* flow coefficient for
the A-T orifice. This parameter measures the ease with which the vapor
traverses the resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Cv flow
   coefficient`
4. One of the following settings in each
   parameter:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

**Note:**

This parameter is enabled only when the A-T orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **A-T orifice maximum Cv flow coefficient** — *Cv* coefficient that corresponds to maximally open component `4` (default) | positive scalar

Value of the *Cv* flow
coefficient when the A-T orifice is fully open and the area available
for flow is at a maximum. This parameter measures the ease with which
the vapor traverses the resistive element when driven by a pressure
differential.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Cv flow
   coefficient`
4. **Opening characteristic** to
   `Linear`
5. One of the following parameters:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

### **A-T orifice Cv flow coefficient vector** — *Cv* coefficients for values in member position vector `[1e-06, .8, 1.6, 2.4, 3.2, 4]` (default) | 1-by-*n* vector

Vector of *Cv* flow
coefficients. Each coefficient corresponds to a value in the
**A-T orifice spool travel vector** parameter. This
parameter measures the ease with which the vapor traverses the resistive
element when driven by a pressure differential. The size of the vector
must be the same as the **A-T orifice spool travel
vector** parameter.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Cv flow
   coefficient`
4. **Opening characteristic** to
   `Tabulated`
5. One of the following parameters:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

### **A-T constant orifice Kv flow coefficient** — Flow coefficient `3.6` (default) | positive scalar

Value of the constant *Kv* flow coefficient for
the A-T orifice. This parameter measures the ease with which the vapor
traverses the resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Kv flow
   coefficient`
4. One of the following settings in each
   parameter:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

**Note:**

This parameter is enabled only when the A-T orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **A-T orifice maximum Kv flow coefficient** — *Kv* coefficient that corresponds to maximally open component `3.6` (default) | positive scalar

Value of the *Kv* flow
coefficient when the A-T orifice is fully open and the area available
for flow is at a maximum. This parameter measures the ease with which
the vapor traverses the resistive element when driven by a pressure
differential.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Kv flow
   coefficient`
4. **Opening characteristic** to
   `Linear`
5. One of the following parameters:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

### **A-T orifice Kv flow coefficient vector** — *Kv* coefficients for values in member position vector `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` (default) | 1-by-*n* vector

Vector of *Kv* flow
coefficients. Each coefficient corresponds to a value in the
**A-T orifice spool travel vector** parameter. This
parameter measures the ease with which the vapor traverses the resistive
element when driven by a pressure differential. The size of the vector
must be the same as the **A-T orifice spool travel
vector** parameter.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Kv flow
   coefficient`
4. **Opening characteristic** to
   `Tabulated`
5. One of the following parameters:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

### **A-T orifice spool travel vector** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances for the tabular parameterization of
the valve area. List the values in ascending order. The first element
must be 0. The block uses linear interpolation between table data
points.

#### Dependencies

To enable this parameter, set one of the following
parameters:

- **Positive spool position open
  connections** to `P-B,
  A-T` or `P-A, P-B, A-T,
  B-T`.
- **Negative spool position open
  connections** to `P-B,
  A-T` or `P-A, P-B, A-T,
  B-T`.

And either:

- **Modeling option** to
  `Liquid operating condition`,
  **Area characteristics** to
  `Different for each flow path`,
  and **Orifice parameterization** to
  `Tabulated data - Area vs. spool
  travel`.
- **Modeling option** to `Vapor
  operating condition`, **Area
  characteristics** to `Different for
  each flow path`, and **Opening
  characteristic** to
  `Tabulated`.

### **A-T maximum orifice area** — Maximum orifice opening area `1e-4 m^2` (default) | positive scalar

Largest open area of the A-T orifice during the operation of the
valve.

#### Dependencies

To enable this parameter, set one of the following parameters:

- **Positive spool position open
  connections** to `P-B,
  A-T` or `P-A, P-B, A-T,
  B-T`.
- **Negative spool position open
  connections** to `P-B,
  A-T` or `P-A, P-B, A-T,
  B-T`.

Also set **Area characteristics** to
`Different for each flow path` and
either:

- **Modeling option** to
  `Liquid operating condition`
  and **Orifice parameterization** to
  `Linear - Area vs. spool
  travel`.
- **Modeling option** to `Vapor
  operating condition`, **Orifice
  parameterization** to `Orifice
  area`, and **Opening
  characteristic** to
  `Linear`.

### **A-T orifice area vector** — Vector of valve opening areas `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of opening areas for the tabular parameterization of the valve area. The vector
elements must correspond one-to-one with the elements in the
**A-T orifice spool travel vector** parameter. The
elements must be greater than 0 and listed in ascending order.

#### Dependencies

To enable this parameter, set one of the following parameters:

- **Positive spool position open
  connections** to `P-B,
  A-T` or `P-A, P-B, A-T,
  B-T`.
- **Negative spool position open
  connections** to `P-B,
  A-T` or `P-A, P-B, A-T,
  B-T`.

Also set **Area characteristics** to
`Different for each flow path` and
either:

- **Modeling option** to
  `Liquid operating condition`
  and **Orifice parameterization** to
  `Tabulated data - Area vs. spool
  travel`.
- **Modeling option** to `Vapor
  operating condition`, **Orifice
  parameterization** to `Orifice
  area`, and **Opening
  characteristic** to
  `Tabulated`.

### **A-T constant orifice area** — Cross-sectional area for constant orifice `1e-4 m^2` (default) | positive scalar

Orifice area when the positive and negative spool positions include
the same orifice.

#### Dependencies

To enable this parameter, set one of the following settings in
each parameter:

- **Positive spool position open
  connections** to `P-B,
  A-T` or `P-A, P-B, A-T,
  B-T`.
- **Negative spool position open
  connections** to `P-B,
  A-T` or `P-A, P-B, A-T,
  B-T`.

And either:

- **Modeling option** to
  `Liquid operating condition`,
  **Area characteristics** to
  `Different for each flow path`,
  and **Orifice parameterization** to
  `Tabulated data - Area vs. spool
  travel` or `Linear - Area vs.
  spool travel`.
- **Modeling option** to `Vapor
  operating condition`, **Area
  characteristics** to `Different for
  each flow path`, and **Opening
  characteristic** to
  `Tabulated`.

**Note:**

This parameter is enabled only when the A-T orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **A-T orifice xT pressure differential ratio factor at choked flow** — Ratio of pressure differentials `0.7` (default) | positive scalar

Ratio between the inlet pressure, *pin*, and the
outlet pressure, *pout*, defined
as (pin−pout)/pin where choking first occurs for the A-T orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Kv flow coefficient` or
   `Cv flow
   coefficient`
4. At least one of the following parameters:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

### B-T Orifice

### **Spool position at maximum B-T orifice area** — Spool offset for fully open B-T orifice `5e-3 m` (default) | positive scalar

Spool offset from the neutral position for a fully open B-T
orifice.

#### Dependencies

To enable this parameter, set one of these parameters.

- **Positive spool position open
  connections** to `P-A,
  B-T` or `P-A, P-B, A-T,
  B-T`.
- **Negative spool position open
  connections** to `P-A,
  B-T` or `P-A, P-B, A-T,
  B-T`.

**Note:**

This parameter is enabled only when the B-T orifice
settings do not appear in both the **Positive spool position open connections** and
**Negative spool position open
connections** parameters.

### **B-T spool travel between closed and open orifice** — Maximum spool stroke `0.005 m` (default) | positive scalar

Maximum distance of spool travel. This value provides an upper limit
to calculations so that simulations do not return unphysical
values.

#### Dependencies

To enable this parameter, set one of the following
parameters:

- **Positive spool position open
  connections** to `P-A,
  B-T` or `P-A, P-B, A-T,
  B-T`.
- **Negative spool position open
  connections** to `P-A,
  B-T` or `P-A, P-B, A-T,
  B-T`.

And either:

- **Modeling option** to
  `Liquid operating condition`,
  **Area characteristics** to
  `Different for each flow path`,
  and **Orifice parameterization** to
  `Linear - Area vs. spool
  travel` or `Linear - Nominal
  mass flow rate vs. spool travel`.
- **Modeling option** to `Vapor
  operating condition`, **Area
  characteristics** to `Different for
  each flow path`, and **Opening
  characteristic** to
  `Linear`.

### **B-T nominal mass flow rate at maximum orifice opening** — Rated mass flow rate `0.1` `kg/s` (default) | positive scalar

Typical, rated, or design mass flow rate through a maximally open B-T
orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. One of the following parameters:

   - **Positive spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.

### **B-T nominal pressure drop at maximum orifice opening** — Rated pressure drop `0.001` `MPa` (default) | positive scalar

Typical, rated, or design pressure drop through a maximally open B-T
orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. One of the following parameters:

   - **Positive spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.

### **B-T nominal inlet condition specification** — Method of determining inlet fluid state `Temperature` (default) | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

Method of determining the inlet fluid state for B-T orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. At least one of the following parameters:

   - **Positive spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.

### **B-T nominal inlet pressure** — Inlet fluid pressure `0.101325` `MPa` (default) | positive scalar

Inlet pressure for the B-T orifice at nominal conditions.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. At least one of the following parameters:

   - **Positive spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.

### **B-T nominal inlet temperature** — Fluid temperature `293.15` `K` (default) | positive scalar

Inlet fluid temperature for the B-T orifice in nominal operating conditions.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** to
   `Temperature`
5. At least one of the following parameters:

   - **Positive spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.

### **B-T nominal inlet vapor quality** — Inlet vapor quality mass fraction `0` (default) | positive scalar in the range [0,1]

Inlet mixture vapor quality by mass fraction for the B-T orifice in nominal operating
conditions. A value of `0` means that the inlet fluid
is subcooled liquid. A value of `1` means that the
inlet fluid is superheated vapor.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** to `Vapor
   quality`
5. At least one of the following parameters:

   - **Positive spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.

### **B-T nominal inlet vapor void fraction** — Inlet vapor void fraction `0` (default) | positive scalar in the range [0,1]

Inlet mixture vapor void fraction for the B-T orifice in nominal operating conditions. A
value of `0` means that the inlet fluid is subcooled
liquid. A value of `1` means that the inlet fluid is
superheated vapor.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** to `Vapor void
   fraction`
5. At least one of the following parameters:

   - **Positive spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.

### **B-T nominal inlet specific enthalpy** — Inlet fluid specific enthalpy `400` `kJ/kg` (default) | positive scalar

Inlet specific enthalpy for the B-T orifice in nominal operating conditions.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** to `Specific
   enthalpy`
5. At least one of the following parameters:

   - **Positive spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.

### **B-T nominal inlet specific internal energy** — Inlet specific internal energy `400` `kJ/kg` (default) | positive scalar

Inlet specific internal energy for the B-T orifice in nominal operating
conditions.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** to `Specific
   internal energy`
5. At least one of the following parameters:

   - **Positive spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.

### **B-T constant orifice nominal mass flow rate** — Nominal mass flow rate `0.1` `kg/s` (default) | positive scalar

Typical, rated, or design mass flow rate through a constant B-T
orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. One of the following settings in each
   parameter:

   - **Positive spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.

**Note:**

This parameter is enabled only when the B-T orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **B-T constant orifice nominal pressure drop** — Nominal pressure drop `0.001` `MPa` (default) | positive scalar

Typical, rated, or design pressure drop through a constant B-T
orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Liquid operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. One of the following settings in each
   parameter:

   - **Positive spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.

**Note:**

This parameter is enabled only when the B-T orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **B-T constant orifice Cv flow coefficient** — Flow coefficient `4` (default) | positive scalar

Value of the constant *Cv* flow coefficient for
the B-T orifice. This parameter measures the ease with which the vapor
traverses the resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Cv flow
   coefficient`
4. One of the following settings in each
   parameter:

   - **Positive spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.

**Note:**

This parameter is enabled only when the B-T orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **B-T orifice maximum Cv flow coefficient** — *Cv* coefficient that corresponds to maximally open component `4` (default) | positive scalar

Value of the *Cv* flow
coefficient when the B-T orifice is fully open and the area available
for flow is at a maximum. This parameter measures the ease with which
the vapor traverses the resistive element when driven by a pressure
differential.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Cv flow
   coefficient`
4. **Opening characteristic** to
   `Linear`
5. One of the following parameters:

   - **Positive spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.

### **B-T orifice Cv flow coefficient vector** — *Cv* coefficients for values in member position vector `[1e-06, .8, 1.6, 2.4, 3.2, 4]` (default) | 1-by-*n* vector

Vector of *Cv* flow
coefficients. Each coefficient corresponds to a value in the
**B-T orifice spool travel vector** parameter. This
parameter measures the ease with which the vapor traverses the resistive
element when driven by a pressure differential. The size of the vector
must be the same as the **B-T orifice spool travel
vector** parameter.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Cv flow
   coefficient`
4. **Opening characteristic** to
   `Tabulated`
5. One of the following parameters:

   - **Positive spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.

### **B-T constant orifice Kv flow coefficient** — Flow coefficient `3.6` (default) | positive scalar

Value of the constant *Kv* flow coefficient for
the B-T orifice. This parameter measures the ease with which the vapor
traverses the resistive element when driven by a pressure differential.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Kv flow
   coefficient`
4. One of the following settings in each
   parameter:

   - **Positive spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.

**Note:**

This parameter is enabled only when the B-T orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **B-T orifice maximum Kv flow coefficient** — *Kv* coefficient that corresponds to maximally open component `3.6` (default) | positive scalar

Value of the *Kv* flow
coefficient when the B-T orifice is fully open and the area available
for flow is at a maximum. This parameter measures the ease with which
the vapor traverses the resistive element when driven by a pressure
differential.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Kv flow
   coefficient`
4. **Opening characteristic** to
   `Linear`
5. One of the following parameters:

   - **Positive spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.

### **B-T orifice Kv flow coefficient vector** — *Kv* coefficients for values in member position vector `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` (default) | 1-by-*n* vector

Vector of *Kv* flow
coefficients. Each coefficient corresponds to a value in the
**B-T orifice spool travel vector** parameter. This
parameter measures the ease with which the vapor traverses the resistive
element when driven by a pressure differential. The size of the vector
must be the same as the **B-T orifice spool travel
vector** parameter.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Kv flow
   coefficient`
4. **Opening characteristic** to
   `Tabulated`
5. One of the following parameters:

   - **Positive spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.

### **B-T orifice spool travel vector** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances for the tabular parameterization of
the valve area. List the values in ascending order. The first element
must be 0. The block uses linear interpolation between table data
points.

#### Dependencies

To enable this parameter, set one of the following
parameters:

- **Positive spool position open
  connections** to `P-A,
  B-T` or `P-A, P-B, A-T,
  B-T`.
- **Negative spool position open
  connections** to `P-A,
  B-T` or `P-A, P-B, A-T,
  B-T`.

And either:

- **Modeling option** to
  `Liquid operating condition`,
  **Area characteristics** to
  `Different for each flow path`,
  and **Orifice parameterization** to
  `Tabulated data - Area vs. spool
  travel`.
- **Modeling option** to `Vapor
  operating condition`, **Area
  characteristics** to `Different for
  each flow path`, and **Opening
  characteristic** to
  `Tabulated`.

### **B-T maximum orifice area** — Maximum orifice opening area `1e-4 m^2` (default) | positive scalar

Largest open area of the B-T orifice during the operation of the
valve.

#### Dependencies

To enable this parameter, set one of the following parameters:

- **Positive spool position open
  connections** to `P-A,
  B-T` or `P-A, P-B, A-T,
  B-T`.
- **Negative spool position open
  connections** to `P-A,
  B-T` or `P-A, P-B, A-T,
  B-T`.

Also set **Area characteristics** to
`Different for each flow path` and
either:

- **Modeling option** to
  `Liquid operating condition`
  and **Orifice parameterization** to
  `Linear - Area vs. spool
  travel`.
- **Modeling option** to `Vapor
  operating condition`, **Orifice
  parameterization** to `Orifice
  area`, and **Opening
  characteristic** to
  `Linear`.

### **B-T orifice area vector** — Vector of valve opening areas `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of opening areas for the tabular parameterization of the valve area. The vector
elements must correspond one-to-one with the elements in the
**B-T orifice spool travel vector** parameter. The
elements must be greater than 0 and listed in ascending order.

#### Dependencies

To enable this parameter, set one of the following parameters:

- **Positive spool position open
  connections** to `P-A,
  B-T` or `P-A, P-B, A-T,
  B-T`.
- **Negative spool position open
  connections** to `P-A,
  B-T` or `P-A, P-B, A-T,
  B-T`.

Also set **Area characteristics** to
`Different for each flow path` and
either:

- **Modeling option** to
  `Liquid operating condition`
  and **Orifice parameterization** to
  `Tabulated data - Area vs. spool
  travel`.
- **Modeling option** to `Vapor
  operating condition`, **Orifice
  parameterization** to `Orifice
  area`, and **Opening
  characteristic** to
  `Tabulated`.

### **B-T constant orifice area** — Cross-sectional area for constant orifice `1e-4 m^2` (default) | positive scalar

Orifice area when the positive and negative spool positions include
the same orifice.

#### Dependencies

To enable this parameter, set one of the following settings in
each parameter:

- **Positive spool position open
  connections** to `P-A,
  B-T` or `P-A, P-B, A-T,
  B-T`.
- **Negative spool position open
  connections** to `P-A,
  B-T` or `P-A, P-B, A-T,
  B-T`.

And either:

- **Modeling option** to
  `Liquid operating condition`,
  **Area characteristics** to
  `Different for each flow path`,
  and **Orifice parameterization** to
  `Tabulated data - Area vs. spool
  travel` or `Linear - Area vs.
  spool travel`.
- **Modeling option** to `Vapor
  operating condition`, **Area
  characteristics** to `Different for
  each flow path`, and **Opening
  characteristic** to
  `Tabulated`.

**Note:**

This parameter is enabled only when the B-T orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **B-T orifice xT pressure differential ratio factor at choked flow** — Ratio of pressure differentials `0.7` (default) | positive scalar

Ratio between the inlet pressure, *pin*, and the
outlet pressure, *pout*, defined
as (pin−pout)/pin where choking first occurs for the B-T orifice.

#### Dependencies

To enable this parameter, set:

1. **Modeling option** to
   `Vapor operating
   condition`
2. **Area characteristics** to
   `Different for each flow
   path`
3. **Orifice parameterization** to
   `Kv flow coefficient` or
   `Cv flow
   coefficient`
4. At least one of the following parameters:

   - **Positive spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-A,
     B-T` or `P-A, P-B, A-T,
     B-T`.

## Libraries

Simscape / Fluids / Two-Phase Fluid / Valves & Orifices / Directional Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

4-Way 2-Position Directional Valve in the two-phase fluid domain

The 4-Way 2-Position Directional Valve (2P) models a valve with four openings — such
as the valves between an actuator, pump, and tank — in a two-phase fluid network. A
single spool controls the valve operation according to the signal at port
**S**. You can set the baseline configuration of your valve by
specifying the orifices that are open when the spool moves in the positive direction and
negative directions in the **Positive spool position open connections**
and **Negative spool position open connections** parameters,
respectively. You can set the valve opening model in the **Orifice
parameterization** parameter as a linear relationship or function of
user-provided data, which you can apply to one or all flow paths in the valve.

This block is a composite component that comprises of multiple instances of the
Orifice
(2P) block. Refer to the Orifice
(2P) block for more details about valve parameterizations and block
calculations. In some configurations, this valve resembles a 3-way valve. To set
additional flow paths when the spool is in the neutral position, see the 4-Way 3-Position
Directional Valve (2P) block.

This image shows an example valve setup where the valve is connected to a tank,
actuator, and pump and the **Positive spool position open connections**
parameter is `P-B, A-T`:

This image shows the valve when the **Negative spool position open
connections** parameter is `P-A, B-T`:

In this configuration, when the signal at port **S** moves the spool
to a negative position, the paths between ports **P** and
**A** and between ports **B** and
**T** are open to flow. The paths between ports
**P** and **B** and ports **A**
and **T** are closed to flow.

This image shows the valve when the **Positive spool position open
connections** parameter is `P-B, A-T`:

In this configuration, when the signal at port **S** moves the spool
to a positive position, the paths between ports **P** and
**B** and between ports **A** and
**T** are open to flow and the paths between ports
**P** and **A** and between ports
**B** and **T** are closed.

The schematic that represents this configuration is:

The left-hand side corresponds to the positive position and the
right-hand side corresponds to the negative position. The valve transitions through
positions in the neutral mid-section.

### Spool Displacement and Valve Configuration

The *spool stroke* is the amount of spool travel an orifice
takes to fully open from a closed position. You can use the **Orifice
parameterization** and **Area characteristics**
parameters to specify the flow path characteristics:

| Orifice Parameterization | Identical for All Flow Paths | Different for Each Flow Path |
| --- | --- | --- |
| `Linear - Area vs. spool travel` | The **Spool travel between closed and open orifice** parameter defines the spool stroke | The **Spool travel between closed and open orifice** parameter defines the spool stroke for each orifice |
| `Tabulated data - Area vs. spool travel` | The difference between the first and last element of the **Spool travel vector** parameter defines the spool stroke | The difference between the first and last element of the **Spool travel vector** parameter for each orifice |
| `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`or `Tabulated data - Mass flow rate vs. spool travel and pressure drop` | The difference between the first and last element of the **Spool travel vector, ds** parameter defines the spool stroke | The difference between the first and last element of the **Spool travel vector, ds** parameter defines the spool stroke for each orifice |

The direction of the spool movement depends on the spool stroke, orifice
orientation, and signal at port **S**. This table shows the spool
travel for an orifice depending on the selections for the **Positive spool
position open connection** and **Negative spool position open
connection** parameters:

| Spool Position When Orifice Is Open | Spool Travel, *ΔS* |
| --- | --- |
| Orifice always closed: orifice not selected for the **Positive spool position open connection** or **Negative spool position open connection** parameters | N/A |
| Orifice always open: orifice selected for both the **Positive spool position open connection** and **Negative spool position open connection** parameters | N/A |
| Negative: orifice selected for only **Negative spool position open connection** parameter | *S*orifice\_max + spool stroke – **S** |
| Positive: orifice selected for only **Positive spool position open connection** parameter | *S*orifice\_max – spool stroke + **S** |

Where *S*orifice\_max is the spool position
at the maximum orifice area defined for each orifice. The orifice area saturates at
the leakage area when *ΔS* is negative and saturates at the maximum
orifice area when the orifice is fully open. When the orifice is fully open,
*ΔS* is equal to the spool stroke, so *ΔS*
greater than the spool stroke does not further increase the orifice area.

This table shows the possible configurations of the 4-Way 2-Position Directional
Valve (TL):

| Configuration | Parameter Values |
| --- | --- |
| All four paths are closed during transition. | - **Positive spool position open   connections**: `P-A,   B-T` - **Negative spool position open   connections**: `P-B,   A-T`  - **Spool position at maximum P-A orifice   area** > P-A spool stroke - **Spool position at maximum P-B orifice   area** < –P-B spool stroke - **Spool position at maximum A-T orifice   area** < –A-T spool stroke - **Spool position at maximum B-T orifice   area** > B-T spool stroke |
| All four paths are open during transition. | - **Positive spool position open   connections**: `P-A,   B-T` - **Negative spool position open   connections**: `P-B,   A-T`  - **Spool position at maximum P-A orifice   area** < P-A spool stroke - **Spool position at maximum P-B orifice   area** > –P-B spool stroke - **Spool position at maximum A-T orifice   area** > –A-T spool stroke - **Spool position at maximum B-T orifice   area** < B-T spool stroke |
| A-T and B-T are closed during transition. | - **Positive spool position open   connections**: `P-A,   B-T` - **Negative spool position open   connections**: `P-B,   A-T`  - **Spool position at maximum P-A orifice   area** < P-A spool stroke - **Spool position at maximum P-B orifice   area** > –P-B spool stroke - **Spool position at maximum A-T orifice   area** < –A-T spool stroke - **Spool position at maximum B-T orifice   area** > B-T spool stroke |
| P-A and P-B are closed during transition. | - **Positive spool position open   connections**:   `P-A` - **Negative spool position open   connections**:   `P-B`  - **Spool position at maximum P-A orifice   area** > P-A spool stroke - **Spool position at maximum P-B orifice   area** < –P-B spool stroke |
| P-B and B-T are closed during transition. | - **Positive spool position open   connections**: `P-B,   A-T` - **Negative spool position open   connections**: `P-A,   B-T`  - **Spool position at maximum P-A orifice   area** < P-A spool stroke - **Spool position at maximum P-B orifice   area** > P-B spool stroke - **Spool position at maximum A-T orifice   area** > A-T spool stroke - **Spool position at maximum B-T orifice   area** < –B-T spool stroke |
| P-A and A-T are closed during transition. | - **Positive spool position open   connections**: `P-B,   A-T` - **Negative spool position open   connections**: `P-A,   B-T`  - **Spool position at maximum P-A orifice   area** < –P-A spool stroke - **Spool position at maximum P-B orifice   area** < P-B spool stroke - **Spool position at maximum A-T orifice   area** > A-T spool stroke - **Spool position at maximum B-T orifice   area** > –B-T spool stroke |
| P-A, P-B, and B-T are open during transition. | - **Positive spool position open   connections**: `P-A,   P-B` - **Negative spool position open   connections**: `P-A,   B-T`  - **Spool position at maximum P-A orifice   area** < P-A spool stroke - **Spool position at maximum P-B orifice   area** < P-B spool stroke - **Spool position at maximum A-T orifice   area** = any value - **Spool position at maximum B-T orifice   area** > –B-T spool stroke |
| P-A, A-T, and B-T are open during transition. | - **Positive spool position open   connections**: `P-B,   A-T` - **Negative spool position open   connections**: `P-A,   P-B`  - **Spool position at maximum P-A orifice   area** > –P-A spool stroke - **Spool position at maximum A-T orifice   area** < A-T spool stroke - **Spool position at maximum B-T orifice   area** = any value |
| P-A and P-B are closed during transition. A-T is always closed. | - **Positive spool position open   connections**: `P-A,   P-B` - **Negative spool position open   connections**: `P-A,   B-T`  - **Spool position at maximum P-B orifice   area** > P-B spool stroke - **Spool position at maximum B-T orifice   area** < –B-T spool stroke |
| All paths are closed during transition. | - **Positive spool position open   connections**: `P-B,   A-T` - **Negative spool position open   connections**: `P-A,   P-B`  - **Spool position at maximum P-A orifice   area** < –P-A spool stroke - **Spool position at maximum P-B orifice   area** > P-B spool stroke - **Spool position at maximum A-T orifice   area** > A-T spool stroke |
| A-T is open during transition. P-A is closed during transition. | - **Positive spool position open   connections**: `P-A,   P-B` - **Negative spool position open   connections**: `P-A,   B-T`  - **Spool position at maximum P-A orifice   area** > P-A spool stroke - **Spool position at maximum P-B orifice   area** > P-B spool stroke - **Spool position at maximum A-T orifice   area** = any value - **Spool position at maximum B-T orifice   area** > –B-T spool stroke |
| B-T is open during transition. P-B is closed during transition. | - **Positive spool position open   connections**: `P-B,   A-T` - **Negative spool position open   connections**: `P-A,   P-B`  - **Spool position at maximum P-A orifice   area** < –P-A spool stroke - **Spool position at maximum P-B orifice   area** > P-B spool stroke - **Spool position at maximum A-T orifice   area** < A-T spool stroke - **Spool position at maximum B-T orifice   area** = any value |
| P-A is closed during transition. | - **Positive spool position open   connections**: `P-A,   B-T` - **Negative spool position open   connections**: `P-A,   P-B`  - **Spool position at maximum P-A orifice   area** > P-A spool stroke - **Spool position at maximum P-B orifice   area** < –P-B spool stroke - **Spool position at maximum B-T orifice   area** > B-T spool stroke |
| P-B is closed during transition. | - **Positive spool position open   connections**: `P-A,   P-B` - **Negative spool position open   connections**: `P-B,   A-T`  - **Spool position at maximum P-A orifice   area** > P-A spool stroke - **Spool position at maximum P-B orifice   area** > P-B spool stroke - **Spool position at maximum A-T orifice   area** > –A-T spool stroke |

### Valve Orifice Parameterizations

The **Modeling option** parameter controls the parameterization
options for a valve designed for modeling either vapor or liquid, but does not
impact the fluid properties. The block calculates fluid properties inside the valve
from inlet conditions.

The **Orifice parameterization** parameter specifies the model
for the open area or flow rate through one or all of the valve orifices. If you set
**Area characteristics** to `Identical for all flow
paths`, the block applies the same data for all flow paths. When
you select `Different for all flow paths`, the block uses
individual parameterizations for each flow path.

**Liquid Valve Parameterization**

When **Modeling option** is `Liquid operating
condition`, the block parameterizations are designed for a
valve controlling liquid flow.

When **Orifice parameterization** is `Linear -
Area vs. spool travel`, the opening area is a linear function
of the spool position received as a signal at port **S**

Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak,

where:

- *ΔS* is the spool travel.

  *Aorifice* saturates at
  *Aleak* when
  *ΔS* is negative and saturates at
  *Amax* when the orifice
  is fully open. When the orifice is fully open, *ΔS* is
  equal to the spool stroke, so a value of *ΔS* that is
  greater than the spool stroke does not increase the orifice area.
- *ΔSmax* is the value of the
  **Spool travel between closed and open orifice**
  parameter.
- *Amax* is the value of the
  **Maximum orifice area** parameter.
- *Aleak* is the value of the
  **Leakage area** parameter.

  When the valve is in a near-open or near-closed position in the
  linear parameterization, you can maintain numerical robustness in your simulation by adjusting
  the **Smoothing factor** parameter. If the **Smoothing
  factor** parameter is nonzero, the block smoothly saturates the opening area
  between *Aleak* and
  *Amax*. For more information, see Numerical Smoothing.

When **Orifice parameterization** is `Tabulated data - Area
vs. spool travel`, you can provide spool travel vectors for
your system or for individual flow paths between ports **P**,
**A**, **B**, and **T**.
The block uses this data to calculate the relationship between the orifice area
and spool displacement. The block uses interpolation to determine the opening
area between given data points. *A*leak
and *A*max are the first and last
parameters of the opening area vector, respectively.

When **Orifice parameterization** is `Tabulated
data - Nominal mass flow rate vs. spool travel`, the block
calculates the mass flow rate for each orifice from the nominal conditions you
specify in the block parameters. The spool position signal from port
**S** scales the orifice opening area, which can also scale
mass flow rate.

**Vapor Valve Parameterization**

When **Modeling option** is `Vapor operating
condition`, the block parameterizations are designed to model a
valve that controls vapor flow.

The method the block uses to control each orifice depends on the
**Opening characteristic** parameter:

- `Linear` — The measure of flow capacity
  depends on the spool position at port **S**. As the spool displaces to open to orifice, the measure of
  flow capacity scales from the specified minimum to the specified
  maximum.
- `Tabulated` — The block calculates the
  measure of flow capacity as a function of the spool position at port
  **S**. This function uses a
  one-dimensional lookup table.

The **Orifice parameterization** parameter determines how the
block calculates the flow rate in each orifice:

- `Cv flow coefficient` — The flow coefficient
  *C*v
  scales the flow rate in each orifice. The flow coefficient measures the
  ease with which a fluid can flow when driven by a certain pressure
  differential.
- `Kv flow coefficient` — The flow coefficient
  *K*v,
  where Kv=0.865Cv, scales the flow rate in each orifice. The flow
  coefficient measures the ease with which a fluid can flow when driven by
  a certain pressure differential.
- `Orifice area` — The size of the orifice area
  scales the flow rate in each orifice.

### Visualize Orifice Openings

To visualize the spool offsets and maximum displacement, right-click the block and
select **Fluids** > **Plot Valve Characteristics**. The plot shows the orifices specified by the parameters in
**Valve Configuration** section. When you set the parameters
in the **Valve Configuration** tab to the same orifice, the
orifice opening is a constant.

Click **Reload Data** to update the data in the figure.

This image shows the default configuration for the block:

- **Positive spool position open connections** is
  `P-A, B-T`
- **Negative spool position open connections** is
  `P-B, A-T`

All other spool positions are at the default values.

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
