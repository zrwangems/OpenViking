---
type: simulink-block
title: 'Simulation 3D Physics Backhoe'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robot Simulation / High-Fidelity Simulation'
documentation_page: 'simulation3dphysicsbackhoe'
documentation_source_path: 'ref/simulation3dphysicsbackhoe.html'
language: en
---

# Simulation 3D Physics Backhoe

## Ports

### Input

### **Velocity** — Move vehicle with velocity input `0` (default) | scalar in the range of `[-7.5 ,7.5]`

Velocity input to move the backhoe vehicle, specified as a scalar in the range of
`[-7.5 , 7.5]`.A positive value moves the vehicle forward, whereas
a negative value reverses the direction. Specify the velocity in meters per second
(m/s).

To keep the input backhoe velocity steady, the system uses a P controller to
internally estimate the required acceleration, taking feedback from the current
backhoe velocity.

**Data Types:** `double`

### **Throttle** — Normalized input to drive backhoe `0` (default) | scalar in the range of `[-1 , 1]`

Normalized input to drive the backhoe, specified as a scalar in the range of
`[-1 , 1]`. A positive value moves the vehicle forward, whereas a
negative value reverses the direction.

The exact response is characterized by the vehicle powertrain. Maximum torque
supported by the block is 200 Newton-meters (Nm) and maximum RPM is 6000.

#### Dependencies

To enable this port, select the **Enable throttle
(disable velocity) input signal** parameter under **Backhoe
Inputs**.

**Data Types:** `double`

### **SteeringAngle** — Direction input to vehicle `0` (default) | scalar in the range of `[-0.7854 , 0.7854]`

Steering angle input to provide direction to the backhoe vehicle, specified as a
scalar in the range of `[-0.7854 , 0.7854]`​. Specify the steering
angle in radians.

As the *z* axis points vertically upwards,a positive input value
executes counterclockwise motion.

**Data Types:** `double`

### **FootBrake** — Normalized deceleration torque input `0` (default) | scalar in the range of `[0 , 1]`

Normalized deceleration torque input to reduce vehicle acceleration, specified as
a scalar in the range of `[0 , 1]`. Maximum strength supported by the
block is 200 Newton-meters (Nm).

#### Dependencies

To enable this port, select the **Enable foot
brake input signal** parameter under **Backhoe
Inputs**.

**Data Types:** `double`

### **FrontBucketAngle** — Raise or lower front bucket with angle input `0` (default) | scalar in the range of `[-0.6109, 1.5533]`

Front bucket angle input to raise front bucket up and lower it, specified as a
scalar in the range of `[-0.6109, 1.5533]`. Specify the front bucket
angle in radians.

#### Dependencies

To enable this port, select the **Enable loader
frame and front bucket angle input signals** parameter under
**Front Bucket Inputs**.

**Data Types:** `double`

### **LoaderFrameAngle** — Raise or lower loader frame with angle input `0` (default) | scalar in the range of `[-1.3963, 0]`

Front loader frame angle input to raise front loader frame up and lower it,
specified as a scalar in the range of `[-1.3963, 0]`. Specify the
loader frame angle in radians.

#### Dependencies

To enable this port, select the **Enable loader
frame and front bucket angle input signals** parameter under
**Front Bucket Inputs**.

**Data Types:** `double`

### **RearBucketAngle** — Raise or lower rear bucket with angle input `0` (default) | scalar in the range of `[0, 1.5533]`

Rear bucket angle input to raise rear bucket up and lower it, specified as a
scalar in the range of `[0, 1.5533]`. Specify the rear bucket angle
in radians.

#### Dependencies

To enable this port, select the **Enable swing
frame, boom, arm, and rear bucket angle input signals** parameter under
**Rear Bucket Inputs**.

**Data Types:** `double`

### **ArmAngle** — Raise or lower rear arm with angle input `0.0571` (default) | scalar in the range of `[0.0571, 1.5533]`

Rear arm angle input to raise rear bucket up and lower it, specified as a scalar
in the range of `[0.0571, 1.5533]`. Specify the arm angle in
radians.

#### Dependencies

To enable this port, select the **Enable swing
frame, boom, arm, and rear bucket angle input signals** parameter under
**Rear Bucket Inputs**.

**Data Types:** `double`

### **BoomAngle** — Raise or lower rear boom with angle input `0` (default) | scalar in the range of `[-1.5533 , 0]`

Rear boom angle input to raise rear boom up and lower it, specified as a scalar in
the range of `[-1.5533 , 0]`. Specify the boom angle in
radians.

