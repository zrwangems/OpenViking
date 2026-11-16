---
type: simulink-block
title: 'OFDM Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / OFDM Modulation'
documentation_page: 'ofdmdemodulatorbaseband'
documentation_source_path: 'ref/ofdmdemodulatorbaseband.html'
language: en
---

# OFDM Demodulator Baseband

## Ports

### Input

### **In** — OFDM-modulated baseband signal matrix

OFDM-modulated baseband signal, specified as an (*osf* ×
*N*In)-by-*N*Streams matrix.

- *osf* is the oversampling factor, as
  determined by **Oversampling factor**.
- When `CyclicPrefixLength` is a scalar,
  *N*CP =
  **Cyclic prefix length** and *N*In
  = *N*Sym ×
  (*N*FFT +
  *N*CP).
- When **Cyclic prefix length** is a row vector,
  *N*CPTotal =
  `sum`(**Cyclic prefix length**) and *N*In
  = (*N*Sym ×
  *N*FFT) +
  *N*CPTotal.
- *N*Sym is the
  number of symbols, as specified by **Number of OFDM symbols**.
- *N*FFT is the
  number of subcarriers, as specified by **FFT length**.
- *N*Streams is the
  number of receive streams specified by **Number of receive antennas** and must be less
  than or equal to the physical number of receive
  antennas.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes
### Output

### **Out** — Output baseband signal matrix | 3D array

Output baseband signal, returned as a matrix or
*N*DataSC-by-*N*Sym-by-*N*Streams
array of the same data type as the input signal. The output reduces to a
matrix when *N*Streams is
`1`.

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
    `1` by selection of **Remove DC carrier**.
  - *N*Pilot
    is the number of pilot subcarriers in each
    symbol.

    - When you select **Pilot output port**,
      *N*Pilot =
      `size`(**Pilot subcarrier
      indices**,`1`).
    - When you do not select **Pilot output port**,
      *N*Pilot =
      `0` for the calculation of
      *N*Out.
  - *N*CustNull
    is the number of subcarriers used for custom
    nulls. To use custom nulls, you must specify
    **Pilot subcarrier indices** as a 3D
    array.
- *N*Sym is the
  number of symbols, as specified by **Number of OFDM symbols**.
- *N*Streams is the
  number of receive streams, as specified by **Number of receive antennas** and is less than
  or equal to the physical number of receive antennas..

For more information, see Subcarrier Allocation, Guard Bands, and Guard Intervals.

### **Pilot** — Pilot signal 3D array

Pilot signal, returned as an
*N*Pilot-by-*N*Sym-by-*N*Streams array.

- *N*Pilot is the
  number of pilot subcarriers in each symbol, as determined by
  `size`(**Pilot subcarrier
  indices**,`1`)
- *N*Sym is the
  number of symbols, as specified by **Number of OFDM symbols**.
- *N*Streams is the
  number of receive streams, as specified by **Number of receive antennas** and is less than
  or equal to the physical number of receive antennas..

#### Dependencies

To return this output, select **Pilot output port**.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **FFT length** — Number of FFT points 64 (default) | positive integer

Number of FFT points, specified as a positive, integer scalar. The length
of the FFT must be greater than or equal to 8 and is equivalent to the
number of subcarriers.

### **Number of guard bands** — Number of subcarriers allocated to left and right guard bands `[6; 5]` (default) | 2-by-1 integer vector

Number of subcarriers allocated to the left and right guard bands, specified as a 2-by-1
integer vector. The number of left and right guard-band subcarriers,
[*N*leftG;
*N*rightG], must fall within [0,⌊*N*FFT/2⌋ −
1], where *N*FFT is
the total number of subcarrier in the OFDM signal specified by **FFT
length**. For more information, see Subcarrier Allocation, Guard Bands, and Guard Intervals.

### **Remove DC carrier** — Option to remove DC subcarrier `off` (default) | `on`

Select this parameter to remove the null DC subcarrier. The null DC subcarrier is located
at the center of the frequency band and has the index value:

- (*N*FFT / 2) + 1 when
  *N*FFT is
  even.
