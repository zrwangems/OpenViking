---
type: simulink-block
title: 'Vehicle Body 6DOF'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Body'
documentation_page: 'vehiclebody6dof'
documentation_source_path: 'ref/vehiclebody6dof.html'
language: en
---

# Vehicle Body 6DOF

## Ports

### Input

### **FSusp** — Suspension forces on vehicle `array`

Suspension longitudinal, lateral, and vertical suspension forces applied to the
vehicle at the hardpoint location, in N. Signal dimensions are
`[3x4]`.

FSusp=[FFLxFFRxFRLxFRRxFFLyFFRyFRLyFRRyFFLzFFRzFRLzFRRz]

| Array Element | Axle | Wheel | Force Axis |
| --- | --- | --- | --- |
| `FSusp(1,1)` | Front | Left | Vehicle-fixed *x*-axis (longitudinal) |
| `FSusp(1,2)` | Front | Right |
| `FSusp(1,3)` | Rear | Left |
| `FSusp(1,4)` | Rear | Right |
| `FSusp(2,1)` | Front | Left | Vehicle-fixed *y*-axis (lateral) |
| `FSusp(2,2)` | Front | Right |
| `FSusp(2,3)` | Rear | Left |
| `FSusp(2,4)` | Rear | Right |
| `FSusp(3,1)` | Front | Left | Vehicle-fixed *z*-axis (vertical) |
| `FSusp(3,2)` | Front | Right |
| `FSusp(3,3)` | Rear | Left |
| `FSusp(3,4)` | Rear | Right |

### **MSusp** — Suspension moment on vehicle `array`

Suspension longitudinal, lateral, and vertical suspension moments applied about the
vehicle at the hardpoint location, in N·m. Signal dimensions are
`[3x4]`.

MSusp=[MFLxMFRxMRLxMRRxMFLyMFRyMRLyMRRyMFLzMFRzMRLzMRRz]

| Array Element | Axle | Wheel | Moment Axis |
| --- | --- | --- | --- |
| `MSusp(1,1)` | Front | Left | Vehicle-fixed *x*-axis (longitudinal) |
| `MSusp(1,2)` | Front | Right |
| `MSusp(1,3)` | Rear | Left |
| `MSusp(1,4)` | Rear | Right |
| `MSusp(2,1)` | Front | Left | Vehicle-fixed *y*-axis (lateral) |
| `MSusp(2,2)` | Front | Right |
| `MSusp(2,3)` | Rear | Left |
| `MSusp(2,4)` | Rear | Right |
| `MSusp(3,1)` | Front | Left | Vehicle-fixed *z*-axis (vertical) |
| `MSusp(3,2)` | Front | Right |
| `MSusp(3,3)` | Rear | Left |
| `MSusp(3,4)` | Rear | Right |

### **FExt** — External forces acting on vehicle `vector`

External forces on the vehicle, in N, specified as a `1-by-3` or
`3-by-1` vector.

FExt=Fext=[FextxFextyFextz]or[FextxFextyFextz]

| Array Element | Force Axis |
| --- | --- |
| `FExt(1,1)` | Vehicle-fixed *x*-axis (longitudinal) |
| `FExt(1,2)` or `FExt(2,1)` | Vehicle-fixed *y*-axis (lateral) |
| `FExt(1,3)` or `FExt(3,1)` | Vehicle-fixed *z*-axis (vertical) |

### **MExt** — External moments acting on vehicle `vector`

External moments acting on the vehicle, in N·m, specified as a
`1-by-3` or `3-by-1` vector.

MExt=Mext=[MextxMextyMextz]or[MextxMextyMextz]

| Array Element | Force Axis |
| --- | --- |
| `MExt(1,1)` | Vehicle-fixed *x*-axis (longitudinal) |
| `MExt(1,2)` or `MExt(2,1)` | Vehicle-fixed *y*-axis (lateral) |
| `MExt(1,3)` or `MExt(3,1)` | Vehicle-fixed *z*-axis (vertical) |

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
*Wz* along inertial *X*-,
*Y*-, and *Z*-axes, in m/s, specified as a
`1-by-3` or `3-by-1` array.

### **AirTemp** — Ambient air temperature `scalar`

Ambient air temperature, *Tair*, in K, specified as a
scalar.

#### Dependencies

To enable this port, under **Environment**, select **Air
temperature**.
### Output

### **Info** — Bus signal bus

Bus signal containing these block values.

