---
type: simulink-block
title: 'Time Scope'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Scopes and Data Logging'
documentation_page: 'timescopeblock'
documentation_source_path: 'ref/timescopeblock.html'
language: en
---

# Time Scope

## Ports

### Input

### **Port\_1** — Signal or signals to visualize scalar | vector | matrix | array | bus | nonvirtual bus

Connect the signals you want to visualize. You can have up to 96 input ports. Input signals can have
these characteristics:

- **Type** — Continuous (sample-based) or discrete (sample-based and
  frame-based).
- **Data type** — Any data type that Simulink supports. See Data Types Supported by Simulink (Simulink).

  This block accepts fixed-point input, but converts it to
  `double` for display.
- **Dimension** — Scalar, one
  dimensional (vector), two dimensional (matrix), or multidimensional
  (array). Display multiple channels within one signal depending on
  the dimension. See Signal Dimensions (Simulink) and Determine Signal Dimensions (Simulink).

#### Input Limitations

- When the input is a constant signal, the scope plots a single
  point.
- The scope shows gaps in the display when the signal value is
  `NaN`.
- When you visualize multiple frame-based signals in the scope,
  some samples of signals with a frame size of 1 might not be
  displayed. To visualize these signals, move the signals with
  frame size of 1 to a separate scope.

#### Bus Support

You can connect nonvirtual bus and arrays of bus signals to a scope.
To display the bus signals, use normal or accelerator simulation mode.
The scope displays each bus element signal in the order the elements
appear in the bus, from the top to the bottom. Nested bus elements are
flattened.

To log nonvirtual bus signals with a scope, set the **Save
format** parameter to `Dataset`.
You can use any **Save format** to log virtual bus
signals.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
**Complex Number Support:** Yes

## Parameters

For information about how to configure the Scope and use the toolstrip,
see Configure Time Scope Block.

### Scope Tab

Scope tab of the Scope block and the Time Scope block.

#### Settings > General

### **Open at simulation start** — Specify when scope opens off (default for Scope) | on (default for Time Scope)

Select this parameter to open the scope when simulation starts.

#### Programmatic Use

See `OpenAtSimulationStart` (Simulink).

### **Display the full path** — Display block path on scope title bar off (default) | on

Select this parameter to display the block path in addition to the block
name.

### **Number of input ports** — Number of input ports on scope `1` (default) | positive integer in the range [1 96]

Specify the number of input ports on the scope as a positive integer in
the range [1 96].

#### Programmatic Use

See `NumInputPorts` (Simulink).

### **Display grid** — Dimensions of display grid [1, 1] (default) | two-element numeric vector

Specify the dimensions of the display grid as a two-element numeric vector
with each element greater than 0 and less than or equal to 16.

#### Programmatic Use

See `LayoutDimensions` (Simulink).

### **Input processing** — Sample- or frame-based processing `Elements as channels (sample based)` (default for Scope) | `Columns as channels (frame based)` (default for Time Scope)

Specify whether the block performs sample- or frame-based
processing.

- `Elements as channels (sample based)` ––
  Process each element of the input as an independent channel.
- `Columns as channels (frame based)` ––
  Process each column of the input as an independent channel.
  Frame-based processing is available only with discrete input
  signals.

When you change the setting of the
**Input processing** parameter, the scope clears the
signal data and the measurements data (if any). Rerun the simulation to plot
the signal data with the new setting. *(since R2025a)*

**Note**

Frame-based processing requires a DSP System Toolbox license. For more information, see Sample- and Frame-Based Concepts.

#### Programmatic Use

See `FrameBasedProcessing` (Simulink).

### **Maximize axes** — Maximize size of plots `Off` (default for Scope) | `Auto` (default for Time Scope) | `On`

- `Auto` –– If **Title**
  and **Y-axis label** properties are not specified,
  maximize all plots.
- `On` –– Maximize all plots. Values in
  **Title** and **Y-axis label**
  are hidden.
- `Off` –– Do not maximize plots.

#### Programmatic Use

See `MaximizeAxes` (Simulink).

#### Settings > Time

### **Sample time** — Simulation interval between scope updates `-1` (for inherited) (default) | positive real number

Specify the time interval between updates of the scope display.
This property does not apply to floating scopes and scope
viewers. For a more detailed explanation of sample time with the scope, see
Sample Time with Scope Blocks (Simulink).

