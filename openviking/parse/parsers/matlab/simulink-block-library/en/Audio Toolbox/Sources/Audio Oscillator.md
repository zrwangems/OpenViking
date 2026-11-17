---
type: simulink-block
title: 'Audio Oscillator'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'audiooscillator'
documentation_source_path: 'ref/audiooscillator.html'
language: en
---

# Audio Oscillator

## Ports
```yaml
ports:
- name: F
  summary: Frequency (Hz) nonnegative scalar | vector of nonnegative values
  direction: input
  data_types: single | double
- name: A
  summary: Amplitude nonnegative scalar | vector of nonnegative values
  direction: input
  data_types: single | double
- name: DC
  summary: DC offset scalar | vector
  direction: input
  data_types: single | double
- name: Port_1
  summary: Output signal vector
  direction: output
  data_types: single | double
```

### Input

### **F** — Frequency (Hz) nonnegative scalar | vector of nonnegative values

#### Dependencies

To enable this port, select **Specify frequency from input
port** for the Frequency (Hz) parameter.

**Data Types:** `single` | `double`

### **A** — Amplitude nonnegative scalar | vector of nonnegative values

#### Dependencies

To enable this port, select **Specify amplitude from input
port** for the Amplitude parameter.

**Data Types:** `single` | `double`

### **DC** — DC offset scalar | vector

#### Dependencies

To enable this port, select **Specify DC offset from input
port** for the DC offset parameter.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Output signal vector

The Audio Oscillator block outputs a periodic signal defined by the
parameters of the block.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Signal type
  summary: Type of generated waveform sine (default) | square | sawtooth
  group: ''
- name: Frequency (Hz)
  summary: Frequency of generated waveform 100 (default) | nonnegative scalar | vector of nonnegative values
  group: ''
- name: Amplitude
  summary: Amplitude of generated waveform 1 (default) | nonnegative scalar | vector of nonnegative values
  group: ''
- name: Phase offset
  summary: Normalized phase offset of generated waveform 0 (default) | scalar in the range [0, 1] | vector with values in
    the range [0, 1]
  group: ''
- name: DC offset
  summary: Value added to each element of generated waveform 0 (default) | scalar | vector
  group: ''
- name: Duty cycle
  summary: Square waveform duty cycle 0.5 (default) | scalar in the range [0, 1]
  group: ''
- name: Width
  summary: Sawtooth width 1 (default) | scalar in the range [0, 1]
  group: ''
- name: Samples per frame
  summary: Number of samples per frame 512 (default) | positive integer
  group: ''
- name: Sample rate (Hz)
  summary: Sample rate of generated waveform 44100 (default) | positive scalar
  group: ''
- name: Output data type
  summary: Data type of generated waveform double (default) | single
  group: ''
- name: Simulate using
  summary: Specify type of simulation to run Code generation (default) | Interpreted execution
  group: ''
