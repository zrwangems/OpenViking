---
type: simulink-block
title: 'Spectrum Analyzer'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Utilities / Other'
documentation_page: 'spectrumanalyzer'
documentation_source_path: 'ref/spectrumanalyzer.html'
language: en
---

# Spectrum Analyzer

## Ports

### Input

### **u** — Signals to visualize scalar | vector | matrix | array

Connect the signals you want to visualize. You can have up to 96 input
ports. Input signals must have these characteristics:

- **Signal Domain** — Frequency or time
  signals.
- **Type** — Discrete signals.
- **Data type** — Any data type that
  Simulink® supports. See Data Types Supported by Simulink.
- **Dimension** — One dimensional
  (vector), two dimensional (matrix), or multidimensional (array)
  signals. Input signal must have a fixed number of channels. See
  Signal Dimensions and Determine Signal Dimensions.

The Spectrum Analyzer block supports variable-size input
signals, that is, the frame size of the signals can change during
simulation. When the signal frame size changes, the sample rate the scope
uses changes accordingly, which in turn updates the frequency span of the
spectrum display.

The Spectrum Analyzer block accepts fixed-point input, but
converts it to `double` for display.

This
port is unnamed until you enable the **RBW** port. *(since R2024a)*

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

### **RBW** — RBW Value positive scalar

Specify the resolution bandwidth in Hz through this port. RBW defines the
smallest positive frequency that can be resolved by the scope. You can also
specify the RBW value using the **RBW (Hz)** parameter on
the **Estimation** tab.

#### Dependency

To enable this port, set the **RBW (Hz)** parameter
on the **Estimation** tab to `Input
port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

This section lists the block parameters for the Spectrum Analyzer block in Simscape and RF Blockset™. For a complete list of parameters, see Spectrum
Analyzer (DSP System Toolbox).

### Scope Tab

#### Views

### **Spectrum** — Type of spectrum to display `Power` (default) | `Power Density` | `RMS`

Set the type of spectrum to display as one of these values:

- `Power` — Spectrum Analyzer shows the
  power spectrum.
- `Power Density` — Spectrum Analyzer shows
  the power spectral density. The power spectral density is the
  squared magnitude of the spectrum normalized to a bandwidth of 1
  Hz.
- `RMS` — Spectrum Analyzer shows the root
  mean squared spectrum. Use this option to view the frequency of
  voltage or current signals.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SpectrumType` |
| **Type:** character vector or string scalar |

**Data Types:** `char` | `string`

#### Bandwidth

### **Sample Rate (Hz)** — Sample rate the scope uses in Hz `Inherited` (default) | positive scalar

Specify the sample rate the scope uses in Hz as one of the following:

- `Inherited` — Use this option to specify the same
  sample rate as the input signal.
- Positive scalar — The sample rate you specify must be at least twice the
  sample rate of the input signal. Otherwise, you might see unexpected
  behavior when visualizing your signal in the scope due to aliasing.

When the signal frame size changes, the sample rate the scope uses changes
accordingly, which in turn updates the frequency span of the spectrum display.

To display the sample rate on the status bar, click the ⋮
icon in the status bar and select `Sample Rate`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleRate`, `SampleRateSource` |
| **Type:** `double` |

**Tunable:** Yes

### **Offset (Hz)** — Offset to apply to frequency axis `0` (default) | scalar | vector

Specify the offset to apply to the frequency axis
(*x*-axis) in units of Hz as one of the
following:

- Scalar — Apply the same frequency offset to all
  channels.
- Vector — Apply a specific frequency offset for each
  channel. The vector length must be equal to the
  number of input channels.

  The overall span must fall within the Nyquist Frequency Interval. You can control the overall span in different
  ways based on how you set the **Span
  (Hz)** parameter.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FrequencyOffset` |
| **Type:** `double` |

#### Configuration > Spectrum Analyzer Settings

### **Num Inputs** — Number of input ports 1 (default) | integer between 1 and 96

The number of input ports to the block, specified as an integer between 1 and 96. To
change the number of input ports, drag a new input signal line to the block and the
block automatically creates new ports.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumInputPorts` |
| **Type:** character vector or string scalar |
| **Values:** scalar between 1 and 96 |

### **Open at Simulation Start** — Automatically open scope when simulation starts on (default) | off

Select this parameter to automatically open the Spectrum Analyzer window when you run
the simulation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OpenAtSimulationStart` |
| **Type:** logical |

