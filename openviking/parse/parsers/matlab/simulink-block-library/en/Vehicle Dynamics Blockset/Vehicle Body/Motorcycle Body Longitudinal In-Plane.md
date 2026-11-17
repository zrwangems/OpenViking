---
type: simulink-block
title: 'Motorcycle Body Longitudinal In-Plane'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Body'
documentation_page: 'motorcyclebodylongitudinalinplane'
documentation_source_path: 'ref/motorcyclebodylongitudinalinplane.html'
language: en
---

# Motorcycle Body Longitudinal In-Plane

## Ports
```yaml
ports:
- name: FCpF
  summary: Longitudinal and vertical forces at front wheel contact patch vector
  direction: input
- name: FCpR
  summary: Longitudinal and vertical forces at rear wheel contact patch vector
  direction: input
- name: MDrvArmR
  summary: Drive chain moment at rear arm scalar
  direction: input
- name: MDrvFrm
  summary: Drive chain moment at frame scalar
  direction: input
- name: FExt
  summary: External longitudinal and vertical forces at frame vector
  direction: input
- name: MExt
  summary: External moment about frame scalar
  direction: input
- name: MBrkF
  summary: Brake moment at front wheel scalar
  direction: input
- name: MBrkR
  summary: Brake moment at rear wheel scalar
  direction: input
- name: MWhlF
  summary: External moment at front wheel scalar
  direction: input
- name: MWhlR
  summary: External moment at rear wheel scalar
  direction: input
- name: FSuspF
  summary: External suspension force at upper fork scalar
  direction: input
- name: MSuspR
  summary: External suspension moment at rear arm scalar
  direction: input
- name: Grade
  summary: Road grade angle scalar
  direction: input
- name: WindXYZ
  summary: Wind speed array
  direction: input
- name: Temp
  summary: Ambient air temperature scalar
  direction: input
- name: Info
  summary: Bus signal bus
  direction: output
- name: VCpF
  summary: Longitudinal, lateral, and vertical velocity at front wheel contact patch vector
  direction: output
- name: PCpF
  summary: Longitudinal, lateral, and vertical position at front wheel contact patch vector
  direction: output
- name: VCpR
  summary: Longitudinal, lateral, and vertical velocity at rear wheel contact patch vector
  direction: output
- name: PCpR
  summary: Longitudinal, lateral, and vertical position at rear wheel contact patch vector
  direction: output
- name: ThetaFrm
  summary: Main frame pitch angle scalar
  direction: output
- name: ThetaArmR
  summary: Rear arm pitch angle scalar
  direction: output
```

### Input

### **FCpF** — Longitudinal and vertical forces at front wheel contact patch `vector`

Longitudinal and vertical forces at front wheel contact patch
*OCpF*, along
*iCpF* and
*kCpF*, in N. Signal
vector dimensions are `[1x2]` or
`[2x1]`.

### **FCpR** — Longitudinal and vertical forces at rear wheel contact patch `vector`

Longitudinal and vertical forces at rear wheel contact patch *OCpR*, along *iCpR* and *kCpR*, in N. Signal vector dimensions are `[1x2]` or `[2x1]`.

### **MDrvArmR** — Drive chain moment at rear arm `scalar`

Drive chain moment at rear arm *OArmRr*, about *jArmRr*, in N·m.

### **MDrvFrm** — Drive chain moment at frame `scalar`

Drive chain moment at the frame *OFrm*, about *jFrm*, in N·m.

### **FExt** — External longitudinal and vertical forces at frame `vector`

External longitudinal and vertical forces applied at equivalent rider
and motorcycle center of mass (CM), along
*iFrm* and
*kFrm*, in N. Signal
vector dimensions are `[1x2]` or
`[2x1]`.

#### Dependencies

To create this port, select **External
forces**.

### **MExt** — External moment about frame `scalar`

External moment about equivalent rider and motorcycle CM,
*jFrm*, for example,
moment due to rider physical motion, in N·m.

#### Dependencies

To create this port, select **External
moments**.

### **MBrkF** — Brake moment at front wheel `scalar`

Brake moment at the front wheel
*GWhlFr*, about
*jWhlFr*, in N·m.

### **MBrkR** — Brake moment at rear wheel `scalar`

Brake moment at the rear wheel *GWhlRr*, about *jWhlRr*, in N·m.

### **MWhlF** — External moment at front wheel `scalar`

External moment at the front wheel
*GWhlFr*, in N·m.

#### Dependencies

To create this port, select **External front wheel
moment**.

### **MWhlR** — External moment at rear wheel `scalar`

External moment at the rear wheel
*GWhlRr*, in N·m.

#### Dependencies

To create this port, select **External rear wheel
moment**.

### **FSuspF** — External suspension force at upper fork `scalar`

External suspension force at upper fork
*OFrkUp*, along
*kFrkUp*, in N.

#### Dependencies

To create this port, set **Suspension type** to
`User-defined`.

### **MSuspR** — External suspension moment at rear arm `scalar`

External suspension force at upper fork
*OArmRr*, about
*jArmRr*, in N·m.

#### Dependencies

To create this port, set **Suspension type** to
`User-defined`.

### **Grade** — Road grade angle `scalar`

Road grade angle, γ, in deg.

#### Dependencies

To create this port, select **Grade
angle**.

### **WindXYZ** — Wind speed `array`

Wind speed, *WX*,
*WY*,
*WZ* along earth-fixed
*X*-, *Y*-, and
*Z*-axes, in m/s. Signal vector dimensions are
`[1x3]` or `[3x1]`.

#### Dependencies

To create this port, select **Wind
velocity**.

### **Temp** — Ambient air temperature `scalar`

Ambient air temperature,
*Tair*, in K. Considering
this option if you want to vary the temperature during run-time.

#### Dependencies

