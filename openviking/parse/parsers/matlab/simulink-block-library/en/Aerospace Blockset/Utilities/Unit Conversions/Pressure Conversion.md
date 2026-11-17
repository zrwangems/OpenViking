---
type: simulink-block
title: 'Pressure Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'pressureconversion'
documentation_source_path: 'pressureconversion.html'
language: en
---

# Pressure Conversion

## Ports
```yaml
ports:
- name: Port_1
  summary: Pressure scalar | array
  direction: input
  data_types: double
- name: Port_1
  summary: Pressure scalar | array
  direction: output
  data_types: double
```

### Input

### **Port\_1** — Pressure scalar | array

Pressure, specified as a scalar or array, in initial pressure
units.

#### Dependencies

The input port label depends on the **Initial
unit** setting.

**Data Types:** `double`
### Output

### **Port\_1** — Pressure scalar | array

Pressure, returned as a scalar or array, in final pressure
units.

#### Dependencies

The output port label depends on the **Final
unit** setting.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Initial unit
  summary: Input units psi (default) | Pa | psf | atm
  group: ''
  block_parameter: IU
  type: character vector
  values: '''psi'' | ''Pa'' | ''psf'' | ''atm'''
  default: '''psi'''
- name: Final unit
  summary: Output units Pa (default) | psi | psf | atm
  group: ''
  block_parameter: OU
  type: character vector
  values: '''psi'' | ''Pa'' | ''psf'' | ''atm'''
  default: '''Pa'''
```

### **Initial unit** — Input units `psi` (default) | `Pa` | `psf` | `atm`

Input units, specified as:

|  |  |
| --- | --- |
| `psi` | Pound mass per square inch |
| `Pa` | Pascals |
| `psf` | Pound mass per square foot |
| `atm` | Atmospheres |

#### Dependencies

The input port label depends on the **Initial unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IU` |
| **Type**: character vector |
| **Values**: `'psi'` | `'Pa'` | `'psf'` | `'atm'` |
| **Default**: `'psi'` |

### **Final unit** — Output units `Pa` (default) | `psi` | `psf` | `atm`

Output units, specified as:

|  |  |
| --- | --- |
| `psi` | Pound mass per square inch |
| `Pa` | Pascals |
| `psf` | Pound mass per square foot |
| `atm` | Atmospheres |

#### Dependencies

The output port label depends on the **Final unit**
setting.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OU` |
| **Type**: character vector |
| **Values**: `'psi'` | `'Pa'` | `'psf'` | `'atm'` |
| **Default**: `'Pa'` |
## Libraries

Aerospace Blockset / Utilities / Unit Conversions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Convert from pressure units to desired pressure units

The Pressure Conversion block computes the conversion factor
from specified input pressure units to specified output pressure units and applies the
conversion factor to the input signal.

The Pressure Conversion block port labels change based on the input and
output units selected from the **Initial unit** and the
**Final unit** lists.
