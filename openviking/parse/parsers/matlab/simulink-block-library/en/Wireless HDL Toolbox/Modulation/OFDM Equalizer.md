---
type: simulink-block
title: 'OFDM Equalizer'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'ofdmequalizer'
documentation_source_path: 'ref/ofdmequalizer.html'
language: en
---

# OFDM Equalizer

## Ports

### Input

### **data** — OFDM data scalar

OFDM data, specified as a complex-valued scalar.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`

### **hEst** — Channel estimated data scalar

Channel estimated data, specified as a complex-valued scalar.

The input data type must be
`fixdt(1,k,m)`, where
*k* is less than or equal to 30, and *m* is less
than *k*.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `single` | `double` | `int8` | `int16` | `fixed point`

### **valid** — Control to indicate valid input data scalar

Control to indicate valid input data, specified as a Boolean scalar.

This port is a control signal that indicates when the input
**data** and **hEst** port values are valid. When
this value is `1`, the block captures the values from the
**data** and **hEst** input ports. When this value
is `0`, the block ignores the values on the **data**
and **hEst** input ports.

**Data Types:** `Boolean`

### **hEstLen** — Length of estimated channel per symbol scalar

Length of the estimated channel per symbol, specified as a scalar in the range
from 2 to 65,536.

To support the minimum number of subcarriers per symbol, this data type must be
`fixdt(0,k,0)`, where *k* is
greater than or equal to 2.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **loadhEst** — Channel estimates control scalar

Channel estimates control, specified as a Boolean scalar.

When this value is `1`, the block loads the channel estimates
until the length of the channel estimate specified by the **hEstLen**
input port. **hEstLen** is sampled at
**loadhEst**.

When this value is `0`, and the input is `1`,
the block performs equalization with the previously sampled
**hEstLen** input and the stored **hEst** input
values. If the previously sampled **hEstLen** value is not available,
the block performs equalization with the instantaneous inputs
**data**, **hEst**, and **nVar**.
For more information, see Algorithms.

**Data Types:** `Boolean`

### **nVar** — Noise variance scalar

Noise variance, specified as a scalar.

When the input **valid** is `1`, the block
samples the **nVar** port. This value must be of data type
`fixdt(0,k,m)`, where
*k* is less than or equal to 16, and *m* is less
than or equal to *k*.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

#### Dependencies

To enable this port, set the **Equalization method** parameter
to `MMSE`.

**Data Types:** `single` | `double` | `uint8` | `uint16` | `fixed point`

### **reset** — Reset internal states scalar

Reset internal states of the block to start with new data, specified as a
scalar.

#### Dependencies

To enable this port, select the **Enable reset input port**
parameter.

**Data Types:** `Boolean`
### Output

### **data** — Complex output data scalar

Complex output data, returned as a scalar. The output data type is the same as the
input data type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`

### **valid** — Indicates valid output data scalar

Indicates valid output data, returned as a Boolean scalar.

This port is a control signal that indicates when the **data**
output port is valid. When the data samples are available on the
**data** output port, the block sets this output
**valid** value to `1`.

**Data Types:** `Boolean`

## Parameters

### **Equalization method** — Equalization method `ZF` (default) | `MMSE`

Select the equalization method. For more information about the equalization methods,
see Algorithms.

### **Maximum length of channel estimate per symbol** — Maximum length of channel estimate per symbol `52` (default) | integer in the range from 2 to 65, 536

Specify the maximum length of the channel estimate per symbol.

To support the minimum number of subcarriers per symbol, which is 2, the data type
of the **hEstLen** input must be
`fixdt(0,k,0)`, where *k* is
greater than or equal to 2.

### **Enable reset input port** — Reset signal `off` (default) | `on`

Select this parameter to enable the **reset** input port.

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

**Introduced in R2021a**

## Description

Equalize OFDM data using channel estimates

The OFDM Equalizer block equalizes the OFDM data using channel estimates.
The block supports zero-forcing (ZF) and minimum mean squared error (MMSE) algorithms for
channel equalization in the frequency domain. The block accepts data symbols, estimated
channel (**hEst**), and the estimated channel length per symbol
(**hEstLen**) data ports and **valid** and
**loadhEst** control ports. The block outputs an equalized data port and a
**valid** control port.

You can use this block to equalize channel effects in different communications standards,
such as long term evolution (LTE) [1], 5G new radio (NR) standard
TS 38.212 [2], and wireless local area
network (WLAN) [3].

The block provides an interface and architecture suitable for HDL code generation and
hardware deployment.
