---
type: simulink-block
title: 'International Geomagnetic Reference Field'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Gravity'
documentation_page: 'internationalgeomagneticreferencefield'
documentation_source_path: 'internationalgeomagneticreferencefield.html'
language: en
---

# International Geomagnetic Reference Field

## Ports
```yaml
ports:
- name: h
  summary: Height scalar
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
- name: dyear
  summary: Desired year scalar
  direction: input
  data_types: double
- name: XYZ
  summary: Magnetic field vector
  direction: output
  data_types: double
- name: H
  summary: Horizontal intensity scalar
  direction: output
  data_types: double
- name: D
  summary: Declination scalar
  direction: output
  data_types: double
- name: l
  summary: Inclination scalar
  direction: output
  data_types: double
- name: F
  summary: Total intensity scalar
  direction: output
  data_types: double
- name: DXDYDZ
  summary: Secular variation of magnetic field vector
  direction: output
  data_types: double
- name: DH
  summary: Secular variation of horizontal intensity scalar
  direction: output
  data_types: double
- name: DD
  summary: Secular variation of declination scalar
  direction: output
  data_types: double
- name: DI
  summary: Secular variation of inclination scalar
  direction: output
  data_types: double
- name: DF
  summary: Secular variation of total intensity scalar
  direction: output
  data_types: double
```

### Input

### **h** — Height scalar

Height, specified as a scalar, in selected units.

**Data Types:** `double`

### **μ (deg)** — Latitude scalar

Latitude, specified as a scalar in degrees. This block accepts latitude values
greater than 90 and less than -90.

**Data Types:** `double`

### **l (deg)** — Longitude scalar

Longitude, specified as a scalar, in degrees. This block accepts ranges greater
than 180 and less than -180.

**Data Types:** `double`

### **dyear** — Desired year scalar

Desired year in a decimal format to include any fraction of the year that has
already passed. The value is the current year plus the number of days that have passed
in this year divided by 365. To calculate the decimal year, `dyear`,
for March 21, 2015:

```
dyear=decyear('21-March-2015','dd-mmm-yyyy')
```

#### Dependencies

To enable this port, select **Input decimal year**.

**Data Types:** `double`
### Output

### **XYZ** — Magnetic field vector

Magnetic field, returned as a vector, in selected units. The components of this
vector are in the north-east-down (NED) reference frame.

**Data Types:** `double`

### **H** — Horizontal intensity scalar

Horizontal intensity, returned as a scalar, in selected units.

**Data Types:** `double`

### **D** — Declination scalar

Declination, returned as a scalar, in degrees.

**Data Types:** `double`

### **l** — Inclination scalar

Inclination, returned as a scalar, in degrees.

**Data Types:** `double`

### **F** — Total intensity scalar

Total intensity, returned as a scalar, in selected units.

**Data Types:** `double`

### **DXDYDZ** — Secular variation of magnetic field vector

Secular variation of magnetic field, returned as a vector in selected units per
year.

#### Dependencies

To enable this port, select **Output secular
variation**.

**Data Types:** `double`

### **DH** — Secular variation of horizontal intensity scalar

Secular variation of horizontal intensity, returned as a scalar, in selected units
per year.

#### Dependencies

To enable this port, select **Output secular
variation**.

**Data Types:** `double`

### **DD** — Secular variation of declination scalar

Secular variation of declination, returned as a scalar, in minutes per
year.

#### Dependencies

To enable this port, select **Output secular
variation**.

**Data Types:** `double`

### **DI** — Secular variation of inclination scalar

Secular variation of inclination, returned as a scalar, in minutes per
year.

#### Dependencies

To enable this port, select **Output secular
variation**.

**Data Types:** `double`

### **DF** — Secular variation of total intensity scalar

Secular variation of total intensity, returned as a scalar, in selected units per
year.

#### Dependencies