```

If a parameter is listed as tunable, then you can change its value during
simulation.

### **Signal type** — Type of generated waveform `sine` (default) | `square` | `sawtooth`

The waveforms are generated using the algorithms specified by the `sin`, `square`, and
`sawtooth`
functions.

### **Frequency (Hz)** — Frequency of generated waveform `100` (default) | nonnegative scalar | vector of nonnegative values

- If Signal type is set to
  `sine`, specify **Frequency (Hz)** as a
  scalar or as a vector. If **Frequency (Hz)** is set to an
  *N*-element vector, then the output from the block is the
  single-channel sum of *N* sinusoids. If **Frequency
  (Hz)** is set to an *N*-element vector, then Amplitude, Phase offset, and DC offset must be scalars
  or *N*-element vectors.
- For square waveforms, specify **Frequency (Hz)** as a
  scalar.
- For sawtooth waveforms, specify **Frequency (Hz)** as a
  scalar.

To specify **Frequency (Hz)** from an input port, select
**Specify frequency from input port**.

**Tunable:** Yes

### **Amplitude** — Amplitude of generated waveform `1` (default) | nonnegative scalar | vector of nonnegative values

- If Signal type is set to
  `sine`, specify **Amplitude** as a
  scalar or as a vector. If **Amplitude** is set to an
  *N*-element vector, then the output from the block is the
  single-channel sum of *N* sinusoids. If
  **Amplitude** is set to an *N*-element vector,
  then Frequency (Hz), Phase offset, and DC offset must be scalars
  or *N*-element vectors.
- For square waveforms, specify **Amplitude** as a scalar.
- For sawtooth waveforms, specify **Amplitude** as a
  scalar.

To specify **Amplitude** from an input port, select
**Specify amplitude from input port**.

**Tunable:** Yes

### **Phase offset** — Normalized phase offset of generated waveform `0` (default) | scalar in the range [0, 1] | vector with values in the range [0, 1]

The phase offset range, `[0,1]`, corresponds to a normalized 2π
radians interval.

- If Signal type is set to
  `sine`, specify **Phase offset** as a
  scalar or as a vector. If **Phase offset** is set to an
  *N*-element vector, then the output from the block is the
  single-channel sum of *N* sinusoids. If **Phase
  offset** is set to an *N*-element vector, then Frequency (Hz), Amplitude, and DC offset must be scalars
  or *N*-element vectors.
- For square waveforms, specify **Amplitude** as a scalar.
- For sawtooth waveforms, specify **Amplitude** as a
  scalar.

### **DC offset** — Value added to each element of generated waveform `0` (default) | scalar | vector

- If Signal type is set to
  `sine`, specify **DC offset** as a
  scalar or as a vector. If **DC offset** is set to an
  *N*-element vector, then the output from the block is the
  single-channel sum of *N* sinusoids. If **DC
  offset** is set to an *N*-element vector, then Frequency (Hz), Amplitude, and Phase offset must be scalars
  or *N*-element vectors.
- For square waveforms, specify **Amplitude** as a scalar.
- For sawtooth waveforms, specify **Amplitude** as a
  scalar.

To specify **DC offset** from an input port, select
**Specify DC offset from input port**.

**Tunable:** Yes

### **Duty cycle** — Square waveform duty cycle `0.5` (default) | scalar in the range [0, 1]

*Square waveform duty cycle* is the percentage of one period in
which the waveform is above the median amplitude. A duty cycle value of 1 or 0 is
equivalent to a DC signal.

#### Dependencies

To enable this parameter, set **Signal type** to
`square`.

### **Width** — Sawtooth width `1` (default) | scalar in the range [0, 1]

*Sawtooth width* determines the point in a sawtooth waveform
period at which the maximum occurs.

#### Dependencies

To enable this property, set **Signal type** to
`sawtooth`.

### **Samples per frame** — Number of samples per frame `512` (default) | positive integer

Number of samples per frame, specified as a positive integer.

### **Sample rate (Hz)** — Sample rate of generated waveform `44100` (default) | positive scalar

The sample rate must be greater than twice the value specified in Frequency (Hz).

### **Output data type** — Data type of generated waveform `double` (default) | `single`

Data type of generated waveform, specified as `double` or
`single`.

**Tunable:** No

### **Simulate using** — Specify type of simulation to run `Code generation` (default) | `Interpreted execution`

- `Code generation` – Simulate the model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for subsequent
  simulations, as long as the model does not change. This option requires additional
  startup time, but the speed of the subsequent simulations is comparable to
  `Interpreted execution`.
- `Interpreted execution` – Simulate model using the
  MATLAB® interpreter. This option reduces startup time and the simulation has
  speed comparable to `Code generation`. In this mode, you
  can debug the source code of the block.
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

Generate sine, square, and sawtooth waveforms

The Audio Oscillator block generates tunable waveforms. Typical uses
include the generation of test signals for test benches, and the generation of control signals
for audio effects. Parameters of the Audio Oscillator block specify the type of
waveform generated.

The Audio Oscillator block enables you to tune the phase offset, DC offset, frequency, and amplitude of your waveforms.
