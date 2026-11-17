---
type: simulink-block
title: 'Bicycle Model'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Driving Scenario and Sensor Modeling'
documentation_page: 'bicyclemodel'
documentation_source_path: 'ref/bicyclemodel.html'
language: en
---

# Bicycle Model

## Ports
```yaml
ports:
- name: WhlAngF
  summary: Wheel angle scalar
  direction: input
- name: FxF
  summary: 'Force Input: Total longitudinal force on the front axle scalar'
  direction: input
- name: FxR
  summary: 'Force Input: Total longitudinal force on the rear axle scalar'
  direction: input
- name: xdotin
  summary: 'Velocity Input: Longitudinal velocity scalar'
  direction: input
- name: Info
  summary: Bus signal bus
  direction: output
- name: xdot
  summary: Vehicle body longitudinal velocity scalar
  direction: output
- name: ydot
  summary: Vehicle body lateral velocity scalar
  direction: output
- name: psi
  summary: Yaw scalar
  direction: output
- name: r
  summary: Yaw rate scalar
  direction: output
```

### Input

### **WhlAngF** — Wheel angle `scalar`

Front wheel angle, in rad.

### **FxF** — Force Input: Total longitudinal force on the front axle `scalar`

Longitudinal force on the front axle,
*FxF*, along
vehicle-fixed `x`-axis, in N.

Bicycle Model - Force Input block input port.

### **FxR** — Force Input: Total longitudinal force on the rear axle `scalar`

Longitudinal force on the rear axle,
*FxR*, along
vehicle-fixed `x`-axis, in N.

Bicycle Model - Force Input block input port.

### **xdotin** — Velocity Input: Longitudinal velocity `scalar`

Vehicle CG velocity along vehicle-fixed *x*-axis,
in m/s.

Bicycle Model - Velocity Input block input port.
### Output

### **Info** — Bus signal bus

Bus signal containing these block values.

