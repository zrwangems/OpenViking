---
type: simulink-block
title: 'Predictive Driver'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / Driver'
documentation_page: 'predictivedriver'
documentation_source_path: 'ref/predictivedriver.html'
language: en
---

# Predictive Driver

## Ports

### Input

### **VelRef** — Reference vehicle velocity `scalar`

Reference velocity, *vref*, in
units specified by **Longitudinal velocity units,
velUnits**.

### **LongRef** — Longitudinal displacement reference `scalar`

Longitudinal center of mass (CM) displacement reference, in the
inertial reference frame, in m.

#### Dependencies

To enable this port:

1. Set **Lateral control type,
   controlTypeLat** to
   `Stanley`.
2. Clear **Vector input for
   poses**.

### **LatRef** — Lateral displacement reference `scalar`

Lateral center of mass (CM) displacement reference, in the inertial
reference frame, in m.

#### Dependencies

To enable this port, do one of these:

- Set **Lateral control type,
  controlTypeLat** to
  `Stanley` and clear
  **Vector input for poses**.
- Set **Lateral control type,
  controlTypeLat** to
  `Predictive`.

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

### **EnblAccelOvr** — Enable acceleration command override `scalar`

Enable acceleration command override.

#### Dependencies

To enable this port, select **Acceleration override**.

**Data Types:** `Boolean`

### **AccelOvrCmd** — Acceleration override command `scalar`

Acceleration override command, normalized from 0 through 1.

#### Dependencies

To enable this port, select **Acceleration override**.

**Data Types:** `double`

### **AccelHld** — Acceleration hold `scalar`

Boolean signal that holds the acceleration command at the current value.

#### Dependencies

To enable this port, select **Acceleration hold**.

**Data Types:** `Boolean`

### **AccelZero** — Disable acceleration command `scalar`

Disable acceleration command.

#### Dependencies

To enable this port, select **Acceleration disable**.

**Data Types:** `Boolean`

### **EnblDecelOvr** — Enable deceleration command override `scalar`

Enable deceleration command override.

#### Dependencies

To enable this port, select **Deceleration override**.

**Data Types:** `Boolean`

### **DecelOvrCmd** — Deceleration override command `scalar`

Deceleration override command, normalized from 0 through 1.

#### Dependencies

To enable this port, select **Deceleration override**.

**Data Types:** `double`

### **DecelHld** — Deceleration hold `scalar`

Boolean signal that holds the deceleration command at the current value.

#### Dependencies

To enable this port, select **Deceleration hold**.

**Data Types:** `Boolean`

### **DecelZero** — Disable deceleration command `scalar`

Disable deceleration command.

#### Dependencies

To enable this port, select **Deceleration disable**.

**Data Types:** `Boolean`

### **ExtGear** — Gear `scalar`

| Gear | Integer |
| --- | --- |
| Park | `80` |
| Reverse | `-1` |
| Neutral | `0` |
| Drive | `1` |
| Gear | `Gear number` |

#### Dependencies

To enable this port, set **Shift type, shftType**
to `External`.

### **Grade** — Road grade angle `scalar`

Road grade angle, *γ*, in deg.

### **Curvature** — Path curvature scalar

Path curvature defined as the rate of change of the tangent angle with
respect to the arc length of the path, *Κ*, in 1/m.

#### Dependencies

To enable this port:

1. Set **Lateral control type,
   controlTypeLat** to
   `Stanley`.
2. Select **Include dynamics**.

### **RefPose** — Reference pose [*Xref*, *Yref*, *φref*] vector

Reference pose, specified as an
[*Xref*,
*Yref*,
*φref*] vector.
*Xref* and
*Yref* are in meters,
and *φref* are in units
specified by **Angular units, angUnits**.

*Xref* and
*Yref* specify the
reference point to steer the vehicle toward.

*φref* specifies the
orientation angle of the path at this reference point and is positive in
the clockwise direction.

The reference point is the point on the path that is closest to the
vehicle CG. You can use the either the Z-up or Z-down vehicle coordinate
system, as long you use the same coordinate system (Z-up or Z-down) for
block inputs and parameters.

Figure indicating location of x, y, and psi on vehicle path

#### Dependencies

To enable this port:

1. Set **Lateral control type,
   controlTypeLat** to
   `Stanley`.
2. Select **Vector input for
   poses**.

**Data Types:** `single` | `double`

### **VelFdbk** — Longitudinal vehicle velocity `scalar`

Longitudinal vehicle velocity, *U*, in the
vehicle-fixed frame, in units specified by **Longitudinal
velocity units, velUnits**.

### **CurrPose** — Current pose [*Xcurr*, *Ycurr*, *φcurr*] vector

