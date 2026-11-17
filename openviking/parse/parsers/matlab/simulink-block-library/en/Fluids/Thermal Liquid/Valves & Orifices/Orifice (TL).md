---
type: simulink-block
title: 'Orifice (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices'
documentation_page: 'orificetl'
documentation_source_path: 'ref/orificetl.html'
language: en
---

# Orifice (TL)

## Ports
```yaml
ports:
- name: S
  summary: Control member displacement, m physical signal
  direction: input
- name: A
  summary: Flow passage thermal liquid
  direction: conserving
- name: B
  summary: Flow passage thermal liquid
  direction: conserving
```

### Input

### **S** — Control member displacement, m physical signal

Instantaneous displacement of the valve control member.
### Conserving

### **A** — Flow passage thermal liquid

Thermal liquid conserving port associated with the opening through which the flow can
enter or exit the valve.

### **B** — Flow passage thermal liquid

Thermal liquid conserving port associated with the opening through which the flow can
enter or exit the valve.
## Parameters
```yaml
parameters:
- name: Orifice type
  summary: Type of orifice Variable (default) | Constant
  group: Parameters
- name: Orifice parameterization
  summary: Constant orifice parameterization Orifice area (default) | Tabulated data - Volumetric flow rate vs. pressure drop
    | Tabulated data - Mass flow rate vs. pressure drop
  group: Parameters
- name: Orifice parameterization
  summary: Variable orifice parameterization Linear - Area vs. control member position (default) | Tabulated data - Area vs.
    control member position | Tabulated data - Volumetric flow rate vs. control member position and pressure drop | Tabulated
    data - Mass flow rate vs. control member position and pressure drop
  group: Parameters
- name: Orifice area
  summary: Area of orifice opening 1e-3 m^2 (default) | positive scalar
  group: Parameters
- name: Pressure drop vector
  summary: Vector of differential pressure values for tabulated parameterization [-4, -3, -2, -1, -.5, 0, .5, 1, 2, 3, 4]
    MPa (default) | 1-by-*n* vector
  group: Parameters
- name: Volumetric flow rate vector
  summary: Vector of volumetric flow rate values [-2.44, -2.12, -1.68, -1.22, -.84, 0, .85, 1.21, 1.7, 2.09, 2.41] .* 1e-3
    m^3/s (default) | 1-by-*n* vector
  group: Parameters
- name: Mass flow rate vector
  summary: Vector of mass flow rate values [-2.44, -2.12, -1.68, -1.22, -.84, 0, .85, 1.21, 1.7, 2.09, 2.41] kg/s (default)
    | vector | 1-by-*n* vector
  group: Parameters
- name: Control member position at closed orifice
  summary: Control member offset 0 m (default) | scalar
  group: Parameters
- name: Control member travel between closed and open orifice
  summary: Control member maximum stroke 5e-3 m (default) | positive scalar
  group: Parameters
- name: Opening orientation
  summary: Direction of member movement that opens the orifice Positive control member displacement opens orifice (default)
    | Negative control member displacement opens orifice
  group: Parameters
- name: Maximum orifice area
  summary: Maximum orifice opening area 1e-4 m^2 (default) | positive scalar
  group: Parameters
- name: Leakage area
  summary: Orifice gap area when in fully closed position 1e-10 m^2 (default) | positive scalar
  group: Parameters
- name: Control member position vector
  summary: Vector of control member positions [0, .002, .004, .007, .017] m (default) | 1-by-*n* vector
  group: Parameters
- name: Orifice area vector
  summary: Vector of orifice opening area values [1e-09, 2.0352e-07, 4.0736e-05, .00011438, .00034356] m^2 (default) | 1-by-*n*
    vector
  group: Parameters
- name: Discharge coefficient
  summary: Discharge coefficient 0.64 (default) | positive scalar
  group: Parameters
- name: Critical Reynolds number
  summary: Upper Reynolds number limit for laminar flow 150 (default) | positive scalar
  group: Parameters
- name: Smoothing factor
  summary: Numerical smoothing factor 0.01 (default) | positive scalar in the range [0,1]
  group: Parameters
- name: Pressure recovery
  summary: Whether to account for pressure increase in area expansions on (default) | off
  group: Parameters
- name: Control member position vector, s
  summary: Vector of opening values [0, .002, .004, .007, .017] m (default) | 1-by-*n* vector
  group: Parameters
- name: Pressure drop vector, dp
  summary: Vector of pressure drop values [.3, .5, .7] MPa (default) | 1-by-*n* vector
  group: Parameters
- name: Volumetric flow rate table, q(s,dp)
  summary: Array of volumetric flow rate values [1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3;
    6, 7.7, 9.13] .* 1e-3 m^3/s (default) | *M*-by-*N* matrix
  group: Parameters
- name: Mass flow rate table, mdot(s,dp)
  summary: Array of mass flow rate values [1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7,
    9.13] kg/s (default) | *M*-by-*N* matrix
  group: Parameters
- name: Reference inflow temperature
  summary: Inlet temperature at which to specify the tabulated data 293.15 K (default) | positive scalar in units of temperature
  group: Parameters
- name: Reference inflow pressure
  summary: Inlet pressure at which to specify the tabulated data 0.101325 MPa (default) | positive scalar in units of pressure
  group: Parameters
- name: Cross-sectional area at ports A and B
  summary: Area at orifice entry or exit 0.01 m^2 (default) | positive scalar
  group: Parameters
- name: Orifice Area fault
  summary: Option to model orifice area fault Add fault
  group: Faults
- name: Opening area when faulted
  summary: Faulted orifice characteristics Closed (default) | Open | Maintain at last value
  group: Faults
```

