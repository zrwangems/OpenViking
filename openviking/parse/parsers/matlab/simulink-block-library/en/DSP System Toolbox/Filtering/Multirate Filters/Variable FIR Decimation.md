---
type: simulink-block
title: 'Variable FIR Decimation'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'variablefirdecimation'
documentation_source_path: 'ref/variablefirdecimation.html'
language: en
---

# Variable FIR Decimation

## Ports

### Input

### **u** — Data input vector | matrix

Specify the data input as a vector or a matrix of size
*P*-by-*Q*. The block treats each column of the
input signal as a separate channel. If the input is a two-dimensional signal, the
first dimension represents the channel length (or frame size) and the second dimension
represents the number of channels. If the input is a one-dimensional signal, then the
block interprets it as a single channel.

The block accepts variable-size input signals, that is, you can change the size of
each input channel during simulation, but you cannot change the number of
channels.

When you set
**Specification** to `Output frame
length`, the input frame length *P* must be an integer
multiple of the output frame length
*Po*. *(since R2023b)*

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **M** — Decimation factor input port positive integer

Specify the decimation factor *M* as a positive integer that is
an integer factor of the maximum decimation factor. For example, if you set
**Maximum decimation factor** to 24, then the possible values for
decimation factor are 1, 2, 3, 4, 6, 8, 12, and 24.

You can tune the decimation factor while the simulation is running. For an
example, see Decimate Sinusoidal Signal with Tunable Decimation Factor.

#### Dependencies

To enable this port:

- Set
  **Specification** to `Decimation
  factor`. *(since R2023b)*
- Select the **Specify decimation factor from input port**
  parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **coeffs** — Prototype filter coefficients vector

Specify the lowpass FIR filter coefficients in descending powers of
*z* as a vector.

The transfer function *H*(*z*) of the FIR filter
is given by:

H(z)=b0+b1z−1+...+bNz−N,

You can generate the FIR filter coefficient vector, **b** = [*b0*,
*b1*, …,
*bN*], using one of the DSP System Toolbox™ filter design functions such as `designMultirateFIR`, `firnyquist`, `firgr`, or `firceqrip`.

Compute the filter coefficients based on the maximum decimation factor
*Mmax* instead of the decimation factor
*M*. For example, if *Mmax*
is 24 and *M* is 8, and you used
`designMultirateFIR` as the design function, compute the filter
coefficients using `designMultirateFIR(1,24)` instead of
`designMultirateFIR(1,8)`.

To act as an effective anti-aliasing filter, the coefficients usually correspond
to a lowpass filter with a normalized cutoff frequency no greater than 1/*Mmax*. To design such a filter, use the `designMultirateFIR` function.

The block internally initializes all filter states to zero.

You can change the filter coefficients during simulation but the number of filter
coefficients must remain constant. For an example, see Specify Filter Coefficients Through Input Port.

#### Dependencies

To enable this port, set the **Numerator source** parameter to
`Input port`.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **y** — Decimated output vector | matrix

Decimated output, returned as a vector or a matrix.

When you set the **Specification**
parameter to `Decimation factor` *(since R2023b)*, the size of the
output signal is same as the size of the input signal. However, the block computes a
maximum of
`ceil`(*P*/*M*)-by-*Q*
output samples, where *P* is the input frame size,
*Q* is the number of input channels, and *M* is
the decimation factor.

If the input is a variable-size signal, the block outputs a variable-size signal
so as to maintain the decimation factor.

When you set the
**Specification** parameter to `Output frame
length`, the size of the output signal is
*Po*-by-*Q*, where
*Po* is the value you specify in the
**Output frame length** parameter. *(since R2023b)*

If the input is a variable-size signal, the
block varies the decimation factor accordingly and outputs a fixed-size signal. *(since R2023b)*

The complexity of the output signal depends on the complexity of the input signal
and the complexity of the filter coefficients. See this table for more details.

| Input Signal | Filter Coefficients | Output Signal |
| --- | --- | --- |
| Real | Complex | Complex |
| Real | Real | Real |
| Complex | Complex | Complex |
| Complex | Real | Complex |

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