Current pose of the vehicle, specified as an
[*Xcurr*,
*Ycurr*,
*φcurr*] vector.
*Xcurr* and
*Ycurr* are in meters,
and *φcurr* is in units
specified by **Angular units, angUnits**.

*Xcurr* and
*Ycurr* specify the
location of the vehicle, which is defined as the vehicle CG.

*φcurr* specifies the
orientation angle of the vehicle location at
(*Xcurr*,
*Ycurr*) and is positive
in the clockwise direction.

You can use the either the Z-up or Z-down vehicle coordinate system,
as long you use the same coordinate system (Z-up or Z-down) for block
inputs and parameters.

Figure indicating location of x, y, and psi on vehicle path

#### Dependencies

To enable this port:

1. Set **Lateral control type,
   controlTypeLat** to
   `Stanley`.
2. Select **Vector input for
   poses**.

**Data Types:** `single` | `double`

### **LatFdbk** — Lateral displacement `scalar`

Lateral CM displacement, *yo*,
in the inertial reference frame, in m.

#### Dependencies

To enable this port, do either of these:

- Set **Lateral control type,
  controlTypeLat** to
  `Stanley` and clear
  **Vector input for poses**.
- Set **Lateral control type,
  controlTypeLat** to
  `Predictive`.

### **LatVelFdbk** — Lateral vehicle velocity `scalar`

Lateral vehicle velocity, *vo*
, in the vehicle-fixed frame, in m/s.

#### Dependencies

To enable this port, Set **Lateral control type,
controlTypeLat** to
`Predictive`.

### **YawFdbk** — Vehicle yaw angle `scalar`

Vehicle yaw angle, *Ψo*, in
the inertial reference frame, in units specified by **Angular
units, angUnits**.

#### Dependencies

To enable this port, do either of these:

- Set **Lateral control type,
  controlTypeLat** to
  `Stanley` and clear
  **Vector input for poses**.
- Set **Lateral control type,
  controlTypeLat** to
  `Predictive`.

### **YawVelFdbk** — Yaw rate `scalar`

Yaw rate, *ro*, in the
vehicle-fixed frame, in units specified by **Angular units,
angUnits** per sec.

#### Dependencies

To enable this port, Set **Lateral control type,
controlTypeLat** to
`Predictive`.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Variable | Description |
| --- | --- | --- | --- | --- |
| `Steer` | | | *δF* | Commanded steer angle, normalized from 0 through 1 |
| `Accel` | | | *yacc* | Commanded vehicle acceleration, normalized from 0 through 1 |
| `Decel` | | | *ydec* | Commanded vehicle deceleration, normalized from 0 through 1 |
| `Gear` | | | | Integer value of commanded gear |
| `Clutch` | | | | Clutch command |
| `Err` | `LatErr` | `Err` | *eref* | Difference in reference vehicle position and vehicle position. |
| `ErrSqrSum` | ∫0teref2dt | Integrated square of error. |
| `ErrMax` | max(eref(t)) | Maximum error during simulation. |
| `ErrMin` | min(eref(t)) | Minimum error during simulation. |
| `LngErr` | `Err` | *eref* | Difference in reference vehicle speed and vehicle speed |
| `ErrSqrSum` | ∫0teref2dt | Integrated square of error |
| `ErrMax` | max(eref(t)) | Maximum error during simulation |
| `ErrMin` | min(eref(t)) | Minimum error during simulation |
| `ExtActions` | `EnblSteerOvr` | | | Override the steering command with an input deceleration command |
| `SteerOvrCmd` | | | Input steering override command |
| `SteerHld` | | | Hold the steering command at the current value |
| `SteerZero` | | | Disable the steering command |
| `EnblAccelOvr` | | | Override the accelerator command with an input acceleration command |
| `AccelOvrCmd` | | | Input accelerator override command |
| `AccelHld` | | | Hold the acceleration command at the current value |
| `AccelZero` | | | Disable the acceleration command |
| `EnblDecelOvr` | | | Override the decelerator command with an input deceleration command |
| `DecelOvrCmd` | | | Input deceleration override command |
| `DecelHld` | | | Hold the decelerator command at current value |
| `DecelZero` | | | Disable the decelerator command |

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

### **AccelCmd** — Commanded vehicle acceleration `scalar`

Commanded vehicle acceleration,
*yacc*, normalized from 0
through 1.

### **DecelCmd** — Commanded vehicle deceleration `scalar`

Commanded vehicle deceleration,
*ydec*, normalized from 0
through 1.

### **GearCmd** — Commanded vehicle gear `scalar`

Integer value of commanded vehicle gear.

