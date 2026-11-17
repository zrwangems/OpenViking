---
type: simulink-block
title: 'LTE OFDM Modulator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'lteofdmmodulator'
documentation_source_path: 'ref/lteofdmmodulator.html'
language: en
---

# LTE OFDM Modulator

## Ports
```yaml
ports:
- name: data
  summary: Input data scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | signed fixed point
- name: valid
  summary: Indicates valid input data scalar
  direction: input
  data_types: Boolean
- name: NDLRB
  summary: Number of downlink resource blocks 6 | 15 | 25 | 50 | 75 | 100
  direction: input
  data_types: uint8 | uint16 | uint32 | fixdt(0,K,0), K >= 7 | single | double
- name: cyclicPrefixType
  summary: Type of CP scalar
  direction: input
  data_types: Boolean
- name: reset
  summary: Clears internal states scalar
  direction: input
  data_types: Boolean
- name: data
  summary: Output data scalar
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

### **data** — Input data scalar

Input data, specified as a signed real or complex number.
`double` and `single` data types
are supported for simulation, but not for HDL code generation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**Complex Number Support:** Yes

### **valid** — Indicates valid input data scalar

Control signal that indicates if the data from the
**data** input port is valid. When this value is
`1` (`true`), the block captures
the value on the **data** input port. When this value
is `0` (`false`), the block ignores
the values on the **data** input port.

**Data Types:** `Boolean`

### **NDLRB** — Number of downlink resource blocks `6` | `15` | `25` | `50` | `75` | `100`

Number of downlink resource blocks, specified as `6`,
`15`, `25`, `50`,
`75`, or `100`. The NDLRB must be
one of these six values specified by LTE standard TS 36.212 [1].
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

### **reset** — Clears internal states scalar

Clears internal states, specified as a `Boolean`
scalar. When this value is `1`
(`true`), the block stops the current calculation and
clears all internal states. When this value is `0`
(`false`) and the **valid** input
value is `1` (`true`), the block
begins a new subframe.

#### Dependencies

To enable this port, select the **Enable reset input
port** parameter.

**Data Types:** `Boolean`
### Output

### **data** — Output data scalar

Output data, returned as a signed real or complex number. The data
type is the same as the data type of the **data** input
port. When you clear the **Divide butterfly outputs by
two** parameter, the word length increases by 1 bit per
stage in inverse fast fourier transform (IFFT).

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**Complex Number Support:** Yes

### **valid** — Indicates valid output data scalar

Control signal that indicates if the data from the
**data** output port is valid. The block sets this
value to `1` (`true`) when the
modulated samples are available on the **data** output
port.

**Data Types:** `Boolean`

### **ready** — Indicates block is ready scalar

Control signal that indicates that the block is ready for new input
data. When this value is `1` (`true`),
the block accepts input data in the next time step. When this value is
`0` (`false`), the block ignores
input data in the next time step.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: NDLRB source
  summary: Source of NDLRB Property (default) | Input port
  group: Main
- name: NDLRB
  summary: Number of downlink resource blocks 6 (default) | 15 | 25 | 50 | 75 | 100
  group: Main
- name: Cyclic prefix source
  summary: Source of cyclic prefix Property (default) | Input port
  group: Main
- name: Cyclic prefix type
  summary: Type of cyclic prefix Normal (default) | Extended
  group: Main
- name: Windowing
  summary: Spectral growth reduction off (default) | on
  group: Main
- name: Window length per NDLRB
  summary: NDRLB window length [4, 6, 4, 6, 8, 8] (default) | row vector of NDLRB window lengths
  group: Main
- name: Enable reset input port
  summary: Reset signal off (default) | on
  group: Main
- name: Output data sample rate
  summary: Output sample rate Use maximum output data sample rate (default) | Match output data sample rate to NDLRB
  group: Main
- name: Divide butterfly outputs by two
  summary: Bit-width control on (default) | off
  group: IFFT Block Parameters
- name: Rounding Method
  summary: Rounding mode for internal fixed-point calculations Floor (default) | Ceiling | Convergent | Nearest | Round |
    Zero
  group: IFFT Block Parameters
```

### Main

### **NDLRB source** — Source of NDLRB `Property` (default) | `Input port`

You can set the NDLRB by selecting a parameter value or using an input
port. To enable the **NDLRB** parameter, select
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

### **Cyclic prefix source** — Source of cyclic prefix `Property` (default) | `Input port`

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

### **Windowing** — Spectral growth reduction `off` (default) | `on`

Select this parameter to perform a windowing operation that reduces
spectral growth and uses the NDRLB window length specified by the
**Window length per NDLRB** parameter. Clear this
parameter to disable windowing operation.

### **Window length per NDLRB** — NDRLB window length [`4, 6, 4, 6, 8, 8`] (default) | row vector of NDLRB window lengths

NDRLB window length, specified as a row vector of nonnegative integers
whose elements correspond to the window lengths for NDRLB
`6`, `15`, `25`,
`50`, `75`, and
`100` respectively. By default, the window lengths
for NDRLB 6, 15, 25, 50, 75, and 100 are 4, 6, 4, 6, 8, and 8,
respectively. The window length for each NDLRB can range from 0 to the
minimum CP value.

- For normal CP, the minimum CP values for NDRLB
  `6`, `15`,
  `25`, `50`,
  `75`, and `100` are 9, 18,
  36, 72, 144, and 144, respectively.
- For extended CP, the minimum CP values for NDRLB
  `6`, `15`,
  `25`, `50`,
  `75`, and `100` are 32,
  64, 128, 256, 512, and 512, respectively.

#### Dependencies

To enable this parameter, select the
**Windowing** parameter.

### **Enable reset input port** — Reset signal `off` (default) | `on`

Select this parameter to enable the **reset** port on
the block icon.

### **Output data sample rate** — Output sample rate `Use maximum output data sample rate` (default) | `Match output data sample rate to NDLRB`

This parameter specifies the type of sample rate for the block to
select for the output data.

- To provide an output data sample rate of 30.72 MHz, select
  `Use maximum output data sample
  rate`.
- To provide an output data sample rate based on the
  **NDLRB** parameter, select
  `Match output data sample rate to
  NDLRB`. The output sampling rates for NDLRB
  `6`, `15`,
  `25`, `50`,
  `75`, and `100` are
  1.92 MHz, 3.84 MHz, 7.68 MHz, 15.36 MHz, 30.72 MHz, and
  30.72 MHz, respectively.

For more information, see Base Rate Controller.

### IFFT Block Parameters

### **Divide butterfly outputs by two** — Bit-width control `on` (default) | `off`

When you select this parameter, the IFFT block in the
LTE OFDM Modulator block implements an overall
1/*N* scale factor by dividing the output of each
butterfly multiplication by two. This adjustment keeps the output of the
IFFT block in the same amplitude range as its input. If you disable this
parameter, the block avoids overflow by increasing the word length by 1
bit after each butterfly multiplication.

### **Rounding Method** — Rounding mode for internal fixed-point calculations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

This parameter specifies the type of rounding mode for internal
fixed-point calculations. Rounding applies to twiddle-factor
multiplication and scaling operations. For more information about
rounding modes, see Rounding
Modes.

When the input is any integer or fixed-point data type, the IFFT
algorithm uses fixed-point arithmetic for internal calculations. This
parameter does not apply when the input data is of data type
`single` or `double`.
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

**Introduced in R2019a**

## Description

Modulate LTE resource grid and return time-domain OFDM samples

The LTE OFDM Modulator block implements an algorithm for modulating LTE
resource grid samples specified by LTE standard TS 36.212 [1]. The block uses an
orthogonal frequency-division multiplexing (OFDM) mechanism in its operation and
converts the resource grid input samples to an equivalent time-domain signal output.
OFDM is effective for communication over channels with high-frequency selectivity and is
widely used in the development of the LTE downlink transmitter. The block implements a
windowing feature to reduce the spectral regrowth, or adjacent channel leakage ratio
(ACLR), of an OFDM signal.

The block provides an interface and architecture suitable for HDL code generation and
hardware deployment.

You can select the number of downlink resource blocks (NDLRB) and choose either normal
or extended cyclic prefix (CP), as described in the LTE standard. The latency from the
first input sample to the first output sample depends on your selection of the
NDLRB.

| NDLRB | Latency |
| --- | --- |
| 6 | 6268 |
| 15 | 6376 |
| 25 | 6496 |
| 50 | 6796 |
| 75 | 7096 |
| 100 | 7396 |
