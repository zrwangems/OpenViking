---
type: simulink-block
title: 'GMSK Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Continuous Phase Modulation'
documentation_page: 'gmskdemodulatorbaseband'
documentation_source_path: 'ref/gmskdemodulatorbaseband.html'
language: en
---

# GMSK Demodulator Baseband

## Ports

Not documented in R2025b.

## Parameters

**Output type**
:   Determines whether the output consists of bipolar or binary values.

**BT product**
:   The product of bandwidth and time.

**Pulse length (symbol intervals)**
:   The length of the frequency pulse shape.

**Symbol prehistory**
:   A scalar or vector value that specifies the data symbols the block uses
    before the start of the simulation, in reverse chronological order.

    - A scalar value expands to a vector of length *L*P –
      1. *L*P
      represents the pulse length, which is specified by the
      **Pulse length (symbol intervals)**
      parameter.
    - For a vector, the length must be *L*P –
      1.

**Phase offset (rad)**
:   The initial phase of the modulated waveform.

**Samples per symbol**
:   The number of input samples that represent each modulated symbol, which
    must be a positive integer. For more information, see Signal Upsampling and Rate Changes in
    *Communications Toolbox™ User's Guide*.

**Rate options**
:   Select the rate processing method for the block.

    - `Enforce single-rate processing` —
      When you select this option, the input and output signals have the
      same port sample time. The block implements the rate change by making
      a size change at the output when compared to the input. The output
      width is the number of symbols (which is given by dividing the input
      length by the **Samples per symbol** parameter value
      when the **Output type** parameter is set to `Integer`).
    - `Allow multirate processing` —
      When you select this option, the input and output signals have different
      port sample times. The output period is the same as the symbol period
      and equals the product of the input period and the **Samples
      per symbol** parameter value.

    For more information, see Single-Rate Processing and Multirate
    Processing in the Description section of this page.

**Traceback depth**
:   The number of trellis branches that the GMSK Demodulator Baseband block
    uses to construct each traceback path.

**Output data type**
:   The output data type can be `boolean`,
    `int8`, `int16`,
    `int32`, or `double`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Demodulate GMSK-modulated data

The GMSK Demodulator Baseband block uses a Viterbi algorithm to demodulate a signal
that was modulated using the Gaussian minimum shift keying method. The input to this
block is a baseband representation of the modulated signal.

### Integer-Valued Signals and Binary-Valued Signals

This block accepts a scalar-valued or column vector input signal with a data type
of `single` or `double`. If you set the
**Output type** parameter to
`Integer`, then the block produces values of 1 and -1. If
you set the **Output type** parameter to
`Bit`, then the block produces values of 0 and
1.

### Single-Rate Processing

In single-rate processing mode, the input and output signals have the same port
sample time. The block implicitly implements the rate change by making a size change
at the output when compared to the input. The input width must be an integer
multiple of the **Samples per symbol** parameter value, and the
input can be a column vector.

- When you set **Output type** to
  `Bit`, the output width is two times the number
  of input symbols.
- When you set **Output type** to
  `Integer`, the output width is the number of
  input symbols.

For a column vector input signal, the width of the input equals the product of the
number of symbols and the value for the **Samples per symbol**
parameter.

### Multirate Processing

In multirate processing mode, the input and output signals have different port
sample times. The input must be a scalar. The output symbol time is the product of
the input sample time and the **Samples per symbol** parameter
value.

- When you set **Output type** to
  `Bit`, the output width equals the number of
  bits per symbol.
- When you set **Output type** to
  `Integer`, the output is a scalar.

### Traceback Depth and Output Delays

Internally, this block creates a trellis description of the modulation scheme and
uses the Viterbi algorithm. The **Traceback depth** parameter, D,
in this block is the number of trellis branches used to construct each traceback
path. D influences the output delay, which is the number of zero symbols that
precede the first meaningful demodulated value in the output.

- When you set the **Rate options** parameter to
  `Allow multirate processing`, and the model
  uses a variable-step solver or a fixed-step solver with the
  **Tasking Mode** parameter set to
  `SingleTasking`, then the delay consists of D+1
  zero symbols.
- When you set the **Rate options** parameter to
  `Enforce single-rate processing`, then the
  delay consists of D zero symbols.

The optimal **Traceback depth** parameter value is dependent on
minimum squared Euclidean distance calculations. Alternatively, a typical value,
dependent on the number of states, can be chosen using the
*five-times-the-constraint-length* rule, which corresponds
to 5log2(*numStates*. The number of states is determined by the following
equation:

numStates={p⋅2(L−1), for even m2p⋅2(L−1), for odd m}

where:

- *h* = *m*/*p* is the
  modulation index in proper rational form

  - *m* = numerator of modulation index
  - *p* = denominator of modulation index
- *L* is the Pulse length
