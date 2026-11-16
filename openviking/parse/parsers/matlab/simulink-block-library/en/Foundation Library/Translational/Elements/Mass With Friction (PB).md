---
type: simulink-block
title: 'Mass With Friction (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Elements'
documentation_page: 'masswithfrictionpb'
documentation_source_path: 'ref/masswithfrictionpb.html'
language: en
---

# Mass With Friction (PB)

## Ports

### Input

### **N** — External normal force control signal, N physical signal

Physical signal input port for the control signal that specifies the external
normal force. The block calculates the total normal force as the sum of the external
normal force and the force proportional to the normal component of gravitational
acceleration.

If the signal becomes negative, the block saturates the input value to 0.

#### Dependencies

To enable this port, set the **External normal force
specification** parameter to `Variable`.
### Conserving

### **R** — Port that connects mass to the circuit position-based mechanical translational

Position-based mechanical translational conserving port that connects the mass to
the physical network.

## Parameters

### **Mass** — Constant mass `1 kg` (default) | positive scalar

Mass value. The mass is constant during simulation.

### **External normal force specification** — Whether external normal force is constant or variable `Constant` (default) | `Variable`

Select whether the external normal force applied to the block is constant or
variable:

- `Constant` — Specify normal force by using the
  **Constant external normal force** parameter value.
- `Variable` — Specify normal force by using the physical
  signal at port **N**.

### **Constant external normal force** — Force normal to motion `0 N` (default) | nonnegative scalar

Force applied to the block in the direction normal to the motion. The block
calculates the total normal force as the sum of this value and the force proportional to
the normal component of gravitational acceleration. The block then calculates the
breakaway friction force and the Coulomb friction force based on the total normal force
and the proportionality coefficients, **Breakaway friction
coefficient** and **Coulomb friction coefficient**.

#### Dependencies

To enable this parameter, set **External normal force
specification** to `Constant`.

### **Breakaway friction coefficient** — Proportionality coefficient between normal force and breakaway friction force `2.5` (default) | nonnegative scalar

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

Point mass with friction and gravitational effects

The Mass With Friction (PB) block represents a mass with
friction and gravitational effects that moves along an inclined rail. Gravity can induce
motion along the rail. Gravity and an optional additional normal force induce friction with
the stationary rail.

The Mass With Friction (PB) block is essentially a
structural component that consists of a Mass (PB) block
connected to port **F** of a Translational Friction
(PB) block. Port **B** of the Translational
Friction (PB) block is connected to an implicit reference.

Mass with friction schematic

The friction force is a function of relative velocity and is assumed to be the sum of
Stribeck, Coulomb, and viscous components, as shown in the figure.

Friction force diagram

The force flow equations are:

facc=m⋅v˙

facc=f+fgp+ffriction

fgp=−m⋅g⋅sin(θ)

ffriction=−2e(Fbrk−FC)⋅exp(−(vvSt)2)⋅vvSt−FC⋅tanh(vvCoul)−fvv

FN=FN,ext+fgn

fgn=m⋅g⋅|cos(θ)|

Fbrk=FN⋅Kbrk

FC=FN⋅KC

vSt=vbrk2

vCoul=vbrk/10

power\_dissipated=−ffriction⋅v

where:

- *f*acc is force proportional to mass
  acceleration. Positive force accelerates the mass in the positive direction.
- *f* is net force of the other mechanical components in the network
  acting on the mass.
- *f*gp is force proportional to the parallel
  component of gravitational acceleration, that is, to the gravitational acceleration acting
  along the rail.
- *f*gn is force proportional to the normal
  component of gravitational acceleration, that is, to gravitational acceleration acting in
  the direction normal to the rail.
- *f*friction is the friction force.
- *m* is the mass.
- *v* is the mass velocity. Ports **B** and
  **F** have the same velocity,
  *v*B =
  *v*F.
- *g* is the gravitational acceleration.
- *θ* is the rail incline angle.
- *F*N is the normal force, which acts on the
  mass in the direction normal to the rail, that is, normal to the direction of the motion.
  This force is the sum of the external normal force and the force proportional to the
  normal component of gravitational acceleration.
- *F*N,ext is the external normal force, which
  acts on the mass in the direction normal to the rail. This is an optional force due to an
  external load. You can specify it as an input signal or as a block parameter.
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
- *power\_dissipated* is the power dissipated through the
  friction.

You can disable frictional effects by setting the **Breakaway friction
coefficient**, **Coulomb friction coefficient**, and
**Viscous friction coefficient** parameters to 0.

The Mechanical Translational Properties (PB) block
specifies the gravitational acceleration and rail incline angle in the network. For more
information, see Interpreting Logged Forces in Mass Blocks.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
