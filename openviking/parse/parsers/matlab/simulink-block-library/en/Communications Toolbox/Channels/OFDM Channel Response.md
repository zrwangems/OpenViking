---
type: simulink-block
title: 'OFDM Channel Response'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Channels'
documentation_page: 'ofdmchannelresponseblock'
documentation_source_path: 'ref/ofdmchannelresponseblock.html'
language: en
---

# OFDM Channel Response

## Ports
```yaml
ports:
- name: Path gains
  summary: Channel path gains array
  direction: input
  data_types: single | double
- name: Path filters
  summary: Channel path filter coefficients matrix
  direction: input
  data_types: single | double
- name: Offset
  summary: Timing offset scalar
  direction: input
  data_types: double | single
- name: hEst
  summary: Frequency response array
  direction: output
```

### Input

### **Path gains** — Channel path gains array

Channel path gains, specified as an
*N*S-by-*N*P-by-T-by-*N*R
array of values.

- *N*S is the number of
  samples.
- *N*P is the number of paths.
- *N*T is the number of transmit
  antennas.
- *N*R is the number of receive
  antennas.

The channel path gains follow the definition of channel path gains as calculated
and output by the fading channel System objects. For example, see MIMO Fading Channel or SISO Fading
Channel. This block assumes that the path gains sample rate matches the OFDM
sample rate.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Path filters** — Channel path filter coefficients matrix

Channel path filter coefficients, specified as an
*N*P-by-*N*H
matrix of values.

- *N*P is the number of paths.
- *N*H is the number of impulse
  response samples.

The channel path filter coefficient matrix is used to convert path gains to
channel filter tap gains for each sample and each pair of transmit and receive
antennas. The channel path filter coefficients follow the definition of channel path
filter coefficients as calculated by the `info` object function of the fading channel System objects.

The channel path gains follow the definition of channel path gains as calculated
and output by the fading channel System objects. For example, see MIMO Fading Channel or SISO Fading
Channel.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Offset** — Timing offset scalar

Timing offset in samples, specified as a nonnegative, integer scalar.

#### Dependencies

- To enable this input port, select the **Enable timing
  offset input port** parameter.

**Data Types:** `double` | `single`
### Output

### **hEst** — Frequency response array

Frequency response, returned as an
*N*SC-by-*N*Symbols-by-*N*T-by-*N*R
array.

- *N*SC is the number of OFDM
  subcarriers and equals the length of **Active
  subcarrier indices**.
- *N*Symbols is the number of whole
  OFDM symbols contained in **Path
  gains**. Specifically, floor(*N*S/(*N*FFT
  + *L*CP)).

  - *N*S is the number of samples
    in **Path
    gains**
  - *N*FFT is the value of
    **FFT
    length**
  - *L*CP is the value of
    **Cyclic
    prefix length**.
- *N*T is the number of transmit
  antennas.
- *N*R is the number of receive
  antennas.

- The returned frequency response corresponds to an OFDM symbol timing alignment
  at the receiver that uses the timing offset:

  - Provided by the **Offset**
    port when **Enable timing
    offset input port** is selected
  - Between the OFDM transmitter and the OFDM receiver as computed by the
    `channelDelay` function using **Path
    gains** and **Path
    filters** as inputs when **Enable timing
    offset input port** is not selected
## Parameters
```yaml
parameters:
- name: FFT length
  summary: FFT length 512 (default) | positive integer
  group: ''
- name: Cyclic prefix length
  summary: Cyclic prefix length of one OFDM symbol 16 (default) | nonnegative integer
  group: ''
- name: Active subcarrier indices
  summary: Number of active subcarriers 1:512 (default) | positive integer | column vector
  group: ''
- name: Enable timing offset input port
  summary: Option to add input port for timing offset off (default) | on
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **FFT length** — FFT length `512` (default) | positive integer

FFT length, specified as a positive, integer scalar. The FFT length must align with
that of the OFDM-modulated signal.

### **Cyclic prefix length** — Cyclic prefix length of one OFDM symbol `16` (default) | nonnegative integer

Cyclic prefix length of one OFDM symbol, specified as a nonnegative, integer scalar
with a value less than **FFT
length**.

### **Active subcarrier indices** — Number of active subcarriers `1:512` (default) | positive integer | column vector

Number of active subcarriers, specified as a positive, integer scalar or column
vector of values in the range [`1`, **FFT
length**].

### **Enable timing offset input port** — Option to add input port for timing offset `off` (default) | `on`

Select this parameter to add an input port to input timing offset.

- `on` — Adds the **Offset** input port to
  specify the timing offset for channel response estimation.
- `off` — The block uses the **Path gains**
  and **Path
  filters** inputs to estimate the timing offset for OFDM channel response
  estimation.

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

Communications Toolbox / Channels

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Calculate OFDM channel response

The OFDM Channel Response block calculates the OFDM channel response in the frequency
domain by using perfect information from the channel. For more information, see OFDM Channel Response.

This icon shows the block with all ports enabled.

OFDM Channel Response block showing all input ports (path gains, path filters, and offset) and the output port (hEst).
