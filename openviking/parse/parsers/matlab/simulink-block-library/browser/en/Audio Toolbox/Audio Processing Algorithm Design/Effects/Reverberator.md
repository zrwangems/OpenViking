---
type: simulink-block
title: 'Reverberator'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Audio Processing Algorithm Design / Effects'
documentation_page: 'reverberator'
documentation_source_path: 'ref/reverberator.html'
language: en
---

# Reverberator

## Ports

### Input

### **x** — Input signal matrix | 1-D vector

- Matrix input –– Each column of the input is treated as an
  independent channel.
- 1-D vector input –– The input is treated as a single
  channel.

This port is unnamed unless you specify additional input ports.

**Data Types:** `single` | `double`

### **Delay** — Pre-delay for reverberation (s) scalar in the range [0,1]

#### Dependencies

To enable this port, select **Specify from input
port** for the Pre-delay (s) parameter.

**Data Types:** `single` | `double`

### **HighCut** — Lowpass filter cutoff positive scalar in the range [0, (Sample Rate)/2]

#### Dependencies

To enable this port, select **Specify from input
port** for the Highcut frequency (Hz)
parameter.

**Data Types:** `single` | `double`

### **Diffusion** — Density of reverb tail scalar in the range [0,1]

#### Dependencies

To enable this port, select **Specify from input
port** for the Diffusion parameter.

**Data Types:** `single` | `double`

### **Decay** — Decay factor of reverb tail scalar in the range [0,1]

#### Dependencies

To enable this port, select **Specify from input
port** for the Decay factor parameter.

**Data Types:** `single` | `double`

### **Damping** — High-frequency damping scalar in the range [0,1]

#### Dependencies

To enable this port, select **Specify from input
port** for the High frequency damping
parameter.

**Data Types:** `single` | `double`

### **WetDry** — Ratio of wet (reverberated) signal to dry (original) signal scalar in the range [0,1]

#### Dependencies

To enable this port, select **Specify from input
port** for the Wet/dry mix parameter.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Output signal matrix

The Reverberator block outputs the reverberated signal as a two-column
matrix.

**Data Types:** `single` | `double`

## Parameters

If a parameter is listed as tunable, then you can change its value during
simulation.

### **Pre-delay (s)** — Pre-delay for reverberation `0` (default) | scalar in the range [0, 1]

*Pre-delay for reverberation* is the time between
hearing direct sound and the first early reflection. The value of
**Pre-delay (s)** is proportional to the size of the
room being modeled.

To specify **Pre-delay (s)** from an input port, select
**Specify from input port** for the parameter.

**Tunable:** Yes

### **Highcut frequency (Hz)** — Lowpass filter cutoff `20000` (default) | scalar in the range [0, (Sample Rate)/2]

*Lowpass filter cutoff*  is the –3 dB cutoff
frequency for the single-pole lowpass filter at the front of the
reverberator structure. It prevents the application of reverberation to
high-frequency components of the input.

To specify **Highcut frequency (Hz)** from an input port,
select **Specify from input port** for the
parameter.

**Tunable:** Yes

### **Diffusion** — Density of reverb tail `0.50` (default) | scalar in the range [0, 1]

**Diffusion** is proportional to the rate at which the
reverb tail builds in density. Increasing **Diffusion**
pushes the reflections closer together, thickening the sound. Reducing
**Diffusion** creates more discrete echoes.

To specify **Diffusion** from an input port, select
**Specify from input port** for the parameter.

**Tunable:** Yes

### **Decay factor** — Decay factor of reverb tail `0.50` (default) | scalar in the range [0, 1]

**Decay factor** is inversely proportional to the time it
takes for reflections to run out of energy. To model a large room, use a
long reverb tail (low decay factor). To model a small room, use a short
reverb tail (high decay factor).

To specify **Decay factor** from an input port, select
**Specify from input port** for the parameter.

**Tunable:** Yes

### **High frequency damping** — High-frequency damping `0.0005` (default) | scalar in the range [0, 1]

**High frequency damping** is proportional to the
attenuation of high frequencies in the reverberation output. Setting
**High frequency damping** to a large value makes
high-frequency reflections decay faster than low-frequency
reflections.

To specify **High frequency damping** from an input port,
select **Specify from input port** for the
parameter.

**Tunable:** Yes

### **Wet/dry mix** — Ratio of wet (reverberated) signal to dry (original) signal `0.3` (default) | scalar in the range [0, 1]

*Wet/dry mix* is the ratio of wet (reverberated)
signal to dry (original) signal that your Reverberator block
outputs.

To specify **Wet/dry mix** from an input port, select
**Specify from input port** for the parameter.

**Tunable:** Yes

### **Inherit sample rate from input** — Specify source of input sample rate on (default) | off

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
  model using the MATLAB® interpreter. This option reduces startup time and the
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

## Libraries

Audio Toolbox / Effects

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

Add reverberation to audio signal

The Reverberator block adds reverberation to
mono or stereo audio signals. You can tune parameters of the Reverberator block
to mimic different acoustic environments.