#### Dependencies

To enable this port, select the **Enable swing
frame, boom, arm, and rear bucket angle input signals** parameter under
**Rear Bucket Inputs**.

**Data Types:** `double`

### **SwingFrameAngle** — Move rear swing left-right with angle input `0` (default) | scalar in the range of `[-1.2217, 1.2217]`

Rear swing angle input to move rear swing left and right, specified as a scalar in
the range of `[-1.2217, 1.2217]`. Specify the swing frame angle in
radians.

#### Dependencies

To enable this port, select the **Enable swing
frame, boom, arm, and rear bucket angle input signals** parameter under
**Rear Bucket Inputs**.

**Data Types:** `double`
### Output

### **BackhoeTranslation** — Current ground truth world translation of backhoe vector

Current ground truth world translation of backhoe, specified as a three-element
row vector in the form [*x*, *y* ,
*z*]. *x*, *y* , and
*z* are the translations along the *x*,
*y*, and *z* axes, respectively. Units are in
meters.

#### Dependencies

To enable this port, select the **Enable ground
truth world tranlsation output signal** parameter under
**Backhoe Outputs**.

**Data Types:** `double`

### **BackhoeRotation** — Current ground truth world rotation of backhoe vector

Current ground truth world rotation of backhoe, specified as a three-element row
vector in the form [*yaw*, *pitch*,
*roll*]. *yaw*, *pitch*, and
*roll* are the rotations about the *z*,
*y*, and *x* axes, respectively. Units are in
radians.

#### Dependencies

To enable this port, select the **Enable ground
truth world rotation output signal** parameter under **Backhoe
Outputs**.

**Data Types:** `double`

### **BackhoeVelocity** — Current velocity of backhoe scalar

Current velocity of the backhoe, specified as a positive or negative scalar value.
Unit are meters per second (m/s).

#### Dependencies

To enable this port, select the **Enable velocity
output signal** parameter under **Backhoe
Outputs**.

**Data Types:** `double`

### **BackhoeAngularVelocity** — Current angular velocity of backhoe `[0 0 0]` (default) | three-element row vector

Current angular velocity of the backhoe, specified as a three-element row vector
in the form [*wx*, *wy*, *wz*].
Unit are radians per second.

#### Dependencies

To enable this port, select the **Enable angular
velocity output signal** parameter under **Backhoe
Outputs**.

**Data Types:** `double`

### **FrontBucketTranslation** — Current ground truth world translation of front bucket vector

Current ground truth world translation of front bucket, specified as a
three-element row vector in the form [*x*, *y* ,
*z*]. *x*, *y* , and
*z* are the translations along the *x*,
*y*, and *z* axes, respectively. Units are in
meters.

#### Dependencies

To enable this port, select the **Enable front
bucket ground truth world translation output signal** parameter under
**Backhoe Outputs**.

**Data Types:** `double`

### **FrontBucketRotation** — Current ground truth world rotation of front bucket vector

Current ground truth world rotation of front bucket, specified as a three-element
row vector in the form [*yaw*, *pitch*,
*roll*]. *yaw*, *pitch*, and
*roll* are the rotations about the *z*,
*y*, and *x* axes, respectively. Units are in
radian.

#### Dependencies

To enable this port, select the **Enable front
bucket ground truth world rotation output signal** parameter under
**Backhoe Outputs**.

**Data Types:** `double`

### **RearBucketTranslation** — Current ground truth world translation of rear bucket vector

Current ground truth world translation of rear bucket, specified as a
three-element row vector, in the form [*x*, *y* ,
*z*]. *x*, *y* , and
*z* are the translations along the *x*,
*y*, and *z* axes respectively. Units are in
meters.

#### Dependencies

To enable this port, select the **Enable rear
bucket ground truth world translation output signal** parameter under
**Backhoe Outputs**.

**Data Types:** `double`

### **RearBucketRotation** — Current ground truth world rotation of rear bucket vector

Current ground truth world rotation of rear bucket, specified as a three-element
row vector in the form [*yaw*, *pitch*,
*roll*]. *yaw*, *pitch*, and
*roll* are the rotations about the *z*,
*y*, and *x* axes, respectively. Units are in
radian.

#### Dependencies

To enable this port, select the **Enable rear
bucket ground truth world rotation output signal** parameter under
**Backhoe Outputs**.

**Data Types:** `double`

### **CurrentFrontBucketAngle** — Current front bucket joint angle scalar

