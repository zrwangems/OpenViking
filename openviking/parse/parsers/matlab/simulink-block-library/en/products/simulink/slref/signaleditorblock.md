---
type: simulink-block
title: 'Signal Editor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Sources'
documentation_page: 'signaleditorblock'
documentation_source_path: 'slref/signaleditorblock.html'
language: en
---

# Signal Editor

## Ports

### Output Arguments

### **Signal1** — Signals in scenario scalar | vector | matrix | array

One or more signals, returned as a scalar, vector, matrix, array, a
bus, or an array of buses *(since R2021a)*. The
block creates one port per signal.

The port label depends on the associated variable in the data set MAT
file.

In rapid accelerator mode, the Signal Editor block does
not support `int64` and `uint64` data
types when the **Interpolate data** parameter is
selected. For more information, see Array of buses support.

**Data Types:** `single` | `double` | `half` | `int` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **To create and edit scenarios, open Signal Editor user interface** — Option to open Signal Editor tool button

To open the Signal Editor, click **Open Signal
Editor** (). The Signal Editor opens
with all the active scenario signals plotted.

To see the signal data changes from the Signal Editor tool,
click the **Save** button in the Signal Editor
tool toolstrip.

#### Programmatic Use

To open the Signal Editor, use the `signalEditor`
function. For more information. see Signal Editor.

### **File name** — Data set file `untitled.mat` (default) | character vector

Data set file, specified as character vector, containing one or more
scalar `Simulink.SimulationData.Dataset` objects. Do not use
a filename from one locale in a different locale. When using the block on
multiple platforms, consider specifying just the MAT filename and having the
MAT file be on the MATLAB path.

To create a MAT file, click . This button opens the Signal
Editor, which lets you create and edit scenario MAT files.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Filename` |
| **Type**: character vector |
| **Values**: character vector |
| **Default**: `'untitled.mat'` |

### **Active scenario** — Active scenario `Scenario` (default) | character vector

Active scenario, specified as a character vector. You can switch the
active scenario as necessary.

If you create this block by using the
`signalBuilderToSignalEditor` function or the
Check model for Signal Builder blocks Upgrade
Advisor check to convert a Signal Builder block to a
Signal Editor block, the active scenario name is the data
set variable name in the MAT file. However, if you pause on this parameter,
the original Signal Builder group name is displayed.

#### Dependencies

To enable this parameter, ensure that the specified MAT file
exists.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ActiveScenario` |
| **Type**: character vector | numeric |
| **Values**: character vector | index value |
| **Default**: `'Scenario'` |

### **Use properties from** — Signal property source `Dialog parameters` (default) | `Signal data in MAT file`

Signal property source, specified as:

- `Dialog parameters` — Use signal
  properties from the block dialog.
- `Signal data in MAT file` — Use signal
  properties from the MAT file specified in **File
  name**. If the signal does not have unit or
  interpolation properties, the signal property defaults to the
  Signal Editor block dialog setting. These
  properties include:

  - **Unit**
  - **Interpolate data**

#### Dependencies

To enable this parameter, ensure that the specified MAT file
exists.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `'SignalPropertySource'` |
| **Type**: character vector |
| **Values**: `Dialog parameters` | `Signal data in MAT file` |
| **Default**: `'SignalPropertySource'` |

### **Active signal** — Signal to configure `Signal 1` (default) | character vector

Signal to configure, specified as a signal name. This signal is considered
the active signal.

#### Dependencies

To enable this parameter, ensure that the specified MAT file
exists.

This parameter has no effect when the **Apply signal
properties to all signals** parameter is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ActiveSignal` |
| **Type**: character vector | numeric |
| **Values**: character vector | index vector |
| **Default**: `'Signal 1'` |

Do not use the `set_param` function to set
`ActiveSignal` in combination with another
name-value argument of the Signal Editor block.

### **Apply signal properties to all scenarios** — Option to apply specified signal properties to active signal `on` (default) | `off`

Option to apply the specified signal properties.

- `on` — Apply the specified signal properties to
  the active signal in all scenarios.
- `off` — Apply signal properties only in the
  current active scenario.

#### Dependencies

- To enable this parameter, set the **Use properties
  from** parameter to `Dialog
  parameters`.
- If the **Apply signal properties to all
  signals** parameter is also selected, the block
  applies the signal properties to all signals in all
  scenarios.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ApplySigPropsToAllScenarios` |
| **Type**: character vector |
| **Values**: `'off' | 'on'` |
| **Default**: `'on'` |

### **Apply signal properties to all signals** — Option to apply signal properties to all signals `off` (default) | `on`

