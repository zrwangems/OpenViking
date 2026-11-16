---
type: simulink-block
title: 'Zoom FFT'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'zoomfft'
documentation_source_path: 'ref/zoomfft.html'
language: en
---

# Zoom FFT

## Ports

### Input

### **x** — Input data vector | matrix

Input data for which the block computes zoom FFT, specified as a
vector or a matrix.

The block treats each column of the input signal as a separate
channel. If the input is a two-dimensional signal, the first dimension
represents the channel length (or frame size) and the second dimension
represents the number of channels. If the input is a one-dimensional
signal, then the block interprets it as a single-channel signal.

When you input a variable-size signal (frame length changes during
simulation), the frame length of the signal can be arbitrary, that is,
the input frame length does not have to be a multiple of the decimation
factor. When you input a fixed-size signal (frame length does not change
during simulation), the frame length can be arbitrary only when you
select the **Allow arbitrary frame length for
fixed-size input signals** parameter.

This port is unnamed until you select the **Specify center
frequency from input port** parameter and click
**Apply**.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Fc** — Center frequency input real scalar

Center frequency of the desired band, specified as a real scalar in
the range (– *Fs*/2, *Fs*/2), where
*Fs* is the sample rate of the input signal. If you
set **Sample rate mode** to `Inherit from
input port` or `Specify on
dialog`, the block inherits *Fs* from
the input signal or uses the value of the **Input sample rate
(Hz)** parameter, respectively. If you set **Sample rate mode** to
`Use normalized frequency (0 to 1)`,
the block sets *Fs* to 2 *(since R2024b)*.

#### Dependency

To enable this port, select the **Specify center frequency
from input port** check box and click
**Apply**.

**Data Types:** `single` | `double`
### Output Arguments

### **Port\_1** — Zoom FFT output vector | matrix

Zoom FFT output, returned as a vector or matrix.

If you select the **Inherit FFT Length from input
dimensions** check box, the dimensions of the output signal
depend on the dimensions of the input signal, the decimation factor of
the Zoom FFT block, and whether you select the
**Allow arbitrary frame length for fixed-size input
signals** parameter.

This table provides more details on the dimensions of the output
signal when you input a fixed-size input signal.

**Fixed-Size Input Signal**

| Input Signal | Output Signal Dimensions |
| --- | --- |
| *P*-by-1 column vector, where *P* is a multiple of the decimation factor *D* | (*P*/*D*)-by-1 |
| *P*-by-1 column vector, where *P* is not a multiple of the decimation factor *D* | `ceil`(*P*/*D*)-by-1 when you select **Allow arbitrary frame length for fixed-size input signals**.  If you do not select **Allow arbitrary frame length for fixed-size input signals**, the block errors. |
| *P*-by-*Q* matrix, where *P* is a multiple of the decimation factor *D* | (*P*/*D*)-by-*Q* |
| *P*-by-*Q* matrix, where *P* is not a multiple of the decimation factor *D* | `ceil`(*P*/*D*)-by-*Q* when you select **Allow arbitrary frame length for fixed-size input signals**.  If you do not select **Allow arbitrary frame length for fixed-size input signals**, the block errors. |

This table gives more details on the dimensions of the output signal
when you input a variable-size input signal. When you input a
variable-size signal (frame length changes during simulation), the
**Allow arbitrary frame length for fixed-size
input signals** is visible on the block dialog box but does
not have any impact on the input frame length. You can input a
variable-size signal of any frame length even if you do not select the
**Allow arbitrary frame length for fixed-size
input signals** parameter.

**Variable-Size Input Signal**

| Input Signal | Output Signal Dimensions |
| --- | --- |
| *P*-by-*Q* | `ceil`(*P*/*D*)-by-*Q* |

If you clear the **Inherit FFT Length from input
dimensions** check box, the output frame size equals the
value you specify in the **FFT
length**(*L*) parameter.

| Input Signal | Output Signal Dimensions |
| --- | --- |
| *P*-by-*Q* | *L*-by-*Q* |

The data type of the output is same as the data type of the
input.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

### **Decimation factor** — Decimation factor `2` (default) | positive integer

Specify the decimation factor as a positive integer. This value specifies
the factor by which the block reduces the bandwidth of the input signal. The
number of rows in the input signal must be a multiple of the decimation
factor.

**Example:**
`4`

**Example:**
`8`

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Specify center frequency from input port** — Flag to specify center frequency from input port `'off'` (default) | `'on'`

When you select this option and click **Apply**, the
input port **Fc** appears on the block icon. You can pass
the center frequency through this input port as a scalar.

### **Center frequency** — Center frequency `0` (default) | real scalar

Specify the center frequency of the desired band as a real scalar in Hz
or in normalized frequency units *(since R2024b)*.
The center frequency must be in the range (– *Fs*/2,
*Fs*/2), where *Fs* is the sample rate
of the input signal. If you set **Sample rate mode** to
`Inherit from input port` or
`Specify on dialog`, the block inherits
*Fs* from the input signal or uses the value of the
**Input sample rate (Hz)** parameter, respectively.
If you set **Sample rate
mode** to `Use normalized frequency (0 to
1)`, the block sets *Fs* to
2 *(since R2024b)*.

