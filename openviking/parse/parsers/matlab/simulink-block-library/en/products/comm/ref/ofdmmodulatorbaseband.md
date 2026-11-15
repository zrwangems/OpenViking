---
type: simulink-block
title: 'OFDM Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / OFDM Modulation'
documentation_page: 'ofdmmodulatorbaseband'
documentation_source_path: 'ref/ofdmmodulatorbaseband.html'
language: en
---

# OFDM Modulator Baseband

## Ports

### Input

### **In** — Input baseband signal array

Input baseband signal, specified as an *N*DataSC-by-*N*Sym-by-*N*Streams array.

- *N*DataSC is the
  number of data subcarriers, such that *N*DataSC
  = *N*FFT −
  *N*leftG −
  *N*rightG
  − *N*DCNull
  − *N*Pilot −
  *N*CustNull.

  - *N*FFT
    is the number of subcarriers, as specified by
    **FFT length**.
  - *N*leftG
    is the number of subcarriers in the left guard
    band, as specified by the first element of
    **Number of guard bands**.
  - *N*rightG
    is the number of subcarriers in the right guard
    band, as specified by the second element of
    **Number of guard bands**.
  - *N*DCNull
    is the number of subcarriers in the DC null,
    specified as `0` or
    `1` based on the selection of
    **Insert DC null**.
  - *N*Pilot
    is the number of pilot subcarriers in each
    symbol.

    - When you select **Pilot input port**,
      *N*Pilot =
      `size`(**Pilot subcarrier
      indices**,`1`).
    - When you do not select **Pilot input port**,
      *N*Pilot =
      `0`.
  - *N*CustNull
    is the number of subcarriers used for custom
    nulls. To use custom nulls, you must specify
    **Pilot subcarrier indices** as a 3D
    array.
- *N*Sym is the
  number of symbols, as specified by **Number of OFDM symbols**.
- *N*Streams is the
  number of transmit streams, as specified by **Number of transmit antennas**, and must be
  less than or equal to the physical number of transmit
  antennas.

For more information, see Subcarrier Allocation, Guard Bands, and Guard Intervals.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes

### **Pilot** — Pilot signal array

Pilot signal, specified as an
*N*Pilot-by-*N*Sym-by-*N*Streams
array.

- *N*Pilot is the
  number of pilot subcarriers in each symbol, determined by
  `size`(**Pilot subcarrier
  indices**,`1`).
- *N*Sym is the
  number of OFDM symbols, as specified by **Number of OFDM symbols**.
- *N*Streams is the
  number of transmit streams, as specified by **Number of transmit antennas**, and must be
  less than or equal to the physical number of transmit
  antennas.

For more information, see Subcarrier Allocation, Guard Bands, and Guard Intervals.

#### Dependencies

This port appears when you select **Pilot input port**.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes
### Output

### **Out** — OFDM-modulated baseband signal matrix

OFDM-modulated baseband signal, returned as an (*osf* ×
*N*Out)-by-*N*Streams matrix of the same data type as the input signal.

- *osf* is the oversampling factor, as
  determined by `OversamplingFactor`.
- When **Cyclic prefix length** is a scalar,
  *N*CP =
  `CyclicPrefixLength` and *N*Out
  = *N*Sym ×
  (*N*FFT +
  *N*CP).
- When **Cyclic prefix length** is a row vector,
  *N*CPTotal =
  `sum`(**Cyclic prefix length**) and *N*Out
  = (*N*Sym ×
  *N*FFT) +
  *N*CPTotal.
- *N*Sym is the
  number of symbols, as specified by **Number of OFDM symbols**.
- *N*FFT is the
  number of subcarriers, as specified by **FFT length**.
- *N*Streams in the
  number of transmit streams, as specified by **Number of transmit antennas**, and must be
  less than or equal to the physical number of transmit
  antennas.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **FFT length** — Number of FFT points 64 (default) | positive integer

Number of FFT points, specified as a positive, integer scalar. The length
of the FFT must be greater than or equal to 8 and is equivalent to the
number of subcarriers.

### **Number of guard bands** — Number of subcarriers allocated to left and right guard bands `[6; 5]` (default) | 2-by-1 integer-valued vector

Number of subcarriers allocated to the left and right guard bands, specified as a 2-by-1
integer-valued vector. The number of left and right guard-band subcarriers,
[*N*leftG;
*N*rightG], must fall within [0,⌊*N*FFT/2⌋ −
1], where *N*FFT is
the total number of subcarriers in the OFDM signal specified by **FFT
length**. For more information, see Subcarrier Allocation, Guard Bands, and Guard Intervals.

### **Insert DC null** — Option to insert DC null `off` (default) | `on`

Select this parameter to insert a null on the DC subcarrier. When inserted, the null DC
subcarrier is at the center of the frequency band and has the index value:

- (*N*FFT / 2) + 1 when
  *N*FFT is
  even.
- (*N*FFT + 1) / 2 when
  *N*FFT is
  odd.

*N*FFT is the total
number of subcarriers in the OFDM signal, as specified by **FFT
length**.

### **Pilot input port** — Option to input pilot subcarriers `off` (default) | `on`

Select this parameter to add a port to input pilot subcarriers. When you set this
parameter to:

- `off` — The input data port, **In**, may include embedded pilot information but the
  block does not assign pilot subcarrier indices.
- `on` — The block assigns subcarriers
  specified by **Pilot subcarrier indices** for pilot modulation
  of the signal at the **Pilot** input port.

