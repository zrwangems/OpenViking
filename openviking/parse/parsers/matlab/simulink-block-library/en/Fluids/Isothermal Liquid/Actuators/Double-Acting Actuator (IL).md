---
type: simulink-block
title: 'Double-Acting Actuator (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Actuators'
documentation_page: 'doubleactingactuatoril'
documentation_source_path: 'ref/doubleactingactuatoril.html'
language: en
---

# Double-Acting Actuator (IL)

## Ports

### Input

### **p** — Piston position input, m physical signal

Physical signal input port associated with the piston position that
you specify using a Simscape
Multibody block.

#### Dependencies

To expose this port, set **Piston displacement from
chamber A cap** to `Provide input signal
from Multibody joint`.
### Output

### **p** — Piston position output, m physical signal

Physical signal port associated with the piston position.

#### Dependencies

To expose this port, set **Piston displacement from
chamber A cap** to `Calculate from velocity
of port R relative to port C`.
### Conserving

### **A** — Inlet to chamber A isothermal liquid

Isothermal liquid conserving port associated with the inlet to chamber
A.

### **B** — Inlet to chamber B isothermal liquid

Isothermal liquid conserving port associated with the inlet to chamber
B.

### **C** — Actuator casing mechanical translational

Mechanical translational conserving port associated with the case.

### **R** — Actuator piston mechanical translational

Mechanical translational conserving port associated with the
piston.

## Parameters

### Actuator

### **Same fluid on both sides** — Option to model same fluid in both chambers `on` (default) | `off`

Whether to model the same fluid in both actuator chambers. If you
select this parameter, the actuator propagates fluid properties through
both chambers. Clear this parameter to model each chamber as a different
fluid, where each chamber is connected to an isolated fluid network.

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

### **Piston cross-sectional area in chamber A** — Chamber A piston area `0.01 m^2` (default) | positive scalar

Cross-sectional area of the piston rod on the chamber A side.

### **Piston cross-sectional area in chamber B** — Chamber B piston area `0.01 m^2` (default) | positive scalar

Cross-sectional area of the piston rod on the chamber B side.

### **Piston stroke** — Maximum piston travel distance `0.1 m` (default) | positive scalar

Maximum piston travel distance.

### **Dead volume in chamber A** — Chamber A fluid volume at full piston retraction `1e-5 m^3` (default) | positive scalar

Volume of liquid when the piston displacement is `0`
in chamber A. This is the liquid volume when the piston is up against
the actuator end cap.

### **Dead volume in chamber B** — Chamber B fluid volume at full piston retraction `1e-5 m^3` (default) | positive scalar

Volume of liquid when the piston displacement is `0`
in chamber B. This is the liquid volume when the piston is up against
the actuator end cap.

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

### **Breakaway to Coulomb friction force ratio** — Ratio of breakaway force to Coulomb friction force `1.2` (default) | positive scalar

Ratio of the breakaway force to the Coulomb friction force.

#### Dependencies

To enable this parameter, in the **Friction** tab, select
**Cylinder friction effect**.

### **Breakaway friction velocity** — Threshold for motion `0.1 m/s` (default) | positive scalar

Threshold velocity for motion against friction force to begin.

#### Dependencies

To enable this parameter, in the **Friction**
tab, select **Cylinder friction effect**.

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

### Converter Cushion A

### **Cylinder A end cushioning** — Whether to model piston slow-down at maximum extension `off` (default) | `on`

Whether to model piston slow-down at the maximum extension. See the Cylinder Cushion (IL)
block for more information.

### **Cushion plunger cross-sectional area** — Cylinder cushion plunger area `1e-4 m^2` (default) | positive scalar

Area of the plunger inside the actuator cushion element.

#### Dependencies

To enable this parameter, select **Cylinder A end cushioning**.

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

Gap area between the cushion plunger and sleeve. This value
contributes to numerical stability by maintaining continuity in the
flow.

#### Dependencies

To enable this parameter, select **Cylinder A end
cushioning**.

### **Check valve cracking pressure differential** — Cushion threshold pressure `0.01 MPa` (default) | positive scalar

Pressure beyond which the valve operation triggers. When the pressure difference between
port **A** and
*P*env meets or exceeds the
value of this parameter, the cushion valve begins to open.

#### Dependencies

To enable this parameter, select **Cylinder A end
cushioning**.

### **Check valve maximum pressure differential** — Maximum cushion differential pressure `0.1 MPa` (default) | positive scalar

Maximum cushion valve differential pressure. This parameter provides
an upper limit to the pressure so that system pressures remain
realistic.

