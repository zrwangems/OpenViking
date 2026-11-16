---
type: simulink-block
title: 'Double-Acting Actuator (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Actuators'
documentation_page: 'doubleactingactuatortl'
documentation_source_path: 'ref/doubleactingactuatortl.html'
language: en
---

# Double-Acting Actuator (TL)

## Ports

### Input

### **p** — Piston position input, m physical signal

Physical signal input associated with the piston position, in m. Connect this port
to a Simscape
Multibody™ network using a Translational Multibody
Interface block.

#### Dependencies

To enable this port, set **Piston displacement from chamber A
cap** to `Provide input signal from Multibody
joint`.
### Output

### **p** — Piston position, m physical signal

Physical signal port associated with the piston position.

#### Dependencies

To enable this port, set **Piston displacement from chamber A
cap** to `Calculate from velocity of port R relative to port
C`.
### Conserving

### **A** — Chamber A inlet thermal liquid

Thermal liquid conserving port associated with the inlet to chamber A.

### **B** — Chamber B inlet thermal liquid

Thermal liquid conserving port associated with the inlet to chamber B.

### **R** — Actuator piston mechanical translational

Mechanical translational conserving port associated with the actuator
piston.

### **C** — Actuator casing mechanical translational

Mechanical translational conserving port associated with the actuator
casing.

### **HA** — Chamber A heat flow thermal

Thermal conserving port associated with chamber A.

### **HB** — Chamber B heat flow thermal

Thermal conserving port associated with chamber B.

## Parameters

### Actuator

### **Same fluid on both sides** — Option to model same fluid in both chambers `on` (default) | `off`

Whether to model the same fluid in both actuator chambers. If you select this
parameter, the actuator propagates fluid properties through both chambers. Clear this
parameter to model each chamber as a different fluid, where each chamber is connected
to an isolated fluid network.

### **Mechanical orientation** — Piston displacement direction `Pressure at A causes positive displacement of R relative to C` (default) | `Pressure at A causes negative displacement of R relative to C`

Piston displacement direction. When you set this parameter to:

- `Pressure at A causes positive displacement of R relative to
  C`, the piston displacement is positive when the volume of liquid
  at port **A** is expanding. This motion corresponds to rod
  extension.
- `Pressure at A causes negative displacement of R relative to
  C`, the piston displacement is negative when the volume of liquid
  at port **A** is expanding. This motion corresponds to rod
  contraction.

### **Piston cross-sectional area in chamber A** — Chamber A piston area `0.01 m^2` (default) | positive scalar

Cross-sectional area of the piston rod on the chamber A side.

### **Piston cross-sectional area in chamber B** — Chamber B piston area `0.01 m^2` (default) | positive scalar

Cross-sectional area of the piston rod on the chamber B side.

### **Piston stroke** — Maximum piston travel distance `0.1 m` (default) | positive scalar

Maximum piston travel distance.

### **Dead volume in chamber A** — Chamber A fluid volume at full piston retraction `1e-5 m^3` (default) | positive scalar

Volume of liquid when the piston displacement is `0` in chamber
A. This parameter is the liquid volume when the piston is against the actuator end
cap.

### **Dead volume in chamber B** — Chamber B fluid volume at full piston retraction `1e-5 m^3` (default) | positive scalar

Volume of liquid when the piston displacement is `0` in chamber
B. This parameter is the liquid volume when the piston is against the actuator end
cap.

### **Environment pressure specification** — Reference environment pressure `Atmospheric pressure` (default) | `Specified pressure`

Environment reference pressure. The `Atmospheric
pressure` option sets the environmental pressure to 0.101325 MPa.

### **Environment pressure** — User-defined environmental pressure `0.101325 MPa` (default) | positive scalar

User-defined environmental pressure.

#### Dependencies

To enable this parameter, set **Environment pressure
specification** to `Specified pressure`.

### Hard Stop

### **Hard stop model** — Hard stop model `Stiffness and damping applied smoothly through transition region, damped rebound` (default) | `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

Hard stop model to use when the piston is at full extension or full extraction.
See the Translational Hard Stop block for more information.

