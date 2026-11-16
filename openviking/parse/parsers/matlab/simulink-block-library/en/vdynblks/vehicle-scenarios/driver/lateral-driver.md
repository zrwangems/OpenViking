---
type: simulink-block
title: 'Lateral Driver'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / Driver'
documentation_page: 'lateraldriver'
documentation_source_path: 'ref/lateraldriver.html'
language: en
---

# Lateral Driver

## Ports

### Input

### **LongRef** — Longitudinal displacement reference `scalar`

Longitudinal center of mass (CM) displacement reference, in the
inertial reference frame, in m.

#### Dependencies

To enable this port:

- Set **Lateral control type,
  controlTypeLat** to
  `Stanley`
- Clear **Vector input for
  poses**

### **LatRef** — Lateral displacement reference `scalar`

Lateral center of mass (CM) displacement reference, in the inertial
reference frame, in m.

#### Dependencies

To enable this port, do either of these:

- Set **Lateral control type,
  controlTypeLat** to
  `Stanley` and clear
  **Vector input for poses**.
- Set **Lateral control type,
  controlTypeLat** to
  `Predictive`.

### **EnblSteerOvr** — Enable steering command override `scalar`

Enable steering command override.

#### Dependencies

To enable this port, select **Steering override**.

**Data Types:** `Boolean`

### **SteerOvrCmd** — Steering override command `scalar`

Steering override command.

Use the **Output handwheel angle** parameter to specify the units for the steering ports.

| Setting | Block Implementation | Port | |
| --- | --- | --- | --- |
| `off` (default) | Commanded steer angle, normalized from -1 through 1. The block uses the tire wheel angle saturation limit **Tire wheel angle limit, theta** parameter to normalize the command. | `SteerCmd` — Output | |
| Overrides the steering command with an input steering command normalized from -1 through 1. | `SteerOvrCmd` — Input | |
| `on` | Commanded steer angle, in units specified by **Angular units, angUnits**. | `SteerCmd` — Output | |
| Overrides the steering command with an input steering command, in units specified by **Angular units, angUnits**. | `SteerOvrCmd` — Input | |

#### Dependencies

To enable this port, select **Steering override**.

**Data Types:** `double`

### **SteerHld** — Steering hold `scalar`

Boolean signal that holds the steering command at the current value.

#### Dependencies

To enable this port, select **Steering hold**.

**Data Types:** `Boolean`

### **SteerZero** — Disable steering command `scalar`

Disable steering command.

#### Dependencies

To enable this port, select **Steering disable**.

**Data Types:** `Boolean`

### **YawRef** — Yaw angle reference `scalar`

Vehicle yaw angle, *Ψo*, in
the inertial reference frame, in units specified by **Angular
units, angUnits**.

#### Dependencies

To enable this port:

- Set **Lateral control type,
  controlTypeLat** to
  `Stanley`
- Clear **Vector input for
  poses**

### **RefPose** — Reference pose [*x*, *y*, *Θ*] vector

Reference pose, specified as an [*x*, *y*,
*Θ*] vector. *x* and *y* are
in meters, and *Θ* are in units specified by **Angular
units, angUnits**.

*x* and *y* specify the reference point to steer
the vehicle toward. *Θ* specifies the orientation angle of the path
at this reference point and is positive in the counterclockwise direction.

The reference point is the point on the path that is closest to the vehicle CG.
You can use the either the Z-up or Z-down vehicle coordinate system, as long you use
the same coordinate system (Z-up or Z-down) for block inputs and parameters.

Figure indicating location of x, y, and theta on vehicle path

#### Dependencies

To enable this port, set **Lateral control type,
controlTypeLat** to `Stanley` and select
**Vector input for poses**.

**Data Types:** `single` | `double`

### **VelFdbk** — Longitudinal vehicle velocity `scalar`

Longitudinal vehicle velocity, *U*, in the vehicle-fixed frame,
in m/s.

### **CurrPose** — Current pose [*x*, *y*, *Θ*] vector

Current pose of the vehicle, specified as an [*x*,
*y*, *Θ*] vector. *x* and
*y* are in meters, and *Θ* is in units
specified by **Angular units, angUnits**.

