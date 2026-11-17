---
type: simulink-block
title: 'To Workspace'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'toworkspace'
documentation_source_path: 'slref/toworkspace.html'
language: en
---

# To Workspace

## Ports

### Input

### **Port\_1** — Data to log to workspace scalar | vector | matrix | array | bus

Input port that receives data to log to workspace. The To
Workspace block supports logging real and complex data of
any built-in data type or user-defined data types such as buses,
enumerations, and fixed-point data.

#### Tips

Logging fixed-point data requires a license for Fixed-Point Designer™.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus` | `image` | `datetime`
**Complex Number Support:** Yes

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Variable name** — Name of variable for saved data `simout` (default) | string | character vector

Specify a name for the variable that contains the logged data. By default,
the To Workspace block saves logged data in a variable called
`simout`. When a model contains multiple To
Workspace blocks, the **Variable name**
parameter value for each block must be unique.

For information about naming MATLAB® variables, see Variable Names.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `VariableName` |
| **Values:** | `"simout"` (default) | valid MATLAB variable name |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param(gcb,"VariableName","myName")`

### **Limit data points to last** — Number of samples to log `inf` (default) | scalar | vector

When you want to save or analyze only the data from the end of a
simulation, specify the number of samples you want to log as a positive
whole number greater than zero. By default, the To Workspace
block logs data for the entire simulation, and the value for the
**Limit data points to last** parameter is
`inf`.

Limiting logged data to the last *n* signal values
directly impacts memory allocation. When you specify this parameter, the
software allocates memory upfront based on the specified value, not on the
time steps generated during the simulation. For this reason, the
**Limit data points to last** parameter is not
recommended when logging an indeterminate number of time steps.

For more information about controlling which samples are logged during
simulation, see Specify Signal Values to Log.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `MaxDataPoints` |
| **Values:** | `"inf"` (default) | positive integer |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param(gcb,"MaxDataPoints","20")`

### **Decimation** — Decimation factor `1` (default) | positive integer

Specify a decimation factor to reduce the effective sample rate for the
logged data. For a decimation factor, *n*, the To
Workspace block logs every
*n*th sample value. For
example, when you specify the **Decimation** value as
`2`, the To Workspace block logs every
other data point.

For more information about controlling which samples are logged during
simulation, see Specify Signal Values to Log.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Decimation` |
| **Values:** | `"1"` (default) | positive integer |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param(gcb,"Decimation","2")`

### **Save format** — Format for data logged to workspace `Timeseries` (default) | `Structure With Time` | `Structure` | `Array`

Specify the format for the data logged to the workspace. To log data for a
bus or array of buses input, use `Timeseries`
format.

| **Save Format** Value | Workspace Data Format | Simulation Workflow Support |
| --- | --- | --- |
| `Timeseries` | Nonbus input logged as a `timeseries` object.  Bus input logged as a structure of `timeseries` objects. The hierarchy and names for fields in the structure matches the hierarchy and names specified in the `Simulink.Bus` object that defines the bus.  Array of buses input logged as an array of structures of `timeseries` objects. | Supported:  - Normal mode simulation - Accelerator mode simulation - Rapid   accelerator mode simulation *(since R2022a)* - External mode simulation that uses XCP   communication provided   `StreamToWks` is set to   `'on'` and   `MATFileLogging` is set to   `'off'`    Not supported:  - External mode simulation that uses TCP/IP or   serial communication - Software-in-the-loop (SIL) simulation - Processor-in-the-loop (PIL)   simulation - Code generation for Simulink   Coder™ targets |
| `Structure With Time` | Nonbus input logged as a structure that contains these fields:  - `time` — Column vector of   simulation time hits for which input value was   logged. - `signals` — Structure with   sample values that contains the fields:  - `values` — Array of sample     values.   - `dimensions` — Sample     dimensions.   - `label` — Name of signal     line in model. - `blockName` — Name of the   To Workspace block. | Always supported:  - Normal mode simulation. - External mode simulation that uses XCP   communication provided   `StreamToWks` is set to   `'on'` and   `MATFileLogging` is set to   `'off'`    Supported except when the To Workspace block is in a referenced model:  - Accelerator mode simulation - Rapid accelerator mode simulation - External mode simulation that uses TCP/IP or   serial communication    Supported if **MAT-file logging (Simulink Coder)** is enabled for generated code, except when the To Workspace block is in a referenced model:  - Software-in-the-loop (SIL) simulation - Processor-in-the-loop (PIL)   simulation - Code generation for Simulink   Coder targets |
| `Structure` | Nonbus input logged as a structure that matches the `Structure With Time` format, but the `time` field of the structure is empty. |
| `Array` | Sample values for nonbus input saved as *N*-dimensional array, where *N* is one greater than the dimensions of the input. For example:  - Scalar signal data is logged as a column   vector. - Vector signal data is logged as a   matrix. - Matrix signal data is logged as a 3-D   array.    The structure of the values in the array depends on the dimensions of the input signal data:  - For scalar and vector signals, each sample   value is a row in the output array. The first   dimension of the array aligns with time such that   `simout(1,:)` returns the first   logged signal value. - For matrix signals, the third dimension of   the output array aligns with time such that   `simout(:,:,1)` returns the first   logged signal value. - For *N*-dimensional   signals, the last dimension aligns with time, such   that the number of elements in the last dimension   is equal to the number of samples logged from   simulation.    The output array contains only signal values and does not contain time data. |

#### Tips

- To log data as frame-based instead of sample-based:

  - Configure the **Save format**
    parameter to log data using the
    `Structure` format or the
    `Array` format.
  - Specify the **Save 2-D signals
    as** parameter as `2-D array
    (concatenate along first
    dimension)`
- When you want to load the logged data using a From
  Workspace block, consider using the
  `Timeseries` or
  `Structure With Time` formats. When
  you log data using the `Array` format,
  you need to incorporate the sample time values into the array
  before loading the data.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SaveFormat` |
