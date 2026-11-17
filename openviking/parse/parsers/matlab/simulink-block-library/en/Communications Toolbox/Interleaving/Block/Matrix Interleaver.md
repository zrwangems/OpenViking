---
type: simulink-block
title: 'Matrix Interleaver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Interleaving / Block'
documentation_page: 'matrixinterleaver'
documentation_source_path: 'ref/matrixinterleaver.html'
language: en
---

# Matrix Interleaver

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters: []
```

**Number of rows**
:   The number of rows in the matrix that the block uses for its
    computations.

**Number of columns**
:   The number of columns in the matrix that the block uses for its
    computations.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Permute input symbols by filling matrix by rows and emptying it by columns

The Matrix Interleaver block performs block interleaving by filling a matrix with the
input symbols row by row and then sending the matrix contents to the output port column
by column.

The **Number of rows** and **Number of columns**
parameters are the dimensions of the matrix that the block uses internally for its
computations.

This block accepts a column vector input signal. The number of elements of the input
vector must be the product of **Number of rows** and **Number
of columns**.

The block accepts the following data types: `int8`,
`uint8`, `int16`, `uint16`,
`int32`, `uint32`, `boolean`,
`single`, `double`, and fixed-point. The output
signal inherits its data type from the input signal.
