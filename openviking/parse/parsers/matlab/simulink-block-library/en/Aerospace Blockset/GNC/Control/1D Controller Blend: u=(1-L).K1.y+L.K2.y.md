---
type: simulink-block
title: '1D Controller Blend u=(1-L).K1.y+L.K2.y'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'GNC / Control'
documentation_page: '1dcontrollerblendu1l.k1.yl.k2.y'
documentation_source_path: '1dcontrollerblendu1l.k1.yl.k2.y.html'
language: en
---

# 1D Controller Blend u=(1-L).K1.y+L.K2.y

## Ports
```yaml
ports:
- name: y
  summary: Aircraft measurements vector
  direction: input
  data_types: double
- name: v
  summary: Scheduling variable vector
  direction: input
  data_types: double
- name: u
  summary: Actuator demands vector
  direction: output
  data_types: double
```

### Input

### **y** — Aircraft measurements vector

Aircraft measurements, specified as a vector.

**Data Types:** `double`

### **v** — Scheduling variable vector

Scheduling variable, specified as a vector, that conforms to the
dimensions of the state-space matrices.

**Data Types:** `double`
### Output

### **u** — Actuator demands vector

Actuator demands, specified as a vector.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: A-matrix(v)
  summary: '*A*-matrix of the state-space implementation A1 (default) | array'
  group: ''
  block_parameter: A
  type: character vector
  values: vector
  default: '''A1'''
- name: B-matrix(v)
  summary: '*B*-matrix of the state-space implementation B1 (default) | array'
  group: ''
  block_parameter: B
  type: character vector
  values: vector
  default: '''B1'''
- name: C-matrix(v)
  summary: '*C*-matrix of the state-space implementation C1 (default) | array'
  group: ''
  block_parameter: C
  type: character vector
  values: vector
  default: '''C1'''
- name: D-matrix(v)
  summary: '*D*-matrix of the state-space implementation D1 (default) | array'
  group: ''
  block_parameter: D
  type: character vector
  values: vector
  default: '''D1'''
- name: Scheduling variable breakpoints
  summary: Breakpoints for scheduling variable [1 1.5 2] (default) | vector
  group: ''
  block_parameter: breakpoints_v
  type: character vector
  values: vector
  default: '''[1 1.5 2]'''
- name: Initial state, x_initial
  summary: Initial states 0 (default) | vector
  group: ''
  block_parameter: x_initial
  type: character vector
  values: vector
  default: '''0'''
- name: Poles of A(v)-H(v)\*C(v) = [w1 ... wn])
  summary: Poles of observer [-5 -2] (default) | vector
  group: ''
  block_parameter: vec_w
  type: character vector
  values: vector
  default: '''[-5 -2]'''
```

### **A-matrix(v)** — *A*-matrix of the state-space implementation `A1` (default) | array

*A*-matrix of the state-space implementation, specified as an array. In
the case of 1-D blending, the *A*-matrix should have three
dimensions, the last one corresponding to scheduling variable
*v*. For example, if the *A*-matrix
corresponding to the first entry of *v* is the identity
matrix, then `A(:,:,1) = [1 0;0 1];`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `A` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'A1'` |

### **B-matrix(v)** — *B*-matrix of the state-space implementation `B1` (default) | array

*B*-matrix of the state-space implementation, specified as an array. In
the case of 1-D scheduling, the *B*-matrix should have
three dimensions, the last one corresponding to the scheduling variable
*v*. For example, if the *B*-matrix
corresponding to the first entry of *v* is the identity
matrix, then `B(:,:,1) = [1 0;0 1];`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `B` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'B1'` |

### **C-matrix(v)** — *C*-matrix of the state-space implementation `C1` (default) | array

*C*-matrix of the state-space implementation, specified as an array. In
the case of 1-D scheduling, the *C*-matrix should have
three dimensions, the last one corresponding to the scheduling variable
*v*. For example, if the *C*-matrix
corresponding to the first entry of *v* is the identity
matrix, then `C(:,:,1) = [1 0;0 1];`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `C` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'C1'` |

### **D-matrix(v)** — *D*-matrix of the state-space implementation `D1` (default) | array

*D*-matrix of the state-space implementation, specified as an array. In
the case of 1-D scheduling, the *D*-matrix should have
three dimensions, the last one corresponding to the scheduling variable
*v*. For example, if the *D*-matrix
corresponding to the first entry of *v* is the identity
matrix, then `D(:,:,1) = [1 0;0 1];`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `D` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'D1'` |

### **Scheduling variable breakpoints** — Breakpoints for scheduling variable `[1 1.5 2]` (default) | vector

Breakpoints for the scheduling variable, specified as a vector. The length
of *v* must be same as the size of the third dimension of
*A*, *B*, *C*, and
*D*.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `breakpoints_v` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'[1 1.5 2]'` |

### **Initial state, x\_initial** — Initial states `0` (default) | vector

Initial states for the controller, such as initial values for the state vector,
*x*, specified as a vector. The length must equal the
size of the first dimension of *A*.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `x_initial` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'0'` |

### **Poles of A(v)-H(v)\*C(v) = [w1 ... wn])** — Poles of observer `[-5 -2]` (default) | vector

Poles of observer, specified as a vector. For incoming controllers, the block uses an
observer-like structure to ensure that the controller output tracks the
current block output, *u*. The number of poles must equal
the dimension of the *A*-matrix. Poles that are too fast
result in sensor noise propagation; poles that are too slow result in the
failure of the controller output to track *u*.

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

Implement 1-D vector of state-space controllers by linear interpolation of their outputs

The 1D Controller Blend u=(1-L).K1.y+L.K2.y block implements
an array of state-space controller designs. The model runs the controllers in parallel
and interpolates their outputs according to the current flight condition or operating
point. The advantage of this implementation approach is that the state-space matrices
*A*, *B*, *C*, and
*D* for the individual controller designs do not need to vary
smoothly from one design point to the next. The output from this block is the actuator
demand, which you can input to an actuator block.