*x* and *y* specify the location of the vehicle,
which is defined as the vehicle CG. You can use the either the Z-up or Z-down
vehicle coordinate system, as long you use the same coordinate system (Z-up or
Z-down) for block inputs and parameters.

Figure indicating location of x, y, and theta on vehicle path

#### Dependencies

To enable this port, set **Lateral control type,
controlTypeLat** to `Stanley` and select
**Vector input for poses**.

**Data Types:** `single` | `double`

### **LatFdbk** — Lateral displacement `scalar`

Lateral CM displacement, *yo*, in the
inertial reference frame, in m.

#### Dependencies

To enable this port, do either of these:

- Set **Lateral control type, controlTypeLat** to
  `Stanley` and clear **Vector
  input for poses**.
- Set **Lateral control type, controlTypeLat** to
  `Predictive`.

### **LatVelFdbk** — Lateral vehicle velocity `scalar`

Lateral vehicle velocity, *vo* , in the
vehicle-fixed frame, in m/s.

#### Dependencies

To enable this port, Set **Lateral control type,
controlTypeLat** to `Predictive`.

### **YawFdbk** — Vehicle yaw angle `scalar`

Vehicle yaw angle, *Ψo*, in the inertial
reference frame, in units specified by **Angular units,
angUnits**.

#### Dependencies

To enable this port, do either of these:

- Set **Lateral control type, controlTypeLat** to
  `Stanley` and clear **Vector
  input for poses**.
- Set **Lateral control type, controlTypeLat** to
  `Predictive`.

### **YawVelFdbk** — Yaw rate `scalar`

Yaw rate, *ro*, in the vehicle-fixed
frame, in units specified by **Angular units, angUnits** per
sec.

#### Dependencies

To enable this port, Set **Lateral control type,
controlTypeLat** to `Predictive`.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | Variable | Description |
| --- | --- | --- | --- |
| `Predicted` | `y` | *y* | Predicted lateral displacement, in the vehicle-fixed frame. |
| `ydot` | *v* | Predicted lateral velocity, in the vehicle-fixed frame. |
| `psi` | *Ψ* | Predicted front wheel heading angle. |
| `r` | *r* | Predicted yaw rate, in the vehicle-fixed frame. |
| `SteerCmd` | | *δF* | Commanded steer angle. |
| `Err` | | *eref* | Difference in reference vehicle position and vehicle position. |
| `ErrSqrSum` | | ∫0teref2dt | Integrated square of error. |
| `ErrMax` | | max(eref(t)) | Maximum error during simulation. |
| `ErrMin` | | min(eref(t)) | Minimum error during simulation. |
| `ExtActions` | `EnblSteerOvr` | | Override the steering command with an input deceleration command. |
| `SteerOvrCmd` | | Input steering override command |
| `SteerHld` | | Hold the steering command at the current value |
| `SteerZero` | | Disable the steering command |

### **SteerCmd** — Steer angle command `scalar`

Commanded steer angle,
*δF*.

Use the **Output handwheel angle** parameter to specify the units for the steering ports.

| Setting | Block Implementation | Port | |
| --- | --- | --- | --- |
| `off` (default) | Commanded steer angle, normalized from -1 through 1. The block uses the tire wheel angle saturation limit **Tire wheel angle limit, theta** parameter to normalize the command. | `SteerCmd` — Output | |
| Overrides the steering command with an input steering command normalized from -1 through 1. | `SteerOvrCmd` — Input | |
| `on` | Commanded steer angle, in units specified by **Angular units, angUnits**. | `SteerCmd` — Output | |
| Overrides the steering command with an input steering command, in units specified by **Angular units, angUnits**. | `SteerOvrCmd` — Input | |

## Parameters

### Configuration

### **Steering override** — Override steering command `off` (default) | `on`

Select to override the steering command with an input steering command.

#### Dependencies

Selecting this parameter creates the `EnblSteerOvr` and
`SteerOvrCmd` input ports.

### **Steering hold** — Hold steering command `off` (default) | `on`

Select to hold the steering command.

#### Dependencies

Selecting this parameter creates the `SteerHld` input
port.

### **Steering disable** — Disable steering command `off` (default) | `on`

Select to disable the steering command.

#### Dependencies

Selecting this parameter creates the `SteerZero` input
port.

### **Output handwheel angle** — Steering port units in rad `off` (default) | `on`

