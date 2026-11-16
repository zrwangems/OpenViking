---
type: simulink-block
title: 'Limited-Slip Differential'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Gears / Gear Assemblies'
documentation_page: 'limitedslipdifferential'
documentation_source_path: 'ref/limitedslipdifferential.html'
language: en
---

# Limited-Slip Differential

## Ports

### Conserving

### **D** — Driving shaft rotational mechanical

Rotational mechanical conserving port associated with the
driveshaft.

### **S1** — Sun gear 1 rotational mechanical

Rotational mechanical conserving port associated with the sun gear 1
shaft.

### **S2** — Sun gear 2 rotational mechanical

Rotational mechanical conserving port associated with the sun gear 2
shaft.

### **H** — Heat flow thermal

Thermal conserving port associated with heat flow.

#### Dependencies

To enable this port, in the **Differential** tab,
set **Friction model** to
`Temperature-dependent
efficiency`.

## Parameters

### Differential

### **Crown gear located** — Crown gear location `To the right of centerline` (default) | `To the left of centerline`

Location of the bevel crown gear relative to the centerline of the
gear assembly.

### **Carrier (C) to driveshaft (D) teeth ratio (NC/ND)** — Crown gear to driveshaft pinion gear teeth ratio `4` (default) | positive scalar

Fixed ratio, *gD*, of the
number of crown gear teeth *NC* to the number of
driveshaft pinion gear teeth *ND*. This gear ratio must
be strictly greater than `0`. The crown gear is rigidly
mounted to the carrier.

### **Friction model** — Friction model `No meshing losses - Suitable for HIL simulation` (default) | `Constant efficiency` | `Temperature-dependent efficiency`

Friction model for the block:

- `No meshing losses - Suitable for HIL
  simulation`— Gear meshing is ideal.
- `Constant efficiency`— Transfer of
  torque between the gear wheel pairs is reduced by a constant
  efficiency, *η*, such that 0<η≤1.
- `Temperature-dependent efficiency`—
  Transfer of torque between the gear wheel pairs is defined by
  the temperature lookup table

### **Sun-sun and carrier-driveshaft ordinary efficiencies** — Differential torque constant transfer efficiencies `[.85, .92]` (default) | vector

Vector of torque transfer efficiencies,
[*ηSS*,
*ηCD*]. Here,

- *ηSS* is the
  output-to-input power ratio that describes the power flow
  from the driving sun gear to the driven sun gear.
- *ηCD* is the
  output-to-input power ratio that describes the power flow
  from the crown gear to the driveshaft pinion gear.

The carrier is rigidly mounted to the crown gear. The
vector elements must be in the range (0,1].

#### Dependencies

To enable this parameter, set **Friction model**
to `Constant efficiency`.

### **Temperature** — Temperature `[280, 300, 320]` `K` (default) | vector

Vector of temperatures used to construct a 1-D temperature-efficiency lookup table.
The vector elements must increase from left to right.

#### Dependencies

To enable this parameter, set **Friction model** to
`Temperature-dependent efficiency`.

### **Sun-sun efficiency** — Torque transfer efficiency from the driving sun gear to the driven sun gear `[.95, .9, .85]` (default) | vector

Vector of output-to-input power ratios that describe the power flow
from the driving sun gear to the driven sun gear,
*ηSS*. The block uses
the values to construct a 1-D temperature-efficiency lookup
table.

Each element is an efficiency that
relates to a temperature in the **Temperature** vector.
The length of the vector must be equal to the length of the
**Temperature** vector. Each element in the vector
must be in the range (0,1].

#### Dependencies

To enable this parameter, set **Friction model**
to `Temperature-dependent
efficiency`.

### **Carrier-driveshaft efficiency** — Torque transfer efficiency from the crown gear to the driveshaft pinon gear `[.95, .9, .85]` (default) | vector

