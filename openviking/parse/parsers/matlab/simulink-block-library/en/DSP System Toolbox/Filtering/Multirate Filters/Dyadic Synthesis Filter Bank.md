---
type: simulink-block
title: 'Dyadic Synthesis Filter Bank'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'dyadicsynthesisfilterbank'
documentation_source_path: 'ref/dyadicsynthesisfilterbank.html'
language: en
---

# Dyadic Synthesis Filter Bank

## Ports

### Input

### **Input 1** — Data input column vector | matrix

Specify the data input as a column vector or a matrix.

The input characteristics vary depending on the block parameter
settings as summarized here:

- **Number of levels** parameter set to
  *n*
- **Tree structure** parameter setting:

  - `Asymmetric` — Block
    accepts *n*+1 input subbands
  - `Symmetric` — Block
    accepts 2*n*
    input subbands
  - **Input** parameter setting can be
    `Multiple ports` or
    `Single port`.

    The inputs to this block are usually the outputs of a Dyadic Analysis
    Filter Bank block. Since the Dyadic
    Analysis Filter Bank block can output from
    either a single port or multiple ports, the
    Dyadic Synthesis Filter Bank block
    accepts inputs to either a single port or to multiple
    ports.

    When you set the **Input** parameter
    to `Multiple ports`, you must
    provide each subband to the block through a different
    input port as a vector or matrix. You should input the
    highest frequency band through the topmost port. When
    you set the **Input** parameter to
    `Single port`, the block
    input must be a vector or matrix of concatenated
    subbands.

**Note**

Any output of a Dyadic Analysis Filter Bank block
whose parameter settings match the corresponding settings of this
block is a valid input to this block. For example, the setting of
the Dyadic Analysis Filter Bank block parameter
**Output** must be the same as the
**Input** parameter (`Single
port` or `Multiple ports`)
in this block.

**Valid Inputs for Input Set to Single
Port**

- Input must be a vector or matrix of concatenated
  subbands.
- Each input column contains the subbands for an independent
  signal.
- Upper input rows contain the high-frequency subbands, and the
  lower rows contain the low-frequency subbands.

**Valid Inputs for Input Set to Multiple
Ports**

- Each subband must be provided as a vector or a matrix to
  separate block input ports.
- The columns of each input contains a subband for an
  independent signal.
- The input to the topmost input port is the subband containing
  the highest frequencies, and the input to the bottommost port is
  the subband containing the lowest frequencies.

This figure illustrates the difference between the two settings for a
3-level asymmetric dyadic synthesis filter bank.

**Valid Inputs to a 3-Level Asymmetric Dyadic Synthesis Filter
Bank**

For general information about the filter banks, see Dyadic Synthesis Filter Banks.

**Note**

This block always performs frame-based processing, and its inputs
must be of certain sizes. To use input subbands that do not fit the
criteria of this block, use the Two-Channel Synthesis Subband
Filter block. You can connect multiple copies of the
Two-Channel Synthesis Subband Filter block to
create a multilevel dyadic synthesis filter bank.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **Output 1** — Reconstructed signal column vector | matrix

The block outputs the reconstructed signal as a column vector or a matrix.

This table summarizes the output characteristics for both types of
inputs. For an illustration of why the output characteristics exist, see
the figure Valid Inputs to a 3-Level Asymmetric Dyadic Synthesis Filter Bank.

|  | Input = Multiple ports | Input = Single port  (Concatenated Subband Inputs) |
| --- | --- | --- |
| **Output Frame Rate** | Same as the input frame rate. | Same as the input rate (the rate of the concatenated subband inputs). |
| **Output Frame Dimensions** | - The output has the same number of columns as   the inputs. - The number of output rows depends on the   tree structure of the filter bank:  - **Asymmetric**     — The number of output rows is twice the     number of rows in the input to the topmost input     port.   - **Symmetric**     — The number of output rows is the product     of the number of input ports and the number of     rows in an input to any input port. | The output has the same number of rows and columns as the input. |

For general information about the filter banks, see Dyadic Synthesis Filter Banks.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

The parameters displayed in the block dialog box vary depending on the setting of the
**Filter** parameter. Only some of the parameters described below
are visible in the dialog box at any one time.

