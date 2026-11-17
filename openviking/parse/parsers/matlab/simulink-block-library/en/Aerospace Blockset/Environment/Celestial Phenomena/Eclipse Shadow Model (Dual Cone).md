---
type: simulink-block
title: 'Eclipse Shadow Model (Dual Cone)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Celestial Phenomena'
documentation_page: 'eclipseshadowmodeldualcone'
documentation_source_path: 'eclipseshadowmodeldualcone.html'
language: en
---

# Eclipse Shadow Model (Dual Cone)

## Ports
```yaml
ports:
- name: Xicrf
  summary: Position of spacecraft 3-element vector | *M*-by-3 array
  direction: input
  data_types: double
- name: TJD
  summary: Julian date scalar
  direction: input
  data_types: double
- name: T0JD
  summary: Julian date epoch scalar
  direction: input
  data_types: double
- name: ΔTJD
  summary: Elapsed Julian time with respect to T0JD scalar
  direction: input
  data_types: double
- name: Rssbary,cb
  summary: Custom central body position 3-by-1 array
  direction: input
  data_types: double
- name: Fraction
  summary: Fraction of visible Sun scalar | *M*-element vector
  direction: output
  data_types: double
- name: Region
  summary: Region scalar | *M*-element vector | integer
  direction: output
  data_types: int32
- name: Secondary Region
  summary: Secondary region scalar | *M*-element vector | integer
  direction: output
  data_types: int32
```

### Input

### **Xicrf** — Position of spacecraft 3-element vector | *M*-by-3 array

Position of the spacecraft with respect to ICRF coordinate system, specified as a
3-element vector or *M*-by-3 array, where *M* is the
number of spacecraft. The **Units** parameter controls the units
designation.

**Data Types:** `double`

### **TJD** — Julian date scalar

Julian date specified as a scalar.

#### Dependencies

To enable this port, set **Dialog** to `Port
(Julian date)`.

**Data Types:** `double`

### **T0JD** — Julian date epoch scalar

Julian date epoch from which to base elapsed Julian time, specified as a
scalar.

#### Dependencies

To enable this port, set **Dialog** to `Port (T0
and elapsed Julian time)`.

**Data Types:** `double`

### **ΔTJD** — Elapsed Julian time with respect to T0JD scalar

Elapsed Julian time with respect to **ΔT**JD,
specified as a scalar elapsed time.

#### Dependencies

To enable this port, set **Dialog** to `Port (T0
and elapsed Julian time)`.

**Data Types:** `double`

### **Rssbary,cb** — Custom central body position 3-by-1 array

Custom central body position with respect to the solar system barycenter, in the
ICRF coordinate frame.

#### Dependencies

To enable this port, set **Central body** to
`Custom`.

**Data Types:** `double`
### Output

### **Fraction** — Fraction of visible Sun scalar | *M*-element vector

Fraction of visible Sun (eclipse), returned as a scalar or vector of size
*M*. *M* is the number of input spacecraft.

#### Dependencies

- When the **Shadow model** parameter is set to
  `Dual cone`, the values are `0`
  (Umbra), between `0` and `1` (Penumbra or
  Antumbra), or `1` (Sunlight).
- When the **Shadow model** parameter is set to
  `Cylindrical`, the values are `0`
  (Umbra) or `1` (Sunlight).

**Data Types:** `double`

### **Region** — Region scalar | *M*-element vector | integer

Region depending on **Shadow model** value, returned as a scalar
or *M*-element vector of integers. *M* is the number
of spacecraft.

- When the **Shadow model** parameter is set to
  `Dual cone`, region can be `0`
  (Umbra), between `0` and `1` (Penumbra or
  Antumbra), or `1` (Sunlight).
- When the **Shadow model** parameter is set to
  `Cylindrical`, region can be `0`
  (Umbra) or `1` (Sunlight).

#### Dependencies

To enable this port:

- Select the **Output index of shadow region** check
  box.

**Data Types:** `int32`

### **Secondary Region** — Secondary region scalar | *M*-element vector | integer

Region depending on **Shadow model** value, returned as a scalar
or *M*-element vector of integers. *M* is the number
of spacecraft.

- When the **Shadow model** parameter is set to
  `Dual cone`, region can be `0`
  (Umbra), between `0` and `1` (Penumbra or
  Antumbra), or `1` (Sunlight).
- When the **Shadow model** parameter is set to
  `Cylindrical`, region can be `0`
  (Umbra) or `1` (Sunlight).

#### Dependencies

To enable this port, select the **Output index of shadow
region** check box and one of these settings:

- - Set **Central body** to
    `Earth`.
  - Select **Include Moon**.

or:

- - Set **Central body** to
    `Moon`.
  - Select **Include Earth**.

**Data Types:** `int32`
## Parameters
```yaml
parameters:
- name: Units
  summary: Position port units Metric (m) (default) | Metric (km) | English (ft) | English (M)
  group: ''
  block_parameter: units
  type: character vector
  values: '''Metric (m)'' | ''Metric (km)'' | ''English (ft)'' | ''English (M)'''
  default: '''Metric (m)'''
- name: Shadow model
  summary: Shadow model Dual cone (default) | Cylindrical
  group: ''
  block_parameter: shadowModel
  type: character vector
  values: '''Dual cone'' | ''Cylindrical'''
  default: '''Dual cone'''
- name: Output index of shadow region
  summary: Output index of shadow region on (default) | off
  group: ''
  block_parameter: outputShadowRegion
  type: character vector
  values: '''off'' | ''on'''
  default: '''on'''
- name: Time source
  summary: Time source method Dialog (default) | Port (Julian date) | Port (T0 and elapsed Julian time)
  group: ''
  block_parameter: timeSource
  type: character vector
  values: '''Dialog'' | ''Port (Julian date)'' | ''Port (T0 and elapsed Julian time)'''
  default: '''Dialog'''
- name: Start date/time (JD)
  summary: Initial start date and time for simulation juliandate(2020, 1, 1) (default) | valid scalar Julian date
  group: ''
  block_parameter: startDate
  type: character vector
  values: '''juliandate(2020, 1, 1)'' | valid scalar Julian date'
  default: '''juliandate(2020, 1, 1)'''
- name: Central body
  summary: Occulting celestial body for eclipse calculations Earth (default) | Moon | Mercury | Venus | Mars | Jupiter | Saturn
    | Uranus | Neptune | Custom
  group: ''
  block_parameter: centralBody
  type: character vector
  values: '''Earth'' | ''Moon'' |''Mercury'' | ''Venus'' | ''Mars'' | ''Jupiter'' | ''Saturn'' | ''Uranus'' | ''Neptune''
    | ''Custom'' |'
  default: '''Earth'''
- name: Equatorial radius
  summary: Custom central body radius 3396200 (default) | double scalar
  group: ''
  block_parameter: customR
  type: character vector
  values: '''3396200'' | double scalar'
  default: '''3396200'''
- name: Include Moon
  summary: Option to include Moon on (default) | off
  group: ''
  block_parameter: includeMoon
  type: character vector
  values: '''off'' | ''on'''
  default: '''on'''
- name: Include Earth
  summary: Option to include Earth on (default) | off
  group: ''
  block_parameter: includeEarth
  type: character vector
  values: '''off'' | ''on'''
  default: '''on'''
- name: Ephemeris model
  summary: Ephemeris model DE405 (default) | DE421 | DE423 | DE430 | DE432t
  group: ''
  block_parameter: ephemerisModel
  type: character vector
  values: DE405 | DE421 | DE423 | DE430
  default: '''DE405'''
- name: Limit ephemerides date range
  summary: Open to enable start and end of range of ephemeris data on (default) | off
  group: ''
  block_parameter: useDateRange
  type: character vector
  values: '''off'' | ''on'' |'
  default: '''on'''
- name: Start date (JD)
  summary: Start date of ephemerides date range juliandate(2020, 1, 1) (default) | Julian date
  group: ''
  block_parameter: startDate
  type: character vector
  values: '''juliandate(2020, 1, 1)'' | Julian date'
  default: '''juliandate(2020, 1, 1)'''
- name: End date (JD)
  summary: End date of ephemerides date range juliandate(2050, 1, 1) (default) | Julian date
  group: ''
  block_parameter: endDate
  type: character vector
  values: '''juliandate(2050, 1, 1)'' | Julian format date'
  default: '''juliandate(2050, 1, 1)'''
- name: Action for out-of-range input
  summary: Out-of-range block behavior Error (default) | Warning | None
  group: ''
  block_parameter: action
  type: character vector
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''Error'''
- name: Enable zero-crossing detection
  summary: Enable zero-crossing detection off (default) | on
  group: ''
  block_parameter: zeroCrossing
  type: character vector, string
  values: '''on'' | ''off'''
  default: '''off'''
```

