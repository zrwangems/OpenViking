---
type: simulink-block
title: 'Selector'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Attributes and Indexing'
documentation_page: 'selector'
documentation_source_path: '../simulink/slref/selector.html'
language: en
---

# Selector

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | multidimensional

Input signal and source of elements to output signal.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **IndxN** — `N`th index signal scalar | vector | matrix

External port specifying an index for the selection of the
corresponding output element.

You can specify integer of custom width (for example, a 15-bit integer
or 23-bit integer) as an index signal value. When you configure the
width of the integer, you must specify the **Mode** as
`Fixed point`, with **Word
length** less than or equal to 65,535,
**Slope** equal to 1, and **Bias**
equal to 0. For more information on specifying a fixed-point data type,
see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable an external index port, in the corresponding row of the
**Index Option** table, set **Index
Option** to `Index vector
(port)`, `Starting index
(port)`, or `Starting and ending
indices (port)`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Port\_1** — Output signal scalar | vector | matrix | multidimensional

Output signal generated from selected or reordered elements of input
signal.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## Parameters

### **Number of input dimensions** — Number of dimensions of input signal `1` (default) | integer

Specifies the number of dimensions of the input signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumberOfDimensions` |
| **Type:** character vector |
| **Values:** `integer` |
| **Default:** `'1'` |

### **Index mode** — Index mode `One-based` (default) | `Zero-based`

Specifies the indexing mode. If `One-based` is selected,
an index of 1 specifies the first element of the input vector. If
`Zero-based` is selected, an index of 0 specifies the
first element of the input vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IndexMode` |
| **Type:** character vector |
| **Values:** `'One-based' | 'Zero-based'` |
| **Default:** `'One-based'` |

### **Index Option** — Index method for elements `Index vector (dialog)` (default) | `Select all` | `Index vector (port)` | `Starting index (dialog)` | `Starting index (port)` | `Starting and ending indices (port)`

Defines, by dimension, how the elements of the signal are to be indexed.
From the list, select:

- `Select all`

  No further configuration is required. All elements are
  selected.
- `Index vector (dialog)`

  Enables the **Index** column. Enter the vector of
  indices of the elements.
- `Index vector (port)`

  No further configuration is required.
- `Starting index (dialog)`

  Enables the **Index** and **Output
  Size** columns. Enter the starting index of the range
  of elements to select in the **Index** column and
  the number of elements to select in the **Output
  Size** column.
- `Starting index (port)`

  Enables the **Output Size** column. Enter the
  number of elements to be selected in the **Output
  Size** column.

- `Starting and ending indices
  (port)`

  No further configuration is required.

  Using this option results in a variable-size output signal. When
  you update, the output dimension is set to be the same as the input
  signal dimension. During execution, the output dimension is updated
  based on the signal feeding the index.

  When logging output signal data, signals not selected are padded
  with NaN values.

The **Index** and **Output Size**
columns appear as needed.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IndexOptionArray` |
| **Type:** cell array of character vectors |
| **Values:** `{'Select all'}` | `{'Index vector (dialog)'}` | `{'Index vector (port)'}` | `{'Starting index (dialog)'}` | `{'Starting index (port)'}` | `{'Starting and ending indices (port)'}` |
| **Default:** `{'Index vector (dialog)'}` |

For a character vector instead of a cell array of character vectors,
use `IndexOptions`.

### **Index** — Index of elements `[1 3]` (default) | integer

When the **Index Option** is `Index vector
(dialog)`, enter the index of each element you are
interested in.

When the **Index Option** is `Starting index
(dialog)`, enter the starting index of the range of
elements to be selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IndexParamArray` |
| **Type:** cell array of character vectors |
| **Values:** integers |
| **Default:** `{'[1 3]'}` |

For a character vector instead of a cell array of character vectors,
use `Indices`.

### **Output Size** — Width of block output signal `1` (default) | integer

