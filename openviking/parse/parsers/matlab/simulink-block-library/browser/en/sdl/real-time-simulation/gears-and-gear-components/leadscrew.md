---
type: simulink-block
title: 'Leadscrew'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Gears / Translational Mechanisms'
documentation_page: 'leadscrew'
documentation_source_path: 'ref/leadscrew.html'
language: en
---

# Leadscrew

## Ports

### Conserving

### **S** — Screw mechanical rotational

Mechanical rotational conserving port associated with the
screw.

### **N** — Nut mechanical translational

Mechanical translational conserving port associated with the
nut.

### **H** — Heat flow thermal

Thermal conserving port associated with heat flow.

## Parameters

### Main

### **Screw lead** — Nut displacement per revolution `0.015` m (default) | positive scalar

Translational displacement *L* of the nut per
revolution of the screw.

### **Screw helix type** — Rotational directional sense `Right-hand` (default) | `Left-hand`

Choose the directional sense of screw rotation corresponding to
positive nut translation. For the `Right-hand`
orientation, the screw angular velocity and the nut velocity have the
same sign.

### Meshing Losses

### **Friction model** — Screw friction model `No meshing losses — Suitable for HIL simulation` (default) | `Constant efficiency` | `Temperature-dependent efficiency`

- `No meshing losses — Suitable for HIL
  simulation` — Screw meshing is
  ideal.
- `Constant efficiency` —
  Transfer of torque between screw and nut is reduced by
  friction.
- `Temperature-dependent
  efficiency` — Torque transfer is
  determined from user-supplied data for screw-nut efficiency,
  nut-screw efficiency, and temperature.

### **Friction parametrization** — Friction losses from nonideal meshing of gear threads `Friction coefficient and geometrical parameters` (default) | `Efficiencies`

- `Friction coefficient and geometrical
  parameters` — Friction is determined by
  contact friction between surfaces.
- `Efficiencies` — Friction is
  determined by constant efficiencies 0 < *η* < 1.

#### Dependencies

To enable this parameter, set **Friction model**
to `Constant efficiency`.

### **Lead angle** — Thread helix angle `15` deg (default) | positive scalar

Thread helix angle *λ* =
arctan[*L*/(*π**d*)], where:

- *L* is the screw lead.
- *d* is the screw pitch diameter.

The value must be greater than zero.

#### Dependencies

To enable this parameter, set **Friction model**
to `Constant efficiency` and
**Friction parameterization** to
`Friction coefficient and geometrical
parameters`.

### **Acme thread half angle** — Thread half-angle `14.5` deg (default) | positive scalar

Half-angle of the acme thread *α* in the normal
plane. In the case of a square thread, *α* = 0. The value must be greater than zero.

#### Dependencies

To enable this parameter, set **Friction model**
to `Constant efficiency` and
**Friction parameterization** to
`Friction coefficient and geometrical
parameters`.

### **Friction coefficient** — Thread friction coefficient `0.08` (default) | positive scalar

Dimensionless coefficient of normal friction in the thread. The value
must be greater than zero.

#### Dependencies

To enable this parameter, set **Friction model**
to `Constant efficiency` and
**Friction parameterization** to
`Friction coefficient and geometrical
parameters`.

### **Screw-nut efficiency** — Efficiency from screw to nut `0.75` (default) | positive scalar in the range of (0,1]

Efficiency *η*SN of the power
transfer from screw to nut.

#### Dependencies

To enable this parameter, set **Friction model**
to `Constant efficiency` and
**Friction parameterization** to
`Efficiencies`.

### **Nut-screw efficiency** — Efficiency from nut to screw `0.45` (default) | positive scalar in the range of (0,1]

Efficiency *η*NS of the power
transfer from nut to screw.

#### Dependencies

To enable this parameter, set **Friction model**
to `Constant efficiency` and
**Friction parameterization** to
`Efficiencies`.

### **Temperature** — Array for tabular parameterization of efficiency `[280 300 320]` K (default) | vector

Array of temperatures used to construct a 1-D temperature-efficiency
lookup table. The array values must increase left to right. The
temperature array must be the same size as the **Screw-nut
efficiency** and **Nut-screw
efficiency** arrays.

#### Dependencies

To enable this parameter, set **Friction model**
to `Temperature-dependent
efficiency`.

### **Screw-nut efficiency** — Array of screw-to-nut efficiencies `[0.75 0.7 0.65]` (default) | vector

Array of component efficiencies with the screw as the driver—
that is, with power from the screw to the nut. The array values are the
efficiencies at the temperatures in the **Temperature**
array. The two arrays must be the same size.

#### Dependencies

To enable this parameter, set **Friction model**
to `Temperature-dependent
efficiency`.

### **Nut-screw efficiency** — Array of nut-to-screw efficiencies `[0.5 0.45 0.4]` (default) | vector

Array of component efficiencies with the nut as the driver—
that is, with power flowing from the nut to the screw. The array values
are the efficiencies at the temperatures in the
**Temperature** array. The two arrays must be the
same size.

