---
type: simulink-block
title: 'LTE OFDM Demodulator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized System Design / Modulation'
documentation_page: 'lteofdmdemodulator'
documentation_source_path: 'ref/lteofdmdemodulator.html'
language: en
---

# LTE OFDM Demodulator

## Ports

### Input

### **data** — Input data scalar

Input data, specified as a signed real or complex number.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**Complex Number Support:** Yes

### **valid** — Indicates valid input data `Boolean` scalar

Control signal that indicates when the sample from the
**data** input port is valid. When this value is
`1` (true), the block captures the values on the
**data** input port. When this value is
`0` (false), the block ignores the input
**data** samples.

**Data Types:** `Boolean`

### **NDLRB** — Number of downlink resource blocks `6` | `15` | `25` | `50` | `75` | `100`

Number of downlink resource blocks, specified as `6`,
`15`, `25`, `50`,
`75`, or `100`. NDLRB must be one
of these six values specified by LTE standard TS 36.212 [1].
The block samples this port at the start of each subframe and ignores
any changes within a subframe.

#### Dependencies

To enable this port, set the **NDLRB source**
parameter to `Input port`.

**Data Types:** `uint8` | `uint16` | `uint32` | `fixdt(0,K,0), K >= 7` | `single` | `double`

### **cyclicPrefixType** — Type of CP scalar

Type of CP, specified as a `Boolean` scalar. When this value is
`0` (false), the block selects normal CP. When this value is
`1` (true), the block selects extended CP. The block samples this
port at the start of each subframe and ignores any changes within a subframe.

#### Dependencies

To enable this port, set the **Cyclic prefix source** parameter
to `Input port`.

**Data Types:** `Boolean`

### **reset** — Clear internal states scalar

Clears internal state, specified as a `Boolean`
scalar. When this value is `1` (true), the block stops
the current calculation and clears all internal states. When this value
is `0` (false), and the **valid**
input value is `1` (true), the block begins a new
subframe.

#### Dependencies

To enable this port, select the **Enable reset input
port** parameter.

**Data Types:** `Boolean`
### Output

### **data** — Output data scalar

Output data, returned as a signed real or complex number. The data
type is the same as the data type of the input **data**
port. When you clear the **Divide butterfly outputs by
two** parameter, the output word length increases by 11
bits to avoid overflow.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**Complex Number Support:** Yes

### **valid** — Indicates valid output data scalar

Control signal that indicates when the **data**
output port is valid. The block sets this value to `1`
(true) when the resource grid samples are available on the
**data** output port. When **Remove DC
subcarrier** is selected, this value is set to
`0` (false) at the center of the output samples to
exclude the DC carrier.

**Data Types:** `Boolean`

### **ready** — Indicates block is ready scalar

Control signal that indicates when the block is ready for new input
data. When this value is `1` (true), the block accepts
input data in the next time step. When this value is
`0` (false), the block ignores input data in the
next time step.

#### Dependencies

To enable this port, set the **Input data sample
rate** parameter to `Match input data
sample rate to NDLRB`.

**Data Types:** `Boolean`

## Parameters

### Main

### **NDLRB source** — Source of NDLRB `Property` (default) | `Input port`

You can set NDLRB with an input port or by selecting a value for the
parameter. To enable the **NDLRB** parameter, select
`Property`. To enable the
**NDLRB** port, select `Input
port`.

### **NDLRB** — Number of downlink resource blocks `6` (default) | `15` | `25` | `50` | `75` | `100`

Number of downlink resource blocks, specified as `6`,
`15`, `25`, `50`,
`75`, or `100`. NDLRB must be one
of these six values specified by LTE standard TS 36.212 [1].

#### Dependencies

To enable this parameter, set the **NDLRB
source** parameter to
`Property`.

### **Cyclic prefix source** — Source of cyclic prefix type `Property` (default) | `Input port`

You can set the cyclic prefix by selecting a parameter value or using
an input port. To enable the **Cyclic prefix type**
parameter, select `Property`. To enable the
**cyclicPrefixType** port, select
`Input port`.

### **Cyclic prefix type** — Type of cyclic prefix `Normal` (default) | `Extended`

Type of cyclic prefix, specified as `Normal`
or `Extended`.

#### Dependencies

To enable this parameter, set the **Cyclic prefix
source** parameter to
`Property`.

### **CP fraction** — Percent of cyclic prefix to remove `0.55` (default) | value from 0 to 1

Cyclic prefix fraction, specified as a value from 0 to 1, inclusive.
This parameter specifies the percentage of CP samples that the block
removes from the start of the OFDM symbol. The block shifts the
remaining CP samples to the end of the OFDM symbol.

When this parameter is `0.55`, the block removes 55%
of the CP from the beginning of the symbol, and shifts 45% to the end of
the symbol. When you set this parameter to `1`, the
block removes 100% of the CP from the start of the OFDM symbol, and does
not shift any samples to the end.

