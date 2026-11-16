---
type: simulink-block
title: 'Single-Acting Actuator (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Actuators'
documentation_page: 'singleactingactuatorg'
documentation_source_path: 'ref/singleactingactuatorg.html'
language: en
---

# Single-Acting Actuator (G)

## Ports

### Input

### **p** — Multibody piston position input, m physical signal

Physical signal input associated with the piston position, in m.
Connect this port to a Simscape
Multibody™ network using a Translational Multibody
Interface block.

#### Dependencies

To enable this port, set **Piston displacement**
to `Provide input signal from Multibody
joint`.
### Output

### **p** — Piston position, m physical signal

Physical signal output associated with the piston position, in
m.

#### Dependencies

To enable this port, set **Piston displacement**
to `Calculate from velocity of port R relative to port
C`.
### Conserving

### **A** — Liquid port gas

Gas conserving port associated with chamber A.

### **C** — Actuator casing translational mechanical

Translational mechanical conserving port associated with the actuator
casing.

### **R** — Actuator piston translational mechanical

Translational mechanical conserving port associated with the actuator
piston.

### **H** — Heat transfer thermal

Thermal conserving port associated with the thermal mass of the gas
volume.

## Parameters

### Actuator

### **Mechanical orientation** — Piston displacement direction `Pressure at A causes positive displacement of R relative to C` (default) | `Pressure at A causes negative displacement of R relative to C`

Piston displacement direction. When you set this parameter to:

- `Pressure at A causes positive displacement of
  R relative to C`, the piston displacement
  is positive when the volume of gas at port
  **A** is expanding. This motion
  corresponds to rod extension.
- `Pressure at A causes negative displacement of
  R relative to C`, the piston displacement
  is negative when the volume of gas at port
  **A** is expanding. This motion
  corresponds to rod contraction.

### **Piston cross-sectional area** — Cross-sectional area of piston rod `0.01` `m^2` (default) | positive scalar

Cross-sectional area of the piston rod.

### **Piston stroke** — Maximum piston travel distance `0.1` `m` (default) | positive scalar

Maximum piston travel distance.

### **Dead volume** — Fluid volume at full piston retraction `1e-5` `m^3` (default) | positive scalar

Volume of gas when the piston displacement is `0`. This parameter is
the gas volume when the piston is against the actuator end cap.

### **Cross-sectional area at port A** — Area at port A `0.01 m^2` (default) | positive scalar

Cross-sectional area of port **A**.

### **Environment pressure specification** — Reference environment pressure `Atmospheric pressure` (default) | `Specified pressure`

Environment reference pressure. When you select
`Atmospheric pressure`, the block assumes a
pressure of 0.101325 MPa.

### **Environment pressure** — User-defined environmental pressure `0.101325` `MPa` (default) | positive scalar

User-defined environmental pressure.

#### Dependencies

To enable this parameter, set **Environment pressure
specification** to `Specified
pressure`.

### Hard Stop

### **Hard stop model** — Hard stop model `Stiffness and damping applied smoothly through transition region, damped rebound` (default) | `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

Hard stop model to use when the piston is at full extension or full
extraction. See the Translational Hard Stop block for more
information.

### **Hard-stop stiffness coefficient** — Stiffness coefficient `1e10` `N/m` (default) | positive scalar

Piston stiffness coefficient.

#### Dependencies

To enable this parameter, set **Hard stop model** to one of these settings:

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **Hard-stop damping coefficient** — Damping coefficient `150` `N*s/m` (default) | positive scalar

Piston damping coefficient.

#### Dependencies

To enable this parameter, set **Hard stop model** to one of these settings:

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **Transition region** — Application range of hard stop force model `0.1` `mm` (default) | positive scalar

Application range of the hard stop force model. The block does not
apply the hard stop model when the maximum extension or retraction of
the piston is outside of this range. In this situation, there is no
additional force on the piston.

#### Dependencies

To enable this parameter, set **Hard stop model**
to `Stiffness and damping applied smoothly through
transition region, damped rebound`.

### **Coefficient of restitution** — Ratio of final-to-initial relative speed between slider and stop after collision `0.7` (default) | unitless value between 0 and 1

