---
type: simulink-block
title: 'Angular Velocity Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'angularvelocityconversion'
documentation_source_path: 'angularvelocityconversion.html'
language: en
---

# Angular Velocity Conversion

## Ports
```yaml
ports:
- name: Port_1
  summary: Angular acceleration scalar | array
  direction: input
  data_types: double
- name: Port_1
  summary: Angular acceleration scalar | array
  direction: output
  data_types: double
```

### Input

### **Port\_1** — Angular acceleration scalar | array

Angular acceleration, specified as a scalar, in initial angular
acceleration units.

#### Dependencies

The input port label depends on the **Initial
unit** setting.

**Data Types:** `double`
### Output

### **Port\_1** — Angular acceleration scalar | array

Angular acceleration, returned as a scalar, in final angular
acceleration units.

#### Dependencies

The output port label depends on the **Final
unit** setting.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Initial unit
  summary: Input units deg/s (default) | rad/s | rpm
  group: ''
  block_parameter: IU
  type: character vector
  values: '''deg/s'' | ''rad/s'' | ''rpm/s'''
  default: '''deg/s'''
- name: Final unit
  summary: Output units rad/s (default) | deg/s | rpm
  group: ''
  block_parameter: OU
  type: character vector
  values: '''deg/s'' | ''rad/s'' | ''rpm/s'''
  default: '''deg/s'''
```

### **Initial unit** — Input units `deg/s` (default) | `rad/s` | `rpm`

Input units, specified as:

|  |  |
| --- | --- |
| `deg`/s | Degrees per second |
| `rad`/s | Radians per second |
| `rpm` | Revolutions per minute |

#### Dependencies

The input port label depends on the **Initial unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IU` |
| **Type**: character vector |
| **Values**: `'deg/s'` | `'rad/s'` | `'rpm/s'` |
| **Default**: `'deg/s'` |

### **Final unit** — Output units `rad/s` (default) | `deg/s` | `rpm`

Output units, specified as:

|  |  |
| --- | --- |
| `deg`/s | Degrees per second |
| `rad`/s | Radians per second |
| `rpm` | Revolutions per minute |

#### Dependencies

The output port label depends on the **Final unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OU` |
| **Type**: character vector |
| **Values**: `'deg/s'` | `'rad/s'` | `'rpm/s'` |
| **Default**: `'deg/s'` |
## Libraries

Aerospace Blockset / Utilities / Unit Conversions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Convert from angular velocity units to desired angular velocity units

The Angular Velocity Conversion block computes the conversion
factor from specified input angular velocity units to specified output angular velocity
units and applies the conversion factor to the input signal.

The Angular Velocity Conversion block port labels change based on the input
and output units selected from the **Initial unit** and the
**Final unit** lists.
