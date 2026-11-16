---
type: simulink-block
title: 'Line of Sight Access'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Spacecraft Simulation'
documentation_page: 'lineofsightaccess'
documentation_source_path: 'lineofsightaccess.html'
language: en
---

# Line of Sight Access

## Ports

### Input

### **TJD** — Julian date scalar

Julian date specified as a scalar in UTC (Universal Coordinated Time).

#### Dependencies

To enable this port, set **Time source** to `Port
(Julian date)`.

**Data Types:** `double`

### **T0JD** — Julian date epoch scalar

Julian date epoch from which to base elapsed Julian time, specified as a scalar in
UTC (Universal Coordinated Time).

#### Dependencies

To enable this port, set **Time source** to `Port
(T0 and elapsed Julian time)`.

**Data Types:** `double`

### **ΔTJD** — Elapsed Julian time with respect to T0JD scalar

Elapsed Julian time with respect to **ΔT**JD,
specified as a scalar elapsed time in UTC (Universal Coordinated Time).

#### Dependencies

To enable this port, set **Time source** to `Port
(Julian date)`.

**Data Types:** `double`

### **Src *`position`*** — Source position 3-element vector | 4-element vector | *M*-by-3 array | *M*-by-4 array

Source position (such as that of the spacecraft) with respect to the source
central body, specified as a 3-element vector or *M*-by-3 array.
*`position`* can be
**Xicrf**,
**Xff**, or **LLA**,
depending on the **Position coordinate frame** setting on the
**Source** tab.

#### Dependencies

When you specify the source position as an *M*-by-3 array, you
must also specify the target position as an *M*-by-3 array.

**Data Types:** `double`

### **Src *`attitude`*** — Source attitude 3-element vector | *M*-by-3 array

Source attitude defined as a rotation from the **Attitude reference
coordinate frame** parameter on the **Source** tab to the
body frame as the current time step, specified as one of these values:

- 4-element vector — **Attitude representation** set to
  `Quaternion`.
- 3-element vector — **Attitude representation** set to
  `Euler angles`.

*`attitude`* can be **q** or
**[R1, R2, R3]**, depending on the **Attitude
representation** setting on the **Source** tab.

#### Dependencies

- To enable this port, select the **Use field of view (FOV)**
  parameter on the **Source** tab.
- When you specify the source attitude as an *M*-by-3 array,
  you must also specify the target attitude as an *M*-by-3
  array.

**Data Types:** `double`

### **Src FOV *`orientation`*** — Source field of view orientation 4-element vector | 3-element vector

Source field of view orientation, defined as a rotation from the body frame to the
sensor frame, specified as one of these values:

- 4-element vector — **Attitude representation** set to
  `Quaternion`.
- 3-element vector — **Attitude representation** set to
  `Euler angles`.

*`orientation`* can be **q** or
**[R1, R2, R3]**, depending on the **Attitude
representation** setting on the **Source** tab.

#### Dependencies

To enable this port,

- Select the **Use field of view (FOV)** parameter on the
  **Source** tab.
- Set the **Source FOV orientation source**to
  `Port`.

When you specify the source FOV orientation as an *M*-by-3
array, you must also specify the target FOV orientation as an
*M*-by-3 array.

### **Tgt *`position`*** — Target position 3-element vector | *M*-by-3 array

One or more target positions, specified as a 3-element vector or
*M*-by-3 array. *`position`* can be
**Xicrf**,
**Xff**, or **LLA**,
depending on the **Position coordinate frame** setting on the
**Source** tab.

#### Dependencies

When you specify the source position as an *M*-by-3 array, you
must also specify the target position as an *M*-by-3 array. However
if source position is a 3-element vector, target position can have any number of
rows (*M*-by-3).

**Data Types:** `double`

### **Tgt *`attitude`*** — Target attitude 3-element vector | *M*-by-3 array

One or more target attitude, specified as a 3-element vector or
*M*-by-3 array. *`attitude`* can be
**q** or **[R1, R2, R3]**, depending on the
**Attitude representation** setting on the
**Source** tab.

