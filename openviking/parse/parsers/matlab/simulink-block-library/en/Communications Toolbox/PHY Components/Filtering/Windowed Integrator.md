---
type: simulink-block
title: 'Windowed Integrator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Filtering'
documentation_page: 'windowedintegrator'
documentation_source_path: 'ref/windowedintegrator.html'
language: en
---

# Windowed Integrator

## Ports

Not documented in R2025b.

## Parameters

**Integration period**
:   The length of the interval of integration, measured in samples.

**Input processing**
:   Specify how the block processes the input signal. You can set
    this parameter to one of the following options:

    - `Columns as channels (frame based)` —
      When you select this option, the block treats each column of the input
      as a separate channel.
    - `Elements as channels (sample based)` —
      When you select this option, the block treats each element of the
      input as a separate channel.

**Rounding mode**
:   Select the rounding mode for fixed-point operations. The block uses the
    **Rounding mode** when the result of a fixed-point
    calculation does not map exactly to a number representable by the data type
    and scaling storing the result. The filter coefficients do not obey this
    parameter; they always round to `Nearest`. For more
    information, see Rounding Modes or Rounding Mode: Simplest (Fixed-Point Designer).

**Saturate on integer overflow**
:   Select the overflow mode for fixed-point operations. The filter
    coefficients do not obey this parameter; they are always saturated.

**Coefficients**
:   The block implementation uses a direct-form FIR filter with all tap
    weights set to one. The **Coefficients** parameter controls
    which data type represents the taps (i.e. ones) when the input data is a
    fixed-point signal.

    Choose how you specify the word length and the fraction length of the
    filter coefficients (numerator and/or denominator).

    - When you select `Same word length as
      input`, the word length of the filter
      coefficients match that of the input to the block. In this mode,
      the fraction length of the coefficients is automatically set to
      the binary-point only scaling that provides you with the best
      precision possible given the value and word length of the
      coefficients.
    - When you select `Specify word
      length`, you are able to enter the word length of
      the coefficients, in bits. In this mode, the fraction length of
      the coefficients is automatically set to the binary-point only
      scaling that provides you with the best precision possible given
      the value and word length of the coefficients.
    - When you select `Binary point
      scaling`, you are able to enter the word length
      and the fraction length of the coefficients, in bits. If
      applicable, you are able to enter separate fraction lengths for
      the numerator and denominator coefficients.
    - When you select `Slope and bias
      scaling`, you are able to enter the word
      length, in bits, and the slope of the coefficients. If
      applicable, you are able to enter separate slopes for the
      numerator and denominator coefficients. This block requires
      power-of-two slope and a bias of zero.
    - The filter coefficients do not obey the **Rounding
      mode** and the **Saturate on integer
      overflow** parameters; they are always saturated
      and rounded to `Nearest`.

    For more information and illustrations depicting the use of the
    coefficient data types in this block, see the filter structure diagrams for
    the Discrete FIR Filter (Simulink)
    block.

**Product output**
:   Use this parameter to specify how you would like to designate the product
    output word and fraction lengths.

    - When you select `Same as input`,
      these characteristics match those of the input to the
      block.
    - When you select `Binary point
      scaling`, you are able to enter the word length
      and the fraction length of the product output, in bits.
    - When you select `Slope and bias
      scaling`, you are able to enter the word
      length, in bits, and the slope of the product output. This block
      requires power-of-two slope and a bias of zero.

    For more information and illustrations depicting the use of the product
    output data type in this block, see Discrete FIR Filter (Simulink) and Multiplication Data Types.

**Accumulator**
:   Use this parameter to specify how you would like to designate the
    accumulator word and fraction lengths.

    - When you select `Same as input`,
      these characteristics match those of the input to the
      block.
    - When you select `Same as product
      output`, these characteristics match those of
      the product output.
    - When you select `Binary point
      scaling`, you are able to enter the word length
      and the fraction length of the accumulator, in bits.
    - When you select `Slope and bias
      scaling`, you are able to enter the word
      length, in bits, and the slope of the accumulator. This block
      requires power-of-two slope and a bias of zero.

    For more information and illustrations depicting the use of the
    accumulator data type in this block, see Discrete FIR Filter (Simulink) and Multiplication Data Types.

**Output**
:   Choose how you specify the output word length and fraction length:

    - When you select `Same as input`, these
      characteristics match those of the input to the block.
    - When you select `Same as accumulator`,
      these characteristics match those of the accumulator.
    - When you select `Binary point scaling`,
      you are able to enter the word length and the fraction length of the
      output, in bits.
    - When you select `Slope and bias scaling`,
      you are able to enter the word length, in bits, and the slope of the
      output. This block requires power-of-two slope and a bias of
      zero.

**Lock scaling against changes by the autoscaling tool**
:   Select this parameter to prevent any fixed-point scaling you specify in
    this block mask from being overridden by the autoscaling tool in the
    Fixed-Point Tool.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Integrate over time window of fixed length

The Windowed Integrator block creates cumulative sums of the input signal values over
a sliding time window of fixed length. If the **Integration period**
parameter is N and the input samples are denoted by x(1), x(2), x(3),..., then the nth
output sample is the sum of the x(k) values for k between n-N+1 and n. In cases where
n-N+1 is less than 1, the block uses an initial condition of 0 to represent those
samples.

### Input and Output Signals

This block accepts scalar, column vector, and
*M*-by-*N* matrix input signals. The block
filters an *M*-by-*N* input matrix as follows:

- When you set the **Input processing** parameter to
  `Columns as channels (frame based)`, the
  block treats each column as a separate channel. In this mode, the block
  creates *N* instances of the same filter, each with its
  own independent state buffer. Each of the *N* filters
  process *M* input samples at every Simulink® time step.
- When you set the **Input processing** parameter to
  `Elements as channels (sample based)`, the
  block treats each element as a separate channel. In this mode, the block
  creates *M*\**N* instances of the same
  filter, each with its own independent state buffer. Each filter
  processes one input sample at every Simulink time step.

The output dimensions always equal those of the input signal. For information
about the data types each block port supports, see the Supported Data Type table on this page.