Ratio of the final to the initial relative speed between the slider
and the stop after the slider bounces.

#### Dependencies

To enable this parameter, set **Hard stop model**
to `Based on coefficient of
restitution`.

### **Static contact speed threshold** — Threshold relative speed between slider and stop before collision `0.001 m/s` (default) | nonnegative scalar

Threshold relative speed between the slider and stop before collision. When the slider
hits the case with a speed less than the value of the **Static
contact speed threshold** parameter, they stay in contact.
Otherwise, the slider bounces. To avoid modeling static contact between
the slider and the case, set this parameter to
`0`.

#### Dependencies

To enable this parameter, set **Hard stop model**
to `Based on coefficient of
restitution`.

### **Static contact release force threshold** — Force needed to transition from contact mode to free mode `0.001 N` (default) | positive scalar

Minimum force needed to release the slider from a static contact mode.

#### Dependencies

To enable this parameter, set **Hard stop model**
to `Based on coefficient of
restitution`.

### Initial Conditions

### **Piston displacement** — Method for determining piston position `Calculate from velocity of port R relative to port C` (default) | `Provide input signal from Multibody joint`

Method for determining the piston position. The block can receive the
position from a Multibody block when set to `Provide input
signal from Multibody joint`, or can calculate the
position internally and report the position at port
**p**. The position is between `0`
and the value of the **Piston stroke** parameter when
the mechanical orientation is positive and between `0`
and the negative value of the **Piston stroke**
parameter when the mechanical orientation is negative.

### **Initial piston displacement** — Piston position at start of simulation `0` `m` (default) | scalar

Piston position at the start of the simulation.

#### Dependencies

To enable this parameter, set **Piston
displacement** to `Calculate from velocity
of port R relative to port C`.

### **Initial gas pressure** — Starting gas pressure `0.101325` `MPa` (default) | positive scalar

Initial pressure of the gas volume in the actuator.

### **Initial gas temperature** — Starting gas temperature `293.15` `K` (default) | scalar

Initial temperature of the gas volume in the actuator.

## Libraries

Simscape / Fluids / Gas / Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Single-acting linear actuator in a gas network

The Single-Acting Actuator (G) block models a linear actuator with a piston
controlled by a single gas chamber. The actuator generates force in the extension and
retraction strokes, but the actuation force depends on the gauge pressure at a single
chamber.

The figure shows the key components of an actuator. Port **A**
represents the gas chamber inlet. Port **R** represents the
translating actuator piston, and port **C** represents the actuator
case. Port **H** represents the thermal interface between the gas
chamber and the environment.

Single-Acting Actuator Schematic

### Displacement

The block measures the piston displacement as the position at port **R**
relative to port **C**. The **Mechanical
orientation** parameter identifies the direction of piston
displacement. The piston displacement is neutral, or `0`, when the
chamber volume is equal to the value of the **Dead volume**
parameter. When the **Piston displacement** parameter is
`Provide input signal from Multibody joint`, you input
the piston displacement using port **p**. You can ensure that the
derivative of the position signal is equal to the piston velocity by using a Translational Multibody Interface block to
provide the piston displacement.

The direction of the piston motion depends on the **Mechanical
orientation** parameter. If the mechanical orientation is positive,
then the piston translation is positive in relation to the actuator case when the
gauge pressure at port **A** is positive. The direction of motion
reverses when the mechanical orientation is negative.

### Hard Stop

A set of hard stops limit the piston range of motion. The block uses an
implementation of the Translational Hard Stop block, which treats hard stops like
spring-damper systems. The spring stiffness coefficient controls the restorative
component of the hard-stop contact force and the damping coefficient the dissipative
component.

The hard stops are located at the distal ends of the piston stroke. If the
mechanical orientation is positive, then the lower hard stop is at *x* = 0, and the upper hard stop is at *x* = +*stroke*. If the mechanical orientation is negative, then the lower hard
stop is at *x* = -*stroke*, and the upper hard stop is at *x* = 0.

### Block Composite

This block is a composite component based on these Simscape™ Foundation blocks:

- Translational Mechanical
  Converter (G)
- Translational Hard
  Stop
- Ideal Translational Motion
  Sensor

Diagram of elements that make up the block.
