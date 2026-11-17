---
type: simulink-block
title: 'Double-Pinion Planetary Gear'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears'
documentation_page: 'doublepinionplanetarygear'
documentation_source_path: 'ref/doublepinionplanetarygear.html'
language: en
---

# Double-Pinion Planetary Gear

## Ports
```yaml
ports:
- name: C
  summary: Planet gear carrier rotational mechanical
  direction: conserving
- name: R
  summary: Ring gear rotational mechanical
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
```yaml
parameters:
- name: Ring (R) to sun (S) teeth ratio (NR/NS)
  summary: Ring to sun gear rotation ratio 2 (default) | positive scalar
  group: Main
- name: Outer planet (Po) to inner planet (Pi) teeth ratio (NPo/NPi)
  summary: Outer planet to inner planet gear rotation ratio 1 (default) | positive scalar
  group: Main
- name: Friction model
  summary: Friction model No meshing losses - Suitable for HIL simulation (default) | Constant efficiency | Temperature-dependent
    efficiency
  group: Meshing Losses
- name: Sun-planet, ring-planet and planet-planet ordinary efficiencies
  summary: Torque transfer efficiencies for the [.98, .98, .99] (default) | vector
  group: Meshing Losses
- name: Temperature
  summary: Temperature [280, 300, 320] K (default) | vector
  group: Meshing Losses
- name: Sun-planet efficiency
  summary: Torque transfer efficiency from the sun gear to the inner planet gears [.75, .65, .6] (default) | vector
  group: Meshing Losses
- name: Ring-planet efficiency
  summary: Torque transfer efficiency from the ring gear to the outer planet gears [.5, .45, .4] (default) | vector
  group: Meshing Losses
- name: Planet-planet efficiency
  summary: Torque transfer efficiency from the inner planet gears to the outer planet gears [.5, .45, .4] (default) | vector
  group: Meshing Losses
- name: Sun-carrier, ring-carrier, and planet-carrier power thresholds
  summary: Minimum efficiency power threshold for the sun-carrier, ring-carrier, and planet-carrier gear couplings [.001,
    .001, .001] W (default) | vector
  group: Meshing Losses
- name: Sun-carrier, ring-carrier, and planet-carrier viscous friction coefficients
  summary: Gear viscous friction [0, 0, 0] N*m/(rad/s) (default) | vector
  group: Viscous Losses
- name: Inertia
  summary: Inertia option off (default) | on
  group: Inertia
- name: Sun gear inertia
  summary: Sun gear inertia 0.001 kg*m^2 (default) | positive scalar
  group: Inertia
- name: Sun gear radius
  summary: Sun gear radius 0.01 m (default) | positive scalar
  group: Inertia
- name: Ring gear inertia
  summary: Ring gear inertia 0.001 kg*m^2 (default) | positive scalar
  group: Inertia
- name: Carrier gear inertia
  summary: Carrier gear inertia 0.001 kg*m^2 (default) | positive scalar
  group: Inertia
- name: Inner planet gear spin inertia
  summary: Inner planet gear spin inertia 0.001 kg*m^2 (default) | positive scalar
  group: Inertia
- name: Inner planet gear mass
  summary: Inner planet gear mass 0.001 kg (default) | positive scalar
  group: Inertia
- name: Inner planet gear radius
  summary: Inner planet gear radius 0.01 m (default) | positive scalar
  group: Inertia
- name: Outer planet gear spin inertia
  summary: Outer planet gear spin inertia 0.001 kg*m^2 (default) | positive scalar
  group: Inertia
- name: Outer planet gear mass
  summary: Inner planet gear mass 0.001 kg (default) | positive scalar
  group: Inertia
- name: Outer planet gear radius
  summary: Inner planet gear radius 0.02 m (default) | positive scalar
  group: Inertia
- name: Thermal mass
  summary: Thermal mass 50 J/K (default) | scalar
  group: Thermal Port
