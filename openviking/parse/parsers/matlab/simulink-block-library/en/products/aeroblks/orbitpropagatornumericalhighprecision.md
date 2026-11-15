---
type: simulink-block
title: 'Orbit Propagator Numerical (high precision)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Spacecraft Simulation'
documentation_page: 'orbitpropagatornumericalhighprecision'
documentation_source_path: 'orbitpropagatornumericalhighprecision.html'
language: en
---

# Orbit Propagator Numerical (high precision)

## Ports

### Input

### **Aicrf** — Applied acceleration 3-element vector | *m*-3 array

Acceleration applied to the spacecraft with respect to the port coordinate system
(ICRF or fixed-frame), specified as a 3-element vector or *m*-by-3
array, at the current time step.

#### Dependencies

To enable this port:

- Set **Propagation method** to `Numerical (high
  precision)`.
- Select the **Input external accelerations** check
  box.

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

- Set **Propagation method** to `Numerical (high
  precision)`.
- Set **Central body** to
  `Moon`.
- Select the **Input Moon libration angles** check
  box.

**Data Types:** `double`

### **αδW** — Right ascension, declination, and rotation angle 3-element vector

Central body spin axis instantaneous right ascension, declination, and rotation
angle, specified as a 3-element vector. This port is available only for custom central
bodies.

#### Dependencies

To enable this port:

- Set **Propagation method** to `Numerical (high
  precision)`.
- Set **Central body** to
  `Custom`.
- Set **Central body spin axis source** to
  `Port`.

**Data Types:** `double`

### **m** — Spacecraft mass used by atmospheric drag calculation scalar | vector of size *numSat*

Spacecraft mass used by atmospheric drag calculation, specified as scalar or
vector of size *numSat*. *numSat* is the number of
spacecraft.

#### Dependencies

To enable this port:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check box.
- Set the **Mass source** parameter to
  `Dialog`.

**Data Types:** `double`

### **ρ** — Atmospheric density scalar

Atmospheric density to calculate acceleration due to atmospheric drag.

#### Dependencies

To enable this port:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check box.
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

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check box.
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

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check box.
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

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check box.
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

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check box.
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

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check box.
- Set the **Drag coefficient source** parameter to
  `Port`.

**Data Types:** `double`

### **Ad** — Atmospheric drag area scalar | vector of size *numSat*

Atmospheric drag area, specified as a scalar or vector of size
*numSat*.

#### Dependencies

To enable this port:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check box.
- Set the **Drag area source** parameter to
  `Port`.

**Data Types:** `double`

### **Rcb, 3** — Position of one or more custom bodies 3-element vector | *numCustom3rdBodies*x3-element vector

Position of one or more custom bodies with respect to the current central body, in the ICRF coordinate frame. *numCustom3rdBodies* is the number of custom bodies. For more information, see **Custom gravitational parameter (m^3/s^2)**.

#### Dependencies

To enable this port:

- Set **Propagation method** to `Numerical (high precision)`.
- Select the **Include third body gravity** check
  box.
- Select the **Custom** check box.

**Data Types:** `double`

### **Fraction** — Fraction of solar disk between `0` (full eclipse) and `1` (full sunlight) | scalar | *numSat*

Fraction of solar disk visible from the spacecraft position. *numSat* is the number of spacecraft.

#### Dependencies

To enable this port:

- Set **Propagation method** to `Numerical (high precision)`.
- Select the **Include solar radiation pressure (SRP)** check box.
- Set **Eclipse fraction source** to `Port`.

**Data Types:** `double`

### **RC** — Reflectivity coefficient scalar or *numSat* of values in the range `1`≤*RC*≤`2`

Reflectivity coefficient, specified as a scalar or *numSat* of values in the
range
`1`≤*RC*≤`2`.
*numSat* is the number of spacecraft.

#### Dependencies

To enable this port:

- Set **Propagation method** to `Numerical (high precision)`.
- Select the **Include solar radiation pressure (SRP)** check box.
- Set the **Reflectivity coefficient
  source** parameter to
  `Port`.

**Data Types:** `double`

### **Asrp** — Cross section area of the spacecraft scalar | *numSat*

Cross section area of the spacecraft seen by the Sun, specified as a scalar or
*numSat*. The block uses this value to calculate
the acceleration due to solar radiation pressure.

#### Dependencies

To enable this port:

- Set **Propagation method** parameter to
  `Numerical (high precision)`.
- Select the **Include solar radiation pressure (SRP)** check box.
- Set **SRP area source** parameter to
  `Port`.

**Data Types:** `double`
### Output

### **Xicrf** — Position of spacecraft 3-element vector | *numSat*-by-3

Position of the spacecraft with respect to (ICRF or fixed-frame), returned as a
3-element vector or *numSat*-by-3 array, where *m*
is number of spacecraft, at the current time step. The size of the initial conditions
provided in the **Orbit** tab control the port dimension.
*numSat* is the number of spacecraft.

**Data Types:** `double`

### **Vicrf** — Velocity 3-element vector | *numSat*-by-3 array

Velocity of the spacecraft with respect to ICRF or fixed-frame, returned as a
3-element vector or *numSat*-by-3 array, at the current time step.
*numSat*-by-3 array. The size of the initial conditions provided in
the **Orbit** tab control the port dimension.

**Data Types:** `double`

### **qicrf2ff** — Transformation 4-element quaternion (scalar first)

Transformation between the ICRF coordinate system and fixed-frame, returned as a
4-element vector (scalar first), at the current time step.

#### Dependencies

To enable this port:

- Set **Propagation method** to `Numerical (high
  precision)`.
- Select the **Output quaternion (ICRF to Fixed-frame)**
  check box.

**Data Types:** `double`

### **tutc** — Time at current time step scalar | 6-element vector

Time at current time step, returned as a:

- scalar — If you specify the **Start data/time** parameter as
  a Julian date.
- 6-element vector — If you specify the **Start data/time**
  parameter as a Gregorian date with six elements (year, month, day, hours, minutes,
  seconds).

This value is equal to the **Start date/time** parameter value +
*the elapsed simulation time*.

#### Dependencies

To enable this parameter, select the **Output current date/time (UTC
Julian date)** check box.

**Data Types:** `double`

## Parameters

### Main

### **Propagation method** — Orbit propagation method `Kepler (unperturbed)` | `Numerical (high precision)`

Orbit propagation method, specified as:

- `Kepler (unperturbed)` — Uses a universal variable
  formulation of the Kepler problem to determine the spacecraft position and
  velocity at each time step. This method is faster than `Numerical
  (high precision)`.
- `Numerical (high precision)` — Determine the
  spacecraft position and velocity at each time step using numerical integration.
  This option models central body gravity based on the settings in the
  **Central body** tab. This method is more accurate than
  `Kepler (unperturbed)`, but slower.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `propagator` |
