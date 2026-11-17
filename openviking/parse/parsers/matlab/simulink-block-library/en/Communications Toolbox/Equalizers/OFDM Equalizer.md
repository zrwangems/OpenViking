---
type: simulink-block
title: 'OFDM Equalizer'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Equalizers'
documentation_page: 'ofdmequalizerblock'
documentation_source_path: 'ref/ofdmequalizerblock.html'
language: en
---

# OFDM Equalizer

## Ports
```yaml
ports:
- name: in
  summary: Input signal 3-D array | 2-D array
  direction: input
  data_types: double | single
- name: hEst
  summary: Channel estimate 3-D array
  direction: input
  data_types: double | single
- name: noiseVar
  summary: Noise variance 0 (default) | nonnegative scalar
  direction: input
  data_types: double | single
- name: out
  summary: Equalized symbols 3-D array | 2-D array
  direction: output
- name: csi
  summary: Soft channel state information matrix
  direction: output
```

### Input

### **in** — Input signal 3-D array | 2-D array

Input signal, specified as a 3-D or 2-D array of received OFDM symbols.

- If **Data format** is set to
  `3-D`, the input signal must be
  specified as an
  *N*SC-by-*N*Symbols-by-*N*R
  array. *N*SC
  represents the number of OFDM subcarriers,
  *N*Symbols
  represents the number of OFDM symbols, and
  *N*R represents
  the number of receive antennas.
- If **Data format** is set to
  `2-D`, the input signal must be
  specified as an
  *N*RE-by-*N*R
  array. *N*RE
  represents the number of resource elements in an irregular
  subset of the OFDM subcarrier symbol grid.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes

### **hEst** — Channel estimate 3-D array

Channel estimate, specified as a 3-D array.

- If **Data format** is set to
  `3-D`, the block expects
  **hEst** to be an
  *N*SC-by-*N*T-by-*N*R
  or an
  (*N*SC×*N*Symbols)-by-*N*T-by-*N*R array.

  - If **hEst** is an
    *N*SC-by-*N*T-by-*N*R
    array, all OFDM symbols in the input signal
    `in` are equalized by the same
    channel estimate.
    *N*SC
    represents the number of OFDM subcarriers,
    *N*T
    represents the number of transmit antennas, and
    *N*R
    represents the number of receive antennas.
  - If **hEst** is an
    (*N*SC×*N*Symbols)-by-*N*T-by-*N*R
    array, each OFDM symbol in the input signal
    `in` is equalized by the
    corresponding entry in **hEst**.
    *N*Symbols
    represents the number of OFDM symbols.
- If **Data format** is set to
  `2-D`, the block expects
  **hEst** to be an
  *N*RE-by-*N*T-by-*N*R
  array. Each OFDM symbol in the input signal
  `in` is equalized by the
  corresponding entry in **hEst**.
  *N*RE represents
  the number of resource elements in an irregular subset of
  the OFDM subcarrier symbol grid.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes

### **noiseVar** — Noise variance 0 (default) | nonnegative scalar

Noise variance estimate for minimum mean squared error (MMSE)
equalization, specified as a nonnegative scalar.

#### Dependencies

The noise variance input port is used only when you set
**Noise variance source** to `Input
port` and **Algorithm** to
`Minimum mean squared error`.

**Data Types:** `double` | `single`
### Output

### **out** — Equalized symbols 3-D array | 2-D array

Equalized symbols, returned as a 3-D or 2-D array.

- If **Data format** is set to
  `3-D`, the block returns an
  *N*SC-by-*N*Symbols-by-*N*T
  array. *N*SC
  represents the number of OFDM subcarriers,
  *N*Symbols
  represents the number of OFDM symbols, and
  *N*T represents
  the number of transmit antennas.
- If **Data format** is set to
  `2-D`, the block returns an
  *N*RE-by-*N*T
  array. *N*RE
  represents the number of resource elements in an irregular
  subset of the OFDM subcarrier symbol grid.

### **csi** — Soft channel state information matrix

Soft channel state information, returned as a matrix with
`size(csi,1) = size(hEst,1)` and
`size(csi,2) = NT
= size(hEst,2)`.
*N*T represents the number
of transmit antennas.

#### Dependencies

To enable this output port, select the **Output soft
channel state information** parameter.
## Parameters
```yaml
parameters:
- name: Data format
  summary: Format of signals 3-D (default) | 2-D
  group: ''
- name: Algorithm
  summary: Equalization algorithm Minimum mean squared error (default) | Zero-forcing
  group: ''
- name: Noise variance source
  summary: Source of noise variance Input port (default) | Property
  group: ''
- name: Noise variance
  summary: Noise variance 0 (default) | nonnegative scalar
  group: ''
- name: Output soft channel state information
  summary: Enable soft channel state information output off (default) | on
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Data format** — Format of signals `3-D` (default) | `2-D`

Format of the signals, specified as `3-D` or
`2-D`.

When this parameter is set to `3-D`, OFDM
subcarriers and OFDM symbols use two separate dimensions in the
representation of **in** and **out**.

- The **in** input must be an
  *N*SC-by-*N*Symbols-by-*N*R
  array.
- The **out** output is returned as an
  *N*SC-by-*N*Symbols-by-*N*T
  array.

When this parameter is set to `2-D`, OFDM
subcarriers and OFDM symbols use one combined dimension in the
representation of **in** and **out**.

- The **in** input must be an
  *N*RE-by-*N*R
  array.
- The **out** output is returned as an
  *N*RE-by-*N*T
  array.

*N*SC represents the number of
OFDM subcarriers. *N*Symbols
represents the number of symbols.
*N*RE represents the number of
resource elements in an irregular subset of the OFDM subcarrier symbol grid.
*N*T represents the number of
transmit antennas. *N*R represents
the number of receive antennas.

### **Algorithm** — Equalization algorithm `Minimum mean squared error` (default) | `Zero-forcing`

Equalization algorithm, specified as `Minimum mean squared
error` or `Zero-forcing`.

- When this parameter is set to `Minimum mean
  squared error`, the block equalizes using the
  MMSE algorithm.
- When this parameter is set to
  `Zero-forcing`, the block equalizes
  using the zero-forcing algorithm. When using the zero-forcing
  algorithm, the **noiseVar** port value is
  ignored.

### **Noise variance source** — Source of noise variance `Input port` (default) | `Property`

Source of noise variance, specified as one of these values:

- `Input port` — Specify this value to
  use the **noiseVar** input port to specify the
  noise variance estimate for MMSE equalization.
- `Property` — Specify this value to
  use the **Noise variance** parameter to specify
  the noise variance estimate for MMSE equalization.

### **Noise variance** — Noise variance 0 (default) | nonnegative scalar

Noise variance estimate for MMSE equalization, specified as a nonnegative
scalar.

#### Dependencies

The noise variance setting is used only when you set **Noise
variance source** to `Property`
and **Algorithm** to `Minimum mean squared
error`.

### **Output soft channel state information** — Enable soft channel state information output `off` (default) | `on`

Select this parameter to enable output port **csi**
containing the soft channel state information.

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

Communications Toolbox / Equalizers

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Equalize OFDM modulated signals

The OFDM Equalizer block performs frequency-domain equalization to recover OFDM modulated
symbols transmitted through a channel.

This icon shows the block with all ports enabled.

OFDM Equalizer block showing optional ports.
