---
type: simulink-block
title: 'Spacecraft Dynamics'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Spacecraft'
documentation_page: 'spacecraftdynamics'
documentation_source_path: 'spacecraftdynamics.html'
language: en
---

# Spacecraft Dynamics

## Ports
```yaml
ports:
- name: Fb
  summary: Applied forces 3-element vector | *numSat*-by-3 array
  direction: input
  data_types: double
- name: Mb
  summary: Applied moments 3-element vector | *numSat*-by-3 array
  direction: input
  data_types: double
- name: A
  summary: External acceleration 3-element vector | *m*-by-3 array
  direction: input
  data_types: double
- name: φθψ
  summary: Moon libration angles 3-element vector
  direction: input
  data_types: double
- name: αδW
  summary: Right ascension, declination, and rotation angle 3-element vector
  direction: input
  data_types: double
- name: m
  summary: Spacecraft mass scalar | 1D array of size *numSat*
  direction: input
  data_types: double
- name: dm/dt
  summary: Rate of change of mass scalar | 1D array of size *numSat*
  direction: input
  data_types: double
- name: I
  summary: Spacecraft inertia tensor 3-by-3 array | 3-by-3-by-*numSat* array
  direction: input
  data_types: double
- name: dI/dt
  summary: Rate of change of inertia tensor matrix 3-by-3 array | 3-by-3-by-*numSat* array
  direction: input
  data_types: double
- name: Vre
  summary: Relative velocity 3-element vector | *numSat*-by-3 array
  direction: input
  data_types: double
- name: ρ
  summary: Atmospheric density scalar
  direction: input
  data_types: double
- name: F107a
  summary: 81-day average Ottawa F10.7 cm solar flux scalar
  direction: input
  data_types: double
- name: F107
  summary: Daily Ottawa F10.7 cm solar flux scalar
  direction: input
  data_types: double
- name: aph
  summary: Daily magnetic index information *N*-by-7 array
  direction: input
  data_types: double
- name: Flags
  summary: Variation flags array of 23
  direction: input
  data_types: double
- name: Cd
  summary: Atmospheric drag coefficient scalar | vector of size *numSat*
  direction: input
  data_types: double
- name: Ad
  summary: Atmospheric drag area scalar | vector of size *numSat*
  direction: input
  data_types: double
- name: Rcb, 3
  summary: Position of one or more custom bodies 3-element vector | *numCustom3rdBodies*x3-element vector
  direction: input
  data_types: double
- name: Fraction
  summary: Fraction of solar disk between 0 (full eclipse) and 1 (full sunlight) | scalar | *numSat*
  direction: input
  data_types: double
- name: RC
  summary: Reflectivity coefficient scalar or *numSat* of values in the range 1≤*RC*≤2
  direction: input
  data_types: double
- name: Asrp
  summary: Cross section area of the spacecraft scalar | *numSat*
  direction: input
  data_types: double
- name: X
  summary: Position of spacecraft 3-element vector | *numSat*-by-3 array
  direction: output
  data_types: double
- name: V
  summary: Velocity 3-element vector | *numSat*-by-3 array
  direction: output
  data_types: double
- name: A
  summary: Total inertial acceleration 3-element vector | *numSat*-by-3 array
  direction: output
  data_types: double
- name: qbody2icrf
  summary: Spacecraft attitude quaternion 4-element quaternion | *numSat*-by-4 array
  direction: output
  data_types: double
- name: DCM
  summary: Spacecraft attitude direction cosine matrix 3-by-3 array | *numSat*-by-3-by-3 array
  direction: output
  data_types: double
- name: R1,R2,R3
  summary: Spacecraft attitude Euler angles 3-element vector | *numSat*-by-3 array
  direction: output
  data_types: double
- name: ω
  summary: Angular rate of spacecraft 3-element vector | *numSat*-by-3 array
  direction: output
  data_types: double
- name: dω/dt
  summary: Body angular acceleration 3-element array | *numSat*-by-3 array
  direction: output
  data_types: double
- name: qicrf2ff
  summary: Coordinate system transformation 4-element array
  direction: output
  data_types: double
- name: tutc
  summary: Time at current time step scalar | 6-element array
  direction: output
  data_types: double
- name: Fuel Status
  summary: Fuel status scalar | *numSat*-element array
  direction: output
  data_types: double
```

### Input

### **Fb** — Applied forces 3-element vector | *numSat*-by-3 array

Force applied to the spacecraft center of mass in the body frame, specified as a
3-element vector or *numSat*-by-3 array at the current time step.
*numSat* is the number of spacecraft.

#### Dependencies

To enable this port, set the **Input body forces** parameter to
`on`.

**Data Types:** `double`

### **Mb** — Applied moments 3-element vector | *numSat*-by-3 array

Moment applied to the spacecraft with respect to mass in the body frame, specified
as a 3-element vector or *numSat*-by-3 array at the current time
step. *numSat* is the number of spacecraft.

#### Dependencies

To enable this port, set the **Input body moments** parameter
to `on`.

**Data Types:** `double`

### **A** — External acceleration 3-element vector | *m*-by-3 array

External acceleration to apply to the spacecraft with respect to the ICRF or
fixed-frame at the current timestep, specified as a 3-element vector or
*m*-by-3 array.

#### Dependencies

To enable this port, set the **Input external accelerations**
parameter to `on`.

To specify the acceleration coordinate frame, set the **External
acceleration coordinate frame** parameter.

**Data Types:** `double`

### **φθψ** — Moon libration angles 3-element vector

Moon libration angles for transformation between the ICRF and Moon-centric
fixed-frame using the Moon-centric Principal Axis (PA) system, specified as a
3-element vector. To get these values, use the Moon Libration block.

**Note**

The fixed-frame used by this block when **Central body** is set
to `Moon` is the Mean Earth/pole axis (ME) system. For more
information, see Algorithms.

#### Dependencies

To enable this port:

- Set **Central body** to
  `Moon`.
- Set the **Input Moon libration angles** parameter to
  `on`.

**Data Types:** `double`

### **αδW** — Right ascension, declination, and rotation angle 3-element vector

Central body spin axis instantaneous right ascension, declination, and rotation
angle, specified as a 3-element vector. This port is available only for custom central
bodies.

#### Dependencies

To enable this port:

- Set **Central body** to
  `Custom`.
- Set **Central body spin axis source** to
  `Port`.

**Data Types:** `double`

### **m** — Spacecraft mass scalar | 1D array of size *numSat*

Spacecraft mass at the current timestep. *numSat* is the number
of spacecraft.

#### Dependencies

To enable this port, set **Mass type** to `Custom
Variable`.

**Data Types:** `double`

### **dm/dt** — Rate of change of mass scalar | 1D array of size *numSat*

Rate of change of mass (positive if accreted, negative if ablated) at the current
timestep, specified as a scalar or 1D array of size *numSat*.
*numSat* is the number of spacecraft.

#### Dependencies

To enable this port, set **Mass type** to `Simple
Variable`.

**Data Types:** `double`

### **I** — Spacecraft inertia tensor 3-by-3 array | 3-by-3-by-*numSat* array

Spacecraft inertia tensor, specified as a 3-by-3 array or
3-by-3-by-*numSat* array at the current timestep.
*numSat* is the number of spacecraft.

#### Dependencies

To enable this port, set **Mass type** to `Custom
Variable`.

**Data Types:** `double`

### **dI/dt** — Rate of change of inertia tensor matrix 3-by-3 array | 3-by-3-by-*numSat* array

Rate of change of inertia tensor matrix, specified as a 3-by-3 array or
3-by-3-by-*numSat* array at the current time step.
*numSat* is the number of spacecraft.

#### Dependencies

To enable this port, set **Mass type** to `Custom
Variable`.

**Data Types:** `double`

### **Vre** — Relative velocity 3-element vector | *numSat*-by-3 array

Relative velocity at which the mass is accreted to or ablated from the body in
body-fixed axes, specified as a 3-element vector or *numSat*-by-3
array. *numSat* is the number of spacecraft.

#### Dependencies

To enable this port:

- Set **Mass type** to `Custom
  Variable` or `Simple Variable`.
- Set the **Include mass flow relative velocity** parameter
  to `on`.

**Data Types:** `double`

### **ρ** — Atmospheric density scalar

Atmospheric density to calculate acceleration due to atmospheric drag.

#### Dependencies

To enable this port:

- Set the **Central Body** parameter to
  `Earth`.
- Set the **Include atmospheric drag** parameter to
  `on`.
- Set the **Atmospheric density source** parameter to
  `Port`.

**Data Types:** `double`

### **F107a** — 81-day average Ottawa F10.7 cm solar flux scalar

81-day average Ottawa F10.7 cm solar flux, centered on the current day specified
in **Start date/time**. These F107 Average values correspond to the
10.7 cm radio flux at the actual distance of the Earth from the Sun. This site
provides both classes of values:

https://www.ngdc.noaa.gov/stp/space-weather/solar-data/solar-features/solar-radio/noontime-flux/penticton/

#### Dependencies

To enable this port:

- Set the **Central Body** parameter to
  `Earth`.
- Set the **Include atmospheric drag** parameter to
  `on`.
- Set the **Atmospheric density source** parameter to
  `Dialog`.

**Data Types:** `double`

### **F107** — Daily Ottawa F10.7 cm solar flux scalar

Daily Ottawa F10.7 cm solar flux, centered on the current day specified in
**Start date/time**. The f107Daily values do not correspond to the
radio flux at 1 AU. This site provides both classes of values:

https://www.ngdc.noaa.gov/stp/space-weather/solar-data/solar-features/solar-radio/noontime-flux/penticton/

#### Dependencies

To enable this port:

- Set the **Central Body** parameter to
  `Earth`.
- Set the **Include atmospheric drag** parameter to
  `on`.
- Set the **Atmospheric density source** parameter to
  `Dialog`.

**Data Types:** `double`

### **aph** — Daily magnetic index information *N*-by-7 array

Daily magnetic index information (aph), specified as an *N*-by-7
array. The magnetic index information consists of:

|  |
| --- |
| Daily magnetic index (AP) |
| 3 hour AP for current time |
| 3 hour AP for 3 hours before current time |
| 3 hour AP for 6 hours before current time |
| 3 hour AP for 9 hours before current time |
| Average of eight 3 hour AP indices from 12 to 33 hours before current time |
| Average of eight 3 hour AP indices from 36 to 57 hours before current time |

The effects of daily magnetic index are not large or established below 80,000 m.
For more information, see Limitations
on NRLMSISE-00 Atmosphere Model.

#### Dependencies

To enable this port:

- Set the **Central Body** parameter to
  `Earth`.
- Set the **Include atmospheric drag** parameter to
  `on`.
- Set the **Atmospheric density source** parameter to
  `Dialog`.

**Data Types:** `double`

### **Flags** — Variation flags array of 23

Variation flags, specified as an array of 23, to enable or disable particular
variations for the outputs. You can specify one of the following values for a field.
The default value for each field is `1`.

- 0.0

  Removes the value effect on the output.
- 1.0

  Applies the main and the cross-term effects of that value on the output.
- 2.0

  Applies only the cross-term effect of that value on the output.

| Field | Description |
| --- | --- |
| `Flags(1)` | F10.7 effect on mean |
| `Flags(2)` | Independent of time |
| `Flags(3)` | Symmetrical annual |
| `Flags(4)` | Symmetrical semiannual |
| `Flags(5)` | Asymmetrical annual |
| `Flags(6)` | Asymmetrical semiannual |
| `Flags(7)` | Diurnal |
| `Flags(8)` | Semidiurnal |
| `Flags(9)` | Daily AP. If you set this field to -1, the block uses the entire matrix of magnetic index information (APH) instead of `APH(:,1)` |
| `Flags(10)` | All UT, longitudinal effects |
| `Flags(11)` | Longitudinal |
| `Flags(12)` | UT and mixed UT, longitudinal |
| `Flags(13)` | Mixed AP, UT, longitudinal |
| `Flags(14)` | Terdiurnal |
| `Flags(15)` | Departures from diffusive equilibrium |
| `Flags(16)` | All exospheric temperature variations |
| `Flags(17)` | All variations from 120,000 meter temperature (TLB) |
| `Flags(18)` | All lower thermosphere (TN1) temperature variations |
| `Flags(19)` | All 120,000 meter gradient (S) variations |
| `Flags(20)` | All upper stratosphere (TN2) temperature variations |
| `Flags(21)` | All variations from 120,000 meter values (ZLB) |
| `Flags(22)` | All lower mesosphere temperature (TN3) variations |
| `Flags(23)` | Turbopause scale height variations |

#### Dependencies

To enable this port:

- Set the **Central Body** parameter to
  `Earth`.
- Set the **Include atmospheric drag** parameter to
  `on`.
- Set the **Atmospheric density source** parameter to
  `Dialog`.
- Set the **Flags source** parameter to
  `Port`.

**Data Types:** `double`

### **Cd** — Atmospheric drag coefficient scalar | vector of size *numSat*

Atmospheric drag coefficient, specified as a scalar or vector of size
*numSat*.

#### Dependencies

To enable this port:

- Set the **Central Body** parameter to
  `Earth`.
- Set the **Include atmospheric drag** parameter to
  `on`.
- Set the **Drag coefficient source** parameter to
  `Port`.

**Data Types:** `double`

### **Ad** — Atmospheric drag area scalar | vector of size *numSat*

Atmospheric drag area, specified as a scalar or vector of size
*numSat*.

#### Dependencies

To enable this port:

- Set the **Central Body** parameter to
  `Earth`.
- Set the **Include atmospheric drag** parameter to
  `on`.
- Set the **Drag area source** parameter to
  `Port`.

**Data Types:** `double`

### **Rcb, 3** — Position of one or more custom bodies 3-element vector | *numCustom3rdBodies*x3-element vector

Position of one or more custom bodies with respect to the current central body, in
the ICRF coordinate frame. *numCustom3rdBodies* is the number of
custom bodies. For more information, see **Custom
gravitational parameter (m^3/s^2)**.

#### Dependencies

To enable this port:

- Set the **Include third body gravity** parameter to
  `on`.
- Set the **Custom** parameter to
  `on`.

**Data Types:** `double`

### **Fraction** — Fraction of solar disk between `0` (full eclipse) and `1` (full sunlight) | scalar | *numSat*

Fraction of solar disk visible from the spacecraft position.
*numSat* is the number of spacecraft.

#### Dependencies

To enable this port:

- Set the **Include solar radiation pressure (SRP)**
  parameter to `on`.
- Set **Eclipse fraction source** to
  `Port`.

**Data Types:** `double`

### **RC** — Reflectivity coefficient scalar or *numSat* of values in the range `1`≤*RC*≤`2`

Reflectivity coefficient, specified as a scalar or *numSat* of
values in the range
`1`≤*RC*≤`2`.
*numSat* is the number of spacecraft.

#### Dependencies

To enable this port:

- Set the **Include solar radiation pressure (SRP)**
  parameter to `on`.
- Set the **Reflectivity coefficient source** parameter to
  `Port`.

**Data Types:** `double`

### **Asrp** — Cross section area of the spacecraft scalar | *numSat*

Cross section area of the spacecraft seen by the Sun, specified as a scalar or
*numSat*. The block uses this value to calculate the acceleration
due to solar radiation pressure.

#### Dependencies

To enable this port:

- Set the **Include solar radiation pressure (SRP)**
  parameter to `on`.
