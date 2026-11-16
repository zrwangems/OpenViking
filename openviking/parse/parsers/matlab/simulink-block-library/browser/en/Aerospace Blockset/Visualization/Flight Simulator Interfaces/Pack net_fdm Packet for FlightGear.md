---
type: simulink-block
title: 'Pack net_fdm Packet for FlightGear'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Visualization / Flight Simulator Interfaces'
documentation_page: 'packnet_fdmpacketforflightgear'
documentation_source_path: 'packnet_fdmpacketforflightgear.html'
language: en
---

# Pack net_fdm Packet for FlightGear

## Ports

### Input

#### Position/Attitude Inputs

### **l** — Longitude scalar

Longitude, specified as a scalar, in rad.

#### Dependencies

To enable this port, select the **Show position/attitude
inputs** check box.

**Data Types:** `double`

### **μ** — Latitude scalar

Latitude, specified as a scalar, in rad.

#### Dependencies

To enable this port, select the **Show position/attitude
inputs** check box.

**Data Types:** `double`

### **h** — Altitude scalar

Altitude, specified as a scalar, in m.

#### Dependencies

To enable this port, select the **Show position/attitude
inputs** check box.

**Data Types:** `double`

### **ϕ** — Roll scalar

Roll, specified as a scalar, in rad.

#### Dependencies

To enable this port, select the **Show position/attitude
inputs** check box.

**Data Types:** `single`

### **θ** — Pitch scalar

Pitch, specified as a scalar, in rad.

#### Dependencies

To enable this port, select the **Show position/attitude
inputs** check box.

**Data Types:** `single`

### **ψ** — Yaw scalar

Yaw, specified as a scalar, in rad.

#### Dependencies

To enable this port, select the **Show position/attitude
inputs** check box.

**Data Types:** `single`

#### Velocity/Acceleration Inputs

### **α** — Angle of attack scalar

Angle of attack, specified as a scalar, in rad.

#### Dependencies

To enable this port, select the **Show
velocity/acceleration inputs** check box.

**Data Types:** `single`

### **β** — Sideslip angle scalar

Sideslip angle, specified as a scalar, in rad.

#### Dependencies

To enable this port, select the **Show
velocity/acceleration inputs** check box.

**Data Types:** `single`

### **dφ/dt** — Roll rate scalar

Roll rate, specified as a scalar, in rad/sec.

#### Dependencies

To enable this port, select the **Show
velocity/acceleration inputs** check box.

**Data Types:** `single`

### **dθ/dt** — Pitch rate scalar

Pitch rate, specified as a scalar, in rad/sec.

#### Dependencies

To enable this port, select the **Show
velocity/acceleration inputs** check box.

**Data Types:** `single`

### **dψ/dt** — Yaw rate scalar

Yaw rate, specified as a scalar, in rad/sec.

#### Dependencies

To enable this port, select the **Show
velocity/acceleration inputs** check box.

**Data Types:** `single`

### **Vcas** — Calibrated airspeed scalar

Calibrated airspeed, specified as a scalar, in knots.

#### Dependencies

To enable this port, select the **Show
velocity/acceleration inputs** check box.

**Data Types:** `single`

### **climb\_rate** — Rate of climb scalar

Rate of climb, specified as a scalar, in feet/sec.

#### Dependencies

To enable this port, select the **Show
velocity/acceleration inputs** check box.

**Data Types:** `single`

### **vnorth** — North velocity in body frame scalar

North velocity in body frame, specified as a scalar, in ft/sec.

#### Dependencies

To enable this port, select the **Show
velocity/acceleration inputs** check box.

**Data Types:** `single`

### **veast** — East velocity in body frame scalar

East velocity in body frame, specified as a scalar, in feet/sec.

#### Dependencies

To enable this port, select the **Show
velocity/acceleration inputs** check box.

**Data Types:** `single`

### **vdown** — Down velocity scalar

Down velocity, specified as a scalar, in feet/sec.

#### Dependencies

To enable this port, select the **Show
velocity/acceleration inputs** check box.

**Data Types:** `single`

### **vwind body north** — North velocity in body frame relative to local airmass scalar

North velocity in body frame relative to local airmass, specified as a scalar, in
ft/sec.

#### Dependencies

To enable this port, select the **Show
velocity/acceleration inputs** check box.

