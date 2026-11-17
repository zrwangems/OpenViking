---
type: simulink-block
title: '4-Way 2-Position Directional Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: '4way2positiondirectionalvalveil'
documentation_source_path: 'ref/4way2positiondirectionalvalveil.html'
language: en
---

# 4-Way 2-Position Directional Valve (IL)

## Ports
```yaml
ports:
- name: A
  summary: Entry or exit port isothermal liquid
  direction: conserving
- name: B
  summary: Entry or exit port isothermal liquid
  direction: conserving
- name: P
  summary: Entry or exit port isothermal liquid
  direction: conserving
- name: T
  summary: Entry or exit port isothermal liquid
  direction: conserving
- name: S
  summary: Spool displacement, m physical signal
  direction: input
```

### Conserving

### **A** — Entry or exit port isothermal liquid

Liquid entry or exit port to the valve.

### **B** — Entry or exit port isothermal liquid

Liquid entry or exit port to the valve.

### **P** — Entry or exit port isothermal liquid

Liquid entry or exit port to the valve.

### **T** — Entry or exit port isothermal liquid

Liquid entry or exit port to the valve.
### Input

### **S** — Spool displacement, m physical signal

Physical signal associated with the spool displacement, in m.
## Parameters
```yaml
parameters:
- name: Positive spool position open connections
  summary: Flow paths open when spool is in a positive position P-A, B-T (default) | P-A, P-B | P-B, A-T | P-A | P-B | P-A,
    P-B, A-T, B-T
  group: Valve Configuration
- name: Negative spool position open connections
  summary: Flow paths open when spool moves in the negative direction P-B, A-T (default) | P-A, B-T | P-A, P-B | P-A | P-B
    | P-A, P-B, A-T, B-T
  group: Valve Configuration
- name: Area characteristics
  summary: Flow equations for orifices Identical for all flow paths (default) | Different for each flow path
  group: Model Parameterization
- name: Orifice parameterization
  summary: Method of calculating opening area Linear area vs. spool travel (default) | Tabulated data - Area vs. spool travel
    | Tabulated data - Volumetric flow rate vs. spool travel and pressure drop
  group: Model Parameterization
- name: Spool travel between closed and open orifice
  summary: Maximum spool stroke 0.005 m (default) | positive scalar
  group: Model Parameterization
- name: Maximum orifice area
  summary: Maximum orifice opening area 1e-4 m^2 (default) | positive scalar
  group: Model Parameterization
- name: Leakage area
  summary: Open area when orifice is fully closed 1e-10 m^2 (default) | positive scalar
  group: Model Parameterization
- name: Spool travel vector
  summary: Vector of spool opening distances relative to fully closed position [0, .00125, .0025, .00375, .005] m (default)
    | 1-by-*n* vector
  group: Model Parameterization
- name: Orifice area vector
  summary: Vector of valve opening areas [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2 (default) | 1-by-*n* vector
  group: Model Parameterization
- name: Spool travel vector, ds
  summary: Vector of spool opening distances relative to fully closed position [0, .00125, .0025, .00375, .005] m (default)
    | 1-by-*n* vector
  group: Model Parameterization
- name: Pressure drop vector, dp
  summary: Vector of valve pressure drop values [-.1, .3, .5, .7] MPa (default) | 1-by-*n* vector
  group: Model Parameterization
- name: Volumetric flow rate table, q(ds,dp)
  summary: Array of volumetric flow rates [-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063,
    .00081, .00096; .00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s (default) | *M*-by-*N* matrix
  group: Model Parameterization
- name: Constant orifice area
  summary: Orifice area for identical flow paths 1e-4 m^2 (default) | positive scalar
  group: Model Parameterization
- name: Constant orifice pressure drop vector
  summary: Vector of pressure differential values for identical flow paths [-.1, .3, .5, .7] MPa (default) | 1-by-*n* vector
  group: Model Parameterization
- name: Constant orifice volumetric flow rate vector
  summary: Vector of volumetric flow rate values for identical flow paths [-.0009, .0016, .002, .0024] m^3/s (default) | 1-by-*n*
    vector
  group: Model Parameterization
- name: Cross-sectional area at ports P, T, A and B
  summary: Area at conserving ports inf m^2 (default) | positive scalar
  group: Model Parameterization
- name: Discharge coefficient
  summary: Discharge coefficient 0.64 (default) | positive scalar
  group: Model Parameterization
- name: Critical Reynolds number
  summary: Upper Reynolds number limit for laminar flow 150 (default) | positive scalar
  group: Model Parameterization
- name: Smoothing factor
  summary: Numerical smoothing factor 0.01 (default) | positive scalar in the range of [0,1]
  group: Model Parameterization
- name: Pressure recovery
  summary: Whether to account for pressure increase in area expansions off (default) | on
  group: Model Parameterization
- name: Spool position at maximum P-A orifice area
  summary: Spool offset for fully open P-A orifice 5e-3 m (default) | positive scalar
  group: P-A Orifice
- name: P-A spool travel between closed and open orifice
  summary: Maximum spool stroke 0.005 m (default) | positive scalar
  group: P-A Orifice
- name: P-A maximum orifice area
  summary: Maximum orifice opening area 1e-4 m^2 (default) | positive scalar
  group: P-A Orifice
- name: P-A orifice spool travel vector
  summary: Vector of spool opening distances relative to fully closed position [0, .00125, .0025, .00375, .005] m (default)
    | 1-by-*n* vector
  group: P-A Orifice
- name: P-A orifice area vector
  summary: Vector of valve opening areas [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2 (default) | 1-by-*n* vector
  group: P-A Orifice
- name: P-A orifice spool travel vector, ds
  summary: Vector of spool opening distances relative to fully closed position [0, .00125, .0025, .00375, .005] m (default)
    | 1-by-*n* vector
  group: P-A Orifice
- name: P-A orifice pressure drop vector, dp
  summary: Vector of pressure drop values [-.1, .3, .5, .7] MPa (default) | 1-by-*n* vector
  group: P-A Orifice
- name: P-A orifice volumetric flow rate table, q(ds,dp)
  summary: Array of volumetric flow rate values [-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036,
    .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s (default) | *M*-by-*N* matrix
  group: P-A Orifice
- name: P-A constant orifice area
  summary: Cross-sectional area for constant orifice 1e-4 m^2 (default) | positive scalar
  group: P-A Orifice
- name: P-A constant orifice pressure drop vector
  summary: Vector of pressure differential values for a constant orifice [-.1, .3, .5, .7] MPa (default) | 1-by-*n* vector
  group: P-A Orifice
- name: P-A constant orifice volumetric flow rate vector
  summary: Vector of volumetric flow rates for constant orifice [-.0009, .0016, .002, .0024] m^3/s (default) | 1-by-*n* vector
  group: P-A Orifice
- name: Spool position at maximum P-B orifice area
  summary: Spool offset for fully open P-B orifice -5e-3 (default) | positive scalar
  group: P-B Orifice
- name: P-B spool travel between closed and open orifice
  summary: Maximum spool stroke 0.005 m (default) | positive scalar
  group: P-B Orifice
- name: P-B maximum orifice area
  summary: Maximum orifice opening area 1e-4 m^2 (default) | positive scalar
  group: P-B Orifice
- name: P-B orifice spool travel vector
  summary: Vector of spool opening distances relative to fully closed position [0, .00125, .0025, .00375, .005] m (default)
    | 1-by-*n* vector
  group: P-B Orifice
- name: P-B orifice area vector
  summary: Vector of valve opening areas [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2 (default) | 1-by-*n* vector
  group: P-B Orifice
- name: P-B orifice spool travel vector, ds
  summary: Vector of spool opening distances relative to fully closed position [0, .00125, .0025, .00375, .005] m (default)
    | 1-by-*n* vector
  group: P-B Orifice
- name: P-B orifice pressure drop vector, dp
  summary: Vector of pressure differential values [-.1, .3, .5, .7] MPa (default) | 1-by*n* vector
  group: P-B Orifice
- name: P-B orifice volumetric flow rate table, q(ds,dp)
  summary: Array of volumetric flow rate values [-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036,
    .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s (default) | *M*-by-*N* matrix
  group: P-B Orifice
- name: P-B constant orifice area
  summary: Cross-sectional area for constant orifice 1e-4 m^2 (default) | positive scalar
  group: P-B Orifice
- name: P-B constant orifice pressure drop vector
  summary: Vector of pressure differential values for constant orifice [-.1, .3, .5, .7] MPa (default) | 1-by-*n* vector
  group: P-B Orifice
- name: P-B constant volumetric flow rate vector
  summary: Vector of volumetric flow rate values for constant orifice [-.0009, .0016, .002, .0024] m^3/s (default) | 1-by-*n*
    vector
  group: P-B Orifice
- name: Spool position at maximum A-T orifice area
  summary: Spool offset for fully open A-T orifice -5e-3 m (default) | positive scalar
  group: A-T Orifice
- name: A-T spool travel between closed and open orifice
  summary: Maximum spool stroke 0.005 m (default) | positive scalar
  group: A-T Orifice
- name: A-T maximum orifice area
  summary: Maximum orifice opening area 1e-4 m^2 (default) | positive scalar
  group: A-T Orifice
- name: A-T orifice spool travel vector
  summary: Vector of spool opening distances relative to fully closed position [0, .00125, .0025, .00375, .005] m (default)
    | 1-by-*n* vector
  group: A-T Orifice
- name: A-T orifice spool travel vector
  summary: Vector of spool opening distances relative to fully closed position [0, .00125, .0025, .00375, .005] m (default)
    | 1-by-*n* vector
  group: A-T Orifice
- name: A-T orifice spool travel vector, ds
  summary: Vector of spool opening distances relative to fully closed position [0, .00125, .0025, .00375, .005] m (default)
    | 1-by-*n* vector
  group: A-T Orifice
- name: A-T orifice pressure drop vector, dp
  summary: Vector of pressure differential values [-.1, .3, .5, .7] MPa (default) | 1-by-*n* vector
  group: A-T Orifice
- name: A-T orifice volumetric flow rate table, q(ds,dp)
  summary: Array of volumetric flow rate values [-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036,
    .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s (default) | *M*-by-*N* matrix
  group: A-T Orifice
- name: A-T constant orifice area
  summary: Cross-sectional area for constant orifice 1e-4 m^2 (default) | positive scalar
  group: A-T Orifice
- name: A-T constant orifice pressure drop vector
  summary: Vector of pressure differential values for constant orifice [-.1, .3, .5, .7] MPa (default) | 1-by-*n* vector
  group: A-T Orifice
- name: A-T constant orifice volumetric flow rate vector
  summary: Vector of volumetric flow rate values for constant orifice [-.0009, .0016, .002, .0024] m^3/s (default) | 1-by-*n*
    vector
  group: A-T Orifice
- name: Spool position at maximum B-T orifice area
  summary: Spool offset for fully open B-T orifice 5e-3 m (default) | positive scalar
  group: B-T Orifice
- name: B-T spool travel between closed and open orifice
  summary: Maximum spool stroke 0.005 m (default) | positive scalar
  group: B-T Orifice
- name: B-T maximum orifice area
  summary: Maximum orifice opening area 1e-4 m^2 (default) | positive scalar
  group: B-T Orifice
- name: B-T orifice spool travel vector
  summary: Vector of spool opening distances relative to fully closed position [0, .00125, .0025, .00375, .005] m (default)
    | 1-by-*n* vector
  group: B-T Orifice
- name: B-T orifice area vector
  summary: Vector of valve opening areas [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2 (default) | 1-by-*n* vector
  group: B-T Orifice
- name: B-T orifice spool travel vector, ds
  summary: Vector of spool opening distances relative to fully closed position [0, .00125, .0025, .00375, .005] m (default)
    | 1-by-*n* vector
  group: B-T Orifice
- name: B-T orifice pressure drop vector, dp
  summary: Vector of pressure differential values [-.1, .3, .5, .7] MPa (default) | 1-by-*n* vector
  group: B-T Orifice
- name: B-T orifice volumetric flow rate table, q(ds,dp)
  summary: Array of volumetric flow rate values [-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036,
    .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s (default) | *M*-by-*N* matrix
  group: B-T Orifice
- name: B-T constant orifice area
  summary: Cross-sectional orifice area for constant orifice 1e-4 m^2 (default) | positive scalar
  group: B-T Orifice
- name: B-T constant orifice pressure drop vector
  summary: Vector of pressure differential values for constant orifice [-.1, .3, .5, .7] MPa (default) | 1-by-*n* vector
  group: B-T Orifice
- name: B-T constant volumetric flow rate vector
  summary: Vector of volumetric flow rates for constant orifice [-.0009, .0016, .002, .0024] m^3/s (default) | 1-by-*n* vector
  group: B-T Orifice
- name: 4-Way 2-Position Directional Valve Area fault
  summary: Option to model valve area fault Add fault
  group: Faults
- name: Spool position when faulted
  summary: Faulted valve characteristics Positive (default) | Negative | Maintain last value
  group: Faults
```

