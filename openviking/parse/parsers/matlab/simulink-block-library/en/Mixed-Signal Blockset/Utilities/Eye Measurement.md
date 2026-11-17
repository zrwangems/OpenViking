---
type: simulink-block
title: 'Eye Measurement'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'eyemeasurement'
documentation_source_path: 'ref/eyemeasurement.html'
language: en
---

# Eye Measurement

## Ports
```yaml
ports:
- name: data
  summary: Input data scalar
  direction: input
  data_types: double
- name: clock
  summary: Sampling clock for input data scalar
  direction: input
  data_types: double
- name: thresholds
  summary: Symbol thresholds used to separate symbols vector | matrix
  direction: input
  data_types: double
```

### Input

### **data** — Input data scalar

Input data used to construct the eye pattern, specified as a scalar.

**Data Types:** `double`

### **clock** — Sampling clock for input data scalar

Sampling clock signal for input data, specified as a scalar. Windows for the eye
pattern are centered on the clock edges.

If you are using clock times at the **clock** port, new clock
times must be within 1 UI of the current simulation time. Clock times should occur in
the center of the corresponding eye opening.

#### Dependencies

To enable this port, select the **Enable clock input port** in
the **Configuration** tab.

**Data Types:** `double`

### **thresholds** — Symbol thresholds used to separate symbols vector | matrix

Symbol threshold(s), used to separate symbols when building the eye diagram. If
you provide this information, it increases the robustness of the PAMn metrics.

If the data at the **thresholds** port is a vector, the same
vector is used across all time points during measurements. If the data at the
**thresholds** port is a matrix, the block uses one vector for each
time point.

#### Dependencies

To enable this port, select the **Enable threshold input port**
in the **Configuration** tab.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Enable threshold input port
  summary: Enable threshold input port on (default) | off
  group: Configuration
- name: Modulation
  summary: Number of symbol levels in eye diagram 2 (default) | nonnegative integer scalar
  group: Configuration
  block_parameter: Modulation
  type: character vector
  values: nonnegative integer scalar
  default: '2'
- name: Symbol thresholds
  summary: Symbol thresholds auto (default) | real valued vector
  group: Configuration
  block_parameter: SymbolThresholds
  type: character vector
  values: real valued vector
  default: auto
- name: Enable clock input port
  summary: Enable clock input port on (default) | off
  group: Configuration
- name: Clock type
  summary: Determine how to sample waveform clock signal Rising (default) | Falling | Both | Times
  group: Configuration
  block_parameter: ClockType
  type: character vector
  values: Rising | Falling | Both | Times
  default: Rising
- name: Clock threshold
  summary: Edge detection threshold for waveform clocks 0 (default) | real scalar
  group: Configuration
  block_parameter: ClockThreshold
  type: character vector
  values: real scalar
  default: '0'
- name: Clock mode
  summary: Represent how data is captured by recovered clock Clocked (default) | Ideal | Convolved
  group: Configuration
  block_parameter: ClockMode
  type: character vector
  values: Clocked | Ideal | Convolved
  default: Clocked
- name: Clock phase offset
  summary: Phase delay for moving clock PDF 0 (default) | nonnegative real scalar
  group: Configuration
  block_parameter: ClockPhaseOffset
  type: character vector
  values: nonnegative real scalar
  default: '0'
- name: Window phase offset
  summary: Delay between ideal clock edge and timing origin 0 (default) | nonnegative real scalar
  group: Configuration
  block_parameter: WindowPhaseOffset
  type: character vector
  values: nonnegative real scalar
  default: '0'
- name: Symbols per diagram
  summary: Width of eye diagram in symbols 2 (default) | scalar
  group: Configuration
  block_parameter: SymbolsperDiagram
  type: character vector
  values: scalar
  default: '2'
- name: Amplitude range
  summary: Minimum and maximum eye amplitudes in eye diagram [] (default) | two-element vector
  group: Configuration
  block_parameter: AmplitudeRange
  type: character vector
  values: two-element vector
  default: '[]'
- name: Amplitude bins
  summary: Number of amplitude bins in eye diagram 257 (default) | positive integer scalar
  group: Configuration
  block_parameter: AmplitudeBins
  type: character vector
  values: positive integer scalar
  default: '257'
