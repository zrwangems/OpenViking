---
type: simulink-block
title: 'Nonlinear Translational Damper'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives / Springs & Dampers'
documentation_page: 'nonlineartranslationaldamper'
documentation_source_path: 'ref/nonlineartranslationaldamper.html'
language: en
---

# Nonlinear Translational Damper

## Ports
```yaml
ports:
- name: R
  summary: Shaft mechanical translational
  direction: conserving
- name: C
  summary: Case mechanical translational
  direction: conserving
```

### Conserving

### **R** — Shaft mechanical translational

Mechanical translational conserving port associated with the
shaft.

### **C** — Case mechanical translational

Mechanical translational conserving port associated with the
case.
## Parameters
```yaml
parameters:
- name: Parameterization
  summary: Option to parameterize damping By polynomial (default) | By table lookup
  group: ''
- name: Symmetry
  summary: Option to parameterize damping symmetry Symmetric (default) | Two-sided
  group: ''
- name: Vector of damping coefficients
  summary: Polynomial damping coefficients [10, 0, 1, 0, .1] N*s/m (default) | vector of length 5
  group: ''
- name: Vector of extension damping coefficients
  summary: Polynomial extension damping coefficients [10, 0, 1, 0, .1] N*s/m (default) | vector of length 5
  group: ''
- name: Vector of contraction damping coefficients
  summary: Polynomial contraction damping coefficients [100, -1, 10, 0, 0] N*s/m (default) | vector of length 5
  group: ''
- name: Velocity vector
  summary: Velocity [-1, -.5, -.3, -.1, .1, .3, .5, 1] m/s (default) | vector
  group: ''
- name: Force vector
  summary: Damping force [-100, -40, -20, -5, 5, 20, 40, 100] N (default) | vector
  group: ''
- name: Interpolation method
  summary: Method of interpolation between breakpoint values Linear (default) | Smooth
  group: ''
- name: Extrapolation method
  summary: Method of handling input values that fall outside range of breakpoint data set Linear (default) | Nearest | Error
  group: ''
```

### **Parameterization** — Option to parameterize damping `By polynomial` (default) | `By table lookup`

Whether to parameterize damping by polynomial or table lookup.

### **Symmetry** — Option to parameterize damping symmetry `Symmetric` (default) | `Two-sided`

Whether to use a symmetric or two-sided table lookup
parameterization.

### **Vector of damping coefficients** — Polynomial damping coefficients `[10, 0, 1, 0, .1]` `N*s/m` (default) | vector of length 5

Damping coefficients. Physical units apply to the first element.

#### Dependencies

To enable this parameter, set **Parameterization** to
`By polynomial` and
**Symmetry** to
`Symmetric`.

### **Vector of extension damping coefficients** — Polynomial extension damping coefficients `[10, 0, 1, 0, .1]` `N*s/m` (default) | vector of length 5

Extension damping coefficients. Physical units apply to the first
element.

#### Dependencies

To enable this parameter, set **Parameterization** to
`By polynomial` and
**Symmetry** to
`Two-sided`.

### **Vector of contraction damping coefficients** — Polynomial contraction damping coefficients `[100, -1, 10, 0, 0]` `N*s/m` (default) | vector of length 5

Contraction damping coefficients. Physical units apply to the first
element.

#### Dependencies

To enable this parameter, set **Parameterization** to
`By polynomial` and
**Symmetry** to
`Two-sided`.

### **Velocity vector** — Velocity `[-1, -.5, -.3, -.1, .1, .3, .5, 1]` `m/s` (default) | vector

Translational velocity. The vector requires a minimum number of elements
based on the interpolation method. When you set **Interpolation
method** to:

- `Linear`, the minimum is two.
- `Smooth`, the minimum is
  three.

The elements correspond one-to-one with the **Force
vector** parameter.

#### Dependencies

To enable this parameter, set **Parameterization** to
`By table lookup`.

### **Force vector** — Damping force `[-100, -40, -20, -5, 5, 20, 40, 100]` `N` (default) | vector

