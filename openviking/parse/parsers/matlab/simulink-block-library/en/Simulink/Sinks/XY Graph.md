---
type: simulink-block
title: 'Record, XY Graph'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2023b
official_category: 'Sinks'
documentation_page: 'record'
documentation_source_path: 'slref/record.html'
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
    | enumerated | bus | image
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

- To log frame-based data, specify the **Input Processing**
  parameter for each port that receives a frame-based signal.
- When you connect a nonscalar signal to an input port of the XY
  Graph block, you must manually configure which channels or elements of
  the nonscalar signal provide the *x* and *y*
  data for the XY plot.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Number of input ports
  summary: Number of input ports 1 (default) | integer in the range [1,100]
  group: Main
  block_parameter: '''NumPorts'''
  type: integer | character vector
  values: integer in the range [1,100]
  default: '1'
- name: Port
  summary: Port for which to specify input processing mode 1 (default) | integer
  group: Main
  block_parameter: '''FrameSettings'''
  type: logical array
  values: 1-by-n row vector, where n is equal to the number of ports
  default: '0'
- name: Input Processing
  summary: Input processing mode for selected port Elements as channels (sample-based) (default) | Columns as channels (frame-based)
  group: Main
  block_parameter: '''FrameSettings'''
  type: logical array
  values: 1-by-n row vector, where n is equal to the number of ports
  default: '0'
- name: Record to Workspace
  summary: Workspace logging option off (default) | on
  group: Record
  block_parameter: '''RecordToWorkspace'''
  type: character vector | boolean | numeric
  values: '''on'' | ''off'' | true or 1 | false or 0'
  default: '''off'''
- name: Workspace Variable Name
  summary: Name for workspace variable that contains logged block data recordout (default) | character vector | string
  group: Record
  block_parameter: '''VariableName'''
  type: character vector | string
  default: '''recordout'''
- name: Record to File
  summary: Log to file option off (default) | on
  group: Record
  block_parameter: '''RecordToFile'''
  type: character vector | boolean | numeric
  values: '''on'' | ''off'' | true or 1 | false or 0'
  default: '''off'''
- name: File Name
  summary: Name of file with logged data recording.mldatx (default) | character vector | string
  group: Record
  block_parameter: '''FileName'''
  type: character vector | string
  default: '''recording.mldatx'''
- name: File Type
  summary: Type of file for logged data *.mldatx (default) | *.mat | *.xslx
  group: Record
  block_parameter: '''FileName'''
  type: character vector | string
  default: '''recording.mldatx'''
- name: File Location
  summary: Path to file with logged data working directory (default) | character vector | string
  group: Record
  block_parameter: '''FileName'''
  type: character vector | string
  default: '''recording.mldatx'''
- name: Time
  summary: Options for exporting time data to Excel file Shared Time Columns (default) | Individual Time Columns
  group: Record
- name: Attributes
  summary: Signal attributes to export to Excel file Data Type | Units | Port Index | Block Path | Interpolation
  group: Record
```

To modify Record block parameters, use the Property Inspector.

### Main

### **Number of input ports** — Number of input ports `1` (default) | integer in the range [`1,100`]

Number of input ports, specified as an integer between `1` and
`100`, inclusive.

The XY Graph block is an alternative configuration of the
Record block that visualizes data connected to two input ports on an
XY plot. The first input port provides the *x* data for the XY plot,
and the second input port provides the *y* data.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'NumPorts'` |
| **Type:** `integer` | `character vector` |
| **Values:** integer in the range [`1`,`100`] |
| **Default:** `1` |

### **Port** — Port for which to specify input processing mode `1` (default) | integer

Use the **Port** and **Input Processing**
parameters together to specify the input processing mode for a port. The input
processing mode determines how the Record block interprets matrix data:

- Sample-based — Each element in the matrix is a separate channel.
- Frame-based — Each column in the matrix is a separate channel.

To use frame-based input processing, the signal must have a discrete sample rate,
and the sample values must be nonscalar with fixed dimensions.

By default, each port processes the input signal as sample-based.

To change the input processing mode for a port:

1. Select the port number using the **Port** parameter.
2. Select the input processing mode using the **Input
   Processing** parameter.

#### Programmatic Use

