---
type: simulink-block
title: 'Vehicle Body 3DOF Longitudinal'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Body'
documentation_page: 'vehiclebody3doflongitudinal'
documentation_source_path: 'ref/vehiclebody3doflongitudinal.html'
language: en
---

# Vehicle Body 3DOF Longitudinal

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

### **FwF** — Total longitudinal force on the front axle `scalar`

Longitudinal force on the front axle,
*FwF*, along
vehicle-fixed *x*-axis, in N.

### **FwR** — Total longitudinal force on the rear axle `scalar`

Longitudinal force on the rear axle,
*FwR*, along
vehicle-fixed *x*-axis, in N.

### **Grade** — Road grade angle `scalar`

Road grade angle, γ, in deg.

### **FsF** — Suspension force on front axle per wheel `vector`

Suspension force on front axle,
*FsF*, along the
vehicle-fixed *z*-axis, in N.

#### Dependencies

To enable this port, for the **Ground interaction
type** parameter, select `External
suspension`.

### **FsR** — Suspension force on rear axle per wheel `vector`

Suspension force on rear axle,
*FsR*, along the
vehicle-fixed *z*-axis, in N.

#### Dependencies

To enable this port, for the **Ground interaction
type** parameter, select `External
suspension`.

### **WindXYZ** — Wind speed `array`

Wind speed, *WX*,
*WY*,
*WZ* along earth-fixed
*X*-, *Y*-, and
*Z*-axes, in m/s. Signal vector dimensions are
`[1x3]` or `[3x1]`.

### **AirTemp** — Ambient air temperature `scalar`

Ambient air temperature,
*Tair*, in K. Considering
this option if you want to vary the temperature during run-time.

#### Dependencies

To enable this port, select **Air
temperature**.

### **zF,R** — Forward and rear axle positions `vector`

Forward and rear axle positions along the vehicle-fixed
*z*-axis, Z¯F,Z¯R, in m.

#### Dependencies

To enable this port, for the **Ground interaction
type** parameter, select `Axle
displacement, velocity`.

### **zdotF,R** — Forward and rear axle velocities `vector`

Forward and rear axle velocities along the vehicle-fixed
*z*-axis, Z¯˙F,Z¯˙R, in m/s.

#### Dependencies

To enable this port, for the **Ground interaction
type** parameter, select `Axle
displacement, velocity`.
### Output

### **Info** — Bus signal bus

Bus signal containing these block values.

