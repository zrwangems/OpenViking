---
type: simulink-block
title: 'Nonlinear Rotational Damper'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives / Springs & Dampers'
documentation_page: 'nonlinearrotationaldamper'
documentation_source_path: 'ref/nonlinearrotationaldamper.html'
language: en
---

# Nonlinear Rotational Damper

## Ports

### Conserving

### **R** — Shaft mechanical translational

Mechanical translational conserving port associated with the
shaft.

### **C** — Case mechanical translational

Mechanical translational conserving port associated with the
case.

## Parameters

### **Parameterization** — Option to parameterize damping `By polynomial` (default) | `By table lookup`

Whether to parameterize damping by polynomial or table lookup.

### **Symmetry** — Option to parameterize damping symmetry `Symmetric` (default) | `Two-sided`

Whether to use a symmetric or two-sided table lookup
parameterization.

### **Vector of damping coefficients** — Polynomial damping coefficients `[.0001, 0, 1e-05, 0, 1e-06]` `N*m*s/rad` (default) | vector of length 5

Damping coefficients. Physical units apply to the first element.

### **Vector of positive rotation damping coefficients** — Polynomial positive rotation damping coefficients `[.0001, 0, 1e-05, 0, 1e-06]` `N*m*s/rad` (default) | vector of length 5

Positive rotation damping coefficients. Physical units apply to the first
element.

#### Dependencies

To enable this parameter, set **Parameterization** to
`By polynomial` and
**Symmetry** to
`Two-sided`.

### **Vector of negative rotation damping coefficients** — Polynomial negative rotation damping coefficients `[.001, -1e-05, .0001, 0, 0]` `N*m*s/rad` (default) | vector of length 5

Negative rotation damping coefficients. Physical units apply to the first
element.

#### Dependencies

To enable this parameter, set **Parameterization** to
`By polynomial` and
**Symmetry** to
`Two-sided`.

### **Angular velocity vector** — Angular velocity `[-1, -.5, -.3, -.1, .1, .3, .5, 1]` `rad/s` (default) | vector

Angular velocity. The vector requires a minimum number of elements based
on the interpolation method. When you set **Interpolation
method** to:

- `Linear`, the minimum is two.
- `Smooth`, the minimum is
  three.

The elements correspond one-to-one with the **Torque
vector** parameter.

#### Dependencies

To enable this parameter, set **Parameterization** to
`By table lookup`.

### **Torque vector** — Damping torque `[-.0001, -4e-05, -2e-05, -5e-06, 5e-06, 2e-05, 4e-05, .0001]` `N*m` (default)

Damping torque for a given angular velocity. The vector requires a minimum
number of elements based on the interpolation method. When you set
**Interpolation method** to:

- `Linear`, the minimum is two.
- `Smooth`, the minimum is
  three.

The elements correspond one-to-one with the **Angular
velocity vector** parameter.

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

Nonlinear damper in a rotational system

The Nonlinear Rotational Damper block represents a
nonlinear rotational damper. Polynomial and table lookup parameterizations define the
nonlinear relationship between damping torque and relative angular velocity. The damping
torque can be symmetric or asymmetric about the zero velocity point. The block applies
equal and opposite damping torques on the two rotational conserving ports.

The symmetric polynomial parameterization defines the damping torque for both positive
and negative relative velocities according to the expression:

T=b1ω+sign(ω)⋅b2ω2+b3ω3+sign(ω)⋅b4ω4+b5ω5,

where:

- *T* — Damping torque
- *b1*,
  *b2*, ...,
  *b5* — Damping
  coefficients
- *ω* — Relative angular velocity between ports
  **R** and **C**, ω=ωR−ωC
- *ωR* — Absolute angular velocity
  associated with port **R**
- *ωC* — Absolute angular velocity
  associated with port **C**

To avoid zero-crossings that slow simulation, eliminate the sign function
from the polynomial expression by specifying an odd polynomial (*b2*,*b4*
= 0).

The two-sided polynomial parameterization defines the damping torque for both positive
and negative relative velocities according to the expression:

T={b1pω+b2pω2+b3pω3+b4pω4+b5pω5,ω≥0b1nω+b2nω2+b3nω3+b4nω4+b5nω5,ω<0,

where:

- *b1p*,
  *b2p*, ...,
  *b5p* — Damping coefficients for
  positive relative velocities
- *b1n*,
  *b2n*, ...,
  *b5n* — Damping coefficients for
  negative relative velocities

Both polynomial parameterizations use a fifth-order polynomial expression. To use a
lower-order polynomial, set the unneeded higher-order coefficients to zero. To use a
higher-order polynomial, fit to a lower-order polynomial or use the table lookup
parameterization.

The table lookup parameterization defines damping torque based on a set of torque and
angular velocity vectors. If not specified, the block automatically adds a data point at
the origin, that is, the intersection of zero angular velocity and zero torque.

### Assumptions and Limitations

The block assumes viscous damping. The damping force depends only on
velocity.
