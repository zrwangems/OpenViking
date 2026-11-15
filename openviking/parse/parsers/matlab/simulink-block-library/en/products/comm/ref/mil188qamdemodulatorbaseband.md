---
type: simulink-block
title: 'MIL-188 QAM Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Amplitude and Phase Modulation'
documentation_page: 'mil188qamdemodulatorbaseband'
documentation_source_path: 'ref/mil188qamdemodulatorbaseband.html'
language: en
---

# MIL-188 QAM Demodulator Baseband

## Ports

### Input

### **In** — MIL-STD-188 standard-specific QAM modulated signal scalar | vector | matrix

MIL-STD-188 standard-specific QAM modulated signal, specified as a
scalar, vector, or matrix. When this input is a matrix, each column is
treated as an independent channel. This port is unnamed until the
`Var` port is enabled.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes

### **Var** — Noise variance positive scalar | vector of positive values

Noise variance, specified as a positive scalar or vector of positive
values. When the noise variance or signal power result in computations
involving extreme positive or negative magnitudes, see MIL-STD-188-110 QAM Soft Demodulation for
demodulation decision type considerations.

#### Dependencies

To enable this port set the **Noise variance source** parameter to
`Input port`.
### Output

### **Out** — Demodulated signal scalar | vector | matrix

Demodulated signal, returned as a scalar, vector, or matrix. The
dimensions of the demodulated signal depend on the specified **Output
type** and **Decision type** parameter values. This port is unnamed on
the block.

| **Output type** | **Decision type** | Demodulated Signal Description | **Dimensions of Demodulated Signal** |
| --- | --- | --- | --- |
| `Integer` | — | Demodulated integer values in the range [0, (*M* – 1)] | The output signal has the same dimensions as input signal. |
| `Bit` | `Hard decision` | Demodulated bits | The number of rows in the output signal is log2(*M*) times the number of rows in the input signal. Each demodulated symbol is mapped to a group of log2(*M*) elements in a column, where the first element represents the MSB, and the last element represents the LSB. |
| `Log-likelihood ratio` | Log-likelihood ratio value for each bit |
| `Approximate log-likelihood ratio` | Approximate log-likelihood ratio value for each bit |
| *M* is the value of **Modulation order**. | | | |

Use **Output
data type** to specify the output data type.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Modulation order** — Modulation order `16` (default) | `32` | `64` | `256`

Modulation order, *M*, specified as
`16`, `32`,
`64`, or `256`. The
modulation order specifies the total number of points in the constellation
of the input signal.

### **Constellation scaling** — Constellation scaling `As specified in standard` (default) | `Unit average power`

Constellation scaling, specified as:

- `As specified in standard` – The
  block scales the constellation based on specifications in the
  relevant standard [1].
- `Unit average power` – The block
  scales the constellation to an average power of 1 watt
  referenced to 1 ohm.

### **Output type** — Input type `Integer` (default) | `Bit`

Output type, specified as `Integer` or
`Bit`. To use
`Integer`, the input signal must consist of
integers in the range [0, (*M* – 1)]. To use `Bit`, the input signal
must contain binary values, and the number of rows must be an integer
multiple of log2(*M*), where *M* is the **Modulation
order**.

### **Decision type** — Demodulation decision type `Hard decision` (default) | `Log-likelihood ratio` | `Approximate log-likelihood ratio`

Demodulation decision type, specified as `Hard
decision`, `Log-likelihood ratio`,
or `Approximate log-likelihood ratio`. See MIL-STD-188-110 QAM Soft Demodulation for
algorithm selection considerations.

#### Dependencies

This parameter applies when you set **Output
type** to `Bit`.

### **Noise variance source** — Noise variance source `Property` (default) | `Input port`

Noise variance source, specified as:

- `Property` — Set the noise variance
  using the Noise variance parameter.
- `Input port` — Set the noise variance
  using the **Var** input port.

#### Dependencies

This parameter applies when you set **Decision type** to either `Log-likelihood
ratio` or `Approximate log-likelihood
ratio`.

### **Noise variance** — Noise variance `1` (default) | positive scalar | vector of positive values

Noise variance, specified as a positive scalar or vector of positive
values.

- When specified as a scalar, that value is used on all elements
  in the input signal.
- When specified as a vector, the vector length must be equal to
  the number of columns in the input signal. Each noise variance
  vector element is applied to its corresponding column in the
  input signal.

When the noise variance or signal power result in computations involving
extreme positive or negative magnitudes, see MIL-STD-188-110 QAM Soft Demodulation for
demodulation decision type considerations.

#### Dependencies

This parameter applies when you set **Noise
variance** to `Property` and
**Decision type** to either `Log-likelihood
ratio` or `Approximate log-likelihood
ratio`.

### **Output data type** — Output data type `double` (default) | `...`

Output data type, specified as one of the acceptable values from this
table. Acceptable **Output
data type** values depend on the **Output
type** and **Decision
type** parameter values.

| **Output type** | **Decision type** | **Output data type** Options |
| --- | --- | --- |
| `Integer` | Not applicable | `double`, `single`, `int8`, `uint8`, `int16`, `uint16`, `int32`, or `uint32` |
| `Bit` | `Hard decision` | `double`, `single`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `uint32`, or `logical` |
| `Log-likelihood ratio` or `Approximate log-likelihood ratio` | The output signal is the same data type as the input signal. |

#### Dependencies

This parameter applies when you set **Output
type** to `Integer` or when you
set **Output
type** to `Bit` and **Decision type** to `Hard
decision`.

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

Communications Toolbox / Modulation / Digital Baseband Modulation / AM Communications Toolbox / Modulation / Digital Baseband Modulation / Standard-Compliant

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `integer` | `single` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

MIL-STD-188-110 B/C standard-specific quadrature amplitude demodulation

The MIL-188 QAM Demodulator Baseband block demodulates the input signal using MIL-STD-188-110 standard-specific
quadrature amplitude modulation (QAM). For a description of MIL-STD-188 compliant
demodulation, see MIL-STD-188-110 QAM Hard Demodulation and MIL-STD-188-110 QAM Soft Demodulation.

This icon shows the block with all ports enabled:
