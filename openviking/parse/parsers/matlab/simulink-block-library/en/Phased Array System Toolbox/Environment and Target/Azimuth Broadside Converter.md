---
type: simulink-block
title: 'Azimuth Broadside Converter'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Environment and Target'
documentation_page: 'azimuthbroadsideconverter'
documentation_source_path: 'ref/azimuthbroadsideconverter.html'
language: en
---

# Azimuth Broadside Converter

## Ports
```yaml
ports:
- name: az
  summary: Azimuth angle scalar | vector of real-values
  direction: input
  data_types: double
- name: bsd
  summary: Broadside angle scalar | vector of real-values
  direction: input
  data_types: double
- name: el
  summary: Elevation angle scalar | vector of real-values
  direction: input
  data_types: double
- name: az
  summary: Azimuth angle scalar | vector of real-values
  direction: output
  data_types: double
- name: bsd
  summary: Broadside angle scalar | vector of real-values
  direction: output
  data_types: double
```

### Input

### **az** — Azimuth angle scalar | vector of real-values

Azimuth angle of direction, specified as a scalar or vector of
real-values. Units are in degrees. When `az` is a
vector, the dimensions of `az` and
`el` must match.

#### Dependencies

To enable this port, set **Conversion Mode** to
**azimuth -> broadside**.

**Data Types:** `double`

### **bsd** — Broadside angle scalar | vector of real-values

Broadside angle of direction, specified as a scalar or vector of
real-values. Units are in degrees. When `bsd` is a
vector, the dimensions of `bsd` and
`el` must match.

#### Dependencies

To enable this port, set **Conversion Mode** to
**broadside -> azimuth**.

**Data Types:** `double`

### **el** — Elevation angle scalar | vector of real-values

Elevation angle of direction, specified as a scalar or vector of
real-values. Units are in degrees. The dimensions of
`el` must match the dimensions of
`az` and `bsd`.

**Data Types:** `double`
### Output

### **az** — Azimuth angle scalar | vector of real-values

Azimuth angle of direction, returned as a scalar or vector of
real-values. Units are in degrees.

#### Dependencies

To enable this port, set **Conversion Mode** to
**broadside -> azimuth**.

**Data Types:** `double`

### **bsd** — Broadside angle scalar | vector of real-values

Broadside angle of direction, returned as a scalar or vector of
real-values. Units are in degrees.

#### Dependencies

To enable this port, set **Conversion Mode** to
**azimuth -> broadside**.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Conversion mode
  summary: Angle conversion type broadside -> azimuth (default) | azimuth -> broadside
  group: ''
```

### **Conversion mode** — Angle conversion type **broadside -> azimuth** (default) | **azimuth -> broadside**

Angle conversion type, specified as

|  |  |
| --- | --- |
| **broadside -> azimuth** | Convert direction expressed in broadside and elevation angles to azimuth and elevation angles. |
| **azimuth -> broadside** | Convert direction expressed in azimuth and elevation angles to broadside and elevation angles. |
## Libraries

Phased Array System Toolbox / Environment and Target

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Convert azimuth angle to broadside angle or broadside angle to azimuth angle

The Azimuth Broadside Converter block converts an angle direction
expressed in terms of Broadside Angles into the equivalent azimuth angle or converts from
azimuth angle into the equivalent broadside angle. In both cases, you must specify the
elevation angle.
