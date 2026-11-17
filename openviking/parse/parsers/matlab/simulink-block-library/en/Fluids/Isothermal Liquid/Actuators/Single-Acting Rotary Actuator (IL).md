---
type: simulink-block
title: 'Single-Acting Rotary Actuator (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Actuators'
documentation_page: 'singleactingrotaryactuatoril'
documentation_source_path: 'ref/singleactingrotaryactuatoril.html'
language: en
---

# Single-Acting Rotary Actuator (IL)

## Ports
```yaml
ports:
- name: A
  summary: Liquid port isothermal liquid
  direction: conserving
- name: R
  summary: Actuator mechanical translational
  direction: conserving
- name: C
  summary: Casing mechanical translational
  direction: conserving
- name: q
  summary: Shaft angle physical signal
  direction: input
- name: q
  summary: Shaft angle physical signal
  direction: output
```

### Conserving

### **A** — Liquid port isothermal liquid

Isothermal liquid conserving port associated with the actuator.

### **R** — Actuator mechanical translational

Mechanical rotational conserving port associated with the shaft angular velocity and
torque.

### **C** — Casing mechanical translational

Mechanical rotational conserving port associated with the actuator
casing.
### Input

### **q** — Shaft angle physical signal

Shaft angle, received as a physical signal from a Simscape
Multibody block.

#### Dependencies

To expose this port, set **Shaft rotation from chamber
A** to `Provide input signal from Multibody
joint`.
### Output

### **q** — Shaft angle physical signal

Shaft angle, reported as a physical signal.

#### Dependencies

To expose this port, set **Shaft rotation from chamber
A** to `Calculate from angular velocity of
port R relative to port C`.
## Parameters
```yaml
parameters:
- name: Mechanical orientation
  summary: Piston displacement direction Pressure at A causes positive displacement of R relative to C (default) | Pressure
    at A causes negative displacement of R relative to C
  group: Actuator
- name: Volume displacement
  summary: Volume displacement 1e-4 m^3/rad (default) | positive scalar
  group: Actuator
- name: Stroke
  summary: Angle 5.0 rad (default) | positive scalar
  group: Actuator
- name: Dead volume
  summary: Fluid volume 1e-5 m^3 (default) | positive scalar
  group: Actuator
- name: Environment pressure specification
  summary: Pressure reference source Atmospheric pressure (default) | Specified pressure
  group: Actuator
- name: Environment pressure
  summary: User-defined pressure reference 0.101325 MPa (default)
  group: Actuator
- name: Hard stop model
  summary: Select the hard stop model Stiffness and damping applied smoothly through transition region, damped rebound (default)
    | Full stiffness and damping applied at bounds, undamped rebound | Full stiffness and damping applied at bounds, damped
    rebound | Based on coefficient of restitution
  group: Hard Stop
- name: Hard stop stiffness coefficient
  summary: Stiffness coefficient 1e6 N\*m/rad (default) | positive scalar
  group: Hard Stop
- name: Hard stop damping coefficient
  summary: Damping coefficient 150 N\*m(rad/s) (default) | positive scalar
  group: Hard Stop
- name: Transition region
  summary: Transition region 0.001 rad (default) | positive scalar
  group: Hard Stop
- name: Coefficient of restitution
  summary: Ratio of final-to-initial relative speed between slider and stop after collision 0.7 (default) | unitless value
    between 0 and 1
  group: Hard Stop
- name: Static contact speed threshold
  summary: Threshold relative speed between slider and stop before collision 0.1 rad/s (default) | nonnegative scalar
  group: Hard Stop
- name: Static contact release torque threshold
  summary: Threshold torque needed to transition from contact mode to free mode 0.001 N*m (default) | positive scalar
  group: Hard Stop
- name: Shaft rotation from chamber A
  summary: Method for determining shaft angle Calculate from angular velocity of port R relative to port C (default) | Provide
    input signal from Multibody joint
  group: Initial Conditions
- name: Initial shaft rotation
  summary: Initial rotation 0 rad (default) | scalar
  group: Initial Conditions
- name: Enable dynamic compressibility
  summary: Fluid compressibility On (default) | Off
  group: Initial Conditions
- name: Initial liquid pressure
  summary: Liquid pressure 0.101325 MPa (default) | positive scalar
  group: Initial Conditions
- name: Nominal liquid pressure
  summary: Pressure at nominal operating conditions 0.101325 MPa (default) | scalar
  group: Initial Conditions
```