- Set **SRP area source** parameter to
  `Port`.

**Data Types:** `double`
### Output

### **X** — Position of spacecraft 3-element vector | *numSat*-by-3 array

Position of the spacecraft with respect to the ICRF or fixed-frame outport
coordinate frame, returned as a 3-element vector or *numSat*-by-3
array at the current time step. *numSat* is the number of
spacecraft.

#### Dependencies

- To change the output coordinate frame for this port, set the **State
  vector output coordinate frame** parameter.
- The size of the initial conditions provided in the
  **Mass**, **Orbit**, or
  **Attitude** tab control the port dimension.

**Data Types:** `double`

### **V** — Velocity 3-element vector | *numSat*-by-3 array

Velocity of the spacecraft with respect to the ICRF or fixed-frame outport
coordinate frame, returned as a 3-element vector or *numSat*-by-3
array at the current time step. *numSat* is the number of
spacecraft.

#### Dependencies

- To change the output coordinate frame for this port, set the **State
  vector output coordinate frame** parameter.
- The size of the initial conditions provided in the
  **Mass**, **Orbit**, or
  **Attitude** tab control the port dimension.

**Data Types:** `double`

### **A** — Total inertial acceleration 3-element vector | *numSat*-by-3 array

Total inertial acceleration of the spacecraft with respect to the ICRF, returned
as a 3-element vector or *numSat*-by-3 array at the current timestep.
*numSat* is the number of spacecraft.

#### Dependencies

- To enable this port, set the **Output total inertial
  acceleration** parameter to `on`.
- The size of the initial conditions provided in the
  **Orbit** tab control the port dimension.

**Data Types:** `double`

### **qbody2icrf** — Spacecraft attitude quaternion 4-element quaternion | *numSat*-by-4 array

Spacecraft attitude quaternion, returned as a (scalar first) quaternion rotation
from the body axis to the outport frame, as a 4-element quaternion, or
*numSat*-by-4 array (scalar first) at the current time step.
*numSat* is the number of spacecraft.

#### Dependencies

The coordinate frame and attitude format of this port depends on these
settings:

- To specify the attitude reference coordinate frame, set the
  **Attitude reference coordinate frame** parameter.
- Set **Attitude representation** to
  `Quaternion`.

**Data Types:** `double`

### **DCM** — Spacecraft attitude direction cosine matrix 3-by-3 array | *numSat*-by-3-by-3 array

Spacecraft attitude direction cosine matrix (DCM), returned as a3-by-3 array or
*numSat*-by-3-by-3 array. *numSat* is the number
of spacecraft.

#### Dependencies

The coordinate frame and attitude format of this port depends on these
settings:

- To specify the attitude reference coordinate frame, set the
  **Attitude reference coordinate frame** parameter.
- Set **Attitude representation** to
  `DCM`.

**Data Types:** `double`

### **R1,R2,R3** — Spacecraft attitude Euler angles 3-element vector | *numSat*-by-3 array

Spacecraft attitude Euler angles, returned as a 3-element vector or
*numSat*-by-3 array. *numSat* is the number of
spacecraft.

#### Dependencies

The coordinate frame and attitude format of this port depend on these
settings:

- To specify the attitude reference coordinate frame, set the
  **Attitude reference coordinate frame** parameter.
- Set **Attitude representation** to `Euler
  angles`.

**Data Types:** `double`

### **ω** — Angular rate of spacecraft 3-element vector | *numSat*-by-3 array

Angular rate of the spacecraft relative to the attitude reference coordinate
frame, returned as a 3-element vector or *numSat*-by-3 array,
expressed as body axis angular rates PQR. *numSat* is the number of
spacecraft.

#### Dependencies

The attitude reference coordinate frame depends on the **Attitude
reference coordinate frame** parameter.

**Data Types:** `double`

### **dω/dt** — Body angular acceleration 3-element array | *numSat*-by-3 array

Body angular acceleration relative to the ICRF frame, returned as a 3-element
array or *numSat*-by-3 array. *numSat* is the number
of spacecraft.

#### Dependencies

To enable this port, set the **Output total inertial angular
acceleration** parameter to `on`.

The attitude reference coordinate frame depends on the **Attitude
reference coordinate frame** parameter.

**Data Types:** `double`

### **qicrf2ff** — Coordinate system transformation 4-element array

Coordinate system transformation between the ICRF and fixed-frame coordinate
system at the current timestep, returned as a 4-element array.

#### Dependencies

To enable this port, set the **Output quaternion (ICRF to
Fixed-frame)** parameter to `on`.

**Data Types:** `double`

### **tutc** — Time at current time step scalar | 6-element array

Time at current time step, returned as a:

- scalar — If you specify the **Start data/time** parameter as
  a Julian date.
- 6-element array — If you specify the **Start data/time**
  parameter as a Gregorian date with six elements (year, month, day, hours, minutes,
  seconds).

This value equals the **Start date/time** parameter value plus
the elapsed simulation time.

#### Dependencies

To enable this parameter, set the **Output current date/time (UTC Julian
date)** parameter to `on`.

**Data Types:** `double`

### **Fuel Status** — Fuel status scalar | *numSat*-element array

Fuel tank status at the current timestep, returned as a scalar or
*numSat*-element array, returned as:

- `1` — Tank is full.
- `0` — Tank is not full or empty.
- `-1` — Tank is empty.

*numSat* is the number of spacecraft.

#### Dependencies

To enable this port:,

- Set **Mass type** to `Simple
  Variable`.
- Set the **Output fuel tank status** parameter to
  `on`.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Input body forces
  summary: Option to enable external forces on (default) | off
  group: Main
  block_parameter: forcesin
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Input body moments
  summary: Option to enable external moments on (default) | off
  group: Main
  block_parameter: momentsIn
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Input external accelerations
  summary: Option to input additional force accelerations off (default) | on
  group: Main
  block_parameter: accelIn
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: External acceleration coordinate frame
  summary: Frame for acceleration input port ICRF (default) | Fixed-frame
  group: Main
  block_parameter: accelFrame
  type: character vector
  values: '''ICRF'' | ''Fixed-frame'''
  default: '''ICRF'''
- name: State vector output coordinate frame
  summary: Position and velocity state output port coordinate frame ICRF (default) | Fixed-frame
  group: Main
  block_parameter: outportFrame
  type: character vector
  values: '''ICRF'' | ''Fixed-frame'''
  default: '''ICRF'''
- name: Output total inertial acceleration
  summary: Option to enable total acceleration port off (default) | on
  group: Main
  block_parameter: AccelOut
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Start date/time (UTC Julian date)
  summary: Initial start time for simulation juliandate (2020, 1, 1, 12, 0, 0) (default) | valid scalar Julian date | valid
    Gregorian date including year, month, day, hours, minutes, seconds as 1D or 6-element array for Gregorian dates
  group: Main
  block_parameter: startDate
  type: character vector
  values: '''juliandate(2020, 1, 1, 12, 0, 0)'' | valid scalar Julian date | valid Gregorian date including year, month, day,
    hours, minutes, seconds as 1D or 6-element array'
  default: '''juliandate(2020, 1, 1, 12, 0, 0)'''
- name: Output current date/time (UTC Julian date)
  summary: Option to add output port tutc on (default) | off
  group: Main
  block_parameter: dateOut
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Action for out-of-range input
  summary: Out-of-range block behavior Warning (default) | Error | None
  group: Main
  block_parameter: action
  type: character vector
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''Warning'''
- name: Mass type
  summary: Spacecraft mass type Fixed (default) | Simple Variable | Custom Variable
  group: Mass
  block_parameter: massType
  type: character vector
  values: '''Fixed'' | ''Simple Variable'' | ''Custom Variable'''
  default: '''Fixed'''
- name: Mass
  summary: Initial mass of rigid body spacecraft 4.0 (default) | scalar | vector of size *numSat*
  group: Mass
  block_parameter: mass
  type: character vector
  values: scalar | vector of size *numSat*
  default: '''4.0'''
- name: Empty mass
  summary: Spacecraft empty mass 3.5 (default) | scalar | vector of size *numSat*
  group: Mass
  block_parameter: emptyMass
  type: character vector
  values: 1D array of size *numSat* | 1D array of size *numSat*
  default: '''3.5'''
- name: Full mass
  summary: Spacecraft full mass 4.0 (default) | scalar | vector of size *numSat*
  group: Mass
  block_parameter: fullMass
  type: character vector
  values: scalar | vector of size *numSat*
  default: '''4.0'''
- name: Inertia tensor
  summary: Inertia tensor matrix [0.2273, 0, 0; 0 0.2273 0; 0 0 .0040] (default) | 3-by-3 array | 3-by-3-by-*numSat* array
  group: Mass
  block_parameter: inertia
  type: character vector
  values: '''[0.2273, 0, 0; 0 0.2273 0; 0 0 .0040]'' | 3-by-3 array | 3-by-3-by-*numSat* array'
  default: '''[0.2273, 0, 0; 0 0.2273 0; 0 0 .0040]'''
- name: Empty inertia tensor
  summary: Empty inertia tensor matrix [0.1989, 0, 0; 0 0.1989 0; 0 0 .0035] (default) | 3-by-3 array | 3-by-3-by-*numSat*
    array
  group: Mass
  block_parameter: emptyInertia
  type: character vector
  values: 3-by-3 array | 3-by-3-by-*numSat* array
  default: '[0.1989, 0, 0; 0 0.1989 0; 0 0 .0035]'
- name: Full inertia tensor
  summary: Full inertia tensor matrix [0.2273, 0, 0; 0, 0.2273, 0; 0, 0, .0040] (default) | 3-by-3 array | 3-by-3-by-*numSat*
    array
  group: Mass
  block_parameter: fullInertia
  type: character vector
  values: 3-by-3 array | 3-by-3-by-*numSat* array
  default: '[0.2273, 0, 0; 0, 0.2273, 0; 0, 0, .0040]'
- name: Include mass flow relative velocity
  summary: Option to enable mass flow velocity off (default) | on
  group: Mass
  block_parameter: useMassFlowRelativeVelocity
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Limit mass flow when mass is empty or full
  summary: Option to limit mass flow on (default) | off
  group: Mass
  block_parameter: limitMassFlow
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Output fuel tank status
  summary: Option to enable fuel tank status on (default) | off
  group: Mass
  block_parameter: outputFuelStatus
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Initial state format
  summary: Input method for initial states of orbit Orbital elements (default) | ICRF state vector | Fixed-frame state vector
  group: Orbit
  block_parameter: stateFormatNum when propagator is set to High precision (numerical)
  type: character vector
  values: '''Orbital elements'' | ''Orbital elements'' | ''ICRF state vector'' | ''Fixed-frame state'' when propagator is
    set to ''High precision (numerical)'''
  default: '''Orbital elements'''
- name: Orbit type
  summary: Orbit classification Keplerian (default) | Elliptical equatorial | Circular | Circular equatorial
  group: Orbit
  block_parameter: orbitType
  type: character vector
  values: '''Keplerian'' | ''Elliptical equatorial'' | ''Circular inclined'' | ''Circular equatorial'''
  default: '''Keplerian'''
- name: Semi-major axis
  summary: Half of major axis of ellipse 6786000 (default) | scalar | 1D array of size *numSat*
  group: Orbit
  block_parameter: semiMajorAxis
  type: character vector
  values: scalar | 1D array of size *numSat*
  default: '''6786000'''
- name: Eccentricity
  summary: Deviation of orbit 0.01 (default) | scalar | value between 0 and 1, or greater than 1 for Keplerian orbit type
    | 1D array of size *numSat*
  group: Orbit
  block_parameter: eccentricity
  type: character vector
  values: 0.01 | scalar | value between 0 and 1, or greater than 1 for Keplerian orbit type | 1D array of size *numSat*
  default: '''0.01'''
- name: Inclination
  summary: Tilt angle of orbital plane 50 (default) | scalar | 1D array of size *numSat* | degrees between 0 and 180 | radians
    between 0 and pi
  group: Orbit
  block_parameter: inclination
  type: character vector
  values: 50 | scalar | 1D array of size *numSat* | degrees between 0 and 180 | radians between 0 and pi
  default: '''50'''
- name: RAAN
  summary: Angular distance in equatorial plane 95 (default) | scalar value between 0 and 360 | 1D array of size *numSat*
  group: Orbit
  block_parameter: raan
  type: character vector
  values: '''95'' | scalar value between 0 and 360 | 1D array of size *numSat*'
  default: '''95'''
- name: Argument of periapsis
  summary: Angle from spacecraft ascending node to periapsis 93 (default) | value between 0 and 360 | 1D array of size *numSat*
  group: Orbit
  block_parameter: argPeriapsis
  type: character vector
  values: 93 | scalar value between 0 and 360 | 1D array of size *numSat*
  default: '''93'''
- name: True anomaly
  summary: Angle between periapsis and initial position of spacecraft 203 (default) | scalar value between 0 and 360 | 1D
    array of size *numSat*
  group: Orbit
  block_parameter: trueAnomaly
  type: character vector
  values: '''203'' | scalar value between 0 and 360 | 1D array of size *numSat*'
  default: '''203'''
- name: Argument of latitude
  summary: Angle between ascending node and initial position of spacecraft 200 (default) | scalar | value between 0 and 360
    | 1D array of size *numSat*
  group: Orbit
  block_parameter: argLat
  type: character vector
  values: '''200'' | scalar value between 0 and 360 | 1D array of size *numSat*'
  default: '''200'''
- name: Longitude of periapsis
  summary: Angle between ICRF *x*-axis and eccentricity vector 100 (default) | scalar | value between 0 and 360 | 1D array
    of size *numSat*
  group: Orbit
  block_parameter: lonPeriapsis
  type: character vector
  values: 100 | scalar value between 0 and 360 | 1D array of size *numSat*
  default: '''100'''
- name: True longitude
  summary: Angle between ICRF *x*-axis and initial position of spacecraft 150 (default) | scalar | value between 0 and 360
    | 1D array of size *numSat* | *numSat*-by-3 vector
  group: Orbit
  block_parameter: trueLon
  type: character vector
  values: '''150'' | scalar value between 0 and 360 | 1D array of size *numSat* | *numSat*-by-3 vector'
  default: '''150'''
- name: ICRF position
  summary: Cartesian position vector of spacecraft [3649700.0 3308200.0 -4676600.0] (default) | 3-element vector | | *numSat*-by-3
    array
  group: Orbit
  block_parameter: inertialPosition
  type: character vector
  values: '[3649700.0 3308200.0 -4676600.0] | 3-element vector | *numSat*-by-3 array'
  default: '''[3649700.0 3308200.0 -4676600.0]'''
- name: ICRF velocity
  summary: Cartesian velocity vector of spacecraft [-2750.8 6666.4 2573.4] (default) | 3-element vector | *numSat*-by-3 array
  group: Orbit
  block_parameter: inertialVelocity
  type: character vector
  values: '[-2750.8 6666.4 2573.4] | 3-element vector | 2-D array of size *numSat*-by-3 array'
  default: '''[-2750.8 6666.4 2573.4]'''
- name: Fixed-frame position
  summary: Position vector of spacecraft [-4142689.0 -2676864.7 -4669861.6] (default) | 3-element vector | *numSat*-by-3 array
  group: Orbit
  block_parameter: fixedPosition
  type: character vector
  values: '''[-4142689.0 -2676864.7 -4669861.6]'' | 3-element vector for single spacecraft | *numSat*-by-3 array'
  default: '''[-2750.8 6666.4 2573.4]'''