Use the **Output handwheel angle** parameter to specify the units for the steering ports.

| Setting | Block Implementation | Port | |
| --- | --- | --- | --- |
| `off` (default) | Commanded steer angle, normalized from -1 through 1. The block uses the tire wheel angle saturation limit **Tire wheel angle limit, theta** parameter to normalize the command. | `SteerCmd` — Output | |
| Overrides the steering command with an input steering command normalized from -1 through 1. | `SteerOvrCmd` — Input | |
| `on` | Commanded steer angle, in units specified by **Angular units, angUnits**. | `SteerCmd` — Output | |
| Overrides the steering command with an input steering command, in units specified by **Angular units, angUnits**. | `SteerOvrCmd` — Input | |

#### Dependencies

To create the `SteerOvrCmd` input port, select **Steering
override**.

### **Lateral control type, controlTypeLat** — Controller `Predictive` (default) | `Stanley`

Use the **Lateral control type, controlTypeLat** parameter to specify the type of lateral control. The table specifies the block implementation.

| Setting | Block Implementation |
| --- | --- |
| `Predictive` (default) | Optimal single-point preview (look ahead) control model developed by C. C. MacAdam1, 2, 3. The model represents driver steering control behavior during path-following and obstacle avoidance maneuvers. Drivers preview (look ahead) to follow a predefined path. |
| `Stanley` | Controller that uses the Stanley4 method to minimize the position error and the angle error of the current pose with respect to the reference pose.  On the **Reference Control** pane, use the:  - **Vector input for poses** parameter to   input the to specify the input.  | Setting | Implementation |   | --- | --- |   | `off` (default) | Block uses the longitudinal, lateral, and yaw reference (`LongRef`, `LatRef`, `LatRef`) input ports and the feedback (`LongFdbk`, `LatFdbk`, `LatFdbk`) input ports for the reference and feedback pose. |   | `on` | Block uses input ports, `RefPose` and `CurrPose`, for the reference and feedback pose, respectively. | - **Include dynamics** parameter to specify   the type of model for the controller to use.  | Setting | Implementation |   | --- | --- |   | `off` (default) | Controller uses a kinematic bicycle model that is suitable for path following in low-speed environments such as parking lots, where inertial effects are minimal. |   | `on` | Controller uses a dynamic bicycle model that is suitable for path following in high-speed environments such as highways, where inertial effects are more pronounced. | |

### **Angular units, angUnits** — Input and output port angular units `rad` (default) | `deg`

Input and output port angular units.

### Reference Control

#### Predictive

### **Driver response time, tau** — Response time `0.1` (default) | `scalar`

Driver response time, *τ*, in s.

#### Dependencies

To enable this parameter, Set **Lateral control type,
controlTypeLat** to `Predictive`.

### **Preview distance, L** — Distance `3` (default) | `scalar`

Driver preview distance, *L*, in m. Used to determine the preview
time window, *T\**.

#### Dependencies

To enable this parameter, Set **Lateral control type,
controlTypeLat** to `Predictive`.

#### Stanley

### **Vector input for poses** — Select to create `RefPose` and `CurrPose` input ports `off` (default) | `on`

Select this parameter to create the `RefPose` and
`CurrPose` input ports.

#### Dependencies

To enable this parameter, Set **Lateral control type,
controlTypeLat** to `Stanley`.

### **Include dynamics** — Select to include dynamics `off` (default) | `on`

The controller computes this command using the Stanley method, whose control law
is based on both a kinematic and dynamic bicycle model. To change between models,
use this parameter.

| Setting | Implementation |
| --- | --- |
| `off` | Controller uses a kinematic bicycle model that is suitable for path following in low-speed environments such as parking lots, where inertial effects are minimal. |
| `on` | Controller uses a dynamic bicycle model that is suitable for path following in high-speed environments such as highways, where inertial effects are more pronounced. |

#### Dependencies

To enable this parameter, Set **Lateral control type,
controlTypeLat** to `Stanley`.

### **Position gain of forward motion, PositionGainF** — Position gain of vehicle in forward motion `2.5` (default) | positive real scalar

Position gain of the vehicle when it is in forward motion, specified as a positive
scalar. This value determines how much the position error affects the steering
angle. Typical values are in the range [1, 5]. Increase this value to increase the
magnitude of the steering angle.

