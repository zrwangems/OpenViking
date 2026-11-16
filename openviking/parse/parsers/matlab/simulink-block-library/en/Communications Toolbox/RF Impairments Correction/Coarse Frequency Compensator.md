---
type: simulink-block
title: 'Coarse Frequency Compensator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments Correction'
documentation_page: 'coarsefrequencycompensator'
documentation_source_path: 'ref/coarsefrequencycompensator.html'
language: en
---

# Coarse Frequency Compensator

## Ports

### Input

### **In** — Input signal column vector

Input signal, specified as a column vector.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **Out** — Compensated output signal complex column vector

Compensated output signal, returned as a complex column vector with
the same dimensions and data type as the input **In**.

**Data Types:** `single` | `double`

### **FreqEst** — Estimate of frequency offset scalar

Estimate of the frequency offset, returned as a scalar.

If you set the **Modulation type of input signal** parameter to
`OQPSK` or `QAM`,
or set the **Estimation algorithm** parameter to
`FFT-based`, the returned frequency offset
estimate is an integer multiple of the **Frequency resolution (Hz)** parameter.

#### Dependencies

To add this port, select **Estimated frequency offset output port**.

**Data Types:** `single` | `double`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Modulation type of input signal** — Modulation type `QAM` (default) | `8PSK` | `BPSK` | `OQPSK` | `PAM` | `QPSK`

Modulation type, specified as `QAM`,
`8PSK`, `BPSK`,
`OQPSK`, `PAM`, or
`QPSK`.

### **Estimation algorithm** — Algorithm used to estimate frequency offset `FFT-based` (default) | `Correlation-based`

Specify the frequency offset estimation algorithm as `FFT-based`
or `Correlation-based`. For more information, see
Algorithms.

**Note**

When you set the **Modulation type of input signal** parameter to
`'OQPSK'` or `'QAM'`, the block
uses the FFT-based estimation algorithm.

#### Dependencies

This parameter appears when you set **Modulation type of input signal** to
`8PSK`, `BPSK`,
`PAM`, or
`QPSK`.

### **Frequency resolution (Hz)** — Frequency resolution `100` (default) | positive scalar

Frequency resolution in Hz, specified as a positive real scalar.

#### Dependencies

This parameter applies when you set **Modulation type of input signal** to
`OQPSK` or `QAM`,
or you set **Estimation algorithm** to
`FFT-based`.

### **Samples per symbol** — Number of samples per symbol `4` (default) | even integer greater than or equal to `4`

Number of samples per symbol, specified as an even integer scalar greater than or equal
to 4.

#### Dependencies

This parameter appears when you set **Modulation type of input signal** to
`OQPSK`.

### **Maximum frequency offset (Hz)** — Maximum measurable frequency offset `5e3` (default) | positive scalar

Maximum measurable frequency offset in Hz, specified as a positive
scalar.

#### Dependencies

This parameter appears when you set **Estimation algorithm** to
`Correlation-based`.

### **Estimated frequency offset output port** — Option to add estimated frequency offset output port `on` (default) | `off`

Select this check box to add the **FreqEst** output port. The **FreqEst** port outputs the
estimated frequency offset in Hz.

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

Communications Toolbox / RF Impairments Correction Communications Toolbox / Synchronization

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015b**

### R2025a: Estimated frequency offset returned as integer multiple of frequency resolution

When configured to use the FFT-based algorithm, the Coarse Frequency Compensator
block now returns the estimated frequency offset, **FreqEst**, as
an integer multiple of the **Frequency
resolution (Hz)** parameter value.

### R2023b: Default settings change

The Coarse Frequency Compensator block parameters have new default values.

| Parameter | New Default | Previous Default |
| --- | --- | --- |
| **Frequency resolution (Hz)** | `100` | `0.001` |
| **Maximum frequency offset (Hz)** | `5e3` | `0.05` |

When executing code created in a previous release, confirm the
coarse frequency compensator settings. The new default settings change your results.
To produce results using the previous default settings, you can manually update the
settings of your block.

## Description

Compensate for carrier frequency offset in PAM, PSK, or QAM

The Coarse Frequency Compensator block compensates for carrier frequency offset in QAM, 8-PSK,
BPSK, OQPSK, PAM, and QPSK modulation schemes.