**CP fraction** provides windowed LTE transmission
support. When a transmitter applies windowing, symbols are cyclically
extended and overlapped. In a receiver design, the best location to
remove the prefix and extract the symbol depends on windowing settings
at the transmitter. For more information on windowing for an LTE
transmitter, see the Algorithms section of `lteOFDMModulate` (LTE Toolbox)
function.

### **Remove DC subcarrier** — Exclude or include DC subcarrier `off` (default) | `on`

When you select this parameter, the block excludes the DC subcarrier
in the resource grid output. The DC subcarrier is present at the center
of the 12×NDLRB subcarriers. The block excludes the DC subcarrier by
setting the **valid** signal low
(`false`) for the center cycle of the output
subcarriers.

### **Enable reset input port** — Reset signal `off` (default) | `on`

Select this parameter to enable the **reset** port on
the block icon.

### **Input data sample rate** — Input sample rate `Use maximum input data sample rate` (default) | `Match input data sample rate to NDLRB`

This parameter specifies the type of sample rate to select for the
input data.

- To provide an input data sample rate of 30.72 MHz, select
  `Use maximum input data sample
  rate`.
- To provide an input data sample rate based on the
  **NDLRB** parameter, select
  `Match input data sample rate to
  NDLRB`. The input sampling rates for
  **NDLRB** values `6`,
  `15`, `25`,
  `50`, `75`, and
  `100` are 1.92 MHz, 3.84 MHz, 7.68 MHz,
  15.36 MHz, 30.72 MHz, and 30.72 MHz, respectively.

For more information, see Data Rate Controller.

### FFT Parameters

### **Divide butterfly outputs by two** — Divide FFT butterfly outputs by two `off` (default) | `on`

This parameter controls the scaling option of the FFT block inside the
LTE OFDM Demodulator.

When you select this parameter, the FFT implements an overall
1/*N* scale factor by dividing the output of each
butterfly multiplication by two. This adjustment keeps the output of the
FFT in the same amplitude range as its input. If you disable this
parameter, the block avoids overflow by increasing the word length by
one bit after each butterfly multiplication.

### **Rounding Method** — Rounding mode for internal fixed-point calculations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

This parameter specifies the type of rounding mode for internal
fixed-point calculations. For more information about rounding modes, see
Rounding
Modes. When the input is any integer data type or fixed-point
data type, the FFT algorithm uses fixed-point arithmetic for internal
calculations. This parameter does not apply when the input is of data
type `single` or `double`. Rounding
applies to twiddle-factor multiplication and scaling operations.

## Libraries

Wireless HDL Toolbox / Modulation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink® accelerator and rapid accelerator modes and for DPI component generation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

You cannot generate HDL for this block inside a Resettable Synchronous
Subsystem (HDL Coder).

## Version History

**Introduced in R2018a**

## Description

Demodulate time-domain OFDM samples and return LTE resource grid

The LTE OFDM Demodulator block implements an algorithm for demodulating
LTE signals specified by LTE standard TS 36.212 [1]. The block returns
the LTE resource grid that is used for cell ID detection,
master information block (MIB) recovery, system information
block (SIB)1 recovery, and further decoding.

You can select the number of downlink resource blocks (NDLRB) and choose either normal
or extended cyclic prefix (CP), as described in the LTE standard. The block implements a
CP fraction to support windowed LTE transmission and provides a parameter to configure
the location of prefix removal.

The block provides an interface and architecture suitable for HDL code generation and
hardware deployment.

The block accepts input data either at maximum rate of 30.72 MHz, or at a sample rate
corresponding to NDLRB. The input sampling rates for NDLRB 6, 15, 25, 50, 75, and 100
are 1.92 MHz, 3.84 MHz, 7.68 MHz, 15.36 MHz, 30.72 MHz, and 30.72 MHz, respectively. The
block uses a 2048-point fast fourier transform (FFT) for all values of NDLRB and returns
the number of resource grid samples needed for the selected NDLRB. By default, the block
excludes the direct current (DC) carrier.

The latency from the first input sample to the first output sample depends on your
selection of the NDLRB and type of cyclic prefix, as shown in this table.

|  | Maximum Sample Rate | | Corresponding to NDLRB Sample Rate | |
| --- | --- | --- | --- | --- |
| NDLRB | Latency — Normal CP | Latency — Extended CP | Latency — Normal CP | Latency — Extended CP |
| 6 | 5295 | 5647 | 6654 | 6676 |
| 15 | 5241 | 5593 | 6520 | 6564 |
| 25 | 5181 | 5533 | 6660 | 6748 |
| 50 | 5031 | 5383 | 6700 | 6876 |
| 75 | 4881 | 5233 | 6930 | 7282 |
| 100 | 4731 | 5083 | 6780 | 7132 |