Option to apply the specified signal properties.

- `on` — Apply the specified signal properties
  to all the signals in the active scenario. There is no concept
  of an active signal.
- `off` — Do not apply signal property to all
  signals.

#### Dependencies

- To enable this parameter, set the **Use properties
  from** parameter to `Dialog
  parameters`.
- If the **Apply signal properties to all
  scenarios** parameter is also selected, the block
  applies the signal properties to all signals in all
  scenarios.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ApplySigPropsToAllSignals` |
| **Type**: character vector |
| **Values**: `'off' | 'on'` |
| **Default**: `'off'` |

### **Output a bus signal** — Configure signal as bus `off` (default) | `on`

To configure a signal as a bus, select this parameter.

Select this parameter only if the active signal is a MATLAB structure whose fields are the same as an existing bus object,
or create a new matching bus object. If you select this parameter for an
active signal that is not a MATLAB structure, simulation returns an error.

#### Dependencies

To enable this parameter, ensure that the specified MAT file
exists.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IsBus` |
| **Type**: character vector |
| **Values**: `'off' | 'on'` |
| **Default**: `'off'` |

### **Select bus object** — Bus object `Bus: BusObject` (default) | bus object name

Select or enter the bus object name. To edit the bus object or create a
bus object using the Data Type Assistant, click **>>**. The
active signal must be a MATLAB structure whose fields are the same as this bus object.

#### Dependencies

To enable this parameter, select **Output a bus
signal**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputBusObjectStr` |
| **Type**: character vector |
| **Values**: bus object name |
| **Default**: `'Bus: BusObject'` |

### **Mode** — Bus object mode `Bus object` (default) | bus object data type

Specify the bus object name. If you do not have a bus object, create one
by clicking **Edit**, which opens the Type Editor. For more
information, see Create Simulink Bus Objects.

### **Unit** — Physical unit `inherit` (default) | supported physical unit

Physical unit of the signal, specified as an allowed unit. To specify a
unit, begin typing in the text box. As you type, the parameter displays
potential matching units. For more information, see Unit Specification in Simulink Models. For a list of supported units, see
Allowed Unit
Systems.

To constrain the unit system, click the link to the right of the
parameter:

- If a Unit System
  Configuration block exists in the component, its dialog
  box opens. Use that dialog box to specify allowed and disallowed
  unit systems for the component.
- If a Unit System Configuration block does not exist
  in the component, the model Configuration Parameters dialog box
  displays. Use that dialog box to specify allowed and disallowed unit
  systems for the model.

#### Dependencies

- To enable this parameter, set the **Use properties
  from** parameter to `Dialog
  parameters`.
- If the **Apply signal properties to all
  scenarios** parameter is also selected, the block
  applies the signal properties to all signals in all
  scenarios.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Unit` |
| **Type**: character vector |
| **Values**: `'inherit'` | supported physical unit |
| **Default**: `'inherit'` |

### **Sample time** — Time interval between samples `0` (default) | `-1` | sample time in seconds

Time interval between samples, specified in seconds.

#### Dependencies

To enable this parameter, ensure that the specified MAT file
exists.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Values**: `-1` | sample time in seconds |
| **Default**: `'0'` |

### **Interpolate data** — Linearly interpolate data `on` (default) | `off`

Linearly interpolate data at time hits for which no corresponding
workspace data exist.

- `on` — Linearly interpolate at time hits for
  which no corresponding workspace data exist.

  **Note**

  If the Signal Editor block is the source for a
  new Simulink®
  Test™ or Simulink
  Design Verifier™ test harness model, the **Interpolate
  data** parameter is off by default.
- `off` — The current output equals the output at
  the most recent time for which data exists.

The Signal Editor block interpolates by using the two
corresponding workspace samples.

- For `double` data, the Signal
  Editor block linearly interpolates the value by using
  the two corresponding samples.
- For `Boolean` data, the Signal
  Editor block uses `false` for the first
  half of the time between two time values and `true`
  for the second half.
- For a built-in data type other than `double` or
  `Boolean`, the Signal Editor
  block:

  - Upcasts the data to `double`
  - Performs linear interpolation (as described for
    `double` data)
  - Downcasts the interpolated value to the original data
    type

When you load enumerated, fixed-point, variable-size signal, or string
data, clear the **Interpolate data**
parameter.

The block uses the value of the last known data point as the value of time
hits that occur after the last known data point.

To determine the block output after the last time hit for which data is
available, combine the settings of these parameters:

- **Interpolate data**
- **Form output after final data value by**

For details, see **Form
output after final data value by**.

