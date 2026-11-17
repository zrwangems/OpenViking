---
type: simulink-block
title: '3-Way Directional Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: '3waydirectionalvalvetl'
documentation_source_path: 'ref/3waydirectionalvalvetl.html'
language: en
---

# 3-Way Directional Valve (TL)

## Ports
```yaml
ports:
- name: S
  summary: Control member displacement physical signal
  direction: input
- name: P
  summary: Flow passage thermal liquid
  direction: conserving
- name: T
  summary: Flow passage thermal liquid
  direction: conserving
- name: A
  summary: Flow passage thermal liquid
  direction: conserving
```

### Input

### **S** — Control member displacement physical signal

Displacement of the valve control member, in m. This is equivalent to
the spool position.
### Conserving

### **P** — Flow passage thermal liquid

Opening through which the flow can enter or exit the valve. This port
is typically connected to a fluid supply line.

### **T** — Flow passage thermal liquid

Opening through which the flow can enter or exit the valve. This port
is typically connected to a fluid return line.

### **A** — Flow passage thermal liquid

Opening through which the flow can enter or exit the valve. This port
is typically connected to an actuation line.
## Parameters
```yaml
parameters:
- name: Positive spool position open connections
  summary: Flow paths open when the spool is in a positive position P-A (default) | All closed | P-A, A-T, P-T | P-T | A-T
  group: Model Parameterization
- name: Negative spool position open connections
  summary: Flow paths open when the spool moves in the negative direction A-T (default) | All closed | P-A, A-T, P-T | P-A
    | P-T
  group: Model Parameterization
- name: Area characteristics
  summary: Flow equations for orifices Identical for all flow paths (default) | Different for each flow path
  group: Model Parameterization
- name: Orifice parameterization
  summary: Method of calculating opening area Linear area vs. spool travel (default) | Tabulated data - Area vs. spool travel
    | Tabulated data - Volumetric flow rate vs. spool travel and pressure dropTabulated data - Mass flow rate vs. spool travel
    and pressure drop
  group: Model Parameterization
- name: Spool travel between closed and open orifice
  summary: Maximum spool stroke 5e-3 m (default) | positive scalar
  group: Model Parameterization
- name: Maximum orifice area
  summary: Maximum orifice opening area 1e-4 m^2 (default) | positive scalar
  group: Model Parameterization
- name: Spool travel vector
  summary: Vector of valve opening distance [0, .00125, .0025, .00375, .005]m (default) | 1-by*n* vector
  group: Model Parameterization
- name: Orifice area vector
  summary: Vector of valve opening areas [1e-10, 1e-05, 4e-05, 8e-05, .0001]m^2 (default) | 1-by*n* vector
  group: Model Parameterization
- name: Leakage area
  summary: Gap area when in fully closed position 1e-10 m^2 (default) | positive scalar
  group: Model Parameterization
- name: Smoothing factor
  summary: Numerical smoothing factor 0.01 (default) | positive scalar in the range [0,1]
  group: Model Parameterization
- name: Spool travel vector, ds
  summary: Vector of valve opening distances [0, .00125, .0025, .00375, .005] m (default) | 1-by-*n* vector
  group: Model Parameterization
- name: Pressure drop vector, dp
  summary: Vector of valve pressure drop values [-.1, .3, .5, .7] MPa (default) | 1-by-*n* vector
  group: Model Parameterization
- name: Volumetric flow rate table, q(ds,dp)
  summary: Array of volumetric flow rates [-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239;
    -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239] m^3/s (default)
    | *M*-by-*N* matrix
  group: Model Parameterization
- name: Reference inflow temperature
  summary: Temperature at which pressure-drop data is specified 293.15 K (default) | positive scalar
  group: Model Parameterization
- name: Reference inflow pressure
  summary: Pressure at which pressure-drop tabulated data is specified 0.101325 MPa (default) | positive scalar
  group: Model Parameterization
- name: Mass flow rate table, mdot(ds,dp)
  summary: Mass flow rate 1e3 * [-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362,
    .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239] kg/s (default) | M-by-N matrix
  group: Model Parameterization
- name: Discharge coefficient
  summary: Discharge coefficient 0.64 (default) | positive scalar
  group: Model Parameterization
- name: Critical Reynolds number
  summary: Upper Reynolds number limit for laminar flow 150 (default) | positive scalar
  group: Model Parameterization
- name: Pressure recovery
  summary: Whether to account for pressure increase in area expansions on (default) | off
  group: Model Parameterization
- name: Cross-sectional area at ports A, P and T
  summary: Area at valve entry or exit 0.01 m^2 (default) | positive scalar
  group: Model Parameterization
- name: Spool position at maximum P-A orifice area
  summary: Spool offset at maximum area between ports P and A 4.5e-3 m (default) | scalar
  group: P-A Orifice
- name: P-A spool travel between closed and open orifice
  summary: Maximum stroke for the spool between ports P and A 0.005 m (default) | positive scalar
  group: P-A Orifice
- name: P-A maximum orifice area
  summary: Maximum area between ports P and A 1e-4 m^2 (default) | positive scalar
  group: P-A Orifice
- name: P-A orifice spool travel vector
  summary: Vector of valve opening distance [0, .00125, .0025, .00375, .005] m (default) | 1-by*n* vector
  group: P-A Orifice
- name: P-A orifice area vector
  summary: Vector of valve opening areas [1e-10, 1e-05, 4e-05, 8e-05, .0001] m^2 (default) | 1-by-*n* vector
  group: P-A Orifice
- name: P-A orifice spool travel vector, ds
  summary: Vector of valve opening distances [0, .00125, .0025, .00375, .005] m (default) | 1-by-*n* vector
  group: P-A Orifice
- name: P-A orifice pressure drop vector, dp
  summary: Vector of pressure drop values over the valve [-.1, .3, .5, .7] MPa (default) | 1-by-*n* vector
  group: P-A Orifice
- name: P-A orifice (ds,dp)
  summary: Vector of valve volumetric flow rates [-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239;
    -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239] m^3/s (default)
    | *M*-by-*N* matrix
  group: P-A Orifice
- name: P-A orifice mass flow rate table, mdot(ds,dp)
  summary: Vector of valve mass flow rates 1e3 * [-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239;
    -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239] kg/s (default) |
    *M*-by-*N* matrix
  group: P-A Orifice
- name: Spool position at maximum A-T orifice area
  summary: Spool offset at maximum area between ports A and T -4.5e-3 m (default) | scalar
  group: A-T Orifice
- name: A-T spool travel between closed and open orifice
  summary: Maximum stroke for the spool between ports A and T 0.005 m (default) | positive scalar
  group: A-T Orifice
- name: A-T maximum orifice area
  summary: Maximum area between ports A and T 1e-4 m^2 (default) | positive scalar
  group: A-T Orifice
- name: A-T orifice spool travel vector
  summary: Vector of valve opening distances [0, .00125, .0025, .00375, .005] m (default) | 1-by-*n* vector
  group: A-T Orifice
- name: A-T orifice area vector
  summary: Vector of valve opening areas [1e-10, 1e-05, 4e-05, 8e-05, .0001] m^2 (default) | 1-by-*n* vector
  group: A-T Orifice
- name: A-T orifice spool travel vector, ds
  summary: Vector of valve opening distances [0, .00125, .0025, .00375, .005] m (default) | 1-by-*n* vector
  group: A-T Orifice
- name: A-T orifice pressure drop vector, dp
  summary: Vector of pressure drop values over the valve [-.1, .3, .5, .7] MPa (default) | 1-by-*n* vector
  group: A-T Orifice
- name: A-T orifice volumetric flow rate table, q(ds,dp)
  summary: Vector of volumetric flow rate for tabular parameterization - different flow paths [-9.05e-10, 1.57e-09, 2.02e-09,
    2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192;
    -.000905, .00156, .002, .00239] m^3/s (default) | *M*-by-*N* matrix
  group: A-T Orifice
- name: A-T orifice mass flow rate table, mdot(ds,dp)
  summary: Vector of mass flow rate for tabular parameterization - different flow paths 1e3 * [-9.05e-10, 1.57e-09, 2.02e-09,
    2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192;
    -.000905, .00156, .002, .00239] kg/s (default) | *M*-by-*N* matrix
  group: A-T Orifice
- name: Spool position at maximum P-T orifice area
  summary: Spool offset at maximum area between ports P and T 4.5e-3 m (default) | scalar
  group: P-T Orifice
- name: P-T spool travel between closed and open orifice
  summary: Maximum stroke for the spool between ports P and T 0.005 m (default) | positive scalar
  group: P-T Orifice
- name: P-T maximum orifice area
  summary: Maximum area between ports P and T 1e-4 m^2 (default) | positive scalar
  group: P-T Orifice
- name: P-T orifice spool travel vector
  summary: Vector of valve opening distances [0, .00125, .0025, .00375, .005] m (default) | 1-by-*n* vector
  group: P-T Orifice
- name: P-T orifice area vector
  summary: Vector of valve opening areas [1e-10, 1e-05, 4e-05, 8e-05, .0001] m^2 (default) | 1-by-*n* vector
  group: P-T Orifice
- name: P-T orifice spool travel vector, ds
  summary: Vector of valve opening distances [0, .00125, .0025, .00375, .005] m (default) | 1-by-*n* vector
  group: P-T Orifice
- name: P-T orifice pressure drop vector, dp
  summary: Vector of pressure drop values over the valve [-.1, .3, .5, .7] MPa (default) | 1-by-*n* vector
  group: P-T Orifice
- name: P-T orifice volumetric flow rate table, q(ds,dp)
  summary: Vector of volumetric flow rate for tabular parameterization - different flow paths [-9.05e-10, 1.57e-09, 2.02e-09,
    2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192;
    -.000905, .00156, .002, .00239] m^3/s (default) | *M*-by-*N* matrix
  group: P-T Orifice
- name: P-T orifice mass flow rate table, mdot(ds,dp)
  summary: Vector of mass flow rate for tabular parameterization - different flow paths 1e3 * [-9.05e-10, 1.57e-09, 2.02e-09,
    2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192;
    -.000905, .00156, .002, .00239] kg/s (default)
  group: P-T Orifice
- name: 3-Way Directional Valve Area fault
  summary: Option to model valve area fault Add fault
  group: Faults
- name: Spool position when faulted
  summary: Faulted valve characteristics Positive (default) | Negative | Maintain last value
  group: Faults
```

