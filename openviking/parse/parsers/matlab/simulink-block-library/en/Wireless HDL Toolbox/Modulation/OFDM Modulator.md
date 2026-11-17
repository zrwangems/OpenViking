---
type: simulink-block
title: 'OFDM Modulator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'ofdmmodulator'
documentation_source_path: 'ref/ofdmmodulator.html'
language: en
---

# OFDM Modulator

## Ports
```yaml
ports:
- name: data
  summary: Input data scalar | column vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | signed fixed point
- name: valid
  summary: Indicates valid input data scalar
  direction: input
  data_types: Boolean
- name: FFTLen
  summary: Length of FFT scalar
  direction: input
  data_types: single | double | uint8 | uint16 | uint32 | unsigned fixed point
- name: CPLen
  summary: Length of cyclic prefix scalar
  direction: input
  data_types: single | double | uint8 | uint16 | uint32 | unsigned fixed point
- name: numLgSc
  summary: Number of left guard carriers of OFDM symbol scalar
  direction: input
  data_types: single | double | uint8 | uint16 | uint32 | unsigned fixed point
- name: numRgSc
  summary: Number of right guard carriers of OFDM symbol scalar
  direction: input
  data_types: single | double | uint8 | uint16 | uint32 | unsigned fixed point
- name: reset
  summary: Clear internal states scalar
  direction: input
  data_types: Boolean
- name: winLen
  summary: Length of window scalar
  direction: input
  data_types: single | double | uint8 | uint16 | uint32 | unsigned fixed point
- name: data
  summary: Modulated output data scalar | column vector
  direction: output
  data_types: single | double | int8 | int16 | int32 | signed fixed point
- name: valid
  summary: Indicates valid output data scalar
  direction: output
  data_types: Boolean
- name: ready
  summary: Indicates block is ready scalar
  direction: output
  data_types: Boolean
```

### Input

### **data** — Input data scalar | column vector

Input data, specified as a scalar or column vector of real or complex values. The
vector size must be a power of 2 and in the range from 1 to 64, and less than or equal
to the FFT length. For more information on how to specify vector inputs, see Specifying Vector Input.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**Complex Number Support:** Yes

### **valid** — Indicates valid input data scalar

Indicates valid input data, specified as a scalar.

This port is a control signal that indicates when the sample from the
**data** input port is valid. When this value is
`1`, the block captures the values on the **data**
input port. When this value is `0`, the block ignores the values on
the **data** input port.

**Data Types:** `Boolean`

### **FFTLen** — Length of FFT scalar

Length of the FFT, specified as a scalar. The FFT length must be power of 2 and in
the range from 8 to 65,536. This value must be less than or equal to the
**Maximum FFT length** parameter value.

To support the minimum FFT length of 8, the **FFTLen** data type
must be `fixdt(0,k,0)`, where *k* is greater than or
equal to 4.

#### Dependencies

To enable this port, set the **OFDM parameters source**
parameter to `Input port`.

**Data Types:** `single` | `double` | `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### **CPLen** — Length of cyclic prefix scalar

Length of the cyclic prefix, specified as a scalar in the range from 0 to
**FFTLen**.

To support the minimum FFT length of 8, the **CPLen** data type
must be `fixdt(0,k,0)`, where *k* is greater than or
equal to 4.

#### Dependencies

To enable this port, set the **OFDM parameters source**
parameter to `Input port`.

**Data Types:** `single` | `double` | `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### **numLgSc** — Number of left guard carriers of OFDM symbol scalar

Number of left guard carriers of the OFDM symbol, specified as a scalar in the
range from 0 to (**FFTLen**/2) – 1.

To support the minimum FFT length of 8, the **numLgSc** data type
must be `fixdt(0,k,0)`, where *k* is greater than or
equal to 2.

#### Dependencies

To enable this port, set the **OFDM parameters source**
parameter to `Input port`.

**Data Types:** `single` | `double` | `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### **numRgSc** — Number of right guard carriers of OFDM symbol scalar

Number of right guard carriers of the OFDM symbol, specified as a scalar in the
range from 0 to (**FFTLen**/2) – 1.

To support the minimum FFT length of 8, the **numRgSc** data type
must be `fixdt(0,k,0)`, where *k* is greater than or
equal to 2.

#### Dependencies

To enable this port, set the **OFDM parameters source**
parameter to `Input port`.

**Data Types:** `single` | `double` | `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### **reset** — Clear internal states scalar