Damping force for a given translational velocity. The vector requires a
minimum number of elements based on the interpolation method. When you set
**Interpolation method** to:

- `Linear`, the minimum is two.
- `Smooth`, the minimum is
  three.

The elements correspond one-to-one with the
**Velocity vector** parameter.

#### Dependencies

To enable this parameter, set **Parameterization** to
`By table lookup`.

### **Interpolation method** — Method of interpolation between breakpoint values `Linear` (default) | `Smooth`

Method to use for lookup table breakpoint interpolation. The block uses
the `tablelookup` function to model nonlinearity by using
array data to map input values to output values:

- `Linear` — Select this option for the
  lowest computational cost.
- `Smooth` — Select this option to produce
  a continuous curve with continuous first-order derivatives.

For more information, see `tablelookup`.

#### Dependencies

To enable this parameter, set **Parameterization** to
`By table lookup`.

### **Extrapolation method** — Method of handling input values that fall outside range of breakpoint data set `Linear` (default) | `Nearest` | `Error`

Method to use for lookup table breakpoint extrapolation. This method
determines the output value when the input value is outside the range
specified in the argument list. The block uses the
`tablelookup` function to model nonlinearity by using
array data to map input values to output values:

- `Linear` — Select this option to
  produce a curve with continuous first-order derivatives in the
  extrapolation region and at the boundary with the interpolation
  region.
- `Nearest` — Select this option to
  produce an extrapolation that does not go above the highest
  point in the data or below the lowest point in the data.
- `Error` — Select this option to avoid
  extrapolating when you want your data to be within the table
  range. If the input signal is outside the range of the table,
  the simulation stops and generates an error.

#### Dependencies

To enable this parameter, set **Parameterization** to
`By table lookup`.
## Libraries

Simscape / Driveline / Couplings & Drives / Springs & Dampers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013a**

## Description

Nonlinear damper in a translational system

The Nonlinear Translational Damper block represents a
nonlinear translational damper. Polynomial and table lookup parameterizations define the
nonlinear relationship between damping force and relative linear velocity. The damping
force can be symmetric or asymmetric about the zero velocity point. The block applies
equal and opposite damping forces on the two translational conserving ports.

The symmetric polynomial parameterization defines the damping force for both positive
and negative relative velocities according to the expression:

F=b1v+sign(v)⋅b2v2+b3v3+sign(v)⋅b4v4+b5v5,

where:

- *F* — Damping force
- *b1*,
  *b2*,...,
  *b5* — Damping
  coefficients
- *v* — Relative linear velocity between ports
  **R** and **C**, v=vR−vC
- *vR* — Absolute linear velocity
  associated with port **R**
- *vC* — Absolute linear velocity
  associated with port **C**

To avoid zero-crossings that slow simulation, eliminate the sign function from the
polynomial expression by specifying an odd polynomial (*b2*,*b4*
= 0).

The two-sided polynomial parameterization defines the damping force for both positive
and negative relative velocities according to the expression:

F={b1ev+b2ev2+b3ev3+b4ev4+b5ev5,v≥0b1cv−b2cv2+b3cv3−b4cv4+b5cv5,v<0,

where:

- *b1e*,
  *b2e*, ...,
  *b5e* — Damping coefficients for
  positive relative velocities
- *b1c*,
  *b2c*, ...,
  *b5c* — Damping coefficients for
  negative relative velocities

Positive relative velocities correspond to damper extension when ports
**R** and **C** move apart. Negative relative
velocities correspond to damper contraction when ports **R** and
**C** move together.

Both polynomial parameterizations use a fifth-order polynomial expression. To use a
lower-order polynomial, set the unneeded higher-order coefficients to zero. For
polynomials of order greater than five, fit to a polynomial of order smaller than or
equal to five, or use the table lookup parameterization.

The table lookup parameterization defines damping force based on a set of velocity and
force vectors. If not included in the vectors, the block automatically adds a data point
at the origin, that is, the intersection of zero velocity and zero force.

### Assumptions and Limitations

The block assumes viscous damping. The damping force depends only on
velocity.