| Signal | | | | | | Description | Value | Units |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `InertFrm` | `Cg` | `Disp` | `X` | | | Vehicle CM displacement along the earth-fixed *X*-axis | Computed relative to the road grade. | m |
| `Y` | | | Vehicle CM displacement along the earth-fixed *Y*-axis | Computed relative to the road grade. | m |
| `Z` | | | Vehicle CM displacement along the earth-fixed *Z*-axis | Computed relative to the road grade. | m |
| `Vel` | `Xdot` | | | Vehicle CM velocity along the earth-fixed *X*-axis | Computed relative to the road grade. | m/s |
| `Ydot` | | | Vehicle CM velocity along the earth-fixed *Y*-axis | Computed relative to the road grade. | m/s |
| `Zdot` | | | Vehicle CM velocity along the earth-fixed *Z*-axis | Computed relative to the road grade. | m/s |
| `Ang` | `phi` | | | Rotation of the vehicle-fixed frame about the earth-fixed *X*-axis (roll) | Computed relative to the grade angle. | rad |
| `theta` | | | Rotation of the vehicle-fixed frame about the earth-fixed *Y*-axis (pitch) | Computed relative to the grade angle. | rad |
| `psi` | | | Rotation of the vehicle-fixed frame about the earth-fixed *Z*-axis (yaw) | Computed relative to the grade angle. | rad |
| `FrntAxl` | `Lft` | `Disp` | `X` | | Front left axle displacement along the earth-fixed *X*-axis | Computed | m |
| `Y` | | Front left axle displacement along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | Front left axle displacement along the earth-fixed *Z*-axis | Computed | m |
| `Vel` | `Xdot` | | Front left axle velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | Front left axle velocity along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | Front left axle velocity along the earth-fixed *Z*-axis | Computed | m/s |
| `Rght` | `Disp` | `X` | | Front right axle displacement along the earth-fixed *X*-axis | Computed | m |
| `Y` | | Front right axle displacement along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | Front right axle displacement along the earth-fixed *Z*-axis | Computed | m |
| `Vel` | `Xdot` | | Front right axle velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | Front right axle velocity along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | Front right axle velocity along the earth-fixed *Z*-axis | Computed | m/s |
| `RearAxl` | `Lft` | `Disp` | `X` | | Rear left axle displacement along the earth-fixed *X*-axis | Computed | m |
| `Y` | | Rear left axle displacement along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | Rear left axle displacement along the earth-fixed *Z*-axis | Computed | m |
| `Vel` | `Xdot` | | Rear left axle velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | Rear left axle velocity along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | Rear left axle velocity along the earth-fixed *Z*-axis | Computed | m/s |
| `Rght` | `Disp` | `X` | | Rear right axle displacement along the earth-fixed *X*-axis | Computed | m |
| `Y` | | Rear right axle displacement along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | Rear right axle displacement along the earth-fixed *Z*-axis | Computed | m |
| `Vel` | `Xdot` | | Rear right axle velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | Rear right axle velocity along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | Rear right axle velocity along the earth-fixed *Z*-axis | Computed | m/s |
| `Hitch` | `Disp` | `X` | | | Hitch offset from axle plane along the earth-fixed *X*-axis | Computed | m |
| `Y` | | | Hitch offset from axle plane along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | | Hitch offset from axle plane along the earth-fixed *Z*-axis | Computed | m |
| `Vel` | `Xdot` | | | Hitch velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | | Hitch velocity along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | | Hitch velocity along the earth-fixed *Z*-axis | Computed | m/s |
| `Geom` | `Disp` | `X` | | | Vehicle chassis offset from axle plane along the earth-fixed *X*-axis | Computed | m |
| `Y` | | | Vehicle chassis offset from center plane along the earth-fixed *Y*-axis | Computed | m |
| `Z` | | | Vehicle chassis offset from axle plane along the earth-fixed *Z*-axis | Computed | m |
| `Vel` | `Xdot` | | | Vehicle chassis offset velocity along the earth-fixed *X*-axis | Computed | m/s |
| `Ydot` | | | Vehicle chassis offset velocity along the earth-fixed *Y*-axis | Computed | m/s |
| `Zdot` | | | Vehicle chassis offset velocity along the earth-fixed *Z*-axis | Computed | m/s |
| `BdyFrm` | `Cg` | `Vel` | `xdot` | | | Vehicle CM velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | | Vehicle CM velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | | Vehicle CM velocity along the vehicle-fixed *z*-axis | Computed | m/s |
| `AngVel` | `p` | | | Vehicle angular velocity about the vehicle-fixed *x*-axis (roll rate) | Computed | rad/s |
| `q` | | | Vehicle angular velocity about the vehicle-fixed *y*-axis (pitch rate) | Computed | rad/s |
| `r` | | | Vehicle angular velocity about the vehicle-fixed *z*-axis (yaw rate) | Computed | rad/s |
| `Acc` | `ax` | | | Vehicle CM acceleration along the vehicle-fixed *x*-axis | Computed | gn |
| `ay` | | | Vehicle CM acceleration along the vehicle-fixed *y*-axis | Computed | gn |
| `az` | | | Vehicle CM acceleration along the vehicle-fixed *z*-axis | Computed | gn |
| `xddot` | | | Vehicle CM acceleration along the vehicle-fixed *x*-axis | Computed | m/s^2 |
| `yddot` | | | Vehicle CM acceleration along the vehicle-fixed *y*-axis | Computed | m/s^2 |
| `zddot` | | | Vehicle CM acceleration along the vehicle-fixed *z*-axis | Computed | m/s^2 |
| `DCM` | Direction cosine matrix | | | | Computed | rad |
| `Forces` | `Body` | `Fx` | | | Net force on vehicle CM along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | | Net force on vehicle CM along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | | Net force on vehicle CM along the vehicle-fixed *z*-axis | Computed | N |
| `Ext` | `Fx` | | | External force on vehicle CM along the vehicle-fixed *x*-axis | Input | N |
| `Fy` | | | External force on vehicle CM along the vehicle-fixed *x*-axis | Input | N |
| `Fz` | | | External force on vehicle CM along the vehicle-fixed *x*-axis | Input | N |
| `FrntAxl` | `Lft` | `Fx` | | Longitudinal force on front left axle along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on front axle left along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Normal force on front axle left along the vehicle-fixed *z*-axis | Computed | N |
| `Rght` | `Fx` | | Longitudinal force on front right axle along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on front axle right along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Normal force on front axle right along the vehicle-fixed *z*-axis | Computed | N |
| `RearAxl` | `Lft` | `Fx` | | Longitudinal force on rear left axle along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on rear left axle along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Normal force on rear left axle along the vehicle-fixed *z*-axis | Computed | N |
| `Rght` | `Fx` | | Longitudinal force on rear right axle along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | Lateral force on rear right axle along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | Normal force on rear right axle along the vehicle-fixed *z*-axis | Computed | N |
| `Hitch` | `Fx` | | | Hitch force applied to body at the hitch location along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | | Hitch force applied to body at the hitch location along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | | Hitch force applied to body at the hitch location along the vehicle-fixed *z*-axis | Computed | N |
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
| `Fz` | Rear right tire force along the vehicle-fixed *z*-axis | Computed | N |
| `Drag` | `Fx` | | | Drag force on vehicle CM along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | | Drag force on vehicle CM along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | | Drag force on vehicle CM along the vehicle-fixed *z*-axis | Computed | N |
| `Grvty` | `Fx` | | | Gravity force on vehicle CM along the vehicle-fixed *x*-axis | Computed | N |
| `Fy` | | | Gravity force on vehicle CM along the vehicle-fixed *y*-axis | Computed | N |
| `Fz` | | | Gravity force on vehicle CM along the vehicle-fixed *z*-axis | Computed | N |
| `Moments` | `Body` | `Mx` | | | Body moment on vehicle CM about the vehicle-fixed *x*-axis | Computed | N·m |
| `My` | | | Body moment on vehicle CM about the vehicle-fixed *y*-axis | Computed | N·m |
| `Mz` | | | Body moment on vehicle CM about the vehicle-fixed *z*-axis | Computed | N·m |
| `Drag` | `Mx` | | | Drag moment on vehicle CM about the vehicle-fixed *x*-axis | Computed | N·m |
| `My` | | | Drag moment on vehicle CM about the vehicle-fixed *y*-axis | Computed | N·m |
| `Mz` | | | Drag moment on vehicle CM about the vehicle-fixed *z*-axis | Computed | N·m |
| `Ext` | `Mx` | | | External moment on vehicle CG about the vehicle-fixed *x*-axis | Computed | N·m |
| `My` | | | External moment on vehicle CG about the vehicle-fixed *y*-axis | Computed | N·m |
| `Mz` | | | External moment on vehicle CG about the vehicle-fixed *z*-axis | Computed | N·m |
| `Hitch` | `Mx` | | | Hitch moment at the hitch location about vehicle-fixed *x*-axis | Computed | N·m |
| `My` | | | Hitch moment at the hitch location about vehicle-fixed *y*-axis | Computed | N·m |
| `Mz` | | | Hitch moment at the hitch location about vehicle-fixed *z*-axis | Computed | N·m |
| `FrntAxl` | `Lft` | `Disp` | `x` | | Front left axle displacement along the vehicle-fixed *x*-axis | Computed | m |
| `y` | | Front left axle displacement along the vehicle-fixed *y*-axis | Computed | m |
| `z` | | Front left axle displacement along the vehicle-fixed *z*-axis | Computed | m |
| `Vel` | `xdot` | | Front left axle velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Front left axle velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | Front left axle velocity along the vehicle-fixed *z*-axis | Computed | m/s |
| `Rght` | `Disp` | `x` | | Front right axle displacement along the vehicle-fixed *x*-axis | Computed | m |
| `y` | | Front right axle displacement along the vehicle-fixed *y*-axis | Computed | m |
| `z` | | Front right axle displacement along the vehicle-fixed *z*-axis | Computed | m |
| `Vel` | `xdot` | | Front right axle velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Front right axle velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | Front right axle velocity along the vehicle-fixed *z*-axis | Computed | m/s |
| `RearAxl` | `Lft` | `Disp` | `x` | | Rear left axle displacement along the vehicle-fixed *x*-axis | Computed | m |
| `y` | | Rear left axle displacement along the vehicle-fixed *y*-axis | Computed | m |
| `z` | | Rear left axle displacement along the vehicle-fixed *z*-axis | Computed | m |
| `Vel` | `xdot` | | Rear left axle velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Rear left axle velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | Rear left axle velocity along the vehicle-fixed *z*-axis | Computed | m/s |
| `Rght` | `Disp` | `x` | | Rear right axle displacement along the vehicle-fixed *x*-axis | Computed | m |
| `y` | | Rear right axle displacement along the vehicle-fixed *y*-axis | Computed | m |
| `z` | | Rear right axle displacement along the vehicle-fixed *z*-axis | Computed | m |
| `Vel` | `xdot` | | Rear right axle velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Rear right axle velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | Rear right axle velocity along the vehicle-fixed *z*-axis | Computed | m/s |
| `Hitch` | `Disp` | | `x` | | Hitch offset from axle plane along the vehicle-fixed *x*-axis | Input | m |
| `y` | | Hitch offset from center plane along the vehicle-fixed *y*-axis | Input | m |
| `z` | | Hitch offset from axle plane along the vehicle-fixed *z*-axis | Input | m |
| `Vel` | | `xdot` | | Hitch offset velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Hitch offset velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | Hitch offset velocity along the vehicle-fixed *z*-axis | Computed | m/s |
| `Pwr` | `PwrExt` | | | | Applied external power | Computed | W |
| `Drag` | | | | Power loss due to drag | Computed | W |
| `Geom` | `Disp` | | `x` | | Vehicle chassis offset from axle plane along the vehicle-fixed *x*-axis | Input | m |
| `y` | | Vehicle chassis offset from center plane along the vehicle-fixed *y*-axis | Input | m |
| `z` | | Vehicle chassis offset from axle plane along the vehicle-fixed *z*-axis | Input | m |
| `Vel` | | `xdot` | | Vehicle chassis offset velocity along the vehicle-fixed *x*-axis | Computed | m/s |
| `ydot` | | Vehicle chassis offset velocity along the vehicle-fixed *y*-axis | Computed | m/s |
| `zdot` | | Vehicle chassis offset velocity along the vehicle-fixed *z*-axis | Computed | m/s |
| `Ang` | | `Beta` | | Body slip angle, *β*    β=VyVx | Computed | rad |

