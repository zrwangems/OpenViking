---
type: simulink-block
title: 'Multi-Instance Guidance Model'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Guidance, Navigation, and Control'
documentation_page: 'multiinstanceguidancemodel'
documentation_source_path: 'ref/multiinstanceguidancemodel.html'
language: en
---

# Multi-Instance Guidance Model

## Ports

### Input

### **Control** — Control input bus

Control input for UAVs, specified as a bus. Specify each element of the bus as a
1-by-*N* vector, where *N* is the number of UAVs
that you want to simulate.

If you set the **Model Type** property to
`MultirotorGuidance`, you must specify a bus with these elements:

- `Roll` — Roll angle of each UAV in radians.
- `Pitch` — Pitch angle of each UAV in radians.
- `YawRate` — Yaw rate of each UAV in radians per
  second.
- `Thrust` — Vertical thrust of each UAV in Newtons.

If you set the **Model Type** property to
`FixedWingGuidance`, you must specify a bus with these elements:

- `Height` — Height of each UAV above the ground in
  meters.
- `Airspeed` — Airspeed of each UAV in meters per
  second.
- `RollAngle` — Roll angle of each UAV in radians.

Specify the name of the control input bus by using the **Control Bus
Name** property.

### **Environment** — Environment inputs bus

Environment inputs, specified as a bus. Specify each element of the bus as a
1-by-*N* vector, where *N* is the number of UAVs
that you want to simulate.

If you set the **Model Type** property to
`MultirotorGuidance`, you must specify a bus with
`Gravity` element which contains the gravitational acceleration for
each UAV in the z-axis direction of the inertial frame in meters per second
squared.

If you set the **Model Type** property to
`FixedWingGuidance`, you must specify a bus with these elements:

- `WindNorth` — Wind velocity in the north direction for each
  UAV in meters per second.
- `WindEast` — Wind velocity in the east direction for each
  UAV in meters per second.
- `WindDown` — Wind velocity in the downward direction for
  each UAV in meters per second.
- `Gravity` — Gravitational acceleration for each UAV in the
  z-axis direction of the inertial frame in meters per second squared.

Specify the name of the environment input bus by using the **Environment
Bus Name** property.

**Data Types:** `bus`
### Output

### **State** — Simulated UAV state bus

Simulated UAV state, returned as a bus. Each element in the bus is a matrix or
vector with *N* columns, where *N* is the number of
UAV that you simulate.

If you set the **Model Type** property to
`MultirotorGuidance`, the block returns the state output as an
eight-element bus with these elements:

- `<WorldPosition>` — 3-by-*N* matrix of
  UAV positions. Each column of the matrix contains the
  *xyz*-position of a UAV in meters.
- `<WorldVelocity>` — 3-by-*N* matrix of
  UAV velocities. Each column of the matrix contains the
  *xyz*-velocity of a UAV in meters per second.
- `<EulerZYX>` — 3-by-*N* matrix of UAV
  Euler angles. Each column of the matrix contains the Euler angles of a UAV in
  *z-*,*y-*,*x-*axis
  (yaw-pitch-roll) rotation sequence.
- `<BodyAngularRateRPY>` — 3-by-*N*
  matrix of UAV angular rates. Each column of the matrix contains the angular rate
  of a UAV with respect to the *x-*,*y-*, and
  *z-* axes (roll rate, pitch rate, and yaw rate, respectively)
  in radians per second.
- `<Thrust>` — 1-by-*N* vector of UAV
  thrusts. Each element of the vector contains the thrust of a UAV in
  newtons.

If you set the **Model Type** property to
`FixedWingGuidance`, the block returns the state output as a bus
with eight elements, where each element is a 1-by-*N* vector. The bus
contains these elements:

- `<North>` — Position in the north direction for each UAV
  in meters.
- `<East>` — Position int he east direction for each UAV
  in meters.
- `<Height>` — Height above the ground for each UAV in
  meters.
- `<AirSpeed>` — Speed relative to the wind for each UAV
  in meters per second.
- `<HeadingAngle>` — Angle between the ground velocity and
  north direction for each UAV in radians.
- `<FlightPathAngle>` — Angle between the ground velocity
  and north-east plane for each UAV in radians.
- `<RollAngle>` — Angle of rotation along the body
  *x*-axis for each UAV in radians per second.
- `<RollAngleRate>` — Angular velocity of rotation along
  the body *x*-axis for each UAV in radians per second.

Specify the name of the state output bus by using the **State Bus
Name** property.

**Data Types:** `bus`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Model Type** — UAV guidance model type `MultirotorGuidance` (default) | `FixedWingGuidance`

Guidance model type for all UAVs. Select `MultirotorGuidance` to
simulate multirotor UAVs or `FixedWingGuidance` to simulate fixed wing
UAVs.

### **Number of Instances** — Number of UAVs to simulate `5` (default) | positive integer

Specify the number of UAVs to simulate as a positive integer.

### **Data Type** — Input and output numeric data types `double` (default) | `single`