### **Hard-stop stiffness coefficient** — Stiffness coefficient `1e10` `N/m` (default) | positive scalar

Piston stiffness coefficient.

#### Dependencies

To enable this parameter, set **Hard stop model** to one of
these settings:

- `Stiffness and damping applied smoothly through transition
  region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped
  rebound`
- `Full stiffness and damping applied at bounds, damped
  rebound`

### **Hard-stop damping coefficient** — Damping coefficient `150` `N*s/m` (default) | positive scalar

Piston damping coefficient.

#### Dependencies

To enable this parameter, set **Hard stop model** to one of
these settings:

- `Stiffness and damping applied smoothly through transition
  region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped
  rebound`
- `Full stiffness and damping applied at bounds, damped
  rebound`

### **Transition region** — Application range of hard stop force model `0.1` `mm` (default) | positive scalar

Application range of the hard stop force model. The block does not apply the hard
stop model when the maximum extension or retraction of the piston is outside of this
range. In this situation, there is no additional force on the piston.

#### Dependencies

To enable this parameter, set **Hard stop model** to
`Stiffness and damping applied smoothly through transition region,
damped rebound`.

### **Coefficient of restitution** — Ratio of final-to-initial relative speed between slider and stop after collision `0.7` (default) | unitless value between 0 and 1

Ratio of the final to the initial relative speed between the slider and the stop
after the slider bounces.

#### Dependencies

To enable this parameter, set **Hard stop model** to
`Based on coefficient of restitution`.

### **Static contact speed threshold** — Threshold relative speed between slider and stop before collision `0.001 m/s` (default) | nonnegative scalar

Threshold relative speed between the slider and stop before collision. When the
slider hits the case with a speed less than the value of the **Static contact
speed threshold** parameter, they stay in contact. Otherwise, the slider
bounces. To avoid modeling static contact between the slider and the case, set this
parameter to `0`.

#### Dependencies

To enable this parameter, set **Hard stop model** to
`Based on coefficient of restitution`.

### **Static contact release force threshold** — Force needed to transition from contact mode to free mode `0.001 N` (default) | positive scalar

Minimum force needed to release the slider from a static contact mode.

#### Dependencies

To enable this parameter, set **Hard stop model** to
`Based on coefficient of restitution`.

### Cushion A

### **Cylinder A end cushioning** — Whether to model piston slow-down at maximum extension `off` (default) | `on`

Whether to model piston slow-down at the maximum extension. See the Cylinder Cushion
(TL) block for more information.

### **Cushion plunger cross-sectional area** — Cylinder cushion plunger area `1e-4 m^2` (default) | positive scalar

Area of the plunger inside the actuator cushion element.

#### Dependencies

To enable this parameter, select **Cylinder A end
cushioning**.

### **Cushion plunger length** — Length of cushion plunger `1e-3 m` (default) | positive scalar

Length of the cushion plunger.

#### Dependencies

To enable this parameter, select **Cylinder A end
cushioning**.

### **Cushion orifice area** — Area of orifice between cushion chambers `1e-6 m^2` (default) | positive scalar

Area of the orifice between the cushion chambers.

#### Dependencies

To enable this parameter, select **Cylinder A end
cushioning**.

### **Leakage area between plunger and cushion sleeve** — Gap between cushion plunger and sleeve `1e-7 m^2` (default) | positive scalar

Gap area between the cushion plunger and sleeve. This value contributes to
numerical stability by maintaining continuity in the flow.

#### Dependencies

To enable this parameter, select **Cylinder A end
cushioning**.

### **Check valve cracking pressure differential** — Cushion threshold pressure `0.01 MPa` (default) | positive scalar

Pressure beyond which the valve operation triggers. When the pressure difference
between port **A** and *Penv*
meets or exceeds the value of this parameter, the cushion valve begins to open.

#### Dependencies

To enable this parameter, select **Cylinder A end
cushioning**.

### **Check valve maximum pressure differential** — Maximum cushion differential pressure `0.1 MPa` (default) | positive scalar

Maximum cushion valve differential pressure. This parameter provides an upper
limit to the pressure so that system pressures remain realistic.

