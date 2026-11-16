---
type: simulink-block
title: 'Power Meter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'powermeter'
documentation_source_path: 'ref/powermeter.html'
language: en
---

# Power Meter

## Ports

### Input

### **Port\_1** — Input signal vector | matrix

Specify the input signal in volts as a vector or a matrix. If
`x` is a matrix, the block treats each column as an independent
channel and computes the power measurement along each channel.

When the **Allow arbitrary frame length for fixed-size input
signals** parameter appears and is not selected, and you input a fixed-size
signal, the frame length must be a multiple of the hop size (window length − overlap
length). In all other cases, the input frame length can be arbitrary.

The block accepts variable-size inputs (frame length changes during simulation).
When you input a variable-size signal, the frame length of the signal can be
arbitrary.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Rst** — Reset port scalar

Specify the boolean reset signal as a scalar. If the input on the
**Rst** port is `true`, the block clears the
internal histograms and statistics before processing the current input. If the input
on the **Rst** port is `false`, the block computes
the measurements from the start of the simulation or from the last reset.

#### Dependencies

To enable this port, select the **Compute CCDF** and
**Reset port** parameters.

**Data Types:** `Boolean`
### Output

### **Avg** — Average power scalar | vector | matrix

Average power of the voltage signal from the start of the simulation or from the
last reset, returned as a scalar, vector, or a matrix. The block computes the average
power along each channel in the units specified in the **Output power
units** parameter. For details on how the block computes the average power,
see Average Power.

If you clear the **Compute CCDF** parameter, the block computes
the moving average power using the Sliding Window Method.

See this table for details on the output signal dimensions.

| Input Signal | Input Dimensions | Output Dimensions When **Allow arbitrary frame length for fixed-size input signals** Appears | Output Dimensions When **Allow arbitrary frame length for fixed-size input signals** Does Not Appear |
| --- | --- | --- | --- |
| Fixed-size signal | *P*-by-*M*, where *M* is a multiple of the hop size (window length − overlap length) | (*P*/hop size)-by-*M* | *P*-by-*M* |
| Fixed-size signal | *P*-by-*M*, where *M* is not a multiple of the hop size (window length − overlap length) | `ceil`(*P*/hop size)-by-*M* when you select **Allow arbitrary frame length for fixed-size input signals**  If you do not select **Allow arbitrary frame length for fixed-size input signals**, the block errors. | *P*-by-*M* |
| Variable-size signal | *P*-by-*M* | `ceil`(*P*/hop size)-by-*M* | *P*-by-*M* |

When the output has an upper bound size of
`ceil`(*P*/hop size)-by-*M*,
during simulation, the size of the first dimension varies within this bound, while the
size of the second dimension remains constant.

If you select the **Compute CCDF** parameter, the block computes
the stationary average power of the entire signal along each channel. In this case,
the size of the output is 1-by-*M*, where *M* is the
number of channels (columns) in the input signal.

#### Dependencies

To enable this port, set **Measurement** to
`Average power` or `All`.

**Data Types:** `single` | `double`

### **Peak** — Peak power scalar | vector | matrix

Peak power of the voltage signal from the start of the simulation or from the last
reset, returned as a scalar, vector, or a matrix. The block computes the peak power
along each channel in the units specified in the **Output power
units** parameter. For details on how the block computes the peak power,
see Peak Power.

If you clear the **Compute CCDF** parameter, the block computes
the moving peak power using the Sliding Window Method.

See this table for details on the output signal dimensions.

| Input Signal | Input Dimensions | Output Dimensions When **Allow arbitrary frame length for fixed-size input signals** Appears | Output Dimensions When **Allow arbitrary frame length for fixed-size input signals** Does Not Appear |
| --- | --- | --- | --- |
| Fixed-size signal | *P*-by-*M*, where *M* is a multiple of the hop size (window length − overlap length) | (*P*/hop size)-by-*M* | *P*-by-*M* |
| Fixed-size signal | *P*-by-*M*, where *M* is not a multiple of the hop size (window length − overlap length) | `ceil`(*P*/hop size)-by-*M* when you select **Allow arbitrary frame length for fixed-size input signals**  If you do not select **Allow arbitrary frame length for fixed-size input signals**, the block errors. | *P*-by-*M* |
| Variable-size signal | *P*-by-*M* | `ceil`(*P*/hop size)-by-*M* | *P*-by-*M* |