#### Dependencies

To enable this parameter, set **Friction model**
to `Temperature-dependent
efficiency`.

### **Power threshold** — Power below which numerical smoothing is applied `0.001` W (default) | positive scalar

Power threshold above which full efficiency factor is in effect. A
hyperbolic tangent function smooths the efficiency factor between zero
at rest and the current efficiency set point.

### Viscous Losses

### **Viscous friction coefficient** — Fluid dynamic friction coefficient `0` N\*m/(rad/s) (default) | positive scalar

Viscous friction coefficient
*μ*S for the screw.

### Thermal Port

### **Thermal mass** — Thermal mass `50` `J/K` (default) | positive scalar

Thermal energy required to change the component temperature by a single
degree. The greater the thermal mass, the more resistant the component is to
temperature change.

### **Initial temperature** — Initial temperature `300` `K` (default) | positive scalar

Component temperature at the start of simulation. The initial temperature
alters the component efficiency according to an efficiency vector that you
specify, affecting the starting meshing or friction losses.

## Libraries

Simscape / Driveline / Gears / Rotational- Translational

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011a**

## Description

Leadscrew gear set of threaded rotating screw and translating nut, with adjustable thread and friction losses

The Leadscrew block represents a threaded rotational-translational gear that
constrains the two connected driveline axes, screw (S) and nut (N), to, respectively,
rotate and translate together in a fixed ratio that you specify. You can choose whether
the nut axis translates in a positive or negative direction, as the screw rotates in a
positive right-hand direction. If the screw helix is right-hand,
*ω*S and
*v*N have the same sign. If the screw helix
is left-hand, *ω*S and
*v*N have opposite signs.

### Ideal Nut Constraint and Transmission Ratio

The block imposes one kinematic constraint on the two connected axes:

|  |  |
| --- | --- |
| *ω*S*L* = 2*π**v*N. | **(1)** |

The transmission ratio is *R*NS =
2*π*/*L*. *L* is the screw lead, the translational
displacement of the nut for one turn of the screw. In terms of this ratio, the
kinematic constraint is:

|  |  |
| --- | --- |
| *ω*S = *R*NS*v*N. | **(2)** |

The two degrees of freedom are reduced to one independent degree of freedom. The
forward-transfer gear pair convention is (1,2) = (S,N).

The torque-force transfer is:

|  |  |
| --- | --- |
| *R*NS*τ*S + *F*N – *F*loss = 0, | **(3)** |

with *F*loss = 0 in the ideal case.

### Nonideal Nut Constraint and Losses

In the nonideal case, *F*loss ≠ 0. For general considerations on nonideal gear modeling, see Model Gears with Losses.

**Geometric Surface Contact Friction**

In the contact friction case, *η*SN
and *η*NS are determined by:

- The screw-nut threading geometry, specified by lead angle
  *λ* and acme thread half-angle
  *α*.
- The surface contact friction coefficient *k*.

|  |  |
| --- | --- |
| *η*SN = (cos*α* – *k*·tan*α*)/(cos*α* + *k*/tan*λ*), | **(4)** |

|  |  |
| --- | --- |
| *η*NS = (cos*α* – *k*/tan*λ*)/(cos*α* + *k*·tan*α*). | **(5)** |

**Constant Efficiencies**

In the constant efficiency case, you specify
*η*SN and
*η*NS, independently of geometric
details.

**Self-Locking and Negative Efficiency**

*η*NS has two distinct regimes,
depending on lead angle *λ*, separated by the
*self-locking point* at which *η*NS = 0 and cos*α* =
*k*/tan*λ*.

- In the *overhauling regime*, *η*NS >
  0. The force acting on the nut can rotate the
  screw.
- In the *self-locking regime*, *η*NS <
  0. An external torque must be applied to the screw to
  release an otherwise locked mechanism. The more negative is
  *η*NS, the larger the torque
  must be to release the mechanism.

*η*SN is conventionally
positive.

### Meshing Efficiency

The efficiencies *η* of meshing between screw and nut are fully
active only if the transmitted power is greater than the power threshold.

If the power is less than the threshold, the actual efficiency is automatically
regularized to unity at zero velocity.

### Viscous Friction Force

The viscous friction coefficient *μ* controls the viscous
friction torque experienced by the screw from lubricated, nonideal gear threads. The
viscous friction torque on a screw driveline axis is
–*μ*S*ω*S.
*ω*S is the angular velocity of the
screw with respect to its mounting.

### Thermal Modeling

You can model
the effects of heat flow and temperature change by enabling the optional thermal port. To enable
the port, set **Friction model** to `Temperature-dependent
efficiency`.

### Hardware-in-the-Loop Simulation

For optimal performance of your real-time simulation, set the **Friction
model** to `No meshing losses - Suitable for HIL
simulation` on the **Meshing Losses** tab.

### Variables

Use the **Variables** settings to set the priority and initial target
values for the block variables before simulating. For more information, see Set Priority and Initial Target for Block Variables.
