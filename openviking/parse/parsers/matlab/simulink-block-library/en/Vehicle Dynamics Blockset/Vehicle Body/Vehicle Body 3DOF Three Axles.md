---
type: simulink-block
title: 'Vehicle Body 3DOF Three Axles'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Body'
documentation_page: 'vehiclebody3dofthreeaxles'
documentation_source_path: 'ref/vehiclebody3dofthreeaxles.html'
language: en
---

# Vehicle Body 3DOF Three Axles

## Ports

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

### **WhlAngM** — Middle wheel steering angles `scalar` | `array`

Middle wheel steering angles,
*δM*, in rad.

| **Vehicle Track** Setting | Variable | Signal Dimension |
| --- | --- | --- |
| `Single (bicycle)` | *δM* | Scalar – `1` |
| `Dual` | δM=[δmlδmr]  or  [δmlδmr] | Array – `[1x2]` or `[2x1]` |

#### Dependencies

To enable this port, on the **Input signals**
pane, select **Middle wheel steering**.

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

Vehicle CG velocity along the vehicle-fixed
*x*-axis, in m/s.

#### Dependencies

To enable this port, set **Axle forces** to
`External longitudinal
velocity`.

### **FwF** — Total force on the front wheels `scalar` | `array`

Force on the front wheels,
*FwF*, along the
vehicle-fixed axis, in N.

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

### **FwM** — Total force on the middle wheels `scalar` | `array`

Force on the middle wheels,
*FwM*, along the
vehicle-fixed axis, in N.

| **Vehicle Track** Setting | **Axle Forces** Setting | Description | Variable | Signal Dimension |
| --- | --- | --- | --- | --- |
| `Single (bicycle)` | `External longitudinal forces` | Longitudinal force on the middle wheel | FwM=Fxr | Scalar – `1` |
| `External forces` | Longitudinal and lateral forces on the middle wheel | FwM=[FxmFym]  or [FxmFym] | Array – `[1x2]` or `[2x1]` |
| `Dual` | `External longitudinal forces` | Longitudinal force on the middle wheels | FwM=[FxmlFxmr] or [FxmlFxmr] | Array – `[1x2]` or `[2x1]` |
| `External forces` | Longitudinal and lateral forces on the middle wheels | FwM=[FxmlFxmrFymlFymr] | Array – `[2x2]` |

#### Dependencies

To enable this port, set **Axle forces** to one of these options:

- `External longitudinal forces`
- `External forces`

### **FwR** — Total force on the rear wheels `scalar` | `array`

Force on the rear wheels,
*FwR*, along the
vehicle-fixed axis, in N.

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

External forces applied to the vehicle CG,
*Fxext*,
*Fyext*,
*Fzext*, in
vehicle-fixed frame, in N. The signal array dimensions are
`[1x3]` or `[3x1]`.

#### Dependencies

To enable this port, on the **Input signals**
pane, select **External forces**.

### **MExt** — External moment about vehicle CG `array`

External moment about the vehicle CG,
*Mx*,
*My*,
*Mz*, in the vehicle-fixed
frame, in N·m. The signal array dimensions are `[1x3]`
or `[3x1]`.

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
*Wz* along the inertial
*X*-, *Y*-, and
*Z*-axes, in m/s. The signal array dimensions are
`[1x3]` or `[3x1]`.

#### Dependencies

To enable this port, on the **Input signals**
pane, select **External wind**.

### **Mu** — Tire friction coefficient `array`

Tire friction coefficient, *μ*, dimensionless.

| **Vehicle Track** Setting | Variable | Signal Dimension |
| --- | --- | --- |
| `Single (bicycle)` | Mu=[μfμmμr] or [μfμmμr] | Array – `[1x3]` or `[3x1]` |
| `Dual` | Mu=[μflμfrμmlμmrμrlμrr] | Array – `[3x2]` |

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

Vehicle angular velocity about the vehicle-fixed
*z*-axis (yaw rate), in rad/s.

#### Dependencies

