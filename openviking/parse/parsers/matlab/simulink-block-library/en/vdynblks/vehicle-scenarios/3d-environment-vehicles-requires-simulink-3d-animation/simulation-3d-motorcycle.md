---
type: simulink-block
title: 'Simulation 3D Motorcycle'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / 3D Environment Vehicles (requires Simulink 3D Animation)'
documentation_page: 'simulation3dmotorcycle'
documentation_source_path: 'ref/simulation3dmotorcycle.html'
language: en
---

# Simulation 3D Motorcycle

## Ports

### Input

### **Translation** — Motorcycle translation `4`-by-`3` array

Motorcycle and component translation, in m. Array dimensions are
`4`-by-`3`.

- `Translation(1,1)`, `Translation(1,2)`,
  and `Translation(1,3)` — Motorcycle translation along the
  inertial vehicle Z-down *X*-, *Y*-, and
  *Z*- axes, respectively.
- `Translation(...,1)`,
  `Translation(...,2)`, and `Translation(...,3)`
  — Motorcycle component translation relative to vehicle, along the vehicle Z-down
  *X*-, *Y*-, and *Z*-
  axes, respectively.

The signal contains translation information according to the locations.

Translation=[XvYvZvXHYHZHXFYFZFXRYRZR]

| Translation | Array Element | Translation Axis |
| --- | --- | --- |
| Motorcycle, *Xv* | `Translation(1,1)` | Inertial vehicle Z-down *X*-axis |
| Motorcycle, *Yv* | `Translation(1,2)` | Inertial vehicle Z-down *Y*-axis |
| Motorcycle, *Zv* | `Translation(1,3)` | Inertial vehicle Z-down *Z*-axis |
| Handlebars, *XH* | `Translation(2,1)` | Vehicle Z-down *X*-axis |
| Handlebars, *YH* | `Translation(2,2)` | Vehicle Z-down *Y*-axis |
| Handlebars, *ZH* | `Translation(2,3)` | Vehicle Z-down *Z*-axis |
| Front wheel, *XF* | `Translation(3,1)` | Vehicle Z-down *X*-axis |
| Front wheel, *YF* | `Translation(3,2)` | Vehicle Z-down *Y*-axis |
| Front wheel, *ZF* | `Translation(3,3)` | Vehicle Z-down *Z*-axis |
| Rear wheel, *XR* | `Translation(4,1)` | Vehicle Z-down *X*-axis |
| Rear wheel, *YR* | `Translation(4,2)` | Vehicle Z-down *Y*-axis |
| Rear wheel, *ZR* | `Translation(4,3)` | Vehicle Z-down *Z*-axis |

### **Rotation** — Motorcycle rotation `4`-by-`3` array

Vehicle and component rotation, in rad. Array dimensions are
`4`-by-`3`.

- `Rotation(1,1)`, `Rotation(1,2)`, and
  `Rotation(1,3)` — Motorcycle rotation about the inertial
  vehicle Z-down *X*-, *Y*-, and
  *Z*- axes, respectively.
- `Rotation(...,1)`, `Rotation(...,2)`, and
  `Rotation(...,3)` — Motorcycle component rotation relative to
  vehicle, about the vehicle Z-down *X*-,
  *Y*-, and *Z*- axes,
  respectively.

The signal contains rotation information according to the locations.

Rotation=[RollvPitchvYawvRollHPitchHYawHRollFPitchFYawFRollRPitchRYawR]

| Rotation | Array Element | Rotation Axis |
| --- | --- | --- |
| Vehicle, *Rollv* | `Rotation(1,1)` | Inertial vehicle Z-down *X*-axis |
| Vehicle, *Pitchv* | `Rotation(1,2)` | Inertial vehicle Z-down *Y*-axis |
| Vehicle, *Yawv* | `Rotation(1,3)` | Inertial vehicle Z-down *Z*-axis |
| Handlebar, *RollH* | `Rotation(2,1)` | Vehicle Z-down *X*-axis |
| Handlebar, *PitchH* | `Rotation(2,2)` | Vehicle Z-down *Y*-axis |
| Handlebar, *YawH* | `Rotation(2,3)` | Vehicle Z-down *Z*-axis |
| Front wheel, *RollF* | `Rotation(3,1)` | Vehicle Z-down *X*-axis |
| Front wheel, *PitchF* | `Rotation(3,2)` | Vehicle Z-down *Y*-axis |
| Front wheel, *YawF* | `Rotation(3,3)` | Vehicle Z-down *Z*-axis |
| Rear wheel, *RollR* | `Rotation(4,1)` | Vehicle Z-down *X*-axis |
| Rear wheel, *PitchR* | `Rotation(4,2)` | Vehicle Z-down *Y*-axis |
| Rear wheel, *YawR* | `Rotation(4,3)` | Vehicle Z-down *Z*-axis |

### **Light controls** — Vehicle lights on or off 1-by-5 vector

