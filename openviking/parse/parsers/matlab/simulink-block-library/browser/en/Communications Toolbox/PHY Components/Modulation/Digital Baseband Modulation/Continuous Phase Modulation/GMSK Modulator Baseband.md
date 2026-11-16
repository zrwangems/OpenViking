---
type: simulink-block
title: 'GMSK Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Continuous Phase Modulation'
documentation_page: 'gmskmodulatorbaseband'
documentation_source_path: 'ref/gmskmodulatorbaseband.html'
language: en
---

# GMSK Modulator Baseband

## Ports

Not documented in R2025b.

## Parameters

**Input type**
:   Indicates whether the input consists of bipolar or binary values.

**BT product**
:   The product of bandwidth and time.

    The block uses this parameter to reduce bandwidth at the expense of
    increased intersymbol interference. Enter a nonnegative scalar value for
    this parameter.

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
:   The initial phase of the output waveform, measured in radians.

**Samples per symbol**
:   The number of output samples that the block produces for each integer or
    bit in the input, which must be a positive integer. For all non-binary
    schemes, as defined by the pulse shapes, this value must be greater than
    1.

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
:   The output type of the block can be specified as a
    `single` or `double`. By default, the
    block sets this to `double`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Modulate using Gaussian minimum shift keying method

The GMSK Modulator Baseband block modulates using the Gaussian minimum shift keying
method. The output is a baseband representation of the modulated signal.

The **BT product** parameter represents bandwidth multiplied by time.
This parameter is a nonnegative scalar. It is used to reduce the bandwidth at the
expense of increased intersymbol interference. The **Pulse length**
parameter measures the length of the Gaussian pulse shape, in symbol intervals. For an
explanation of the pulse shape, see the work by Anderson, Aulin, and Sundberg among the
references listed below. The
frequency pulse shape is defined by the following equations.

g(t)=12T{Q[2πBbt−T2ln(2)]−Q[2πBbt+T2ln(2)]}Q(t)=∫t∞12πe−τ2/2dτ

For this block, an input symbol of 1 causes a phase shift of π/2 radians.

The group delay is the number of samples between the start of a filter's response and
its peak. The group delay that the block introduces is **Pulse
length**/2 \* **Samples per symbol** (using a reference of
output sample periods). For GMSK, **Pulse length** denotes the
truncated frequency pulse length in symbols. The net delay effect at the receiver
(demodulator) is due to the **Traceback depth** parameter, which in
most cases would be larger than the group delay.

### Integer-Valued Signals and Binary-Valued Signals

When you set the **Input type** parameter to
`Integer`, then the block accepts values of 1 and -1.

When you set the **Input type** parameter to
`Bit`, then the block accepts values of 0 and 1.

This block accepts a scalar-valued or column vector input signal. For a column
vector input signal, the width of the output equals the product of the number of
symbols and the value for the **Samples per symbol** parameter.

### Single-Rate Processing

In single-rate processing mode, the input and output signals have the same port
sample time. The block implicitly implements the rate change by making a size change
at the output when compared to the input. In this mode, the input to the block can
be multiple symbols.

- When you set **Input type** to
  `Integer`, the input can be a column vector,
  the length of which is the number of input symbols.
- When you set **Input type** to
  `Bit`, the input width must be an integer
  multiple of 2.

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
