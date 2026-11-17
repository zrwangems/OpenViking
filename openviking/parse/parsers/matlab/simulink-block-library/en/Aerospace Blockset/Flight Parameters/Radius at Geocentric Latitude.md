---
type: simulink-block
title: 'Radius at Geocentric Latitude'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Parameters'
documentation_page: 'radiusatgeocentriclatitude'
documentation_source_path: 'radiusatgeocentriclatitude.html'
language: en
---

# Radius at Geocentric Latitude

## Ports
```yaml
ports:
- name: λs
  summary: Geocentric latitude scalar | vector
  direction: input
  data_types: double
- name: rs
  summary: Radius scalar | vector
  direction: output
  data_types: double
```

### Input

### **λs** — Geocentric latitude scalar | vector

Geocentric latitude, specified as a scalar or vector, in
degrees.

**Data Types:** `double`
### Output

### **rs** — Radius scalar | vector

Radius of planet at geocentric latitude, returned as a scalar or
vector, in the same units as flattening.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Units
  summary: Output units Metric (MKS) (default) | English
  group: ''
  block_parameter: units
  type: character vector
  values: '''Metric (MKS)'' | ''English'''
  default: '''Metric (MKS)'''
- name: Planet model
  summary: Planet model Earth (WGS84) (default) | Custom
  group: ''
  block_parameter: ptype
  type: character vector
  values: '''Earth (WGS84)'' | ''Custom'''
  default: '''Earth (WGS84)'''
- name: Flattening
  summary: Flattening of planet 1/298.257223563 (default) | scalar
  group: ''
  block_parameter: F
  type: character vector
  values: double scalar
  default: 1/298.257223563
- name: Equatorial radius of planet
  summary: Radius of planet at equator 6378137 (default) | scalar
  group: ''
  block_parameter: R
  type: character vector
  values: double scalar
  default: '6378137'
```

### **Units** — Output units `Metric (MKS)` (default) | `English`

Output units, specified as:

| Units | Equatorial Radius | Radius at Geocentric Latitude |
| --- | --- | --- |
| `Metric (MKS)` | Meters | Meters |
| `English` | Feet | Feet |

#### Dependencies

To enable this parameter, set **Planet model** to
`Earth (WGS84)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English'` |
| **Default**: `'Metric (MKS)'` |

### **Planet model** — Planet model `Earth (WGS84)` (default) | `Custom`

Planet model to use, `Custom` or
`Earth (WGS84)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ptype` |
| **Type**: character vector |
| **Values**: `'Earth (WGS84)'` | `'Custom'` |
| **Default**: `'Earth (WGS84)'` |

### **Flattening** — Flattening of planet `1/298.257223563` (default) | scalar

Flattening of the planet, specified as a double scalar.

#### Dependencies

To enable this parameter, set **Planet
model** to `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `F` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `1/298.257223563` |

### **Equatorial radius of planet** — Radius of planet at equator `6378137` (default) | scalar

Radius of the planet at its equator, in the same units as the desired
units for ECEF position.

#### Dependencies

To enable this parameter, set **Planet
model** to `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `R` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `6378137` |
## Libraries

Aerospace Blockset / Flight Parameters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Estimate radius of ellipsoid planet at geocentric latitude

The Radius at Geocentric Latitude block estimates the radius (rs) of an ellipsoid planet at a particular geocentric latitude (λs).

Ellipsoid planet at a particular geocentric latitude showing the ellipsoid radius, flattening, geocentric latitude, and equatorial radius.

The following equation estimates the ellipsoid radius (rs) using flattening (f¯), geocentric latitude (λ¯s), and equatorial radius (R¯):

rs=R21+[1/(1−f)2−1]sin2λs.
