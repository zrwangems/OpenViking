---
type: simulink-block
title: 'Translational Friction (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Elements'
documentation_page: 'translationalfrictionpb'
documentation_source_path: 'ref/translationalfrictionpb.html'
language: en
---

# Translational Friction (PB)

## Ports
```yaml
ports:
- name: N
  summary: Normal force control signal, N physical signal
  direction: input
- name: B
  summary: Base port position-based mechanical translational
  direction: conserving
- name: F
  summary: Follower port position-based mechanical translational
  direction: conserving
```

### Input

### **N** — Normal force control signal, N physical signal

Physical signal input port for the control signal that specifies the normal force.
If the signal becomes negative, the block saturates the input value to 0.

#### Dependencies

To enable this port, set the **Normal force specification**
parameter to `Variable`.
### Conserving

### **B** — Base port position-based mechanical translational

Position-based mechanical translational conserving port that represents the base
connection.

### **F** — Follower port position-based mechanical translational

Position-based mechanical translational conserving port that represents the
follower connection. For positive length, port **F** has a more
positive position than port **B**.
## Parameters
```yaml
parameters:
- name: Normal force specification
  summary: Whether normal force is constant or variable Constant (default) | Variable
  group: ''
- name: Normal force
  summary: Force normal to motion 10 N (default) | nonnegative scalar
  group: ''
- name: Breakaway friction coefficient
  summary: Proportionality coefficient between normal force and breakaway friction force 2.5 (default) | positive scalar
  group: ''
- name: Breakaway friction velocity
  summary: Peak velocity for Stribeck friction 0.1 m/s (default) | positive scalar
  group: ''
- name: Coulomb friction coefficient
  summary: Proportionality coefficient between normal force and friction that opposes motion 2 (default) | nonnegative scalar
  group: ''
- name: Viscous friction coefficient
  summary: Viscous losses proportionality coefficient 0 N/(m/s) (default) | nonnegative scalar
  group: ''
```

### **Normal force specification** — Whether normal force is constant or variable `Constant` (default) | `Variable`

Select whether the normal force applied to the block is constant or variable:

- `Constant` — Specify normal force by using the
  **Normal force** parameter value.
- `Variable` — Specify normal force by using the physical
  signal at port **N**.

### **Normal force** — Force normal to motion `10 N` (default) | nonnegative scalar

Force applied to the block in the direction normal to the motion. The block
calculates the breakaway friction force and the Coulomb friction force based on this
value and the proportionality coefficients, **Breakaway friction
coefficient** and **Coulomb friction coefficient**.

#### Dependencies

To enable this parameter, set **Normal force specification** to
`Constant`.

### **Breakaway friction coefficient** — Proportionality coefficient between normal force and breakaway friction force `2.5` (default) | positive scalar

Coefficient for calculating the breakaway friction force, which is the sum of the
Coulomb and the static frictions, based on the normal force. The parameter value must be
greater than or equal to the **Coulomb friction coefficient** value.

### **Breakaway friction velocity** — Peak velocity for Stribeck friction `0.1 m/s` (default) | positive scalar

Velocity at which the Stribeck friction is at its peak. At this point, the sum of
the Stribeck and Coulomb friction is the breakaway friction force. This parameter
specifies the velocity threshold, which affects the tradeoff between the simulation
accuracy and speed.

### **Coulomb friction coefficient** — Proportionality coefficient between normal force and friction that opposes motion `2` (default) | nonnegative scalar

Coefficient for calculating the Coulomb friction force, which is the friction that
opposes motion, based on the normal force.

### **Viscous friction coefficient** — Viscous losses proportionality coefficient `0 N/(m/s)` (default) | nonnegative scalar

Proportionality coefficient between the friction force and the relative velocity.
Viscous losses do not depend on the normal force.
## Libraries

Simscape / Foundation Library / Translational / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Resistive frictional contact between surfaces in position-based mechanical translational systems

The Translational Friction (PB) block represents resistive
frictional contact between surfaces.

The friction force is a function of relative velocity and is assumed to be the sum of
Stribeck, Coulomb, and viscous components, as shown in the figure.

Friction force diagram

The Stribeck friction, *F*S, is the negatively
sloped characteristics taking place at low velocities [1]. The Coulomb friction,
*F*C, results in a constant force at any velocity.
The viscous friction, *F*V, opposes motion with the
force directly proportional to the relative velocity. The sum of the Coulomb and Stribeck
frictions at the vicinity of zero velocity is the breakaway friction,
*F*brk.

You specify the normal force, *F*N, which acts on
the block in the direction normal to the rail, that is, normal to the direction of the motion.
The block calculates the breakaway friction force and the Coulomb friction force based on the
normal force and the proportionality coefficients that you also specify. The normal force can
be either constant or variable.

The friction is approximated with the following equations:

ffriction=−2e(Fbrk−FC)⋅exp(−(vvSt)2)⋅vvSt−FC⋅tanh(vvCoul)−fvv

Fbrk=FN⋅Kbrk

FC=FN⋅KC

vSt=vbrk2

vCoul=vbrk/10

v=vF−vB

length=xF−xB

power\_dissipated=−ffriction⋅v

where:

- *f*friction is the friction force.
- *F*N is the normal force, which acts on the
  block in the direction normal to the rail, that is, normal to the direction of the
  motion.
- *F*C is the Coulomb friction.
- *K*C is the Coulomb friction
  coefficient.
- *F*brk is the breakaway friction.
- *K*brk is the breakaway friction
  coefficient.
- *f*v is the viscous friction
  coefficient.
- *v*brk is the breakaway friction
  velocity.
- *v*St is the Stribeck velocity
  threshold.
- *v*Coul is the Coulomb velocity
  threshold.
- *v* is the relative velocity.
- *v*B and
  *v*F are the absolute velocities of ports
  **B** and **F**, respectively.
- *length* is the friction length.
- *x*B and
  *x*F are the absolute positions of ports
  **B** and **F**, respectively.
- *power\_dissipated* is the power dissipated through the
  friction.

The negative sign in the first equation reflects the force flow conventions used in the
position-based mechanical translational domain. Unless the ports have inverted, a positive
value of *f*friction indicates that the block is in a
state of compression and a negative value of
*f*friction indicates that the block is in a state
of tension. For more information, see Two-Port Block Orientation and Force Flow Conventions.

The exponential function used in the Stribeck portion of the force equation is continuous
and decays at velocity magnitudes greater than the breakaway friction velocity.

The hyperbolic tangent function used in the Coulomb portion of the force equation ensures
that the equation is smooth and continuous through *v* = 0, but quickly reaches its full value at nonzero velocities.

Connections **B** and **F** are position-based
mechanical translational conserving ports. The friction force acts from port
**B** on port **F**. Positive friction force drives port
**F** in the positive direction. You can specify the normal force either by
using the **Normal force** parameter or by using the physical signal port
**N**.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
