---
type: simulink-block
title: 'Non-Standard Day 310'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Atmosphere'
documentation_page: 'nonstandardday310'
documentation_source_path: 'nonstandardday310.html'
language: en
---

# Non-Standard Day 310

## Ports

### Input

### **Port\_1** — Geopotential height scalar | array

Geopotential height, specified as a scalar or array, in specified units.

**Data Types:** `double`
### Output

### **Port\_1** — Temperature scalar | array

Temperature, specified as a scalar or array, in specified units.

**Data Types:** `double`

### **Port\_2** — Speed of sound scalar | array

Speed of sound, specified as a scalar or array, in specified units.

**Data Types:** `double`

### **Port\_3** — Air pressure scalar | array

Air pressure, specified as a scalar or array, in specified units.

**Data Types:** `double`

### **Port\_4** — Air density scalar | array

Air density, specified as a scalar or array, in specified units.

**Data Types:** `double`

## Parameters

### **Units** — Input and output units `Metric (MKS)` (default) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

Input and output units, specified as:

| Units | Height | Temperature | Speed of Sound | Air Pressure | Air Density |
| --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | Meters | Kelvin | Meters per second | Pascal | Kilograms per cubic meter |
| `English (Velocity in ft/s)` | Feet | Degrees Rankine | Feet per second | Pound-force per square inch | Slug per cubic foot |
| `English (Velocity in kts)` | Feet | Degrees Rankine | Knots | Pound-force per square inch | Slug per cubic foot |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **Default**: `'Metric (MKS)'` |

### **Specification** — Atmosphere model type `1976 COESA-extended U.S. Standard Atmosphere` (default) | `MIL-HDBK-310` | `MIL-STD-210C`

Atmosphere model type, specified as `1976 COESA-extended U.S. Standard
Atmosphere`, `MIL-HDBK-310`, or
`MIL-STD-210C`. For the
`MIL-HDBK-310` and `MIL-STD-210C`
options:

|  |  |
| --- | --- |
| `MIL-HDBK-310` | This selection is linked to the Non-Standard Day 310 block. See the block reference for more information. Selecting `MIL-HDBK-310` enables the parameters **Atmospheric model type**, **Extreme parameter**, **Frequency of occurrence**, and **Altitude of extreme value**. |
| `MIL-STD-210C` | This selection is linked to the Non-Standard Day 210C block. See the block reference for more information. Selecting `MIL-HDBK-310` enables the parameters **Atmospheric model type**, **Extreme parameter**, **Frequency of occurrence**, and **Altitude of extreme value**. |

#### Dependencies

Selecting `MIL-HDBK-310` or
`MIL-STD-210C` enables these parameters:

- **Atmospheric model type**
- **Extreme parameter**
- **Frequency of occurrence**
- **Altitude of extreme value**

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `spec` |
| **Type**: character vector |
| **Values**: `'1976 COESA-extended U.S. Standard Atmosphere'` | `'MIL-HDBK-310'` | `'MIL-STD-210C'` |
| **Default**: `'1976 COESA-extended U.S. Standard Atmosphere'` |

### **Atmospheric model type** — Model type `Profile` (default) | `Envelope`

Representation of atmospheric model type, specified as:

|  |  |
| --- | --- |
| `Profile` | Realistic atmospheric profiles associated with extremes at specified altitudes. Recommended for simulation of vehicles vertically traversing the atmosphere or when the total influence of the atmosphere is needed. |
| `Envelope` | Uses extreme atmospheric values at each altitude. Recommended for vehicles only horizontally traversing the atmosphere without much change in altitude. |

#### Dependencies

- Selecting `MIL-HDBK-310` or
  `MIL-STD-210C` for the
  **Specification** parameter enables this parameter.
- Selecting `Profile` enables the **Attitude of
  extreme value** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `model` |
| **Type**: character vector |
| **Values**: `'Profile'` | `'Envelope'` |
| **Default**: `'Profile'` |

### **Extreme parameter** — Model type `High temperature` (default) | `Low temperature` | `High density` | `Low density` | `High pressure` | `Low pressure`

Atmospheric parameter that is the extreme value.

#### Dependencies

- Selecting `MIL-HDBK-310` or
  `MIL-STD-210C` for the
  **Specification** parameter enables this parameter.
- The `High pressure` and `Low pressure`
  options appear only when **Atmospheric model type** is set to
  `Envelope`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `profile_var` |
| **Type**: character vector |
| **Values**: `'High temperature'` | `'Low temperature'` | `'High density'` | `'Low density'` | `'High pressure'` | `'Low pressure'` |
| **Default**: `'High temperature'` |

### **Frequency of occurrence** — Model type `1%` (default) | `Extreme values` | `5%` | `10%` | `20%`

Percent of time the values would occur.

#### Dependencies

- Selecting `MIL-HDBK-310` or
  `MIL-STD-210C` for the
  **Specification** parameter enables this parameter.
- `Extreme values`, `5%`, and
  `20%` are available only when
  `Envelope` is selected for **Atmospheric
  model type**.
- `1%` and `10%` are always
  available.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `profile_percent` |
| **Type**: character vector |
| **Values**: `'Extreme values'` | `'1%'` | `'5%'` | `'10%'` | `'20%'` |
| **Default**: `'1%'` |

### **Altitude of extreme value** — Geometric altitude `5 km (16404 ft)` (default) | `10 km (32808 ft)` | `20 km (65617 ft)` | `30 km (98425 ft)` | `40 km (131234 ft)`

Geometric altitude at which the extreme values occur, specified as `5 km
(16404 ft)`, `10 km (32808 ft)`, `20 km (65617
ft)`, `30 km (98425 ft)`, or `40 km (131234
ft)`.

#### Dependencies

This parameter appears if the **Atmospheric model type** is set
to `Profile`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `profile_alt` |
| **Type**: character vector |
| **Values**: `5 km (16404 ft)` | `10 km (32808 ft)` | `20 km (65617 ft)` | `30 km (98425 ft)` | `40 km (131234 ft)` |
| **Default**: `40 km (131234 ft)` |

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

## Libraries

Aerospace Blockset / Environment / Atmosphere

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Implement MIL-HDBK-310 climatic data

The Non-Standard Day 310 block implements a portion of the climatic
data of the MIL-HDBK-310 worldwide air environment to 80 km (geometric or approximately
262,467 feet geometric) for absolute temperature, pressure, density, and speed of sound for
the input geopotential altitude.

The COESA Atmosphere Model, Non-Standard Day 210C, and
Non-Standard Day 310 blocks are identical blocks. When configured for
COESA Atmosphere Model, the block implements the COESA mathematical
representation. When configured for Non-Standard Day 210C, the block implements
MIL-STD-210C climatic data. When configured for Non-Standard Day 310, the block
implements MIL-HDBK-310 climatic data.

The COESA Atmosphere Model block port labels change based on the input and
output units selected from the **Units** list.