### **Vb** — Vehicle velocity along vehicle-fixed frame `vector`

Vehicle CM velocity along the vehicle-fixed
*x*-, *y*-,
*z*-axes, respectively, in m/s,
returned as a vector.

### **pqr** — Vehicle angular velocity about vehicle-fixed frame `vector`

Vehicle CM angular velocity about the vehicle-fixed *x*- (roll
rate), *y*- (pitch rate), *z*-axes (yaw rate),
respectively, in rad/s, returned as a vector.

### **DCM** — Direction cosine matrix `array`

Direction cosine matrix, in rad, returned as an array.

### **Euler** — Euler angles `array`

Euler angles, *φ*, *θ*, and *ψ*,
respectively, in rad, returned as an array.

### **Xe** — Vehicle position in inertial reference frame `vector`

Vehicle CM position along inertial-fixed *X*-, *Y*-,
*Z*-axes, respectively, in m, returned as a vector.

### **Ve** — Vehicle velocity in inertial reference frame `vector`

Vehicle CM velocity along inertial-fixed
*X*-, *Y*-,
*Z*-axes, respectively, in m/s,
returned as a vector.

## Parameters

### Block Options

#### Input Signals

### **Hitch forces** — Create input port `off` (default) | `on`

Select to create an input port, `Fh`, for the hitch
forces.

