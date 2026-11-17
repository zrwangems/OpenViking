---
type: simulink-block
title: 'Velocity Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'velocityconversion'
documentation_source_path: 'velocityconversion.html'
language: en
---

# Velocity Conversion

## Ports
```yaml
ports:
- name: Port_1
  summary: Velocity scalar | array
  direction: input
  data_types: double
- name: Port_1
  summary: Velocity scalar | array
  direction: output
  data_types: double
```

### Input

### **Port\_1** — Velocity scalar | array

Velocity, specified as a scalar or array, in initial velocity
units.

#### Dependencies

The input port label depends on the **Initial
unit** setting.

**Data Types:** `double`
### Output

### **Port\_1** — Velocity scalar | array

Velocity, returned as a scalar or array, in final velocity
units.

#### Dependencies

The output port label depends on the **Final
unit** setting.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Initial unit
  summary: Input units ft/s (default) | m/s | km/s | in/s | km/h | mph | kts | ft/min
  group: ''
  block_parameter: IU
  type: character vector
  values: '''m/s'' | ''ft/s'' | ''km/s'' | ''in/s'' | ''km/h'' | ''mph'' | ''kts'' | ''ft/min'''
  default: '''ft/s'''
- name: Final unit
  summary: Output units m/s (default) | ft/s | km/s | in/s | km/h | mph | kts | ft/min
  group: ''
  block_parameter: OU
  type: character vector
  values: '''m/s'' | ''ft/s'' | ''km/s'' | ''in/s'' | ''km/h'' | ''mph'' | ''kts'' | ''ft/min'''
  default: '''m/s'''
```

### **Initial unit** — Input units `ft/s` (default) | `m/s` | `km/s` | `in/s` | `km/h` | `mph` | `kts` | `ft/min`

Input units, specified as:

|  |  |
| --- | --- |
| `m/s` | Meters per second |
| `ft/s` | Feet per second |
| `km/s` | Kilometers per second |
| `in/s` | Inches per second |
| `km/h` | Kilometers per hour |
| `mph` | Miles per hour |
| `kts` | Nautical miles per hour |
| `ft/min` | Feet per minute |

#### Dependencies

The input port label depends on the **Initial unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IU` |
| **Type**: character vector |
| **Values**: `'m/s'` | `'ft/s'` | `'km/s'` | `'in/s'` | `'km/h'` | `'mph'` | `'kts'` | `'ft/min'` |
| **Default**: `'ft/s'` |

### **Final unit** — Output units `m/s` (default) | `ft/s` | `km/s` | `in/s` | `km/h` | `mph` | `kts` | `ft/min`

Output units, specified as:

|  |  |
| --- | --- |
| `m/s` | Meters per second |
| `ft/s` | Feet per second |
| `km/s` | Kilometers per second |
| `in/s` | Inches per second |
| `km/h` | Kilometers per hour |
| `mph` | Miles per hour |
| `kts` | Nautical miles per hour |
| `ft/min` | Feet per minute |

#### Dependencies

The output port label depends on the **Final unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OU` |
| **Type**: character vector |
| **Values**: `'m/s'` | `'ft/s'` | `'km/s'` | `'in/s'` | `'km/h'` | `'mph'` | `'kts'` | `'ft/min'` |
| **Default**: `'m/s'` |
## Libraries

Aerospace Blockset / Utilities / Unit Conversions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Convert from velocity units to desired velocity units

The Velocity Conversion block computes the conversion factor
from specified input velocity units to specified output velocity units and applies the
conversion factor to the input signal.

The Velocity Conversion block port labels change based on the input and
output units selected from the **Initial unit** and the
**Final unit** lists.
