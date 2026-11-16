---
type: simulink-block
title: 'DVBS-APSK Demodulator Baseband'
family: 'satcom'
product_id: 'satcom'
product_name: 'Satellite Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation'
documentation_page: 'dvbsapskdemodulatorbaseband'
documentation_source_path: 'ref/dvbsapskdemodulatorbaseband.html'
language: en
---

# DVBS-APSK Demodulator Baseband

## Ports

### Input

### **In** — DVB-S2/S2X/SH standard-specific APSK modulated signal scalar | vector | matrix

DVB-S2/S2X/SH standard-specific APSK modulated signal, specified as a
scalar, vector, or matrix. When this input is a matrix, each column is
treated as an independent channel. This port is unnamed until the
`Var` port is enabled.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes

### **Var** — Noise variance positive scalar | vector of positive values

Noise variance, specified as a positive scalar or vector of positive values. When the
noise variance or signal power result in computations involving extreme
positive or negative magnitudes, see DVB Compliant APSK Soft Demodulation for
demodulation decision type considerations.

#### Dependencies

This parameter applies when **Noise variance source** is set to `Input
port`.

**Data Types:** `double` | `single`
### Output

### **Out** — Demodulated signal scalar | vector | matrix

Demodulated signal, returned as a scalar, vector, or matrix. The dimensions of the
demodulated signal depend on the specified **Output type** and **Decision type**. This port is unnamed on the
block.

| **Output type** | **Decision type** | **Demodulated Signal Description** | **Dimensions of Demodulated Signal** |
| --- | --- | --- | --- |
| `Integer` | — | Demodulated integer values in the range [0, (*M* – 1)] | The output signal has the same dimensions as the input signal. |
| `Bit` | `Hard decision` | Demodulated bits | The number of rows in the output signal is log2(*M*) times the number of rows in the input signal. Each demodulated symbol is mapped to a group of log2(*M*) elements in a column, where the first element represents the MSB and the last element represents the LSB. |
| `Log-likelihood ratio` | Log-likelihood ratio value for each bit |
| `Approximate log-likelihood ratio` | Approximate log-likelihood ratio value for each bit |
| *M* is the value of **Modulation order**. | | | |

Use **Output data type** to specify the output data
type.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **DVB standard suffix** — Standard suffix `S2` | `S2X` | `SH`

Standard suffix for DVB modulation variant, specified as
`S2`, `S2X`, or
`SH`.

### **Frame length** — Frame length `Normal` (default) | `Short`

Frame length, specified as `Normal` or
`Short`.

#### Dependencies

This parameter applies only when **DVB
standard suffix** is set to `S2`
or `S2X`.

### **Modulation order** — Modulation order `16` (default) | integer

Modulation order, specified as a power of two. The modulation order specifies the total
number of points in the constellation of the input signal. The list of valid
modulation orders varies depending on the setting for **DVB
standard suffix** and **Frame
length**.

| **DVB standard suffix** | **Frame length** | **Modulation order** Options |
| --- | --- | --- |
| `S2` | `Normal` or `Short` | `16` or `32` |
| `S2X` | `Normal` | `8`, `16`, `32`, `64`, or `256` |
| `Short` | `16` or `32` |
| `SH` | Not applicable | `16` |

### **Code identifier** — Code identifier `2/3` | character vector

Code identifier, specified as a character vector. The list of valid code identifier
values varies depending on the setting for **DVB
standard suffix**, **Frame
length**, and **Modulation order**. This table lists the available options
for **Code identifier** values.

| **Modulation order** | **DVB standard suffix** | **Frame length** | **Code identifier** Options |
| --- | --- | --- | --- |
| `8` | `S2X` | `Normal` | `100/180` or `104/180` |
| `16` | `S2` or `S2X` | `Normal` | `2/3`, `3/4`, `4/5`, `5/6`, `8/9`, or `9/10` |
| `Short` | `2/3`, `3/4`, `4/5`, `5/6`, or `8/9` |
| `16` | `S2X` | `Normal` | `26/45`, `3/5`, `28/45`, `23/36`, `25/36`, `13/18`, `140/180`, `154/180`, `100/180`, `96/180`, `90/180`, `18/30`, or `20/30` |
| `Short` | `7/15`, `8/16`, `26/45`, `3/5`, or `32/45` |
| `32` | `S2` or `S2X` | `Normal` | `3/4`, `4/5`, `5/6`, `8/9`, or `9/10` |
| `Short` | `3/4`, `4/5`, `5/6`, or `8/9` |
| `32` | `S2X` | `Normal` | `128/180`, `132/180`, `140/180`, or `2/3` |
| `Short` | `2/3` or `32/45` |
| `64` | `S2X` | `Normal` | `128/180` , `132/180`, `7/9`, `4/5`, or `5/6` |
| `128` | `S2X` | `Normal` | `135/180` or `140/180` |
| 256 | `S2X` | `Normal` | `116/180`, `124/180`, `128/180`, `20/30`, or `135/180` |