| **Type:** character vector |
| **Values:** `'Kepler (unperturbed)'` | `'Numerical (high precision)'` |
| **Default:** `'Kepler (unperturbed)'` |

### **Input external accelerations** — Input additional accelerations off (default) | on

To enable additional external accelerations to be included in the integration of
the spacecraft equations of motion, select this check box. Otherwise, clear this check
box.

#### Dependencies

To enable this check box, set **Propagation method** to
`Numerical (high precision)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `accelIn` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **External acceleration coordinate frame** — Frame for additional accelerations `ICRF` (default) | `Fixed-frame`

Input additional accelerations, specified as `ICRF` or
`Fixed-frame`. These accelerations are included in
integration of the spacecraft equations of motion.

#### Dependencies

To enable this parameter:

- Set **Propagation method** to `Numerical (high
  precision)`
- Select the **Input external accelerations** check
  box

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `accelFrame` |
| **Type:** character vector |
| **Values:** `'ICRF'` | `'Fixed-frame'` |
| **Default:** `'ICRF'` |

### **State vector output coordinate frame** — Port coordinate frame `ICRF` (default) | `Fixed-frame`

Coordinate frame for output ports, specified as `ICRF` or
`Fixed-frame`. These port labels are affected:

- Output port **X**
- Output port **V**

#### Dependencies

To enable this parameter, set **Propagation method** to
`Numerical (high precision)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `outportFrame` |
| **Type:** character vector |
| **Values:** `'ICRF'` | `'Fixed-frame'` |
| **Default:** `'ICRF'` |

### **Start date/time (UTC Julian date)** — Initial start time for simulation `juliandate (2020, 1, 1, 12, 0, 0)` (default) | valid scalar Julian date | valid Gregorian date including year, month, day, hours, minutes, seconds as 6-element vector

Initial start date and time of simulation, specified as a Julian or Gregorian
date. The block defines initial conditions using this value.

**Tip**

To calculate the Julian date, use the `juliandate` function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `startDate` |
| **Type:** character vector |
| **Values:** `'juliandate(2020, 1, 1, 12, 0, 0)'` | valid scalar Julian date | valid Gregorian date including year, month, day, hours, minutes, seconds as 6-element vector |
| **Default:**  `'juliandate(2020, 1, 1, 12, 0, 0)'` |

### **Output current date/time (UTC Julian date)** — Add output port tutc on (default) | off

To output the current date or time, select this check box. Otherwise, clear this
check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `dateOut` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Mass source** — Mass source `Dialog` (default) | `Port`

Mass source, specified as `Dialog` or
`Port`.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `massSrc` |
| **Type:** character vector |
| **Values:** `'Dialog'` | `'Port'` |
| **Default:** `'Dialog'` |

### **Mass** — Spacecraft mass used by atmospheric drag calculation `4.0` (default) | scalar | vector of size *numSat*

