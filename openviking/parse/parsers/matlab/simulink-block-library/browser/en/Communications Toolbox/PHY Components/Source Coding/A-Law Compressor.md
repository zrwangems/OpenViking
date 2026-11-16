---
type: simulink-block
title: 'A-Law Compressor'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Source Coding'
documentation_page: 'alawcompressor'
documentation_source_path: 'ref/alawcompressor.html'
language: en
---

# A-Law Compressor

## Ports

Not documented in R2025b.

## Parameters

**A value**
:   The A-law parameter of the compressor.

**Peak signal magnitude**
:   The peak value of the input signal. This is also the peak value of the
    output signal.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Implement A-law compressor for source coding

The A-Law Compressor block implements an A-law compressor for the input signal. The
formula for the A-law compressor is

y={A|x|1+logAsgn(x)for 0≤|x|≤VAV(1+log(A|x|/V))1+logAsgn(x)for VA<|x|≤V

where *A* is the A-law parameter of the compressor,
*V* is the peak signal magnitude for *x*, log is
the natural logarithm, and *sgn* is the `sign` function.

The most commonly used *A* value is 87.6.

The input can have any shape or frame status. This block processes each vector element
independently.
