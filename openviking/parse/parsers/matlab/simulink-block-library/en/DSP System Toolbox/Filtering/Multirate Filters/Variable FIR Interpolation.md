---
type: simulink-block
title: 'Variable FIR Interpolation'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'variablefirinterpolation'
documentation_source_path: 'ref/variablefirinterpolation.html'
language: en
---

# Variable FIR Interpolation

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

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **L** — Interpolation factor input port positive integer

Specify the interpolation factor *L* as a positive integer that
is an integer factor of the maximum interpolation factor. For example, if you set
**Maximum interpolation factor** to 24, then the possible values
for interpolation factor are 1, 2, 3, 4, 6, 8, 12, and 24.

You can tune the interpolation factor while the simulation is running. For an
example, see Interpolate Sinusoidal Signal with Tunable Interpolation Factor.

#### Dependencies

To enable this port:

- Set
  **Specification** to `Interpolation
  factor`. *(since R2023b)*
- Select the **Specify interpolation factor from input
  port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **coeffs** — Prototype filter coefficients vector

Specify the numerator coefficients of the FIR filter transfer function
*H*(*z*).

H(z)=b0+b1z−1+...+bNz−N,

You can generate the FIR filter coefficient vector, **b** = [*b0*,
*b1*, …,
*bN*], using one of the DSP System Toolbox™ filter design functions such as `designMultirateFIR`, `firnyquist`, `firgr` or `firceqrip`.

Compute the filter coefficients based on the maximum interpolation factor
*Lmax* instead of the interpolation factor
*L*. For example, if *Lmax*
is 24 and *L* is 8, and you used
`designMultirateFIR` as the design function, compute the filter
coefficients using `designMultirateFIR(24,1)` instead of
`designMultirateFIR(8,1)`.

To act as an effective anti-imaging filter, the coefficients usually correspond to
a lowpass filter with a normalized cutoff frequency no greater than the reciprocal of
the maximum interpolation factor. To design such a filter, use the `designMultirateFIR` function.

The block internally initializes all filter states to zero.

You can change the filter coefficients during simulation but the number of filter
coefficients must remain constant. For an example, see Specify Filter Coefficients Through Input Port.

#### Dependencies

To enable this port, set the **Numerator source** parameter to
`Input port`.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **y** — Interpolated output vector | matrix

Interpolated output, returned as a vector or a matrix.

When you set the **Specification**
parameter to `Interpolation factor` *(since R2023b)*, the size of
the output signal is *Lmax* ×
*P*-by-*Q*, where *P* is the
input frame size, *Q* is the number of input channels, and
*Lmax* is the maximum interpolation
factor. However, the block computes only *L* ×
*P*-by-*Q* samples. The remaining samples in the
output signal are zero.

If the input is a variable-size signal, the block outputs a variable-size signal
so as to maintain the interpolation factor.

When you set the
**Specification** parameter to `Output frame
length`, the size of the output signal is
*Po*-by-*Q*, where
*Po* is the value you specify in the
**Output frame length** parameter. *(since R2023b)*

If the input is a variable-size signal, the
block varies the interpolation factor accordingly and outputs a fixed-size
signal. *(since R2023b)*

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

### **Specification** — Specify mode to control interpolation factor `Interpolation factor` (default) | `Output frame length`

*Since R2023b*

Specify the mode in which you control the interpolation factor.

When you set **Specification** to:

- `Interpolation factor` –– The block maintains the
  interpolation factor that you specify. If the input signal frame length changes
  during simulation (variable-size input signal), the output frame length changes in
  a way as to maintain the interpolation factor *L*.

  A variable-size input generates a variable-size output.
- `Output frame length` –– The block maintains the
  output frame length that you specify. If the input signal frame length changes
  during simulation (variable-size input signal), the interpolation factor changes
  in a way as to maintain the output frame length
  *Po*.

  A variable-size input generates a fixed-size output.

### **Maximum interpolation factor** — Maximum interpolation factor `24` (default) | positive integer

Specify the maximum interpolation factor
*Lmax* as a positive integer. The
interpolation factor you specify through the input port **L** must be a factor of the value you specify in this parameter.

When you set the
**Specification** parameter to `Output frame
length`, the block treats the output frame length as the maximum
interpolation factor *Lmax*. *(since R2023b)*

#### Dependencies

To enable this port, set the
**Specification** parameter to `Interpolation
factor`. *(since R2023b)*

### **Specify interpolation factor from input port** — Specify interpolation factor from input port `on` (default) | `off`

When you select this parameter, you can specify the interpolation factor through the
input port **L**. When you clear this parameter, you can specify the
interpolation factor in the block dialog box through the **Interpolation
factor** parameter.

#### Dependencies

To enable this parameter, set the
**Specification** parameter to `Interpolation
factor`. *(since R2023b)*

### **Interpolation factor** — Interpolation factor `24` (default) | positive integer

Specify the interpolation factor *L* as a positive integer that is
an integer factor of the maximum interpolation factor. For example, if you set
**Maximum interpolation factor** to 24, then the possible values for
**Interpolation factor** are 1, 2, 3, 4, 6, 8, 12, and 24.

You can tune the interpolation factor while the simulation is running.

