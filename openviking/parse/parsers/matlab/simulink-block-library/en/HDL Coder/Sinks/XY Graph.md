---
type: simulink-block
title: 'Record, XY Graph'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'record'
documentation_source_path: '../simulink/slref/record.html'
language: en
---

# Record, XY Graph

## Ports
```yaml
ports:
- name: Port_1
  summary: Signal to record scalar | vector | matrix | array | bus
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image | datetime
```

### Input

### **Port\_1** — Signal to record scalar | vector | matrix | array | bus

Signal to record. You can add ports to the Record block by dragging
lines to the edge of the block or by using the **Ports**
parameter.

The Record block supports logging variable-size signals but does
not support visualizing variable-size signals.

The XY Graph block is an alternative configuration of the
Record block that visualizes data connected to two input ports on an
XY plot. The first input port provides the *x* data for the XY plot,
and the second input port provides the *y* data.

#### Tips

- To log frame-based data, specify the **Input processing**
  parameter for each port that receives a frame-based signal.
- When you connect a nonscalar signal to an input port of the XY
  Graph block, you must manually configure which channels or elements of
  the nonscalar signal provide the *x* and *y*
  data for the XY plot.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `datetime`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Number of input ports
  summary: Number of input ports 1 (default) | integer in the range [1,100]
  group: Main
  block_parameter: NumPorts
  values: 1 (default) | integer in the range [1, 100]
- name: Decimation
  summary: Decimation factor 1 (default) | positive integer
  group: Main
  block_parameter: Decimation
  values: '"1" (default) | positive integer in quotes'
- name: Limit data points to last
  summary: Number of samples to log inf (default) | scalar | vector
  group: Main
  block_parameter: MaxDataPoints
  values: '"inf" (default) | positive integer in quotes'
- name: Select port
  summary: Port for which to specify input processing mode 1 (default) | integer
  group: Main
  block_parameter: FrameSettings
  values: false (default) | 1-by-n row vector of logical values, where n is equal to the number of ports
- name: Input processing
  summary: Input processing mode for selected port Elements as channels (sample-based) (default) | Columns as channels (frame-based)
  group: Main
  block_parameter: FrameSettings
  values: false (default) | 1-by-n row vector of logical values, where n is equal to the number of ports
- name: Record to workspace
  summary: Workspace logging option off (default) | on
  group: Record
  block_parameter: RecordToWorkspace
  values: '"off" (default) | "on" | false or 0 | true or 1'
- name: Workspace variable name
  summary: Name for workspace variable that contains logged block data recordout (default) | character vector | string
  group: Record
  block_parameter: VariableName
  values: '"recordout" (default) | valid MATLAB variable name'
- name: Record to file
  summary: Log to file option off (default) | on
  group: Record
  block_parameter: RecordToFile
  values: '"off" (default) | "on" | false or 0 | true or 1'
- name: File name
  summary: Name of file with logged data recording.mldatx (default) | character vector | string
  group: Record
  block_parameter: FileName
  values: '"recording.mldatx" (default) | valid filename'
- name: File type
  summary: Type of file for logged data *.mldatx (default) | *.mat | *.xslx | *.parquet
  group: Record
  block_parameter: FileName
  values: '"recording.mldatx" (default) | valid filename'
- name: File location
  summary: Path to file with logged data working directory (default) | character vector | string
  group: Record
  block_parameter: FileName
  values: '"recording.mldatx" (default) | valid filename'
- name: Time
  summary: Options for exporting time data to Excel or Parquet file Shared Time Columns (default) | Individual Time Columns
  group: Record
  block_parameter: SharedTimeColumn
  values: '"on" (default) | "off"'
- name: Signal Attributes
  summary: Signal attributes to export to Excel file Data Type | Units | Port Index | Block Path | Interpolation
  group: Record
- name: Compression Type
  summary: Compression options Fastest (snappy) (default) | Balanced for Size and Speed (gzip) | Compact (brotli) | None (uncompressed)
  group: Record
  block_parameter: ParquetCompression
  values: '"fastest" (default) | "balanced" | "compact" | "none"'
