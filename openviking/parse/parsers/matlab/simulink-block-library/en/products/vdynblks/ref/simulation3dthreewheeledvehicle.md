---
type: simulink-block
title: 'Simulation 3D Three-Wheeled Vehicle'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / 3D Environment Vehicles (requires Simulink 3D Animation)'
documentation_page: 'simulation3dthreewheeledvehicle'
documentation_source_path: 'ref/simulation3dthreewheeledvehicle.html'
language: en
---

# Simulation 3D Three-Wheeled Vehicle

## Ports

### Input

### **Translation** — Vehicle translation 5-by-3 array

Vehicle and wheel translation, in m. Array dimensions are 5-by-3.

- `Translation(1,1)`,
  `Translation(1,2)`, and
  `Translation(1,3)` — Vehicle
  translation along the inertial vehicle
  *Z*-down *X*-,
  *Y*-, and *Z*-
  axes, respectively.
- `Translation(...,1)`,
  `Translation(...,2)`, and
  `Translation(...,3)` — Wheel
  translation relative to vehicle, along the vehicle
  *Z*-down *X*-,
  *Y*-, and *Z*-
  axes, respectively.

The signal contains translation information according to the axle and
wheel locations.

Translation=[XvYvZvXHYHZHXFYFZFXRLYRLZRLXRRYRRZRR]

| Translation | Array Element | Translation Axis |
| --- | --- | --- |
| Vehicle, *Xv* | `Translation(1,1)` | Inertial vehicle *Z*-down *X*-axis |
| Vehicle, *Yv* | `Translation(1,2)` | Inertial vehicle *Z*-down *Y*-axis |
| Vehicle, *Zv* | `Translation(1,3)` | Inertial vehicle *Z*-down *Z*-axis |
| Handlebars, *XH* | `Translation(2,1)` | Inertial vehicle *Z*-down *X*-axis |
| Handlebars, *YH* | `Translation(2,2)` | Inertial vehicle *Z*-down *Y*-axis |
| Handlebars, *ZH* | `Translation(2,3)` | Inertial vehicle *Z*-down *Z*-axis |
| Front wheel, *XF* | `Translation(3,1)` | Vehicle *Z*-down *X*-axis |
| Front wheel, *YF* | `Translation(3,2)` | Vehicle *Z*-down *Y*-axis |
| Front wheel, *ZF* | `Translation(3,3)` | Vehicle *Z*-down *Z*-axis |
| Rear left wheel, *XRL* | `Translation(4,1)` | Vehicle *Z*-down *X*-axis |
| Rear left wheel, *YRL* | `Translation(4,2)` | Vehicle *Z*-down *Y*-axis |
| Rear left wheel, *ZRL* | `Translation(4,3)` | Vehicle *Z*-down *Z*-axis |
| Rear right wheel, *XRR* | `Translation(5,1)` | Vehicle *Z*-down *X*-axis |
| Rear right wheel, *YRR* | `Translation(5,2)` | Vehicle *Z*-down *Y*-axis |
| Rear right wheel, *ZRR* | `Translation(5,3)` | Vehicle *Z*-down *Z*-axis |

### **Rotation** — Vehicle rotation 5-by-3 array

Vehicle and wheel rotation, in rad. Array dimensions are 5-by-3.

- `Rotation(1,1)`,
  `Rotation(1,2)`, and
  `Rotation(1,3)` — Vehicle rotation
  about the inertial vehicle *Z*-down
  *X*-, *Y*-, and
  *Z*- axes, respectively.
- `Rotation(...,1)`,
  `Rotation(...,2)`, and
  `Rotation(...,3)` — Wheel rotation
  relative to vehicle, about the vehicle
  *Z*-down *X*-,
  *Y*-, and *Z*-
  axes, respectively.

**Note**

If the yaw value provided for the front wheel differs from the
yaw value provided for the handlebars, the yaw value of the
handlebars is used for the front wheel. The yaw value of the
handlebars and the front wheel is limited to the range of [-30,
30] degrees.

The signal contains rotation information according to the axle and
wheel locations.

Rotation=[RollvPitchvYawvRollHPitchHYawHRollFPitchFYawFRollRLPitchRLYawRLRollRRPitchRRYawRR]

