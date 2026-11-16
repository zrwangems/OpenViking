---
type: simulink-block
title: 'From File'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'fromfile'
documentation_source_path: 'slref/fromfile.html'
language: en
---

# From File

## Ports

### Output

### **Port\_1** — Output created using MAT file data scalar | vector | matrix | array

Output created using data loaded from the specified MAT file. Depending on the data you
load, the output might be a scalar or multidimensional signal or a
nonvirtual bus. The From File block supports loading real
and complex data of all built-in data types except
`half`, `int64`, and
`uint64`.

The From File block does not support loading data for
an array of buses.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`
**Complex Number Support:** Yes

## Parameters

### **File name** — MAT file name or path to MAT file `untitled.mat` (default) | MAT file name | path to MAT file

MAT file name or path to MAT file with data you want to load. Specify the
path to the file when the file is not on the MATLAB path or in the current working directory.

You can type the path or file name into the text box, or you can browse to the MAT file
by clicking the **Browse for a MAT-file** button
. On UNIX® systems, the path can start with a tilde (~), which indicates
your home folder.

You cannot load data from a file to which the model logs data in the same
simulation.

#### Tips

- The From File block supports loading data from
  a file created using a To File block without any
  modification to the data or file.
- To determine the current working directory, enter
  `pwd` into the MATLAB Command Window.
- For information about data requirements for C/C++ code
  generation with the From File block, see Code Generation.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `FileName` |
| **Values:** | `'untitled.mat'` (default) | MAT file name | path to MAT file |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/From
File","FileName","InputData.mat")` configures the From
File block named `From File` in the model
`mdl` to load input data from the file
`InputData.mat`.

### **Output data type** — Data type of data in MAT file `Inherit: auto` (default) | `double` | `single` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class_name>` | `Bus: <bus_object>` | `<data type expression>` | ...

Data type of the data in the MAT file loaded by the From
File block. By default, the From File block
inherits the output signal data type from the data in the file or from a
downstream block that defines the data type for the signal. The software
issues an error if the data type of the data in the MAT file does not match
the inherited data type.

When you load data for a scalar or multidimensional signal, you can choose
to inherit the output data type, or you can specify the output data type to
match the data type of the data in the MAT file.

To load data for a bus, set the **Output data type** to
`Bus: <bus object>` and specify the name
of the `Simulink.Bus` object that
defines the output bus.

To load enumerated data, set the **Output data type** to
`Enum: <class name>` and specify the name of
the enumeration class that defines the enumerated data values.

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `'Inherit (auto)'` (default) | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'Enum: <class name>'` | `'Bus: <object name>'` | `'<data type expression>'` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/From
File","OutputDataTypestr","double")` configures the
From File block named `From File` in the model
`mdl` to load data from a MAT file that
contains `double` signal values and produce a
signal with `double` data type.

### **Sample time** — Output sample period and optional time offset `0` | scalar | `1`-by-`2` vector

The **Sample time** parameter specifies when the block
computes a new output value during simulation. For details, see Specify Sample Time.

Specify the **Sample time** parameter as a scalar when
you do not want the output to have a time offset. To add a time offset to
the output, specify the **Sample time** parameter as a
`1`-by-`2` vector where the first
element is the sampling period and the second element is the offset.

By default, the **Sample time** parameter value is `0`,
which indicates continuous sample time with no time offset. For a discrete
signal, specify the sample time as the discrete sampling interval. For
example, specify the sample time as `0.1` to model a
discrete signal sampled every 100ms. Specify the sample time as
`-1` to inherit the value.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `'0'` (default) | scalar | `1`-by-`2` vector |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/From
File","SampleTime","-1")` configures the From File
block named `From File` in the model
`mdl` to inherit its sample
time.

### **Data extrapolation before first data point** — Method to determine block output before first data point in MAT file `Linear extrapolation` (default) | `Hold first value` | `Ground value`

Extrapolation method used to determine output values for simulation times before the
first sample in the MAT file data.

| Method | Description | Example |
| --- | --- | --- |
| `Linear extrapolation` | How the block determines the output value depends on the type of data in the MAT file.  - For `double` data, the   From File block linearly   extrapolates the output value using the first two   samples. - For `Boolean` data, the   From File block uses the first   value in MAT file data for the output   value. - For all other built-in data types, the   From File block:  1. Upcasts the data to      `double`.   2. Linearly extrapolates the output value using      the first two samples in the MAT file data.   3. Downcasts the extrapolated data value to the      original data type.  If the MAT file data only contains one sample, the From File block provides that value at the output.  Do not use the `Linear extrapolation` option when the From File block loads enumerated or fixed-point data.  The extrapolation setting is applied to all signals in a bus. If any signal in the bus contains enumerated or fixed-point data, do not use the `Linear extrapolation` option. | Plot that shows the output for a From File block configured to linearly extrapolate the output value for simulation times before the first sample in the loaded data. The block loads data that starts 2 seconds into the simulation. |
| `Hold first value` | The From File block uses the first data value in the MAT file as the output value. | Plot that shows the output for a From File block configured to hold the first value in the loaded data for simulation times before the first sample in the loaded data. The block loads data that starts 2 seconds into the simulation. |
| `Ground value` | The From File block output value depends on the type of data in the MAT file.  - Built-in numeric types —   `0` - `Boolean` —   `false` - Fixed-point data types — Representation for   value of `0`, which may not be   exactly `0` due to scaling and   limited precision. - Enumerated data types — Default value | Plot that shows the output for a From File block configured to use the ground value as the output value for simulation times before the first sample in the loaded data. The block loads data that starts 2 seconds into the simulation. |

#### Tips

To generate code that builds ERT or GRT targets or uses SIL or PIL
simulation modes, specify **Data extrapolation before first data
point** as `Linear extrapolation`.
For more information about C/C++ code generation with the  From
File block, see Code Generation.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ExtrapolationBeforeFirstDataPoint` |
| **Values:** | `'Linear extrapolation'` (default) | `'Hold first value'` | `'Ground value'` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/From
File","ExtrapolationBeforeFirstDataPoint","Hold first
value")` configures the From File block named
`From File` in the model `mdl`
to extrapolate values before the first value in the file by holding
the first value in the file.

### **Data interpolation within time range** — Interpolation method `Linear interpolation` (default) | `Zero order hold`

Interpolation method used to determine output values for simulation times
between samples in the MAT file data.

| Method | Description | Example |
| --- | --- | --- |
| `Linear interpolation` | How the block determines the output value depends on the type of data in the MAT file.  - For `double` data, the   From File block linearly   interpolates the output value using data values   before and after the simulation time that needs an   output value. - For all other built-in numeric data types, the   From File block:  1. Upcasts the data to      `double`.   2. Linearly interpolates the output value using      the MAT file data values before and after the      simulation time that needs an output value.   3. Downcasts the extrapolated data value to the      original data type. - For `Boolean` data, if the   simulation time is between two workspace data   points with different values, the From   File block positions the value transition   halfway between the MAT file data points. For   example, if the data transitions from   `true` to   `false`, the From   File block provides an output value of   `true` for simulation times in   the first half of the interval between the MAT   file data points and an output value of   `false` for simulation times in   the latter half of the interval.  If the MAT file data only contains one sample, the From File block provides that value at the output.  Do not use the `Linear interpolation` option when the From File block loads enumerated or fixed-point data.  The interpolation setting is applied to all signals in a bus. If any signal in the bus contains enumerated data, do not use the `Linear interpolation` option. | Plot that shows the output for a From File block configured to linearly interpolate the output value for simulation times between the samples in the loaded data. |
| `Zero order hold` | The From File block holds each data value from one sample to the next. The output value for a simulation time between two samples in the MAT file data is the value of the sample that precedes the simulation time. | Plot that shows the output for a From File block configured to use zero-order-hold interpolation for simulation times between the samples in the loaded data. |

#### Tips

To generate code that builds ERT or GRT targets or uses SIL or PIL
simulation modes, specify **Data interpolation within time
range** as `Linear interpolation`.
For more information on C/C++ code generation with the From
File block, see Code Generation.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InterpolationWithinTimeRange` |
| **Values:** | `'Linear interpolation'` (default) | `'Zero order hold'` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/From
File","InterpolationWithinTimeRange","Zero order
hold")` configures the From File block named
`From File` in the model `mdl`
to use zero order hold interpolation.

### **Data extrapolation after last data point** — Method to determine block output after final data point in MAT file `Linear extrapolation` (default) | `Hold last value` | `Ground value`

Extrapolation method used to determine output values for simulation times
after the last sample in the MAT file data.

| Method | Description | Example |
| --- | --- | --- |
| `Linear extrapolation` | How the block determines the output value depends on the type of data in the MAT file.  - For `double` data, the   From File block linearly   extrapolates the output value using the last two   samples in the MAT file. - For `Boolean` data, the   From File block uses the sample   value in MAT file for the output value. - For all other built-in data types, the   From File block:  1. Upcasts the data to      `double`.   2. Linearly extrapolates the output value using      the last two samples in the MAT file data.   3. Downcasts the extrapolated data value to the      original data type.  If the MAT file data only contains one sample, the From File block uses that value as the output.  Do not use the `Linear extrapolation` option when the From File block loads enumerated or fixed-point data.  The extrapolation setting is applied to all signals in a bus. If any signal in the bus contains enumerated data, do not use the `Linear extrapolation` option. | Plot that shows the output for a From File block configured to linearly interpolate the output value for simulation times after the last sample in the loaded data. The block loads data that ends 2 seconds before the end of the simulation. |
| `Hold last value` | The From File block uses the last data value in the MAT file as the output value. | Plot that shows the output for a From File block configured to hold the last output value for simulation times after the last sample in the loaded data. The block loads data that ends 2 seconds before the end of the simulation. |
| `Ground value` | The From File block output value depends on the type of data in the MAT file.  - Built-in numeric types —   `0` - `Boolean` —   `false` - Fixed-point data types — Representation for   value of `0`, which may not be   exactly `0` due to scaling and   limited precision. - Enumerated data types — Default value | Plot that shows the output for a From File block configured to use the ground value as the output value for simulation times after the last sample in the loaded data. The block loads data that ends 2 seconds before the end of the simulation. |

#### Tips

To generate code that builds ERT or GRT targets or uses SIL or PIL
simulation modes, specify **Data extrapolation after last data
point** as `Linear extrapolation`.
For more information on C/C++ code generation with the From
File block, see Code Generation.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ExtrapolationAfterLastDataPoint` |
| **Values:** | `'Linear extrapolation'` (default) | `'Hold last value'` | `'Ground value'` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/From
File","ExtrapolationAfterLastDataPoint","Hold last
value")` configures the From File block named
`From File` in the model `mdl`
to extrapolate values after the last value in the file by holding
the last value in the file.

### **Enable zero-crossing detection** — Option to enable zero-crossing detection for this block `off` (default) | `on`

Zero-crossing detection locates discontinuities, or *zero
crossings*, in the block output and prevents variable-step
solvers from taking excessively small time steps near the discontinuities,
which can slow down a simulation. The From File block can
detect zero crossings when the **Sample time** parameter is
set to `0` for continuous sample time.

The loaded data creates a discontinuity in the block output when the data
includes multiple samples with the same time. For example, for this input
data, a discontinuity occurs at time
`2`.

```
time:     0 1 2 2 3
signal:   2 3 4 5 6
```

The From File block can also create discontinuities in the
output based on how you configure interpolation and extrapolation.

- Setting **Data extrapolation before first data
  point** to `Ground value`
  can create a discontinuity at the first sample in the loaded
  data.
- Setting **Data extrapolation after the last data
  point** to `Ground value`
  can create a discontinuity at the last sample in the loaded
  data.
- Setting **Data interpolation within time
  range** to `Zero-order
  hold` creates a discontinuity at each sample in
  the loaded data, including the last.

This block supports zero-crossing detection only in simulations
that use a variable-step solver. When you use a fixed-step solver for simulation, the software
does not detect or locate zero crossings for this block.

For more information, see Zero-Crossing Detection.

#### Tips

To generate code that builds ERT or GRT targets or uses SIL or PIL
simulation modes, clear this check box. For more information on C/C++
code generation with the From File block, see Code Generation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroCross` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'on'` |

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

