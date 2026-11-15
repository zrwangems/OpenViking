---
type: simulink-block
title: 'Vehicle Body 1DOF Longitudinal'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Motion'
documentation_page: 'vehiclebody1doflongitudinal'
documentation_source_path: 'ref/vehiclebody1doflongitudinal.html'
language: en
---

# Vehicle Body 1DOF Longitudinal

## Ports

### Input

### **FExt** — External force on vehicle CG `array`

External forces applied to vehicle CG,
*Fxext*,
*Fyext*,
*Fzext*, in
vehicle-fixed frame, in N. Signal vector dimensions are
`[1x3]` or `[3x1]`.

#### Dependencies

To enable this port, select **External
forces**.

### **MExt** — External moment about vehicle CG `array`

External moment about vehicle CG,
*Mx*,
*My*,
*Mz*, in the
vehicle-fixed frame, in N·m. Signal vector dimensions are
`[1x3]` or `[3x1]`.

#### Dependencies

To enable this port, select **External
moments**.

### **FwF** — Total longitudinal force on front axle `scalar`

Longitudinal force on the front axle,
*Fxf*, along
vehicle-fixed `x`-axis, in N.

### **FwR** — Total longitudinal force on rear axle `scalar`

Longitudinal force on the rear axle,
*FwR*, along
vehicle-fixed `x`-axis, in N.

### **Grade** — Road grade angle `scalar`

Road grade angle, γ, in deg.

### **WindX** — Longitudinal wind speed `scalar`

Longitudinal wind speed, *Ww*,
along earth-fixed `X`-axis, in m/s.

#### Dependencies

To enable this port, clear **Wind X,Y,Z
components**.

### **WindXYZ** — Wind speed `array`

Wind speed, *Ww*,
*WwY*,
*WwZ* along inertial
*X*-, *Y*-, and
*Z*-axes, in m/s. Signal vector dimensions are
`[1x3]` or `[3x1]`.

#### Dependencies

To enable this port, select **Wind X,Y,Z
components**.

### **AirTemp** — Ambient air temperature `scalar`

Ambient air temperature,
*Tair*, in K. Considering
this option if you want to vary the temperature during run-time.

#### Dependencies

To enable this port, select **Air
temperature**.
### Output

### **Info** — Bus signal bus

Bus signal containing these block values.