| **Values:** | `"Timeseries"` (default) | `"Structure with Time"` | `"Structure"` | `"Array"` |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param(gcb,"SaveFormat","Structure")`

### **Save 2-D signals as** — Arrangement of 2-D sample values in logged data `3-D array (concatenate along third dimension)` (default) | `2-D array (concatenate along first dimension)`

Specify whether to log 2-D input data as a 3-D array or a 2-D
array.

Logging as a 3-D array is well suited for sample-based input data. Samples
are concatenated along the third dimension, allowing easy access of
2-dimensional sample data.

Logging as a 2-D array is well suited for frame-based input data. Samples
are concatenated along the first dimension, which in effect removes the
frame buffering from the first dimension.

| Input Data Dimensions | Save 2-D Signal As... | Workspace Data Dimensions |
| --- | --- | --- |
| *M*-by-*N* | `2-D array (concatenate along first dimension)` | *K*-by-*N* matrix, where *K* is equal to *M* times the number of samples logged from simulation.  For example, logging ten samples of a `2`-by-`4` matrix input creates a `20`-by-`4` matrix. |
| `3-D array (concatenate along first dimension)` | *M*-by-*N*-by-*K* array, where *K* is equal to the number of samples logged from simulation.  For example, logging ten samples of a `2`-by-`4` matrix input creates a `2`-by-`4`-by-`10` array. |

#### Dependencies

To enable this parameter, set the **Save format** to
`Array` or
`Structure`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Save2DSignal` |
| **Values:** | `"3-D array (concatenate along third dimension)"` (default) | `"2-D array (concatenate along first dimension)"` |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param(gcb,"Save2DSignal","2-D array
(concatenate along first dimension)")`

### **Log fixed-point data as a fi object** — Data type for logged fixed-point data `on` (default) | `off`

Specify how to log fixed-point input data.

The To Workspace block always logs fixed-point input data
as a `fi` (Fixed-Point Designer) object when the
**Save format** parameter is specified as
`Timeseries`. To log fixed-point data as a
`fi` object when the **Save format**
parameter is not specified as `Timeseries`, select
the **Log fixed-point data as a fi object** parameter and
run the simulation in normal or accelerator mode.

When you clear the **Log fixed-point data as a fi
object** parameter or run the simulation in rapid accelerator
mode, fixed-point input data is logged as `double`.

To log input data of type `int64` as
`int64` or type `uint64` as
`uint64`, select the **Log fixed-point data as
a fi object** parameter. When you clear the **Log
fixed-point data as a fi object** parameter, input data of type
`int64` or `uint64` is logged as
`double`.

Using the To Workspace block to log fixed-point data
requires a license for Fixed-Point Designer.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `FixptAsFi` |
| **Values:** | `"on"` (default) | `"off"` |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param(gcb,"FixptAtFi","off")`

### **Sample time** — Sampling interval and optional time offset -1 (default) | scalar

Specify when the block logs the input value during simulation. By default,
the sample time is inherited (`-1`). For continuous sample
time, specify the value as `0`. To use a discrete sample
time, specify the **Sample time** parameter as a scalar.
For more information, see Specify Sample Time.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param(gcb,"SampleTime","0")`

## Libraries

Simulink / Sinks DSP System Toolbox / Sinks HDL Coder / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code.

To generate code that logs the input to the To Workspace block to a
MAT file, enable the **MAT-file logging** parameter. For more
information, see **MAT-file logging (Simulink Coder)**.

Code generation is not supported for:

- String data types.
- Blocks inside referenced models.
- Blocks that log data using the `Timeseries`
  format. For more information, see **Save
  format**.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `No HDL` | Do not generate HDL code for this block. |

**HDL Block Properties**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | Control the removal of unconnected logic. The default is `off`, which means unconnected logic is not preserved in HDL code. For more details, see PreserveUpstreamLogic (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2025a: Log `datetime` data

The To Workspace block supports logging `datetime` data.

### R2023b: Log unbounded variable-size signals

In normal and accelerator mode simulations, you can log an unbounded variable-size
signal using the To Workspace block. Logging is not supported for
nonvirtual buses that contain unbounded variable-size signals.

### R2023a: Log nonvirtual buses that contain variable-size signals

In normal and accelerator mode simulation, the To Workspace block
supports logging:

- Nonvirtual buses that contain variable-size signals directly or in nested
  buses
- Buses with nested nonvirtual buses that contain variable-size
  signals

In normal mode simulations only, the To Workspace block supports
logging:

- Arrays of buses with nonvirtual buses that contain variable-size
  signals

### R2022a: Log data to the Simulation Data Inspector as well as the workspace

Data is automatically logged to the Simulation Data Inspector as well as the
workspace. The Simulation Data Inspector automatically retains results from each
simulation. Because data logged using the To Workspace block streams
to the Simulation Data Inspector, this data is also retained.

In previous releases, data logged using the To Workspace block
only logged to the workspace and was overwritten for each simulation unless you
changed the logging variable names or manually saved the results.

In most cases, you do not need to make any changes to your code. Logging large
amounts of data or running many simulations can produce large amounts of data that
fill up disk space. To learn how to control the amount of data retained in the
Simulation Data Inspector, see Limit the Size of Logged Data.

### R2022a: Log `int64` and `uint64` data using built-in data types

Log `int64` and `uint64` data using the built-in
data types.

In previous releases, the To Workspace block logged
`int64` and `uint64` data as a
`fi` object when a license for Fixed-Point Designer was available and as `double` when the license was
not available.

### R2022a: Log signals with `string` and `half` data types

The To Workspace block supports logging signals with
`string` and `half` data types.

### R2022a: Log arrays of buses

The To Workspace block supports logging an array of buses.

### R2022a: Log data using the `Timeseries` format in rapid accelerator simulations

Previously, only normal mode simulation or accelerator mode simulation could be
used to log data in `Timeseries` format.

### R2022a: Log data using the `Timeseries` format for To Workspace blocks inside for-each subsystems

You can use the `Timeseries` format to log data in a To
Workspace block inside for-each subsystems.

## Description

Log data to workspace from Simulink model

The To Workspace block logs the data connected to its input port to a
workspace from a Simulink® model. Typically, logged data is returned in the base workspace. When you
simulate a model programmatically inside a function, logged data is returned in the
workspace for the function. During simulation, logged data streams to the Simulation
Data Inspector. Logged data is written to the workspace when the simulation pauses or
stops.

You can use the To Workspace block to log data for a signal, a bus, or
an array of buses. The To Workspace block supports logging scalar and
multidimensional data, including data for variable-size signals.

You can configure the name of the variable that stores the data the To
Workspace block logs, and you can specify the format for the logged data.
You can also control which values the To Workspace block logs by
specifying block or model parameters. For more information, see Specify Signal Values to Log.

### Access Logged Data

How simulation results are returned to the workspace depends on how you simulate
and configure the model. Simulation results are returned in a single `Simulink.SimulationOutput` object in
any of these situations:

- You enable the **Single simulation
  output** parameter.

  By default, the **Single simulation output**
  parameter is enabled when you create a new model. You can enable the
  parameter using the Configuration Parameters dialog box. On the
  **Modeling** tab, under
  **Settings**, click **Model
  Settings**. Then, in the Configuration Parameters dialog
  box, select **Data Import/Export** and select
  **Single simulation output**.
- You run a set of simulations using the Multiple Simulations pane.
- You simulate the model programmatically using one or more `Simulink.SimulationInput`
  objects.

  You can configure simulations using `SimulationInput`
  objects when you run simulations using the `sim`, `parsim`, and `batchsim` functions.
- You simulate the model using a `sim` function
  syntax that returns results as a single simulation output.

  For more information, see `sim`.

When simulation results are returned in a single output, the
`SimulationOutput` object contains a variable for each To
Workspace block in the model. To access the data logged by a To
Workspace block:

- Use a dot with the variable name specified using the
  **Variable name** parameter of the block. By
  default, models are configured to return a single simulation output
  using the variable name `out`, and the To
  Workspace block saves data to a variable named
  `simout`.

  ```
  toWksData = out.simout;
  ```
- Use the `get` function with the
  name of the variable that contains the logged data.

  ```
  toWksData = get(out,simout);
  ```

In the model, the To Workspace block indicates how to access the
data in the workspace. By default, the block shows `out.simout`.
The block appearance updates when you:

- Specify a different value for the **Variable name**
  parameter on the block.
- Specify a different variable name for the single simulation
  output.
- Clear the **Single simulation output** configuration
  parameter.
