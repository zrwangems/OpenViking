---
type: simulink-block
title: 'Single-Acting Actuator (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Actuators'
documentation_page: 'singleactingactuatoril'
documentation_source_path: 'ref/singleactingactuatoril.html'
language: en
---

# Single-Acting Actuator (IL)

## Ports
```yaml
ports:
- name: p
  summary: Multibody piston position input, m physical signal
  direction: input
- name: p
  summary: Piston position, m physical signal
  direction: output
- name: A
  summary: Liquid port isothermal liquid
  direction: conserving
- name: C
  summary: Actuator casing translational mechanical
  direction: conserving
- name: R
  summary: Actuator piston translational mechanical
  direction: conserving
```

### Input

### **p** — Multibody piston position input, m physical signal

Physical signal input port associated with the piston position, in m.
Connect this port to a Simscape
Multibody block.

#### Dependencies

To enable this port, set **Piston displacement**
to `Provide input signal from Multibody
joint`.
### Output

### **p** — Piston position, m physical signal

Piston position in m, returned as a physical signal.

#### Dependencies

To expose this port, set **Piston displacement**
to `Calculate from velocity of port R relative to port
C`.
### Conserving

### **A** — Liquid port isothermal liquid

Thermal liquid conserving port associated with chamber A.

### **C** — Actuator casing translational mechanical

Translational mechanical conserving port associated with the actuator
casing.

### **R** — Actuator piston translational mechanical

