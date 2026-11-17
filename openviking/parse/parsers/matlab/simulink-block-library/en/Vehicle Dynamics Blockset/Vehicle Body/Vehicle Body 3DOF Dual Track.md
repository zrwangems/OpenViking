---
type: simulink-block
title: 'Vehicle Body 3DOF'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Body'
documentation_page: 'vehiclebody3dof'
documentation_source_path: 'ref/vehiclebody3dof.html'
language: en
---

# Vehicle Body 3DOF

## Ports
```yaml
ports:
- name: WhlAngF
  summary: Front wheel steering angles scalar | array
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
- name: FwR
  summary: Total force on the rear wheels scalar | array
  direction: input
- name: FExt
  summary: External force on vehicle CG array
  direction: input
- name: MExt
  summary: External moment about vehicle CG array
  direction: input
- name: Fh
  summary: Hitch force on the body array
  direction: input
- name: Mh
  summary: Hitch moment about body array
  direction: input
- name: WindXYZ
  summary: Wind speed array
  direction: input
- name: Mu
  summary: Tire friction coefficient scalar
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
  summary: Bus signal bus
  direction: output
- name: xdot
  summary: Vehicle longitudinal velocity scalar
  direction: output
- name: ydot
  summary: Vehicle lateral velocity scalar
  direction: output
- name: psi
  summary: Yaw scalar
  direction: output
- name: r
  summary: Yaw rate scalar
  direction: output
- name: FzF
  summary: Normal force on front wheels scalar | array
  direction: output
- name: FzR
  summary: Normal force on rear wheels scalar | array
  direction: output
```

### Input

### **WhlAngF** — Front wheel steering angles `scalar` | `array`

Front wheel steering angles,
*δF*, in rad.

| **Vehicle Track** Setting | Variable | Signal Dimension |
| --- | --- | --- |
| `Single (bicycle)` | *δF* | Scalar – `1` |
| `Dual` | δF=[δflδfr]  or  [δflδfr] | Array – `[1x2]` or `[2x1]` |

#### Dependencies

To enable this port, on the **Input signals**
pane, select **Front wheel steering**.

### **WhlAngR** — Rear wheel steering angles `scalar` | `array`

Rear wheel steering angles,
*δR*, in rad.

| **Vehicle Track** Setting | Variable | Signal Dimension |
| --- | --- | --- |
| `Single (bicycle)` | *δR* | Scalar – `1` |
| `Dual` | δR=[δrlδrr]  or  [δrlδrr] | Array – `[1x2]` or `[2x1]` |

#### Dependencies

To enable this port, on the **Input signals**
pane, select **Rear wheel steering**.

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
| `Single (bicycle)` | `External longitudinal forces` | Longitudinal force on the front wheel | FwF=Fxf | Scalar – `1` |
| `External forces` | Longitudinal and lateral forces on the front wheel | FwF=[FxfFyf]  or [FxfFyf] | Array – `[1x2]` or `[2x1]` |
| `Dual` | `External longitudinal forces` | Longitudinal force on the front wheels | FwF=[FxflFxfr] or [FxflFxfr] | Array – `[1x2]` or `[2x1]` |
| `External forces` | Longitudinal and lateral forces on the front wheels | FwF=[FxflFyflFxfrFyfr] | Array – `[2x2]` |

#### Dependencies

To enable this port, set **Axle forces** to one of these options:

- `External longitudinal forces`
- `External forces`

### **FwR** — Total force on the rear wheels `scalar` | `array`

Force on the rear wheels,
*FwR*, along the vehicle-fixed
axis, in N.

| **Vehicle Track** Setting | **Axle Forces** Setting | Description | Variable | Signal Dimension |
| --- | --- | --- | --- | --- |
| `Single (bicycle)` | `External longitudinal forces` | Longitudinal force on the rear wheel | FwR=Fxr | Scalar – `1` |
| `External forces` | Longitudinal and lateral forces on the rear wheel | FwR=[FxrFyr]  or [FxrFyr] | Array – `[1x2]` or `[2x1]` |
| `Dual` | `External longitudinal forces` | Longitudinal force on the rear wheels | FwR=[FxrlFxrr] or [FxrlFxrr] | Array – `[1x2]` or `[2x1]` |
| `External forces` | Longitudinal and lateral forces on the rear wheels | FwR=[FxrlFyrlFxrrFyrr] | Array – `[2x2]` |

#### Dependencies

To enable this port, set **Axle forces** to one of these options:

- `External longitudinal forces`
- `External forces`

### **FExt** — External force on vehicle CG `array`

External forces applied to vehicle CG,
*Fxext*,
*Fyext*,
*Fzext*, in
vehicle-fixed frame, in N. Signal vector dimensions are
`[1x3]` or `[3x1]`.

#### Dependencies

To enable this port, on the **Input signals**
pane, select **External forces**.

### **MExt** — External moment about vehicle CG `array`

External moment about vehicle CG,
*Mx*,
*My*,
*Mz*, in the vehicle-fixed
frame, in N·m. Signal vector dimensions are `[1x3]` or
`[3x1]`.

#### Dependencies

To enable this port, on the **Input signals**
pane, select **External moments**.

### **Fh** — Hitch force on the body `array`

Hitch force applied to the body at the hitch location,
*Fhx*,
*Fhy*,
*Fhz*, in the vehicle-fixed frame, in N,
specified as a `1-by-3` or `3-by-1` array.

#### Dependencies

To enable this port, under **Input signals**, select
**Hitch forces**.

### **Mh** — Hitch moment about body `array`

Hitch moment at the hitch location, *Mhx*,
*Mhy*,
*Mhz*, about the
vehicle-fixed frame, in N·m, specified as a `1-by-3` or
`3-by-1` array.