| Gear | Integer |
| --- | --- |
| Park | `80` |
| Reverse | `-1` |
| Neutral | `0` |
| Drive | `1` |
| Gear | `Gear number` |

#### Dependencies

To enable this port, select **Output gear signal**.

## Parameters

### Configuration

#### External Actions

### **Accelerator override** — Override acceleration command `off` (default) | `on`

Select to override the acceleration command with an input acceleration
command.

#### Dependencies

Selecting this parameter creates the `EnblAccelOvr` and
`AccelOvrCmd` input ports.

### **Accelerator hold** — Hold acceleration command `off` (default) | `on`

Select to hold the acceleration command.

#### Dependencies

Selecting this parameter creates the `AccelHld` input
port.

### **Accelerator disable** — Disable acceleration command `off` (default) | `on`

Select to disable the acceleration command.

#### Dependencies

Selecting this parameter creates the `AccelZero` input
port.

### **Decelerator override** — Override deceleration command `off` (default) | `on`

Select to override the deceleration command with an input deceleration
command.

#### Dependencies

Selecting this parameter creates the `EnblDecelOvr` and
`DecelOvrCmd` input ports.

### **Decelerator hold** — Hold deceleration command `off` (default) | `on`

Select to hold the deceleration command.

#### Dependencies

Selecting this parameter creates the `DecelHld` input
port.

### **Decelerator disable** — Disable deceleration command `off` (default) | `on`

Select to disable the deceleration command.

#### Dependencies

Selecting this parameter creates the `DecelZero` input
port.

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

#### Control and Shift

### **Longitudinal control type, cntrlType** — Longitudinal control `PI` (default) | `Scheduled PI` | `Predictive`

Type of longitudinal control.

| Setting | Block Implementation |
| --- | --- |
| `PI` | Proportional-integral (PI) control with tracking windup and feed-forward gains. |
| `Scheduled PI` | PI control with tracking windup and feed-forward gains that are a function of vehicle velocity. |
| `Predictive` | Optimal single-point preview (look ahead) control model developed by C. C. MacAdam1, 2, 3. The model represents driver steering control behavior during path-following and obstacle avoidance maneuvers. Drivers preview (look ahead) to follow a predefined path. To implement the MacAdam model, the block:  - Represents the dynamics as a linear single track (bicycle)   vehicle - Minimizes the previewed error signal at a single point   *T\** seconds ahead in time - Accounts for the driver lag deriving from perceptual and   neuromuscular mechanisms |

### **Lateral control type, controlTypeLat** — Controller `Predictive` (default) | `Stanley`

Use the **Lateral control type, controlTypeLat** parameter to specify the type of lateral control. The table specifies the block implementation.

| Setting | Block Implementation |
| --- | --- |
| `Predictive` (default) | Optimal single-point preview (look ahead) control model developed by C. C. MacAdam1, 2, 3. The model represents driver steering control behavior during path-following and obstacle avoidance maneuvers. Drivers preview (look ahead) to follow a predefined path. |
| `Stanley` | Controller that uses the Stanley4 method to minimize the position error and the angle error of the current pose with respect to the reference pose.  On the **Reference Control** pane, use the:  - **Vector input for poses** parameter to   input the to specify the input.  | Setting | Implementation |   | --- | --- |   | `off` (default) | Block uses the longitudinal, lateral, and yaw reference (`LongRef`, `LatRef`, `LatRef`) input ports and the feedback (`LongFdbk`, `LatFdbk`, `LatFdbk`) input ports for the reference and feedback pose. |   | `on` | Block uses input ports, `RefPose` and `CurrPose`, for the reference and feedback pose, respectively. | - **Include dynamics** parameter to specify   the type of model for the controller to use.  | Setting | Implementation |   | --- | --- |   | `off` (default) | Controller uses a kinematic bicycle model that is suitable for path following in low-speed environments such as parking lots, where inertial effects are minimal. |   | `on` | Controller uses a dynamic bicycle model that is suitable for path following in high-speed environments such as highways, where inertial effects are more pronounced. | |

### **Shift type, shftType** — Shift type `None` (default) | `Reverse, Neutral, Drive` | `Scheduled` | `External`

Shift type.