### **Display Precision** — Precision of data in scope display `4` (default) | positive integer ≤ 15

*Since R2024b*

Specify the precision of numeric values in the scope display as a positive integer in
the range [1, 15].

**Tunable:** Yes

### **Y-Label** — *y*-axis label character vector | string scalar

Specify the *y*-axis label in the Spectrum display as a
character vector or a string scalar. To display signal units, add
`(%<SignalUnits>)` to the label. When simulation
starts, Simulink replaces `(%SignalUnits)` with the units
associated with the signals. For example, for a velocity signal with units
of m/s
enter:

```
Velocity (%<SignalUnits>)
```

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `YLabel` |
| **Type:** character vector or string scalar |

### **Y-Limits** — *y*-axis limits [`−80` `20`] | [`ymin ymax`]

Specify the *y*-axis limits in the Spectrum Analyzer
display as a two-element numeric vector of the form [`ymin
ymax`]. The units of the *y*-axis limits
depend on the **Spectrum Unit** in the
**Spectrum** tab.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `YLimits` |
| **Type:** `double` |

### **Title** — Display title character vector | string

Specify the display title. Enter `%<SignalLabel>`
to use the signal labels in the Simulink model as the axes titles.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Title` |
| **Type:** character vector or string |

### **Show Grid** — Show internal grid lines `on` (default) | `off`

Select this check box to show the grid in the Spectrum
Analyzer display.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowGrid` |
| **Type:** `logical` |

### **Plot Type** — Plot type `Line` (default) | `Stem`

Specify whether to display a `Line` or
`Stem` plot in the Spectrum display.

You can individually control the
type of plot for each line. Select the line and set the **Plot
Type** accordingly. *(since R2025a)*

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PlotType` |
| **Type:** character vector or string scalar |

### **Font Size** — Font size of labels `8.5` (default) | positive scalar

Specify the font size of the ticks, labels, title, and measurements of the scope as a positive
scalar.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `-` |
| **Type:** double |

### **Background** — Window background black (default) | color picker

Specify the background color in the scope figure.

**Tunable:** Yes

### **Axes** — Axes background color black (default) | color picker

Specify the background color of the axes.

**Tunable:** Yes

### **Labels** — Color of labels gray (default) | color picker

Specify the color of the labels, grid, and the channel names in the legend.

**Tunable:** Yes

### **Line** — Channel for line property settings channel names

Specify the channel for which you want to modify the visibility, line color, style, width, and
marker properties.

**Tunable:** Yes

### **Visible** — Channel visibility `on` (default) | `off`

Select this check box to display the channel you have selected. If you clear this
check box, the selected channel is no longer visible. You can also click the signal name
in the legend to control its visibility. For more details, see Legend.

**Tunable:** Yes

### **Style** — Line style `-` (default) | `:` | `-`. | `--` | `None`

Specify the line style for the selected channel.

**Tunable:** Yes

### **Width** — Line width `1.5` (default) | `0.5` | `1` | `2` | ...

Specify the line width for the selected channel.

**Tunable:** Yes

### **Marker** — Data point markers `None` (default) | `+` | `x` | ...

Specify a data point marker for the selected channel. This parameter is similar to the
Marker property for plots. You
can choose any of the marker symbols from the drop-down list.

**Tunable:** Yes

### **Color** — Line color yellow (default) | color picker

Specify the line color for the selected channel.

**Tunable:** Yes

#### Configuration

### **Legend** — Show or hide signal legend button

Click the **Legend** button to enable the Spectrum
Analyzer to display. The legend displays the signal names from the model.
For signals with multiple channels, the scope appends a channel index after
the signal name. Continuous signals have straight lines before their names
and discrete signals have step-shaped lines.

You can control which signals are visible using the legend. To hide a
signal in the scope legend, click the signal name. To display the signal,
click the signal name again. Alternatively, you can control which signal is
visible using the **Visible** parameter in the
**Spectrum Analyzer Settings** (Gear button).

To display only one signal and hide all other signals, right-click the
name of the signal you want the scope to display. To show all signals, press
**Esc**.

**Note**

The legend displays only the first 20 signals. You cannot view or
control any additional signals from the legend.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowLegend` |
| **Type:** `logical` |

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

### Estimation Tab

#### Frequency Resolution

