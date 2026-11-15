---
type: simulink-block
title: 'For Each'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Modeling / Design Model Behavior / Iterator Subsystems'
documentation_page: 'foreach'
documentation_source_path: 'slref/foreach.html'
language: en
---

# For Each

## Ports

### Output

### **Partition index** — Index of current partition scalar

Index of current partition (starting at zero), returned as a
scalar.

#### Dependencies

To enable this port, select **Show partition index output
port**.

**Data Types:** `int32` | `double`

## Parameters

### Input Partition Tab

Select each input signal you want to partition and specify the corresponding
**Partition Dimension**, **Partition Width**,
and **Partition offset** parameters. For more information, see
Inport.

### **Port** — List of input ports Read-only: input port name

This parameter is read-only.

List of input ports connected to the For Each Subsystem
block.

### **Partition** — Select input port signals to partition `off` (default) | `on`

Select input port signals connected to the For Each
Subsystem block to partition into subarrays or elements. For
each port listed in the **Port** column, select the
corresponding check box to partition that signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InputPartition` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Partition Dimension** — Specify dimension `1` (default) | `2` | positive integer

Specify the dimension through which to slice the selected input signal
array. The resulting slices are perpendicular to the dimension that you
specify. The slices partition the array into subarrays or elements, as
appropriate.

`1`
:   Slice input array along the columns.

`2`
:   Slice input array along the rows.

`n`
:   Slice input array along dimension
    `n`.

#### Dependencies

To enable this parameter, select **Partition**
for the relevant input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InputPartitionDimension` |
| **Type**: cell array of character vectors |
| **Values**: `{'1'}` | `{'2'}` | positive integer |
| **Default**: `{'1'}` |

### **Partition Width** — Specify width `1` (default) | positive integer

Specify the width of each partition slice of the selected input
signal.

#### Dependencies

To enable this parameter, select **Partition**
for the relevant input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InputPartitionWidth` |
| **Type**: cell array of character vectors |
| **Values**: `{'1'}` | integer |
| **Default**: `{'1'}` |

### **Partition Offset** — Specify partition offset `0` (default) | integer

Specify the offset for each partition slice of the selected input
signal.

`0`
:   No offset between partition slices, that is, partition
    slices have no gaps between them and do not overlap.

integer
:   Specify partition offset, using a positive integer to
    specify a gap between slices or a negative integer to
    indicate an overlap. The sum of the **Partition
    Width** and the **Partition
    Offset** must be a positive integer.

    For example, a **Partition Width** of
    `3` and a **Partition
    Offset** of `-2` indicates
    that each 3-element slice overlaps its neighboring slices by
    2 elements; whereas a **Partition Width**
    of `2` and a **Partition
    Offset** of `1` indicates that
    there is a 1-element-wide gap between each pair of
    neighboring 2-element-wide slices.

#### Dependencies

To enable this parameter, select **Partition**
for the relevant input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InputPartitionOffset` |
| **Type**: cell array of character vectors |
| **Values**: `{'0'}` | integer |
| **Default**: `{'0'}` |

### Parameter Partition Tab

Select each mask parameter you want to partition and specify the corresponding
**Partition Dimension** and **Partition
Width** parameters.

### **Parameter** — List of mask parameters Read-only: parameter name

This parameter is read-only.

List of mask parameters for the For Each Subsystem
block.

#### Dependencies

Mask parameters appear in the list only if you have added an
editable parameter to the mask of the For Each
Subsystem block. See Author Block Masks.

### **Partition** — Select mask parameters to partition `off` (default) | `on`

