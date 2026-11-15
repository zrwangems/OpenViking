---
type: simulink-block
title: 'Simulation 3D Rotorcraft'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Visualization / Aerospace Scenarios'
documentation_page: 'simulation3drotorcraft'
documentation_source_path: 'simulation3drotorcraft.html'
language: en
---

# Simulation 3D Rotorcraft

## Ports

### Input

### **Translation** — Rotorcraft translation `6`-by-`3` array | `19`-by-`3` array | `11`-by-`3` array

Rotorcraft translation, specified as:

- `6`-by-`3` array — Rotorcraft
  **Type** is `Light helicopter`.
- `19`-by-`3` array — Rotorcraft
  **Type** is `Helicopter`.
- `11`-by-`3` array — Rotorcraft
  **Type** is `Multirotor`.

The signal contains translation [X, Y, Z], in meters, with one row of the array
for each bone of the rotorcraft.

The translation applies to these bones of the `Light
helicopter` type.

| Bone | Index |
| --- | --- |
| BODY | 1 |
| ENGINE | 2 |
| ROTOR1 | 3 |
| ROTOR2 | 4 |
| SENSOR1 | 5 |
| SENSOR2 | 6 |

The translation applies to these bones of the
`Helicopter` type.

| Bone | Index |
| --- | --- |
| BODY | 1 |
| ENGINE1 | 2 |
| ENGINE2 | 3 |
| ROTOR1 | 4 |
| ROTOR2 | 5 |
| NOSE\_GEAR | 6 |
| NOSE\_WHEEL | 7 |
| NOSE\_GEAR\_DOOR1 | 8 |
| NOSE\_GEAR\_DOOR2 | 9 |
| LEFT\_GEAR | 10 |
| LEFT\_WHEEL | 11 |
| LEFT\_GEAR\_DOOR1 | 12 |
| LEFT\_GEAR\_DOOR2 | 13 |
| RIGHT\_GEAR | 14 |
| RIGHT\_WHEEL | 15 |
| RIGHT\_GEAR\_DOOR1 | 16 |
| RIGHT\_GEAR\_DOOR2 | 17 |
| SENSOR1 | 18 |
| SENSOR2 | 19 |

The translation applies to these bones of the
`Multirotor` type.

| Bone | Index |
| --- | --- |
| BODY | 1 |
| ROTOR1 | 2 |
| ROTOR2 | 3 |
| ROTOR3 | 4 |
| ROTOR4 | 5 |
| ROTOR5 | 6 |
| ROTOR6 | 7 |
| ROTOR7 | 8 |
| ROTOR8 | 9 |
| SENSOR1 | 10 |
| SENSOR2 | 11 |

**Data Types:** `single` | `double`

### **Rotation** — Rotorcraft and wheel rotation `6`-by-`3` array | `19`-by-`3` array | `11`-by-`3` array

Rotorcraft rotation, specified as:

- `6`-by-`3` array — Rotorcraft
  **Type** is `Light helicopter`.
- `19`-by-`3` array — Rotorcraft
  **Type** is `Helicopter`.
- `11`-by-`3` array — Rotorcraft
  **Type** is `Multirotor`.

The rotation applies to the same bones as listed for the Translation port.

The signal contains the rotation [roll, pitch, yaw], in radians, with one row of
the array for each bone of the rotorcraft.

**Data Types:** `single` | `double`

### **LightStates** — Rotorcraft light control 1-by-7 vector of double values

Rotorcraft light control, specified as a 1-by-7 vector of double values. Each
element of the vector turns on (`1`) or off (`0`) a
specific rotorcraft light group. The vector has this order:

- `LANDING_LIGHTS`
- `NOSE_LIGHTS`
- `ANTICOLLISION_BEACONS`
- N/A (Ignored)
- `STROBE_LIGHTS`
- `NAVIGATION_LIGHTS`
- `POSITION_LIGHTS`

#### Dependencies

To enable this port, set the **Light Configuration** parameter
to `Configurable lights`.

