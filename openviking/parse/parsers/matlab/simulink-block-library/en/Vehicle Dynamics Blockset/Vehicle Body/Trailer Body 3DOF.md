---
type: simulink-block
title: 'Trailer Body 3DOF'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Body'
documentation_page: 'trailerbody3dof'
documentation_source_path: 'ref/trailerbody3dof.html'
language: en
---

# Trailer Body 3DOF

## Ports
```yaml
ports:
- name: WhlAngF
  summary: Front wheel steering angles scalar | array
  direction: input
- name: WhlAngM
  summary: Middle wheel steering angles scalar | array
  direction: input
- name: WhlAngR
  summary: Rear wheel steering angles scalar | array
  direction: input
- name: xdotin
  summary: Longitudinal velocity scalar
  direction: input
- name: FwF
  summary: Total force on the front wheels scalar | array
  direction: input
- name: FwM
  summary: Total force on the middle wheels scalar | array
  direction: input
- name: FwR
  summary: Total force on the rear wheels scalar | array
  direction: input
- name: FExt
  summary: External force on the vehicle CG array
  direction: input
- name: MExt
  summary: External moment about vehicle CG array
  direction: input
- name: FhF
  summary: Front hitch force on the body array
  direction: input
- name: MhF
  summary: Front hitch moment about body array
  direction: input
- name: FhR
  summary: Rear hitch force on the body array
  direction: input
- name: MhR
  summary: Rear hitch moment about body array
  direction: input
- name: WindXYZ
  summary: Wind speed array
  direction: input
- name: Mu
  summary: Tire friction coefficient array
  direction: input
- name: AirTemp
  summary: Ambient air temperature scalar
  direction: input
- name: X_o
  summary: Initial longitudinal position scalar
  direction: input
- name: Y_o
  summary: Initial lateral position scalar
  direction: input
- name: xdot_o
  summary: Initial longitudinal position scalar
  direction: input
- name: ydot_o
  summary: Initial lateral position scalar
  direction: input
- name: psi_o
  summary: Initial yaw angle scalar
  direction: input
- name: r_o
  summary: Initial yaw rate scalar
  direction: input
- name: Info
  summary: Trailer data bus
  direction: output
- name: xdot
  summary: Trailer longitudinal velocity scalar
  direction: output
- name: ydot
  summary: Trailer lateral velocity scalar
  direction: output
- name: psi
  summary: Yaw scalar
  direction: output
- name: r
  summary: Yaw rate scalar
  direction: output
- name: FzF
  summary: Normal force on the front wheels scalar | array
  direction: output
- name: FzM
  summary: Normal force on the middle wheels scalar | array
  direction: output
- name: FzR
  summary: Normal force on the rear wheels scalar | array
  direction: output
- name: Fhz
  summary: Normal component of hitch force on the body scalar
  direction: output
```

### Input

### **WhlAngF** — Front wheel steering angles `scalar` | `array`

Front wheel steering angles,
*δF*, in rad.

| **Vehicle Track** Setting | Variable | Signal Dimension |
| --- | --- | --- |
| `Single 1-axle`  `Single 2-axle`  `Single 3-axle` | *δF* | Scalar – `1` |
| `Dual 1-axle`  `Dual 2-axle`  `Dual 3-axle` | δF=[δflδfr]  or  [δflδfr] | Array – `[1x2]` or `[2x1]` |

#### Dependencies

To enable this port, under **Input signals**,
select **Front wheel steering**.

### **WhlAngM** — Middle wheel steering angles `scalar` | `array`

Middle wheel steering angles,
*δM*, in rad.

| **Vehicle Track** Setting | Variable | Signal Dimension |
| --- | --- | --- |
| `Single 3-axle` | *δM* | Scalar – `1` |
| `Dual 3-axle` | δM=[δmlδmr]  or  [δmlδmr] | Array – `[1x2]` or `[2x1]` |

#### Dependencies

To enable this port:

- Set **Vehicle track** to
  `Single 3-axle` or
  `Dual 3-axle`.
- To enable this port, under **Input
  signals**, select **Middle wheel
  steering**.

### **WhlAngR** — Rear wheel steering angles `scalar` | `array`

Rear wheel steering angles,
*δR*, in rad.

| **Vehicle Track** Setting | Variable | Signal Dimension |
| --- | --- | --- |
| `Single 1-axle`  `Single 2-axle`  `Single 3-axle` | *δR* | Scalar – `1` |
| `Dual 1-axle`  `Dual 2-axle`  `Dual 3-axle` | δR=[δrlδrr]  or  [δrlδrr] | Array – `[1x2]` or `[2x1]` |

#### Dependencies

To enable this port, under **Input signals**,
select **Rear wheel steering**.

### **xdotin** — Longitudinal velocity `scalar`

Vehicle CG velocity along the vehicle-fixed *x*-axis,
in m/s.

#### Dependencies

To enable this port, set **Axle forces** to
`External longitudinal
velocity`.

### **FwF** — Total force on the front wheels `scalar` | `array`

Force on the front wheels,
*FwF*, along the vehicle-fixed
axis, in N.

| **Vehicle Track** Setting | **Axle Forces** Setting | Description | Variable | Signal Dimension |
| --- | --- | --- | --- | --- |
| `Single 1-axle`  `Single 2-axle`  `Single 3-axle` | `External longitudinal forces` | Longitudinal force on the front wheel | FwF=Fxf | Scalar – `1` |
| `External forces` | Longitudinal and lateral forces on the front wheel | FwF=[FxfFyf]  or [FxfFyf] | Array – `[1x2]` or `[2x1]` |
| `Dual 1-axle`  `Dual 2-axle`  `Dual 3-axle` | `External longitudinal forces` | Longitudinal force on the front wheels | FwF=[FxflFxfr] or [FxflFxfr] | Array – `[1x2]` or `[2x1]` |
| `External forces` | Longitudinal and lateral forces on the front wheels | FwF=[FxflFyflFxfrFyfr] | Array – `[2x2]` |

#### Dependencies

To enable this port, set **Axle forces** to one of these options:

- `External longitudinal forces`
- `External forces`

### **FwM** — Total force on the middle wheels `scalar` | `array`

Force on the middle wheels,
*FwM*, along the vehicle-fixed
axis, in N.

| **Vehicle Track** Setting | **Axle Forces** Setting | Description | Variable | Signal Dimension |
| --- | --- | --- | --- | --- |
| `Single 3-axle` | `External longitudinal forces` | Longitudinal force on the middle wheel | FwM=Fxr | Scalar – `1` |
| `External forces` | Longitudinal and lateral forces on the middle wheel | FwM=[FxmFym]  or [FxmFym] | Array – `[1x2]` or `[2x1]` |
| `Dual 3-axle` | `External longitudinal forces` | Longitudinal force on the middle wheels | FwM=[FxmlFxmr] or [FxmlFxmr] | Array – `[1x2]` or `[2x1]` |
| `External forces` | Longitudinal and lateral forces on the middle wheels | FwM=[FxmlFxmrFymlFymr] | Array – `[2x2]` |

#### Dependencies

To enable this port, set:

- **Vehicle track** to
  `Single 3-axle` or
  `Dual 3-axle`.
- **Axle forces** to
  `External longitudinal
  forces` or `External
  forces`.

### **FwR** — Total force on the rear wheels `scalar` | `array`

Force on the rear wheels,
*FwR*, along the vehicle-fixed
axis, in N.

| **Vehicle Track** Setting | **Axle Forces** Setting | Description | Variable | Signal Dimension |
| --- | --- | --- | --- | --- |
| `Single 2-axle`  `Single 3-axle` | `External longitudinal forces` | Longitudinal force on the rear wheel | FwR=Fxr | Scalar – `1` |
| `External forces` | Longitudinal and lateral forces on the rear wheel | FwR=[FxrFyr]  or [FxrFyr] | Array – `[1x2]` or `[2x1]` |
| `Dual 2-axle`  `Dual 3-axle` | `External longitudinal forces` | Longitudinal force on the rear wheels | FwR=[FxrlFxrr] or [FxrlFxrr] | Array – `[1x2]` or `[2x1]` |
| `External forces` | Longitudinal and lateral forces on the rear wheels | FwR=[FxrlFyrlFxrrFyrr] | Array – `[2x2]` |

#### Dependencies

To enable this port, set:

- **Vehicle track** to
  `Single 3-axle`,
  `Single 2-axle`,
  `Dual 3-axle` or
  `Dual 2-axle`.
- **Axle forces** to
  `External longitudinal
  forces` or `External
  forces`.

### **FExt** — External force on the vehicle CG `array`

External forces applied to the vehicle CG,
*Fxext*,
*Fyext*,
*Fzext*, in
vehicle-fixed frame, in N. The signal vector dimensions are
`[1x3]` or `[3x1]`.

#### Dependencies

To enable this port, under **Input signals**,
select **External forces**.

### **MExt** — External moment about vehicle CG `array`

External moment about the vehicle CG,
*Mx*,
*My*,
*Mz*, in the
vehicle-fixed frame, in N·m. The signal vector dimensions are
`[1x3]` or `[3x1]`.

#### Dependencies

To enable this port, under **Input signals**,
select **External moments**.

### **FhF** — Front hitch force on the body `array`

Hitch force applied to the body at the front hitch location,
*FhFx*,
*FhFy*,
*FhFz*, in the vehicle-fixed frame, in
N, specified as a `1-by-3` or `3-by-1` array.

#### Dependencies

To enable this port, under **Input signals**, select
**Front hitch forces**.

### **MhF** — Front hitch moment about body `array`

Hitch moment at the front hitch location,
*MhFx*,
*MhFy*,
*MhFz*, about the
vehicle-fixed frame, in N·m, specified as a `1-by-3` or
`3-by-1` array.

#### Dependencies

To enable this port, under **Input signals**, select
**Front hitch moments**.

### **FhR** — Rear hitch force on the body `array`

Hitch force applied to the body at the rear hitch location,
*FhRx*,
*FhRy*,
*FhRz*, in the vehicle-fixed frame, in
N, specified as a `1-by-3` or `3-by-1` array.

#### Dependencies

To enable this port, under **Input signals**, select
**Rear hitch forces**.

### **MhR** — Rear hitch moment about body `array`

Hitch moment at the rear hitch location,
*MhRx*,
*MhRy*,
*MhRz*, about the
vehicle-fixed frame, in N·m, specified as a `1-by-3` or
`3-by-1` array.