| Signal | | | | | Description | Value | Units |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `InertFrm` | `Cg` | `Disp` | `X` | | Vehicle CG displacement along earth-fixed `X`-axis | Computed relative to the road grade. | m |
| `Y` | | Vehicle CG displacement along earth-fixed `Y`-axis | `0` | m |
| `Z` | | Vehicle CG displacement along earth-fixed `Z`-axis | Computed relative to the road grade. | m |
| `Vel` | `Xdot` | | Vehicle CG velocity along earth-fixed `X`-axis | Computed relative to the road grade. | m/s |
| `Ydot` | | Vehicle CG velocity along earth-fixed `Y`-axis | `0` | m/s |
| `Zdot` | | Vehicle CG velocity along earth-fixed `Z`-axis | Computed relative to the road grade. | m/s |
| `Ang` | `phi` | | Rotation of vehicle-fixed frame about the earth-fixed `X`-axis (roll) | `0` | rad |
| `theta` | | Rotation of vehicle-fixed frame about the earth-fixed `Y`-axis (pitch) | Computed relative to the grade angle. | rad |
| `psi` | | Rotation of vehicle-fixed frame about the earth-fixed `Z`-axis (yaw) | `0` | rad |
| `FrntAxl` | `Disp` | `X` | | Front axle displacement along the earth-fixed `X`-axis | Computed | m |
| `Y` | | Front axle displacement along the earth-fixed `Y`-axis | `0` | m |
| `Z` | | Front axle displacement along the earth-fixed `Z`-axis | Computed | m |
| `Vel` | `Xdot` | | Front axle velocity along the earth-fixed `X`-axis | Computed | m/s |
| `Ydot` | | Front axle velocity along the earth-fixed `Y`-axis | `0` | m/s |
| `Zdot` | | Front axle velocity along the earth-fixed `Z`-axis | Computed | m/s |
| `RearAxl` | `Disp` | `X` | | Rear axle displacement along the earth-fixed `X`-axis | Computed | m |
| `Y` | | Rear axle displacement along the earth-fixed `Y`-axis | `0` | m |
| `Z` | | Rear axle displacement along the earth-fixed `Z`-axis | Computed | m |
| `Vel` | `Xdot` | | Rear axle velocity along the earth-fixed `X`-axis | Computed | m/s |
| `Ydot` | | Rear axle velocity along the earth-fixed `Y`-axis | `0` | m/s |
| `Zdot` | | Rear axle velocity along the earth-fixed `Z`-axis | Computed | m/s |
| `BdyFrm` | `Cg` | `Disp` | `x` | | Vehicle CG displacement along the vehicle-fixed `x`-axis | Computed | m |
| `y` | | Vehicle CG displacement along the vehicle-fixed `y`-axis | `0` | m |
| `z` | | Vehicle CG displacement along the vehicle-fixed `z`-axis | `0` | m |
| `Vel` | `xdot` | | Vehicle CG velocity along the vehicle-fixed `x`-axis | Computed | m/s |
| `ydot` | | Vehicle CG velocity along the vehicle-fixed `y`-axis | `0` | m/s |
| `zdot` | | Vehicle CG velocity along the vehicle-fixed `z`-axis | `0` | m/s |
| `AngVel` | `p` | | Vehicle angular velocity about the vehicle-fixed `x`-axis (roll rate) | `0` | rad/s |
| `q` | | Vehicle angular velocity about the vehicle-fixed y-axis (pitch rate) | `0` | rad/s |
| `r` | | Vehicle angular velocity about the vehicle-fixed z-axis (yaw rate) | `0` | rad/s |
| `Accel` | `ax` | | Vehicle CG inertial acceleration along the vehicle-fixed *x*-axis | Computed | gn |
| `ay` | | Vehicle CG inertial acceleration along the vehicle-fixed *y*-axis | `0` | gn |
| `az` | | Vehicle CG inertial acceleration along the vehicle-fixed *z*-axis | `0` | gn |
| `xddot` | | Vehicle CG acceleration along the vehicle-fixed *x*-axis, excluding the centrifugal component | Computed | m/s^2 |
| `yddot` | | Vehicle CG acceleration along the vehicle-fixed *y*-axis, excluding the centrifugal component | Computed | m/s^2 |
| `zddot` | | Vehicle CG acceleration along the vehicle-fixed *z*-axis, excluding the centrifugal component. | `0` | m/s^2 |
| `Forces` | `Body` | `Fx` | | Net force on vehicle CG along the vehicle-fixed `x`-axis | `0` | N |
| `Fy` | | Net force on vehicle CG along the vehicle-fixed `y`-axis | `0` | N |
| `Fz` | | Net force on vehicle CG along the vehicle-fixed `z`-axis | `0` | N |
| `Ext` | `Fx` | | External force on vehicle CG along the vehicle-fixed `x`-axis | `Computed` | N |
| `Fy` | | External force on vehicle CG along the vehicle-fixed `y`-axis | `Computed` | N |
| `Fz` | | External force on vehicle CG along the vehicle-fixed `z`-axis | `Computed` | N |
| `FrntAxl` | `Fx` | | Longitudinal force on front axle, along the vehicle-fixed `x`-axis | `0` | N |
| `Fy` | | Lateral force on front axle, along the vehicle-fixed `y`-axis | `0` | N |
| `Fz` | | Normal force on front axle, along the vehicle-fixed `z`-axis | Computed | N |
| `RearAxl` | `Fx` | | Longitudinal force on rear axle, along the vehicle-fixed `x`-axis | `0` | N |
| `Fy` | | Lateral force on rear axle, along the vehicle-fixed `y`-axis | `0` | N |
| `Fz` | | Normal force on rear axle, along the vehicle-fixed `z`-axis | Computed | N |
| `Tires` | `FrntTire` | `Fx` | Front tire force, along the vehicle-fixed `x`-axis | `0` | N |
| `Fy` | Front tire force, along the vehicle-fixed `y`-axis | `0` | N |
| `Fz` | Front tire force, along the vehicle-fixed `z`-axis | Computed | N |
| `RearTire` | `Fx` | Rear tire force, along the vehicle-fixed `x`-axis | `0` | N |
| `Fy` | Rear tire force, along the vehicle-fixed `y`-axis | `0` | N |
| `Fz` | Rear tire force, along the vehicle-fixed `z`-axis | Computed | N |
| `Drag` | `Fx` | | Drag force on vehicle CG along the vehicle-fixed `x`-axis | Computed | N |
| `Fy` | | Drag force on vehicle CG along the vehicle-fixed `y`-axis | Computed | N |
| `Fz` | | Drag force on vehicle CG along the vehicle-fixed `z`-axis | Computed | N |
| `Grvty` | `Fx` | | Gravity force on vehicle CG along the vehicle-fixed `x`-axis | Computed | N |
| `Fy` | | Gravity force on vehicle CG along the vehicle-fixed `y`-axis | `0` | N |
| `Fz` | | Gravity force on vehicle CG along the vehicle-fixed `z`-axis | Computed | N |
| `Moments` | `Body` | `Mx` | | Net moment on vehicle CG about the vehicle-fixed `x`-axis | `0` | N·m |
| `My` | | Net moment on vehicle CG about the vehicle-fixed `y`-axis | `0` | N·m |
| `Mz` | | Net moment on vehicle CG about the vehicle-fixed `z`-axis | `0` | N·m |
| `Drag` | `Mx` | | Drag moment on vehicle CG about the vehicle-fixed `x`-axis | Computed | N·m |
| `My` | | Drag moment on vehicle CG about the vehicle-fixed `y`-axis | Computed | N·m |
| `Mz` | | Drag moment on vehicle CG about the vehicle-fixed `z`-axis | Computed | N·m |
| `Ext` | `Fx` | | External moment on vehicle CG about the vehicle-fixed `x`-axis | `Computed` | N·m |
| `Fy` | | External moment on vehicle CG about the vehicle-fixed `y`-axis | `Computed` | N·m |
| `Fz` | | External moment on vehicle CG about the vehicle-fixed `z`-axis | `Computed` | N·m |
| `FrntAxl` | `Disp` | `x` | | Front axle displacement along the vehicle-fixed `x`-axis | Computed | m |
| `y` | | Front axle displacement along the vehicle-fixed `y`-axis | `0` | m |
| `z` | | Front axle displacement along the vehicle-fixed `z`-axis | Computed | m |
| `Vel` | `xdot` | | Front axle velocity along the vehicle-fixed `x`-axis | Computed | m/s |
| `ydot` | | Front axle velocity along the vehicle-fixed `y`-axis | `0` | m/s |
| `zdot` | | Front axle velocity along the vehicle-fixed `z`-axis | Computed | m/s |
| `Steer` | `WhlAngFL` | | Front left wheel steering angle | Computed | rad |
| `WhlAngFR` | | Front right wheel steering angle | Computed | rad |
| `RearAxl` | `Disp` | `x` | | Rear axle displacement along the vehicle-fixed `x`-axis | Computed | m |
| `y` | | Rear axle displacement along the vehicle-fixed `y`-axis | `0` | m |
| `z` | | Rear axle displacement along the vehicle-fixed `z`-axis | Computed | m |
| `Vel` | `xdot` | | Rear axle velocity along the vehicle-fixed `x`-axis | Computed | m/s |
| `ydot` | | Rear axle velocity along the vehicle-fixed `y`-axis | `0` | m/s |
| `zdot` | | Rear axle velocity along the vehicle-fixed `z`-axis | Computed | m/s |
| `Steer` | `WhlAngRL` | | Rear left wheel steering angle | Computed | rad |
| `WhlAngRR` | | Rear right wheel steering angle | Computed | rad |
| `Pwr` | `PwrExt` | | | Applied external power | Computed | W |
| `Drag` | | | Power loss due to drag | Computed | W |
| `PwrInfo` | `PwrTrnsfrd` | `PwrFxExt` | | | Externally applied force power | Computed | W |
| `PwrFwFx` | | | Longitudinal force power applied at the front axle | Computed | W |
| `PwrFwRx` | | | Longitudinal force power applied at the rear axle | Computed | W |
| `PwrNotTrnsfrd` | `PwrFxDrag` | | | Drag force power | Computed | W |
| `PwrStored` | `wrStoredGrvty` | | | Rate change in gravitational potential energy | Computed | W |
| `PwrStoredxdot` | | | Rate in change of longitudinal kinetic energy | Computed | W |