### Parameters

### **Orifice type** — Type of orifice `Variable` (default) | `Constant`

Type of orifice, defined by the orifice area. When set to
`Variable`, the orifice area varies
according to the input signal received at port
**S**.

- `Orifice area`—The assigned area
  does not change over the simulation.
- `Tabulated data - Volumetric flow rate vs.
  pressure drop`—The area remains constant,
  but the volumetric flow rate through the orifice can vary.
  This value is interpolated directly from the
  **Volumetric flow rate vector** and the
  **Pressure drop vector**
  dataset.
- `Tabulated data - Mass flow rate vs. pressure
  drop`—The area remains constant, but the
  volumetric flow rate through the orifice can vary. This
  value is interpolated directly from the **Mass flow
  rate vector** and the **Pressure drop
  vector** dataset.

When you set **Orifice type** to
`Variable`, there are four options.

- `Linear - Area vs. control member
  position`. Area is determined by a linear
  relationship to the control member position with respect to
  a fully open or fully closed orifice. The position is set by
  a varying physical signal at port
  **S**.
- `Tabulated data - Area vs. control member
  position`. The opening area is interpolated
  from the **Control member position vector**
  and the **Orifice area vector** based on
  the control member position received at port
  **S**.
- `Tabulated data - Volumetric flow rate vs.
  control member position and pressure drop`.
  The volumetric flow rate is directly interpolated from the
  user- provided **Control member position vector,
  s**, **Pressure drop vector,
  dp**, and **Volumetric flow rate table,
  q(s,dp)** parameters based on the control
  member position received at port **S** and
  the pressure drop across ports **A** and
  **B**.
- `Tabulated data - Mass flow rate vs. control
  member position and pressure drop`. The
  mass flow rate is directly interpolated from the user-
  provided **Control member position vector,
  s**, **Pressure drop vector,
  dp**, and **Mass flow rate table,
  mdot(s,dp)** parameters based on the control
  member position received at port **S** and
  the pressure drop across ports **A** and
  **B**.

