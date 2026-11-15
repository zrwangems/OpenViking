---
type: simulink-block
title: 'Belt Drive'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Driveline Modeling / Power Transmission Using Pulley Networks'
documentation_page: 'beltdrive'
documentation_source_path: 'ref/beltdrive.html'
language: en
---

# Belt Drive

## Ports

### Conserving

### **A** — Pulley A shaft mechanical rotational

Mechanical rotational conserving port associated with the shaft of
pulley A.

### **B** — Pulley B shaft mechanical rotational

Mechanical rotational conserving port associated with the shaft of
pulley B.

## Parameters

### Belt

### **Drive type** — Belt drive configuration `Open belt` (default) | `Crossed belt`

Belt drive configuration. For more information, see Belt Drive Diagrams.

### **Belt type** — Belt parameterization `Ideal - No slip` (default) | `Flat belt` | `V-belt`

Belt type selection. The belt type affects slip conditions

- `Ideal - No slip` — Parameterize
  an ideal belt, which does not slip relative to the
  pulley.
- `Flat belt` — Parameterize a belt
  with a rectangular cross-section.
- `V-belt`— Parameterize a belt
  with a V-shaped cross-section.

### **Compliance** — Compliance option `No compliance - Suitable for HIL simulation` (default) | `Specify stiffness and damping`

Option to simulate compliance.

- `No compliance - Suitable for HIL
  simulation` — Simulates a noncompliant belt
  that does not yield elastically when subjected to a force.
  To prioritize performance, select this option.
- `Specify stiffness and damping` —
  Simulates a compliant belt that does yield elastically when
  subjected to a force. To prioritize fidelity, select this
  option.

#### Dependencies

To enable this parameter, set **Belt type** to
`Ideal - No slip`.

### **V-belt sheave angle** — Sheave angle `30` `deg` (default) | nonnegative scalar

Sheave angle of the V-belt.

#### Dependencies

To enable this parameter, set **Belt type** to
`V-belt`.

### **Number of V-belts** — Number of belts `1` (default) | positive scalar integer

Number of V-belts.

The block rounds noninteger values to the nearest integer. Increasing
the number of belts increases the friction force, effective mass per
unit length, and maximum allowable tension.

#### Dependencies

To enable this parameter, set **Belt type** to
`V-belt`.

### **Centrifugal force** — Centrifugal force option `Do not model centrifugal force - Suitable for HIL simulation` (default) | `Model centrifugal force`

Option to include the effects of centrifugal force. If you set this
parameter to `Model centrifugal force`,
centrifugal force saturates to approximately 90% of the value of the
force on each belt end.

#### Dependencies

To enable this parameter, set **Belt type** to
`Flat belt` or
`V-belt`.

### **Belt mass per unit length** — Mass per unit length `0.6` `kg/m` (default) | positive scalar

Centrifugal force contribution in terms of linear density.

#### Dependencies

To enable this parameter, set **Belt type** to
`Flat belt` or
`V-belt` and **Centrifugal
force** to `Model centrifugal
force`.

### **Longitudinal stiffness** — Belt effective stiffness `1e4` `N/m` (default) | nonnegative scalar

Effective stiffness of the belt.

#### Dependencies

To enable this parameter, set **Belt type** to
`Ideal - No slip` and
**Compliance** to `Specify
stiffness and damping` or set **Belt
type** to `Flat belt` or
`V-belt`.

### **Longitudinal damping** — Belt effective damping `1e3` `N/(m/s)` (default) | nonnegative scalar

Effective damping of the belt.

To enable this parameter, either set

- **Belt type** to `Ideal - No
  slip` and **Compliance**
  to `Specify stiffness and damping`,
  or
- **Belt type** to `Flat
  belt` or
  `V-belt`

### **Pre-tension** — Resting belt tension `100` `N` (default) | positive scalar

Tension in the belt when the belt and pulleys are at rest. The value
must be positive.

To enable this parameter, either set

- **Belt type** to `Ideal - No
  slip` and **Compliance**
  to `Specify stiffness and damping`,
  or
- **Belt type** to `Flat
  belt` or
  `V-belt`

### **Maximum tension** — Tension threshold option `No maximum tension` (default) | `Specify maximum tension`

