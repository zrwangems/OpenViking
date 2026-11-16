---
type: simulink-block
title: 'Simulation 3D Aircraft'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Simulation 3D'
documentation_page: 'simulation3daircraft'
documentation_source_path: 'simulation3daircraft.html'
language: en
---

# Simulation 3D Aircraft

## Ports

### Input

### **Translation** — Aircraft translation `11`-by-`3` array | `12`-by-`3` array | `15`-by-`3` array | `30`-by-`3` array | `57`-by-`3` array

Aircraft translation, specified as:

- `11`-by-`3` array — Aircraft
  **Type** is `Sky Hogg`.
- `12`-by-`3` array — Aircraft
  **Type** is `Airliner`.
- `15`-by-`3` array — Aircraft
  **Type** is `General Aviation`.
- `30`-by-`3` array — Aircraft
  **Type** is `Air Transport`.
- `57`-by-`3` array — Aircraft
  **Type** is `Custom`.

The signal contains translation [X, Y, Z], in meters, with one row of the array
for each bone of the aircraft.

The translation applies to these bones of the `Airliner`
type:

| Bone | Index |
| --- | --- |
| BODY | 1 |
| LEFT\_ENGINE | 2 |
| RIGHT\_ENGINE | 3 |
| RUDDER | 4 |
| ELEVATOR | 5 |
| LEFT\_AILERON | 6 |
| RIGHT\_AILERON | 7 |
| FLAPS | 8 |
| NOSE\_WHEEL\_STRUT | 9 |
| NOSE\_WHEEL | 10 |
| LEFT\_WHEEL | 11 |
| RIGHT\_WHEEL | 12 |

The translation applies to these bones of the `Sky Hogg`
type:

| Bone | Index |
| --- | --- |
| BODY | 1 |
| PROPELLER | 2 |
| RUDDER | 3 |
| ELEVATOR | 4 |
| LEFT\_AILERON | 5 |
| RIGHT\_AILERON | 6 |
| FLAPS | 7 |
| NOSE\_WHEEL\_STRUT | 8 |
| NOSE\_WHEEL | 9 |
| LEFT\_WHEEL | 10 |
| RIGHT\_WHEEL | 11 |

The translation applies to these bones of the `General
Aviation` type:

| Bone | Index |
| --- | --- |
| BODY | 1 |
| ENGINE1 | 2 |
| RUDDER | 3 |
| ELEVATOR | 4 |
| LEFT\_AILERON | 5 |
| RIGHT\_AILERON | 6 |
| FLAPS | 7 |
| LEFT\_SPOILER | 8 |
| RIGHT\_SPOILER | 9 |
| NOSE\_GEAR | 10 |
| NOSE\_WHEEL | 11 |
| LEFT\_GEAR | 12 |
| LEFT\_WHEEL | 13 |
| RIGHT\_GEAR | 14 |
| RIGHT\_WHEEL | 15 |

The translation applies to these bones of the `Air
Transport` type:

| Bone | Index |
| --- | --- |
| BODY | 1 |
| ENGINE1 | 2 |
| ENGINE2 | 3 |
| ENGINE3 | 4 |
| ENGINE4 | 5 |
| RUDDER | 6 |
| ELEVATOR | 7 |
| HORIZONTAL\_STAB | 8 |
| LEFT\_AILERON | 9 |
| RIGHT\_AILERON | 10 |
| FLAPS1 | 11 |
| FLAPS2 | 12 |
| LEFT\_SPOILER | 13 |
| RIGHT\_SPOILER | 14 |
| NOSE\_GEAR | 15 |
| NOSE\_WHEEL | 16 |
| NOSE\_GEAR\_DOOR1 | 17 |
| NOSE\_GEAR\_DOOR2 | 18 |
| LEFT\_GEAR | 19 |
| LEFT\_WHEEL | 20 |
| LEFT\_GEAR\_LINK | 21 |
| LEFT\_GEAR\_DOOR1 | 22 |
| LEFT\_GEAR\_DOOR2 | 23 |
| LEFT\_GEAR\_DOOR2\_2 | 24 |
| RIGHT\_GEAR | 25 |
| RIGHT\_WHEEL | 26 |
| RIGHT\_GEAR\_LINK | 27 |
| RIGHT\_GEAR\_DOOR1 | 28 |
| RIGHT\_GEAR\_DOOR2 | 29 |
| RIGHT\_GEAR\_DOOR2\_2 | 30 |

