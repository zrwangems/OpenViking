---
type: simulink-block
title: 'Walsh Code Generator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Sources / Sequence Generators'
documentation_page: 'walshcodegenerator'
documentation_source_path: 'ref/walshcodegenerator.html'
language: en
---

# Walsh Code Generator

## Ports

Not documented in R2025b.

## Parameters

**Code length**
:   Integer scalar that is a power of 2 specifying the length of the output
    code.

**Code index**
:   Integer scalar in the range [0, 1, ... , N - 1], where N is the
    **Code length**, specifying the number of zero
    crossings in the output code.

**Sample time**
:   Positive scalars specify the time in seconds between each
    sample of the output signal. If you set the sample time to `-1`, the output
    signal inherits the sample time from downstream. For information on the relationship between the
    **Sample time** and **Samples per frame** parameters,
    see
    Sample Timing.

**Samples per frame**
:   Samples per frame, specified as a positive integer indicating the number
    of samples per frame in one channel of the output data. If **Samples
    per frame** is greater than the **Code
    length**, the code is cyclically repeated. For information on
    the relationship between **Sample time** and
    **Samples per frame**, see Sample Timing.

**Output data type**
:   The output type of the block can be specified as an
    `int8` or `double`. By default, the
    block sets this to `double`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

### R2020a: Existing models automatically update this block to current version

Starting in R2020a, Simulink® no longer allows you to use the Walsh Code Generator block version available
before R2015b.

Existing models automatically update to load the Walsh Code Generator block version
announced in Source blocks output frames of contiguous time samples but do not use frame attribute. For more
information on block forwarding, see Maintain Compatibility of Library Blocks Using Forwarding Tables (Simulink).

## Description

Generate Walsh code from orthogonal set of codes

Walsh codes are defined as a set of *N* codes, denoted
*W*j, for *j* = 0, 1,
... , *N* - 1, which have the following properties:

- *W*j takes on the values +1 and
  -1.
- *W*j[0] = 1 for all
  *j*.
- *W*j has exactly
  *j* zero crossings, for *j* = 0, 1,
  ... , *N* - 1.
- WjWkT={0j≠kNj=k
- Each code W*j* is either even or odd with respect to its
  midpoint.

Walsh codes are defined using a Hadamard matrix of order *N*. The
Walsh Code Generator block outputs a row of the Hadamard matrix specified by the
**Walsh code index**, which must be an integer in the range [0,
..., *N* - 1]. If you set **Walsh code index** equal
to an integer *j*, the output code has exactly *j*
zero crossings, for *j* = 0, 1, ... , *N* -
1.

Note, however, that the indexing in the Walsh Code Generator block is different than
the indexing in the Hadamard Code Generator block. If you set the **Walsh code
index** in the Walsh Code Generator block and the **Code index
parameter** in the Hadamard Code Generator block, the two blocks output
different codes.
