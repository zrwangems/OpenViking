---
type: simulink-block
title: 'CPM Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Continuous Phase Modulation'
documentation_page: 'cpmdemodulatorbaseband'
documentation_source_path: 'ref/cpmdemodulatorbaseband.html'
language: en
---

# CPM Demodulator Baseband

## Ports

### Input

### **In** — Input signal scalar | column vector

Input signal, specified as a scalar or column vector. The length of the input signal
must be an integer multiple of the number of samples per symbol specified in the
**Samples per symbol** parameter. For more information, see Integer-Valued and Binary-Valued Output Signals.

**Data Types:** `double` | `single`
### Output

### **Out** — Output signal scalar | column vector

Output signal, returned as a scalar or column vector. For more information, see Integer-Valued and Binary-Valued Output Signals.

#### Supported Data Types

- Double-precision floating point
- Boolean (when **Output type** is set to
  `Bit`)
- 8-, 16-, and 32-bit signed integers (when **Output type** is set to
  `Integer`)

**Data Types:** `double` | `Boolean` | `int8` | `int16` | `int32`

For more information on the processing rates, see Single-Rate Processing, and Multirate Processing.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **M-ary number** — Modulation order `4` (default) | positive integer

Modulation order indicating the alphabet size, specified as a positive integer that is a
nonzero power of two. *M* must have the form 2*K* for some positive integer
*K*, where *K* is the number of bits per symbol.

### **Output type** — Determines whether output consists of integers or groups of bits `Integer` (default) | `Bit`

Determines whether the output consists of integers or groups of bits, specified as
`Integer` or `Bit`.

### **Symbol set ordering** — Bit mapping `Binary` (default) | `Gray`

Bit mapping, specified as `Binary` or
`Gray`.

- Set this parameter to `Binary` to map symbols using
  binary-coded ordering.
- Set this parameter to `Gray` to map symbols using Gray-coded
  ordering.

For more information, see Integer-Valued and Binary-Valued Output Signals.

#### Dependencies

To enable this parameter, set **Output type** to
`Bit`.

### **Modulation index** — Modulation index {*h*i} `0.5` (default) | nonnegative scalar | column vector

Modulation index {*h*i}, specified as a
nonnegative scalar or column vector.

{*h*} represents a sequence of modulation indices. For more information,
see CPM Demodulation.

### **Frequency pulse shape** — Type of pulse shaping `Rectangular` (default) | `Raised Cosine` | `Spectral Raised Cosine` | `Gaussian` | `Tamed FM`

Type of pulse shaping used to smooth the phase transitions of the modulated signal,
specified as `Rectangular`, `Raised Cosine`,
`Spectral Raised Cosine`, `Gaussian`, or
`Tamed FM`. For more information on the filtering options, see Pulse Shape Filtering.

### **Main lobe pulse duration (symbol intervals)** — Main lobe duration `1` (default) | positive integer

Main lobe duration of the largest lobe in the spectral raised cosine pulse, specified as
a positive integer representing the number of symbol intervals used by the demodulator to
pulse-shape the modulated signal.

#### Dependencies

To enable this parameter, set **Frequency pulse shape** to
`Spectral Raised Cosine`.

### **Rolloff** — Rolloff factor of spectral raised cosine pulse shape `0.2` (default) | scalar in the range [0, 1]

Rolloff factor of the spectral raised cosine pulse, specified as a scalar in the range
[0, 1].

#### Dependencies

To enable this parameter, set **Frequency pulse shape** to
`Spectral Raised Cosine`.

### **BT product** — Product of bandwidth and symbol time of Gaussian pulse `0.3` (default) | positive scalar

Product of the bandwidth and symbol time of the Gaussian pulse shape, specified as a
positive scalar. Use **BT product** to reduce the bandwidth, at the expense
of increased intersymbol interference.

#### Dependencies

To enable this parameter, set **Frequency pulse shape** to
`Gaussian`.

### **Pulse length (symbol intervals)** — Length of frequency pulse shape `1` (default) | positive integer

Frequency pulse shape length, specified as a positive scalar. For more information on the
frequency pulse length, refer to *LT* in Pulse Shape Filtering.

### **Symbol prehistory** — Data symbols used before the start of simulation `1` (default) | scalar | vector

Data symbols used before the start of simulation, specified as scalar or vector with odd
integer elements in the range [– (*M* – 1), (*M* – 1)].
*M* represents the modulation order, which is specified by the **M-ary number** parameter. The **Symbol prehistory** parameter
defines the data symbols used by the modulator prior to the first call of the block, in
reverse chronological order.

- A scalar value expands to a vector of length *L*P – 1. *L*P represents the pulse
  length, which is specified by the **Pulse length (symbol intervals)**
  parameter.
- For a vector, the length must be *L*P – 1.

### **Phase offset (rad)** — Initial phase offset `0` (default) | scalar

Initial phase offset in radians of the modulated waveform, specified as a scalar.

### **Samples per symbol** — Symbol sampling rate `8` (default) | positive scalar

Symbol sampling rate, specified as a positive scalar. This parameter represents the
number of samples output for each integer or binary word input. For all nonbinary schemes, as
defined by the pulse shapes, this value must be greater than 1.

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

### **Traceback depth** — Traceback depth for Viterbi algorithm `16` (default) | positive integer

Traceback depth for the Viterbi algorithm, specified as a positive integer representing
the number of trellis branches that the Viterbi algorithm uses to construct each traceback
path. The value of this parameter is also the output delay and the number of zero symbols that
precede the first meaningful demodulated symbol in the output. For more information, see Traceback Depth and Output Delays.

### **Output data type** — Output data type `double` (default) | `boolean` | `int8` | `int16` | `int32`

Output data type, specified as `double`,
`boolean`, `int8`,
`int16`, or `int32`. For more information,
see **Supported Data Types** in `Out`.

## Libraries

Communications Toolbox / Modulation / Digital Baseband Modulation / CPM

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

Demodulate signal using CPM method and Viterbi algorithm

The CPM Demodulator Baseband block demodulates an input signal that was modulated using the continuous
phase modulation (CPM) method.

CPM is a modulation method with memory. The block processing includes a correlator followed
by a maximum-likelihood sequence detector (MLSD) that searches the paths through the state
trellis for the minimum Euclidean distance path. The block uses the Viterbi algorithm to perform
MLSD.

For more information about this demodulation and the filtering applied, see CPM Demodulation and Pulse Shape Filtering.