To enable this port, on the **Input signals**
pane, select **Initial yaw rate**.
### Output

### **Info** — Vehicle data bus

Vehicle data, returned as a bus signal containing these block
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
| `Hitch` | `Disp` | `X` | | | Trailer hitch offset from the axle plane along the earth-fixed *X*-axis | Computed | m |
| `Y` | | | Trailer hitch offset from the center plane along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | | Trailer hitch offset from the axle plane along the earth-fixed *Z*-axis | Computed | m |
| `Vel` | `Xdot` | | | Trailer hitch offset velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | | Trailer hitch offset velocity along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | | Trailer hitch offset velocity along the earth-fixed *Z*-axis | Computed | m/s |
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
| `Forces` | `Body` | `Fx` | | | Net force on vehicle CG along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | | Net force on vehicle CG along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | | Net force on vehicle CG along the vehicle-fixed *z*-axis | `0` | N |
| `Ext` | `Fx` | | | External force on vehicle CG along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | | External force on vehicle CG along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | | External force on vehicle CG along the vehicle-fixed *z*-axis | `0` | N |
| `Hitch` | `Fx` | | | Hitch force applied to body at the hitch location along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | | Hitch force applied to body at the hitch location along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | | Hitch force applied to body at the hitch location along the vehicle-fixed *z*-axis | Computed | N |
| `FrntAxl` | `Lft` | `Fx` | | Longitudinal force on left front wheel along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on left front wheel along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Normal force on left front wheel along the vehicle-fixed *z*-axis | Computed | N |
| `Rght` | `Fx` | | Longitudinal force on right front wheel along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on right front wheel along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Normal force on right front wheel along the vehicle-fixed *z*-axis | Computed | N |
| `MidlAxl` | `Lft` | `Fx` | | Longitudinal force on left middle wheel along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on left middle wheel along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Normal force on left middle wheel along the vehicle-fixed *z*-axis | Computed | N |
| `Rght` | `Fx` | | Longitudinal force on right middle wheel along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on right middle wheel along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Normal force on right middle wheel along the vehicle-fixed *z*-axis | Computed | N |
| `RearAxl` | `Lft` | `Fx` | | Longitudinal force on left rear wheel along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on left rear wheel along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Normal force on left rear wheel along the vehicle-fixed *z*-axis | Computed | N |
| `Rght` | `Fx` | | Longitudinal force on right rear wheel along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on right rear wheel along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Normal force on right rear wheel along the vehicle-fixed *z*-axis | Computed | N |
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
| `Hitch` | `Disp` | | `x` | | Hitch offset from axle plane along the vehicle-fixed *x*-axis | Input | m |
| `y` | | Hitch offset from center plane along the vehicle-fixed *y*-axis | Input | m |
| `z` | | Hitch offset from axle plane along the earth-fixed *z*-axis | Input | m |
| `Vel` | | `xdot` | | Hitch offset velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Hitch offset velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | Hitch offset velocity along the vehicle-fixed *z*-axis | `0` | m/s |
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

### **xdot** — Vehicle longitudinal velocity `scalar`

Vehicle CG velocity along the vehicle-fixed
*x*-axis, in m/s.

### **ydot** — Vehicle lateral velocity `scalar`

Vehicle CG velocity along the vehicle-fixed
*y*-axis, in m/s.

### **psi** — Yaw `scalar`

Rotation of the vehicle-fixed frame about the earth-fixed
*Z*-axis (yaw), in rad.

### **r** — Yaw rate `scalar`

Vehicle angular velocity, `r`, about the
vehicle-fixed *z*-axis (yaw rate), in rad/s.

### **FzF** — Normal force on front wheels `scalar` | `array`

Normal force on the front wheels,
*FzF*, along the
vehicle-fixed *z*-axis, in N.

| **Vehicle Track** Setting | Description | Variable | Signal Dimension |
| --- | --- | --- | --- |
| `Single (bicycle)` | Normal force on front axle | FzF=Fzf | Scalar – `1` |
| `Dual` | Normal force on the right and left front wheels | FzF=[FzflFzfr] | Array – `[1x2]` |

