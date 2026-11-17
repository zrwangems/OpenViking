---
type: simulink-block
title: 'Sun-Planet'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears / Planetary Subcomponents'
documentation_page: 'sunplanet'
documentation_source_path: 'ref/sunplanet.html'
language: en
---

# Sun-Planet

## Ports
```yaml
ports:
- name: C
  summary: Planet gear carrier rotational mechanical
  direction: conserving
- name: P
  summary: Planet gear rotational mechanical
  direction: conserving
- name: S
  summary: Sun gear rotational mechanical
  direction: conserving
- name: H
  summary: Heat flow thermal
  direction: conserving
```

### Conserving

### **C** — Planet gear carrier rotational mechanical

Rotational conserving port associated with the planet gear
carrier.

### **P** — Planet gear rotational mechanical

Rotational conserving port associated with the panet gear.

### **S** — Sun gear rotational mechanical

Rotational conserving port associated with the sun gear.

### **H** — Heat flow thermal

Thermal conserving port associated with heat flow. Heat flow affects the power
transmission efficiency by altering the gear temperatures.

#### Dependencies

To enable this port, set **Friction model** to
`Temperature-dependent efficiency`.
## Parameters
```yaml
parameters:
- name: Planet (P) to sun (S) teeth ratio (NP/NS)
  summary: Planet-to-sun gear ratio 2 (default) | positive scalar
  group: Main
- name: Friction model
  summary: Friction model No meshing losses - Suitable for HIL simulation (default) | Constant efficiency | Temperature-dependent
    efficiency
  group: Meshing Losses
- name: Ordinary efficiency
  summary: Efficiency 0.98 (default) | scalar | 0 < *ηSP* ≤ 1
  group: Meshing Losses
- name: Temperature
  summary: Temperature [280, 300, 320] K (default) | vector
  group: Meshing Losses
- name: Efficiency
  summary: Gear efficiency [.95, .9, .85] (default) | array | 0 < *ηSP* ≤ 1
  group: Meshing Losses
- name: Sun-carrier power threshold
  summary: Power threshold 0.001 W (default) | scalar
  group: Meshing Losses
- name: Sun-carrier viscous friction coefficient
  summary: Viscous friction 0 N*m/(rad/s) (default)
  group: Viscous Losses
- name: Thermal mass
  summary: Thermal mass 50 J/K (default) | scalar
  group: Thermal Port
```

### Main

### **Planet (P) to sun (S) teeth ratio (NP/NS)** — Planet-to-sun gear ratio `2` (default) | positive scalar

Ratio *gPS* of the planet gear
wheel radius to the sun gear wheel radius.

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

### **Ordinary efficiency** — Efficiency `0.98` (default) | scalar | `0` < *ηSP* ≤ `1`

Torque transfer efficiency,
*ηSP*, for sun-planet gear
wheel pair meshings. The value must be greater than `0`
and less than or equal to `1`.

#### Dependencies

This parameter is exposed when the **Friction
model** parameter is set to `Constant
efficiency`.

### **Temperature** — Temperature `[280, 300, 320]` `K` (default) | vector

Vector of temperatures used to construct a 1-D temperature-efficiency lookup table.
The vector elements must increase from left to right.

#### Dependencies

To enable this parameter, set **Friction model** to
`Temperature-dependent efficiency`.

### **Efficiency** — Gear efficiency `[.95, .9, .85]` (default) | array | `0` < *ηSP* ≤ `1`

Array of mechanical efficiencies, ratios of output power to input
power, for the power flow from the ring gear to the planet gear,
*ηRP*. The block uses
the values to construct a 1-D temperature-efficiency lookup
table.

Each element is an efficiency that
relates to a temperature in the **Temperature** vector.
The length of the vector must be equal to the length of the
**Temperature** vector. Each element in the vector
must be in the range (0,1].

#### Dependencies

This parameter is exposed when the **Friction
model** parameter is set to
`Temperature-dependent
efficiency`.

### **Sun-carrier power threshold** — Power threshold `0.001` `W` (default) | scalar

Power threshold, *pth*, above
which full efficiency is in effect. Below this values, a hyperbolic
tangent function smooths the efficiency factor. For a model without
thermal losses, the function lowers the efficiency losses to zero when
no power is transmitted. For a model that considers thermal losses, the
function smooths the efficiency factors between zero at rest and the
values provided by the temperature-efficiency lookup tables at the power
thresholds.

#### Dependencies

This parameter is exposed when the **Friction
model** parameter is set to `Constant
efficiency` or `Temperature-dependent
efficiency`.

### Viscous Losses

### **Sun-carrier viscous friction coefficient** — Viscous friction `0` `N*m/(rad/s)` (default)

Viscous friction coefficient
*μS* for the sun-carrier
gear motion.

### Thermal Port

These settings are visible when, in the **Meshing Losses**
settings, the **Friction model**  parameter is set to
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

Planetary gear set of carrier, planet, and sun wheels with adjustable gear ratio and friction losses

The Sun-Planet gear block represents a set of carrier,
planet, and sun gear wheels. The planet is connected to and rotates with respect to the
carrier. The planet and sun corotate with a fixed gear ratio that you specify and in the
same direction with respect to the carrier. A sun-planet and a ring-planet gear are
basic elements of a planetary gear set. For model details, see Equations.

### Thermal Model

You can model
the effects of heat flow and temperature change by enabling the optional thermal port. To enable
the port, set **Friction model** to `Temperature-dependent
efficiency`.

### Equations

**Ideal Gear Constraints and Gear Ratios**

Sun-Planet imposes one kinematic and one geometric constraint on the three
connected axes:

rCωC=rSωS+rPωP

The planet-sun gear ratio is

gPS=rP/rS=NP/NS

Where *N* is the number of teeth on each
gear. In terms of this ratio, the key kinematic constraint is:

ωS= –gPSωP+ (1 +gPS)ωC

The three degrees of freedom reduce to two independent degrees of freedom. The
gear pair is (1, 2) = (*S*, *P*).

The torque transfer is:

gPSτS+τP–τloss= 0

In the ideal case, there is no torque loss,
that is *τloss* = 0.

**Nonideal Gear Constraints and Losses**

In the nonideal case, *τloss* ≠ 0. For more information, see Model Gears with Losses.

### Variables

Use the **Variables** settings to set the priority and initial target
values for the block variables before simulating. For more information, see Set Priority and Initial Target for Block Variables.