#### Dependencies

When you specify the source attitude as an *M*-by-3 array, you
must also specify the target attitude as an *M*-by-3 array.

**Data Types:** `double`

### **Tgt FOV *`orientation`*** — Target field of view orientation 4-element vector | 3-element vector

Target field of view orientation, defined as a rotation from the body frame to the
sensor frame, specified as one of these:

- 4-element vector — **Attitude representation** set to
  `Quaternion`.
- 3-element vector — **Attitude representation** set to
  `Euler angles`.

*`orientation`* can be **q** or
**[R1, R2, R3]**, depending on the **Attitude
representation** setting on the **Source** tab.

#### Dependencies

To enable this port,

- Select the **Use field of view (FOV)** parameter on the
  **Target** tab.
- Set the **Source FOV orientation source**to
  `Port`.

When you specify the source attitude as an *M*-by-3 array, you
must also specify the target central body as an *M*-by-3
array.

### **Rssbary,cb** — Custom central body position 3-by-1 array

Custom central body position with respect to the solar system barycenter, in the
ICRF coordinate frame. **cb** can be
**cb**srcor
**cb**tgt depending on whether
**Central body** on the **Source** or
**Target** tab is set to `Custom`.

#### Dependencies

To enable this port on the **Source** or
**Target** tab, set **Central body** to
`Custom`.

**Data Types:** `double`

### **φθψ** — Moon libration angles 3-element vector

Moon libration angles for transformation between the International Celestial
Reference Frame (ICRF) and Moon-centric fixed frame, specified as a 3-element vector.
To get these values, use the Moon Libration block.

**Note**

The fixed frame used by this block when a **Central body** on
the **Source** or **Target** tab is set to
`Moon` is the mean Earth/pole axis (ME) system. For more
information, see Algorithms.

#### Dependencies

To enable this port:

- On the **Source** or **Target** tab,
  set **Central body** to `Moon`.
- Select the **Input Moon libration angles**
  parameter.

**Data Types:** `double`
### Output

### **Access** — Total combined line of sight access status `0` (false) | `1` (true)

Total combined line of sight access status for all enabled obstructions or
constraints.

- `0` (false) — No line of sight.
- `1` (true) — Established line of sight.

#### Dependencies

- To display this port as **Access**, clear the **Output
  access status for each occulting body** parameter.
- To display this port as **Access**total,
  select the **Output access status for each occulting body**
  parameter.

**Data Types:** `Boolean`

### **AccesssourceCB** — Line of sight access status for source central body `0` (false) | `1` (true)

Status of line of sight access from source to target for only the source central
body. This status is `1` (true) if line of sight access between the
source and target is not blocked by the source central body. *source*
depends on the **Central body** option set on the
**Source** tab.

- `0` (false) — No line of sight.
- `1` (true) — Established line of sight.

#### Dependencies

To enable this port, select the **Output access status for each
occulting body** parameter.

**Data Types:** `Boolean`

### **AccessEarth/Moon** — Line of sight access status for Earth or Moon `0` (false) | `1` (true)

Line of sight access status from source to target for the Earth or Moon when
either is enabled for the source central body or target central body. This status is 1
(true) if the Earth or Moon does not block the line of sight access between the source
and target.

- `1` (true) — If the Earth or Moon does not block the line of
  sight access between the source and target.
- `0` (false) — If the Earth or Moon blocks the line of sight
  access between the source and target.

#### Dependencies

To enable this port:

- Select the **Output access status for each occulting
  body** parameter.
- Select the **Include Moon** or **Include
  Earth** parameter for source or target central body.

**Data Types:** `Boolean`

### **AccesstargetCB** — Line of sight access status for target central body `0` (false) | `1` (true)

Line of sight access status from source to target for only the target central
body. This status is `1` (true) if the target central body does not
block the line of sight access between the source and target.

- `0` (false) — No line of sight.
- `1` (true) — Established line of sight.