To create this port, select **Ambient
temperature**.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | | | | Signal | Units |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Geom` | | | | `PosOrgInert` | | Main frame position along the earth-fixed axes | m |
| `PosFwBdy` | | Front wheel center position relative to initial vehicle-fixed wheel position, along the vehicle Z-down *X*-, *Y*-, and *Z*-axes | m |
| `PosRwBdy` | | Rear wheel center position relative to initial vehicle-fixed wheel position, along the vehicle Z-down *X*-, *Y*-, and *Z*-axes | m |
| `AngOrgInert` | | Main frame rotation about the earth-fixed axes | rad |
| `Frame` | `Inert` | `Cg` | `Disp` | `X` | | Vehicle CM displacement along the earth-fixed *X*-axis | m |
| `Y` | | Vehicle CM displacement along the earth-fixed *Y*-axis | m |
| `Z` | | Vehicle CM displacement along the earth-fixed *Z*-axis | m |
| `Vel` | `Xdot` | | Vehicle CM velocity along the earth-fixed *X*-axis | m/s |
| `Ydot` | | Vehicle CM velocity along the earth-fixed *Y*-axis | m/s |
| `Zdot` | | Vehicle CM velocity along the earth-fixed *Z*-axis | m/s |
| `Ang` | `phi` | | Rotation of the vehicle-fixed frame about the earth-fixed *X*-axis (roll) | rad |
| `theta` | | Rotation of the vehicle-fixed frame about the earth-fixed *Y*-axis (pitch) | rad |
| `psi` | | Rotation of the vehicle-fixed frame about the earth-fixed *Z*-axis (yaw) | rad |
| `BdyFrm` | `Cg` | `Disp` | `x` | | Vehicle CM position along the road-fixed *x*-axis | m |
| `y` | | Vehicle CM position along the road-fixed *y*-axis | m |
| `z` | | Vehicle CM position along the road-fixed *z*-axis | m |
| `Vel` | `xdot` | | Vehicle CM velocity along the road-fixed *x*-axis | m/s |
| `ydot` | | Vehicle CM velocity along the road-fixed *y*-axis | m/s |
| `zdot` | | Vehicle CM velocity along the road-fixed *z*-axis | m/s |
| `AngVel` | `p` | | Vehicle angular velocity about the road-fixed *x*-axis (roll rate) | rad/s |
| `q` | | Vehicle angular velocity about the road-fixed *y*-axis (pitch rate) | rad/s |
| `r` | | Vehicle angular velocity about the road-fixed *z*-axis (yaw rate) | rad/s |
| `Acc` | `ax` | | Vehicle CM acceleration along the road-fixed *x*-axis | m/s2 |
| `ay` | | Vehicle CM acceleration along the road-fixed *y*-axis | m/s2 |
| `az` | | Vehicle CM acceleration along the road-fixed *z*-axis | m/s2 |
| `xddot` | | Vehicle CM acceleration along the road-fixed *x*-axis | m/s2 |
| `yddot` | | Vehicle CM acceleration along the road-fixed *y*-axis | m/s2 |
| `zddot` | | Vehicle CM acceleration along the road-fixed *z*-axis | m/s2 |
| `AngAcc` | `pdot` | | Vehicle angular acceleration about the road-fixed *x*-axis | rad/s2 |
| `qdot` | | Vehicle angular acceleration about the road-fixed *y*-axis | rad/s2 |
| `rdot` | | Vehicle angular acceleration about the road-fixed *z*-axis | rad/s2 |
| `Forces` | `Ext` | `Fx` | | External force on vehicle CM along the road-fixed *x*-axis | N |
| `Fy` | | External force on vehicle CM along the road-fixed *x*-axis | N |
| `Fz` | | External force on vehicle CM along the road-fixed *x*-axis | N |
| `Drag` | `Fx` | | Drag force on vehicle CM along the road-fixed *x*-axis | N |
| `Fy` | | Drag force on vehicle CM along the road-fixed *y*-axis | N |
| `Fz` | | Drag force on vehicle CM along the road-fixed *z*-axis | N |
| `Grvty` | `Fx` | | Gravity force on vehicle CM along the road-fixed *x*-axis | N |
| `Fy` | | Gravity force on vehicle CM along the road-fixed *y*-axis | N |
| `Fz` | | Gravity force on vehicle CM along the road-fixed *z*-axis | N |
| `Moments` | `Drag` | `Mx` | | Drag moment on vehicle CM about the road-fixed *x*-axis | N·m |
| `My` | | Drag moment on vehicle CM about the road-fixed *z*-axis | N·m |
| `Mz` | | Drag moment on vehicle CM about the road-fixed *z*-axis | N·m |
| `Ext` | `Mx` | | External moment on vehicle CG about the road-fixed *x*-axis | N·m |
| `My` | | External moment on vehicle CG about the road-fixed *y*-axis | N·m |
| `Mz` | | External moment on vehicle CG about the road-fixed *z*-axis | N·m |
| `Pwr` | `PwrExt` | | | Applied external power | W |
| `Drag` | | | Power loss due to drag | W |
| `PwrInfo` | `Pwr`  `Trnsfrd` | `PwrFxExt` | | | Mechanical power from longitudinal external force | W |
| `PwrFzExt` | | | Mechanical power from vertical external force | W |
| `PwrMyExt` | | | Mechanical power from external pitch moment | W |
| `PwrNot`  `Trnsfrd` | `PwrFxDrag` | | | Mechanical power loss from longitudinal drag force | W |
| `PwrFzDrag` | | | Mechanical power loss from vertical lift force | W |
| `PwrMyDrag` | | | Mechanical power loss from pitch moment drag | W |
| `PwrStored` | `PwrStoredGrvty` | | | Rate change in gravitational potential energy | W |
| `PwrStoredxdot` | | | Rate of change of longitudinal kinetic energy | W |
| `PwrStoredzdot` | | | Rate of change of vertical kinetic energy | W |
| `PwrStoredq` | | | Rate of change of rotational pitch kinetic energy | W |
| `Genrl` | `Vel` | `xdot` | | | Vehicle CM velocity along the road-fixed *x*-axis | m/s |
| `zdot` | | | Vehicle CM velocity along the road-fixed *z*-axis | m/s |
| `Ang` | `thetafrm` | | | Pitch angle of main frame | rad |
| `AngVel` | `thetafrmdot` | | | Main frame rotational velocity | rad/s |
| `AngAcc` | `thetafrmddot` | | | Main frame rotational acceleration | rad/s2 |
| `Whl` | `Genrl` | `Frnt` | `Cp` | `Disp` | `x` | Front wheel contact patch position along the road-fixed *x*-axis | m |
| `z` | Front wheel contact patch position along the road-fixed *z*-axis | m |
| `Vel` | `xdot` | Front wheel contact patch velocity along the road-fixed *x*-axis | m/s |
| `zdot` | Front wheel contact patch velocity along the road-fixed *z*-axis | m/s |
| `Acc` | `xddot` | Front wheel contact patch acceleration along the road-fixed *x*-axis | m/s2 |
| `zddot` | Front wheel contact patch acceleration along the road-fixed *z*-axis | m/s2 |
| `Axl` | `Vel` | `xdot` | Front wheel axle velocity along the road-fixed *x*-axis | m/s |
| `zdot` | Front wheel axle velocity along the road-fixed *z*-axis | m/s |
| `Rear` | `Cp` | `Disp` | `x` | Rear wheel contact patch position along the road-fixed *x*-axis | m |
| `z` | Rear wheel contact patch position along the road-fixed *z*-axis | m |
| `Vel` | `xdot` | Rear wheel contact patch velocity along the road-fixed *x*-axis | m/s |
| `zdot` | Rear wheel contact patch velocity along the road-fixed *z*-axis | m/s |
| `Acc` | `xddot` | Rear wheel contact patch acceleration along the road-fixed *x*-axis | m/s2 |
| `zddot` | Rear wheel contact patch acceleration along the road-fixed *z*-axis | m/s2 |
| `Axl` | `Vel` | `xdot` | Rear wheel axle velocity along the road-fixed *x*-axis | m/s |
| `zdot` | Rear wheel axle velocity along the road-fixed *z*-axis | m/s |
| `RearArm` | `Genrl` | `Vel` | `xdot` | | | Rear arm velocity along the road-fixed *x*-axis | m/s |
| `zdot` | | | Rear arm velocity along the road-fixed *z*-axis | m/s |
| `Ang` | `thetara` | | | Pitch angle of rear arm | rad |
| `AngVel` | `thetaradot` | | | Rear arm rotational velocity | rad/s |
| `AngAcc` | `thetaraddot` | | | Rear arm rotational acceleration | rad/s2 |
| `Fork` | `Genrl` | `Upr` | `Vel` | `xdot` | | Upper fork velocity along the road-fixed *x*-axis | m/s |
| `zdot` | | Upper fork velocity along the road-fixed *z*-axis | m/s |
| `Lwr` | `Disp` | `df` | | Fork length | m |
| `Vel` | `xdot` | | Lower fork velocity along the road-fixed *x*-axis | m/s |
| `zdot` | | Lower fork velocity along the road-fixed *z*-axis | m/s |
| `dfdot` | | Fork length velocity | m/s |
| `Acc` | `dfddot` | | Fork length acceleration | m/s2 |
| `Susp` | `Genrl` | `Rear` | `Moments` | `Mthetafrm` | | Rear suspension moment at frame | N·m |
| `Frnt` | `Forces` | `Fdf` | | Suspensive force at upper fork | N |

### **VCpF** — Longitudinal, lateral, and vertical velocity at front wheel contact patch `vector`

Longitudinal, lateral, and vertical velocity at front wheel contact
patch *OCpF*, along
*iCpF* and
*kCpF*, in m/s. Signal
vector dimensions are `[1x3]` or
`[3x1]`. The lateral component is set to 0.

### **PCpF** — Longitudinal, lateral, and vertical position at front wheel contact patch `vector`

Longitudinal, lateral, and vertical position at front wheel contact
patch *OCpF*, along
*iCpF* and
*kCpF*, in m. Signal
vector dimensions are `[1x3]` or
`[3x1]`. The lateral component is set to 0.

### **VCpR** — Longitudinal, lateral, and vertical velocity at rear wheel contact patch `vector`

Longitudinal, lateral, and vertical velocity at rear wheel contact
patch *OCpR*, along
*iCpR* and
*kCpR*, in m/s. Signal
vector dimensions are `[1x3]` or
`[3x1]`. The lateral component is set to 0.

### **PCpR** — Longitudinal, lateral, and vertical position at rear wheel contact patch `vector`

Longitudinal, lateral, and vertical position at rear wheel contact
patch *OCpR*, along
*iCpR*, and
*kCpR*, in m. Signal
vector dimensions are `[1x3]` or
`[3x1]`. The lateral component is set to 0.

### **ThetaFrm** — Main frame pitch angle `scalar`

Main frame pitch angle, *ϴfrm*, in rad.

### **ThetaArmR** — Rear arm pitch angle `scalar`

Rear arm pitch angle, *ϴra*, in rad.
## Parameters
```yaml
parameters:
- name: Suspension type
  summary: Type of suspension Simple (default) | User-defined
  group: Options
