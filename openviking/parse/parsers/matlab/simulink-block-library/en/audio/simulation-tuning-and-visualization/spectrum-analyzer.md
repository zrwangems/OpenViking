---
type: simulink-block
title: 'Spectrum Analyzer'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Scopes and Data Logging'
documentation_page: 'spectrumanalyzerblock'
documentation_source_path: 'ref/spectrumanalyzerblock.html'
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
  Simulink supports. See Data Types Supported by Simulink (Simulink).
- **Dimension** — One dimensional
  (vector), two dimensional (matrix), or multidimensional (array)
  signals. Input signal must have a fixed number of channels. See
  Signal Dimensions (Simulink) and Determine Signal Dimensions (Simulink).

The Spectrum Analyzer block supports variable-size input
signals, that is, the frame size of the signals can change during
simulation. When the signal frame size changes, the sample rate the scope
uses changes accordingly, which in turn updates the frequency span of the
spectrum display. For an example that shows this
behavior, see Display Variable-Size Input Signals on Spectrum Analyzer.

The Spectrum Analyzer block accepts fixed-point input, but
converts it to `double` for display.

This
port is unnamed until you enable one of these inputs ports:

- **F**
- **RBW**
- **VBW**

*(since R2024a)*

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

### **F** — Frequencies in Hz column vector

Specify the frequencies in Hz. The frequency vector must be a finite,
monotonically increasing, column vector with two or more elements. The
number of frequency vector points must be equal to the input frame size. You
can also specify the frequencies using the **Frequency
(Hz)** parameter on the **Estimation**
tab.

#### Dependency

To enable this port, set the:

- **Input Domain** parameter on the
  **Estimation** tab to
  `Frequency`.
- **Frequency (Hz)** parameter on the
  **Estimation** tab to
  `Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

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

### **VBW** — VBW Value positive scalar

Specify the video bandwidth in Hz through this port. Video bandwidth is
the bandwidth of the lowpass filter that the scope uses to average or smooth
the noise in the signal before displaying it. You can also specify the VBW
value using the **VBW (Hz)** parameter on the
**Estimation** tab.

#### Dependency

To enable this port, set the:

- **Input Domain** parameter on the
  **Estimation** tab to
  `Time`.
- **Averaging Method** parameter on the
  **Estimation** tab to
  `VBW`.
- **VBW (Hz)** parameter on the
  **Estimation** tab to
  `Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Scope Tab

#### Views

### **Spectrum** — Type of spectrum to display `Power` (default) | `Power Density` | `RMS`

Set the type of spectrum to display as one of these values:

- `Power` — Spectrum Analyzer shows the
  power spectrum.
- `Power Density` — Spectrum Analyzer
  shows the power spectral density. The power spectral density is
  the squared magnitude of the spectrum normalized to a bandwidth
  of 1 Hz.
- `RMS` — Spectrum Analyzer shows the
  root mean squared spectrum. Use this option to view the
  frequency of voltage or current signals.

**Tunable:** Yes

#### Dependency

To enable this parameter, set the **Input
Domain** parameter on the
**Estimation** tab to
`Time`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SpectrumType` |
| **Type:** character vector or string scalar |

### **Spectrogram** — Type of spectrogram to display `Power` (default) | `Power Density` | `RMS`

Set the type of spectrogram to display as one of these values:

- `Power` — Spectrum Analyzer shows the
  power spectrogram.
- `Power Density` — Spectrum Analyzer
  shows the power density of the spectrogram. The power
  spectrogram density is the squared magnitude of the spectrogram
  normalized to a bandwidth of 1 Hz.
- `RMS` — Spectrum Analyzer shows the
  root mean square of the spectrogram. The root-mean-square shows
  the square root of the mean square. Use this option to view the
  frequency of voltage or current signals.

**Tunable:** Yes

#### Dependency

To enable this parameter, set the **Input
Domain** parameter on the
**Estimation** tab to
`Time`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SpectrumType` |
| **Type:** character vector or string scalar |

#### Bandwidth

### **Sample Rate (Hz)** — Sample rate the scope uses in Hz `Inherited` (default) | positive scalar

Specify the sample rate the scope uses in Hz as one of the following:

- `Inherited` — Use this option to specify the same
  sample rate as the input signal.
- Positive scalar — The sample rate you specify must be at least twice the
  sample rate of the input signal. Otherwise, you might see unexpected
  behavior when visualizing your signal in the scope due to aliasing.

When the signal frame size changes, the sample rate the scope uses changes
accordingly, which in turn updates the frequency span of the spectrum display. For an example that shows this behavior, see Display Variable-Size Input Signals on Spectrum Analyzer.

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

#### Configuration > Spectrum Analyzer Settings (Gear button)

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

Specify the *y*-axis label in the Spectrum display as
a character vector or a string scalar. To display signal units, add
`(%<SignalUnits>)` to the label. When
simulation starts, Simulink replaces `(%SignalUnits)` with the units
associated with the signals.

For example, for a velocity signal with units of m/s
enter

```
Velocity (%<SignalUnits>)
```

**Tunable:** Yes

#### Dependency

To enable this parameter, select **Spectrum** in
the **Scope** tab.

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

#### Dependency

To enable this parameter, select **Spectrum** in
the **Scope** tab.

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

### **Color Map** — Spectrogram colormap `jet` (default) | `hot` | `bone` | `cool` | `copper` | `gray` | `parula` | three-column matrix

Select a valid colormap name for the spectrogram, or enter a
three-column matrix with values in the range [0,1] defining RGB
triplets. For more information about colormaps, see `colormap`.

