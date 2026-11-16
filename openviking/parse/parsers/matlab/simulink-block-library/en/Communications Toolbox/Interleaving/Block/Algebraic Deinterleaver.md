---
type: simulink-block
title: 'Algebraic Deinterleaver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Interleaving / Block'
documentation_page: 'algebraicdeinterleaver'
documentation_source_path: 'ref/algebraicdeinterleaver.html'
language: en
---

# Algebraic Deinterleaver

## Ports

Not documented in R2025b.

## Parameters

**Type**
:   The type of permutation table that the block uses for deinterleaving.
    Choices are `Takeshita-Costello` and
    `Welch-Costas`.

**Number of elements**
:   The number of elements, *N*, in the input vector.

**Multiplicative factor**
:   The factor the block uses to compute the corresponding interleaver's cycle
    vector. This field appears only when you set **Type** to
    `Takeshita-Costello`.

**Cyclic shift**
:   The amount by which the block shifts indices when creating the
    corresponding interleaver's permutation table. This field appears only when
    you set **Type** to
    `Takeshita-Costello`.

**Primitive element**
:   An element of order *N* in the finite field GF(N+1). This
    field appears only if **Type** is set to
    `Welch-Costas`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Restore ordering of input symbols using algebraically derived permutation

The Algebraic Deinterleaver block restores the original ordering of a sequence that
was interleaved using the Algebraic Interleaver block. In typical
usage, the parameters in the two blocks have the same values.

The **Number of elements** parameter, *N*, indicates
how many numbers are in the input vector. This block accepts a column vector input
signal.

The block accepts the following data types: `int8`,
`uint8`, `int16`, `uint16`,
`int32`, `uint32`, `boolean`,
`single`, `double`, and fixed-point. The output
signal inherits its data type from the input signal.

The **Type** parameter indicates the algebraic method that the block
uses to generate the appropriate permutation table. Choices are
`Takeshita-Costello` and
`Welch-Costas`. Each of these methods has parameters and
restrictions that are specific to it; these are described on the reference page for the
Algebraic Interleaver block.