| Signal | | | | | | Description | Value | Units |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `InertFrm` | `Cg` | `Disp` | `X` | | | Vehicle CG displacement along the earth-fixed *X*-axis | Computed | m |
| `Y` | | | Vehicle CG displacement along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | | Vehicle CG displacement along the earth-fixed *Z*-axis | `0` | m |
| `Vel` | `Xdot` | | | Vehicle CG velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | | Vehicle CG velocity along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | | Vehicle CG velocity along the earth-fixed *Z*-axis | `0` | m/s |
| `Ang` | `phi` | | | Rotation of the vehicle-fixed frame about the earth-fixed *X*-axis (roll) | `0` | rad |
| `theta` | | | Rotation of the vehicle-fixed frame about the earth-fixed *Y*-axis (pitch) | `0` | rad |
| `psi` | | | Rotation of the vehicle-fixed frame about the earth-fixed *Z*-axis (yaw) | Computed | rad |
| `FrntAxl` | `Disp` | `X` | | | Front wheel displacement along the earth-fixed *X*-axis | Computed | m |
| `Y` | | | Front wheel displacement along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | | Front wheel displacement along the earth-fixed *Z*-axis | `0` | m |
| `Vel` | `Xdot` | | | Front wheel velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | | Front wheel velocity along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | | Front wheel velocity along the earth-fixed *Z*-axis | `0` | m/s |
| `RearAxl` | `Disp` | `X` | | | Rear wheel displacement along the earth-fixed *X*-axis | Computed | m |
| `Y` | | | Rear wheel displacement along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | | Rear wheel displacement along the earth-fixed *Z*-axis | `0` | m |
| `Vel` | `Xdot` | | | Rear wheel velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | | Rear wheel velocity along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | | Rear wheel velocity along the earth-fixed *Z*-axis | `0` | m/s |
| `Hitch` | `Disp` | `X` | | | Hitch offset from axle plane along the earth-fixed *X*-axis | Computed | m |
| `Y` | | | Hitch offset from center plane along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | | Hitch offset from axle plane along the earth-fixed *Z*-axis | Computed | m |
| `Vel` | `Xdot` | | | Hitch offset velocity from axle plane along the earth-fixed *X*-axis | Computed | m |
| `Ydot` | | | Hitch offset velocity from center plane along the earth-fixed *Y*-axis | Computed | m |
| `Zdot` | | | Hitch offset velocity from axle plane along the earth-fixed *Z*-axis | Computed | m |
| `Geom` | `Disp` | `X` | | | Vehicle chassis offset from axle plane along the earth-fixed *X*-axis | Computed | m |
| `Y` | | | Vehicle chassis offset from center plane along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | | Vehicle chassis offset from axle plane along the earth-fixed *Z*-axis | Computed | m |
| `Vel` | `Xdot` | | | Vehicle chassis offset velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | | Vehicle chassis offset velocity along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | | Vehicle chassis offset velocity along the earth-fixed *Z*-axis | Computed | m/s |
| `BdyFrm` | `Cg` | `Vel` | `xdot` | | | Vehicle CG velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | | Vehicle CG velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | | Vehicle CG velocity along the vehicle-fixed *z*-axis | `0` | m/s |
| `Ang` | `Beta` | | | Body slip angle, *β*    β=VyVx | Computed | rad |
| `AngVel` | `p` | | | Vehicle angular velocity about the vehicle-fixed *x*-axis (roll rate) | `0` | rad/s |
| `q` | | | Vehicle angular velocity about the vehicle-fixed *y*-axis (pitch rate) | `0` | rad/s |
| `r` | | | Vehicle angular velocity about the vehicle-fixed *z*-axis (yaw rate) | Computed | rad/s |
| `Acc` | `ax` | | | Vehicle CG acceleration along the vehicle-fixed *x*-axis | Computed | gn |
| `ay` | | | Vehicle CG acceleration along the vehicle-fixed *y*-axis | Computed | gn |
| `az` | | | Vehicle CG acceleration along the vehicle-fixed *z*-axis | `0` | gn |
| `xddot` | | | Vehicle CG acceleration along the vehicle-fixed *x*-axis | Computed | m/s^2 |
| `yddot` | | | Vehicle CG acceleration along the vehicle-fixed *y*-axis | Computed | m/s^2 |
| `zddot` | | | Vehicle CG acceleration along the vehicle-fixed *z*-axis | `0` | m/s^2 |
| `AngAcc` | `pdot` | | | Vehicle angular acceleration about the vehicle-fixed *x*-axis | `0` | rad/s |
| `qdot` | | | Vehicle angular acceleration about the vehicle-fixed *y*-axis | `0` | rad/s |
| `rdot` | | | Vehicle angular acceleration about the vehicle-fixed *z*-axis | Computed | rad/s |
| `DCM` | Direction cosine matrix | | | | Computed | rad |
| `Forces` | `Body` | `Fx` | | | Net force on vehicle CG along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | | Net force on vehicle CG along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | | Net force on vehicle CG along the vehicle-fixed *z*-axis | `0` | N |
| `Ext` | `Fx` | | | External force on vehicle CG along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | | External force on vehicle CG along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | | External force on vehicle CG along the vehicle-fixed *z*-axis | `0` | N |
| `Hitch` | `Fx` | | | Hitch force applied to body at the hitch location along the vehicle-fixed *x*-axis | Input | N |
| `Fy` | | | Hitch force applied to body at the hitch location along the vehicle-fixed *y*-axis | Input | N |
| `Fz` | | | Hitch force applied to body at the hitch location along the vehicle-fixed *z*-axis | Input | N |
| `FrntAxl` | `Fx` | | | Longitudinal force on front wheel, along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | | Lateral force on front wheel along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | | Normal force on front wheel, along the vehicle-fixed *z*-axis | Computed | N |
| `RearAxl` | `Fx` | | | Longitudinal force on rear wheel, along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | | Lateral force on rear wheel along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | | Normal force on rear wheel, along the vehicle-fixed *z*-axis | Computed | N |
| `Tires` | `FrntTire` | `Fx` | | Front tire force, along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Front tire force, along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Front tire force, along the vehicle-fixed *z*-axis | Computed | N |
| `RearTire` | `Fx``Fx` | | Rear tire force, along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Rear tire force, along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Rear tire force, along the vehicle-fixed *z*-axis | Computed | N |
| `Drag` | `Fx` | | | Drag force on vehicle CG along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | | Drag force on vehicle CG along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | | Drag force on vehicle CG along the vehicle-fixed *z*-axis | Computed | N |
| `Grvty` | `Fx` | | | Gravity force on vehicle CG along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | | Gravity force on vehicle CG along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | | Gravity force on vehicle CG along the vehicle-fixed *z*-axis | Computed | N |
| `Moments` | `Body` | `Mx` | | | Body moment on vehicle CG about the vehicle-fixed *x*-axis | `0` | N·m |
| `My` | | | Body moment on vehicle CG about the vehicle-fixed *y*-axis | Computed | N·m |
| `Mz` | | | Body moment on vehicle CG about the vehicle-fixed *z*-axis | `0` | N·m |
| `Drag` | `Mx` | | | Drag moment on vehicle CG about the vehicle-fixed *x*-axis | `0` | N·m |
| `My` | | | Drag moment on vehicle CG about the vehicle-fixed *y*-axis | Computed | N·m |
| `Mz` | | | Drag moment on vehicle CG about the vehicle-fixed *z*-axis | `0` | N·m |
| `Ext` | `Mx` | | | External moment on vehicle CG about the vehicle-fixed *x*-axis | `0` | N·m |
| `My` | | | External moment on vehicle CG about the vehicle-fixed *y*-axis | Computed | N·m |
| `Mz` | | | External moment on vehicle CG about the vehicle-fixed *z*-axis | `0` | N·m |
| `Hitch` | `Mx` | | | Hitch moment at the hitch location about vehicle-fixed *x*-axis | `0` | N·m |
| `My` | | | Hitch moment at the hitch location about vehicle-fixed *y*-axis | Computed | N·m |
| `Mz` | | | Hitch moment at the hitch location about vehicle-fixed *z*-axis | `0` | N·m |
| `FrntAxl` | `Disp` | `x` | | | Front wheel displacement along the vehicle-fixed *x*-axis | Computed | m |
| `y` | | | Front wheel displacement along the vehicle-fixed *y*-axis | Computed | m |
| `z` | | | Front wheel displacement along the vehicle-fixed *z*-axis | Computed | m |
| `Vel` | `xdot` | | | Front wheel velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | | Front wheel velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | | Front wheel velocity along the vehicle-fixed *z*-axis | `0` | m/s |
| `Steer` | `WhlAngFL` | | | Front left wheel steering angle | Computed | rad |
| `WhlAngFR` | | | Front right wheel steering angle | Computed | rad |
| `RearAxl` | `Disp` | `x` | | | Rear wheel displacement along the vehicle-fixed *x*-axis | Computed | m |
| `y` | | | Rear wheel displacement along the vehicle-fixed *y*-axis | Computed | m |
| `z` | | | Rear wheel displacement along the vehicle-fixed *z*-axis | Computed | m |
| `Vel` | `xdot` | | | Rear wheel velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | | Rear wheel velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | | Rear wheel velocity along the vehicle-fixed *z*-axis | `0` | m/s |
| `Steer` | `WhlAngRL` | | | Rear left wheel steering angle | Computed | rad |
| `WhlAngRR` | | | Rear right wheel steering angle | Computed | rad |
| `Hitch` | `Disp` | | `x` | | Hitch offset from axle plane along the vehicle-fixed *x*-axis | Input | m |
| `y` | | Hitch offset from center plane along the vehicle-fixed *y*-axis | Input | m |
| `z` | | Hitch offset from axle plane along the earth-fixed *z*-axis | Input | m |
| `Vel` | | `xdot` | | Hitch offset velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Hitch offset velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | Hitch offset velocity along the vehicle-fixed *z*-axis | Computed | m/s |
| `Pwr` | `Ext` | | | | Applied external power | Computed | W |
| `Hitch` | | | | Power loss due to hitch | Computed | W |
| `Drag` | | | | Power loss due to drag | Computed | W |
| `Geom` | `Disp` | | `x` | | Vehicle chassis offset from axle plane along the vehicle-fixed *x*-axis | Input | m |
| `y` | | Vehicle chassis offset from center plane along the vehicle-fixed *y*-axis | Input | m |
| `z` | | Vehicle chassis offset from axle plane along the earth-fixed *z*-axis | Input | m |
| `Vel` | | `xdot` | | Vehicle chassis offset velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Vehicle chassis offset velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | Vehicle chassis offset velocity along the vehicle-fixed *z*-axis | `0` | m/s |
| `Ang` | | `Beta` | | Body slip angle, *β*    β=VyVx | Computed | rad |

