---
type: simulink-block
title: 'Simulation 3D Physics Vehicle'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / 3D Environment Vehicles (requires Simulink 3D Animation)'
documentation_page: 'simulation3dphysicsvehicle'
documentation_source_path: 'ref/simulation3dphysicsvehicle.html'
language: en
---

# Simulation 3D Physics Vehicle

## Ports

### Input

### **SteerCmd** — Normalized steer angle scalar

Normalized steer angle, specified as a scalar. **SteerCmd**
corresponds to the minimum and maximum range of the steering angle as determined by
the **Front wheel max steer angle** and **Rear wheel max
steer angle** parameters, respectively.

### **AccelCmd** — Normalized vehicle acceleration scalar

Normalized acceleration torque request to the vehicle powertrain, specified as a
scalar. The exact response is characterized by the engine, transmission, and other
vehicle parameters.

### **DecelCmd** — Normalized vehicle deceleration scalar

Normalized deceleration torque request to the vehicle braking system, specified as
a scalar. The exact braking response is characterized by the engine, transmission and
other vehicle parameters.

### **GearCmd** — Gear input `1` | `-1` | `0`

Gear input, specified as either `1`, `-1`, or
`0`.

- `1` – Forward shift gear
- `-1` – Reverse gear
- `0` – Neutral gear

If you select manual shift mode, then the vehicle shifts according to the signal,
but the values listed still apply. Any input set that does not correspond to a valid
gear is ignored.
### Output

### **Info** — Bus signal bus

This port is optional.

Bus signal containing these block values.

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
| `DCM` | Direction cosine matrix | | | | Computed | rad |
| `Forces` | `Tires` | `FrntTires` | `Lft` | `Fx` | Front left tire force along the vehicle-fixed *x*-axis | Estimated | N |
| `Fy` | Front left tire force along the vehicle-fixed *y*-axis | Estimated | N |
| `Fz` | Front left tire force along the vehicle-fixed *z*-axis | Estimated | N |
| `Rght` | `Fx` | Front right tire force along the vehicle-fixed *x*-axis | Estimated | N |
| `Fy` | Front right tire force along the vehicle-fixed *y*-axis | Estimated | N |
| `Fz` | Front right tire force along the vehicle-fixed *z*-axis | Estimated | N |
| `RearTires` | `Lft` | `Fx` | Rear left tire force along the vehicle-fixed *x*-axis | Estimated | N |
| `Fy` | Rear left tire force along the vehicle-fixed *y*-axis | Estimated | N |
| `Fz` | Rear left tire force along the vehicle-fixed *z*-axis | Estimated | N |
| `Rght` | `Fx` | Rear right tire force along the vehicle-fixed *x*-axis | Estimated | N |
| `Fy` | Rear right tire force along the vehicle-fixed *y*-axis | Estimated | N |

**Note**

Tire forces are no longer explicitly available from Unreal Engine as a result of Epic Games® transition from PhysX® to Chaos Physics. The values calculated for the tire forces are
approximate estimates.

| Signal | | Description | Variable | Units |
| --- | --- | --- | --- | --- |
| `Mtr` | `MtrSpd` | Applied drive shaft angular speed input | *ωi* | RPM |
| `Trans` | `TransGearCmd` | Commanded gear | *Ncmd* | N/A |
| `TransGear` | Engaged gear | *N* | N/A |

### **xdot** — Vehicle longitudinal velocity `scalar`

Vehicle CG velocity along the vehicle-fixed *x*-axis, in
m/s.

### **ydot** — Vehicle lateral velocity `scalar`

Vehicle CG velocity along the vehicle-fixed *y*-axis, in
m/s.

### **psi** — Yaw `scalar`

Rotation of the vehicle-fixed frame about the earth-fixed
*Z*-axis (yaw), in rad.

### **r** — Yaw rate `scalar`

Vehicle angular velocity, `r`, about the vehicle-fixed
*z*-axis (yaw rate), in rad/s.

## Parameters

### Chassis

### **Type, PassVehMesh** — Type `Muscle car` (default) | `Sedan` | `Sport utility vehicle` | `Small pickup truck` | `Hatchback` | `Box truck` | `Custom`