#### Programmatic Use

See `SampleTime` (Simulink).

### **Time span** — Length of *x*-axis to display `Auto` (default) | `One frame period` | `<user-defined>`

Specify the length of the *x*-axis to display as one of
these:

- `Auto` — Difference between the
  simulation start and stop times.

  The block calculates the beginning and end times of the time range
  using the **Time display offset** and
  **Time span** parameters. For example, if you
  set the **Time display offset** to
  `10` and the **Time span**
  to `20`, the scope sets the time range from
  `10` to `30`.
- `One frame period` — Use the frame period
  of the input signal to the Time
  Scope block. This option is available only when you set the
  **Input processing** parameter to
  `Columns as channels (frame
  based)`.
- `<user-defined>` — Enter any value
  less than the total simulation time.

#### Programmatic Use

See `TimeSpan` (Simulink).

### **Overrun action** — Display data beyond visible *x*-axis `Wrap` (default) | `Scroll`

Specify how to display data beyond the visible *x*-axis
range.

You can see the effects of this option only when plotting is slow with
large models or small step sizes.

- `Wrap` — Draw a full screen of data from
  left to right, clear the screen, and then restart drawing the data
  from the left.
- `Scroll` — Move data to the left as new
  data is drawn on the right. This mode is graphically intensive and
  can affect run-time performance.

#### Programmatic Use

See `TimeSpanOverrunAction` (Simulink).

### **Time units** — *x*-axis units `None` (default for Scope) | `Metric (based on Time Span)` (default for Time Scope) | `Seconds`

Specify the *x*-axis units as one of these
options:

- `Metric (based on Time Span)` — Display
  time units based on the length of **Time
  span**.
- `Seconds` — Display time in
  seconds.
- `None` — Do not display time
  units.

#### Programmatic Use

See `TimeUnits` (Simulink).

### **Time display offset** — *x*-axis offset `0` (default) | scalar | vector

Offset the *x*-axis by a specified time value, specified
as a real number or a vector of real numbers.

For input signals with multiple channels, you can enter a scalar or
vector:

- Scalar — Offset all channels of an input signal by the same time
  value.
- Vector — Independently offset the channels.

#### Programmatic Use

See `TimeDisplayOffset` (Simulink).

### **T-axis and ticks labels** — Display of *x*-axis (time) and tick labels `Bottom displays only` (default for Scope) | `All` (default for Time Scope) | `None`

Specify how the *x*-axis (time) and tick labels display:

- `All` — Display
  *x*-axis labels on all
  *y*-axes.
- `None` — Do not display labels.
  Selecting `None` also clears the
  **Show time-axis label** parameter.
- `Bottom displays only` — Display
  *x*-axis label on the bottom
  *y*-axis.

#### Dependencies

To enable this parameter:

- Select **Show time-axis label**.
- Set **Maximize axes** to
  `Off`.

#### Programmatic Use

See `TimeAxisLabels` (Simulink).

### **Time offset view** — Show time offset on status bar on (default) | off

Select this parameter to show the time offset on the status bar.

### **Show time-axis label** — Display or hide *x*-axis labels off (default for Scope) | on (default for Time Scope)

Select this parameter to show the *x*-axis label for the
active display.

#### Dependencies

To enable this parameter, set **T-axis and ticks
labels** to `All` or
`Bottom displays only`.

#### Programmatic Use

See `ShowTimeAxisLabel` (Simulink).

#### Settings > Axes Scaling

### **Scale Y-axis limits** — *y*-axis scaling mode `Manual` (default) | `Auto` | `After N Updates`

Specify the *y*-axis scaling mode as one of these:

- `Manual` — Manually scale the
  *y*-axis range.
- `Auto` — Scale the
  *y*-axis range during and after simulation.
  Selecting this option displays the **Y-axis limits do not
  shrink** parameter. If you want the y-axis range to
  increase and decrease with the maximum value of a signal, set
  **Scale Y-axis limits** to
  `Auto` and clear the **Y axis
  limits do not shrink** parameter.
- `After N Updates` — Scale
  *y*-axis after the number of time steps
  specified in the **Number of updates** parameter
  (`10` by default). Scaling occurs only once
  during each run.

#### Programmatic Use

See `AxesScaling` (Simulink).