| Signal | | | Description | | Value | Units |
| --- | --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` | `PwrFxExt` | Externally applied longitudinal force power | | Computed | W |
| `PwrFyExt` | Externally applied lateral force power | | Computed | W |
| `PwrMzExt` | Externally applied roll moment power | | Computed | W |
| `PwrFwFx` | Longitudinal force applied at the front axle power | | Computed | W |
| `PwrFwFy` | Lateral force applied at the front axle power | | Computed | W |
| `PwrFwRx` | Longitudinal force applied at the rear axle power | | Computed | W |
| `PwrFwRy` | Lateral force applied at the rear axle power | | Computed | W |
| `PwrNotTrnsfrd` | `PwrFxDrag` | Longitudinal drag force power | | Computed | W |
| `PwrFyDrag` | Lateral drag force power | | Computed | W |
| `PwrMzDrag` | Drag pitch moment power | | Computed | W |
| `PwrStored` | `PwrStoredGrvty` | Rate change in gravitational potential energy | | Computed | W |
| `PwrStoredxdot` | Rate of change of longitudinal kinetic energy | | Computed | W |
| `PwrStoredydot` | Rate of change of lateral kinetic energy | | Computed | W |
| `PwrStoredr` | Rate of change of rotational yaw kinetic energy | | Computed | W |

### **xdot** — Vehicle body longitudinal velocity `scalar`

Vehicle CG velocity along vehicle-fixed `x`-axis, in
m/s.

### **ydot** — Vehicle body lateral velocity `scalar`

Vehicle CG velocity along vehicle-fixed `y`-axis, in
m/s.

### **psi** — Yaw `scalar`

Rotation of the vehicle-fixed frame about earth-fixed
`Z`-axis (yaw), in rad.

### **r** — Yaw rate `scalar`

Vehicle angular velocity, `r`, about the
vehicle-fixed `z`-axis (yaw rate), in rad/s.
## Parameters
```yaml
parameters:
- name: Number of wheels on front axle, NF
  summary: Front wheel count 2 (default) | scalar
  group: ''