### **FzM** — Normal force on middle wheels `scalar` | `array`

Normal force on the middle wheels,
*FzM*, along the
vehicle-fixed *z*-axis, in N.

| **Vehicle Track** Setting | Description | Variable | Signal Dimension |
| --- | --- | --- | --- |
| `Single (bicycle)` | Normal force on middle axle | FzM=Fzm | Scalar – `1` |
| `Dual` | Normal force on the right and left middle wheels | FzM=[FzmlFzrl] | Array – `[1x2]` |

### **FzR** — Normal force on rear wheels `scalar` | `array`

Normal force on the rear wheels,
*FzR*, along the
vehicle-fixed *z*-axis, in N.

| **Vehicle Track** Setting | Description | Variable | Signal Dimension |
| --- | --- | --- | --- |
| `Single (bicycle)` | Normal force on rear wheel | FzR=Fzr | Scalar – `1` |
| `Dual` | Normal force on the right and left rear wheels | FzR=[FzrlFzrr] | Array – `[1x2]` |

## Parameters

#### Options

### **Vehicle track** — Number of vehicle wheels `Dual` (default) | `Single (bicycle)`

Use the **Vehicle track** parameter to specify the number of wheels.

| Vehicle Track Setting | Implementation |
| --- | --- |
| `Single (bicycle)` | - Forces act along the center line of the axles. - No lateral load transfer. |
| `Dual` | Forces act at the axle hard-point locations. |

### **Axle forces** — Type of axle force `External longitudinal velocity` (default) | `External longitudinal forces` | `External forces`

Use the **Axle forces** parameter to specify
the type of force.

| Axle Forces Setting | Implementation |
| --- | --- |
| `External longitudinal velocity` | - The block assumes that the external longitudinal velocity   is in a quasi-steady state, so the longitudinal acceleration   is approximately zero. - Because the motion is quasi-steady, the block calculates   lateral forces using the tire slip angles and linear   cornering stiffness. - Consider this setting when you want to:  - Generate virtual sensor signal data.   - Conduct high-level software studies that are     not impacted by driveline or nonlinear tire     responses. |
| `External longitudinal forces` | - The block uses the external longitudinal force to   accelerate or brake the vehicle. - The block calculates lateral forces using the tire slip   angles and linear cornering stiffness. - Consider this setting when you want to:  - Account for changes in the longitudinal     velocity on the lateral and yaw motion.   - Specify the external longitudinal motion     through a force instead of an external     longitudinal velocity.   - Connect the block to tractive actuators,     wheels, brakes, and hitches. |
| `External forces` | - The block uses the external lateral and longitudinal   forces to steer, accelerate, or brake the vehicle. - The block does not use the steering input to calculate   vehicle motion. - Consider this setting when you need tire models with more   accurate nonlinear combined lateral and longitudinal   slip. |

#### Input Signals

### **Front wheel steering** — `WhlAngF` input port `on` (default) | `off`

Select to create input port `WhlAngF`.

### **Middle wheel steering** — `WhlAngM` input port `off` (default) | `on`

Select to create input port `WhlAngM`.

### **Rear wheel steering** — `WhlAngR` input port `off` (default) | `on`

Select to create input port `WhlAngR`.

### **External wind** — `WindXYZ` input port `off` (default) | `on`

Select to create input port `WindXYZ`.

### **External friction** — `Mu` input port `off` (default) | `on`

Select to create input port `Mu`.

#### Dependencies

To enable this parameter, set **Axle forces** to
`External longitudinal forces` or
`External forces`.

### **External forces** — `FExt` input port `off` (default) | `on`

Select to create input port `FExt`.

### **External moments** — `MExt` input port `off` (default) | `on`

Select to create input port `MExt`.

### **Hitch forces** — `Fh` input port `on` (default) | `off`

Select to create input port `Fh`.