### Model Parameterization

### **Positive spool position open connections** — Flow paths open when the spool is in a positive position `P-A` (default) | `All closed` | `P-A, A-T, P-T` | `P-T` | `A-T`

Flow paths open when the spool is in a positive position. This
parameter sets the valve configuration and defines the direction of
spool movement according to the signal received at port
**S**.

### **Negative spool position open connections** — Flow paths open when the spool moves in the negative direction `A-T` (default) | `All closed` | `P-A, A-T, P-T` | `P-A` | `P-T`

Flow paths open when the spool moves in the negative direction. This
parameter sets the valve configuration and defines the direction of
spool movement according to the signal received at port
**S**.

### **Area characteristics** — Flow equations for orifices `Identical for all flow paths` (default) | `Different for each flow path`

Applies uniform or individual flow equations for the valve orifice
area. `Identical for all flow paths` uses the
same orifice and spool geometries, flow rates, pressure, and area
vectors for all valve orifices. When using `Different for
each flow path`, the spool offsets and tabulated data
are assigned to the orifices between ports **P** and
**A**, ports **A** and
**T**, and ports **P** and
**T**. In both cases, ports **A**,
**P**, and **T** have the same
cross-sectional areas, discharge coefficients, and Reynolds numbers. The
same **Orifice parameterization** is also applied to
all flow paths.

