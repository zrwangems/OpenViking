---
type: simulink-block
title: 'Earth Orientation Parameters'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Celestial Phenomena'
documentation_page: 'earthorientationparameters'
documentation_source_path: 'earthorientationparameters.html'
language: en
---

# Earth Orientation Parameters

## Ports
```yaml
ports:
- name: UTCMJD
  summary: UTC scalar
  direction: input
  data_types: double
- name: ΔUT1
  summary: Difference between UT1 and UTC scalar
  direction: output
  data_types: double
- name: '[xp,yp]'
  summary: Polar displacement of Earth vector
  direction: output
  data_types: double
- name: '[dX,dY]'
  summary: Adjustment to location of Celestial Intermediate Pole (CIP) vector
  direction: output
  data_types: double
- name: ΔUT1err
  summary: Return errors for the measured and predicted values in the IERS data vector
  direction: output
- name: '[xp,yp]err'
  summary: Return errors for the measured and predicted values in the IERS data vector
  direction: output
- name: '[dX,dY]err'
  summary: Return errors for the measured and predicted values in the IERS data vector
  direction: output
```

### Input

### **UTCMJD** — UTC scalar

UTC, specified as a scalar modified Julian date. Use the Julian Date Conversion
block to convert the UTC date to a modified Julian date.

**Data Types:** `double`
### Output

### **ΔUT1** — Difference between UT1 and UTC scalar

Difference between UT1 and UTC, specified as a scalar, in
seconds.

**Data Types:** `double`

### **[xp,yp]** — Polar displacement of Earth vector

Polar displacement of the Earth,
[*xp*,*yp*], specified as a
vector, in radians, from the motion of the Earth crust, along the
*x*- and *y*-axes.

**Data Types:** `double`

### **[dX,dY]** — Adjustment to location of Celestial Intermediate Pole (CIP) vector

Adjustment to the location of the Celestial Intermediate Pole (CIP),
specified as a vector, in radians. This location
([d*X*,d*Y*]) is along the
*x*- and *y*-axes.

**Data Types:** `double`

### **ΔUT1err** — Return errors for the measured and predicted values in the IERS data vector

Return errors for the measured and predicted values in the IERS data
for the difference between UT1 and UTC, specified as a vector, in
seconds.

#### Dependencies

This port is enabled when the **Output parameter
error** is selected.

### **[xp,yp]err** — Return errors for the measured and predicted values in the IERS data vector

Return errors for the measured and predicted values in the IERS data
for the polar displacement of Earth, specified as a vector, in
radians.

#### Dependencies

This port is enabled when the **Output parameter
error** is selected.

### **[dX,dY]err** — Return errors for the measured and predicted values in the IERS data vector

Return errors for the measured and predicted values in the IERS data
for the adjustment to location of Celestial Intermediate Pole (CIP),
specified as a vector, in radians.

#### Dependencies

This port is enabled when the **Output parameter
error** is selected.
## Parameters
```yaml
parameters:
- name: IERS data file
  summary: Earth orientation data aeroiersdata.mat (default) | MAT-file
  group: ''
  block_parameter: FileName
  type: character vector
  values: scalar
  default: '''aeroiersdata.mat'''
- name: Output parameter error
  summary: Enable output ports to return errors off (default) | on
  group: ''
  block_parameter: OutputError
  type: character vector
  values: scalar
  default: '''off'''
- name: Action for out-of-range input
  summary: Out-of-range block behavior None (default) | Warning | Error
  group: ''
  block_parameter: action
  type: character vector
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''Warning'''
- name: IERS data URL
  summary: Web site or Earth orientation data file http://maia.usno.navy.mil/ser7/finals2000A.data (default) | web site address
    | file name
  group: ''
  block_parameter: FileName
  type: character vector
  values: scalar
  default: '''aeroiersdata.mat'''
- name: Destination folder
  summary: Folder for IERS data file current Folder (default)
  group: ''
  block_parameter: FileName
  type: character vector
  values: scalar
  default: '''aeroiersdata.mat'''
```

### **IERS data file** — Earth orientation data `aeroiersdata.mat` (default) | MAT-file

Custom list of Earth orientation data, specified in a MAT-file.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `FileName` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'aeroiersdata.mat'` |

### **Output parameter error** — Enable output ports to return errors `off` (default) | `on`

Select this parameter to enable output ports to return errors for the
measured and predicted values in the IERS data file:

- Difference between UT1 and UTC
- Polar displacement of Earth
- Adjustment to location of Celestial Intermediate Pole (CIP)

#### Dependencies

Selecting this check box enables these ports:

- ΔUT1err
- [xp,yp]err
- [dX,dY]err

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputError` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'off'` |

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

### **IERS data URL** — Web site or Earth orientation data file `http://maia.usno.navy.mil/ser7/finals2000A.data` (default) | web site address | file name

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
| **Block Parameter**: `FileName` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'aeroiersdata.mat'` |

### **Destination folder** — Folder for IERS data file current Folder (default)

Folder for IERS data file, specified as a character array or string.
Before running this function, create *foldername* with
write permission.

To create the IERS data file in the destination folder, click the
**Create** button.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `FileName` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'aeroiersdata.mat'` |
## Libraries

Aerospace Blockset / Environment / Celestial Phenomena

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

### R2020b: Updated `aeroiersdata.mat` file

The contents of the `aeroiersdata.mat` file have been updated.
Correspondingly, the output of this block will have different results when using the
default value (`'aeroiersdata.mat'`) as the value of the
**IERS data file** parameter. The results reflect more accurate
external data from the International Earth Rotation and Reference Systems Service
(IERS).

## Description

Calculate Earth orientation parameters (EOP)

The Earth Orientation Parameters block calculates these
parameters:

- Difference between the Coordinated Universal Time (UTC) and Universal Time
  (UT1)
- Movement of the rotation axis with respect to the crust of the Earth
- Adjustment to the location of the Celestial Intermediate Pole (CIP)

By default, this block uses a prepopulated list of International Earth Rotation and
Reference Systems Service (IERS) data. This list contains measured and calculated
(predicted) data supplied by the IERS. The IERS measures and calculates this data for a
set of predetermined dates. For dates after those listed in the prepopulated list,
Earth Orientation Parameters calculates the ΔUT1 using this equation,
limiting the values to +/- 0.9 s:

```
UT1-UTC=0.5309-0.00123(MJD-57808)-(UT2-UT1)
```

Use this block when your application uses Earth Centered Inertial to Earth Centered
Earth Fixed transformations, such as for high altitude applications.
