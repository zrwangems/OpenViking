---
type: simulink-block
title: 'Block Processing'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'blockprocessing'
documentation_source_path: 'ref/blockprocessing.html'
language: en
---

# Block Processing

## Ports

### Input

### **I** — Input signal matrix

Input signal, specified as an *M*-by-*N*
matrix. This port is unnamed unless you select the **Add port to
supply subsystem parameters** parameter or set the **Number of inputs** parameter to `2` or more. If you
select **Add port to supply subsystem parameters**
parameter, the port name becomes **I**. If you set
**Number of inputs** to a value greater than
`1`, *n*, then block has *n*
input ports from **I** to **In**. The contents of the subsystem determines the data type of the input
data.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

### **P** — Additional input to supply subsystem parameters scalar | vector | matrix | array

Additional input to supply subsystem parameters, specified as a scalar, vector,
matrix, or array. The contents of the subsystem determines the data type of the input
data.

#### Dependencies

To enable this port, you must select the **Add port to
supply subsystem parameters** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `string`
### Output

### **Port\_1** — Output signal matrix

Output data, returned as a matrix. The value of the **Number
of outputs** determines the number of output ports. The contents of the
subsystem determine the data type of the output data.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### **Number of inputs** — Number of inputs `1` (default) | positive scalar

Specify the number of input ports to the Block Processing block as a positive
scalar.

### **Add port to supply subsystem parameters** — Subsystem parameter input port `off` (default) | `on`

Select this parameter to add an additional input port to the Block Processing block
for supplying subsystem parameters.

### **Number of outputs** — Number of outputs `1` (default) | positive scalar

Specify the number of output ports on the Block Processing block as a positive
scalar.

### **Block size** — Block size `{[8 8]}` (default) | cell array

Specify the size of each block as a cell of two-element vectors. The cell array
must contain either a single cell or one cell for each input port. If the block has one
input port, enter only one vector. If the block has more than one input port, you can
enter one vector to use for all inputs, or you can specify an individual vector for each
input. The block uses the vectors in the order you enter them.

### **Overlap** — Block overlap `{[0 0]}` (default) | cell array

Specify the overlap of each block as cell of two-element vectors. The cell array
must contain either a single cell or one cell for each input port. If the block has one
input port, enter only one vector. If the block has more than one input port, you can
enter one vector to use for all inputs, or you can specify an individual vector for each
input. The block uses the vectors in the order you enter them.

### **Traverse order** — Order of block extraction `Row-wise` (default) | `Column-wise`

Specify the traverse order with which the Block Processing block extracts
submatrices from the input matrix. If you select `Row-wise`,
the block extracts submatrices by moving across the rows. If you select
`Column-wise`, the block extracts submatrices by moving down
the columns

**Subsystem**

To configure the subsystem of the Block Processing block.

- Click **Open Subsystem** to open the Block Processing
  subsystem.
- Drag blocks into this subsystem to define the processing operations the block
  performs on the submatrices.

## Libraries

Computer Vision Toolbox / Utilities

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `doublea` | `fixed pointa` | `integera` | `singlea` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
|  |  |
| --- | --- |
| a The blocks inside the subsystem dictate the data types supported by this block. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Repeat user-specified operation on blocks of input matrix

The Block Processing block extracts submatrices, or *blocks* , from
an input matrix, passes each block to a subsystem that performs a user-specified operation. It
then reassembles the processed blocks to form the output matrix. You can use this block to
process an image block-wise, rather than processing the entire image at once. Matrix block
processing proceeds from input matrix to extracted blocks, then the subsystem, and then
recombines the processed blocks into an output matrix.