| Signal | | | | | Description | Value | Units |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `InertFrm` | `Cg` | `Disp` | `X` | | Vehicle CG displacement along earth-fixed *X*-axis | Computed | m |
| `Y` | | Vehicle CG displacement along earth-fixed *Y*-axis | `0` | m |
| `Z` | | Vehicle CG displacement along earth-fixed *Z*-axis | Computed | m |
| `Vel` | `Xdot` | | Vehicle CG velocity along earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | Vehicle CG velocity along earth-fixed *Y*-axis | `0` | m/s |
| `Zdot` | | Vehicle CG velocity along earth-fixed *Z*-axis | Computed | m/s |
| `Ang` | `phi` | | Rotation of vehicle-fixed frame about the earth-fixed *X*-axis (roll) | `0` | rad |
| `theta` | | Rotation of vehicle-fixed frame about the earth-fixed *Y*-axis (pitch) | Computed | rad |
| `psi` | | Rotation of vehicle-fixed frame about the earth-fixed *Z*-axis (yaw) | `0` | rad |
| `FrntAxl` | `Disp` | `X` | | Front axle displacement along the earth-fixed *X*-axis | Computed | m |
| `Y` | | Front axle displacement along the earth-fixed *Y*-axis | `0` | m |
| `Z` | | Front axle displacement along the earth-fixed *Z*-axis | Computed | m |
| `Vel` | `Xdot` | | Front axle velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | Front axle velocity along the earth-fixed *Y*-axis | `0` | m/s |
| `Zdot` | | Front axle velocity along the earth-fixed *Z*-axis | Computed | m/s |
| `RearAxl` | `Disp` | `X` | | Rear axle displacement along the earth-fixed *X*-axis | Computed | m |
| `Y` | | Rear axle displacement along the earth-fixed *Y*-axis | `0` | m |
| `Z` | | Rear axle displacement along the earth-fixed *Z*-axis | Computed | m |
| `Vel` | `Xdot` | | Rear axle velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | Rear axle velocity along the earth-fixed *Y*-axis | `0` | m/s |
| `Zdot` | | Rear axle velocity along the earth-fixed *Z*-axis | Computed | m/s |
| `BdyFrm` | `Cg` | `Disp` | `x` | | Vehicle CG displacement along the vehicle-fixed *x*-axis | Computed | m |
| `y` | | Vehicle CG displacement along the vehicle-fixed *y*-axis | `0` | m |
| `z` | | Vehicle CG displacement along the vehicle-fixed *z*-axis | Computed | m |
| `Vel` | `xdot` | | Vehicle CG velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Vehicle CG velocity along the vehicle-fixed *y*-axis | `0` | m/s |
| `zdot` | | Vehicle CG velocity along the vehicle-fixed *z*-axis | Computed | m/s |
| `AngVel` | `p` | | Vehicle angular velocity about the vehicle-fixed *x*-axis (roll rate) | `0` | rad/s |
| `q` | | Vehicle angular velocity about the vehicle-fixed y-axis (pitch rate) | Computed | rad/s |
| `r` | | Vehicle angular velocity about the vehicle-fixed *z*-axis (yaw rate) | `0` | rad/s |
| `Accel` | `ax` | | Vehicle CG acceleration along the vehicle-fixed *x*-axis | Computed | gn |
| `ay` | | Vehicle CG acceleration along the vehicle-fixed *y*-axis | `0` | gn |
| `az` | | Vehicle CG acceleration along the vehicle-fixed *z*-axis | Computed | gn |
| `Forces` | `Body` | `Fx` | | Net force on vehicle CG along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Net force on vehicle CG along the vehicle-fixed *y*-axis | `0` | N |
| `Fz` | | Net force on vehicle CG along the vehicle-fixed *z*-axis | Computed | N |
| `Ext` | `Fx` | | External force on vehicle CG along the vehicle-fixed *x*-axis | `Computed` | N |
| `Fy` | | External force on vehicle CG along the vehicle-fixed *y*-axis | `Computed` | N |
| `Fz` | | External force on vehicle CG along the vehicle-fixed *z*-axis | `Computed` | N |
| `FrntAxl` | `Fx` | | Longitudinal force on front axle, along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on front axle, along the vehicle-fixed *y*-axis | `0` | N |
| `Fz` | | Normal force on front axle, along the vehicle-fixed *z*-axis | Computed | N |
| `RearAxl` | `Fx` | | Longitudinal force on rear axle, along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on rear axle, along the vehicle-fixed *y*-axis | `0` | N |
| `Fz` | | Normal force on rear axle, along the vehicle-fixed *z*-axis | Computed | N |
| `Tires` | `FrntTire` | `Fx` | Front tire force, along the vehicle-fixed *x*-axis | `0` | N |
| `Fy` | Front tire force, along the vehicle-fixed *y*-axis | `0` | N |
| `Fz` | Front tire force, along the vehicle-fixed *z*-axis | Computed | N |
| `RearTire` | `Fx` | Rear tire force, along the vehicle-fixed *x*-axis | `0` | N |
| `Fy` | Rear tire force, along the vehicle-fixed *y*-axis | `0` | N |
| `Fz` | Rear tire force, along the vehicle-fixed *z*-axis | Computed | N |
| `Drag` | `Fx` | | Drag force on vehicle CG along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Drag force on vehicle CG along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Drag force on vehicle CG along the vehicle-fixed *z*-axis | Computed | N |
| `Grvty` | `Fx` | | Gravity force on vehicle CG along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Gravity force on vehicle CG along the vehicle-fixed *y*-axis | `0` | N |
| `Fz` | | Gravity force on vehicle CG along the vehicle-fixed *z*-axis | Computed | N |
| `Moments` | `Body` | `Mx` | | Body moment on vehicle CG about the vehicle-fixed *x*-axis | `0` | N·m |
| `My` | | Body moment on vehicle CG about the vehicle-fixed *y*-axis | Computed | N·m |
| `Mz` | | Body moment on vehicle CG about the vehicle-fixed *z*-axis | `0` | N·m |
| `Drag` | `Mx` | | Drag moment on vehicle CG about the vehicle-fixed *x*-axis | `0` | N·m |
| `My` | | Drag moment on vehicle CG about the vehicle-fixed *y*-axis | Computed | N·m |
| `Mz` | | Drag moment on vehicle CG about the vehicle-fixed *z*-axis | `0` | N·m |
| `Ext` | `Fx` | | External moment on vehicle CG about the vehicle-fixed *x*-axis | `Computed` | N·m |
| `Fy` | | External moment on vehicle CG about the vehicle-fixed *y*-axis | `Computed` | N·m |
| `Fz` | | External moment on vehicle CG about the vehicle-fixed *z*-axis | `Computed` | N·m |
| `FrntAxl` | `Disp` | `x` | | Front axle displacement along the vehicle-fixed *x*-axis | Computed | m |
| `y` | | Front axle displacement along the vehicle-fixed *y*-axis | `0` | m |
| `z` | | Front axle displacement along the vehicle-fixed *z*-axis | Computed | m |
| `Vel` | `xdot` | | Front axle velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Front axle velocity along the vehicle-fixed *y*-axis | `0` | m/s |
| `zdot` | | Front axle velocity along the vehicle-fixed *z*-axis | Computed | m/s |
| `Steer` | `WhlAngFL` | | Front left wheel steering angle | Computed | rad |
| `WhlAngFR` | | Front right wheel steering angle | Computed | rad |
| `RearAxl` | `Disp` | `x` | | Rear axle displacement along the vehicle-fixed *x*-axis | Computed | m |
| `y` | | Rear axle displacement along the vehicle-fixed *y*-axis | `0` | m |
| `z` | | Rear axle displacement along the vehicle-fixed *z*-axis | Computed | m |
| `Vel` | `xdot` | | Rear axle velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Rear axle velocity along the vehicle-fixed *y*-axis | `0` | m/s |
| `zdot` | | Rear axle velocity along the vehicle-fixed *z*-axis | Computed | m/s |
| `Steer` | `WhlAngRL` | | Rear left wheel steering angle | Computed | rad |
| `WhlAngRR` | | Rear right wheel steering angle | Computed | rad |
| `Pwr` | `PwrExt` | | | Applied external power | Computed | W |
| `Drag` | | | Power loss due to drag | Computed | W |
| `PwrInfo` | `PwrTrnsfrd` | `PwrFxExt` | | | Externally applied longitudinal force power | Computed | W |
| `PwrFzExt` | | | Externally applied longitudinal force power | Computed | W |
| `PwrMyExt` | | | Externally applied pitch moment power | Computed | W |
| `PwrFwFx` | | | Longitudinal force applied at the front axle | Computed | W |
| `PwrFwRx` | | | Longitudinal force applied at the rear axle | Computed | W |
| `PwrNotTrnsfrd` | `PwrFsF` | | | Internal power transferred between suspension and vehicle body at the front axle | Computed | W |
| `PwrFsR` | | | Internal power transferred between suspension and vehicle body at the rear axle | Computed | W |
| `PwrFxDrag` | | | Longitudinal drag force power | Computed | W |
| `PwrFzDrag` | | | Vertical drag force power | Computed | W |
| `PwrMyDrag` | | | Drag pitch moment power | Computed | W |
| `PwrFsb` | | | Total suspension damping power | Computed | W |
| `PwrStored` | `PwrStoredGrvty` | | | Rate change in gravitational potential energy | Computed | W |
| `PwrStoredxdot` | | | Rate of change of longitudinal kinetic energy | Computed | W |
| `PwrStoredzdot` | | | Rate of change of longitudinal kinetic energy | Computed | W |
| `PwrStoredq` | | | Rate of change of rotational pitch kinetic energy | Computed | W |
| `PwrStoredFsFzSprng` | | | Stored spring energy from front suspension | Computed | W |
| `PwrStoredFsRzSprng` | | | Stored spring energy from rear suspension | Computed | W |