#### Dependencies

To enable this parameter, select **Cylinder A end
cushioning**.

### **Check valve maximum area** — Area of fully opened cushion valve `1e-4 m^2` (default) | positive scalar

Cross-sectional area of the cushion valve in the fully open position.

#### Dependencies

To enable this parameter, select **Cylinder A end
cushioning**.

### **Check valve leakage area** — Cushion valve gap area in fully closed position `1e-10 m^2` (default) | positive scalar

Sum of all gaps when the cushion check valve is in the fully closed
position. Any area smaller than this value saturates to the specified
leakage area. This value contributes to numerical stability by
maintaining continuity in the flow.

#### Dependencies

To enable this parameter, select **Cylinder A end
cushioning**.

### Converter Cushion B

### **Cylinder B end cushioning** — Whether to model piston slow-down at maximum extension `off` (default) | `on`

Whether to model piston slow-down at the maximum extension. See the Cylinder Cushion (IL)
block for more information.

### **Cushion plunger cross-sectional area** — Cylinder cushion plunger area `1e-4 m^2` (default) | positive scalar

Area of the plunger inside the actuator cushion element.

#### Dependencies

To enable this parameter, select **Cylinder B end cushioning**.

### **Cushion plunger length** — Length of cushion plunger `1e-3 m` (default) | positive scalar

Length of the cushion plunger.

#### Dependencies

To enable this parameter, select **Cylinder B end cushioning**.

### **Cushion orifice area** — Area of orifice between cushion chambers `1e-6 m^2` (default) | positive scalar

Area of the orifice between the cushion chambers.

#### Dependencies

To enable this parameter, select **Cylinder B end
cushioning**.

### **Leakage area between plunger and cushion sleeve** — Gap between cushion plunger and sleeve `1e-7 m^2` (default) | positive scalar

Gap area between the cushion plunger and sleeve. This value
contributes to numerical stability by maintaining continuity in the
flow.

#### Dependencies

To enable this parameter, select **Cylinder B end
cushioning**.

### **Check valve cracking pressure differential** — Cushion threshold pressure `0.01 MPa` (default) | positive scalar

Pressure beyond which the valve operation triggers. When the pressure difference between
port **A** and
*P*env meets or exceeds the
value of this parameter, the cushion valve begins to open.

#### Dependencies

To enable this parameter, select **Cylinder B end
cushioning**.

### **Check valve maximum pressure differential** — Maximum cushion differential pressure `0.1 MPa` (default) | positive scalar

Maximum cushion valve differential pressure. This parameter provides
an upper limit to the pressure so that system pressures remain
realistic.

#### Dependencies

To enable this parameter, select **Cylinder B end
cushioning**.

### **Check valve maximum area** — Area of fully opened cushion valve `1e-4 m^2` (default) | positive scalar

Cross-sectional area of the cushion valve in the fully open position.

#### Dependencies

To enable this parameter, select **Cylinder B end
cushioning**.

### **Check valve leakage area** — Cushion valve gap area in fully closed position `1e-10 m^2` (default) | positive scalar

Sum of all gaps when the cushion check valve is in the fully closed
position. Any area smaller than this value saturates to the specified
leakage area. This value contributes to numerical stability by
maintaining continuity in the flow.

#### Dependencies

To enable this parameter, select **Cylinder B end
cushioning**.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar

Continuous smoothing factor that introduces a layer of gradual change
to the flow response when the variable orifice and check valve are in
near-open or near-closed positions. Set this value to a nonzero value
less than one to increase the stability of your simulation in these
regimes.

#### Dependencies

To enable this parameter, select **Cylinder B end
cushioning**.

### Friction

### **Cylinder friction effect** — Whether to model friction against piston motion `off` (default) | `on`

Whether to model friction against piston motion. The block accounts for Coulomb,
Stribeck, and viscous friction. See the Cylinder Friction block for more
information.

### **Breakaway to Coulomb friction force ratio** — Ratio of breakaway force to Coulomb friction force `1.2` (default) | positive scalar

Ratio of the breakaway force to the Coulomb friction force.

#### Dependencies

To enable this parameter, select **Cylinder
friction**.

### **Breakaway friction velocity** — Threshold for motion `0.1` `m/s` (default) | positive scalar

Threshold velocity for the motion against the friction force to
begin.

#### Dependencies

To enable this parameter, select **Cylinder
friction**.

### **Preload force** — Initial force on cylinder `20 N` (default) | scalar

Force on the cylinder when it is in the neutral position.

#### Dependencies