- name: Number of wheels on rear axle, NR
  summary: Rear wheel count 2 (default) | scalar
  group: ''
- name: Vehicle mass, m
  summary: Vehicle mass 2000 (default) | scalar
  group: ''
- name: Longitudinal distance from center of mass to front axle, a
  summary: Front axle distance 1.4 (default) | scalar
  group: ''
- name: Longitudinal distance from center of mass to rear axle, b
  summary: Rear axle distance 1.6 (default) | scalar
  group: ''
- name: Vertical distance from center of mass to axle plane, h
  summary: Height 0.35 (default) | scalar
  group: ''
- name: Initial inertial frame longitudinal position, X_o
  summary: Position 0 (default) | scalar
  group: ''
- name: Initial longitudinal velocity, xdot_o
  summary: Velocity 0 (default) | scalar
  group: ''
- name: Front tire corner stiffness, Cy_f
  summary: Stiffness 12e3 (default) | scalar
  group: ''
- name: Rear tire corner stiffness, Cy_r
  summary: Stiffness 11e3 (default) | scalar
  group: ''
- name: Initial inertial frame lateral displacement, Y_o
  summary: Position 0 (default) | scalar
  group: ''
- name: Initial lateral velocity, ydot_o
  summary: Velocity 0 (default) | scalar
  group: ''
- name: Yaw polar inertia, Izz
  summary: Inertia 4000 (default) | scalar
  group: ''
- name: Initial yaw angle, psi_o
  summary: Psi rotation 0 (default) | scalar
  group: ''
- name: Initial yaw rate, r_o
  summary: Yaw rate 0 (default) | scalar
  group: ''
- name: Longitudinal drag area, Af
  summary: Effective vehicle cross-sectional area 2 (default) | scalar
  group: ''
- name: Longitudinal drag coefficient, Cd
  summary: Air drag coefficient .3 (default) | scalar
  group: ''
- name: Longitudinal lift coefficient, Cl
  summary: Air lift coefficient .1 (default) | scalar
  group: ''
- name: Longitudinal drag pitch moment, Cpm
  summary: Pitch drag .1 (default) | scalar
  group: ''
- name: Relative wind angle vector, beta_w
  summary: Wind angle [0:0.01:0.3] (default) | vector
  group: ''