- name: Time bins
  summary: Number of time bins in eye diagram 256 (default) | positive integer scalar
  group: Configuration
  block_parameter: TimeBins
  type: character vector
  values: positive integer scalar
  default: '256'
- name: Hold off time
  summary: Delay before measurement analysis 0 (default) | nonnegative real scalar
  group: Configuration
  block_parameter: HoldOffTime
  type: character vector
  values: nonnegative real scalar
  default: '0'
- name: Symbol time
  summary: Time for one symbol 16e-9 (default) | positive real scalar
  group: Configuration
  block_parameter: SymbolTime
  type: character vector
  values: positive real scalar
  default: 16e-9
- name: Sample time
  summary: Time for one sample [1e-9, 0] (default) | two-element vector | scalar
  group: Configuration
  block_parameter: SampleTime
  type: character vector
  values: two-element vector | scalar
  default: '[1e-9, 0]'
- name: Add Metric
  summary: Add new metric to calculate button
  group: Metric Setup
- name: Remove Selected Metrics
  summary: Remove selected metrics button
  group: Metric Setup
- name: Store results in base workspace
  summary: Store metric results to base workspace off (default) | on
  group: Metric Setup
- name: Metrics variable name
  summary: Name of metrics variable that stores measurement results ans (default) | string
  group: Metric Setup
  block_parameter: MetricsVariableName
  type: character vector
  values: string
  default: ans
- name: Export to file
  summary: Export simulation results to file button
  group: Metric Setup
- name: Export to base workspace
  summary: Export simulation results to base workspace button
  group: Metric Setup
- name: Eye mask type
  summary: Shape of eye mask Off (default) | Rectangle | Diamond | Hexagon | Custom
  group: Eye Mask
- name: W1 (UI)
  summary: Width of rectangle, diamond, and center of hexagon eye masks 0.2 (default) | positive real scalar
  group: Eye Mask
  block_parameter: W1
  type: character vector
  values: positive real scalar
  default: '0.2'
- name: W2 (UI)
  summary: Width of top and bottom of hexagon eye mask 0.1 (default) | positive real scalar
  group: Eye Mask
  block_parameter: W2
  type: character vector
  values: positive real scalar
  default: '0.1'
- name: H
  summary: Height of rectangle, diamond, or hexagon eye masks 0.1 (default) | positive real scalar
  group: Eye Mask
  block_parameter: H
  type: character vector
  values: positive real scalar
  default: '0.1'
- name: Position mask in eye
  summary: Position of origin of shape of mask in eye diagram At clock (default) | For best height margin | For best width
    margin
  group: Eye Mask
  block_parameter: PositionMaskInEye
  type: character vector
  values: At clock | For best height margin | For best width margin
  default: At clock
- name: Custom eye mask
  summary: Define custom eye mask from eye mask object [] (default) | object
  group: Eye Mask
  block_parameter: CustomEyeMask
  type: character vector
  values: object
  default: '[]'
- name: Margin SER
  summary: Symbol error rate to measure eye mask margin 1e-5 | nonnegative real scalar in the range [0,1]
  group: Eye Mask
  block_parameter: MarginSER
  type: character vector
  values: nonnegative real scalar in the range [0,1]
  default: 1e-5
- name: Margin extrapolation
  summary: Extrapolation method to generate eye contours none (default) | dualdirac | gaussian | linear | spline | pchip |
    makima
  group: Eye Mask
  block_parameter: MarginExtrapolation
  type: character vector
  values: none | dualdirac | gaussian | linear | spline | pchip | makima
  default: none
- name: Mask variable name
  summary: Name of mask variable to export mask ans (default) | string
  group: Eye Mask
  block_parameter: MaskVariableName
  type: character vector
  values: string
  default: ans
- name: Export mask to file
  summary: Export mask to file button
  group: Eye Mask
- name: Export mask to base workspace
  summary: Export mask to base workspace button
  group: Eye Mask
- name: Show plots at end of simulation
  summary: Automatically show plots at end of simulation on (default) | off
  group: Plot Setup
- name: Plot grouping
  summary: define how plots are grouped together Subplot on same figure (default) | One figure per plot
  group: Plot Setup
- name: Add Plot
  summary: Add new plot to show button
  group: Plot Setup