The translation applies to these bones of the `Custom`
type:

| Bone | Index |
| --- | --- |
| `BODY` | 1 |
| `ENGINE1` | 2 |
| `ENGINE1_PROP` | 3 |
| `ENGINE2` | 4 |
| `ENGINE2_PROP` | 5 |
| `ENGINE3` | 6 |
| `ENGINE3_PROP` | 7 |
| `ENGINE4` | 8 |
| `ENGINE4_PROP` | 9 |
| `ENGINE5` | 10 |
| `ENGINE5_PROP` | 11 |
| `ENGINE6` | 12 |
| `ENGINE6_PROP` | 13 |
| `ENGINE7` | 14 |
| `ENGINE7_PROP` | 15 |
| `ENGINE8` | 16 |
| `ENGINE8_PROP` | 17 |
| `ENGINE9` | 18 |
| `ENGINE9_PROP` | 19 |
| `ENGINE10` | 20 |
| `ENGINE10_PROP` | 21 |
| `ENGINE11` | 22 |
| `ENGINE11_PROP` | 23 |
| `ENGINE12` | 24 |
| `ENGINE12_PROP` | 25 |
| `ENGINE13` | 26 |
| `ENGINE13_PROP` | 27 |
| `ENGINE14` | 28 |
| `ENGINE14_PROP` | 29 |
| `ENGINE15` | 30 |
| `ENGINE15_PROP` | 31 |
| `ENGINE16` | 32 |
| `ENGINE16_PROP` | 33 |
| `WING1` | 34 |
| `WING1_LEFT_FLAP` | 35 |
| `WING1_RIGHT_FLAP` | 36 |
| `WING1_LEFT_AILERON` | 37 |
| `WING1_RIGHT_AILERON` | 38 |
| `WING1_LEFT_SPOILER` | 39 |
| `WING1_RIGHT_SPOILER` | 40 |
| `WING2` | 41 |
| `WING2_LEFT_FLAP` | 42 |
| `WING2_RIGHT_FLAP` | 43 |
| `HORIZONTAL_STABILIZER` | 44 |
| `LEFT_ELEVATOR` | 45 |
| `RIGHT_ELEVATOR` | 46 |
| `LEFT_RUDDER` | 47 |
| `RIGHT_RUDDER` | 48 |
| `NOSE_GEAR` | 49 |
| `NOSE_WHEEL` | 50 |
| `NOSE_GEAR_DOOR` | 51 |
| `LEFT_GEAR` | 52 |
| `LEFT_WHEEL` | 53 |
| `LEFT_GEAR_DOOR` | 54 |
| `RIGHT_GEAR` | 55 |
| `RIGHT_WHEEL` | 56 |
| `RIGHT_GEAR_DOOR` | 57 |

**Data Types:** `single` | `double`

### **Rotation** — Aircraft and wheel rotation `11`-by-`3` array | `12`-by-`3` array | `15`-by-`3` array | `30`-by-`3` array | `57`-by-`3` array

Aircraft rotation, specified as:

- `11`-by-`3` array — Aircraft
  **Type** is `Sky Hogg`.
- `12`-by-`3` array — Aircraft
  **Type** is `Airliner`.
- `15`-by-`3` array — Aircraft
  **Type** is `General Aviation`.
- `30`-by-`3` array — Aircraft
  **Type** is `Air Transport`.
- `57`-by-`3` array — Aircraft
  **Type** is `Custom`.

The rotation applies to the same bones as listed for the Translation port.

The signal contains the rotation [roll, pitch, yaw], in radians, with one row of
the array for each bone of the aircraft.

**Data Types:** `single` | `double`

### **LightStates** — Aircraft light control 1-by-7 vector of double values

Aircraft light control, specified as a 1-by-7 vector of double values. Each
element of the vector turns on (`1`) or off (`0`) a
specific aircraft light group. The vector has this order:

- `LANDING_LIGHTS`
- `TAXI_LIGHTS`
- `ANTICOLLISION_BEACONS`
- `WINGTIP_STROBE_LIGHTS`
- `TAIL_STROBE_LIGHTS`
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

### **Altitude** — Aircraft attitude 1-by-4 vector

Aircraft altitude, returned as a 1-by-4 vector. The four altitudes are, in
order:

- `aircraft_body`
- `aircraft_front_tire`
- `aircraft_left_tire`
- `aircraft_right_tire`

#### Dependencies

To enable this port, select the **Enable altitude sensor**
check box.

**Data Types:** `double`

### **WoW** — Weight on wheels `1` | `0`

Aircraft weight on wheels logical switch, returned as `1`(true)
if either of the contact locations or main gear tires (left or right) are on the
ground. Otherwise, `0` (false) is returned.

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

### Aircraft

### **Type** — Aircraft type `Sky Hogg` (default) | `Airliner` | `General Aviation` | `Air Transport` | `Custom`

Aircraft type, specified as `Sky Hogg`,
`Airliner`, `General Aviation`,
`Air Transport`, or `Custom`.

#### Dependencies

Setting this parameter requires that you set the **Initial
translation** and **Initial rotation** parameters to the
matching array size. Failure to appropriately set these array sizes causes an
error.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Mesh` |
| **Type**: character vector |
| **Values**: `'Sky Hogg'` | `'Airliner'` | `'General Aviation'` | `'Air Transport'` | `'Custom'` |
| **Default**: `'Sky Hogg'` |

### **Path to general aviation mesh** — Path to general aviation mesh `/MathWorksAerospaceContent/Vehicles/Aircraft/GeneralAviation/Mesh/SK_GeneralAviation.SK_GeneralAviation'` (default) | character vector

Path to general aviation mesh, specified as a character vector. To create a custom
aerospace mesh, see Prepare Custom Aircraft Mesh for the Unreal Editor.

#### Dependencies

- To enable this parameter, set **Type** to
  `General Aviation`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MeshPathGA` |
| **Type**: character vector |
| **Values**: `'/MathWorksAerospaceContent/Vehicles/Aircraft/GeneralAviation/Mesh/SK_GeneralAviation.SK_GeneralAviation'` |
| **Default**: `'/MathWorksAerospaceContent/Vehicles/Aircraft/GeneralAviation/Mesh/SK_GeneralAviation.SK_GeneralAviation'` |

### **Path to air transport mesh** — Path to air transport mesh `/MathWorksAerospaceContent/Vehicles/Aircraft/AirTransport/Mesh/SK_AirTransport.SK_AirTransport` (default) | character vector

Path to air transport mesh, specified as a character vector. To create a custom
aerospace mesh, see Prepare Custom Aircraft Mesh for the Unreal Editor.

#### Dependencies

- To enable this parameter, set **Type** to `Air
  Transport`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MeshPathAT` |
| **Type**: character vector |
| **Values**: `'/MathWorksAerospaceContent/Vehicles/Aircraft/AirTransport/Mesh/SK_AirTransport.SK_AirTransport'` |
| **Default**: `'/MathWorksAerospaceContent/Vehicles/Aircraft/AirTransport/Mesh/SK_AirTransport.SK_AirTransport'` |

### **Path to custom mesh** — Path to custom mesh `/MathWorksAerospaceContent/Vehicles/Aircraft/Custom/Mesh/SK_HL20.SK_HL20` (default) | `/MathWorksAerospaceContent/Vehicles/Aircraft/Custom/Mesh/SK_Aircraft.SK_Aircraft` | character vector

Path to custom mesh, specified as a character vector. To create a custom aerospace
mesh, see Prepare Custom Aircraft Mesh for the Unreal Editor.

#### Dependencies

- To enable this parameter, set **Type** to
  `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MeshPath` |
| **Type**: character vector |
| **Values**: `'/MathWorksAerospaceContent/Vehicles/Aircraft/Custom/Mesh/SK_HL20.SK_HL20'` | `'/MathWorksAerospaceContent/Vehicles/Aircraft/Custom/Mesh/SK_Aircraft.SK_Aircraft'` |
| **Default**: `'/MathWorksAerospaceContent/Vehicles/Aircraft/Custom/Mesh/SK_HL20.SK_HL20'` |

### **Color** — Aircraft color `Red` (default) | `Orange` | `Yellow` | `Green` | `Cyan` | `Blue` | `Black` | `White` | `Silver` | `Metal`

Aircraft color, specified as `Red`,
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

### **Name** — Aircraft name `SimulinkVehicle1` (default) | character vector