#### Dependencies

To enable this parameter, Set **Lateral control type,
controlTypeLat** to `Stanley`.

### **Position gain of reverse motion, PositionGainR** — Position gain of vehicle in reverse motion `2.5` (default) | positive real scalar

Position gain of the vehicle when it is in reverse motion, specified as a positive
scalar. This value determines how much the position error affects the steering
angle. Typical values are in the range [1, 5]. Increase this value to increase the
magnitude of the steering angle.

#### Dependencies

To enable this parameter, Set **Lateral control type,
controlTypeLat** to `Stanley`.

### **Yaw rate feedback gain, YawRateGain** — Yaw rate feedback gain `.2` (default) | nonnegative real scalar

Yaw rate feedback gain, specified as a nonnegative real scalar. This value
determines how much weight is given to the current yaw rate of the vehicle when the
block computes the steering angle command.

#### Dependencies

To enable this parameter, Set **Lateral control type,
controlTypeLat** to `Stanley` and select
**Include dynamics**.

### **Steering angle feedback gain, DelayGain** — Steering angle feedback gain `.2` (default) | nonnegative real scalar

Steering angle feedback gain, specified as a nonnegative real scalar. This value
determines how much the difference between the current steering angle command,
**SteerCmd**, and the current steering angle,
**CurrSteer**, affects the next steering angle command.

#### Dependencies

To enable this parameter, Set **Lateral control type,
controlTypeLat** to `Stanley` and select
**Include dynamics**.

#### Vehicle Parameters

### **Forward location of tire, a** — Along vehicle longitudinal axis `1.41` (default) | `scalar`

Forward location of tire, *a*, in m. Distance from
vehicle cg to forward tire location, along vehicle longitudinal
axis.

### **Rearward location of tire, b** — Along vehicle longitudinal axis `1.41` (default) | `scalar`

Rearward location of tire, *b*, in m. Absolute value
of distance from vehicle cg to rearward tire location, along vehicle
longitudinal axis.

### **Vehicle mass, m** — Mass `2016` (default) | `scalar`

Vehicle mass, *m*, in kg.

#### Dependencies

To enable this port, do either of these:

- Set **Lateral control type,
  controlTypeLat** to
  `Stanley` and select
  **Include dynamics**.
- Set **Lateral control type,
  controlTypeLat** to
  `Predictive`.

### **Front tire cornering coefficient, Cy\_f** — Coefficient `25266` (default) | `scalar`

Cornering stiffness coefficient, *CαF*, in N/rad.

#### Dependencies

To enable this port, do either of these:

- Set **Lateral control type,
  controlTypeLat** to
  `Stanley` and select
  **Include dynamics**.
- Set **Lateral control type,
  controlTypeLat** to
  `Predictive`.

### **Rear tire cornering coefficient, Cy\_r** — Coefficient `70933` (default) | `scalar`

Cornering stiffness coefficient, *CαR*, in N/rad.

#### Dependencies

To enable this port, set **Lateral control type,
controlTypeLat** to
`Predictive`.

### **Vehicle rotational inertia, I** — Inertia about yaw axis `4013` (default) | `scalar`

Vehicle rotational inertia, *I*, about the vehicle
yaw axis, in N·m·s^2.

#### Dependencies

To enable this parameter, Set **Lateral control type,
controlTypeLat** to
`Predictive`.

### **Nominal steering ratio, Ksteer** — Steering ratio `18` (default) | `scalar`

Steering ratio, *Ksteer*. The
value has no dimension.

#### Dependencies

To enable this parameter, select **Output handwheel
angle**.

### **Tire wheel angle limit, theta** — Angle limit `45*pi/180` (default) | `scalar`

Tire wheel angle limit, *θ*, in rad.

## Libraries

Vehicle Dynamics Blockset / Vehicle Scenarios / Driver

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Lateral path-tracking controller

The Lateral Driver block implements a control model to generate
normalized steering commands that track a lateral reference displacement. The normalized
steering commands can vary between -1 to 1. To model the dynamics, the block uses a
linear single track (bicycle) model. Use the Lateral Driver block to:

- Close the loop between a predefined path and actual vehicle motion.
- Generate steering commands that track predefined paths. You can connect
  the Lateral Driver block output to steering block
  inputs.

