---
type: simulink-block
title: 'Density Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'densityconversion'
documentation_source_path: 'densityconversion.html'
language: en
---

# Density Conversion

## Ports
```yaml
ports:
- name: Port_1
  summary: Density scalar | array
  direction: input
  data_types: double
- name: Port_1
  summary: Density scalar | array
  direction: output
  data_types: double
```

### Input

### **Port\_1** — Density scalar | array

Contains the density, specified as a scalar or array, in initial density units.

#### Dependencies

The input port label depends on the **Initial
unit** setting.

**Data Types:** `double`
### Output

### **Port\_1** — Density scalar | array

Contains the density, returned as a scalar or array, in initial density units.

#### Dependencies

The output port label depends on the **Final
unit** setting.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Initial unit
  summary: Input units lbm/ft^3 (default) | kg/m^3 | slug/ft^3 | lbm/in^3
  group: ''
  block_parameter: IU
  type: character vector
  values: '''lbm/ft^3'' | ''kg/m^3'' | ''slug/ft^3'' | ''lbm/in^3'''
  default: '''lbm/ft^3'''
- name: Final unit
  summary: Output units kg/m^3 (default) | lbm/ft^3 | slug/ft^3 | lbm/in^3
  group: ''
  block_parameter: OU
  type: character vector
  values: '''lbm/ft^3'' | ''kg/m^3'' | ''slug/ft^3'' | ''lbm/in^3'''
  default: '''kg/m^3'''
```

### **Initial unit** — Input units `lbm/ft^3` (default) | `kg/m^3` | `slug/ft^3` | `lbm/in^3`

Input units, specified as:

|  |  |
| --- | --- |
| `lbm/ft^3` | Pound mass per cubic foot |
| `kg/m^3` | Kilograms per cubic meter |
| `slug/ft^3` | Slugs per cubic foot |
| `lbm/in^3` | Pound mass per cubic inch |

#### Dependencies

The input port label depends on the **Initial unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IU` |
| **Type**: character vector |
| **Values**: `'lbm/ft^3'` | `'kg/m^3'` | `'slug/ft^3'` | `'lbm/in^3'` |
| **Default**: `'lbm/ft^3'` |

### **Final unit** — Output units `kg/m^3` (default) | `lbm/ft^3` | `slug/ft^3` | `lbm/in^3`

Output units, specified as:

|  |  |
| --- | --- |
| `lbm/ft^3` | Pound mass per cubic foot |
| `kg/m^3` | Kilograms per cubic meter |
| `slug/ft^3` | Slugs per cubic foot |
| `lbm/in^3` | Pound mass per cubic inch |

#### Dependencies

The output port label depends on the **Final unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OU` |
| **Type**: character vector |
| **Values**: `'lbm/ft^3'` | `'kg/m^3'` | `'slug/ft^3'` | `'lbm/in^3'` |
| **Default**: `'kg/m^3'` |
## Libraries

Aerospace Blockset / Utilities / Unit Conversions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Convert from density units to desired density units

The Density Conversion block computes the conversion factor
from specified input density units to specified output density units and applies the
conversion factor to the input signal.

The Density Conversion block port labels change based on the input and output
units selected from the **Initial unit** and the **Final unit** lists.
