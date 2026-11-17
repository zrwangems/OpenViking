---
type: simulink-block
title: 'Vehicle Body Total Road Load'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Vehicle Dynamics'
documentation_page: 'vehiclebodytotalroadload'
documentation_source_path: 'ref/vehiclebodytotalroadload.html'
language: en
---

# Vehicle Body Total Road Load

## Ports
```yaml
ports:
- name: xdot
  summary: Vehicle longitudinal velocity scalar
  direction: input
- name: xddot
  summary: Vehicle longitudinal acceleration scalar
  direction: input
- name: PwrTot
  summary: Tractive input power scalar
  direction: input
- name: ForceTot
  summary: Tractive input force scalar
  direction: input
- name: Grade
  summary: Road grade angle scalar
  direction: input
- name: Info
  summary: Bus signal bus
  direction: output
- name: xdot
  summary: Vehicle longitudinal velocity scalar
  direction: output
- name: ForceTot
  summary: Tractive input force scalar
  direction: output
```

### Input

### **xdot** — Vehicle longitudinal velocity `scalar`

Vehicle total longitudinal velocity, x˙, in m/s.

#### Dependencies

To enable this port, for the **Input Mode**
parameter, select `Kinematic`.

### **xddot** — Vehicle longitudinal acceleration `scalar`

Vehicle total longitudinal acceleration, x¨, in m/s^2.

#### Dependencies

To enable this port, for the **Input Mode**
parameter, select `Kinematic`.

### **PwrTot** — Tractive input power `scalar`

Tractive input power,
*Ptotal*, in W.

#### Dependencies

To enable this port, for the **Input Mode**
parameter, select `Power`.

### **ForceTot** — Tractive input force `scalar`

Tractive input force,
*Ftotal*, in N.

#### Dependencies

To enable this port, for the **Input Mode**
parameter, select `Force`.

### **Grade** — Road grade angle `scalar`

Road grade angle, *Θ*, in deg.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | | Description | Value | Units |
| --- | --- | --- | --- | --- | --- | --- |
| `InertFrm` | `Cg` | `Disp` | `X` | Vehicle CG displacement along earth-fixed `X`-axis | Computed relative to the road grade. | m |
| `Y` | Vehicle CG displacement along earth-fixed `Y`-axis | `0` | m |
| `Z` | Vehicle CG displacement along earth-fixed `Z`-axis | Computed relative to the road grade. | m |
| `Vel` | `Xdot` | Vehicle CG velocity along earth-fixed `X`-axis | Computed relative to the road grade. | m/s |
| `Ydot` | Vehicle CG velocity along earth-fixed `Y`-axis | `0` | m/s |
| `Zdot` | Vehicle CG velocity along earth-fixed `Z`-axis | Computed relative to the road grade. | m/s |
| `Ang` | `phi` | Rotation of vehicle-fixed frame about the earth-fixed `X`-axis (roll) | `0` | rad |
| `theta` | Rotation of vehicle-fixed frame about the earth-fixed `Y`-axis (pitch) | Computed relative to the grade angle. | rad |
| `psi` | Rotation of vehicle-fixed frame about the earth-fixed `Z`-axis (yaw) | `0` | rad |
| `BdyFrm` | `Cg` | `Disp` | `x` | Vehicle CG displacement along the vehicle-fixed `x`-axis | Computed | m |
| `y` | Vehicle CG displacement along the vehicle-fixed `y`-axis | `0` | m |
| `z` | Vehicle CG displacement along the vehicle-fixed `z`-axis | `0` | m |
| `Vel` | `xdot` | Vehicle CG velocity along the vehicle-fixed `x`-axis | Computed | m/s |
| `ydot` | Vehicle CG velocity along the vehicle-fixed `y`-axis | `0` | m/s |
| `zdot` | Vehicle CG velocity along the vehicle-fixed `z`-axis | `0` | m/s |
| `Acc` | `ax` | Vehicle CG inertial acceleration along the vehicle-fixed *x*-axis | Computed | gn |
| `ay` | Vehicle CG inertial acceleration along the vehicle-fixed *y*-axis | `0` | gn |
| `az` | Vehicle CG inertial acceleration along the vehicle-fixed *z*-axis | `0` | gn |
| `xddot` | Vehicle CG acceleration along the vehicle-fixed *x*-axis, excluding the centrifugal component | Computed | m/s^2 |
| `yddot` | Vehicle CG acceleration along the vehicle-fixed *y*-axis, excluding the centrifugal component | Computed | m/s^2 |
| `zddot` | Vehicle CG acceleration along the vehicle-fixed *z*-axis, excluding the centrifugal component. | `0` | m/s^2 |
| `Forces` | `Body` | `Fx` | Net force on vehicle CG along the vehicle-fixed `x`-axis | Computed | N |
| `Fy` | Net force on vehicle CG along the vehicle-fixed `y`-axis | `0` | N |
| `Fz` | Net force on vehicle CG along the vehicle-fixed `z`-axis | `0` | N |
| `Ext` | `Fx` | External force on vehicle CG along the vehicle-fixed `x`-axis | Computed | N |
| `Fy` | External force on vehicle CG along the vehicle-fixed `y`-axis | `0` | N |
| `Fz` | External force on vehicle CG along the vehicle-fixed `z`-axis | `0` | N |
| `Drag` | `Fx` | Drag force on vehicle CG along the vehicle-fixed `x`-axis | Computed | N |
| `Fy` | Drag force on vehicle CG along the vehicle-fixed `y`-axis | `0` | N |
| `Fz` | Drag force on vehicle CG along the vehicle-fixed `z`-axis | `0` | N |
| `Grvty` | `Fx` | Gravity force on vehicle CG along the vehicle-fixed `x`-axis | Computed | N |
| `Fy` | Gravity force on vehicle CG along the vehicle-fixed `y`-axis | `0` | N |
| `Fz` | Gravity force on vehicle CG along the vehicle-fixed `z`-axis | Computed | N |
| `Pwr` | `PwrExt` | | Applied external power | Computed | W |
| `Drag` | | Power loss due to drag | Computed | W |
| `PwrInfo` | `PwrTrnsfrd` | `PwrFxExt` | | Externally applied force power | *PFxExt* | W |
| `PwrNotTrnsfrd` | `PwrFxDrag` | | Drag force power | *PD* | W |
| `PwrStored` | `wrStoredGrvty` | | Rate change in gravitational potential energy | *Pg* | W |
| `PwrStoredxdot` | | Rate in change of longitudinal kinetic energy | *Pxdot* | W |