Spacecraft mass used by atmospheric drag calculation, specified as scalar or
vector of size *numSat*. *numSat* is the number of
spacecraft.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check box.
- Set the **Mass source** to
  `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `mass` |
| **Type:** character vector |
| **Values:** scalar | vector of size *numSat* |
| **Default:** `'4.0'` |

### **Action for out-of-range input** — Out-of-range block behavior `Warning` (default) | `Error` | `None`

Out-of-range block behavior, specified as follows:

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

### Orbit

Define the initial states of the space craft.

### **Initial state format** — Input method for initial states of orbit `Orbital elements` (default) | `ICRF state vector` | `Fixed-frame state vector`

Input method for initial states of orbit, specified as `Orbital
elements`, `ICRF state vector`, or
`Fixed-frame state vector`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter** `stateFormatNum` |
| **Type:** character vector |
| **Values:**  `'Orbital elements'` | `'ICRF state vector'` | `'Fixed-frame state vector'` |
| **Default:** `'Orbital elements'` |

### **Orbit Type** — Orbit classification `Keplerian` (default) | `Elliptical equatorial` | `Circular` | `Circular equatorial`

Orbit classification, specified as:

- `Keplerian` — Model elliptical orbits using six
  standard Keplerian orbital elements.
- `Elliptical equatorial` — Define an equatorial orbit,
  where inclination is 0 or 180 degrees and the right ascension of the ascending
  node is undefined.
- `Circular` — Define a circular orbit, where
  eccentricity is 0 and the argument of periapsis is undefined.
- `Circular equatorial` — Define a circular orbit,
  where eccentricity is 0 or 10 degrees. Argument of periapsis and the right
  ascension of the ascending node are undefined.

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

### **Semi-major axis** — Half of major axis of ellipse 6786000 (default) | 1D array of size *numSat*

Half of ellipsis major axis, specified as a 1D array whose size is the number of
spacecraft.

- For parabolic orbits, this block interprets this parameter as the periapsis
  radius (distance from periapsis to the focus point of orbit).
- For hyperbolic orbits, this block interprets this parameter as the distance
  from periapsis to the hyperbola center.

#### Dependencies

To enable this parameter, set **Initial state format** to
`Orbital elements`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `semiMajorAxis` |
| **Type:** character vector |
| **Values:** scalar | 1D array of size *m*, number of spacecraft |
| **Default:** `'6786000'` |

### **Eccentricity** — Deviation of orbit 0.01 (default) | scalar | value between `0` and `1`, or greater than `1` for Keplerian orbit type | 1D array of size *numSat*

Deviation of the orbit from a perfect circle, specified as a scalar or 1D array of
size that is number of spacecraft.

If **Orbit** type is set to `Keplerian`,
value can be:

- `0` for circular orbit
- Between `0` and `1` for elliptical
  orbit
- `1` for parabolic orbit
- Greater than `1` for hyperbolic orbit

#### Dependencies

To enable this parameter, set:

- **Initial state format** to `Orbital
  elements`.
- **Orbit type** to `Keplerian` or
  `Elliptical equatorial`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `eccentricity` |
| **Type:** character vector |
| **Values:** `0.01` | scalar | value between `0` and `1`, or greater than `1` for Keplerian orbit type | 1D array of size *numSat* |
| **Default:** `'0.01'` |

### **Inclination (deg)** — Tilt angle of orbital plane 50 (default) | scalar | 1D array of size *numSat* | degrees between 0 and 180 | radians between 0 and pi

Vertical tilt of the ellipse with respect to the reference plane measured at the
ascending node, specified as a scalar or 1D array of size *numSat*,
in specified units. *numSat* is the number of spacecraft.

#### Dependencies

To enable this parameter, set:

- **Initial state format** to `Orbital
  elements`
- **Orbit type** to `Keplerian` or
  `Circular inclined`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `inclination` |
| **Type:** character vector |
| **Values:** 50 | scalar | 1D array of size *numSat* | degrees between 0 and 180 | radians between 0 and pi |
| **Default:** `'50'` |

### **RAAN (deg)** — Angular distance in equatorial plane 95 (default) | scalar value between `0` and `360` | 1D array of size *numSat*

Right ascension of ascending node (RAAN), specified as a scalar value between
`0` and `360` or 1D array of size
*numSat*, in specified units. *numSat* is the
number of spacecraft. RAAN is the angular distance along the reference plane from the
ICRF *x*-axis to the location of the ascending node (the point at
which the spacecraft crosses the reference plane from south to north).

#### Dependencies

To enable this parameter, set:

- **Initial state format** to `Orbital
  elements`.
- **Orbit type** to `Keplerian` or
  `Circular inclined`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `raan` |
| **Type:** character vector |
| **Values:** `95` | scalar value between `0` and `360` | 1D array of size *m* number of spacecraft |
| **Default:** `'95'` |

### **Argument of periapsis (deg)** — Angle from spacecraft ascending node to periapsis 93 (default) | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *m*, number of spacecraft

Angle from the spacecraft ascending node to periapsis (closest point of orbit to
the central body), specified as a 1D array of size *m* that is number
of spacecraft, in specified units.

#### Dependencies

To enable this parameter, set:

- **Initial state format** to `Orbital
  elements`
- **Orbit type** to
  `Keplerian`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `argPeriapsis` |
| **Type:** character vector |
| **Values:** `'95'` | scalar value between `0` and `360` | 1D array of size *numSat* |
| **Default:** `'93'` |

### **True anomaly** — Angle between periapsis and initial position of spacecraft 203 (default) | scalar | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *numSat*

Angle between periapsis (closest point of orbit to the central body) and the
initial position of spacecraft along its orbit at **Start
date/time**, specified as a scalar or 1D array of size
*numSat*, in specified units. *numSat* is the
number of spacecraft.

#### Dependencies

To enable this parameter, set:

- **Initial state format** to `Orbital
  elements`.
- **Orbit type** to `Keplerian` or
  `Elliptical inclined`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `trueAnomaly` |
| **Type:** character vector |
| **Values:** `'203'` | scalar | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *numSat* |
| **Default:** `'203'` |

### **Argument of latitude (deg)** — Angle between ascending node and initial position of spacecraft 200 (default) | scalar | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *numSat*

Angle between the ascending node and the initial position of spacecraft along its
orbit at **Start date/time**, specified as a scalar or 3-element
vector or 1D array of size number of spacecraft, in specified units.

#### Dependencies

To enable this parameter, set:

- **Initial state format** to `Orbital
  elements`.
- **Orbit Type** to `Circular
  inclined`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `argLat` |
| **Type:** character vector |
| **Values:** `'200'` | scalar | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *numSat* |
| **Default:** `'200'` |

### **Longitude of periapsis (deg)** — Angle between ICRF *x*-axis and eccentricity vector 100 (default) | scalar | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *numSat*

Angle between the ICRF x-axis and the eccentricity vector, specified as a scalar
or 3-element vector or 1D array of size number of spacecraft, in specified
units.

#### Dependencies

To enable this parameter, set:

- **Initial state format** to `Orbital
  elements`.
- **Orbit type** to `Elliptical
  equatorial`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `lonPeriapsis` |
| **Type:** character vector |
| **Values:** 100 | scalar | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *m*, number of spacecraft |
| **Default:** `'100'` |

### **True longitude (deg)** — Angle between ICRF *x*-axis and initial position of spacecraft 150 (default) | scalar | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *numSat*

Angle between the ICRF x-axis and the initial position of spacecraft along its
orbit at **Start date/time**, specified as a scalar or 1D array of
size *numSat*, in specified units. *numSat* is the
number of spacecraft.

#### Dependencies

To enable this parameter, set:

- **Initial state format** to `Orbital
  elements`.
- **Orbit type** to `Circular
  equatorial`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `trueLon` |
| **Type:** character vector |
| **Values:** `'150'` | scalar | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *numSat* |
| **Default:** `'150'` |

### **ICRF position** — Cartesian position vector of spacecraft `[3649700.0 3308200.0 -4676600.0]` (default) | 3-element vector | | *numSat*-by-3 array

Cartesian position vector of spacecraft in ICRF coordinate system at
**Start date/time**, specified as a 3-element vector for single
spacecraft or *numSat*-by-3 array for multiple spacecraft.
*numSat* is the number of spacecraft.

#### Dependencies

To enable this parameter, set **Initial state format** to
`ICRF state vector`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `inertialPosition` |
| **Type:** character vector |
| **Values:** `[3649700.0 3308200.0 -4676600.0]` | 3-element vector for single spacecraft or 2-D array of size *m*-by-3 array of multiple spacecraft |
| **Default:** `'[3649700.0 3308200.0 -4676600.0]'` |

### **ICRF velocity** — Cartesian velocity vector of spacecraft `[-2750.8 6666.4 2573.4]` (default) | 3-element vector for single spacecraft or 2-D array of size *m*-by-3 array of multiple spacecraft

Cartesian velocity vector of spacecraft in ICRF coordinate system at
**Start date/time**, specified as a 3-element vector for single
spacecraft or 2-D array of size *m*-by-3 array of multiple
spacecraft.

#### Dependencies

To enable this parameter, set **Initial state format** to
`ICRF state vector`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `inertialVelocity` |
| **Type:** character vector |
| **Values:** `[-2750.8 6666.4 2573.4]` | 3-element vector for single spacecraft or 2-D array of size *m*-by-3 array of multiple spacecraft |
| **Default:** `'[-2750.8 6666.4 2573.4]'` |

### **Fixed-frame position** — Position vector of spacecraft [-4142689.0 -2676864.7 -4669861.6] (default) | 3-element vector for single spacecraft or 2-D array of size *m*-by-3 array of multiple spacecraft

Cartesian position vector of spacecraft in fixed-frame coordinate system at
**Start date/time**, specified as a 3-element vector for single
spacecraft or 2-D array of size *m*-by-3 array of multiple
spacecraft.

#### Dependencies

To enable this parameter, set:

- **Propagation method** to `Numerical (high
  precision)`.
- set **Initial state format** to `Fixed-frame
  state vector`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `fixedPosition` |
| **Type:** character vector |
| **Values:** `'[-4142689.0 -2676864.7 -4669861.6]'` | 3-element vector for single spacecraft or 2-D array of size *m*-by-3 array of multiple spacecraft |
| **Default:** `'[-2750.8 6666.4 2573.4]'` |

### **Fixed-frame velocity** — Velocity vector of spacecraft [1452.7 -6720.7 2568.1] (default) | 3-element vector for single spacecraft or 2-D array of size *m*-by-3 array of multiple spacecraft

Cartesian velocity vector of spacecraft in fixed-frame coordinate system at
**Start date/time**, specified as a 3-element vector for single
spacecraft or 2-D array of size *m*-by-3 array of multiple
spacecraft.

#### Dependencies

To enable this parameter, set:

- **Propagation method** to `Numerical (high
  precision)`.
- **Initial state format** to `Fixed-frame state
  vector`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `fixedVelocity` |
| **Type:** character vector |
| **Values:** `'[1452.7 -6720.7 2568.1]'` | 3-element vector for single spacecraft or 2-D array of size *m*-by-3 array of multiple spacecraft |
| **Default:** `'[1452.7 -6720.7 2568.1]'` |

### Central Body

Configure the central body environment around which the spacecraft orbits.

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

### **Gravitational potential model** — Control gravity model for central body `Spherical harmonics` when **Central body** set to `Earth`, `Moon`, `Mars`, or `Custom`, Oblate ellipsoid when **Central body** set to `Mercury`, `Venus`, `Jupiter`, `Saturn`, `Uranus`, or `Neptune` (default) | `None` | `Point-mass` | `Oblate ellipsoid (J2)`

Control the gravity model for the central body, specified as
`Spherical harmonics`,
`Point-mass`, or `Oblate ellipsoid
(J2)`.

#### Dependencies

To enable this parameter, set **Propagation method** to
`Numerical (high precision)`. Available options are based
on **Central body** settings:

| Earth, Moon, Mars, or Custom | Mercury, Venus, Jupiter, Saturn, Uranus, or Neptune |
| --- | --- |
| `None` | `None` |
| `Spherical harmonics` | `Oblate ellipsoid (J2)` |
| `Point-mass` | `Point-mass` |
| `Oblate ellipsoid (J2)` | — |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `gravityModel` when `centralBody` set to `'Earth'`, `'Moon'`, `'Mars'`, or `'Custom'` | `gravityModelnoSH` when `centralBody` set to `Mercury`, `Venus`, `Jupiter`, `Saturn`, `Uranus`, or `Neptune` |
| **Type:** character vector |
| **Values:** `'Spherical harmonics'` | `'None'` | `'Point-mass'` | `'Oblate ellipsoid (J2)'` when `centralBody` set to `'Earth'`, `'Moon'`, `'Mars'`, or `'Custom'`; `'Point-mass'` | `'Oblate ellipsoid (J2)'` when `centralBody` set to `Mercury`, `Venus`, `Jupiter`, `Saturn`, `Uranus`, or `Neptune` |
| **Default:** `'Spherical harmonics'` when `centralBody` set to `'Earth'`, `'Moon'`, `'Mars'`, or `'Custom'`; `'Oblate ellipsoid (J2)'` when `centralBody` set to `Mercury`, `Venus`, `Jupiter`, `Saturn`, `Uranus`, or `Neptune` |

### **Spherical harmonic model** — Spherical harmonic model `EGM2008` for **Central body** set to `Earth`, `LP-100K` for **Central body** set to `Moon`, `GMM2B` for **Central body** set to `Mars`, (default) | `EGM96` | `EIGEN-GL04C` | `LP-165P`

Spherical harmonic gravitational potential model, specified according to the
specified **Central body**.

#### Dependencies

To enable this parameter, set **Propagation method** to
`Numerical (high precision)`. Available options are based
on **Central body** settings:

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

### **Spherical harmonic coefficient file** — Harmonic coefficient MAT file `aerogmm2b.mat` (default) | harmonic coefficient MAT file

Harmonic coefficient MAT file that contains definitions for a custom planetary
model, specified as a character vector or string.

This file must contain:

| Variable | Description |
| --- | --- |
| *Re* | Scalar of planet equatorial radius in meters (m). |
| *GM* | Scalar of planetary gravitational parameter in meters cubed per second squared (m3/s2). |
| *degree* | Scalar of maximum degree. |
| *C* | (*degree*+1)-by-(*degree*+1) matrix containing normalized spherical harmonic coefficients matrix, *C*. |
| *S* | (*degree*+1)-by-(*degree*+1) matrix containing normalized spherical harmonic coefficients matrix, *S*. |

#### Dependencies

To enable this parameter, set:

- **Propagation method** to `Numerical (high
  precision)`.
- **Central body** to
  `Custom`.
- **Gravitational potential model** to `Spherical
  harmonics`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `shFile` |
| **Type:** character vector |
| **Values:** `'aerogmm2b.mat'` | harmonic coefficient MAT file |
| **Default:** `'aerogmm2b.mat'` |

### **Degree** — Degree of harmonic model `120` (default) | scalar | maximum of 2159

Degree of harmonic model, specified as a double scalar:

| Planet Model | Recommended Degree | Maximum Degree |
| --- | --- | --- |
| `EGM2008` | 120 | 2159 |
| `EGM96` | 70 | 360 |
| `LP100K` | 60 | 100 |
| `LP165P` | 60 | 165 |
| `GMM2B` | 60 | 80 |
| `EIGENGL04C` | 70 | 360 |
| `Custom` | — | Maximum degree is extracted from the spherical harmonic coefficient file. |

#### Dependencies

To enable this parameter, set:

- **Propagation method** to `Numerical (high
  precision)`.
- **Central body** to `Earth`,
  `Moon`, `Mars`, or
  `Custom`.
- **Gravitational potential model** to `Spherical harmonics`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `shDegree` |
| **Type:** character vector |
| **Values:** `'80'` | scalar |
| **Default:** `'80'` |

### **Use Earth orientation parameters (EOPs)** — Use Earth orientation parameters on (default) | off

Select this check box to use Earth orientation parameters for the transformation
between the ICRF and fixed-frame coordinate systems. Otherwise, clear this check
box.

#### Dependencies

To enable this parameter, set:

- **Propagation method** to `Numerical (high
  precision)`.
- **Central body** to
  `Earth`.

Additionally, it must satisfy one of these criteria:

- **Gravitational potential model** is set to either
  `Spherical harmonics` or `Oblate
  ellipsoid (J2)`.
- **External acceleration coordinate frame** is set to
  `Fixed-frame`.
- **State vector output coordinate frame** is set to
  `Fixed-frame`.

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

- Select the **Use Earth orientation parameters (EOPs)** to
  check box.
- Set **Propagation method** to `Numerical (high
  precision)`.
- Set **Central body** to
  `Earth`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `eopFile` |
| **Type:** character vector |
| **Values:** `'aeroiersdata.mat'` | `MAT file` |
| **Default:** `'aeroiersdata.mat'` |

### **Input Moon libration angles** — Moon libration angle rate off (default) | on

To specify libration angles (φ θ ψ) for Moon orientation, select this check
box.

#### Dependencies

To enable this parameter, set:

- **Propagation method** to `Numerical (high
  precision)`.
- **Central body** to `Moon`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `useMoonLib` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Output quaternion (ICRF to Fixed-frame)** — Add output transformation quaternion port off (default) | on

To add output transformation quaternion port for the quaternion transformation
from the ICRF to the Fixed-frame coordinate system, select this check box.

#### Dependencies

To enable this check box, set **Propagation method** to
`Numerical (high precision)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `outputTransform` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Central body spin axis source** — Central body spin source `Port` (default) | `Dialog`