### **Specification** — Specify mode to control decimation factor `Decimation factor` (default) | `Output frame length`

*Since R2023b*

Specify the mode in which you control the decimation factor.

When you set **Specification** to:

- `Decimation factor` –– The block maintains the
  decimation factor that you specify. If the input signal frame length changes
  during simulation (variable-size input signal), the output frame length changes in
  a way so as to maintain the decimation factor *M*.

  A variable-size input generates a variable-size output.
- `Output frame length` –– The block maintains the
  output frame length that you specify. If the input signal frame length changes
  during simulation (variable-size input signal), the decimation factor changes in a
  way so as to maintain the output frame length
  *Po*.

  A variable-size input generates a fixed-size output.

### **Maximum decimation factor** — Maximum decimation factor `24` (default) | positive integer

Specify the maximum decimation factor
*Mmax* as a positive integer. The decimation
factor you specify through the input port **M** must be a
factor of the value you specify in this parameter.

When you set the
**Specification** parameter to `Output frame
length`, the block treats the input frame length as the maximum
decimation factor *Mmax*. *(since R2023b)*

#### Dependencies

To enable this port, set the
**Specification** parameter to `Decimation
factor`. *(since R2023b)*

### **Specify decimation factor from input port** — Specify decimation factor from input port `on` (default) | `off`

When you select this parameter, you can specify the decimation factor through the
input port **M**. When you clear this parameter, you can specify the
decimation factor in the block dialog box through the **Decimation
factor** parameter.

#### Dependencies

To enable this parameter, set the
**Specification** parameter to `Decimation
factor`. *(since R2023b)*

### **Decimation factor** — Decimation factor `24` (default) | positive integer

Specify the decimation factor *M* as a positive integer that is an
integer factor of the maximum decimation factor
*Mmax*. For example, if you set
**Maximum decimation factor** to 24, then the possible values for
**Decimation factor** are 1, 2, 3, 4, 6, 8, 12, and 24.

You can tune the decimation factor while the simulation is running.

