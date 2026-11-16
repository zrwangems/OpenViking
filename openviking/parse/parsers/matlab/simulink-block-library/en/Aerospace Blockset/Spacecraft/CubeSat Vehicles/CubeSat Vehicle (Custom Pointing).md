---
type: simulink-block
title: 'CubeSat Vehicle Earth (Nadir) Pointing'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Spacecraft / CubeSat Vehicles'
documentation_page: 'cubesatvehicleearthnadirpointing'
documentation_source_path: 'cubesatvehicleearthnadirpointing.html'
language: en
---

# CubeSat Vehicle Earth (Nadir) Pointing

## Ports

### Input

### **AECEF (m/s2)** — Vehicle accelerations vector of size 3

Vehicle gravity accelerations (including gravity) used for orbit propagation,
specified as a vector of size 3, in m/s2.

**Data Types:** `single` | `double`

### **1st AlignmentBody** — Primary alignment vector three-element vector

Primary alignment vector, in the Body frame, to align with primary constraint
vector.

**Data Types:** `double`

### **1st ConstraintECI** — Primary constraint vector three-element vector

Primary constraint vector specifying the direction in which to align the primary
alignment vector.

#### Dependencies

This port is not available when **Pointing mode** is set to
`Earth (Nadir) Pointing` or `Sun
Tracking`, which have implied primary constraint vectors.

**Data Types:** `double`

### **1st AlignmentBody** — Primary alignment vector three-element vector

Primary alignment vector, in the Body frame, to align with primary constraint
vector.

**Data Types:** `double`

### **1st ConstraintECI** — Primary constraint vector three-element vector

Primary constraint vector specifying the direction in which to align the primary
alignment vector.

#### Dependencies

- The direction depends on the **Constraint coordinate
  system**.
- This port is not available when **Pointing mode** is set to
  `Earth (Nadir) Pointing` or `Sun
  Tracking`, which have implied primary constraint vectors.

**Data Types:** `double`

### **2nd AlignmentBody** — Secondary alignment vector three-element vector

Secondary alignment vector, in the Body frame, to align with secondary constraint
vector.

**Data Types:** `double`

### **2nd ConstraintECI** — Secondary constraint vector three-element vector

Secondary constraint vector specifying the direction in which to align the
secondary alignment vector.

#### Dependencies

The direction depends on the **Constraint coordinate
system**.

**Data Types:** `double`
### Output

### **XECEF** — CubeSat position three-element vector

Earth-centered Earth-fixed CubeSat position components, specified as a 3-by-1
array.

**Data Types:** `double`

### **VECEF** — Velocity components 3-by-1 array

Earth-centered Earth-fixed velocity components, specified as a 3-by-1
array.

**Data Types:** `double`

### **qECI2Body** — Quaternion rotation 4-by-1 array

Quaternion rotation from Earth-centered inertial frame to Body frame.

**Data Types:** `double`

### **qECEF2Body** — Quaternion array 4-by-1 array

Quaternion rotation from Earth-centered Earth-fixed frame to Body frame.

**Data Types:** `double`

## Parameters

### **Start date [Julian date]** — Initial start date of simulation `2458488` (default) | Julian date

Initial start date of simulation. The block defines initial conditions using this
date.

**Tip**

To calculate the Julian date, use the `juliandate` function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sim_t0` |
| **Type:** character vector |
| **Values:** Julian date |
| **Default:** `'2458488'` |

### CubeSat Orbit

### **Input method** — Initial vehicle `Keplerian Orbital Elements` (default) | `ECI Position and Velocity` | `ECEF Position and Velocity` | `Geodetic LatLonAlt and Velocity in NED`

Initial vehicle position and velocity input method.

#### Dependencies

Selecting the `Keplerian Orbital Elements` input method
enables these parameters:

- **Epoch of ECI frame [Julian date]**
- **Semi-major axis [m]**
- **Eccentricity**
- **Inclination [deg]**
- **Right ascension of the ascending node [deg]**
- **Argument of periapsis [deg]**
- **True anomaly [deg]**
- **True longitude [deg] (circular equatorial)**
- **Argument of latitude [deg] (circular inclined)**
- **Longitude of periapsis [deg] (elliptical
  equatorial)**

Selecting the `ECI Position and Velocity` input method
enables these parameters:

- **Epoch of ECI frame [Julian date]**
- **ECI position vector [m]**
- **ECI velocity vector [m/s]**

Selecting the `ECEF Position and Velocity` input method
enables these parameters:

- **ECEF position vector [m]**
- **ECEF velocity vector [m/s]**

Selecting the `Geodetic LatLonAlt and Velocity in NED`
input method enables these parameters:

- **Geodetic latitude, longitude, altitude [deg, deg,
  m]**
- **NED velocity vector [m/s]**

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `method` |
| **Type:** character vector |
| **Values:** `'Keplerian Orbital Elements'` | `'ECI Position and Velocit'` | `'ECEF Position and Velocity'` | `'Geodetic LatLonAlt and Velocity in NED'` |
| **Default:** `'Keplerian Orbital Elements'` |

### **Epoch of ECI frame [Julian date]** — Epoch of ECI frame `2451545` (default) | Julian date

Epoch of ECI frame, specified as a Julian date.

**Tip**

To calculate the Julian date for a particular date, use the `juliandate` function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `epoch` |
| **Type:** character vector |
| **Values:** Julian date format |
| **Default:** `'2451545'` |

### **Semi-major axis [m]** — CubeSat semi-major axis `6878137` (default) | axis in meters

CubeSat semi-major axis (half of the longest orbit diameter), specified in
m.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `a` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'6878137'` |

