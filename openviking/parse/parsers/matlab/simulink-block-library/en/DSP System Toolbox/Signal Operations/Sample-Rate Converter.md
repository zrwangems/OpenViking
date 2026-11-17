---
type: simulink-block
title: 'Sample-Rate Converter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'samplerateconverter'
documentation_source_path: 'ref/samplerateconverter.html'
language: en
---

# Sample-Rate Converter

## Ports
```yaml
ports:
- name: Port_1
  summary: Input signal scalar | vector | matrix
  direction: input
  data_types: single | double
- name: Port_1
  summary: Resampled signal scalar | vector | matrix
  direction: output
  data_types: single | double
```

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Specify the input signal as a real or a complex-valued scalar, vector, or a
matrix.

The block treats each column of a two-dimensional input signal as a
separate channel. If the input is a two-dimensional signal, the first
dimension represents the channel length (or frame size), and the second
dimension represents the number of channels. If the input is a
one-dimensional signal, then the block interprets the signal as having a
single channel.

When you input a variable-size signal (frame length changes during simulation), the
frame length of the signal can be arbitrary, that is, the input frame
length does not have to be a multiple of the decimation factor. When you
input a fixed-size signal (frame length does not change during
simulation), the frame length can be arbitrary only when you select the
**Allow arbitrary frame length for fixed-size input
signals** parameter.

To determine the decimation factor, click the **View Info** button in
the block dialog box.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Resampled signal scalar | vector | matrix

The Sample-Rate Converter block outputs a signal that has the same data
type and complexity as the input signal.

The output signal dimensions depend on the input signal dimensions, the interpolation
and decimation factors of the individual stages of the sample-rate
converter, and whether you select the **Allow arbitrary frame
length for fixed-size input signals** parameter. You can
determine the interpolation factor *L* and the
decimator factor *M* of the individual stages by
clicking the **View Info** button in the block dialog
box.

This table provides more details on the dimensions of the output signal when you input a
fixed-size signal and the block implements the filter in a single
stage.

**Single-Stage Filter With Fixed-Size Input Signal**

| Input Signal | Output Signal Dimensions |
| --- | --- |
| *P*-by-1 column vector, where *P* is a multiple of the decimation factor *M* | (*LP*/*M*)-by-1, where *L* is the interpolation factor |
| *P*-by-1 column vector, where *P* is not a multiple of the decimation factor *M* | `ceil`(*LP*/*M*)-by-1 when you select **Allow arbitrary frame length for fixed-size input signals**.  If you do not select **Allow arbitrary frame length for fixed-size input signals**, the block errors. |
| *P*-by-*Q* matrix, where *P* is a multiple of the decimation factor *M* | (*LP*/*M*)-by-*Q* |
| *P*-by-*Q* matrix, where *P* is not a multiple of the decimation factor *M* | `ceil`(*LP*/*M*)-by-*Q* when you select **Allow arbitrary frame length for fixed-size input signals**.  If you do not select **Allow arbitrary frame length for fixed-size input signals**, the block errors. |

This table gives more details on the dimensions of the output signal when you input a
variable-size signal and the block implements the filter in a single
stage.

When you input a variable-size signal (frame length changes during
simulation), the **Allow arbitrary frame length for
fixed-size input signals** parameter is visible in the
block dialog box but does not have any impact on the input frame length.
You can input a variable-size signal of any frame length even if you do
not select the **Allow arbitrary frame length for
fixed-size input signals** parameter.

**Single-Stage Filter With Variable-Size Input Signal**

