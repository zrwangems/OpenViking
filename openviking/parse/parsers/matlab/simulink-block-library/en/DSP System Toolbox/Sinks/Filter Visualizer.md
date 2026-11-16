---
type: simulink-block
title: 'Filter Visualizer'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'filtervisualizer'
documentation_source_path: 'ref/filtervisualizer.html'
language: en
---

# Filter Visualizer

## Ports

### Input

### **Num** — Numerator coefficients column vector | row vector | *L*-by-3 matrix | *L*-by-5 matrix

Specify the numerator coefficients of the filter as a row vector, column vector,
*L*-by-3 matrix corresponding to a cascade of second-order
sections, or an *L*-by-5 matrix corresponding to a cascade of
fourth-order sections, where *L* is the number of filter
sections.

If you set **Num Filters** to a value greater than 1, then the
block displays a **Num** port for each filter.

When you set **Filter Type** to `FIR`,
inputs on all **Num** ports must be column or row vectors.

**Data Types:** `single` | `double`

### **Den** — Denominator coefficients column vector | row vector | *L*-by-3 matrix | *L*-by-5 matrix

Specify the denominator coefficients of the filter as a row vector, column
vector, *L*-by-3 matrix corresponding to a cascade of second-order
sections, or an *L*-by-5 matrix corresponding to a cascade of
fourth-order sections, where *L* is the number of filter
sections.

If you set **Num Filters** to a value greater than 1, then the
block displays a **Den** port for each filter.

#### Dependency

To enable this port, set **Filter Type** to
`IIR`.

**Data Types:** `single` | `double`

## Parameters

### Scope Tab

#### Configuration

### **Num Filters** — Number of filters to display `1` (default) | positive integer in the range [1 20]

Specify the number of filters to display as a positive integer in the range [1
20]. The value of this parameter determines the number of input ports on the
block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumFilters` |
| **Type:** character vector or string scalar |
| **Values:** scalar in the range [1 20] |

### **Filter Type** — Type of filter response `FIR` (default) | `IIR`

Specify the filter response type as one of these options:

- `FIR` –– The block displays one input port per
  filter. You input the numerator coefficients of the filter(s) through the
  port(s).
- `IIR` –– The block displays two input ports per
  filter. You input the numerator and the denominator coefficients of the
  filter(s) through the ports.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FilterType` |
| **Type:** character vector or string scalar |
| **Values:** `'FIR'`, `'IIR'` |

### **Legend** — Display signal legend `off` (default) | `on`

Select this option to display the legend on the plot. The legend contains the
filter names in the format
`Filter:Number`. If you are visualizing
only one filter, the legend displays `Filter`. If you are visualizing
the magnitude and phase responses of multiple filters, the visualizer displays a
separate legend for each response in the format
`mag(Filter:Number)` and
`phase(Filter:Number)`, respectively.
If you are visualizing the responses of only one filter, the legend displays
`mag(Filter)` and `phase(Filter)`.

You can control which filters are visible in the scope using the legend. Click a
filter name in the legend to hide the frequency response of that filter in the scope.
To display the filter response, click the filter name again. To display only one
filter response, right-click the name of that filter, which hides all other filter
responses. To show all filter responses, press **Esc**. This setting is
equivalent to changing the **Visible** parameter in the
**Scope** tab > **Settings** (Gear button) > **Color and Styling**.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowLegend` |
| **Type:**`boolean` |

### **Magnitude Phase** — Plot magnitude and phase response of filter button

Click the button to plot the magnitude and phase response of the filter on two
separate axes. Click the button again to plot only the magnitude response.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PlotAsMagnitudePhase` |
| **Type:**`boolean` |

#### Configuration> Filter Visualizer Settings (Gear button)

### **FFT Length** — FFT length `2048` (default) | positive integer

Specify the FFT length that the filter visualizer uses to compute the spectral
estimates as a positive integer.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FFTLength` |
| **Type:** character vector or string scalar |
| **Values:** scalar |

### **Normalized Frequency** — Display the frequency response in normalized units `on` (default) | `off`

Select this parameter to display the frequency response of the filter in
normalized frequency units.

When you select this parameter, the frequency range is [0,1] and the frequency
axis (*x*-axis) units switch to `Normalized Frequency (×π
rad/sample)`.

When you clear this parameter, the frequency range is [0 *Fs*/2]
and the frequency axis (*x*-axis) units are in Hz.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NormalizedFrequency` |
| **Type:**`boolean` |