#### Dependencies

To enable this port, under **Input signals**, select **Hitch
moments**.

### **WindXYZ** — Wind speed `array`

Wind speed, *Wx*,
*Wy*,
*Wz* along inertial
*X*-, *Y*-, and
*Z*-axes, in m/s. Signal vector dimensions are
`[1x3]` or `[3x1]`.

#### Dependencies

To enable this port, on the **Input signals**
pane, select **External wind**.

### **Mu** — Tire friction coefficient `scalar`

Tire friction coefficient, *μ*. The value is dimensionless.

| **Vehicle Track** Setting | Description | Variable | Signal Dimension |
| --- | --- | --- | --- |
| `Single (bicycle)` | Longitudinal force on the front wheel | Mu=[μfμr] or [μfμr] | Array – `[1x2]` or `[2x1]` |
| `Dual` | Longitudinal force on the front wheels | Mu=[μflμfrμrlμrr] | Array – `[2x2]` |

#### Dependencies

To enable this port, on the **Input signals**
pane, select **External friction**.

### **AirTemp** — Ambient air temperature `scalar`

Ambient air temperature, in K.

#### Dependencies

To enable this port, on the **Input signals**
pane, select **Air temperature**.

### **X\_o** — Initial longitudinal position `scalar`

Initial vehicle CG displacement along the earth-fixed
*X*-axis, in m.

#### Dependencies

To enable this port, on the **Input signals**
pane, select **Initial longitudinal
position**.

### **Y\_o** — Initial lateral position `scalar`

Initial vehicle CG displacement along the earth-fixed
*Y*-axis, in m.

#### Dependencies

To enable this port, on the **Input signals**
pane, select **Initial lateral position**.

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
2. On the **Input signals** pane, select
   **Initial longitudinal
   velocity**

### **ydot\_o** — Initial lateral position `scalar`

Initial vehicle CG velocity along the vehicle-fixed
*y*-axis, in m/s.

#### Dependencies

To enable this port, on the **Input signals**
pane, select **Initial lateral velocity**.

### **psi\_o** — Initial yaw angle `scalar`

Rotation of the vehicle-fixed frame about the earth-fixed
*Z*-axis (yaw), in rad.

#### Dependencies

To enable this port, on the **Input signals**
pane, select **Initial yaw angle**.

### **r\_o** — Initial yaw rate `scalar`

Initial vehicle angular velocity about the vehicle-fixed
*z*-axis (yaw rate), in rad/s.

#### Dependencies

To enable this port, on the **Input signals**
pane, select **Initial yaw rate**.
### Output

### **Info** — Bus signal bus

Bus signal containing these block values.

| Signal | | | | | | Description | Value | Units |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `InertFrm` | `Cg` | `Disp` | `X` | | | Vehicle CG displacement along the earth-fixed *X*-axis | Computed relative to the road grade. | m |
| `Y` | | | Vehicle CG displacement along the earth-fixed *Y*-axis | Computed relative to the road grade. | m |
| `Z` | | | Vehicle CG displacement along the earth-fixed *Z*-axis | `0` | m |
| `Vel` | `Xdot` | | | Vehicle CG velocity along the earth-fixed *X*-axis | Computed relative to the road grade. | m/s |
| `Ydot` | | | Vehicle CG velocity along the earth-fixed *Y*-axis | Computed relative to the road grade. | m/s |
| `Zdot` | | | Vehicle CG velocity along the earth-fixed *Z*-axis | `0` | m/s |
| `Ang` | `phi` | | | Rotation of the vehicle-fixed frame about the earth-fixed *X*-axis (roll) | `0` | rad |
| `theta` | | | Rotation of the vehicle-fixed frame about the earth-fixed *Y*-axis (pitch) | `0` | rad |
| `psi` | | | Rotation of the vehicle-fixed frame about the earth-fixed *Z*-axis (yaw) | Computed relative to the grade angle. | rad |
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
| `Hitch` | `Disp` | `X` | | | Hitch offset from axle plane along the earth-fixed *X*-axis | Computed | m |
| `Y` | | | Hitch offset from center plane along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | | Hitch offset from axle plane along the earth-fixed *Z*-axis | Computed | m |
| `Vel` | `Xdot` | | | Hitch offset velocity from axle plane along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | | Hitch offset velocity from center plane along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | | Hitch offset velocity from axle plane along the earth-fixed *Z*-axis | Computed | m/s |
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
| `Acc` | `ax` | | | Vehicle CG inertial acceleration along the vehicle-fixed *x*-axis | Computed | gn |
| `ay` | | | Vehicle CG inertial acceleration along the vehicle-fixed *y*-axis | Computed | gn |
| `az` | | | Vehicle CG inertial acceleration along the vehicle-fixed *z*-axis | `0` | gn |
| `xddot` | | | Vehicle CG acceleration along the vehicle-fixed *x*-axis, excluding the centrifugal component | Computed | m/s^2 |
| `yddot` | | | Vehicle CG acceleration along the vehicle-fixed *y*-axis, excluding the centrifugal component | Computed | m/s^2 |
| `zddot` | | | Vehicle CG acceleration along the vehicle-fixed *z*-axis, excluding the centrifugal component | `0` | m/s^2 |
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
| `FrntAxl` | `Lft` | `Fx` | | Longitudinal force on left front wheel, along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on left front wheel along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Normal force on left front wheel, along the vehicle-fixed *z*-axis | Computed | N |
| `Rght` | `Fx` | | Longitudinal force on right front wheel, along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on right front wheel along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Normal force on right front wheel, along the vehicle-fixed *z*-axis | Computed | N |
| `RearAxl` | `Lft` | `Fx` | | Longitudinal force on left rear wheel, along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on left rear wheel along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Normal force on left rear wheel, along the vehicle-fixed *z*-axis | Computed | N |
| `Rght` | `Fx` | | Longitudinal force on right rear wheel, along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on right rear wheel along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Normal force on right rear wheel, along the vehicle-fixed *z*-axis | Computed | N |
| `Tires` | `FrntTires` | `Lft` | `Fx` | Front left tire force, along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | Front left tire force, along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | Front left tire force, along the vehicle-fixed *z*-axis | Computed | N |
| `Rght` | `Fx` | Front right tire force, along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | Front right tire force, along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | Front right tire force, along the vehicle-fixed *z*-axis | Computed | N |
| `RearTires` | `Lft` | `Fx` | Rear left tire force, along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | Rear left tire force, along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | Rear left tire force, along the vehicle-fixed *z*-axis | Computed | N |
| `Rght` | `Fx` | Rear right tire force, along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | Rear right tire force, along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | Rear right tire force, along the vehicle-fixed *z*-axis | Computed |  |
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
| `Hitch` | `Disp` | | `x` | | Hitch offset from axle plane along the vehicle-fixed *x*-axis | Input | m |
| `y` | | Hitch offset from center plane along the vehicle-fixed *y*-axis | Input | m |
| `z` | | Hitch offset from axle plane along the vehicle-fixed *z*-axis | Input | m |
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
| `Beta` | | `Beta` | | Body slip angle, *β*    β=VyVx | Computed | rad |