### **Eccentricity** — Orbital eccentricity `0` (default) | eccentricity greater than or equal to 0

Deviation of the CubeSat orbit from a perfect circle.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ecc` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0'` |

### **Inclination [deg]** — Tilt angle of CubeSat orbital plane `0` | degrees between 0 and 180

Tilt angle of CubeSat orbital plane, specified between 0 and 180 deg.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `incl` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0'` |

### **Right ascension of the ascending node [deg]** — Angular distance in equatorial plane `0` (default) | degrees between 0 and 360

Angular distance in equatorial plane from *x*-axis to location of
the ascending node (point at which the satellite crosses the equator from south to
north), specified between 0 and 360 deg.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `omega` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0'` |

### **Argument of periapsis [deg]** — Angle from CubeSat body ascending node to periapsis `0` (default) | degrees between 0 and 360

Angle from the CubeSat body ascending node to the periapsis (closest point of
orbit to Earth), specified between 0 and 360 deg.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `argp` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0'` |

### **True anomaly [deg]** — Angle between periapsis and current position of CubeSat `0` (default) | degrees between 0 and 360

Angle between the periapsis (closest point of orbit to Earth) and the current
position of CubeSat, specified between 0 and 360 deg.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `nu` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0'` |

### **True longitude [deg] (circular equatorial)** — Angle between *x*-axis of periapsis and position of CubeSat vector `0` (default) | degrees between 0 and 360

Angle between *x*-axis of periapsis and position of CubeSat
vector, specified between 0 and 360 deg.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `truelon` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0'` |

### **Argument of latitude [deg] (circular inclined)** — Angle between ascending node and satellite position vector `0` (default) | degrees between 0 and 360

Angle between ascending node and satellite position vector, specified between 0
and 360 deg.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `arglat` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0'` |

### **Longitude of periapsis [deg] (elliptical equatorial)** — Angle between *x*-axis of periapsis and eccentricity vector `0` (default) | degrees between 0 and 360

Angle between the *x*-axis of the periapsis and the eccentricity
vector, specified between 0 and 360 deg.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `lonper` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0'` |

### **ECI position vector [m]** — Cartesian position vector `[0 0 0]` (default) | vector

Cartesian position vector of satellite in ECI coordinate frame at **Start
Date**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `r_eci` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[0 0 0]'` |

### **ECI velocity vector [m/s]** — Cartesian velocity vector `[0 0 0]` (default) | velocity vector

Cartesian velocity vector of satellite in ECI coordinate frame at **Start
Date**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `v_eci` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[0 0 0]'` |

### **ECEF position vector [m]** — Cartesian position vector `[0 0 0]` (default) | vector

Cartesian position vector of satellite in ECEF coordinate frame at **Start
Date**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `r_ecef` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[0 0 0]'` |

### **ECEF velocity vector [m/s]** — Cartesian velocity vector `[0 0 0]` (default) | velocity vector

Cartesian velocity vector of satellite in ECEF coordinate frame at **Start
Date**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `v_ecef` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[0 0 0]'` |

### **Geodetic latitude, longitude, altitude [deg, deg, m]** — Geodetic latitude and longitude, and altitude `[0 0 0]` (default) | velocity vector

Geodetic latitude and longitude, in deg, and altitude above WGS84 ellipsoid, in
m.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `lla` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[0 0 0]'` |

### **NED velocity vector [m/s]** — Body velocity `[0 0 0]` (default) | velocity vector

Body velocity with respect to Earth-centered Earth-fixed (ECEF), expressed in the
north-east-down (NED) coordinate frame, specified as a vector, in m/s.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `v_ned` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[0 0 0]'` |