### **RBW (Hz)** — Resolution bandwidth in Hz `Auto` (default) | `Input port` | positive scalar

Specify the resolution bandwidth in Hz. This parameter defines the smallest positive frequency
that can be resolved by the scope. By default, this parameter is set to
`Auto`. In this case, the spectrum analyzer determines the
appropriate value to ensure that there are 1024 RBW intervals over the specified
frequency span.

If you set this parameter to `Input port`, you can specify
the RBW value through an input port on the block.

If you set this parameter to a numeric value, the value must allow at least two RBW intervals over the specified frequency span. In other words, the ratio of the overall frequency span to RBW must be greater than two:

spanRBW>2

To display this property on the status bar, click the ⋮
icon in the status bar and select `RBW`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RBWSource`, `RBW` |
| **Type:** character vector, string scalar, `double` |

**Tunable:** Yes

#### Averaging

### **Averaging Method** — Smoothing method `Exponential` (default) | `VBW` | `Running`

Specify the smoothing method as one of the following:

- `Exponential` — The
  block computes the average over samples weighted by an
  exponentially decaying forgetting factor. Use the
  **Forgetting Factor** parameter to specify
  the weighted forgetting factor.
- `VBW` — The block uses a lowpass
  filter to smooth the trace and decrease the noise. Use the
  **VBW (Hz)** parameter to specify the video
  bandwidth (VBW) value.
- `Running` — Running average of
  the last *Q* samples. Use the
  **Spectral Averages** parameter to specify
  *Q*. *(since R2025a)*

For more information on the averaging methods, see Averaging Method.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AveragingMethod` |
| **Type:** character vector or string scalar |

### **VBW (Hz)** — Video bandwidth `Auto` (default) | `Input port` | positive scalar

Specify the video bandwidth as one of the following:

- `Auto` –– The Spectrum Analyzer adjusts the
  VBW such that the equivalent forgetting factor is 0.9.
- `Input port` –– An input port appears
  on the scope and you can specify the VBW value through this
  port.
- Positive scalar –– You specify a positive scalar. The Spectrum
  Analyzer adjusts the VBW using this value. The value you specify
  must be less than or equal to **Sample Rate
  (Hz)**/2.

For more details on the video bandwidth method, see Averaging Method.

The Spectrum Analyzer shows the VBW value in the status bar at the bottom
of the display. To display the VBW value, click the kebab icon in the right most corner of the status bar icon in the status bar and select
`VBW`.

#### Dependency

To enable this parameter, set **Averaging Method** to
`VBW`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VBWSource`, `VBW` |
| **Type:** `double` |

**Tunable:** Yes

### **Forgetting Factor** — Forgetting factor of weighted average method `0.9` (default) | scalar in the range [0,1]

Specify the forgetting factor of the exponential weighted averaging method
as a scalar in the range [0,1].

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Averaging Method** to
`Exponential`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ForgettingFactor` |
| **Type:** `double` |

### **Spectral Averages** — Number of spectral averages `1` (default) | positive integer

*Since R2025a*

Specify the number of spectral averages *Q* as a positive
integer.

The Spectrum Analyzer computes the current power spectrum estimate by
computing a running average of the last *Q* power spectrum
estimates.

#### Dependency

To enable this parameter, set **Averaging Method** to
`Running`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SpectralAverages` |
| **Type:** `double` |

**Data Types:** `double`

#### Window Options

### **Window** — Windowing method `Hann` (default) | `Rectangular`

Specify the windowing method to apply to the spectrum. Windowing is used
to control the effect of sidelobes in spectral estimation. The window you
specify affects the window length required to achieve a resolution bandwidth
and the required number of samples per update. For more information about
windowing, see Windows (Signal Processing Toolbox).

You can access additional windowing algorithms if you install DSP System Toolbox.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Window` |
| **Type:** character vector or string scalar |

### **Overlap (%)** — Percentage of overlap `0` (default) | scalar in the range [0 100)