To enable this parameter, select **Cylinder friction effect**.

### **Coulomb friction force coefficient** — Coulomb friction force coefficient `1e-6 N/Pa` (default) | positive scalar

Coulomb force coefficient of friction.

#### Dependencies

To enable this parameter, select **Cylinder friction
effect**.

### **Viscous friction coefficient** — Viscous friction coefficient `100 N/(m/s)` (default) | positive scalar

Viscous friction coefficient.

#### Dependencies

To enable this parameter, select **Cylinder friction
effect**.

### Leakage

### **Internal leakage** — Whether to model annular leakage `off` (default) | `on`

Whether to model annular leakage between the fluid chamber and the
piston reservoir at reference environment conditions. The leakage is
considered laminar. See the Laminar Leakage (IL)
block for more information.

#### Dependencies

To enable this parameter, select **Same fluid on both
sides**.

### **Piston-cylinder clearance** — Radial clearance `1e-4 m` (default) | positive scalar

Radial distance between the piston rod and cylinder casing.

#### Dependencies

To enable this parameter, select **Same fluid on both sides** and
**Internal leakage**.

### **Piston head length** — Annular length of piston mounting `0.01 m` (default) | positive scalar

Length of the piston head.

#### Dependencies

To enable this parameter, select **Same fluid on both
sides** and **Internal
leakage**.

### Initial Conditions

### **Piston displacement from chamber A cap** — Method for determining piston position `Calculate from velocity of port R relative to port C` (default) | `Provide input signal from Multibody joint`

Method for determining the piston position. The block can receive the position from a
Multibody block when set to `Provide input signal from
Multibody joint`, or calculates the position internally
and reports the position at port **p**. The position is
between `0` and the **Piston stroke**
when the mechanical orientation is positive and `0` and
–**Piston stroke** when the mechanical orientation
is negative.

### **Initial piston displacement from chamber A cap** — Piston position measured from chamber A cap at start of simulation `0 m` (default) | scalar

Piston position with respect to the chamber A cap at the start of the
simulation.

#### Dependencies

To enable this parameter, set **Piston displacement from
chamber A cap** to `Calculate from velocity
of port R relative to port C`.

### **Enable dynamic compressibility** — Whether to model fluid compressibility `on` (default) | `off`

Whether to model any change in fluid density due to fluid
compressibility. When you select **Enable dynamic
compressibility**, changes due to the mass flow rate into
the block are calculated in addition to density changes due to changes
in pressure. In the Isothermal Liquid Library, all blocks calculate
density as a function of pressure.

### **Initial liquid pressure in chamber A** — Starting liquid pressure in chamber A `0.101325 MPa` (default) | positive scalar

Starting liquid pressure for compressible fluids.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.

### **Initial liquid pressure in chamber B** — Starting liquid pressure in chamber B `0.101325 MPa` (default) | positive scalar

Starting liquid pressure for compressible fluids.

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

### **Nominal liquid pressure in chamber B** — Pressure at nominal operating conditions in chamber B `0.101325 MPa` (default) | scalar

Liquid pressure at nominal operating conditions in chamber B. The
block uses this value to calculate the nominal density to use in the
mass conservation equation when dynamic compressibility is
disabled.

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

### R2024a: Model different fluids on each side of the actuator

Clear the new **Same fluid on both sides** parameter to block
the propagation of fluid properties and model each chamber as a different fluid
connected to its own isolated fluid network.

### R2023a: New hard stop parameterization option

The block has a new option for the **Hard stop model** parameter.
This option, called `Based on coefficient of restitution`,
models the hard stop by using a mode chart.

## Description

Linear conversion of pressure differential to actuation in an isothermal liquid system

The Double-Acting Actuator (IL) block represents the linear
conversion of a pressure differential between two chambers to piston motion. The piston
actuation is controlled by the pressure differential acting on the piston plate that
separates the chambers. The motion of the piston when it is near full extension or full
retraction is limited by one of four hard stop models. Fluid compressibility is
optionally modeled in both piston chambers.

Ports **A** and **B** are isothermal liquid inlets. Port
**C** represents the actuator casing, while piston velocity is
returned at port **R**. When the piston position is calculated
internally, it is reported at port **p**, and when the position is set
by a connection to a Simscape™
Multibody™ joint, it is received as a physical signal at port
**p**.

You can define the piston displacement direction with the **Mechanical
orientation** parameter. If the mechanical orientation is set to
`Pressure at A causes positive displacement of R relative to
C`, the piston extends when the pressure differential
*p*A –
*p*B is positive. If **Mechanical
orientation** is set to `Pressure at A causes negative
displacement of R relative to C`, the piston retracts for a positive
pressure difference between the liquid and gas chambers.

