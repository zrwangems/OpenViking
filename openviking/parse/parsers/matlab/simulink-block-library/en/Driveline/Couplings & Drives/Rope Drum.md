---
type: simulink-block
title: 'Rope Drum'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'ropedrum'
documentation_source_path: 'ref/ropedrum.html'
language: en
---

# Rope Drum

## Ports
```yaml
ports:
- name: S
  summary: Drum shaft mechanical rotational
  direction: conserving
- name: A
  summary: Rope end A mechanical translational
  direction: conserving
- name: B
  summary: Rope end B mechanical translational
  direction: conserving
```

### Conserving

### **S** — Drum shaft mechanical rotational

Mechanical rotational conserving port associated with the drum
shaft.

### **A** — Rope end A mechanical translational

Mechanical translational conserving port associated with rope end
A.

### **B** — Rope end B mechanical translational

Mechanical translational conserving port associated with rope end
B.
## Parameters
```yaml
parameters:
- name: Drum radius
  summary: Size of drum 0.10 m (default) | positive scalar
  group: Rope Winding
- name: Rope windup type
  summary: Direction of B rope end with respect to A rope end Ends move in same direction (default) | Ends move in opposite
    direction
  group: Rope Winding
- name: Tension warning
  summary: Optional lost tension warning Do not check tension (default) | Warn if either end loses tension
  group: Rope Winding
- name: Bearing viscous friction coefficient
  summary: Viscous friction for drum rotation 0.001 N*m/(rad/s) (default) | nonnegative scalar
  group: Drum Dynamics
- name: Inertia
  summary: Resistance to angular acceleration No inertia (default) | Specify inertia and initial velocity
  group: Drum Dynamics
- name: Drum inertia
  summary: Drum tendency to remain in motion 0.01 kg*m^2 (default) | positive scalar
  group: Drum Dynamics
- name: Drum initial velocity
  summary: Initial drum state 0 rad/s (default) | scalar
  group: Drum Dynamics
```

### Rope Winding

### **Drum radius** — Size of drum `0.10` `m` (default) | positive scalar

Distance between the drum center and its periphery. The drum periphery
coincides with the contact surface between the drum and the rope.

### **Rope windup type** — Direction of B rope end with respect to A rope end `Ends move in same direction` (default) | `Ends move in opposite direction`

Relative direction of the translation motion of the two rope ends, A and B, where B is
the following end.

### **Tension warning** — Optional lost tension warning `Do not check tension` (default) | `Warn if either end loses tension`

Option to generate a warning when a rope end becomes slack. A rope end becomes slack
when the net tensile forces responsible for keeping it taut fall below
zero. Because slack cables do not transmit force, the simulation results
may not be accurate when the rope loses tension.

### Drum Dynamics

### **Bearing viscous friction coefficient** — Viscous friction for drum rotation `0.001` `N*m/(rad/s)` (default) | nonnegative scalar

Linear damping coefficient in effect at the drum bearing. This coefficient determines
the power losses due to viscous friction at a given drum angular
velocity.

### **Inertia** — Resistance to angular acceleration `No inertia` (default) | `Specify inertia and initial velocity`

Option to account for drum inertia.

- `No inertia` — Select this setting if
  drum inertia has a negligible impact on driveline dynamics. This
  setting sets drum inertia to zero.
- `Specify inertia and initial
  velocity` — Select this setting if drum inertia
  has a significant impact on driveline dynamics.

### **Drum inertia** — Drum tendency to remain in motion `0.01` `kg*m^2` (default) | positive scalar

Moment of inertia of the drum about its rotation axis. In the simple
case of a solid cylindrical drum, the moment of inertia is

I=12MR2,

where *M* is the drum mass and
*R* is the drum radius.

#### Dependencies

To enable this parameter, set **Inertia** to `Specify
inertia and initial velocity`.

### **Drum initial velocity** — Initial drum state `0` `rad/s` (default) | scalar

Angular velocity of the drum at the start of the simulation.

#### Dependencies

To enable this parameter, set **Inertia** to `Specify
inertia and initial velocity`.
## Libraries

Simscape / Driveline / Couplings & Drives

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012a**

## Description

Power transmission system with tightly wound rope around cylindrical drum

The Rope Drum block represents a power transmission system
where a rope is tightly wound around a cylindrical drum at a sufficient tension level to
prevent slipping. You can configure the rope so that the ends point in the same or
opposite directions. You can set the direction that the ends move with the
**Rope windup type** parameter:

- If the rope ends point in the same direction, they translate in opposite
  directions.
- If the rope ends point in opposite directions, they translate in the same
  direction.

The equations refer to rope ends A and B, as illustrated by the figure.

When rope ends A and B point in the same direction, they translate in opposite directions. When rope ends A and B point in opposite directions, they translate in the same direction.

During normal operation, a driving torque causes the cylindrical drum to rotate about its
axis of symmetry. The rotating drum transmits tensile force to the rope ends, which
translate with respect to the drum centerline. The relative direction of translation
between the two rope ends depends on the setting of the **Rope windup
type** parameter. However, a positive drum rotation always corresponds to a
positive translation at port **A**.

The block assumes that each rope end remains taut during simulation because slack rope ends
do not transmit force. You can set the block to warn you if the rope loses
tension.

You can optionally set parameters for:

- Drum inertia
- Viscous friction at the drum bearing

The block balances the torques and forces, such that

T=FB·R·δ−FA·R+μ·ω,

where:

- *T* is the external torque acting on the drum. Due to
  torque balance, the external torque acting on the drum is the negative of
  the net torque applies by forces acting on the rope ends.
- *F*A and
  *F*B are the external forces
  pulling on rope ends A and B.
- *R* is the drum radius.
- *μ* is the viscous friction coefficient at the drum
  bearings.
- *ω* is the drum angular velocity.
- *δ* is the rope windup type according to the parameter settings:

  - When you set **Rope windup type** to
    `Ends move in the same direction`,
    *δ = -1*.
  - When you set **Rope windup type** to
    `Ends move in the opposite
    directions`, *δ = +1*.

The figure shows a crossed rope configuration and an open rope
configuration, which correspond to the `Ends move in the same
direction` and `Ends move in the opposite
directions` settings, respectively.

Variables associated with the Rope Drum demonstrated in the cross rope configuration and open rope configuration.

The translational velocities of the two rope ends are functions of the drum radius and
angular velocity. Each translational velocity is equal to the tangential velocity of a
point at the drum periphery according to the expressions

VA=ωRVB=δωR

where:

- *V*A is the translational velocity
  of rope end A.
- *V*B is the translational velocity
  of rope end B.

### Assumptions and Limitations

- The
  block ignores slip at the rope-drum contact surface.
- The block ignores rope compliance.