### **Hitch moments** — `Mh` input port `on` (default) | `off`

Specify to create input port `Mh`.

### **Initial longitudinal position** — `X_o` input port `off` (default) | `on`

Specify to create input port `X_o`.

### **Initial yaw angle** — `psi_o` input port `off` (default) | `on`

Specify to create input port `psi_o`.

### **Initial longitudinal velocity** — `xdot_o` input port `off` (default) | `on`

Specify to create input port `xdot_o`.

#### Dependencies

To enable this parameter, set **Axle forces** to
`External longitudinal forces` or
`External forces`.

### **Initial yaw rate** — `r_o` input port `off` (default) | `on`

Specify to create input port `r_o`.

### **Initial lateral position** — `Y_o` input port `off` (default) | `on`

Specify to create input port `Y_o`.

### **Air temperature** — `AirTemp` input port `off` (default) | `on`

Specify to create input port `AirTemp`.

### **Initial lateral velocity** — `ydot_o` input port `off` (default) | `on`

Specify to create input port `ydot_o`.

#### Longitudinal

### **Number of wheels on front axle, NF** — Front wheel count `2` (default) | `scalar`

Number of wheels on the front axle,
*NF*, dimensionless.

### **Number of wheels on middle axle, NM** — Middle wheel count `2` (default) | `scalar`

Number of wheels on the middle axle,
*NM*, dimensionless.

### **Number of wheels on rear axle, NR** — Rear wheel count `2` (default) | `scalar`

Number of wheels on the rear axle,
*NR*, dimensionless.

### **Vehicle mass, m** — Vehicle mass `47000` (default) | `scalar`

Vehicle mass, *m*, in kg.

### **Longitudinal distance from center of mass to front axle, a** — Distance from CM to front axle `0.5` (default) | `scalar`

Distance from vehicle CM to front axle, *a*, in m.

Side view of tractor showing distances of hitch and axles from CM

### **Longitudinal distance from center of mass to middle axle, b** — Distance from CM to middle axle `4.5` (default) | `scalar`

Distance from vehicle CM to middle axle, *b*, in m.

Side view of tractor showing distances of hitch and axles from CM

### **Longitudinal distance from center of mass to rear axle, c** — Distance from CM to rear axle `5.7` (default) | `scalar`

Distance from vehicle CM to rear axle, *c*, in m.

Side view of tractor showing distances of hitch and axles from CM

### **Vertical distance from center of mass to axle plane, h** — Distance from CM to axle plane `0.3` (default) | `scalar`

Vertical distance from vehicle CM to axle plane, *h*, in m.

Side view of tractor showing distances of hitch and axles from CM

### **Vertical distance from hitch to axle plane, hh** — Distance from hitch to axle plane `0.5` (default) | `scalar`

Vertical distance from hitch to axle plane, *hh*, in m.

Side view of tractor showing distances of hitch and axles from CM

#### Dependencies

To enable this parameter, on the **Input signals**
pane, select **Hitch forces** or **Hitch
moments**.

### **Longitudinal distance from center of mass to hitch, dh** — Distance from CM to hitch `5` (default) | `scalar`

Longitudinal distance from center of mass to hitch, *dh*,
in m.

Side view of tractor showing distances of hitch and axles from CM

#### Dependencies

To enable this parameter, on the **Input signals**
pane, select **Hitch forces** or **Hitch
moments**.

### **Initial inertial frame longitudinal position, X\_o** — Initial longitudinal displacement `0` (default) | `scalar`

Initial vehicle CG displacement along the earth-fixed
*X*-axis, in m.

### **Initial longitudinal velocity, xdot\_o** — Initial longitudinal velocity `0` (default) | `scalar`

Initial vehicle CG velocity along the vehicle-fixed
*x*-axis, in m/s.

#### Dependencies

To enable this parameter, set **Axle forces** to one
of these options:

- `External longitudinal
  forces`
- `External forces`

#### Lateral

