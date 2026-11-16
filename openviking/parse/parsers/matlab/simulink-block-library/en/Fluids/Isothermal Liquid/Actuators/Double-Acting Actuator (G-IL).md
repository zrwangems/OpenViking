---
type: simulink-block
title: 'Double-Acting Actuator (G-IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Actuators'
documentation_page: 'doubleactingactuatorgil'
documentation_source_path: 'ref/doubleactingactuatorgil.html'
language: en
---

# Double-Acting Actuator (G-IL)

## Ports

### Output

### **p** — Piston position, m physical signal

Physical signal port associated with the piston position.
### Conserving

### **A** — Inlet to chamber A isothermal liquid

Isothermal liquid conserving port associated with the inlet to chamber
A.

### **B** — Inlet to chamber B gas

Gas conserving port associated with the inlet to chamber B.

### **C** — Actuator casing mechanical translational

Mechanical translational conserving port associated with the case.

### **R** — Actuator piston rod mechanical translational

Mechanical translational conserving port associated with the piston
rod.

### **H** — Heat flow thermal

Thermal conserving port associated with heat transfer to or from the
gas chamber.

## Parameters

### Configuration

### **Mechanical orientation** — Piston displacement direction `Pressure at A causes positive displacement of R relative to C` (default) | `Pressure at A causes negative displacement of R relative to C`

Piston displacement direction. `Pressure at A causes positive displacement
of R relative to C` corresponds to piston extension
when the pressure difference between chambers A and B is positive.
`Pressure at A causes negative displacement of R
relative to C` corresponds to piston retraction when
the pressure difference between chambers A and B is positive.

### **Piston stroke** — Maximum piston travel distance `0.1 m` (default) | positive scalar

Maximum piston travel distance.

### **Initial piston displacement from chamber A cap** — Piston position at start of simulation `0 m` (default) | scalar

Piston position at the start of the simulation.

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

### Isothermal Liquid Side

### **Piston cross-sectional area in chamber A** — Cross-sectional area of piston rod `0.01 m^2` (default) | positive scalar

Cross-sectional area of the piston rod in chamber A.

### **Dead volume in chamber A** — Chamber volume at full piston retraction `1e-5 m^3` (default) | positive scalar

Open volume in the fluid chamber when the piston is fully
retracted.

### **Enable dynamic compressibility** — Whether to model fluid compressibility `On` (default) | `Off`

Whether to model any change in fluid density due to fluid
compressibility. When **Fluid compressibility** is set
to `On`, changes due to the mass flow rate into
the block are calculated in addition to density changes due to changes
in pressure. In the Isothermal Liquid Library, all blocks calculate
density as a function of pressure.

### **Initial liquid pressure in chamber A** — Initial liquid pressure for compressible fluids `0.101325 MPa` (default) | positive scalar

Initial liquid pressure for compressible fluids.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.

### **Nominal liquid pressure in chamber A** — Pressure at nominal operating conditions in chamber A `0.101325 MPa` (default) | scalar

Liquid pressure at nominal operating conditions in chamber A. The
block uses this value to calculate the nominal density to use in the
mass conservation equation when dynamic compressibility is
disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** checkbox.

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

### Gas Side

### **Piston cross-sectional area in chamber B** — Cross-sectional area of piston rod `0.01 m^2` (default) | positive scalar

Cross-sectional area of the piston rod in chamber B.

### **Cross-sectional area at port B** — Port cross-sectional area `1e-3 m^2` (default) | positive scalar

Cross-sectional area at port **B**.

### **Dead volume in chamber B** — Chamber volume at full piston retraction `1e-5 m^3` (default) | positive scalar

Open volume in the gas chamber when the piston is fully
retracted.

### **Initial gas pressure in chamber B** — Starting gas chamber pressure `0.101325 MPa` (default) | positive scalar

Initial pressure in the gas chamber.

### **Initial gas temperature in chamber B** — Starting gas chamber temperature `293.15 K` (default) | positive scalar

Initial temperature in the gas chamber.

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

Linear actuator with isothermal liquid and gas chambers

The Double-Acting Actuator (G-IL) block represents an
isothermal liquid chamber and a gas chamber separated by a piston plate. The piston
actuation is controlled by the pressure differential between the chambers. The motion of
the piston when it is near full extension or full retraction is limited by one of four
hard stop models.

Port **A** is the isothermal liquid inlet and port **B**
is the gas inlet. Connect elements for heat transfer between the gas chamber and the
environment to port **H**. Port **C** acts as a
mechanical translational reference for the actuator casing. Port **R**
is associated with the actuator piston. The piston position is reported at port
**P**.

### Displacement

The piston displacement is measured as the position at port **R** relative
to port **C**. The **Mechanical orientation**
identifies the direction of piston displacement. The piston displacement is neutral,
or `0`, when the chamber volume is equal to the chamber dead
volume. When displacement is received as an input, ensure that the derivative of the
position is equal to the piston velocity. This is automatically the case when the
input is received from a Translational Multibody Interface block
connection to a Simscape™
Multibody™ joint.

### Hard Stop Model

To avoid mechanical damage to the piston when it is fully extended or fully retracted, an
actuator typically displays nonlinear behavior when the piston approaches these
limits. The Double-Acting Actuator (G-IL) block models this behavior with a choice
of four hard stop models, which model the material compliance through a
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
**Piston stroke** or piston initial displacement. Outside of
this region, FHardStop=0.

For more information about these settings, see the Translational Hard Stop block page.

### Block Schematic

The Double-Acting Actuator (G-IL) block is a composite of
four Simscape Foundation blocks:

- Translational Mechanical
  Converter (G)
- Translational Mechanical Converter (IL)
- Translational Hard
  Stop
- Ideal Translational Motion
  Sensor
