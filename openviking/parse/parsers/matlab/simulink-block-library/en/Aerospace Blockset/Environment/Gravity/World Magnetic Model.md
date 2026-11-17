---
type: simulink-block
title: 'World Magnetic Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Gravity'
documentation_page: 'worldmagneticmodel'
documentation_source_path: 'worldmagneticmodel.html'
language: en
---

# World Magnetic Model

## Ports
```yaml
ports:
- name: h
  summary: Ellipsoidal height scalar
  direction: input
  data_types: double
- name: μ (deg)
  summary: Latitude scalar
  direction: input
  data_types: double
- name: l (deg)
  summary: Longitude scalar
  direction: input
  data_types: double
- name: Decimal Year
  summary: Desired year scalar
  direction: input
  data_types: double
- name: Magnetic Field (nT)
  summary: Magnetic field vector
  direction: output
  data_types: double
- name: Horizontal Intensity (nT)
  summary: Horizontal intensity scalar
  direction: output
  data_types: double
- name: Declination (deg)
  summary: Declination scalar
  direction: output
  data_types: double
- name: Inclination (deg)
  summary: Inclination scalar
  direction: output
  data_types: double
- name: Total Intensity (nT)
  summary: Total intensity scalar
  direction: output
  data_types: double
```

### Input

### **h** — Ellipsoidal height scalar

Ellipsoidal height above the WGS84 ellipsoid, specified as a scalar, in selected
units.

**Data Types:** `double`

### **μ (deg)** — Latitude scalar

Latitude, specified as a scalar, in degrees. If latitude is out of range, the
block wraps it to be within the range when **Action for
out-of-range** input is set to `None` or
`Warning`. It does not wrap when **Action for
out-of-range** is set to `Error`.

**Data Types:** `double`

### **l (deg)** — Longitude scalar

Longitude, specified as a scalar, in degrees. If longitude is out of range, the
block wraps it to be within the range when **Action for
out-of-range** input is set to `None` or
`Warning`. It does not wrap when **Action for
out-of-range** is set to `Error`.

**Data Types:** `double`

### **Decimal Year** — Desired year scalar

Desired year in a decimal format to include any fraction of the year that has
already passed. The value is the current year plus the number of days that have passed
in this year divided by 365.

For example, to calculate the decimal year, `dyear`, for March
21, 2015:

```
dyear=decyear('21-March-2015','dd-mmm-yyyy')
```

```
dyear =
   2.0152e+03
```

**Data Types:** `double`
### Output

### **Magnetic Field (nT)** — Magnetic field vector

Magnetic field, returned as a vector, in selected units. The magnetic field is
defined in the NED frame.

**Data Types:** `double`

### **Horizontal Intensity (nT)** — Horizontal intensity scalar

Horizontal intensity, returned as a scalar, in specified units.

**Data Types:** `double`

### **Declination (deg)** — Declination scalar

Declination, returned as a scalar, in degrees.

**Data Types:** `double`

### **Inclination (deg)** — Inclination scalar

Inclination, returned as a scalar, in degrees.

**Data Types:** `double`

### **Total Intensity (nT)** — Total intensity scalar

Total intensity, returned as a scalar, in selected units.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: WMM coefficients
  summary: World Magnetic Model coefficient file WMM2025 (2025-2030) (default) | WMM2020 (2020-2025) | WMM2015 V2 (2015-2020)
    | WMM2000 (2000-2005) | WMM2005 (2005-2010) | WMM2010 (2010-2015) | WMM2015 V1 (2015-2020) | Custom
  group: ''
  block_parameter: model
  type: character vector
  values: '''WMM2025 (2025-2030)'' ''WMM2020 (2020-2025)'' | ''WMM2015 V2 (2015-2020)'' | ''WMM2000 (2000-2005)'' | ''WMM2005
    (2005-2010)'' | ''WMM2010 (2010-2015)'' | ''WMM2015 V1 (2015-2020)'' | ''Custom'''
  default: '''WMM2025 (2025-2030)'''