| Input Signal | Output Signal Dimensions |
| --- | --- |
| *P*-by-*Q* | `ceil`(*LP*/*M*)-by-*Q* |

**Multistage Filter
Implementation**

When the block implements the filter using multiple stages, the output
frame size of the block depends on the input frame size
*P* and the rate conversion factors of the
individual filter stages. For more information on these filter stages,
click the **View Info** button in the block dialog
box.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Sample rate of input signal (Hz)
  summary: Sample rate of input signal in Hz 48e3 (default) | positive scalar
  group: ''
- name: Sample rate of output signal (Hz)
  summary: Sample rate of output signal in Hz 96e3 (default) | positive scalar
  group: ''
- name: Tolerance for output sample rate
  summary: Maximum tolerance for output sample rate 0 (default) | positive scalar in the range [0,0.5]
  group: ''
- name: Two-sided bandwidth of interest (Hz)
  summary: Two-sided bandwidth of interest in Hz 40e3 (default) | positive scalar
  group: ''
- name: Stopband attenuation (dB)
  summary: Minimum attenuation for aliased components in dB 80 (default) | positive scalar
  group: ''
- name: Allow arbitrary frame length for fixed-size input signals
  summary: Allow arbitrary frame length for fixed-size input signals off (default) | on
  group: ''
- name: View Filter Response
  summary: View Filter Response button
  group: ''
- name: View Info
  summary: Display information about filter button
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

### **Sample rate of input signal (Hz)** — Sample rate of input signal in Hz `48e3` (default) | positive scalar

Specify the sample rate of the input signal as a positive scalar in Hz.
The input sample rate must be greater than the bandwidth of interest.

### **Sample rate of output signal (Hz)** — Sample rate of output signal in Hz `96e3` (default) | positive scalar

Specify the sample rate of the output signal as a positive scalar in Hz.
The output sample rate must be greater than the bandwidth of
interest.

### **Tolerance for output sample rate** — Maximum tolerance for output sample rate `0` (default) | positive scalar in the range [`0`,`0.5`]

Specify the maximum tolerance for the output sample rate as a positive
scalar in the range [`0`,`0.5`]. The
default is `0`.

The actual output sample rate varies but is within the specified range.
For example, if you set the **Tolerance for output sample
rate** to 0.01, then the actual output sample rate is in the
range given by sample rate of output signal ± 1%. This
flexibility allows for a simpler filter design.

### **Two-sided bandwidth of interest (Hz)** — Two-sided bandwidth of interest in Hz `40e3` (default) | positive scalar

Specify the two-sided bandwidth of interest (after the rate of conversion)
as a positive scalar in Hz.

### **Stopband attenuation (dB)** — Minimum attenuation for aliased components in dB `80` (default) | positive scalar

Specify the minimum amount of attenuation for aliased components in the stopband as a
positive scalar in dB. This parameter is the minimum amount by which the
block attenuates any aliasing involved in the process.

### **Allow arbitrary frame length for fixed-size input signals** — Allow arbitrary frame length for fixed-size input signals `off` (default) | `on`

*Since R2023a*

Specify whether fixed-size input signals (whose size does not change during simulation)
can have an arbitrary frame length, where the frame length does not have to
be a multiple of the decimation factor. The block uses this parameter only
for fixed-size input signals and ignores it if the input data varies in size
during simulation.

When the input signal is a variable-size signal, the signal can have
arbitrary frame length, that is, the frame length does not have to be a
multiple of the decimation factor.

For fixed-size input signals, if you:

- Select the **Allow arbitrary frame length for
  fixed-size input signals** parameter, the frame
  length of the signal does not have to be a multiple of the
  decimation factor. If the input is not a multiple of the
  decimation factor, then the output is generally a variable-size
  signal. Therefore, to support arbitrary input size, the block
  must also support variable-size operations, which you can enable
  by selecting the **Allow arbitrary frame length for
  fixed-size input signals** parameter.
- Clear the **Allow arbitrary frame length for
  fixed-size input signals** parameter, the input
  frame length must be a multiple of the decimation factor.

### **View Filter Response** — View Filter Response button

Opens the Filter Visualization Tool FVTool and displays the magnitude/phase response of
the Sample-Rate Converter. The response is based on the block
parameters. FVTool updates when you change the parameters.

To update the magnitude response while FVTool is running, modify the parameters in the
dialog box and click **Apply**.

### **View Info** — Display information about filter button

Click on the **View Info** button to display the filter
information of the Sample-Rate Converter block:

- `Overall Interpolation Factor`
- `Overall Decimation Factor`
- `Number of Filters`
- `Multiplication per Input Sample`
- `Number of Coefficients`
- `Filters`

The button brings the functionality of the `info`
function into the Simulink® environment.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB® interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.
## Libraries

DSP System Toolbox / Signal Operations DSP System Toolbox / Filtering / Multirate Filters

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The Sample-Rate Converter block supports SIMD code generation using
Intel® AVX2 code replacement library under these conditions:

- For upsampling, the ratio of output sample rate to input sample rate
  must be an integer.
- For downsampling, the ratio of input sample rate to output sample rate
  must be an integer.
- Input signal has a data type of `single` or
  `double`.

The SIMD technology significantly improves the performance of the generated code.
For more information, see SIMD Code Generation. To
generate SIMD code from this block, see Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks.

## Version History

**Introduced in R2015b**

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

### R2023a: Support for arbitrary input frame length

This block supports input signals with arbitrary frame lengths when the:

- Input signal is a fixed-size signal (frame length does not change
  during simulation) and you select the **Allow arbitrary frame
  length for fixed-size input signals** parameter.
- Input signal is a variable-size signal (frame length changes during
  simulation).

When this block supports an input signal with an arbitrary frame length, the input frame
length does not have to be a multiple of the decimation factor.

## Description

Multistage sample-rate conversion

The Sample-Rate Converter block implements a multistage FIR sample-rate
converter. The multistage FIR converter converts the rate of each channel of the input
signal from the input sample rate to the output sample rate. Multistage implementations
minimize the amount of computation required for the sample-rate conversions by first
reducing the sample rate of the input signal. Next, the block determines the optimal
number of decimators and interpolators based on the parameters you specify in the block
dialog box. The block then accordingly designs filters in the individual stages.

This block supports SIMD code generation. For details, see Code Generation.
