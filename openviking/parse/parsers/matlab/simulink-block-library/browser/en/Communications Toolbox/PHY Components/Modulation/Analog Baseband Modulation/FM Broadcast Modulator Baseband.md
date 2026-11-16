---
type: simulink-block
title: 'FM Broadcast Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Analog Baseband Modulation'
documentation_page: 'fmbroadcastmodulatorbaseband'
documentation_source_path: 'ref/fmbroadcastmodulatorbaseband.html'
language: en
---

# FM Broadcast Modulator Baseband

## Ports

### Input

### **In1** — Audio signal *N*-element column vector | 2-by-*N* matrix

Audio signal, specified as one of these options.

- *N*-element column vector for mono
  signals — If you do not select **Stereo
  audio**, you must specify the audio signal as
  a column vector. *N* is the number of
  samples in the audio signal.
- 2-by-*N* matrix for stereo signals — If
  you select **Stereo
  audio**, the audio signal must have two
  channels and the block performs stereo encoding after
  pre-emphasis filtering. *N* is the number
  of samples in the audio signal per channel.

For information about signal length restrictions, see
Limitations.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes

### **In2** — RDS (or RBDS) signal *N*-element column vector | 2-by-*N* matrix

RDS (or RBDS) signal, specified as one of these options.

- *N*-element column vector for mono
  signals — If you do not select **Stereo
  audio**, you must specify the audio signal as
  a column vector. *N* is the number of
  samples in the audio signal.
- 2-by-*N* matrix for stereo signals — If
  you select **Stereo
  audio**, the audio signal must have two
  channels and the block performs stereo encoding after
  pre-emphasis filtering. *N* is the number
  of samples in the audio signal per channel.

For information about signal length restrictions, see
Limitations.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes
### Output

### **Out** — FM-modulated baseband signal column vector

FM-modulated baseband signal, returned as a column vector of complex values of the same
data type as the input signal. The length of this output is
`length`(`Input 1` × **Sample rate
(Hz)** / **Sample rate of audio
input signal (Hz)**).

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Sample rate (Hz)** — Output signal sample rate `240e3` | positive scalar

Output signal sample rate in Hz, specified as a positive scalar. The
sample rate must be greater than twice the frequency deviation.
Specifically, **Sample rate** > 2×**Frequency
Deviation**.

### **Frequency deviation (Hz)** — Peak deviation of modulator output signal frequency `75e3` | positive scalar

Peak deviation of the modulator output signal frequency in Hz, specified
as a positive scalar. The frequency deviation must be less than half the
sample rate.

The system bandwidth equals two times the sum of the frequency deviation
and the message bandwidth. FM broadcast standards specify a value of 75 kHz
in the United States and 50 kHz in Europe.

### **Pre-emphasis filter time constant (s)** — Pre-emphasis highpass filter time constant `7.5e-05` (default) | positive scalar

Pre-emphasis highpass filter time constant in seconds, specified as a
positive scalar. FM broadcast standards specify a value of 75 μs in the
United States and 50 μs in Europe.

### **Sample rate of audio input signal (Hz)** — Sample rate of input audio signal `48000` (default) | positive scalar

Sample rate of the input audio signal in Hz, specified as a positive
scalar.

### **Stereo audio** — Option to enable stereo modulation `off` (default) | `on`

Select this check box if the input signal is a stereophonic audio signal. If you do not
select, the audio signal is assumed to be monophonic. If you select the
**Stereo audio** check box, the block modulates the
stereo audio (*L*–*R*) at the 38 kHz band,
in addition to the baseband (*L*+*R*). For
more information, see Multiplexed Stereo and RDS (or RBDS) FM Signal.

### **RDS/RBDS modulation** — Option to enable RDS (or RBDS) waveform modulation `off` (default) | `on`

Select this check box to modulate a baseband RBDS signal at 57 kHz. For
more information, see Multiplexed Stereo and RDS (or RBDS) FM Signal.

### **Oversampling factor of RDS/RBDS input** — Oversampling factor of RDS (or RBDS) input signal `10` (default) | positive integer

Oversampling factor of the RDS (or RBDS) input signal, specified as a positive integer.
The sample rate of RDS (or RBDS) broadcast data is 1187.5 Hz. The RDS (or
RBDS) signal sample rate is (**Oversampling factor of RDS/RBDS
input** × `1187.5`) Hz.

#### Dependencies

To enable this parameter, select **RDS/RBDS
modulation**.

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

Modulate using broadcast FM method

The FM Broadcast Modulator Baseband block creates the FM channel structure for broadcast of an FM signal. For
more details, see Algorithms.

This icon shows the block with all ports enabled.FM Broadcast Modulator Baseband block showing optional input port
