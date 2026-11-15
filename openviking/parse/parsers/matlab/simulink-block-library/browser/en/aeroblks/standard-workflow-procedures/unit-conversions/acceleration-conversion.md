---
type: simulink-block
title: 'Acceleration Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Unit Conversions'
documentation_page: 'accelerationconversion'
documentation_source_path: 'accelerationconversion.html'
language: en
---

# Acceleration Conversion

## Ports

### Input

### **Port\_1** — Acceleration scalar | array

Acceleration, specified as a scalar or array, in initial acceleration units.

#### Dependencies

The input port label depends on the **Initial
unit** setting.

**Data Types:** `double`
### Output

### **Port\_1** — Acceleration scalar | array

Acceleration, returned as a scalar or array, in final acceleration units.

#### Dependencies

The output port label depends on the **Final
unit** setting.

**Data Types:** `double`

## Parameters

### **Initial unit** — Input units `ft/ss` (default) | `m/s2` | `km/s2` | `in/s2` | `km/h-s` | `mph/s` | `G's`

Input units, specified as:

|  |  |
| --- | --- |
| `m/s`2 | Meters per second squared |
| `ft/s`2 | Feet per second squared |
| `km/s`2 | Kilometers per second squared |
| `in/s`2 | Inches per second squared |
| `km/h-s` | Kilometers per hour per second |
| `mph-s` | Miles per hour per second |
| `G's` | g-units |

#### Dependencies

The input port label depends on the **Initial unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IU` |
| **Type**: character vector |
| **Values**: `'ft/s^s` | `'m/s^2'` | `'km/s^2'` | `'in/s^2'` | `'km/h-s'` | `'mph/s'` | `'G's'` |
| **Default**: `'ft/s2'` |

### **Final unit** — Output units `ft/s^2'` (default) | `m/s^2` | `km/s^2` | `in/s^2` | `km/h-s` | `mph/s` | `G's`

Output units, specified as:

|  |  |
| --- | --- |
| `m/s`2 | Meters per second squared |
| `ft/s`2 | Feet per second squared |
| `km/s`2 | Kilometers per second squared |
| `in/s`2 | Inches per second squared |
| `km/h-s` | Kilometers per hour per second |
| `mph-s` | Miles per hour per second |
| `G's` | g-units |

#### Dependencies

The output port label depends on the **Final unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OU` |
| **Type**: character vector |
| **Values**: `'ft/s^2'` | `'m/s^2'` | `'km/s^2'` | `'in/s^2'` | `'km/h-s'` | `'mph/s'` | `'G's'` |
| **Default**: `'ft/s2'` |

## Libraries

Aerospace Blockset / Utilities / Unit Conversions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Convert from acceleration units to desired acceleration units

The Acceleration Conversion block computes the conversion
factor from specified input acceleration units to specified output acceleration units
and applies the conversion factor to the input signal.

The Acceleration Conversion block port labels change based on the input and
output units selected from the **Initial unit** and
**Final unit** parameters.