- name: Side force coefficient vector, Cs
  summary: Side force coefficient [0:0.03:0.9] (default) | vector
  group: ''
- name: Yaw moment coefficient vector, Cym
  summary: Yaw moment drag [0:0.01:0.3] (default) | vector
  group: ''
- name: Absolute pressure, Pabs
  summary: Pressure 101325 (default) | scalar | scalar
  group: ''
- name: Air temperature, Tair
  summary: Temperature 273 (default) | scalar
  group: ''
- name: Gravitational acceleration, g
  summary: Gravity 9.81 (default) | scalar
  group: ''
- name: Nominal friction scaling factor, mu
  summary: Friction scale factor 1 (default) | scalar
  group: ''
- name: Longitudinal velocity tolerance, xdot_tol
  summary: Tolerance .01 (default) | scalar
  group: ''
- name: Nominal normal force, Fznom
  summary: Normal force 5000 (default) | scalar
  group: ''
- name: Geometric longitudinal offset from axle plane, longOff
  summary: Longitudinal offset 0 (default) | scalar
  group: ''
- name: Geometric lateral offset from center plane, latOff
  summary: Lateral offset 0 (default) | scalar
  group: ''
- name: Geometric vertical offset from axle plane, vertOff
  summary: Vertical offset 0 (default) | scalar
  group: ''