**Example:**
`0.5`

**Example:**
`10`

#### Dependencies

This parameter applies when you clear the **Specify center
frequency from input port** check box.

**Data Types:** `single` | `double`

### **Inherit FFT Length from input dimensions** — Flag to inherit FFT length from input dimensions `'on'` (default) | `'off'`

When you select this option, the FFT length is the ratio of the input
frame size (number of rows in the input) and the **Decimation
factor**.

### **FFT length** — FFT length `64` (default) | positive scalar

Specify the FFT length as a positive integer. The FFT length must be
greater than or equal to the ratio of the frame size (number of input rows)
and the **Decimation factor**.

**Example:** `24`

**Example:** `52`

#### Dependencies

To enable this parameter, clear the **Inherit FFT Length from
input dimensions** check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Sample rate mode** — Mode to specify input sample rate `Use normalized frequency (0 to 1)` (default) | `Specify on dialog` | `Inherit from input port`

*Since R2024b*

Specify the input sample rate using one of these options:

- `Use normalized frequency (0 to 1)`
  –– Specify the center frequency of the desired band in
  normalized frequency units (0 to 1).
- `Specify on dialog` –– Specify the
  input sample rate in the block dialog box using the
  **Input sample rate (Hz)**
  parameter.
- `Inherit from input port` –– The
  block inherits the sample rate from the input signal.

### **Input sample rate (Hz)** — Input sample rate `44100` (default) | positive real scalar

Specify the input sample rate *Fs* as a real positive
scalar in Hz.

**Example:** `44100`

**Example:** `48000`

#### Dependencies

To enable this parameter, set
the **Sample rate mode** parameter to
`Specify on dialog`. *(since R2024b)*

### **Allow arbitrary frame length for fixed-size input signals** — Allow arbitrary frame length for fixed-size input signals `off` (default) | `on`

*Since R2023a*

Specify whether fixed-size input signals (whose size does not change
during simulation) can have an arbitrary frame length, where the frame
length does not have to be a multiple of the decimation factor. The block
uses this parameter only for fixed-size input signals and ignores it if the
input has a variable-size.

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

DSP System Toolbox / Transforms

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `No` |
| **Variable-Size Signals** | `Yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

### R2024b: Support for normalized frequencies

When you set the **Sample rate mode** parameter to
`Use normalized frequency (0 to 1)`, you can specify
the center frequency of the desired band in normalized frequency units (0 to
1).

### R2023a: Support for arbitrary input frame length

This block supports input signals with arbitrary frame lengths when the:

- Input signal is a fixed-size signal (frame length does not change
  during simulation) and you select the **Allow arbitrary frame
  length for fixed-size input signals** parameter.
- Input signal is a variable-size signal (frame length changes during
  simulation).

When this block supports an input signal with an arbitrary frame length, the input
frame length does not have to be a multiple of the decimation factor and the output
is a variable-size signal.

## Description

High-resolution FFT of a portion of a spectrum

The Zoom FFT block computes the fast Fourier Transform (FFT) of a
signal over a portion of frequencies in the Nyquist interval. By setting an appropriate
decimation factor *D*, and sampling rate *Fs*, you can
choose the bandwidth of frequencies to analyze *BW*, where
*BW* = *Fs*/*D*. You can also
select a specific range of frequencies to analyze in the Nyquist interval by choosing
the center frequency of the desired band. If you set
**Sample rate mode** to `Use normalized frequency
(0 to 1)`, the block sets *BW* as
2/*D*. *(since R2024b)*

The resolution of a signal is the ratio of *Fs* and the FFT length
(*L*). Using zoom FFT, you can retain the same resolution you would
achieve with a full-size FFT on your original signal by computing a small FFT on a
shorter signal. The shorter signal comes from decimating the original signal. The
savings come from being able to compute a much shorter FFT while achieving the same
resolution. For a decimation factor of *D*, the new sampling rate,
*Fsd*, is *Fs*/*D*, and the new
frame size (and FFT length) is *Ld* =
*L*/*D*. The resolution of the decimated signal is
*Fsd*/*Ld* =
*Fs*/*L*. To achieve a higher resolution of the
shorter band, use the original FFT length, *L*, instead of the
decimated FFT length, *Ld*.