Vector of output-to-input power ratios that describe the power flow
from the crown gear to the driveshaft pinion gear,
*ηCD*. The block uses
the values to construct a 1-D temperature-efficiency lookup table. The
carrier gear is rigidly mounted to the crown gear.

Each element is an efficiency that
relates to a temperature in the **Temperature** vector.
The length of the vector must be equal to the length of the
**Temperature** vector. Each element in the vector
must be in the range (0,1].

#### Dependencies

To enable this parameter, set **Friction model**
to `Temperature-dependent
efficiency`.

### **Sun-carrier and driveshaft-casing power thresholds** — Minimum efficiency power thresholds for the sun gear to the crown gear and driveshaft-casing gear couplings `[.001, .001]` `W` (default) | vector

Vector of power thresholds,
*pth*, for sun-carrier and
longitudinal driveshaft-casing
[*pS*,
*pD*], respectively. The
full efficiency loss applies above these values. Below these values, a
hyperbolic tangent function smooths the efficiency factor.

When you set **Friction model** to
`Constant efficiency`, the block lowers the
efficiency losses to zero when no power is transmitted. When you set
**Friction model** to
`Temperature-dependent efficiency`, the
block smooths the efficiency factors between zero when at rest and the
values provided by the temperature-efficiency lookup tables at the power
thresholds.

#### Dependencies

To enable this parameter, set **Friction model**
to `Constant efficiency` or
`Temperature-dependent
efficiency`.

### **Sun-carrier and driveshaft-casing viscous friction coefficients** — Viscous friction coefficients `[0, 0]` `N*m/(rad/s)` (default) | vector

Vector
of viscous friction coefficients
[*μS*,
*μD*] for the
sun-carrier and longitudinal driveshaft-casing gear motions,
respectively.

### **Inertia** — Inertia option `off` (default) | `on`

Whether to include the effects of inertia in the block.

### **Sun gear inertia** — Sun gear inertia `0.001` `kg*m^2` (default) | positive scalar

Sun gear inertia.

#### Dependencies

To enable this parameter, select
**Inertia**.

### **Sun gear radius** — Sun gear radius `0.01` `m` (default) | positive scalar

Sun gear radius.

#### Dependencies

To enable this parameter, select
**Inertia**.

### **Carrier inertia** — Carrier inertia `0.001` `kg*m^2` (default) | positive scalar

Moment of inertia of the planet gear carrier.

#### Dependencies

To enable this parameter, select
**Inertia**.

### **Planet gear spin inertia** — Planet gear spin inertia `0.001` `kg*m^2` (default) | positive scalar

Planetary gear inertia about its own axis.

#### Dependencies

To enable this parameter, select
**Inertia**.

### **Planet gear mass** — Planet gear mass `0.001` `kg*m^2` (default) | positive scalar

Planet gear mass.

#### Dependencies

To enable this parameter, select
**Inertia**.

### Clutch

### **Number of friction surfaces** — Number of contact surfaces `4` (default) | positive scalar

Number, *N*, of friction-generating contact surfaces
inside the clutch.

### **Effective torque radius** — Friction force application radius `130` `mm` (default) | positive scalar

Effective moment arm radius,
*reff*, that determines the
kinetic friction torque inside the clutch.

### **Preload force** — Clutch plate engagement pressure `300` `N` (default) | nonegative scalar

Force that the spring preload exerts on the clutch plate assemblies.
Must be greater than or equal to zero.

### **Static friction coefficient** — Static friction coefficient `0.35` (default) | positive scalar

Static or peak value of the friction coefficient. The static friction
coefficient must be greater than the kinetic friction
coefficient.

#### Dependencies

To enable this parameter, set **Friction model**
to `No meshing losses - Suitable for HIL
simulation` or `Fixed kinetic friction
coefficient`.

### **Static friction coefficient vector** — Static friction coefficient `[.4, .38, .36]` (default) | vector