### **xdot** — Vehicle longitudinal velocity `scalar`

Vehicle CG velocity along the vehicle-fixed
*x*-axis, in m/s.

### **FzF** — Normal force on front wheels `scalar`

Normal force on single wheel of front wheels,
*FzF*, along the
vehicle-fixed *z*-axis, in N.

### **FzR** — Normal force on rear wheels `scalar`

Normal force on single wheel of rear wheels,
*FzR*, along the
vehicle-fixed *z*-axis, in N.

## Parameters

#### Options

### **Ground interaction type** — Axle attachment to the vehicle `Grade angle` (default) | `Axle displacement, velocity` | `External suspension`

Specify the type of axle attachment to the vehicle:

- `Grade angle` — Vertical axle
  displacement from road surface to axles remains constant. The
  block uses tabular stiffness and damping parameters to model the
  suspension forces acting between the vehicle body and
  axles.
- `Axle displacement, velocity`
  — Axles have input-provided vertical displacement and
  velocity with respect to the road grade. The block uses tabular
  stiffness and damping parameters to model the suspension forces
  acting between the vehicle body and axle.
- `External suspension` — Axles
  have externally applied forces for coupling the vehicle body to
  custom suspension models.

### **External forces** — `FExt` input port `off` (default) | `on`

Specify to create input port `FExt`.

