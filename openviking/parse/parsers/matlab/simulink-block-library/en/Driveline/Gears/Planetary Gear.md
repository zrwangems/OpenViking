---
type: simulink-block
title: 'Planetary Gear'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears'
documentation_page: 'planetarygear'
documentation_source_path: 'ref/planetarygear.html'
language: en
---

# Planetary Gear

## Ports

### Conserving

### **C** — Planet gear carrier rotational mechanical

Rotational mechanical conserving port associated with the planet gear
carrier.

### **R** — Ring gear rotational mechanical

Rotational mechanical conserving port associated with the ring
gear.

### **S** — Sun gear rotational mechanical

Rotational mechanical conserving port associated with the sun
gear.

### **H** — Heat flow thermal

Thermal conserving port associated with heat flow. Heat flow affects the power
transmission efficiency by altering the gear temperatures.

#### Dependencies

To enable this port, set **Friction model** to
`Temperature-dependent efficiency`.

## Parameters

### Main

### **Ring (R) to sun (S) teeth ratio (NR/NS)** — Ring gear to sun gear rotation ratio `2` (default) | scalar integer

Fixed ratio, *gRS*, of the
ring gear to the sun gear rotations as defined by the number of ring
gear teeth divided by the number of sun gear teeth. The gear ratio must
be strictly greater than `1`.

### Meshing Losses

### **Friction model** — Friction model `No meshing losses - Suitable for HIL simulation` (default) | `Constant efficiency` | `Temperature-dependent efficiency`

Friction model for the block:

- `No meshing losses - Suitable for HIL simulation`
  — Gear meshing is ideal.
- `Constant efficiency` — Transfer of torque
  between the gear wheel pairs is reduced by a constant efficiency,
  *η*, such that 0 < *η* ≤ 1.
- `Temperature-dependent efficiency` — Transfer of
  torque between the gear wheel pairs is defined by the table lookup based on
  the temperature.

### **Sun-planet and ring-planet ordinary efficiencies** — Torque transfer efficiencies from the sun gear to the planet gear and from the ring gear to the planet gear `[.96, .98]` (default) | vector

Vector of torque transfer efficiencies,
[*ηSP*
*ηRP*], for sun-planet and
ring-carrier gear wheel pair meshings, respectively.

#### Dependencies

To enable this parameter, set **Friction model**
to `Constant efficiency`.

### **Temperature** — Temperature `[280, 300, 320]` `K` (default) | vector

Vector of temperatures used to construct a 1-D temperature-efficiency lookup table.
The vector elements must increase from left to right.

#### Dependencies

To enable this parameter, set **Friction model** to
`Temperature-dependent efficiency`.

### **Wave generator flexspline efficiency** — Wave generator to flexspline torque transfer efficiency `[.95, .9, .85]` (default) | vector

Vector of output-to-input power ratios that describe the power flow
from the wave generator gear to the flexspline gear,
*ηSP*. The block uses
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

### **Ring-flexspline efficiency** — Torque transfer efficiency from the ring gear to the flexspline gear `[.95, .9, .85]` (default) | vector

Vector of output-to-input power ratios that describe the power flow
from the ring gear to the flexspline gear,
*ηRP*. The block uses
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

### **Sun-carrier and planet-carrier power thresholds** — Minimum efficiency power threshold for the sun-carrier and planet-carrier gear couplings `[.001, .001]` `W` (default) | vector

Vector of power thresholds above which full efficiency factors apply.
Enter the thresholds in the order sun-carrier, planet-carrier. Below
these values, a hyperbolic tangent function smooths the efficiency
factor.

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

### Viscous Losses

### **Sun-carrier and planet-carrier viscous friction coefficients** — Gear viscous friction `[0, 0]` `N*m/(rad/s)` (default) | vector

Vector of viscous friction coefficients,
[*μS*,
*μP*], for the
sun-carrier and planet-carrier gear motions, respectively.

### Inertia

### **Inertia** — Inertia option `off` (default) | `on`

Whether to include the effects of inertia in the block.

### **Sun gear inertia** — Sun gear inertia `0.001` `kg*m^2` (default) | positive scalar

Sun gear inertia.

#### Dependencies

To enable this parameter, select
**Inertia**.

### **Ring gear inertia** — Ring gear inertia `0.001` `kg*m^2` (default) | positive scalar

