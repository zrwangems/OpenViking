---
type: simulink-block
title: 'Dryden Wind Turbulence Model (Discrete)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Wind'
documentation_page: 'drydenwindturbulencemodeldiscrete'
documentation_source_path: 'drydenwindturbulencemodeldiscrete.html'
language: en
---

# Dryden Wind Turbulence Model (Discrete)

## Ports

### Input

### **h** — Altitude scalar

Altitude, specified as a scalar, in selected units.

**Data Types:** `double`

### **V** — Aircraft speed scalar

Aircraft speed, specified as a scalar, in selected units.

**Data Types:** `double`

### **DCM** — Direction cosine matrix 3-by-3 matrix

Direction cosine matrix, specified as a 3-by-3 matrix representing the flat Earth coordinates
to body-fixed axis coordinates.

**Data Types:** `double`
### Output

### **Vwind** — Turbulence velocities three-element vector

Turbulence velocities, returned as a three-element vector in the same body
coordinate reference as the **DCM** input, in specified
units.

**Data Types:** `double`

### **ωwind** — Turbulence angular rates three-element vector

Turbulence angular rates, specified as a three-element vector, in radians per second.

**Data Types:** `double`

## Parameters

### **Units** — Wind speed units `Metric (MKS)` (default) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

Units of wind speed due to turbulence, specified as:

| Units | Wind Velocity | Altitude | Air Speed |
| --- | --- | --- | --- |
| `Metric (MKS)` | Meters/second | Meters | Meters/second |
| `English (Velocity in ft/s)` | Feet/second | Feet | Feet/second |
| `English (Velocity in kts)` | Knots | Feet | Knots |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **Default**: `'Metric (MKS)'` |

### **Specification** — Military reference `MIL-F-8785C` (default) | `MIL-HDBK-1797` | `MIL-HDBK-1797B`

Military reference, which affects the application of turbulence scale lengths in the lateral and vertical directions, specified as `MIL-F-8785C`, `MIL-HDBK-1797`, or `MIL-HDBK-1797B`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `spec` |
| **Type**: character vector |
| **Values**: `'MIL-F-8785C'` | `'MIL-HDBK-1797'` | `'MIL-HDBK-1797B'` |
| **Default**: `'MIL-F-8785C'` |

### **Model type** — Turbulence model `Discrete Dryden (+q +r)` (default) | `Continuous Von Karman (+q +r)` | `Continuous Von Karman (-q +r)` | `Continuous Dryden (+q -r)` | `Continuous Dryden (+q +r)` | `Continuous Dryden (-q +r)` | `Discrete Dryden (+q -r)` | `Continuous Von Karman (+q -r)` | `Discrete Dryden (-q +r)`

Select the wind turbulence model to use:

|  |  |
| --- | --- |
| `Continuous Von Karman (+q -r)` | Use continuous representation of Von Kármán velocity spectra with positive vertical and negative lateral angular rates spectra. |
| `Continuous Von Karman (+q +r)` | Use continuous representation of Von Kármán velocity spectra with positive vertical and lateral angular rates spectra. |
| `Continuous Von Karman (-q +r)` | Use continuous representation of Von Kármán velocity spectra with negative vertical and positive lateral angular rates spectra. |
| `Continuous Dryden (+q -r)` | Use continuous representation of Dryden velocity spectra with positive vertical and negative lateral angular rates spectra. |
| `Continuous Dryden (+q +r)` | Use continuous representation of Dryden velocity spectra with positive vertical and lateral angular rates spectra. |
| `Continuous Dryden (-q +r)` | Use continuous representation of Dryden velocity spectra with negative vertical and positive lateral angular rates spectra. |
| `Discrete Dryden (+q -r)` | Use discrete representation of Dryden velocity spectra with positive vertical and negative lateral angular rates spectra. |
| `Discrete Dryden (+q +r)` | Use discrete representation of Dryden velocity spectra with positive vertical and lateral angular rates spectra. |
| `Discrete Dryden (-q +r)` | Use discrete representation of Dryden velocity spectra with negative vertical and positive lateral angular rates spectra. |