### **External moments** — `MExt` input port `off` (default) | `on`

Specify to create input port `MExt`.

### **Air temperature** — `AirTemp` input port `off` (default) | `on`

Specify to create input port `AirTemp`.

#### Longitudinal

### **Number of wheels on front axle, NF** — Front wheel count `2` (default) | `scalar`

Number of wheels on front axle,
*NF*. The value is
dimensionless.

### **Number of wheels on rear axle, NR** — Rear wheel count `2` (default) | `scalar`

Number of wheels on rear axle,
*NR*. The value is
dimensionless.

### **Mass, m** — Vehicle mass `1200` (default) | `scalar`

Vehicle mass, *m*, in kg.

### **Horizontal distance from CG to front axle, a** — Front axle distance `1.4` (default) | `scalar`

Horizontal distance *a* from the vehicle CG to the front
wheel axle, in m.

### **Horizontal distance from CG to rear axle, b** — Rear axle distance `1.8` (default) | `scalar`

Horizontal distance *b* from the vehicle CG to the rear
wheel axle, in m.

### **CG height above axles, h** — Height `0.35` (default) | `scalar`

Height of vehicle CG above the axles, *h*, in m.

### **Longitudinal drag coefficient, Cd** — Drag `.3` (default) | `scalar`

Air drag coefficient, *Cd*. The
value is dimensionless.

### **Frontal area, Af** — Area `2` (default) | `scalar`

Effective vehicle cross-sectional area,
*Af* to calculate the
aerodynamic drag force on the vehicle, in m^2.

### **Initial position, x\_o** — Position `0` (default) | `scalar`

Vehicle body longitudinal initial position along earth-fixed
*x*-axis,
*xo*, in m.

### **Initial velocity, xdot\_o** — Velocity `0` (default) | `scalar`

Vehicle body longitudinal initial velocity along earth-fixed
*x*-axis, x˙0, in m/s.

#### Vertical

### **Longitudinal lift coefficient, Cl** — Lift `.1` (default) | `scalar`

Lift coefficient, *Cl*. The value
is dimensionless.

### **Initial vertical position, z\_o** — Position `-.35` (default) | `scalar`

Initial vertical CG position,
*zo*, along the vehicle-fixed
*z*-axis, in m.

### **Initial vertical velocity, zdot\_o** — Velocity `0` (default) | `scalar`

Initial vertical CG velocity,
*zdoto*, along the vehicle-fixed
*z*-axis, in m.

#### Pitch

### **Inertia, Iyy** — About body `y`-axis `3500` (default) | `scalar`

Vehicle body moment of inertia about body
*z*-axis.

### **Longitudinal drag pitch moment, Cpm** — Drag coefficient `.1` (default) | `scalar`

Pitch drag moment coefficient. The value is dimensionless.

### **Initial pitch angle, theta\_o** — Pitch `0` (default) | `scalar`

Initial pitch angle about body *z*-axis, in rad.

### **Initial angular velocity, q\_o** — Pitch velocity `0` (default) | `scalar`