- name: Fixed-frame velocity
  summary: Velocity vector of spacecraft [1452.7 -6720.7 2568.1] (default) | 3-element vector | *numSat*-by-3 array
  group: Orbit
  block_parameter: fixedVelocity
  type: character vector
  values: '''[1452.7 -6720.7 2568.1]'' | 3-element vector | *numSat*-by-3 array'
  default: '''[1452.7 -6720.7 2568.1]'''
- name: Attitude reference coordinate frame
  summary: Attitude and angular rate coordinate frame ICRF (default) | Fixed-frame | NED | LVLH
  group: Attitude
  block_parameter: attitudeFrame
  type: character vector
  values: '''ICRF'' | ''Fixed-frame'' | ''NED'' | ''LVLH'''
  default: '''ICRF'''
- name: Attitude representation
  summary: Orientation format Quaternion (default) | DCM | Euler angles
  group: Attitude
  block_parameter: attitudeFrame
  type: character vector
  values: '''Quaternion'' | ''DCM'' | ''Euler angles'''
  default: '''Quaternion'''
- name: Initial body attitude
  summary: Spacecraft initial attitude [1, 0, 0, 0] (default) | 4-element vector | *numSat*-by-4 array | 3-by-3 array | *numSat*-by-3-by-3
    array
  group: Attitude
  block_parameter: attitude
  type: character vector
  values: 4-element vector | *numSat*-by-4 array | 3-by-3 array | *numSat*-by-3-by-3 array | 3-element array | *numSat*-by-3
    array
  default: '''[1, 0, 0, 0]'''
- name: Angle rotation order
  summary: Angle rotation order ZYX (default) | ZYX | ZYZ | ZXY | ZXZ | YXZ | YXY | YZX | YZY | XYZ | XYX | XZY | XZX
  group: Attitude
  block_parameter: rotationOrder
  type: character vector
  values: '''ZYX'' | ''ZYZ'' |''ZXY'' | ''ZXZ'' | ''YXZ'' | ''YXY'' | ''YZX'' | ''YZY'' | ''XYZ'' | ''XYX'' | ''XZY'' | ''XZX'''
  default: '''ZYX'''
- name: Initial body angular rates PQR
  summary: Initial body-fixed angular rates [0, 0, 0] (default) | 3-element vector | *numSat*-by-3 array
  group: Attitude
  block_parameter: attitudeRate
  type: character vector
  values: 3-element vector | *numSat*-by-3 array
  default: '[0, 0, 0]'
- name: Output total inertial angular acceleration
  summary: Option to enable total vehicle acceleration off (default) | on
  group: Attitude
  block_parameter: angAccelOut
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Include gravity gradient torque
  summary: Option to enable gravity gradient torque on (default) | off
  group: Attitude
  block_parameter: angAccelOut
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Central body
  summary: Celestial body around which spacecraft orbits Earth (default) | Moon | Mercury | Venus | Mars | Jupiter | Saturn
    | Uranus | Neptune | Sun | Custom
  group: Central Body
  block_parameter: centralBody
  type: character vector
  values: '''Earth'' | ''Moon'' |''Mercury'' | ''Venus'' | ''Mars'' | ''Jupiter'' | ''Saturn'' | ''Uranus'' | ''Neptune''
    | ''Sun'' | ''Custom'' |'
  default: '''Earth'''
- name: Gravitational potential model
  summary: Gravity model for central body Spherical harmonics when Central body set to Earth, Moon, Mars, or Custom, Oblate
    ellipsoid when Central body set to Mercury, Venus, Jupiter, Saturn, Uranus, or Neptune (default) | Point-mass | Oblate
    ellipsoid (J2)
  group: Central Body
  block_parameter: gravityModel when centralBody set to 'Earth', 'Moon', 'Mars', or 'Custom' | gravityModelnoSH when centralBody
    set to Mercury, Venus, Jupiter, Saturn, Uranus, or Neptune
  type: character vector
  values: '''Spherical harmonics'' | ''Point-mass'' | ''Oblate ellipsoid (J2)'' when centralBody set to ''Earth'', ''Moon'',
    ''Mars'', or ''Custom''; ''Point-mass'' | ''Oblate ellipsoid (J2)'' when centralBody set to Mercury, Venus, Jupiter, Saturn,
    Uranus, or Neptune'
  default: '''Spherical harmonics'' when centralBody set to ''Earth'', ''Moon'', ''Mars'', or ''Custom''; ''Oblate ellipsoid
    (J2)'' when centralBody set to Mercury, Venus, Jupiter, Saturn, Uranus, or Neptune'
- name: Spherical harmonic model
  summary: Spherical harmonic model EGM2008 for Central body set to Earth, LP-100K for Central body set to Moon, GMM2B for
    Central body set to Mars, (default) | EGM96 | EIGEN-GL04C | LP-165P
  group: Central Body
  block_parameter: '''earthSH'' when centralBody set to ''Earth'' | ''moonSH'' when centralBody set to ''Moon'' | ''marsSH''
    when centralBody set to ''Mars'''
  type: character vector
  values: '''EGM2008'' | ''EGM96'' | ''EIGEN-GL04C'' when centralBody set to ''earthSH''; ''LP-100K'' | ''LP-165P'' when centralBody
    set to ''moonSH''; ''GMM2B'' when centralBody set to ''marsSH'''
  default: '''Spherical harmonics'''
- name: Rotational rate
  summary: Rotational rate 4.06124975e-3 (default) | scalar
  group: Central Body
  block_parameter: '''customOmega'''
  type: character vector
  values: '''4.06124975e-3'' | scalar'
  default: '''4.06124975e-3'''
- name: Spherical harmonic coefficient file
  summary: Harmonic coefficient MAT file aerogmm2b.mat (default) | harmonic coefficient MAT file
  group: Central Body
  block_parameter: shFile
  type: character vector
  values: '''aerogmm2b.mat'' | harmonic coefficient MAT file'
  default: '''aerogmm2b.mat'''
- name: Degree
  summary: Degree of harmonic model 120 (default) | scalar | maximum of 2159
  group: Central Body
  block_parameter: shDegree
  type: character vector
  values: '''80'' | scalar'
  default: '''80'''
- name: Use Earth orientation parameters (EOPs)
  summary: Option to use Earth orientation parameters on (default) | off
  group: Central Body
  block_parameter: useEOPs
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: IERS EOP data file
  summary: Earth orientation data aeroiersdata.mat (default) | MAT file
  group: Central Body
  block_parameter: eopFile
  type: character vector
  values: '''aeroiersdata.mat'' | MAT-file'
  default: '''aeroiersdata.mat'''
- name: Input Moon libration angles
  summary: Moon libration Euler angle rate off (default) | on
  group: Central Body
  block_parameter: useMoonLib
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Output quaternion (ICRF to Fixed-frame)
  summary: Option to add output transformation quaternion port off (default) | on
  group: Central Body
  block_parameter: outputTransform
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Central body spin axis source
  summary: Central body spin source Port (default) | Dialog
  group: Central Body
  block_parameter: cbPoleSrc
  type: character vector
  values: '''Port'' | ''Dialog'''
  default: '''Port'''
- name: Spin axis right ascension (RA) at J2000
  summary: Right ascension of central body spin axis at J2000 317.68143 (default) | double scalar
  group: Central Body
  block_parameter: cbRA
  type: character vector
  values: '''317.68143'' | double scalar'
  default: '''317.68143'''
- name: Spin axis RA rate (deg/century)
  summary: Right ascension rate of central body spin axis -0.1061 (default) | double scalar
  group: Central Body
  block_parameter: cbRARate
  type: character vector
  values: '''-0.1061'' | double scalar'
  default: '''-0.1061'''
- name: Spin axis declination (Dec) at J2000
  summary: Declination of central body spin axis at J2000 52.88650 (default) | double scalar
  group: Central Body
  block_parameter: cbDec
  type: character vector
  values: '''52.88650'' | double scalar'
  default: '''52.88650'''
- name: Spin axis Dec rate (deg/century)
  summary: Declination rate of central body spin axis -0.0609 (default) | double scalar
  group: Central Body
  block_parameter: cbDecRate
  type: character vector
  values: '''-0.0609'' | double scalar'
  default: '''-0.0609'''
- name: Initial rotation angle at J2000
  summary: Rotation angle of central body *x*-axis 176.630 (default) | double scalar
  group: Central Body
  block_parameter: cbRotAngle
  type: character vector
  values: '''176.630'' | double scalar'
  default: '''176.630'''
- name: Rotation rate (deg/day)
  summary: Rotation rate of central body *x*-axis 350.89198226 (default) | double scalar
  group: Central Body
  block_parameter: cbRotRate
  type: character vector
  values: '''350.89198226'' | double scalar'
  default: '''350.89198226'''
- name: Equatorial radius
  summary: Equatorial radius 3.3962e6 (default) | double scalar
  group: Central Body
  block_parameter: customR
  type: character vector
  values: '''3.3962e6'' | double scalar'
  default: '''3.3962e6'''
- name: Flattening
  summary: Flattening of planet 0.00589 (default) | double scalar
  group: Central Body
  block_parameter: customF
  type: character vector
  values: '''0.00589'' | double scalar'
  default: '''0.00589'''
- name: Gravitational parameter
  summary: Gravitational parameter 4.305e13 (default) | double scalar
  group: Central Body
  block_parameter: customMu
  type: character vector
  values: '''4.305e13'' | double scalar'
  default: '''4.305e13'''
- name: Second degree zonal harmonic (J2)
  summary: Most significant or largest spherical harmonic term 1.0826269e-03 (default) | double scalar
  group: Central Body
  block_parameter: customJ2
  type: character vector
  values: '''1.0826269e-03'' | double scalar'
  default: '''1.0826269e-03'''
- name: Include atmospheric drag
  summary: Option to include atmospheric drag off (default) | on
  group: Drag
  block_parameter: useDrag
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Atmospheric density source
  summary: Source of atmospheric density value Dialog (default) | Port
  group: Drag
  block_parameter: atmosSrc
  type: character vector
  values: '''Dialog'' | ''Port'''
  default: '''Dialog'''
- name: Atmospheric model
  summary: Atmospheric model NRLMSISE-00 (default)
  group: Drag
  block_parameter: atmosModel
  type: character vector
  values: '''NRLMSISE-00'''
  default: '''NRLMSISE-00'''
- name: Flux source
  summary: Source of space weather data Dialog (default) | Port
  group: Drag
  block_parameter: fluxSrc
  type: character vector
  values: '''Dialog'' | ''Port'''
  default: '''Dialog'''
- name: Space weather data file
  summary: MAT file of space weather data aeroSpaceWeatherData.mat (default) | MAT file name
  group: Drag
  block_parameter: SpaceWeatherDataFile
  type: character vector
  values: '''aeroSpaceWeatherData.mat'' | MAT file name'
  default: '''aeroSpaceWeatherData.mat'''
- name: F10.7 extrapolation method
  summary: Extrapolation method for f107Average and f107Daily None - clip (default) | Constant | Least squares fit
  group: Drag
  block_parameter: F107ExtrapMethod
  type: character vector
  values: '''None - clip'' | ''Constant'' | ''Least squares fit'''
  default: '''None - clip'''
- name: Magnetic index extrapolation method
  summary: Extrapolation method for magnetic index information None - clip (default) | Constant | IGRF
  group: Drag
  block_parameter: MagneticIndexExtrapMethod
  type: character vector
  values: '''None - clip'' | ''Constant'' | ''IGRF'''
  default: '''None - clip'''
- name: Flags source
  summary: Variation flag source Dialog (default) | Port
  group: Drag
  block_parameter: fluxFlagsSrc
  type: character vector
  values: '''Dialog'' | ''Port'''
  default: '''Dialog'''
- name: Flags
  summary: Variation flags ones(1,23) (default)
  group: Drag
  block_parameter: fluxFlags
  type: character vector
  values: '''ones(1,23)'''
  default: '''ones(1,23)'''
- name: Include anomalous oxygen in density calculation
  summary: Option to include anomalous oxygen in density calculation off (default) | on
  group: Drag
  block_parameter: useOxygen
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Drag coefficient source
  summary: Source of drag coefficient Dialog (default) | Port
  group: Drag
  block_parameter: dragCoeffSrc
  type: character vector
  values: '''Dialog'' | ''Source'''
  default: '''Dialog'''
- name: Drag coefficient
  summary: Spacecraft coefficient of drag 2.179 (default) | scalar | vector of size *numSat*
  group: Drag
  block_parameter: dragCoeff
  type: character vector
  values: scalar | vector of size *numSat*
  default: '''2.179'''
- name: Drag area source
  summary: Source of drag area Dialog (default) | Port
  group: Drag
  block_parameter: dragAreaSrc
  type: character vector
  values: '''Dialog'' | ''Source'''
  default: '''Dialog'''
- name: Drag area
  summary: Area to compute acceleration due to atmospheric drag 1.0 (default) | scalar | vector of size *numSat*
  group: Drag
  block_parameter: dragArea
  type: character vector
  values: scalar | vector of size *numSat*
  default: '''1.0'''
- name: Ephemeris model
  summary: Ephemeris model DE405 (default) | DE421 | DE423 | DE430 | DE432t
  group: Third Body
  block_parameter: ephemerisModel
  type: character vector
  values: DE405 | DE421 | DE423 | DE430
  default: '''DE405'''
- name: Limit ephemerides date range
  summary: Option to enable start and end of range of ephemeris data off (default) | on
  group: Third Body
  block_parameter: useDateRange
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Start date (JD)
  summary: Start date of ephemerides date range juliandate(2020, 1, 1) (default) | Julian date
  group: Third Body
  block_parameter: startDate
  type: character vector
  values: '''juliandate(2020, 1, 1)'' | Julian date'
  default: '''juliandate(2020, 1, 1)'''
- name: End date (JD)
  summary: End date of ephemerides date range juliandate(2050, 1, 1) (default) | Julian date
  group: Third Body
  block_parameter: endDate
  type: character vector
  values: '''juliandate(2050, 1, 1)'' | Julian format date'
  default: '''juliandate(2050, 1, 1)'''
- name: Include third body gravity
  summary: Acceleration due to third body gravity off (default) | on
  group: Third Body
  block_parameter: useThirdBodyGravity
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Sun
  summary: Include gravitational acceleration due to Sun on (default) | off
  group: Third Body
  block_parameter: includeSunGravity
  type: character vector
  values: '''off'' | ''on'''
  default: '''on'''
- name: Sun gravity model
  summary: Third body gravity model for Sun Point-mass (default) | Oblate ellipsoid (J2)
  group: Third Body
  block_parameter: sunThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'''
  default: '''Point-mass'''
- name: Mercury
  summary: Include gravitational acceleration due to Mercury off (default) | on
  group: Third Body
  block_parameter: includeMercuryGravity
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Mercury gravity model
  summary: Mercury gravity model Point-mass (default) | Oblate ellipsoid (J2)
  group: Third Body
  block_parameter: mercuryThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'''
  default: '''Point-mass'''
- name: Venus
  summary: Include gravitational acceleration due to Venus off (default) | on
  group: Third Body
  block_parameter: includeVenusGravity
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Venus gravity model
  summary: Venus gravity model Point-mass (default) | Oblate ellipsoid (J2)
  group: Third Body
  block_parameter: venusThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'''
  default: '''Point-mass'''