Specify the vehicle type. This table provides
links to the vehicle dimensions.

| **Vehicle type** Setting | Vehicle Dimensions |
| --- | --- |
| `Muscle car` | Muscle Car |
| `Sedan` | Sedan |
| `Sport utility vehicle` | Sport Utility Vehicle |
| `Small pickup truck` | Small Pickup Truck |
| `Hatchback` | Hatchback |
| `Box truck` | Box Truck |

#### Dependencies

Selecting `Custom` enables parameters that allow you to import a
custom mesh for your vehicle.

### **Color, VehColor** — Color of vehicle `Red` (default) | `Orange` | `Yellow` | `Green` | `Blue` | `Black` | `White` | `Silver` | `Dazzle camouflage`

Select the color of the vehicle.

### **Name, ActorName** — Name of vehicle `SimulinkVehicle1` (default) | character vector

By default, when you use this block in your model, the block sets the
**Name** parameter to
`SimulinkVehicleX`. The value of
`X` depends on the number of
Simulation 3D Physics Vehicle and Simulation 3D
Vehicle blocks in your model.

### **Initial position [X, Y, Z], InitialPos [m]** — Vehicle initial position `[ 0, 0, -0.5]` (default) | 1-by-3 array

Initial vehicle position, specified as a 1-by-3 array, in m. Array elements are
values along the **Coordinate system** parameter
*X*-, *Y*-, and *Z*- axes,
respectively.

### **Initial rotation [Roll, Pitch, Yaw], InitialRot [rad]** — Vehicle initial rotation `[ 0, 0, 0 ]` (default) | 1-by-3 array

Initial vehicle rotation, specified as a 1-by-3 array, in rad. Array elements are
values about the **Coordinate system** parameter
*X*-, *Y*-, and *Z*-axes,
respectively.

### **Mass, Mass [kg]** — Vehicle mass `1500` (default) | scalar

Vehicle mass, in kg. This value does not include the wheel masses.

### **Center of mass offset vector, CgOffset [m]** — Offset in center of mass `[0, 0, 0]` (default) | three-element vector

Offset in center of mass, specified as a three-element vector, in meters.

### **Inertia tensor scaling vector, IvehScale []** — Scaling of inertia tensor `[1, 1, 1]` (default) | three-element vector

Scaling of inertia tensor, specified as a three-element dimensionless
vector.

### **Chassis height (used in drag), ChassisHeight [m]** — Height of chassis `1.0` (default) | scalar

Height of chassis used to calculate drag force, specified in meters.

### **Drag coefficient, Cd []** — Vehicle drag coefficient `0.3` (default) | scalar

Vehicle drag coefficient, dimensionless.

### **Drag lift coefficient, Cl []** — Longitudinal lift coefficient `0.1` (default) | scalar

Longitudinal lift coefficient, dimensionless.

### **Path to custom mesh, MeshPath** — Path to custom mesh character vector

Path to custom mesh file.

#### Dependencies

To enable this parameter, set **Type** to
`Custom`.

### **Track width, TrackWidth [m]** — Distance between wheels `1.9` (default) | scalar

The vehicle track width refers to the distance between the wheels, or the axle
length, specified in meters.

#### Dependencies

To enable this parameter, set **Type** to
`Custom`.

### **Wheel base in custom mesh [m]** — Wheel base in custom mesh `3` (default) | scalar

Wheel base, in meters.

#### Dependencies

To enable this parameter, set **Type** to
`Custom`.

### **Front Wheel radius, FrntWhlRadius [m]** — Front wheel radius `0.23` (default) | scalar

Front wheel radius, in meters.

#### Dependencies

To enable this parameter, set **Type** to
`Custom`.

### **Front wheel width, FrntWhlWidth [m]** — Front wheel width `0.20` (default) | scalar

Front wheel width, in meters.

#### Dependencies

To enable this parameter, set **Type** to
`Custom`.

### **Rear Wheel radius, RearWhlRadius [m]** — Rear wheel radius `0.23` (default) | scalar

Rear wheel radius, in meters.

#### Dependencies

