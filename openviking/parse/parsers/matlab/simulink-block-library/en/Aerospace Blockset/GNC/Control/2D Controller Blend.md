---
type: simulink-block
title: '2D Controller Blend'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'GNC / Control'
documentation_page: '2dcontrollerblend'
documentation_source_path: '2dcontrollerblend.html'
language: en
---

# 2D Controller Blend

## Ports
```yaml
ports:
- name: y
  summary: Aircraft measurements vector
  direction: input
  data_types: double
- name: v1
  summary: Scheduling variable vector
  direction: input
  data_types: double
- name: v2
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

### **v1** — Scheduling variable vector

Scheduling variable, specified as a vector, that conforms to the dimensions of the
state-space matrices.

**Data Types:** `double`

### **v2** — Scheduling variable vector

Scheduling variable, specified as a vector, that conforms to the dimensions of the
state-space matrices.

**Data Types:** `double`
### Output

### **u** — Actuator demands vector

Actuator demands, specified as a vector.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: A-matrix(v1,v2)
  summary: '*A*-matrix of the state-space implementation A (default) | array'
  group: ''
  block_parameter: A
  type: character vector
  values: vector
  default: '''A'''
- name: B-matrix(v1,v2)
  summary: '*B*-matrix of the state-space implementation A (default) | array'
  group: ''
  block_parameter: B
  type: character vector
  values: vector
  default: '''B'''
- name: C-matrix(v1,v2)
  summary: '*C*-matrix of the state-space implementation C (default) | array'
  group: ''
  block_parameter: C
  type: character vector
  values: vector
  default: '''C'''
- name: D-matrix(v1,v2)
  summary: '*D*-matrix of the state-space implementation C (default) | array'
  group: ''
  block_parameter: D
  type: character vector
  values: vector
  default: '''D'''
- name: First scheduling variable (v1) breakpoints
  summary: Breakpoints for first scheduling variable v1_vec (default) | vector
  group: ''
  block_parameter: breakpoints_v1
  type: character vector
  values: vector
  default: '''v1_vec'''
- name: Second scheduling variable (v2) breakpoints
  summary: Breakpoints for second scheduling variable v2_vec (default) | vector
  group: ''
  block_parameter: breakpoints_v2
  type: character vector
  values: vector
  default: '''v2_vec'''
- name: Initial state, x_initial
  summary: Initial states 0 (default) | vector
  group: ''
  block_parameter: x_initial
  type: character vector
  values: vector
  default: '''0'''
- name: Poles of A(v)-H(v)\*C(v)
  summary: Desired poles [-5 -2] (default)
  group: ''
  block_parameter: vec_w
  type: character vector
  values: vector
  default: '''[-5 -2]'''
```

### **A-matrix(v1,v2)** — *A*-matrix of the state-space implementation A (default) | array

*A*-matrix of the state-space implementation. In the case of 2-D
blending, the *A*-matrix should have four dimensions, the
last two corresponding to scheduling variables *v*1 and
*v*2. For example, if the *A*-matrix
corresponding to the first entry of *v*1 and first entry of
*v*2 is the identity matrix, then `A(:,:,1,1) =
[1 0;0 1];`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `A` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'A'` |

### **B-matrix(v1,v2)** — *B*-matrix of the state-space implementation A (default) | array

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

### **C-matrix(v1,v2)** — *C*-matrix of the state-space implementation C (default) | array

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

### **D-matrix(v1,v2)** — *D*-matrix of the state-space implementation C (default) | array

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

### **First scheduling variable (v1) breakpoints** — Breakpoints for first scheduling variable `v1_vec` (default) | vector

Breakpoints for the first scheduling variable, specified as a vector. The
length of *v*1 should be same as the size of the third
dimension of *A*, *B*,
*C*, and *D*.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `breakpoints_v1` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'v1_vec'` |

### **Second scheduling variable (v2) breakpoints** — Breakpoints for second scheduling variable `v2_vec` (default) | vector

Breakpoints for the second scheduling variable, specified as a vector. The
length of *v*2 should be same as the size of the fourth
dimension of *A*, *B*,
*C*, and *D*.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `breakpoints_v2` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'v2_vec'` |

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

### **Poles of A(v)-H(v)\*C(v)** — Desired poles `[-5 -2]` (default)

For oncoming controllers, an observer-like structure is used to ensure
that the controller output tracks the current block output,
*u*. The poles of the observer are defined in this
dialog box as a vector, the number of poles being equal to the dimension of
the *A*-matrix. Poles that are too fast result in sensor
noise propagation, and poles that are too slow result in the failure of the
controller output to track *u*.

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

Implement 2-D vector of state-space controllers by linear interpolation of their outputs

The 2D Controller Blend block implements an array of
state-space controller designs. The controllers are run in parallel, and their outputs
interpolated according to the current flight condition or operating point. The advantage
of this implementation approach is that the state-space matrices *A*,
*B*, *C*, and *D* for the
individual controller designs do not need to vary smoothly from one design point to the
next. The output from this block is the actuator demand, which you can input to an
actuator block.

For the 2D Controller Blend block, at any given instant in time, nine
controller designs are updated.

As the value of the scheduling parameter varies and the index
of the controllers that need to be run changes, the states of the
oncoming controller are initialized by using the self-conditioned
form as defined for the Self-Conditioned [A,B,C,D] block.
