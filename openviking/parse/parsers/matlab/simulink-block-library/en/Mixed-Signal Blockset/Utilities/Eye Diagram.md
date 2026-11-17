---
type: simulink-block
title: 'Eye Diagram'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'legacyeyediagramscope'
documentation_source_path: 'ref/legacyeyediagramscope.html'
language: en
---

# Eye Diagram

## Ports
```yaml
ports:
- name: In
  summary: Input signal scalar | column vector
  direction: input
  data_types: double
```

### Input

### **In** — Input signal scalar | column vector

Input signal, specified as a scalar or column vector.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Display mode
  summary: Display mode Line plot (default) | 2D color Histogram
  group: Main Tab
- name: Enable measurements
  summary: Enable measurements off (default) | on
  group: Main Tab
- name: Show horizontal (jitter) histogram
  summary: Display jitter histogram off (default) | on
  group: Main Tab
- name: Show vertical (noise) histogram
  summary: Display noise histogram off (default) | on
  group: Main Tab
- name: Do not show horizontal or vertical histogram
  summary: Do not show horizontal or vertical histogram on (default) | off
  group: Main Tab
- name: Show horizontal bathtub curve
  summary: Show horizontal bathtub curve off (default) | on
  group: Main Tab
- name: Show vertical bathtub curve
  summary: Show vertical bathtub curve off (default) | on
  group: Main Tab
- name: Eye diagram to display
  summary: Eye diagram to display Real only (default) | Real and imaginary
  group: Main Tab
- name: Color fading
  summary: Color fading off (default) | on
  group: Main Tab
- name: Samples per symbol
  summary: Samples per symbol 8 (default) | positive integer
  group: Main Tab
- name: Sample offset
  summary: Sample offset 0 (default) | nonnegative integer
  group: Main Tab
- name: Symbols per trace
  summary: Symbols per trace 2 (default) | positive integer
  group: Main Tab
- name: Traces to display
  summary: Number of traces to display 40 (default) | positive integer
  group: Main Tab
- name: Title
  summary: Title label *None* (default)
  group: Axes Tab
- name: Show grid
  summary: Toggle scope grid on (default) | off
  group: Axes Tab
- name: Y-limits (Minimum)
  summary: Lower limit of *y*-axis -1.1 (default) | scalar
  group: Axes Tab
- name: Y-limits (Maximum)
  summary: Upper limit of *y*-axis 1.1 (default) | scalar
  group: Axes Tab
- name: Real axis label
  summary: Real axis label Real Amplitude (default)
  group: Axes Tab
- name: Imaginary axis label
  summary: Imaginary axis label Imaginary Amplitude (default)
  group: Axes Tab
- name: Oversampling method
  summary: Oversampling method None (default) | Input interpolation | Histogram interpolation
  group: 2D Histogram Tab
- name: Color scale
  summary: Color scale Linear (default) | Logarithmic
  group: 2D Histogram Tab
- name: Export measurements, histograms and bathtub curves
  summary: Export measurements, histograms and bathtub curves Off (default) | off
  group: Export Tab
- name: Variable name
  summary: Variable name EyeData (default)
  group: Export Tab
- name: Figure color
  summary: Figure color black (default)
  group: Style Dialog Box
- name: Axes colors
  summary: Axes colors black | gray (default)
  group: Style Dialog Box
- name: Line
  summary: Line style, thickness and color for line plots continuous | 0.5 | yellow (default)
  group: Style Dialog Box
- name: Marker
  summary: Data point marker None (default) | ...
  group: Style Dialog Box
- name: Colormap
  summary: Colormap for histograms Hot (default) | Parula | Jet | HSV | Cool | Spring Summer | Autumn | Winter | Gray | Bone
    | Copper | Pink | Lines | Custom
  group: Style Dialog Box
- name: Eye level boundaries
  summary: Time range for calculating eye levels [40 60] (default) | two-element vector
  group: Measurement Settings Pane
- name: Decision boundary
  summary: Amplitude level threshold 0 (default) | scalar
  group: Measurement Settings Pane
- name: Rise/Fall thresholds
  summary: Amplitude levels of the rise and fall transitions [10 90] (default) | two-element vector
  group: Measurement Settings Pane
- name: Hysteresis
  summary: Amplitude tolerance of the horizontal crossings 0 (default) | scalar
  group: Measurement Settings Pane
- name: BER threshold
  summary: BER used for eye measurements 1e-12 (default) | nonnegative scalar from 0 to 0.5
  group: Measurement Settings Pane
- name: Bathtub BERs
  summary: BER values used to calculate openings of bathtub curves [0.5 0.1 0.01 0.001 0.0001 1e-05 1e-06 1e-07 1e-08 1e-09
    1e-10 1e-11 1e-12] (default) | vector
  group: Measurement Settings Pane
