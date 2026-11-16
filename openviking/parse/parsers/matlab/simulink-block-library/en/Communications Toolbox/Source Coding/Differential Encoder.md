---
type: simulink-block
title: 'Differential Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Source Coding'
documentation_page: 'differentialencoder'
documentation_source_path: 'ref/differentialencoder.html'
language: en
---

# Differential Encoder

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

Encode binary signal using differential coding

The Differential Encoder block encodes the binary input signal within a channel. The
output is the logical difference between the current input element and the previous
output element. More specifically, the input and output are related by

d(i0) = m(i0) XOR
**Initial condition** parameter value

d(ik) = d(ik-1) XOR
m(ik)

where

- m is the input message.
- d is the differentially encoded output.
- ik is the kth element.
- XOR is the logical exclusive-or operator.

This block accepts a scalar or column vector input signal and treats columns as
channels.
