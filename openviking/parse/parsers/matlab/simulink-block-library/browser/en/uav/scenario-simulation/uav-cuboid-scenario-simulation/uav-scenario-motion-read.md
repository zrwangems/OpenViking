---
type: simulink-block
title: 'UAV Scenario Motion Read'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / UAV Cuboid Scenario Simulation'
documentation_page: 'uavscenariomotionread'
documentation_source_path: 'ref/uavscenariomotionread.html'
language: en
---

# UAV Scenario Motion Read

## Ports

### Output

### **Motion** — UAV motion data bus

Output motion from a platform or sensor specified as a bus with the following
properties with the name specified in Platform or sensor name:

- *PlatformID* – ID of platform based on order of platforms
  in the `uavScenario.Platforms` property.
- *Position* – Position in NED frame specified as a 1-by-3
  vector.
- *Orientation* – Orientation in NED frame specified as a
  1-by-4 vector, quaternion, frame rotation from NED frame to UAV body
  frame.
- *Velocity* – Velocity in NED frame specified as a 1-by-3
  vector.
- *Acceleration* – Acceleration in NED frame specified as a
  1-by-3 vector.
- *AngularVelocity* – Angular velocity in NED frame specified
  as a 1-by-3 vector.

If a sensor name is specified in `Platform or sensor
name`, the *SensorID* field is added to the bus fields of
the motion output bus.

- *SensorID* – ID of sensor specified as a scalar based on
  the order of sensors in the `uavScenario.Platforms`
  property.

The platform and sensors motion buses are of the type named in the
`Sensor motion bus name` and `Sensor motion bus
name` properties of the UAV Scenario
Configuration block in the model.

### **SampledWind** — Resultant wind translational and angular velocity 1-by-6 vector

Resultant wind translational and angular velocity from all wind model objects in
UAV platform body frame, returned as a 1-by-6 vector of the form
[uw vw ww
pw qw rw].
uw, vw, and ww
represents resultant wind translational velocities in positive x- y- and z- directions
of the UAV platform body frame in m/s. pw,
qw, and rw represents resultant wind
angular velocities in positive x- y- and z- directions of the UAV platform body frame
in rad/s.

#### Dependencies

This port is only visible if **Generate wind velocity and angular
velocity samples** is checked.

### **SampledWindByComponent** — Wind translational and angular velocities from each wind model objects *N*-by-6 matrix

Wind translational and angular velocity from each wind model objects in UAV
platform body frame, returned as a *N*-by-6 matrix where
*N* is the number of wind model objects added to the UAV platform.
Each row has the form [uw vw
ww pw qw
rw]. uw, vw,
and ww represents wind translational velocities in positive x-
y- and z- directions in m/s. pw, qw, and
rw represents wind angular velocities in positive x- y- and
z- directions in rad/s.

#### Dependencies

This port is only visible if **Generate wind velocity and angular
velocity samples** is checked.

## Parameters

### **Platform or sensor name** — Platform or sensor name `'UAV'` (default) | string

Use **Select** to choose one platform or sensor from the UAV
Scenario to read motion from.

This parameter effects the fields of the motion bus output. See `Motion` output for
more information.

### **Coordinate frame of output motion** — Coordinate frame of output motion `'ENU'` (default) | `'NED'` | string

Specify the coordinate frame of the output motion as East-North-Up
(`'ENU'`) or North-East-Down (`'NED'`).

### **Generate wind velocity and angular velocity samples** — Generate wind velocity and angular velocities samples `off` (default) | `on`

Output wind velocity from the **SampledWind** and
**SampledWindByComponent** ports.

#### Dependencies

This parameter is only enabled if you have selected a platform and the Aerospace Blockset™ license is available. Simulating with this parameter turned on checks
out the Aerospace Blockset license

## Libraries

UAV Toolbox / UAV Scenario and Sensor Modeling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

### R2024a: **Generate wind velocity and angular velocity samples**

UAV Scenario Motion Read block now has generate wind velocity and angular velocity
samples parameter that you can enable to output the wind translational and angular
velocities

## Description

Read platform and sensor motions from UAV scenario simulation

Use this block to read motion as a bus from a sensor or platform in a UAV scenario
simulation. The motion bus contains the position, orientation, velocity, angular velocity,
acceleration, and ID of the platform or sensor.

To use this block, ensure that a UAV Scenario
Configuration block is in your model.

This block uses the sample time specified in the UAV Scenario Configuration
block.
