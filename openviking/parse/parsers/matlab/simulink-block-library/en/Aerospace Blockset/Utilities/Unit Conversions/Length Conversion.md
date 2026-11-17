---
type: simulink-block
title: 'Length Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'lengthconversion'
documentation_source_path: 'lengthconversion.html'
language: en
---

# Length Conversion

## Ports
```yaml
ports:
- name: Port_1
  summary: Length scalar | array
  direction: input
  data_types: double
- name: Port_1
  summary: Length scalar | array
  direction: output
  data_types: double
```

### Input

### **Port\_1** — Length scalar | array

Length, specified as a scalar or array, in initial length
units.

#### Dependencies

The input port label depends on the **Initial
unit** setting.

**Data Types:** `double`
### Output

### **Port\_1** — Length scalar | array

Length, returned as a scalar or array, in final length units.

#### Dependencies

The output port label depends on the **Final
unit** setting.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Initial unit
  summary: Input units ft (default) | m | km | in | mi | naut mi
  group: ''
  block_parameter: IU
  type: character vector
  values: '''m'' | ''ft'' | ''km'' | ''in'' | ''mi'' | ''naut mi'''
  default: '''ft'''
- name: Final unit
  summary: Input units m (default) | ft | km | in | mi | naut mi
  group: ''
  block_parameter: OU
  type: character vector
  values: '''m'' | ''ft'' | ''km'' | ''in'' | ''mi'' | ''naut mi'''
  default: '''m'''
```

### **Initial unit** — Input units `ft` (default) | `m` | `km` | `in` | `mi` | `naut mi`

Input units, specified as:

|  |  |
| --- | --- |
| `m` | Meters |
| `ft` | Feet |
| `km` | Kilometers |
| `in` | Inches |
| `mi` | Miles |
| `naut mi` | Nautical miles |

#### Dependencies

The input port label depends on the **Initial unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IU` |
| **Type**: character vector |
| **Values**: `'m'` | `'ft'` | `'km'` | `'in'` | `'mi'` | `'naut mi'` |
| **Default**: `'ft'` |

### **Final unit** — Input units `m` (default) | `ft` | `km` | `in` | `mi` | `naut mi`

Output units, specified as:

|  |  |
| --- | --- |
| `m` | Meters |
| `ft` | Feet |
| `km` | Kilometers |
| `in` | Inches |
| `mi` | Miles |
| `naut mi` | Nautical miles |

#### Dependencies

The output port label depends on the **Final unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OU` |
| **Type**: character vector |
| **Values**: `'m'` | `'ft'` | `'km'` | `'in'` | `'mi'` | `'naut mi'` |
| **Default**: `'m'` |
## Libraries

Aerospace Blockset / Utilities / Unit Conversions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Convert from length units to desired length units

The Length Conversion block computes the conversion factor
from specified input length units to specified output length units and applies the
conversion factor to the input signal.

The Length Conversion block port labels change based on the input and output
units selected from the **Initial unit** and the **Final unit** lists.
