---
type: simulink-block
title: 'CIRA-86 Atmosphere Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Atmosphere'
documentation_page: 'cira86atmospheremodel'
documentation_source_path: 'cira86atmospheremodel.html'
language: en
---

# CIRA-86 Atmosphere Model

## Ports

### Input

### **Port\_1** — Latitude array

Contains the latitude in degrees (limited to +/-80 degrees).

**Data Types:** `double`

### **Port\_2** — Geopotential heights or pressures array

Contains an `m` array of either:

- Geopotential heights in selected length units
  (**Coordinate type** is
  `GPHeight`)
- Pressures in selected pressure units (**Coordinate
  type** is `Pressure`)

**Data Types:** `double`
### Output

### **Port\_1** — Mean temperature array

Mean temperature, specified as an array, in selected units.

**Data Types:** `double`

### **Port\_2** — Pressures or geopotential heights array

`m` array of either:

- Pressures in selected pressure units (**Coordinate
  type** is `GPHeight`)
- Geopotential heights in selected length units
  (**Coordinate type** is
  `Pressure`)

**Data Types:** `double`

### **Port\_3** — Mean zonal winds array

Mean zonal winds, specified as an array, in selected units.

**Data Types:** `double`

## Parameters

### **Units** — Units `Metric (MKS)` (default) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

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

### **Coordinate type** — Coordinate type representation `Pressure` (default) | `GPHeight`

Coordinate type representation, specified as:

- `Pressure`

  Indicates pressure in pascal.
- `GPHeight`

  Indicates geopotential height in meters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ctype` |
| **Type**: character vector |
| **Values**: `'GPHeight'` | `'Pressure'` |
| **Default**: `'GPHeight'` |

### **Mean value type** — Mean value types `Monthly` (default) | `Annual`

Mean value types, specified as:

- `Monthly`

  Indicates monthly values. If you select
  `Monthly`, you must also set the
  **Month** parameter.
- `Annual`

  Indicates annual values. Valid when **Coordinate
  type** has a value of
  `Pressure`.

#### Dependencies

Setting this parameter to `Monthly` enables
the **Month** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mtype` |
| **Type**: character vector |
| **Values**: `'Monthly'` | `'Annual'` |
| **Default**: `'Monthly'` |

### **Month** — Month of mean value `January` (default) | `February` | `March` | `April` | `May` | `June` | `July` | `August` | `September` | `October` | `November` | `December`

Month in which the mean values are taken.

#### Dependencies

This parameter is enabled when **Mean value type**
is set to `Monthly`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `month` |
| **Type**: character vector |
| **Values:** `'January'` | `'February'` | `'March'` | `'April'` | `'May'` | `'June'` | `'July'` | `'August'` | `'September'` | `'October'` | `'November'` | `'December'` |
| **Default**: `'January'` |

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

**Introduced in R2007b**

### R2023b: CIRA-86 Atmosphere Model Block Update

The CIRA-86 Atmosphere Model block has been updated to take action
when inputs to the function are outside the CIRA 1986 model limitations (see Limitations).

## Description

Implement mathematical representation of 1986 CIRA atmosphere

The CIRA-86 Atmosphere Model block implements the
mathematical representation of the 1986 Committee on Space Research (COSPAR)
International Reference Atmosphere (CIRA). The block provides values for mean
temperature, pressure, and zonal wind speed for the input geopotential altitude.

The CIRA-86 Atmosphere Model block port labels change based on the input and
output units selected from the **Units** list.