### Valve Configuration

### **Positive spool position open connections** — Flow paths open when spool is in a positive position `P-A, B-T` (default) | `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-T, B-T`

Flow paths open when the spool is in a positive position. This
parameter sets the valve configuration and defines the direction of
spool movement according to the signal received at port
**S**.

### **Negative spool position open connections** — Flow paths open when spool moves in the negative direction `P-B, A-T` (default) | `P-A, B-T` | `P-A, P-B` | `P-A` | `P-B` | `P-A, P-B, A-T, B-T`

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

### **Orifice parameterization** — Method of calculating opening area `Linear area vs. spool travel` (default) | `Tabulated data - Area vs. spool travel` | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`

Method of calculating the valve opening area. If you set this
parameter to one of the tabulated data parameterizations, you can
provide your own valve area and spool travel data for nonlinear valve
opening profiles, or provide data in terms of volumetric flow rate,
spool travel, and pressure drop over the flow path.

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

### **Leakage area** — Open area when orifice is fully closed `1e-10 m^2` (default) | positive scalar

Open area when an orifice is fully closed. The block maintains any
area smaller than this value at the specified leakage area. This
parameter contributes to numerical stability by maintaining continuity
in the flow.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Linear - Area vs.
spool travel`.

### **Spool travel vector** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances when parameterizing the orifice
according to tabulated valve area data. The vector elements must
correspond one-to-one with the elements in the **Orifice area
vector** parameter. List the values in ascending order. The
first element must be 0. The block uses linear interpolation between
table data points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Tabulated data -
Area vs. spool travel`.