### **Hitch moments** — Create input port `off` (default) | `on`

Select to create an input port, `Mh`, for the hitch
moments.

### Chassis

### **Vehicle mass, m** — Mass `2000` (default) | `scalar`

Vehicle mass, *m*, in kg. This mass typically
corresponds to a sprung mass.

### **Longitudinal distance from center of mass to front axle, a** — Distance `1.4` (default) | `scalar`

Distance from vehicle CM to front axle, *a*, in m.

Top down and side views of vehicle showing load locations

### **Longitudinal distance from center of mass to rear axle, b** — Distance `1.6` (default) | `scalar`

Distance from vehicle CM to front axle, *b*, in m.

Top down and side views of vehicle showing load locations

### **Lateral distance from geometric centerline to center of mass, d** — Distance `0` (default) | `scalar`

Lateral distance from geometric centerline to center of mass,
*d*, in m, along the vehicle-fixed
*y*. Positive values indicate that the vehicle CM
is to the right of the geometric centerline. Negative values indicate
that the vehicle CM is to the left of the geometric centerline.

Top down and side views of vehicle showing load locations

### **Vertical distance from center of mass to axle plane, h** — Distance `.35` (default) | `scalar`

Vertical distance from vehicle CM to axle plane, *h*,
in m.

Top down and side views of vehicle showing load locations

### **Longitudinal distance from center of mass to hitch, dh** — Longitudinal distance from CM to hitch `1` (default) | `scalar`

Longitudinal distance from center of mass to hitch,
*dh*, in m.

Top down and side views of vehicle showing load locations

#### Dependencies

To enable this parameter, on the **Input
signals** pane, select **Hitch
forces** or **Hitch moments**.

### **Lateral distance from geometric centerline to hitch, hl** — Lateral distance from centerline to hitch `0` (default) | `scalar`

Lateral distance from geometric centerline to hitch,
*hl*, in m.

Top down and side views of vehicle showing load locations

#### Dependencies

To enable this parameter, on the **Input
signals** pane, select **Hitch
forces** or **Hitch moments**.

### **Vertical distance from hitch to axle plane, hh** — Distance from hitch to axle plane `0.1` (default) | `scalar`

Vertical distance from hitch to axle plane, *hh*, in m.

Top down and side views of vehicle showing load locations

#### Dependencies

To enable this parameter, on the **Input
signals** pane, select **Hitch
forces** or **Hitch moments**.

### **Initial position in the inertial frame [Xeo,Yeo,Zeo], Xe\_o** — Position `[0,0,0]` (default) | `vector`

Initial position of vehicle in the inertial frame,
*Xeo*, in m.

### **Initial velocity in body axes [xdot\_o,ydot\_o,zdot\_o], xbdot\_o** — Velocity `[0,0,0]` (default) | `vector`

Initial vehicle CM velocity along the vehicle-fixed
*x*-, *y*-, and
*z*- axes, respectively, in m/s.

### **Initial Euler orientation [roll, pitch, yaw], eul\_o** — Rotation `[0,0,0]` (default) | `vector`

Initial Euler rotation of the vehicle-fixed frame about the
earth-fixed *X*(roll)-,
*Y*(pitch)-, *Z*(yaw)- axes,
respectively, in rad.

### **Initial body rotation rates [p,q,r], p\_o** — Rotation rate `[0,0,0]` (default) | `vector`

Initial vehicle CM angular velocity about the vehicle-fixed
*x*(roll rate)-, *y*(pitch
rate)-, *z*(yaw rate)- axes, respectively, in
rad/s.

### **Chassis inertia tensor, Iveh** — Inertia `[430 0 0; 0 1900 0; 0 0 2100]` (default) | `array`

Vehicle inertia tensor,
*Iveh*, in kg\*m^2. Dimensions
are `[3-by-3]`.

### **Track widths [front,rear], w** — Widths `[1.9,1.9]` (default) | `vector`

Front and rear track width, in m. Dimensions are
`[1-by-2]`.

### Inertial Loads

#### Front

### **Mass, z1m** — Mass `0` (default) | `scalar`

Mass, *z1m*, in kg.

### **Distance vector from front axle, z1R** — Distance `[-.25,.125,.15]` (default) | `vector`

Distance vector from front axle to load, *z1R*, in m.
Dimensions are `[1-by-3]`.

| Array Element | Description |
| --- | --- |
| `z1R(1,1)` | Front suspension hardpoint to load, along the vehicle-fixed *x*-axis |
| `z1R(1,2)` | Vehicle centerline to load, along the vehicle-fixed *y*-axis |
| `z1R(1,3)` | Front suspension hardpoint to load, along the vehicle-fixed *z*-axis |

Top down and side views of vehicle showing load locations

For example, this table summarizes the parameter settings that specify
the load location indicated by the dots.

| Example Location | Sign |
| --- | --- |
| - Forward of the front axle - Right of the vehicle centerline - Above the front axle suspension   hardpoint | - `z1R(1,1)` < 0 - `z1R(1,2)` > 0 - `z1R(1,3)` > 0 |

### **Inertia tensor, z1I** — Inertia `[1.4,-.2,.1;-.2,1.4,.1;.1,.1,2.25].*0` (default) | `array`

Inertia tensor, *z1I*, in kg·m^2. Dimensions are
`[3-by-3]`.

z1I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

The tensor uses a coordinate system with an origin at the load CM.

- *x*-axis along the vehicle-fixed
  *x*-axis
- *y*-axis along the vehicle-fixed
  *y*-axis
- *z*-axis along the vehicle-fixed
  *z*-axis

Top down and side views of vehicle showing load locations

#### Overhead

### **Mass, z2m** — Mass `0` (default) | `scalar`

Mass, *z2m*, in kg.

### **Distance vector from front axle, z2R** — Distance `[1.4,0,.8]` (default) | `vector`

Distance vector from front axle to load, *z2R*, in m.
Dimensions are `[1-by-3]`.

| Array Element | Description |
| --- | --- |
| `z2R(1,1)` | Front suspension hardpoint to load, along the vehicle-fixed *x*-axis |
| `z2R(1,2)` | Vehicle centerline to load, along the vehicle-fixed *y*-axis |
| `z2R(1,3)` | Front suspension hardpoint to load, along the vehicle-fixed *z*-axis |

Top down and side views of vehicle showing load locations

For example, this table summarizes the parameter settings that specify
the load location indicated by the dot.

| Example Location | Sign |
| --- | --- |
| - Rear of the front axle - Left of the vehicle centerline - Above the front axle suspension   hardpoint | - `z2R(1,1)` > 0 - `z2R(1,2)` < 0 - `z2R(1,3)` > 0 |

### **Inertia tensor, z2I** — Inertia `[1.4,-.2,.1;-.2,1.4,.1;.1,.1,2.25].*0` (default) | `array`

Inertia tensor, *z2I*, in kg·m^2. Dimensions are
`[3-by-3]`.

z2I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

The tensor uses a coordinate system with an origin at the load CM.

- *x*-axis along the vehicle-fixed
  *x*-axis
- *y*-axis along the vehicle-fixed
  *y*-axis
- *z*-axis along the vehicle-fixed
  *z*-axis

Top down and side views of vehicle showing load locations

#### Row 1, left side

### **Mass, z3m** — Mass `0` (default) | `scalar`

Mass, *z3m*, in kg.

### **Distance vector from front axle, z3R** — Distance `[.75,-.5,.4]` (default) | `vector`

Distance vector from front axle to load, *z3R*, in m.
Dimensions are `[1-by-3]`.

| Array Element | Description |
| --- | --- |
| `z3R(1,1)` | Front suspension hardpoint to load, along the vehicle-fixed *x*-axis |
| `z3R(1,2)` | Vehicle centerline to load, along the vehicle-fixed *y*-axis |
| `z3R(1,3)` | Front suspension hardpoint to load, along the vehicle-fixed *z*-axis |

Top down and side views of vehicle showing load locations

For example, this table summarizes the parameter settings that specify
the load location indicated by the dot.

| Example Location | Sign |
| --- | --- |
| - Rear of the front axle - Left of the vehicle centerline - Above the front axle suspension   hardpoint | - `z3R(1,1)` > 0 - `z3R(1,2)` < 0 - `z3R(1,3)` > 0 |

### **Inertia tensor, z3I** — Inertia `[5,-.1,-2;-2,9,.1;-.1,.1,6].*0` (default) | `array`

Inertia tensor, *z3I*, in kg·m^2. Dimensions are
`[3-by-3]`.

z3I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

The tensor uses a coordinate system with an origin at the load CM.

- *x*-axis along the vehicle-fixed
  *x*-axis
- *y*-axis along the vehicle-fixed
  *y*-axis
- *z*-axis along the vehicle-fixed
  *z*-axis

Top down and side views of vehicle showing load locations

#### Row 1, right side

### **Mass, z4m** — Mass `0` (default) | `scalar`

Mass, *z4m*, in kg.

### **Distance vector from front axle, z4R** — Distance `[.75,.5,.4]` (default) | `vector`

Distance vector from front axle to load, *z4R*, in m.
Dimensions are `[1-by-3]`.

| Array Element | Description |
| --- | --- |
| `z4R(1,1)` | Front suspension hardpoint to load, along the vehicle-fixed *x*-axis |
| `z4R(1,2)` | Vehicle centerline to load, along the vehicle-fixed *y*-axis |
| `z4R(1,3)` | Front suspension hardpoint to load, along the vehicle-fixed *z*-axis |

Top down and side views of vehicle showing load locations

For example, this table summarizes the parameter settings that specify
the load location indicated by the dot.

| Example Location | Sign |
| --- | --- |
| - Rear of the front axle - Right of the vehicle centerline - Above the front axle suspension   hardpoint | - `z4R(1,1)` > 0 - `z4R(1,2)` > 0 - `z4R(1,3)` > 0 |

### **Inertia tensor, z4I** — Inertia `[5,-.1,-2;-2,9,.1;-.1,.1,6].*0` (default) | `array`

Inertia tensor, *z4I*, in kg·m^2. Dimensions are
`[3-by-3]`.

z4I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

The tensor uses a coordinate system with an origin at the load CM.

- *x*-axis along the vehicle-fixed
  *x*-axis
- *y*-axis along the vehicle-fixed
  *y*-axis
- *z*-axis along the vehicle-fixed
  *z*-axis

Top down and side views of vehicle showing load locations

#### Row 2, left side

### **Mass, z5m** — Mass `0` (default) | `scalar`

Mass, z5m, in kg.

### **Distance vector from front axle, z5R** — Distance `[1.25,-.5,.4]` (default) | `vector`

Distance vector from front axle to load, *z5R*, in m.
Dimensions are `[1-by-3]`.

| Array Element | Description |
| --- | --- |
| `z5R(1,1)` | Front suspension hardpoint to load, along the vehicle-fixed *x*-axis |
| `z5R(1,2)` | Vehicle centerline to load, along the vehicle-fixed *y*-axis |
| `z5R(1,3)` | Front suspension hardpoint to load, along the vehicle-fixed *z*-axis |

Top down and side views of vehicle showing load locations

For example, this table summarizes the parameter settings that specify
the load location indicated by the dot.

| Example Location | Sign |
| --- | --- |
| - Rear of the front axle - Left of the vehicle centerline - Above the front axle suspension   hardpoint | - `z5R(1,1)` > 0 - `z5R(1,2)` < 0 - `z5R(1,3)` > 0 |

### **Inertia tensor, z5I** — Inertia `[5,-.1,-2;-2,9,.1;-.1,.1,6].*0` (default) | `array`

Inertia tensor, *z5I*, in kg·m^2. Dimensions are
`[3-by-3]`.

z5I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

The tensor uses a coordinate system with an origin at the load CM.

- *x*-axis along the vehicle-fixed
  *x*-axis
