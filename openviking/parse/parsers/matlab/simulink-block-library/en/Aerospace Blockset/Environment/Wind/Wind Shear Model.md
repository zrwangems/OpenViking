---
type: simulink-block
title: 'Wind Shear Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Wind'
documentation_page: 'windshearmodel'
documentation_source_path: 'windshearmodel.html'
language: en
---

# Wind Shear Model

## Ports
```yaml
ports:
- name: h
  summary: Altitude scalar
  direction: input
  data_types: double
- name: DCM
  summary: Direction cosine matrix 3-by-3 matrix
  direction: input
  data_types: double
- name: Vwind
  summary: Mean wind speed three-element vector
  direction: output
  data_types: double
```

### Input

### **h** — Altitude scalar

Altitude, specified as a scalar in specified units.

**Data Types:** `double`

### **DCM** — Direction cosine matrix 3-by-3 matrix

Direction cosine matrix, specified as a 3-by-3 matrix representing the
flat Earth coordinates to body-fixed axis coordinates.

**Data Types:** `double`
### Output

### **Vwind** — Mean wind speed three-element vector

Mean wind speed, returned as a three-element vector in the same body coordinate
reference as the **DCM** input, in specified units.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Units
  summary: Wind shear units Metric (MKS) (default) | English (Velocity in ft/s) | English (Velocity in kts)
  group: ''
  block_parameter: units
  type: character vector
  values: '''Metric (MKS)'' | ''English (Velocity in ft/s)'' | ''English (Velocity in kts)'''
  default: '''Metric (MKS)'''
- name: Flight phase
  summary: Flight phase Category C - Terminal Flight Phase (default) | Other
  group: ''
  block_parameter: phase
  type: character vector
  values: '''Category C - Terminal Flight Phase'' | ''Other'''
  default: '''Category C - Terminal Flight Phase'''
- name: Wind speed at 20 ft altitude (kts)
  summary: Wind speed 15 (default) | scalar
  group: ''
  block_parameter: W_20
  type: character vector
  values: scalar
  default: '''15'''
- name: Wind direction at 20 ft altitude (degrees clockwise from north)
  summary: Wind direction 0 (default) | scalar
  group: ''
  block_parameter: Wdeg
  type: character vector
  values: scalar
  default: '''0'''
```

### **Units** — Wind shear units `Metric (MKS)` (default) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

Wind shear units, specified as:

| Units | Wind | Altitude |
| --- | --- | --- |
| `Metric (MKS)` | Meters/second | Meters |
| `English (Velocity in ft/s)` | Feet/second | Feet |
| `English (Velocity in kts)` | Knots | Feet |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **Default**: `'Metric (MKS)'` |

### **Flight phase** — Flight phase `Category C - Terminal Flight Phase` (default) | `Other`

Flight phase, specified as:

- `Category C - Terminal Flight Phase`, as
  specified by Military Specification MIL-F-8785C.
- `Other`

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `phase` |
| **Type**: character vector |
| **Values**: `'Category C - Terminal Flight Phase'` | `'Other'` |
| **Default**: `'Category C - Terminal Flight Phase'` |

### **Wind speed at 20 ft altitude (kts)** — Wind speed `15` (default) | scalar

Measured wind speed at a height of 6 m (20 ft) above the ground, specified
as a scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `W_20` |
| **Type**: character vector |
| **Values**: `scalar` |
| **Default**: `'15'` |

### **Wind direction at 20 ft altitude (degrees clockwise from north)** — Wind direction `0` (default) | scalar

Wind direction at a height of 6 m (20 ft) above the ground, specified as a
scalar, in degrees clockwise from the direction of the Earth
*x*-axis (north). The wind direction is defined as the
direction from which the wind is coming.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wdeg` |
| **Type**: character vector |
| **Values**: `scalar` |
| **Default**: `'0'` |
## Libraries

Aerospace Blockset / Environment / Wind

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Calculate wind shear conditions

The Wind Shear Model block adds wind shear to the aerospace
model. This implementation is based on the mathematical representation in the Military
Specification MIL-F-8785C [1].
