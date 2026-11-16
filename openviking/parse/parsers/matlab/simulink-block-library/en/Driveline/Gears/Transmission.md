---
type: simulink-block
title: 'Transmission'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears'
documentation_page: 'transmission'
documentation_source_path: 'ref/transmission.html'
language: en
---

# Transmission

## Ports

### Input

### **G** — Gear selection physical signal

Physical input signal associated with the gear selection. An input of where
`0` represents neutral, `-1`
represents reverse, and the values in the **Forward gear
ratios** parameter represent the forward gears. The block
saturates the signal from `-1` to the length of the
**Forward gear ratios** parameter.
### Conserving

### **B** — Base interface mechanical rotational

Mechanical rotational conserving port associated with the base
interface.

### **F** — Follower interface mechanical rotational

Mechanical rotational conserving port associated with the follower
interface.

### **H** — Heat flow thermal

Thermal conserving port associated with heat flow.

#### Dependencies

To enable this port, set **Thermal port** to
`Model`.

## Parameters

### Gears

### **Forward gear ratios** — Transmission forward gear ratios `[2.3, 1.6, 1.2, 1, .8, .6]` (default) | vector of positive numbers

Ordered vector of transmission gear ratios. The block uses the position of each element
in the vector to assign that element to a given input signal. You can
parameterize an arbitrary number of gear ratios.

### **Reverse gear ratio** — Transmission reverse gear ratio `-3` (default) | negative scalar

Gear ratio of the reverse gear.

#### Dependencies

To enable this parameter, set **Friction model**
to `Gear-dependent efficiency`.

### **Friction model** — Friction model `No meshing losses - Suitable for HIL simulation` (default) | `Constant efficiency` | `Gear-dependent efficiency`

Friction model for the block:

- `No meshing losses - Suitable for HIL
  simulation` — Gear meshing is ideal.
- `Constant efficiency` — The block
  reduces torque transfer between all of the gear wheel pairs
  according to the **Efficiency**
  parameter.
- `Gear-dependent efficiency` — The
  block defines torque transfer between the gear wheel pairs
  according to the **Efficiency vector**
  parameter.

### **Efficiency** — Gear efficiency `0.95` (default) | positive scalar

Efficiency that the block applies to all gear ratios.

#### Dependencies

To enable this parameter, set **Friction model**
to `Constant efficiency`.

### **Efficiency vector** — Forward gear-dependent efficiencies `[.95, .95, .95, .95, .95, .95]` (default) | vector of positive elements

Gear-dependent efficiency where each element corresponds to a gear
ratio in the **Forward gear ratios** parameter.

#### Dependencies

To enable this parameter, set **Friction model**
to `Gear-dependent efficiency`.

### **Reverse efficiency** — Reverse gear efficiency `0.90` (default) | positive scalar

Efficiency that the block applies to the reverse gear.

### **Follower power threshold** — Point at which block applies full efficiency loss `0.001` `W` (default) | positive scalar

Absolute power at which the block applies the full efficiency to the follower.

#### Dependencies

To enable this parameter, set **Friction model**
to `Constant efficiency` or
`Gear-dependent efficiency`.

### **Stiffness at base (B)** — Base spring rate coefficient `3e5` `N*m/rad` (default) | positive scalar

Reciprocal of the transmission angular compliance measured at the
base.

### **Damping at base (B)** — Base damping coefficient `3e4` `N*m*s/rad` (default) | positive scalar

Reciprocal of the transmission angular compliance damping measured at
the base.

### **Initial input torque at base (B)** — Starting torque at base `0` `N*m` (default) | scalar

Torque applied at the base shaft at the start of simulation.

### **Viscous friction coefficients at base (B) and follower (F)** — Base and follower viscous friction vector `[0, 0]` `N*m/(rad/s)` (default) | vector of nonnegative elements

Vector of viscous damping coefficients applied at the base and
follower shafts, respectively.

### Clutch

### **Kinetic friction torque** — Kinetic friction torque threshold `1000` `N*m` (default) | nonnegative scalar

Minimum torque threshold to maintain relative motion between the
clutch plates.

### **Static friction torque** — Static friction torque threshold `2000` `N*m` (default) | positive scalar

Minimum torque threshold to cause relative motion between the clutch
plates.

### **Shift model** — Option to include finite shift time `Instantaneous` (default) | `Finite shift time`

Whether the block completes gear shifts instantaneously or transitions
into neutral for a finite amount of time between gears.

### **Shift time** — Time in neutral between gear ratios `100` `ms` (default) | positive scalar

Time to complete a gear shift. The transmission remains in neutral
during this time.

#### Dependencies

To enable this parameter, set **Shift model** to
`Finite shift time`

### **Clutch velocity tolerance** — Motion boundary condition `0.001` `rad/s` (default) | nonnegative scalar

Clutch minimum angular velocity.

### **Initial State** — Clutch state at simulation start `Unlocked` (default) | `Locked`

Option to start the simulation with the clutch unlocked or
locked.

### Thermal Port

### **Thermal port** — Option to expose thermal port `Omit` (default) | `Model`

Whether to expose the thermal port and associated parameters.

### **Thermal mass** — Thermal mass `100` `kJ/K` (default) | positive scalar

Thermal energy required to change the component temperature by a
single temperature unit. The greater the thermal mass, the more
resistant the component is to temperature change.

#### Dependencies

To enable this parameter, set **Thermal port** to
`Model`.

### **Initial temperature** — Temperature at simulation start `300` `K` (default) | positive scalar

Initial transmission temperature when modeling heat flow and
temperature change.

#### Dependencies

To enable this parameter, set **Thermal port** to
`Model`.

## Libraries

Simscape / Driveline / Gears

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Abstract transmission for system-level driveline modeling

The Transmission block represents an abstract transmission
for system-level driveline models. The block accepts the gear ratio command as a
physical signal to port **G**, where `0` represents
neutral, `-1` represents reverse, and the values in the
**Forward gear ratios** parameter represent the forward gears. The
length of this vector corresponds to the number of forward gears. The block rounds the
input values to integers. The transmission is non-sequential, which allows you to
transition between any two gear ratios without having to stop at the intermediate
ratios. For the block to behave like a sequential transmission, you must specify each
gear ratio in the sequence.

The Transmission block is a composite of two blocks.
The block uses a subcomponent implementation of the Variable Ratio
Transmission block to simulate the transmission gear ratio dynamics,
and the block simulates abstracted clutch dynamics using the
Logic-Controlled Clutch block. To learn more, see
About Composite Components.

### Thermal Model

You can model the effects of heat flow and
temperature change by enabling the optional thermal port. To enable the port, set
**Thermal port** to `Model`.
