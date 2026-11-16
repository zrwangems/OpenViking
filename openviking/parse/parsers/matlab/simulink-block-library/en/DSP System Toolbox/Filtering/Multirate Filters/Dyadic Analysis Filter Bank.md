---
type: simulink-block
title: 'Dyadic Analysis Filter Bank'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'dyadicanalysisfilterbank'
documentation_source_path: 'ref/dyadicanalysisfilterbank.html'
language: en
---

# Dyadic Analysis Filter Bank

## Ports

### Input

### **Input 1** — Data input column vector | matrix

Specify the data input as a column vector or a matrix.

The block always interprets the input signal as frames and operates along the columns.
It treats each column of the input as an independent channel, and the
number of rows of each channel must be a multiple of
2*n*, where
*n* is the number of filter bank levels that you
specify in the **Number of levels** parameter. For
example, a frame size of 16 is appropriate for a three-level tree (16 is
a multiple of 23).

For more information on why the input data must meet these requirements, see the figure
in Outputs of a 3-Level Asymmetric Dyadic Analysis Filter Bank.

The block decomposes the input signal into either *n*
+ 1 or 2*n* subbands. To
decompose signals with a frame size that is not a multiple of
2*n*, use the Two-Channel Analysis Subband
Filter block. You can connect multiple copies of the
Two-Channel Analysis Subband Filter block to create a
multilevel dyadic analysis filter bank.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **Output 1** — Dyadic subband decomposition output column vector | matrix

The block outputs the dyadic subband decomposition output as a column vector or a
matrix. The decomposition output contains elements with the
highest-frequency subband first followed by subbands in decreasing
frequency.

The output characteristics vary depending on the block parameter
settings, as summarized in the following list and figure:

- **Number of levels** parameter set to
  *n*
- **Tree structure** parameter setting:

  - `Asymmetric` — Block
    produces *n*+1 output subbands
  - `Symmetric` — Block
    produces
    2*n*
    output subbands
- **Output** parameter setting can be
  `Multiple ports` or
  `Single port`. When you set the
  **Output** parameter to `Single
  port`, the block outputs one vector or matrix
  of concatenated subbands. The following figure illustrates the
  difference between the two settings for a 3-level asymmetric
  dyadic analysis filter bank. For an explanation of the
  illustrated output characteristics, see the table Output Characteristics for an n-Level Dyadic Analysis Filter Bank.

For more information about the filter bank levels and structures, see
Dyadic Analysis Filter Banks.

**Outputs of a 3-Level Asymmetric Dyadic Analysis Filter
Bank**

The following table summarizes the different output characteristics of the block when
you set it to output from single or multiple ports.

**Output Characteristics for an n-Level Dyadic
Analysis Filter Bank**

