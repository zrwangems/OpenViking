---
type: simulink-block
title: 'Unpack net_ctrl Packet from FlightGear'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Flight Simulator Interfaces'
documentation_page: 'unpacknet_ctrlpacketfromflightgear'
documentation_source_path: 'unpacknet_ctrlpacketfromflightgear.html'
language: en
---

# Unpack net_ctrl Packet from FlightGear

## Ports
```yaml
ports:
- name: net_ctrl
  summary: FlightGear packet to be unpacked array
  direction: input
  data_types: uint8
- name: wind_speed_kt
  summary: Wind speed scalar
  direction: output
  data_types: double
- name: wind_dir_deg
  summary: Wind direction scalar
  direction: output
  data_types: double
- name: turbulence_norm
  summary: Turbulence norm scalar
  direction: output
  data_types: double
- name: temp_c
  summary: Ambient temperature scalar
  direction: output
  data_types: double
- name: press_inhg
  summary: Ambient pressure scalar
  direction: output
  data_types: double
- name: hground
  summary: Ground elevation scalar
  direction: output
  data_types: double
- name: magvar
  summary: Local magnetic variation scalar
  direction: output
  data_types: double
- name: icing
  summary: Icing status scalar
  direction: output
  data_types: uint32
- name: aileron
  summary: Normalized aileron position 1 | scalar
  direction: output
  data_types: double
- name: elevator
  summary: Normalized elevator position 1 | scalar
  direction: output
  data_types: double
- name: rudder
  summary: Normalized rudder position 1 | scalar
  direction: output
  data_types: double
- name: aileron_trim
  summary: Normalized aileron trim position scalar
  direction: output
  data_types: double
- name: elevator_trim
  summary: Normalized elevator trim position 1 | scalar
  direction: output
  data_types: double
- name: rudder_trim
  summary: Normalized rudder trim position 1 | scalar
  direction: output
  data_types: double
- name: flaps
  summary: Normalized flaps position 1 | scalar
  direction: output
  data_types: double
- name: spoilers
  summary: Normalized spoilers position 1 | scalar
  direction: output
  data_types: single
- name: speedbrake
  summary: Normalized speedbrake position 1 | scalar
  direction: output
  data_types: single
- name: flaps_power
  summary: Power for flaps 1 | scalar
  direction: output
  data_types: uint32
- name: flap_motor_ok
  summary: Flap motor powered scalar
  direction: output
  data_types: uint32
- name: num_engines
  summary: Number of valid engines scalar
  direction: output
  data_types: uint32
- name: master_bat
  summary: Master battery switch vector
  direction: output
  data_types: uint32
- name: master_alt
  summary: Master alternator switch vector
  direction: output
  data_types: uint32
- name: magnetos
  summary: Magnetos switch scalar
  direction: output
  data_types: uint32
- name: starter_power
  summary: Power to start motor 1 | vector
  direction: output
  data_types: uint32
- name: throttle
  summary: Normalized throttle position 1 | vector
  direction: output
  data_types: double
- name: mixture
  summary: Normalized mixture lever position 1 | vector
  direction: output
  data_types: double
- name: condition
  summary: Normalized condition 1 | vector
  direction: output
  data_types: uint32
- name: fuel_pump_power
  summary: Normalized speedbrake position 1 | scalar
  direction: output
  data_types: uint32
- name: prop_advance
  summary: Propeller advance 1 | vector
  direction: output
  data_types: double
- name: feed_tank_to
  summary: Feed tank to switch vector
  direction: output
  data_types: uint32
- name: reverse
  summary: Reverse switch vector
  direction: output
  data_types: uint32
- name: engine_ok
  summary: Engine status indicator vector
  direction: output
  data_types: uint32
- name: mag_left_ok
  summary: Left magneto status indicator vector
  direction: output
  data_types: uint32
- name: mag_right_ok
  summary: Right magneto status indicator vector
  direction: output
  data_types: uint32
- name: spark_plugs_ok
  summary: Normalized speedbrake position vector
  direction: output
  data_types: uint32
- name: oil_press_status
  summary: Oil pressure status indicator 0 | 1 | 2 | scalar
  direction: output
  data_types: uint32
- name: fuel_pump_ok
  summary: Fuel management status indicator vector
  direction: output
  data_types: uint32
- name: num_tanks
  summary: Number of valid tanks scalar
  direction: output
  data_types: uint32
- name: fuel_selector
  summary: Fuel selector scalar
  direction: output
  data_types: single
- name: xfer_pump
  summary: Specify transfer vector
  direction: output
  data_types: uint32
- name: cross_feed
  summary: Cross feed valve scalar
  direction: output
  data_types: single
- name: brake_left
  summary: Left brake pedal position pilot scalar
  direction: output
  data_types: double
- name: brake_right
  summary: Right brake pedal position pilot scalar
  direction: output
  data_types: double
- name: copilot_brake_left
  summary: Left brake pedal position pilot scalar
  direction: output
  data_types: double
- name: copilot_brake_right
  summary: Right brake pedal position pilot scalar
  direction: output
  data_types: double
- name: brake_parking
  summary: Brake parking position scalar
  direction: output
  data_types: double
- name: gear_handle
  summary: Gear handle position scalar
  direction: output
  data_types: uint32
- name: master_avionics
  summary: Master avionics switch scalar
  direction: output
  data_types: uint32
- name: comm_1
  summary: Comm 1 frequency scalar
  direction: output
  data_types: double
- name: comm_2
  summary: Comm 2 frequency scalar
  direction: output
  data_types: double
- name: nav_1
  summary: Nav 1 frequency scalar
  direction: output
  data_types: double
- name: nav_2
  summary: Nav 2 frequency scalar
  direction: output
  data_types: double
```