#### Dependencies

To enable this port, under **Input signals**, select
**Rear hitch moments**.

### **WindXYZ** — Wind speed `array`

Wind speed, *Wx*,
*Wy*,
*Wz*, along the inertial
*X*-, *Y*-, and
*Z*-axes, in m/s. The signal vector dimensions
are `1-by-3` or `3-by-1`.

#### Dependencies

To enable this port, under **Input signals**,
select **External wind**.

### **Mu** — Tire friction coefficient `array`

Tire friction coefficient, *μ*. The value is
dimensionless.

| **Vehicle Track** Setting | Description | Variable | Signal Dimension |
| --- | --- | --- | --- |
| `Single 1-axle` | Friction coefficient on the wheels | Mu=μf | Array – `[1x1]` |
| `Dual 1-axle` | Friction coefficient on the wheels | Mu=[μflμfr] or [μflμfr] | Array – `[1x2]` or `[2x1]` |
| `Single 2-axle` | Friction coefficient on the wheels | Mu=[μfμr] or [μfμr] | Array – `[1x2]` or `[2x1]` |
| `Dual 2-axle` | Friction coefficient on the wheels | Mu=[μflμfrμrlμrr] | Array – `[2x2]` |
| `Single 3-axle` | Friction coefficient on the wheels | Mu=[μfμmμr] or [μfμmμr] | Array – `[1x3]` or `[3x1]` |
| `Dual 3-axle` | Friction coefficient on the wheels | Mu=[μflμfrμmlμmrμrlμrr] | Array – `[3x2]` |

#### Dependencies

To enable this port, under **Input signals**,
select **External friction**.

### **AirTemp** — Ambient air temperature `scalar`

Ambient air temperature, in K.

#### Dependencies

To enable this port, under **Input signals**,
select **Air temperature**.

### **X\_o** — Initial longitudinal position `scalar`

Initial vehicle CG displacement along the earth-fixed
*X*-axis, in m.

#### Dependencies

To enable this port, under **Input signals**,
select **Initial longitudinal position**.

### **Y\_o** — Initial lateral position `scalar`

Initial vehicle CG displacement along the earth-fixed
*Y*-axis, in m.

#### Dependencies

To enable this port, under **Input signals**,
select **Initial lateral position**.

### **xdot\_o** — Initial longitudinal position `scalar`

Initial vehicle CG velocity along the vehicle-fixed
*x*-axis, in m/s.

#### Dependencies

To enable this port:

1. Set **Axle forces** to one of these options:

   - `External longitudinal
     forces`
   - `External
     forces`
2. Under **Input signals**, select
   **Initial longitudinal
   velocity**

### **ydot\_o** — Initial lateral position `scalar`

Initial vehicle CG velocity along the vehicle-fixed
*y*-axis, in m/s.

#### Dependencies

To enable this port, under **Input signals**,
select **Initial lateral velocity**.

### **psi\_o** — Initial yaw angle `scalar`

Rotation of the vehicle-fixed frame about the earth-fixed
*Z*-axis (yaw), in rad.

#### Dependencies

To enable this port, under **Input signals**,
select **Initial yaw angle**.

### **r\_o** — Initial yaw rate `scalar`

Vehicle angular velocity about the vehicle-fixed
*z*-axis (yaw rate), in rad/s.

#### Dependencies

To enable this port, under **Input signals**,
select **Initial yaw rate**.
### Output

### **Info** — Trailer data bus