Programmatically specify the input processing mode for each port by specifying
the `FrameSettings` parameter as a row vector with as many elements
as block ports. The element index corresponds to the port number on the block.
Specify `1` to use frame-based input processing for the port and
`0` to use sample-based processing.

|  |
| --- |
| **Block Parameter:** `'FrameSettings'` |
| **Type:** logical array |
| **Values:** `1`-by-`n` row vector, where `n` is equal to the number of ports |
| **Default:** `0` |

### **Input Processing** — Input processing mode for selected port `Elements as channels (sample-based)` (default) | `Columns as channels (frame-based)`

Use the **Port** and **Input Processing**
parameters together to specify the input processing mode for a port. The input
processing mode determines how the Record block interprets matrix data:

- Sample-based — Each element in the matrix is a separate channel.
- Frame-based — Each column in the matrix is a separate channel.

To use frame-based input processing, the signal must have a discrete sample rate,
and the sample values must be nonscalar with fixed dimensions.

By default, each port processes the input signal as sample-based.

To change the input processing mode for a port:

1. Select the port number using the **Port** parameter.
2. Select the input processing mode using the **Input
   Processing** parameter.

#### Programmatic Use

Programmatically specify the input processing mode for each port by specifying
the `FrameSettings` parameter as a row vector with as many elements
as block ports. The element index corresponds to the port number on the block.
Specify `1` to use frame-based input processing for the port and
`0` to use sample-based processing.

|  |
| --- |
| **Block Parameter:** `'FrameSettings'` |
| **Type:** logical array |
| **Values:** `1`-by-`n` row vector, where `n` is equal to the number of ports |
| **Default:** `0` |

### Record

### **Record to Workspace** — Workspace logging option `off` (default) | `on`

Workspace logging option. By default, the Record block logs data to
the Simulation Data Inspector only. Select **Record to Workspace** to
log data for signals connected to the Record block to the MATLAB® workspace in a `Simulink.SimulationData.Dataset`
object.

Use the **Workspace Variable Name** parameter to specify the name
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
- You can use a single Record block to log data to the
  Simulation Data Inspector, to the workspace, and to a file.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'RecordToWorkspace'` |
| **Type:** character vector | boolean | numeric |
| **Values:** `'on'` | `'off'` | `true` or `1` | `false` or `0` |
| **Default:** `'off'` |

### **Workspace Variable Name** — Name for workspace variable that contains logged block data `recordout` (default) | character vector | string

Name for the workspace variable that contains the logged block data.

#### Dependencies

To enable this parameter, select the **Record to Workspace**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'VariableName'` |
| **Type:** character vector | string |
| **Default:** `'recordout'` |

### **Record to File** — Log to file option `off` (default) | `on`

Log to file option. By default, the Record block logs data to the
Simulation Data Inspector only. Select **Record to File** to log data
for signals connected to the Record block to a file.

#### Tips

- Use the **File Name** parameter to specify a name for the
  file.
- Use the **File Type** parameter to specify whether to log
  data to an MLDATX file, a MAT file, or an Excel file.
- Use the **File Location** parameter to specify the path
  to the file.
- Logging intervals specified using the **Logging intervals**
  configuration parameter do not apply to data logged to a file using the
  Record block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `'RecordToFile'` |
| **Type:** character vector | boolean | numeric |
| **Values:** `'on'` | `'off'` | `true` or `1` | `false` or `0` |
| **Default:** `'off'` |

### **File Name** — Name of file with logged data `recording.mldatx` (default) | character vector | string

Name of the file that contains the logged data. The name does not need to include
the file extension. If you do include the file extension in the name, ensure the name
uses a valid extension for the specified **File Type**.

#### Tips

- If you do not change the name or location of the file you log to from one
  run to the next, the Record block overwrites prior data in the
  file.
- When you want to save the file in a location other than your working
  directory, use the **File Location** parameter to specify the
  path to the directory where you want to save the file.

#### Dependencies

To enable this parameter, select the **Record to File**
parameter.

#### Programmatic Use

Use the `FileName` parameter to specify the **File
Name**, **File Type**, and **File
Location** parameters. Include the extension for the desired file type in
the name you pass to `set_param`. When you want to save the file
somewhere other than the current working directory, specify the path with the file
name and extension.

