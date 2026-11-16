---
type: simulink-block
title: 'Force Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'forceconversion'
documentation_source_path: 'forceconversion.html'
language: en
---

# Force Conversion

## Ports

### Input

### **Port\_1** — Force scalar | array

Force, specified as a scalar or array, in initial force units.

#### Dependencies

The input port label depends on the **Initial
unit** setting.

**Data Types:** `double`
### Output

### **Port\_1** — Force scalar | array

Force, returned as a scalar or array, in final force units.

#### Dependencies

The output port label depends on the **Final
unit** setting.

**Data Types:** `double`

## Parameters

### **Initial unit** — Input units `lbf` (default) | `N`

Input units, specified as:

|  |  |
| --- | --- |
| `lbf` | Pound force |
| `N` | Newtons |

#### Dependencies

The input port label depends on the **Initial unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IU` |
| **Type**: character vector |
| **Values**: `lbf` | `N` |
| **Default**: `lbf` |

### **Final unit** — Output units `N` (default) | `lbf`

Output units, specified as:

|  |  |
| --- | --- |
| `lbf` | Pound force |
| `N` | Newtons |

#### Dependencies

The output port label depends on the **Final unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OU` |
| **Type**: character vector |
| **Values**: `lbf` | `N` |
| **Default**: `N` |

## Libraries

Aerospace Blockset / Utilities / Unit Conversions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Convert from force units to desired force units

The Force Conversion block computes the conversion factor
from specified input force units to specified output force units and applies the
conversion factor to the input signal.

The Force Conversion block port labels change based on the input and output
units selected from the **Initial unit** and the **Final unit** lists.