| Setting | Block Implementation |
| --- | --- |
| `None` | No transmission. Block outputs a constant gear of 1.  Use this setting to minimize the number of parameters you need to generate acceleration and braking commands to track forward vehicle motion. This setting does not allow reverse vehicle motion. |
| `Reverse, Neutral, Drive` | Block uses a Stateflow chart to model reverse, neutral, and drive gear shift scheduling.  Use this setting to generate acceleration and braking commands to track forward and reverse vehicle motion using simple reverse, neutral, and drive gear shift scheduling. Depending on the vehicle state and vehicle velocity feedback, the block uses the initial gear and time required to shift to shift the vehicle up into drive or down into reverse or neutral.  For neutral gears, the block uses braking commands to control the vehicle speed. For reverse gears, the block uses an acceleration command to generate torque and a brake command to reduce vehicle speed. |
| `Scheduled` | Block uses a Stateflow chart to model reverse, neutral, park, and N-speed gear shift scheduling.  Use this setting to generate acceleration and braking commands to track forward and reverse vehicle motion using reverse, neutral, park, and N-speed gear shift scheduling. Depending on the vehicle state and vehicle velocity feedback, the block uses these parameters to determine the:  - Initial gear - Upshift and downshift accelerator pedal positions - Upshift and downshift velocity - Timing for shifting and engaging forward and reverse from   neutral    For neutral gears, the block uses braking commands to control the vehicle speed. For reverse gears, the block uses an acceleration command to generate torque and a brake command to reduce vehicle speed. |
| `External` | Block uses the input gear, vehicle state, and velocity feedback to generate acceleration and braking commands to track forward and reverse vehicle motion.  For neutral gears, the block uses braking commands to control the vehicle speed. For reverse gears, the block uses an acceleration command to generate torque and a brake command to reduce vehicle speed. |

### **Longitudinal velocity units, velUnits** — Velocity units `m/s` (default)

Vehicle velocity reference and feedback units.

#### Dependencies

If you set **Longitudinal control type,
CntrlType** control type to
`Scheduled` or `Scheduled
PI`, the block uses the **Longitudinal
velocity units, velUnits** for the **Nominal
speed, vnom** parameter dimension.

If you set **Shift Type, shftType** to
`Scheduled`, the block uses the
**Longitudinal velocity units, velUnits** for
these parameter dimensions:

- **Upshift velocity data table,
  upShftTbl**
- **Downshift velocity data table,
  dwnShftTbl**

### **Angular units, angUnits** — Yaw, steering, and pose angle units `rad` (default) | `deg`

Units for yaw, steering, and pose angle input and output ports.

### **Output gear signal** — Create `GearCmd` output port `off` (default) | `on`

Specify to create output port `GearCmd`.

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

### Reference Control

#### Longitudinal

### **Proportional gain, Kp** — Gain `10` (default) | `scalar`

Proportional gain, *Kp*,
dimensionless.

#### Dependencies

To create this parameter, set **Control type** to
`PI`.

### **Integral gain, Ki** — Gain `5` (default) | `scalar`

Proportional gain, *Ki*,
dimensionless.

#### Dependencies

To create this parameter, set **Control type** to
`PI`.

### **Velocity feed-forward, Kff** — Gain `.1` (default) | `scalar`

Velocity feed-forward gain, *Kff*,
dimensionless.

#### Dependencies

To create this parameter, set **Control type** to
`PI`.

### **Grade angle feed-forward, Kg** — Gain `0` (default) | `scalar`

Grade angle feed-forward gain, *Kg*, in
1/deg.

#### Dependencies

To create this parameter, set **Control type** to
`PI`.

### **Velocity gain breakpoints, VehVelVec** — Breakpoints `[0 100]` (default) | `vector`

Velocity gain breakpoints, *VehVelVec*, dimensionless.

#### Dependencies

To create this parameter, set **Control type** to `Scheduled
PI`.

### **Velocity feed-forward gain values, KffVec** — Gain `[.1 .1]` (default) | `vector`

Velocity feed-forward gain values, *KffVec*, as a function of
vehicle velocity, dimensionless.

#### Dependencies

To create this parameter, set **Control type** to `Scheduled
PI`.

### **Proportional gain values, KpVec** — Gain `[10 10]` (default) | `vector`

Proportional gain values, *KpVec*, as a function of vehicle
velocity, dimensionless.

#### Dependencies

To create this parameter, set **Control type** to `Scheduled
PI`.

### **Integral gain values, KiVec** — Gain `[5 5]` (default) | `vector`

Integral gain values, *KiVec*, as a function of vehicle velocity,
dimensionless.

#### Dependencies

To create this parameter, set **Control type** to `Scheduled
PI`.

### **Grade angle feed-forward values, KgVec** — Grade gain `[0 0]` (default) | `vector`

Grade angle feed-forward values, *KgVec*, as a function of
vehicle velocity, in 1/deg.

#### Dependencies

To create this parameter, set **Control type** to `Scheduled
PI`.

### **Nominal speed, vnom** — Nominal vehicle speed `5` (default) | `scalar`

Nominal vehicle speed, *vnom*, in units
specified by the **Reference and feedback units, velUnits**
parameter. The block uses the nominal speed to normalize the controller
gains.

