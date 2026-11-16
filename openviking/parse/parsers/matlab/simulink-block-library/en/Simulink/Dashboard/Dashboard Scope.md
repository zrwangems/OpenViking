---
type: simulink-block
title: 'Dashboard Scope'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Dashboard'
documentation_page: 'dashboardscope'
documentation_source_path: 'slref/dashboardscope.html'
language: en
---

# Dashboard Scope

## Ports

Not documented in R2025b.

## Parameters

### Connection Table

Use the **Connection** table to select one or more signals to
display and to configure the line style and color.

### **Connection** — Signals to connect and display signal connection options

Populate the **Connection** table by selecting
signals in the model. To connect a signal, select the check box next to
the signal you want to connect, then click **Apply**.
For more information about connecting dashboard blocks, see Connect Dashboard Blocks to Simulink Model.

#### Tips

You can connect signals to a Dashboard Scope block
during simulation.

#### Programmatic Use

To programmatically specify one or more signals to connect to the
Dashboard Scope block, use a cell array of
`Simulink.HMI.SignalSpecification` objects.

|  |
| --- |
| **Block Parameter:** `Binding` |
| **Type:** cell array of `Simulink.HMI.SignalSpecification` objects |
| **Default:** `[]` |

### **Line Style** — Line style and color for connected signals line style and color options

You can configure the line style and color for signals connected to a
Dashboard Scope block using the
**Connection** table. To change the line style or
color for a signal, in the **Style** column that
corresponds to the signal row, click the preview of the signal
appearance. When **Override style and color** is
cleared, the **Style** column displays the word
`auto` instead of a preview of the line style. For
more information, see Configure Signal Line Style and Color.

#### Programmatic Use

To programmatically configure the line style and color for
connected signals, use the `Colors` parameter.
Specify the value for the `Colors` parameter as an
array of structures where each structure specifies the style
override setting, line style, and line color for one signal.
Settings specified using the `Colors` parameter
apply to the signal at the same index in the value for the
`Binding` parameter.

Specify the line style and color for each signal as a structure
with these fields:

- `Auto` — Style override setting
  specified by:

  - `"on"` — Line style and
    color automatically set by the software
  - `"off"` — Line style and
    color specified by `Color` and
    `LineStyle`
- `Color` —
  `1`-by-`3`
  `[r g b]` vector with values between
  `0` and
  `1`.
- `LineStyle` — Character vector that
  specifies one of these line style options:

  - Solid: `'-'`
  - Dashed: `'––'`
  - Dotted: `':'`
  - Dash-dotted: `'-.'`

```
sigColors1.Color = '';
sigColors1.LineStyle = '';
sigColors1.Auto = "on";
sigColors2.Color = [0 0 1];
sigColors2.LineStyle = '--';
sigColors2.Auto = "off";
sigColors = [sigColors1 sigColors2];

set_param(blockPath,'Colors',sigColors);
```

|  |
| --- |
| **Block Parameter:** `Colors` |
| **Type:** array of structures |

### Main

### **Time Span** — Time axis span `auto` (default) | scalar

A finite, real, double, scalar value that sets the time span of the
plot.

When **Time Span** is set to `auto`,
the block sets its time span to the simulation stop time.

#### Tips

When you set the **Time Span** to a value that is
less than the duration of the simulation, use the **Update
Mode** parameter to control whether the display wraps
or scrolls when the simulation time exceeds the specified time
span.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TimeSpan` |
| **Type:** string | character array |
| **Values:** `'auto'` or numeric value |
| **Default:** `'auto'` |

### **Update Mode** — Display update behavior `Wrap` (default) | `Scroll`

How the display updates during simulation, specified as
`Wrap` or
`Scroll`.

- `Wrap` — Display wraps to show incoming
  data after simulation time reaches end of time span.
- `Scroll` — Display scrolls to show
  incoming data after simulation time reaches end of time
  span.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UpdateMode` |
| **Type:** string | character array |
| **Values:** `'Wrap'` | `'Scroll'` |
| **Default:** `'Wrap'` |

### **Min** — Vertical axis minimum `-3` (default) | scalar

A finite, real, double, scalar value that sets the minimum of the
vertical axis.

#### Tips

To maintain the minimum and maximum vertical axis limits set by
**Min** and **Max** after the
simulation stops, clear **Scale axes limits at
stop**.

#### Programmatic Use

To specify the `Min` parameter for the
Dashboard Scope block programmatically, create a
`1`-by-`2` vector that
contains the minimum *y*-axis value and maximum
*y*-axis value, in that order.

|  |
| --- |
| **Block Parameter:** `YLimits` |
| **Type:** `1x2` vector |
| **Default:** `[-3 3]` |

### **Max** — Vertical axis maximum `3` (default) | scalar

A finite, real, double, scalar value that sets the maximum of the
vertical axis.

#### Tips

To maintain the minimum and maximum vertical axis limits set by
**Min** and **Max** after the
simulation stops, clear **Scale axes limits at
stop**.

