---
type: simulink-block
title: 'M-FSK Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Frequency Modulation'
documentation_page: 'mfskmodulatorbaseband'
documentation_source_path: 'ref/mfskmodulatorbaseband.html'
language: en
---

# M-FSK Modulator Baseband

## Ports

### Input

### **In** — Input signal scalar | row vector

Input signal, specified as a scalar or column vector. For more
information, see **Input
type**.

This port is unnamed on the block.

**Data Types:** `double`
### Output

### **Out** — M-FSK-modulated signal scalar | column vector

M-FSK-modulated signal, returned as a scalar or column vector of
complex symbols. For more information, see Single-Rate Processing and Multirate Processing.

The output is a baseband representation of the modulated signal. The
**Output
data type** parameter specifies the desired output data
type.

This port is unnamed on the block.

**Data Types:** `double`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **M-ary number** — Number of frequencies in modulated signal `8` (default) | positive integer ≥ 2

Number of frequencies in the modulated signal, specified as a positive
integer ≥ 2.

### **Input type** — Integer or group of bits input indicator `Integer` (default) | `Bit`

Indicates whether the input consists of integers or groups of bits,
specified as `Integer` or
`Bit`.

If you set this parameter to `Bit`, then the
**M-ary
number** parameter must be
2*K* for some positive
integer *K*.

### **Symbol set ordering** — Symbol mapping `Binary` (default) | `Gray`

Symbol mapping of input symbols, specified as
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

### **Phase continuity** — Phase continuity `Continuous` (default) | `Discontinuous`

Phase continuity, specified as `Continuous` or
`Discontinuous` to determine whether the
modulated signal changes phases in a continuous or discontinuous way.

- If you set this parameter to
  `Continuous`, then the modulated signal
  maintains its phase even when it changes its frequency.
- If you set this parameter to
  `Discontinuous`, then the modulated
  signal comprises portions of *M* sinusoids of
  different frequencies. A change in the input value sometimes causes
  a change in the phase of the modulated signal. *M*
  is the **M-ary number** parameter value.

### **Samples per symbol** — Symbol sampling rate `17` (default) | positive integer

Symbol sampling rate, specified as a positive integer representing the
number of output samples that the block produces for each integer or binary
word in the input.

For more information, see Signal Upsampling and Rate Changes.

### **Rate options** — Block processing rate `Enforce single-rate processing` (default) | `Allow multirate processing`

Block processing rate, specified as one of these options:

- `Enforce single-rate processing` — The input and
  output signals have the same sample time. The block implements the rate
  change by making a size change at the output when compared to the input. The
  output width equals the product of the number of symbols and the
  **Samples per symbol** parameter value.
- `Allow multirate processing` — The input and
  output signals have different sample times. The output sample time equals
  the symbol period divided by the **Samples per symbol**
  parameter value.

### **Output data type** — Output data type `double` (default) | `single`

Output data type, specified as `double` or
`single`.

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

Modulate using M-ary frequency shift keying method

The M-FSK Modulator Baseband block modulates a signal using the M-ary frequency
shift keying (M-FSK) method.

To prevent aliasing in the output signal, set the sampling frequency to a value
greater than the product of the **M-ary
number** and the **Frequency separation
(Hz)** parameter values. The sampling frequency is the **Samples per
symbol** parameter value divided by the input symbol period (in seconds)
defined for the model.
