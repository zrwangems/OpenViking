---
type: simulink-block
title: 'Moving RMS'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'movingrms'
documentation_source_path: 'ref/movingrms.html'
language: en
---

# Moving RMS

## Ports

### Input

### **x** — Data input vector | matrix

The block computes the moving RMS of the data specified at this input port. Specify
real- or complex-valued multichannel inputs of the size
*m*-by-*n*, where *m* ≥ 1 and
*n* ≥ 1.

When the **Allow arbitrary frame length for fixed-size input signals**
parameter appears and is not selected, and you input a fixed-size signal, the frame length
must be a multiple of the hop size (window length − overlap length). In all other cases, the
input frame length can be arbitrary.

The block accepts variable-size inputs (frame length changes during simulation). When
you input a variable-size signal, the frame length of the signal can be arbitrary.

This port is unnamed until you set **Method** to
`Exponential weighting` and select the **Specify forgetting
factor from input port** parameter.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **lambda** — Forgetting factor non-negative real scalar in the range [0,1]

Specify the forgetting factor as a non-negative real scalar in the range [0,1]. The
forgetting factor determines how much weight past data is given. A forgetting factor of 0.9
gives more weight to the older data than does a forgetting factor of 0.1. A forgetting factor
of 1.0 indicates infinite memory and all previous samples are given an equal weight. A
forgetting factor of 0 indicates no memory and the past samples have no weight on the current
computation.

#### Dependencies

This port appears when you set **Method** to `Exponential
weighting` and select the **Specify forgetting factor from input
port** parameter.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Moving RMS output vector | matrix

Moving RMS output, returned as a vector or a matrix. The block computes the moving RMS
based on the **Method** parameter settings using either the sliding window
method or the exponential weighting method. For more details, see Algorithms.

This table provides more details on the dimensions of the output signal.

| Input Signal | Input Dimensions | Output Dimensions When **Allow arbitrary frame length for fixed-size input signals** Appears | Output Dimensions When **Allow arbitrary frame length for fixed-size input signals** Does Not Appear |
| --- | --- | --- | --- |
| Fixed-size signal | *m*-by-*n*, where *m* is a multiple of the hop size (window length − overlap length) | (*m*/hop size)-by-*n* | *m*-by-*n* |
| Fixed-size signal | *m*-by-*n*, where *m* is not a multiple of the hop size (window length − overlap length) | `ceil`(*m*/hop size)-by-*n* when you select **Allow arbitrary frame length for fixed-size input signals**  If you do not select **Allow arbitrary frame length for fixed-size input signals**, the block errors. | *m*-by-*n* |
| Variable-size signal | *m*-by-*n* | `ceil`(*m*/hop size)-by-*n* | *m*-by-*n* |

When the output has an upper bound size of
`ceil`(*m*/hop size)-by-*n*, during
simulation, the size of the first dimension varies within this bound and the size of the
second dimension remains constant. For an example that shows this behavior, see Compute Moving RMS of Noisy Step Signal.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

If a parameter is listed as tunable, then you can change its value during simulation.

### **Method** — Moving RMS method `Sliding window` (default) | `Exponential weighting`

- `Sliding window` — A window of length **Window
  length** moves over the input data along each channel. For every sample the
  window moves over, the block computes the RMS over the data in the window.
- `Exponential weighting` — The block multiplies the
  squares of the samples by a set of weighting factors. The magnitude of the weighting
  factors decreases exponentially as the age of the data increases, but the magnitude never
  reaches zero. To compute the RMS, the algorithm sums the weighted data and takes a square
  root of the sum.

### **Specify window length** — Flag to specify window length on (default) | off

When you select this check box, the length of the sliding window is equal to the value
you specify in **Window length**. When you clear this check box, the length
of the sliding window is infinite. In this mode, the block computes the RMS of the current
sample and all the previous samples in the channel.

#### Dependencies

To enable this parameter, set **Method** to `Sliding
window`.

### **Window length** — Length of sliding window 4 (default) | positive scalar integer

Specifies the length of the sliding window in samples.

#### Dependencies

To enable this parameter, set **Method** to `Sliding
window` and select the **Specify window length** check
box.

### **Overlap length** — Overlap length between windows `3` (default) | nonnegative integer

Specify the overlap length between sliding windows as a nonnegative integer. The value of
overlap length varies in the range [0, **Window length** − 1].

#### Dependencies

To enable this parameter, set **Method** to `Sliding
window` and select the **Specify window length** check
box.

### **Allow arbitrary frame length for fixed-size input signals** — Allow arbitrary frame length for fixed-size input signals off (default) | on

Specify whether fixed-size input signals (whose size does not change during simulation)
can have an arbitrary frame length, where the frame length does not have to be a multiple of
the hop size. Hop size is defined as **Window length** − **Overlap
length**. The block uses this parameter setting only for fixed-size input signals
and ignores this parameter if the input has a variable-size.

When the input signal is a variable-size signal, the signal can have arbitrary frame
length, that is, the frame length does not have to be a multiple of the hop size.

For fixed-size input signals, if you:

- Select the **Allow arbitrary frame length for fixed-size input
  signals** parameter, the frame length of the signal does not have to be a
  multiple of the hop size. If the input is not a multiple of the hop size, then the output
  is generally a variable-size signal. Therefore, to support arbitrary input size, the block
  must also support variable-size operations, which you can enable by selecting the
  **Allow arbitrary frame length for fixed-size input signals**
  parameter.
- Clear the **Allow arbitrary frame length for fixed-size input
  signals** parameter, the input frame length must be a multiple of the hop
  size.

#### Dependencies

To enable this parameter, set **Method** to `Sliding
window` and select the **Specify window length** check
box.

### **Specify forgetting factor from input port** — Flag to specify forgetting factor off (default) | on

When you select this check box, the forgetting factor is input through the
**lambda** port. When you clear this check box, the forgetting factor is
specified on the block dialog through the **Forgetting factor**
parameter.

#### Dependencies

To enable this parameter, set **Method** to `Exponential
weighting`.

### **Forgetting factor** — Exponential weighting factor 0.9 (default) | non-negative real scalar in the range [0,1]

Specify the exponential weighting factor as a non-negative real scalar in the range
[0,1]. This value determines how much weight the past data is given. A forgetting factor of
0.9 gives more weight to the older data than does a forgetting factor of 0.1. A forgetting
factor of 1.0 indicates infinite memory and all the past samples are given an equal weight. A
forgetting factor of 0 indicates no memory and the past samples have no weight on the current
computation.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Method** to `Exponential
weighting` and clear the **Specify forgetting factor from input
port** check box.

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

DSP System Toolbox / Statistics

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `No` |
| **Variable-Size Signals** | `Yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2024b: Specify a forgetting factor of 0

You can now specify a forgetting factor of 0 in the Moving RMS block.

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

### R2022b: New **Overlap length** parameter

Starting in R2022b, you can specify the overlap length between sliding windows using the
**Overlap length** parameter.

### R2022b: Support for arbitrary input frame length

Moving RMS block supports input signals with arbitrary frame lengths when the:

- Input signal is a fixed-size signal (frame length does not change during simulation) and
  you select the **Allow arbitrary frame length for fixed-size input signals**
  parameter (if enabled).
- Input signal is a variable-size signal (frame length changes during simulation).

When this block supports an arbitrary frame length input signal, the input frame length
does not have to be a multiple of the hop size.

## Description

Moving root mean square (RMS)

The Moving RMS block computes the moving root mean square (RMS) of the input
signal along each channel independently over time. The block uses either the sliding window
method or the exponential weighting method to compute the moving RMS. In the sliding window
method, a window of specified length moves over the data sample by sample, and the block computes
the RMS over the data in the window. In the exponential weighting method, the block squares the
data samples, multiplies them with a set of weighting factors, and sums the weighed data. The
block then computes the RMS by taking the square root of the sum. For more details on these
methods, see Algorithms.