For more information, refer to Tables 9 and 10 in the DVB-S2
standard [1] and Table 17a in
the DVB-S2X standard [2].

#### Dependencies

This parameter applies only when **DVB standard
suffix** is set to `S2` or
`S2X`.

### **Constellation scaling** — Constellation scaling `Outer radius as 1` (default) | `Unit average power`

Constellation scaling, specified as `Outer radius as
1` or `Unit average power`.

#### Dependencies

This input argument applies only when **DVB standard
suffix** is set to `S2` or
`S2X`.

### **Output type** — Output type `Integer` (default) | `Bit`

Output type, specified as `Integer` or
`Bit`.

### **Decision type** — Demodulation decision type `Hard decision` (default) | `Log-likelihood ratio` | `Approximate log-likelihood ratio`

Demodulation decision type, specified as `Hard
decision`, `Log-likelihood ratio`,
or `Approximate log-likelihood ratio`. See DVB Compliant APSK Soft Demodulation for algorithm
selection considerations.

#### Dependencies

This parameter applies when **Output type** is set to
`Bit`.

### **Noise variance source** — Noise variance source `Property` (default) | `Input port`

Noise variance source, specified as:

- `Property` — The noise variance is
  set using the **Noise variance** parameter.
- `Input port` — The noise variance is
  set using the **Var** input port.

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
extreme positive or negative magnitudes, see DVB Compliant APSK Soft Demodulation for demodulation
decision type considerations.

#### Dependencies

This parameter applies when **Noise variance source** is set to
`Property` and **Decision type** is set to either
`Log-likelihood ratio` or
`Approximate log-likelihood ratio`.

### **Output data type** — Output data type `double` (default) | `...`

Output data type, specified as one of the acceptable values from this
table. Acceptable **Output data type** values depend on the
**Output
type** and **Decision
type** parameter values.

| **Output type** | **Decision type** | **Output data type** Options |
| --- | --- | --- |
| `Integer` | Not applicable | `double`, `single`, `int8`, `uint8`, `int16`, `uint16`, `int32`, or `uint32` |
| `Bit` | `Hard decision` | `double`, `single`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `uint32`, or `logical` |
| `Log-likelihood ratio` or `Approximate log-likelihood ratio` | The output signal is the same data type as the input signal. |

#### Dependencies

This parameter applies only when **Output
type** is set to `Integer` or
when **Output
type** is set to `Bit` and
**Decision
type** is set to `Hard
decision`.

### **Simulate using** — Type of simulation to run `Code generation` (default) | `Interpreted execution`

Type of simulation to run, specified as `Code
generation` or `Interpreted
execution`.

- `Code generation` — Simulate the
  model by using generated C code. The first time you run a
  simulation, Simulink generates C code for the block. The model reuses
  the C code for subsequent simulations unless the model changes.
  This option requires additional startup time, but the speed of
  the subsequent simulations is faster than with the
  `Interpreted execution`
  option.
- `Interpreted execution` — Simulate
  the model by using the MATLAB® interpreter. This option shortens startup time,
  but the speed of subsequent simulations is slower than with the
  `Code generation` option. In this
  mode, you can debug the source code of the block.

## Libraries

Satellite Communications Toolbox / Modulation / Digital Baseband Modulation

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

### R2024b: Moved to Satellite Communications Toolbox from Communications Toolbox

Previously, `DVBS-APSK Demodulator Baseband` required Communications Toolbox™.

## Description

DVB-S2/S2X/SH standard-specific APSK demodulation

The DVBS-APSK Demodulator Baseband block demodulates the input signal using Digital Video Broadcasting (DVB-S2/S2X/SH) standard-specific amplitude
phase shift keying (APSK) demodulation.

This icon shows the block with all ports enabled: DVBS-APSK demodulator baseband block icon with all port enabled