When the output has an upper bound size of
`ceil`(*P*/hop size)-by-*M*,
during simulation, the size of the first dimension varies within this bound, while the
size of the second dimension remains constant.

If you select the **Compute CCDF** parameter, the block computes
the stationary peak power of the entire signal along each channel. In this case, the
size of the output is 1-by-*M*, where *M* is the
number of channels (columns) in the input signal.

#### Dependencies

To enable this port, set **Measurement** to `Peak
power` or `All`.

**Data Types:** `single` | `double`

### **PAPR** — Peak-to-average power ratio scalar | vector | matrix

Ratio of the peak power to the average power (PAPR) of the voltage signal,
returned as a scalar, vector, or a matrix. The block computes the peak-to-average
power ratio along each channel. For details on how the block computes this
measurement, see Peak-to-Average Power Ratio.

If you clear the **Compute CCDF** parameter, the block computes
the moving peak-to-average power ratio using the Sliding Window Method.

See this table for details on the output signal dimensions.

| Input Signal | Input Dimensions | Output Dimensions When **Allow arbitrary frame length for fixed-size input signals** Appears | Output Dimensions When **Allow arbitrary frame length for fixed-size input signals** Does Not Appear |
| --- | --- | --- | --- |
| Fixed-size signal | *P*-by-*M*, where *M* is a multiple of the hop size (window length − overlap length) | (*P*/hop size)-by-*M* | *P*-by-*M* |
| Fixed-size signal | *P*-by-*M*, where *M* is not a multiple of the hop size (window length − overlap length) | `ceil`(*P*/hop size)-by-*M* when you select **Allow arbitrary frame length for fixed-size input signals**  If you do not select **Allow arbitrary frame length for fixed-size input signals**, the block errors. | *P*-by-*M* |
| Variable-size signal | *P*-by-*M* | `ceil`(*P*/hop size)-by-*M* | *P*-by-*M* |

When the output has an upper bound size of
`ceil`(*P*/hop size)-by-*M*,
during simulation, the size of the first dimension varies within this bound, while the
size of the second dimension remains constant.

If you select the **Compute CCDF** parameter, the block computes
the stationary peak-to-average power ratio of the entire signal along each channel. In
this case, the size of the output is 1-by-*M*, where
*M* is the number of channels (columns) in the input signal.

PAPR should be less that 100 dB to obtain accurate CCDF measurements. If PAPR is
above 100 dB, the block shows only the highest 100 dB power levels.

#### Dependencies

To enable this port, set **Measurement** to
`Peak-to-average power ratio` or
`All`.

**Data Types:** `single` | `double`

### **RelPwr** — Relative power *N*-by-*M* matrix

Relative power (dB above average power), returned as an
*N*-by-*M* matrix, where:

- *M* is the number of channels (columns) in the input
  signal.
- When you set **CCDF output** to `Relative power
  (dB above average power)`, *N* equals the length
  of the column vector that you specify in the **Specify probability (%)
  for relative power output** parameter.
- When you set **CCDF output** to `Relative power
  and probability (whole CCDF curve)`, *N* equals
  `ceil`(**Power range
  (dB)**/**Power resolution (dB)**) + 1.

Relative power is the power in dB by which the instantaneous signal power is above
the average signal power with a probability of **Prob**, expressed as
a percentage. For details on how the block computes relative power, see Relative Power.

#### Dependencies

To enable this port, select the **Compute CCDF** parameter and
then set the **CCDF output** parameter to `Relative
power (dB above average power)` or `Relative power and
probability (whole CCDF curve)`.

**Data Types:** `single` | `double`

### **Prob** — Probability in percentage *N*-by-*M* matrix

Probability in percentage, returned as an
*N*-by-*M* matrix, where:

- *M* is the number of channels (columns) in the input
  signal.
- When you set **CCDF output** to `Probability
  (%)`, *N* equals the length of the column vector
  that you specify in the **Specify relative power (dB) for probability
  output** parameter.
- When you set **CCDF output** to `Relative power
  and probability (whole CCDF curve)`, *N* equals
  `ceil`(**Power range
  (dB)**/**Power resolution (dB)**) + 1.

