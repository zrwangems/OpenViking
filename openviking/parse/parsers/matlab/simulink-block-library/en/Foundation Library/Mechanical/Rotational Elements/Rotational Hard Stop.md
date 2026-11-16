---
type: simulink-block
title: 'Rotational Hard Stop'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Rotational Elements'
documentation_page: 'rotationalhardstop'
documentation_source_path: 'ref/rotationalhardstop.html'
language: en
---

# Rotational Hard Stop

## Ports

### Conserving

### **R** — Slider mechanical rotational

Mechanical rotational conserving port associated with the slider that
travels between the stops installed on the case.

### **C** — Case mechanical rotational

Mechanical rotational conserving port associated with the case.

## Parameters

### **Upper bound** — Gap between slider and upper bound `0.1 rad` (default) | scalar

Gap between the slider and the upper bound. Specify the direction with
respect to the local coordinate system, with the slider located in the
origin. A positive value specifies the gap between the slider and the upper
bound. A negative value sets the slider as penetrating into the upper bound.

### **Lower bound** — Gap between slider and lower bound `-0.1 rad` (default) | scalar

Gap between the slider and the lower bound. Specify the direction with
respect to the local coordinate system, with the slider located in the
origin. A negative value specifies the gap between the slider and the lower
bound. A positive value sets the slider as penetrating into the lower bound.

### **Hard stop model** — Select the hard stop model `Stiffness and damping applied smoothly through transition region, damped rebound` (default) | `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

Select the hard stop model:

- `Stiffness and damping applied smoothly through
  transition region, damped rebound` — Specify
  a transition region in which the torque ramps up from zero. At the
  end of the transition region, the block applies the full stiffness
  and damping. This model applies damping on the rebound, but damping
  is limited to the value of the stiffness torque. Therefore, damping
  can reduce or eliminate the torque provided by the stiffness, but
  never exceed it. All equations are smooth and produce no zero
  crossings.
- `Full stiffness and damping applied at bounds,
  undamped rebound` — This model has full
  stiffness and damping applied with impact at upper and lower bounds,
  with no damping on the rebound. The equations produce no zero
  crossings when velocity changes sign, but there is a position-based
  zero crossing at the bounds. Having no damping on rebound helps to
  push the slider past this position quickly. This model has nonlinear
  equations.
- `Full stiffness and damping applied at bounds, damped
  rebound` — This model has full stiffness and
  damping applied with impact at upper and lower bounds, with damping
  applied on the rebound as well. The equations are switched linear,
  but produce position-based zero crossings. Use this hard stop model
  if `simscape.findNonlinearBlocks` indicates that
  this block prevents the whole network from being switched linear.
- `Based on coefficient of restitution`
  — This model uses a mode chart with regular and instantaneous
  modes to represent the hard stop behavior. All equations are smooth
  and produce no zero crossings. This modeling option improves
  simulation performance. For more information, see Model Based on Coefficient of Restitution.

### **Contact stiffness at upper bound** — Elasticity of collision at upper bound `1e6 N*m/rad` (default) | positive scalar

Elastic property of the colliding bodies when the slider hits the upper
bound. The greater the value of this parameter, the less the bodies
penetrate into each other and the more rigid the impact becomes. Setting
this parameter to lesser values makes contact softer, but generally improves
convergence and computational efficiency.

#### Dependencies

To enable this parameter, set **Hard stop model** to

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at bounds,
  undamped rebound`
- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`

### **Contact stiffness at lower bound** — Elasticity of collision at lower bound `1e6 N*m/rad` (default) | positive scalar

Elastic property of the colliding bodies when the slider hits the lower
bound. The greater the value of this parameter, the less the bodies
penetrate into each other and the more rigid the impact becomes. Setting
this parameter to lesser values makes contact softer, but generally improves
convergence and computational efficiency.

#### Dependencies

To enable this parameter, set **Hard stop model** to

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at bounds,
  undamped rebound`
- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`

### **Contact damping at upper bound** — Dissipating property at upper bound `0.01 N*m/(rad/s)` (default) | positive scalar