### Input

### **net\_ctrl** — FlightGear packet to be unpacked array

FlightGear packet to be unpacked, specified as an array.

**Data Types:** `uint8`
### Output

#### Environment Outputs

### **wind\_speed\_kt** — Wind speed scalar

Wind speed, specified as a scalar, in knots.

#### Dependencies

To enable this port, select the **Show environment
outputs** check box.

**Data Types:** `double`

### **wind\_dir\_deg** — Wind direction scalar

Wind direction, specified as a scalar, in deg.

#### Dependencies

To enable this port, select the **Show environment
outputs** check box.

**Data Types:** `double`

### **turbulence\_norm** — Turbulence norm scalar

Turbulence norm, specified as a scalar.

#### Dependencies

To enable this port, select the **Show environment
outputs** check box.

**Data Types:** `double`

### **temp\_c** — Ambient temperature scalar

Ambient temperature, specified as a scalar, in deg C.

#### Dependencies

To enable this port, select the **Show environment
outputs** check box.

**Data Types:** `double`

### **press\_inhg** — Ambient pressure scalar

Ambient pressure, specified as a scalar, in inHg.

#### Dependencies

To enable this port, select the **Show environment
outputs** check box.

**Data Types:** `double`

### **hground** — Ground elevation scalar

Ground elevation, specified as a scalar, in m.

#### Dependencies

To enable this port, select the **Show environment
outputs** check box.

**Data Types:** `double`

### **magvar** — Local magnetic variation scalar

Local magnetic variation, specified as a scalar.

#### Dependencies

To enable this port, select the **Show environment
outputs** check box.

**Data Types:** `double`

### **icing** — Icing status scalar

Icing status, specified as a scalar, in deg.

#### Dependencies

To enable this port, select the **Show environment
outputs** check box.

**Data Types:** `uint32`

#### Control Surface Position Inputs

### **aileron** — Normalized aileron position `1` | scalar

Normalized aileron position [-1,1], specified as a scalar.

#### Dependencies

To enable this port, select the **Show control surface
position outputs** check box.

**Data Types:** `double`

### **elevator** — Normalized elevator position `1` | scalar

Normalized elevator position [-1,1], specified as a scalar.

#### Dependencies

To enable this port, select the **Show control surface
position outputs** check box.

**Data Types:** `double`

### **rudder** — Normalized rudder position `1` | scalar

