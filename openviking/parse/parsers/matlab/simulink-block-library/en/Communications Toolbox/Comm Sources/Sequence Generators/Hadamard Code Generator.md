---
type: simulink-block
title: 'Hadamard Code Generator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Sources / Sequence Generators'
documentation_page: 'hadamardcodegenerator'
documentation_source_path: 'ref/hadamardcodegenerator.html'
language: en
---

# Hadamard Code Generator

## Ports

Not documented in R2025b.

## Parameters

**Code length**
:   A positive integer that is a power of two specifying the length of the
    Hadamard code.

**Code index**
:   An integer between 0 and *N*-1, where
    *N* is the **Code length**, specifying
    a row of the Hadamard matrix.

**Sample time**
:   Positive scalars specify the time in seconds between each
    sample of the output signal. If you set the sample time to `-1`, the output
    signal inherits the sample time from downstream. For information on the relationship between the
    **Sample time** and **Samples per frame** parameters,
    see
    Sample Timing.

**Samples per frame**
:   Samples per frame, specified as a positive integer indicating the number
    of samples per frame in one channel of the output data. For information on
    the relationship between **Sample time** and
    **Samples per frame**, see Sample Timing.

**Output data type**
:   The output type of the block can be specified as an
    `int8` or `double`. By default, the
    block sets this to `double`.

**Simulate using**
:   Select the simulation mode.

    `Code generation`
    :   On the first model run, simulate and generate code. If the
        structure of the block does not change, subsequent model runs do
        not regenerate the code.

        If the simulation mode is `Code
        generation`, System objects corresponding to
        the blocks accept a maximum of nine inputs.

    `Interpreted execution`
    :   Simulate model without generating code. This option results in
        faster start times but can slow subsequent simulation
        performance.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

### R2020a: Existing models automatically update this block to current version

Starting in R2020a, Simulink® no longer allows you to use the Hadamard Code Generator block version available
before R2015b.

Existing models automatically update to load the Hadamard Code Generator block version
announced in Source blocks output frames of contiguous time samples but do not use frame attribute. For more
information on block forwarding, see Maintain Compatibility of Library Blocks Using Forwarding Tables (Simulink).

## Description

Generate Hadamard code from orthogonal set of codes

The Hadamard Code Generator block generates a Hadamard code from a Hadamard matrix,
whose rows form an orthogonal set of codes. Orthogonal codes can be used for spreading
in communication systems in which the receiver is perfectly synchronized with the
transmitter. In these systems, the despreading operation is ideal, as the codes are
decorrelated completely.

The Hadamard codes are the individual rows of a Hadamard matrix. Hadamard matrices are
square matrices whose entries are +1 or -1, and whose rows and columns are mutually
orthogonal. If *N* is a nonnegative power of 2,
the*N*-by-*N* Hadamard matrix, denoted
*H*N, is defined recursively as
follows.

H1=[1]H2N=[HNHNHN−HN]

The N-by-N Hadamard matrix has the property that

*H*N*H*NT
= *N**I*N

where *I*N is the
*N*-by-*N* identity matrix.

The Hadamard Code Generator block outputs a row of
*H*N. The output is bipolar. You specify the
length of the code, *N*,by the **Code length**
parameter. The **Code length** must be a power of 2. You specify the
index of the row of the Hadamard matrix, which is an integer in the range [0, 1, ... ,
*N*-1], by the **Code index** parameter.
