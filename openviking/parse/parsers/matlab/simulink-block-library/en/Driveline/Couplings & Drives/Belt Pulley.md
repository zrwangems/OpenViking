---
type: simulink-block
title: 'Belt Pulley'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'beltpulley'
documentation_source_path: 'ref/beltpulley.html'
language: en
---

# Belt Pulley

## Ports

### Conserving

### **S** — Pulley shaft angular velocity mechanical rotational

Mechanical rotational conserving port associated with the angular velocity of the pulley
shaft.

### **A** — Belt end A linear velocity mechanical translational

Mechanical translational conserving port associated with the linear
velocity of belt end A.

### **B** — Belt end B linear velocity mechanical translational

Mechanical translational conserving port associated with the linear
velocity of belt end B.

### **C** — Pulley center linear velocity mechanical translational

Mechanical translational conserving port associated with pulley translation. The pulley
moves in the plane and along the bisect of the pulley wrap angle. When
the relative velocity is positive, the pulley center moves.

#### Dependencies

To enable this port, select **Pulley translation**.

## Parameters

### Belt

### **Belt type** — Belt parameterization `Ideal - No slip` (default) | `Flat belt` | `V-belt`

Belt type selection. The belt type affects slip conditions.

- `Ideal - No slip` — Parameterize
  an ideal belt that does not slip relative to the
  pulley.
- `Flat belt` — Parameterize a belt
  with a rectangular cross-section.
- `V-belt`— Parameterize a belt
  with a V-shaped cross-section.

### **V-belt sheave angle** — Sheave angle `30` `deg` (default) | positive scalar

Sheave angle of the V-belt.

#### Dependencies

To enable this parameter, set **Belt type** to
`V-belt`.

### **Number of V-belts** — Number of belts `1` (default) | positive scalar integer

Number of V-belts.

The block rounds noninteger values to the nearest integer. Increasing the number of
belts increases the effective mass per unit length and maximum allowable
tension.

#### Dependencies

To enable this parameter, set **Belt type** to
`V-belt`.

### **Centrifugal force** — Centrifugal force option `Do not model centrifugal force - Suitable for HIL simulation` (default) | `Model centrifugal force`

Option to include the effects of centrifugal force. If you set this parameter to
`Model centrifugal force`, centrifugal
force saturates to approximately 90% of the value of the force on each
belt end.

#### Dependencies

To enable this parameter, set **Belt type** to
`Flat belt` or
`V-belt`.

### **Belt mass per unit length** — Mass per unit length `0.6` `kg/m` (default) | positive scalar

Centrifugal force contribution in terms of linear density expressed as
mass per unit length.

#### Dependencies

To enable this parameter, set **Belt type** to `Flat
belt` or `V-belt` and
**Centrifugal force** to `Model
centrifugal force`.

### **Belt direction** — Initial relative motion direction of the belt end `Ends move in opposite direction` (default) | `Ends move in same direction`

Relative direction of translational motion of one belt end with
respect to the other.

### **Maximum tension** — Tension threshold option `No maximum tension` (default) | `Specify maximum tension`

Option to specify a maximum tension. If you select `Specify maximum
tension` and the belt tension on either end of the belt
meets or exceeds the value that you specify for the **Belt
maximum tension** parameter, the simulation stops and
generates an assertion error.

### **Belt maximum tension** — Maximal tension threshold `1e5` `N` (default) | positive scalar

Maximum allowable tension for each belt. When the tension on either
end of the belt meets or exceeds this value, the simulation stops and
generates an assertion error.

#### Dependencies

To enable this parameter, set **Maximum tension**
to `Specify maximum tension`.

### **Tension warning** — Slack threshold reporting `Do not check tension` (default) | `Warn if leading end loses tension`

Whether the block generates a warning when the tension at either end
of the belt falls below zero.

**Note**

When combining Belt Pulley blocks
with Rope blocks to form loops, set
the Belt Pulley block
**Tension warning** parameter to
`Do not check tension` and set the
Rope block **Tension
warning** parameter to `Warn if rope loses
tension`.

### Pulley

### **Pulley translation** — Option to allow linear motion `off` (default) | `on`

Whether to allow the pulley to translate. Selecting this parameter enables port
**C**.

### **Pulley radius** — Pulley radius `.15` `m` (default) | positive scalar

Radius of the pulley.

### **Bearing viscous friction coefficient** — Bearing viscous friction `0.001` `N*m/(rad/s)` (default) | scalar

Viscous friction associated with the bearings that hold the axis of
the pulley.

### **Inertia** — Rotational inertia `No inertia` (default) | `Specify inertia and initial velocity`

Option to parameterize the rotational inertia with an initial velocity.

### **Pulley inertia** — Pulley inertia `0.01` `kg*m^2` (default) | positive scalar

