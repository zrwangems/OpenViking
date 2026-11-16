---
type: simulink-block
title: 'Differential Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Source Coding'
documentation_page: 'differentialdecoder'
documentation_source_path: 'ref/differentialdecoder.html'
language: en
---

# Differential Decoder

## Ports

Not documented in R2025b.

## Parameters

**Initial conditions**
:   The logical exclusive-or of this value with the initial input value forms
    the initial output value.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Decode binary signal using differential coding

The Differential Decoder block decodes the binary input signal. The output is the
logical difference between the consecutive input element within a channel. More
specifically, the block's input and output are related by

m(i0) = d(i0) XOR
**Initial condition** parameter value

m(ik) = d(ik) XOR
d(ik-1)

where

- d is the differentially encoded input.
- m is the output message.
- ik is the kth element.
- XOR is the logical exclusive-or operator.

This block accepts a scalar, column vector, or matrix input signal and treats columns
as channels.