### **Orifice parameterization** — Constant orifice parameterization `Orifice area` (default) | `Tabulated data - Volumetric flow rate vs. pressure drop` | `Tabulated data - Mass flow rate vs. pressure drop`

Method by which to model the opening characteristics of the orifice.
The default setting prescribes a linear relationship between the orifice
opening area and the orifice opening. The alternative settings allow for
a general, nonlinear relationship to be specified in tabulated form, in
one case between the opening area and the orifice opening, in the other
case between the mass flow rate and both the orifice opening and the
pressure drop between the ports.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Constant`.

### **Orifice parameterization** — Variable orifice parameterization `Linear - Area vs. control member position` (default) | `Tabulated data - Area vs. control member position` | `Tabulated data - Volumetric flow rate vs. control member position and pressure drop` | `Tabulated data - Mass flow rate vs. control member position and pressure drop`

When you set **Orifice type** to
`Variable`, there are four options.

- `Linear - Area vs. control member
  position`. Area is determined by a linear
  relationship to the control member position with respect to
  a fully open or fully closed orifice. The position is set by
  a varying physical signal at port
  **S**.
- `Tabulated data - Area vs. control member
  position`. The opening area is interpolated
  from the **Control member position vector**
  and the **Orifice area vector** based on
  the control member position received at port
  **S**.
- `Tabulated data - Volumetric flow rate vs.
  control member position and pressure drop`.
  The volumetric flow rate is directly interpolated from the
  user- provided **Control member position vector,
  s**, **Pressure drop vector,
  dp**, and **Volumetric flow rate table,
  q(s,dp)** parameters based on the control
  member position received at port **S** and
  the pressure drop across ports **A** and
  **B**.
- `Tabulated data - Mass flow rate vs. control
  member position and pressure drop`. The
  mass flow rate is directly interpolated from the user-
  provided **Control member position vector,
  s**, **Pressure drop vector,
  dp**, and **Mass flow rate table,
  mdot(s,dp)** parameters based on the control
  member position received at port **S** and
  the pressure drop across ports **A** and
  **B**.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable`.

### **Orifice area** — Area of orifice opening `1e-3` `m^2` (default) | positive scalar

Cross-sectional area of the orifice opening.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Constant` and **Orifice
parameterization** to `Orifice
area`.

### **Pressure drop vector** — Vector of differential pressure values for tabulated parameterization `[-4, -3, -2, -1, -.5, 0, .5, 1, 2, 3, 4] MPa` (default) | 1-by-*n* vector

Vector of pressure differential values for the tabulated
parameterization of volumetric flow rate. The values in this vector
correspond one-to-one to values in the **Volumetric flow rate
vector** parameter. The pressure drop vector values are
listed in ascending order. The volumetric flow rate is interpolated
directly from the **Volumetric flow rate vector**
parameter, which depends on the **Pressure drop
vector** parameter.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Constant` and **Orifice
parameterization** to `Tabulated data -
Volumetric flow rate vs. pressure drop`.

### **Volumetric flow rate vector** — Vector of volumetric flow rate values `[-2.44, -2.12, -1.68, -1.22, -.84, 0, .85, 1.21, 1.7, 2.09, 2.41] .* 1e-3 m^3/s` (default) | 1-by-*n* vector

Vector of volumetric flow rate values for the tabulated
parameterization of volumetric flow rate. The values in this vector
correspond one-to-one to values in the **Pressure drop
vector** parameter. The volumetric flow rate is
interpolated directly from the provided **Volumetric flow rate
vector** parameter, which depends on the **Pressure
drop vector** parameter.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Constant` and **Orifice
parameterization** to `Tabulated data -
Volumetric flow rate vs. pressure drop`.

### **Mass flow rate vector** — Vector of mass flow rate values `[-2.44, -2.12, -1.68, -1.22, -.84, 0, .85, 1.21, 1.7, 2.09, 2.41] kg/s` (default) | vector | 1-by-*n* vector

Vector of mass flow rate values for the tabulated parameterization of
volumetric flow rate. The values in this vector correspond one-to-one to
values in the **Pressure drop vector** parameter. The
mass flow rate is interpolated directly from the provided **Mass
flow rate vector** parameter, which depends on the
**Pressure drop vector** parameter.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Constant` and **Orifice
parameterization** to `Tabulated data -
Mass flow rate vs. pressure drop`.