|  | Single Output Port | Multiple Output Ports |
| --- | --- | --- |
| **Output Description** | Block concatenates all the subbands into one vector or matrix, and outputs the concatenated subbands from a single output port. Each output column contains subbands of the corresponding input channel. | Block outputs each subband from a separate output port. The topmost port outputs the subband with the highest frequencies. Each output column contains a subband for the corresponding input channel. |
| **Output Frame Rate** | *Not applicable* | Same as input frame rate   (However, the output frame sizes can vary, so the output sample rates can vary.) |
| **Output Dimensions (Frame Size)** | Same number of rows and columns as the input. | The output has the same number of columns as the input. The number of output rows is the output frame size. For an input with frame size *M*i output *yk* has frame size *Mo,k*:  - `Symmetric`   — All outputs have the frame size   *M*i /   2*n*. - `Asymmetric`   — The frame size of each output (except the   last) is half that of the output from the previous   level. The outputs from the last two output ports   have the same frame size since they originate from   the same level in the filter bank.  Mo,k={Mi/2k(1≤k≤n)Mi/2n(k=n+1) |
| **Output Sample Rate** | Same as input sample rate. | Though the outputs have the same frame rate as the input, they have different frame sizes than the input. Thus, the output sample rates *Fso,k* are different from the input sample rate *Fsi*:  - `Symmetric`   — All outputs have the sample rate   *Fsi* /   2*n*. - `Asymmetric`   —  Fso,k={Fsi/2k(1≤k≤n)Fsi/2n(k=n+1) |

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

The parameters displayed in the block dialog box vary depending on the setting of the
**Filter** parameter. Only some of the parameters described below
are visible in the dialog box at any one time.

### **Filter** — Type of filter used in subband decomposition `User-defined` (default) | `Haar` | `Daubechies` | `Symlets` | `Coiflets` | `Biorthogonal` | `Reverse Biorthogonal` | `Discrete Meyer`

Specify the highpass and lowpass filters in the filter bank by setting the
**Filter** parameter to one of these options:

- `User defined` — Allows you to
  explicitly specify the filters with two vectors of filter
  coefficients in the **Lowpass FIR filter
  coefficients** and **Highpass FIR filter
  coefficients** parameters. The block uses the same
  lowpass and highpass filters throughout the filter bank. The two
  filters should be halfband filters, where each filter passes the
  frequency band that the other filter stops.
- Wavelet such as `Biorthogonal` or
  `Daubechies` — The block uses
  the specified wavelet to construct the lowpass and highpass filters
  using the Wavelet Toolbox
  `wfilters` function. Depending on the wavelet, the
  block enable either the **Wavelet order** or the
  **Filter order [synthesis / analysis]**
  parameter. The **Filter order [synthesis /
  analysis]** parameter allows you to specify different
  wavelet orders for the analysis and synthesis filter stages. You
  must have a Wavelet Toolbox license to use wavelets.

See this table for a list of the supported wavelets.

**Specifying Filters with the Filter Parameter and
Related Parameters**

| Filter | Sample Setting for Related Filter Specification Parameters | Corresponding Wavelet Function Syntax |
| --- | --- | --- |
| **User-defined** | Filters based on Daubechies wavelets with wavelet order `3`:  - **Lowpass FIR filter coefficients =**`[0.0352 -0.0854 -0.1350 0.4599   0.8069 0.3327]` - **Highpass FIR filter coefficients =**`[-0.3327 0.8069 -0.4599   -0.1350 0.0854 0.0352]` | None |
| **Haar** | None | `wfilters('haar')` |
| **Daubechies** | **Wavelet order =**`4` | `wfilters('db4')` |
| **Symlets** | **Wavelet order =**`3` | `wfilters('sym3')` |
| **Coiflets** | **Wavelet order =**`1` | `wfilters('coif1')` |
| **Biorthogonal** | **Filter order [synthesis / analysis] =**`[3/1]` | `wfilters('bior3.1')` |
| **Reverse Biorthogonal** | **Filter order [synthesis / analysis] =**`[3/1]` | `wfilters('rbio3.1')` |
| **Discrete Meyer** | None | `wfilters('dmey')` |

### **Filter order [synthesis / analysis]** — Analysis and synthesis filter orders for biorthogonal filters `[1 / 1]` (default) | `[1 / 3]` | `[1 / 5]` | `[2 / 2]` | `[2 / 4]` | `[2 / 6]` | `[2 / 8]` | `[3 / 1]` | `[3 / 3]` | `[3 / 5]` | `[3 / 7]` | `[3 / 9]` | `[4 / 4]` | `[5 / 5]` | `[6 / 8]`

Set the order of the wavelet for the synthesis and analysis filter stages. For example,
when you set the **Filter** parameter to
`Biorthogonal` and set the **Filter
order [synthesis / analysis]** parameter to `[2 /
6]`, the block calls the `wfilters` function
with input argument `'bior2.6'`.

#### Dependencies

To enable this parameter, set the **Filter** parameter to
`Biorthogonal` or `Reverse
Biorthogonal`.

### **Wavelet order** — Order for orthogonal wavelets `2` (default) | positive integer

Set the order of the wavelet selected in the **Filter**
parameter.

#### Dependencies

To enable this parameter, set the **Filter** parameter to
`Daubechies`,
`Symlets`, or
`Coiflets`.

### **Lowpass FIR filter coefficients** — Lowpass FIR filter coefficients `[0.0352 -0.0854 -0.1350 0.4599 0.8069 0.3327]` (default) | row vector

Specifies coefficients used by all the lowpass filters in the filter bank using a vector
of filter coefficients (descending powers of *z*). The
lowpass filter should be a half-band filter that passes the frequency band
stopped by the filter specified in the **Highpass FIR filter
coefficients** parameter. The default values of this parameter
specify a filter based on a Daubechies wavelet with wavelet order
`3`.

#### Dependencies

To enable this parameter, set the **Filter** parameter to
`User-defined`.

### **Highpass FIR filter coefficients** — Highpass FIR filter coefficients `[-0.3327 0.8069 -0.4599 -0.1350 0.0854 0.0352]` (default) | row vector

Specifies coefficients used by all the highpass filters in the filter bank
using a vector of filter coefficients (descending powers of
*z*). This parameter is enabled when you set
**Filter** to `User defined`.
The highpass filter should be a half-band filter that passes the frequency
band stopped by the filter specified in the **Lowpass FIR filter
coefficients** parameter. The default values of this parameter
specify a filter based on a Daubechies wavelet with wavelet order
`3`.

#### Dependencies

To enable this parameter, set the **Filter** parameter to
`User-defined`.

### **Number of levels** — Number of filter bank levels used in analysis (decomposition) `2` (default) | integer greater than or equal to 1

Select the number of filter bank levels. An *n*-level asymmetric
structure has *n*+1 outputs, and an
*n*-level symmetric structure has
2*n* outputs, as shown
in Multilevel Filter Banks. The block icon
changes depending on the value of this parameter.

### **Tree structure** — Structure of filter bank `Asymmetric` (default) | `Symmetric`

Select the structure of the filter bank: `Asymmetric`, or
`Symmetric`. See Multilevel Filter Banks for more
information.

The default setting of this parameter is `Asymmetric` for the
Dyadic Analysis Filter Bank block, and
`Symmetric` for the DWT block.

### **Output** — Single port or multiple ports `Multiple ports` (default) | `Single port`

Set to `Multiple ports` to output each output
subband on a separate port. The topmost port outputs the subband with the
highest frequency band. Set to `Single port` to
concatenate the subbands into one vector or matrix and output the
concatenated subbands on a single port. For more information, see the Output port description.

The default setting of this parameter is `Multiple
ports` for the Dyadic Analysis Filter Bank
block and `Single port` for the DWT block.

## Libraries

DSP System Toolbox / Filtering / Multirate Filters

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

Decompose signals into subbands with smaller bandwidths and slower sample rates or compute discrete wavelet transform (DWT)

You can configure this block to decompose a broadband signal into a collection of subbands
with smaller bandwidths and slower sample rates. The block uses a series of highpass and
lowpass FIR filters to repeatedly divide the input frequency range, as illustrated in
Multilevel Filter Banks (the Asymmetric one).

You can specify the filter bank highpass and lowpass filters by providing vectors of filter
coefficients. You can do so directly on the block mask. If you have a Wavelet Toolbox™ license, you can specify wavelet-based filters by selecting a wavelet from
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

The Dyadic Analysis Filter Bank block is same as the DWT
block, but with different default settings.
