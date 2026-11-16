---
type: simulink-block
title: 'Angle Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'angleconversion'
documentation_source_path: 'angleconversion.html'
language: en
---

# Angle Conversion

## Ports

### Input

### **Port\_1** — Angle scalar | array

Angle, specified as a scalar or array, in initial acceleration units.

#### Dependencies

The input port label depends on the **Initial
unit** setting.

**Data Types:** `double`
### Output

### **Port\_1** — Angle scalar | array

Angle, returned as a scalar, in final acceleration units.

#### Dependencies

The output port label depends on the **Final
unit** setting.

**Data Types:** `double`

## Parameters

### **Initial unit** — Input units `deg` (default) | `rad` | `rev`

Input units, specified as:

|  |  |
| --- | --- |
| `deg` | Degrees |
| `rad` | Radians |
| `rev` | Revolutions |

#### Dependencies

The input port label depends on the **Initial unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IU` |
| **Type**: character vector |
| **Values**: `'deg'` | `'rad'` | `'rev'` |
| **Default**: `'deg'` |

### **Final unit** — Output units `rad` (default) | `deg` | `rev`

Output units, specified as:

|  |  |
| --- | --- |
| `deg` | Degrees |
| `rad` | Radians |
| `rev` | Revolutions |

#### Dependencies

The output port label depends on the **Final unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OU` |
| **Type**: character vector |
| **Values**: `'deg'` | `'rad'` | `'rev'` |
| **Default**: `'rad'` |

## Libraries

Aerospace Blockset / Utilities / Unit Conversions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Convert from angle units to desired angle units

The Angle Conversion block computes the conversion factor
from specified input angle units to specified output angle units and applies the
conversion factor to the input signal.

The Angle Conversion block port labels change based on the input and output
units selected from the **Initial unit** and the **Final unit** lists.
