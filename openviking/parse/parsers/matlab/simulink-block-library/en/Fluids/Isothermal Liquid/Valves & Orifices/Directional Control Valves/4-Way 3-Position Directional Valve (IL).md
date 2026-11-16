---
type: simulink-block
title: '4-Way 3-Position Directional Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: '4way3positiondirectionalvalveil'
documentation_source_path: 'ref/4way3positiondirectionalvalveil.html'
language: en
---

# 4-Way 3-Position Directional Valve (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Liquid entry or exit port to the valve.

### **B** — Liquid port isothermal liquid

Liquid entry or exit port to the valve.

### **P** — Liquid port isothermal liquid

Liquid entry or exit port to the valve.

### **T** — Liquid port isothermal liquid

Liquid entry or exit port to the valve.
### Input

### **S** — Spool displacement, m physical signal

Spool displacement, in m, specified as a physical signal.

## Parameters

### Valve Configuration

### **Positive spool position open connections** — Flow paths open when the spool is in a positive position `P-A, B-T` (default) | `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-B`

Flow paths open when the spool is in a positive position. This
parameter sets the valve configuration and defines the direction of
spool movement according to the signal received at port
**S**. The settings for this parameter can be
checked against the definitions for the other orifices for consistency
when the **Consistency check for neutral spool position open
connections** is set to `Warning`
or `Error`.

### **Neutral spool position open connections** — Flow paths open when the spool is in the neutral position `All closed` (default) | `P-A, P-B, A-T, B-T` | `A-T, B-T` | `P-A, A-T` | `P-A, B-T` | `P-A, P-B` | `P-B, A-T` | `P-B, B-T` | `A-T` | `B-T` | `P-A` | `P-B` | `P-T` | `P-A, A-T, P-T` | `P-A, P-B, A-B` | `P-B, B-T, P-T` | `P-A, P-B, A-T, B-T, P-T`

Flow paths open when the spool is in the neutral position. This
parameter sets the valve configuration and defines the direction of
spool movement according to the signal received at port
**S**. The settings for this parameter can be
checked against the definitions for the other orifices for consistency
when the **Consistency check for neutral spool position open
connections** is set to `Warning`
or `Error`.

### **Negative spool position open connections** — Flow paths open when the spool moves in the negative direction `P-A, B-T` (default) | `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-B`

Flow paths open when the spool moves in the negative direction. This
parameter sets the valve configuration and defines the direction of
spool movement according to the signal received at port
**S**. The settings for this parameter can be
checked against the definitions for the other orifices for consistency
when the **Consistency check for neutral spool position open
connections** is set to `Warning`
or `Error`.

### **Consistency check for neutral spool position open connections** — Whether to check if the orifice settings are consistent with the specified spool position for maximum orifice opening `Warning` (default) | `Error` | `None`

Whether to check if the neutral spool position open settings on the
**Valve Configuration** tab are consistent with the
specified spool position at the maximum orifice area. For each enabled
orifice, the actual offset at the spool neutral position should be
commensurate with the specified spool offset for each individual
orifice.

### Model Parameterization

### **Area characteristics** — Flow equations for orifices `Identical for all flow paths` (default) | `Different for each flow path`

Applies uniform or individual flow equations for the valve orifice
area. `Identical for all flow paths` uses the
same orifice and spool geometries, flow rates, pressure, and area
vectors for all valve orifices. When using `Different for
each flow path`, these parameters are specified
individually for each orifice. In both cases, orifices
**A**, **B**,
**P**, and **T** have the same
cross-sectional areas, discharge coefficients, and Reynolds numbers in
the `Linear - Area vs. spool travel` and
`Tabulated data - Area vs. spool travel`
parameterizations. The same **Orifice
parameterization** is applied to all flow paths.

### **Orifice parameterization** — Method of calculating opening area `Linear area vs. spool travel` (default) | `Tabulated data - Area vs. spool travel` | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`

Method of calculating the valve opening area. In the tabulated data
parameterizations, you can provide your own valve area and spool travel
data for nonlinear valve opening profiles, or you can provide data in
terms of volumetric flow rate, spool travel, and pressure drop over the
flow path.

### **Spool travel between closed and open orifice** — Maximum spool stroke `0.005 m` (default) | positive scalar

Maximum distance of spool travel.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Linear - Area vs.
spool travel`.

### **Maximum orifice area** — Maximum orifice opening area `1e-4 m^2` (default) | positive scalar

Largest open area of each orifice during the operation of the
valve.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Linear - Area vs.
spool travel`.

### **Leakage area** — Open area when an orifice is fully closed `1e-9 m^2` (default) | positive scalar

Open area when an orifice is fully closed. Any area smaller than this
value is maintained at the specified leakage area. This parameter
contributes to numerical stability by maintaining continuity in the
flow.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Linear - Area vs.
spool travel`.

### **Spool travel vector** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances for the tabular parameterization of
valve area. The vector elements must correspond one-to-one with the
elements in the **Orifice area vector** parameter. The
values are listed in ascending order and the first element must be 0.
Linear interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Tabulated data -
Area vs. spool travel`.

### **Orifice area vector** — Vector of valve opening areas `[1e-09, 1e-05, 4e-05, 6e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of opening areas for the tabular parameterization of valve
opening area. The vector elements must correspond one-to-one with the
elements in the **Spool travel vector** parameter. The
elements are listed in ascending order and must be greater than
0.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Tabulated data -
Area vs. spool travel`.

### **Spool travel vector, ds** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances for the tabular parameterization of volumetric flow
rate. The spool travel vector forms an independent axis with the
**Pressure drop vector, dp** parameter for the 2-D
dependent **Volumetric flow rate table, q(ds,dp)**
parameter. The values are listed in ascending order and the first
element must be 0. Linear interpolation is employed between table data
points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`.

### **Pressure drop vector, dp** — Vector of valve pressure drop values `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure drop values for the tabular parameterization of volumetric flow rate.
The pressure drop vector forms an independent axis with the
**Spool travel vector, ds** parameter for the 2-D
dependent **Volumetric flow rate table, q(ds,dp)**
parameter. The values are listed in ascending order and must be greater
than 0. Linear interpolation is employed between table data
points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`.

### **Volumetric flow rate table, q(ds,dp)** — Array of volumetric flow rates `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; .00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of volumetric flow
rates based on independent values of pressure drop and spool travel
distance. *M* and *N* are the sizes of
the correlated vectors:

- *M* is the number of vector elements in
  the **Spool travel vector, ds**
  parameter.