### **Sample Rate (Hz)** — Sample rate in Hz `44100` (default) | positive scalar

Enter the sample rate as a positive scalar in Hz.

**Tunable:** Yes

#### Dependencies

To enable this parameter, clear the **Normalized Frequency**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleRate` |
| **Type:** character vector or string scalar |
| **Values:** scalar |

### **Range** — Frequency range `[0,1]` (default) | two-element numeric vector

Specify the frequency range as a two-element numeric vector that is monotonically
increasing and of the form [*fmin*, *fmax*].

When you select the **Normalized Frequency** parameter,
*fmax* is in normalized frequency units and must be a positive
scalar that is less than or equal to 1. When you clear the **Normalized
Frequency** parameter, *fmax* is in Hz and must be less
than or equal to *Fs*/2, where *Fs* is the value you
specify in the **Sample Rate (Hz)** parameter.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FrequencyRange` |
| **Type:** character vector or string |
| **Value:** two-element numeric vector |

### **Display Unit** — Magnitude units `Magnitude (dB)` (default) | `Magnitude` | `Magnitude squared`

Specify the magnitude units in the display as one of these:

- `Magnitude`
- `Magnitude (dB)`
- `Magnitude squared`

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MagnitudeDisplay` |
| **Type:** character vector or string scalar |
| **Values:** `'Magnitude (dB)'`, `'Magnitude'`, `'Magnitude squared'` |

### **Display Precision** — Precision of data in scope display `4` (default) | positive integer ≤ 15

*Since R2024b*

Specify the precision of numeric values in the scope display as a positive integer in
the range [1, 15].

**Tunable:** Yes

### **Title** — Display title character vector | string

Specify the display title as a character vector or a string.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Title` |
| **Type:** character vector or string |

### **X-Scale** — Scale of frequency axis `Linear` (default) | `Log`

Specify the scale of the frequency axis as `'Linear'` or
`'Log'`.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `XScale` |
| **Type:** character vector or string |
| **Values:** `'Linear'`, `'Log'` |

### **Y-Limits** — *y*-axis limits [`−25` `25`] | [`ymin ymax`]

Specify the *y*-axis limits of the magnitude display in the
Filter Visualizer as a two-element numeric vector of the form [`ymin
ymax`]. The units of the *y*-axis limits depend on the
**Display Unit** parameter.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `YLimits` |
| **Type:** character vector or string |
| **Value:** two-element numeric vector |

### **Show Grid** — Show internal grid lines `on` (default) | `off`

Select this check box to show the grid in the Filter Visualizer display.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowGrid` |
| **Type:** `logical` |

### **Plot Type** — Type of plot `Line` (default) | `Stairs` | `Stem`

Specify the type of plot to use in the filter visualizer window as one of these:

- `Line` –– The filter visualizer connects each point
  on the magnitude and phase response plot with a line.
- `Stairs` –– The filter visualizer displays the
  filter response (magnitude, phase, or both) as a stair-step graph. A stair-step
  graph is made up of only horizontal lines and vertical lines. Each horizontal
  line represents the filter response over a frequency value and is connected to
  two vertical lines. Each vertical line represents a change in values occurring
  at a frequency.
- `Stem` –– The filter visualizer displays the
  frequency response as circles with vertical lines extending down to the
  *x*-axis at each of the frequency values.

You can individually control the type of
plot for each filter response curve. To control the type of plot for each curve,
select the filter and set the **Plot Type** parameter accordingly. If
you display both the magnitude and phase responses, the visualizer applies the same
plot type setting to both the response curves. *(since R2025a)*

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PlotType` |
| **Type:** character vector or string scalar |
| **Values:** `'Stem'`, `'Line'`, `'Stairs'` |

### **Font Size** — Font size of labels `8.5` (default) | scalar in the range [1,100]

Specify the font size as a positive scalar in the range [1,100].

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `-` |
| **Type:** double |