### **Units** — Position port units `Metric (m)` (default) | `Metric (km)` | `English (ft)` | `English (M)`

Position port units, specified as one of these values:

| Units | Distance |
| --- | --- |
| `Metric (m)` | meters |
| `Metric (km)` | kilometers |
| `English (ft)` | feet |
| `English (M)` | miles |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `units` |
| **Type:** character vector |
| **Values:** `'Metric (m)'` | `'Metric (km)'` | `'English (ft)'` | `'English (M)'` |
| **Default:** `'Metric (m)'` |

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

### **Output index of shadow region** — Output index of shadow region `on` (default) | `off`

To enable the port for the index of the shadow region, select this check box.
Otherwise, clear this check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `outputShadowRegion` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'on'` |

### **Time source** — Time source method `Dialog` (default) | `Port (Julian date)` | `Port (T0 and elapsed Julian time)`

Time source method, specified as one of these values:

- `Dialog` — Block dialog parameter.
- `Port (Julian date)` —
  **T**JD port.
- `Port (T0 and elapsed Julian time)` —
  **T**JD and
  **ΔT**JD ports.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `timeSource` |
| **Type:** character vector |
| **Values:**`'Dialog'` | `'Port (Julian date)'` | `'Port (T0 and elapsed Julian time)'` |
| **Default:** `'Dialog'` |

### **Start date/time (JD)** — Initial start date and time for simulation `juliandate(2020, 1, 1)` (default) | valid scalar Julian date

Initial start date and time of simulation, specified as a valid scalar Julian date.
To determine the current time at each simulation timestep, the block adds elapsed
simulation time to this value.

**Tip**

To calculate the Julian date, use the `juliandate` function.

#### Dependencies

To enable this parameter, set **Time source** to
`Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `startDate` |
| **Type:** character vector |
| **Values:**`'juliandate(2020, 1, 1)'` | valid scalar Julian date |
| **Default:** `'juliandate(2020, 1, 1)'` |

### **Central body** — Occulting celestial body for eclipse calculations `Earth` (default) | `Moon` | `Mercury` | `Venus` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Custom`

Occulting celestial body for eclipse calculations, specified as
`Earth`, `Moon`,
`Mercury`, `Venus`,
`Mars`, `Jupiter`,
`Saturn`, `Uranus`,
`Neptune`, or `Custom`.

Position inputs are referenced with respect to the origin of the central
body.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `centralBody` |
| **Type:** character vector |
| **Values:** `'Earth'` | `'Moon'` |`'Mercury'` | `'Venus'` | `'Mars'` | `'Jupiter'` | `'Saturn'` | `'Uranus'` | `'Neptune'` | `'Custom'` | |
| **Default:** `'Earth'` |

### **Equatorial radius** — Custom central body radius `3396200` (default) | double scalar

Equatorial radius for a custom central body, specified as a double scalar in the
units specified in the **Units** parameter..

#### Dependencies