When you set the
**Specification** parameter to `Output frame
length`, the block treats the ratio of the input frame length
*P* to the output frame length
*Po* as the decimation factor
*M*, that is, *M* =
*P*/*Po*. *(since R2023b)*

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set the
  **Specification** parameter to `Decimation
  factor`. *(since R2023b)*
- Clear the **Specify decimation factor from input port**
  parameter.

### **Output frame length** — Output frame length `48` (default) | positive integer

*Since R2023b*

Specify the output frame length *Po* as a
positive integer. In this mode, the block maintains the frame length of the output
signal at the value you specify in this parameter. If the input signal frame length
changes during simulation (variable-size input signal), the decimation factor of the
block changes in a way so as to maintain the output frame length.

The input frame length must be an integer multiple of the output frame
length.

The value you specify in this parameter determines the current decimation factor
*M*. For more details, see the **Decimation factor**
parameter.

#### Dependencies

To enable this parameter, set the **Specification** parameter to
`Output frame length`.

### **Numerator source** — FIR filter coefficient source `Auto` (default) | `Dialog parameter` | `Input port`

Specify the FIR filter coefficient source as one of the following:

- `Auto` –– The block designs an FIR decimator using
  the `designMultirateFIR` function. This
  function designs the filter and returns the coefficients used by the block.

  For more information on the filter design, see Orfanidis [1].
- `Dialog parameter` –– Specify the filter coefficients
  through the **Prototype filter numerator coefficients** parameter
  in the block dialog box.
- `Input port` –– Specify the filter coefficients
  through the **coeffs** input port.

### **Prototype filter numerator coefficients** — Prototype lowpass FIR filter coefficients `designMultirateFIR(1,24)` (default) | vector

Specify the prototype lowpass FIR filter coefficients in descending powers of
*z* as a vector. By default,
`designMultirateFIR(1,24)` computes the filter coefficients with
the maximum decimation factor *Mmax* of
24.

The transfer function *H*(*z*) of the FIR filter
is given by:

H(z)=b0+b1z−1+...+bNz−N,

You can generate the FIR filter coefficient vector, **b** = [*b0*,
*b1*, …,
*bN*], using one of the DSP System Toolbox filter design functions such as `designMultirateFIR`, `firnyquist`, `firgr`, or `firceqrip`.

Compute the filter coefficients based on the maximum decimation factor
*Mmax* instead of the decimation factor
*M*. For example, if *Mmax*
is 24 and *M* is 8, and you used
`designMultirateFIR` as the design function, compute the filter
coefficients using `designMultirateFIR(1,24)` instead of
`designMultirateFIR(1,8)`.

To act as an effective anti-aliasing filter, the coefficients usually correspond to
a lowpass filter with a normalized cutoff frequency no greater than 1/*Mmax*. To design such a filter, use the `designMultirateFIR` function.

The block internally initializes all filter states to zero.

#### Dependencies

To enable this parameter, set the **Numerator source** parameter
to `Dialog parameter`.

**Tunable:** Yes

### **View Filter Response** — View Filter Response button

Click this button to open the filter visualizer and display the magnitude response
of the variable FIR decimation filter. The response is based on the parameters you
select in the block dialog box. To update the magnitude response while the dynamic
filter visualizer is running, modify the parameters in the dialog box and click
**Apply**.

You can configure the plot settings and the signal measurements from the interface
of the visualizer.

On the **Scope** tab, the **Configuration**
section allows you to modify the plot settings. Click **Magnitude
Phase** to display the magnitude and phase response of the filter. On the
**Measurements** tab, you can measure the signal statistics, place
data cursors, and display the peak values of the selected signal.

For more details on the filter visualizer interface and its tools, see Configure Filter Visualizer.

#### Dependencies

You cannot view the filter response when you set the **Specification** parameter to `Output frame
length` *(since R2023b)* or the **Numerator source**
parameter to `Input port`. To view the filter response, set
the **Specification** parameter to
`Decimation factor` *(since R2023b)* and the **Numerator
source** parameter to `Auto` or
`Dialog parameter`.

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

DSP System Toolbox / Filtering / Multirate Filters

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

## Version History

**Introduced in R2023a**

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

### R2023b: Variable FIR Decimation block can generate fixed-size output signal for variable-size input signal

When you set **Specification** to `Output frame
length` and specify a value for the **Output frame length**
parameter, the Variable FIR Decimation block generates a fixed-size output
signal. To maintain the fixed-size at the output even when the input frame size changes
during simulation (variable-size), the block varies the decimation factor
*M*.

When you set **Specification** to `Decimation
factor`, you specify the decimation factor directly in the block dialog box.
In this mode, for a variable-size input signal, the block generates a variable-size output
signal. The decimation factor *M* remains constant.

## Description

Polyphase FIR decimation with tunable decimation factor

The Variable FIR Decimation block performs an efficient polyphase FIR
decimation with a tunable decimation factor. You can update the decimation factor and the
filter coefficients in the block dialog box or through an input port while the simulation is
running. To control the decimation, you can specify the decimation factor or the output frame
length.

When you specify the decimation factor, if the input frame length changes (variable-size
signal) during simulation, the output frame length also changes in order to keep the
decimation factor constant. When you specify the output frame length instead of the decimation
factor, and if the input frame length changes (variable-size signal) during simulation, the
decimation factor also changes in order to keep the output frame length constant.

Conceptually, the FIR decimator (as shown in the schematic) consists of an anti-aliasing
FIR filter followed by a downsampler. To design an FIR anti-aliasing filter, use the `designMultirateFIR` function.

The FIR filter filters the data in each channel of the input using a direct-form FIR
filter. The downsampler that follows downsamples each channel of filtered data by taking every
*M*-th sample and discarding the *M* – 1 samples that follow. *M* is the value of the decimation
factor. The resulting discrete-time signal has a sample rate that is 1/*M*
times the original sample rate.

FIR decimator contains an anti-aliasing FIR filter followed by a downsampler.

Note that the actual block algorithm implements a direct-form FIR polyphase structure, an
efficient equivalent of the combined system depicted in the diagram. For more details, see
Algorithms.

The block supports C and C++ code generation.
