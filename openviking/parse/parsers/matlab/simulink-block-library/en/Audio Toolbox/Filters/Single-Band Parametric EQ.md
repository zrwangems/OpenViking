---
type: simulink-block
title: 'Single-Band Parametric EQ'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Filters'
documentation_page: 'singlebandparametriceq'
documentation_source_path: 'ref/singlebandparametriceq.html'
language: en
---

# Single-Band Parametric EQ

## Ports

### Input

### **x** — Input signal matrix | 1-D vector

- Matrix input –– Each column of the input is treated as an
  independent channel.
- 1-D vector input –– The input is treated as a signal
  channel.

This port is unnamed unless you specify additional input ports.

**Data Types:** `single` | `double`

### **Fc** — Center frequency (Hz) scalar

Specify the center frequency as a positive scalar that is less than
half the sample rate of the input signal.

#### Dependencies

To enable this port, select **Specify from input
port** for the **Center Frequency
(Hz)** parameter.

**Data Types:** `single` | `double`

### **BW** — Bandwidth (Hz) scalar

Specify the filter bandwidth as a positive scalar that is less than or
equal to half the sample rate of the input signal and 20 kHz.

#### Dependencies

To enable this port, select `Bandwidth and Center
Frequency` for the **Filter
specification** and **Specify from input
port** for the **Filter Bandwidth
(Hz)** parameter.

**Data Types:** `single` | `double`

### **GdB** — Peak or dip gain (dB) scalar

Specify the peak or dip gain in dB as a scalar.

#### Dependencies

To enable this port, select **Specify from input
port** for the **Peak Gain (dB)**
parameter.

**Data Types:** `single` | `double`

### **Q** — Quality factor scalar

Specify the quality factor as a positive scalar.

#### Dependencies

To enable this port, select `Quality factor and center
frequency` for the **Filter
Specification** and **Specify from input
port** for the **Quality Factor**
parameter.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Output signal matrix

The Single-Band Parametric EQ block outputs a signal with the same data type as
the input signal. The size of the output depends on the size of the input:

- Matrix input –– The block outputs a matrix the same size
  and data type as the input signal.
- 1-D vector input –– The block outputs an
  *N*-by-1 matrix (column vector), where
  *N* is the number of elements in the
  1-D vector.

**Data Types:** `single` | `double`

## Parameters

If a parameter is listed as tunable, then you can change its value during
simulation.

### **Filter order** — Order of filter `2` (default) | positive even scalar

**Tunable:** No

### **Filter specification** — Specify parameters used to design filter `Bandwidth and center frequency` (default) | `Quality factor and center frequency`

- `Bandwidth and center frequency` ––
  Design the filter using **Filter Bandwidth (Hz)**,
  **Center Frequency (Hz)**, and **Peak
  Gain (dB)**.
- `Quality factor and center frequency` ––
  Design the filter using **Center Frequency (Hz)**,
  **Peak Gain (dB)**, and **Quality
  Factor**.

**Tunable:** No

### **Center Frequency (Hz)** — Center frequency of filter `11025` (default) | positive scalar

Specify the center frequency as a positive scalar that is less than half
the sample rate of the input signal.

To specify **Center Frequency (Hz)** from an input port,
select **Specify from input port** for the
parameter.

**Tunable:** Yes

### **Filter Bandwidth (Hz)** — Bandwidth of filter `2205` (default) | positive scalar in the range [0, max(fs/2, 20,000)]

Specify the filter bandwidth as a positive scalar that is less than or
equal to half the sample rate of the input signal or 20 kHz, whichever is
larger.

To specify **Filter Bandwidth (Hz)** from an input port,
select **Specify from input port** for the
parameter.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Filter
specification** to `Bandwidth and center
frequency`.

### **Quality Factor** — Quality factor `5` (default) | scalar in the range [0.1, 20]

Specify the quality factor as a scalar in the range [0.1, 20].

To specify **Quality Factor** from an input port, select
**Specify from input port** for the parameter.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Filter
specification** to `Quality factor and center
frequency`.

### **Peak Gain (dB)** — Peak or dip gain of filter `6.0206` (default) | scalar in the range [−30, 30]

Specify the peak gain in dB as a scalar in the range [−30, 30].

**Tunable:** Yes

### **Inherit sample rate from input** — Specify source of input sample rate on (default) | off

When you select this parameter, the block inherits its sample rate from
the input signal. When you clear this parameter, you specify the sample rate
in **Input sample rate (Hz)**.

**Tunable:** No

### **Input sample rate (Hz)** — Sample rate of input `44100` (default) | scalar

**Tunable:** Yes

#### Dependencies

To enable this parameter, clear the **Inherit sample rate from
input** parameter.

### **Simulate using** — Specify type of simulation to run `Code generation` (default) | `Interpreted execution`

- `Interpreted execution` –– Simulate model
  using the MATLAB® interpreter. This option shortens startup time and has
  simulation speed comparable to `Code
  generation`. In this mode, you can debug the source
  code of the block.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused
  for subsequent simulations, as long as the model does not change.
  This option requires additional startup time, but the speed of the
  subsequent simulations is faster compared to
  `Interpreted execution`.

**Tunable:** No

## Libraries

Audio Toolbox / Filters

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

**Introduced in R2019a**

### R2022b: **Input sample rate (Hz)** parameter is tunable

You can change the value of the **Input sample rate (Hz)**
parameter during simulation.

## Description

Second-order parametric equalizer filter

The Single-Band Parametric EQ block filters each channel of the input signal
over time using a specified center frequency, bandwidth, and peak (dip) gain. This block
offers tunable filter design parameters, which enable you to tune the filter
characteristics while the simulation is running. The filter is designed using `designParamEQ` and implemented using `dsp.SOSFilter`.

This block supports variable-size input, enabling you to change
the channel length during simulation. To enable variable-size input,
clear the **Inherit sample rate from input** parameter.
The number of channels must remain constant.
