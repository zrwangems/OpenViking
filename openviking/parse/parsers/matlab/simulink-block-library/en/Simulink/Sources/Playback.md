---
type: simulink-block
title: 'Playback'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'playback'
documentation_source_path: 'slref/playback.html'
language: en
---

# Playback

## Ports

### Output

### **Port\_1** — Data loaded from workspace, file, or Simulation Data Inspector scalar | vector | matrix | array

The Playback block supports loading real or complex signals with fixed or
variable dimensions, discrete and continuous signals, messages ,
multidimensional signals, buses, and arrays of buses.

When you load bus data, the Playback block assigns a port to each element
of the bus.

The Playback block cannot load data as a message if the data type is
floating-point `half`.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`
**Complex Number Support:** Yes

## Parameters

### Port Parameters

You can access port parameters through the **Port Editor**. Double-click
the Playback block. In the **Simulation** tab, in
the **Port** section, click **Port Editor**.
Properties for each port can be set independently using the **Port
Editor**.

### **Number of Ports** — Number of output ports `0` (default) | integer in the range [`0,100`]

When you add signals to the Playback block and automatically assign
signals to ports, a new port is created for each signal or bus element
you add. You can add or delete ports after adding signal data. The
number of ports does not need to be equal to the number of signals you
add to the block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `NumPorts` |
| **Values:** | `0` (default) | integer in the range [`0`,`100`] |
| **Data Types:** | `integer` |

**Example:** `set_param(gcb,"NumPorts",5)`

### **Data Type** — Output data type for each port `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `string` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | ...

By default, the port data type is inherited from the source data type
or from a downstream block.

You can set the data type of the port independently of the signal data type. For
numerical data, the Playback block converts to the data
type specified by the port. If a conversion is not possible, such as in
the case of converting numerical data to a string, the software throws
an error.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

