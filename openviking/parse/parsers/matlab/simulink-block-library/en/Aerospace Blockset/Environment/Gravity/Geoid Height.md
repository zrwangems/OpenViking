---
type: simulink-block
title: 'Geoid Height'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Gravity'
documentation_page: 'geoidheight'
documentation_source_path: 'geoidheight.html'
language: en
---

# Geoid Height

## Ports

### Input

### **μ (deg)** — Geodetic latitude scalar

Geodetic latitude, specified as a scalar, in degrees, where north latitude is positive
and south latitude is negative. Input latitude must be of type single or
double. If latitude is not in the range from –90 to 90, the block wraps
it to be within the range.

**Data Types:** `double` | `single`

### **l (deg)** — Longitude scalar

Longitude, specified as a scalar, in degrees, where east longitude is
positive in the range from 0 to 360. Input longitude must be of type
single or double. If longitude is not in the range from 0 to 360, the
block wraps it to be within the range when **Action for
out-of-range input** is set to
`None` or
`Warning`. It does not wrap when
**Action for out-of-range input** is set to
`Error`.

**Data Types:** `double` | `single`
### Output

### **N** — geoid height scalar

Geoid height, returned as a scalar, in selected length units. The data
type is the same as the latitude in the first input.

**Data Types:** `double` | `single`

## Parameters

### **Units** — Parameter and output units `Metric (MKS)` (default) | `English`

Parameter and output units, specified as:

| Units | Height |
| --- | --- |
| `Metric (MKS)` | Meters |
| `English` | Feet |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English'` |
| **Default**: `'Metric (MKS)'` |

### **Geopotential model** — Geopotential model `EGM96` (default) | `EGM2008` | `Custom`

Geopotential model, specified as:

| Geopotential Model | Description |
| --- | --- |
| `EGM96 (Earth)` | Default. EGM96 Geopotential Model to degree and order 360. This model uses a 15-minute grid of point values in the tide-free system. This block calculates geoid heights to an accuracy of 0.01 m for this model. |
| `EGM2008 (Earth)` | EGM2008 Geopotential Model to degree and order 2159. This model uses a 2.5-minute grid of point values in the tide-free system. This block calculates geoid heights to an accuracy of 0.001 m for this model.  **Note**  This block requires that you download geoid data for the EGM2008 Geopotential Model with the Add-On Explorer. Click the **Get data** button to start the Add-On Explorer. For more information, see `aeroDataPackage`. If the data is installed, the **Get data** button does not appear. |
| `Custom` | Custom geopotential model that you define in **Geopotential mat-file**. This block calculates geoid heights to an accuracy of 0.01 m for custom models. Selecting `Custom` enables the **Geopotential mat-file** parameter. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `gtype` |
| **Type**: character vector |
| **Values**: `'EGM96'` | `'EGM2008'` | `'Custom'` |
| **Default**: `'Earth'` |

### **Geopotential mat-file** — Geopotential MAT-file `'geoidegm96grid'` (default) | MAT-file

Geopotential MAT-file that defines your custom geopotential model.

#### Dependencies

To enable this, set **Geopotential model** to
`Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `datafile` |
| **Type**: character vector |
| **Values**: `'geoidegm96grid'` | MAT-file |
| **Default**: `'geoidegm96grid'` |

### **Data type** — Data type of input and output signals `double` (default) | `single`

Data type of the input and output signals, specified as
`double` or
`single`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `dtype` |
| **Type**: character vector |
| **Values**: `'double'` | `'single'` |
| **Default**: `'double'` |

### **Action for out-of-range input** — Out-of-range input behavior `Warning` (default) | `Error` | `None`

Out-of-range input behavior (latitude outside –90 to 90 degrees, longitude outside 0 to
360 degrees), specified as follows.

| Action | Description |
| --- | --- |
| `None` | No action. |
| `Warning` | Warning in the Diagnostic Viewer. |
| `Error` (default) | MATLAB® returns an exception, model simulation stops. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `action` |
| **Type**: character vector |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'Warning'` |

## Libraries

Aerospace Blockset / Environment / Gravity

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2010b**

## Description

Calculate undulations/height

The Geoid Height block calculates the geoid height using the
**Geopotential model** parameter. The block interpolates the geoid
heights from a grid of point values in the tide-free system. It uses the specified
geopotential model to degree and order of the model. The geoid undulations are relative
to the WGS84 ellipsoid.

The interpolation scheme wraps over the poles to allow for geoid height calculations at and
near these locations.