Clear internal states, specified as a Boolean scalar. When this value is
`1`, the block stops the current calculation and clears all
internal states.

#### Dependencies

To enable this port, select the **Enable reset input port**
parameter.

**Data Types:** `Boolean`

### **winLen** — Length of window scalar

Length of the window for overlap-adding of adjacent OFDM symbols, specified as a
scalar in the range from 1 to **Maximum window length**.

#### Dependencies

To enable this port, set the **OFDM parameters source**
parameter to `Input port`.

**Data Types:** `single` | `double` | `uint8` | `uint16` | `uint32` | `unsigned fixed point`
### Output

### **data** — Modulated output data scalar | column vector

Modulated output data, returned as a complex-valued scalar or a column vector. The
data type of the output is dependent on the data type of the input
**data** port.

- When you set the **OFDM parameters source** parameter to
  `Property` and clear the **Divide butterfly
  outputs by two** parameter, the output word length increases by
  log2(*FFTLength*) bits.
- When you set the **OFDM parameters source** parameter to
  `Input port` and clear the **Divide butterfly
  outputs by two** parameter, the output word length increases by
  log2(*MaxFFTLength*) bits.

To avoid overflow, select the **Divide butterfly outputs by two**
parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**Complex Number Support:** Yes

### **valid** — Indicates valid output data scalar

Indicates valid output data, returned as a scalar.

This port is a control signal that indicates when the **data**
output port is valid. The block sets this value to `1` when the data
samples are available on the **data** output port.

**Data Types:** `Boolean`

### **ready** — Indicates block is ready scalar

Indicates block is ready, returned as a scalar.

This is a control signal that indicates when the block is ready for new input
data. When this value is `1`, the block accepts input data in the
next time step. When this value is `0`, the block ignores input data
in the next time step.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: OFDM parameters source
  summary: Source of OFDM parameters Property (default) | Input port
  group: Main
- name: Maximum FFT length
  summary: Maximum length of FFT length 64 (default) | power of 2 in range from 8 to 65,536
  group: Main
- name: FFT length
  summary: Length of FFT 64 (default) | power of 2 in range from 8 to 65, 536
  group: Main
- name: Cyclic prefix length
  summary: Length of cyclic prefix 16 (default) | integer in range from 0 to *FFTLength*
  group: Main
- name: Number of left guard subcarriers
  summary: Number of guard band subcarriers in left extreme of OFDM symbol 6 (default) | integer in range from 0 to (*FFTLength*/2)
    – 1
  group: Main
- name: Number of right guard subcarriers
  summary: Number of guard band subcarriers in right extreme of OFDM symbol 5 (default) | integer in range from 0 to (*FFTLength*/2)
    – 1
  group: Main
- name: Insert DC Null
  summary: Option to insert DC null on (default) | off
  group: Main
- name: Enable reset input port
  summary: Reset signal off (default) | on
  group: Main
- name: Windowing
  summary: Spectral growth reduction off (default) | on
  group: Main
- name: Window length
  summary: Length of window 4 (default) | even integer in range from 1 to Cyclic prefix length
  group: Main
- name: Maximum window length
  summary: Maximum length of window 8 (default) | integer in the range from 1 to CPLen
  group: Main
- name: Divide butterfly outputs by two
  summary: Divide FFT butterfly outputs by two on (default) | off
  group: IFFT Parameters
- name: Rounding Method
  summary: Rounding mode for internal fixed-point calculations Floor (default) | Ceiling | Convergent | Nearest | Round |
    Zero
  group: IFFT Parameters