Central body spin axis, specified as `Port` or
`Dialog`. The block uses the spin axis to calculate the
transformation from the ICRF to the fixed-frame coordinate system for the custom
central body.

#### Dependencies

To enable this parameter, set:

- **Propagation method** to `Numerical (high
  precision)`.
- **Central body** to
  `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `cbPoleSrc` |
| **Type:** character vector |
| **Values:** `'Port'` | `'Dialog'` |
| **Default:** `'Port'` |

### **Spin axis right ascension (RA) at J2000 (deg)** — Right ascension of central body spin axis at J2000 `317.68143` (default) | double scalar

Right ascension of central body spin axis at J2000 (2451545.0 JD, 2000 Jan 1
12:00:00 TT), specified as a double scalar.

#### Dependencies

To enable this parameter, set:

- **Propagation method** to `Numerical (high
  precision)`.
- **Central body** to
  `Custom`.
- **Central body spin axis source** to
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

#### Dependencies

To enable this parameter, set:

- **Propagation method** to `Numerical (high
  precision)`.
- **Central body** to
  `Custom`.
- **Central body spin axis source** to
  `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `cbRARate` |
| **Type:** character vector |
| **Values:** `'-0.1061'` | double scalar |
| **Default:** `'-0.1061'` |

### **Spin axis declination (Dec) at J2000 (deg)** — Declination of central body spin axis at J2000 `52.88650` (default) | double scalar

