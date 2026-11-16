---
type: simulink-block
title: 'M-FSK Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Frequency Modulation'
documentation_page: 'mfskdemodulatorbaseband'
documentation_source_path: 'ref/mfskdemodulatorbaseband.html'
language: en
---

# M-FSK Demodulator Baseband

## Ports

### Input

### **In** — Input signal scalar

Input signal, specified as a scalar. The input is a baseband
representation of the modulated signal.

This port is unnamed on the block.

**Data Types:** `double`
### Output

### **Out** — Demodulated output signal scalar | column vector

Demodulated output signal, returned as a scalar or column vector. For
more information, see Single-Rate Processing and Multirate Processing. The **Output
type** parameter specifies whether the block outputs
integers or groups of bits.

This port is unnamed on the block.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **M-ary number** — Number of frequencies in modulated signal `8` (default) | positive integer ≥ 2

Number of frequencies in the modulated signal, specified as a positive
integer ≥ 2.

### **Output type** — Integer or group of bits output indicator `Integer` (default) | `Bit`

Indicates whether the block outputs integers or groups of bits, specified
as `Integer` or
`Bit`.

If you set this parameter to `Bit`, then the
**M-ary
number** parameter must be
2*K* for some positive
integer *K*.

### **Symbol set ordering** — Symbol mapping `Binary` (default) | `Gray`

Symbol mapping of output symbols, specified as
`Binary` or `Gray`.

- Set this parameter to `Binary` to map
  symbols using binary-coded ordering.
- Set this parameter to `Gray` to map
  symbols using Gray-coded ordering. For Gray-coded ordering, the
  **M-ary number** value must be a power of
  two.

For more information, see Integer-Valued Signals and Binary-Valued Signals.

### **Frequency separation (Hz)** — Frequency separation in Hz `6` (default) | positive scalar

Frequency separation in Hz, specified as a positive scalar representing
the distance between successive frequencies in the modulated signal.

### **Samples per symbol** — Symbol sampling rate `17` (default) | positive integer

Symbol sampling rate, specified as a positive integer indicating the
number of input samples that represent each modulated symbol.

For more information, see Signal Upsampling and Rate Changes.

### **Rate options** — Block processing rate `Enforce single-rate processing` (default) | `Allow multirate processing`

Block processing rate, specified as one of these options:

- `Enforce single-rate processing` — The input and
  output signals have the same port sample time. The block implements the rate
  change by making a size change at the output when compared to the input. The
  output width is the number of symbols (which is given by dividing the input
  length by the **Samples per symbol** parameter value when
  the **Output type** parameter is set to
  `Integer`).
- `Allow multirate processing` — The input and
  output signals have different port sample times. The output period is the
  same as the symbol period and equals the product of the input period and the
  **Samples per symbol** parameter value.

### **Output data type** — Output data type `double` (default) | `boolean` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

Output data type, specified as `double`,
`boolean`, `int8`,
`uint8`, `int16`,
`uint16`, `int32`, or
`uint32`.

## Libraries

Communications Toolbox / Modulation / Digital Baseband Modulation / FM

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Demodulate FSK-modulated data

The M-FSK Demodulator Baseband block demodulates a signal that was modulated using the
M-ary frequency shift keying (M-FSK) method. The input and output are discrete-time
signals.