Select mask parameters for the For Each Subsystem block
to partition into subarrays or elements. For each port listed in the
**Parameter** column, select the corresponding
check box to partition that mask parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SubsysMaskParameterPartition` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Partition Dimension** — Specify dimension `1` (default) | `2` | positive integer

Specify the dimension through which to slice the selected mask
parameter array. The resulting slices are perpendicular to the dimension
that you specify. The slices partition the array into subarrays or
elements, as appropriate.

`1`
:   Slice mask parameter array along the columns.

`2`
:   Slice mask parameter array along the rows.

`n`
:   Slice mask parameter array along dimension
    `n`.

#### Dependencies

To enable this parameter, select **Partition**
for the relevant mask parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SubsysMaskParameterPartitionDimension` |
| **Type**: cell array of character vectors |
| **Values**: `{'1'}` | integer |
| **Default**: `{'1'}` |

### **Partition Width** — Specify partition width `1` (default) | positive integer

Specify the width of each partition slice of the selected mask
parameter array.

#### Dependencies

To enable this parameter, select **Partition**
for the relevant mask parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SubsysMaskParameterPartitionWidth` |
| **Type**: cell array of character vectors |
| **Values**: `{'1'}` | positive integer |
| **Default**: `{'1'}` |

### Output Concatenation Tab

For each output port, specify the dimension along which to stack (concatenate) the
For Each Subsystem block results. For more information, see
Outport.

### **Port** — List of output ports Read-only: output port name

This parameter is read-only.

List of output ports connected to the For Each
Subsystem block.

### **Concatenation Dimension** — Specify dimension `1` (default) | `2` | positive integer

For each output port, specify the dimension along which to stack the
results of the For Each Subsystem block.

`1`
:   Stack the results in the
    *d*1 direction,
    that is, vertically. If the block generates column vectors,
    the concatenation process results in a single column vector.
    If the block generates row vectors, the concatenation
    process results in a matrix.

`2`
:   Stack the results in the
    *d*2 direction,
    that is, horizontally. If the block generates row vectors,
    the concatenation process results in a single row vector. If
    the block generates row vectors, the concatenation process
    results in a matrix.

`n`
:   Stack the results in the
    *d*n
    direction.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputConcatenationDimension` |
| **Type**: cell array of character vectors |
| **Values**: `{'1'}` | integer |
| **Default**: `{'1'}` |

### Other Parameters

### **Show partition index output port (zero-based indexing)** — Control display of output port `off` (default) | `on`

Control display of output port for partition index.

off
:   Hide output port.

on
:   Display output port on block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ShowIterationIndex` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Partition index output data type** — Specify partition index data type `'int32'` (default) | `'double'`

Specify partition index data type for output port.

`int32`
:   Select signed 32-bit integer.

`double`
:   Select double real.

#### Dependencies

To enable this parameter, select **Show partition index
output port**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IterationIndexDataType` |
| **Type**: character vector |
| **Values**: `'int32'` | `'double'` |
| **Default**: `'int32'` |

### **Number of iterations** — Specify number of partitions to process `-1` (default) | integer

To process a subset of data, specify the number of partition slices of
the input signal or mask parameter array to process, else specify
`-1` to process all slices. The number must not be
greater than the total number of slices available.

`-1`
:   Process all slices

integer
:   Number of slices to process

    For example, a **Number of iterations**
    of `3` indicates that only the first 3
    slices are to be processed.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SpecifiedNumIters` |
| **Type**: character vector |
| **Values**: `'-1'` | integer in quotes |
| **Default**: `'-1'` |

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual code generation support depends on block implementation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type support depends on block implementation.

## Version History

**Introduced in R2010a**

### R2024b: Add signal breakpoints and port value labels to iteration number outputs in iterator subsystems

You can now pause a simulation on a particular iteration of an iterator subsystem by adding
signal breakpoints to signals produced by:

- Iteration number output ports of While Iterator blocks inside While Iterator Subsystem blocks
- Iterator value output ports of For Iterator blocks inside For Iterator Subsystem blocks
- Partition index output ports of For Each blocks inside For Each Subsystem blocks

In previous releases, you could add a breakpoint in these locations, but the breakpoints
did not pause the simulation and appeared as invalid in the block diagram.

Port value labels at the same locations now display the iteration number. In previous releases, port value labels at these locations showed `inaccessible`.

For an example, see Debug Simulation of Iterator Subsystem.

## Description

Control block for for-each subsystem

The For Each block serves as a control block for the For
Each Subsystem block. Specifically, the For Each block enables the
blocks inside the for-each subsystem to process the elements of either input signals or mask
parameters independently. Each block inside this subsystem that has states maintains a
separate set of states for each element or subarray that it processes. As the set of blocks in
the subsystem processes the elements or subarrays, the subsystem concatenates the results to
form output signals.

For Each Subsystem block icon, displayed alongside contents of for-each subsystem

Use a for-each subsystem to iteratively compute outputs after changing inputs or mask
parameters. To do so, configure the partitioning of input signals or mask parameters in the
For Each block dialog box.

### Partition Input Signals to the Subsystem

To specify which input signals to partition for each iteration in a for-each
subsystem, use the **Input Partition** tab in the dialog box of the
For Each block. When specifying a signal to be partitioned, specify the
**Partition Dimension**, **Partition Width**, and
**Partition Offset** parameters.

### Partition Mask Parameters of the Subsystem

You can partition the mask parameters of a For Each Subsystem
block. Partitioning is useful for systems that have identical structures in each iteration
but different parameter values. In this case, changing the model to partition extra input
signals for each parameter is cumbersome. Instead, add a mask parameter to a for-each
subsystem. For more information, see Create a Simple Mask. To select the mask
parameter for partitioning, use the **Parameter Partition** tab of the
For Each block dialog box. For more information, see Select Partition Parameters, below.

### Concatenate Output

Define the dimension along which to concatenate the results by specifying the
**Concatenation Dimension** in the **Output
Concatenation** tab.

The results generated by the block for each subarray are stacked along the
concatenation dimension. By default, dimension 1 (*y*-axis) is
used, meaning that the results are stacked vertically. However, if you specify a
concatenation dimension of 2, the results concatenate along the horizontal direction
(*x*-axis). Thus, if the process generates row vectors, then
the concatenated result is a matrix in the first case and a row vector in the second
case.

### Select Partition Parameters

When selecting an input signal or subsystem mask parameter for partitioning, you
need to specify how to decompose it into elements or subarrays for each iteration.
Do this by setting integer values for the **Partition Dimension**,
**Partition Width**, and **Partition Offset**
parameters.

As an illustration, consider an input signal matrix `A` of the
form:

3-by-3 matrix A with all 9 elements displayed, showing d1 as the vertical dimension and d2 as the horizontal dimension

The labels *d*1 and
*d*2, respectively, define dimensions 1
and 2. If you retain the default setting of `1` for both the
partition dimension and the partition width, and `0` for the
partition offset, then Simulink® slices perpendicular to partition dimension 1 at a width equal to the
partition width, that is one element:

3-by-3 matrix A, with all 9 elements showing, partitioned into rows

Matrix A decomposes into these three row vectors:

3-by-3 matrix A, decomposed into 3 3-element row vectors

If instead you specify `2` as the partition dimension,
Simulink slices perpendicular to dimension 2 to form three column
vectors:

3-by-3 matrix A, decomposed into 3 3-element column vectors

In addition to setting the **Partition Dimension** to
`2`, if you set the **Partition Width** to
`2` and the **Partition Offset** to
`-1`, Simulink uses two overlapping 3-by-2 partitions for processing.

3-by-3 matrix A, decomposed into 2 overlapping 3-by-2 matrices

By default, all partitions of the input signal or mask parameter are processed. To
process a subset of the partitions, enter the number of partitions to process as the
**Number of iterations**. In the matrix examples above, if
**Partition Offset** is set to `0` (the
default) and **Number of iterations** is set to
`2`, only the first 2 rows or columns of the input matrix
`A` are processed.

**Note**

Only signals are considered one-dimensional in Simulink. Mask parameters are row or column vectors, according to their
orientation. To partition a row vector, specify the partition dimension as 2
(along the columns). To partition a column vector, specify the partition
dimension as 1 (along the rows).
