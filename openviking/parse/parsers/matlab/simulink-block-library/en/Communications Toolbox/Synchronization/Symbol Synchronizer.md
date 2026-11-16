---
type: simulink-block
title: 'Symbol Synchronizer'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Synchronization'
documentation_page: 'symbolsynchronizer'
documentation_source_path: 'ref/symbolsynchronizer.html'
language: en
---

# Symbol Synchronizer

## Ports

### Input

### **Samp** — Input samples scalar (default) | column vector

Input samples, specified as a scalar or column vector of a PAM, PSK,
QAM, or OQPSK modulated single-carrier signal. This port in unnamed on
the block.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes
### Output

### **Sym** — Output signal symbols scalar | column vector

Output signal symbols, returned as a variable-size scalar or column
vector that has the same data type as the input. For an input with
dimensions of *N*samp-by-1, the
output at **Sym** has dimensions of
*N*sym-by-1.
*N*sym is approximately
equal to *N*samp divided by the
*N*sps.
*N*sps is equal to the
**Samples per symbol** parameter value. The
output length is truncated if it exceeds the maximum output size of ⌈NsampNsps×1.1⌉.

This port is unnamed when **Normalized timing error output
port** is not selected.

### **Err** — Estimated timing error scalar | column vector

Estimated timing error for each input sample, returned as a scalar or
column vector with values in the range [0, 1]. The estimated timing
error is normalized by the input sample time. **Err**
has the same data type and size as the input signal.

#### Dependencies

To enable this port, select **Normalized timing error
output port**.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Modulation type** — Modulation type `PAM/PSK/QAM` (default) | `OQPSK`

Modulation type, specified as `PAM/PSK/QAM`, or
`OQPSK`. When using OQPSK modulation, see Tips.

### **Timing error detector** — Type of timing error detector `Zero-Crossing (decision-directed)` (default) | `Gardner (non-data-aided)` | `Early-Late (non-data-aided)` | `Mueller-Muller (decision-directed)`

Type of timing error detector, specified as `Zero-Crossing
(decision-directed)`, `Gardner
(non-data-aided)`, `Early-Late
(non-data-aided)`, or `Mueller-Muller
(decision-directed)`. This parameter assigns the timing
error detection scheme used in the synchronizer.

For more information, see Timing Error Detection (TED).

### **Samples per symbol** — Samples per symbol `2` (default) | positive integer greater than 1

Samples per symbol, specified as a positive integer greater than 1. For
more information, see *N*sps in
Loop Filter.

### **Damping factor** — Damping factor of the loop filter `1` (default) | positive scalar

Damping factor of the loop filter, specified as a positive scalar. For
more information, see *ζ* in Loop Filter.

**Tunable:** Yes

### **Normalized loop bandwidth** — Normalized bandwidth of loop filter `0.01` (default) | positive scalar less than 1

Normalized bandwidth of the loop filter, specified as a positive scalar less than 1. The
loop bandwidth (*B*n) is normalized
by the symbol rate (*T*s) of the
input signal. For more information, see
*B*n*T*s
in Loop Filter.

**Note**

To ensure that the symbol synchronizer locks, set the
**Normalized loop bandwidth** parameter to a value
less than `0.1`.

**Tunable:** Yes

### **Detector gain** — Phase detector gain `2.7` (default) | positive scalar

Phase detector gain, specified as a positive scalar. For more information,
see *K*p in Loop Filter.

**Tunable:** Yes

### **Normalized timing error output port** — Enable normalized timing error output port `on` (default) | `off`

Select this parameter to output normalized timing error data at the output
port **Err**.

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

Communications Toolbox / Synchronization

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015a**

## Description

Correct symbol timing clock skew

The Symbol Synchronizer block corrects symbol timing clock skew for PAM, PSK,
QAM, or OQPSK modulation schemes between a single-carrier transmitter and receiver. For
more information, see Symbol Synchronization Overview.

**Note**

The input signal operates on a sample rate basis, while the output signal
operates on a symbol rate basis.