Current front bucket joint angle, specified as a positive or negative scalar
value. Units are in radians.

#### Dependencies

To enable this port, select the **Enable current
loader frame and front bucket angle output signals** parameter under
**Front Bucket Outputs**.

**Data Types:** `double`

### **CurrentLoaderFrameAngle** — Current loader frame joint angle scalar

Current loader frame joint angle, specified as a negative scalar value. Units are
in radians.

#### Dependencies

To enable this port, select the **Enable current
loader frame and front bucket angle output signals** parameter under
**Front Bucket Outputs**.

**Data Types:** `double`

### **CurrentRearBucketAngle** — Current rear bucket joint angle scalar

Current rear bucket joint angle, specified as a positive scalar value. Units are
in radians.

#### Dependencies

To enable this port, select the **Enable current
swing frame, boom, arm, and rear bucket angle input signals** parameter
under **Rear Bucket Outputs**.

**Data Types:** `double`

### **CurrentArmAngle** — Current rear arm joint angle scalar

Current rear arm joint angle, specified as a positive scalar value. Units are in
radians.

#### Dependencies

To enable this port, select the **Enable current
swing frame, boom, arm, and rear bucket angle input signals** parameter
under **Rear Bucket Outputs**.

**Data Types:** `double`

### **CurrentBoomAngle** — Current rear boom joint angle scalar

Current rear boom joint angle, specified as a negative scalar value. Units are in
radians.

#### Dependencies

To enable this port, select the **Enable current
swing frame, boom, arm, and rear bucket angle input signals** parameter
under **Rear Bucket Outputs**.

**Data Types:** `double`

### **CurrentSwingFrameAngle** — Current swing frame joint angle scalar

Current swing frame joint angle, specified as a positive or negative scalar value.
Units are in radians.

#### Dependencies

To enable this port, select the **Enable current
swing frame, boom, arm, and rear bucket angle input signals** parameter
under **Rear Bucket Outputs**.

**Data Types:** `double`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Chassis

### **Type** — Backhoe chassis type `Wheeled Backhoe` (default)

Backhoe chassis type, specified as `Wheeled
Backhoe`.

### **Color** — Backhoe color `Yellow` (default) | `Blue` | `Orange`

Backhoe body color, specified as one of these drop down options:

- `Blue`
- `Yellow`
- `Orange`

### **Name** — Backhoe identifier string scalar

Backhoe identifier name, specified as a string scalar.

### Initial Values

#### Backhoe Initialization

### **Initial translation (m)** — Initial translation of backhoe vehicle `[0 0 0]` (default) | vector

Initial translation of backhoe vehicle, specified as a three-element row vector,
in the form [*x*, *y* , *z*].
*x*, *y* , and *z* are the
translations along the *x*, *y*, and
*z* axes respectively, which uses the right-hand rule world
coordinate system. Units are in meters.

### **Initial rotation (rad)** — Initial rotation of backhoe vehicle `[0 0 0]` (default) | vector

Initial rotation of backhoe vehicle, specified as a three-element row vector, in
the form [*yaw*, *pitch*, *roll*].
*yaw*, *pitch*, and *roll* are
the rotations about the *z*, *y*, and
*x* axes respectively, which uses the right-hand rule world
coordinate system. Units are in radians.

### rigidBodyTree Geometry Settings

Set the parameters in this tab to enable the visualization of the rigid body tree
geometry in the 3D visualization environment.

#### Collision Geometry Visualization

### **Enable collision geometry visualization in 3D scene** — Visualize rigid body tree collision geometry in 3D visualization environment `off` (default) | `on`

Select this parameter to visualize rigid body tree collision geometry in the 3D
visualization environment.

### **Collision geometry color** — Color of the rigid body tree collision geometry `[0 1 0]` (default) | vector

Color of the rigid body tree collision geometry being visualized in the 3D
visualization environment, specified as a three-element row vector.

### **Collision geometry transparency** — Transparency of the rigid body tree collision geometry `0.1` (default) | scalar

Transparency of the rigid body tree collision geometry being visualized in the 3D
visualization environment, specified as a scalar.

### Inputs

#### Backhoe Inputs

### **Enable throttle (disable velocity) input signal** — Specify throttle to move backhoe at input port `off` (default) | `on`

Select this parameter to disable the velocity input and specify throttle at the
input port to move the backhoe vehicle.

### **Enable foot brake input signal** — Specify foot brake at input port `off` (default) | `on`

