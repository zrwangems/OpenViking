---
type: simulink-block
title: 'DWT'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'dwt'
documentation_source_path: 'ref/dwt.html'
language: en
---

# DWT

## Ports

Not documented in R2025b.

## Parameters

Not documented in R2025b.

## Libraries

DSP System Toolbox / Transforms

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `No` |
| **Variable-Size Signals** | `No` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

## Version History

**Introduced before R2006a**

## Description

Compute discrete wavelet transform (DWT) of input or decompose signals into subbands with smaller bandwidths and slower sample rates

You can configure this block to compute the Discrete Wavelet Transform (DWT) of the
input signal or decompose the signal into subbands with smaller bandwidths and slower
sample rates. The block uses a series of highpass and lowpass FIR filters to repeatedly
divide the input frequency range, as illustrated in Multilevel Filter Banks (the Asymmetric one).

You can specify the filter bank highpass and lowpass filters by providing vectors of
filter coefficients. You can do so directly on the block mask. If you have a Wavelet Toolbox™ license, you can specify wavelet-based filters by selecting a wavelet from
the **Filter** parameter. You must set the filter bank structure to
asymmetric or symmetric, and specify the number of levels in the filter bank.

For the same input, the DWT configuration of this block does not produce the same
results as the Wavelet Toolbox
`dwt` function. Because DSP System Toolbox™ is designed for real-time implementation and Wavelet Toolbox is designed for analysis, the products handle boundary conditions and
filter states differently. To make the output of the `dwt` function
match the DWT output of this block, complete the following steps:

1. Set the boundary condition of the `dwt` function to
   zero-padding. To do so, type `dwtmode('zpd')` at the
   MATLAB® command line.
2. To match the latency of the block (implemented using FIR filters), add zeros
   to the input of the `dwt` function. The number of zeros you add
   must be equal to the half-length of the filter.

**Note**

The DWT block is same as the Dyadic Analysis Filter
Bank block with different default settings. For more information on
block ports and parameters, see the Dyadic Analysis Filter Bank block reference page.
