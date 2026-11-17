---
type: simulink-block
title: 'Ring-Planet'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears / Planetary Subcomponents'
documentation_page: 'ringplanet'
documentation_source_path: 'ref/ringplanet.html'
language: en
---

# Ring-Planet

## Ports
```yaml
ports:
- name: C
  summary: Planet gear carrier rotational mechanical
  direction: conserving
- name: R
  summary: Ring gear rotational mechanical
  direction: conserving
- name: P
  summary: Planet gear rotational mechanical
  direction: conserving
- name: H
  summary: Heat flow thermal
  direction: conserving
```

### Conserving

### **C** — Planet gear carrier rotational mechanical

Rotational mechanical conserving port associated with the planet gear
carrier.

### **R** — Ring gear rotational mechanical

Rotational mechanical conserving port associated with the ring
gear.

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
```yaml
parameters:
- name: Ring (R) to planet (P) teeth ratio (NR/NP)
  summary: Ring to planet gear rotation ratio 2 (default) | scalar greater than 1
  group: Main
- name: Friction model
  summary: Friction model No meshing losses - Suitable for HIL simulation (default) | Constant efficiency | Temperature-dependent
    efficiency
  group: Meshing Losses
- name: Ordinary efficiency
  summary: Torque transfer efficiency 0.98 (default) | scalar
  group: Meshing Losses
- name: Temperature
  summary: Temperature [280, 300, 320] K (default) | vector
  group: Meshing Losses
- name: Efficiency
  summary: Gear efficiency [.95, .9, .85] (default) | vector
  group: Meshing Losses
- name: Planet-carrier power threshold
  summary: Minimum efficiency power threshold for the planet-carrier gear coupling 0.001 W (default) | scalar
  group: Meshing Losses
- name: Planet-carrier viscous friction coefficient
  summary: Gear viscous friction 0 N*m/(rad/s) (default) | scalar
  group: Viscous Losses
- name: Thermal mass
  summary: Thermal mass 50 J/K (default) | scalar
  group: Thermal Port
```

### Main

### **Ring (R) to planet (P) teeth ratio (NR/NP)** — Ring to planet gear rotation ratio `2` (default) | scalar greater than 1

Ratio, *gRP*, of the ring gear
to planet gear rotations as defined by the number of ring gear teeth
divided by the number of planet gear teeth. This gear ratio must be
strictly greater than 1.

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

### **Ordinary efficiency** — Torque transfer efficiency `0.98` (default) | scalar

Torque transfer efficiency,
*ηRP*, for the outer and
inner planet gear wheel pair meshing. This value must be in the range
(0,1].

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
from the ring gear to the planet gear,
*ηRP*. The block uses
the values to construct a 1-D temperature-efficiency lookup
table.

Each element is an efficiency that relates to a temperature in the
**Temperature** vector. The length of the vector
must be equal to the length of the **Temperature**
vector. Each element in the vector must be in the range (0,1].

#### Dependencies

To enable this parameter, set **Friction model**
to `Temperature-dependent
efficiency`.

### **Planet-carrier power threshold** — Minimum efficiency power threshold for the planet-carrier gear coupling `0.001` `W` (default) | scalar

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

### **Planet-carrier viscous friction coefficient** — Gear viscous friction `0` `N*m/(rad/s)` (default) | scalar

Viscous friction coefficient,
*μP*, for the planet-carrier
gear motion.

### Thermal Port

To enable this parameter, set **Friction model** to
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

Planetary gear set of carrier, planet, and ring wheels with adjustable gear ratio and friction losses

The Ring-Planet block represents a carrier, a ring
gear, and a set of planet gears. The planet gears are connected to and rotate with
respect to the carrier. The planet and ring gears corotate with a fixed gear ratio that
you specify. A ring-planet and a sun-planet gear are basic elements of a planetary gear
set. For model details, see Equations.

### Thermal Model

You can model
the effects of heat flow and temperature change by enabling the optional thermal port. To enable
the port, set **Friction model** to `Temperature-dependent
efficiency`.

### Equations

**Ideal Gear Constraints and Gear Ratios**

The Ring-Planet block imposes one kinematic and
one geometric constraint on the three connected axes:

rRωR=rCωC+rPωP

rR=rC+rP

The ring-planet gear ratio is

gRP=rR/rP=NR/NP,

where *N* is the number of teeth on each
gear. In terms of this ratio, the key kinematic constraint is

gRPωR=ωP+ (gRP– 1)ωC.

The three degrees of freedom reduce to two independent degrees of freedom. The
gear pair is (1, 2) = (*P*, *R*).

**Warning**

The ring-planet gear ratio *gRP*
must be strictly greater than one.

The torque transfer is:

gRPτP+τR–τloss= 0.

In the ideal
case where there is no torque loss, *τloss* = 0.

**Nonideal Gear Constraints and Losses**

In the nonideal case, *τloss* ≠ 0. For more information, see Model Gears with Losses.

### Variables

Use the **Variables** settings to set the priority and initial target
values for the block variables before simulating. For more information, see Set Priority and Initial Target for Block Variables.

### Assumptions and Limitations

- Gear inertia is assumed to be negligible.
- Gears are treated as rigid components.
- Coulomb friction slows down simulation. For more information, see Adjust Model Fidelity.
