---
type: simulink-block
title: 'Voice Activity Detector'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'AI for Audio / Segmentation'
documentation_page: 'voiceactivitydetector'
documentation_source_path: 'ref/voiceactivitydetector.html'
language: en
---

# Voice Activity Detector

## Ports

### Input

### **x** — Input signal matrix | 1-D vector

- Matrix input –– Each column of the input is treated as an
  independent channel.
- 1-D vector input –– The input is treated as a single
  channel.

This port is unnamed unless you specify additional input ports.

**Data Types:** `single` | `double`

### **SilenceToSpeech** — Threshold (dB) scalar in the range [0, 1]

#### Dependencies

To enable this port, select **Specify silence-to-speech
probability from input port** for the Probability of transition from a silence frame to a speech frame
parameter.

**Data Types:** `single` | `double`

### **SpeechToSilence** — Threshold (dB) scalar in the range [0, 1]

#### Dependencies

To enable this port, select **Specify speech-to-silence
probability from input port** for the Probability of transition from a speech frame to a silence frame
parameter.

**Data Types:** `single` | `double`
### Output

### **P** — Probability that speech is present scalar | row vector

The block outputs a scalar or row vector with the same number of
columns as the input signal.

This port is unnamed until you select the **Output noise
variance** parameter.

**Data Types:** `single` | `double`

### **N** — Estimate of noise variance per frequency bin column vector | matrix

The block outputs a column vector or a matrix with the same number of
columns as the input signal.

#### Dependencies

To enable this port, select the **Output noise
variance** parameter.

**Data Types:** `single` | `double`

## Parameters

If a parameter is listed as tunable, then you can change its value during
simulation.

### **Domain of the input** — Domain of the input `Time` (default) | `Frequency`

### **Window** — Windowing function applied before FFT `Hann` (default) | `Chebyshev` | `Flat Top` | `Hamming` | `Kaiser` | `Rectangular`

The window function is designed using the algorithms of the following functions:

- `Hann` –– `hann`
- `Chebyshev` –– `chebwin`
- `Flat Top` –– `flattopwin`
- `Hamming` –– `hamming`
- `Kaiser` –– `kaiser`

**Tunable:** No

#### Dependencies

To enable this parameter, set **Domain of the input**
to `Time`.

### **Sidelobe attenuation of the window (dB)** — Sidelobe attenuation of the window (dB) `60` (default) | positive finite scalar

#### Dependencies

To enable this parameter, set **Domain of the input**
to `Time` and **Window** to
`Chebyshev` or
`Kaiser`.

**Data Types:** `single` | `double`

### **Inherit FFT length from input dimensions** — Set FFT length to number of input samples on (default) | off

**Tunable:** No

#### Dependencies

To enable this parameter, set **Domain of the input**
to `Time`.

### **FFT length** — Number of bins in frequency domain `1024` (default) | positive integer

**Tunable:** No

#### Dependencies

To enable this parameter, set **Domain of the input**
to `Time` and clear the **Inherit FFT
length from input dimensions** parameter.

**Data Types:** `single` | `double`

### **Probability of transition from a silence frame to a speech frame** — Probability that a speech frame follows a silence frame `0.2` (default) | scalar in the range [0,1]

To specify **Probability of transition from a silence frame to a
speech frame** from an input port, select **Specify
silence-to-speech probability from input port**.

**Tunable:** Yes

**Data Types:** `single` | `double`

### **Probability of transition from a speech frame to a silence frame** — Probability that a silence frame follows a speech frame `0.1` (default) | scalar in the range [0,1]

To specify **Probability of transition from a speech frame to a
silence frame** from an input port, select **Specify
speech-to-silence probability from input port**.

**Tunable:** Yes

**Data Types:** `single` | `double`

### **Output noise variance** — Output estimate of noise variance per frequency bin `off` (default) | `on`

When you select this parameter, an additional output port,
**N**, is added to the block.

### **Simulate using** — Specify type of simulation to run `Code generation` (default) | `Interpreted execution`

- `Code generation` – Simulate the model
  using generated C code. The first time you run a simulation,
  Simulink® generates C code for the block. The C code is reused
  for subsequent simulations, as long as the model does not change.
  This option requires additional startup time, but the speed of the
  subsequent simulations is comparable to `Interpreted
  execution`.
- `Interpreted execution` – Simulate the
  model using the MATLAB® interpreter. This option reduces startup time, but has
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
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Detect presence of speech in audio signal

The Voice Activity Detector block detects the presence of speech in an
audio signal. You can also use the Voice Activity Detector block to
output an estimate of the noise variance per frequency bin.
