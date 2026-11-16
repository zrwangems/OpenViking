---
type: simulink-block
title: 'Overwrite Values'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Operations'
documentation_page: 'overwritevalues'
documentation_source_path: 'ref/overwritevalues.html'
language: en
---

# Overwrite Values

## Ports

### Input

### **A** — Input data scalar | vector | matrix

Specify the input data as a scalar, vector, or a matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `bus`

### **V** — Overwriting values scalar | vector | matrix

Specify the value(s) with which to overwrite the specified portion of
the input matrix. The dimensions of this parameter must match the
dimensions of the portion of the matrix that you specify to overwrite
using the row span and column span related parameters in the block
dialog box.

For more information on how to specify valid overwriting values, see
Valid Overwriting Values.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `bus`
### Output

### **B** — Modified data scalar | vector | matrix

Data that is modified based on the row span and column span related
parameters in the block dialog box, returned as a scalar, vector, or a
matrix.

The output has the same size as the original input signal. The
input(s) and output of this block must have the same data type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `bus`

## Parameters

### **Overwrite** — Overwrite submatrix or diagonal `Submatrix` (default) | `Diagonal`

Specify whether to overwrite a submatrix or a specified portion of the
diagonal.

### **Source of overwriting value(s)** — Source of overwriting values `Specify via dialog` (default) | `Second input port`

Specify the source of overwriting values as one of these options:

- `Specify via dialog` — You
  must provide the overwriting value(s) in the **Overwrite
  with** parameter. The block uses the same
  overwriting values to overwrite the specified portion of the
  input at each time step. To learn how to specify valid
  overwriting values, see Valid Overwriting Values.
- `Second input port` — You must
  provide overwriting values through a second block input port,
  **V**. Use this setting to provide
  different overwriting values at each time step. The output
  inherits its size and rate from the input signal, not the
  overwriting values.

  The rate at which you provide the overwriting values through
  input port **V** must match the rate at which
  the block receives each input matrix at input port
  **A**. In other words, the input signals
  must have the same Simulink® sample time.

### **Overwrite with** — Overwrite with value(s) `0` (default) | scalar | vector | matrix

Specify the value(s) with which to overwrite the specified portion of the
input matrix. The dimensions of this parameter must match the dimensions of
the portion of the matrix that you specify to overwrite using the row span
and column span related parameters in the block dialog box.

For more information on how to specify valid overwriting values, see Valid Overwriting Values.

#### Dependencies

To enable this parameter, set **Source of overwriting
value(s)** to `Specify via
dialog`.

### **Row span** — Span of input rows `Range of rows` (default) | `All rows` | `One row`

Specify the span of the input rows to overwrite. You can set this
parameter to one of these options:

- `Range of rows` — The
  submatrix contains one or more rows of the input, which you must
  specify in the **Starting row** and
  **Ending row** parameters.
- `All rows` — The submatrix
  contains all rows of the input matrix.
- `One row` — The submatrix
  contains only one row of the input matrix, which you must
  specify in the **Row** parameter.

When you set **Row span** to `One
row` or `Range of rows`, you need
to further specify the row(s) contained in the submatrix by setting the
**Row** or **Starting row** and
**Ending row** parameters.

### **Row/Starting row** — Row or starting Row `First` (default) | `Index` | `Offset from last` | `Last` | `Offset from middle` | `Middle`

Specify the input row that is the first row of the submatrix that the
block overwrites. You can set this parameter to one of these options:

- `First` –– First row of the
  input
- `Index` –– Specify the first input
  row using the **Row index** and
  **Starting row index** parameters
- `Offset from last` –– Input row with
  the index *M* − *rowOffset*,
  where *M* is the number of input rows, and
  *rowOffset* is the value you specify in the
  **Row offset** and **Starting row
  offset** parameters
- `Last` –– Last row of the
  input
- `Offset from middle` –– Input row
  with the index `floor`(*M*/2
  + 1 − *rowOffset*), where *M*
  is the number of input rows, and *rowOffset* is
  the value you specify in the **Row offset** and
  **Starting row offset** parameters
- `Middle` –– Input row with the index
  `floor`(*M*/2 + 1),
  where *M* is the number of input rows

#### Dependencies

To enable the **Row** parameter, set **Row
span** to `One row`.

To enable the **Starting row**  parameter, set
**Row span** to `Range of
rows`.