- *y*-axis along the vehicle-fixed
  *y*-axis
- *z*-axis along the vehicle-fixed
  *z*-axis

Top down and side views of vehicle showing load locations

#### Row 2, right side

### **Mass, z6m** — Mass `0` (default) | `scalar`

Mass, *z6m*, in kg.

### **Distance vector from front axle, z6R** — Distance `[1.25,-.5,.4]` (default) | `vector`

Distance vector from front axle to load, *z6R*, in m.
Dimensions are `[1-by-3]`.

| Array Element | Description |
| --- | --- |
| `z6R(1,1)` | Front suspension hardpoint to load, along the vehicle-fixed *x*-axis |
| `z6R(1,2)` | Vehicle centerline to load, along the vehicle-fixed *y*-axis |
| `z6R(1,3)` | Front suspension hardpoint to load, along the vehicle-fixed *z*-axis |

Top down and side views of vehicle showing load locations

For example, this table summarizes the parameter settings that specify
the load location indicated by the dot.

| Example Location | Sign |
| --- | --- |
| - Rear of the front axle - Right of the vehicle centerline - Above the front axle suspension   hardpoint | - `z6R(1,1)` > 0 - `z6R(1,2)` > 0 - `z6R(1,3)` > 0 |

### **Inertia tensor, z6I** — Inertia `[5,-.1,-2;-2,9,.1;-.1,.1,6].*0` (default) | `array`

Inertia tensor, *z6I*, in kg·m^2. Dimensions are
`[3-by-3]`.

z6I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

The tensor uses a coordinate system with an origin at the load CM.

- *x*-axis along the vehicle-fixed
  *x*-axis
- *y*-axis along the vehicle-fixed
  *y*-axis
- *z*-axis along the vehicle-fixed
  *z*-axis

Top down and side views of vehicle showing load locations

#### Rear

### **Mass, z7m** — Mass `0` (default) | `scalar`

Mass, *z7m*, in kg.

### **Distance vector from front axle, z7R** — Distance `[2,0,.25]` (default) | `vector`

Distance vector from front axle to load, *z7R*, in m.
Dimensions are `[1-by-3]`.

| Array Element | Description |
| --- | --- |
| `z7R(1,1)` | Front suspension hardpoint to load, along the vehicle-fixed *x*-axis |
| `z7R(1,2)` | Vehicle centerline to load, along the vehicle-fixed *y*-axis |
| `z7R(1,3)` | Front suspension hardpoint to load, along the vehicle-fixed *z*-axis |

Top down and side views of vehicle showing load locations

For example, this table summarizes the parameter settings that specify
the load location indicated by the dot.

| Example Location | Sign |
| --- | --- |
| - Rear of the front axle - Right of the vehicle centerline - Above the front axle suspension   hardpoint | - `z7R(1,1)` > 0 - `z7R(1,2)` > 0 - `z7R(1,3)` > 0 |

### **Inertia tensor, z7I** — Inertia `[1.4,-.2,.1;-.2,1.4,.1;.1,.1,2.25].*0` (default) | `array`

Inertia tensor, *z7I*, in kg·m^2. Dimensions are
`[3-by-3]`.

z7I=[IxxIxyIxzIyxIyyIyzIzxIzyIzz]

The tensor uses a coordinate system with an origin at the load CM.

- *x*-axis along the vehicle-fixed
  *x*-axis
- *y*-axis along the vehicle-fixed
  *y*-axis
- *z*-axis along the vehicle-fixed
  *z*-axis

Top down and side views of vehicle showing load locations

### Aerodynamic

### **Longitudinal drag area, Af** — Area `2` (default) | `scalar`

Effective vehicle cross-sectional area,
*Af* to calculate the
aerodynamic drag force on the vehicle, in m^2.

### **Longitudinal drag coefficient, Cd** — Drag `.3` (default) | `scalar`

Air drag coefficient, *Cd*,
dimensionless.

### **Longitudinal lift coefficient, Cl** — Lift `.1` (default) | `scalar`

Air lift coefficient, *Cl*,
dimensionless.

### **Longitudinal drag pitch moment, Cpm** — Pitch drag `.1` (default) | `scalar`

Longitudinal drag pitch moment coefficient,
*Cpm*,
dimensionless.

### **Relative wind angle vector, beta\_w** — Wind angle `[0:0.001:0.01]` (default) | `vector`

Relative wind angle vector,
*βw*, in rad.

### **Side force coefficient vector, Cs** — Side force drag `[0:0.01:0.1]` (default) | `vector`

Side force coefficient vector coefficient,
*Cs*,
dimensionless.

### **Yaw moment coefficient vector, Cym** — Yaw moment drag `[0:0.001:0.01]` (default) | `vector`

Yaw moment coefficient vector coefficient,
*Cym*,
dimensionless.

### Environment

### **Absolute Pressure, Pabs** — Pressure `101325` (default) | `scalar`

Environmental air absolute pressure,
*Pabs*, in Pa.

### **Air temperature, Tair** — Ambient air temperature `273` (default) | `scalar`

Ambient air temperature, *Tair*, in K.

#### Dependencies

To enable this parameter, clear **Air temperature**.

### **Gravitational acceleration, g** — Gravity `9.81` (default) | `scalar`

Gravitational acceleration, *g*, in m/s^2.

### Simulation

### **Longitudinal velocity tolerance, xdot\_tol** — Tolerance `.1` (default) | `scalar`

Longitudinal velocity tolerance,
*xdottol*, in
m/s.

The block uses this parameter to avoid a division by zero when it
calculates the body slip angle, *β*.

### **Geometric longitudinal offset from axle plane, longOff** — Longitudinal offset `0` (default) | `scalar`

Vehicle chassis offset from axle plane along body-fixed
*x*-axis, in m. When you use the 3D visualization
engine, consider using the offset to locate the chassis independent of
the vehicle CG.

### **Geometric lateral offset from center plane, latOff** — Lateral offset `0` (default) | `scalar`

Vehicle chassis offset from center plane along body-fixed
*y*-axis, in m. When you use the 3D visualization
engine, consider using the offset to locate the chassis independent of
the vehicle CG.

### **Geometric vertical offset from axle plane, vertOff** — Vertical offset `0` (default) | `scalar`

Vehicle chassis offset from axle plane along body-fixed
*z*-axis, in m. When you use the 3D visualization
engine, consider using the offset to locate the chassis independent of
the vehicle CG.

### **Wrap Euler angles, wrapAng** — Selection `on` (default) | `off`

Wrap the Euler angles to the interval `[-pi, pi]`.
For vehicle maneuvers that might undergo vehicle yaw rotations that are
outside of the interval, consider deselecting the parameter if you want to:

- Track the total vehicle yaw rotation.
- Avoid discontinuities in the vehicle state
  estimators.

## Libraries

Vehicle Dynamics Blockset / Vehicle Body

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Two-axle vehicle body with translational and rotational motion

The Vehicle Body 6DOF block implements a six degrees-of-freedom (DOF)
rigid two-axle vehicle body model to calculate longitudinal, lateral, vertical, pitch,
roll, and yaw motion. The block accounts for body mass, inertia, aerodynamic drag, road
incline, and weight distribution between the axles due to suspension and external forces
and moments. Use the **Inertial Loads** parameters to analyze the
vehicle dynamics under different loading conditions.

You can connect the block to virtual sensors, suspension system, or external systems
like body control actuators. Use the Vehicle Body 6DOF block in ride and
handling studies to model the effects of drag forces, passenger loading, and suspension
hardpoint locations.

To create additional input ports, under **Input signals**, select these block parameters.

| Parameter | Input Port | Description |
| --- | --- | --- |
| **Front hitch forces** | `FhF` | Hitch force applied to the body at the front hitch location, *FhFx*, *FhFy*, and *FhFz*, in the vehicle-fixed frame |
| **Front hitch moments** | `MhF` | Hitch moment at the front hitch location, *MhFx*, *MhFy*, and *MhFz*, about the vehicle-fixed frame |
| **Rear hitch forces** | `FhR` | Hitch force applied to the body at the rear hitch location, *FhRx*, *FhRy*, and *FhRz*, in the vehicle-fixed frame |
| **Rear hitch moments** | `MhR` | Hitch moment at the rear hitch location, *MhRx*, *MhRy*, and *MhRz*, about the vehicle-fixed frame |

### Inertial Loads

To analyze the vehicle dynamics under different loading conditions, use the
**Inertial Loads** parameters. Specifically, you can specify these loads:

- Front powertrain
- Front and rear row passengers
- Overhead cargo
- Rear cargo

For each of the loads, you can specify the mass, location, and inertia.

The illustrations provide the load locations and vehicle parameter dimensions. The table
provides the corresponding location parameter sign settings.

Top down and side views of vehicle showing load locations

This table summarizes the parameter settings that specify the load locations indicated by the
dots. For the location, the block uses this distance vector:

- Front suspension hardpoint to load, along the vehicle-fixed
  *x*-axis
- Vehicle centerline to load, along the vehicle-fixed
  *y*-axis
- Front suspension hardpoint to load, along the vehicle-fixed
  *z*-axis

| Load | Parameter | Example Location |
| --- | --- | --- |
| Front | **Distance vector from front axle, z1R** | - `z1R(1,1)<0` — Forward of the   front axle - `z1R(1,2)>0` — Right of the vehicle   centerline - `z1R(1,3)>0` — Above the front axle   suspension hardpoint |
| Overhead | **Distance vector from front axle, z2R** | - `z2R(1,1)>0` — Rear of the front   axle - `z2R(1,2)<0` — Left of the vehicle   centerline - `z2R(1,3)>0` — Above the front axle   suspension hardpoint |
| Row 1, left side | **Distance vector from front axle, z3R** | - `z3R(1,1)>0` — Rear of the front   axle - `z3R(1,2)<0` — Left of the vehicle   centerline - `z3R(1,3)>0` — Above the front axle   suspension hardpoint |
| Row 1, right side | **Distance vector from front axle, z4R** | - `z4R(1,1)>0` — Rear of the front   axle - `z4R(1,2)>0` — Right of the vehicle   centerline - `z4R(1,3)>0` — Above the front axle   suspension hardpoint |
| Row 2, left side | **Distance vector from front axle, z5R** | - `z5R(1,1)>0` — Rear of the front   axle - `z5R(1,2)<0` — Left of the vehicle   centerline - `z5R(1,3)>0` — Above the front axle   suspension hardpoint |
| Row 2, right side | **Distance vector from front axle, z6R** | - `z6R(1,1)>0` — Rear of the front   axle - `z6R(1,2)>0` — Right of the vehicle   centerline - `z6R(1,3)>0` — Above the front axle   suspension hardpoint |
| Rear | **Distance vector from front axle, z7R** | - `z7R(1,1)>0` — Rear of the front   axle - `z7R(1,2)>0` — Right of the vehicle   centerline - `z7R(1,3)>0` — Above the front axle   suspension hardpoint |

### Equations of Motion

To determine the vehicle motion, the block implements calculations for the rigid
body vehicle dynamics, wind drag, inertial loads, and coordinate transformations.
The body-fixed and the vehicle-fixed are the same coordinate systems.

The Vehicle Body 6DOF block considers the rotation of a body-fixed
coordinate frame about a flat earth-fixed inertial reference frame. The origin of
the body-fixed coordinate frame is the vehicle center of gravity of the body.

Isometric view of vertical, longitudinal, and lateral forces acting at suspension locations

The block uses this equation to calculate the translational motion of the
body-fixed coordinate frame, where the applied forces
[*Fx Fy
Fz*]T are in the
body-fixed frame, and the mass of the body, *m*, is assumed constant.

F¯b=[FxFyFz]=m(V¯˙b+ω¯×V¯b)M¯b=[LMN]=Iω¯˙+ω¯×(Iω¯)I=[Ixx−Ixy−Ixz−IyxIyy−Iyz−Izx−IzyIzz]