Vector of static or peak values of the friction coefficient for a
given temperature. The vector must be the same length as the
**Temperature**. Each element must be greater than
the maximum value of the corresponding row in the **Kinetic
friction coefficient matrix**.

#### Dependencies

To enable this parameter, set **Friction model**
to `Temperature-dependent
efficiency`.

### **Kinetic friction coefficient relative velocity vector** — Absolute surface velocity `[0, 100, 1000]` `rad/s` (default) | vector

Vector of input values for the relative velocity. The values in the
vector must increase from left to right. The minimum number of values
depends on the interpolation method that you select. For linear
interpolation, provide at least two values per dimension. For smooth
interpolation, provide at least three values per dimension.

### **Kinetic friction coefficient vector** — Coulomb coefficient of friction, *k*K `[.3, .22, .19]` (default) | vector

Vector of output values for the kinetic friction coefficient. All
values must be greater than zero.

#### Dependencies

To enable this parameter, in the **Differential**
tab, set **Friction model** to `No
meshing losses - Suitable for HIL simulation` or
`Constant efficiency`.

### **Kinetic friction coefficient matrix** — Coulomb coefficient of friction, *k*K `[.34, .32, .3; .3, .28, .25; .25, .2, .15]` (default) | matrix

Matrix of output values for the kinetic friction coefficient. All
values must be greater than zero.

#### Dependencies

To enable this parameter, in the **Differential**
tab, set **Friction model** to
`Temperature-dependent
efficiency`.

### **Friction coefficient interpolation method** — Output value filling method `Linear` (default) | `Smooth`

Interpolation methods for approximating the output value when the
input value is between two consecutive grid points. To optimize
performance, select `Linear`. To produce a
continuous curve with continuous first-order derivatives, select
`Smooth`.

For more information on interpolation algorithms, see PS Lookup Table
(1D).

### **Friction coefficient extrapolation method** — Output value extending method `Linear` (default) | `Nearest`

Extrapolation methods for approximating the output value when the
input value is outside the range specified in the argument list. To
produce a curve with continuous first-order derivatives in the
extrapolation region and at the boundary with the interpolation region,
select `Linear`. To produce an extrapolation
that does not go above the highest point in the data or below the lowest
point in the data, select `Nearest`.

For more information on interpolation algorithms, see PS Lookup Table
(1D).

### **Velocity tolerance** — Slip velocity locking boundary `0.001` `rad/s` (default)

Maximum slip velocity at which the clutch can lock. The slip velocity
is the signed difference between the base and follower shaft angular
velocities, w=wF−wB. When the kinetic friction torque is nonzero and the
transferred torque is within the static friction torque limits, the
clutch locks if the actual slip velocity falls below the velocity
tolerance.

### **Initial state** — Initial clutch state `Unlocked` (default) | `Locked`

Clutch state at the start of simulation. The clutch can be in one of
two states, locked and unlocked. A locked clutch constrains the base and
follower shafts to spin at the same velocity, that is, as a single unit.
An unlocked clutch allows the two shafts to spin at different
velocities, resulting in slip between the clutch plates.

### Thermal Port

To enable these settings, set **Friction model** to
`Temperature-dependent efficiency`.

### **Thermal mass** — Thermal mass `50` `J/K` (default) | scalar

Thermal energy required to change the component temperature by a
single temperature unit. The greater the thermal mass, the more
resistant the component is to temperature change.

#### Dependencies

To enable this parameter, set**Friction model**
to `Temperature-dependent
efficiency`.

### **Initial temperature** — Initial temperature `300` `K` (default) | scalar

Block temperature at the start of simulation. The initial temperature sets the initial
component efficiencies according to their respective efficiency vectors.

#### Dependencies

To enable this parameter, set **Friction model** to
`Temperature-dependent efficiency`.

## Libraries

Simscape / Driveline / Gears

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

### R2025a: Enumeration Updates

The **Inertia** parameter now uses a check box. This parameter
used a drop down in previous releases.