### **Orifice area vector** — Vector of valve opening areas `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of opening areas when parameterizing the orifice according to
tabulated valve area data. The vector elements must correspond
one-to-one with the elements in the **Spool travel
vector** parameter. List the values in ascending order. The
elements must be greater than 0.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Tabulated data -
Area vs. spool travel`.

### **Spool travel vector, ds** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances when parameterizing the orifice
according to tabulated volumetric flow rate data. The spool travel
vector forms an independent axis with the **Pressure drop
vector, dp** parameter for the 2-D dependent
**Volumetric flow rate table, q(ds,dp)** parameter.
List the values in ascending order. The first element must be 0. The
block uses linear interpolation between table data points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`.

### **Pressure drop vector, dp** — Vector of valve pressure drop values `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure drop values when parameterizing the orifice
according to tabulated flow rate data. The pressure drop vector forms an
independent axis with the **Spool travel vector, ds**
parameter for the 2-D dependent **Volumetric flow rate table,
q(ds,dp)** parameter. List the values in ascending order.
The values must be greater than 0. The block uses linear interpolation
between table data points.

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

Orifice area when the positive and negative spool positions include the same
orifice.

#### Dependencies

To enable this parameter, set **Area characteristics** to
`Identical for all flow paths` and
**Orifice parameterization** to either:

- `Linear - area vs. spool
  travel`
- `Tabulated data - Area vs. spool
  travel`

Select the same orifice for both of the parameters in
the **Valve Configuration** section:

- **Positive spool position open
  connections**
- **Negative spool position open
  connections**

### **Constant orifice pressure drop vector** — Vector of pressure differential values for identical flow paths `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure differential values over the valve when the positive and negative
spool positions include the same orifice. The vector elements correspond
one-to-one with the elements in the **Constant orifice
volumetric flow rate vector** parameter. List the values in
ascending order. The block uses linear interpolation between the data
points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`.

Select the same orifice for both of the parameters in the **Valve
Configuration** section:

- **Positive spool position open
  connections**
- **Negative spool position open
  connections**

### **Constant orifice volumetric flow rate vector** — Vector of volumetric flow rate values for identical flow paths `[-.0009, .0016, .002, .0024] m^3/s` (default) | 1-by-*n* vector

Vector of volumetric flow rate values for a constant orifice when the positive and
negative spool positions include the same orifice. The vector elements
correspond one-to-one with the elements in the **Constant
orifice pressure drop vector** parameter. List the values
in ascending order. The block uses linear interpolation between the data
points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`.

Select the same orifice for both of the parameters in the **Valve
Configuration** section:

- **Positive spool position open
  connections**
- **Negative spool position open
  connections**

### **Cross-sectional area at ports P, T, A and B** — Area at conserving ports `inf m^2` (default) | positive scalar

Maximum cross-sectional areas at the entry and exit ports **P**,
**T**, **A**, and
**B**, which the block uses in the pressure-flow
rate equation that determines the mass flow rate through the
valve.

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

### **Spool position at maximum P-A orifice area** — Spool offset for fully open P-A orifice `5e-3 m` (default) | positive scalar

Spool offset from the neutral position for a fully open P-A orifice.

#### Dependencies

To enable this parameter, set one of these parameters.

Set **Positive spool position open connections** to:

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

Set **Negative spool position open
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
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

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