| Rotation | Array Element | Rotation Axis |
| --- | --- | --- |
| Vehicle, *Rollv* | `Rotation(1,1)` | Inertial vehicle *Z*-down *X*-axis |
| Vehicle, *Pitchv* | `Rotation(1,2)` | Inertial vehicle *Z*-down *Y*-axis |
| Vehicle, *Yawv* | `Rotation(1,3)` | Inertial vehicle *Z*-down *Z*-axis |
| Handlebars, *RollH* | `Rotation(2,1)` | Inertial vehicle *Z*-down *X*-axis |
| Handlebars, *PitchH* | `Rotation(2,2)` | Inertial vehicle *Z*-down *Y*-axis |
| Handlebars, *YawH* | `Rotation(2,3)` | Inertial vehicle *Z*-down *Z*-axis |
| Front wheel, *RollF* | `Rotation(3,1)` | Vehicle *Z*-down *X*-axis |
| Front wheel, *PitchF* | `Rotation(3,2)` | Vehicle *Z*-down *Y*-axis |
| Front wheel, *YawF* | `Rotation(3,3)` | Vehicle *Z*-down *Z*-axis |
| Rear left wheel, *RollRL* | `Rotation(4,1)` | Vehicle *Z*-down *X*-axis |
| Rear left wheel, *PitchRL* | `Rotation(4,2)` | Vehicle *Z*-down *Y*-axis |
| Rear left wheel, *YawRL* | `Rotation(4,3)` | Vehicle *Z*-down *Z*-axis |
| Rear right wheel, *RollRR* | `Rotation(5,1)` | Vehicle *Z*-down *X*-axis |
| Rear right wheel, *PitchRR* | `Rotation(5,2)` | Vehicle *Z*-down *Y*-axis |
| Rear right wheel, *YawRR* | `Rotation(5,3)` | Vehicle *Z*-down *Z*-axis |

### **Light controls** — Vehicle light controls 1-by-6 vector

Light controls input signal, specified as a 1-by-6 Boolean vector. Each element of the
vector turns a specific vehicle light on or off, as indicated in this table. A value of
1 turns the light on; a value of 0 turns the light off.

| Vector Element | Vehicle Light |
| --- | --- |
| (1,1) | Headlight high beam |
| (1,2) | Headlight low beam |
| (1,3) | Brake |
| (1,4) | Reverse |
| (1,5) | Left signal |
| (1,6) | Right signal |

#### Dependencies

To create this port, on the **Light Controls** tab, select
**Enable light controls**.

**Data Types:** `Boolean`

## Parameters

### Vehicle Parameters

### **Type** — Type of vehicle `Tuk tuk` (default)

Type of vehicle. By default, **Type** is set to
`Tuk tuk`. For vehicle dimensions, see Tuk tuk.

### **Name** — Name of vehicle `SimulinkVehicle1` (default) | character vector

Name of vehicle. By default, when you use the block in your model, the
block sets the **Name** parameter to
`SimulinkVehicleX`.
The value of `X` depends on
the number of Simulation 3D Vehicle with Ground Following
and Simulation 3D Vehicle blocks that you have in your
model.

### **Sample time** — Sample time `-1` (default) | `scalar`

Sample time, *Ts*. The
graphics frame rate is the inverse of the sample time.

### Initial Values

### **Initial array values to translate vehicle per part, Translation** — Vehicle initial translation zeros( 5, 3 ) (default) | 5-by-3 array

Initial vehicle and wheel translation, in m. Array dimensions are 5-by-3.

- `Translation(1,1)`,
  `Translation(1,2)`, and
  `Translation(1,3)` — Initial vehicle
  translation along the inertial vehicle
  *Z*-down coordinate system
  *X*-, *Y*-, and
  *Z*- axes, respectively.
- `Translation(...,1)`,
  `Translation(...,2)`, and
  `Translation(...,3)` — Initial wheel
  translation relative to vehicle, along the vehicle
  *Z*-down *X*-,
  *Y*-, and *Z*-
  axes, respectively.

The parameter contains translation information according to the axle
and wheel locations.

Translation=[XvYvZvXHYHZHXFYFZFXRLYRLZRLXRRYRRZRR]

| Translation | Array Element | Translation Axis |
| --- | --- | --- |
| Vehicle, *Xv* | `Translation(1,1)` | Inertial vehicle *Z*-down *X*-axis |
| Vehicle, *Yv* | `Translation(1,2)` | Inertial vehicle *Z*-down *Y*-axis |
| Vehicle, *Zv* | `Translation(1,3)` | Inertial vehicle *Z*-down *Z*-axis |
| Handlebars, *XH* | `Translation(2,1)` | Vehicle *Z*-down *X*-axis |
| Handlebars, *YH* | `Translation(2,2)` | Vehicle *Z*-down *Y*-axis |
| Handlebars, *ZH* | `Translation(2,3)` | Vehicle *Z*-down *Z*-axis |
| Front wheel, *XF* | `Translation(3,1)` | Vehicle *Z*-down *X*-axis |
| Front wheel, *YF* | `Translation(3,2)` | Vehicle *Z*-down *Y*-axis |
| Front wheel, *ZF* | `Translation(3,3)` | Vehicle *Z*-down *Z*-axis |
| Rear left wheel, *XRL* | `Translation(4,1)` | Vehicle *Z*-down *X*-axis |
| Rear left wheel, *YRL* | `Translation(4,2)` | Vehicle *Z*-down *Y*-axis |
| Rear left wheel, *ZRL* | `Translation(4,3)` | Vehicle *Z*-down *Z*-axis |
| Rear right wheel, *XRR* | `Translation(5,1)` | Vehicle *Z*-down *X*-axis |
| Rear right wheel, *YRR* | `Translation(5,2)` | Vehicle *Z*-down *Y*-axis |
| Rear right wheel, *ZRR* | `Translation(5,3)` | Vehicle *Z*-down *Z*-axis |