**Tunable:** Yes

#### Dependency

To enable this parameter, select **Spectrogram**
in the **Scope** tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Colormap` |
| **Type:** character vector or string scalar |

### **Color Limits** — Color limits of spectrogram [`-80 20`] (default) | [`colorMin colorMax`]

Specify the color limits of the spectrogram as a two-element numeric
vector of the form [`colorMin colorMax`]. The units of
the color limits directly depend upon the **Spectrum
Unit** in the **Spectrogram** tab.

**Tunable:** Yes

#### Dependencies

To enable this parameter, select **Spectrogram**
in the **Scope** tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ColorLimits` |
| **Type:** `double` |

### **Plot Type** — Plot type `Line` (default) | `Stem`

Specify whether to display a `Line` or
`Stem` plot in the Spectrum display.

You can individually control the
type of plot for each channel. To control the type of plot for each
channel, select the channel and set the **Plot Type**
parameter accordingly. *(since R2025a)*

**Tunable:** Yes

#### Dependency

To enable this parameter:

- Select **Spectrum** in the
  **Scope** tab.
- Select the **Normal Trace** check box
  in the **Spectrum** tab.

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

Click the **Legend** button to enable the spectrum
analyzer to display the signal legend. The legend displays the signal
names from the model. For signals with multiple channels, the scope
appends a channel index after the signal name. Continuous signals have
straight lines before their names and discrete signals have step-shaped
lines.

You can control which signals are visible using the legend. To hide a
signal, in the scope legend, click the signal name. To display the
signal, click the signal name again. Alternatively, you can control
which signal is visible using the **Visible** parameter
in the **Spectrum Analyzer Settings** (Gear button).

To display only one signal and hide all other signals, right-click the
name of the signal you want the scope to display. To show all signals,
press **Esc**.

**Note**

The legend displays only the first 20 signals. You cannot view
or control any additional signals from the legend.

**Tunable:** Yes

#### Dependency

To enable the **Legend**, select
**Spectrum** in the **Scope**
tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowLegend` |
| **Type:** `logical` |

### **Colorbar** — Show or hide color bar button

When you select the **Colorbar** button, the
spectrum analyzer shows the color bar.

**Tunable:** Yes

#### Dependencies

To enable the **Colorbar** button, select
**Spectrogram** in the
**Scope** tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowColorbar` |
| **Type:** `logical` |

### **Layout** — Stack axes vertically or horizontally vertical layout (default) | horizontal layout

Stack axes vertically or horizontally by selecting the appropriate
configuration in the layout grid.

**Tunable:** Yes

#### Dependencies

To enable the **Layout**, select
**Spectrum** and
**Spectrogram** in the
**Scope** tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AxesLayout` |
| **Type:** character vector or string scalar |

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

#### Domain

### **Input Domain** — Domain of the input signal `Time` (default) | `Frequency`

The domain of the input signal you want to visualize. If you visualize
time-domain signals, the scope transforms the signal to the frequency
spectrum based on the algorithm you specify in the **Estimation
Method** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputDomain` |
| **Type:** character vector or string scalar |

### **Frequency (Hz)** — Frequency vector `Auto` (default) | `Input port` | monotonically increasing vector

Set the frequency vector which determines the
*x*-axis of the display to one of these values:

- `Auto` — The scope calculates the
  frequency vector from the length of the input. For more
  details, see Frequency Vector.
- `Input port` — You specify the
  frequency vector at the **Frequency** input
  port on the block.
- Custom vector — You specify a custom vector as the
  frequency vector. The length of the custom vector must be
  equal to the frame size of the input signal.

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Input Domain** to
`Frequency`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FrequencyVectorSource`, `FrequencyVector` |
| **Type:** character vector, string scalar, `double` |

### **Input Unit** — Units of frequency input `dBm` (default) | `dBuV` *(since R2023b)* | `dBV` | `dBW` | `Vrms` | `Watts` | `None`

Select the units of the frequency-domain input. This parameter enables
the spectrum analyzer to scale frequency data when you select a
different display unit in the **Spectrum Unit**
parameter in the **Estimation** tab.

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Input Domain** to
`Frequency`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputUnits` |
| **Type:** character vector or string scalar |

#### Frequency Resolution

### **Estimation Method** — Spectrum estimation method `Filter Bank` (default) | `Welch`

Select the spectrum estimation method as one of the following:

- `Filter Bank` — Use an analysis
  filter bank to estimate the power spectrum. Compared to
  Welch's method, this method has a lower noise floor, better
  frequency resolution, lower spectral leakage, and requires
  fewer samples per update.
- `Welch` — Use Welch's method of
  averaged modified periodograms.

For more details on these methods, see Algorithms.

**Tunable:** Yes

#### Dependency

To use this parameter, set **Input Domain** to
`Time`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Method` |
| **Type:** character vector or string scalar |

### **Resolution Method** — Frequency resolution method `RBW` (default) | `Number of frequency bands` | `Window length`

*Since R2024a*

Specify the frequency resolution method of the spectrum analyzer as
one of these options:

- `RBW` — The **RBW
  (Hz)** parameter controls the frequency resolution
  (in Hz) of the analyzer.
- `Number of frequency bands` — Applies
  only when you set **Estimation Method** to
  `Filter bank`. The **FFT
  Length** parameter controls the frequency
  resolution.
- `Window length` — Applies only when
  you set **Estimation Method** to
  `Welch`. The **Window
  Length** parameter controls the frequency
  resolution.

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Input Domain** to
`Time`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FrequencyResolutionMethod` |
| **Type:** character vector or string scalar |