- name: Earth
  summary: Include gravitational acceleration due to Earth on (default) | off
  group: Third Body
  block_parameter: includeEarthGravity
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Earth gravity model
  summary: Earth gravity model Point-mass (default) | Oblate ellipsoid (J2) | Spherical harmonics
  group: Third Body
  block_parameter: earthThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'' | ''Spherical harmonics'''
  default: '''Point-mass'''
- name: Moon
  summary: Include gravitational acceleration due to Moon on (default) | off
  group: Third Body
  block_parameter: includeMoonGravity
  type: character vector
  values: '''off'' | ''on'' |'
  default: '''on'''
- name: Moon gravity model
  summary: Moon gravity model Point-mass (default) | Oblate ellipsoid (J2) | Spherical harmonics
  group: Third Body
  block_parameter: moonThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'' | ''Spherical harmonics'''
  default: '''Point-mass'''
- name: Mars
  summary: Include gravitational acceleration due to Mars off (default) | on
  group: Third Body
  block_parameter: includeMarsGravity
  type: character vector
  values: '''off'' | ''on'' |'
  default: '''off'''
- name: Mars gravity model
  summary: Mars gravity model Point-mass (default) | Oblate ellipsoid (J2) | Spherical harmonics
  group: Third Body
  block_parameter: marsThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'' | ''Spherical harmonics'''
  default: '''Point-mass'''
- name: Jupiter
  summary: Include gravitational acceleration due to Jupiter off (default) | on
  group: Third Body
  block_parameter: includeJupiterGravity
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Jupiter gravity model
  summary: Jupiter gravity model Point-mass (default) | Oblate ellipsoid (J2)
  group: Third Body
  block_parameter: jupiterThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'''
  default: '''Point-mass'''
- name: Saturn
  summary: Include gravitational acceleration due to Saturn off (default) | on
  group: Third Body
  block_parameter: includeSaturnGravity
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Saturn gravity model
  summary: Saturn gravity model Point-mass (default) | Oblate ellipsoid (J2)
  group: Third Body
  block_parameter: saturnThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'''
  default: '''Point-mass'''
- name: Uranus
  summary: Include gravitational acceleration due to Uranus off (default) | on
  group: Third Body
  block_parameter: includeUranusGravity
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Uranus gravity model
  summary: Uranus gravity model Point-mass (default) | Oblate ellipsoid (J2)
  group: Third Body
  block_parameter: uranusThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'''
  default: '''Point-mass'''
- name: Neptune
  summary: Include gravitational acceleration due to Neptune off (default) | on
  group: Third Body
  block_parameter: includeNeptuneGravity
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Neptune gravity model
  summary: Neptune gravity model Point-mass (default) | Oblate ellipsoid (J2)
  group: Third Body
  block_parameter: neptuneThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'''
  default: '''Point-mass'''
- name: Pluto
  summary: Include gravitational acceleration due to Pluto off (default) | on
  group: Third Body
  block_parameter: includePlutoGravity
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Pluto gravity model
  summary: Pluto gravity model Point-mass (default) | Oblate ellipsoid (J2)
  group: Third Body
  block_parameter: plutoThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'''
  default: '''Point-mass'''
- name: Custom
  summary: Include gravitational acceleration due to custom planet off (default) | on
  group: Third Body
  block_parameter: includeCustomGravity
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Custom gravity model
  summary: Custom gravity model Point-mass (default) | Oblate ellipsoid (J2) | Spherical harmonics
  group: Third Body
  block_parameter: customThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'''
  default: '''Point-mass'''
- name: Gravitational parameter (m^3/s^2)
  summary: Custom gravitational acceleration 42.828314258067e12 (default) | scalar | vector of length *numCustom3rdBodies*
  group: Third Body
  block_parameter: customThirdBodyMu
  type: character vector
  values: '''42.828314258067e12'' | scalar | vector of length *numCustom3rdBodies*'
  default: '''42.828314258067e12'''
- name: Include solar radiation pressure (SRP)
  summary: Acceleration due to solar radiation pressure off (default) | on
  group: SRP
  block_parameter: useSRP
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Eclipse fraction source
  summary: Source of eclipse fraction Dialog (default) | Port
  group: SRP
  block_parameter: useSRP
  type: character vector
  values: '''Dialog'' | ''Port'''
  default: '''Dialog'''
- name: Shadow model
  summary: Shadow model Dual cone (default) | Cylindrical
  group: SRP
  block_parameter: shadowModel
  type: character vector
  values: '''Dual cone'' | ''Cylindrical'''
  default: '''Dual cone'''
- name: Include Earth
  summary: Option to include Earth on (default) | off
  group: SRP
  block_parameter: includeEarth
  type: character vector
  values: '''off'' | ''on'''
  default: '''on'''
- name: Include Moon
  summary: Option to include Moon on (default) | off
  group: SRP
  block_parameter: includeMoon
  type: character vector
  values: '''off'' | ''on'''
  default: '''on'''
- name: Reflectivity coefficient source
  summary: Source for spacecraft coefficient of reflectivity 'Dialog' (default) | 'Port'
  group: SRP
  block_parameter: reflectivityCoeffSrc
  type: character vector
  values: '''Dialog'' | ''Port'''
  default: '''on'''
- name: Reflectivity coefficient
  summary: Spacecraft coefficient of reflectivity 1.8 (default) | scalar | 2D array of size *numSat* | between [1,2]
  group: SRP
  block_parameter: reflectivityCoeff
  type: character vector
  values: '''1.8'' | scalar | 2D array of size *numSat* | between [1,2]'
  default: '''1.8'''
- name: SRP area source
  summary: Source for spacecraft solar radiation pressure area Dialog (default) | Port
  group: SRP
  block_parameter: srpAreaSrc
  type: character vector
  values: '''Dialog'' | ''Port'''
  default: '''Dialog'''
- name: SRP area
  summary: Cross section area of the spacecraft seen by the Sun 1.0 (default) | scalar | 2D array of size *numSat*
  group: SRP
  block_parameter: srpArea
  type: character vector
  values: '''1.0'' | scalar | 2D array of size *numSat*'
  default: '''1.0'''
- name: Solar flux pressure (W\*s/m^3)
  summary: Spacecraft solar flux pressure 4.5344321e-6 (default) | scalar
  group: SRP
  block_parameter: fluxPressure
  type: character vector
  values: 4.5344321e-6 | scalar
  default: '''4.5344321e-6'''
- name: Units
  summary: Parameter and port units Metric (m/s) (default) | Metric (km/s) | Metric (km/h) | English (ft/s) | English (kts)
  group: Units
  block_parameter: units
  type: character vector
  values: '''Metric (m/s)'' | ''Metric (km/s)'' | ''Metric (km/h)'' | ''English (ft/s)'' | ''English (kts)'''
  default: '''Metric (m/s)'''
- name: Angle units
  summary: Angle units Degrees (default) | Radians
  group: Units
  block_parameter: angleUnits
  type: character vector
  values: '''Degrees'' | ''Radians'''
  default: '''Degrees'''
- name: Time format
  summary: Time format for start date and time output Julian date (default) | Gregorian
  group: Units
  block_parameter: timeFormat
  type: character vector
  values: '''Julian date'' | ''Gregorian'''
  default: '''Julian date'''
```

### Main

### **Input body forces** — Option to enable external forces on (default) | off

To enable external forces to be included in the integration of the spacecraft
equations of motion in the body frame, select this parameter. Otherwise, clear this
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `forcesin` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Input body moments** — Option to enable external moments on (default) | off

To enable external moments to be included in the integration of the spacecraft
equations of motion in the body frame, select this parameter. Otherwise, clear this
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `momentsIn` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Input external accelerations** — Option to input additional force accelerations off (default) | on

To enable additional external accelerations to be included in the integration of
the spacecraft equations of motion, select this parameter. Otherwise, clear this
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `accelIn` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **External acceleration coordinate frame** — Frame for acceleration input port `ICRF` (default) | `Fixed-frame`

Frame for acceleration input port **A**, specified as
`ICRF` or `Fixed-frame`.

#### Dependencies

To enable this parameter, set the **Input external
accelerations** parameter to `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `accelFrame` |
| **Type:** character vector |
| **Values:** `'ICRF'` | `'Fixed-frame'` |
| **Default:** `'ICRF'` |

### **State vector output coordinate frame** — Position and velocity state output port coordinate frame `ICRF` (default) | `Fixed-frame`

Position and velocity state output port coordinate frame setup, specified as
`ICRF` or `Fixed-frame`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `outportFrame` |
| **Type:** character vector |
| **Values:** `'ICRF'` | `'Fixed-frame'` |
| **Default:** `'ICRF'` |

### **Output total inertial acceleration** — Option to enable total acceleration port off (default) | on

Enable the total acceleration output computed by the block with respect to the
ICRF or fixed-frame outport coordinate frame. This acceleration includes all external
accelerations, forces, and internal environmental accelerations that act on the
spacecraft.

**Note**

Do not use this port as part of a simulation loop (in other words, do not feed
this output back into the block).

**Tunable:** Yes

#### Dependencies

To change the output coordinate frame for this port, set the ****State vector output coordinate frame****
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AccelOut` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **Start date/time (UTC Julian date)** — Initial start time for simulation `juliandate (2020, 1, 1, 12, 0, 0)` (default) | valid scalar Julian date | valid Gregorian date including year, month, day, hours, minutes, seconds as 1D or 6-element array for Gregorian dates

Initial start date and time of simulation, specified as a Julian or Gregorian
date. The block defines initial conditions using this value.

**Tip**

To calculate the Julian date, use the `juliandate` function.

**Tunable:** Yes

#### Dependencies

The data format for this parameter is controlled by the **Time
format** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `startDate` |
| **Type:** character vector |
| **Values:** `'juliandate(2020, 1, 1, 12, 0, 0)'` | valid scalar Julian date | valid Gregorian date including year, month, day, hours, minutes, seconds as 1D or 6-element array |
| **Default:**  `'juliandate(2020, 1, 1, 12, 0, 0)'` |

### **Output current date/time (UTC Julian date)** — Option to add output port tutc on (default) | off

To output the current date or time, select this parameter. Otherwise, clear this
parameter.

#### Dependencies

The data format for this parameter is controlled by the **Time
format** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `dateOut` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Action for out-of-range input** — Out-of-range block behavior `Warning` (default) | `Error` | `None`

Out-of-range block behavior action. Specify one of these options.

| Action | Description |
| --- | --- |
| `None` | No action. |
| `Warning` | Warning in the Diagnostic Viewer, model simulation continues. |
| `Error` (default) | Error in the Diagnostic Viewer, model simulation stops. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `action` |
| **Type**: character vector |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'Warning'` |

### Mass

### **Mass type** — Spacecraft mass type `Fixed` (default) | `Simple Variable` | `Custom Variable`

Spacecraft mass type, specified as:

- `Fixed` — Mass and inertia are constant throughout
  the simulation.
- `Simple Variable` — Mass and inertia vary linearly as
  a function of mass rate.
- `Custom Variable` — Instantaneous mass, inertia, and
  inertia rate are inputs to the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `massType` |
| **Type**: character vector |
| **Values**: `'Fixed'` | `'Simple Variable'` | `'Custom Variable'` |
| **Default**: `'Fixed'` |

### **Mass** — Initial mass of rigid body spacecraft 4.0 (default) | scalar | vector of size *numSat*

Initial mass of rigid body spacecraft, specified as scalar or vector of size
*numSat*. *numSat* is the number of
spacecraft.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Mass type** parameter to
either **Fixed** or **Simple variable**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `mass` |
| **Type:** character vector |
| **Values:** scalar | vector of size *numSat* |
| **Default:** `'4.0'` |

### **Empty mass** — Spacecraft empty mass `3.5` (default) | scalar | vector of size *numSat*

Spacecraft empty (dry) mass, specified as a scalar or vector of size
*numSat*. *numSat* is the number of
spacecraft.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Mass type** to
`Simple variable`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `emptyMass` |
| **Type:** character vector |
| **Values:** 1D array of size *numSat* | 1D array of size *numSat* |
| **Default:** `'3.5'` |

### **Full mass** — Spacecraft full mass 4.0 (default) | scalar | vector of size *numSat*

Spacecraft full (wet) mass, specified as a scalar or vector of size
*numSat*. *numSat* is the number of
spacecraft.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Mass type** to
`Simple variable`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `fullMass` |
| **Type:** character vector |
| **Values:** scalar | vector of size *numSat* |
| **Default:** `'4.0'` |

### **Inertia tensor** — Inertia tensor matrix `[0.2273, 0, 0; 0 0.2273 0; 0 0 .0040]` (default) | 3-by-3 array | 3-by-3-by-*numSat* array

Initial inertia tensor matrix of the spacecraft, specified, as a 3-by-3 array for
a single spacecraft or a 3-by-3-by-*numSat* array for multiple
spacecraft.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Mass type** to
`Fixed`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `inertia` |
| **Type:** character vector |
| **Values:** `'[0.2273, 0, 0; 0 0.2273 0; 0 0 .0040]'` | 3-by-3 array | 3-by-3-by-*numSat* array |
| **Default:** `'[0.2273, 0, 0; 0 0.2273 0; 0 0 .0040]'` |

### **Empty inertia tensor** — Empty inertia tensor matrix `[0.1989, 0, 0; 0 0.1989 0; 0 0 .0035]` (default) | 3-by-3 array | 3-by-3-by-*numSat* array

Empty (dry) inertia tensor matrix, specified as a 3-by-3 array for a single
spacecraft or a 3-by-3-by-*numSat* array for multiple
spacecraft.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Mass type** to
`Simple variable`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `emptyInertia` |
| **Type:** character vector |
| **Values:** 3-by-3 array | 3-by-3-by-*numSat* array |
| **Default:** `[0.1989, 0, 0; 0 0.1989 0; 0 0 .0035]` |

### **Full inertia tensor** — Full inertia tensor matrix `[0.2273, 0, 0; 0, 0.2273, 0; 0, 0, .0040]` (default) | 3-by-3 array | 3-by-3-by-*numSat* array

Full (wet) inertia tensor matrix, specified as a 3-by-3 array for a single
spacecraft or a 3-by-3-by-*numSat* array for multiple
spacecraft.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Mass type** to
`Simple variable`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `fullInertia` |
| **Type:** character vector |
| **Values:** 3-by-3 array | 3-by-3-by-*numSat* array |
| **Default:** `[0.2273, 0, 0; 0, 0.2273, 0; 0, 0, .0040]` |

### **Include mass flow relative velocity** — Option to enable mass flow velocity off (default) | on

To enable mass flow velocity to the block, select this parameter. The mass flow
velocity is the relative velocity in the body frame at which the mass is accreted or
ablated. To disable mass flow velocity to the block, clear this parameter.

#### Dependencies

To enable this parameter, set **Mass type** to
`Simple variable` or `Custom
variable`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `useMassFlowRelativeVelocity` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **Limit mass flow when mass is empty or full** — Option to limit mass flow on (default) | off

To limit the mass flow when the spacecraft mass is full or empty, select this
parameter. Otherwise, clear this parameter.

#### Dependencies

To enable this parameter, set **Mass type** to
`Simple variable`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `limitMassFlow` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Output fuel tank status** — Option to enable fuel tank status on (default) | off

