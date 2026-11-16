---
type: simulink-block
title: 'CPFSK Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Continuous Phase Modulation'
documentation_page: 'cpfskdemodulatorbaseband'
documentation_source_path: 'ref/cpfskdemodulatorbaseband.html'
language: en
---

# CPFSK Demodulator Baseband

## Ports

Not documented in R2025b.

## Parameters

**M-ary number**
:   The size of the alphabet.

**Output type**
:   Determines whether the output consists of integers or groups of
    bits.

**Symbol set ordering**
:   Determines how the block maps each integer to a group of output bits. This
    field is active only when **Output type** is set to
    `Bit`.

**Modulation index**
:   Specify the modulation index {hi}. The default is
    `0.5`. The value of this property must be a real,
    nonnegative scalar or column vector.

    This block supports multi-h **Modulation index**. See
    CPM Modulator Baseband for
    details.

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
:   The number of trellis branches that the CPFSK Demodulator Baseband block
    uses to construct each traceback path.

**Output datatype**
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

Demodulate CPFSK-modulated data

The CPFSK Demodulator Baseband block demodulates a signal that was modulated using the
continuous phase frequency shift keying method. The input to this block is a baseband
representation of the modulated signal. The **M-ary number** parameter,
*M*, is the size of the input alphabet. *M* must
have the form 2*K* for some positive integer
*K*.

This block supports multi-h **Modulation index**. See CPM
Modulator Baseband for details.

### Integer-Valued Signals and Binary-Valued Signals

When you set the **Output type** parameter to
`Integer`, then the block produces odd integers between
-(M-1) and M-1.

When you set the **Output type** parameter to
`Bit`, then the block produces groupings of
*K* bits. Each grouping is called a binary
*word*.

In binary output mode, the block first maps each input symbol to an intermediate
value as in the integer output mode. The block then maps the odd integer k to the
nonnegative integer (k+M-1)/2. Finally, the block maps each nonnegative integer to a
binary word, using a mapping that depends on whether the **Symbol set
ordering** parameter is set to `Binary` or
`Gray`.

This block accepts a scalar-valued or column vector input signal with a data type
of `single` or `double`.

### Single-Rate Processing

In single-rate processing mode, the input and output signals have the same port
sample time. The block implicitly implements the rate change by making a size change
at the output when compared to the input. The input width must be an integer
multiple of the **Samples per symbol** parameter value, and the
input can be a column vector.

- When you set **Output type** to
  `Bit`, the output width is *K*
  times the number of input symbols.
- When you set **Output type** to
  `Integer`, the output width is the number of
  input symbols.

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
uses the Viterbi algorithm. The **Traceback depth** parameter,
*D*, in this block is the number of trellis branches that the
algorithm uses to construct each traceback path. *D* influences the
output delay, which is the number of zero symbols that precede the first meaningful
demodulated value in the output.

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
“five-times-the-constraint-length” rule, which corresponds to
5·log2(*numStates*).

For the definition of the number of states, see CPM Demodulator Baseband Help page.
