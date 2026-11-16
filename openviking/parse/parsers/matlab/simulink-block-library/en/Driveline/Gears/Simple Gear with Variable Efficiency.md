---
type: simulink-block
title: 'Simple Gear with Variable Efficiency'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears'
documentation_page: 'simplegearwithvariableefficiency'
documentation_source_path: 'ref/simplegearwithvariableefficiency.html'
language: en
---

# Simple Gear with Variable Efficiency

## Ports

### Input

### **E** — Meshing efficiency physical signal

Physical signal input port associated with the
meshing efficiency of the gear. The block accepts
efficiency in the range (0,1].
### Conserving

### **B** — Base rotational mechanical

Mechanical rotational conserving port
associated with the base shaft.

### **F** — Follower mechanical rotational

Mechanical rotational conserving port
associated with the follower shaft.

### **H** — Heat flow thermal

Thermal conserving port associated with heat
flow. Heat flow affects gear temperature, and
therefore, power transmission efficiency.

#### Dependencies

To enable this port, set **Thermal
port** to
`Model`.

## Parameters

### Main

### **Follower (F) to base (B) teeth ratio (NF/NB)** — Gear ratio `2` (default) | positive scalar

Gear ratio. This is the fraction of follower
over base gear teeth numbers, NF/NB. The ratio
must be positive.

### **Output shaft rotates** — Shaft rotation orientation `In opposite direction to input shaft` (default) | `In same direction as input shaft`

Relative rotation between shafts. This is the
rotation direction of the output shaft with
respect to the input shaft. You can choose either
equal or opposite rotational directions.

### Meshing Losses

### **Minimum efficiency** — Minimum efficiency `0.01` (default) | positive scalar in the range (0,1]

Smallest efficiency value allowed for the
gear. The efficiency is the power ratio between
output and input shafts. The physical signal input
is maintained at values below the minimum
efficiency or above a value of 1. The value must
be positive.

### **Follower power threshold** — Power below which numerical smoothing is applied `0.001` W (default) | positive scalar

Follower shaft power above which full
efficiency factor is in effect. A hyperbolic
tangent function smooths the efficiency factor
between zero, when at rest, and the efficiency set
point.

### Viscous Losses

### **Viscous friction coefficients at base (B) and follower (F)** — Fluid dynamic friction coefficients `[0 0]` `N*m/(rad/s)` (default) | positive two-element vector

Two-element array with the viscous friction coefficients in effect at the base
and follower shafts. The default array corresponds to zero viscous
losses.

### Thermal Port

### **Thermal port** — Whether to model thermal effects `Omit` (default) | `Model`

Whether to model thermal effects and enable
port **H** for
temperature-dependent performance.

### **Thermal mass** — Thermal mass `50` J/K (default) | positive scalar

Thermal energy required to change the
component temperature by a single degree. The
greater the thermal mass, the more resistant the
component is to temperature change.

#### Dependencies

To enable this parameter, set
**Thermal port** to
`Model`.

### **Initial temperature** — Initial temperature `300` K (default) | positive scalar

Component temperature at the start of
simulation. The initial temperature alters the
component efficiency according to an efficiency
vector that you specify, affecting the starting
meshing or friction losses.

#### Dependencies

To enable this parameter, set
**Thermal port** to
`Model`.

## Libraries

Simscape / Driveline / Gears

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013a**

## Description

Gear set with parallel-axis rotation and variable meshing efficiency

The Simple Gear with Variable Efficiency block
represents a simple gear train with variable meshing efficiency. The gear
train transmits torque at a specified ratio between base and follower shafts
arranged in a parallel configuration. Shaft rotation can occur in equal or
opposite directions. Gear losses are optional. They include meshing and
viscous bearing losses. To specify the variable meshing efficiency, the
block contains a physical signal port that you can use to input a general
time-varying signal. Inertia and compliance effects are ignored.

### Simple Gear Model

**Ideal Gear Constraint and Gear Ratio**

Simple Gear imposes one kinematic constraint on the two
connected axes:

|  |  |
| --- | --- |
| *r*F*ω*F = *r*B*ωB*. | **(1)** |

The follower-base gear ratio
*g*FB =
*r*F/*r*B
=
*N*F/*N*B.
*N* is the number of teeth on each
gear. The two degrees of freedom reduce to one independent
degree of freedom.

The torque transfer is:

|  |  |
| --- | --- |
| *g*FB*τ*B + *τ*F – *τ*loss = 0, | **(2)** |

with *τ*loss
= 0 in the ideal case.

### Nonideal Gear Constraint and Losses

In the nonideal case, *τ*loss
≠ 0. For general considerations on nonideal gear
modeling, see Model Gears with Losses.

### Thermal Model

You can model
the effects of heat flow and temperature change by enabling the optional thermal port. To enable
the port, set **Friction model** to `Temperature-dependent
efficiency`.

### Variables

Use the **Variables** settings to set the priority and initial target
values for the block variables before simulating. For more information, see Set Priority and Initial Target for Block Variables.