### **Row index/Starting row index** — Row index or starting row index `1` (default) | positive integer

Specify the index of the input row that is the first row of the submatrix
that the block overwrites as a positive integer.

#### Dependencies

To enable the **Row index**  parameter, set
**Row** to `Index`.

To enable the **Starting row index**  parameter, set
**Starting row**  to
`Index`.

### **Row offset/Starting row offset** — Row offset or starting row offset 1 | nonnegative integer

Specify the offset of the input row that is the first row of the submatrix
that the block overwrites. When you set **Row/Starting
row** to one of these options:

- `Offset from last` –– Input row with the
  index *M* − *rowOffset*, where
  *M* is the number of input rows, and
  *rowOffset* is the value you specify in this
  parameter
- `Offset from middle` –– Input row with
  the index `floor`(*M*/2 + 1 −
  *rowOffset*), where *M* is the
  number of input rows, and *rowOffset* is the value
  you specify in this parameter

#### Dependencies

To enable **Row offset**, set
**Row** to `Offset from middle`or `Offset from last`.

To enable **Starting row offset**, set
**Starting row**  to `Offset from
middle` or `Offset from
last`.

### **Ending row** — Ending row `Last` (default) | `Index` | `Offset from last` | `Offset from middle` | `Middle`

Specify the input row that is the last row of the submatrix that the block
overwrites. You can set this parameter to one of these options:

- `Index` –– Specify the ending input
  row using the **Ending row index**
  parameter
- `Offset from last` –– Input row with
  the index *M* − *rowOffset*,
  where *M* is the number of input rows, and
  *rowOffset* is the value you specify in the
  **Ending row offset** parameter
- `Last` –– Last row of the
  input
- `Offset from middle` –– Input row
  with the index `floor`(*M*/2
  + 1 − *rowOffset*), where *M*
  is the number of input rows, and *rowOffset* is
  the value you specify in the **Ending row
  offset** parameter
- `Middle` –– Input row with the index
  `floor`(*M*/2 + 1),
  where *M* is the number of input rows

#### Dependencies

To enable the **Ending row** parameter, set
**Row span** to `Range of
rows` and **Starting row**  to any
option other than `Last`.

### **Ending row index** — Index of last row of submatrix `1` (default) | positive integer

Specify the index of the input row that is the last row of the submatrix
that the block overwrites.

#### Dependencies

To enable this parameter, set **Ending row**  to
`Index`.

### **Ending row offset** — Ending row offset 1 | nonnegative integer

Specify the offset of the input row that is the last row of the submatrix
that the block overwrites. When you set **Ending row** to
one of these options:

- `Offset from last` –– Input row with
  the index *M* − *rowOffset*,
  where *M* is the number of input rows, and
  *rowOffset* is the value you specify in the
  **Ending row offset** parameter
- `Offset from middle` –– Input row
  with the index `floor`(*M*/2
  + 1 − *rowOffset*), where *M*
  is the number of input rows, and *rowOffset* is
  the value you specify in the **Ending row
  offset** parameter

#### Dependencies

To enable this parameter, set **Ending row**  to
`Offset from middle` or `Offset
from last`.

### **Column span** — Span of input columns `Range of columns` (default) | `All columns` | `One column`

Specify the span of the input columns to overwrite. You can set this
parameter to one of these options:

- `Range of columns` — The
  submatrix contains one or more columns of the input, which you
  must specify in the **Starting column** and
  **Ending column** parameters.
- `All columns` — The submatrix
  contains all columns of the input matrix.
- `One column` — The submatrix
  contains only one column of the input matrix, which you must
  specify in the **Column** parameter.

When you set **Column span** to `One
column` or `Range of columns`, you
need to further specify the column(s) contained in the submatrix by setting
the **Column** or **Starting column** and
**Ending column** parameters.

### **Column/Starting column** — Column or starting column `First` (default) | `Index` | `Offset from last` | `Last` | `Offset from middle` | `Middle`

Specify the input column that is the first column of the submatrix that
the block overwrites. You can set this parameter to one of these options:

- `First` –– First column of the
  input
- `Index` –– Specify the first input
  column using the **Column index** and
  **Starting column index** parameters
- `Offset from last` –– Input column
  with the index *N* −
  *colOffset*, where *N* is
  the number of input columns, and *colOffset* is
  the value you specify in the **Column offset**
  and **Starting column offset**
  parameters
- `Last` –– Last column of the
  input
