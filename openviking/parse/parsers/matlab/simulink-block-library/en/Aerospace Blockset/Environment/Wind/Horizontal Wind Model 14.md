---
type: simulink-block
title: 'Horizontal Wind Model 14'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Wind'
documentation_page: 'horizontalwindmodel14'
documentation_source_path: 'horizontalwindmodel14.html'
language: en
---

# Horizontal Wind Model 14

## Ports
```yaml
ports:
- name: First
  summary: geodetic latitude (μ), longitude (l), and geopotential altitude (h) three-element vector of doubles
  direction: input
- name: Second
  summary: day of year scalar double
  direction: input
- name: Third
  summary: elapsed seconds scalar double
  direction: input
- name: Fourth (Optional)
  summary: Ap index scalar double
  direction: input
- name: First
  summary: wind velocity vector 1-by-2 vector of doubles
  direction: output
```

### Input

### **First** — geodetic latitude (μ), longitude (`l`), and geopotential altitude (`h`) three-element vector of doubles

The input specifies the geodetic latitude (μ), longitude
(`l`), and geopotential altitude (`h`)
where the block implements the model.

Latitude and longitude values are in degrees.

The altitude value is in the units you selected in the **Units** parameter.
Specify the altitude element as a value between 0 and 500 km. Values are
held outside the range 0 to 500 km.

### **Second** — day of year scalar double

The input specifies the day of year in Coordinated Universal Time (UTC). The input specifies
the day as a value between 1 and 366 (for a leap year). Values are
wrapped within 1 to 366 days.

### **Third** — elapsed seconds scalar double

Contains elapsed seconds since midnight for the selected day,
in UTC.

### **Fourth (Optional)** — Ap index scalar double

Contains the Ap index for the Universal Time (UT) when the block evaluates the model. Select
the index from the NOAA
National Geophysical Data Center, which contains 3 hour
interval geomagnetic disturbance index values. If the Ap index value is
greater than zero, the software takes into account magnetic effects
during model evaluation.
### Output

### **First** — wind velocity vector 1-by-2 vector of doubles

The wind velocity vector contains the meridional and zonal wind
components in that order.
## Parameters
```yaml
parameters:
- name: Units
  summary: input and output units Metric (MKS) (default) | English (Velocity in ft/s) | English (Velocity in kts)
  group: ''
  block_parameter: units
  type: character vector
  values: '''Metric (MKS)'' | ''English (Velocity in ft/s)'' | ''English (Velocity in kts)'''
  default: '''Metric (MKS)'''
- name: Model
  summary: horizontal wind model Quiet (default) | Total | Disturbance
  group: ''
  block_parameter: model
  type: character vector
  values: '''Quiet'' | ''Total'' | ''Disturbance'''
  default: '''Quiet'''
- name: Action for out-of-range input
  summary: block behavior Error (default) | Warning | None
  group: ''
  block_parameter: action
  type: character vector
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''Error'''
```

### **Units** — input and output units `Metric (MKS)` (default) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

Input and output units for wind speed and velocity, specified as:

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

### **Model** — horizontal wind model `Quiet` (default) | `Total` | `Disturbance`

Select the horizontal wind model type for which to calculate
the wind components.

- `Quiet`

  Calculate the horizontal wind model without the magnetic disturbances.
  For this model type, do not input an Ap index value.
- `Total`

  Calculate the combined effect of the quiet and magnetic disturbances.
  For this model type, input Ap index values greater than or equal to
  zero.
- `Disturbance`

  Calculate the effect of magnetic disturbances in the wind. For
  this model type, input Ap index values greater than or equal to zero.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `model` |
| **Type**: character vector |
| **Values**: `'Quiet'` | `'Total'` | `'Disturbance'` |
| **Default**: `'Quiet'` |

### **Action for out-of-range input** — block behavior `Error` (default) | `Warning` | `None`

Specify the block behavior when the block inputs are out of
range.

| Value | Description |
| --- | --- |
| `Error` (default) | MATLAB® returns an exception, and model simulation stops. For Accelerator and Rapid Accelerator modes, setting the action to `Error` has no effect and the model behaves as though the action is set to `None`. |
| `Warning` | Warning in the Diagnostic Viewer, and model simulation continues. For Accelerator and Rapid Accelerator modes, setting the action to `Warning` has no effect and the model behaves as though the action is set to `None`. |
| `None` | No action. The block imposes upper and lower limits on an input signal. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `action` |
| **Type**: character vector |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'Error'` |
## Libraries

Aerospace Blockset / Environment / Wind

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2021b: Horizontal Wind Model 14 Block Possible Changed Returned Values

The Horizontal Wind Model 14 block now accepts:

- **day** port values that are decimal, negative,
  `0`, or greater than `366`.
- **sec** port values that are `0` or
  greater than `86400`.

As a result, the output values from this block might change from previous
releases.

## Description

Implement Horizontal Wind Model 14

The Horizontal Wind Model 14 block implements the U.S. Naval Research Laboratory (HWM™) routine to calculate the meridional and zonal components of the wind for
a set of geographic coordinates: latitude, longitude, and altitude.
