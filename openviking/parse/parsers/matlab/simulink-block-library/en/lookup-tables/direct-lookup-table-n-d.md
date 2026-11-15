---
type: simulink-block
title: 'Direct Lookup Table (n-D)'
family: lookup-tables
documentation_release: R2025b
official_category: 'Lookup Tables'
documentation_page: 'directlookuptablend'
language: en
---

# Direct Lookup Table (n-D)

Index into n-dimensional table to retrieve element, vector, or 2-D matrix

## Libraries

Simulink / Lookup Tables HDL Coder / Lookup Tables

## Description

The Direct Lookup Table (n-D) block indexes into an n-dimensional table to retrieve an
element, vector, or 2-D matrix. The first selection index corresponds to the top (or
left) input port. You can choose to provide the table data as an input to the block, or
define the table data on the block dialog box. The number of input ports and the size of
the output depend on the number of table dimensions and the output slice you
select.

If you select a vector from a 2-D table, the output vector can be a column or a row,
depending on the model configuration parameter setting **Math and Data Types** > **Use algorithms optimized for row-major array layout**. The block inputs are zero-based indices (for more information, see the
**Inputs select this object from table** parameter.

The Direct Lookup Table block supports symbolic dimensions.

### Block Inputs and Outputs

The Direct Lookup Table (n-D) block uses inputs as zero-based indices into an
*n*-dimensional table. The number of inputs varies with the
shape of the output: an element, vector, or 2-D matrix.

You define a set of output values as the **Table data** parameter. For the
default column-major algorithm behavior, the first input specifies the zero-based
index to the table dimension that is one higher than the output dimensionality. The
next input specifies the zero-based index to the next table dimension, and so
on.

| Output Shape | Output Dimensionality | Table Dimension that Maps to the First Input |
| --- | --- | --- |
| Element | 0 | 1 |
| Vector | 1 | 2 |
| Matrix | 2 | 3 |

Suppose that you want to select a vector of values from a 4-D table.

The following mapping of block input port to table dimension applies.

| This input port... | Is the index for this table dimension... |
| --- | --- |
| 1 | 2 |
| 2 | 3 |
| 3 | 4 |

### Changes in Block Icon Appearance

Depending on parameters you set, the block icon changes appearance. For table dimensions
higher than 4, the icon matches the 4-D version but shows the exact number of
dimensions at the top.

When you use the **Table data** parameter, you see these icons for the
default column-major behavior. Some icons are different when you select the
configuration parameter **Math and Data Types** > **Use algorithms optimized for row-major array layout**.

| Object that Inputs Select from the Table | Number of Table Dimensions | | | |
| --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |
| Element |  |  |  |  |
| Vector |  |  |  |  |
| 2-D Matrix | Not applicable |  |  |  |

When you use the table input port, you see these icons.

| Object that Inputs Select from the Table | Number of Table Dimensions | | | |
| --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |
| Element |  |  |  |  |
| Vector |  |  |  |  |
| 2-D Matrix | Not applicable |  |  |  |

## Ports

### Input

### **Port\_1** — Index `i1` input values scalar | vector

For the default column-major algorithm, the first input port, specifying the zero-based
index to the table dimension that is one higher than the output
dimensionality (0, 1, or 2). The next input specifies the zero-based
index to the next table dimension, and so on. All index inputs must be
real-valued.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **Port\_N** — Index `N` input values scalar | vector

For the default column-major algorithm, the N-th input port,
specifying the zero-based index to the table dimension that is N higher
than the output dimensionality (0, 1, or 2). The number of inputs varies
with the shape of the output. All index inputs must be
real-valued.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **T** — Table data vector | matrix | N-D array

Table data, specified as a vector, matrix, or N-D array. The table size must match the
dimensions of the **Number of dimensions** parameter.
The block's output data type is the same as the table data type.

#### Dependencies

To enable this port, select the **Make table an
input** check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### Output

### **Port\_1** — Output element, vector, or 2-D matrix scalar | vector | 2-D matrix

Output slice, provided as a scalar, vector, or 2-D matrix. The size of the block output
is determined by the setting of the **Inputs select this object
from table** parameter. The output data type is the same as
the table data type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

## Parameters

### Main

#### Table

### **Number of table dimensions** — Number of dimensions of table data `2` (default) | `1` | `3` | `4` | ...

Number of dimensions that the **Table data** parameter must have. This
value determines the number of independent variables for the table and
the number of inputs to the block.

| To specify... | Do this... |
| --- | --- |
| 1, 2, 3, or 4 | Select the value from the menu. |
| A higher number of table dimensions | Enter a positive integer directly in the box.  The maximum number of table dimensions that this block supports is 30. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumberOfTableDimensions` |
| **Type:** character vector |
| **Values:** `'1' | '2' | '3' | '4' | ... |'30'` |
| **Default:** `'2'` |

### **Make table an input** — Provide table data as a block input `off` (default) | `on`

Select this check box to provide table data to the Direct Lookup Table
(n-D) block as a block input. When you select this check box, a new
input port, `T`, appears. Use this port to input the
table data.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableIsInput` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Table data** — Table of output values `[4 5 6; 16 19 20; 10 18 23]` (default) | scalar | vector | matrix | N-D array

Specify the table of output values. The table size must match the
dimensions of the **Number of table dimensions**
parameter.

**Tip**

During block diagram editing, you can leave the **Table
data** field empty. But for simulation, you must match
the number of dimensions in **Table data** to the
**Number of table dimensions**. For details on
how to construct multidimensional MATLAB® arrays, see Multidimensional Arrays.

Click **Edit** to open the Lookup Table Editor. For more information,
see Lookup Table Editor.

#### Dependencies

To enable the **Table data** field, clear the
**Make table an input** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Table` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix | N-D array |
| **Default:** `'[4 5 6;16 19 20;10 18 23]'` |

#### Algorithm

### **Inputs select this object from table** — Specify whether output is an element, vector, or 2-D matrix `Element` (default) | `Vector` | `2-D Matrix`

Specify whether the output data is a single element, a vector, or a
2-D matrix. The number of input ports for indexing depends on your
selection.

| Selection | Number of Input Ports for Indexing |
| --- | --- |
| `Element` | Number of table dimensions |
| `Vector` | Number of table dimensions -1 |
| `2-D Matrix` | Number of table dimensions -2 |

This numbering matches MATLAB indexing. For example, if you have a 4-D table of data,
follow these guidelines.

| To access... | Specify... | As in... |
| --- | --- | --- |
| An element | Four indices | `array(1,2,3,4)` |
| A vector | Three indices | `array(:,2,3,4)` (default column-major algorithm) |
| A 2-D matrix | Two indices | `array(:,:,3,4)` (default column-major algorithm) |

#### Tips

When the **Math and Data Types** > **Use algorithms optimized for row-major array
layout** configuration parameter is set, the Direct Lookup
Table block behavior changes from column-major to row-major. For
this block, the column-major and row-major algorithms may differ
semantically in output calculations, resulting in different
numerical values. For example, assume that **Inputs select
this object from table** parameter is set to
`Vector`. The elements of the selected
vector are contiguous in the table storage memory. This table shows
the column-major and row-major algorithm depending on the table
dimension:

| Table Dimension | Column-Major Algorithm | Row-Major Algorithm |
| --- | --- | --- |
| 2-D table | Column vector is selected | Row vector is selected |
| 3-D and higher table | Output vector is selected from the first dimension of the table | Output vector is selected from the last dimension of the table |

Consider the row-major and column-major direct lookup algorithms
with vector output from a 3-D table. The last dimension is the third
dimension of a 3-D table. Due to semantic changes, column-major and
row-major direct lookup may output different vector size and
numerical values.

This figure shows a Direct Lookup Table (n-D) block configured with a
3-D table and a vector output. By default, the block icon shows the
column-major algorithm.

To have the same block use the row-major algorithm, change the **Math and Data Types** > **Use algorithm optimized for row-major
layout** configuration parameter of the model and recompile.
The block icon changes to reflect the change to the algorithm
optimized for row-major behavior.

For more information on row-major support, see Code Generation of Matrices and Arrays (Simulink Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputsSelectThisObjectFromTable` |
| **Type:** character vector |
| **Values:** `'Element' | 'Vector' | '2-D Matrix'` |
| **Default:** `'Element'` |

### **Diagnostic for out-of-range input** — Block action when input is out of range `Warning` (default) | `None` | `Error`

Specify whether to show a warning or error when an index is out of
range with respect to the table dimension. Options include:

- `None` — Produce no
  response.
- `Warning` — Display a warning
  and continue the simulation.
- `Error` — Terminate the
  simulation and display an error.

When you select `None` or
`Warning`, the block clamps out-of-range
indices to fit table dimensions. For example, if the specified index is
5.3 and the maximum index for that table dimension is 4, the block
clamps the index to 4.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DiagnosticForOutOfRangeInput` |
| **Type:** character vector |
| **Values:** `'None' | 'Warning' | 'Error'` |
| **Default:** `'Warning'` |

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

### Code generation

### **Remove protection against out-of-range input in generated code** — Remove code that checks for out-of-range input values `off` (default) | `on`

Specify whether or not to include code that checks for out-of-range
input values.

| Check Box | Result | When to Use |
| --- | --- | --- |
| `on` | Generated code does not include conditional statements to check for out-of-range breakpoint inputs.  When the input is out-of-range, it may cause undefined behavior for generated code. | For code efficiency |
| `off` | Generated code includes conditional statements to check for out-of-range inputs. | For safety-critical applications |

If your input is not out of range, you can select the **Remove
protection against out-of-range index in generated code**
check box for code efficiency. By default, this check box is cleared.
For safety-critical applications, do not select this check box. If you
want to select the **Remove protection against out-of-range
index in generated code** check box, first check that your
model inputs are in range. For example:

1. Clear the **Remove protection against out-of-range
   index in generated code** check box.
2. Set the **Diagnostic for out-of-range input**
   parameter to `Error`.
3. Simulate the model in normal mode.
4. If there are out-of-range errors, fix them to be in range and
   run the simulation again.
5. When the simulation no longer generates out-of-range input
   errors, select the **Remove protection against
   out-of-range index in generated code** check
   box.

   **Note**

   When you select the **Remove protection against
   out-of-range index in generated code** check
   box and the input is out of range, the behavior is undefined
   for generated code.

Depending on your application, you can run the following Model Advisor
checks to verify the usage of this check box:

- **By Product** > **Embedded Coder** > **Identify lookup table blocks that generate
  expensive out-of-range checking code**
- **By Product** > **Simulink Check** > **Modeling Standards** > **DO-178C/DO-331 Checks** > **Check usage of lookup table
  blocks**

For more information about the Model Advisor, see Run Model Advisor Checks.

Additionally, to determine if it is safe to select this check box, if
you have a Simulink®
Design Verifier™ license, consider using the Detect Block Input Range Violations (Simulink Design Verifier)
check.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RemoveProtectionInput` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### Table Attributes

**Note**

The parameters in the **Table Attributes** pane are not
available if you select **Make table an input**. In this case,
the block inherits all table attributes from the input port with the label
`T`.

### **Table minimum** — Minimum value table data can have `[]` (default) | finite, real, double, scalar

Specify the minimum value for table data. The default value is
`[]` (unspecified).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableMin` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Table maximum** — Maximum value table data can have `[]` (default) | finite, real, double, scalar

Specify the maximum value for table data. The default value is
`[]` (unspecified).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableMax` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Table data type** — Data type of table data `Inherit: Inherit from 'Table data'` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

Specify the table data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit from 'Table
  data'`
- The name of a built-in data type, for example,
  `single`
- The name of a data type class, for example, an enumerated data
  type class
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit from 'Table data'' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'Enum: <class name>'|'<data type expression>'` |
| **Default:** `'Inherit: Inherit from 'Table data''` |

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types you specify on this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed pointa` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a This block supports fixed-point data types for 'Table' data only. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

**MAX 10 Device Settings**

If you use Intel® MAX 10 device, to map the lookup table to RAM, add this Tcl
command when creating the project in the Quartus tool:

`set_global_assignment -name INTERNAL_FLASH_UPDATE_MODE "SINGLE IMAGE
WITH ERAM"`

**Required Block Settings**

- **Number of table dimensions**: Select the table
  dimension between 1 to 30.
- **Make table an input**: Clear this check
  box.
- **Diagnostic for out-of-range input**: Select
  `None`,
  `Warning` (default), or
  `Error` (recommended). Select
  `Error` for efficient HDL code
  generation. If you select `None` or
  `Warning`, HDL Coder generates additional logic to handle out-of-range
  inputs.

**Table Data Typing and Sizing**

- It is good practice to size each dimension in the table to be a
  power of two. If the length of a dimension
  (*except* the innermost dimension) is not a
  power of two, HDL Coder issues a warning. By following this practice, you can
  avoid multiplications during table indexing operations and realize a
  more efficient table in hardware.
- All ports on the block require
  scalar values.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

This block supports fixed-point data types for **Table data** only. In
addition to built-in data types, the index input also supports fixed-point data type
with bias equal to 0, slope equal to 1.0, fractional length equal to 0, and word
length less than or equal to 65,535.

## Version History

**Introduced before R2006a**
