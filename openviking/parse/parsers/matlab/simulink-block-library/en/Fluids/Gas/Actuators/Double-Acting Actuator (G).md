---
type: simulink-block
title: 'Double-Acting Actuator (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Actuators'
documentation_page: 'doubleactingactuatorg'
documentation_source_path: 'ref/doubleactingactuatorg.html'
language: en
---

# Double-Acting Actuator (G)

## Ports
```yaml
ports:
- name: p
  summary: Piston position input, m physical signal
  direction: input
- name: p
  summary: Piston position, m physical signal
  direction: output
- name: A
  summary: Liquid port gas
  direction: conserving
- name: B
  summary: Liquid port gas
  direction: conserving
- name: R
  summary: Actuator piston mechanical translational
  direction: conserving
- name: C
  summary: Actuator casing mechanical translational
  direction: conserving
- name: HA
  summary: Heat transfer thermal
  direction: conserving
- name: HB
  summary: Heat transfer thermal
  direction: conserving
```

### Input

### **p** — Piston position input, m physical signal

Physical signal input associated with the piston position, in m.
Connect this port to a Simscape
Multibody™ network using a Translational Multibody
Interface block.

#### Dependencies

To enable this port, set **Piston displacement from
chamber A cap** to `Provide input signal
from Multibody joint`.
### Output

### **p** — Piston position, m physical signal

Physical signal port associated with the piston position.

#### Dependencies

To enable this port, set **Piston displacement from
chamber A cap** to `Calculate from velocity
of port R relative to port C`.
### Conserving

### **A** — Liquid port gas

Gas conserving port associated with the inlet to chamber A.

### **B** — Liquid port gas

Gas conserving port associated with the inlet to chamber B.

### **R** — Actuator piston mechanical translational

Mechanical translational conserving port associated with the actuator
piston.

### **C** — Actuator casing mechanical translational

Mechanical translational conserving port associated with the actuator
casing.

### **HA** — Heat transfer thermal

Thermal conserving port associated with chamber A.

### **HB** — Heat transfer thermal

Thermal conserving port associated with chamber B.
## Parameters
```yaml
parameters:
- name: Same fluid on both sides
  summary: Option to model same fluid in both chambers on (default) | off
  group: Actuator
- name: Mechanical orientation
  summary: Piston displacement direction Pressure at A causes positive displacement of R relative to C (default) | Pressure
    at A causes negative displacement of R relative to C
  group: Actuator
- name: Piston cross-sectional area in chamber A
  summary: Chamber A piston area 0.01 m^2 (default) | positive scalar
  group: Actuator
- name: Piston cross-sectional area in chamber B
  summary: Chamber B piston area 0.01 m^2 (default) | positive scalar
  group: Actuator
- name: Piston stroke
  summary: Maximum piston travel distance 0.1 m (default) | positive scalar
  group: Actuator
- name: Dead volume in chamber A
  summary: Chamber A fluid volume at full piston retraction 1e-5 m^3 (default) | positive scalar
  group: Actuator
- name: Dead volume in chamber B
  summary: Chamber B fluid volume at full piston retraction 1e-5 m^3 (default) | positive scalar
  group: Actuator
- name: Cross-sectional area at port A
  summary: Area at port A 0.01 m^2 (default) | positive scalar
  group: Actuator
- name: Cross-sectional area at port B
  summary: Area at port B 0.01 m^2 (default) | positive scalar
  group: Actuator
- name: Environment pressure specification
  summary: Reference environment pressure Atmospheric pressure (default) | Specified pressure
  group: Actuator
- name: Environment pressure
  summary: User-defined environmental pressure 0.101325 MPa (default) | positive scalar
  group: Actuator
- name: Hard stop model
  summary: Hard stop model Stiffness and damping applied smoothly through transition region, damped rebound (default) | Full
    stiffness and damping applied at bounds, undamped rebound | Full stiffness and damping applied at bounds, damped rebound
    | Based on coefficient of restitution
  group: Hard Stop
- name: Hard-stop stiffness coefficient
  summary: Stiffness coefficient 1e10 N/m (default) | positive scalar
  group: Hard Stop
- name: Hard-stop damping coefficient
  summary: Damping coefficient 150 N*s/m (default) | positive scalar
  group: Hard Stop
- name: Transition region
  summary: Application range of hard stop force model 0.1 mm (default) | positive scalar
  group: Hard Stop
- name: Coefficient of restitution
  summary: Ratio of final-to-initial relative speed between slider and stop after collision 0.7 (default) | unitless value
    between 0 and 1
  group: Hard Stop
- name: Static contact speed threshold
  summary: Threshold relative speed between slider and stop before collision 0.001 m/s (default) | nonnegative scalar
  group: Hard Stop
- name: Static contact release force threshold
  summary: Force needed to transition from contact mode to free mode 0.001 N (default) | positive scalar
  group: Hard Stop
- name: Piston displacement from chamber A cap
  summary: Method for determining piston position Calculate from velocity of port R relative to port C (default) | Provide
    input signal from Multibody joint
  group: Initial Conditions
- name: Initial piston displacement from chamber A cap
  summary: Piston displacement at start of simulation 0 m (default) | scalar
  group: Initial Conditions
- name: Initial gas pressure in chamber A
  summary: Starting gas pressure in chamber A 0.101325 MPa (default) | positive scalar
  group: Initial Conditions
- name: Initial gas pressure in chamber B
  summary: Starting gas pressure in chamber B 0.101325 MPa (default) | positive scalar
  group: Initial Conditions
- name: Initial gas temperature in chamber A
  summary: Starting gas temperature in chamber A 293.15 K (default) | scalar
  group: Initial Conditions
- name: Initial gas temperature in chamber B
  summary: Starting gas temperature in chamber B 293.15 K (default) | scalar
  group: Initial Conditions
```

