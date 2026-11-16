---
type: simulink-block
title: 'Quadrature Decoder'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Sensor Decoders'
documentation_page: 'quadraturedecoder'
documentation_source_path: 'ref/quadraturedecoder.html'
language: en
---

# Quadrature Decoder

## Ports

### Input

### **Cnt** — Quadrature encoder counter value scalar

Value that the quadrature encoder counter generates with respect to the
slit-position. The port only accepts a scalar unsigned integer based on the
**Counter size** parameter. For example, if you select
`8 bits` for **Counter size**, the input
data type must be uint8.

**Data Types:** `uint8` | `uint16` | `uint32`

### **Idx** — Quadrature encoder counter value at last index pulse scalar

Value that the quadrature encoder counter generated with respect to the
slit-position at the time of the last index pulse. The port only accepts a scalar
unsigned integer based on the **Counter size** parameter. For
example, if you select `8 bits` for **Counter
size**, the input data type must be uint8.

#### Dependencies

To enable this port, select the **External index count**
parameter.

**Data Types:** `uint8` | `uint16` | `uint32`

### **CountsPerRev** — Number of counts generated for every revolution scalar

Number of counts the quadrature encoder generates for each revolution.

**CountsPerRev** = **Encoder slits** ⨯
**Encoder counts per slit**

#### Dependencies

To enable this port, select the **Use input port for computed parameters
(run-time motor swap)** parameter.

**Data Types:** `uint8` | `uint16` | `uint32` | `single` | `double` | `fixed point`

### **1/CountsPerRev** — Inverse of the number of counts generated for every revolution scalar

Specify the inverse of the number of counts the quadrature encoder generates for
each revolution at this port. The **Data type for 1/CountsPerRev
input** parameter defines the data type of this input.

#### Dependencies

To enable this port, select the **Use input port for computed parameters
(run-time motor swap)** parameter.

**Data Types:** `single` | `double` | `fixed point`

**Note**

The data type of the input at the **Cnt** and **Idx** ports must be
identical.
### Output

### **θm** — Angular position of quadrature encoder scalar

Angular position that the block computes based on the `Cnt` and
`Idx` inputs.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Use input port for computed parameters (run-time motor swap)** — Enable `CountsPerRev` and `1/CountsPerRev` input ports `off` (default) | `on`

The block enables the `CountsPerRev` and
`1/CountsPerRev` input ports only if you select this parameter. When
you select this parameter, the block also disables the **Encoder
slits** and **Encoder counts per slits** parameters.

### **Data type for 1/CountsPerRev input** — Data type of `1/CountsPerRev` input `single` (default) | `double` | `fixed point`

Specify the data type for the `1/CountsPerRev` input. If you
specify the fixed-point data type, you can use this parameter to specify the precision
of the `1/CountsPerRev` input.

#### Dependencies

To enable this parameter, select the **Use input port for computed
parameters (run-time motor swap)** parameter.

### **Encoder slits** — Number of slits per phase `1000` (default) | scalar

The number of slits available in each phase of the quadrature encoder.

#### Dependencies

To enable this parameter, clear the **Use input port for computed
parameters (run-time motor swap)** parameter.

### **Encoder counts per slit** — Number of counts generated for every slit `4` (default) | `1` | `2`

The number of counts that the quadrature encoder generates for every slit. A count
indicates a slit position. For example, select 4 (quadrature mode) if you want the
encoder to generate four counts corresponding to 00, 10, 11, and 01 slit positions or
values. If you select the quadrature mode:

Encoder counts per revolution (post-quadrature) = **Encoder counts per
slit** ✖ **Encoder slits**

#### Dependencies

To enable this parameter, clear the **Use input port for computed
parameters (run-time motor swap)** parameter.

### **Counter size** — Size of quadrature encoder counter `16 bits` (default) | `8 bits` | `32 bits`

Counter size signifies the register size of the counter used by the processor to
count the quadrature encoder pulses. For example, when using TI’s C2000™ based hardware, it is the data type of the counter output of the
eQEP block from C2000™ Microcontroller Blockset.

### **External index count** — Enable `Idx` input port `on` (default) | `off`

The block enables the **Idx** input port only if you select this
parameter. The **Idx** input port expects a value equal to
**Cnt** at the time of index pulse.

### **Position unit** — Unit of angular position output `Radians` (default) | `Degrees` | `Per unit`

Unit of the angular position output.

### **Position data type** — Data type of angular position output `single` (default) | `double` | `fixed point`

The data type for the angular position output.

**Note**

The Quadrature Decoder block can display the warning message
`'Wrap on overflow detected'` when needed.

## Libraries

Motor Control Blockset / Sensor Decoders Motor Control Blockset HDL Support / Sensor Decoders

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

The block supports HDL code generation when you set **Position data
type** as well as the inputs **CountsPerRev** and
**1/CountsPerRev** to use identical data type (either floating point or
fixed point).

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

## Description

Compute position of quadrature encoder

The Quadrature Decoder block computes the position of the quadrature
encoder.

To calculate the angular position of the quadrature encoder (and the rotor) in either
degrees, radians, or per-unit, the block uses one of the following methods.

- Difference between current encoder counter value and encoder counter value at the
  previous index pulse (when index pulse is available).
- Current encoder counter value (when index pulse is not available).

This figure shows a quadrature encoder disk with two channels (QEPA and QEPB) and an index
pulse (QEPI):

In this example, the timer driven by the QEP increments by four for each slit:

### Equations

The block computes the angular position (in counts) of the quadrature encoder using the
`Cnt` and `Idx` block inputs:

When *Cnt ≥ Idx*:

Position count=(Cnt−Idx)

When *Cnt < Idx*:

Position count=Counts per revolution+(Cnt−Idx)

When `Cnt` (an unsigned integer) exceeds the maximum value of the
selected counter size, the block adds the necessary compensation internally.

When you clear the **External index count** checkbox, only
`Cnt` input is available, therefore:

Position count=Cnt

where:

- Position count is the angular position of the quadrature encoder in counts.
- Counts per revolution is the number of counts in one rotation cycle of the quadrature
  encoder *(Counts per revolution = Encoder slits ⨯ Encoder counts per
  slit)*.

The block computes the output **θm** as:

θm=MaxPosition×(Position countEncoder slits×Encoder counts per slit)=MaxPosition×(Position countCounts per revolution)

Where, *MaxPosition* = 360 (degrees) or 2π (radians) or 1 (per-unit),
based on the selected value of the **Position unit** parameter.