Declination of the central body spin axis at J2000 (2451545.0 JD, 2000 Jan 1
12:00:00 TT), specified as a double scalar.

#### Dependencies

To enable this parameter, set:

- **Propagation method** to `Numerical (high
  precision)`.
- **Central body** to
  `Custom`.
- **Central body spin axis source** to
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

#### Dependencies

To enable this parameter, set:

- **Propagation method** to `Numerical (high
  precision)`.
- **Central body** to
  `Custom`.
- **Central body spin axis source** to
  `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `cbDecRate` |
| **Type:** character vector |
| **Values:** `'-0.0609'` | double scalar |
| **Default:** `'-0.0609'` |

### **Initial rotation angle at J2000 (deg)** — Rotation angle of central body *x*-axis `176.630` (default) | double scalar

Rotation angle of the central body x axis with respect to the ICRF
*x*-axis at J2000 (2451545.0 JD, 2000 Jan 1 12:00:00 TT), specified
as a double scalar, in specified angle units.

#### Dependencies

To enable this parameter, set:

- **Propagation method** to `Numerical (high
  precision)`.
- **Central body** to
  `Custom`.
- **Central body spin axis source** to
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
double scalar, specified angle units/day.

#### Dependencies

To enable this parameter, set:

- **Propagation method** to `Numerical (high
  precision)`.
- **Central body** to
  `Custom`.
- **Central body spin axis source** to
  `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `cbRotRate` |
| **Type:** character vector |
| **Values:** `'350.89198226'` | double scalar |
| **Default:** `'350.89198226'` |

### **Equatorial radius** — Equatorial radius `3396200` (default) | double scalar

Equatorial radius for a custom central body, specified as a double scalar.

#### Dependencies

To enable this parameter, set:

- **Propagation method** to `Numerical (high
  precision)`.
- **Gravitational potential model** to
  `None`, `Point-mass`, or
  `Oblate ellipsoid (J2)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `customR` |
| **Type:** character vector |
| **Values:** `'3396200'` | double scalar |
| **Default:** `'3396200'` |

### **Flattening** — Flattening of planet `0.00589` (default) | double scalar

Flattening of planet for custom central body, specified as a double scalar.

#### Dependencies

To enable this parameter, set:

- **Central body** to
  `Custom`.
- **Gravitational potential model** to
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

#### Dependencies

To enable this parameter, set:

- **Central body** to
  `Custom`.
- **Gravitational potential model** to
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

#### Dependencies

To enable this parameter, set:

- **Propagation method** to `Numerical (high
  precision)`.
- **Central body** to
  `Custom`.
- **Gravitational potential model** to `Oblate
  ellipsoid (J2)`.

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

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
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

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check
  box.

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

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check
  box.
- Set the **Atmospheric density source** parameter
  to `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `atmosModel` |
| **Type:** character vector |
| **Values:** `'NRLMSISE-00'` |
| **Default:** `'NRLMSISE-00'` |

### **Flux source** — Source of space weather data `Dialog` (default) | `Port`

Source for historical and predicted flux and geomagnetic indices used by
atmospheric density calculation, specified as `Dialog`
or `Port`.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check
  box.