### **Filter Sharpness** — Sharpness of lowpass filter `0.5` (default) | nonnegative scalar in the range [0,1]

Specify the sharpness of the prototype lowpass filter as a real
nonnegative scalar in the range [0,1].

Increasing the filter sharpness decreases the spectral leakage and
gives a more accurate power reading.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Estimation
Method** to `Filter
bank`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FilterSharpness` |
| **Type:** `double` |

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

### **Window Length** — Window length `1024` (default) | integer greater than 2

*Since R2024a*

Specify the window length in samples as an integer greater than 2. The
block uses the window length to compute the spectral estimates. This
parameter controls the frequency resolution.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set:

- **Estimation Method** to
  `Welch`.
- **Resolution Method** to
  `Window Length`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `WindowLength` |
| **Type:**`double` |

### **FFT Length** — Length of FFT `Auto` (default) | `1024` | positive integer

*Since R2024a*

You can set the FFT length to one of these options:

- `Auto` — The value of FFT length
  depends on the setting of the frequency resolution method.
  When you set:

  - **Resolution Method** to
    `RBW`, the FFT length
    equals the number of samples per update,
    *Nsamples*.
    For more details on
    *Nsamples*,
    see the Algorithms section.
  - **Resolution Method** to
    `Window length`, the FFT
    length equals the value you specify in the
    **Window length** parameter or
    1024, whichever is larger.
  - **Resolution Method** to
    `Number of frequency
    bands`, the FFT length equals the
    input frame size (number of rows).
- Positive integer — The number of FFT points equals the
  value you specify in the `FFTLength`
  property.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set:

- **Estimation Method** to
  `Welch`.
- **Estimation Method** to
  `Filter bank` and
  **Resolution Method** to
  `Number of frequency
  bands`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FFTLengthSource`, `FFTLength` |
| **Type:**character vector or string scalar, `double` |

#### Averaging

### **Averaging Method** — Smoothing method `VBW` (default) | `Exponential` | `Running`

Specify the smoothing method as one of these:

- `VBW` — Video bandwidth method.
  The block uses a lowpass filter to smooth the trace and
  decrease the noise. Use the **VBW (Hz)**
  parameter to specify the video bandwidth (VBW) value.
- `Exponential` —
  Weighted average of samples. The block computes the average
  over samples weighted by an exponentially decaying
  forgetting factor. Use the **Forgetting
  Factor** parameter to specify the weighted
  forgetting factor.
- `Running` — Running average
  of the last *Q* samples. Use the
  **Spectral Averages** parameter to
  specify *Q*. *(since R2025a)*

For more information on the averaging methods, see Averaging Method.

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Input Domain** to
`Time`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AveragingMethod` |
| **Type:** character vector or string scalar |

### **VBW (Hz)** — Video bandwidth `Auto` (default) | `Input port` | positive scalar

Specify the video bandwidth as one of the following: S

- `Auto` — The spectrum analyzer adjusts
  the VBW such that the equivalent forgetting factor is
  0.9.
- `Input port` You specify the
  frequency vector at the **VBW** input port
  on the block.
- Positive scalar — You specify a positive scalar. The
  spectrum analyzer adjusts the VBW using this value. The
  value you specify must be less than or equal to
  **Sample Rate (Hz)**/2.

For more details on the video bandwidth method, see Averaging Method.

The spectrum analyzer shows the VBW value in the status bar at the
bottom of the display. To display the VBW value, click the ⋮
icon in the status bar and select `VBW`.

#### Dependency

To enable this parameter, set:

- **Input Domain** to
  `Time`.
- `Averaging Method` to
  `VBW`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VBWSource`, `VBW` |
| **Type:** `double` |

**Tunable:** Yes

### **Forgetting Factor** — Forgetting factor of weighted average method `0.9` (default) | scalar in the range [0,1]

Specify the forgetting factor of the exponential weighted averaging
method as a scalar in the range [0,1].

**Tunable:** Yes

#### Dependency

To enable this parameter, set:

- **Input Domain** to
  `Time`.
- **Averaging Method** to
  `Exponential`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ForgettingFactor` |
| **Type:** `double` |

### **Spectral Averages** — Number of spectral averages `1` (default) | positive integer

*Since R2025a*

Specify the number of spectral averages *Q* as a
positive integer.

The spectrum analyzer computes the current power spectrum estimate by
computing a running average of the last *Q* power
spectrum estimates.

#### Dependency

To enable this parameter, set:

- **Input Domain** to
  `Time`.
- **Averaging Method** to
  `Running`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SpectralAverages` |
| **Type:** `double` |

**Data Types:** `double`

#### Frequency Options

### **Frequency Span** — Frequency span mode `Full` (default) | `Span and Center Frequency` | `Start and Stop Frequencies`

Specify the frequency span mode as one of the following:

- `Full` — The spectrum analyzer
  computes and plots the spectrum over the entire Nyquist Frequency Interval.
- `Span and Center Frequency` — The
  spectrum analyzer computes and plots the spectrum over the
  interval specified by the **Span (Hz)** and
  **Center Frequency (Hz)**
  parameters.
- `Start and Stop Frequencies` — The
  spectrum analyzer computes and plots the spectrum over the
  interval specified by the **Start Frequency
  (Hz)** and **Stop Frequency (Hz)**
  parameters.

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Input Domain** to
`Time`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FrequencySpan` |
| **Type:** character vector or string scalar |

### **Span (Hz)** — Frequency span to compute spectrum in Hz `10e3` (default) | real positive scalar

Specify the frequency span in Hz over which the spectrum analyzer
computes and plots the spectrum. The overall span, defined by this
parameter and the **Center Frequency (Hz)** parameter,
must fall within the Nyquist Frequency Interval. This parameter defines the range of the values
shown on the Frequency axis in the spectrum analyzer window.

**Tunable:** Yes

#### Dependency

To enable this parameter, set:

- **Input Domain** to
  `Time`.
- **Frequency Span** to
  `Span and Center
  Frequency`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Span` |