#### Programmatic Use

To specify the `Max` parameter for the
Dashboard Scope block programmatically, create a
`1`-by-`2` vector that
contains the minimum *y*-axis value and maximum
*y*-axis value, in that order.

|  |
| --- |
| **Block Parameter:** `YLimits` |
| **Type:** `1x2` vector |
| **Default:** `[-3 3]` |

### **Normalize y-axis limits** — Option to normalize *y*-axis `off` (default) | `on`

When enabled, the connected signal data is normalized to display on a
*y*-axis range of [`0,1`].

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NormalizeYAxis` |
| **Type:** string | character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **Scale axes limits at stop** — Option to perform fit-to-view upon simulation stop `on` (default) | `off`

When enabled, performs a fit-to-view operation on the data displayed
in the plot when the simulation stops.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ScaleAtStop` |
| **Type:** string | character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Show "Double-click to connect" message** — Connection instructions visibility `on` (default) | `off`

When enabled, shows instructional text if the block is not connected.
When the block is not connected, you can specify this parameter as
`off` to hide the text.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowInitialText` |
| **Type:** string | character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### Display

### **Ticks** — Axes tick positions `Outside` (default) | `Inside` | `None`

Axes tick positions, specified as `Outside`,
`Inside`, or
`None`.

- `Outside` — Ticks are drawn on
  the outside of the *x*- and
  *y*-axes.
- `Inside` — Ticks are drawn on the
  inside of the *x*- and
  *y*-axes.
- `None` — No ticks are shown on
  the *x*- or
  *y*-axes.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TicksPosition` |
| **Type:** string | character vector |
| **Values:** `'Outside'` | `'Inside'` | `'None'` |
| **Default:** `'Outside'` |

### **Tick Labels** — Tick label visibility `All` (default) | `T-Axis` | `Y-Axis` | `None`

Visibility of tick labels on the *x*- and
*y*-axes.

- `All` — Ticks labels are shown on
  the *x*- and
  *y*-axes.
- `T-Axis` — Tick labels are shown
  on the *x*-axis only.
- `Y-Axis` — Tick labels are shown
  on the *y*-axis only.
- `None` — No tick labels are shown
  on the *x*- or
  *y*-axis.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TickLabels` |
| **Type:** string | character vector |
| **Values:** `'All'` | `'T-Axis'` | `'Y-Axis'` | `'None'` |
| **Default:** `'All'` |

### **Legend** — Legend position `Top` (default) | `Right` | `Inside top` | `Inside right` | `Hide`

You can position the legend at the top of the plot inside or outside
the plot area or on the right of the plot inside or outside the plot
area. You can also hide the legend. The legend shows the color chosen
for each connected signal next to the signal name.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LegendPosition` |
| **Type:** string | character vector |
| **Values:** `'Top'` | `'Right'` | `'InsideTop'` | `'InsideRight` | `'Hide'` |
| **Default:** `'Top'` |

### **Horizontal** — Horizontal grid line visibility `on` (default) | `off`

Visibility of horizontal grid lines.

- `on` — Horizontal grid lines are
  visible on Dashboard Scope.
- `off` — Horizontal grid lines are
  not shown on Dashboard Scope.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Grid` |
| **Type:** string | character vector |
| **Values:** `'All'` | `'Horizontal'` | `'Vertical'` | `'None'` |
| **Default:** `'All'` |

### **Vertical** — Vertical grid line visibility `on` (default) | `off`

Visibility of vertical grid lines.

- `on` — Vertical grid lines are
  visible on Dashboard Scope.
- `off` — Vertical grid lines are
  not shown on Dashboard Scope.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Grid` |
| **Type:** string | character vector |
| **Values:** `'All'` | `'Horizontal'` | `'Vertical'` | `'None'` |
| **Default:** `'All'` |

### **Border** — Plot border visibility `on` (default) | `off`

Plot border visibility.

- `on` — Plot border is shown on
  Dashboard Scope.
- `off` — Plot border is not shown
  on Dashboard Scope.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Border` |
| **Type:** string | character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Markers** — Option to show signal data markers `off` (default) | `on`

When enabled, data markers are shown for signals plotted on the
Dashboard Scope block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Markers` |
| **Type:** string | character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

### Style

### **Foreground Color** — Grid lines color `[r g b]` vector

Select the color for the grid lines from a palette of standard colors
or specify a custom color using `RGB` values between
`0` and `255`.

#### Programmatic Use

Specify the `ForegroundColor` parameter for the
block as a string or a character vector that defines a
`1`-by-`3`
`[r g b]` vector with values between
`0` and `1`.

|  |
| --- |
| **Block Parameter:** `ForegroundColor` |
| **Type:** string | character vector |
| **Values:** `[r g b]` vector |

### **Background Color** — Plot area color `[r g b]` vector

Select the color for the plot area from a palette of standard colors
or specify a custom color using `RGB` values between
`0` and `255`.

#### Programmatic Use

