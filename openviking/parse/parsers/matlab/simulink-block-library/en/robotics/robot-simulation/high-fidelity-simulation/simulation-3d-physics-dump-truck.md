---
type: simulink-block
title: 'Simulation 3D Physics Dump Truck'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robot Simulation / High-Fidelity Simulation'
documentation_page: 'simulation3dphysicsdumptruck'
documentation_source_path: 'ref/simulation3dphysicsdumptruck.html'
language: en
---

# Simulation 3D Physics Dump Truck

## Ports

### Input

### **Velocity** — Move vehicle with velocity input `0` (default) | scalar

Velocity input to move the dump truck vehicle, specified as a positive or negative
scalar value in the range of `[-5 , 5]`. Positive value of the
**Velocity** input makes the vehicle move in forward direction whereas
negative value makes it move in the reverse direction. Unit for the velocity input is
meters per second (m/s).

To keep the input truck velocity steady, the system uses a P controller to
internally estimate the required acceleration, taking feedback from the current truck
velocity.

**Data Types:** `double`

### **Throttle** — Normalized input to drive dump truck `0` (default) | scalar

Normalized input to drive dump truck, specified as a positive or negative scalar
value in the range of `[-1 , 1]`. Positive value of the
**Throttle** input makes the vehicle move in forward direction whereas
negative value makes it move in the reverse direction.

The exact response is characterized by the vehicle powertrain. Maximum torque
supported is 200 Newton-meters (Nm) and maximum RPM supported is 6000.

#### Dependencies

To enable this port, select the **Enable throttle
(disable velocity) input signal** parameter. It replaces the
**Velocity** input port with the **Throttle** input port.

**Data Types:** `double`

### **SteeringAngle** — Direction input to vehicle `0` (default) | scalar

Steering angle input to provide direction to the dump truck vehicle, specified as
a positive or negative scalar value in the range of `[-0.7854 ,
0.7854]`​. Unit used is radian.

As the *z* axis points vertically upwards, positive input value
executes counterclockwise motion.

**Data Types:** `double`

### **FootBrake** — Normalized deceleration torque input `0` (default) | scalar

Normalized deceleration torque input to reduce vehicle acceleration, specified as
a nonnegative scalar value in the range of `[0 , 1]`. Maximum
strength supported is 200 Newton-meters (Nm).

#### Dependencies

To enable this port, select the **Enable foot
brake input signal** parameter.

**Data Types:** `double`

### **TruckBedAngle** — Move truck bed up and down with angle input `0` (default) | scalar

Truck bed angle input to raise truck bed up and lower it, specified as a
nonnegative scalar value in the range of `[0 , 0.7854]`. Unit used is
radian.

#### Dependencies

To enable this port, select the **Enable lift
angle input signal** parameter.

**Data Types:** `double`
### Output

### **DumpTruckTranslation** — Current ground truth world translation of dump truck vector

Current ground truth world translation of dump truck, specified as a three-element
row vector, in the form [*x*, *y* ,
*z*]. *x*, *y* , and
*z* are the translations along the *x*,
*y*, and *z* axes respectively. Units are in
meters.

#### Dependencies

To enable this port, select the **Enable ground
truth world tranlsation output signal** parameter under **Dump
Truck Outputs**.

**Data Types:** `double`

### **DumpTruckRotation** — Current ground truth world rotation of dump truck vector

Current ground truth world rotation of dump truck, specified as a three-element
row vector, in the form [*yaw*, *pitch*,
*roll*]. *yaw*, *pitch*, and
*roll* are the rotations about the *z*,
*y*, and *x* axes respectively. Units are in
radians.

#### Dependencies

To enable this port, select the **Enable ground
truth world rotation output signal** parameter under **Dump
Truck Outputs**.

**Data Types:** `double`

### **DumpTruckVelocity** — Current dump truck velocity scalar

Current dump truck velocity, specified as a positive or negative scalar value.
Unit used is meters per second (m/s).

#### Dependencies

To enable this port, select the **Enable velocity
output signal** parameter under **Dump Truck
Outputs**.

**Data Types:** `double`

### **DumpTruckAngularVelocity** — Current dump truck angular velocity `[0 0 0]` (default)

Current dump truck angular velocity, specified as a three-element row vector in
the form [*wx*, *wy*, *wz*]. Unit
used is radians per second.

#### Dependencies

To enable this port, select the **Enable angular
velocity output signal** parameter under **Dump Truck
Outputs**.

**Data Types:** `double`

### **TruckBedTranslation** — Current ground truth world translation of truck bed vector

Current ground truth world translation of truck bed, specified as a three-element
row vector, in the form [*x*, *y* ,
*z*]. *x*, *y* , and
*z* are the translations along the *x*,
*y*, and *z* axes respectively. Units are in
meters.

#### Dependencies

To enable this port, select the **Enable ground
truth world translation output signal** parameter under **Truck
Bed Outputs**.

**Data Types:** `double`

### **TruckBedRotation** — Get current truck-bed world ground truth pose vector

Current ground truth world rotation of dump truck, specified as a three-element
row vector, in the form [*yaw*, *pitch*,
*roll*]. *yaw*, *pitch*, and
*roll* are the rotations about the *z*,
*y*, and *x* axes respectively. Units are in
radian.