**Data Types:** `single`

### **vwind body east** — East velocity in body frame relative to local airmass scalar

East velocity in body frame relative to local airmass, specified as a scalar, in ft/sec.

#### Dependencies

To enable this port, select the **Show
velocity/acceleration inputs** check box.

**Data Types:** `single`

### **vwind body down** — Down velocity in body frame relative to airmass scalar

Down velocity in body frame relative to airmass, specified as a scalar, in ft/sec.

#### Dependencies

To enable this port, select the **Show
velocity/acceleration inputs** check box.

**Data Types:** `single`

### **AX pilot** — *X* acceleration in body frame scalar

*X* acceleration in body frame, specified as a scalar, in
ft/sec2.

#### Dependencies

To enable this port, select the **Show
velocity/acceleration inputs** check box.

**Data Types:** `single`

### **AY pilot** — *Y* acceleration in body frame scalar

*Y* acceleration in body frame, specified as a scalar, in
ft/sec2.

#### Dependencies

To enable this port, select the **Show
velocity/acceleration inputs** check box.

**Data Types:** `single`

### **AZ pilot** — *Z* acceleration in body frame scalar

*Z* acceleration in body frame, specified as a scalar, in
ft/sec2.

#### Dependencies

To enable this port, select the **Show
velocity/acceleration inputs** check box.

**Data Types:** `single`

### **stall\_warning** — Amount of stall scalar

Amount of stall [0-1], specified as a scalar.

#### Dependencies

To enable this port, select the **Show
velocity/acceleration inputs** check box.

**Data Types:** `single`

### **slip\_degree** — Slip ball deflection scalar

Slip ball deflection, specified as a scalar, in degrees.

#### Dependencies

To enable this port, select the **Show
velocity/acceleration inputs** check box.

**Data Types:** `single`

#### Control Surface Position Inputs

### **elevator** — Normalized elevator position scalar

Normalized elevator position, specified as a scalar.

#### Dependencies

To enable this port, select the **Show control surface
position inputs** check box.

**Data Types:** `single`

### **elevator\_trim\_tab** — Normalized elevator trim tab position scalar

Normalized elevator trim tab position, specified as a scalar.

#### Dependencies

To enable this port, select the **Show control surface
position inputs** check box.

**Data Types:** `single`

### **left\_flap** — Normalized left flap position scalar

Normalized left flap position, specified as a scalar.

#### Dependencies

To enable this port, select the **Show control surface
position inputs** check box.

**Data Types:** `single`

### **right\_flap** — Normalized right flap position scalar

Normalized right flap position, specified as a scalar.

#### Dependencies

To enable this port, select the **Show control surface
position inputs** check box.

**Data Types:** `single`

### **left\_aileron** — Normalized left aileron position scalar

Normalized left aileron position. specified as a scalar.

#### Dependencies

To enable this port, select the **Show control surface
position inputs** check box.

**Data Types:** `single`

### **right\_aileron** — Normalized right aileron position scalar

Normalized right aileron position, specified as a scalar.

#### Dependencies

To enable this port, select the **Show control surface
position inputs** check box.

**Data Types:** `single`

### **rudder** — Normalized rudder position scalar

Normalized rudder position, specified as a scalar.

#### Dependencies

To enable this port, select the **Show control surface
position inputs** check box.

**Data Types:** `single`

### **nose\_wheel** — Normalized nose wheel position scalar

Normalized nose wheel position, specified as a scalar.

#### Dependencies

To enable this port, select the **Show control surface
position inputs** check box.

**Data Types:** `single`

### **speedbrake** — Normalized speedbrake position scalar

Normalized speedbrake position, specified as a scalar.

#### Dependencies

To enable this port, select the **Show control surface
position inputs** check box.

**Data Types:** `single`

### **spoilers** — Normalized spoilers position scalar

Normalized spoilers position, specified as a scalar.

#### Dependencies

To enable this port, select the **Show control surface
position inputs** check box.

**Data Types:** `single`

#### Engine/Fuel Inputs

### **num\_engines** — Number of engines scalar

Number of engines, specified as a scalar.

#### Dependencies

To enable this port, select the **Show engine/fuel
inputs** check box.

**Data Types:** `uint32`

### **eng\_state** — Engine state vector

