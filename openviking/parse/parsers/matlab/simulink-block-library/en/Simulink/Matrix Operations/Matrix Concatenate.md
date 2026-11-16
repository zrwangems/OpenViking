---
type: simulink-block
title: 'Matrix Concatenate'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'matrixconcatenate'
documentation_source_path: '../simulink/slref/matrixconcatenate.html'
language: en
---

# Matrix Concatenate

## Ports

### Input

### **Port\_1** — First input to concatenate scalar | vector | matrix | array

First input to concatenate, specified as a scalar, vector, matrix, or array.

- Inputs must be of the same data type.
- Matrix and array inputs are supported only when you set
  **Mode** to `Multidimensional
  array`.

When the data type is a `Simulink.Bus` object, the inputs must be nonvirtual buses.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **Port\_N** — *N*th input to concatenate scalar | vector | matrix | array

*N*th input to concatenate, specified as a scalar, vector, matrix, or array.

- Inputs must be of the same data type.
- Matrix and array inputs are supported only when you set
  **Mode** to `Multidimensional
  array`.

#### Dependencies

To add input ports, set **Number of inputs** to an integer greater than or
equal to 2.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### Output

### **Port\_1** — Concatenation of input signals scalar | vector | matrix | array

Concatenation of input signals along specified dimension. Outputs have the same data type as the input.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Number of inputs** — Number of input ports `2` (default) | positive integer

Specify the number of inputs for the block as a real-valued, positive integer, less
than or equal to 65536.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `NumInputs` |
| **Values:** | `'2'` (default) | positive integer in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param(gcb,'NumInputs','3')`

### **Mode** — Type of concatenation `Vector` | `Multidimensional array`

Select whether the block operates in vector or multidimensional array concatenation mode. The default **Mode** of the Vector Concatenate block is `Vector`. The default **Mode** of the Matrix Concatenate block is `Multidimensional array`.

- When you select `Vector`, the block performs vector concatenation.
- When you select `Multidimensional array`, the block performs matrix concatenation.

| **Mode** Setting | Input Signals | Output Signal |
| --- | --- | --- |
| `Vector` | - Vectors - Row vectors (1-by-*M* matrices) - Column vectors (*M*-by-1 matrices) - Combination of vectors and either row or column vectors | When all inputs are vectors, the output is a vector.  If any of the inputs are row or column vectors, the output is a row or column vector, respectively. |
| `Multidimensional array` | Signals of any dimensionality (scalars, vectors, and matrices) | The output is always an array.  Trailing dimensions are assumed to be `1` for lower dimensionality inputs. For example, if the output is 4-D and the input is `[2x3]` (2-D), this block treats the input as `[2x3x1x1]`.  Concatenation is on the dimension that you specify with the **Concatenate dimension** parameter. |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Mode` |
| **Values:** | `'Vector'` | `'Multidimensional array'` |

**Example:** `set_param(gcb,'Mode','Vector')`

### **Concatenate dimension** — Output dimension along which to concatenate input arrays scalar integer

Specify the output dimension along which to concatenate the input arrays.

- `1` — Concatenate inputs vertically. The vertical matrix
  concatenation stacks the input matrices on top of each other in the output matrix.
  When you insert a Vector Concatenate block and set
  **Mode** to `Multidimensional array`,
  the default is `1`.
- `2` — Concatenate inputs horizontally. The horizontal matrix
  concatenation places the input matrices side-by-side in the output matrix. When you
  insert a Matrix Concatenate block, the default is
  `2`.
- `3` or more — Perform multidimensional concatenation on the
  inputs.

The input matrices must have compatible sizes for concatenation. Vertical
concatenation requires the input matrices to have the same number of columns. Horizontal
concatenation requires input matrices to have the same number of rows.

#### Dependencies

To enable this parameter, set **Mode** to `Multidimensional array`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ConcatenateDimension` |
| **Values:** | scalar integer in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param(gcb,'ConcatenateDimension','2')`

## Libraries

Simulink / Math Operations Simulink / Matrix Operations DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Operations HDL Coder / Math Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `image` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Data Type Support**

The block supports these data types for HDL code generation:

| Input Port | Dimension | Fixed-Point | Floating-Point | Built-in Integers | Bus | Boolean | Enumerated | Complex Signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | Scalar  Vector  Matrix (up to 2-D) | Yes | Half  Single  Double | No | Yes | Yes | Yes | Yes |

**Optimizations**

The block participates in these HDL optimizations to optimize the speed, and
area.

**Area Optimization**

| Optimization | Description |
| --- | --- |
| Resource Sharing (HDL Coder) | *Resource sharing* is an area optimization in which HDL Coder identifies multiple functionally equivalent resources and replaces them with a single resource. |
| Streaming (HDL Coder) | *Streaming* is an area optimization in which HDL Coder transforms a vector data path to a scalar data path (or to several smaller-sized vector data paths). |

**Speed Optimization**

| Optimization | Description |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *Distributed pipelining*, or register retiming, is a speed optimization that moves existing delays in a design to reduce the critical path while preserving functional behavior. |
| Clock-Rate Pipelining (HDL Coder) | *Clock-rate pipelining* is an optimization framework in HDL Coder that allows other speed and area optimizations to introduce latency at the clock rate. |
| Adaptive Pipelining (HDL Coder) | *Adaptive pipelining* optimization creates patterns or combination of blocks with registers that can improve the achievable clock frequency and reduce the area usage on the FPGA boards by inserting pipeline registers to the blocks in your design. |
| Critical Path Estimation (HDL Coder) | To quickly identify the most likely critical path in your design, use *Critical Path Estimation*. Critical path estimation speeds up the iterative process of finding the critical path. To know blocks that are characterized in critical path estimation, see Characterized Blocks (HDL Coder). |

**FOR-GENERATE Loop Support**

For this block, HDL Coder generates code using `FOR-GENERATE` loop. For
more information, see Unroll For-Generate Loops (HDL Coder)

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2009b**

## Description

Concatenate input matrices of same data type for iterative processing

The Matrix Concatenate block concatenates input signals to create a nonscalar
signal that you can iteratively process with a subsystem, for example, a for-each,
while-iterator, or for-iterator subsystem.

You can use multiple Matrix Concatenate blocks to create the output signal in
stages, but the result is flat along each concatenation dimension, as if you used a single
block to concatenate the signals.

The signals in the output signal appear in the same order as the input signals for the block
along the concatenation dimension. For a description of the port order for various block
orientations, see Identify Port Location on Rotated or Flipped Block.

You must use a Vector Concatenate or Matrix Concatenate block
to define an array of buses. For more information, see Group Nonvirtual Buses in Arrays of Buses.
