---
type: simulink-block
title: 'Estimate Inertia Tensor'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Mass Properties'
documentation_page: 'estimateinertiatensor'
documentation_source_path: 'estimateinertiatensor.html'
language: en
---

# Estimate Inertia Tensor

## Ports

### Input

### **mass** — Mass scalar

Mass, specified as a scalar.

**Data Types:** `double`

### **dm/dt** — Rate of change scalar

Rate of change of mass, specified as a scalar.

**Data Types:** `double`
### Output

### **I** — Inertia tensor 3-by-3 matrix

Inertia tensor, returned as a 3-by-3 matrix.

**Data Types:** `double`

### **dI/dt** — Rate of change 3-by-3 matrix

Rate of change of inertia tensor, returned as a 3-by-3 matrix.

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

Empty mass of the vehicle, specified as a double scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `emass` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'1'` |

### **Full inertia matrix** — Full inertia matrix `eye(3)` (default) | 3-element matrix

Inertia tensor at gross mass of the vehicle, specified as a three-element matrix.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `fI` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'eye(3)'` |

### **Empty inertia matrix** — Empty inertia matrix `eye(3)/2` (default) | scalar

Inertia tensor at empty mass of the vehicle, specified as a scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `eI` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'eye(3)/2'` |

## Libraries

Aerospace Blockset / Mass Properties

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Calculate inertia tensor

The Estimate Inertia Tensor block calculates the inertia
tensor and the rate of change of the inertia tensor.

Linear interpolation is used to estimate the inertia tensor as a function of mass. The rate of change of the inertia tensor is a linear function of rate of change of mass.
