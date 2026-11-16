---
type: simulink-block
title: 'Binary Linear Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Error Detection and Correction / Block Coding / Linear Block Codes'
documentation_page: 'binarylineardecoder'
documentation_source_path: 'ref/binarylineardecoder.html'
language: en
---

# Binary Linear Decoder

## Ports

Not documented in R2025b.

## Parameters

**Generator matrix**
:   Generator matrix for the code; same as in Binary Linear Encoder
    block.

**Decoding table**
:   Either a 2N-K-by-N matrix that lists correction
    vectors for each codeword's syndrome; or the scalar 0, in which case the
    block defaults to the table corresponding to the **Generator
    matrix** parameter.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Decode linear block code to recover binary vector data

The Binary Linear Decoder block recovers a binary message vector from a binary
codeword vector of a linear block code.

The **Generator matrix** parameter is the generator matrix for the
block code. For proper decoding, this should match the **Generator
matrix** parameter in the corresponding Binary Linear Encoder block. If *N* is the codeword length
of the code, then **Generator matrix** must have *N*
columns. If *K* is the message length of the code, then the
**Generator matrix** parameter must have *K*
rows.

This block accepts a column vector input signal containing *N*
elements. This block outputs a column vector with a length of *K*
elements.

The decoder tries to correct errors, using the **Decoding table**
parameter. If **Decoding table** is the scalar 0, then the block
defaults to the table produced by the Communications Toolbox™ function `syndtable`. Otherwise, **Decoding
table** must be a 2N-K-by-N binary matrix. The
*r*th row of this matrix is the correction vector for a received
binary codeword whose syndrome has decimal integer value *r*-1. The
syndrome of a received codeword is its product with the transpose of the parity-check
matrix.

For information about the data types each block port supports, see the Supported Data Type table on this page.