To enable this port, select the **Enable ground
truth world rotation output signal** parameter under **Truck Bed
Outputs**.

**Data Types:** `double`

### **CurrentTruckBedAngle** — Current truck bed elevation scalar

Current truck bed current elevation, specified as a positive scalar value. Unit
used is radian.

To enable this port, select the **Enable current
lift angle output signals** parameter under **Truck Bed
Outputs**.

**Data Types:** `double`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Chassis

### **Type** — Dump truck chassis type `Standard Dump Truck` (default)

Dump truck chassis type, specified as `Standard Dump
Truck`.

### **Color** — Dump truck color `Yellow` (default) | `Red` | `White`

Dump truck body color, specified as one of these drop down options:

- `Red`
- `Yellow`
- `White`

### **Name** — Dump truck identifier string scalar

Dump truck identifier name, specified as a string scalar.

### Initial Values

#### Dump Truck Initialization

### **Initial translation (m)** — Initial translation of dump truck vehicle `[0 0 0]` (default) | three-element row vector

Initial translation of dump truck vehicle, specified as a three-element row
vector, in the form [*x*, *y* ,
*z*]. *x*, *y* , and
*z* are the translations along the *x*,
*y*, and *z* axes respectively, which uses the
right-hand rule world coordinate system. Units are in meters.

### **Initial rotation (rad)** — Initial rotation of dump truck vehicle `[0 0 0]` (default) | three-element row vector

Initial rotation of dump truck vehicle, specified as a three-element row vector,
in the form [*yaw*, *pitch*,
*roll*]. *yaw*, *pitch*, and
*roll* are the rotations about the *z*,
*y*, and *x* axes respectively, which uses the
right-hand rule world coordinate system. Units are in radians.

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

#### Dump Truck Inputs

### **Enable throttle (disable velocity) input signal** — Specify throttle to move dump truck at input port `off` (default) | `on`

Select this parameter to disable velocity and specify throttle at input port to
move the dump truck.

### **Enable foot brake input signal** — Specify foot brake at input port `off` (default) | `on`

Specify foot brake torque at input port to de-accelerate the dump truck
vehicle.

#### Truck Bed Inputs

### **Enable lift angle input signal** — Specify truck bed lift angle at input port `off` (default) | `on`

Specify truck bed lift angle to enable **TruckBedAngle** signal at input
port.

### Outputs

#### Dump Truck Outputs

### **Enable ground truth world tranlsation output signal** — Output ground truth world translation of dump truck `off` (default) | `on`

Select this parameter to output ground truth world translation of dump truck at
**DumpTruckTranslation** output port.

### **Enable ground truth world rotation output signal** — Output ground truth world rotation of dump truck `off` (default) | `on`

Select this parameter to output ground truth world rotation of dump truck at
**DumpTruckRotation** output port.

### **Enable velocity output signal** — Output current dump truck velocity `off` (default) | `on`

Select this parameter to output ground truth world rotation of dump truck at
**DumpTruckVelocity** output port.

### **Enable angular velocity output signal** — Output current dump truck angular velocity `off` (default) | `on`

Select this parameter to output ground truth world rotation of dump truck at
**DumpTruckAngularVelocity** output port.

#### Truck Bed Outputs

### **Enable ground truth world translation output signal** — Output ground truth world translation of truck bed `off` (default) | `on`

Select this parameter to output ground truth world translation of truck bed at
**TruckBedTranslation** output port.

### **Enable ground truth world rotation output signal** — Output ground truth world rotation of truck bed `off` (default) | `on`

Select this parameter to output ground truth world rotation of truck bed at
**TruckBedRotation** output port.

### **Enable current lift angle output signals** — Output current truck bed elevation `off` (default) | `on`

Select this parameter to output current truck bed elevation at
**CurrentTruckBedAngle** output port.

## Libraries

Offroad Autonomy Library / Simulation 3D

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Dump truck physics model in 3D simulation environment

The Simulation 3D Physics Dump Truck block provides an interface to
implement a dump truck vehicle in the Simulink® 3D world.

**Note**

Simulating models with the Simulation 3D Physics Dump Truck block requires
Simulink
3D Animation™ and the Robotics System Toolbox™ Offroad Autonomy Library support package. For more information about downloading the support package, see
Install Robotics System Toolbox Offroad Autonomy Library Support Package.

To use this block, ensure that the Simulation 3D Scene
Configuration block is in your model. If you set the **Sample
time** parameter of the Simulation 3D Physics Dump Truck block to
`-1`, the block inherits the sample time specified in the Simulation
3D Scene Configuration block. The sample time in the Simulation 3D Scene
Configuration block must be set to 0.01 or less to prevent jittering of the dump
truck in the 3D visualization environment.

These illustrations provide insight into the dimensions and locations of the
`DumpTruck` asset parameters relative to the coordinate axes, following the
`yaw(z)`, `pitch(y)`, `roll(x)` sequence.
The vehicle layout follows Unreal Engine® co-ordinate system which follows the left-hand rule world coordinate system. For
more information, see Coordinate Systems for Unreal Engine Simulation in Robotics System Toolbox.

Unreal Engine Dump Truck Asset Dimensions

Unreal Engine Dump Truck Axle
