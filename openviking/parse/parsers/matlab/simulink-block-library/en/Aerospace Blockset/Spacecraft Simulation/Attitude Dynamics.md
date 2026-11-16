---
type: simulink-block
title: 'Attitude Dynamics'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Spacecraft Simulation'
documentation_page: 'attitudedynamics'
documentation_source_path: 'attitudedynamics.html'
language: en
---

# Attitude Dynamics

## Ports

### Input

### **X** — Position of spacecraft 3-element vector | *numSat*-by-3 array

Position of the spacecraft with respect to the state vector coordinate frame,
specified as a 3-element vector or *numSat*-by-3 array at the current
time step. *numSat* is the number of spacecraft.

#### Dependencies

- To change the coordinate frame for this port, set the **State vector
  output coordinate frame** parameter.
- The size of the initial conditions provided in the **Mass**
  or **Attitude** tab control the port dimension.

**Data Types:** `double`

### **V** — Velocity 3-element vector | *numSat*-by-3 array

Velocity of the spacecraft with respect to the state vector coordinate frame,
specified as a 3-element vector or *numSat*-by-3 array at the current
time step. *numSat* is the number of spacecraft.

#### Dependencies

- To change the coordinate frame for this port, set the **State vector
  output coordinate frame** parameter.
- The size of the initial conditions provided in the **Mass**
  or **Attitude** tab control the port dimension.

**Data Types:** `double`

### **Mb** — External moments 3-element vector | *numSat*-by-3 array

Moment applied to the spacecraft in the body frame, specified as a 3-element
vector or *numSat*-by-3 array at the current time step.
*numSat* is the number of spacecraft.

#### Dependencies

To enable this port, select the **Input body moments** check
box.

**Data Types:** `double`

### **dm/dt** — Rate of change of mass scalar | 1D array of size *numSat*

Rate of change of mass (positive if accreted, negative if ablated) at the current
timestep, specified as a scalar or 1D array of size *numSat*.
*numSat* is the number of spacecraft.

#### Dependencies

To enable this port, set **Mass type** to `Simple
Variable`.

**Data Types:** `double`

### **m** — Spacecraft mass scalar | 1D array of size *numSat*

Spacecraft mass at the current timestep. *numSat* is the number
of spacecraft.

#### Dependencies