Engine state (off, cranking, running), specified as a vector.

#### Dependencies

To enable this port, select the **Show engine/fuel
inputs** check box.

**Data Types:** `uint32`

### **rpm** — Engine RPM vector

Engine RPM, specified as a vector, in rev/min.

#### Dependencies

To enable this port, select the **Show engine/fuel
inputs** check box.

**Data Types:** `single`

### **fuel\_flow** — Fuel flow vector

Fuel flow, specified as a vector, in gal/hr.

#### Dependencies

To enable this port, select the **Show engine/fuel
inputs** check box.

**Data Types:** `single`

### **fuel\_px** — Fuel pressure vector

Fuel pressure, specified as a vector, in psi.

#### Dependencies

To enable this port, select the **Show engine/fuel
inputs** check box.

**Data Types:** `single`

### **egt** — Exhaust gas temperature vector

Exhaust gas temperature, specified as a vector, in deg F.

#### Dependencies

To enable this port, select the **Show engine/fuel
inputs** check box.

**Data Types:** `single`

### **cht** — Cylinder head temperature scalar

Cylinder head temperature, specified as a vector, in deg F.

#### Dependencies

To enable this port, select the **Show engine/fuel
inputs** check box.

**Data Types:** `single`

### **mp\_osi** — Manifold pressure vector

Manifold pressure, specified as a vector, in psi.

#### Dependencies

To enable this port, select the **Show engine/fuel
inputs** check box.

**Data Types:** `single`

### **tit** — Turbine inlet temperature vector

Turbine inlet temperature, specified as a vector, in deg F.

#### Dependencies

To enable this port, select the **Show engine/fuel
inputs** check box.

**Data Types:** `single`

### **oil\_temp** — Oil temperature vector

Oil temperature, specified as a vector, in deg F.

#### Dependencies

To enable this port, select the **Show engine/fuel
inputs** check box.

**Data Types:** `single`

### **oil\_px** — Oil pressure vector

Oil pressure, specified as a vector, in psi.

#### Dependencies

To enable this port, select the **Show engine/fuel
inputs** check box.

**Data Types:** `single`

### **num\_tanks** — Number of fuel tanks scalar

Number of fuel tanks, specified as a scalar.

#### Dependencies

To enable this port, select the **Show engine/fuel
inputs** check box.

**Data Types:** `uin32`

### **fuel\_quantity** — Fuel quantity per tank vector

Fuel quantity per tank, specified as a vector, in gal.

#### Dependencies

To enable this port, select the **Show engine/fuel
inputs** check box.

**Data Types:** `single`

#### Landing Gear Inputs

### **num\_wheels** — Number of wheels scalar

Number of wheels, specified as a scalar.

#### Dependencies

To enable this port, select the **Show landing gear
inputs** check box.

**Data Types:** `uint32`

### **wow** — Weight on wheels switch vector

Weight on wheels switch, specified as a vector.

#### Dependencies

To enable this port, select the **Show landing gear
inputs** check box.

**Data Types:** `uint32`

### **gear\_pos** — Landing gear normalized position vector

Landing gear normalized position, specified as a vector.

#### Dependencies

To enable this port, select the **Show landing gear
inputs** check box.

**Data Types:** `single`

### **gear\_steer** — Landing gear normalized steering vector

Landing gear normalized steering, specified as a vector.

#### Dependencies

To enable this port, select the **Show landing gear
inputs** check box.

**Data Types:** `single`

### **gear\_compression** — Landing gear normalized compression vector

Landing gear normalized compression, specified as a vector.

#### Dependencies

To enable this port, select the **Show landing gear
inputs** check box.

**Data Types:** `single`

#### Environment Inputs

### **agl** — Altitude above ground level scalar

Altitude above ground level, specified as a scalar, in m.

#### Dependencies

To enable this port, select the **Show environment
inputs** check box.

**Data Types:** `single`

### **cur\_time** — Current UNIX® time scalar

Current UNIX time, specified as a scalar, in sec.

#### Dependencies

To enable this port, select the **Show environment
inputs** check box.

**Data Types:** `uint32`

### **warp** — Offset in seconds to UNIX time scalar

Offset in seconds to UNIX time, specified as a scalar, in sec.

#### Dependencies

To enable this port, select the **Show environment
inputs** check box.

