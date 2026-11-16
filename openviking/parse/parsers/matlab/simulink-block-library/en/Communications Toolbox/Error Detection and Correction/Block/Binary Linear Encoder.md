---
type: simulink-block
title: 'Binary Linear Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'binarylinearencoder'
documentation_source_path: 'ref/binarylinearencoder.html'
language: en
---

# Binary Linear Encoder

## Ports

Not documented in R2025b.

## Parameters

**Generator matrix**
:   A *K*-by-*N* matrix, where
    *K* is the message length and *N* is
    the codeword length.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Create linear block code from binary vector data

The Binary Linear Encoder block creates a binary linear block code using a generator
matrix that you specify. If *K* is the message length of the code, then
the **Generator matrix** parameter must have *K* rows.
If *N* is the codeword length of the code, then **Generator
matrix** must have *N* columns.

This block accepts a column vector input signal containing *K*
elements. This block outputs a column vector with a length of *N*
elements. For information about the data types each block port supports, see Supported Data Type.