**Prob**(*i*)/100 is the probability that the
instantaneous signal power of the *j*th
channel is above its average signal power by
**RelPwr**(*i*,*j*) in dB.

#### Dependencies

To enable this port, select the **Compute CCDF** parameter and
then set the **CCDF output** parameter to `Probability
(%)` or `Relative power and probability (whole CCDF
curve)`.

**Data Types:** `single` | `double`

## Parameters

### **Measurement** — Desired power measurement `Average power` (default) | `Peak power` | `Peak-to-average power ratio` | `All`

Specify the desired power measurement as one of the following:

- `Average power` (default)
- `Peak power`
- `Peak-to-average power ratio`
- `All`

For details on how the block computes these measurements, see Algorithms.

### **Reference load (ohms)** — Reference load in ohms `1` (default) | positive scalar in ohms

Specify the reference load that the power meter uses to compute power values as a
real, positive scalar in ohms.

**Tunable:** Yes

**Data Types:** `single` | `double`

### **Output power units** — Units of measured power values `dBm` (default) | `dBW` | `Watts`

Specify the units of the measured power values as one of the following:

- `dBm`
- `dBW`
- `Watts`

### **Compute CCDF** — Enable CCDF computations off (default) | on

Select the **Compute CCDF** parameter to enable the block to
compute the CCDF of the power of voltage signals. CCDF measurements include the relative
power and the probability (in percentage). Relative power is the amount of power in dB
by which the instantaneous signal power is above the average signal power. Probability
in percentage refers to the probability that the instantaneous signal power is above the
average signal power by the relative power in dB.

These measurements provide a qualitative way to view the power distribution between
the amplitude values of an input signal over time. The CCDF curves (plot of probability
in percentage against relative power in dB) are useful indicators of the dynamic range
of a signal.

When you select **Compute CCDF**:

- The block uses all the input samples from the start of the simulation or from
  a reset signal on the **Rst** port to compute the statistics. The
  power measurements are stationary.
- You can specify variable-size input signals.

When you clear **Compute CCDF**,

- The block does not calculate the CCDF measurements and computes the power
  measurements using the Sliding Window Method.
- The block accepts input signals of arbitrary frame length only when you select
  the **Allow arbitrary frame length for fixed-size input signals**
  parameter.

### **Window length** — Window length `256` (default) | positive integer

Specify the window length over which the block computes the measurement as a
positive integer.

#### Dependencies

To enable this parameter, clear the **Compute CCDF** check box.
When you select **Compute CCDF**, **Window length**
becomes `Inf`.

**Data Types:** `single` | `double`

### **Overlap length** — Overlap length between windows `255` (default) | nonnegative integer

Specify the overlap length between sliding windows as a nonnegative integer. The
value of overlap length varies in the range [0, **Window length** −
1].

#### Dependencies

To enable this parameter, clear the **Compute CCDF** check box.
When you select **Compute CCDF**, **Overlap length**
becomes `0`.

**Data Types:** `single` | `double`

### **Allow arbitrary frame length for fixed-size input signals** — Allow arbitrary frame length for fixed-size input signals off (default) | on

Specify whether fixed-size input signals (whose size does not change during
simulation) can have an arbitrary frame length, where the frame length does not have to
be multiple of the hop size. Hop size is defined as **Window length** −
**Overlap length**. The block uses this parameter setting only for
fixed-size input signals and ignores this parameter if the input has a
variable-size.

When the input signal is a variable-size signal, the signal can have arbitrary frame
length, that is, the frame length does not have to be a multiple of the hop size.

For fixed-size input signals, if you:

- Select the **Allow arbitrary frame length for fixed-size input
  signals** parameter, the frame length of the signal does not have to be
  a multiple of the hop size. If the input is not a multiple of the hop size, then
  the output is generally a variable-size signal. Therefore, to support arbitrary
  input size, the block must also support variable-size operations, which you can
  enable by selecting the **Allow arbitrary frame length for fixed-size
  input signals** parameter.
