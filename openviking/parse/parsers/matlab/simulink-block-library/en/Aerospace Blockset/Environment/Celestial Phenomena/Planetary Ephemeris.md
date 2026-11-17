---
type: simulink-block
title: 'Planetary Ephemeris'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Celestial Phenomena'
documentation_page: 'planetaryephemeris'
documentation_source_path: 'planetaryephemeris.html'
language: en
---

# Planetary Ephemeris

## Ports
```yaml
ports:
- name: TJD
  summary: Julian date scalar | positive | between minimum and maximum Julian dates
  direction: input
  data_types: double
- name: T0JD
  summary: Fixed Julian date scalar | positive
  direction: input
  data_types: double
- name: ΔTJD
  summary: Elapsed Julian time scalar | positive
  direction: input
  data_types: double
- name: Xicrf1
  summary: Barycenter position vector
  direction: output
  data_types: double
- name: Vicrf
  summary: Velocity vector
  direction: output
  data_types: double
```

### Input

### **TJD** — Julian date scalar | positive | between minimum and maximum Julian dates

Julian date, specified as a positive scalar between minimum and maximum Julian dates.

Specify the Julian dates in Barycentric Dynamical Time (TDB).

See the **Ephemeris model** parameter for the minimum
and maximum Julian dates.

#### Dependencies

This port displays if the **Epoch** parameter is
set to `Julian date`.

**Data Types:** `double`

### **T0JD** — Fixed Julian date scalar | positive

Fixed Julian date for a specific epoch that is the most recent
midnight at or before the interpolation epoch, specified as a positive
scalar. The sum of *T0JD* and
*ΔTJD* must fall between
the minimum and maximum Julian date.

Specify the Julian dates in Barycentric Dynamical Time (TDB).

See the **Ephemeris model** parameter for the
minimum and maximum Julian dates.

#### Dependencies

This port displays if the **Epoch** parameter is
set to `T0 and elapsed Julian time`.

**Data Types:** `double`

### **ΔTJD** — Elapsed Julian time scalar | positive

Elapsed Julian time between the fixed Julian date and the ephemeris
time, specified as a positive scalar. The sum of
*T0JD* and
*ΔTJD* must fall between
the minimum and maximum Julian date.

See the **Ephemeris model** parameter for the
minimum and maximum Julian dates.

#### Dependencies

This port displays if the **Epoch** parameter is
set to `T0 and elapsed Julian time`.

**Data Types:** `double`
### Output

### **Xicrf1** — Barycenter position vector

Barycenter position (*X*icrf1)
of the **Target** object relative to the barycenter of
the **Center** object, output as a vector, in km or
astronomical units (AU).

**Tip**

This block outputs the barycenter position in International
Celestial Reference Frame (ICRF) coordinates. To convert these
coordinates to Earth-centered Earth-fixed (ECEF), use the Direction Cosine Matrix ECI
to ECEF block.

**Data Types:** `double`

### **Vicrf** — Velocity vector

Velocity (*V*icrf) of the
barycenter of the **Target** object relative to the
barycenter of the **Center** object, specified as a
vector, in km/s or astronomical units (AU)/day.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Units
  summary: Output units km,km/s (default) | AU,AU/day
  group: ''
  block_parameter: units
  type: character vector
  values: m,m/s | km,km/s | AU,AU/day
  default: '''km,km/s'''
- name: Epoch
  summary: Epoch Julian date (default) | T0 and elapsed Julian time
  group: ''
  block_parameter: epochFormat
  type: character vector
  values: Julian date | T0 and elapsed Julian time
  default: '''Julian date'''
- name: Ephemeris model
  summary: Ephemeris model DE405 (default) | DE421 | DE423 | DE430 | DE432t
  group: ''
  block_parameter: ephemerisModel
  type: character vector
  values: DE405 | DE421 | DE423 | DE430
  default: '''DE405'''
- name: Ephemeris model
  summary: Ephemeris model DE405 (default) | DE421 | DE423 | DE430 | DE432t
  group: ''
  block_parameter: ephemerisModel
  type: character vector
  values: DE405 | DE421 | DE423 | DE430
  default: '''DE405'''
- name: Center
  summary: Center body Sun (default) | Mercury | Venus | Earth | Moon | Mars | Jupiter | Saturn | Uranus | Neptune | Pluto
    | Solar system barycenter | Earth-Moon barycenter
  group: ''
  block_parameter: center
  type: character vector
  values: Sun | Mercury | Venus | Earth | Moon | Mars | Jupiter | Saturn | Uranus | Neptune | Pluto | Solar system barycenter
    | Earth-Moon barycenter
  default: '''Sun'''
- name: Target
  summary: Target body Sun (default) | Mercury | Venus | Earth | Moon | Mars | Jupiter | Saturn | Uranus | Neptune | Pluto
    | Solar system barycenter | Earth-Moon barycenter
  group: ''
  block_parameter: target
  type: character vector
  values: Sun | Mercury | Venus | Earth | Moon | Mars | Jupiter | Saturn | Uranus | Neptune | Pluto | Solar system barycenter
    | Earth-Moon barycenter
  default: '''Moon'''