- *N* is the number of vector elements in
  the **Pressure drop vector, dp**
  parameter.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`.

### **Constant orifice area** — Orifice area for identical flow paths `1e-4 m^2` (default) | positive scalar

Orifice area when the positive, neutral, and negative spool positions
feature the same orifice.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to either:

- `Linear - area vs. spool
  travel`.
- `Tabulated data - Area vs. spool
  travel`

The same orifice must be selected in all three of the
**Valve Configuration** parameters:

- **Positive spool position open
  connections**
- **Neutral spool position open
  connections**
- **Negative spool position open
  connections**

### **Constant orifice pressure drop vector** — Vector of pressure differential values for identical flow paths `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure differential values over the valve when the
positive, neutral, and negative spool positions feature the same
orifice. The vector elements correspond one-to-one with the elements in
the **Constant orifice volumetric flow rate vector**
parameter. The values are listed in ascending order. Linear
interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`.

The same orifice must be selected in all three of the
**Valve Configuration** parameters:

- **Positive spool position open
  connections**
- **Neutral spool position open
  connections**
- **Negative spool position open
  connections**

### **Constant orifice volumetric flow rate vector** — Vector of volumetric flow rate values for identical flow paths `[-.0009, .0016, .002, .0024] m^3/s` (default) | 1-by-*n* vector

Vector of volumetric flow rate values for a constant orifice when the
positive, neutral, and negative spool positions feature the same
orifice. The vector elements correspond one-to-one with the elements in
the **Constant orifice pressure drop vector**
parameter. The values are listed in ascending order. Linear
interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`.

The same orifice must be selected in all three of the
**Valve Configuration** parameters:

- **Positive spool position open
  connections**
- **Neutral spool position open
  connections**
- **Negative spool position open
  connections**

### **Cross-sectional area at ports P, T, A and B** — Area at conserving ports `inf m^2` (default) | positive scalar

Maximum cross-sectional areas at the entry and exit ports
**P**, **T**,
**A**, and **B**, which are used
in the pressure-flow rate equation that determines the mass flow rate
through the valve.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to either:

- `Linear - area vs. spool
  travel`
- `Tabulated data - Area vs. spool
  travel`

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor that accounts for discharge losses in theoretical
flows.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to either:

- `Linear - Area vs. spool
  travel`
- `Tabulated data - Area vs. spool
  travel`

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the orifice.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to:

- `Linear - area vs. spool
  travel`
- `Tabulated data - Area vs. spool
  travel`

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range of [0,1]

Continuous smoothing factor that introduces a layer of gradual change
based to the flow response when the valve is in near-open and
near-closed positions. To increase the stability of your simulation in
these regimes, set this parameter to a nonzero value less than
one.

#### Dependencies

To enable this parameter, set **Orifice parameterization** to
`Linear - area vs. spool
travel`.

### **Pressure recovery** — Whether to account for pressure increase in area expansions `off` (default) | `on`

Whether to account for pressure increase when fluid flows from a
region of smaller cross-sectional area to a region of larger
cross-sectional area.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to:

- `Linear - area vs. spool
  travel`
- `Tabulated data - Area vs. spool
  travel`

### P-A Orifice

### **Spool position at maximum P-A orifice area** — Spool offset for fully open P-A orifice `7.5e-3 m` (default) | positive scalar

Spool offset from the neutral position for a fully open P-A orifice.
The **Consistency check for neutral spool position open
connections** parameter will notify you if the values set
for this spool position are inconsistent or unphysical according to
other orifice spool positions. To visualize the defined offsets, see
Visualize Orifice Openings.

#### Dependencies

To enable this parameter, set one of the following parameters:

**Positive spool position open connections** to:

- `P-A, B-T`
- `P-A, P-B`
- `P-A`

**Neutral spool position open
connections** to:

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`

**Negative spool position open
connections** to:

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`

**Note:**

This parameter is enabled only when the P-A orifice
settings do not appear in all three spool position
parameters: **Positive spool position
open connections**, **Neutral spool
position open connections**, and **Negative spool position open
connections**.

### **P-A spool travel between closed and open orifice** — Maximum spool stroke `0.005 m` (default) | positive scalar

Maximum distance of spool travel. This value provides an upper limit
to calculations so that simulations do not return unphysical
values.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Linear - Area vs. spool
   travel`.
3. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A maximum orifice area** — Maximum orifice opening area `1e-4 m^2` (default) | positive scalar

Largest open area of the P-A orifice during the operation of the
valve.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Linear - Area vs. spool
   travel`.
3. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A orifice spool travel vector** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances for the tabular parameterization of
valve area. The vector elements must correspond one-to-one with the
elements in the **P-A orifice area vector** parameter.
The values are listed in ascending order and the first element must be
0. Linear interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Area vs. spool
   travel`.
3. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A orifice area vector** — Vector of valve opening areas `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of opening areas for the tabular parameterization of valve
opening area. The vector elements must correspond one-to-one with the
elements in the **P-A spool travel vector** parameter.
The elements are listed in ascending order and must be greater than
0.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Area vs. spool
   travel`.
3. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A orifice spool travel vector, ds** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances for the tabular parameterization of
volumetric flow rates. The spool travel vector forms an independent axis
with the **P-A orifice pressure drop vector, dp**
parameter for the 2-D dependent **P-A orifice volumetric flow
rate table, q(ds,dp)** parameter. The values are listed in
ascending order and the first element must be 0. Linear interpolation is
employed between table data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A orifice pressure drop vector, dp** — Vector of pressure drop values `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure drop values for the tabular parameterization of volumetric flow rate.
The pressure drop vector forms an independent axis with the
**P-A orifice spool travel vector, ds** parameter
for the 2-D dependent **P-A orifice volumetric flow rate table,
q(ds,dp)** parameter. The values are listed in ascending
order and must be greater than 0. Linear interpolation is employed
between table data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A orifice volumetric flow rate table, q(ds,dp)** — Array of volumetric flow rate values `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of volumetric flow
rates based on independent values of pressure drop and spool travel
distance. *M* and *N* are the sizes of
the correlated vectors:

- *M* is the number of vector elements in
  the **P-A orifice spool travel vector,
  ds** parameter.
- *N* is the number of vector elements in
  the **P-A orifice pressure drop vector,
  dp** parameter.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A constant orifice area** — Cross-sectional area for a constant orifice `1e-4 m^2` (default) | positive scalar

Orifice area when the positive, neutral, and negative spool positions
feature the same orifice.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to either:

   - `Linear - area vs. spool
     travel`
   - `Tabulated data - Area vs. spool
     travel`
3. One of the following settings in each
   parameter:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A constant orifice pressure drop vector** — Vector of pressure differential values for a constant orifice `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure differential values over the valve when the