#### Dependencies

To enable this port:

- Select the **Output access status for each occulting
  body** parameter.
- Clear the **Use same central body as Source**
  parameter.

**Data Types:** `Boolean`

### **AccessSrc FOV** — Status of line of sight access from source to target for source field of view `0` (false) | `1` (true)

Status of line of sight access from source to target for only the source field of
view (FOV). This status is `1` (true) when the target is inside of
the FOV of the source.

- `0` (false) — No line of sight.
- `1` (true) — Established line of sight.

#### Dependencies

To enable this port:

- Select the **Output access status for each occulting
  body** parameter.
- Select the **Use field of view (FOV)** parameter on the
  **Source** tab.

**Data Types:** `Boolean`

### **AccessTgt FOV** — Status of line of sight access from source to target for the target field of view `0` (false) | `1` (true)

Status of line of sight access from source to target for only the target field of
view (FOV). This status is `1` (true) when the source is inside of
the FOV of the target.

- `0` (false) — No line of sight.
- `1` (true) — Established line of sight.

#### Dependencies

To enable this port:

- Select the **Output access status for each occulting
  body** parameter.
- Select the **Use field of view (FOV)** parameter on the
  **Target** tab.

**Data Types:** `Boolean`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Units** — Parameter and port units `Metric (m)` (default) | `Metric (km)` | `English (ft)` | `English (M)`

Parameter and port units, specified as `Metric (m)`,
`Metric (km)`, `English (ft)`, or
`English (M)`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Units` |
| **Values:** | `Metric (m)` (default) | `Metric (km)` | `English (ft)` | `English (M)` |

### **Time source** — Time source method `Dialog` (default) | `Port (Julian date)` | `Port (T0 and elapsed Julian time)`

Time source method, specified as one of these values:

- `Dialog` — Block dialog box parameter
- `Port (Julian date)` —
  **T**JD port
- `Port (T0 and elapsed Julian time)` —
  **T**JD and
  **ΔT**JD ports

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `timeSource` |
| **Values:** | `Dialog` (default) | `Port (Julian date)` | `Port (T0 and elapsed Julian time)` |

### **Start date/time (JD)** — Initial start date and time for simulation `juliandate(2020, 1, 1)` (default) | valid scalar Julian date

Initial start date and time of simulation, specified as a valid scalar Julian
date. To determine the current time at each simulation time step, the block adds
elapsed simulation time to this value.

**Tip**

To calculate the Julian date, use the `juliandate` function.

#### Dependencies

To enable this parameter, set **Time source** to
`Dialog`.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `startDate` |
| **Values:** | `juliandate(2020, 1, 1)` (default) | valid scalar Julian date |

### **Access calculation type** — Method to control access type `Cumulative` (default) | `Element-wise`

Method to control how access is calculated between sources and targets.

- `Cumulative`

  - Scalar source and *M* targets — The block establishes
    access if the source can see each target (for example, **Access**
    port is `1` (true) if the `Src` can see
    `Tgt 1` and `Tgt 2`). Access status
    outputs are scalar.
  - *M* sources and *M* targets — The block
    establishes access if line of sight access exists between all corresponding
    indices of source and target (for example, **Access** is true if
    `Src 1` can see `Tgt 1` and `Src
    2` can see `Tgt 2`). Access status outputs are
    scalar.
- `Element-wise`

  - Scalar source and *M* targets — The block establishes and
    reports access individually between the source and each target (for example,
    `Access 1` element is `1` (true) if
    `Src` can see `Tgt 1` and `Access
    2` is true if `Src` can see `Tgt
    2`). Access status outputs are of size *M*.
    `Access 1` and `Access 2` are the first
    and second element of the **Access** port, respectively.
  - *M* sources and *M* targets — The block
    establishes and reports access individually for corresponding indices of
    sources and targets (for example, `Access 1` is
    `1` (true) if `Src 1` can see `Tgt
    1` and `Access 2` is `1` (true)
    if `Src 2` can see `Tgt 2`). Access status
    outputs are of size *M*. `Access 1` and
    `Access 2` are the first and second element of the
    **Access** port, respectively.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `targetType` |
| **Values:** | `Cumulative` (default) | `Element-wise` |

### **Output access status for each occulting body** — Output access status for each occulting body `off` (default) | `on`

Output access status for obstructions for the source central body, target central
body, and the Earth, the Moon, or both. By default, the block outputs only the
combined total access.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `outputIndividualAccess` |
| **Values:** | `off` (default) | `on` |

### **Ephemeris model** — Ephemeris model `DE405` (default) | `DE421` | `DE423` | `DE430` | `DE432t`

Select one of these ephemeris models defined by the Jet Propulsion Laboratory. The
block uses ephemeris data to calculate relative celestial positions of central bodies
required for line of sight access calculations.

| **Ephemeris Model** | Description |
| --- | --- |
| `DE405` | Released in 1998. This ephemeris takes into account the Julian date range 2305424.50 (December 9, 1599) to 2525008.50 (February 20, 2201).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 1.0, adopted in 1998. |
| `DE421` | Released in 2008. This ephemeris takes into account the Julian date range 2414992.5 (December 4, 1899) to 2469808.5 (January 2, 2050).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 1.0, adopted in 1998. |
| `DE423` | Released in 2010. This ephemeris takes into account the Julian date range 2378480.5 (December 16, 1799) to 2524624.5 (February 1, 2200).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 2.0, adopted in 2010. |
| `DE430` | Released in 2013. This ephemeris takes into account the Julian date range 2287184.5 (December 21, 1549) to 2688976.5 (January 25, 2650).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 2.0, adopted in 2010. |
| `DE432t` | Released in April 2014. This ephemeris takes into account the Julian date range 2287184.5, (December 21, 1549 ) to 2688976.5, (January 25, 2650).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 2.0, adopted in 2010. |

The Line of Sight Access block loads Jet Propulsion Laboratory planetary
ephemeris data when:

- The source central body differs from the target central body.
- You define the source or target custom central body with respect to the solar
  system barycenter.

**Note**

This block requires that you download ephemeris data using the Add-On Explorer.
To start the Add-On Explorer, in the MATLAB® Command Window, type `aeroDataPackage`. in the MATLAB desktop toolstrip, click **Add-Ons**.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ephemerisModel` |
| **Values:** | `DE405` (default) | `DE421` | `DE423` | `DE430` | `DE432t` |