Normalized rudder position [-1,1], specified as a scalar.

#### Dependencies

To enable this port, select the **Show control surface
position outputs** check box.

**Data Types:** `double`

### **aileron\_trim** — Normalized aileron trim position scalar

Normalized aileron trim position [-1,1], specified as a scalar.

#### Dependencies

To enable this port, select the **Show control surface
position outputs** check box.

**Data Types:** `double`

### **elevator\_trim** — Normalized elevator trim position `1` | scalar

Normalized elevator trim position [-1,1], specified as a
scalar.

#### Dependencies

To enable this port, select the **Show control surface
position outputs** check box.

**Data Types:** `double`

### **rudder\_trim** — Normalized rudder trim position `1` | scalar

Normalized rudder trim position [-1,1], specified as a scalar.

#### Dependencies

To enable this port, select the **Show control surface
position outputs** check box.

**Data Types:** `double`

### **flaps** — Normalized flaps position `1` | scalar

Normalized flaps position [-0,1], specified as a scalar.

#### Dependencies

To enable this port, select the **Show control surface
position outputs** check box.

**Data Types:** `double`

### **spoilers** — Normalized spoilers position `1` | scalar

Normalized spoilers position [0,1], specified as a scalar.

#### Dependencies

To enable this port, select the **Show control surface
position outputs** check box.

**Data Types:** `single`

### **speedbrake** — Normalized speedbrake position `1` | scalar

Normalized speedbrake position [0,1], specified as a scalar.

#### Dependencies

To enable this port, select the **Show control surface
position outputs** check box.

**Data Types:** `single`

### **flaps\_power** — Power for flaps `1` | scalar

Power for flaps, specified as a scalar. A value of
`1` indicates that power is available.

#### Dependencies

To enable this port, select the **Show control surface
position outputs** check box.

**Data Types:** `uint32`

### **flap\_motor\_ok** — Flap motor powered scalar

Flap motor powered, specified as a scalar.

#### Dependencies

To enable this port, select the **Show control surface
position outputs** check box.

**Data Types:** `uint32`

#### Engine/Fuel Outputs

### **num\_engines** — Number of valid engines scalar

Number of valid engines, specified as a scalar.

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `uint32`

### **master\_bat** — Master battery switch vector

Master battery switch, specified as a
vector.

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `uint32`

### **master\_alt** — Master alternator switch vector

Master alternator switch, specified as a
vector.

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `uint32`

### **magnetos** — Magnetos switch scalar

Magnetos switch, specified as a scalar.

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `uint32`

### **starter\_power** — Power to start motor `1` | vector

Power to starter motor, specified as a vector. A value of
`1` indicates that power is available.

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `uint32`

### **throttle** — Normalized throttle position `1` | vector

Normalized throttle position [0,1], specified as a vector.

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `double`

### **mixture** — Normalized mixture lever position `1` | vector

Normalized mixture lever position [0,1], specified as a vector.

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `double`

### **condition** — Normalized condition `1` | vector

Normalized condition [0,1], specified as a vector.

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `uint32`

### **fuel\_pump\_power** — Normalized speedbrake position `1` | scalar

Power to fuel pump, specified as a vector. A value of
`1` indicates that pump is on.

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `uint32`

### **prop\_advance** — Propeller advance `1` | vector

Propeller advance [0,1], specified as a vector.

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `double`

### **feed\_tank\_to** — Feed tank to switch vector

Feed tank to switch, specified as a vector.

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `uint32`

### **reverse** — Reverse switch vector

Reverse switch, specified as a vector.

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `uint32`

### **engine\_ok** — Engine status indicator vector

Engine status indicator, specified as a vector.

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `uint32`

### **mag\_left\_ok** — Left magneto status indicator vector

Left magneto status indicator, specified as a vector.

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `uint32`

### **mag\_right\_ok** — Right magneto status indicator vector

Right magneto status indicator, specified as a vector.

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `uint32`

### **spark\_plugs\_ok** — Normalized speedbrake position vector

