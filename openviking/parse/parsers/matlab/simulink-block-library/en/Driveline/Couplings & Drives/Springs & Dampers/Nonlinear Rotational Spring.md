---
type: simulink-block
title: 'Nonlinear Rotational Spring'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives / Springs & Dampers'
documentation_page: 'nonlinearrotationalspring'
documentation_source_path: 'ref/nonlinearrotationalspring.html'
language: en
---

# Nonlinear Rotational Spring

## Ports
```yaml
ports: []
```

`C`
:   Rotational conserving port

`R`
:   Rotational conserving port
## Parameters
```yaml
parameters: []
```

**Parameterization**
:   Select spring parameterization. Options are `By
    polynomial` and `By table
    lookup`.

     By Polynomial

    Specify nonlinear spring function in terms of polynomial
    coefficients.

    **Symmetry**
    :   Choose between symmetric and two-sided polynomial parameterizations.

        - `Symmetric` —
          Specify one set of polynomial coefficients
          governing spring torque in both tension and
          compression.

          **Vector of spring coefficients**
          :   Enter five-element vector with polynomial
              spring coefficients. The highest non-zero order
              must be positive. Physical units are for the first
              coefficient.

              The default vector is `[1 0 0.1 0
              0.01]`. The default unit is
              `N*m/rad`.
        - `Two-sided` —
          Specify two sets of polynomial coefficients
          governing spring torque, one for positive
          deformation, the other for negative
          deformation.

          **Vector of spring tension coefficients**
          :   Enter a five-element vector containing the
              coefficients of the polynomial spring
              *tension* function. The highest
              order non-zero coefficient must be positive. The
              specified physical unit is the unit of the first
              polynomial coefficient.

          **Vector of spring compression coefficients**
          :   Enter a five-element vector containing the
              coefficients of the polynomial spring
              *compression* function. The
              highest order non-zero coefficient must be
              positive. The specified physical unit is the unit
              of the first polynomial coefficient.

     By table lookup

    **Deformation vector**
    :   Enter a vector containing the deformation values used in
        the table lookup. The vector must contain a minimum number
        of elements based on the interpolation method: two for
        `Linear`, and three for
        `Smooth`. The vector must also
        contain the same number of elements as the torque
        vector.

    **Torque vector**
    :   Enter a vector containing the torque values that
        correspond to the deformation vector values. The vector must
        contain a minimum number of elements based on the
        interpolation method: two for
        `Linear`, and three for
        `Smooth`. The vector must also
        contain the same number of elements as the deformation
        vector. If not included in the vectors, the block
        automatically adds a point at the (0,0) deformation–torque coordinate.

    **Interpolation method**
    :   Select method used to calculate deformation-torque values
        between table lookup data points.

        - `Linear` — Select
          this option to get the best performance.
        - `Smooth` — Select
          this option to produce a continuous curve with
          continuous first-order derivatives.

        For more information on interpolation algorithms, see the
        PS Lookup Table
        (1D) block reference page.

    **Extrapolation method**
    :   Select method used to calculate deformation-torque values
        outside the table lookup data range.

        - `Linear` — Select
          this option to produce a curve with continuous
          first-order derivatives in the extrapolation region
          and at the boundary with the interpolation
          region.
        - `Nearest` — Select
          this option to produce an extrapolation that does
          not go above the highest point in the data or below
          the lowest point in the data.

        For more information on extrapolation algorithms, see the
        PS Lookup Table
        (1D) block reference page.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013a**

## Description

Torsional spring based on polynomial or table lookup parameterizations

The block represents a torsional spring with nonlinear torque-displacement curve. The
spring torque magnitude is a general function of displacement. It need not satisfy
Hooke’s law. Polynomial and table lookup parameterizations provide two ways to specify
the torque-displacement relationship. The spring torque can be symmetric or asymmetric
with respect to zero deformation.

The symmetric polynomial parameterization defines spring torque according to the expression:

T=k1θ+sign(θ)⋅k2θ2+k3θ3+sign(θ)⋅k4θ4+k5θ5,

where:

- *T* — Spring force
- *k*1,
  *k*2,
  ...,*k*5 — Spring
  coefficients
- *θ* — Relative displacement between ports R and C, θ=θinit+θR−θC
- *θ*init — Initial spring
  deformation
- *θ*R — Absolute angular
  position of port R
- *θ*C — Absolute angular
  position of port C

At simulation start (t=0), *θ*R and
*θ*C are zero, making *θ*
equal to *θ*init.

To avoid zero-crossings that slow simulation, eliminate the sign function from the
polynomial expression by specifying an odd polynomial (*b*2,*b*4
= 0).

The two-sided polynomial parameterization defines spring torque according to the expression:

T={k1tθ+k2tθ2+k3tθ3+k4tθ4+k5tθ5,θ≥0k1cθ−k2cθ2+k3cθ3−k4cθ4+k5cθ5,θ<0,

where:

- *k*1t,
  *k*2t, ...,
  *k*5t — Spring tension
  coefficients
- *k*1c,
  *k*2c, ...,
  *k*5c — Spring compression
  coefficients

Both polynomial parameterizations use a fifth-order polynomial expression. To use a
lower-order polynomial, set the unneeded higher-order coefficients to zero. To use a
higher-order polynomial, fit to a lower-order polynomial or use the table lookup
parameterization.

The table lookup parameterization defines spring torque based on a set of torque and
angular velocity vectors. If not specified, the block automatically adds a data point at
the origin (zero angular velocity and zero torque).

### Variables

To set the priority and initial target values for the block variables prior to simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
