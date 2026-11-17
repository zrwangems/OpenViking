---
type: simulink-block
title: 'Nonlinear Translational Spring'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives / Springs & Dampers'
documentation_page: 'nonlineartranslationalspring'
documentation_source_path: 'ref/nonlineartranslationalspring.html'
language: en
---

# Nonlinear Translational Spring

## Ports
```yaml
ports:
- name: C
  summary: Follower port mechanical rotational
  direction: conserving
- name: R
  summary: Base port mechanical rotational
  direction: conserving
```

### Conserving

### **C** — Follower port mechanical rotational

Mechanical rotational conserving port associated with the follower
end.

### **R** — Base port mechanical rotational

Mechanical rotational conserving port associated with the base
end.
## Parameters
```yaml
parameters:
- name: Parameterization
  summary: Method to characterize spring behavior By polynomial (default) | By table lookup
  group: ''
- name: Symmetry
  summary: Spring behavior versus zero deformation position Symmetric (default) | Two-sided
  group: ''
- name: Vector of spring coefficients
  summary: Symmetric deformation polynomial coefficients [100, 0, 10, 0, 1] N/m (default) | vector
  group: ''
- name: Vector of spring tension coefficients
  summary: Positive two-sided deformation polynomial coefficients [100, 0, 10, 0, 1] N/m (default)
  group: ''
- name: Vector of spring compression coefficients
  summary: Negative two-sided deformation polynomial coefficients [1000, -10, 100, 0, 0] N/m (default)
  group: ''
- name: Deformation vector
  summary: Deformation due to force table lookup entry [-1, -.5, -.3, -.1, .1, .3, .5, 1] (default)
  group: ''
- name: Force vector
  summary: Applied force table lookup entry [-1000, -400, -200, -50, 50, 200, 400, 1000] (default)
  group: ''
- name: Interpolation method
  summary: Method of interpolation between breakpoint values Smooth (default) | Linear
  group: ''
- name: Extrapolation method
  summary: Method of handling input values that fall outside range of breakpoint data set Linear (default) | Nearest | Error
  group: ''
```

### **Parameterization** — Method to characterize spring behavior `By polynomial` (default) | `By table lookup`

Spring behavior selection. You can choose to parameterize by polynomial or
lookup table.

### **Symmetry** — Spring behavior versus zero deformation position `Symmetric` (default) | `Two-sided`

Spring behavior symmetry about the point of zero deformation. When you
select `Symmetric`, the block applies one
polynomial symmetrically about the point of zero deformation. When you
select `Two-sided`, the block applies unique
polynomials for tension and compression.

#### Dependencies

To enable this parameter, set **Parameterization** to
`By polynomial`.

### **Vector of spring coefficients** — Symmetric deformation polynomial coefficients `[100, 0, 10, 0, 1]` `N/m` (default) | vector

Polynomial spring rate coefficients. The highest non zero-order element must be positive.
Physical units represent the first coefficient, and the block selects the
appropriate higher-order units for you. This vector must have a length of
5.

#### Dependencies

To enable this parameter, set **Parameterization** to
`By polynomial` and
**Symmetry** to
`Symmetric`.

### **Vector of spring tension coefficients** — Positive two-sided deformation polynomial coefficients `[100, 0, 10, 0, 1]` `N/m` (default)

Polynomial coefficients for the spring tension. Physical units represent the first
coefficient, and the block selects the appropriate higher-order units for
you. This vector must have a length of 5.

#### Dependencies

To enable this parameter, set **Parameterization** to
`By polynomial` and
**Symmetry** to
`Two-sided`.

### **Vector of spring compression coefficients** — Negative two-sided deformation polynomial coefficients `[1000, -10, 100, 0, 0]` `N/m` (default)

Polynomial coefficients for the spring compression. Physical units represent the first
coefficient, and the block selects the appropriate higher-order units for
you. This vector must have a length of 5.

### **Deformation vector** — Deformation due to force table lookup entry `[-1, -.5, -.3, -.1, .1, .3, .5, 1]` (default)

Relative displacement values with respect to the zero-deformation position
for the corresponding elements in the **Force vector**
parameter. This parameter must be the same length as the **Force
vector** parameter. The minimum vector length depends on the
interpolation method: two for `Linear` and three
for `Smooth`. If not included in the vector, the
block automatically adds a point at the origin deformation–force
coordinate.

### **Force vector** — Applied force table lookup entry `[-1000, -400, -200, -50, 50, 200, 400, 1000]` (default)

Force values for the corresponding element in the **Deformation
vector** parameter. This parameter must be the same length as
the **Deformation vector** parameter. The minimum vector
length is: two for `Linear` and three for
`Smooth`. The block automatically adds a point
at the origin deformation-force coordinate if you do not specify one.

### **Interpolation method** — Method of interpolation between breakpoint values `Smooth` (default) | `Linear`

Lookup table breakpoint interpolation. The block uses the
`tablelookup` function to model nonlinearity by using
vector data to map input values to output values:

- `Linear` — Select this option for the
  lowest computational cost.
- `Smooth` — Select this option to produce
  a continuous curve with continuous first-order derivatives.

For more information, see `tablelookup`.

### **Extrapolation method** — Method of handling input values that fall outside range of breakpoint data set `Linear` (default) | `Nearest` | `Error`

Lookup table breakpoint extrapolation. This method determines the output
value when the input value is outside the range specified in the argument
list. The block uses the `tablelookup` function to model
nonlinearity by using vector data to map input values to output values:

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

For more information, see `tablelookup`.
## Libraries

Simscape / Driveline / Couplings & Drives / Springs & Dampers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013a**

## Description

Translational spring based on polynomial or table lookup parameterizations

The Nonlinear Translational Spring block represents a
translational spring with a nonlinear force-displacement curve. The spring force
magnitude is a general function of displacement and does not necessarily need to satisfy
Hooke’s law. You can parameterize the force-displacement relationship using a polynomial
or a lookup table. The spring force can be symmetric or asymmetric with respect to zero
deformation.

The symmetric polynomial parameterization defines spring force according to the expression

F=k1x+sign(x)⋅k2x2+k3x3+sign(x)⋅k4x4+k5x5,

where:

- *F* is the spring force.
- *k*1,
  *k*2, ...,
  *k*5 are the spring
  coefficients.
- *x* is the relative displacement between ports
  **R** and **C**.
- *x*init is the initial relative
  displacement.

At simulation start *x* is equal to
*x*init.

To avoid zero-crossings that slow simulation, eliminate the sign function from the
polynomial expression by specifying an odd polynomial (*b*2,*b*4
= 0).

The asymmetric polynomial parameterization defines spring force according to the expression:

F={k1tx+k2tx2+k3tx3+k4tx4+k5tx5,x≥0k1cx+k2cx2+k3cx3+k4cx4+k5cx5,x<0,

where:

- *k*1,
  *k*2, ...,
  *k*5 are the spring tension
  coefficients.
- *k*1,
  *k*2, ...,
  *k*5 are the spring compression
  coefficients.

Both polynomial parameterizations use a fifth-order polynomial expression. To use a
lower-order polynomial, set the unneeded higher-order coefficients to zero. To use a
higher-order polynomial, fit to a lower-order polynomial or use the table lookup
parameterization.

Setting **Parameterization** to `By table lookup`
defines the damping torque based on a set of torque and angular velocity vectors. If you
do not enter a datapoint for the origin, the block automatically adds one (zero angular
velocity and zero torque).

### Variables

To set the priority and initial target values for the block variables prior to simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
