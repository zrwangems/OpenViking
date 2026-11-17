---
type: simulink-block
title: 'LTE Gold Sequence Generator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'ltegoldsequencegenerator'
documentation_source_path: 'ref/ltegoldsequencegenerator.html'
language: en
---

# LTE Gold Sequence Generator

## Ports
```yaml
ports:
- name: load
  summary: Load initial shift register value scalar
  direction: input
  data_types: Boolean
- name: init
  summary: Initial shift register value scalar | vector
  direction: input
  data_types: ufix31
- name: enable
  summary: Enable sequence generation scalar
  direction: input
  data_types: Boolean
- name: data
  summary: Generated Gold sequence scalar | vector
  direction: output
  data_types: Boolean
- name: valid
  summary: Indicates valid output data scalar
  direction: output
  data_types: Boolean
```

### Input

### **load** — Load initial shift register value scalar

When this control signal is set to `true` (1), the
block loads the value on the **init** port into the
shift register. You can use this signal to restart the sequence at any
point in time.

**Data Types:** `Boolean`

### **init** — Initial shift register value scalar | vector

Initial shift register value, specified as a `ufix31`
number representing the 31 binary values. To generate multiple Gold
sequence outputs in parallel, specify a vector of initial values to
represent multiple channels.

**Data Types:** `ufix31`

### **enable** — Enable sequence generation scalar

When this control signal is set to `true` (1), it
enables Gold sequence
generation.

**Data Types:** `Boolean`
### Output

### **data** — Generated Gold sequence scalar | vector

Generated Gold sequence, returned as a `Boolean`
scalar or vector, depending on the size of the **init**
input. If **init** is a vector, then
**data** is a vector of the same size, representing
sequences on independent channels.

**Data Types:** `Boolean`

### **valid** — Indicates valid output data scalar

Control signal that indicates when the **data**
output port is valid.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Wireless HDL Toolbox / Utilities

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

## Version History

**Introduced in R2018a**

## Description

Generate Gold sequence

The LTE Gold Sequence Generator block returns Gold sequences generated
using the polynomial and shift length specified by LTE standard TS 36.212 [1]. Gold codes are
pseudorandom sequences that have high autocorrelation and low crosscorrelation. Due to
these properties, Gold codes are widely used in communications systems. For example,
they are used to separate different mobile cells operating on the same frequency. LTE
systems use a Gold sequence generator for reference symbols and for
scrambling/descrambling data, such as in MIB and SIB coding and decoding.

This block provides minimal latency by implementing the shift register initialization
in parallel.

Use the **load** control signal to indicate when the
**init** value is valid. Use the **enable**
control signal to request the next Gold sequence value. The **valid**
signal indicates when an output sample is available. The first output sample is ready
three cycles after **enable** is asserted. The
**data** and **valid** outputs follow the pattern
of the **enable** input.
