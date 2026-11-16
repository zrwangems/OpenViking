---
type: simulink-block
title: 'General CRC Syndrome Detector HDL Optimized'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Error Detection and Correction / Cyclic Redundancy Check Codes'
documentation_page: 'generalcrcsyndromedetectorhdloptimized'
documentation_source_path: 'ref/generalcrcsyndromedetectorhdloptimized.html'
language: en
---

# General CRC Syndrome Detector HDL Optimized

## Ports

### Input

### **dataIn** — Input data scalar | vector

Input data, specified as one of these options.

- Scalar – Specify an integer representing several bits. For this case, the
  block supports an unsigned integer (`uint8`,
  `uint16`, or `uint32`) or
  `fixdt(0,N,0)` data type.
- Vector – Specify a vector of binary values. For this case, the block supports
  a `double` or `Boolean` data type.

The data width must be less than or equal to the CRC length, and the CRC length
must be divisible by the data width. For CRC-CCITT/CRC-16, the valid data widths are
16, 8, 4, 2, and 1.

**Example:** The `uint8` vector input `[0 0 0 1 0 0 1
1]` is equivalent to `19`.

**Data Types:** `double` | `uint8` | `uint16` | `uint32` | `fixed point` | `Boolean`

### **startIn** — Start of input frame indicator scalar

Start of input frame indicator, specified as a Boolean scalar.

**Data Types:** `Boolean`

### **endIn** — End of input frame indicator scalar

End of input frame indicator, specified as a Boolean scalar.

**Data Types:** `Boolean`

### **validIn** — Valid input data indicator scalar

Valid input data indicator, specified as a Boolean scalar.

This a control signal that indicates if the data on the **dataIn** port is valid.

**Data Types:** `Boolean`
### Output

### **dataOut** — Output data scalar | vector

Output data, returned as a scalar or vector. The output data type and size are the
same as the input data.

**Data Types:** `double` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **startOut** — Start of output frame indicator scalar

Start of output frame indicator, returned as a Boolean scalar.

**Data Types:** `Boolean`

### **endOut** — End of output frame indicator scalar

End of output frame indicator, returned as a `Boolean`
scalar.

**Data Types:** `Boolean`

### **validOut** — Valid output data indicator scalar

Valid output data indicator, returned as a Boolean scalar.

This is a control signal that indicates if the data on the **dataOut** port is valid.

**Data Types:** `Boolean`

### **err** — Error indicator scalar

Error indicator for the corruption of the received data, returned as a Boolean
scalar.

When this value is `1`, the message contains at least one error.
When this value is `0`, the message contains zero errors.

**Data Types:** `Boolean`

## Parameters

### **Polynomial** — Generator polynomial `[1 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 1]` (default) | binary vector

Specify the generator polynomial as a binary vector with coefficients in descending
order of powers. The vector length is equal to the degree of the polynomial plus
1.

### **Initial state** — Initial conditions of shift register `0` (default) | binary scalar | binary vector

Specify initial conditions of the internal shift register as a binary,
double-precision, or single-precision scalar or vector. For vector inputs, the length of
the initial state must be equal to the degree of the generator polynomial.

### **Direct method** — Method of calculating checksum `off` (default) | `on`

Specify the method of calculating checksum as a Boolean scalar.

- Select this parameter to use the direct algorithm for CRC checksum
  calculations.
- Clear this parameter to use the nondirect algorithm for CRC checksum
  calculations.

To learn about the direct and non-direct algorithms, see Cyclic Redundancy Check Codes.

### **Reflect input** — Input byte order `off` (default) | `on`

Specify the input byte order.

- Select this parameter for the block to flip each input byte before it enters the
  shift register.
- Clear this parameter for the block to pass the message data to the shift
  register unchanged.

The input data width must be a multiple of 8.

### **Reflect CRC checksum** — Checksum byte order `off` (default) | `on`

Specify the checksum byte order.

- Select this parameter for the block to flip each checksum byte before passing it
  to the final XOR stage.
- Clear this parameter for the block to pass the checksum byte to the final XOR
  stage unchanged.

The input data width must be a multiple of 8.

### **Final XOR value** — Checksum `0` (default) | binary scalar | binary vector

Specify the checksum as a binary, double-precision, or single-precision data type
scalar or vector. The block performs XOR operation on the CRC checksum with this value
before appending it to the input data.

If you specify a vector input, the vector length must be equal to the degree of the
generator polynomial.

## Libraries

Communications Toolbox HDL Support / Error Detection and Correction / CRC

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- Not recommended for production code.

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

## Version History

**Introduced in R2012b**

## Description

Detect errors in input data using CRC

The General CRC Syndrome Detector HDL Optimized block performs a cyclic
redundancy check (CRC) on data and compares the resulting checksum with the appended checksum.
The General CRC Syndrome Detector HDL Optimized block processing is optimized
for HDL code generation. If the two checksums do not match, the block reports an error.
Instead of processing an entire frame at once, the block accepts and returns a data sample
stream with accompanying control signals. The control signals indicate the validity of the
samples and the boundaries of the frame. To achieve higher throughput, the block accepts
vector data up to the CRC length and implements a parallel architecture.