Initial vehicle body angular velocity about body
*z*-axis, in rad/s.

#### Suspension

### **Front axle stiffness force data, FskF** — Force `[-50, -1, 0, 2, 3, 52].*1.5e4` (default) | `vector`

Front axle stiffness force data,
*FkF*, in N.

#### Dependencies

To enable this parameter, for the **Ground interaction
type** parameter, select `Grade
angle` or `Axle displacement,
velocity`.

### **Front axle displacement data, dzsF** — Displacement `[-5e-3, -1e-4, 0, .2, .2001, .2051]` (default) | `vector`

Front axle displacement data, in m.

#### Dependencies

To enable this parameter, for the **Ground interaction
type** parameter, select `Grade
angle` or `Axle displacement,
velocity`.

### **Front axle damping force data, FsbF** — Damping force `[-10000 -100 -10 0 10 100 10000]` (default) | `vector`

Front axle damping force, in N.

#### Dependencies

To enable this parameter, for the **Ground interaction
type** parameter, select `Grade
angle` or `Axle displacement,
velocity`.

### **Front axle velocity data, dzdotsF** — Velocity `[-10 -1 -.1 0 .1 1 10]` (default) | `vector`

Front axle velocity data, in m/s.

#### Dependencies

To enable this parameter, for the **Ground interaction
type** parameter, select `Grade
angle` or `Axle displacement,
velocity`.

### **Rear axle stiffness force data, FskR** — Force `[-50, -1, 0, 2, 3, 52].*1e4` (default) | `vector`

Rear axle stiffness force data, in N.

#### Dependencies

To enable this parameter, for the **Ground interaction
type** parameter, select `Grade
angle` or `Axle displacement,
velocity`.

### **Rear axle displacement data, dzsR** — Displacement `[-5e-3, -1e-4, 0, .2, .2001, .2051]` (default) | `vector`

Rear axle displacement data, in m.

#### Dependencies

To enable this parameter, for the **Ground interaction
type** parameter, select `Grade
angle` or `Axle displacement,
velocity`.

### **Rear axle damping force data, FsbR** — Damping force `[-10000 -100 -10 0 10 100 10000]` (default) | `vector`

Rear axle damping force, in N.

#### Dependencies

To enable this parameter, for the **Ground interaction
type** parameter, select `Grade
angle` or `Axle displacement,
velocity`.

### **Rear axle velocity data, dzdotsR** — Velocity `[-10 -1 -.1 0 .1 1 10]` (default) | `vector`

Rear axle velocity data, in m/s.

#### Dependencies

To enable this parameter, for the **Ground interaction
type** parameter, select `Grade
angle` or `Axle displacement,
velocity`.

#### Environment

### **Absolute air pressure, Pabs** — Pressure `101325` (default) | `scalar`

Environmental air absolute pressure, *Pabs*,
in Pa.

### **Air temperature, Tair** — Ambient air temperature `273` (default) | `scalar`

Ambient air temperature, *Tair*, in K.

#### Dependencies

To enable this parameter, clear **Air temperature**.

### **Gravitational acceleration, g** — Gravity `9.81` (default)

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

3DOF rigid vehicle body to calculate longitudinal, vertical, and pitch motion

The Vehicle Body 3DOF Longitudinal block implements a three
degrees-of-freedom (3DOF) rigid vehicle body model with configurable axle stiffness to
calculate longitudinal, vertical, and pitch motion. The block accounts for body mass,
aerodynamic drag, road incline, and weight distribution between the axles due to
acceleration and the road profile.

You can specify the type of axle attachment to the vehicle:

- Grade angle — Vertical axle displacement from road surface to axles
  remains constant. The block uses tabular stiffness and damping parameters to
  model the suspension forces acting between the vehicle body and
  axles.
- Axle displacement — Axles have input-provided vertical displacement
  and velocity with respect to the road grade. The block uses tabular
  stiffness and damping parameters to model the suspension forces acting
  between the vehicle body and axle.
- External suspension — Axles have externally applied forces for
  coupling the vehicle body to custom suspension models.

If the weight transfer from vertical and pitch motions are not negligible, consider
using this block to represent vehicle motion in powertrain and fuel economy studies. For
example, in studies with heavy breaking or acceleration or road profiles that contain
larger vertical changes.