Rotational inertia of the pulley.

#### Dependencies

To enable this parameter, set **Inertia** to
`Specify inertia and initial
velocity`.

### **Pulley initial rotational velocity** — Initial pulley rotational velocity `0` `rad/s` (default) | scalar

Initial rotational velocity of the pulley.

#### Dependencies

To enable this parameter, set **Inertia** to
`Specify inertia and initial
velocity`.

### **Pulley mass** — Pulley mass `0.01` `kg` (default) | positive scalar

Pulley mass for the inertia calculation.

#### Dependencies

To enable this parameter,

- Select **Pulley translation**
- Set **Inertia** to
  `Specify inertia and initial
  velocity`

### **Pulley initial translational velocity** — Initial pulley rotational velocity `0` `m/s` (default) | scalar

Initial translational velocity of the pulley.

#### Dependencies

To enable this parameter,

- Select **Pulley translation**
- Set **Inertia** to
  `Specify inertia and initial
  velocity`

### Contact

To enable these settings, set **Belt type** to `Flat
belt` or `V-belt`.

### **Friction model** — Friction method selection `Modal` (default) | `Continuous`

Option to parameterize continuous or modal friction.

#### Dependencies

To enable this parameter, clear **Pulley translation**.

### **Initial state** — Initial state of pulley `Unlocked` (default) | `Locked`

Option to initialize the simulation with the pulley locked or
unlocked.

#### Dependencies

To enable this parameter,

- Clear **Pulley translation**
- Set **Friction model** to
  `Modal`

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

### **Wrap angle** — Belt-to-pulley contact angle `180` `deg` (default) | positive scalar

Radial contact angle between the belt and the pulley.

### **Velocity threshold** — Velocity threshold `0.001` `m/s` (default) | positive scalar

Relative velocity required for peak
kinetic friction in the contact. The friction velocity threshold
improves the numerical stability of the simulation by ensuring that the
force is continuous when the direction of the velocity changes.

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

### Enumeration Updates

The **Pulley translation** parameter now uses a check box. This
parameter used a drop down in previous releases.

## Description

Power transmission element with frictional belt wrapped around pulley circumference

The Belt Pulley block represents a pulley wrapped in a
flexible ideal, flat, or V-shaped belt. When you set **Belt type** to
`Ideal - No slip`, the belt does not slip relative to the
pulley surfaces. You can optionally enable pulley linear translation.

The block accounts for friction between the flexible belt and the pulley surface. The
tensioner slips when the load exceeds the friction force. The block accounts for
centrifugal loading in the flexible belt, pulley inertia, and bearing friction.

The belt ends can either move in the same direction or in the opposite direction.

The block equations relate power transmission between the belt branches or to or from the
pulley. The driving and driven branches use the same calculation. Without sufficient
tension, the frictional force is not enough to transmit power between the pulley and
belt.

Your model is valid when both ends of the belt are in tension. You can choose to display a
warning in the Simulink® Diagnostic Viewer when the leading belt end loses tension. When assembling
a model, ensure that tension is maintained throughout the simulation by adding mass to
at least one of the belt ends or by adding a tensioner like the Cable
block. Use the Variable Viewer to ensure that any springs attached to the belt are in
tension. For more details on building a tensioner, see Best Practices for Modeling Pulley Networks.

You can set **Friction model** to `Modal` to use a
modal parameterization for the pulley. Choose the modal parameterization for greater
numerical robustness. To enable this parameter, clear the **Pulley
translation** parameter.

The Belt Pulley block uses a composite implementation
of the Fundamental Friction Clutch block to
produce the conditions for the modal parameterization.

### Equations

For either setting of the **Friction model** parameter, the block
equations refer to these quantities:

- *β* is the belt direction sign. When you set
  **Belt direction** to `Ends move in
  same direction`, *β* = 1. Otherwise,
  *β* = -1.
- *Vrel* is the relative
  velocity between the belt and pulley periphery.
  *Vrel* = 0 when
  **Belt type** is `Ideal - No
  slip`.
- *VA* is the linear velocity of
  branch A.
- *VB* is the linear velocity of
  branch B.
- *VC* is the linear velocity of
  the pulley at its center. When you clear **Pulley
  translation**, the block constrains this value to 0.
- *ωS* is the angular velocity
  of the pulley contact surface.
- *R* is the radius of the pulley.
- *Fcentrifugal* is centrifugal
  force of the belt.
- *FC* is the force acting
  through the pulley centroid. When you specify a value for
  **Inertia**,
  *FC* includes force due to
  the pulley mass acceleration.
- *ρ* is the belt linear density.
- *Ffr* is the friction force
  between the pulley and the belt.
- *FA* is the force acting along
  branch A.