### **Y-axis limits do not shrink** — Allow *y*-axis range limits to increase on (default) | off

Select this parameter to allow *y*-axis range limits to
increase during simulation.

#### Dependencies

To use this parameter, set **Scale Y-axis limits** to
`Auto`.

### **Number of updates** — Number of updates before scaling `10` (default) | integer

Set this property to delay auto scaling the
*y*-axis.

#### Dependencies

To use this parameter, set **Scale Y-axis limits** to
`After N Updates`.

#### Programmatic Use

See `AxesScalingNumUpdates` (Simulink).

### **Scale Y-axis limits at stop** — Scale *y*-axis limits when simulation stops on (default) | off

When you select this parameter, the scope scales the
*y*-axis limits only when the simulation stops. When you
clear this parameter, the scope scales the *y*-axis limits
continuously.

### **Y-axis data range (%)** — Percent of *y*-axis to use for plotting `80` (default) | integer between [1,100]

Specify the percentage of the *y*-axis range used for
plotting data. If you set this parameter to `100`, the
plotted data uses the entire *y*-axis range.

### **Y-axis align** — Alignment along *y*-axis `Center` (default) | `Top` | `Bottom`

Specify where to align plotted data along the *y*-axis
data range when **Y-axis data range (%)** is set to less
than 100 percent.

- `Top` — Align signals with the
  maximum values of the *y*-axis range.
- `Center` — Center signals between the
  minimum and maximum values.
- `Bottom` — Align signals with the
  minimum values of the *y*-axis range.

### **Scale X-axis limits** — Scale *x*-axis range limits off (default) | on

Scale *x*-axis range to fit all signal values. If
**Scale Y-axis limits** is set to
`Auto`, the data currently within the axes is scaled,
not the entire signal in the data buffer.

### **X-axis data range (%)** — Percent of *x*-axis to use for plotting `100` (default) | integer in the range [1,100]

Specify the percentage of the *x*-axis range to plot data
on. For example, if you set this parameter to `100`,
plotted data uses the entire *x*-axis range.

#### Dependencies

To enable this parameter, select **Scale X-axis
limits**.

### **X-axis align** — Alignment along *x*-axis `Center` (default) | `Left` | `Right`

Specify where to align plotted data along the *x*-axis
data range when **X-axis data range (%)** is set to less
than 100 percent.

- `Right` — Align signals with the maximum
  values of the *x*-axis range.
- `Center` — Center signals between the
  minimum and maximum values.
- `Left` — Align signals with the minimum
  values of the *x*-axis range.

#### Dependencies

To enable this parameter, select **Scale X-axis
limits**.

#### Settings > Logging

### **Limit data points to last**, **Limit frames to last** — Limit buffered data points or frames `off` (default) | `on`

Select this property to limit data saved by the scope internally. When you
select this property and set the **Input processing**
parameter to:

- `Elements as channels (sample based)`
  –– The scope saves the last *n* data points to
  a MATLAB® variable specified in **Variable
  name**. In this setting, the name of this property
  is **Limit data points to last**.
- `Columns as channels (frame based)`
  –– The scope saves the last *n* data frames to
  a MATLAB variable specified in **Variable
  name**. In this setting, the name of this property
  is **Limit frames to last**.

*n* is the scalar value you specify in the **Max
points** parameter.

When you select this parameter, the scope can plot signals for less than
the entire time range of a simulation, for example, if the sample time is
small. If the scope plots only a portion of the signal, consider increasing
the number of data points to save.

When you clear this property, the scope saves all the data. You can
visualize the entire data in the scope after the simulation finishes. For
simulations with **Stop Time** set to
`inf`, consider selecting this property.

**Note**

If you do not select this property and you have a high sample rate
or long simulation time, you can run into issues with memory or
system performance.

#### Programmatic Use

See `DataLoggingLimitDataPoints` (Simulink).

### **Max points** — Maximum number of data points to save `5000` | positive integer

Specify the maximum number of data points *n* to save as
a positive integer. The scope saves the last *n* data
points to a MATLAB variable specified in **Variable
name**.

#### Dependencies

To enable this parameter, select the **Limit data points to
last** or the **Limit frames to last**
parameter.

#### Programmatic Use

See `DataLoggingMaxPoints` (Simulink).