To enable this port, set **Mass type** to `Custom
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
- Select the **Include mass flow relative velocity** check
  box.

**Data Types:** `double`

### **φθψ** — Moon libration angles 3-element vector

Moon libration angles for transformation between the International Celestial
Reference Frame (ICRF) and Moon-centric fixed-frame using the Moon-centric Principal
Axis (PA) system, specified as a 3-element vector. To get these values, use the Moon Libration block.

**Note**

The fixed-frame used by this block when **Central body** is set
to `Moon` is the Mean Earth/pole axis (ME) system. For more
information, see Algorithms.

#### Dependencies

To enable this port:

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

- Set **Central body** to
  `Custom`.
- Set **Central body spin axis source** to
  `Port`.

**Data Types:** `double`
### Output

### **qbody2icrf** — Spacecraft attitude quaternion 4-element quaternion | *numSat*-by-4 array

Spacecraft attitude quaternion, returned as a scalar-first 4-element quaternion
rotation from the body axis to the outport frame or scalar-first
*numSat*-by-4 array at the current time step.
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

Spacecraft attitude direction cosine matrix (DCM), returned as a 3-by-3 array or
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

### **qicrf2ff** — Coordinate system transformation 4-element array

Coordinate system transformation between the ICRF and fixed-frame coordinate
system at the current timestep, returned as a 4-element array.

#### Dependencies

To enable this port, select the **Output quaternion (ICRF to
Fixed-frame)** check box.

**Data Types:** `double`

### **tutc** — Time at current time step scalar | 6-element array

Time at current time step, returned as a:

- scalar — If you specify the **Start data/time** parameter as
  a Julian date.
- 6-element array — If you specify the **Start data/time**
  parameter as a Gregorian date with six elements: year, month, day, hours, minutes,
  seconds.

This value equals the **Start date/time** parameter value plus
the elapsed simulation time.

#### Dependencies

To enable this parameter, select the **Output current date/time (UTC
Julian date)** check box.

**Data Types:** `double`

### **Fuel Status** — Fuel status scalar | *numSat*-element array

Fuel tank status at the current timestep, returned as a scalar or
*numSat*-element array:

- `1` — Tank is full.
- `0` — Tank is not full or empty.
- `-1` — Tank is empty.

*numSat* is the number of spacecraft.

#### Dependencies

To enable this port:,

- Set **Mass type** to `Simple
  Variable`.
- Select the **Output fuel tank status** check box.

**Data Types:** `double`

## Parameters

### Main

### **Input body moments** — Option to enable external moments on (default) | off

To enable external moments to be included in the integration of the spacecraft
equations of motion in the body frame, select this check box. Otherwise, clear this
check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `momentsIn` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **State vector coordinate frame** — Position and velocity state port coordinate frame `ICRF` (default) | `Fixed-frame`

Position and velocity state port coordinate frame setup, specified as
`ICRF` or `Fixed-frame`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `outportFrame` |
| **Type:** character vector |
| **Values:** `'ICRF'` | `'Fixed-frame'` |
| **Default:** `'ICRF'` |

### **Start date/time (UTC Julian date)** — Initial start time for simulation `juliandate (2020, 1, 1, 12, 0, 0)` (default) | valid scalar Julian date | valid Gregorian date

Initial start date and time of simulation, specified as a Julian or Gregorian
date. A valid Gregorian date must include the year, month, day, hours, minutes, and
seconds as a 1D or 6-element array. The block defines initial conditions using this
value.

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
| **Values:** `'juliandate(2020, 1, 1, 12, 0, 0)'` | valid scalar Julian date | valid Gregorian date |
| **Default:**  `'juliandate(2020, 1, 1, 12, 0, 0)'` |

### **Output current date/time (UTC Julian date)** — Option to add output port tutc on (default) | off

To output the current date or time, select this check box. Otherwise, clear this
check box.

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

Spacecraft empty (dry) mass, specified as a scalar or as a vector of size
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

Spacecraft full (wet) mass, specified as a scalar or as a vector of size
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
spacecraft. *numSat* is the number of spacecraft.

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
spacecraft or a 3-by-3-by-*numSat* array for multiple spacecraft.
*numSat* is the number of spacecraft.

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
spacecraft or a 3-by-3-by-*numSat* array for multiple spacecraft.
*numSat* is the number of spacecraft.

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

To enable mass flow velocity to the block, select this check box. The mass flow
velocity is the relative velocity in the body frame at which the mass is accreted or
ablated. To disable mass flow velocity to the block, clear this check box.

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
check box. Otherwise, clear this check box.

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

To enable fuel tank status, select this check box. Otherwise, clear this check
box.

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

### **Initial body attitude** — Spacecraft initial attitude `[1, 0, 0, 0]` (default) | 4-element vector | *numSat*-by-4 array | 3-by-3 array | *numSat*-by-3-by-3 array | 3-element vector | *numSat*-by-3 array

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

### **Include gravity gradient torque** — Option to enable gravity gradient torque on (default) | off

Select this check box to enable the use of the gravity gradient torque in the
block rotational dynamics equations. Otherwise, clear this check box.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `angAccelOut` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### Central Body

### **Central body** — Celestial body around which spacecraft orbits `Earth` (default) | `Moon` | `Mercury` | `Venus` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Custom`