Dissipating property of the colliding bodies when the slider hits the
upper bound. The greater the value of this parameter, the more energy
dissipates during an interaction.

#### Dependencies

To enable this parameter, set **Hard stop model** to

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at bounds,
  undamped rebound`
- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`

### **Contact damping at lower bound** — Dissipating property at lower bound `0.01 N*m/(rad/s)` (default) | positive scalar

Dissipating property of the colliding bodies when the slider hits the
lower bound. The greater the value of this parameter, the more energy
dissipates during an interaction.

#### Dependencies

To enable this parameter, set **Hard stop model** to

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at bounds,
  undamped rebound`
- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`

### **Transition region** — Region where torque ramps up `0.001 rad` (default) | positive scalar

Region where the torque ramps up from zero to the full value. At the end
of the transition region, the block applies full stiffness and damping.

#### Dependencies

To enable this parameter, set **Hard stop model** to
`Stiffness and damping applied smoothly through
transition region, damped rebound`.

### **Coefficient of restitution** — Ratio of final-to-initial relative speed between slider and stop after collision `0.7` (default) | unitless value between 0 and 1

Ratio of the final to the initial relative speed between the slider and
the stop after the slider bounces.

#### Dependencies

To enable this parameter, set **Hard stop model** to
`Based on coefficient of
restitution`.

### **Static contact speed threshold** — Threshold relative speed between slider and stop before collision `0.1 rad/s` (default) | nonnegative scalar

Threshold relative speed between the slider and the stop before collision.
When the slider hits the case with speed less than the value of this
parameter, they stay in contact. Otherwise, the slider bounces. To avoid
modeling static contact between the slider and the case, set this parameter
to `0`.

#### Dependencies

To enable this parameter, set **Hard stop model** to
`Based on coefficient of
restitution`.

### **Static contact release torque threshold** — Threshold torque needed to transition from contact mode to free mode `0.001 N*m` (default) | positive scalar

Minimum torque needed to release the slider from a static contact mode.

#### Dependencies

To enable this parameter, set **Hard stop model** to
`Based on coefficient of
restitution`.

## Libraries

Simscape / Foundation Library / Mechanical / Rotational Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

### R2023a: Modeling option based on coefficient of restitution

The new option for the **Hard stop model** parameter,
`Based on coefficient of restitution`, models the hard
stop by using a mode chart that includes free mode, where there is no torque
transmission between the slider and the case, and static contact mode, where there
is zero speed difference between the slider and the case.

In previous releases, only the modeling options based on stiffness and damping
were available.

This change has no compatibility impact.

## Description

Double-sided rotational hard stop

The Rotational Hard Stop block represents a
double-sided mechanical rotational hard stop that restricts the motion of a body between
upper and lower bounds.

Schematic of the mechanical rotational hard stop

The slider connects to port **R** and the case connects to port
**C**. The block transmits torque from port **R**
to port **C** when the gap is closed in the positive direction.

The block computes the slider angular position, *φ*, from the slider
angular velocity, *ω* = *ω*R -
*ω*C.

*θ* is the slider arc angle and *ψ* is the slider
angular position on the negative side, *θ* = |*φ* -
*ψ*|. The block assumes the slider arc angle is 0 and does not
model *θ* and *ψ*, but the schematic uses these
symbols to explain the basic design of the hard stop.

*g*p is the initial gap on the positive side,
measured from *x*:

- For the positive gap to be open, *g*p
  must be positive.
- A negative value of *g*p means that
  the slider is penetrating into the upper bound.
- The gap is closed when *g*p -
  *φ* ≤ 0.

*g*n is the initial gap on the negative side,
measured from *y*:

- For the negative gap to be open, *g*n
  must be negative.
- A positive value of *g*n means that
  the slider is penetrating into the lower bound.
- The gap is closed when *ψ* -
  *g*n ≤ 0.

The block provides several modeling options:

- Three options based on stiffness and damping. These models use similar
  underlying equations and differ in how stiffness and damping are applied at
  bounds.
- A modeling option based on the coefficient of restitution. This model is
  different from the other three because it uses a mode chart to represent the
  hard stop behavior.

