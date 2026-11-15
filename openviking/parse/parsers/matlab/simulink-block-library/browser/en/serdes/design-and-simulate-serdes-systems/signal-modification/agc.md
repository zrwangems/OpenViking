---
type: simulink-block
title: 'AGC'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Design and Simulate SerDes Systems / Signal Modification'
documentation_page: 'agc'
documentation_source_path: 'ref/agc.html'
language: en
---

# AGC

## Ports

### Input

### **WaveIn** — Input baseband signal scalar | vector

Input baseband signal. The input signal can be a sample-by-sample signal specified
as a scalar, or an impulse response vector signal.

**Data Types:** `double`
### Output

### **WaveOut** — Estimated channel output scalar | vector

Estimated channel output. If the input signal is a sample-by-sample signal
specified as a scalar, the output is also scalar. If the input signal is an impulse
response vector signal, the output is also a vector.

**Data Types:** `double`

## Parameters

### **Mode** — AGC operating mode `On` (default) | `Off`

AGC operating mode:

- `Off` — AGC is bypassed, the input waveform
  remains unchanged.
- `On` — AGC adjusts gain of input waveform to
  maintain **Target RMS voltage** in output waveform.

#### Programmatic Use

- Use `get_param(gcb,'Mode')` to view the current AGC
  **Mode**.
- Use `set_param(gcb,'Mode',value)` to set AGC to a specific
  **Mode**.

### **Target RMS voltage (V)** — Desired RMS voltage of output waveform `0.3` (default) | real scalar in the range [0.003, 10]

Desired RMS voltage of the output waveform, specified as a real scalar in the range
[0.003, 10] in volts.

#### Programmatic Use

- Use `get_param(gcb,'TargetRMSVoltage')` to view the
  current value of **Target RMS voltage (V)**.
- Use `set_param(gcb,'TargetRMSVoltage',value)` to set
  **Target RMS voltage (V)** to a specific value.

**Data Types:** `double`

### **Maximum gain** — Maximum allowed AGC gain `10` (default) | positive real scalar

Maximum allowed AGC gain, specified as a positive real scalar. **Maximum
gain** provides a stable startup of the adaptive algorithm.

#### Programmatic Use

- Use `get_param(gcb,'MaxGain')` to view the current value
  of **Maximum gain**.
- Use `set_param(gcb,'MaxGain',value)` to set
  **Maximum gain** to a specific value.

**Data Types:** `double`

### **Averaging length** — Averaging length for RMS calculation `100` (default) | positive real scalar

Averaging length, specified as a positive real integer. **Averaging
length** defines the number of symbol over which the RMS calculation of the
input signal is made.

#### Programmatic Use

- Use `get_param(gcb,'AveragingLength')` to view the
  current value of **Averaging length**.
- Use `set_param(gcb,'AveragingLength',value)` to set
  **Averaging length** to a specific value.

**Data Types:** `double`

#### IBIS-AMI parameters

### **Mode** — Include Mode parameter in IBIS-AMI model on (default) | off

Select to include **Mode** as a parameter in the IBIS-AMI file. If
you deselect **Mode**, it is removed from the AMI files, effectively
hard-coding **Mode** to its current value.

### **Target RMS voltage** — Include Target RMS voltage parameter in IBIS-AMI model on (default) | off

Select to include **Target RMS voltage** as a parameter in the
IBIS-AMI file. If you deselect **Target RMS voltage**, it is removed
from the AMI files, effectively hard-coding **Target RMS voltage** to
its current value.

## Libraries

SerDes Toolbox / Datapath Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Automatically adjusts gain to maintain output waveform amplitude

The AGC  block applies an adaptive variable gain to the input waveform to
achieve a desired RMS output voltage. Averaging the RMS voltage over a specified number of
symbols, AGC performs automatic gain control (AGC) by increasing or decreasing
the gain, or keeping the gain constant.