- Clear the **Allow arbitrary frame length for fixed-size input
  signals** parameter, the input frame length must be a multiple of the
  hop size.

#### Dependencies

To enable this parameter, clear the **Compute CCDF**
parameter.

### **Power range (dB)** — Power range in dB `50` (default) | positive scalar

Specify the *x*-axis range of the CCDF curves as a positive scalar
in dB. The CCDF curves end at the maximum relative power, namely, the PAPR of the
signal, and start at PAPR − **Power range (dB)**. In the CCDF
capability of the Power Meter block, relative power is the power in dB by
which the instantaneous signal power is above the average signal power.

#### Dependencies

To enable this parameter, select the **Compute CCDF** check
box.

**Data Types:** `single` | `double`

### **Power resolution (dB)** — Power Resolution in dB `0.1` (default) | positive scalar

Specify the *x*-axis resolution of the CCDF curves as a positive
scalar in dB.

#### Dependencies

To enable this parameter, select the **Compute CCDF** check
box.

**Data Types:** `single` | `double`

### **CCDF output** — CCDF output `Relative power (dB above average power)` (default) | `Probability (%)` | `Relative power and probability (whole CCDF curve)`

Specify the block to output:

- **RelPwr** –– Relative power (dB above average power). This
  is the amount of power in dB by which the instantaneous signal power is above the
  average power.
- **Prob** –– Probability in percentage. This is the
  probability that the instantaneous signal power is above the average signal power
  by the value of the relative power in dB.
- Both the **RelPwr** and the **Prob**.

#### Dependencies

To enable this parameter, select the **Compute CCDF** check
box.

### **Specify probability (%) for relative power output** — Specify probability for relative power output [`10`;`1`;`0.1`;`0.01`;`0.001`;`0.0001`] (default) | column vector

Specify the probability (in percentage) for the relative power output as a column
vector. The length of this vector determines the number of rows in the relative power
output at the **RelPwr** port.

#### Dependencies

To enable this parameter, select the **Compute CCDF** check box
and set the **CCDF output** parameter to `Relative power
(dB above average power)`.

This also enables the **RelPwr** output port.

**Data Types:** `single` | `double`

### **Specify relative power (dB) for probability output** — Specify relative power for probability output [`0`;`3`;`6`;`9`;`12`] (default) | column vector

Specify the relative power (in dB) for the probability output as a column vector.
The length of this vector determines the number of rows in the probability output at the
**Prob** port.

#### Dependencies

To enable this parameter, select the **Compute CCDF** check box
and set the **CCDF output** parameter to `Probability
(%)`.

This also enables the **Prob** output port.

**Data Types:** `single` | `double`

### **Reset port** — Enable reset port off (default) | on

Select this parameter to enable the input port **Rst** that accepts
a boolean signal. If the value at the **Rst** port is
`true`, then the block clears the internal histograms and statistics
before processing the current input.

#### Dependencies

To enable this parameter, select the **Compute CCDF** check
box.

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

DSP System Toolbox / Statistics Communications Toolbox / Utility Blocks

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

**Introduced in R2021a**

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

### R2022b: New **Overlap length** parameter

Starting in R2022b, when the block is not computing the CCDF measurements, you can
specify the overlap length between sliding windows using the **Overlap
length** parameter.

### R2022b: Support for arbitrary input frame length

Power Meter block supports input signals with arbitrary frame lengths
when the:

- Input signal is a fixed-size signal (frame length does not change during
  simulation) and you select the **Allow arbitrary frame length for fixed-size
  input signals** parameter (if enabled).
- Input signal is a variable-size signal (frame length changes during
  simulation).

When this block supports an arbitrary frame length input signal, the input frame length
does not have to be a multiple of the hop size.

## Description

Measure power and the CCDF of the power of voltage signal in Simulink

The Power Meter block computes the power measurements of a voltage signal.
When you select the **Compute CCDF** parameter, the block also calculates the
complementary cumulative distribution function (CCDF) of the power of a voltage signal. The
CCDF measurements that the block outputs are relative power and probability (in percentage).
The power measurements include average power, peak power, and peak-to-average power
ratio.

For more details on how the block computes the power measurements and the CCDF
measurements, see Algorithms.