- name: External forces
  summary: FExt input port off (default) | on
  group: Options
- name: External moments
  summary: MExt input port off (default) | on
  group: Options
- name: External front wheel moment
  summary: MWhlF input port off (default) | on
  group: Options
- name: External rear wheel moment
  summary: MWhlR input port off (default) | on
  group: Options
- name: Grade angle
  summary: Grade input port on (default) | off
  group: Options
- name: Wind velocity
  summary: WindXYZ input port on (default) | off
  group: Options
- name: Ambient temperature
  summary: Temp input port off (default) | on
  group: Options
- name: Center of mass location, FrmCmPxz
  summary: Frame location [0.255, -0.02] (default) | vector
  group: Layout
- name: Mass, FrmMass
  summary: Frame mass 223 (default) | scalar
  group: Layout
- name: Mass moment of inertia, FrmIyy
  summary: Frame inertia 26.2 (default) | scalar
  group: Layout
- name: Length, FrmLen
  summary: Frame length 0.730 (default) | scalar
  group: Layout
- name: Center of mass location, RdrCmPxz
  summary: Rider location [0.275, -0.61] (default) | vector
  group: Layout
- name: Mass, RdrMass
  summary: Rider mass 78 (default) | scalar
  group: Layout
- name: Mass moment of inertia, RdrIyy
  summary: Rider inertia 26.2 (default) | scalar
  group: Layout