### Displacement

The piston displacement is measured as the position at port **R** relative
to port **C**. The **Mechanical orientation**
identifies the direction of piston displacement. The piston displacement is neutral,
or `0`, when the chamber A volume is equal to the chamber dead
volume. When displacement is received as an input, ensure that the derivative of the
position is equal to the piston velocity. This is automatically the case when the
input is received from a Translational Multibody Interface block
connection to a Simscape Multibody joint.

### Hard Stop Model

To avoid mechanical damage to an actuator when it is fully extended or fully retracted, an
actuator typically displays nonlinear behavior when the piston approaches these
limits. The Double-Acting Actuator (IL) block models this behavior with a choice of
four hard stop models, which model the material compliance through a spring-damper
system. The hard stop models are:

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

### Cushion

The block can model cushioning toward the extremes of the piston stroke. Select
**Cylinder end cushioning** to slow the piston motion as it
approaches the maximum extension, defined by the **Piston stroke**
parameter. For more information on the functionality of a cylinder cushion, see the
Cylinder Cushion (IL) block.

### Friction

The block can model friction against piston motion. When you select
**Cylinder friction**, the resulting friction is a combination
of the Stribeck, Coulomb, and viscous effects. The block measures the pressure
difference between the chamber pressure and the environment pressure. For more
information on the friction model and its limitations, see the Cylinder Friction
(IL) block.

### Leakage

You can optionally model leakage between the chamber A and chamber B. When the fluid in
both chambers is the same and you select **Internal leakage**,
Poiseuille flow is modeled between the piston and cylinder. This block uses the
Simscape Foundation Library Laminar Leakage (IL) block. The
flow rate is calculated as:

m˙=π128(d04−di4−(d02−di2)2log(d0/di))υL(pA−pB),

where:

- *ν* is the fluid kinematic viscosity.
- *L* is the piston length, **p** –
  *P*0.
- *p*A is the pressure at port
  **A**.
- *p*B is the pressure at port
  **B**.

The cylinder diameter, *d*0,
is d0=di+2c, where *c* is the **Piston-cylinder
clearance**, and the piston diameter,
*d*i, is di=4APπ, where *A*P is the average
of the **Piston cross-sectional area in chamber A** and
**Piston cross-sectional area in chamber B** parameters.

### Numerically-Smoothed Area and Pressure

You can maintain numerical robustness in your
simulation by adjusting the **Smoothing factor** parameter. If
the **Smoothing factor** parameter is nonzero, the block smooths
the cushion A and B orifice areas and the check valve pressure ranges. The orifice
area is smoothly saturated between the cushion A and cushion B **Leakage
area between plunger and cushion sleeve** and **Cushion
plunger cross-sectional area** parameters while the valve pressure is
saturated between the cushion A and cushion B **Check valve cracking
pressure differential** and **Check valve maximum pressure
differential** parameters. For more information, see Numerical Smoothing.

### Block Schematic

The Double-Acting Actuator (IL) block comprises four Simscape Foundation blocks:

- Laminar Leakage (IL)
- Translational Mechanical Converter (IL)
- Translational Hard Stop
- Ideal Translational Motion Sensor

and two Isothermal Liquid library blocks:

- Cylinder Cushion (IL)
- Cylinder Friction (IL)

### Momentum Balance

The momentum conservation equation for the actuator is

F= ε(SApA−SBpB−SRodpenv)

where:

- *F* is the force the liquid exerts on the converter
  interface. This force expression does not account for the force
  contributions due to the hard stop, cylinder cushions, or cylinder
  friction subcomponents. To see those force contributions to the
  converter interface, see the documentation pages for those
  subcomponents.
- *ε* depends on the **Mechanical
  orientation** of the converter. If **Mechanical
  orientation** is `Pressure at A causes
  positive displacement of R relative to C`,
  *ε* `= 1`. If
  **Mechanical orientation** is
  `Pressure at A causes negative displacement of R
  relative to C`, *ε* `=
  -1`.
- *SRod* is the rod
  cross-sectional area whereSRod=SA−SB.
- *SA* is the value of the
  **Piston cross-sectional area in chamber A**
  parameter.
- *SB* is the value of the
  **Piston cross-sectional area in chamber B**
  parameter.
- *pA* is the pressure inside
  chamber A.
- *pB* is the pressure inside
  chamber B.
- *penv* is the environment
  pressure.