### Models Based on Stiffness and Damping

In hard stop models based on stiffness and damping, the impact interaction between
the slider and the stops is assumed to be elastic. This assumption means that the
block represents the stop as a spring that comes into contact with the slider as the
gap is cleared and opposes the slider penetration into the stop with a torque
linearly proportional to this penetration. The block models this elasticity with the
**Contact stiffness at upper bound** and **Contact
stiffness at lower bound** parameters. To account for energy
dissipation and nonelastic effects, the block uses the **Contact damping at
upper bound** and **Contact damping at lower bound**
parameters.

The basic hard stop model, `Full stiffness and damping applied at
bounds, damped rebound`, uses these equations:

T={Kp⋅(φ−gp)+Dp⋅ωfor φ≥gp0for gn<φ<gpKn⋅(φ−gn)+Dn⋅ωfor φ≤gn

ω=dφdt

where:

- *T* is the interaction torque between the slider and the
  case.
- *g*p is the initial gap between
  the slider and upper bound.
- *g*n is the initial gap between
  the slider and lower bound.
- *φ* is the slider angular position.
- *K*p is the contact stiffness at
  the upper bound.
- *K*n is the contact stiffness at
  the lower bound.
- *D*p is the damping coefficient at
  the upper bound.
- *D*n is the damping coefficient at
  the lower bound.
- *ω* is the slider angular velocity.
- *t* is time.

In the `Full stiffness and damping applied at bounds, undamped
rebound` hard stop model, the equations contain additional terms,
`ge`(*ω*,0) and
`le`(*ω*,0). These terms ensure that the
block does not apply damping on the rebound.

T={Kp⋅(φ−gp)+Dp⋅ω⋅ge(ω,0)for φ≥gp0for gn<φ<gpKn⋅(φ−gn)+Dn⋅ω⋅le(ω,0)for φ≤gn

The relational functions `ge` (greater than or equal) and
`le` (less than or equal) do not generate zero crossings when
the angular velocity changes sign. For more information, see Enabling and Disabling Zero-Crossing Conditions in Simscape Language. However, the solver treats the
`ge` and `le` functions as nonlinear.
Therefore, if `simscape.findNonlinearBlocks` indicates that the
rest of your network is linear or switched linear, use the `Full
stiffness and damping applied at bounds, damped rebound` option to
improve performance.

The default hard stop model, `Stiffness and damping applied smoothly
through transition region, damped rebound`, adds two transitional
regions to the equations, one at each bound. When the slider travels through a
transition region, the block smoothly ramps up the torque from zero to the full
value. At the end of the transition region, the block applies the full stiffness and
damping. On the rebound, the block smoothly decreases both stiffness and damping
torques to zero. These equations also use the `ge` and
`le` relational functions, which do not produce zero
crossings.

### Model Based on Coefficient of Restitution

Unlike the models based on stiffness and damping, this model does not allow
penetration of slider into the hard stops. The hard stop behavior is represented by
a mode chart with three regular modes and three instantaneous modes:

- `FREE` — There is no torque transmission between the
  slider and case.
- `CONTACT_UPPER` — The positive gap is closed.
- `CONTACT_LOWER` — The negative gap is closed.
- `RELEASE_UPPER` — The instantaneous mode needed to
  transition from `CONTACT_UPPER` to
  `FREE`.
- `RELEASE_LOWER` — The instantaneous mode needed to
  transition from `CONTACT_LOWER` to
  `FREE`.
- `IMPACT` — The instantaneous mode used when the slider
  bounces.

When the slider hits the case slowly, with speed less than the static contact
speed threshold, the slider and case stay in contact. Otherwise, the slider bounces.
When the slider bounces, it loses the speed due to the coefficient of restitution.
In either of the contact modes, slider speed *ω* = 0. To transition
from a contact mode to free mode, a torque greater than the static contact release
torque threshold must be applied to the slider, and the transition must go through
an instantaneous release mode to set the initial speed.

This modeling option improves simulation performance because static contact mode
does not require the block to keep computing hard stop torque when the block is in
contact mode.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