- Set the **Atmospheric density source** parameter
  to `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `fluxSrc` |
| **Type:** character vector |
| **Values:** `'Dialog'` | `'Port'` |
| **Default:** `'Dialog'` |

### **Space weather data file** — MAT file of space weather data `aeroSpaceWeatherData.mat` (default) | MAT file name

MAT file of space weather data. This file is the output from the `aeroReadSpaceWeatherData` function.

Aerospace Blockset™ includes a default space weather data file,
`aeroSpaceWeatherData.mat`. To use the most recent data available,
use `aeroReadSpaceWeatherData` to generate a new MAT file, and
specify the file name for this parameter. For more information, see `aeroReadSpaceWeatherData`.

If the file is not on the MATLAB® path, specify the full pathname. The MAT file must contain these variables
from the space weather data file:

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

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check box.
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

Extrapolation method for `f107Average` and `f107Daily`
for times outside the range of the MAT file data, specified as one of these
values.

| Method | Description |
| --- | --- |
| `None - clip` | Set `f107Average` and `f107Daily` to the nearest data point available in the MAT file. |
| `Constant` | Set `f107Average` and `f107Daily` to a constant value specified by the **Magnetic index extrapolation method** parameter value. |
| `Least squares fit` | Approximate `f107Average` and `f107Daily` using a least-squares fit of the space weather data from October 1, 1957, to December 1, 2040. This method uses a trigonometric function of the form:  `a + b*cos(c*t + d*sin(e*t))`,  where:    - *a* is `128.2351780622538` - *b* is `54.3285872213434` - *c* is `0.0015460708364` - *d* is `0.2429462096495` - *e* is `0.0015563188188` - *t* is *jdCurrent* -   *jdReftime* - *jdCurrent* is the current Julian date - *jdRef* is `2436112.5` |

**Note**

For `f107Average` values, if part of the 81-day period falls
inside the MAT file range of space weather data, the Solar Flux and
Geomagnetic Index block uses the actual daily values from the
overlapping portion. To calculate the average for the nonoverlapping portion, the
block uses the clipped, constant, or least squares daily value.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check box.
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

### **F10.7 extrapolation value** — Extrapolation value to assign to `f107Average` and to calculate `f107Daily` `150.0` (default) | scalar

Extrapolation value to assign to `f107Average` and to calculate `f107Daily`, specified as a scalar.

**Tunable:** Yes

#### Dependencies

This value is assigned when:

- **F10.7 extrapolation method** is set to `Constant`.
- Time specified by the **Year**, **DOY**,
  and **UT (sec)** ports is outside the range of the data in
  the MAT file.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `F107ExtrapValue` |
| **Type**: character vector |
| **Values**: `'150.0'` | scalar |
| **Default**: `'150.0'` |

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check box.
- Set the **Atmospheric density source** parameter to
  `Dialog`.
- Set **Atmospheric model** to
  `NRLMSISE-00`.
- Set **F10.7 extrapolation method** to
  `Constant`.

### **Magnetic index extrapolation method** — Extrapolation method for magnetic index information `None - clip` (default) | `Constant` | `IGRF`

Extrapolation method for magnetic index information values for times outside the range
of the MAT file data, specified as one of these values.

| Method | Description |
| --- | --- |
| `None - clip` | Set elements of magnetic index information to the nearest data point available in the MAT file. |
| `Constant` | Set elements of magnetic index information to a constant value specified by the **Magnetic index extrapolation method** parameter.  The elements of magnetic index for times outside this range are based on clipped values of the horizontal magnetic field strength at these time limits. |
| `IGRF` | Calculate the elements of magnetic index information using the International Geomagnetic Reference Field. Because this model is defined for times between January 1, 1900, 12:00 AM UTC and January 1, 2025, 12:00 AM UTC, the predictions for times outside this range are clipped to values at these time limits. |

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check box.
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

### **Magnetic index extrapolation value** — Extrapolation value used to calculate magnetic index elements `4.0` (default) | scalar

Extrapolation value used to calculate magnetic index elements, specified as a scalar.

**Tunable:** Yes

#### Dependencies

This parameter is enabled when **Magnetic index extrapolation method** is set to `Constant`.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check box.
- Set the **Atmospheric density source** parameter to
  `Dialog`.
- Set **Atmospheric model** to
  `NRLMSISE-00`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MagneticIndexExtrapValue` |
| **Type**: character vector |
| **Values**: `'4.0'` | scalar |
| **Default**: `'4.0'` |

### **Flags source** — Variation flag source `Dialog` (default) | `Port`

Variation flag source, specified as `Dialog` or
`Port`.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check
  box.
- Set the **Atmospheric density source** parameter
  to `Dialog`.
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

Variation flags, specified as an array of 23 (`ones(1,23)`).
You can specify one of the following values for a field. The default value for
each field is `1`.

- 0.0 — Removes the effect on the output.
- 1.0 — Applies the main and the cross-term effects of that value on
  the output.
- 2.0 — Applies only the cross-term effect of that value on the
  output.

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

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check
  box.
- Set the **Flags source** to
  `Dialog`.
- Set the **Atmospheric density source** parameter
  to `Dialog`.
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

To include anomalous oxygen in density calculations, select this check
box.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check
  box.
- Set the **Atmospheric density source** parameter
  to `Dialog`.
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

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check
  box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `dragCoeffSrc` |
| **Type:** character vector |
| **Values:** `'Dialog'` | `'Source'` |
| **Default:** `'Dialog'` |

### **Drag coefficient** — Spacecraft coefficient of drag 2.179 (default) | scalar | vector of size *numSat*

Spacecraft coefficient of drag used by atmospheric drag calculation, specified
as a scalar or as a vector of size *numSat*.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check
  box.
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

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check
  box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `dragAreaSrc` |
| **Type:** character vector |
| **Values:** `'Dialog'` | `'Source'` |
| **Default:** `'Dialog'` |

### **Drag area** — Area to compute acceleration due to atmospheric drag 1.0 (default) | scalar | vector of size *numSat*

Area to compute acceleration due to atmospheric drag, specified as a scalar or
as a vector of size *numSat*. This area of the spacecraft is
perpendicular to the spacecraft relative velocity.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check
  box.
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

Select one of these ephemerides models defined by the Jet Propulsion Laboratory. The block
uses ephemeris data to calculate relative celestial positions required for third body
point mass gravity and solar radiation pressure.

| **Ephemeris Model** | Description |
| --- | --- |
| `DE405` | Released in 1998. This ephemeris takes into account the Julian date range 2305424.50 (December 9, 1599) to 2525008.50 (February 20, 2201).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 1.0, adopted in 1998. |
| `DE421` | Released in 2008. This ephemeris takes into account the Julian date range 2414992.5 (December 4, 1899) to 2469808.5 (January 2, 2050).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 1.0, adopted in 1998. |
| `DE423` | Released in 2010. This ephemeris takes into account the Julian date range 2378480.5 (December 16, 1799) to 2524624.5 (February 1, 2200).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 2.0, adopted in 2010. |
| `DE430` | Released in 2013. This ephemeris takes into account the Julian date range 2287184.5 (December 21, 1549) to 2688976.5 (January 25, 2650).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 2.0, adopted in 2010. |
| `DE432t` | Released in April 2014. This ephemeris takes into account the Julian date range 2287184.5, (December 21, 1549 ) to 2688976.5, (January 25, 2650).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 2.0, adopted in 2010. |

**Note**

This block requires that you download ephemeris data using the Add-On Explorer. To
start the Add-On Explorer, in the MATLAB Command Window, type `aeroDataPackage`. in the MATLAB desktop toolstrip, click **Add-Ons**.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.

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
  the **Ephemeris model** table.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.

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

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Select the **Limit ephemerides date range**
  parameter.

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

To enable this parameter, select the **Limit ephemerides date range** check box.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Limit ephemerides date range** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `endDate` |
| **Type**: character vector |
| **Values**: `'juliandate(2050, 1, 1)'` | Julian format date |
| **Default**: `'juliandate(2050, 1, 1)'` |