Spark plugs status indicator, specified as a vector. A value of
`0` indicates that the plugs have failed.

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `uint32`

### **oil\_press\_status** — Oil pressure status indicator `0` | `1` | `2` | scalar

Oil pressure status indicator, specified as a vector.

- `0` — Normal oil pressure
- `1` — Low oil pressure
- `2` — Failed oil pressure

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `uint32`

### **fuel\_pump\_ok** — Fuel management status indicator vector

Fuel management status indicator, specified as a vector.

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `uint32`

### **num\_tanks** — Number of valid tanks scalar

Number of valid tanks, specified as a scalar.

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `uint32`

### **fuel\_selector** — Fuel selector scalar

Fuel selector, specified as a vector.

- `0` — Off
- `1` — On

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `single`

### **xfer\_pump** — Specify transfer vector

Specifies transfer from array value to tank, specified by value as a
vector.

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `uint32`

### **cross\_feed** — Cross feed valve scalar

Cross feed valve, specified as a scalar.

- `0` — False
- `1` — On

#### Dependencies

To enable this port, select the **Show engine/fuel
outputs** check box.

**Data Types:** `single`

#### Landing Gear Outputs

### **brake\_left** — Left brake pedal position pilot scalar

Left brake pedal position pilot, specified as a scalar.

#### Dependencies

To enable this port, select the **Show landing gear
outputs** check box.

**Data Types:** `double`

### **brake\_right** — Right brake pedal position pilot scalar

Right brake pedal position pilot, specified as a scalar.

#### Dependencies

To enable this port, select the **Show landing gear
outputs** check box.

**Data Types:** `double`

### **copilot\_brake\_left** — Left brake pedal position pilot scalar

Left brake pedal position pilot, specified as a scalar.

#### Dependencies

To enable this port, select the **Show landing gear
outputs** check box.

**Data Types:** `double`

### **copilot\_brake\_right** — Right brake pedal position pilot scalar

Right brake pedal position pilot, specified as a scalar.

#### Dependencies

To enable this port, select the **Show landing gear
outputs** check box.

**Data Types:** `double`

### **brake\_parking** — Brake parking position scalar

Brake parking position, specified as a scalar.

#### Dependencies

To enable this port, select the **Show landing gear
outputs** check box.

**Data Types:** `double`

### **gear\_handle** — Gear handle position scalar

Gear handle position, specified as a scalar.

- `0` — Gear handle up
- `1` — Gear handle down

#### Dependencies

To enable this port, select the **Show landing gear
outputs** check box.

**Data Types:** `uint32`

#### Avionic Outputs

### **master\_avionics** — Master avionics switch scalar

Master avionics switch, specified as a
scalar.

#### Dependencies

To enable this port, select the **Show avionic
outputs** check box.

**Data Types:** `uint32`

### **comm\_1** — Comm 1 frequency scalar

Comm 1 frequency, specified as a scalar, in Hz.

#### Dependencies

To enable this port, select the **Show avionic
outputs** check box.

**Data Types:** `double`

### **comm\_2** — Comm 2 frequency scalar

Comm 2 frequency, specified as a scalar, in Hz.

#### Dependencies

To enable this port, select the **Show avionic
outputs** check box.

**Data Types:** `double`

### **nav\_1** — Nav 1 frequency scalar

Nav 1 frequency, specified as a scalar, in Hz.

#### Dependencies

To enable this port, select the **Show avionic
outputs** check box.

**Data Types:** `double`

### **nav\_2** — Nav 2 frequency scalar

Nav 2 frequency, specified as a scalar, in Hz.

#### Dependencies

To enable this port, select the **Show avionic
outputs** check box.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Show control surface position outputs
  summary: Control surface position outputs off (default) | on
  group: ''
  block_parameter: ShowControlSurfacePositionOutputs
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Show engine/fuel outputs
  summary: Engine/fuel outputs off (default) | on
  group: ''
  block_parameter: ShowEngineFuelOutputs
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Show landing gear outputs
  summary: Landing gear outputs off (default) | on
  group: ''
  block_parameter: ShowLandingGearOutputs
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Show avionic outputs
  summary: Avionic outputs off (default) | on
  group: ''
  block_parameter: ShowAvionicOutputs
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Show environment outputs
  summary: Environment outputs on (default) | off
  group: ''
  block_parameter: ShowEnvironmentOutputs
  type: character vector
  values: '''off'' | ''on'''
  default: '''on'''
