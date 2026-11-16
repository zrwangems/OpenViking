---
type: simulink-block
title: 'Orbit Propagator Kepler (unperturbed)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Spacecraft Simulation'
documentation_page: 'orbitpropagatorkeplerunperturbed'
documentation_source_path: 'orbitpropagatorkeplerunperturbed.html'
language: en
---

# Orbit Propagator Kepler (unperturbed)

## Ports

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

### **Initial state format** — Input method for initial states of orbit `Orbital elements` (default) | `ICRF state vector`

Input method for initial states of orbit, specified as `Orbital
elements` or `ICRF state vector`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter** `stateFormatKep` |
| **Type:** character vector |
| **Values:**  `'Orbital elements'` | `'ICRF state vector'` |
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

### R2023b: Orbit Propagator Block Changes

The Orbit Propagator block has been updated to take into account:

- The effects of third body gravity on orbit propagation.
- Space weather data from a data file generated by the `aeroReadSpaceWeatherData` function.
- Solar radiation pressure (SRP).

## Description

Propagate orbit of one or more spacecraft using Kepler universal variable formulation

The Orbit Propagator Kepler (unperturbed) block propagates the orbit of one
or more spacecraft using the Kepler universal variable formulation. The Orbit
Propagator Kepler (unperturbed) and Orbit Propagator Numerical
(high precision) blocks are alternative configurations of the same block.

- Orbit Propagator Kepler (unperturbed) — Kepler universal variable
  formulation (quicker)
- Orbit Propagator Kepler Numerical (high precision) — More
  accurate

The Orbit Propagator Kepler (unperturbed) block does not take into account atmospheric drag, third
body gravity, or solar radiation pressure. For orbit propagations that take these effects into
account, see the Orbit Propagator Numerical
(high precision) block.

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
