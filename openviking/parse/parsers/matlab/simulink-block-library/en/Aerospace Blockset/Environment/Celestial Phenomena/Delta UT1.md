---
type: simulink-block
title: 'Delta UT1'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Celestial Phenomena'
documentation_page: 'deltaut1'
documentation_source_path: 'deltaut1.html'
language: en
---

# Delta UT1

## Ports
```yaml
ports:
- name: UTC
  summary: UT1 for UTC modified Julian date
  direction: input
  data_types: double
- name: ΔUT1
  summary: Difference between UT1 and UTC double
  direction: input
  data_types: double
```

### Input

### **UTC** — UT1 for UTC modified Julian date

UT1 for UTC, specified as a modified Julian date. Use the `mjuliandate` function to
convert the UTC date to a modified Julian date.

**Data Types:** `double`
### Output Arguments

### **ΔUT1** — Difference between UT1 and UTC double

Difference between UT1 and UTC.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: IERS data file
  summary: Earth orientation data aeroiersdata.mat (default) | MAT-file
  group: ''
  block_parameter: FileName
  type: character vector
  values: '''aeroiersdata.mat'' | MAT-file'
  default: '''aeroiersdata.mat'''
- name: Action for out-of-range input
  summary: Out-of-range block behavior None (default) | Warning | Error
  group: ''
  block_parameter: action
  type: character vector
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''Warning'''
- name: IERS data URL
  summary: Web site or Earth orientation data file https://maia.usno.navy.mil/ser7/finals2000A.data (default) | web site address
    | file name
  group: ''
  block_parameter: iersurl
  type: character vector
  values: '''https://maia.usno.navy.mil/ser7/finals2000A.data'' | web site address | file name'
  default: '''https://maia.usno.navy.mil/ser7/finals2000A.data'''
- name: Destination folder
  summary: Folder for IERS data file Current Folder (default)
  group: ''
  block_parameter: folder
  type: character vector
  values: '''Current Folder'' | folder name'
  default: '''Current Folder'''
```

### **IERS data file** — Earth orientation data `aeroiersdata.mat` (default) | MAT-file

Custom list of Earth orientation data, specified in a MAT-file.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `FileName` |
| **Type**: character vector |
| **Values**: `'aeroiersdata.mat'` | MAT-file |
| **Default**: `'aeroiersdata.mat'` |

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

### **IERS data URL** — Web site or Earth orientation data file `https://maia.usno.navy.mil/ser7/finals2000A.data` (default) | web site address | file name

Web site or Earth orientation data file containing the Earth orientation
data according to the IAU 2000A, specified as a web site address or file
name.

**Note**

If you receive an error message while accessing the default site, use
one of these alternate sites:

- `https://datacenter.iers.org/data/latestVersion/10_FINALS.DATA_IAU2000_V2013_0110.txt`
- `ftp://cddis.gsfc.nasa.gov/pub/products/iers/finals2000A.data`

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `iersurl` |
| **Type**: character vector |
| **Values**: `'https://maia.usno.navy.mil/ser7/finals2000A.data'` | web site address | file name |
| **Default**: `'https://maia.usno.navy.mil/ser7/finals2000A.data'` |

### **Destination folder** — Folder for IERS data file Current Folder (default)

Folder for IERS data file, specified as a character array or string.
Before running this function, create *foldername* with
write permission.

To create the IERS data file in the destination folder, click the
**Create** button.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `folder` |
| **Type**: character vector |
| **Values**: `'Current Folder'` | folder name |
| **Default**: `'Current Folder'` |
## Libraries

Aerospace Blockset / Environment / Celestial Phenomena Aerospace Blockset / Utilities / Axes Transformations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

### R2020b: Updated `aeroiersdata.mat` file

The contents of the `aeroiersdata.mat` file have been updated.
Correspondingly, the output of this block will have different results when using the
default value (`'aeroiersdata.mat'`) as the value of the
**IERS data file** parameter. The results reflect more accurate
external data from the International Earth Rotation and Reference Systems Service
(IERS).

## Description

Calculate difference between principal Universal Time (UT1) and Coordinated Universal Time (UTC) according to International Astronomical Union (IAU) 2000A reference system

The Delta UT1 block calculates the difference between principal UT1 and UTC according
to the IAU 2000A reference system and Earth orientation data. By default, this block
uses a prepopulated list of International Earth Rotation and Reference Systems Service
(IERS) data. This list contains measured and calculated (predicted) data supplied by the
IERS. The IERS measures and calculates this data for a set of predetermined dates. For
dates after those listed in the prepopulated list, Delta UT1 calculates
the data using this equation, limiting the values to +/-
.9s:

```
UT1-UTC=0.5309-0.00123(MJD-57808)-(UT2-UT1)
```
