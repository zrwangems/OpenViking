---
type: simulink-block
title: 'CPFSK Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Continuous Phase Modulation'
documentation_page: 'cpfskmodulatorbaseband'
documentation_source_path: 'ref/cpfskmodulatorbaseband.html'
language: en
---

# CPFSK Modulator Baseband

## Ports

Not documented in R2025b.

## Parameters

**M-ary number**
:   The size of the alphabet.

**Input type**
:   Indicates whether the input consists of integers or groups of bits.

**Symbol set ordering**
:   Determines how the block maps each group of input bits to a corresponding
    integer. This field is active only when **Input type** is
    set to `Bit`.

**Modulation index**
:   Specify the modulation index {hi}. The default is
    `0.5`. The value of this property must be a real,
    nonnegative scalar or column vector.

    This block supports multi-h **Modulation index**. See
    CPM Modulator Baseband for
    details.

**Phase offset (rad)**
:   The initial phase of the output waveform, measured in radians.

**Samples per symbol**
:   The number of output samples that the block produces for each integer or
    binary word in the input, which must be a positive integer. For all
    non-binary schemes, as defined by the pulse shapes, this value must be
    greater than 1.

    For more information, see Signal Upsampling and Rate Changes.

**Rate options**
:   Select the rate processing option for the block.

    - `Enforce single-rate processing` —
      When you select this option, the input and output signals have the
      same port sample time. The block implements the rate change by making
      a size change at the output when compared to the input. The output
      width equals the product of the number of symbols and the **Samples
      per symbol** parameter value.
    - `Allow multirate processing` —
      When you select this option, the input and output signals have different
      port sample times. The output sample time equals the symbol period
      divided by the **Samples per symbol** parameter value.

**Output data type**
:   Select the data type of the output signal. The output data type can be
    `single` or `double`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Modulate using continuous phase frequency shift keying method

The CPFSK Modulator Baseband block modulates a signal using the continuous phase
frequency shift keying method. The output is a baseband representation of the modulated
signal. The **M-ary number** parameter, *M*,
represents the size of the input alphabet. *M* must have the form
2*K* for some positive integer
*K*.

This block supports multi-h **Modulation index**. See CPM
Modulator Baseband for details.

### Integer-Valued Signals and Binary-Valued Signals

When you set the **Input type** parameter to
`Integer`, the block accepts odd integers between
-(M-1) and M-1.

When you set the **Input type** parameter to
`Bit`, the block accepts groupings of
*K* bits. Each grouping is called a binary
*word*. The input vector length must be an integer multiple
of *K*.

In binary input mode, the block maps each binary word to an integer between 0 and
M-1, using a mapping scheme that depends on whether you set the **Symbol set
ordering** parameter to `Binary` or
`Gray`. The block then maps the integer
*k* to the intermediate value 2k-(M-1) and proceeds as if it
operates in the integer input mode. For more information, see Integer-Valued and Binary-Valued Symbols.

This block accepts a scalar-valued or column vector input signal. If you set
**Input type** to `Bit`, then the
input signal can also be a vector of length *K*.

### Single-Rate Processing

In single-rate processing mode, the input and output signals have the same port
sample time. The block implicitly implements the rate change by making a size change
at the output when compared to the input. In this mode, the input to the block can
be multiple symbols.

- When you set **Input type** to
  `Integer`, the input can be a column vector,
  the length of which is the number of input symbols.
- When you set **Input type** to
  `Bit`, the input must be a column vector with a
  width that is an integer multiple of *K*, the number of
  bits per symbol.

The output width equals the product of the number of input symbols and the
**Samples per symbol** parameter value.

### Multirate Processing

In multirate processing mode, the input and output signals have different port
sample times. In this mode, the input to the block must be one symbol.

- When you set **Input type** to
  `Integer`, the input must be a scalar.
- When you set **Input type** to
  `Bit`, the input width must equal the number of
  bits per symbol.

The output sample time equals the symbol period divided by the **Samples
per symbol** parameter value.