To enable this parameter, set **Type** to
`Custom`.

### **Rear wheel width, RearWhlWidth [m]** — Rear wheel width `0.20` (default) | scalar

Rear wheel width, in meters.

#### Dependencies

To enable this parameter, set **Type** to
`Custom`.

### Powertrain and Driveline

#### Powertrain

### **Motor torque indices, TrqCrv [Nm]** — Motor torque indices `[ 75, 75, 97, 117, 152, 175, 175, 175, 175, 165, 155, 145, 140, 135, 125, 115, 50 ]` (default) | vector

Motor torque indices, in N·m. You can use these pre-transmission values to
represent either an electric motor or a conventional engine.

**Data Types:** `double`

### **Motor speed breakpoints, SpdCrv [rpm]** — Motor speed breakpoints `[ 0, 750, 1054, 1357, 1660, 1964, 2267, 2571, 2875, 3178, 3482, 3785, 4089, 4393, 4696, 5000, 7000 ]` (default) | vector

Motor speed breakpoints, in rpm.

**Data Types:** `double`

### **Maximum powertrain speed, MaxRPM [rpm]** — Maximum powertrain speed `7000` (default) | scalar

Max powertrain speed, in rpm. If you select an automatic transmission option, this
value also corresponds to the normalized shift points used in the upshift and
downshift logic.

**Data Types:** `double`

### **Powertrain rotational inertia, Jmot [kg\*m^2]** — Powertrain rotational inertia `1.0` (default) | scalar

Powertrain rotational inertia, in kg·m2.

**Data Types:** `double`

### **Powertrain damping at full torque request, bEngMax [Nms/rad]** — Powertrain damping at full torque request `0.15` (default) | scalar

Powertrain damping at full torque request, in
kg·m2/s.

**Data Types:** `double`

### **Powertrain damping at zero torque request in gear, bEngMin [Nms/rad]** — Powertrain damping at zero torque request in gear `2` (default) | scalar

Powertrain damping at zero torque request in gear, in
kg·m2/s.

**Data Types:** `double`

#### Driveline

### **Drivetrain type** — Drivetrain `Rear Wheel Drive` (default) | `Front Wheel Drive` | `All Wheel Drive`

Implement rear wheel, front wheel, or all wheel drive.

### **Front to rear torque split ratio, FrntRearSplit []** — Front to rear torque split ratio 0.5 (default) | scalar in the range (0,1)

Front to rear torque split ratio, dimensionless.

`1` indicates 100% torque to the front. `0`
indicates 100% to the rear.

#### Dependencies

To enable this parameter, set **Drivetrain type** to
`All Wheel Drive`.

### **Transmission type** — Transmission `Automatic` (default) | `Manual`

Implement an automatic or manual transmission.

**Note**

You must provide a **GearCmd** input even if
**Transmission type** is set to
`Automatic`.

### **Gear number vector, G []** — Gear number `[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]` (default) | vector

Gear number vector, dimensionless.

**Data Types:** `double`

### **Gear ratio vector, N []** — Gear ratios `[ -3.5, 1, 4.75, 3.75, 3.25, 2.75, 2.25, 1.5, 1, 0.75 ]` (default) | vector

Gear ratios, dimensionless.

**Note**

You must provide at least one negative ratio for reverse gear. You must also
provide a neutral ratio where the length of the array corresponds to the number of
forward gears plus two, one for reverse and one for neutral.

**Data Types:** `double`

### **Upshift speed, UpShiftRPM [rpm]** — Upshift speed 4000 (default) | scalar greater than `DownShiftRPM`

Upshift speed, in rpm.

### **Downshift speed, DownShiftRPM [rpm]** — Downshift speed 2000 (default) | scalar in the range [0, `UpShiftRPM`)

Downshift speed, in rpm.

### **Minimum (idle) speed, MinRPM [rpm]** — Minimum powertrain speed `750` (default) | scalar in the range [`0`, `MaxRPM`]

Minimum powertrain speed, in rpm.

### **Shift time, tShift [s]** — Time taken to complete shift `0.1` (default) | scalar

Time taken to complete a shift, specified as a scalar, in s.

