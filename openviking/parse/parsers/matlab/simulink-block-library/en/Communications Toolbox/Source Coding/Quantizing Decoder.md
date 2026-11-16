---
type: simulink-block
title: 'Quantizing Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Source Coding'
documentation_page: 'quantizingdecoder'
documentation_source_path: 'ref/quantizingdecoder.html'
language: en
---

# Quantizing Decoder

## Ports

Not documented in R2025b.

## Parameters

**Quantization codebook**
:   A real vector that prescribes the output value corresponding to each
    nonnegative integer of the input.

**Quantized output data type**
:   Select the output data type.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Decode quantization index according to codebook

The Quantizing Decoder block converts quantization indices to the corresponding
codebook values. The **Quantization codebook** parameter, a vector of
length N, prescribes the possible output values. If the input is an integer k between 0
and N-1, then the output is the (k+1)st element of **Quantization
codebook**.

The input must be a discrete-time signal. This block processes each vector element
independently. For information about the data types each block port supports, see the
Supported Data Type table on this page.

**Note**

The Quantizing Encoder block also uses a
**Quantization codebook** parameter. The first output of that
block corresponds to the input of Quantizing Decoder, while the second output of
that block corresponds to the output of Quantizing Decoder.
