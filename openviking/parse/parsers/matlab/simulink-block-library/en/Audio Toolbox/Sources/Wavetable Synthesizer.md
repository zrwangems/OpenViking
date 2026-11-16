---
type: simulink-block
title: 'Wavetable Synthesizer'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'wavetablesynthesizer'
documentation_source_path: 'ref/wavetablesynthesizer.html'
language: en
---

# Wavetable Synthesizer

## Ports

### Input

### **WT** — Single-cycle waveform vector of real values

#### Dependencies

To enable this port, select **Specify wavetable from input
port** for the Single-cycle waveform parameter.

**Data Types:** `single` | `double`

### **F** — Output wave frequency (Hz) nonnegative scalar | vector of nonnegative values

#### Dependencies

To enable this port, select **Specify frequency from input
port** for the Output wave frequency (Hz) parameter.

**Data Types:** `single` | `double`

### **A** — Output wave amplitude nonnegative scalar

#### Dependencies

To enable this port, select **Specify amplitude from input
port** for the Output wave amplitude parameter.

**Data Types:** `single` | `double`

### **DC** — Output wave DC offset scalar

#### Dependencies

To enable this port, select **Specify DC offset from input
port** for the Output wave DC offset parameter.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Output signal vector | matrix

The Wavetable Synthesizer block outputs a periodic signal defined
by the parameters of the block.

**Data Types:** `single` | `double`

## Parameters

If a parameter is listed as tunable, then you can change its value during
simulation.

### **Single-cycle waveform** — Wavetable `sin(2*pi*(0:511)/512)` (default) | vector of real values

The Wavetable Synthesizer block indexes into the single-cycle
waveform to synthesize a periodic wave.

To specify **Single-cycle waveform** from an input port, select
**Specify wavetable from input port** for the parameter.

**Tunable:** Yes

### **Output wave frequency (Hz)** — Frequency of generated signal `100` (default) | nonnegative scalar

The number of times the single-cycle waveform is repeated in one second.

To specify **Output wave frequency (Hz)** from an input port,
select **Specify frequency from input port** for the parameter.

**Tunable:** Yes

### **Output wave amplitude** — Amplitude of generated signal `1` (default) | nonnegative scalar

Amplitude scaling is applied before DC offset.

To specify **Output wave amplitude** from an input port, select
**Specify amplitude from input port** for the parameter.

**Tunable:** Yes

### **Output wave phase offset** — Normalized phase offset of generated signal `0` (default) | scalar in the range `[0,1]`

The phase offset range, `[0,1]`, corresponds to a normalized 2π
radians interval.

### **Output wave DC offset** — Value added to each element of generated signal `0` (default) | scalar

To specify **Output wave DC offset** from an input port, select
**Specify DC offset from input port** for the parameter.

**Tunable:** Yes

### **Samples per frame** — Number of samples per frame output from block `512` (default) | positive integer scalar

Number of samples per frame output from block, specified as a positive integer
scalar.

**Tunable:** No

### **Sample rate (Hz)** — Sample rate of generated signal `44100` (default) | positive scalar

Sample rate of generated signal, specified as a positive scalar.

**Tunable:** No

### **Output data type** — Data type of generated signal `double` (default) | `single`

Data type of generated signal, specified as `double` or
`single`.

**Tunable:** No

### **Simulate using** — Specify type of simulation to run `Code generation` (default) | `Interpreted execution`

- `Code generation` – Simulate the model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for subsequent
  simulations, as long as the model does not change. This option requires additional
  startup time, but the speed of the subsequent simulations is comparable to
  `Interpreted execution`.
- `Interpreted execution` – Simulate the model using
  the MATLAB® interpreter. This option reduces startup time and the simulation
  speed is comparable to `Code generation`. In this mode,
  you can debug the source code of the block.

## Libraries

Audio Toolbox / Sources

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

**Introduced in R2020a**

## Description

Generate periodic signal from single-cycle waveforms

The Wavetable Synthesizer block generates a periodic signal with tunable
parameters. The periodic signal is defined by a single-cycle waveform cached as the
**Single-cycle waveform** parameter of your Wavetable
Synthesizer block.

The Wavetable Synthesizer block enables you to output a repeated single-cycle waveform while tuning aspects of the single-cycle waveform, such as frequency, amplitude, and offset.