**Data Types:** `double`

### **Final drive ratio, NDiff []** — Final drive ratio `3.2` (default) | scalar

Final drive ratio, dimensionless. This value is the post transmission ratio,
typically found in a differential or final drive gearbox.

**Data Types:** `double`

### **Transmission efficiency, eta []** — Efficiency factor 0.94 (default) | scalar in the range [0,1)

Efficiency factor, dimensionless.

### Steering and Brakes

#### Steering

### **Steering type** — Option to set steering type `Ackermann` (default) | `Linear`

Steering type, specified as `Ackermann` or
`Linear`.

### **Outside to inside steering ratio, SteerAngleRatio []** — Outside to inside steer angle ratio 1.0 (default) | scalar

Outside to inside steer angle ratio, dimensionless.

#### Dependencies

To enable this parameter, set **Steering type** to
`Linear`.

### **Front wheel max steer angle, FrntWhlMaxSteer [rad]** — Front wheel max steer angle `45*pi/180` (default) | scalar

Front wheel max steer angle, in radians. This value is the absolute angle which
the front wheels turn with a `-1` or `1` steer
command input signal.

**Data Types:** `double`

### **Rear wheel max steer angle, RearWhlMaxSteer [rad]** — Rear wheel max steer angle 0 (default) | scalar

Rear wheel max steer angle, in radians. This value is the absolute angle which the
rear wheels turn with a `-1` or `1` steer command
input signal.

**Data Types:** `double`

### **Maximum steering ratio breakpoints, SteerCrv []** — Maximum steering ratio `[ 1, 0.8, 0.7 ]` (default) | vector

Maximum steering ratio breakpoints, dimensionless. This value is the gain by which
the steering command is affected by the vehicle speed brake points.

**Data Types:** `double`

### **Steering ratio speed breakpoints, SteerSpdCrv [m/s]** — Steering ratio speed breakpoints `[ 0, 60, 120 ]./3.6` (default) | vector

Steering ratio speed breakpoints, in m/s. This value is the vehicle forward speed
break points used by the steer ratio gains.

**Data Types:** `double`

#### Brakes

### **Maximum front wheel torque, FrntWhlMaxTrq [Nm]** — Maximum front wheel torque `1500` (default) | scalar

Maximum front wheel torque, in N·m. This value is the maximum braking torque
applied to the front wheels corresponding to the normalized
**DecelCmd** input.

**Data Types:** `double`

### **Maximum rear wheel torque, RearWhlMaxTrq [Nm]** — Maximum rear wheel torque `1500` (default) | scalar

Maximum rear wheel torque, in N·m. This value is the maximum braking torque
applied to the rear wheels corresponding to the normalized
**DecelCmd** input.

**Data Types:** `double`

### **Option to enable handbrake input** — Enable handbrake input `off` (default) | `on`

Select this parameter to enable handbrake input.

**Data Types:** `Boolean`

### **Front wheels affected by handbrake** — Handbrake option for front wheels `off` (default) | `on`

Enable this parameter to have the handbrake affect the front wheels.

#### Dependencies

To enable this parameter, select **Enable handbrake
input**.

**Data Types:** `Boolean`

### **Rear wheels affected by handbrake** — Handbrake option for rear wheels `off` (default) | `on`

Enable this parameter to have the handbrake affect the rear wheels.

#### Dependencies

To enable this parameter, select **Enable handbrake
input**.

**Data Types:** `Boolean`

### **Maximum front wheel hand brake torque, FrntWhlMaxHndBrkTrq [Nm]** — Maximum front wheel hand brake torque `3000` (default) | scalar

Maximum front wheel hand brake torque, in Nm.

#### Dependencies

To enable this parameter, select **Front wheels affected by
handbrake**.

### **Maximum rear wheel hand brake torque, RearWhlMaxHndBrkTrq [Nm]** — Maximum rear wheel hand brake torque `3000` (default) | scalar

Maximum rear wheel hand brake torque, in Nm.

#### Dependencies

To enable this parameter, select **Front wheels affected by
handbrake**.

### Suspension, Wheels and Tires

#### Suspension