|  |
| --- |
| **Block Parameter:** `'FileName'` |
| **Type:** character vector | string |
| **Default:** `'recording.mldatx'` |

### **File Type** — Type of file for logged data `*.mldatx` (default) | `*.mat` | `*.xslx`

Use the **File Type** parameter to specify whether you want to
log data to an MLDATX file, a MAT file, or an Excel file.

#### Tips

- When you log data to an Excel file, the data is formatted as described in Microsoft Excel Import, Export, and Logging Format.
- When you log data to an Excel file, you can specify whether to share time columns using the
  **Time** parameter and which signal attributes to log using
  the **Attributes** parameter.

#### Dependencies

To enable this parameter, select **Record to File**.

#### Programmatic Use

Use the `FileName` parameter to specify the **File
Name**, **File Type**, and **File
Location** parameters. Include the extension for the desired file type in
the name you pass to `set_param`. When you want to save the file
somewhere other than the current working directory, specify the path with the file
name and extension.

|  |
| --- |
| **Block Parameter:** `'FileName'` |
| **Type:** character vector | string |
| **Default:** `'recording.mldatx'` |

### **File Location** — Path to file with logged data working directory (default) | character vector | string

Use the **File Location** parameter to specify the location where
you want to save the file with the logged data when you want to save the file
somewhere other than the working directory. Ensure you have write permissions in the
directory you specify.

#### Dependencies

To enable this parameter, select **Record to File**.

#### Programmatic Use

Use the `FileName` parameter to specify the **File
Name**, **File Type**, and **File
Location** parameters. Include the extension for the desired file type in
the name you pass to `set_param`. When you want to save the file
somewhere other than the current working directory, specify the path with the file
name and extension.

|  |
| --- |
| **Block Parameter:** `'FileName'` |
| **Type:** character vector | string |
| **Default:** `'recording.mldatx'` |

### **Time** — Options for exporting time data to Excel file `Shared Time Columns` (default) | `Individual Time Columns`

Use the **Time** parameter to specify how to log signal time data
when you log the Record block data to an Excel file.

- `Shared Time Columns` — When time data is identical for
  multiple signals, the signals share a single time column in the logging file.
  The logging file may still include multiple time columns if the
  Record block logs data for signals with unique time
  data.
- `Individual Time Columns` — Each logged signal always has
  its own time column in the logging file.

#### Dependencies

To enable this parameter, select **Record to File** and specify
**File Type** as `*.xlsx`.

### **Attributes** — Signal attributes to export to Excel file `Data Type` | `Units` | `Port Index` | `Block Path` | `Interpolation`

Select one or more signal attribute options to include in the logging file when
you log data to an Excel file. Selected signal attributes appear in the signal column above the
first data point according to the format described in Microsoft Excel Import, Export, and Logging Format.

#### Dependencies

To enable this parameter, select **Record to File** and specify
**File Type** as `*.xlsx`.
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

You can use this block to record data from a simulation when you use the block with
subsystems that generate HDL code. The block cannot be included in the hardware
implementation.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

This block is ignored for code generation.

## Version History

**Introduced in R2021a**

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

Log data to the workspace, to a file, or both

You can use the Record block or the XY Graph block to record
data to the workspace, to a file, or to both the workspace and a file. When you log data to a
file, you can choose to log to a MAT file, an MLDATX file, or an Excel® file. Signals connected to a Record block always log to the
Simulation Data Inspector. If you decide that you need to save data after simulation, you can
export data from the Record block to the workspace or to any supported file
type.

You can also use the Record block to visualize connected signals. To view
data for signals connected to the Record block, double-click the block. You
have access to simulation controls, such as the **Run** button, while viewing
data in the Record block.

By default, the Record block displays all connected signals on a sparklines
plot. A sparkline is added for each connected signal. After sparklines fill the visible space,
a scrollbar allows you to continue plotting signals.

A model opened to view data logged by a Record block with the block parameters visible in the Property Inspector.

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

The Record block does not support the array visualization available in
the Simulation Data Inspector. The Record block supports logging
multidimensional signal data, including variable-size signals, but does not support
visualizing multidimensional data. To visualize the data for a multidimensional signal using
the Record block, convert the signal with multidimensional sample values to a
set of signals, called *channels*, that each have scalar sample values.
For more information, see Analyze Multidimensional Signal Data.