| Signal | | | Description | | Value | Units |
| --- | --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` | `PwrFxExt` | Externally applied longitudinal force power | | Computed | W |
| `PwrFyExt` | Externally applied lateral force power | | Computed | W |
| `PwrMzExt` | Externally applied roll moment power | | Computed | W |
| `PwrFwFLx` | Longitudinal force applied at the front left axle power | | Computed | W |
| `PwrFwFLy` | Lateral force applied at the front left axle power | | Computed | W |
| `PwrFwFRx` | Longitudinal force applied at the front right axle power | | Computed | W |
| `PwrFwFRy` | Lateral force applied at the front right axle power | | Computed | W |
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

### **xdot** — Vehicle longitudinal velocity `scalar`

Vehicle CG velocity along the vehicle-fixed *x*-axis,
in m/s.

### **ydot** — Vehicle lateral velocity `scalar`

Vehicle CG velocity along the vehicle-fixed *y*-axis,
in m/s.

### **psi** — Yaw `scalar`

Rotation of the vehicle-fixed frame about the earth-fixed
*Z*-axis (yaw), in rad.

### **r** — Yaw rate `scalar`

Vehicle angular velocity, `r`, about the
vehicle-fixed *z*-axis (yaw rate), in rad/s.

### **FzF** — Normal force on front wheels `scalar` | `array`

Normal force on front wheels,
*FzF*, along the vehicle-fixed
*z*-axis, in N.

| **Vehicle Track** Setting | Description | Variable | Signal Dimension |
| --- | --- | --- | --- |
| `Single (bicycle)` | Normal force on front axle | FzF=Fzf | Scalar – `1` |
| `Dual` | Normal force on the front wheels | FzF=[FzflFzfr] | Array – `[1x2]` |

### **FzR** — Normal force on rear wheels `scalar` | `array`

Normal force on rear wheels,
*FzR*, along the vehicle-fixed
*z*-axis, in N.

| **Vehicle Track** Setting | Description | Variable | Signal Dimension |
| --- | --- | --- | --- |
| `Single (bicycle)` | Normal force on rear wheel | FzR=Fzr | Scalar – `1` |
| `Dual` | Normal force on the rear wheels | FzR=[FzrlFzrr] | Array – `[1x2]` |
## Parameters
```yaml
parameters:
- name: Vehicle track
  summary: Number of wheels Single (bicycle) | Dual
  group: ''
- name: Axle forces
  summary: Type of axle force External longitudinal velocity | External longitudinal forces | External forces
  group: ''
- name: Front wheel steering
  summary: WhlAngF input port on (default) | off
  group: ''
- name: External wind
  summary: WindXYZ input port off (default) | on
  group: ''
- name: External forces
  summary: FExt input port off (default) | on
  group: ''
- name: External moments
  summary: MExt input port off (default) | on
  group: ''
- name: Rear wheel steering
  summary: WhlAngR input port off (default) | on
  group: ''
- name: External friction
  summary: Mu input port off (default) | on
  group: ''
- name: Hitch forces
  summary: Fh input port off (default) | on
  group: ''
- name: Hitch moments
  summary: Mh input port off (default) | on
  group: ''
- name: Initial longitudinal position
  summary: X_o input port off (default) | on
  group: ''
- name: Initial lateral position
  summary: Y_o input port off (default) | on
  group: ''
- name: Initial longitudinal velocity
  summary: xdot_o input port off (default) | on
  group: ''
- name: Initial lateral velocity
  summary: ydot_o input port off (default) | on
  group: ''
- name: Initial yaw angle
  summary: psi_o input port off (default) | on
  group: ''
- name: Initial yaw rate
  summary: r_o input port off (default) | on
  group: ''
- name: Air temperature
  summary: AirTemp input port off (default) | on
  group: ''
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
- name: Longitudinal distance from center of mass to hitch, dh
  summary: Distance from CM to hitch 1 (default) | scalar
  group: ''
- name: Vertical distance from hitch to axle plane, hh
  summary: Distance from hitch to axle plane 0.2 (default) | scalar
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
- name: Mapped corner stiffness
  summary: Selection off (default) | on
  group: ''