### Actuator

### **Mechanical orientation** — Piston displacement direction `Pressure at A causes positive displacement of R relative to C` (default) | `Pressure at A causes negative displacement of R relative to C`

Sets the piston displacement direction. When you set this parameter to:

- `Pressure at A causes positive displacement of
  R relative to C` the piston displacement is
  positive when the volume of liquid at port
  **A** is expanding. This corresponds to
  rod extension.
- `Pressure at A causes negative displacement of
  R relative to C` the piston displacement is
  negative when the volume of liquid at port
  **A** is expanding. This corresponds to
  rod contraction.

### **Volume displacement** — Volume displacement `1e-4 m^3/rad` (default) | positive scalar

Effective displacement of the actuator.

### **Stroke** — Angle `5.0 rad` (default) | positive scalar

Shaft maximum travel between stops.

### **Dead volume** — Fluid volume `1e-5 m^3` (default) | positive scalar

Volume of liquid when the piston displacement is `0`.
This is the liquid volume when the piston is up against the actuator end
cap.

### **Environment pressure specification** — Pressure reference source `Atmospheric pressure` (default) | `Specified pressure`

Choice of environment pressure. Options include
`Atmospheric pressure` and
`Specified pressure`.

### **Environment pressure** — User-defined pressure reference `0.101325 MPa` (default)

Pressure outside the actuator casing. This pressure acts against the
pressures inside the actuator chambers. A value of zero corresponds to a
vacuum.

#### Dependencies

To enable this parameter, set **Environment pressure
specification** to `Specified
pressure`.

### Hard Stop

### **Hard stop model** — Select the hard stop model `Stiffness and damping applied smoothly through transition region, damped rebound` (default) | `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

Model choice for the force on the piston at full extension or full
retraction. See the Rotational Hard Stop block for more
information.

### **Hard stop stiffness coefficient** — Stiffness coefficient `1e6` N\*m/rad (default) | positive scalar

Specifies the elastic property of colliding bodies for the Rotational Hard Stop block.
The greater the value of the parameter, the more rigid the impact
between the piston and the stop becomes. Lower values make contact
softer and generally improve convergence and computational
efficiency.

#### Dependencies

To enable this parameter, set **Hard stop model** to

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **Hard stop damping coefficient** — Damping coefficient `150` N\*m(rad/s) (default) | positive scalar

Specifies the dissipating property of colliding bodies for the Rotational Hard Stop
block. At zero damping, the impact is elastic. The greater the value of
the parameter, the greater the energy dissipation during piston-stop
interaction. Damping affects slider motion as long as the slider is in
contact with the stop, including the period when slider is pulled back
from the contact. Set this parameter to a nonzero value to improve the
efficiency and convergence of your simulation.

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

### **Transition region** — Transition region `0.001 rad` (default) | positive scalar

Distance below which scaling is applied to the hard-stop force. The
contact force is zero when the distance to the hard stop is equal to the
value of this parameter. The contact force is at its full value when the
distance to the hard stop is zero.

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

### **Static contact speed threshold** — Threshold relative speed between slider and stop before collision `0.1 rad/s` (default) | nonnegative scalar

Threshold relative speed between the slider and stop before collision. When the slider
hits the case with speed less than the value of the **Static
contact speed threshold** parameter, they stay in contact.
Otherwise, the slider bounces. To avoid modeling static contact between
the slider and the case, set this parameter to
`0`.

#### Dependencies

To enable this parameter, set **Hard stop model**
to `Based on coefficient of
restitution`.

### **Static contact release torque threshold** — Threshold torque needed to transition from contact mode to free mode `0.001 N*m` (default) | positive scalar

Minimum torque needed to release the slider from a static contact mode.

#### Dependencies

To enable this parameter, set **Hard stop model**
to `Based on coefficient of
restitution`.

### Initial Conditions

### **Shaft rotation from chamber A** — Method for determining shaft angle `Calculate from angular velocity of port R relative to port C` (default) | `Provide input signal from Multibody joint`

