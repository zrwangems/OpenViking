---
type: simulink-block
title: 'Divide by Constant and Round'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: 'Embedded Implementation / Fixed-Point Math Operations in MATLAB and Simulink / Arithmetic Operations'
documentation_page: 'dividebyconstantandround'
documentation_source_path: 'ref/dividebyconstantandround.html'
language: en
---

# Divide by Constant and Round

## Ports

### Input

### **X** — Dividend scalar | vector | matrix | N-D array

Dividend, specified as a scalar, vector, matrix, or N-D array.

Divide by Constant and Round does not support data types with word
length greater than 65,535. Slope-bias representation is not supported for fixed-point
data types.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Y** — Result of division and round operation scalar | vector | matrix | N-D array

Result of division and round operation, returned as a scalar, vector, matrix, or
N-D array.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## Parameters

### **Denominator** — Divisor 10 (default) | scalar

Divisor, specified as a positive, real-valued, finite scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Denominator` |
| **Type:** character vector |
| **Values:** MATLAB® expression that evaluates to a positive, real-valued, finite fixed point or numeric value |
| **Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` |
| **Default:** `'10'` |

### **Rounding Method** — Rounding method to use `Floor` (default) | `Ceiling` | `Nearest` | `Zero` | `Convergent`

Rounding method to use, specified as one of these values:

- `Floor` — Round to nearest integer in the direction of
  negative infinity.
- `Ceiling` — Round to nearest integer in the direction
  of positive infinity.
- `Nearest` — Round to the nearest integer. Ties are
  rounded to the nearest integer in the direction of positive infinity.
- `Zero` — Round to the nearest integer in the direction
  of zero.
- `Convergent` — Round to the nearest integer. Ties are
  rounded to the nearest even integer.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Floor'` | `'Ceiling'` | `'Nearest'` | `'Zero'` | `'Convergent'` |
| **Default:** `'Floor'` |

## Libraries

Fixed-Point Designer

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Slope-bias representation is not supported for fixed-point data types.

## Version History

**Introduced in R2021a**

## Description

Divide input by a constant and round to integer

The Divide by Constant and Round block outputs the result of dividing the
input by a constant and rounds the result to an integer using the specified rounding
method.

The Divide by Constant and Round block uses an algorithm that is
functionally similar to the Granlund-Montgomery-Warren Method. The division operation is
computed via a multiplication by inverse, which generally results in better performance on
embedded systems.
