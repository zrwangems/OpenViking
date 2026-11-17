---
type: simulink-block
title: 'FM Broadcast Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Analog Baseband Modulation'
documentation_page: 'fmbroadcastdemodulatorbaseband'
documentation_source_path: 'ref/fmbroadcastdemodulatorbaseband.html'
language: en
---

# FM Broadcast Demodulator Baseband

## Ports
```yaml
ports:
- name: In
  summary: FM-modulated baseband audio signal column vector
  direction: input
  data_types: double | single
- name: Out
  summary: RDS (or RBDS) signal *N*-element column vector | 2-by-*N* matrix
  direction: output
```

### Input

### **In** — FM-modulated baseband audio signal column vector

FM-modulated baseband audio signal, specified as a column vector. For
information about signal length restrictions, see Limitations.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes
### Output

### **Out** — RDS (or RBDS) signal *N*-element column vector | 2-by-*N* matrix

RDS (or RBDS) signal, returned as a column vector with the same data
type as the input signal.

- *N*-element column vector for mono
  signals — *N* is the number of samples in
  the audio signal. If you do not select **Stereo
  audio**, the output is a column vector.
- 2-by-*N* matrix for stereo signals —
  *N* is the number of samples in the
  audio signal per channel. If you select **Stereo
  audio**, the output has two channels and the
  block performs stereo decoding after de-emphasis filtering.
## Parameters
```yaml
parameters:
- name: Sample rate (Hz)
  summary: Output signal sample rate 240e3 | positive scalar
  group: ''
- name: Frequency deviation (Hz)
  summary: Peak deviation of the output signal frequency 75e3 | positive scalar
  group: ''
- name: De-emphasis filter time constant (s)
  summary: De-emphasis lowpass filter time constant 7.5e-05 (default) | positive scalar
  group: ''
- name: Output audio sample rate (Hz)
  summary: Output audio sample rate 48000 (default) | positive scalar
  group: ''
- name: Play audio device
  summary: Play sound using default audio device on (default) | off
  group: ''
- name: Buffer size (samples)
  summary: Buffer size 4096 (default) | positive scalar
  group: ''
- name: Stereo audio
  summary: Option to enable stereo demodulation off (default) | on
  group: ''
- name: RDS/RBDS demodulation
  summary: Option to enable RDS (or RBDS) waveform demodulation off (default) | on
  group: ''
- name: Number of samples per RDS/RBDS symbol
  summary: Number of samples output per RDS/RBDS symbol 10 (default) | positive integer
  group: ''
- name: RDS/RBDS Costas loop
  summary: Option to enable Costas Loop off (default) | on
  group: ''
- name: Simulate using
  summary: Type of simulation to run Code generation (default) | Interpreted execution
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Sample rate (Hz)** — Output signal sample rate `240e3` | positive scalar

Output signal sample rate in Hz, specified as a positive scalar. The sample rate must be
greater than twice the frequency deviation. Specifically, **Sample rate (Hz)**
> `2` × **Frequency deviation
(Hz)**.

### **Frequency deviation (Hz)** — Peak deviation of the output signal frequency `75e3` | positive scalar

Peak deviation of the modulator output signal frequency in Hz, specified
as a positive real scalar. The frequency deviation must be less than half
the sample rate.

The system bandwidth equals two times the sum of the frequency deviation
and the message bandwidth. FM broadcast standards specify a value of 75 kHz
in the United States and 50 kHz in Europe.

### **De-emphasis filter time constant (s)** — De-emphasis lowpass filter time constant `7.5e-05` (default) | positive scalar

De-emphasis lowpass filter time constant in seconds, specified as a
positive scalar. FM broadcast standards specify a value of 75 μs in the
United States and 50 μs in Europe.

### **Output audio sample rate (Hz)** — Output audio sample rate `48000` (default) | positive scalar

Specify the output audio sample rate in Hz as a positive scalar.

### **Play audio device** — Play sound using default audio device `on` (default) | `off`

Select this check box to play sound from a default audio device.

### **Buffer size (samples)** — Buffer size `4096` (default) | positive scalar

Specify the buffer size in samples that the block uses to communicate with
an audio device as a positive integer scalar.

#### Dependencies

To enable this parameter, select **Play audio
device**.

### **Stereo audio** — Option to enable stereo demodulation `off` (default) | `on`

Select this check box to enable demodulation of a stereo audio signal.

- If you do not select the **Stereo audio**
  check box, the audio signal is assumed to be monophonic.
- If you select the **Stereo audio** check
  box, the block demodulates the stereo audio
  (*L*–*R*) at the 38 KHz
  band, in addition to the baseband
  (*L*+*R*).

For more information, see Multiplexed Stereo and RDS (or RBDS) FM Signal.

### **RDS/RBDS demodulation** — Option to enable RDS (or RBDS) waveform demodulation `off` (default) | `on`

Select this check box to demodulate the RBDS signal from the input complex
baseband FM signal. For more information, see Multiplexed Stereo and RDS (or RBDS) FM Signal.

### **Number of samples per RDS/RBDS symbol** — Number of samples output per RDS/RBDS symbol `10` (default) | positive integer

Number of samples output per RDS/RBDS symbol, specified as a positive integer. The sample
rate of RDS (or RBDS) broadcast data is 1187.5 Hz. The RDS (or RBDS) sample
rate is by (**Number of samples per RDS/RBDS symbol** ×
`1187.5`) Hz.

#### Dependencies

To enable this parameter, select **RDS/RBDS
demodulation**.

### **RDS/RBDS Costas loop** — Option to enable Costas Loop `off` (default) | `on`

Specify whether the block uses a Costas loop to recover the phase of the RBDS signal.
Select this check box for radio stations that do not lock the
`57` kHz RBDS signal in phase with the third harmonic
of the `19` kHz pilot tone.

#### Dependencies

To enable this parameter, select **RDS/RBDS
demodulation**.

### **Simulate using** — Type of simulation to run `Code generation` (default) | `Interpreted execution`

Type of simulation to run, specified as `Code generation` or
`Interpreted execution`.

- `Code generation` — Simulate the model by using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The model reuses the C code
  for subsequent simulations unless the model changes. This option requires
  additional startup time, but the speed of the subsequent simulations is
  faster than with the `Interpreted execution`
  option.
- `Interpreted execution` — Simulate the model by
  using the MATLAB® interpreter. This option shortens startup time, but the speed
  of subsequent simulations is slower than with the `Code
  generation` option. In this mode, you can debug the source
  code of the block.

For more information, see Interpreted Execution vs. Code Generation (Simulink).
## Libraries

Communications Toolbox / Modulation / Analog Baseband Modulation

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015a**

## Description

Demodulate broadcast FM-modulated signal

The FM Broadcast Demodulator Baseband block demodulates a broadcast FM signal
into a stereophonic or monophonic audio signal, and the optional RDS (or RBDS) signal.
For more information, see Algorithms.

This icon shows the block with all ports enabled.FM Broadcast Demodulator Baseband block showing optional input port