### **Background** — Window background black (default) | color picker

Specify the color that you want to apply to the background of the scope
figure.

**Tunable:** Yes

### **Axes** — Axes background color black (default) | color picker

Specify the color that you want to apply to the background of the axes.

**Tunable:** Yes

### **Labels** — Color of labels gray (default) | color picker

Specify the color of the labels, grid, and the channel names in the legend.

**Tunable:** Yes

### **Line** — Filter for line property settings filter names

Select the filter for which you want to modify the visibility, line color, style,
width, and marker properties.

**Tunable:** Yes

### **Visible** — Filter visibility `on` (default) | `off`

Specify whether the selected filter is visible. If you clear this check box, the
frequency response line disappears in the display.

You can control this parameter directly from the legend. Click a filter name in
the legend to hide the frequency response of the filter in the scope. To show the
filter response, click the filter name again. To show only one filter response,
right-click the filter name, which hides all other filter responses. To show all
filter responses, press **Esc**.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Visible` |
| **Type:** `logical` |

### **Style** — Line style `-` (default) | `:` | `-`. | `--` | `None`

Specify the line style for the selected filter response.

**Tunable:** Yes

### **Width** — Line width `1.5` (default) | `0.5` | `1` | `2` | ...

Specify the line width for the selected filter response.

**Tunable:** Yes

### **Marker** — Data point markers `None` (default) | `+` | `x` | ...

Specify markers for the selected filter response to show at its data points. This
parameter is similar to the Marker property for plots. You
can choose any of the marker symbols from the drop-down list.

**Tunable:** Yes

### **Color** — Line color yellow (default) | color picker

Specify the line color for the selected filter response.

**Tunable:** Yes

#### Share

### **Copy to Clipboard** — Send display to clipboard button

Click this button to copy the scope display to the clipboard. You can preserve the
color in the display by selecting **Preserve Colors** in the
**Copy to Clipboard** drop down.

### **Preserve Colors** — Preserve colors when copying to clipboard `off` (default) | `on`

When you copy the display to the clipboard using the **Copy to
Clipboard** and the **Print** options in the
**Scope** tab > **Share** section, select this
parameter for the scope to preserve the colors.

To access **Preserve Colors**, click the drop-down arrow for **Copy
to Clipboard**.

**Tunable:** Yes

### **Print** — Print display button

Click this button to save the scope display as an image or a PDF or to print the
display.

### Measurements Tab

#### Channel

### **Channel** — Filter for which to obtain measurements `Filter` (default) | filter name

Choose the filter response for which you need to obtain measurements. The filter
names are in the format `Filter:Number`.
If you are visualizing only one filter, the legend displays `Filter`.
If you are visualizing the magnitude and phase responses of multiple filters, the
visualizer displays a separate name for each response in the format
`mag(Filter:Number)` and
`phase(Filter:Number)`, respectively.
If you are visualizing the responses of only one filter, the legend becomes
`mag(Filter)` and `phase(Filter)`.

**Tunable:** Yes

#### Dependency

To enable this parameter, pass some data through the scope.

#### Cursors

### **Data Cursors** — Enable cursor measurements button

Click the **Data Cursors** button to enable data cursor
measurements. Each cursor tracks a vertical line along the frequency response. The
scope displays the difference between frequency(*x*) values and
frequency response (*y*) values of the filter at the two cursors in
the box between the cursors.

**Tunable:** Yes

### **Snap to data** — Snap cursors to data `off` (default) | `on`

Select this parameter to position the cursors on the signal data points.

**Tunable:** Yes

### **Lock cursor spacing** — Lock cursor spacing `off` (default) | `on`

Select this parameter to lock the frequency difference between the two
cursors.

**Tunable:** Yes

#### Peaks

### **Peak Finder** — Enable peak finder measurements button

Select **Peak Finder** to enable peak finder measurements. An
arrow appears on the plot at each maxima and a Peaks panel appears at the bottom of
the scope window.

**Tunable:** Yes

### **Num Peaks** — Maximum number of peaks to show `3` (default) | positive integer less than 100

Specify the maximum number of peaks to show as a positive integer less than
100.

**Tunable:** Yes

### **Min Height** — Level above which scope detects peaks `-Inf` (default) | real scalar value

Specify the level above which the scope detects peaks as a real scalar.

**Tunable:** Yes

### **Min Distance** — Minimum number of samples between adjacent peaks `1` (default) | positive integer

Specify the minimum number of samples between adjacent peaks as a positive
integer.

**Tunable:** Yes

### **Threshold** — Minimum difference in height of peak and its neighboring samples `0` (default) | nonnegative scalar

Specify the minimum difference in the height of the peak and its neighboring
samples as a nonnegative scalar.

**Tunable:** Yes

### **Label Peaks** — Label peaks button

Select **Label Peaks** to label the peaks. The scope displays
the labels (**P1**, **P2**,
…) above the arrows in the plot.

**Tunable:** Yes

### Property Inspector Only

### **Filter Names** — Input filter names `[]` (default) | character vector | string | array of strings or character vectors.

Input filter names, specified as a character vector, string, or array of either.
The names appear in the legend, **Filter Visualizer Settings**, and
**Measurements** panels. If you do not specify filter names, the
block displays the filter names as `Filter: 1`, `Filter:
2`, etc.

#### Dependency

To see the filter names, select **Legend** in the
**Scope** tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FilterNames` |
| **Type:** cell array of character vectors or string array |

