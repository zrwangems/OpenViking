---
type: simulink-block
title: 'OFDM Demodulator'
family: 'wireless-hdl'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'ofdmdemodulator'
documentation_source_path: '../wireless-hdl/ref/ofdmdemodulator.html'
language: en
---

# OFDM Demodulator

## Ports

### Input

### **data** — Input data scalar | column vector

Input data, specified as a scalar or column vector of real or complex values. The
vector size must be a power of 2, in the range from 1 to 64, and less than or equal to
the FFT length.

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

Number of left guard carriers of OFDM symbol, specified as a scalar in the range
from 0 to (**FFTLen**/2) – 1.

To support the minimum FFT length of 8, the **numLgSc** data type
must be `fixdt(0,k,0)`, where *k* is greater than or
equal to 2.

#### Dependencies

To enable this port, set the **OFDM parameters source**
parameter to `Input port`.

**Data Types:** `single` | `double` | `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### **numRgSc** — Number of right guard carriers of OFDM symbol scalar

Number of right guard carriers of OFDM symbol, specified as a scalar in the range
from 0 to (**FFTLen**/2) – 1.

To support the minimum FFT length of 8, the **numRgSc** data type
must be `fixdt(0,k,0)`, where *k* is greater than or
equal to 2.

#### Dependencies

To enable this port, set the **OFDM parameters source**
parameter to `Input port`.

**Data Types:** `single` | `double` | `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### **CPFraction** — CP Fraction real positive scalar

CP Fraction, specified as a real positive scalar in the range [0, 1].

To support maximum precision, the **CPFraction** data type must
be `fixdt(0,k,p)`, where *k* is less than or equal
to 16 and *p* is equal to *k* - 1.

#### Dependencies

To enable this port, select the **Enable CP fraction**
parameter and set the **CP fraction source** parameter to
`Input port`.

**Data Types:** `single` | `double` | `unsigned fixed point`

### **reset** — Clear internal states scalar

Clear internal states, specified as a scalar. When this value is
`1` (true), the block stops the current calculation and clears all
internal states.

#### Dependencies

To enable this port, select the **Enable reset input port**
parameter.

**Data Types:** `Boolean`
### Output

### **data** — Demodulated output data scalar | column vector

Demodulated output data, returned as a complex-valued scalar or column vector.
Output data type is dependent on the data type of the input **data**
port.

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

Indicates valid input data, returned as a scalar.

This port is a control signal that indicates when the **data**
output port is valid. The block sets this value to `1` when the data
samples are available on the **data** output port. When you select
the **Remove DC subcarrier** parameter, this value is set to
`0` at the center of the output samples to exclude the DC
carrier.

**Data Types:** `Boolean`

### **ready** — Indicates block is ready scalar

Control signal that indicates when the block is ready for new input data. When
this value is `1`, the block accepts input data in the next time
step. When this value is `0`, the block ignores input data in the
next time step.

#### Dependencies

To enable this port, set the **OFDM parameters source**
parameter to `Input port`.

**Data Types:** `Boolean`

## Parameters

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
**numLgSc**, **numRgSc** input ports and the
**Maximum FFT length** parameter. The **Maximum
FFT length** parameter sets the upper bound of the range of valid values
for the **FFTLen** input port.

### **Maximum FFT length** — Maximum length of FFT length `64` (default) | power of 2 in range from 8 to 65,536

Specify the maximum length of the FFT.

#### Dependencies

To enable this parameter, set the **OFDM parameters source**
parameter to `Input port`.

### **FFT length** — Length of FFT `64` (default) | power of 2 in range from 8 to 65,536

Specify the FFT length. When you set the **OFDM parameters
source** parameter to `Property`, the block uses
this FFT length value as the maximum FFT length.

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

### **Enable CP fraction** — CP fraction enabler `off` (default) | `on`

Select this parameter to enable the CP fraction either through
`Property` or through `Input
port`.

### **CP fraction source** — CP fraction source type `Property` (default) | `Input port`

You can set CP fraction with an input port or by selecting a value for the
parameter.

Select `Property` to enable the **CP
fraction** parameter.

Select `Input port` to enable the
**CPFraction** input port.

#### Dependencies

To enable this parameter, select the **Enable CP fraction**
parameter.

### **CP fraction** — Percent of cyclic prefix to remove `0.55` (default) | range from 0 to 1

Cyclic prefix fraction, specified as a value from 0 to 1, inclusive. This
parameter specifies the percentage of CP samples that the block removes from the start
of the OFDM symbol. The block shifts the remaining CP samples to the end of the OFDM
symbol.

When this parameter is `0.55`, the block removes 55% of the CP
from the beginning of the symbol, and shifts 45% to the end of the symbol. When you
set this parameter to `1`, the block removes 100% of the CP from the
start of the OFDM symbol, and does not shift any samples to the end.

#### Dependencies

To enable this parameter, select the **Enable CP fraction**
parameter and the set the **CP fraction source** parameter to
`Property`.

### **Remove DC subcarrier** — Exclude or include DC subcarrier `on` (default) | `off`

When you select this parameter, the block excludes the DC subcarrier in the output
by setting the output valid signal to `0` for the center of the
output subcarriers.

### **Enable reset input port** — Reset signal `off` (default) | `on`

Select this parameter to enable the **reset** input port.

### FFT Parameters

### **Divide butterfly outputs by two** — Divide FFT butterfly outputs by two `off` (default) | `on`

This parameter controls the scaling option of the FFT
 block inside the OFDM Demodulator block.

When you select this parameter, the FFT implements an overall
1/*N* scale factor by dividing the output of each butterfly
multiplication by two. This adjustment keeps the output of the FFT in the same
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

**Introduced in R2019b**

### R2023a: CP fraction as input port

You can now specify the CP fraction through port. To enable this port, select the
**Enable CP fraction** parameter and set the **CP fraction
source** parameter to `Input port`.

## Description

Demodulate time-domain OFDM samples and return subcarriers for custom communication protocols

The OFDM Demodulator block demodulates time-domain orthogonal frequency
division multiplexing (OFDM) samples and outputs subcarriers based on the OFDM parameters. The
block supports 5G new radio (NR) standard, long term evolution (LTE) [1], wireless local area network
(WLAN 802.11a/g/n/ac) [2], WiMAX, digital video
broadcast (DVB), and digital audio broadcast (DAB) standards.

The block accepts input data along with a valid control signal and these OFDM parameters:
FFT length, CP length, and the number of right and left guard subcarriers. The block outputs
demodulated data along with valid and ready controls signals. The block enables the **ready** output port only when these OFDM parameters are provided to the
block through input ports. The block samples the corresponding OFDM parameters only when the
**ready** port is `1` (high) and the first
**valid** port of each OFDM symbol is `1` (high).

The block supports scalar and vector inputs. You can use a vector input to increase the
data throughput and achieve a giga-sample-per-second (GSPS) throughput. The block provides an
interface and architecture suitable for HDL code generation and hardware deployment.
