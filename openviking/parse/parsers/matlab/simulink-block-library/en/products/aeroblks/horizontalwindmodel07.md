---
type: simulink-block
title: 'Horizontal Wind Model 07'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Wind'
documentation_page: 'horizontalwindmodel07'
documentation_source_path: 'horizontalwindmodel07.html'
language: en
---

# Horizontal Wind Model 07

## Ports

### Input

### **μ l h** — Geodetic latitude, longitude, and geopotential altitude three-element vector | altitude is a value between 0 and 500 km

Geodetic latitude (μ), longitude (l), and geopotential altitude (h),
specified as a three-element vector.

Latitude and longitude values are in degrees.

Altitude values are held outside the range 0 to 500 km. The altitude value is in the
units selected in **Units**.

**Data Types:** `double`

### **day** — Day scalar | value between 1 and 366

Day of year in Coordinated Universal Time (UTC), specified as a value between 1 and 366
(for a leap year). Values are wrapped within the range 1 to 366
days.

**Data Types:** `double`

### **sec** — Elapsed seconds scalar

Elapsed seconds since midnight for the specified day, in UTC.

**Data Types:** `double`

### **Ap** — Ap index scalar | range from 0 to 400

Ap index for the Universal Time (UT), specified as a scalar, ranging
from 0 to 400. Select the index from NOAA
National Geophysical Data Center, which contains 3 hour
interval geomagnetic disturbance index values. If the Ap index value is
greater than zero, the software takes into account magnetic effects
during model evaluation.

#### Dependencies

To enable this port, set **Model** to
`Total` or
`Disturbance`.

**Data Types:** `double`
### Output

### **Vwind** — Wind velocity vector 1-by-2 vector

Wind velocity vector, returned as a 1-by-2 vector, containing the
meridional and zonal wind components, in that order.

**Data Types:** `double`

## Parameters

### **Units** — Input and output units `Metric (MKS)` (default) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

Input and output units, specified as:

| Units | Wind Speed | Wind Velocity |
| --- | --- | --- |
| `Metric (MKS)` | Meters per second | Meters per second |
| `English (Velocity in ft/s)` | Feet per second | Feet per second |
| `English (Velocity in kts)` | Knots | Knots |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **Default**: `'Metric (MKS)'` |

### **Model** — Horizontal wind model type `Quiet` (default) | `Total` | `Disturbance`

Horizontal wind model type for which to calculate the wind components,
specified as:

- `Disturbance`

  Calculate the effect of only magnetic disturbances in the
  wind.
- `Quiet`

  Calculate the horizontal wind model without magnetic
  disturbances.
- `Total`

  Calculate the combined effect of the quiet and magnetic
  disturbances.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `model` |
| **Type**: character vector |
| **Values**: `'Quiet'` | `'Total'` | `'Disturbance'` |
| **Default**: `'Quiet'` |

### **Action for out-of-range input** — Out-of-range block behavior `Error` (default) | `Warning` | `None`

Out-of-range block behavior, specified as follows.

| Value | Description |
| --- | --- |
| `None` | No action. The block imposes upper and lower limits on an input signal. |
| `Warning` | Warning in the Diagnostic Viewer, model simulation continues. For Accelerator and Rapid Accelerator modes, setting the action to `Warning` has no effect and the model behaves as though the action is set to `None`. |
| `Error` | MATLAB® returns an exception, model simulation stops. For Accelerator and Rapid Accelerator modes, setting the action to `Error` has no effect and the model behaves as though the action is set to `None`. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `action` |
| **Type**: character vector |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'Warning'` |

## Libraries

Aerospace Blockset / Environment / Wind

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014b**

### R2021b: Horizontal Wind Model 07 Block Possible Changed Returned Values

The Horizontal Wind Model 07 block now accepts:

- **day** port values that are decimal, negative,
  `0`, or greater than `366`.
- **sec** port values that are `0` or
  greater than `86400`.

As a result, the output values from this block might change from previous
releases.

## Description

Implement Horizontal Wind Model 07

The Horizontal Wind Model 07 block implements the U.S. Naval Research
Laboratory HWM™ routine to calculate the meridional and zonal components of the wind for a
set of geographic coordinates: latitude, longitude, and altitude.