The block uses rigid-body vehicle motion, suspension system forces, and wind and drag
forces to calculate the normal forces on the front and rear axles. The block resolves
the force components and moments on the rigid vehicle body frame:

Fx=FwF+FwR−Fd,x−Fsx,F−Fsx,R+Fg,xFz=Fd,z−Fsz,F−Fsz,R+Fg,zMy=aFsz,F−bFsz,R+h(FwF+FwR+Fsx,F+Fsx,R)−Md,y

Inclined vehicle diagram

### Rigid-Body Vehicle Motion

The vehicle axles are parallel and form a plane. The longitudinal direction lies
in this plane and is perpendicular to the axles. If the vehicle is traveling on an
inclined slope, the normal direction is not parallel to gravity but is always
perpendicular to the axle-longitudinal plane.

The block uses the net effect of all the forces and torques acting on it to
determine the vehicle motion. The longitudinal tire forces push the vehicle forward
or backward. The weight of the vehicle acts through its center of gravity (CG).
Depending on the inclined angle, the weight pulls the vehicle to the ground and
either forward or backward. Whether the vehicle travels forward or backward,
aerodynamic drag slows it down. For simplicity, the drag is assumed to act through
the CG.

The Vehicle Body 3DOF Longitudinal implements these equations.

x¨=Fxm−qzz¨=Fzm−qxq˙=MyIyyθ˙=q

### Suspension System Forces

If you configure the block with the **Ground interaction type**
parameter `Grade angle` or `Axle displacement,
velocity`, the block uses nonlinear stiffness and damping
parameters to model the suspension system.

The front and rear axle suspension forces are given by:

FsF=NF[FkF+FbF]FsR=NR[FkR+FbR]

The block uses lookup tables to implement the front and rear suspension stiffness.
To account for kinematic and material nonlinearities, including collisions with
end-stops, the tables are functions of the stroke.

FkF=f(dZF)FkR=f(dZR)

The block uses lookup tables to implement the front and rear suspension damping.
To account for nonlinearities, compression, and rebound, the tables are functions of
the stroke rate.

FbF=f(dZ˙F)FbR=f(dZ˙R)

The stroke is the difference in the vehicle vertical and axle positions. The
stroke rate is the difference in the vertical and axle velocities.

dZF=ZF−Z¯FdZR=ZR−Z¯RdZ˙F=Z˙F−Z¯˙FdZ˙R=Z˙R−Z¯˙R

When the **Ground interaction type** parameter is
`Grade angle`, the axle vertical positions (Z¯F,Z¯R) and velocities (Z¯˙F,Z¯˙R) are set to `0`.

### Wind and Drag Forces

The block subtracts the wind speeds from the vehicle velocity components to obtain
a net relative airspeed. To calculate the drag force and moments acting on the
vehicle, the block uses the net relative airspeed:

Fd,x=12TRCdAfPabs(x˙−wx)2Fd,z=12TRClAfPabs(x˙−wx)2Md,y=12TRCpmAfPabs(x˙−wx)2(a+b)

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrFxExt` | Externally applied longitudinal force power | PFxExt=FxExtx˙ |
| `PwrFzExt` | Externally applied longitudinal force power | PFzExt=FzExtz˙ |
| `PwrMyExt` | Externally applied pitch moment power | PMzExt=MzExtθ˙ |
| `PwrFwFx` | Longitudinal force applied at the front axle | PFwFx=FwFx˙ |
| `PwrFwRx` | Longitudinal force applied at the rear axle | PFwRx=FwRx˙ |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrFsF` | Internal power transferred between suspension and vehicle body at the front axle | PFs,F=−PFwFx+PFsbF+PFsk,F+FxFx˙F+FzFz˙F |
| `PwrFsR` | Internal power transferred between suspension and vehicle body at the rear axle | PFs,R=−PFwRx+PFsb,R+PFsk,R+FxFx˙F+FzFz˙F |
| `PwrFxDrag` | Longitudinal drag force power | Pd,x=Fd,xx˙ |
| `PwrFzDrag` | Vertical drag force power | Pd,z=Fd,zz˙ |
| `PwrMyDrag` | Drag pitch moment power | Pd,My=Md,yθ˙ |
| `PwrFsb` | Total suspension damping power | PFsb=∑i=F,RFsb,iz˙i |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrStoredGrvty` | Rate change in gravitational potential energy | Pg=−mgZ˙ |
| `PwrStoredxdot` | Rate of change of longitudinal kinetic energy | Px˙=mx¨x˙ |
| `PwrStoredzdot` | Rate of change of longitudinal kinetic energy | Pz˙=mz¨z˙ |
| `PwrStoredq` | Rate of change of rotational pitch kinetic energy | Pθ˙=Iyyθ¨θ˙ |
| `PwrStoredFsFzSprng` | Stored spring energy from front suspension | PFskF=Fsk,Fz˙F |
| `PwrStoredFsRzSprng` | Stored spring energy from rear suspension | PFskF=Fsk,Rz˙R |

The equations use these variables.

|  |  |
| --- | --- |
| *Fx* | Longitudinal force on vehicle |
| *Fz* | Normal force on vehicle |
| *My* | Torque on vehicle about the vehicle-fixed *y*-axis |
| *FwF*, *FwR* | Longitudinal force on front and rear axles along vehicle-fixed *x*-axis |
| *Fd,x*, *Fd,z* | Longitudinal and normal drag force on vehicle CG |
| *Fsx,F*, *Fsx,R* | Longitudinal suspension force on front and rear axles |
| *Fsz,F*, *Fsz,R* | Normal suspension force on front and rear axles |
| *Fg,x*,*Fg,z* | Longitudinal and normal gravitational force on vehicle along the vehicle-fixed frame |
| *Md,y* | Torque due to drag on vehicle about the vehicle-fixed *y*-axis |
| *a*,*b* | Distance of front and rear axles, respectively, from the normal projection point of vehicle CG onto the common axle plane |
| *h* | Height of vehicle CG above the axle plane along vehicle-fixed *z*-axis |
| *FsF*, *FsR* | Front and rear axle suspension force along vehicle-fixed *z*-axis |
| *ZwF*, *ZwR* | Front and rear vehicle normal position along earth-fixed *z*-axis |
| *Θ* | Vehicle pitch angle about the vehicle-fixed *y*-axis |
| *m* | Vehicle body mass |
| *NF*, *NR* | Number of front and rear wheels |
| *Iyy* | Vehicle body moment of inertia about the vehicle-fixed *y*-axis |
| *x*, x˙, x¨ | Vehicle longitudinal position, velocity, and acceleration along the vehicle-fixed *x*-axis |
| z, z˙, z¨ | Vehicle normal position, velocity, and acceleration along the vehicle-fixed *z*-axis |
| *FkF*, *FkR* | Front and rear wheel suspension stiffness force along vehicle-fixed *z*-axis |
| *FbF*, *FbR* | Front and rear wheel suspension damping force along vehicle-fixed *z*-axis |
| *ZF*, *ZR* | Front and rear vehicle vertical position along earth-fixed *Z*-axis |
| Z˙F,Z˙R | Front and rear vehicle vertical velocity along vehicle-fixed *z*-axis |
| Z¯F,Z¯R | Front and rear wheel axle vertical position along vehicle-fixed *z*-axis |
| Z¯˙F,Z¯˙R | Front and rear wheel axle vertical velocity along earth-fixed *z*-axis |
| *dZF*, *dZR* | Front and rear axle suspension deflection along vehicle-fixed *z*-axis |
| dZ˙F,dZ˙R | Front and rear axle suspension deflection rate along vehicle-fixed *z*-axis |
| *Cd* | Frontal air drag coefficient acting along the vehicle-fixed *x*-axis |
| *Cl* | Lateral air drag coefficient acting along the vehicle-fixed *z*-axis |
| *Cpm* | Aerodynamic pitch moment coefficient acting in the vehicle pitch plane or about the vehicle-fixed *y*-axis |
| *Af* | Frontal area |
| *Pabs* | Environmental absolute pressure |
| *R* | Atmospheric specific gas constant |
| *T* | Environmental air temperature |
| *wx* | Wind speed along the vehicle-fixed *x*-axis |