### **Limit ephemerides date range** — Option to enable start and end of range of ephemeris data `on` (default) | `off`

Control how much data is loaded into memory during simulation and how much data is
included in generated code for the block:

- Clear this parameter to include data for the complete date range defined in
  the Ephemeris model table.
- Select this parameter to limit the loading of ephemeris data to a specified
  date range.

#### Dependencies

To enable this parameter, select the **Limit ephemerides date
range** parameter.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `useDateRange` |
| **Values:** | `on` (default) | `off` |

### **Start date (JD)** — Start date of ephemerides date range `juliandate(2020, 1, 1)` (default) | Julian date

Start date of ephemerides date range, specified as a Julian date.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ephemerisStartDate` |
| **Values:** | `juliandate(2020, 1, 1)` (default) | Julian date |

### **End date (JD)** — End date of ephemerides date range `juliandate(2035, 1, 1)` (default) | Julian date

End date of ephemerides date range, specified as a Julian date.

#### Dependencies

To enable this parameter, select the **Limit ephemerides date
range** parameter.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ephemerisEndDate` |
| **Values:** | `juliandate(2035, 1, 1)` (default) | Julian date |

### **Action for out-of-range input** — Out-of-range block behavior `Warning` (default) | `Error` | `None`

Out-of-range block behavior, specified as one of these values.

| Action | Description |
| --- | --- |
| `None` | No action. |
| `Warning` (default) | Warning in the Diagnostic Viewer. Model simulation continues. |
| `Error` | Error in the Diagnostic Viewer. Model simulation stops. |

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `action` |
| **Values:** | `Warning` (default) | `Error` | `None` |