### CubeSat Attitude

### **Initial Euler angles (roll, pitch, yaw) [deg]** — Initial Euler rotation angles `[0 0 0]` (default) | vector | degrees

Initial Euler rotation angles (roll, pitch, yaw) between Body and NED coordinate
frames, specified in degrees.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `euler` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[0 0 0]'` |

### **Initial body angular rates [deg/s]** — Initial angular rates `[0 0 -0.05168]` (default) | vector

Initial angular rates with respect to NED frame, expressed in Body frame,
specified as a vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `pqr` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[0 0 0]'` |

### **Pointing mode** — CubeSat vehicle pointing mode `Earth (Nadir) Pointing` (default) | `Sun Tracking` | `Custom Pointing` | `Standby (Off)`

CubeSat vehicle pointing mode, specified as `Earth (Nadir)
Pointing`, `Sun Tracking`, or
`Custom Pointing`. The CubeSat vehicle uses the pointing
mode for precise attitude control. For no attitude control, select
`Standby (Off)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `pointingMode` |
| **Type:** character vector |
| **Values:** `'Earth (Nadir) Pointing'` | `'Sun Tracking'` | `'Custom Pointing'` | `'Standby (Off)'` |
| **Default:** `'Earth (Nadir) Pointing'` |

### **Primary alignment vector (Body wrt BCM)** — Primary alignment vector `Dialog` (default) | `Input port`

Primary alignment vector, in Body frame, to align with primary constraint
vector.

#### Dependencies

- Selecting `Dialog` enables a text box in which you
  specify the primary alignment vector. The default value is `[0 0
  1]`.
- Selecting `Input port` enables the
  1st AlignmentBody input
  port, at which you specify the primary alignment vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `firstAlign` |
| **Type:** character vector |
| **Values:** vector |
| **Default:** `'[0 0 1]'` |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `firstAlignExt` |
| **Type:** character vector |
| **Values:** `'Input port'` | `'Dialog'` |
| **Default:** `'Dialog'` |

### **Secondary alignment vector (Body wrt BCM)** — Secondary alignment vector `Dialog` (default) | `Input port`

Secondary alignment vector, in Body frame, to align with secondary constraint
vector.

#### Dependencies

- Selecting `Dialog` enables a text box in which you
  specify the secondary alignment vector. The default value is `[0 1
  0]`.
- Selecting `Input port` enables the
  2nd AlignmentBody input
  port, at which you specify the secondary alignment vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `secondAlign` |
| **Type:** character vector |
| **Values:** vector |
| **Default:** `'[0 1 0]'` |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `secondAlignExt` |
| **Type:** character vector |
| **Values:** `'Input port'` | `'Dialog'` |
| **Default:** `'Dialog'` |

### **Constraint coordinate system** — Constraint coordinate system `ECI Axes` (default) | `ECEF Axes` | `NED Axes` | `Body-Fixed Axes`

Constraint coordinate system, specified as `ECI Axes`,
`ECEF Axes`, `NED Axes`, or
`Body-Fixed Axes`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `constraintCoord` |
| **Type:** character vector |
| **Values:** `'ECI Axes'` | `'ECEF Axes'` | `'NED Axes'` | `'Body-Fixed Axes'` |
| **Default:** `'ECI Axes'` |

### **Primary constraint vector (wrt BCM)** — Primary constraint vector `Dialog` (default) | `Input port`

Primary constraint vector, in the Body frame, to align with the primary alignment
vector.

#### Dependencies

- This parameter is disabled when **Pointing mode** is
  `Earth (Nadir) Pointing` or `Sun
  Tracking`.
- Selecting `Dialog` enables a text box in which you
  specify the primary constraint vector. The default value is `[1 0
  0]`.
- Selecting `Input port` enables the
  1st constraintBody input
  port, at which you specify the primary constraint vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `firstRef` |
| **Type:** character vector |
| **Values:** vector |
| **Default:** `'[1 0 0]'` |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `firstRefExt` |
| **Type:** character vector |
| **Values:** `'Input port'` | `'Dialog'` |
| **Default:** `'Dialog'` |

### **Secondary constraint vector (wrt BCM)** — Secondary constraint vector `Dialog` (default) | `Input port`

Secondary constraint vector, in the Body frame, to align with the secondary
alignment vector.

#### Dependencies

- Selecting `Dialog` enables a text box in which you
  specify the secondary constraint vector. The default value is `[0 0
  1]`.
- Selecting `Input port` enables the
  2nd constraintBody input
  port, at which you specify the secondary constraint vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `secondRef` |
| **Type:** character vector |
| **Values:** vector |
| **Default:** `'[0 0 1]'` |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `secondRefExt` |
| **Type:** character vector |
| **Values:** `'Input port'` | `'Dialog'` |
| **Default:** `'Dialog'` |

### Mission Analysis

### **Analysis run time source** — Source of run time for mission analysis live script `Dialog` (default) | `Model Stop Time`

Source of run time for mission analysis live script, specified as:

- `Dialog` — Defined in **Run time**
  parameter.
- `Model Stop Time` — Defined in model configuration
  parameter **Stop Time**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `missionRTSource` |
| **Type:** character vector |
| **Values:** `'Dialog'` | `'Model StopTime'` |
| **Default:** `'Dialog'` |

### **Run time [sec]** — Run time for mission analysis live script `6*60*60` (default) | scalar

Run time for mission analysis live script, specified as a scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `missionRT` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'6*60*60'` |