### **Front suspension force offset location, FrntSuspFOffset [m]** — Front suspension force offset `[0,0,0]` (default) | three-element vector

Front suspension force offset, specified as a three-element vector, in
meters.

### **Maximum front suspension compression (jounce), FrntSuspMaxComp [m]** — Maximum front suspension compression `0.15` (default) | scalar

Maximum front suspension compression or jounce, specified as a scalar, in meters.
Jounce is the upward movement or compression of suspension components.

### **Front spring preload, FrntSpringPreload [N]** — Front suspension preload force `200` (default) | scalar

Front suspension preload force, in N.

### **Front spring stiffness, FrntSpringRate [N/m]** — Front suspension spring rate `30e3` (default) | scalar

Front suspension spring rate, in N/m.

### **Maximum front suspension extension (rebound), FrntSuspMaxExt [m]** — Maximum front suspension extension `0.1` (default) | scalar

Maximum front suspension extension or rebound, specified as a scalar in meters.
Rebound is the downward movement or extension of suspension components.

### **Front suspension damping ratio, FrntSuspDamping []** — Damping ratio of front suspension `0.5` (default) | scalar

Damping ratio of front suspension, dimensionless. Damping ratio is the coefficient
of the damper at its peak level, where the vehicle is in a completely stable
state.

### **Front roll bar stiffness scaling, FrntRollbarScaling []** — Front anti-roll effect 0.15 (default) | scalar in the range (0,1)

Front anti-roll effect, dimensionless.

### **Rear suspension force offset location, RearSuspFOffset [m]** — Rear suspension force offset `[0,0,0]` (default) | three-element vector

Rear suspension force offset, specified as a three-element vector, in
meters.

### **Maximum rear suspension compression (jounce), RearSuspMaxComp [m]** — Maximum rear suspension compression `0.15` (default) | scalar

Maximum rear suspension compression or jounce, specified as a scalar, in meters.
Jounce is the upward movement or compression of suspension components.

### **Rear spring preload, RearSpringPreload [N]** — Rear suspension preload force `200` (default) | scalar

Rear suspension preload force, in N.

### **Rear spring stiffness, RearSpringRate [N/m]** — Rear suspension spring rate `30e3` (default) | scalar

Rear suspension spring rate, in N/m.

### **Maximum rear suspension extension (rebound), RearSuspMaxExt [m]** — Maximum rear suspension extension `0.1` (default) | scalar

Maximum rear suspension extension or rebound, specified as a scalar, in meters.
Rebound is the downward movement or extension of suspension components.

### **Rear suspension damping ratio, RearSuspDamping []** — Damping ratio of rear suspension `0.5` (default) | scalar

Damping ratio of rear suspension, dimensionless. Damping ratio is the coefficient
of the damper at its peak level, where the vehicle is in a completely stable
state.

### **Rear roll bar stiffness scaling, RearRollbarScaling []** — Rear anti-roll effect 0.15 (default) | scalar in the range (0,1)

Rear anti-roll effect, dimensionless.

#### Wheels

### **Enable anti-lock braking** — Option to enable anti-lock braking `off` (default) | `on`

Select this parameter to enable anti-lock braking.

**Data Types:** `Boolean`

### **Enable traction control** — Option to enable traction control `off` (default) | `on`

Select this parameter to enable traction control.

**Data Types:** `Boolean`

#### Tires

### **Front wheel corner stiffness, Cy\_f [N/rad]** — Front cornering stiffness `70e3` (default) | scalar

Front cornering stiffness, in N/rad.

### **Front wheel slip modifier, FrntSideSlipModifier []** — Front slip modifier `20` (default) | scalar in the range (0,1)

Front slip modifier, dimensionless.

### **Rear wheel corner stiffness, Cy\_r [N/rad]** — Rear cornering stiffness `70e3` (default) | scalar

Rear cornering stiffness, in N/rad.

### **Rear wheel slip modifier, RearSideSlipModifier []** — Rear slip modifier `20` (default) | scalar in the range (0,1)

Rear slip modifier, dimensionless.

### **Friction scaling factor, lambda\_mu []** — Friction scaling `1.0` (default) | scalar