Trailer data, returned as a bus signal containing these block
values.

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
| `FrntAxl` | `Lft` | `Disp` | `X` | | Front left wheel displacement along the earth-fixed *X*-axis | Computed | m |
| `Y` | | Front left wheel displacement along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | Front left wheel displacement along the earth-fixed *Z*-axis | `0` | m |
| `Vel` | `Xdot` | | Front left wheel velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | Front left wheel velocity along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | Front left wheel velocity along the earth-fixed *Z*-axis | `0` | m/s |
| `Rght` | `Disp` | `X` | | Front right wheel displacement along the earth-fixed *X*-axis | Computed | m |
| `Y` | | Front right wheel displacement along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | Front right wheel displacement along the earth-fixed *Z*-axis | `0` | m |
| `Vel` | `Xdot` | | Front right wheel velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | Front right wheel velocity along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | Front right wheel velocity along the earth-fixed *Z*-axis | `0` | m/s |
| `MidlAxl` | `Lft` | `Disp` | `X` | | Middle left wheel displacement along the earth-fixed *X*-axis | Computed | m |
| `Y` | | Middle left wheel displacement along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | Middle left wheel displacement along the earth-fixed *Z*-axis | `0` | m |
| `Vel` | `Xdot` | | Middle left wheel velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | Middle left wheel velocity along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | Middle left wheel velocity along the earth-fixed *Z*-axis | `0` | m/s |
| `Rght` | `Disp` | `X` | | Middle right wheel displacement along the earth-fixed *X*-axis | Computed | m |
| `Y` | | Middle right wheel displacement along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | Middle right wheel displacement along the earth-fixed *Z*-axis | `0` | m |
| `Vel` | `Xdot` | | Middle right wheel velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | Middle right wheel velocity along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | Middle right wheel velocity along the earth-fixed *Z*-axis | `0` | m/s |
| `RearAxl` | `Lft` | `Disp` | `X` | | Rear left wheel displacement along the earth-fixed *X*-axis | Computed | m |
| `Y` | | Rear left wheel displacement along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | Rear left wheel displacement along the earth-fixed *Z*-axis | `0` | m |
| `Vel` | `Xdot` | | Rear left wheel velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | Rear left wheel velocity along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | Rear left wheel velocity along the earth-fixed *Z*-axis | `0` | m/s |
| `Rght` | `Disp` | `X` | | Rear right wheel displacement along the earth-fixed *X*-axis | Computed | m |
| `Y` | | Rear right wheel displacement along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | Rear right wheel displacement along the earth-fixed *Z*-axis | `0` | m |
| `Vel` | `Xdot` | | Rear right wheel velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | Rear right wheel velocity along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | Rear right wheel velocity along the earth-fixed *Z*-axis | `0` | m/s |
| `Geom` | `Disp` | `X` | | | Trailer body offset from the axle plane along the earth-fixed *X*-axis | Computed | m |
| `Y` | | | Trailer body offset from the center plane along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | | Trailer body offset from the axle plane along the earth-fixed *Z*-axis | Computed | m |
| `Vel` | `Xdot` | | | Trailer body offset velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | | Trailer body offset velocity along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | | Trailer body offset velocity along the earth-fixed *Z*-axis | Computed | m/s |
| `HitchF` | `Disp` | `X` | | | Trailer front hitch offset from the axle plane along the earth-fixed *X*-axis | Computed | m |
| `Y` | | | Trailer front hitch offset from the center plane along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | | Trailer front hitch offset from the axle plane along the earth-fixed *Z*-axis | Computed | m |
| `Vel` | `Xdot` | | | Trailer front hitch offset velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | | Trailer front hitch offset velocity along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | | Trailer front hitch offset velocity along the earth-fixed *Z*-axis | Computed | m/s |
| `HitchR` | `Disp` | `X` | | | Trailer rear hitch offset from the axle plane along the earth-fixed *X*-axis | Computed | m |
| `Y` | | | Trailer rear hitch offset from the center plane along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | | Trailer rear hitch offset from the axle plane along the earth-fixed *Z*-axis | Computed | m |
| `Vel` | `Xdot` | | | Trailer rear hitch offset velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | | Trailer rear hitch offset velocity along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | | Trailer rear hitch offset velocity along the earth-fixed *Z*-axis | Computed | m/s |
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
| `Forces` | `Body` | `Fx` | | | Net force on the vehicle CG along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | | Net force on the vehicle CG along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | | Net force on the vehicle CG along the vehicle-fixed *z*-axis | `0` | N |
| `Ext` | `Fx` | | | External force on the vehicle CG along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | | External force on the vehicle CG along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | | External force on the vehicle CG along the vehicle-fixed *z*-axis | `0` | N |
| `HitchF` | `Fx` | | | Hitch front force applied to the body at the hitch location along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | | Hitch front force applied to the body at the hitch location along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | | Hitch front force applied to the body at the hitch location along the vehicle-fixed *z*-axis | Computed | N |
| `HitchR` | `Fx` | | | Hitch rear force applied to the body at the hitch location along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | | Hitch rear force applied to the body at the hitch location along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | | Hitch rear force applied to the body at the hitch location along the vehicle-fixed *z*-axis | Computed | N |
| `FrntAxl` | `Lft` | `Fx` | | Longitudinal force on the left front wheel along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on the left front wheel along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Normal force on the left front wheel along the vehicle-fixed *z*-axis | Computed | N |
| `Rght` | `Fx` | | Longitudinal force on the right front wheel along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on the right front wheel along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Normal force on the right front wheel along the vehicle-fixed *z*-axis | Computed | N |
| `MidlAxl` | `Lft` | `Fx` | | Longitudinal force on the left middle wheel along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on the left middle wheel along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Normal force on the left middle wheel along the vehicle-fixed *z*-axis | Computed | N |
| `Rght` | `Fx` | | Longitudinal force on the right middle wheel along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on the right middle wheel along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Normal force on the right middle wheel along the vehicle-fixed *z*-axis | Computed | N |
| `RearAxl` | `Lft` | `Fx` | | Longitudinal force on the left rear wheel along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on the left rear wheel along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Normal force on the left rear wheel along the vehicle-fixed *z*-axis | Computed | N |
| `Rght` | `Fx` | | Longitudinal force on the right rear wheel along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on the right rear wheel along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Normal force on the right rear wheel along the vehicle-fixed *z*-axis | Computed | N |
| `Tires` | `FrntTires` | `Lft` | `Fx` | Front left tire force along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | Front left tire force along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | Front left tire force along the vehicle-fixed *z*-axis | Computed | N |
| `Rght` | `Fx` | Front right tire force along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | Front right tire force along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | Front right tire force along the vehicle-fixed *z*-axis | Computed | N |
| `RearTires` | `Lft` | `Fx` | Rear left tire force along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | Rear left tire force along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | Rear left tire force along the vehicle-fixed *z*-axis | Computed | N |
| `Rght` | `Fx` | Rear right tire force along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | Rear right tire force along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | Rear right tire force along the vehicle-fixed *z*-axis | Computed |  |
| `Drag` | `Fx` | | | Drag force on the vehicle CG along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | | Drag force on the vehicle CG along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | | Drag force on the vehicle CG along the vehicle-fixed *z*-axis | Computed | N |
| `Grvty` | `Fx` | | | Gravity force on the vehicle CG along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | | Gravity force on the vehicle CG along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | | Gravity force on the vehicle CG along the vehicle-fixed *z*-axis | Computed | N |
| `Moments` | `Body` | `Mx` | | | Body moment on the vehicle CG about the vehicle-fixed *x*-axis | `0` | N·m |
| `My` | | | Body moment on the vehicle CG about the vehicle-fixed *y*-axis | Computed | N·m |
| `Mz` | | | Body moment on the vehicle CG about the vehicle-fixed *z*-axis | `0` | N·m |
| `Drag` | `Mx` | | | Drag moment on the vehicle CG about the vehicle-fixed *x*-axis | `0` | N·m |
| `My` | | | Drag moment on the vehicle CG about the vehicle-fixed *y*-axis | Computed | N·m |
| `Mz` | | | Drag moment on the vehicle CG about the vehicle-fixed *z*-axis | `0` | N·m |
| `Ext` | `Mx` | | | External moment on the vehicle CG about the vehicle-fixed *x*-axis | `0` | N·m |
| `My` | | | External moment on the vehicle CG about the vehicle-fixed *y*-axis | Computed | N·m |
| `Mz` | | | External moment on the vehicle CG about the vehicle-fixed *z*-axis | `0` | N·m |
| `HitchF` | `Mx` | | | Hitch moment at the front hitch location about vehicle-fixed *x*-axis | `0` | N·m |
| `My` | | | Hitch moment at the front hitch location about vehicle-fixed *y*-axis | Computed | N·m |
| `Mz` | | | Hitch moment at the front hitch location about vehicle-fixed *z*-axis | `0` | N·m |
| `HitchR` | `Mx` | | | Hitch moment at the rear hitch location about vehicle-fixed *x*-axis | `0` | N·m |
| `My` | | | Hitch moment at the rear hitch location about vehicle-fixed *y*-axis | Computed | N·m |
| `Mz` | | | Hitch moment at the rear hitch location about vehicle-fixed *z*-axis | `0` | N·m |
| `FrntAxl` | `Lft` | `Disp` | `x` | | Front left wheel displacement along the vehicle-fixed *x*-axis | Computed | m |
| `y` | | Front left wheel displacement along the vehicle-fixed *y*-axis | Computed | m |
| `z` | | Front left wheel displacement along the vehicle-fixed *z*-axis | Computed | m |
| `Vel` | `xdot` | | Front left wheel velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Front left wheel velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | Front left wheel velocity along the vehicle-fixed *z*-axis | `0` | m/s |
| `Rght` | `Disp` | `x` | | Front right wheel displacement along the vehicle-fixed *x*-axis | Computed | m |
| `y` | | Front right wheel displacement along the vehicle-fixed *y*-axis | Computed | m |
| `z` | | Front right wheel displacement along the vehicle-fixed *z*-axis | Computed | m |
| `Vel` | `xdot` | | Front right wheel velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Front right wheel velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | Front right wheel velocity along the vehicle-fixed *z*-axis | `0` | m/s |
| `Steer` | `WhlAngFL` | | | Front left wheel steering angle | Computed | rad |
| `WhlAngFR` | | | Front right wheel steering angle | Computed | rad |
| `MidlAxl` | `Lft` | `Disp` | `x` | | Middle left wheel displacement along the vehicle-fixed *x*-axis | Computed | m |
| `y` | | Middle left wheel displacement along the vehicle-fixed *y*-axis | Computed | m |
| `z` | | Middle left wheel displacement along the vehicle-fixed *z*-axis | Computed | m |
| `Vel` | `xdot` | | Middle left wheel velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Middle left wheel velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | Middle left wheel velocity along the vehicle-fixed *z*-axis | `0` | m/s |
| `Rght` | `Disp` | `x` | | Middle right wheel displacement along the vehicle-fixed *x*-axis | Computed | m |
| `y` | | Middle right wheel displacement along the vehicle-fixed *y*-axis | Computed | m |
| `z` | | Middle right wheel displacement along the vehicle-fixed *z*-axis | Computed | m |
| `Vel` | `xdot` | | Middle right wheel velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Middle right wheel velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | Middle right wheel velocity along the vehicle-fixed *z*-axis | `0` | m/s |
| `Steer` | `WhlAngRL` | | | Middle left wheel steering angle | Computed | rad |
| `WhlAngRR` | | | Middle right wheel steering angle | Computed | rad |
| `RearAxl` | `Lft` | `Disp` | `x` | | Rear left wheel displacement along the vehicle-fixed *x*-axis | Computed | m |
| `y` | | Rear left wheel displacement along the vehicle-fixed *y*-axis | Computed | m |
| `z` | | Rear left wheel displacement along the vehicle-fixed *z*-axis | Computed | m |
| `Vel` | `xdot` | | Rear left wheel velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Rear left wheel velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | Rear left wheel velocity along the vehicle-fixed *z*-axis | `0` | m/s |
| `Rght` | `Disp` | `x` | | Rear right wheel displacement along the vehicle-fixed *x*-axis | Computed | m |
| `y` | | Rear right wheel displacement along the vehicle-fixed *y*-axis | Computed | m |
| `z` | | Rear right wheel displacement along the vehicle-fixed *z*-axis | Computed | m |
| `Vel` | `xdot` | | Rear right wheel velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Rear right wheel velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | Rear right wheel velocity along the vehicle-fixed *z*-axis | `0` | m/s |
| `Steer` | `WhlAngRL` | | | Rear left wheel steering angle | Computed | rad |
| `WhlAngRR` | | | Rear right wheel steering angle | Computed | rad |
| `HitchF` | `Disp` | | `x` | | Front hitch offset from axle plane along the vehicle-fixed *x*-axis | Input | m |
| `y` | | Front hitch offset from center plane along the vehicle-fixed *y*-axis | Input | m |
| `z` | | Front hitch offset from axle plane along the earth-fixed *z*-axis | Input | m |
| `Vel` | | `xdot` | | Front hitch offset velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Front hitch offset velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | Front hitch offset velocity along the vehicle-fixed *z*-axis | `0` | m/s |
| `HitchR` | `Disp` | | `x` | | Rear hitch offset from axle plane along the vehicle-fixed *x*-axis | Input | m |
| `y` | | Rear hitch offset from center plane along the vehicle-fixed *y*-axis | Input | m |
| `z` | | Rear hitch offset from axle plane along the earth-fixed *z*-axis | Input | m |
| `Vel` | | `xdot` | | Rear hitch offset velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Rear hitch offset velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | Rear hitch offset velocity along the vehicle-fixed *z*-axis | `0` | m/s |
| `Pwr` | `Ext` | | | | Applied external power | Computed | W |
| `HitchF` | | | | Front hitch power | Computed | W |
| `HitchR` | | | | Rear hitch power | Computed | W |
| `Drag` | | | | Power loss due to drag | Computed | W |
| `Geom` | `Disp` | | `x` | | Trailer offset from axle plane along the vehicle-fixed *x*-axis | Input | m |
| `y` | | Trailer offset from center plane along the vehicle-fixed *y*-axis | Input | m |
| `z` | | Trailer offset from axle plane along the vehicle-fixed *z*-axis | Input | m |
| `Vel` | | `xdot` | | Trailer offset velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Trailer offset velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | Trailer offset velocity along the vehicle-fixed *z*-axis | `0` | m/s |
| `Ang` | | `Beta` | | Body slip angle, *β*    β=VyVx | Computed | rad |

| Signal | | | Description | | Value | Units |
| --- | --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` | `PwrFxExt` | Externally applied longitudinal force power | | Computed | W |
| `PwrFyExt` | Externally applied lateral force power | | Computed | W |
| `PwrMzExt` | Externally applied yaw moment power | | Computed | W |
| `PwrFwFLx` | Longitudinal force applied at the front left axle power | | Computed | W |
| `PwrFwFLy` | Lateral force applied at the front left axle power | | Computed | W |
| `PwrFwFRx` | Longitudinal force applied at the front right axle power | | Computed | W |
| `PwrFwFRy` | Lateral force applied at the front right axle power | | Computed | W |
| `PwrFwMLx` | Longitudinal force applied at the middle left axle power | | Computed | W |
| `PwrFwMLy` | Lateral force applied at the middle left axle power | | Computed | W |
| `PwrFwMRx` | Longitudinal force applied at the middle right axle power | | Computed | W |
| `PwrFwMRy` | Lateral force applied at the middle right axle power | | Computed | W |
| `PwrFwRLx` | Longitudinal force applied at the rear left axle power | | Computed | W |
| `PwrFwRLy` | Lateral force applied at the rear left axle power | | Computed | W |
| `PwrFwRRx` | Longitudinal force applied at the rear right axle power | | Computed | W |
| `PwrFwRRy` | Lateral force applied at the rear right axle power | | Computed | W |
| `PwrNotTrnsfrd` | `PwrFxDrag` | Longitudinal drag force power | | Computed | W |
| `PwrFyDrag` | Lateral drag force power | | Computed | W |
| `PwrMzDrag` | Drag pitch moment power | | Computed | W |
| `PwrStored` | `PwrStoredGrvty` | Rate change in gravitational potential energy | | Computed | W |
| `PwrStoredxdot` | Rate of change of longitudinal kinetic energy | | Computed | W |
| `PwrStoredydot` | Rate of change of lateral kinetic energy | | Computed | W |
| `PwrStoredr` | Rate of change of rotational yaw kinetic energy | | Computed | W |

### **xdot** — Trailer longitudinal velocity `scalar`

Trailer CG velocity along the vehicle-fixed *x*-axis,
in m/s.

### **ydot** — Trailer lateral velocity `scalar`

Trailer CG velocity along the vehicle-fixed *y*-axis,
in m/s.

### **psi** — Yaw `scalar`

Rotation of the vehicle-fixed frame about the earth-fixed
*Z*-axis (yaw), in rad.

### **r** — Yaw rate `scalar`

Vehicle angular velocity, *r*, about the
vehicle-fixed *z*-axis (yaw rate), in rad/s.

### **FzF** — Normal force on the front wheels `scalar` | `array`

Normal force on the front wheels,
*FzF*, along the
vehicle-fixed *z*-axis, in N.

| **Vehicle Track** Setting | Description | Variable | Signal Dimension |
| --- | --- | --- | --- |
| `Single 2-axle`  `Single 3-axle` | Normal force on the front axle | FzF=Fzf | Scalar – `1` |
| `Dual 2-axle`  `Dual 3-axle` | Normal force on the front wheels | FzF=[FzflFzfr] | Array – `[1x2]` |

### **FzM** — Normal force on the middle wheels `scalar` | `array`

Normal force on the middle wheels,
*FzM*, along the
vehicle-fixed *z*-axis, in N.

| **Vehicle Track** Setting | Description | Variable | Signal Dimension |
| --- | --- | --- | --- |
| `Single 3-axle` | Normal force on the middle axle | FzM=Fzm | Scalar – `1` |
| `Dual 3-axle` | Normal force on the right and left middle wheels | FzM=[FzmlFzrl] | Array – `[1x2]` |

#### Dependencies

To enable this port, set **Vehicle track** to
`Single 3-axle` or `Dual
3-axle`.

### **FzR** — Normal force on the rear wheels `scalar` | `array`

Normal force on the rear wheels,
*FzR*, along the
vehicle-fixed *z*-axis, in N.

| **Vehicle Track** Setting | Description | Variable | Signal Dimension |
| --- | --- | --- | --- |
| `Single 2-axle`  `Single 3-axle` | Normal force on the rear wheel | FzR=Fzr | Scalar – `1` |
| `Dual 2-axle`  `Dual 3-axle` | Normal force on the rear wheels | FzR=[FzrlFzrr] | Array – `[1x2]` |

### **Fhz** — Normal component of hitch force on the body `scalar`

Normal hitch force applied to the body at the hitch location,
*Fhz*, in the
vehicle-fixed frame *z*-axis, in N.

If you enable the **Hitch forces** parameter, the
block offsets the normal hitch force,
*Fhz*, with the value of
the *Fh* input port component along the vehicle-fixed
*z*-axis.
## Parameters
```yaml
parameters:
- name: Vehicle track
  summary: Type of vehicle track Dual 2-axle (default) | Single 1-axle | Dual 1-axle | Single 2-axle | Dual 3-axle
  group: ''
