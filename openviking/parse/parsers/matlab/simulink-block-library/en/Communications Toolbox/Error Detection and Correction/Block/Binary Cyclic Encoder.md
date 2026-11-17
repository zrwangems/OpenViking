---
type: simulink-block
title: 'Binary Cyclic Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'binarycyclicencoder'
documentation_source_path: 'ref/binarycyclicencoder.html'
language: en
---

# Binary Cyclic Encoder

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters: []
```

**Codeword length N**
:   The codeword length, which is also the output vector length.

**Message length K, or generator polynomial**
:   Either the message length, which is also the input vector length, a polynomial character vector, or a binary vector that represents
    the generator polynomial for the code.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Create systematic cyclic code from binary vector data

The Binary Cyclic Encoder block creates a systematic cyclic code with message length
*K* and codeword length *N*.

This block accepts a column vector input signal containing *K*
elements. The output signal is a column vector containing *N*
elements.

You can determine the systematic cyclic coding scheme in one of two ways:

- To create an [N,K] code, enter N and K as the first and second dialog
  parameters, respectively. The block computes an appropriate generator
  polynomial, namely, `cyclpoly(N,K,'min')`.
- To create a code with codeword length *N* and a particular
  degree-(N-K) binary *generator polynomial*, enter
  *N* as the first parameter and a polynomial character
  vector or a binary vector as the second parameter. The vector
  represents the generator polynomial by listing its coefficients in order of
  ascending exponents. You can create cyclic generator polynomials using the
  Communications Toolbox™
  `cyclpoly` function.

For information about the data types each block port supports, see the Supported Data Type table on this page.