| **Type:** `double` |

### **Center Frequency (Hz)** — Center of frequency span in Hz `0` (default) | real scalar

Specify the center of the frequency span in Hz over which the spectrum
analyzer computes and plots the spectrum. Use this parameter with the
**Span (Hz)** parameter to define the frequency
span around a center frequency. This parameter defines the midpoint of
the Frequency axis in the spectrum analyzer window.

**Tunable:** Yes

#### Dependency

To enable this parameter, set:

- **Input Domain** to
  `Time`.
- **Frequency Span** to
  `Span and Center
  Frequency`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CenterFrequency` |
| **Type:** `double` |

### **Start Frequency (Hz)** — Start frequency in Hz `-5e3` (default) | scalar

Specify the starting frequency in Hz of the frequency interval over
which the spectrum analyzer computes and plots the spectrum. The overall
span, which is defined by this parameter and the **Stop
Frequency (Hz)** parameter, must fall within the Nyquist Frequency Interval. This parameter defines the leftmost value on the
Frequency axis in the spectrum analyzer window.

**Tunable:** Yes

#### Dependency

To enable this parameter, set:

- **Input Domain** to
  `Time`.
- **Frequency Span** to
  `Start and Stop
  Frequencies`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StartFrequency` |
| **Type:** `double` |

### **Stop Frequency (Hz)** — Stop frequency in Hz `5e3` (default) | scalar

Specify the stop frequency in Hz of the frequency interval over which
the spectrum analyzer computes and plots the spectrum. The overall span,
which is defined by this parameter and the **Start Frequency
(Hz)** parameter, must fall within the Nyquist Frequency Interval. This parameter defines the rightmost value on the
Frequency axis in the spectrum analyzer window.

**Tunable:** Yes

#### Dependency

To enable this parameter, set:

- **Input Domain** to
  `Time`.
- **Frequency Span** to
  `Start and Stop
  Frequencies`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StopFrequency` |
| **Type:** `double` |

#### Window Options

### **Window** — Windowing method `Hann` (default) | `Blackman-Harris` | `Chebyshev` | `Flat Top` | `Hamming` | `Kaiser` | `Rectangular` | custom window function name

Specify the windowing method to apply to the spectrum. Windowing is
used to control the effect of sidelobes in spectral estimation. The
window you specify affects the window length required to achieve a
resolution bandwidth and the required number of samples per update. For
more information about windowing, see Windows.

You can use your own spectral estimation window by directly specifying
a custom window function name in the **Window**
parameter.

**Tunable:** Yes

#### Dependency

To enable this parameter, set:

- **Input Domain** to
  `Time`.
- **Estimation Method** to
  `Welch`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Window`, `CustomWindow` |
| **Type:** character vector or string scalar |

### **Attenuation (dB)** — Sidelobe attenuation in dB `60` (default) | scalar greater than or equal to `45`

Specify the sidelobe attenuation in dB as a scalar greater than or
equal to `45`.

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Window** to
`Chebyshev` or
`Kaiser`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SidelobeAttenuation` |
| **Type:** `double` |

### **Overlap (%)** — Percentage of overlap `0` (default) | scalar in the range [0 100)

Specify the percentage of overlap between the previous and the current
buffered data segments as a scalar in the range [0 100). The overlap
creates a window segment that the scope uses to compute a spectral
estimate. The value must be greater than or equal to zero and less than
100.

**Tunable:** Yes

#### Dependency

To enable this parameter, set:

- **Input Domain** to
  `Time`.
- **Estimation Method** to
  `Welch`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OverlapPercent` |
| **Type:** `double` |

### Measurements Tab

**Note**

To access the phase noise measurement settings, you must have a valid
Mixed-Signal Blockset™ license.

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

#### Phase Noise

### **Phase Noise** — Enable phase noise measurements button

Click the **Phase Noise** button to enable phase
noise measurements. A Phase Noise axis and Phase Noise panel appear in
the scope window when you click this button.

**Note**

To access the phase noise measurement settings, you must have a
valid Mixed-Signal Blockset license.

**Tunable:** Yes

#### Programmatic Use

See `Enabled`.

### **Frequency Offsets (Hz)** — Frequency offsets in Hz [`10 100 1000`] (default) | vector with monotonically increasing values

Specify the frequency offsets in Hz at which the scope measures the
phase noise as a numeric vector with monotonically increasing
values.

**Tunable:** Yes

#### Programmatic Use

See `FrequencyOffset`.

### **Plot Target Phase Noise** — Option to plot target phase noise profile off (default) | on

Select this parameter to plot the target phase noise profile. You can
specify this profile in the **Target Phase Noise
(dBc/Hz)** parameter.

**Tunable:** Yes

#### Programmatic Use

See `PlotTargetPhaseNoise`.

### **Target Phase Noise (dBc/Hz)** — Target phase noise profile in dBc/Hz [`-300 -300 -300`] (default) | vector

Specify the target phase noise profile in dBc/Hz as a numeric vector
of the same length as the **Frequency Offsets (Hz)**
vector.

**Tunable:** Yes

#### Dependencies

To enable this parameter, select the **Plot Target Phase
Noise** parameter.

#### Programmatic Use