To determine the relationship between the body-fixed angular velocity vector,
[*p q r*]T, and the rate of change
of the Euler angles, [ϕ˙  θ˙   ψ˙]T, the block resolves the Euler rates into the body-fixed frame.

[pqr]=[ϕ˙00]+[1000cosϕsinϕ0−sinϕcosϕ][0θ˙0]+[1000cosϕsinϕ0−sinϕcosϕ][cosθ0−sinθ010sinθ0cosθ][00ψ˙]≡J−1[ϕ˙θ˙ψ˙]

Inverting *J* gives the required relationship to determine the
Euler rate vector.

[ϕ˙θ˙ψ˙]=J[pqr] =[1(sinϕtanθ)(cosϕtanθ)0cosϕ−sinϕ0sinϕcosθcosϕcosθ][pqr]

The applied forces and moments are the sum of the drag, gravitational, external,
and suspension forces.

F¯b=[FxFyFz]=[FdxFdyFdz]+[FgxFgyFgz]+[FextxFextyFextz]+[FFLxFFLyFFLz]+[FFRxFFRyFFRz]+[FRLxFRLyFRLz]+[FRRxFRRyFRRz]M¯b=[MxMyMz]=[MdxMdyMdz]+[MextxMextyMextz]+[MFLxMFLyMFLz]+[MFRxMFRyMFRz]+[MRLxMRLyMRLz]+[MRRxMRRyMRRz]+M¯F

| Calculation | Implementation |
| --- | --- |
| *Load masses and inertias* | Block uses parallel axis theorem to resolve the individual load masses and inertias with the vehicle mass and inertia.  Jij=Iij+m(|R|2δij−RiRj) |
| *Gravitational forces, *Fg** | Block uses direction cosine matrix (DCM) to transform the gravitational vector in the inertial-fixed frame to the body-fixed frame. |
| *Drag forces, *Fd*, and moments*, *Md* | To determine a relative airspeed, the block subtracts the wind speed from the vehicle center of mass (CM) velocity. Using the relative airspeed, the block determines the drag forces.  w¯=(x˙−wx)2+(y˙−wy)2+(wz)2Fdx=−12TRCdAfPabs(w¯)2Fdy=−12TRCsAfPabs(w¯)2Fdz=−12TRClAfPabs(w¯)2    Using the relative airspeed, the block determines the drag moments.  Mdr=−12TRCrmAfPabs(w¯)2(a+b)Mdp=−12TRCpmAfPabs(w¯)2(a+b)Mdy=−12TRCymAfPabs(w¯)2(a+b) |
| *External forces, *Fin*, and moments*, *Min* | External forces and moments are input via ports `FExt` and `MExt`. |
| *Suspension forces and moments* | Block assumes that the suspension forces and moments act on these hardpoint locations:  - *FFL*,   *MFL* —   Front left - *FFR*,   *MFR* —   Front right - *FRL*,   *MRL* —   Rear left - *FRR*,   *MRR* —   Rear right |

The equations use these variables.

|  |  |
| --- | --- |
| x,x˙,x¨ | Vehicle CM displacement, velocity, and acceleration along the vehicle-fixed *x*-axis |
| y,y˙,y¨ | Vehicle CM displacement, velocity, and acceleration along the vehicle-fixed *y*-axis |
| z,z˙,z¨ | Vehicle CM displacement, velocity, and acceleration along the vehicle-fixed *z*-axis |
| *φ* | Rotation of the vehicle-fixed frame about the earth-fixed *X*-axis (roll) |
| *θ* | Rotation of the vehicle-fixed frame about the earth-fixed *Y*-axis (pitch) |
| *ψ* | Rotation of the vehicle-fixed frame about the earth-fixed *Z*-axis (yaw) |
| *FFLx*, *FFLy*, *FFLz* | Suspension forces applied to front left hardpoint along the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *FFRx*, *FFRy*, *FFRz* | Suspension forces applied to front right hardpoint along the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *FRLx*, *FRLy*, *FRLz* | Suspension forces applied to rear left hardpoint along the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *FRRx*, *FRRy*, *FRRz* | Suspension forces applied to rear right hardpoint along the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *MFx*, *FFy*, *FFz* | Suspension moments applied to vehicle CM about the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *Fextx*, *Fexty*, *Fextz* | External forces applied to vehicle CM along the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *Fdx*, *Fdy*, *Fdz* | Drag forces applied to vehicle CM along the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *Mextx*, *Mexty*, *Mextz* | External moment about vehicle CM about the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *Mdx*, *Mdy*, *Mdz* | Drag moment about vehicle CM about the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *I* | Vehicle body moments of inertia |
| *a*, *b* | Distance of front and rear wheels, respectively, from the normal projection point of vehicle CM onto the common axle plane |
| *d* | Lateral distance from the geometric centerline to the center of mass along the vehicle-fixed *y*-axis |
| *h* | Height of vehicle CM above the axle plane |
| *hh* | Height of the hitch above the axle plane along the vehicle-fixed *z*-axis |
| *dh* | Longitudinal distance of the hitch from the normal projection point of tractor CG onto the common axle plane |
| *hl* | Lateral distance from center of mass to hitch along the vehicle-fixed *y*-axis. |
| *wF*, *wR* | Front and rear track widths |
| *Cd* | Air drag coefficient acting along the vehicle-fixed *x*-axis |
| *Cs* | Air drag coefficient acting along the vehicle-fixed *y*-axis |
| *Cl* | Air drag coefficient acting along the vehicle-fixed *z*-axis |
| *Crm* | Air drag roll moment acting about vehicle-fixed *x*-axis |
| *Cpm* | Air drag pitch moment acting about the vehicle-fixed *y*-axis |
| *Cym* | Air drag yaw moment acting about vehicle-fixed *z*-axis |
| *Af* | Frontal area |
| *R* | Atmospheric specific gas constant |
| *T* | Environmental air temperature |
| *Pabs* | Environmental absolute pressure |
| *wx*, *wy*, *wz* | Wind speed along the vehicle-fixed *x*-, *y*-, and *z*-axes |
| *Wx*, *Wy*, *Wz* | Wind speed along inertial *X*-, *Y*-, and *Z*-axes |