**Example:** `set_param("mdl/From
File","ZeroCross","off")` configures the From File
block named `From File` in the model
`mdl` to disable zero-crossing
detection.

## Libraries

Simulink / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed pointa` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |
|  |  |
| --- | --- |
| a Supports up to 32-bit fixed-point data types. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code.

Generating code for an RSim target has no special requirements or limitations. All other
code generation targets support loading only real, double, one-dimensional signal
data from an array in a MAT file where the first column contains time data and
subsequent columns contain the signal data. Generating code that builds ERT or GRT
targets or uses SIL or PIL simulation modes requires that:

- The loaded MAT file contains an array with at least two rows and no
  `NaN`, `Inf`, or
  `-Inf` values.
- The **Data extrapolation before first data point** and
  **Data extrapolation after last data point** parameters
  are set to `Linear extrapolation`.
- The **Data interpolation within time range** parameter is
  set to `Linear interpolation`.
- The **Enable zero-crossing detection** parameter is
  cleared.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

The From File block supports fixed-point data types up to 32 bits.

## Version History

**Introduced before R2006a**

## Description

Load data from MAT file into Simulink model

The From File block reads data into a Simulink® model from a MAT file and provides the data as a signal or nonvirtual bus
at the block output. You can load data from a MAT file that is on or off the MATLAB® path. A model can contain multiple From File blocks that
load data from the same MAT file.

You can specify how the block constructs the output from the data in the file, including the
sample time for the output, interpolation and extrapolation behavior, and whether to use
zero-crossing detection.

The From File block icon shows the name of the MAT file that supplies the
data to the block. For example, if you use the From File block to load
data from the file `myData.mat`, the block displays
`myData.mat`.

### MAT File Data

The From File block can load data from a MAT file that is stored in
a `timeseries` object or in an array where the first row contains
time data and subsequent rows contain data for a scalar or vector signal. Loading
data stored in a `timeseries` object supports a wider range of data
and output types and requires that the MAT file is Version 7.3.

| Data Consideration | `timeseries` Format | Array Format |
| --- | --- | --- |
| Time data requirements | - Data type must be `double` - Values must increase monotonically | - Data type must be `double` - Values must increase monotonically |
| Supported signal data types | - Any built-in data types except   `half`, `int64`, and   `uint64` - Enumerated data type - Fixed-point data type with up to a 32-bit word   length | `double` |
| Signal data complexity | Real or complex | Real |
| Signal data requirements | Must not contain `NaN`, `Inf`, or `-Inf` values | Must not contain `NaN`, `Inf`, or `-Inf` values |
| Type of output | - Scalar, vector, or multidimensional signal - Bus | Scalar or vector signal |
| MAT file version | Version 7.3 | All versions |

The From File block loads data from only one variable in the MAT file,
regardless of the number of variables the MAT file contains. When you load data from
a Version 7.3 MAT file that contains multiple variables, the From
File block loads the data in the variable that is first alphabetically.
The ordering algorithm used by Version 7.0 and earlier MAT files is more
complicated, so ensure that the MAT file only contains data for a single variable
when you load data from a Version 7.0 or earlier MAT file.

**Note**

Logging outputs, states, or a signal connected to a To
Workspace block using the `Array` format
generates an array in a different format than the From File block
expects. In the `Array` format for logging, the first
column contains time values, and in the array format for the From
File block, the first row contains time values. The From
File block and To File block use the same array
format.

### MAT File Version

The version of the MAT file also affects how the From File block
loads the data. When you load data from a Version 7.3 MAT file, data is loaded
incrementally during simulation. When you load data from a Version 7.0 or earlier
MAT file, all the data is loaded into memory at the start of simulation.

To convert a MAT file to Version 7.3, use the `load` function to load the data in
the Version 7.0 or earlier MAT file into the base workspace. Then, save the data to
a Version 7.3 MAT file using the `save` function with the version
specified as `'-v7.3'`. For example, these commands convert the
file `myData.mat` that contains the variable
`inputData` to Version
7.3.

```
load("myData.mat");
save("myData.mat","inputData","-v7.3");
```

For more information, see MAT-File Versions.