### **Decimation**, **Decimate frames** — Reduce amount of scope data to display and save `off` (default) | `on`

Select this property to plot and log (save) scope data every
*N*th data point or frame, where *N*
is the decimation factor you specify in the **Decimation
value** parameter.

When you select this property and specify a scalar value in the
**Decimation value** parameter, the scope limits the
data values plotted and saved to a MATLAB variable specified in **Variable
name**.

When you set the **Input processing** parameter to:

- `Elements as channels (sample based)`
  –– The scope plots and logs data every *N*th
  data point. The name of this property is
  **Decimation**.
- `Columns as channels (frame based)`
  –– The scope plots and logs data every *N*th
  frame. The name of this property is **Decimate
  frames**.

When you clear this property, the scope saves all the scope data.

#### Programmatic Use

See `DataLoggingDecimateData` (Simulink) and `DataLoggingDecimation` (Simulink).

### **Decimation value** — Decimation value `2` (default) | positive integer

Specify the scope to save or log data every *N*th data
point or frame, where *N* is the value you specify in this
parameter.

A value of `1` buffers all the data values.

#### Dependencies

To enable this parameter, select **Decimation** or
**Decimate frames**.

#### Programmatic Use

See `DataLoggingDecimateData` (Simulink) and `DataLoggingDecimation` (Simulink).

### **Log data to workspace** — Save data to MATLAB workspace `off` (default) | `on`

Select this parameter to enable logging and to save the logged data to the
MATLAB workspace. When you select this parameter, the scope enables
the **Variable name** and **Save format**
parameters as well. This parameter does not apply to floating scopes and
scope viewers.

For an example of saving signals to
the MATLAB Workspace using a Scope block, see Save Simulation Data Using Scope Block (Simulink).

#### Programmatic Use

See `DataLogging` (Simulink).

### **Variable name** — Name of saved data variable `ScopeData` (default) | character vector | string scalar

Specify a variable name for saving scope data in the MATLAB workspace. This parameter does not apply to floating scopes
and scope viewers.

#### Dependencies

To enable this parameter, select **Log data to
workspace**.

#### Programmatic Use

See `DataLoggingVariableName` (Simulink).

### **Save format** — MATLAB variable format `Dataset` (default) | `Structure With Time` | `Structure` | `Array`

Select the MATLAB variable format for saving data to the MATLAB workspace. This parameter does not apply to floating scopes
and scope viewers.

- `Dataset` — Save data as a `Dataset` (Simulink) object,
  by default a `timeseries` object.
- `Structure With Time` — Save data as
  a structure with associated time information.
- `Structure` — Save data as a
  structure.
- `Array` — Save data as an array with
  associated time information. This format does not support
  variable-size data.

#### Dependencies

To enable this parameter, select **Log data to
workspace**.

#### Programmatic Use

See `DataLoggingSaveFormat` (Simulink).

#### Settings > Axes Style

### **Plot type** — Type of plot `Auto` (default for Scope) | `Line` (default for Time Scope) | `Stairs` | `Stem`

Specify the type of the plot as one of these:

- `Auto` –– The plot type is a line
  graph for continuous signals, a stair-step graph for discrete
  signals, and a stem graph for Simulink message signals.
- `Line` –– Line graph.
- `Stairs` –– Stair-step graph. A
  stair-step graph is made up of only horizontal and vertical
  lines. Each horizontal line represents the signal value for a
  discrete sample period and is connected to two vertical lines.
  Each vertical line represents the change in the signal value
  occurring at a specific sample time.
- `Stem` –– Stem graph displayed as
  circles at the input value with vertical lines to the
  *x*-axis.

### **Axes background** — Background color for individual displays black (default) | color

Select the background color for the scope display.

### **Axes and grid** — Axes, grid, and label color for individual displays gray (default) | color

Select the axes, grid, and label color for individual displays.

### **Scope background** — Background color for scope window black (default) | color

Select the background color for the scope window.

### **Preserve colors for copy** — Preserve colors when copying scope off (default) | on

Select this parameter to preserve colors when copying the scope display to
the clipboard. When you do not select this parameter, the scope changes the
color of the scope to be printer friendly (white background, visible lines).
To preserve the existing colors on the scope while copying, select this
parameter.

#### Settings > Display Properties

### **Active Display** — Active display `1` (default) | positive integer