Vector of spool travel distances for the tabular parameterization of the valve area. The
vector elements must correspond one-to-one with the elements in the
**P-A orifice area vector** parameter. List the
values in ascending order. The first element must be 0. The block uses
linear interpolation between the data points.

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
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A orifice area vector** — Vector of valve opening areas `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of opening areas for the tabular parameterization of the valve area. The vector
elements must correspond one-to-one with the elements in the
**P-A spool travel vector** parameter. The elements
are listed in ascending order. The elements must be greater than
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
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A orifice spool travel vector, ds** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances for the tabular parameterization of the volumetric flow
rates. The spool travel vector forms an independent axis with the
**P-A orifice pressure drop vector, dp** parameter
for the 2-D dependent **P-A orifice volumetric flow rate table,
q(ds,dp)** parameter. List the values in ascending order.
The first element must be 0. The block uses linear interpolation between
the data points.

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
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A orifice pressure drop vector, dp** — Vector of pressure drop values `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure drop values for the tabular parameterization of the volumetric flow
rates. The pressure drop vector forms an independent axis with the
**P-A orifice spool travel vector, ds** parameter
for the 2-D dependent **P-A orifice volumetric flow rate table,
q(ds,dp)** parameter. List the values in ascending order.
The elements must be greater than 0. The block uses linear interpolation
between the data points.

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
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

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
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A constant orifice area** — Cross-sectional area for constant orifice `1e-4 m^2` (default) | positive scalar

Orifice area when the positive and negative spool positions include
the same orifice.

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

This parameter is enabled only when the P-A orifice
settings appear in both the **Positive
spool position open connections** and **Negative spool position open
connections** parameters.

### **P-A constant orifice pressure drop vector** — Vector of pressure differential values for a constant orifice `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure differential values over the valve when the
positive and negative spool positions include the same orifice. The
vector elements correspond one-to-one with the elements in the
**P-A constant orifice volumetric flow rate
vector** parameter. List the values in ascending order. The
block uses linear interpolation between the data points.

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

This parameter is enabled only when the P-A orifice
settings appear in both the **Positive
spool position open connections** and **Negative spool position open
connections** parameters.

### **P-A constant orifice volumetric flow rate vector** — Vector of volumetric flow rates for constant orifice `[-.0009, .0016, .002, .0024] m^3/s` (default) | 1-by-*n* vector

Vector of pressure differential values over the valve when the
positive and negative spool positions include the same orifice. The
vector elements correspond one-to-one with the elements in the
**P-A constant orifice pressure drop vector**
parameter. List the values in ascending order. The block uses linear
interpolation between the data points.

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

### P-B Orifice

### **Spool position at maximum P-B orifice area** — Spool offset for fully open P-B orifice `-5e-3` (default) | positive scalar

Spool offset from the neutral position for a fully open P-B orifice.

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

**Note:**

This parameter is enabled only when the P-B orifice
settings do not appear in both the **Positive spool position open connections** and
**Negative spool position open
connections** parameters.

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
   - `P-A, P-B, A-T,
     B-T`

   or set **Negative spool position
   open connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

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

Vector of spool travel distances for the tabular parameterization of the valve area. The
vector elements must correspond one-to-one with the elements in the
**P-B orifice area vector** parameter. List the
values in ascending order. The first element must be 0. The block uses
linear interpolation between the data points.

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
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B orifice area vector** — Vector of valve opening areas `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of opening areas for the tabular parameterization of the valve area. The vector
elements must correspond one-to-one with the elements in the
**P-B spool travel vector** parameter. List the
elements in ascending order. The elements must be greater than 0.

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
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B orifice spool travel vector, ds** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances for the tabular parameterization of the volumetric flow
rates. The spool travel vector forms an independent axis with the
**P-B orifice pressure drop vector, dp** parameter
for the 2-D dependent **P-B orifice volumetric flow rate table,
q(ds,dp)** parameter. List the values in ascending order.
The first element must be 0. The block uses linear interpolation between
the data points.

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
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B orifice pressure drop vector, dp** — Vector of pressure differential values `[-.1, .3, .5, .7] MPa` (default) | 1-by*n* vector

Vector of pressure drop values for tabular parameterization of the volumetric flow
rates. The pressure drop vector forms an independent axis with the
**P-B orifice spool travel vector, ds** parameter
for the 2-D dependent **P-B orifice volumetric flow rate table,
q(ds,dp)** parameter. List the values in ascending order.
The elements must be greater than 0. The block uses linear interpolation
between the data points.

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
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

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
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** to:

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B constant orifice area** — Cross-sectional area for constant orifice `1e-4 m^2` (default) | positive scalar

Orifice area when the positive and negative spool positions include
the same orifice.

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

### **P-B constant orifice pressure drop vector** — Vector of pressure differential values for constant orifice `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure differential values over the valve when the
positive and negative spool positions include the same orifice. The
vector elements correspond one-to-one with the elements in the
**P-B constant orifice volumetric flow rate
vector** parameter. List the values in ascending order. The
block uses linear interpolation between the data points.

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

