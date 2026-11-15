---
type: simulink-block
title: 'Rack & Pinion'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Gears / Translational Mechanisms'
documentation_page: 'rackpinion'
documentation_source_path: 'ref/rackpinion.html'
language: en
---

# Rack & Pinion

## Ports

Not documented in R2025b.

## Parameters

### Main

### **Parameterize by** — Rack and gear parameterization method `Pinion radius` (default) | `Tooth parameters`

Parameterization method of the rack and pinion gear.

- `Pinion radius` — Gear
  ratio is defined by the effective radius of the
  pinion.
- `Tooth parameters` — Gear
  ratio is defined by the number of teeth on the pinion gear
  and the rack tooth spacing.

### **Pinion radius** — Pinion effective radius `100` mm (default) | positive scalar

Effective radius of the pinion
*r*P. The value must be
greater than zero.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Pinion radius`.

### **Number of pinion teeth** — Number of pinion teeth `20` (default) | positive scalar

Number of teeth on the pinion
*N*P. The value must be
greater than zero.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Tooth parameters`.

### **Rack tooth spacing** — Space between rack and teeth `5` mm (default) | positive scalar

Spacing between the teeth on the rack
*x*R. The value must be
greater than zero.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Tooth parameters`.

### **Rack direction** — Rack rotational orientation `Positive for positive pinion rotation` (default) | `Negative for positive pinion rotation`

Choose whether the rack axis translates in a positive or negative
direction when the pinion rotates in a positive direction.

### Meshing Losses

### **Friction model** — Friction losses from nonideal meshing of gear threads `No meshing losses — Suitable for HIL simulation` (default) | `Constant efficiency` | `Temperature-dependent efficiency`

- `No meshing losses — Suitable for HIL
  simulation` — Gear meshing is
  ideal.
- `Constant efficiency` —
  Transfer of torque between rack and pinion is reduced by
  friction.
- `Temperature-dependent
  efficiency` — Torque transfer is
  determined from user-supplied data for efficiency and
  temperature.

### **Efficiency** — Torque transfer efficiency `0.8` (default) | positive scalar in the range of (0,1]

Torque transfer efficiency *η* for the rack-pinion
gear meshing, which is the same for the forward and reverse power flows.
Must be greater than zero but less than, or equal to, one.

#### Dependencies

To enable this parameter, set **Friction model**
to `Constant efficiency`.

### **Temperature** — Array for tabular parameterization of efficiency `[280 300 320]` K (default) | vector

Array of temperatures used to construct a 1-D temperature-efficiency
lookup table. The array values must increase left to right. The
temperature array must be the same size as the
**Efficiency** array.

#### Dependencies

To enable this parameter, set **Friction model**
to `Temperature-dependent
efficiency`.

### **Efficiency** — Array of efficiencies `[0.95 0.9 0.85]` (default) | vector

Array of component efficiencies used to construct a 1-D
temperature-efficiency lookup table. The array values are the
efficiencies at the temperatures in the **Temperature**
array. The two arrays must be the same size.

#### Dependencies

To enable this parameter, set **Friction model**
to `Temperature-dependent
efficiency`.

### **Rack power threshold** — Power below which numerical smoothing is applied `0.001` W (default) | positive scalar

Power threshold above which the full efficiency factor is in effect.
Below this value, a hyperbolic tangent function smooths the efficiency
factor, lowering the efficiency losses to zero when no power is
transmitted.

### Viscous Losses

### **Pinion rotational viscous friction coefficient** — Pinion fluid dynamic friction coefficient `0` N\*m/(rad/s) (default) | positive scalar

Viscous friction coefficient
*μ*P for the pinion
shaft.

### **Rack translational viscous friction coefficient** — Numerical constant `0` N/(m/s) (default) | positive scalar

Viscous friction coefficient
*μ*R for the rack
motion.

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

Rack and pinion gear coupling translational and rotational motion, with adjustable pinion radius and friction losses

The Rack & Pinion block represents rack and pinion gear that converts between
translational and rotational motion. The rotational-translational gear constrains the
pinion (P) and rack (R) to, respectively, rotate and translate together in a fixed ratio
that you specify. You can choose whether the rack axis translates in a positive or
negative direction, as the pinion rotates in a positive direction, by using the
**Rack direction** parameter.

### Model Variables

|  |  |
| --- | --- |
| *R*RP | Rack-pinion gear ratio |
| *ω*P | Angular velocity of the pinion shaft |
| *v*R | Translational velocity of the rack |
| *r*P | Effective radius of the pinion |
| *N*P | Number of teeth on the pinion |
| *x*R | Rack tooth spacing |
| *τ*P | Pinion shaft torque |
| *F*R | Rack force |
| *F*loss | Total loss force |
| *F*Coul | Friction force |
| *η* | Torque transfer efficiency |
| *p*th | Power threshold |
| *μ*P | Viscous friction coefficient for the pinion shaft |
| *μ*R | Viscous friction coefficient for the rack motion |

### Ideal Gear Constraint and Gear Ratio

Rack & Pinion imposes one kinematic constraint on the two connected
axes:

|  |  |
| --- | --- |
| *ω*P = *R*RP*v*R. | **(1)** |

The transmission ratio is:

|  |  |
| --- | --- |
| *R*RP = 1 / *r*P = *ω*P / *v*N = ± 2*π* / *N*P*v*R. | **(2)** |

The two degrees of freedom are reduced to one independent degree of freedom. The
forward-transfer gear pair convention is (1,2) = (P,R).

The torque-force transfer is:

|  |  |
| --- | --- |
| *R*RP*τ*P + *F*R – *F*loss = 0, | **(3)** |

with *F*loss = 0 in the ideal case.

### Nonideal Gear Constraint

In the nonideal case, *F*loss ≠ 0. For general considerations on nonideal gear modeling, see Model Gears with Losses.

In a nonideal pinion-rack pair (P,R), the angular velocity and geometric
constraints are unchanged. But the transferred torque, force, and power are reduced
by:

- Coulomb friction between teeth surfaces on P and R, characterized by
  constant efficiency *η*
- Viscous coupling of driveshafts with bearings, parametrized by viscous
  friction coefficients *μ*

### Meshing Efficiency

The efficiency *η* of meshing between pinion and rack is fully
active only if the transmitted power is greater than the power threshold.

If the power is less than the threshold, the actual efficiency is automatically
regularized to unity at zero velocity.

Efficiency is assumed equal for both the forward and reverse power flow.

### Viscous Friction Force

The viscous friction coefficients *μ*P and
*μ*R control the viscous friction torque
and force experienced by the rack and pinion from lubricated, nonideal bearings. The
viscous friction torque on the pinion axis is
–*μ*P*ω*P.
The viscous friction force on the rack motion is
–*μ*R*v*R.

### Thermal Model

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