### **Mapped corner stiffness** — Enable mapped corner stiffness `off` (default) | `on`

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
*y*-axis. Positive values indicate that the vehicle
CM is to the right of the geometric centerline. Negative values indicate
that the vehicle CM is to the left of the geometric centerline.

Top down view of track widths and CM offset from centerline

### **Track width, w** — Front, middle, and rear track widths `[1.82,1.82,1.82]` (default) | `vector`

Front, middle, and rear track widths, *wf*,
*wm*, and, *wr*, respectively, in m.
Dimensions are `1-by-3`.

Top down view of track widths and CM offset from centerline

#### Dependencies

To enable this parameter, set **Vehicle track** to
`Dual`.

### **Front axle tire corner stiffness, Cy\_f** — Front tire corner stiffness `12e3` | `scalar`

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

### **Middle axle tire corner stiffness, Cy\_m** — Middle tire corner stiffness `11e3` | `scalar`

Middle axle tire corner stiffness,
*Cym*, in N/rad.

#### Dependencies

To enable this parameter:

1. Set **Axle forces** to one of these options:

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
2. Clear **Mapped corner stiffness**.

### **Rear axle tire corner stiffness, Cy\_r** — Rear tire corner stiffness `11e3` | `scalar`

Rear axle tire corner stiffness,
*Cyr*, in N/rad.

#### Dependencies

To enable this parameter:

1. Set **Axle forces** to one of these options:

   - `External longitudinal
     velocity`
   - `External longitudinal
     forces`
2. Clear **Mapped corner stiffness**.

### **Front tire(s) relaxation length, sigma\_f** — Front tire relaxation length `.1` (default) | `scalar`

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

### **Middle tire(s) relaxation length, sigma\_m** — Middle tire relaxation length `.1` (default) | `scalar`

Middle tire relaxation length,
*σm*, in m.

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

### **Rear tire(s) relaxation length, sigma\_r** — Rear tire relaxation length `.1` (default) | `scalar`

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

### **Front axle tire corner data, Cy\_f\_data** — Front axle tire corner data `[-9e3 9e3]` (default) | `vector`

Front axle tire corner data,
*Cyfdata*, in N/rad.

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

### **Middle axle tire corner data, Cy\_m\_data** — Middle axle tire corner data `[-9e3 9e3]` (default) | `vector`

Middle axle tire corner data,
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

### **Rear axle tire corner data, Cy\_r\_data** — Rear axle tire corner data `[-9e3 9e3]` (default) | `vector`

Rear axle tire corner data,
*Cyrdata*, in N/rad.

#### Dependencies

To enable this parameter:

1. Set **Axle forces** to one of these options:

   - `External longitudinal velocity`
   - `External longitudinal forces`
2. Select **Mapped corner stiffness**.

### **Initial inertial frame lateral displacement, Y\_o** — Initial lateral displacement `0` (default) | `scalar`

Initial vehicle CG displacement along the earth-fixed
*Y*-axis, in m.

### **Initial lateral velocity, ydot\_o** — Initial lateral velocity `0` (default) | `scalar`

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

Three-axle vehicle body with longitudinal, lateral, and yaw motion

The Vehicle Body 3DOF Three Axles block implements a rigid, three-axle
vehicle body model to calculate longitudinal, lateral, and yaw motion. The block
accounts for the axle and hitch reaction forces due to the vehicle body mass
acceleration, aerodynamic drag, and steering.

Use this block in vehicle dynamics and automated driving studies to model nonholonomic
vehicle motion when vehicle pitch, roll, and vertical motion are not significant.

Use the **Vehicle track** parameter to specify the number of wheels.

| Vehicle Track Setting | Implementation |
| --- | --- |
| `Single (bicycle)` | - Forces act along the center line of the axles. - No lateral load transfer. |
| `Dual` | Forces act at the axle hard-point locations. |

Use the **Axle forces** parameter to specify
the type of force.