**Data Types:** `single` | `double`

### **Scale** — Mesh scale `[1 1 1]` (default) | 1-by-3 array

Mesh scale, specified as a 1-by-3 array.

#### Dependencies

To enable this port, set the **Scale source** parameter to `Port`.
### Output

### **Altitude** — Rotorcraft attitude 1-by-5 vector

Rotorcraft attitude, returned as a 1-by-5 vector. The altitudes are, in
order:

| Light Helicopter | Helicopter | Multirotor |
| --- | --- | --- |
| `rotorcraft_body` | `rotorcraft_body` | `rotorcraft_body` |
| `rotorcraft_contact_location1` | `rotorcraft_front_tire` | `rotorcraft_contact_location1` |
| `rotorcraft_contact_location2` | `rotorcraft_left_tire` | `rotorcraft_contact_location2` |
| `rotorcraft_contact_location3` | `rotorcraft_right_tire` | `rotorcraft_contact_location3` |
| `rotorcraft_contact_location4` | N/A (`0`) | `rotorcraft_contact_location4` |

#### Dependencies

To enable this port, select the **Enable altitude and Wow
sensors** check box.

**Data Types:** `double`

### **WoW** — Weight on wheels `true` | `false`

Rotorcraft weight on wheels, WoW, logical switch, returned as
`true` if either of the contact locations or main gear tires (left
or right) are on the ground. Otherwise, the output is `false`.

#### Dependencies

To enable this port, select the **Enable altitude and Wow
sensors** check box.

**Data Types:** `Boolean`

## Parameters

### **Sample time** — Sample time `-1` (default) | real scalar

Sample time, *Ts*. The graphics frame rate
is the inverse of the sample time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'-1'` |

### Rotorcraft

### **Type** — Rotorcraft type `Light helicopter` (default) | `Helicopter` | `Multirotor`

Rotorcraft type, specified as `Light helicopter`,
`Helicopter`, or `Multirotor`.

#### Dependencies

To set this parameter, set the **Initial translation** and
**Initial rotation** parameters to the matching array size.
Failure to appropriately set these array sizes causes an error.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Mesh` |
| **Type**: character vector |
| **Values**: `'Light helicopter'` | `'Helicopter'` | `'Multiroter'` |
| **Default**: `'Light helicopter'` |

### **Path to light helicopter mesh** — Path to light helicopter mesh `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/LightHelicopter/Mesh/SK_LightHelicopter.SK_LightHelicopter'` (default) | character vector

Path to light helicopter mesh, specified as a character vector. To create a custom
aerospace mesh, see Prepare Custom Aircraft Mesh for the Unreal Editor.

#### Dependencies

To enable this parameter, set **Type** to `Light
helicopter`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MeshPathLight` |
| **Type**: character vector |
| **Values**: `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/LightHelicopter/Mesh/SK_LightHelicopter.SK_LightHelicopter'` |
| **Default**: `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/LightHelicopter/Mesh/SK_LightHelicopter.SK_LightHelicopter'` |

### **Path to helicopter mesh** — Path to helicopter mesh `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/Helicopter/Mesh/SK_Helicopter.SK_Helicopter'` (default) | character vector

Path to helicopter mesh, specified as a character vector. To create a custom
aerospace mesh, see Prepare Custom Aircraft Mesh for the Unreal Editor.

#### Dependencies

To enable this parameter, set **Type** to
`Helicopter`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MeshPath` |
| **Type**: character vector |
| **Values**: `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/Helicopter/Mesh/SK_Helicopter.SK_Helicopter'` |
| **Default**: `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/Helicopter/Mesh/SK_Helicopter.SK_Helicopter'` |

### **Path to multirotor mesh** — Path to multirotor mesh `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/Multirotor/Mesh/SK_Quadcopter.SK_Quadcopter'` (default) | `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/Multirotor/Mesh/SK_QuadcopterMini.SK_QuadcopterMini'` | character vector