### **P-B constant volumetric flow rate vector** — Vector of volumetric flow rate values for constant orifice `[-.0009, .0016, .002, .0024] m^3/s` (default) | 1-by-*n* vector

Vector of volumetric flow rate values over the valve when the positive
and negative spool positions include the same orifice. The vector
elements correspond one-to-one with the elements in the **P-B
constant orifice pressure drop vector** parameter. List the
values in ascending order. The block uses linear interpolation between
the data points.

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

### A-T Orifice

### **Spool position at maximum A-T orifice area** — Spool offset for fully open A-T orifice `-5e-3 m` (default) | positive scalar

Spool offset from the neutral position for a fully open A-T
orifice.

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

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Linear - Area vs. spool
   travel`.
3. One of the following parameters:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

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

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

### **A-T orifice spool travel vector** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances for the tabular parameterization of the valve area. The
vector elements must correspond one-to-one with the elements in the
**A-T orifice area vector** parameter. List the
values in ascending order. The first element must be 0. The block uses
linear interpolation between the data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Area vs. spool
   travel`.
3. One of the following parameters:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

### **A-T orifice spool travel vector** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances for the tabular parameterization of the valve area. The
vector elements must correspond one-to-one with the elements in the
**A-T orifice area vector** parameter. List the
values in ascending order. The first element must be 0. The block uses
linear interpolation between the data points.

#### Dependencies

To enable this parameter, set:

1. **Area characteristics** to
   `Different for each flow
   path`.
2. **Orifice parameterization** to
   `Tabulated data - Area vs. spool
   travel`.
3. One of the following parameters:

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

### **A-T orifice spool travel vector, ds** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances for the tabular parameterization of the volumetric flow
rates. The spool travel vector forms an independent axis with the
**A-T orifice pressure drop vector, dp** parameter
for the 2-D dependent **A-T orifice volumetric flow rate table,
q(ds,dp)** parameter. List the values in ascending order.
The first element must be 0. The block uses linear interpolation between
the data points.

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

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

### **A-T orifice pressure drop vector, dp** — Vector of pressure differential values `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure drop values for tabular parameterization of the volumetric flow
rates. The pressure drop vector forms an independent axis with the
**A-T orifice spool travel vector, ds** parameter
for the 2-D dependent **A-T orifice volumetric flow rate table,
q(ds,dp)** parameter. List the values in ascending order.
The elements must be greater than 0. The block uses linear interpolation
between the data points.

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

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

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

   - **Positive spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.
   - **Negative spool position open
     connections** to `P-B,
     A-T` or `P-A, P-B, A-T,
     B-T`.

### **A-T constant orifice area** — Cross-sectional area for constant orifice `1e-4 m^2` (default) | positive scalar

Orifice area when the positive and negative spool positions include
the same orifice.

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

### **A-T constant orifice pressure drop vector** — Vector of pressure differential values for constant orifice `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure differential values over the valve when the
positive and negative spool positions include the same orifice. The
vector elements correspond one-to-one with the elements in the
**A-T constant orifice volumetric flow rate
vector** parameter. List the values in ascending order. The
block uses linear interpolation between the data points.

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

### **A-T constant orifice volumetric flow rate vector** — Vector of volumetric flow rate values for constant orifice `[-.0009, .0016, .002, .0024] m^3/s` (default) | 1-by-*n* vector

Vector of volumetric flow rate values when the positive and negative
spool positions include the same orifice. The vector elements correspond
one-to-one with the elements in the **A-T constant orifice
pressure drop vector** parameter. List the values in
ascending order. The block uses linear interpolation between the data
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

### B-T Orifice

### **Spool position at maximum B-T orifice area** — Spool offset for fully open B-T orifice `5e-3 m` (default) | positive scalar

Spool offset from the neutral position for a fully open B-T
orifice.

#### Dependencies

To enable this parameter, set one of the following parameters:

- **Positive spool position open
  connections** to `P-A,
  B-T`.
- **Negative spool position open
  connections** to `P-A,
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

   **Negative spool position open connections** to `P-A,
   B-T`.

### **B-T orifice spool travel vector** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of spool travel distances for the tabular parameterization of the valve area. The
vector elements must correspond one-to-one with the elements in the
**B-T orifice area vector** parameter. List the
values in ascending order. The first element must be 0. The block uses
linear interpolation between the data points.

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

   **Negative spool position open connections** to `P-A,
   B-T`.

### **B-T orifice area vector** — Vector of valve opening areas `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of opening areas for the tabular parameterization of the valve area. The vector
elements must correspond one-to-one with the elements in the
**B-T orifice spool travel vector** parameter. The
elements are listed in ascending order. The elements must be greater
than 0.

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

   **Negative spool position open connections** to `P-A,
   B-T`.