**Data Types:** `int32`

### **visibility** — Visibility scalar

Visibility (for visual effects), specified as a scalar, in m.

#### Dependencies

To enable this port, select the **Show environment
inputs** check box.

**Data Types:** `single`
### Output

### **net\_fdm** — Packet generated for FlightGear array

Packet generated for FlightGear, specified as an array.

**Data Types:** `single` | `double` | `uint32`

## Parameters

### **Show position/altitude inputs** — Position and altitude inputs `on` (default) | `off`

Select this check box to include the position and altitude inputs in the
FlightGear `net_fdm` data packet.

#### Dependencies

Select this check box to enable these input ports.

**Signal Group 1: Position/Altitude Inputs**

| Name | Units | Type | Width | Description |
| --- | --- | --- | --- | --- |
| *`longitude`* | rad | double | 1 | Geodetic longitude |
| *`latitude`* | rad | double | 1 | Geodetic latitude |
| *`altitude`* | m | double | 1 | Altitude above sea level |
| *`theta`* | rad | single | 1 | Pitch |
| *`phi`* | rad | single | 1 | Roll |
| *`psi`* | rad | single | 1 | Yaw |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowPositionAttitudeInputs` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'on'` |

### **Show velocity/acceleration inputs** — Velocity and acceleration inputs `off` (default) | `on`

Select this check box to include the velocity and acceleration inputs in
the FlightGear `net_fdm` data packet.

#### Dependencies

Select this check box to enable these input ports.

**Signal Group 2: Velocity/Acceleration Inputs**

| Name | Units | Type | Width | Description |
| --- | --- | --- | --- | --- |
| *`alpha`* | rad | double | 1 | Angle of attack |
| *`beta`* | rad | single | 1 | Sideslip angle |
| *`dphi/dt`* | rad/sec | single | 1 | Roll rate |
| *`dtheta/dt`* | rad/sec | single | 1 | Pitch rate |
| *`dpsi/dt`* | rad/sec | single | 1 | Yaw rate |
| *`Vcas`* | knot | single | 1 | Calibrated airspeed |
| *`climb_rate`* | feet/sec | single | 1 | Rate of climb |
| *`v_north`* | feet/sec | single | 1 | North velocity in body frame |
| *`v_east`* | feet/sec | single | 1 | East velocity in body frame |
| *`v_down`* | feet/sec | single | 1 | Down velocity |
| *`v_wind_body_north`* | feet/sec | single | 1 | North velocity in body frame relative to local airmass |
| *`v_wind_body_east`* | feet/sec | single | 1 | East velocity in body frame relative to local airmass |
| *`v_wind_body_down`* | feet/sec | single | 1 | Down velocity in body frame relative to airmass |
| *`Axpilot`* | feet/sec2 | single | 1 | *X* acceleration in body frame |
| *`Aypilot`* | feet/sec2 | single | 1 | *Y* acceleration in body frame |
| *`Azpilot`* | feet/sec2 | single | 1 | *Z* acceleration in body frame |
| *`stall_warning`* | — | single | 1 | Amount of stall [0-1] |
| *`slip_deg`* | degrees | single | 1 | Slip ball deflection |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowVelocityAccelerationInputs` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Show control surface position inputs** — Control surface position inputs `off` (default) | `on`

Select this check box to include the control surface position inputs in
the FlightGear `net_fdm` data packet.

#### Dependencies

Select this check box to enable these input ports.

**Signal Group 3: Control Surface Position Inputs**

| Name | Units | Type | Width | Description |
| --- | --- | --- | --- | --- |
| *`elevator`* | 1 (dimensionless) | single | 1 | Normalized elevator position |
| *`elevator_trim_tab`* | 1 (dimensionless) | single | 1 | Normalized elevator trim tab position |
| *`left_flap`* | 1 (dimensionless) | single | 1 | Normalized left flap position |
| *`right_flap`* | 1 (dimensionless) | single | 1 | Normalized right flap position |
| *`left_aileron`* | 1 (dimensionless) | single | 1 | Normalized left aileron position |
| *`right_aileron`* | 1 (dimensionless) | single | 1 | Normalized right aileron position |
| *`rudder`* | 1 (dimensionless) | single | 1 | Normalized rudder position |
| *`nose_wheel`* | 1 (dimensionless) | single | 1 | Normalized nose wheel position |
| *`speedbrake`* | 1 (dimensionless) | single | 1 | Normalized speedbrake position |
| *`spoilers`* | 1 (dimensionless) | single | 1 | Normalized spoilers position |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowControlSurfacePositionInputs` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Show engine/fuel inputs** — Engine and fuel inputs `off` (default) | `on`

