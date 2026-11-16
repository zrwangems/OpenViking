---
type: simulink-block
title: 'Double-Acting Actuator (TL-G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid Library / Actuators'
documentation_page: 'doubleactingactuatortlg'
documentation_source_path: 'ref/doubleactingactuatortlg.html'
language: en
---

# Double-Acting Actuator (TL-G)

## Ports

### Output

### **P** — Piston position, m physical signal

Physical signal output port associated with the piston position. The
measurement is absolute. The first reading is the value of the
**Piston initial displacement** parameter.
### Conserving

### **A** — Inlet to chamber A thermal liquid

Thermal liquid conserving port associated with the inlet to chamber
A.

### **B** — Inlet to chamber B gas

Gas conserving port representing the inlet to chamber B.

### **R** — Actuator piston mechanical translational

Mechanical translational conserving port representing the actuator
piston.

### **C** — Actuator casing mechanical translational

Mechanical translational conserving port representing the actuator
casing.

### **HA** — Chamber A heat flow thermal

Thermal conserving port associated with the surface through which heat
exchange can occur between the thermal liquid volume and the actuator
surroundings. The thermal processes at this port influence the
temperature in the thermal liquid chamber and therefore at port
**A**.

### **HB** — Chamber B heat flow thermal

Thermal conserving port associated with the surface through which heat
exchange can occur between the gas volume and the actuator surroundings.
The thermal processes at this port influence the temperature in the gas
chamber and therefore at port **A**.

## Parameters

### Thermal Liquid Side

### **Mechanical orientation** — Direction of motion of the piston relative to the direction of flow of the fluid `Positive` | `Negative`

Orientation of the actuator piston relative to the direction of fluid
flow. A positive orientation causes the piston to move in the positive
direction relative to the actuator casing in response to a positive flow
rate through port A. The mechanical orientation affects the placement of
the piston hard stops. See the block description for more information on
the hard stop placement.

### **Piston cross-sectional area in chamber A** — Cross-sectional area of the fluid volume in the thermal liquid chamber `0.01 m^2` (default) | scalar in units of area

Area normal to the direction of flow in the body of the thermal liquid
chamber. The block uses this area to calculate the hydraulic force due
to the fluid pressure in the thermal liquid chamber. This parameter must
be greater than zero.

### **Piston stroke** — Distance of travel of the piston from hard stop to hard stop `0.2 m` (default) | scalar in units of length

Total distance of travel available to the piston, from one hard stop
to the other. The hard stops limit the piston motion so that the piston
is confined to stroke of the piston. See the block description for more
information on the locations of the hard stops.

### **Piston initial displacement** — Position of the piston at the start of simulation `0 m` (default) | scalar in units of length

Absolute position of the piston at the start of simulation. The zero
position coincides with the lower hard stop if the mechanical
orientation is positive and with the upper hard stop if the mechanical
orientation is negative.

### **Dead volume in chamber A** — Fluid volume in the thermal liquid chamber in the bottomed-out position `1e-4 m^3` (default) | scalar in units of volume

Thermal liquid volume remaining in the thermal liquid chamber when the
piston is pressed against the hard stop closest to the thermal liquid
inlet. The dead volume enables the block to capture the internal states
of the thermal liquid volume—its pressure and
temperature—when this volume is at a minimum. This parameter must
be greater than zero.

### **Enable dynamic compressibility** — Choice to model the effects of dynamic compressibility inside the thermal liquid chamber `On` (default) | `Off`

Option to model the effects of dynamic compressibility inside the
thermal liquid chamber. The thermal liquid is treated as compressible if
this parameter is set to `On` and as
incompressible if it is set to `Off`. The block
ignores the dependence of the thermal liquid density on pressure and
temperature if `Off` is selected.

### **Initial liquid pressure in chamber A (absolute)** — Absolute pressure in the thermal liquid chamber `0.101325 Pa` (default) | scalar in units of pressure

Pressure inside the thermal liquid chamber at simulation time zero
relative to absolute zero. This parameter helps set the initial states
of the thermal liquid volume.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.

### **Initial liquid temperature in chamber A** — Temperature in the thermal liquid chamber at the start of simulation `293.15 K` (default) | scalar in units of temperature

Average temperature inside the thermal liquid chamber at the start of
simulation. This parameter helps set the initial states of the thermal
liquid volume.

### **Nominal liquid pressure in chamber A (absolute)** — Pressure at nominal operating conditions in chamber A `0.101325 MPa` (default) | scalar

Liquid pressure at nominal operating conditions in chamber A. The
block uses this value to calculate the nominal density to use in the
mass conservation equation when dynamic compressibility is
disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** checkbox.

### **Nominal liquid temperature in chamber A** — Temperature at nominal operating conditions in chamber A `293.15` `K` (default) | scalar

Liquid temperature at nominal operating conditions in chamber A. The
block uses this value to calculate the nominal density to use in the
mass conservation equation when dynamic compressibility is
disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** checkbox.

### **Environment pressure specification** — Choice of atmospheric or custom environment pressure for the thermal liquid side `Atmospheric pressure` (default) | `Specified pressure`

Option to set the environment pressure of the thermal liquid chamber
to the typical value of one earth atmosphere or to a custom value.
Selecting `Specified pressure` exposes an
additional parameter, **Environment pressure**, that
you use to specify a custom pressure.

### **Environment pressure** — Absolute pressure of the environment outside the thermal liquid chamber `0.101325 MPa` (default) | scalar in units of pressure