**Note**

To use this block to reconstruct a signal decomposed by a Dyadic Analysis Filter Bank block, all the parameters in this block
must be the same as the corresponding parameters in the Dyadic Analysis
Filter Bank block (except the **Lowpass FIR filter
coefficients** and **Highpass FIR filter
coefficients**. See the descriptions of these parameters).

### **Filter** — Type of filter used in filter bank `User-defined` (default) | `Haar` | `Daubechies` | `Symlets` | `Coiflets` | `Biorthogonal` | `Reverse Biorthogonal` | `Discrete Meyer`

To determine the highpass and lowpass FIR filters in the filter bank:

- Select `User defined` to explicitly
  specify the filter coefficients in the **Lowpass FIR filter
  coefficients** and **Highpass FIR filter
  coefficients** parameters.
- Select a wavelet such as `Biorthogonal`
  or `Daubechies` to specify a wavelet-based
  filter. The block uses the Wavelet Toolbox
  `wfilters` function to construct the filters. Extra
  parameters such as **Wavelet order** or
  **Filter order [synthesis / analysis]** become
  enabled. For a list of the supported wavelets, see the table Specifying Filters with the Filter Parameter and Related Parameters.

  You must specify the highpass and lowpass filters in the filter
  bank by setting the **Filter** parameter to one of
  the following options:

  - `User defined` — Allows
    you to explicitly specify the filters with two vectors of
    filter coefficients in the **Lowpass FIR filter
    coefficients** and **Highpass FIR
    filter coefficients** parameters. The block
    uses the same lowpass and highpass filters throughout the
    filter bank. The two filters should be halfband filters,
    where each filter passes the frequency band that the other
    filter stops. To use this block to perfectly reconstruct a
    signal decomposed by a Dyadic Analysis Filter
    Bank block, the filters in this block
    *must* be designed to perfectly
    reconstruct the outputs of the analysis filter bank. To
    learn how to design your own perfect reconstruction filters,
    see References.
  - Wavelet such as `Biorthogonal` or
    `Daubechies` — The block
    uses the specified wavelet to construct the lowpass and
    highpass filters using the Wavelet Toolbox function `wfilters`.
    Depending on the wavelet, the block might enable either the
    **Wavelet order** or **Filter
    order [synthesis / analysis]** parameter. (The
    latter parameter allows you to specify different wavelet
    orders for the analysis and synthesis filter stages.) To use
    this block to reconstruct a signal decomposed by a Dyadic Analysis Filter
    Bank block, you must set both blocks to use the
    same wavelets with the same order. You must have a
    Wavelet Toolbox license to use wavelets.

  **Specifying Filters with the Filter Parameter
  and Related Parameters**

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

### **Filter order [synthesis / analysis]** — Wavelet order for synthesis filter stage `[1 / 1]` (default) | `[1 / 3]` | `[1 / 5]` | `[2 / 2]` | `[2 / 4]` | `[2 / 6]` | `[2 / 8]` | `[3 / 1]` | `[3 / 3]` | `[3 / 5]` | `[3 / 7]` | `[3 / 9]` | `[4 / 4]` | `[5 / 5]` | `[6 / 8]`

The order of the wavelet for the synthesis and analysis filter stages. For
example, when you set the **Filter** parameter
to **Biorthogonal** and set the **Filter order [synthesis / analysis]** parameter to
`[2 / 6]`, the block calls the
`wfilters` function with input argument
`'bior2.6'`.

#### Dependencies

To enable this parameter, set the **Filter**
parameter to `Biorthogonal` or
`Reverse Biorthogonal`.

### **Wavelet order** — Wavelet order `2` (default) | positive integer

Set the order of the wavelet selected in the **Filter**
parameter.

#### Dependencies

To enable this parameter, set the **Filter** parameter to
`Daubechies`,
`Symlets`, or
`Coiflets`.

### **Lowpass FIR filter coefficients** — Lowpass FIR filter coefficients `[0.3327 0.8069 0.4599 -0.1350 -0.0854 0.0352]` (default)