Aircraft name, specified as a character vector. By default, when you use the block
in your model, the block sets the **Name** parameter to
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

### **Initial translation (m)** — Initial translation of aircraft `zeros(11,3)` (default) | `11`-by-`3` array | `12`-by-`3` array | `15`-by-`3` array | `30`-by-`3` array | `57`-by-`3` array

Initial translation of aircraft, specified as an
`11`-by-`3`,
`12`-by-`3`,
`15`-by-`3`,
`30`-by-`3`, or
`57`-by-`3` array.

#### Dependencies

This parameter must match the aircraft type you set in
**Type**. Failure to appropriately set these array sizes causes an
error.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Translation` |
| **Type**: character vector |
| **Values**: `11`-by-`3` array | `12`-by-`3` array | `15`-by-`3` array | `30`-by-`3` array | `57`-by-`3` array |
| **Default**: `'zeros(11,3)'` |

**Data Types:** `single` | `double`

### **Initial rotation (rad)** — Aircraft rotation `zeros(11,3)` (default) | `11`-by-`3` array | `12`-by-`3` array | `15`-by-`3` array | `30`-by-`3` array | `57`-by-`3` array

Initial rotation of aircraft, specified as a
`11`-by-`3`,
`12`-by-`3`,
`15`-by-`3`,
`30`-by-`3`, or
`57`-by-`3` array.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Rotation` |
| **Type**: character vector |
| **Values**: `11`-by-`3` array | `12`-by-`3` array | `15`-by-`3` array | `30`-by-`3` array | `57`-by-`3` array |
| **Default**: `'zeros(11,3)'` |

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

To enable the altitude and WoW (weight on wheels) sensors, select this check box.
Otherwise, clear this check box.

- Altitude sensors return the vertical distance to the ground below a vehicle
  origin, mimicking a radar altimeter. For more information, see Altitude Sensors.
- The WoW sensor returns a logical true (`1`) if either of the
  main landing gear wheels are on the ground, and false (`0`)
  otherwise. For more information, see WoW Sensors.

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

Length of rays, specified as a real scalar in meters. The length of the rays
limits the altitude detection. For example, if the vertical distance to the ground
beneath the aircraft origin is greater than the length of the rays plus the aircraft
body *Z* offset, the altitude sensor returns `-1`
for the first value.

#### Dependencies

To enable this parameter, select the **Enable altitude sensor**
check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GHRayLength` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'1524'` |

### **Body Z offset (m)** — Aircraft body *Z* offset `0.90` (default) | real scalar

Aircraft body *Z* offset, specified as a real scalar in
meters.

#### Dependencies

To enable this parameter, select the **Enable altitude sensor**
check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GHBodyOffset` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'0.90'` |

### **Front tire radius (m)** — Front gear tire radius `0.21` (default) | real scalar

Front gear tire radius, specified as a real scalar in meters. The front gear
altitude ray originates at the front gear axle center plus the front gear tire radius
*Z* offset.

#### Dependencies

To enable this parameter, select the **Enable altitude sensor**
check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GHFrontTireRadius` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'0.21'` |

### **Left tire radius (m)** — Left gear tire radius 0.21 (default) | real scalar

Left gear tire radius, specified as a real scalar in meters.

#### Dependencies

To enable this parameter, select the **Enable altitude sensor**
check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GHLeftTireRadius` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'0.21'` |

### **Right tire radius (m)** — Right gear tire radius 0.21 (default) | real scalar

Right gear tire radius, specified as a real scalar in meters.

#### Dependencies

To enable this parameter, select the **Enable altitude sensor**
check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GHRightTireRadius` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'0.21'` |

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

Light configuration options

- `Automatic lights` — Use default aircraft lighting
  configuration that provides realistic pattern cycling.
- `Configurable lights` — Configure aircraft lighting
  parameters.
- `Lights off` — Turn off all aircraft lights.

#### Dependencies

- Setting this parameter to `Automatic lights`
  disables the configurability of all other **Light
  Configuration** parameters. The block uses the default parameter
  values for aircraft lighting values.
- Setting this parameter to `Configurable lights`
  enables the configurability of the **Light Configuration**
  parameters according to the aircraft type.
