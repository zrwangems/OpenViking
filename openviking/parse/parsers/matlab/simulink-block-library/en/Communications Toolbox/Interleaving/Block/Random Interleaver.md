---
type: simulink-block
title: 'Random Interleaver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Interleaving / Block'
documentation_page: 'randominterleaver'
documentation_source_path: 'ref/randominterleaver.html'
language: en
---

# Random Interleaver

## Ports

Not documented in R2025b.

## Parameters

**Number of elements**
:   The number of elements in the input vector.

**Initial seed**
:   The initial seed value for the random number generator.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Reorder input symbols using random permutation

The Random Interleaver block rearranges the elements of its input vector using a
random permutation. This block accepts a column vector input signal. The
**Number of elements** parameter indicates how many numbers are in
the input vector.

The block accepts the following data types: `int8`,
`uint8`, `int16`, `uint16`,
`int32`, `uint32`, `boolean`,
`single`, `double`, and fixed-point. The output
signal inherits its data type from the input signal.

The **Initial seed** parameter initializes the random number
generator that the block uses to determine the permutation. The block is predictable for
a given seed, but different seeds produce different permutations.