Translational mechanical conserving port associated with the actuator
piston.
## Parameters
```yaml
parameters:
- name: Mechanical orientation
  summary: Piston displacement direction Pressure at A causes positive displacement of R relative to C (default) | Pressure
    at A causes negative displacement of R relative to C
  group: Actuator
- name: Piston cross-sectional area
  summary: Cross-sectional area of piston rod 0.01 m^2 (default) | positive scalar
  group: Actuator
- name: Piston stroke
  summary: Maximum piston travel distance 0.1m (default) | positive scalar
  group: Actuator
- name: Dead volume
  summary: Fluid volume at full piston retraction 1e-5 m^3 (default) | positive scalar
  group: Actuator
- name: Environment pressure specification
  summary: Reference environment pressure Atmospheric pressure (default) | Specified pressure
  group: Actuator
- name: Environment pressure
  summary: User-defined environmental pressure 0.101325 MPa (default) | positive scalar
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
- name: Cylinder end cushioning
  summary: Whether to model piston slow-down at maximum extension off (default) | on
  group: Cushion
- name: Cushion plunger cross-sectional area
  summary: Cylinder cushion plunger area 1e-4 m^2 (default) | positive scalar
  group: Cushion
- name: Cushion plunger length
  summary: Length of cushion plunger 1e-3 m (default) | positive scalar
  group: Cushion
- name: Cushion orifice area
  summary: Area of orifice between cushion chambers 1e-6 m^2 (default) | positive scalar
  group: Cushion
- name: Leakage area between plunger and cushion sleeve
  summary: Gap between cushion plunger and sleeve 1e-7 m^2 (default) | positive scalar
  group: Cushion
- name: Check valve cracking pressure differential
  summary: Cushion threshold pressure 0.01 MPa (default) | positive scalar
  group: Cushion
- name: Check valve maximum pressure differential
  summary: Cushion differential pressure maximum 0.1 MPa (default) | positive scalar
  group: Cushion
- name: Check valve maximum area
  summary: Area of fully opened cushion valve 1e-4 m^2 (default) | positive scalar
  group: Cushion
- name: Check valve leakage area
  summary: Cushion valve gap area in fully closed position 1e-10 m^2 (default) | positive scalar
  group: Cushion
- name: Smoothing factor
  summary: Numerical smoothing factor 0.01 (default) | positive scalar
  group: Cushion
- name: Cylinder friction
  summary: Whether to model friction against piston motion off (default) | on
  group: Friction
- name: Breakaway to Coulomb friction force ratio
  summary: Ratio of breakaway force to Coulomb friction force 1.2 (default) | positive scalar
  group: Friction
- name: Breakaway friction velocity
  summary: Threshold for motion 0.1 m/s (default) | positive scalar
  group: Friction
- name: Preload force
  summary: Initial force in cylinder due to seal assembly 20 N (default) | scalar
  group: Friction
- name: Coulomb friction force coefficient
  summary: Coulomb friction force coefficient 1e-6 N/Pa (default) | positive scalar
  group: Friction
- name: Viscous friction coefficient
  summary: Viscous friction coefficient 100 N*s/m (default) | positive scalar
  group: Friction
- name: Leakage
  summary: Whether to model annular leakage off (default) | on
  group: Leakage
- name: Piston-cylinder clearance
  summary: Radial clearance 1e-4 m (default) | positive scalar
  group: Leakage
- name: Piston head length
  summary: Annular length of piston mounting 0.01 m (default) | positive scalar
  group: Leakage
- name: Piston displacement
  summary: Method for determining piston position Calculate from velocity of port R relative to port C (default) | Provide
    input signal from Multibody joint
  group: Initial conditions
- name: Initial piston displacement
  summary: Piston position at start of simulation 0 m (default) | scalar
  group: Initial conditions
- name: Enable dynamic compressibility
  summary: Whether to model fluid compressibility on (default) | off
  group: Initial conditions
- name: Initial liquid pressure
  summary: Starting liquid pressure for compressible fluids 0.101325 MPa (default) | positive scalar
  group: Initial conditions
- name: Nominal liquid pressure
  summary: Pressure at nominal operating conditions 0.101325 MPa (default) | scalar
  group: Initial conditions
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

### **Piston cross-sectional area** — Cross-sectional area of piston rod `0.01` `m^2` (default) | positive scalar

Cross-sectional area of the piston rod.

### **Piston stroke** — Maximum piston travel distance `0.1``m` (default) | positive scalar

Maximum piston travel distance.

### **Dead volume** — Fluid volume at full piston retraction `1e-5` `m^3` (default) | positive scalar

Volume of liquid when the piston displacement is `0`. This is the
liquid volume when the piston is up against the actuator end cap.

### **Environment pressure specification** — Reference environment pressure `Atmospheric pressure` (default) | `Specified pressure`

Environment reference pressure. The `Atmospheric
pressure` option sets the environmental pressure to
0.101325 MPa.

### **Environment pressure** — User-defined environmental pressure `0.101325` `MPa` (default) | positive scalar

User-defined environmental pressure.

#### Dependencies

To enable this parameter, set **Environment pressure
specification** to `Specified
pressure`.

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

### Cushion

### **Cylinder end cushioning** — Whether to model piston slow-down at maximum extension `off` (default) | `on`

Whether to model piston slow-down at the maximum extension. See the Cylinder Cushion (IL)
block for more information.

### **Cushion plunger cross-sectional area** — Cylinder cushion plunger area `1e-4` `m^2` (default) | positive scalar

Area of the plunger inside the actuator cushion element.

#### Dependencies

To enable this parameter, select **Cylinder end cushioning**.

### **Cushion plunger length** — Length of cushion plunger `1e-3` `m` (default) | positive scalar

Length of the cushion plunger.

#### Dependencies

To enable this parameter, select **Cylinder end
cushioning**.

### **Cushion orifice area** — Area of orifice between cushion chambers `1e-6` `m^2` (default) | positive scalar

Area of the orifice between the cushion chambers.

#### Dependencies

To enable this parameter, select **Cylinder end
cushioning**.

### **Leakage area between plunger and cushion sleeve** — Gap between cushion plunger and sleeve `1e-7` `m^2` (default) | positive scalar

Gap area between the cushion plunger and sleeve. This value
contributes to numerical stability by maintaining continuity in the
flow.

#### Dependencies

To enable this parameter, select **Cylinder end
cushioning**.

### **Check valve cracking pressure differential** — Cushion threshold pressure `0.01` `MPa` (default) | positive scalar

Pressure beyond which the valve operation triggers. When the pressure difference between
port **A** and
*P*env meets or exceeds the
value of this parameter, the cushion valve begins to open.

#### Dependencies

To enable this parameter, select **Cylinder end
cushioning**.

### **Check valve maximum pressure differential** — Cushion differential pressure maximum `0.1` `MPa` (default) | positive scalar

Maximum cushion valve differential pressure. This parameter provides
an upper limit to the pressure so that system pressures remain
realistic.

#### Dependencies

To enable this parameter, select **Cylinder end
cushioning**.

### **Check valve maximum area** — Area of fully opened cushion valve `1e-4` `m^2` (default) | positive scalar

Cross-sectional area of the cushion valve in the fully open position.

#### Dependencies

To enable this parameter, select **Cylinder end
cushioning**.

### **Check valve leakage area** — Cushion valve gap area in fully closed position `1e-10` `m^2` (default) | positive scalar

Sum of all gaps when the cushion check valve is in the fully closed
position. Any area smaller than this value saturates to the specified
leakage area. This value contributes to numerical stability by
maintaining continuity in the flow.

#### Dependencies

To enable this parameter, select **Cylinder end
cushioning**.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar

Continuous smoothing factor that introduces a layer of gradual change
to the flow response when the variable orifice and check valve are in
near-open or near-closed positions. Set this value to a nonzero value
less than one to increase the stability of your simulation in these
regimes.

#### Dependencies

To enable this parameter, select **Cylinder end
cushioning**.

### Friction

### **Cylinder friction** — Whether to model friction against piston motion `off` (default) | `on`

Whether to model friction against piston motion. The block accounts for Coulomb,
Stribeck, and viscous friction. See the Cylinder Friction block for more
information.

### **Breakaway to Coulomb friction force ratio** — Ratio of breakaway force to Coulomb friction force `1.2` (default) | positive scalar

Ratio of the breakaway force to the Coulomb friction force.

#### Dependencies

To enable this parameter, select **Cylinder friction**.

### **Breakaway friction velocity** — Threshold for motion `0.1` `m/s` (default) | positive scalar

Threshold velocity for the motion against the friction force to begin.

#### Dependencies

To enable this parameter, select **Cylinder
friction**.

### **Preload force** — Initial force in cylinder due to seal assembly `20` `N` (default) | scalar

Initial force in the cylinder due to the seal assembly.

#### Dependencies

To enable this parameter, select **Cylinder
friction**.

### **Coulomb friction force coefficient** — Coulomb friction force coefficient `1e-6` `N/Pa` (default) | positive scalar

Coulomb force coefficient of friction.

#### Dependencies

To enable this parameter, select **Cylinder
friction**.

### **Viscous friction coefficient** — Viscous friction coefficient `100` `N*s/m` (default) | positive scalar

Viscous friction coefficient.

#### Dependencies

To enable this parameter, select **Cylinder
friction**.

### Leakage

### **Leakage** — Whether to model annular leakage `off` (default) | `on`

Whether to model annular leakage between the fluid chamber and the
piston reservoir at reference environment conditions. The leakage is
considered laminar. See the Laminar Leakage (IL)
block for more information.

### **Piston-cylinder clearance** — Radial clearance `1e-4` `m` (default) | positive scalar

Radial distance between the piston rod and cylinder casing.

#### Dependencies

To enable this parameter, select **Leakage**.

### **Piston head length** — Annular length of piston mounting `0.01` `m` (default) | positive scalar

Length of the piston head.

#### Dependencies

To enable this parameter, select
**Leakage**.

### Initial conditions

### **Piston displacement** — Method for determining piston position `Calculate from velocity of port R relative to port C` (default) | `Provide input signal from Multibody joint`

Method for determining the piston position. The block can receive the position from a
Multibody block when set to `Provide input signal from
Multibody joint`, or calculates the position internally
and reports the position at port **p**. The position is
between `0` and the **Piston stroke**
when the mechanical orientation is positive and `0` and
–**Piston stroke** when the mechanical orientation
is negative.

### **Initial piston displacement** — Piston position at start of simulation `0` `m` (default) | scalar

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

### **Initial liquid pressure** — Starting liquid pressure for compressible fluids `0.101325` `MPa` (default) | positive scalar

Starting liquid pressure for compressible fluids.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.

### **Nominal liquid pressure** — Pressure at nominal operating conditions `0.101325 MPa` (default) | scalar

Liquid pressure at nominal operating conditions. The block uses this value to calculate
the nominal density to use in the mass conservation equation when
dynamic compressibility is disabled.

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

Single-acting linear actuator in an isothermal liquid system

The Single-Acting Actuator (IL) block represents an actuator
that converts the liquid pressure at port **A** into a mechanical force
at port **R** via an extending-retracting piston. The piston motion is
limited by a hard stop model. When the piston position is calculated internally, it is
reported at port **p**, and when the position is set by a connection to
a Simscape™
Multibody™ joint, it is received as a physical signal at port **p**.

The **Initial piston displacement**, **Enable dynamic
compressibility**, and reference environmental pressure can be modified.
Fluid and mechanical inertia are not modeled.

### Displacement

The piston displacement is measured as the position at port **R** relative
to port **C**. The **Mechanical orientation**
identifies the direction of piston displacement. The piston displacement is neutral,
or `0`, when the chamber volume is equal to the **Dead
volume**. When displacement is received as an input, ensure that the
derivative of the position is equal to the piston velocity. This is automatically
the case when the input is received from a Translational Multibody Interface block
connection to a Simscape Multibody joint.

### Hard Stop Model

Four models are available to model the extension limit of the actuator piston. This block
uses a similar formulation as the Translational Hard Stop block and models uniform
damping and stiffness coefficients at both ends of the piston stroke. For more
information on the hard stop model options, see the Translational Hard Stop block.

The hard stop force is modeled when the piston is at its upper or lower bound. The
boundary region is within the **Transition region** of the
**Piston stroke** or **Piston initial
displacement**. Outside of this region, FHardStop=0.

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

You can optionally model leakage between the liquid chamber and the piston reservoir. When
you select **Leakage**, Poiseuille flow is modeled between the
piston and cylinder. This block uses the Simscape Foundation Library Laminar Leakage (IL) block. The
flow rate is calculated as:

m˙=π128(d04−di4−(d02−di2)2log(d0/di))υL(pA−penv),

where:

- *ν* is the fluid kinematic viscosity.
- *L* is the piston length, **p** –
  *P*0.
- *p*A is the pressure at port
  **A**.
- *p*env is the environmental
  pressure, which is selected in the **Environment pressure
  specification** parameter.

The cylinder diameter, *d*0,
is d0=di+2c, where *c* is the **Piston-cylinder
clearance**, and the piston diameter,
*d*i, is di=4APπ, where *A*P is the
**Piston cross-sectional area**.

### Numerically-Smoothed Area and Pressure

You can maintain numerical robustness in your
simulation by adjusting the **Smoothing factor** parameter. If
the **Smoothing factor** parameter is nonzero, the block smooths
the cushion orifice area and the check valve pressure range. The orifice area is
smoothly saturated between the **Leakage area between plunger and cushion
sleeve** and **Cushion plunger cross-sectional area**
parameters while the valve pressure is saturated between the **Check valve
cracking pressure differential** and **Check valve maximum
pressure differential** parameters. For more information, see Numerical Smoothing.

### Block Sub-Components

The Single-Acting Actuator (IL) block comprises four Simscape Foundation and two
Fluids Library blocks:

- Translational Hard Stop
- Laminar Leakage (IL)
- Translational Mechanical Converter (IL)
- Ideal Translational Motion Sensor
- Cylinder Cushion (IL)
- Cylinder Friction (IL)

**Actuator Structural Diagram**