Celestial body around which the spacecraft orbits, specified as
`Earth`, `Moon`,
`Mercury`, `Venus`,
`Mars`, `Jupiter`,
`Saturn`, `Uranus`,
`Neptune`, or `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `centralBody` |
| **Type:** character vector |
| **Values:** `'Earth'` | `'Moon'` |`'Mercury'` | `'Venus'` | `'Mars'` | `'Jupiter'` | `'Saturn'` | `'Uranus'` | `'Neptune'` | `'Custom'` | |
| **Default:** `'Earth'` |

### **Rotational rate** — Rotational rate `4.06124975e-3` (default) | scalar

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

### **Use Earth orientation parameters (EOPs)** — Option to use Earth orientation parameters on (default) | off

Select this check box to use Earth orientation parameters for the transformation
between the ICRF and fixed-frame coordinate systems. Otherwise, clear this check
box.

#### Dependencies

To enable this parameter, set **Central body** to
`Earth`.

Additionally, it must satisfy one of these criteria:

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

### **IERS EOP data file** — Earth orientation data `aeroiersdata.mat` (default) | MAT-file

Custom list of Earth orientation data, specified in a MAT-file.

#### Dependencies

To enable this parameter:

- Select the **Use Earth orientation parameters (EOPs)**
  check box.
- Set **Central body** to
  `Earth`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `eopFile` |
| **Type:** character vector |
| **Values:** `'aeroiersdata.mat'` | MAT-file |
| **Default:** `'aeroiersdata.mat'` |

### **Input Moon libration angles** — Moon libration Euler angle rate off (default) | on

To specify Euler libration angles (φ θ ψ) for Moon orientation, select this check
box. Otherwise, clear this check box.

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

To add an output transformation quaternion port for the quaternion transformation
from the ICRF to the fixed-frame coordinate system, select this check box. Otherwise,
clear this check box.

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
in specified angle units per century.

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
specified angle units per century.

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

Rotation angle of the central body *x*-axis with respect to the
ICRF *x*-axis at J2000 (2451545.0 JD, 2000 Jan 1 12:00:00 TT),
specified as a double scalar, in specified angle units.

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

Rotation rate of the central body *x*-axis with respect to the
ICRF *x*-axis (2451545.0 JD, 2000 Jan 1 12:00:00 UTC), specified as a
double scalar, in angle units per day.

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

### **Equatorial radius** — Equatorial radius `3396200` (default) | double scalar

Equatorial radius for a custom central body, specified as a double scalar.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Central Body** to
`Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `customR` |
| **Type:** character vector |
| **Values:** `'3396200'` | double scalar |
| **Default:** `'3396200'` |

### **Flattening** — Flattening of planet `0.00589` (default) | double scalar

Flattening of planet for custom central body, specified as a double scalar.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Central body** to
`Custom`.

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

To enable this parameter, set **Central body** to
`Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `customMu` |
| **Type:** character vector |
| **Values:** `'4.305e13'` | double scalar |
| **Default:** `'4.305e13'` |

### Units

### **Units** — Parameter and port units `Metric (m/s)` (default) | `Metric (km/s)` | `Metric (km/h)` | `English (ft/s)` | `English (kts)`

Parameter and port units, specified as shown in the table.

| Units | Moment | Mass | Inertia | Distance | Velocity | Acceleration |
| --- | --- | --- | --- | --- | --- | --- |
| `Metric (m/s)` | Newton-meter | Kilograms | Kilogram m2 | meters | meters/sec | meters/sec2 |
| `Metric (km/s)` | Newton-meter | Kilograms | Kilogram m2 | kilometers | kilometers/sec | kilometers/sec2 |
| `Metric (km/h)` | Newton-meter | Kilograms | Kilogram m2 | kilometers | kilometers/hour | kilometers/hour2 |
| `English (ft/s)` | Foot-pound | Slugs | Slug ft2 | feet | feet/sec | feet/sec2 |
| `English (kts)` | Foot-pound | Slugs | Slug ft2 | nautical mile | knots | knots/sec |

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

**Introduced in R2023a**

## Description

Model attitude dynamics of one or more spacecraft

The Attitude Dynamics block models rotational dynamics of spacecraft using
numerical integration. The block computes the attitude and angular velocity of one or more
spacecraft over time using provided position and velocity states. For the most accurate
results, use a variable-step solver with low tolerance settings (less than 1e-8). To trade off
accuracy for speed, use larger tolerances, depending on your mission requirements.

For more information on the coordinate systems and translational and rotation dynamics
that the Attitude Dynamics block uses, see Algorithms.