### **xdot** — Vehicle body longitudinal velocity `scalar`

Vehicle body longitudinal velocity along the vehicle-fixed reference
frame `x`-axis, in m/s.

### **FzF** — Normal force on front wheels `scalar`

Normal force on single wheel of front wheels,
*Fzf*, along
vehicle-fixed `z`-axis, in N.

### **FzR** — Normal force on rear wheels `scalar`

Normal force on single wheel of rear wheels,
*Fzr*, along the
vehicle-fixed `z`-axis, in N.

## Parameters

#### Options

### **External forces** — `FExt` input port `off` (default) | `on`

Specify to create input port `FExt`.

### **External moments** — `MExt` input port `off` (default) | `on`

Specify to create input port `MExt`.

### **Air temperature** — `AirTemp` input port `off` (default) | `on`

Specify to create input port `AirTemp`.

### **Wind X,Y,Z components** — `WindXYZ` input port `off` (default) | `on`

Specify to create input port `WindXYZ`.

#### Longitudinal

### **Number of wheels on front axle, NF** — Front wheel count `2` (default) | `scalar`

Number of wheels on front axle,
*NF*. The value is
dimensionless.

### **Number of wheels on rear axle, NR** — Rear wheel count `2` (default) | `scalar`

Number of wheels on rear axle,
*NR*. The value is
dimensionless.