### **Enable zero-crossing detection** — Enable zero-crossing detection `off` (default) | `on`

Select to enable zero-crossing detection, allowing Line of Sight Access to identify zero
crossings when transiting in and out of line of sight. For more information, see Zero-Crossing Detection.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `zeroCrossing` |
| **Values:** | `off` (default) | `on` |

### Source

### **Central body** — Celestial central body for source position `Earth` (default) | `Moon` | `Mercury` | `Venus` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Sun` | `Custom`

Celestial central body for source position, specified as
`Earth`, `Moon`,
`Mercury`, `Venus`,
`Mars`, `Jupiter`,
`Saturn`, `Uranus`,
`Neptune`, `Sun`, or
`Custom`.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `sourceCentralBody` |
| **Values:** | `Earth` (default) | `Moon` | `Mercury` | `Venus` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Sun` | `Custom` |

### **Include Moon** — Option to include Moon `off` (default) | `on`

Option to include Moon as a secondary occulting body in access calculations when
source central body is Earth.

#### Dependencies

To enable this parameter, set the **Source** tab
**Central body** parameter to
`Earth`.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `sourceIncludeMoon` |
| **Values:** | `off` (default) | `on` |

### **Include Earth** — Option to include Earth `off` (default) | `on`

Option to include Earth as a secondary occulting body in access calculations when
source central body is Moon.

#### Dependencies

To enable this parameter, set the **Source** tab
**Central body** parameter to
`Moon`.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `sourceIncludeEarth` |
| **Values:** | `off` (default) | `on` |

### **Position coordinate frame** — Position coordinate frame `ICRF` (default) | `Fixed-frame` | `Latitude, Longitude, Altitude`

Position coordinate frame, specified as `ICRF`,
`Fixed-frame`, or `Latitude, Longitude,
Altitude`. For more information, see Algorithms.

#### Dependencies

To enable this parameter, set the **Central body** parameter
in the **Source** tab to any option other than
`Custom`. When the central body is
`Custom`, the position coordinate frame is always
International Celestial Reference Frame (ICRF).

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `sourceFrame` |
| **Values:** | `ICRF` (default) | `Fixed-frame` | `Latitude, Longitude, Altitude` |

### **Minimum elevation angle (deg)** — Minimum elevation angle `0` (default) | double scalar | vector

Minimum elevation angle,

Minimum elevation angle to use when computing access for the source object,
specified as a double scalar or vector.

- If the elevation angle between the source and target is less than the minimum
  elevation angle, the block does not establish access. Values must be in the range
  `[–90, 90]`.
- If more than one source is provided and you specify **Minimum
  Elevation Angle** as a scalar, the block assigns the value to each
  source input.
- If more than one source is provided and you specify **Minimum
  Elevation Angle** as a vector, the vector length must be equal to the
  number source inputs provided to the block.

#### Dependencies

To enable this parameter, set the **Position coordinate
frame** parameter on the **Source** tab to
`Latitude, Longitude, Altitude`.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `sourceFrame` |
| **Values:** | `ICRF` (default) | `Fixed-frame` | `Latitude, Longitude, Altitude` |

**Data Types:** `double`

### **Input Moon libration angles** — Moon libration off (default) | on

To specify Moon libration angles (φ θ ψ) for Moon orientation, select this
parameter. Otherwise, clear this parameter.

#### Dependencies

To enable this parameter, set **Central body** on the
**Source** tab to `Moon`.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `sourceUseMoonLib` |
| **Values:** | `'off'` (default) | `'on'` |

### **Use Earth orientation parameters (EOPs)** — Option to use Earth orientation parameters on (default) | off

Select this check box to use Earth orientation parameters for the transformation
between the ICRF and fixed-frame coordinate systems. Otherwise, clear this check
box.

#### Dependencies

To enable this parameter, set **Central body** on the
**Source** tab to `Earth`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `useEOPs` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **IERS EOP data file** — Earth orientation data `aeroiersdata.mat` (default) | MAT file

Custom list of Earth orientation data, specified in a MAT file. To create this
file, see `aeroReadIERSData`.

#### Dependencies

To enable this parameter:

- Select the **Use Earth orientation parameters (EOPs)**
  parameter.
- Set **Central body** on the **Source** tab
  to `Earth`.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `sourceEOPFile` |
| **Values:** | `aeroiersdata.mat` (default) | MAT file |

### **Equatorial radius** — Custom equatorial radius `3.3962e6` (default) | double scalar

Custom equatorial radius for a custom central body, specified as a double
scalar.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Central body** on the
**Source** tab to `Custom`.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `sourceCustomR` |
| **Values:** | `3.3962e6` (default) | double scalar |

### **Use field of view (FOV)** — Option to specify field of view `off` (default) | `on`

Option to specify whether to constrain access calculation to a conical field of
view. This option simulates the behavior of a sensor or camera.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `sourceUseFOV` |
| **Values:** | `off` (default) | `on` |

### **FOV half angle (deg)** — Field of view half angle `22.5` (default) | double scalar

Field of view half angle, specified as a double scalar.

#### Dependencies

To enable this parameter, select the **Use field of view
(FOV)** parameter on the **Source** tab.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `sourceFOVHalfAngle` |
| **Values:** | `22.5` (default) | double scalar |

### **Attitude representation** — Attitude representation `Quaternion` (default) | `Euler angles`

Attitude representation for source attitude and FOV orientation, specified as
`Quaternion` or `Euler
angles`.

#### Dependencies

To enable this parameter, select the **Use field of view
(FOV)** parameter on the **Source** tab.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `sourceRotationFormat` |
| **Values:** | `Quaternion` (default) | `Euler angles` |

### **FOV orientation source** — Field of view orientation source method `Dialog` (default) | `Port`

Field of view orientation source, specified as one of these values:

- `Dialog` — Block dialog parameter.
- `Port` — **Src FOV** port

#### Dependencies

To enable this parameter, select the **Use field of view
(FOV)** parameter on the **Source** tab.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `sourceFOVOrientationSrc` |
| **Values:** | `Dialog` (default) | `Port` |

### **FOV orientation** — Field of view orientation 4-element vector | 3-element vector

Orientation of the FOV boresight with respect to the source body frame, specified
as a 4-element vector (quaternion) or 3-element vector (Euler angles).

- 4-element vector — **Attitude representation** set to
  `Quaternion`.
- 3-element vector — **Attitude representation** set to
  `Euler angles`.

#### Dependencies

To enable this parameter:

- Set **FOV orientation source** to
  `Dialog`.
- Select the **Use field of view (FOV)** parameter on the
  **Source** tab.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `sourceRotationFormat` |
| **Values:** | `Quaternion` (default) | `Euler angles` |

### **Attitude reference coordinate frame** — Attitude reference coordinate frame `ICRF` | `Fixed-frame` | `NED`

Coordinate system used for source attitude definition, specified as
`ICRF`, `Fixed-frame`, or
`NED`. *Attitudes* are the rotation
from the attitude reference coordinate frame to the body frame.

#### Dependencies

To enable this parameter, select the **Use field of view
(FOV)** parameter on the **Source** tab.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `sourceRotationFormat` |
| **Values:** | `ICRF` | `Fixed-frame` | `NED` |

### **Angle rotation order** — Angle rotation order `ZYX` (default) | `ZYX` | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

Rotation angle sequence for Euler angle attitude representation.

**Tunable:** Yes

#### Dependencies

To enable this parameter, on the **Source** tab:

- Select the **Use field of view (FOV)** parameter.
- Set the `Attitude Representation` parameter to
  `Euler Angles`.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `sourceRotationOrder` |
| **Values:** | `ZYX` (default) | `ZYX` | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX` |