Ring gear inertia.

#### Dependencies

To enable this parameter, select
**Inertia**.

### **Carrier gear inertia** — Carrier gear inertia `0.001` `kg*m^2` (default) | positive scalar

Carrier gear inertia.

#### Dependencies

To enable this parameter, select
**Inertia**.

### **Carrier gear radius** — Carrier gear radius `0.01` `m` (default) | positive scalar

Carrier gear radius.

#### Dependencies

To enable this parameter, select
**Inertia**.

### **Planet gear spin inertia** — Planet gear spin inertia `0.001` `kg*m^2` (default) | positive scalar

Planetary gear inertia about its own axis.

#### Dependencies

To enable this parameter, select
**Inertia**.

### **Planet gear mass** — Planet gear mass `0.001` `kg` (default) | positive scalar

Planet gear mass.

#### Dependencies

To enable this parameter, select
**Inertia**.

### Thermal Port

To enable these settings, set **Friction model** to
`Temperature-dependent efficiency`.

### **Thermal mass** — Thermal mass `50` `J/K` (default) | scalar

Thermal energy required to change the component temperature by a single temperature unit. The
greater the thermal mass, the more resistant the component is to temperature
change.

#### Dependencies

To enable this parameter, set **Friction model** to
`Temperature-dependent
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

**Introduced in R2011a**

### R2025a: Enumeration Updates

The **Inertia** parameter now uses a check box. This parameter
used a drop down in previous releases.

### R2024b: Inertia updates

You now can specify the inertia of all gear subcomponents including the sun, ring,
and carrier gears. You also now can include the effects of planet procession in the
planet inertia behavior.

## Description

Gear train with sun, planet, and ring gears

The Planetary Gear block models a gear train with sun, planet, and ring gears.
Planetary gears are common in transmission systems, where they provide high gear ratios
in compact geometries. A carrier connected to a drive shaft holds the planet gears.
Ports **C**, **R**, and **S**
represent the shafts connected to the planet gear carrier, ring gear, and sun gear.

The block models the planetary gear as a structural component based on Sun-Planet and Ring-Planet
Simscape™
Driveline™ blocks. The figure shows the block diagram of this structural component.

To increase the fidelity of the gear model, you can specify properties such as gear
inertia, meshing losses, and viscous losses. By default, gear inertia and viscous losses
are assumed to be negligible.

### Thermal Model

You can model
the effects of heat flow and temperature change by enabling the optional thermal port. To enable
the port, set **Friction model** to `Temperature-dependent
efficiency`.

### Equations

**Ideal Gear Constraints and Gear Ratios**

The Planetary Gear block imposes two kinematic
and two geometric constraints,

rCωC=rSωS+rPωP

rRωR=rCωC+rPωP

rC=rS+rP

rR=rC+rP

where:

- *rC* is the radius of the
  carrier gear.
- *ωC* is the angular
  velocity of the carrier gear.
- *rS* is the radius of the
  sun gear.
- *ωS* is the angular
  velocity of the sun gear.
- *rP* is the radius of
  planet gear.
- *ωp* is the angular
  velocity of the planet gears.
- *rR* is the radius of the
  ring gear.

The ring-sun gear ratio is

gRS=rR/rS=NR/NS,

where *N* is the number of teeth on each
gear.

In terms of this ratio, the key kinematic constraint is:

(1 + gRS)ωC = ωS + gRSωR.

The four degrees of freedom reduce to two independent degrees of freedom. The
gear pairs are (1, 2) = (*S*, *P*) and
(*P*, *R*).

**Warning**

The gear ratio *g*RS must be
strictly greater than one.

The torque transfer is

gRSτS + τR– τloss= 0,

where:

- *τS* is torque transfer
  for the sun gear.
- *τR* is torque transfer
  for the ring gear.
- *τloss* is torque transfer
  loss.

In the ideal
case where there is no torque loss, *τloss* = 0.

**Nonideal Gear Constraints and Losses**

In the nonideal case, *τloss* ≠ 0. For more information, see Model Gears with Losses.

### Assumptions and Limitations

- Gear inertia is assumed to be negligible.
- Gears are treated as rigid components.
- Coulomb friction slows down simulation. For more information, see Adjust Model Fidelity.