### **Include third body gravity** — Acceleration due to third body gravity `off` (default) | `on`

To include acceleration due to third body gravity in orbit propagation calculation,
select this check box. Otherwise, clear this check box.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `useThirdBodyGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Sun** — Include gravitational acceleration due to Sun `on` (default) | `off`

To include gravitational acceleration due to Sun, select this check box. Otherwise,
clear it. To specify the gravity model, select it from Sun gravity model.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to any value other
  than `Sun`.
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

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to any value
  other than `Sun`.
- Select the **Include third body gravity**
  parameter.
- Select the **Sun** third body gravity
  parameter.

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

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to any value other
  than `Mercury`.
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
**Mercury** third body gravity parameter is
selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to any value
  other than `Sun`.
- Select the **Include third body gravity**
  parameter.
- Select the **Mercury** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `mercuryThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Venus** — Include gravitational acceleration due to Venus `off` (default) | `on`

To include gravitational acceleration due to Venus, select this check box. Otherwise,
clear it. To specify the gravity model, select it from Venus gravity model.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to any value other
  than `Venus`.
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
**Venus** third body gravity parameter is
selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to any value
  other than `Sun`.
- Select the **Include third body gravity**
  parameter.
- Select the **Venus** parameter.

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

- Set the **Propagation method**
  parameter to `Numerical (high
  precision)`.
- Set the **Central Body** parameter to
  any value other than
  `Earth`.
- Set the **Include third body
  gravity** to
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
**Earth** third body gravity parameter is
selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`
- `Spherical harmonics`

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to any value
  other than `Earth`.
- Select the **Include third body gravity**
  parameter.
- Select the **Earth** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `earthThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` | `'Spherical harmonics'` |
| **Default:** `'Point-mass'` |

### **Moon** — Include gravitational acceleration due to Moon `on` (default) | `off`

To include gravitational acceleration due to Moon, select this check box. Otherwise,
clear it. To specify the gravity model, select it from Moon gravity model.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to any value other
  than `Moon`.
- Set the **Include third body gravity** parameter to
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

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to any value
  other than `Moon`.
- Select the **Include third body gravity**
  parameter.
- Select the **Moon** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `moonThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` | `'Spherical harmonics'` |
| **Default:** `'Point-mass'` |

### **Mars** — Include gravitational acceleration due to Mars `off` (default) | `on`

To include gravitational acceleration due to Mars, select this check box. Otherwise,
clear it. To specify the gravity model, select it from Mars gravity model.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to any value other
  than `Mars`.
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

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to any value
  other than `Mars`.
- Select the **Include third body gravity**
  parameter.
- Select the **Mars** parameter.

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

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to any value other
  than `Jupiter`.
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
**Jupiter** third body gravity parameter is
selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to any value
  other than `Jupiter`.
- Select the **Include third body gravity**
  parameter.
- Select the **Jupiter** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `jupiterThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Saturn** — Include gravitational acceleration due to Saturn `off` (default) | `on`

To include gravitational acceleration due to Saturn, select this check box. Otherwise,
clear it. To specify the gravity model, select it from Saturn gravity model.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to any value other
  than `Saturn`.
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
**Saturn** third body gravity parameter is
selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to any value
  other than `Saturn`.
- Select the **Include third body gravity**
  parameter.
- Select the **Saturn** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `saturnThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Uranus** — Include gravitational acceleration due to Uranus `off` (default) | `on`

To include gravitational acceleration due to Uranus, select this check box. Otherwise,
clear it. To specify the gravity model, select it from Uranus gravity model.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to any value other
  than `Uranus`.
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
**Uranus** third body gravity parameter is
selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to any value
  other than `Uranus`.
- Select the **Include third body gravity**
  parameter.
- Select the **Uranus** parameter.

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

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to any value other
  than `Neptune`.
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
**Neptune** third body gravity parameter is
selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to any value
  other than `Neptune`.
- Select the **Include third body gravity**
  parameter.
- Select the **Neptune** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `neptuneThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Pluto** — Include gravitational acceleration due to Pluto `off` (default) | `on`

To include gravitational acceleration due to Pluto, select this check box. Otherwise,
clear it. To specify the gravity model, select it from Pluto gravity model.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Include third body gravity** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `includePlutoGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Pluto gravity model** — Pluto gravity model `Point-mass` (default) | `Oblate ellipsoid (J2)`

Select a gravitational potential model from the list to use when
**Pluto** third body gravity parameter is
selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Select the **Include third body gravity**
  parameter.
- Select the **Pluto** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `plutoThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Custom** — Include gravitational acceleration due to custom planet `off` (default) | `on`

To include gravitational acceleration due to a custom planet, select this check box.
Otherwise, clear it. To specify the gravity model, select it from Custom gravity model.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Include third body gravity** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `includeCustomGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Custom gravity model** — Custom gravity model `Point-mass` (default) | `Oblate ellipsoid (J2)` | `Spherical harmonics`

Select a gravitational potential model from the list to use when
**Custom** third body gravity parameter is
selected.

- `Point-mass`
- `Oblate ellipsoid (J2)`
- `Spherical harmonics`

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to any value
  other than `Sun`.
- Select the **Include third body gravity**
  parameter.
- Select the **Custom** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `customThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Gravitational parameter (m^3/s^2)** — Custom gravitational acceleration `42.828314258067e12` (default) | scalar | vector of length *numCustom3rdBodies*

Custom gravitational acceleration for custom third body, specified as a scalar or as a
vector of length *numCustom3rdBodies*. *numCustom3rdBodies*
is the number of rows provided to the **R\_cb** input port. Provide more than
one value to include multiple custom bodies.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to `Numerical
  (high precision)`.
- Set the **Include third body gravity** parameter to
  `on`.