- `Offset from middle` –– Input column
  with the index `floor`(*N*/2
  + 1 − *colOffset*), where *N*
  is the number of input columns, and *colOffset*
  is the value you specify in the **Column
  offset** and **Starting column
  offset** parameters
- `Middle` –– Input column with the
  index `floor`(*N*/2 + 1),
  where *N* is the number of input columns

#### Dependencies

To enable the **Column** parameter, set
**Column span** to `One
column`.

To enable the **Starting column**  parameter, set
 **Column span** to `Range of
columns`.

### **Column index/Starting column index** — Column index or starting column index 1 | positive integer

Specify the index of the input column that is the first column of the
submatrix that the block overwrites as a positive integer.

#### Dependencies

To enable the **Column index** parameter, set
**Column** to
`Index`.

To enable the **Starting column index**  parameter,
set  **Starting column** to
`Index`.

### **Column offset/Starting column offset** — Column offset or starting column offset 1 | nonnegative integer

Specify the offset of the input column that is the first column of the
submatrix that the block overwrites. When you set **Starting
column** to one of these options:

- `Offset from last` –– Input column
  with the index *N* −
  *colOffset*, where *N* is
  the number of input columns, and *colOffset* is
  the value you specify in the **Column offset**
  and **Starting column offset**
  parameters
- `Offset from middle` –– Input column
  with the index `floor`(*N*/2
  + 1 − *colOffset*), where *N*
  is the number of input columns, and *colOffset*
  is the value you specify in the **Column
  offset** and **Starting column
  offset** parameters

#### Dependencies

To enable the **Column offset** parameter, set
**Column** to `Offset from
middle` or `Offset from
last`.

To enable the **Starting column offset** parameter,
set **Starting column**  to `Offset from
middle` or `Offset from
last`.

### **Ending column** — Ending column `Last` (default) | `Index` | `Offset from last` | `Offset from middle` | `Middle`

Specify the input column that is the last column of the submatrix that the
block overwrites. You can set the parameter to one of these options:

- `Last` –– Last column of the
  input
- `Index` –– Specify the input column
  using the **Ending column index**
  parameter
- `Offset from last` –– Input column
  with the index *N* −
  *colOffset*, where *N* is
  the number of input columns, and *colOffset* is
  the value you specify in the **Ending column
  offset** parameter
- `Offset from middle` –– Input column
  with the index `floor`(*N*/2
  + 1 − *colOffset*), where *N*
  is the number of input columns, and *colOffset*
  is the value you specify in the **Ending column
  offset** parameter
- `Middle` –– Input column with the
  index `floor`(*N*/2 + 1),
  where *N* is the number of input columns

#### Dependencies

To enable this parameter, set **Column span** to
`Range of columns`, and **Starting
column** to any option other than
`Last`.

### **Ending column index** — Ending column index `1` (default) | positive integer

Specify the index of the input column that is the last column of the
submatrix that the block overwrites as a positive integer.

#### Dependencies

To enable this parameter, set **Ending column**  to
`Index`.

### **Ending column offset** — Ending column offset `1` | nonnegative integer

Specify the offset of the input column that is the last column of the
submatrix that the block overwrites. When you set **Ending
column** to one of these options:

- `Offset from last` –– Input column
  with the index *N* −
  *colOffset*, where *N* is
  the number of input columns, and *colOffset* is
  the value you specify in this parameter
- `Offset from middle` –– Input column
  with the index `floor`(*N*/2
  + 1 − *colOffset*), where *N*
  is the number of input columns, and *colOffset*
  is the value you specify in this parameter

#### Dependencies

To enable this parameter, set **Ending column**  to
`Offset from middle` or `Offset
from last`.

### **Diagonal span** — Span of diagonal elements `Range of elements` (default) | `All elements` | `One element`

Specify the span of the diagonal elements to be overwritten. You can set
the parameter to one of these options:

- `Range of elements` –– Overwrite a
  portion of the input diagonal, which you must specify in the
  **Starting element** and
  **Ending element**
  parameters.
- `All elements` –– Overwrite the
  entire input diagonal.
- `One element` –– Overwrite one
  element in the diagonal, which you must specify in the **Element** parameter.

When you set **Diagonal span** to `One
element` or `Range of elements`,
you need to further specify the diagonal element(s) to overwrite by setting
the **Element** or **Starting element**
and **Ending element** parameters.

#### Dependencies

