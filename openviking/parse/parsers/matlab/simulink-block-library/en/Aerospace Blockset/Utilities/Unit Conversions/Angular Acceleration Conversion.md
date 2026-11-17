---
type: simulink-block
title: 'Angular Acceleration Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'angularaccelerationconversion'
documentation_source_path: 'angularaccelerationconversion.html'
language: en
---

# Angular Acceleration Conversion

## Ports
```yaml
ports:
- name: Port_1
  summary: Angular input acceleration scalar | array
  direction: input
  data_types: double
- name: Port_1
  summary: Angular output acceleration scalar | array
  direction: output
  data_types: double
```

### Input

### **Port\_1** — Angular input acceleration scalar | array

Angle, specified as a scalar, in initial acceleration units.

#### Dependencies

The input port label depends on the **Initial
unit** setting.

**Data Types:** `double`
### Output

### **Port\_1** — Angular output acceleration scalar | array

Angle, returned as a scalar, in final acceleration units.

#### Dependencies

The output port label depends on the **Final
unit** setting.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Initial unit
  summary: Input units deg/s2 (default) | rad/s2 | rpm/s
  group: ''
  block_parameter: IU
  type: character vector
  values: '''deg/s^2'' | ''rad/s^2'' | ''rpm/s'''
  default: '''deg/s^2'''
- name: Final unit
  summary: Output units rad/ss (default) | deg/ss | rpm/s
  group: ''
  block_parameter: OU
  type: character vector
  values: '''deg/s^2'' | ''rad/s^2'' | ''rpm/s'''
  default: '''rad/s^2'''
```

### **Initial unit** — Input units `deg/s2` (default) | `rad/s2` | `rpm/s`

Specifies the input units, specified as:

|  |  |
| --- | --- |
| `deg/s`2 | Degrees per second squared |
| `rad/s`2 | Radians per second squared |
| `rpm/s` | Revolutions per minute per second |

#### Dependencies

The input port label depends on the **Initial unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IU` |
| **Type**: character vector |
| **Values**: `'deg/s^2'` | `'rad/s^2'` | `'rpm/s'` |
| **Default**: `'deg/s^2'` |

### **Final unit** — Output units `rad/ss` (default) | `deg/ss` | `rpm/s`

Output units, specified as:

|  |  |
| --- | --- |
| `deg/s`2 | Degrees per second squared |
| `rad/s`2 | Radians per second squared |
| `rpm/s` | Revolutions per minute per second |

#### Dependencies

The output port label depends on the **Final unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OU` |
| **Type**: character vector |
| **Values**: `'deg/s^2'` | `'rad/s^2'` | `'rpm/s'` |
| **Default**: `'rad/s^2'` |
## Libraries

Aerospace Blockset / Utilities / Unit Conversions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Convert from angular acceleration units to desired angular acceleration units

The Angular Acceleration Conversion block computes the
conversion factor from specified input angular acceleration units to specified output
angular acceleration units and applies the conversion factor to the input signal.

The Angular Acceleration Conversion block port labels change based on the
input and output units selected from the **Initial unit**
and the **Final unit** lists.