Path to multirotor mesh, specified as a character vector. To create a custom
aerospace mesh, see Prepare Custom Aircraft Mesh for the Unreal Editor.

#### Dependencies

To enable this parameter, set **Type** to
`Multirotor`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MeshPathMulti` |
| **Type**: character vector |
| **Values**: `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/Multirotor/Mesh/SK_Quadcopter.SK_Quadcopter'` | `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/Multirotor/Mesh/SK_QuadcopterMini.SK_QuadcopterMini'` |
| **Default**: `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/Multirotor/Mesh/SK_Quadcopter.SK_Quadcopter'` |

### **Color** — Rotorcraft color `Red` (default) | `Orange` | `Yellow` | `Green` | `Cyan` | `Blue` | `Black` | `White` | `Silver` | `Metal`

Rotorcraft color, specified as `Red`,
`Orange`, `Yellow`,
`Green`, `Cyan`,
`Blue`, `Black`,
`White`, `Silver`, or
`Metal`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AircraftColor` |
| **Type**: character vector |
| **Values**: `'Red'` | `'Orange'` | `'Yellow'` | `'Green'` | `'Cyan'` | `'Blue'` | `'Black'` | `'White'` | `'Silver'` | `'Metal'` |
| **Default**: `'Red'` |

### **Name** — Rotorcraft name `SimulinkVehicle1` (default) | character vector

Rotorcraft name, specified as a character vector. By default, when you use the
block in your model, the block sets the **Name** parameter to
`SimulinkVehicleX`. The value of
`X` depends on the number of other
simulation 3D blocks that you have in your model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ActorName` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'SimulinkVehicle1'` |

### **Initial translation (m)** — Initial translation of rotorcraft `zeros(6,3)` (default) | 19-by-3 array | 11-by-3 array

Initial translation of rotorcraft, specified as an 6-by-3, 19-by-3, or 11-by-3
array.

#### Dependencies

This parameter must match the rotorcraft type you set in
**Type**. Failure to appropriately set these array sizes causes
an error.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Translation` |
| **Type**: character vector |
| **Values**: 6-by-3 array | 19-by-3 array | 11-by-3 array |
| **Default**: `'zeros(6,3)'` |

**Data Types:** `single` | `double`

### **Initial rotation (rad)** — Rotorcraft rotation `zeros(6,3)` (default) | 19-by-3 array | 11-by-3 array

Initial rotation of rotorcraft, specified as an 6-by-3, 19-by-3, or 11-by-3 array.

#### Dependencies

This parameter must match the rotorcraft type you set in
**Type**. Failure to appropriately set these array sizes causes
an error.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Rotation` |
| **Type**: character vector |
| **Values**: 6-by-3 array | 19-by-3 array | 11-by-3 array |
| **Default**: `'zeros(6,3)'` |

**Data Types:** `single` | `double`

### **Scale source** — Scale source `Dialog` (default) | `Port`

Scale source, specified as `Dialog` or `Port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ScaleInputPort` |
| **Type**: character vector |
| **Values**: `'Dialog'` | `'Port'` |
| **Default**: `'Dialog'` |

### **Initial scale** — Initial mesh scale `[1 1 1]` (default) | 1-by-3 array

Initial mesh scale, specified as a 1-by-3 array.

#### Dependencies

To enable this parameter, set **Scale source** to
`Port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InitialScale` |
| **Type**: character vector |
| **Values**: `1`-by-`3` array |
| **Default**: `'[1 1 1]'` |

**Data Types:** `single` | `double`

### **Scale** — Mesh scale `[1 1 1]` (default) | 1-by-3 array

Mesh scale, specified as a 1-by-3 array.

#### Dependencies

To enable this parameter, set **Scale source** to `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Scale` |
| **Type**: character vector |
| **Values**: `1`-by-`3` array |
| **Default**: `'[1 1 1]'` |

**Data Types:** `single` | `double`

### Altitude Sensor

### **Enable altitude and WoW sensors** — Altitude and WoW sensors on (default) | off

To enable output ports for altitude and WoW sensors, select this check box.
Otherwise, clear this check box. For more information on the altitude and WoW sensors,
see Altitude Sensors and WoW Sensors.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IsGHSensorEnabled` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Show sensor rays in viewer** — Option to show sensor rays off (default) | on