Nominal friction scale, dimensionless.

**Data Types:** `double`

### Light Controls

### **Enable light controls** — Option to control vehicle lights `off` (default) | `on`

Select whether to control the vehicle headlights. Use the enabled parameters
to set the light parameters, including headlight intensity.

#### Dependencies

Selecting this parameter:

- Creates the input port `Light
  controls`.
- Enables these light parameters.

  | Lights | Light Parameters |
  | --- | --- |
  | **Headlights** | - **Headlight color** - **High beam   intensity** - **Low beam   intensity** - **High beam cone half   angle** - **Low beam cone half   angle** - **Left headlight beam   orientation** - **Right headlight beam   orientation** |
  | **Brake lights** | **Brake light intensity** |
  | **Reverse lights** | **Reverse light intensity** |
  | **Turn signal lights** | - **Turn signal light   intensity** - **Period** - **Pulse width** |

#### Headlights

### **Headlight color [R,G,B], HeadlightColor** — Headlight color `[1,1,1]` (default) | 1-by-3 vector of RGB triplet values

Headlight color, specified as a normalized 1-by-3 vector of RGB triplet
values.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `int8` | `uint8`

### **High beam intensity, HighBeamIntensity** — High beam intensity `100000` (default) | positive scalar

High beam intensity, in cd.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **Low beam intensity, LowBeamIntensity** — Low beam intensity `60000` (default) | positive scalar

Low beam intensity, in cd.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **High beam cone half angle, HighBeamConeAngle** — High beam cone half angle `1.22` (default) | positive scalar less than pi/2

High beam cone half angle, in rad.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **Low beam cone half angle, LowBeamConeAngle** — Low beam cone half angle `1.22` (default) | positive scalar less than pi/2

Low beam cone half angle, in rad.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **Left headlight beam orientation [Pitch, Yaw], LeftHeadlightOrientation** — Left headlight beam orientation `[0,0]` (default) | 1-by-2 vector with values between -pi and pi

Pitch and yaw orientation of the left headlight beam orientation in the
*Z*-down coordinate system, specified as a 1-by-2 vector,
in rad. The first element of the vector, `[1,1]`, is the pitch
angle. The second element of the vector, `[1,2]`, is the yaw
angle.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **Right headlight beam orientation [Pitch, Yaw], RightHeadlightOrientation** — Right headlight beam orientation `[0,0]` (default) | 1-by-2 vector with values between -pi and pi

Pitch and yaw orientation of the right headlight beam orientation in the
*Z*-down coordinate system, specified as a 1-by-2 vector,
in rad. The first element of the vector, `[1,1]`, is the pitch
angle. The second element of the vector, `[1,2]`, is the yaw
angle.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

#### Brake Lights

### **Brake light intensity, BrakelightIntensity** — Brake light intensity `500` (default) | positive scalar

Brake light intensity, in cd/m^2.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

#### Reverse Lights

### **Reverse light intensity, ReverselightIntensity** — Reverse light intensity `500` (default) | positive scalar

Reverse light intensity, in cd/m^2.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

#### Turn Signal Lights

### **Turn signal light intensity, SignallightIntensity** — Turn signal light intensity `500` (default) | positive scalar

Turn signal light intensity, in cd/m^2.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **Period, SignallightPeriod** — Turn signal light period `1` (default) | positive scalar

Turn signal light period, in s.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **Pulse width, SignalPulseWidth** — Pulse width `50` (default) | positive scalar less than 100

Turn signal light pulse width, specified as a percent of the period.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### Sample Time

### **Sample time, SampleTime** — Sample time `-1` (default) | `scalar`

Sample time, *Ts*. The graphics frame
rate is the inverse of the sample time.

### Ground Truth

### **Output location and orientation** — Option to return location and orientation `off` (default) | `on`

Select this parameter to return location and orientation.

**Data Types:** `Boolean`

### **Output nominal vehicle state feedback** — Option to return nominal vehicle state feedback `off` (default) | `on`

Select this parameter to return nominal vehicle state feedback.

**Data Types:** `Boolean`

## Libraries

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

### R2024b: New Simulation 3D Physics Vehicle block color option