Pressure outside the thermal liquid chamber relative to absolute zero.
This pressure acts against the pressure inside the thermal liquid
chamber. A pressure of zero corresponds to a perfect vacuum.

#### Dependencies

This parameter is enabled when the **Environment pressure
specification** is set to `Specified
pressure`.

### Gas Side

### **Piston cross-sectional area in chamber B** — Cross-sectional area of the fluid volume in the gas chamber `1e-3 m^2` (default) | positive scalar in units of area

Area normal to the direction of flow in the body of the gas chamber.
The block uses this area to calculate the pneumatic force due to the
fluid pressure in the gas chamber. This parameter must be greater than
zero.

### **Cross-sectional area at port B** — Cross-sectional area of the inlet of the gas chamber `1e-3 m^2` (default) | positive scalar in units of area

Area normal to the direction of flow at the entrance to the gas
chamber. The cross-sectional area at the entrance can differ from that
in the body of the chamber. Set the two cross-sectional areas to
different values to model the effects of a sudden area change at the
inlet. This parameter must be greater than zero.

### **Dead volume in chamber B** — Fluid volume in the gas chamber in the bottomed-out state `1e-4 m^3` (default) | positive scalar in units of volume

Gas volume remaining in the gas chamber when the piston is pressed
against the hard stop closest to the gas inlet. The dead volume enables
the block to capture the internal states of the gas volume—its
pressure and temperature—when this volume is at a minimum. This
parameter must be greater than zero.

### **Initial gas pressure in chamber B (absolute)** — Absolute pressure inside the gas chamber at the start of simulation `0.101325 MPa` (default) | scalar in units of pressure

Pressure inside the gas chamber at simulation time zero relative to
absolute zero. This pressure helps set the initial state of the gas
volume.

### **Initial gas temperature in chamber B** — Temperature in the gas chamber at the start of simulation `293.15 K` (default) | scalar in units of temperature

Average temperature inside the gas chamber at the start of simulation.
This parameter helps set the initial states of the gas volume.

### **Environment pressure specification** — Choice of atmospheric or custom environment pressure for the gas side `Atmospheric pressure` (default) | `Specified pressure`

Option to set the environment pressure of the gas chamber to the
typical value of one earth atmosphere or to a custom value. Selecting
`Specified pressure` exposes an additional
parameter, **Environment pressure**, that you use to
specify a custom pressure.

### **Environment pressure** — Absolute pressure of the environment outside the gas chamber `0.101325 MPa` (default) | scalar in units of pressure

Pressure outside the gas chamber relative to absolute zero. This
pressure acts against the pressure inside the gas chamber. A pressure of
zero corresponds to a perfect vacuum.

#### Dependencies

This parameter is enabled when the **Environment pressure
specification** is set to `Specified
pressure`.

### Hard Stop

### **Hard stop model** — Select the hard stop model `Stiffness and damping applied smoothly through transition region, damped rebound` (default) | `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

Model choice for the force on the piston at full extension or full
retraction. See the Translational Hard Stop block for more
information.

### **Hard-stop stiffness coefficient** — Stiffness coefficient `1e6` `N/m` (default) | positive scalar

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

## Libraries

Simscape / Fluids / Thermal Liquid / Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2023a: New hard stop parameterization option

The block has a new option for the **Hard stop model** parameter.
This option, called `Based on coefficient of restitution`,
models the hard stop by using a mode chart.

## Description

Linear actuator with opposing thermal liquid and gas chambers

The Double-Acting Actuator (TL-G) block models a linear actuator with
opposing chambers of thermal liquid and gas. The chambers can be individually
pressurized to power the actuator in both extension and retraction strokes. A piston
between the chambers converts the pressure difference across them into actuation
force.

The figure maps the conserving ports of the block to the actuator parts. Ports
**A** and **B** are the inlets of the thermal
liquid and gas chambers. Ports **R** and **C** are the
translating piston and case. The chambers can exchange heat with the environment and are
fitted for this purpose with ports **HA** and **HB**.
The piston is perfectly insulating. The thermal liquid and gas chambers do not exchange
heat with each other.

The sign of the piston displacement relative to the case depends on the mechanical
orientation of the actuator. Use the **Mechanical orientation**
parameter to specify this setting. If the mechanical orientation is positive, the piston
displacement is positive when the pressure is highest in the thermal liquid chamber
(port **A**). If the mechanical orientation is negative, the piston
displacement (under the same pressure conditions) is negative.

Use port **P** to output the instantaneous piston position. The
measurement is absolute (relative to zero). Hard stops limit the motion of the piston to
the length of the case. The stops are modeled as spring-dampers, with spring and damping
coefficients to capture material compliance. One is located at the bottom of the piston
stroke and the other at the top:

- If the **Mechanical orientation** setting is
  `Positive`, the bottom stop is at zero, and the
  top stop is at a distance equal to the piston stroke.
- If the **Mechanical orientation** setting is
  `Negative`, the top stop is at zero, and the
  bottom stop is at a distance equal to the piston stroke.

The block is a composite component built from Simscape™ Foundation blocks. For more information on how the Double-Acting
Actuator (TL-G) block works, see the reference pages of the constituent blocks:

- Translational Mechanical Converter
  (TL)
- Translational Mechanical Converter
  (G)
- Translational Hard
  Stop
- Ideal Translational Motion
  Sensor