- name: Remove Selected Plots
  summary: Remove selected plots button
  group: Plot Setup
- name: Show Plots
  summary: Show plots button
  group: Plot Setup
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Configuration

### **Enable threshold input port** — Enable threshold input port on (default) | off

Select to enable the threshold input port. By default, this port is
enabled.

### **Modulation** — Number of symbol levels in eye diagram `2` (default) | nonnegative integer scalar

Number of symbol levels expected in the eye diagram, specified as a nonnegative
integer scalar.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Modulation` |
| **Type:** character vector |
| **Values:** nonnegative integer scalar |
| **Default:** `2` |

### **Symbol thresholds** — Symbol thresholds `auto` (default) | real valued vector

Symbol thresholds to use, specified as a real valued vector. Use this parameter to
specify the symbol thresholds if you do not provide a threshold input.

#### Dependencies

To enable this parameter, deselect the **Enable threshold input
port**

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SymbolThresholds` |
| **Type:** character vector |
| **Values:** real valued vector |
| **Default:** `auto` |

### **Enable clock input port** — Enable clock input port on (default) | off

Select to enable the clock input port. By default, this port is enabled.

### **Clock type** — Determine how to sample waveform clock signal `Rising` (default) | `Falling` | `Both` | `Times`

Determine how to sample waveform clock signals:

- `Rising` — Sample the data waveform at the rising
  edge of the clock waveform.
- `Falling` — Sample the data waveform at the falling
  edge of the clock waveform.
- `Both` — Sample the data waveform at both rising and
  falling edges of the clock waveform.
- `Times` — Sample the data waveform at the time values
  specified by the clock signal.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ClockType` |
| **Type:** character vector |
| **Values:** `Rising` | `Falling` | `Both` | `Times` |
| **Default:** `Rising` |

### **Clock threshold** — Edge detection threshold for waveform clocks `0` (default) | real scalar

Edge detection threshold for waveform clocks, specified as a real scalar.

#### Dependencies

To enable this parameter, set the **Enable clock input port**
option as on and set the **Clock type** as
`Rising`, `Falling`, or
`Both`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ClockThreshold` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `0` |

### **Clock mode** — Represent how data is captured by recovered clock `Clocked` (default) | `Ideal` | `Convolved`

Represent how data is captured by the recovered clock from the system
perspective.

- `Clocked` — The data is captured at the input to the
  decision latch using the clock from the output of the clock recovery
  circuit.
- `Ideal` — The data and clock are captured using an
  ideal reference clock source.
- `Convolved` — The data eye and clock PDF captured in
  normal mode are convolved together to present an eye and clock that look as though
  the simulation had been run in clocked mode.

For more information, see Clock Modes (Signal Integrity Toolbox).

**Note**

If you set the **Enable clock input port** option as off,
**Clock mode** is set to `Ideal` and you
cannot change it.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ClockMode` |
| **Type:** character vector |
| **Values:** `Clocked` | `Ideal` | `Convolved` |
| **Default:** `Clocked` |

### **Clock phase offset** — Phase delay for moving clock PDF `0` (default) | nonnegative real scalar

Phase delay for moving the clock PDF, specified as a nonnegative real scalar in
seconds, samples, or UI.

**Clock phase offset** applies to the external clock you
provide when you set **Clock mode** to
`clocked`. If you do not provide an external clock, the
block generates the clock PDF derived from an ideal clock.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ClockPhaseOffset` |
| **Type:** character vector |
| **Values:** nonnegative real scalar |
| **Default:** `0` |

### **Window phase offset** — Delay between ideal clock edge and timing origin `0` (default) | nonnegative real scalar

Delay between the ideal clock edge and the timing origin, specified as a
nonnegative real scalar in seconds, samples, or UI.

When you set the **Clock mode** to
`Ideal` or `Convolved`, the
**Window phase offset** is used to determine the window position
relative to an internal ideal reference clock.

#### Dependencies

To enable this parameter, set **Clock mode** to
`Ideal` or `Convolved`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `WindowPhaseOffset` |
| **Type:** character vector |
| **Values:** nonnegative real scalar |
| **Default:** `0` |

### **Symbols per diagram** — Width of eye diagram in symbols `2` (default) | scalar

