---
type: simulink-block
title: 'A-Law Expander'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Source Coding'
documentation_page: 'alawexpander'
documentation_source_path: 'ref/alawexpander.html'
language: en
---

# A-Law Expander

## Ports

Not documented in R2025b.

## Parameters

**A value**
:   The A-law parameter of the compressor.

**Peak signal magnitude**
:   The peak value of the input signal. This is also the peak value of the
    output signal.

Match these parameters to the ones in the corresponding A-Law
Compressor block.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Implement A-law expander for source coding

The A-Law Expander block recovers data that the A-Law
Compressor block compressed. The formula for the A-law expander, shown
below, is the inverse of the compressor function.

x={y(1+logA)Afor 0≤|y|≤V1+logAexp(|y|(1+logA)/V−1)VAsgn(y)for V1+logA<|y|≤V

The input can have any shape or frame status. This block processes each vector element
independently.