Select this check box to include the engine and fuel inputs in the
FlightGear `net_fdm` data packet.

#### Dependencies

Select this check box to enable these input ports.

**Signal Group 4: Engine/Fuel Inputs**

| Name | Units | Type | Width | Description |
| --- | --- | --- | --- | --- |
| *`num_engines`* | — | uint32 | 1 | Number of engines |
| *`eng_state`* | — | uint32 | 4 | Engine state (off, cranking, running) |
| *`rpm`* | rev/min | single | 4 | Engine RPM |
| *`fuel_flow`* | gal/hour | single | 4 | Fuel flow |
| *`fuel_px`* | psi | single | 4 | Fuel pressure |
| *`egt`* | deg F | single | 4 | Exhaust gas temperature |
| *`cht`* | deg F | single | 4 | Cylinder head temperature |
| *`mp_osi`* | psi | single | 4 | Manifold pressure |
| *`tit`* | deg F | single | 4 | Turbine inlet temperature |
| *`oil_temp`* | deg F | single | 4 | Oil temperature |
| *`oil_px`* | psi | single | 4 | Oil pressure |
| *`num_tanks`* | — | uint32 | 1 | Number of fuel tanks |
| *`fuel_quantity`* | gal | single | 4 | Fuel quantity per tank |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowEngineFuelInputs` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Show landing gear inputs** — Landing gear inputs `off` (default) | `on`

Select this check box to include the landing gear inputs in the FlightGear
`net_fdm` data packet.

#### Dependencies

Select this check box to enable these input ports.

**Signal Group 5: Landing Gear Inputs**

| Name | Units | Type | Width | Description |
| --- | --- | --- | --- | --- |
| *`num_wheels`* | — | uint32 | 1 | Number of wheels |
| *`wow`* | — | uint32 | 3 | Weight on wheels switch |
| *`gear_pos`* | — | single | 3 | Landing gear normalized position |
| *`gear_steer`* | — | single | 3 | Landing gear normalized steering |
| *`gear_compression`* | — | single | 3 | Landing gear normalized compression |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowLandingGearInputs` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Show environment inputs** — Environment inputs `off` (default) | `on`

Select this check box to include the environment inputs in the FlightGear
`net_fdm` data packet.

#### Dependencies

Select this check box to enable these input ports.

**Signal Group 6: Environment Inputs**

| Name | Units | Type | Width | Description |
| --- | --- | --- | --- | --- |
| *`agl`* | m | single | 1 | Altitude above ground level |
| *`cur_time`* | sec | uint32 | 1 | Current UNIX time |
| *`warp`* | sec | int32 | 1 | Offset in seconds to UNIX time |
| *`visibility`* | m | single | 1 | Visibility in meters (for visual effects) |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowEnvironmentInputs` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Sample time** — Sample time `1/30` (default) | scalar

Specify the sample time (-1 for inherited).

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

**Introduced before R2006a**

## Description

Generate net_fdm packet for FlightGear

The Pack net\_fdm Packet for FlightGear block creates, from
separate inputs, a FlightGear `net_fdm` data packet compatible with a
particular version of FlightGear flight simulator. This block accepts all signals
supported by the FlightGear `net_fdm` data packet. These signals are
arranged into six groups:

- Position/attitude inputs
- Velocity/acceleration inputs
- Control surface position inputs
- Engine/fuel inputs
- Landing gear inputs
- Environment inputs

To enable or disable the inputs for these groups, select the associated block
parameter. The block input ports change depending on the requested signal groups. The
block inserts zeros for packet values that are part of inactive signal groups.

The Aerospace Blockset™ product supports FlightGear versions starting from v2.6. If you are using
a FlightGear version older than 2.6, the model displays a notification from the
Simulink® Upgrade Advisor. Consider using the Upgrade Advisor to upgrade your
FlightGear version. For more information, see Supported FlightGear Versions.