positive, neutral, and negative spool positions feature the same
orifice. The vector elements correspond one-to-one with the elements in
the **P-A constant orifice volumetric flow rate
vector** parameter. The values are listed in ascending
order. Linear interpolation is employed between table data
points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. One of the following settings in each
   parameter:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A constant orifice volumetric flow rate vector** — Vector of volumetric flow rates for a constant orifice `[-.0009, .0016, .002, .0024] m^3/s` (default) | 1-by-*n* vector

Vector of pressure differential values over the valve when the
positive, neutral, and negative spool positions feature the same
orifice. The vector elements correspond one-to-one with the elements in
the **P-A constant orifice pressure drop vector**
parameter. The values are listed in ascending order. Linear
interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. One of the following settings in each
   parameter:

   **Positive spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### P-B Orifice

### **Spool position at maximum P-B orifice area** — Spool offset from the neutral position for a fully open P-B orifice `7.5e-3 m` (default) | positive scalar

Spool offset from the neutral position for a fully open P-B orifice.
The **Consistency check for neutral spool position open
connections** parameter will notify you if the values set
for this spool position are inconsistent or unphysical according to
other orifice spool positions. To visualize the defined offsets, see
Visualize Orifice Openings.

#### Dependencies

To enable this parameter, set one of the following parameters:

**Positive spool position open connections** to:

- `P-B, A-T`
- `P-A, P-B`
- `P-B`

**Neutral spool position open
connections** to:

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`

**Negative spool position open
connections** to:

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`

**Note:**

This parameter is enabled only when the P-B orifice
settings do not appear in all three spool position
parameters: **Positive spool position
open connections**, **Neutral spool
position open connections**, and **Negative spool position open
connections**.

### **P-B spool travel between closed and open orifice** — Maximum spool stroke `0.005 m` (default) | positive scalar

Maximum distance of spool travel. This value provides an upper limit
to calculations so that simulations do not return unphysical
values.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Linear - Area vs. spool
   travel`.
3. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   or set **Neutral spool position
   open connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   or set **Negative spool position
   open connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B maximum orifice area** — Maximum orifice opening area `1e-4 m^2` (default) | positive scalar

Largest open area of the P-B orifice during the operation of the
valve.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Linear - Area vs. spool
   travel`.
3. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **Negative spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B orifice spool travel vector** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances for the tabular parameterization of
valve area. The vector elements must correspond one-to-one with the
elements in the **P-B orifice area vector** parameter.
The values are listed in ascending order and the first element must be
0. Linear interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Area vs. spool
   travel`.
3. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **Negative spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B orifice area vector** — Vector of valve opening areas `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of opening areas for the tabular parameterization of valve
opening area. The vector elements must correspond one-to-one with the
elements in the **P-B spool travel vector** parameter.
The elements are listed in ascending order and must be greater than
0.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Area vs. spool
   travel`.
3. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **Negative spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B orifice spool travel vector, ds** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances for the tabular parameterization of
volumetric flow rates. The spool travel vector forms an independent axis
with the **P-T orifice pressure drop vector, dp**
parameter for the 2-D dependent **P-T orifice volumetric flow
rate table, q(ds,dp)** parameter. The values are listed in
ascending order and the first element must be 0. Linear interpolation is
employed between table data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`.

   **Negative spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B orifice pressure drop vector, dp** — Vector of pressure differential values `[-.1, .3, .5, .7] MPa` (default) | 1-by*n* vector

Vector of pressure drop values for tabular parameterization of volumetric flow rate. The
pressure drop vector forms an independent axis with the **P-B
orifice spool travel vector, ds** parameter for the 2-D
dependent **P-B orifice volumetric flow rate table,
q(ds,dp)** parameter. The values are listed in ascending
order and must be greater than 0. Linear interpolation is employed
between table data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **Negative spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B orifice volumetric flow rate table, q(ds,dp)** — Array of volumetric flow rate values `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of volumetric flow
rates based on independent values of pressure drop and spool travel
distance. *M* and *N* are the sizes of
the correlated vectors:

- *M* is the number of vector elements in
  the **P-B orifice spool travel vector,
  ds** parameter.
- *N* is the number of vector elements in
  the **P-B orifice pressure drop vector,
  dp** parameter.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. One of the following parameters:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **Negative spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B constant orifice area** — Cross-sectional area for a constant orifice `1e-4 m^2` (default) | positive scalar

Orifice area when the positive, neutral, and negative spool positions
feature the same orifice.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to either:

   - `Linear - area vs. spool
     travel`
   - `Tabulated data - Area vs. spool
     travel`
3. One of the following settings in each
   parameter:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **Negative spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B constant orifice pressure drop vector** — Vector of pressure differential values for a constant orifice `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure differential values over the valve when the
positive, neutral, and negative spool positions feature the same
orifice. The vector elements correspond one-to-one with the elements in
the **P-B constant orifice volumetric flow rate
vector** parameter. The values are listed in ascending
order. Linear interpolation is employed between table data
points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. One of the following settings in each
   parameter:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **Negative spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B constant orifice volumetric flow rate vector** — Vector of volumetric flow rate values for a constant orifice `[-.0009, .0016, .002, .0024] m^3/s` (default) | 1-by-*n* vector

Vector of volumetric flow rate values over the valve when the
positive, neutral, and negative spool positions feature the same
orifice. The vector elements correspond one-to-one with the elements in
the **P-B constant orifice pressure drop vector**
parameter. The values are listed in ascending order. Linear
interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. One of the following settings in each
   parameter:

   **Positive spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **Negative spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### A-T Orifice

### **Spool position at maximum A-T orifice area** — Spool offset from the neutral position for a fully open A-T orifice `7.5e-3 m` (default) | positive scalar

Spool offset from the neutral position for a fully open A-T orifice.
The **Consistency check for neutral spool position open
connections** parameter will notify you if the values set
for this spool position are inconsistent or unphysical according to
other orifice spool positions. To visualize the defined offsets, see
Visualize Orifice Openings.

#### Dependencies

To enable this parameter, set one of the following parameters:

- **Positive spool position open
  connections** to `P-B,
  A-T`.
- **Neutral spool position open
  connections** to:

  - `P-A, P-B, A-T,
    B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
- **Negative spool position open
  connections** to `P-B,
  A-T`.

**Note:**

This parameter is enabled only when the A-T orifice
settings do not appear in all three spool position
parameters: **Positive spool position
open connections**, **Neutral spool
position open connections**, and **Negative spool position open
connections**.

### **A-T spool travel between closed and open orifice** — Maximum spool stroke `0.005 m` (default) | positive scalar

Maximum distance of spool travel. This value provides an upper limit
to calculations so that simulations do not return unphysical
values.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Linear - Area vs. spool
   travel`.
