---
type: simulink-block
title: 'Loudness Meter'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Psychoacoustics'
documentation_page: 'loudnessmeter'
documentation_source_path: 'ref/loudnessmeter.html'
language: en
---

# Loudness Meter

## Ports

### Input

### **Port\_1** — Input signal matrix | 1-D vector

- Matrix input –– Each column of the input is treated as an independent channel. If you use the
  default **Channel weights**, specify the input
  channels in order: [Left, Right, Center, Left surround, Right
  surround].
- 1-D vector input –– The input is treated as a single channel.

**Data Types:** `single` | `double`
### Output

### **M** — Momentary loudness measurement column vector

The block outputs a column vector with the same data type and
number of rows as the input signal.

**Data Types:** `single` | `double`

### **S** — Short-term loudness measurement column vector

The block outputs a column vector with the same data type and
number of rows as the input signal.

**Data Types:** `single` | `double`

### **TP** — True-peak value real scalar

The block outputs a real scalar with the same data type as the
input signal.

#### Dependencies

To enable this port, select the **Output true-peak value** parameter.

**Data Types:** `single` | `double`

## Parameters

If a parameter is listed as tunable, then you can change its value during
simulation.

### **Channel weights** — Linear weighting applied to each input channel `[1, 1, 1, 1.41, 1.41]` (default) | nonnegative row vector

The number of elements of the row vector must be equal to or greater than
the number of input channels. Excess values in the vector are
ignored.

The default channel weights follow the ITU-R BS.1170-4 standard. To use
the default channel weights, specify the input to the Loudness
Meter block as a matrix whose columns correspond to channels in
this order: [Left, Right, Center, Left surround, Right surround].

It is a best practice to specify the channel weights in order: [Left,
Right, Center, Left surround, Right surround].

**Tunable:** Yes

### **Use relative scale for loudness measurements** — Specify block to output loudness measurements relative to target level off (default) | on

- On — The loudness measurements are relative to the value
  specified by **Target loudness level (LUFS)**. The
  output of the block is returned in loudness units (LU).
- Off — The loudness measurements are absolute, and returned
  in loudness units full scale (LUFS).

**Tunable:** No

### **Target loudness level (LUFS)** — Reference level for relative loudness measurements `–23` (default) | real scalar

For example, if the **Target loudness level (LUFS)** is
–23, then a loudness value of –24 LUFS is reported as –1 LU.

**Tunable:** Yes

#### Dependencies

To enable this parameter, select the **Use relative scale for
loudness measurements** parameter.

### **Output true-peak value** — Add output port for true-peak value off (default) | on

When you select this parameter, an additional output port,
**TP**, is added to the block. The
**TP** port outputs the true-peak value of the input
frame.

**Tunable:** No

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

- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused
  for subsequent simulations, as long as the model does not change.
  This option requires additional startup time but the speed of the
  subsequent simulations is comparable to `Interpreted
  execution`.
- `Interpreted execution` –– Simulate model
  using the MATLAB® interpreter. This option shortens startup time but has
  a slower simulation speed than `Code
  generation`. In this mode, you can debug the source
  code of the block.

**Tunable:** No

## Libraries

Audio Toolbox / Measurements

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

**Introduced in R2016b**

## Description

Standard-compliant loudness measurements

The Loudness Meter block measures the loudness
and true-peak of an audio signal based on EBU R 128 and ITU-R BS.1770-4
standards.