Method for determining the shaft angle. The block can receive the
angle from a Multibody block when set to `Provide input
signal from Multibody joint`, or calculates the angle
internally, which is reported at port **q**.

### **Initial shaft rotation** — Initial rotation `0 rad` (default) | scalar

The position of the actuator at the beginning of simulation. This value falls between
`0` and the value of the
**Stroke** in the positive orientation, and
`0` and the negative value of the
**Stroke** in the negative orientation.

#### Dependencies

To enable this parameter, set **Shaft rotation from
chamber A** to `Calculate from angular
velocity of port R relative to port C`.

### **Enable dynamic compressibility** — Fluid compressibility `On` (default) | `Off`

Whether to model any change in fluid density due to fluid
compressibility. When you select **Enable dynamic
compressibility**, changes due to the mass flow rate into
the block are calculated in addition to density changes due to changes
in pressure. In the Isothermal Liquid Library, all blocks calculate
density as a function of pressure.

### **Initial liquid pressure** — Liquid pressure `0.101325 MPa` (default) | positive scalar

Pressure in actuator chamber A at the start of simulation.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.

### **Nominal liquid pressure** — Pressure at nominal operating conditions `0.101325 MPa` (default) | scalar

Liquid pressure at nominal operating conditions. The block uses this
value to calculate the nominal density to use in the mass conservation
equation when dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** checkbox.
## Libraries

Simscape / Fluids / Isothermal Liquid / Actuators

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

Single-acting rotary actuator in an isothermal liquid system

The Single-Acting Rotary Actuator (IL) block models a rotary
actuator that converts liquid pressure into mechanical torque in an isothermal liquid
network. The motion of the piston when it is near full extension or full retraction is
limited by one of four hard stop models.

Port **A** is the isothermal liquid conserving port associated with inlet
of the liquid chamber. Ports **R** and **C** are the
mechanical rotational conserving ports associated with the rotating shaft and the
actuator casing, respectively. If **Mechanical orientation** is set to
`Pressure at A causes positive rotation of R relative to
C`, the pressure in the liquid chamber causes a positive rotation of the
shaft at port **R** relative to port **C**. When the
shaft angle is calculated internally, the physical signal port **q**
reports the angle. When the angle is set by a connection to a Simscape™
Multibody™ joint, it is received as a physical signal at port
**q**.

### Displacement

The piston displacement is measured as the position at port **R** relative
to port **C**. The **Mechanical orientation**
identifies the direction of piston displacement. The piston displacement is neutral,
or `0`, when the chamber volume is equal to the **Dead
volume**. When displacement is received as an input, ensure that the
derivative of the position is equal to the piston velocity. This is automatically
the case when the input is received from a Rotational Multibody Interface block
connection to a Simscape Multibody joint.

### Hard Stop Model

To avoid mechanical damage to an actuator when it is fully extended or fully retracted, an
actuator typically displays nonlinear behavior when the piston approaches these
limits. The Single-Acting Rotary Actuator (IL) block models this behavior with a
choice of four hard stop models, which model the material compliance through a
spring-damper system. The hard stop models are:

- `Stiffness and damping applied smoothly through transition
  region, damped rebound`.
- `Full stiffness and damping applied at bounds, undamped
  rebound`.
- `Full stiffness and damping applied at bounds, damped
  rebound`.
- `Based on coefficient of restitution`

The hard stop force is modeled when the piston is at its upper or lower bound. The boundary
region is within the **Transition region** of the
**Stroke** or piston initial displacement. Outside of this
region, FHardStop=0.

For more information about these settings, see the Rotational Hard Stop block page.

### Block Schematics

The actuator block comprises three Foundation Library blocks:

- Ideal Rotational Motion Sensor
- Rotational Hard Stop
- Rotational Mechanical Converter (IL)

**Underlying Block Components**

### Leakage

Laminar leakage is not accounted for in the Single-Acting Rotary Actuator
(IL) block. To include leakage in your simulation, set the
**Cross-sectional geometry** parameter to
`Custom` and connect port **A** to
port **A** of the Laminar Leakage (IL) block.
Connect port **B** of the Laminar Leakage (IL) block to a Reservoir (IL)
block.

**Adding Leakage to the Simulation**