#### Dependencies

To create this parameter, set **Control type** to
`PI` or `Scheduled PI`.

### **Anti-windup, Kaw** — Gain `1` (default) | `scalar`

Anti-windup gain, *Kaw*,
dimensionless.

#### Dependencies

To create this parameter, set **Control type** to
`PI` or `Scheduled PI`.

### **Error filter time constant, tauerr** — Filter `.01` (default) | `scalar`

Error filter time constant, *τerr*, in s.
To disable the filter, enter 0.

#### Dependencies

To create this parameter, set **Control type** to
`PI` or `Scheduled PI`.

#### Predictive

### **Driver response time, tau** — Response time `0.1` (default) | `scalar`

Driver response time, *τ*, in s.

#### Dependencies

To enable this parameter, Set **Longitudinal control type,
cntrlType** or **Lateral control type,
controlTypeLat** to
`Predictive`.

### **Preview distance, L** — Distance `3` (default) | `scalar`

Driver preview distance, *L*, in m. Used to determine
the preview time window,
*T\**.

#### Dependencies

To enable this parameter, Set **Longitudinal control type,
cntrlType** or **Lateral control type,
controlTypeLat** to
`Predictive`.

### **Effective vehicle total tractive force, Kpt** — Tractive force `3000` (default) | `scalar`

Effective vehicle total tractive force,
*Kpt*, in
N.

#### Dependencies

To create this parameter, set **Longitudinal control type, cntrlType** to
`Predictive`.

### **Rolling resistance coefficient, aR** — Resistance `200` (default) | `scalar`

Static rolling and driveline resistance coefficient,
*aR*, in N. Block uses the parameter to
estimate the constant acceleration or braking effort.

#### Dependencies

To create this parameter, set **Longitudinal control type, cntrlType** to
`Predictive`.

### **Rolling and driveline resistance coefficient, bR** — Resistance `2.5` (default) | `scalar`

Rolling and driveline resistance coefficient,
*bR*, in
N·s/m. Block uses the parameter to estimate the linear
velocity-dependent acceleration or braking effort.

#### Dependencies

To create this parameter, set **Longitudinal control type, cntrlType** to
`Predictive`.

### **Aerodynamic drag coefficient, cR** — Drag `.5` (default) | `scalar`

Aerodynamic drag coefficient,
*cR*, in
N·s^2/m^2. Block uses the parameter to estimate the quadratic
velocity-dependent acceleration or braking effort.

#### Dependencies

To create this parameter, set **Longitudinal control type, cntrlType** to
`Predictive`.

### **Gravitational constant, g** — Gravitational constant `9.81` (default) | `scalar`

Gravitational constant, g, in m/s^2.

#### Dependencies

To create this parameter, set **Longitudinal control type, cntrlType** to
`Predictive`.

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

### Vehicle Parameters

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

### Shift

#### Reverse, Neutral, Drive

### **Initial gear, GearInit** — Initial gear `0` (default) | `scalar`

Integer value of the initial gear. The block uses the initial gear to generate
acceleration and braking commands to track forward and reverse vehicle
motion.

| Gear | Integer |
| --- | --- |
| Park | `80` |
| Reverse | `-1` |
| Neutral | `0` |
| Drive | `1` |
| Gear | `Gear number` |

#### Dependencies

To create this parameter, set **Shift type, shftType** to
`Reverse, Neutral, Drive` or
`Scheduled`. If you specify
`Reverse, Neutral, Drive`, the
**Initial Gear, GearInit** parameter value can be only
`-1`, `0`, or
`1`.

### **Time required to shift, tShift** — Time `.1` (default) | `scalar`

Time required to shift, *tShift*, in s. The block uses the
time required to shift to generate acceleration and braking commands to track
forward and reverse vehicle motion using reverse, neutral, and drive gear shift
scheduling.

#### Dependencies

To create this parameter, set **Shift type, shftType** to
`Reverse, Neutral, Drive`.

#### Scheduled

### **Initial gear, GearInit** — Initial gear `0` (default) | `scalar`

Integer value of the initial gear. The block uses the initial gear to generate
acceleration and braking commands to track forward and reverse vehicle
motion.

| Gear | Integer |
| --- | --- |
| Park | `80` |
| Reverse | `-1` |
| Neutral | `0` |
| Drive | `1` |
| Gear | `Gear number` |

#### Dependencies

To create this parameter, set **Shift type, shftType** to
`Reverse, Neutral, Drive` or
`Scheduled`. If you specify `Reverse,
Neutral, Drive`, the **Initial Gear, GearInit**
parameter value can be only `-1`, `0`, or
`1`.