### **Orifice parameterization** — Method of calculating opening area `Linear area vs. spool travel` (default) | `Tabulated data - Area vs. spool travel` | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop``Tabulated data - Mass flow rate vs. spool travel and pressure drop`

Method of calculating the valve opening area. In the tabulated data
parameterizations, you can provide your own valve area and spool travel
data for nonlinear valve opening profiles, or you can provide data in
terms of volumetric flow rate, spool travel, and pressure drop over the
flow path. The thermal liquid domain allows you to parameterize the
orifice using tabulated mass flow rate data.

### **Spool travel between closed and open orifice** — Maximum spool stroke `5e-3 m` (default) | positive scalar

Maximum distance of spool travel. This value provides an upper limit
to calculations so that simulations do not return unphysical
values.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths`.

### **Maximum orifice area** — Maximum orifice opening area `1e-4 m^2` (default) | positive scalar

Largest open area during operation of valve.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths`.

### **Spool travel vector** — Vector of valve opening distance `[0, .00125, .0025, .00375, .005]`m (default) | 1-by*n* vector

Vector of control member travel distances for the tabular
parameterization of valve area. The vector elements must correspond
one-to-one with the elements in the **Orifice area
vector** parameter. The values are listed in ascending
order and the first element must be 0. Linear interpolation is employed
between table data points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Tabulated data -
Area vs. spool travel`.

### **Orifice area vector** — Vector of valve opening areas `[1e-10, 1e-05, 4e-05, 8e-05, .0001]`m^2 (default) | 1-by*n* vector

Vector of opening areas for the tabular parameterization of valve
opening area. The vector elements must correspond one-to-one with the
elements in the **Spool travel vector** parameter. The
elements are listed in ascending order and must be greater than
0.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Opening
parameterization** to `Tabulated data -
Area vs. spool travel`.

### **Leakage area** — Gap area when in fully closed position `1e-10 m^2` (default) | positive scalar

Sum of all gaps when the valve is in its fully closed position. Any
area smaller than this value is maintained at the specified leakage
area. This contributes to numerical stability by maintaining continuity
in the flow.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Linear - area vs.
spool travel`.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change
based to the flow response when the valve is in near-open and
near-closed positions. To increase the stability of your simulation in
these regimes, set this parameter to a nonzero value less than
one.