The Discrete Dryden selections conform to the transfer function
descriptions.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `model` |
| **Type**: character vector |
| **Values**: `'Continuous Von Karman (+q +r)'` | `'Continuous Von Karman (-q +r)'` | `'Continuous Dryden (+q -r)'` | `'Continuous Dryden (+q +r)'` | `'Continuous Dryden (-q +r)'` | `'Discrete Dryden (+q -r)'` | `'Discrete Dryden (+q +r)'` | `'Discrete Dryden (-q +r)'` |
| **Default**: `'Discrete Dryden (+q +r)'` |

### **Wind speed at 6 m defines the low altitude intensity** — Measured wind speed `15` (default) | real scalar

Measured wind speed at a height of 20 feet (6 meters), specified as a real scalar, which
provides the intensity for the low-altitude turbulence model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `W20` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'15'` |

### **Wind direction at 6 m (degrees clockwise from north)** — Measured wind direction `0` (default) | real scalar

Measured wind direction at a height of 20 feet (6 meters), specified as a real scalar, which
is an angle to aid in transforming the low-altitude turbulence model into a body
coordinates.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wdeg` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'0'` |

### **Probability of exceedance of high-altitude intensity** — Turbulence intensity `10^-2 - Light` (default) | `10^-1` | `2x10^-1` | `10^-3 - Moderate` | `10^-4` | `10^-5 - Severe` | `10^-6`

Probability of the turbulence intensity being exceeded, specified as `10^-2 - Light`, `10^-1`, `2x10^-1`, `10^-3 - Moderate`, `10^-4`, `10^-5 - Severe`, or `10^-6`. Above 2000 feet, the turbulence intensity is determined from a lookup table that gives the turbulence intensity as a function of altitude and the probability of the turbulence intensity being exceeded.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TurbProb` |
| **Type**: character vector |
| **Values**: `'2x10^-1'` | `'10^-1'` | `'10^-2 - Light'` | `'10^-3 - Moderate'` | `'10^-4'` | `'10^-5 - Severe'` | `'10^-6'` |
| **Default**: `'10^-2 - Light'` |

### **Scale length at medium/high altitudes (m)** — Turbulence scale length `533.4` (default) | real scalar

Turbulence scale length above 2000 feet, specified as a real scalar, which is assumed
constant. From the military references, a figure of 1750 feet is recommended
for the longitudinal turbulence scale length of the Dryden spectra.

**Note**

An alternate scale length value changes the power spectral density
asymptote and gust load.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `L_high` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'533.4'` |

### **Wingspan** — Wingspan `10` (default) | real scalar

Wingspan, specified as a real scalar, which is required in the calculation of the turbulence
on the angular rates.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Wingspan` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'10'` |

### **Band limited noise sample time (seconds)** — Noise sample time `0.1` (default) | real scalar

Noise sample time, specified as a real scalar, at which the unit variance white noise signal is generated.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ts` |
| **Type**: character vector |
| **Values**: real scalar |
| **Default**: `'0.1'` |

### **Random noise seeds** — Noise seeds [ug vg wg pg] `[23341 23342 23343 23344]` (default) | four-element vector

Random noise seeds, specified as a four-element vector, which are used to generate the
turbulence signals, one for each of the three velocity components and one for the roll
rate:

The turbulences on the pitch and yaw angular rates are based on further shaping of the outputs from the shaping filters for the vertical and lateral velocities.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Seed` |
| **Type**: character vector |
| **Values**: four-element vector |
| **Default**: `'[23341 23342 23343 23344]'` |

### **Turbulence on** — Turbulence signals `on` (default) | `off`

To generate the turbulence signals, select this check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `T_on` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

## Libraries

Aerospace Blockset / Environment / Wind

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Generate discrete wind turbulence with Dryden velocity spectra

The Dryden Wind Turbulence Model (Discrete) block uses the
Dryden spectral representation to add turbulence to the aerospace model by using
band-limited white noise with appropriate digital filter finite difference equations.
This block implements the mathematical representation in the Military Specification
MIL-F-8785C, Military Handbook MIL-HDBK-1797, and Military Handbook MIL-HDBK-1797B. For
more information, see Algorithms.
