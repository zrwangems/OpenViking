---
type: simulink-block
title: 'Estimate Center of Gravity'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Atmospheric Flight / Mass Properties'
documentation_page: 'estimatecenterofgravity'
documentation_source_path: 'estimatecenterofgravity.html'
language: en
---

# Estimate Center of Gravity

## Ports

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