- name: Custom .COF file
  summary: Custom World Magnetic Model coefficient file 'WMM2025COF' (default) | any coefficient file name
  group: ''
  block_parameter: customFile
  type: character vector
  values: '''WMM2025.COF'' | any coefficient file name'
  default: '''WMM2025.COF'''
- name: Units
  summary: Input and output units Metric (MKS) (default) | English
  group: ''
  block_parameter: units
  type: character vector
  values: '''Metric (MKS)'' | ''English'''
  default: '''Metric (MKS)'''
- name: Input decimal year
  summary: Input decimal year on (default) | off
  group: ''
  block_parameter: time_in
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Month
  summary: Input month January (default) | February | March | April | May | June | July | August | September | October | November
    | December
  group: ''
  block_parameter: month
  type: character vector
  values: '''January'' | ''February'' | ''March'' | ''April'' | ''May'' | ''June'' | ''July'' | ''August'' | ''September''
    | ''October'' | ''November'' | ''December'''
  default: '''January'''
- name: Day
  summary: Input day 1 (default) | 1 to 31
  group: ''
  block_parameter: day
  type: character vector
  values: '''1'' to ''31'''
  default: '''1'''
- name: Year
  summary: Input year 2025 (default) | any year
  group: ''
  block_parameter: year
  type: character vector
  values: any year
  default: '''2025'''
- name: Action for out-of-range input
  summary: Out-of-range action Error (default) | Warning | None
  group: ''
  block_parameter: action
  type: character vector
  values: '''Error'' | ''Warning'' | ''None'''
  default: '''Error'''
- name: Output horizontal intensity
  summary: Output horizontal intensity on (default) | off
  group: ''
  block_parameter: h_out
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Output declination
  summary: Output declination on (default) | off
  group: ''
  block_parameter: dec_out
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Output inclination
  summary: Output inclination on (default) | off
  group: ''
  block_parameter: inc_out
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Output total intensity
  summary: Output total intensity on (default) | off
  group: ''
  block_parameter: ti_out
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
```

### **WMM coefficients** — World Magnetic Model coefficient file `WMM2025 (2025-2030)` (default) | `WMM2020 (2020-2025)` | `WMM2015 V2 (2015-2020)` | `WMM2000 (2000-2005)` | `WMM2005 (2005-2010)` | `WMM2010 (2010-2015)` | `WMM2015 V1 (2015-2020)` | `Custom`

World Magnetic Model coefficient file, selected from the list.

- `WMM2000 (2000-2005)` — World Magnetic Model 2000
  coefficient file
- `WMM2005 (2005-2010)` — World Magnetic Model 2005
  coefficient file
- `WMM2010 (2010-2015)` — World Magnetic Model 2010
  coefficient file
- `WMM2015 V1 (2015-2020)` — World Magnetic Model 2015
  (v1) coefficient file
- `WMM2015 V2 (2015-2020)` — World Magnetic Model 2015
  (v2) coefficient file
- `WMM2020 (2020-2025)` — World Magnetic Model 2020
  coefficient file
- `WMM2025 (2025-2030)` — World Magnetic Model 2025
  coefficient file
- `Custom` — Specify your own World Magnetic Model
  coefficient file. You can download a World Magnetic Model coefficient file from
  The
  World Magnetic Model.

#### Dependencies

Selecting `Custom` enables the **Custom .COF
file** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `model` |
| **Type:** character vector |
| **Values:** `'WMM2025 (2025-2030)'` `'WMM2020 (2020-2025)'` | `'WMM2015 V2 (2015-2020)'` | `'WMM2000 (2000-2005)'` | `'WMM2005 (2005-2010)'` | `'WMM2010 (2010-2015)'` | `'WMM2015 V1 (2015-2020)'` | `'Custom'` |
| **Default:** `'WMM2025 (2025-2030)'` |

### **Custom .COF file** — Custom World Magnetic Model coefficient file `'WMM2025COF'` (default) | any coefficient file name

World Magnetic Model coefficient file, downloaded from The World
Magnetic Model. For example, if you want to download a coefficient file not yet
listed in the **WMM coefficients** list.

#### Dependencies

To enable this parameter, select `Custom` for the
**WMM coefficients** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `customFile` |
| **Type:** character vector |
| **Values:** `'WMM2025.COF'` | any coefficient file name |
| **Default:** `'WMM2025.COF'` |

### **Units** — Input and output units `Metric (MKS)` (default) | `English`

Input and output units:

| Units | Height | Magnetic Field | Horizontal Intensity | Total Intensity |
| --- | --- | --- | --- | --- |
| `Metric (MKS)` | Meters | Nanotesla | Nanotesla | Nanotesla |
| `English` | Feet | Nanogauss | Nanogauss | Nanogauss |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `units` |
| **Type:** character vector |
| **Values:** `'Metric (MKS)'` | `'English'` |
| **Default:** `'Metric (MKS)'` |

### **Input decimal year** — Input decimal year on (default) | off

- To specify the decimal year with an input port for the World Magnetic Model 2015
  block, select this check box
- To specify the decimal year using the values of **Month**,
  **Day**, and **Year**, clear this check
  box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `time_in` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Month** — Input month `January` (default) | `February` | `March` | `April` | `May` | `June` | `July` | `August` | `September` | `October` | `November` | `December`

Month to calculate decimal year.

#### Dependencies

To enable this parameter, select **Input decimal year**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `month` |
| **Type:** character vector |
| **Values:** `'January'` | `'February'` | `'March'` | `'April'` | `'May'` | `'June'` | `'July'` | `'August'` | `'September'` | `'October'` | `'November'` | `'December'` |
| **Default:** `'January'` |

### **Day** — Input day 1 (default) | `1` to `31`

Day to calculate decimal year.

#### Dependencies

To enable this parameter, select **Input decimal year**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `day` |
| **Type:** character vector |
| **Values:** `'1'` to `'31'` |
| **Default:** `'1'` |

### **Year** — Input year 2025 (default) | any year

Year to calculate decimal year.

#### Dependencies

To enable this parameter, select **Input decimal year**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `year` |
| **Type:** character vector |
| **Values:** any year |
| **Default:** `'2025'` |

### **Action for out-of-range input** — Out-of-range action `Error` (default) | `Warning` | `None`

Out-of-range block behavior, specified as follows.

| Action | Description |
| --- | --- |
| `None` | No action. |
| `Warning` | Warning in the Diagnostic Viewer, model simulation continues. |
| `Error` (default) | Error in the Diagnostic Viewer, model simulation stops. |

If longitude or latitude is out of range, the block wraps it to be within the range
when **Action for out-of-range** input is set to
`None` or `Warning`. It does not
wrap when **Action for out-of-range** is set to
`Error`.

The World Magnetic Model block accepts out-of-range height inputs
(less than -1000 m or greater than 850000 m) when **Action for
out-of-range** is set to `None` or
`Warning`. However, the block output might not be accurate or
reliable for these values. The World Magnetic Model is valid only between -1000 m and
850000 m.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `action` |
| **Type:** character vector |
| **Values:** `'Error'` | `'Warning'` | `'None'` |
| **Default:** `'Error'` |

### **Output horizontal intensity** — Output horizontal intensity on (default) | `off`

To output the horizontal intensity value, select this check box. Otherwise, clear
this check box.

#### Dependencies

To enable the **Horizontal Intensity** output port, select this
check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `h_out` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Output declination** — Output declination on (default) | `off`

To output the declination, the angle between true north and the magnetic field
vector (positive eastwards), select this check box. Otherwise, clear this check
box.

#### Dependencies

To enable the **Declination** output port, select this check
box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `dec_out` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Output inclination** — Output inclination on (default) | `off`

To output the inclination, the angle between the horizontal plane and the magnetic
field vector (positive downwards), select this check box. Otherwise, clear this check
box.

#### Dependencies

To enable the **Inclination** output port, select this check
box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `inc_out` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Output total intensity** — Output total intensity on (default) | `off`

To output the total intensity, select this check box. Otherwise, clear this check
box.

#### Dependencies

To enable the **Total Intensity** output port, select this check
box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ti_out` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |
## Libraries

Aerospace Blockset / Environment / Gravity

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

### R2025a: World Magnetic Model block now supports World Magnetic Model (WMM) WMM2025

The World Magnetic Model block now supports the World Magnetic Model (WMM)
WMM2025.

## Description

Calculate Earth's magnetic field at specific location and time using World Magnetic Model

The World Magnetic Model block implements the mathematical
representation of the National Geospatial Intelligence Agency (NGA) World Magnetic Model. The
World Magnetic Model block calculates the Earth magnetic field vector,
horizontal intensity, declination, inclination, and total intensity at a specified location
and time. The reference frame is north-east-down (NED).

**Note**

Use this block to model the Earth magnetic field between altitudes of -1,000 m to
850,000 m meters.
