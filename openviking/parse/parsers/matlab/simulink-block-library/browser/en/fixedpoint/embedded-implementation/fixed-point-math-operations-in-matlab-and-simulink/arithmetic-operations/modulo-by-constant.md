---
type: simulink-block
title: 'Modulo by Constant'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: 'Embedded Implementation / Fixed-Point Math Operations in MATLAB and Simulink / Arithmetic Operations'
documentation_page: 'modulobyconstant'
documentation_source_path: 'ref/modulobyconstant.html'
language: en
---

# Modulo by Constant

## Ports

### Input

### **X** — Dividend real-valued scalar | vector | matrix | multidimensional array

Dividend, specified as a real-valued scalar, vector, matrix, or multidimensional
array.

If `X` is a fixed-point data type, it must use binary-point
scaling. Slope-bias representation is not supported for fixed-point data types.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `fixed point`
### Output

### **Y** — Result of modulus operation scalar | vector | matrix | multidimensional array

Result of modulus operation, returned as a scalar, vector, matrix, or
multidimensional array.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `fixed point`

## Parameters

### **Denominator for Modulo Problem** — Divisor 10 (default) | real-valued scalar | vector | matrix | multidimensional array

Divisor to use for the modulus operation, specified as a positive, real-valued,
finite scalar, vector, matrix, or multidimensional array.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Denominator` |
| **Type:** character vector |
| **Values:** MATLAB® expression that evaluates to a positive, real-valued, finite fixed point or numeric value |
| **Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` |
| **Default:** `'10'` |

## Libraries

Fixed-Point Designer

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Slope-bias representation is not supported for fixed-point data types.

## Version History

**Introduced in R2021a**

### R2023b: Support for vector and matrix input

The Modulo by Constant block now supports vector and matrix
inputs.

### R2023b: Modulo by Consant block supported for use in For Each Subsystem block

The Modulo by Consant block is supported for use inside a For
Each Subsystem block.

## Description

Perform modulo operation with a constant denominator

The Modulo by Constant block performs the modulo operation (remainder after
division) with a constant denominator.

The Modulo by Constant block uses an algorithm that is functionally similar
to a Barrett Reduction. The division operation is computed via a multiplication by inverse,
which generally results in better performance on embedded systems.