- Set the **Custom** parameter to `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `customThirdBodyMu` |
| **Type:** character vector |
| **Values**: `'42.828314258067e12'` | scalar | vector of length *numCustom3rdBodies* |
| **Default:** `'42.828314258067e12'` |

### SRP

### **Include solar radiation pressure (SRP)** — Acceleration due to solar radiation pressure `off` (default) | `on`

To include acceleration due to solar radiation pressure in orbit propagation calculation,
select this check box. Otherwise, clear the check box.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `useSRP` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Eclipse fraction source** — Source of eclipse fraction `Dialog` (default) | `Port`

Source of the eclipse fraction (fraction of solar disk visible from the spacecraft location), specified as `Dialog` or `Port`.

#### Dependencies

To enable this parameter:

- Set the **Propagation
  method** parameter to
  `Numerical (high
  precision)`.
- Set the **Include solar radiation pressure (SRP)** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `useSRP` |
| **Type**: character vector |
| **Values**: `'Dialog'` | `'Port'` |
| **Default**: `'Dialog'` |

### **Shadow model** — Shadow model `Dual cone` (default) | `Cylindrical`

Shadow model for eclipse calculations, specified as one of these values.

- `Cylindrical` — Fraction can be 0.0
  (Umbra) or 1.0 (Sunlight).
- `Dual cone` — Fraction can be 0.0
  (Umbra), between 0.0 and 1.0 (Penumbra or Antumbra), or 1.0
  (Sunlight).

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

Option to include Moon as a secondary occulting body in eclipse calculations
when central body is Earth.

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

To enable this check box:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Select the **Include solar radiation pressure (SRP)**
  check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `reflectivityCoeffSrc` |
| **Type**: character vector |
| **Values:** `'Dialog'` | `'Port'` |
| **Default:** `'on'` |

### **Reflectivity coefficient** — Spacecraft coefficient of reflectivity `1.8` (default) | scalar | 2D array of size *numSat* | between `[1,2]`

Spacecraft coefficient of reflectivity used by solar radiation pressure calculation,
specified as a scalar, 2D array of size *numSat*.
*numSat* is the number of spacecraft.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
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

To enable this parameter:

- Set the **Propagation
  method** parameter to
  `Numerical (high
  precision)`.
- Set the **Include solar radiation pressure (SRP)** parameter to
  `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `srpAreaSrc` |
| **Type**: character vector |
| **Values:** `'Dialog'` | `'Port'` |
| **Default:** `'Dialog'` |

### **SRP area** — Cross section area of the spacecraft seen by the Sun `1.0` (default) | scalar | 2D array of size *numSat*

Cross section area of the spacecraft seen by the Sun, specified as a
scalar or as a 2D array of size *numSat*.
*numSat* is the number of
spacecraft.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set the **Propagation
  method** parameter to
  `Numerical (high
  precision)`.
- Set the **Include solar radiation
  pressure (SRP)** parameter to
  `on`.
- Set the **SRP area source**
  parameter to
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

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Include solar radiation pressure (SRP)**
  parameter to `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `fluxPressure` |
| **Type**: character vector |
| **Values:** `4.5344321e-6` | scalar |
| **Default:** `'4.5344321e-6'` |

### Units

### **Units** — Parameter and port units `Metric (m/s)` (default) | `Metric (km/s)` | `Metric (km/h)` | `English (ft/s)` | `English (kts)`

Parameter and port units, specified as:

| Units | Distance | Velocity | Acceleration | Mass | Area | Density |
| --- | --- | --- | --- | --- | --- | --- |
| `Metric (m/s)` | meters | meters/sec | meters/sec2 | Kilograms | m2 | kg/m3, some density outputs 1/m3 |
| `Metric (km/s)` | kilometers | kilometers/sec | kilometers/sec2 | Kilograms | m2 | kg/m3, some density outputs 1/m3 |
| `Metric (km/h)` | kilometers | kilometers/hour | kilometers/hour2 | Kilograms | m2 | kg/m3, some density outputs 1/m3 |
| `English (ft/s)` | feet | feet/sec | feet/sec2 | Slugs | feet2 | lbm/ft3, some density outputs 1/ft3 |
| `English (kts)` | nautical mile | knots | knots/sec | Slugs | feet2 | lbm/ft3, some density outputs 1/ft3 |

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

**Introduced in R2020b**

### R2025a: Orbit Propagator Numerical (high precision) block supports high fidelity gravity effects for third bodies

The Orbit Propagator Numerical (high precision) block now supports higher fidelity workflows using new
third body gravity options. Use these options to more accurately model orbit propagation in
spacecraft simulations.

To access these effects, select the **Include third body gravity**
parameter on the **Third Body** tab. The **Include third body
gravity** parameter replaces the **Include third body point-mass
gravity** parameter.

Selecting **Include third body gravity** lets you configure the
gravity options for the Sun, Mercury, Venus, Moon, Earth, Mars, Jupiter, Saturn, Uranus,
Neptune, Pluto, and Custom.

### R2023b: Orbit Propagator Block Changes

The Orbit Propagator block has been updated to take into account:

- The effects of third body gravity on orbit propagation.
- Space weather data from a data file generated by the `aeroReadSpaceWeatherData` function.
- Solar radiation pressure (SRP).

## Description

Propagate orbit of one or more spacecraft using Kepler universal variable formulation

The Orbit Propagator blocks propagate the orbit of one or more spacecraft
by a propagation method. The Orbit Propagator Numerical (high precision) and
Orbit Propagator Kepler
(unperturbed) blocks are alternative configurations of the same block.

- Orbit Propagator Kepler (unperturbed) — Kepler universal variable
  formulation (quicker)
- Orbit Propagator Kepler Numerical (high precision) — More
  accurate

The size of the provided initial conditions determines the number of spacecraft being
modeled. If you supply more than one value for a parameter in the **Orbit**
tab, the block outputs a constellation of satellites. Any parameter with a single provided
value is expanded and applied to all the satellites in the constellation. For example, if you
provide a single value for all the parameters on the block except **True
anomaly**, which contains six values, the block creates a constellation of six
satellites, varying true anomaly only.

The block applies the same expansion behavior to input port **A\_icrf**
(applied acceleration). This port accepts either a single value expanded to all spacecraft
being modeled, or individual values to apply to each spacecraft.

For more information on the propagation methods the Orbit Propagator blocks
use, see Orbit Propagation Methods.

You can define initial orbital states in the **Orbit** tab as:

- A set of orbital elements
- Position and velocity state vectors in International Celestial Reference Frame (ICRF)
  or fixed-frame coordinate systems.

The block uses quaternions, which are defined using the scalar-first convention.

For more information on the coordinate systems the Orbit Propagator blocks
use, see Coordinate Systems.

### Atmospheric Drag

To help model the drag on spacecraft for high precision orbit propagation, the
Orbit Propagator Numerical (high precision) block supports drag. Atmospheric drag affects spacecraft
flying at low Earth orbit (LEO); it is less relevant further away from Earth. For the
atmospheric drag equation, see Atmospheric Drag.

### Third Body Gravity Effects

To include the effects of point-mass Third Body gravity, select which third bodies to include. These calculations require an **Ephemeris model** and data. For the third body contribution equation, see
Third Body Gravity.

### Solar Radiation Pressure

To include the effects of solar radiation pressure (SRP) on the spacecraft, provide an eclipse fraction or specify a shadow model to compute the
fraction. Consider taking solar radiation pressure into account when atmosphere drag is
negligible and pointing accuracy requirements are strict. For the solar radiation pressure
equation, see Solar Radiation Pressure.