### **Control member position at closed orifice** — Control member offset `0 m` (default) | scalar

Initial control member offset when the variable orifice is fully
closed.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable` and set **Orifice
parameterization** to `Linear – Area vs.
control member position`.

### **Control member travel between closed and open orifice** — Control member maximum stroke `5e-3 m` (default) | positive scalar

Maximum distance the control member travels between closed and open
orifice. The orifice is fully open at the sum of the **Control
member position at closed orifice** and **Control
member travel between closed and open orifice**
parameters.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable` and **Orifice
parameterization** to `Linear - Area vs.
control member position`.

### **Opening orientation** — Direction of member movement that opens the orifice `Positive control member displacement opens orifice` (default) | `Negative control member displacement opens orifice`

Direction of member displacement that opens a variable orifice. A
positive orientation means that a positive signal at
**S** opens the orifice. A negative orientation
means that a negative signal at **S** opens the
orifice.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable` and **Orifice
parameterization** to `Linear - Area vs.
control member position`.

### **Maximum orifice area** — Maximum orifice opening area `1e-4 m^2` (default) | positive scalar

Maximum orifice area experienced during simulation. When using
`Tabulated data - Area vs. control member
position`, the maximum orifice area is the last element
of the **Orifice area vector** parameter.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable` and **Orifice
parameterization** to `Linear - Area vs.
control member position`.

### **Leakage area** — Orifice gap area when in fully closed position `1e-10 m^2` (default) | positive scalar

Sum of all gaps when the valve is in fully closed position. Any area
smaller than this value is maintained at the specified leakage area.
This parameter contributes to numerical stability by maintaining
continuity in the flow.

#### Dependencies

To enable this parameter, set **Orifice** type to
`Variable` and **Orifice
parameterization** to `Linear - Area vs.
control member position`.

### **Control member position vector** — Vector of control member positions `[0, .002, .004, .007, .017] m` (default) | 1-by-*n* vector

Vector of control member positions for the tabulated parameterization
of orifice area. The vector elements correspond one-to-one to the values
in the **Orifice area vector** parameter. The vector
elements must be either strictly monotonically increasing or decreasing.
The orifice opening area is interpolated from the **Orifice area
vector**, which depends on the **Control member
position vector** parameter.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable` and **Orifice
parameterization** to `Tabulated data -
Area vs. control member position`.

### **Orifice area vector** — Vector of orifice opening area values `[1e-09, 2.0352e-07, 4.0736e-05, .00011438, .00034356] m^2` (default) | 1-by-*n* vector

Vector of orifice area values for the tabulated parameterization of
orifice area. The values in this vector correspond one-to-one with the
elements in the **Control member position vector**
parameter. If the vector is increasing, the first element of this vector
is the orifice leakage area and the last element is the maximum orifice
area. If the vector is decreasing, the first element of this vector is
the orifice maximum orifice area and the last element is the leakage
area. The orifice opening area is interpolated from the
**Orifice area vector** parameter, which depends on
the **Control member position vector**
parameter.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable` and **Orifice
parameterization** to `Tabulated data -
Area vs. control member position`.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor that accounts for discharge losses in theoretical
flows.

#### Dependencies

To enable this parameter, set either:

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

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the orifice.

#### Dependencies