To show sensor rays in the viewer, select this check box. Otherwise, clear this check
box.

#### Dependencies

To enable this parameter, select the **Enable altitude and Wow
sensors** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AreGHRaysVisible` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Interpret vector outputs as 1-D** — Control reshaping on sensor output ports off (default) | on

Control if reshaping occurs on the **Altitude**
**WoW** sensor output ports:

- Select this check box to enable reshaping.
- Clear this check box to disable reshaping.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IsOutputReshapeEnabled` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Length of rays (m)** — Length of rays `1524` (default) | real scalar

Length of rays, specified as a real scalar, in meters. The length of the rays
limits the altitude detection. For example, if the vertical distance to the ground
beneath the rotorcraft origin is greater than the length of the rays plus the
rotorcraft body *Z* offset, the altitude sensor returns
`-1` for the first value.

#### Dependencies

To enable this parameter, select the **Enable altitude and Wow
sensors** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GHRayLength` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'1524'` |

### **Rotorcraft body Z offset (m)** — Rotorcraft body *Z* offset `1.169` (default) | real scalar

Rotorcraft body *Z* offset, specified as a real scalar, in
meters.

#### Dependencies

To enable this parameter, select the **Enable altitude and Wow
sensors** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GHBodyOffset` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'1.169'` |

### **Ground-contact location 1 (m)** — First ground contact location `[1.47 -1.04 1.169]` (default) | 3-element vector

First ground contact location, specified as a 3-element vector, in meters.

#### Dependencies

To enable this parameter:

- Set **Type** to `Light helicopter`
  or `Multirotor`.
- Select the **Enable altitude and Wow sensors** check
  box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GHContactLocation1` |
| **Type**: character vector |
| **Values**: 3-element vector |
| **Default**: `'[1.47 -1.04 1.169]'` |

### **Ground-contact location 2 (m)** — Second ground contact location `[-1.24 -1.04 1.169]` (default) | 3-element vector

Second ground contact location, specified as a 3-element vector, in meters.

#### Dependencies

To enable this parameter:

- Set **Type** to `Light helicopter`
  or `Multirotor`.
- Select the **Enable altitude and Wow sensors** check
  box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GHContactLocation2` |
| **Type**: character vector |
| **Values**: 3-element vector |
| **Default**: `'[-1.24 -1.04 1.169]'` |

### **Ground-contact location 3 (m)** — Third ground contact location `[-1.24 1.04 1.169]` | 3-element vector

Third ground contact location, specified as a 3-element vector, in meters.

#### Dependencies

To enable this parameter:

- Set **Type** to `Light helicopter`
  or `Multirotor`.
- Select the **Enable altitude and Wow sensors** check
  box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GHContactLocation3` |
| **Type**: character vector |
| **Values**: 3-element vector |
| **Default**: `'[-1.24 1.04 1.169]'` |

### **Ground-contact location 4 (m)** — Fourth ground contact location `[1.47 1.04 1.169]` | 3-element vector

Fourth ground contact location, specified as a 3-element vector, in meters.

#### Dependencies

To enable this parameter:

- Set **Type** to `Light helicopter`
  or `Multirotor`.
- Select the **Enable altitude and Wow sensors** check
  box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GHContactLocation4` |
| **Type**: character vector |
| **Values**: 3-element vector |
| **Default**: `'[1.47 1.04 1.169]'` |

### **Front tire radius (m)** — Front gear tire radius `0.196` (default) | real scalar

Front gear tire radius, specified as a real scalar, in meters. The front gear
altitude ray originates at the front gear axle center plus the front gear tire radius
*Z* offset.

#### Dependencies

To enable this parameter:

- Set **Type** to
  `Helicopter`.
- Select the **Enable altitude and Wow sensors** check
  box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GHFrontTireRadius` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'0.196'` |

### **Left tire radius (m)** — Left gear tire radius `0.203` (default) | real scalar

Left gear tire radius, specified as a real scalar, in meters.

#### Dependencies

To enable this parameter:

- Set **Type** to
  `Helicopter`.
- Select the **Enable altitude and Wow sensors** check
  box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GHLeftTireRadius` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'0.203'` |

### **Right tire radius (m)** — Right gear tire radius `0.203` (default) | real scalar

Right gear tire radius, specified as a real scalar, in meters.

#### Dependencies

To enable this parameter:

- Set **Type** to
  `Helicopter`.
- Select the **Enable altitude and Wow sensors** check
  box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GHRightTireRadius` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'0.203'` |

### **WoW sensor tolerance (m)** — Wow sensor tolerance `0.05` (default) | real scalar

Wow sensor tolerance, specified as a real scalar.

#### Dependencies

To enable this parameter, select the **Enable altitude and Wow sensors**
check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `WoWSensorTolerance` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'0.05'` |

### Light Configuration

### **Light configuration** — Light configurations options `Automatic lights` (default) | `Configurable lights` | `Lights off`

Light configuration options, specified as one of these values:

- `Automatic lights` — Use default rotorcraft lighting
  configuration that provides realistic pattern cycling.
- `Configurable lights` — Configure rotorcraft lighting
  parameters.
- `Lights off` — Turn off all rotorcraft lights.

#### Dependencies

- Setting this parameter to `Automatic lights`
  disables the configurability of all other **Light
  Configuration** parameters. The block uses the default parameter
  values for rotorcraft lighting values.
- Setting this parameter to `Configurable lights`
  enables the configurability of the **Light Configuration**
  parameters according to the rotorcraft type.
- Setting **Type** to a given rotorcraft type and
  **Light Configuration** to `Configurable
  lights` enables the configurability of the lighting parameters in
  use for each rotorcraft.
- Setting this parameter to `Lights off` disables the
  configurability of all other **Light Configuration**
  parameters. The block turns off all rotorcraft lighting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LightsConfig` |
| **Type**: character vector |
| **Values**: `'Automatic lights'` | `'Configurable lights'` | `'Lights off'` |
| **Default**: `'Automatic lights'` |

### **Landing light intensity (cd)** — Landing lights intensity `300000` (default) | positive scalar

Landing light intensity, specified as a positive scalar, in candela.

#### Dependencies

To enable this parameter, set **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LandingLightIntensity` |
| **Type**: character vector |
| **Values**: positive scalar |
| **Default**: `'300000'` |

### **Landing light cone half angle (deg)** — Landing lights cone half angle `15` (default) | positive scalar

Landing lights cone half angle, specified as a positive scalar, in degrees.

#### Dependencies

To enable this parameter, set **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LandingLightConeAngle` |
| **Type**: character vector |
| **Values**: positive scalar |
| **Default**: `'15'` |

### **Landing light color [r g b]** — Landing light color `[1 1 1]` (default) | 3-element vector

Landing light color, specified as a 3-element vector [red green blue].

#### Dependencies

To enable this parameter:

- Set **Type** to **Multirotor**.
- Set **Light configuration** to `Configurable
  lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LandingLightColor` |
| **Type**: character vector |
| **Values**: 3-element vector |
| **Default**: `'[1 1 1]'` |

### **Landing light location** — Landing light location `[0 0 0]` (default) | 3-element vector

Landing light location with respect to the associated bone of the skeletal mesh,
specified as a 3-element vector.

#### Dependencies

To enable this parameter, set **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `HelicopterLeftLandingLightLocation` |
| **Type**: character vector |
| **Values**: 3-element vector |
| **Default**: `'[0 0 0]'` |

### **Landing light orientation (deg)** — Landing light orientation `[0 0 0]` (default) | 3-element vector