- name: Axle forces
  summary: Type of axle force External forces (default) | External longitudinal velocity | External longitudinal forces
  group: ''
- name: Front wheel steering
  summary: WhlAngF input port off (default) | on
  group: ''
- name: Middle wheel steering
  summary: WhlAngM input port off (default) | on
  group: ''
- name: Rear wheel steering
  summary: WhlAngR input port off (default) | on
  group: ''
- name: External wind
  summary: WindXYZ input port off (default) | on
  group: ''
- name: External friction
  summary: Mu input port off (default) | on
  group: ''
- name: External forces
  summary: FExt input port off (default) | on
  group: ''
- name: External moments
  summary: MExt input port off (default) | on
  group: ''
- name: Front hitch forces
  summary: FhF input port on (default) | off
  group: ''
- name: Front hitch moments
  summary: MhF input port on (default) | off
  group: ''
- name: Rear hitch forces
  summary: FhR input port off (default) | on
  group: ''
- name: Rear hitch moments
  summary: MhR input port off (default) | on
  group: ''
- name: Initial longitudinal position
  summary: X_o input port off (default) | on
  group: ''
- name: Initial yaw angle
  summary: psi_o input port off (default) | on
  group: ''
- name: Initial longitudinal velocity
  summary: xdot_o input port off (default) | on
  group: ''
- name: Initial yaw rate
  summary: r_o input port off (default) | on
  group: ''
- name: Initial lateral position
  summary: Y_o input port off (default) | on
  group: ''
- name: Air temperature
  summary: AirTemp input port off (default) | on
  group: ''
- name: Initial lateral velocity
  summary: ydot_o input port off (default) | on
  group: ''
- name: Number of wheels on front axle, NF
  summary: Front wheel count 2 (default) | scalar
  group: ''
- name: Number of wheels on middle axle, NM
  summary: Middle wheel count 2 (default) | scalar
  group: ''
- name: Number of wheels on rear axle, NR
  summary: Rear wheel count 2 (default) | scalar
  group: ''
- name: Vehicle mass, m
  summary: Vehicle mass 26000 (default) | scalar
  group: ''
- name: Longitudinal distance from center of mass to front axle, a
  summary: Distance from CM to front axle 4 (default) | scalar
  group: ''
- name: Longitudinal distance from center of mass to middle axle, b
  summary: Distance from CM to middle axle 4.5 (default) | scalar
  group: ''
- name: Longitudinal distance from center of mass to rear axle, c
  summary: Distance from CM to rear axle 5 (default) | scalar
  group: ''
- name: Vertical distance from center of mass to axle plane, h
  summary: Distance from CM to axle plane 2 (default) | scalar
  group: ''
- name: Longitudinal distance from center of mass to front hitch, dh_f
  summary: Distance to front hitch 7.5 (default) | scalar
  group: ''
- name: Vertical distance from front hitch to axle plane, hh_f
  summary: Distance from front hitch to axle plane 0.6 (default) | scalar
  group: ''
- name: Longitudinal distance from center of mass to rear hitch, dh_r
  summary: Distance to front hitch 7.5 (default) | scalar
  group: ''
- name: Vertical distance from front hitch to axle plane, hh_r
  summary: Distance from rear hitch to axle plane 0.6 (default) | scalar
  group: ''
- name: Initial inertial frame longitudinal position, X_o
  summary: Initial inertial X location 0 (default) | scalar
  group: ''
- name: Initial longitudinal velocity, xdot_o
  summary: Initial velocity 0 (default) | scalar
  group: ''
- name: Mapped corner stiffness
  summary: Selection off (default) | on
  group: ''
- name: Include relaxation length dynamics
  summary: Enable relaxation length dynamics on (default) | off
  group: ''
- name: Lateral distance from geometric centerline to center of mass, d
  summary: Distance from centerline to CM 0 (default) | scalar
  group: ''
- name: Lateral distance from geometric centerline to front hitch, hl_f
  summary: Distance from centerline to front hitch 0 (default) | scalar
  group: ''
- name: Lateral distance from geometric centerline to rear hitch, hl_r
  summary: Distance from centerline to rear hitch 0 (default) | scalar
  group: ''
- name: Front track width, w_f
  summary: Front track width 1.82 (default) | scalar
  group: ''
- name: Middle track width, w_m
  summary: Middle track width 1.82 (default) | scalar
  group: ''
- name: Rear track width, w_r
  summary: Rear track width 1.82 (default) | scalar
  group: ''
- name: Front axle tire corner stiffness, Cy_f
  summary: Front axle tire stiffness 12.3 (default) | scalar
  group: ''
- name: Middle axle tire corner stiffness, Cy_m
  summary: Middle axle tire stiffness 11.3 (default) | scalar
  group: ''
- name: Rear axle tire corner stiffness, Cy_r
  summary: Rear axle tire stiffness 11.3 (default) | scalar
  group: ''
- name: Front tire(s) relaxation length, sigma_f
  summary: Relaxation length .1 (default) | scalar
  group: ''
- name: Middle tire(s) relaxation length, sigma_m
  summary: Relaxation length .1 (default) | scalar
  group: ''
- name: Rear tire(s) relaxation length, sigma_r
  summary: Relaxation length .1 (default) | scalar
  group: ''
- name: Front axle slip angle breakpoints, alpha_f_brk
  summary: Breakpoints [-.1 .1] (default) | vector
  group: ''
- name: Front axle corner data, Cy_f_data
  summary: Breakpoints [-9e3 9e3] (default) | vector
  group: ''
- name: Middle axle slip angle breakpoints, alpha_m_brk
  summary: Breakpoints [-.1 .1] (default) | vector
  group: ''
- name: Middle axle corner data, Cy_m_data
  summary: Breakpoints [-9e3 9e3] (default) | vector
  group: ''
- name: Rear axle slip angle breakpoints, alpha_r_brk
  summary: Breakpoints [-.1 .1] (default) | vector
  group: ''
- name: Rear axle corner data, Cy_r_data
  summary: Data [-9e3 9e3] (default) | vector
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
- name: Absolute air pressure, Pabs
  summary: Pressure 101325 (default) | scalar
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
- name: Wrap Euler angles, wrapAng
  summary: Wrap the Euler angles to the interval [-pi, pi] off (default) | on
  group: ''