To enable fuel tank status, select this parameter. Otherwise, clear this
parameter.

#### Dependencies

To enable this parameter, set **Mass type** to
`Simple variable`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `outputFuelStatus` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### Orbit

Define the initial states of the spacecraft.

### **Initial state format** — Input method for initial states of orbit `Orbital elements` (default) | `ICRF state vector` | `Fixed-frame state vector`

Input method for initial states of orbit, specified as `Orbital
elements`, `ICRF state vector`, or
`Fixed-frame state vector`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter** `stateFormatNum` when `propagator` is set to `High precision (numerical)` |
| **Type:** character vector |
| **Values:**  `'Orbital elements'` | `'Orbital elements'` | `'ICRF state vector'` | `'Fixed-frame state'` when `propagator` is set to `'High precision (numerical)'` |
| **Default:** `'Orbital elements'` |

### **Orbit type** — Orbit classification `Keplerian` (default) | `Elliptical equatorial` | `Circular` | `Circular equatorial`

Orbit classification, specified as:

- `Keplerian` — Model elliptical, parabolic, and
  hyperbolic orbits using six standard Keplerian orbital elements.
- `Elliptical equatorial` — Fully define an equatorial
  orbit, where inclination is 0 or 180 degrees and the right ascension of the
  ascending node is undefined.
- `Circular` — Define a circular orbit, where
  eccentricity is 0 and the argument of periapsis is undefined. To fully define a
  circular orbit, select `Circular equatorial`.
- `Circular equatorial` — Fully define a circular
  orbit, where eccentricity is 0 and the argument of periapsis is undefined.

#### Dependencies

To enable this parameter, set **Initial state format** to
`Orbital elements`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `orbitType` |
| **Type:** character vector |
| **Values:** `'Keplerian'` | `'Elliptical equatorial'` | `'Circular inclined'` | `'Circular equatorial'` |
| **Default:** `'Keplerian'` |

### **Semi-major axis** — Half of major axis of ellipse 6786000 (default) | scalar | 1D array of size *numSat*

Half of ellipse major axis, specified as a 1D array of size
*numSat*. *numSat* is the number of spacecraft.

- For parabolic orbits, this block interprets this parameter as the periapsis
  radius (distance from periapsis to the focus point of orbit).
- For hyperbolic orbits, this block interprets this parameter as the distance
  from periapsis to the hyperbola center.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Initial state format** to
`Orbital elements`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `semiMajorAxis` |
| **Type:** character vector |
| **Values:** scalar | 1D array of size *numSat* |
| **Default:** `'6786000'` |

### **Eccentricity** — Deviation of orbit 0.01 (default) | scalar | value between `0` and `1`, or greater than `1` for Keplerian orbit type | 1D array of size *numSat*

Deviation of the orbit from a perfect circle, specified as a scalar or 1D array of
size *numSat*. *numSat* is the number of
spacecraft.

If **Orbit** type is set to `Keplerian`,
this value can be:

- `1` for parabolic orbit
- Greater than `1` for hyperbolic orbit

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Initial state format** to `Orbital
  elements`.
- Set **Orbit type** to `Keplerian`
  or `Elliptical equatorial`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `eccentricity` |
| **Type:** character vector |
| **Values:** `0.01` | scalar | value between `0` and `1`, or greater than `1` for Keplerian orbit type | 1D array of size *numSat* |
| **Default:** `'0.01'` |

### **Inclination** — Tilt angle of orbital plane 50 (default) | scalar | 1D array of size *numSat* | degrees between 0 and 180 | radians between 0 and pi

Vertical tilt of the ellipse with respect to the reference plane measured at the
ascending node, specified as a scalar or 1D array of size *numSat*,
in specified units. *numSat* is the number of spacecraft.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Initial state format** to `Orbital
  elements`
- Set **Orbit type** to `Keplerian`
  or `Circular inclined`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `inclination` |
| **Type:** character vector |
| **Values:** 50 | scalar | 1D array of size *numSat* | degrees between 0 and 180 | radians between 0 and pi |
| **Default:** `'50'` |

### **RAAN** — Angular distance in equatorial plane 95 (default) | scalar value between `0` and `360` | 1D array of size *numSat*

Right ascension of ascending node (RAAN), specified as a value between
`0` and `360`, specified as a scalar or 1D array
of size *numSat*, in specified units. *numSat* is
the number of spacecraft. RAAN is the angular distance along the reference plane from
the International Celestial Reference Frame (ICRF) *x*-axis to the
location of the ascending node — the point at which the spacecraft crosses the
reference plane from south to north.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Initial state format** to `Orbital
  elements`.
- Set **Orbit type** to `Keplerian`
  or `Circular inclined`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `raan` |
| **Type:** character vector |
| **Values:** `'95'` | scalar value between `0` and `360` | 1D array of size *numSat* |
| **Default:** `'95'` |

### **Argument of periapsis** — Angle from spacecraft ascending node to periapsis 93 (default) | value between `0` and `360` | 1D array of size *numSat*

Angle from the spacecraft ascending node to periapsis (closest point of orbit to
the central body), specified as a 1D array of size *numSat*, in
specified units. *numSat* is the number of spacecraft.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Initial state format** to `Orbital
  elements`
- Set **Orbit type** to
  `Keplerian`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `argPeriapsis` |
| **Type:** character vector |
| **Values:** 93 | scalar value between `0` and `360` | 1D array of size *numSat* |
| **Default:** `'93'` |

### **True anomaly** — Angle between periapsis and initial position of spacecraft 203 (default) | scalar value between `0` and `360` | 1D array of size *numSat*

Angle between periapsis (closest point of orbit to the central body) and the
initial position of spacecraft along its orbit at **Start
date/time**, specified as a scalar or 1D array of size
*numSat*, in specified units. *numSat* is the
number of spacecraft.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Initial state format** to `Orbital
  elements`.
- Set **Orbit type** to `Keplerian`
  or `Elliptical inclined`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `trueAnomaly` |
| **Type:** character vector |
| **Values:** `'203'` | scalar value between `0` and `360` | 1D array of size *numSat* |
| **Default:** `'203'` |

### **Argument of latitude** — Angle between ascending node and initial position of spacecraft 200 (default) | scalar | value between `0` and `360` | 1D array of size *numSat*

Angle between the ascending node and the initial position of spacecraft along its
orbit at **Start date/time**, specified as a scalar or 3-element
vector or 1D array of size *numSat*, in specified units.
*numSat* is number of spacecraft.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Initial state format** to `Orbital
  elements`.
- Set **Orbit Type** to `Circular
  inclined`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `argLat` |
| **Type:** character vector |
| **Values:** `'200'` | scalar value between `0` and `360` | 1D array of size *numSat* |
| **Default:** `'200'` |

### **Longitude of periapsis** — Angle between ICRF *x*-axis and eccentricity vector 100 (default) | scalar | value between `0` and `360` | 1D array of size *numSat*

Angle between the ICRF *x*-axis and the eccentricity vector,
specified as a scalar or 3-element vector or 1D array of size
*numSat*, in specified units. *numSat* is the
number of spacecraft.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Initial state format** to `Orbital
  elements`.
- Set **Orbit type** to `Elliptical
  equatorial`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `lonPeriapsis` |
| **Type:** character vector |
| **Values:** 100 | scalar value between `0` and `360` | 1D array of size *numSat* |
| **Default:** `'100'` |

### **True longitude** — Angle between ICRF *x*-axis and initial position of spacecraft 150 (default) | scalar | value between `0` and `360` | 1D array of size *numSat* | *numSat*-by-3 vector

Angle between the ICRF *x*-axis and the initial position of
spacecraft along its orbit at **Start date/time**, specified as a
scalar or 1D array of size *numSat* or a
*numSat*-by-3 vector, in specified units. *numSat*
is the number of spacecraft.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Initial state format** to `Orbital
  elements`.
- Set **Orbit type** to `Circular
  equatorial`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `trueLon` |
| **Type:** character vector |
| **Values:** `'150'` | scalar value between `0` and `360` | 1D array of size *numSat* | *numSat*-by-3 vector |
| **Default:** `'150'` |

### **ICRF position** — Cartesian position vector of spacecraft `[3649700.0 3308200.0 -4676600.0]` (default) | 3-element vector | | *numSat*-by-3 array

Cartesian position vector of spacecraft in ICRF coordinate system at
**Start date/time**, specified as a 3-element vector for single
spacecraft or a *numSat*-by-3 array for multiple spacecraft.
*numSat* is the number of spacecraft.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Initial state format** to
`ICRF state vector`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `inertialPosition` |
| **Type:** character vector |
| **Values:** `[3649700.0 3308200.0 -4676600.0]` | 3-element vector | *numSat*-by-3 array |
| **Default:** `'[3649700.0 3308200.0 -4676600.0]'` |

### **ICRF velocity** — Cartesian velocity vector of spacecraft `[-2750.8 6666.4 2573.4]` (default) | 3-element vector | *numSat*-by-3 array

Cartesian velocity vector of spacecraft in ICRF coordinate system at
**Start date/time**, specified as a 3-element vector for single
spacecraft or a *numSat*-by-3 array for multiple spacecraft.
*numSat* is the number of spacecraft.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Initial state format** to
`ICRF state vector`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `inertialVelocity` |
| **Type:** character vector |
| **Values:** `[-2750.8 6666.4 2573.4]` | 3-element vector | 2-D array of size *numSat*-by-3 array |
| **Default:** `'[-2750.8 6666.4 2573.4]'` |

### **Fixed-frame position** — Position vector of spacecraft [-4142689.0 -2676864.7 -4669861.6] (default) | 3-element vector | *numSat*-by-3 array

Cartesian position vector of spacecraft in fixed-frame coordinate system at
**Start date/time**, specified as a 3-element vector for single
spacecraft or a *numSat*-by-3 array for multiple spacecraft.
*numSat* is the number of spacecraft.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Initial state format** to
`Fixed-frame state vector`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `fixedPosition` |
| **Type:** character vector |
| **Values:** `'[-4142689.0 -2676864.7 -4669861.6]'` | 3-element vector for single spacecraft | *numSat*-by-3 array |
| **Default:** `'[-2750.8 6666.4 2573.4]'` |

### **Fixed-frame velocity** — Velocity vector of spacecraft [1452.7 -6720.7 2568.1] (default) | 3-element vector | *numSat*-by-3 array

Cartesian velocity vector of spacecraft in fixed-frame coordinate system at
**Start date/time**, specified as a 3-element vector for single
spacecraft or a *numSat*-by-3 array for multiple spacecraft.
*numSat* is the number of spacecraft.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Initial state format** to
`Fixed-frame state vector`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `fixedVelocity` |
| **Type:** character vector |
| **Values:** `'[1452.7 -6720.7 2568.1]'` | 3-element vector | *numSat*-by-3 array |
| **Default:** `'[1452.7 -6720.7 2568.1]'` |

### Attitude

### **Attitude reference coordinate frame** — Attitude and angular rate coordinate frame `ICRF` (default) | `Fixed-frame` | `NED` | `LVLH`

Attitude and angular rate coordinate frame with respect to the attitude and
angular rate initial conditions, specified as:

- `ICRF`
- `Fixed-frame`
- `NED`
- `LVLH`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `attitudeFrame` |
| **Type:** character vector |
| **Values:** `'ICRF'` | `'Fixed-frame'` | `'NED'` | `'LVLH'` |
| **Default:** `'ICRF'` |

### **Attitude representation** — Orientation format `Quaternion` (default) | `DCM` | `Euler angles`

Orientation format for spacecraft attitude (initial condition and output port),
specified as `Quaternion`, `DCM`, or
`Euler angles`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `attitudeFrame` |
| **Type:** character vector |
| **Values:** `'Quaternion'` | `'DCM'` | `'Euler angles'` |
| **Default:** `'Quaternion'` |

### **Initial body attitude** — Spacecraft initial attitude `[1, 0, 0, 0]` (default) | 4-element vector | *numSat*-by-4 array | 3-by-3 array | *numSat*-by-3-by-3 array

Spacecraft initial attitude (orientation) of the spacecraft provided as either a
quaternion, DCM, or Euler angle set with respect to **Attitude
representation**.

**Tunable:** Yes

#### Dependencies

This parameter name and value format changes depending on the **Attitude
representation** parameter.

| Parameter Name | Attitude Representation Setting | Value Format |
| --- | --- | --- |
| **Initial quaternion** | `Quaternion` | - 4-element vector - *numSat*-by-4 array |
| **Initial DCM** | `DCM` | - 3-by-3 array - *numSat*-by-3-by-3 array |
| **Initial Euler angles** | `Euler angles` | - 3-element vector - *numSat*-by-3 array |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `attitude` |
| **Type:** character vector |
| **Values:** 4-element vector | *numSat*-by-4 array | 3-by-3 array | *numSat*-by-3-by-3 array | 3-element array | *numSat*-by-3 array |
| **Default:** `'[1, 0, 0, 0]'` |

### **Angle rotation order** — Angle rotation order `ZYX` (default) | `ZYX` | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

Rotation angle sequence for Euler angle attitude representation.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Attitude representation** to
`Euler angles`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `rotationOrder` |
| **Type**: character vector |
| **Values**: `'ZYX'` | `'ZYZ'` |`'ZXY'` | `'ZXZ'` | `'YXZ'` | `'YXY'` | `'YZX'` | `'YZY'` | `'XYZ'` | `'XYX'` | `'XZY'` | `'XZX'` |
| **Default**: `'ZYX'` |

### **Initial body angular rates PQR** — Initial body-fixed angular rates `[0, 0, 0]` (default) | 3-element vector | *numSat*-by-3 array

Initial body-fixed angular rates (PQR) with respect to **Attitude
reference coordinate frame**.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `attitudeRate` |
| **Type:** character vector |
| **Values:** | 3-element vector | *numSat*-by-3 array |
| **Default:** `[0, 0, 0]` |

### **Output total inertial angular acceleration** — Option to enable total vehicle acceleration off (default) | on

Enable output total vehicle acceleration computed by the block with respect to the
ICRF attitude reference coordinate frame. This acceleration includes all moments that
act on the spacecraft.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `angAccelOut` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **Include gravity gradient torque** — Option to enable gravity gradient torque on (default) | off

Select this parameter to enable the use of the gravity gradient torque in the
block rotational dynamics equations. Otherwise, clear this parameter.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `angAccelOut` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### Central Body

### **Central body** — Celestial body around which spacecraft orbits `Earth` (default) | `Moon` | `Mercury` | `Venus` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Sun` | `Custom`

Celestial body, specified as `Earth`,
`Moon`, `Mercury`,
`Venus`, `Mars`,
`Jupiter`, `Saturn`,
`Uranus`, `Neptune`,
`Sun`, or `Custom`, around which
the spacecraft defined in the **Orbit** tab orbits.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `centralBody` |
| **Type:** character vector |
| **Values:** `'Earth'` | `'Moon'` |`'Mercury'` | `'Venus'` | `'Mars'` | `'Jupiter'` | `'Saturn'` | `'Uranus'` | `'Neptune'` | `'Sun'` | `'Custom'` | |
| **Default:** `'Earth'` |

### **Gravitational potential model** — Gravity model for central body `Spherical harmonics` when **Central body** set to `Earth`, `Moon`, `Mars`, or `Custom`, `Oblate ellipsoid` when **Central body** set to `Mercury`, `Venus`, `Jupiter`, `Saturn`, `Uranus`, or `Neptune` (default) | `Point-mass` | `Oblate ellipsoid (J2)`

