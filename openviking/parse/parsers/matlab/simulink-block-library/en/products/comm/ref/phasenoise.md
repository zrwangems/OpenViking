---
type: simulink-block
title: 'Phase Noise'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Component Modeling / Impairments and Components'
documentation_page: 'phasenoise'
documentation_source_path: 'ref/phasenoise.html'
language: en
---

# Phase Noise

## Ports

### Input

### **In** — Input signal vector | matrix

Input signal, specified as an
*N*S-by-1 numeric vector or
*N*S-by-*M*
numeric matrix. *N*S represents
the number of samples and *M* is the number of
channels.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes
### Output

### **Out** — Output signal vector | matrix

Output signal, returned as a complex-valued signal with the same data
type and size as the input signal.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Phase noise level (dBc/Hz)** — Phase noise level `[-80 -100]` (default) | vector of negative scalars

Phase noise level in decibels relative to carrier per hertz (dBc/Hz),
specified as a vector of negative scalars. The **Phase noise level
(dBc/Hz)** and **Frequency offset (Hz)**
parameters must have the same length.

### **Frequency offset (Hz)** — Frequency offset `[2000 20000]` (default) | vector of positive increasing values

Frequency offset in Hz, specified as a vector of positive increasing
values. The maximum frequency offset value must be less than *F*S /
2, where *F*S
represents the **Sample rate (Hz)** parameter value.

The **Phase noise level (dBc/Hz)** and
**Frequency offset (Hz)** parameters must have the same
length.

### **Sample rate (Hz)** — Sample rate `1e6` (default) | positive scalar

Sample rate in Hz, specified as a positive scalar greater than two times
the maximum value specified by the **Frequency offset
(Hz)** parameter.

### **Initial seed** — Initial seed of noise generator `2137` (default) | positive scalar

Initial seed of noise generator, specified as a positive scalar.

This block uses the Random Source block to generate
noise. The block generates random numbers using the Ziggurat method (V5
RANDN algorithm). Every time you rerun the simulation, the block reuses the
same initial seed. That way, the block outputs the same signal each time you
run a simulation.

### **View Filter Response** — Display magnitude response of filter button

Display magnitude response of filter defined by the block.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Type of simulation to run, specified as `Interpreted
execution` or `Code generation`.

- `Interpreted execution` — Simulate the model by
  using the MATLAB® interpreter. This option requires less startup time, but the
  speed of subsequent simulations is slower than with the `Code
  generation` option. In this mode, you can debug the source
  code of the block.
- `Code generation` — Simulate the model by using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The model reuses the C code
  for subsequent simulations unless the model changes. This option requires
  additional startup time, but the speed of the subsequent simulations is
  faster than with the `Interpreted execution`
  option.

For more information, see Interpreted Execution vs. Code Generation (Simulink).

## Libraries

Communications Toolbox / RF Impairments and Components

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

### R2024a: Model high frequency phase noise impairment

Use the Phase Noise block to accurately model
phase noise at higher frequency signals. Use the **View Filter
Response** button on Phase Noise block mask to verify
the accuracy of the realized phase noise.

## Description

Apply receiver phase noise to complex baseband signal

The Phase Noise block adds phase noise to a complex signal. This block emulates
impairments introduced by the local oscillator of a wireless communication transmitter
or receiver. The block generates filtered phase noise according to the specified
spectral mask and adds it to the input signal. For a description of the phase noise
modeling, see Algorithms.
