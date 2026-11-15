---
type: simulink-block
title: 'Worm Gear'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Gears / Gear Assemblies'
documentation_page: 'wormgear'
documentation_source_path: 'ref/wormgear.html'
language: en
---

# Worm Gear

## Ports

### Conserving

### **W** — Worm mechanical rotational

Rotational conserving port representing the worm torque and angular
velocity.

### **G** — Gear mechanical rotational

Rotational conserving port representing the gear torque and angular
velocity.

### **H** — Optional heat transfer port mechanical translational

Thermal conserving port for thermal modeling.

#### Dependencies

To enable this port, set **Friction model** to
either:

- `Temperature-dependent
  efficiency`
- `Temperature and load-dependent
  efficiency`

.

## Parameters

### Main

### **Gear ratio** — Ratio of angular velocities `25` (default) | positive scalar greater than 1

Gear or transmission ratio
*RWG* determined as the
ratio of the worm angular velocity to the gear angular velocity.

### **Worm thread type** — Rotational orientation `Right-hand` (default) | `Left-hand`

Choose the directional sense of gear rotation corresponding to
positive worm rotation. If you select `Left-hand`,
rotation of the worm in the generally-assigned positive direction
results in the gear rotation in negative direction.

### Meshing Losses

### **Friction model** — Gear friction model `No meshing losses — Suitable for HIL simulation` (default) | `Constant efficiency` | `Temperature-dependent efficiency`

- `No meshing losses — Suitable for HIL
  simulation` — Gear meshing is
  ideal.
- `Constant efficiency` —
  Transfer of torque between worm and gear is reduced by
  friction.
- `Temperature-dependent
  efficiency` — Torque transfer is
  determined from user-supplied data for worm-gear efficiency,
  gear-worm efficiency, and temperature.

### **Friction parametrization** — Friction losses from nonideal meshing of gear threads `Friction coefficient and geometrical parameters` (default) | `Efficiencies`

- `Friction coefficient and geometrical
  parameters` — Friction is determined by
  contact friction between surfaces.
- `Efficiencies` — Friction is
  determined by constant efficiencies 0 < *η* < 1.

#### Dependencies

To enable this parameter, set **Friction model**
to `Constant efficiency`.

### **Normal pressure angle** — Thread pressure angle `17.5` deg (default) | positive scalar

Thread pressure angle *α* in the normal plane. The
value must be greater than zero and less than 90 degrees.

#### Dependencies

To enable this parameter, set **Friction model**
to `Constant efficiency` and
**Friction parameterization** to
`Friction coefficient and geometrical
parameters`.

### **Lead angle** — Thread helix angle `20` deg (default) | positive scalar

Thread helix angle *λ* =
arctan[*L*/(*π**d*)], where:

- *L* is the worm lead.
- *d* is the worm pitch diameter.

The value must be greater than zero.

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

### **Worm-gear efficiency** — Efficiency from worm to gear `0.74` (default) | positive scalar in the range of (0,1]

Efficiency *η*WG of the power
transfer from worm to gear.

#### Dependencies

To enable this parameter, set **Friction model**
to `Constant efficiency` and
**Friction parameterization** to
`Efficiencies`.

### **Gear-worm efficiency** — Efficiency from gear to worm `0.65` (default) | positive scalar in the range of (0,1]

Efficiency *η*GW of the power
transfer from gear to worm.

#### Dependencies

To enable this parameter, set **Friction model**
to `Constant efficiency` and
**Friction parameterization** to
`Efficiencies`.

### **Temperature** — Array for tabular parameterization of efficiency `[280 300 320]` K (default) | vector

Array of temperatures used to construct a 1-D temperature-efficiency
lookup table. The array values must increase left to right. The
temperature array must be the same size as the **Worm-gear
efficiency** and **Gear-worm efficiency**
arrays.

#### Dependencies

To enable this parameter, set **Friction model**
to `Temperature-dependent
efficiency`.

### **Worm-gear efficiency** — Array of worm-to-gear efficiencies `[0.75 0.7 0.65]` (default) | vector

Array of component efficiencies with the worm as the driver—
that is, with power flowing from the worm to the gear. The array values
are the efficiencies at the temperatures in the
**Temperature** array. The two arrays must be the
same size.

#### Dependencies

To enable this parameter, set **Friction model**
to `Temperature-dependent
efficiency`.

### **Gear-worm efficiency** — Array of gear-to-worm efficiencies `[0.5 0.45 0.4]` (default) | vector

Array of component efficiencies with the gear as the driver—
that is, with power flowing from the gear to the worm. The array values
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

### **Viscous friction coefficients at worm (W) and gear (G)** — Fluid dynamic friction coefficient `[0 0]` N\*m/(rad/s) (default) | positive two-element vector

Vector of viscous friction coefficients
[*μ*W
*μ*G], for the worm and gear,
respectively.

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

Simscape / Driveline / Gears

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011a**

## Description

Worm gear with adjustable gear ratio and friction losses

The block represents a rotational gear that constrains the two connected driveline
axes, worm (W) and gear (G), to rotate together in a fixed ratio that you specify. You
can choose whether the gear rotates in a positive or negative direction. Right-hand
rotation is the positive direction. If the worm thread is right-hand,
*ω*W and
*ω*G have the same sign. If the worm thread
is left-hand, *ω*W and
*ω*G have opposite signs.

