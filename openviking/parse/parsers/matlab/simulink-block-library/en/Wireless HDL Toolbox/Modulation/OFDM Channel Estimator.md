---
type: simulink-block
title: 'OFDM Channel Estimator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'ofdmchannelestimator'
documentation_source_path: 'ref/ofdmchannelestimator.html'
language: en
---

# OFDM Channel Estimator

## Ports

### Input

### **data** — Input data subcarriers scalar

Input data subcarriers, specified as a scalar of real or complex values.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**Complex Number Support:** Yes

### **valid** — Indicates valid input data scalar

Indicates valid input data, specified as a scalar.

This port is a control signal that indicates when the sample from the
**data** input port is valid. When this value is
`1`, the block captures the values from the
**data** input port. When this value is `0`, the
block ignores the values from the **data** input port.

**Data Types:** `Boolean`

### **refData** — Reference data subcarriers scalar

Reference data subcarriers, specified as a scalar of real or complex
values.

Reference data must be a sequence of unimodular values. In a sequence of values,
*r1*,
*r2*,
*r3*…,
*r*n**, the values are
unimodular if *r*j** x
*r*j*\**
= `1`,

where:

- *j* = 1, 2, 3, …, *n*.
- *r*j*\**
  is the complex conjugate of
  *r*j**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**Complex Number Support:** Yes

### **refValid** — Indicates valid reference data scalar

Indicates valid reference data, specified as a scalar.

This port is a control signal that indicates when the sample from the
**refData** input port is valid. When this value is
`1`, the block captures the values from the
**refData** input port. When this value is `0`,
the block ignores the values from the **refData** input port.

**refValid** port values must be synchronized with
**valid** port values.

**Data Types:** `Boolean`

### **numScPerSym** — Number of valid subcarriers per OFDM symbol scalar

Number of valid subcarriers per OFDM symbol, specified as a scalar in the range
from 2 to 65,536.

To support the minimum number of subcarriers per symbol,
**numScPerSym** must be of data type
`fixdt(0,k,0)`, where *k* is
greater than or equal to 2.

#### Dependencies

To enable this port, select the **Enable averaging** parameter
or **Enable interpolation** parameter.

**Data Types:** `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### **reset** — Clear internal states scalar

Clear internal states, specified as a scalar. When this value is
`1`, the block stops the current calculation and clears all
internal states.

#### Dependencies

To enable this port, select the **Enable reset input port**
parameter.

**Data Types:** `Boolean`
### Output

### **data** — Output channel estimates scalar

Output channel estimates, returned as a scalar. The output data type is the same
as the input data.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**Complex Number Support:** Yes

### **valid** — Indicates valid output data scalar

Indicates valid output data, returned as a scalar.

This port is a control signal that indicates when the **data**
output port is valid. The block sets this value to `1` when the data
samples are available from the **data** output port.

**Data Types:** `Boolean`

## Parameters

### **Enable averaging** — Average LS estimates `off` (default) | `on`

Select this parameter to enable averaging.

### **Number of symbols to be averaged** — Number of symbols to be averaged `2` (default) | integer in range from 2 to 14

Specify the number of symbols to be averaged.

#### Dependencies

To enable this parameter, select the **Enable averaging**
parameter.

### **Enable interpolation** — Interpolate LS estimates `off` (default) | `on`

Select this parameter to enable interpolation.

### **Interpolation factor** — Interpolation factor `3` (default) | integer in range from 2 to 12

Specify the interpolation factor.

#### Dependencies

To enable this parameter, select the **Enable interpolation**
parameter.

### **Maximum number of subcarriers per symbol** — Maximum number of subcarriers per symbol `52` (default) | integer in range from 2 to 65, 536

Specify the maximum number of subcarriers per symbol.

#### Dependencies

To enable this parameter, select the **Enable averaging**
parameter or **Enable interpolation** parameter.

### **Enable reset input port** — Reset signal `off` (default) | `on`

Select this parameter to enable the **reset** port on the block
icon.

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

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

You cannot generate HDL for this block inside a Resettable Synchronous Subsystem (HDL Coder).

## Version History

**Introduced in R2020a**

## Description

Estimate channel using input data and reference subcarriers

The OFDM Channel Estimator block estimates a channel using input data and
reference subcarriers. The block accepts data subcarriers, a **valid**
control port, and **refData** and **refValid** reference
ports. The block outputs channel estimates and a **valid** control port. The
block allows you to specify the number of subcarriers to estimate for each output
symbol.

You can use this block to estimate multipath faded channels on the receiver side in
different communications standards, such as long term evolution (LTE) [1] and wireless local area
network (WLAN) [4]. To perform proper channel
estimation, the **refData** and **refValid** ports must be
synchronized with the **data** and **valid** ports,
respectively. For more information about channel estimation and reference data, see Channel Estimation (LTE Toolbox).

This block provides an interface and architecture suitable for HDL code generation and
hardware deployment.
