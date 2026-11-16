---
type: simulink-block
title: 'FEM-Parameterized PMSM'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Permanent Magnet'
documentation_page: 'femparameterizedpmsm'
documentation_source_path: 'ref/femparameterizedpmsm.html'
language: en
---

# FEM-Parameterized PMSM

## Ports

### Conserving

### **a** — A-phase connection electrical

Electrical conserving port associated with the A-phase
connection.

#### Dependencies

To enable this port, set **Winding type** to
`Wye-wound` or
`Delta-wound`.

### **b** — B-phase connection electrical

Electrical conserving port associated with the B-phase
connection.

#### Dependencies

To enable this port, set **Winding type** to
`Wye-wound` or
`Delta-wound`.

### **c** — C-phase connection electrical

Electrical conserving port associated with the C-phase
connection.

#### Dependencies

To enable this port, set **Winding type** to
`Wye-wound` or
`Delta-wound`.

### **a1** — *a* positive-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *a*
positive-end connection.

#### Dependencies

To enable this port, set **Winding type** to
`Open-end`.

### **b1** — *b* positive-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *b*
positive-end connection.

#### Dependencies

To enable this port, set **Winding type** to
`Open-end`.

### **c1** — *c* positive-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *c*
positive-end connection.

#### Dependencies

To enable this port, set **Winding type** to
`Open-end`.

### **a2** — *a* negative-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *a*
negative-end connection.

#### Dependencies

To enable this port, set **Winding type** to
`Open-end`.

### **b2** — *b* negative-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *b*
negative-end connection.

#### Dependencies

To enable this port, set **Winding type** to
`Open-end`.

### **c2** — *c* negative-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *c*
negative-end connection.

#### Dependencies

To enable this port, set **Winding type** to
`Open-end`.

### **n** — Neutral phase electrical

Electrical conserving port associated with the neutral phase.

#### Dependencies

To enable this port, set **Modeling option**
parameter to either

- `2-D partial derivative data | No thermal
  port`, `2-D partial
  derivative data | Show thermal port`,
  `3-D partial derivative data | No
  thermal port`, `3-D partial
  derivative data | Show thermal port`,
  `4-D partial derivative data | No
  thermal port`, or `4-D
  partial derivative data | Show thermal
  port` and set the **Winding
  type** parameter to
  `Wye-wound`.
- `3-D flux linkage data | No thermal
  port` or `3-D flux linkage
  data | Show thermal port`, and set the
  **Winding type** parameter to
  `Wye-wound` and the
  **Expose neutral port** parameter
  to `Yes`.

### **C** — Motor case mechanical

Mechanical rotational conserving port associated with the motor
case.

### **R** — Motor rotor mechanical

Mechanical rotational conserving port associated with the motor
rotor.

### **HA** — Winding A thermal port thermal

Thermal conserving port associated with winding A.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HB** — Winding B thermal port thermal

Thermal conserving port associated with winding B.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HC** — Winding C thermal port thermal

Thermal conserving port associated with winding C.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HR** — Rotor thermal port thermal

Thermal conserving port associated with the rotor.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

## Parameters

### **Modeling option** — Flux and torque parameterization methods `2-D partial derivative data | No thermal port` (default) | `2-D partial derivative data | Show thermal port` | `3-D partial derivative data | No thermal port` | `3-D partial derivative data | Show thermal port` | `4-D partial derivative data | No thermal port` | `4-D partial derivative data | Show thermal port` | `3-D flux linkage data | No thermal port` | `3-D flux linkage data | Show thermal port`

Parameterization method for the flux and torque. To model the effects of
copper resistance and iron losses that convert electrical power to heat,
choose the options with thermal ports.

### Electrical (2-D Partial Derivative Data Parameterization)

This configuration of the **Electrical** parameters corresponds
to the 2-D Partial Derivative Data block parameterizations, with or without thermal
ports. If you are using the 3-D Partial Derivative Data, 4-D Partial Derivative
Data, or 3-D Flux Linkage Data parameterization of the block, see Electrical (3-D Partial Derivative Data Parameterization), Electrical (4-D Partial Derivative Data Parameterization), or Electrical (3-D Flux Linkage Data Parameterization) respectively.

### **Parameterization** — Parameterization method `Assume constant mutual inductance - tabulate with phase current and rotor angle` (default) | `Assume sinusoidal back emf - tabulate with d- and q-axis currents`

Select the parameterization method:

- `Assume constant mutual inductance - tabulate
  with phase current and rotor angle`
  — This method assumes that the flux linking each
  winding depends nonlinearly only on the current in that same
  winding, plus the rotor angle.
- `Assume sinusoidal back emf - tabulate with d-
  and q-axis currents` — This method
  assumes that the flux linking each winding depends
  nonlinearly on all stator winding currents. It also assumes
  that the permanent magnet flux linkage is sinusoidal. This
  option is usually a good fit for interior magnet PMSMs (or
  IPMSMs).

### **Winding type** — Stator windings configuration `Wye-wound` (default) | `Delta-wound` | `Open-end`

Select the configuration for the stator windings:

- `Wye-wound` — The stator windings
  are wye-wound.
- `Delta-wound` — The stator
  windings are delta-wound. The *a*-phase is
  connected between ports **a** and
  **b**, the *b*-phase
  between ports **b** and
  **c** and the
  *c*-phase between ports
  **c** and
  **a**.
- `Open-end` — The windings are in
  an open-end configuration. The block exposes each end of the
  windings as electrical connections.

### **Current vector, i** — Vector of currents `[-2, 0, 2]` `A` (default)

Vector of currents corresponding to the provided flux linkage partial
derivatives. The current vector must be two-sided (have positive and
negative values).

#### Dependencies

This parameter is visible only when you set the
**Parameterization** parameter to
`Assume constant mutual inductance - tabulate with
phase current and rotor angle`.

### **Rotor angle vector, theta** — Vector of rotor angles `[0, 20, 40, 60]` `deg` (default)