### **xdot** — Vehicle longitudinal velocity `scalar`

Vehicle total longitudinal velocity, x˙, in m/s.

#### Dependencies

To enable this port, for the **Input Mode**
parameter, select `Power` or
`Force`.

### **ForceTot** — Tractive input force `scalar`

Tractive input force,
*Ftotal*, in N.

#### Dependencies

To enable this port, for the **Input Mode**
parameter, select `Kinematic`.
## Parameters
```yaml
parameters:
- name: Input Mode
  summary: Specify input mode Kinematic (default) | Force | Power
  group: ''
- name: Mass
  summary: Vehicle body mass 1200 (default) | scalar
  group: ''
- name: Rolling resistance coefficient, a
  summary: Rolling 196 (default) | scalar
  group: ''
- name: Rolling and driveline resistance coefficient, b
  summary: Rolling and driveline 2.232 (default) | scalar
  group: ''
- name: Aerodynamic drag coefficient, c
  summary: Drag 0.389 (default) | scalar
  group: ''
- name: Gravitational acceleration, g
  summary: Gravity 9.81 (default) | scalar
  group: ''
- name: Initial position, x_o
  summary: Position 0 (default) | scalar
  group: ''
- name: Initial velocity, xdot_o
  summary: Velocity 0 (default) | scalar
  group: ''
```

### **Input Mode** — Specify input mode `Kinematic` (default) | `Force` | `Power`

Specify the input type.

- `Kinematic` — Block uses the
  vehicle longitudinal velocity and acceleration to calculate the
  tractive force and power. Use this configuration for powertrain,
  driveline, and braking system design, or component
  sizing.
- `Force` — Block uses the
  tractive force to calculate the vehicle longitudinal
  displacement and velocity. Use this configuration for
  system-level performance, fuel economy, or drive cycle tracking
  studies.
- `Power` — Block uses the
  engine or transmission power to calculate the vehicle
  longitudinal displacement and velocity. Use this configuration
  for system-level performance, fuel economy, or drive cycle
  tracking studies.

#### Dependencies

This table summarizes the port and input mode configurations.