- name: Measurement delay
  summary: Duration of initial data discarded from measurements 0 (default) | nonnegative scalar
  group: Measurement Settings Pane
```

### Main Tab

### **Display mode** — Display mode `Line plot` (default) | `2D color Histogram`

Display mode of the eye diagram, specified as `Line
plot` or `2D color histogram`.
Selecting `2D color histogram` makes the
histogram tab available.

**Tunable:** Yes

### **Enable measurements** — Enable measurements `off` (default) | `on`

Select this check box to enable eye measurements of the input signal.

### **Show horizontal (jitter) histogram** — Display jitter histogram `off` (default) | `on`

Select this radio button to display the jitter histogram. This can
also be accessed by using the histogram button drop down on the
toolbar.

#### Dependencies

This parameter is available when **Display mode**
is `2D color histogram` and
**Enable measurements** is selected.

### **Show vertical (noise) histogram** — Display noise histogram `off` (default) | `on`

Select this radio button to display the noise histogram. This can also
be accessed by using the histogram button drop down on the
toolbar.

#### Dependencies

This parameter is available when **Display mode**
is `2D color histogram` and
**Enable measurements** is selected.

### **Do not show horizontal or vertical histogram** — Do not show horizontal or vertical histogram `on` (default) | `off`

Select this radio button to display neither the histogram noise nor
the histogram jitter.

#### Dependencies

This parameter is available when **Display mode**
is `2D color histogram` and
**Enable measurements** is selected.

### **Show horizontal bathtub curve** — Show horizontal bathtub curve `off` (default) | `on`

Select this check box to display the horizontal bathtub curve. This
can also be accessed by using the bathtub curve button on the
toolbar.

#### Dependencies

This parameter is available when **Enable
measurements** is selected.

### **Show vertical bathtub curve** — Show vertical bathtub curve `off` (default) | `on`

Select this check box to display the vertical bathtub curve. This can
also be accessed by using the bathtub curve button on the
toolbar.

#### Dependencies

This parameter is available when **Enable
measurements** is selected.

### **Eye diagram to display** — Eye diagram to display `Real only` (default) | `Real and imaginary`

Select either `Real only` or
`Real and imaginary` to display one or both
eye diagrams. To make eye measurements, this parameter must be
`Real only`.

**Tunable:** Yes

### **Color fading** — Color fading `off` (default) | `on`

Select this check box to fade the points in the display as the
interval of time after they are first plotted increases.

**Tunable:** Yes

#### Dependencies

This parameter is available only when the **Display
mode** is `Line plot`.

### **Samples per symbol** — Samples per symbol 8 (default) | positive integer

Number of samples per symbol, specified as a positive integer. Use
with **Symbols per trace** to determine the number of
samples per trace.

**Tunable:** Yes

### **Sample offset** — Sample offset 0 (default) | nonnegative integer

Sample offset, specified as a nonnegative integer smaller than the
product of **Samples per symbol** and **Symbols
per trace**. The offset provides the number of samples to
omit before plotting the first point.

**Tunable:** Yes

### **Symbols per trace** — Symbols per trace 2 (default) | positive integer

Number of symbols plotted per trace, specified as a positive
integer.

**Tunable:** Yes

### **Traces to display** — Number of traces to display 40 (default) | positive integer

Number of traces plotted, specified as a positive integer.

**Tunable:** Yes

#### Dependencies

This parameter is available only when the **Display
mode** is `Line plot`

### Axes Tab

### **Title** — Title label *None* (default)

Label that appears above the eye diagram plot.

**Tunable:** Yes

### **Show grid** — Toggle scope grid `on` (default) | `off`

Toggle this check box to turn the grid on and off.

**Tunable:** Yes

### **Y-limits (Minimum)** — Lower limit of *y*-axis `-1.1` (default) | scalar

Minimum value of the *y*-axis.

**Tunable:** Yes

### **Y-limits (Maximum)** — Upper limit of *y*-axis `1.1` (default) | scalar

Maximum value of the *y*-axis.

**Tunable:** Yes

### **Real axis label** — Real axis label `Real Amplitude` (default)

Text that the scope displays along the real axis.

**Tunable:** Yes

### **Imaginary axis label** — Imaginary axis label `Imaginary Amplitude` (default)

Text that the scope displays along the imaginary axis.

**Tunable:** Yes

### 2D Histogram Tab

The 2D histogram tab is available when you click the histogram button or when the
display mode is set to `2D color histogram`.

### **Oversampling method** — Oversampling method `None` (default) | `Input interpolation` | `Histogram interpolation`

Oversampling method, specified as `None`,
`Input interpolation`, or
`Histogram interpolation`.

To plot eye diagrams as quickly as possible, set the
**Oversampling method** to
`None`. The drawback to not oversampling is
that the plots look pixelated when the number of samples per trace is
small. To create smoother, less-pixelated plots using a small number of
samples per trace, set the **Oversampling method** to
`Input interpolation` or
`Histogram interpolation`.
`Input interpolation` is the faster of the
two interpolation methods and produces good results when the
signal-to-noise ratio (SNR) is high. With a lower SNR, this oversampling
method is not recommended because it introduces a bias to the centers of
the histogram ranges. `Histogram interpolation`
is not as fast as the other techniques, but it provides good results
even when the SNR is low.

**Tunable:** Yes

### **Color scale** — Color scale `Linear` (default) | `Logarithmic`

Color scale of the histogram plot, specified as either
`Linear` or
`Logarithmic`. Set **Color
scale** to `Logarithmic` if
certain areas of the eye diagram include a disproportionate number of
points.

**Tunable:** Yes

The toolbar contains a histogram reset button , which resets the internal histogram buffers and clears the
display. This button is not available when the display mode is set to
`Line plot`.

### Export Tab

### **Export measurements, histograms and bathtub curves** — Export measurements, histograms and bathtub curves `Off` (default) | `off`

Select this check box export the eye diagram measurements to the
MATLAB® workspace.

**Tunable:** Yes

### **Variable name** — Variable name `EyeData` (default)

Specify the name of the variable to which the eye diagram measurements
are saved. The data is saved as a structure having these fields:

- `MeasurementSettings`
- `Measurements`
- `JitterHistogram`
- `NoiseHistogram`
- `HorizontalBathtub`
- `VerticalBathtub`
- `BlockName`

**Tunable:** Yes

### Style Dialog Box

In the **Style** dialog box, you can customize the style of the
active display. You can change the color of the figure containing the displays, the
background and foreground colors of display axes, and properties of lines in a
display. To open this dialog box, select **View** > **Style**.

### **Figure color** — Figure color `black` (default)

Specify the background color of the scope figure.

### **Axes colors** — Axes colors `black` | `gray` (default)

Specify the fill and line colors for the axes.

### **Line** — Line style, thickness and color for line plots `continuous` | `0.5` | `yellow` (default)

Specify the line style, line width, and line color for the displayed
signal.

#### Dependencies

This parameter is available only when the **Display
mode** is `Line plot`.

### **Marker** — Data point marker `None` (default) | ...

Data point marker for the selected signal, specified as one of the
choices in this table data point markers. This parameter is similar to
the `Marker` property for MATLAB
Handle Graphics® plot objects.

| Specifier | Marker Type |
| --- | --- |
| none | No marker (default) |
|  | Circle |
|  | Square |
|  | Cross |
|  | Point |
|  | Plus sign |
|  | Asterisk |
|  | Diamond |
|  | Downward-pointing triangle |
|  | Upward-pointing triangle |
|  | Left-pointing triangle |
|  | Right-pointing triangle |
|  | Five-pointed star (pentagram) |
|  | Six-pointed star (hexagram) |

#### Dependencies

This parameter is available only when the **Display
mode** is `Line plot`.

### **Colormap** — Colormap for histograms `Hot` (default) | `Parula` | `Jet` | `HSV` | `Cool` | `Spring` `Summer` | `Autumn` | `Winter` | `Gray` | `Bone` | `Copper` | `Pink` | `Lines` | `Custom`

Specify the colormap of the histogram plots as one of these schemes:
`Parula`, `Jet`,
`HSV`, `Hot`,
`Cool`, `Spring`,
`Summer`,
`Autumn`, `Winter`,
`Gray`, `Bone`,
`Copper`, `Pink`,
`Lines`, or
`Custom`. If you select
`Custom`, a dialog box pops up from which you can
enter code to specify your own colormap.

#### Dependencies

This parameter is available only when the **Display
mode** is `2D color
histogram`.

### Measurement Settings Pane

To change measurement settings, first select **Enable
measurements**. Then, in the **Eye Measurements**
pane, click the arrow next to **Settings**. You can control these
measurement settings.

### **Eye level boundaries** — Time range for calculating eye levels `[40 60]` (default) | two-element vector

Time range for calculating eye levels, specified as a two-element
vector. These values are expressed as a percentage of the symbol
duration.

**Tunable:** Yes

### **Decision boundary** — Amplitude level threshold `0` (default) | scalar

Amplitude level threshold in V, specified as a scalar. This parameter
separates the different signaling regions for horizontal (jitter)
histograms. This parameter is tunable, but the jitter histograms reset
when the parameter changes.

For non-return-to-zero (NRZ) signals, set **Decision
boundary** to 0. For return-to-zero (RZ) signals, set
**Decision boundary** to half the maximum
amplitude.

**Tunable:** Yes

### **Rise/Fall thresholds** — Amplitude levels of the rise and fall transitions `[10 90]` (default) | two-element vector

Amplitude levels of the rise and fall transitions, specified as a
two-element vector. These values are expressed as a percentage of the
eye amplitude. This parameter is tunable, but the crossing histograms of
the rise and fall thresholds reset when the parameter changes.

**Tunable:** Yes

### **Hysteresis** — Amplitude tolerance of the horizontal crossings `0` (default) | scalar

Amplitude tolerance of the horizontal crossings in V, specified as a
scalar. Increase hysteresis to provide more tolerance to spurious
crossings due to noise. This parameter is tunable, but the jitter and
the rise and fall histograms reset when the parameter changes.

**Tunable:** Yes

### **BER threshold** — BER used for eye measurements `1e-12` (default) | nonnegative scalar from 0 to 0.5

BER used for eye measurements, specified as a nonnegative scalar from
0 to 0.5. The value is used to make measurements of random jitter, total
jitter, horizontal eye openings, and vertical eye openings.

**Tunable:** Yes

### **Bathtub BERs** — BER values used to calculate openings of bathtub curves `[0.5 0.1 0.01 0.001 0.0001 1e-05 1e-06 1e-07 1e-08 1e-09 1e-10 1e-11 1e-12]` (default) | vector

BER values used to calculate openings of bathtub curves, specified as
a vector whose elements range from 0 to 0.5. Horizontal and vertical eye
openings are calculated for each of the values specified by this
parameter.

**Tunable:** Yes

#### Dependencies

To enable this parameter, select **Show horizontal bathtub
curve**, **Show vertical bathtub
curve**, or both.

### **Measurement delay** — Duration of initial data discarded from measurements `0` (default) | nonnegative scalar

Duration of initial data discarded from measurements, in seconds,
specified as a nonnegative scalar.
## Libraries

Communications Toolbox / Comm Sinks Communications Toolbox HDL Support / Comm Sinks Mixed-Signal Blockset / Utilities SerDes Toolbox / Utilities

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

This block is excluded from the generated code when code generation is performed on a system containing this block.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

This block can be used for simulation visibility in subsystems
that generate HDL code, but is not included in the hardware implementation.

## Version History

**Introduced in R2014a**

### R2025a: Eye diagram analysis has been removed

Eye diagram analysis, such as measurements, histograms, and bathtub curves, have be
removed from the Eye Diagram block. To
access these functionalities you need licenses to Signal Integrity
Toolbox™, SerDes Toolbox™, or Mixed-Signal Blockset™.

- Use the `eyeDiagramSI` (Signal Integrity Toolbox) system object, Eye
  Measurement (Signal Integrity Toolbox) block, `eyeContour` (Signal Integrity Toolbox) object, and `eyeMask` (Signal Integrity Toolbox)object to measure eye diagram metrics such as eye height,
  width, area, linearity, vertical eye closure (VEC), and channel operating
  margin (COM).
- For the new eye diagram block in Communications Toolbox™, see Eye Diagram.

### R2023b: Eye diagram analysis will be removed

Eye diagram analysis, such as measurements, histograms, and bathtub curves, will be
removed from the Eye Diagram block in a
future release. To access these functionalities:

- Refer to Measurements and Testbenches to
  analyze performance metrics such as phase noise, reference and fractional
  spurs, aperture jitter, timing impairments, and lock time.
- Refer to Get Started with SerDes Toolbox (SerDes Toolbox)
  export a Simulink model and assess metrics such as bathtub curve and channel
  operating margin (COM), including the effects of jitter and crosstalk.
- Refer to Analyze Serial Links with Serial Link Designer (Signal Integrity Toolbox) and Analyze Parallel Links with Parallel Link Designer (Signal Integrity Toolbox) to understand
  how to set up a topology or use one of the predefined ‘kits’ to run simulations
  of interest. Use the Signal Integrity Viewer app to view the waveforms,
  bathtubs, measurements, and more.
- For the new eye diagram block, see Eye
  Diagram.

## Description

(Removed) Display eye diagram of time-domain signal

The Eye Diagram block displays multiple traces of a modulated signal to
produce an eye diagram. You can use the block to reveal the modulation characteristics of
the signal, such as the effects of pulse shaping or channel distortions. .

The Eye Diagram block has one input port. This block accepts a column
vector or scalar input signal. The block accepts a signal with the following data types:
double, single, base integer, and fixed point. All data types are cast as double before
the block displays results.

To modify the eye diagram display, select **View** > **Configuration Properties** or click the **Configuration Properties** button (). Then select the **Main**, **2D color
histogram**, **Axes**, or **Export** tabs
and modify the settings.