### **Spool travel vector, ds** — Vector of valve opening distances `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of control member travel distances for tabular parameterization
of volumetric flow rate. The spool travel vector forms an independent
axis with the **Pressure drop vector, dp** parameter
for the 3-D dependent **Volumetric flow rate table,
q(ds,dp)** or **Mass flow rate table,
mdot(ds,dp)** parameters. A positive displacement
corresponds to valve opening. The values are listed in ascending order
and the first element must be 0. Linear interpolation is employed
between table data points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Volumetric flow rate
vs. spool travel and pressure drop` or
`Tabulated data - Mass flow rate vs. spool travel
and pressure drop`.

### **Pressure drop vector, dp** — Vector of valve pressure drop values `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure drop values for tabular parameterization of
volumetric flow rate. The pressure drop vector forms an independent axis
with the **Spool travel vector, s** parameter for the
3-D dependent **Volumetric flow rate table, q(ds,dp)**
or **Mass flow rate table, mdot(ds,dp)** parameters.
The values are listed in ascending order and must be greater than 0.
Linear interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Volumetric flow rate
vs. spool travel and pressure drop` or
`Tabulated data - Mass flow rate vs. spool travel
and pressure drop`.

### **Volumetric flow rate table, q(ds,dp)** — Array of volumetric flow rates `[-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239] m^3/s` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of volumetric flow
rates based on independent values of pressure drop and spool travel
distance. *M* and *N* are the sizes of
the corresponding vectors:

- *M* is the number of elements in the
  **Spool travel vector, ds**
  parameter.
- *N* is the number of elements in the
  **Pressure drop vector, dp**
  parameter.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`.

### **Reference inflow temperature** — Temperature at which pressure-drop data is specified `293.15 K` (default) | positive scalar

Temperature at which the tabulated pressure-drop data is
specified.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Tabulated data -
Mass flow rate vs. spool travel and pressure
drop`.

### **Reference inflow pressure** — Pressure at which pressure-drop tabulated data is specified `0.101325 MPa` (default) | positive scalar

Pressure at which the tabulated pressure-drop data is specified. The
block uses this parameter to calculate a third reference parameter, the
reference density. The reference that it uses to scale the tabulated
pressure drop data for pressures and temperatures deviating from the
reference conditions.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Tabulated data -
Mass flow rate vs. spool travel and pressure
drop`.

### **Mass flow rate table, mdot(ds,dp)** — Mass flow rate `1e3 * [-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239] kg/s` (default) | M-by-N matrix

Mass flow rate for *M* given control member positions
and *N* given pressure drops over the orifice. The
control member position represents a spool or other mechanism that
controls the opening area.

#### Dependencies

To enable this parameter, set **Orifice
parameterization** to `Tabulated data -
Mass flow rate vs. spool travel and pressure
drop`.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor that accounts for discharge losses in theoretical
flows.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the valve.

### **Pressure recovery** — Whether to account for pressure increase in area expansions `on` (default) | `off`

Select to account for pressure increase when fluid flows from a region
of a smaller cross-sectional area to a region of larger cross-sectional
area.

### **Cross-sectional area at ports A, P and T** — Area at valve entry or exit `0.01 m^2` (default) | positive scalar

Cross-sectional area at the entry and exit ports
**A**, **P**, and
**T**. These areas are used in the pressure-flow
rate equation that determines volumetric flow rate through the
valve.

### P-A Orifice

### **Spool position at maximum P-A orifice area** — Spool offset at maximum area between ports P and A `4.5e-3 m` (default) | scalar

Initial orifice opening distance between ports **P**
and **A**. The default represents a underlapped
system.

- If the magnitude of **Spool position at maximum
  orifice area** is less than the value of
  **Spool travel between closed and open
  orifice**, the orifice is underlapped, or
  partially open when the spool position equals 0 m.
- If the magnitude of **Spool position at maximum
  orifice area** is greater than the value of
  **Spool travel between closed and open
  orifice**, the orifice is overlapped. This
  means the valve remains closed over a range of spool
  positions.
- If the magnitude of **Spool position at maximum
  orifice area** is equal to the value of
  **Spool travel between closed and open
  orifice**, the orifice is zero-lapped. This
  means the valve is closed when the spool position equals 0
  and begins to open as soon as the spool position changes.

### **P-A spool travel between closed and open orifice** — Maximum stroke for the spool between ports P and A `0.005 m` (default) | positive scalar

