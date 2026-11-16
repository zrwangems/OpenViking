---
type: simulink-block
title: 'Shock Absorber'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Couplings and Drives / Coupling and Drive Assemblies'
documentation_page: 'shockabsorber'
documentation_source_path: 'ref/shockabsorber.html'
language: en
---

# Shock Absorber

## Ports

### Conserving

### **C** — Case mechanical translational

Mechanical translational conserving port associated with one end of
the shock absorber. Positive force acts from port **R**
to port **C**.

### **R** — Rod mechanical translational

Mechanical translational conserving port associated with one end of
the shock absorber. Positive force acts from port **R**
to port **C**.

## Parameters

### Spring-Damper

### **Spring stiffness** — Stiffness of spring `1e4` `N/m` (default) | nonnegative scalar

Value of the spring stiffness constant, *k*.

### **Viscous friction coefficient** — Viscous friction coefficient `1e2` `N*s/m` (default) | nonnegative scalar

Value of the viscous damping constant, *b*.

### **Coulomb friction force** — Coulomb friction force `0` `N` (default) | nonnegative scalar

Value of the Coulomb friction force. Setting the value to
`0` eliminates the Coulomb friction force
contribution, which enhances simulation speed and makes the model more
suitable for HIL testing.

### **Ratio of static to kinetic friction** — Static-to-kinetic friction ratio `1.1` (default) | scalar greater than or equal to 1

Value of the ratio of static friction to kinetic friction,
*Fs*/*Fk*.

### **Velocity tolerance** — Slip velocity threshold `0.001` `m/s` (default) | positive scalar

Value of the relative velocity below which ports
**R** and **C** lock and translate
together. When the relative velocity is greater than this value, the
ports slide relative to one another.

### Hard Stops

### **Hard stop** — Hard stop option `No hard stops - Suitable for HIL simulation` (default) | `Compliant hard stops`

Whether to model translational hard stops. Select from these options:

- `No hard stops — Suitable for HIL
  simulation` — Enhance simulation speed by
  excluding the hard-stop force contribution.
- `Compliant hard stops` — Enhance
  model fidelity by including the hard-stop force
  contribution.

### **Upper bound** — Gap between slider and upper bound `0.1` `m` (default) | scalar

Upper hard-stop position, *UB*. Positive displacement
beyond the upper bound activates the hard-stop contact force. The value
must be greater than the **Lower bound**
parameter.

#### Dependencies

To enable this parameter, set **Hard Stop** to
`Compliant hard stops`.

### **Lower bound** — Gap between slider and lower bound `-0.1` `m` (default) | scalar

Lower hard-stop position, *LB*. Negative displacement
beyond the lower bound activates the hard-stop contact force. The value
must be smaller than the **Upper bound** parameter.

#### Dependencies

To enable this parameter, set **Hard Stop** to
`Compliant hard stops`.

### **Contact stiffness** — Contact stiffness constant `1e6` `N/m` (default) | nonnegative scalar

Value of the hard-stop stiffness constant,
*kHS*.

#### Dependencies

To enable this parameter, set **Hard Stop** to
`Compliant hard stops`.

### **Contact damping** — Contact damping constant `1e4` `N*s/m` (default) | positive scalar

Value of the hard stop damping constant,
*bHS*. This parameter
specifies a dissipating property of colliding bodies. The greater the
value of the parameter, the more energy the hard stop dissipates during
an interaction.

#### Dependencies

To enable this parameter, set **Hard Stop** to
`Compliant hard stops`.

### **Hard stop model** — Hard stop transition behavior `Stiffness and damping applied smoothly through transition region, damped rebound` (default) | ...

Stiffness and rebound options for the hard stop model. The block uses
a composite implementation of the Translational Hard
Stop block. You can choose from the following options:

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at bounds,
  undamped rebound`
- `Full stiffness and damping applied at bounds,
  damped rebound`
- `Based on coefficient of
  restitution`

### **Transition region** — Hard-stop transition distance `0.1` `mm` (default) | positive scalar

Region where the force ramps up from zero to the full value. At the
end of the transition region, the block applies full stiffness and
damping.

#### Dependencies

To enable this parameter, set **Hard Stop** to
`Stiffness and damping applied smoothly through
transition region, damped rebound`.

### **Coefficient of restitution** — Ratio of final-to-initial relative speed between slider and stop after collision `0.7` (default) | unitless value between 0 and 1

Ratio of the final to the initial relative speed between the slider
and the stop after the slider bounces.

#### Dependencies

To enable this parameter, set **Hard stop**  to
`Compliant hard stops` and
**Hard stop model** to `Based on
coefficient of restitution`.

### **Static contact speed threshold** — Threshold relative speed between slider and stop before collision `0.001` `m/s` (default) | nonnegative scalar

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

### **Static contact release force threshold** — Threshold torque needed to transition from contact mode to free mode `0.001` `N` (default)

Minimum torque needed to release the slider from a static contact
mode.

#### Dependencies

To enable this parameter, set **Hard stop**  to
`Compliant hard stops` and
**Hard stop model** to `Based on
coefficient of restitution`.

## Libraries

Simscape / Driveline / Couplings & Drives

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013a**

### R2023a: Composite Hard Stop Updates

Due to updates in the Translational Hard Stop block, the **Hard stop
model** parameter now features the `Coefficient of
restitution` option.

## Description

Spring and damper system that absorbs translational shocks

The Shock Absorber block represents a spring-damper
system that absorbs vibrations. An internal force acts between ports
**R** and **C**. This force is the sum of spring
stiffness, damping, Coulomb friction, and hard-stop contributions. All force
contributions are optional.

Diagram of a shock absorber with port R at the opposite end of port C.

The block is a composite of these blocks:

| Block | Function | Library |
| --- | --- | --- |
| Loaded-Contact Translational Friction | Coulomb friction | **Simscape** / **Driveline** / **Brakes & Detents** / **Translational** |
| Translational Damper | Damping | **Simscape** / **Foundation Library** / **Mechanical** / **Translational Elements** |
| Translational Spring | Spring |
| Translational Hard Stop | Hard stop |

### Assumptions and Limitations

- Setting **Hard stop** to `Compliant hard
  stop` or setting **Coulomb friction
  force** to a nonzero value enhances model fidelity, but reduces
  simulation speed. For more information, see Driveline Simulation Performance.