- name: Position, FrkUpCmPxz
  summary: Upper fork location [0.023, -0.098] (default) | vector
  group: Layout
- name: Mass, FrkUpMass
  summary: Upper fork mass 8.8 (default) | scalar
  group: Layout
- name: Mass moment of inertia, FrkUpIyy
  summary: Upper fork inertia 0.14 (default) | scalar
  group: Layout
- name: Offset, FrkOfs
  summary: Upper fork offset 0.034 (default) | scalar
  group: Layout
- name: Position, FrkLwCmPxz
  summary: Lower fork location [-0.029, -0.189] (default) | vector
  group: Layout
- name: Mass, FrkLwMass
  summary: Lower fork mass 7.0 (default) | scalar
  group: Layout
- name: Mass moment of inertia, FrkLwIyy
  summary: Lower fork inertia 0.18 (default) | scalar
  group: Layout
- name: Position, ArmRrCmPxz
  summary: Rear arm location [0.275, -0.052] (default) | vector
  group: Layout
- name: Mass, ArmRrMass
  summary: Rear arm mass 10 (default) | scalar
  group: Layout
- name: Mass moment of inertia, ArmRrIyy
  summary: Rear arm inertia 0.8 (default) | scalar
  group: Layout
- name: Length, ArmRrLen
  summary: Rear arm length 0.535 (default) | scalar
  group: Layout
- name: Mass, WhlFrMass
  summary: Front wheel mass 12 (default) | scalar
  group: Layout
- name: Radius, WhlFrR
  summary: Front wheel radius 0.3 (default) | scalar
  group: Layout
- name: Mass, WhlRrMass
  summary: Rear wheel mass 16.2 (default) | scalar
  group: Layout
- name: Radius, WhlRrR
  summary: Rear wheel radius 0.33 (default) | scalar
  group: Layout
- name: Stiffness, SuspFrK
  summary: Front suspension stiffness 25e3 (default) | scalar
  group: Layout
- name: Damping, SuspFrC
  summary: Front suspension damping 1250 (default) | scalar
  group: Layout
- name: Equilibrium length, FrkLwL0
  summary: Front suspension equilibrium length 0.473 (default) | scalar
  group: Layout
- name: Stiffness, SuspRrK
  summary: Rear arm suspension stiffness 1500 (default) | scalar
  group: Layout
- name: Damping, SuspRrC
  summary: Rear arm suspension damping 150 (default) | scalar
  group: Layout
- name: Equilibrium angle, ShkRrAng0
  summary: Rear suspension equilibrium angle 0 (default) | scalar
  group: Layout
- name: Longitudinal drag area, Af
  summary: Area 2 (default) | scalar
  group: Aerodynamic
- name: Longitudinal drag coefficient, Cd
  summary: Drag .2 (default) | scalar
  group: Aerodynamic
- name: Longitudinal lift coefficient, Cl
  summary: Lift .1 (default) | scalar
  group: Aerodynamic
- name: Longitudinal drag pitch moment, Cpm
  summary: Pitch drag .1 (default) | scalar
  group: Aerodynamic
- name: Pitch moment length, Lcpm
  summary: Pitch drag 2 (default) | scalar
  group: Aerodynamic
- name: Gravitational acceleration, g
  summary: Gravity 9.80665 (default) | scalar
  group: Environment
- name: Absolute air pressure, Pabs
  summary: Pressure 101325 (default) | scalar
  group: Environment
- name: Air temperature, Tair
  summary: Ambient air temperature 273 (default) | scalar
  group: Environment
- name: Rear contact patch longitudinal coordinate, CpRrX0
  summary: Longitudinal coordinate 0 (default) | scalar
  group: Initial conditions
- name: Rear contact patch vertical coordinate, CpRrZ0
  summary: Vertical coordinate 0 (default) | scalar
  group: Initial conditions
- name: Pitch angle of rear arm, ArmRrAng0
  summary: Rear arm angle 0.0590379 (default) | scalar
  group: Initial conditions
- name: Pitch angle of main frame, FrmAng0
  summary: Angle length 0.377024 (default) | scalar
  group: Initial conditions
- name: Fork length, FrkFrL0
  summary: Fork length 0.4262193 (default) | scalar
  group: Initial conditions
- name: Longitudinal velocity of rear contact patch
  summary: Longitudinal velocity 0 (default) | scalar
  group: Initial conditions
- name: Vertical velocity of rear contact patch, CpRrVz0
  summary: Vertical velocity 0 (default) | scalar
  group: Initial conditions
- name: Pitch rate of rear arm, ArmRrAngV0
  summary: Pitch rate 0 (default) | scalar
  group: Initial conditions