3. One of the following parameters:

   **Positive spool position open connections** to `P-B,
   A-T`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **Negative spool position open connections** to `P-B,
   A-T`.

### **A-T maximum orifice area** — Maximum orifice opening area `1e-4 m^2` (default) | positive scalar

Largest open area of the A-T orifice during the operation of the
valve.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Linear - Area vs. spool
   travel`.
3. One of the following parameters:

   **Positive spool position open connections** to `P-B,
   A-T`

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **Negative spool position open connections** to `P-B,
   A-T`.

### **A-T orifice spool travel vector** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances for the tabular parameterization of
valve area. The vector elements must correspond one-to-one with the
elements in the **A-T orifice area vector** parameter.
The values are listed in ascending order and the first element must be
0. Linear interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Area vs. spool
   travel`.
3. One of the following parameters:

   **Positive spool position open connections** to `P-B,
   A-T`.

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **Negative spool position open connections** to `P-B,
   A-T`.

### **A-T orifice area vector** — Vector of valve opening areas `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of opening areas for the tabular parameterization of valve
opening area. The vector elements must correspond one-to-one with the
elements in the **A-T spool travel vector** parameter.
The elements are listed in ascending order and must be greater than
0.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Area vs. spool
   travel`.
3. One of the following parameters:

   **Positive spool position open connections** to `P-B,
   A-T`.

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **Negative spool position open connections** to `P-B,
   A-T`.

### **A-T orifice spool travel vector, ds** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances for the tabular parameterization of
volumetric flow rates. The spool travel vector forms an independent axis
with the **A-T orifice pressure drop vector, dp**
parameter for the 2-D dependent **A-T orifice volumetric flow
rate table, q(ds,dp)** parameter. The values are listed in
ascending order and the first element must be 0. Linear interpolation is
employed between table data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. One of the following parameters:

   **Positive spool position open connections** to `P-B,
   A-T`.

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **Negative spool position open connections** to `P-B,
   A-T`.

### **A-T orifice pressure drop vector, dp** — Vector of pressure differential values `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure drop values for tabular parameterization of volumetric flow rate. The
pressure drop vector forms an independent axis with the **A-T
orifice spool travel vector, ds** parameter for the 2-D
dependent **A-T orifice volumetric flow rate table,
q(ds,dp)** parameter. The values are listed in ascending
order and must be greater than 0. Linear interpolation is employed
between table data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. One of the following parameters:

   **Positive spool position open connections** to `P-B,
   A-T`.

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **Negative spool position open connections** to `P-B,
   A-T`.

### **A-T orifice volumetric flow rate table, q(ds,dp)** — Array of volumetric flow rate values `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of volumetric flow
rates based on independent values of pressure drop and spool travel
distance. *M* and *N* are the sizes of
the correlated vectors:

- *M* is the number of vector elements in
  the **A-T orifice spool travel vector,
  ds** parameter.
- *N* is the number of vector elements in
  the **A-T orifice pressure drop vector,
  dp** parameter.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. One of the following parameters:

   **Positive spool position open connections** to `P-B,
   A-T`.

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **Negative spool position open connections** to `P-B,
   A-T`.

### **A-T constant orifice area** — Cross-sectional area for a constant orifice `1e-4 m^2` (default) | positive scalar

Orifice area when the positive, neutral, and negative spool positions
feature the same orifice.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to either:

   - `Linear - area vs. spool
     travel`
   - `Tabulated data - Area vs. spool
     travel`
3. One of the following settings in each
   parameter:

   **Positive spool position open connections** to `P-B,
   A-T`.

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **Negative spool position open connections** to `P-B,
   A-T`.

### **A-T constant orifice pressure drop vector** — Vector or pressure differential values for a constant orifice `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure differential values over the valve when the
positive, neutral, and negative spool positions feature the same
orifice. The vector elements correspond one-to-one with the elements in
the **A-T constant orifice volumetric flow rate
vector** parameter. The values are listed in ascending
order. Linear interpolation is employed between table data
points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. One of the following settings in each
   parameter:

   **Positive spool position open
   connections** to `P-B,
   A-T`.

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **Negative spool position open
   connections** to `P-B,
   A-T`.

### **A-T constant orifice volumetric flow rate vector** — Vector of volumetric flow rate values for a constant orifice `[-.0009, .0016, .002, .0024] m^3/s` (default) | 1-by-*n* vector

Vector of volumetric flow rate values when the positive, neutral, and
negative spool positions feature the same orifice. The vector elements
correspond one-to-one with the elements in the **Constant
orifice volumetric flow rate vector** parameter. The values
are listed in ascending order. Linear interpolation is employed between
table data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. One of the following settings in each
   parameter:

   **Positive spool position open
   connections** to `P-B,
   A-T`.

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **Negative spool position open
   connections** to `P-B,
   A-T`.

### B-T Orifice

### **Spool position at maximum B-T orifice area** — Spool offset from the neutral position for a fully open B-T orifice `7.5e-3 m` (default) | positive scalar

Spool offset from the neutral position for a fully open B-T orifice.
The **Consistency check for neutral spool position open
connections** parameter will notify you if the values set
for this spool position are inconsistent or unphysical according to
other orifice spool positions. To visualize the defined offsets, see
Visualize Orifice Openings.

#### Dependencies

To enable this parameter, set one of the following parameters:

- **Positive spool position open
  connections** to `P-A,
  B-T`.
- **Neutral spool position open
  connections** to:

  - `P-A, P-B, A-T,
    B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
- **Negative spool position open
  connections** to `P-A,
  B-T`.

**Note:**

This parameter is enabled only when the B-T orifice
settings do not appear in all three spool position
parameters: **Positive spool position
open connections**, **Neutral spool
position open connections**, and **Negative spool position open
connections**.

### **B-T spool travel between closed and open orifice** — Maximum spool stroke `0.005 m` (default) | positive scalar

Maximum distance of spool travel. This value provides an upper limit
to calculations so that simulations do not return unphysical
values.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Linear - Area vs. spool
   travel`.
3. One of the following parameters:

   **Positive spool position open connections** to `P-A,
   B-T`.

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   **Negative spool position open connections** to `P-A,
   B-T`.

### **B-T maximum orifice area** — Maximum orifice opening area `1e-4 m^2` (default) | positive scalar

