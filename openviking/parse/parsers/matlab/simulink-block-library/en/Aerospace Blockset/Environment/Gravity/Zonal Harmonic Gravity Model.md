---
type: simulink-block
title: 'Zonal Harmonic Gravity Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Gravity'
documentation_page: 'zonalharmonicgravitymodel'
documentation_source_path: 'zonalharmonicgravitymodel.html'
language: en
---

# Zonal Harmonic Gravity Model

## Ports
```yaml
ports:
- name: Xecef
  summary: Planet-centered planet-fixed coordinates m-by-3 matrix
  direction: input
  data_types: double
- name: gecef
  summary: Gravity values m-by-3 array
  direction: output
  data_types: double
```

### Input

### **Xecef** — Planet-centered planet-fixed coordinates m-by-3 matrix

Planet-centered planet-fixed coordinates, specified as an
*m*-by-3 matrix, from the center of the planet in
the selected length units. If **Planet model** has a
value of `Earth`, this matrix contains Earth-centered
Earth-fixed (ECEF) coordinates.

**Data Types:** `double`
### Output

### **gecef** — Gravity values m-by-3 array

Gravity values, returned as an *m*-by-3 array, in the
*x*-axis, *y*-axis and
*z*-axis of the planet-centered planet-fixed
coordinates, in the selected length units per second squared.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Units
  summary: Input units Metric (MKS) (default) | English
  group: ''
  block_parameter: units
  type: character vector
  values: '''Metric (MKS)'' | ''English'''
  default: '''Metric (MKS)'''
- name: Degree
  summary: Degree of harmonic model 4 (default) | 2 | 3
  group: ''
  block_parameter: degree
  type: character vector
  values: '''2'' | ''3'' | ''4'''
  default: '''4'''
- name: Action for out-of-range input
  summary: Out-of-range input behavior Warning (default) | ErrorNone
  group: ''
  block_parameter: action
  type: character vector
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''Warning'''
- name: Planet model
  summary: Planetary model Mercury (default) | Venus | Earth | Moon | Mars | Jupiter | Saturn | Uranus | Neptune | Custom
  group: ''
  block_parameter: ptype
  type: character vector
  values: '''Mercury'' | ''Venus'' | ''Earth'' | ''Moon'' | ''Mars'' | ''Jupiter'' | ''Saturn'' | ''Uranus'' | ''Neptune''
    | ''Custom'''
  default: '''Earth'''
- name: Equatorial radius
  summary: Planetary equatorial radius 6378136.3 (default) | scalar
  group: ''
  block_parameter: R
  type: character vector
  values: scalar
  default: '''6378136.3'''
- name: Gravitational parameter
  summary: Planetary gravitational parameter 398600441500000 (default) | scalar
  group: ''
  block_parameter: GM
  type: character vector
  values: scalar
  default: '''398600441500000'''
- name: J values
  summary: Zonal harmonic coefficients [1.0826269e-03 -2.5323000e-06 -1.6204000e-06] (default) | 3-element array
  group: ''
  block_parameter: jvalue
  type: character vector
  values: scalar
  default: '''[1.0826269e-03 -2.5323000e-06 -1.6204000e-06]'''
```

### **Units** — Input units `Metric (MKS)` (default) | `English`

Input units, specified as:

| Units | Position | Equatorial Radius | Gravitational Parameter |
| --- | --- | --- | --- |
| `Metric (MKS)` | Meters | Meters | Meters cubed per second squared |
| `English` | Feet | Feet | Feet cubed per second squared |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English'` |
| **Default**: `'Metric (MKS)'` |

### **Degree** — Degree of harmonic model `4` (default) | `2` | `3`

Degree of harmonic model, specified as.

- `2` — Second degree, J2. Most significant or
  largest spherical harmonic term, which accounts for the oblateness
  of a planet.
- `3` — Third degree, J3.
- `4` — Fourth degree, J4 (default).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `degree` |
| **Type**: character vector |
| **Values**: `'2'` | `'3'` | `'4'` |
| **Default**: `'4'` |

### **Action for out-of-range input** — Out-of-range input behavior `Warning` (default) | `Error``None`

Out-of-range input behavior, specified as:

| Value | Description |
| --- | --- |
| `None` | No action. |
| `Warning` | Warning in the Diagnostic Viewer, model simulation continues. |
| `Error` | MATLAB® returns an exception, model simulation stops. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `action` |
| **Type**: character vector |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'Warning'` |

### **Planet model** — Planetary model `Mercury` (default) | `Venus` | `Earth` | `Moon` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Custom`

Planetary model, specified as `Mercury`,
`Venus`, `Earth`,
`Moon`, `Mars`,
`Jupiter`, `Saturn`,
`Uranus`, `Neptune`, or
`Custom`.

Selecting `Custom` enables you to specify your own
planetary model.

- Selecting `Mercury`, `Venus`,
  `Moon`, `Uranus`, or
  `Neptune` limits the degree to
  `2`.
- Selecting `Mars` limits the degree to
  `3`.

#### Dependencies

Selecting `Custom` enables the
**Equatorial radius**, **Gravitational
parameter** and **J values rate**
parameters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ptype` |
| **Type**: character vector |
| **Values**: `'Mercury'` | `'Venus'` | `'Earth'` | `'Moon'` | `'Mars'` | `'Jupiter'` | `'Saturn'` | `'Uranus'` | `'Neptune'` | `'Custom'` |
| **Default**: `'Earth'` |

### **Equatorial radius** — Planetary equatorial radius `6378136.3` (default) | scalar

Planetary equatorial radius, specified as a scalar, in the length units
that the **Units** parameter defines.

#### Dependencies

To enable this parameter, set **Planet model** to
`Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `R` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'6378136.3'` |

### **Gravitational parameter** — Planetary gravitational parameter `398600441500000` (default) | scalar

Planetary gravitational parameter, specified as a scalar, in the length
units cubed per second squared that the **Units** parameter
defines.

#### Dependencies

To enable this parameter, set **Planet model** to
`Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GM` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'398600441500000'` |

### **J values** — Zonal harmonic coefficients `[1.0826269e-03 -2.5323000e-06 -1.6204000e-06]` (default) | 3-element array

Zonal harmonic coefficient, specified as a 3-element array.

#### Dependencies

To enable this parameter, set **Planet model** to
`Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `jvalue` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'[1.0826269e-03 -2.5323000e-06 -1.6204000e-06]'` |
## Libraries

Aerospace Blockset / Environment / Gravity

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2009b**

## Description

Calculate zonal harmonic representation of planetary gravity

The Zonal Harmonic Gravity Model block calculates the zonal harmonic
representation of planetary gravity at a specific location based on planetary
gravitational potential. This block provides a convenient way to describe the
gravitational field of a planet outside its surface.

By default, the block uses the fourth order zonal coefficient for Earth to calculate the zonal harmonic gravity. It also allows you to specify the second or third zonal coefficient.

For information on the planetary parameter values for each planet in the block
implementation, see Algorithms.