### Thermal Model

You can model
the effects of heat flow and temperature change by enabling the optional thermal port. To enable
the port, set **Friction model** to `Temperature-dependent
efficiency`.

### Model Variables

|  |  |
| --- | --- |
| *R*WG | Gear ratio |
| *ω*W | Worm angular velocity |
| *ω*G | Gear angular velocity |
| *α* | Normal pressure angle |
| *λ* | Worm lead angle |
| *L* | Worm lead |
| *d* | Worm pitch diameter |
| *τ*G | Gear torque |
| *τ*W | Torque on the worm |
| *τ*loss | Torque loss due to meshing friction. The loss depends on the device efficiency and the power flow direction. To avoid abrupt change of the friction torque at *ω*G = 0, the friction torque is introduced via the hyperbolic function. |
| *τ*fr | Steady-state value of the friction torque at *ω*G → ∞. |
| *k* | Friction coefficient |
| *ηWG* | Torque transfer efficiency from worm to gear |
| *ηGW* | Torque transfer efficiency from gear to worm |
| *p*th | Power threshold |
| [*μ*W *μ*G] | Vector of viscous friction coefficients for the worm and gear |

### Ideal Gear Constraint and Gear Ratio

Worm gear imposes one kinematic constraint on the two connected axes:

|  |  |
| --- | --- |
| *ω*W = *R*WG*ω*G. | **(1)** |

The two degrees of freedom are reduced to one independent degree of freedom. The
forward-transfer gear pair convention is (1,2) = (W,G).

The torque transfer is:

|  |  |
| --- | --- |
| *R*WG*τ*W – *τ*G – *τ*loss = 0, | **(2)** |

with *τ*loss = 0 in the ideal case.

### Nonideal Gear Constraint

In the nonideal case, *τ*loss ≠ 0. For general considerations on nonideal gear modeling, see Model Gears with Losses.

**Geometric Surface Contact Friction**

In the contact friction case, *η*WG
and *η*GW are determined by:

- The worm-gear threading geometry, specified by lead angle
  *λ* and normal pressure angle
  *α*.
- The surface contact friction coefficient *k*.

|  |  |
| --- | --- |
| *η*WG = (cos*α* – *k*·tan*λ*)/(cos*α* + *k*/tan*λ*) | **(3)** |

|  |  |
| --- | --- |
| *η*GW = (cos*α* – *k*/tan*λ*)/(cos*α* + *k*·tan*λ*) | **(4)** |

**Constant Efficiencies**

In the constant friction case, you specify
*η*WG and
*η*GW, independently of geometric
details.

**Self-Locking and Negative Efficiency**

*η*GW has two distinct regimes,
depending on lead angle *λ*, separated by the
*self-locking point* at which *η*GW = 0 and cos*α* =
*k*/tan*λ*.

- In the *overhauling regime*, *η*GW >
  0, and the force acting on the nut can rotate the
  screw.
- In the *self-locking regime*, *η*GW <
  0, and an external torque must be applied to the screw
  to release an otherwise locked mechanism. The more negative is
  *η*GW, the larger the torque
  must be to release the mechanism.

*η*WG is conventionally
positive.

### Meshing Efficiency

The efficiencies *η* of meshing between worm and gear are fully
active only if the transmitted power is greater than the power threshold.

If the power is less than the threshold, the actual efficiency is automatically
regularized to unity at zero velocity.

You can set the meshing losses friction model to:

- `No meshing losses - suitable for HIL
  simulation`.
- `Constant efficiency`, which is the default
  friction setting for block versions prior to R2020b.
- `Temperature-dependent efficiency`, which
  models variability in the base-shaft efficiencies calculated in the
  `Constant efficiency` setting according to
  a user-supplied look-up table. The temperature-dependency setting
  enables a thermal conserving port **H**. This port
  receives the heat flow into the block, which is translated into the
  block temperature according to the gear **Thermal
  mass**.

### Viscous Friction Force

The viscous friction coefficient *μ*W
controls the viscous friction torque experienced by the worm from lubricated,
nonideal gear threads and viscous bearing losses. The viscous friction torque on a
worm driveline axis is
–*μ*W*ω*W.
*ω*W is the angular velocity of the worm
with respect to its mounting.

The viscous friction coefficient *μ*G
controls the viscous friction torque experienced by the gear, mainly from viscous
bearing losses. The viscous friction torque on a gear driveline axis is
–*μ*G*ω*G.
*ω*G is the angular velocity of the gear
with respect to its mounting.

### Hardware-in-the-Loop Simulation

For optimal performance of your real-time simulation, set the **Friction
model** to `No meshing losses - Suitable for HIL
simulation` on the **Meshing Losses** tab.

### Variables

Use the **Variables** settings to set the priority and initial target
values for the block variables before simulating. For more information, see Set Priority and Initial Target for Block Variables.

### Limitations

- Gear inertia is assumed to be negligible.
- Gears are treated as rigid components.
- Coulomb friction slows down simulation. For more information, see Adjust Model Fidelity.