Specify foot brake torque at the input port to de-accelerate the backhoe
vehicle.

#### Front Bucket Inputs

### **Enable loader frame and front bucket angle input signals** — Specify loader frame and front bucket angle at input port `off` (default) | `on`

Select this parameter to specify the loader frame and front bucket angles at the
input port.

#### Rear Bucket Inputs

### **Enable swing frame, boom, arm, and rear bucket angle input signals** — Specify swing frame, boom, arm, and rear bucket angle at input port `off` (default) | `on`

Select this parameter to specify the swing frame, boom, arm, and rear bucket angle
at the input port.

### Outputs

#### Backhoe Outputs

### **Enable ground truth world tranlsation output signal** — Output ground truth world translation of backhoe `off` (default) | `on`

Select this parameter to output ground truth world translation of backhoe at the
**BackhoeTranslation** output port.

### **Enable ground truth world rotation output signal** — Output ground truth world rotation of backhoe `off` (default) | `on`

Select this parameter to output ground truth world rotation of backhoe at the
**BackhoeRotation** output port.

### **Enable velocity output signal** — Output current velocity of backhoe `off` (default) | `on`

Select this parameter to output current velocity of backhoe at the
**BackhoeVelocity** output port.

### **Enable angular velocity output signal** — Output current angular velocity of backhoe `off` (default) | `on`

Select this parameter to output current angular velocity of backhoe at the
**BackhoeAngularVelocity** output port.

#### Front Bucket Outputs

### **Enable front bucket ground truth world translation output signal** — Output ground truth world translation of front bucket `off` (default) | `on`

Select this parameter to output ground truth world translation of front bucket at
the **FrontBucketTranslation** output port.

### **Enable front bucket ground truth world rotation output signal** — Output ground truth world rotation of front bucket `off` (default) | `on`

Select this parameter to output ground truth world rotation of front bucket at the
**FrontBucketRotation** output port.

### **Enable current loader frame and front bucket angle output signals** — Output current loader frame and front bucket joint angle `off` (default) | `on`

Select this parameter to output current loader frame and front bucket joint angle
at the **CurrentLoaderFrameAngle** and **CurrentFrontBucketAngle**
output ports respectively.

#### Rear Bucket Outputs

### **Enable rear bucket ground truth world translation output signal** — Output ground truth world translation of rear bucket `off` (default) | `on`

Select this parameter to output ground truth world translation of rear bucket at
the **RearBucketTranslation** output port.

### **Enable rear bucket ground truth world rotation output signal** — Output ground truth world rotation of rear bucket `off` (default) | `on`

Select this parameter to output ground truth world rotation of rear bucket at the
**RearBucketRotation** output port.

### **Enable current swing frame, boom, arm, and rear bucket angle output signals** — Output current swing frame angle and current rear bucket, rear boom and rear arm joint angle `off` (default) | `on`

Set this parameter to output the current swing frame angle and the current rear
bucket, rear boom, and rear arm joint angles at the **CurrentSwingAngle**,
**CurrentRearBucketAngle**, **CurrentBoomAngle**, and
**CurrentArmAngle** output ports, respectively.

## Libraries

Offroad Autonomy Library / Simulation 3D

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Backhoe physics model in 3D simulation environment

The Simulation 3D Physics Backhoe block provides an interface to implement
a backhoe vehicle in the Simulink® 3D world.

**Note**

Simulating models with the Simulation 3D Physics Backhoe block requires
Simulink
3D Animation™ and the Robotics System Toolbox™ Offroad Autonomy Library support package. For more information about downloading the support package, see
Install Robotics System Toolbox Offroad Autonomy Library Support Package.

To use this block, ensure that the Simulation 3D Scene
Configuration block is in your model. If you set the **Sample
time** parameter of the Simulation 3D Physics Backhoe block to
`-1`, the block inherits the sample time specified in the Simulation
3D Scene Configuration block. The sample time in the Simulation 3D Scene
Configuration block must be set to 0.01 or less to prevent jittering of the backhoe
in the 3D visualization environment.

These illustrations show the dimensions and locations of the backhoe asset parameters
relative to the coordinate axes, following the `yaw(z)`,
`pitch(y)`, `roll(x)` sequence. The vehicle layout follows
Unreal Engine® co-ordinate system which follows the left-hand rule world coordinate system. For
more information, see Coordinate Systems for Unreal Engine Simulation in Robotics System Toolbox.

Backhoe vehicle side view

Backhoe vehicle top view