Specify the percentage of overlap between the previous and the current
buffered data segments as a scalar in the range [0 100). The overlap creates
a window segment that the scope uses to compute a spectral estimate. The
value must be greater than or equal to zero and less than 100.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OverlapPercent` |
| **Type:** `double` |

### Measurements Tab

#### Channel

### **Channel** — Channel for which to obtain measurements `1` (default) | positive integer

The channel for which you need to obtain measurements, specified as a positive integer in the range [1 *N*], where *N* is the number of input channels.

**Tunable:** Yes

#### Dependency

To enable this parameter, pass some data through the scope.

#### Programmatic Use

See `MeasurementChannel`.

#### Cursors

### **Data Cursors** — Enable cursor measurements button

Click the **Data Cursors** button to enable data cursor measurements. Each
cursor tracks a vertical line along the signal. The scope displays the difference
between *x*- and *y*-values of the signal at the two
cursors in the box between the cursors.

**Tunable:** Yes

#### Programmatic Use

See `Enabled`.

### **Snap to data** — Snap cursors to data `off` (default) | `on`

Select this parameter to position the cursors on the signal data points.

**Tunable:** Yes

#### Programmatic Use

See `SnapToData`.

### **Lock cursor spacing** — Lock cursor spacing `off` (default) | `on`

Select this parameter to lock the frequency difference between the two cursors.

**Tunable:** Yes

#### Programmatic Use

See `LockSpacing`.

#### Peaks

### **Peak Finder** — Enable peak finder measurements button

Click the **Peak Finder** button to enable peak finder
measurements. An arrow appears on the plot at each maxima and a Peaks panel appears at
the bottom of the scope window.

**Tunable:** Yes

#### Programmatic Use

See `Enabled`.

### **Num Peaks** — Maximum number of peaks to show `3` (default) | positive integer less than 100

Specify the maximum number of peaks to show as a positive integer less than 100.

**Tunable:** Yes

#### Programmatic Use

See `NumPeaks`.

### **Min Height** — Level above which scope detects peaks `-Inf` (default) | real scalar value

Specify the level above which the scope detects peaks as a real scalar.

**Tunable:** Yes

#### Programmatic Use

See `MinHeight`.

### **Min Distance** — Minimum number of samples between adjacent peaks `1` (default) | positive integer

Specify the minimum number of samples between adjacent peaks as a positive integer.

**Tunable:** Yes

#### Programmatic Use

See `MinDistance`.

### **Threshold** — Minimum difference between height of peak and its neighboring samples `0` (default) | nonnegative scalar

Specify the minimum difference between the height of the peak and its neighboring
samples as a nonnegative scalar.

**Tunable:** Yes

#### Programmatic Use

See `Threshold`.

### **Label Peaks** — Label peaks button

Click the **Label Peaks** button to label the peaks. The scope displays the
labels (**P1**, **P2**, …)
above the arrows in the plot.

**Tunable:** Yes

#### Programmatic Use

See `LabelPeaks`.

#### Distortion

### **Distortion** — Enable distortion measurements button

Click the **Distortion** button to enable distortion measurements. A
Distortion panel appears at the bottom of the scope window when you click this
button.

**Tunable:** Yes

#### Programmatic Use

See `Enabled`.

### **Distortion Type** — Type of measurement to display `Harmonic` (default) | `Intermodulation`

Specify the type of measurement data to display as `Harmonic` or `Intermodulation`. For more details, see Distortion Measurements.

**Tunable:** Yes

#### Programmatic Use

See `Type`.

### **Num Harmonics** — Number of harmonics to measure `6` (default) | positive integer

Specify the number of harmonics to measure as a positive integer less than or equal to 99.

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Distortion Type** to `Harmonic`.

#### Programmatic Use

See `NumHarmonics`.

### **Label Harmonics** — Label harmonics `off` (default) | `on`

When you select this parameter, the spectrum analyzer adds numerical labels to harmonics in
the spectrum display.

**Tunable:** Yes

#### Programmatic Use

See `LabelValues`.

### **Label Frequencies** — Label frequencies `off` (default) | `on`

When you select this parameter, the spectrum analyzer adds numerical labels to the first-order
intermodulation product and third-order frequencies in the spectrum analyzer
display.

**Tunable:** Yes

#### Programmatic Use

See `LabelValues`.

### Spectrum Tab

#### Trace Options

### **Two-Sided Spectrum** — Enable two-sided spectrum view `on` (default) | `off`

Select this check box to enable a two-sided spectrum view. In this view,
the spectrum analyzer shows both negative and positive frequencies.
When the input signal is complex-valued, you must select this
parameter. If you clear this check box, the spectrum analyzer shows a
one-sided spectrum with positive frequencies only. In this case, the
input signal data must be real valued.

When you clear this check box, the spectrum analyzer uses power folding.
The *y*-axis values are twice the amplitude that they
would be if you were to select this parameter, except at
`0` and the Nyquist frequency. A one-sided
power spectral density (PSD) contains the total power of the signal in
the frequency interval from DC to half the Nyquist rate. For more
information, see `pwelch` (Signal Processing Toolbox).

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PlotAsTwoSidedSpectrum` |
| **Type:** `logical` |