### Configurations

**External Actions**

Use the **External Actions** parameters to create input ports
for signals that can disable, hold, or override the closed-loop steering
command. The block uses this priority order for the input commands: disable
(highest), hold, override. The block uses this priority order for the input
commands: disable (highest), hold, override.

This table summarizes the external action parameters.

| Goal | External Action Parameter | Input Ports | Data Type |
| --- | --- | --- | --- |
| Override the steering command with an input steering command. | **Steering override** | `EnblSteerOvr` | `Boolean` |
| `SteerOvrCmd` | `double` |
| Hold the steering command at the current value. | **Steering hold** | `SteerHld` | `Boolean` |
| Disable the steering command. | **Steering disable** | `SteerZero` | `Boolean` |

Use the **Output handwheel angle** parameter to specify the units for the steering ports.

| Setting | Block Implementation | Port | |
| --- | --- | --- | --- |
| `off` (default) | Commanded steer angle, normalized from -1 through 1. The block uses the tire wheel angle saturation limit **Tire wheel angle limit, theta** parameter to normalize the command. | `SteerCmd` — Output | |
| Overrides the steering command with an input steering command normalized from -1 through 1. | `SteerOvrCmd` — Input | |
| `on` | Commanded steer angle, in units specified by **Angular units, angUnits**. | `SteerCmd` — Output | |
| Overrides the steering command with an input steering command, in units specified by **Angular units, angUnits**. | `SteerOvrCmd` — Input | |

Also, you can specify a tire wheel angle saturation limit using the
**Tire wheel angle limit, theta** parameter.

**Control Type and Units**

Use the **Lateral control type, controlTypeLat** parameter to specify the type of lateral control. The table specifies the block implementation.

| Setting | Block Implementation |
| --- | --- |
| `Predictive` (default) | Optimal single-point preview (look ahead) control model developed by C. C. MacAdam1, 2, 3. The model represents driver steering control behavior during path-following and obstacle avoidance maneuvers. Drivers preview (look ahead) to follow a predefined path. |
| `Stanley` | Controller that uses the Stanley4 method to minimize the position error and the angle error of the current pose with respect to the reference pose.  On the **Reference Control** pane, use the:  - **Vector input for poses** parameter to   input the to specify the input.  | Setting | Implementation |   | --- | --- |   | `off` (default) | Block uses the longitudinal, lateral, and yaw reference (`LongRef`, `LatRef`, `LatRef`) input ports and the feedback (`LongFdbk`, `LatFdbk`, `LatFdbk`) input ports for the reference and feedback pose. |   | `on` | Block uses input ports, `RefPose` and `CurrPose`, for the reference and feedback pose, respectively. | - **Include dynamics** parameter to specify   the type of model for the controller to use.  | Setting | Implementation |   | --- | --- |   | `off` (default) | Controller uses a kinematic bicycle model that is suitable for path following in low-speed environments such as parking lots, where inertial effects are minimal. |   | `on` | Controller uses a dynamic bicycle model that is suitable for path following in high-speed environments such as highways, where inertial effects are more pronounced. | |

Use the **Angular units,
angUnits** parameter to specify the angular units for the input and
output ports.

### Controller: Predictive Lateral Path-Tracking

If you set **Lateral control type, controlTypeLat** to
`Predictive`, the Lateral Driver block
implements an optimal single-point preview (look ahead) control model developed by C. C.
MacAdam1, 2, 3. The model represents driver steering control
behavior during path-following and obstacle avoidance maneuvers. Drivers preview (look
ahead) to follow a predefined path. To implement the MacAdam model, the block:

- Represents the dynamics as a linear single track (bicycle) vehicle
- Minimizes the previewed error signal at a single point T\* seconds ahead in
  time
- Accounts for the driver lag deriving from perceptual and neuromuscular
  mechanisms

This figure illustrates the block implementation of the single-point version of the driver model.

Block diagram illustrating implementation of single-point driver model

**Vehicle Dynamics**

For lateral and yaw motion, the block implements these linear dynamic equations.

y˙=v+Uψv˙=[−2(CαF+CαR)mU]v+[2(bCαR−aCαF)mU−U]r+(2CαFm)δFr˙=[2(bCαR−aCαF)IU]v+[−2(a2CαF+b2CαR)IU]r+(2aCαFI)δFψ˙=r

