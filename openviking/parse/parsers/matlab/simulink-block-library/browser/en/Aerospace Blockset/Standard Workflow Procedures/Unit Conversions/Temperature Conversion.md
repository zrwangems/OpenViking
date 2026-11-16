---
type: simulink-block
title: 'Temperature Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Unit Conversions'
documentation_page: 'temperatureconversion'
documentation_source_path: 'temperatureconversion.html'
language: en
---

# Temperature Conversion

## Ports

### Input

### **Port\_1** — Temperature scalar | array

Temperature, specified as a scalar or array, in initial temperature
units.

#### Dependencies

The input port label depends on the **Initial
unit** setting.

**Data Types:** `double`
### Output

### **Port\_1** — Temperature scalar | array

Temperature, returned as a scalar or array, in final temperature
units.

#### Dependencies

The output port label depends on the **Final
unit** setting.

**Data Types:** `double`

## Parameters

### **Initial unit** — Input units `R` (default) | `F` | `C` | `K`

Input units, specified as:

|  |  |
| --- | --- |
| `K` | Kelvin |
| `F` | Degrees Fahrenheit |
| `C` | Degrees Celsius |
| `R` | Degrees Rankine |

#### Dependencies

The input port label depends on the **Initial unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IU` |
| **Type**: character vector |
| **Values**: `'K'` | `'F'` | `'C'` | `'R'` |
| **Default**: `'R'` |

### **Final unit** — Output units `K` (default) | `F` | `C` | `R`

Output units, specified as:

|  |  |
| --- | --- |
| `K` | Kelvin |
| `F` | Degrees Fahrenheit |
| `C` | Degrees Celsius |
| `R` | Degrees Rankine |

#### Dependencies

The output port label depends on the **Final unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OU` |
| **Type**: character vector |
| **Values**: `'K'` | `'F'` | `'C'` | `'R'` |
| **Default**: `'K'` |

## Libraries

Aerospace Blockset / Utilities / Unit Conversions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Convert from temperature units to desired temperature units

The Temperature Conversion block computes the conversion
factor from specified input temperature units to specified output temperature units and
applies the conversion factor to the input signal.

The Temperature Conversion block port labels change based on the input and
output units selected from the **Initial unit** and the
**Final unit** lists.