Control the gravity model for the central body by specifying as
`Spherical harmonics`,
`Point-mass`, or `Oblate ellipsoid
(J2)`.

#### Dependencies

Available options are based on **Central body**
settings.

| Earth, Moon, Mars, or Custom | Mercury, Venus, Jupiter, Saturn, Uranus, or Neptune |
| --- | --- |
| `Spherical harmonics` | `Oblate ellipsoid (J2)` |
| `Point-mass` | `Point-mass` |
| `Oblate ellipsoid (J2)` | — |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `gravityModel` when `centralBody` set to `'Earth'`, `'Moon'`, `'Mars'`, or `'Custom'` | `gravityModelnoSH` when `centralBody` set to `Mercury`, `Venus`, `Jupiter`, `Saturn`, `Uranus`, or `Neptune` |
| **Type:** character vector |
| **Values:** `'Spherical harmonics'` | `'Point-mass'` | `'Oblate ellipsoid (J2)'` when `centralBody` set to `'Earth'`, `'Moon'`, `'Mars'`, or `'Custom'`; `'Point-mass'` | `'Oblate ellipsoid (J2)'` when `centralBody` set to `Mercury`, `Venus`, `Jupiter`, `Saturn`, `Uranus`, or `Neptune` |
| **Default:** `'Spherical harmonics'` when `centralBody` set to `'Earth'`, `'Moon'`, `'Mars'`, or `'Custom'`; `'Oblate ellipsoid (J2)'` when `centralBody` set to `Mercury`, `Venus`, `Jupiter`, `Saturn`, `Uranus`, or `Neptune` |

### **Spherical harmonic model** — Spherical harmonic model `EGM2008` for **Central body** set to `Earth`, `LP-100K` for **Central body** set to `Moon`, `GMM2B` for **Central body** set to `Mars`, (default) | `EGM96` | `EIGEN-GL04C` | `LP-165P`

Spherical harmonic gravitational potential model, specified according to the
specified **Central body**.

#### Dependencies

Available options are based on **Central body**
settings:

| Central body | Spherical Harmonic Model Option |
| --- | --- |
| Earth | EGM2008, EGM96, or EIGEN-GL04C |
| Moon | LP-100K or LP-165P |
| Mars | GMM2B |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'earthSH'` when `centralBody` set to `'Earth'` | `'moonSH'` when `centralBody` set to `'Moon'` | `'marsSH'` when `centralBody` set to `'Mars'` |
| **Type:** character vector |
| **Values:** `'EGM2008'` | `'EGM96'` | `'EIGEN-GL04C'` when `centralBody` set to `'earthSH'`; `'LP-100K'` | `'LP-165P'` when `centralBody` set to `'moonSH'`; `'GMM2B'` when `centralBody` set to `'marsSH'` |
| **Default:** `'Spherical harmonics'` |

### **Rotational rate** — Rotational rate 4.06124975e-3 (default) | scalar

Rotational rate of a custom central body, specified as a scalar.

#### Dependencies

To enable this parameter, set **Central body** to
`Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'customOmega'` |
| **Type:** character vector |
| **Values:** `'4.06124975e-3'` | scalar |
| **Default:** `'4.06124975e-3'` |

### **Spherical harmonic coefficient file** — Harmonic coefficient MAT file `aerogmm2b.mat` (default) | harmonic coefficient MAT file

Harmonic coefficient MAT file that contains definitions for a custom planetary
model, specified as a character vector or string.

This file must contain these variables:

| Variable | Description |
| --- | --- |
| *Re* | Scalar of planet equatorial radius in meters (m). |
| *GM* | Scalar of planetary gravitational parameter in meters cubed per second squared (m3/s2). |
| *degree* | Scalar of maximum degree. |
| *C* | (*degree*+1)-by-(*degree*+1) matrix containing normalized spherical harmonic coefficients matrix, *C*. |
| *S* | (*degree*+1)-by-(*degree*+1) matrix containing normalized spherical harmonic coefficients matrix, *S*. |

#### Dependencies

To enable this parameter:

- Set **Central body** to
  `Custom`.
- Set **Gravitational potential model** to`Spherical harmonics`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `shFile` |
| **Type:** character vector |
| **Values:** `'aerogmm2b.mat'` | harmonic coefficient MAT file |
| **Default:** `'aerogmm2b.mat'` |

### **Degree** — Degree of harmonic model `120` (default) | scalar | maximum of 2159

Degree of harmonic model, specified as a scalar.

| Planet Model | Recommended Degree | Maximum Degree |
| --- | --- | --- |
| `EGM2008` | 120 | 2159 |
| `EGM96` | 70 | 360 |
| `LP100K` | 60 | 100 |
| `LP165P` | 60 | 165 |
| `GMM2B` | 60 | 80 |
| `EIGENGL04C` | 70 | 360 |

#### Dependencies

To enable this parameter:

- Set **Central body** to `Earth`,
  `Moon`, `Mars`, or
  `Custom`.
- Set **Gravitational potential model** to
  `Spherical harmonics`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `shDegree` |
| **Type:** character vector |
| **Values:** `'80'` | scalar |
| **Default:** `'80'` |

### **Use Earth orientation parameters (EOPs)** — Option to use Earth orientation parameters on (default) | off

Select this parameter to use Earth orientation parameters for the transformation
between the ICRF and fixed-frame coordinate systems. Otherwise, clear this
parameter.

#### Dependencies

To enable this parameter, set **Central body** to
`Earth`.

Additionally, it must satisfy one of these criteria:

- **Gravitational potential model** is set to either
   `Spherical harmonics` or `Oblate
  ellipsoid (J2)`.
- **External acceleration coordinate frame** is set to
  `Fixed-frame`.
- **State vector output coordinate frame** is set to
  `Fixed-frame`.
- **Attitude reference coordinate frame** is set to
  `Fixed-frame` or
  `NED`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `useEOPs` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **IERS EOP data file** — Earth orientation data `aeroiersdata.mat` (default) | MAT file

Custom list of Earth orientation data, specified in a MAT file.

#### Dependencies

To enable this parameter:

- Set the **Use Earth orientation parameters (EOPs)**
  parameter to `on`.
- Set **Central body** to
  `Earth`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `eopFile` |
| **Type:** character vector |
| **Values:** `'aeroiersdata.mat'` | `MAT-file` |
| **Default:** `'aeroiersdata.mat'` |

### **Input Moon libration angles** — Moon libration Euler angle rate off (default) | on

To specify Euler libration angles (φ θ ψ) for Moon orientation, select this
parameter.

#### Dependencies

To enable this parameter, set **Central body** to
`Moon`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `useMoonLib` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Output quaternion (ICRF to Fixed-frame)** — Option to add output transformation quaternion port off (default) | on

To add output transformation quaternion port for the quaternion transformation
from the ICRF to the fixed-frame coordinate system, select this parameter. Otherwise,
clear this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `outputTransform` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Central body spin axis source** — Central body spin source `Port` (default) | `Dialog`

Central body spin axis source, specified as `Port` or
`Dialog`. The block uses the spin axis to calculate the
transformation from the ICRF to the fixed-frame coordinate system for the custom
central body.

#### Dependencies

To enable this parameter, set **Central body** to
`Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `cbPoleSrc` |
| **Type:** character vector |
| **Values:** `'Port'` | `'Dialog'` |
| **Default:** `'Port'` |

### **Spin axis right ascension (RA) at J2000** — Right ascension of central body spin axis at J2000 `317.68143` (default) | double scalar

Right ascension of central body spin axis at J2000 (2451545.0 JD, 2000 Jan 1
12:00:00 TT), specified as a double scalar.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Central body** to
  `Custom`.
- Set **Central body spin axis source** to
  `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `cbRA` |
| **Type:** character vector |
| **Values:** `'317.68143'` | double scalar |
| **Default:** `'317.68143'` |

### **Spin axis RA rate (deg/century)** — Right ascension rate of central body spin axis `-0.1061` (default) | double scalar

Right ascension rate of the central body spin axis, specified as a double scalar,
in specified angle units/century.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Central body** to
  `Custom`.
- Set **Central body spin axis source** to
  `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `cbRARate` |
| **Type:** character vector |
| **Values:** `'-0.1061'` | double scalar |
| **Default:** `'-0.1061'` |

### **Spin axis declination (Dec) at J2000** — Declination of central body spin axis at J2000 `52.88650` (default) | double scalar

Declination of the central body spin axis at J2000 (2451545.0 JD, 2000 Jan 1
12:00:00 TT), specified as a double scalar.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Central body** to
  `Custom`.
- Set **Central body spin axis source** to
  `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `cbDec` |
| **Type:** character vector |
| **Values:** `'52.88650'` | double scalar |
| **Default:** `'52.88650'` |

### **Spin axis Dec rate (deg/century)** — Declination rate of central body spin axis `-0.0609` (default) | double scalar

Declination rate of the central body spin axis, specified as a double scalar, in
specified angle units/century.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Central body** to
  `Custom`.
- Set **Central body spin axis source** to
  `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `cbDecRate` |
| **Type:** character vector |
| **Values:** `'-0.0609'` | double scalar |
| **Default:** `'-0.0609'` |

### **Initial rotation angle at J2000** — Rotation angle of central body *x*-axis `176.630` (default) | double scalar

Rotation angle of the central body x axis with respect to the ICRF
*x*-axis at J2000 (2451545.0 JD, 2000 Jan 1 12:00:00 TT), specified
as a double scalar, in specified angle units.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Central body** to
  `Custom`.
- Set **Central body spin axis source** to
  `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `cbRotAngle` |
| **Type:** character vector |
| **Values:** `'176.630'` | double scalar |
| **Default:** `'176.630'` |

### **Rotation rate (deg/day)** — Rotation rate of central body *x*-axis `350.89198226` (default) | double scalar

Rotation rate of the central body x axis with respect to the ICRF
*x*-axis (2451545.0 JD, 2000 Jan 1 12:00:00 UTC), specified as a
double scalar, in angle units/day.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Central body** to
  `Custom`.
- Set **Central body spin axis source** to
  `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `cbRotRate` |
| **Type:** character vector |
| **Values:** `'350.89198226'` | double scalar |
| **Default:** `'350.89198226'` |

### **Equatorial radius** — Equatorial radius `3.3962e6` (default) | double scalar

Equatorial radius for a custom central body, specified as a double scalar.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Gravitational potential model**
to `None`, `Point-mass`, or
`Oblate ellipsoid (J2)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `customR` |
| **Type:** character vector |
| **Values:** `'3.3962e6'` | double scalar |
| **Default:** `'3.3962e6'` |

### **Flattening** — Flattening of planet `0.00589` (default) | double scalar

Flattening of planet for custom central body, specified as a double scalar.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Central body** to
  `Custom`.
- Set **Gravitational potential model** to
  `Point-mass`, `Oblate ellipsoid
  (J2)`, or `Spherical harmonics`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `customF` |
| **Type:** character vector |
| **Values:** `'0.00589'` | double scalar |
| **Default:** `'0.00589'` |

### **Gravitational parameter** — Gravitational parameter `4.305e13` (default) | double scalar

Gravitational parameter for a custom central body, specified as a double scalar.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Central body** to
  `Custom`.
- Set **Gravitational potential model** to
  `None`, `Point-mass`, or
  `Oblate ellipsoid (J2)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `customMu` |
| **Type:** character vector |
| **Values:** `'4.305e13'` | double scalar |
| **Default:** `'4.305e13'` |

### **Second degree zonal harmonic (J2)** — Most significant or largest spherical harmonic term `1.0826269e-03` (default) | double scalar

Most significant or largest spherical harmonic term, which accounts for oblateness
of a celestial body, specified as a double scalar.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Central body** to
  `Custom`.
- Set **Gravitational potential model** to
  `Oblate ellipsoid (J2)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `customJ2` |
| **Type:** character vector |
| **Values:** `'1.0826269e-03'` | double scalar |
| **Default:** `'1.0826269e-03'` |

### Drag

Configure the atmospheric drag environment.

### **Include atmospheric drag** — Option to include atmospheric drag off (default) | on

To include atmospheric drag, select this check box.

#### Dependencies

To enable this parameter, set the **Central Body** parameter to
`Earth`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `useDrag` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Atmospheric density source** — Source of atmospheric density value `Dialog` (default) | `Port`

Source of atmospheric density value, specified as
`Dialog` or `Port`.

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to
  `Earth`.
- Set the **Include atmospheric drag** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `atmosSrc` |
| **Type:** character vector |
| **Values:** `'Dialog'` | `'Port'` |
| **Default:** `'Dialog'` |

### **Atmospheric model** — Atmospheric model `NRLMSISE-00` (default)

Atmospheric model for atmospheric drag calculation, specified as
`NRLMSISE-00`.

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to
  `Earth`.
- Set the **Include atmospheric drag** parameter to
  `on`.
- Set the **Atmospheric density source** parameter to
  `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `atmosModel` |
| **Type:** character vector |
| **Values:** `'NRLMSISE-00'` |
| **Default:** `'NRLMSISE-00'` |

### **Flux source** — Source of space weather data `Dialog` (default) | `Port`

Source for historical and predicted flux and geomagnetic indices used by
atmospheric density calculation, specified as `Dialog` or
`Port`.

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to
  `Earth`.
- Set the **Include atmospheric drag** parameter to
  `on`.
- Set the **Atmospheric density source** parameter to
  `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `fluxSrc` |
| **Type:** character vector |
| **Values:** `'Dialog'` | `'Port'` |
| **Default:** `'Dialog'` |

### **Space weather data file** — MAT file of space weather data `aeroSpaceWeatherData.mat` (default) | MAT file name

MAT file of space weather data. This file is the output from the `aeroReadSpaceWeatherData` function.

Aerospace Blockset includes a default space weather data file,
`aeroSpaceWeatherData.mat`. To use the most recent data available,
use `aeroReadSpaceWeatherData` to generate a new MAT file, and
specify the file name for this parameter. For more information, see `aeroReadSpaceWeatherData`.

If the file is not on the MATLAB® path, specify the full pathname. The MAT file must contain these
variables from the space weather data file:

- `YEAR`
- `MONTH`
- `DAY`
- `AP1`
- `AP2`
- `AP3`
- `AP4`
- `AP5`
- `AP6`
- `AP7`
- `AP8`
- `AP_AVG`
- `F107_OBS`
- `F107_DATA_TYPE`
- `F107_OBS_CENTER81`

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to
  `Earth`.
- Set the **Include atmospheric drag** parameter to
  `on`.
- Set the **Atmospheric density source** parameter to
  `Dialog`.
- Set **Atmospheric model** to
  `NRLMSISE-00`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SpaceWeatherDataFile` |
| **Type**: character vector |
| **Values**: `'aeroSpaceWeatherData.mat'` | MAT file name |
| **Default**: `'aeroSpaceWeatherData.mat'` |

### **F10.7 extrapolation method** — Extrapolation method for `f107Average` and `f107Daily` `None - clip` (default) | `Constant` | `Least squares fit`

Extrapolation method for `f107Average` and
`f107Daily` for times outside the range of the MAT file data,
specified as one of these values.

