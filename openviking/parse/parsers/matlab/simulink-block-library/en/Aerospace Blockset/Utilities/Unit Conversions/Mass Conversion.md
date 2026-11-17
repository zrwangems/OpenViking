---
type: simulink-block
title: 'Mass Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'massconversion'
documentation_source_path: 'massconversion.html'
language: en
---

# Mass Conversion

## Ports
```yaml
ports:
- name: Port_1
  summary: Mass scalar | array
  direction: input
  data_types: double
- name: Port_1
  summary: Mass scalar | array
  direction: output
  data_types: double
```

### Input

### **Port\_1** — Mass scalar | array

Mass, specified as a scalar or array, in initial mass units.

#### Dependencies

The input port label depends on the **Initial
unit** setting.

**Data Types:** `double`
### Output

### **Port\_1** — Mass scalar | array

Mass, returned as a scalar or array, in final mass units.

#### Dependencies

The output port label depends on the **Final
unit** setting.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Initial unit
  summary: Input units lbm (default) | kg | slug
  group: ''
  block_parameter: IU
  type: character vector
  values: '''lbm'' | ''kg'' | ''slug'''
  default: '''lbm'''
- name: Final unit
  summary: Output units kg (default) | lbm | slug
  group: ''
  block_parameter: OU
  type: character vector
  values: '''lbm'' | ''kg'' | ''slug'''
  default: '''kg'''
```

### **Initial unit** — Input units `lbm` (default) | `kg` | `slug`

Input units, specified as:

|  |  |
| --- | --- |
| `lbm` | Pound mass |
| `kg` | Kilograms |
| `slug` | Slugs |

#### Dependencies

The input port label depends on the **Initial unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IU` |
| **Type**: character vector |
| **Values**: `'lbm'` | `'kg'` | `'slug'` |
| **Default**: `'lbm'` |

### **Final unit** — Output units `kg` (default) | `lbm` | `slug`

Output units, specified as:

|  |  |
| --- | --- |
| `lbm` | Pound mass |
| `kg` | Kilograms |
| `slug` | Slugs |

#### Dependencies

The output port label depends on the **Final unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OU` |
| **Type**: character vector |
| **Values**: `'lbm'` | `'kg'` | `'slug'` |
| **Default**: `'kg'` |
## Libraries

Aerospace Blockset / Utilities / Unit Conversions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Convert from mass units to desired mass units

The Mass Conversion block computes the conversion factor from
specified input mass units to specified output mass units and applies the conversion
factor to the input signal.

The Mass Conversion port block labels change based on the input and output
units selected from the **Initial unit** and the **Final unit** lists.