- name: Initial temperature
  summary: Initial temperature 300 K (default) | scalar
  group: Thermal Port
```

### Main

### **Ring (R) to sun (S) teeth ratio (NR/NS)** — Ring to sun gear rotation ratio `2` (default) | positive scalar

Fixed ratio of the ring gear to the sun gear rotations as defined by
the number of planet gear teeth divided by the number of sun gear
teeth.

### **Outer planet (Po) to inner planet (Pi) teeth ratio (NPo/NPi)** — Outer planet to inner planet gear rotation ratio `1` (default) | positive scalar

Fixed ratio of the outer planet gear to the inner planet gear
rotations as defined by the number of planet gear teeth divided by the
number of sun gear teeth.

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

### **Sun-planet, ring-planet and planet-planet ordinary efficiencies** — Torque transfer efficiencies for the `[.98, .98, .99]` (default) | vector

Vector of torque transfer efficiencies,
[*ηSP*,
*ηRP*,
*ηRPP*], for sun-planet,
and ring-planet, and planet-planet gear wheel pair meshings,
respectively. The vector elements must be in the interval (0,1].

#### Dependencies

To enable this parameter, set **Friction model**
to `Constant efficiency`.

### **Temperature** — Temperature `[280, 300, 320]` `K` (default) | vector

Vector of temperatures used to construct a 1-D temperature-efficiency lookup table.
The vector elements must increase from left to right.

#### Dependencies

To enable this parameter, set **Friction model** to
`Temperature-dependent efficiency`.

### **Sun-planet efficiency** — Torque transfer efficiency from the sun gear to the inner planet gears `[.75, .65, .6]` (default) | vector

Vector of output-to-input power ratios that describe the power flow
from the sun gear to the inner planet gears,
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

### **Ring-planet efficiency** — Torque transfer efficiency from the ring gear to the outer planet gears `[.5, .45, .4]` (default) | vector

Vector of output-to-input power ratios that describe the power flow
from the ring gear to the outer planet gears,
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

### **Planet-planet efficiency** — Torque transfer efficiency from the inner planet gears to the outer planet gears `[.5, .45, .4]` (default) | vector

Vector of output-to-input power ratios that describe the power flow
from the inner planet gear to the outer planet gear,
*ηPP*. The block uses
the values to construct a 1-D temperature-efficiency lookup
table.

Each element
is an efficiency that relates to a temperature in the **Temperature** vector.
The length of the vector must be equal to the length of the **Temperature**
vector. Each element in the vector must be in the range (0,1].

#### Dependencies

To enable this parameter, set **Friction model**
to `Temperature-dependent
efficiency`.

### **Sun-carrier, ring-carrier, and planet-carrier power thresholds** — Minimum efficiency power threshold for the sun-carrier, ring-carrier, and planet-carrier gear couplings `[.001, .001, .001]` `W` (default) | vector

Vector of power thresholds above which the full efficiency factors
apply. Enter the thresholds in the order sun-carrier, ring-carrier,
planet-carrier.

When you set **Friction model** to
`Constant efficiency`, the block lowers the
efficiency losses to zero when no power is transmitted. When you set
**Friction model** to
`Temperature-dependent efficiency`, the
block smooths the efficiency factors between zero when at rest and the
values provided by the temperature-efficiency lookup tables at the power
thresholds.

The power threshold should be lower than the expected power
transmitted during simulation. Higher values may cause the block to
underestimate efficiency losses. Very low values may raise the
computational cost.

#### Dependencies

To enable the parameter, set **Friction model**
to `Constant efficiency` or
`Temperature-dependent
efficiency`.

### Viscous Losses

### **Sun-carrier, ring-carrier, and planet-carrier viscous friction coefficients** — Gear viscous friction `[0, 0, 0]` `N*m/(rad/s)` (default) | vector

Vector of viscous friction coefficients,
[*μS*
*μR*
*μP*], for the sun-carrier,
ring-carrier, and planet-carrier gear motions, respectively.

### Inertia

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

### **Inner planet gear spin inertia** — Inner planet gear spin inertia `0.001` `kg*m^2` (default) | positive scalar

Inertia of the inner planet gear about its own axis.

#### Dependencies

To enable this parameter, select
**Inertia**.

### **Inner planet gear mass** — Inner planet gear mass `0.001` `kg` (default) | positive scalar

Mass of the inner planet gear.

#### Dependencies

To enable this parameter, select
**Inertia**.

### **Inner planet gear radius** — Inner planet gear radius `0.01` `m` (default) | positive scalar

Radius of the inner planet gear.

#### Dependencies

To enable this parameter, select
**Inertia**.

### **Outer planet gear spin inertia** — Outer planet gear spin inertia `0.001` `kg*m^2` (default) | positive scalar

Outer planet gear inertia about its own axis.

#### Dependencies

To enable this parameter, select
**Inertia**.

### **Outer planet gear mass** — Inner planet gear mass `0.001` `kg` (default) | positive scalar

Mass of the outer planet gear.

#### Dependencies

To enable this parameter, select
**Inertia**.

### **Outer planet gear radius** — Inner planet gear radius `0.02` `m` (default) | positive scalar

Radius of the outer planet gear.

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

**Introduced in R2013b**

### R2025a: Enumeration Updates

The **Inertia** parameter now uses a check box. This parameter
used a drop down in previous releases.

### R2024b: Inertia updates

You now can specify the inertia of all gear subcomponents including the sun, ring,
and carrier gears. You also now can include the effects of planet procession in the
planet inertia behavior.

## Description

Planetary gear train with two meshed planet gear sets

The Double-Pinion Planetary Gear block represents a planetary gear train with two
meshed planet gear sets between the sun gear and the ring gear. A single carrier holds
the two planet gear sets at different radii from the sun gear centerline, while allowing
the individual gears to rotate with respect to each other. The gear model includes power
losses due to friction between meshing gear teeth and viscous damping of the spinning
gear shafts.

Structurally, the double-pinion planetary gear resembles a Ravigneaux gear without its
second, large, sun gear. The inner planet gears mesh with the sun gear and the outer
planet gears mesh with the ring gear. Because it contains two planet gear sets, the
double-pinion planetary gear reverses the relative rotation directions of the ring and
sun gears.

The teeth ratio of a meshed gear pair fixes the relative angular velocities of the two
gears in that pair. In the Double-Pinion Planetary Gear
block, you can specify the gear teeth ratios between the ring and sun gears and the
outer planet and inner planet gears. A geometric constraint fixes the remaining teeth
ratios—the ring gear to the outer planet gear and the inner planet gear to the sun gear.
This constrains the ring gear radius to the sum of the sun gear radius and the inner and
outer planet gear diameters.

rr=rs+2⋅rpi+2⋅rpo,

where:

- *rr* is the ring gear
  radius.
- *rs* is the sun gear
  radius.
- *rpi* is the inner planet gear
  radius.
- *rpo* is the outer planet gear
  radius.

The ring to outer planet gear teeth ratio is

rrrpo=2⋅rrrs(rrrs−1)⋅(rporpi+1)rporpi.

The inner planet-sun teeth ratio is

rpirs=(rrrs−1)2(rporpi+1).

The Double-Pinion Planetary Gear block is a composite
component. It contains three underlying blocks—Ring-Planet, Planet-Planet, and Sun-Planet—connected as shown in the figure. Each block connects to a
separate drive shaft through a rotational conserving port.

### Thermal Model

You can model
the effects of heat flow and temperature change by enabling the optional thermal port. To enable
the port, set **Friction model** to `Temperature-dependent
efficiency`.

### Assumptions and Limitations

- Gear inertia is assumed to be negligible.
- Gears are treated as rigid components.
- Coulomb friction slows down simulation. For more information, see Adjust Model Fidelity.