Specify the `BackgroundColor` parameter for the
block as a string or a character vector that defines a
`1`-by-`3`
`[r g b]` vector with values between
`0` and `1`.

|  |
| --- |
| **Block Parameter:** `BackgroundColor` |
| **Type:** string | character vector |
| **Values:** `[r g b]` vector |

### **Font Color** — Ticks and tick labels color `[r g b]` vector

Select the color for the ticks and tick labels from a palette of
standard colors or specify a custom color using `RGB`
values between `0` and `255`.

#### Programmatic Use

Specify the `FontColor` parameter for the block
as a `1`-by-`3`
`[r g b]` vector with values between
`0` and `1`.

|  |
| --- |
| **Block Parameter:** `FontColor` |
| **Type:** `[r g b]` vector |

## Libraries

Simulink / Dashboard

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Dashboard blocks are ignored for code generation.

## Version History

**Introduced in R2015a**

## Description

Trace signals on scope display during simulation

The Dashboard Scope block plots connected signals during simulation on
a scope display. You can use the Dashboard Scope block with other
dashboard blocks to build an interactive dashboard of controls and indicators for your
model. Signals connected to the Dashboard Scope block log to the
Simulation Data Inspector for analysis during or after simulation. The Dashboard
Scope block can display signals of any data type that Simulink® supports, including enumerated data types, and up to eight signals from an
array or bus.

### Connect Dashboard Blocks

Dashboard blocks do not use ports to connect to model elements. To connect a dashboard block,
use connect mode. To enter connect mode on an unconnected block, pause on the block you want
to connect and click the Connect button . To enter connect mode on a connected block, select the
block, pause on the ellipsis that appears (…), and in the action menu that expands, click
the Connect button.

To connect a display block to a signal in your model or change the connection of a display
block, enter connect mode. Select the signal line to which you want to connect. From the
list that appears, select the signal to which you want to connect. Then, pause on the
dashboard block and click the Done Connecting button . To see the dashboard block display the value of the
connected block, run the simulation.

For more information about connecting dashboard blocks, see Connect Dashboard Blocks to Simulink Model.

You can also connect dashboard blocks to a Stateflow® chart. For more information, see Connect Dashboard Blocks to Stateflow (Stateflow).

This animation shows how to connect the Dashboard Scope block to
your model.

An unconnected Dashboard Scope block connects three signals.

### Analyze Signal Data

You can use the subplot menu or the context menu for the Dashboard
Scope block to:

- Show or hide data cursors.
- Zoom out by a fixed amount.
- Configure the mouse interaction to pan and select or to zoom in time,
  in *y*, or in both time and
  *y*.
- Perform a fit-to-view in time, in *y*, or in both
  time and *y*.

**Note**

To use keyboard shortcuts to analyze data, select a signal or axis in the
Dashboard Scope block.

To access the subplot menu, select the Dashboard Scope block then
click the three dots that appear when you pause on the plot area.

A selected Dashboard Scope block with two cursors displayed and the subplot menu visible.

### Configure Signal Line Style and Color

You can modify the color and line style for signals connected to a
Dashboard Scope block using the **Connection**
table in the Block Parameters dialog box or the Property Inspector. To modify the
appearance of a connected signal:

1. Click the preview of the signal appearance in the
   **Style** column of the
   **Connection** table.

   Line color and style selection menu for a signal connected to a Dashboard Scope block.
2. Choose a color from the palette of standard colors or select the
   **Custom** tab to specify a custom color using
   `RGB` values between `0` and
   `255`.
3. Select the line style from the solid, dotted, dashed, and dot-dashed
   options in the **Style** column.
4. Click **Set**.

When you mark a signal connected to the Dashboard Scope block for
signal logging, you can also configure the signal color and line style using the
Instrumentation Properties dialog box. In the signal color and line
style menu for the Dashboard Scope block, the **Override
style and color** option is selected by default and specifies whether
signal appearance options you choose using the **Connection** table
for the Dashboard Scope block override signal appearance options
configured in the instrumentation properties for the connected signals.

When you connect signals to the Dashboard Scope block using the
Block Parameters dialog box, the connection table shows the default signal color and
line style for each signal you connect. As you select signals to connect, the
**Connection** table updates the style and color for signals
that are not selected to indicate the style and color for the next signal you connect.

Connection table for a Dashboard Scope block with several options of signals to connect and two signals selected.

### Configure Complex Signal Format

When you connect a complex signal to the Dashboard Scope block, you
can configure how the signal is displayed by specifying the **Complex
Format** property for the signal:

1. Mark the complex signal for signal logging.
2. Right-click the logging badge for the complex signal and select
   **Properties**.
3. Specify the **Complex Format**.
4. Click **OK**.

When you specify the **Complex Format** for a signal as
`Real-Imaginary` or
`Magnitude-Phase`, the Dashboard Scope
block displays both components of the signal. The real or magnitude component is
displayed using the color indicated in the **Connection** table.
The imaginary or phase component is displayed using a different shade of the color
indicated in the **Connection** table.
