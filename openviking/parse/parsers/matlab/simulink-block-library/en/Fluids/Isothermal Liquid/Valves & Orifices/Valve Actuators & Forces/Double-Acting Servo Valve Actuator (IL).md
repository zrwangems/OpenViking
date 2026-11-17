---
type: simulink-block
title: 'Double-Acting Servo Valve Actuator (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces'
documentation_page: 'doubleactingservovalveactuatoril'
documentation_source_path: 'ref/doubleactingservovalveactuatoril.html'
language: en
---

# Double-Acting Servo Valve Actuator (IL)

## Ports
```yaml
ports:
- name: A
  summary: Liquid port for chamber A isothermal liquid
  direction: conserving
- name: B
  summary: Liquid port for chamber B isothermal liquid
  direction: conserving
- name: S
  summary: Spool position, m physical signal
  direction: output
```

### Conserving

### **A** — Liquid port for chamber A isothermal liquid

Isothermal liquid conserving port associated with the liquid inlet of
chamber A.

### **B** — Liquid port for chamber B isothermal liquid

Isothermal liquid conserving port associated with the liquid inlet of
chamber B.
### Output

### **S** — Spool position, m physical signal

Physical signal associated with the spool position, in m. A position
of zero indicates that the spool is at a neutral position in the middle
of a stroke.
## Parameters
```yaml
parameters:
- name: Spool cross-sectional area
  summary: Area measurement 1e-4 m^2 (default) | positive scalar
  group: Actuator
- name: Spool stroke
  summary: Distance 5e-3 m (default) | positive scalar
  group: Actuator
- name: Spring stiffness
  summary: Rate of force for the spring 1e3 N/m (default) | scalar
  group: Actuator
- name: Damping coefficient
  summary: Damping coefficient 150 N/(m/s) (default) | positive scalar
  group: Actuator
- name: Hard stop model
  summary: Select the hard stop model Stiffness and damping applied smoothly through transition region, damped rebound (default)
    | Full stiffness and damping applied at bounds, undamped rebound | Full stiffness and damping applied at bounds, damped
    rebound | Based on coefficient of restitution
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
  summary: Threshold force needed to transition from contact mode to free mode 0.001 N (default) | positive scalar
  group: Hard Stop
- name: Spool initial displacement
  summary: Initial location of the spool 0 m (default) | scalar
  group: Effects and Initial Conditions
- name: Enable dynamic compressibility
  summary: Fluid compressibility On (default) | Off
  group: Effects and Initial Conditions
- name: Nominal liquid pressure in chamber A
  summary: Pressure at nominal operating conditions in chamber A 0.101325 MPa (default) | scalar
  group: Effects and Initial Conditions
- name: Nominal liquid pressure in chamber B
  summary: Pressure at nominal operating conditions in chamber B 0.101325 MPa (default) | scalar
  group: Effects and Initial Conditions
- name: Initial liquid pressure in chamber A
  summary: Liquid pressure 0.101325 MPa (default) | positive scalar
  group: Effects and Initial Conditions
- name: Initial liquid pressure in chamber B
  summary: Liquid pressure 0.101325 MPa (default) | positive scalar
  group: Effects and Initial Conditions
```

### Actuator

### **Spool cross-sectional area** — Area measurement `1e-4 m^2` (default) | positive scalar

Cross-sectional area of the spool

### **Spool stroke** — Distance `5e-3 m` (default) | positive scalar

Distance the spool travels in a stroke.

### **Spring stiffness** — Rate of force for the spring `1e3 N/m` (default) | scalar

Spring rate of the centering springs.

### **Damping coefficient** — Damping coefficient `150 N/(m/s)` (default) | positive scalar

Damping coefficient in the contact between the piston and the
case.

### Hard Stop

### **Hard stop model** — Select the hard stop model `Stiffness and damping applied smoothly through transition region, damped rebound` (default) | `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

Model choice for the force on the piston at full extension or full
retraction. See the Translational Hard Stop block for more
information.

### **Hard-stop stiffness coefficient** — Stiffness coefficient `1e10` `N/m` (default) | positive scalar

Piston stiffness coefficient.

#### Dependencies

To enable this parameter, set **Hard stop model**
to

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