Select the display which updates based on the settings in the
**Display Properties** > **Line
Style**, **Y-axis**, and
**Display**.

Specify the desired display using a positive integer that corresponds to
the column-wise placement index. For layouts with multiple columns and rows,
display numbers are mapped down and then across.

#### Dependencies

To enable this parameter, set the display grid to have more than one
display, that is, set **Display grid** under
**Settings** > **General** to a
two-element numeric vector with at least one of the values greater than
1.

#### Programmatic Use

See `ActiveDisplay` (Simulink).

**Note**

All the **Line Style** properties affect only the active display
that you select through the **Active Display** parameter.

#### Settings > Line Style

### **Line** — Line to change `Channel 1` (default) | channel name

Select the active line for setting line style properties.

### **Style** — Line style `-` (default) | `:` | `-`. | `--` | `None`

Select the line style for the active line that you select using the
**Line** parameter.

### **Width** — Line width `1.5` (default) | `0.5` | `1` | `2` | `3` | `4` | `6` | ...

Specify the line width for the active line that you select using the
**Line** parameter.

### **Marker** — Data point marker style `none` (default) | `o` | `+` | `x` | ...

Specify a data point marker for the active line that you select using the
**Line** parameter. This parameter is similar to the
`'Marker'` property for plots. You can choose any of the
marker symbols from the drop-down list.

### **Color** — Line color yellow (default) | color picker

Specify the line color for the active line that you select using the
**Line** parameter.

**Tunable:** Yes

### **Line visible** — Line visibility on (default) | off

Show or hide a signal on the plot.

Select this parameter to display signal on the plot. If you clear this
parameter, the signal you select is no longer visible.

**Note**

All the **Y-axis** properties affect only the active display that
you select through the **Active Display** parameter.

#### Settings > Y-axis

### **Y-axis label** — Y-axis label none (default for Scope) | `Amplitude` (default for Time Scope) | character vector | string scalar

Specify the text to display on the *y*-axis. To display
signal units, add `(%<SignalUnits>)` to the label. At
the beginning of a simulation, Simulink replaces `(%SignalUnits)` with the units
associated with the signals.

**Example:** For a velocity signal with units of `m/s`, enter
`Velocity (%<SignalUnits>)`.

#### Dependencies

If you select the **Plot as magnitude-phase**
parameter under **Display** settings, this parameter
does not apply. The *y*-axes are labeled
`Magnitude` and `Phase`.

#### Programmatic Use

See `YLabel` (Simulink).

### **Y-axis limits** — Y-axis limits [`-10` `10`] (default) | two-element numeric vector

Specify the *y*-axis limits as a two-element numeric
vector.

**Tunable:** Yes

#### Dependencies

If you select **Plot as magnitude-phase**, this
property only applies to the magnitude plot. The
*y*-axis limits of the phase plot are always
`[-180 180]`.

#### Programmatic Use

See `YLimits` (Simulink).

**Note**

All the **Display** properties affect only the active display
that you select through the **Active Display** parameter.

#### Settings > Display

### **Title** — Display name `%<SignalLabel>` (default) | character vector | string scalar

Specify the title for the display. The default value
`%<SignalLabel>` uses the input signal name for
the title.

#### Programmatic Use

See `Title` (Simulink).

### **Show legend** — Display signal legend off (default) | on

Select this parameter to display the signal legend. The names listed in
the legend are the signal names from the model. For signals with multiple
channels, the scope appends a channel index after the signal name.
Continuous signals have straight lines before their names, and discrete
signals have step-shaped lines.

From the legend, you can control which signals are visible. This control
is equivalent to changing the visibility in the **Line
Style** properties. In the scope legend, click a signal name to
hide the signal in the scope. To show the signal, click the signal name
again. To show only one signal, right-click the signal name, which hides all
other signals. To show all signals, press **Esc**.

**Note**

The legend only shows the first 20 signals. Any additional signals
cannot be controlled from the legend.

#### Programmatic Use

See `ShowLegend` (Simulink).

### **Show grid** — Show internal grid lines on (default) | off

Select this parameter to show internal grid lines.

#### Programmatic Use

See `ShowGrid` (Simulink).

### **Plot as magnitude-phase** — Split display into magnitude and phase plots off (default) | on

Select this parameter to split the display into magnitude and phase
plots.