#### Scale

### **Frequency Scale** — Scale of frequency axis `Linear` (default) | `Log`

Specify the scale to display frequencies as
`Linear` or `Log`.
When the frequency span contains negative frequency values, you cannot
choose the logarithmic option.

**Tunable:** Yes

#### Dependency

To set the **Frequency Scale** to
`Log`, clear the **Two-Sided
Spectrum** check box in the **Trace
Options** section in the **Spectrum**
tab. If you select the **Two-Sided Spectrum** check
box, then the **Frequency Scale** parameter is set to
`Linear`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FrequencyScale` |
| **Type:** character vector or string scalar |

### **Reference load (Ω)** — Reference load in Ω `1` (default) | positive real scalar

Specify the reference load in ohms that the Spectrum
Analyzer uses as a reference to compute the power values.

**Tunable:** Yes

#### Dependency

To enable this parameter, set:

- **Spectrum** type to
  `Power` or
  `Power Density`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ReferenceLoad` |
| **Type:** `double` |

### **Spectrum Unit** — Units of the spectrum `dBm` (default) | `dBm/Hz` | `dBV` | `dBuV` *(since R2023b)* | `Vrms`

Specify the units in which the Spectrum Analyzer displays the power values
as one of the following:

- `dBm`
- `dBV`
- `dBuV` *(since R2023b)*
- `Vrms`
- `dBm/Hz`

**Tunable:** Yes

#### Dependency

The units available depend on the value you choose for the
**Spectrum** parameter in the
**Scope** tab.

| Scope tab > Spectrum option | Available Units |
| --- | --- |
| `Power` | `dBm` |
| `Power Density` | `dBm/Hz` |
| `RMS` | `dBV`, `dBuV` *(since R2023b)*, `Vrms` |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SpectrumUnits` |
| **Type:** character vector or string scalar |

### Property Inspector Only

### **Channel Names** — Input channel names `[]` (default) | character vector | string | array of strings or character vectors.

Input channel names, specified as a character vector, string, or array. The names appear in
the legend, **Settings**, and **Measurements**
panels. If you do not specify the names, the scope labels the channels as
`Channel 1`, `Channel 2`, etc.

**Example:** ["A","B"]

#### Dependency

To see channel names, select **Legend** in the **Scope**
tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ChannelNames` |
| **Type:** cell array of character vectors or string array |

### **Maximize Axes** — Maximize size of plots `Auto` (default) | `Off` | `On`

- `Auto` — If you have not specified
  **Title** and **Y-Label**, the
  scope maximizes all plots.
- `On` — The scope maximizes all plots and hides all
  values in **Title** and **Y-label**.
- `Off` — The scope does not maximize plots.

Hover over the Spectrum Analyzer to see the maximize axes button
.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MaximizeAxes` |
| **Type:** character vector or string scalar |

### **Axes Scaling** — Y-axis scaling mode `OnceAtStop` (default) | `Manual` | `Auto` | `Updates`

- `OnceAtStop` — Scale *y*-axis after
  simulation completes.
- `Manual` — Manually scale *y*-axis range with the **Scale Y-axis Limits** toolbar button.
- `Auto` — Scale *y*-axis range during and after simulation.
- `Updates` — Scale *y*-axis after the number of time steps specified in the Number of Updates text box (`100` by default). Scaling occurs only once during each run.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AxesScaling` |
| **Type:** character vector or string scalar |

### **Number of Updates** — Number of updates before scaling `100` (default) | integer

Set this property to delay auto scaling the y-axis.

**Tunable:** Yes

#### Dependency