Landing light orientation with respect to the associated bone of the skeletal
mesh, specified as a 3-element vector.

#### Dependencies

To enable this parameter, **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `HelicopterLeftLandingLightOrientation` |
| **Type**: character vector |
| **Values**: 3-element vector |
| **Default**: `'[0 0 0]'` |

### **Nose light intensity (cd)** — Nose lights intensity `150000` (default) | positive scalar

Nose lights intensity, specified as a positive scalar, in candela.

#### Dependencies

To enable this parameter, set **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NoseLightIntensity` |
| **Type**: character vector |
| **Values**: positive scalar |
| **Default**: `'150000'` |

### **Nose light cone half angle (deg)** — Nose light cone half angle `36` (default) | positive scalar

Nose light cone half angle, specified as a positive scalar, in degrees.

#### Dependencies

To enable this parameter, set **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NoseLightConeAngle` |
| **Type**: character vector |
| **Values**: positive scalar |
| **Default**: `'36'` |

### **Nose light location** — Nose light location `[0 0 0]` (default) | 3-element vector

Nose light location with respect to the associated bone of the skeletal mesh,
specified as a 3-element vector.

#### Dependencies

To enable this parameter, set **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `HelicopterNoseLightLocation` |
| **Type**: character vector |
| **Values**: 3-element vector |
| **Default**: `'[0 0 0]'` |

### **Nose light orientation (deg)** — Nose light orientation `[0 0 0]` (default) | 3-element vector

Nose light orientation with respect to the associated bone of the skeletal mesh,
specified as a 3-element vector.

#### Dependencies

To enable this parameter, set **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `HelicopterNoseLightOrientation` |
| **Type**: character vector |
| **Values**: 3-element vector |
| **Default**: `'[0 0 0]'` |

### **Navigation lights intensity** — Navigation lights intensity `500` (default) | positive scalar

Navigation lights intensity, specified as a positive scalar.

#### Dependencies

To enable this parameter, set **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NavLightIntensity` |
| **Type**: character vector |
| **Values**: positive scalar |
| **Default**: `'500'` |

### **Position light intensity** — Position light intensity `500` (default) | positive scalar

Position light intensity, specified as a positive scalar.

#### Dependencies

To enable this parameter, set **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PositionLightIntensity` |
| **Type**: character vector |
| **Values**: positive scalar |
| **Default**: `'500'` |

### **Strobe light intensity** — Strobe light intensity `5000` (default) | positive scalar

Strobe light intensity, specified as a positive scalar.

#### Dependencies

To enable this parameter, set **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `StrobeLightIntensity` |
| **Type**: character vector |
| **Values**: positive scalar |
| **Default**: `'5000'` |

### **Strobe color [r g b]** — Strobe color `[1 1 1]` (default) | 3-element vector

Strobe light color, specified as a 3-element vector [red green blue].

#### Dependencies

To enable this parameter:

- Set **Type** to
  `Multirotor`.
- Set **Light configuration** to `Configurable
  lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `StrobeLightColor` |
| **Type**: character vector |
| **Values**: 3-element vector |
| **Default**: `'[1 1 1]'` |

### **Strobe period (s)** — Strobe period `1.5` (default) | positive scalar

Strobe period, specified as a positive scalar.

#### Dependencies

To enable this parameter, set **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `StrobePeriod` |
| **Type**: character vector |
| **Values**: positive scalar |
| **Default**: `'1.5'` |

### **Strobe pulse width (% of period)** — Strobe pulse width `6` (default) | positive scalar

Strobe pulse width, specified as a positive scalar.

#### Dependencies

To enable this parameter, set **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `StrobePulseWidth` |
| **Type**: character vector |
| **Values**: positive scalar |
| **Default**: `'6'` |

### **Beacon light intensity** — Beacon light intensity `4000` (default) | positive scalar

Beacon light intensity, specified as a positive scalar.

#### Dependencies

To enable this parameter, set **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BeaconLightIntensity` |
| **Type**: character vector |
| **Values**: positive scalar |
| **Default**: `'4000'` |

### **Beacon color [r g b]** — Beacon color `[1 0 0]` (default) | 3-element vector

Beacon color, specified as a 3-element vector [red green blue].

#### Dependencies

To enable this parameter:

- Set **Type** to **Multirotor**.
- Set **Light configuration** to `Configurable
  lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BeaconLightColor` |
| **Type**: character vector |
| **Values**: 3-element vector |
| **Default**: `'[1 0 0]'` |

### **Beacon period (s)** — Beacon period `1.5` (default) | positive scalar

Beacon period, specified as a positive scalar, in seconds.

#### Dependencies

To enable this parameter, set **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BeaconPeriod` |
| **Type**: character vector |
| **Values**: positive scalar |
| **Default**: `'1.5'` |

### **Beacon pulse width (% of period)** — Beacon pulse width `10` (default) | positive scalar

Beacon pulse width, specified as a positive scalar.

#### Dependencies

To enable this parameter, set **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BeaconPulseWidth` |
| **Type**: character vector |
| **Values**: positive scalar |
| **Default**: `'10'` |

## Libraries

Aerospace Blockset / Animation / Simulation 3D

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023a**

### R2024b: Simulation 3D Environment: Scale mesh for Simulation 3D Rotorcraft

You can now change the size of the mesh for the Simulation 3D Rotorcraft block using the
**Scale** parameter or the **Scale** port. The default scale is
a 1-by-3 vector of `[1 1 1]`.

To enable the parameters or port, use the **Scale source**
parameter.

- `Dialog` — Enable the **Scale** parameter.
- `Port` — Enable the **Scale** port and
  **Initial scale** parameter.

### R2024a: Requires Simulink 3D Animation

Simulating models with the Simulation 3D Rotorcraft block requires
Simulink
3D Animation.

### R2024a: Simulation 3D Rotorcraft Block Supports Single-Precision Inputs

The Simulation 3D Rotorcraft block now supports single- and double-precision inputs for the
**Translation** and **Rotation** input ports. Prior to R2024a, this
block supported only double-precision inputs for these ports.

## Description

Implement 3D Rotorcraft

**Note**

Simulating models with the Simulation 3D Rotorcraft block requires
Simulink®
3D Animation™.

The Simulation 3D Rotorcraft block implements a rotorcraft in a 3D
visualization environment using translation and rotation to place the rotorcraft.

To use this block, your model must contain a Simulation 3D Scene
Configuration block. If you set the **Sample time** parameter of
this block to `-1`, the block uses the sample time specified in the
Simulation 3D Scene Configuration block.

The block input uses the rotorcraft north-east-down (NED)
*right-handed* (RH) *Cartesian* coordinate system.

- *X*-axis — Along rotorcraft longitudinal axis, points forward
- *Y*-axis — Along rotorcraft lateral axis, points to the
  right
- *Z*-axis — Points downward

For more information, see Fundamental Coordinate System Concepts.

**Tip**

Verify that the Simulation 3D Rotorcraft
block executes before the Simulation 3D Scene Configuration block. That way,
Simulation 3D Rotorcraft prepares the signal data before the Unreal Engine® 3D visualization environment receives the data. To check the block execution
order, right-click the blocks and select **Properties**. On the
**General** tab, confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Rotorcraft — `-1`

For more information about execution order, see Control and Display Execution Order.

### Skeletons, Bones, and Meshes

Unreal® uses a *skeleton*, *bones*, and
*mesh* to define a 3D model. A skeleton is comprised of a set of
bones. A mesh is the outer covering of the skeleton. Rotorcraft parts are sections of the
mesh, such as rotor blades or wheels, which are linked to the bones. For more information,
see https://docs.unrealengine.com/4.27/AnimatingObjects/SkeletalMeshAnimation/Skeleton/.

For more information on how the Simulation 3D Rotorcraft block
translation input arrays connect to rotorcraft types, see Algorithms.
