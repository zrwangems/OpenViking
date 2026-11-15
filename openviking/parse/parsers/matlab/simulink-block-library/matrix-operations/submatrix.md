---
type: simulink-block
title: 'Submatrix'
family: matrix-operations
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'submatrix'
---

# Submatrix

Select subset of elements (submatrix) from matrix input

## Libraries

Simulink / Matrix Operations

## Description

The Submatrix block extracts a contiguous submatrix, *y*,
from the *M*-by-*N* input matrix `u`.
For more information about selecting the rows and columns to extract, see Range Specification Options.

## Ports

### Input

### **Port\_1** — Input signal vector | matrix

Input signal, from which the block extracts the specified
submatrix.

This block supports Simulink® virtual buses.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### Output

### **Port\_1** — Selected submatrix vector | matrix

Submatrix selected from the input signal. The data type of the output
is the same as the input.

This block supports Simulink virtual buses.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

## Parameters

For more information about selecting the subset of elements to form the submatrix, see Range Specification Options.

### **Row span** — Range of rows `All rows` (default) | `One row` | `Range of rows`

The range of input rows to be retained in the output.

### **Row** — First row of output `First` (default) | `Index` | `Offset from last` | `Last` | `Offset from middle` | `Middle`

The input row to be used as the first and only row of the output.

#### Dependencies

To enable this parameter, set **Row span** to
`One row`.

### **Starting row** — First row of output `First` (default) | `Index` | `Offset from last` | `Last` | `Offset from middle` | `Middle`

The input row to be used as the first row of the output.

#### Dependencies

To enable this parameter, set **Row span** to
`Range of rows`.

### **Row index** — Index of first row `1` (default) | positive integer

The index of the input row to be used as the first and only row of the
output, specified as an integer greater than or equal to one.

#### Dependencies

To enable this parameter, set **Row span** to
`One row` and **Row** to
`Index`.

### **Starting row index** — Index of first row `1` (default) | positive integer

The index of the input row to be used as the first row of the output,
specified as an integer greater than or equal to one.

#### Dependencies

To enable this parameter, set **Row span** to
`Range of rows` and **Starting
row** to `Index`.

### **Row offset** — Offset of first row `1` (default) | positive integer

The offset of the input row to be used as the first and only row of the
output, specified as an integer greater than or equal to one.

#### Dependencies

To enable this parameter, set **Row span** to
`One row` and **Row** to
`Offset from last` or `Offset
from middle`.

### **Starting row offset** — Offset of first row `1` (default) | positive integer

The offset of the input row to be used as the first row of the output,
specified as an integer greater than or equal to one.

#### Dependencies

To enable this parameter, set **Row span** to
`Range of rows` and **Starting
row** to `Offset from last` or
`Offset from middle`.

### **Ending row** — Last row `Last` (default) | `Index` | `Offset from last` | `Offset from middle` | `Middle`

The input row to be used as the last row of the output.

#### Dependencies

To enable this parameter, set **Row span** to
`Range of rows` and set **Starting
row** to any value except
`Last`.

### **Ending row index** — Index of last row `1` (default) | positive integer

The index of the input row to be used as the last row of the output,
specified as an integer greater than or equal to one.

#### Dependencies

To enable this parameter, set **Ending row** to
`Index`.

### **Ending row offset** — Offset of last row `1` (default) | positive integer

The offset of the input row to be used as the last row of the
output.

#### Dependencies

To enable this parameter, set **Ending row** to
`Offset from middle` or `Offset
from last`.

### **Column span** — Range of input columns `All columns` (default) | `One column` | `Range of columns`

The range of input columns to be retained in the output.

### **Column** — First column `First` (default) | `Index` | `Offset from last` | `Last` | `Offset from middle` | `Middle`

The input column to be used as the first and only column of the output.

#### Dependencies

To enable this parameter, set **Column span** to
`One column`.

### **Starting column** — First column `First` (default) | `Index` | `Offset from last` | `Last` | `Offset from middle` | `Middle`

The input column to be used as the first column of the output.

#### Dependencies

To enable this parameter, set **Column span** to
`Range of columns`.

### **Starting column index** — Index of first column `1` (default) | positive integer

The index of the input column to be used as the first column of the
output, specified as an integer greater than or equal to one.

#### Dependencies

To enable this parameter, set **Column span** to
`Range of columns` and **Starting
column** to `Index`.

### **Column index** — Index of first column `1` (default) | positive integer

The index of the input column to be used as the first and only column of
the output, specified as an integer greater than or equal to one.

#### Dependencies

To enable this parameter, set **Column span** to
`One column` and
**Column** to
`Index`.

### **Column offset** — Offset of first column `1` (default) | positive integer

The offset of the input column to be used as the first and only column of
the output, specified as an integer greater than or equal to one.

#### Dependencies

To enable this parameter, set **Column span** to
`One column` and
**Column** to `Offset from
last` or `Offset from
middle`.

### **Starting column offset** — Offset of first column `1` (default) | positive integer

The offset of the input column to be used as the first column of the
output, specified as an integer greater than or equal to one.

#### Dependencies

To enable this parameter, set **Column span** to
`Range of columns` and **Starting
column** to `Offset from last` or
`Offset from middle`.

### **Ending column** — Last column `Last` (default) | `Index` | `Offset from last` | `Offset from middle` | `Middle`

The input column to be used as the last column of the output.

#### Dependencies

To enable this parameter, set **Column span** to
`Range of columns` and set
**Starting column** to any value except
`Last`.

### **Ending column index** — Index of last column `1` (default) | positive integer

The index of the input column to be used as the last column of the output,
specified as an integer greater than or equal to one.

#### Dependencies

To enable this parameter, set **Ending column** to
`Index`.

### **Ending column offset** — Offset of last column `1` (default) | positive integer

The offset of the input column to be used as the last column of the
output.

#### Dependencies

To enable this parameter, set **Ending column** to
`Offset from middle` or `Offset
from last`.

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2021b: Create Submatrix Block Moved to Simulink Matrix Operations Library

The Submatrix block has been moved from the **DSP System Toolbox** > **Math Functions** > **Matrices and Linear Algebra** > **Matrix Operations** library to the **Simulink** > **Matrix Operations**library. All existing models continue to work.