Maximum distance of spool travel for the orifice between ports
**P** and **A**. This value
provides an upper limit to calculations so that simulations do not
return unphysical values.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path`.

### **P-A maximum orifice area** — Maximum area between ports P and A `1e-4 m^2` (default) | positive scalar

Cross-sectional area of the orifice between ports
**P** and **A** in its fully open
position.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Orifice
parameterization** to `Linear - area vs.
spool travel`.

### **P-A orifice spool travel vector** — Vector of valve opening distance `[0, .00125, .0025, .00375, .005] m` (default) | 1-by*n* vector

Vector of control member travel distances for the tabular
parameterization of valve area. The vector elements must correspond
one-to-one with the elements in the **P-A orifice area
vector** parameter. The values are listed in ascending
order and the first element must be 0. Linear interpolation is employed
between table data points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Orifice
parameterization** to `Tabulated data -
Area vs. spool travel`.

### **P-A orifice area vector** — Vector of valve opening areas `[1e-10, 1e-05, 4e-05, 8e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of opening areas for the tabular parameterization of valve
opening area. The vector elements must correspond one-to-one with the
elements in the **P-A orifice spool travel vector**
parameter. The elements are listed in ascending order and must be
greater than 0.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Opening
parameterization** to `Tabulated data -
Area vs. spool travel`.

### **P-A orifice spool travel vector, ds** — Vector of valve opening distances `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of control member travel distances for tabular parameterization
of volumetric flow rate. The spool travel vector forms an independent
axis with the **P-A orifice pressure drop vector, dp**
parameter for the 3-D dependent **P-A orifice volumetric flow
rate table, q(s,dp)** or **Mass flow rate table,
mdot(ds,dp)** parameters. A positive displacement
corresponds to valve opening. The values are listed in ascending order
and the first element must be 0. Linear interpolation is employed
between table data points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Volumetric flow rate
vs. spool travel and pressure drop` or
`Tabulated data - Mass flow rate vs. spool travel
and pressure drop`.

### **P-A orifice pressure drop vector, dp** — Vector of pressure drop values over the valve `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure drop values for tabular parameterization of
volumetric flow rate. The pressure drop vector forms an independent axis
with the **P-A orifice spool travel vector, s**
parameter for the 3-D dependent **P-A orifice volumetric flow
rate table, q(s,dp)** or **Mass flow rate table,
mdot(ds,dp)** parameters. The values are listed in
ascending order and must be greater than 0. Linear interpolation is
employed between table data points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Volumetric flow rate
vs. spool travel and pressure drop` or
`Tabulated data - Mass flow rate vs. spool travel
and pressure drop`.

### **P-A orifice (ds,dp)** — Vector of valve volumetric flow rates `[-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239] m^3/s` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of volumetric flow
rates based on independent values of pressure drop and spool travel
distance. *M* and *N* are the sizes of
the corresponding vectors:

- *M* is the number of elements in the
  **P-A orifice spool travel vector,
  ds** parameter.
- *N* is the number of elements in the
  **P-A orifice pressure drop vector,
  dp** parameter.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Orifice
parameterization** to `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`.

### **P-A orifice mass flow rate table, mdot(ds,dp)** — Vector of valve mass flow rates `1e3 * [-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239] kg/s` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of mass flow rates
based on independent values of pressure drop and spool travel distance.
*M* and *N* are the sizes of the
corresponding vectors:

- *M* is the number of elements in the
  **P-A orifice spool travel vector,
  ds** parameter.
- *N* is the number of elements in the
  **P-A orifice pressure drop vector,
  dp** parameter.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Orifice
parameterization** to `Tabulated data -
Mass flow rate vs. spool travel and pressure
drop`.

### A-T Orifice

### **Spool position at maximum A-T orifice area** — Spool offset at maximum area between ports A and T `-4.5e-3 m` (default) | scalar

Initial orifice opening distance between ports **A**
and **T**. The default represents a underlapped
system.

- If the magnitude of **Spool position at maximum
  orifice area** is less than the value of
  **Spool travel between closed and open
  orifice**, the orifice is underlapped, or
  partially open when the spool position equals 0 m.
- If the magnitude of **Spool position at maximum
  orifice area** is greater than the value of
  **Spool travel between closed and open
  orifice**, the orifice is overlapped. This
  means the valve remains closed over a range of spool
  positions.
- If the magnitude of **Spool position at maximum
  orifice area** is equal to the value of
  **Spool travel between closed and open
  orifice**, the orifice is zero-lapped. This
  means the valve is closed when the spool position equals 0
  and begins to open as soon as the spool position changes.

### **A-T spool travel between closed and open orifice** — Maximum stroke for the spool between ports A and T `0.005 m` (default) | positive scalar

Maximum distance of spool travel for the orifice between ports
**A** and **T**. This value
provides an upper limit to calculations so that simulations do not
return unphysical values.

#### Dependencies

To enable this parameter, set **Area
characteristics** type to `Different for
each flow path`.

### **A-T maximum orifice area** — Maximum area between ports A and T `1e-4 m^2` (default) | positive scalar

Cross-sectional area of the orifice between ports
**A** and **T** in its fully open
position.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Orifice
parameterization** to `Linear - area vs.
spool travel`.

### **A-T orifice spool travel vector** — Vector of valve opening distances `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of control member travel distances for the tabular
parameterization of valve area. The vector elements must correspond
one-to-one with the elements in the **A-T orifice area
vector** parameter. The values are listed in ascending
order and the first element must be 0. Linear interpolation is employed
between table data points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Orifice
parameterization** to `Tabulated data -
Area vs. spool travel`.

### **A-T orifice area vector** — Vector of valve opening areas `[1e-10, 1e-05, 4e-05, 8e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of opening areas for the tabular parameterization of valve
opening area. The vector elements must correspond one-to-one with the
elements in the **A-T orifice spool travel vector**
parameter. The elements are listed in ascending order and must be
greater than 0.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Opening
parameterization** to `Tabulated data -
Area vs. spool travel`.

### **A-T orifice spool travel vector, ds** — Vector of valve opening distances `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of control member travel distances for tabular parameterization
of volumetric flow rate. The spool travel vector forms an independent
axis with the **A-T orifice pressure drop vector, dp**
parameter for the 3-D dependent **A-T orifice (ds,dp)**
or **Mass flow rate table, mdot(ds,dp)** parameters. A
positive displacement corresponds to valve opening. The values are
listed in ascending order and the first element must be 0. Linear
interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Volumetric flow rate
vs. spool travel and pressure drop` or
`Tabulated data - Mass flow rate vs. spool travel
and pressure drop`.

### **A-T orifice pressure drop vector, dp** — Vector of pressure drop values over the valve `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure drop values for tabular parameterization of
volumetric flow rate. The pressure drop vector forms an independent axis
with the **A-T orifice spool travel vector, s**
parameter for the 3-D dependent **A-T orifice (ds,dp)**
or **Mass flow rate table, mdot(ds,dp)** parameters.
The values are listed in ascending order and must be greater than 0.
Linear interpolation is employed between table data points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Volumetric flow rate
vs. spool travel and pressure drop` or
`Tabulated data - Mass flow rate vs. spool travel
and pressure drop`.

### **A-T orifice volumetric flow rate table, q(ds,dp)** — Vector of volumetric flow rate for tabular parameterization - different flow paths `[-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239] m^3/s` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of volumetric flow
rates based on independent values of pressure drop and spool travel
distance. *M* and *N* are the sizes of
the corresponding vectors:

- *M* is the number of elements in the
  **A-T orifice spool travel vector,
  ds** parameter.
- *N* is the number of elements in the
  **A-T orifice pressure drop vector,
  dp** parameter.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Orifice
parameterization** to `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`.

### **A-T orifice mass flow rate table, mdot(ds,dp)** — Vector of mass flow rate for tabular parameterization - different flow paths `1e3 * [-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239] kg/s` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of mass flow rates
based on independent values of pressure drop and spool travel distance.
*M* and *N* are the sizes of the
corresponding vectors:

- *M* is the number of elements in the
  **A-T orifice spool travel vector,
  ds** parameter.
- *N* is the number of elements in the
  **A-T orifice pressure drop vector,
  dp** parameter.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Orifice
parameterization** to `Tabulated data -
Mass flow rate vs. spool travel and pressure
drop`.

### P-T Orifice

### **Spool position at maximum P-T orifice area** — Spool offset at maximum area between ports P and T `4.5e-3 m` (default) | scalar

Initial orifice opening distance between ports **P**
and **T**. The default represents a underlapped
system.

- If the magnitude of **Spool position at maximum
  orifice area** is less than the value of
  **Spool travel between closed and open
  orifice**, the orifice is underlapped, or
  partially open when the spool position equals 0 m.
- If the magnitude of **Spool position at maximum
  orifice area** is greater than the value of
  **Spool travel between closed and open
  orifice**, the orifice is overlapped. This
  means the valve remains closed over a range of spool
  positions.
- If the magnitude of **Spool position at maximum
  orifice area** is equal to the value of
  **Spool travel between closed and open
  orifice**, the orifice is zero-lapped. This
  means the valve is closed when the spool position equals 0
  and begins to open as soon as the spool position changes.

### **P-T spool travel between closed and open orifice** — Maximum stroke for the spool between ports P and T `0.005 m` (default) | positive scalar

Maximum distance of spool travel for the orifice between ports
**P** and **T**. This value
provides an upper limit to calculations so that simulations do not
return unphysical values.

#### Dependencies

To enable this parameter, set **Area
characteristics** type to `Different for
each flow path`.

### **P-T maximum orifice area** — Maximum area between ports P and T `1e-4 m^2` (default) | positive scalar

Cross-sectional area of the orifice between ports
**P** and **T** in its fully open
position.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Orifice
parameterization** to `Linear - area vs.
spool travel`.

### **P-T orifice spool travel vector** — Vector of valve opening distances `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of control member travel distances for the tabular
parameterization of valve area. The vector elements must correspond
one-to-one with the elements in the **P-T orifice area
vector** parameter. The values are listed in ascending
order and the first element must be 0. Linear interpolation is employed
between table data points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Orifice
parameterization** to `Tabulated data -
Area vs. spool travel`.

### **P-T orifice area vector** — Vector of valve opening areas `[1e-10, 1e-05, 4e-05, 8e-05, .0001] m^2` (default) | 1-by-*n* vector

Vector of opening areas for the tabular parameterization of valve
opening area. The vector elements must correspond one-to-one with the
elements in the **P-T orifice spool travel vector**
parameter. The elements are listed in ascending order and must be
greater than 0.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Opening
parameterization** to `Tabulated data -
Area vs. spool travel`.

### **P-T orifice spool travel vector, ds** — Vector of valve opening distances `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

Vector of control member travel distances for tabular parameterization
of volumetric flow rate. The spool travel vector forms an independent
axis with the **P-T orifice pressure drop vector, dp**
parameter for the 3-D dependent **P-T orifice volumetric flow
rate table, q(ds,dp)** or **Mass flow rate table,
mdot(ds,dp)** parameters. A positive displacement
corresponds to valve opening. The values are listed in ascending order
and the first element must be 0. Linear interpolation is employed
between table data points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Volumetric flow rate
vs. spool travel and pressure drop` or
`Tabulated data - Mass flow rate vs. spool travel
and pressure drop`.

### **P-T orifice pressure drop vector, dp** — Vector of pressure drop values over the valve `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

Vector of pressure drop values for tabular parameterization of
volumetric flow rate. The pressure drop vector forms an independent axis
with the **P-T orifice spool travel vector, ds**
parameter for the 3-D dependent **P-T orifice volumetric flow
rate table, q(ds,dp)** or **Mass flow rate table,
mdot(ds,dp)** parameters. The values are listed in
ascending order and must be greater than 0. Linear interpolation is
employed between table data points.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Identical for all
flow paths` and **Orifice
parameterization** to `Volumetric flow rate
vs. spool travel and pressure drop` or
`Tabulated data - Mass flow rate vs. spool travel
and pressure drop`.

### **P-T orifice volumetric flow rate table, q(ds,dp)** — Vector of volumetric flow rate for tabular parameterization - different flow paths `[-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239] m^3/s` (default) | *M*-by-*N* matrix

*M*-by-*N* matrix of volumetric flow
rates based on independent values of pressure drop and spool travel
distance. *M* and *N* are the sizes of
the corresponding vectors:

- *M* is the number of elements in the
  **P-T orifice spool travel vector,
  ds** parameter.
- *N* is the number of elements in the
  **P-T orifice pressure drop vector,
  dp** parameter.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Orifice
parameterization** to `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`.

### **P-T orifice mass flow rate table, mdot(ds,dp)** — Vector of mass flow rate for tabular parameterization - different flow paths `1e3 * [-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239] kg/s` (default)

*M*-by-*N* matrix of mass flow rates
based on independent values of pressure drop and spool travel distance.
*M* and *N* are the sizes of the
corresponding vectors:

- *M* is the number of elements in the
  **P-T orifice spool travel vector,
  ds** parameter.
- *N* is the number of elements in the
  **P-T orifice pressure drop vector,
  dp** parameter.

#### Dependencies

To enable this parameter, set **Area
characteristics** to `Different for each
flow path` and **Orifice
parameterization** to `Tabulated data -
Mass flow rate vs. spool travel and pressure
drop`.

### Faults

### **3-Way Directional Valve Area fault** — Option to model valve area fault `Add fault`

Option to model a valve area fault in the block. To add a fault, click
the **Add fault** hyperlink. When a fault occurs, the
valve area normally set by the opening parameterization is set based the
value specified in the **Spool position when faulted**
parameter.

### **Spool position when faulted** — Faulted valve characteristics `Positive` (default) | `Negative` | `Maintain last value`

Faulted valve spool position. You can choose for the valve to seize
when the spool is in the positive position, negative position, or at the
position when the fault triggers.

#### Dependencies

To enable this parameter, click the **Add
fault** hyperlink.
## Libraries

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Directional Control Valves

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

### R2024b: Model faults with the Simscape faults interface

The 3-Way Directional Valve (TL) block now supports the Simscape™ faults interface. To learn more, see Introduction to Simscape Faults.

### R2022b: Right-click blocks to view opening characteristic plots

You can view the plot of the area or volumetric flow rate with respect to spool
position for each orifice by right-clicking the block and selecting **Fluids** > **Plot Valve Characteristics**.

## Description

3-position directional valve in a thermal liquid network

The 3-Way Directional Valve (TL) block represents a
valve with three openings in a thermal liquid network, typically between an actuator,
pump, and tank. The valve operation is controlled by a single spool displaced according
to the signal at port **S**. You can set the baseline configuration of
your valve by specifying the orifices that are open when the spool moves in the positive
direction and negative directions in the **Positive spool position open
connections** and **Negative spool position open
connections** parameters, respectively.

You can set the model for valve opening in the **Orifice
parameterization** parameter as a linear relationship or function of
user-provided data, which can be applied to one or all flow paths in the valve.

Diagram of example valve configuration

In this configuration, **Positive spool position open connections**
is set to `A-T`. When the signal at port **S**
moves the spool to a positive position, the path between ports **A**
and **T** is open to flow. The paths between ports
**P** and **A** and between ports
**P** and **T** are closed:

Diagram showing flow between ports A and T with port P closed off

In this configuration, **Negative spool position open connections**
is set to `P-A`. When the signal at port **S**
moves the spool to a negative position, the path between ports **P**
and **A** is open to flow and the paths between ports
**T** and **A** and between ports
**P** and **T** are closed:

Diagram showing flow between ports A and P with port T closed off

You can open the path between ports **P** and **T**
by setting either **Positive spool position open connections** or
**Negative spool position open connections** to
`P-T` or `P-A, A-T, P-T`.

A flow path can be open in either the positive or negative spool positions, but not
both.

### Valve Orifice Parameterizations

The **Orifice parameterization** sets the method for calculating
the valve open area. The calculations are based either on the orifice parameters or
tabulated data sets specified in the **Model Parameterization**
tab. The block uses the same data for all flow paths if **Area
characteristics** is set to `Identical for all flow
paths`; otherwise, individual values are applied in the
`Different for all flow paths` setting. The orifice
parameterizations are:

- `Linear - area vs. spool travel`

  The opening area is a linear function of the spool travel distance and
  the signal received at port **S**:

  Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak,

  where:

  - *A*max is the
    **Maximum orifice area**.
  - *A*leak is the
    **Leakage area**.
  - *ΔS*max is the
    **Spool travel between closed and open
    orifice**.
  - *ΔS* is the spool travel distance. For flow
    paths that are open in the positive position:

    ΔS=Sorifice\_max−ΔSmax+S,

    and for flow paths that are open in the
    negative position:

    ΔS=Sorifice\_max+ΔSmax−S,

    where
    *Sorifice\_max*
    is the **Spool position at maximum orifice
    area**.

  When the valve is in a near-open or near-closed position in the
  linear parameterization, you can maintain numerical robustness in your simulation by adjusting
  the **Smoothing factor** parameter. If the **Smoothing
  factor** parameter is nonzero, the block smoothly saturates the opening area
  between *Aleak* and
  *Amax*. For more information, see Numerical Smoothing.
- `Tabulated data - Area vs. spool travel`

  Provide spool travel vectors for your system or for individual flow paths
  between ports **P** and **A**,
  **A** and **T**, and
  **P** and **T**. This data will be
  used to calculate the relationship between the orifice opening area and
  spool travel distance. Interpolation is used to determine the opening area
  between given data points. *A*leak
  and *A*max are the first and last
  parameters of the **Opening area vector**, respectively.
- `Tabulated data - Volumetric flow rate vs. spool travel and
  pressure drop`

  Provide spool travel and pressure drop vectors. The volumetric flow rate
  is calculated based on the relationship between pressure change and the
  spool travel distance. Interpolation is used to determine flow rate between
  given data points. The mass flow rate is the product of the volumetric flow
  rate and the local density.

  When you set **Orifice parameterization** to
  `Tabulated data - Mass flow rate vs. spool travel and
  pressure drop` the block calculates the mass flow rate
  directly from the control member position and the pressure drop across the
  valve. The relationship between the three variables can be nonlinear and it
  is given by the tabulated data in the **Spool travel vector,
  ds**, **Pressure drop vector, dp**, and
  **Mass flow rate table, mdot(ds,dp)**
  parameters.

### Visualize Orifice Openings

To visualize spool offsets and displacement, right-click the block and select **Fluids** > **Plot Valve Characteristics**. The plot shows the orifices selected in the **Valve
Configuration** settings. The parameterization selection sets the
axes, which are either:

- Orifice area versus spool position
- Volumetric flow rate versus spool position, queried at a specific
  pressure differential
- Mass flow rate versus spool position for the reference inflow
  temperature and reference inflow pressure, queried at a specific
  pressure differential

To update the data after changing the block parameters, click **Reload
Data** on the figure window.

This image shows an example valve configuration. In the **Valve
Configuration** settings:

- **Positive spool position open connections** is
  `P-A`.
- **Negative spool position open connections** is
  `A-T`.

All other spool positions are at the default values.

Plot of area versus spool position for each orifice.

### Faults

To model a fault, in the **Faults** section,
click the **Add fault** hyperlink next to the fault that you want to model. Use
the fault parameters to specify the fault properties. For more information about fault modeling,
see Introduction to Simscape Faults.

The **Spool position when faulted** parameter has three fault options:

- `Positive` — The spool position
  freezes in the positive position, and the flow paths specified by the
  **Positive spool position open connections**
  parameter open to their maximum value. The flow paths specified by the
  **Negative spool position open connections**
  parameter are closed.
- `Negative` — The spool position
  freezes in the positive position, and the flow paths specified by the
  **Negative spool position open connections**
  parameter open to their maximum value. The flow paths specified by the
  **Positive spool position open connections**
  parameter are closed.
- `Maintain last value` — The valve
  freezes at the spool position when the trigger occurs.

Due to numerical smoothing at the extremes of the valve area, in the
linear parameterization, the minimum area that he block uses is larger than the
**Leakage area**, and the maximum is smaller than the
**Maximum orifice area**, in proportion to the
**Smoothing factor** value. For more information, see Numerical Smoothing.

After the fault triggers, the valve remains at the faulted area for the rest of
the simulation.

### Assumptions

- Fluid inertia is ignored.
- Spool loading due to inertial, spring, and other forces is ignored.
- All valve orifices are assumed to be identical in size unless otherwise
  specified.