See `TargetPhaseNoise`.

### **Label Phase Noise** — Option to label measured phase noise on plot off (default) | on

Select this parameter to label the measured phase noise on the plot.
When you select this parameter, the spectrum analyzer labels the
measured phase noise values on the plot as `SN1`,
`SN2`, and so on.

**Tunable:** Yes

#### Programmatic Use

See `LabelPhaseNoise`.

### Spectrum Tab

**Note**

This tab appears when you select **Spectrum** in the
**Scope** tab.

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
information, see `pwelch`.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PlotAsTwoSidedSpectrum` |
| **Type:** `logical` |

### **Normal Trace** — Normal trace view `on` (default) | `off`

When you select this check box, the spectrum analyzer calculates and
plots the power spectral estimates. The spectrum analyzer performs a
smoothing operation by averaging several spectral estimates and
continues its spectral computations even when you clear this
parameter.

**Tunable:** Yes

#### Dependencies

To clear this check box, first select either the
**Max-Hold Trace** or the **Min-Hold
Trace** parameters.

To enable this parameter, select **Spectrum** in
the **Scope** tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PlotNormalTrace` |
| **Type:** `logical` |

### **Max-Hold Trace** — Maximum hold trace view `off` (default) | `on`

Select this check box to enable the spectrum analyzer to plot the
maximum spectral values of all the estimates. The spectrum analyzer
computes the maximum-hold spectrum at each frequency bin by keeping the
maximum value of all the power spectrum estimates. When you clear this
check box, the spectrum analyzer resets its maximum-hold
computations.

**Tunable:** Yes

#### Dependency

To enable this parameter, select **Spectrum** in
the **Scope** tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PlotMaxHoldTrace` |
| **Type:** `logical` |

### **Min-Hold Trace** — Minimum hold trace view `off` (default) | `on`

Select this check box to enable the spectrum analyzer to plot the
minimum spectral values of all the estimates. The spectrum analyzer
computes the minimum-hold spectrum at each frequency bin by keeping the
minimum value of all the power spectrum estimates. When you clear this
check box, the spectrum analyzer resets its minimum-hold
computations.

**Tunable:** Yes

#### Dependency

To enable this parameter, select **Spectrum** in
the **Scope** tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PlotMinHoldTrace` |
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
or the **Spectrogram** tab (if enabled). If you
select the **Two-Sided Spectrum** check box, then
the **Frequency Scale** parameter is set to
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
- **Spectrum Unit** to any
  option other than `dBFS`
  or `dBFS/Hz`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ReferenceLoad` |
| **Type:** `double` |

### **Spectrum Unit** — Units of the spectrum `dBm` (default) | `dBFS` | `dBV` | `dBuV` *(since R2023b)* | `dBW` | `Vrms` | `Watts` | `dBm/Hz` | `dBW/Hz` | `dBFS/Hz` | `Watts/Hz` | `Auto`

Specify the units in which the spectrum analyzer displays the power
values as one of the following:

- `dBm`
- `dBFS`
- `dBuV` *(since R2023b)*
- `dBV`
- `dBW`
- `Vrms`
- `Watts`
- `dBm/Hz`
- `dBW/Hz`
- `dBFS/Hz`
- `Watts/Hz`
- `Auto`

**Tunable:** Yes

#### Dependency

The units available depend on the value you choose for the
**Spectrum** parameter in the
**Scope** tab.

| Estimation tab > Input Domain parameter | Scope tab > Spectrum option | Available Units |
| --- | --- | --- |
| `Time` | `Power` | `dBm`, `dBW`, `dBFS`, `Watts` |
| `Power Density` | `dBm/Hz`, `dBW/Hz`,`dBFS/Hz`, `Watts/Hz` |
| `RMS` | `dBuV` *(since R2023b)*, `dBV`, `Vrms` |
| `Frequency` | ― | `Auto`, `dBm`, `dBuV` *(since R2023b)*, `dBV`, `dBW`, `Vrms`, `Watts` |

If you set the **Input Domain** parameter to
`Frequency` and the **Spectrum
Unit** parameter to `Auto`,
the spectrum analyzer assumes the spectrum units to be equal to
input units specified in the **Estimation** tab >
**Input Unit** parameter. If you set the
**Input Domain** parameter to
`Time` and the **Spectrum
Unit** parameter to any option other than
`Auto`, the spectrum analyzer converts
the units specified in the **Input Unit** parameter
to the units specified in the **Spectrum Unit**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SpectrumUnits` |
| **Type:** character vector or string scalar |

### **Full Scale** — Full scale for dBFS units `Auto` (default) | positive real scalar

The full scale used for the decibel full scale (dBFS) units. By
default, the spectrum analyzer uses the entire spectrum scale. Specify a
positive real scalar for the dBFS full scale.

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- In the **Scope** tab, set the
  spectrum type to `Power` or
  `Power Density`.
- In the **Estimation** tab, set
  **Input Domain** to
  `Time`.
- In the **Spectrum** tab, set
  **Spectrum Unit** to
  `dBFS` or
  `dBFS/Hz` (when spectrum
  type is set to `Power
  Density`).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FullScale` |
| **Type:** `double` |

### Spectrogram Tab

**Note**

This tab appears when you select **Spectrogram** in the
**Scope** tab.

#### Channel

### **Channel** — Channel for which spectrogram is plotted `1` (default) | character vector of a positive integer | string scalar of a positive integer

Select the signal channel for which the spectrogram settings
apply.

**Tunable:** Yes

#### Dependency

To enable this parameter, select **Spectrogram**
in the **Scope** tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SpectrogramChannel` |
| **Type:** character vector, string scalar, `double` |