In rapid accelerator mode, the Signal Editor block does not
support `int64` and `uint64` data types
when the **Interpolate data** parameter is
selected.

#### Dependencies

- To enable this parameter, set the **Use properties
  from** parameter to `Dialog
  parameters`.
- If the **Apply signal properties to all
  scenarios** parameter is also selected, the block
  applies the signal properties to all signals in all
  scenarios.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Interpolate` |
| **Type**: character vector |
| **Values**: `'off' | 'on'` |
| **Default**: `'on'` |

### **Enable zero-crossing detection** — Detect zero-crossings `off` (default) | `on`

If you select **Enable zero-crossing detection**, the
Signal Editor block detects a zero crossing when the
input array contains multiple entries for the same time value. For example,
suppose that the block loads this input data.

```
time:     0 1 2 2 3
signal:   2 3 4 5 6
```

At time `2`, a zero crossing occurs because of the
discontinuity in the input data. For more information, see Zero-Crossing Detection.

When you load input data for a bus, the Signal Editor block
detects zero crossings for all leaf bus elements.

This block supports zero-crossing detection only in simulations
that use a variable-step solver. When you use a fixed-step solver for simulation, the software
does not detect or locate zero crossings for this block.

#### Dependencies

To enable this parameter, ensure that the specified MAT file
exists.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroCross` |
| **Type**: character vector |
| **Values**: `'off' | 'on'` |
| **Default**: `'off'` |

### **Form output after final data value by** — Block output after the last time hit for which data is available `Setting to zero` (default) | `Extrapolation` | `Holding final value`

To determine the block output after the last time hit for which workspace
data is available, combine the settings of these parameters:

- **Interpolate data**
- **Form output after final data value by**

This table lists the block output, based on the values of the two
options.

| Setting for Form Output After Final Data Value By | Setting for Interpolate Data | Block Output After Final Data |
| --- | --- | --- |
| `Extrapolation` | On | Extrapolated from final data value |
| Off | Error |
| `Setting to zero` | On | Zero |
| Off | Zero |
| `Holding final value` | On | Final value from workspace |
| Off | Final value from workspace |

For example, the block uses the last two known data points to extrapolate
data points that occur after the last known point if you:

- Select **Interpolate data**.
- Set **Form output after final data value by** to
  `Extrapolation`.

#### Dependencies