- name: Pitch rate of main frame, FrmAngV0
  summary: Pitch rate 0 (default) | scalar
  group: Initial conditions
- name: Lower fork deformation velocity, FrkLwV0
  summary: Deformation velocity 0 (default) | scalar
  group: Initial conditions
- name: Longitudinal offset, longOff
  summary: Longitudinal offset 0 (default) | scalar
  group: Coordinate Offsets
- name: Lateral offset, latOff
  summary: Lateral offset 0 (default) | scalar
  group: Coordinate Offsets
- name: Vertical offset, vertOff
  summary: Vertical offset 0 (default) | scalar
  group: Coordinate Offsets
- name: Roll offset, pitchOff
  summary: Roll offset 0 (default) | scalar
  group: Coordinate Offsets
- name: Pitch offset, pitchOff
  summary: Pitch offset 0 (default) | scalar
  group: Coordinate Offsets
- name: Yaw offset, pitchOff
  summary: Yaw offset 0 (default) | scalar
  group: Coordinate Offsets
```

### Options

### **Suspension type** — Type of suspension `Simple` (default) | `User-defined`

Use the **Suspension type** parameter to specify the type of suspension.

| Setting | Description |
| --- | --- |
| `Simple` | Block models the suspension force and moment as a spring-damper system:  - Suspension force at the upper fork - Suspension moment at the rear arm |
| `User-defined` | Input the suspension force and moment:  - `FSuspF` – Suspension force at the upper   fork - `MSuspR` – Suspension moment at the rear   arm |

#### Input signals

### **External forces** — `FExt` input port `off` (default) | `on`

Specify to create input port `FExt`.

### **External moments** — `MExt` input port `off` (default) | `on`

Specify to create input port `MExt`.

### **External front wheel moment** — `MWhlF` input port `off` (default) | `on`

Specify to create input port `MWhlF`. Consider using
this port to input external moments such as wheel motors and external
intermittent friction-related disturbances.

### **External rear wheel moment** — `MWhlR` input port `off` (default) | `on`

Specify to create input port `MWhlR`. Consider using
this port to input external moments such as wheel motors and external
intermittent friction-related disturbances.

### **Grade angle** — `Grade` input port `on` (default) | `off`

Specify to create input port `Grade`.

### **Wind velocity** — `WindXYZ` input port `on` (default) | `off`

Specify to create input port `WindXYZ`.

### **Ambient temperature** — `Temp` input port `off` (default) | `on`

Specify to create input port `Temp`.

### Layout

Motorcycle body diagram

Use the parameters in this table to specify the geometric
layout of your motorcycle.

| Parameter | | | Variable in Figure |
| --- | --- | --- | --- |
| **Initial conditions** | **Position** | **Rear contact patch longitudinal coordinate, CpRrX0** | *OCpR* with respect to road-fixed coordinate system, along `x` |
| **Rear contact patch vertical coordinate, CpRrZ0** | *OCpR* with respect to road-fixed coordinate system, along `z` |
| **Pitch angle of rear arm, ArmRrAng0** | *θra* |
| **Pitch angle of main frame, FrmAng0** | *θFrm* |
| **Fork length, FrkFrL0** | *df* |
| **Frame** | | **Center of mass location, FrmCmPxz** | *GFrm* with respect to *OFrm*, along *iFrm* and *kFrm*, respectively |
| **Length, FrmLen** | *FrmLen* |
| **Rider** | | **Center of mass location, RdrCmPxz** | *GRdr* with respect to *OFrm*, along *iFrm* and *kFrm*, respectively |
| **Front Fork** | **Upper** | **Position, FrkUpCmPxz** | *GFrkUp* with respect to *OFrkUp*, along *iFrkUp* and *kFrkUp*, respectively |
| **Offset, FrkOfs** | *FrkOfs* |
| **Lower** | **Position, FrkLwCmPxz** | *GFrkLw* with respect to *OFrkLw*, along *iFrkLw* and *kFrkLw*, respectively |
| **Rear Arm** | | **Position, ArmRrCmPxz** | *GArmRr* with respect to *OArmRr*, along *iArmRr* and *kArmRr*, respectively |
| **Length, ArmRrLen** | *ArmRrLen* |
| **Wheels** | **Front** | **Radius, WhlFrR** | *WhlFrR* |
| **Rear** | **Radius, WhlRrR** | *WhlRrR* |
| **Suspension** | **Front** | **Equilibrium length, FrkLwL0** | *df* |
| **Rear** | **Equilibrium angle, ShkRrAng0** | *θFrm* |

#### Frame

### **Center of mass location, FrmCmPxz** — Frame location `[0.255, -0.02]` (default) | `vector`

Center of mass location of the frame,
*GFrm*. Specified as a
vector with respect to *OFrm*,
along *iFrm* and
*kFrm*,
respectively.

### **Mass, FrmMass** — Frame mass `223` (default) | `scalar`

Frame mass, *FrmMass*, in kg.

### **Mass moment of inertia, FrmIyy** — Frame inertia `26.2` (default) | `scalar`

Mass moment of inertia, *FrmIyy*, in
kg·m2.

### **Length, FrmLen** — Frame length `0.730` (default) | `scalar`

Length of the frame, *FrmLen*, in m.

#### Rider

### **Center of mass location, RdrCmPxz** — Rider location `[0.275, -0.61]` (default) | `vector`

Center of mass location of the rider,
*GRdr*. Specified as a
vector with respect to *OFrm*,
along *iFrm* and
*kFrm*,
respectively.

### **Mass, RdrMass** — Rider mass `78` (default) | `scalar`

Rider mass, *RdrMass*, in kg.

### **Mass moment of inertia, RdrIyy** — Rider inertia `26.2` (default) | `scalar`

Rider mass moment of inertia, *RdrIyy*, in
kg·m2.

#### Front Fork – Upper

### **Position, FrkUpCmPxz** — Upper fork location `[0.023, -0.098]` (default) | `vector`

Center of mass location of the upper fork,
*GFrkUp*. Specified as a
vector with respect to *OFrkUp*,
along *iFrkUp* and
*kFrkUp*,
respectively.

### **Mass, FrkUpMass** — Upper fork mass `8.8` (default) | `scalar`

Upper fork mass, *FrkUpMass*, in kg.

### **Mass moment of inertia, FrkUpIyy** — Upper fork inertia `0.14` (default) | `scalar`

Upper fork mass moment of inertia, *FrkUpIyy*, in
kg·m2.

### **Offset, FrkOfs** — Upper fork offset `0.034` (default) | `scalar`

Upper fork offset, *FrkOfs*, in m.

#### Front Fork – Lower

### **Position, FrkLwCmPxz** — Lower fork location `[-0.029, -0.189]` (default) | `vector`

Center of mass location of the lower fork,
*GFrkLw*. Specified as a
vector with respect to *OFrkLw*,
along *iFrkLw* and
*kFrkLw*,
respectively.

### **Mass, FrkLwMass** — Lower fork mass `7.0` (default) | `scalar`

Lower fork mass, *FrkLwMass*, in kg.

### **Mass moment of inertia, FrkLwIyy** — Lower fork inertia `0.18` (default) | `scalar`

Lower fork mass moment of inertia, *FrkLwIyy*, in
kg·m2.

#### Rear Arm

### **Position, ArmRrCmPxz** — Rear arm location `[0.275, -0.052]` (default) | `vector`

Center of mass location of the rear arm,
*GArmRr*. Specified as a
vector with respect to *OArmRr*,
along *iArmRr* and
*kArmRr*,
respectively.

### **Mass, ArmRrMass** — Rear arm mass `10` (default) | `scalar`

Rear arm mass, *ArmRrMass*, in kg.

### **Mass moment of inertia, ArmRrIyy** — Rear arm inertia `0.8` (default) | `scalar`

Rear arm mass moment of inertia, *ArmRrIyy*, in
kg·m2.

### **Length, ArmRrLen** — Rear arm length `0.535` (default) | `scalar`

Rear arm length, *ArmRrLen*, in m.

#### Wheels – Front

### **Mass, WhlFrMass** — Front wheel mass `12` (default) | `scalar`

Front wheel mass, *WhlFrMass*, in kg.

### **Radius, WhlFrR** — Front wheel radius `0.3` (default) | `scalar`

Front wheel radius, *WhlFrR*, in m.

#### Wheels – Rear

### **Mass, WhlRrMass** — Rear wheel mass `16.2` (default) | `scalar`

Rear wheel mass, *WhlRrMass*, in kg.

### **Radius, WhlRrR** — Rear wheel radius `0.33` (default) | `scalar`

Rear wheel radius, *WhlRrR*, in m.

#### Suspension – Front

### **Stiffness, SuspFrK** — Front suspension stiffness `25e3` (default) | `scalar`

Front suspension stiffness at
*OFrkUp*, along
*kFrkUp*, in N/m.

### **Damping, SuspFrC** — Front suspension damping `1250` (default) | `scalar`

Front suspension damping, at
*OFrkUp*, along
*kFrkUp*, in
N·s/m.

### **Equilibrium length, FrkLwL0** — Front suspension equilibrium length `0.473` (default) | `scalar`

Front suspension equilibrium length,
*df*, in m.

#### Suspension – Rear

### **Stiffness, SuspRrK** — Rear arm suspension stiffness `1500` (default) | `scalar`

Rear arm suspension stiffness at
*OArmRr*, about
*jArmRr*, in
N/rad.

### **Damping, SuspRrC** — Rear arm suspension damping `150` (default) | `scalar`

Rear arm suspension damping at
*OArmRr*, about
*jArmRr*, in
N·s/rad.

### **Equilibrium angle, ShkRrAng0** — Rear suspension equilibrium angle `0` (default) | `scalar`

Rear suspension equilibrium angle,
*θFrm*, in rad.

### Aerodynamic

### **Longitudinal drag area, Af** — Area `2` (default) | `scalar`

Effective vehicle cross-sectional area,
*Af* to calculate the
aerodynamic drag force on the vehicle, in
m2.

### **Longitudinal drag coefficient, Cd** — Drag `.2` (default) | `scalar`

Air drag coefficient, *Cd*,
dimensionless.

### **Longitudinal lift coefficient, Cl** — Lift `.1` (default) | `scalar`

Air lift coefficient, *Cl*,
dimensionless.

### **Longitudinal drag pitch moment, Cpm** — Pitch drag `.1` (default) | `scalar`

Longitudinal drag pitch moment coefficient,
*Cpm*,
dimensionless.

### **Pitch moment length, Lcpm** — Pitch drag `2` (default) | `scalar`

Pitch moment length, *Lcpm*, in m.

### Environment

### **Gravitational acceleration, g** — Gravity `9.80665` (default) | `scalar`

Gravitational acceleration, *g*, in
m/s2.

### **Absolute air pressure, Pabs** — Pressure `101325` (default) | `scalar`

Environmental air absolute pressure, *Pabs*,
in Pa.

### **Air temperature, Tair** — Ambient air temperature `273` (default) | `scalar`

Ambient air temperature,
*Tair*, in K.

#### Dependencies

To enable this parameter, clear **Ambient
temperature**.

### Initial conditions

#### Position

### **Rear contact patch longitudinal coordinate, CpRrX0** — Longitudinal coordinate `0` (default) | `scalar`

Rear contact patch longitudinal coordinate,
*OCpR*, with respect to
road-fixed coordinate system, along `x`, in m.

### **Rear contact patch vertical coordinate, CpRrZ0** — Vertical coordinate `0` (default) | `scalar`

Rear contact patch vertical coordinate,
*OCpR*, with respect to
road-fixed coordinate system, along `z`, in m.

### **Pitch angle of rear arm, ArmRrAng0** — Rear arm angle `0.0590379` (default) | `scalar`

Pitch angle of rear arm,
*θra*, in rad.

### **Pitch angle of main frame, FrmAng0** — Angle length `0.377024` (default) | `scalar`

Pitch angle of main frame,
*θFrm*, in rad.

### **Fork length, FrkFrL0** — Fork length `0.4262193` (default) | `scalar`

Fork length, *df*, in
m.

#### Velocity

### **Longitudinal velocity of rear contact patch** — Longitudinal velocity `0` (default) | `scalar`

Rear contact patch longitudinal coordinate, O˙CpR, with respect to road-fixed coordinate system, along
`x`, in m/s.

### **Vertical velocity of rear contact patch, CpRrVz0** — Vertical velocity `0` (default) | `scalar`

Vertical velocity of rear contact patch, O˙CpR, with respect to road-fixed coordinate system, along
`z`, in m/s.

### **Pitch rate of rear arm, ArmRrAngV0** — Pitch rate `0` (default) | `scalar`

Pitch rate of rear arm, θ˙ra, in rad/s.

### **Pitch rate of main frame, FrmAngV0** — Pitch rate `0` (default) | `scalar`

Pitch rate of main frame, θ˙Frm, in rad/s.

### **Lower fork deformation velocity, FrkLwV0** — Deformation velocity `0` (default) | `scalar`

Lower fork deformation velocity, d˙f, in m/s.

### Coordinate Offsets

### **Longitudinal offset, longOff** — Longitudinal offset `0` (default) | `scalar`

Vehicle main frame offset along the earth-fixed
*X*-axis, in m.

### **Lateral offset, latOff** — Lateral offset `0` (default) | `scalar`

Vehicle main frame offset along the earth-fixed
*Y*-axis, in m.

### **Vertical offset, vertOff** — Vertical offset `0` (default) | `scalar`

Vehicle main frame offset along the earth-fixed
*Z*-axis, in m.

### **Roll offset, pitchOff** — Roll offset `0` (default) | `scalar`

Vehicle main frame offset about the earth-fixed
*X*-axis, in rad.

### **Pitch offset, pitchOff** — Pitch offset `0` (default) | `scalar`

Vehicle main frame offset about the earth-fixed
*Y*-axis, in rad.

### **Yaw offset, pitchOff** — Yaw offset `0` (default) | `scalar`

Vehicle main frame offset about the earth-fixed
*Z*-axis, in rad.
## Libraries

Powertrain Blockset / Vehicle Dynamics Vehicle Dynamics Blockset / Vehicle Body

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Longitudinal in-plane motorcycle vehicle motion

The Motorcycle Body Longitudinal In-Plane block implements a
longitudinal in-plane motorcycle body model to calculate longitudinal, vertical, and
pitch motion. The block accounts for:

- Mass of the frame, rear arm, front upper fork, front lower fork, front
  wheel, and rear wheel
- In-plane dynamic effects of the frame, front lower fork, front wheel, rear
  wheel, rear suspension, front suspension, rear wheel damper, rear arm, and
  chain
- External forces, external moments, and aerodynamic drag
- Road incline
- Weight distribution between the axles due to acceleration

Consider using this block to represent motorcycle motion in powertrain and fuel
economy studies, for example, in studies with heavy breaking or acceleration or road
profiles that contain larger vertical changes.

The block uses rigid-body vehicle motion, suspension system forces, and wind and drag
forces to calculate the forces on the motorcycle frames. The block then determines the
position and velocity of motorcycle at the front and rear contact patches.

### Layout

To determine the rigid-body motorcycle motion, the block uses
right-handed (RH) *Cartesian* reference frames systems attached to the
motorcycle. *i*, *j*, and *k* are orthogonal
unit vectors attached to the frames.

Motorcycle body diagram

| Frame | Variable in Figure | Description |
| --- | --- | --- |
| Road | *x*, *z* | Road-fixed coordinate system. *x* is along road grade, and *z* points downward. |
| Motorcycle main frame  - *iFrm* – Forward   along vector given by   *θfrm* - *kFrm* –   Downward - *jFrm* –   Orthogonal to motorcycle plane | *OFrm* | Main frame origin |
| *GFrm* | Center of mass (CM) of the main frame with respect to *OFrm*, along *iFrm* and *kFrm*, respectively |
| *GRdr* | CM of the rider with respect to *OFrm*, along *iFrm* and *kFrm*, respectively |
| *ϴfrm* | Main frame rotation about *jFrm* |
| Upper fork  - *iFrkUp* – Forward   along vector given by   *θfrm* - *kFrkUp* –   Downward - *jFrkUp* –   Orthogonal to motorcycle plane | *OFrkUp* | Upper fork origin |
| *GFrkUp* | CM of the upper fork with respect to *OFrkUp*, along *iFrkUp* and *kFrkUp*, respectively |
| Lower fork  - *iFrkLw* – Forward   along vector given by   *θfrm* - *kFrkLw* –   Downward - *jFrkLw* –   Orthogonal to motorcycle plane | *OFrkLw* | Lower fork origin |
| *GFrkLw* | CM of the lower fork with respect to *OFrkLw*, along *iFrkLw* and *kFrkLw*, respectively |
| Rear arm  - *iArmRr* – Forward   along vector given by   *θra* - *kArmRr* –   Downward - *jArmRr* –   Orthogonal to motorcycle plane | *OArmRr* | Rear arm origin |
| *GArmRr* | CM of the rear arm with respect to *OArmRr*, along *iArmRr* and *kArmRr*, respectively |
| *ϴra* | Rear arm rotation about *jArmRr* |
| Front wheel contact patch  - *iCpF* – Forward   along vector given by road-fixed *x*-   axis - *kCpF* – Downward   along vector given by road-fixed *z*-   axis - *jCpF* –   Orthogonal to motorcycle plane | *OCpF* | Front wheel contact patch origin |
| Rear wheel contact patch  - *iCpR* – Forward   along vector given by road-fixed *x*-   axis - *kCpR* – Downward   along vector given by road-fixed *z*-   axis - *jCpR* –   Orthogonal to motorcycle plane | *OCpR* | Rear wheel contact patch origin |

Use the parameters in this table to specify the geometric
layout of your motorcycle.

| Parameter | | | Variable in Figure |
| --- | --- | --- | --- |
| **Initial conditions** | **Position** | **Rear contact patch longitudinal coordinate, CpRrX0** | *OCpR* with respect to road-fixed coordinate system, along `x` |
| **Rear contact patch vertical coordinate, CpRrZ0** | *OCpR* with respect to road-fixed coordinate system, along `z` |
| **Pitch angle of rear arm, ArmRrAng0** | *θra* |
| **Pitch angle of main frame, FrmAng0** | *θFrm* |
| **Fork length, FrkFrL0** | *df* |
| **Frame** | | **Center of mass location, FrmCmPxz** | *GFrm* with respect to *OFrm*, along *iFrm* and *kFrm*, respectively |
| **Length, FrmLen** | *FrmLen* |
| **Rider** | | **Center of mass location, RdrCmPxz** | *GRdr* with respect to *OFrm*, along *iFrm* and *kFrm*, respectively |
| **Front Fork** | **Upper** | **Position, FrkUpCmPxz** | *GFrkUp* with respect to *OFrkUp*, along *iFrkUp* and *kFrkUp*, respectively |
| **Offset, FrkOfs** | *FrkOfs* |
| **Lower** | **Position, FrkLwCmPxz** | *GFrkLw* with respect to *OFrkLw*, along *iFrkLw* and *kFrkLw*, respectively |
| **Rear Arm** | | **Position, ArmRrCmPxz** | *GArmRr* with respect to *OArmRr*, along *iArmRr* and *kArmRr*, respectively |
| **Length, ArmRrLen** | *ArmRrLen* |
| **Wheels** | **Front** | **Radius, WhlFrR** | *WhlFrR* |
| **Rear** | **Radius, WhlRrR** | *WhlRrR* |
| **Suspension** | **Front** | **Equilibrium length, FrkLwL0** | *df* |
| **Rear** | **Equilibrium angle, ShkRrAng0** | *θFrm* |

### Input Signals

You can use these block parameters to create
additional input ports. This table summarizes the settings.

| Input Signals Pane Parameter | Input Port | Description |
| --- | --- | --- |
| **External forces** | `FExt` | External longitudinal and vertical forces applied at equivalent rider and motorcycle center of mass (CM). |
| **External moments** | `MExt` | External moment about equivalent rider and motorcycle CM, for example, moment due to rider physical motion. |
| **External front wheel moment** | `MWhlF` | External moment at the front wheel *GWhlFr*, for example, wheel motors and external intermittent friction-related disturbances. |
| **External rear wheel moment** | `MWhlR` | External moment at the rear wheel *GWhlRr*, for example, wheel motors and external intermittent friction-related disturbances. |
| **Grade angle** | `Grade` | Road grade angle. |
| **Wind velocity** | `WindXYZ` | Wind speed. |
| **Ambient temperature** | `Temp` | Ambient air temperature. Consider this option if you want to vary the temperature during run-time. |

### Suspension System

Use the **Suspension type** parameter to specify the type of suspension.

| Setting | Description |
| --- | --- |
| `Simple` | Block models the suspension force and moment as a spring-damper system:  - Suspension force at the upper fork - Suspension moment at the rear arm |
| `User-defined` | Input the suspension force and moment:  - `FSuspF` – Suspension force at the upper   fork - `MSuspR` – Suspension moment at the rear   arm |

### Wind and Drag Forces

The block subtracts the wind speeds from the vehicle velocity components to obtain
a net relative airspeed. To calculate the drag force and moments acting on the
motorcycle, the block uses the net relative airspeed.

### Use in 3D Environment

To co-simulate in the Unreal Engine® and provide a motorcycle with the motion calculated by the
Motorcycle Body Longitudinal In-Plane block:

1. Put the Simulation 3D Motorcycle block in your model.
2. Route these the Info bus port signals to the Simulation 3D
   Motorcycle input ports Translation and Rotation.

   - `PosOrgInert`
   - `PosFwBdy`
   - `PosRwBdy`
   - `AngOrgInert`

   Figure Simulation 3D Motorcycle block inputs

For more information about using the block in the 3D environment, see Longitudinal Motorcycle Braking Test.

### Power Accounting

The block accounts for the power transferred, not transferred, and
stored.

| Bus Signal | | | Description |
| --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrFxExt` | Mechanical power from longitudinal external force |
| `PwrFzExt` | Mechanical power from vertical external force |
| `PwrMyExt` | Mechanical power from external pitch moment |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrFxDrag` | Mechanical power loss from longitudinal drag force |
| `PwrFzDrag` | Mechanical power loss from vertical lift |
| `PwrMyDrag` | Mechanical power loss from pitch moment drag |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrStoredGrvty` | Rate change in gravitational potential energy |
| `PwrStoredxdot` | Rate of change of longitudinal kinetic energy |
| `PwrStoredzdot` | Rate of change of vertical kinetic energy |
| `PwrStoredq` | Rate of change of rotational pitch kinetic energy |
| `PwrStoredFsFzSprng` | Stored spring energy from front suspension |
| `PwrStoredFsRzSprng` | Stored spring energy from rear suspension |