### Target

### **Use same central body as Source** — Option to use same central body as specified for source body `on` (default) | `off`

Option to use same central body for target as specified for source.

The Line of Sight Access block lets you define source and target central
bodies. You cannot set the same planet for both central bodies using the
**Central body** parameter. If you want to use the same central
body for the source and target, in the **Target** tab, select the
**Use same central body as Source** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `useTargetCentralBodyForTarget` |
| **Values:** | `on` (default) | `off` |

### **Central body** — Celestial central body for target position `Earth` (default) | `Moon` | `Mercury` | `Venus` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Sun` | `Custom`

Celestial central body for target position, specified as
`Earth`, `Moon`,
`Mercury`, `Venus`,
`Mars`, `Jupiter`,
`Saturn`, `Uranus`,
`Neptune`, `Sun`, or
`Custom`.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `targetCentralBody` |
| **Values:** | `Earth` (default) | `Moon` | `Mercury` | `Venus` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Sun` | `Custom` |

### **Include Moon** — Option to include Moon `off` (default) | `on`

Option to include Moon as a secondary occulting body in access calculations when
target central body is Earth.

#### Dependencies

To enable this parameter, set the **Central body** parameter
on the **Target** tab to `Earth`.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `targetIncludeMoon` |
| **Values:** | `off` (default) | `on` |

### **Include Earth** — Option to include Earth `off` (default) | `on`

Option to include Earth as a secondary occulting body in access calculations when
target central body is Moon.

#### Dependencies

To enable this parameter, set the **Central body** parameter
on the **Target** tab to `Moon`.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `targetIncludeEarth` |
| **Values:** | `off` (default) | `on` |

### **Position coordinate frame** — Position coordinate frame `ICRF` (default) | `Fixed-frame` | `Latitude, Longitude, Altitude`

Position coordinate frame, specified as `ICRF`,
`Fixed-frame`, or `Latitude, Longitude,
Altitude`. For more information, see Algorithms.

#### Dependencies

To enable this parameter, set the **Central body** parameter
on the **Target** tab to any option other than
`Custom`. When the central body is
`Custom`, the position coordinate frame is always
International Celestial Reference Frame (ICRF).

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `targetCustomR` |
| **Values:** | `ICRF` (default) | double scalar |

### **Minimum elevation angle (deg)** — Minimum elevation angle `0` (default) | double scalar | vector

Minimum elevation angle,

Minimum elevation angle to use when computing access for the target object,
specified as a double scalar or vector.

- If the elevation angle between the source and target is less than the minimum
  elevation angle, the block does not establish access. Values must be in the range
  `[–90, 90]`.
- If more than one target is provided and you specify **Minimum
  Elevation Angle** as a scalar, the block assigns the value to each
  source input.
- If more than one target is provided and you specify **Minimum
  Elevation Angle** as a vector, the vector length must be equal to the
  number source inputs provided to the block.

#### Dependencies

To enable this parameter, set the **Position coordinate
frame** parameter on the **Target** tab to
`Latitude, Longitude, Altitude`.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `targetMinimumElevationAngle` |
| **Values:** | `0` (default) | double scalar |

**Data Types:** `double`

### **Input Moon libration angles** — Moon libration angles off (default) | on

To specify Moon libration angles (φ θ ψ) for Moon orientation, select this check
box. Otherwise, clear this check box.

#### Dependencies

To enable this parameter, set the **Central body** parameter on
the **Target** tab to `Moon`.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `targetUseMoonLib` |
| **Values:** | `'off'` (default) | `'on'` |

### **IERS EOP data file** — Earth orientation data `aeroiersdata.mat` (default) | MAT file

Custom list of Earth orientation data, specified in a MAT file. To create this
file, see `aeroReadIERSData`.

#### Dependencies

To enable this parameter, on the **Target** tab:

- Select the **Use Earth orientation parameters (EOPs)**
  parameter.
- Set **Central body** to
  `Earth`.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `targetEOPFile` |
| **Values:** | `aeroiersdata.mat` (default) | MAT file |

### **Equatorial radius** — Custom equatorial radius `3.3962e6` (default) | double scalar

Custom equatorial radius for a custom central body, specified as a double scalar.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Central body** parameter
on the **Target** tab to `Custom`.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `targetCustomR` |
| **Values:** | `3.3962e6` (default) | double scalar |

### **Use field of view (FOV)** — Option to specify field of view `off` (default) | `on`

Option to specify whether a field of view is used for targets in access
calculations.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `targetUseFOV` |
| **Values:** | `off` (default) | `on` |

### **FOV half angle (deg)** — Field of view half angle `22.5` (default) | double scalar

Field of view half angle, specified as a double scalar.

#### Dependencies

To enable this parameter, select the **Use field of view
(FOV)** parameter on the **Target** tab.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `targetFOVHalfAngle` |
| **Values:** | `22.5` (default) | double scalar |

### **Attitude representation** — Attitude representation `Quaternion` (default) | `Euler angles`

Attitude representation, specified as `Quaternion` or
`Euler angles`.

#### Dependencies

To enable this parameter, select the **Use field of view
(FOV)** parameter on the **Target** tab.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `targetRotationFormat` |
| **Values:** | `Quaternion` (default) | `Euler angles` |

### **FOV orientation source** — Field of view orientation source method `Dialog` (default) | `Port`

Field of view orientation source method, specified as one of these values:

- `Dialog` — Block dialog box parameter
- `Port` — **Tgt FOV** port

#### Dependencies

To enable this parameter, select the **Use field of view
(FOV)** parameter on the **Target** tab.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `targetFOVOrientationSrc` |
| **Values:** | `Dialog` (default) | `Port` |

### **FOV orientation** — Field of view orientation 4-element vector | 3-element vector

Orientation of the FOV boresight with respect to the target body frame, expressed
as a 4-element vector (quaternion) or 3-element vector (Euler angles).

- 4-element vector — **Attitude representation** set to
  `Quaternion`.
- 3-element vector — **Attitude representation** set to
  `Euler angles`.

#### Dependencies

To enable this parameter, select the **Use field of view
(FOV)** parameter on the **Target** tab.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `targetRotationFormat` |
| **Values:** | `Quaternion` (default) | `Euler angles` |

### **Attitude reference coordinate frame** — Attitude reference coordinate frame `ICRF` (default) | `Fixed-frame` | `NED`

Coordinate system used for target attitude definition, specified as
`ICRF`, `Fixed-frame`, or
`NED`. Attitudes are the rotation from the attitude
reference coordinate frame to the body frame.

#### Dependencies

To enable this parameter, select the **Use field of view
(FOV)** parameter on the **Target** tab.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `targetRotationFormat` |
| **Values:** | `ICRF` | `Fixed-frame` | `NED` |

### **Angle rotation order** — Angle rotation order `ZYX` (default) | `ZYX` | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

Rotation angle sequence for Euler angle attitude representation.

**Tunable:** Yes

#### Dependencies

To enable this parameter, on the **Target** tab:

- Select the **Use field of view (FOV)** parameter.
- Set the `Attitude Representation` parameter to
  `Euler Angles`.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `targetRotationOrder` |
| **Values:** | `ZYX` (default) | `ZYX` | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX` |

## Libraries

Aerospace Blockset / Spacecraft / Spacecraft Dynamics

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

### R2025a: `Line of Sight Access` block changes

The Line of Sight Access block now supports zero-crossing detection. This change
enables the block to identify when zero crossings transit in and out of line of
sight.

## Description

Determine line of sight (LOS) access between one or more source positions and one or more target positions

The Line of Sight Access block determines whether line of sight (LOS) access exists
from one or more source positions to one or more target positions at the current time
step.

### Source and Target Central Bodies

The Line of Sight Access block lets you define sources and targets with respect to
different central bodies. You cannot set the same central body for both the source and
target **Central body** parameter. If you want to use the same central
body for the source and target, in the **Target** tab, select the
**Use same central body as Source** parameter.
