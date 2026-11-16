---
type: simulink-block
title: 'Notch-Peak Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Designs'
documentation_page: 'notchpeakfilter'
documentation_source_path: 'ref/notchpeakfilter.html'
language: en
---

# Notch-Peak Filter

## Ports

### Input

### **Input** — Input signal vector | matrix

Specify the input signal as a vector or a matrix. Each column of the
input signal is treated as a separate channel. If the input is a
two-dimensional signal, the first dimension represents the channel
length (or frame size) and the second dimension represents the number of
channels. If the input is a one-dimensional signal, then it is
interpreted as a single channel.

This block supports variable-size input, enabling you to change the
channel length during simulation. To enable variable-size input, clear
the **Inherit sample rate from input** check box. The
number of channels must remain constant.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **notch** — Notch filter output vector | matrix

Notch filter output, returned as a vector or a matrix.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **peak** — Peak filter output vector | matrix

Peak filter output, returned as a vector or a matrix.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

### **Filter specification** — Filter design specifications `Bandwidth and center frequency` (default) | `Coefficients` | `Quality factor and center frequency`

Specify the parameter or the coefficients the block uses to design the filter:

- `Bandwidth and center frequency`
  (default) — Design the filter using **3 dB
  bandwidth** and **Center frequency of notch
  or peak**.
- `Coefficients` — Design the
  filter using **Bandwidth coefficient** and
  **Center frequency coefficient**.
- `Quality factor and center frequency`
  — Design the filter using **Quality
  factor** and **Center frequency of notch or
  peak**.

### **Specify bandwidth from input port** — Option to specify 3 dB bandwidth from input port `off` (default) | `on`

When you select this check box, the 3 dB bandwidth is input through the
**BW** port. When you clear this check box, the 3 dB
bandwidth is specified in the block dialog box through the **3 dB
bandwidth** parameter.

#### Dependencies

To enable this parameter, set **Filter
specification** to `Bandwidth and center
frequency`.

### **3 dB bandwidth** — 3-dB bandwidth `2205` (default) | positive scalar

Specify the 3-dB bandwidth of the filter as a positive scalar in Hz
or in normalized frequency
units *(since R2024a)*.

If you set the **Sample rate
mode** parameter to:

- `Specify on dialog` or
  `Inherit from input port` –– The
  value of the 3-dB bandwidth is in Hz and must be less than half
  the sample rate of the input signal.
- `Use normalized frequency (0 to 1)`
  –– The value of the 3-dB bandwidth is in normalized frequency
  units. The value must be a positive scalar less than
  `1.0`.

*(since R2024a)*

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Filter
specification** to `Bandwidth and center
frequency`, and clear the **Specify bandwidth
from input port** parameter.

### **Specify center frequency from input port** — Option to specify center frequency from input port `off` (default) | `on`

When you select this check box, the center frequency is input through the
**Fc** port. When you clear this check box, the center
frequency is specified in the block dialog box through the **Center
frequency of notch or peak** parameter.

#### Dependencies

To enable this parameter, set **Filter
specification** to `Bandwidth and center
frequency` or `Quality factor and center
frequency`.

### **Center frequency of notch or peak** — Notch or peak center frequency `11025` (default) | positive scalar

Specify the center frequency of the notch and peak of the filter as a positive numeric
scalar in Hz or in normalized frequency
units *(since R2024a)*.

If you set the **Sample rate
mode** parameter to:

- `Specify on dialog` or
  `Inherit from input port` –– The
  value of the center frequency is in Hz and must be less than
  half the sample rate of the input signal.
- `Use normalized frequency (0 to 1)`
  –– The value of the center frequency is in normalized frequency
  units. The value must be a positive scalar less than
  `1.0`.

*(since R2024a)*

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Filter
specification** to `Bandwidth and center
frequency` or `Quality factor and center
frequency`, and clear the **Specify center
frequency from input port** parameter.

### **Specify bandwidth coefficient from input port** — Option to specify bandwidth coefficient from input port `off` (default) | `on`

When you select this check box, the bandwidth coefficient is input through
the port, **BWCoeff**. When you clear this check box, the
bandwidth coefficient is specified in the block dialog box through the
**Bandwidth coefficient** parameter.

#### Dependencies

To enable this parameter, set **Filter
specification** to
`Coefficients`.

### **Bandwidth coefficient** — Bandwidth coefficient `0.72654` (default) | real scalar in the range [−`1` `1`]

Specify the coefficient that determines the 3 dB bandwidth of the filter
as a finite numeric scalar in the range [−`1`
`1`].

- `-1` corresponds to the maximum 3 dB
  bandwidth (one-fourth the sample rate of the input
  signal).
- `1` corresponds to the minimum bandwidth (0
  Hz, that is, an allpass filter).

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Filter
specification** to `Coefficients`
and clear the **Specify bandwidth coefficient from input
port** parameter.

