---
type: simulink-block
title: '1D Self-Conditioned [A(v),B(v),C(v),D(v)]'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Guidance, Navigation, and Control (GNC) / Control'
documentation_page: '1dselfconditionedavbvcvdv'
documentation_source_path: '1dselfconditionedavbvcvdv.html'
language: en
---

# 1D Self-Conditioned [A(v),B(v),C(v),D(v)]

## Ports

### Input

### **y** — Aircraft measurements vector

Aircraft measurements, specified as a vector.

**Data Types:** `double`

### **v** — Scheduling variable vector

Scheduling variable, specified as a vector, ordered according to the dimensions of the
state-space matrices.

**Data Types:** `double`

### **u\_meas** — Measured actuator position vector

Measured actuator position, specified as a vector.

**Data Types:** `double`
### Output

### **u\_dem** — Actuator demands vector

Actuator demands, specified as a vector.

**Data Types:** `double`

## Parameters

### **A-matrix(v)** — *A*-matrix of the state-space implementation `A` (default) | array

*A*-matrix of the state-space implementation. The
*A*-matrix should have three dimensions, the last one
corresponding to the scheduling variable *v*. For example,
if the *A*-matrix corresponding to the first entry of
*v* is the identity matrix, then `A(:,:,1) = [1
0;0 1];`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `A` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'A'` |

### **B-matrix(v)** — *B*-matrix of the state-space implementation `B` (default) | array

*B*-matrix of the state-space implementation. The
*B*-matrix should have three dimensions, the last one
corresponding to the scheduling variable *v*. For example,
if the *B*-matrix corresponding to the first entry of
*v* is the identity matrix, then `B(:,:,1) = [1
0;0 1];`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `B` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'B'` |

### **C-matrix(v)** — *C*-matrix of the state-space implementation `C` (default) | array

*C*-matrix of the state-space implementation. The
*C*-matrix should have three dimensions, the last one
corresponding to the scheduling variable *v*. For example,
if the *C*-matrix corresponding to the first entry of
*v* is the identity matrix, then `C(:,:,1) = [1
0;0 1];`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `C` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'C'` |

### **D-matrix(v)** — *D*-matrix of the state-space implementation `D` (default) | array

*D*-matrix of the state-space implementation. The
*D*-matrix should have three dimensions, the last one
corresponding to the scheduling variable *v*. For example,
if the *D*-matrix corresponding to the first entry of
*v* is the identity matrix, then `D(:,:,1) = [1
0;0 1];`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `D` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'D'` |

### **Scheduling variable breakpoints** — Breakpoints for scheduling variable `v_vec` (default) | vector

Vector of the breakpoints for the first scheduling variable. The length of
*v* should be same as the size of the third dimension
of *A*, *B*, *C*, and
*D*.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `breakpoints_v` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'v_vec'` |

### **Initial state, x\_initial** — Initial states `0` (default) | vector

Vector of initial states for the controller, that is, initial values for the state
vector, *x*. It should have length equal to the size of the
first dimension of *A*.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `x_initial` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'0'` |

### **Poles of A(v)-H(v)\*C(v)** — Desired poles `[-5 -2]` (default) | vector

Desired poles of *A*-*HC*, specified as
a vector. The poles are assigned to the same locations for all values of the
scheduling parameter *v*. Hence, the number of pole
locations defined should be equal to the length of the first dimension of
the *A*-matrix.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `vec_w` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'[-5 -2]'` |

## Libraries

Aerospace Blockset / GNC / Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Implement gain-scheduled state-space controller in self-conditioned form depending on one scheduling parameter

The 1D Self-Conditioned [A(v),B(v),C(v),D(v)] block
implements a gain-scheduled state-space controller as defined in Algorithms.

The output from this block is the actuator demand, which you can input to an actuator
block.