### **B-T orifice spool travel vector, ds** — Vector of spool opening distances relative to fully closed position `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of control member travel distances for the tabular parameterization of the
volumetric flow rates. The spool travel vector forms an independent axis
with the **B-T orifice pressure drop vector, dp**
parameter for the 2-D dependent **B-T orifice volumetric flow
rate table, q(ds,dp)** parameter. List the values in
ascending order. The first element must be 0. The block uses linear
interpolation between the data points.

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

   **Negative spool position open connections** to `P-A,
   B-T`.

### **B-T orifice pressure drop vector, dp** — Vector of pressure differential values `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure drop values for tabular parameterization of the volumetric flow
rates. The pressure drop vector forms an independent axis with the
**B-T orifice spool travel vector, ds** parameter
for the 2-D dependent **B-T orifice volumetric flow rate table,
q(ds,dp)** parameter. List the values in ascending order.
The elements must be greater than 0. The block uses linear interpolation
between the data points.

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

   **Negative spool position open connections** to `P-A,
   B-T`.

### **B-T constant orifice area** — Cross-sectional orifice area for constant orifice `1e-4 m^2` (default) | positive scalar

Orifice area when the positive and negative spool positions include
the same orifice.

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

   **Negative spool position open connections** to `P-A,
   B-T`.

**Note:**

