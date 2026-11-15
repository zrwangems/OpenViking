---
type: simulink-block
title: 'PLL with Feed Forward'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Signal Management'
documentation_page: 'pllwithfeedforward'
documentation_source_path: 'ref/pllwithfeedforward.html'
language: en
---

# PLL with Feed Forward

## Ports

### Input

### **α** — *α*-axis signal scalar

Input signal along the *α*-axis.

**Data Types:** `single` | `double` | `fixed point`

### **β** — *β*-axis signal scalar

Input signal along the *β*-axis.

**Data Types:** `single` | `double` | `fixed point`

### **Rst** — External reset pulse scalar

External pulse that resets the block.

**Data Types:** `single` | `double` | `fixed point`

### **ParameterBus** — Computed parameters for PLL with Feed Forward bus

Computed parameters for the PLL with Feed Forward block. The
input port accepts the following parameters:

- **Maximum application frequency (Hz)**
- **Cutoff frequency for output filter (Hz)**
- **Number of data points for lookup table**
- **Proportional (P)**
- **Integral (I)**

Use this port along with the Compute
Parameter block to update the preceding block parameters optimally
at run-time.

#### Dependencies

To enable this port, select the **Use input port for computed
parameters (run-time motor swap)** parameter available in the
**Advanced Options** section.

**Data Types:** `single` | `double`
### Output

### **θ** — Angular position scalar

Angular position (in either degrees, radians, or per-unit) that the block
computes from the orthogonal input signals.

#### Dependencies

To enable this port, set the **Position output**
parameter to `Angular position`.

**Data Types:** `single` | `double` | `fixed point`

### **Sin θ** — Sine of angular position scalar

Sine equivalent of the computed angular position.

#### Dependencies

To enable this port, set the **Position output**
parameter to `Sine and Cosine Position`.

**Data Types:** `single` | `double` | `fixed point`

### **Cos θ** — Cos of angular position scalar

Cosine equivalent of the computed angular position.

#### Dependencies

To enable this port, set the **Position output**
parameter to `Sine and Cosine Position`.

**Data Types:** `single` | `double` | `fixed point`

### **ω** — Angular frequency scalar

Angular frequency (in either degrees/sec, radians/sec, or hertz) of the
orthogonal input signals.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Enable input normalization** — Enable block to normalize inputs `on` (default) | `off`

The block normalizes the **α** and **β**
orthogonal input signals only if you select this parameter.

### **Use input port for computed parameters (run-time motor swap)** — Option to enable input port to accept computed parameters `off` (default) | on

Select this parameter to enable the **ParameterBus** input
port and disable the following parameters:

- **Maximum application frequency (Hz)**
- **Cutoff frequency for output filter (Hz)**
- **Number of data points for lookup table**
- **Proportional (P)**
- **Integral (I)**

This parameter enables you to use the input port along with the Compute
Parameter block to update block parameters optimally at
run-time.

### **Position output** — Type of position output `Angular position` (default) | `Sine and Cosine Position`

Type of position output that the block should generate:

- `Angular position` — Select this option to use a
  sine-cosine lookup table to compute the angular position
  (**θ**).
- `Sine and Cosine Position` — Select this option
  to use an oscillator based algorithm to compute the sine and cosine
  equivalents (**sin θ** and **cos θ**) of
  the angular position.

### **Discrete step size (s)** — Sample time after which block executes again `50e-6` (default) | scalar

The fixed time interval (in seconds) between consecutive instances of block
execution.

### PLL Parameters

### **Frequency ratio** — Ratio of frequencies of output and input signals `1` (default) | scalar

The ratio of the frequency of the output signal to the frequency of the
input signal of the block.

### **Maximum application frequency (Hz)** — Maximum applicable input frequency `7500` (default) | scalar

Maximum possible frequency of the input signals (in hertz).

### **Cutoff frequency for output filter (Hz)** — Cutoff frequency of lowpass filter `15` (default) | scalar

Cutoff frequency of the lowpass filter that the block uses to filter the
estimated angular frequency (in hertz).

### **Number of data points for lookup table** — Size of lookup table array `1024` (default) | scalar

Size of the lookup table array that the block provides to the SinCos Embedded Optimized block, which
is used internally. This parameter accepts a value between 125 and 4095.

#### Dependencies

To enable this parameter, set **Position output** to
`Angular position`.

### **Proportional (P)** — Proportional controller gain `942.4778` (default) | scalar

Proportional gain (*Kp*) of the PID
controller used by the block to compute the angular frequency.

### **Integral (I)** — Integral controller gain `222066.099` (default) | scalar

Integral gain (*Ki*) of the PID
controller used by the block to compute the angular frequency.

Click **Compute default parameters** to calculate an approximate
proportional gain (*Kp*) and integral gain
(*Ki*) and update these fields.

### Datatypes

### **Position unit** — Unit of position output `Degrees` (default) | `Radians` | `Per-unit`

Unit of the position output.

#### Dependencies

To enable this parameter, set **Position output** to
`Angular position`.

### **Position data type** — Data type of position output `single` (default) | `double` | `fixed point`

Data type of the position output.

### **Frequency unit** — Unit of angular frequency output `Degrees/sec` (default) | `Radians/sec` | `Hz`

Unit of the angular frequency output.

### **Frequency data type** — Data type of angular frequency output `single` (default) | `double` | `fixed point`

Data type of the angular frequency output.

### **Table data type** — Data type of sine-cosine lookup table `single` (default) | `double` | `fixed point`

Data type of the sine-cosine lookup table used by the block.

#### Dependencies

To enable this parameter, set **Position output** to
`Angular position`.

## Libraries

Motor Control Blockset / Signal Management

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

**Restrictions**

The block does not support 16-bit fixed-point inputs.

## Version History

**Introduced in R2023b**

## Description

Compute position and angular frequency from orthogonal sinusoidal signals

The PLL with Feed Forward block computes angular position (θ) or its sine
and cosine equivalents (sin θ, cos θ) and the angular frequency (ω) from two orthogonal
sinusoidal signals.

In addition to the angular frequency, the block uses either a sine-cosine lookup table
to calculate the angular position or an oscillator based algorithm to compute the sine and
cosine equivalents of position. You can use the **Position output**
parameter to output either angular position or its sine and cosine equivalents.

The two orthogonal sinusoidal input signals must have identical peak magnitudes. If the
inputs are not normalized in the range of [-1,1], select the **Enable input
normalization** parameter.

The following image shows the relationship between block inputs and outputs:

For more information on the block algorithm, see Algorithm.

**Note**

The block does not support 16-bit fixed-point inputs.

In addition, you can use the advanced options to enable the
**ParameterBus** input port, which you can use with the Compute Parameter
block to update the block parameters optimally at run-time. You can use this functionality
when motor parameters can change over time, for example, while building applications that
may require swapping of motors at run-time.