### **Initial array values to rotate vehicle per part, Rotation** — Vehicle initial rotation zeros( 5, 3 ) (default) | 5-by-3 array

Initial vehicle and wheel rotation, about the vehicle
*Z*-down *X*-,
*Y*-, and *Z*- axes.

Array dimensions are 5-by-3.

- `Rotation(1,1)`,
  `Rotation(1,2)`, and
  `Rotation(1,3)` — Initial vehicle
  rotation about the inertial vehicle
  *Z*-down coordinate system
  *X*-, *Y*-, and
  *Z*- axes, respectively.
- `Rotation(...,1)`,
  `Rotation(...,2)`, and
  `Rotation(...,3)` — Initial wheel
  rotation relative to vehicle, about the vehicle
  *Z*-down *X*-,
  *Y*-, and *Z*-
  axes, respectively.

The parameter contains rotation information according to the axle and
wheel locations.

Rotation=[RollvPitchvYawvRollHPitchHYawHRollFPitchFYawFRollRLPitchRLYawRLRollRRPitchRRYawRR]

| Rotation | Array Element | Rotation Axis |
| --- | --- | --- |
| Vehicle, *Rollv* | `Rotation(1,1)` | Inertial vehicle *Z*-down *X*-axis |
| Vehicle, *Pitchv* | `Rotation(1,2)` | Inertial vehicle *Z*-down *Y*-axis |
| Vehicle, *Yawv* | `Rotation(1,3)` | Inertial vehicle *Z*-down *Z*-axis |
| Handlebars, *RollH* | `Rotation(2,1)` | Vehicle *Z*-down *X*-axis |
| Handlebars, *PitchH* | `Rotation(2,2)` | Vehicle *Z*-down *Y*-axis |
| Handlebars, *YawH* | `Rotation(2,3)` | Vehicle *Z*-down *Z*-axis |
| Front wheel, *RollF* | `Rotation(3,1)` | Vehicle *Z*-down *X*-axis |
| Front wheel, *PitchF* | `Rotation(3,2)` | Vehicle *Z*-down *Y*-axis |
| Front wheel, *YawF* | `Rotation(3,3)` | Vehicle *Z*-down *Z*-axis |
| Rear left wheel, *RollRL* | `Rotation(4,1)` | Vehicle *Z*-down *X*-axis |
| Rear left wheel, *PitchRL* | `Rotation(4,2)` | Vehicle *Z*-down *Y*-axis |
| Rear left wheel, *YawRL* | `Rotation(4,3)` | Vehicle *Z*-down *Z*-axis |
| Rear right wheel, *RollRR* | `Rotation(5,1)` | Vehicle *Z*-down *X*-axis |
| Rear right wheel, *PitchRR* | `Rotation(5,2)` | Vehicle *Z*-down *Y*-axis |
| Rear right wheel, *YawRR* | `Rotation(5,3)` | Vehicle *Z*-down *Z*-axis |

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

## Libraries

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

### R2024a: Requires Simulink 3D Animation

Simulating models with the Simulation 3D Three-Wheeled Vehicle block requires
Simulink
3D Animation.

## Description

Implement three-wheeled vehicle in 3D environment

**Note**

Simulating models with the Simulation 3D Three-Wheeled Vehicle block requires
Simulink®
3D Animation™.

The Simulation 3D Three-Wheeled Vehicle block implements a vehicle with three wheels in the
3D simulation environment.

To use this block, ensure that the Simulation 3D Scene Configuration
block is in your model. If you set the **Sample time** parameter of
this block to `-1`, the block uses the sample time specified in the
Simulation 3D Scene Configuration block.

The block input uses the vehicle Z-down *right-handed* (RH)
*Cartesian* coordinate system defined in SAE
J6701. The coordinate system is inertial and initially
aligned with the vehicle geometric center:

- *X*-axis — Along vehicle longitudinal axis, points
  forward
- *Y*-axis — Along vehicle lateral axis, points to the
  right
- *Z*-axis — Points downward

**Tip**

Verify that the Simulation 3D Three-Wheeled
Vehicle block executes before the Simulation 3D Scene
Configuration block. That way, Simulation 3D Three-Wheeled
Vehicle prepares the signal data before the Unreal Engine® 3D visualization environment receives it. To check the block execution
order, right-click the blocks and select **Properties**. On the
**General** tab, confirm these **Priority** settings:

- Simulation 3D Scene Configuration —
  `0`
- Simulation 3D Three-Wheeled Vehicle —
  `-1`

For more information about execution order, see Control and Display Execution Order.