To enable this port, select **Output secular
variation**.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Generation
  summary: International Geomagnetic Reference Field generation IGRF-14 (default) | IGRF-13 | IGRF-11 | IGRF-12
  group: ''
  block_parameter: generation
  type: character vector
  values: '''IGRF-14'' | ''IGRF-13'' | ''IGRF-12'' | ''IGRF-11'' |'
  default: '''IGRF-14'''
- name: Units
  summary: Units Metric (MKS) (default) | English
  group: ''
  block_parameter: units
  type: character vector
  values: '''Metric (MKS)'' | ''English'''
  default: '''Metric (MKS)'''
- name: Input decimal year
  summary: Desired year on (default) | off
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
  summary: Input year 2025 (default) | 1900 to 2030
  group: ''
  block_parameter: year
  type: character vector
  values: any year
  default: '''2025'''
- name: Action for out-of-range input
  summary: Out-of-range block behavior None (default) | Warning | Error
  group: ''
  block_parameter: action
  type: character vector
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''Warning'''
- name: Output secular variance
  summary: Secular variances on (default) | off
  group: ''
  block_parameter: sv_out
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
```

### **Generation** — International Geomagnetic Reference Field generation `IGRF-14` (default) | `IGRF-13` | `IGRF-11` | `IGRF-12`

International Geomagnetic Reference Field generation, selected from
`IGRF-14`, `IGRF-13`,
`IGRF-12`, or `IGRF-11`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `generation` |
| **Type:** character vector |
| **Values:** `'IGRF-14'` | `'IGRF-13'` | `'IGRF-12'` | `'IGRF-11'` | |
| **Default:** `'IGRF-14'` |

**Data Types:** `char` | `string`

### **Units** — Units `Metric (MKS)` (default) | `English`

Parameter and output units, specified as:

| Units | Height |
| --- | --- |
| `Metric (MKS)` | Meters |
| `English` | Feet |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `units` |
| **Type:** character vector |
| **Values:** `'Metric (MKS)'` | `'English'` |
| **Default:** `'Metric (MKS)'` |

### **Input decimal year** — Desired year `on` (default) | `off`

- To specify the decimal year with an input port, select this check box.
- To specify the decimal year using the values of **Month**,
  **Day**, and **Year**, clear this check
  box.

#### Dependencies

To enable **Month**, **Day**, and
**Year**, clear this parameter.

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

To enable this parameter, clear **Input decimal year**.

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

To enable this parameter, clear **Input decimal year**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `day` |
| **Type:** character vector |
| **Values:** `'1'` to `'31'` |
| **Default:** `'1'` |

### **Year** — Input year `2025` (default) | `1900` to `2030`

Year to calculate decimal year, specified as `1900` to
`2030`.

#### Dependencies

To enable this parameter, clear **Input decimal year**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `year` |
| **Type:** character vector |
| **Values:** any year |
| **Default:** `'2025'` |

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

### **Output secular variance** — Secular variances `on` (default) | `off`

Select this check box to enable the output of secular variances (annual rate of
change) with nonsecular variances. Otherwise, clear this check box.

| Secular Variance | Description |
| --- | --- |
| Magnetic Field | Magnetic field vector, in nanotesla (nT). *Z* is the vertical component (+ve down) |
| Horizontal Intensity | Horizontal intensity, in nanotesla (nT) |
| Declination | Declination, in degrees (+ve east) |
| Inclination | Inclination, in degrees (+ve down) |
| Total Intensity | Total intensity, in nanotesla (nT) |
| SV Magnetic Field | Secular variation of magnetic field |
| SV Horizontal Intensity | Secular variation of horizontal intensity |
| SV Declination | Secular variation of declination, the angle between true north and the magnetic field vector (positive eastward) |
| SV Inclination | Secular variation of inclination, the angle between the horizontal plane and the magnetic field vector (positive downward) |
| SV Total Intensity | Secular variation of total intensity |

Clear this check box to enable just the nonsecular variances:

- Magnetic Field
- Horizontal Intensity
- Declination
- Inclination
- Total Intensity

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sv_out` |
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

**Introduced in R2020b**

### R2025a: International Geomagnetic Reference Field block now supports International Geomagnetic Reference Field generation 14 (IGRF-14)

The International Geomagnetic Reference Field block now supports the International Geomagnetic
Reference Field generation 14 (IGRF-14).

## Description

Calculate Earth magnetic field and secular variation using International Geomagnetic Reference Field

The International Geomagnetic Reference Field block calculates the Earth
magnetic field and secular variation using the selected International Geomagnetic Reference
Field generation. It calculates the Earth magnetic field and secular variation at a position
and time using the selected International Geomagnetic Reference Field generation.
