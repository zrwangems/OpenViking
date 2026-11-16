---
type: simulink-block
title: 'Variable Bandwidth FIR Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Designs'
documentation_page: 'variablebandwidthfirfilter'
documentation_source_path: 'ref/variablebandwidthfirfilter.html'
language: en
---

# Variable Bandwidth FIR Filter

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

- **Specify cutoff frequency from input
  port**
- **Specify center frequency from input
  port**
- **Specify bandwidth from input
  port**

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Fcut** — Filter cutoff frequency positive scalar

Specify the cutoff frequency of the FIR filter as a real positive scalar in Hz or in normalized frequency
units *(since R2023a)*.

#### Dependencies

To enable this port, select the **Specify cutoff frequency
from input port** parameter.

**Data Types:** `single` | `double`

### **Fc** — Filter center frequency positive scalar

Specify the center frequency of the FIR filter as a real positive scalar in Hz or in normalized frequency
units *(since R2023a)*.

#### Dependencies

To enable this port, select the **Specify center frequency
from input port** parameter.

**Data Types:** `single` | `double`

### **BW** — Filter bandwidth positive scalar

Specify the bandwidth of the FIR filter as a real positive scalar in Hz or in normalized frequency
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

### **FIR filter order** — FIR filter order `30` (default) | positive integer

Specify the order of the FIR filter as a positive integer scalar.

### **Filter type** — Filter type `Lowpass` (default) | `Highpass` | `Bandpass` | `Bandstop`

Specify the type of FIR filter. You can set this parameter to:

- `Lowpass`
- `Highpass`
- `Bandpass`
- `Bandstop`

### **Specify cutoff frequency from input port** — Specify cutoff frequency from input port `off` (default) | `on`

When you select this check box, specify the cutoff frequency through the
**Fcut** port. When you clear this check box, specify
the cutoff frequency in the block dialog box through the **Filter
cutoff frequency** parameter.

#### Dependency

To enable this parameter, set **Filter type** to
`Lowpass` or
`Highpass`.

### **Filter cutoff frequency** — Filter cutoff frequency 512 (default) | positive scalar

Specify the cutoff frequency of the FIR filter as a real positive scalar
in Hz or in normalized frequency
units *(since R2023a)*.

If you set the **Sample rate
mode** parameter to:

- `Specify on dialog` or
  `Inherit from input port` –– The
  value of the filter cutoff frequency is in Hz and must be less
  than half the value of the input sample rate.
- `Use normalized frequency (0 to 1)`
  –– The value of the filter cutoff frequency is in normalized
  frequency units. The value must be a positive scalar less than
  `1.0`.

*(since R2023a)*

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set **Filter type** to
  `Lowpass` or
  `Highpass`.
- Clear the **Specify cutoff frequency from input
  port** parameter.

### **Specify center frequency from input port** — Specify center frequency from input port `off` (default) | `on`

When you select this check box, specify the center frequency through the
**Fc** port. When you clear this check box, specify the
center frequency in the block dialog box through the **Filter center
frequency** parameter.

#### Dependencies

To enable this parameter, set **Filter type** to
`Bandpass` or
`Bandstop`.

### **Filter center frequency** — Filter center frequency 44100/4 (default) | positive scalar

Specify the center frequency of the FIR filter as a real positive scalar
in Hz or in normalized frequency
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

When you select this check box, specify the filter bandwidth through the
**BW** port. When you clear this check box, specify the
filter bandwidth in the block dialog box through the **Filter
bandwidth** parameter.

#### Dependency

To enable this parameter, set **Filter type** to
`Bandpass` or
`Bandstop`.

### **Filter bandwidth** — Filter bandwidth 7680 (default) | positive scalar

Specify the bandwidth of the FIR filter as a real positive scalar in Hz
or in normalized frequency
units *(since R2023a)*.

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

### **Window function** — Window function `Hann` (default) | `Hamming` | `Chebyshev` | `Kaiser`

Specify the window function used to design the FIR filter. You can set this parameter to:

- `Hann`
- `Hamming`
- `Chebyshev`
- `Kaiser`

### **Chebyshev window sidelobe attenuation (dB)** — Chebyshev window sidelobe attenuation 60 (default) | positive scalar

Specify the sidelobe attenuation of the Chebyshev window as a real positive
scalar.

#### Dependencies

To enable this parameter, set **Window function** to
`Chebyshev`.

### **Kaiser window parameter** — Kaiser window parameter 0.5 (default) | real scalar

Specify the Kaiser window parameter as a real scalar.

#### Dependencies

To enable this parameter, set **Window function** to
`Kaiser`.

### **Sample rate mode** — Mode to specify the input sample rate `Use normalized frequency (0 to 1)` (default) | `Specify on dialog` | `Inherit from input port`

*Since R2023a*

Specify the input sample rate using one of these options:

- `Use normalized frequency (0 to 1)`
  –– Specify the filter cutoff frequency, center frequency, and
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

Specify the sample rate of the input signal as a positive scalar in Hz.

#### Dependencies

To enable this parameter, set
the **Sample rate mode** parameter to
`Specify on dialog`. *(since R2023a)*

### **View Filter Response** — View Filter Response button

Clicking this button opens the filter visualizer and displays the magnitude response of
the variable bandwidth FIR filter. The response is based on the parameters
you select in the block dialog box. To update the magnitude response while
the filter visualizer is running, modify the parameters in the dialog box
and click **Apply**.

You can configure the plot settings and the signal measurements from the
interface of the visualizer.

On the **Scope** tab of the filter visualizer toolstrip, the
**Configuration** section allows you to modify the plot
settings. On the **Measurements** tab, you can measure the
signal statistics, place data cursors, and display the peak values of the
selected signal.

For more details on the filter visualizer interface and its tools, see Configure Filter Visualizer.

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

The Variable Bandwidth FIR Filter block supports SIMD code generation using
Intel® AVX2 code replacement library when the input signal has a data type of
`single` or `double`.

The SIMD technology significantly improves the performance of the generated code.
For more information, see SIMD Code Generation. To
generate SIMD code from this block, see Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks.

## Version History

**Introduced in R2015a**

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

### R2023a: Support for normalized frequencies

When you set the **Sample rate mode** parameter to
`Use normalized frequency (0 to 1)`, you can specify
the filter cutoff frequency, center frequency, and filter bandwidth in normalized
frequency units (0 to 1).

## Description

Design tunable bandwidth FIR filter

The Variable Bandwidth FIR Filter block filters each channel of the input
signal over time using the specified FIR filter specifications. This block offers
tunable filter design parameters, which enable you to tune the filter characteristics
while the simulation is running.

The block designs the FIR filter according to the filter parameters specified in the block
dialog box. The output port properties, such as datatype, complexity, and dimension, are
identical to the input port properties.

This block also supports SIMD code generation. For details, see Code Generation.