When you set the
**Specification** parameter to `Output frame
length`, the block treats the ratio of the output frame length
*Po* to the input frame length
*P* as the interpolation factor *L*, that is,
*L* =
*Po*/*P*. *(since R2023b)*

**Tunable:** Yes

#### Dependencies

To enable this parameter:

- Set the
  **Specification** parameter to `Interpolation
  factor`. *(since R2023b)*
- Clear the **Specify interpolation factor from input port**
  parameter.

### **Output frame length** — Output frame length `48` (default) | positive integer

*Since R2023b*

Specify the output frame length *Po* as a
positive integer. In this mode, the block maintains the frame length of the output
signal at the value you specify in this parameter. If the input signal frame length
changes during simulation (variable-size input signal), the interpolation factor of the
block changes in a way as to maintain the output frame length.

The input frame length must be a divisor of the output frame length.

The value you specify in this parameter determines the maximum interpolation factor
*Lmax* and the current interpolation factor
*L*. For more details, see the **Maximum interpolation
factor** and the **Interpolation factor** parameters.

#### Dependencies

To enable this parameter, set the **Specification** parameter to
`Output frame length`.

### **Numerator source** — FIR filter coefficient source `Auto` (default) | `Dialog parameter` | `Input port`

Specify the FIR filter coefficient source as one of the following:

- `Auto` –– The block designs an FIR interpolator using
  the interpolation factor in the **Interpolation factor**
  parameter. The `designMultirateFIR` function designs
  the filter and returns the coefficients used by the block.

  For more information on the filter design, see Orfanidis [1].
- `Dialog parameter` –– Specify the filter coefficients
  through the **Prototype filter numerator coefficients** parameter
  in the block dialog box.
- `Input port` –– Specify the filter coefficients
  through the **coeffs** input port.

### **Prototype filter numerator coefficients** — Prototype filter coefficients `designMultirateFIR(24,1)` (default) | vector

Specify the numerator coefficients of the FIR filter transfer function
*H*(*z*).

H(z)=b0+b1z−1+...+bNz−N,

You can generate the FIR filter coefficient vector, **b** = [*b0*,
*b1*, …,
*bN*], using one of the DSP System Toolbox filter design functions such as `designMultirateFIR`, `firnyquist`, `firgr` or `firceqrip`.

Compute the filter coefficients based on the maximum interpolation factor
*Lmax* instead of the interpolation factor
*L*. For example, if *Lmax*
is 24 and *L* is 8, and you used
`designMultirateFIR` as the design function, compute the filter
coefficients using `designMultirateFIR(24,1)` instead of
`designMultirateFIR(8,1)`.

To act as an effective anti-imaging filter, the coefficients usually correspond to a
lowpass filter with a normalized cutoff frequency no greater than the reciprocal of the
maximum interpolation factor. To design such a filter, use the `designMultirateFIR` function.

The block internally initializes all filter states to zero.

You can change the filter coefficients during simulation but the number of filter
coefficients must remain constant.

#### Dependencies

To enable this parameter, set the **Numerator source** parameter
to `Dialog parameter`.

**Tunable:** Yes

### **View Filter Response** — View Filter Response button

Click this button to open the filter visualizer and display the magnitude response
of the variable FIR interpolation filter. The response is based on the parameters you
select in the block dialog box. To update the magnitude response while the filter
visualizer is running, modify the parameters in the dialog box and click
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
`Interpolation factor` *(since R2023b)* and the
**Numerator source** parameter to `Auto`
or `Dialog parameter`.

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

### R2023b: Variable FIR Interpolation block can generate fixed-size output signal for variable-size input signal

When you set **Specification** to `Output frame
length` and specify a value for the **Output frame length**
parameter, the Variable FIR Interpolation block generates a fixed-size output
signal. To maintain the fixed-size at the output even when the input frame size changes
during simulation (variable-size), the block varies the interpolation factor
*L*.

When you set **Specification** to `Interpolation
factor`, you specify the interpolation factor directly in the block dialog
box. In this mode, for a variable-size input signal, the block generates a variable-size
output signal. The interpolation factor *L* remains constant.

## Description

Polyphase FIR interpolation with tunable interpolation factor

The Variable FIR Interpolation block performs an efficient polyphase FIR
interpolation with a tunable interpolation factor. You can update the interpolation factor and
the filter coefficients in the block dialog box or through an input port while the simulation
is running. To control the interpolation, you can specify the interpolation factor or the
output frame length.

When you specify the interpolation factor, if the input frame length changes
(variable-size signal) during simulation, the output frame length also changes in order to
keep the interpolation factor constant. When you specify the output frame length instead of
the interpolation factor, and if the input frame length changes (variable-size signal) during
simulation, the interpolation factor also changes in order to keep the output frame length
constant.

Conceptually, the FIR interpolator (as shown in the schematic) consists of an upsampler
followed by an FIR anti-imaging filter, which is usually an approximation of an ideal
band-limited interpolation filter. To design an FIR anti-imaging filter, use the `designMultirateFIR` function. The upsampler upsamples each channel of the input
to a higher rate by inserting *L*–1 zeros between samples. The FIR filter
that follows filters each channel of the upsampled data. The resulting discrete-time signal
has a sample rate that is *L* times the original sample rate.

FIR interpolator contains an upsampler followed by an anti-imaging FIR filter.

However, the actual block algorithm implements a direct-form FIR polyphase structure, an
efficient equivalent of the combined system depicted in the diagram. For more details, see
Algorithms.

The block supports C and C++ code generation.