| Method | Description |
| --- | --- |
| `None - clip` | Set `f107Average` and `f107Daily` to the nearest data point available in the MAT file. |
| `Constant` | Set `f107Average` and `f107Daily` to a constant value specified by the **Magnetic index extrapolation method** parameter value. |
| `Least squares fit` | Approximate `f107Average` and `f107Daily` using a least-squares fit of the space weather data from October 1, 1957, to December 1, 2040. This method uses a trigonometric function of the form:  `a + b*cos(c*t + d*sin(e*t))`,  where:    - *a* is   `128.2351780622538` - *b* is `54.3285872213434` - *c* is `0.0015460708364` - *d* is `0.2429462096495` - *e* is `0.0015563188188` - *t* is *jdCurrent* -   *jdReftime* - *jdCurrent* is the current Julian date - *jdRef* is `2436112.5` |

**Note**

For `f107Average` values,if part of the 81-day period falls
inside the MAT file range of space weather data, the Solar Flux and
Geomagnetic Index block uses the actual daily values from the overlapping
portion. To calculate the average for the nonoverlapping portion, the block uses the
clipped, constant, or least squares daily value.

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to
  `Earth`.
- Set the **Include atmospheric drag** parameter to
  `on`.
- Set the **Atmospheric density source** parameter to
  `Dialog`.
- Set **Atmospheric model** to
  `NRLMSISE-00`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `F107ExtrapMethod` |
| **Type**: character vector |
| **Values**: `'None - clip'` | `'Constant'` | `'Least squares fit'` |
| **Default**: `'None - clip'` |

### **Magnetic index extrapolation method** — Extrapolation method for magnetic index information `None - clip` (default) | `Constant` | `IGRF`

Extrapolation method for magnetic index information values for times outside the
range of the MAT file data, specified as one of these values.

| Method | Description |
| --- | --- |
| `None - clip` | Set elements of magnetic index information to the nearest data point available in the MAT file. |
| `Constant` | Set elements of magnetic index information to a constant value specified by the **Magnetic index extrapolation method** parameter.  The elements of magnetic index for times outside this range are based on clipped values of the horizontal magnetic field strength at these time limits. |
| `IGRF` | Calculate the elements of magnetic index information using the International Geomagnetic Reference Field. Because this model is defined for times between January 1, 1900, 12:00 AM UTC and January 1, 2025, 12:00 AM UTC, the predictions for times outside this range are clipped to values at these time limits. |

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to
  `Earth`.
- Set the **Include atmospheric drag** parameter to
  `on`.
- Set the **Atmospheric density source** parameter to
  `Dialog`.
- Set **Atmospheric model** to
  `NRLMSISE-00`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MagneticIndexExtrapMethod` |
| **Type**: character vector |
| **Values**: `'None - clip'` | `'Constant'` | `'IGRF'` |
| **Default**: `'None - clip'` |

### **Flags source** — Variation flag source `Dialog` (default) | `Port`

Variation flag source, specified as `Dialog` or
`Port`.

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to
  `Earth`.
- Set the **Include atmospheric drag** parameter to
  `on`.
- Set the **Atmospheric density source** parameter to
  `Dialog`.
- Set the **Atmospheric model** parameter to
  `NRLMSISE-00`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `fluxFlagsSrc` |
| **Type:** character vector |
| **Values:** `'Dialog'` | `'Port'` |
| **Default:** `'Dialog'` |

### **Flags** — Variation flags `ones(1,23)` (default)

Variation flags, specified as an array of 23 (`ones(1,23)`). You
can specify one of the following values for a field. The default value for each field
is `1`.

- 0.0 — Removes the effect on the output.
- 1.0 — Applies the main and the cross-term effects of that value on the
  output.
- 2.0 — Applies only the cross-term effect of that value on the output.

The array has these fields.

| Field | Description |
| --- | --- |
| `Flags(1)` | F10.7 effect on mean |
| `Flags(2)` | Independent of time |
| `Flags(3)` | Symmetrical annual |
| `Flags(4)` | Symmetrical semiannual |
| `Flags(5)` | Asymmetrical annual |
| `Flags(6)` | Asymmetrical semiannual |
| `Flags(7)` | Diurnal |
| `Flags(8)` | Semidiurnal |
| `Flags(9)` | Daily AP. If you set this field to -1, the block uses the entire matrix of magnetic index information (APH) instead of `APH(:,1)`. |
| `Flags(10)` | All UT, longitudinal effects |
| `Flags(11)` | Longitudinal |
| `Flags(12)` | UT and mixed UT, longitudinal |
| `Flags(13)` | Mixed AP, UT, longitudinal |
| `Flags(14)` | Terdiurnal |
| `Flags(15)` | Departures from diffusive equilibrium |
| `Flags(16)` | All exospheric temperature variations |
| `Flags(17)` | All variations from 120,000 meter temperature (TLB) |
| `Flags(18)` | All lower thermosphere (TN1) temperature variations |
| `Flags(19)` | All 120,000 meter gradient (S) variations |
| `Flags(20)` | All upper stratosphere (TN2) temperature variations |
| `Flags(21)` | All variations from 120,000 meter values (ZLB) |
| `Flags(22)` | All lower mesosphere temperature (TN3) variations |
| `Flags(23)` | Turbopause scale height variations |

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to
  `Earth`.
- Set the **Include atmospheric drag** parameter to
  `on`.
- Set the **Flags source** to
  `Dialog`.
- Set the **Atmospheric density source** parameter to
  `Dialog`.
- Set the **Atmospheric model** parameter to
  `NRLMSISE-00`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `fluxFlags` |
| **Type:** character vector |
| **Values:** `'ones(1,23)'` |
| **Default:** `'ones(1,23)'` |

### **Include anomalous oxygen in density calculation** — Option to include anomalous oxygen in density calculation off (default) | on

To include anomalous oxygen in density calculations, select this check box.

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to
  `Earth`.
- Set the **Include atmospheric drag** parameter to
  `on`.
- Set the **Atmospheric density source** parameter to
  `Dialog`.
- Set the **Atmospheric model** parameter to
  `NRLMSISE-00`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `useOxygen` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Drag coefficient source** — Source of drag coefficient `Dialog` (default) | `Port`

Source of drag coefficient, specified as `Dialog` or
`Port`.

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to
  `Earth`.
- Set the **Include atmospheric drag** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `dragCoeffSrc` |
| **Type:** character vector |
| **Values:** `'Dialog'` | `'Source'` |
| **Default:** `'Dialog'` |

### **Drag coefficient** — Spacecraft coefficient of drag 2.179 (default) | scalar | vector of size *numSat*

Spacecraft coefficient of drag used by atmospheric drag calculation, specified as
a scalar or as a vector of size *numSat*.

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to
  `Earth`.
- Set the **Include atmospheric drag** parameter to
  `on`.
- Set the **Drag coefficient source** parameter to
  `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `dragCoeff` |
| **Type:** character vector |
| **Values:** scalar | vector of size *numSat* |
| **Default:** `'2.179'` |

### **Drag area source** — Source of drag area `Dialog` (default) | `Port`

Source of drag area, specified as `Dialog` or
`Port`.

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to
  `Earth`.
- Set the **Include atmospheric drag** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `dragAreaSrc` |
| **Type:** character vector |
| **Values:** `'Dialog'` | `'Source'` |
| **Default:** `'Dialog'` |

### **Drag area** — Area to compute acceleration due to atmospheric drag 1.0 (default) | scalar | vector of size *numSat*

Area to compute acceleration due to atmospheric drag, specified as a scalar or as
a vector of size *numSat*. This area of the spacecraft is
perpendicular to the spacecraft relative velocity.

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to
  `Earth`.
- Set the **Include atmospheric drag** parameter to
  `on`.
- Set the **Drag area source** parameter to
  `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `dragArea` |
| **Type:** character vector |
| **Values:** scalar | vector of size *numSat* |
| **Default:** `'1.0'` |

### Third Body

Configure third body point mass for gravitational acceleration.

### **Ephemeris model** — Ephemeris model `DE405` (default) | `DE421` | `DE423` | `DE430` | `DE432t`

Select one of these ephemerides models defined by the Jet Propulsion Laboratory.
The block uses ephemeris data to calculate relative celestial positions required for
third body point mass gravity and solar radiation pressure.

| **Ephemeris Model** | Description |
| --- | --- |
| `DE405` | Released in 1998. This ephemeris takes into account the Julian date range 2305424.50 (December 9, 1599) to 2525008.50 (February 20, 2201).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 1.0, adopted in 1998. |
| `DE421` | Released in 2008. This ephemeris takes into account the Julian date range 2414992.5 (December 4, 1899) to 2469808.5 (January 2, 2050).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 1.0, adopted in 1998. |
| `DE423` | Released in 2010. This ephemeris takes into account the Julian date range 2378480.5 (December 16, 1799) to 2524624.5 (February 1, 2200).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 2.0, adopted in 2010. |
| `DE430` | Released in 2013. This ephemeris takes into account the Julian date range 2287184.5 (December 21, 1549) to 2688976.5 (January 25, 2650).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 2.0, adopted in 2010. |
| `DE432t` | Released in April 2014. This ephemeris takes into account the Julian date range 2287184.5, (December 21, 1549 ) to 2688976.5, (January 25, 2650).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 2.0, adopted in 2010. |

**Note**

This block requires that you download ephemeris data using the Add-On Explorer.
To start the Add-On Explorer, in the MATLAB Command Window, type `aeroDataPackage`. in the MATLAB desktop toolstrip, click **Add-Ons**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ephemerisModel` |
| **Type**: character vector |
| **Values**: `DE405` | `DE421` | `DE423` | `DE430` |
| **Default**: `'DE405'` |

### **Limit ephemerides date range** — Option to enable start and end of range of ephemeris data `off` (default) | `on`

Control how much data is loaded into memory during simulation and how much data is
included in generated code for the block:

- Select this check box to limit the loading of ephemeris data to a specified
  date range.
- Clear this check box to include data for the complete date range defined in
  the **Ephemeris model**
  table.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `useDateRange` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Start date (JD)** — Start date of ephemerides date range `juliandate(2020, 1, 1)` (default) | Julian date

Start date of ephemerides date range, specified as a Julian date.

#### Dependencies

To enable this parameter set the **Limit ephemerides date
range** parameter to `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `startDate` |
| **Type**: character vector |
| **Values**: `'juliandate(2020, 1, 1)'` | Julian date |
| **Default**: `'juliandate(2020, 1, 1)'` |

### **End date (JD)** — End date of ephemerides date range `juliandate(2050, 1, 1)` (default) | Julian date

End date of ephemerides date range, specified as a Julian date.

#### Dependencies

To enable this parameter, set the **Limit ephemerides date
range** parameter to `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `endDate` |
| **Type**: character vector |
| **Values**: `'juliandate(2050, 1, 1)'` | Julian format date |
| **Default**: `'juliandate(2050, 1, 1)'` |

### **Include third body gravity** — Acceleration due to third body gravity `off` (default) | `on`

To include acceleration due to third body gravity in orbit propagation
calculation, select this check box. Otherwise, clear this check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `useThirdBodyGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Sun** — Include gravitational acceleration due to Sun `on` (default) | `off`

To include gravitational acceleration due to Sun, select this check box.
Otherwise, clear it. To specify the gravity model, select it from Sun gravity model.

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to any value other than
  `Sun`.
- Set the **Include third body gravity** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `includeSunGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'on'` |

### **Sun gravity model** — Third body gravity model for Sun `Point-mass` (default) | `Oblate ellipsoid (J2)`

Select a gravitational potential model from the list to use when
**Sun** third body gravity parameter is selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to any value other than
  `Sun`.
- Set the **Include third body gravity** parameter to
  `on`.
- Set the **Sun** third body gravity parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sunThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Mercury** — Include gravitational acceleration due to Mercury `off` (default) | `on`

To include gravitational acceleration due to Mercury, select this check box.
Otherwise, clear it. To specify the gravity model, select it from Mercury gravity model.

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to any value other than
  `Mercury`.
- Set the **Include third body gravity** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `includeMercuryGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Mercury gravity model** — Mercury gravity model `Point-mass` (default) | `Oblate ellipsoid (J2)`

Select a gravitational potential model from the list to use when
**Mercury** third body gravity parameter is selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to any value other than
  `Sun`.
- Set the **Include third body gravity** parameter to
  `on`.
- Set the **Mercury** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `mercuryThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Venus** — Include gravitational acceleration due to Venus `off` (default) | `on`

To include gravitational acceleration due to Venus, select this check box.
Otherwise, clear it. To specify the gravity model, select it from Venus gravity model.

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to any value other than
  `Venus`.
- Set the **Include third body gravity** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `includeVenusGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Venus gravity model** — Venus gravity model `Point-mass` (default) | `Oblate ellipsoid (J2)`

Select a gravitational potential model from the list to use when
**Venus** third body gravity parameter is selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to any value other than
  `Sun`.
- Set the **Include third body gravity** parameter to
  `on`.
- Set the **Venus** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `venusThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Earth** — Include gravitational acceleration due to Earth `on` (default) | `off`

To include gravitational acceleration due to Earth, select this check box.
Otherwise, clear it. To specify the gravity model, select it from Earth gravity model.

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to any value other than
  `Earth`.
- Set the **Include third body gravity** to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `includeEarthGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Earth gravity model** — Earth gravity model `Point-mass` (default) | `Oblate ellipsoid (J2)` | `Spherical harmonics`

Select a gravitational potential model from the list to use when
**Earth** third body gravity parameter is selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`
- `Spherical harmonics`

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to any value other than
  `Earth`.
- Set the **Include third body gravity** parameter to
  `on`.
- Set the **Earth** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `earthThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` | `'Spherical harmonics'` |
| **Default:** `'Point-mass'` |

### **Moon** — Include gravitational acceleration due to Moon `on` (default) | `off`

To include gravitational acceleration due to Moon, select this check box.
Otherwise, clear it. To specify the gravity model, select it from Moon gravity model.

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to any value other than
  `Moon`.
- Set the **Include third body gravity** to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `includeMoonGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` | |
| **Default:** `'on'` |

### **Moon gravity model** — Moon gravity model `Point-mass` (default) | `Oblate ellipsoid (J2)` | `Spherical harmonics`

Select a gravitational potential model from the list to use when
**Moon** third body gravity parameter is selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`
- `Spherical harmonics`

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to any value other than
  `Moon`.
- Set the **Include third body gravity** parameter to
  `on`.
- Set the **Moon** parameter to `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `moonThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` | `'Spherical harmonics'` |
| **Default:** `'Point-mass'` |

### **Mars** — Include gravitational acceleration due to Mars `off` (default) | `on`

To include gravitational acceleration due to Mars, select this check box.
Otherwise, clear it. To specify the gravity model, select it from Mars gravity model.

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to any value other than
  `Mars`.
- Set the **Include third body gravity** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `includeMarsGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` | |
| **Default:** `'off'` |

### **Mars gravity model** — Mars gravity model `Point-mass` (default) | `Oblate ellipsoid (J2)` | `Spherical harmonics`

Select a gravitational potential model from the list to use when
**Mars** third body gravity parameter is selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`
- `Spherical harmonics`

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to any value other than
  `Mars`.
- Set the **Include third body gravity** parameter to
  `on`.
