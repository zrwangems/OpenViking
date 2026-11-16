---
type: simulink-block
title: 'From Workspace'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Import and Export'
documentation_page: 'fromworkspace'
documentation_source_path: '../simulink/slref/fromworkspace.html'
language: en
---

# From Workspace

## Ports

### Output

### **Port\_1** — Data loaded from workspace scalar | vector | matrix | array

Data loaded from workspace, provided at the block output as a signal or a nonvirtual
bus. Depending on the data you load, the output signal may be:

- A scalar, vector, multidimensional, or a bounded variable-size
  signal
- A bus
- An array of buses *(since R2021a)*

The From Workspace block supports loading real and
complex data of all built-in numeric data types and custom fixed-point
data types. You can also load string data and data with custom
enumerated or bus data types.

*Before R2024b: The From
Workspace block does not support loading input signal values
with `int64` or `uint64` data
types.*

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
**Complex Number Support:** Yes

## Parameters

### **Data** — Data to load from workspace `timeseries` object | `timetable` object | structure | 2-D array | MATLAB expression

Data to load from workspace, specified as a MATLAB variable or MATLAB expression that evaluates to data in a format supported by the
From Workspace block. The expression could create the
data the From Workspace block provides at its output, or the
expression could reference a workspace variable that contains the data to
load. For more information about how the expression is evaluated, see Symbol Resolution.

The From Workspace block can load real or complex data for scalar,
multidimensional, and variable-size signals as well as data for a bus or
array of buses.

The From Workspace block supports different input data formats depending
on the type of output you want the block to produce in your model. For all
types of outputs and data formats:

- Time values in the input data must have
  `double` data type and increase
  monotonically.
- Time and data values must not contain `Inf`
  or `NaN` values.

| Type of Output | Data Formats | Tips |
| --- | --- | --- |
| Scalar or vector signal | - `timetable` that contains a single   column - `timeseries` object - `Simulink.SimulationData.Signal`   object - Structure with fields and hierarchy that   match the `Structure` or   `Structure with time`   logging format. - Two-dimensional array in which the first   column is time and one or more additional columns   contain the signal value for each timestamp | - For scalar and vector signals, the number of   rows in the signal data must match the number of   rows in the time vector. - To create a `timetable`, the   time values must be a `duration` vector.  Simulation time always uses units of   seconds. When you create a duration vector that   uses units other than seconds, the software   converts the value to seconds for use in the   simulation. - Array format does not support signal values   that are complex or that have a data type other   than `double`. |
| Multidimensional signal | - `timeseries` object - `timetable` that contains a single   column - `Simulink.SimulationData.Signal`   object - Structure with fields and hierarchy that   match the `Structure` or   `Structure with time`   logging format | - For a multidimensional signal with values   that have two or more dimensions, the length of   the last dimension must match the length of the   time vector.  For example, input data for 10 samples of a   `2`-by-`2`   matrix signal has a time vector that contains 10   rows and an array of signal values that has   dimensions   `2`-by-`2`-by-`10`. - To create a `timetable`, the   time values must be a `duration`   vector.  Simulation time always uses units of   seconds. When you create a duration vector that   uses units other than seconds, the software   converts the value to seconds for use in the   simulation. |
| Variable-size signal | Structure with fields and hierarchy that match the `Structure` or `Structure with time` logging format | To log a variable-size signal in a format you can load using the From Workspace block, connect the signal to a top-level Outport block and set the **Save format** configuration parameter for the model to `Structure` or `Structure with time`. |
| Bus | Structure of `timetable` or `timeseries` objects:    - Specify the **Output data   type** parameter as the `Simulink.Bus` object that defines the   bus. - The hierarchy and field names of the   structure must match the hierarchy and element   names of the bus. - Each `timetable` or   `timeseries` object contains data   for a leaf signal in the bus. - Each `timetable` must contain   only one column. | To partially specify input data for a bus, set bus elements for which you do not need to load data to `[]` in the input data structure. |
| Array of buses *(since R2021a)* | Array of structures that each represent data for a bus within the array of buses | - Loading data for an array of buses is not   supported for rapid accelerator   simulations. - From Workspace blocks in the   top model support loading data for an array of   buses in normal and accelerator mode   simulations. - From Workspace blocks in   referenced models support loading data for an   array of buses only when the referenced model   executes in normal mode. - To partially specify input data for an array   of buses, set bus elements for which you do not   need to load data to `[]` in the   structure that represents the data for that   bus. |

For details, see Load Data Using the From Workspace Block.

#### Tips

- To load data that was logged in array format using the
  To File block, transpose the array so that
  the time values are in a single column rather than a single row.
  You can use the `transpose`
  function and save the transposed data to a new file.
- For programmatic simulations you run using the `sim`, `parsim`, or
  `batchsim` functions, you can use a `Simulink.SimulationInput` object to specify the
  data for the From Workspace block to load.

  - Set the value of the
    `VariableName` parameter to use
    in the simulation on the block using the `setBlockParameter` function.
  - Add the variable that contains the input data to
    the `SimulationInput` object using
    the `setVariable` function.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `VariableName` |
