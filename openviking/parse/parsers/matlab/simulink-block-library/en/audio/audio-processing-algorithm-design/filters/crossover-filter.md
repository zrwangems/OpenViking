---
type: simulink-block
title: 'Crossover Filter'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Audio Processing Algorithm Design / Filters'
documentation_page: 'crossoverfilter'
documentation_source_path: 'ref/crossoverfilter.html'
language: en
---

# Crossover Filter

## Ports

### Input

### **x** — Input signal matrix | 1-D vector

- Matrix input –– Each column of the input is treated as an
  independent channel.
- 1-D vector input –– The input is treated as a single
  channel.

This port is unnamed unless you specify additional input ports.

**Data Types:** `single` | `double`

### **F1** — Crossover frequency (Hz) real scalar in the range `20` to `20000`

#### Dependencies

To enable this port, select **Specify from input
port** for the Crossover frequency (Hz)
parameter.

**Data Types:** `single` | `double`

### **O1** — Crossover order integer in the range `0` to `8`

#### Dependencies

To enable this port, select **Specify from input
port** for the Crossover order
parameter.

**Data Types:** `single` | `double`

### **F2** — Crossover frequency (Hz) real scalar in the range `20` to `20000`

#### Dependencies

To enable this port, you need to both:

- Select **Specify from input port**
  for the Crossover frequency (Hz) parameter.
- Set Number of crossovers to `2`,
  `3` or
  `4`.

**Data Types:** `single` | `double`

### **O2** — Crossover order integer in the range `0` to `8`

#### Dependencies

To enable this port, you need to both:

- Select **Specify from input port**
  for the Crossover order
  parameter.
- Set Number of crossovers to `2`,
  `3` or
  `4`.

**Data Types:** `single` | `double`

### **F3** — Crossover frequency (Hz) real scalar in the range `20` to `20000`

#### Dependencies

To enable this port, you need to both:

- Select **Specify from input port**
  for the Crossover frequency (Hz) parameter.
- Set Number of crossovers to `3` or
  `4`.

**Data Types:** `single` | `double`

### **O3** — Crossover order integer in the range `0` to `8`

#### Dependencies

To enable this port, you need to both:

- Select **Specify from input port**
  for the Crossover order
  parameter.
- Set Number of crossovers to `3` or
  `4`.

**Data Types:** `single` | `double`

### **F4** — Crossover frequency (Hz) real scalar in the range `20` to `20000`

#### Dependencies

To enable this port, you need to both:

- Select **Specify from input port**
  for the Crossover frequency (Hz) parameter.
- Set Number of crossovers to `4`.

**Data Types:** `single` | `double`

### **O4** — Crossover order integer in the range `0` to `8`

#### Dependencies

To enable this port, you need to both:

- Select **Specify from input port**
  for the Crossover order
  parameter.
- Set Number of crossovers to `4`.

**Data Types:** `single` | `double`
### Output

### **Y1** — Output signal matrix

Port **Y1** always corresponds to a lowpass
filter.

#### Dependencies

Available if **Number of crossovers** is set to
`1`, `2`,
`3`, or
`4`.

**Data Types:** `single` | `double`

### **Y2** — Output signal matrix

Depending on the number of crossovers specified, port **Y2** outputs
the original audio signal passed through a bandpass or highpass filter.

#### Dependencies

Available if **Number of crossovers** is set to
`1`, `2`,
`3`, or
`4`.

**Data Types:** `single` | `double`

### **Y3** — Output signal matrix

Depending on the number of crossovers specified, port **Y3** corresponds
to a bandpass or highpass filter of the original audio signal.

#### Dependencies

Available if **Number of crossovers** is set to
`2`, `3`, or
`4`.

**Data Types:** `single` | `double`

### **Y4** — Output signal matrix

#### Dependencies

Available if **Number of crossovers** is set to
`3` or
`4`.

**Data Types:** `single` | `double`

### **Y5** — Output signal matrix

#### Dependencies

Available if **Number of crossovers** is set to
`4`.

**Data Types:** `single` | `double`

## Parameters

If a parameter is listed as tunable, then you can change its value during
simulation.

### **Number of crossovers** — Number of magnitude response band crossings `1` (default) | `2` | `3` | `4`

If you specify multiple crossovers, the corresponding **Crossover
frequency (Hz)** and **Crossover order**
parameters populate in the dialog box automatically.

The number of bands output by the Crossover Filter block is
one more than the **Number of crossovers**.

| **Number of Crossovers** | Number of Bands in Output |
| --- | --- |
| `1` | Two |
| `2` | Three |
| `3` | Four |
| `4` | Five |

### **Crossover frequency (Hz)** — Intersections of magnitude response bands `100` (default) | real scalar in the range `20` to `20000`

Crossover frequencies are the intersections of magnitude response bands of
the individual two-band crossover filters used in the multiband crossover
filter.

**Tunable:** Yes

### **Crossover order** — Order of individual crossover filters `2` (default) | integer in the range [0, 8]

The crossover filter order relates to the crossover filter slope in
dB/octave: slope=N×6, where *N* is the crossover order.

**Tunable:** Yes

### **View filter response** — Open plot of magnitude response of each filter band button

The plot is updated automatically when parameters of the Crossover
Filter block change.

**Tunable:** Yes

### **Variable name** — Variable name of exported filter `myFilt` (default) | valid variable name

Name of the variable in the base workspace to contain the filter when it
is exported. The name must be a valid MATLAB® variable name.

### **Overwrite variable if it already exists** — Overwrite variable if it already exists `on` (default) | `off`

When you select this parameter, exporting the filter overwrites the
variable specified by the **Variable name** parameter if it
already exists in the base workspace. If you do not select this parameter
and the specified variable already exists in the workspace, exporting the
filter creates a new variable with an underscore and a number appended to
the variable name. For example, if the variable name is
`var` and it already exists, the exported variable will
be named `var_1`.

### **Export filter to workspace** — Export filter to workspace button

Export the filter to the base workspace in the variable specified by the
**Variable name** parameter.

#### Tips

- You cannot export the filter if you have enabled the
  **Inherit sample rate from input**
  parameter and the model is not running.
- You cannot export the filter if you are specifying filter
  characteristics from input ports.

### **Inherit sample rate from input** — Specify source of input sample rate off (default) | on

When you select this parameter, the block inherits its sample rate from
the input signal. When you clear this parameter, you specify the sample rate
in **Input sample rate (Hz)**.

### **Input sample rate (Hz)** — Sample rate of input `44100` (default) | positive scalar

**Tunable:** Yes

#### Dependencies

To enable this parameter, clear the **Inherit sample rate from
input** parameter.

### **Simulate using** — Specify type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` – Simulate the
  model using the MATLAB interpreter. This option reduces startup time and the
  simulation speed is comparable to `Code
  generation`. In this mode, you can debug the source
  code of the block.
- `Code generation` – Simulate the model
  using generated C code. The first time you run a simulation,
  Simulink® generates C code for the block. The C code is reused
  for subsequent simulations, as long as the model does not change.
  This option requires additional startup time, but the speed of the
  subsequent simulations is comparable to `Interpreted
  execution`.

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

**Introduced in R2016a**

## Description

Audio crossover filter

The Crossover Filter block implements an audio
crossover filter, which is used to split an audio signal into two
or more frequency bands. Crossover filters are multiband filters whose
overall magnitude frequency response is flat.