| Axle Forces Setting | Implementation |
| --- | --- |
| `External longitudinal velocity` | - The block assumes that the external longitudinal velocity   is in a quasi-steady state, so the longitudinal acceleration   is approximately zero. - Because the motion is quasi-steady, the block calculates   lateral forces using the tire slip angles and linear   cornering stiffness. - Consider this setting when you want to:  - Generate virtual sensor signal data.   - Conduct high-level software studies that are     not impacted by driveline or nonlinear tire     responses. |
| `External longitudinal forces` | - The block uses the external longitudinal force to   accelerate or brake the vehicle. - The block calculates lateral forces using the tire slip   angles and linear cornering stiffness. - Consider this setting when you want to:  - Account for changes in the longitudinal     velocity on the lateral and yaw motion.   - Specify the external longitudinal motion     through a force instead of an external     longitudinal velocity.   - Connect the block to tractive actuators,     wheels, brakes, and hitches. |
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

| Calculation | Description |
| --- | --- |
| *Dynamics* | The block solves the rigid-body planar dynamics equations to determine the vehicle longitudinal motion. If you set **Axle forces** to `External longitudinal velocity`, the block assumes a quasi-steady state for the longitudinal acceleration. |
| *External forces* | External forces include both drag and external force inputs. The forces act on the vehicle CG.  The block divides the normal forces by the nominal normal load to vary the effective friction parameters during weight and load transfer. The block maintains pitch and roll equilibrium. |
| *Tire forces* | The block uses the ratio of the local, longitudinal, and lateral velocities to determine the slip angles.  The block uses the steering angles to transform the tire forces to the vehicle-fixed frame.  If you set **Axle forces** to `External forces`, the block assumes that the externally provided forces are in the vehicle-fixed frame at the axle-wheel location. |

**Single Track**

Isometric view of vertical, longitudinal, and lateral forces acting at single track suspension locations

**Dual Track**

Isometric view of vertical, longitudinal, and lateral forces acting at dual track suspension locations

The illustrations use these variables.

|  |  |
| --- | --- |
| *a*, *b*, *c* | Longitudinal distance of the front, middle, and rear axles, respectively, from the normal projection point of the vehicle CG onto the common axle plane |
| *h* | Height of vehicle CG above the axle plane along the vehicle-fixed *z*-axis |
| *d* | Lateral distance from geometric centerline to center of mass along the vehicle-fixed *y*-axis |
| *hh* | Height of the hitch above the axle plane along the vehicle-fixed *z*-axis |
| *dh* | Longitudinal distance of the hitch from normal projection point of the vehicle CG onto the common axle plane |
| *hl* | Lateral distance from center of mass to hitch along the vehicle-fixed *y*-axis. |
| *wf*, *wm*, *wr* | Front, middle, and rear track width, respectively |

**Drag**

This table summarizes the block implementation for the drag
calculation.

| Calculation | Description |
| --- | --- |
| *Coordinate transformation* | The block transforms the wind speeds from the inertial frame to the vehicle-fixed frame. |
| *Drag forces* | To determine a relative airspeed, the block subtracts the wind speed from the CG vehicle velocity. Using the relative airspeed, the block determines the drag forces. |
| *Drag moments* | Using the relative airspeed, the block determines the drag moments. |

**Lateral Corner Stiffness and Relaxation Dynamics**

To enable the mapped corner stiffness and relaxation length dynamic
parameters, set **Axle forces** to `External
longitudinal force` or `External longitudinal
velocity`.

| Parameter Settings | | Description |
| --- | --- | --- |
| Mapped Corner Stiffness | Include Relaxation Length Dynamics |
| `Off` (default) | `On` (default) | The block uses constant corner stiffness values.  The slip angles include the relaxation length dynamic settings. The relaxation length approximates an effective corner stiffness force that is a function of wheel travel. |
| `On` | `On` (default) | The block uses lookup tables that are functions of the corner stiffness data and slip angles.  The slip angles include the relaxation length dynamic settings. The relaxation length approximates an effective corner stiffness force that is a function of wheel travel. |
| `Off` (default) | `Off` | The block uses constant corner stiffness values. |
