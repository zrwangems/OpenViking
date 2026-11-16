---
type: simulink-block
title: 'Variable Bandwidth IIR Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filter Design and Analysis / Filter Design / Singlerate'
documentation_page: 'variablebandwidthiirfilter'
documentation_source_path: 'ref/variablebandwidthiirfilter.html'
language: en
---

# Variable Bandwidth IIR Filter

## Ports

### Input

### **x** — Data input vector | matrix

Specify the data input as a vector or a matrix. The block treats each column of the
input signal as a separate channel. If the input is a two-dimensional
signal, the first dimension represents the channel length (or frame
size) and the second dimension represents the number of channels. If the
input is a one-dimensional signal, then the block interprets it as
having a single channel.

The block accepts variable-size input signals, that is, you can change the size of each
input channel during simulation but you cannot change the number of
channels.

This port is unnamed until you select one of these parameters:

- **Specify passband frequency from input
  port**
- **Specify center frequency from input
  port**
- **Specify bandwidth from input
  port**

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Fp** — Filter passband frequency positive scalar

Specify the passband frequency of the IIR filter as a real positive
scalar in Hz or in normalized frequency
units *(since R2023a)*.

#### Dependencies

To enable this port, select the **Specify passband
frequency from input port** parameter.

**Data Types:** `single` | `double`

### **Fc** — Filter center frequency positive scalar

Specify the center frequency of the IIR filter as a real positive
scalar in Hz or in normalized frequency
units *(since R2023a)*.

#### Dependencies

To enable this port, select the **Specify center frequency
from input port** parameter.

**Data Types:** `single` | `double`

### **BW** — Filter bandwidth positive scalar

Specify the bandwidth of the IIR filter as a real positive scalar in
Hz or in normalized frequency
units *(since R2023a)*.

#### Dependencies

To enable this port, select the **Specify bandwidth from
input port** parameter.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Filtered output vector | matrix

Filtered output, returned as a vector or a matrix. The size, data
type, and complexity of the output signal matches that of the input
signal.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

### **Filter type** — Filter type `Lowpass` (default) | `Highpass` | `Bandpass` | `Bandstop`

Specify the type of IIR filter. You can set this parameter to:

- `Lowpass`
- `Highpass`
- `Bandpass`
- `Bandstop`

### **IIR filter order** — IIR filter order 8 (default) | positive integer

Specify the order of the IIR filter as a positive integer.

### **Specify passband frequency from input port** — Specify passband frequency from input port `off` (default) | `on`

When you select this check box, specify the filter passband frequency through the
**Fp** port. When you clear this check box, specify the
passband frequency in the block dialog box through the **Filter
passband frequency** parameter.

#### Dependency

To enable this parameter, set **Filter type** to
`Lowpass` or
`Highpass`.

### **Filter passband frequency** — Filter passband frequency 512 (default) | positive scalar

Specify the filter passband frequency as a real, positive scalar in Hz
or in normalized frequency
units *(since R2023a)*.

If you set the **Sample rate
mode** parameter to:

- `Specify on dialog` or
  `Inherit from input port` –– The
  value of the filter passband frequency is in Hz and must be less
  than half the value of the input sample rate.
- `Use normalized frequency (0 to 1)`
  –– The value of the filter passband frequency is in normalized
  frequency units. The value must be a positive scalar less than
  `1.0`.

*(since R2023a)*

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Filter type** to
  `Lowpass` or
  `Highpass`.
- Clear the **Specify passband frequency from input
  port** parameter.

### **Specify center frequency from input port** — Specify center frequency from input port `off` (default) | `on`

When you select this check box, specify the center frequency of the IIR filter through
the **Fc** port. When you clear this check box, specify the
center frequency in the block dialog box through the **Filter center
frequency** parameter.

#### Dependencies

To enable this parameter, set **Filter type** to
`Bandpass` or
`Bandstop`.

### **Filter center frequency** — Filter center frequency 44100/4 (default) | positive scalar

Specify the filter center frequency as a real positive scalar in Hz
or in normalized frequency
units *(since R2023a)*.

If you set the **Sample rate
mode** parameter to:

- `Specify on dialog` or
  `Inherit from input port` –– The
  value of the filter center frequency is in Hz and must be less
  than half the value of the input sample rate.
- `Use normalized frequency (0 to 1)`
  –– The value of the filter center frequency is in normalized
  frequency units. The value must be a positive scalar less than
  `1.0`.

*(since R2023a)*

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Filter type** to
  `Bandpass` or
  `Bandstop`.
- Clear the **Specify center frequency from input
  port** parameter.

### **Specify bandwidth from input port** — Specify bandwidth from input port `off` (default) | `on`

When you select this check box, specify the bandwidth of the IIR filter through the
**BW** port. When you clear this check box, specify the
filter bandwidth in the block dialog box through the **Filter
bandwidth** parameter.

#### Dependencies

To enable this parameter, set **Filter type** to
`Bandpass` or
`Bandstop`.

### **Filter bandwidth** — Filter bandwidth 7680 (default) | positive scalar

Specify the filter bandwidth as a positive scalar in Hz or in normalized frequency units *(since R2023a)*.

If you set the **Sample rate
mode** parameter to:

- `Specify on dialog` or
  `Inherit from input port` –– The
  value of the filter bandwidth is in Hz and must be less than
  half the value of the input sample rate.
- `Use normalized frequency (0 to 1)`
  –– The value of the filter bandwidth is in normalized frequency
  units. The value must be a positive scalar less than
  `1.0`.

*(since R2023a)*

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Filter type** to
  `Bandpass` or
  `Bandstop`.
- Clear the **Specify bandwidth from input
  port** parameter.

### **Filter passband ripple (dB)** — Filter passband ripple 1 (default) | positive scalar

Specify the filter passband ripple as a real, positive scalar.

### **Filter Stopband attenuation (dB)** — Filter Stopband attenuation 60 (default) | positive scalar

Specify the filter stopband attenuation as a real, positive scalar.

### **Sample rate mode** — Mode to specify the input sample rate `Use normalized frequency (0 to 1)` (default) | `Specify on dialog` | `Inherit from input port`

*Since R2023a*

Specify the input sample rate using one of these options:

- `Use normalized frequency (0 to 1)`
  –– Specify the filter passband frequency, center frequency, and
  the filter bandwidth in normalized frequency units (0 to
  1).
- `Specify on dialog` –– Specify the
  input sample rate in the block dialog box using the
  **Input sample rate (Hz)**
  parameter.
- `Inherit from input port` –– The
  block inherits the sample rate from the input signal as
  *N* / *Ts*, where
  *N* is the frame size of the input signal
  and *Ts* is the sample time of the input
  signal.

### **Input sample rate (Hz)** — Input sample rate 44100 (default) | positive scalar

Specify the sample rate of the input signal as a positive scalar in
Hz.

#### Dependencies

To enable this parameter, set
the **Sample rate mode** parameter to
`Specify on dialog`. *(since R2023a)*

### **View Filter Response** — View Filter Response button

Clicking this button opens the filter visualizer and displays the magnitude response of
the variable bandwidth IIR filter. The response is based on the parameters
you select in the block parameters dialog box. To update the magnitude
response while the filter visualizer is running, modify the parameters in
the dialog box and click **Apply**.

You can configure the plot settings and the signal measurements from the
interface of the visualizer.

On the **Scope** tab, the **Configuration** section
allows you to modify the plot settings. On the
**Measurements** tab, you can measure the signal
statistics, place data cursors, and display the peak values of the selected
signal.

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

### R2023a: Support for normalized frequencies

When you set the **Sample rate mode** parameter to
`Use normalized frequency (0 to 1)`, you can specify
the filter passband frequency, center frequency, and filter bandwidth in normalized
frequency units (0 to 1).

## Description

Design tunable bandwidth IIR filter

The Variable Bandwidth IIR Filter block filters each channel of the input
signal over time using the IIR filter specifications. This block offers tunable filter
design parameters, which enable you to tune the filter characteristics while the
simulation is running.

The block designs the IIR filter according to the filter parameters set in the block dialog box. The output port properties, such as datatype, complexity, and dimension, are identical to the input port properties.