Starting in R2024b, you can specify **Color, VehColor** as
`Dazzle Camouflage` for the Simulation 3D Physics
Vehicle block.

### R2024a: Requires Simulink 3D Animation

Simulating models with the Simulation 3D Physics Vehicle block requires
Simulink
3D Animation.

### R2024a: Transition from PhysX to Chaos Physics

Starting in R2024a, the Unreal Engine version that ships with Simulink
3D Animation uses Chaos Physics instead of the
PhysX physics engine. As a result of this change, a number of parameters have been
removed and added.

This table lists the parameters that have been removed.

| Vehicle Element | Removed Parameter |
| --- | --- |
| **Powertrain** | **Powertrain damping at zero torque request, in neutral** |
| **Driveline** | **Shift down indices** |
| **Shift up indices** |
| **Clutch slip torque** |
| **Minimum shift latency** |
| **Steering** | **Percent Ackermann** |
| **Suspension** | **Front suspension natural frequency** |
| **Rear suspension natural frequency** |
| **Wheels** | **Front wheel mass** |
| **Rear wheel mass** |
| **Front wheel damping** |
| **Rear wheel damping** |
| **Tires** | **Front tire lateral stiffness** |
| **Rear tire lateral stiffness** |
| **Front tire longitudinal stiffness** |
| **Rear tire longitudinal stiffness** |
| **Front tire max lateral stiffness factor** |
| **Rear tire max lateral stiffness factor** |

This table lists the parameters that have been added.

| Vehicle Element | Added Parameter |
| --- | --- |
| **Chassis** | **Drag lift coefficient** |
| **Front wheel width** |
| **Rear wheel width** |
| **Powertrain** | **Minimum (idle) speed** |
| **Driveline** | **Downshift speed** |
| **Upshift speed** |
| **Transmission efficiency** |
| **Steering** | **Steer type** |
| **Outside to inside steering ratio** |
| **Suspension** | **Front spring stiffness** |
| **Front spring preload** |
| **Rear spring stiffness** |
| **Rear spring preload** |
| **Front roll bar stiffness scaling** |
| **Rear roll bar stiffness scaling** |
| **Wheels** | **Enable anti-lock braking** |
| **Enable traction control** |
| **Tires** | **Front wheel corner stiffness** |
| **Front wheel slip modifier** |
| **Rear wheel corner stiffness** |
| **Rear wheel slip modifier** |

### R2023a: Compatible with Unreal Engine 4.27

The Simulation 3D Physics Vehicle block is compatible with Unreal Engine 4.27. Support for future releases of Unreal Engine may require changes to block parameters, including driveline dynamics, shift
scheduling, and tire parameters.

## Description

Implement controllable 6DOF vehicle 3D environment

**Note**

Simulating models with the Simulation 3D Physics Vehicle block requires
Simulink®
3D Animation™.

The Simulation 3D Physics Vehicle block implements a controllable 10DOF
vehicle in the 3D simulation environment, with a vertical DOF for each wheel and 6DOF for the
chassis.

To use the Simulation 3D Physics Vehicle block, ensure that the
Simulation 3D Scene Configuration block is in your model. If you set the
**Sample time** parameter of the Simulation 3D Physics Vehicle block to
`-1`, the block uses the sample time specified in the Simulation 3D
Scene Configuration block.

The block input uses the vehicle *Z*-down
*right-handed* (RH) *Cartesian* coordinate system
defined in SAE J670[1]. The
coordinate system is inertial and initially aligned with the vehicle geometric center:

- *X*-axis — Along vehicle longitudinal axis, points forward
- *Y*-axis — Along vehicle lateral axis, points to the right
- *Z*-axis — Points downward

**Tip**

Verify that the Simulation 3D Scene
Configuration block executes before the Simulation 3D Physics
Vehicle block. With this sequence, the Unreal Engine® 3D visualization environment prepares the data before the Simulation 3D
Physics Vehicle block receives the data. To check the block execution order,
right-click the blocks and select **Properties**. On the
**General** tab, confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Physics Vehicle — `-1`

For more information about execution order, see Control and Display Execution Order.
