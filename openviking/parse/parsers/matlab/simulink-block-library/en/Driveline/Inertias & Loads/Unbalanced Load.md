---
type: simulink-block
title: 'Unbalanced Load'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Inertias & Loads'
documentation_page: 'unbalancedload'
documentation_source_path: 'ref/unbalancedload.html'
language: en
---

# Unbalanced Load

## Ports

### Conserving

### **LConn 1** — Shaft connection mechanical rotational

Mechanical rotational conserving port associated with the shaft
connection to the unbalanced load.

## Parameters

### **Parameterization** — Option to model moment of inertia `Circular rotation` (default) | `Elliptical rotation` | `By table lookup`

Choice of parameterization for modeling the moment of inertia of the
unbalanced load. Select `Circular rotation` or
`Elliptical rotation` to parameterize the load
inertia in terms of the load’s rotation path. Select `By table
lookup` to provide the load inertia directly across its
rotation path.

### **Moment of inertia about own axis** — Moment of inertia `1` `kg*m^2` (default) | positive scalar

Constant moment of inertia about the intrinsic rotation axis of the
unbalanced load.

#### Dependencies

To enable this parameter, set **Parameterization** to
`Circular rotation`.

### **Mass** — Load mass `1` `kg` (default) | positive scalar

Mass of the unbalanced load.

#### Dependencies

To enable this parameter, set **Parameterization** to
`Circular rotation`.

### **Distance from axis to center of rotation** — Offset radius `.01` `m` (default) | positive scalar

Distance between the main rotation axis and the center of the rotation
path.

#### Dependencies

To enable this parameter, set **Parameterization** to
`Circular rotation`.

### **Radius of rotation** — Radius of rotation `.01` `m` (default) | positive scalar

Radius of the circular rotation path traversed by the unbalanced
load.

#### Dependencies

To enable this parameter, set **Parameterization** to
`Circular rotation`.

### **Radius of rotation inline with distance from axis** — Semimajor radius `.01` `m` (default) | positive scalar

Length of the semimajor axis of the elliptical rotation path traversed by
the unbalanced load. The semimajor axis is in line with the line segment
joining the main rotation axis and the elliptical rotation center.

#### Dependencies

To enable this parameter, set **Parameterization** to
`Elliptical rotation`.

### **Radius of rotation perpendicular to distance from axis** — Semiminor radius `.005` `m` (default) | positive scalar

Length of the semiminor axis of the elliptical rotation path traversed by
the unbalanced load. The semiminor axis is perpendicular to the line segment
joining the main rotation axis and the elliptical rotation center.

#### Dependencies

To enable this parameter, set **Parameterization** to
`Elliptical rotation`.

### **Angle vector** — Angle `[0, pi, 3 * pi / 2]` `rad` (default) | vector

Array of angular positions at which to specify the load inertia. The block
calculates the load inertia between the angles specified using linear
interpolation.

#### Dependencies

To enable this parameter, set **Parameterization** to
`By table lookup`.

### **Inertia vector** — Inertia `[1, 10, 1]` `kg*m^2` (default) | vector

Array of load inertias about the intrinsic rotation axis of the load. Each
inertia corresponds to an angle specified in the **Angle
vector** parameter.

#### Dependencies

To enable this parameter, set **Parameterization** to
`By table lookup`.

## Libraries

Simscape / Driveline / Inertias & Loads

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015b**

## Description

Load with angle-dependent rotational inertia

The Unbalanced Load block represents the effects of a
load whose rotational inertia varies with the rotation angle. Examples include the
wobbling of a spinning axle and shaking of an off-center rotating machine. You can
specify the load inertia in terms of its rotation path or as an angle-inertia lookup
table.

The block provides two rotation path parameterizations. One assumes circular motion of
the unbalanced load. The other assumes elliptical motion. In each case, the distance
between the unbalanced load and the main rotation axis varies with the rotation angle.
The varying distance causes the moment of inertia, given by the parallel-axis theorem,
to vary during rotation:

I(θ)=I0+Mr2(θ),

where:

- *I* is the moment of inertia about the main rotation
  axis.
- *I*0 is the moment of inertia
  about the intrinsic rotation axis of the unbalanced load.
- *M* is the total mass of the unbalanced load.
- *r* is the distance between the unbalanced load and the
  main rotation axis.

The angle dependence of the moment of inertia leads to an angle dependence of the
inertial torque acting on the unbalanced load:

TI(θ)=I(θ)ω˙,

where:

- *T*I is the inertial
  torque.
- *ω* is the angular velocity of the load.

If the load moves in a circular path, its distance to the main rotation axis is given by

r(θ)=(rCcos(θ)+rA)2+(rCsin(θ))2,

where:

- *r*A is the distance between the
  main rotation axis and the offset rotation axis.
- *r*C is the radius of the circular
  path.

**Circular Rotation Path**

If the load moves in an elliptical path, its distance to the main rotation axis is
given by

r(θ)=(r∥cos(θ)+rA)2+(r⊥sin(θ))2,

where:

- *r*∥ is the radius of the
  elliptical path in line with the distance from the main rotation
  axis.
- *r*⊥ is radius of the elliptical
  path perpendicular to the distance from the main rotation axis.

**Elliptical Rotation Path**