To enable this parameter, ensure that the specified MAT file
exists.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputAfterFinalValue` |
| **Type**: character vector |
| **Values**: `'Setting to zero' | 'Extrapolation' | 'Holding final value'` |
| **Default**: `'Setting to zero'` |

## Libraries

Simulink / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ has additional configuration options that affect HDL implementation
and synthesized logic.

You can generate code that has multiple test benches from your subsystem. To
generate multiple test benches:

- Create and edit multiple signals in multiple data sets by using the
  Signal Editor tool. By default, the Signal Editor creates `timeseries` data. For
  more information, see Create and Edit Signal Data.
- Set up a scenario in the Signal Editor block parameter
  dialog box by specifying the MAT file that contains the list of
  scenarios and selecting the **Active scenario** from
  the drop-down list.
- Generate the test bench by using the HDL Workflow Advisor. In the
  **HDL Code Generation** > **Generate RTL
  Code and Testbench** task, select **Generate RTL
  testbench** and click **Apply**.

**Limitations**

- Code generation does not support designs that use buses.
- Code generation does not support designs that include multiple
  Signal Editor blocks.
- Multi-file test cases and simulations support designs only if you
  connect all the input signals to the same Signal Editor
  block.

**Restrictions**

Connect the Signal Editor block to the DUT ports to use it as a
source block in your model, but ensure it is not placed inside the DUT
subsystem.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2017b**

### R2025a: Signal Editor block updates

Starting in R2025a, the Signal Editor block has these
updates:

- The **Interpolate data** parameter is now enabled by
  default.

  **Note**

  If the Signal Editor block is the source for a new
  Simulink
  Test or Simulink
  Design Verifier test harness model, the **Interpolate
  data** parameter is off by default.
- The new **Use properties from** lets you specify the
  source of signal property definitions.

### R2024b: Signal Editor block updates

The Signal
Editor block has these updates:

- When you open the Signal Editor tool from the Signal Editor
  block, the Signal Editor tool now opens with all the active
  scenario signals already plotted.
- The Signal Editor block supports loading input signal data values that have
  an `int64` or `uint64` data type. When you
  use the Signal Editor block to load `int64` or
  `uint64` signal data:

  - Only the signal values can have the `int64` or
    `uint64` data type. Time values must have
    `double` data type.
  - Use a format other than array, such as `timetable`,
    `timeseries`, or structure. Array format does not
    support any data type other than `double`.

  While loading `int64` and `uint64`
  signal data is supported in all simulation modes, interpolation of
  `int64` and `uint64` data is not
  supported in rapid accelerator simulations. To load `int64`
  or `uint64` data into a rapid accelerator
  simulation:

  1. Clear the **Interpolate data** parameter.
  2. Set the **Form output after final data value by**
     parameter to any value except
     `Extrapolation`.

### R2023b: Signal Editor block updates

The Signal Editor block dialog box has these updates:

- In the **Signal properties** section, the new
  **Apply signal properties to all signals** check box
  lets you apply the specified signal properties to all signals.
- When you pause on the **Active scenario** parameter, a
  tooltip displays the `Name` property of the data set
  object. If the block is converted from a Signal Builder block
  using the `signalBuilderToSignalEditor` function, the
  `Name` property is the same as the Signal
  Builder block **Group** name.

### R2023a: Signal Editor block updates

The Signal
Editor block dialog box has these updates:

- The **Launch Signal Editor** button has moved to the
  top of the block parameters dialog box.
- The **Signal properties** section is reorganized.
- In the **Signal properties** section, the new
  **Apply properties to active signal in all scenarios**
  check box lets you apply the specified signal properties to the active
  signal with the same name in all scenarios.

### R2021a: Array of buses support

The Signal Editor block supports loading data for an array of buses.
A Signal Editor block in the top model can load data for an array of
buses in normal or accelerator mode simulations. Loading data for an array of buses
using a Signal Editor block in a referenced model is supported only
when the referenced model executes in normal mode.

## Description

Display, create, edit, and switch interchangeable scenarios

The Signal Editor block displays, creates, and edits interchangeable
scenarios, which contain signals. Signals can be:

- MATLAB®
  `timeseries` objects.
  `timeseries` objects cannot have empty
  `Data` properties.
- `timetable` objects.
  `timetable` objects cannot represent multiple
  variables.
- Structure of MATLAB
  `timeseries` or `timetable` objects.
- Two-dimensional matrices.

The block creates one port for each signal.

To create and edit scenarios and the signals contained in the scenarios, click
**Open Signal Editor** (). You can also use the Signal Editor
block to switch scenarios in and out of models.

The Signal Editor block supports MAT files that contain signals as one
or more scalar `Simulink.SimulationData.Dataset` objects.

### Create and Edit Scenarios and Signals

To create and edit scenarios and the signals contained in them, open the Signal
Editor tool by clicking . The Signal Editor tool enables you to easily
manipulate signals in these ways:

- Create and edit multiple signals in multiple data sets. By default, the
  Signal Editor creates timeseries format data.
- Use signal notations to create more complicated signals using MATLAB expressions. You can use the Author and Insert dialog box or
  manually enter simple MATLAB expressions in the tabular area.
- Use existing scenarios to get existing data sets for which you can edit
  and create signals.
- Create and edit multidimensional signals.

For more information on the Signal Editor tool, see Create and Edit Signal Data.

### Programmatic Interactions

To programmatically get the total number of scenarios and signals in the
Signal Editor block, use the `get_param`
function with the `NumberOfScenarios` and
`NumberOfSignals` parameters, respectively. These read-only
parameters contain the values as character vectors. To convert these values to
doubles, use the `str2double` function.

To programmatically enable the Signal Editor block to label output
signal lines, set `PreserveSignalName` to `'on'`
(default) with the `set_param` function.

```
set_param(gcb,'PreserveSignalName','on')
```

For more information on programmatic interactions, see Parameters and Replace Programmatic Use of signalbuilder.

### Import and Export

The Signal Editor supports custom file types, such as Microsoft®
Excel®, by letting you:

- Edit signals imported from registered custom file types. For more
  information, see Import Custom File Type.
- Export signals from Signal Editor to your registered custom file types.
  For more information, see Export Signals to Custom Registered File Types.

### Migrating from Signal Builder Blocks

You can port Signal Builder block configurations to the
Signal Editor block using the
`signalBuilderToSignalEditor` function. For more information,
see Replace Signal Builder Block with Signal Editor Block and Migrate from Signal Builder Block to Signal Editor Block.

### Fast Restart

The Signal Editor block supports fast restart. With fast restart
enabled, you can still:

- Change the active scenario.
- Change the active signal.

  While you can change the active signal, you cannot edit the signal
  properties in the block.
- Open the Signal Editor and edit data.