### **Up and down shift accelerator pedal positions, pdlVec** — Pedal position breakpoints `[0.1 0.4 0.5 0.9]` (default) | `[1-by-m] vector`

Pedal position breakpoints for lookup tables when calculating upshift and
downshift velocities, dimensionless. Vector dimensions are 1 by the number of
pedal position breakpoints, `m`.

#### Dependencies

To create this parameter, set **Shift type, shftType** to
`Scheduled`.

### **Upshift velocity data table, upShftTbl** — Table `[m-by-n] array`

Upshift velocity data as a function of pedal position and gear, in units
specified by the **Reference and feedback units, velUnits**
parameter. Upshift velocities indicate the vehicle velocity at which the gear
should increase by 1.

The array dimensions are `m` pedal positions by
`n` gears. The first column of data, when
`n` equals 1, is the upshift velocity for the neutral
gear.

#### Dependencies

To create this parameter, set **Shift type, shftType** to
`Scheduled`.

### **Downshift velocity data table, dwnShftTbl** — Table `[m-by-n] array`

Downshift velocity data as a function of pedal position and gear, in units
specified by the **Reference and feedback units, velUnits**
parameter. Downshift velocities indicate the vehicle velocity at which the gear
should decrease by 1.

The array dimensions are `m` pedal positions by
`n` gears. The first column of data, when
`n` equals 1, is the downshift velocity for the neutral
gear.

#### Dependencies

To create this parameter, set **Shift type, shftType** to
`Scheduled`.

### **Time required to shift, tClutch** — Time `.5` (default) | `scalar`

Time required to shift, *tClutch*, in
s.

#### Dependencies

To create this parameter, set **Shift type, shftType** to
`Scheduled`.

### **Time required to engage reverse from neutral, tRev** — Time `.5` (default) | `scalar`

Time required to engage reverse from neutral,
*tRev*, in s.

#### Dependencies

To create this parameter, set **Shift type, shftType** to
`Scheduled`.

### **Time required to engage park from neutral, tPark** — Time `120` (default) | `scalar`

Time required to engage park from neutral,
*tPark*, in s.

#### Dependencies

To create this parameter, set **Shift type, shftType** to
`Scheduled`.

## Libraries

Vehicle Dynamics Blockset / Vehicle Scenarios / Driver

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Predictive driver controller to track longitudinal speed and lateral path

The Predictive Driver block implements a controller that generates
normalized steering, acceleration, and braking commands to track longitudinal velocity
and a lateral reference displacement. The normalized commands can vary between -1 to 1.
The controller uses a single-track (bicycle) model for optimal single-point preview
control.

### Configurations

**External Actions**

Use the **External Actions** parameters to create input ports
for signals that you can use to simulate standard test maneuvers. The block uses
this priority order for the input commands: disable (highest), hold,
override.

This table summarizes the external action parameters.

| Goal | External Action Parameter | Input Ports | Data Type |
| --- | --- | --- | --- |
| Override the accelerator command with an input acceleration command. | **Accelerator override** | `EnablAccelOvr` | `Boolean` |
| `AccelOvrCmd` | `double` |
| Hold the acceleration command at the current value. | **Accelerator hold** | `AccelHld` | `Boolean` |
| Disable the acceleration command. | **Accelerator disable** | `AccelZero` | `Boolean` |
| Override the decelerator command with an input deceleration command. | **Decelerator override** | `EnablDecelOvr` | `Boolean` |
| `DecelOvrCmd` | `double` |
| Hold the decelerator command at current value. | **Decelerator hold** | `DecelHld` | `Boolean` |
| Disable the decelerator command. | **Decelerator disable** | `DecelZero` | `Boolean` |
| Override the steering command with an input steering command. | **Steering override** | `EnblSteerOvr` | `Boolean` |
| `SteerOvrCmd` | `double` |
| Hold the steering command at the current value. | **Steering hold** | `SteerHld` | `Boolean` |
| Disable the steering command. | **Steering disable** | `SteerZero` | `Boolean` |

**Controllers**

Use the **Longitudinal control type, cntrlType** parameter to
specify one of these control options.

| Setting | Block Implementation |
| --- | --- |
| `PI` | Proportional-integral (PI) control with tracking windup and feed-forward gains. |
| `Scheduled PI` | PI control with tracking windup and feed-forward gains that are a function of vehicle velocity. |
| `Predictive` | Optimal single-point preview (look ahead) control model developed by C. C. MacAdam1, 2, 3. The model represents driver steering control behavior during path-following and obstacle avoidance maneuvers. Drivers preview (look ahead) to follow a predefined path. To implement the MacAdam model, the block:  - Represents the dynamics as a linear single track (bicycle)   vehicle - Minimizes the previewed error signal at a single point   *T\** seconds ahead in time - Accounts for the driver lag deriving from perceptual and   neuromuscular mechanisms |

