---
type: simulink-block
title: 'Create 3x3 Matrix'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Math Operations'
documentation_page: 'create3x3matrix'
documentation_source_path: 'create3x3matrix.html'
language: en
---

# Create 3x3 Matrix

## Ports
```yaml
ports:
- name: A11
  summary: First row, first column of matrix matrix element
  direction: input
  data_types: double
- name: A12
  summary: First row, second column of matrix matrix element
  direction: input
  data_types: double
- name: A13
  summary: First row, third column of matrix matrix element
  direction: input
  data_types: double
- name: A21
  summary: Second row, first column of matrix matrix element
  direction: input
  data_types: double
- name: A22
  summary: Second row, second column of matrix matrix element
  direction: input
  data_types: double
- name: A23
  summary: Second row, third column of matrix matrix element
  direction: input
  data_types: double
- name: A31
  summary: Third row, first column of matrix matrix element
  direction: input
  data_types: double
- name: A32
  summary: Third row, second column of matrix matrix element
  direction: input
  data_types: double
- name: A33
  summary: Third row, third column of matrix matrix element
  direction: input
  data_types: double
- name: A
  summary: Matrix 3-by-3 matrix
  direction: output
  data_types: double
```

### Input

### **A11** — First row, first column of matrix matrix element

First row, first column of the matrix, specified as a matrix
element.

**Example:** 1

**Data Types:** `double`

### **A12** — First row, second column of matrix matrix element

First row, second column of the matrix, specified as a matrix
element.

**Example:** 2

**Data Types:** `double`

### **A13** — First row, third column of matrix matrix element

First row, third column of the matrix, specified as a matrix
element.

**Example:** 3

**Data Types:** `double`

### **A21** — Second row, first column of matrix matrix element

Second row, first column of the matrix, specified as a matrix
element.

**Example:** 4

**Data Types:** `double`

### **A22** — Second row, second column of matrix matrix element

Second row, second column of the matrix, specified as a matrix
element.

**Example:** 5

**Data Types:** `double`

### **A23** — Second row, third column of matrix matrix element

Second row, third column of the matrix, specified as a matrix
element.

**Example:** 6

**Data Types:** `double`

### **A31** — Third row, first column of matrix matrix element

Third row, first column of the matrix, specified as a matrix
element.

**Example:** 7

**Data Types:** `double`

### **A32** — Third row, second column of matrix matrix element

Third row, second column of the matrix, specified as a matrix
element.

**Example:** 8

**Data Types:** `double`

### **A33** — Third row, third column of matrix matrix element

Third row, third column of the matrix, specified as a matrix
element.

**Example:** 9

**Data Types:** `double`
### Output

### **A** — Matrix 3-by-3 matrix

Matrix, output as a 3-by-3 matrix.

**Data Types:** `double`
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Aerospace Blockset / Utilities / Math Operations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Create 3-by-3 matrix from nine input values

The Create 3x3 Matrix block creates a 3-by-3 matrix from nine
input values where each input corresponds to an element of the matrix.

The output matrix has the form of

A=[A11A12A13A21A22A23A31A32A33]