### **Maximize Axes** — Maximize size of plots `Auto` (default) | `Off` | `On`

- `Auto` — If you do not specify
  **Title** and y-label, maximize all plots by default.
- `On` — Maximize all plots and hide
  **Title** and y-label.
- `Off` — Do not maximize plots.

Point anywhere in the Filter Visualizer to see the maximize axes
button.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MaximizeAxes` |
| **Type:** character vector or string scalar |

### **Axes Scaling** — Y-axis scaling mode `Auto` (default) | `Manual` | `Updates` | `OnceAtStop`

- `Auto` — The filter visualizer scales the axes as
  needed to fit the data, both during and after simulation.
- `Manual` — The filter visualizer does not scale the
  axes automatically.
- `Updates` — The filter visualizer scales the axes
  limits once after completing the number of visual updates specified in the
  **Number of Updates** text box (`100` by
  default). Scaling occurs only once during each run.
- `OnceAtStop` — The filter visualizer scales the axes
  when the simulation stops.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AxesScaling` |
| **Type:** character vector or string scalar |

### **Number of Updates** — Number of updates before scaling `100` (default) | integer

Set this property to delay auto scaling the *y*-axis.

**Tunable:** Yes

#### Dependency

To enable this property, set **Axes Scaling** to
`Updates`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AxesScalingNumUpdates` |
| **Type:** character vector or string scalar |
| **Values:** scalar |

## Libraries

DSP System Toolbox / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block can be used for simulation visibility in systems that generate code, but is
not included in the generated code.

## Version History

**Introduced in R2023a**

### R2025a: Control plot type for each filter response curve individually

You can now individually control the type of plot for each filter response curve. To
control the type of plot for each curve, select the filter and set the **Plot
Type** parameter accordingly. If you display both the magnitude and phase
responses, the visualizer applies the same plot type setting to both the response
curves.

### R2024b: Higher display precision in scope UI

You can now increase the display precision to 15 digits using the **Display
Precision** property in the scope settings under **Display and
Labels**. This precision affects all the measurements and data that the scope
displays on its status bar.

### R2024b: **Preserve Colors** is now available in scope toolstrip

The **Preserve colors for copy to clipboard** property has been renamed to **Preserve Colors** and is now available in the scope toolstrip under **Copy Display**.

## Description

Display magnitude and phase response of time-varying digital filters

The Filter Visualizer block displays the magnitude response and phase
response of time-varying digital filters or time-varying filter coefficients. You can
visualize the frequency response of up to 20 filters at a time using this visualizer.

You can use the visualizer to configure the plot settings, find the peak values, enable
cursor measurements, and even copy the scope display to the clipboard For more information,
see Configure Filter Visualizer. To access the filter
visualizer programmatically, use the `dsp.DynamicFilterVisualizer` object.

Filter Visualizer showing the Measurements Tab of the toolstrip. Data cursors and the peak finder are enabled.
