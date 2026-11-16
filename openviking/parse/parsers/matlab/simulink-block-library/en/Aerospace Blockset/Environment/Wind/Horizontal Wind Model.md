---
type: simulink-block
title: 'Horizontal Wind Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Wind'
documentation_page: 'horizontalwindmodel'
documentation_source_path: 'horizontalwindmodel.html'
language: en
---

# Horizontal Wind Model

## Ports

### Input

### **DCM** — Direction cosine matrix 3-by-3 matrix

Direction cosine matrix, specified as a 3-by-3 matrix representing the
flat Earth coordinates to body-fixed axis coordinates.

**Data Types:** `double`

### **Vwind** — Wind speed 1-by-3 vector

Wind speed, specified as a 1-by-3 vector, in selected units.

#### Dependencies

To enable this parameter, set **Wind speed
source** to `External`.

**Data Types:** `double`

### **θwind** — Wind direction scalar

Wind direction, specified as a scalar, in degrees. The direction of
the wind is in degrees clockwise from the direction of the Earth
*x*-axis (north). The wind direction is defined as
the direction from which the wind is coming.

#### Dependencies

To enable this parameter, set **Wind direction
source** to `External`.

**Data Types:** `double`
### Output

### **Vwind** — Wind velocity 3-by-3 matrix

Wind velocity, returned as a three-element signal in the same body coordinate reference
as the **DCM** input, in specified units.

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
| **Values**: `'Metric (MKS)'` | `'English (Velocity in kts)'` | `'English (Velocity in ft/s)'` |
| **Default**: `'Metric (MKS)'` |

### **Wind speed source** — Wind speed source `Internal` (default) | `External`

Wind speed source, specified as:

|  |  |
| --- | --- |
| `External` | Variable wind speed input to block |
| `Internal` | Constant wind speed specified in mask |

#### Dependencies

- Setting this parameter to `Internal`
  enables **Wind speed at altitude**.
- Setting this parameter to `External`
  enables the **Vwind**
  input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Vw_source` |
| **Type**: character vector |
| **Values**: `'Internal'` | `'External'` |
| **Default**: `'Internal'` |

### **Wind speed at altitude (m/s)** — Wind speed `15` (default) | scalar

Constant wind speed, specified as a double scalar, in specified
units.

#### Dependencies

To enable this parameter, set **Wind speed source**
to `Internal`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Vwind` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'15'` |

### **Wind direction source** — Wind direction source `Internal` (default) | `External`

Wind direction source, specified as:

|  |  |
| --- | --- |
| `External` | Variable wind direction input to block |
| `Internal` | Constant wind direction specified in mask |

#### Dependencies

- Setting this parameter to `Internal`
  enables **Wind direction at altitude (degrees clockwise
  from north)**.
- Setting this parameter to `External`
  enables the **θwind**
  input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `W_source` |
| **Type**: character vector |
| **Values**: `'Internal'` | `'External'` |
| **Default**: `'Internal'` |

### **Wind direction at altitude (degrees clockwise from north)** — Wind direction `0` (default)

Constant wind direction, specified as a scalar, in degrees clockwise from
the direction of the Earth *x*-axis (north). The wind
direction is the direction from which the wind is coming.

#### Dependencies

To enable this parameter, set **Wind direction
source** to `Internal`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wdeg` |
| **Type**: character vector |
| **Values**: scalar |
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

Transform horizontal wind into body-axes coordinates

The Horizontal Wind Model block computes the wind velocity in
body-axes coordinates.

The wind is specified by wind speed and wind direction in Earth
axes. The speed and direction can be constant or variable over time.
The direction of the wind is in degrees clockwise from the direction
of the Earth *x*-axis (north). The wind direction is defined as the direction from which the wind is coming. Using the direction cosine matrix (DCM), the wind velocities are transformed into body-axes coordinates.
