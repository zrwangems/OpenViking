---
type: simulink-block
title: 'FM Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Analog Baseband Modulation'
documentation_page: 'fmmodulatorbaseband'
documentation_source_path: 'ref/fmmodulatorbaseband.html'
language: en
---

# FM Modulator Baseband

## Ports
```yaml
ports:
- name: In
  summary: Input data signal scalar | vector | matrix
  direction: input
  data_types: double | single
- name: Out
  summary: Output data signal scalar | vector | matrix
  direction: output
  data_types: double | single
```

### Input

### **In** — Input data signal `scalar` | `vector` | `matrix`

Input signal, specified as a real scalar, vector, or matrix.

**Data Types:** `double` | `single`
### Output

### **Out** — Output data signal `scalar` | `vector` | `matrix`

Output signal, returned as a real scalar, vector, or matrix. The data at this port
has the same data type and size as the input signal.

**Data Types:** `double` | `single`
## Parameters
```yaml
parameters:
- name: Frequency deviation (Hz)
  summary: Frequency deviation of modulator 75e3 (default) | positive scalar
  group: ''
- name: Simulate using
  summary: Type of simulation to run Code generation (default) | Interpreted execution
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Frequency deviation (Hz)** — Frequency deviation of modulator `75e3` (default) | `positive scalar`

Frequency deviation of the modulator, in Hz, specified as a positive scalar. The
system bandwidth is equal to twice the sum of the frequency deviation and the message
bandwidth.

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

Modulate using FM method

The FM Modulator Baseband block applies frequency modulation to a real
input signal and returns a complex output signal.