Largest open area of the B-T orifice during the operation of the
valve.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Linear - Area vs. spool
   travel`.
3. One of the following parameters:

   **Positive spool position open connections** to `P-A,
   B-T`.

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   **Negative spool position open connections** to `P-A,
   B-T`.

### **B-T orifice spool travel vector** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances for the tabular parameterization of
valve area. The vector elements must correspond one-to-one with the
elements in the **B-T orifice area vector** parameter.
The values are listed in ascending order and the first element must be
0. Linear interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Area vs. spool
   travel`.
3. One of the following parameters:

   **Positive spool position open connections** to `P-A,
   B-T`.

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   **Negative spool position open connections** to `P-A,
   B-T`.

### **B-T orifice area vector** — Vector of valve opening areas `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of opening areas for the tabular parameterization of valve
opening area. The vector elements must correspond one-to-one with the
elements in the **B-T orifice spool travel vector**
parameter. The elements are listed in ascending order and must be
greater than 0.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Area vs. spool
   travel`.
3. One of the following parameters:

   **Positive spool position open connections** to `P-A,
   B-T`.

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   **Negative spool position open connections** to `P-A,
   B-T`.

### **B-T orifice spool travel vector, ds** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of control member travel distances for the tabular
parameterization of volumetric flow rates. The spool travel vector forms
an independent axis with the **B-T orifice pressure drop vector,
dp** parameter for the 2-D dependent **B-T orifice
volumetric flow rate table, q(ds,dp)** parameter. The
values are listed in ascending order and the first element must be 0.
Linear interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. One of the following parameters:

   **Positive spool position open connections** to `P-A,
   B-T`.

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   **Negative spool position open connections** to `P-A,
   B-T`.

### **B-T orifice pressure drop vector, dp** — Vector of pressure differential values `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure drop values for tabular parameterization of volumetric flow rate. The
pressure drop vector forms an independent axis with the **B-T
orifice spool travel vector, ds** parameter for the 2-D
dependent **B-T orifice volumetric flow rate table,
q(ds,dp)** parameter. The values are listed in ascending
order and must be greater than 0. Linear interpolation is employed
between table data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. One of the following parameters:

   **Positive spool position open connections** to `P-A,
   B-T`.

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   **Negative spool position open connections** to `P-A,
   B-T`.

### **B-T orifice volumetric flow rate table, q(ds,dp)** — Array of volumetric flow rate values `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of volumetric flow
rates based on independent values of pressure drop and spool travel
distance. *M* and *N* are the sizes of
the correlated vectors:

- *M* is the number of vector elements in
  the **B-T orifice spool travel vector,
  ds** parameter.
- *N* is the number of vector elements in
  the **B-T orifice pressure drop vector,
  dp** parameter.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. One of the following parameters:

   **Positive spool position open connections** to `P-A,
   B-T`.

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   **Negative spool position open connections** to `P-A,
   B-T`.

### **B-T constant orifice area** — Cross-sectional orifice area for constant orifices `1e-4 m^2` (default) | positive scalar

Orifice area when the positive, neutral, and negative spool positions
feature the same orifice.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   either:

   - `Linear - area vs. spool
     travel`
   - `Tabulated data - Area vs. spool
     travel`
3. One of the settings in each parameter:

   **Positive spool position open connections** to `P-A,
   B-T`.

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   **Negative spool position open connections** to `P-A,
   B-T`.

### **B-T constant orifice pressure drop vector** — Vector of pressure differential values for a constant orifice `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure differential values over the valve when the
positive, neutral, and negative spool positions feature the same
orifice. The vector elements correspond one-to-one with the elements in
the **B-T constant orifice volumetric flow rate
vector** parameter. The values are listed in ascending
order. Linear interpolation is employed between table data
points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. One of the settings in each parameter:

   **Positive spool position open
   connections** to `P-A,
   B-T`.

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   **Negative spool position open
   connections** to `P-A,
   B-T`.

### **B-T constant orifice volumetric flow rate vector** — Vector of volumetric flow rates for a constant orifice `[-.0009, .0016, .002, .0024] m^3/s` (default) | 1-by-*n* vector

Vector of pressure differential values over the valve when the
positive, neutral, and negative spool positions feature the same
orifice. The vector elements correspond one-to-one with the elements in
the **B-T constant orifice pressure drop vector**
parameter. The values are listed in ascending order. Linear
interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. One of the settings in each parameter:

   **Positive spool position open
   connections** to `P-A,
   B-T`.

   **Neutral spool position open
   connections** to:

   - `P-A, P-B, A-T,
     B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   **Negative spool position open
   connections** to `P-A,
   B-T`.

### P-T Orifice

### **Spool position at maximum P-T orifice area** — Spool offset from the neutral position for a fully open P-T orifice `0 m` (default) | positive scalar

Spool offset from the neutral position for a fully open P-T orifice.
The **Consistency check for neutral spool position open
connections** parameter will notify you if the values set
for this spool position are inconsistent or unphysical according to
other orifice spool positions. To visualize the defined offsets, see
Visualize Orifice Openings.

#### Dependencies

To enable this parameter, set **Neutral spool position open
connections** to

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

.

### **P-T spool travel between closed and open orifice** — Maximum spool stroke `0.005 m` (default) | positive scalar

Maximum distance of spool travel. This value provides an upper limit
to calculations so that simulations do not return unphysical
values.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Linear - Area vs. spool
   travel`.
3. **Neutral spool position open
   connections** to:

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T maximum orifice area** — Maximum orifice opening area `1e-4 m^2` (default) | positive scalar

Largest open area of the P-T orifice during the operation of the
valve.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Linear - Area vs. spool
   travel`.
3. **Neutral spool position open
   connections** to:

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice spool travel vector** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of control member travel distances for the tabular
parameterization of valve area. The vector elements must correspond
one-to-one with the elements in the **P-T orifice area
vector** parameter. The values are listed in ascending
order and the first element must be 0. Linear interpolation is employed
between table data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Area vs. spool
   travel`.
3. **Neutral spool position open
   connections** to:

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice spool travel vector, ds** — Vector of spool opening distances relative to fully-closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of control member travel distances for the tabular
parameterization of volumetric flow rate. The spool travel vector forms
an independent axis with the **P-T orifice pressure drop vector,
dp** parameter for the 2-D dependent **P-T orifice
volumetric flow rate table, q(ds,dp)** parameter. The
values are listed in ascending order and the first element must be 0.
Linear interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Area vs. spool
   travel`.
3. **Neutral spool position open
   connections** to:

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice pressure drop vector, dp** — Vector of pressure differential values `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure drop values for tabular parameterization of volumetric flow rate. The
pressure drop vector forms an independent axis with the **P-T
orifice spool travel vector, ds** parameter for the 2-D
dependent **P-T orifice volumetric flow rate table,
q(ds,dp)** parameter. The values are listed in ascending
order and must be greater than 0. Linear interpolation is employed
between table data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Area vs. spool
   travel`.
3. **Neutral spool position open
   connections** to:

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice volumetric flow rate table, q(ds,dp)** — Array of volumetric flow rates `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of volumetric flow
rates based on independent values of pressure drop and spool travel
distance. *M* and *N* are the sizes of
the correlated vectors:

- *M* is the number of vector elements in
  the **P-T orifice spool travel vector,
  ds** parameter.
- *N* is the number of vector elements in
  the **P-T orifice pressure drop vector,
  dp** parameter.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Area vs. spool
   travel`.
3. **Neutral spool position open
   connections** to:

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### Faults

### **4-Way 3-Position Directional Valve Area fault** — Option to model valve area fault `Add fault`

Option to model a valve area fault in the block. To add a fault, click the **Add
fault** hyperlink. When a fault occurs, the valve area
normally set by the opening parameterization is set based on the value
specified in the **Spool position when faulted**
parameter.

### **Spool position when faulted** — Faulted valve characteristics `Positive` (default) | `Neutral` | `Negative` | `Maintain last value`

Faulted valve spool position. You can choose for the valve to seize when the spool is in
the positive position, negative position, or at the position when the
fault triggers.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink.

## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Directional Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

### R2024a: Model faults with the Simscape faults interface

The 4-Way 3-Position Directional Valve (IL) block now supports the Simscape™ faults interface. To learn more, see Introduction to Simscape Faults.

## Description

4-way, 3-position directional valve in an isothermal liquid system

The 4-Way 3-Position Directional Valve (IL) block models a valve with four openings in
an isothermal liquid network, typically between an actuator, pump, and tank. The valve
operation is controlled by a single spool displaced according to the signal at port
**S**. You can set the baseline configuration of your valve by
specifying the orifices that are open when the spool is in the neutral position
(centered at 0 m) in the **Neutral spool position open connections**
parameter, when the spool moves in the positive direction in the **Positive
spool position open connections** parameter, and when the spool moves in
the negative direction in the **Negative spool position open
connections**.

You can set the model for valve opening in the **Orifice
parameterization** parameter as a linear relationship or function of
user-provided data, which can be applied to one or all flow paths in the valve.

**Example Valve Setup**

In this example configuration, **Neutral spool position open
connections** is set to `All closed`. When the
spool is in the neutral position, all orifices are closed to flow:

In this configuration, **Negative spool position open connections** is set
to `P-A, B-T`. When the signal at port **S**
moves the spool to a negative position, the paths between ports **P**
and **A** and between ports **B** and
**T** are open to flow. The paths between ports
**P** and **B** and ports **A**
and **T** are closed to flow:

In this configuration, **Positive spool position open connections** is set
to `P-B, A-T`. When the signal at port **S**
moves the spool to a positive position, the paths between ports **P**
and **B** and between ports **A** and
**T** are open to flow and the paths between ports
**P** and **A** and between ports
**B** and **T** are closed:

Schematically, this configuration is shown as:

The left-hand side corresponds to the positive position and the
right-hand side corresponds to the negative position.

### Spool Displacement and Valve Configuration

The *spool stroke* is the amount of spool travel an orifice
takes to fully open from a closed position and is defined for each orifice selected
on the **Valve Configuration** tab. The table below shows how the
stroke is calculated in accordance with the valve orifice parameterization and flow
path characteristics.

**Spool Stroke Based on Parameterization and Flow Path**

| Orifice Parameterization | Identical for All Flow Paths | Different for Each Flow Path |
| --- | --- | --- |
| Linear - Area vs. spool travel | Defined by the **Spool travel between closed and open orifice** parameter | Defined by the Spool travel between closed and open orifice parameter, for each orifice |
| Tabulated data - Area vs. spool travel | The difference between the first and last element of the **Spool travel vector** parameter | The difference between the first and last element of the spool travel vector parameter for each orifice |
| Tabulated data - Volumetric flow rate vs. spool travel and pressure drop | The difference between the first and last element of the **Spool travel vector, ds** parameter | The difference between the first and last element of the spool travel vector, ds parameter for each orifice |

The section Visualize Orifice Openings details how to
see the orientation of all valve orifices.

The direction of spool movement signaled at port **S** depends on
the spool stroke and the orifice orientation:

**Orifice Definition and Spool Travel Direction**

| Spool Position when Orifice is Open | Spool Travel, *ΔS* |
| --- | --- |
| Always closed (orifice is not selected in any spool position configuration) | N/A |
| Always open (orifice is selected in positive, neutral, and negative spool position configurations) | N/A |
| Negative | *S*orifice\_max + spool stroke – **S** |
| Negative and Neutral | *S*orifice\_max + spool stroke – **S** |
| Positive | *S*orifice\_max – spool stroke + **S** |
| Positive and Neutral | *S*orifice\_max – spool stroke + **S** |
| Neutral | |*S*orifice\_max| + spool stroke – |**S**| |
| Positive and Negative | –|*S*orifice\_max| + spool stroke – |**S**| |

Where *S*orifice\_max is the spool position at the
maximum orifice area defined for each orifice. The orifice area saturates at the
leakage area when *ΔS* is negative and saturates at the maximum
orifice area when the orifice is fully open. When the orifice is fully open,
*ΔS* is equal to the spool stroke, so *ΔS*
greater than the spool stroke does not further increase the orifice area.

The **Consistency check for neutral spool position open
connections** parameter verifies that

- Any orifice listed in **Neutral spool position open
  connections** is open when the signal at
  **S** is 0.
- Any orifice that is not listed in **Neutral spool position
  open connections** is closed when the signal at
  **S** is 0.

You can optionally choose to receive a warning or error when this
check is violated.

The possible configurations of the 4-Way 3-Position Directional Valve (IL) block are shown
below.

**4-Way 3-Position Directional Valve Configuration**

| Configuration | Parameter Values |
| --- | --- |
|  | All four orifices are closed in the neutral position. (default)  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**: `All   closed` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke - **Spool position at maximum A-T   orifice area** < –A-T spool   stroke - **Spool position at maximum B-T   orifice area** > B-T spool stroke |
|  | All four orifices are open in the neutral position.  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**: `P-A, P-B,   A-T, B-T` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** < P-A spool   stroke - **Spool position at maximum P-B   orifice area** > –P-B spool stroke - **Spool position at maximum A-T   orifice area** > –A-T spool stroke - **Spool position at maximum B-T   orifice area** < B-T spool   stroke |
|  | Orifices A-T and B-T are closed. Orifices P-A and P-B are overlapped.  - **Positive spool position open   connections**:   `P-A` - **Neutral spool position open   connections**: `All   closed` - **Negative spool position open   connections**:   `P-B`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke |
|  | Orifices A-T and B-T are open. Orifices P-A and P-B are overlapped.  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**: `A-T,   B-T` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke - **Spool position at maximum A-T   orifice area** > –A-T spool stroke - **Spool position at maximum B-T   orifice area** < B-T spool   stroke |
|  | Orifices P-A and A-T are open in the neutral position. Orifices P-B and B-T are overlapped.  - **Positive spool position open   connections**: `P-B,   A-T` - **Neutral spool position open   connections**: `P-A,   A-T` - **Negative spool position open   connections**: `P-A,   B-T`    - **Spool position at maximum P-A   orifice area** < P-A spool   stroke - **Spool position at maximum P-B   orifice area** > P-B spool stroke - **Spool position at maximum A-T   orifice area** > A-T spool stroke - **Spool position at maximum B-T   orifice area** < –B-T spool   stroke |
|  | Orifice A-T is open in the neutral position. Orifices P-B, A-T, and B-T are overlapped.  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**:   `A-T` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke - **Spool position at maximum A-T   orifice area** > –A-T spool stroke - **Spool position at maximum B-T   orifice area** > B-T spool stroke |
|  | Orifice B-T is open in the neutral position. Orifices P-A, P-B, and A-T are overlapped.  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**:   `B-T` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke - **Spool position at maximum A-T   orifice area** < –A-T spool   stroke - **Spool position at maximum B-T   orifice area** < B-T spool   stroke |
|  | Orifices P-A, P-B are open. Orifices A-T and B-T are overlapped.  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**: `P-A,   P-B` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** < P-A spool   stroke - **Spool position at maximum P-B   orifice area** > –P-B spool stroke - **Spool position at maximum A-T   orifice area** < –A-T spool   stroke - **Spool position at maximum B-T   orifice area** > B-T spool stroke |
|  | Orifice P-A is open in the neutral position. Orifices P-B, A-T, and B-T are overlapped.  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**:   `P-A` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** < P-A spool   stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke - **Spool position at maximum A-T   orifice area** < –A-T spool   stroke - **Spool position at maximum B-T   orifice area** > B-T spool stroke |
|  | Orifice P-B is open in the neutral position. Orifices P-A, A-T, and B-T are overlapped.  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**:   `P-B` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** > –P-B spool stroke - **Spool position at maximum A-T   orifice area** < –A-T spool   stroke - **Spool position at maximum B-T   orifice area** > B-T spool stroke |
|  | Orifices P-B and B-T are open in the neutral position. Orifices P-A and A-T are overlapped.  - **Positive spool position open   connections**: `P-B,   A-T` - **Neutral spool position open   connections**: `P-B,   B-T` - **Negative spool position open   connections**: `P-A,   B-T`    - **Spool position at maximum P-A   orifice area** < –P-A spool   stroke - **Spool position at maximum P-B   orifice area** < P-B spool   stroke - **Spool position at maximum A-T   orifice area** > A-T spool stroke - **Spool position at maximum B-T   orifice area** > –B-T spool stroke |
|  | Orifices P-A, P-B, A-T, and B-T are closed in the neutral position. P-T is open in the neutral position and closes when the spool displaces.  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**:   `P-T` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke - **Spool position at maximum A-T   orifice area** < –A-T spool   stroke - **Spool position at maximum B-T   orifice area** > B-T spool stroke - **Spool position at maximum P-T   orifice area** = any value |
|  | Orifice P-A is a constant orifice. Orifices P-B, A-T, and B-T are open in the neutral position.  - **Positive spool position open   connections**: `P-A,   P-B` - **Neutral spool position open   connections**: `P-A, P-B,   A-T, B-T` - **Negative spool position open   connections**: `P-A,   B-T`    - **Spool position at maximum P-A   orifice area** < P-A spool   stroke - **Spool position at maximum P-B   orifice area** < P-B spool   stroke - **Spool position at maximum A-T   orifice area** = any value - **Spool position at maximum B-T   orifice area** > –B-T spool stroke |
|  | Orifice P-B is a constant orifice. Orifices P-A, A-T, B-T are open in the neutral position.  - **Positive spool position open   connections**: `P-B,   A-T` - **Neutral spool position open   connections**: `P-A, P-B,   A-T, B-T` - **Negative spool position open   connections**: `P-A,   P-B`  - **Spool position at maximum P-A orifice   area** > –P-A spool stroke - **Spool position at maximum A-T orifice   area** < A-T spool stroke - **Spool position at maximum B-T orifice   area** = any value |
|  | Orifice P-A is closed in the neutral position. Ports **A** and **T** do not form a flow path.  - **Positive spool position open   connections**: `P-A,   P-B` - **Neutral spool position open   connections**: `All   closed` - **Negative spool position open   connections**: `P-A,   B-T`  - |**Spool position at maximum P-A orifice   area**| > P-A spool stroke - **Spool position at maximum P-B orifice   area** > P-B spool stroke - **Spool position at maximum B-T orifice   area** < –B-T spool stroke |
|  | Orifice P-B is closed in the neutral position. Ports **B** and **T** do not form a flow path.  - **Positive spool position open   connections**: `P-B,   A-T` - **Neutral spool position open   connections**: `All   closed` - **Negative spool position open   connections**: `P-A,   P-B`  - **Spool position at maximum P-A orifice   area** < –P-A spool stroke - |**Spool position at maximum P-B orifice   area**| > P-B spool stroke - **Spool position at maximum A-T orifice   area** > A-T spool stroke |
|  | Orifice P-A is closed in the neutral position. Orifice A-T is open in the neutral position.  - **Positive spool position open   connections**: `P-A,   P-B` - **Neutral spool position open   connections**: `A-T,   B-T` - **Negative spool position open   connections**: `P-A,   B-T`  - |**Spool position at maximum P-A orifice   area**| > P-A spool stroke - **Spool position at maximum P-B orifice   area** > P-B spool stroke - **Spool position at maximum A-T orifice   area** = any value - **Spool position at maximum B-T orifice   area** > –B-T spool stroke |
|  | Orifice P-B is closed in the neutral position. Orifice B-T is open in the neutral position.  - **Positive spool position open   connections**: `P-B,   A-T` - **Neutral spool position open   connections**: `A-T,   B-T` - **Negative spool position open   connections**: `P-A,   P-B`  - **Spool position at maximum P-A orifice   area** < –P-A spool stroke - |**Spool position at maximum P-B orifice   area**| > P-B spool stroke - **Spool position at maximum A-T orifice   area** < A-T spool stroke - **Spool position at maximum B-T orifice   area** = any value |
|  | Orifice P-B is closed in the neutral position. Orifice P-T is open in the neutral position. Ports **A** and **T** do not form a flow path.  - **Positive spool position open   connections**: `P-A,   P-B` - **Neutral spool position open   connections**:   `P-T` - **Negative spool position open   connections**: `P-B,   A-T`  - **Spool position at maximum P-A orifice   area** > P-A spool stroke - |**Spool position at maximum P-B orifice   area**| > P-B spool stroke - **Spool position at maximum B-T orifice   area** < –B-T spool stroke - **Spool position at maximum P-T orifice   area** = any value |
|  | Orifice P-A is closed in the neutral position. Orifice P-T is open in the neutral position. Ports **A** and **T** do not form a flow path.  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**:   `P-T` - **Negative spool position open   connections**: `P-A,   P-B`  - |**Spool position at maximum P-A orifice   area**| > P-A spool stroke - **Spool position at maximum P-B orifice   area** < –P-B spool stroke - **Spool position at maximum B-T orifice   area** > B-T spool stroke - **Spool position at maximum P-T orifice   area** = any value |

### Valve Orifice Parameterizations

The **Orifice parameterization** parameter sets the model for the
open area or volumetric flow rate through one or all of the valve orifices. The
block applies the same data for all flow paths if **Area
characteristics** is set to `Identical for all flow
paths`; otherwise, individual parameterizations are applied for the
`Different for all flow paths` setting. You can model
valve opening in three ways:

- `Linear - area vs. spool travel`

  The opening area is a linear function of the spool position received as a signal at port
  **S**:

  Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak,

  where:

  - *ΔS* is the spool travel defined in Orifice Definition and Spool Travel Direction.
  - *ΔSmax* is the
    **Spool travel between closed and open
    orifice**.
  - *Amax* is the
    **Maximum orifice area**.
  - *Aleak* is the
    **Leakage area**.

  *Aorifice* saturates
  at *Aleak* when
  *ΔS* is negative and saturates at
  *Amax* when the orifice is
  fully open. When the orifice is fully open, *ΔS* is equal
  to the spool stroke, so *ΔS* greater than the spool stroke
  does not further increase the orifice area.

  When the valve is in a near-open or near-closed position in the
  linear parameterization, you can maintain numerical robustness in your simulation by adjusting
  the **Smoothing factor** parameter. If the **Smoothing
  factor** parameter is nonzero, the block smoothly saturates the opening area
  between *Aleak* and
  *Amax*. For more information, see Numerical Smoothing.
- `Tabulated data - Area vs. spool travel`

  Provide spool travel vectors for your system or for individual flow paths
  between ports **P**, **A**,
  **B**, and **T**. This data will be
  used to calculate the relationship between the orifice area and spool
  displacement. Interpolation is used to determine the opening area between
  given data points. *A*leak and
  *A*max are the first and last
  parameters of the opening area vector, respectively.
- `Tabulated data - Volumetric flow rate vs. spool travel and
  pressure drop`

  Provide spool travel and pressure drop vectors and a dependent, 2-D
  volumetric flow rate array. Interpolation is used to determine flow rate
  between given data points. The mass flow rate is the product of the
  volumetric flow rate and the local density.

### Visualize Orifice Openings

To visualize spool offsets and maximum displacement, right-click the block and
select **Fluids** > **Plot Valve Characteristics**. The plot shows the orifices selected in the **Valve
Configuration** settings. The orifice parameterization sets the axes,
which are either:

- Orifice area versus spool position
- Volumetric flow rate versus spool position, queried at a specific
  pressure differential

When the positive, neutral, and negative settings in the
**Valve Configuration** feature the same orifice, the plot
displays the orifice openings as a constant.

To update the data after changing the block parameters, click **Reload
Data** on the figure window.

This image shows an example valve configuration. In the **Valve
Configuration** settings:

- **Positive spool position open connections** is
  `P-A, B-T`.
- **Neutral spool position open connections** is
  `P-T`.
- **Negative spool position open connections** is
  `P-B, A-T`.

In the **P-A Orifice** settings:

- **Spool position at maximum P-A orifice area** is
  `2.5e-3 m`.

All other spool positions are at the default values.

**Example Spool Position Visualization**

The visualization shows that the P-A orifice is open between the spool position at
`-2.53e-3` and `2.53e-3` m. Because the P-A
orifice is open only when the spool is displaced in the positive direction, setting
the **Consistency check for neutral spool and position open
connections** parameter to `Warning`
returns:

`Warning: P-A orifice must be closed when the spool is in
the neutral position. Adjust Spool position at maximum P-A orifice area, Neutral
spool position open connections, or Consistency check for neutral spool position
open connections. Right-click on the block and select Fluids > Plot Valve
Characteristics to view the area or flow of each connection versus spool
position.`

To resolve this warning, you can change:

- **Spool position at maximum P-A orifice area** to a
  value larger than 0.005 m.
- **Consistency check for neutral spool position open
  connections** to `None`.
- The valve configuration by setting **Neutral spool position
  open connections** to
  `P-A`.

### Faults

To model a fault, in the **Faults** section,
click the **Add fault** hyperlink next to the fault that you want to model. Use
the fault parameters to specify the fault properties. For more information about fault modeling,
see Introduction to Simscape Faults.

The **Spool position when faulted** parameter has four fault options:

- `Positive` — The spool position
  freezes in the positive position, opening the flow paths specified by
  the **Positive spool position open connections**
  parameter to their maximum value. The flow paths specified by the
  **Negative spool position open connections** and
  **Neutral spool position open connections**
  parameters are closed.
- `Neutral` — The spool position freezes
  in the neutral position, opening all flow paths to their specified
  values at 0 m.
- `Negative` — The spool position
  freezes in the negative position, opening the flow paths specified by
  the **Negative spool position open connections**
  parameter to their maximum value. The flow paths specified by the
  **Positive spool position open connections** and
  **Neutral spool position open connections**
  parameters are closed.
- `Maintain last value` — The valve
  freezes at the spool position when the trigger occurs.

Due to numerical smoothing at the extremes of the valve area, in the
linear parameterization, the minimum area that he block uses is larger than the
**Leakage area**, and the maximum is smaller than the
**Maximum orifice area**, in proportion to the
**Smoothing factor** value. For more information, see Numerical Smoothing.

After the fault triggers, the valve remains at the faulted area for the rest of the
simulation.

### Composite Structure

This block is a composite component comprising of multiple instances of the Orifice
(IL) block. Refer to the Orifice
(IL) block for more detail on the valve parameterizations and
block calculations.

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