- On — Display magnitude and phase plots. If the signal is real, the
  scope plots the absolute value of the signal for the magnitude. The
  phase is 0 degrees for positive values and 180 degrees for negative
  values. This feature is useful for complex-valued input signals. If
  the input is a real-valued signal, selecting this parameter returns
  the absolute value of the signal for the magnitude.
- Off — Display signal plot. If the signal is complex, the scope
  plots the real and imaginary parts on the same
  *y*-axis.

#### Programmatic Use

See `PlotAsMagnitudePhase` (Simulink).

#### Display Grid

### **Display Grid** — Display layout 1-by-1 display (default) | an arrangement of `m`-by-`n` axes

Specify the layout of the displays. Opens a grid picker similar to the
scope layout. The layout can have a maximum of 16 rows and 16 columns. Using
the grid picker, you can select a layout of size up to 5-by-5. To select a
layout of size greater than 5-by-5:

- Set **Display grid** under
  **Settings** >
  **General** in the
  **Scope** tab of the toolstrip to a
  two-element numeric vector with each element greater than 0 and
  less than or equal to 16. For example, setting **Display
  grid** to [`2`
  `1`] changes the layout to 2-by-1.
- Use the `LayoutDimensions` property of the
  `TimeScopeConfiguration` (Simulink) object.

Animated GIF of changing the layout from one display to two displays

If the number of displays is equal to the number of ports, signals from
each port appear on separate displays. If the number of displays is less
than the number of ports, signals from additional ports appear on the last
display. For layouts with multiple columns and rows, ports are mapped down
then across. If the number of displays is greater than the number of ports,
the scope creates empty tiles.

#### Programmatic Use

See `LayoutDimensions` (Simulink).

#### Dock

### **Dock** — Dock the scope into scope container **Dock Scope** (default) | **Dock All Scopes**

Click **Dock** or **Dock Scope** in the
**Scope** tab to add the currently active scope to the
scope container. Click **Dock All Scopes** to add all the
opened scopes in the current model to the scope container.

For more information on the scope container, see Scope Window Management.

### **Undock** — Undock the scope from the scope container **Undock** (default) | **Undock All**

Click **Undock** in the **Home** tab of
the scope container to remove the currently active scope from the container
into a separate stand-alone window. Click **Undock All** to
remove all scopes from the container into separate stand-alone
windows.

For more information on the scope container, see Scope Window Management.

#### Dependencies

This parameter is available only on the **Home** tab
of the scope container.

### **Dock New Scopes on Open** — Add new scopes to the container on open off (default) | on

Select this parameter to add the newly opened scopes (which have not been
opened before in the current session of MATLAB) automatically to the existing scope container.

For more information on the scope container, see Scope Window Management.

#### Dependencies

This parameter is available only on the **Home** tab
of the scope container. To access this parameter, click the drop down
arrow of **Dock All** under the
**Home** tab of the scope container.

### Measurements Tab

The **Measurements** tab contains the settings for all the signal
measurements that the scope supports. The measurement panels appear at the bottom of the
scope window. To open a measurement panel, you must first enable the corresponding
measurement in the **Measurements** tab.

Measurements tab of the Scope block and the Time Scope block.

For more information on the measurements, see these pages:

- Triggers — Set triggers to sync repeating signals and pause the
  display when events occur.
- Cursor Measurements — Measure signal values using vertical and
  horizontal cursors.
- Signal Statistics — Display the maximum, minimum, peak-to-peak
  difference, mean, median, and RMS values of a selected signal.
- Peak Finder — Find maxima, showing the *x*-axis
  values at which they occur.
- Bilevel Measurements — Measure transitions, overshoots, undershoots, and
  cycles.

## Libraries

DSP System Toolbox / Sinks DSP System Toolbox HDL Support / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `busa` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Virtual bus not supported. Nonvirtual bus supported only in normal and accelerator mode simulation. Data logging for nonvirtual bus supported only in the dataset format. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block can be used for simulation visibility in systems that generate code, but is not
included in the generated code.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

This block can be used for simulation visibility in subsystems
that generate HDL code, but is not included in the hardware implementation.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

This block can be used for simulation visibility in systems that generate code, but is not
included in the generated code.

## Version History

**Introduced in R2015b**

### R2025a: Improved Scope and new scope container to dock all scopes in one window