Use the **Lateral control type, controlTypeLat** parameter to specify the type of lateral control. The table specifies the block implementation.

| Setting | Block Implementation |
| --- | --- |
| `Predictive` (default) | Optimal single-point preview (look ahead) control model developed by C. C. MacAdam1, 2, 3. The model represents driver steering control behavior during path-following and obstacle avoidance maneuvers. Drivers preview (look ahead) to follow a predefined path. |
| `Stanley` | Controller that uses the Stanley4 method to minimize the position error and the angle error of the current pose with respect to the reference pose.  On the **Reference Control** pane, use the:  - **Vector input for poses** parameter to   input the to specify the input.  | Setting | Implementation |   | --- | --- |   | `off` (default) | Block uses the longitudinal, lateral, and yaw reference (`LongRef`, `LatRef`, `LatRef`) input ports and the feedback (`LongFdbk`, `LatFdbk`, `LatFdbk`) input ports for the reference and feedback pose. |   | `on` | Block uses input ports, `RefPose` and `CurrPose`, for the reference and feedback pose, respectively. | - **Include dynamics** parameter to specify   the type of model for the controller to use.  | Setting | Implementation |   | --- | --- |   | `off` (default) | Controller uses a kinematic bicycle model that is suitable for path following in low-speed environments such as parking lots, where inertial effects are minimal. |   | `on` | Controller uses a dynamic bicycle model that is suitable for path following in high-speed environments such as highways, where inertial effects are more pronounced. | |

**Shift**

Use the **Shift type, ShftType** parameter to specify one of
these shift options.

| Setting | Block Implementation |
| --- | --- |
| `None` | No transmission. Block outputs a constant gear of 1.  Use this setting to minimize the number of parameters you need to generate acceleration and braking commands to track forward vehicle motion. This setting does not allow reverse vehicle motion. |
| `Reverse, Neutral, Drive` | Block uses a Stateflow® chart to model reverse, neutral, and drive gear shift scheduling.  Use this setting to generate acceleration and braking commands to track forward and reverse vehicle motion using simple reverse, neutral, and drive gear shift scheduling. Depending on the vehicle state and vehicle velocity feedback, the block uses the initial gear and time required to shift to shift the vehicle up into drive or down into reverse or neutral.  For neutral gears, the block uses braking commands to control the vehicle speed. For reverse gears, the block uses an acceleration command to generate torque and a brake command to reduce vehicle speed. |
| `Scheduled` | Block uses a Stateflow chart to model reverse, neutral, park, and N-speed gear shift scheduling.  Use this setting to generate acceleration and braking commands to track forward and reverse vehicle motion using reverse, neutral, park, and N-speed gear shift scheduling. Depending on the vehicle state and vehicle velocity feedback, the block uses these parameters to determine the:  - Initial gear - Upshift and downshift accelerator pedal positions - Upshift and downshift velocity - Timing for shifting and engaging forward and reverse from   neutral    For neutral gears, the block uses braking commands to control the vehicle speed. For reverse gears, the block uses an acceleration command to generate torque and a brake command to reduce vehicle speed. |
| `External` | Block uses the input gear, vehicle state, and velocity feedback to generate acceleration and braking commands to track forward and reverse vehicle motion.  For neutral gears, the block uses braking commands to control the vehicle speed. For reverse gears, the block uses an acceleration command to generate torque and a brake command to reduce vehicle speed. |

**Units**

Use the **Longitudinal velocity
units, velUnits** parameter to specify units for longitudinal
velocity input ports.

Use the **Angular units,
angUnits** parameter to specify units for yaw, steering, and pose
angle input and output ports.

**Gear Signal**

Use the **Output gear signal** parameter to create the
`GearCmd` output port. The `GearCmd`
signal contains the integer value of the commanded vehicle gear.

| Gear | Integer |
| --- | --- |
| Park | `80` |
| Reverse | `-1` |
| Neutral | `0` |
| Drive | `1` |
| Gear | `Gear number` |

**Output Handwheel Angle**

Use the **Output handwheel angle** parameter to specify the units for the steering ports.

| Setting | Block Implementation | Port | |
| --- | --- | --- | --- |
| `off` (default) | Commanded steer angle, normalized from -1 through 1. The block uses the tire wheel angle saturation limit **Tire wheel angle limit, theta** parameter to normalize the command. | `SteerCmd` — Output | |
| Overrides the steering command with an input steering command normalized from -1 through 1. | `SteerOvrCmd` — Input | |
| `on` | Commanded steer angle, in units specified by **Angular units, angUnits**. | `SteerCmd` — Output | |
| Overrides the steering command with an input steering command, in units specified by **Angular units, angUnits**. | `SteerOvrCmd` — Input | |