- name: Sample time
  summary: Sample time 1/30 (default) | scalar
  group: ''
  block_parameter: SampleTime
  type: character vector
  values: scalar
  default: '''1/30'''
```

### **Show control surface position outputs** — Control surface position outputs `off` (default) | `on`

Select this check box to include the control surface position outputs from
the FlightGear `net_ctrl` data packet.

#### Dependencies

Select this check box to enable these input ports.

**Signal Group 1: Control surface position outputs**

| Name | Units | Type | Width | Description |
| --- | --- | --- | --- | --- |
| *`aileron`* | 1 (dimensionless) | double | 1 | Normalized aileron position [-1,1] |
| *`elevator`* | 1 (dimensionless) | double | 1 | Normalized elevator position [-1,1] |
| *`rudder`* | 1 (dimensionless) | double | 1 | Normalized rudder position [-1,1] |
| *`aileron_trim`* | 1 (dimensionless) | double | 1 | Normalized aileron trim position [-1,1] |
| *`elevator_trim`* | 1 (dimensionless) | double | 1 | Normalized elevator trim position [-1,1] |
| *`rudder_trim`* | 1 (dimensionless) | double | 1 | Normalized rudder trim position [-1,1] |
| *`flaps`* | 1 (dimensionless) | double | 1 | Normalized flaps position [-0,1] |
| *`spoilers`* | 1 (dimensionless) | double | 1 | Normalized spoilers position [0,1] |
| *`speedbrake`* | 1 (dimensionless) | double | 1 | Normalized speedbrake position [0,1] |
| *`flaps_power`* | 1 (dimensionless) | uint32 | 1 | Power for flaps (`1` = power available) |
| *`flap_motor_ok`* | — | uint32 | 1 | Flap motor powered |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowControlSurfacePositionOutputs` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Show engine/fuel outputs** — Engine/fuel outputs `off` (default) | `on`

Select this check box to include the engine and fuel outputs from the
FlightGear `net_ctrl` data packet.

#### Dependencies

Select this check box to enable these input ports.

**Signal Group 2: Engine/fuel outputs**

| Name | Units | Type | Width | Description |
| --- | --- | --- | --- | --- |
| *`num_engines`* | — | uint32 | 1 | Number of valid engines |
| *`master_bat`* | — | uint32 | 4 | Master battery switch |
| *`master_alt`* | — | uint32 | 4 | Master alternator switch |
| *`magnetos`* | — | uint32 | 4 | Magnetos switch |
| *`starter_power`* | — | uint32 | 4 | Power to starter motor (`1` = starter power available) |
| *`throttle`* | 1 (dimensionless) | double | 4 | Normalized throttle position [0,1] |
| *`mixture`* | 1 (dimensionless) | double | 4 | Normalized mixture lever position [0,1] |
| *`condition`* | 1 (dimensionless) | double | 4 | Normalized condition [0,1] |
| *`fuel_pump_power`* | — | uint32 | 4 | Power to fuel pump `1` = on) |
| *`prop_advance`* | 1 (dimensionless) | double | 4 | Propeller advance [0,1] |
| *`feed_tank_to`* | — | uint32 | 4 | Feed tank to switch |
| *`reverse`* | — | uint32 | 4 | Reverse switch |
| *`engine_ok`* | — | uint32 | 4 | Engine status indicator |
| *`mag_left_ok`* | — | uint32 | 4 | Left magneto status indicator |
| *`mag_right_ok`* | — | uint32 | 4 | Right magneto status indicator |
| *`spark_plugs_ok`* | — | uint32 | 4 | Spark plugs status indicator (`0` = failed plugs) |
| *`oil_press_status`* | — | uint32 | 4 | Oil pressure status indicator (0 = normal, 1 = low, 2 = full failure) |
| *`fuel_pump_ok`* | — | uint32 | 4 | Fuel management status indicator |
| *`num_tanks`* | — | uint32 | 1 | Number of valid tanks |
| *`fuel_selector`* | — | uint32 | 8 | Fuel selector. (`0` = off, `1` = on) |
| *`xfer_pump`* | — | uint32 | 5 | Specifies transfer from array value to tank specified by value |
| *`cross_feed`* | — | uint32 | 1 | Cross feed valve (`0` = false, `1` = on) |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowEngineFuelOutputs` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Show landing gear outputs** — Landing gear outputs `off` (default) | `on`

Select this check box to include the landing gear outputs from the
FlightGear `net_ctrl` data packet.

#### Dependencies

Select this check box to enable these input ports.

**Signal Group 3: Landing gear outputs**

| Name | Units | Type | Width | Description |
| --- | --- | --- | --- | --- |
| *`brake_left`* | — | double | 1 | Left brake pedal position pilot |
| *`brake_right`* | — | double | 1 | Right brake pedal position pilot |
| *`copilot_brake_left`* | — | double | 1 | Left brake pedal position copilot |
| *`copilot_brake_right`* | — | double | 1 | Right brake pedal position copilot |
| *`brake_parking`* | — | double | 1 | Brake parking position |
| *`gear_handle`* | — | uint32 | 1 | Gear handle position (`1` = gear handle down, `0` = gear handle up) |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowLandingGearOutputs` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Show avionic outputs** — Avionic outputs `off` (default) | `on`