| **Values:** | `'simin'` (default) | MATLAB expression | `timeseries` object | `timetable` | structure | 2-D array |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("myModel/From
Workspace","VariableName","inData")` configures the
From Workspace block named `From
Workspace` in the model `myModel` to
load data stored in the MATLAB variable named
`inData`.

### **Output data type** — Loaded workspace data type `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | ...

Data type of the workspace data the From Workspace block
loads. By default, the From Workspace block inherits the
output signal data type from the workspace data or from a downstream block
that defines the data type for the signal.

#### Tips

- When you load data for a scalar, vector, or multidimensional
  signal, you can choose to inherit the output data type or you
  can specify the output data type to match the data type of the
  workspace data.
- To load data for a bus or an array of buses, set the
  **Output data type** to `Bus:
  <bus_object>` and specify the name of the
  `Simulink.Bus`
  object that defines the output bus.

  When you load enumerated data, set the **Output data
  type** to `Enum: <class_name>`
  and specify the name of the enumeration class that defines the
  enumerated data values.
- The **Data Type Assistant** helps you set data
  attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `'Inherit: auto'` (default) | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'string'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'Enum: <class name>'` | `'Bus: <object name>'` | data type expression |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("myModel/From
Workspace","OutDataTypeStr","int32")` specifies that
data type must be `int32` for the data the
From Workspace block named `From
Workspace` loads into the model
`myModel`.

### **Sample time** — Output sample period and optional time offset `0` (default) | scalar | vector

The **Sample time** parameter specifies when the block
computes a new output value during simulation. For details, see Specify Sample Time.

Specify the **Sample time** parameter as a scalar when
you do not want the output to have a time offset. To add a time offset to
the output, specify the **Sample time** parameter as a
`1`-by-`2` vector where the first
element is the sampling period and the second element is the offset.

By default, the **Sample time** parameter value is
`0`, which indicates continuous sample time with no
time offset. For a discrete signal, specify the **Sample
time** as the discrete sampling interval. For example, specify
the **Sample time** as `0.1` to model a
discrete signal sampled every 100ms. Specify the **Sample
time** as `-1` to inherit the value.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `'0'` (default) | scalar | vector |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("myModel/From
Workspace","SampleTime","0.1")` configures the
From Workspace block named `From
Workspace` in the model `myModel` to
execute with a sample time of `0.1`
seconds.

### **Interpolate data** — Interpolation method `on` (default) | `off`

Interpolation method used to provide output values for simulation times
that are in between time values in the loaded workspace data. When you
select **Interpolate data**, the From
Workspace block linearly interpolates an output value using
adjacent values in the loaded workspace data. When **Interpolate
data** is not selected, the From Workspace block
provides the value of the previous data point in the loaded workspace data.
For more information about the interpolation algorithm, see Interpolation.

The **Interpolate data** and **Form output after final data
value by** parameters control how the From
Workspace block extrapolates output values for simulation times
that occur prior to the first data point or after the last data point in the
loaded workspace data. For complete information regarding the From
Workspace block extrapolation behavior, see Extrapolation.

Clear the **Interpolate data** parameter and set the
**Form output after final data value by** parameter to
a value other than `Extrapolation` when:

- You load string, enumerated, fixed-point, or variable-size signal
  data.
- You load `int64` or `uint64`
  data for a rapid accelerator simulation.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Interpolate` |
| **Values:** | `'on'` (default) | `'off'` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("myModel/From
Workspace","Interpolate","off")` configures the
From Workspace block named `From
Workspace` to use zero-order hold interpolation for
loading data into the model
`myModel`.

### **Enable zero-crossing detection** — Zero-crossing detection `on` (default) | `off`

Zero-crossing detection is a technique used to locate discontinuities in the block output
and avoid using excessively small time steps near the discontinuities, which
can slow down a simulation. A *zero crossing* refers to
a discontinuity in the data. The From Workspace block can
detect zero crossings when the sample time is continuous
(`0`).

The loaded workspace data creates a discontinuity in the block output when the data
includes multiple samples with the same time. For example, for this input
data, a discontinuity occurs at time
`2`.

```
time:     0 1 2 2 3
signal:   2 3 4 5 6
```

The From Workspace block detects zero crossings caused by
duplicate time values in the input data only when you select the
**Interpolation** parameter.

The From Workspace block can also create a discontinuity in
the output at the last sample in the workspace data when you set
**Form output after final data value by** to
`Setting to zero`.

When you load input data for a bus, the From Workspace block detects zero
crossings for all bus elements.

This block supports zero-crossing detection only in simulations
that use a variable-step solver. When you use a fixed-step solver for simulation, the software
does not detect or locate zero crossings for this block.

For more information, see Zero-Crossing Detection.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ZeroCross` |
| **Values:** | `'on'` (default) | `'off'` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("myModel/From
Workspace","ZeroCross","off")` disables the
**Enable zero-crossing detection** parameter
for the From Workspace block named `From
Workspace` in the model
`myModel`.

### **Form output after final data value by** — Method to determine block output after final data point `Extrapolation` (default) | `Setting to zero` | `Holding final value` | `Cyclic repetition`

The From Workspace block uses the **Interpolate
data** and **Form output after final data value
by** settings to determine the block output for simulation
times after the last sample available in the workspace data.

| Setting for Form output after final data value by | Setting for Interpolate data | Block Output After Final Data |
| --- | --- | --- |
| **Extrapolation** | On | Extrapolated from final data value |
| Off | Error |
| **Setting to zero** | On | Zero |
| Off |
| **Holding final value** | On | Final value from workspace |
| Off |
| **Cyclic repetition** | On | Error |
| Off | When the loaded workspace data uses the structure without time format, repeats workspace data from the first value.  Errors for workspace data formats other than structure with time. |

For complete information regarding the From Workspace block
extrapolation behavior, see Extrapolation.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutputAfterFinalValue` |
| **Values:** | `'Extrapolation'` (default) | `'Setting to zero'` | `'Holding final value'` | `'Cyclic repetition'` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("myModel/From Workspace","OutputAfterFinalValue","Holding
final value")` configures the From
Workspace block named `From Workspace`
in the model `myModel` to use the final input data
value as the output value for time steps that occur after the last
time value in the input data.

## Libraries

Simulink / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed pointa` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `yes` |
|  |  |
| --- | --- |
| a Supports input via fi objects created using Fixed-Point Designer. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code. The data the From Workspace block loads
is hard coded as a statically allocated array in the generated code. Using the
From Workspace block for code generation can increase the size of
the generated code and memory usage significantly. To implement an input port in
generated code, use the Inport block or In Bus Element block.

For software-in-the-loop (SIL) testing, consider using the SIL/PIL
Manager (Embedded Coder). You can use a From Workspace block to provide
input for SIL testing on code generated for a model reference. For more information,
see Test Generated Code with SIL and PIL Simulations (Embedded Coder).

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Supports input via `fi` (Fixed-Point Designer) objects created using
Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2024b: `int64` and `uint64` data type support

The From Workspace block supports loading input signal data values
that have an `int64` or `uint64` data type. When
you use the From Workspace block to load `int64` or
`uint64` signal data:

- Only the signal values can have the `int64` or
  `uint64` data type. Time values must have
  `double` data type.
- Use a format other than array, such as `timetable`,
  `timeseries`, or structure. Array format does not support
  any data type other than `double`.

While loading `int64` and `uint64` signal data
is supported in all simulation modes, interpolation of `int64` and
`uint64` data is not supported in rapid accelerator
simulations. To load `int64` or `uint64` data into
a rapid accelerator simulation:

1. Clear the **Interpolate data** parameter.
2. Set the **Form output after final data value by**
   parameter to any value except
   `Extrapolation`.

### R2021a: Array of buses support

The From Workspace block supports loading data for an array of
buses. A From Workspace block in the top model can load data for an
array of buses in normal or accelerator mode simulations. Loading data for an array
of buses using a From Workspace block in a referenced model is
supported only when the referenced model executes in normal mode.

### R2020a: `timetable` support

The From Workspace block supports loading data stored as a
`timetable`. The `timetable` must contain only a
single column of data.

When you load input data for a bus, the structure that contains the data can
include one or more `timetable` objects that contain only a single
column of data for a leaf signal.

### R2018b: String support

The From Workspace block supports loading string data. When you use
the From Workspace block to load string data:

- Only the signal values can have the `string` data type.
  Time values must have `double` data type.
- Use a format other than array, such as `timeseries` or
  structure. Array format does not support any data type other than
  `double`.

## Description

Load signal data from workspace into Simulink model

The From Workspace block reads data into a Simulink® model from a workspace and provides the data as a signal or a nonvirtual
bus at the block's output. You can load data from the base workspace, model workspace,
or mask workspace. You can use the From Workspace block to load signal
data into any model or subsystem in a model hierarchy from a workspace accessible to the
referenced model or subsystem.

You can specify how the block constructs the output from the workspace data, including the
output sample period, interpolation and extrapolation behavior, and whether to use
zero-crossing detection.

The From Workspace block icon shows the value of the
**Data** parameter. For example, if you use the From
Workspace block to load data in the variable *x*, you
specify `x` as the value for the **Data** parameter,
and the block displays `x`.

### Specify Data to Load

Specify data for the From Workspace block to load using the
**Data** parameter. You can specify the value of the
**Data** parameter as a MATLAB® expression, such as a variable name. The expression in the
**Data** parameter must evaluate to data in a format that the
From Workspace block supports. For details about how the
expression is evaluated, see Symbol Resolution.

The From Workspace block does not load data from a data dictionary. Use a
data dictionary to store only design data for a model, not simulation input data.
You can store design data related to the From Workspace block, such
as the value for the **Sample time** parameter, in a data
dictionary.