- Setting **Type** to these aircraft types and
  **Light Configuration** to `Configurable
  lights` enables the configurability of the lighting parameters in
  use for each aircraft.

  | Type | Lights | Light Parameters |
  | --- | --- | --- |
  | `Airliner` | **Landing lights** | - **Landing lights intensity (cd)** - **Landing lights cone half angle   (deg)** |
  | **Taxi lights** | - **Taxi lights intensity (cd)** - **Taxi lights cone half angle   (deg)** |
  | **Red/green navigation lights** | **Navigation lights intensity** |
  | **White strobe lights** | - **Strobe lights intensity** - **Wingtip strobe period (s)** - **Wingtip strobe pulse width (% of   period)** - **Tail strobe period (s)** - **Tail strobe pulse width (% of   period)** |
  | **Red beacon lights** | - **Beacon lights intensity** - **Beacon period (s)** - **Beacon pulse width (% of period)** |
  | `Sky Hogg` | **Landing lights** | - **Landing lights intensity (cd)** - **Landing lights cone half angle   (deg)** |
  | **Red/green navigation lights** | **Navigation lights intensity** |
  | **White strobe lights** | - **Strobe lights intensity** - **Tail strobe period (s)** - **Tail strobe pulse width (% of   period)** |
  | **Red beacon lights** | - **Beacon lights intensity** - **Beacon period (s)** - **Beacon pulse width (% of period)** |
  | `General Aviation`, `Air Transport`, or `Custom` | **Landing lights** | - **Landing lights intensity (cd)** - **Landing lights cone half angle   (deg)** - **Left landing light location** - **Left landing light orientation** - **Right landing light location** - **Right landing light orientation** |
  | **Taxi lights** | - **Taxi lights intensity (cd)** - **Taxi lights cone half angle   (deg)** - **Taxi lights location** - **Taxi lights orientation (deg)** |
  | **Red/green navigation lights** | **Navigation lights intensity** |
  | **White navigation lights** | **Position light intensity** |
  | **White strobe lights** | - **Strobe lights intensity** - **Wingtip strobe period (s)** - **Wingtip strobe pulse width (% of   period)** - **Tail strobe period (s)** - **Tail strobe pulse width (% of   period)** |
  | **Red beacon lights** | - **Beacon lights intensity** - **Beacon period (s)** - **Beacon pulse width (% of period)** |
- Setting this parameter to `Lights off` disables the
  configurability of all other **Light Configuration**
  parameters. The block turns off all aircraft lighting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LightsConfig` |
| **Type**: character vector |
| **Values**: `'Automatic lights'` | `'Configurable lights'` | `'Lights off'` |
| **Default**: `'Automatic lights'` |

### **Landing lights intensity (cd)** — Landing lights intensity 30000 (default) | positive scalar

Landing lights intensity, specified as a positive scalar, in candela.

#### Dependencies

To enable this parameter, set **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LandingLightIntensity` |
| **Type**: character vector |
| **Values**: positive scalar |
| **Default**: `'30000'` |

### **Landing lights cone half angle (deg)** — Landing lights cone half angle 15 (default) | positive scalar

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

### **Left landing light location** — Left landing light location `[0 0 0]` (default) | 3-element vector

Left landing light location with respect to the associated bone of the skeletal
mesh, specified as a 3-element vector.

#### Dependencies

To enable this parameter, set **Type** to `General
Aviation`, `Air Transport`, or
`Custom` and **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CustomLeftLandingLightLocation` |
| **Type**: character vector |
| **Values**: 3-element vector |
| **Default**: `'[0 0 0]'` |

### **Left landing light orientation (deg)** — Left landing light orientation `[0 0 0]` (default) | 3-element vector

Left landing light orientation with respect to the associated bone of the skeletal
mesh, specified as a 3-element vector.

#### Dependencies

To enable this parameter, set **Type** to `General
Aviation`, `Air Transport`, or
`Custom` and **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CustomLeftLandingLightOrientation` |
| **Type**: character vector |
| **Values**: 3-element vector |
| **Default**: `'[0 0 0]'` |

### **Right landing light location** — Right landing light location `[0 0 0]` (default) | 3-element vector

Right landing light location with respect to the associated bone of the skeletal
mesh, specified as a 3-element vector.

#### Dependencies