- (*N*FFT + 1) / 2 when
  *N*FFT is
  odd.

*N*FFT is the total
number of subcarriers in the OFDM signal specified by **FFT
length**.

### **Pilot output port** — Option to output pilot subcarriers `off` (default) | `on`

Select this parameter to add a port to output pilot subcarriers. When you set this
parameter to:

- `off` — Pilot information may be present but
  remains embedded in the output data.
- `on` — The block separates the subcarriers,
  specified by **Pilot subcarrier indices**, from the output data
  and outputs the demodulated pilot signal to the **Pilot** port.

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
*N*TxStreams transmit streams.

- When the pilot indices are the same for every symbol and
  transmit antenna, the parameter has dimensions of NPilot-by-1.
- When the pilot indices vary across symbols, the parameter has
  dimensions of *N*Pilot-by-*N*Sym.
- If the received signal assigned one symbol across multiple
  transmit streams, the parameter has dimensions of *N*Pilot-by-1-by-*N*TxStreams.
- If the indices vary across the number of symbols and transmit
  streams, the parameter has dimensions of *N*Pilot-by-*N*Sym-by-*N*TxStreams.

**Tip**

To minimize interference between transmissions across more than
one transmit stream, the pilot indices per symbol must be mutually
distinct across the streams.

#### Dependencies

This parameter applies when you select **Pilot
output port**.

### **Cyclic prefix length** — Length of cyclic prefix `16` (default) | positive integer | row vector

Length of the cyclic prefix for each OFDM symbol, specified as a positive, integer scalar
or row vector containing **Number of
OFDM symbols** elements. The cyclic prefix length must be in
the range [0, *N*FFT], where
*N*FFT is the total number of
subcarriers in the OFDM signal specified by **FFT
length**. When you specify the cyclic prefix length as a:

- Scalar — The cyclic prefix length is the same for all symbols
  through all streams.
- Row vector — The cyclic prefix length may vary across symbols
  but does not vary across streams.

### **Oversampling factor** — Oversampling factor `1` (default) | positive scalar

Oversampling factor, specified as a positive scalar. The oversampling
factor must satisfy these constraints:

- (**Oversampling factor**×**FFT length**) must be an integer value.
- (**Oversampling factor**×**Cyclic prefix length**) must be an integer
  value.

**Tip**

If you set the oversampling factor to a noninteger rational number, specify a fractional value
rather than a decimal value. For example, with an FFT length of `12` and an
oversampling factor of `4/3`, their product is the integer
`16`. However, rounding `4/3` to
`1.333` when setting the oversampling factor results in a noninteger
product of `15.9960`, which results in a code error.

### **Number of OFDM symbols** — Number of OFDM symbols `1` (default) | positive integer

Number of OFDM symbols in the time-frequency grid, specified as a
positive, integer scalar.

### **Number of receive antennas** — Number of receive streams 1 (default) | positive integer

Number of receive streams to receive the OFDM modulated signal, specified
as a positive, integer scalar less than or equal to `64`.
The value must be less than or equal the physical number of receive
antennas.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Type of simulation to run, specified as `Interpreted
execution` or `Code generation`.

- `Interpreted execution` — Simulate the model by
  using the MATLAB® interpreter. This option requires less startup time, but the
  speed of subsequent simulations is slower than with the `Code
  generation` option. In this mode, you can debug the source
  code of the block.
- `Code generation` — Simulate the model by using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The model reuses the C code
  for subsequent simulations unless the model changes. This option requires
  additional startup time, but the speed of the subsequent simulations is
  faster than with the `Interpreted execution`
  option.

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

`OFDM Demodulator Baseband` now supports oversampling.

## Description

Demodulate using OFDM method

The OFDM Demodulator Baseband block demodulates an input time domain signal by using the orthogonal
frequency division multiplexing (OFDM) method. For more information, see OFDM Demodulation. The block accepts a
single input and has one or two output ports, depending on the status of **Pilot output
port**.

This icon shows the block with all ports enabled.OFDM Demodulator Baseband block showing optional Pilot output port