The width of the eye diagram in symbols, specified as a scalar.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SymbolsperDiagram` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `2` |

### **Amplitude range** — Minimum and maximum eye amplitudes in eye diagram `[]` (default) | two-element vector

Minimum and maximum amplitudes contained in the eye diagram, specified as a
two-element vector.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `AmplitudeRange` |
| **Type:** character vector |
| **Values:** two-element vector |
| **Default:** `[]` |

### **Amplitude bins** — Number of amplitude bins in eye diagram `257` (default) | positive integer scalar

Number of amplitude bins in the eye diagram, specified as a positive integer
scalar.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `AmplitudeBins` |
| **Type:** character vector |
| **Values:** positive integer scalar |
| **Default:** `257` |

### **Time bins** — Number of time bins in eye diagram `256` (default) | positive integer scalar

Number of time bins in the eye diagram, specified as a positive integer
scalar.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `TimeBins` |
| **Type:** character vector |
| **Values:** positive integer scalar |
| **Default:** `256` |

### **Hold off time** — Delay before measurement analysis `0` (default) | nonnegative real scalar

Delays measurement analysis to avoid corruption by transients, specified as a
nonnegative real scalar in seconds, samples, or UI.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `HoldOffTime` |
| **Type:** character vector |
| **Values:** nonnegative real scalar |
| **Default:** `0` |

### **Symbol time** — Time for one symbol `16e-9` (default) | positive real scalar

Time for one symbol, specified as a positive real scalar.

**Note**

**Symbol time** must be evenly divisible by **Sample
time**.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SymbolTime` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `16e-9` |

### **Sample time** — Time for one sample `[1e-9, 0]` (default) | two-element vector | scalar

Time for one sample, specified as a positive real scalar.

If **Sample time** is specified as a 2- element vector, it
represents the fixed-step discrete sample time in Simulink.

If **Sample time** is specified as a scalar, it represents the
sample interval used in the SerDes Toolbox™.

**Note**

**Symbol time** must be evenly divisible by **Sample
time**.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** two-element vector | scalar |
| **Default:** `[1e-9, 0]` |

### Metric Setup

### **Add Metric** — Add new metric to calculate button

Click to add new eye diagram metric to calculate. You can define which metric to
calculate at what point, the symbol error rate, and the extrapolation method.

### **Remove Selected Metrics** — Remove selected metrics button

Click to remove selected eye diagram metrics to focus on the area of
interest.

### **Store results in base workspace** — Store metric results to base workspace off (default) | on

Select to store the metric calculation result to the base workspace at the end of
simulation.

### **Metrics variable name** — Name of metrics variable that stores measurement results `ans` (default) | string

Name of the metrics variable that stores measurement results in the base
workspace.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `MetricsVariableName` |
| **Type:** character vector |
| **Values:** string |
| **Default:** `ans` |

### **Export to file** — Export simulation results to file button

Click to export the simulation results to a file to save for later use.

### **Export to base workspace** — Export simulation results to base workspace button

Click to export the simulation results to the base workspace.

### Eye Mask

### **Eye mask type** — Shape of eye mask `Off` (default) | `Rectangle` | `Diamond` | `Hexagon` | `Custom`

Shape of the eye mask for the mask margin measurement. For more information, see
`eyeMask`.

### **W1 (UI)** — Width of rectangle, diamond, and center of hexagon eye masks `0.2` (default) | positive real scalar

The width of the rectangle or diamond eye masks or the width at the center of the
hexagon eye mask, specified as a positive real scalar.

#### Dependencies

To enable this parameter, set **Eye mask type** to
`Rectangle`, `Diamond`, or
`Hexagon`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `W1` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `0.2` |

### **W2 (UI)** — Width of top and bottom of hexagon eye mask `0.1` (default) | positive real scalar

The width at the top and bottom of the hexagon eye mask, specified as a positive
real scalar.

#### Dependencies

To enable this parameter, set **Eye mask type** to
`Hexagon`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `W2` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `0.1` |

### **H** — Height of rectangle, diamond, or hexagon eye masks `0.1` (default) | positive real scalar

The height of the rectangle, diamond or hexagon eye masks, specified as a positive
real scalar.

#### Dependencies