The Simulink
Scope (Simulink), Time Scope, and Floating Scope and Scope Viewer (Simulink) blocks in Simulink have a new user interface that you can use to access settings and measurements
of the scope. The scope is now more responsive and its performance is improved. Use the new
scope container to dock multiple scope windows into a single window and to manage and
organize the scopes. The scope container also enables you to view all the scopes in the
model in a single window.

Key improvements to the Scope, Time Scope, and
Floating Scope and Scope Viewer blocks are:

- Streamlined user interface: Easy access to all the general scope settings from
  the **Scope** tab and all the measurement settings from the
  **Measurements** tab of the new scope toolstrip.
- New scope container: A single window providing a unified view for all the
  scope displays in the model, enabling you to manage and organize multiple scopes
  in one place.
- Updated settings panel: Updated panel consolidates all general and style
  settings of the scope. To open the panel, click **Settings** in
  the **Scope** tab of the toolstrip.

### R2025a: Access to Time Scope through MATLAB Graphics API has been removed

The underlying graphics of the Time Scope block have changed. You
cannot access or modify the Time Scope block through the MATLAB Graphics API.

To display the scope data in a MATLAB Graphics window, use the **Print to Figure**
functionality in the **Scope** tab of the Time Scope
block toolstrip.

### R2025a: Ability to dock Scopes to MATLAB desktop has been removed

The ability to dock the Simulink
Scope (Simulink), Time Scope, and Floating Scope and Scope Viewer (Simulink) to the MATLAB desktop has been removed. Use the new scope container instead. For more
information, see Scope Window Management.

If you have a model created in R2024b or a previous release with four or more open scopes,
and you open that model in R2025a, the opened scopes automatically dock in the scope
container window.

## Description

Display and analyze signals generated during simulation and log signal data to MATLAB

The Simulink®
Scope block and DSP System Toolbox™
Time Scope block display time domain signals.

The two blocks have identical
functionality, but different default settings. The Time Scope is optimized for discrete time processing.
The Scope is optimized for general time-domain simulation. For a side-by-side comparison, see Simulink Scope Block Versus DSP System Toolbox Time Scope Block (Simulink).

**Scope Tab**

This screenshot highlights the important aspects of the scope window.

**Scope display features:**

- Simulation control — Run and debug models from a Scope window using
  **Run**, **Step Forward**, and
  **Step Backward** toolbar buttons.
- Multiple signals — Plot multiple signals on the same display using multiple
  input
  ports.
- Multiple displays — Display signals on multiple subplots. All the
  *y*-axes of the subplots have a common time range on the
  *x*-axis. Control the layout of the subplots using the
  **Display Grid** parameter in the
  **Scope** tab of the toolstrip.
- Modify parameters — Modify scope parameter values before and during a
  simulation.
- Axis autoscaling — Autoscale axes during or at the end of a simulation.
  Margins are drawn at the top and bottom of the axes.
- Display data after simulation — Scope data is saved during a simulation. If a
  scope is closed at the start of a simulation, when you open the scope after a
  simulation, the scope displays simulation results for attached input signals.

  **Note**

  If you have a high sample rate or long simulation time, you may run
  into issues with memory or system performance because the scope saves
  data internally. To limit the amount of data saved for scope
  visualization, use the `Limit data points to last`
  property.
- Scope window management –– The scope container enables you to dock multiple
  scopes of the Simulink model into a single window. The container provides a convenient
  interface from which you can visualize the signals and manage the settings of
  the scopes.

**Measurements Tab**

This screenshot highlights the important aspects of the measurements window.

Here is a list of all the measurements the Time
Scope block supports:

- Triggers —
  Set triggers to sync repeating signals and pause the display when events
  occur.
- Cursor Measurements — Measure signal values using vertical and horizontal
  cursors.
- Signal Statistics — Display the maximum, minimum, peak-to-peak difference,
  mean, median, and RMS values of a selected signal.
- Peak Finder — Find maxima, showing the *x*-axis values at
  which they occur.
- Bilevel Measurements — Measure transitions, overshoots, undershoots, and
  cycles.

You must have a Simscape™ or DSP System Toolbox license to use the Peak Finder, Bilevel Measurements, and Signal
Statistics.

For information on controlling a
scope programmatically, see Control Scope Blocks Programmatically (Simulink).