### R2024b: Inertia updates

You now can specify the inertia of all gear subcomponents including the sun, ring,
and carrier gears. You also now can include the effects of planet procession in the
planet inertia behavior.

## Description

Reduce velocity difference between two connected shafts

The Limited-Slip Differential block represents a
limited-slip differential (LSD), which is a gear assembly that limits the velocity
difference between two connected shafts. The block models the LSD mechanism as a
structural component that combines a differential and a clutch.

The differential component in the LSD block is an open differential. An *open
differential* is a gear mechanism that allows two driven shafts to spin at
different speeds. In an automobile, a differential allows the inner wheels to spin more
slowly than the outer wheels when the vehicle is cornering. A vehicle that has wheel
shafts connected by an open differential can get stuck when one of the wheels slips and
spins freely due to traction loss. This vehicle stops moving because the driveshaft
supplies less power to the wheel with traction than it supplies to the spinning
wheel.

In the same scenario, a vehicle that has an LSD is less likely to get stuck because it
contains a clutch assembly that can transmit power to the wheel that retains traction.
The clutch component in the LSD block is a friction clutch that has two sets of flat
friction plates. The clutch engages when applied pressure exceeds the engagement
threshold pressure. In an LSD, a spring preload that separates the sun gears presses the
plates in both sets together. When the shafts experience a traction differential, the
planet pinion gears exert an additional force in the direction of the high-traction
shaft. If the additional pressure exceeds the engagement threshold, the clutch assembly
engages. The engagement allows the driveshaft to transmit more power to the
slower-spinning high-traction wheel. The additional power reduces the difference in
velocity of the two shafts. Because the high-traction wheel continues to rotate, the
vehicle continues to move.

The figure shows the orientation of the major components in an LSD mechanism. The
driveshaft pinion gear is not visible is this representation.

The Limited-Slip Differential block models the LSD
mechanism as a structural component based on the Simscape™
Driveline™
Differential and Disc Friction Clutch blocks. The differential mechanism modeled by
the Differential block is a structural
component based on two other Simscape
Driveline blocks, the Simple Gear and the Sun-Planet Bevel. The block diagram shows the structural components
of the LSD.

The ports of the Limited-Slip Differential block are
associated with the driveshaft (port **D**) and the two driven shafts
(ports **S1** and **S2**), which connect the sun gears
to the wheels.

The Limited-Slip Differential block enables you to
specify inertias only for the gear carrier and internal planet gears. By default, the
inertias of the outer gears are assumed negligible. To model the inertias of the outer
gears, connect Simscape
Inertia blocks to the
**D**, **S1**, and **S2** ports.

The table shows the rotation direction of the driven shaft ports for different block
parameterizations and input conditions.

| Rotation Direction of the Driven Shaft Ports (S1 and S2) | Crown Gear Location Relative to the Centerline | Rotation Direction of Driveshaft Port D | Relative Slippage Across the Differential |
| --- | --- | --- | --- |
| Positive | Right | Positive | 0 |
| - Positive for the nonslipping port - Negative the slipping port | Right | Positive | > 0 |
| Negative | Right | Negative | 0 |
| - Negative for the nonslipping port - Positive the slipping port | Right | Negative | > 0 |
| Negative | Left | Positive | 0 |
| - Negative for the nonslipping port - Positive the slipping port | Left | Positive | > 0 |
| Positive | Left | Negative | 0 |
| - Positive for the nonslipping port - Negative the slipping port | Left | Negative | > 0 |

### Model

To examine the mathematical models for the structural components of the
Limited-Slip Differential block, see:

- Disc Friction
  Clutch
- Differential
- Simple Gear
- Sun-Planet Bevel

### Thermal Model

You can model
the effects of heat flow and temperature change by enabling the optional thermal port. To enable
the port, set **Friction model** to `Temperature-dependent
efficiency`.