- Set the **Mars** parameter to `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `marsThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` | `'Spherical harmonics'` |
| **Default:** `'Point-mass'` |

### **Jupiter** — Include gravitational acceleration due to Jupiter `off` (default) | `on`

To include gravitational acceleration due to Jupiter, select this check box.
Otherwise, clear it. To specify the gravity model, select it from Jupiter gravity model.

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to any value other than
  `Jupiter`.
- Set the **Include third body gravity** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `includeJupiterGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Jupiter gravity model** — Jupiter gravity model `Point-mass` (default) | `Oblate ellipsoid (J2)`

Select a gravitational potential model from the list to use when
**Jupiter** third body gravity parameter is selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to any value other than
  `Jupiter`.
- Set the **Include third body gravity** parameter to
  on.
- Set the **Jupiter** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `jupiterThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Saturn** — Include gravitational acceleration due to Saturn `off` (default) | `on`

To include gravitational acceleration due to Saturn, select this check box.
Otherwise, clear it. To specify the gravity model, select it from Saturn gravity model.

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to any value other than
  `Saturn`.
- Set the **Include third body gravity** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `includeSaturnGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Saturn gravity model** — Saturn gravity model `Point-mass` (default) | `Oblate ellipsoid (J2)`

Select a gravitational potential model from the list to use when
**Saturn** third body gravity parameter is selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to any value other than
  `Saturn`.
- Set the **Include third body gravity** parameter to
  `on`.
- Set the **Saturn** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `saturnThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Uranus** — Include gravitational acceleration due to Uranus `off` (default) | `on`

To include gravitational acceleration due to Uranus, select this check box.
Otherwise, clear it. To specify the gravity model, select it from Uranus gravity model.

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to any value other than
  `Uranus`.
- Set the **Include third body gravity** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `includeUranusGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Uranus gravity model** — Uranus gravity model `Point-mass` (default) | `Oblate ellipsoid (J2)`

Select a gravitational potential model from the list to use when
**Uranus** third body gravity parameter is selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to any value other than
  `Uranus`.
- Set the **Include third body gravity** parameter to
  `on`.
- Set the **Uranus** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `uranusThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Neptune** — Include gravitational acceleration due to Neptune `off` (default) | `on`

To include gravitational acceleration due to Neptune, select this check box.
Otherwise, clear it. To specify the gravity model, select it from Neptune gravity model.

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to any value other than
  `Neptune`.
- Set the **Include third body gravity** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `includeNeptuneGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Neptune gravity model** — Neptune gravity model `Point-mass` (default) | `Oblate ellipsoid (J2)`

Select a gravitational potential model from the list to use when
**Neptune** third body gravity parameter is selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### Dependencies

To enable this parameter:

- Set the **Central Body** parameter to any value other than
  `Neptune`.
- Set the **Include third body gravity** parameter to
  `on`.
- Set the **Neptune** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `neptuneThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Pluto** — Include gravitational acceleration due to Pluto `off` (default) | `on`

To include gravitational acceleration due to Pluto, select this check box.
Otherwise, clear it. To specify the gravity model, select it from Pluto gravity model.

#### Dependencies

To enable this parameter, set the **Include third body
gravity** parameter to `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `includePlutoGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Pluto gravity model** — Pluto gravity model `Point-mass` (default) | `Oblate ellipsoid (J2)`

Select a gravitational potential model from the list to use when
**Pluto** third body gravity parameter is selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### Dependencies

To enable this parameter:

- Set the **Include third body gravity** parameter to
  `on`.
- Set the **Pluto** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `plutoThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Custom** — Include gravitational acceleration due to custom planet `off` (default) | `on`

To include gravitational acceleration due to a custom planet, select this check
box. Otherwise, clear it. To specify the gravity model, select it from Custom gravity model.

#### Dependencies

To enable this parameter, set the **Include third body
gravity** parameter to `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `includeCustomGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Custom gravity model** — Custom gravity model `Point-mass` (default) | `Oblate ellipsoid (J2)` | `Spherical harmonics`

Select a gravitational potential model from the list to use when
**Custom** third body gravity parameter is selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`
- `Spherical harmonics`

#### Dependencies

To enable this parameter:

- Select the **Include third body gravity** parameter.
- Select the **Custom** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `customThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Gravitational parameter (m^3/s^2)** — Custom gravitational acceleration `42.828314258067e12` (default) | scalar | vector of length *numCustom3rdBodies*

Custom gravitational acceleration for custom third body, specified as a scalar or
as a vector of length *numCustom3rdBodies*.
*numCustom3rdBodies* is the number of rows provided to the
**R\_cb** input port. Provide more than one value to include
multiple custom bodies.

#### Dependencies

To enable this parameter:

- Set the **Include third body gravity** parameter to
  `on`.
- Set the **Custom** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `customThirdBodyMu` |
| **Type:** character vector |
| **Values**: `'42.828314258067e12'` | scalar | vector of length *numCustom3rdBodies* |
| **Default:** `'42.828314258067e12'` |

### SRP

### **Include solar radiation pressure (SRP)** — Acceleration due to solar radiation pressure `off` (default) | `on`

To include acceleration due to solar radiation pressure in orbit propagation
calculation, select this check box. Otherwise, clear the check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `useSRP` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Eclipse fraction source** — Source of eclipse fraction `Dialog` (default) | `Port`

Source of the eclipse fraction (fraction of solar disk visible from the spacecraft
location), specified as `Dialog` or
`Port`.

#### Dependencies

To enable this parameter set the **Include solar radiation pressure
(SRP)** parameter to `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `useSRP` |
| **Type**: character vector |
| **Values**: `'Dialog'` | `'Port'` |
| **Default**: `'Dialog'` |

### **Shadow model** — Shadow model `Dual cone` (default) | `Cylindrical`

Shadow model for eclipse calculations, specified as one of these values.

- `Cylindrical` — Fraction can be 0.0 (Umbra) or 1.0
  (Sunlight).
- `Dual cone` — Fraction can be 0.0 (Umbra), between
  0.0 and 1.0 (Penumbra or Antumbra), or 1.0 (Sunlight).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `shadowModel` |
| **Type:** character vector |
| **Values:** `'Dual cone'` | `'Cylindrical'` |
| **Default:** `'Dual cone'` |

### **Include Earth** — Option to include Earth `on` (default) | `off`

Option to include Earth as a secondary occulting body in eclipse calculations when
central body is Moon.

#### Dependencies

Set the **Central body** parameter to
`Moon`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `includeEarth` |
| **Type**: character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'on'` |

### **Include Moon** — Option to include Moon `on` (default) | `off`

Option to include Moon as a secondary occulting body in eclipse calculations when
central body is Earth.

#### Dependencies

Set the **Central body** parameter to
`Earth`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `includeMoon` |
| **Type**: character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'on'` |

### **Reflectivity coefficient source** — Source for spacecraft coefficient of reflectivity `'Dialog'` (default) | `'Port'`

Source for the spacecraft coefficient of reflectivity, specified as
`Dialog` or `Port`.

#### Dependencies

To enable this parameter, set the **Include solar radiation pressure
(SRP)** to `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `reflectivityCoeffSrc` |
| **Type**: character vector |
| **Values:** `'Dialog'` | `'Port'` |
| **Default:** `'on'` |

### **Reflectivity coefficient** — Spacecraft coefficient of reflectivity `1.8` (default) | scalar | 2D array of size *numSat* | between `[1,2]`

Spacecraft coefficient of reflectivity used by solar radiation pressure
calculation, specified as a scalar, 2D array of size *numSat*.
*numSat* is the number of spacecraft.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set the **Include solar radiation pressure (SRP)**
  parameter to `on`.
- Set the **Reflectivity coefficient source** parameter to
  `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `reflectivityCoeff` |
| **Type**: character vector |
| **Values:** `'1.8'` | scalar | 2D array of size *numSat* | between `[1,2]` |
| **Default:** `'1.8'` |

### **SRP area source** — Source for spacecraft solar radiation pressure area `Dialog` (default) | `Port`

Source for the spacecraft solar radiation pressure (SRP) area, specified as
`Dialog` or `Port`.

#### Dependencies

To enable this parameter, set the **Include solar radiation pressure
(SRP)** parameter to `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `srpAreaSrc` |
| **Type**: character vector |
| **Values:** `'Dialog'` | `'Port'` |
| **Default:** `'Dialog'` |

### **SRP area** — Cross section area of the spacecraft seen by the Sun `1.0` (default) | scalar | 2D array of size *numSat*

Cross section area of the spacecraft seen by the Sun, specified as a scalar or as
a 2D array of size *numSat*. *numSat* is the number
of spacecraft.

**Tunable:** Yes

#### Dependencies

To enable this parameter

- Set the **Include solar radiation pressure (SRP)**
  parameter to `on`.
- Set the **SRP area source** parameter to
  `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `srpArea` |
| **Type**: character vector |
| **Values:** `'1.0'` | scalar | 2D array of size *numSat* |
| **Default:** `'1.0'` |

### **Solar flux pressure (W\*s/m^3)** — Spacecraft solar flux pressure `4.5344321e-6` (default) | scalar

Solar flux pressure, specified as a scalar.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Include solar radiation pressure
(SRP)** parameter to `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `fluxPressure` |
| **Type**: character vector |
| **Values:** `4.5344321e-6` | scalar |
| **Default:** `'4.5344321e-6'` |

### Units

### **Units** — Parameter and port units `Metric (m/s)` (default) | `Metric (km/s)` | `Metric (km/h)` | `English (ft/s)` | `English (kts)`

Parameter and port units, specified as shown here.

| Units | Forces | Moment | Mass | Inertia | Distance | Velocity | Acceleration | Area | Density |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Metric (m/s)` | Newton | Newton-meter | Kilograms | Kilogram m2 | meters | meters/sec | meters/sec2 | m2 | kg/m3, some density outputs 1/m3 |
| `Metric (km/s)` | Newton | Newton-meter | Kilograms | Kilogram m2 | kilometers | kilometers/sec | kilometers/sec2 | m2 | kg/m3, some density outputs 1/m3 |
| `Metric (km/h)` | Newton | Newton-meter | Kilograms | Kilogram m2 | kilometers | kilometers/hour | kilometers/hour2 | m2 | kg/m3, some density outputs 1/m3 |
| `English (ft/s)` | Pound-force | Foot-pound | Slugs | Slug ft2 | feet | feet/sec | feet/sec2 | feet2 | lbm/ft3, some density outputs 1/ft3 |
| `English (kts)` | Pound-force | Foot-pound | Slugs | Slug ft2 | nautical mile | knots | knots/sec | feet2 | lbm/ft3, some density outputs 1/ft3 |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `units` |
| **Type:** character vector |
| **Values:** `'Metric (m/s)'` | `'Metric (km/s)'` | `'Metric (km/h)'` | `'English (ft/s)'` | `'English (kts)'` |
| **Default:** `'Metric (m/s)'` |

### **Angle units** — Angle units `Degrees` (default) | `Radians`

Parameter and port units for angles, specified as
`Degrees` or `Radians`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `angleUnits` |
| **Type:** character vector |
| **Values:** `'Degrees'` | `'Radians'` |
| **Default:** `'Degrees'` |

### **Time format** — Time format for start date and time output `Julian date` (default) | `Gregorian`

Time format for **Start date/time (UTC Julian date)** and output
port **tutc**, specified as
`Julian date` or `Gregorian`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `timeFormat` |
| **Type:** character vector |
| **Values:** `'Julian date'` | `'Gregorian'` |
| **Default:** `'Julian date'` |
## Libraries

Aerospace Blockset / Spacecraft / Spacecraft Dynamics

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

### R2025a: Spacecraft Dynamics block supports high fidelity gravity effects for third bodies

The Spacecraft Dynamics block now supports higher fidelity workflows using new
third body gravity options. Use these options to more accurately model orbit propagation in
spacecraft simulations.

To access these effects, select the **Include third body gravity**
parameter on the **Third Body** tab. The **Include third body
gravity** parameter replaces the **Include third body point-mass
gravity** parameter.

Selecting **Include third body gravity** lets you configure the
gravity options for the Sun, Mercury, Venus, Moon, Earth, Mars, Jupiter, Saturn, Uranus,
Neptune, Pluto, and Custom.

### R2023b: Spacecraft Dynamics Block Changes

The Spacecraft Dynamics block has been updated to take into account:

- The effects of third body gravity on orbit propagation.
- Space weather data from a data file generated by the `aeroReadSpaceWeatherData` function.
- Solar radiation pressure (SRP).

## Description

Model dynamics of one or more spacecraft

The Spacecraft Dynamics block models translational and rotational dynamics
of spacecraft using numerical integration. It computes the position, velocity, attitude, and
angular velocity of one or more spacecraft over time. For the most accurate results, use a
variable step solver with low tolerance settings (less than 1e-8). To trade off accuracy for
speed, use larger tolerances, depending on your mission requirements.

You can define initial orbital states as

- A set of orbital elements.
- Position and velocity state vectors.

To propagate orbital states, the block uses the gravity model selected for the current
central body. It also includes external accelerations and forces that you provide as inputs to
the block. To define initial attitude states, use quaternions, direction cosine matrices
(DCMs), or Euler angles.

To propagate attitude states, the block uses moments provided as inputs to the block and
mass properties defined on the block.

Aerospace Blockset™ uses quaternions that are defined using the scalar-first convention.

The Spacecraft Dynamics block supports scalar and vector expansion. The
block parameter and input port dimensions determine the number of the output signals and the
number of spacecraft. After scalar and vector expansion, all parameters in the
**Orbit**, **Mass**, and **Attitude**
tabs and all input ports except for **φθψ** (Moon libration angles) and
**αδW** (right ascension, declination, and rotation angle) input ports are
defined for each spacecraft.

The size of the provided initial conditions determines the number of spacecraft being
modeled. If you supply more than one value for a parameter in the **Orbit**,
**Attitude**, or **Mass** tabs, the block outputs a
constellation of satellites. Any parameter with a single provided value is expanded and
applied to all the satellites in the constellation. For example, if you provide a single value
for all the parameters on the block except **True anomaly**, which contains
six values, the block creates a constellation of six satellites, varying true anomaly
only.

The block applies the same expansion behavior to the block input ports. All input ports
support expansion except **Moon libration angles** (when **Central
body** is `Moon`) and **Spin axis right ascension
(RA) at J2000**, **Spin axis declination (Dec) at J2000**, and
**Initial rotation angle at J2000** (when **Central body**
is `Custom`). All other ports accept either a single value expanded
to all spacecraft being modeled, or individual values applied to each spacecraft.

For more information on the coordinate systems and rotational and translational dynamics
the Spacecraft Dynamics block uses, see Algorithms.

### Atmospheric Drag

To help model the drag on spacecraft for high precision orbit propagation, the
Spacecraft Dynamics block supports drag. Atmospheric drag affects spacecraft flying
at low Earth orbit (LEO); it is less relevant further away from Earth. For the atmospheric
drag equation, see Translational Dynamics.

### Third Body Gravity Effects

To include the effects of point-mass Third Body gravity, select which third bodies to include. These calculations require an **Ephemeris model** and data. For the third body contribution equation, see Translational Dynamics.

### Solar Radiation Pressure

To include the effects of solar radiation pressure (SRP) on the spacecraft, provide an eclipse fraction or specify a shadow model to compute the
fraction. Consider taking solar radiation pressure into account when atmosphere drag is
negligible and pointing accuracy requirements are strict. For the solar radiation pressure
equation, see Translational Dynamics.