To enable this property, set Axes Scaling to `Updates`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AxesScalingNumUpdates` |
| **Type:** character vector or string scalar |
| **Values:** scalar |

## Libraries

Simscape / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2025a: Control plot type for each line individually

You can now individually control the type of plot for each line. To control the type of plot
for a line, select the line and set the **Plot Type**
parameter accordingly.

### R2025a: Support for running averaging method

The Spectrum Analyzer block now supports the running averaging method to
compute the power spectrum estimate. To enable this mode, set the **Averaging
Method** parameter in the **Estimation** tab to
`Running` and the **Spectral Averages**
parameter to a positive integer.

For more information, see the Algorithms section.

### R2024b: Display spectral data for any number of input samples and adjust RBW accordingly

Previously, the Spectrum Analyzer block required a minimum number of samples to update
the display for a given RBW value. Starting in R2024b, this limitation is removed. The scope
now updates its display for any number of input samples and adjusts the RBW value
accordingly.

### R2024b: Auto adjust RBW to maintain 1024 samples

The Spectrum Analyzer block can now automatically adjust the resolution bandwidth (RBW) so as
to maintain the number of samples per spectral update at 1024 (*Nsamples* =
1024) irrespective of the window you select.

To enable this mode in the Spectrum Analyzer block, set:

- **RBW (Hz)** to `Auto`.

### R2024b: Higher display precision in scope UI

You can now increase the display precision to 15 digits using the **Display
Precision** property in the scope settings under **Display and
Labels**. This precision affects all the measurements and data that the scope
displays on its status bar.

### R2024b: **Preserve Colors** is now available in scope toolstrip

The **Preserve colors for copy to clipboard** property has been renamed to **Preserve Colors** and is now available in the scope toolstrip under **Copy Display**.

### R2024a: **Analyzer** tab has been renamed as **Scope** tab

The **Analyzer** tab in spectrum analyzer has been renamed as
**Scope** tab.

### R2023b: Spectrum Analyzer supports `dBuV` units

You can set **Spectrum Unit** to `dBuV` when
you set **Spectrum** to `RMS`.

### R2023a: Spectrum Analyzer with improved responsiveness and toolstrip interface in Simulink

In R2023a, the Spectrum Analyzer block is more responsive and its
toolstrip interface is improved to provide you easy access to spectral analysis, estimation,
and measurements. You can configure and display Spectrum Analyzer settings from the command
line with the `SpectrumAnalyzerBlockConfiguration` object.

## Description

Display frequency spectrum

**Note**

The Spectrum Analyzer block in Simscape™ provides a subset of the functionality provided by the DSP System Toolbox™ block with the same name. This page describes the block configuration and
functionality available with a Simscape license. If you also have a DSP System Toolbox license, then the Spectrum Analyzer block in the **Simscape** > **Utilities** library is identical to the block in the **DSP System Toolbox** > **Sinks** library. For more information, see Spectrum
Analyzer (DSP System Toolbox).

The Spectrum Analyzer block displays frequency spectra of input signals
with discrete sample times.

In a Simscape model, to use a Spectrum Analyzer block instead of a regular
scope:

1. Add a Spectrum Analyzer block to your block diagram.
2. If your model uses a variable-step solver, also add a Rate Transition block and connect it to the input port of the Spectrum Analyzer
   block. Set the **Output port sample time** parameter to the sample time
   you want the Spectrum Analyzer to use.

   If your model uses a local solver, then it outputs physical signals with discrete
   sample times and you do not need to add a Rate Transition block. However,
   if you need to downsample from the solver fixed step size, you can use a Rate
   Transition block. For more information on using local solvers, see Making Optimal Solver Choices for Physical Simulation.
3. Use a PS-Simulink Converter block to connect the physical output signal
   of interest to the input port of the Spectrum Analyzer block (or to the
   input of the Rate Transition block, if you are using one). For more
   information, see Connecting Simscape Diagrams to Simulink Sources and Scopes. You can also use additional signal processing blocks between the PS-Simulink
   Converter and the Spectrum Analyzer blocks to enhance signal
   quality.
4. Run the simulation. Once the simulation is complete, the Spectrum Analyzer, referred
   to here as the scope, opens and displays the frequency spectrum of the signal.

**Note**

To prevent the scope from opening when you run your model, right-click the scope icon
and select `Comment Out`. If the scope is already open, and you
comment it out in the model, the scope displays this message: `No data can be shown
because this scope is commented out`. Select `Uncomment`
to turn the scope on again.

### Programmatic Control

You can configure and display the Spectrum Analyzer settings from the command line with
the `SpectrumAnalyzerBlockConfiguration` object.