In matrix notation:

x˙=Fx+gδFwhere:x=[yvrψ]F=[010U0-2CαF+CαR mU2bCαR−aCαF mU−U002bCαR−aCαF IU-2a2CαF+b2CαR IU00010]x=[02CαFm2aCαFI0]

The single-point model assumes a minimum previewed error signal at a single point T\*
seconds ahead in time. a\* is the driver ability to predict the future vehicle response
based on the current steering control input. b\* is the driver ability to predict the
future vehicle response based on the current vehicle state. The block uses these equations.

a\*=T\*mT[I+∑n=1∞Fn(T\*)n(n+1)!]gb\*=mT[I+∑n=1∞Fn(T\*)nn!]where: mT=[1000]

The equations use these variables.

|  |  |
| --- | --- |
| *a*, *b* | Forward and rearward tire location, respectively |
| *m* | Vehicle mass |
| *I* | Vehicle rotational inertia |
| *CɑF* | Front tire cornering coefficient |
| *CɑR* | Rear tire cornering coefficient |
| *a\**, ***b**\** | Driver prediction scalar and vector gain, respectively |
| ***x*** | Predicted vehicle state vector |
| *v* | Lateral velocity |
| *r* | Yaw rate |
| *Ψ* | Front wheel heading angle |
| *y* | Lateral displacement |
| ***F*** | System matrix |
| *δ*, *δF* | Steer angle and front axle steer angle, respectively |
| ***g*** | Control coefficient vector |
| *U* | Forward (longitudinal) vehicle velocity |
| *T\** | Preview time window |
| *ƒ(t+T\*)* | Previewed path input T\* seconds ahead |
| *U* | Forward vehicle velocity |
| ***mT*** | Constant observer vector; provides vehicle lateral position |

**Optimization**

The single-point model implemented by the block finds the steering command that minimizes a local performance index, *J*, over the current preview interval, (*t*, *t+T*).

J=1T∫tt+T[f(η)−y(η)]2dη

To minimize *J* with respect to the steering command, this condition must be met.

dJdu=0

You can express the optimal control solution in terms of a current non-optimal and
corresponding nonzero preview output error *T\** seconds
ahead1, 2, 3.

uo(t)=u(t)+e(t+T\*)a\*

The block uses the preview distance and vehicle longitudinal velocity to determine the
preview time window.

T\*=LU

The equations use these variables.

|  |  |
| --- | --- |
| *T\** | Preview time window |
| *ƒ(t+T\*)* | Previewed path input *T\** sec ahead |
| *y(t+T\*)* | Previewed plant output *T\** sec ahead |
| *e(t+T\*)* | Previewed error signal *T\** sec ahead |
| *u(t)*, *uo(t)* | Steer angle and optimal steer angle, respectively |
| *L* | Preview distance |
| *J* | Performance index |
| *U* | Forward (longitudinal) vehicle velocity |

**Driver Lag**

The single-point model implemented by the block introduces a driver lag. The driver lag accounts for the delay when the driver is tracking tasks. Specifically, it is the transport delay deriving from perceptual and neuromuscular mechanisms. To calculate the driver transport delay, the block implements this equation.

H(s)=e−sτ

The equations use these variables.

|  |  |
| --- | --- |
| *τ* | Driver transport delay |
| *y(t+T\*)* | Previewed plant output *T\** sec ahead |
| *e(t+T\*)* | Previewed error signal *T\** sec ahead |
| *u(t)*, *uo(t)* | Steer angle and optimal steer angle, respectively |
| *J* | Performance index |

### Controller: Stanley Lateral Path-Tracking

If you set **Lateral control type, controlTypeLat** to
`Stanley`, the block implements the Stanley
method4. To compute the steering angle command, the Stanley
controller minimizes the position error and the angle error of the current pose with respect
to the reference pose. The driving direction of the vehicle determines these error
values.

To compute the steering angle command, the controller minimizes the position error and the
angle error of the current pose with respect to the reference pose.

- The *position error* is the lateral distance from the
  vehicle center-of-gravity (CG) to the reference point on the path.
- The *angle error* is the angle of the vehicle with
  respect to reference path.