Light controls input signal, specified as a 1-by-5 Boolean vector. Each element of
the vector turns a specific vehicle light on or off, as indicated in this table. A
value of 1 turns the light on; a value of 0 turns the light off.

| Vector Element | Vehicle Light |
| --- | --- |
| (1,1) | Headlight high beam |
| (1,2) | Headlight low beam |
| (1,3) | Brake |
| (1,4) | Left signal |
| (1,5) | Right signal |

#### Dependencies

To create this port, on the **Light Controls** tab, select
**Enable light controls**.

**Data Types:** `Boolean`

## Parameters

### Vehicle Parameters

### **Type** — Type `Sports bike` (default) | `Motor bike` | `Scooter`

Use the **Type** parameter to
specify the motorcycle type. This table provides links to the motorcycle
dimensions.

| Setting | Vehicle Dimensions |
| --- | --- |
| `Sports bike` | Sports Bike |
| `Motor bike` | Motor Bike |
| `Scooter` | Scooter |

### **Color** — Color of vehicle `Red` (default) | `Orange` | `Yellow` | `Green` | `Blue` | `Black` | `White` | `Silver` | `Dazzle Camouflage`

Select the color of the vehicle.

### **Name** — Name of motorcycle `SimulinkVehicle1` (default) | character vector

Name of motorcycle. By default, when you use the block in your model, the block
sets the **Name** parameter to
`SimulinkVehicleX`. The value of
`X` depends on the number of 3D
simulation blocks that you have in your model.

### **Sample time** — Sample time `-1` (default) | `scalar`

Sample time, *Ts*. The
graphics frame rate is the inverse of the sample
time.

### Light Controls

### **Enable light controls, VehLightsControl** — Control vehicle lights `off` (default) | `on`

Select whether to control the vehicle headlights. Use the enabled parameters to
set the light parameters, including headlight intensity.

#### Dependencies

Selecting this parameter:

- Creates the input port `Light controls`
- Enables these light parameters.

  | Lights | Light Parameters |
  | --- | --- |
  | **Headlights** | - **Headlight color** - **High beam intensity** - **Low beam intensity** - **High beam cone half angle** - **Low beam cone half angle** - **Left headlight beam   orientation** - **Right headlight beam   orientation** |
  | **Brake lights** | **Brake light intensity** |
  | **Turn signal lights** | - **Turn signal light intensity** - **Period** - **Pulse width** |

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

### **Left headlight beam orientation [Pitch, Yaw], LeftHeadlightOrientation** — Left headlight beam orientation `[0,0]` (default) | 1-by-2 vector greater with values between -pi and pi

Pitch and yaw orientation of the left headlight beam orientation in the
*Z*-down coordinate system, specified as a 1-by-2 vector, in rad.
The first element of the vector, `[1,1]`, is the pitch angle. The
second element of the vector, `[1,2]` is the yaw angle.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **Right headlight beam orientation [Pitch, Yaw], RightHeadlightOrientation** — Right headlight beam orientation `[0,0]` (default) | 1-by-2 vector greater with values between -pi and pi

Pitch and yaw orientation of the right headlight beam orientation in the
*Z*-down coordinate system, specified as a 1-by-2 vector, in rad.
The first element of the vector, `[1,1]`, is the pitch angle. The
second element of the vector, `[1,2]` is the yaw angle.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

#### Brake Lights

### **Brake light intensity, BrakelightIntensity** — Intensity `500` (default) | positive scalar

Brake light intensity, in cd/m^2.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

#### Turn Signal Lights

### **Turn signal light intensity, SignallightIntensity** — Intensity `500` (default) | positive scalar

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

Turn signal light pulse width, as a percent of the period.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### Initial Values

### **Initial array values to translate vehicle per part, Translation** — Motorcycle initial translation zeros( 4, 3 ) (default) | `4`-by-`3` array

Initial motorcycle and component translation, in m. Array dimensions are
`5`-by-`3`.

- `Translation(1,1)`, `Translation(1,2)`,
  and `Translation(1,3)` — Initial vehicle translation along the
  inertial vehicle Z-down coordinate system *X*-,
  *Y*-, and *Z*- axes,
  respectively.
- `Translation(...,1)`,
  `Translation(...,2)`, and `Translation(...,3)`
  — Initial motorcycle component translation relative to vehicle, along the
  vehicle Z-down *X*-, *Y*-, and
  *Z*- axes, respectively.

The parameter contains translation information according to the locations.

Translation=[XvYvZvXHYHZHXFYFZFXRYRZR]