### **Pilot subcarrier indices** — Indices of pilot subcarrier locations `[12; 26; 40; 54]` (default) | column vector | matrix | 3D array

Indices of the pilot subcarrier locations, specified as a column vector,
matrix, or 3D array with integer-element values in the range

[NleftG+1, NFFT/2]∪[NFFT/2+2, NFFT−NrightG],

where *N*FFT is
the total number of subcarriers specified by **FFT
length**, and *N*leftG
and *N*rightG are the left and right
guard bands specified by **Number of
guard bands**.

You can assign the *N*Pilot pilot carrier indices
to the same or different *N*Sym
subcarriers for each symbol, and across
*N*Streams transmit streams.

- When the pilot indices are the same for every symbol and
  transmit stream, the parameter has dimensions NPilot-by-1.
- When the pilot indices vary across symbols, the parameter has
  dimensions of *N*Pilot-by-*N*Sym.
- If the **Pilot** port has only one symbol but the block
  configuration assigns multiple transmit streams, the parameter
  has dimensions of *N*Pilot-by-1-by-*N*Streams.
- If the indices vary across the number of symbols and transmit
  streams, the parameter has dimensions of *N*Pilot-by-*N*Sym-by-*N*Streams.

**Tip**

To minimize interference between transmissions across more than
one transmit stream, the pilot indices per symbol must be mutually
distinct across the streams.

#### Dependencies

This parameter applies when you select **Pilot
input port**.

### **Cyclic prefix length** — Length of cyclic prefix 16 (default) | positive integer | row vector

Length of the cyclic prefix for each OFDM symbol, specified as a positive, integer-valued
scalar or row vector containing **Number of
OFDM symbols** elements. The cyclic prefix length must be in
the range [0, *N*FFT], where
*N*FFT is the total number of
subcarriers in the OFDM signal specified by **FFT
length**. When you specify the cyclic prefix length as a:

- Scalar — The cyclic prefix length is the same for all symbols
  through all streams.
- Row vector — The cyclic prefix length may vary across symbols
  but does not vary across streams.

### **Apply raised cosine windowing between OFDM symbols** — Option to apply raised cosine window between OFDM symbols `off` (default) | `on`

Select this parameter to apply raised cosine windowing between OFDM
symbols.

To reduce the power of out-of-band subcarriers caused by spectral regrowth, apply
windowing. For more information, see OFDM Raised Cosine Windowing.

### **Window length** — Length of raised cosine window 1 (default) | positive integer

Length of raised cosine window, specified as a positive, integer scalar. This value must
be less than or equal to the minimum cyclic prefix length specified by
**Cyclic
prefix length**. For example, in a configuration of four
symbols with cyclic prefix lengths 12, 14, 16, and 18, the window length
must be less than or equal to 12.

#### Dependencies

This parameter applies when you select **Apply
raised cosine windowing between OFDM symbols**.

### **Oversampling factor** — Oversampling factor `1` (default) | positive scalar

Oversampling factor, specified as a positive scalar. The oversampling
factor must satisfy these constraints:

- (**Oversampling factor**×**FFT length**) must be an integer value.
- (**Oversampling factor**×**Cyclic prefix length**) must be an integer
  value.
- If you select **Apply raised cosine windowing between OFDM
  symbols**, (**Oversampling
  factor**×**Window length**) must be an integer value.

**Tip**

If you set the oversampling factor to a noninteger rational number, specify a fractional value
rather than a decimal value. For example, with an FFT length of `12` and an
oversampling factor of `4/3`, their product is the integer
`16`. However, rounding `4/3` to
`1.333` when setting the oversampling factor results in a noninteger
product of `15.9960`, which results in a code error.

### **Number of OFDM symbols** — Number of OFDM symbols 1 (default) | positive integer

Number of OFDM symbols in the time-frequency grid, specified as a positive, integer
scalar.

### **Number of transmit antennas** — Number of transmit streams 1 (default) | positive integer

Number of transmit streams, specified as a positive, integer scalar less
than or equal to `64`. The value must be less than or equal
the physical number of transmit antennas.

### **Simulate using** — Type of simulation to run `Code generation` (default) | `Interpreted execution`

Type of simulation to run, specified as `Code generation` or
`Interpreted execution`.

- `Code generation` — Simulate the model by using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The model reuses the C code
  for subsequent simulations unless the model changes. This option requires
  additional startup time, but the speed of the subsequent simulations is
  faster than with the `Interpreted execution`
  option.
- `Interpreted execution` — Simulate the model by
  using the MATLAB® interpreter. This option shortens startup time, but the speed
  of subsequent simulations is slower than with the `Code
  generation` option. In this mode, you can debug the source
  code of the block.

For more information, see Interpreted Execution vs. Code Generation (Simulink).

## Libraries

Communications Toolbox / Modulation / Digital Baseband Modulation / OFDM

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014a**

### R2023a: Adds support for oversampling

`OFDM Modulator Baseband` now supports oversampling.

## Description

Modulate using OFDM method

The OFDM Modulator Baseband block modulates a frequency domain signal by using the
orthogonal frequency division multiplexing (OFDM) method. For more information, see
Orthogonal Frequency Division Multiplexing. The output is a
baseband representation of the OFDM-modulated signal.

This icon shows the block with all ports enabled.

OFDM Modulator block showing optional pilot input port
