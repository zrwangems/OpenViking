---
type: simulink-block
title: 'Helical Interleaver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Interleaving / Convolutional'
documentation_page: 'helicalinterleaver'
documentation_source_path: 'ref/helicalinterleaver.html'
language: en
---

# Helical Interleaver

## Ports

Not documented in R2025b.

## Parameters

**Number of columns in helical array**
:   The number of columns, C, in the helical array.

**Group size**
:   The size, N, of each group of input symbols. The input width is C times
    N.

**Helical array step size**
:   The number of rows of separation between consecutive input groups in their
    respective columns of the helical array.

**Initial conditions**
:   A scalar that fills the array before the first input is placed.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Permute input symbols using helical array

The Helical Interleaver block permutes the symbols in the input signal by placing them
in an array in a helical fashion and then sending rows of the array to the output
port.

The block uses the array internally for its computations. If *C* is
the **Number of columns in helical array** parameter, then the array
has *C* columns and unlimited rows. If *N* is the
**Group size** parameter, then the block accepts an input of length
*C*·*N* at each time step and partitions the
input into consecutive groups of *N* symbols. Counting from the
beginning of the simulation, the block places the
*k*th group in the array along column
*k* mod *C*. The placement is helical because of
the reduction modulo *C* and because the first symbol in the
*k*th group is in row
1+(*k*-1)· *s*, where *s* is
the **Helical array step size** parameter. Positions in the array that
do not contain input symbols have default contents specified by the **Initial
condition** parameter.

The block sends *C*·*N* symbols from the array
to the output port by reading the next *N* rows sequentially. At a
given time step, the output symbols might be the **Initial condition**
parameter value, symbols from that time step's input vector, or symbols left in the
array from a previous time step.

This block accepts a column vector input signal containing
*C*·*N* elements.

The block can accept the data types `int8`, `uint8`,
`int16`, `uint16`, `int32`,
`uint32`, `boolean`, `single`,
`double`, and fixed-point. The data type of this output will be the
same as that of the input signal.