To enable this parameter, set **Type** to `General
Aviation`, `Air Transport`, or
`Custom` and **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CustomRightLandingLightLocation` |
| **Type**: character vector |
| **Values**: 3-element vector |
| **Default**: `'[0 0 0]'` |

### **Right landing light orientation (deg)** — Right landing light orientation `[0 0 0]` (default) | 3-element vector

Right landing light orientation with respect to the associated bone of the
skeletal mesh, specified as a 3-element vector.

#### Dependencies

To enable this parameter, set **Type** to `General
Aviation`, `Air Transport`, or
`Custom` and **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CustomRightLandingLightOrientation` |
| **Type**: character vector |
| **Values**: 3-element vector |
| **Default**: `'[0 0 0]'` |

### **Taxi lights intensity (cd)** — Taxi lights intensity `150000` (default) | positive scalar

Taxi lights intensity, specified as a positive scalar, in candela.

#### Dependencies

To enable this parameter, set **Type** to
`Airliner`, `General Aviation`,
`Air Transport`, or `Custom` and
**Light configuration** to `Configurable
lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TaxiLightIntensity` |
| **Type**: character vector |
| **Values**: positive scalar |
| **Default**: `'150000'` |

### **Taxi lights cone half angle (deg)** — Taxi lights cone half angle `36` (default) | positive scalar

Taxi lights cone half angle, specified as a positive scalar, in degrees.

#### Dependencies

To enable this parameter, set **Type** to
`Airliner`, `General Aviation`,
`Air Transport`, or `Custom` and
**Light configuration** to `Configurable
lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TaxiLightConeAngle` |
| **Type**: character vector |
| **Values**: positive scalar |
| **Default**: `'36'` |

### **Taxi lights location** — Taxi lights location `[0 0 0]` (default) | 3-element vector

Taxi lights location with respect to the associated bone of the skeletal mesh,
specified as a 3-element vector

#### Dependencies

To enable this parameter, set **Type** to `General
Aviation`, `Air Transport`, or
`Custom` and **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CustomTaxiLightLocation` |
| **Type**: character vector |
| **Values**: positive scalar |
| **Default**: `'[0 0 0]'` |

### **Taxi lights orientation (deg)** — Taxi lights orientation `[0 0 0]` (default) | 3-element vector

Taxi lights orientation with respect to the associated bone of the skeletal mesh,
specified as a 3-element vector

#### Dependencies

To enable this parameter, set **Type** to `General
Aviation`, `Air Transport`, or
`Custom` and **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CustomTaxiLightOrientation` |
| **Type**: character vector |
| **Values**: positive scalar |
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

### **Strobe lights intensity** — Strobe lights intensity `5000` (default) | positive scalar

Strobe lights intensity, specified as a positive scalar.

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

### **Wingtip strobe period (s)** — Wingtip strobe period `1.5` (default) | positive scalar

Wingtip strobe period, specified as a positive scalar.

#### Dependencies

To enable this parameter, set **Type** to
`Airliner`, `General Aviation`,
`Air Transport`, or `Custom` and
**Light configuration** to `Configurable
lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `WingtipStrobePeriod` |
| **Type**: character vector |
| **Values**: positive scalar |
| **Default**: `'1.5'` |

### **Wingtip strobe pulse width (% of period)** — Wingtip strobe pulse width `6` (default) | positive scalar

Wingtip strobe pulse width, specified as a positive scalar.

#### Dependencies

To enable this parameter, set **Type** to
`Airliner`, `General Aviation`,
`Air Transport`, or `Custom` and
**Light configuration** to `Configurable
lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `WingtipStrobePulseWidth` |
| **Type**: character vector |
| **Values**: positive scalar |
| **Default**: `'6'` |

### **Tail strobe period (s)** — Tail strobe period `1.5` (default) | positive scalar

Tail strobe period, specified as a positive scalar, in seconds.

#### Dependencies

To enable this parameter, set **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TailStrobePeriod` |
| **Type**: character vector |
| **Values**: positive scalar |
| **Default**: `'1.5'` |

### **Tail strobe pulse width (% of period)** — Tail strobe pulse width `6` (default) | positive scalar

Tail strobe pulse width, specified as a positive scalar.

#### Dependencies

To enable this parameter, set **Light configuration** to
`Configurable lights`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TailStrobePulseWidth` |
| **Type**: character vector |
| **Values**: positive scalar |
| **Default**: `'6'` |

### **Beacon lights intensity** — Beacon lights intensity `4000` (default) | positive scalar

Beacon lights intensity, specified as a positive scalar.

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

**Introduced in R2021b**

### R2024b: Simulation 3D Environment: Scale mesh for Simulation 3D Aircraft

You can now change the size of the mesh for the Simulation 3D Aircraft block using the
**Scale** parameter or the **Scale** port. The default scale is
a 1-by-3 vector of `[1 1 1]`.

To enable the parameters or port, use the **Scale source**
parameter.

- `Dialog` — Enable the **Scale** parameter.
- `Port` — Enable the **Scale** port and
  **Initial scale** parameter.

### R2024a: Requires Simulink 3D Animation

Simulating models with the Simulation 3D Aircraft block requires
Simulink
3D Animation.

### R2024a: Simulation 3D Aircraft Block Supports Single-Precision Inputs

The Simulation 3D Aircraft block now supports single- and double-precision inputs for the
**Translation** and **Rotation** input ports. Prior to R2024a, this
block supported only double-precision inputs for these ports.

### R2023a: Simulation 3D Aircraft Block Updates

The Simulation 3D
Aircraft block has these changes:

- The contents of the block **Initial Values** tab have moved to the
  **Aircraft** tab under the **Initial Values**
  section.
- The **Altitude Sensor** tab has these changes:

  - **Enable altitude sensor** has been renamed to **Enable
    Altitude and WoW sensors**.

    Starting with R2023a, the WoW (weight on wheels) sensor uses the altitude sensor
    rays and offsets that you specify in the block mask to determine if one or more
    wheel or ground contact location is touching the ground.
  - **Enable visible sensor rays** has been renamed to
    **Show sensor rays in viewer**.
  - **Aircraft body Z offset (in meters)** has been renamed to
    **Body Z offset (m)**.
  - **Front gear tire radius (in meters)** has been renamed to
    **Front tire radius (m)**.
  - **Left gear tire radius (in meters)** has been renamed to
    **Left tire radius (m)**.
  - **Right gear tire radius (in meters)** has been renamed to
    **Right tire radius (m)**.
  - **WoW sensor tolerance**, to set a WoW sensor tolerance.
  - New parameter, **Interpret vector outputs as 1-D**, to control
    if reshaping occurs on the **Altitude** and
    **WoW** sensor output ports.

### R2022a: Support for Custom Meshes and Aircraft Lighting

The block now supports:

- The specification of a custom aircraft mesh with the **Path to custom
  mesh** parameter. To enable this parameter, set **Type** to
  `Custom`.
- The configuration of aircraft lighting with a new **Light
  Configuration** tab.
- More colors for aircraft bodies in the **Color** parameter.

## Description

Implement aircraft in 3D environment

**Note**

Simulating models with the Simulation 3D Aircraft block requires
Simulink®
3D Animation™.

The Simulation 3D Aircraft block implements an aircraft in a 3D
visualization environment using translation and rotation to place the aircraft.

To use this block, ensure that the Simulation 3D Scene Configuration block
is in your model. If you set the **Sample time** parameter of this block to
`-1`, the block uses the sample time specified in the Simulation 3D
Scene Configuration block.

The block input uses the aircraft north-east-down (NED) *right-handed*
(RH) *Cartesian* coordinate system.

- *X*-axis — Along aircraft longitudinal axis, points forward
- *Y*-axis — Along aircraft lateral axis, points to the right
- *Z*-axis — Points downward

For more information, see Fundamental Coordinate System Concepts.

**Tip**

Verify that the Simulation 3D Aircraft
block executes before the Simulation 3D Scene Configuration block. That way,
Simulation 3D Aircraft prepares the signal data before the Unreal Engine® 3D visualization environment receives it. To check the block execution order,
right-click the blocks and select **Properties**. On the
**General** tab, confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Aircraft — `-1`

For more information about execution order, see Control and Display Execution Order.

### Skeletons, Bones, and Meshes

Unreal® uses a *skeleton*, *bones*, and
*mesh* to define a 3D model. A skeleton is comprised of a set of
bones. A mesh is the outer covering of the skeleton. Aircraft parts are sections of the
mesh, such as ailerons or wheels, which are linked to the bones. For more information, see
https://docs.unrealengine.com/4.27/AnimatingObjects/SkeletalMeshAnimation/Skeleton/.

For more information on how the Simulation 3D Aircraft block translation
input arrays connect to aircraft types, see Algorithms.
