---
type: simulink-block
title: 'CLA Math'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2803x'
documentation_page: 'clamath'
documentation_source_path: 'ref/clamath.html'
language: en
---

# CLA Math

## Ports
```yaml
ports:
- name: u
  summary: Input data vector
  direction: input
  data_types: single
- name: y
  summary: Output data scalar
  direction: output
  data_types: single
```

### Input

### **u** — Input data vector

The block accepts data specified as an *N*-by-1 array.

**Data Types:** `single`
### Output

### **y** — Output data scalar

The blocks outputs data of single as *N*-by-1
array. The block outputs the value of the selected function parameter.

**Data Types:** `single`
## Parameters
```yaml
parameters:
- name: Function
  summary: Select CLA Math function CLAsin (default) | CLAcos | CLAasin | CLAacos | CLAatan | CLAatan2 | CLAsinPU | CLAcosPU
    | CLAatan2PU | CLAexp | CLAexp2 | CLAexp10 | CLAexpN | CLALn | CLALog10 | CLALogN | CLAdiv | CLAsqrt | CLAisqrt
  group: ''
```

### **Function** — Select CLA Math function `CLAsin` (default) | `CLAcos` | `CLAasin` | `CLAacos` | `CLAatan` | `CLAatan2` | `CLAsinPU` | `CLAcosPU` | `CLAatan2PU` | `CLAexp` | `CLAexp2` | `CLAexp10` | `CLAexpN` | `CLALn` | `CLALog10` | `CLALogN` | `CLAdiv` | `CLAsqrt` | `CLAisqrt`

Select the CLA Math functions which includes trigonometric, logarithmic,
exponential and power functions.
## Libraries

C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023a**

## Description

Implements CLA Math functions from CLA Math library

The CLA Math implements CLA Math functions from CLA Math library. CLA
Math functions include trigonometric, logarithmic, exponential, and power functions.

**Note**

The CLA Math block only works within the model configured for CLA.

Trigonometric functions accept input in radians. PU Trigonometric functions accept input
in per unit.

The block accepts only input of datatype single and outputs data of type single.