Specifies coefficients used by all the lowpass filters in the filter bank using a vector
of filter coefficients (descending powers of *z*). This
parameter is enabled when you set **Filter** to
`User defined`. The lowpass filter should be a
half-band filter that passes the frequency band stopped by the filter
specified in the **Highpass FIR filter coefficients**
parameter. To perfectly reconstruct a signal decomposed by the Dyadic Analysis Filter Bank, the
filters in this block must be designed to perfectly reconstruct the outputs
of the analysis filter bank. Otherwise, the reconstruction is not perfect.
The default values of this parameter specify a perfect reconstruction filter
for the default settings of the Dyadic Analysis Filter Bank
(based on a Daubechies wavelet with wavelet order
`3`).

#### Dependencies

To enable this parameter, set the **Filter** parameter to
`User-defined`.

### **Highpass FIR filter coefficients** — Highpass FIR filter coefficients `[0.0352 0.0854 -0.1350 -0.4599 0.8069 -0.3327]` (default)

Specifies coefficients used by all the highpass filters in the filter bank using a vector
of filter coefficients (descending powers of *z*). This
parameter is enabled when you set **Filter** to
`User defined`. The highpass filter should be a
half-band filter that passes the frequency band stopped by the filter
specified in the **Lowpass FIR filter coefficients**
parameter. To perfectly reconstruct a signal decomposed by the Dyadic Analysis Filter Bank, the
filters in this block must be designed to perfectly reconstruct the outputs
of the analysis filter bank. Otherwise, the reconstruction is not perfect.
The default values of this parameter specify a perfect reconstruction filter
for the default settings of the Dyadic Analysis Filter Bank
(based on a Daubechies wavelet with wavelet order
`3`).

#### Dependencies

To enable this parameter, set the **Filter** parameter to
`User-defined`.

### **Number of levels** — Number of filter bank levels `2` (default) | positive integer

Select the number of filter bank levels. An *n*-level asymmetric
structure has *n*+1 inputs, and an
*n*-level symmetric structure has
2*n* inputs, as shown in
Multilevel Filter Banks.

### **Tree structure** — Structure of filter bank `Asymmetric` (default) | `Symmetric`

Select the structure of the filter bank: `Asymmetric`, or
`Symmetric`. See Multilevel Filter Banks for more details on
these structures.

The default setting of this parameter is
`Asymmetric` for the Dyadic Synthesis
Filter Bank block, and `Symmetric` for
the IDWT block.

### **Input** — Input `Multiple ports` (default) | `Single port`

Set to `Multiple ports` to accept each input subband at a
separate port. The topmost port accepts the subband with the highest
frequency band. Set to `Single port` to accept one
vector or matrix of concatenated subbands at a single port. For more
information, see Input port description.

The default setting of this parameter is `Multiple
ports` for the Dyadic Synthesis Filter Bank
block, and `Single port` for the
IDWT block.

When you set the **Input** parameter to
`Multiple ports`, you must provide each subband
to the block through a different input port as a vector or a matrix. You
should input the highest frequency band through the topmost port. When you
set the **Input** parameter to `Single
port`, the block input must be a vector or matrix of
concatenated subbands.

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

Reconstruct signals from subbands with smaller bandwidths and slower sample rates or compute inverse discrete wavelet transform (IDWT)

You can configure this block to compute the inverse discrete wavelet transform (IDWT) or
reconstruct a signal from subbands with smaller bandwidths and slower sample rates. When
the block computes the inverse discrete wavelet transform (IDWT) of the input, the
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

To use a dyadic synthesis filter bank to perfectly reconstruct the output of a
dyadic analysis filter bank, the number of levels and tree structures of both filter
banks must be the same. In addition, the filters in the synthesis filter bank must
be designed to perfectly reconstruct the outputs of the analysis filter bank.
Otherwise, the reconstruction is not perfect. For an example that shows perfect
reconstruction, see Wavelet Reconstruction and Noise Reduction.

This block automatically computes wavelet-based perfect reconstruction filters
when the wavelet selection in the **Filter** parameter of this
block is the same as the **Filter** parameter setting of the
corresponding Dyadic Analysis Filter Bank block. The
use of wavelets requires a Wavelet Toolbox license. To learn how to design your own perfect reconstruction
filters, see References.
