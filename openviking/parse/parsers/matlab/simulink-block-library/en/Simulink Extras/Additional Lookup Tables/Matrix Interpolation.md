---
type: simulink-block
title: 'Matrix Interpolation'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Additional Lookup Tables'
documentation_page: 'matrixinterpolation'
documentation_source_path: '../simulink/ref_extras/matrixinterpolation.html'
language: en
---

# Matrix Interpolation

## Ports
```yaml
ports:
- name: k1
  summary: Index, k1, for the first dimension of the table scalar
  direction: input
  data_types: single | double
- name: f1
  summary: Fraction, f1, for the first dimension of the table scalar
  direction: input
  data_types: single | double
- name: kn
  summary: Index, kn, for the n-th dimension of the table scalar
  direction: input
  data_types: single | double
- name: fn
  summary: Fraction, fn, for the n-th dimension of the table scalar
  direction: input
  data_types: single | double
- name: Port_1
  summary: Approximation of N-dimensional function scalar | vector | matrix | N-D array
  direction: output
  data_types: single | double
```

### Input

### **k1** — Index, `k1`, for the first dimension of the table scalar

Index `k1` for the first dimension of the
table.

**Data Types:** `single` | `double`

### **f1** — Fraction, `f1`, for the first dimension of the table scalar

Fraction `f1` for the first dimension of the
table.

**Data Types:** `single` | `double`

### **kn** — Index, `kn`, for the n-th dimension of the table scalar

Index `kn` for the n-th dimension of the
table.

**Data Types:** `single` | `double`

### **fn** — Fraction, `fn`, for the n-th dimension of the table scalar

Fraction `fn` for the n-th dimension of the
table.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Approximation of N-dimensional function scalar | vector | matrix | N-D array

Approximation of N-dimensional function, computed by interpolating (or
extrapolating) table data using values from the input index,
`k`, and the fraction, `f`.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Interpolation method
  summary: Interpolation method Linear (default) | Nearest | Flat
  group: ''
  block_parameter: InterpMethod
  type: character vector
  values: '''Flat'' | ''Nearest'' | ''Linear'''
  default: '''Linear'''
- name: Extrapolation method
  summary: Extrapolation method Clip (default) | Linear
  group: ''
  block_parameter: ExtrapMethod
  type: character vector
  values: '''Clip'' | ''Linear'''
  default: '''Clip'''
- name: Interpolate Dimension
  summary: Number of lookup table dimensions 1 (default) | 2 | 3
  group: ''
  block_parameter: InterpolateDimension
  type: character vector
  values: '''1'' | ''2'' | ''3'''
  default: '''1'''
- name: Table data
  summary: Table of output values 1:1:10 (default) | vector | matrix | N-D array
  group: ''
  block_parameter: TableData
  type: character vector
  values: vector | matrix | N-D array
  default: '''1:1:10'''
- name: Simulate using
  summary: Simulation mode Code generation | Interpreted execution
  group: ''
  block_parameter: SimulateUsing
  type: character vector
  values: '''Code generation'' | ''Interpreted execution'''
  default: '''Code generation'''
```

### **Interpolation method** — Interpolation method `Linear` (default) | `Nearest` | `Flat`

Choose how to interpolate table data in between breakpoints. Select
`Flat`, `Nearest`, or
`Linear`. For more information, see Interpolation Methods.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InterpMethod` |
| **Type:** character vector |
| **Values:** `'Flat' | 'Nearest' | 'Linear'` |
| **Default:** `'Linear'` |

### **Extrapolation method** — Extrapolation method `Clip` (default) | `Linear`

Choose how to extrapolate table data if your index *k*
and fraction *f* from the inputs are beyond the range of
the breakpoints. Select `Clip` or
`Linear`. For more information, see Extrapolation Methods.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ExtrapMethod` |
| **Type:** character vector |
| **Values:** `'Clip' | 'Linear'` |
| **Default:** `'Clip'` |

### **Interpolate Dimension** — Number of lookup table dimensions `1` (default) | `2` | `3`

Enter the number of dimensions of the lookup table by specifying an
integer from `1` to `3`. This parameter
determines:

- The number of independent variables for the table and the number
  of block inputs.
- The number of breakpoint input sets to specify.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InterpolateDimension` |
| **Type:** character vector |
| **Values:** `'1' | '2' | '3'` |
| **Default:** `'1'` |

### **Table data** — Table of output values `1:1:10` (default) | vector | matrix | N-D array

Enter the table of output values. The number of dimensions of the table
data must be the sum of the number of breakpoint dimensions and the number
of matrix dimensions because each data point is a matrix for this
block.

For information about how to construct multidimensional arrays in
MATLAB®, see Multidimensional Arrays.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableData` |
| **Type:** character vector |
| **Values:** vector | matrix | N-D array |
| **Default:** `'1:1:10'` |

### **Simulate using** — Simulation mode `Code generation` | `Interpreted execution`

Select the simulation mode.

- `Code generation` — On the first model
  run, simulate, and generate code for the MATLAB
  System block with only MATLAB functions supported for code generation. If the
  structure of the block does not change, subsequent model runs do not
  regenerate the code.

  If the simulation mode is `Code
  generation`, system objects accept a maximum of 32
  inputs.
- `Interpreted execution` — Simulate the
  model by using all supported MATLAB functions. Choosing this option can slow simulation
  performance.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimulateUsing` |
| **Type:** character vector |
| **Values:** `'Code generation' | 'Interpreted execution'` |
| **Default:** `'Code generation'` |
## Libraries

Simulink Extras / Additional Lookup Tables

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016a**

## Description

Interpolate between matrices

The Matrix Interpolation block performs interpolation (or extrapolation) on
an N-dimensional table by using pre-calculated indices and fraction values. Each data
point can be a matrix. It supports interpolation up to three breakpoint dimensions. If
you specify *n* dimensions for the breakpoints, and each data point in
your table is a matrix that has *m* dimensions, then the number of
dimensions for your table data is *m+n*. The last *n*
dimensions of the table data must be the length of breakpoints in each interpolation
dimension. The first *m* dimensions of the matrix are each a data
point.
