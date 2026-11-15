---
type: simulink-block
title: 'Earth Nutation'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Celestial Phenomena'
documentation_page: 'earthnutation'
documentation_source_path: 'earthnutation.html'
language: en
---

# Earth Nutation

## Ports

### Input

### **TJD** — Julian date scalar | positive | between minimum and maximum Julian dates

Julian date, specified as a positive scalar between minimum and maximum Julian
dates.

See the **Ephemeris model** parameter for the minimum and maximum
Julian dates.

#### Dependencies

This port displays if the **Epoch** parameter is
set to `Julian date`.

**Data Types:** `double`

### **T0JD** — Fixed Julian date scalar | positive

Fixed Julian date for a specific epoch that is the most recent midnight at or before the
interpolation epoch, specified as a positive scalar. The sum of
*T0JD* and
*ΔTJD* must fall between
the minimum and maximum Julian dates.

See the **Ephemeris model** parameter for the minimum and maximum
Julian dates.

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

See the **Ephemeris model** parameter for the minimum and maximum
Julian dates.

#### Dependencies

This port displays if the **Epoch** parameter is
set to `T0 and elapsed Julian time`.

**Data Types:** `double`
### Output

### **Δψ Δε (rad)** — Earth nutation vector

Earth nutation, output as a vector of longitude (Δψ) and obliquity (Δε), in rad.

**Data Types:** `double`

### **Δψ dot Δεdot (rad/day)** — Earth nutation angular rate scalar

Earth nutation angular rate for the longitude (Δψ dot ) and
obliquity (Δε dot ), specified as a scalar in
rad/day.

#### Dependencies

This port displays if the **Calculate rates** parameter is
selected.

**Data Types:** `double`

## Parameters

### **Epoch** — Epoch `Julian date` (default) | `T0 and elapsed Julian time`

Epoch, specified as:

- `Julian date`

  Julian date to calculate the Earth nutation. When this option is
  selected, the block has one input port,
  *TJD*.
- `T0 and elapsed Julian time`

  Julian date, specified by two block inputs:

  - Fixed Julian date representing a starting epoch.
  - Elapsed Julian time between the
    *T0JD* and
    the desired model simulation time. The sum of
    *T0JD* and
    Δ*TJD* must
    fall between the minimum and maximum Julian dates.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `epochflag` |
| **Type**: character vector |
| **Values**: `Julian date` | `T0 and elapsed Julian time` |
| **Default**: `'Julian date'` |

### **Ephemeris model** — Ephemeris model `DE405` (default) | `DE421` | `DE423` | `DE430`

Select an Ephemeris model from the list defined by the Jet Propulsion Laboratory:

| **Ephemeris Model** | Description |
| --- | --- |
| `DE405` | Released in 1998. This ephemeris takes into account the Julian date range 2305424.50 (December 9, 1599) to 2525008.50 (February 20, 2201).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 1.0, adopted in 1998. |
| `DE421` | Released in 2008. This ephemeris takes into account the Julian date range 2414992.5 (December 4, 1899) to 2469808.5 (January 2, 2050).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 1.0, adopted in 1998. |
| `DE423` | Released in 2010. This ephemeris takes into account the Julian date range 2378480.5 (December 16, 1799) to 2524624.5 (February 1, 2200).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 2.0, adopted in 2010. |
| `DE430` | Released in 2013. This ephemeris takes into account the Julian date range 2287184.5 (December 21, 1549) to 2688976.5 (January 25, 2650).  This block implements these ephemerides with respect to the International Celestial Reference Frame version 2.0, adopted in 2010. |

**Note**

This block requires that you download ephemeris data using the Add-On
Explorer. To start the Add-On Explorer, in the MATLAB® Command Window, type `aeroDataPackage`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `de` |
| **Type**: character vector |
| **Values**: `DE405` | `DE421` | `DE423` | `DE430` |
| **Default**: `'DE405'` |

### **Action for out-of-range input** — Out-of-range block behavior `None` (default) | `Warning` | `Error`

Out-of-range block behavior, specified as follows.

| Action | Description |
| --- | --- |
| `None` | No action. |
| `Warning` | Warning in the Diagnostic Viewer, model simulation continues. |
| `Error` (default) | Error in the Diagnostic Viewer, model simulation stops. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `errorflag` |
| **Type**: character vector |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'Error'` |

### **Calculate rates** — Calculate rate of Earth nutation `on` (default) | `off`

Calculate the rate of the Earth nutation by selecting this check
box.

#### Dependencies

Select this check box to display the *Δψ
dot
Δεdot* port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `velflag` |
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

## Description

Implement Earth nutation

The Earth Nutation block implements the International Astronomical Union
(IAU) 1980 nutation series for a given Julian date The block uses the Chebyshev
coefficients that the NASA Jet Propulsion Laboratory provides.

The **Epoch** parameter controls the number of block inputs. If you select
`Julian date`, the block has one input port, if you select
`T0 and elapsed Julian time`, the block has two input
ports.

**Tip**

For `TJD`, Julian date input for the block:

- Calculate the date using the Julian Date Conversion
  block or the Aerospace Toolbox
  `juliandate`
  function.
- Calculate the Julian date using some other means and input it using
  the Constant block.