#### Time Options

### **Time Resolution (s)** — Time resolution in seconds `Auto` (default) | positive scalar

Time resolution is the amount of data, in seconds, used to compute a
spectrogram line. The minimum attainable resolution is the amount of
time it takes to compute a single spectral estimate. The tooltip
displays the minimum attainable resolution given the current spectrum
analyzer settings.

When you set **RBW (Hz)** and **Time
Resolution (s)** to `Auto`, then
the spectrum analyzer adjusts the RBW value such that there are 1024 RBW
intervals in one frequency span and sets the time resolution is set to
1/`RBW`.

When you set **RBW (Hz)** to
`Auto` and **Time Resolution
(s)** to a positive scalar, then time resolution becomes
the main control and RBW is set to 1/**Time Resolution
(s)** Hz.

When you set **RBW (Hz)** to a positive scalar and
**Time Resolution (s)** to
`Auto`, then RBW becomes the main control
and the time resolution is set 1/**RBW (Hz)** s.

When you set **RBW (Hz)** and **Time
Resolution (s)** to a positive value, then time resolution
must be equal to or larger than the minimum attainable time resolution
defined by 1/**RBW (Hz)**. Several spectral estimates
are combined into one spectrogram line to obtain the desired time
resolution. Interpolation is used to obtain time resolution values that
are not integer multiples of 1/**RBW (Hz)**.

**Tunable:** Yes

#### Dependency

To enable this parameter, select **Spectrogram**
in the **Scope** tab and set **Input
Domain** to `Time` in the
**Estimation** tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TimeResolutionSource`, `TimeResolution` |
| **Type:** character vector, string scalar, `double` |

### **Time Span (s)** — Time span in seconds `Auto` (default) | positive scalar

The time span over which the spectrum analyzer displays the
spectrogram specified as a positive scalar in seconds. The time span is
the product of the desired number of spectral lines and the time
resolution. When you set this parameter to
`Auto`, the spectrogram displays 100
spectrogram lines at any given time. Otherwise, the spectrogram uses the
time duration you specify in this parameter. The time span that you
specify must be at least two times larger than the duration of the
number of samples required for a spectral update.

**Tunable:** Yes

#### Dependency

To enable this parameter, select **Spectrogram**
in the **Scope** tab and set **Input
Domain** to `Time` in the
**Estimation** tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TimeSpanSource`, `TimeSpan` |
| **Type:** character vector, string scalar, `double` |

For more information on `Two-Sided Spectrum`, see Spectrum Tab > Trace Options.

### Spectral Mask Tab

**Note**

This tab appears when you select **Spectrum** in the
**Scope** tab and set the **Spectrum**
type to be `Power` or `Power
Density`.

#### Views

### **Upper Mask** — Enable upper spectral mask button

Select **Upper Mask** to display the upper mask in
the spectrum plot. The **Spectral Mask** panel appears
at the bottom of the spectrum analyzer window and displays mask details,
such as number of times a mask succeeded, number of times a mask failed,
channels causing the mask failure, and so on.

Use the **Upper Limits** parameter to specify the
upper mask. If the entire spectrum plot is below the upper mask, the
upper mask looks green. In all other cases, the upper mask looks
red.

**Tunable:** Yes

#### Programmatic Use

See `EnabledMasks`.

### **Lower Mask** — Enable lower spectral mask button

Select **Lower Mask** to display the lower mask in
the spectrum plot. The **Spectral Mask** panel appears
at the bottom of the spectrum analyzer window and displays mask details,
such as number of times a mask succeeded, number of times a mask failed,
channels causing the mask failure, and so on.

Use the **Lower Limits** parameter to specify the
lower mask. If the entire spectrum plot is above the lower mask, the
lower mask looks green. In all other cases, the lower mask looks
red.

**Tunable:** Yes

#### Programmatic Use

See `EnabledMasks`.

#### Configuration

### **Upper Limits** — Limit for upper spectral mask `Inf` (default) | scalar | two-column matrix

Specify the limit for the upper spectral mask as a scalar or a
two-column matrix.

If `UpperMask` is a scalar, the upper limit mask
uses the same power value for all frequencies specified in the spectrum
analyzer.

If you specify a matrix, the first column contains the frequency
values (Hz), which correspond to the *x*-axis values.
The second column contains the power values, which correspond to the
associated *y*-axis values.

To apply offsets to the power and frequency values, use the
**Reference Level (dBr)** and the
**Frequency Offset (Hz)** parameters.

**Tunable:** Yes

#### Programmatic Use

See `UpperMask`.

### **Lower Limits** — Limit for lower spectral mask `-Inf` (default) | scalar | two-column matrix

Specify the limit for the lower spectral mask as a scalar or a
two-column matrix.

If `LowerMask` is a scalar, the lower limit mask
uses the same power value for all frequencies specified in the spectrum
analyzer.

If you specify a matrix, the first column contains the frequency
values (Hz), which correspond to the *x*-axis values.
The second column contains the power values, which correspond to the
associated *y*-axis values.

To apply offsets to the power and frequency values, use the
**Reference Level (dBr)** and the
**Frequency Offset (Hz)** parameters.

**Tunable:** Yes

#### Programmatic Use

See `LowerMask`.

### **Reference Level (dBr)** — Reference level for mask power values `0` (default) | real scalar | `Spectrum peak`

Specify the reference level for mask power values as a numeric scalar
or set it to `Spectrum peak`.

When you set **Reference Level (dBr)** to a scalar
value, the spectrum analyzer uses this value as the reference to the
power values (in dBr) for the upper mask and the lower mask of the
spectrum analyzer. The reference level should have the same units as the
**Spectrum Unit** parameter in the
**Spectrum** tab.

When you set **Reference Level (dBr)** to
`Spectrum peak`, the spectrum analyzer uses
the peak value of the current spectrum of the
**Channel** in the **Spectral
Mask** tab as the reference power value.

**Tunable:** Yes

#### Programmatic Use

See `ReferenceLevel` and `CustomReferenceLevel`.

### **Channel** — Input channel with peak spectrum `1` (default) | integer

Select the input channel which the spectrum analyzer uses to determine
the mask reference level. The peak value of the spectrum in this channel
becomes the mask reference level when you set the **Reference
Level (dBr)** parameter to `Spectrum
peak`.

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Reference Level
(dBr)** to `Spectrum peak` and
display some data on the scope.

#### Programmatic Use

See `SelectedChannel`.

### **Frequency Offset (Hz)** — Frequency offset in Hz `0` (default) | finite numeric scalar

Specify the frequency offset in Hz as a finite numeric scalar. Using
this value, the spectrum analyzer offsets the frequency values in the
**Upper Mask** and the **Lower
Mask** parameters.

**Tunable:** Yes

#### Programmatic Use

See `MaskFrequencyOffset`.

### Channel Measurements Tab

**Note**

This tab appears when you select **Spectrum** in the
**Scope** tab.

#### Channel

### **Channel** — Channel for computing occupied bandwidth and adjacent channel power ratio `1` (default) | positive integer

Specify the channel over which the spectrum analyzer computes and
displays the occupied bandwidth and adjacent channel power ratio as a
positive integer in the range [1 *N*], where
*N* is the number of input channels.

**Tunable:** Yes

#### Dependency

To enable this parameter, pass data through the scope.

#### Programmatic Use

See `MeasurementChannel`.

#### Channel Measurements

### **Channel Measurements** — Enable channel measurements button

Click **Channel Measurements** to enable channel
measurements.

**Tunable:** Yes

#### Programmatic Use

See `Enabled`.

### **Type** — Type of measurement data to display `Occupied BW` (default) | `ACPR`

Specify the type of measurement data to display as
`Occupied BW` or
`ACPR`.

**Tunable:** Yes

#### Programmatic Use

See `Type`.

### **Occupied BW (%)** — Percentage of power to compute occupied bandwidth `99` (default) | positive scalar

Specify the percentage of power over which the spectrum analyzer
computes the occupied bandwidth as a positive scalar.

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Type** to
`Occupied BW`.

#### Programmatic Use

See `PercentOccupiedBW`.

#### Frequency Options

### **Frequency Span** — Frequency span mode `Span and Center Frequency` (default) | `Start and Stop Frequencies`

Specify the frequency span mode as one of the following:

- `Span and Center Frequency` —
  Measure over a frequency range specified in **Span
  (Hz)** and around the frequency value specified
  in **Center Frequency (Hz)**.
- `Start and Stop Frequencies` —
  Measure over the frequency range [**Start Frequency
  (Hz)**, **Stop Frequency
  (Hz)**].

**Tunable:** Yes

#### Programmatic Use

See `FrequencySpan`.

### **Span (Hz)** — Frequency span in Hz `2000` (default) | positive scalar

Specify the frequency span over which the spectrum analyzer computes
the channel measurements as a positive scalar in Hz.

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Frequency Span**
to `Span and Center Frequency`.

#### Programmatic Use

See `Span`.

### **Center Frequency (Hz)** — Center frequency of span in Hz `0` (default) | real scalar

Center frequency of the span over which the object computes the
channel measurements, specified as a real scalar in Hz.

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Frequency Span**
to `Span and Center Frequency`.

#### Programmatic Use

See `CenterFrequency`.

### **Start Frequency (Hz)** — Start frequency in Hz `-1000` (default) | real scalar

Specify the start frequency in Hz over which the spectrum analyzer
computes the channel measurements.

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Frequency Span**
to `Start and Stop Frequencies`.

#### Programmatic Use

See `StartFrequency`.

### **Stop Frequency (Hz)** — Stop frequency in Hz `1000` (default) | real scalar

Specify the stop frequency in Hz over which the spectrum analyzer
computes the channel measurements.

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Frequency Span**
to `Start and Stop Frequencies`.

#### Programmatic Use

See `StopFrequency`.

#### Adjacent Channels

### **Num Pairs** — Number of adjacent channel pairs `2` (default) | positive integer in range [`1`, `12`]

Specify the number of adjacent channel pairs as a positive integer in
the range [`1`, `12`].

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Type** to
`ACPR`.

#### Programmatic Use

See `NumOffsets`.

### **Offsets (Hz)** — ACPR offsets in Hz `[2000 3500]` (default) | vector

Specify the frequency of the adjacent channel relative to the center
frequency of the main channel as a real vector of length equal to the
number of offset pairs specified in **Num
Pairs**.

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Type** to
`ACPR`.

#### Programmatic Use

See `ACPROffsets`.

### **Adjacent BW (Hz)** — Adjacent channel bandwidth in Hz `1000` (default) | positive scalar

Specify the adjacent channel bandwidth in Hz as a positive
scalar.

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Type** to
`ACPR`.

#### Programmatic Use

See `AdjacentBW`.

### **Filter Shape** — Filter shape `None` (default) | `RRC` | `Gaussian`

Specify the filter shape for the main and adjacent channels as
`None`, `RRC`, or
`Gaussian`.

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Type** to
`ACPR`.

#### Programmatic Use

See `FilterShape`.

### **Roll-off Factor** — Roll-off factor `0.5` (default) | real scalar in range [`0`, `1`]

Specify the roll-off factor as a real scalar in the range
[`0`, `1`].

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Type** to
`ACPR` and **Filter
Shape** to `RRC`.

#### Programmatic Use

See `FilterCoeff`.

### **BT Product** — BT product `0.5` (default) | real scalar in range [`0`, `1`]

Specify the BT product as a real scalar in the range
[`0`, `1`].

**Tunable:** Yes

#### Dependency

To enable this parameter, set **Type** to
`ACPR` and **Filter
Shape** to `Gaussian`.

#### Programmatic Use

See `FilterCoeff`.

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

DSP System Toolbox / Sinks Audio Toolbox / Sinks DSP System Toolbox HDL Support / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block can be used for simulation visibility in systems that generate code,
but is not included in the generated code.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic. See also Generate HDL Code with Annotations or Comments (HDL Coder) and Integrate Custom HDL Code by Using DocBlock (HDL Coder).

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `No HDL` | Do not generate HDL code for this block. |

**HDL Block Properties**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | Control the removal of unconnected logic. The default is `off`, which means unconnected logic is not preserved in HDL code. For more details, see PreserveUpstreamLogic (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

This block can be used for simulation visibility in systems that generate PLC
code, but is not included in the generated code.

## Version History

**Introduced in R2014b**

### R2025a: Control plot type for each line individually

You can now individually control the type of plot for each line. To control the type of plot
for a line, select the line and set the **Plot Type**
parameter accordingly.

### R2025a: New phase noise measurements in Spectrum Analyzer block

You can now measure and plot the phase noise of a signal using the Spectrum
Analyzer block.

To enable the phase noise measurements in the Spectrum Analyzer
window, click the **Measurements** tab on the scope toolstrip and
then click the **Phase Noise** button.

**Note**

To access the phase noise measurement settings, you must have a valid
Mixed-Signal Blockset license.

### R2025a: Support for running averaging method

The Spectrum Analyzer block now supports the running averaging
method to compute the power spectrum estimate. To enable this mode, set the
**Averaging Method** parameter in the
**Estimation** tab to `Running` and
the **Spectral Averages** parameter to a positive integer.

For more information, see the Algorithms
section.

### R2024b: Display spectral data for any number of input samples and adjust RBW accordingly

Previously, the Spectrum Analyzer block required a minimum number of samples to
update the display for a given RBW value. Starting in R2024b, this limitation is
removed. The scope now updates its display for any number of input samples and
adjusts the RBW value accordingly.

### R2024b: Auto adjust RBW to maintain 1024 samples

The Spectrum Analyzer block can now automatically adjust the resolution bandwidth (RBW) so as
to maintain the number of samples per spectral update at 1024 (*Nsamples* =
1024) irrespective of the window you select.

To enable this mode in the Spectrum Analyzer block, set:

- **Estimation Method** to
  `Welch`.
- **Resolution Method** to
  `RBW`.
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

### R2024a: Specify window length and FFT length

You can now specify the window length and FFT length in the spectrum analyzer
under certain conditions. These parameters are available starting R2024a:

- **Resolution Method**
- **Window Length**
- **FFT Length**

### R2023b: Spectrum Analyzer supports `dBuV` units

You can set **Spectrum Unit** to `dBuV`
when you set:

- **Input Domain** to `Time`
  and **Spectrum** to `RMS`.
- **Input Domain** to
  `Frequency`.

You can set **Input Unit** to `dBuV`
when you set **Input Domain** to
`Frequency`.

### R2023a: Spectrum Analyzer with improved responsiveness and toolstrip interface in Simulink

In R2023a, the Spectrum Analyzer block is more responsive and its
toolstrip interface is improved to provide you easy access to spectral analysis,
estimation, and measurements. You can configure and display Spectrum Analyzer
settings from the command line with the `SpectrumAnalyzerBlockConfiguration` object.

## Description

Display frequency spectrum

The Spectrum Analyzer block, referred to here as the scope, displays
frequency-domain signals and the frequency spectrum of time-domain signals. The scope
shows the spectrum view and the spectrogram view. The block algorithm performs spectral
estimation using the filter bank method and Welch's method of averaged modified
periodograms. You can customize the spectrum analyzer display to show the data and the
measurement information that you need. For more details, see Algorithms.

Snapshot of spectrum analyzer scope showing both the spectrum and the Spectrogram.

You can use the Spectrum Analyzer block in models running in
`Normal` or `Accelerator`
simulation modes. You can also use the Spectrum Analyzer block in models
running in `Rapid Accelerator` or
`External` simulation modes with some limitations.

You can use the Spectrum Analyzer block inside all subsystems and conditional
subsystems. *Conditional subsystems* include enabled subsystems,
triggered subsystems, enabled and triggered subsystems, and function-call subsystems.
See Conditionally Executed Subsystems Overview (Simulink) for more
information.

### Measurements

- Cursor Measurements — Measure signal
  values using vertical and horizontal cursors.
- Peak Finder Measurements — Find maxima
  and show the *x*-axis values at which they
  occur.
- Channel Measurements — Measure the
  occupied bandwidth or adjacent channel power ratio (ACPR).
- Distortion Measurements — Measure
  harmonic distortion and intermodulation distortion.
- Spectral Mask — Visualize
  spectrum limits and compare spectrum values to specification values.

### Programmatic Control

Configure and display the spectrum analyzer settings from the command line with
the `SpectrumAnalyzerBlockConfiguration`
object.