| Input Mode | Creates Ports |
| --- | --- |
| `Kinematic` | `xdot`  `xddot` |
| `Force` | `Force` |
| `Power` | `Power` |

### **Mass** — Vehicle body mass `1200` (default) | `scalar`

Vehicle body mass, *m*, in kg.

### **Rolling resistance coefficient, a** — Rolling `196` (default) | `scalar`

Steady-state rolling resistance coefficient, *a*, in
N.

### **Rolling and driveline resistance coefficient, b** — Rolling and driveline `2.232` (default) | `scalar`

Viscous driveline and rolling resistance coefficient,
*b*, in N\*s/m.

### **Aerodynamic drag coefficient, c** — Drag `0.389` (default) | `scalar`

Aerodynamic drag coefficient, *c*, in N·s^2/m.

### **Gravitational acceleration, g** — Gravity `9.81` (default) | `scalar`

Gravitational acceleration, *g*, in m/s^2.

### **Initial position, x\_o** — Position `0` (default) | `scalar`

Vehicle longitudinal initial position, in m.

### **Initial velocity, xdot\_o** — Velocity `0` (default) | `scalar`

Vehicle longitudinal initial velocity with respect to ground, in
m/s.
## Libraries

Powertrain Blockset / Vehicle Dynamics Vehicle Dynamics Blockset / Vehicle Body

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Vehicle motion using coast-down testing coefficients

The Vehicle Body Total Road Load block implements a one
degree-of-freedom (1DOF) rigid vehicle model using coast-down testing coefficients. You
can use this block in a vehicle model to represent the load that the driveline and
chassis applies to a transmission or engine. It is suitable for system-level
performance, component sizing, fuel economy, or drive cycle tracking studies. The block
calculates the dynamic powertrain load with minimal parameterization or computational
cost.

You can configure the block for kinematic, force, or total power input.

- Kinematic — Block uses the vehicle longitudinal velocity and
  acceleration to calculate the tractive force and power.
- Force — Block uses the tractive force to calculate the vehicle
  longitudinal displacement and velocity.
- Power — Block uses the engine or transmission power to calculate
  the vehicle longitudinal displacement and velocity.

### Dynamics

To calculate the total road load acting on the vehicle, the block implements this equation.

Froad=a+bx˙+cx˙2+mgsin(θ)

To determine the coefficients *a*,
*b*, and *c*, you can use a test procedure
similar to the one described in *Road Load Measurement and Dynamometer
Simulation Using Coastdown Techniques*. You can also use Simulink®
Design Optimization™ to fit the coefficients to measured data (see Estimate Vehicle Drag Coefficients by Coast-Down Testing (Simulink Design Optimization)).

To calculate the vehicle motion, the block uses Newton’s law for rigid bodies.

Ftotal=mx¨+Froad

Total power input is a product of the total force and longitudinal velocity. Power
due to road and gravitational forces is a product of the road force and longitudinal velocity.

Ptotal=Ftotalx˙Proad=Froadx˙

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Variable | Equations |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrFxExt` | Externally applied force power | *PFxExt* | PFxExt=Ftotalx˙ |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrFxDrag` | Drag force power | *PD* | Pd=−(a+bx˙+cx˙2)x˙ |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `wrStoredGrvty` | Rate change in gravitational potential energy | *Pg* | Pg=−mgZ˙ |
| `PwrStoredxdot` | Rate in change of longitudinal kinetic energy | *Pxdot* | Px˙=mx¨x˙ |

The equations use these variables.

|  |  |
| --- | --- |
| *a* | Steady-state rolling resistance coefficient |
| *b* | Viscous driveline and rolling resistance coefficient |
| *c* | Aerodynamic drag coefficient |
| *g* | Gravitational acceleration |
| *x* | Vehicle longitudinal displacement with respect to ground, in the vehicle-fixed frame |
| x˙ | Vehicle longitudinal velocity with respect to ground, in the vehicle-fixed frame |
| x¨ | Vehicle longitudinal acceleration with respect to ground, vehicle-fixed frame |
| *m* | Vehicle body mass |
| *Θ* | Road grade angle |
| *Ftotal* | Total force acting on vehicle |
| *Froad* | Resistive road load due to losses and gravitational load |
| *Ptotal* | Total tractive input power |
| *Proad* | Total power due to losses and gravitational load |
| Z˙ | Vehicle vertical velocity along the vehicle-fixed `z`-axis |
