---
type: simulink-block
title: 'Pressure Altitude'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Atmosphere'
documentation_page: 'pressurealtitude'
documentation_source_path: 'pressurealtitude.html'
language: en
---

# Pressure Altitude

## Ports

### Input

### **Port\_1** — Static pressure scalar | array

Static pressure, specified as a scalar or array.

**Data Types:** `double`
### Output

### **Port\_1** — Pressure altitude scalar | array

Pressure altitude, returned as a scalar or vector.

**Data Types:** `double`

## Parameters

### **Units** — Input units `Metric (MKS)` (default) | `English`

Input units, specified as:

| Units | Pstatic | Alt\_p |
| --- | --- | --- |
| `Metric (MKS)` | Pascal | Meters |
| `English` | Pound force per square inch | Feet |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English'` |
| **Default**: `'Metric (MKS)'` |

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

Calculate pressure altitude based on ambient pressure

The Pressure Altitude block computes the pressure altitude
based on ambient pressure. Pressure altitude is the altitude in the 1976 Committee on
the Extension of the Standard Atmosphere (COESA) United States with specified ambient
pressure.

Pressure altitude is also known as the mean sea level (MSL) altitude.

The Pressure Altitude block icon port label change based on the input and
output units selected from the **Units** list.
