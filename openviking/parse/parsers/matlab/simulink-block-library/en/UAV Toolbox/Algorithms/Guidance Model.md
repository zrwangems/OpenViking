---
type: simulink-block
title: 'Guidance Model'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Algorithms'
documentation_page: 'guidancemodel'
documentation_source_path: 'ref/guidancemodel.html'
language: en
---

# Guidance Model

## Ports

### Input

### **Control** — Control commands bus

Control commands sent to the UAV model, specified as a bus.

For multirotor UAVs, the model is approximated as separate PD controllers for each
command. The elements of the bus are control command:

- `Roll` - Roll angle in radians.
- `Pitch` - Pitch angle in radians.
- `YawRate` - Yaw rate in radians per second. (D = 0. P only
  controller)
- `Thrust` - Vertical thrust of the UAV in Newtons. (D = 0. P
  only controller)

For fixed-wing UAVs, the model assumes the UAV is flying under the
coordinated-turn condition. The guidance model equations assume zero side-slip. The
elements of the bus are:

- `Height` - Altitude above the ground in meters.
- `AirSpeed` - UAV speed relative to wind in meters per
  second.
- `RollAngle` - Roll angle along body forward axis in
  radians. Because of the coordinated-turn condition, the heading angular rate is
  based on the roll angle.

Specify the name of the control input bus by using the **Control Bus
Name** property.

### **Environment** — Environmental inputs bus

Environmental inputs, specified as a bus. The model compensates for these
environmental inputs when trying to achieve the commanded controls.

If you set the **Model Type** property to
`MultirotorGuidance`, you must specify a bus with
`Gravity` element which contains the gravitational acceleration for
the UAV in the z-axis direction of the inertial frame in meters per second
squared.

If you set the **Model Type** property to
`FixedWingGuidance`, you must specify a bus with these elements:

- `WindNorth` — Wind velocity in the north direction for the
  UAV in meters per second.
- `WindEast` — Wind velocity in the east direction for the
  UAV in meters per second.
- `WindDown` — Wind velocity in the downward direction for
  the UAV in meters per second.
- `Gravity` — Gravitational acceleration for the UAV in the
  z-axis direction of the inertial frame in meters per second squared.

Specify the name of the environment input bus by using the **Environment
Bus Name** property.

**Data Types:** `bus`
### Output

### **State** — Simulated UAV state bus

Simulated UAV state, returned as a bus. The block uses the
`Control` and `Environment` inputs with the
guidance model equations to simulate the UAV state.

For multirotor UAVs, the state is a five-element bus:

- **WorldPosition** - `[x y z]` in
  meters.
- **WorldVelocity** - `[vx vy vz]` in meters
  per second.
- **EulerZYX** - `[psi theta phi]` Euler
  angles in radians.
- **BodyAngularRateRPY** - `[r p q]` in
  radians per second along the `xyz`-axes of the UAV.
- **Thrust** - `F` in Newtons.

For fixed-wing UAVs, the state is an eight-element bus:

- **North** - Position in north direction in meters.
- **East** - Position in east direction in meters.
- **Height** - Height above ground in meters.
- **AirSpeed** - Speed relative to wind in meters per
  second.
- **HeadingAngle** - Angle between ground velocity and north
  direction in radians.
- **FlightPathAngle** - Angle between ground velocity and
  north-east plane in radians.
- **RollAngle** - Angle of rotation along body
  *x*-axis in radians per second.
- **RollAngleRate** - Angular velocity of rotation along body
  *x*-axis in radians per second.

**Data Types:** `bus`

## Parameters

### **ModelType** — UAV guidance model type `MultirotorGuidance` (default) | `FixedWingGuidance`

UAV guidance model type, specified as `MultirotorGuidance` or
`FixedWingGuidance`. The model type determines the elements of the
UAV `State` and the required `Control` and
`Environment` inputs.

**Tunable:** No

### **DataType** — Input and output numeric data types `double` (default) | `single`

Input and output numeric data types, specified as either `double`
or `single`. Choose the data type based on possible software or
hardware limitations.

**Tunable:** No

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Code generation` — Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for subsequent
  simulations, as long as the model does not change. This option requires additional
  startup time, but the speed of the subsequent simulations is comparable to
  `Interpreted execution`.
- `Interpreted execution` — Simulate model using
  the MATLAB® interpreter. This option shortens startup time but has a slower
  simulation speed than `Code generation`. In this mode, you
  can debug the source code of the block.

**Tunable:** No

### **Initial State** — Initial UAV state tab multiple table entries

Initial UAV state tab, specified as multiple table entries. All entries on this tab
are nontunable.

For multirotor UAVs, the initial state is:

- **World Position** - `[x y z]` in
  meters.
- **World Velocity** - `[vx vy vz]` in meters
  per second.
- **Euler Angles (ZYX)** - `[psi theta phi]`
  in radians.
- **Body Angular Rates** - `[p q r]` in
  radians per second.
- **Thrust** - `F` in Newtons.

For fixed-wing UAVs, the initial state is:

- **North** - Position in north direction in meters.
- **East** - Position in east direction in meters.
- **Height** - Height above ground in meters.
- **Air Speed** - Speed relative to wind in meters per
  second.
- **Heading Angle** - Angle between ground velocity and north
  direction in radians.
- **Flight Path Angle** - Angle between ground velocity and
  north-east plane in radians.
- **Roll Angle** - Angle of rotation along body
  *x*-axis in radians per second.
- **Roll Angle Rate** - Angular velocity of rotation along body
  *x*-axis in radians per second.

**Tunable:** No

### **Configuration** — UAV controller configuration tab multiple table entries

UAV controller configuration tab, specified as multiple table entries. This tab
allows you to configure the parameters of the internal control behaviour of the UAV.
Specify the proportional (P) and derivative (D) gains for the dynamic model and the UAV
mass in kilograms (for multirotor).

For multirotor UAVs, the parameters are:

- **PD Roll**
- **PD Pitch**
- **P YawRate**
- **P Thrust**
- **Mass**(kg)

For fixed-wing UAVs, the parameters are:

- **P Height**
- **P Flight Path Angle**
- **PD Roll**
- **P Air Speed**
- **Min/Max Flight Path Angle** (`[min max]`
  angle in radians)

**Tunable:** No

### **Input/Output Bus Names** — Simulink bus signal names tab multiple entries of character vectors

Simulink bus signal names tab, specified as multiple entries of character vectors.
These buses have a default name based on the UAV model and input type. To use multiple
guidance models in the same Simulink model, specify different bus names that do not intersect. All entries on
this tab are nontunable.

## Libraries

UAV Toolbox / Algorithms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Reduced-order model for UAV

The Guidance Model block represents a small unmanned aerial vehicle (UAV)
fixed-wing[1] and multirotor[2] guidance model that estimates
the UAV state based on control and environmental inputs. The model approximates the behavior
of a closed-loop system consisting of an autopilot controller and a fixed-wing or multirotor
kinematic model for 3-D motion. Use this block as a reduced-order guidance model to simulate
your fixed-wing or multirotor UAV. Specify the **ModelType** to select your
UAV type. Use the **Initial State** tab to specify the initial state of the
UAV depending on the model type. The **Configuration** tab defines the
control parameters and physical parameters of the UAV.