```

#### Options

### **Vehicle track** — Type of vehicle track `Dual 2-axle` (default) | `Single 1-axle` | `Dual 1-axle` | `Single 2-axle` | `Dual 3-axle`

Use the **Vehicle track** parameter to specify the number of wheels.

| Vehicle Track Setting | Implementation |
| --- | --- |
| `Single 1-axle` | Trailer with a single track and one axle.  - Forces act along the center line of the   axle. - No lateral load transfer. |
| `Dual 1-axle` | Trailer with a dual track and one axle. Forces act at the axle hard-point locations. |
| `Single 2-axle` | Trailer with a single track and two axles.  - Forces act along the center line of the axles. - No lateral load transfer. |
| `Dual 2-axle`(default) | Trailer with a dual track and two axles. Forces act at the axle hard-point locations. |
| `Single 3-axle` | Trailer with a single track and three axles.  - Forces act along the center line of the axles. - No lateral load transfer. |
| `Dual 3-axle` | Trailer with a dual track and three axles. Forces act at the axle hard-point locations. |

### **Axle forces** — Type of axle force `External forces` (default) | `External longitudinal velocity` | `External longitudinal forces`

Use the **Axle forces** parameter to specify the type of force.

| Axle Forces Setting | Implementation |
| --- | --- |
| `External longitudinal velocity` | - The block assumes that the external longitudinal velocity   is in a quasi-steady state, and the longitudinal   acceleration is approximately zero. - Because the motion is quasi-steady, the block calculates   lateral forces using the tire slip angles and linear   cornering stiffness. - Consider this setting when you want to:  - Generate virtual sensor signal data.   - Conduct high-level software studies that are not impacted by driveline or nonlinear tire responses. |
| `External longitudinal forces` | - The block uses the external longitudinal force to   accelerate or brake the vehicle. - The block calculates lateral forces using the tire slip   angles and linear cornering stiffness. - Consider this setting when you want to:  - Account for changes in the longitudinal velocity on the lateral and yaw motion.   - Specify the external longitudinal motion through a force instead of an external longitudinal velocity.   - Connect the block to tractive actuators, wheels, brakes, and hitches. |
| `External forces` | - The block uses the external lateral and longitudinal   forces to steer, accelerate, or brake the vehicle. - The block does not use the steering input to calculate   vehicle motion. - Consider this setting when you need tire models with more   accurate nonlinear combined lateral and longitudinal   slip. |

#### Input Signals

### **Front wheel steering** — `WhlAngF` input port `off` (default) | `on`

Select to create input port `WhlAngF`.

### **Middle wheel steering** — `WhlAngM` input port `off` (default) | `on`

Select to create input port `WhlAngM`.

#### Dependencies

To enable this parameter, set **Vehicle track** to
`Single 3-axle` or `Dual
3-axle`.

### **Rear wheel steering** — `WhlAngR` input port `off` (default) | `on`

Select to create input port `WhlAngR`.

#### Dependencies

To enable this parameter, set **Vehicle track** to
`Single 2-axle`, `Dual
2-axle`, `Single 3-axle`, or
`Dual 3-axle`.

### **External wind** — `WindXYZ` input port `off` (default) | `on`

Select to create input port `WindXYZ`.

### **External friction** — `Mu` input port `off` (default) | `on`

Select to create input port `Mu`.

#### Dependencies

To enable this parameter, set **Axle forces** to one
of these options:

- `External longitudinal
  forces`
- `External forces`

### **External forces** — `FExt` input port `off` (default) | `on`

Select to create input port `FExt`.

### **External moments** — `MExt` input port `off` (default) | `on`

Select to create input port `MExt`.

### **Front hitch forces** — `FhF` input port `on` (default) | `off`

Select to create input port `Fh`.

### **Front hitch moments** — `MhF` input port `on` (default) | `off`

Select to create input port `Mh`.

### **Rear hitch forces** — `FhR` input port `off` (default) | `on`

Select to create input port `Fh`.

### **Rear hitch moments** — `MhR` input port `off` (default) | `on`

Select to create input port `Mh`.

### **Initial longitudinal position** — `X_o` input port `off` (default) | `on`

Select to create input port `X_o`.

### **Initial yaw angle** — `psi_o` input port `off` (default) | `on`

Select to create input port `psi_o`.

### **Initial longitudinal velocity** — `xdot_o` input port `off` (default) | `on`

Select to create input port `xdot_o`.

#### Dependencies

To enable this parameter, set **Axle forces** to
`External longitudinal forces` or
`External forces`.

### **Initial yaw rate** — `r_o` input port `off` (default) | `on`

Select to create input port `r_o`.

### **Initial lateral position** — `Y_o` input port `off` (default) | `on`

Select to create input port `Y_o`.

### **Air temperature** — `AirTemp` input port `off` (default) | `on`

Select to create input port `AirTemp`.

### **Initial lateral velocity** — `ydot_o` input port `off` (default) | `on`

Select to create input port `ydot_o`.

#### Longitudinal

### **Number of wheels on front axle, NF** — Front wheel count `2` (default) | `scalar`

Number of wheels on the front axle,
*NF*. The value is
dimensionless.

### **Number of wheels on middle axle, NM** — Middle wheel count `2` (default) | `scalar`

Number of wheels on the middle axle,
*NM*. The value is
dimensionless.

#### Dependencies

To enable this parameter, set **Vehicle track** to
`Single 3-axle` or `Dual
3-axle`.

### **Number of wheels on rear axle, NR** — Rear wheel count `2` (default) | `scalar`

Number of wheels on the rear axle,
*NR*. The value is
dimensionless.

To enable this parameter, set **Vehicle track** to
`Single 2-axle`, `Single
3-axle`, `Dual 2-axle`, or
`Dual 3-axle`.

### **Vehicle mass, m** — Vehicle mass `26000` (default) | `scalar`

Vehicle mass, *m*, in kg.

### **Longitudinal distance from center of mass to front axle, a** — Distance from CM to front axle `4` (default) | `scalar`

Distance from the vehicle CM to the front axle, *a*, in m.

Side view of trailer showing longitudinal axle and hitch distances from CM

### **Longitudinal distance from center of mass to middle axle, b** — Distance from CM to middle axle `4.5` (default) | `scalar`

Distance from vehicle CM to middle axle, *b*, in m.

Side view of trailer showing longitudinal axle and hitch distances from CM

#### Dependencies

To enable this parameter, set **Vehicle track** to
`Single 3-axle` or `Dual
3-axle`.

### **Longitudinal distance from center of mass to rear axle, c** — Distance from CM to rear axle `5` (default) | `scalar`

Distance from vehicle CM to the front axle, *c*, in m.

Side view of trailer showing longitudinal axle and hitch distances from CM

#### Dependencies

To enable this parameter, set **Vehicle track** to
`Single 2-axle`, `Single
3-axle`, `Single 3-axle`, or
`Dual 3-axle`.

### **Vertical distance from center of mass to axle plane, h** — Distance from CM to axle plane `2` (default) | `scalar`

Vertical distance from vehicle CM to the axle plane, *h*,
in m.

Side view of trailer showing longitudinal axle and hitch distances from CM

### **Longitudinal distance from center of mass to front hitch, dh\_f** — Distance to front hitch `7.5` (default) | `scalar`

Longitudinal distance from the center of mass to the front hitch,
*dh\_f*, in m.

Side view of trailer showing longitudinal axle and hitch distances from CM

#### Dependencies

To enable this parameter, on the **Input signals** pane, select
**Front hitch forces** or **Front hitch
moments**.

### **Vertical distance from front hitch to axle plane, hh\_f** — Distance from front hitch to axle plane `0.6` (default) | `scalar`

Vertical distance from the front hitch to the axle plane,
*hh\_f*, in m.

Side view of trailer showing longitudinal axle and hitch distances from CM

#### Dependencies

To enable this parameter, on the **Input signals** pane, select
**Front hitch forces** or **Front hitch
moments**.

### **Longitudinal distance from center of mass to rear hitch, dh\_r** — Distance to front hitch `7.5` (default) | `scalar`

Longitudinal distance from the center of mass to the rear hitch,
*dh\_r*, in m.

Side view of trailer showing longitudinal axle and hitch distances from CM

#### Dependencies

To enable this parameter, on the **Input signals** pane, select
**Rear hitch forces** or **Rear hitch
moments**.

### **Vertical distance from front hitch to axle plane, hh\_r** — Distance from rear hitch to axle plane `0.6` (default) | `scalar`

Vertical distance from the rear hitch to the axle plane,
*hh\_r*, in m.

Side view of trailer showing longitudinal axle and hitch distances from CM

#### Dependencies

To enable this parameter, on the **Input signals** pane, select
**Rear hitch forces** or **Rear hitch
moments**.

### **Initial inertial frame longitudinal position, X\_o** — Initial inertial X location `0` (default) | `scalar`

Initial vehicle CG displacement along the earth-fixed
*X*-axis, in m.

### **Initial longitudinal velocity, xdot\_o** — Initial velocity `0` (default) | `scalar`

Initial vehicle CG velocity along the vehicle-fixed
*x*-axis, in m/s.

#### Dependencies

To enable this parameter, set **Axle forces** to one
of these options:

- `External longitudinal
  forces`
- `External forces`

#### Lateral

### **Mapped corner stiffness** — Selection `off` (default) | `on`

Enables mapped corner stiffness calculation.

#### Dependencies

To enable this parameter, set **Axle forces** to one
of these options:

- `External longitudinal
  velocity`
- `External longitudinal
  forces`

### **Include relaxation length dynamics** — Enable relaxation length dynamics `on` (default) | `off`

Enables relaxation length dynamics.

#### Dependencies

To enable this parameter:

1. Set **Axle forces** to one of these options:

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
2. Clear **Mapped corner stiffness**.

### **Lateral distance from geometric centerline to center of mass, d** — Distance from centerline to CM `0` (default) | `scalar`

Lateral distance from the geometric centerline to the center of mass,
*d*, in m, along the vehicle-fixed
*y*. Positive values indicate that the trailer CM is
to the right of the geometric centerline. Negative values indicate that the
trailer CM is to the left of the geometric centerline.

Top down view of track widths and CM offset from centerline

### **Lateral distance from geometric centerline to front hitch, hl\_f** — Distance from centerline to front hitch `0` (default) | `scalar`

Lateral distance from the geometric centerline to the front hitch,
*hl\_f*, in m, along the vehicle-fixed *y*.
Positive values indicate that the trailer hitch is to the right of the geometric
centerline. Negative values indicate that the trailer hitch is to the left of the
geometric centerline.

Top down view of axle widths and CM offset from centerline

#### Dependencies

To enable this parameter, on the **Input signals** pane, select
**Front hitch forces** or **Front hitch
moments**.

### **Lateral distance from geometric centerline to rear hitch, hl\_r** — Distance from centerline to rear hitch `0` (default) | `scalar`

Lateral distance from the geometric centerline to the rear hitch,
*hl\_r*, in m, along the vehicle-fixed *y*.
Positive values indicate that the trailer hitch is to the right of the geometric
centerline. Negative values indicate that the trailer hitch is to the left of the
geometric centerline.

Top down view of axle widths and CM offset from centerline

#### Dependencies

To enable this parameter, on the **Input signals** pane, select
**Rear hitch forces** or **Rear hitch
moments**.

### **Front track width, w\_f** — Front track width `1.82` (default) | `scalar`

Front track width, *wf*, in m.

Top down view of track widths and CM offset from centerline

#### Dependencies

To enable this parameter, set **Vehicle track** to
`Dual 2-axle`, `Dual
2-axle`, or `Dual
3-axle`.

### **Middle track width, w\_m** — Middle track width `1.82` (default) | `scalar`

Middle track width, *wm*, in m.

Top down view of track widths and CM offset from centerline

#### Dependencies

To enable this parameter, set **Vehicle track** to
`Dual 3-axle`.

### **Rear track width, w\_r** — Rear track width `1.82` (default) | `scalar`

Rear track width, *wr*, in m.

Top down view of track widths and CM offset from centerline

#### Dependencies

To enable this parameter, set **Vehicle track** to
`Dual 2-axle` or `Dual
3-axle`.

### **Front axle tire corner stiffness, Cy\_f** — Front axle tire stiffness `12.3` (default) | `scalar`

Front tire corner stiffness,
*Cyf*, in N/rad.

#### Dependencies

To enable this parameter:

1. Set **Axle forces** to one of these options:

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
2. Clear **Mapped corner stiffness**.

### **Middle axle tire corner stiffness, Cy\_m** — Middle axle tire stiffness `11.3` (default) | `scalar`

Middle tire corner stiffness,
*Cym*, in N/rad.

#### Dependencies

To enable this parameter:

1. Set **Vehicle track** to one of these options:

   - `Single
     3-axle`
   - `Dual 3-axle`
2. Set **Axle forces** to one of these options:

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
3. Clear **Mapped corner stiffness**.

### **Rear axle tire corner stiffness, Cy\_r** — Rear axle tire stiffness `11.3` (default) | `scalar`

Rear tire corner stiffness, *Cyr*,
in N/rad.

#### Dependencies

To enable this parameter:

1. Set **Vehicle track** to one of these options:

   - `Single
     2-axle`
   - `Dual 2-axle`
   - `Single
     3-axle`
   - `Dual 3-axle`
2. Set **Axle forces** to one of these options:

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
3. Clear **Mapped corner stiffness**.

### **Front tire(s) relaxation length, sigma\_f** — Relaxation length `.1` (default) | `scalar`

Front tire relaxation length,
*σf*, in m.

#### Dependencies

To enable this parameter:

1. Set **Vehicle track** to one of these options:

   - `Single 2-axle`
   - `Dual 2-axle`
   - `Single 3-axle`
   - `Dual 3-axle`
2. Set **Axle forces** to one of these options:

   - `External longitudinal velocity`
   - `External longitudinal forces`
3. Do either of these:

   - Select **Mapped corner stiffness**.
   - Clear **Mapped corner stiffness** and select
     **Include relaxation length dynamics**.

### **Middle tire(s) relaxation length, sigma\_m** — Relaxation length `.1` (default) | `scalar`

Middle tire relaxation length,
*σm*, in m.

#### Dependencies

To enable this parameter:

1. Set **Vehicle track** to one of these options:

   - `Single
     3-axle`
   - `Dual 3-axle`
2. Set **Axle forces** to one of these options:

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
3. Do either of these:

   - Select **Mapped corner
     stiffness**.
   - Clear **Mapped corner
     stiffness** and select **Include
     relaxation length dynamics**.

### **Rear tire(s) relaxation length, sigma\_r** — Relaxation length `.1` (default) | `scalar`

Rear tire relaxation length, *σr*,
in m.

#### Dependencies

To enable this parameter:

1. Set **Vehicle track** to one of these options:

   - `Single 2-axle`
   - `Dual 2-axle`
   - `Single 3-axle`
   - `Dual 3-axle`
2. Set **Axle forces** to one of these options:

   - `External longitudinal velocity`
   - `External longitudinal forces`
3. Do either of these:

   - Select **Mapped corner stiffness**.
   - Clear **Mapped corner stiffness** and select
     **Include relaxation length dynamics**.

### **Front axle slip angle breakpoints, alpha\_f\_brk** — Breakpoints `[-.1 .1]` (default) | `vector`

Front axle slip angle breakpoints,
*αfbrk*, in rad.

#### Dependencies

To enable this parameter:

1. Set **Axle forces** to one of these options:

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. Select **Mapped corner stiffness**.

### **Front axle corner data, Cy\_f\_data** — Breakpoints `[-9e3 9e3]` (default) | `vector`

Front axle corner data, *Cyfdata*,
in N/rad.

#### Dependencies

To enable this parameter:

1. Set **Axle forces** to one of these options:

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. Select **Mapped corner stiffness**.

### **Middle axle slip angle breakpoints, alpha\_m\_brk** — Breakpoints `[-.1 .1]` (default) | `vector`

Middle axle slip angle breakpoints,
*αmbrk*, in rad.

#### Dependencies

To enable this parameter:

1. Set **Axle forces** to one of these options:

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. Select **Mapped corner stiffness**.

### **Middle axle corner data, Cy\_m\_data** — Breakpoints `[-9e3 9e3]` (default) | `vector`

Middle axle corner data,
*Cymdata*, in N/rad.

#### Dependencies

To enable this parameter:

1. Set **Axle forces** to one of these options:

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. Select **Mapped corner stiffness**.

### **Rear axle slip angle breakpoints, alpha\_r\_brk** — Breakpoints `[-.1 .1]` (default) | `vector`

Rear axle slip angle breakpoints,
*αrbrk*, in rad.

#### Dependencies

To enable this parameter:

1. Set **Axle forces** to one of these options:

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. Select **Mapped corner stiffness**.

### **Rear axle corner data, Cy\_r\_data** — Data `[-9e3 9e3]` (default) | `vector`

Rear axle corner data, *Cyrdata*,
in N/rad.

#### Dependencies

To enable this parameter:

1. Set **Axle forces** to one of these options:

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. Select **Mapped corner stiffness**.

### **Initial inertial frame lateral displacement, Y\_o** — Position `0` (default) | `scalar`

Initial vehicle CG displacement along the earth-fixed
*Y*-axis, in m.

### **Initial lateral velocity, ydot\_o** — Velocity `0` (default) | `scalar`

Initial vehicle CG velocity along the vehicle-fixed
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

### **Absolute air pressure, Pabs** — Pressure `101325` (default) | `scalar`

Environmental absolute pressure, *Pabs*,
in Pa.

### **Air temperature, Tair** — Temperature `273` (default) | `scalar`

Environmental absolute temperature, *T*, in K.

#### Dependencies

To enable this parameter, clear **Air temperature**.

### **Gravitational acceleration, g** — Gravity `9.81` (default) | `scalar`

Gravitational acceleration, *g*, in m/s^2.

### **Nominal friction scaling factor, mu** — Friction scale factor `1` (default) | `scalar`

Nominal friction scale factor, *μ*. The value is
dimensionless.

#### Dependencies

To enable this parameter:

1. Set **Axle forces** to one of these options:

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
2. Clear **External Friction**.

#### Simulation

### **Longitudinal velocity tolerance, xdot\_tol** — Tolerance `.01` (default) | `scalar`

Longitudinal velocity tolerance, in m/s.

### **Nominal normal force, Fznom** — Normal force `5000` (default) | `scalar`

Nominal normal force, in N.

#### Dependencies

To enable this parameter, set **Axle forces** to one of these options:

- `External longitudinal velocity`
- `External longitudinal forces`

### **Geometric longitudinal offset from axle plane, longOff** — Longitudinal offset `0` (default) | `scalar`

Vehicle chassis offset from the axle plane along the vehicle-fixed
*x*-axis, in m. When you use the 3D visualization engine,
consider using the offset to locate the chassis independently of the vehicle
CG.

### **Geometric lateral offset from center plane, latOff** — Lateral offset `0` (default) | `scalar`

Vehicle chassis offset from the center plane along the vehicle-fixed
*y*-axis, in m. When you use the 3D visualization engine,
consider using the offset to locate the chassis independently of the vehicle
CG.

### **Geometric vertical offset from axle plane, vertOff** — Vertical offset `0` (default) | `scalar`

Vehicle chassis offset from the axle plane along the vehicle-fixed
*z*-axis, in m. When you use the 3D visualization engine,
consider using the offset to locate the chassis independently of the vehicle
CG.

### **Wrap Euler angles, wrapAng** — Wrap the Euler angles to the interval `[-pi, pi]` `off` (default) | `on`

Wrap the Euler angles to the interval `[-pi, pi]`. For vehicle
maneuvers that might undergo vehicle yaw rotations that are outside of this
interval, consider clearing the parameter if you want to:

- Track the total vehicle yaw rotation.
- Avoid discontinuities in the vehicle state estimators.
## Libraries

Vehicle Dynamics Blockset / Vehicle Body

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Trailer body with longitudinal, lateral, and yaw motion

The Trailer Body 3DOF block implements a rigid one-axle, two-axle or
three-axle trailer body model to calculate longitudinal, lateral, and yaw motion.
Configure the block for a single or dual track. The block accounts for axle and hitch
reaction forces due to the trailer acceleration, aerodynamic drag, and steering.

Use this block in vehicle dynamics and automated driving studies to model nonholonomic
vehicle motion when vehicle pitch, roll, and vertical motion are not significant.

Use the **Vehicle track** parameter to specify the number of wheels.

| Vehicle Track Setting | Implementation |
| --- | --- |
| `Single 1-axle` | Trailer with a single track and one axle.  - Forces act along the center line of the   axle. - No lateral load transfer. |
| `Dual 1-axle` | Trailer with a dual track and one axle. Forces act at the axle hard-point locations. |
| `Single 2-axle` | Trailer with a single track and two axles.  - Forces act along the center line of the axles. - No lateral load transfer. |
| `Dual 2-axle`(default) | Trailer with a dual track and two axles. Forces act at the axle hard-point locations. |
| `Single 3-axle` | Trailer with a single track and three axles.  - Forces act along the center line of the axles. - No lateral load transfer. |
| `Dual 3-axle` | Trailer with a dual track and three axles. Forces act at the axle hard-point locations. |

Use the **Axle forces** parameter to specify the type of force.

| Axle Forces Setting | Implementation |
| --- | --- |
| `External longitudinal velocity` | - The block assumes that the external longitudinal velocity   is in a quasi-steady state, and the longitudinal   acceleration is approximately zero. - Because the motion is quasi-steady, the block calculates   lateral forces using the tire slip angles and linear   cornering stiffness. - Consider this setting when you want to:  - Generate virtual sensor signal data.   - Conduct high-level software studies that are not impacted by driveline or nonlinear tire responses. |
| `External longitudinal forces` | - The block uses the external longitudinal force to   accelerate or brake the vehicle. - The block calculates lateral forces using the tire slip   angles and linear cornering stiffness. - Consider this setting when you want to:  - Account for changes in the longitudinal velocity on the lateral and yaw motion.   - Specify the external longitudinal motion through a force instead of an external longitudinal velocity.   - Connect the block to tractive actuators, wheels, brakes, and hitches. |
| `External forces` | - The block uses the external lateral and longitudinal   forces to steer, accelerate, or brake the vehicle. - The block does not use the steering input to calculate   vehicle motion. - Consider this setting when you need tire models with more   accurate nonlinear combined lateral and longitudinal   slip. |

To create additional input ports, under **Input
signals**, select these block parameters.

| Input Signals Pane Parameter | Input Port | Description |
| --- | --- | --- |
| **Front wheel steering** | `WhlAngF` | Front wheel angle, *δF* |
| **Middle wheel steering** | `WhlAngM` | Middle wheel angle, *δM* |
| **Rear wheel steering** | `WhlAngR` | Rear wheel angle, *δR* |
| **External wind** | `WindXYZ` | Wind speed, *WX*, *WY*, and *WZ*, in an inertial reference frame |
| **External friction** | `Mu` | Friction coefficient |
| **External forces** | `FExt` | External force on the vehicle center of gravity (CG), *Fx*, *Fy*, and *Fz*, in the vehicle-fixed frame |
| **External moments** | `MExt` | External moment about the vehicle CG, *Mx*, *My*, and *Mz*, in the vehicle-fixed frame |
| **Front hitch forces** | `FhF` | Hitch force applied to the body at the front hitch location, *FhFx*, *FhFy*, and *FhFz*, in the vehicle-fixed frame |
| **Front hitch moments** | `MhF` | Hitch moment at the front hitch location, *MhFx*, *MhFy*, and *MhFz*, about the vehicle-fixed frame |
| **Rear hitch forces** | `FhR` | Hitch force applied to the body at the rear hitch location, *FhRx*, *FhRy*, and *FhRz*, in the vehicle-fixed frame |
| **Rear hitch moments** | `MhR` | Hitch moment at the rear hitch location, *MhRx*, *MhRy*, and *MhRz*, about the vehicle-fixed frame |
| **Initial longitudinal position** | `X_o` | Initial vehicle CG displacement along the earth-fixed *X*-axis |
| **Initial yaw angle** | `psi_o` | Initial rotation of the vehicle-fixed frame about the earth-fixed *Z*-axis (yaw) |
| **Initial longitudinal velocity** | `xdot_o` | Initial vehicle CG velocity along the vehicle-fixed *x*-axis |
| **Initial yaw rate** | `r_o` | Initial vehicle angular velocity about the vehicle-fixed *z*-axis (yaw rate) |
| **Initial lateral position** | `Y_o` | Initial vehicle CG displacement along the earth-fixed *Y*-axis |
| **Air temperature** | `AirTemp` | Ambient air temperature. Consider this option if you want to vary the temperature during run time. |
| **Initial lateral velocity** | `ydot_o` | Initial vehicle CG velocity along the vehicle-fixed *y*-axis |

### Theory

To determine the vehicle motion, the block solves the rigid body planar dynamics
equations of motion.

**Signal Track**

| Calculation | Description |
| --- | --- |
| *Dynamics* | The block uses these equations to calculate the rigid body planar dynamics.  y¨=−x˙r+Fyf+Fym+Fyr+Fyext+Fhyf+Fhyrmr˙=−aFyf−bFym−cFyr+dhfFhyf−dhrFhyr+Mzext+Mhzf+MhzrIzzr=ψ˙  If you set **Axle forces** to either `External longitudinal forces` or `External forces`, the block uses this equation for the longitudinal acceleration.  x¨=y˙r+Fxf+Fxm+Fxr−gsin(γ)+Fxext+Fhxf+Fhxrm  If you set **Axle forces** to `External longitudinal velocity`, the block assumes a quasi-steady state for the longitudinal acceleration.  x¨=0 |
| *External forces* | External forces include both drag and external force inputs. The forces act on the vehicle CG.  Fx,y,z ext=Fd x,y,z+Fx,y,z inputMx,y,z ext=Md x,y,z+Mx,y,z input    If you set **Axle forces** to `External longitudinal forces`, the block uses these equations.  Fxft=FxfinputFyft=−CyfαfμfFzfFznomFxmt=FxminputFymt=−CymαmμmFzmFznomFxrt=FxrinputFyrt=−CyrαrμrFzrFznom    If you set **Axle forces** to `External longitudinal velocity`, the block uses these equations.  Fxft=0Fyft=−CyfαfμfFzfFznomFxmt=0Fymt=−CymαmμmFzmFznomFxrt=0Fyrt=−CyrαrμrFzrFznom    The block divides the normal forces by the nominal normal load to vary the effective friction parameters during weight and load transfer. The block maintains pitch and roll equilibrium.  Fzf=bmgcos(γ)−(x¨−y˙r)mh+hFxext+bFzext−Myexta+bFzr=amgcos(γ)+(x¨−y˙r)mh−hFxext+aFzext+Myexta+b |
| *Tire forces* | The block uses the ratio of the local, longitudinal, and lateral velocities to determine the slip angles.  αf=atan(y˙−arx˙)−δfαm=atan(y˙−brx˙)−δmαr=atan(y˙−crx˙)−δr    The block uses the steering angles to transform the tire forces to the vehicle-fixed frame.  Fxf=Fxftcos(δf)−Fyftsin(δf)Fyf=−Fxftsin(δf)+Fyftcos(δf)Fxm=Fxmtcos(δm)−Fymtsin(δm)Fym=−Fxmtsin(δm)+Fymtcos(δm)Fxr=Fxrtcos(δr)−Fyrtsin(δr)Fyr=−Fxrtsin(δr)+Fyrtcos(δr)    If you set **Axle forces** to `External forces`, the block assumes that the externally provided forces are in the vehicle-fixed frame at the axle-wheel location.  Fxf=Fxft=FxfinputFyf=Fyft=FyfinputFxm=Fxmt=FxminputFym=Fymt=FyminputFxr=Fxrt=FxrinputFyr=Fyrt=Fyrinput |

**Single Track — Three Axles**

Isometric view of vertical, longitudinal, and lateral forces acting at three axle locations

**Single Track — Two Axles**

Isometric view of vertical, longitudinal, and lateral forces acting at two axle locations

**Single Track — One Axle**

Isometric view of vertical, longitudinal, and lateral forces acting at one axle location

**Dual Track**

| Calculation | Description |
| --- | --- |
| *Dynamics* | The block uses these equations to calculate the rigid body planar dynamics.  x¨=y˙r+Fxfl+Fxfr+Fxml+Fxmr+Fxrl+Fxrr−gsin(γ)+Fxext+Fhxf+Fhxrmy¨=−x˙r+Fyfl+Fyfr+Fyml+Fymr+Fyrl+Fyrr+Fyext+Fhyf+Fhyrmr˙=−a(Fyfl+Fyfr)−b(Fyml+Fymr)−c(Fyrl+Fyrr)+dhfFhyf−dhrFhyr+Fxfl(wf2+d)−Fxfr(wf2−d)+Fxml(wm2+d)−Fxmr(wm2−d)+Fxrl(wr2+d)−Fxrr(wr2−d)+Mzext+Mhfz+Mhrz−Fhxfhlf−FhxrhlrIzzr=ψ˙  If you set **Axle forces** to `External longitudinal velocity`, the block assumes a quasi-steady state for the longitudinal acceleration.  x¨=0 |
| *External forces* | External forces include both drag and external force inputs. The forces act on the vehicle CG.  Fx,y,z ext=Fd x,y,z+Fx,y,z inputMx,y,z ext=Md x,y,z+Mx,y,z input    If you set **Axle forces** to `External longitudinal forces`, the block uses these equations.  Fxflt=FxflinputFyflt=−CyflαflμflFzfl2FznomFxfrt=FxfrinputFyfrt=−CyfrαfrμfrFzfr2FznomFxmlt=FxmlinputFymlt=−CymlαmlμmlFzml2FznomFxmrt=FxmrinputFymrt=−CymrαmrμmrFzmr2FznomFxrlt=FxrlinputFyrlt=−CyrlαrlμrlFzrl2FznomFxrrt=FxrrinputFyrrt=−CyrrαrrμrrFzrr2Fznom    If you set **Axle forces** to `External longitudinal velocity`, the block uses these equations.  Fxflt=0Fyflt=−CyflαflμflFzfl2FznomFxfrt=0Fyfrt=−CyfrαfrμfrFzfr2FznomFxmlt=0Fymlt=−CymlαmlμmlFzml2FznomFxmrt=0Fymrt=−CymrαmrμmrFzmr2FznomFxrlt=0Fyrlt=−CyrlαrlμrlFzrl2FznomFxrrt=0Fyrrt=−CyrrαrrμrrFzrr2Fznom    The block divides the normal forces by the nominal normal load to vary the effective friction parameters during weight and load transfer. The block maintains pitch and roll equilibrium.  Fzf=bmgcos(γ)−(x¨−y˙r)mh+hFxext+bFzext−Myexta+bFzr=amgcos(γ)+(x¨−y˙r)mh−hFxext+aFzext+Myext(a+b)Fzfl=Fzf+(mh(y¨+x˙r)−hFyext−Mxext)2wfFzfr=Fzf+(−mh(y¨+x˙r)+hFyext+Mxext)2wfFzrl=Fzr+(mh(y¨+x˙r)−hFyext−Mxext)2wrFzrr=Fzr+(−mh(y¨+x˙r)+hFyext+Mxext)2wr |
| *Tire forces* | The block uses the ratio of the local, longitudinal, and lateral velocities to determine the slip angles.  αfl=atan(y˙−arx˙+rwf2)−δflαfr=atan(y˙−arx˙−rwf2)−δfrαml=atan(y˙−brx˙+rwm2)−δmlαmr=atan(y˙−brx˙−rwm2)−δmrαrl=atan(y˙−crx˙+rwr2)−δrlαrr=atan(y˙−crx˙−rwr2)−δrr    The block uses the steering angles to transform the tire forces to the vehicle-fixed frame.  Fxfl=Fxfltcos(δfl)−Fyfltsin(δfl)Fxfr=Fxfrtcos(δfr)−Fyfrtsin(δfr)Fxml=Fxmltcos(δml)−Fymltsin(δml)Fxmr=Fxmrtcos(δmr)−Fymrtsin(δmr)Fyfl=−Fxfltsin(δfl)+Fyfltcos(δfl)Fyfr=−Fxfrtsin(δfr)+Fyfrtcos(δfr)Fyml=−Fxmltsin(δml)+Fymltcos(δml)Fymr=−Fxmrtsin(δmr)+Fymrtcos(δmr)Fxrl=Fxrltcos(δrl)−Fyrltsin(δrl)Fxrr=Fxrrtcos(δrr)−Fyrrtsin(δrr)Fyrl=−Fxrltsin(δrl)+Fyrltcos(δrl)Fyrr=−Fxrrtsin(δrr)+Fyrrtcos(δrr)    If you set **Axle forces** to `External forces`, the block assumes that the externally provided forces are in the vehicle-fixed frame at the axle-wheel location.  Fxfl=Fxflt=FxflinputFxfr=Fxfrt=FxfrinputFxml=Fxmlt=FxmlinputFxmr=Fxmrt=FxmrinputFyfl=Fyflt=FyflinputFyfr=Fyfrt=FyfrinputFyml=Fymlt=FymlinputFymr=Fymrt=FymrinputFxrl=Fxrlt=FxrlinputFxrr=Fxrrt=FxrrinputFyrl=Fyrlt=FyrlinputFyrr=Fyrrt=Fyrrinput |

**Dual Track — Three Axles**

Isometric view of vertical, longitudinal, and lateral forces acting at dual track three axle locations

**Dual Track — Two Axles**

Isometric view of vertical, longitudinal, and lateral forces acting at dual track two axle locations

**Dual Track — One Axle**

Isometric view of vertical, longitudinal, and lateral forces acting at dual track one axle location

The illustrations use these variables.

|  |  |
| --- | --- |
| *a*, *b*, *c* | Longitudinal distance of the front, middle, and rear axles, respectively, from the normal projection point of the vehicle CG onto the common axle plane |
| *h* | Height of the tractor CG above the axle plane along the vehicle-fixed *z*-axis |
| *d* | Lateral distance from the geometric centerline to the center of mass along the vehicle-fixed *y*-axis |
| *hh\_f*, *hh\_r* | Height of the front and rear hitch, respectively, above the axle plane along the vehicle-fixed *z*-axis |
| *dh\_f*, *dh\_r* | Longitudinal distance of the front and rear hitch, respectively, from the normal projection point of tractor CG onto the common axle plane |
| *wf*, *wm*, *wr* | Front, middle, and rear track width, respectively |

**Drag**

This table summarizes the block implementation for the drag
calculation.

| Calculation | Description |
| --- | --- |
| *Coordinate transformation* | The block transforms the wind speeds from the inertial frame to the vehicle-fixed frame.  wx=Wxcos(ψ)+Wysin(ψ)wy=Wycos(ψ)−Wxsin(ψ)wz=Wz |
| *Drag forces* | To determine a relative airspeed, the block subtracts the wind speed from the CG vehicle velocity. Using the relative airspeed, the block determines the drag forces.  w¯=(x˙−wx)2+(y˙−wy)2+(wz)2Fdx=−12TRCdAfPabs(w¯)2Fdy=−12TRCsAfPabs(w¯)2Fdz=−12TRClAfPabs(w¯)2 |
| *Drag moments* | Using the relative airspeed, the block determines the drag moments.  Mdr=−12TRCrmAfPabs(w¯)2(dh+c)Mdp=−12TRCpmAfPabs(w¯)2(dh+c)Mdy=−12TRCymAfPabs(w¯)2(dh+c) |

**Lateral Corner Stiffness and Relaxation Dynamics**

To enable the mapped corner stiffness and relaxation length dynamic
parameters, set **Axle forces** to `External
longitudinal forces` or `External longitudinal
velocity`.

| Parameter Settings | | Description |
| --- | --- | --- |
| Mapped Corner Stiffness | Include Relaxation Length Dynamics |
| `Off` (default) | `On` (default) | The block uses constant corner stiffness values for *Cyf*, *Cym*, and *Cyr*.  The slip angles include the relaxation length dynamic settings. The relaxation length approximates an effective corner stiffness force that is a function of wheel travel. |
| `On` | `On` (default) | The block uses lookup tables that are functions of the corner stiffness data and slip angles.  Cyf=f(αfσ,Cyfdata)Cym=f(αmσ,Cymdata)Cyr=f(αrσ,Cyrdata)αfσ=1s[(αf−αfσ)vwfαf]αmσ=1s[(αm−αmσ)vmfαm]αrσ=1s[(αr−αrσ)vwrαr]    The slip angles include the relaxation length dynamic settings. The relaxation length approximates an effective corner stiffness force that is a function of wheel travel. |
| `Off` (default) | `Off` | The block uses constant corner stiffness values *Cyf*, *Cym* and *Cyr*. |

The equations use these variables.

|  |  |
| --- | --- |
| x,x˙,x¨ | Vehicle CG displacement, velocity, and acceleration, along the vehicle-fixed *x*-axis |
| y,y˙,y¨ | Vehicle CG displacement, velocity, and acceleration, along the vehicle-fixed *y*-axis |
| *ψ* | Rotation of the vehicle-fixed frame about the earth-fixed *Z*-axis (yaw) |
| *r*,Ψ˙ | Vehicle angular velocity, about the vehicle-fixed *z*-axis (yaw rate) |
| *Fxf*, *Fxm*, *Fxr* | Longitudinal forces applied to front, middle, and rear wheels, along the vehicle-fixed *x*-axis |
| *Fyf*, *Fym*, *Fyr* | Lateral forces applied to front, middle, and rear wheels, along vehicle-fixed *y*-axis |
| *Fxext*, *Fyext*, *Fzext* | External forces applied to vehicle CG, along the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *Fdx*, *Fdy*, *Fdz* | Drag forces applied to vehicle CG, along the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *Fxinput*, *Fyinput*, *Fzinput* | Input forces applied to vehicle CG, along the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *Mxext*, *Myext*, *Mzext* | External moment about vehicle CG, about the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *Mdx*, *Mdy*, *Mdz* | Drag moment about vehicle CG, about the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *Mxinput*, *Myinput*, *Mzinput* | Input moment about vehicle CG, about the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *Izz* | Vehicle body moment of inertia about the vehicle-fixed *z*-axis |
| *Fxft*, *Fxmt*, *Fxrt* | Longitudinal tire force applied to front, middle, and rear wheels, along the vehicle-fixed *x*-axis |
| *Fyft*, *Fymt*, *Fyrt* | Lateral tire force applied to front, middle, and rear wheels, along vehicle-fixed *y*-axis |
| *Fxfl*, *Fxfr* | Longitudinal force applied to front left and front right wheels, along the vehicle-fixed *x*-axis |
| *Fyfl*, *Fyfr* | Lateral force applied to front left and front right wheels, along the vehicle-fixed *y*-axis |
| *Fxrl*, *Fxrr* | Longitudinal force applied to rear left and rear right wheels, along the vehicle-fixed *x*-axis |
| *Fyrl*, *Fyrr* | Lateral force applied to rear left and rear right wheels, along the vehicle-fixed *y*-axis |
| *Fxflt*, *Fxfrt* | Longitudinal tire force applied to front left and front right wheels, along the vehicle-fixed *x*-axis |
| *Fxmlt*, *Fxmrt* | Longitudinal tire force applied to middle left and middle right wheels, along the vehicle-fixed *x*-axis |
| *Fxrlt*, *Fxrrt* | Longitudinal tire force applied to rear left and rear right wheels, along the vehicle-fixed *x*-axis |
| *Fyflt*, *Fyfrt* | Lateral force tire applied to front left and front right wheels, along the vehicle-fixed *y*-axis |
| *Fymlt*, *Fymrt* | Lateral force tire applied to middle left and middle right wheels, along the vehicle-fixed *y*-axis |
| *Fyrlt*, *Fyrrt* | Lateral force applied to rear left and rear right wheels, along the vehicle-fixed *y*-axis |
| *Fzf*,*Fzr* | Normal force applied to front and rear wheels, along vehicle-fixed *z*-axis |
| *Fznom* | Nominal normal force applied to axles, along the vehicle-fixed *z*-axis |
| *Fzfl*,*Fzfr* | Normal force applied to front left and right wheels, along vehicle-fixed *z*-axis |
| *Fzrl*,*Fzrr* | Normal force applied to rear left and right wheels, along vehicle-fixed *z*-axis |
| *m* | Vehicle body mass |
| *a*, *b* | Distance of front and rear wheels, respectively, from the normal projection point of vehicle CG onto the common axle plane |
| *h* | Height of vehicle CG above the axle plane |
| *d* | Lateral distance from the geometric centerline to the center of mass along the vehicle-fixed *y*-axis |
| *hh* | Height of the hitch above the axle plane along the vehicle-fixed *z*-axis |
| *dh* | Longitudinal distance of the hitch from the normal projection point of tractor CG onto the common axle plane |
| *hl* | Lateral distance from center of mass to hitch along the vehicle-fixed *y*-axis. |
| *αf*, *αr* | Front and rear wheel slip angles |
| *αfl*, *αfr* | Front left and right wheel slip angles |
| *αrl*, *αrr* | Rear left and right wheel slip angles |
| *δf*, *δr* | Front and rear wheel steering angles |
| *δrl*, *δrr* | Rear left and right wheel steering angles |
| *δfl*, *δfr* | Front left and right wheel steering angles |
| *wf*, *wr* | Front and rear track widths |
| *Cyf*, *Cyr* | Front and rear wheel cornering stiffness |
| *Cyfdata*, *Cyrdata* | Front and rear wheel cornering stiffness data |
| *σf*, *σr* | Front and rear wheel relaxation length |
| *αfσ*, *αrσ* | Front and rear wheel slip angles that include relaxation length |
| *vwf*, *vwr* | Magnitude of front and rear wheel hardpoint velocity |
| *μf*, *μr* | Front and rear wheel friction coefficient |
| *μfl*, *μfr* | Front left and right wheel friction coefficient |
| *μrl*, *μrr* | Rear left and right wheel friction coefficient |
| *Cd* | Air drag coefficient acting along vehicle-fixed *x*-axis |
| *Cs* | Air drag coefficient acting along vehicle-fixed *y*-axis |
| *Cl* | Air drag coefficient acting along vehicle-fixed *z*-axis |
| *Crm* | Air drag roll moment acting about the vehicle-fixed *x*-axis |
| *Cpm* | Air drag pitch moment acting about the vehicle-fixed *y*-axis |
| *Cym* | Air drag yaw moment acting about the vehicle-fixed *z*-axis |
| *Af* | Frontal area |
| *R* | Atmospheric specific gas constant |
| *T* | Environmental air temperature |
| *Pabs* | Environmental absolute pressure |
| *wx*, *wy*, *wz* | Wind speed, along the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *Wx*, *Wy*, *Wz* | Wind speed, along inertial *X*-, *Y*-, and *Z*-axes |