- name: Include relaxation length dynamics
  summary: Enable relaxation length dynamics on (default) | off
  group: ''
- name: Lateral distance from geometric centerline to center of mass, d
  summary: Distance 0 (default) | scalar
  group: ''
- name: Lateral distance from geometric centerline to hitch, hl
  summary: Distance 0 (default) | scalar
  group: ''
- name: Track width
  summary: Width [1.4,1.4] (default) | 1-by-2 vector
  group: ''
- name: Front tire(s) relaxation length, sigma_f
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
- name: Rear axle slip angle breakpoints, alpha_r_brk
  summary: Breakpoints [-.1 .1] (default) | vector
  group: ''
- name: Rear axle corner data, Cy_r_data
  summary: Data [-9e3 9e3] (default) | vector
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
  summary: Side force coefficient [0 0.01:0.01:0.3] (default) | vector
  group: ''
- name: Yaw moment coefficient vector, Cym
  summary: Yaw moment drag [0 1e-6:0.01:0.3] (default) | vector
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
- name: Wrap Euler angles, wrapAng
  summary: Selection off (default) | on
  group: ''
```

#### Options

### **Vehicle track** — Number of wheels `Single (bicycle)` | `Dual`

In the Vehicle Dynamics Blockset library, there are two types of Vehicle Body 3DOF blocks that model
longitudinal, lateral, and yaw motion.

| Block | Vehicle Track Setting | Implementation |
| --- | --- | --- |
| Vehicle Body 3DOF Single TrackVehicle Body 3DOF block single track | `Single (bicycle)` | - Forces act along the center line at the front and rear   axles. - No lateral load transfer. |
| Vehicle Body 3DOF Dual TrackVehicle Body 3DOF block | `Dual` | Forces act at the four vehicle corners or *hard points*. |

### **Axle forces** — Type of axle force `External longitudinal velocity` | `External longitudinal forces` | `External forces`

Use the **Axle forces** parameter to specify
the type of force.

| Axle Forces Setting | Implementation |
| --- | --- |
| `External longitudinal velocity` | - The block assumes that the external longitudinal velocity   is in a quasi-steady state, so the longitudinal acceleration   is approximately zero. - Because the motion is quasi-steady, the block calculates   lateral forces using the tire slip angles and linear   cornering stiffness. - Consider this setting when you want to:  - Generate virtual sensor signal data.   - Conduct high-level software studies that are     not impacted by driveline or nonlinear tire     responses. |
| `External longitudinal forces` | - The block uses the external longitudinal force to   accelerate or brake the vehicle. - The block calculates lateral forces using the tire slip   angles and linear cornering stiffness. - Consider this setting when you want to:  - Account for changes in the longitudinal     velocity on the lateral and yaw motion.   - Specify the external longitudinal motion     through a force instead of an external     longitudinal velocity.   - Connect the block to tractive actuators,     wheels, brakes, and hitches. |
| `External forces` | - The block uses the external lateral and longitudinal   forces to steer, accelerate, or brake the vehicle. - The block does not use the steering input to calculate   vehicle motion. - Consider this setting when you need tire models with more   accurate nonlinear combined lateral and longitudinal   slip. |

#### Input Signals

### **Front wheel steering** — `WhlAngF` input port `on` (default) | `off`

Specify to create input port `WhlAngF`.

### **External wind** — `WindXYZ` input port `off` (default) | `on`

Specify to create input port `WindXYZ`.

### **External forces** — `FExt` input port `off` (default) | `on`

Specify to create input port `FExt`.

### **External moments** — `MExt` input port `off` (default) | `on`

Specify to create input port `MExt`.

### **Rear wheel steering** — `WhlAngR` input port `off` (default) | `on`

Specify to create input port `WhlAngR`.

### **External friction** — `Mu` input port `off` (default) | `on`

Specify to create input port `Mu`.

### **Hitch forces** — `Fh` input port `off` (default) | `on`

Select to create input port `Fh`.

### **Hitch moments** — `Mh` input port `off` (default) | `on`

Specify to create input port `Mh`.

### **Initial longitudinal position** — `X_o` input port `off` (default) | `on`

Specify to create input port `X_o`.

### **Initial lateral position** — `Y_o` input port `off` (default) | `on`

Specify to create input port `Y_o`.

### **Initial longitudinal velocity** — `xdot_o` input port `off` (default) | `on`

Specify to create input port `xdot_o`.

### **Initial lateral velocity** — `ydot_o` input port `off` (default) | `on`

Specify to create input port `ydot_o`.

### **Initial yaw angle** — `psi_o` input port `off` (default) | `on`

Specify to create input port `psi_o`.

### **Initial yaw rate** — `r_o` input port `off` (default) | `on`

Specify to create input port `r_o`.

### **Air temperature** — `AirTemp` input port `off` (default) | `on`

Specify to create input port `AirTemp`.

#### Longitudinal

### **Number of wheels on front axle, NF** — Front wheel count `2` (default) | `scalar`

Number of wheels on front axle, *NF*. The
value is dimensionless.

### **Number of wheels on rear axle, NR** — Rear wheel count `2` (default) | `scalar`

Number of wheels on rear axle, *NR*. The
value is dimensionless.

### **Vehicle mass, m** — Vehicle mass `2000` (default) | `scalar`

Vehicle mass, *m*, in kg.

### **Longitudinal distance from center of mass to front axle, a** — Front axle distance `1.4` (default) | `scalar`

Horizontal distance *a* from the vehicle CG to the front wheel
axle, in m.

### **Longitudinal distance from center of mass to rear axle, b** — Rear axle distance `1.6` (default) | `scalar`

Horizontal distance *b* from the vehicle CG to the rear wheel
axle, in m.

### **Vertical distance from center of mass to axle plane, h** — Height `0.35` (default) | `scalar`

Height of vehicle CG above the axles, *h*, in m.

### **Longitudinal distance from center of mass to hitch, dh** — Distance from CM to hitch `1` (default) | `scalar`

Longitudinal distance from center of mass to hitch, *dh*, in
m.

#### Dependencies

To enable this parameter, on the **Input signals** pane,
select **Hitch forces** or **Hitch
moments**.

### **Vertical distance from hitch to axle plane, hh** — Distance from hitch to axle plane `0.2` (default) | `scalar`

Vertical distance from hitch to axle plane, *hh*, in m.

#### Dependencies

To enable this parameter, on the **Input signals** pane,
select **Hitch forces** or **Hitch
moments**.

### **Initial inertial frame longitudinal position, X\_o** — Position `0` (default) | `scalar`

Initial vehicle CG displacement along earth-fixed *X*-axis, in
m.

### **Initial longitudinal velocity, xdot\_o** — Velocity `0` (default) | `scalar`

Initial vehicle CG velocity along vehicle-fixed *x*-axis, in
m/s.

#### Dependencies

For the Vehicle Body 3DOF Single Track or Vehicle Body
3DOF Dual Track blocks, to enable this parameter, set **Axle
forces** to one of these options:

- `External longitudinal forces`
- `External forces`

#### Lateral

### **Front tire corner stiffness, Cy\_f** — Stiffness `12e3` (default) | `scalar`

Front tire corner stiffness, *Cyf*, in
N/rad.

#### Dependencies

For the Vehicle Body 3DOF Single Track or Vehicle Body 3DOF Dual
Track blocks, to enable this parameter:

1. Set **Axle forces** to one of these options:

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. Clear **Mapped corner stiffness**.

### **Rear tire corner stiffness, Cy\_r** — Stiffness `11e3` (default) | `scalar`

Rear tire corner stiffness, *Cyr*, in
N/rad.

#### Dependencies

For the Vehicle Body 3DOF Single Track or Vehicle Body 3DOF Dual
Track blocks, to enable this parameter:

1. Set **Axle forces** to one of these options:

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. Clear **Mapped corner stiffness**.

### **Initial inertial frame lateral displacement, Y\_o** — Position `0` (default) | `scalar`

Initial vehicle CG displacement along earth-fixed *Y*-axis, in
m.

### **Initial lateral velocity, ydot\_o** — Velocity `0` (default) | `scalar`

Initial vehicle CG velocity along vehicle-fixed *y*-axis, in
m/s.

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

### **Lateral distance from geometric centerline to center of mass, d** — Distance `0` (default) | `scalar`

Lateral distance from geometric centerline to center of mass,
*d*, in m, along the vehicle-fixed
*y*. Positive values indicate that the vehicle CM is
to the right of the geometric centerline. Negative values indicate that the
vehicle CM is to the left of the geometric centerline.

### **Lateral distance from geometric centerline to hitch, hl** — Distance `0` (default) | `scalar`

Lateral distance from geometric centerline to the hitch,
*hl*, in m, along the vehicle-fixed
*y*. Positive values indicate that the hitch is to
the right of the geometric centerline. Negative values indicate that the
hitch is to the left of the geometric centerline.

#### Dependencies

To enable this parameter, on the **Input signals**
pane, select **Hitch forces** or **Hitch
moments**.

### **Track width** — Width `[1.4,1.4]` (default) | `1`-by-`2` `vector`

Track width, *w*, in m.

#### Dependencies

To enable this parameter, set **Vehicle track** to
`Dual`.

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
*Af*, to calculate the
aerodynamic drag force on the vehicle, in
m2.

### **Longitudinal drag coefficient, Cd** — Air drag coefficient `.3` (default) | `scalar`

Air drag coefficient, *Cd*. The
value is dimensionless.

### **Longitudinal lift coefficient, Cl** — Air lift coefficient `.1` (default) | `scalar`

Air lift coefficient, *Cl*. The
value is dimensionless.

### **Longitudinal drag pitch moment, Cpm** — Pitch drag `.1` (default) | `scalar`

Longitudinal drag pitch moment coefficient,
*Cpm*. The value is
dimensionless.

### **Relative wind angle vector, beta\_w** — Wind angle `[0:0.01:0.3]` (default) | `vector`

Relative wind angle vector, *βw*,
in rad.

### **Side force coefficient vector, Cs** — Side force coefficient `[0 0.01:0.01:0.3]` (default) | `vector`

Side force coefficient vector coefficient,
*Cs*. The value is
dimensionless.

### **Yaw moment coefficient vector, Cym** — Yaw moment drag `[0 1e-6:0.01:0.3]` (default) | `vector`

Yaw moment coefficient vector,
*Cym*. The value is
dimensionless.

#### Environment

### **Absolute pressure, Pabs** — Pressure `101325` (default) | `scalar` | `scalar`

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

For the Vehicle Body 3DOF Single Track or Vehicle Body
3DOF Dual Track blocks, to enable this parameter:

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

For the Vehicle Body 3DOF Single Track or Vehicle Body
3DOF Dual Track blocks, to enable this parameter, set **Axle
forces** to one of these options:

- `External longitudinal velocity`
- `External longitudinal forces`

### **Geometric longitudinal offset from axle plane, longOff** — Longitudinal offset `0` (default) | `scalar`

Vehicle chassis offset from axle plane along body-fixed
*x*-axis, in m. When you use the 3D visualization engine,
consider using the offset to locate the chassis independent of the vehicle
CG.

### **Geometric lateral offset from center plane, latOff** — Lateral offset `0` (default) | `scalar`

Vehicle chassis offset from center plane along body-fixed
*y*-axis, in m. When you use the 3D visualization engine,
consider using the offset to locate the chassis independent of the vehicle
CG.

### **Geometric vertical offset from axle plane, vertOff** — Vertical offset `0` (default) | `scalar`

Vehicle chassis offset from axle plane along body-fixed
*z*-axis, in m. When you use the 3D visualization engine,
consider using the offset to locate the chassis independent of the vehicle
CG.

### **Wrap Euler angles, wrapAng** — Selection `off` (default) | `on`

Wrap the Euler angles to the interval `[-pi, pi]`. For vehicle
maneuvers that might undergo vehicle yaw rotations that are outside of the interval,
consider deselecting the parameter if you want to:

- Track the total vehicle yaw rotation.
- Avoid discontinuities in the vehicle state estimators.
## Libraries

Vehicle Dynamics Blockset / Vehicle Body

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

3DOF rigid vehicle body to calculate longitudinal, lateral, and yaw motion

The Vehicle Body 3DOF block implements a rigid two-axle vehicle body
model to calculate longitudinal, lateral, and yaw motion. The block accounts for body
mass and aerodynamic drag between the axles due to acceleration and steering.

Use this block in vehicle dynamics and automated driving studies to model nonholonomic
vehicle motion when vehicle pitch, roll, and vertical motion are not significant.

In the Vehicle Dynamics Blockset™ library, there are two types of Vehicle Body 3DOF blocks that model
longitudinal, lateral, and yaw motion.

| Block | Vehicle Track Setting | Implementation |
| --- | --- | --- |
| Vehicle Body 3DOF Single TrackVehicle Body 3DOF block single track | `Single (bicycle)` | - Forces act along the center line at the front and rear   axles. - No lateral load transfer. |
| Vehicle Body 3DOF Dual TrackVehicle Body 3DOF block | `Dual` | Forces act at the four vehicle corners or *hard points*. |

Use the **Axle forces** parameter to specify
the type of force.

| Axle Forces Setting | Implementation |
| --- | --- |
| `External longitudinal velocity` | - The block assumes that the external longitudinal velocity   is in a quasi-steady state, so the longitudinal acceleration   is approximately zero. - Because the motion is quasi-steady, the block calculates   lateral forces using the tire slip angles and linear   cornering stiffness. - Consider this setting when you want to:  - Generate virtual sensor signal data.   - Conduct high-level software studies that are     not impacted by driveline or nonlinear tire     responses. |
| `External longitudinal forces` | - The block uses the external longitudinal force to   accelerate or brake the vehicle. - The block calculates lateral forces using the tire slip   angles and linear cornering stiffness. - Consider this setting when you want to:  - Account for changes in the longitudinal     velocity on the lateral and yaw motion.   - Specify the external longitudinal motion     through a force instead of an external     longitudinal velocity.   - Connect the block to tractive actuators,     wheels, brakes, and hitches. |
| `External forces` | - The block uses the external lateral and longitudinal   forces to steer, accelerate, or brake the vehicle. - The block does not use the steering input to calculate   vehicle motion. - Consider this setting when you need tire models with more   accurate nonlinear combined lateral and longitudinal   slip. |

You can use these block parameters to create additional input ports. This table summarizes the settings.

| Input Signals Pane Parameter | Input Port | Description |
| --- | --- | --- |
| **Front wheel steering** | `WhlAngF` | Front wheel angle, *δF* |
| **External wind** | `WindXYZ` | Wind speed, *WX*, *WY*, *WZ*, in the inertial reference frame |
| **External forces** | `FExt` | External force on vehicle center of gravity (CG), *Fx*, *Fy*, *Fz*, in the vehicle-fixed frame |
| **Rear wheel steering** | `WhlAngR` | Rear wheel angle, *δR* |
| **External friction** | `Mu` | Friction coefficient |
| **External moments** | `MExt` | External moment about vehicle CG, *Mx*, *My*, *Mz*, in vehicle-fixed frame |
| **Hitch forces** | `Fh` | Hitch force applied to the body at the hitch location, *Fhx*, *Fhy*, and *Fhz*, in the vehicle-fixed frame |
| **Hitch moments** | `Mh` | Hitch moment at the hitch location, *Mhx*, *Mhy*, and *Mhz*, about the vehicle-fixed frame |
| **Initial longitudinal position** | `X_o` | Initial vehicle CG displacement along the earth-fixed *X*-axis, in m |
| **Initial lateral position** | `Y_o` | Initial vehicle CG displacement along the earth-fixed *Y*-axis, in m |
| **Initial longitudinal velocity** | `xdot_o` | Initial vehicle CG velocity along the vehicle-fixed *x*-axis, in m/s |
| **Initial lateral velocity** | `ydot_o` | Initial vehicle CG velocity along the vehicle-fixed *y*-axis, in m/s |
| **Initial yaw angle** | `psi_o` | Initial rotation of the vehicle-fixed frame about the earth-fixed *Z*-axis (yaw), in rad |
| **Initial yaw rate** | `r_o` | Initial vehicle angular velocity about the vehicle-fixed *z*-axis (yaw rate), in rad/s |
| **Air temperature** | `AirTemp` | Ambient air temperature. Considering this option if you want to vary the temperature during run-time. |

### Theory

The Vehicle Body 3DOF block implements a rigid two-axle vehicle
body model to calculate longitudinal, lateral, and yaw motion. The block accounts
for body mass, aerodynamic drag, and weight distribution between the axles due to
acceleration and steering. To determine the vehicle motion, the block implements
these equations for the single track, dual track, and drag calculations.

**Single Track**

| Calculation | Description |
| --- | --- |
| *Dynamics* | The block uses these equations to calculate the rigid body planar dynamics.  y¨=−x˙r+Fyf+Fyr+Fyextmr˙=aFyf−bFyr+MzextIzzr=ψ˙  If you set **Axle forces** to either `External longitudinal forces` or `External forces`, the block uses this equation for the longitudinal acceleration.  x¨=y˙r+Fxf+Fxr+Fxextm  If you set **Axle forces** to `External longitudinal velocity`, the block assumes a quasi-steady state for the longitudinal acceleration.  x¨=0 |
| *External forces* | External forces include both drag and external force inputs. The forces act on the vehicle CG.  Fx,y,z ext=Fd x,y,z+Fx,y,z inputMx,y,z ext=Md x,y,z+Mx,y,z input    If you set **Axle forces** to `External longitudinal forces`, the block uses these equations.  Fxft=FxfinputFyft=−CyfαfμfFzfFznomFxrt=FxrinputFyrt=−CyrαrμrFzrFznom    If you set **Axle forces** to `External longitudinal velocity`, the block uses these equations.  Fxft=0Fyft=−CyfαfμfFzfFznomFxrt=0Fyrt=−CyrαrμrFzrFznom    The block divides the normal forces by the nominal normal load to vary the effective friction parameters during weight and load transfer. The block uses these equations to maintain pitch and roll equilibrium.  Fzf=bmg−(x¨−y˙r)mh+hFxext+bFzext−Myexta+bFzr=amg+(x¨−y˙r)mh−hFxext+aFzext+Myexta+b |
| *Tire forces* | The block uses the ratio of the local and longitudinal and lateral velocities to determine the slip angles.  αf=atan(y˙+arx˙)−δfαr=atan(y˙−brx˙)−δr    To determine the tire forces, the block uses the slip angles.  Fxf=Fxftcos(δf)−Fyftsin(δf)Fyf=−Fxftsin(δf)+Fyftcos(δf)Fxr=Fxrtcos(δr)−Fyrtsin(δr)Fyr=−Fxrtsin(δr)+Fyrtcos(δr)    If you set **Axle forces** to `External forces`, the block sets the tire forces equal to the external input force.  Fxf=Fxft=FxfinputFyf=Fyft=FyfinputFxr=Fxrt=FxrinputFyr=Fyrt=Fyrinput |

**Dual Track**

Isometric view of vertical, longitudinal, and lateral forces acting at suspension locations

| Calculation | Description |
| --- | --- |
| *Dynamics* | The block uses these equations to calculate the rigid body planar dynamics.  x¨=y˙r+Fxfl+Fxfr+Fxrl+Fxrr+Fxextmy¨=−x˙r+Fyfl+Fyfr+Fyrl+Fyrr+Fyextmr˙=a(Fyfl+Fyfr)−b(Fyrl+Fyrr)+wf(Fxfl−Fxfr)2+wr(Fxrl−Fxrr)2+MzextIzzr=ψ˙  If you set **Axle forces** to `External longitudinal velocity`, the block assumes a quasi-steady state for the longitudinal acceleration.  x¨=0 |
| *External forces* | External forces include both drag and external force inputs. The forces act on the vehicle CG.  Fx,y,z ext=Fd x,y,z+Fx,y,z inputMx,y,z ext=Md x,y,z+Mx,y,z input    If you set **Axle forces** to `External longitudinal forces`, the block uses these equations.  Fxflt=FxflinputFyflt=−CyflαflμflFzfl2FznomFxfrt=FxlrinputFyfrt=−CyfrαfrμfrFzfr2FznomFxrlt=FxrlinputFyrlt=−CyrlαrlμrlFzrl2FznomFxrrt=FxrrinputFyrrt=−CyrrαrrμrrFzrr2Fznom    If you set **Axle forces** to `External longitudinal velocity`, the block uses these equations.  Fxflt=0Fyflt=−CyflαflμflFzfl2FznomFxfrt=0Fyfrt=−CyfrαfrμfrFzfr2FznomFxrlt=0Fyrlt=−CyrlαrlμrlFzrl2FznomFxrrt=0Fyrrt=−CyrrαrrμrrFzrr2Fznom    The block divides the normal forces by the nominal normal load to vary the effective friction parameters during weight and load transfer. The block uses these equations to maintain pitch and roll equilibrium.  Fzf=bmg−(x¨−y˙r)mh+hFxext+bFzext−Myexta+bFzr=amg+(x¨−y˙r)mh−hFxext+aFzext+Myext(a+b)Fzfl=Fzf+(mh(y¨+x˙r)−hFyext−Mxext)2wfFzfr=Fzf+(−mh(y¨+x˙r)+hFyext+Mxext)2wfFzrl=Fzr+(mh(y¨+x˙r)−hFyext−Mxext)2wrFzrr=Fzr+(−mh(y¨+x˙r)+hFyext+Mxext)2wr |
| *Tire forces* | The block uses the ratio of the local and longitudinal and lateral velocities to determine the slip angles.  αfl=atan(y˙+arx˙+rwf2)−δflαfr=atan(y˙+arx˙−rwf2)−δfrαrl=atan(y˙−arx˙+rwr2)−δrlαrr=atan(y˙−arx˙−rwr2)−δrr    The block uses the steering angles to transform the tire forces to the vehicle-fixed frame.  Fxfl=Fxfltcos(δfl)−Fyfltsin(δfl)Fxfr=Fxfrtcos(δfr)−Fyfrtsin(δfr)Fyfl=−Fxfltsin(δfl)+Fyfltcos(δfl)Fyfr=−Fxfrtsin(δfr)+Fyfrtcos(δfr)Fxrl=Fxrltcos(δrl)−Fyrltsin(δrl)Fxrr=Fxrrtcos(δrr)−Fyrrtsin(δrr)Fyrl=−Fxrltsin(δrl)+Fyrltcos(δrl)Fyrr=−Fxrrtsin(δrr)+Fyrrtcos(δrr)    If you set **Axle forces** to `External forces`, the block uses these equations. The blocks assumes that the externally provided forces are in the vehicle-fixed frame at the axle-wheel location.  Fxfl=Fxflt=FxflinputFxfr=Fxfrt=FxfrinputFyfl=Fyflt=FyflinputFyfr=Fyfrt=FyfrinputFxrl=Fxrlt=FxrlinputFyrr=Fyrrt=Fyrrinput |

**Drag**

| Calculation | Description |
| --- | --- |
| *Coordinate transformation* | The block transforms the wind speeds from the inertial frame to the vehicle-fixed frame.  wx=Wxcos(ψ)+Wysin(ψ)wy=Wycos(ψ)−Wxsin(ψ)wz=Wz |
| *Drag forces* | To determine a relative airspeed, the block subtracts the wind speed from the CG vehicle velocity. Using the relative airspeed, the block determines the drag forces.  w¯=(x˙−wx)2+(y˙−wy)2+(wz)2Fdx=−12TRCdAfPabs(w¯)2Fdy=−12TRCsAfPabs(w¯)2Fdz=−12TRClAfPabs(w¯)2 |
| *Drag moments* | Using the relative airspeed, the block determines the drag moments.  Mdr=−12TRCrmAfPabs(w¯)2(a+b)Mdp=−12TRCpmAfPabs(w¯)2(a+b)Mdy=−12TRCymAfPabs(w¯)2(a+b) |

**Lateral Corner Stiffness and Relaxation Dynamics**

| Description | Implementation |
| --- | --- |
| *Constant values.* | The block uses constant stiffness values for *Cyf* and *Cyr*. |
| *Lookup tables as a function of corner stiffness data and slip angles.* | The block uses lookup tables that are functions of the corner stiffness data and slip angles.  Cyf=f(αf,Cyfdata)Cyr=f(αr,Cyrdata) |
| *Lookup tables as a function of corner stiffness data and slip angles.*  *Slip angles include the relaxation length dynamic settings.* | The block uses lookup tables that are functions of the corner stiffness data and slip angles. The slip angles include the relaxation length dynamic settings. The relaxation length approximates an effective corner stiffness force that is a function of wheel travel.  Cyf=f(αfσ,Cyfdata)Cyr=f(αrσ,Cyrdata)αfσ=1s[(αf−αfσ)vwfαf]αrσ=1s[(αr−αrσ)vwrαr] |

The equations use these variables.

|  |  |
| --- | --- |
| x,x˙,x¨ | Vehicle CG displacement, velocity, and acceleration, along the vehicle-fixed *x*-axis |
| y,y˙,y¨ | Vehicle CG displacement, velocity, and acceleration, along the vehicle-fixed *y*-axis |
| *ψ* | Rotation of the vehicle-fixed frame about the earth-fixed *Z*-axis (yaw) |
| *r*,Ψ˙ | Vehicle angular velocity, about the vehicle-fixed *z*-axis (yaw rate) |
| *Fxf*, *Fxr* | Longitudinal forces applied to front and rear wheels, along the vehicle-fixed *x*-axis |
| *Fyf*, *Fyr* | Lateral forces applied to front and rear wheels, along vehicle-fixed *y*-axis |
| *Fxext*, *Fyext*, *Fzext* | External forces applied to vehicle CG, along the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *Fdx*, *Fdy*, *Fdz* | Drag forces applied to vehicle CG, along the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *Fxinput*, *Fyinput*, *Fzinput* | Input forces applied to vehicle CG, along the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *Mxext*, *Myext*, *Mzext* | External moment about vehicle CG, about the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *Mdx*, *Mdy*, *Mdz* | Drag moment about vehicle CG, about the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *Mxinput*, *Myinput*, *Mzinput* | Input moment about vehicle CG, about the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *Izz* | Vehicle body moment of inertia about the vehicle-fixed *z*-axis |
| *Fxft*, *Fxrt* | Longitudinal tire force applied to front and rear wheels, along the vehicle-fixed *x*-axis |
| *Fyft*, *Fyft* | Lateral tire force applied to front and rear wheels, along vehicle-fixed *y*-axis |
| *Fxfl*, *Fxfr* | Longitudinal force applied to front left and front right wheels, along the vehicle-fixed *x*-axis |
| *Fyfl*, *Fyfr* | Lateral force applied to front left and front right wheels, along the vehicle-fixed *y*-axis |
| *Fxrl*, *Fxrr* | Longitudinal force applied to rear left and rear right wheels, along the vehicle-fixed *x*-axis |
| *Fyrl*, *Fyrr* | Lateral force applied to rear left and rear right wheels, along the vehicle-fixed *y*-axis |
| *Fxflt*, *Fxfrt* | Longitudinal tire force applied to front left and front right wheels, along the vehicle-fixed *x*-axis |
| *Fyflt*, *Fyfrt* | Lateral force tire applied to front left and front right wheels, along the vehicle-fixed *y*-axis |
| *Fxrlt*, *Fxrrt* | Longitudinal tire force applied to rear left and rear right wheels, along the vehicle-fixed *x*-axis |
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
