---
type: simulink-block
title: 'IDWT'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'idwt'
documentation_source_path: 'ref/idwt.html'
language: en
---

# IDWT

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
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

## Version History

**Introduced before R2006a**

## Description

Inverse discrete wavelet transform (IDWT) of input or reconstruct signals from subbands with smaller bandwidths and slower sample rates

You can configure this block to compute the inverse discrete wavelet transform (IDWT)
or reconstruct a signal from subbands with smaller bandwidths and slower sample rates.
When the block computes the inverse discrete wavelet transform (IDWT) of the input, the
output has the same dimensions as the input. Each column of the output is the IDWT of
the corresponding input column. When reconstructing a signal, the block uses a series of
highpass and lowpass FIR filters to reconstruct the signal from the input subbands, as
illustrated in Multilevel Filter Banks (the Asymmetric one). The
reconstructed signal has a wider bandwidth and faster sample rate than the input
subbands.

You can specify the filter bank highpass and lowpass filters by providing vectors of filter
coefficients. You can do so directly on the block dialog box. If you have a Wavelet Toolbox™ license, you can specify wavelet-based filters by selecting a wavelet from
the **Filter** parameter. You must set the filter bank structure to
asymmetric or symmetric, and specify the number of levels in the filter bank.

**Note**

The IDWT block is the same as the Dyadic Synthesis Filter
Bank block with different default settings. For more information on
block ports and parameters, see the Dyadic Synthesis Filter Bank block reference page.