- *FB* is the force acting along
  branch B.
- *θ* is the contact wrap angle.
- *τS* is the pulley
  torque.

The kinematic constraints between the pulley and belt are:

−βVA=VC−RωS−βVrel

VB=VC+RωS+βVrel

When you set **Belt type** to either `V-belt` or
`Flat belt` and set **Centrifugal
force** to `Model centrifugal force`, the
centrifugal force is:

Fcentrifugal=ρ(VB−VC)2.

When you select **Pulley translation**, the
force balancing equation is:

FC=(βFA−FB−Fcentrifugal,smooth,sat)⋅sin(θ2).

To calculate
*Fcentrifugal,smooth,sat*, the block

- Smooths *Fcentrifugal* using
  *Fthr*. You can increase
  smoothing by raising *Fthr*, and
  you can decrease smoothing by lowering
  *Fthr*.
- Saturates values above
  *βFA-FB*.

The sign convention is such that, when **Belt direction** is
`Ends move in opposite direction`, a positive rotation
in port **S** results in a negative translation for port
**A** and a positive translation for port
**B**.

To enable the **Friction model** parameter, set **Belt
type** to `Flat belt` or
`V-belt` and clear **Pulley
translation**.

**Continuous Friction**

When you set **Friction model** to `Continuous`,
the block equations refer to these quantities:

- *μ* is the **Contact friction
  coefficient** parameter.
- *μsmoothed* is the
  instantaneous value of the friction coefficient.
- *Vthr* is the
  **Velocity threshold** parameter.
- *b* is the viscous damping of the bearing.
- *Fthr* is the
  **Force threshold** parameter.

The instantaneous friction coefficient is a function of the
relative velocity such that

μsmoothed=μsheavetanh(4VrelVthr),

where the hyperbolic tangent function maintains numerical robustness by ensuring a smooth
and continuous output for *Vrel*
zero-crossings.

For a V-belt, the block derives the contact friction value using the sheave angle:

μsheave=μsin(ϕ2),

where:

- *μsheave* is the effective
  friction coefficient.
- *Φ* is the sheave angle.

For a flat belt, *μsheave* =
*μ*.

The friction velocity threshold controls the width of the region within which the friction
coefficient changes its value from zero to a steady-state maximum. The friction
velocity threshold specifies the velocity at which the hyperbolic tangent equals
`0.999`. The smaller the value, the steeper the change of
*μ*.

The block determines the effect of friction on the force at the belt ends as:

−βFA−Fcentrifugal=(FB−Fcentrifugal)e−μsmoothedθ,

which follows the form of the capstan equation, also known as
the Euler-Eytelwein equation. The torque acting on the pulley is

τS=(−βFA−FB)Rσ+ωSb,

where *σ* = 1 when you set **Belt type** to
`Ideal - No slip`. Otherwise,

σ=tanh(4VrelVthr)tanh(FBFthr).

**Modal Friction**

For a V-belt, the block derives the static and kinetic friction values by using the sheave angle:

μStatic,sheave=μStaticsin(ϕ2)μKinetic,sheave=μKineticsin(ϕ2)

where:

- *μStatic* is the
  **Static friction coefficient**
  parameter.
- *μStatic,sheave* is
  effective static friction coefficient.
- *μKinetic* is the
  **Kinetic friction coefficient**
  parameter.
- *μKinetic,sheave* is
  effective kinetic friction coefficient.
- *Φ* is the sheave angle.

For a flat belt, *μStatic,sheave* =
*μStatic*, and *μKinetic,sheave* =
*μKinetic*.

When you set **Friction model** to
`Modal`, the block calculates the maximum static
friction force before slipping as

FFriction,Static,Max=(FDrive−FCentrifugal)⋅(1−e−μStatic,sheaveθ),

where *FFriction,Static,Max* is the maximum force
magnitude due to static friction, and
*FDrive* is the force due to tension
felt at the end of the pulley with the greatest force magnitude. As with
*Fcentrifugal*, the block uses
*Fthr* to smooth
*FDrive*. To increase or
decrease the smoothing on *FDrive*,
raise of lower the value of the **Force threshold**
parameter.

The block smoothly saturates
*FFriction,Static,Max* to be
greater than or equal to 0 as

FFriction,Static,Max,Smooth=0.5(FFriction,Static,Max+FFriction,Static,Max2+(RFthr)2).

During slip,

FFriction,Slip=μKinetic,sheaveμStatic,sheaveFFriction,Static,Max,

where
*μKinetic,sheave* is the kinetic
friction coefficient. The block resolves the torque balance using

τS=ωSb+RFFriction,

and

RβFA+RFB=−RFFriction,

where Simscape™ logs *RFFriction* as
`fundamental_clutch.torque`.
