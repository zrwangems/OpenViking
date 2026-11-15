---
type: simulink-block
title: 'Rotating Single-Acting Actuator (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Actuators'
documentation_page: 'rotatingsingleactingactuatoril'
documentation_source_path: 'ref/rotatingsingleactingactuatoril.html'
language: en
---

# Rotating Single-Acting Actuator (IL)

## Ports

### Conserving

### **A** — Liquid chamber inlet port isothermal liquid

Inlet port to the liquid chamber.

### **C** — Actuator casing mechanical translational

Reference port for actuator velocity and force.

### **R** — Rod velocity mechanical translational

Port associated with the piston velocity and force.
### Input

### **W** — Actuator rotational velocity physical signal

Actuator rotational velocity, received as a physical signal in
rad/s.

### **p** — Piston position, m physical signal

Piston position in m, received as a physical signal from a Simscape
Multibody block.

#### Dependencies

To expose this port, set **Piston displacement**
to `Provide input signal from Multibody
joint`.
### Output

### **p** — Piston position, m physical signal

Piston position in m, returned as a physical signal.

#### Dependencies

To expose this port, set **Piston displacement**
to `Calculate from velocity of port R relative to port
C`.

## Parameters

### Actuator

### **Piston outer radius** — Piston outer radius `0.1 m` (default) | positive scalar

Piston outer radius.

### **Piston inner radius** — Piston inner radius `0.05 m` (default) | positive scalar

Piston inner radius.

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

### **Piston stroke** — Maximum piston travel distance `0.1 m` (default) | positive scalar

Maximum piston travel distance.

### **Dead volume** — Fluid volume at full piston retraction `1e-5 m^3` (default) | positive scalar

Volume of liquid when the piston displacement is `0`.
This is the liquid volume when the piston is up against the actuator end
cap.

### **Environment pressure specification** — Reference environment pressure `Atmospheric pressure` (default) | `Specified pressure`

Environment reference pressure. The `Atmospheric
pressure` option sets the environmental pressure to
0.101325 MPa.

### **Environment pressure** — User-defined environmental pressure `0.101325 MPa` (default) | positive scalar

User-defined environmental pressure.

#### Dependencies

To enable this parameter, set **Environment pressure
specification** to `Specified
pressure`.

### Fluid Channel

### **Fluid entry radius** — Fluid channel radius `0.06 m` (default) | positive scalar

Radius of the fluid opening in the rotating shaft. This value must be
greater than or equal to the **Piston inner radius**
and less than or equal to the **Piston outer
radius**.

### **Fluid channel cross-sectional area** — Fluid cross-sectional area `1e-3 m^2` (default) | positive scalar

Cross-sectional area of the fluid channel.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Flow discharge loss coefficient.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the orifice.

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

### Initial Conditions

### **Piston displacement** — Method for determining piston position `Calculate from velocity of port R relative to port C` (default) | `Provide input signal from Multibody joint`

Method for determining the piston position. The block can receive the
position from a Multibody block when set to `Provide input
signal from Multibody joint`, or calculates the
position internally and reports the position at port
**p**. The position is between `0`
and the **Piston stroke** when the mechanical
orientation is positive and `0` and –**Piston
stroke** when the mechanical orientation is
negative.

### **Initial piston displacement** — Piston position at start of simulation `0 m` (default) | scalar

Piston position at the start of the simulation.

#### Dependencies

To enable this parameter, set **Piston
displacement** to `Calculate from velocity
of port R relative to port C`.

### **Enable dynamic compressibility** — Whether to model fluid compressibility `on` (default) | `off`

Whether to model any change in fluid density due to fluid
compressibility. When you select **Enable dynamic
compressibility**, changes due to the mass flow rate into
the block are calculated in addition to density changes due to changes
in pressure. In the Isothermal Liquid Library, all blocks calculate
density as a function of pressure.

### **Initial liquid pressure** — Starting liquid pressure for compressible fluids `0.101325 MPa` (default) | positive scalar

Starting liquid pressure for compressible fluids.

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

Actuator on a rotating shaft in an isothermal liquid network

The Rotating Single-Acting Actuator (IL) block models an actuator that rotates around
its central axis in an isothermal liquid network. Rotating actuators are used in
rotating shaft control components such as friction clutches or brakes. The fluid enters
the actuator at port **A**. The angular velocity is set at port
**W**. Port **C** is associated with the actuator
casing and the piston velocity and force are set at port **R**.

When the piston position is calculated internally, it is reported at port
**p**, and when the position is set by a connection to a
Simscape™
Multibody™ joint, it is received as a physical signal at port **p**.
The motion of the piston when it is near full extension or full retraction is limited by
one of four hard stop models. **Enable dynamic compressibility** can
optionally be modeled.

### Displacement

The piston displacement is measured as the position at port **R**
relative to port **C**. The **Mechanical
orientation** identifies the direction of piston displacement. The
piston displacement is neutral, or `0`, when the chamber volume is
equal to the **Dead volume**. When displacement is received as an
input, ensure that the derivative of the position is equal to the piston velocity.
This is automatically the case when the input is received from a Translational Multibody Interface block
connection to a Simscape Multibody joint.

### Hard Stop Model

To avoid mechanical damage to an actuator when it is fully extended or fully
retracted, an actuator typically displays nonlinear behavior when the piston
approaches these limits. The Double-Acting Actuator (IL) block models this behavior
with a choice of four hard stop models, which model the material compliance through
a spring-damper system. The hard stop models are:

- `Stiffness and damping applied smoothly through transition
  region, damped rebound`.
- `Full stiffness and damping applied at bounds, undamped
  rebound`.
- `Full stiffness and damping applied at bounds, damped
  rebound`.
- `Based on coefficient of restitution`

The hard stop force is modeled when the piston is at its upper or lower bound. The
boundary region is within the **Transition region** of the
**Piston stroke** or piston initial displacement. Outside of
this region, FHardStop=0.

For more information about these settings, see the Translational Hard Stop block page.

### Block Subcomponents

The Rotating Single-Acting Actuator (IL) block comprises three Isothermal Liquid
library blocks:

- Rotating Channel (IL)
- Single-Acting Actuator (IL)
- Rotating Cylinder Force (IL)

**Actuator Schematic**