Specifies the width of the block output signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputSizeArray` |
| **Type:** cell array of character vectors |
| **Values:** integers |
| **Default:** `{'1'}` |

For a character vector instead of a cell array of character vectors,
use `OutputSizes`.

### **Input port size** — Width of input signal `3` (default) | integer

Specify the width of the block input signal for 1-D signals. Enter
`-1` to inherit from the driving block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputPortWidth` |
| **Type:** character vector |
| **Values:** `integer` |
| **Default:** `'3'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Dependencies

This parameter is visible only if you set it to a value other than
`-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar or vector in quotes |

### **Check for out-of-range index in accelerated simulation** — Option to check for out-of-range index values in accelerator and rapid accelerator simulation modes `off` (default) | `on`

Select this check box to have Simulink® check during simulation in accelerator or rapid accelerator
mode whether any index values are outside the range of valid indices for the
relevant dimension of the input signal. If an index is out of range,
Simulink stops the simulation and displays an error message.

**Note**

If you do not select this check box, out-of-range index values
could lead to undefined behavior during accelerator or rapid
accelerator mode simulation.

Simulink performs this check during normal mode simulation regardless
of whether you select this check box.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `RuntimeRangeChecks` |
| **Type:** character vector |
| **Values:** `'Off'` | `'On'` |
| **Default:** `'Off'` |

## Libraries

Simulink / Signal Routing HDL Coder / Signal Routing

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

| Native Floating Point | |
| --- | --- |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, or `Zero` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |

**Data Type Support**

The block supports these data types for HDL code generation:

| Input Port | Dimension | Fixed-Point | Floating-Point | Built-in Integers | Bus | Boolean | Enumerated | Complex Signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Port1** | Scalar  Vector  Matrix (up to 2-D) | Yes | Half  Single  Double | No | Yes | Yes | Yes | Yes |

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

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2023a: Index signal supports integer of custom width

Starting in R2023a, you can customize the width of the integer that you use to
specify the index signal value for the Selector block.

### R2023a: Variable size signal support for `Index vector (dialog)` and `Starting index (dialog)` as **Index Option**

Starting in R2023a, a Selector block that is configured to accept a
1-D variable-size input signal, supports `Index vector
(dialog)` and `Starting index (dialog)` as
the **Index Option**.

This enhancement allows you to choose from all the available **Index
Option** settings when you configure the Selector block
to accept a1-D variable-size input signal.

## Description

Select input elements from vector, matrix, or multidimensional signal

The Selector block extracts selected elements of an input vector,
matrix, or multidimensional signal based on specified indices. The extracted signals can be
grouped differently than the input signals.

Based on the value you enter for the **Number of input dimensions**
parameter, a table of indexing settings is displayed. Each row of the table corresponds
to one of the input dimensions in **Number of input dimensions**. For
each dimension, you define the elements of the signal to work with. Specify a vector
signal as a 1-D signal and a matrix signal as a 2-D signal. When you configure the
Selector block for multidimensional signal operations, the block icon
changes.

For example, assume a 6-D signal with a one-based index mode. The table of the
Selector block dialog box changes to include one row for each
dimension. If you define dimensions as shown in the next table, the output is `Y
= U(1:end,2:6,[1 3 5],Idx4:Idx4+7,Idx5,Idx6(1):Idx6(2))`, where
`Idx4`, `Idx5`, and `Idx6` are
the index ports for dimensions 4, 5, and 6. For more information, see Select Elements from Multidimensional Array Using Selector Block.

| Row | Index Option | Index | Output Size |
| --- | --- | --- | --- |
| 1 | `Select all` |  |  |
| 2 | `Starting index (dialog)` | `2` | `5` |
| 3 | `Index vector (dialog)` | `[1 3 5]` |  |
| 4 | `Starting index (port)` |  | `8` |
| 5 | `Index vector (port)` |  |  |
| 6 | `Starting and ending indices (port)` |  |  |

You can use an array of buses as an input signal to a Selector block.
For details about defining and using an array of buses, see Group Nonvirtual Buses in Arrays of Buses.

**Note**

Selector block does not change the dimensionality (number of
dimensions) of the input signals. If you need to change the dimensionality of the
signal to the dimensions you specify, use Reshape block.