To enable this parameter, set either:

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

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change
to the flow response when the orifice is in near-open or near-closed
positions. Set this value to a nonzero value less than one to increase
the stability of your simulation in these regimes.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable` and **Orifice
parameterization** to `Linear - Area vs.
control member position`.

### **Pressure recovery** — Whether to account for pressure increase in area expansions `on` (default) | `off`

Whether to account for pressure increase when fluid flows from a
region of smaller cross-sectional area to a region of larger
cross-sectional area. This increase in pressure is not captured when you
clear **Pressure recovery** check box.

#### Dependencies

To enable this parameter, set either:

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

### **Control member position vector, s** — Vector of opening values `[0, .002, .004, .007, .017] m` (default) | 1-by-*n* vector

Vector of control member positions for tabulated parameterization of volumetric flow
rate. The control member position vector forms an independent axis with
the **Pressure drop vector, dp** parameter for the 2-D
dependent **Volumetric flow rate table, q(s,dp)**
parameter. A positive displacement corresponds to valve opening. The
values are listed in ascending order and the first element must be 0.
Linear interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable` and **Orifice
parameterization** to `Tabulated data -
Volumetric flow rate vs. control member position and pressure
drop` or `Tabulated data - Mass flow
rate vs. control member position and pressure
drop`.

### **Pressure drop vector, dp** — Vector of pressure drop values `[.3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure drop values for tabulated parameterization of volumetric flow rate.
The pressure drop vector forms an independent axis with the
**Control member position vector, s** parameter for
the 2-D dependent **Volumetric flow rate table,
q(s,dp)** parameter. The values are listed in ascending
order and must be greater than 0. Linear interpolation is employed
between table data points.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable` and **Orifice
parameterization** to `Tabulated data -
Volumetric flow rate vs. control member position and pressure
drop`.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable` and **Orifice
parameterization** to `Tabulated data -
Volumetric flow rate vs. control member position and pressure
drop` or `Tabulated data - Mass flow
rate vs. control member position and pressure
drop`.

### **Volumetric flow rate table, q(s,dp)** — Array of volumetric flow rate values `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13] .* 1e-3 m^3/s` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of volumetric flow
rates based on independent values of pressure drop and control member
position. *M* and *N* are the sizes of
the corresponding vectors:

- *M* is the number of elements in the
  **Pressure drop vector, dp**
  parameter.
- *N* is the number of elements in the
  **Control member position vector, s**
  parameter.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable` and **Orifice
parameterization** to `Tabulated data -
Volumetric flow rate vs. control member position and pressure
drop`.

### **Mass flow rate table, mdot(s,dp)** — Array of mass flow rate values `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13]` `kg/s` (default) | *M*-by-*N* matrix

Mass flow rates based on independent values of pressure drop and
control member position. *M* and *N*
are the sizes of the corresponding vectors:

- *M* is the number of elements in the
  **Pressure drop vector, dp**
  parameter.
- *N* is the number of elements in the
  **Control member position vector, s**
  parameter.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable` and **Orifice
parameterization** to `Tabulated data -
Mass flow rate vs. control member position and pressure
drop`.

### **Reference inflow temperature** — Inlet temperature at which to specify the tabulated data `293.15 K` (default) | positive scalar in units of temperature

Nominal inlet temperature, with reference to absolute zero, at which
to specify the tabulated data. This parameter is used to adjust the mass
flow rate according to the temperature measured during
simulation.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Tabulated data -
Mass flow rate vs. opening and pressure
drop`.

### **Reference inflow pressure** — Inlet pressure at which to specify the tabulated data `0.101325 MPa` (default) | positive scalar in units of pressure

Nominal inlet pressure, with reference to absolute zero, at which to
specify the tabulated data. This parameter is used to adjust the mass
flow rate according to the pressure measured during simulation.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Tabulated data -
Mass flow rate vs. opening and pressure
drop`.

### **Cross-sectional area at ports A and B** — Area at orifice entry or exit `0.01 m^2` (default) | positive scalar

Cross-sectional area at the entry and exit ports
**A** and **B**. This area is used
in the pressure-flow rate equation that determines the mass flow rate
through the orifice.