- name: Limit ephemerides date range
  summary: Option to enable start and end of range of ephemeris data off (default) | on
  group: ''
  block_parameter: useDateRange
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
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
  summary: Out-of-range block behavior None (default) | Warning | Error
  group: ''
  block_parameter: action
  type: character vector
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''Warning'''
- name: Calculate velocity
  summary: Calculate rate of target barycenter on (default) | off
  group: ''
  block_parameter: outputVelocity
  type: character vector
  values: '''off'' | ''on'' |'
  default: '''on'''
```

### **Units** — Output units `km,km/s` (default) | `AU,AU/day`

Output units, specified as `km,km/s` or
`AU,AU/day`.

| Units | Position | Velocity |
| --- | --- | --- |
| `m,m/s` | m | m/s |
| `km,km/s` | km | km/s |
| `Au,AU/day` | astronomical units (AU) | AU/day |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `m,m/s` | `km,km/s` | `AU,AU/day` |
| **Default**: `'km,km/s'` |

### **Epoch** — Epoch `Julian date` (default) | `T0 and elapsed Julian time`

Epoch, specified as:

- `Julian date`

  Julian date to implement the position and velocity of the
  **Target** object.. When this option is
  selected, the block has one input port,
  *TJD*.
- `T0 and elapsed Julian time`

  Julian date, specified by two block inputs:

  - Fixed Julian date representing a starting epoch.
  - Elapsed Julian time between the fixed Julian date
    (*T0JD*) and
    the desired model simulation time. The sum of
    *T0JD* and
    Δ*TJD* must
    fall between the minimum and maximum Julian date.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `epochFormat` |
| **Type**: character vector |
| **Values**: `Julian date` | `T0 and elapsed Julian time` |
| **Default**: `'Julian date'` |

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
start the Add-On Explorer, in the MATLAB® Command Window, type `aeroDataPackage`. in the MATLAB desktop toolstrip, click **Add-Ons**.

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
start the Add-On Explorer, in the MATLAB Command Window, type `aeroDataPackage`. In the MATLAB desktop toolstrip, click **Add-Ons**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ephemerisModel` |
| **Type**: character vector |
| **Values**: `DE405` | `DE421` | `DE423` | `DE430` |
| **Default**: `'DE405'` |

### **Center** — Center body `Sun` (default) | `Mercury` | `Venus` | `Earth` | `Moon` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Pluto` | `Solar system barycenter` | `Earth-Moon barycenter`

Center body (astronomical object) or reference body, specified as a point
of reference for the **Target** barycenter position and
velocity measurement.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `center` |
| **Type**: character vector |
| **Values**: `Sun` | `Mercury` | `Venus` | `Earth` | `Moon` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Pluto` | `Solar system barycenter` | `Earth-Moon barycenter` |
| **Default**: `'Sun'` |

### **Target** — Target body `Sun` (default) | `Mercury` | `Venus` | `Earth` | `Moon` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Pluto` | `Solar system barycenter` | `Earth-Moon barycenter`

Target body (astronomical object) or reference body, specified as a point
of reference for the barycenter position and velocity measurement.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `target` |
| **Type**: character vector |
| **Values**: `Sun` | `Mercury` | `Venus` | `Earth` | `Moon` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Pluto` | `Solar system barycenter` | `Earth-Moon barycenter` |
| **Default**: `'Moon'` |

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

### **Action for out-of-range input** — Out-of-range block behavior `None` (default) | `Warning` | `Error`

Out-of-range block behavior, specified as:

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

### **Calculate velocity** — Calculate rate of target barycenter `on` (default) | `off`

Select this check box to calculate the velocity of the
**Target** barycenter relative to the
**Center** barycenter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `outputVelocity` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` | |
| **Default**: `'on'` |
## Libraries

Aerospace Blockset / Environment / Celestial Phenomena

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013a**

### R2023a: Planetary Ephemeris Block Controls Range of Ephemeris Data

You can now control the range of ephemeris data for the Planetary Ephemeris using these new
parameters:

- **Limit ephemerides date range** — Select this check box
  to enable the start and end of the range of ephemeris data.
- **Start data** — Enter the start date of the range of
  ephemeris data. The **Epoch** parameter affects this date
  format.
- **End data** — Enter the end date of the range of
  ephemeris data. The **Epoch** parameter affects this date
  format.

## Description

Implement position and velocity of astronomical objects

The Planetary Ephemeris block uses Chebyshev coefficients to implement the
position and velocity of the target object relative to the specified center object for a
given Julian date. The **Target** parameter specifies an astronomical
object. The block implements the ephemerides using the **Center**
parameter for an astronomical object as the reference.

The block uses the Chebyshev coefficients that the NASA Jet Propulsion Laboratory provides.

**Tip**

For `TJD`, Julian date input for the block:

- Calculate the date using the Julian Date Conversion
  block or the Aerospace Toolbox
  `juliandate`
  function.
- Calculate the Julian date using some other means and input it using
  the Constant block.

This block implements the position and velocity using the International Celestial Reference
Frame. If you require the planetary ephemeris position value relative to Earth in
Earth-fixed (ECEF) coordinates, use the Direction Cosine Matrix ECI to ECEF block.