### **Mass, m** — Vehicle mass `1500` (default) | `scalar`

Vehicle mass, *M*, in kg.

### **Horizontal distance from CG to front axle, a** — Front axle distance `1.4` (default) | `scalar`

Horizontal distance *a* from the vehicle CG to the front
wheel axle, in m.

### **Horizontal distance from CG to rear axle, b** — Rear axle distance `1.8` (default) | `scalar`

Horizontal distance *b* from the vehicle CG to the rear
wheel axle, in m.

### **CG height above axles, h** — Height `.35` (default) | `scalar`

Height of vehicle CG above the ground, *h*, in m.

### **Longitudinal drag coefficient, Cd** — Drag `.3` (default) | `scalar`

Air drag coefficient, *Cd*. The
value is dimensionless.

### **Longitudinal lift coefficient, Cl** — Lift `0` (default) | `scalar`

Air lift coefficient, *Cl*. The
value is dimensionless.

### **Longitudinal drag pitch moment, Cpm** — Pitch drag `0` (default) | `scalar`

Pitch drag moment coefficient,
*Cpm*. The value is
dimensionless.

### **Frontal area, Af** — Area `4` (default) | `scalar`

Effective vehicle cross-sectional area, *A*, to calculate
the aerodynamic drag force on the vehicle, in
m2.

### **Initial position, x\_o** — Position `0` (default) | `scalar`

Vehicle body longitudinal initial position along the vehicle-fixed
`x`-axis, *xo*,
in m.

### **Initial velocity, xdot\_o** — Velocity `0` (default) | `scalar`

Vehicle body longitudinal initial velocity along the vehicle-fixed
`x`-axis, x˙0, in m/s.

#### Environment

### **Absolute air pressure, Pabs** — Pressure `101325` (default) | `scalar`

Environmental air absolute pressure, *Pabs*,
in Pa.

### **Air temperature, T** — Ambient air temperature `273` (default) | `scalar`

Ambient air temperature, *Tair*,
in K.

#### Dependencies

To enable this parameter, clear **Air
temperature**.

### **Gravitational acceleration, g** — Gravity `9.81` (default) | `scalar`

Gravitational acceleration, *g*, in
m/s2.

## Libraries

Powertrain Blockset / Vehicle Dynamics Vehicle Dynamics Blockset / Vehicle Body

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Two-axle vehicle in forward and reverse motion

The Vehicle Body 1DOF Longitudinal block implements a one
degree-of-freedom (1DOF) rigid vehicle body with constant mass undergoing longitudinal
(that is, forward and reverse) motion. Use the block:

- In powertrain and fuel economy studies to represent the vehicle inertial
  and drag loads when weight transfer from vertical and pitch motions are
  negligible.
- To determine the engine torque and power required for the vehicle to
  follow a specified drive cycle.

You can select block options to create input ports for external forces, moments, air
temperature, and wind speed.

| Block Option Setting | **External Input Ports** | Description |
| --- | --- | --- |
| **External forces** | `FExt` | External force applied to vehicle CG in the vehicle-fixed frame. |
| **External moments** | `MExt` | External moment about vehicle CG in the vehicle-fixed frame. |
| **Air temperature** | `AirTemp` | Ambient air temperature. Consider this option if you want to vary the temperature during run-time. |
| **Wind X,Y,Z** | `WindXYZ` | Wind speed along earth-fixed *X*-, *Y*-, and *Z*-axes.  If you do not select this option, the block implements input port `WindX` — Longitudinal wind speed along the earth-fixed *X*-axis. |

