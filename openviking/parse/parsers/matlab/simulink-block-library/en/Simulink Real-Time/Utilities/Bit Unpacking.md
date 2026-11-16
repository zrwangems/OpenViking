---
type: simulink-block
title: 'Bit Unpacking'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'bitunpacking'
documentation_source_path: 'io_ref/bitunpacking.html'
language: en
---

# Bit Unpacking

## Ports

Not documented in R2025b.

## Parameters

### **Bit Patterns** — Select bit pattern {[0:31]} (default)

Specify bit patterns. The data type must be a MATLAB® cell array vector. The number of elements in the cell array define the
number of input ports shown by this block instance. The cell array elements must be of
type double array and define the position of each bit of the incoming value (data typed
input port) in the outgoing double value (data frame). From a data type perspective, the
block behaves like a Sink block. The **Input port (packed) data types**
specify the data type of the input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BitPatterns` |

### **Input port (packed) data types** — Packed data type `uint32` (default) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `boolean`

From the list, select an input port (packed) data type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PackDataType` |

### **Input port (packed) dimension** — Packed data dimension [1] (default)

Specify the dimensions of the input port (packed). Enter this value as a vector.
Specify the size of the port by using a format compatible with the MATLAB
`size` command.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PackDataSize` |

### **Output port (unpacked) data types (cell array)** — Unpacked data type `{'uint32'}` (default)

The output ports (packed) can be of an arbitrary data type. The number of elements
in the cell array define the number of output ports shown by this block instance. The
data types are:

- `double`
- `single`
- `int8`
- `uint8`
- `int16`
- `uint16`
- `int32`
- `uint32`
- `boolean`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UnpackDataTypes` |

### **Output port (unpacked) dimension (cell array)** — Unpacked data dimension {[1]} (default)

Specify the dimensions of each output port (unpacked). Enter this value as a cell
array of vector sizes.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UnpackDataSizes` |

### **Sign extend** — Enable sign extension `on` (default) | `off`

Select this check box to enable sign extension. If you select this check box and
unpack the data frame into a signed type (`int8`,
`int16`, or `int32`), the block performs sign
extension. For example, if the bit pattern is `[0:4]`, and the data
type is `int8`, you are extracting 5 bits into an 8-bit wide signed
type. In this case, bits 5, 6, and 7 are the same as bit 4, resulting in sign extension.
This functionality enables you to pack and unpack negative numbers without losing
precision.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SignExtend` |

## Libraries

Simulink Real-Time / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2006a**

## Description

Deconstruct data frames

The Bit Unpacking block extracts data frames. Its input port is typically
connected to an output port of a Receive block or Digital Input block.

The block has one input port, which represents the data frame entity from which the
signals are extracted and leaving the block at its output ports. The number of output ports
and the data type of each output port depend on the settings in the block dialog box.

### Bit Unpack Four Bytes

This example shows how to configure a Bit Upacking block to:

- Receive a 32-bit word as input by using input port data type
  `uint32`.
- Unpack four 8-bit words (bytes) from the input data by using a bit pattern.
- Send four 8-bit words as output by using the output data type
  `uint8`.

Configure the block by using the Bit Unpacking block parameters dialog box.

After configuring the block parameters, the Bit Upacking block appears as
shown.

This Bit Unpacking block is configured to have four byte-wide outputs.
