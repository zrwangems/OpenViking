---
type: simulink-block
title: 'Sun-Planet Bevel'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears / Planetary Subcomponents'
documentation_page: 'sunplanetbevel'
documentation_source_path: 'ref/sunplanetbevel.html'
language: en
---

# Sun-Planet Bevel

## Ports

### Conserving

### **C** — Planet gear carrier rotational mechanical

Rotational mechanical conserving port associated with the planet gear
carrier.

### **P** — Planet gear rotational mechanical

Rotational mechanical conserving port associated with the planet
gear.

### **H** — Heat flow thermal

Thermal conserving port associated with heat flow. Heat flow affects the power
transmission efficiency by altering the gear temperatures.

#### Dependencies

To enable this port, set **Friction model** to
`Temperature-dependent efficiency`.

## Parameters

### Main

### **Planet (P) to sun (S) teeth ratio (NP/NS)** — Planet to sun gear rotation ratio `2` (default) | scalar

Ratio, *gPS*, of the planet
gear to sun gear rotations as defined by the number of planet gear teeth
divided by the number of sun gear teeth. This gear ratio must be
strictly greater than 1.

### **Assembly orientation** — Gear relative rotational direction `Left - Sun and planet gears rotate in same direction` (default) | `Right - Sun and planet gears rotate in opposite directions`

Relative orientation of the sun and planet gears and their corotation
direction. Left or right orientation implies that the gears corotate in
the same or opposite direction, respectively.

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

### **Ordinary efficiency** — Torque transfer efficiency `0.9` (default) | scalar

Torque transfer efficiency,
*ηPS*, for the planet gear
to the sun gear pair meshing. This value must be greater than
`0` and less than or equal to
`1`.

#### Dependencies

To enable this parameter, set **Friction model**
to `Constant efficiency`.

### **Temperature** — Temperature `[280, 300, 320]` `K` (default) | vector

Vector of temperatures used to construct a 1-D temperature-efficiency lookup table.
The vector elements must increase from left to right.

#### Dependencies

To enable this parameter, set **Friction model** to
`Temperature-dependent efficiency`.

### **Efficiency** — Gear efficiency `[.95, .9, .85]` (default) | vector

Vector of output-to-input power ratios that describe the power flow
from the outer planet gear to the inner planet gear,
*ηPS*. The block uses
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

### **Sun-carrier power threshold** — Minimum efficiency power threshold for the sun-carrier gear coupling `0.001` `W` (default) | scalar

Power threshold, *pth*, above
which full efficiency is in effect. Below this value, a hyperbolic
tangent function smooths the efficiency factor.

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

### **Sun-carrier viscous friction coefficient** — Gear viscous friction `0` `N*m/(rad/s)` (default) | scalar

Viscous friction coefficient,
*μS*, for the sun-carrier
gear motion.

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

## Libraries

Simscape / Driveline / Gears / Planetary Subcomponents

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011a**

## Description

Planetary gear set of carrier and beveled planet and sun wheels with adjustable gear ratio, assembly orientation, and friction losses

The Sun-Planet Bevel gear block represents a carrier
and beveled planet and sun wheels. The planet is connected to and rotates with respect
to the carrier. The planet and sun gears corotate with a fixed gear ratio. You control
the direction of rotation by setting the assembly orientation left or right. For model
details, see Equations.

### Thermal Model

You can model
the effects of heat flow and temperature change by enabling the optional thermal port. To enable
the port, set **Friction model** to `Temperature-dependent
efficiency`.

### Equations

**Ideal Gear Constraints and Gear Ratios**

The Sun-Planet Bevel block imposes one
kinematic and one geometric constraint on the three connected axes:

rCωC=rSωS±rPωP

rC=rS±rP

where:

- *rC* is the radius of the
  carrier gear.
- *ωC* is the angular
  velocity of the carrier gear.
- *rS* is the radius of the
  sun gear.
- *ωS* is the angular
  velocity of the sun gear.
- *rP* is the radius of the
  planet gear.
- *ωP* is the angular
  velocity of the planet gear.

The planet-sun gear ratio is defined as

gPS=rPrS=NPNS,

where:

- *gPS* is the planet-sun
  gear ratio. As rP>rS, gPS>1.

- *NP* is the number of
  teeth in the planet gear.
- *NS* is the number of sun
  gear teeth.

In terms of this ratio, the key kinematic constraint is:

- ωS=gPSωP+ωC for a left-oriented bevel assembly
- ωS=−gPSωP+ωC for a right-oriented bevel assembly

The three degrees of freedom reduce to two independent degrees of freedom. The
gear pair is (1,2) = (*S*,*P*).

**Warning**

The planet-sun gear ratio, *gPS*,
must be strictly greater than one.

The torque transfer is defined as

τP=τloss−gPSτS,

where:

- *τloss* is the torque
  loss.
- *τs* is the torque for the
  sun gear.
- *τp* is the torque for the
  planet gear.

In the ideal case where there is no torque loss, *τloss* = 0. The resulting torque transfer equation is τP=gPSτS.

**Nonideal Gear Constraints and Losses**

In the nonideal case, *τloss* ≠ 0. For more information, see Model Gears with Losses.

### Variables

Use the **Variables** settings to set the priority and initial target
values for the block variables before simulating. For more information, see Set Priority and Initial Target for Block Variables.

### Assumptions and Limitations

- Gear inertia is assumed to be negligible.
- Gears are treated as rigid components.
- Coulomb friction slows down simulation. For more information, see Adjust Model Fidelity.