### Vehicle Body Model

The vehicle axles are parallel and form a plane. The longitudinal direction lies
in this plane and is perpendicular to the axles. If the vehicle is traveling on an
inclined slope, the normal direction is not parallel to gravity but is always
perpendicular to the axle-longitudinal plane.

The block uses the net effect of all the forces and torques acting on it to
determine the vehicle motion. The longitudinal tire forces push the vehicle forward
or backward. The weight of the vehicle acts through its center of gravity (CG). The
grade angle changes the direction of the resolved gravitational force acting on the
vehicle CG. Similarly, the block resolves the resistive aerodynamic drag force on
the vehicle CM.

Vehicle free body force diagram showing forces acting on CM and tires

The Vehicle Body 1DOF Longitudinal block implements these
equations.

Fb=mx¨Fb=FxF+FxR−Fd,x+Fext,x−mgsinγ

Zero normal acceleration and zero pitch torque determine the normal force on each
front and rear axles.

FzF=−Mext,y−Md,y+  b(Fd,z+Fext,z+ mgcosγ)−h(−Fext,x+Fd,x+ mgsinγ+mx¨)NF(a+b) FzR=Mext,y+Md,y+ a(Fd,z+Fext,z+ mgcosγ)+h(−Fext,x+Fd,x+ mgsinγ+mx¨)NR(a+b)

The wheel normal forces satisfy this equation.

NFFzF+NRFzR−Fext,z=mgcosγ

### Wind and Drag Forces

The block subtracts the wind speeds from the vehicle velocity components to obtain
a net relative airspeed. To calculate the drag force and moments acting on the
vehicle, the block uses the net relative airspeed.

Fd,x=12TRCdAfPabs(x˙−wx)2Fd,z=12TRClAfPabs(x˙−wx)2Md,y=12TRCpmAfPabs(x˙−wx)2(a+b)

By default, to calculate the wind speed along the vehicle-fixed
*x*-axis, the block uses the longitudinal wind speed along
the earth-fixed *X*-axis. If you select
**WindX,Y,Z**, the block uses the wind speed along the
earth-fixed *X*-, *Y*-, *Z*-axes.

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrFxExt` | Externally applied force power | PFxExt=FxExtx˙ |
| `PwrFwFx` | Longitudinal force power applied at the front axle | PFwFx=FwFx˙ |
| `PwrFwRx` | Longitudinal force power applied at the rear axle | PFwRx=FwRx˙ |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrFxDrag` | Drag force power | Pd=−0.5CdAfPabs(x˙2−wx)2287.058Tx˙ |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `wrStoredGrvty` | Rate change in gravitational potential energy | Pg=−mgZ˙ |
| `PwrStoredxdot` | Rate in change of longitudinal kinetic energy | Px˙=mx¨x˙ |

The equations use these variables.

|  |  |
| --- | --- |
| *Fxf*, *Fxr* | Longitudinal forces on each wheel at the front and rear ground contact points, respectively |
| *Fzf*, *Fzr* | Normal load forces on each wheel at the front and rear ground contact points, respectively |
| *FwF*, *FwR* | Longitudinal force on front and rear axles along vehicle-fixed *x*-axis |
| *FxExt*, *FwR* | External force along the vehicle-fixed *x*-axis |
| *Fd,x*, *Fd,z* | Longitudinal and normal drag force on vehicle CG |
| *Md,y* | Torque due to drag on vehicle about the vehicle-fixed *y*-axis |
| *Fd* | Aerodynamic drag force |
| *Vx* | Velocity of the vehicle. When *Vx* > 0, the vehicle moves forward. When *Vx* < 0, the vehicle moves backward. |
| *Nf*, *Nr* | Number of wheels on front and rear axle, respectively |
| γ | Angle of road grade |
| *m* | Vehicle body mass |
| *a*,*b* | Distance of front and rear axles, respectively, from the normal projection point of vehicle CG onto the common axle plane |
| *h* | Height of vehicle CG above the axle plane |
| *Cd* | Frontal air drag coefficient |
| *Af* | Frontal area |
| *Pabs* | Absolute pressure |
| *ρ* | Mass density of air |
| *x*, x˙, x¨ | Vehicle longitudinal position, velocity, and acceleration along the vehicle-fixed *x*-axis |
| *wx* | Wind speed along the vehicle-fixed *x*-axis |
| Z˙ | Vehicle vertical velocity along the vehicle-fixed *z*-axis |
