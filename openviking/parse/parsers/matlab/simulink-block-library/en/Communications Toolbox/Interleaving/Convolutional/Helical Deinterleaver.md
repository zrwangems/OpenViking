---
type: simulink-block
title: 'Helical Deinterleaver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Interleaving / Convolutional'
documentation_page: 'helicaldeinterleaver'
documentation_source_path: 'ref/helicaldeinterleaver.html'
language: en
---

# Helical Deinterleaver

## Ports

Not documented in R2025b.

## Parameters

**Number of columns in helical array**
:   The number of columns, *C*, in the helical array.

**Group size**
:   The size, *N*, of each group of symbols. The input width
    is *C* times *N*.

**Helical array step size**
:   The number of rows of separation between consecutive output groups as the
    block selects them from their respective columns of the helical
    array.

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

Restore ordering of symbols permuted by helical interleaver

The Helical Deinterleaver block permutes the symbols in the input signal by placing
them in an array row by row and then selecting groups in a helical fashion to send to
the output port.

The block uses the array internally for its computations. If *C* is
the **Number of columns in helical array** parameter, then the array
has *C* columns and unlimited rows. If *N* is the
**Group size** parameter, then the block accepts an input of length
*C*·*N* at each time step and inserts them
into the next *N* rows of the array. The block also places the
**Initial condition** parameter into certain positions in the top
few rows of the array (not only to accommodate the helical pattern but also to preserve
the vector indices of symbols that pass through the Helical Interleaver and Helical
Deinterleaver blocks in turn).

The output consists of consecutive groups of *N* symbols. Counting
from the beginning of the simulation, the block selects the kth output group in the
array from column *k* mod *C*. The selection is
helical because of the reduction modulo C and because the first symbol in the
*k*th group is in row
1+(*k*-1)\*s, where *s* is the **Helical
array step size** parameter.

This block accepts a column vector input signal containing
*C*·*N* elements.

The block can accept the data types `int8`, `uint8`,
`int16`, `uint16`, `int32`,
`uint32`, `boolean`, `single`,
`double`, and fixed-point. The data type of this output will be the
same as that of the input signal.

### Delay of Interleaver-Deinterleaver Pair

After processing a message with the Helical Interleaver block and the Helical Deinterleaver block, the
deinterleaved data lags the original message by

CN⌈s(C−1)N⌉

samples. Before this delay elapses, the deinterleaver output is either the
**Initial condition** parameter in the Helical Deinterleaver
block or the **Initial condition** parameter in the Helical
Interleaver block.

If your model incurs an additional delay between the interleaver output and the
deinterleaver input, then the restored sequence lags the original sequence by the
sum of the additional delay and the amount in the formula above. For proper
synchronization, the delay between the interleaver and deinterleaver must be m·
*C* · *N* for some nonnegative integer
*m*. You can use the DSP System Toolbox™
Delay block to adjust delays manually, if
necessary.
