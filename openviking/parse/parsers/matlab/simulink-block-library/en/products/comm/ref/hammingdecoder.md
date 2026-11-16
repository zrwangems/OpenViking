---
type: simulink-block
title: 'Hamming Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Error Detection and Correction / Block Coding / Linear Block Codes'
documentation_page: 'hammingdecoder'
documentation_source_path: 'ref/hammingdecoder.html'
language: en
---

# Hamming Decoder

## Ports

Not documented in R2025b.

## Parameters

**Codeword length N**
:   The codeword length *N*, which is also the input vector
    length.

**Message length K, or M-degree primitive polynomial**
:   The message length, which is also the input vector length or a binary
    vector that represents a primitive polynomial for
    GF(2M) or a polynomial character vector.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Decode Hamming code to recover binary vector data

The Hamming Decoder block recovers a binary message vector from a binary Hamming
codeword vector. For proper decoding, the parameter values in this block should match
those in the corresponding Hamming Encoder block.

If the Hamming code has message length *K* and codeword length
*N*, then *N* must have the form
2M-1 for some integer *M* greater than
or equal to 3. Also, *K* must equal
*N*-*M*.

This block accepts a column vector input signal of length *N*. The
output signal is a column vector of length *K*.

The coding scheme uses elements of the finite field GF(2M).
You can either specify the primitive polynomial that the algorithm should use, or you
can rely on the default setting:

- To use the default primitive polynomial, simply enter *N* and
  *K* as the first and second dialog parameters,
  respectively. The algorithm uses `gfprimdf(M)` as the primitive
  polynomial for GF(2M).
- To specify the primitive polynomial, enter *N* as the first
  parameter and a binary vector as the second parameter. The vector represents the
  primitive polynomial by listing its coefficients in order of ascending
  exponents. You can create primitive polynomials using the Communications Toolbox™
  `gfprimfd` function.
- In addition, you can specify the primitive polynomial as a character vector, for
  example, `'D^3 + D + 1'`.

For information about the data types each block port supports, see the Supported Data Type table on this page.