- name: Generate Sidecar
  summary: Option to generate JSON sidecar on (default) | off
  group: Record
  block_parameter: ParquetMetaData
  values: '"on" (default) | "off"'
- name: Row Group Policy
  summary: Options for grouping rows in Parquet file Row Group Height (default) | Row Group Size (MB)
  group: Record
  block_parameter: ParquetRowGroupPolicy
  values: '"height" (default) | "sizeinmb"'
- name: Row Group Policy Value
  summary: Height or size of row group auto (default when Row Group Policy is Row Group Height) | 512 (default when Row Group
    Policy is Row Group Size (MB) | number of rows | size of row group
  group: Record
  block_parameter: ParquetRowGroupSize
  values: '"512" (default) | positive number in the range (0, 1000] in quotes'
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Number of input ports** — Number of input ports `1` (default) | integer in the range [`1,100`]

Number of input ports, specified as an integer between `1` and
`100`, inclusive.

The XY Graph block is an alternative configuration of the
Record block that visualizes data connected to two input ports on an
XY plot. In the XY Graphblock, the first input port provides the
*x* data, and the second input port provides the
*y* data.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `NumPorts` |
| **Values:** | 1 (default) | integer in the range [`1`, `100`] |
| **Data Types:** | `integer` |

**Example:** `set_param("myModel/Record","NumPorts",2)`

### **Decimation** — Decimation factor `1` (default) | positive integer

*Since R2025a*

Specify a decimation factor to reduce the effective sample rate for the logged
data. For a decimation factor, *n*, the Record block
logs every *n*th sample value. For
example, when you specify the **Decimation** value as
`2`, the Record block logs every other data
point.

For more information about controlling which samples are logged during simulation,
see Specify Signal Values to Log.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Decimation` |
| **Values:** | `"1"` (default) | positive integer in quotes |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param("myModel/Record","Decimation","2")`

### **Limit data points to last** — Number of samples to log `inf` (default) | scalar | vector

*Since R2025a*

When you want to save or analyze only the data from the end of a simulation,
specify the number of samples you want to log as a positive integer greater than zero.
By default, the Record block logs data for the entire simulation, and
the value for the **Limit data points to last** parameter is
`inf`.

Limiting logged data to the last *n* signal values directly
impacts memory allocation. When you specify this parameter, the software allocates
memory upfront based on the specified value, not on the time steps generated during
the simulation. For this reason, the **Limit data points to
last** parameter is not recommended when logging an indeterminate number
of time steps.

For more information about controlling which samples are logged during simulation,
see Specify Signal Values to Log.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `MaxDataPoints` |
| **Values:** | `"inf"` (default) | positive integer in quotes |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param("myModel/Record","MaxDataPoints","20")`

### **Select port** — Port for which to specify input processing mode `1` (default) | integer

Use the **Select port** and **Input processing**
parameters together to specify the input processing mode for a port. The input
processing mode determines how the Record block interprets matrix data:

- Sample-based — Each element in the matrix is a separate channel.
- Frame-based — Each column in the matrix is a separate channel.

To use frame-based input processing, the signal must have a discrete sample rate,
and the sample values must be nonscalar with fixed dimensions.

By default, each port processes the input signal as sample-based.

To change the input processing mode for a port:

1. Select the port number using the **Select port**
   parameter.
2. Select the input processing mode using the **Input
   processing** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

Programmatically specify the input processing mode for each port by specifying
the `FrameSettings` parameter as a row vector with as many elements
as block ports. The element index corresponds to the port number on the block.
Specify `1` to use frame-based input processing for the port and
`0` to use sample-based processing.

|  |  |
| --- | --- |
| **Parameter:** | `FrameSettings` |
| **Values:** | `false` (default) | `1`-by-`n` row vector of logical values, where `n` is equal to the number of ports |
| **Data Types:** | `logical array` |

**Example:** `set_param("myModel/Record","FrameSettings",[true,false,true])`

### **Input processing** — Input processing mode for selected port `Elements as channels (sample-based)` (default) | `Columns as channels (frame-based)`

Use the **Select port** and **Input processing**
parameters together to specify the input processing mode for a port. The input
processing mode determines how the Record block interprets matrix data:

- Sample-based — Each element in the matrix is a separate channel.
- Frame-based — Each column in the matrix is a separate channel.

To use frame-based input processing, the signal must have a discrete sample rate,
and the sample values must be nonscalar with fixed dimensions.

By default, each port processes the input signal as sample-based.

To change the input processing mode for a port:

1. Select the port number using the **Select port**
   parameter.
2. Select the input processing mode using the **Input
   processing** parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

Programmatically specify the input processing mode for each port by specifying
the `FrameSettings` parameter as a row vector with as many elements
as block ports. The element index corresponds to the port number on the block.
Specify `1` to use frame-based input processing for the port and
`0` to use sample-based processing.

|  |  |
| --- | --- |
| **Parameter:** | `FrameSettings` |
| **Values:** | `false` (default) | `1`-by-`n` row vector of logical values, where `n` is equal to the number of ports |
| **Data Types:** | `logical array` |

**Example:** `set_param("myModel/Record","FrameSettings"[true,false,true])`

### Record

### **Record to workspace** — Workspace logging option `off` (default) | `on`

Workspace logging option. By default, the Record block logs data
only to the Simulation Data Inspector. Select **Record to workspace**
to log data for signals connected to the Record block to the
MATLAB® workspace in a `Simulink.SimulationData.Dataset`
object.

Use the **Workspace variable name** parameter to specify the name
of the `Dataset` object that contains the logged Record
block data.

#### Tips

- When you log data to the workspace, the way you access the data depends on
  your model configuration. By default, models provide all logged data in a single
  output variable as a `Simulink.SimulationOutput` object.
  You can access the Record block data using the `get` function or a dot with the
  Record block workspace variable name. When the **Single simulation output**
  option is disabled, logging data appears in separate variables in the workspace,
  and you access the Record block data directly.
- Logging intervals specified using the **Logging intervals**
  configuration parameter apply to data logged to the workspace using the
  Record block.
- Use a single Record block to log data to the Simulation Data
  Inspector, the workspace, and a file.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RecordToWorkspace` |
| **Values:** | `"off"` (default) | "on" | `false` or `0` | `true` or `1` |

**Example:** `set_param("myModel/Record","RecordToWorkspace","on")`

### **Workspace variable name** — Name for workspace variable that contains logged block data `recordout` (default) | character vector | string

Name for the workspace variable that contains the logged block data.

#### Dependencies

To enable this parameter, select the **Record to workspace**
parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `VariableName` |
| **Values:** | `"recordout"` (default) | valid MATLAB variable name |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param("myModel/Record","VariableName","RecordedData")`

### **Record to file** — Log to file option `off` (default) | `on`

Log to file option. By default, the Record block logs data to the
Simulation Data Inspector only. Select **Record to file** to log data
for signals connected to the Record block to a file.

#### Tips

- Use the **File name** parameter to specify a name for the
  file.
- Use the **File type** parameter to specify whether to log
  data to an MLDATX file, a MAT file, an Excel file, or a Parquet
  file *(since R2025a)*.
- Use the **File location** parameter to specify the path
  to the file.
- Logging intervals specified using the **Logging intervals**
  configuration parameter do not apply to data logged to a file using the
  Record block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RecordToFile` |
| **Values:** | `"off"` (default) | "on" | `false` or `0` | `true` or `1` |

**Example:** `set_param("myModel/Record","RecordToFile","on")`

### **File name** — Name of file with logged data `recording.mldatx` (default) | character vector | string

Name of the file that contains the logged data. The name does not need to include
the file extension. If you do include the file extension in the name, ensure the name
uses a valid extension for the specified **File type**.

#### Tips

- If you do not change the name or location of the file you log to from one
  run to the next, the Record block overwrites prior data in the
  file.
- When you want to save the file in a location other than your working
  directory, use the **File location** parameter to specify the
  path to the directory where you want to save the file.

#### Dependencies

To enable this parameter, select the **Record to file**
parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

Specify the **File name**, **File type**, and
**File location** parameters. Include the extension for the
desired file type in the name you pass to `set_param`. When you
want to save the file somewhere other than the current working directory, specify
the path with the filename and extension.

|  |  |
| --- | --- |
| **Parameter:** | `FileName` |
| **Values:** | `"recording.mldatx"` (default) | valid filename |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param("myModel/Record","FileName","myRecording.mldatx")`

### **File type** — Type of file for logged data `*.mldatx` (default) | `*.mat` | `*.xslx` | `*.parquet`

Use the **File type** parameter to specify whether you want to
log data to an MLDATX, MAT, Excel, or Parquet file *(since R2025a)*.

#### Tips

- When you log data to an Excel file, the data is formatted as described in Microsoft Excel Import, Export, and Logging Format.
- When you log data to an Excel file, you can specify whether to share time columns using the
  **Time** parameter and which signal attributes to log using
  the **Attributes** parameter.

#### Dependencies

To enable this parameter, select **Record to file**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

Use the `FileName` parameter to specify the **File
name**, **File type**, and **File
location** parameters. Include the extension for the desired file type in
the name you pass to `set_param`. When you want to save the file
somewhere other than the current working directory, specify the path with the
filename and extension.

|  |  |
| --- | --- |
| **Parameter:** | `FileName` |
| **Values:** | `"recording.mldatx"` (default) | valid filename |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param("myModel/Record","FileName","myRecording.parquet")`

### **File location** — Path to file with logged data working directory (default) | character vector | string

Use the **File location** parameter to specify the location where
you want to save the file with the logged data when you want to save the file
somewhere other than the working directory. Ensure you have write permissions in the
directory you specify.

#### Dependencies

To enable this parameter, select **Record to file**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

Use the `FileName` parameter to specify the **File
name**, **File type**, and **File
location** parameters. Include the extension for the desired file type in
the name you pass to `set_param`. When you want to save the file
somewhere other than the current working directory, specify the path with the
filename and extension.

|  |  |
| --- | --- |
| **Parameter:** | `FileName` |
| **Values:** | `"recording.mldatx"` (default) | valid filename |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param("myModel/Record","FileName","myRecording.mldatx")`

### **Time** — Options for exporting time data to Excel or Parquet file `Shared Time Columns` (default) | `Individual Time Columns`

Specify how to log signal time data when you log the Record block
data to an Excel file or Parquet file *(since R2025a)*.

- `Shared Time Columns` — When time data is identical for
  multiple signals, the signals share a single time column in the logging file.
  The logging file can still include multiple time columns if the
  Record block logs data for signals with unique time
  data.
- `Individual Time Columns` — Each logged signal always has
  its own time column in the logging file.

#### Dependencies

To enable this parameter, select **Record to file** and specify
**File type** as `*.xlsx` or `*.parquet` *(since R2025a)*.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

Programmatically setting the **Time** parameter is supported
only for Parquet files.

|  |  |
| --- | --- |
| **Parameter:** | `SharedTimeColumn` |
| **Values:** | `"on"` (default) | `"off"` |

**Example:** `set_param("myModel/Record","SharedTimeColumn",
"off")`

### **Signal Attributes** — Signal attributes to export to Excel file `Data Type` | `Units` | `Port Index` | `Block Path` | `Interpolation`

Select one or more signal attribute options to include in the logging file when
you log data to an Excel file. Selected signal attributes appear in the signal column above the
first data point according to the format described in Microsoft Excel Import, Export, and Logging Format.

#### Dependencies

To enable this parameter, select **Record to file** and specify
**File type** as `*.xlsx`.

### **Compression Type** — Compression options `Fastest (snappy)` (default) | `Balanced for Size and Speed (gzip)` | `Compact (brotli)` | `None (uncompressed)`

*Since R2025a*

Specify compression as one of these options:

- `Fastest (snappy)` — Similar save speed to an
  uncompressed file, smaller file size
- `Balanced for Size and Speed (gzip)` — Balance
  between file size and save speed
- `Compact (brotli)` — Smallest file size, slowest save
  speed
- `None (uncompressed)` — Largest file size, fastest
  save speed

#### Dependencies

To enable this parameter, select **Record to file** and specify
**File type** as `*.parquet`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ParquetCompression` |
| **Values:** | `"fastest"` (default) | `"balanced"` | `"compact"` | `"none"` |

**Example:** `set_param("myModel/Record","ParquetCompression","balanced")`

### **Generate Sidecar** — Option to generate JSON sidecar `on` (default) | `off`

*Since R2025a*

Select this parameter to generate a JSON sidecar that contains all the logged
metadata.

#### Dependencies

To enable this parameter, select **Record to file** and specify
**File type** as `*.parquet`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ParquetMetaData` |
| **Values:** | `"on"` (default) | `"off"` |

**Example:** `set_param("myModel/Record","ParquetMetaData","off")`

### **Row Group Policy** — Options for grouping rows in Parquet file `Row Group Height` (default) | `Row Group Size (MB)`

*Since R2025a*

Specify row groups in the Parquet file.

- `Row Group Height` — Specify the number of rows per
  group.
- `Row Group Size (MB)` — Specify the size of the row group
  in megabytes.

#### Dependencies

To enable this parameter, select **Record to file** and specify
**File type** as `*.parquet`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ParquetRowGroupPolicy` |
| **Values:** | `"height"` (default) | `"sizeinmb"` |

**Example:** `set_param("myModel/Record","ParquetRowGroupPolicy","sizeinmb")`

### **Row Group Policy Value** — Height or size of row group `auto` (default when `Row Group Policy` is `Row Group Height`) | `512` (default when `Row Group Policy` is `Row Group Size (MB)` | number of rows | size of row group

*Since R2025a*

To specify the number of rows in each row group, set the **Row Group
Policy** parameter to `Row Group Height`. Then, use the
**Row Group Policy Value** parameter to define the number of rows
in each group, choosing a value between `1` and
`67,108,864`. By default, the value is `auto`,
which creates the largest possible row group without exceeding 512 MB.

To specify the size of each row group, set the **Row Group
Policy** parameter to `Row Group Size (MB)`. Then, use
the **Row Group Policy Value** parameter to set the data size of
the row group in megabytes, up to 1GB.

#### Dependencies

To enable this parameter, select **Record to file** and specify
**File type** as `*.parquet`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ParquetRowGroupHeight` |
| **Values:** | `"auto"` (default) | integer in the range [`1`, `67108864`] in quotes |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param("myModel/Record","ParquetRowGroupPolicy","height","ParquetRowGroupHeight","5000")`

|  |  |
| --- | --- |
| **Parameter:** | `ParquetRowGroupSize` |
| **Values:** | `"512"` (default) | positive number in the range (`0`, `1000`] in quotes |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param("myModel/Record","ParquetRowGroupPolicy","sizeinmb","ParquetRowGroupsize","450")`
## Libraries

Simulink / Sinks

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

This block is ignored for code generation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `No HDL` | Do not generate HDL code for this block. |

**HDL Block Properties**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | Control the removal of unconnected logic. The default is `off`, which means unconnected logic is not preserved in HDL code. For more details, see PreserveUpstreamLogic (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

This block is ignored for code generation.

## Version History

**Introduced in R2021a**

### R2025a: Log `datetime` data

The Record block supports logging `datetime` data.

### R2025a: Live streaming no longer supported in XY visualizations

To avoid scalability issues, data is no longer streamed to XY visualizations in the
Simulation Data Inspector, Record block, or XY Graph
block.

### R2025a: Limit data logged by Record block

Limit the size of data logged by the Record block by specifying signal
values to log. You can specify signal values to log using these two parameters:

- **Decimation** — Log every *n*th signal value.
- **Limit data points to last** — Log only the last
  *n* signal values.

### R2025a: Export data to a Parquet file using the Record block

Use the Record block to export data from scalar and multidimensional
signals, as well as data from buses or arrays of buses, to a Parquet file. The
Record block logs and can export real and complex data of any built-in data
type, as well as enumerations, strings, and fixed-point data. For more information, see
Export Data to Parquet File Using Record Block.

### R2023b: Log unbounded variable-size signals

In normal and accelerator mode simulations, the Record block supports
logging unbounded variable-size signals but does not support visualizing
unbounded-variable-size signals. Logging is not supported for nonvirtual buses that contain
unbounded variable-size signals.

### R2023a: Log nonvirtual buses that contain variable-size signals

In normal and accelerator mode simulations, the Record block supports
logging:

- Nonvirtual buses that contain variable-size signals directly or in nested
  buses
- Buses with nested nonvirtual buses that contain variable-size signals

In normal mode simulations only, the Record block supports
logging:

- Arrays of buses with nonvirtual buses that contain variable-size signals

The Record block does not support visualizing variable-size
signals.

### R2022b: Scale individual signals

You can set the display scale and offset for an individual signal in the Record
block.

- Time plots and sparklines — Scale and offset the display of *y* values.
- XY plots — Scale and offset the display of the *x*
  values and *y* values independently.
- Maps — Scale and offset the longitude and latitude independently.

Cursors continue to show the unscaled values.

### R2021b: XY Graph block replaced with alternative configuration of the Record block

The XY Graph block is replaced with a Record block that is
preconfigured to display two input signals on an XY plot. Using the updated XY
Graph block, you can:

- View data on the XY plot during simulation.
- Record the XY plot data to the workspace, a file, or the workspace and a
  file.
- Zoom, pan, fit to view, and adjust the axis limits for the XY plot without having to
  simulate again.
- Analyze the XY trace by using cursors and by adding a trend line.
- Add additional ports and subplots to visualize additional simulation data alongside
  the XY plot on several visualization types, including time plots, maps, or additional XY
  plots.
- Visualize multiple traces on the XY plot.

Upon simulation, the prior version of the XY Graph block opened a new
window to display the connected signal data during simulation. To view data on the updated
XY Graph block, double-click the block in the model. To view the XY plot in
a new window, right-click the block and select **Open in New
Window**.

XY Graph blocks in existing models are automatically replaced with the
new XY Graph block. XY Graph viewers are also replaced with the new XY
Graph block. Goto and From blocks connect signals to
the XY Graph block that replaces the XY Graph viewer.

Signals connected to an XY Graph block always stream to the Simulation
Data Inspector.

### R2021a: **Logging intervals** configuration parameter applies to data logged to the workspace using the Record block

The **Logging intervals** configuration parameter applies to data
logged to the workspace using the Record block.

The **Logging intervals** parameter does not affect data logged to a
file using the Record block or how signals are displayed in the
Record block. You can also access complete signal data for signals
connected to the Record block in the Simulation Data Inspector.

## Description

View and log data to the workspace, a file, or both

Use the Record block or the XY Graph block to record data to
the workspace, a file, or to both the workspace and a file. When you log data to a file, you
can choose to log to a MAT file, an MLDATX file, an Excel® file, or a Parquet file *(since R2025a)*. Signals connected
to a Record block always log to the Simulation Data Inspector. If you decide
that you need to save data after simulation, you can export data from the
Record block to the workspace or to any supported file type except a Parquet
file.

You can also use the Record block to visualize connected signals. To view
data for signals connected to the Record block, double-click the block. You
have access to simulation controls, such as the **Run** button, while viewing
data in the Record block.

By default, the Record block displays all connected signals on a sparklines
plot. A sparkline is added for each connected signal. After sparklines fill the visible space,
a scrollbar allows you to continue plotting signals.

A model opened to view data logged by a Record block with the block parameters visible in the Property Inspector

### Build Visualizations

The Record block supports most visualizations available in the Simulation
Data Inspector. When a different visualization makes sense for your data, you can modify the
plot layout and plot types using the **Layouts** option and the plot types
selector, labeled **Sparklines** by default. Use the
**Layouts** list to select a layout of subplots. To change the plot type
of a subplot, select the subplot then select the desired plot type from the plot types
selector.

For more information, see Log Data to the Workspace and a File Using the Record Block. For examples that show
how to use each visualization type, see:

- Sparklines — View Many Signals Together Using Sparklines
- XY — Visualize Simulation Data on XY Plot and Analyze Data Using XY Plot
- Map — View and Replay Map Data
- Time plot and text editor — Create Plots Using the Simulation Data Inspector