To enable this parameter, set **Central body** to
`Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `customR` |
| **Type:** character vector |
| **Values:** `'3396200'` | double scalar |
| **Default:** `'3396200'` |

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

### **Ephemeris model** — Ephemeris model `DE405` (default) | `DE421` | `DE423` | `DE430` | `DE432t`

Select one of these ephemerides models defined by the Jet Propulsion Laboratory.

| **Ephemeris Model** | Description |
| --- | --- |
| `DE405` | Released in 1998. This ephemeris takes into account the Julian date range 2305424.50 (December 9, 1599) to 2525008.50 (February 20, 2201).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 1.0, adopted in 1998. |
| `DE421` | Released in 2008. This ephemeris takes into account the Julian date range 2414992.5 (December 4, 1899) to 2469808.5 (January 2, 2050).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 1.0, adopted in 1998. |
| `DE423` | Released in 2010. This ephemeris takes into account the Julian date range 2378480.5 (December 16, 1799) to 2524624.5 (February 1, 2200).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 2.0, adopted in 2010. |
| `DE430` | Released in 2013. This ephemeris takes into account the Julian date range 2287184.5 (December 21, 1549) to 2688976.5 (January 25, 2650).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 2.0, adopted in 2010. |
| `DE432t` | Released in April 2014. This ephemeris takes into account the Julian date range 2287184.5, (December 21, 1549 ) to 2688976.5, (January 25, 2650).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 2.0, adopted in 2010. |

**Note**

This block requires that you download ephemeris data using the Add-On Explorer. To
start the Add-On Explorer, in the MATLAB® Command Window, type `aeroDataPackage`. In the MATLAB desktop toolstrip, click **Add-Ons**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ephemerisModel` |
| **Type**: character vector |
| **Values**: `DE405` | `DE421` | `DE423` | `DE430` |
| **Default**: `'DE405'` |

### **Limit ephemerides date range** — Open to enable start and end of range of ephemeris data `on` (default) | `off`

Control how much data is loaded into memory during simulation and how much data is
included in generated code for the block:

- Clear this check box to include data for the complete date range defined in
  the Ephemeris model table.
- Select this check box to limit the loading of ephemeris data to a specified
  date range.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `useDateRange` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` | |
| **Default**: `'on'` |

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

### **Action for out-of-range input** — Out-of-range block behavior `Error` (default) | `Warning` | `None`

Out-of-range block behavior, specified as one of these values:

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
| **Default**: `'Error'` |

### **Enable zero-crossing detection** — Enable zero-crossing detection `off` (default) | `on`

Select to enable zero-crossing detection, allowing Eclipse Shadow Model (Dual Cone) to identify zero crossings when transiting in and out of eclipse. For more information, see Zero-Crossing Detection.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `zeroCrossing` |
| **Type:** character vector, string |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |
## Libraries

Aerospace Blockset / Environment / Celestial Phenomena

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

### R2025a: `Eclipse Shadow Model (Dual Cone)` block changes

The Eclipse Shadow Model (Dual Cone) and Eclipse Shadow Model
(Cylindrical) blocks now support zero-crossing detection. This change enables the
blocks to identify when zero crossings transit in and out of eclipse.

## Description

Calculate fraction of solar disk visible at inertial positions

The Eclipse Shadow Model (Dual Cone) block calculates the fraction of the
solar disk that is visible from the provided inertial positions, assuming that the occulted
bodies and the Sun are spherical. The block operates with two shadow models:

Dual cone model — The block differentiates between partial, annular, and total eclipse,
which means the spacecraft can be in sunlight, penumbra, antumbra, or umbra. The eclipse is
partial in penumbra, annular in antumbra, and total in umbra. In summary:

- Umbra, no sunlight — 0
- Penumbra or Antumbra, partial sunlight — 0 to 1
- Full sunlight — 1

Cylindrical model — The block differentiates only between total eclipse (umbra) and full
sunlight. For more information, see Alternative Configurations section.

- Umbra, no sunlight — 0
- Full sunlight — 1