This parameter is enabled only when the B-T orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **B-T constant orifice pressure drop vector** — Vector of pressure differential values for constant orifice `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure differential values over the valve when the
positive and negative spool positions include the same orifice. The
vector elements correspond one-to-one with the elements in the
**B-T constant orifice volumetric flow rate
vector** parameter. List the values in ascending order. The
block uses linear interpolation between the data points.

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

   **Negative spool position open
   connections** to `P-A,
   B-T`.

**Note:**

This parameter is enabled only when the B-T orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### **B-T constant volumetric flow rate vector** — Vector of volumetric flow rates for constant orifice `[-.0009, .0016, .002, .0024] m^3/s` (default) | 1-by-*n* vector

Vector of pressure differential values over the valve when the
positive and negative spool positions include the same orifice. The
vector elements correspond one-to-one with the elements in the
**B-T constant orifice pressure drop vector**
parameter. List the values in ascending order. The block uses linear
interpolation between the data points.

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

   **Negative spool position open
   connections** to `P-A,
   B-T`.

**Note:**

This parameter is enabled only when the B-T orifice settings
appear in both the **Positive spool position
open connections** and **Negative spool position open connections**
parameters.

### Faults

### **4-Way 2-Position Directional Valve Area fault** — Option to model valve area fault `Add fault`

Option to model a valve area fault in the block. To add a fault, click the **Add
fault** hyperlink. When a fault occurs, the valve area
normally set by the opening parameterization is set based on the value
specified in the **Spool position when faulted**
parameter.

### **Spool position when faulted** — Faulted valve characteristics `Positive` (default) | `Negative` | `Maintain last value`

Faulted valve spool position. You can choose for the valve to seize
when the spool is in the positive position, negative position, or at the
position when the fault triggers.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink.
## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Directional Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

### R2024a: Model faults with the Simscape faults interface

The 4-Way 2-Position Directional Valve (IL) block now supports the Simscape™ faults interface. To learn more, see Introduction to Simscape Faults.

## Description

4-way 2-position directional valve in an isothermal liquid network

The 4-Way 2-Position Directional Valve (IL) block models a valve with four openings — such
as the valves between an actuator, pump, and tank — in an isothermal liquid network. The
valve operation is controlled by a single spool displaced according to the signal at
port **S**. You can set the baseline configuration of your valve by
specifying the orifices that are open when the spool moves in the positive direction and
negative directions in the **Positive spool position open connections**
and **Negative spool position open connections** parameters,
respectively. You can set the valve opening model in the **Orifice
parameterization** parameter as a linear relationship or function of
user-provided data, which you can apply to one or all flow paths in the valve.

This block is a composite component that comprises of multiple instances of the
Orifice
(IL) block. Refer to the Orifice
(IL) block for more details about the valve parameterizations and
block calculations. In some configurations, this valve resembles a 3-way valve. To set
additional flow paths when the spool is in the neutral position, see the 4-Way 3-Position
Directional Valve (IL) block.

This image shows an example valve setup where the valve is connected to a tank, actuator,
and pump and the **Positive spool position open connections** parameter
is `P-B, A-T`:

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

The *spool stroke* is the amount of spool travel an orifice takes to
fully open from a closed position. You can use the **Orifice
parameterization** and **Area characteristics**
parameters to specify the flow path characteristics:

| Orifice Parameterization | Identical for All Flow Paths | Different for Each Flow Path |
| --- | --- | --- |
| `Linear - Area vs. spool travel` | The **Spool travel between closed and open orifice** parameter defines the spool stroke | The **Spool travel between closed and open orifice** parameter defines the spool stroke for each orifice |
| `Tabulated data - Area vs. spool travel` | The difference between the first and last element of the **Spool travel vector** parameter defines the spool stroke | The difference between the first and last element of the **Spool travel vector** parameter for each orifice |
| `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` | The difference between the first and last element of the **Spool travel vector, ds** parameter defines the spool stroke | The difference between the first and last element of the **Spool travel vector, ds** parameter defines the spool stroke for each orifice |

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

Where *S*orifice\_max is the spool position at the
maximum orifice area defined for each orifice. The orifice area saturates at the
leakage area when *ΔS* is negative and saturates at the maximum
orifice area when the orifice is fully open. When the orifice is fully open,
*ΔS* is equal to the spool stroke, so *ΔS*
greater than the spool stroke does not further increase the orifice area.

This table shows the possible configurations of the 4-Way 2-Position Directional Valve
(IL):

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

The **Orifice parameterization** parameter specifies the model for the
open area or volumetric flow rate through one or all of the valve orifices. If you
set **Area characteristics** to `Identical for all flow
paths`, the block applies the same data for all flow paths. When
you select `Different for all flow paths`, the block uses
individual parameterizations for each flow path.

When **Orifice parameterization** is `Linear - area
vs. spool travel`, the opening area is a linear function of the
spool position received as a signal at port **S**

Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak,

where:

- *ΔS* is the spool travel.

  *Aorifice* saturates at
  *Aleak* when
  *ΔS* is negative and saturates at
  *Amax* when the orifice is
  fully open. When the orifice is fully open, *ΔS* is equal
  to the spool stroke, so a value of *ΔS* that is greater
  than the spool stroke does not increase the orifice area.
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

When **Orifice parameterization** is `Tabulated data
- Area vs. spool travel`, you can provide spool travel vectors for
your system or for individual flow paths between ports **P**,
**A**, **B**, and **T**. The
block uses this data to calculate the relationship between the orifice area and
spool displacement. The block uses interpolation to determine the opening area
between the data points. *A*leak and
*A*max are the first and last parameters
of the opening area vector, respectively.

When **Orifice parameterization** is `Tabulated data
- Volumetric flow rate vs. spool travel and pressure drop`, you can
provide spool travel and pressure drop vectors and a dependent, 2-D volumetric flow
rate array. The block uses interpolation to determine the flow rate between the data
points. The mass flow rate is the product of the volumetric flow rate and the local
density.

### Visualize Orifice Openings

To visualize the spool offsets and maximum displacement, right-click the block and
select **Fluids** > **Plot Valve Characteristics**. The plot shows the orifices specified by the parameters in
**Valve Configuration** section. The axes are either:

- Orifice Area verses Spool Position
- Volumetric Flow Rate verses Spool Position, queried at a specific
  pressure differential

When you set the parameters in the **Valve
Configuration** tab to the same orifice, the orifice opening is a
constant.

Click **Reload Data** to update the data in the figure.

This image shows the default configuration for the block:

- **Positive spool position open connections** is
  `P-A, B-T`.
- **Negative spool position open connections** is
  `P-B, A-T`.

All other spool positions are at the default values.

**Example Spool Position Visualization**

### Faults

To model a fault, in the **Faults** section,
click the **Add fault** hyperlink next to the fault that you want to model. Use
the fault parameters to specify the fault properties. For more information about fault modeling,
see Introduction to Simscape Faults.

The **Spool position when faulted** parameter has three fault options:

- `Positive` — The spool position
  freezes in the positive position, opening the flow paths specified by
  the **Positive spool position open connections**
  parameter to their maximum value. The flow paths specified by the
  **Negative spool position open connections**
  parameter are closed.
- `Negative` — The spool position
  freezes in the negative position, opening the flow paths specified by
  the **Negative spool position open connections**
  parameter to their maximum value. The flow paths specified by the
  **Positive spool position open connections**
  parameter are closed.
- `Maintain last value` — The valve
  freezes at the spool position when the trigger occurs.

Due to numerical smoothing at the extremes of the valve area, in the
linear parameterization, the minimum area that he block uses is larger than the
**Leakage area**, and the maximum is smaller than the
**Maximum orifice area**, in proportion to the
**Smoothing factor** value. For more information, see Numerical Smoothing.

After the fault triggers, the valve remains at the faulted area for the rest of the
simulation.

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