### **Ground station geodetic latitude, longitude [deg, deg]** — Ground station location [42, -71] (default) | vector

Ground station location, specified as a vector, in geodetic latitude and longitude
in deg, deg.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `missionGS` |
| **Type:** character vector |
| **Values:** vector |
| **Default:** `'[42, -71]'` |

### **Run TOI analysis** — Enable time of interest mission analysis on (default) | off

Select this check box to enable time of interest analysis in a mission analysis
live script.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `missionTOICheck` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Time of interest [Julian date]** — Time of interest for mission analysis live script `[]` (default) | Julian date

Time of interest mission analysis, specified as a Julian date. To use the
simulation start date, enter an empty array (`[]`).

**Tip**

To calculate the Julian date, use the `juliandate` function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `missionTOI` |
| **Type:** character vector |
| **Values:** Julian date |
| **Default:** `'[]'` |

### **Camera field-of-view (FOV) half angle (deg)** — Half angle of field of view 55 (default) | `[]` | scalar

Half angle of field of view for nadir on-pointed camera. To exclude from analysis,
enter an empty array (`[]`).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `missionEta` |
| **Type:** character vector |
| **Values:** `'[]'` | scalar |
| **Default:** `'55'` |

### **Live script file name** — File name for mission analysis live script report blank entry (default) | live script file name

File name for mission analysis live script report, generated as a live script. To
create a default mission analysis report with the format
`CubeSatMissionReport_currentdate.mlx`, leave
the parameter blank. To create a live script of the mission analysis report, click the
**Create Live Script Report** button.

#### Dependencies

To create the live script with the specified file name, click the
**Create Live Script Report** button. If this parameter is blank,
the block creates a live script with a default file name.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `missionName` |
| **Type:** character vector |
| **Values:** blank entry | file name |
| **Default:** blank entry |

### **Create Live Script Report** — Analyze mission and create live script report button

To analyze mission and create report in live script format, click this button. To
create a default mission analysis report with the format
`CubeSatMissionReport_currentdate.mlx`, leave
the parameter blank. To create a live script of the mission analysis report, click the
**Create Live Script Report** button.

#### Dependencies

To create the live script with the file name specified in **Live script
file name**, click the **Create Live Script Report**
button. If **Live script file name** is blank, the block creates a
live script with a default file name.

## Libraries

Aerospace Blockset / Spacecraft / CubeSat Vehicles

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

### R2021a: CubeSat Vehicle now propagates in the ECI coordinate frame

The CubeSat Vehicle now propagates in the ECI coordinate frame using
Earth orientation parameters data from the `aeroiersdata.mat` file. Results
differ from previous releases, but are more accurate than with previous versions of the
block.

## Description

Model CubeSat vehicle whose primary alignment vector points towards center of Earth

The CubeSat Vehicle blocks model CubeSat vehicles to provide a high level
mission planning/rapid prototyping option to quickly model and propagate satellite orbits, one
satellite at a time. (To propagate multiple satellites simultaneously, see the Orbit Propagator
block.) To accommodate constellation planning workflows, you can also use these blocks
multiple times in a model. Specify this information for the vehicle:

- Initial orbital state
- Attitude control (pointing) mode

The library contains three versions of the CubeSat Vehicle block
preconfigured for these common attitude control modes. To select these configurations, set the
**Pointing mode** parameter.

- CubeSat Vehicle Earth (Nadir) Pointing — Primary alignment vector
  points towards the center of the Earth
- CubeSat Vehicle Sun Tracking — Primary alignment vector points toward
  the Sun
- CubeSat Vehicle Custom Pointing — Custom alignment and constraint
  vectors