The size of the string array is equal to the number of ports. The
index of each element is determined by the port number.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `"Inherit: auto"` (default) | `"double"` | `"single"` | `"half"` | `"int8"` |  `"uint8"`  | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"string"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` |
| **Data Types:** | `string array` |

**Example:** `set_param(gcb,"OutDataTypeStr",["double","int64"])`

### **Complexity** — Complexity of each port `"auto"` (default) | `"real"` | `"complex"`

You can specify the complexity for each port independently. Port
complexity does not need to match the corresponding signal complexity.
By default, the complexity of the port is `"auto"` and
inherited from the signal data.

- If the signal data is real, the complexity of the port
  that loads the signal can be real or complex. If the port is
  set to `"complex"`, the complex part of the
  signal is a signal ground.
- If the signal data is complex, the complexity of the port
  that loads the signal must be complex.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

The size of the string array is equal to the number of ports. The
index of each element is determined by the port number.

|  |  |
| --- | --- |
| **Parameter:** | `PortComplexity` |
| **Values:** | `"auto"` (default) | `"real"` | `"complex"` |
| **Data Types:** | `string array` |

**Example:** `set_param(gcb,"PortComplexity",["auto","real","complex","real"])`

### **Units** — Physical units for each port inherit (default) | supported physical unit

Physical units for each port, specified as a supported physical unit.
To see a list of supported physical units, use the function
`showunitslist`.

```
showunitslist
```

- If no unit is set on the port, the output units are
  inherited from the signal units.
- If different units are set on both the signal and the
  port, then the Playback block performs a unit
  conversion if the units are compatible.

The Playback block propagates units for each
port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

The size of the string array is equal to the number of ports. The
index of each element is determined by the port number.

|  |  |
| --- | --- |
| **Parameter:** | `PortUnits` |
| **Values:** | `" "` (default) | supported physical unit |
| **Data Types:** | `string array` |

**Example:** `set_param(gcb,"PortUnits",["m","m/s","m/s^2"])`

### **Sample time** — Output sample period and optional time offset `-1` | scalar | vector

The **Sample time** parameter specifies when the
block computes a new output value during simulation. For details, see
Specify Sample Time.

Specify the **Sample time** parameter as a scalar
when you do not want the output to have a time offset. To add a time
offset to the output, specify the **Sample time**
parameter as a `1`-by-`2` vector where
the first element is the sampling period and the second element is the
offset.

By default, the **Sample time** parameter value is
`-1`, which indicates that the port sample time is
inherited from the signal. If the sample time of a port differs from the
sample time of the associated signal, the Playback block
interpolates data as needed using the interpolation setting of the
signal.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

The size of the string array is equal to the number of ports. The
index of each element is determined by the port number.

|  |  |
| --- | --- |
| **Parameter:** | `PortSampleTimes` |
| **Values:** | `"-1"` (default) | scalar | vector |
| **Data Types:** | `string array` |

**Example:** `set_param(gcb,"PortSampleTimes",["-1","0","inf"])`

### **Dimensions** — Dimensions of each port `" "` (default) | integer | integer array

To inherit the dimensions of a port from the data, leave the parameter empty. If the
port does not have assigned data, setting the dimensions generates the
ground.

The Playback block stores a multidimensional signal as a single signal
with nonscalar sample values, a set of channels, or frames. For more
information, see Analyze Multidimensional Signal Data.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

The size of the cell array is equal to the number of ports. The
index of each element is determined by the port number.

|  |  |
| --- | --- |
| **Parameter:** | `PortDimensions` |
| **Values:** | empty `1×1` cell array (default) | cell array of positive integers | cell array of vectors |
| **Data Types:** | `cell array` |

**Example:** `set_param(gcb,"PortDimensions",[{2},{[1,2,3]}])`

### **Dimension Mode** — Dimension mode of each port `"auto"` (default) | `"Fixed"` | `"Variable"`

Dimension mode of each port, returned as a string array where each
element may be `"auto"`, `"Fixed"`, or
`"Variable"`.

- If the dimension mode is `"auto"`, then
  the port inherits the dimension mode from the data.
- If the dimension mode is `"Fixed"`, then
  the port allows only fixed-sized signals.
- If the dimension mode is `"Variable"`,
  then the port allows only variable-size signals.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

The size of the string array is equal to the number of ports. The
index of each element is determined by the port number.

|  |  |
| --- | --- |
| **Parameter:** | `PortDimsModes` |
| **Values:** | `"auto"` (default) | `"Fixed"` | `"Variable"` |
| **Data Types:** | `string array` |

**Example:** `set_param(gcb,"PortDimsModes",["Fixed","auto"])`

### Block Parameters

You can access most block parameters through the **Parameter Settings**.
Double-click the Playback block. In the
**Simulation** tab, click **Parameter
Settings** to configure block parameters.

Block parameter settings apply to all ports.

### **Before first point** — Extrapolation method to determine block output before first data point in loaded data `Linear` (default) | `Hold First Value` | `Ground Value`

Extrapolation method used to determine output values for simulation times before the
first sample in the file, workspace, or Simulation Data Inspector data.

| Method | Description | Example |
| --- | --- | --- |
| `Linear` | Extrapolated output depends on the type of data.  - For `double` data, the   Playback block linearly   extrapolates the output value using the first two   samples. - For `Boolean` data, the   Playback block uses the first data   point value for the output value. - For all other built-in data types, the   Playback block:  1. Upcasts the data to      `double`   2. Linearly extrapolates the output value using      the first two data samples   3. Downcasts the extrapolated data value to the      original data type  If the data contains only one sample, the Playback block provides that value at the output.  Do not use the `Linear` option when the Playback block loads enumerated or fixed-point data.  The extrapolation setting is applied to all signals in a bus. If any signal in the bus contains enumerated or fixed-point data, do not use the `Linear` option. | Plot that shows the output for a Playback block configured to linearly extrapolate the output value for simulation times before the first sample in the loaded data. The block loads data that starts 2 seconds into the simulation. |
| `Hold First Value` | The Playback block uses the first data value as the output value. | Plot that shows the output for a Playback block configured to hold the first value in the loaded data for simulation times before the first sample in the loaded data. The block loads data that starts 2 seconds into the simulation. |
| `Ground Value` | Extrapolated output depends on the type of data.  - Built-in numeric types —   `0` - `Boolean` —   `false` - Fixed-point data types — Representation for   value of `0`, which may not be   exactly `0` due to scaling and   limited precision. - Enumerated data types — Default value | Plot that shows the output for a Playback block configured to use the ground value as the output value for simulation times before the first sample in the loaded data. The block loads data that starts 2 seconds into the simulation. |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ExtrapolationBeforeFirstDataPoint` |
| **Values:** | `"Linear extrapolation"` (default) | `"Hold first value"` | `"Ground value"` |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param(gcb,"ExtrapolationBeforeFirstDataPoint","Hold
first value")`

### **After last point** — Extrapolation method to determine block output after final data point in loaded data `Linear` (default) | `Hold Last Value` | `Ground Value`

Extrapolation method used to determine output values for simulation
times after the last sample in the file, workspace, or Simulation Data
Inspector data.

| Method | Description | Example |
| --- | --- | --- |
| `Linear` | Extrapolated output depends on the type of data.  - For `double` data, the   Playback block linearly   extrapolates the output value using the last two   samples. - For `Boolean` data, the   Playback block uses the last sample   value for the output value. - For all other built-in data types, the   Playback block:  1. Upcasts the data to      `double`   2. Linearly extrapolates the output value using      the last two data samples   3. Downcasts the extrapolated data value to the      original data type  If the data contains only one sample, the Playback block uses that value as the output.  Do not use the `Linear` option when the Playback block loads enumerated or fixed-point data. | Plot that shows the output for a Playback block configured to linearly interpolate the output value for simulation times after the last sample in the loaded data. The block loads data that ends 2 seconds before the end of the simulation. |
| `Hold Last Value` | The Playback block uses the last data value as the output value. | Plot that shows the output for a Playback block configured to hold the last output value for simulation times after the last sample in the loaded data. The block loads data that ends 2 seconds before the end of the simulation. |
| `Ground Value` | The Playback block output value depends on the type of data.  - Built-in numeric types —   `0` - `Boolean` —   `false` - Fixed-point data types — Representation for   value of `0`, which may not be   exactly `0` due to scaling and   limited precision. - Enumerated data types — Default value | Plot that shows the output for a Playback block configured to use the ground value as the output value for simulation times after the last sample in the loaded data. The block loads data that ends 2 seconds before the end of the simulation. |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ExtrapolationAfterLastDataPoint` |
| **Values:** | `"Linear extrapolation"` (default) | `"Hold last value"` | `"Ground value"` |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param(gcb,"ExtrapolationAfterLastDataPoint","Hold
last value")`

### **Enable zero-crossing detection** — Zero-crossing detection `'off'` (default) | `'on'`

Zero-crossing detection locates discontinuities, or *zero
crossings*, in the block output and prevents excessively
small time steps near the discontinuities, which can slow down
simulation. The Playback block detects zero crossings for
a signal only when the sample time of the signal is continuous.

The loaded data creates a discontinuity in the block output when the
data includes multiple samples with the same time. For example, for this
input data, a discontinuity occurs at time
`2`.

```
time:     0 1 2 2 3
signal:   2 3 4 5 6
```

The Playback block can also create discontinuities in the output based on
how you configure interpolation and extrapolation.

- Setting **Before first point** to
  `Ground Value` can create a
  discontinuity at the first sample in the loaded data.
- Setting **After last point** to
  `Ground Value` can create a
  discontinuity at the last sample in the loaded data.

This block supports zero-crossing detection only in simulations
that use a variable-step solver. When you use a fixed-step solver for simulation, the software
does not detect or locate zero crossings for this block.

For more information, see Zero-Crossing Detection.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ZeroCross` |
| **Values:** | `"off"` (default) | `"on"` |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param(gcb,"ZeroCross","on")`

### **Signals** — Information about signals added to Playback block `Simulink.playback.Signal` object

*Since R2024a*

Information about signals added to Playback block, specified as a
`Simulink.playback.Signal` object.

You can use the **Signals** parameter to
retrieve information about signals in the block using the
`get_param` function or add new signals to the
block using the `set_param` function.
`Simulink.playback.Signal` objects store information
about signals added to the Playback block.

To add one or more signals to the Playback block, create a
`Simulink.playback.Signal` object using the `Simulink.playback.createSignals` function. Then, use the
`set_param` function to apply the
`Simulink.playback.Signal` object to the
**Signals** parameter of the
Playback block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Signals` |
| **Values:** | `Simulink.playback.Signal` object |

**Example:** `set_param(gcb,"Signals",pgSigObj)`

### Table Parameters

You can access table parameters through the **Format** tab of the
table visualization. To view a data table of the plotted signals, on the
**Simulation** tab, in the **View** section,
click **Show Table**. To configure table parameters, select the
table visualization, and then click the **Format** tab.

### **Table Placement** — Position of table visualization `Bottom` (default) | `Top` | `Left` | `Right` | `Center`

Position of the table visualization relative to the sparklines visualization, specified
as one of these options:

- `Bottom` — 2-by-1 layout with the data
  table in the lower subplot and the sparklines visualization
  in the upper subplot
- `Top` — 2-by-1 layout with the data table
  in the upper subplot and the sparklines visualization in the
  lower subplot
- `Left` — 1-by-2 layout with the data
  table in the left subplot and the sparklines visualization
  in the right subplot
- `Right` — 1-by-2 layout with the data
  table in the right subplot and the sparklines visualization
  in the left subplot
- `Center` — 1-by-1 layout of only the data
  table

### **Time Values** — Time-based column organization options `Union Time` (default) | `Shared Time` | `Individual Time`

Time-based column organization, specified as `Union
Time`, `Shared Time`, or
`Individual Time`.

| Column Organization Option | Description | Table Format |
| --- | --- | --- |
| `Shared Time` | Data is grouped by shared time columns. | Data table with shared time columns |
| `Individual Time` | Each signal is paired with its corresponding time column. | Data table with individual time columns |
| `Union Time` | Data is aligned with a single time column that includes every sample time between the signals.  When a signal does not have a data value for a given time step, the cell is empty. To interpolate missing data values, on the **Format** tab, click **Use Signal Interpolation**. Use the `Interp Method` property in the **Properties** pane to view or change the interpolation method for a selected signal. | Data table with a unified time column |

### **Use Signal Interpolation** — Option to interpolate missing data values `off` (default) | `on`

When you organize table data using the `Union Time` column organization
option, some signals might not have data points for each time step.
Click the **Use Signal Interpolation** button to
interpolate missing data values using the interpolation settings of each
signal. To view or change the interpolation method for a selected
signal, use the `Interp Method` property in the
**Properties** pane.

## Libraries

Simulink / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code.

## Version History

**Introduced in R2022b**

### R2025a: View signals in a data table

You can view plotted signals in a data table in addition to a sparklines
visualization.

### R2024b: Group data by source

You can group data in the signal table by source. When you group signals by
source, signals are organized based on whether the data originated from a file, the
workspace, or is saved in the model.

### R2024a: Add data to Playback block programmatically

You can add data from the workspace, a file, or the Simulation Data Inspector to
the Playback block programmatically by applying a
`Simulink.playback.Signal` object to the
**Signals** parameter of the block.

### R2024a: Search for signals in the Add Signals dialog box

When you use the Add Signals dialog box to add signals to the Playback block, you can
search for specific signals. You can also refine your search to exclude partial
matches, match specific capitalization, or use regular expressions to find signals
that follow a certain pattern.

### R2023b: Added Preferences dialog box

A Preferences dialog box has been added to the Playback block that lets you choose
how to group data in the signal table and which signal properties to display. You
can choose to group signals by data hierarchy or choose not to group data and
instead display a flat list of signals.

### R2023a: Load MLDATX files

The Playback block supports loading data from a Simulation Data Inspector session
file. Adding data from a native MLDATX file format speeds up loading time and allows
you to selectively load individual signals from large data sets.

### R2023a: Export data from the Playback block

You can aggregate data that has been added to the Playback block from different
sources (linked to from the source or saved in the model) and export that data to
the workspace or a file.

## Description

Load data from workspace, file, or Simulation Data Inspector

Use the Playback block to load input data for simulation. The
Playback block supports loading real or complex signals with fixed or
variable dimensions, discrete and continuous signals, and messages. Using the
Playback block, you can load data from:

- Workspace variables of any data format supported by the Simulation Data
  Inspector
- Files in the same formats supported by the Record block and the Simulation
  Data Inspector such as MAT, MLDATX *(since R2023a)*, and
  Microsoft®
  Excel® files
- Data from a custom file reader
- Runs in the Simulation Data Inspector

For more information about workspace variables and file formats supported
by the Playback block, see Import Data from Workspace or File into Simulation Data Inspector.

You can also use the Playback block in conjunction with the Record block as part of
a record and playback workflow. Use the Record block to record data from
physical devices or simulations. Then, use the Playback block to load the
recorded data into a model. Using real or simulated data, you can then develop, test,
and optimize the model.

### Add Data to Playback Block

You can add signals, messages, multidimensional signals, buses, and arrays of buses to the
Playback block. To load data to a model using the
Playback block, first add data to the block. Then, select the
data to load by assigning signals or messages to ports. When you run a simulation,
the Playback block loads data into the model.

To add signals to the Playback block interactively, double-click the block.
When you double-click a Playback block that has no signals, the block
shows a screen with options to add data.

You can choose from three types of sources to add data to the Playback block:

- Add a workspace variable from the base workspace, model workspace, or
  mask workspace.
- Add data from a file. If the file is not on the MATLAB® path or in your current directory, you can click the
  folder icon to browse for your data.
- Add data from the workspace, a file, or the Simulation Data Inspector
  using the Add Signals dialog box.

Use the Add Signals dialog box to access more options for adding data from the workspace or
a file or to add data from the Simulation Data Inspector. You can also search for specific signals. *(since R2024a)* As you
type the signal name, the table of signals updates to display only the signal names
that contain your search term. You can also refine your search to exclude partial
matches, match specific capitalization, or use regular expressions to find signals
that follow a certain pattern.

When you add data from the workspace or a file, you can choose to reference the signals in
the source or save a copy of the signals in the model. Adding signal data from the
Simulation Data Inspector always saves a copy of the signals in the model.

Referencing the signal in the source links the signal in the
Playback block to the variable or file that contains the signal
data. If the data in the source variable or file changes, that change is reflected
in the data loaded by the Playback block. When linking data, only
metadata is stored on the block for each signal.

When you save a copy of the signals in the model, the Playback
block loads from the copied data. Changes made to the original data source variable
or file are not reflected in the Playback block output.

The Add Signals dialog box also allows you to choose whether to assign ports automatically
or manually. If you choose to manually assign ports, you can create ports using the
**Port Editor** and assign ports using the port column of the
signal table.

To add signals to the Playback block
programmatically, use the `Simulink.playback.createSignals` function to create a `Simulink.playback.Signal` object that contains the signals to add.
Then, use the `set_param` function to apply the
`Simulink.playback.Signal` object to the
**Signals** parameter of the Playback
block. *(since R2024a)*

For example, to add signals with the variable names `x1` and
`x2` from the workspace to the Playback
block:

1. Use the `Simulink.playback.createSignals` function to
   create a `Simulink.playback.Signal` object for the
   `x1` and `x2` signals. Specify the
   source of the data as the workspace, and list the variable names of the
   signals to be added.
2. Use the `set_param` function to set the
   `Simulink.playback.Signals` object as the value of the
   **Signals** parameter.

```
pbSig  = Simulink.playback.createSignals("workspace","Variables",["x1","x2"]);
set_param("PlaybackModel/Playback","Signals",pbSig);
```

### View Signals in Sparkline Visualization

After you add signal data, you can visualize the signals in the Playback
block to verify the data before loading it into your model.

By default, the Playback block plots your data using a sparkline plot. A
sparkline is created for each signal added to the Playback block. If
you add input data for a bus, a sparkline is created for each bus element.
Multidimensional signals must be converted to channels or frames to visualize the
data. Use the check boxes next to each signal name to control which signals are
plotted.

**Note**

You can select or clear the check boxes to change the appearance of the
sparklines visualization without affecting which signals the
Playback block loads into your model during simulation. To
control which signals are loaded to the model, use the port column in the table
of signals.

To change the appearance of the signal table, click
**Preferences**. In the Preferences dialog box, you can
choose which signal properties to display and how to group the data in the signal
table. You can group data by: *(since R2023b)*

- Hierarchy — Group data based on the data hierarchy.
- Source — Group data based on the origin of the
  data. *(since R2024b)*

  - File — Signals sourced and referenced from a file are
    collected in a group specified by the filename. If you add
    signals from multiple files, a group is created for each
    file.
  - Workspace — Signals sourced and referenced from the workspace
    are collected in a group named
    `Workspace`.
  - Saved in model — Signals that are saved to the model, such as
    signals sourced from the Simulation Data Inspector, are
    collected in a group named `Signals saved in
    model`.
- No grouping — Display a flat list of signals.

### View Signals in Data Table

*Since R2025a*

To view signals in a data table, on the **Simulation** tab, in the
**View** section, click **Show Table**. By
default, the Playback block creates a 2-by-1 layout with the sparklines
visualization in the upper subplot and the data table in the lower subplot. Toggle
which signals are plotted and appear in the table by selecting or clearing the check
box next to each signal name. The table displays all plotted signals with
color-coordinated columns. When you select a signal from the signal table or
sparkline visualization, the Playback block also highlights the corresponding column
in the data table.

A 2-by-1 layout in the Playback block showing a sparkline visualization in the upper subplot and a data table in the lower subplot.

You can change the position of the data table, use cursors to examine your data,
and configure how the data in the table is presented with respect to time. For more
information, see View Table of Data in Playback Block.

### View and Edit Signals and Ports

You can view and edit signal properties using the **Properties**
pane in the Playback block.

In the **Properties** pane, you can edit any row with a white background.
The number of editable fields depends on whether you choose to reference the signal
in the source or save a copy of the data in the model.

Port properties for the Playback block can be set separately from the signal
properties using the **Port Editor**.

Using the **Port Editor**, you can add ports, delete ports, and edit port
properties. You can also change port assignments using the **Port**
column of the signal table. By default, port properties are inherited from the
signal. However, you can set a port property independently of the signal property.
When compatible with the signal property, the port property determines the output of
the Playback block. For example, you can convert the units of a
signal with assigned measurement by setting the **Units** property
for that port to a different unit of measurement. When the signal units and port
units are compatible, the Playback block performs a unit conversion.

The Playback block supports multirate sample times, allowing you to set a
different sample time for each port. Port sample times can also be set separately
from the signal sample time.

### Export Data Added to Playback Block

*Since R2023a*

You can use the Playback block to aggregate data from the workspace, files,
and the Simulation Data Inspector (linked to from the source or saved in the model)
and export that data to the workspace or a file. The Playback block
exports all data added to the block, even signals that are not assigned to ports. To
export all data added to the Playback block:

1. On the **Simulation** tab, in the
   **Share** section, click
   **Export**.
2. Select **Base workspace** or
   **File** to export the data to the workspace or to
   a file. You can choose to export the data to the workspace or to a MAT,
   MLDATX, or Microsoft
   Excel file.
3. Click **Export**.

If you choose to export data to an MLDATX file, you can specify the name of the run using
the **Exported run name** text box.

If you choose to export data to an Excel file, click
**Options** to select meta data to export and specify how
time data is exported.
