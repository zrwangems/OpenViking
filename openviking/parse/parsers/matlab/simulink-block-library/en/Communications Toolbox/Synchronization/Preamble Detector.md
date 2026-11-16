---
type: simulink-block
title: 'Preamble Detector'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Synchronization'
documentation_page: 'preambledetector'
documentation_source_path: 'ref/preambledetector.html'
language: en
---

# Preamble Detector

## Ports

### Input

### **In** — Input data [ ] | scalar | column vector

Input data of symbols or bits, specified as a scalar, a column vector,
or it can be empty. The input data can contain multiple packets. This
port is unnamed on the block.

**Data Types:** `single` | `double` | `Boolean` | `int8` | `uint8`
**Complex Number Support:** Yes
### Output

### **Idx** — Index of last preamble symbol [ ] | scalar | column vector

Index of the last preamble symbol, returned as a scalar or a column
vector, or empty of the same data type as the input data.

- When the **Detections** parameter is set to
  `All`, `Idx` outputs
  the index corresponding to the last element of each detected
  preamble.
- When the **Detections** parameter is set to
  `First`, `Idx`
  outputs the index corresponding to the last element of the
  first detected preamble.

This port is unnamed until the `DtMt`
port is enabled.

### **DtMt** — Detection metric scalar | column vector

Detection metric, returned as a scalar or column vector of the same
dimensions and data type as the input data packet, `In`.

- If either the preamble or input data is complex, the detection
  metric is the absolute value of the cross-correlation of the
  preamble and the input data.
- If both the preamble and input data are real, the detection
  metric is the cross-correlation of the preamble and the input
  data.

#### Dependencies

To enable this port, set the **Input** parameter
to `Symbol`, and select the **Output
detection metric** parameter.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Input** — Input type `Symbol` (default) | `Bit`

Input type, specified as `Symbol` or
`Bit`.

- For binary inputs, set this parameter to
  `Bit`.
- For all other inputs, set this parameter to
  `Symbol`.

For information on execution speed, see Tips.

### **Preamble** — Preamble sequence `[1 + 1i; 1 - 1i]` (default) | column vector

Preamble sequence, specified as a column vector.

- If the **Input** parameter is set to
  `Bit`, the preamble must be
  binary.
- If the **Input** parameter is set to
  `Symbol`, the preamble can be any
  real or complex sequence.

### **Detection threshold** — Detection threshold `3` (default) | nonnegative scalar

Detection threshold, specified as a nonnegative scalar. When the detection
metric is greater than or equal to the threshold, the block detects the
preamble and updates `Idx`.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Input** parameter to
`Symbol`.

### **Output detection metric** — Option to output detection metric `off` (default) | `on`

Select this parameter to output the detection metric and enable the
`DtMt` output port.

#### Dependencies

To enable this parameter, set the **Input** parameter to
`Symbol`.

### **Detections** — Detections returned `All` (default) | `First`

Detections returned, specified as `All` or
`First`. Specifying
`All` returns all detected preambles.
Specifying `First` returns only the first detected
preamble.

**Tunable:** Yes

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
| **Data Types** | `Boolean` | `double` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

## Description

Detect preamble in data packet

The Preamble Detector block detects the end of preambles in data packets. A preamble is a
set of symbols or bits used in packet-based communications systems to indicate the start
of a packet. Packets consist of preamble data and user data. The length of the user data
portion of the packet can vary during a simulation run.

This icon shows the block with all ports enabled:
