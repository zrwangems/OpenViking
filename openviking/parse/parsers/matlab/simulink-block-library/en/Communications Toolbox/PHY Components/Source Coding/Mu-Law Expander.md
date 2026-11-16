---
type: simulink-block
title: 'Mu-Law Expander'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Source Coding'
documentation_page: 'mulawexpander'
documentation_source_path: 'ref/mulawexpander.html'
language: en
---

# Mu-Law Expander

## Ports

Not documented in R2025b.

## Parameters

**mu value**
:   The µ-law parameter of the compressor.

**Peak signal magnitude**
:   The peak value of the input signal. This is also the peak value of the
    output.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Implement µ-law expander for source coding

The Mu-Law Expander block recovers data that the Mu-Law Compressor block compressed. The formula for the µ-law expander,
shown below, is the inverse of the compressor function.

x=Vμ(e|y|log(1+μ)/V−1)sgn(y)

The input can have any shape or frame status. This block processes each vector element
independently.