Specify the input and output numeric data types as `double` or
`single`.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Code generation` — Simulate model using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for subsequent
  simulations, as long as the model does not change. This option requires additional
  startup time, but the speed of the subsequent simulations is comparable to
  `Interpreted execution`.
- `Interpreted execution` — Simulate model using
  the MATLAB® interpreter. This option shortens startup time but has a slower
  simulation speed than `Code generation`. In this mode, you
  can debug the source code of the block.

### **Initial State** — Initial UAV state tab multiple table entries

Initial UAV state tab, specified as multiple table entries. In all initial state
descriptions, *N* is the number of UAVs that you are simulating.

For multirotor UAVs, you must specify these initial states:

- **World Position** — 3-by-*N* matrix.
  Specify each column of the matrix as the initial *xyz*-position
  of a UAV in meters. The default value for each UAV is
  `[0;0;0]`.
- **World Velocity** — 3-by-*N*. Specify each
  column of the matrix as the initial *xyz*-velocity of a UAV in
  meters per second. The default value for each UAV is
  `[0;0;0]`.
- **Euler Angles (ZYX)** — 3-by-*N* matrix.
  Specify each column of the matrix with the initial Euler angles of a UAV in
  *z-*,*y-*,*x-*axis
  (yaw-pitch-roll) rotation sequence. The default value for each UAV is
  `[0;0;0]`.
- **Body Angular Rates** — 3-by-*N* matrix.
  Specify each column of the matrix as the initial angular rate of a UAV with
  respect to the *x-*,*y-*, and
  *z-*axes (roll rate, pitch rate, and yaw rate, respectively) in
  radians per second. The default value for each UAV is
  `[0;0;0]`.
- **Thrust** — 1-by*-N* vector. Specify each
  element of the vector as the initial thrust of a UAV in newtons. The default value
  for each UAV is `0`.

For fixed-wing UAVs, you must specify these initial states as
1-by-*N* vectors:

- **North Position** — Initial position in the north direction
  for each UAV in meters. The default value for each UAV is
  `0`.
- **East Position** — Initial position in the east direction
  for each UAV in meters. The default value for each UAV is
  `0`.
- **Height** — Initial height above the ground each for each
  UAV in meters. The default value for each UAV is `0`.
- **Air Speed** — Initial speed relative to the wind for each
  UAV in meters per second. The default value for each UAV is
  `0`.
- **Heading Angle** — Initial angle between the ground velocity
  and north direction for each UAV in radians. The default value for each UAV is
  `0`.
- **Flight Path Angle** — Initial angle between the ground
  velocity and north-east plane for each UAV in radians. The default value for each
  UAV is `0`.
- **Roll Angle** — Initial angle of rotation along the body
  *x*-axis for each UAV in radians per second. The default value
  for each UAV is `0`.
- **Roll Angle Rate** — Initial angular velocity of rotation
  along the body *x*-axis for each UAV in radians per second. The
  default value for each UAV is `0`.

**Tunable:** No

### **Configuration** — UAV controller configuration tab multiple table entries

UAV controller configuration tab, specified as multiple table entries. In all
controller configuration descriptions, *N* is the number of UAVs that
you are simulating.

For multirotor UAVs, specify these parameters:

- **PD Roll** — *N*-by-2 matrix. Specify each
  row of the matrix as the proportional and derivative gains of the roll angle
  controller for a UAV. The default value for each UAV is `[3402.97
  116.67]`.
- **PD Pitch** — *N*-by-2 matrix. Specify each
  row of the matrix as the proportional and derivative gains of the pitch angle
  controller for a UAV. The default value for each UAV is `[3402.97
  116.67]`.
- **P YawRate** — *N*-by-1 vector. Specify
  each element of the vector as the proportional gain of the yaw rate controller for
  a UAV. The default value for each UAV is `1950`.
- **P Thrust** — *N*-by-1 vector. Specify each
  row of the vector as the proportional gain of the thrust controller for a UAV. The
  default value for each UAV is `3900`.
- **Mass** — *N*-by-1 vector. Specify each
  element of the vector as the mass of a UAV in Kg. The default value for each UAV
  is `0.1`.

For fixed-wing UAVs, specify these parameters:

- **P Height** — *N*-by-1 vector. Specify each
  element of the vector as the proportional gain of the height controller for a UAV.
  The default value for each UAV is `3.9`.
- **P Flight Path Angle** — *N*-by-1 vector.
  Specify each element of the vector as the proportional gain of the flight path
  angle controller for a UAV. The default value for each UAV is
  `39`.
- **PD Roll** — *N*-by-2 matrix. Specify each
  element of the matrix as the proportional and derivative gains of the pitch angle
  controller for a UAV. The default value for each UAV is `[3402.97
  116.67]`.
- **P Air Speed** — *N*-by-1 vector. Specify
  each element of the vector as the proportional gain of the air speed controller
  for a UAV. The default value for each UAV is `1`.
- **Min/Max Flight Path Angle** — *N*-by-2
  matrix. Specify each element of the matrix as the minimum and maximum flight path
  angle for a UAV in radians. The default value for each UAV is `[-pi/2
  pi/2]`

### **Input/Output Bus Names** — Simulink bus signal names tab bus names

This tab contains the **State Bus Name**, **Control Bus
Name**, and **Environment Bus Name** parameters, which
specify the name of the output state bus, the input control bus, and the input
environment bus, respectively. Each bus has a default name based on the UAV model and
input type.

| Model Type Parameter | Default State Bus Name | Default Control Bus Name | Default Environment Bus Name |
| --- | --- | --- | --- |
| `FixedWingGuidance` | `FixedWingGuidanceStateBus` | `FixedWingGuidanceControlBus` | `FixedWingGuidanceEnvironmentBus` |
| `MultirotorGuidance` | `MultirotorGuidanceStateBus` | `MultirotorGuidanceControlBus` | `MultirotorGuidanceEnvironmentBus` |

To use multiple guidance models in the same Simulink model, specify bus names for each Multi-Instance Guidance Model block that
do not intersect with one another.

## Libraries

UAV Toolbox / Algorithms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Reduced-order model for multiple UAVs

The Multi-Instance Guidance Model block simulates multiple small UAVs by
using reduced-order fixed-wing [1] or multirotor [2] kinematic models and
autopilot controllers.