#### Dependencies

To enable this parameter, set either:

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

### Faults

### **Orifice Area fault** — Option to model orifice area fault `Add fault`

Option to model a orifice area fault in the block. When a fault
occurs, the valve area normally set by the opening parameterization is
set based on the value specified in the **Opening area when
faulted** parameter. To add a fault, click the
**Add fault** hyperlink.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable`.

### **Opening area when faulted** — Faulted orifice characteristics `Closed` (default) | `Open` | `Maintain at last value`

Faulted orifice area. You can choose for the orifice to seize at the
fully closed or fully open position, or at the valve area when the fault
triggers.

#### Dependencies

To enable this parameter, set **Orifice type** to
`Variable` and click the **Add
fault** hyperlink.
## Libraries

Simscape / Fluids / Thermal Liquid / Valves & Orifices

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

### R2024b: Model faults with the Simscape faults interface

The Orifice (TL) block now supports the Simscape™ faults interface. To learn more, see Introduction to Simscape Faults.

### R2023b: Model non-monotonic area and volumetric flow rate parameters

The block no loner requires the **Orifice area vector**,
**Volumetric flow rate table, q(s,dp)**, or **Mass flow
rate table, mdot(s,dp)** parameters to monotonically increase or
decrease with respect to the **Control member position vector, s**
parameter.

## Description

Constant-area or variable-area orifice in a thermal liquid system

The Orifice (TL) block models the flow through a local
restriction with a constant or variable opening area. For variable orifices, a control
member connected to port **S** sets the opening position. The opening
area is parametrized either linearly or by lookup table.

The block conserves mass such that

m˙A+m˙B=ρvAAA+ρvBAB=0.

This mass balance implies that there is an increase in velocity when there is a decrease in
area, and there is a reduction in velocity when the flow discharges into a larger area.
In accordance with the Bernoulli principle, this change in velocity results in a region
of lower pressure in the orifice and a higher pressure in the expansion zone. The
resulting increase in pressure, which is called *pressure recovery*,
depends on the discharge coefficient of the orifice and the ratio of the orifice and
port areas.

### Constant Orifices

For constant orifices, the orifice area,
*A*orifice, does not change over the
course of the simulation.

**Using the `Constant` Area Parameterization**

The block calculates the mass flow rate as

m˙=CdAorifice2ρ¯PRloss(1−(AorificeAport)2)pA−pB≈CdAorifice2ρ¯PRloss(1−(AorificeAport)2)pA−pB[(pA−pB)2+Δpcrit]1/4,

where:

- *C*d is the
  **Discharge coefficient** parameter.
- *A*orifice is the
  instantaneous orifice open area.
- *A*port is the
  **Cross-sectional area at ports A and B**
  parameter.
- ρ¯ is the average fluid density.

*PR*loss and
*Δp*crit are calculated in the same
manner for constant and variable orifices.

This approximation for m˙ and the Local
Resistance (TL) block are the same.

**Using the `Tabulated data - Volumetric flow rate vs. pressure
drop` Parameterization**

The volumetric flow rate is determined from the tabulated values of the pressure
differential, *Δp*, which you can provide. If you provide only
non-negative values for both the volumetric flow rate and pressure drop vectors,
the block extrapolates the table to contain negative values. The volumetric flow
rate is interpolated from this extended table.

If the **Volumetric flow rate vector** and **Pressure
drop vector** parameters contain both negative and positive values
but no 0, the block inserts an origin into the vectors to ensure the valve does
not have nonzero flow rate when the pressure drop is 0, which is
non-physical.

### Variable Orifices

For variable orifices, when you set **Opening orientation** to
`Positive control member displacement opens orifice`
opens the orifice when the signal at **S** is positive, while a
`Negative control member displacement opens orifice`
orientation opens the orifice when the signal at **S** is negative.
In both cases, the signal is positive and the orifice opening is set by the
magnitude of the signal.

**Using the `Linear - Area vs. control member
position` Parameterization**

The orifice area *A*orifice is based
on the control member position and the ratio of orifice area and maximum control
member position:

Aorifice=(Amax−Aleak)ΔS(S−Smin)ε+Aleak,

where:

- *S*min is the
  **Control member position at closed orifice**
  parameter.
- *ΔS* is the **Control member travel
  between closed and open orifice** parameter.
- *A*max is the
  **Maximum orifice area** parameter.
- *A*leak is the
  **Leakage area** parameter.
- *ε* is the **Opening
  orientation** parameter.

The volumetric flow rate is determined by the pressure-flow rate equation:

m˙=CdAorifice2ρ¯PRloss(1−(AorificeA)2)Δp[Δp2+Δpcrit2]1/4,

where *A* is the **Cross-sectional
area at ports A and B**.

When the orifice is in a near-open or
near-closed position in the linear parameterization, you can maintain numerical
robustness in your simulation by adjusting the **Smoothing
factor** parameter. If the **Smoothing factor**
parameter is nonzero, the block smoothly saturates the opening area between
*Aleak* and
*Amax*. For more information,
see Numerical Smoothing.

**Using the `Tabulated data - Area vs. control member
position` Parameterization**

When you use the `Tabulated data - Area vs. control member
position` parameterization, the orifice area
*A*orifice is interpolated from the
tabulated values of opening area and the control member position,
*ΔS*, which you can provide. As with the
`Linear - Area vs. control member position`
parameterization, the volumetric flow rate is determined by the pressure-flow
rate equation:

m˙=CdAorifice2ρ¯PRloss(1−(AorificeA)2)Δp[Δp2+Δpcrit2]1/4,

where *A*orifice is:

- *Amax*, the last element
  of the **Orifice area vector** parameter, if the
  physical signal at port **S** is larger than the
  last element of the **Control member position
  vector** parameter.
- *Aleak*, the first element
  of the **Orifice area vector** parameter, if the
  physical signal at port **S** is smaller than the
  first element of the **Control member position
  vector** parameter.
- The linearly interpolated value of the **Orifice area
  vector** parameter if the calculated area is between
  the limits of the first and last element of the **Control
  member position vector** parameter.

*Aorifice* is a function
of the control member position received at port **S**. The
block queries between data points with linear interpolation and uses nearest
extrapolation for points beyond the table boundaries.

**Using the `Tabulated data - Volumetric flow rate vs. control
member position and pressure drop` Parameterization**

The `Tabulated data - Volumetric flow rate vs. control member position and
pressure drop` parameterization interpolates the volumetric
flow rate directly from a user-provided volumetric flow rate table, which is
based on the control member position and pressure drop over the orifice. The
block queries between data points with linear interpolation and uses
nearest
extrapolation with respect to control member position and linear extrapolation
with respect to pressure drop.

This data can include negative pressure drops and negative opening values. If
a negative pressure drop is included in the dataset, the volumetric flow rate
will change direction. However, the flow rate will remain unchanged for negative
opening values.

If the **Pressure drop vector, dp** parameter does not contain a 0 and
the **Volumetric flow rate table, q(s,dp)** parameter does not
contain a corresponding column of 0's, the block inserts them to ensure the
valve does not have nonzero flow rate when the pressure drop is 0, which is
non-physical.

**Using the `Tabulated data - Mass flow rate vs. control member
position and pressure drop` Parameterization**

`Tabulated data - Mass flow rate vs. control member position and pressure
drop` — Calculate the mass flow rate directly from the control
member position and the pressure drop across the valve. The relationship between
the three variables can be nonlinear and it is given by the tabulated data in
the **Control member position vector, s**, **Pressure
drop vector, dp**, and **Mass flow rate table,
mdot(s,dp)** block parameters:

m˙Tab=ρAvgρRefm˙(ΔS,Δp),

where m˙ is the tabulated form of the mass flow rate, a function of the
control member position, *h*, and of the pressure drop across
the orifice, *Δp*. The mass flow rate is adjusted for
temperature and pressure by the ratio *ρAvg*/*ρRef*, where *ρAvg* is the
average fluid density in the orifice and
*ρref* is the reference density for
the values of the **Reference inflow temperature** and
**Reference inflow pressure** parameters.

### Pressure Loss

*Pressure loss* describes the reduction of pressure in the valve due to
a decrease in area. The block calculates the pressure loss term,
*PR*loss as:

PRloss=1−(AorificeAport)2(1−Cd2)−CdAorificeAport1−(AorificeAport)2(1−Cd2)+CdAorificeAport.

*Pressure recovery* describes the positive pressure change in the valve
due to an increase in area. If you do not want to capture this increase in pressure,
clear the **Pressure recovery** check box. In this case,
*PR*loss is 1.

### Critical Pressure

The critical pressure difference, *Δp*crit, is the
pressure differential associated with the **Critical Reynolds
number** parameter, *Re*crit,
which is the point of transition between laminar and turbulent flow in the
fluid:

Δpcrit=πρ¯8Aorifice(νRecritCd)2.

### Energy Balance

The block treats the orifice as an adiabatic component. No heat exchange can occur between
the fluid and the wall that surrounds it. No work is done on or by the fluid as it
traverses from inlet to outlet. With these assumptions, energy can flow by advection
only, through ports **A** and **B**. By the principle of conservation of energy, the sum of the port
energy flows must always equal zero:

ϕA+ϕB=0,

where *ϕ* is defined as the energy flow rate
*into* the orifice through one of the ports (**A** or **B**).

### Faults

When the **Orifice type** parameter is
`Variable`, the block can model faults.

To model a fault, in the **Faults** section,
click the **Add fault** hyperlink next to the fault that you want to model. Use
the fault parameters to specify the fault properties. For more information about fault modeling,
see Introduction to Simscape Faults.

The **Opening area when faulted** parameter has three fault options:

- `Closed` — The orifice freezes at its
  smallest value, depending on the **Orifice
  parameterization**:

  - When **Orifice parameterization** is set
    to `Linear - Area vs. control member
    position`, the orifice freezes at the
    **Leakage area**.
  - When **Orifice parameterization** is set
    to `Tabulated data - Area vs. control member
    position`, the orifice freezes at the first
    element of the **Orifice area
    vector**.
  - When **Orifice parameterization** is set
    to `Tabulated data - Volumetric flow rate vs.
    control member position and pressure drop`,
    the orifice freezes at the first row of the
    **Volumetric flow rate table,
    q(s,dp)**.
  - When **Orifice parameterization** is set
    to `Tabulated data - Mass flow rate vs. control
    member position and pressure drop`, the
    orifice freezes at the first row of the **Mass flow
    rate table, mdot(s,dp)**.
- `Open` — The orifice freezes at its
  largest value, depending on the **Orifice
  parameterization**:

  - When **Orifice parameterization** is set
    to `Linear - Area vs. control member
    position`, the orifice freezes at the
    **Maximum orifice area**.
  - When **Orifice parameterization** is set
    to `Tabulated data - Area vs. control member
    position`, the orifice freezes at the last
    element of the **Orifice area
    vector**.
  - When **Orifice parameterization** is set
    to `Tabulated data - Volumetric flow rate vs.
    control member position and pressure drop`,
    the orifice freezes at the last row of the
    **Volumetric flow rate table,
    q(s,dp)**.
  - When **Orifice parameterization** is set
    to `Tabulated data - Mass flow rate vs. control
    member position and pressure drop`, the
    orifice freezes at the last row of the **Mass flow
    rate table, mdot(s,dp)**.
- `Maintain at last value` — The orifice
  seizes at the open area or volumetric flow rate when the trigger occurs.
