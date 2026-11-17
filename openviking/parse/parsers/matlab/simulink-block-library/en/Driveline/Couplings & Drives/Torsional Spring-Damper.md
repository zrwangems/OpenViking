---
type: simulink-block
title: 'Torsional Spring-Damper'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'torsionalspringdamper'
documentation_source_path: 'ref/torsionalspringdamper.html'
language: en
---

# Torsional Spring-Damper

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

Mechanical rotational port associated with the slider that travels between the stops
installed on the case.

### **R** — Base port mechanical rotational

Mechanical rotational port associated with the rod.
## Parameters
```yaml
parameters:
- name: Spring stiffness
  summary: Torsional spring stiffness 1000 N*m/rad (default) | nonnegative scalar
  group: Spring-Damper
- name: Viscous friction coefficient
  summary: Torsional viscous friction 10 N*m/(rad/s) (default) | nonnegative scalar
  group: Spring-Damper
- name: Coulomb friction torque
  summary: Kinetic friction torque 0 N*m (default) | nonnegative scalar
  group: Spring-Damper
- name: Ratio of static to kinetic friction
  summary: Static friction with respect to kinetic friction 1.1 (default) | positive scalar
  group: Spring-Damper
- name: Velocity tolerance
  summary: Mating driveshaft differential speed tolerance 0.001 rad/s (default) | positive scalar
  group: Spring-Damper
- name: Hard stop
  summary: Simulate boundary hard stops No hard stops - Suitable for HIL simulation (default) | Compliant hard stops
  group: Hard Stops
- name: Upper bound
  summary: Location of upper hard stop 10 deg (default) | scalar
  group: Hard Stops
- name: Lower bound
  summary: Location of lower hard stop -10 deg (default) | scalar
  group: Hard Stops
- name: Contact stiffness
  summary: Hard stop proportional spring constant 1e6 N*m/(rad/s) (default) | nonnegative scalar
  group: Hard Stops
- name: Contact damping
  summary: Hard stop proportional damping 10 (N*m)/(rad/s) (default) | positive scalar
  group: Hard Stops
- name: Hard stop model
  summary: Hard stop transition behavior Stiffness and damping applied smoothly through transition region, damped rebound
    (default) | ...
  group: Hard Stops
- name: Transition region
  summary: Region of partial hard stop effects 0.001 rad (default) | positive scalar
  group: Hard Stops
- name: Coefficient of restitution
  summary: Ratio of final-to-initial relative speed between slider and stop after collision 0.7 (default) | unitless value
    between 0 and 1
  group: Hard Stops
- name: Static contact speed threshold
  summary: Threshold relative speed between slider and stop before collision 0.1 rad/s (default) | nonnegative scalar
  group: Hard Stops
- name: Static contact release torque threshold
  summary: Threshold force needed to transition from contact mode to free mode 0.001 N*m (default)
  group: Hard Stops
- name: Initial deformation
  summary: Starting deformation value 0 deg (default) | scalar
  group: Initial Conditions
```

### Spring-Damper

### **Spring stiffness** — Torsional spring stiffness `1000` `N*m/rad` (default) | nonnegative scalar

Torsional spring stiffness that acts on connected driveshafts.

### **Viscous friction coefficient** — Torsional viscous friction `10` `N*m/(rad/s)` (default) | nonnegative scalar

Torsional friction that acts on the connected driveshafts.

### **Coulomb friction torque** — Kinetic friction torque `0` `N*m` (default) | nonnegative scalar

Constant kinetic friction torque that acts on the connected
driveshafts. This constant torque opposes rotation at any
velocity.

### **Ratio of static to kinetic friction** — Static friction with respect to kinetic friction `1.1` (default) | positive scalar

Constant ratio of static Coulomb friction torque to kinetic Coulomb friction torque that
acts on connected driveshafts. The value must be greater than or equal
to one.

### **Velocity tolerance** — Mating driveshaft differential speed tolerance `0.001` `rad/s` (default) | positive scalar

Minimum relative angular speed below which the two connected driveshafts can lock and
rotate together.

### Hard Stops

### **Hard stop** — Simulate boundary hard stops `No hard stops - Suitable for HIL simulation` (default) | `Compliant hard stops`

Include or exclude hard-stop torque by selecting one of these options:

- `No hard stops - Suitable for HIL
  simulation` — Select this option to enhance
  simulation speed by excluding the hard-stop torque
  contribution.
- `Compliant hard stops` — Select
  this option to enhance model fidelity by including the hard
  stop torque contribution.

### **Upper bound** — Location of upper hard stop `10` `deg` (default) | scalar

Upper hard-stop angular displacement from the zero-torque reference angle. The value
must be greater than the **Lower bound**
parameter.

#### Dependencies