To enable this parameter, set **Overwrite** to
`Diagonal`.

### **Element/Starting element** — Element or starting element `Index` (default) | `First` | `Offset from last` | `Last` | `Offset from middle` | `Middle`

Specify the input diagonal element that is the first element in the
subdiagonal that the block overwrites. You can set this parameter to one of
these options:

- `Index` –– *k*th
  diagonal element, where *k* is the value of
  the **Element index** or **Starting
  element index** parameter
- `First` –– Diagonal element in first
  row of the input
- `Offset from last` –– Diagonal
  element in the row with the index *M* −
  *offset*, where *M* is the
  number of input rows, and *offset* is the value
  you specify in the **Element offset** and
  **Starting element offset**
  parameters
- `Last` –– Diagonal element in the
  last row of the input
- `Offset from middle` –– Diagonal
  element in the input row with the index
  `floor`(*M*/2 + 1 −
  *offset*), where *M* is
  the number of input rows, and *offset* is the
  value you specify in the **Element offset** and
  **Starting element offset**
  parameters
- `Middle` –– Diagonal element in the
  input row with the index
  `floor`(*M*/2 + 1),
  where *M* is the number of input rows

#### Dependencies

To enable the **Element** parameter, set
**Element span** to `One
element`.

To enable the **Starting element**  parameter, set
 **Element span** to `Range of
elements`.

### **Element index/Starting element index** — Element or starting element index `2` (default) | positive integer

Specify the index of the input diagonal element that is the first element
of the subdiagonal that the block overwrites as a positive integer.

#### Dependencies

To enable the **Element index** parameter, set
**Element** to
`Index`.

To enable the **Starting element index** parameter,
set **Starting element** to
`Index`.

### **Ending element** — Ending element `Index` (default) | `Offset from last` | `Last` | `Offset from middle` | `Middle`

Specify the input diagonal element that is the last element of the
subdiagonal that the block overwrites. You can set this parameter to one of
these options:

- `Index` –– *k*th
  diagonal element, where *k* is the value of
  the **Ending element index** parameter
- `Last` –– Diagonal element in the
  last row of the input
- `Offset from last` –– Diagonal
  element in the row with the index *M* −
  *offset*, where *M* is the
  number of input rows, and *offset* is the value
  you specify in the **Ending element offset**
  parameter
- `Offset from middle` –– Diagonal
  element in the input row with the index
  `floor`(*M*/2 + 1 −
  *offset*), where *M* is
  the number of input rows, and *offset* is the
  value you specify in the **Ending element
  offset** parameter
- `Middle` –– Diagonal element in the
  input row with the index
  `floor`(*M*/2 + 1),
  where *M* is the number of input rows

#### Dependencies

To enable this parameter, set **Element span** to
`Range of elements`, and **Starting
element** to any option but
`Last`.

### **Ending element index** — Ending element index `4` (default) | positive integer

Specify the index of the input diagonal element that is the last element
of the subdiagonal that the block overwrites as a positive integer.

#### Dependencies

To enable this parameter, set **Ending element**  to
`Index`.

### **Element offset/Starting element offset** — Element offset or starting element offset `2` | integer (for offset from middle) | nonnegative integer (for offset from last)

Specify the offset of the input diagonal element that is the first element
of the subdiagonal that the block overwrites. When you set
**Starting element** to:

- `Offset from middle` –– Specify the
  value of this parameter as an integer.
- `Offset from last` –– Specify the
  value of this parameter as a nonnegative integer.

#### Dependencies

To enable **Element offset**, set
**Element** to `Offset from
middle` or `Offset from
last`.

To enable **Starting element offset**, set
**Starting element** to `Offset from
middle` or `Offset from
last`.

### **Ending element offset** — Ending element offset `4` | nonnegative integer

Specify the offset of the input diagonal element that is the last element
of the subdiagonal that the block overwrites as a nonnegative
integer.

#### Dependencies

To enable this parameter, set **Ending element** to
`Offset from middle` or `Offset
from last`.

## Libraries

DSP System Toolbox / Signal Management / Indexing / Matrix Operations DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

## Version History

**Introduced before R2006a**

## Description

Overwrite submatrix or subdiagonal of input

The Overwrite Values block overwrites a contiguous submatrix or subdiagonal
of an input matrix. You can provide the overwriting values by typing them in a block
parameter or through an additional input port, which is useful for providing overwriting
values that change at each time step.
