---
type: simulink-block
title: 'Integrate and Dump'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Filtering'
documentation_page: 'integrateanddump'
documentation_source_path: 'ref/integrateanddump.html'
language: en
---

# Integrate and Dump

## Ports

Not documented in R2025b.

## Parameters

**Integration period**
:   The number of input samples between resets.

**Offset**
:   A nonnegative integer vector or scalar specifying the number of input
    samples to discard from each column of input data at the beginning of the
    simulation.

**Output intermediate values**
:   Determines whether the block outputs the intermediate cumulative sums
    between successive resets.

### Fixed-Point Signal Flow Diagram

### Fixed-Point Attributes

The settings for the following parameters only apply when block inputs are
fixed-point signals.

**Rounding mode**
:   Use this parameter to specify the rounding method to be used when the
    result of a fixed-point calculation does not map exactly to a number
    representable by the data type and scaling storing the result.

    For more information, see Rounding Modes or Rounding Mode: Simplest (Fixed-Point Designer).

**Saturate on integer overflow**
:   Use this parameter to specify the method to be used if the magnitude
    of a fixed-point calculation result does not fit into the range of the
    data type and scaling that stores the result:

    - Saturate represents positive overflows as the largest
      positive number in the range being used, and negative
      overflows as the largest negative number in the range being
      used.
    - Wrap uses modulo arithmetic to cast an overflow back into
      the representable range of the data type. See Modulo Arithmetic (Fixed-Point Designer) for more information.

**Accumulator—Mode**
:   Use the **Accumulator—Mode** parameter to
    specify how you would like to designate the accumulator word and
    fraction lengths:

    - When you select `Inherit via internal
      rule`, the block automatically calculates the
      accumulator output word and fraction lengths.
    - When you select `Same as input`,
      these characteristics match those of the input to the
      block.
    - When you select `Binary point
      scaling`, you are able to enter the word length
      and the fraction length of the accumulator, in bits.
    - When you select `Slope and bias
      scaling`, you are able to enter the word
      length, in bits, and the slope of the accumulator.

**Output**
:   Use the **Output** parameter to choose how you
    specify the word length and fraction length of the output of the block:

    - When you select `Same as
      accumulator`, these characteristics match
      those of the accumulator.
    - When you select `Same as input`,
      these characteristics match those of the input to the
      block.
    - When you select `Binary point
      scaling`, enter the word length and the
      fraction length of the output, in bits.
    - When you select `Slope and bias
      scaling`, enter the word length, in bits,
      and the slope of the output.

For additional information about the parameters pertaining to fixed-point
applications, see Specify Fixed-Point Attributes for Blocks.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Integrate discrete-time signal, resetting to zero periodically

The Integrate and Dump block creates a cumulative sum of the discrete-time input
signal, while resetting the sum to zero according to a fixed schedule. When the
simulation begins, the block discards the number of samples specified in the
**Offset** parameter. After this initial period, the block sums the
input signal along columns and resets the sum to zero every *N* input
samples, where *N* is the **Integration period**
parameter value. The reset occurs after the block produces its output at that time
step.

Receiver models often use the integrate-and-dump operation when the system's
transmitter uses a simple square-pulse model. Fiber optics and in spread-spectrum
communication systems, such as CDMA (code division multiple access) applications, also
use the operation.

This block accepts a scalar, column vector, or matrix input signal. When the input
signal is not a scalar value, it must contain
*k*·*N* rows for some positive integer
*k*. For these input signals, the block processes each column
independently.

Selecting **Output intermediate values** affects the contents,
dimensions, and sample time as follows:

- If you clear the check box, then the block outputs the cumulative sum at each
  reset time.

  - If the input is a scalar value, then the output sample time is
    *N* times the input sample time and the block
    experiences a delay whose duration is one output sample period. In this
    case, the output dimensions match the input dimensions.
  - If the input is a
    (*k*·*N*)-by-*n*
    matrix, then the output is *k*-by-*n*.
    In this case, the block experiences no delay and the output period
    matches the input period.
- If you select the check box, then the block outputs the cumulative sum at each
  time step. The output has the same sample time and the same matrix dimensions as
  the input.

### Transients and Delays

A nonzero value in the **Offset** parameter causes the block to
output one or more zeros during the initial period while it discards input samples.
If the input is a matrix with *n* columns and the
**Offset** parameter is a length-*n* vector,
then the *m*th element of the
**Offset** vector is the offset for the
*m*th column of data. If
**Offset** is a scalar, then the block applies the same offset
to each column of data. The output of initial zeros due to a nonzero
**Offset** value is a transient effect, not a persistent
delay.

When you clear **Output intermediate values**, the block's output
is delayed, relative to its input, throughout the simulation:

- If the input is a scalar value, then the output is delayed by one sample
  after any transient effect is over. That is, after removing transients from
  the input and output, you can see the result of the
  *m*th integration period in
  the output sample indexed by m+1.
- If the input is a column vector or matrix and the
  **Offset** parameter is nonzero, then after the
  transient effect is over, the result of each integration period appears in
  the output frame corresponding to the *last* input sample
  of that integration period. This is one frame later than the output frame
  corresponding to the first input sample of that integration period, in cases
  where an integration period spans two input frames. For an example of this
  situation, see Example of Transient and Delay.