#### Dependencies

To enable this parameter, select **Cylinder A end
cushioning**.

### **Check valve maximum area** — Area of fully opened cushion valve `1e-4 m^2` (default) | positive scalar

Cross-sectional area of the cushion valve in the fully open position.

#### Dependencies

To enable this parameter, select **Cylinder A end
cushioning**.

### **Check valve leakage area** — Cushion valve gap area in fully closed position `1e-10 m^2` (default) | positive scalar

Sum of all gaps when the cushion check valve is in the fully closed position. Any
area smaller than this value saturates to the specified leakage area. This value
contributes to numerical stability by maintaining continuity in the flow.

#### Dependencies

To enable this parameter, select **Cylinder A end
cushioning**.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar

Continuous smoothing factor that introduces a layer of gradual change to the flow
response when the variable orifice and check valve are in near-open or near-closed
positions. Set this value to a nonzero value less than one to increase the stability
of your simulation in these regimes.

#### Dependencies

To enable this parameter, select **Cylinder A end
cushioning**.

### Cushion B

### **Cylinder B end cushioning** — Whether to model piston slow-down at maximum extension `off` (default) | `on`

Whether to model piston slow-down at the maximum extension. See the Cylinder Cushion
(TL) block for more information.

### **Cushion plunger cross-sectional area** — Cylinder cushion plunger area `1e-4 m^2` (default) | positive scalar

Area of the plunger inside the actuator cushion element.

#### Dependencies

To enable this parameter, select **Cylinder B end
cushioning**.

### **Cushion plunger length** — Length of cushion plunger `1e-3 m` (default) | positive scalar

Length of the cushion plunger.

#### Dependencies

To enable this parameter, select **Cylinder B end
cushioning**.

### **Cushion orifice area** — Area of orifice between cushion chambers `1e-6 m^2` (default) | positive scalar

Area of the orifice between the cushion chambers.

#### Dependencies

To enable this parameter, select **Cylinder B end
cushioning**.

### **Leakage area between plunger and cushion sleeve** — Gap between cushion plunger and sleeve `1e-7 m^2` (default) | positive scalar

Gap area between the cushion plunger and sleeve. This value contributes to
numerical stability by maintaining continuity in the flow.

#### Dependencies

To enable this parameter, select **Cylinder B end
cushioning**.

### **Check valve cracking pressure differential** — Cushion threshold pressure `0.01 MPa` (default) | positive scalar

Pressure beyond which the valve operation triggers. When the pressure difference
between port **A** and *P*env
meets or exceeds the value of this parameter, the cushion valve begins to open.

#### Dependencies

To enable this parameter, select **Cylinder B end
cushioning**.

### **Check valve maximum pressure differential** — Maximum cushion differential pressure `0.1 MPa` (default) | positive scalar

Maximum cushion valve differential pressure. This parameter provides an upper
limit to the pressure so that system pressures remain realistic.

#### Dependencies

To enable this parameter, select **Cylinder B end
cushioning**.

### **Check valve maximum area** — Area of fully opened cushion valve `1e-4 m^2` (default) | positive scalar

Cross-sectional area of the cushion valve in the fully open position.

#### Dependencies

To enable this parameter, select **Cylinder B end
cushioning**.

### **Check valve leakage area** — Cushion valve gap area in fully closed position `1e-10 m^2` (default) | positive scalar

Sum of all gaps when the cushion check valve is in the fully closed position. Any
area smaller than this value saturates to the specified leakage area. This value
contributes to numerical stability by maintaining continuity in the flow.

#### Dependencies

To enable this parameter, select **Cylinder B end
cushioning**.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar

Continuous smoothing factor that introduces a layer of gradual change to the flow
response when the variable orifice and check valve are in near-open or near-closed
positions. Set this value to a nonzero value less than one to increase the stability
of your simulation in these regimes.

#### Dependencies

To enable this parameter, select **Cylinder B end
cushioning**.

### Friction

### **Cylinder friction** — Whether to model friction against piston motion `off` (default) | `on`

Whether to model friction against piston motion. The block accounts for Coulomb,
Stribeck, and viscous friction. See the Cylinder Friction
(TL) block for more information.

### **Breakaway to Coulomb friction force ratio** — Ratio of breakaway force to Coulomb friction force `1.2` (default) | positive scalar

Ratio of the breakaway force to the Coulomb friction force.

#### Dependencies

To enable this parameter, select **Cylinder friction**.

### **Breakaway friction velocity** — Threshold for motion `0.1` `m/s` (default) | positive scalar

Threshold velocity for the motion against the friction force to begin.

#### Dependencies

To enable this parameter, select **Cylinder friction**.

### **Preload force** — Initial force on cylinder `20 N` (default) | scalar

Force on the cylinder when it is in the neutral position.

#### Dependencies

To enable this parameter, select **Cylinder friction**.

### **Coulomb friction force coefficient** — Coulomb friction force coefficient `1e-6 N/Pa` (default) | positive scalar

Coulomb force coefficient of friction.

#### Dependencies

To enable this parameter, select **Cylinder friction**.

### **Viscous friction coefficient** — Viscous friction coefficient `100 N*s/m` (default) | positive scalar

Viscous friction coefficient.

#### Dependencies

To enable this parameter, select **Cylinder friction**.

### Initial Conditions

### **Piston displacement from chamber A cap** — Method for determining piston position `Calculate from velocity of port R relative to port C` (default) | `Provide input signal from Multibody joint`

Method for determining the piston position. The block can receive the position
from a Multibody block when set to `Provide input signal from Multibody
joint`, or can calculate the position internally and report the
position at port **p**. The position is between `0`
and the value of the **Piston stroke** parameter when the mechanical
orientation is positive and between `0` and the negative value of the
**Piston stroke** parameter when the mechanical orientation is
negative.

### **Initial piston displacement from chamber A cap** — Piston position at start of simulation `0` `m` (default) | scalar

Piston position at the start of the simulation.

#### Dependencies

To enable this parameter, set **Piston displacement** to
`Calculate from velocity of port R relative to port
C`.

### **Enable dynamic compressibility** — Whether to model fluid compressibility `on` (default) | `off`

Whether to model any change in fluid density due to fluid compressibility. When
you select **Fluid compressibility**, changes due to the mass flow
rate into the block are calculated in addition to density changes due to changes in
pressure. In the Isothermal Liquid Library, all blocks calculate density as a function
of pressure.

### **Initial liquid temperature in chamber A** — Starting liquid temperature in chamber A `293.15` `K` (default) | scalar

Initial temperature of the liquid volume in the actuator.

### **Initial liquid temperature in chamber B** — Starting liquid temperature in chamber B `293.15` `K` (default) | scalar

Initial temperature of the liquid volume in the actuator.

### **Initial liquid pressure in chamber A** — Starting liquid pressure in chamber A for compressible fluids `0.101325` `MPa` (default) | positive scalar

Starting liquid pressure for compressible fluids.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.

### **Initial liquid pressure in chamber B** — Starting liquid pressure in chamber B for compressible fluids `0.101325` `MPa` (default) | positive scalar

Starting liquid pressure for compressible fluids.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.

### **Nominal liquid pressure in chamber A** — Pressure at nominal operating conditions in chamber A `0.101325 MPa` (default) | scalar

Liquid pressure at nominal operating conditions in chamber A. The block uses this
value to calculate the nominal density to use in the mass conservation equation when
dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** checkbox.

### **Nominal liquid pressure in chamber B** — Pressure at nominal operating conditions in chamber B `0.101325 MPa` (default) | scalar

Liquid pressure at nominal operating conditions in chamber B. The block uses this
value to calculate the nominal density to use in the mass conservation equation when
dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** checkbox.

### **Nominal liquid temperature in chamber A** — Temperature at nominal operating conditions in chamber A `293.15` `K` (default) | scalar

Liquid temperature at nominal operating conditions in chamber A. The block uses
this value to calculate the nominal density to use in the mass conservation equation
when dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** checkbox.

### **Nominal liquid temperature in chamber B** — Temperature at nominal operating conditions in chamber B `293.15` `K` (default) | scalar

