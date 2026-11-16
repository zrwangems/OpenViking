---
type: simulink-block
title: 'GMSK Modulator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized System Design / Modulation'
documentation_page: 'gmskmodulator'
documentation_source_path: 'ref/gmskmodulator.html'
language: en
---

# GMSK Modulator

## Ports

### Input

### **data** — Data bits scalar

Data bits, specified as a Boolean scalar or `ufix1`.

For HDL code generation, the input data type must be `ufix1` or
`Boolean` and the maximum output word length the block supports is
16 bits.

**Data Types:** `Boolean` | `fixdt(0,1,0)`

### **valid** — Indicates valid input data scalar

Indicates valid input data, specified as a Boolean scalar.

This port is a control signal that indicates when the sample from the
**data** input port is valid. When this value is
`1`, the block captures the values on the **data**
input port. When this value is `0`, the block ignores the values on
the **data** input port.

**Data Types:** `Boolean`

### **reset** — Clear internal states scalar

Clear internal states, specified as a Boolean scalar. When this value is
`1`, the block stops the current calculation and clears all
internal states.

#### Dependencies

To enable this port, select the **Enable reset input port**
parameter.

**Data Types:** `Boolean`
### Output

### **data** — Modulated complex output data symbols complex scalar | complex column vector

Modulated complex output data symbols, returned as a complex-valued scalar or
column vector.

- When you set the **Output type** parameter to
  `Vector`, the output is a vector of number of samples
  per symbol.
- When you set the **Output type** parameter to
  `Scalar`, the output is a scalar.

**Data Types:** `signed fixed point`
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

#### Dependencies

To enable this port, set the **Output type** parameter to
`Scalar`.

**Data Types:** `Boolean`

## Parameters

### Main

### **Bandwidth time product** — Product of the bandwidth and symbol time for the Gaussian pulse shape `0.3` (default) | positive scalar value

Product of the signal bandwidth and symbol time for the Gaussian pulse shape,
specified as a positive scalar value.

### **Pulse length** — Pulse length `8` (default) | positive integer in the range from 1 to 16

Pulse length, specified as a positive integer. The pulse length value represents
the length of the Gaussian pulse shape in symbol intervals.

### **Symbol prehistory** — Symbol prehistory `1` (default) | `-1` | vector of –1s or 1s with length equal to *L* – 1

Symbol prehistory, specified as a scalar or vector of –1s or 1s that the block
uses before the start of the simulation.

- For a scalar value, the block expands it to a vector of length
  *L* – 1, where *L* represents the pulse
  length. You can specify the *L* value using the **Pulse length** parameter.

  For example, if you specify a scalar value `-1` and
  if the **Pulse length** parameter is set to
  `4`, the block expands this value as `[-1
  -1 -1]`.
- For a vector value, the block considers the elements in the vector in a
  reverse chronological order. The vector length must be *L* –
  1.

  For example, if you specify a vector value `[-1 1
  1]` and if the **Pulse length**
  parameter is set to `4`, the block considers this value
  as `[1 1 -1]`.

### **Phase offset (rad)** — Phase offset of modulated waveform `0` (default) | numeric scalar in the range from -2\*π to 2\*π.

Phase offset of the modulated waveform in radians, specified as a numeric scalar
in the range from –2\*π to 2\*π.

### **Number of samples per symbol** — Number of samples per symbol `4` (default) | in the range 1 to 64

Number of samples per symbol, specified as a positive integer in the range 1 to
64. The number of samples per symbol represents the upsampling factor from input
samples to output samples.

### **Number of data points** — Number of data points `1024` (default) | positive integer within the range 65,536 and a power of 2

Number of data points to retrieve from the look-up table (LUT), specified as a
positive integer and a power of 2. The maximum value the block supports is
65,536.

### **Output type** — Output type `Vector` (default) | `Scalar`

Specify the output type as `Vector` or
`Scalar`.

### Data Type

### **Output word length** — Output word length `16` (default) | positive scalar value with word length less than 16

Output word length, specified as a positive scalar with word length less than
16.

### Control Port

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

**Introduced in R2024a**

## Description

Modulate data bits using Gaussian minimum shift keying (GMSK) method

The GMSK Modulator block modulates data bits using the Gaussian minimum
shift keying (GMSK) method. The block supports scalar inputs and outputs modulated
complex-valued scalar or column-vector data symbols along with valid and ready controls
signals. The block enables you to use your bandwidth more effectively and helps reduce the
problems caused by multipath fading and signal distortion.

You can use this block in applications such as global system for mobile communications
(GSM), satellite communications, Bluetooth, military communications, tactical radios, drone
control/command and missile communications. The block provides an interface and architecture
suitable for HDL code generation and hardware deployment.
