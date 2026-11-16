---
type: simulink-block
title: 'General Block Interleaver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Interleaving / Block'
documentation_page: 'generalblockinterleaver'
documentation_source_path: 'ref/generalblockinterleaver.html'
language: en
---

# General Block Interleaver

## Ports

Not documented in R2025b.

## Parameters

**Permutation vector source**
:   A selection that specifies the source of the permutation vector. The
    source can be either `Dialog` or `Input
    port`. The default value is
    `Dialog`.

**Permutation vector**
:   A vector of length N that lists the indices of the output elements that
    came from the input vector. This parameter is available only when
    **Permutation vector source** is set to
    `Dialog`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Reorder symbols in input vector

The General Block Interleaver block rearranges the elements of its input vector
without repeating or omitting any elements. If the input contains *N*
elements, then the **Permutation vector** parameter is a column vector
of length *N*. The column vector indicates the indices, in order, of
the input elements that form the length-*N* output vector; that
is,

Output(*k*) = Input(**Permutation
vector**(k))

for each integer *k* between 1 and *N*. The contents
of **Permutation vector** must be integers between 1 and N, and must
have no repetitions.

Both the input and the **Permutation vector** parameter must be
column vector signals.

This block can output sequences that vary in length during simulation. For more
information about sequences that vary in length, or variable-size signals, see Variable-Size Signal Basics (Simulink).

This block accept the following data types: `int8`,
`uint8`, `int16`, `uint16`,
`int32`, `uint32`, `boolean`,
`single`, `double`, and fixed-point. The output
signal inherits its data type from the input signal.
