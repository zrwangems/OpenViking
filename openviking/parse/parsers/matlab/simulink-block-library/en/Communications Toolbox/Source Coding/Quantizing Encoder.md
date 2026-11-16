---
type: simulink-block
title: 'Quantizing Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Source Coding'
documentation_page: 'quantizingencoder'
documentation_source_path: 'ref/quantizingencoder.html'
language: en
---

# Quantizing Encoder

## Ports

Not documented in R2025b.

## Parameters

**Quantization partition**
:   The vector of endpoints of the partition intervals.

**Quantization codebook**
:   The vector of output values assigned to each partition.

**Index output data type**
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

Quantize signal using partition and codebook

The Quantizing Encoder block quantizes the input signal according to the
**Partition** vector and encodes the input signal according to the
**Codebook** vector. This block processes each vector element
independently. The input must be a discrete-time signal. This block processes each
vector element independently. For information about the data types each block port
supports, see the Supported Data Type table on this page.

The first output is the quantization index. The second output is the quantized signal.
The values for the quantized signal are taken from the **Codebook**
vector.

The **Quantization partition** parameter, *P*, is a
real vector of length n whose entries are in strictly ascending order. The quantization
index (second output signal value) corresponding to an input value of
*x* is

- 0 if *x* ≤ *P*(1)
- m if *P*(m) < *x* ≤
  *P*(m+1)
- n if *P*(n) < *x*

The **Quantization codebook** parameter, whose length is n+1,
prescribes a value for each partition in the quantization. The first element of
**Quantization codebook** is the value for the interval between
negative infinity and the first element of *P*. The second output
signal from this block contains the quantization of the input signal based on the
quantization indices and prescribed values.

Use the `lloyds` function with a representative
sample of your data as training data, to obtain appropriate partition and codebook
parameters.