Vector of rotor angles corresponding to the provided flux linkage
partial derivatives. The vector must start at zero. This value
corresponds to the angle where the A-phase magnetic flux aligns with the
rotor permanent magnetic peak flux direction (the direct-axis, or
*`d`*-axis). The last value,
*Θ*max, must be the rotor
angle where the flux linkage pattern peaks again. Therefore, the number
of pole pairs is 360/*Θ*max if *Θ*max is
expressed in degrees. The default value corresponds to a 6 pole-pair
motor.

#### Dependencies

This parameter is visible only when you set the
**Parameterization** parameter to
`Assume constant mutual inductance - tabulate with
phase current and rotor angle`.

### **Flux linkage partial derivative wrt current, dPhi(i,theta)/di** — Flux linkage partial derivative with respect to current `0.0002*ones(3,4)` `Wb/A` (default)

Matrix of the flux linkage partial derivatives with respect to
current, defined as a function of current vector and rotor angle vector.
Flux linkage is the flux multiplied by the number of winding turns. The
default value corresponds to the special case where stator inductance
does not depend on stator current or on rotor angle.

#### Dependencies

This parameter is visible only when you set the
**Parameterization** parameter to
`Assume constant mutual inductance - tabulate with
phase current and rotor angle`.

### **Flux linkage partial derivative wrt angle, dPhi(i,theta)/dtheta** — Flux linkage partial derivative with respect to angle `[0, -0.16, 0.16, 0; 0, -0.16, 0.16, 0; 0, -0.16, 0.16, 0]` `Wb/rad` (default)

Matrix of the flux linkage partial derivatives with respect to the
rotor angle, defined as a function of current vector and rotor angle
vector. Flux linkage is the flux multiplied by the number of winding
turns. The default value is `[0, -0.16, 0.16, 0; 0, -0.16, 0.16,
0; 0, -0.16, 0.16, 0]` Wb/rad, which corresponds to the
special case where stator inductance does not depend on stator
current.

#### Dependencies

This parameter is visible only when you set the
**Parameterization** parameter to
`Assume constant mutual inductance - tabulate with
phase current and rotor angle`.

### **Direct axis current vector, id** — Direct axis current vector `[-200, 0, 200]` `A` (default)

Vector of *`d`*-axis currents corresponding to
the provided inductances. The current vector must be two-sided (have
positive and negative values).

#### Dependencies

This parameter is visible only when you set the
**Parameterization** parameter to
`Assume sinusoidal back emf - tabulate with d- and
q-axis currents`.

### **Quadrature axis current vector, iq** — Quadrature axis current vector `[-200, 0, 200]` `A` (default)

Vector of *`q`*-axis currents corresponding to
the provided inductances. The current vector must be two-sided (have
positive and negative values).

#### Dependencies

This parameter is visible only when you set the
**Parameterization** parameter to
`Assume sinusoidal back emf - tabulate with d- and
q-axis currents`.

### **Ld matrix, Ld(id,iq)** — Ld matrix `0.0002*ones(3,3)` `H` (default)

Matrix of the *`d`*-axis inductances with
respect to current, defined as a function of
*`d`*-axis and
*`q`*-axis current vectors.

#### Dependencies

This parameter is visible only when you set the
**Parameterization** parameter to
`Assume sinusoidal back emf - tabulate with d- and
q-axis currents`.

### **Lq matrix, Lq(id,iq)** — Lq matrix `0.0002*ones(3,3)` `H` (default)

Matrix of the *`q`*-axis inductances with
respect to current, defined as a function of
*`d`*-axis and
*`q`*-axis current vectors.

#### Dependencies

This parameter is visible only when you set the
**Parameterization** parameter to
`Assume sinusoidal back emf - tabulate with d- and
q-axis currents`.

### **Permanent magnet flux linkage, PM(id,iq)** — Permanent magnet flux linkage `0.1*ones(3,3)` `Wb` (default)

Matrix of the permanent magnet flux linkages with respect to current,
defined as a function of *`d`*-axis and
*`q`*-axis current vectors. Flux linkage is
the flux multiplied by the number of winding turns.

#### Dependencies

This parameter is visible only when you set the
**Parameterization** parameter to
`Assume sinusoidal back emf - tabulate with d- and
q-axis currents`.

### **Number of pole pairs** — Number of pole pairs `6` (default)

Number of the permanent magnet motor pole pairs.

#### Dependencies

This parameter is visible only when you set the
**Parameterization** parameter to
`Assume sinusoidal back emf - tabulate with d- and
q-axis currents`.

### **Calculate torque matrix?** — Electromagnetic torque data specification `Yes` (default) | `No — specify directly`

Specify the way of providing the electromagnetic torque data:

- Yes — The block calculates the torque from the flux
  linkage information, as a function of current and rotor
  angle.
- `No — specify directly`
  — Enter the electromagnetic torque data directly, by
  using the **Torque matrix, T(i,theta)**
  parameter.

#### Dependencies

This parameter is visible only when you set the
**Parameterization** parameter to
`Assume constant mutual inductance - tabulate with
phase current and rotor angle`. If you set the
**Parameterization** parameter to
`Assume sinusoidal back emf - tabulate with d- and
q-axis currents`, the equation for torque is
explicit in terms of the provided matrices.

### **Torque matrix, T(i,theta)** — Torque matrix `zeros(3, 3, 3, 4)` `N*m` (default)

Specify a matrix of the electromagnetic torque applied to the rotor,
as a function of current and rotor angle. This parameter is visible only
if **Calculate torque matrix?** is set to
`No — specify directly`.

#### Dependencies

This parameter is visible only when you set the
**Calculate torque matrix?** parameter to
`No — specify directly`.

### **Interpolation method** — Interpolation method `Linear` `Smooth` (default)

Select one of the following interpolation methods for approximating
the output value when the input value is between two consecutive grid
points:

- `Linear` — Uses an extension
  of linear algorithm for multidimensional interpolation. Select
  this option to get the best performance.
- `Smooth` — Uses a modified
  Akima interpolation algorithm. Select this option to produce a
  continuous surface with continuous first-order
  derivatives.

For more information on interpolation methods, see the PS Lookup Table (2D)
block reference page.

### **Stator resistance per phase, Rs** — Stator resistance per phase `0.013` `Ohm` (default)

Resistance of each of the stator windings.

### **Stator mutual inductance, Ms** — Stator mutual inductance `0.00002` `H` (default)

Stator-stator mutual inductance, which is assumed to be independent of
both current and rotor angle.

#### Dependencies

This parameter is visible only when you set the
**Parameterization** parameter to
`Assume constant mutual inductance - tabulate with
phase current and rotor angle`.

### **Stator zero-sequence inductance, L0** — Stator zero-sequence inductance `0.00016` `H` (default)

Zero-sequence inductance.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Assume
sinusoidal back emf - tabulate with d- and q-axis
currents`.

### Electrical (3-D Partial Derivative Data Parameterization)

This configuration of the **Electrical** parameters corresponds
to the 3-D Partial Derivative Data block variants, with or without thermal ports. If
you are using the 2-D Partial Derivative Data, 4-D Partial Derivative Data, or 3-D
Flux Linkage Data parameterization of the block, see Electrical (2-D Partial Derivative Data Parameterization), Electrical (4-D Partial Derivative Data Parameterization), or Electrical (3-D Flux Linkage Data Parameterization) respectively.

### **Winding type** — Stator windings configuration `Wye-wound` (default) | `Delta-wound` | `Open-end`

Select the configuration for the stator windings:

- `Wye-wound` — The stator windings
  are wye-wound.
- `Delta-wound` — The stator
  windings are delta-wound. The *a*-phase is
  connected between ports **a** and
  **b**, the *b*-phase
  between ports **b** and
  **c** and the
  *c*-phase between ports
  **c** and
  **a**.
- `Open-end` — The windings are in
  an open-end configuration. The block exposes each end of the
  windings as electrical connections.

### **Direct-axis current vector, iD** — Direct-axis current vector `[-200, 0, 200]` `A` (default)

Vector of direct-axis currents corresponding to the provided flux
linkage partial derivatives. The current vector must be two-sided (have
positive and negative values).

### **Quadrature-axis current vector, iQ** — Quadrature-axis current vector `[-200, 0, 200]` `A` (default)

Vector of quadrature-axis currents corresponding to the provided flux
linkage partial derivatives. The current vector must be two-sided (have
positive and negative values).

### **Rotor angle vector, theta** — Rotor angle vector `[0, 20, 40, 60]` `deg` (default)

Vector of rotor angles corresponding to the provided flux linkage
partial derivatives. The vector must start at zero. This value
corresponds to the angle where the A-phase magnetic flux aligns with the
rotor permanent magnetic peak flux direction (the direct-axis, or
*`d`*-axis). The last value,
*Θ*max, must be the rotor
angle where the flux linkage pattern peaks again. Therefore, the number
of pole pairs is 360/*Θ*max if *Θ*max is
expressed in degrees. The default value corresponds to a 6 pole-pair
motor.

### **A-phase flux linkage partial derivative wrt iA, dPhiA(id,iq,theta)/diA** — A-phase flux linkage partial derivative with respect to iA `zeros(3, 3, 4)` `Wb/A` (default)

Matrix of the A-phase flux linkage partial derivatives with respect to
current in winding A, defined as a function of the two current vectors
and the rotor angle vector. Flux linkage is the flux multiplied by the
number of winding turns.

### **A-phase flux linkage partial derivative wrt iB, dPhiA(id,iq,theta)/diB** — A-phase flux linkage partial derivative with respect to iB `zeros(3, 3, 4)` `Wb/A` (default)

Matrix of the A-phase flux linkage partial derivatives with respect to
current in winding B, defined as a function of the two current vectors
and the rotor angle vector. Flux linkage is the flux multiplied by the
number of winding turns.

### **A-phase flux linkage partial derivative wrt iC, dPhiA(id,iq,theta)/diC** — A-phase flux linkage partial derivative with respect to iC `zeros(3, 3, 4)` `Wb/A` (default)

Matrix of the A-phase flux linkage partial derivatives with respect to
current in winding C, defined as a function of the two current vectors
and the rotor angle vector. Flux linkage is the flux multiplied by the
number of winding turns.

### **A-phase flux linkage partial derivative wrt angle, dPhiA(id,iq,theta)/dtheta** — A-phase flux linkage partial derivative with respect to angle `zeros(3, 3, 4)` `Wb/rad` (default)

Matrix of the A-phase flux linkage partial derivatives with respect to
rotor angle, defined as a function of the two current vectors and the
rotor angle vector. Flux linkage is the flux multiplied by the number of
winding turns.

### **Torque matrix, T(id,iq,theta)** — Torque matrix `zeros(3, 3, 4)` `N*m` (default)

Specify a matrix of the electromagnetic torque applied to the rotor,
as a function of the two currents and the rotor angle.

### **Interpolation method** — Interpolation method `Linear` (default) | `Smooth`

Select one of the following interpolation methods for approximating
the output value when the input value is between two consecutive grid
points:

- `Linear` — Uses an extension
  of linear algorithm for multidimensional interpolation. Select
  this option to get the best performance.
- `Smooth` — Uses a modified
  Akima interpolation algorithm. Select this option to produce a
  continuous surface with continuous first-order
  derivatives.

For more information on interpolation methods, see the PS Lookup Table (3D)
block reference page.

### **Stator resistance per phase, Rs** — Stator resistance per phase `0.013` `Ohm` (default)

Resistance of each of the stator windings.

### Electrical (4-D Partial Derivative Data Parameterization)

This configuration of the **Electrical** parameters corresponds
to the 4-D Partial Derivative Data block variants, with or without thermal ports. If
you are using the 2-D Partial Derivative Data, 3-D Partial Derivative Data, or 3-D
Flux Linkage Data parameterization of the block, see Electrical (2-D Partial Derivative Data Parameterization), Electrical (3-D Partial Derivative Data Parameterization), or Electrical (3-D Flux Linkage Data Parameterization) respectively.

### **Winding type** — Stator windings configuration `Wye-wound` (default) | `Delta-wound` | `Open-end`

Select the configuration for the stator windings:

- `Wye-wound` — The stator windings
  are wye-wound.
- `Delta-wound` — The stator
  windings are delta-wound. The *a*-phase is
  connected between ports **a** and
  **b**, the *b*-phase
  between ports **b** and
  **c** and the
  *c*-phase between ports
  **c** and
  **a**.
- `Open-end` — The windings are in
  an open-end configuration. The block exposes each end of the
  windings as electrical connections.

### **A-phase current vector, iA** — A-phase current vector `[-200, 0, 200]` `A` (default)

Vector of A-phase currents corresponding to the provided flux linkage
partial derivatives. The current vector must be two-sided (have positive
and negative values).

### **B-phase current vector, iB** — B-phase current vector `[-200, 0, 200]` `A` (default)

Vector of B-phase currents corresponding to the provided flux linkage
partial derivatives. The current vector must be two-sided (have positive
and negative values).

### **C-phase current vector, iC** — C-phase current vector `[-200, 0, 200]` `A` (default)

Vector of C-phase currents corresponding to the provided flux linkage
partial derivatives. The current vector must be two-sided (have positive
and negative values).

### **Rotor angle vector, theta** — Rotor angle vector `[0, 20, 40, 60]` `deg` (default)

Vector of rotor angles corresponding to the provided flux linkage
partial derivatives. The vector must start at zero. This value
corresponds to the angle where the A-phase magnetic flux aligns with the
rotor permanent magnetic peak flux direction (the direct-axis, or
*`d`*-axis). The last value,
*Θ*max, must be the rotor
angle where the flux linkage pattern peaks again. Therefore, the number
of pole pairs is 360/*Θ*max if *Θ*max is
expressed in degrees. The default value corresponds to a 6 pole-pair
motor.

### **A-phase flux linkage partial derivative wrt iA, dPhiA(iA,iB,iC,theta)/diA** — A-phase flux linkage partial derivative with respect to iA `zeros(3, 3, 3, 4)` `Wb/A` (default)

Matrix of the A-phase flux linkage partial derivatives with respect to
current in winding A, defined as a function of the three current vectors
and the rotor angle vector. Flux linkage is the flux multiplied by the
number of winding turns.

### **A-phase flux linkage partial derivative wrt iB, dPhiA(iA,iB,iC,theta)/diB** — A-phase flux linkage partial derivative with respect to iB `zeros(3, 3, 3, 4)` `Wb/A` (default)

Matrix of the A-phase flux linkage partial derivatives with respect to
current in winding B, defined as a function of the three current vectors
and the rotor angle vector. Flux linkage is the flux multiplied by the
number of winding turns.

### **A-phase flux linkage partial derivative wrt iC, dPhiA(iA,iB,iC,theta)/diC** — A-phase flux linkage partial derivative with respect to iC `zeros(3, 3, 3, 4)` `Wb/A` (default)

Matrix of the A-phase flux linkage partial derivatives with respect to
current in winding C, defined as a function of the three current vectors
and the rotor angle vector. Flux linkage is the flux multiplied by the
number of winding turns.

### **A-phase flux linkage partial derivative wrt angle, dPhiAiA,iB,iC,theta)/dtheta** — A-phase flux linkage partial derivative with respect to angle `zeros(3, 3, 3, 4)` `Wb/rad` (default)

Matrix of the A-phase flux linkage partial derivatives with respect to
rotor angle, defined as a function of the three current vectors and the
rotor angle vector. Flux linkage is the flux multiplied by the number of
winding turns.

### **Torque matrix, T(iA,iB,iC,theta)** — Torque matrix `zeros(3, 3, 3, 4)` `N*m` (default)

Specify a matrix of the electromagnetic torque applied to the rotor,
as a function of the three currents and the rotor angle.

### **Interpolation method** — Interpolation method `Linear` (default) | `Smooth`

Select one of the following interpolation methods for approximating
the output value when the input value is between two consecutive grid
points:

- `Linear` — Uses an extension
  of linear algorithm for multidimensional interpolation. Select
  this option to get the best performance.
- `Smooth` — Uses a modified
  Akima interpolation algorithm. Select this option to produce a
  continuous surface with continuous first-order
  derivatives.

For more information on interpolation methods, see the PS Lookup Table (3D)
block reference page.

### **Stator resistance per phase, Rs** — Stator resistance per phase `0.013` `Ohm` (default)

Resistance of each of the stator windings.

### Electrical (3-D Flux Linkage Data Parameterization)

This configuration of the **Electrical** parameters corresponds
to the 3-D Flux Linkage Data block variants, with or without thermal ports. If you
are using the 2-D Partial Derivative Data, 3-D Partial Derivative Data, or 4-D
Partial Derivative Data parameterization of the block, see Electrical (2-D Partial Derivative Data Parameterization), Electrical (3-D Partial Derivative Data Parameterization), or Electrical (4-D Partial Derivative Data Parameterization), respectively.

### **Flux linkage data format** — Flux linkage data format `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` (default) | `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` | `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` | `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`

Select the flux linkage data format used by your FE tool:

- `D and Q axes flux linkages as a function of
  D-axis current (iD), Q-axis current (iQ), and rotor
  angle (theta)`
- `D and Q axes flux linkages as a function of
  peak current magnitude (I), current advance angle (B),
  and rotor angle (theta)`
- `A-phase flux linkage as a function of D-axis
  current (iD), Q-axis current (iQ), and rotor angle
  (theta)`
- `A-phase flux linkage as a function of peak
  current magnitude (I), current advance angle (B), and
  rotor angle (theta)`

### **Winding type** — Stator windings configuration `Wye-wound` (default) | `Delta-wound` | `Open-end`

Select the configuration for the stator windings:

- `Wye-wound` — The stator windings
  are wye-wound.
- `Delta-wound` — The stator
  windings are delta-wound. The *a*-phase is
  connected between ports **a** and
  **b**, the *b*-phase
  between ports **b** and
  **c** and the
  *c*-phase between ports
  **c** and
  **a**.
- `Open-end` — The windings are in
  an open-end configuration. The block exposes each end of the
  windings as electrical connections.

### **Expose neutral port** — Neutral port visibility `No` (default) | `Yes`

Whether to expose the neutral port of the block.

If you expose the neutral port, the block also models the zero
sequence currents. The zero sequence is parameterized by the
**Stator zero-sequence inductance, L0** parameter.
When you tabulate in terms of *iD* and
*iQ*, or in terms of current magnitude and phase
advance, there is no information about non-linear dependence on the
zero-sequence current, and the block introduces a degree of
approximation. For more accurate results, particularly for large
zero-sequence currents, use the **4-D partial derivative
data** parameterization option.

#### Dependencies

To enable this parameter, set **Winding type**
parameter to `Wye-wound`.

### **Number of pole pairs** — Number of pole pairs `4` (default)

Number of the permanent magnet motor pole pairs. The default value is
`4`.

### **Park's convention for tabulated data** — Park's convention for tabulated data `Q leads D, rotor angle measured from A-phase to D-axis` (default) | `Q leads D, rotor angle measured from A-phase to Q-axis` | `D leads Q, rotor angle measured from A-phase to D-axis` | `D leads Q, rotor angle measured from A-phase to Q-axis`

Select the order and reference angle for the Park transform mapping
the given *dq* data to the three windings.

- `Q leads D, rotor angle measured from A-phase
  to D-axis` — Quadrature-direct
  transformation with angle measured with respect to
  *d* axis.
- `Q leads D, rotor angle measured from A-phase
  to Q-axis` — Quadrature-direct
  transformation with angle measured with respect to
  *q* axis.
- `D leads Q, rotor angle measured from A-phase
  to D-axis` — Direct-quadrature
  transformation with angle measured with respect to
  *d* axis.
- `D leads Q, rotor angle measured from A-phase
  to Q-axis` — Direct-quadrature
  transformation with angle measured with respect to
  *q* axis.

### **Direct-axis current vector, iD** — Direct-axis current vector `[-200, 0, 200]` `A` (default)

Vector of direct-axis currents at which the flux linkage is tabulated.
The current vector must be two-sided (have positive and negative
values).

#### Dependencies

This parameter is visible only when you set the **Flux
linkage data format** parameter to `D and Q
axes flux linkages as a function of D-axis current (iD), Q-axis
current (iQ), and rotor angle (theta)` or
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`.

### **Quadrature-axis current vector, iQ** — Quadrature-axis current vector `[-200, 0, 200]` `A` (default)

Vector of quadrature-axis currents at which the flux linkage is
tabulated. The current vector must be two-sided (have positive and
negative values).

#### Dependencies

This parameter is visible only when you set the **Flux
linkage data format** parameter to `D and Q
axes flux linkages as a function of D-axis current (iD), Q-axis
current (iQ), and rotor angle (theta)` or
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`.

### **Peak current magnitude vector, I** — Peak current magnitude vector `[0, 100, 200]` `A` (default)

Row vector of current magnitudes at which the flux linkage is
tabulated. The first element must be zero. The adjacent current value
should be small relative to the current values at which magnetic
saturation begins to occur. This is because derived flux partial
derivatives are ill-defined at zero current, and so are calculated at
this first nonzero current instead.

#### Dependencies

This parameter is visible only when you set the **Flux
linkage data format** parameter to `D and Q
axes flux linkages as a function of peak current magnitude (I),
current advance angle (B), and rotor angle (theta)`
or `A-phase flux linkage as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)`.

### **Current advance angle, B** — Current advance angle `[-180, -90, 0, 90, 180]` `deg` (default)

Row vector of current advance angle values at which the flux linkage
is tabulated. Current advance angle is defined as the angle by which the
current leads the quadrature (Q) axis.

#### Dependencies

This parameter is visible only when you set the **Flux
linkage data format** parameter to `D and Q
axes flux linkages as a function of peak current magnitude (I),
current advance angle (B), and rotor angle (theta)`
or `A-phase flux linkage as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)`.

### **Rotor angle vector, theta** — Rotor angle vector `[0, 5, 10, 15, 20, 25, 30]` `deg` (default)

Vector of rotor angles at which the flux linkage is tabulated. The
vector must start at zero. The default value corresponds to a 4
pole-pair motor.

If **Flux linkage data format** is `D and
Q axes flux linkages as a function of D-axis current (iD), Q-axis
current (iQ), and rotor angle (theta)` or
`D and Q axes flux linkages as a function of peak
current magnitude (I), current advance angle (B), and rotor angle
(theta)` (that is, if you tabulate D and Q flux linkage
data), then the rotor angle vector must have four or more points and a
range from 0 to 120/*N* degrees, where
*N* is the number of pole pairs. If **Flux
linkage data format** is `A-phase flux linkage
as a function of D-axis current (iD), Q-axis current (iQ), and rotor
angle (theta)` or `A-phase flux linkage as
a function of peak current magnitude (I), current advance angle (B),
and rotor angle (theta)` (that is, if you tabulate
A-phase flux linkage data), then the rotor angle vector must have
3*n*+1 points, where *n*>=2, and
the range must be from 0 to 360/*N* degrees.

### **D-axis flux linkage, Fd(iD,iQ,theta)** — D-axis flux linkage `zeros(3, 3, 7)` `Wb` (default)

Matrix of the *d*-axis flux linkage, defined as a
function of the *dq* currents, and the rotor angle
vector. Flux linkage is the flux multiplied by the number of winding
turns.

If your flux data is given in a different order, you can use the
`permute` function to
reorder it. For an example of this reordering, see the associated MATLAB
script in Import IPMSM Flux Linkage Data from ANSYS Maxwell.

#### Dependencies

This parameter is visible only when you set the **Flux
linkage data format** parameter to `D and Q
axes flux linkages as a function of D-axis current (iD), Q-axis
current (iQ), and rotor angle (theta)`.

### **Q-axis flux linkage, Fq(iD,iQ,theta)** — Q-axis flux linkage `zeros(3, 3, 7)` `Wb` (default)

Matrix of the *q*-axis flux linkage, defined as a
function of the *dq* currents, and the rotor angle
vector. Flux linkage is the flux multiplied by the number of winding
turns.

If your flux data is given in a different order, you can use the
`permute` function to
reorder it. For an example of this reordering, see the associated MATLAB
script in Import IPMSM Flux Linkage Data from ANSYS Maxwell.

#### Dependencies

This parameter is visible only when you set the **Flux
linkage data format** parameter to `D and Q
axes flux linkages as a function of D-axis current (iD), Q-axis
current (iQ), and rotor angle (theta)`.

### **D-axis flux linkage, Fd(I,B,theta)** — D-axis flux linkage `zeros(3, 5, 7)` `Wb` (default)

3-D matrix of *d*-axis flux linkage values as a
function of **Peak current magnitude vector, I**,
**Current advance angle, B**, and **Rotor
angle vector, theta**.

If your flux data is given in a different order, you can use the
`permute` function to
reorder it. For an example of this reordering, see the associated MATLAB
script in Import IPMSM Flux Linkage Data from ANSYS Maxwell.

#### Dependencies

This parameter is visible only when you set the **Flux
linkage data format** parameter to `D and Q
axes flux linkages as a function of peak current magnitude (I),
current advance angle (B), and rotor angle
(theta)`.

### **Q-axis flux linkage, Fq(I,B,theta)** — Q-axis flux linkage `zeros(3, 5, 7)` `Wb` (default)

3-D matrix of *q*-axis flux linkage values as a
function of **Peak current magnitude vector, I**,
**Current advance angle, B**, and **Rotor
angle vector, theta**.

If your flux data is given in a different order, you can use the
`permute` function to
reorder it. For an example of this reordering, see the associated MATLAB
script in Import IPMSM Flux Linkage Data from ANSYS Maxwell.

#### Dependencies

This parameter is visible only when you set the **Flux
linkage data format** parameter to `D and Q
axes flux linkages as a function of peak current magnitude (I),
current advance angle (B), and rotor angle
(theta)`.

### **A-phase flux linkage, F(iD,iQ,theta)** — A-phase flux linkage `zeros(3, 3, 7)` `Wb` (default)

3-D matrix of A-phase flux linkage values, as a function of the
*dq* currents and the rotor angle.

If your flux data is given in a different order, you can use the
`permute` function to
reorder it. For an example of this reordering, see the associated MATLAB
script in Import IPMSM Flux Linkage Data from ANSYS Maxwell.

#### Dependencies

This parameter is visible only when you set the **Flux
linkage data format** parameter to `A-phase
flux linkage as a function of D-axis current (iD), Q-axis
current (iQ), and rotor angle (theta)`.

### **A-phase flux linkage, F(I,B,theta)** — A-phase flux linkage `zeros(3, 5, 7)` `Wb` (default)

3-D matrix of A-phase flux linkage values, as a function of
**Peak current magnitude vector, I**,
**Current advance angle, B**, and **Rotor
angle vector, theta**.

If your flux data is given in a different order, you can use the
`permute` function to
reorder it. For an example of this reordering, see the associated MATLAB
script in Import IPMSM Flux Linkage Data from ANSYS Maxwell.

#### Dependencies

This parameter is visible only when you set the **Flux
linkage data format** parameter to `A-phase
flux linkage as a function of D-axis current (iD), Q-axis
current (iQ), and rotor angle (theta)`.

### **Torque matrix, T(iD,iQ,theta)** — Torque matrix `zeros(3, 3, 7)` `N*m` (default)

3-D matrix of the electromagnetic torque applied to the rotor, as a
function of the *dq* currents and the rotor
angle.

If your flux data is given in a different order, you can use the
`permute` function to
reorder it. For an example of this reordering, see the associated MATLAB
script in Import IPMSM Flux Linkage Data from ANSYS Maxwell.

#### Dependencies

This parameter is visible only when you set the **Flux
linkage data format** parameter to `D and Q
axes flux linkages as a function of D-axis current (iD), Q-axis
current (iQ), and rotor angle (theta)` or
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`.

### **Torque matrix, T(I,B,theta)** — Torque matrix `zeros(3, 5, 7)` `N*m` (default)

3-D matrix of the electromagnetic torque applied to the rotor, as a
function of **Peak current magnitude vector, I**,
**Current advance angle, B**, and **Rotor
angle vector, theta**.

If your flux data is given in a different order, you can use the
`permute` function to
reorder it. For an example of this reordering, see the associated MATLAB
script in Import IPMSM Flux Linkage Data from ANSYS Maxwell.

#### Dependencies

This parameter is visible only when you set the **Flux
linkage data format** parameter to `D and Q
axes flux linkages as a function of peak current magnitude (I),
current advance angle (B), and rotor angle (theta)`
or `A-phase flux linkage as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)`.

### **Interpolation method** — Interpolation method `Linear` (default) | `Smooth`

Select one of the following interpolation methods for approximating
the output value when the input value is between two consecutive grid
points:

- `Linear` — Uses an extension
  of linear algorithm for multidimensional interpolation. Select
  this option to get the best performance.
- `Smooth` — Uses a modified
  Akima interpolation algorithm. Select this option to produce a
  continuous surface with continuous first-order
  derivatives.

For more information on interpolation methods, see the PS Lookup Table (4D)
block reference page.

### **Stator resistance per phase, Rs** — Stator resistance per phase `0.013` `Ohm` (default)

Resistance of each of the stator windings.

### **Stator zero-sequence inductance, L0** — Stator zero-sequence inductance `0.00016` `H` (default)

Zero-sequence inductance.

#### Dependencies

To enable this parameter, set **Winding type** to
`Delta-Wound` or **Expose
neutral port** to
`Yes`.

### Iron Losses

For more information on calculating iron losses, see Calculating Iron Losses.

### **Model** — Iron losses modeling option `None` (default) | `Specify open and short circuit loss data (permanent magnet motors only)` | `Specify tabulated Steinmetz coefficients` | `Tabulate with current and speed`

Whether to enable iron losses modeling. The `Specify
tabulated Steinmetz coefficients` and
`Tabulate with current and speed` options
are only available if you choose the **3-D flux linkage data
| No thermal port**  or **3-D flux linkage
data | Show thermal port**  variants.

### **Open-circuit iron losses, [P\_hysteresis P\_eddy P\_excess]** — Open-circuit iron losses `[0.0, 0.0, 0.0]` `W` (default)

Row vector, of length 3, of the open-circuit iron losses due to
hysteresis, Eddy, and excess losses, respectively, at the frequency
specified by **Electrical frequency at which losses
determined**.

#### Dependencies

To enable this parameter, set **Model** to
`Specify open and short circuit loss data (permanent
magnet motors only)`

### **Short-circuit iron losses, [P\_hysteresis P\_eddy P\_excess]** — Short-circuit iron losses `[0.0, 0.0, 0.0]` `W` (default)

Row vector, of length 3, of the short-circuit iron losses due to
hysteresis, Eddy, and excess losses, respectively, at the frequency
specified by **Electrical frequency at which losses
determined**.

#### Dependencies

To enable this parameter, set **Model** to
`Specify open and short circuit loss data (permanent
magnet motors only)`

### **Electrical frequency at which losses determined** — Electrical frequency at which losses determined `60` `Hz` (default)

Electrical frequency at which the open-circuit and short-circuit iron
losses were measured.

#### Dependencies

To enable this parameter, set **Model** to
`Specify open and short circuit loss data (permanent
magnet motors only)`.

### **Short-circuit RMS current for short-circuit iron losses** — Short-circuit RMS current for short-circuit iron losses `95` `A` (default)

The resulting short-circuit RMS phase current when measuring the
short-circuit losses.

#### Dependencies

To enable this parameter, set **Model** to
`Specify open and short circuit loss data (permanent
magnet motors only)`

### **Rotor hysteresis loss coefficient, k\_hr(id,iq)** — Rotor hysteresis loss coefficient `zeros(3, 3)` `W/Hz` (default)

Hysteresis loss coefficient of the rotor depending on the
*d*-axis and *q*-axis currents. It
is used by the Steinmetz equation.

#### Dependencies

To enable this parameter, set **Model** to
`Specify tabulated Steinmetz
coefficients` and, in the
**Electrical** tab, set **Flux linkage
data format** to either `D and Q axes flux
linkages as a function of D-axis current (iD), Q-axis current
(iQ), and rotor angle (theta)` or
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`.

### **Rotor eddy current loss coefficient, k\_Jr(id,iq)** — Rotor eddy current loss coefficient `zeros(3, 3)` `W/Hz^2` (default)

Eddy current loss coefficient of the rotor depending on the
*d*-axis and *q*-axis currents. It
is used by the Steinmetz equation.

#### Dependencies

To enable this parameter, set **Model** to
`Specify tabulated Steinmetz
coefficients` and, in the
**Electrical** tab, set **Flux linkage
data format** to either `D and Q axes flux
linkages as a function of D-axis current (iD), Q-axis current
(iQ), and rotor angle (theta)` or
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`.

### **Rotor excess current loss coefficient, k\_er(id,iq)** — Rotor excess current loss coefficient `zeros(3, 3)` `W/Hz^1.50000` (default)

Excess current loss coefficient of the rotor depending on the
*d*-axis and *q*-axis currents. It
is used by the Steinmetz equation.

#### Dependencies

To enable this parameter, set **Model** to
`Specify tabulated Steinmetz
coefficients` and, in the
**Electrical** tab, set **Flux linkage
data format** to either `D and Q axes flux
linkages as a function of D-axis current (iD), Q-axis current
(iQ), and rotor angle (theta)` or
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`.

### **Stator hysteresis loss coefficient, k\_hs(id,iq)** — Stator hysteresis loss coefficient `zeros(3, 3)` `W/Hz` (default)

Hysteresis loss coefficient of the stator depending on the
*d*-axis and *q*-axis currents. It
is used by the Steinmetz equation.

#### Dependencies

To enable this parameter, set **Model** to
`Specify tabulated Steinmetz
coefficients` and, in the
**Electrical** tab, set **Flux linkage
data format** to either `D and Q axes flux
linkages as a function of D-axis current (iD), Q-axis current
(iQ), and rotor angle (theta)` or
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`.

### **Stator eddy current loss coefficient, k\_Js(id,iq)** — Stator eddy current loss coefficient `zeros(3, 3)` `W/Hz^2` (default)

Eddy current loss coefficient of the stator depending on the
*d*-axis and *q*-axis currents. It
is used by the Steinmetz equation.

#### Dependencies

To enable this parameter, set **Model** to
`Specify tabulated Steinmetz
coefficients` and, in the
**Electrical** tab, set **Flux linkage
data format** to either `D and Q axes flux
linkages as a function of D-axis current (iD), Q-axis current
(iQ), and rotor angle (theta)` or
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`.

### **Stator excess current loss coefficient, k\_es(id,iq)** — Stator excess current loss coefficient `zeros(3, 3)` `W/Hz^1.50000` (default)

Excess current loss coefficient of the stator depending on the
*d*-axis and *q*-axis currents. It
is used by the Steinmetz equation.

#### Dependencies

To enable this parameter, set **Model** to
`Specify tabulated Steinmetz
coefficients` and, in the
**Electrical** tab, set **Flux linkage
data format** to either `D and Q axes flux
linkages as a function of D-axis current (iD), Q-axis current
(iQ), and rotor angle (theta)` or
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`.

### **Rotor hysteresis loss coefficient, k\_hr(I,B)** — Rotor hysteresis loss coefficient `zeros(3, 5)` `W/Hz` (default)

Hysteresis loss coefficient of the rotor depending on the current
magnitude and current phase advance. It is used by the Steinmetz
equation.

#### Dependencies

To enable this parameter, set **Model** to
`Specify tabulated Steinmetz
coefficients` and, in the
**Electrical** tab, set **Flux linkage
data format** to either `D and Q axes flux
linkages as a function of peak current magnitude (I), current
advance angle (B), and rotor angle (theta)` or
`A-phase flux linkage as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)`.

### **Rotor eddy current loss coefficient, k\_Jr(I,B)** — Rotor eddy current loss coefficient `zeros(3, 5)` `W/Hz^2` (default)

Eddy current loss coefficient of the rotor depending on the current
magnitude and current phase advance. It is used by the Steinmetz
equation.

#### Dependencies

To enable this parameter, set **Model** to
`Specify tabulated Steinmetz
coefficients` and, in the
**Electrical** tab, set **Flux linkage
data format** to either `D and Q axes flux
linkages as a function of peak current magnitude (I), current
advance angle (B), and rotor angle (theta)` or
`A-phase flux linkage as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)`.

### **Rotor excess current loss coefficient, k\_er(I,B)** — Rotor excess current loss coefficient `zeros(3, 5)` `W/Hz^1.50000` (default)

Excess current loss coefficient of the rotor depending on the current
magnitude and current phase advance. It is used by the Steinmetz
equation.

#### Dependencies

To enable this parameter, set **Model** to
`Specify tabulated Steinmetz
coefficients` and, in the
**Electrical** tab, set **Flux linkage
data format** to either `D and Q axes flux
linkages as a function of peak current magnitude (I), current
advance angle (B), and rotor angle (theta)` or
`A-phase flux linkage as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)`.

### **Stator hysteresis loss coefficient, k\_hs(I,B)** — Stator hysteresis loss coefficient `zeros(3, 5)` `W/Hz` (default)

Hysteresis loss coefficient of the stator depending on the current
magnitude and current phase advance. It is used by the Steinmetz
equation.

#### Dependencies

To enable this parameter, set **Model** to
`Specify tabulated Steinmetz
coefficients` and, in the
**Electrical** tab, set **Flux linkage
data format** to either `D and Q axes flux
linkages as a function of peak current magnitude (I), current
advance angle (B), and rotor angle (theta)` or
`A-phase flux linkage as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)`.

### **Stator eddy current loss coefficient, k\_Js(I,B)** — Stator eddy current loss coefficient `zeros(3, 5)` `W/Hz^2` (default)

Eddy current loss coefficient of the stator depending on the current
magnitude and current phase advance. It is used by the Steinmetz
equation.

#### Dependencies

To enable this parameter, set **Model** to
`Specify tabulated Steinmetz
coefficients` and, in the
**Electrical** tab, set **Flux linkage
data format** to either `D and Q axes flux
linkages as a function of peak current magnitude (I), current
advance angle (B), and rotor angle (theta)` or
`A-phase flux linkage as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)`.

### **Stator excess current loss coefficient, k\_es(I,B)** — Stator excess current loss coefficient `zeros(3, 5)` `W/Hz^1.50000` (default)

Excess current loss coefficient of the stator depending on the current
magnitude and current phase advance. It is used by the Steinmetz
equation.

#### Dependencies

To enable this parameter, set **Model** to
`Specify tabulated Steinmetz
coefficients` and, in the
**Electrical** tab, set **Flux linkage
data format** to either `D and Q axes flux
linkages as a function of peak current magnitude (I), current
advance angle (B), and rotor angle (theta)` or
`A-phase flux linkage as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)`.

### **Rotor speed vector, w** — Rotor speed `[1000, 2000]` `rpm` (default)

Vector of rotor speed at which the iron loss is tabulated.

#### Dependencies

To enable this parameter, set **Model** to
`Tabulate with current and speed` and,
in the **Electrical** setting, set **Flux
linkage data format** to either `D and Q
axes flux linkages as a function of D-axis current (iD), Q-axis
current (iQ), and rotor angle (theta)` or
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`.

### **Rotor iron loss table, Pr(id,iq,w)** — Rotor iron loss table `zeros(3, 3, 2)` `W` (default)

Iron losses of the rotor tabulated on the *d*-axis
and *q*-axis currents, and rotor speed.

#### Dependencies

To enable this parameter, set **Model** to
`Tabulate with current and speed` and,
in the **Electrical** setting, set **Flux
linkage data format** to either `D and Q
axes flux linkages as a function of D-axis current (iD), Q-axis
current (iQ), and rotor angle (theta)` or
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`.

### **Stator iron loss table, Ps(id,iq,w)** — Stator iron loss table `zeros(3, 3, 2)` `W` (default)

Iron losses of the stator tabulated on the *d*-axis
and *q*-axis currents, and rotor speed.

#### Dependencies

To enable this parameter, set **Model** to
`Tabulate with current and speed` and,
in the **Electrical** setting, set **Flux
linkage data format** to either `D and Q
axes flux linkages as a function of D-axis current (iD), Q-axis
current (iQ), and rotor angle (theta)` or
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`.

### **Rotor iron loss table, Pr(I,B,w)** — Rotor iron loss table `zeros(3, 5, 2)` `W` (default)

Iron losses of the rotor tabulated on the current magnitude, current
phase advance, and rotor speed.

#### Dependencies

To enable this parameter, set **Model** to
`Tabulate with current and speed` and,
in the **Electrical** setting, set **Flux
linkage data format** to either `D and Q
axes flux linkages as a function of peak current magnitude (I),
current advance angle (B), and rotor angle (theta)`
or `A-phase flux linkage as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)`.

### **Stator iron loss table, Ps(I,B,w)** — Stator iron loss table `zeros(3, 5, 2)` `W` (default)

Iron losses of the stator tabulated on the current magnitude, current
phase advance, and rotor speed.

#### Dependencies

To enable this parameter, set **Model** to
`Tabulate with current and speed` and,
in the **Electrical** setting, set **Flux
linkage data format** to either `D and Q
axes flux linkages as a function of peak current magnitude (I),
current advance angle (B), and rotor angle (theta)`
or `A-phase flux linkage as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)`.

### Mechanical

### **Rotor inertia** — Rotor inertia `0.01` `kg*m^2` (default)

Inertia of the rotor attached to mechanical translational port
**R**. The value can be zero.

### **Rotor damping** — Rotor damping `0` `N*m/(rad/s)` (default)

Rotary damping.

### Temperature Dependence

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Measurement temperature** — Measurement temperature `298.15` `K` (default)

The temperature for which motor parameters are quoted.

### **Resistance temperature coefficient** — Resistance temperature coefficient `3.93e-3` `1/K` (default)

Coefficient α in the equation relating resistance to temperature, as
described in Thermal Model for Actuator Blocks. The default value is for
copper.

### **Permanent magnet flux temperature coefficient** — Permanent magnet flux temperature coefficient `-0.001` (default)

The fractional rate of change of permanent magnet flux density with
temperature. It is used to linearly reduce the torque and the induced
back EMF as temperature rises.

### Thermal Port

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Thermal mass for each stator winding** — Thermal mass for each stator winding `100` `J/K` (default)

The thermal mass value for the A, B, and C windings. The thermal mass
is the energy required to raise the temperature by one degree.

### **Initial stator winding temperatures** — Initial stator winding temperatures `[298.15, 298.15, 298.15]` `K` (default)

A 1-by-3 row vector defining the temperature of the A, B, and C
thermal ports at the start of simulation.

### **Rotor thermal mass** — Rotor thermal mass `200` `J/K` (default)

The thermal mass of the rotor, that is, the energy required to raise
the temperature of the rotor by one degree.

### **Rotor initial temperature** — Rotor initial temperature `298.15` `K` (default)

The temperature of the rotor at the start of simulation.

### **Percentage of main flux path iron losses associated with the rotor** — Percentage of main flux path iron losses associated with the rotor `90` (default)

The percentage of the main flux path iron losses associated with the
magnetic path through the rotor. It determines how much of the iron loss
heating is attributed to the rotor thermal port **HR**,
and how much is attributed to the three winding thermal ports
**HA**, **HB**, and
**HC**.

### **Percentage of cross-tooth flux path iron losses associated with the rotor** — Percentage of cross-tooth flux path iron losses associated with the rotor `30` (default)

The percentage of the cross-tooth flux path iron losses associated
with the magnetic path through the rotor. It determines how much of the
iron loss heating is attributed to the rotor thermal port
**HR**, and how much is attributed to the three
winding thermal ports **HA**, **HB**,
and **HC**.

## Libraries

Simscape / Electrical / Electromechanical / Permanent Magnet

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

### R2024a: Open-end configuration for stator windings

To model the stator windings of the machine in an open-end configuration, set the
**Winding type** parameter to
`Open-end`. The FEM-Parameterized PMSM block then exposes each end
of the windings by enabling the corresponding electrical conserving ports.

## Description

Permanent magnet synchronous motor defined in terms of magnetic flux linkage

The FEM-Parameterized PMSM block models a permanent
magnet synchronous motor (PMSM) defined in terms of magnetic flux linkage. Use this
block to model any three-phase motor that has a permanent magnet rotor such as:

- Axial flux (pancake) motors
- Brushless servomotors
- Motors with interior magnet rotors, such as an interior permanent magnet
  (IPM) motor or an interior permanent magnet synchronous motors
  (IPMSMs)
- Motors with surface-mounted magnet rotors:

  - Surface permanent magnet (SPM) motors or surface permanent magnet
    synchronous motors (SPMSMs)
  - Brushless direct current (BLDC) motors

You parameterize the block by using tabulated data of the motor magnetic
flux as a function of current and rotor angle. This is the way that finite element
method (FEM) packages usually export flux information. Because the block uses tabulated
data, the flux can vary nonlinearly with both rotor angle and current. The nonlinear
dependence on rotor angle enables the block to support trapezoidal flux profiles
exhibited by BLDC motors and also capture the higher harmonics for motors with only
approximately sinusoidal flux profiles.

This figure shows the equivalent circuit for a wye-connected PMSM.

This figure shows the motor construction with a single pole-pair on the rotor. The
rotor angle is zero when the permanent magnet flux aligns with the
*A*-phase magnetic axis.

In practice, the flux linking each of the three windings depends on all three currents
and the rotor angle. Tabulating the flux as a function of four independent variables can
lead to simulation inefficiency and significant memory requirements. The block,
therefore, lets you use the **Modeling option** parameter to specify
how to model the flux and torque:

- 2-D partial derivative data — 2-D table lookup, with options to tabulate in
  terms of current and the rotor angle, or in terms of
  *`d`*-axis and *`q`*-axis
  currents. The first option assumes constant mutual inductance and supports
  nonsinusoidal back electromotive force (EMF) profiles. The second option assumes
  a sinusoidal back EMF and captures saturation effects for IPMSMs.
- 3-D partial derivative data — 3-D table lookup, based on direct current,
  quadrature current, and the rotor angle. You provide the flux lookup data for
  the *a* phase. The block uses Park transform to map the three
  stator winding currents to direct and quadrature currents. This method reduces
  the data complexity compared to the 4-D table lookup and results in improved
  simulation performance.
- 4-D partial derivative data — 4-D table lookup, based on the three stator
  winding currents and the rotor angle. You provide the flux lookup data for the
  *a* phase. This model has higher fidelity than the 2-D and
  3-D partial derivative data models, but it has the most inefficient simulation
  performance and the highest memory requirements.
- 3-D flux linkage data — 3-D table lookup, based on the flux linkage data. You
  can provide the flux linkage data in a variety of formats. The block uses Park
  transform to map the three stator winding currents to direct and quadrature
  currents. This method reduces the data complexity compared to the 4-D table
  lookup and results in improved simulation performance.

Some of the **Modeling option** parameter settings also enable
thermal ports. For more information, see Model Thermal Effects.

By default, the block implements a wye-wound configuration for the stator windings for
all these parameterization methods. However, you can switch to a delta-wound or an
open-end configuration by using the **Winding type** parameter. In the
delta-wound configuration, the *a*-phase connects ports
**a** and **b**, the *b*-phase
between ports **b** and **c** and the
*c*-phase connects ports **c** and
**a**.

**Note**

Simscape™
Electrical™ includes several blocks that can model the same type of motor or actuator.
Choose a block that has sufficient modeling detail for the engineering design questions that
you need to answer. Do not use a block that has more modeling detail than you need, because
higher-fidelity models slow down simulation and are more complex to parameterize.

Blocks like the FEM-Parameterized PMSM block define motor behavior in
terms of flux linkage. These models have a high level of fidelity. Use this block only when you
need a high level of modeling detail, for example, to predict efficiency for traction
applications or to capture torque and electrical current harmonics. For more information about
choosing the right block to model your motor at the right level of fidelity, see Choose Blocks to Model Motors or Actuators.

### 2-D Data Model with Constant Mutual Inductance

In this 2-D flux data model, the flux linking each winding is assumed to depend
nonlinearly only on the current in that same winding, plus the rotor angle. In
practice, this is a reasonable assumption for many permanent magnet synchronous
motors; however, it is less accurate for switched reluctance motors. Given this
assumption, the fluxes in the three windings are:

[ϕaϕbϕc]=[0−Ms−Ms−Ms0−Ms−Ms−Ms0][iaibic]+[ϕ(ia,θr)ϕ(ib,θr−2π/(3N))ϕ(ic,θr−4π/(3N))]

where ϕ(θr,ia) is the flux linkage for the A-phase winding as a function of the
rotor angle and A-phase current. *Θ*r = 0 corresponds to the rotor *`d`*-axis
aligning with the A-phase positive magnetic flux direction.
*M*s is the stator-stator mutual
inductance.

For improved numerical performance, the equations implemented in the block
actually work with the partial derivatives of flux linkage with respect to current, ∂ϕ(i,θr)/∂i, and the rotor angle, ∂ϕ(i,θr)/∂θr, rather than the flux directly. If your FEM package does not
export these partial derivatives, you can determine them using a MATLAB® script. See the Solenoid
Parameterized with FEM Data example model and its supporting MATLAB script for an example of how to do this.

The electrical equations for the block, defined in terms of flux partial
derivatives, are:

va=∂ϕ∂iadiadt+∂ϕ∂θrdθrdt−Ms(dibdt+dicdt)+Rsiavb=∂ϕ∂ibdibdt+∂ϕ∂θrdθrdt−Ms(diadt+dicdt)+Rsibvc=∂ϕ∂icdicdt+∂ϕ∂θrdθrdt−Ms(diadt+dibdt)+Rsic

where

- *v*a,
  *v*b,
  *v*c are the voltages applied to
  the A, B, and C stator windings.
- *i*a,
  *i*b,
  *i*c are the stator currents in
  each of the three windings.
- *R*s is the resistance of each of
  the stator windings.
- *M*s is the stator-stator mutual
  inductance.
- ∂ϕ/∂ia, ∂ϕ/∂ib, ∂ϕ/∂ic are the partial derivatives of flux linkage with respect
  to stator current in each of the three windings.
- ∂ϕ/∂θr is the partial derivative of flux linkage with respect to
  the rotor angle.

The block can automatically calculate the torque matrix from the flux information
that you provide. Alternatively, you can set the **Calculate torque
matrix?** parameter to `No` and directly
specify the torque as a function of current and the rotor angle. See the FEM-Parameterized Rotary Actuator block reference page for more
information.

### 2-D Data Model with Sinusoidal Back EMF

In this 2-D flux data model, the flux linking each winding is assumed to depend
nonlinearly on all stator winding currents, plus it is assumed that the permanent
magnet flux linkage is sinusoidal. Interior magnet PMSMs (or IPMSMs) usually fit
this assumption well. The equations are:

[ϕdϕq]=[Ld(id,iq)Lq(id,iq)][idiq]+[ϕm(id,iq)]

T=32N(iq(idLd(id,iq)+ϕm(id,iq))−idiqLq(id,iq))

where

- *i*d and
  *i*q are the
  *`d`*-axis and *`q`*-axis
  currents, respectively.
- *ϕ*d and
  *ϕ*q are the
  *`d`*-axis and *`q`*-axis
  flux linkages, respectively.
- *ϕ*m is the permanent magnet flux
  linkage.
- *L*d and
  *L*q are the
  *`d`*-axis and *`q`*-axis
  inductances, respectively. They are assumed to depend on the
  *`d`*-axis and *`q`*-axis
  currents.
- *N* is the number of pole pairs.
- *T* is the electrical torque.

### 3-D Partial Derivative Data Model Using Park Transform

Working with four-dimensional data has both a simulation performance cost and a
memory cost. To reduce the table dimension to three-dimensional, the 3-D data model
uses Park transform to map the three currents to direct and quadrature currents:

[idiq]=23[cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)−sin(Nθr)−sin(Nθr−2π3)−sin(Nθr+2π3)][iaibic]

In the general case, Park transform maps to direct, quadrature, and zero-sequence
currents. However, the zero-sequence current is typically small under normal
operating conditions. Therefore, the model neglects the dependence of the flux
linkage terms on zero-sequence current, and determines the flux linkage in terms of
just direct and quadrature currents plus the rotor angle. The flux equation for the
3-D data model is:

[ϕaϕbϕc]=[ϕ(id,iq,θr)ϕ(id,iq,θr−2π/(3N))ϕ(id,iq,θr−4π/(3N))]

The electrical equations for the block are also defined in terms of flux partial
derivatives, similar to the 4-D data model. You can calculate 3-D flux linkage
partial derivative data from 4-D flux linkage data using `ee_calculateFluxPartialDerivatives`.

### 4-D Partial Derivative Data Model

The flux linking each of the windings is a function of the current in that
winding, the currents in the other two windings, and the rotor angle. For full
accuracy, the 4-D flux data model assumes that the flux linkage is a function of the
three currents and the rotor angle, therefore performing four-dimensional table
lookups. The flux equation is:

[ϕaϕbϕc]=[ϕ(ia,ib,ic,θr)ϕ(ib,ic,ia,θr−2π/(3N))ϕ(ic,ia,ib,θr−4π/(3N))]

where

- *ϕ*a,
  *ϕ*b,
  *ϕ*c are the flux linkages for
  the A, B, and C stator windings.
- *i*a,
  *i*b,
  *i*c are the stator currents in
  each of the three windings.
- *Θ*r is the rotor angle. *Θ*r =
  0 corresponds to the case where the permanent magnet flux is
  aligned with the A-phase stator winding flux.
- *N* is the number of pole pairs.

Flux linkage data is assumed cyclic with
*Θ*r. If, for example, the motor has six
pole pairs, then the range for the data is 0 ≤ *Θ*r ≤
60°. You must provide data both at 0 and 60 degrees, and because the
data is cyclic, the flux linkage partial derivatives must be the same at these two
end points.

The torque equation is:

τ=T(ia,ib,ic,θr)

The 4-D data model does not have an option for the block to determine torque from
flux linkage. Because of the increased numerical overhead in the 4-D case, it is
better to precalculate the torque just once, rather than calculate it every time you
run the simulation.

For improved numerical performance, the equations implemented in the block
actually work with the partial derivatives of flux linkage with respect to the three
currents and the rotor angle, rather than the flux directly. If your FEM package
does not export these partial derivatives, you can determine them using `ee_calculateFluxPartialDerivatives`.

The electrical equations for the block, defined in terms of flux partial
derivatives, are:

va=∂ϕa∂iadiadt+∂ϕa∂ibdibdt+∂ϕa∂icdicdt+∂ϕa∂θrdθrdt+Rsiavb=∂ϕb∂iadiadt+∂ϕb∂ibdibdt+∂ϕb∂icdicdt+∂ϕb∂θrdθrdt+Rsibvc=∂ϕc∂iadiadt+∂ϕc∂ibdibdt+∂ϕc∂icdicdt+∂ϕc∂θrdθrdt+Rsic

where

- *v*a,
  *v*b,
  *v*c are the voltages applied to
  the A, B, and C stator windings.
- *i*a,
  *i*b,
  *i*c are the stator currents in
  each of the three windings.
- *R*s is the resistance of each of
  the stator windings.

### 3-D Flux Linkage Data Models

The 3-D flux linkage data options let you work with raw flux linkage data exported
from your finite-element (FE) motor design tool. This is in contrast to the 3-D
partial derivative data options, for which you need to determine the partial
derivatives. You can provide flux linkage data in a variety of formats, to support
different FE tool conventions:

- Tabulate DQ-axes flux linkage data or A-phase flux linkage data — Some
  tools support working with flux linkage resolved into direct (D) and
  quadrature (Q) axes. An advantage of this approach is that data for rotor
  angles in the range 0 to 360/*N*/3 degrees is required
  (where *N* is the number of pole pairs). Other tools work
  directly with A-, B-, and C-phase flux linkages, and for this you can import
  just the A-phase flux linkage, for which the rotor angle range must be in
  the range 0 to 360/*N* degrees. The implicit assumption of
  importing just the A-phase data is that the B and C phase data is the same
  except shifted in phase.
- Tabulate using Cartesian or polar current coordinates — Cartesian
  tabulation implies the flux linkage is tabulated in terms of D-axis current
  and Q-axis current (plus the rotor angle). Alternatively, polar tabulation
  involves tabulating flux linkages in terms of current magnitude, current
  advance angle relative to the Q-axis, and the rotor angle. The advantage of
  polar coordinates is that it more naturally reflects the permitted operating
  currents, thereby avoiding unused table data points.

These conventions result in four **Flux linkage data format**
parameterization options:

- `D and Q axes flux linkages as a function of D-axis current
  (iD), Q-axis current (iQ), and rotor angle (theta)`
- `D and Q axes flux linkages as a function of peak current
  magnitude (I), current advance angle (B), and rotor angle
  (theta)`
- `A-phase flux linkage as a function of D-axis current (iD),
  Q-axis current (iQ), and rotor angle (theta)`
- `A-phase flux linkage as a function of peak current magnitude
  (I), current advance angle (B), and rotor angle
  (theta)`

The FEM-Parameterized PMSM block requires 3-D flux linkage data. To convert 2-D flux linkage
data, `F(id,iq)`, into a 3-D table, `F(id,iq,x)`,
use the `repmat` function.

Besides selecting the flux linkage data format used by your FE tool, you have to
select the version of Park transform used by the tool. The four conventions are
described below and correspond to the four options for the **Park’s
convention for tabulated data** drop-down menu.

**Note**

When looking at logged values for D- and Q-axis currents, keep in mind that
for each of these options, the format is converted, as needed, so that
internally the FEM-Parameterized PMSM block
consistently uses Option 1.

**Note**

To preserve higher-order harmonics due to the permanent magnet back EMF,
provide the A-phase flux data rather than the D-axis and Q-axis flux data.
Conversely, if you provide D-axis and Q-axis fluxes, the Park's transform
removes the higher-order harmonics. Working with D and Q fluxes is sufficient
for many applications, particularly if you set the **Winding
type** parameter to `Wye-wound` and there
aren't connections to the neutral port of this block. For this particular case,
the constraint that the sum of the currents is zero at the neutral port removes
all third-order harmonics.

**Option 1. Q leads D, rotor angle measured from A-phase to D-axis**

This is the Park’s convention used internally by Simscape
Electrical motor and machine blocks. All other options are converted into
this format.

- *N*: number of pole pairs
- *θ*r: rotor angle
- *i*d,
  *i*q: D-axis and Q-axis
  currents
- *i*p: Current magnitude = id2+iq2
- *β*: Current advance angle = tan−1(−id/iq)

Corresponding Park transform is

[idiqi0]=23[cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)−sin(Nθr)−sin(Nθr−2π3)−sin(Nθr+2π3)121212][iaibic]

where *i*a,
*i*b, and
*i*c are the A-phase, B-phase, and
C-phase currents, respectively.

**Option 2. Q leads D, rotor angle measured from A-phase to Q-axis**

- *N*: number of pole pairs
- *θ*r: rotor angle
- *i*d,
  *i*q: D-axis and Q-axis
  currents
- *i*p: Current magnitude = id2+iq2
- *β*: Current advance angle = tan−1(−id/iq)

Corresponding Park transform is

[idiqi0]=23[sin(Nθr)sin(Nθr−2π3)sin(Nθr+2π3)cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)121212][iaibic]

where *i*a,
*i*b, and
*i*c are the A-phase, B-phase, and
C-phase currents, respectively.

**Option 3. D leads Q, rotor angle measured from A-phase to D-axis**

- *N*: number of pole pairs
- *θ*r: rotor angle
- *i*d,
  *i*q: D-axis and Q-axis
  currents
- *i*p: Current magnitude = id2+iq2
- *β*: Current advance angle = tan−1(−id/iq)

Corresponding Park transform is

[idiqi0]=23[cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)sin(Nθr)sin(Nθr−2π3)sin(Nθr+2π3)121212][iaibic]

where *i*a,
*i*b, and
*i*c are the A-phase, B-phase, and
C-phase currents, respectively.

**Option 4. D leads Q, rotor angle measured from A-phase to Q-axis**

- *N*: number of pole pairs
- *θ*r: rotor angle
- *i*d,
  *i*q: D-axis and Q-axis
  currents
- *i*p: Current magnitude = id2+iq2
- *β*: Current advance angle = tan−1(−id/iq)

Corresponding Park transform is

[idiqi0]=23[−sin(Nθr)−sin(Nθr−2π3)−sin(Nθr+2π3)cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)121212][iaibic]

where *i*a,
*i*b, and
*i*c are the A-phase, B-phase, and
C-phase currents, respectively.

### Calculating Iron Losses

The FEM-Parameterized PMSM block models iron losses
according to the parameterization methods you choose for flux and torque.

These iron losses produce heat. The block injects the heat from rotor iron losses
into the **HR** thermal port that represents the rotor thermal mass. The
block splits the stator iron losses in three equal parts and injects each part into
the stator winding thermal ports, **HA**, **HB**, and
**HC**.

**Specify open-circuit and short-circuit loss data (permanent magnet motors
only)**

For the **2-D partial derivative data**,
**3-D partial derivative data**, and **4-D
partial derivative data** options, with or without thermal
ports, the iron loss model is based on the work of Mellor [1]. Iron losses are divided into two terms, one representing the main
magnetizing path, and the other representing the cross-tooth tip path that
becomes active during field weakened operation.

The term representing the main magnetizing path depends on the induced RMS
stator voltage, Vmrms:

POC(Vmrms)=ahkVmrms+ajk2Vmrms2+aexk1.5Vmrms1.5.

This is the dominant term during no-load operation. *k* is
the back EMF constant relating RMS volts per Hz. It is defined as k=Vmrms/f, where *f* is the electrical frequency. The
first term on the right-hand side is the magnetic hysteresis loss, the second is
the eddy current loss and the third is the excess loss. The three coefficients
appearing on the numerators are derived from the values that you provide for the
open-circuit hysteresis, eddy, and excess losses.

The term representing the cross-tooth tip path becomes important when a
demagnetizing field is set up and can be determined from a finite element
analysis short-circuit test. It depends on the RMS EMF associated with the
cross-tooth tip flux, Vdrms\*:

PSC(Vdrms\*)=bhkVdrms\*+bjk2Vdrms\*2+bexk1.5Vdrms\*1.5.

The three numerator terms are derived from the values you provide for the
short-circuit hysteresis, eddy, and excess losses.

**Steinmetz parameterization method**

For the **3-D flux linkage data** with or without
thermal ports, you can also model the iron losses based on the Steinmetz
equation. The Steinmetz method scales for different motor speeds or electrical
frequencies so that iron loss data is only required as function of motor
currents.

If, in the **Iron Losses** setting, you set the
**Model** parameter to `Specify open and short
circuit loss data (permanent magnet motors only)`, the block
uses the Steinmetz method, but assumes constant coefficients and no dependency
on peak current and current phase advance. Select this option if you have dyno
measurements or if you perform an FE analysis to get the iron losses from just
open-circuit and short-circuit simulations.

Conversely, if you set the **Flux linkage data format**
parameter to either `D and Q axes flux linkages as a function of
peak current magnitude (I), current advance angle (B), and rotor angle
(theta)` or `A-phase flux linkage as a function of
peak current magnitude (I), current advance angle (B), and rotor angle
(theta)` , then the block tabulated the coefficients with the
**Peak current magnitude vector, I** and **Current
advance angle vector, B** parameters, so that the iron losses are
given by:

Protor(f)=khr(Ip,β)f+kJr(Ip,β)f2+ker(Ip,β)f1.5Pstator(f)=khs(Ip,β)f+kJs(Ip,β)f2+kes(Ip,β)f1.5

where:

- *f* is the electrical instantaneous frequency, in
  `Hz`, and is equal to the rotor
  mechanical speed multiplied by the number of pole pairs. This
  frequency is a variable that changes over time.
- *khr(Ip,β)*
  is the **Rotor hysteresis loss coefficient,
  k\_hr(I,B)**.
- *kJr(Ip,β)*
  is the **Rotor eddy current loss coefficient,
  k\_Jr(I,B)**.
- *ker(Ip,β)*
  is the **Rotor excess current loss coefficient,
  k\_er(I,B)**.
- *khs(Ip,β)*
  is the **Stator hysteresis loss coefficient,
  k\_hs(I,B)**.
- *kJs(Ip,β)*
  is the **Stator eddy current loss coefficient,
  k\_Js(I,B)**.
- *kes(Ip,β)*
  is the **Stator excess current loss coefficient,
  k\_es(I,B)**.

Similarly, if you set the **Flux linkage data format**
parameter to either `D and Q axes flux linkages as a function of
D-axis current (iD), Q-axis current (iQ), and rotor angle
(theta)` or `A-phase flux linkage as a function of
D-axis current (iD), Q-axis current (iQ), and rotor angle
(theta)`, then the iron losses are given by:

Ploss,rotor(f)=khr(id,iq)f+kJr(id,iq)f2+ker(id,iq)f1.5Ploss,stator(f)=khs(id,iq)f+kJs(id,iq)f2+kes(id,iq)f1.5

where:

- *khr(id,iq)*
  is the **Rotor hysteresis loss coefficient,
  k\_hr(id,iq)**.
- *kJr(id,iq)*
  is the **Rotor eddy current loss coefficient,
  k\_Jr(id,iq)**.
- *ker(id,idq)*
  is the **Rotor excess current loss coefficient,
  k\_er(id,iq)**.
- *khs(id,iq)*
  is the **Stator hysteresis loss coefficient,
  k\_hs(id,iq)**.
- *kJs(id,iq)*
  is the **Stator eddy current loss coefficient,
  k\_Js(id,iq)**.
- *kes(id,iq)*
  is the **Stator excess current loss coefficient,
  k\_es(id,iq)**.

Select this option only in conjunction with a motor design tool
that can calculate the coefficients. You can export the Steinmetz coefficients
lookup tables in Cartesian coordinates
(*id*,*iq*)
or radial coordinates
(*Ip*,*β*) by using
FEM tools such as Motor-CAD or ANSYS® Maxwell®. These coefficients are
valid for a range of currents and frequencies. To obtain the right value based
on the current state of the machine, this block interpolates the Steinmetz
coefficient value at run-time.

For more information about importing Steinmetz coefficients from FEM tools,
see the Import IPMSM Flux Linkage Data from Motor-CAD example.

**Tabulate with current and speed**

For the **3-D flux linkage data** with or without
thermal ports, you can also model the iron losses by tabulating them
independently for rotor and stator.

If you set the **Flux linkage data format** parameter to
either `D and Q axes flux linkages as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)` or `A-phase flux linkage as a function of
peak current magnitude (I), current advance angle (B), and rotor angle
(theta)`, the block tabulated the iron losses with the
**Peak current magnitude vector, I** and **Current
advance angle vector, B** parameters, so that the iron losses are
given by:

Ploss(Ip,β,w)=tablelookup(Ptable,Ip,β,w)

where *w* is the **Rotor speed
vector, w** parameter.

Similarly, if you set the **Flux linkage data format**
parameter to either `D and Q axes flux linkages as a function of
D-axis current (iD), Q-axis current (iQ), and rotor angle
(theta)` or `A-phase flux linkage as a function of
D-axis current (iD), Q-axis current (iQ), and rotor angle
(theta)`, then the iron losses are given by:

Ploss(id,iq,w)=tablelookup(Ptable,id,iq,w).

### Model Thermal Effects

You can expose thermal ports to model the effects of losses that convert power to heat. To
expose the thermal ports, set the **Modeling option** parameter to either:

- `2-D partial derivative data | No thermal port` — 2-D
  table lookup parameterization, with options to tabulate in terms of current and
  rotor angle, but without thermal ports.
- `2-D partial derivative data | Show thermal port` —
  2-D table lookup parameterization, with options to tabulate in terms of current
  and rotor angle, and with thermal ports.
- `3-D partial derivative data | No thermal port` — 3-D
  table lookup parameterization, based on direct current, quadrature current, and
  rotor angle, but without thermal ports.
- `3-D partial derivative data | Show thermal port` —
  3-D table lookup parameterization, based on direct current, quadrature current,
  and rotor angle, and with thermal ports.
- `4-D partial derivative data | No thermal port` — 4-D
  table lookup parameterization, based on the three stator winding currents and
  the rotor angle, but without thermal ports.
- `4-D partial derivative data | Show thermal port` —
  4-D table lookup parameterization, based on the three stator winding currents
  and the rotor angle, and with thermal ports.
- `3-D flux linkage data | No thermal port` — 3-D table
  lookup parameterization, based on the flux linkage data without thermal
  ports.
- `3-D flux linkage data | Show thermal port` — 3-D
  table lookup parameterization, based on the flux linkage data with thermal
  ports.

For more information about using thermal ports in actuator blocks, see Simulating Thermal Effects in Rotational and Translational Actuators.

**Temperature Dependency for Permanent Magnet Flux**

To calculate the temperature dependence of the permanent magnet, the block
uses the **Permanent magnet flux temperature coefficient**
parameter, *αflux*. This parameter
determines how much the motor flux decreases for each increase of degree of
temperature. The block calculates the flux reduction factor by using this equation:

FluxReductionForTemp=1+αflux⋅(TR−Tmeas),

where *TR* is the
temperature at the **HR** port and
*Tmeas* is the value of the
**Measurement temperature** parameter. In this block, the
flux decreases linearly with the temperature. This decrease causes the back EMF
and torque to also decrease linearly with the temperature by the same amount,

EMF=FluxReductionForTemp⋅EMF0τ=FluxReductionForTemp⋅τ0

where:

- *τ0* is the torque when
  the rotor temperature is equal to the value of the
  **Measurement temperature** parameter.
- *EMF0* is the EMF when the
  rotor temperature is equal to the value of the **Measurement
  temperature** parameter.

After adjusting the torque based on the temperature, the block
further reduces the torque, *τ*, based on the iron
losses.

**Temperature Dependency for Stator Resistance**

The increase in temperature in the permanent magnet changes the stator
resistance. The **Resistance temperature coefficient**
parameter, *α*, drives this change of the resistance:

Ra=Rs⋅[1+α(TA−Tmeas)]Rb=Rs⋅[1+α(TB−Tmeas)]Rc=Rs⋅[1+α(TC−Tmeas)]

where *Ra*,
*Rb*, and
*Rc* are the
temperature-adjusted resistances at each phase and
*TA*,
*TB*, and
*TC* are the temperatures at the
**HA**, **HB**, and
**HC** ports.
