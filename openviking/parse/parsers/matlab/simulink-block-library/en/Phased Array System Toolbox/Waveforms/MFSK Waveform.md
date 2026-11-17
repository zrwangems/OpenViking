---
type: simulink-block
title: 'MFSK Waveform'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Waveforms'
documentation_page: 'mfskwaveform'
documentation_source_path: 'ref/mfskwaveform.html'
language: en
---

# MFSK Waveform

## Ports
```yaml
ports:
- name: Port_1
  summary: MFSK Waveform complex-valued column vector
  direction: output
```

### Output

### **Port\_1** — MFSK Waveform complex-valued column vector

MFSK waveform, returned as a complex-valued column vector containing
the waveform samples.

- If the **Output signal format** parameter
  is set to `Steps`, the output of the port
  consists of the number of steps set by the **Number
  of frequency steps in output**
  parameter.
- If the **Output signal format** parameter
  is set to `Samples`, the output of the port
  consists of the number of samples set by the
  **Number of samples in output**
  parameter.
- If the **Output signal format** parameter
  is set to `Sweeps`, the output of the port
  consists of the number of sweeps set by the **Number
  of sweeps in output** parameter.
## Parameters
```yaml
parameters:
- name: Sample rate (Hz)
  summary: Sample rate 151e6 (default) | positive scalar
  group: ''
- name: Sweep bandwidth (Hz)
  summary: MFSK sweep bandwidth 150e6 (default) | positive scalar
  group: ''
- name: Frequency step burst time (s)
  summary: Frequency step burst time 5e-6 (default) | positive scalar
  group: ''
- name: Number of steps per sweep
  summary: Total number of frequency steps 512 (default) | even positive scalar
  group: ''
- name: Chirp offset frequency (Hz)
  summary: Chirp offset frequency -294e3 (default) | real scalar
  group: ''
- name: Output signal format
  summary: Output signal format Steps (default) | Samples | Sweeps
  group: ''
- name: Number of sweeps in output
  summary: Number of sweeps in output 1 (default) | positive integer
  group: ''
- name: Number of frequency steps in output
  summary: Number of frequency steps in output 1 (default) | positive integer
  group: ''
- name: Number of samples in output
  summary: Number of samples in output 100 (default) | positive integer
  group: ''
  block_parameter: NumSamples
  type: double
  values: positive scalar
  default: '100'
- name: Simulate using
  summary: Block simulation method Interpreted Execution (default) | Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution, Code Generation
  default: Interpreted Execution
```

### **Sample rate (Hz)** — Sample rate `151e6` (default) | positive scalar

Sample rate of the signal, specified as a positive scalar. Units are in
hertz.

### **Sweep bandwidth (Hz)** — MFSK sweep bandwidth `150e6` (default) | positive scalar

Bandwidth of the MFSK sweep, specified as a positive scalar. Units are in
hertz.

### **Frequency step burst time (s)** — Frequency step burst time `5e-6` (default) | positive scalar

Time duration of each frequency step, specified as a positive scalar.
Units are in seconds.

### **Number of steps per sweep** — Total number of frequency steps `512` (default) | even positive scalar

Total number of steps in each sweep, specified as an even positive
integer.

### **Chirp offset frequency (Hz)** — Chirp offset frequency `-294e3` (default) | real scalar

Chirp offset frequency, specified as a real scalar. Units are in hertz.
The offset determines the frequency translation between the two
sequences.

### **Output signal format** — Output signal format `Steps` (default) | `Samples` | `Sweeps`

Format of the output signal, specified as one of the following:

- `Steps` — The block outputs the
  number of samples contained in an integer number of frequency steps
  specified by the **Number of frequency steps in
  output** parameter.
- `Samples` — The block outputs the
  number of samples specified in the **Number of samples in
  output** parameter.
- `Sweeps` — The block outputs the
  number of samples contained in an integer number of sweeps specified
  by the **Number of sweeps in output**
  parameter.

### **Number of sweeps in output** — Number of sweeps in output `1` (default) | positive integer

Number of sweeps in the block output, specified as a positive
integer.

#### Dependencies

This parameter appears only when you set **Output signal
format** to `Sweeps`.

### **Number of frequency steps in output** — Number of frequency steps in output `1` (default) | positive integer

Number of steps in the block output, specified as a positive
integer.

#### Dependencies

This parameter appears only when you set **Output signal
format** to `Steps`.

### **Number of samples in output** — Number of samples in output `100` (default) | positive integer

Number of samples in the block output, specified as a positive integer.

**Example:** `1000`

#### Dependencies

To enable this parameter, set the **Output signal format**
parameter to `Samples`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`NumSamples` |
| **Type:**double |
| **Values:**`positive scalar` |
| **Default:**`100` |

**Data Types:** `double`

### **Simulate using** — Block simulation method `Interpreted Execution` (default) | `Code Generation`

Block simulation, specified as `Interpreted Execution` or
`Code Generation`. If you want your block to use the
MATLAB® interpreter, choose `Interpreted Execution`. If
you want your block to run as compiled code, choose `Code
Generation`. Compiled code requires time to compile but usually runs
faster.

Interpreted execution is useful when you are developing and tuning a model. The block
runs the underlying System object™ in MATLAB. You can change and execute your model quickly. When you are satisfied
with your results, you can then run the block using `Code
Generation`. Long simulations run faster with generated code than in
interpreted execution. You can run repeated executions without recompiling, but if you
change any block parameters, then the block automatically recompiles before
execution.

This table shows how the **Simulate using** parameter affects the
overall simulation behavior.

When the Simulink® model is in `Accelerator` mode, the block mode specified
using **Simulate using** overrides the simulation mode.

**Acceleration Modes**

|  |  |  |  |
| --- | --- | --- | --- |
| Block Simulation | Simulation Behavior | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | The block executes using the MATLAB interpreter. | The block executes using the MATLAB interpreter. | Creates a standalone executable from the model. |
| `Code Generation` | The block is compiled. | All blocks in the model are compiled. |

For more information, see Choosing a Simulation Mode (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimulateUsing` |
| **Type:** enum |
| **Values:** `Interpreted Execution`, `Code Generation` |
| **Default:** `Interpreted Execution` |
## Libraries

Phased Array System Toolbox / Waveforms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2015a**

## Description

Multiple frequency shift keying (MFSK) continuous waveform

The MFSK Waveform block generates a multiple frequency-shift keying (MFSK)
continuous waveform with a specified step time, sweep bandwidth, frequency offset, and
number of steps. The block outputs an integer number of samples, steps, or sweeps. For
details on the structure of an MFSK waveform, see `phased.MFSKWaveform`.