### Controller: PI Speed-Tracking

If you set the control type to `PI` or `Scheduled
PI`, the block implements proportional-integral (PI) control with tracking
windup and feedforward gains. For the `Scheduled PI` configuration,
the block uses feed forward gains that are a function of vehicle velocity.

To calculate the speed control output, the block uses these equations.

| Setting | Equation |
| --- | --- |
| `PI` | y=Kffvnomvref+Kperefvnom+∫(Kierefvnom+Kaweout)dt+Kgγ |
| `Scheduled PI` | y=Kff(v)vnomvref+Kp(v)erefvnom+∫(Ki(v)erefvnom+Kaweout)dt+Kg(v)γ |

where:eref=vref−veout=ysat−yysat={−1y<−1y−1≤y≤111<y

The velocity error low-pass filter uses this transfer function.

H(s)=1τerrs+1   for   τerr>0

To calculate the acceleration and braking commands, the block uses these equations.

yacc={0ysat<0ysat0≤ysat≤111<ysatydec={0ysat>0−ysat−1≤ysat≤01ysat<−1

The equations use these variables.

|  |  |
| --- | --- |
| *vnom* | Nominal vehicle speed |
| *Kp* | Proportional gain |
| *Ki* | Integral gain |
| *Kaw* | Anti-windup gain |
| *Kff* | Velocity feedforward gain |
| *Kg* | Grade angle feedforward gain |
| *γ* | Grade angle |
| *τerr* | Error filter time constant |
| *y* | Nominal control output magnitude |
| *ysat* | Saturated control output magnitude |
| *eref* | Velocity error |
| *eout* | Difference between saturated and nominal control outputs |
| *yacc* | Acceleration signal |
| *ydec* | Braking signal |
| *v* | Velocity feedback signal |
| *vref* | Reference velocity signal |

### Controller: Predictive Speed-Tracking

If you set the **Longitudinal control type, cntrlType** or
**Lateral control type, cntrlType** to
`Predictive`, the block implements an optimal
single-point preview (look ahead) control model developed by C. C.
MacAdam[1], [2], [3]. The model represents driver steering control behavior during
path-following and obstacle avoidance maneuvers. Drivers preview (look ahead) to
follow a predefined path. To implement the MacAdam model, the block:

- Represents the dynamics as a linear single track (bicycle)
  vehicle
- Minimizes the previewed error signal at a single point
  *T\** seconds ahead in time
- Accounts for the driver lag deriving from perceptual and neuromuscular
  mechanisms

**Vehicle Dynamics**

For lateral and yaw motion, the block implements these linear dynamic
equations.

x1=Ux˙1=x2=Kptm+ vr−gsin(γ)+Frx1y˙=v+Uψv˙=[−2(CαF+CαR)mU]v+[2(bCαR−aCαF)mU−U]r+(2CαFm)δFr˙=[2(bCαR−aCαF)IU]v+[−2(a2CαF+b2CαR)IU]r+(2aCαFI)δFψ˙=r

In matrix notation:

x˙=Fx+guwhere:x=[x1x2yvrψ]F=[010000Frm000v000010U000−2(CαF+CαR)mU2(bCαR−aCαF)mU−U00002(bCαR−aCαF)IU−2(a2CαF+b2CαR)IU0000010]g=[00Kptm00002CαFm02aCαFI00]u=[u¯ δF]  u¯=u− m2Kptgsin(γ)

The single-point model assumes a minimum previewed error signal at a single
point *T\** seconds ahead in time. *a\** is the
driver ability to predict the future vehicle response based on the current
steering control input. *b\** is the driver ability to predict
the future vehicle response based on the current vehicle state. The block uses
these equations.

a\*=(T\*)mT[I+∑n=1∞Fn(T\*)n(n+1)!]gb\*=mT[I+∑n=1∞Fn(T\*)nn!]mT=[111000]

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
| *γ* | Grade angle |
| ***g*** | Control coefficient vector |
| *U* | Forward (longitudinal) vehicle velocity |
| *T\** | Preview time window |
| *ƒ(t+T\*)* | Previewed path input T\* seconds ahead |
| ***u*** | Tractive force |
| ***mT*** | Constant observer vector; provides vehicle lateral position |
| *ar* | Static rolling and driveline resistance |
| *br* | Linear rolling and driveline resistance |
| *cr* | Aerodynamic rolling and driveline resistance |
| *Fr* | Rolling resistance |

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