Liquid temperature at nominal operating conditions in chamber B. The block uses
this value to calculate the nominal density to use in the mass conservation equation
when dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** checkbox.

## Libraries

Simscape / Fluids / Thermal Liquid / Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

### R2024a: Model different fluids on each side of the actuator

Clear the new **Same fluid on both sides** parameter to block the
propagation of fluid properties and model each chamber as a different fluid connected to its
own isolated fluid network.

### R2023b: Model cylinder friction or cushion

The block has a new options for modeling cylinder friction or cushion. Select the
**Cylinder friction effect** parameter to include the effects of friction
on the piston motion. Select the **Cylinder A end cushioning** or
**Cylinder B end cushioning** parameters to model piston slowdown at
maximum extension in either cylinder.

### R2023a: New hard stop parameterization option

The block has a new option for the **Hard stop model** parameter. This
option, called `Based on coefficient of restitution`, models the
hard stop by using a mode chart.

## Description

Double-acting linear actuator in a thermal liquid network

The Double-Acting Actuator (TL) block models a linear actuator with a
piston controlled by two opposing thermal liquid chambers. The actuator generates force in the
extension and retraction strokes. The generated force depends on the pressure difference
between the two chambers.

The figure shows the key components of the actuator. Ports **A** and
**B** represent the thermal liquid chamber inlets. Port
**R** represents the translating actuator piston and port
**C** represents the actuator case. Ports **HA** and
**HB** represent the thermal interfaces between each chamber and the
environment. The moving piston is adiabatic.

Double-Acting Actuator Schematic

### Displacement

The block measures the piston displacement as the position at port
**R** relative to port **C**. The **Mechanical
orientation** parameter identifies the direction of piston displacement. The
piston displacement is neutral, or `0`, when the chamber A volume is equal
to the value of the **Dead volume in chamber A** parameter. When the
**Piston displacement from chamber A cap** parameter is
`Provide input signal from Multibody joint`, you input the piston
displacement using port **p**. You can ensure that the derivative of the
position signal is equal to the piston velocity by using a Translational Multibody Interface block to provide the
piston displacement.

The direction of the piston motion depends on the **Mechanical
orientation** parameter. If the mechanical orientation is positive, then the
piston translation is positive in relation to the actuator case when the gauge pressure at
port **A** is positive. The direction of motion reverses when the
mechanical orientation is negative.

### Hard Stop

A set of hard stops limit the piston range of motion. The block uses an implementation
of the Translational Hard Stop block, which treats hard stops like spring-damper
systems. The spring stiffness coefficient controls the restorative component of the
hard-stop contact force and the damping coefficient the dissipative component.

The hard stops are located at the distal ends of the piston stroke. If the mechanical
orientation is positive, then the lower hard stop is at *x* = 0, and the upper hard stop is at *x* = +*stroke*. If the mechanical orientation is negative, then the lower hard stop is at *x* = -*stroke*, and the upper hard stop is at *x* = 0.

### Cushion

The block can model cushioning toward the extremes of the piston stroke. Select
**Cylinder end cushioning** to slow the piston motion as it approaches
the maximum extension, defined by the **Piston stroke** parameter. For more
information on the functionality of a cylinder cushion, see the Cylinder Cushion
(TL) block.

### Friction

The block can model friction against piston motion. When you select **Cylinder
friction**, the resulting friction is a combination of the Stribeck, Coulomb, and
viscous effects. The block measures the pressure difference between the chamber pressure and
the environment pressure. For more information on the friction model and its limitations,
see the Cylinder Friction
(TL) block.

### Block Composite

This block is a composite component based on these Simscape™ Foundation blocks:

- Translational Mechanical Converter
  (TL)
- Translational Hard Stop
- Ideal Translational Motion Sensor

Diagram of elements that make up the block.

If you select **Cylinder friction**, **Cylinder A end
cushioning**, or **Cylinder B end cushioning**, the block
composite also includes the Cylinder Friction
(TL) block or two Cylinder Cushion
(TL) blocks.

Diagram of elements that make up the block with friction and cushion.