### **Specify center frequency coefficient from input port** — Option to specify center frequency coefficient from input port `off` (default) | `on`

When you select this check box, the center frequency coefficient is input
through the **FcCoeff** port. When you clear this check
box, the center frequency coefficient is specified in the block dialog box
through the **Center frequency coefficient**
parameter.

#### Dependencies

To enable this parameter, set **Filter
specification** to
`Coefficients`.

### **Center frequency coefficient** — Center frequency coefficient `0` (default) | real scalar in the range [−`1` `1`]

Specify the coefficient that determines the center frequency of the filter
as a finite numeric scalar in the range [−`1`
`1`].

- `-1` corresponds to the minimum center
  frequency (`0` Hz).
- `1` corresponds to the maximum center
  frequency (half the sample rate of the input signal).

The default value of `0` corresponds to quarter the
sample rate of the input signal.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Filter
specification** to `Coefficients`
and clear the **Specify center frequency coefficient from input
port** parameter.

### **Specify quality factor from input port** — Option to specify quality factor from input port `off` (default) | `on`

When you select this check box, the quality factor is input through the
**Q** port. When you clear this check box, the quality
factor is specified in the block dialog box through the **Quality
factor** parameter.

#### Dependencies

To enable this parameter, set **Filter
specification** to `Quality factor and center
frequency`.

### **Quality factor** — Quality factor for notch or peak filter `5` (default) | positive scalar

Specify the quality factor of the notch and peak filter as a real positive scalar. The
quality factor is defined as **Center frequency of notch or
peak** / **3 dB bandwidth**. A higher quality
factor corresponds to a narrower peak or dip.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Filter
specification** to `Quality factor and center
frequency` and clear the **Specify quality
factor from input port** parameter.

### **Filter output** — Filter response to output `Notch and Peak` (default) | `Notch` | `Peak`

Specify the response to output as one of these:

- `Notch and Peak` — The block
  outputs the notch and peak responses of the filter.
- `Notch` — The block outputs
  the notch response of the filter.
- `Peak` — The block outputs the
  peak response of the filter.

### **Sample rate mode** — Mode to specify the input sample rate `Use normalized frequency (0 to 1)` (default) | `Specify on dialog` | `Inherit from input port`

*Since R2024a*

Specify the input sample rate using one of these options:

- `Use normalized frequency (0 to 1)`
  –– Specify the passband edge and the stopband edge frequencies
  in normalized frequency units (0 to 1).
- `Specify on dialog` –– Specify the
  input sample rate in the block dialog box using the
  **Input sample rate (Hz)**
  parameter.
- `Inherit from input port` –– The
  block inherits the sample rate from the input signal. The block
  computes the sample rate as
  *N*/*Ts*, where
  *N* is the frame size of the input signal
  and *Ts* is the sample time of the input
  signal.

### **Input sample rate (Hz)** — Sample rate of input `44100` (default) | positive scalar

Specify the sample rate of the input signal as a positive scalar
value.

#### Dependencies

To enable this parameter, set:

- **Filter specification** to any accepted
  value except `Coefficients`.
- **Sample
  rate mode** to `Specify on
  dialog`. *(since R2024a)*

### **View Filter Response** — View filter response button (default)

Clicking this button opens the filter visualizer and displays the magnitude response of
the notch-peak filter. The response is based on the parameters you select in
the block dialog box. To update the response while the visualizer is
running, modify the parameters in the dialog box and click
**Apply**.

You can configure the plot settings and the frequency response
measurements from the interface of the visualizer.

On the **Scope** tab, you can enable the legend, specify to plot both
magnitude and phase responses of the filter, modify the plot settings,
generate a script to re-create the plot, and even save or share the
settings. On the **Measurements** tab, you can enable data
cursors, and display the peak values of the filter response.

For more details on the filter visualizer interface and its tools, see
Configure Filter Visualizer.

#### Dependencies

To enable this button, do not specify any filter specifications from
the input port.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB® interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.

## Libraries

DSP System Toolbox / Filtering / Filter Designs

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `No` |
| **Variable-Size Signals** | `Yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015a**

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

### R2023b: Support for normalized frequencies

When you set the **Sample rate mode** parameter to
`Use normalized frequency (0 to 1)`, you can specify
the 3 dB bandwidth and center frequency in normalized frequency units (0 to
1).

## Description

Design second-order tunable notching and peaking IIR filter

The Notch-Peak Filter block filters each channel of the input signal
over time using a specified center frequency and 3 dB bandwidth. This block offers
tunable filter design parameters, which enable you to tune the filter characteristics
while the simulation is running. The block designs the filter according to the filter
parameters set in the block dialog box. The output port properties such as datatype,
complexity, and dimension, are identical to the input port properties.
