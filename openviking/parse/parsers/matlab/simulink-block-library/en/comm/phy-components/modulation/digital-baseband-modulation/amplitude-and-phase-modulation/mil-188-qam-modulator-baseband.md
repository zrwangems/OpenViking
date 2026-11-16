---
type: simulink-block
title: 'MIL-188 QAM Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Amplitude and Phase Modulation'
documentation_page: 'mil188qammodulatorbaseband'
documentation_source_path: 'ref/mil188qammodulatorbaseband.html'
language: en
---

# MIL-188 QAM Modulator Baseband

## Ports

### Input

### **In** — Input signal scalar | vector | matrix

Input signal, specified as a scalar, vector, or matrix. The input
signal must be binary values or integers in the range [0,
(*M* – 1)], where *M* is the
**Modulation order**. This port is unnamed on the block.

**Note**

To process the input signal as binary elements, set the
**Input type** parameter value to
`Bit`. For binary inputs, the
number of rows must be an integer multiple of
log2(*M*). Groups of
log2(*M*) bits in a
column are mapped onto a symbol, with the first bit representing
the MSB and the last bit representing the LSB.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Out** — MIL-STD-188 standard-specific QAM modulated signal scalar | vector | matrix

MIL-STD-188 standard-specific QAM modulated signal, returned as a
complex scalar, vector, or matrix. The output signal dimensions depend
on the specified **Input
type** parameter value. This port is unnamed on the
block.

| **Input type** | Dimensions of Output Signal |
| --- | --- |
| `Integer` | The output signal has the same dimensions as the input signal. |
| `Bit` | The number of rows in the output signal equals the number of rows in the input signal divided by log2(*M*), where *M* is the **Modulation order**. |

Use **Output
data type** to specify the output data type.

**Data Types:** `double` | `single`

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
of the output signal.

### **Constellation scaling** — Constellation scaling `As specified in standard` (default) | `Unit average power`

Constellation scaling, specified as:

- `As specified in standard` – The
  block scales the constellation based on specifications in the
  relevant standard [1].
- `Unit average power` – The block
  scales the constellation to an average power of 1 watt
  referenced to 1 ohm.

### **Input type** — Input type `Integer` (default) | `Bit`

Input type, specified as `Integer` or
`Bit`. To use
`Integer`, the input signal must consist of
integers in the range [0, (*M* – 1)]. To use `Bit`, the input signal
must contain binary values, and the number of rows must be an integer
multiple of log2(*M*), where *M* is the **Modulation
order**.

### **Output data type** — Output data type `double` (default) | `single`

Output data type, specified as `double` or
`single`.

### **View Constellation** — Plot reference constellation `button`

To plot the reference constellation, click the **View
Constellation** button.

### **Simulate using** — Type of simulation to run `Code generation` (default) | `Interpreted execution`

Type of simulation to run, specified as:

- `Code generation` –– Simulate the
  model using generated C code. The first time you run a
  simulation, Simulink generates C code for the block. The C code is
  reused for subsequent simulations as long as the model does not
  change. This option requires additional startup time, but the
  speed of the subsequent simulations is comparable to
  `Interpreted execution`.
- `Interpreted execution` –– Simulate
  the model using the MATLAB® interpreter. This option shortens startup time and
  has a simulation speed comparable to `Code
  generation`. In `Interpreted
  execution` mode, you can debug the source code
  of the block.

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

MIL-STD-188-110 B/C standard-specific quadrature amplitude modulation (QAM)

The MIL-188 QAM Modulator Baseband block modulates the input signal using MIL-STD-188-110 standard-specific
quadrature amplitude modulation (QAM).