To enable this parameter, set **Eye mask type** to
`Rectangle`, `Diamond`, or
`Hexagon`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `H` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `0.1` |

### **Position mask in eye** — Position of origin of shape of mask in eye diagram `At clock` (default) | `For best height margin` | `For best width margin`

Define the position of origin of the shape of the mask in the eye diagram. You can
position it at the clock, or for the best eye height or width.

#### Dependencies

To enable this parameter, set **Eye mask type** to
`Rectangle`, `Diamond`, or
`Hexagon`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PositionMaskInEye` |
| **Type:** character vector |
| **Values:** `At clock` | `For best height margin` | `For best width margin` |
| **Default:** `At clock` |

### **Custom eye mask** — Define custom eye mask from eye mask object `[]` (default) | object

Define a custom eye mask from an eye mask object.

#### Dependencies

To enable this parameter, set **Eye mask type** to
`Custom`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CustomEyeMask` |
| **Type:** character vector |
| **Values:** object |
| **Default:** `[]` |

### **Margin SER** — Symbol error rate to measure eye mask margin `1e-5` | nonnegative real scalar in the range [0,1]

Symbol error rate (SER) at which the block measures the eye mask margin, specified
as a nonnegative real scalar in the range [0,1].

#### Dependencies

To enable this parameter, set **Eye mask type** to
`Rectangle`, `Diamond`,
`Hexagon`, or `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `MarginSER` |
| **Type:** character vector |
| **Values:** nonnegative real scalar in the range [0,1] |
| **Default:** `1e-5` |

### **Margin extrapolation** — Extrapolation method to generate eye contours `none` (default) | `dualdirac` | `gaussian` | `linear` | `spline` | `pchip` | `makima`

Extrapolation method to generate eye contours used for measuring eye margins. The
block extrapolates eye diagram to a specified SER using interpolation between adjacent
bins. For more information, see Extrapolation.

**Note**

This functionality requires a license to Signal Integrity
Toolbox™, Optimization Toolbox™, or Curve Fitting Toolbox™. The license requirements are listed according to the order of
performance, where Signal Integrity
Toolbox provides fastest calculation.

#### Dependencies

To enable this parameter, set **Eye mask type** to
`Rectangle`, `Diamond`,
`Hexagon`, or `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `MarginExtrapolation` |
| **Type:** character vector |
| **Values:** `none` | `dualdirac` | `gaussian` | `linear` | `spline` | `pchip` | `makima` |
| **Default:** `none` |

### **Mask variable name** — Name of mask variable to export mask `ans` (default) | string

Name of the mask variable to export the mask to the base workspace.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `MaskVariableName` |
| **Type:** character vector |
| **Values:** string |
| **Default:** `ans` |

### **Export mask to file** — Export mask to file button

Click to export the mask to a file to save for later use.

### **Export mask to base workspace** — Export mask to base workspace button

Click to export the mask to the base workspace.

### Plot Setup

### **Show plots at end of simulation** — Automatically show plots at end of simulation on (default) | off

Select to automatically show the simulation results as plots at the end of
simulation. You can define which type of plot to generate, including the eye, clock,
and bathtub.

### **Plot grouping** — define how plots are grouped together `Subplot on same figure` (default) | `One figure per plot`

Define how the plots are grouped together.

### **Add Plot** — Add new plot to show button

Click to add new plot to show.

### **Remove Selected Plots** — Remove selected plots button

Click to remove selected plots to focus on the area of interest.

### **Show Plots** — Show plots button

Click to show the plots.
## Libraries

Mixed-Signal Blockset / Utilities SerDes Toolbox / Utilities Signal Integrity Toolbox / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

### R2025b: Move Clock PDF or Eye Diagram Window

Use the **Clock phase offset** parameter to move the clock PDF. This
is useful when **Clock mode** is clocked to center the eye in the
diagram, or in other modes to move the clock PDF relative to the eye diagram. Use
**Window phase offset** parameter to move the eye diagram window in
ideal or convolved clock modes.

### R2025a: Updated Extrapolation Methods

Choose from different extrapolation methods to observe the trend in eye metrics as you
change system parameters to satisfy your requirements.

## Description

Calculate metrics from eye diagram

The Eye Measurement block generates eye pattern from time-domain waveform
data and calculates metrics from the generated pattern.