Option to specify a maximum tension. If you set this parameter to
`Specify maximum tension` and the belt
tension on either end of the belt meets or exceeds the value that you
specify for the **Belt maximum tension** parameter, the
simulation stops and generates an assertion error.

#### Dependencies

To enable this parameter, either set

- **Belt type** to `Ideal -
  No slip` and
  **Compliance** to
  `Specify stiffness and
  damping`, or
- **Belt type** to `Flat
  belt` or
  `V-belt`

### **Belt maximum tension** — Maximal tension threshold `1e5` `N` (default) | positive scalar

Maximum allowable tension for each belt. When the tension on either
end of the belt meets or exceeds this value, the simulation stops and
generates an assertion error.

To enable this parameter, either set

- **Belt type** to `Ideal - No
  slip`, **Compliance** to
  `Specify stiffness and
  damping`, and **Maximum
  tension** to `Specify maximum
  tension`, or
- **Belt type** to `Flat
  belt` or `V-belt`
  and **Maximum tension** to
  `Specify maximum
  tension`

### Pulley A

### **Pulley radius** — Pulley radius `.15` `m` (default) | positive scalar

Radius of the pulley.

### **Bearing viscous friction coefficient** — Bearing viscous friction `0` `N*m/(rad/s)` (default) | scalar

Viscous friction associated with the bearings that hold the axis of
the pulley.

### **Inertia** — Rotational inertia `No inertia` (default) | `Specify inertia and initial velocity`

Option to parameterize rotational inertia with an initial
velocity.

### **Pulley inertia** — Pulley inertia `0.01` `kg*m^2` (default) | positive scalar

Rotational inertia of the pulley.

#### Dependencies

To enable this parameter, set **Inertia** to
`Specify inertia and initial
velocity`.

### **Pulley initial velocity** — Initial pulley rotational velocity `0` `rad/s` (default) | scalar

Initial rotational velocity of the pulley.

#### Dependencies

To enable this parameter, set **Inertia** to
`Specify inertia and initial
velocity`.

### Pulley B

### **Pulley radius** — Pulley radius `.30` `m` (default) | positive scalar

Radius of the pulley.

### **Bearing viscous friction coefficient** — Bearing viscous friction `0.001` `N*m/(rad/s)` (default) | scalar

Viscous friction associated with the bearings that hold the axis of
the pulley.

### **Inertia** — Rotational inertia `No inertia` (default) | `Specify inertia and initial velocity`

Option to parameterize rotational inertia with an initial
velocity.

### **Pulley inertia** — Pulley inertia `0.03` `kg*m^2` (default) | positive scalar

Rotational inertia of the pulley.

#### Dependencies

To enable this parameter, set **Inertia** to
`Specify inertia and initial
velocity`.

### **Pulley initial velocity** — Initial pulley rotational velocity `0` `rad/s` (default) | scalar

Initial rotational velocity of the pulley.

#### Dependencies

To enable this parameter, set **Inertia** to
`Specify inertia and initial
velocity`.

### Contact

To enable these settings, set **Belt type** to `Flat
belt` or `V-belt`.

### **Friction model** — Friction method selection `Modal` (default) | `Continuous`

Option to parameterize continuous or modal friction.

### **Pulley A initial state** — Initial state of pulley A `Unlocked` (default) | `Locked`

Option to initialize the simulation with pulley A locked or
unlocked.

#### Dependencies

To enable this parameter, set **Friction model**
to `Modal`.

### **Pulley B initial state** — Initial state of pulley B `Unlocked` (default) | `Locked`

Option to initialize the simulation with pulley B locked or
unlocked.

#### Dependencies

To enable this parameter, set **Friction model**
to `Modal`.

### **Static friction coefficient** — Static friction coefficient `0.5` (default) | positive scalar

Belt friction while maintaining static contact.

#### Dependencies

To enable this parameter, set **Friction model**
to `Modal`.

### **Kinetic friction coefficient** — Kinetic friction coefficient `0.42` (default) | positive scalar

Belt friction while slipping.

#### Dependencies

To enable this parameter, set **Friction model**
to `Modal`.

### **Contact friction coefficient** — Contact friction coefficient `0.5` (default) | positive scalar

Coulomb friction coefficient between the belt and the pulley
surface.

#### Dependencies

To enable this parameter, set **Friction model**
to `Continuous`.

### **Wrap angle calculation** — Angle calculation type `Specify pulley center separation` (default) | `Specify wrap angles`

Option to calculate the wrap angle by the pulley center separation or
to specify those values directly.

- `Specify pulley center
  separation` — The block calculates the wrap
  angle of the belt on the pulleys by using the pulley radii,
  center separation, and drive type.
- `Specify wrap angles` — The block
  uses the wrap angles that you specify.

### **Pulley center separation** — Pulley center separation distance `0.5` `m` (default) | positive scalar

Distance between the centers of the pulleys.

#### Dependencies

To enable this parameter, set **Wrap angle
calculation** to `Specify pulley center
separation`.

### **Pulley A wrap angle** — Pulley wrap angle `145` `deg` (default) | scalar

Angle of contact between the belt and pulley attached to port
**A**.

#### Dependencies

To enable this parameter, set **Wrap angle
calculation** to `Specify wrap
angles`.

### **Pulley B wrap angle** — Pulley wrap angle `215` `deg` (default) | scalar

Angle of contact between the belt and pulley attached to port
**B**.

#### Dependencies

To enable this parameter, set **Wrap angle
calculation** to `Specify wrap
angles`.

### **Velocity threshold** — Contact threshold `0.001` `m/s` (default) | positive scalar

Relative velocity required for peak kinetic friction in the contact.
The friction velocity threshold improves the numerical stability of the
simulation by ensuring that the force is continuous when the direction
of the velocity changes.

### **Force threshold** — Force threshold `0.01` `N` (default) | positive scalar

Relative force required for peak kinetic friction in the
contact.

#### Dependencies

To enable this parameter, set **Belt type** to
`Flat belt` or
`V-belt`.

## Libraries

Simscape / Driveline / Couplings & Drives

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012a**

## Description

Power transmission system with taut belt connecting two pulleys

The Belt Drive block represents a pair of pulleys
connected with a flexible ideal, flat, or V-shaped belt. When you set **Belt
type** to `Ideal - No slip`, the belt does not
slip relative to the pulley surfaces.

The block accounts for friction between the flexible belt and the pulley periphery. If
the friction force is not sufficient to drive the load, the block allows slip. The
relationship between the tensions in the driving and driven branches conforms to the
capstan equation, also known as the Euler-Eytelwein equation. The block accounts for
centrifugal loading in the flexible belt, pulley inertia, and bearing friction.

The Belt Drive block is a structural component based on
the Simscape™
Driveline™
Belt Pulley block and Simscape
Translational Spring and
Translational Damper
blocks.

The Translational Spring and
Translational Damper blocks simulate the compliance
of the belt. For the equations governing the contact dynamics between the belt and the
pulley, see the Belt Pulley block. The figure shows
the functional block diagram for the Belt Drive block.

To learn more about the construction of the block, see About Composite Components and the reference pages for the individual component blocks.

### Equations

The diagrams show the open and crossed belt drive configurations. When you set
**Drive type** to `Open belt`, both
pulleys tend to rotate in the same direction and the larger pulley has a larger belt
wrap angle. When you set **Drive type** to `Crossed
belt`, the pulleys tend to rotate in opposite directions and have
the same wrap angle.

**Belt Drive Diagrams**

The figures and equations refer to these quantities:

- *θA* is the wrap angle of pulley A.
- *θB* is the wrap angle of pulley B.
- *RA* is the effective radius of pulley A.
- *RB* is the effective radius of pulley B.
- *C* is the distance between the centers of pulleys A and
  B.

**Open Belt**

When you set **Drive type** to `Open
belt`, the block calculates the wrap angle of the belt around
each pulley as:

θA=π+2∗sin−1RA−RBC,θB=π−2∗sin−1RA−RBC

The diagram shows the wrap angles and parameters.

**Crossed Belt**

When you set **Drive type** to `Crossed
belt`, the two wrap angles are equal and the wrap angle of the
belt around each pulley:

θA=θB=π+2∗sin−1RA+RBC.

The diagram shows the wrap angles and parameters.