To enable this parameter, set **Hard stop model**
to

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **Transition region** — Application range of hard stop force model `0.1` `mm` (default) | positive scalar

Application range of the hard stop force model. Outside of this range
of the piston maximum extension and piston maximum retraction, the
**Hard stop model** is not applied and there is no
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

Threshold relative speed between slider and stop before collision.
When the slider hits the case with speed less than the value of the
**Static contact speed threshold** parameter, they
stay in contact. Otherwise, the slider bounces. To avoid modeling static
contact between the slider and the case, set this parameter to
`0`.

#### Dependencies

To enable this parameter, set **Hard stop model**
to `Based on coefficient of
restitution`.

### **Static contact release force threshold** — Threshold force needed to transition from contact mode to free mode `0.001 N` (default) | positive scalar

Minimum force needed to release the slider from a static contact mode.

#### Dependencies

To enable this parameter, set **Hard stop model**
to `Based on coefficient of
restitution`.

### Effects and Initial Conditions

### **Spool initial displacement** — Initial location of the spool `0 m` (default) | scalar

When the initial displacement of the spool is set to 0, the spool
begins directly between chamber A and chamber B. A positive distance
moves the spool away from chamber A, while a negative amount moves the
spool toward chamber A.

### **Enable dynamic compressibility** — Fluid compressibility `On` (default) | `Off`

Whether to model any change in fluid density due to fluid compressibility. When
**Enable dynamic compressibility** is set to
`On`, changes due to the mass flow rate
into the block are calculated in addition to density changes due to
changes in pressure. In the Isothermal Liquid Library, all blocks
calculate density as a function of pressure.

### **Nominal liquid pressure in chamber A** — Pressure at nominal operating conditions in chamber A `0.101325 MPa` (default) | scalar

Liquid pressure at nominal operating conditions in chamber A. The
block uses this value to calculate the nominal density to use in the
mass conservation equation when dynamic compressibility is
disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** checkbox.

### **Nominal liquid pressure in chamber B** — Pressure at nominal operating conditions in chamber B `0.101325 MPa` (default) | scalar

Liquid pressure at nominal operating conditions in chamber B. The
block uses this value to calculate the nominal density to use in the
mass conservation equation when dynamic compressibility is
disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** checkbox.

### **Initial liquid pressure in chamber A** — Liquid pressure `0.101325 MPa` (default) | positive scalar

Pressure in actuator chamber A at the start of simulation.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.

### **Initial liquid pressure in chamber B** — Liquid pressure `0.101325 MPa` (default) | positive scalar

Pressure in actuator chamber B at the start of simulation.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.
## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

### R2023a: New hard stop parameterization option

The block has a new option for the **Hard stop model** parameter.
This option, called `Based on coefficient of restitution`,
models the hard stop by using a mode chart.

## Description

Double-acting servo cylinder with spring-centered spool in an isothermal liquid system

The Double-Acting Servo Valve Actuator (IL) block models a
double-acting servo cylinder arranged as a spring-centered spool. The spring neutral
position is where the spool is located at the middle of the stroke. The motion of the
piston when it is near full extension or full retraction is limited by one of four hard
stop models. Fluid compressibility is optionally modeled in both piston chambers.

The physical signal output **S** reports the spool position.

### Hard Stop Model

To avoid mechanical damage to an actuator when it is fully extended or fully retracted, an
actuator typically displays nonlinear behavior when the piston approaches these
limits. The Double-Acting Servo Valve Actuator (IL) block models this behavior with
a choice of four hard stop models, which model the material compliance through a
spring-damper system. The hard stop models are:

- `Stiffness and damping applied smoothly through transition
  region, damped rebound`.
- `Full stiffness and damping applied at bounds, undamped
  rebound`.
- `Full stiffness and damping applied at bounds, damped
  rebound`.
- `Based on coefficient of restitution`

The hard stop force is modeled when the piston is at its upper or lower bound. The
boundary region is within the **Transition region** of the
**Spool stroke** or piston initial displacement. Outside of
this region, FHardStop=0.

For more information about these settings, see the Translational Hard Stop block page.

### Block Schematic

The Double-Acting Servo Actuator block comprises an Isothermal Liquid library
block and two Simscape Foundation blocks:

- Double-Acting Actuator (IL)
- Translational Spring
- Translational Damper