Select this check box to include the avionic outputs from the FlightGear
`net_ctrl` data packet.

#### Dependencies

Select this check box to enable these input ports.

**Signal Group 4: Avionics outputs**

| Name | Units | Type | Width | Description |
| --- | --- | --- | --- | --- |
| *`master_avionics`* | — | uint32 | 1 | Master avionics switch |
| *`comm_1`* | Hz | double | 1 | Comm 1 frequency |
| *`comm_2`* | Hz | double | 1 | Comm 2 frequency |
| *`nav_1`* | Hz | double | 1 | Nav 1 frequency |
| *`nav_2`* | Hz | double | 1 | Nav 2 frequency |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowAvionicOutputs` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Show environment outputs** — Environment outputs `on` (default) | `off`

Select this check box to include the environment outputs from the
FlightGear `net_ctrl` data packet.

#### Dependencies

Select this check box to enable these input ports.

**Signal Group 5: Environment outputs**

| Name | Units | Type | Width | Description |
| --- | --- | --- | --- | --- |
| *`wind_speed_kt`* | knot | double | 1 | Wind speed |
| *`wind_dir_deg`* | deg | double | 1 | Wind direction |
| *`turbulence_norm`* | — | double | 1 | Turbulence norm |
| *`temp_c`* | deg C | double | 1 | Ambient temperature |
| *`press_inhg`* | inHg | double | 1 | Ambient pressure |
| *`hground`* | m | double | 1 | Ground elevation |
| *`magvar`* | deg | double | 1 | Local magnetic variation |
| *`icing`* | – | uint32 | 1 | Icing status |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowEnvironmentOutputs` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'on'` |

### **Sample time** — Sample time 1/30 (default) | scalar

Specify the sample time (-1 for inherited), as a scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'1/30'` |
## Libraries

Aerospace Blockset / Animation / Flight Simulator Interfaces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2012a**

## Description

Unpack net_ctrl variable packet received from FlightGear

The Unpack net\_ctrl Packet from FlightGear block unpacks
`net_ctrl` variable packets received from FlightGear via the
Receive net\_ctrl Packet from FlightGear  block, and makes them
available for the Simulink® environment.

The Aerospace Blockset™ product supports FlightGear versions starting from v2.6. If you are using
a FlightGear version older than 2.6, the model displays a notification from the
Simulink Upgrade Advisor. Consider using the Upgrade Advisor to upgrade your
FlightGear version. For more information, see Supported FlightGear Versions.