```

### Main

### **OFDM parameters source** — Source of OFDM parameters `Property` (default) | `Input port`

You can set OFDM parameters with an input port or by selecting a value for the
parameter.

Select `Property` to enable the **FFT
length**, **Cyclic prefix length**, **Number of
left guard subcarriers**, and **Number of right guard
subcarriers** parameters.

Select `Input port` to enable the
**FFTLen**, **CPLen**,
**numLgSc**, and **numRgSc** input ports and the
**Maximum FFT length** parameter. The **Maximum
FFT length** parameter sets the upper bound of the range of valid values
for the **FFTLen** input port.

### **Maximum FFT length** — Maximum length of FFT length `64` (default) | power of 2 in range from 8 to 65,536

Specify the maximum length of the FFT.

#### Dependencies

To enable this parameter, set the **OFDM parameters source**
parameter to `Input port`.

### **FFT length** — Length of FFT `64` (default) | power of 2 in range from 8 to 65, 536

Specify the FFT length.

When you set the **OFDM parameters source** parameter to
`Property`, the block uses the **FFT
length** value as the maximum FFT length.

#### Dependencies

To enable this parameter, set the **OFDM parameters source**
parameter to `Property`.

### **Cyclic prefix length** — Length of cyclic prefix `16` (default) | integer in range from 0 to *FFTLength*

Specify the length of the cyclic prefix.

#### Dependencies

To enable this parameter, set the **OFDM parameters source**
parameter to `Property`.

### **Number of left guard subcarriers** — Number of guard band subcarriers in left extreme of OFDM symbol `6` (default) | integer in range from 0 to (*FFTLength*/2) – 1

Specify the number of left guard subcarriers.

#### Dependencies

To enable this parameter, set the **OFDM parameters source**
parameter to `Property`.

### **Number of right guard subcarriers** — Number of guard band subcarriers in right extreme of OFDM symbol `5` (default) | integer in range from 0 to (*FFTLength*/2) – 1

Specify the number of right guard subcarriers.

#### Dependencies

To enable this parameter, set the **OFDM parameters source**
parameter to `Property`.

### **Insert DC Null** — Option to insert DC null `on` (default) | `off`

Select this parameter to insert a null on the DC subcarrier.

### **Enable reset input port** — Reset signal `off` (default) | `on`

Select this parameter to enable the **reset** input port.

### **Windowing** — Spectral growth reduction `off` (default) | `on`

Select this parameter to perform a windowing operation that reduces spectral
growth based on the specified window length. Clear this parameter to disable the
windowing operation. For more information about windowing, see Windowing.

### **Window length** — Length of window `4` (default) | even integer in range from 1 to **Cyclic prefix length**

Specify the window length to overlap-add adjacent OFDM symbols.

#### Dependencies

To enable this parameter, set the **OFDM parameters source**
parameter to `Property` and select the
**Windowing** parameter.

### **Maximum window length** — Maximum length of window `8` (default) | integer in the range from 1 to **CPLen**

Specify the maximum window length.

#### Dependencies

To enable this parameter, set the **OFDM parameters source**
parameter to `Input port` and select the
**Windowing** parameter.

### IFFT Parameters

### **Divide butterfly outputs by two** — Divide FFT butterfly outputs by two `on` (default) | `off`

This parameter controls the scaling option of the IFFT  block inside the OFDM Modulator block.

When you select this parameter, the FFT implements an overall
1/*N* scale factor by dividing the output of each butterfly
multiplication by two. This adjustment keeps the output of the IFFT in the same
amplitude range as its input. If you clear this parameter, the block avoids overflow
by increasing the word length by one bit after each butterfly multiplication.

### **Rounding Method** — Rounding mode for internal fixed-point calculations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

This parameter specifies the type of rounding mode for internal fixed-point
calculations. For more information about rounding modes, see Rounding Modes. When the input is any integer data
type or fixed-point data type, the FFT algorithm uses fixed-point arithmetic for
internal calculations. This parameter does not apply when the input is of data type
`single` or `double`. Rounding applies to
twiddle-factor multiplication and scaling operations.
## Libraries

Wireless HDL Toolbox / Modulation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink® accelerator and rapid accelerator modes and for DPI component generation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

This block does not have any HDL Block
Properties.

## Version History

**Introduced in R2020a**

## Description

Modulate frequency-domain OFDM subcarriers to time-domain samples for custom communication protocols

The OFDM Modulator block modulates frequency-domain orthogonal frequency
division multiplexing (OFDM) subcarriers to time-domain samples based on the OFDM parameters.
The block supports 5G new radio (NR) standard, long term evolution (LTE) [1], wireless local area network
(WLAN 802.11a/g/n/ac) [2], WiMAX, digital video
broadcast (DVB), and digital audio broadcast (DAB) standards.

The block accepts input data along with a valid control signal and these OFDM parameters:
FFT length, CP length, and the number of right and left guard subcarriers. The block outputs
modulated data along with valid and ready controls signals. The block samples the
corresponding OFDM parameters only when the **ready** port is
`1` (high) and when the first **valid** port of each OFDM
symbol is `1` (high).

The block supports scalar and vector inputs. You can use a vector input to increase the
data throughput and achieve a giga-sample-per-second (GSPS) throughput. The block supports
windowing for scalar and vector inputs to reduce the spectral regrowth, or adjacent channel
leakage ratio (ACLR), of an OFDM signal. The block provides an interface and architecture
suitable for HDL code generation and hardware deployment.