### Actuator

### **Same fluid on both sides** — Option to model same fluid in both chambers `on` (default) | `off`

Whether to model the same fluid in both actuator chambers. If you
select this parameter, the actuator propagates fluid properties through
both chambers. Clear this parameter to model each chamber as a different
fluid, where each chamber is connected to an isolated fluid network.

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

### **Piston cross-sectional area in chamber A** — Chamber A piston area `0.01 m^2` (default) | positive scalar

Cross-sectional area of the piston rod on the chamber A side.

### **Piston cross-sectional area in chamber B** — Chamber B piston area `0.01 m^2` (default) | positive scalar

Cross-sectional area of the piston rod on the chamber B side.

### **Piston stroke** — Maximum piston travel distance `0.1 m` (default) | positive scalar

Maximum piston travel distance.

### **Dead volume in chamber A** — Chamber A fluid volume at full piston retraction `1e-5 m^3` (default) | positive scalar

Volume of gas when the piston displacement is `0` in chamber A. This
parameter is the gas volume when the piston is against the actuator end
cap.

### **Dead volume in chamber B** — Chamber B fluid volume at full piston retraction `1e-5 m^3` (default) | positive scalar

Volume of gas when the piston displacement is `0` in chamber B. This
parameter is the gas volume when the piston is against the actuator end
cap.

### **Cross-sectional area at port A** — Area at port A `0.01 m^2` (default) | positive scalar

Cross-sectional area of port **A**.

### **Cross-sectional area at port B** — Area at port B `0.01 m^2` (default) | positive scalar

Cross-sectional area of port **B**.

### **Environment pressure specification** — Reference environment pressure `Atmospheric pressure` (default) | `Specified pressure`

Environment reference pressure. When you select `Atmospheric
pressure`, the block assumes a pressure of 0.101325
MPa.

### **Environment pressure** — User-defined environmental pressure `0.101325 MPa` (default) | positive scalar

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

Application range of the hard stop force model. The block does not apply the hard stop
model when the maximum extension or retraction of the piston is outside
of this range. In this situation, there is no additional force on the
piston.

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

### **Piston displacement from chamber A cap** — Method for determining piston position `Calculate from velocity of port R relative to port C` (default) | `Provide input signal from Multibody joint`

Method for determining the piston position. The block can receive the position from a
Multibody block when set to `Provide input signal from
Multibody joint`, or can calculate the position
internally and report the position at port **p**. The
position is between `0` and the value of the
**Piston stroke** parameter when the mechanical
orientation is positive and between `0` and the
negative value of the **Piston stroke** parameter when
the mechanical orientation is negative.

### **Initial piston displacement from chamber A cap** — Piston displacement at start of simulation `0` `m` (default) | scalar

Piston position at the start of the simulation with respect to the
chamber A cap.

#### Dependencies

To enable this parameter, set **Piston
displacement** to `Calculate from velocity
of port R relative to port C`.

### **Initial gas pressure in chamber A** — Starting gas pressure in chamber A `0.101325` `MPa` (default) | positive scalar

Starting gas pressure in chamber A.

### **Initial gas pressure in chamber B** — Starting gas pressure in chamber B `0.101325` `MPa` (default) | positive scalar

Starting gas pressure in chamber B.

### **Initial gas temperature in chamber A** — Starting gas temperature in chamber A `293.15` `K` (default) | scalar

Initial temperature of the gas volume in the actuator.

### **Initial gas temperature in chamber B** — Starting gas temperature in chamber B `293.15` `K` (default) | scalar

Initial temperature of the gas volume in the actuator.
## Libraries

Simscape / Fluids / Gas / Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

### R2024a: Model different fluids on each side of the actuator

Clear the new **Same fluid on both sides** parameter to block
the propagation of fluid properties and model each chamber as a different fluid
connected to its own isolated fluid network.

## Description

Double-acting linear actuator in a gas network

The Double-Acting Actuator (G) block models a linear actuator with a piston
controlled by two opposing gas chambers. The actuator generates force in the extension
and retraction strokes. The generated force depends on the pressure difference between
the two chambers.

The figure shows the key components of the actuator. Ports **A** and
**B** represent the gas chamber inlets. Port **R**
represents the translating actuator piston and port **C** represents
the actuator case. Ports **HA** and **HB** represent
the thermal interfaces between each gas chamber and the environment. The moving piston
is adiabatic.

Double-Acting Actuator Schematic

### Displacement

The block measures the piston displacement as the position at port **R**
relative to port **C**. The **Mechanical
orientation** parameter identifies the direction of piston
displacement. The piston displacement is neutral, or `0`, when the
chamber A volume is equal to the value of the **Dead volume in chamber
A** parameter. When the **Piston displacement from chamber A
cap** parameter is `Provide input signal from Multibody
joint`, you input the piston displacement using port
**p**. Ensure that the derivative of the position signal is
equal to the piston velocity. You can ensure that the derivative of the position
signal is equal to the piston velocity by using a Translational Multibody Interface block to
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
