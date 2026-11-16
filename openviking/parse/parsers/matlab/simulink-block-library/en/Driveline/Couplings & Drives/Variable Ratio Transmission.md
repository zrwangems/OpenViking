---
type: simulink-block
title: 'Variable Ratio Transmission'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'variableratiotransmission'
documentation_source_path: 'ref/variableratiotransmission.html'
language: en
---

# Variable Ratio Transmission

## Ports

### Input

### **r** — Input-to-output shaft velocity ratio, unitless physical signal

Physical signal port associated with the ratio of base to follower torques, which equals
the ratio of follower to base angular velocities.
### Conserving

### **B** — Base driveshaft mechanical rotational

Mechanical rotational conserving port associated with the base
driveshaft.

### **F** — Follower driveshaft mechanical rotational

Mechanical rotational conserving port associated with the follower
driveshaft.

## Parameters

### Main

### **Output shaft rotates** — Output shaft direction versus input shaft direction `In same direction as input shaft` (default) | `In opposite direction to input shaft`

Output driveshaft rotation relative to the input driveshaft.

### Compliance

### **Transmission stiffness at base (B)** — Base spring rate coefficient `5e5` `N*m/rad` (default) | positive scalar

Reciprocal of the transmission angular compliance
*kp* measured at the
base.

### **Transmission damping at base (B)** — Base damping coefficient `5e3` `N*m/(rad/s)` (default) | positive scalar

Reciprocal of the transmission angular compliance damping
*kv* measured at the
base.

### **Initial input torque at base (B)** — Starting torque at base `0` `N*m` (default) | scalar

Torque applied at the base driveshaft at the start of simulation.

### **Ratio threshold** — Zero transition smoothing `0.01` (default) | scalar

Transmission ratio below which the block uses smoothing. The block
smooths the transmission ratio when the ratio is between zero and the
value of the **Ratio threshold** parameter.

### Transmission Losses

### **Losses model** — Optional loss modeling `No losses — Suitable for HIL simulation` (default) | `Constant efficiency`

Implementation of friction losses from nonideal torque transfer.

- `No losses — Suitable for HIL simulation` —
  Torque transfer is ideal.
- `Constant efficiency` — The block reduces
  gear box torque transfer by a constant efficiency
  *η* satisfying 0 < *η* ≤ 1.

### **Efficiency** — Base-to-follower torque transfer efficiency `0.8` (default) | positive scalar

Effective torque transfer efficiency *η* between the
base and follower driveshafts.

#### Dependencies

To enable this parameter, set **Losses model** to
`Constant efficiency`.

### **Follower power threshold** — Point at which block applies full efficiency losses `0.001` `W` (default) | positive scalar

Absolute value of the follower shaft power above which the full
efficiency factor is in effect. Below this value, a hyperbolic tangent
function smooths the efficiency factor to 1, lowering the efficiency
losses to 0 when no power is transmitted.

As a guideline, the power threshold should be lower than the expected
power transmitted during simulation. Higher values might cause the block
to underestimate efficiency losses. Very low values tend to raise the
computational cost of simulation.

#### Dependencies

To enable this parameter, set **Losses model** to
`Constant efficiency`.

### Viscous Losses

### **Viscous friction coefficients at base (B) and follower (F)** — Base and follower viscous friction vector `[0, 0]` `N*m/(rad/s)` (default) | vector of nonnegative elements

Vector of viscous damping coefficients
[*μB*,
*μF*] applied at the
base and follower driveshafts, respectively.

## Libraries

Simscape / Driveline / Couplings & Drives

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011a**

### R2025a: Specify a ratio of zero

You can now specify a zero-ratio or a continuously variable ratio that changes
sign in the block. When the ratio is zero, the block does not transfer power between
ports **B** and **F**.

## Description

Dynamic gearbox with variable and controllable gear ratio, transmission compliance, and friction losses

The Variable Ratio Transmission block represents a
gearbox that dynamically transfers motion and torque between the two connected
driveshaft axes, the base and the follower.

You can choose whether the follower axis rotates in the same or opposite direction as the
base axis. If the follower and base axis rotate in the same direction,
*ωF* and
*ωB* have the same sign. If the follower
and base axis rotate in opposite directions,
*ωF* and
*ωB* have opposite signs. When the input
ratio is positive, the rotating direction of the output shaft is the one you specify.
When the ratio is negative, the output shaft rotates in the opposite direction of the
input shaft. When the ratio is zero, the two shafts become disengaged and do not
transfer torque.

Transmission compliance introduces internal time delay between the axis motions. Unlike a
gear, a variable ratio transmission does not act as a kinematic constraint. You can also
control the torque loss caused by transmission and viscous losses.

### Ideal Motion and Torque Transfer

The Variable Ratio Transmission block dynamically transfers
motion and torque between the base shaft and the follower shaft.

If the relative compliance *ϕ* between the axes is absent, the block is
equivalent to a gear with a variable ratio
*gFB(t)*. Such a gear imposes a
time-dependent kinematic constraint on the motions of the two driveshafts:

ωB=±gFB(t)ωF

τF=±gFB(t)τB

However, the Variable Ratio Transmission does include
compliance between the axes. Dynamic motion and torque transfer replace the
kinematic constraint, with a nonzero *ϕ* that dynamically responds
through the base compliance parameters *k*p
and *k*v:

dϕdt=(±gFB(t)ωF−ωB )α−kpkv ϕ(1−α)τB=(−kpϕ(t)−kv(±gFB(t)ωF−ωB))α±gFB(t)τB+τF−τloss=0

where *ɑ =
3u2-2u3*, and u=|gFB(t)|gFB,thr. The function, *α*, enables smooth transitions
between engaged and disengaged states, and the ratio threshold
*gFB,thr* determines the magnitude
of the ratio to initiate a transition. When you set **Losses
model** to `No losses — Suitable for HIL
simulation`, *τloss* = 0.

**Estimating Compliance Parameters**

- You can estimate the base transmission stiffness,
  *kp*, from the
  transmission time constant *tc*
  and inertia *J*.

  kp=J(2πtc)2
- You can estimate the base transmission damping
  *kv* from the
  transmission time constant *tc*,
  inertia *J*, and damping coefficient
  *C*.

  kv=2Ctc2π=2CJkp

### Nonideal Torque Transfer and Losses

When you set **Losses model** to `Constant
efficiency`, *τloss* ≠ 0. The block models losses similarly to nonideal gears. For general
information about nonideal gear modeling, see Model Gears with Losses.

In a nonideal gearbox, the angular velocity and compliance dynamics remain the
same as in the ideal case. The transferred torque and power are reduced by:

- Coulomb friction, such as the friction between belt and wheel, or internal
  belt losses due to stretching, characterized by an efficiency
  *η*.
- Viscous coupling of driveshafts with bearings, parametrized by viscous
  friction coefficients, *μ1* and
  *μ2*.

The torque loss in the torque balance equation is due to Coulomb friction, such that

τloss=(1−η)(1+tanh4ppthr2(±gFB(t)τB)+1−tanh4ppthr2τF)

where *pthr* is the
**Follower power threshold** parameter. The block calculates
the viscous shaft frictions as internal damping torques attached to ports
**B** and **F**, such that

τdamper,B=μBωBτdamper,F=μFωF

where the total torque is the sum of
*τB* or
*τF* and its respective damping
torque.