To enable this parameter, set **Hard stop** to
`Compliant hard stops`.

### **Lower bound** — Location of lower hard stop `-10` `deg` (default) | scalar

Lower hard-stop angular displacement from the zero spring force reference angle. The
value must be less than the **Upper bound**
parameter.

#### Dependencies

To enable this parameter, set **Hard stop** to
`Compliant hard stops`.

### **Contact stiffness** — Hard stop proportional spring constant `1e6` `N*m/(rad/s)` (default) | nonnegative scalar

Hard-stop stiffness. This value only applies if the relative angle moves into the
hard-stop region.

#### Dependencies

To enable this parameter, set **Hard stop** to
`Compliant hard stops`.

### **Contact damping** — Hard stop proportional damping `10` `(N*m)/(rad/s)` (default) | positive scalar

Hard-stop damping. This value only applies if the relative angle moves into the
hard-stop region. The value must be greater than zero.

#### Dependencies

To enable this parameter, set **Hard stop** to
`Compliant hard stops`.

### **Hard stop model** — Hard stop transition behavior `Stiffness and damping applied smoothly through transition region, damped rebound` (default) | ...

Stiffness and rebound options for the hard stop model. The block uses
a composite implementation of the Rotational Hard Stop block. You can choose from the
following options:

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at bounds,
  undamped rebound`
- `Full stiffness and damping applied at bounds,
  damped rebound`
- `Based on coefficient of
  restitution`

#### Dependencies

To enable this parameter, set **Hard stop** to
`Compliant hard stops`.

### **Transition region** — Region of partial hard stop effects `0.001` `rad` (default) | positive scalar

Distance from full compression or full extension where the effects of stiffness and
damping are partially applied. When you set **Hard stop
model** to `Stiffness and damping applied
smoothly through transition region, damped rebound`,
the block smoothly transitions the onset of stiffness and damping as the
spring approaches full extension or full compression.

#### Dependencies

To enable this parameter, set **Hard stop**  to `Compliant
hard stops` and **Hard stop
model** to `Stiffness and damping applied
smoothly through transition region, damped
rebound`.

### **Coefficient of restitution** — Ratio of final-to-initial relative speed between slider and stop after collision `0.7` (default) | unitless value between 0 and 1

Ratio of the final to the initial relative speed between the slider
and the stop after the slider bounces.

#### Dependencies

To enable this parameter, set **Hard stop**  to
`Compliant hard stops` and
**Hard stop model** to `Based on
coefficient of restitution`.

### **Static contact speed threshold** — Threshold relative speed between slider and stop before collision `0.1` `rad/s` (default) | nonnegative scalar

Threshold relative speed between the slider and the stop before
collision. When the slider hits the case with speed less than the value
of this parameter, they stay in contact. Otherwise, the slider bounces.
To avoid modeling static contact between the slider and the case, set
this parameter to `0`.

#### Dependencies

To enable this parameter, set **Hard stop**  to
`Compliant hard stops` and
**Hard stop model** to `Based on
coefficient of restitution`.

### **Static contact release torque threshold** — Threshold force needed to transition from contact mode to free mode `0.001` `N*m` (default)

Minimum force needed to release the slider from a static contact
mode.

#### Dependencies

To enable this parameter, set **Hard stop**  to
`Compliant hard stops` and
**Hard stop model** to `Based on
coefficient of restitution`.

### Initial Conditions

### **Initial deformation** — Starting deformation value `0` `deg` (default) | scalar

Initial deformation of the torsional spring relative to the zero-torque reference
angle.
## Libraries

Simscape / Driveline / Couplings & Drives

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011a**

### R2023a: Composite Hard Stop Updates

Due to updates in the Rotational Hard Stop block, the **Hard stop
model** parameter now features the `Coefficient of
restitution` option.

## Description

Rotational spring and damper coupling with Coulomb friction, locking, and hard stops

The Torsional Spring-Damper block represents a rotational
spring and damper that imposes a combination of internally generated torques between the
two connected driveshaft axes, the rod and the case. The block defines the torque using
the following behaviors:

- Linear damped spring
- Coulomb friction (including locking static friction)
- Hard-stop compliance

This block is a composite component that consists of these blocks:

| Block | Contribution | Library |
| --- | --- | --- |
| Loaded-Contact Rotational Friction | Coulomb friction | **Simscape** / **Driveline** / **Brakes & Detents** / **Rotational** |
| Rotational Damper | Damping | **Simscape** / **Foundation Library** / **Mechanical** / **Rotational Elements** |
| Rotational Spring | Spring |
| Rotational Hard Stop | Hard stop |

For more information, see Composite Components.

### Assumptions and Limitations

- Including hard-stop and Coulomb friction enhances model fidelity, but
  reduces simulation speed. For more information, see Driveline Simulation Performance.
