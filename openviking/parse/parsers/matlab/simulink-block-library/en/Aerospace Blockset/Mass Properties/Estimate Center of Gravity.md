---
type: simulink-block
title: 'Estimate Center of Gravity'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Mass Properties'
documentation_page: 'estimatecenterofgravity'
documentation_source_path: 'estimatecenterofgravity.html'
language: en
---

# Estimate Center of Gravity

## Ports
```yaml
ports:
- name: mass
  summary: Mass scalar
  direction: input
  data_types: double
- name: dm/dt
  summary: Rate of change scalar | 3-element vector
  direction: input
  data_types: '| double'
- name: CG
  summary: Center of gravity location 3-element vector
  direction: output
  data_types: double
- name: dCG/dt
  summary: Rate of change 3-element vector
  direction: output
  data_types: double
```

### Input

### **mass** — Mass scalar

Mass, specified as a scalar.

**Data Types:** `double`

### **dm/dt** — Rate of change scalar | 3-element vector

Rate of change of mass, specified as a scalar or three-element vector.

**Data Types:**  | `double`
### Output

### **CG** — Center of gravity location 3-element vector

Center of gravity location, returned as a three-element vector.

**Data Types:** `double`

### **dCG/dt** — Rate of change 3-element vector

Rate of the change of center of gravity location, returned as a three-element
vector.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Full mass
  summary: Mass 2 (default) | scalar
  group: ''
  block_parameter: fmass
  type: character vector
  values: double scalar
  default: '''2'''
- name: Empty mass
  summary: Empty mass 1 (default) | scalar
  group: ''
  block_parameter: emass
  type: character vector
  values: double scalar
  default: '''1'''
- name: Full center of gravity
  summary: Full center of gravity [1 1 1]' (default) | 3-element vector
  group: ''
  block_parameter: fcg
  type: character vector
  values: 3-element vector
  default: '[1 1 1]'''
- name: Empty center of gravity
  summary: Empty center of gravity [0.5 0.5 0.5]' (default) | 3-element vector
  group: ''
  block_parameter: ecg
  type: character vector
  values: 3-element vector
  default: '[0.5 0.5 0.5]'''
```

### **Full mass** — Mass `2` (default) | scalar

Gross mass of the vehicle, specified as a double scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `fmass` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'2'` |

### **Empty mass** — Empty mass `1` (default) | scalar

Empty mass of the vehicle, specified as double scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `emass` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'1'` |

### **Full center of gravity** — Full center of gravity `[1 1 1]'` (default) | 3-element vector

Center of gravity at the gross mass of the vehicle, specified as a three-element
vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `fcg` |
| **Type**: character vector |
| **Values**: 3-element vector |
| **Default**: `[1 1 1]'` |

### **Empty center of gravity** — Empty center of gravity `[0.5 0.5 0.5]'` (default) | 3-element vector

Center of gravity at the empty mass of the vehicle, specified as a three-element
vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ecg` |
| **Type**: character vector |
| **Values**: 3-element vector |
| **Default**: `[0.5 0.5 0.5]'` |
## Libraries

Aerospace Blockset / Mass Properties

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Calculate center of gravity location

The Estimate Center of Gravity block calculates the center of
gravity location and the rate of change of the center of gravity.

Linear interpolation is used to estimate the location of the center of gravity as a function
of mass. The rate of change of the center of gravity is a linear function of the rate of
change of mass.