```

#### Longitudinal

### **Number of wheels on front axle, NF** — Front wheel count `2` (default) | `scalar`

Number of wheels on front axle,
*NF*. The value is
dimensionless.

### **Number of wheels on rear axle, NR** — Rear wheel count `2` (default) | `scalar`

Number of wheels on rear axle,
*NR*. The value is
dimensionless.

### **Vehicle mass, m** — Vehicle mass `2000` (default) | `scalar`

Vehicle mass, *m*, in kg.

### **Longitudinal distance from center of mass to front axle, a** — Front axle distance `1.4` (default) | `scalar`

Horizontal distance *a* from the vehicle CG to the front
wheel axle, in m.

### **Longitudinal distance from center of mass to rear axle, b** — Rear axle distance `1.6` (default) | `scalar`

Horizontal distance *b* from the vehicle CG to the rear
wheel axle, in m.

### **Vertical distance from center of mass to axle plane, h** — Height `0.35` (default) | `scalar`

Height of vehicle CG above the axles, *h*, in m.

### **Initial inertial frame longitudinal position, X\_o** — Position `0` (default) | `scalar`

Initial vehicle CG displacement along earth-fixed
*X*-axis, in m.

### **Initial longitudinal velocity, xdot\_o** — Velocity `0` (default) | `scalar`

Initial vehicle CG velocity along vehicle-fixed
*x*-axis, in m/s.

#### Lateral

### **Front tire corner stiffness, Cy\_f** — Stiffness `12e3` (default) | `scalar`

Front tire corner stiffness,
*Cyf*, in N/rad.

### **Rear tire corner stiffness, Cy\_r** — Stiffness `11e3` (default) | `scalar`

Rear tire corner stiffness, *Cyr*,
in N/rad.

### **Initial inertial frame lateral displacement, Y\_o** — Position `0` (default) | `scalar`

Initial vehicle CG displacement along earth-fixed
*Y*-axis, in m.

### **Initial lateral velocity, ydot\_o** — Velocity `0` (default) | `scalar`

Initial vehicle CG velocity along vehicle-fixed
*y*-axis, in m/s.

#### Yaw

### **Yaw polar inertia, Izz** — Inertia `4000` (default) | `scalar`

Yaw polar inertia, in kg\*m^2.

### **Initial yaw angle, psi\_o** — Psi rotation `0` (default) | `scalar`

Rotation of the vehicle-fixed frame about earth-fixed *Z*-axis
(yaw), in rad.

### **Initial yaw rate, r\_o** — Yaw rate `0` (default) | `scalar`

Vehicle angular velocity about the vehicle-fixed *z*-axis (yaw
rate), in rad/s.

#### Aerodynamic

### **Longitudinal drag area, Af** — Effective vehicle cross-sectional area `2` (default) | `scalar`

Effective vehicle cross-sectional area,
*Af*, to calculate the aerodynamic drag
force on the vehicle, in m2.

### **Longitudinal drag coefficient, Cd** — Air drag coefficient `.3` (default) | `scalar`

Air drag coefficient, *Cd*. The value is
dimensionless.

### **Longitudinal lift coefficient, Cl** — Air lift coefficient `.1` (default) | `scalar`

Air lift coefficient, *Cl*. The value is
dimensionless.

### **Longitudinal drag pitch moment, Cpm** — Pitch drag `.1` (default) | `scalar`

Longitudinal drag pitch moment coefficient,
*Cpm*. The value is
dimensionless.

### **Relative wind angle vector, beta\_w** — Wind angle `[0:0.01:0.3]` (default) | `vector`

Relative wind angle vector, *βw*, in
rad.

### **Side force coefficient vector, Cs** — Side force coefficient `[0:0.03:0.9]` (default) | `vector`

Side force coefficient vector coefficient,
*Cs*. The value is dimensionless.

### **Yaw moment coefficient vector, Cym** — Yaw moment drag `[0:0.01:0.3]` (default) | `vector`

Yaw moment coefficient vector, *Cym*. The
value is dimensionless.

#### Environment

### **Absolute pressure, Pabs** — Pressure `101325` (default) | `scalar` | `scalar`

Environmental absolute pressure,
*Pabs*, in Pa.

### **Air temperature, Tair** — Temperature `273` (default) | `scalar`

Environmental absolute temperature, *T*, in K.

### **Gravitational acceleration, g** — Gravity `9.81` (default) | `scalar`

Gravitational acceleration, *g*, in m/s^2.

### **Nominal friction scaling factor, mu** — Friction scale factor `1` (default) | `scalar`

Nominal friction scale factor, *μ*. The value is
dimensionless.

#### Simulation

### **Longitudinal velocity tolerance, xdot\_tol** — Tolerance `.01` (default) | `scalar`

Longitudinal velocity tolerance, in m/s.

### **Nominal normal force, Fznom** — Normal force `5000` (default) | `scalar`

Nominal normal force, in N.

### **Geometric longitudinal offset from axle plane, longOff** — Longitudinal offset `0` (default) | `scalar`

Vehicle chassis offset from axle plane along body-fixed
*x*-axis, in m. When you use the 3D visualization
engine, consider using the offset to locate the chassis independent of the
vehicle CG.

### **Geometric lateral offset from center plane, latOff** — Lateral offset `0` (default) | `scalar`

Vehicle chassis offset from center plane along body-fixed
*y*-axis, in m. When you use the 3D visualization
engine, consider using the offset to locate the chassis independent of the
vehicle CG.

### **Geometric vertical offset from axle plane, vertOff** — Vertical offset `0` (default) | `scalar`

Vehicle chassis offset from axle plane along body-fixed
*z*-axis, in m. When you use the 3D visualization
engine, consider using the offset to locate the chassis independent of the
vehicle CG.
## Libraries

Automated Driving Toolbox / Driving Scenario and Sensor Modeling Vehicle Dynamics Blockset / Vehicle Body

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2024a: Requires Simulink 3D Animation

Simulating models with the Bicycle Model block requires
Simulink
3D Animation.

## Description

Implement a single track 3DOF rigid vehicle body to calculate longitudinal, lateral, and yaw motion

**Note**

Simulating models with the Bicycle Model block requires
Simulink®
3D Animation™.

The Bicycle Model block implements a rigid two-axle single track
vehicle body model to calculate longitudinal, lateral, and yaw motion. The block
accounts for body mass, aerodynamic drag, and weight distribution between the axles due
to acceleration and steering. There are two types of Bicycle Model
blocks.

| Block | Implementation |
| --- | --- |
| Bicycle Model - Velocity InputBicycle model block with velocity input ports WhlAngF and xdotin. | - Block assumes that the external longitudinal velocity   is quasi-steady state so the longitudinal acceleration   is approximately zero. - Since the motion is quasi-steady, the block calculates   only lateral forces using the tire slip angles and   linear cornering stiffness. |
| Bicycle Model - Force InputBicycle model block with force input ports WhlAngF, FxF and FxR. | - Block uses the external longitudinal force to   accelerate or brake the vehicle. - Block calculates lateral forces using the tire slip   angles and linear cornering stiffness. |

To calculate the normal forces on the front and rear axles, the
block uses rigid-body vehicle motion, suspension system forces, and wind and drag forces. The
block resolves the force and moment components on the rigid vehicle body frame.