| Translation | Array Element | Translation Axis |
| --- | --- | --- |
| Motorcycle, *Xv* | `Translation(1,1)` | Inertial vehicle Z-down *X*-axis |
| Motorcycle, *Yv* | `Translation(1,2)` | Inertial vehicle Z-down *Y*-axis |
| Motorcycle, *Zv* | `Translation(1,3)` | Inertial vehicle Z-down *Z*-axis |
| Handlebars, *XH* | `Translation(2,1)` | Vehicle Z-down *X*-axis |
| Handlebars, *YH* | `Translation(2,2)` | Vehicle Z-down *Y*-axis |
| Handlebars, *ZH* | `Translation(2,3)` | Vehicle Z-down *Z*-axis |
| Front wheel, *XF* | `Translation(3,1)` | Vehicle Z-down *X*-axis |
| Front wheel, *YF* | `Translation(3,2)` | Vehicle Z-down *Y*-axis |
| Front wheel, *ZF* | `Translation(3,3)` | Vehicle Z-down *Z*-axis |
| Rear wheel, *XR* | `Translation(4,1)` | Vehicle Z-down *X*-axis |
| Rear wheel, *YR* | `Translation(4,2)` | Vehicle Z-down *Y*-axis |
| Rear wheel, *ZR* | `Translation(4,3)` | Vehicle Z-down *Z*-axis |

### **Initial array values to rotate vehicle per part, Rotation** — Motorcycle initial rotation zeros( 4, 3 ) (default) | `4`-by-`3` array

Initial motorcycle and component rotation, about the vehicle Z-down
*X*-, *Y*-, and *Z*-
axes.

Array dimensions are `5`-by-`3`.

- `Rotation(1,1)`, `Rotation(1,2)`, and
  `Rotation(1,3)` — Initial motorcycle rotation about the
  inertial vehicle Z-down coordinate system*X*-,
  *Y*-, and *Z*- axes,
  respectively.
- `Rotation(...,1)`, `Rotation(...,2)`, and
  `Rotation(...,3)` — Initial motorcycle component rotation
  relative to vehicle, about the vehicle Z-down *X*-,
  *Y*-, and *Z*- axes,
  respectively.

The parameter contains rotation information according to the location.

Rotation=[RollvPitchvYawvRollHPitchHYawHRollFPitchFYawFRollRPitchRYawR]

| Rotation | Array Element | Rotation Axis |
| --- | --- | --- |
| Vehicle, *Rollv* | `Rotation(1,1)` | Inertial vehicle Z-down *X*-axis |
| Vehicle, *Pitchv* | `Rotation(1,2)` | Inertial vehicle Z-down *Y*-axis |
| Vehicle, *Yawv* | `Rotation(1,3)` | Inertial vehicle Z-down *Z*-axis |
| Handlebar, *RollH* | `Rotation(2,1)` | Vehicle Z-down *X*-axis |
| Handlebar, *PitchH* | `Rotation(2,2)` | Vehicle Z-down *Y*-axis |
| Handlebar, *YawH* | `Rotation(2,3)` | Vehicle Z-down *Z*-axis |
| Front wheel, *RollF* | `Rotation(3,1)` | Vehicle Z-down *X*-axis |
| Front wheel, *PitchF* | `Rotation(3,2)` | Vehicle Z-down *Y*-axis |
| Front wheel, *YawF* | `Rotation(3,3)` | Vehicle Z-down *Z*-axis |
| Rear wheel, *RollR* | `Rotation(4,1)` | Vehicle Z-down *X*-axis |
| Rear wheel, *PitchR* | `Rotation(4,2)` | Vehicle Z-down *Y*-axis |
| Rear wheel, *YawR* | `Rotation(4,3)` | Vehicle Z-down *Z*-axis |

## Libraries

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

### R2024b: New Simulation 3D Motorcycle block color option

Starting in R2024b, you can specify **Color, VehColor** as
`Dazzle Camouflage` for the Simulation 3D
Motorcycle block.

### R2024a: Requires Simulink 3D Animation

Simulating models with the Simulation 3D Motorcycle block requires
Simulink
3D Animation.

## Description

Implement motorcycle in 3D environment

**Note**

Simulating models with the Simulation 3D Motorcycle block requires
Simulink®
3D Animation™.

The Simulation 3D Motorcycle block implements a motorcycle with two wheels
in the 3D simulation environment.

To use this block, ensure that the Simulation 3D Scene Configuration block
is in your model. If you set the **Sample time** parameter of this block to
`-1`, the block uses the sample time specified in the Simulation 3D
Scene Configuration block.

The block input uses the vehicle Z-down *right-handed* (RH)
*Cartesian* coordinate system defined in SAE
J6701. The coordinate system is inertial and initially aligned
with the vehicle geometric center:

- *X*-axis — Along vehicle longitudinal axis, points forward
- *Y*-axis — Along vehicle lateral axis, points to the right
- *Z*-axis — Points downward

**Tip**

Verify that the Simulation 3D Motorcycle
block executes before the Simulation 3D Scene Configuration block. That way,
Simulation 3D Motorcycle prepares the signal data before the Unreal Engine® 3D visualization environment receives it. To check the block execution order,
right-click each block and select **Properties**. On the
**General** tab, confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Motorcycle — `-1`

For more information about execution order, see Control and Display Execution Order.
